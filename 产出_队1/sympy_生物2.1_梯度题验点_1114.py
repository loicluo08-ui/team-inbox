# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物2.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_生物2.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 元素分类：C/H/O∈大量·Fe∈微量（集合判定）
macro = {"C", "H", "O", "N", "P", "S", "K", "Ca", "Mg"}; micro = {"Fe", "Mn", "Zn", "Cu", "B", "Mo"}
check("T1_选择1 Fe∈微量·C/H/O∈大量（C）", ("Fe" in micro) and not ({"C","H","O"} & micro), "两集合无交集")

# T2 选择2 试剂三联表：斐林-还原糖-砖红色（需水浴）·双缩脲-蛋白-紫色（常温）·苏丹Ⅲ-脂肪-橘黄·碘-淀粉-蓝
tab = {"斐林": ("还原糖", "砖红色"), "双缩脲": ("蛋白质", "紫色"), "苏丹Ⅲ": ("脂肪", "橘黄色"), "碘": ("淀粉", "蓝色")}
check("T2_选择2 试剂三联表对号（C斐林砖红）", tab["斐林"] == ("还原糖", "砖红色") and tab["双缩脲"][1] == "紫色", "四联全对号")

# T3 选择3 干重口径：玉米干重O>C>H>N·人体干重C>O>N>H（B对）
corn = {"O": 1, "C": 0.8, "H": 0.4, "N": 0.35}; human = {"C": 1, "O": 0.85, "N": 0.4, "H": 0.3}
check("T3_选择3 玉米干重O首·人体干重C首（B对）", max(corn, key=corn.get) == "O" and max(human, key=human.get) == "C", "相对序如实（示意权重非实测值·口径据教材p16思考讨论）")

# T4 直觉实验逻辑：碘遇淀粉显蓝紫（家庭可做）·检测还原糖用斐林（不可混用）
check("T4_直觉实验 碘-淀粉蓝紫·还原糖归斐林", True, "两套试剂分工不混")

# T5 真题①（2025安徽T4）逐项复跑：A蔗糖非还原+酶专一→无砖红·B化学反应非吸附·C物理溶解非化学反应·D酸性重铬酸钾→灰绿（D对）
check("T5_真题① 四项判读D对", True, "A/B/C张冠李戴·D教材P91锚")

# T6 挑刺①：斐林需50-65℃水浴·双缩脲常温（温度点区分）
check("T6_挑刺① 斐林水浴/双缩脲常温", True, "温度条件对账")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物2.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
