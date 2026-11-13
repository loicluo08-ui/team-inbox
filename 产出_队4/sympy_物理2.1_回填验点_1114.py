# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理2.1真题锚全题四段式回填·验点（v2.3工序七·承两件套令①）
# [补落留痕1114：初版inline三版跑毕仅txt入库py缺席=承诺与实体不符·本件真脚本补落
#  [修复留痕1114三轮：①甲卷v̄AD口径混用24/10误写②R1/R2 cm/s÷100统一m/s③R1分母585/40000笔误→585/400·数值全程无误]]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
v_a = (sp.Rational(860,100) - sp.Rational(275,100)) / sp.Rational(4,100)
v_a_ms = v_a/100
check("16Ⅰ⑵ x₃=8.60→v₂=1.4625 m/s", v_a_ms == sp.Rational(585,400) and float(v_a_ms)==1.4625, f"v₂={float(v_a)} cm/s={float(v_a_ms)} m/s")
v_b = (sp.Rational(865,100) - sp.Rational(275,100)) / sp.Rational(4,100)
v_b_ms = v_b/100
check("16Ⅰ⑵ x₃=8.65→v₂=1.475 m/s", float(v_b_ms)==1.475, f"v₂={float(v_b)} cm/s={float(v_b_ms)} m/s")
v_ad = sp.Rational(24, 1) / sp.Rational(3, 10)
check("甲卷⑴ v̄AD=80.00 cm/s", v_ad == 80, f"v̄AD={float(v_ad)} cm/s=0.8 m/s")
r4 = 2*sp.Integer(68)
check("甲卷⑷ a=2k=136 cm/s²=1.36 m/s²", r4==136, f"2×68.0={r4}")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理2.1回填验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
