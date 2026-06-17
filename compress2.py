import pathlib
from PIL import Image

src_dir = pathlib.Path(r"C:\duronex-img\img_backup")  # 무손실 원본에서
out_dir = pathlib.Path(r"C:\duronex-img\img")          # 웹 폴더에 출력
files = sorted(src_dir.glob("*.jpeg")) + sorted(src_dir.glob("*.jpg"))
print(f"원본 소스: {src_dir.name} / 대상 {len(files)}장\n")
tb = ta = 0
for f in files:
    out = out_dir / f.name
    before = f.stat().st_size; tb += before
    img = Image.open(f)
    if img.mode != "RGB": img = img.convert("RGB")
    if img.width > 1600:
        r = 1600 / img.width; img = img.resize((1600, int(img.height * r)), Image.LANCZOS)
    img.save(out, "JPEG", quality=65, optimize=True, progressive=True)
    after = out.stat().st_size; ta += after
    print(f"{f.name}: {before//1024}KB(원본) -> {after//1024}KB")
print(f"\n총합(원본 대비): {tb//1024//1024}MB -> {ta//1024//1024}MB ({100-int(ta/tb*100)}% 절감)")
