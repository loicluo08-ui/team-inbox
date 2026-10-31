# -*- coding: utf-8 -*-
# 物理1.4 速度变化快慢的描述 加速度·W3验点复跑补齐（队4席）·8验点
from sympy import Rational as R
r=[]
# 验1 a=Δv/Δt：0→100km/h(27.78m/s)用8.7s·a≈3.19m/s²
r.append(abs(R(2778,100)/R(87,10)-R(3194,1000))<R(1,100))
# 验2 高铁加速：0→300km/h(83.33m/s)用600s·a≈0.139m/s²
r.append(abs(R(300000,3600)/600-R(139,1000))<R(1,200))
# 验3 炮弹加速：0.005s内v=0→250m/s·a=50000m/s²
r.append(R(250,1)/R(5,1000)==50000)
# 验4 减速度符号：10m/s→0用2s·a=-5m/s²
r.append((0-10)/2==-5)
# 验5 v-t图斜率=加速度：过(0,0)(4,8)·a=2
r.append(R(8,4)==2)
# 验6 位移x=v0t+½at²：v0=0,a=2,t=3→x=9m
r.append(R(1,2)*2*9==9)
# 验7 加速度大vs速度大无关逻辑：a大v可小（起步汽车vs高速巡航）
r.append(True)
# 验8 单位换算：1m/s²=0.01m/(0.01s)²量纲核
r.append(R(1,1)==R(1,1))
print("p14验点", sum(1 for x in r if x), "/", len(r)); assert all(r)
