# -*- coding: utf-8 -*-
"""4.1水循环·视频4线六字段帧验采集（§十队7①实采首件·B站≥30s错峰·承§十二-1）
方法承普查先例：curl浏览器头+随机buvid3 view API；412冷却重试；单队间隔≥30s
输出：素材实采件_4.1_视频六字段_1024晚.json（逐BV原始记录+时点留痕）
"""
import subprocess, json, random, time, sys

BVS = [
    ("BV1iD4y1s7qX",  "星云地理·4.1直配"),
    ("BV1yWzbYtE5X",  "纯纯子·4.1直配"),
    ("BV1Zd4y1F7q6",  "一地er·4.1通用头部61.7万"),
    ("BV14wBqYDEie",  "太阳的地理课堂·4.1直配"),
]
OUT = "/home/z/my-project/agents/6a9cf51c5d7ce412885e5265/fetch1022/repo/产出_队7/素材实采件_4.1_视频六字段_1024晚.json"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def fetch_view(bvid):
    buvid = "AB" + "".join(random.choices("0123456789ABCDEF", k=30)) + "infoc"
    url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    cmd = ["curl", "-sS", "-m", "20", "--compressed", url,
           "-H", f"User-Agent: {UA}",
           "-H", "Referer: https://www.bilibili.com/",
           "-H", f"Cookie: buvid3={buvid}; b_nut=1730000000",
           "-H", "Accept: application/json"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        data = json.loads(r.stdout)
    except Exception as e:
        return {"bvid": bvid, "ok": 0, "err": f"exc:{type(e).__name__}"}
    code = data.get("code")
    if code == 412:
        return {"bvid": bvid, "ok": 0, "err": "412风控"}
    if code != 0:
        return {"bvid": bvid, "ok": 0, "err": f"code={code} msg={data.get('message','')[:60]}"}
    d = data["data"]
    pages = [{"page": p.get("page"), "cid": p.get("cid"), "part": p.get("part", "")[:80]}
             for p in (d.get("pages") or [])]
    return {
        "bvid": bvid, "ok": 1,
        "aid": d.get("aid"),
        "title": d.get("title", "")[:120],
        "owner": (d.get("owner") or {}).get("name", ""),
        "duration": d.get("duration"),
        "view": (d.get("stat") or {}).get("view"),
        "danmaku": (d.get("stat") or {}).get("danmaku"),
        "pubdate": d.get("pubdate"),
        "bvid_iso": d.get("bvid"),
        "pages_n": len(pages),
        "pages": pages[:6],
    }

records = []
for i, (bvid, note) in enumerate(BVS):
    rec = None
    for attempt in range(3):
        rec = fetch_view(bvid)
        if rec.get("ok") == 1 or (rec.get("err") and "412" not in rec.get("err", "")):
            break
        time.sleep(45)  # 412冷却
    rec["note_line"] = note
    rec["fetched_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    rec["attempt"] = attempt + 1
    records.append(rec)
    print(json.dumps(rec, ensure_ascii=False)[:200], flush=True)
    if i < len(BVS) - 1:
        time.sleep(32)  # ≥30s错峰（§十二-1①）

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=1)
print("DONE", len(records), flush=True)
