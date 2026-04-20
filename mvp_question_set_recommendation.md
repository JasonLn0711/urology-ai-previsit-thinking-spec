# MVP 題組納入建議

日期：2026-04-20
文件目的：定義泌尿科 previsit interview MVP 建議題組，並說明核心必問、條件跳題、護理補問、臨床端保留與暫不納入項目。
重要邊界：MVP 只做 guided question flow、missing-information prompts、patient/nurse review、clinician-facing summary。不可做診斷、治療建議或自動分流。

## 1. MVP 設計原則

【來源支持】AUA/SUFU OAB、AUA BPH/LUTS、AUA/SUFU microhematuria、AUA/CUA/SUFU recurrent UTI、NICE CG97、NICE NG123 皆把病史與症狀評估放在初始評估核心，並把理學檢查、尿液檢查、PVR、影像、膀胱鏡、尿動力與正式診斷留在臨床端。

【來源支持】ICS 與 ICIQ 支持 bladder diary、frequency-volume chart、urinary incontinence frequency/amount/impact/leakage context 等病人回報欄位，但不支持把所有日誌內容強制塞進每位病人的核心問卷。

【推論】MVP 應採取「短核心 + 症狀觸發 + 護理補齊 + 醫師覆核」：

- 核心必問控制在 10 到 14 題。
- 條件模組只在相關症狀出現後顯示。
- 護理頁顯示協助需求、缺漏、日誌 cue、用藥 cue、需 review observations。
- 醫師頁顯示整理後的 patient-reported observations，不顯示診斷或治療建議。

## 2. Level 1：核心必問題

| 順序 | 病人版題目 | 建議回答形式 | 納入理由 | 摘要影響 | 主要風險與控制 |
|---:|---|---|---|---|---|
| 1 | 這份資料是誰填的？ | 單選：本人 / 家人協助 / 護理師協助 | 【推論】判斷資料來源與協助需求。 | 顯示填答來源。 | 避免讓病人覺得被評價；文字中性。 |
| 2 | 今天最想請醫師幫忙看的泌尿問題是什麼？ | 大按鈕單選 + 其他短文字 | 【來源支持】初始評估需要主訴與病史。 | 摘要置頂，觸發模組。 | 選項不足時提供其他。 |
| 3 | 這個問題大約從什麼時候開始？ | 單選區間 + 不清楚 | 【來源支持】病史需要時間脈絡；區間為【推論】。 | 顯示 duration。 | 不要求精準日期。 |
| 4 | 這個問題目前對生活造成多大困擾？ | 0 到 10 量表 | 【來源支持】ICIQ impact / NICE QoL questionnaire。 | 顯示 bother score。 | 不把分數轉診斷。 |
| 5 | 白天清醒時，是否覺得尿尿次數明顯比以前多？ | 是 / 否 / 不確定 | 【來源支持】AUA OAB、NICE FVC、ICS FVC。 | storage observation。 | 用「比以前多」避免正常值混淆。 |
| 6 | 晚上睡覺後，通常會起床尿尿幾次？ | 0 / 1 / 2 / 3 次以上 / 不確定 | 【來源支持】NICE FVC、ICS diary。 | nocturia count。 | 說明是睡著後起床。 |
| 7 | 是否會突然很想尿，而且很難忍住？ | 是 / 否 / 不確定 | 【來源支持】AUA OAB、ICS urgency。 | urgency observation。 | 不標示 OAB 診斷。 |
| 8 | 最近 4 週是否有尿不小心漏出來？ | 是 / 否 / 不確定 | 【來源支持】ICIQ-UI SF、NICE NG123。 | 觸發漏尿模組。 | 中性語降低羞恥。 |
| 9 | 尿尿時會痛、刺痛或灼熱嗎？ | 是 / 否 / 不確定 | 【來源支持】AUA rUTI、NICE NG123。 | pain/infection-related observation。 | 不標示 UTI。 |
| 10 | 是否看過尿液呈紅色、茶色，或看到血塊？ | 是 / 否 / 不確定 | 【來源支持】AUA hematuria、NICE hematuria context。 | visible hematuria observation。 | 不問 microscopic hematuria；不暗示癌症。 |
| 11 | 是否曾經或現在明明很想尿，卻尿不太出來或完全尿不出來？ | 是 / 否 / 不確定；若是，問「現在是否仍發生」 | 【來源支持】AUA OAB PVR if emptying symptoms；NICE retention。 | emptying/retention review observation。 | 不自動建議急診或導尿。 |
| 12 | 最近是否有發燒、發冷，或腰部兩側疼痛？ | 複選：發燒 / 發冷 / 腰側痛 / 沒有 / 不確定 | 【來源支持】AUA rUTI systemic/complicating concern；NICE urine testing context。 | review observation。 | 不診斷感染。 |
| 13 | 今天是否能提供目前正在吃的藥或藥單？ | 可以 / 只記得部分 / 不清楚 / 沒有固定用藥 | 【來源支持】NICE medication review。 | medication completeness。 | 不要求病人分類藥物。 |
| 14 | 還有什麼你希望醫師先知道？可以留空。 | 選填短文字 | 【推論】補足固定選項未涵蓋主訴。 | 摘要最後補充。 | 限字數，避免冗長。 |

