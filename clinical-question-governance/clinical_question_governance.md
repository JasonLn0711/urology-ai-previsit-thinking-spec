# 泌尿科 Previsit Interview 臨床題目治理總報告

日期：2026-04-20
文件定位：臨床需求分析與題目納入治理文件
適用範圍：泌尿科初診或回診前的病人自填 / 護理協助填答 / 醫師預覽摘要
不適用範圍：診斷、治療建議、自動分流、自動處置、正式病歷判讀

## 0. 核心判斷

【來源支持】泌尿科初始評估的共同主軸不是「由系統診斷疾病」，而是取得病史、症狀型態、困擾程度、用藥與相關風險脈絡，再由臨床端搭配理學檢查、尿液檢查、殘尿量、影像或膀胱鏡等檢查判斷。AUA/SUFU overactive bladder guideline 要求初始評估包含病史、膀胱症狀評估、理學檢查與尿液分析，並明確指出症狀問卷與排尿日誌可協助判斷症狀與困擾程度，但不應常規在初始評估做尿動力、膀胱鏡或影像。來源：[AUA/SUFU OAB Guideline 2024](https://www.auanet.org/guidelines-and-quality/guidelines/idiopathic-overactive-bladder)

【來源支持】男性 LUTS 初始評估需要一般病史、共病、用藥檢視、症狀導向理學檢查、尿液 dipstick、頻率尿量圖，並在治療前使用 validated symptom score，例如 IPSS。NICE 同時明確說明 uncomplicated LUTS 初始評估不常規做膀胱鏡、上泌尿道影像、尿流速或殘尿量。來源：[NICE CG97 Recommendations](https://www.nice.org.uk/guidance/cg97/chapter/Recommendations)

【來源支持】女性尿失禁初始評估需要依症狀分類 stress、mixed、urgency urinary incontinence / OAB；需要尿液 dipstick；voiding dysfunction 或 recurrent UTI 症狀才考慮殘尿量；尿失禁或 OAB 初始評估可使用至少 3 天 bladder diary；單純尿失禁初始評估不使用 cystoscopy 或 routine imaging。來源：[NICE NG123 Recommendations](https://www.nice.org.uk/guidance/ng123/chapter/Recommendations)

【來源支持】ICS 對 frequency-volume chart 與 bladder diary 的定義支持收集排尿時間、尿量、液體攝取、漏尿、pad usage、urgency、pain、incontinence episodes 等資料，但這些資料比較適合條件模組或日誌指引，不適合全部塞進核心必問。來源：[ICS Bladder Diary / Frequency Volume Chart](https://www.ics.org/committees/standardisation/terminologydiscussions/bladderdiary)

【來源支持】ICIQ-UI SF 是已驗證的尿失禁簡短問卷，支援詢問漏尿頻率、漏尿量、生活影響與自我感覺的漏尿情境。來源：[ICIQ-UI SF](https://iciq.net/iciq-ui-sf)

【推論】因此，本系統的 MVP 題目治理原則應是「少量核心必問 + 條件模組 + 護理補問 + 臨床端保留」。核心必問只收集幾乎所有泌尿初診都能用、病人能理解、醫師/護理能行動的資訊；其餘資料依症狀觸發。

## 1. Step 1：證據層級

| 等級 | 來源類型 | 本系統中的使用方式 | 可支持的題目類型 | 不可推出的結論 |
|---|---|---|---|---|
| A | 國際或國家級正式指南 | 作為是否納入題目的主要依據 | 初始評估、病史、症狀分類、尿液檢查、何時不做進階檢查 | 不可把指南中的臨床判斷改寫成病人自我診斷 |
| A | AUA/SUFU、AUA/CUA/SUFU、NICE | 支持 OAB、LUTS、UI、microhematuria、recurrent UTI 的題目邊界 | 主訴、症狀型態、困擾程度、血尿、感染症狀、用藥、日誌 | 不可產生治療建議或自動風險分層 |
| B | 專業標準術語與共識 | 統一題目語義，避免用字混亂 | storage / voiding / emptying、frequency-volume chart、bladder diary | 不可要求病人理解專業術語 |
| B | 已驗證問卷與日誌 | 支持簡短、可填、可比較的病人回報欄位 | IPSS / AUA-SI、ICIQ-UI SF、ICIQ bladder diary | 不可拆改後宣稱仍保有完整量表效度 |
| C | 正式公共衛生、可用性、易讀性文件 | 支持病人端語言、協助填答、錯誤預防 | 簡短句、少概念、可重填、不知道選項、輔助填答 | 不可替代臨床效度證據 |
| D | 臨床工作流合理推論 | 補足護理與摘要工作流設計 | 缺漏提醒、護理補問、摘要欄位排序 | 必須標示【推論】，不可偽裝成 guideline |

## 2. Step 2：候選題目盤點原則

【來源支持】指南與驗證問卷共同指向以下資料類別：症狀、病史、用藥、尿液檢查、日誌、困擾程度、漏尿情境、血尿、感染症狀、排空問題、臨床檢查。來源：AUA/SUFU OAB、AUA BPH/LUTS、AUA microhematuria、AUA/CUA/SUFU recurrent UTI、NICE CG97、NICE NG123、ICS、ICIQ。

【推論】但 previsit interview 不應把所有臨床評估內容轉成病人題目。候選題目先全列，再依三方需求與安全邊界分層：

- Level 1：核心必問題。所有或大多數泌尿初診可使用，低理解門檻，高摘要價值。
- Level 2：條件模組題。只在症狀觸發後詢問，避免填答疲勞。
- Level 3：護理補充題。需要護理協助、缺漏補齊、日誌教學、立即回報提示。
- Level 4：臨床端保留題。需要理學檢查、尿液檢查、影像、PVR、膀胱鏡或醫師判斷。

## 3. Step 3：三方需求整合

### 3.1 病人端需求

【推論】病人最適合回答「自己感受到的症狀」與「近期生活影響」：尿急、頻尿、夜尿、漏尿、疼痛、灼熱、看得到的血尿、尿不出來、何時開始、困擾程度、是否需要協助填答。這些資訊是第一手經驗，不需要臨床訓練。

【來源支持】ICIQ-UI SF 支持以簡短問法詢問漏尿頻率、漏尿量、生活影響與漏尿情境；ICS 支持 bladder diary 由病人記錄排尿時間、尿量、fluid intake、urgency、leakage、pad use 等。來源：[ICIQ-UI SF](https://iciq.net/iciq-ui-sf)、[ICS Bladder Diary / Frequency Volume Chart](https://www.ics.org/committees/standardisation/terminologydiscussions/bladderdiary)

【推論】病人常不確定的題目必須提供「不清楚 / 不知道」：目前藥名、尿液檢查結果、是否曾被診斷 recurrent UTI、是否有 microscopic hematuria、是否有 PVR、是否有前列腺相關診斷、是否使用抗凝血藥。沒有「不知道」會增加猜答與錯填。

【推論】病人端不應一開始就問大量專業題：例如完整 IPSS 全量表、血尿風險分層、膀胱鏡史細節、影像細節、尿動力結果。這些題目會增加疲勞，且許多答案需要病歷或臨床解釋。

### 3.2 臨床醫師需求

【來源支持】醫師需要能快速掌握病史、膀胱症狀、尿液檢查必要性、是否有 infection 或 microhematuria、是否有 emptying / retention 可能性。AUA/SUFU OAB 指南將 medical history、bladder symptoms、urinalysis、必要時 PVR 和 voiding diary 放在 evaluation/diagnosis。來源：[AUA/SUFU OAB Guideline 2024](https://www.auanet.org/guidelines-and-quality/guidelines/idiopathic-overactive-bladder)

【來源支持】男性 LUTS 醫師需要一般病史、共病、用藥、frequency-volume chart、尿液 dipstick、validated symptom score，並知道 recurrent/persistent UTI、retention、疑似癌症等需要 specialist assessment 的情境。來源：[NICE CG97 Recommendations](https://www.nice.org.uk/guidance/cg97/chapter/Recommendations)

【來源支持】血尿相關資訊不能只靠病人自填。AUA/SUFU microhematuria 指南要求病史、理學檢查、血壓、serum creatinine、smoking history 等風險因素，並以 microscopic urinalysis 與 risk-based evaluation 決定後續。來源：[AUA/SUFU Microhematuria Guideline 2025](https://www.auanet.org/guidelines-and-quality/guidelines/microhematuria)

【推論】因此醫師摘要頁最需要的是：主訴、症狀開始時間、症狀分類、困擾程度、red-flag observations、目前用藥是否完整、缺漏資訊、是否需要尿液檢查 / bladder diary / PVR 由臨床端判斷。醫師最不需要的是冗長自由文字、低品質猜測、系統代替醫師貼診斷標籤。

### 3.3 臨床護理師需求

【來源支持】NICE NG123 提到女性尿失禁照護涉及 continence specialist nurse，且 containment product review 可由受訓的 registered healthcare professional 或在其監督下執行。來源：[NICE NG123 Recommendations](https://www.nice.org.uk/guidance/ng123/chapter/Recommendations)

【來源支持】CDC health literacy 資料指出醫療人員與行政支援人員需要清楚與病人溝通，常用策略包含簡單語言、一次限制概念數量、需要時使用翻譯或口譯。來源：[CDC Communication Strategies](https://www.cdc.gov/health-literacy/php/research-summaries/communication-strategies.html)

【推論】護理師在此系統中需要四種資訊：是否需要協助填答、是否有需立即回報醫師的病人回報訊號、哪些常缺欄位要補問、是否需要教導 bladder diary 或 containment support。護理摘要必須顯示「可操作的缺漏與協助需求」，不是只顯示醫師診斷資訊。

## 4. Step 4：題目納入 / 不納入判準

### 4.1 納入條件

候選題目若符合大多數條件，才可納入核心或條件模組：

- 【來源支持】有正式指南、標準術語、驗證問卷或正式醫療組織文件支持。
- 【推論】對醫師或護理工作流有明確用途：分類、缺漏補齊、摘要、日誌教學、用藥回顧、風險觀察。
- 【推論】病人有合理機率能自行回答，或可由護理協助補問。
- 【推論】能服務症狀分類、危險訊號觀察、後續檢查提示或生活品質/困擾程度，而不是只增加資料量。
- 【推論】不讓系統看起來像在做診斷、治療建議或自動分流。
- 【推論】題目數量與回答形式不會明顯造成填答疲勞。

### 4.2 不納入條件

候選題目若符合任一高風險條件，應不納入病人端：

- 沒有可靠來源，或只是「看似有趣」但無臨床行動價值。
- 需要理學檢查、尿液檢查、PVR、尿流速、影像、膀胱鏡或尿動力才能回答。
- 高度依賴醫師判斷，例如「我是否是 OAB / BPH / UTI / bladder cancer」。
- 問法暗示診斷，例如「你是不是前列腺肥大造成尿不出來」。
- 答案不會改變摘要、補問、護理協助或醫師預覽。
- 題目過細造成病人疲勞，且可以由 bladder diary 或臨床端替代。

## 5. Step 5：MVP 題組建議

### 5.1 Level 1 核心必問題

【推論】MVP 核心題目應控制在 10 到 14 題以內，包含：

1. 是否本人填寫，是否需要協助。
2. 今天最想處理的泌尿問題。
3. 問題開始時間。
4. 目前困擾程度。
5. 白天排尿次數是否明顯增加。
6. 夜間起床尿尿次數。
7. 是否有突然很急、很難忍住的尿意。
8. 是否有漏尿。
9. 是否有排尿疼痛或灼熱。
10. 是否看見尿中有血或血塊。
11. 是否曾或現在尿不太出來 / 完全尿不出來。
12. 是否發燒、畏寒或腰側痛。
13. 目前用藥是否可提供完整藥單。
14. 是否願意或需要護理師協助補充資訊。

### 5.2 Level 2 條件模組

【來源支持】ICS 與 ICIQ 支持將 diary 與尿失禁細節放在有相關症狀者。NICE 支持在 LUTS、UI、OAB 使用 frequency-volume chart / bladder diary。來源：ICS、ICIQ、NICE CG97、NICE NG123。

MVP 條件模組應包含：

- 頻尿 / 夜尿 / 急尿模組。
- 漏尿模組。
- 排尿困難 / 弱尿流 / 尿不乾淨模組。
- 血尿模組。
- 感染 / 疼痛模組。
- retention / urgent concern 觀察模組。
- 用藥 / 共病 / 影響因子模組。

### 5.3 Level 3 護理補充題

【推論】MVP 護理補充題應聚焦工作流，而非新增診斷：

- 是否需要代讀或協助填答。
- 是否需要 bladder diary instruction。
- 是否需要 containment product support。
- 是否有藥單缺漏需補問。
- 是否有病人回報訊號需依院內流程通知醫師。
- 是否有問卷內容前後矛盾或空白。

### 5.4 Level 4 臨床端保留

【來源支持】AUA、NICE 多項指南將 physical exam、urinalysis、culture、PVR、imaging、cystoscopy、urodynamics、DRE、pelvic exam 放在臨床端評估，而非病人自填。來源：AUA/SUFU OAB、AUA microhematuria、AUA/CUA/SUFU rUTI、AUA BPH/LUTS、NICE CG97、NICE NG123。

MVP 不應將以下內容做成病人端題目：

- 「我是否有 microscopic hematuria」。
- 「我是否需要膀胱鏡 / CT / 尿動力」。
- 「我是否是 OAB / BPH / UTI / cancer」。
- 「我應該用什麼藥」。
- DRE、pelvic exam、PVR、尿液培養、影像與膀胱鏡結果的病人自我判讀。

## 6. Step 6：仍需臨床現場 Review 的待確認問題

1. 【推論】台灣泌尿科門診實際初診時間、護理協助角色與填表位置：候診區、報到後、診間前、或線上預填。
2. 【推論】院內是否已有固定初診表、IPSS、OABSS、ICIQ、bladder diary 或尿失禁問卷，是否需要避免重複。
3. 【推論】紅旗訊號顯示方式應依院內流程設計：只標示「需護理 review」，還是有正式 escalation SOP。
4. 【推論】是否要在 MVP 使用完整 IPSS / ICIQ，或只採「不宣稱量表效度」的簡化題組。
5. 【推論】護理師是否能在看診前補問用藥、藥袋照片、抗凝血藥、利尿劑與泌尿科相關病史。
6. 【推論】對長者、視力不佳、手部操作不便、台語使用者，是否需要紙本同步版或護理代填模式。
7. 【推論】台灣病人對「血尿」、「尿不乾淨」、「急尿」、「漏尿」的常用語是否需經醫護與病人訪談修訂。

## 7. 安全邊界

本系統可做：

- 【來源支持】收集病人回報症狀與困擾程度。
- 【來源支持】提示可由臨床端考慮的日誌、尿液檢查、用藥回顧與進一步問診。
- 【推論】標示病人回報的 red-flag observations，供護理或醫師 review。
- 【推論】標示缺漏資訊，減少重複問診。

本系統不可做：

- 自動診斷 OAB、BPH、UTI、bladder cancer、urinary retention。
- 自動判定病人風險等級或就醫急迫性。
- 自動建議藥物、檢查或處置。
- 對病人說「你不需要看醫師」或「你應立即接受某治療」。
- 將病人自填問卷宣稱為完整臨床評估。

## 8. 審查者檢查清單

每一題在納入前必須能回答：

1. 依據是什麼？
2. 誰會使用這個答案？
3. 若不問，會造成什麼臨床或工作流缺漏？
4. 若問了，摘要頁如何使用？
5. 病人是否能理解？
6. 是否需要「不清楚 / 不知道」？
7. 是否需條件跳題？
8. 是否會暗示診斷或治療？
9. 是否增加護理負擔？
10. 是否更適合留在臨床端？
