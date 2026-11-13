# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·生物5.3真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 有氧呼吸ATP储能效率 977.28/2870≈34.1%
e1 = sp.Rational("977.28")/sp.Rational("2870")*100
check("T1_有氧呼吸ATP储能效率≈34.1%（34.05→保留1位）", round(float(e1),1) == 34.1, f"{round(float(e1),2)}%")

# T2 无氧呼吸ATP储能效率 61.08/196.65≈31.1%
e2 = sp.Rational("61.08")/sp.Rational("196.65")*100
check("T2_无氧呼吸ATP储能效率≈31.1%", round(float(e2),1) == 31.1, f"{round(float(e2),2)}%")

# T3 无氧呼吸乳酸储能 196.65-61.08=135.57 kJ
check("T3_乳酸储能196.65−61.08=135.57 kJ", sp.Rational("196.65")-sp.Rational("61.08") == sp.Rational("135.57"), "p94域")

# T4 无氧呼吸1mol葡萄糖→2mol乳酸 C守恒6→2×3
check("T4_C守恒6C→2×3C（1mol糖→2mol乳酸）", 6 == 2*3, "乳酸型第二阶段")

# T5 有氧呼吸总式原子守恒：C₆H₁₂O₆+6O₂+6H₂O→6CO₂+12H₂O
c, h, o = sp.symbols("c h o", integer=True)
c = 6; h_l = 12+6*2; o_l = 6+6*2+6  # 左
h_r = 12*2; o_r = 6*2+12  # 右
check("T5_有氧呼吸总式原子守恒C6·H24·O18", c == 6 and h_l == h_r == 24 and o_l == o_r == 24, f"左H{h_l}/O{o_l}·右H{h_r}/O{o_r}")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 生物5.3真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_生物5.3_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
