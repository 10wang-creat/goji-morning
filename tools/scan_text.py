import os, json
from PIL import Image, ImageStat
D="/sessions/rcw-01utmn9wggptsjy98hwnpf28/mnt/goji-morning/images"
res=[]
for slug in sorted(os.listdir(D)):
    p=os.path.join(D,slug)
    if not os.path.isdir(p): continue
    for f in sorted(os.listdir(p)):
        if not f.endswith(".jpg"): continue
        im=Image.open(os.path.join(p,f)).convert("L")
        w,h=im.size
        top=im.crop((0,0,w,int(h*0.55)))
        px=top.getdata(); n=len(px)
        dark=sum(1 for v in px if v<120)/n
        res.append((round(dark*100,3), slug, f))
res.sort()
for r in res[:30]: print(r)
print("...")
print("total", len(res))