## 3. Level 2：條件模組題

### 3.1 頻尿 / 夜尿 / 急尿模組

觸發條件：第 5、6、7 題任一為「有 / 2 次以上 / 不確定且困擾高」。

| 題目 | 回答形式 | 納入理由 | MVP 判斷 |
|---|---|---|---|
| 白天清醒時，大約尿尿幾次？ | 區間：1-4、5-7、8-10、10 次以上、不確定 | 【來源支持】FVC/diary 支持排尿頻率；區間設計為【推論】。 | 條件跳題。 |
| 最近一週，突然很急、很難忍住的情況大約多常發生？ | 每天多次 / 每天一次 / 每週幾次 / 很少 / 不確定 | 【來源支持】OAB/urgency assessment；ICS diary 可記錄 urgency。 | 條件跳題。 |
| 你是否常喝咖啡、茶、酒，或睡前喝很多水？ | 複選 + 不確定 | 【來源支持】NICE 支持 caffeine/fluid discussion。 | 條件跳題；不給自動建議。 |
| 如果醫護人員需要，你是否能記錄 3 天尿尿時間、尿量與喝水？ | 可以 / 需要協助 / 可能不方便 / 不確定 | 【來源支持】NICE/ICS/ICIQ diary。 | 條件跳題，護理 cue。 |

### 3.2 漏尿模組

觸發條件：第 8 題回答「有 / 不確定」。

| 題目 | 回答形式 | 納入理由 | MVP 判斷 |
|---|---|---|---|
| 最近 4 週，漏尿大約多常發生？ | ICIQ-like frequency categories | 【來源支持】ICIQ-UI SF frequency。 | 條件跳題；若非完整量表，不宣稱 ICIQ score。 |
| 通常漏出來的量大約是多少？ | 幾滴 / 少量 / 會濕內褲或護墊 / 很多 / 不確定 | 【來源支持】ICIQ-UI SF amount；ICS pad usage。 | 條件跳題。 |
| 什麼情況容易漏尿？ | 複選：來不及到廁所、咳嗽/打噴嚏、運動、睡覺、尿完穿好後、無明顯原因、不確定 | 【來源支持】ICIQ self-diagnostic item；NICE UI symptom categorisation。 | 條件跳題；只列情境，不診斷類型。 |
| 是否使用護墊、尿布或其他用品？ | 沒有 / 偶爾 / 每天 / 不確定 | 【來源支持】ICS pad usage；NICE containment review。 | 條件跳題，護理 cue。 |

### 3.3 排尿困難 / 弱尿流 / 尿不乾淨模組

觸發條件：主訴為排尿困難、尿流弱、尿不乾淨，或第 11 題回答「有 / 不確定」。

| 題目 | 回答形式 | 納入理由 | MVP 判斷 |
|---|---|---|---|
| 是否覺得尿流變細、變弱？ | 是 / 否 / 不確定 | 【來源支持】IPSS/AUA-SI domain、AUA BPH、NICE LUTS。 | 條件跳題。 |
| 尿尿時是否常需要用力才尿得出來？ | 是 / 否 / 不確定 | 【來源支持】IPSS/AUA-SI domain。 | 條件跳題。 |
| 尿尿時是否會斷斷續續？ | 是 / 否 / 不確定 | 【來源支持】IPSS/AUA-SI domain。 | 條件跳題。 |
| 尿完後是否常覺得還沒尿乾淨？ | 是 / 否 / 不確定 | 【來源支持】IPSS/AUA-SI domain；PVR 由臨床端評估。 | 條件跳題。 |

