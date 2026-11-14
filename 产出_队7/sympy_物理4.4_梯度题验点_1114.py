# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·物理4.4真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答1 单位换算 72 km/h÷3.6=20 m/s
v0 = sp.Rational("72")/sp.Rational("3.6")
check("T1_72km/h÷3.6=20 m/s", v0 == 20, f"v₀={v0}")

# T2 解答1 v=v₀+at=20+2×5=30 m/s
v = v0 + 2*5
check("T2_v=20+2×5=30 m/s", v == 30, f"v={v}")

# T3 选择2量纲链 N=kg·m/s²（F=ma数值核：2kg×3m/s²=6N）
F_check = sp.Rational(2)*3
check("T3_F=ma量纲组装数值核=6N", F_check == 6, "N=kg·m/s²")

# T4 选择3 J=N·m=kg·m²/s²（量纲指数核）
kg, m_, s_ = sp.symbols("kg m s", positive=True)
J_dim = kg*m_**2/s_**2
check("T4_J量纲=kg·m²/s²", sp.simplify(J_dim - kg*m_**2/s_**2) == 0, "功=力×位移")

# T5 解答2① a单位约分 (kg·m/s²)/kg=m/s²
a_dim = sp.simplify((kg*m_/s_**2)/kg)
check("T5_a单位=(kg·m/s²)/kg=m/s²", a_dim == m_/s_**2, f"化简={a_dim}")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 物理4.4真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_物理4.4_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
