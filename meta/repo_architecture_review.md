# Repository Architecture Review

日期：2026-04-20

## First-Principles Question

這個 repo 是否仍然服務原始目的：保存泌尿科 previsit interview 的思考層、臨床題目治理、工作流推理、安全邊界與後續審查證據？

判斷：符合，但在新增臨床題目治理文件後，根目錄已開始混合不同責任類型。若不整理，下一步會出現 reviewer 找不到來源、AI agent 不知道該更新哪份文件、同一結論散落多處的風險。

## Architecture Decision

採用四個責任區：

1. `core/`：穩定系統邏輯。
2. `clinical-question-governance/`：臨床題目納入治理。
3. `discovery/`：會議、訪談、決策操作包。
4. `records/` 與 `meta/`：dated evidence、assumptions、constraints、open questions、architecture review。

這個整理沒有刪除內容，只改變檔案路由。

## Redundancy Review

| 檔案或區域 | 是否 redundant | 判斷 |
|---|---|---|
| `../core/THINKING_SPEC.md` 與其他 core 文件 | 否，屬於 deliberate overlap | `../core/THINKING_SPEC.md` 是整合敘事；其他 core 文件是可獨立 review 的維度。 |
| `../core/SAFETY_BOUNDARY.md` 與 clinical governance 安全段落 | 否，但需保持層級清楚 | `../core/SAFETY_BOUNDARY.md` 是全系統邊界；clinical governance 是把邊界套用到具體題目。 |
| `../clinical-question-governance/source_evidence_map.md` 與 demo repo 的 `../../urology-ai-previsit-demo/docs/source-verification.md` | 部分重疊，但職責不同 | thinking repo 是詳細 evidence map；demo repo 應只保留 demo-level source trace，並指向 thinking repo 作為治理來源。 |
| `../discovery/NEXT_STEP.md` 與 discovery templates | 否 | `../discovery/NEXT_STEP.md` 是流程；templates 是可填寫表單。 |
| `../records/2026-04-23/*` 與 evergreen docs | 否 | records 是 dated evidence，不應被當成永久規格。 |
| Synthetic sample outputs in demo repo | 否 | samples 是會議展示與測試資料，不是治理文件。 |

## Current Risks

1. Demo repo 的 source verification 目前比 clinical governance 簡略，若未標示權威來源，可能讓 reviewer 以為 demo docs 是最高來源。
2. Clinical governance pack 與 demo UI question flow 目前尚未完全同步；下一步若要改 MVP 問題，應先從 `../clinical-question-governance/question_candidates_matrix.md` 開始。
3. Core 文件仍多為英文，clinical governance 為繁中；這不是錯誤，但若面向台灣臨床 reviewer，後續可建立繁中 reviewer brief。

## Cut Rules

不要新增以下內容：

- root-level Markdown 文件，除非是入口或總索引。
- 與 clinical question governance 重複的 demo-side 詳細 evidence map。
- 未連到 source evidence 的新病人題目。
- 會讓 system 看起來能診斷、triage 或治療的 wording。
- real patient data fixtures。

## Next Organization Step

1. Demo repo README 應清楚說明：clinical governance source of truth 在 sibling thinking repo。
2. Demo repo `../../urology-ai-previsit-demo/docs/source-verification.md` 應改成 demo source trace，不與 detailed clinical evidence map 競爭。
3. 若下一步要更新 UI 題目，先更新 `../clinical-question-governance/mvp_question_set_recommendation.md`，再同步 demo app。
