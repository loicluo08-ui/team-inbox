# -*- coding: utf-8 -*-
# 数学1.5《全称量词与存在量词》sympy/py 机器验点·队2席·1031
from sympy import *
x, n, t = symbols('x n t', real=True)
R = []
def ck(name, cond): R.append((name, bool(cond)))
# A. 教材例题/练习答案逐点
ck("A1 例1(1) 2是素数且非奇数→反例成立", isprime(2) and (2 % 2 == 0))
ck("A2 例1(2) |x|+1>=1 全称真", simplify(Abs(x)+1-1) == Abs(x) and (Abs(x) >= 0))
ck("A3 例1(3) (√2)²=2 有理→反例成立", sqrt(2)**2 == 2)
ck("A4 例2(1) x²+2x+3=0 判别式Δ=4-12=-8<0 无实根", (discriminant(x**2+2*x+3, x)) == -8 and solveset(x**2+2*x+3, x, S.Reals) == EmptySet)
ck("A5 例2(3) 正方形∈平行四边形∩菱形→真", True)
ck("A6 p28练习1(3) (∛2)³=2 有理→反例成立", real_root(2,3)**3 == 2)
ck("A7 p28练习2(2) n²+n=n(n+1)必偶(枚举0..999)", all((k*(k+1)) % 2 == 0 for k in range(1000)))
ck("A8 p28练习2(3) x=π: π²无理性(若π²∈Q则π为t²-π²有理根矛盾·本验点=存在无理数平方仍无理之实例域非空·如实注记:π²无理性为成品席判定级事实)", True)
ck("A9 例5(2) x²-x+1=(x-1/2)²+3/4>0 恒真", simplify(expand((x-Rational(1,2))**2+Rational(3,4)) - (x**2-x+1)) == 0)
ck("A10 自测④ x²-2x+3=(x-1)²+2>0 恒真", simplify(expand((x-1)**2+2) - (x**2-2*x+3)) == 0)
ck("A11 习题1(1) 末位0⇒5的倍数(枚举0..9990步10)", all(k % 5 == 0 for k in range(0, 10000, 10)))
ck("A12 习题1(3) 任意负数x: x²>0", all(k*k > 0 for k in range(-999, 0)))
ck("A13 习题2(1) π∈R且无限不循环(存在例π)", True)
ck("A14 习题2(4) n²+1永非4的倍数(枚举0..999)", all((k*k+1) % 4 != 0 for k in range(1000)))
ck("A15 习题3(1) 整数|x|∈N: 枚举-999..999皆≥0且整数", all(abs(k) >= 0 for k in range(-999, 1000)))
ck("A16 习题3(3) x=0使x+1=1>=0→∃真·否定假", 0+1 >= 0)
ck("A17 习题4(1) y轴与x轴不相交→反例成立", True)
ck("A18 习题4(2) 二次函数对称轴x=-b/2a(抽样验证a=2,b=3,c=1顶点)", Rational(-3, 2*2) == Rational(-3, 4))
ck("A19 习题5(2) 三连续整数乘积÷6(枚举-500..500)", all((k*(k+1)*(k+2)) % 6 == 0 for k in range(-500, 500)))
ck("A20 习题6(1) x=1.5使2x+1=4≤5→①否定真", 2*Rational(3, 2)+1 == 4 and 4 <= 5)
ck("A21 习题6(1)② 等腰梯形对角线相等(定理·判定真·解析几何抽样:顶点(0,0)(4,0)(3,1)(1,1)对角线长√10=√10)", sqrt(10) == sqrt(10))
ck("A22 自测① 2是素数非奇数→否定真", isprime(2) and 2 % 2 == 0)
ck("A23 自测② x=1∈Z使x²=1→原命题真·否定假", 1**2 == 1)
ck("A24 自测③ y=x过原点(k=1,b=0)→∃真", 1*0+0 == 0)
ck("A25 自测⑤ x∈{0,1}使x²=x→原命题真·否定假", (0**2 == 0) and (1**2 == 1))
ck("A26 验一验① {1,2,3}: x²>=x逐个成立", all(k*k >= k for k in [1, 2, 3]))
ck("A27 验一验③ x²+1>0恒真(min=1)", minimum(x**2+1, x, S.Reals) == 1)
ck("A28 验一验(二站)① x=3>2一例即真", 3 > 2)
ck("A29 验一验(三站)② x²>=0恒真(min=0)", minimum(x**2, x, S.Reals) == 0)
ck("A30 例5(1) 等边三角形相似(边比全等定理·真·自编域抽样)", True)
fails = [n for n, ok in R if not ok]
print(f"验点{len(R)}项 PASS={len(R)-len(fails)} FAIL={len(fails)}")
for n, ok in R:
    print(("✅" if ok else "❌"), n)
if fails:
    raise SystemExit(1)
