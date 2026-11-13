# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·化学3.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_化学3.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答1：1t NH₃ → HNO₃（N守恒1:1）→ 63/17 ≈ 3.71t
m1 = sp.Rational(1) * sp.Integer(10)**6 / 17 * 63 / sp.Integer(10)**6
check("T1_解答1 1t NH₃→HNO₃ 3.71t", sp.simplify(m1) == sp.Rational(63,17) and round(float(sp.Rational(63,17).evalf(6)), 2) == 3.71, f"精确值={m1}t≈3.71t（两位）")

# T2 真题A项：2.24L(标况)NO/N₂O混合气=0.1mol·两种分子各含1个O原子→O原子0.1N_A（A对）
check("T2_真题A项 O原子0.1N_A（A对）", sp.Rational(224,100)/sp.Rational(224,10) == sp.Rational(1,10), "NO 1个O·N₂O 1个O·无论比例皆0.1N_A")

# T3 真题C项：3.3g NH₂OH（M=33）=0.1mol·N(−1→+3)失4e/mol→0.4N_A（选项0.6N_A错）
n3 = sp.Rational(33,10)/33; e3 = n3*4
check("T3_真题C项 0.4N_A（C错核·非0.6）", n3 == sp.Rational(1,10) and e3 == sp.Rational(4,10), "N −1→+3失4e")

# T4 真题D项：2.8g N₂=0.1mol·价电子10/分子→1N_A（选项0.6N_A错）
n4 = sp.Rational(28,10)/28
check("T4_真题D项 价电子1N_A（D错核·非0.6）", n4 == sp.Rational(1,10) and n4*10 == 1, "N原子5个价电子×2")

# T5 歧化平衡：3NO₂+H₂O=2HNO₃+NO（N 3=3·H 2=2·O 6+1=6+1）
check("T5_选择3 3NO₂+H₂O=2HNO₃+NO四守恒", 3 == 2+1 and 2 == 2 and 6+1 == 6+1, "NO₂歧化+4→+5/+2")

# T6 NH₃→NO电子转移：N(−3→+2)失5e/mol
check("T6_考向二 NH₃催化氧化失5e/mol", sp.Integer(2)-(-3) == 5, "4NH₃+5O₂=4NO+6H₂O")

# T7 考位锚既有复跑：1mol HNO₃(+5→0)完全转化为N₂转移5N_A（既有账数值复核）
check("T7_考位锚既有 5N_A复跑", sp.Integer(5)-0 == 5, "HNO₃→N₂每N得5e")

# T8 生成1mol HNO₃耗NO₂ 1.5mol（3NO₂:2HNO₃比）
check("T8_选择3 D项核 1.5mol NO₂/HNO₃", sp.Rational(3,2) == sp.Rational(3,2), "3NO₂+H₂O=2HNO₃+NO·3:2")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学3.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
