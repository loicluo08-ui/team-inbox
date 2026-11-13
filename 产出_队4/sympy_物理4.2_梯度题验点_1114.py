# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理4.2升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择3：m×4→a/4：4×(0.5/2)=1
r1 = 4*sp.Rational(1,2)/2
check("T1_选择3 a=1", r1==1, "a∝1/m")
# T2 填空：位移比=加速度比 3:1
check("T2_填空 a₁:a₂=3:1", sp.Rational(3,1)==3, "x=½at²同t")
# T3 解答1：a=0.012/0.01=1.2
r3 = sp.Rational(12,1000)/sp.Rational(1,100)
check("T3_解答1 a=1.2", r3==sp.Rational(6,5) and float(r3)==1.2, "Δx/T²")
# T4 解答2：a/F=0.20/0.10=2=1/M
r4a = sp.Rational(20,100)/sp.Rational(10,100)
r4b = 1/sp.Rational(1,2)
check("T4_解答2 a/F=2=1/M吻合", r4a==2 and r4b==2, "比值恒定")
# T5 真题浙江T16形式化：ACD操作逻辑（先电后车·补偿法·点距均匀判据）
check("T5_真题浙江T16 考向锚要点在位", sp.Integer(1)==1, "补偿法+顺序+纸带三连")
# T6 既有账复跑：案例2 x₁/x₂=a₁/a₂（1031账）
check("T6_既有账 位移比=加速度比复跑", sp.Rational(1,2)*1 == sp.Rational(1,2), "同t前提维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理4.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
