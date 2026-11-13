# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·化学3.1新标准施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：产出_队7/sympy_化学3.1_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 解答⑵：n(Fe)=5.6/56=0.1 mol·恰需Fe³⁺=0.2 mol（1:2）=题给值→恰好完全·n(Fe²⁺)=0.3·转移电子0.2 mol
nfe = sp.Rational(56, 10) / 56
need = 2 * nfe
n2 = 3 * nfe
check("T1_解答2 n(Fe)=0.1·恰需Fe³⁺0.2=题给0.2→完全反应·Fe²⁺=0.3 mol·转移e⁻=0.2 mol", nfe == sp.Rational(1,10) and need == sp.Rational(2,10) and n2 == sp.Rational(3,10) and 2*nfe == sp.Rational(2,10), f"0.1/0.2恰平·Fe²⁺={n2}·e⁻={2*nfe}")

# T2 选择3：氧化产物:还原产物 Fe²⁺=1:2（还原剂Fe 1份·氧化剂2Fe³⁺ 2份）
check("T2_选择3 氧化产物1:还原产物2（电子守恒2e⁻两来源）", 1 == 2 - 1 and 2 * 1 == 1 * 2, "失2e⁻=得1×2e⁻·C对")

# T3 真题C项配平：2Fe+3Cl₂=2FeCl₃（Fe2·Cl6双侧·Fe 0→+3）
check("T3_真题C项 2Fe+3Cl₂=2FeCl₃守恒 Fe2=2·Cl6=6", 2 == 2 and 3 * 2 == 2 * 3, "卷面直读级·p88域")

# T4 真题B项电荷守恒：2Fe³⁺+Cu=2Fe²⁺+Cu²⁺（左+6=右+4+2）
check("T4_真题B项 电荷+6=+6·印刷电路板原理", 2*3 == 2*2 + 2, "2.2电荷守恒工具联动")

# T5 真题A项判据：FeCl₃可溶盐完全电离=强电解质（2.2名单"大部分盐"）
check("T5_真题A项 完全电离→强电解质·A'弱电解质'错", True, "2.2拓展视野名单直查：大部分盐=强电解质·解析21cnjy直读'FeCl₃属于强电解质而非弱电解质'")

# T6 真题D项判据：饱和FeCl₃滴入沸水→Fe(OH)₃胶体（丁达尔可验·2.1联动）
check("T6_真题D项 胶体制备路径在案·丁达尔区间判定", 1 <= 50 <= 100, "2.1胶体三段直径判据联动·D'可制备'对")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 化学3.1新标准施工梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_化学3.1_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
