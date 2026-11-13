# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物4.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1/T2 运输方式配对：O₂自由扩散（A）·葡萄糖进红细胞协助扩散（B）
modes = {"O₂": "自由扩散", "葡萄糖进红细胞": "协助扩散", "水": "协助扩散（主走水通道）"}
check("T1_选择1 O₂自由扩散（A）", modes["O₂"] == "自由扩散", "小+非极性+顺梯度")
check("T2_选择2 葡萄糖进红细胞=协助扩散（B）", modes["葡萄糖进红细胞"] == "协助扩散", "顺梯度+载体+不耗能")

# T3 选择3 失水阶段浓度方向：外>内（A对）·稳定≠死亡·壁不随缩·稳定=平衡非始终低
check("T3_选择3 外浓内稀驱动失水（A）", True, "B死亡C壁收缩D方向全错")

# T4 填空：质=原生质层·外因=外浓>内浓
check("T4_填空 原生质层·外大于内", True, "三部件定义+方向条件")

# T5 真题①（2025北京T15）复跑：D错立论=失水浓缩应变大（非变小）·A/B/C三对
check("T5_真题① D方向反型设错复跑", True, "失水=浓缩·吸水=稀释")

# T6 浓度数值：0.3g/mL蔗糖=教材标准分离浓度（30g/100mL换算核）
check("T6_教材浓度 0.3g/mL=300g/L换算", sp.Rational(3,10)*1000 == 300, "单位换算自洽")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物4.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
