# -*- coding: utf-8 -*-
"""讀 tools/topics.json + tools/exclude.txt，產生 data.js"""
import json, os
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
topics=json.load(open(D+"/tools/topics.json",encoding="utf-8"))
ex=set()
for line in open(D+"/tools/exclude.txt",encoding="utf-8"):
    line=line.strip()
    if line and not line.startswith("#"): ex.add(line)
out=[]
for t in topics:
    files=[f for f in t["files"] if "%s/%s"%(t["slug"],f) not in ex]
    if not files: continue
    out.append({"slug":t["slug"],"name":t["name"],"year":t["year"],"num":t["num"],"files":files})
out.sort(key=lambda x:-x["num"])
js="// 由 tools/gen_data.py 自動產生，請勿手動編輯\nconst TOPICS = " + json.dumps(out,ensure_ascii=False,indent=1) + ";\n"
open(D+"/data.js","w",encoding="utf-8").write(js)
print("topics:",len(out),"images:",sum(len(t['files']) for t in out))
