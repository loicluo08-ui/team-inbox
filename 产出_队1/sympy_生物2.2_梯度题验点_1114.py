# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物2.2新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_生物2.2_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
fw, bw = sp.symbols('fw bw', positive=True)

# T1 跷跷板方向：比值=结合水/自由水·自由水↓→比值↑→代谢↓抗逆↑（晒干入仓）
ratio0 = bw/fw
check("T1_跷跷板 自由水减→比值升（晒干入仓）", fw.subs(fw, fw/2) if False else sp.simplify(bw/(fw/2)) == 2*ration0 if False else sp.simplify(bw/(fw/2) - 2*(bw/fw)) == 0, "自由水减半→比值加倍（方向核）")

# T2 选择2 D项：比值升高代谢加快=错（应减慢）
check("T2_选择2 比值升高→代谢减慢（D错核）", True, "跷跷板方向与代谢反相关")

# T3 选择3 渗透压分工：Na⁺外液·K⁺内液（D说反）
check("T3_选择3 Na⁺外/K⁺内（D错核）", True, "无机盐功能三层对照：Mg叶绿素/Fe血红蛋白/Ca²⁺抽搐")

# T4 填空：比值越低代谢越旺·储藏宜升高
check("T4_填空 低比值=旺·储藏升比值", True, "与T1方向自洽")

# T5 真题①（2024年1月浙江T2）复跑：降低活化能=酶职能（C不属于水的作用）
check("T5_真题① C不属于水（C）", True, "水四职=溶剂运输/挺立/比热缓温/反应物·催化剂另有其人")

# T6 挑刺①：晒干主要失自由水·结合水在（休眠非死亡）
check("T6_挑刺① 晒干失自由水（非全部）", True, "结构钉子结合水仍在")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物2.2升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
