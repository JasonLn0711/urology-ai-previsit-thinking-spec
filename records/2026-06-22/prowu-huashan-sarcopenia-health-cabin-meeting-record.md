# 2026-06-22 16:29 Prof. Wu / Prof. Chiang / Ken Sync

Status: captured

## Source

- Meeting time: 2026-06-22 16:29-17:32
- Participants: 吳育德老師, 國防醫學院江老師, 慧誠智醫余總 Ken, Jason
- Corrected transcript:
  `sources/transcript_260622_1629_withProWu_corrected_v2.txt`
- Correction notes:
  `sources/transcript_260622_1629_correction_notes.md`
- Planning source archive:
  `../planning-everything-track/data/knowledge/personal/sources/2026-06-22-prowu-huashan-sarcopenia-health-cabin-sync/`

## Decision Summary

本次會議把華山 `高齡者 AI 步態與肌少症風險篩檢暨閉環整合照護導流計畫` 的智慧互動與健康艙段落收斂成三個 proposal-safe 決策：

1. 機器人主要寫成衛教、導覽、流程說明、安全提醒與現場互動輔助；computer vision / 影像篩檢是 optional 模組。
2. 收案設計要從第一年就包含陽性個案，並保留年齡、性別、族群來源、陰性/陽性比例與 reference-standard label。
3. 健康艙需要明確定義在肌少症計畫中的用途，包含生理量測、人口學資料、肌少症相關欄位、問卷互動、QR/report、雲端資料流、HIS/FHIR-ready 介接與紅黃綠燈導流。

## Group-Post Version

```text
各位老師好，我先把今天 16:29 會議的三個重點整理如下：

1. 機器人定位：computer vision / 影像篩檢模組可以作為 optional 模組，但 proposal 主要定位應放在衛教、導覽、流程說明與現場互動輔助。現場肌少症篩檢仍需要人員維護安全，機器人不宜被寫成完全取代照護人員的核心量測主體。

2. 收案與模型驗證：第一年不能只收社區健康居民或陰性個案。若要承接既有影像篩檢或建立 STS5 / TUG / 步態預測模型，需要納入陽性個案，並注意年齡、性別、族群來源與陽性/陰性比例，才能支撐後續模型信效度、外部效度與 proposal KPI。

3. 健康艙在肌少症計畫的用途：健康艙適合承擔基礎生理量測、資料整合、問卷互動、QR/report、雲端資料流與 HIS/FHIR-ready 後續介接。下一步要釐清健康艙可量測哪些與肌少症相關的資料，例如身高體重、BIA、血壓、血糖血脂、握力或外部匯入資料，以及如何和 STS5 / TUG / 步態、紅黃綠燈分流、衛教與回診/健促班導流串起來。

我會把這三點帶到後續 Kevin / 美如主任 / 慧誠智醫討論，先確認健康艙、機器人、行動量測包與資料流各自的角色，再回頭調整華山計畫書的 KPI 與驗證設計。
```

## Transcript Evidence

- `00:08:50-00:10:34`: 華山計畫以 STS5、TUG、步態、肌少症/跌倒風險預測、COM-B、APP/LINE 居家追蹤與紅黃綠燈導流為核心。
- `00:20:29-00:25:37`: 影像篩檢放到 AMR / 機器人上有現場安全與高齡者互動挑戰；篩檢中心仍需要人員維護安全。
- `00:29:13-00:31:08`: 智慧互動終端可做語音與螢幕引導、流程說明、衛教與導覽；proposal 不宜把它主要寫成影像量測機器人。
- `00:33:10-00:39:45`: 承接或建立預測模型前，需要資料庫來源、樣本數、陽性/陰性比例、年齡性別分布、外部效度與預測力。
- `00:42:38-00:43:06`: 社區樣本多為陰性，陽性個案收案是必要設計。
- `00:47:00-00:56:13`: 健康艙 / station / 行動包主要連到 vital sign、生理量測、雲端、QR report、HIS/FHIR-ready 資料流與 HAH 居家照護方向。
- `01:01:45-01:02:22`: 吳老師正式交辦 Jason 整理三點：機器人 CV optional / 衛教為主、收案要有陽性且注意年齡性別、健康艙用在肌少症的用途。

## Proposal Writing Implications

### Robot Scope

Use this proposal-safe sentence:

```text
智慧互動終端 / 機器人提供流程引導、衛教、導覽、安全提醒與現場互動輔助；影像篩檢模組可作為選配或後續驗證模組，於完成設備、場域、人員安全與模型效度確認後納入擴充。
```

### Validation Scope

Model and KPI language should be backed by an explicit evidence plan:

- positive and negative case source;
- age and sex distribution;
- community / health-center / LTC / hospital source label;
- STS5, TUG, gait, grip strength, calf circumference, BIA, SARC-F, SPPB, or
  other reference-standard labels;
- device and camera setup;
- AUC, sensitivity, specificity, external validation, TFDA/IRB status.

### Health Cabin Scope

Use the Health Cabin as the fixed measurement and data-integration anchor:

```text
健康艙整合基本人口學、生理量測、肌少症相關量測資料、互動問卷、衛教回饋、QR 報告與後續 HIS/FHIR-ready 資料流，支援紅黃綠燈分流、家醫科或健康促進課程導流，以及年度 KPI evidence。
```

## Open Questions For Kevin / 美如主任 / 慧誠智醫

1. Kevin v3 中「智慧互動終端」是否正式改成衛教/導覽/流程引導為主，CV 作為 optional？
2. 華山第一年陽性個案要從哪裡來：健康服務中心、養護中心、長照據點、醫院門診、還是既有合作資料庫？
3. 健康艙可原生量測哪些肌少症相關欄位，哪些需外部匯入？
4. BIA、握力、小腿圍、STS5、TUG、步態、血壓、血糖血脂、基本人口學與問卷是否能整合成同一份 QR/report？
5. FHIR/HIS-ready 是 live integration、JSON/ERD 設計、mapping draft，還是 future activation gate？
6. 現有影像篩檢模型是否有可提供的資料來源、樣本數、陽性/陰性比例、年齡性別分布、外部驗證、AUC/敏感度/特異度與 TFDA/IRB 狀態？

## Scope Controls

- 慧誠智醫 / imedtac capability is proposal context and discovery material until procurement, maintenance, data-processing, and deployment responsibilities are confirmed.
- 高榮、奇美、台南、市政府點位、中正區與華山健康中心等部署或價格資訊 remain meeting statements until the partner provides supporting evidence.
- Health Cabin medical use should stay in a staff-review / screening-support / governed workflow scope until intended use, device classification, validation, privacy, cybersecurity, and hospital integration gates are confirmed.
