#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B站双源视频表字幕级核验 v1（队1追加件①-3·B席执行）
流程：游客指纹自取（首页Set-Cookie+spi兜底）→ view取cid → player/v2取字幕字段 → 台账增量落盘
用法：python3 bv_verify_v1.py --test BV16R4y1H77L ｜ --range 0:20 ｜ --range 20:47
台账：bv_verify_台账_1023.json（逐行JSON）+ 进度stdout
"""
import sys, json, time, re, urllib.request, http.cookiejar, gzip, io

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
WORKDIR = "/home/z/my-project/agents/6a9cf52e26f40cafe9f060a9"
DAN = WORKDIR + "/bv_verify_台账_1023.json"
WORKSHEET = "/home/z/my-project/agents/6a9cf52e26f40cafe9f060a9/tb_ro/产出_队1/追加件-视频表字幕级核验工作单_队1_1023.md"

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def hdr():
    return {
        "User-Agent": UA,
        "Referer": "https://www.bilibili.com/",
        "Origin": "https://www.bilibili.com",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

def get(url, timeout=15):
    req = urllib.request.Request(url, headers=hdr())
    r = opener.open(req, timeout=timeout)
    data = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        data = gzip.GzipFile(fileobj=io.BytesIO(data)).read()
    return json.loads(data.decode("utf-8", "ignore"))

def bootstrap():
    """取游客指纹：首页埋点 → spi接口兜底"""
    try:
        req = urllib.request.Request("https://www.bilibili.com/", headers=hdr())
        opener.open(req, timeout=15).read(1024)
    except Exception as e:
        print("[bootstrap] homepage warn:", e)
    try:
        j = get("https://api.bilibili.com/x/frontend/finger/spi")
        b3, b4 = j.get("data", {}).get("b_3"), j.get("data", {}).get("b_4")
        if b3:
            import http.cookiejar as hc
            ck = hc.Cookie(0, "buvid3", b3, None, False, ".bilibili.com", True, True, "/", False, False, None, False, None, None, {})
            cj.set_cookie(ck)
        if b4:
            import http.cookiejar as hc
            ck = hc.Cookie(0, "buvid4", b4, None, False, ".bilibili.com", True, True, "/", False, False, None, False, None, None, {})
            cj.set_cookie(ck)
        print("[bootstrap] spi ok buvid3=", (b3 or "")[:24])
    except Exception as e:
        print("[bootstrap] spi warn:", e)
    got = [c.name for c in cj]
    print("[bootstrap] cookies:", got)

def parse_worksheet():
    """解析工作单47行BV清单 → [{jie, src, bv}]"""
    txt = open(WORKSHEET, encoding="utf-8").read()
    rows = []
    for line in txt.splitlines():
        m = re.match(r"^\|\s*([\d.]+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if not m:
            continue
        jie, c2, c3 = m.group(1), m.group(2), m.group(3)
        if "汉水" in c2 or "BV" not in c2 and "BV" not in c3:
            if "BV" not in c2 and "BV" not in c3:
                continue
        for src, cell in (("汉水", c2), ("李林", c3)):
            for bv in re.findall(r"BV[0-9A-Za-z]{10}", cell):
                rows.append({"jie": jie, "src": src, "bv": bv})
    return rows

def verify_one(bv):
    out = {"bv": bv, "code": None, "pages": None, "cid_p1": None, "subs": [], "note": "", "method": "api", "ts": time.strftime("%m-%d %H:%M:%S")}
    try:
        v = get("https://api.bilibili.com/x/web-interface/view?bvid=" + bv)
        out["code"] = v.get("code")
        if v.get("code") == 0:
            d = v["data"]
            out["pages"] = d.get("videos", 1)
            pages = d.get("pages") or []
            out["cid_p1"] = pages[0]["cid"] if pages else d.get("cid")
            out["title"] = (d.get("title") or "")[:40]
            out["owner"] = (d.get("owner") or {}).get("name", "")
        else:
            out["note"] = "view_code=" + str(v.get("code")) + " " + str(v.get("message", ""))[:30]
            return out
        time.sleep(1.2)
        p = get("https://api.bilibili.com/x/player/v2?bvid=%s&cid=%s" % (bv, out["cid_p1"]))
        out["pcode"] = p.get("code")
        if p.get("code") == 0:
            subs = (p.get("data", {}).get("subtitle") or {}).get("subtitles") or []
            out["subs"] = [{"lan": s.get("lan"), "lan_doc": s.get("lan_doc"), "ai_type": s.get("ai_type"), "ai_status": s.get("ai_status")} for s in subs]
            if not subs:
                out["note"] = "游客态subtitle空（AI字幕需登录态风险兑现，转agent-browser或标未核验）"
        else:
            out["note"] = "player_code=" + str(p.get("code")) + " " + str(p.get("message", ""))[:30]
    except urllib.error.HTTPError as e:
        out["note"] = "HTTP%d" % e.code + ("(412拦截→需换道)" if e.code == 412 else "")
    except Exception as e:
        out["note"] = "ERR:" + str(e)[:60]
    return out

def main():
    argv = sys.argv[1:]
    rows = parse_worksheet()
    print("[worksheet] 解析BV总数 =", len(rows), "（预期47）")
    targets = rows
    if "--test" in argv:
        bv = argv[argv.index("--test") + 1]
        bootstrap()
        print(json.dumps(verify_one(bv), ensure_ascii=False))
        return
    if "--range" in argv:
        a, b = argv[argv.index("--range") + 1].split(":")
        targets = rows[int(a):int(b)]
    bootstrap()
    done = {}
    import os
    if os.path.exists(DAN):
        for line in open(DAN, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    r = json.loads(line)
                    done[r["bv"]] = r
                except Exception:
                    pass
    with open(DAN, "a", encoding="utf-8") as f:
        for i, row in enumerate(targets):
            if row["bv"] in done:
                print("[skip] %s 已有记录" % row["bv"])
                continue
            r = verify_one(row["bv"])
            r.update({"jie": row["jie"], "src": row["src"]})
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
            print("[%d/%d] %s %s %s subs=%d %s" % (i + 1, len(targets), row["jie"], row["src"], row["bv"], len(r.get("subs", [])), r.get("note", "")))
            time.sleep(2.0)

if __name__ == "__main__":
    main()
