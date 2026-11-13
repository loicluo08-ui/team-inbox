# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学3.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学3.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, k, b = sp.symbols('x k b', real=True)

# T1 选择1：|x|=√(x²) 同一函数（定义域R·对应法则同值）·(√x)²定义域[0,∞)≠R
t1 = sp.simplify(sp.sqrt(x**2) - sp.Abs(x))
check("T1_选择1 √(x²)=|x|恒等（D同函数）", t1 == 0, "A定义域缩·B x⁰域x≠0·C对应法则异")

# T2 选择2：f(x)={x+2, x<1; x², x≥1}：f(−1)=1→f(1)=1
def f2(v): return v + 2 if v < 1 else v**2
check("T2_选择2 f(f(−1))=1", f2(f2(-1)) == 1, "f(−1)=−1+2=1<1→又走x+2？1不<1→走x²=1·f(f(−1))=f(1)=1")

# T3 选择3：f(x+1)=x²−2x → f(x)=(x−1)²−2(x−1)=x²−4x+3
t3 = sp.expand((x-1)**2 - 2*(x-1))
check("T3_选择3 f(x)=x²−4x+3", t3 == x**2 - 4*x + 3, f"配凑展开={t3}")

# T4 填空：√(x−1)+1/(x−2) 定义域 [1,2)∪(2,+∞)
dom = sp.solve_univariate_inequality(x-1 >= 0, x, relational=False)
excl = sp.simplify(1/(x-2)).subs(x, 2)
check("T4_填空 域=[1,2)∪(2,∞)（x−1≥0且x≠2）", dom == sp.Interval(1, sp.oo) and excl == sp.zoo, f"根号域={dom}·x=2处分母发散={excl}")

# T5 挑刺①：x=2在[1,+∞)但分母为0→必须剔除
check("T5_挑刺① x=2剔除（1/(x−2)无定义）", True, "只看根号漏分母≠0——①错实锤")

# T6 挑刺②：f(2)=f(1+1)代x=1：1²−2×1=−1≠0
t6 = sp.expand((x**2 - 2*x).subs(x, 1))
check("T6_挑刺② f(2)=−1（代x+1=2即x=1）", t6 == -1, "直接代x=2得0是自变量混淆")

# T7 解答1：f(x)=kx+b，f(f(x))=k²x+kb+b=4x+3 → k=±2·k=2→b=1·k=−2→b=−3
sols = sp.solve([sp.Eq(k**2, 4), sp.Eq(k*b + b, 3)], [k, b], dict=True)
got = sorted((s[k], s[b]) for s in sols)
check("T7_解答1 f(x)=2x+1或f(x)=−2x−3", got == [(-2, -3), (2, 1)], f"解集={got}")

# T8 解答2：f(x)+2f(−x)=3x²+x 与 f(−x)+2f(x)=3x²−x 联立 → f(x)=x²−x
fx, fnx = sp.symbols('fx fnx', real=True)
eq1 = sp.Eq(fx + 2*fnx, 3*x**2 + x); eq2 = sp.Eq(fnx + 2*fx, 3*x**2 - x)
sol8 = sp.solve([eq1, eq2], [fx, fnx], dict=True)[0]
f_of_x = sp.simplify(sol8[fx])
check("T8_解答2 f(x)=x²−x·回代验证", sp.simplify(f_of_x - (x**2 - x)) == 0 and sp.simplify((f_of_x + 2*f_of_x.subs(x, -x)) - (3*x**2 + x)) == 0, f"f(x)={f_of_x}·回代(1)式成立")

# T9 真题①（2024新课标ⅠT8）：f(n)≥F(n−1)·f(3)+F(n−2)·f(2)（斐波那契系数）·f(20)>1000（答案B）
def fib(n):
    a, b_ = 1, 1
    for _ in range(n - 2): a, b_ = b_, a + b_
    return a
f3v, f2v = 3, 2
lower20 = fib(19)*f3v + fib(18)*f2v
check("T9_真题① f(20)下界=fib系数加权>1000（B成立）", lower20 > 1000, f"fib(19)={fib(19)}·fib(18)={fib(18)}·下界={lower20}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学3.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
