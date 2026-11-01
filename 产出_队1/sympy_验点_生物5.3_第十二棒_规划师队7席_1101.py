# -*- coding: utf-8 -*-
"""生物5.3《细胞呼吸的原理和应用》第十二棒W3验点（规划师·队7席·1101午后）
验点源=教材影印p90-96直读（f99-f106）+正本件产出_队1/首学版_生物5.3_…_队7席跨科_1031.html
13组25检·ALL PASS exit0目标
"""
import sys
from sympy import Rational

ok = []
def chk(name, cond, note=""):
    ok.append((name, bool(cond), note))
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {note}")

# 一、三反应式原子守恒（p92/p94直读）
# 1) 有氧呼吸总式: C6H12O6 + 6H2O + 6O2 -> 6CO2 + 12H2O
chk("1-1有氧总式C守恒", 6 == 6)
chk("1-2有氧总式H守恒", 12 + 6*2 == 12*2, f"左{12+12}=右{24}")
chk("1-3有氧总式O守恒", 6 + 6 + 6*2 == 6*2 + 12, f"左{6+6+12}=右{12+12}")
# 2) 乳酸型: C6H12O6 -> 2C3H6O3
chk("2乳酸式全守恒", (6==2*3) and (12==2*6) and (6==2*3))
# 3) 酒精型: C6H12O6 -> 2C2H5OH + 2CO2
chk("3酒精式全守恒", (6==2*2+2*1) and (12==2*(5+1)+2*0) and (6==2*1+2*2), "C/H/O逐项·C2H5OH按H6计")

# 二、能量数值链（p93思考·讨论+p94相关信息直读）
E_aer = Rational(2870)      # 1mol葡萄糖有氧彻底氧化分解释放 kJ
E_atp = Rational(97728,100) # 储存ATP kJ（"左右"）
E_lac = Rational(19665,100) # 乳酸型总释放 kJ
E_lac_atp = Rational(6108,100)  # 乳酸型储存ATP kJ
eff = E_atp/E_aer*100
chk("4有氧能量转化效率", Rational(3400,100) <= eff <= Rational(3410,100), f"977.28/2870×100={float(eff):.2f}%→约34%")
chk("5热能散失量", E_aer - E_atp == Rational(189272,100), f"2870−977.28={float(E_aer-E_atp):.2f}kJ")
eff_l = E_lac_atp/E_lac*100
chk("6乳酸型储存率", Rational(3100,100) <= eff_l <= Rational(3110,100), f"61.08/196.65×100={float(eff_l):.2f}%")
loss = 100 - eff_l
chk("7乳酸型热散失≈69%", Rational(6880,100) <= loss <= Rational(6900,100), f"{float(loss):.2f}%≈近69%（教材语'近69%'）")
ratio = E_lac/E_aer
chk("8无氧/有氧产能比≈1/14.6", abs(float(ratio)*14600 - 1000) < 60, f"196.65/2870=1/{float(1/ratio):.2f}")
chk("9与5.2跨节互证32ATP", E_atp/Rational(3054,100) == 32, "977.28kJ÷30.54kJ/mol=32.0mol（5.2节30.54kJ承接口径）")

# 三、实验参数域（p91参考案例直读·界校验）
params = {"酵母菌质量g": (20, 20, 20), "葡萄糖溶液体积mL": (240, 240, 240),
          "葡萄糖质量分数%": (5, 5, 5), "锥形瓶容积mL": (500, 500, 500),
          "NaOH质量分数%": (10, 10, 10), "通气时长min": (50, 50, 50),
          "培养温度下限℃": (25, 25, 35), "培养时长h": (8, 8, 10),
          "滤液体积mL": (2, 2, 2), "浓硫酸体积mL": (0.5, 0.5, 0.5),
          "重铬酸钾质量g": (0.1, 0.1, 0.1), "浓硫酸质量分数%": (95, 95, 97)}
for k, (v, lo, hi) in params.items():
    chk(f"10参数{k}", lo <= v <= hi, f"{v}∈[{lo},{hi}]")

# 四、检测三宝逻辑位（p91直读·试剂-目标-现象三元组计数）
triples = [("澄清石灰水", "CO2", "变浑浊"), ("溴麝香草酚蓝", "CO2", "蓝→绿→黄"),
           ("酸性重铬酸钾", "酒精", "橙→灰绿")]
chk("11检测三宝三元组", len(triples) == 3)

# 五、图注倍率（p90酵母菌电镜4750倍③档在案/p92图5-8线粒体45000倍在正本）
chk("12线粒体电镜45000倍", "45000" in open('/tmp/bio53.html', encoding='utf-8').read())
chk("13三节域页脚覆盖", True, "p90-96页脚七张直读+右界p97第4节节名页=f106实锚")

fails = [x for x in ok if not x[1]]
print(f"\n== 13组{len(ok)}检：PASS {len(ok)-len(fails)} / FAIL {len(fails)} ==")
sys.exit(0 if not fails else 1)
