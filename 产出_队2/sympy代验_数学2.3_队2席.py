#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数学2.3《二次函数与一元二次方程、不等式》sympy代验·搜索规划师·队2席·1031
import random
from sympy import symbols, solve, expand, Rational, sqrt, oo, Interval, Union, S, solveset, Eq, Poly, discriminant
x, v, t, w, k = symbols('x v t w k')
R14=[]
def chk(n, cond, note):
    R14.append((n, bool(cond), note))

# 1 例1: x^2-5x+6>0
chk("例1", expand((x-2)*(x-3))==x**2-5*x+6 and solve(x**2-5*x+6,x)==[2,3], "因式分解+根2,3·解集x<2或x>3")
# 2 例2: 9x^2-6x+1>0
chk("例2", expand((3*x-1)**2)==9*x**2-6*x+1 and Rational(1,3) in solve(9*x**2-6*x+1,x), "完全平方·Δ=0根1/3·解集x≠1/3")
# 3 例3: -x^2+2x-3>0 → x^2-2x+3<0
disc=discriminant(x**2-2*x+3,x)
chk("例3", disc==-8 and (x**2-2*x+3).subs(x,1)==2>0, "Δ=-8<0·顶点值2>0恒正·解集∅")
# 4 例4: -20x^2+2200x>60000
chk("例4", solve(x**2-110*x+3000,x)==[50,60] and len([i for i in range(51,60)])==9, "根50,60·整数解51-59共9个")
# 5 例5: v^2+9v-7110>0
f5=lambda t_: t_**2+9*t_-7110
v2=(-9+sqrt(28521))/2
chk("例5", f5(79)<0 and f5(80)>0 and 79.9<float(v2.evalf(6))<80, "整数检验79负80正·v₂=(−9+√28521)/2≈79.94∈(79.9,80)")
# 6 回环2.1问题2: 2x^2-13x+20<=0
chk("回环", solve(2*x**2-13*x+20,x)==[Rational(5,2),4], "根2.5,4·解集2.5≤x≤4·定价2.5~4元")
# 7 习题1(1): 13-4x^2>0
chk("习题1(1)", solve(13-4*x**2,x)==[-sqrt(13)/2,sqrt(13)/2], "根±√13/2≈±1.8028")
# 8 习题1(4): -3x^2+5x-4>0
chk("习题1(4)", discriminant(3*x**2-5*x+4,x)==-23, "化正后Δ=−23<0·解集∅")
# 9 习题2(1): x^2-4x+9
chk("习题2(1)", expand((x-2)**2+5)==x**2-4*x+9, "(x−2)²+5≥5>0恒成立·有意义域R")
# 10 习题2(2): -2x^2+12x-18
chk("习题2(2)", expand(-2*(x-3)**2)==-2*x**2+12*x-18, "=−2(x−3)²·仅x=3非负·定义域{x|3}")
# 11 习题3: M∩N/M∪N
M=Interval.open(-oo,Rational(-3,2)) | Interval.open(Rational(5,2),oo)
N=Interval.open(-oo,-1) | Interval.open(6,oo)
chk("习题3", expand((2*x-5)*(2*x+3))==4*x**2-4*x-15 and expand((x-6)*(x+1))==x**2-5*x-6 and M.intersect(N)==(Interval.open(-oo,Rational(-3,2)) | Interval.open(6,oo)) and M.union(N)==(Interval.open(-oo,-1) | Interval.open(Rational(5,2),oo)), "M根5/2,−3/2·N根6,−1·M∩N/M∪N区间核对·并集左臂取宽者N(−∞,−1)吸收M(−∞,−3/2)")
# 12 习题4: 12t-5t^2>2
t1=(6-sqrt(26))/5; t2=(6+sqrt(26))/5
chk("习题4", abs(float((t2-t1).evalf(4))-2.04)<0.005, "t∈((6−√26)/5,(6+√26)/5)·停留2.04s")
# 13 习题5: A∪B
A=Interval.open(-4,4); B=Interval.open(-oo,1)|Interval.open(3,oo)
chk("习题5", A.union(B)==S.Reals, "A∪B=R")
# 14 习题6: 热带风暴
d=300*sqrt(2)
t_start=(d-150)/20; t_end=(d+150)/20
chk("习题6", abs(float(t_start.evalf(4))-13.7)<0.05 and abs(float((t_end-t_start).evalf(4))-15.0)<0.05, "13.7h后受影响·持续15.0h")
# 15 练习1(2): 3x^2-7x<=10
chk("练习1(2)", expand((3*x-10)*(x+1))==3*x**2-7*x-10, "根10/3,−1·解集−1≤x≤10/3")
# 16 表2.3-1随机200组: case逻辑 vs sympy
def case_solset(a,b,c):
    D=b*b-4*a*c
    if D>0:
        r1=(-b-sqrt(D))/(2*a); r2=(-b+sqrt(D))/(2*a)
        return (Interval.open(-oo,r1)|Interval.open(r2,oo), Interval.open(r1,r2))
    elif D==0:
        m=-b/(2*a)
        return (S.Reals-Interval(m,m), S.EmptySet)
    else:
        return (S.Reals, S.EmptySet)
random.seed(1031); bad=0
for _ in range(200):
    a=random.choice([1,2,3,Rational(1,2)]); b=random.randint(-20,20); c=random.randint(-30,30)
    gt,lt=case_solset(a,b,c)
    gt_s=solveset(a*x**2+b*x+c>0,x,S.Reals); lt_s=solveset(a*x**2+b*x+c<0,x,S.Reals)
    if not (gt_s==gt and lt_s==lt): bad+=1
chk("表2.3-1", bad==0, f"200组随机(a>0)case逻辑与sympy解集逐组一致(不符{bad}组)")

ok=sum(1 for _,c,_ in R14 if c)
for n,c,note in R14: print(f"{'PASS' if c else 'FAIL'} {n}: {note}")
print(f"\n共{len(R14)}验点·{ok} PASS / {len(R14)-ok} FAIL")
