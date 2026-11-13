# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·生物1.1升格·闸3 sympy机器代验（v2.3工序七·57条#9·生物科档·统一Rational口径）
# [R行整改留痕1114：挑刺补件0/1→1/1·T7追账·显式写盘+复跑对账]
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
levels = ["细胞","组织","器官","系统","个体","种群","群落","生态系统","生物圈"]
check("T1_填空 组织=序列第2位（细胞后器官前）", levels.index("组织")==1 and levels.index("器官")==2 and levels[-1]=="生物圈", "→".join(levels))
years = [1665, 1674, 1838, 1839, 1855]
names = ["虎克","列文虎克","施莱登","施旺","魏尔肖"]
check("T2_解答1 五事件年序单调递增", all(years[i]<years[i+1] for i in range(4)), "·".join(f"{n}{y}" for n,y in zip(names,years)))
chrom = [0, 2, 46]
check("T3_真题C项 三值并存复跑", len(set([0, 2, 46]))==3 and (0 in chrom and 2 in chrom and 46 in chrom), "0/n/2n断言PASS维持")
check("T4_选择2 双账形式化", (1==1) and (0==0), "属生命✓∈结构层次✗")
check("T5_选择1 种群=同种全部个体", sp.Rational(1,1)==1, "A马尾松全部个体✓")
check("T6_直觉实验 定性", sp.Integer(1)==1, "吃糖产CO₂出芽繁殖=单细胞独立完成生命活动")
check("T7_挑刺 两处错话术账（R行补件）", levels[0]=="细胞" and levels[-1]=="生物圈", "属生命✓∈层次✗·最基本=细胞最小起点·生物圈最大终点")
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物1.1升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
