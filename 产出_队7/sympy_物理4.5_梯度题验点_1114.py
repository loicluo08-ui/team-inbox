# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·物理4.5真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择2 整体法 a=F/(m1+m2)=10/5=2 m/s²
a = sp.Rational(10)/(2+3)
check("T1_整体a=10/5=2 m/s²", a == 2, f"a={a}")

# T2 选择3 隔离法 N=m2·a=3×2=6 N
N = 3*a
check("T2_内力N=m2a=6 N", N == 6, f"N={N}")

# T3 解答1 匀速下滑 f=mg·sin30°=10 N
f = 2*10*sp.Rational(1, 2)
check("T3_匀速下滑f=mg·sin30°=10 N", f == 10, f"f={f}")

# T4 解答2① 斜面加速 a=g(sin37°−μcos37°)=2 m/s²
a2 = 10*(sp.Rational(6, 10) - sp.Rational(1, 2)*sp.Rational(8, 10))
check("T4_斜面下滑a=g(sin−μcos)=2 m/s²", a2 == 2, f"a={a2}")

# T5 解答2② v=at=2×2=4 m/s
v = a2*2
check("T5_2s末v=4 m/s", v == 4, f"v={v}")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 物理4.5真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_物理4.5_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
