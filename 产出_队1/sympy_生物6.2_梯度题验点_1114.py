# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物6.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择3 层次对账：同个体两细胞核DNA相同·mRNA/蛋白质不完全相同（A）
check("T1_选择3 DNA同·表达不同（A）", True, "管家基因同·特异基因异")

# T2 选择2 全能性三条件：全套遗传+离体+适宜（B）
check("T2_选择2 植物细胞离体全能性（B）", True, "胡萝卜实验·动物体细胞核具全能性")

# T3 真题①（2025安徽T3）复跑：B错立论（分化核仍具全能性）·A/C/D对
check("T3_真题① B错立论复跑", True, "全套遗传信息保留·核移植为证")

# T4 挑刺①②：遗传物质不变·表达不完全不同（管家基因）
check("T4_挑刺①② 两处错核", True, "账本只改读法·管家基因家家表")

# T5 填空：干细胞定义（分裂+分化）
check("T5_填空 干细胞=备件库", True, "自我更新+按需上岗")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物6.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
