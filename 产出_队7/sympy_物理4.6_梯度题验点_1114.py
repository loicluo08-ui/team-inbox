# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·物理4.6真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1/3 加速段超重 N=m(g+a)=60×12=720 N
N1 = 60*(10+2)
check("T1_加速段N=720 N（超重）", N1 == 720, f"N={N1}")

# T2 选择3 三段压力 720/600/480（加速/匀速/减速）
N2, N3 = 60*10, 60*(10-2)
check("T2_三段N=720/600/480 N", (N1, N2, N3) == (720, 600, 480), f"({N1},{N2},{N3})")

# T3 填空 50kg加速600 N·减速400 N
Na, Nd = 50*(10+2), 50*(10-2)
check("T3_50kg加速600/减速400 N", (Na, Nd) == (600, 400), f"({Na},{Nd})")

# T4 解答1 减速上升失重 N=m(g−a)=420 N
N4 = 60*(10-3)
check("T4_减速上升N=420 N（失重）", N4 == 420, f"N={N4}")

# T5 解答2 天问仿段 a=Δv/t=90/90=1 m/s²·F=200 N
a5 = sp.Rational(100-10)/90
F5 = 200*a5
check("T5_天问仿段a=1 m/s²·F=200 N", a5 == 1 and F5 == 200, f"a={a5}·F={F5}")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 物理4.6真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_物理4.6_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
