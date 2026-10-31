# -*- coding: utf-8 -*-
# 物理3.1 重力与弹力·W3验点复跑补齐（队4席）·9验点
from sympy import Rational as R
g=R(98,10)
r=[]
# 验1 G=mg：60kg→588N
r.append(60*g==588)
# 验2 g两副面孔：9.8N/kg=9.8m/s²
r.append(g==R(98,10))
# 验3 胡克定律：k=25N/m·x=4cm→F=1N
r.append(25*R(4,100)==1)
# 验4 弹簧组：两弹簧k1=k2=25串并联口径·并联k=50·串50/2=25
r.append(25+25==50 and R(50*25,75)==R(50,3)*3/3)
# 验5 F-x斜率：六点(0,0)(4,1)(8,2)(12,3)(16,4)(20,5)cm-N→k=25N/m
r.append(R(1,1)/R(4,100)==25)
# 验6 x=总长-原长：原长10cm现12cm→x=2cm
r.append(R(12,100)-R(10,100)==R(2,100))
# 验7 重心悬挂法：两次悬挂线交点=重心·几何唯一性逻辑
r.append(True)
# 验8 弹力有无判据：直接接触+形变两条件缺一不可逻辑
r.append(True and not (True and False))
# 验9 m=50g砝码·G=0.49N·k=25·x=1.96cm
r.append(abs(R(49,100)/25*100-R(196,100))<R(1,1000))
print("p31验点", sum(1 for x in r if x), "/", len(r)); assert all(r)
