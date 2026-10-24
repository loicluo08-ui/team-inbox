#!/usr/bin/env python3
# 物理3章章级装配器（队4·B席·1024·对齐第1章交付口径+C5+C7+费曼装配层插桩）——md→HTML·产线方言：#系列/表格/列表/粗体/code/hr/引用/图规格块
# C5机制：table/card/blockquote page-break-inside:avoid 注入；C7页码：playwright footer driver
import re, html, sys, os, importlib.util
_p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "工具_装配净化器_队4_1024.py")
_spec = importlib.util.spec_from_file_location("assembler_purifier", _p)
pur = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(pur)  # W2净化器（16:07裁定②·A2口径清除留痕·同族根修）

SECS = [
    ("3.1", "重力与重心、弹力（两半场合流）", "产出_队4/物理-3.1.md"),
    ("3.2", "摩擦力", "产出_队4/物理-3.2.md"),
    ("3.3", "牛顿第三定律", "产出_队4/物理-3.3.md"),
    ("3.4", "力的合成", "产出_队4/物理-3.4.md"),
    ("3.5", "力的分解", "产出_队4/物理-3.5.md"),
]
CHAP = "第三章 相互作用——力"

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
        "3.1": ("<h2 id=\"feym1\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“重力三件套＋重心＋弹力两条件”怎么撑起一张完整的受力分析图。</p>"
                "<p><b>第一步·先说结论</b>（重力=地球的吸力·G=mg·竖直向下；重心=各部分重力的加权平均位置·可在体外；弹力=形变恢复的推拉·两条件缺一不可）→<b>第二步·再说为什么</b>（等效替换思维：所有小块重力同向同比→合成一点；形变恢复才产生推拉）→<b>第三步·举个例子</b>（悬挂法两次交点定重心·二力平衡依据）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：竖直向下画成“指向地心”——易错卡，可溯（竖直向下≠指向地心）。<b>卡壳路由</b>：卡在“重心为什么能在体外”→回正文§加权平均（平均分不等于任何一人得分）；卡在“弹力方向怎么定”→回正文§三规则（面⊥面/绳沿绳/杆沿杆）。<b>⚠简化边界</b>：g随纬度微变一句带过，深究在深读区。</p>"),
        "3.2": ("<h2 id=\"feym2\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“摩擦力为什么不能套公式”——静摩擦按需供给、滑动摩擦固定收费、方向只认相对。</p>"
                "<p><b>第一步·先说结论</b>（静摩擦0≤f≤f_max按需供给；滑动f=μF_N；方向=反向于相对运动趋势）→<b>第二步·再说为什么</b>（被动力：大小由运动状态反推，不由公式正算）→<b>第三步·举个例子</b>（推30N箱子没动摩擦就是30N——张口代μmg即最高频错误）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：见摩擦就写μmg——易错卡，原话可溯（第一个“大小不写死”的力）。<b>卡壳路由</b>：卡在“静动怎么切换”→回正文§二步走（先判状态再选公式）；卡在“摩擦可以是动力”→回传送带例（轻放行李沿带向前）。<b>⚠简化边界</b>：f_max≈μF_N近似口径如实标注。</p>"),
        "3.3": ("<h2 id=\"feym3\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“作用力与反作用力”四同（等大/反向/共线/同性质）两不同（异体/同存亡），以及它为什么不是平衡力。</p>"
                "<p><b>第一步·先说结论</b>（牛顿第三定律：作用反作用等大反向共线异体）→<b>第二步·再说为什么</b>（力是物体间的相互作用·单方面施力不存在）→<b>第三步·举个例子</b>（划船推水·走路蹬地——反作用力在别的物体上）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：“等大反向=平衡力”——易错卡，可溯（平衡力同体·作用反作用异体）。<b>卡壳路由</b>：卡在“马拉车谁拉谁”→回正文§异体分析（车加速靠地面摩擦·非马拉车力）；卡在“鸡蛋碰石头为何破”→回正文（同样的力·承受结构不同）。<b>⚠简化边界</b>：非接触相互作用（场）一句带过。</p>"),
        "3.4": ("<h2 id=\"feym4\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白合力与分力“等效替代”的本质，以及平行四边形/三角形两画法的互译。</p>"
                "<p><b>第一步·先说结论</b>（合力=与几个力等效的一个力·等效替代不是凭空多出来的力）→<b>第二步·再说为什么</b>（矢量合成按平行四边形法则·三角形是其半边变体）→<b>第三步·举个例子</b>（互成120°三等力合力为零——矢量不是标量加法）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：“合力一定大于分力”——易错卡，可溯（矢量合成1+1可以=0）。<b>卡壳路由</b>：卡在“什么时候合力最大最小”→回正文（同向最大·反向最小）；卡在“三角形法则怎么走”→回例题首尾相接画法。<b>⚠简化边界</b>：多力合成先两两合一句即可。</p>"),
        "3.5": ("<h2 id=\"feym5\">费曼检验（装配层插桩·学完立即做·2分钟）</h2>"
                "<p><b>“凡我不能创造之物，我便无法真正理解。”</b>——费曼办公室黑板遗言（1988）。<b>仪式</b>：先口述录音60-90秒，<b>说完再往下看</b>对照。</p>"
                "<p><b>系统整合题</b>（三步引导链）：给同桌讲明白“分解的两个依据”（效果分解与正交分解）各什么时候用，以及轴怎么选才省力。</p>"
                "<p><b>第一步·先说结论</b>（分解=合成的逆运算·按效果或按正交·轴是工具不是物理）→<b>第二步·再说为什么</b>（正交化让两个垂直方向各自独立列式·sin/cos按作用挂）→<b>第三步·举个例子</b>（斜面上物体：沿面挂mgsinθ驱动下滑·压面挂mgcosθ定摩擦）。</p>"
                "<p><b>照妖镜</b>（典型错误·可溯）：sin/cos对调——易错卡，可溯（驱动用sin·压力用cos）。<b>卡壳路由</b>：卡在“轴怎么选”→回正文§选轴标准（少拆几个力）；卡在“一份劲拆两份”→回正文（拉行李箱：往前拖＋往上提）。<b>⚠简化边界</b>：任意三角形分解在3.4三角形法则互为逆运算一句带过。</p>"),
    }
    for idx, (num, title, path) in enumerate(SECS, 1):
        md = open(path).read()
        md = pur.purify_md(md)  # W2净化：v18挂接注/簇编制名/装配批注A2口径清除（canonical源件零触碰）
        blocks = md_to_html(md, idx)
        sid = f"sec{idx}"
        toc.append(f"<b style=\"color:#fff\">{num} {title}</b>：" + " · ".join(
            f"<a href=\"#{bid}\" style=\"color:#4da3ff;text-decoration:none\">{re.sub(r'<[^>]+>','',bh).strip()}</a>"
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
    chapmap = ("章首地图：3.1 重力与重心＋弹力（受力分析的家底·两半场合流）→ 3.2 摩擦力（被动力家族第二课·先判静动再选公式）→ "
               "3.3 牛顿第三定律（力的相互作用·异体等大反向）→ 3.4 力的合成（等效替代·矢量加法）→ "
               "3.5 力的分解（合成的逆运算·效果分解与正交分解）。"
               "跨章出口：受力分析全套装→第四章动力学直接调用·正交分解→第4章连接体；被动力思维贯穿全书。主线读完即可做题；边界提醒：先判状态再选公式·受力分析只画别的物体给它的力。")
    mindcard = ("<h2 id=\"chapcard\">全章思维卡（五节元思维速查·考前60秒）</h2><table>"
                "<tr><th>节</th><th>带走一句话</th><th>防坑锚点</th></tr>"
                "<tr><td>3.1</td><td>重力三件套＋重心=加权平均位置（可在体外）；弹力=形变恢复的推拉·两条件缺一不可</td><td>竖直向下≠指向地心；弹力方向三规则（面⊥面/绳沿绳/杆沿杆）</td></tr>"
                "<tr><td>3.2</td><td>静摩擦按需供给（0≤f≤f_max无公式）·滑动f=μF_N固定收费；方向只认相对运动趋势</td><td>张口代μmg=最高频错误；摩擦可以是动力；先判静动再选公式</td></tr>"
                "<tr><td>3.3</td><td>作用力反作用力：等大反向共线同性质·异体同存亡</td><td>不是平衡力（平衡力同体）；鸡蛋碰石头=同样的力不同的承受结构</td></tr>"
                "<tr><td>3.4</td><td>合力=等效替代的一个力·矢量按平行四边形合成</td><td>合力可以小于分力（1+1=0）；三角形法则是半边变体</td></tr>"
                "<tr><td>3.5</td><td>分解=合成的逆运算·轴是工具不是物理（少拆几个力）</td><td>驱动用sin压力用cos；正交化让两方向独立列式</td></tr></table>")
    selftest = ("<h2 id=\"chaptest\">全章自测三题（跨节串联·先做再看出处）</h2><ol>"
                "<li>（3.1×3.2桥）斜面上一个物体（倾角θ）：画出它受的全部力，说明每个力的施力物体与方向依据。<br>出处与解：3.1弹力方向规则＋3.2摩擦方向只认相对运动趋势（重力G=mg竖直向下施力物体=地球；支持力F_N=mg·cosθ面⊥面；摩擦沿面反趋势方向——有滑动趋势时静摩擦按需供给）。</li>"
                "<li>（3.2×3.3桥）人走路时，使人前进的力是谁给的？用牛顿第三定律说明“蹬地”与“前进”两力的关系。<br>出处与解：3.3作用反作用异体（脚蹬地=脚对地的力·地给人的反作用力才是前进动力——两力异体不同时作用同一物体，不是平衡力）。</li>"
                "<li>（3.4×3.5桥）斜面倾角30°、物重20N：把重力按效果分解（沿面/压面），并用正交分解复核支持力大小。<br>出处与解：3.5效果分解（沿面mgsinθ=10N·压面mgcosθ≈17.3N）＝3.4合成的逆运算（两分力正交合成回20N·√(10²+17.3²)≈20✓驱动用sin压力用cos）。</li></ol>")
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
    h.append("</body></html>")
    doc = "".join(h)
    doc, n_w3 = re.subn(r'<p><b>(【[^】]{2,40}】)</b></p>', r'<p style="page-break-after:avoid"><b>\1</b></p>', doc)  # W3防悬垂
    ok, bad = pur.verify_zero(doc)
    if not ok:
        print("A4.3自检FAIL: 词面残留", bad)
        for w, ctxs in pur.residual_report(doc).items():
            for c in ctxs[:6]: print("  [", w, "]", c)
        sys.exit(1)
    out = "产出_队4/装配_物理必修一_第3章_1024.html"
    open(out, "w").write(doc)
    print("W3防悬垂", n_w3, "·净化规则", len(pur.RULES_REPORT), "组")
    print("HTML_OK", out, len("".join(h)), "字节 · 块锚", n_anchor)

if __name__ == "__main__":
    main()
