# ML-1 V3: миграционная привлекательность муниципалитетов

## Фактически выполненный анализ
Исходный источник D01: 7564bcb6af322758369069273f15462ba42404e7e2aa6c1c89886e467477ed5f. Наблюдений 31445, муниципалитетов 2286, региональных групп 80; годы 2010–2023. Коэффициент приведён в человек на 1000 жителей с масштабом исходного ряда ×1000.0, проверенным на 27922 парах.

## Реальные модели и данные
Успешных метрик регрессии: 486; модельных прогнозов: 870660; 50-seed завершений: 150 из 150 запланированных. Внешних факторных индикаторов: 22, из них региональных: 6. Пространственных наборов: 0. Ошибок: 0, ограничений: 109.

## Оптимизация
Optuna/TPE, n_trials={'ridge': 3, 'elasticnet': 4, 'huber': 3, 'histgb': 4, 'catboost': 6, 'lightgbm': 6}. Вся настройка только на FIT/DEV; для рекурсивных горизонтов статус многолетнего DEV фиксируется в таблице DEV_подбор.

## Гипотезы
Подтверждающие H1–H3 сравнения выполнены на одинаковых test keys, p Holm. Поддержано: 3. H4 описывает неоднородность, H5 проверяет переносимость между режимами при условной независимости. Неисполнимые гипотезы остаются явно размеченными.

## Границы достоверности
Текущая выгрузка — ретроспективный срез; отсутствие подлинных исторических vintages ограничивает строгий backtest. Граница территории и тип уровня проверяются по доступным кодам и метаданным, полная юридическая преемственность требует архивной географии. Значимость и SHAP — прогнозные связи, не эффект миграционной политики. Отчёт не предполагает автоматически подтверждённые гипотезы без фактических тестов.

