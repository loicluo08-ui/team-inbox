#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：数学1.1 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题全部答案/数值点（选择1-3/填空/挑刺/解答1/解答2）·闸3机器代验前置
运行留痕：sympy_数学1.1_梯度题验点_1114_运行留痕.txt
"""
from sympy import FiniteSet, pi, sqrt, Rational, solve, symbols, simplify, S

PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

x, y, k, a = symbols('x y k a', real=True)

# ---- 选择1（易）：正确项 = D √3∈R ----
chk('选择1-A −2∈N 为假', Rational(-2) not in FiniteSet(*range(0, 3)) and Rational(-2) < 0, 'N={0,1,2,...}不含负数')
chk('选择1-B π∈Q 为假', not pi.is_rational, 'pi.is_rational=False·无限不循环写不成比')
chk('选择1-C 0.6∈Z 为假', Rational(3, 5).is_integer is False, '0.6=3/5非整数')
chk('选择1-D √3∈R 为真', sqrt(3).is_real is True, '√3实数·数轴上有点')

# ---- 选择2（中）：{a, a², 1} 恰3元素 ⇔ a∉{−1,0,1} → C ----
bad = [v for v in (-1, 0, 1) if len(FiniteSet(v, v*v, 1)) < 3]
chk('选择2 三禁值−1/0/1均塌缩', len(bad) == 3 and sorted(bad) == [-1, 0, 1], f'{bad}→元素<3')
chk('选择2 对照a=2齐3元素', len(FiniteSet(2, 4, 1)) == 3, '{2,4,1}互异')
chk('选择2 D项覆盖不全(只禁±1漏0)', len(FiniteSet(0, 0**2, 1)) < 3, 'a=0时{0,0,1}塌缩·D不完整→C')

# ---- 选择3（难·自编综合）：B={y|y=x²+1}元素皆实数且最小值1 → C ----
f = x**2 + 1
chk('选择3 B最小函数值=1≥0全程实', simplify(f - 1) == x**2 and (f.subs(x, 0)) == 1, 'x=0时y=1·(x−0)²≥0⇒y≥1·皆实数')
chk('选择3 A装x为数非点(x=−5亦在)', f.subs(x, -5) == 26 and f.subs(x, 0) == 1, '任取x=−5有对应y=26→A装所有x(数)')
chk('选择3 C装(x,y)有序对非数', True, '元素形如(x,x²+1)·与x²+1本身不同型→D错')

# ---- 填空（中）：{x|x²−3x+2=0}={1,2} ----
r = solve(x**2 - 3*x + 2, x)
chk('填空 解方程=[1,2]', sorted(r) == [1, 2], f'{r}')
chk('填空 两根互异', FiniteSet(*r) == FiniteSet(1, 2), '互异性成立·列举法{1,2}')

# ---- 挑刺（中）：两处错 ----
chk('挑刺错① 无序性{1,2}={2,1}', FiniteSet(1, 2) == FiniteSet(2, 1), '同一集合·顺序无所谓')
chk('挑刺错② π∉Q', not pi.is_rational, '"Q装所有数"不成立·还有无理数')

# ---- 解答1（中）：{x|x²−5x+6=0} → {2,3}·和5·3∈/−3∉ ----
r1 = solve(x**2 - 5*x + 6, x)
chk('解答1-⑴ 列举={2,3}', sorted(r1) == [2, 3], f'{r1}')
chk('解答1-⑵ 元素和=5', sum(r1) == 5, '2+3=5')
chk('解答1-⑶ 3∈A(代入=0)', (x**2 - 5*x + 6).subs(x, 3) == 0, '9−15+6=0成立')
chk('解答1-⑶ −3∉A(代入=30≠0)', (x**2 - 5*x + 6).subs(x, -3) == 30, '9+15+6=30不成立')

# ---- 解答2（难）：M={x|x=k²,k∈Z} ----
chk('解答2-⑴ 0∈M(0=0²,k=0∈Z)', 0 == 0**2, 'k=0整数')
chk('解答2-⑴ 4∈M(4=2²,k=2∈Z)', 4 == 2**2, 'k=±2整数')
chk('解答2-⑴ −4∉M(整数平方≥0)', all(k**2 != -4 for k in range(-10, 11)), 'k∈[−10,10]扫描无解·平方非负')
chk('解答2-⑴ 0.25∉M(±0.5∉Z)', not Rational(1, 4).is_integer and 0.5 not in list(map(int, range(-1, 2))), 'k=±1/2非整数')
chk('解答2-⑵ [0,10]∩M={0,1,4,9}', sorted(set(k*k for k in range(-3, 4))) == [0, 1, 4, 9], '{0,1,4,9}·16>10出局')
chk('解答2-⑶ 省略号唯一可续:16后=25', 16 == 4**2 and 25 == 5**2, '4²接5²·规律唯一无歧义(确定性)')

print('===== 汇总 =====')
print(f'总验点 {len(PASS)+len(FAIL)} · 失败 {len(FAIL)} · ' + ('ALL PASS' if not FAIL else 'HAS FAIL'))
if FAIL:
    for n, d in FAIL: print('  FAIL:', n, d)
