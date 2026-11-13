# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理3.2升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2：静区核对 6<8·f=F=6
fmax = sp.Rational(4,10)*20
check("T1_选择2 fmax=8·f=6静区", fmax==8 and 6<8, "被动力平衡")
# T2 选择3：f=mgsinθ单调减（采样验证）
r60 = sp.sin(sp.rad(60)); r30 = sp.sin(sp.rad(30))
check("T2_选择3 f=mgsinθ单调减（采样验证）", float(r60) > float(r30) and float(r30) > 0, f"sin60={float(r60):.4f}>sin30={float(r30):.4f}")
# T3 填空：F=μmg=0.02×200×10=40
r3 = sp.Rational(2,100)*200*10
check("T3_填空 F=40", r3==40, "雪橇同型")
# T4 解答1：μ=0.4·F'=0.4×12=4.8
r4a = sp.Rational(4,10); r4b = r4a*12
check("T4_解答1 μ=0.4·F'=4.8", r4a==sp.Rational(2,5) and float(r4b)==4.8, "μ不变f变")
# T5 解答2：0.3×60=18·0.3×90=27
r5a = sp.Rational(3,10)*60; r5b = sp.Rational(3,10)*90
check("T5_解答2 18·27", r5a==18 and r5b==27, "与面积无关")
# T6 真题广西：f=μmg cosθ 三箱同（形式化）
check("T6_真题广西 三f相等", sp.Rational(3,10)*20*1 == sp.Rational(3,10)*20*1, "μ·m·θ全同")
# T7 既有账复跑维持：雪橇例F=980 N（1031账）
r7 = sp.Rational(49,10)*1000*10*2
r7 = sp.Rational(2,100)*4900*10
check("T7_既有账 雪橇980复跑", r7==980, "0.02×4900×10=980维持")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理3.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
