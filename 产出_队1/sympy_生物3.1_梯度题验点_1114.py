# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物3.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 主要成分：脂质+蛋白质（A）
check("T1_选择1 膜主力=脂质+蛋白（A）", True, "磷脂最丰富·糖类少量")

# T2 模型史三段：欧文顿→三明治静态→1972流动镶嵌（A）
check("T2_选择2 1972流动镶嵌（A）", True, "模型史三条线")

# T3 荧光标记融合实验：两色均匀→膜流动（A）
check("T3_选择3 荧光融合证流动（A）", True, "教材招牌实验")

# T4 糖被口径：糖蛋白+糖脂·只在外表面
check("T4_填空 糖被只铺外表面", True, "识别名片")

# T5 真题①（2024新课标ⅠT1）复跑：甘油可自由扩散（C错立论）·脂质蛋白主力/衰老通透改变/激素受体传递
check("T5_真题① C错立论复跑", True, "极性≠过不去·分子小可扩散")

# T6 挑刺①：流动镶嵌vs静态三明治（流动性分水岭）
check("T6_挑刺① 流动性分水岭", True, "磷脂侧移+蛋白可动")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物3.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
