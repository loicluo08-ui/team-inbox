# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理3.4升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# [R行整改留痕1114：初版py经cp进程替换落盘失败=txt内容冒充py（QC R行抓出）·本件真脚本重提交替换
#  [T5三点采样=120°/150°/170°·按物理已验方向（随夹角增大单调发散）修正留痕对账]]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 选择2：8/6合力范围2~14·7在带内
lo = abs(8-6); hi = 8+6
check("T1_选择2 范围2~14·7在带内", lo==2 and hi==14 and lo<=7<=hi, "|F₁−F₂|≤F≤F₁+F₂")
# T2 选择3：120°特例 2×20×cos60°=20
r2 = 2*20*sp.cos(sp.rad(60))
check("T2_选择3 120°合力=20", sp.simplify(r2)==20, "等边三角形特例")
# T3 填空：勾股3-4-5
r3 = sp.sqrt(3**2+4**2)
check("T3_填空 合力5", r3==5, "勾股")
# T4 解答1：√(30²+40²)=50·标度5.0cm
r4 = sp.sqrt(30**2+40**2)
check("T4_解答1 F=50·5.0cm", r4==50 and 50/10==5, "作图口径互证")
# T5 解答2：T=20/(2cos60°)=20·三点采样单调发散（120°/150°/170°·方向=随夹角增大T单调增大）
t120 = 20/(2*sp.cos(sp.rad(60))); t150 = 20/(2*sp.cos(sp.rad(75))); t170 = 20/(2*sp.cos(sp.rad(85)))
check("T5_解答2 T=20·三点采样单调发散", sp.simplify(t120)==20 and float(t150) > 20 and float(t170) > float(t150), f"120°={float(t120):.1f}→150°={float(t150):.1f}→170°={float(t170):.1f}（单调递增方向已验）")
# T6 真题重庆：2Fcos(α/2)形式化——α=90°时2Fcos45°=√2F
r6 = 2*sp.cos(sp.pi/4)
check("T6_真题重庆 2Fcos(α/2)尺", sp.simplify(r6)==sp.sqrt(2), "α=90°→√2F带内自洽")
# T7 既有账复跑维持：pit例 F₁=F₂=10·120°合力=10
r7 = 2*10*sp.cos(sp.rad(60))
check("T7_既有账 pit例合力10复跑", sp.simplify(r7)==10, "120°特例维持B席账")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理3.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
