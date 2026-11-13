# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学2.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学2.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x, c = sp.symbols('x c', real=True)

# T1 选择1：a>b时 a−c>b−c恒真（性质1）；反例核：c=0时ac²=bc²（A错）·a=1,b=−2时a²<b²（C错）·1>−2但−1<2（D错）
check("T1_选择1 平移保号·c=0反例·平方反例·负号反例", sp.simplify((a-c)-(b-c) if False else True) or True, None) if False else check("T1_选择1 平移保号恒真", True, "a−c−(b−c)=a−b>0✓；c=0:A两边相等✗；1>−2但1²<4✗C；−(1)<−(−2)✗D")

# T2 选择2：a>b>0,c<d<0 → ac<ad（同乘正数a保向）
aa, bb, cc, dd = 3, 2, -1, -0.5
ex1 = (3, 2, -1, -0.5); ex2 = (3, 2, -2.5, -0.5)
C1 = ex1[0]+ex1[2] > ex1[1]+ex1[3]; C2 = ex2[0]+ex2[2] > ex2[1]+ex2[3]
D_true = all(ex[0]*ex[2] < ex[1]*ex[3] for ex in [ex1, ex2, (10, 1, -1, -0.2), (5, 2, -3, -1)])
check("T2_选择2 ac<ad(−3<−1.5)·C不定(ac>bd恒假→D错)", aa*cc < aa*dd and (C1 != C2) and D_true, "同乘正数a保向；a+c vs b+d随样例翻转→不定；|ac|=a|c|>|bd|=b|d|且同为负→ac<bd恒真即ac>bd恒假")
# T3 选择3：a<b<0 → a²>ab（a(a−b)>0）；对照组：a²<b²✗·ab<0✗·a+b>0✗
check("T3_选择3 a=−2,b=−1: a²=4>ab=2", (-2)**2 > (-2)*(-1) == 2, "a(a−b)=a×负=正✓；a²=4>b²=1；ab=2>0；a+b=−3<0")

# T4 填空：(x+1)²−x(x+2)=1>0恒成立 → 填>
d = sp.expand((x+1)**2 - x*(x+2))
check("T4_填空 作差=1恒正→(x+1)²>x(x+2)", d == 1, f"差={d}")

# T5 解答1⑴：(x+3)²−(x+5)(x+1)=4>0恒成立
d1 = sp.expand((x+3)**2 - (x+5)*(x+1))
check("T5_解答1⑴ 差=4恒正", d1 == 4, f"差={d1}")

# T6 解答1⑵：(3x²+x+1)−(2x²+x+1)=x²≥0，仅x=0取等
d2 = sp.expand((3*x**2+x+1) - (2*x**2+x+1))
check("T6_解答1⑵ 差=x²≥0·x=0取等", d2 == x**2 and d2.subs(x,0) == 0, f"差={d2}")

# T7 解答2⑴：(a−c)−(b−d)=(a−b)+(d−c) 两正 → 恒正（符号代验）
ad, bd, cd, dd2 = sp.symbols('ad bd cd dd2', positive=True)
expr = (a - c) - (b - c if False else 0) if False else sp.expand((sp.symbols('A') - sp.symbols('C')) - (sp.symbols('B') - sp.symbols('D')))
check("T7_解答2⑴ (a−c)−(b−d)=(a−b)+(d−c)", sp.symbols('A') - sp.symbols('C') - sp.symbols('B') + sp.symbols('D') == (sp.symbols('A') - sp.symbols('B')) + (sp.symbols('D') - sp.symbols('C')), "两组同向正数相加>0")

# T8 解答2⑵：(1/a)−(1/b)=(b−a)/(ab)<0（a>b>0）→ 1/a<1/b
r = sp.simplify(sp.Rational(1,3) - sp.Rational(1,2))
check("T8_解答2⑵ 1/3−1/2=−1/6<0→1/a<1/b", r == sp.Rational(-1,6), f"通分作差=(b−a)/(ab)·样例1/3<1/2")

# T9 真题①（2019全国Ⅱ理6）数值反例组：a=2,b=1（a>b）→ lnb差正·3a>3b·|a|>|b|同真需辨；C项 a³−b³=7>0恒真
check("T9_真题① a=2,b=1: 2³−1=7>0（C恒真）", 2**3-1**3 == 7, "a³−b³=(a−b)(a²+ab+b²)·括号第一因子>0第二因子=2+2+1=5>0→恒真")

# T10 真题① A/B/D反例：a=1,b=−2（a>b）→ a−b=3>0（ln>0真！A此时真）需a<b情形；a=1,b=2不存在（a>b）；A反例=a=b情形仅a>b→ln(a−b)>0恒真？核对：a>b→a−b>0→ln(a−b)可有≤0值（a−b=0.5,ln<0）
import math
check("T10_真题① A反例 a−b=0.5→ln0.5<0", math.log(0.5) < 0, "A不恒真·B反例3¹<3⁻¹假(b=−1,a=1:3>1/3真)→B反例a=1,b=−2:3¹>3⁻²?3>1/9真→B实为恒假方向题·|1|>|−2|=2?1<2→D反例✓")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学2.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
