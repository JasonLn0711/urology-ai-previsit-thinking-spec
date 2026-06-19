# 健康台灣深耕計畫 KPI / 預算 / 年度 Checkpoint 整合表

狀態：2026-06-19 AI-only v0.8 planning

目前提案包：

```text
泌尿科門診前問診與醫師覆核摘要支持系統
```

## Active Gate

```text
AI 問診 + 醫師覆核摘要 + 治理 + KPI + NT$10,000,000 budget mapping
```

CRM 已排除，不再列入本案架構、預算、KPI、資料交接或下一步討論。

## Official-Format Crosswalk

| 正式提案位置 | 本案要填什麼 | 不要混入什麼 |
| --- | --- | --- |
| 封面 | 計畫名稱、臺北市、範疇三主打 / 範疇一副支援、三年 NT$10M working budget | CRM、PSA SOP owner、院外追蹤承諾 |
| 壹、自我檢核 | 格式、簽章、資格、COI、未重複申請、參與同意待主提單位完成 | 技術內容長篇敘述 |
| 貳、計畫概要 | 門診前症狀蒐集、醫師覆核摘要、減少重複問診與缺欄補問 | AI 診斷、治療建議、CRM 追蹤 |
| 參、申請單位簡介 | 陽明交大負責 AI 問診設計、摘要 schema、治理與 evidence | 醫院 CRM 建置或病人追蹤 |
| 肆、計畫規劃 | workflow、題組、摘要、source label、missing fields、治理 | CRM-ready handoff、HIS/EMR writeback |
| 伍、效益評估 | summary read time、clinician usefulness、missing-field visibility、source label、unsafe wording | 癌症偵測率、慢病改善率、CRM 留存率 |
| 陸、出國計畫 | 預設不編列；若主提案要求再補 | 無關訓練 |
| 柒、經費規劃 | NT$10M discussion allocation and KPI mapping | CRM 預算 |
| 捌、人力配置 | proposal coordinator、clinical reviewer、engineering、AI/data governance、evaluation、budget owner | CRM operator |
| 玖、其他 | open owner questions、governance gates、review response | 未確認實施承諾 |

## KPI Architecture

| KPI | 草案目標 | Evidence | 年度 |
| --- | --- | --- | --- |
| Summary read time | <= 60 秒 design target, report actual | timed reviewer scorecard | Year 1-2 |
| Clinician usefulness | median >= 4/5 or revise | clinician scorecard | Year 1-2 |
| AI 問診 completion | >= 90% minimum fields completed or flagged | synthetic / approved walkthrough | Year 1 |
| Missing-field visibility | >= 90% key missing fields surfaced | missing-field report | Year 1 |
| Source-label completeness | 100% summary fields labeled | audit sample | Year 1 |
| Unsafe wording count | 0 diagnosis / treatment / triage / queue-priority / EMR phrases | safety checklist | Every year |
| Staff-friction review | no unacceptable duplicate entry / clicks / exception load | staff-friction worksheet | Year 1-2 |
| Governance checklist | AI/data/security/IRB-QI gates named before real-data claim | governance checklist | Year 1 |
| KPI-to-budget traceability | 100% core budget lines mapped | budget table audit | submission |

## Annual Checkpoints

| 階段 | 主要目標 | Checkpoint | Evidence |
| --- | --- | --- | --- |
| Year 1 setup | 確認範圍、題組、摘要格式與治理邊界 | intended use、question set、summary schema、safety wording | scope note、question table、summary sample |
| Year 1 reviewer evidence | 讓專家判斷是否值得寫進正式計畫 | 3-5 synthetic cases, timed summary review | scorecards、walkthrough report |
| Year 2 approved workflow evaluation | 若院內治理允許，進行 limited workflow evidence | workflow slot、staff-friction、clinician usefulness | approved protocol or QI note |
| Year 3 handoff | 完成 final evidence 與維運 / 下一階段決策 | final KPI report、maintenance owner、next-stage governance brief | final packet |

## Budget Architecture

| Budget Area | Total | Why It Exists |
| --- | ---: | --- |
| Proposal coordination、PM、RA、KPI evidence | 2,500,000 | 讓提案、KPI、年度 evidence、專家回饋可管理 |
| Clinical workflow review and reviewer sessions | 1,200,000 | 驗證醫師是否讀得完、用得上，並避免 staff burden |
| Question governance、intake flow、summary schema | 1,900,000 | 建立可驗收的問診題組與摘要結構 |
| AI 問診與摘要 prototype / implementation evidence | 1,900,000 | 支援 prototype、合成案例、audit sample 與摘要 evidence |
| AI/data/security/privacy governance | 1,000,000 | 支援範疇三所需治理可信度 |
| Evaluation、baseline、QI/IRB preparation | 1,000,000 | 支援 baseline、approved workflow evaluation 與 final report |
| Optional ASR / intake station readiness | 500,000 | 只有在 input-burden / accessibility KPI 成立時啟用 |
| Total | 10,000,000 | 目前 AI-only discussion allocation |

## Design Rule

```text
先用 NT$10M 作工作上限，但 KPI 不是由金額硬湊出來。
KPI 來自 workflow value；預算再分配到能產出 KPI evidence 的工作包。
```
