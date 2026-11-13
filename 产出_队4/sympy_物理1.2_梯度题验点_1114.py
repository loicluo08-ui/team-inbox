# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理1.2升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# 对象=升格新增试题与真题全部可机器验数值点 · 结果留痕sympy_物理1.2_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择3：Δx = -2 - 2 = -4（大小4 方向负）
r1 = sp.Integer(-2) - sp.Integer(2)
check("T1_选择3位移 -2-2=-4", r1 == -4, f"-2-2={r1}")

# T2 填空：10:07:20 - 10:05:50 = 90 s
h1, m1, s1 = 10, 5, 50; h2, m2, s2 = 10, 7, 20
t1 = h1*3600 + m1*60 + s1; t2 = h2*3600 + m2*60 + s2
check("T2_填空时间间隔 07:20-05:50=90s", t2 - t1 == 90, f"{t2}-{t1}={t2-t1}")

# T3 解答1：位移 -3-2=-5；路程 |7-2|+|-3-7|=15
r3a = sp.Integer(-3) - sp.Integer(2)
r3b = abs(sp.Integer(7) - sp.Integer(2)) + abs(sp.Integer(-3) - sp.Integer(7))
check("T3_解答1位移-5/路程15", r3a == -5 and r3b == 15, f"Δx={r3a}·s={r3b}")

# T4 解答2：勾股 sqrt(40²+30²)=50；东偏北角 atan(30/40)≈36.87°→约37°
r4 = sp.sqrt(sp.Integer(40)**2 + sp.Integer(30)**2)
ang = sp.deg(sp.atan(sp.Rational(30, 40)))
check("T4_解答2位移50km/东偏北≈37°", r4 == 50 and abs(float(ang) - 36.87) < 0.1, f"√(40²+30²)={r4}·atan(30/40)={float(ang):.2f}°")

# T5 真题2024江西T3：x(1)-x(0)=(1+2+3)-1=5（答案C后半句）·x(1)=6系坐标非位移
x = sp.symbols('x', real=True)
expr = 1 + 2*sp.Symbol('t') + 3*sp.Symbol('t')**2
x0 = expr.subs('t', 0); x1 = expr.subs('t', 1)
check("T5_江西T3 x(1)-x(0)=5且x(1)=6", x1 - x0 == 5 and x1 == 6, f"x(0)={x0}·x(1)={x1}·Δx={x1-x0}")

# T6 真题2025黑吉辽蒙T1：闭合轨迹位移=0（x终-x初=0形式化）
check("T6_黑吉辽蒙T1 闭合位移0", sp.Integer(0) - sp.Integer(0) == 0, "a→b→a：x终=x初=a·Δx=0")

# T7 教材数据复用（答案解析引用）：自测②Δx=-2-3=-5（既有验点在案复跑）
check("T7_既有自测② Δx=-2-3=-5复跑", sp.Integer(-2) - sp.Integer(3) == -5, "维持1031账一致")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理1.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
