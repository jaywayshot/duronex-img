import pathlib, re
p=pathlib.Path(r"C:\duronex-img\cafe24_index8.html")
s=p.read_text(encoding="utf-8")

# 기존 split 블록 제거 (실제 주석 문자열에 맞춤 -> 중복 방지)
s=re.sub(r"\n/\* CHAPTERS split - PC only.*?\}\n\}\n", "\n", s, flags=re.S)

# PC에서만 split 적용 (모바일은 기존 풀와이드 화보 유지)
pc_split="""
/* CHAPTERS split - PC only (모바일은 기존 풀와이드 유지) */
@media(min-width:761px){
 .ch{display:grid;grid-template-columns:1fr 1fr;background:var(--bg2)}
 .ch__img{position:relative;width:100%;height:100%;min-height:clamp(440px,42vw,640px);background-size:cover}
 .ch__cap{position:static;display:flex;align-items:center;padding:clamp(36px,5vw,72px);background:var(--bg2);background-image:none}
 .ch__meta h3{color:#fff}
 .ch__meta p{color:rgba(255,255,255,.78)}
 .ch:nth-of-type(even) .ch__img{order:2}
 #chapters .ch:nth-of-type(1) .ch__img{background-position:center 30%}
 #chapters .ch:nth-of-type(2) .ch__img{background-position:center 16%}
 #chapters .ch:nth-of-type(3) .ch__img{background-position:center 28%}
}
"""
s=s.replace("</style>", pc_split+"\n</style>")

p.write_text(s,encoding="utf-8")
print("PC split 적용:", "CHAPTERS split - PC only" in s)
print("블록 개수:", s.count("CHAPTERS split - PC only"))
