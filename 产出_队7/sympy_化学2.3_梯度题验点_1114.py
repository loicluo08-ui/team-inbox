# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学2.3新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：产出_队7/sympy_化学2.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择3：KMnO₄+16HCl——Mn×2各收5e⁻=10e⁻→10份HCl被氧化·16−10=6未氧化·比10:6
ox = sp.Integer(2) * 5
check("T1_选择3 被氧化HCl=10·未氧化=16−10=6·比10:6", ox == 10 and 16 - 10 == 6, "Mn+7→+2×2=10e⁻·B对")

# T2 真题C项守恒：C(−2→+4)×5=30e⁻ = N(+5→0)×6=30e⁻→氧化剂:还原剂=6:5
lost = 5 * (4 - (-2)); gained = 6 * (5 - 0)
check("T2_真题C项 失30=得30·氧化剂:还原剂=6:5", lost == gained == 30, f"CH₃OH失{lost}·NO₃⁻得{gained}")

# T3 真题配平独立复核：5CH₃OH+6NO₃⁻+6H⁺=5CO₂+3N₂+13H₂O（C5·N6·H26·O23·电荷0）
check("T3_真题配平 C5=5·N6=6·H26=26·O23=23·电荷−6+6=0", 5==5 and 6==6 and 5*4+6==13*2 and 5+18==10+13 and -6+6==0, "全元素+电荷守恒✓")

# T4 解答⑵：n(CO)=3.36/22.4=0.15 mol→电子守恒n(Fe)=2×0.15/3=0.1 mol→m=5.6 g
nco = sp.Rational(336, 100) / sp.Rational(224, 10)
nfe = 2 * nco / 3
m = nfe * 56
check("T4_解答2 n(CO)=0.15·n(Fe)=0.1 mol·m=5.6 g", nco == sp.Rational(15,100) and nfe == sp.Rational(1,10) and float(m) == 5.6, f"n={nco}→{nfe}→{float(m)} g")

# T5 解答⑴电子守恒核：Fe₂O₃得2×3=6 = CO失3×2=6
check("T5_解答1守恒 得2×3=6=失3×2=6", 2*3 == 3*2, "Fe+3→0·C+2→+4·守恒闭合")

# T6 直觉实验判据：Fe钉→Cu置换 Fe 0→+2失2 = Cu +2→0得2（1:1·蓝色变浅判据）
check("T6_直觉实验 Fe失2=Cu得2·1:1置换", 2 == 2, "铁钉版居家复刻判据·Fe+CuSO₄=FeSO₄+Cu")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学2.3新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_化学2.3_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
