import pathlib
p=pathlib.Path(r"C:\duronex-img\cafe24_index8.html")
s=p.read_text(encoding="utf-8")
n=s.count("보디")
print("보디 발견:", n, "곳")
s=s.replace("보디","바디")
p.write_text(s,encoding="utf-8")
print("→ 바디로 변경 완료")
