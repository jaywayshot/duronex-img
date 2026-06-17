import urllib.request
files=["hero-1","hero-2","hero-3","hero-4","hero-5","hero-6","ch-01.","ch-02","ch-03","look-01","look-02","look-03","look-04","look-05","look-06","buy-black","buy-silver","close"]
for n in files:
    url=f"https://purge.jsdelivr.net/gh/jaywayshot/duronex-img@main/img/{n}.jpeg"
    try:
        urllib.request.urlopen(url,timeout=20); print("purged:",n)
    except Exception as e:
        print("fail:",n,e)
