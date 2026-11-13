# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理3.1升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2：k=100·挂3N伸3cm·总长13cm
r1k = sp.Rational(1,1)/sp.Rational(1,100)
r1x = 3/r1k
check("T1_选择2 k=100·x=3cm·总长13", r1k==100 and r1x==sp.Rational(3,100) and 10+3==13, "先减原长")
# T2 选择3：k甲=100·k乙=200
r2a = sp.Rational(1,1)/sp.Rational(1,100); r2b = sp.Rational(2,1)/sp.Rational(1,100)
check("T2_选择3 k甲=100·k乙=200", r2a==100 and r2b==200, "乙硬")
# T3 填空：F=2N·k=50
r3f = sp.Rational(2,10)*10; r3k = r3f/sp.Rational(4,100)
check("T3_填空 F=2·k=50", r3f==2 and r3k==50, "16-12=4cm")
# T4 解答1：山东同型 k=0.3×10/(3×0.02)=50
r4 = sp.Rational(3,10)*10/(3*sp.Rational(2,100))
check("T4_解答1 k=50", r4==50, "对称分担")
# T5 解答2：串联F=10·x₁=10cm·x₂=5cm·总15cm
r5f = 1*10; r5x1 = sp.Rational(r5f, 100); r5x2 = sp.Rational(r5f, 200)
check("T5_解答2 F=10·x₁=0.1·x₂=0.05", r5f==10 and r5x1==sp.Rational(1,10) and r5x2==sp.Rational(1,20) and r5x1+r5x2==sp.Rational(3,20), "串联等力")
# T6 真题山东T2：k=0.3×10/(3×0.01)=100
r6 = sp.Rational(3,10)*10/(3*sp.Rational(1,100))
check("T6_真题山东 k=100", r6==100, "mg/(3x)")
# T7 既有账复跑维持：T6首尾法26.1·验④k=25（1031账）
check("T7_既有账 k=0.5/0.02=25复跑", sp.Rational(1,2)/sp.Rational(2,100)==25, "验④维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理3.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
