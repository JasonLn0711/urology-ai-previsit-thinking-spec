---
document_type: health_taiwan_deep_cultivation_plan
source_file: "忠孝 信義深耕計畫_修改20260709.docx"
output_file: "ai_agent_readable_plan.md"
language: zh-Hant-TW
converted_at: "2026-07-09"
verification_status: "web_verified_with_risk_notes"
preservation_policy: "原創計畫正文不直接改寫；僅做格式轉換、索引化、查證註記與風險標示。"
ai_agent_readable: true
---

# 「健康台灣深耕計畫」AI Agent Readable Markdown

## 0. 使用原則

本檔將原始 DOCX 轉為可供 AI agent 擷取、比對、審查與後續修改管理的 Markdown。原創計畫內容保留在「原始計畫內容轉寫區」。本檔前段加入「索引、查證、風險、待決策事項」，用於協助審查與修訂，但不直接覆寫原始計畫主張。

### 0.1 Agent 操作規則

- `preserve_original_content`: true
- `do_not_autocorrect_original_body`: true
- `fact_check_notes_are_separate`: true
- `recommended_edit_mode`: "先由人類確認，再回寫正式計畫書"
- `primary_risk`: "行政資料、政策口徑、經費試算、績效指標定義需人工確認"

---

## 1. Agent Index / Metadata

| 欄位 | 內容 |
|---|---|
| 計畫名稱 | 「健康台灣深耕計畫」－推動三高篩檢與腦心血管疾病預防，同步守護健康『攝區』，攝護腺癌 PSA 精準篩檢 |
| 主提機構 | 臺北市立聯合醫院附設信義門診部 |
| 主提機構醫事機構代碼 | 2101170050 |
| 主提機構統一編號 | 99958172 |
| 申請縣市 | 臺北市 |
| 申請模式 | A3 |
| 計畫範疇 | 導入智慧科技醫療；社會責任醫療永續 |
| 執行期程 | 116 年 1 月 1 日至 118 年 12 月 31 日 |
| 計畫主持人 | 陳瑞泉（醫師兼主任） |
| 聯絡人 | 洪淑如（技術師） |
| 主要疾病主軸 | 三高、腦心血管疾病預防、攝護腺癌 PSA 篩檢、PHI 風險分層 |
| 主要服務區域 | 信義區、南港區、內湖區；並連結忠孝院區與門診部網絡 |

## 2. 合作機構索引

| 序號 | 機構 | 原文代碼 | 查證狀態 | Agent note |
|---:|---|---|---|---|
| 1 | 臺北市立聯合醫院 | 0101090517 | 已查證可對應北市聯醫體系 | 忠孝院區等聯醫院區使用同一醫療機構代碼。 |
| 2 | 臺北市信義區健康服務中心 | 未列醫事代碼 | 待確認 | 屬健康服務中心合作單位，需確認是否需立案/機關代碼。 |
| 3 | 臺北市南港區健康服務中心 | 未列醫事代碼 | 待確認 | 原文機構名後有頓號「、」，正式送件前建議刪除。 |
| 4 | 臺北市內湖區健康服務中心 | 未列醫事代碼 | 待確認 | 屬健康服務中心合作單位，需確認是否需立案/機關代碼。 |
| 5 | 臺北市立聯合醫院附設內湖門診部 | 2101110027 | 已查證 | 與官方資料一致。 |
| 6 | 臺北市立聯合醫院附設南港門診部 | 原文：21011200140 | 需修正 | 官方資料顯示為 `2101120014`，原文多一個 0，屬高風險行政錯誤。 |

## 3. 網路查證與合理性檢核

> 註：本節是查證與審查紀錄，不直接改寫原始計畫正文。若要回寫正式版，建議由計畫主持人或承辦窗口逐項確認後處理。

