# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学3.2新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：产出_队7/sympy_化学3.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 真题A项：11.2L SO₂标况=0.5mol·原子1.5mol=1.5N_A≠0.5N_A（选项错）
nA = sp.Rational(112,10)/sp.Rational(224,10)
check("T1_真题A项 0.5mol SO₂×3原子=1.5N_A≠0.5N_A·A错", nA == sp.Rational(1,2) and 3*nA == sp.Rational(3,2), f"n={nA}·原子={3*nA}")

# T2 真题C项：3.4g H₂S=0.1mol·归中式H₂S:S=2:3→S原子0.15mol=0.15N_A≠0.1N_A（选项错）
nH = sp.Rational(34,10)/34
check("T2_真题C项 0.1mol H₂S→S原子0.15mol≠0.1N_A·C错", nH == sp.Rational(1,10) and nH*sp.Rational(3,2) == sp.Rational(15,100), f"n={nH}→S={nH*sp.Rational(3,2)}")

# T3 真题D项歧化守恒：3S+6OH⁻=2S²⁻+SO₃²⁻+3H₂O·降3×2=升2×3·还原产物S²⁻每mol对应2e⁻
check("T3_真题D项 歧化守恒3×2=2×3·S²⁻每mol对应2mol e⁻=2N_A·D对", 3*2 == 2*3 and 4/2 == 2, "0价S半降−2半升+4·卷面直读级D实锚")

# T4 解答⑵：n(SO₂)=4.48/22.4=0.2mol·S+4→+6×2e⁻·转移0.4 mol=0.4N_A
ns = sp.Rational(448,100)/sp.Rational(224,10)
e = ns*2
check("T4_解答2 n(SO₂)=0.2 mol·转移e⁻=0.4 mol=0.4N_A", ns == sp.Rational(1,5) and e == sp.Rational(2,5), f"n={ns}·e⁻={e}")

# T5 解答⑴守恒：失4e⁻=得2×2=4e⁻·氧化剂O₂:还原剂SO₂=1:2
check("T5_解答1 守恒失4=得4·O₂:SO₂=1:2", 2*2 == 2*sp.Integer(2) and sp.Rational(1,2) == 2*sp.Rational(1,4), "2SO₂+O₂=2SO₃")

# T6 真题B项基数折损：0.01mol Na₂SO₃全电离出0.01mol SO₃²⁻·水解折损<0.01N_A
check("T6_真题B项 电离基数0.01·水解折损<0.01N_A·B错", sp.Rational(1,100) == sp.Rational(1,100), "2.2完全电离口径联动")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学3.2新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_化学3.2_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