### 3.4 血尿模組

觸發條件：第 10 題回答「有 / 不確定」。

| 題目 | 回答形式 | 納入理由 | MVP 判斷 |
|---|---|---|---|
| 看到血尿是一次、反覆發生，還是每次尿尿都有？ | 一次 / 反覆 / 幾乎每次 / 不確定 | 【來源支持】血尿需臨床評估；具體模式問法為【推論】。 | 條件跳題。 |
| 是否曾看到血塊？ | 是 / 否 / 不確定 | 【推論】可幫醫師了解病人可見觀察。 | 條件跳題，醫師覆核。 |
| 血尿是否伴隨疼痛、尿痛、發燒或腰側痛？ | 複選 | 【來源支持】AUA/NICE 需評估感染、非惡性與其他原因；具體合併症狀問法為【推論】。 | 條件跳題。 |

不納入 MVP 病人端：

- 「你是否有 microscopic hematuria？」
- 「你是否屬於高風險血尿？」
- 「你是否需要膀胱鏡或影像？」

### 3.5 感染 / 疼痛模組

觸發條件：第 9 或 12 題回答「有 / 不確定」，或主訴為反覆感染。

| 題目 | 回答形式 | 納入理由 | MVP 判斷 |
|---|---|---|---|
| 排尿疼痛或灼熱是每次尿尿都有，還是偶爾？ | 每次 / 偶爾 / 不確定 | 【來源支持】symptomatic episodes 需搭配 urine studies；具體頻率問法為【推論】。 | 條件跳題。 |
| 過去 12 個月是否因類似症狀就醫或吃過抗生素？ | 沒有 / 1 次 / 2 次以上 / 不確定 | 【來源支持】AUA rUTI 需 symptomatic episodes 與尿液證據；此題只問病史。 | 條件跳題；不診斷 rUTI。 |
| 腰側痛大約多痛？ | 0 到 10 | 【推論】協助護理/醫師 review。 | 條件跳題。 |

不納入 MVP 病人端：

- 「你是不是泌尿道感染？」
- 「你需要抗生素嗎？」
- 「你的尿液培養是否陽性？」

### 3.6 用藥 / 共病 / 影響因子模組

觸發條件：用藥不完整、血尿、夜尿、排尿困難、反覆感染或醫護需要。

| 題目 | 回答形式 | 納入理由 | MVP 判斷 |
|---|---|---|---|
| 你是否願意讓護理師協助看藥袋或藥單？ | 願意 / 需要家人協助 / 今天沒有帶 / 不確定 | 【來源支持】NICE medication review；具體協助方式為【推論】。 | 護理補問。 |
| 是否知道自己有糖尿病、腎臟病、神經系統疾病或脊髓受傷？ | 是 / 否 / 不確定 | 【來源支持】AUA/NICE 共病脈絡；具體題目為【推論】。 | 條件題，不核心必問。 |
| 是否正在使用利尿劑或抗凝血藥？ | 知道有 / 知道沒有 / 不清楚，請看藥單 | 【來源支持】NICE med review；AUA microhematuria anticoagulant evaluation。 | 優先護理補問，不建議病人核心自填。 |

## 4. Level 3：護理補問與工作項

| 護理項目 | 觸發條件 | 顯示方式 | 納入理由 |
|---|---|---|---|
| 協助閱讀/操作 | 病人選擇需要協助、填答時間過長、欄位空白多 | `需要填答協助` | 【來源支持】CDC health literacy、FDA human factors、WCAG。 |
| 補用藥資訊 | 藥單不完整或不清楚 | `請協助確認藥袋/藥單` | 【來源支持】NICE medication review。 |
| Bladder diary instruction | frequency/nocturia/urgency/leakage | `可考慮說明 3 天 bladder diary` | 【來源支持】NICE、ICS、ICIQ。 |
| Containment support | 漏尿且使用護墊/尿布，或有皮膚/外出困擾 | `可詢問用品與皮膚/生活困擾` | 【來源支持】NICE containment review、ICS pad usage。 |
| Review trigger | 尿不出來、可見血尿/血塊、發燒畏寒、腰側痛、嚴重疼痛 | `依院內流程 review` | 【來源支持】NICE/AUA；具體 SOP 為【推論】。 |

## 5. Level 4：臨床端保留

