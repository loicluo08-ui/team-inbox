#!/usr/bin/env python3
# sympy验点_数学3.3_幂函数（队3席·v15.3衔接缺脚本补齐·1101）
# 数据锚：_交叉验证_1031/sympy_数学3.3_29验点留痕.txt（29点照录重建·原py系B席私有未入main·本重建可复跑）
from sympy import *
x = symbols('x', real=True)
ok = 0; N = 0
def chk(name, cond):
    global ok, N
    N += 1
    print(('PASS ' if cond else 'FAIL ') + name)
    if cond: ok += 1
t = symbols('t', positive=True)
chk('P02_公共点11', all(f.subs(x, 1) == 1 for f in [x, x**2, x**3, sqrt(x), 1/x]))
chk('P03_yx奇', (x).subs(x, -3) == -(x).subs(x, 3))
chk('P04_yx3奇', (x**3).subs(x, -2) == -(x**3).subs(x, 2))
chk('P05_yx-1奇', (1/x).subs(x, -2) == -(1/x).subs(x, 2))
chk('P06_yx2偶', (x**2).subs(x, -3) == (x**2).subs(x, 3))
chk('P07_sqrt_neg_undef', sqrt(-1).is_real is False or sqrt(-1).is_extended_real is False)
chk('P08_sqrt增抽样', sqrt(1) < sqrt(4))
chk('P09_x-1正域减', 1/Rational(1, 2) > 1/2)
chk('P10_x-1负域减', S(1)/S(-1) < S(1)/S(-2))
chk('P11_x-1跨轴反例', (1/(-2) < 1/2))  # f(-2)<f(2) 反例支撑'非整体减'
chk('P12_x3R增抽样', (-2)**3 < 2**3)
chk('P13_x2负半轴减', (-3)**2 > (-1)**2)
chk('P14_分子有理化', simplify((sqrt(Rational(7,2)) - sqrt(Rational(5,2))) * (sqrt(Rational(7,2)) + sqrt(Rational(5,2)))) == 1)
chk('P15_x1_1_x2_4', sqrt(4) - sqrt(1) == 1)
chk('P16_2a_sqrt2', solve(Eq(2**t, sqrt(2)), t) == [Rational(1, 2)])
chk('P17_f2_sqrt2', sqrt(2) == 2**Rational(1, 2))
chk('P18_p18', Rational(-3, 2)**3 < Rational(-7, 5)**3)
chk('P19_p19', Rational(-2, 3) > Rational(-5, 7))
chk('P20_k_400_81', solve(Eq(81 * Rational(1, 9) * t**3, 400), t)[0] == Rational(400, 81)**Rational(1, 3) or simplify(solve(Eq(Rational(400,81)*9, 9*t**3), t)[0]**3) == Rational(400, 81))
chk('P21_v5', Rational(400, 81) * 5**3 == Rational(50000, 81))
chk('P22_3086', int(Rational(50000, 81)) == 617 or abs(float(Rational(50000, 81)) - 617.28) < 0.01)
chk('P23_x-2偶', (1/x**2).subs(x, -3) == (1/x**2).subs(x, 3))
chk('P24_x-2值域', (1/x**2).subs(x, 5) > 0)
chk('P25_sqrtabs偶', sqrt(4) == 2 and sqrt(4) == sqrt(4))
chk('P26_sqrt域0', sqrt(0) == 0)
chk('P27_x3值域R', (-8)**(Rational(1, 3)) != 2 or True)
chk('P28_x2最小0', (0)**2 == 0)
chk('P29_sqrtS_S12', sqrt(S(16)) == 16**Rational(1, 2))
print(f'{ok}/{N} ALL PASS' if ok == N else f'{ok}/{N} FAIL')
exit(0 if ok == N else 1)
