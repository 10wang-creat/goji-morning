# -*- coding: utf-8 -*-
"""替 images/ 與 gold/ 的每張圖產生 400px 小縮圖到 thumbs/（圖庫用，點進去才載大圖）"""
import os
from PIL import Image
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
n = 0
for base in ("images", "gold"):
    for root, _, files in os.walk(os.path.join(D, base)):
        for f in files:
            if not f.lower().endswith(".jpg"): continue
            src = os.path.join(root, f)
            dst = os.path.join(D, "thumbs", os.path.relpath(src, D))
            if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im = Image.open(src).convert("RGB"); im.thumbnail((400, 400), Image.LANCZOS)
            im.save(dst, "JPEG", quality=72, optimize=True, progressive=True); n += 1
print("新增縮圖 %d 張" % n)
