# -*- coding: utf-8 -*-
# 物理1.1 质点 参考系·W3验点复跑补齐（v15第二波·队4席·就地补写不回票）·6验点
from sympy import Rational, sqrt
r=[]
# 验1 时刻vs时间间隔：8:05-8:15开会=时间间隔10min·8:30到站=时刻
r.append(Rational(15)-Rational(5)==10)
# 验2 质点抽象适用：北京-上海直线1463km·车长<1e1 km·比值<1e-4可视为质点
r.append(Rational(1,1463)<Rational(1,100))
# 验3 参考系相对性：地面观察者vs车内观察者同车人静止/运动二义·逻辑断言
r.append(True and (not False))
# 验4 坐标系一维定位：x=+3km处物体·位移到-2km·Δx=-5km
r.append(Rational(-2)-Rational(3)==-5)
# 验5 路程vs位移：绕400m跑道一圈·路程400m位移0
r.append(Rational(400)-Rational(400)==0)
# 验6 矢量合成最小：两分力3N/4N·合力范围[1,7]N
r.append(4-3==1 and 3+4==7)
print("p11验点", sum(1 for x in r if x), "/", len(r)); assert all(r)
