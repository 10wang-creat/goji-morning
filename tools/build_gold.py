# -*- coding: utf-8 -*-
"""金句海報：W35 起在「第4個資料夾的第3張」。只處理 gold/ 裡還沒有的新主題（編號 >= 39）。
不想收的編號寫進 tools/gold_exclude.txt（每行一個數字）。"""
import os, re, sys, glob, importlib.util
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); DST = os.path.dirname(HERE)
SRC = sys.argv[1] if len(sys.argv) > 1 else next(iter(glob.glob(os.path.expanduser("~/mnt/IG貼圖")) + glob.glob("/sessions/*/mnt/IG貼圖")), "")
spec = importlib.util.spec_from_file_location("b", os.path.join(HERE, "slugs.py")); b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
ex = set()
p = os.path.join(HERE, "gold_exclude.txt")
if os.path.exists(p):
    ex = {l.strip() for l in open(p, encoding="utf-8") if l.strip() and not l.startswith("#")}
os.makedirs(os.path.join(DST, "gold"), exist_ok=True)
for topic in sorted(os.listdir(os.path.join(SRC, "2026"))):
    m = re.match(r"\s*(\d+)", topic)
    if not m: continue
    num = int(m.group(1))
    if num < 39 or str(num) in ex: continue
    slug = b.SLUG.get(str(num).zfill(2))
    if not slug: print("缺 slug:", topic); continue
    out = os.path.join(DST, "gold", slug + ".jpg")
    if os.path.exists(out): continue
    tdir = os.path.join(SRC, "2026", topic)
    sub = next((d for d in os.listdir(tdir) if os.path.isdir(os.path.join(tdir, d)) and b.order(d) == 4), None)
    if not sub: print("沒有第4資料夾:", topic); continue
    imgs = sorted([f for f in os.listdir(os.path.join(tdir, sub)) if f.lower().endswith((".png", ".jpg", ".jpeg"))], key=b.fkey)
    if len(imgs) < 3: print("第4資料夾不足3張:", topic); continue
    im = Image.open(os.path.join(tdir, sub, imgs[2])).convert("RGB"); im.thumbnail((1080, 1080), Image.LANCZOS)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    print("GOLD", topic, "->", slug, flush=True)
