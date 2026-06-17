import pathlib, re
src = pathlib.Path(r"C:\duronex-img\cafe24_index7.html").read_text(encoding="utf-8")

# 1) 과한 GPU 레이어 정리 (translate3d/backface 남발이 PC서 역효과)
src = src.replace(".hero__img,.ch__img,.cl,.buy__media,.look__item{transform:translate3d(0,0,0);-webkit-backface-visibility:hidden;backface-visibility:hidden}", "")
src = src.replace(".ch__img,.cl,.hero__img,.look__item,.buy__media{transform:translateZ(0);content-visibility:auto}", ".ch__img,.cl,.hero__img,.look__item,.buy__media{content-visibility:auto}")
src = src.replace(";backface-visibility:hidden", "")

# 2) 룩북 무한루프: 스크롤 성능 위해 GPU 단일 레이어만
src = src.replace(
  ".look__track{display:flex;gap:14px;width:max-content;animation:lookflow 48s linear infinite;padding-block:4px}",
  ".look__track{display:flex;gap:14px;width:max-content;animation:lookflow 60s linear infinite;padding-block:4px;transform:translateZ(0);will-change:transform}"
)

# 3) 배경이미지 리페인트 줄이기: 큰 이미지 섹션만 레이어 승격
perf = """
/* === PC scroll perf === */
.hero,.ch,.cl,.buy__media{transform:translateZ(0)}
.hero__img{image-rendering:auto}
@media(min-width:1025px){
 .look__track{animation-duration:70s}
}
"""
src = src.replace("</style>", perf + "\n</style>")

pathlib.Path(r"C:\duronex-img\cafe24_index8.html").write_text(src, encoding="utf-8")
print("생성: cafe24_index8.html /", len(src), "자")
print("PC perf:", "PC scroll perf" in src)
print("backface 정리됨:", src.count("backface-visibility")<=1)
