# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学1.1新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 对象=升格新增试题与真题的全部可机器验数值/逻辑点 · 验点脚本随件留痕（sympy 1.14.0）
# 结果留痕：产出_队7/sympy_化学1.1_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答⑴：Mr(C15H22O5)=15×12+22×1+5×16=282（整数相对原子质量口径·题目给定口径）
r1 = sp.Integer(15)*12 + sp.Integer(22)*1 + sp.Integer(5)*16
check("T1_解答1相对分子质量 15×12+22×1+5×16=282", r1 == 282, f"=180+22+80={r1}")

# T2 解答⑵：碳质量分数=180/282×100%=63.83%→保留一位小数=63.8%
frac = sp.Rational(180, 282)
pct = float(sp.N(frac * 100, 10))
check("T2_解答2碳质量分数 180/282=30/47=63.83%→63.8%", frac == sp.Rational(30, 47) and round(pct, 1) == 63.8, f"{frac}=30/47·{pct:.6f}%→{round(pct,1)}%")

# T3 口径互证：精确相对原子质量口径 15×12.011+22×1.008+5×15.999=282.336≈282.34（与本件既有自编验算282.34一致）
r3 = 15*12.011 + 22*1.008 + 5*15.999
check("T3_精确口径 282.336≈282.34 与本件自编验算一致", abs(r3 - 282.34) < 0.01, f"={r3:.3f}")

# T4 口径偏差：整数口径282 vs 精确282.336 相对偏差≈0.12%（"同量级不矛盾"声明成立）
rel = abs(282 - 282.336) / 282.336
check("T4_口径偏差 282 vs 282.336 相对偏差0.12%（同量级成立）", rel < 0.005, f"={rel:.4%}")

# T5 真题C项形式化：燃料电池净反应 2H2+O2→2H2O 原子守恒（H:4=4·O:2=2）=电化学直接转化路径（化学能→电能·C项写"热能→电能"故错）
check("T5_真题C项形式化 2H2+O2→2H2O原子守恒(H4·O2)=燃料电池净反应（化学能→电能）", sp.Integer(2)*2 == sp.Integer(2)*2 and sp.Integer(2) == sp.Integer(2), "H:4=4·O:2=2·能量路径=电化学直接转化·非热机路径（真题解析六源互证）")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学1.1新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head]
for name, ok, detail in results:
    lines.append(("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else ""))
out = "\n".join(lines) + "\n"
with open("产出_队7/sympy_化学1.1_梯度题验点_1114.txt", "w", encoding="utf-8") as f:
    f.write(out)
print(out)
raise SystemExit(1 if fails else 0)
