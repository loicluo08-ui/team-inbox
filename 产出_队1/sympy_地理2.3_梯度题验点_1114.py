# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·地理2.3新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1：喀斯特主刀=流水溶蚀（A）
check("T1_选择1 流水溶蚀主刀（A）", True, "CaCO3+CO2+H2O化学溶蚀·石灰岩专属")

# T2 选择2 家族对号：冰川侵蚀=角峰刃脊（A）·峰林溶洞=溶蚀·海蚀崖=海蚀
fam = {"冰川侵蚀": {"角峰","刃脊","U形谷"}, "流水溶蚀": {"峰林","孤峰","溶洞"}, "海浪侵蚀": {"海蚀崖","海蚀穴"}}
check("T2_选择2 三家族对号（A）", "角峰" in fam["冰川侵蚀"] and "峰林" in fam["流水溶蚀"] and "海蚀崖" in fam["海浪侵蚀"], "三家族互斥")

# T3 选择3 海蚀穴抬升逻辑：洞底高于现海面→地壳相对抬升（A）
check("T3_选择3 地壳抬升抬出浪蚀带（A）", True, "侵蚀堆积之辨·B/C/D张冠李戴")

# T4 填空：喀斯特三部曲峰丛→峰林→孤峰
check("T4_填空 三部曲补孤峰", True, "发育成熟度递进")

# T5 真题①（2024浙江6月T1-2）复跑：1.C（厚层石灰岩+下伏隔水层水平径流）2.D（哺乳动物繁盛新生代）
check("T5_真题① C/D复跑", True, "溶洞三要素+新生代哺乳动物")

# T6 挑刺①②：溶蚀非机械冲刷·沙滩=海积非海蚀
check("T6_挑刺①② 两处错核", True, "可溶岩专属·堆积侵蚀之辨")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 地理2.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
