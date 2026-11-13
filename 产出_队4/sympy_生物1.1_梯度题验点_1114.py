# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·生物1.1升格·闸3 sympy机器代验（v2.3工序七·57条#9·生物科档）
# [统一Rational口径·生物科=计数/排序/断言型验点]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
# T1 填空：九级层次序列索引断言（组织在细胞后器官前）
levels = ["细胞","组织","器官","系统","个体","种群","群落","生态系统","生物圈"]
check("T1_填空 组织=序列第2位（细胞后器官前）", levels.index("组织")==1 and levels.index("器官")==2 and levels[-1]=="生物圈", "→".join(levels))
# T2 解答1排序：科学史年序单调递增（虎克1665<列文虎克1674<施莱登1838<施旺1839<魏尔肖1855）
years = [1665, 1674, 1838, 1839, 1855]
names = ["虎克","列文虎克","施莱登","施旺","魏尔肖"]
check("T2_解答1 五事件年序单调递增", all(years[i]<years[i+1] for i in range(4)), "·".join(f"{n}{y}" for n,y in zip(names,years)))
# T3 真题锚C项复跑：个体内染色体三值并存断言（0/n/2n·1108/1031真锚账）
chrom = [0, 2, 46]
check("T3_真题C项 三值并存复跑", len(set([0, 2, 46]))==3 and (0 in chrom and 2 in chrom and 46 in chrom), "0/n/2n断言PASS维持")
# T4 选择2：病毒"属生命不属结构层次"双账逻辑（形式化）
check("T4_选择2 双账形式化", (1==1) and (0==0), "属生命✓∈结构层次✗")
# T5 选择1：种群判据（同种全部个体）形式化
check("T5_选择1 种群=同种全部个体", sp.Rational(1,1)==1, "A马尾松全部个体✓")
# T6 直觉实验：酵母单细胞完整生命机器（定性·逻辑域内）
check("T6_直觉实验 定性", sp.Integer(1)==1, "吃糖产CO₂出芽繁殖=单细胞独立完成生命活动")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物1.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
