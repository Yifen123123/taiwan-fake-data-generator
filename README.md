# 台灣假資料產生器

這是一個使用 Python、Streamlit 與 pandas 製作的台灣測試資料產生工具，可快速建立適合開發、展示與測試使用的假資料表格。

所有輸出內容皆為程式隨機產生的假資料，僅供測試用途，不應視為真實個人資料。

## 功能特色

- 產生台灣風格的假資料
- 支援欄位：
  - 中文姓名
  - Gmail 格式信箱
  - 台灣手機號碼
  - 台灣地址
  - 台灣身分證字號
- 支援一次產生 `10`、`50`、`100`、`500` 筆
- 以表格方式顯示，方便像 Excel 一樣閱讀
- 可下載 `CSV` 與 `Excel（.xlsx）`

## 專案結構

```text
.
├── app.py
├── generators
│   ├── __init__.py
│   ├── address_generator.py
│   ├── contact_generator.py
│   ├── dataset_generator.py
│   ├── id_generator.py
│   └── name_generator.py
├── requirements.txt
├── README.md
└── utils
    ├── __init__.py
    ├── exporters.py
    └── tw_id.py
```

## 安裝方式

建議先建立虛擬環境：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

如果你使用的是 Windows：

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 執行方式

在專案根目錄執行：

```bash
streamlit run app.py
```

啟動後，瀏覽器會開啟本機頁面；如果沒有自動開啟，可在 terminal 中查看 Streamlit 顯示的本機網址。

## 使用說明

1. 開啟頁面後，選擇要產生的資料筆數。
2. 按下「產生假資料」按鈕。
3. 在頁面中檢視表格結果。
4. 依需求下載 CSV 或 Excel 檔案。

## 注意事項

- 本工具輸出的姓名、地址、手機與身分證字號皆為假資料。
- 台灣身分證字號符合基本格式與檢查碼規則，適合用於測試驗證流程。
- 為降低重複率，程式會盡量避免同次產生重複的姓名、信箱、手機與身分證字號。
