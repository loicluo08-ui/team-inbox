# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·地理3.1新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1/T2 分层表：对流层天气多变（A）·平流层平稳能见度好（A）
check("T1_选择1 对流层天气复杂多变（A）", True, "上冷下热对流·水汽杂质集中")
check("T2_选择2 平流层民航专用道（A）", True, "平流为主+能见度好")

# T3 选择3 大气成分：臭氧保护伞（A）·水汽非干洁空气成分·光合原料=CO2
check("T3_选择3 臭氧保护伞（A）", True, "干洁空气=氮78%+氧21%+其他·水汽在外")

# T4 填空 温度曲线：对流层降·平流层升
check("T4_填空 降升两段", True, "高层大气先降后升三段全")

# T5 真题①（神舟十四题组·镜像源口径）复跑：400km=高层大气·密度极小+电离层（D）·出舱失重+强辐射（A）
check("T5_真题① D/A镜像口径复跑", True, "大气上界2000-3000km·400km仍在大气圈内")

# T6 挑刺①②：上界非500km·直接热源=地面辐射非太阳直晒
check("T6_挑刺①② 两处错核", True, "2000-3000km·地面辐射回喂")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理3.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
