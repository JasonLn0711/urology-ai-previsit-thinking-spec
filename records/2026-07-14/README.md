# 2026-07-14 健康台灣深耕計畫第二階段正式申請格式收件包

Status: verified source copies preserved / current format baseline activated /
proposal transfer and owner confirmation in progress

## FIRST PRINCIPLE

- Scarce resource: 2026-08-17 送件前的格式正確性、規則一致性與文書轉版時間。
- Canonical home: 本 repo `records/2026-07-14/` 保存本次 LINE 收件、來源完整性與提案影響紀錄。
- Source ownership: `sources/` 保存 PDF 與 DOCX 的 verified AI-agent-readable copies；原始 PDF／DOCX 與主管機關最新公告維持最高文件證據層。
- Planning role: `planning-everything-track` 僅保留 locator、status、capacity impact 與 next gate。
- Evidence gate: 兩份 repository copies 與 Downloads 來源 SHA-256 完全一致。
- Next gate: proposal coordinator 以本次 DOCX 格式轉入母案內容，逐欄確認主提／合作機構、申請模式、PI、預算、附件及簽章 owner；Jason 於 2026-07-16 說明會覆核經費與平台操作細節。

## Source Package

| LINE attachment | Source role | Repository copy | SHA-256 |
| --- | --- | --- | --- |
| `1150713-attach1.pdf` | 衛福部 116-118 年第二階段申請作業須知；使用者提供的 Markdown 為 PDF verified AI-agent-readable conversion | `sources/health-taiwan-phase2-application-instructions-116-118-ai-agent-readable-verified-2026-07-07.md` | `3db9bf9e3bf746595f67e1a196c3602bfd74f834eeeda61ad7a1a2219449fb66` |
| `1150713-attach2.docx` | 第二階段計畫書格式與附件包；使用者提供的 Markdown 為 DOCX verified AI-agent-readable conversion | `sources/health-taiwan-phase2-application-template-and-attachments-116-118-ai-agent-readable-verified-2026-07-13.md` | `98aca8ab01a9ae25a59e4ff642b04024440c7a2b52fd3f82093463924f571b18` |

命名以文件角色與來源日期取代聊天附件流水號，讓後續 agent 可以直接辨識 authority、用途與版本。完整來源與 copy verification 見 [sources/README.md](sources/README.md)。

## LINE Record

- Canonical record: [line-health-taiwan-phase2-new-application-format-record.md](line-health-taiwan-phase2-new-application-format-record.md)
- `confirmed`: 陳美如主任於 08:07 提醒團隊注意計畫格式。
- `confirmed`: 趙康邑於 10:29 宣布新格式已發布，並分享 `1150713-attach1.pdf` 與 `1150713-attach2.docx`。
- `adopted decision`: 本次 attach1 與 attach2 成為 116-118 第二階段 proposal 的 current formal-format baseline，取代 114-115 第一階段格式作為填表骨架。

## Activated Application Controls

1. 申請期間為 2026-07-13 10:00 至 2026-08-17 23:59；紙本函送期限為 2026-08-17。
2. 計畫本文上限 60 頁，每個上傳檔案上限 25 MB，平台產製兩份申請檔並函送紙本 1 份。
3. 計畫摘要控制在 500 字內；延續型計畫另填第一階段質化／量化成果、1-2 項亮點與精進方式。
4. 116、117、118 年分年目標、策略、方法、成果及 KPI 使用同一條 traceability chain；KPI 以任務成果與可驗證成效為主。
5. 範疇三案件附智慧醫療整體執行情形聲明書，並建立 AI、資料、資安、FHIR/TW Core IG 與臨床 AI 登錄治理證據。
6. 涉及人體研究者於申請時附 IRB 核准文件或已送審證明，正式核准文件於核定撥款前補齊。
7. 經費採統塊式核給；資本門原則上限 30%；範疇二國外旅費上限 20%；設備以單價新臺幣 1 萬元以上且使用年限 2 年以上定義。
8. 正式附件包含計畫申請聲明暨未重複補助切結書、參與計畫同意書、範疇三智慧醫療聲明書及 B2 條件式切結書；利衝揭露依申請人身分與法規條件啟動。

## Proposal Impact

- [正式格式對照表](../../discovery/DEEP_CULTIVATION_OFFICIAL_FORMAT_CROSSWALK.md) 現以本次 attach2 為 current template，新增 500 字摘要、延續型成果、正式附件與分年 KPI 欄位控制。
- [MOHW compliance rubric](../../discovery/DEEP_CULTIVATION_MOHW_COMPLIANCE_RUBRIC.md) 現以 attach1／attach2 作 current downloaded official-file layer；7/13 說明會保留為 briefing interpretation layer。
- [年度 checkpoint](../../discovery/DEEP_CULTIVATION_ANNUAL_CHECKPOINT_TABLE.md) 將 formal-notice/template gate 標記為完成，並把 7/16 定位為經費、平台及現場問答的下一個 validation layer。
- [7/13 briefing record](../2026-07-13/README.md) 提供規則摘要與 LINE 協調；本記錄提供正式作業須知與 live template evidence。
- [7/9 writing-spec analysis](../2026-07-09/health-taiwan-application-writing-spec-analysis-for-xinyi.md) 保留章節責任與 20 頁子案壓縮策略；最終母案欄位與附件以本次 attach2 為準。
- [governance checklist](../../discovery/DEEP_CULTIVATION_GOVERNANCE_CHECKLIST.md) 承接 IRB、AI/data/security governance 與 real-data activation gate。

## Action Register

| ID | Action | Owner | Due / trigger | Evidence |
| --- | --- | --- | --- | --- |
| HT-0714-01 | 將母案與各工作包轉入 attach2 current template，保留來源與修訂對照 | proposal coordinator + section owners | immediate | field-level transfer checklist |
| HT-0714-02 | 確認延續／新增計畫、A/B/C/D 模式、主提與合作機構、PI、聯絡人及機構代碼 | parent proposal owner | before formal circulation | signed owner sheet |
| HT-0714-03 | 逐列核對 116-118 KPI、現況值、公式、資料來源、owner、預算與公開成果治理 | evaluation + budget + data owners | before draft freeze | KPI-budget-evidence matrix |
| HT-0714-04 | 完成 IRB/QI purpose map，取得一般／簡易／免審或送審路徑的正式意見 | PI + IRB liaison | before real-data/research activation | written determination / submission proof |
| HT-0714-05 | 7/16 覆核經費科目、負面表列、平台操作、檔案產製與截止流程 | Jason + proposal coordinator | 2026-07-16 13:00-16:30 | dated briefing notes |
| HT-0714-06 | 在 8/17 前完成平台檔案、紙本函送、附件簽章與版本一致性 preflight | proposal coordinator + institutional admin | 2026-08-17 | submission manifest + platform receipt |
