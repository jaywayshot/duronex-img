import pathlib, re
src = pathlib.Path(r"C:\duronex-img\cafe24_index2.html").read_text(encoding="utf-8")

# ===== 1) 히어로 출렁임 완전 제거 =====
# dvh도 일부 브라우저서 출렁임 -> 고정픽셀 비율 + JS 없이 안정화
src = re.sub(
  r"\.hero\{position:relative;height:[^}]*\}",
  ".hero{position:relative;height:88vh;height:min(88dvh,860px);min-height:520px;overflow:hidden;background:var(--bg2)}",
  src
)
# 히어로 이미지: 스크롤 시 리사이즈 안 되게 고정
src = src.replace(
  ".hero__img{position:absolute;inset:0;background-size:cover;background-position:center;opacity:0;transition:opacity .9s}",
  ".hero__img{position:absolute;inset:0;width:100%;height:100%;background-size:cover;background-position:center;opacity:0;transition:opacity .9s;will-change:opacity}"
)

# ===== 2) 모바일 히어로/타이포 정리 =====
mobile_css = """
/* === mobile fix === */
@media(max-width:760px){
 .hero{height:78vh;height:min(78dvh,680px);min-height:480px}
 .hero__big h1{font-size:clamp(3rem,17vw,5.5rem)}
 .hero__tag{top:64px}
 .hd__in{padding:12px 18px}
 .hd__logo{font-size:1.25rem}
 .hd{background:linear-gradient(180deg,rgba(0,0,0,.6),transparent)}
}
@media(max-width:460px){
 .hero__row .btn{width:100%;text-align:center}
}
"""
src = src.replace("</style>", mobile_css + "\n</style>")

pathlib.Path(r"C:\duronex-img\cafe24_index3.html").write_text(src, encoding="utf-8")
print("생성: cafe24_index3.html /", len(src), "자")
print("히어로 min(dvh):", "min(88dvh" in src)
print("모바일fix:", "mobile fix" in src)
print("헤더숨김 유지:", "#header, .xans" in src)
print("dvh 유지:", "dvh" in src)
