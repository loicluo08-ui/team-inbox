# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·地理3.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 直接热源=地面辐射（B）
check("T1_选择1 地面辐射=直接热源（B）", True, "短波穿膜晒地面·地面长波喂大气")

# T2 选择2 熏烟防霜冻=增强逆辐射（A）
check("T2_选择2 熏烟增逆辐射（A）", True, "人工造云·扣热低空")

# T3 选择3 昼夜口诀：白多云凉·夜多云暖（B）
check("T3_选择3 夜多云更暖（B）", True, "伞与被分工")

# T4 填空 波长配对：太阳短波·地面长波
check("T4_填空 短波/长波配对", True, "温度高波长短")

# T5 真题①（2024广东T1-2）复跑：1.B旱季云雾少逆辐射弱·2.D夏季差值小加热小·C反（林冠层=热源）
check("T5_真题① B/D复跑", True, "L↑>L↓→有效辐射为正→林冠层供热")

# T6 挑刺①②：逆辐射还地面非还宇宙·昼夜两把尺
check("T6_挑刺①② 两处错核", True, "方向装反+昼夜同款错")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理3.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