| claim_id | 原文主張／位置 | 查證結果 | 風險等級 | 建議 agent action | 主要來源 |
|---|---|---|---|---|---|
| FC-001 | 「健康台灣深耕計畫」與四大範疇 | 可查證。官方資料顯示計畫期程為 114–118 年，四大範疇為優化醫療工作條件、規劃多元人才培訓、導入智慧科技醫療、社會責任醫療永續。 | 低 | 保留。 | [健康台灣深耕計畫](https://htsprout.nhri.org.tw/dhplan.html) |
| FC-002 | 三高每年導致約 6.2 萬人死亡、約占總死亡 30%，目標 119 年降低三高相關慢性病標準化死亡率三分之一 | 可查證，與行政院「三高防治888計畫」政策文字一致。 | 低 | 保留，但建議標示政策來源。 | [行政院：三高防治888計畫](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/6bc8beff-6a2a-4542-bd0e-255ceeda76c8) |
| FC-003 | 攝護腺癌為臺灣男性發生率第三位癌症、死亡率第六 | 可查證。國健署 2025/10/30 資料指出：111 年發生人數 9,062 人，113 年死亡人數 1,897 人，男性發生率第三、死亡率第六。 | 低 | 保留；若原文使用「最新癌症登記資料」，建議註明年份，避免日後過期。 | [國民健康署：攝護腺癌為男性常見癌症](https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4878&pid=19543) |
| FC-004 | PSA 是攝護腺癌重要篩檢工具，但我國尚未納入公費癌症篩檢 | 「未納入公費癌症篩檢」可查證。國健署現行公費癌症篩檢介紹列乳癌、子宮頸癌、大腸癌、口腔癌、肺癌，未列 PSA。 | 中 | 保留，但需補上「共享決策、充分告知、非全民篩檢」語氣，避免與國健署審慎立場衝突。 | [國健署癌症篩檢介紹](https://www.hpa.gov.tw/Pages/List.aspx?nodeid=211)；[國健署：攝護腺癌要趕快篩？](https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=127&pid=3755) |
| FC-005 | 50 歲以上男性、45 歲以上具家族病史高風險男性進行 PSA 篩檢 | 與美國癌症協會及部分臨床指引的風險溝通年齡大致相容，但不同國家／組織建議不完全相同。 | 中 | 保留為「專案目標族群」，但需明確加入醫師評估、知情同意與 shared decision-making。 | [American Cancer Society](https://pressroom.cancer.org/releases?item=1347)；[NCBI StatPearls: Prostate Cancer Screening](https://www.ncbi.nlm.nih.gov/books/NBK556081/) |
| FC-006 | 臺灣約 33% 患者確診時已第四期，美國約 8% | 臺灣 33.9% 可由 109 年癌症登記相關解讀資料支持，但不是最新年度；美國 8%可對應 CDC 2017 年 distant stage 比例，CDC 2022 年資料則為 9%。 | 中 | 保留論點，但建議改成「以 109 年資料／CDC 2017 或 2022 資料比較」，避免被質疑引用年份不一致。 | [臺大醫院／楓城泌尿學會攝護腺癌介紹 PDF](https://www.tmua.org.tw/storage/health/52/53.pdf?v=20230522083357)；[CDC MMWR 2001–2017](https://www.cdc.gov/mmwr/volumes/69/wr/mm6941a1.htm)；[CDC 2022](https://www.cdc.gov/united-states-cancer-statistics/publications/prostate-cancer.html) |
| FC-007 | PHI 整合 Total PSA、Free PSA、p2PSA，協助 PSA 4–10 ng/ml 灰色地帶風險分層 | 可查證；與臺灣攝護腺癌臨床介紹相容。 | 低 | 保留。建議在流程中明確寫「由醫師判斷是否加驗 PHI」。 | [臺大醫院／楓城泌尿學會攝護腺癌介紹 PDF](https://www.tmua.org.tw/storage/health/52/53.pdf?v=20230522083357) |
| FC-008 | 去雄性激素療法可能提高高血壓、高血脂、代謝症候群風險 | 方向大致合理，但需更精準。近年 meta-analysis 支持 ADT 與糖尿病、高血壓風險增加相關；對「代謝症候群」的關聯則較保守。 | 中 | 保留臨床整合理由，但建議改成「與糖尿病、高血壓、脂質與身體組成變化等代謝風險相關」，不要過度斷言。 | [PubMed: ADT and metabolic disease meta-analysis](https://pubmed.ncbi.nlm.nih.gov/36621463/)；[Investigative and Clinical Urology review](https://icurology.org/DOIx.php?id=10.4111%2Fkju.2015.56.1.12) |
| FC-009 | 臺北市整合式篩檢為一站式健康檢查服務，結合健康服務中心及醫療院所 | 可查證。臺北市衛生局資料說明整合性篩檢結合健康服務中心及醫療院所，提供醫院型與社區型一站式服務。 | 低 | 保留；但原文「五大癌症篩檢」與臺北市頁面「6項癌症篩檢」口徑不同，送件前需統一。 | [臺北市政府衛生局：整合性篩檢](https://health.gov.taipei/cp.aspx?n=06AF6414B09FEAA2) |
| FC-010 | 忠孝院區／聯醫可提供攝護腺癌相關治療，含手術、放射線、荷爾蒙、標靶、化療、海福刀等 | 大致可查證。忠孝院區泌尿科服務列腫瘤評估、荷爾蒙治療、放射線治療、化學治療、標靶治療、免疫治療、手術、攝護腺癌海福刀等。 | 低 | 保留。 | [臺北市立聯合醫院忠孝院區泌尿科](https://tpech.gov.taipei/mp109171/cp.aspx?n=591411D5DFB87DC2&s=6C7045BE0EFE517E) |
| FC-011 | 南港門診部醫事機構代碼 | 原文列 `21011200140`；官方資料為 `2101120014`。 | 高 | 正式送件前必須修正。 | [健保署北市聯醫體系名單 PDF](https://www.nhi.gov.tw/ch/dl-59136-0a3c7ba7c4fa434e95bdedd9ddd324a5-1.pdf) |
| FC-012 | 「臺北市健康服務中心的社區三高篩檢，全台獨一無二，各縣市衛生所都沒有此一模式」 | 未能以公開資料充分查證。這是絕對性、比較性主張，審查時容易被要求舉證。 | 高 | 若無內部公文或官方比較資料，建議改為較保守敘述，例如「臺北市健康服務中心具備高度制度化之社區篩檢合作基礎」。 | 待補正式佐證 |

## 4. 行政資料與一致性風險

| risk_id | 問題 | 原文狀態 | 風險 | 建議處理 |
|---|---|---|---|---|
| R-001 | 南港門診部代碼疑似錯誤 | `21011200140` | 高 | 改為 `2101120014`，並由承辦人以健保署或院內資料確認。 |
| R-002 | 執行期程與年度查核點不一致 | 封面為 116/1/1–118/12/31；查核點仍是 114/9/1–115/3/31、115/4/1–115/12/31 | 高 | 依實際徵件年度重排查核點。 |
| R-003 | 主文「信義健區康服務中心」疑似錯字 | 原文出現「信義健區康」 | 中 | 正式版改為「信義區健康服務中心」。 |
| R-004 | 電子郵件符號 | `Z3805＠tpech.gov.tw` 使用全形 ＠ | 中 | 改為半形 `Z3805@tpech.gov.tw`。 |
| R-005 | 申請經費仍為 placeholder | `○○○,○○○,○○○` | 高 | 正式送件前填入總補助款、配合款、總經費。 |
| R-006 | 「五大癌症篩檢」與臺北市整合性篩檢頁面「6項癌症篩檢」口徑不同 | 原文使用五大癌症篩檢 | 中 | 依送件年度政策口徑統一。 |
| R-007 | PSA 專案與國健署審慎立場需切齊 | 原文強調 PSA 精準篩檢 | 中 | 補強「非全民篩檢、風險族群、醫師評估、共同決策、異常不等於癌症」。 |

## 5. 經費試算檢核

| item_id | 項目 | 原文單價／數量／合計 | 試算結果 | 檢核結論 |
|---|---|---|---|---|
| BUD-001 | 專任助理 | 36,300 元 × 2 人/月 × 27 個月 = 980,100 | 正確應為 1,960,200；980,100 等於 1 人 × 27 個月 | 高風險。需確認到底是 1 人或 2 人。 |
| BUD-002 | 勞保費 | 2,032 × 2 人/月 × 24 個月 = 48,768 | 正確應為 97,536；48,768 等於 1 人 × 24 個月 | 高風險。需與人事費人數一致。 |
| BUD-003 | 健保費 | 3,675 × 2 人/月 × 24 個月 = 88,200 | 正確應為 176,400；88,200 等於 1 人 × 24 個月 | 高風險。需與人事費人數一致。 |
| BUD-004 | 公提勞工退休金 | 2,520 × 2 人/月 × 24 個月 = 60,480 | 正確應為 120,960；60,480 等於 1 人 × 24 個月 | 高風險。需與人事費人數一致。 |
| BUD-005 | 人事費小計 | 1,177,548 | 與「1 人」版本相符，不符合「2 人」版本 | 高風險。人數或小計須二擇一修正。 |
| BUD-006 | PSA 檢查 | 500 × 3,500 = 1,750,000 | 正確 | 可保留。 |
| BUD-007 | PHI | 2,300 × 175 = 402,500 | 正確 | 可保留；但需確認 175 人比例是否符合預估異常率。 |
| BUD-008 | 護理師／醫檢師臨時人員 | 534 × 480 = 256,320 | 正確 | 可保留。 |
| BUD-009 | 行政人員臨時人員 | 415 × 480 = 199,200 | 正確 | 可保留。 |
| BUD-010 | 材料費 | 46.05 × 3,000 = 138,150 | 正確 | 可保留。 |
| BUD-011 | 資本門小計 | 原文小計 81 萬 | 各項相加為 810,000 | 可保留。 |

## 6. KPI 合理性檢核

| kpi_id | KPI | 原文目標 | 檢核意見 | 建議 |
|---|---:|---:|---|---|
| KPI-001 | PSA 篩檢總人次 | ≥ 3,500 人次/年 | 若一年 20 場，平均每場需 175 人；對社區場域與職場場域皆屬高負載。 | 需確認場次規模、報到率、抽血人力、資料輸入流程。 |
| KPI-002 | PSA 異常個案追蹤完成率 | ≥ 60% | 第一階段可作為保守目標，但若申請核心是早期發現，60%略低。 | 可設分年提升，例如 60%→70%→80%，但需由計畫端決策。 |
| KPI-003 | 晚期攝護腺癌診斷比例 | 減少至 30% 以下 | 指標受分母定義與個案數影響大。若只看本計畫篩出之確診個案，年度樣本可能不足。 | 需定義分母：本計畫確診者？聯醫忠孝院區新診斷者？轄區新診斷者？三年合併計算？ |
| KPI-004 | 健康篩檢活動次數 | 20 次/年 | 與 3,500 人次/年連動，需高效率動線。 | 建議補上每場標準作業流程、人力配置、預約與備援機制。 |
| KPI-005 | 社區衛教講座 | 20 次/年 | 數量可行，但需區分「講座」與「篩檢活動」是否同場計算。 | 建議定義佐證資料：簽到表、照片、講義、滿意度問卷。 |

## 7. Agent 待辦清單

```yaml
pending_human_decisions:
  - id: D-001
    decision: "確認正式送件年度與查核點期間"
    owner: "計畫主持人／承辦窗口"
    priority: high
  - id: D-002
    decision: "確認南港門診部醫事機構代碼是否改為 2101120014"
    owner: "承辦窗口"
    priority: high
  - id: D-003
    decision: "確認人事費到底編 1 名或 2 名專任助理"
    owner: "經費編列窗口"
    priority: high
  - id: D-004
    decision: "確認 PSA 篩檢是否補上 shared decision-making 與知情同意文字"
    owner: "計畫主持人／泌尿科專業端"
    priority: medium
  - id: D-005
    decision: "確認五大癌症篩檢／六項癌症篩檢採用哪一年度政策口徑"
    owner: "公衛窗口"
    priority: medium
  - id: D-006
    decision: "確認是否保留『全台獨一無二』等絕對性主張"
    owner: "計畫主持人"
    priority: high
```

---

# 8. 原始計畫內容轉寫區

> 下列內容由原始 DOCX 轉為 Markdown。除圖片路徑改為相對路徑以利打包外，正文主張不在此區直接改寫。

**「健康台灣深耕計畫」－**

<u>**推動三高篩檢與腦心血管疾病預防**，**同步守護健康『攝區』，攝護腺癌PSA精準篩檢**</u>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 33%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6">縣市別（以主提機構所在地勾選）</th>
<th colspan="3">申請模式</th>
<th colspan="5">計畫範疇</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6" rowspan="4"><p>■臺北市□新北市□基隆市□宜蘭縣</p>
<p>□金門縣□連江縣□桃園市□新竹市</p>
<p>□新竹縣□苗栗縣□臺中市□彰化縣</p>
<p>□南投縣□雲林縣□嘉義市□嘉義縣</p>
<p>□臺南市□高雄市□屏東縣□澎湖縣</p>
<p>□花蓮縣□臺東縣</p></td>
<td>A</td>
<td colspan="2"><p>□A1</p>
<p>□A2</p>
<p>■A3</p></td>
<td colspan="5" rowspan="4"><p>□優化醫療工作條件</p>
<p>□規劃多元人才培育</p>
<p>■導入智慧科技醫療</p>
<p>■社會責任醫療永續</p></td>
</tr>
<tr class="even">
<td colspan="3">□B</td>
</tr>
<tr class="odd">
<td colspan="3">□C</td>
</tr>
<tr class="even">
<td colspan="3">□D</td>
</tr>
<tr class="odd">
<td
colspan="14">申請單位/團隊內各機構之名稱及醫事機構代碼<mark>(醫學會或醫事公會請填立案證書字號)</mark></td>
</tr>
<tr class="even">
<td
colspan="14">Ⅰ.醫學中心、Ⅱ.準醫學中心、Ⅲ.區域醫院、Ⅳ.地區醫院、Ⅴ.診所、Ⅵ.醫學會、Ⅶ.公會、Ⅷ.其他</td>
</tr>
<tr class="odd">
<td colspan="2">主提機構</td>
<td colspan="2">Ⅴ</td>
<td colspan="6">臺北市立聯合醫院附設信義門診部(2101170050)</td>
<td>統一編號</td>
<td colspan="3"><strong>99958172</strong></td>
</tr>
<tr class="even">
<td rowspan="7">合作機構</td>
<td>1</td>
<td colspan="2">Ⅲ</td>
<td colspan="8">臺北市立聯合醫院(0101090517)</td>
<td>■</td>
<td rowspan="7">與主提機構同體系或聯盟</td>
</tr>
<tr class="odd">
<td>2</td>
<td colspan="2">Ⅷ</td>
<td colspan="8">臺北市信義區健康服務中心</td>
<td>□</td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="2">Ⅷ</td>
<td colspan="8">臺北市南港區健康服務中心、</td>
<td>□</td>
</tr>
<tr class="odd">
<td>4</td>
<td colspan="2">Ⅷ</td>
<td colspan="8">臺北市內湖區健康服務中心</td>
<td>□</td>
</tr>
<tr class="even">
<td>5</td>
<td colspan="2">Ⅴ</td>
<td colspan="8">臺北市立聯合醫院附設內湖門診部(2101110027)</td>
<td>■</td>
</tr>
<tr class="odd">
<td>6</td>
<td colspan="2">Ⅴ</td>
<td colspan="8">臺北市立聯合醫院附設南港門診部(21011200140)</td>
<td>■</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td colspan="8">(自行增列)</td>
<td>□</td>
</tr>
<tr class="odd">
<td colspan="3">申請經費</td>
<td colspan="9">○○○,○○○,○○○（含配合款：○○○,○○○,○○○）</td>
<td colspan="2">元</td>
</tr>
<tr class="even">
<td colspan="3">執行期程</td>
<td colspan="11">116年1月1日至118年12月31日</td>
</tr>
<tr class="odd">
<td colspan="3">計畫主持人</td>
<td colspan="2">陳瑞泉(醫師兼主任)</td>
<td colspan="3">聯絡人</td>
<td colspan="6">洪淑如(技術師)</td>
</tr>
<tr class="even">
<td colspan="3">單位</td>
<td colspan="2">臺北市立聯合醫院附設信義門診部</td>
<td colspan="3">單位</td>
<td colspan="6">臺北市立聯合醫院</td>
</tr>
<tr class="odd">
<td colspan="3">電話</td>
<td colspan="2">(02)8780-4152</td>
<td colspan="3">電話</td>
<td colspan="6">(02)27861288分機8672</td>
</tr>
<tr class="even">
<td colspan="3">傳真</td>
<td colspan="2">11081臺北市信義區大道路116號1樓</td>
<td colspan="3">傳真</td>
<td colspan="6">(02)27861491</td>
</tr>
<tr class="odd">
<td colspan="3">電子郵件</td>
<td colspan="2">DAP60@tpech.gov.tw</td>
<td colspan="3">電子郵件</td>
<td colspan="6">Z3805＠tpech.gov.tw</td>
</tr>
<tr class="even">
<td colspan="14"><blockquote>
<p><strong>中華民國 115 年 7 月 9 日</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

**目錄**

[壹、申請單位自我檢核項目表
[1](#壹申請單位自我檢核項目表)](#壹申請單位自我檢核項目表)

[貳、計畫概要 [2](#貳計畫概要)](#貳計畫概要)

[參、申請單位簡介 [2](#參申請單位簡介)](#參申請單位簡介)

[肆、計畫規劃 [2](#肆計畫規劃)](#肆計畫規劃)

[伍、效益評估 [3](#伍效益評估)](#伍效益評估)

[陸、出國計畫書 [6](#陸出國計畫書)](#陸出國計畫書)

[柒、經費規劃 [7](#柒經費規劃)](#柒經費規劃)

[捌、人力配置表
[9](#捌人力配置表受補助單位人員)](#捌人力配置表受補助單位人員)

[玖、其他 [10](#玖其他)](#玖其他)

[拾、公職人員利益衝突迴避自主檢核表
[11](#拾公職人員利益衝突迴避自主檢核表)](#拾公職人員利益衝突迴避自主檢核表)

[拾壹、未有重複申請計畫之聲明切結書
[14](#拾壹未有重複申請計畫之聲明切結書)](#拾壹未有重複申請計畫之聲明切結書)

[拾貳、參與計畫同意書 [15](#拾貳參與計畫同意書)](#拾貳參與計畫同意書)

[拾參、審查意見回復表 [16](#_Toc207977409)](#_Toc207977409)

# 壹、申請單位自我檢核項目表

> **衛生福利部補（捐）助計畫-「健康台灣深耕計畫」**
>
> **申請單位自我檢核項目表**

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 22%" />
<col style="width: 59%" />
<col style="width: 4%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>項次</strong></th>
<th><strong>檢核項目</strong></th>
<th><strong>說明</strong></th>
<th><strong>符合</strong></th>
<th><strong>備註</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>申請資格及</p>
<p>檢附證明文件</p></td>
<td><p>(一)1.醫療機構 2.社區醫療群 3.衛福部部定專科醫學會</p>
<blockquote>
<p>4.各醫事人員法規所定之公會 5.其他。</p>
</blockquote>
<p>(二)須附資格證明文件。（詳本作業須知肆）</p></td>
<td>□</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2">2</td>
<td rowspan="2"><p>依格式撰擬</p>
<p>計畫書</p></td>
<td>(一)須由申請單位/團隊具函向衛生福利部提出申請。</td>
<td>□</td>
<td rowspan="2">詳如計畫書格式封面頁</td>
</tr>
<tr class="odd">
<td>(二)須於計畫書封面載明計畫名稱、縣市別、申請之模式及計畫範疇、申請單位/團隊內各機構之名稱及醫事機構代碼或立案證書字號等。</td>
<td>□</td>
</tr>
<tr class="even">
<td>3</td>
<td>填具「公職人員利益衝突迴避自主檢核表」及「身分關係揭露表」</td>
<td><ol>
<li><p>須填具「公職人員利益衝突迴避自主檢核表」。</p></li>
<li><p>須填具「公職人員利益衝突迴避法第14條第2項公職人員及關係人身分關係揭露表」。（非屬公職人員或關係人者，免填此表，仍須簽名或蓋章）</p></li>
<li><p>以上包含申請團隊內各機構、團體等。</p></li>
</ol></td>
<td>□</td>
<td rowspan="3"><p><mark>詳如計畫書拾至拾貳</mark></p>
<p><mark>簽署及掃描後合併至計畫書</mark></p></td>
</tr>
<tr class="odd">
<td>4</td>
<td>無重複申請補助之情事，並簽署「未有重複申請計畫之聲明切結書」</td>
<td>須計畫主持人簽名蓋章並用機構印，聲明所申請之計畫內容、經費等未有任一項目已向衛生福利部、其他部會或地方政府申請並獲得補助，無重複申請補助之情事（含合作團隊內各機構、團體）。</td>
<td>□</td>
</tr>
<tr class="even">
<td>5</td>
<td>同意由主提機構代表申請本計畫，並簽署「參與計畫同意書」</td>
<td>須機構負責人簽名蓋章並用機構印，聲明同意參與主提機構申請本計畫，並明確瞭解計畫內容。</td>
<td>□</td>
</tr>
<tr class="odd">
<td>6</td>
<td>於申請模式中僅申請其中1類</td>
<td>須確認申請單位（含合作團隊內各機構、團體）於本計畫申請模式之4類別中各僅申請1件計畫。</td>
<td>□</td>
<td></td>
</tr>
<tr class="even">
<td>7</td>
<td>合作機構中是否有與主提機構同體系或聯盟</td>
<td><p>與主提機構同體系或聯盟之<u>機構名稱</u>：</p>
<p><u>1.</u></p>
<p><u>2.</u></p>
<p><u>3.</u></p>
<p><u>4.</u></p>
<p><u>5.</u></p>
<p><u>(請自行增列)</u></p></td>
<td><p>□有</p>
<p>□無</p></td>
<td><mark>須與計畫書封面一致</mark></td>
</tr>
</tbody>
</table>

> **※以上資料供檢核，請務必詳實填列。**

# 貳、計畫概要

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>三高問題（高血壓、高血糖和高血脂）不僅是全球主要的慢性病，也是心血管疾病、腎臟病等重大疾病的風險來源，更是國人健康首要大敵，每年導致約6.2萬人死亡，占總死亡人數約30%。政府為全面應對此一問題，推動「三高防治888計畫」，協助民眾早期發現三高問題，並透過健康管理與醫療介入，改善健康狀況，以達成119年降低三高相關慢性病標準化死亡率三分之一的目標。</p>
<p>臺灣即將邁入超高齡社會，男性人口老化速度持續增加，根據衛福部最新癌症登記資料顯示，攝護腺癌已成為臺灣男性發生率第三位之癌症，亦為男性癌症死亡原因前六位，且近十年新診斷人數逐年增加。由於攝護腺癌早期症狀不明顯，即使出現排尿困難、頻尿等情形，也常與良性攝護腺肥大混淆，導致部分患者延誤就醫，許多病人於出現骨轉移、血尿或排尿困難時才被診斷，錯失最佳治療時機。因此台灣有約33%患者在確診時是已經出現遠端轉移的第四期，相較於美國的8%高出甚多，這可能與台灣前列腺癌篩檢不夠普及有關。除了人口高齡化是主要原因外，生活型態改變亦被認為是重要因素之一，例如高脂飲食、代謝症候群及三高問題，都可能與罹癌風險上升相關。</p>
<p>目前攝護腺特異抗原（Prostate-Specific Antigen,
PSA）檢測為國際公認最重要之攝護腺癌篩檢工具，然而我國尚未將 PSA
納入公費癌症篩檢項目，計畫核心願景為「由醫院走入社區，建立男性健康防線」，臺北市立聯合醫院忠孝院區位處臺北市東區醫療服務核心，轄區涵蓋南港、信義及內湖等人口密集區域，並鄰近內湖科學園區、南港科技園區與大量社區聚落，具備推動男性健康促進及癌症預防醫學之重要角色。</p>
<p>過去臺北醫學大學用全民健康保險研究資料庫進行分析，評估前列腺癌病患接受去雄性激素療法之代謝症候群及其他共病影響，初步研究成果顯示去雄性激素療法確實有可能提高患者得到高血壓、高血脂和代謝症侯群的機率，因此在去雄性激素療法仍是局部侵犯型及轉移性攝護腺癌的主要治療時，建議醫師需要將病患是否有高血壓、高血脂或代謝症侯群病史以及是否為其危險族群加入治療評估。(探討前列腺癌病患接受去雄性激素療法之癒後及併發代謝症候群對於病程的影響與可能的藥物預防)</p>
<p>「整合式篩檢」是臺北市衛生局、各區健康服務中心，與醫療院所合作推動的「一站式」健康檢查服務。提供醫院型與社區型，結合政府補助的成人預防保健與癌症篩檢，讓民眾能一次完成多項檢查，早期發現慢性病與癌症。整合式篩檢通常包含以下幾大類項目，實際依個人年齡與資格而定：成人健康檢查：身體理學檢查、血壓、血糖、血脂、肝腎功能及尿液篩檢。五大癌症篩檢：子宮頸抹片、乳房X光攝影、糞便潛血檢查（大腸癌）、口腔黏膜檢查（口腔癌）及低劑量電腦斷層（肺癌）。B、C型肝炎篩檢：提供特定年齡層終身一次免費篩檢。</p>
<p>因此本計畫將結合整合式篩檢，採取「垂直整合與區域聯防」模式，針對 50
歲以上男性以及 45
歲以上具家族病史之高風險男性，以簡單的抽血檢查，即可初步掌握攝護腺健康狀況，並依風險高低安排後續追蹤頻率。</p>
<p>當PSA數值出現異常時，並不一定代表罹患攝護腺癌，也可能是攝護腺肥大、發炎或感染等良性因素，導致指數上升。此時，PHI可做為進一步風險評估的工具，採取整合Total
PSA、Free
PSA與p2PSA三項指標進行計算，提供更具參考價值的風險分數。針對PSA介於4至10之間的「灰色地帶」族群，PHI能協助醫師區分高低風險，也成為臨床上判斷是否進行切片檢查的參考依據，協助臨床判斷。PHI已成為醫師與患者共同決策時的重要輔助工具，協助在過度診斷與延遲治療之間取得更好的平衡。</p>
<p>合作單位臺北市立聯合醫院提供的攝護腺癌治療服務，涵蓋手術、放射線、高強度聚焦超音波（海福刀）、新型賀爾蒙療法、標靶與化學治療等多元方式。治療團隊結合泌尿科、放射腫瘤科、心臟科、腎臟科、營養科、新陳代謝科、家庭醫學科等多科專業，由個管師統整協調，提供病人完整且貼心的照護。希望藉此計畫提高攝護腺癌及代謝疾病的治療成果。並且預防心血管疾病、腎臟病等併發症。</p>
<p>本計畫同時建立創新價值的攝護腺癌結合三高照護模式，提供網路平台及完整個案管理機制，讓每位使用者都能就近找得到資源並使用服務，以獲得適切妥善的照護。</p>
<p>本計畫將提供相關資訊及轉介等支持服務；連結醫療資源，提供個案醫療照護相關服務及傳播健康識能，建構系統能讓病患藉此系統，與醫事人員進行互動或取得正確的衛教相關資訊內容。醫療人員在醫事端能及時回應或監測各生理訊號，對病患進行遠距照護關懷服務。健康諮詢不需到醫院，線上即問即答，更有個管師密切監測，一有異常立刻通知主治醫師及病患、家屬。系統上可看自己的檢驗數值，隨時掌握自己健康狀況。</p>
<p>本院攜手信義健區康服務中心、南港區健康服務中心、內湖區健康服務中心、南港門診部、內湖門診部積極參與，展現公衛管理與醫療協力的高度凝聚力。透過跨單位合作，實踐「早期發現、早期治療」的健康理念，持續為民眾健康把關。結合各區健康服務中心到社區篩檢，找出異常個案，轉介至門診部治療，並且跟各區健康服務中心的衛教服務串連。</p>
<p>台北市健康服務中心的社區三高篩檢，全台獨一無二，各縣市的衛生所都沒有此一模式，成為信義門診部申請健康計畫的特色：運用門診部的醫療資源，結合健康服務中心的社區三高篩檢，有效發掘潛在三高個案，並儘早進入預防醫學服務。本計畫透過主動篩檢、數位化追蹤及智慧健康管理，建立從篩檢到診斷、治療的整合照護流程，以期達成早期發現、降低晚期癌症比例與心血管疾病預防之目標。</p>
<p>執行單位:</p>
<p><img src="ai_agent_readable_plan_assets/image1.png"
style="width:7.08611in;height:4in" /></p>
<p>PSA 篩檢流程</p>
<p><img src="ai_agent_readable_plan_assets/image2.png"
style="width:5.63223in;height:4.50023in" /></p>
<p>攝護腺癌篩檢( PSA 檢測) 問卷</p>
<p>攝護腺癌篩檢( PSA 檢測) 問卷<img
src="ai_agent_readable_plan_assets/image3.png"
style="width:5.76806in;height:3.57708in" /></p>
<p>身高: 公分 體重: 公斤 腰圍: 公分</p>
<p>□葷食</p>
<p>□全素食 □蛋奶素</p>
<p>家族癌症病史</p>
<p>□祖父□父親□舅舅□伯叔□兄弟□兒子□其他</p>
<p>□祖母□母親□姨媽□姑媽□姐妹□女兒□其他</p>
<p>□攝護腺癌</p>
<p>□腎細胞癌</p>
<p>□膀胱癌</p>
<p>□肺癌</p>
<p>□大腸癌</p>
<p>□胃癌</p>
<p>□小腸癌</p>
<p>□乳癌</p>
<p>□卵巢癌</p>
<p>□子宮內膜癌</p>
<p>□子宮頸癌</p>
<p>□其他</p>
<p>國際攝護腺(前列腺)症狀評分問卷(IPSS) International Prostate Symptom
Score</p>
<p>1.排尿後仍有殘尿感</p>
<p>□完全沒有 □5次中有1 次 □少於一半 □約一半 □多於一半 □幾乎每次</p>
<p>2解尿後2小時內，需要再去廁所的頻率</p>
<p>□完全沒有 □5次中有1 次 □少於一半 □約一半 □多於一半 □幾乎每次</p>
<p>3排尿時斷斷續續的現象</p>
<p>□完全沒有 □5次中有1 次 □少於一半 □約一半 □多於一半 □幾乎每次</p>
<p>4從想要小便時到廁所的時間，無法忍尿</p>
<p>□完全沒有 □5次中有1 次 □少於一半 □約一半 □多於一半 □幾乎每次</p>
<p>5有尿流速變慢的現象</p>
<p>□完全沒有 □5次中有1 次 □少於一半 □約一半 □多於一半 □幾乎每次</p>
<p>6需要肚子用力才有辦法解尿的機率</p>
<p>□完全沒有□ 5次中有1 次 □少於一半 □約一半 □多於一半□ 幾乎每次</p>
<p>7從晚上睡著到隔天起床這段期間，需要幾次起床小便?</p>
<p>□完全沒有 □一次 □兩次 □三次 □四次 □五次或以上</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 參、申請單位簡介

1.  機構一

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>信義門診部地址：臺北市信義區大道路 116 號
1樓。設在廣慈衛福大樓一樓的信義門診部，周遭環境及醫院清潔美觀，視野遼闊，交通便捷，在步行100～150公尺的信義路旁就有“信義行政中心（奉天宮）”公車站牌，信義幹線、仁愛幹線以及許多線公車，較遠處，有捷運後山埤站和永春站。</p>
<p>門診部有泌尿科、內科、外科、骨科、小兒科、婦產科、家庭醫學科、復健科、精神科門診，二樓更設有復健部門，提供完整的復健治療設備，輔助復健科門診的業務。全部醫療及醫事服務人力由臺北市立聯合醫院忠孝院區支援。</p>
<p>一樓設有調劑室、檢驗室、X光室，加強門診就地服務的能力。</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  機構二

|     |
|-----|

# 肆、計畫規劃

1.  範疇一

|     |
|-----|

2.  範疇二

|     |
|-----|

3.  範疇三

|     |
|-----|

4.  範疇四

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p><strong>提升重要癌症篩檢率</strong>：針對尚未納入公費的 PSA
檢驗，主動進入社區與企業職場推廣健康促進與專案篩檢，強化男性民眾的健康識能，以期達成早期發現、降低晚期癌症比例之目標。</p></li>
<li><p><strong>落實分級醫療與區域聯防</strong>：建立「信義門診部（初步篩檢）→
忠孝院區（精進診斷與分期治療）」的雙向轉診網絡。篩檢異常個案將由專任個案管理師協助後送至忠孝院區進行數位化追蹤及智慧健康管理</p></li>
<li><p><strong>建立 ESG
與永續管理模式</strong>：透過社區健康支持網絡的形成，讓每位民眾在社區中都能獲得個人化且連續性的健康服務，減輕未來晚期攝護腺癌對社會造成的醫療負擔</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1)  

# 伍、效益評估

1.  績效指標

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 27%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 1%" />
<col style="width: 24%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>範疇</strong></p>
</blockquote></th>
<th><strong>績效指標</strong></th>
<th><strong>衡量或量化基準定義</strong></th>
<th><strong>現況數據</strong></th>
<th colspan="3"><strong>第一階段達成值</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7"><strong>一、優化醫療工作條件</strong></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>二、規劃多元人才培訓</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>三、導入智慧科技醫療</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>四、社會責任醫療永續</strong></p>
</blockquote></td>
<td><p>1.PSA篩檢總人次</p>
<p>2.PSA異常個案追蹤完成率</p>
<p>3.晚期攝護腺癌診斷比例</p>
<p>4.健康篩檢活動的次數</p>
<p>5.社區衛教講座次數</p></td>
<td><p>1.完成PSA抽血檢測之男性人數</p>
<p>2.PSA異常個案完成泌尿科門診追蹤人數 ÷ PSA異常個案總數 ×100%</p>
<p>3.初次晚期攝護腺癌診斷(第四期)</p>
<p>4.健康篩檢活動</p>
<p>5.社區衛教講座(里民講座)</p></td>
<td colspan="2"><p>1. 無系統性社區篩檢</p>
<p>2. 尚未建立追蹤機制</p>
<p>3. 33.9%</p>
<p>4.無系統性社區篩檢</p>
<p>5.無系統性社區篩檢</p></td>
<td><p>1.≥ 3500人次/年</p>
<p>2.≥ 60%</p>
<p>3.減少至30%以下</p>
<p>4.20次篩檢活動/年</p>
<p>5.20次社區衛教/年</p></td>
<td></td>
</tr>
</tbody>
</table>

2.  年度查核點說明

<!-- -->

1)  114年9月1日至115年3月31日。

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>工作內容</strong></td>
<td colspan="2"><strong>查核點</strong></td>
<td rowspan="2"><strong>累計預定進度(%)</strong></td>
<td rowspan="2"><strong>累計預定支用數(元)</strong></td>
<td rowspan="2"><p><strong>查核點說明</strong></p>
<p><strong>(預期成果與效益)</strong></p></td>
</tr>
<tr class="even">
<td><strong>內容狀態</strong></td>
<td><strong>預定完成日期</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

2)  115年4月1日至115年12月31日。

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>工作內容</strong></td>
<td colspan="2"><strong>查核點</strong></td>
<td rowspan="2"><strong>累計預定進度(%)</strong></td>
<td rowspan="2"><strong>累計預定支用數(元)</strong></td>
<td rowspan="2"><p><strong>查核點說明</strong></p>
<p><strong>(預期成果與效益)</strong></p></td>
</tr>
<tr class="even">
<td><strong>內容狀態</strong></td>
<td><strong>預定完成日期</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

1.  

# 陸、出國計畫書

<span class="mark">（限範疇二「規劃多元人才培訓」才可填列，藍字為範例）</span>

> 一、計畫內容：

1)  計畫總表

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 30%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>項次</strong></th>
<th><strong>主題</strong></th>
<th><strong>名稱或內容</strong></th>
<th><strong>時程</strong></th>
<th><p><strong>國別與</strong></p>
<p><strong>城市</strong></p></th>
<th><p><strong>參加</strong></p>
<p><strong>人員數</strong></p></th>
<th><strong>經費需求(元)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>會議</td>
<td>無</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>培訓</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>考察</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>標竿參訪</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>研討會</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>進修</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>(自行敘明)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>經費合計</td>
<td colspan="6">元</td>
</tr>
</tbody>
</table>

2)  出國計畫1：

<!-- -->

1.  目的

|     |
|-----|

2.  詳細內容

|     |
|-----|

3.  行程

| **預估日期** | **行程** | **備註** |
|--------------|----------|----------|
|              |          |          |
|              |          |          |

4.  經費概算

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>項目</strong></th>
<th><strong>金額(臺幣，元)</strong></th>
<th><strong>備註</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>生活費</td>
<td>日支數</td>
<td>301×5×30=45,150</td>
<td><p>1.日本東京日支數額為301美元。</p>
<p>2.美元兌台幣匯率以1：30估算。</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">總計</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ※參與計畫之相關人員因計畫需要必須出國開會、研習、訓練及考察者，得申請本項經費。但出國經費佔計畫總經費之比例以不超過百分之二十為原則。
>
> ※派員出國之人數、天數應力求精簡。每次人數以不超過二人為原則，同一年度內接受本部補助出國之次數，每人以一次為原則。對於第二人之出國經費，本部得視其出國理由之必需性，採不予補助或酌予補助。
>
> ※請詳述預定各出國人員之出國行程、預估經費、天數及地點。
>
> ※機票費及其他費用之標準，請依照行政院「中央各機關（含事業機構）派赴國外進修、研究、實習人員補助項目及數額表」、「國外出差旅費報支要點」規定填列。
>
> ※生活費依「中央政府各機關派赴國外各地區出差人員生活費日支數額」等相關規定編列，並依行政院「國外出差旅費報支要點」規定覈實報支。
>
> ※請將所列各項費用換算為新臺幣，並註明估算匯率。

# 柒、經費規劃

> 一、分年經費總表（項目需依「健康台灣深耕計畫經費支用標準」項目名稱編列，並詳列細目、單價及數量。）
> 單位：新臺幣(元)
>
> <span class="mark">(藍字為範例)</span>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 35%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>經費</th>
<th colspan="7"><strong>補助經費(A)</strong></th>
<th><p><strong>機構</strong></p>
<p><strong>配合款</strong></p>
<p><strong>(F)</strong></p></th>
<th><p><strong>總計</strong></p>
<p><strong>(G=A+F)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="31">第一階段</td>
<td colspan="8"><strong>經常門(B)</strong></td>
<td rowspan="31"></td>
</tr>
<tr class="even">
<td colspan="8"><strong>人事費(C)</strong></td>
</tr>
<tr class="odd">
<td>項目</td>
<td>單價</td>
<td colspan="2">單位</td>
<td>數量</td>
<td>合計</td>
<td>支用說明或編列基準</td>
<td></td>
</tr>
<tr class="even">
<td>專任助理</td>
<td>36,300元</td>
<td colspan="2">2人/月</td>
<td>27個月</td>
<td>980,100</td>
<td>大學畢業年終獎金1.5月</td>
<td></td>
</tr>
<tr class="odd">
<td>勞保費</td>
<td>2,032</td>
<td colspan="2">2人/月</td>
<td>24個月</td>
<td>48,768</td>
<td>以114年健保級距、勞保級距、勞退6%計算(3,675+2,032+2,520)
*15月*8人=987,240元</td>
<td></td>
</tr>
<tr class="even">
<td>健保費</td>
<td>3,675</td>
<td colspan="2">2人/月</td>
<td>24個月</td>
<td>88,200</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>公提勞工退休金</td>
<td>2,520</td>
<td colspan="2">2人/月</td>
<td>24個月</td>
<td>60,480</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td><mark>小計</mark></td>
<td><mark>1,177,548</mark></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>業務費(D)</strong></td>
</tr>
<tr class="even">
<td>項目</td>
<td>單價</td>
<td>單位</td>
<td colspan="2">數量</td>
<td>合計</td>
<td>支用說明或編列基準</td>
<td></td>
</tr>
<tr class="odd">
<td>PSA 檢查</td>
<td>500</td>
<td>次</td>
<td colspan="2">3500</td>
<td>1,750,000</td>
<td>不必符合健保特殊適應症，使用自費價</td>
<td></td>
</tr>
<tr class="even">
<td>攝護腺健康指數（PHI）</td>
<td>2300</td>
<td>次</td>
<td colspan="2">175</td>
<td>402,500</td>
<td>PHI: 總PSA、游離PSA及 pro2PSA計算，若是PSA篩檢異常，數值介於4.0 ~
10.0 ng/ml之間不必符合健保特殊適應症，使用自費價</td>
<td></td>
</tr>
<tr class="odd">
<td>臨時人員費用</td>
<td>534</td>
<td>小時</td>
<td colspan="2">480</td>
<td>256,320</td>
<td>護理師、醫事檢驗師 534元/時* 20場篩檢(每場6小時)*4人</td>
<td></td>
</tr>
<tr class="even">
<td>臨時人員費用</td>
<td>415</td>
<td>小時</td>
<td colspan="2">480</td>
<td>199,200</td>
<td>行政人員 415元/時* 20場篩檢(每場6小時) *4人</td>
<td></td>
</tr>
<tr class="odd">
<td>文具紙張</td>
<td>5,000</td>
<td>批</td>
<td colspan="2">5</td>
<td>25,000</td>
<td>需油墨、碳粉匣、紙張、文具</td>
<td></td>
</tr>
<tr class="even">
<td>郵電</td>
<td>10,000</td>
<td>批</td>
<td colspan="2">5</td>
<td>50,000</td>
<td>本計畫所需之郵資及電話費</td>
<td></td>
</tr>
<tr class="odd">
<td>審查費/出席費</td>
<td>2500元</td>
<td>次</td>
<td colspan="2">40</td>
<td>100,000</td>
<td><p>需聘請專家學者</p>
<p>進行實質審查並提供書面意見</p></td>
<td></td>
</tr>
<tr class="even">
<td>講座鐘點費</td>
<td>2,000</td>
<td>次</td>
<td colspan="2">20</td>
<td>40,000</td>
<td><p>訓練研討活</p>
<p>動之授課講演鐘點費或實習指導費：外聘2000內聘1000</p></td>
<td></td>
</tr>
<tr class="odd">
<td>調查訪問費</td>
<td>100</td>
<td>份</td>
<td colspan="2">3,000</td>
<td>300,000</td>
<td><p>需問卷調查之填表或訪視費。</p>
<p>問卷調查或訪視時所需之禮品或宣導品費用。每份100元</p></td>
<td></td>
</tr>
<tr class="even">
<td>印刷</td>
<td>20,000</td>
<td>批</td>
<td colspan="2">3</td>
<td>60,000</td>
<td>本計畫所需之印刷問卷、宣傳單\海報費用</td>
<td></td>
</tr>
<tr class="odd">
<td>受試者營養費</td>
<td>100</td>
<td>份</td>
<td colspan="2">3,000</td>
<td>300,000</td>
<td>每人次100元</td>
<td></td>
</tr>
<tr class="even">
<td>電腦處理費</td>
<td>5,000</td>
<td>批</td>
<td colspan="2">6</td>
<td>30,000</td>
<td><p>資料譯碼及鍵入費、電腦使用時間費、</p>
<p>硬碟、隨身碟、光碟片及報表紙</p></td>
<td></td>
</tr>
<tr class="odd">
<td>資料處理費</td>
<td>100</td>
<td>份</td>
<td colspan="2">3,000</td>
<td>300,000</td>
<td>醫療數據彙整、分析、統計、預測預算等費用</td>
<td></td>
</tr>
<tr class="even">
<td>圖書及資料蒐集費</td>
<td>10,000</td>
<td>批</td>
<td colspan="2">5</td>
<td>50,000</td>
<td><p>購置圖書應詳列其名</p>
<p>圖書費每本需低於一萬元。</p>
<p>(6本)</p>
<h1
id="campbell-walsh-wein-urology-第13版分成volume-123三本-共20321元">Campbell
Walsh Wein Urology 第13版分成Volume 1、2、3三本 共20321元。</h1>
<p>其他參考書目</p></td>
<td></td>
</tr>
<tr class="odd">
<td>材料費</td>
<td>46.05</td>
<td>次</td>
<td colspan="2">3,000</td>
<td>138,150</td>
<td><p>1.採血針(Blood Collection Needle)4.95元。</p>
<p>2.試管(Blood Collection Tubes)6.1元。</p>
<p>3.前列腺特異性抗原檢驗試劑(PSA)35元。</p></td>
<td></td>
</tr>
<tr class="even">
<td>餐費</td>
<td>100</td>
<td>人</td>
<td colspan="2">4</td>
<td>20,000</td>
<td>每人次最高一百元。宣傳活動及相關會議所需之誤餐費預計：100元*50人*4次</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><mark>小計</mark></td>
<td><mark>3,981,170</mark></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>雜支費</td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td><p>最高以業務費扣除國外旅費</p>
<p>後之金額百分之五為上限，</p>
<p>且不得超過十萬元。</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><strong>資本門(E)</strong></td>
</tr>
<tr class="even">
<td>項目</td>
<td>單價</td>
<td>單位</td>
<td colspan="2">數量</td>
<td>合計</td>
<td>支用說明或編列基準</td>
<td></td>
</tr>
<tr class="odd">
<td>診間廣播機</td>
<td>1萬元</td>
<td>台</td>
<td colspan="2">10</td>
<td>10萬元</td>
<td>請 10 號 王小明，至一號診間報到</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>問卷用平板電腦</td>
<td>3萬元</td>
<td>台</td>
<td colspan="2">3</td>
<td>9萬元</td>
<td>與醫療系統（HIS/院內電腦）連線</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>全自動藍芽傳輸身高體重計(須外加軟體)</td>
<td>9萬元</td>
<td>台</td>
<td colspan="2">2</td>
<td>18萬元</td>
<td>三高篩檢自動化傳輸，避免人工抄寫錯誤</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>藍芽血壓計(須外加軟體)</td>
<td>9萬元</td>
<td>台</td>
<td colspan="2">2</td>
<td>18萬元</td>
<td>三高篩檢自動化傳輸，避免人工抄寫錯誤</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>微電腦藍芽傳輸液晶視力檢查表(須外加軟體)</td>
<td>8萬元</td>
<td>台</td>
<td colspan="2">2</td>
<td>16萬元</td>
<td>三高篩檢自動化傳輸，避免人工抄寫錯誤</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>診所專用叫號機與麥克風系統</td>
<td>1萬元</td>
<td>台</td>
<td colspan="2">6</td>
<td>6萬元</td>
<td>能大幅降低櫃檯負擔，避免護理人員喊到聲音沙啞</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>碎紙機</td>
<td>1萬元</td>
<td>台</td>
<td colspan="2">4</td>
<td>4萬元</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td>小計81萬元</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 二、各範疇經費配置表 單位：新臺幣(元)

<table style="width:100%;">
<colgroup>
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2" rowspan="2">範疇</td>
<td colspan="2"><strong>範疇一</strong></td>
<td colspan="2"><strong>範疇二</strong></td>
<td colspan="2"><strong>範疇三</strong></td>
<td colspan="2"><strong>範疇四</strong></td>
<td colspan="6"><strong>總計(G)</strong></td>
</tr>
<tr class="even">
<td>補助款</td>
<td>配合款</td>
<td>補助款</td>
<td>配合款</td>
<td>補助款</td>
<td>配合款</td>
<td>補助款</td>
<td>配合款</td>
<td colspan="3"><strong>補助款(A)</strong></td>
<td colspan="3"><strong>配合款(F)</strong></td>
</tr>
<tr class="odd">
<td rowspan="9">申請數</td>
<td rowspan="9">第一階段</td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="9"></td>
<td rowspan="2">經常門</td>
<td>人事費</td>
<td></td>
<td rowspan="2">經常門</td>
<td>人事費</td>
<td></td>
</tr>
<tr class="even">
<td>業務費</td>
<td></td>
<td>業務費</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">資本門</td>
<td></td>
<td colspan="2">資本門</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="6"></td>
</tr>
<tr class="even">
<td colspan="3"><p><strong><mark>資本門占補助款(A)</mark></strong></p>
<p><strong><mark>百分比(%)</mark></strong></p></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td
colspan="6"><strong><mark>機構配合款(F)占總經費(G)百分比(F/G%)</mark></strong></td>
</tr>
<tr class="odd">
<td colspan="6"></td>
</tr>
</tbody>
</table>

# 捌、人力配置表（受補助單位人員）

| 類別 | 姓名 | 現職 | 在本計畫內擔任之具體工作性質、項目及範圍 |
|------|------|------|------------------------------------------|
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |
|      |      |      |                                          |

#  玖、其他

如附件、表目錄、圖目錄、或其他相關單位分工及配合事項

| 如報價單等 |
|------------|

# ** **拾、公職人員利益衝突迴避自主檢核表

**衛生福利部補助案件**

**公職人員利益衝突迴避自主檢核表**

> **114.3.6版**

一、依公職人員利益衝突迴避法(下稱利衝法)第14條規定，申請人如為**公職人員或其關係人**，除非符合下列例外情形，否則不得與公職人員服務或受其監督之機關申請補助：

1)  基於法定身分依法令規定申請之補助。

2)  對公職人員之關係人依法令規定以公開公平方式辦理之補助。

3)  禁止其補助反不利於公共利益且經補助法令主管機關核定同意之補助。

4)  一定金額以下之補助。

二、上述例外情形得向本部申請之補助案件，若為依第(二)、(三)款規定辦理者，申請人應於<u>補助核定前</u>主動於申請文件內據實表明其身分關係，違反者，得處新臺幣5萬元以上50萬元以下罰鍰，並得按次處罰。

三、為協助補助申請人於申請本部補助案件時自我檢視是否符合利衝法相關規範，請申請人確實依據下列情形填寫本檢核表：

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 52%" />
<col style="width: 16%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>項次</strong></th>
<th><strong>自主檢核項目</strong></th>
<th><strong>檢核結果</strong></th>
<th><strong>法律規範</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>貴單位(法人、團體)是否有利衝法規範之<strong>公職人員</strong>擔任負責人、董事、獨立董事、監察人、經理人或相類似職務?</td>
<td>是□/否□</td>
<td
rowspan="3"><p>如補助案係採一、(二)款方式辦理，勾選結果其一為「是」，即需填寫「身分揭露表」。</p>
<p>如補助案係以「非公開方式」辦理，勾選結果其一為「是」，即屬利衝法第14條禁止補助之行為態樣，不得進行補助行為（是否有一、（三）情形，得例外為補助行為需個案認定，並應填寫「身分揭露表」）。</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>貴單位(法人、團體)是否有利衝法規範之<strong>公職人員之配偶或共同生活之家屬</strong>擔任負責人、董事、獨立董事、監察人、經理人或相類似職務?</td>
<td>是□/否□</td>
</tr>
<tr class="odd">
<td>3</td>
<td>貴單位(法人、團體)是否有利衝法規範之<strong>公職人員之二親等以內親屬</strong>擔任負責人、董事、獨立董事、監察人、經理人或相類似職務?</td>
<td>是□/否□</td>
</tr>
</tbody>
</table>

申請補助單位名稱：

計畫主持人簽名或蓋章：

填表日期： 年 月 日

備註：

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>與本部業務往來時，適用利衝法第2條之「公職人員」範圍：</strong></p>
<p>一、總統、副總統。</p>
<p>二、行政院正(副)院長、行政院正(副)秘書長、行政院政務委員。</p>
<p>三、立法委員、監察委員。</p>
<p>四、本部部長、政務次長、常務次長、主任秘書。</p>
<p>五、本部秘書處【專責承辦採購業務】、會計處【依會計法令辦理內部審核業務】與政風處之處長、副處長及科長。</p>
<p><strong>利衝法第3條之「關係人」範圍：</strong></p>
<p>一、配偶或共同生活之家屬。</p>
<p>二、二親等以內親屬。</p>
<p>三、公職人員、上述第一項與第二項所列人員擔任負責人、董事、獨立董事、監察人、經理人或相類似職務之<strong>營利事業、非營利之法人及非法人團體</strong>。<strong>但屬政府或公股指派、遴聘代表或由政府聘任者，不包括之。</strong></p>
<p><strong>二親等以內親屬關係如下：</strong></p>
<p>血親:</p>
<p>一親等：父母、子女。</p>
<p>二親等：兄弟姊妹、(外)祖父母、(外)孫子女。</p>
<p>姻親:</p>
<p>一親等：子媳、女婿、繼父、繼母、公婆、岳父母、繼子、繼女、配偶之子媳、女婿。</p>
<p>二親等：兄嫂、弟媳、姐夫、妹夫、(外)孫子媳、(外)孫女婿、配偶之兄弟姐妹、配偶之(外)祖父母、配偶之(外)孫子女、配偶之兄嫂、弟媳、姐夫、妹夫、配偶之(外)孫子媳、(外)孫女婿。</p>
<p><strong>一定金額定義：</strong></p>
<blockquote>
<p>指每筆新臺幣1萬元。同年度（每年1月1日起至12月31日止）同一補助對象合計不逾10萬元。</p>
</blockquote>
<p>※除上述表列中之「公職人員」遇案須迴避外，其餘公務員雖非利衝法之規範對象，惟於執行職務時，涉及本人或關係人之利益，仍應注意公務員服務法、行政程序法等相關迴避規定。</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**公職人員利益衝突迴避法第14條第2項**

<span class="mark">填寫範例請參考「行政院人事行政總處」</span>

**公職人員及關係人身分關係揭露表範本**

**【A.事前揭露】：本表由公職人員或關係人填寫**

（公職人員或其關係人與公職人員服務之機關團體或受其監督之機關團體為補助或交易行為前，應主動於申請或投標文件內據實表明其身分關係）

**※交易或補助對象屬公職人員或關係人者，請填寫此表。非屬公職人員或關係人者，免填此表。**

表1：

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 41%" />
</colgroup>
<tbody>
<tr class="odd">
<td>參與交易或補助案件名稱：</td>
<td>案號： （無案號者免填）</td>
</tr>
<tr class="even">
<td colspan="2">本案補助或交易對象係公職人員或其關係人：</td>
</tr>
<tr class="odd">
<td colspan="2"><p>□公職人員（勾選此項者，無需填寫表2）</p>
<p>姓名： 服務機關團體： 職稱：</p></td>
</tr>
<tr class="even">
<td colspan="2">□公職人員之關係人（勾選此項者，請繼續填寫表2）</td>
</tr>
</tbody>
</table>

表2：

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 28%" />
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><p>公職人員：</p>
<p>姓名： 服務機關團體： 職稱：</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><p>關係人 關係人（屬自然人者）：姓名</p>
<p>關係人（屬營利事業、非營利之法人或非法人團體）：</p>
<p>名稱 統一編號 代表人或管理人姓名</p></td>
</tr>
<tr class="even">
<td></td>
<td
colspan="4"><strong>關係人與公職人員間係第3條第1項各款之關係</strong></td>
</tr>
<tr class="odd">
<td>□第1款</td>
<td colspan="4">公職人員之配偶或共同生活之家屬</td>
</tr>
<tr class="even">
<td>□第2款</td>
<td colspan="2">公職人員之二親等以內親屬</td>
<td colspan="2">稱謂：</td>
</tr>
<tr class="odd">
<td>□第3款</td>
<td colspan="2">公職人員或其配偶信託財產之受託人</td>
<td colspan="2">受託人名稱：</td>
</tr>
<tr class="even">
<td><p>□第4款</p>
<p>（請填寫abc欄位）</p></td>
<td><p>a.請勾選關係人係屬下列何者：</p>
<p>□營利事業</p>
<p>□非營利法人</p>
<p>□非法人團體</p></td>
<td colspan="2"><p>b.請勾選係以下何者擔任職務：</p>
<p>□公職人員本人</p>
<p>□公職人員之配偶或共同生活之家屬。姓名：</p>
<p>□公職人員二親等以內親屬。</p>
<p>親屬稱謂： (填寫親屬稱謂例如：兒媳、女婿、兄嫂、弟媳、連襟、妯娌)</p>
<p>姓名：</p></td>
<td><p>c.請勾選擔任職務名稱：</p>
<p>□負責人</p>
<p>□董事</p>
<p>□獨立董事</p>
<p>□監察人</p>
<p>□經理人</p>
<p>□相類似職務：</p></td>
</tr>
<tr class="odd">
<td>□第5款</td>
<td>經公職人員進用之機要人員</td>
<td colspan="3">機要人員之服務機關： 職稱：</td>
</tr>
<tr class="even">
<td>□第6款</td>
<td>各級民意代表之助理</td>
<td colspan="3">助理之服務機關： 職稱：</td>
</tr>
</tbody>
</table>

填表人簽名或蓋章： 此致機關：

（<u>填表人屬營利事業、非營利之法人或非法人團體者，請一併由該「事業法人團體」**及**「負責人」蓋章</u>）

備註：

填表日期： 年 月 日

#  拾壹、未有重複申請計畫之聲明切結書

**未有重複申請計畫之聲明切結書**

本人謹代表本申請機構： 及合作機構：

，申請衛生福利部補（捐）助計畫-『健康台灣深耕計畫』。本計畫申請內容、經費等未有向衛生福利部及所屬機關、其他部會或地方政府申請，且無重複獲得補助之情事，如有不實，願負法律責任，特此聲明，以昭公信。

此致

衛生福利部

計畫主持人： (簽章)

機構全銜： (用印)

中華民國 年 月 日

# ** **拾貳、參與計畫同意書

**<u>(機構全銜)</u> 參與計畫同意書**

本機構： ，同意參與主提機構

**<u>(主提機構全銜)</u>**
申請衛生福利部補（捐）助計畫-『健康台灣深耕計畫』，且明確瞭解計畫內容，並配合計畫相關規定辦理，願負法律責任，特此聲明，以昭公信。

此致

衛生福利部

機構負責人： (簽章)

機構全銜： (用印)

中華民國 年 月 日

<span id="_Toc207977409" class="anchor"></span>拾參、審查意見回復表

| 執行機構                     |         |              | 主持人   |                      |          |
|------------------------------|---------|--------------|----------|----------------------|----------|
| 計畫名稱                     |         |              |          |                      |          |
| 計畫編號                     | A1-0001 |              | 執行期程 | 計畫核定日-115/12/31 |          |
| 委員意見                     |         | 執行單位回復 |          |                      | 修正位置 |
| **範疇一：優化醫療工作條件** |         |              |          |                      |          |
|                              |         |              |          |                      |          |
| **範疇二：規劃多元人才培育** |         |              |          |                      |          |
|                              |         |              |          |                      |          |
| **範疇三：導入智慧科技醫療** |         |              |          |                      |          |
|                              |         |              |          |                      |          |
| **範疇四：社會責任醫療永續** |         |              |          |                      |          |
|                              |         |              |          |                      |          |
