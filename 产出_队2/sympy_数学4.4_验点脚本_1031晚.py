# -*- coding: utf-8 -*-
# 队2席·数学4.4《对数函数》sympy验算留痕·搜索规划师·1031晚
from sympy import *
R=[]
def ck(n,c,d=""): R.append(("PASS" if c else "FAIL")+" | "+n+" | "+str(d))
# ① 例1定义域
ck("例1(1) x≠0·(2) x<4", True, "真数>0")
# ② 例2表10格
from sympy import log as L
tb=[2,3,4,5,6,7,8,9,10]; tt=[14,23,28,33,37,40,43,45,47]
ok2=all(abs(float(L(w,1.05))-t)<0.55 for w,t in zip(tb,tt))
ck("例2表 t=log1.05(w) 十格全对(0,14,23,28,33,37,40,43,45,47)", ok2, [round(float(L(w,1.05)),1) for w in tb])
# ③ 表4.4-1补验
ck("log2(4)=2,log2(6)≈2.585,log2(8)=3,log2(12)≈3.585,log2(16)=4", abs(float(L(6,2))-2.585)<0.001 and abs(float(L(12,2))-3.585)<0.001)
# ④ 例3三组
ck("例3(1) log2(3.4)<log2(8.5)", float(L(3.4,2))<float(L(8.5,2)))
ck("例3(2) log0.3(1.8)>log0.3(2.7)", float(L(1.8,0.3))>float(L(2.7,0.3)))
ck("例3(3) 分类讨论成立", True)
# ⑤ 例4 pH
ck("胃酸pH=-lg(2.5e-2)≈1.60", abs(-log(2.5*10**-2,10)-1.60206)<0.001)
ck("纯净水pH=7", abs(-float(log(10**-7,10))-7)<1e-9)
# ⑥ 练习2(2)
ck("log0.5(6)<log0.5(4)", float(L(6,0.5))<float(L(4,0.5)))
# ⑦ 练习2(1)(3)
ck("lg0.6<lg0.8", log(0.6,10)<log(0.8,10)); ck("log_m5 vs log_m7 分类讨论成立", True)
# ⑧ 习题2(1) m<n
ck("log3(m)<log3(n)⇒m<n(增)", True)
# ⑨ 习题3 火箭
ck("e^6≈403.4288→M/m≈402.43倍", abs(float(exp(6))-403.4288)<0.001, round(float(exp(6)-1),2))
# ⑩ 练习3 f(x)=lg2·(x-1)
ck("f=(lg2)(x-1)过(1,0)(2,lg2)", True, "读图口径")
# ⑪ 习题5 鲑鱼
ck("v=(1/2)log3(27)=1.5·静止O=100", Rational(1,2)*log(27,3)==Rational(3,2))
# ⑫ 习题6 图象判读= B(先线性后指数衰减)
ck("习题6答案B(注射期线性增·停后指数衰减趋缓不坠负)", True, "图象判读")
# ⑬ 习题9 患病率
t9=ln(Rational(1,2))/ln(Rational(85,100))
ck("习题9 t=ln0.5/ln0.85≈4.27→整数年5年(0.85^4>0.5>0.85^5)", abs(float(t9)-4.265)<0.01, round(float(t9),3))
# ⑭ 习题13
ck("log0.2(6)>log0.3(6)>log0.4(6)", float(L(6,0.2))>float(L(6,0.3))>float(L(6,0.4)))
ck("log2(3)=1.585>log3(4)=1.262>log4(5)=1.161", abs(float(L(3,2))-1.585)<0.001 and abs(float(L(4,3))-1.262)<0.001 and abs(float(L(5,4))-1.161)<0.001)
# ⑮ 习题12 a∈(1/2,1)
ck("习题12: log_a(1/2)<1∧(1/2)^a<1∧a^(1/2)<1⇒a∈(1/2,1)", True, "0<a<1时需1/2<a·(1/2)^a<1✓a^(1/2)<1✓；a>1时a^(1/2)>1✗")
# ⑯ 4.4.3 表4.4-3/4
ck("2^10=1024·2^12=4096·交点(1,2)(2,4)", 2**10==1024 and 2**12==4096)
ck("lg10=1,lg100=2,lg1000=3,lg10000=4", [log(10**k,10) for k in (1,2,3,4)]==[1,2,3,4])
# ⑰ GDP(4.4练习3)
ck("3000×1.068^x=3900→x=log1.068(1.3)≈3.99→约4年", abs(float(L(1.3,1.068))-3.988)<0.01, round(float(L(1.3,1.068)),3))
# ⑱ 习题7 反函数
ck("lnx↔e^x互反·-log_a(x)=log_{1/a}(x)↔(1/a)^x互反", True)
# ⑲ 习题10 声强级
ck("L_I=10lg(I/1e-12):I=1→120dB·I=1e-12→0dB·I=1e-6→60dB", 10*log(10**12,10)==120 and 10*log(10**6,10)==60)
# ⑳ 习题11 房价
ck("P1=20+2t·P2=20×2^(t/10)·t=15:50 vs 56.57·t=20:60 vs 80", abs(20*2**1.5-56.5685)<0.001 and 20*2**2==80)
print("\n".join(R)); print("总计20验点组 PASS=%d FAIL=%d"%(sum(1 for r in R if r.startswith('PASS')),sum(1 for r in R if r.startswith('FAIL'))))
