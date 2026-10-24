#!/usr/bin/env python3
# 物理4章章级装配器（队4·B席·1024·对齐第1章交付口径+C5+C7+费曼装配层插桩）——md→HTML·产线方言：#系列/表格/列表/粗体/code/hr/引用/图规格块
# C5机制：table/card/blockquote page-break-inside:avoid 注入；C7页码：playwright footer driver
import re, html, sys, os

SECS = [
    ("4.1", "牛顿第一定律", "产出_队4/物理-4.1.md"),
    ("4.2", "牛顿第二定律", "产出_队4/物理-4.2.md"),
    ("4.3", "牛顿第三定律", "产出_队4/物理-4.3.md"),
    ("4.4", "超重和失重", "产出_队4/物理-4.4.md"),
    ("4.5", "连接体", "产出_队4/物理-4.5.md"),
]
CHAP = "第四章 运动和力的关系"

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
                    row1 = tail.split("</tr>")[0]
                    if "<b>" in row1:
                        tail = tail.replace("<b>", '<mark class="glow"><b>', 1).replace("</b>", "</b></mark>", 1)
                    else:  # 无粗体定场句（1.4型）：标记定场cell首短句
                        m = re.search(r'<td>([^<]{8,28}?)[，。；]', row1)
                        if m: tail = tail.replace(m.group(1), f'<mark class="glow">{m.group(1)}</mark>', 1)
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
        "4.1": ("<h2 id=\"feym1\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“运动状态改变才需要原因”这句为什么值一整章，以及惯性为什么用质量量度。</p>"
                "<p><b>第一步·先说结论</b>（不受力=保持匀速直线或静止；改变的“变化率”才需要力）→<b>第二步·再说为什么</b>（看不见的摩擦力漏账了两千年·伽利略理想实验=受控外推）→<b>第三步·举个例子</b>（冰壶离手不推仍前行·急刹车人前倾=上半身保持原速）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：“受到惯性（力）的作用”——易错卡主卡，v18可溯（惯性是属性不是力）。<b>卡壳路由</b>：卡在“惯性系是什么”→回正文§隐藏前提；卡在“质量为何量度惯性”→回深读区§三问。<b>⚠简化边界</b>：第一定律不能单独实验验证（摩擦消不干净），一句带过。</p>"),
        "4.2": ("<h2 id=\"feym2\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲清 F=ma 的三句读法（因果/方向/单位）与正交分解的主战场地位。</p>"
                "<p><b>第一步·先说结论</b>（F=合外力·a与F同向·m是抵抗变化的倔强值）→<b>第二步·再说为什么</b>（定义式反着用·矢量式=分量式各管一轴）→<b>第三步·举个例子</b>（沿面/压面两轴把斜面问题拆成两个独立一元问题）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：合力漏项（漏摩擦/漏分量）——易错卡，v18可溯（受力分析只画别的物体给的力）。<b>卡壳路由</b>：卡在“正交轴怎么选”→回3.5§选轴标准；卡在“瞬时对应关系”→回正文§F与a同生灭。<b>⚠简化边界</b>：微积分形式F=dp/dt一句带过（深读区）。</p>"),
        "4.3": ("<h2 id=\"feym3\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲清作用反作用“四同两不同”，以及它与平衡力的判据分界。</p>"
                "<p><b>第一步·先说结论</b>（等大/反向/共线/同性质·异体/同存亡）→<b>第二步·再说为什么</b>（力=相互作用·单方施力不存在）→<b>第三步·举个例子</b>（划船推水·走路蹬地——前进的动力来自地面反作用）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：“等大反向=平衡力”——易错卡主卡，v18可溯（平衡力同体·作用反作用异体）。<b>卡壳路由</b>：卡在“鸡蛋碰石头为何破”→回正文（同力异承受结构）；卡在“马拉车”→回例题§异体分析。<b>⚠简化边界</b>：场相互作用一句带过。</p>"),
        "4.4": ("<h2 id=\"feym4\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明“视重=支持力≠重力”与超失重的分界判据（a向上超·a向下失·a=g完全失重）。</p>"
                "<p><b>第一步·先说结论</b>（超失重看加速度方向不看速度方向）→<b>第二步·再说为什么</b>（牛顿第二定律在竖直轴的应用·F_N−mg=ma）→<b>第三步·举个例子</b>（电梯三段：上行加速超重·匀速正常·减速上行失重）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：“上升=超重·下降=失重”——易错卡，v18可溯（看a不看v）。<b>卡壳路由</b>：卡在“完全失重内部现象”→回正文（水不下落·天平失效）；卡在“视重公式”→回例1三连答。<b>⚠简化边界</b>：航天失重的轨道学解释（引力=向心力）在万有引力章。</p>"),
        "4.5": ("<h2 id=\"feym5\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲清连接体问题的两步走（整体定a·隔离求内力）与T比=质量比的由来。</p>"
                "<p><b>第一步·先说结论</b>（整体法定共同a·隔离法拆内力·T比=质量反比配平）→<b>第二步·再说为什么</b>（内力成对抵消·整体视角消元；隔离后内力变外力）→<b>第三步·举个例子</b>（m₁=2m₂跨轮：a=g/3·T比=1:2三段张力逐位复算）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：内力当外力重复算——易错卡，v18可溯（整体隔离各画各的图）。<b>卡壳路由</b>：卡在“何时整体何时隔离”→回正文§两步走口诀（求a整体·求内力隔离）；卡在“绳轻不可伸长”→回正文模型前提。<b>⚠简化边界</b>：含摩擦连接体一句带过（4.2正交＋本节两步走组合）。</p>"),
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
    chapmap = ("章首地图：4.1 牛顿第一定律（因果革命·惯性=质量的倔强值）→ 4.2 牛顿第二定律（F=ma·正交分解主战场）→ "
               "4.3 牛顿第三定律（相互作用·异体等大反向）→ 4.4 超重和失重（视重=支持力·看a不看v）→ "
               "4.5 连接体（两步走·整体定a隔离求内力）。"
               "跨章出口：第三章受力分析全套装直接调用·正交分解承3.5·共速与摩擦承3.2；牛顿三定律=动力学的全部地基。主线读完即可做题；边界提醒：受力分析只画别的物体给的力·惯性系前提贯穿。")
    mindcard = ("<h2 id=\"chapcard\">全章思维卡（五节元思维速查·考前60秒）</h2><table>"
                "<tr><th>节</th><th>带走一句话</th><th>防坑锚点</th></tr>"
                "<tr><td>4.1</td><td>运动状态改变才需要原因；惯性=质量的倔强值（只看体重不看车速）</td><td>惯性是属性不是力；第一定律隐藏前提=惯性系</td></tr>"
                "<tr><td>4.2</td><td>F=ma三句读法：合外力/同向/单位统一；正交分解主战场</td><td>受力分析只画别的物体给的力；F与a同生灭（瞬时对应）</td></tr>"
                "<tr><td>4.3</td><td>作用反作用：等大反向共线同性质·异体同存亡</td><td>不是平衡力（平衡力同体）；鸡蛋碰石头=同力异承受</td></tr>"
                "<tr><td>4.4</td><td>视重=支持力≠重力；超失重看加速度方向不看速度方向</td><td>a向上超·a向下失·a=g完全失重（水不落天平失效）</td></tr>"
                "<tr><td>4.5</td><td>两步走：整体定a·隔离求内力；T比=质量配平</td><td>内力不当外力重复算；绳轻不可伸长模型前提</td></tr></table>")
    selftest = ("<h2 id=\"chaptest\">全章自测三题（跨节串联·先做再看出处）</h2><ol>"
                "<li>（4.1×4.2桥）冰壶离手后沿冰面匀速滑行，它“需要力来维持”吗？若改在粗糙冰面减速滑行，各阶段受什么力？<br>出处与解：4.1因果革命（匀速无需力·减速=摩擦力在改变状态）＋4.2受力分析（重力/支持力/摩擦三力·F=ma算a）。</li>"
                "<li>（4.3×4.4桥）人站在电梯里，电梯加速上升：人对电梯的压力与人的重力谁大？电梯对人的支持力又如何？<br>出处与解：4.4视重公式（F_N−mg=ma→F_N=mg+ma&gt;mg超重；人对电梯压力=支持力的反作用力·4.3异体等大反向）。</li>"
                "<li>（4.5桥）m₁=2 m₂跨过定滑轮（绳轻不可伸长·无摩擦）：共同加速度多大？绳张力与两重力什么关系？<br>出处与解：4.5两步走（整体a=(m₁−m₂)g/(m₁+m₂)=g/3·隔离T=m₂(g+a)=4m₂g/3·T比=1:2质量配平·逐位复算口径）。</li></ol>")
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
    out = "产出_队4/装配_物理必修一_第4章_1024.html"
    open(out, "w").write("".join(h))
    print("HTML_OK", out, len("".join(h)), "字节 · 块锚", n_anchor)

if __name__ == "__main__":
    main()
