#!/usr/bin/env python3
# 物理1章章级装配器（队4·B席·1024）——md→HTML·产线方言：#系列/表格/列表/粗体/code/hr/引用/图规格块
# C5机制：table/card/blockquote page-break-inside:avoid 注入；C7页码：playwright footer driver
import re, html, sys, os

SECS = [
    ("1.1", "质点 参考系", "产出_队4/物理-1.1.md"),
    ("1.2", "位移 速度", "产出_队4/物理-1.2.md"),
    ("1.3", "加速度", "产出_队4/物理-1.3.md"),
    ("1.4", "匀变速直线运动的运动学公式（三公式+两推论）", "产出_队4/物理-1.4.md"),
    ("1.5", "运动学图像：x-t图与v-t图", "产出_队4/物理-1.5.md"),
    ("1.6", "追及相遇问题", "产出_队4/物理-1.6.md"),
]
CHAP = "第一章 运动的描述"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s

def md_to_html(md, sn):
    """单节md→HTML块序列。返回 (块列表, 锚表)。块=(kind, id, html)"""
    lines = md.split("\n")
    out, k, in_code, code_buf = [], 0, False, []
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            if in_code:
                out.append(("code", None, "<pre class=\"chain\">" + esc("\n".join(code_buf)) + "</pre>"))
                in_code, code_buf = False, []
            else:
                in_code = True
            i += 1; continue
        if in_code:
            code_buf.append(ln); i += 1; continue
        if ln.startswith("# ") and i == 0:
            i += 1; continue  # L1卡名→节分隔由外壳处理
        if ln.startswith("### "):
            k += 1; hid = f"s{sn}h{k}"
            out.append(("h3", hid, f"<h3 id=\"{hid}\">{inline(ln[4:])}</h3>"))
        elif ln.startswith("## "):
            k += 1; hid = f"s{sn}b{k}"
            out.append(("h2", hid, f"<h2 id=\"{hid}\">{inline(ln[3:])}</h2>"))
        elif ln.startswith("#### "):
            k += 1; hid = f"s{sn}c{k}"
            out.append(("h4", hid, f"<h4 id=\"{hid}\">{inline(ln[5:])}</h4>"))
        elif ln.strip() == "---":
            out.append(("hr", None, "<hr>"))
        elif ln.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ")); i += 1
            out.append(("quote", None, "<div class=\"map\">" + "<br>".join(inline(x) for x in buf) + "</div>"))
            continue
        elif ln.startswith("|"):
            buf = []
            while i < len(lines) and lines[i].startswith("|"):
                buf.append(lines[i]); i += 1
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in buf]
            rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c or "---") for c in r)]
            if rows:
                tb = "<table>" + "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>"
                for r in rows[1:]:
                    tb += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                tb += "</table>"
                if "这节是什么" in tb:  # B9荧光判据：每节速览卡定场核心词mark（确定性规则·一节一mark）
                    tb = tb.replace("<td><b>", '<td><mark class="glow"><b>', 1).replace("</b></td>", "</b></mark></td>", 1)
                out.append(("table", None, tb))
            continue
        elif re.match(r"^\d+\. ", ln) or ln.startswith("- "):
            ordered = bool(re.match(r"^\d+\. ", ln))
            items, tag = [], ("ol" if ordered else "ul")
            while i < len(lines) and (re.match(r"^\d+\. ", lines[i]) if ordered else lines[i].startswith("- ")):
                item = re.sub(r"^(\d+\. |- )", "", lines[i])
                items.append(f"<li>{inline(item)}</li>"); i += 1
            out.append(("list", None, f"<{tag}>" + "".join(items) + f"</{tag}>"))
            continue
        elif ln.strip():
            out.append(("p", None, f"<p>{inline(ln)}</p>"))
        i += 1
    return out

