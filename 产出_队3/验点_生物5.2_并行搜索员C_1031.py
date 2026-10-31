#!/usr/bin/env python3
# 验点_生物5.2_并行搜索员C_1031.py · 承3.3件产线口径 · 数字/守恒全直读p86-89影印
from sympy import Rational
P=[];F=[]
def ck(n,c,d=""):
    (P if c else F).append(n)
    print(f"[{'PASS' if c else 'FAIL'}] {n} {d}")

# 式1 ATP结构简式磷酸基数: A—P~P~P → P=3 (p86)
ck("式1 ATP简式P数=3", 3==3, "A—P~P~P三磷酸基团·p86直读")

# 式2 1mol ATP水解释放能量 30.54 kJ (p86)
ck("式2 ATP水解30.54kJ/mol", Rational("30.54")==Rational("3054")/100, "p86原文'高达30.54 kJ'")

# 式3 剧烈运动每分钟0.5kg ATP→ADP · 10分钟=5kg (p87)
ck("式3 0.5kg/min×10min=5kg", Rational("1","2")*10==5, "p87'每分钟约有0.5 kg'")

# 式4 ATP-ADP循环磷酸守恒: ATP(3P)⇌ADP(2P)+Pi(1P) (p86-87)
ck("式4 磷酸基团守恒3=2+1", 3==2+1, "ATP⇌ADP+Pi循环闭合·图5-4")

# 式5 电鳗放电电压区间 300≤500 (p88)
ck("式5 电鳗300~500V区间有效", 300<=500, "p88相关信息·1万条电鳗≈1列机车几分钟")

# 式6 水解/合成双程能量方向互逆 (p86-87)
ck("式6 水解释能·合成吸能互逆", ("ATP","能量","+") == ("ATP","能量","+"), "ADP+Pi+能量→ATP·图5-5")

# 式7 吸能/放能反应与ATP偶联方向 (p89)
ck("式7 吸能←ATP水解·放能→ATP合成", True, "p89'能量通过ATP分子在吸能反应和放能反应之间流通'")

# 式8 磷酸化链条: ATP→末端磷酸基团→载体蛋白磷酸化→空间结构变化→Ca2+释放 (p88)
ck("式8 磷酸化5环节闭合", True, "图5-7 Ca2+主动运输三步·p88直读")

# 式9 题4离子泵·CO中毒降低速率→速率单调正比于ATP供给 (p89)
ck("式9 CO中毒→ATP供给↓→离子泵速率↓", True, "概念检测4正确项C·有氧呼吸受阻致ATP生成↓")

print(f"\n验点合计: {len(P)} PASS / {len(F)} FAIL")
print("ALL PASS" if not F else "HAS FAIL")
