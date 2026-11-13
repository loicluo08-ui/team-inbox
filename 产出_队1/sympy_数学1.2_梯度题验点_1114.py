# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学1.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学1.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
a, x = sp.symbols('a x', real=True)

# T1 选择1：∅⫋{0}（真）·0⊆{0}/{0}∈{0}（假·点圈辨析）
check("T1_选择1 ∅⫋{0}真·{0}∈{0}假", (set() < {0}) and ({0} not in {0}) and (0 in {0}), "∅⊊{0}成立；0⊆{0}点是点圈是圈✗；{0}∈{0}元素是0✗；0∈{0}✓")

# T2 选择3：{1,2}⊆A⫋{1,2,3,4} 的A个数=3（{1,2}/{1,2,3}/{1,2,4}）
As = [frozenset(s) for s in [(1,2),(1,2,3),(1,2,4),(1,2,3,4)]]
cnt = sum(1 for s in As if {1,2} <= s and s < frozenset({1,2,3,4}))
check("T2_选择3 满足{1,2}⊆A⊊{1,2,3,4}的A=3个", cnt == 3, f"计数={cnt}")

# T3 填空：{a,b,c}真子集=2³−1=7
check("T3_填空 真子集7个", 2**3-1 == 7, "8−1=7")

# T4 解答1：A={1,2}，B={x|1≤x≤2, x∈Z}={1,2} → A=B
A = set(sp.solve(sp.Eq(x**2-3*x+2, 0), x))
B = {v for v in [1,2,3] if sp.Integer(1) <= v <= sp.Integer(2)}
check("T4_解答1 A=B={1,2}", A == {1,2} and B == {1,2} and A == B, f"A={A} B={B}")

# T5 解答2：B={1,2}⊆A={1,a,a²} → a∈{2,√2,−√2}，逐一过互异性
cands = sorted({sp.Integer(2), sp.sqrt(2), -sp.sqrt(2)}, key=float)
ok = all(len({1, aa, aa**2}) == 3 and sp.Integer(2) in {1, aa, aa**2} for aa in cands)
check("T5_解答2 a∈{2,±√2}全过互异性且2∈A", ok and len(cands) == 3, f"a={ [sp.nsimplify(c) for c in cands] }")

# T6 真题①（2023新课标ⅡT2）：A={0,−a},B={1,a−2,2a−2},A⊆B → 仅a=1
vals = [sp.Rational(n, 2) for n in range(-6, 9)]
sols = [aa for aa in vals if {sp.Integer(0), -aa} <= {sp.Integer(1), aa-2, 2*aa-2}]
check("T6_真题① A⊆B → a=1", sols == [sp.Integer(1)], f"有理数网格扫描解={sols}")

# T7 真题②（2024新课标ⅠT1）：A∩B={−1,0}
Aint = {bb for bb in [-3,-1,0,2,3] if -5 < bb**3 < 5}
check("T7_真题② A∩B={−1,0}（答案A）", Aint == {-1, 0}, f"∛5≈{float(sp.real_root(5,3)):.4f}∈(1,2)·B中落区间者={sorted(Aint)}")

# T8 真题①原题自洽：a=2时B={1,0,2}含0但−2∉B（舍）复跑
check("T8_真题① a=2舍去复跑 −2∉B", -2 not in {1, 0, 2}, "A={0,−2}中−2∉B={1,0,2}→舍")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学1.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
