import pathlib
p=pathlib.Path(r"C:\duronex-img\cafe24_index8.html")
s=p.read_text(encoding="utf-8")

# 챕터 이미지: center -> center 30% (얼굴 위쪽 살림)
s=s.replace(
 ".ch__img{width:100%;height:clamp(380px,68vw,640px);background-size:cover;background-position:center}",
 ".ch__img{width:100%;height:clamp(380px,68vw,640px);background-size:cover;background-position:center 30%}"
)
# 클로징도 같이
s=s.replace(
 ".cl{position:relative;min-height:560px;display:flex;align-items:flex-end;background:var(--bg2) center/cover;overflow:hidden}",
 ".cl{position:relative;min-height:560px;display:flex;align-items:flex-end;background:var(--bg2) center 25%/cover;overflow:hidden}"
)
p.write_text(s,encoding="utf-8")
print("변경 완료 / center 30% 적용:", "center 30%" in s)
