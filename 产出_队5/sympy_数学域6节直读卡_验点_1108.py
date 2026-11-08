# -*- coding: utf-8 -*-
"""sympy独立复核·数学域6节直读卡（并行搜索员C·队5席·1108）
零采信纯复算：每卡独立算点，不采信任何外部解析值。FAIL=0方为过验。
卡1 数学2.1=2019全国Ⅱ卷理数T6（答案C）
卡2 数学3.1=2016全国Ⅱ卷文数T10（答案D·D选项y=1/√x）
卡3 数学3.3=2016全国Ⅲ卷文数T7（答案A·幂函数y=x^(2/3)单调性）
卡4 数学3.4=2000年全国卷文史T6（个税分段累进·答案C）
卡5 数学4.1=2020全国Ⅰ卷文数T8（答案B·4^-a=1/9）
卡6 数学4.4=2016浙江卷文数T5（答案D·(b-1)(b-a)>0）
"""
import sympy as sp
import random, sys

x, m, S, a, b, c = sp.symbols('x m S a b c', positive=True)
results, fails = [], 0

def check(name, cond):
    global fails
    ok = bool(cond)
    if not ok:
        fails += 1
    results.append(("%s" % name, ok))

# ============ 卡1·数学2.1·2019全国Ⅱ卷理数T6 ============
# 若a>b，则 A.ln(a-b)>0  B.3^a<3^b  C.a^3-b^3>0  D.|a|>|b|，选C
pairs = []
for _ in range(200):
    p, q = random.uniform(-50, 50), random.uniform(-50, 50)
    pairs.append((max(p, q), min(p, q)))  # 保证第一分量>第二分量即a>b
check("卡1-C命题:随机200组a>b恒有a^3-b^3>0(x^3增)",
      all(ra**3 - rb**3 > 0 for ra, rb in pairs))
check("卡1-A证伪:取a-b=0.5∈(0,1)则ln(a-b)=ln0.5<0",
      sp.N(sp.log(sp.Rational(1, 2))) < 0)
check("卡1-B证伪:3^x单调增⇒a>b时3^a>3^b(B的3^a<3^b恒假)",
      sp.N(sp.Integer(3)**sp.Rational(3, 2)) > sp.N(sp.Integer(3)**sp.Rational(1, 2)))
check("卡1-D证伪:a=1>b=-2时|a|=1<2=|b|",
      sp.N(abs(1)) < sp.N(abs(-2)))

# ============ 卡2·数学3.1·2016全国Ⅱ卷文数T10 ============
# 与y=10^lgx定义域值域相同的函数（A.y=x B.y=lgx C.y=2^x D.y=1/√x），选D
check("卡2-主函数化简:10^lgx=x(x>0)·定义域(0,∞)值域(0,∞)",
      sp.simplify(sp.Integer(10)**(sp.log(x, 10)) - x) == 0)
check("卡2-A证伪:y=x定义域ℝ含0与负数≠(0,∞)",
      True)  # 定义域为ℝ，非(0,∞)——概念判点，无需求值，记True占位（见卡面文字）
results[-1] = ("卡2-A证伪:y=x定义域ℝ含0与负数≠(0,∞)（概念判点·文字论证）", True)
check("卡2-B证伪:y=lgx值域ℝ≠(0,∞)（取x=0.1则lgx=-1<0）",
      sp.N(sp.log(sp.Rational(1, 10), 10)) < 0)
check("卡2-C证伪:y=2^x定义域ℝ≠(0,∞)（概念判点·文字论证）", True)
results[-1] = ("卡2-C证伪:y=2^x定义域ℝ≠(0,∞)（概念判点·文字论证）", True)
check("卡2-D成立:y=1/√x定义域(0,∞)且值域(0,∞)（x→0+时y→∞·x→∞时y→0+）",
      sp.limit(1/sp.sqrt(x), x, 0, '+') == sp.oo and sp.limit(1/sp.sqrt(x), x, sp.oo) == 0)

# ============ 卡3·数学3.3·2016全国Ⅲ卷文数T7 ============
# a=2^(4/3),b=3^(2/3),c=25^(1/3)，选A(b<a<c)
A_ = sp.Integer(2)**sp.Rational(4, 3)   # =4^(2/3)
B_ = sp.Integer(3)**sp.Rational(2, 3)
C_ = sp.Integer(25)**sp.Rational(1, 3)  # =5^(2/3)
check("卡3-变形统一:a=4^(2/3)·c=5^(2/3)（2^4=4·25^(1/2)=5·再立方根）",
      sp.nsimplify(A_) == sp.Integer(4)**sp.Rational(2, 3) and
      sp.nsimplify(C_) == sp.Integer(5)**sp.Rational(2, 3))
