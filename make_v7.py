import pathlib, re
src = pathlib.Path(r"C:\duronex-img\cafe24_index6.html").read_text(encoding="utf-8")

# 모든 섹션의 vh 의존 제거 -> 픽셀 고정 (주소창 변화 무시)
reps = {
 # 챕터 이미지
 ".ch__img{width:100%;height:clamp(380px,76vh,820px)":".ch__img{width:100%;height:clamp(380px,68vw,640px)",
 # 클로징
 ".cl{position:relative;min-height:88vh":".cl{position:relative;min-height:560px",
 # 구매 미디어
 ".buy__media{background:#ddd center/cover;min-height:84vh":".buy__media{background:#ddd center/cover;min-height:600px",
 # 룩북 아이템(이미 aspect-ratio라 ok), 매니페스토 패딩 vh 제거
 "padding:clamp(64px,12vh,150px) 0":"padding:clamp(64px,9vw,130px) 0",
 "padding:clamp(56px,10vh,140px) 0":"padding:clamp(56px,8vw,120px) 0",
 "padding:clamp(54px,9vh,110px) 0":"padding:clamp(54px,7vw,100px) 0",
 "bottom:clamp(28px,6vh,68px)":"bottom:clamp(28px,5vw,60px)",
 "padding-bottom:clamp(36px,7vh,80px)":"padding-bottom:clamp(36px,6vw,72px)",
 "padding:clamp(44px,7vh,84px) 0 34px":"padding:clamp(44px,6vw,80px) 0 34px",
}
cnt=0
for a,b in reps.items():
    if a in src: src=src.replace(a,b); cnt+=1
    else: print("못찾음:",a[:40])

# 모바일 버전들도
src=src.replace(".buy__media{min-height:62vh",".buy__media{min-height:440px")

pathlib.Path(r"C:\duronex-img\cafe24_index7.html").write_text(src, encoding="utf-8")
print(f"\n생성: cafe24_index7.html / {len(src)}자 / 교체 {cnt}건")
print("남은 vh 개수:", src.count("vh"))
