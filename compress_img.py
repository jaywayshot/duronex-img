import pathlib
from PIL import Image

src_dir = pathlib.Path(r"C:\duronex-img\img")
out_dir = pathlib.Path(r"C:\duronex-img\img")  # 같은 폴더에 덮어쓰기

files = sorted(src_dir.glob("*.jpeg")) + sorted(src_dir.glob("*.jpg"))
print(f"대상: {len(files)}장\n")

total_before = 0
total_after = 0
for f in files:
    before = f.stat().st_size
    total_before += before
    img = Image.open(f)
    # RGB 변환 (CMYK/RGBA 대비)
    if img.mode != "RGB":
        img = img.convert("RGB")
    # 가로 최대 1920px로 리사이즈 (그 이상은 웹에서 불필요)
    if img.width > 1920:
        ratio = 1920 / img.width
        img = img.resize((1920, int(img.height * ratio)), Image.LANCZOS)
    # 품질 80으로 저장 (육안상 거의 동일, 용량 급감)
    img.save(f, "JPEG", quality=80, optimize=True, progressive=True)
    after = f.stat().st_size
    total_after += after
    print(f"{f.name}: {before//1024}KB -> {after//1024}KB")

print(f"\n총합: {total_before//1024//1024}MB -> {total_after//1024//1024}MB")
print(f"절감률: {100-int(total_after/total_before*100)}%")
