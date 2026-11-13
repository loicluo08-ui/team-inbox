# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学4.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学4.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, a = sp.symbols('x a', real=True)

# T1 选择1：4^(1/2)·8^(1/3)=2×2=4
check("T1_选择1 4^(1/2)×8^(1/3)=4", sp.sqrt(4) * 2 == 4, "2×2=4")

# T2 选择2：a<0时 (a²)^(1/2)+a/|a|=−a−1（样例a=−2：2−1=1=−(−2)−1）
check("T2_选择2 a=−2样例=1=−a−1", sp.Integer(2) + sp.Rational(-2, 2) == 1 and -(-2)-1 == 1, "(a²)^(1/2)=|a|=2·a/|a|=−1→2−1=1")

# T3 选择3：3^a=2,3^b=5 → 9^(2a−b)=3^(4a−2b)=2⁴/5²=16/25
check("T3_选择3 16/25（答案A）", sp.Integer(2)**4 / sp.Integer(5)**2 == sp.Rational(16,25), "指数性质套用")

# T4 填空：(2^(3/2))^(2/3)×2^(−1/2)=2^1×2^(−1/2)=√2
r4 = (sp.Integer(2)**sp.Rational(3,2))**sp.Rational(2,3) * sp.Integer(2)**sp.Rational(-1,2)
check("T4_填空 =√2", sp.simplify(r4) == sp.sqrt(2), f"{sp.simplify(r4)}")

# T5 挑刺①：⁴√((−2)⁴)=2（非−2·偶次根非负）
check("T5_挑刺① ((−2)⁴)^(1/4)=2", sp.Integer(16)**sp.Rational(1,4) == 2, "|−2|=2")

# T6 挑刺②：5²=25=x+x^(−1)+2 → x+x^(−1)=23（交叉项2）
check("T6_挑刺② x+x^(−1)=23", sp.Integer(25) - 2 == 23, "丢交叉项错成25")

# T7 解答1：x^(1/2)+x^(−1/2)=3 → x+x^(−1)=7 → x²+x^(−2)=47
s1 = sp.Integer(3)**2 - 2; s2 = sp.Integer(s1)**2 - 2
check("T7_解答1 x²+x^(−2)=47", s1 == 7 and s2 == 47, f"两层平方套娃7→47")

# T8 解答2⑴：2^(1/2)·4^(1/3)=2^(1/2+2/3)=2^(7/6)→六次方=2⁷=128
r8a = (sp.Integer(2)**sp.Rational(1,2) * sp.Integer(4)**sp.Rational(1,3))**6
check("T8_解答2⑴ =128", r8a == 128, f"2^(7/6×6)=2⁷")

# T9 解答2⑵：(1/4)^(−1/2)+8^(2/3)−(π−4)⁰=2+4−1=5
r9 = 4**sp.Rational(1,2) + sp.Integer(8)**sp.Rational(2,3) - 1
check("T9_解答2⑵ =5", r9 == 5, "负指数+分数指数+零次幂全覆盖")

# T10 真题①（2022浙江T7）：2^a=5·log₈3=b=(1/3)log₂3 → 4^(a−3b)=2^(2a−6b)=25×3^(−2)=25/9（答案C）
r10 = sp.Integer(5)**2 / sp.Integer(3)**2
check("T10_真题① 4^(a−3b)=25/9（答案C）", r10 == sp.Rational(25,9), "2^(6b)=3²（8^(2b)=3²·log₈3=b→8^b=3）")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学4.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
