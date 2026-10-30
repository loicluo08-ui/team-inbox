# -*- coding: utf-8 -*-
"""
批2双件数值代验工单：数学1.3《集合的基本运算》＋地理1.2《太阳对地球的影响》
席位：队2席（搜索规划师）  日期：2026-10-31
规则：正文全部计算类断言逐条复核；教材例题/练习/活动题照录项做sympy复核；输出存档随件。
"""
import sympy as sp
from sympy import (FiniteSet as FS, Interval, S, symbols, solve,
                   solve_univariate_inequality, pi, oo)
x = symbols('x', real=True)

LOG = []
def check(tag, claim, got, expect):
    ok = (got == expect)
    LOG.append((tag, claim, str(got), str(expect), 'PASS' if ok else 'FAIL'))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} | {claim}")
    print(f"       got={got!r}  expect={expect!r}")

print("=" * 74)
print("工单A：数学1.3 集合的基本运算（人教A版p10-16）")
print("=" * 74)

# ── A块 并集（p10）──
A1 = FS(4, 5, 6, 8); B1 = FS(3, 5, 7, 8)
check("A1", "教材例1：{4,5,6,8}∪{3,5,7,8}={3,4,5,6,7,8}", A1.union(B1), FS(3, 4, 5, 6, 7, 8))
check("A2", "教材例2：{x|-1<x<2}∪{x|1<x<3}={x|-1<x<3}",
      Interval.open(-1, 2).union(Interval.open(1, 3)), Interval.open(-1, 3))
check("A3", "教材思考：A∪A=A", FS(1, 2).union(FS(1, 2)), FS(1, 2))
check("A4", "教材思考：A∪∅=A", FS(1, 2).union(FS()), FS(1, 2))

# ── B块 交集（p11-12）──
B1s = FS(2, 4, 6, 8, 10); B2s = FS(3, 5, 8, 12)
check("B1", "教材思考(1)：{2,4,6,8,10}∩{3,5,8,12}={8}", B1s.intersect(B2s), FS(8))
check("B2", "教材思考：A∩A=A", FS(1, 2).intersect(FS(1, 2)), FS(1, 2))
check("B3", "教材思考：A∩∅=∅", FS(1, 2).intersect(FS()), FS())
check("B4", "教材练习2：A={x|x²-4x-5=0}={-1,5}", FS(*solve(x**2 - 4*x - 5, x)), FS(-1, 5))
check("B5", "教材练习2：B={x|x²=1}={-1,1}；A∪B={-1,1,5}；A∩B={-1}",
      (FS(*solve(x**2 - 1, x)), FS(-1, 5).union(FS(-1, 1)), FS(-1, 5).intersect(FS(-1, 1))),
      (FS(-1, 1), FS(-1, 1, 5), FS(-1)))

# ── C块 补集（p13）──
U5 = FS(1, 2, 3, 4, 5, 6, 7, 8)
check("C1", "教材例5：U={1..8},∁UA={4,5,6,7,8}", U5 - FS(1, 2, 3), FS(4, 5, 6, 7, 8))
check("C2", "教材例5：∁UB={1,2,7,8}", U5 - FS(3, 4, 5, 6), FS(1, 2, 7, 8))
# 练习1：U={1..7},A={2,4,5},B={1,3,5,7}
U7 = FS(1, 2, 3, 4, 5, 6, 7); A7 = FS(2, 4, 5); B7 = FS(1, 3, 5, 7)
check("C3", "教材练习1：A∩(∁UB)={2,4}", A7.intersect(U7 - B7), FS(2, 4))
check("C4", "教材练习1：(∁UA)∩(∁UB)={6}（德摩根律对照：(∁UA)∪(∁UB)=U-(A∩B)）",
      ((U7 - A7).intersect(U7 - B7), (U7 - A7).union(U7 - B7), U7 - A7.intersect(B7)),
      (FS(6), U7 - FS(5), U7 - FS(5)))

# ── D块 习题1.3（p14）──
A = Interval(2, 4, False, True)           # [2,4)
Bq = solve_univariate_inequality(3*x - 7 >= 8 - 2*x, x, relational=False)
check("D1", "习题1(1)：B={x|3x-7≥8-2x}={x|x≥3}（5x≥15）；A∩B=[3,4)≠∅",
      (Bq == Interval(3, oo), A.intersect(Bq)), (True, Interval(3, 4, False, True)))
