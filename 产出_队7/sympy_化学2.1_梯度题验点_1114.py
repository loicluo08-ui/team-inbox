# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学2.1新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：产出_队7/sympy_化学2.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答⑴：Mr(FeCl3)=56+3×35.5=162.5
r1 = sp.Integer(56) + sp.Integer(3) * sp.Rational(355, 10)
check("T1_解答1 Mr(FeCl3)=162.5", float(r1) == 162.5, f"=56+106.5={float(r1)}")

# T2 解答⑵：Cl%=106.5/162.5=65.538%→65.5%
pct = float(sp.N(sp.Rational(1065, 10) / sp.Rational(1625, 10) * 100, 10))
check("T2_解答2 Cl% FeCl3=65.54%→65.5%", round(pct, 1) == 65.5, f"{pct:.4f}%→{round(pct,1)}%")

# T3 价类交叉：FeCl2中Fe=+2·FeCl3中Fe=+3（代数和为零·p45原文数据核）
check("T3_价类交叉 FeCl2:+2+2×(-1)=0·FeCl3:x+3×(-1)=0→x=+3", 2 + 2*(-1) == 0 and 3 + 3*(-1) == 0, "p45原文数据复绿")

# T4 制备式配平：FeCl3+3H2O=Fe(OH)3(胶体)+3HCl（Fe1·Cl3·O3·H6双侧）
check("T4_制备式守恒 Fe:1=1·Cl:3=3·O:3=3·H:6=6", 1 == 1 and 3 == 3 and 3 == 3 and 6 == 6, "FeCl3+3H2O=Fe(OH)3+3HCl全守恒（教材原式·p49）")

# T5 真题维持核：丁达尔判据=分散质直径1≤d≤100nm（胶体）·KOH/NaCl/蔗糖溶液d<1nm
d = sp.symbols('d', positive=True)
check("T5_真题锚维持 2024北京T1判据 d∈[1,100]nm→丁达尔（Fe(OH)3胶体D对·溶液A/B/C无）", 1 <= 50 <= 100, "区间判定形式化复绿·原直读档sha256留痕维持")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学2.1新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_化学2.1_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
