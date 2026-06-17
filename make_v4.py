import pathlib, re
src = pathlib.Path(r"C:\duronex-img\cafe24_index3.html").read_text(encoding="utf-8")

# 1) 크로스페이드 transition 부드럽게 (ease-in-out + 시간 조정)
src = src.replace(
  ".hero__img{position:absolute;inset:0;width:100%;height:100%;background-size:cover;background-position:center;opacity:0;transition:opacity .9s;will-change:opacity}",
  ".hero__img{position:absolute;inset:0;width:100%;height:100%;background-size:cover;background-position:center;opacity:0;transition:opacity 1.2s cubic-bezier(.4,0,.2,1);will-change:opacity;backface-visibility:hidden}"
)

# 2) 전환 주기 살짝 늘려서 로딩 여유 (4200 -> 5000)
src = src.replace("setInterval(tick,4200)", "setInterval(tick,5000)")

# 3) 모든 히어로 이미지 미리 로딩 (preload) - hero 직전에 삽입
preload = """<script>
(function(){
 var urls=["hero-1","hero-2","hero-3","hero-4","hero-5","hero-6"];
 urls.forEach(function(n){var i=new Image();i.src="https://cdn.jsdelivr.net/gh/jaywayshot/duronex-img@main/img/"+n+".jpeg";});
})();
</script>
"""
src = src.replace('<section class="hero"', preload + '<section class="hero"', 1)

pathlib.Path(r"C:\duronex-img\cafe24_index4.html").write_text(src, encoding="utf-8")
print("생성: cafe24_index4.html /", len(src), "자")
print("부드러운 transition:", "cubic-bezier(.4,0,.2,1)" in src)
print("preload 삽입:", "new Image()" in src)
print("주기 5초:", "tick,5000" in src)
