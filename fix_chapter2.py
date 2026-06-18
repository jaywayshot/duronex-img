import pathlib, re
p=pathlib.Path(r"C:\duronex-img\cafe24_index8.html")
s=p.read_text(encoding="utf-8")

# 1) 챕터 박스: 와이드 화면서도 비율 유지(aspect-ratio) -> 납작해지지 않음
s=re.sub(
 r"\.ch__img\{width:100%;height:[^}]*\}",
 ".ch__img{width:100%;aspect-ratio:16/10;max-height:760px;min-height:420px;background-size:cover;background-position:center 25%}",
 s
)

# 2) 챕터별 얼굴 라인 위로 (목 안 잘리게)
per="""
/* 챕터별 포커스 (얼굴 살림) */
#chapters .ch:nth-of-type(1) .ch__img{background-position:center 30%}
#chapters .ch:nth-of-type(2) .ch__img{background-position:center 12%}
#chapters .ch:nth-of-type(3) .ch__img{background-position:center 30%}
@media(min-width:1400px){
 #chapters .ch:nth-of-type(2) .ch__img{background-position:center 8%}
}
"""
# 기존 per_chapter 블록 있으면 교체, 없으면 추가
if "챕터별 포커스" in s or "챕터별 이미지 포커스" in s:
    s=re.sub(r"\n/\* 챕터별[^*]*\*/.*?(?=\n</style>)", "", s, flags=re.S)
s=s.replace("</style>", per+"\n</style>")

p.write_text(s,encoding="utf-8")
print("aspect-ratio 적용:", "aspect-ratio:16/10" in s)
print("챕터2 위로(12%):", "nth-of-type(2) .ch__img{background-position:center 12%}" in s)
