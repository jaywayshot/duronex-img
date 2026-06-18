import pathlib
base = pathlib.Path(r"C:\siteforge")
html = (base/"build/duronex/index.html").read_text(encoding="utf-8")
css  = (base/"templates/template-06-flash/assets/css/style.css").read_text(encoding="utf-8")
js   = (base/"templates/template-06-flash/assets/js/main.js").read_text(encoding="utf-8")
CDN = "https://cdn.jsdelivr.net/gh/jaywayshot/duronex-img@main/img"
html = html.replace("assets/img/", CDN + "/")
html = html.replace('<link rel="stylesheet" href="assets/css/style.css">', "<style>\n"+css+"\n</style>")
html = html.replace('<script src="assets/js/main.js"></script>', "<script>\n"+js+"\n</script>")
pathlib.Path(r"C:\duronex-img\index.html").write_text(html, encoding="utf-8")
print("OK", len(html), html.count(CDN))