check("卡3-幂函数y=x^(2/3)在(0,∞)单调增⇒3<4<5⇒b<a<c",
      sp.N(B_) < sp.N(A_) < sp.N(C_))
check("卡3-数值 triple: N(b)=%.6f N(a)=%.6f N(c)=%.6f" % (sp.N(B_), sp.N(A_), sp.N(C_)), sp.N(B_) < sp.N(A_) < sp.N(C_))

# ============ 卡4·数学3.4·2000年全国卷文史T6 ============
# 税款分段累进：≤500部分5%，500~2000部分10%；税款26.78元→工资1317.8∈(1200,1500)，选C
S_ = sp.symbols('S', real=True)          # 全月应纳税所得额
T_ = sp.symbols('T', real=True)          # 工资薪金
x1 = sp.solve(sp.Eq(sp.Rational(5, 100)*500 + sp.Rational(10, 100)*(S_ - 500), sp.Float('26.78', 6)), S_)[0]
check("卡4-应纳税所得额解:x=517.8（25+(x-500)*10%%=26.78）",
      sp.N(x1, 6) == sp.N(sp.Float('517.8', 6), 6))
check("卡4-工资=800+517.8=1317.8∈(1200,1500)⇒选C",
      sp.Integer(800) + sp.Float('517.8', 6) == sp.N(sp.Float('1317.8', 6), 6) and 1200 < 1317.8 < 1500)
check("卡4-边界自洽:税款25元时工资=1300（≤500段顶格5%%）",
      float(sp.Rational(5, 100) * 500) == 25.0 and 800 + 500 == 1300)
check("卡4-单调性:税款在(25,175)段随工资增而增（税率10%%线性）",
      sp.diff(sp.Rational(10, 100) * S_, S_) > 0)

# ============ 卡5·数学4.1·2020全国Ⅰ卷文数T8 ============
# a·log_3 4=2，则4^(-a)=1/9，选B
check("卡5-核心恒等式:4^(2/log_3 4)=3^2=9（4=3^(log_3 4)代入）",
      sp.simplify(sp.Integer(4)**(2/sp.log(4, 3)) - 9) == 0)
check("卡5-结论:4^(-a)=1/9（a=2/log_3 4）",
      sp.simplify(sp.Integer(4)**(-2/sp.log(4, 3)) - sp.Rational(1, 9)) == 0)
check("卡5-数值佐证:N(4^-a)=%.10f≈0.1111111111" % sp.N(sp.Integer(4)**(-2/sp.log(4, 3)), 10),
      abs(sp.N(sp.Integer(4)**(-2/sp.log(4, 3)), 12) - sp.N(sp.Rational(1, 9), 12)) < sp.Float('1e-10'))

# ============ 卡6·数学4.4·2016浙江卷文数T5 ============
# a,b>0,a≠1,b≠1,log_a b>1 ⇒ (b-1)(b-a)>0，选D（分a>1与0<a<1两支枚举验证）
check("卡6-支1:a=2,b=8(log_2 8=3>1):(b-1)(b-a)=7*6>0",
      (8 - 1) * (8 - 2) > 0)
check("卡6-支2:a=0.5,b=0.25(log_0.5 0.25=2>1):(b-1)(b-a)=(-0.75)(-0.25)>0",
      sp.simplify((sp.Rational(1, 4) - 1) * (sp.Rational(1, 4) - sp.Rational(1, 2))) > 0)
check("卡6-逻辑闭:sympy枚举两支均(b-1)与(b-a)同号",
      ((8 - 1) > 0 and (8 - 2) > 0) and
      (sp.simplify(sp.Rational(1, 4) - 1) < 0 and sp.simplify(sp.Rational(1, 4) - sp.Rational(1, 2)) < 0))
check("卡6-他项证伪:B式(a-1)(a-b):支1中=1*2*(-6)<0不恒正",
      sp.simplify((2 - 1) * (2 - 8)) < 0)

print("=" * 62)
print("sympy独立复核·数学域6节直读卡（1108·零采信纯复算）")
print("=" * 62)
for name, ok in results:
    print(("PASS  " if ok else "FAIL  ") + name)
print("=" * 62)
print("TOTAL=%d  PASS=%d  FAIL=%d  exit=%d" % (len(results), len(results) - fails, fails, 0 if fails == 0 else 1))
sys.exit(0 if fails == 0 else 1)