| 項目 | 為什麼不放病人端 | 來源標示 |
|---|---|---|
| 理學檢查、DRE、pelvic exam | 需要臨床訓練與現場檢查。 | 【來源支持】AUA BPH、NICE CG97/NG123、AUA rUTI。 |
| 尿液 dipstick、urinalysis、culture 判讀 | 需檢驗與臨床解釋。 | 【來源支持】AUA OAB/MH/rUTI、NICE NG123。 |
| PVR、uroflowmetry | 需儀器，是否需要由醫師判斷。 | 【來源支持】AUA OAB/BPH、NICE CG97/NG123。 |
| 膀胱鏡、影像、尿動力 | 不是初始 previsit 病人自填內容，且需臨床適應症。 | 【來源支持】AUA OAB、AUA MH、NICE CG97/NG123。 |
| microhematuria risk stratification | 需要尿液顯微、年齡、性別、吸菸、風險因子與醫師判斷。 | 【來源支持】AUA microhematuria。 |
| 診斷與治療建議 | 超出 previsit interview 安全邊界。 | 【來源支持】指南均定位於 clinician evaluation；禁止結論為【推論】與安全治理。 |

## 6. 暫不納入 MVP 的有價值題目

| 題目 | 有價值原因 | 暫不納入理由 | 未來條件 |
|---|---|---|---|
| 完整 IPSS / AUA-SI | 對男性 LUTS baseline 有價值。 | 需確認版權/語言版本/是否完整採用；不宜混入通用核心。 | 醫師決定以男性 LUTS 模組完整使用。 |
| 完整 ICIQ-UI SF 分數 | 對尿失禁評估有驗證價值。 | 需授權與完整題目；自訂改寫不可宣稱原分數。 | 取得正式版本與 clinical reviewer approval。 |
| OABSS 或其他地區常用量表 | 可能符合台灣臨床習慣。 | 需確認本院醫師偏好與授權。 | 現場 review 後決定。 |
| 詳細吸菸量與職業暴露 | 血尿風險評估有價值。 | 對所有病人負擔高；血尿模組中也可能需要護理/醫師確認。 | 血尿 pathway 成熟後加入 clinician-facing 模組。 |
| 性功能、骨盆疼痛、腸道症狀細項 | 對特定疾病或女性泌尿有價值。 | MVP 範圍過廣，會增加敏感性與填答負擔。 | 特定 specialty module 才納入。 |
| 既往影像、膀胱鏡、尿動力詳細結果 | 對複雜病人有用。 | 病人難以正確判讀；需要病歷。 | 進入正式臨床整合或人工補件流程。 |

## 7. MVP 摘要輸出規格

### 7.1 醫師摘要

應顯示：

- 主訴與開始時間。
- 困擾程度。
- Storage / voiding / pain / hematuria / retention observations。
- 漏尿情境與用品使用。
- 用藥完整性。
- 缺漏資訊。
- 需臨床 review 的 patient-reported observations。

不應顯示：

- 系統診斷。
- 自動風險等級。
- 自動治療建議。
- 自動檢查建議。

### 7.2 護理摘要

應顯示：

- 填答協助需求。
- 缺漏欄位。
- 用藥/藥單補問。
- Bladder diary instruction cue。
- Containment support cue。
- 需依院內流程 review 的回報。

不應顯示：

- 要護理師做診斷判斷的標籤。
- 沒有 SOP 的緊急分流命令。
- 無法行動的低價值資訊。

## 8. 臨床現場 Review 前不得宣稱的內容

【推論】在醫師與護理現場 review 前，不得宣稱：

- 題組已符合任一院所正式臨床流程。
- 題組可取代既有初診單。
- 題組可診斷 OAB、BPH、UTI、hematuria risk 或 retention。
- 題組可改善治療結果。
- 題組已完成台灣病人可讀性驗證。

## 9. 臨床審查待確認問題

1. 核心題數是否太多？是否需降到 10 題以內？
2. 台灣泌尿科是否偏好 IPSS/OABSS/ICIQ 的哪一套正式量表？
3. 血尿題是否需要在 MVP 就問吸菸史，或先留給醫師端？
4. 護理師能否在候診階段補藥單與教 diary？
5. 哪些 review triggers 在院內有 SOP？沒有 SOP 的不應做突出警示。
6. 病人端語言是否需加入台語口語對照或圖示輔助？
7. 是否需要針對男性 LUTS、女性 UI、感染、血尿建立不同入口，而不是一個通用入口？
