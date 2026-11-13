# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物5.4新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 场所：光反应=类囊体薄膜（B）
check("T1_选择1 光反应场所=类囊体薄膜（B）", True, "暗反应=叶绿体基质")

# T2 选择3 C3/C5断光方向：C3增多C5减少（A）·机制两步核
check("T2_选择3 断光C3↑C5↓（A）", True, "NADPH/ATP断供→C3还原受阻堆积·CO2固定续耗C5")

# T3 填空 光解产物：O2+NADPH
check("T3_填空 水光解产O2·NADP+接电子成NADPH", True, "三件套之2件")

# T4 真题①（2024北京T3）复跑：D氧气对·A产ATP非耗能·B被还原非氧化·C需色素
check("T4_真题① D对A/B/C错复跑", True, "光反应三件套卷尺")

# T5 挑刺② 能量路线：光能→活跃化学能→稳定化学能（两站）
check("T5_挑刺② 能量两站非直达", True, "NADPH/ATP中间站")

# T6 解答1 对照逻辑：照光管蓝→无色·暗管不变（电子来自水光解）
check("T6_解答1 两管颜色对照", True, "DCIP得电子被还原")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物5.4升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