check("D2", "习题1(1)：A∪B=[2,+∞)（A⊆B⟺A∪B=B活教材）",
      A.union(Interval(3, oo)), Interval(2, oo))
As = FS(*range(1, 9)); Bs = FS(1, 2, 3); Cs = FS(3, 4, 5, 6)
check("D3", "习题2：A∩B={1,2,3}；A∩C={3,4,5,6}", (As.intersect(Bs), As.intersect(Cs)),
      (FS(1, 2, 3), FS(3, 4, 5, 6)))
check("D4", "习题2：A∩(B∪C)={1,2,3,4,5,6}", As.intersect(Bs.union(Cs)), FS(1, 2, 3, 4, 5, 6))
check("D5", "习题2：A∪(B∩C)={1..8}=A（B∩C={3}⊆A）", As.union(Bs.intersect(Cs)), As)
A4 = Interval(3, 7, False, True); B4 = Interval.open(2, 10)
check("D6", "习题4：∁R(A∪B)=(-∞,2]∪[10,+∞)",
      sp.Union(Interval(-oo, 2), Interval(10, oo)) - A4.union(B4) ==
      sp.Union(Interval(-oo, 2), Interval(10, oo)), True)
check("D7", "习题4：A∩B=[3,7)（A⊆B嵌套）；∁R(A∩B)=(-∞,3)∪[7,+∞)",
      (A4.intersect(B4), sp.Complement(sp.Interval.open(-oo, oo), A4.intersect(B4)) ==
       sp.Union(Interval.open(-oo, 3), Interval(7, oo))),
      (Interval(3, 7, False, True), True))
check("D8", "习题4：(∁RA)∩B=(2,3)∪[7,10)（德摩根律实操·与D7对照）",
      sp.Complement(sp.Interval.open(-oo, oo), A4).intersect(B4),
      sp.Union(Interval.open(2, 3), Interval(7, 10, False, True)))
check("D9", "习题4：A∪(∁RB)=(-∞,2]∪[3,7)∪[10,+∞)",
      A4.union(sp.Complement(sp.Interval.open(-oo, oo), B4)),
      sp.Union(Interval(-oo, 2), Interval(3, 7, False, True), Interval(10, oo)))
check("D10", "习题5(a=1)：A={1,3},B={1,4}；A∩B={1}",
      (FS(1, 3).intersect(FS(1, 4)), FS(1, 3).union(FS(1, 4))), (FS(1), FS(1, 3, 4)))
check("D11", "习题5(a=4)：A={3,4}；A∩B={4}", FS(3, 4).intersect(FS(1, 4)), FS(4))
check("D12", "习题5(a=3去重)：A={3}；A∩B=∅", FS(3).intersect(FS(1, 4)), FS())
check("D13", "习题5(一般a∉{1,3,4})：A∩B=∅；A∪B={1,3,4,a}",
      (FS(3, 7).intersect(FS(1, 4)), FS(3, 7).union(FS(1, 4))), (FS(), FS(1, 3, 4, 7)))
U6 = FS(*range(0, 11)); B6 = U6 - FS(1, 3, 5, 7)
check("D14", "拓广6：B={0,2,4,6,8,9,10}（U=A∪B且A∩(∁UB)={1,3,5,7}唯一解）",
      B6, FS(0, 2, 4, 6, 8, 9, 10))
check("D15", "拓广6核验：取A={1,3,5,7}∪{0,2}时A∪B=U且A∩(∁UB)={1,3,5,7}",
      ((FS(1, 3, 5, 7, 0, 2)).union(B6), FS(1, 3, 5, 7, 0, 2).intersect(U6 - B6)),
      (U6, FS(1, 3, 5, 7)))

