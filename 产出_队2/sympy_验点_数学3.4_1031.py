# -*- coding: utf-8 -*-
"""数学3.4 函数的应用（一）· 首学版 sympy 独立代验脚本（并行搜索员B·队2席·1031晚）
29验点·承QC前置六项③·独立代验口径（先例：2.2收口件sympy重建代验）"""
import sympy as sp
x,t = sp.symbols('x t', real=True)
P=[]; F=[]
def chk(i,name,expr_ok): 
    (P if expr_ok else F).append(i); print(('PASS' if expr_ok else 'FAIL'),i,name)

# 例1 个税模型（p93-94）
chk(1,"t=x-60000-x*20%-9600-560 化简=0.8x-70160",sp.simplify(x-60000-x*sp.Rational(20,100)-9600-560-(sp.Rational(8,10)*x-70160))==0)
chk(2,"t=0 拐点 x=87700",sp.solve(sp.Eq(sp.Rational(8,10)*x-70160,0),x)==[sp.Rational(87700,1)])
chk(3,"x=117600→t=23920",sp.Rational(8,10)*117600-70160==23920)
chk(4,"第二段 y=0.024x-2104.8 @117600 =717.6",sp.Rational(24,1000)*117600-sp.Rational(21048,10)==sp.Rational(7176,10))
chk(5,"第二段系数=0.8×3%",sp.Rational(8,10)*sp.Rational(3,100)==sp.Rational(24,1000))
chk(6,"第二段截距=-70160×3%",sp.Rational(-70160,1)*sp.Rational(3,100)==sp.Rational(-21048,10))
chk(7,"第三段截距=10%×70160+速算2520=9536",sp.Rational(10,100)*70160+2520==9536)
chk(8,"x=153600∈(132700,267700]落第三段",132700<153600<=267700)
chk(9,"(2)问 y=0.08×153600-9536=2752",sp.Rational(8,100)*153600-9536==2752)
chk(10,"第四段截距=20%×70160+速算16920=30952",sp.Rational(20,100)*70160+16920==30952)
chk(11,"第五段截距=25%×70160+速算31920=49460",sp.Rational(25,100)*70160+31920==49460)
chk(12,"第六段截距=30%×70160+速算52920=73968",sp.Rational(30,100)*70160+52920==73968)
chk(13,"第七段截距=35%×70160+速算85920=110476",sp.Rational(35,100)*70160+85920==110476)
chk(14,"第八段截距=45%×70160+速算181920=213492",sp.Rational(45,100)*70160+181920==213492)
# 例2 汽车行程（p94-95）
chk(15,"五段面积 50+80+90+75+65=360",50+80+90+75+65==360)
chk(16,"s(1)=50×1+2004=2054",50*1+2004==2054)
chk(17,"s(2)=80×1+2054=2134",80*(2-1)+2054==2134)
chk(18,"s(3)=90×1+2134=2224",90*(3-2)+2134==2224)
chk(19,"s(4)=75×1+2224=2299",75*(4-3)+2224==2299)
chk(20,"s(5)=65×1+2299=2364",65*(5-4)+2299==2364)
chk(21,"总里程 2364-2004=360=面积",2364-2004==360)
# 练习（p95）
chk(22,"练1 a=20/60²=1/180",sp.Rational(20,1)/sp.Rational(60,1)**2==sp.Rational(1,180))
chk(23,"练1 100²/180≈55.6>50 超速",sp.Rational(100,1)**2/sp.Rational(180,1)>50)
l=sp.Symbol('l',positive=True); w=sp.symbols('w',positive=True)
S=w*(l/2-w); crit=sp.solve(sp.diff(S,w),w)
chk(24,"练2 周长l矩形面积最大 w=l/4(正方形)",crit==[l/4] and sp.simplify(S.subs(w,l/4)-l**2/16)==0)
u=sp.symbols('u',positive=True)
y4=sp.Rational(35,100)*u-150-sp.Rational(25,100)*u
chk(25,"练3 总利润 y4=0.1u-150·盈亏平衡 u=1500",sp.simplify(y4-(sp.Rational(1,10)*u-150))==0 and sp.solve(sp.Eq(y4,0),u)==[1500])
# 习题3.4（p96）
s=sp.symbols('s',positive=True)
W=95*2*6*(s+200/s)+135*200
chk(26,"习2 xy=1200/6=200",sp.Rational(1200,1)/6==200)
chk(27,"习2 x=y=√200≈14.1·W≈59148≤70000",abs(sp.sqrt(200).evalf(3)-sp.Float('14.1',3))<0.06 and W.subs(s,sp.sqrt(200)).evalf(2)<=70000)
chk(28,"习3 阶梯水价 3×12+6×(x-12)=48→x=14",sp.solve(sp.Eq(3*12+6*(x-12),48),x)==[14])
d=sp.symbols('d',real=True)
chk(29,"习1 去程60km/h×2.5h=150km",60*sp.Rational(5,2)==150)
print(f"\n== 29验点：PASS {len(P)} / FAIL {len(F)} ==")
exit(0 if not F else 1)
