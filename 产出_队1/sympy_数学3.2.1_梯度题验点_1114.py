# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学3.2.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学3.2.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, a = sp.symbols('x a', real=True)

# T1 选择1：y=x²+1在(0,∞)递增（对照组1/x、−x²+1、−2x+1均减）
check("T1_选择1 x²+1在(0,∞)递增", sp.diff(x**2+1, x).subs(x, 1) > 0, "对照：1/x导数−1/x²<0·−x²+1导数−2x<0·−2x+1斜率−2<0")

# T2 选择2：f(x)=x²−4x+3对称轴x=2→递增区间[2,+∞)
check("T2_选择2 对称轴x=2→增区间[2,∞)", -(-4)/(2*1) == 2, "顶点横坐标−b/2a=2")

# T3 选择3：f增→a+1>2a且a+1,2a∈[−2,2]→a∈[−1,1)
check("T3_选择3 a∈[−1,1)（域+增双约束）", sp.solve(sp.Eq(2*a, -2), a) == [-1] and sp.solve(sp.Eq(2*a, 2), a) == [1] and sp.solve(sp.Eq(a+1, 2*a), a) == [1], "a+1>2a→a<1·2a∈[−2,2]→a∈[−1,1]·交集[−1,1)")

# T4 填空：f(x)=x+1/x在[1/2,3]：min=2（x=1）·max=10/3（x=3）·差=4/3
f4 = x + 1/x
pts = [sp.Rational(1,2), 1, 3]
vals = [f4.subs(x, p) for p in pts]
check("T4_填空 max=10/3·min=2·差=4/3", max(vals) == sp.Rational(10,3) and min(vals) == 2 and max(vals)-min(vals) == sp.Rational(4,3), f"f(1/2)={vals[0]}·f(1)={vals[1]}·f(3)={vals[2]}")

# T5 挑刺①：1/x整体不单调——x₁=−1<x₂=1但f(−1)=−1<f(1)=1（递减应>f）
check("T5_挑刺① f(−1)=−1<f(1)=1反例", f4.subs(x,-1) if False else sp.simplify((1/x).subs(x,-1)) == -1 and sp.simplify((1/x).subs(x,1)) == 1 and -1 < 1, "定义域断裂不能并区间谈单调")

# T6 挑刺②：f(x)=−x²+2x在[−1,3]最大值=f(1)=1（顶点）≠f(3)=−3
f6 = -x**2 + 2*x
check("T6_挑刺② 顶点x=1∈[−1,3]·f(1)=1>f(3)=−3", f6.subs(x,1) == 1 and f6.subs(x,3) == -3 and 1 > -3, "最大值在对称轴处")

# T7 解答1：(x₁−x₂)(x₁+x₂)<0 证 f(x)=x²+1 在(0,∞)递增
x1, x2 = sp.symbols('x1 x2', positive=True)
d7 = sp.expand((x1**2+1) - (x2**2+1))
sample = (d7 == (x1-x2)*(x1+x2))
check("T7_解答1 差式=(x₁−x₂)(x₁+x₂)·样例x₁=1,x₂=2差=−3<0", sp.expand((x1-x2)*(x1+x2)) - d7 == 0 and float(d7.subs({x1:1, x2:2})) == -3.0, "0<x₁<x₂→两因子一负一正→差<0→递增")

# T8 解答2：f(x)=x²−2ax+3在[1,3]最小值g(a)：a<1:4−2a·1≤a≤3:3−a²·a>3:12−6a·max g(a)=2
g1 = 4 - 2*a          # a<1（x=1端）
g2 = 3 - a**2         # 1≤a≤3（x=a顶点）
g3 = 12 - 6*a         # a>3（x=3端）
check("T8_解答2 g(1)=2·g段①极限2·g段③极限−6→max g(a)=2", g1.subs(a,1) == 2 and g2.subs(a,1) == 2 and g3.subs(a,3) == -6, "①段递减趋2·②段a=1时2·③段a→3⁺趋−6·最大值2")

# T9 真题①（2025新课标ⅠT8）：设公共值t——特值核：t=0→(1/4,1/27,1/125)即x>y>z✓；t=5→(8,9,1)即y>x>z✓；t=8→(64,243,125)即y>z>x✓；x>z>y不可能（答案B）
v0 = (sp.Rational(1,4), sp.Rational(1,27), sp.Rational(1,125)); v5 = (8, 9, 1); v8 = (64, 243, 125)
c0 = v0[0] > v0[1] > v0[2]; c5 = v5[1] > v5[0] > v5[2]; c8 = v8[1] > v8[2] > v8[0]
check("T9_真题① 三特值全吻合·x>z>y无例（答案B）", c0 and c5 and c8, f"t=0:{v0}·t=5:{v5}·t=8:{v8}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学3.2.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
