# 🌿 今天的問候圖

給家人轉發到 LINE 的每日問候圖網站。
網址：https://10wang-creat.github.io/goji-morning/

圖片來源是 IG「遇見中藥 Meet the Herbs」的兩類貼文：

- **隨手語錄**：每週第 5 個資料夾（週五），每個主題 3 張
- **金句海報**：角色配一句話的單張海報。W34 以前在週三第 3 張，W35 起在**週四第 3 張**

---

## 網站怎麼用（給媽媽）

1. 打開就是**今天的圖**，每天自動換，而且只挑當季適合的（11 月不會跳出端午、三伏天）
2. 按綠色的 **「傳給家人」** → 跳出分享選單 → 選 LINE → 選群組
3. 喜歡的圖按 **「♡ 收藏」**，之後在「看全部 → ❤️ 收藏」裡找得到
4. 「看全部」上面有六顆按鈕：當季、最新、收藏、金句、語錄、節慶

收藏是存在那支手機的瀏覽器裡，換手機或清除瀏覽資料就會不見。

---

## 每週更新流程

1. 新一週的圖照原本習慣放進 `創作素材/IG貼圖/2026/<編號. 主題>/1～5/`
2. 在 `tools/slugs.py` 加一行「編號 → 英文代號」，在 `tools/seasons.json` 加一行「編號 → 月份」
3. 跟 Claude 說「更新問候圖網站」（會跑 `tools/update.py`，自動抓語錄、抓金句、做縮圖、重建清單）
4. GitHub Desktop → Commit → Push，一兩分鐘後網站自動更新

不想上架的語錄圖：在 `tools/exclude.txt` 加一行 `代號/檔名.jpg`。
不想收某一週的金句：在 `tools/gold_exclude.txt` 加一行編號。
改完再跑一次 `tools/gen_data.py` 就好。

---

## 資料夾結構

```
index.html            網站本體（單一檔案）
data.js               圖片清單（自動產生，勿手改）
images/<代號>/N.jpg    隨手語錄，1080px
gold/<代號>.jpg        金句海報，1080px
thumbs/…              圖庫用的 400px 小縮圖（自動產生）
icons/ manifest.json  加到主畫面用的圖示與設定
tools/
  update.py           一鍵更新（依序跑下面四支）
  build.py            抓各主題第 5 個資料夾 → images/
  build_gold.py       抓編號 39 之後各主題第 4 個資料夾第 3 張 → gold/
  build_thumbs.py     產生 thumbs/
  gen_data.py         產生 data.js
  slugs.py            編號 → 英文代號
  seasons.json        編號 → 適合月份、是否為節慶（春節／端午／中秋）
  exclude.txt         不上架的語錄圖
  topics.json         build.py 產生的主題清單
```

---

## 首頁「今天的圖」怎麼挑

- 一般主題：只在它的月份與前後各一個月出現
- 節慶主題（春節、端午、中秋）：只在節日前後出現，節日當天與前一天優先顯示
- 同一個月內不會重複；農曆節日的日期寫在 `index.html` 的 `FEST` 表，目前排到 2030 年