def main():
    parts, toc, n_anchor = [], [], 0
    toc.append(f"<b style=\"color:#7ec9a0\">{CHAP}</b>（六节）")
    for idx, (num, title, path) in enumerate(SECS, 1):
        md = open(path).read()
        blocks = md_to_html(md, idx)
        sid = f"sec{idx}"
        toc.append(f"<b style=\"color:#fff\">{num} {title}</b>：" + " · ".join(
            f"<a href=\"#{bid}\" style=\"color:#4da3ff;text-decoration:none\">{re.sub(r'<[^>]+>','',bh)[3:20].strip('（ ')}</a>"
            for kind, bid, bh in blocks if bid))
        parts.append(f"<div class=\"secdiv\" id=\"{sid}\">◆ ◆ ◆　{num}　{title}</div>")
        parts.extend(bh for _, _, bh in blocks)
        n_anchor += sum(1 for _, bid, _ in blocks if bid)
    chapmap = ("章首地图：1.1 质点 参考系（开工手续：对象简化＋描述起评线）→ 1.2 位移 速度（矢量符号系统·正负号承载方向）→ "
               "1.3 加速度（变化率语法·唯一标准=a与v同向反向）→ 1.4 三公式两推论（预报系统·五量知三求二·刹车截断）→ "
               "1.5 图像（读图三看·斜率/面积两件套）→ 1.6 追及相遇（综合演武场·共速=距离极值判据）。"
               "跨章出口：惯性力→第四章；自由落体→2.4；图像语法全册复用。主线读完即可做题；边界提醒：a恒定＋单向直线＋惯性系三前提贯穿全章。")
    mindcard = ("<h2 id=\"chapcard\">全章思维卡（六节元思维速查·考前60秒）</h2><table>"
                "<tr><th>节</th><th>带走一句话</th><th>防坑锚点</th></tr>"
                "<tr><td>1.1</td><td>身份跟问题走，不跟物体走；不选参考系就谈运动是没有语义的句子</td><td>“小”不是通行证；描述会变，规律不变</td></tr>"
                "<tr><td>1.2</td><td>位移只认“从哪到哪”；平均吃掉方向信息，快慢看平均速率</td><td>长区间平均速度不能冒充瞬时；时间词四种说法先圈圈</td></tr>"
                "<tr><td>1.3</td><td>a量度的是快慢被改写的猛度；判断加速减速唯一标准=a与v同向还是反向</td><td>Δv是矢量差不是标量减法；正负只是坐标系产物</td></tr>"
                "<tr><td>1.4</td><td>五量知三求二，列参数表走路由，不背口诀</td><td>刹车先查t停，数学解要过物理安检；比例结论前提v₀=0漏验即翻车</td></tr>"
                "<tr><td>1.5</td><td>读图三看：先认轴、再看线、后看点；斜率=变化率，面积=累积</td><td>x-t交点=相遇、v-t交点=共速，两者永不混；轴下面积记负</td></tr>"
                "<tr><td>1.6</td><td>统一参考系＋统一时间零点是第一纪律；共速=距离极值临界</td><td>幽灵解必须物理筛；刹车截断位移封顶</td></tr></table>")
    selftest = ("<h2 id=\"chaptest\">全章自测三题（跨节串联·先做再看出处）</h2><ol>"
                "<li>（1.1×1.2桥）商场扶梯以v₁=1 m/s匀速上行，人以相对扶梯v₂=2 m/s沿梯上行，扶梯长L=6 m。分别以扶梯、地面为参考系求通行时间，并说明研究对象能否视为质点。<br>出处与解：1.1跨簇连接题（两系一致t=3 s；人需视为质点——本题不关心肢体姿态）。</li>"
                "<li>（1.2×1.5桥）v-t图上甲以4 m/s匀速、乙同时静止以2 m/s²加速，何时相距最远、最远多少？用面积差与位移公式双轨验证。<br>出处与解：1.2跨簇连接题（t=2 s共速相距最远4 m；面积差读距离=二次函数顶点两张脸）。</li>"
                "<li>（1.4×1.6桥）汽车以20 m/s行驶、刹车加速度大小5 m/s²，求刹车后6 s内位移——并解释为何不能直接代t=6。<br>出处与解：1.4最小验证①（t停=4 s截断，x=40 m；直接代6 s得30 m系“倒车幽灵解”——1.6刹车封顶同款纪律）。</li></ol>")
    css = """<style>
body{font-family:"PingFang SC","Microsoft YaHei",sans-serif;margin:0;padding:18px;background:#0d1117;color:#c9d1d9;line-height:1.75;}
h1.chap{color:#fff;font-size:20px;border-bottom:2px solid #30363d;padding-bottom:8px;}
.secdiv{background:#1c2430;color:#7ec9a0;border-left:4px solid #7ec9a0;padding:6px 10px;margin:20px 0 10px;font-weight:bold;letter-spacing:1px;}
h2{color:#58a6ff;font-size:16px;border-bottom:1px solid #21262d;padding-bottom:4px;margin:18px 0 8px;}
h3{color:#79c0ff;font-size:14.5px;margin:14px 0 6px;}
h4{color:#8b949e;font-size:13px;margin:10px 0 4px;}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:13px;}
th,td{border:1px solid #30363d;padding:5px 8px;text-align:left;vertical-align:top;}
th{background:#161b22;color:#58a6ff;}
pre.chain{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:10px;font-size:12px;line-height:1.5;white-space:pre-wrap;}
.map{background:#12261e;border-left:3px solid #2ea043;padding:7px 10px;margin:8px 0;font-size:13px;}
.toc{background:#1c2430;border:1px solid #2a3140;border-radius:8px;padding:10px 14px;margin:14px 0;font-size:12px;line-height:2;word-spacing:4px;}
.chapmap{background:#1a2332;border-left:3px solid #58a6ff;padding:9px 12px;margin:12px 0;font-size:13px;}
hr{border:0;border-top:1px dashed #30363d;margin:14px 0;}
b{color:#e6edf3;} li{margin:3px 0;}
@media print{
 body{background:#fff;color:#111;}
 h1.chap{color:#000;border-color:#333;} .secdiv{background:#eee;color:#000;border-color:#333;}
 h2{color:#000;border-color:#bbb;} h3,h4{color:#000;} b{color:#000;}
 th,td{border-color:#888;} th{background:#e8e8e8;color:#000;}
 pre.chain{background:#f2f2f2;border-color:#999;color:#000;} .map{background:#f0f7f0;color:#111;}
 .toc{background:#f6f6f6;border-color:#999;} .toc a{color:#000 !important;text-decoration:none;}
 .chapmap{background:#eef4fc;color:#111;} hr{border-color:#aaa;}
 /* C5机制注入：块级防断（表格/卡面/引用/链图/节隔/清单行） */
 table,.map,.toc,.secdiv,.chapmap,pre.chain,.feedback{page-break-inside:avoid;}
 tr,li{page-break-inside:avoid;}
 h2,h3{page-break-after:avoid;}
}
</style>"""
    h = [f"<!DOCTYPE html><html lang=\"zh\"><head><meta charset=\"utf-8\"><title>{CHAP}·物理必修一</title>{css}</head><body>"]
    h.append(f"<h1 class=\"chap\">{CHAP}　物理必修一</h1>")
    h.append(f"<div class=\"chapmap\">{esc(chapmap)}</div>")
    h.append(f"<div class=\"toc\"><b style=\"color:#fff\">本章目录</b>　" + "　|　".join(toc) +
             "　|　<a href=\"#chapcard\" style=\"color:#4da3ff;text-decoration:none\">全章思维卡</a> · <a href=\"#chaptest\" style=\"color:#4da3ff;text-decoration:none\">全章自测三题</a></div>")
    h.extend(parts)
    h.append(mindcard)
    h.append(selftest)
    h.append("<div style=\"margin-top:14px;font-size:11px;color:#8b949e\">第一章完 · 六节（1.1-1.6）｜回收：惯性力→第四章·自由落体→2.4·图像语法→全册</div>")
    h.append("</body></html>")
    out = "产出_队4/装配_物理必修一_第1章_1024.html"
    open(out, "w").write("".join(h))
    print("HTML_OK", out, len("".join(h)), "字节 · 块锚", n_anchor)

if __name__ == "__main__":
    main()
