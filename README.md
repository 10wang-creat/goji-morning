# 🌿 今天的問候圖

給家人轉發到 LINE 的每日問候圖網站。
圖片來源：IG「遇見中藥 Meet the Herbs」每週五的「隨手語錄」。

網址：https://goji-morning.vercel.app

---

## 網站怎麼用（給媽媽）

1. 打開網站 → 最上面就是**今天的圖**（每天自動換一張）
2. 按綠色的 **「傳給家人」** → 手機會直接跳出分享選單 → 選 LINE → 選群組
3. 想換別張 → 按「換一張」，或按「看全部」慢慢挑

手機瀏覽器如果不支援直接分享，會自動跳出「怎麼傳到 LINE」的三步驟教學。

建議把網站**加到手機主畫面**，用起來就像一個 App。

---

## 資料夾結構

```
index.html          網站本體（單一檔案，含樣式與程式）
data.js             圖片清單（自動產生，勿手改）
manifest.json       加到主畫面用的設定
icons/              App 圖示
images/<藥材>/N.jpg  圖片（已壓縮到 1080px、約 100KB）
tools/              產圖與產清單的腳本
  build.py          從 IG貼圖 資料夾抓「週五：隨手語錄」→ 壓縮進 images/
  gen_data.py       讀 topics.json + exclude.txt → 產生 data.js
  exclude.txt       不想上架的圖（無文字的底圖、出圖瑕疵）
  topics.json       build.py 產生的主題清單
  sheet.py          把所有圖拼成總覽圖，方便一次檢查
```

---

## 每週更新流程

1. 把新一週的圖放進 `創作素材/IG貼圖/<年>/<編號. 藥材>/5.../`（照原本習慣即可，資料夾叫 `5`、`週五`、`星期五` 都可以）
2. 在 `tools/build.py` 的 `SLUG` 對照表加上新編號 → 英文代號
3. 跟 Claude 說「更新問候圖網站」，會自動跑 `build.py` + `gen_data.py`
4. GitHub Desktop → Commit → Push → Vercel 自動更新

不想上架的圖，在 `tools/exclude.txt` 加一行 `藥材代號/檔名.jpg`，再重跑 `gen_data.py`。

---

## 為什麼改版

舊版每張圖是 6MB 的原始 PNG，手機讀很慢；要點兩層才能存圖，也沒有「今天推薦哪張」。
新版把圖壓到約 100KB、首頁只給一張今日圖、分享改成一鍵叫出系統分享選單。
