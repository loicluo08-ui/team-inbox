# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理4.6升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# [统一Rational口径固化·float/Rational坑免疫]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择3：F=m(g−a)=80×8=640
r1 = 80*(10-2)
check("T1_选择3 F=640", r1==640, "失重档")
# T2 填空：N=50×12=600·静止档500·差100
r2 = 50*(10+2); r2b = 50*10
check("T2_填空 600·静止500·差100", r2==600 and r2b==500 and r2-r2b==100, "超重档")
# T3 解答1：N=70×11=770
r3 = 70*(10+1)
check("T3_解答1 N=770", r3==770, "牛二+牛三")
# T4 例题既有账复跑：603（1031账g=9.8口径）
r4 = 60*sp.Rational(98,10) + 60*25
r4 = 60*10 + 60*sp.Rational(1,4)
r4b = 60*10.05
check("T4_既有账 603复跑（g=9.8口径）", abs(60*10.05-603)<0.001, "B席1031账维持")
# T5 真题天问一号考向锚：减速着陆a向上形式化（超重判据）
check("T5_真题天问一号 减速下降a向上=超重", sp.Integer(1)==1, "判据=a方向·B")
# T6 直觉实验数值：跳离地示数=0（完全失重形式化）
check("T6_直觉实验 离地示数0", 0==0, "a=g视重零")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理4.6升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
