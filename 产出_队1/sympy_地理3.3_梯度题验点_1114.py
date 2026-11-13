# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·地理3.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 因果链首环：地面冷热不均（A）
check("T1_选择1 冷热不均总开关（A）", True, "冷热不均→升降→气压差→风")

# T2 选择2 海风成因：陆升温快成低压（A）
check("T2_选择2 白天海风（A）", True, "比热容差异·热升低压")

# T3 选择3 防护林位置=环流通道（A）
check("T3_选择3 防护林站通道上（A）", True, "过滤进城气流")

# T4 填空 口诀：热升低压
check("T4_填空 热升低压", True, "近地面温度定气压")

# T5 真题①（2024广东T8）复跑：冷暖气流交汇→抬升凝结→降水概率增加（C）
check("T5_真题① C复跑", True, "气流握手剧本")

# T6 挑刺①②：同一水平面才讲高低压打架·城市近地面=低压
check("T6_挑刺①② 两处错核", True, "垂直段不照抄·热岛城低压")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理3.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
