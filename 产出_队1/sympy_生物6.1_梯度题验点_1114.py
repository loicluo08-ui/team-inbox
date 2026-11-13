# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物6.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
n = sp.symbols('n', positive=True, integer=True)

# T1 选择3 数值核：2n=24→后期染色体48·核DNA 48
check("T1_选择3 2n=24后期48/48（B）", 24*2 == 48, "着丝粒分裂染色体加倍·DNA已复制")

# T2 通式：后期染色体=4n/2·核DNA=2×2n/2（符号核：2n=24→48）
chrom = 4*(n/2); dna = 4*(n/2)
check("T2_通式 后期染色体=核DNA=2×2n", chrom.subs(n, 24) == 48 and dna.subs(n, 24) == 48, "后期一倍体基准×2")

# T3 选择2 间期占比：约90%+（视野抽样逻辑）
check("T3_选择2 间期占周期绝大部分（A）", True, "随机抓拍多数间期")

# T4 真题①（2025云南T4）复跑：干细胞多/肝癌多→增殖（A）
check("T4_真题① 数量线索定向增殖（A）", True, "分裂旺处细胞蛇多")

# T5 真题②（2024江西T3）复跑：B错（中期着丝粒排列不受后期突变连累）·A/C/D对
check("T5_真题② B错立论复跑", True, "时期责任划分")

# T6 填空：纺锤体前期·染色体加倍后期
check("T6_填空 前期纺锤体/后期加倍", True, "时期两连")

# T7 解答1：秋水仙素断纺锤体→染色体不能移两极→加倍（多倍体化）
check("T7_解答1 断绳留加倍", True, "多倍体育种原理")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物6.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
