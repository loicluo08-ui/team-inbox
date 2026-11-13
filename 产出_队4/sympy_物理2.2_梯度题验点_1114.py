# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理2.2升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# 结果留痕sympy_物理2.2_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1：6+2×3=12
r1 = 6 + 2*3
check("T1_选择1 v=12", r1 == 12, "v=v₀+at")

# T2 选择2：刹车停止时间15/3=5 s·6s末v=0（陷阱）
r2 = sp.Rational(15, 3)
check("T2_选择2 t停=5·6s末0", r2 == 5, "6>5已停")

# T3 选择3：1.6×3=4.8·1.6×2=3.2（C错证）
r3a = sp.Rational(16, 10) * 3
r3b = sp.Rational(16, 10) * 2
check("T3_选择3 4.8/3.2", r3a == sp.Rational(24, 5) and r3b == sp.Rational(16, 5), f"v₃={r3a}·v₂={r3b}")

# T4 填空：12-0.5×10=7
r4 = 12 - sp.Rational(5, 10) * 10
check("T4_填空 v=7", r4 == 7, "减速配负号")

# T5 解答1：10/1.25=8 s·9s末0（陷阱）
r5 = sp.Rational(10, 125) * 100
check("T5_解答1 t停=8·9s末0", r5 == 8, "9>8已停")

# T6 解答2：25+0.5×20=35·35/1=35·20+35=55
r6a = 25 + sp.Rational(5, 10) * 20
r6b = r6a / 1
r6c = 20 + r6b
check("T6_解答2 35·35·55", r6a == 35 and r6b == 35 and r6c == 55, "分段各管各的v₀")

# T7 真题江苏T1：a=12/2=6 m/s²（答案C）
r7 = sp.Rational(12, 2)
check("T7_真题江苏 a=6", r7 == 6, "0=12+a×2→a=−6大小6")

# T8 既有账复跑维持：教材例题36km/h=10·刹车16/6=2.67·验一验③12/4=3
r8a = sp.Rational(36, 36, ); r8a = sp.Rational(36, 1) / sp.Rational(36, 10)
r8b = sp.Rational(16, 6)
check("T8_既有账 10·2.67·3复跑", r8a == 10 and abs(float(r8b) - 2.67) < 0.01 and sp.Rational(12, 4) == 3, f"36→{r8a}·16/6={float(r8b):.4f}·12/4=3")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理2.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
