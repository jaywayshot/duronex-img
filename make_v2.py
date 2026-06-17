import pathlib, re

src = pathlib.Path(r"C:\duronex-img\cafe24_index.html").read_text(encoding="utf-8")

# ===== 1) 모바일 스크롤 출렁임: 100svh -> 100dvh =====
src = src.replace(
  ".hero{position:relative;height:100svh;min-height:560px;overflow:hidden;background:var(--bg2)}",
  ".hero{position:relative;height:100vh;height:100dvh;min-height:560px;max-height:920px;overflow:hidden;background:var(--bg2)}"
)

# ===== 2) 헤더 CSS 강화 (카페24 기본헤더 숨기고 우리 헤더만) =====
# 우리 .hd 헤더에 카페24 기본 #header 숨김 + 모바일 대응 추가
extra_css = """
/* === DURONEX header override (카페24 기본 헤더 숨김) === */
#header, .xans-layout-statelogin, hr.layout, #skipNavigation{display:none!important}
.hd{position:fixed;top:0;left:0;right:0;z-index:1000;mix-blend-mode:normal;background:linear-gradient(180deg,rgba(0,0,0,.55),transparent)}
.hd__in{display:flex;align-items:center;justify-content:space-between;padding:18px var(--gut)}
.hd__logo{font-weight:800;letter-spacing:-.02em;font-size:1.6rem;color:#fff}
.hd__nav{display:flex;gap:26px;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;align-items:center}
.hd__util{display:flex;gap:16px;font-size:.7rem;font-weight:700;letter-spacing:.08em;color:#fff;text-transform:uppercase}
@media(max-width:760px){.hd__logo{font-size:1.3rem}.hd__nav{display:none}.hd__util{gap:12px;font-size:.66rem}}
"""
src = src.replace("</style>", extra_css + "\n</style>")

# ===== 3) 우리 헤더에 로그인/장바구니(카페24 기능) 추가 =====
old_header = '''<header class="hd"><div class="hd__in">
 <a class="hd__logo" href="#top">DURONEX</a>
 <nav class="hd__nav"><a href="#buy">SHOP</a><a href="#sizes">SIZE</a><a href="#chapters">FEATURES</a><a href="#look">LOOKBOOK</a></nav>
</div></header>'''
# 빌드본 헤더가 위와 다를 수 있으니 정규식으로도 시도
new_header = '''<header class="hd"><div class="hd__in">
 <a class="hd__logo" href="/index.html">DURONEX</a>
 <nav class="hd__nav"><a href="#buy">SHOP</a><a href="#sizes">SIZE</a><a href="#chapters">FEATURES</a><a href="#look">LOOKBOOK</a></nav>
 <div class="hd__util"><a href="/member/login.html">LOGIN</a><a href="/order/orderform.html">CART</a><a href="/myshop/">MY</a></div>
</div></header>'''
if old_header in src:
    src = src.replace(old_header, new_header)
else:
    src = re.sub(r'<header class="hd">.*?</header>', new_header, src, flags=re.S)

pathlib.Path(r"C:\duronex-img\cafe24_index2.html").write_text(src, encoding="utf-8")
print("생성: cafe24_index2.html /", len(src), "자")
print("dvh 적용:", "100dvh" in src)
print("헤더 util 추가:", "hd__util" in src)
print("기본헤더 숨김:", "#header, .xans" in src)
