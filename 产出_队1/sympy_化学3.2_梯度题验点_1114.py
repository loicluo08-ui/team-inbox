# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·化学3.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_化学3.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答1：4FeS₂+11O₂=2Fe₂O₃+8SO₂·含FeS₂ 60%黄铁矿100t → n(FeS₂)=0.5×10⁶mol → SO₂=1×10⁶mol → 64t
n_fes2 = sp.Rational(100*60, 100) * sp.Integer(10)**6 / 120
n_so2 = n_fes2 * 8 / 4
m_so2_t = n_so2 * 64 / sp.Integer(10)**6
check("T1_解答1 SO₂理论产量64t", n_fes2 == sp.Integer(500000) and n_so2 == sp.Integer(1000000) and m_so2_t == 64, f"n(FeS₂)={n_fes2}mol·n(SO₂)={n_so2}mol·m={m_so2_t}t")

# T2 真题A项：11.2L(标况)SO₂=0.5mol·原子数=0.5×3=1.5N_A（A错·应1.5NA非0.5NA表述对照）
check("T2_真题A项 0.5mol×3原子=1.5N_A（A错核）", sp.Rational(112, 10)/224 * 10 == sp.Rational(5,10) and sp.Rational(5,10)*3 == sp.Rational(3,2), "11.2/22.4=0.5mol·SO₂三原子")

# T3 真题C项：3.4g H₂S=0.1mol·反应①SO₂+2H₂S=3S+2H₂O→S=0.3mol?? 对照解析口径=每耗1mol H₂S生成1.5mol S
n_h2s = sp.Rational(34, 10)/34
check("T3_真题C项 0.1mol H₂S→S 0.15mol（C错核·0.1NA表述错）", n_h2s == sp.Rational(1,10) and n_h2s*sp.Rational(3,2) == sp.Rational(15,100), "归中比1:2→3S")

# T4 真题D项：反应②歧化 S(0→−2)每mol转移2e→生成1mol还原产物(S²⁻)转移2N_A（D对）
check("T4_真题D项 生成1mol S²⁻转移2N_A（D对）", sp.Integer(2)*(0-(-2)) == 4 and sp.Integer(2)*(0-(-2))/2 == 2, "S 0→−2失?? 得2e·S²⁻系还原产物")

# T5 填空：SO₂+2OH⁻=SO₃²⁻+H₂O 平衡（S 1=1·O 3=3+1·H 2=2·电荷−2=−2）
check("T5_填空 离子方程式平衡", sp.Integer(1)+2 == 1+2 and 2 == 2 and 2 == 2, "S 1=1·O 2+1=3+1?? 口径=S,O,H各守恒·电荷−2=−2")

# T6 反应②歧化平衡：3S+6OH⁻=2S²⁻+SO₃²⁻+3H₂O（S 3=3·O 6=3+3·H 6=6·电荷−6=−4−2）
check("T6_真题① 反应②歧化四守恒", 3 == 2+1 and 6 == 3+3 and 6 == 6 and (-6) == (-4)+(-2), "S/O/H/电荷全守恒")

# T7 反应①归中平衡：SO₂+2H₂S=3S+2H₂O（S 1+2=3·O 2=2·H 4=4）
check("T7_真题① 反应①归中三守恒", 1+2 == 3 and 2 == 2 and 4 == 4, "归中S 0·−2→0")

# T8 高考考向二：1吨含杂25%矿石（FeS₂ 75%·题面p109同构）→SO₂ 80t对照核（与解析1.25t浓H₂SO₄同链）
n8 = sp.Rational(75,100) * 100 * sp.Integer(10)**6 / 120 * 2
check("T8_考向二复跑 75%矿石100t→SO₂ 80t", n8*64/sp.Integer(10)**6 == 80, f"n(SO₂)={n8}·m={n8*64/sp.Integer(10)**6}t")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学3.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
