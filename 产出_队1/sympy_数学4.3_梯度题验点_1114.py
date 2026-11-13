# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学4.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学4.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, a, b = sp.symbols('x a b', real=True)

# T1 选择1：log₃(1/9)=−2（C）·log₄8=3/2（B错）·ln1=0（D错）
c1 = sp.log(sp.Rational(1,9), 3); b1 = sp.log(8, 4); d1 = sp.log(1)
check("T1_选择1 C对·B=3/2错·ln1=0", sp.simplify(c1) == -2 and sp.simplify(b1) == sp.Rational(3,2) and sp.simplify(d1) == 0, "逐项核")

# T2 选择2：log₇[log₃(log₂x)]=0 → log₃(log₂x)=1 → log₂x=3 → x=8 → x^(1/3)=2
check("T2_选择2 x=8→x^(1/3)=2（答案A）", sp.log(8, 2) == 3 and sp.Integer(8)**sp.Rational(1,3) == 2, "三层洋葱剥法")

# T3 选择3：log₈27·log₉4=1（答案A）
r3 = sp.log(27, 8) * sp.log(4, 9)
check("T3_选择3 =1（答案A）", sp.simplify(r3) == 1, f"log₂3×log₃2倒数对·{sp.simplify(r3)}")

# T4 填空：lg5=1−lg2=1−a
t4 = sp.simplify(sp.log(5, 10) + sp.log(2, 10))
check("T4_填空 lg5=1−a", sp.simplify(t4) == 1, f"lg2+lg5={t4}")

# T5 挑刺①：log₂(8−1)=log₂7（对数无加减法则）
check("T5_挑刺① log₂7≠3", sp.log(7, 2) != 3 and sp.log(8, 2) == 3, "加减无法则·只有乘除幂")

# T6 挑刺②：lg4+lg9=lg36=2lg6≠lg13
t6 = sp.simplify((sp.log(4, 10) + sp.log(9, 10)) - sp.log(36, 10))
check("T6_挑刺② lg36≠lg13", t6 == 0 and sp.simplify(sp.log(36, 10) - sp.log(13, 10)) != 0, "和法则=lg(ab)")

# T7 解答1：log₂25·log₃4·log₅9=8（链式换底倒数归一）
r7 = sp.log(25, 2) * sp.log(4, 3) * sp.log(9, 5)
check("T7_解答1 =8", sp.simplify(r7) == 8, f"{sp.simplify(r7)}")

# T8 解答2：lg15=1+b−a·lg3.6=2(a+b)−1
lg2, lg3 = sp.Symbol('a'), sp.Symbol('b')
check("T8_解答2 lg15=1+b−a·lg3.6=2(a+b)−1", sp.log(sp.Rational(15,1), 10).evalf(6) - (1 + float(sp.log(3, 10).evalf(6)) - float(sp.log(2, 10).evalf(6))) < 1e-5 and abs(float(sp.log(sp.Rational(36,10), 10).evalf(6)) - (2*(float(sp.log(2,10).evalf(6)) + float(sp.log(3,10).evalf(6))) - 1)) < 1e-5, "数值核两式")

# T9 真题①（2022天津T6）：(2log₄3+log₈3)(log₃2+log₉2)=2（答案B）
r9 = (2*sp.log(3, 4) + sp.log(3, 8)) * (sp.log(2, 3) + sp.log(2, 9))
check("T9_真题① =2（答案B）", sp.simplify(r9) == 2, f"=(4/3)log₂3×(3/2)log₃2·{sp.simplify(r9)}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学4.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
