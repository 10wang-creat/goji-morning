# -*- coding: utf-8 -*-
"""一鍵更新：抓新語錄 -> 抓新金句 -> 產生縮圖 -> 重建 data.js"""
import os, subprocess, sys
T = os.path.dirname(os.path.abspath(__file__))
for s in ("build.py", "build_gold.py", "build_thumbs.py", "gen_data.py"):
    print("== " + s, flush=True)
    r = subprocess.run([sys.executable, os.path.join(T, s)] + sys.argv[1:])
    if r.returncode: sys.exit(r.returncode)
