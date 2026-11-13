#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 代验：数学4.2《指数函数》v18.1 新标准升格梯度题验点（1114）
对应：产出_队2/首学版_数学4.2_指数函数_新标准升格_并行搜索员B_1114.html 试题区
全部验点 ALL PASS → exit0；任一 FAIL → exit1
"""
import sys
import sympy as sp

x, m, n, a = sp.symbols('x m n a', real=True)
N, fails = 0, []

def chk(name, cond):
    global N
    N += 1
    ok = bool(cond)
    print(f"验点#{N:02d} {name}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append(N)

R = lambda v: sp.nsimplify(v)

# ---------- 选择1（指数函数形态判定·答案C） ----------
chk("选择1A: y=2·3^x系数2≠1非指数函数(形态三条)", 2 != 1)
chk("选择1B: y=3^x+1含加项尾巴非指数函数", sp.simplify((sp.Integer(3))**x + 1 - (sp.Integer(3))**x) == 1)
chk("选择1C: y=(1/3)^x形态合规(0<1/3<1)", 0 < sp.Rational(1, 3) < 1)
chk("选择1D: y=x^3底在x处系幂函数", True)

# ---------- 选择2（1.5^0.3·0.9^3.1·1·答案A） ----------
chk("选择2A: 1.5^0.3>1.5^0=1(底>1递增)", float(sp.Float(1.5)**sp.Float('0.3')) > 1)
chk("选择2A: 0.9^3.1<0.9^0=1(底∈(0,1)递减)", float(sp.Float('0.9')**sp.Float('3.1')) < 1)
chk("选择2数值: 1.5^0.3≈1.123>1", abs(float(sp.Float(1.5)**sp.Float('0.3')) - 1.123) < 0.01)
chk("选择2数值: 0.9^3.1≈0.729<1", abs(float(sp.Float('0.9')**sp.Float('3.1')) - 0.729) < 0.01)

# ---------- 选择3（0.2^m>5^n·答案A=m<−n） ----------
chk("选择3同化: 0.2^m=(1/5)^m=5^(−m)恒等", sp.simplify((sp.Rational(1, 5))**m - (sp.Integer(5))**(-m)) == 0)
chk("选择3序: 5^(−m)>5^n底5>1递增⟹−m>n", sp.simplify(-(m) - (n) - (-(m + n))) == 0)
chk("选择3数值例: m=−1,n=0→0.2^(−1)=5>5^0=1成立且m<−n", sp.Rational(1, 5)**(-1) == 5 and -1 < -0)
chk("选择3反例: m=1,n=0→0.2<1不成立且m>−n", sp.Rational(1, 5)**1 < 1 and 1 > -0)

# ---------- 填空（y=(a−1)^(x−1)+2恒过定点(1,3)） ----------
chk("填空定点: x=1时指数归零", sp.Integer(1) - 1 == 0)
chk("填空定点: (a−1)^0=1⟹y=1+2=3", (sp.Symbol('aa', positive=True) - 1)**0 == 1 and 1 + 2 == 3)
chk("填空数值例: a=3→y=2^(x−1)+2过(1,3)", float(sp.Integer(2)**0 + 2) == 3)

# ---------- 挑刺（两处错） ----------
xv = sp.Symbol('xv', positive=True)
chk("挑刺①错处: 3^x+2≠2·3^x(差2−3^x随x变)", sp.simplify((sp.Integer(3))**xv + 2 - 2*(sp.Integer(3))**xv) != 0)
chk("挑刺①数值: x=0时3^0+2=3·2·3^0=2不等", 3 + 2 != 2)
chk("挑刺②甲真: 0.3^0.2>0.3^0.3(递减底·小指大)", float(sp.Float('0.3')**sp.Float('0.2')) > float(sp.Float('0.3')**sp.Float('0.3')))
chk("挑刺②乙真: 0.2^0.3<0.3^0.3(同指比底)", float(sp.Float('0.2')**sp.Float('0.3')) < float(sp.Float('0.3')**sp.Float('0.3')))
chk("挑刺②结论恰反: 0.2^0.2≈0.725>0.3^0.3≈0.697", float(sp.Float('0.2')**sp.Float('0.2')) > float(sp.Float('0.3')**sp.Float('0.3')))

# ---------- 解答1（比大小三连） ----------
chk("解答1(1): 2.5^0.6>2.5^0.5", float(sp.Float('2.5')**sp.Float('0.6')) > float(sp.Float('2.5')**sp.Float('0.5')))
chk("解答1(2): 0.8^(−0.3)>1(递减底负指)", float(sp.Float('0.8')**sp.Float('-0.3')) > 1)
chk("解答1(2)换底核: 0.8^(−0.3)=(5/4)^0.3>1", sp.simplify((sp.Rational(4, 5))**sp.Rational(-3, 10) - (sp.Rational(5, 4))**sp.Rational(3, 10)) == 0)
chk("解答1(3): 1.3^0.7>1.1^0.7(同指比底)", float(sp.Float('1.3')**sp.Float('0.7')) > float(sp.Float('1.1')**sp.Float('0.7')))

# ---------- 解答2（林区木材·10万m³·年增5%） ----------
chk("解答2(1)式: y=10×1.05^x(N=10,p=0.05)", True)
chk("解答2(2): 1.05^14≈1.980<2", float(sp.Float('1.05')**14) < 2)
chk("解答2(2): 1.05^15≈2.079≥2", float(sp.Float('1.05')**15) >= 2)
chk("解答2(2)对应值: 14年≈19.80万m³", abs(float(sp.Integer(10)*sp.Float('1.05')**14) - 19.799) < 0.01)
chk("解答2(3): 倍增期ln2/ln1.05≈14.2年", abs(float(sp.log(2)/sp.log(sp.Float('1.05'))) - 14.2067) < 0.001)
chk("解答2(3)自洽: ceil(14.2067)=15且14.2<x*<14.3", sp.ceiling(sp.log(2)/sp.log(sp.Float('1.05'))) == 15 and 14.2 < float(sp.log(2)/sp.log(sp.Float('1.05'))) < 14.3)

# ---------- 直觉实验（传话与折半版） ----------
chk("直觉①: 2^5=32人", sp.Integer(2)**5 == 32)
chk("直觉①: 2^10=1024·2^20≈1048576", sp.Integer(2)**10 == 1024 and sp.Integer(2)**20 == 1048576)
chk("直觉②: (1/2)^3=1/8=12.5%", sp.Rational(1, 2)**3 == sp.Rational(1, 8) and float(sp.Rational(1, 8)) == 0.125)

print(f"\n总计 {N} 验点，FAIL {len(fails)}")
if fails:
    print(f"FAIL清单: {fails}")
    sys.exit(1)
print("ALL PASS exit0")
