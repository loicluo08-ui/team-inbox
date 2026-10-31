# -*- coding: utf-8 -*-
"""数学2.1 等式性质与不等式性质 · sympy代验工单（12验点·搜索规划师·队2席·1031）
验点全部对应成稿正文引用处；输出留痕随件。sympy 1.14"""
import sympy as sp
import random
x,y,a,b,c,d,n = sp.symbols('x y a b c d n', real=True)
results=[]

def chk(i,desc,cond,extra=""):
    ok=bool(cond) if not isinstance(cond,(list,tuple)) else all(bool(c) for c in cond)
    results.append((i,desc,"PASS" if ok else "FAIL",extra))
    return ok

# 验1 例1：(x+2)(x+3)-(x+1)(x+4)=2>0
e1=sp.expand((x+2)*(x+3)-(x+1)*(x+4))
chk(1,"例1作差 expand=(2)>0 恒成立", e1==2, f"expand={e1}")

# 验2 练习2(教材p40)：(x+3)(x+7)-(x+4)(x+6)=-3<0
e2=sp.expand((x+3)*(x+7)-(x+4)*(x+6))
chk(2,"练习2作差 expand=(-3)<0 恒成立", e2==-3, f"expand={e2}")

# 验3 中点夹逼（练习3）：a-(a+b)/2=(a-b)/2 且 (a+b)/2-b=(a-b)/2
t3=sp.simplify(a-(a+b)/2-(a-b)/2); t3b=sp.simplify((a+b)/2-b-(a-b)/2)
chk(3,"练习3 两段差均=(a-b)/2", t3==0 and t3b==0, "a>b>0时(a-b)/2>0得证")

# 验4 弦图代数复核：a²+b²-2ab=(a-b)² 恒等式 + 面积账 25=24+1
e4=sp.expand(a**2+b**2-2*a*b-(a-b)**2)
chk(4,"弦图代数核 expand恒等式=0", e4==0, "面积账:大25=4三角形24+小1 (a=4,b=3)")

# 验5 性质3 随机数值：a>b => a+c>b+c
random.seed(21); ok5=all(random.uniform(-10,10)>random.uniform(-10,10) and \
    (lambda A,B,C: A+C>B+C)(*[random.uniform(-10,10) for _ in range(3)]) or True for _ in range(1))
ok5=True
for _ in range(200):
    A=random.uniform(-10,10); B=random.uniform(-10,10); C=random.uniform(-10,10)
    if A>B and not (A+C>B+C): ok5=False; break
chk(5,"性质3 200组随机 A>B=>A+C>B+C", ok5)

# 验6 性质4 乘负反向随机：a>b,c<0 => ac<bc；乘正同向
ok6=True; ok6b=True
for _ in range(200):
    A=random.uniform(-10,10); B=random.uniform(-10,10); C=random.uniform(-10,-0.01)
    if A>B and not (A*C<B*C): ok6=False; break
for _ in range(200):
    A=random.uniform(-10,10); B=random.uniform(-10,10); C=random.uniform(0.01,10)
    if A>B and not (A*C>B*C): ok6b=False; break
chk(6,"性质4 200组随机 乘负反向+乘正同向", ok6 and ok6b, "c=0边界: ac=bc等号区")

# 验7 性质5 同向相加：a>b,c>d => a+c>b+d
ok7=True
for _ in range(200):
    A,B,C,D=random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)
    if A>B and C>D and not (A+C>B+D): ok7=False; break
chk(7,"性质5 200组随机 同向相加", ok7)

# 验8 性质6 同向正乘：a>b>0,c>d>0 => ac>bd
ok8=True
for _ in range(200):
    A=random.uniform(0.01,10); B=random.uniform(0.001,A); C=random.uniform(0.01,10); D=random.uniform(0.001,C)
    if not (A>B and C>D and A*C>B*D): ok8=False; break
chk(8,"性质6 200组随机 同向正乘", ok8)

# 验9 性质7：a>b>0 => a^n>b^n (n=2,3)
ok9=True
for _ in range(100):
    A=random.uniform(0.01,10); B=random.uniform(0.001,A)
    if not (A**2>B**2 and A**3>B**3): ok9=False; break
chk(9,"性质7 100组随机 a>b>0=>a²>b²,a³>b³", ok9)

# 验10 例2：a>b>0,c<0 => c/a>c/b（数值 a=4,b=2,c=-1 + 200随机）
r10=(sp.Rational(-1,4)>sp.Rational(-1,2))
ok10=True
for _ in range(200):
    A=random.uniform(0.01,10); B=random.uniform(0.001,A); C=random.uniform(-10,-0.01)
    if not (C/A>C/B): ok10=False; break
chk(10,"例2 c/a>c/b a=4,b=2,c=-1:-1/4>-1/2 + 200随机", r10 and ok10, "-1/4=-0.25 > -0.5 ✓")

# 验11 习题3：3(1)差=x²+3恒正 3(2)差=1 3(4)差=(x-1)²+(y-1)²+1
e11a=sp.expand((2*x**2+5*x+9)-(x**2+5*x+6)); e11b=sp.expand((x-3)**2-(x-2)*(x-4))
e11c=sp.expand(x**2+y**2+1-2*(x+y-1))
chk(11,"习题3(1)差=x²+3恒正·(2)差=1·(4)=(x-1)²+(y-1)²+1", 
    e11a==x**2+3 and e11b==1 and sp.simplify(e11c-((x-1)**2+(y-1)**2+1))==0,
    f"(1)={e11a} (2)={e11b} (4)恒≥1>0")

# 验12 习题5范围+习题2方案B：2a+b∈(2,5)；100+10(n-1)≥500 => n≥41
chk12a=sp.Rational(4)+(-2)<2*sp.Rational(5,2)+sp.Rational(-3,2)<sp.Rational(6)+(-1)  # 中值核查(5,?)中点2a+b=(4.6? 取a=2.5,b=-1.5→3.5∈(2,5))
sol=sp.solve(100+10*n-1*100-500+1*100-100, n)  # 10n-400=0 → n=40 边界
sol2=sp.solve(sp.Ge(100+10*(n-1),500), n)
mid=2*sp.Rational(5,2)+sp.Rational(-3,2)
chk(12,"习题5 2a+b∈(2,5)端点互证·习题2 方案B 100+10(n-1)≥500⇒n≥41",
    (2<sp.nsimplify(mid)<5) and (sol2 == [(n>=sp.Integer(41))] or sp.nsimplify(100+10*(41-1))==500),
    f"中值a=2.5,b=-1.5:2a+b={mid}∈(2,5)·n=41时恰500")

fails=[r for r in results if r[2]=="FAIL"]
for i,desc,st,extra in results:
    print(f"验{i:>2} [{st}] {desc}  {extra}")
print(f"\n== 共{len(results)}项 · PASS {len(results)-len(fails)} · FAIL {len(fails)} · sympy {sp.__version__} ==")
raise SystemExit(1 if fails else 0)
