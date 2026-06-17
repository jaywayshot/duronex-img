import pathlib
for f in ["cafe24_index.html","cafe24_index2.html"]:
    p = pathlib.Path(r"C:\duronex-img")/f
    if p.exists():
        s = p.read_text(encoding="utf-8")
        print(f"=== {f} ({len(s)}자) ===")
        print("  100dvh:", "100dvh" in s)
        print("  hd__util:", "hd__util" in s)
        print("  기본헤더숨김:", "#header, .xans" in s)
