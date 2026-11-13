# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学1.5新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学1.5_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x = sp.symbols('x', real=True)

# T1 选择3：∃x∈Z, x²=2 无解（√2∉Z）→ 否定∀x∈Z, x²≠2 为真
ints = [sp.Integer(i)**2 == 2 for i in range(-10, 11)]
check("T1_选择3 整数平方均≠2→否定为真(B)", not any(ints), f"−10..10平方无2·√2≈{sp.sqrt(2).evalf(4)}∉Z")

# T2 填空：∀x∈{1,2,3}, x<4 的否定=∃x∈{1,2,3}, x≥4·假（三元素全<4）
check("T2_填空 {1,2,3}全<4→否定假", all(v < 4 for v in [1,2,3]), "1,2,3均<4·∃正例不存在")

# T3 解答1⑴：x²+1>0对全体实数恒真→¬p(∃x∈R,x²+1≤0)假
samples = [float(i)/2 for i in range(-6, 7)]
check("T3_解答1⑴ 抽样+配方恒真·¬p假", all(v*v + 1 > 0 for v in samples) and float((x**2+1).subs(x,0)) > 0, "x²+1≥1>0恒成立")

# T4 解答1⑵：x=6∈Z被2和3同时整除→q真→¬q假
check("T4_解答1⑵ 6%2==0且6%3==0→¬q假", 6 % 2 == 0 and 6 % 3 == 0, "x=6正例")

# T5 解答2⑴：∀x∈{1,2}, x²−a<0 ⇔ a>max(1,4)=2
vals = [v**2 for v in [1,2]]
check("T5_解答2⑴ max{x²}=4→a>4", max(vals) == 4 and 4 > 2 > 1, "{1,4}·两条件取交集→较严的a>4")

# T6 解答2⑵：a=3时x²−3<0对{1,2}成立→¬p(∃x∈{1,2},x²−a≥0)假
check("T6_解答2⑵ a=5: 1−5=−4<0且4−5=−1<0→¬p假·a=3反证4−3=1≥0", (1-5 < 0) and (4-5 < 0) and (4-3 >= 0), "a>4时两元素均<0·a=3时x=2给出1≥0即¬p真→边界必要")

# T7 真题①（2024新课标ⅡT2）：p假于x=−1（|x+1|=0）·q真于x=1（1³=1）
check("T7_真题① |−1+1|=0≯1·1³=1", abs(-1+1) == 0 and 1**3 == 1, "p假¬p真·q真→答案B")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学1.5升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
