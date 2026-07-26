# -*- coding: utf-8 -*-
"""把 IG貼圖 各主題「週五：隨手語錄」的圖壓縮輸出到 images/<slug>/N.jpg，並產生 tools/topics.json"""
import os, re, json, sys, glob
from PIL import Image

# DST = 這個 repo 的根目錄（tools/ 的上一層）
DST = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SRC = IG貼圖 資料夾；可用第一個參數指定，否則自動找已連接的資料夾
SRC = sys.argv[1] if len(sys.argv) > 1 else next(iter(glob.glob("/sessions/*/mnt/IG貼圖")), "")
MAX, QUALITY = 1080, 82

SLUG = {
 "01":"goji","02":"chrysanthemum","03":"jujube","04":"hawthorn","05":"gathering",
 "06":"winter-tonic","07":"ginger","08":"longan","09":"astragalus",
 "10":"angelica","11":"tangerine","12":"lotusseed","13":"newyear","14":"spring-festival",
 "15":"rose","16":"coix","17":"mint","18":"cassia","19":"honeysuckle","20":"spring-liver",
 "21":"poria","22":"lotusleaf","23":"lily","24":"guyu","25":"loquat","26":"mugwort",
 "27":"mungbean","28":"mume","29":"ophiopogon","30":"apricot","31":"dragonboat","32":"sanfu",
 "33":"coptis","34":"yam","35":"paozhi","36":"dashu","37":"euryale","38":"fritillaria",
}
CN = {"一":1,"二":2,"三":3,"四":4,"五":5}

def order(name):
    s = re.sub(r"^(星期|週|周)", "", name.strip())
    m = re.match(r"(\d+)", s)
    if m: return int(m.group(1))
    if s and s[0] in CN: return CN[s[0]]
    return 99

def topic_num(name):
    m = re.match(r"\s*(\d+)", name)
    if not m: return None, None
    return m.group(1).zfill(2), re.sub(r"^\s*\d+\s*[.\-、]?\s*", "", name).strip()

out = []
for year in ("2025", "2026"):
    ydir = os.path.join(SRC, year)
    if not os.path.isdir(ydir): continue
    for topic in sorted(os.listdir(ydir)):
        tdir = os.path.join(ydir, topic)
        if not os.path.isdir(tdir): continue
        num, label = topic_num(topic)
        if not num: continue
        subs = [d for d in os.listdir(tdir) if os.path.isdir(os.path.join(tdir, d))]
        fifth = next((d for d in subs if order(d) == 5), None)
        if fifth is None:
            print("SKIP(no-5th) %s %s :: %s" % (year, topic, subs), flush=True); continue
        sdir = os.path.join(tdir, fifth)
        imgs = sorted([f for f in os.listdir(sdir) if f.lower().endswith((".jpg",".jpeg",".png",".webp"))],
                      key=lambda x: (int(re.match(r"\d+", x).group()) if re.match(r"\d+", x) else 99, x))
        if not imgs:
            print("SKIP(empty) %s %s" % (year, topic), flush=True); continue
        slug = SLUG.get(num, "t" + num)
        odir = os.path.join(DST, "images", slug)
        os.makedirs(odir, exist_ok=True)
        files = []
        for i, f in enumerate(imgs, 1):
            op = os.path.join(odir, "%d.jpg" % i)
            sp = os.path.join(sdir, f)
            if os.path.exists(op) and os.path.getmtime(op) >= os.path.getmtime(sp):
                files.append("%d.jpg" % i); continue
            for attempt in range(3):
                try:
                    im = Image.open(sp).convert("RGB")
                    im.thumbnail((MAX, MAX), Image.LANCZOS)
                    im.save(op, "JPEG", quality=QUALITY, optimize=True, progressive=True)
                    files.append("%d.jpg" % i); break
                except Exception as e:
                    if attempt == 2: print("ERR %s %s %s %s" % (year, topic, f, e), flush=True)
        out.append({"num": int(num), "year": int(year), "slug": slug, "name": label,
                    "src": fifth, "files": files})
        print("OK %s %s [%s] -> %s (%d)" % (year, topic, fifth, slug, len(files)), flush=True)

with open(os.path.join(DST, "tools", "topics.json"), "w", encoding="utf-8") as fp:
    json.dump(out, fp, ensure_ascii=False, indent=2)
print("DONE %d topics" % len(out), flush=True)
