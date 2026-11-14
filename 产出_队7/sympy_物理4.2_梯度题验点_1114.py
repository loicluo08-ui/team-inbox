# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·物理4.2真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答2① 绳拉力 F=Ma=mg·M/(M+m)=5/11 N
M, m, g = sp.Rational("0.50"), sp.Rational("0.05"), sp.Rational("10")
a_total = m*g/(M+m)
F = M*a_total
check("T1_绳拉力F=5/11≈0.455 N", F == sp.Rational(5, 11) and round(float(F), 3) == 0.455, f"F={F} N·a={a_total:.6f}")

# T2 解答2② 偏差=(mg−F)/mg=m/(M+m)=1/11≈9.1%
bias = (m*g - F)/(m*g)
check("T2_偏差=m/(M+m)=1/11≈9.1%", bias == sp.Rational(1, 11) and round(float(bias)*100, 1) == 9.1, f"偏差={float(bias)*100:.2f}%")

# T3 填空 计数点间隔=5×0.02=0.1 s
check("T3_计数点间隔5T=0.1 s", 5*sp.Rational("0.02") == sp.Rational("0.1"), "每5间隔取一计数点")

# T4 真题(4)逐差公式自洽：xₖ=½a(5kT)²→(x₆−2x₃)/(15T)²=a（符号恒等）
a_, T_ = sp.symbols("a T", positive=True)
xk = lambda k: sp.Rational(1, 2)*a_*(5*k*T_)**2
ratio = sp.simplify((xk(6) - 2*xk(3))/(15*T_)**2)
check("T4_逐差公式(x₆−2x₃)/(15T)²≡a符号恒等", ratio == a_, f"化简={ratio}")

# T5 真题(4)瞬时速度公式数值核：a=2·T=0.02→v₅=(x₆−x₄)/(10T)=0.2 m/s=a·t₅
a_num = sp.Rational(2); T_num = sp.Rational("0.02")
x6 = sp.Rational(1, 2)*a_num*(5*6*T_num)**2; x4 = sp.Rational(1, 2)*a_num*(5*4*T_num)**2
v5 = (x6 - x4)/(10*T_num)
check("T5_v₅=(x₆−x₄)/(10T)=a·t₅数值自洽（t₅=25T=0.5s）", v5 == a_num*25*T_num, f"v₅={v5} m/s")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 物理4.2真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_物理4.2_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
