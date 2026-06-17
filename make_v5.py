import pathlib, re
src = pathlib.Path(r"C:\duronex-img\cafe24_index4.html").read_text(encoding="utf-8")

# 1) will-change 남발 제거 (GPU 메모리 과부하 원인)
src = src.replace(";will-change:opacity;backface-visibility:hidden", ";backface-visibility:hidden")
src = src.replace("animation:lookflow 48s linear infinite;padding-block:4px;will-change:transform", "animation:lookflow 48s linear infinite;padding-block:4px")

# 2) 챕터/클로징 무거운 배경이미지에 GPU 레이어 + 스크롤 최적화
opt_css = """
/* === scroll perf === */
.ch__img,.cl,.hero__img,.look__item,.buy__media{transform:translateZ(0);content-visibility:auto}
.look__track{will-change:transform}
@media(max-width:760px){
 .look__track{animation-duration:60s}
 .hero__img{background-attachment:scroll}
}
"""
src = src.replace("</style>", opt_css + "\n</style>")

pathlib.Path(r"C:\duronex-img\cafe24_index5.html").write_text(src, encoding="utf-8")
print("생성: cafe24_index5.html /", len(src), "자")
print("content-visibility:", "content-visibility:auto" in src)
print("translateZ:", "translateZ(0)" in src)
