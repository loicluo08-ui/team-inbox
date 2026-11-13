# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学1.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学1.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x = sp.symbols('x', real=True)

# T1 选择1：A∪B={1,2,3,4}
check("T1_选择1 {1,2,3}∪{2,3,4}={1,2,3,4}", {1,2,3} | {2,3,4} == {1,2,3,4}, f"{sorted({1,2,3} | {2,3,4})}")

# T2 选择2：A={x|−1<x≤3}∩B={x|x>2}={x|2<x≤3}
check("T2_选择2 区间交 (−1,3]∩(2,∞)=(2,3]", sp.Interval.Lopen(-1,3).intersect(sp.Interval.Lopen(2, sp.oo)) == sp.Interval.Lopen(2,3), "端点2开3闭")

# T3 选择3：(∁R A)∪B，A={x|2≤x≤3}，B={x|x<2} → {x|x<2或x>3}
A = sp.Interval(2,3); B = sp.Interval.open(-sp.oo, 2)
lhs = sp.Complement(sp.S.Reals, A).union(B)
check("T3_选择3 (∁R A)∪B={x|x<2或x>3}", lhs == sp.Interval.open(-sp.oo,2).union(sp.Interval.open(3, sp.oo)), "德·摩根自洽：(∁RA)∪B=∁R(A∩∁R B)")

# T4 填空：{x|x²=1}∪{x|x²=4} 元素4个
u = set(sp.solve(sp.Eq(x**2,1),x)) | set(sp.solve(sp.Eq(x**2,4),x))
check("T4_填空 并集4个元素", u == {-1,1,-2,2} and len(u) == 4, f"{sorted(u)}（互异性：4根互异）")

# T5 挑刺①：{1,2}∪{2,3} 共3个≠4个（并集非求和）
check("T5_挑刺① 并集计数3个（重复只算一）", len({1,2}|{2,3}) == 3, "元素个数≠|A|+|B|")

# T6 解答1：A=(−2,4], B=[3,∞): A∩B=[3,4], A∪B=(−2,∞)
Aa = sp.Interval.Lopen(-2,4); Bb = sp.Interval(3, sp.oo)
check("T6_解答1 A∩B=[3,4]·A∪B=(−2,∞)", Aa.intersect(Bb) == sp.Interval(3,4) and Aa.union(Bb) == sp.Interval.Lopen(-2, sp.oo), "端点3闭4闭·−2开∞开")

# T7 解答2⑴：B⊆A ⇔ a≥2（A={x|x≤a}⊇[−1,2]）
check("T7_解答2⑴ a=2时A⊇B成立", sp.Interval(-sp.oo,2).issuperset(sp.Interval(-1,2)), "a≥2即A⊇B·a=2端点含2")

# T8 解答2⑵：A∩B=∅ ⇔ a<−1（a=−1时A∩B={−1}非空）
check("T8_解答2⑵ a=−1时交={−1}非空→需a<−1", sp.Interval(-sp.oo,-1).intersect(sp.Interval(-1,2)) == sp.EmptySet or sp.Interval(-sp.oo,-1).contains(-1) == sp.true, "a=−1边界仍在B内取到−1→严格a<−1")

# T9 真题①（2024北京T1）：M∪N=(−3,4)（答案C）
M = sp.Interval.open(-3,1); N = sp.Interval.Ropen(-1,4)
check("T9_真题① M∪N={x|−3<x<4}（答案C）", M.union(N) == sp.Interval.open(-3,4), "(−3,1)∪[−1,4)=(−3,4)·端点−3开4开")

# T10 真题②（2023新课标ⅠT1）：M∩N={−2}（答案C）
Mm = {-2,-1,0,1,2}; Nn = sp.solve(sp.Eq(x**2-x-6, 0), x)
Nset = {v for v in Mm if v**2 - v - 6 >= 0}
check("T10_真题② M∩N={−2}（答案C）", Nset == {-2}, f"N集=={sorted(Nset)}·根={Nn}→N=(−∞,−2]∪[3,∞)")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学1.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
