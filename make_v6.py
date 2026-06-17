import pathlib, re
src = pathlib.Path(r"C:\duronex-img\cafe24_index5.html").read_text(encoding="utf-8")

# 1) 히어로 높이를 vh/dvh 대신 JS 고정 픽셀로 (출렁임 원천 차단)
src = re.sub(
  r"\.hero\{position:relative;height:[^}]*\}",
  ".hero{position:relative;height:88vh;min-height:520px;max-height:860px;overflow:hidden;background:var(--bg2)}",
  src
)
src = re.sub(
  r"@media\(max-width:760px\)\{\s*\.hero\{height:[^}]*\}",
  "@media(max-width:760px){.hero{max-height:680px}",
  src
)

# 2) JS: 로딩 시 히어로 높이를 픽셀로 고정 (주소창 변화 무시)
fix_js = """<script>
(function(){
 function lockHero(){
  var h=document.querySelector('.hero');
  if(!h)return;
  var vh=window.innerHeight;
  var target=Math.min(Math.round(vh*(window.innerWidth<=760?0.82:0.88)), window.innerWidth<=760?680:860);
  if(target<480)target=480;
  h.style.height=target+'px';
 }
 lockHero();
 window.addEventListener('orientationchange',function(){setTimeout(lockHero,300);});
 var rw;window.addEventListener('resize',function(){
  if(Math.abs(window.innerHeight-(window._lastIH||0))<120){return;}
  window._lastIH=window.innerHeight;clearTimeout(rw);rw=setTimeout(lockHero,200);
 });
 window._lastIH=window.innerHeight;
})();
</script>
"""
src = src.replace("</body>", fix_js + "</body>") if "</body>" in src else src.replace("<!--@define(cmc_log)-->", fix_js + "<!--@define(cmc_log)-->")

pathlib.Path(r"C:\duronex-img\cafe24_index6.html").write_text(src, encoding="utf-8")
print("생성: cafe24_index6.html /", len(src), "자")
print("JS 높이고정:", "lockHero" in src)
print("resize 가드:", "_lastIH" in src)
