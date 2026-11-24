#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Независимый пересчёт основных показателей статьи по опубликованному набору СПО.

Установка: pip install pandas pyarrow numpy scipy
Запуск:    python reproduce_spo_article.py
Источник: ML-5 V10.2, публикация от 24.11.2026. Доступ к записи в GitHub не нужен.
"""
import hashlib
import io
import json
import pathlib
import urllib.request
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

TAG = "ml5-v102-stage2-20261124-184818730468-a50a10cc"
REPO = "AntonDozhdikov/Demograf_sovetnik"
BASE = f"https://github.com/{REPO}/releases/download/{TAG}"
FILENAME = "ML5_SCI_adc70420e1ee75.parquet"
EXPECTED_SHA256 = "3629a383dce562d8b918a3fce17c19b9d4a927833a075079cb34eff34a5424c0"
OUT = pathlib.Path("article_results")
OUT.mkdir(exist_ok=True)

req = urllib.request.Request(f"{BASE}/{FILENAME}",headers={"User-Agent":"SPO-research-reproduction/1.0"})
with urllib.request.urlopen(req, timeout=180) as response:
    payload = response.read()
actual_sha = hashlib.sha256(payload).hexdigest()
if actual_sha != EXPECTED_SHA256:
    raise RuntimeError(f"SHA-256 не совпадает: {actual_sha}")
od = pd.read_parquet(io.BytesIO(payload))
needed = {"year","origin_code","destination_code","value"}
if not needed.issubset(od.columns):
    raise RuntimeError("Нарушена схема исходного набора")
for k in ("year","origin_code","destination_code"):
    od[k] = pd.to_numeric(od[k], errors="raise").astype("int64")
od["value"] = pd.to_numeric(od["value"], errors="raise")
if len(od)!=12400 or od.duplicated(["year","origin_code","destination_code"]).any():
    raise RuntimeError("Нарушен размер панели или уникальность региональных направлений")
years = sorted(od.year.unique().tolist())
if years != [2021,2022,2023,2024,2025] or (od.groupby("year").size()!=2480).any():
    raise RuntimeError("Неполная пятилетняя панель")
regions = sorted(set(od.origin_code).union(set(od.destination_code)))
if len(regions) != 85:
    raise RuntimeError("Число регионов отличается от опубликованной спецификации")
MOSCOW, PETERSBURG = 45000000,40000000
rows, by_year = [], {}
for year, block in od.groupby("year"):
    incoming = block.groupby("destination_code")["value"].sum().reindex(regions, fill_value=0).astype(float)
    outgoing = block.groupby("origin_code")["value"].sum().reindex(regions, fill_value=0).astype(float)
    if not np.isclose(incoming.sum(),outgoing.sum()):
        raise RuntimeError(f"Нарушен региональный баланс в {year} г.")
    total = incoming.sum()
    shares = incoming / total
    remaining = incoming.drop(MOSCOW)
    without_both = incoming.drop([MOSCOW,PETERSBURG])
    by_year[int(year)]=incoming
    rows.append({"год":int(year),"постоянных_направлений":len(block),
       "сумма":int(total),"доля_Москвы":float(shares.loc[MOSCOW]),
       "доля_Санкт_Петербурга":float(shares.loc[PETERSBURG]),
       "HHI":float((shares**2).sum()),
       "HHI_без_Москвы":float(((remaining/remaining.sum())**2).sum()),
       "HHI_без_обеих_столиц":float(((without_both/without_both.sum())**2).sum()),
       "регионов_положительный_баланс":int((incoming-outgoing>0).sum())})
annual=pd.DataFrame(rows).sort_values("год")
if int(annual.loc[annual["год"]==2021,"сумма"].iloc[0])!=64189 or int(annual.loc[annual["год"]==2025,"сумма"].iloc[0])!=96487:
    raise RuntimeError("Контрольные суммы не воспроизведены")
rho=float(spearmanr(by_year[2021],by_year[2025]).statistic)
a=od[od.year==2021].set_index(["origin_code","destination_code"])["value"]
b=od[od.year==2025].set_index(["origin_code","destination_code"])["value"]
d=(b-a).sort_values(ascending=False).rename("изменение_2021_2025")
changes=d.reset_index()
changes["начало_2021"]=a.reindex(d.index).to_numpy()
changes["конец_2025"]=b.reindex(d.index).to_numpy()
all_change=float(d.sum())
moscow_change=float(d.reset_index().loc[lambda x:x.destination_code==MOSCOW,"изменение_2021_2025"].sum())
moscow_oblast_moscow=float(d.loc[(46000000,MOSCOW)])
annual.to_csv(OUT/"concentration_by_year.csv",index=False,encoding="utf-8-sig")
changes.to_csv(OUT/"changes_by_route.csv",index=False,encoding="utf-8-sig")
summary={"source_asset":FILENAME,"sha256":actual_sha,"rows":len(od),
 "per_year":annual.to_dict(orient="records"),"spearman_2021_2025":rho,
 "all_change_2021_2025":all_change,"moscow_destination_change":moscow_change,
 "moscow_share_of_total_change":moscow_change/all_change,
 "moscow_oblast_to_moscow_change":moscow_oblast_moscow,
 "moscow_oblast_to_moscow_share_of_total_change":moscow_oblast_moscow/all_change}
(OUT/"audit.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding="utf-8")
print("PASS; сумма 2025:",int(annual.iloc[-1]["сумма"]),"HHI 2025:",round(annual.iloc[-1]["HHI"],6),
      "Spearman:",round(rho,6),"Moscow growth share:",round(moscow_change/all_change,6))
