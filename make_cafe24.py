import pathlib, re
src = pathlib.Path(r"C:\duronex-img\index.html").read_text(encoding="utf-8")

# <main>...</main> 내부만 추출 (헤더/푸터는 카페24 레이아웃이 담당)
m = re.search(r"<main>(.*)</main>", src, re.S)
body = m.group(1).strip() if m else src

# <style>...</style> 와 <script>...</script> 도 그대로 살림 (인라인돼 있음)
style = re.search(r"<style>.*?</style>", src, re.S)
script = re.search(r"<script>.*?</script>", src, re.S)
style = style.group(0) if style else ""
script = script.group(0) if script else ""

out = []
out.append("<!--@layout(/layout/basic/main.html)-->")
out.append("")
out.append("<!-- ===== DURONEX custom skin ===== -->")
out.append(style)
out.append("")
out.append(body)
out.append("")
out.append(script)
out.append("")
out.append("<!--@define(cmc_log)-->")
result = "\n".join(out)

pathlib.Path(r"C:\duronex-img\cafe24_index.html").write_text(result, encoding="utf-8")
print("생성: cafe24_index.html /", len(result), "자")
print("@layout:", "<!--@layout" in result)
print("@define:", "@define(cmc_log)" in result)
print("CDN참조:", result.count("cdn.jsdelivr.net"))
