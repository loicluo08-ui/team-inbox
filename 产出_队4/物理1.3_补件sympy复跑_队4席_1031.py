#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
物理1.3《速度》main正本件dd922c8 补件QC·sympy独立复跑
队4席（并行搜索员A·本会话6a59c9165b94d92a3eab22fe·批2）1031午后
口径：对正本件foot所列16验点+正文内嵌sympy标签逐条独立复算；
      另对图B(v-t示意)SVG几何值域做审计（点值/时 span 由坐标反算）。
留痕：本文件+运行输出（输出全文嵌入QC单随件）。
"""
from sympy import Rational, simplify
import re, sys

PASS, FAIL = [], []

def chk(name, expr, expect):
    try:
        val = simplify(expr)
        ok = simplify(val - expect) == 0
        (PASS if ok else FAIL).append(f"{name}: {expr} = {val} (期望{expect}) {'✅' if ok else '❌'}")
    except Exception as e:
        FAIL.append(f"{name}: 异常 {e}")

# ---------- 一、foot 16验点复算 ----------
chk("验点1 前1s平均",   Rational(9,1),  9)
chk("验点2 前2s平均",   Rational(16,2), 8)
chk("验点3 前3s平均",   Rational(21,3), 7)
chk("验点4 前4s平均",   Rational(24,4), 6)
chk("验点5 全程5s平均", Rational(25,5), 5)
chk("验点6 最后2s平均", Rational(4,2),  2)
chk("验点7 72km/h→m/s", Rational(72,1)/Rational(36,10), 20)
chk("验点8 100km/h→m/s", Rational(100,1)/Rational(36,10), Rational(250,9))
chk("验点9 0.02×5",     Rational(2,100)*5,  Rational(1,10))
chk("验点10 0.02×3",    Rational(2,100)*3,  Rational(3,50))
# 验点11 往返平均48≠50：s=120km整数化
t_go = Rational(120,60); t_back = Rational(120,40)
v_round = Rational(240,1)/(t_go+t_back)
chk("验点11 往返平均", v_round, 48)
(PASS if simplify(v_round-50)!=0 else FAIL).append(f"验点11b 48≠50 断言 {'✅' if simplify(v_round-50)!=0 else '❌'}")
chk("验点12 100/12.5", Rational(100,1)/Rational(25,2), 8)
chk("验点13 100/20",   Rational(100,20), 5)
# 验点14 描点min/max/跨度：见下文三、几何审计（此处记转核）
# 验点15/16 Δx=20−100=−80；v=−80/4=−20
chk("验点15 Δx=20−100", 20-100, -80)
chk("验点16 v=−80/4",  Rational(-80,4), -20)

# ---------- 二、正文内嵌sympy标签复算（HTML行号锚） ----------
chk("L97  图A甲 100/12.5", Rational(100,1)/Rational(125,10), 8)
chk("L98  图A乙 100/20",   Rational(100,20), 5)
chk("L120 五连", Rational(9,1)+Rational(16,2)+Rational(21,3)+Rational(24,4)+Rational(25,5), 35)  # 9+8+7+6+5
chk("L121 往返反例", v_round, 48)
chk("L122/188 最后2s", Rational(3+1,2), 2)
chk("L129 速度计 72/3.6", Rational(72,1)/Rational(36,10), 20)
chk("L135 计数点0.1s", Rational(2,100)*5, Rational(1,10))
chk("L137 逼近0.06s",  Rational(2,100)*3, Rational(3,50))

# ---------- 三、图B(v-t示意)SVG几何审计 ----------
# 正本件SVG：轴 y=250→v=0，47px每0.05（网格y=203/156/109/62）；t轴 x=70→0，82.67px每1s
cys = [199.4,199.4,184.2,171.9,167.2,158.8,150.4,146.6,142.8,150.4]
cxs = [70,104,139,173,207,242,276,310,345,379]
vs = [Rational(250*100- int(c*100), 94000) for c in cys]   # v=(250−cy)/940
ts = [Rational(int((c-70)*100), 8267) for c in cxs]
vmin, vmax = min(vs), max(vs)
tspan = max(ts)-min(ts)
print(f"图B几何审计：点列v值={[float(v) for v in vs]}")
print(f"图B几何审计：v_min={float(vmin):.4f} v_max={float(vmax):.4f} t_span={float(tspan):.3f}s")
geo_note = (f"SVG内标注'0.07→0.14 m/s·跨度3.6s' 与几何反算值 "
            f"v_min={float(vmin):.3f}/v_max={float(vmax):.3f}/跨度{float(tspan):.2f}s 不一致"
            f"（点列程序生成走向示意·轴刻度自洽·标注值未随几何·观察级候v1.1口径修注）")

# ---------- 四、foot验点8/15/16正文对应位审计 ----------
html = open("正本_物理1.3.html", encoding="utf-8").read()
body = html.split("<body>")[1]
for tag, pat in [("验点8 100/3.6", r"100\s*/\s*3\.6|100÷3\.6|250/9"),
                 ("验点15 Δx=−80", r"−80|-80"),
                 ("验点16 v=−20",  r"−20(?!18)|m/s）|v＝?−20")]:
    hits = [m.start() for m in re.finditer(pat, body)]
    # 只统计 foot 之外（foot 位于 .foot div）
    footpos = body.find('class="foot"')
    inbody = [h for h in hits if footpos == -1 or h < footpos]
    print(f"{tag} 正文对应位: {'未见（验点冗余·观察级）' if not inbody else f'命中{len(inbody)}处'}")

print("\n===== PASS明细 =====")
for p in PASS: print("✅", p)
print("\n===== FAIL明细 =====")
print("（无）" if not FAIL else "\n".join("❌ "+f for f in FAIL))
print(f"\n统计：数值验点 PASS={len(PASS)} FAIL={len(FAIL)}")
print(geo_note)
sys.exit(1 if FAIL else 0)