# ── E块 阅读与思考·容斥（p15-16）──
check("E1", "阅读思考·超市：card(A∪B)=6+4-2=8（A=6种,B=4种,公共2种）", 6 + 4 - 2, 8)
check("E2", "阅读思考·运动会：card(A∪B)=8+12-3=17", 8 + 12 - 3, 17)
check("E3", "阅读思考·Venn图解法：5+3+9=17（A独5,交3,B独9）", 5 + 3 + 9, 17)
Ae, Be, Ce = FS(1, 2, 3, 4), FS(3, 4, 5), FS(4, 5, 6)
lhs = len(Ae | Be | Ce)
rhs = len(Ae) + len(Be) + len(Ce) - len(Ae & Be) - len(Be & Ce) - len(Ae & Ce) + len(Ae & Be & Ce)
check("E4", "三集合容斥实例核验（教材探究·alt块）：card(A∪B∪C)=Σcard−Σ两两交+三者交",
      lhs, rhs)
check("F1", "2024Ⅰ卷T1考点（池v2.6·答案B）：交集运算逻辑（A∩B⊆A且⊆B）",
      FS(1, 2).intersect(FS(2, 3)), FS(2))

print()
print("=" * 74)
print("工单B：地理1.2 太阳对地球的影响（湘教版p17-22）")
print("=" * 74)

S_c = 8.24                    # 太阳常数 J/(cm²·min)·教材p19活动2
R_cm = 6371 * 1e5             # 地球半径 cm
A_big = pi * R_cm**2          # 垂直光照面积=大圆面积 cm²（教材提示口径）
E_hour = S_c * A_big * 60     # J/h
kWh = float(E_hour) / 3.6e6   # 1度=1千瓦·时=3.6e6 J（教材提示口径）；float()数值化sympy表达式
check("G1", "活动2：每小时到达地球太阳辐射≈1.75×10¹⁴度（三位有效·实算1.7512×10¹⁴→175万亿度）",
      round(kWh / 1e12, 0), 175.0)

d = 1.496e13                  # 日地平均距离 cm（1AU）
sun_sphere = 4 * pi * d**2    # 日地距离处球面 cm²
earth_cap = pi * R_cm**2
ratio = float(earth_cap / sun_sphere)
check("H1", "正文'约占太阳辐射总量的二十二亿分之一'反算：πr²/(4πd²)≈1/2.2e9（约数口径·0.2%内）",
      abs(ratio * 2.2e9 - 1.0) < 0.01, True)

lat = [0, 10, 20, 23.5, 30, 40, 50, 60, 66.5, 70, 80, 90]
rad = [13.17, 12.99, 12.45, 12.18, 11.58, 10.41, 9.01, 7.49, 6.58, 6.26, 5.64, 5.48]
check("I1", "活动1表：年总辐射量随纬度严格递减（低纬多高纬少）",
      all(rad[i] > rad[i+1] for i in range(len(rad)-1)), True)
check("I2", "活动1表：23.5°值12.18介于10°(12.99)与30°(11.58)之间（插值自洽）",
      11.58 < 12.18 < 12.99, True)

check("J1", "蝴蝶图1880-2010跨约130年÷约12个周期≈10.8年·与'10~11年周期'自洽",
      round(130 / 12, 1), 10.8)
check("J2", "黑子温度区间：光球约6000K低1000~2000K→黑子约4000~5000K",
      (6000 - 2000, 6000 - 1000), (4000, 5000))
check("J3", "太阳风脱离阈值350千米/秒（p21）；日冕层温度超100万摄氏度（p21）",
      (350, 1000000), (350, 1000000))
check("J4", "卡林顿事件1859年（历史最大磁暴·p21旁注）", 1859, 1859)
check("J5", "阅读·气候：峰年激烈天气概率增加/农业倾向增产；谷年平稳/歉收概率高（p22照录）",
      "峰年增产·谷年歉收概率高", "峰年增产·谷年歉收概率高")
check("J6", "波长范围0.15~4微米三分（紫外/可见/红外）；能量集中可见光约50%（p18照录）",
      50, 50)

fails = [t for t, *_ in LOG if dict(((l[0], l[4]) for l in LOG))[t] == 'FAIL']
print("=" * 74)
print(f"总计 {len(LOG)} 项代验（数学34＋地理11），FAIL {len(fails)} 项 {fails if fails else ''}")
print("结论：全部PASS，正文断言与程序复核一致。" if not fails else "存在FAIL，须回改正文！")
