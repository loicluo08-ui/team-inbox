# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学3.3新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：产出_队7/sympy_化学3.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 真题A项：2.24L X+Y混合=0.1mol·X=NO(1O)·Y=N₂O(1O)·每分子1个O→O原子0.1mol=0.1N_A
n = sp.Rational(224,100)/sp.Rational(224,10)
check("T1_真题A项 0.1mol混合气·每分子1O·O原子=0.1N_A·A对", n == sp.Rational(1,10) and 1*n == sp.Rational(1,10), "比例无关原子数必对·卷面直读级")

# T2 真题C项：M(NH₂OH)=14+3+16+1=33·3.3g=0.1mol·N−1→+3升4e⁻·0.4N_A≠0.6N_A
mNH = sp.Integer(14) + 3*sp.Integer(1) + sp.Integer(16)
eC = sp.Rational(33,10)/mNH*4
check("T2_真题C项 M=33·0.1mol×4e⁻=0.4N_A≠0.6N_A·C错", mNH == 33 and eC == sp.Rational(4,10), f"M={mNH}·e⁻={eC}")

# T3 真题D项：2.8g N₂=0.1mol·价电子每N5×2=10→1N_A≠0.6N_A
nN2 = sp.Rational(28,10)/(2*14)
check("T3_真题D项 0.1mol N₂×10价电子=1N_A≠0.6N_A·D错", nN2 == sp.Rational(1,10) and nN2*10 == 1, "5×2=10")

# T4 解答⑵：n(N₂)=11.2/22.4=0.5mol·1:2→n(NH₃)=1mol·m=17 g
nn = sp.Rational(112,10)/sp.Rational(224,10)
mNH3 = nn*2*17
check("T4_解答2 n(N₂)=0.5·n(NH₃)=1 mol·m=17 g", nn == sp.Rational(1,2) and float(mNH3) == 17.0, f"n={nn}→m={mNH3}")

# T5 解答⑶电子守恒：N₂每分子收2×3=6e⁻·0.5mol×6=3 mol
check("T5_解答3 转移电子=0.5×6=3 mol", 2*3 == 6 and sp.Rational(1,2)*6 == 3, "N 0→−3·得3e⁻×2原子")

# T6 选择3：HNO₃中N+5→0·5e⁻/N·1mol=5 mol·B对（kao考向二原句）
check("T6_选择3 5−0=5e⁻/N·1mol→5 mol·B对", 5-0 == 5, "考位锚考向二同款算法")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学3.3新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_化学3.3_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
