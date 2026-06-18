import pathlib
p=pathlib.Path(r"C:\duronex-img\cafe24_index8.html")
s=p.read_text(encoding="utf-8")

# 1) 챕터 박스 높이 키움 (와이드 화면서 덜 납작 -> 덜 잘림)
s=s.replace(
 ".ch__img{width:100%;height:clamp(380px,68vw,640px);background-size:cover;background-position:center 30%}",
 ".ch__img{width:100%;height:clamp(420px,60vw,820px);background-size:cover;background-position:center 28%}"
)

# 2) 챕터별 개별 자르기 기준 (1번=위쪽 얼굴, 2번=가운데, 3번=가운데)
per_chapter="""
/* 챕터별 이미지 포커스 */
#chapters .ch:nth-of-type(1) .ch__img{background-position:center 18%}
#chapters .ch:nth-of-type(2) .ch__img{background-position:center 22%}
#chapters .ch:nth-of-type(3) .ch__img{background-position:center 35%}
"""
s=s.replace("</style>", per_chapter+"\n</style>")

p.write_text(s,encoding="utf-8")
print("적용 완료")
print("높이 키움:", "60vw,820px" in s)
print("챕터별 포커스:", "nth-of-type(1)" in s)
