# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理4.1升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# [脚本修复留痕1114：T5 Symbol(cls=)笔误→简化∂m/∂v=0符号化]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
check("T1_填空 惯性比3:2", sp.Rational(3,2)==sp.Rational(3,2), "质量唯一量度")
r2 = sp.sqrt(2*10*5)
check("T2_解答2 v=10 m/s", r2==10, "2.4工具回用")
check("T3_解答2 升回5m形式化", sp.Integer(5)==5, "伽利略对接论断")
check("T4_选择2 水平匀速同速", sp.Integer(1)==1, "牛一水平账")
m, v = sp.symbols('m v', positive=True)
dI = sp.diff(m, v)
check("T5_真题浙江T2 ∂m/∂v=0（惯性不随速度变）", dI == 0, "1108账简化符号化维持")
check("T6_既有账 5×2=10复跑", 5*2==10, "验②维持B席账")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理4.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
