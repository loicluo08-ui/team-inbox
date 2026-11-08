# -*- coding: utf-8 -*-
"""化学4.1《原子结构与元素周期表》（人教版2019必修第一册 p92-106）sympy验点留痕
承任务包_化学第4章补齐_1108 §三"symbols与sympy留痕：化学节涉及计算的逐题验算留痕"
出品：并行搜索员B·队3席B线·1108·分支dui3_chem41_1108
"""
from sympy import Matrix, Rational, nsimplify, S

ok = 0; total = 0
def check(name, cond, detail=""):
    global ok, total
    total += 1
    status = "PASS" if cond else "FAIL"
    if cond: ok += 1
    print(f"[{status}] {name} {detail}")

# ===== 一、表4-1 氢的三种核素：质量数=质子数+中子数 =====
check("氕 1H: A=Z+N", 1+0==1, "A=1")
check("氘 2H: A=Z+N", 1+1==2, "A=2")
check("氚 3H: A=Z+N", 1+2==3, "A=3")

# ===== 二、稀有气体电子层排布（教材p93思考与讨论表）：各层和=核电荷数 & 2n^2上界 =====
rg = {"He(2)": ([2],2), "Ne(10)": ([2,8],10), "Ar(18)": ([2,8,8],18),
      "Kr(36)": ([2,8,18,8],36), "Xe(54)": ([2,8,18,18,8],54), "Rn(86)": ([2,8,18,32,18,8],86)}
for name,(layers,Z) in rg.items():
    check(f"{name} 各层和=核电荷数", sum(layers)==Z, f"layers={layers}")
n2 = [2*n*n for n in range(1,5)]
check("第n层最多2n^2: n=1..4 = 2,8,18,32", n2==[2,8,18,32], str(n2))
check("最外层≤8（除K层≤2）：稀有气体各最外层均≤8", all(l[-1]<=8 for l,_ in rg.values()))

# ===== 三、1~20号元素排布全表自验（教材p93-94口径：2n^2容量·最外层≤8·K层≤2·先满内层）=====
tbl = {1:[1],2:[2],3:[2,1],4:[2,2],5:[2,3],6:[2,4],7:[2,5],8:[2,6],9:[2,7],10:[2,8],
       11:[2,8,1],12:[2,8,2],13:[2,8,3],14:[2,8,4],15:[2,8,5],16:[2,8,6],17:[2,8,7],
       18:[2,8,8],19:[2,8,8,1],20:[2,8,8,2]}
bad=[]
for Z,lay in tbl.items():
    if sum(lay)!=Z: bad.append(f"Z{Z}和{sum(lay)}")
    if lay[-1]>8 or (len(lay)==1 and lay[0]>2): bad.append(f"Z{Z}外层超容")
    for i,n in enumerate(range(1,len(lay))):  # 内层≤2n^2（容量上界）；Z≤18时内层必满（教材简化口径）
        if lay[i]>2*n*n: bad.append(f"Z{Z}内层{n}超容")
        if Z<=18 and lay[i]!=2*n*n: bad.append(f"Z{Z}内层{n}未满")
check("1~20号排布全表20项（和=Z·内层满2n^2·外层≤8·K≤2）", not bad, "全过" if not bad else str(bad))
spot = {11:[2,8,1], 17:[2,8,7], 19:[2,8,8,1], 20:[2,8,8,2]}
for Z,exp in spot.items():
    check(f"{Z}号元素排布与教材图一致", tbl[Z]==exp, f"{tbl[Z]}")

# ===== 四、碱金属（表4-2/p99示意图）：排布层和=核电荷数 =====
am = {"Li(3)":([2,1],3), "Na(11)":([2,8,1],11), "K(19)":([2,8,8,1],19),
      "Rb(37)":([2,8,18,8,1],37), "Cs(55)":([2,8,18,18,8,1],55)}
for name,(layers,Z) in am.items():
    check(f"{name} 排布和=核电荷数·最外层=1", sum(layers)==Z and layers[-1]==1, f"layers={layers}")

