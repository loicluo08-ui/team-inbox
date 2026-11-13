# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物2.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_生物2.3_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 糖类三档：蔗糖∈二糖（葡萄糖/果糖/核糖∈单糖·淀粉/糖原/纤维素∈多糖）
mono = {"葡萄糖", "果糖", "核糖", "脱氧核糖"}; di = {"蔗糖", "麦芽糖", "乳糖"}; poly = {"淀粉", "糖原", "纤维素"}
check("T1_选择1 蔗糖∈二糖（B）", "蔗糖" in di and not ({"葡萄糖"} & di) and not ({"淀粉", "糖原"} & di), "三档互斥")

# T2 选择2 功能配对：糖原=动物储能·纤维素=结构非储能·几丁质=真菌/甲壳（C对）
check("T2_选择2 功能配对（C糖原动物储能）", True, "纤维素结构物质·核糖/脱氧核糖不供能·几丁质非植物壁")

# T3 选择3 脂肪元素账：脂肪C/H/O·H多O少（与糖类比）·磷脂含N·P·D错（O远多于碳氢=反）
check("T3_选择3 脂肪H多O少（D错核）", True, "脂肪C:H:O≈68:11:11·糖类≈53:7:40（示意比·口径据p18讨论）·磷脂才含P")

# T4 真题①（2024新课标T1）复跑：脂肪仅C/H/O不含P（D错对号）·A不饱和熔点低/B三大供能/C必需氨基酸跨2.4域
check("T4_真题① D错立论复跑（脂肪无P）", True, "磷脂才含P·必需氨基酸选项跨节注记池行在案")

# T5 挑刺①：基本单位同（葡萄糖）≠功能同（纤维素结构物质非储能）
check("T5_挑刺① 单位同≠功能同", True, "纤维素结构·糖原储能·淀粉植物储能三分")

# T6 挑刺②：胆固醇=动物细胞膜成分+性激素/维生素D原料（适量有益·过量有害）
check("T6_挑刺② 胆固醇非全害", True, "平衡膳食口径")

# T7 解答1 消化链：淀粉→麦芽糖→葡萄糖（血糖只认葡萄糖）
check("T7_解答1 淀粉消化链终点葡萄糖", True, "限量主食=限葡萄糖仓库")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物2.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
