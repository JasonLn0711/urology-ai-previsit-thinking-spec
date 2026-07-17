# 2026-07-17 信義申請資格與臨時會議資料包

Status: source preserved / minutes-for-review captured / official verification
complete / Xinyi medical-group feasibility assessment active

## Use this packet for

- 2026-07-16 `晴天霹靂` 與衛福部溝通的 LINE source boundary。
- 2026-07-17 14:00 臨時會議、完整校正逐字稿與決策重建。
- 2026-07-17 14:49 送審會議紀錄、四則照片 placeholder 與兩個附件檔名。
- A3 歷史路徑轉向 B/B2 的官方資格查核。
- 信義門診部 `一般診所（醫務室）` 分類、社區醫療群運作與主提資格的白話說明。
- B 類每年 990 萬元整案上限，以及既有 1,000 萬元 AI-only／3,750 萬元 A3 預算的重編 gate。

## Canonical files

- [臨時會議查核、決策狀態與 action register](health-taiwan-phase2-emergency-meeting-verification-and-decision-record.md)
- [校正 ASR 完整來源副本](sources/health-taiwan-phase2-emergency-meeting-corrected-asr-agent-readable-2026-07-17.md)
- [115 年社區醫療群申請書 XLSX](sources/nhi-taipei-community-medical-group-application-form-115-2026-06-26.xlsx) — SHA-256 `5a6be510...95cc6d0`
- [115 年家醫整合照護計畫公告版 PDF](sources/nhi-family-physician-integrated-care-program-115-announcement-2026-06-26.pdf) — SHA-256 `6effe339...960a362`，與官網相同
- [會前／會後 LINE 資格中斷紀錄](line-xinyi-application-eligibility-b2-pivot-record.md)
- [使用者提供的 GPT 分析原文](sources/user-supplied-gpt-analysis-xinyi-eligibility-b2-2026-07-17.md)

## Current decision boundary

- `confirmed`: 官方規則允許第一合作醫院、診所或衛生所代表社區醫療群申請 B2。
- `confirmed`: 健保公開資料把信義門診部列為一般診所（醫務室）。
- `confirmed by minutes-for-review`: 中正加入既有鄰近醫療群，以每年 990 萬元重編後續申請。
- `confirmed direction`: 信義須盡速評估重新成立醫療群，並以社區醫療群方式提報。
- `active status`: `medical_group_feasibility_assessment_active`；新群是否可成立、院方是否送件仍待決定。
- `pending confirmation`: 主提能力、群員與專科比例、合作醫院、核定時程、無重複申請、四張照片與核定版會議紀錄。
- `scope change`: A3 與舊預算保留為歷史；正式 B2 重寫與每年 990 萬元整案預算從新群可行性、院方送件決定與資格證據啟動。

## Security boundary

Webex token、會議編號與密碼未寫入 tracked files。XLSX/PDF 已保存並驗證；7/16、7/17 圖片實體仍待以安全 source manifest 補完。
