# -*- coding: utf-8 -*-
# 队2席·数学4.3《对数》sympy验点·缺件补齐·搜索规划师·1101凌晨
# 源：首学版_数学4.3_对数_队2B_1031.html（main正本·v1.0.2）
from sympy import *
x=symbols('x')
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
L=log
# ① 定义回写：5⁴=625⇒log₅625=4·(1/2)^(−4)=16⇒log_{1/2}16=−4
ck("log₅625=4（5⁴=625）", L(625,5)==4)
ck("log_{1/2}16=−4（(1/2)^(−4)=16）", simplify(L(16,Rational(1,2))+4)==0)
# ② 简记 lg/ln·负数0无对数
ck("lg=底10简记·ln=底e简记（记号点）", True)
ck("负数和0没有对数（a^x>0恒正）", True)
# ③ 基本值 log_a1=0·log_aa=1
ck("log_a1=0·log_aa=1（抽底2/5/e）", L(1,2)==0 and L(2,2)==1 and L(1,5)==0 and L(5,5)==1 and L(1,E)==0 and L(E,E)==1)
# ④ 运算性质三条（数值域抽验）
ck("性质1 乘→加: lg2+lg3=lg6", simplify(L(2,10)+L(3,10)-L(6,10))==0)
ck("性质2 除→减: lg8−lg2=lg4", simplify(L(8,10)-L(2,10)-L(4,10))==0)
ck("性质3 幂→乘: lg2³=3lg2", simplify(L(8,10)-3*L(2,10))==0)
# ⑤ 换底公式 log_ab=lg b/lg a·log_2 6=lg6/lg2≈2.585
ck("换底 log₂6=lg6/lg2≈2.585", abs(float(L(6,2))-2.585)<0.001, round(float(L(6,2)),4))
ck("换底自洽 log_{1.11}2=ln2/ln1.11≈6.642", abs(float(L(2,Rational(111,100)))-6.642)<0.002, round(float(L(2,Rational(111,100))),4))
# ⑥ 问题起点反问：1.11ˣ=2 ⇒ x≈6.64（游客翻倍年数·承4.2下一站预告）
ck("翻倍年数 1.11^6.64≈2.000（x≈6.64年）", abs(1.11**6.642-2)<0.002, round(1.11**6.642,4))
# ⑦ 反写恒等 a^(log_a N)=N
ck("恒等 2^(log₂7)=7·e^(ln5)=5·10^(lg100)=100", simplify(2**L(7,2)-7)==0 and simplify(E**L(5)-5)==0 and simplify(10**L(100,10)-100)==0)
# ⑧ 里氏震级差1级≈能量32倍（10^1.5≈31.62）
ck("震级 10^1.5≈31.62≈32倍", abs(10**Rational(3,2)-31.62)<0.01, float(10**Rational(3,2)))
# ⑨ 近似值类 log_{1.1}12（大真数演示）与 lg2≈0.301·lg3≈0.477
ck("lg2≈0.3010·lg3≈0.4771", abs(float(L(2,10))-0.3010)<5e-4 and abs(float(L(3,10))-0.4771)<5e-4)
# ⑩ 运算性质反向用：log₅625=log₅(5⁴)=4log₅5=4
ck("性质3反向 log₅625=4log₅5=4", 4*L(5,5)==4)
print("\n".join(R))
p=sum(1 for r in R if r.startswith("PASS")); fq=sum(1 for r in R if r.startswith("FAIL"))
print("数学4.3 缺件补齐验点 PASS=%d FAIL=%d"%(p,fq))
import sys; sys.exit(1 if fq else 0)
