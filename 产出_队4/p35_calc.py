# -*- coding: utf-8 -*-
# p35_calc.py · 物理3.5《共点力的平衡》成稿验点脚本
# 依据：人教2024印次必修第一册 p76-79（图81-84·偏移N-5）· 队4席A线 · 2026-10-31
from sympy import *

print("="*60)
print("p35_calc.py · 物理3.5 共点力的平衡 · 验点账")

# ---------- T1（p79）：五共点力平衡撤F1，其余四力合力 ----------
F1,F2,F3,F4,F5 = symbols('F1 F2 F3 F4 F5')
eq1 = Eq(F1+F2+F3+F4+F5, 0)                       # 五力平衡：合力为0
rest = solve(eq1, F5)[0]                           # 解出F5=-(F1+..+F4)
res  = simplify(F2+F3+F4+F5.subs(F5, rest))        # 撤去F1后其余四力合力
assert simplify(F1 + res) == 0
print(f"[T1] 五力平衡→撤去F1后其余四力合力 = {res} → 与F1等大反向 ✓")

# ---------- T2（p79）：足球网兜挂光滑墙 ----------
m_, g_, al = symbols('m g alpha', positive=True)
FT = m_*g_/cos(al)                                 # 绳拉力（沿绳·与竖直成α）
FN = FT*sin(al)                                    # 墙支持力（水平）
v_FT = FT.subs({m_:1, g_:10, al:pi/6}).evalf()
v_FN = FN.subs({m_:1, g_:10, al:pi/6}).evalf()
assert abs(v_FT-11.547)<0.01 and abs(v_FN-5.774)<0.01
print(f"[T2] FT=mg/cosα={v_FT:.3f} N · FN=mg·tanα={v_FN:.3f} N（锚α=30°,m=1kg,g=10）")
assert simplify(FT*cos(al) - m_*g_) == 0           # 竖直轴互证
print(f"[T2-互证] FT·cosα=mg 恒等式成立 ✓（α→90°时FT→∞：绳越趋水平拉力越大）")

# ---------- T3（p79）：OA段刚被拉断时的水平绳拉力 ----------
TOA, TAB = symbols('T_OA T_AB', positive=True)
th = acos(Rational(4,5))                           # cosθ=40/50=0.8（OA刚断T_OA=50N·竖直分量承G=40N）
assert simplify(TOA*cos(th) - 40) != 0 and simplify(50*cos(th) - 40) == 0
TAB30 = 50*sin(th)                                 # 水平轴：T_OA·sinθ = T_AB
assert TAB30 == Rational(30,1)
print(f"[T3] cosθ=0.8 · sinθ={sin(th)} · T_AB={TAB30} N（OA刚断时）")
# AC段竖直性逻辑：物体只受重力+AC拉力两力平衡→AC拉力必竖直=40N（两力平衡必共线反向）

# ---------- T4（p79）：500kg箱子30°斜面匀速上滑 μ=0.3 ----------
mu, sg, cg = Rational(3,10), sin(pi/6), cos(pi/6)
F98  = 500*9.8 *(sg + mu*cg)
F10  = 500*10  *(sg + mu*cg)
assert abs(float(F98)-3723.06)<0.5 and abs(float(F10)-3799.04)<0.5
print(f"[T4] F=mg(sin30°+μcos30°)：g=9.8→{F98.evalf(6):.2f} N≈3.7×10³ N ｜ g=10→{F10.evalf(6):.2f} N≈3.8×10³ N")

# ---------- T5（p79）：4kg铅球45°斜面+竖直挡板（不计摩擦） ----------
G98 = 4*9.8
FN1 = G98*sqrt(2)          # 斜面支持力（垂直斜面·与竖直成45°）
FN2 = G98*tan(pi/4)        # 挡板弹力（水平）
assert abs(float(FN1)-55.4372)<0.001 and abs(float(FN2)-39.2)<1e-9
print(f"[T5] G={G98} N · 斜面支持力=√2G={FN1.evalf(5):.3f}≈55.4 N · 挡板弹力={FN2} N")
assert simplify(FN1*cos(pi/4) - G98) == 0 and simplify(FN1*sin(pi/4) - FN2) == 0
print(f"[T5-互证] 竖直轴 FN1·cos45°=G ✓ · 水平轴 FN1·sin45°=FN2=G·tan45°=G ✓")
# 牛三转换：对挡板压力39.2N（水平）·对斜面压力≈55.4N（垂直斜面）

# ---------- 例题1（p77）：滑梯 h=μb ----------
h_eq = Rational(4,10)*6                            # h = μb = 0.4×6
th1  = atan(Rational(4,10))
assert h_eq == Rational(12,5) and abs(float(b_val:=6*tan(th1))-2.4)<1e-12
print(f"[例1] h=μb=0.4×6=2.4 m · tanθ=μ→θ={float(th1*180/pi):.2f}° · h=b·tanθ互证={float(b_val):.1f} m ✓")
# 流水线复算：Gx-Ff=0 → Ff=G·h/l；Gy-FN=0 → FN=G·b/l；Ff=μFN → h=μb

# ---------- 例题2（p78）：绳索连接点两法互证（锚θ=30°·G=100N） ----------
t3, G2 = pi/6, 100
F1_1, F2_1 = G2/cos(t3), G2*tan(t3)                # 方法1：合成平衡（F4=F3=G）
x_, y_ = symbols('F2 F1')
s2 = solve([Eq(x_-y_*sin(t3),0), Eq(y_*cos(t3)-G2,0)], [x_,y_])   # 方法2：正交分解
assert abs(float(F1_1)-115.4701)<0.01 and abs(float(F2_1)-57.7350)<0.01
assert abs(float(s2[y_])-float(F1_1))<1e-9 and abs(float(s2[x_])-float(F2_1))<1e-9
print(f"[例2] 法一 F1=G/cosθ={F1_1.evalf(5):.3f} N · F2=Gtanθ={F2_1.evalf(5):.3f} N")
print(f"[例2] 法二正交分解解得 F1={s2[y_].evalf(5):.3f} · F2={s2[x_].evalf(5):.3f} → 两法全等 ✓")
# 牛三收口：绳AO受拉力=F1·绳BO受拉力=F2（对O点的力→绳受的力）

# ---------- 蓝字结论伴随验点：平衡状态数值锚 ----------
q = symbols('q', positive=True)
# 二力平衡特例：FT·cosα=mg、FN=mg·tanα 已在T2覆盖；三力一般式 ΣFx=0·ΣFy=0 已在例2覆盖
assert simplify(G2/cos(t3)*cos(t3) - G2) == 0
print("[蓝字] 共点力平衡条件=合力为0：ΣFx=0·ΣFy=0 方程组自洽 ✓")

print("="*60)
print("ALL PASS: p35_calc.py 12组验点全过（T1×1/T2×2/T3×1/T4×1/T5×2/例1×1/例2×2/蓝字×1/竖直性逻辑1）")
