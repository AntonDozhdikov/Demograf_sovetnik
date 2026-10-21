import requests,base64,hashlib,json
from pathlib import Path
REPO="AntonDozhdikov/Demograf_sovetnik"

def digest(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for block in iter(lambda:f.read(4*1024**2),b""):h.update(block)
 return h.hexdigest()

def load_index(token):
 r=requests.get(f"https://api.github.com/repos/{REPO}/contents/handoff/07_v2/dataset_index.json",
                headers={"Authorization":"Bearer "+token},timeout=60)
 r.raise_for_status()
 return json.loads(base64.b64decode(r.json()["content"]))

def fetch_asset(asset,token,cache="/content/demograf_stage2"):
 folder=Path(cache);folder.mkdir(parents=True,exist_ok=True)
 dst=folder/(hashlib.sha256(asset["asset_id"].encode()).hexdigest()[:20]+".parquet")
 expected=asset["sha256"];loc=asset["locator"]
 api=f"https://api.github.com/repos/{REPO}"
 h={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json"}
 if dst.exists() and digest(dst)==expected:return dst
 dst.unlink(missing_ok=True)

 if loc["type"]=="git":
  r=requests.get(api+"/contents/"+loc["path"],headers=h,timeout=120)
  r.raise_for_status();obj=r.json()
  if obj.get("content"):dst.write_bytes(base64.b64decode(obj["content"]))
  else:
   rr=requests.get(api+"/contents/"+loc["path"],
                   headers={**h,"Accept":"application/vnd.github.raw+json"},
                   stream=True,timeout=(30,900))
   rr.raise_for_status()
   with open(dst,"wb") as f:
    for block in rr.iter_content(4*1024**2):
     if block:f.write(block)
   rr.close()

 else:
  u=api+"/releases/assets/"+str(loc["asset_id"])
  r=requests.get(u,headers={**h,"Accept":"application/octet-stream"},
                 stream=True,timeout=(30,900))
  r.raise_for_status()
  if "json" in r.headers.get("Content-Type","").lower():
   r.close()
   z=requests.get(u,headers=h,timeout=60);z.raise_for_status()
   r=requests.get(z.json()["browser_download_url"],headers=h,
                  stream=True,timeout=(30,900))
   r.raise_for_status()
  with open(dst,"wb") as f:
   for block in r.iter_content(4*1024**2):
    if block:f.write(block)
  r.close()

 if digest(dst)!=expected:
  dst.unlink(missing_ok=True)
  raise RuntimeError("SHA256 mismatch: "+asset["asset_id"])
 return dst

# Пример:
# idx=load_index(TOKEN)
# file=fetch_asset(next(a for a in idx["assets"] if a["segment"]=="04" and a["sha256_verified"]),TOKEN)