- LIMITATION: HISTORICAL_VINTAGE — One retrospective 2026 snapshot; historical data vintages and boundary continuity cannot be guaranteed
- NOT_FEASIBLE: h3_DIRECT_MODEL — Insufficient past label history for direct horizon; recursive endogenous alternative evaluated separately
- NOT_FEASIBLE: h5_DIRECT_MODEL — Insufficient past label history for direct horizon; recursive endogenous alternative evaluated separately
- NOT_FEASIBLE: ('CLASSIFY', 1, 'CROSSED', 'stable_outflow_3y', 'frequency', 0, 11) — insufficient train/test positive-negative labels: train=6911, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'CROSSED', 'stable_outflow_3y', 'logistic', 0, 11) — insufficient train/test positive-negative labels: train=6911, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'CROSSED', 'stable_outflow_3y', 'catboost_cls', 0, 11) — insufficient train/test positive-negative labels: train=6911, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'ROLLING_TIME', 'stable_outflow_3y', 'frequency', 0, 11) — insufficient train/test positive-negative labels: train=9978, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'ROLLING_TIME', 'stable_outflow_3y', 'logistic', 0, 11) — insufficient train/test positive-negative labels: train=9978, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'ROLLING_TIME', 'stable_outflow_3y', 'catboost_cls', 0, 11) — insufficient train/test positive-negative labels: train=9978, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'frequency', 0, 11) — insufficient train/test positive-negative labels: train=7721, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'logistic', 0, 11) — insufficient train/test positive-negative labels: train=7721, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'catboost_cls', 0, 11) — insufficient train/test positive-negative labels: train=7721, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'TERRITORY_ONLY', 'stable_outflow_3y', 'frequency', 0, 11) — insufficient train/test positive-negative labels: train=5299, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'TERRITORY_ONLY', 'stable_outflow_3y', 'logistic', 0, 11) — insufficient train/test positive-negative labels: train=5299, test=0
- NOT_FEASIBLE: ('CLASSIFY', 1, 'TERRITORY_ONLY', 'stable_outflow_3y', 'catboost_cls', 0, 11) — insufficient train/test positive-negative labels: train=5299, test=0
- NOT_FEASIBLE: ('CLASSIFY', 3, 'CROSSED', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'CROSSED', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'CROSSED', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'CROSSED', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'CROSSED', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'CROSSED', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME_PREV', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME_PREV', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME_PREV', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME_PREV', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'TERRITORY_ONLY', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'TERRITORY_ONLY', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'TERRITORY_ONLY', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'TERRITORY_ONLY', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'TERRITORY_ONLY', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 3, 'TERRITORY_ONLY', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'CROSSED', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'CROSSED', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'CROSSED', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'CROSSED', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'CROSSED', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'CROSSED', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME_PREV', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME_PREV', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME_PREV', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME_PREV', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'ROLLING_TIME_PREV', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'TERRITORY_ONLY', 'target_sign', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'TERRITORY_ONLY', 'target_sign', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'TERRITORY_ONLY', 'practical_outflow', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'TERRITORY_ONLY', 'practical_outflow', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'TERRITORY_ONLY', 'stable_outflow_3y', 'logistic', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: ('CLASSIFY', 5, 'TERRITORY_ONLY', 'stable_outflow_3y', 'catboost_cls', 0, 11) — No honest calibrated h-year classification training window; output available only as a deterministic flow-simulation rule
- NOT_FEASIBLE: INTERACTION/wage×housing_new — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/employment×education — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/income×neighbor_rate — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/wage×housing_new — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/employment×education — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/income×neighbor_rate — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/wage×housing_new — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/employment×education — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/income×neighbor_rate — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/wage×housing_new — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/employment×education — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/income×neighbor_rate — Required variables unavailable
- NOT_FEASIBLE: ('INTERVALS', 3, 'CROSSED', 0, 0, 0, 0) — No independent horizon-specific calibration labels before test cutoff; 1-step interval forbidden
- NOT_FEASIBLE: INTERACTION/wage×housing_new — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/employment×education — Required variables unavailable
- NOT_FEASIBLE: INTERACTION/income×neighbor_rate — Required variables unavailable
- NOT_FEASIBLE: ('INTERVALS', 3, 'ROLLING_TIME', 0, 0, 0, 0) — No independent horizon-specific calibration labels before test cutoff; 1-step interval forbidden

## Сравнение на закрытых тестах (человек на 1000 жителей)

- h=1, CROSSED: последний известный 6.4351; зафиксированная по DEV A_history/lightgbm: 5.7008; изменение ошибки +11.41%. DEV=6.2599.
- h=1, ROLLING_TIME: последний известный 6.7637; зафиксированная по DEV C_housing_services/catboost: 5.7466; изменение ошибки +15.04%. DEV=6.2320.
- h=1, ROLLING_TIME_PREV: последний известный 7.5168; зафиксированная по DEV B_economy/catboost: 6.1814; изменение ошибки +17.76%. DEV=5.9340.
- h=1, TERRITORY_ONLY: последний известный 6.9169; зафиксированная по DEV B_economy/catboost: 6.4411; изменение ошибки +6.88%. DEV=5.8736.
- h=3, CROSSED: последний известный 7.0817; зафиксированная по DEV C_housing_services/recursive_catboost: 6.0158; изменение ошибки +15.05%. DEV=6.0072.
- h=3, ROLLING_TIME: последний известный 7.4302; зафиксированная по DEV B_economy/recursive_elasticnet: 6.9005; изменение ошибки +7.13%. DEV=5.5723.
- h=3, ROLLING_TIME_PREV: последний известный 7.3135; зафиксированная по DEV E_all/recursive_catboost: 6.6247; изменение ошибки +9.42%. DEV=5.6264.
- h=3, TERRITORY_ONLY: последний известный 7.0448; зафиксированная по DEV A_history/recursive_catboost: 6.4937; изменение ошибки +7.82%. DEV=7.0239.
- h=5, CROSSED: последний известный 7.8897; зафиксированная по DEV E_all/recursive_catboost: 6.5940; изменение ошибки +16.42%. DEV=6.5370.
- h=5, ROLLING_TIME: последний известный 7.8416; зафиксированная по DEV E_all/recursive_catboost: 6.2403; изменение ошибки +20.42%. DEV=6.1288.
- h=5, ROLLING_TIME_PREV: последний известный 8.2470; зафиксированная по DEV C_housing_services/recursive_catboost: 8.0494; изменение ошибки +2.40%. DEV=5.4308.
- h=5, TERRITORY_ONLY: последний известный 8.2643; зафиксированная по DEV A_history/recursive_catboost: 7.7237; изменение ошибки +6.54%. DEV=6.1852.

## Гипотезы и множественные проверки

- H1: протоколов 12, статусы {'OK': 12}; статистически поддержано: 2.
- H2: протоколов 12, статусы {'OK': 12}; статистически поддержано: 1.
- H3: протоколов 12, статусы {'NOT_FEASIBLE': 12}; статистически поддержано: 0.

## Факторные источники (не подменять региональный показатель муниципальным)

- housing_new: Введено в действие жилых домов; код Y48010001; единица «Квадратный метр общей площади»; уровень municipality; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 5.
- housing_individual: Введено в действие индивидуальных жилых домов; код Y48010002; единица «Квадратный метр общей площади»; уровень municipality; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 5.
- housing_waitlist_families: Число семей, состоящих на учете в качестве нуждающихся в жилых помещениях; код Y48011011; единица «Единица»; уровень municipality; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 1.
- housing_improved_families: Число семей, получивших жилые помещения и улучшивших жилищные условия; код Y48011010; единица «Единица»; уровень municipality; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 1.
- preschool_count: Число организаций, осуществляющих образовательную деятельность по образовательным программам дошкольного образования, присмотр и уход за детьми; код Y48014001; единица «Единица»; уровень municipality; пересекающиеся годы 10; качество: SELECTED, конфликтных пар 0.
- preschool_capacity: Число мест в организациях, осуществляющих образовательную деятельность по образовательным программам дошкольного образования, присмотр и уход за детьми; код Y48014002; единица «Единица»; уровень municipality; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 2.
- preschool_waitlist: Численность детей, стоящих на учете для определения в дошкольные образовательные организации, на конец отчетного года; код Y48014004; единица «Человек»; уровень municipality; пересекающиеся годы 6; качество: SELECTED, конфликтных пар 0.
- school_count: Число общеобразовательных организаций на начало учебного года; код Y48015001; единица «Единица»; уровень municipality; пересекающиеся годы 8; качество: SELECTED, конфликтных пар 12.
- student_count: Численность обучающихся общеобразовательных организаций с учетом обособленных подразделений (филиалов); код Y48015002; единица «Человек»; уровень municipality; пересекающиеся годы 8; качество: SELECTED, конфликтных пар 17.
- school_branches: Число обособленных подразделений (филиалов) общеобразовательных организаций; код Y48015005; единица «Единица»; уровень municipality; пересекающиеся годы 8; качество: SELECTED, конфликтных пар 0.
- budget_balance: Профицит, дефицит (-) бюджета муниципального образования (местного бюджета), фактически исполнено; код Y48013003; единица «Тысяча рублей»; уровень municipality; пересекающиеся годы 11; качество: SELECTED, конфликтных пар 90.
- municipal_sme_support: Расходы на развитие и поддержку малого и среднего предпринимательства; код Y48013012; единица «Тысяча рублей»; уровень municipality; пересекающиеся годы 3; качество: SELECTED, конфликтных пар 0.
- budget_own_share: Доля налоговых и неналоговых доходов местного бюджета (за исключением поступлений налоговых доходов по дополнительным нормативам отчислений) в общем объеме собственных доходов бюджета муниципального образования (без учета субвенций); код Y48013015; единица «Процент»; уровень municipality; пересекающиеся годы 11; качество: SELECTED, конфликтных пар 3.
- budget_admin_cost_pc: Расходы бюджета муниципального образования на содержание работников органов местного самоуправления в расчете на одного жителя муниципального образования; код Y48013004; единица «2008 г. — тысяча рублей, с 2009 г. — рубль»; уровень municipality; пересекающиеся годы 11; качество: SELECTED, конфликтных пар 2.
- budget_revenue: Доходы местного бюджета, фактически исполненные; код Y48013001; единица «Тысяча рублей»; уровень municipality; пересекающиеся годы 11; качество: SELECTED, конфликтных пар 76.
- budget_expenditure: Расходы местного бюджета, фактически исполненные; код Y48013002; единица «Тысяча рублей»; уровень municipality; пересекающиеся годы 11; качество: SELECTED, конфликтных пар 85.
- regional_median_wage: Медианная заработная плата работников организаций; код Y477110208; единица «Без субъектов малого предпринимательства, по данным выборочных обследований, за апрель, рублей»; уровень region; пересекающиеся годы 7; качество: SELECTED, конфликтных пар 0.
- regional_employment: Среднегодовая численность занятых; код Y477170012; единица «Тысяч человек»; уровень region; пересекающиеся годы 7; качество: SELECTED, конфликтных пар 0.
- regional_wage: Среднемесячная начисленная заработная плата наёмных работников в организациях, у индивидуальных предпринимателей и физических лиц; код Y477170013; единица «Рублей»; уровень region; пересекающиеся годы 4; качество: SELECTED, конфликтных пар 0.
- regional_unemployment: Уровень безработицы; код Y477170028; единица «В процентах»; уровень region; пересекающиеся годы 5; качество: SELECTED, конфликтных пар 0.
- regional_investment_pc: Инвестиции в основной капитал на душу населения; код Y477140023; единица «В фактически действовавших ценах, рублей»; уровень region; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 0.
- regional_working_age_share: Возрастной состав населения: Население в трудоспособном возрасте; код Y477110050; единица «Оценка на конец года, в процентах от общей численности населения»; уровень region; пересекающиеся годы 14; качество: SELECTED, конфликтных пар 0.

## Оптимизация и интерпретация

- Optuna/TPE: 1054 завершенных trial, точные параметры и DEV-мера в DEV_подбор; итоговые метрики закрытого TEST не используются для выбора модели.
- Интерпретация: permutation/grouped permutation, SHAP при технической поддержке, ALE, PDP и взаимодействия. Все значения обозначают прогностические ассоциации, а не причинный эффект экономической или миграционной политики.
- Пространственная география при соответствии — только прокси по реальным поселениям; исторический административный контур и доступность этого справочника на прошлую дату не установлены.
- Для рекурсивных горизонтов экзогенные переменные заморожены на информационном срезе origin; при недостатке ранних меток многолетний DEV заменён открыто обозначенной одногодичной прокси.

## Практическая применимость
Результаты описывают прогнозную неопределённость и не допускают автоматической политики изменения миграции. Отрицательный выигрыш относительно baseline, отсутствие пригодной выборки и неустойчивые значения SHAP не удаляются из отчёта.

# ML-1 V4 — выпущенные материалы

Статус вычислений: COMPUTE_COMPLETE_WITH_LIMITATIONS.
Исходные базы не перевыпускаются. Научная приёмка независимая.

Release: https://github.com/AntonDozhdikov/Demograf_sovetnik/releases/tag/stage2-ml1-v4.0.0-20261026T130048Z-58bd8971

- ML1_V4_RESULTS.xlsx: SHA-256 26e13ba5c40d0efb0565fd8be3f92d2d6bbcf770f62fb77b043365a1d78b3e78
- ML1_V4_PREDICTIONS.xlsx: SHA-256 fe877e5fa0d65ffda2acd3f6d9cb40e3af7c1b1242d20d43b92f46710a713350
- ML1_V4_DATA_QA.xlsx: SHA-256 598864e10a5fae44640b5097fcad7cf1e4226eec0c606a8f1898967fc584a4b0
- ML1_V4_MODEL_QA.xlsx: SHA-256 92b1e498792319d7b79b0d0c6c70b61cddbb279905f7781a390d3429e1ab1f42
- ML1_V4_FIGURES.zip: SHA-256 b468f9966cecb3cd6de4f932d70460156e6695db42f17fadfc6d13f9c3cb520f