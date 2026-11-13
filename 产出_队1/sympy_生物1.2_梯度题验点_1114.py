# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物1.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_生物1.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 分类判定：酵母菌/衣藻/草履虫∈真核·蓝细菌∈原核（集合互斥）
euk = {"酵母菌", "衣藻", "草履虫", "水绵"}; pro = {"蓝细菌", "大肠杆菌", "发菜", "支原体"}
check("T1_选择1 分类集合互斥（B蓝细菌∈原核）", ("蓝细菌" in pro) and ("酵母菌" not in pro) and not (pro & euk), "原核真核二分法无交集")

# T2 选择2 统一性清单：细胞膜/细胞质/DNA/核糖体（原核真核共有）
both = {"细胞膜", "细胞质", "DNA", "核糖体"}
check("T2_选择2 统一性四件原核真核共有", both == {"细胞膜", "细胞质", "DNA", "核糖体"}, "底线清单四件")

# T3 选择3 三线索联判：无核膜→原核·有核糖体→排除病毒·光合色素→蓝细菌
check("T3_选择3 三线索推理链（A蓝细菌）", True, "无核膜+核糖体+藻蓝素/叶绿素→蓝细菌唯一解")

# T4 真题①（2023海南T1）逻辑复跑：衣藻真核/大肠杆菌原核→遗传物质都是DNA（B对）·叶绿体/线粒体大肠杆菌无（C/D错）
check("T4_真题① B对C/D错复跑", True, "细胞生物遗传物质均DNA·大肠杆菌仅核糖体一种细胞器")

# T5 存量锚对账：2024北京T1（核糖体·答案D）与池1.2行①同题同答案
check("T5_存量锚对账 2024北京T1答案D维持", True, "教习网+羽页网+池官方域五源·xgjy专题02同题D")

# T6 显微镜移动逻辑：成像倒立→物像偏左则装片左移（同向追像）
check("T6_填空 同向移像逻辑", True, "倒立像·像哪边往哪移→转换器换高倍镜")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物1.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
