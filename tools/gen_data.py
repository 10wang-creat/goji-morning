# -*- coding: utf-8 -*-
"""讀 topics.json + exclude.txt + seasons.json + gold/ 資料夾，產生 data.js（新的在前）"""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(D, "tools")
topics = json.load(open(os.path.join(T, "topics.json"), encoding="utf-8"))
seasons = json.load(open(os.path.join(T, "seasons.json"), encoding="utf-8"))
ex = {l.strip() for l in open(os.path.join(T, "exclude.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")}
out = []; nq = ng = 0
for t in topics:
    files = [f for f in t["files"] if "%s/%s" % (t["slug"], f) not in ex]
    gold = os.path.exists(os.path.join(D, "gold", t["slug"] + ".jpg"))
    if not files and not gold: continue
    s = seasons.get(str(t["num"]), {})
    row = {"slug": t["slug"], "name": t["name"], "num": t["num"], "m": s.get("m", 0), "files": files, "gold": gold}
    if s.get("fest"): row["fest"] = s["fest"]
    out.append(row); nq += len(files); ng += gold
out.sort(key=lambda x: -x["num"])
js = "// 由 tools/gen_data.py 自動產生，請勿手動編輯\nconst TOPICS = [\n" + ",\n".join(" " + json.dumps(r, ensure_ascii=False) for r in out) + "\n];\n"
open(os.path.join(D, "data.js"), "w", encoding="utf-8").write(js)
print("主題 %d｜語錄 %d 張｜金句 %d 張｜合計 %d" % (len(out), nq, ng, nq + ng))
