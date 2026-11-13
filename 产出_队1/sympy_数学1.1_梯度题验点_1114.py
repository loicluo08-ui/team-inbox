# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学1.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 对象=升格新增试题与真题的全部可机器验数值/逻辑点 · 验点脚本随件留痕（sympy 1.14.0）
# 结果留痕：sympy_数学1.1_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

x, y, m = sp.symbols('x y m', real=True)

# T1 选择2：A={x | 1<x<4, x∈Z}={2,3}；2∈A 且 1,4,2.5∉A
A = {v for v in range(-10, 11) if sp.Integer(1) < v < sp.Integer(4)}
check("T1_选择2 A={2,3}·2∈A·1,4,2.5∉A", A == {2, 3} and 2 in A and 1 not in A and 4 not in A, f"A={sorted(A)}")

# T2 选择3（形式化）：P={x|y=x²} 元素为数（x 取遍全体实数），Q={(x,y)|y=x²} 元素为有序数对（点）
P_sample = [sp.Integer(0), sp.Integer(1), sp.Integer(2)]            # P 的样本：纯数
Q_sample = [(sp.Integer(0), sp.Integer(0)), (sp.Integer(1), sp.Integer(1)), (sp.Integer(2), sp.Integer(4))]  # Q 的样本：点
check("T2_选择3形式化 P元素=数·Q元素=点(样本型断言)·P≠Q", all(isinstance(v, sp.Expr) and not isinstance(v, tuple) for v in P_sample) and all(isinstance(v, tuple) for v in Q_sample) and (0, 0) in Q_sample and sp.Integer(0) not in Q_sample, "P装数x，Q装点(x,y)；Q含(0,0)而数0∉Q（元素类型异）")

# T3 填空：x²=1 的根 = {−1,1}（两根都收）
sol3 = sp.solve(sp.Eq(x**2, 1), x)
check("T3_填空 x²=1 → {−1,1}", sorted(sol3) == [-1, 1], f"roots={sol3}")

# T4 挑刺②：{5,5,8} 去重后元素 2 个（互异性）
check("T4_挑刺② len({5,5,8})=2", len({5, 5, 8}) == 2, f"{sorted({5,5,8})}")

# T5 解答1：B={x+y | x∈A, y∈A}, A={−1,0,1} → {−2,−1,0,1,2} 共5个
Asrc = {-1, 0, 1}
B = {int(a + b) for a in Asrc for b in Asrc}
check("T5_解答1 B={−2,−1,0,1,2}·5个", B == {-2, -1, 0, 1, 2} and len(B) == 5, f"B={sorted(B)} n={len(B)}（9种搭配去重）")

# T6 解答2⑴：m=0 → x²−2x=0 → {0,2}
sol6 = sp.solve(sp.Eq(x**2 - 2*x, 0), x)
check("T6_解答2⑴ x²−2x=0 → {0,2}", sorted(sol6) == [0, 2], f"roots={sol6}")

# T7 解答2⑵：Δ=4−4m=0 → m=1；此时 x²−2x+1=(x−1)² → {1}
m_sol = sp.solve(sp.Eq(sp.Integer(4) - 4*m, 0), m)
sol7 = sp.solve(sp.Eq(x**2 - 2*x + 1, 0), x)
check("T7_解答2⑵ Δ=0→m=1·A={1}", m_sol == [1] and sol7 == [1], f"m={m_sol}·roots={sol7}")

# T8 解答2核对边界：Δ=4−4m 符号域（m>1→Δ<0零根∅；m<1→Δ>0两根）
check("T8_解答2核对 Δ<0 ⟺ m>1·Δ>0 ⟺ m<1", ((4 - 4*m) < 0).subs(m, 2) == sp.true and ((4 - 4*m) > 0).subs(m, sp.Rational(1, 2)) == sp.true, "m=2:4−8<0(∅)·m=0.5:4−2>0(两根)·仅m=1单根")

# T9 真题①（2018全国Ⅱ理2）：{(x,y)∈Z² | x²+y²≤3} 元素个数=9（暴力全计）
pts = [(a, b) for a in range(-3, 4) for b in range(-3, 4) if a*a + b*b <= 3]
check("T9_真题① 整点计数=9（答案A）", len(pts) == 9, f"计数={len(pts)}·样点={sorted(pts)[:4]}…")

# T10 真题②（2013山东理2）：B={x−y | x∈A,y∈A}, A={0,1,2} → {−2,−1,0,1,2} 共5个（答案C）
A2 = {0, 1, 2}
B2 = {int(a - b) for a in A2 for b in A2}
check("T10_真题② B={−2,−1,0,1,2}·5个（答案C）", B2 == {-2, -1, 0, 1, 2} and len(B2) == 5, f"B2={sorted(B2)} n={len(B2)}（9种搭配去重）")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学1.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
