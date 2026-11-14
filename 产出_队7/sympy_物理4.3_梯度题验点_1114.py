# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·物理4.3真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择3/填空 a=F合/m：4/2=2 m/s²
a1 = sp.Rational(4)/2
check("T1_a=4N/2kg=2 m/s²", a1 == 2, f"a={a1}")

# T2 填空 力加倍a加倍：8/2=4 m/s²
a2 = sp.Rational(8)/2
check("T2_a=8N/2kg=4 m/s²（正比翻倍）", a2 == 4 and a2 == 2*a1, f"a={a2}")

# T3 解答1 上升段 a=(mg+f)/m=(5+0.5)/0.5=11 m/s²
m_, g_, f_ = sp.Rational("0.5"), sp.Rational("10"), sp.Rational("0.5")
a3 = (m_*g_ + f_)/m_
check("T3_上抛上升段a=(mg+f)/m=11 m/s²", a3 == 11, f"a={a3}")

# T4 解答2① 超重 N=m(g+a)=60×11=660 N
N = sp.Rational("60")*(sp.Rational("10")+1)
check("T4_电梯加速上升N=m(g+a)=660 N", N == 660, f"N={N}")

# T5 解答2② 超重差量 ΔN=ma=60 N
dN = sp.Rational("60")*1
check("T5_超重差量ΔN=ma=60 N", dN == 60, f"ΔN={dN}")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 物理4.3真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_物理4.3_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
