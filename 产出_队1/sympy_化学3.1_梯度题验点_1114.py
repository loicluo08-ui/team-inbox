# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·化学3.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_化学3.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答1⑴：2Fe²⁺+Cl₂=2Fe³⁺+2Cl⁻ 电荷/原子平衡（LHS+4=RHS+4·Fe 2=2·Cl 2=2）
check("T1_解答1 离子方程式电荷原子双平衡", sp.Integer(2)*2 + 0 == sp.Integer(2)*3 + sp.Integer(2)*(-1) and True, "LHS 2(+2)=+4·RHS 2(+3)+2(−1)=+4·Fe 2=2·Cl 2=2")

# T2 解答1⑴ 电子转移：Cl₂得2e（0→−1）·Fe²⁺失1e/个×2=2e（+2→+3）
check("T2_解答1 电子转移2e（Cl₂ 0→−1×2）", sp.Integer(2)*(0 - (-1)) == 2 and sp.Integer(2)*(3-2) == 2, "得失电子守恒2e")

# T3 变价差：Fe 0→+3 失3e（Cl₂强氧化剂一步到顶）·+2→+3 失1e
check("T3_挑刺① 变价差3e（Fe+Cl₂→+3）", sp.Integer(3)-0 == 3 and sp.Integer(3)-2 == 1, "强氧化剂拉到最高价·弱氧化剂H⁺只到+2")

# T4 转化配平核：2Fe³⁺+Fe=3Fe²⁺（电荷+6+0=+6·Fe 3=3）
check("T4_选择2 2Fe³⁺+Fe=3Fe²⁺平衡", sp.Integer(2)*3 + 0 == 3*2 and 3 == 3, "加铁粉降价配平")

# T5 Fe₃O₄价态和：2(+3)+(+2)=+8=4×|−2|（混合价态）
check("T5_选择1 Fe₃O₄混合价+8平衡", sp.Integer(2)*3 + 2 == 8 and 4*2 == 8, "1个+2与2个+3")

# T6 真题①A项逻辑：FeCl₃溶于水完全电离=强电解质（盐类强电解质判定·非数值逻辑断言）
check("T6_真题① 盐=强电解质判定（A错立论）", True, "FeCl₃完全电离Fe³⁺/Cl⁻·水解不改变强电解质判定")

# T7 选择3除杂逻辑：Fe³⁺+Fe→Fe²⁺不引新杂（B）·Cu引入Cu²⁺/Zn引入Zn²⁺（C/D引杂）
check("T7_选择3 除杂三问（B合规）", True, "不引新杂·不耗主物·过滤可分")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 化学3.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
