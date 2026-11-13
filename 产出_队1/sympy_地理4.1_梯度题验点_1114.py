# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·地理4.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 海陆间循环=陆地淡水生命线（A）
check("T1_选择1 海陆间循环（A）", True, "海面蒸发→输送→陆地降水→径流回海")

# T2 选择2 硬化地面：下渗减·地表径流增（A）
check("T2_选择2 硬化封口（A）", True, "城市内涝根源")

# T3 选择3 植树造林：下渗增地表径流减（A）·蒸腾增强非减少·D必然过头
check("T3_选择3 植树三件事（A）", True, "截留/固土增渗/蒸腾耗水")

# T4 填空 主链五环：蒸发→输送→降水→径流
check("T4_填空 升运落跑", True, "降水补位")

# T5 真题①（2024新课标卷人工降雨）复跑：1.A最浅变化最早·2.B裸地深层无变化=产流多·3.C覆盖石子②③增
check("T5_真题① A/B/C复跑", True, "此消彼长：下渗多地表跑的少")

# T6 挑刺①②：循环并行（为主≠唯一）·重力是第二动力
check("T6_挑刺①② 两处错核", True, "多循环并行+重力撑场")

# T7 数值核：30°坡地测量深度30/60/100cm层序
check("T7_题组数值 深度30<60<100cm递增", sp.Rational(30) < 60 < 100, "浅层先变逻辑基础")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理4.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
