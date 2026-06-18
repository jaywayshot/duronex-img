import pathlib
from PIL import Image, ImageDraw, ImageFont

out = pathlib.Path(r"C:\duronex-img\img")
out.mkdir(exist_ok=True)
BLUE=(43,79,255); WHITE=(255,255,255)

def font(sz):
    for p in [r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\Arial.ttf"]:
        try: return ImageFont.truetype(p, sz)
        except: pass
    return ImageFont.load_default()

def make(size):
    img=Image.new("RGBA",(size,size),(0,0,0,0))
    d=ImageDraw.Draw(img)
    r=int(size*0.18)
    d.rounded_rectangle([0,0,size-1,size-1], radius=r, fill=BLUE)
    f=font(int(size*0.66))
    d.text((size/2, size/2-size*0.04), "D", font=f, fill=WHITE, anchor="mm")
    return img

# 마스터(512) + 각 사이즈
master=make(512)
master.save(out/"favicon-512.png")
make(180).save(out/"apple-touch-icon.png")
make(32).save(out/"favicon-32.png")
make(16).save(out/"favicon-16.png")
# .ico 멀티사이즈
master.save(out/"favicon.ico", sizes=[(16,16),(32,32),(48,48)])

print("생성 완료:")
for f in ["favicon.ico","favicon-512.png","apple-touch-icon.png","favicon-32.png","favicon-16.png"]:
    p=out/f
    print(" ", f, "-", p.stat().st_size//100/10, "KB" if p.exists() else "실패")
