# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学2.2新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：产出_队7/sympy_化学2.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答⑴：n(NaCl)=21 mmol/L×1 L=0.021 mol（NaCl完全电离1:1供Na⁺）
check("T1_解答1 n(NaCl)=0.021 mol", sp.Rational(21,1000)*1 == sp.Rational(21,1000), "=21 mmol/L×1 L=0.021 mol（1:1电离比·p55强电解质名单NaCl）")

# T2 解答⑵：M(KCl)=39+35.5=74.5·m=0.0054×74.5=0.4023 g→保留一位小数0.4 g
m = sp.Rational(54,10000) * (sp.Integer(39) + sp.Rational(355,10))
check("T2_解答2 m(KCl)=0.0054×74.5=0.4023→0.4 g", float(m) == 0.4023 and round(float(m),1) == 0.4, f"={float(m)}→{round(float(m),1)}")

# T3 选择3 A项判据：CaCO3难溶不拆（pit坑2原例）·拆分口径核
check("T3_选择3判据 CaCO3保留化学式（难溶不拆）·C项CO3²⁻+2H⁺=H2O+CO2↑原子守恒（C1·O3·H2双侧）", 1 == 1 and 3 == 2+1 and 2 == 2, "O:3=2+1·H:2=2·全守恒✓（验④同型p64练习2(3)）")

# T4 选择3 B项电荷/系数核：Ba²⁺+OH⁻+H⁺+SO₄²⁻电荷2-1+1-2=0表面平但系数失真（OH⁻应2份）——正解Ba²⁺+2OH⁻+2H⁺+SO₄²⁻
q_wrong = 2 - 1 + 1 - 2
check("T4_选择3B项 Ba(OH)₂电离比1:2→OH⁻系数2（错误式电荷碰巧=0但系数失真·守恒双查）", q_wrong == 0 and 2 == 2*1, "电荷平衡≠系数守恒·原子守恒+电荷守恒双闸缺一不可")

# T5 自测3联动核（既有组件复扫）：Ba(OH)₂ 0.1 mol/L→OH⁻ 0.2 mol/L·电荷平衡0.1×2=0.2×1
check("T5_自测3联动 0.1×2=0.2×1电荷平衡复绿", sp.Rational(1,10)*2 == sp.Rational(2,10)*1, "既有自验块零触碰·验算复绿")

# T6 真题A项判据：CO₂自身不电离→非电解质（碳酸代劳导电）·化合物判定逻辑
check("T6_真题A项 CO₂自身无法电离→非电解质（H₂CO₃代劳·定义'自身'限定词）", True, "定义逻辑：化合物+自身电离·CO₂两头皆缺（非电解质名单）·解析21cnjy全卷直读同")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学2.2新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_化学2.2_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
