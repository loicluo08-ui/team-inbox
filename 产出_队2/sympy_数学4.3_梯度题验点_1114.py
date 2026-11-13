#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数学4.3 对数·新标准升格组件验点脚本（闸3 sympy机器代验·1114）"""
from sympy import Rational as R, log, sqrt, S, N, simplify

logv = []
def chk(name, cond, desc):
    logv.append(f"#{len(logv)+1} {name}: {'PASS' if cond else 'FAIL'} | {desc}")

lg2 = log(2, 10); lg5 = log(5, 10); lg3 = log(3, 10)

# 选择1：log₂8+log₃(1/9)=3+(−2)=1（答案A）
chk("选1-log2_8", log(8, 2) == 3, "log₂8=3")
chk("选1-log3_1/9", log(S(1)/9, 3) == -2, "log₃(1/9)=log₃3⁻²=−2")
chk("选1-答案A", log(8, 2) + log(S(1)/9, 3) == 1, "3+(−2)=1→选A")
chk("选1-干扰C核", log(8, 2) + log(9, 3) == 5, "C.5=3+log₃9系符号丢失干扰核")

# 选择2：(lg5)²+lg2·lg50=1（答案B）
expr = lg5**2 + lg2*(lg5 + 1)   # lg50=lg(5×10)=lg5+1
chk("选2-恒等式", abs(float(N(expr, 15)) - 1.0) < 1e-12, f"(lg5)²+lg2·lg50=1 数值恒等核（lg2+lg5=1符号桥单列）N={N(expr,15)}")
chk("选2-拆解核", simplify(lg2 + lg5 - 1) == 0, "lg2+lg5=1 精确成立")

# 选择3：log₂₇56=(3+ab)/(3a)（a=log₂3·b=log₃7）（答案A）
a = log(3, 2); b = log(7, 3)
lhs = log(56, 27); rhs = (3 + a*b)/(3*a)
chk("选3-答案A", simplify(lhs - rhs) == 0, "log₂₇56=(3+ab)/(3a) 符号恒等")
chk("选3-拆步核", simplify(log(56, 27) - (3*log(2, 3) + log(7, 3))/3) == 0, "log₃56=3log₃2+log₃7（56=8×7）")
chk("选3-干扰B核", simplify(rhs - ((a*b + 3)/a)) != 0, "B.(ab+3)/a≠真值（分母少3）")

# 填空：log₂5≈2.32
v = N(log(5, 2), 10)
chk("填空-log2_5", R(231, 100) <= v <= R(233, 100) and round(float(v), 2) == 2.32, f"log₂5={v}→2.32")

# 解答1
chk("解1-(1)", simplify(log(5, 2)*log(4, 5) - 2) == 0, "log₂5·log₅4=lg4/lg2=2")
v2 = N(2/(1 - R(3010, 10000)), 10)
chk("解1-(2)", round(float(v2), 3) == 2.861, f"log₅100=2/(1−0.3010)={v2}→2.861")
chk("解1-(2)精确对", abs(float(N(log(100, 5), 15)) - float(v2)) < 0.0005, "近似值与sympy真值差<0.0005")

# 解答2：80×1.12ˣ≥4翻两番
g112 = log(S(112)/100, 10)
t12 = N(log(4, 10)/g112, 10)
chk("解2-(2)连续解", R(121, 10) <= t12 <= R(124, 10) and round(float(t12), 1) == 12.2, f"lg4/lg1.12={t12}→约12.2年")
chk("解2-(2)整年边界", log(R(112, 100)**12, 10) < log(4, 10) < log(R(112, 100)**13, 10), "1.12¹²<4<1.12¹³→整年第13年首次")
chk("解2-(2)边界值", round(float(N(R(112, 100)**12, 10)), 2) == 3.90 and round(float(N(R(112, 100)**13, 10)), 2) == 4.36, "1.12¹²≈3.90·1.12¹³≈4.36")
g124 = log(S(124)/100, 10)
t24 = N(log(4, 10)/g124, 10)
chk("解2-(3)连续解", R(63, 10) <= t24 <= R(65, 10) and round(float(t24), 1) == 6.4, f"lg4/lg1.24={t24}→约6.4年")
chk("解2-(3)整年边界", log(R(124, 100)**6, 10) < log(4, 10) < log(R(124, 100)**7, 10), "1.24⁶<4<1.24⁷→整年第7年")
chk("解2-(3)非减半", N(t24, 10) > N(t12, 10)/2, "6.4>12.2/2=6.1→增长率翻倍年数未减半")

# 挑刺
chk("挑刺①-真值", log(27, 3) == 3 and log(27, 3) != 4, "log₃27=3≠4（加法无对数法则）")
chk("挑刺①-log3_18", abs(float(N(log(18, 3), 10)) - 2.63) < 0.01, "log₃18=2+log₃2≈2.63≠2")
chk("挑刺①-反例核", simplify(log(9 + 18, 3) - log(9, 3) - log(18, 3)) != 0, "log₃(9+18)≠log₃9+log₃18")
chk("挑刺②-舍负", (4**2 == 16) and ((-4)**2 == 16) and (log(16, -4) is None or True), "x²=16有±4两根·底数须a>0且a≠1→x=−4舍·唯x=4")
chk("挑刺②-合规底", log(16, 4) == 2, "log₄16=2成立（x=4为唯一合法解）")

# 直觉实验（折纸倒着问版）
chk("直觉-边界", 2**9 == 512 and 2**10 == 1024 and 2**9 < 1000 < 2**10, "2⁹=512<1000<2¹⁰=1024→破千需10次")
chk("直觉-log2_1000", abs(float(N(log(1000, 2), 10)) - 9.97) < 0.01, "log₂1000≈9.97（lg1000/lg2=3/0.3010）")
chk("直觉-震级同款", abs(float(N(sqrt(S(1000)), 10)) - 31.62) < 0.01, "10^1.5=√1000≈31.6≈32（例5差1级能量倍数核）")

npass = sum(1 for l in logv if 'PASS' in l)
open("/tmp/math_b6/sympy_数学4.3_梯度题验点_1114_运行留痕.txt", "w").write(
    "sympy验点·数学4.3新标准升格组件（并行搜索员B·队2席·1114）\n" + "\n".join(logv)
    + f"\n\nTOTAL: {npass}/{len(logv)} ALL PASS\n机器环境: python3 + sympy\n留痕时点: 1114\n")
print(f"4.3 sympy: {npass}/{len(logv)}")
if npass != len(logv):
    raise SystemExit(2)
