#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读者层话术预扫脚本 v1.1（队6席·承管理员段2 SOP增补令·1031夜·红黄双轨版）
用途：出品自检增补条款——主件html交付前预扫"生产调度话术"词面。
      红=判例应修（今夜三件红线判例校准）；黄=判例容忍级提示（目验复核）。
用法：python3 qc_读者层话术预扫_v1.py 成稿.html [成稿2.html ...]
退出码：0=无红（可交·黄项自行目验） 1=有红（先修后交） 2=参数错误
判例校准基准：今夜三红线件（数学4.3/化学3.3/地理5.1）必红；已并main件
（如数学4.4含"宁缺毋编"注记）不得误报红——以main在并件为阴性对照。
词表增补候裁项由队6席台账差量单承载。
"""
import io, re, sys

# ── 红词面（判例应修·学生可见正文即修） ────────────────────────
RED_LITERAL = [
    "出品席", "承办席", "工作单", "候QC", "候qc", "eol图床", "认领行",
    "禁直推", "并main", "直推main", "硬闸", "心跳", "落池", "入池",
    "让渡", "归档态", "转援", "放量批", "候补件清单", "候验池",
]
RED_PATTERN = [
    (r"sha256|sha1前8|图证sha", "技术指针"),
    (r"\bcommit\b", "commit引用"),
    (r"dui\d_\d+_1031|dui\d_batch\d*", "分支名"),
    (r"contentId|content_id", "资源ID字面"),
    (r"ts=\d{10,}", "ts时间戳字面"),
    (r"UUID[:：]|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}", "UUID字面"),
    (r"批[二三四五六七八九]?\d+·|0\d\d批", "批号引用"),
]
# ── 黄词面（判例容忍级·目验复核不放exit码） ────────────────────
AMBER_LITERAL = [
    "宁缺毋编", "在库可引", "候采", "候验", "候并", "候裁", "候终读",
    "本席", "他席", "三条差距", "随件", "四口径", "出库", "哨兵线",
]
AMBER_PATTERN = [
    (r"队\d席[AB]线|队\d席", "席名"),
    (r"并行搜索员[ABC]", "席位署名"),
]
FOOT_HINT = re.compile(r'class="[^"]*foot[^"]*"|<footer\b', re.I)
WHITELIST_HINTS = ["批处理", "批量", "一批", "这批", "每批"]

def strip_foot_regions(html):
    lines = html.split("\n")
    keep, in_foot = [], False
    for ln, raw in enumerate(lines, 1):
        if FOOT_HINT.search(raw):
            in_foot = True
        if in_foot:
            if "</footer>" in raw.lower() or "</div>" in raw:
                in_foot = False
            continue
        keep.append((ln, raw))
    return keep

def scan(path):
    html = io.open(path, encoding="utf-8", errors="replace").read()
    keep = strip_foot_regions(html)
    reds, ambers = [], []
    for ln, raw in keep:
        text = re.sub(r"<[^>]+>", " ", raw)
        for w in RED_LITERAL:
            if w in text:
                reds.append((ln, w, text.strip()[:100]))
        for pat, tag in RED_PATTERN:
            m = re.search(pat, text, re.I)
            if m and not (tag == "批号引用" and any(h in text for h in WHITELIST_HINTS)):
                reds.append((ln, f"{tag}·{m.group(0)[:24]}", text.strip()[:100]))
        for w in AMBER_LITERAL:
            if w in text:
                ambers.append((ln, w, text.strip()[:80]))
        for pat, tag in AMBER_PATTERN:
            m = re.search(pat, text)
            if m:
                ambers.append((ln, f"{tag}·{m.group(0)[:20]}", text.strip()[:80]))
    return reds, ambers

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    total_red = 0
    for p in sys.argv[1:]:
        reds, ambers = scan(p)
        total_red += len(reds)
        if reds:
            print(f"❌{p}: {len(reds)}处红（判例应修·先修后交）")
            for ln, w, ctx in reds:
                print(f"   L{ln}[红·{w}] …{ctx}…")
        else:
            print(f"✅{p}: 红0（可交）")
        if ambers:
            print(f"   ⚠️黄{len(ambers)}处（判例容忍级·目验复核）：" +
                  "；".join(sorted({w for _, w, _ in ambers}))[:160])
    print(f"== 预扫汇总: 红{total_red} ==")
    sys.exit(1 if total_red else 0)

if __name__ == "__main__":
    main()