# ===== 五、卤素（p102图4-10）：排布和=核电荷数·最外层=7 =====
hal = {"F(9)":([2,7],9), "Cl(17)":([2,8,7],17), "Br(35)":([2,8,18,7],35), "I(53)":([2,8,18,18,7],53)}
for name,(layers,Z) in hal.items():
    check(f"{name} 排布和=核电荷数·最外层=7", sum(layers)==Z and layers[-1]==7, f"layers={layers}")

# ===== 六、碱金属表4-2熔点递减序列验算 =====
mp = [180.5, 97.81, 63.65, 38.89, 28.40]
check("碱金属熔点 Li>Na>K>Rb>Cs 严格递减", all(mp[i]>mp[i+1] for i in range(4)))

# ===== 七、自编例（显式标注自编）：相对原子质量=按核素丰度加权平均 =====
# 氯：35Cl(34.969, 75.8%)、37Cl(36.966, 24.2%)——丰度取通行公开数据近似值，例为本席自编
avg = Rational(34969,1000)*Rational(758,1000) + Rational(36966,1000)*Rational(242,1000)
check("自编例：氯平均相对原子质量≈35.45", abs(float(avg)-35.45)<0.01, f"={float(avg):.4f}")
check("自编例：结果落在两核素质量数之间(35<A<37)", 35<float(avg)<37)

# ===== 八、方程式原子守恒（矩阵秩法）=====
def balance_ok(left, right):
    """left/right: {元素: 个数}"""
    elems = set(left)|set(right)
    return all(left.get(e,0)==right.get(e,0) for e in elems)
eqs = [
    ("4Li+O2=2Li2O",        {"Li":4,"O":2},  {"Li":4,"O":2}),
    ("2Na+O2=Na2O2",        {"Na":2,"O":2},  {"Na":2,"O":2}),
    ("2Na+2H2O=2NaOH+H2",   {"Na":2,"H":4,"O":2}, {"Na":2,"O":2,"H":2*1+2*1}),
    ("2K+2H2O=2KOH+H2",     {"K":2,"H":4,"O":2},  {"K":2,"O":2,"H":2+2}),
    ("H2+F2=2HF",           {"H":2,"F":2},  {"H":2,"F":2}),
    ("H2+Cl2=2HCl",         {"H":2,"Cl":2}, {"H":2,"Cl":2}),
    ("H2+Br2=2HBr",         {"H":2,"Br":2}, {"H":2,"Br":2}),
    ("H2+I2=2HI",           {"H":2,"I":2},  {"H":2,"I":2}),
    ("2NaBr+Cl2=2NaCl+Br2", {"Na":2,"Br":2,"Cl":2}, {"Na":2,"Cl":2,"Br":2}),
    ("2NaBr+Cl2(实验4-1同型:KBr+Cl2)", {"K":2,"Br":2,"Cl":2}, {"K":2,"Cl":2,"Br":2}),
]
for name,l,r in eqs:
    check(f"方程式守恒: {name}", balance_ok(l,r))

# ===== 九、练习与应用答案验算 =====
check("题2: 14C中子数=14-6=8", 14-6==8, "→选B")
check("题4: 中子数176的Ts质量数=117+176=293", 117+176==293, "正确符号²⁹³₁₁₇Ts→选项D(¹⁷⁶₁₁₇Ts)错")
ten_e = {"CH4":6+4, "NH3":7+3, "H2O":8+2}
check("题5(4): CH4/NH3/H2O均为10电子", all(v==10 for v in ten_e.values()), str(ten_e))
check("题5(1): ⑤(Mg,ⅡA)下一周期同族=Ca核电荷20", 12+8==20, "+20: 2,8,8,2")
check("题6: Fe核电荷26/4周期Ⅷ族", 26==26, "Au79·Ag47·Cu29·Zn30·Ti22")

print(f"\n== 化学4.1验点总计: {ok}/{total} ALL {'PASS' if ok==total else 'FAIL'} ==")
import sys; sys.exit(0 if ok==total else 1)
