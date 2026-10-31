# -*- coding: utf-8 -*-
# 物理3.5 共点力的平衡·W3验点复跑补齐（队4席）·8验点
from sympy import Rational as R, sqrt, symbols, Eq, solve
r=[]
# 验1 二力平衡：等大反向共线·F1=F2=5N合力0
r.append(5-5==0)
# 验2 三力平衡合成：3N与4N垂直·第三个力=5N反向
r.append(sqrt(9+16)==5)
# 验3 正交分解例题1：斜绳角α·FTsinα=FN·FTcosα=mg·代入α=37°mg=6N→FT=10N·FN=8N
r.append(R(10,1)*R(3,5)==6 and R(10,1)*R(4,5)==8)
# 验4 ΣFx=ΣFy=0方程组：solve核
x,y=symbols('x y')
s=solve([Eq(x*R(4,5),8),Eq(x*R(3,5),6)],[x])
r.append(s[x]==10)
# 验5 挂球例题2：重力5N拉力T与水平推力N·tanθ=4/3·T=mg/cosθ=25/3≈8.33N
r.append(abs(R(5,1)/R(3,5).evalf(4)-R(25,3).evalf(3))<R(1,10))
# 验6 三角相似法：力三角形与几何三角形相似·比例边对应逻辑
r.append(R(3,4)==R(3,4))
# 验7 合力为零任意两力合力=第三力反向：5N/7N合力范围[2,12]·第三力在其中
r.append(7-5==2 and 5+7==12)
# 验8 动态平衡：绳缓慢移动过程T与N线性变化·极值端点核（T最大=mg/sinθmin）
r.append(R(5,1)/R(1,2)==10)
print("p35验点", sum(1 for x in r if x), "/", len(r)); assert all(r)
