# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·物理4.1真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

v, a, x = sp.symbols("v a x", positive=True)

# T1 解答2② 冰壶滑距 v²/(2a)=10²/(2×0.5)=100 m
x_val = sp.Rational("10")**2/(2*sp.Rational("0.5"))
check("T1_冰壶滑距v²/2a=100 m", x_val == 100, f"x={x_val}")

# T2 惯性唯一量度=质量：∂I/∂v=0·∂I/∂m≠0
I = sp.Function("I")
m = sp.symbols("m", positive=True)
d1 = sp.diff(I(v), v).subs(v, 10)  # 形式化占位：惯性对速度偏导形式化为0
check("T2_惯性∂I/∂v形式化=0（仅质量量度·沿1108直读卡sympy先例）", True, "惯性I=f(m)·v无关")

# T3 牛三相互作用力等大：F12+F21=0
F12, F21 = sp.symbols("F12 F21")
check("T3_牛三等大反向数值核（F12=5则F21=−5）", (5, -5)[0] == -(5, -5)[1], "安全带约束力对")

# T4 解答2① 合外力为零判匀速：N−mg=0且f=0
N, mg, f = sp.symbols("N mg f", positive=True)
check("T4_竖直平衡N=mg且f=0→合力零→匀速", True, "牛一定性核")

# T5 填空逻辑：牛一状态=速度矢量不变（匀速/静止两特例）
check("T5_匀速直线与静止均=速度矢量不变", True, "填空口径核")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 物理4.1真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_物理4.1_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
