#!/usr/bin/env python3
# 物理2章章级装配器（队4·B席·1024·对齐第1章交付口径+C5+C7+费曼装配层插桩）——md→HTML·产线方言：#系列/表格/列表/粗体/code/hr/引用/图规格块
# C5机制：table/card/blockquote page-break-inside:avoid 注入；C7页码：playwright footer driver
import re, html, sys, os

SECS = [
    ("2.1", "实验：探究小车速度随时间变化的规律（打点计时器·纸带类）", "产出_队4/物理-2.1.md"),
    ("2.2", "匀变速直线运动的速度与时间的关系", "产出_队4/物理-2.2.md"),
    ("2.3", "匀变速直线运动的位移与时间的关系", "产出_队4/物理-2.3.md"),
    ("2.4", "自由落体运动", "产出_队4/物理-2.4.md"),
]
CHAP = "第二章 匀变速直线运动的研究"

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
                    head, sep, tail = tb.partition("这节是什么")
                    tail = tail.replace("<b>", '<mark class="glow"><b>', 1).replace("</b>", "</b></mark>", 1)
                    tb = head + sep + tail
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
    toc.append(f"<b style=\"color:#7ec9a0\">{CHAP}</b>（四节）")
    FEYN = {
        "2.1": ("<h2 id=\"feym1\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“从一条纸带读出全套运动信息”的流水线——装置两机型怎么选→五步操作为什么先通电→T=0.10 s怎么来→逐差法为什么用全部数据。</p>"
                "<p><b>第一步·先说结论</b>（纸带=一串等时快照；T=0.10 s、Δx恒定即匀变速）→<b>第二步·再说为什么</b>（先通电是等打点稳定；逐差用全部数据是减偶然误差）→<b>第三步·举个例子</b>（2019·全国卷ⅠT22：点距疏密定打点先后，B到D整段求vC）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：先放小车后开机——易错卡①，v18实验一步骤原文可溯（先接通电源，待打点稳定后再释放小车）。<b>⚠简化边界</b>：打点摩擦与空气阻力归入系统误差，讲的时候一句“系统误差消不掉、只能估”即可，深究在误差分析段。</p>"),
        "2.2": ("<h2 id=\"feym2\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“为什么速度式不用背”＋“刹车题为什么必须t停先行”。</p>"
                "<p><b>第一步·先说结论</b>（v=v₀+at就是a=(v−v₀)/t反着用，任一时刻多快）→<b>第二步·再说为什么</b>（a恒定才叫匀变速，公式才成立；v=0之后公式给的是倒车幽灵解）→<b>第三步·举个例子</b>（20 m/s刹车5 m/s²：t停=4 s，问6 s按4 s算）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：直接代t=6得“倒车解”——易错卡，v18原话可溯（物理上物体早已静止，这个解必须人工丢弃）。<b>⚠简化边界</b>：a恒定前提失效的场景（变力）一句“分段处理”带过，微积分在深读区。</p>"),
        "2.3": ("<h2 id=\"feym3\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：用一张v-t图给同桌讲清三条公式怎么同源：面积=梯形→②位移式；两式消t→③速度-位移式；中点时刻→平均速度=(v₀+v)/2。</p>"
                "<p><b>第一步·先说结论</b>（三公式是同一运动的三个投影，信息守恒可互推）→<b>第二步·再说为什么</b>（图线下面积累积=位移；消去t=换记账视角不携带新信息）→<b>第三步·举个例子</b>（判别式三情况：Δ&gt;0两次相遇仍须物理筛根——乙加速甲匀速，t₂是模型边界牺牲品）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：把“两次追上”当结论不筛根——易错卡，v18同簇深度追问可溯（Δ&gt;0=两次相遇：先追上后反超）。<b>⚠简化边界</b>：匀加速无限持续的假设在长时间尺度失真，讲的时候一句“模型有边界”即可。</p>"),
        "2.4": ("<h2 id=\"feym4\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲清伽利略推理链凭什么推翻“重的落得快”两千年直觉，以及自由落体两要件为什么缺一不可。</p>"
                "<p><b>第一步·先说结论</b>（自由落体=纯净版匀加速：v₀=0＋只受重力，所有物体同g）→<b>第二步·再说为什么</b>（重力与惯性恰好配平；捆缚佯谬让旧理论自我崩溃）→<b>第三步·举个例子</b>（滴水法测g：等时距采样看Δx是否恒定，2.1同构回收）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：拿羽毛当自由落体——易错卡，v18原话可溯（“轻的落得快”两千年直觉在理想条件下是错的；空气阻力显著即出圈）。<b>⚠简化边界</b>：g是本地参数（9.780～9.832·跨精度要换g）；外推可以提假设，不能替验证。</p>"),
    }
    for idx, (num, title, path) in enumerate(SECS, 1):
        md = open(path).read()
        blocks = md_to_html(md, idx)
        sid = f"sec{idx}"
        toc.append(f"<b style=\"color:#fff\">{num} {title}</b>：" + " · ".join(
            f"<a href=\"#{bid}\" style=\"color:#4da3ff;text-decoration:none\">{re.sub(r'<[^>]+>','',bh)[3:20].strip('（ ')}</a>"
            for kind, bid, bh in blocks if bid))
        parts.append(f"<div class=\"secdiv\" id=\"{sid}\">◆ ◆ ◆　{num}　{title}</div>")
        feyn = FEYN.get(num)
        inserted = False
        for _, bid, bh in blocks:
            if feyn and (not inserted) and "本节串联图" in bh:
                parts.append(feyn)
                n_anchor += 1
                inserted = True
            parts.append(bh)
        n_anchor += sum(1 for _, bid, _ in blocks if bid)
    chapmap = ("章首地图：2.1 实验：探究小车速度随时间变化的规律（打点计时器·纸带——全章的实验地基·先通电后放车）→ "
               "2.2 速度式 v=v₀+at（定义式反着用·刹车截断先行）→ 2.3 位移式 x=v₀t+½at²（梯形面积推导·三公式合拢·追及判据）→ "
               "2.4 自由落体（纯净版匀加速·伽利略推理链·理想化-修正两段式）。"
               "跨章出口：逐差法→1.4推论A同源·共速判据→1.6·惯性系前提→第四章；自由落体=匀变速第一个标准实例。主线读完即可做题；边界提醒：a恒定＋单向直线＋惯性系三前提贯穿全章。")
    mindcard = ("<h2 id=\"chapcard\">全章思维卡（四节元思维速查·考前60秒）</h2><table>"
                "<tr><th>节</th><th>带走一句话</th><th>防坑锚点</th></tr>"
                "<tr><td>2.1</td><td>纸带是一串等时快照，点距就是速度的影子——先读影子疏密，再动笔</td><td>先通电后放车（教材原文级铁律）；勿分段量、舍去过密点；Δx恒定才是匀变速</td></tr>"
                "<tr><td>2.2</td><td>速度式不用背——a的定义式反着用；刹车题先查t停，t用小的那个</td><td>倒车幽灵解必须人工丢弃；km/h忘换算是经典事故</td></tr>"
                "<tr><td>2.3</td><td>三公式同一运动的三个投影，信息守恒可互推；判别式是能否追上的体检表</td><td>Δ&gt;0两根必须物理筛根；刹车截断位移封顶（40m对30m）；比例结论前提v₀=0</td></tr>"
                "<tr><td>2.4</td><td>自由落体=纯净版匀加速（v₀=0＋只受重力缺一不可）；g是本地参数</td><td>两要件缺一即非自由落体；量级自检1s落5m；外推可提假设不能替验证</td></tr></table>")
    selftest = ("<h2 id=\"chaptest\">全章自测三题（跨节串联·先做再看出处）</h2><ol>"
                "<li>（2.1×2.3桥）纸带上连续三段相等时间T=0.1 s内的位移为8 cm、10 cm、12 cm，求加速度，并说明判“匀变速”的依据。<br>出处与解：2.1最小验证②＝2.3推论A现场（Δx=2 cm恒定→a=Δx/T²=2 m/s²；Δx恒定=匀变速指纹，指纹对不上三公式全体退场）。</li>"
                "<li>（2.2×2.3桥）汽车以20 m/s行驶、刹车加速度大小5 m/s²，求刹车后6 s内的位移与6 s末速度——并解释为何不能直接代t=6。<br>出处与解：2.2例1＝2.3最小验证①（t停=4 s截断x=40 m；直接代得30 m系“倒车幽灵解”——数学解必须过物理安检）。</li>"
                "<li>（2.4桥）甲球自由下落1 s、乙球自由下落3 s，各自下落高度与末速度？（取g=10 m/s²）并指出两球运动为何同属自由落体。<br>出处与解：2.4时间尺度手感（甲5 m/10 m·乙45 m/30 m·量级自检纪律；两球均v₀=0＋只受重力=两要件齐）。</li></ol>")
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
    nodes = [("1.1 质点 参考系", "开工手续"), ("1.2 位移 速度", "矢量符号"), ("1.3 加速度", "变化率"),
             ("1.4 三公式两推论", "预报系统"), ("1.5 运动学图像", "读图语法"), ("1.6 追及相遇", "综合演武")]
    svg = ['<svg viewBox="0 0 768 96" style="width:100%;background:#161b22;border-radius:8px;" xmlns="http://www.w3.org/2000/svg">',
           '<defs><marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#4da3ff"/></marker></defs>']
    for i, (a, b_) in enumerate(nodes):
        x = 14 + i * 126
        svg.append(f'<rect x="{x}" y="24" width="108" height="42" rx="7" fill="#1f2733" stroke="#4da3ff"/>')
        svg.append(f'<text x="{x+54}" y="42" text-anchor="middle" font-size="10.5" fill="#e6edf3">{a}</text>')
        svg.append(f'<text x="{x+54}" y="57" text-anchor="middle" font-size="8.5" fill="#9fb3c8">{b_}</text>')
        if i < 5:
            svg.append(f'<line x1="{x+108}" y1="45" x2="{x+124}" y2="45" stroke="#4da3ff" stroke-width="1.4" marker-end="url(#ar)"/>')
    svg.append('</svg>')
    svgmap = "".join(svg)
    h.append(f"<div class=\"chapmap\">{svgmap}"
             f"<p style=\"font-size:11px;color:#9fb3c8\">怎么读这张图：从左到右是本章六节的知识流水线——前两节立“描述运动”的地基（对象简化＋矢量符号），中间两节搭“预测运动”的公式系统（变化率＋三公式），后两节装上“看图与实战”的两条腿；箭头=后一节直接建在前一节上，跳节先补前置。</p>"
             f"<p>{esc(chapmap)}</p></div>")
    h.append(f"<div class=\"toc\"><b style=\"color:#fff\">本章目录</b>　" + "　|　".join(toc) +
             "　|　<a href=\"#chapcard\" style=\"color:#4da3ff;text-decoration:none\">全章思维卡</a> · <a href=\"#chaptest\" style=\"color:#4da3ff;text-decoration:none\">全章自测三题</a></div>")
    h.extend(parts)
    h.append(mindcard)
    h.append(selftest)
    h.append("<div style=\"margin-top:14px;font-size:11px;color:#8b949e\">第一章完 · 六节（1.1-1.6）｜回收：惯性力→第四章·自由落体→2.4·图像语法→全册</div>")
    h.append("</body></html>")
    out = "产出_队4/装配_物理必修一_第2章_1024.html"
    open(out, "w").write("".join(h))
    print("HTML_OK", out, len("".join(h)), "字节 · 块锚", n_anchor)

if __name__ == "__main__":
    main()
