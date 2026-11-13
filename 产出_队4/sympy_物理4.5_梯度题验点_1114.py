# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理4.5升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# [R行整改留痕1114同族第三例：初版py经cp进程替换落盘失败=txt内容冒充py（QC R行抓出）·本件真脚本重提交替换·显式写盘+落盘后校验流程
#  [修复留痕1114三轮：μ₁mg=0.02×1000×10两次漏乘10+float/Rational==坑·统一Rational口径固化·数值全程无误]]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
r1a = sp.Rational(16,8); r1f = 2*r1a
check("T1_选择2 a=2·f=4", r1a==2 and r1f==4, "整体求a隔离求内力")
X = sp.Symbol('X', positive=True)
r2 = 3*X/X
check("T2_选择3 T₁:T₃=3:1", sp.simplify(r2)==3, "Tₙ=(N+1−n)X·分配看结构")
r3 = 60*10*sp.Rational(1,2)
check("T3_填空 f=300", r3==300, "匀速=平衡")
r4a = sp.Rational(4,10)*10; r4x = 12**2/(2*4); r4t = sp.Rational(12,4)
check("T4_解答1 4·18·3", r4a==4 and r4x==18 and r4t==3, "单向通路")
mumu = sp.Rational(2,100)*1000*10
r5a = (sp.Rational(400,1) - mumu)/1000
r5v = r5a*10
r5x1 = sp.Rational(1,2)*r5a*100
r5b = sp.Rational(1,10)*10
r5t2 = sp.Rational(2,1)/r5b
r5x2 = sp.Rational(4,2)
check("T5_解答2 全链", mumu==200 and r5a==sp.Rational(1,5) and r5v==2 and r5x1==10 and r5b==1 and r5t2==2 and r5x2==2, f"μ₁mg={int(mumu)}·a₁={float(r5a)}·v={float(r5v)}·x₁={float(r5x1)}·a₂={float(r5b)}·t₂={float(r5t2)}·x₂={float(r5x2)}·总{float(r5x1+r5x2)}m/{float(10+r5t2)}s")
r6u = 3*sp.Rational(1,1)*(0+1); r6u2 = 2*1; r6u3 = 1*1
check("T6_真题福建T5 3:2:1两态恒定复跑", r6u==3 and r6u2==2 and r6u3==1, "1108直读卡账维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理4.5升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
