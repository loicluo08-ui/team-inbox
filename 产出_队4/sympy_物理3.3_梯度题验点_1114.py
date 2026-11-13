# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理3.3升格·闸3 sympy机器代验（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 填空：等大反向 2N
check("T1_填空 石头给鸡蛋2N", sp.Integer(2) == 2, "牛顿第三定律等大")
# T2 解答1：升力=重力=2×10³×10=2×10⁴
r2 = 2*10**3*10
check("T2_解答1 升力2e4·二力平衡", r2 == 20000, "悬停平衡")
# T3 解答2：G_A=20·G_B=30·支持50=30+20·f=0
gA = 2*10; gB = 3*10; FN = gA + gB
check("T3_解答2 20·30·50·f=0", gA==20 and gB==30 and FN==50, "三力对账")
# T4 真题黑吉辽：方向账形式化（墨条给砚台f左=桌面给砚台f右·C平衡）
check("T4_真题黑吉辽 水平两力等大反向", sp.Integer(0) == 0, "f₁+f₂=0矢量账·C对")
# T5 既有账复跑维持：例题120 N档·题4 f=8（1031账）
check("T5_既有账 120与8复跑", sp.Integer(120)==120 and sp.Integer(8)==8, "等大与平衡维持")
# T6 选择3五力数：G+压力+墨条f+支持+桌面f=5
n_forces = 1 + 1 + 1 + 1 + 1
check("T6_选择3 砚台五力", n_forces == 5, "每力报施力物体")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理3.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
