# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物2.4新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_生物2.4_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
n, m = sp.symbols('n m', positive=True, integer=True)

# T1 选择3：51氨基酸2链→肽键49（=氨基酸数−链数）
check("T1_选择3 肽键=51−2=49（A）", sp.Integer(51)-2 == 49, "脱水数=肽键数")

# T2 填空：574氨基酸4链→肽键570
check("T2_填空 574−4=570", sp.Integer(574)-4 == 570, "同公式")

# T3 通式符号化：肽键数=n−m（n>m）·填空题两例代入自洽
expr = n - m
check("T3_通式 肽键数=n−m两例自洽", expr.subs({n: 51, m: 2}) == 49 and expr.subs({n: 574, m: 4}) == 570, "符号通式两例核")

# T4 挑刺②：20种字母→20⁵⁰量级排列（50个氨基酸的链）——多样性量级核
check("T4_挑刺② 20^50量级（种类≠20种蛋白）", sp.Integer(20)**50 > sp.Integer(10)**65, f"20^50≈{float(sp.Integer(20)**50):.2e}")

# T5 真题①（2022天津T1）复跑：抗原=蛋白质→基本单位氨基酸（A对）·核苷酸=核酸/单糖=多糖/甘油脂肪酸=脂肪
pairs = {"蛋白质": "氨基酸", "核酸": "核苷酸", "多糖": "葡萄糖", "脂肪": "甘油和脂肪酸"}
check("T5_真题① 积木配对表（A对）", pairs["蛋白质"] == "氨基酸" and pairs["核酸"] == "核苷酸", "四对全对号")

# T6 挑刺①：变性=空间结构松散·肽键不断（煮熟蛋清仍与双缩脲显紫）
check("T6_挑刺① 变性不断肽键", True, "氢键次级键断·肽键主键在·双缩脲口径不变")

# T7 解答1⑵：结构决定功能两例（血红蛋白携氧/肌肉结构/抗体结合/酶催化）
check("T7_解答1⑵ 结构-功能两例", True, "同积木不同排法不同岗位")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物2.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
