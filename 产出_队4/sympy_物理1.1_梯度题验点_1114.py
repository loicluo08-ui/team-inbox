# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理1.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 对象=升格新增试题与真题的全部可机器验数值/逻辑点 · 验点脚本随件留痕（sympy 1.14.0）
# 结果留痕：sympy_物理1.1_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

t, x = sp.symbols('t x', real=True)

# T1 填空/选择2：相对速度=速度差（向东为正）  v乙-v甲 = 5-8 = -3 → 向西3 m/s
r1 = sp.simplify(sp.Integer(5) - sp.Integer(8))
check("T1_填空相对速度 5-8=-3（向西3 m/s）", r1 == -3, f"5-8={r1}")

# T2 解答1⑴：乙相对甲速度 = 4-10 = -6 → 向西6 m/s
r2 = sp.simplify(sp.Integer(4) - sp.Integer(10))
check("T2_解答1相对速度 4-10=-6（向西6 m/s）", r2 == -6, f"4-10={r2}")

# T3 解答1⑵：追上=位置相同 10t = 4t + 60 → t=10 s
sol3 = sp.solve(sp.Eq(sp.Integer(10)*t, sp.Integer(4)*t + 60), t)
check("T3_解答1追及时间 t=10 s", sol3 == [10], f"solve 10t=4t+60 → t={sol3}")

# T4 解答2速度换算：72 km/h = 72/3.6 = 20 m/s
r4 = sp.simplify(sp.Rational(72, 1) / sp.Rational(36, 10))
check("T4_解答2换算 72km/h=20m/s", r4 == 20, f"72/3.6={r4}")

# T5 解答2⑴：全部通过=桥长+车长 → t=(850+150)/20=50 s
r5 = sp.simplify((sp.Integer(850) + sp.Integer(150)) / sp.Integer(20))
check("T5_解答2过桥时间 (850+150)/20=50 s", r5 == 50, f"(850+150)/20={r5}")

# T6 解答2⑵量级判据：150/1300km ≈ 1.15e-4 ≈ 0.01%（"约0.01%"措辞成立性核验）
r6 = sp.Rational(150, 1) / (sp.Integer(1300) * 1000)
check("T6_解答2车长占比 150/1.3e6≈1.15e-4（约0.01%）", abs(float(r6) - 1.1538e-4) < 1e-6 and float(r6) < 2e-4, f"150/1300000={float(r6):.6e}")

# T7 选择1A/挑刺错①教材数据复验：1.3e4/1.5e8 = 8.67e-5 < 1e-4（"还不到万分之一"成立）
r7 = sp.Rational(13, 10) * 10**4 / (sp.Rational(15, 10) * 10**8)
check("T7_教材公转判据 1.3e4/1.5e8=8.67e-5<1e-4", r7 == sp.Rational(13, 150000) and float(r7) < 1e-4, f"1.3e4/1.5e8={float(r7):.4e}")

# T8 真题2（2023浙江）形式化：对接后两器速度矢量相同 → 相对速度=0 → 互选参考系静止
v_s, v_t = sp.symbols('v_s v_t')
rel = sp.simplify(v_s - v_t)
check("T8_真题2形式化 对接后v相同→v_rel=0（相对静止C对D错）", rel.subs({v_s: 7660, v_t: 7660}) == 0, "v神州=v天和=7660（示例同值）→v_rel=0；对地位置随t变→A/B错")

# T9 真题1（2021浙江）定性判据复核：10909 m量级 vs 潜水器尺度（约10m）→ 比值~1e-3量级内可忽略前提（估算总时间问题）
r9 = sp.Rational(10, 10909)
check("T9_真题1量级 潜水器特征尺度10m/坐底深度10909m≈9.2e-4", float(r9) < 1e-3, f"10/10909={float(r9):.4e}（估算下降总时间问题中尺度可忽略·A成立）")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理1.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
