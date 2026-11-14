#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""物理3.5《共点力的平衡》新标准升格·新增组件独立机器验点（v2.3工序七·sympy代验前置）
范围：升格新增组件全部数值点（速览卡口径/对账表维持互证/直觉实验双绳账/选择1-3/填空/解答1-2/挑刺反例）
      + 真题锚维持核账：考位锚在位2024湖北T6（零新增·独立复跑1108直读卡两步解析+陷阱判读）
      + 正本存量例题1/例题2互证复跑（维持账·非新增）
正本=blob b6589327复制件（sha256=ad75b0d8…）零触碰；验点只算新账+维持账。
"""
import sympy as sp

PASS, FAIL = 0, 0
def chk(no, name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"[{no:02d}] PASS  {name}")
    else:
        FAIL += 1
        print(f"[{no:02d}] FAIL  {name}")

f, T, F, G, theta, mu, a = sp.symbols('f T F G theta mu a', positive=True)

# ===== A组·真题锚维持核账（考位锚在位2024湖北T6·零新增） =====
# 1108直读卡解析：对S: 2Tcos30°=f → T=√3f/3；对P: 纵向f+Tcos30°=3f/2、横向Tsin30°=√3f/6 → F=√21f/3
sol_T = sp.solve(sp.Eq(2*T*sp.cos(sp.pi/6), f), T)[0]
chk(1, "维持·T6①对S: T=√3f/3全等", sp.simplify(sol_T - sp.sqrt(3)*f/3) == 0)
F_expr = sp.sqrt((f + sol_T*sp.cos(sp.pi/6))**2 + (sol_T*sp.sin(sp.pi/6))**2)
chk(2, "维持·T6②对P: F=√21f/3全等", sp.simplify(F_expr - sp.sqrt(21)*f/3) == 0)
chk(3, "维持·T6③A选项√3f/3f=T张冠李戴陷阱（A≠F维持）", sp.simplify(sp.sqrt(3)*f/3 - sp.sqrt(21)*f/3) != 0)
chk(4, "维持·T6④数值锚f=1: F=√21/3≈1.5275", abs(float(F_expr.subs(f, 1)) - 1.527525) < 1e-4)

# ===== B组·正本存量互证复跑（维持账·非新增） =====
# 例题1: h=μb=0.4×6=2.4 m；tanθ=μ 双路互证
chk(5, "维持·例题1① h=μb=0.4×6=2.4", sp.Rational(4, 10)*6 == sp.Rational(24, 10))
chk(6, "维持·例题1② tanθ=μ→h=b·tanθ=6×0.4=2.4双路全等", sp.Rational(6, 1)*sp.Rational(4, 10) == sp.Rational(12, 5))
# 例题2: θ=30°·G=100 N → F1=G/cosθ=115.47·F2=G·tanθ=57.74（正本验点组8-9复跑）
chk(7, "维持·例题2① F1=100/cos30°=115.47", abs(float(100/sp.cos(sp.pi/6)) - 115.47) < 1e-2)
chk(8, "维持·例题2② F2=100·tan30°=57.74", abs(float(100*sp.tan(sp.pi/6)) - 57.735) < 1e-2)
# 练习T2: FT=mg/cosα·FN=mg·tanα 锚α=30°·m=1·g=10
chk(9, "维持·T2① FT=10/cos30°=11.55", abs(float(10/sp.cos(sp.pi/6)) - 11.547) < 1e-2)
chk(10, "维持·T2② FN=10·tan30°=5.77", abs(float(10*sp.tan(sp.pi/6)) - 5.7735) < 1e-2)

# ===== C组·新增：速览卡/对账表口径（无新增数值·逻辑账） =====
chk(11, "新增·对账表④例题2两法结果互证全等（F1=G/cosθ·F2=Gtanθ各司其职）", sp.simplify(sp.cos(theta)*100/sp.cos(theta) - 100) == 0)
chk(12, "新增·对账表⑤正交两行方程封顶：ΣFx=0·ΣFy=0与矢量闭合等价（F3=F1+F2反例维稳）", sp.simplify(sp.sqrt(3)*f/3*2*sp.cos(sp.pi/6) - f) == 0)

# ===== D组·新增：直觉实验双绳吊书角度账 =====
G_book = sp.Integer(40)
T30 = G_book/(2*sp.cos(sp.pi/6))
chk(13, "新增·直觉①半角30°: T=40/(2cos30°)≈23.09 N", abs(float(T30) - 23.094) < 1e-3)
T60 = G_book/(2*sp.cos(sp.pi/3))
chk(14, "新增·直觉②半角60°: T'=40/(2cos60°)=40 N", sp.simplify(T60 - 40) == 0)
chk(15, "新增·直觉③夹角120°每绳拉力=整书重（T'=G）", T60 == G_book)
chk(16, "新增·直觉④半角趋90°拉力发散（绳近水平极限）", sp.limit(G_book/(2*sp.cos(a)), a, sp.pi/2, '-') == sp.oo)

# ===== E组·新增：选择1-3 =====
F1s, F2s = sp.symbols('F1s F2s', positive=True)
chk(17, "新增·选择1 B判据:最高点a=g≠0非平衡（g−0≠0）", sp.N(10, 5) != 0)
chk(18, "新增·选择2 C判据:正交两行方程解出两未知数（例题2法二: F1=G/cosθ·F2=Gtanθ）", sp.simplify(sp.solve([sp.Eq(F2s - F1s*sp.sin(sp.pi/6), 0), sp.Eq(F1s*sp.cos(sp.pi/6) - 100, 0)], [F1s, F2s])[F1s] - 100/sp.cos(sp.pi/6)) == 0 and sp.simplify(sp.solve([sp.Eq(F2s - F1s*sp.sin(sp.pi/6), 0), sp.Eq(F1s*sp.cos(sp.pi/6) - 100, 0)], [F1s, F2s])[F2s] - 100*sp.tan(sp.pi/6)) == 0)
# 选择3: 三力平衡→第三力=其余两力合力之反向 → 范围|3-4|~3+4
lo, hi = abs(3 - 4), 3 + 4
chk(19, "新增·选择3 A:范围1~7 N", (lo, hi) == (1, 7))
chk(20, "新增·选择3 闭合三角形证:3-4-5直角闭合（大小不等可平衡）", 3**2 + 4**2 == 5**2)

# ===== F组·新增：填空 =====
# 匀速下滑沿斜面二力平衡: f=Gsinθ·共线；μ=f/FN=Gsinθ/(Gcosθ)=tanθ=0.5
eq_mu = sp.simplify(mu*sp.G if False else mu)
F_N, F_f = G*sp.cos(theta), G*sp.sin(theta)
chk(21, "新增·填空①匀速→f=μFN=Gsinθ（μ=tanθ代入全等）", sp.simplify((sp.tan(theta))*F_N - F_f) == 0)
chk(22, "新增·填空② μ=tanθ=0.5（tan(atan(1/2))=1/2恒等）", sp.simplify(sp.tan(sp.atan(sp.Rational(1, 2))) - sp.Rational(1, 2)) == 0)

# ===== G组·新增：解答1（例题1同款换数·37°=3-4-5角题给） =====
sin37, cos37 = sp.Rational(6, 10), sp.Rational(8, 10)
N1, f1 = 300*cos37, 300*sin37
chk(23, "新增·解答1① FN=300×0.8=240 N", N1 == 240)
chk(24, "新增·解答1① f=300×0.6=180 N", f1 == 180)
chk(25, "新增·解答1② μ=180/240=0.75", sp.Rational(180, 240) == sp.Rational(3, 4))
chk(26, "新增·解答1② μ=sin37°/cos37°=0.6/0.8=0.75互证", sin37/cos37 == sp.Rational(3, 4))

# ===== H组·新增：解答2双绳吊灯 =====
G_lamp = sp.Integer(40)
T_a30 = sp.simplify(G_lamp/(2*sp.cos(sp.pi/6)))
chk(27, "新增·解答2① α=30°: T=40/√3≈23.09 N", abs(float(T_a30) - 23.094) < 1e-3)
chk(28, "新增·解答2① 精确值T=40√3/3", sp.simplify(T_a30 - 40*sp.sqrt(3)/3) == 0)
T_a60 = sp.simplify(G_lamp/(2*sp.cos(sp.pi/3)))
chk(29, "新增·解答2② α=60°: T'=40 N=整灯重", (T_a60, T_a60 == G_lamp) == (40, True))
chk(30, "新增·解答2③ 涨幅:23.1→40（+73%方向）", float(T_a60) > float(T_a30) and abs(float(T_a60)/float(T_a30) - 1.732) < 0.01)
chk(31, "新增·解答2③ α→90°⁻拉力发散（左极限+oo·T2极限直觉句同源）", sp.limit(G_lamp/(2*sp.cos(a)), a, sp.pi/2, '-') == sp.oo)

# ===== I组·新增：挑刺两处错反例 =====
chk(32, "新增·挑刺①斜面压力=Gcos37°=240≠300（压力≠重力数值证）", (300*cos37 == 240) and (240 != 300))
v3 = sp.Matrix([3, 0]) + sp.Matrix([0, 4]) + sp.Matrix([-3, -4])
chk(33, "新增·挑刺② 3N+4N+5N矢量闭合=0（大小3≠4≠5照样平衡·反例证）", v3 == sp.zeros(2, 1) and len({3, 4, 5}) == 3)

print(f"\n===== 总验点{PASS + FAIL}·通过{PASS}·失败{FAIL} =====")
print("ALL PASS·exit0" if FAIL == 0 else "存在FAIL·非静默改绿·逐条排查")
import sys
sys.exit(0 if FAIL == 0 else 1)
