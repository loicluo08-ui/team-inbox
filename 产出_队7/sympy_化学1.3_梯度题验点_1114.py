# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学1.3新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 对象=升格新增试题与真题的全部可机器验数值/逻辑点 · 验点脚本随件留痕（sympy 1.14.0）
# 结果留痕：产出_队7/sympy_化学1.3_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答⑴：n=c×V=1.5×0.25=0.375 mol→m=0.375×58.5=21.9375→保留一位小数21.9 g
n = sp.Rational(15, 10) * sp.Rational(25, 100)
m = n * sp.Rational(585, 10)
check("T1_解答1 n=1.5×0.25=0.375 mol·m=0.375×58.5=21.9375→21.9 g", n == sp.Rational(375, 1000) and float(m) == 21.9375 and round(float(m), 1) == 21.9, f"n={n}·m={float(m)}→{round(float(m),1)}")

# T2 解答⑵：V(HCl)=0.375×22.4=8.4 L（标况气体桥）
v = n * sp.Rational(224, 10)
check("T2_解答2 V(HCl)=0.375×22.4=8.4 L", float(v) == 8.4, f"={float(v)}")

# T3 选择3：n(Zn)=6.5/65=0.1 mol→计量比1:1→n(H2)=0.1 mol→V=0.1×22.4=2.24 L
nz = sp.Rational(65, 10) / 65
v2 = nz * sp.Rational(224, 10)
check("T3_选择3 n(Zn)=0.1 mol→V(H2)=2.24 L", nz == sp.Rational(1, 10) and float(v2) == 2.24, f"n={nz}·V={float(v2)}")

# T4 真题A项形式化：C价变+2→+4=失2e⁻/mol CO→1 mol CO₂转移2 mol e⁻=2N_A
check("T4_真题A项 1mol CO→CO₂价变2→转移电子2 mol=2N_A", sp.Integer(4) - sp.Integer(2) == 2, "C:+2→+4·Δ=2·A项对（D项错：N₂仅还原产物·氧化产物=CO₂·一产物一头）")

# T5 挑刺②判据：0.04 mol/0.1 L=0.4 mol·L⁻¹（倒出前后浓度不变）
c = sp.Rational(4, 100) / sp.Rational(1, 10)
check("T5_挑刺② 0.04mol÷0.1L=0.4 mol·L⁻¹（浓度属性不变）", float(c) == 0.4, f"={float(c)} mol·L⁻¹·倒出前后同值")

# T6 自测①交叉核对（升格后既有组件复扫联动）：8×6.02×10²³=4.816×10²⁴
n_e = sp.Integer(8) * sp.Rational(602, 100)
check("T6_自测①复核 8×6.02×10²³=4.816×10²⁴（既有自验块零触碰联动核）", float(n_e) == 48.16, f"={float(n_e)}×10²³")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学1.3新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head]
for name, ok, detail in results:
    lines.append(("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else ""))
out = "\n".join(lines) + "\n"
with open("产出_队7/sympy_化学1.3_梯度题验点_1114.txt", "w", encoding="utf-8") as f:
    f.write(out)
print(out)
raise SystemExit(1 if fails else 0)
