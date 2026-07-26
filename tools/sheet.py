import os
from PIL import Image, ImageDraw
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items=[]
for slug in sorted(os.listdir(D+"/images")):
    p=os.path.join(D,"images",slug)
    if not os.path.isdir(p): continue
    for f in sorted(os.listdir(p)):
        if f.endswith(".jpg"): items.append((slug,f,os.path.join(p,f)))
CELL,COLS,ROWS=300,6,6
PER=COLS*ROWS
os.makedirs(D+"/tools/sheets",exist_ok=True)
for si in range(0,len(items),PER):
    chunk=items[si:si+PER]
    sh=Image.new("RGB",(COLS*CELL,((len(chunk)-1)//COLS+1)*(CELL+22)),"#333333")
    dr=ImageDraw.Draw(sh)
    for i,(slug,f,path) in enumerate(chunk):
        im=Image.open(path); im.thumbnail((CELL-4,CELL-4))
        x=(i%COLS)*CELL; y=(i//COLS)*(CELL+22)
        dr.text((x+4,y+5),"%s/%s"%(slug,f[0]),fill="#ffffff")
        sh.paste(im,(x+2,y+22))
    out=D+"/tools/sheets/sheet%d.jpg"%(si//PER+1)
    sh.save(out,"JPEG",quality=88)
    print(out, len(chunk))
print("total",len(items))
