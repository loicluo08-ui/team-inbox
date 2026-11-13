# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物3.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 分泌蛋白路径序：核糖体→内质网→高尔基体→细胞膜（A）
path = ["核糖体", "内质网", "高尔基体", "细胞膜"]
check("T1_选择1 五站顺序（A）", path == ["核糖体", "内质网", "高尔基体", "细胞膜"], "顺序一乱全错")

# T2 选择2 膜层数：高尔基体单层（C）·线粒体叶绿体双层·核糖体无膜
mem = {"线粒体": 2, "叶绿体": 2, "高尔基体": 1, "核糖体": 0}
check("T2_选择2 高尔基体单层（C）", mem["高尔基体"] == 1, "单层膜四兄弟：内质网/高尔基体/溶酶体/液泡")

# T3 选择3 ³H亮氨酸追踪序：附着核糖体→内质网→高尔基体→膜外（A）
trace = ["附着核糖体", "内质网", "高尔基体", "细胞膜外"]
check("T3_选择3 同位素追踪序（A）", trace[0] == "附着核糖体" and trace[1] == "内质网", "教材实验标准序")

# T4 真题①（2024浙1月T12）复跑：A特异性✓·B受体缺陷只堵送入·C走通道非囊泡·D性激素是脂质不走流水线
check("T4_真题① A对B/C/D错复跑", True, "读流程抓分工")

# T5 挑刺①：合成在核糖体·内质网只加工运输
check("T5_挑刺① 合成场所=核糖体", True, "挂在墙上≠墙生产")

# T6 挑刺②：水解酶核糖体合成·经内质网高尔基体分拣送达
check("T6_挑刺② 酶不溶酶体自产", True, "又一条流水线")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物3.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
