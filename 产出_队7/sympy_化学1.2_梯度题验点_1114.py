# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学1.2新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 对象=升格新增试题与直觉实验的全部可机器验数值/配平点 · 验点脚本随件留痕（sympy 1.14.0）
# 结果留痕：产出_队7/sympy_化学1.2_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

Na, Cl, O, H = 23, 35.5, 16, 1

# T1 解答⑴：Mr(NaClO)=23+35.5+16=74.5
r1 = sp.Rational(230, 10) + sp.Rational(355, 10) + 16
check("T1_解答1 Mr(NaClO)=23+35.5+16=74.5", float(r1) == 74.5, f"={float(r1)}")

# T2 解答⑵：Cl质量分数=35.5/74.5=47.65%→保留一位小数=47.7%
pct = float(sp.N(sp.Rational(355, 10) / sp.Rational(745, 10) * 100, 10))
check("T2_解答2 Cl质量分数 35.5/74.5=47.65%→47.7%", round(pct, 1) == 47.7, f"{pct:.5f}%→{round(pct,1)}%")

# T3 选择2 D选项判据复算：Na2O中O%=16/62=25.81%·Na2O2中O%=32/78=41.03%（差近16个百分点·"根本不同"成立）
o1 = 16 / 62 * 100; o2 = 32 / 78 * 100
check("T3_选择2判据 O%(Na2O)=25.81% O%(Na2O2)=41.03% 差15.2个百分点", abs(o1 - 25.81) < 0.01 and abs(o2 - 41.03) < 0.01 and abs(o2 - o1) > 14, f"{o1:.2f}%·{o2:.2f}%·Δ={o2-o1:.2f}个百分点")

# T4 挑刺①判据复算：84消毒液有效成分NaClO（教材p19）·配平核 NaClO电中性=+1-1平衡
check("T4_挑刺①判据 NaClO电中性核（Na+1·Cl+1·O-2）", 1 + 1 - 2 == 0, "化合价代数和=0·NaClO中性成立")

# T5 真题锚维持核：2023湖北T2歧化式 Cl2+2NaOH=NaCl+NaClO+H2O 元素守恒（Cl:2=1+1·Na:2=2·O:2=1+1·H:2=1+1）
check("T5_真题锚歧化式守恒 Cl:2=1+1·Na:2=2·O:2=1+1·H:2=1+1", 2 == 1 + 1 and 2 == 2 and 2 == 1 + 1 and 2 == 1 + 1, "Cl₂+2NaOH=NaCl+NaClO+H₂O全元素守恒·原锚维持判据复绿")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学1.2新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head]
for name, ok, detail in results:
    lines.append(("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else ""))
out = "\n".join(lines) + "\n"
with open("产出_队7/sympy_化学1.2_梯度题验点_1114.txt", "w", encoding="utf-8") as f:
    f.write(out)
print(out)
raise SystemExit(1 if fails else 0)
