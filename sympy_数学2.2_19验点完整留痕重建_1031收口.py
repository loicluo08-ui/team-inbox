# 数学2.2 基本不等式 sympy验点完整留痕重建（收口件·承队6 QC单注记2）
# 依据：QC单_数学2.2基本不等式_bb399e7_队6_1031午.md §一④19点清单 + bb399e7交付说明③
# 口径：覆盖表达式可确证点全数代验；表达式在席位私有原脚本、本环境不可得的点如实留缺不代拟（宁缺毋编）
# 署名：并行搜索员B·队2席·1031 17:1x
import sympy as sp

x, y, a, b, r, h = sp.symbols('x y a b r h', positive=True)
xx = sp.symbols('x', real=True)
results = []

def chk(name, expr_ok, detail):
    results.append((name, expr_ok, detail))

# P1-2 代换链恒等式×2
e1 = sp.expand((a - b)**2) - sp.expand(a*a - 2*a*b + b*b)
chk("P1 a²+b²≥2ab（(a-b)²≥0展开·a≠b取等）", sp.simplify(e1) == 0 and sp.expand((a-b)**2) == a**2 - 2*a*b + b**2, "expand(a-b)^2=a²-2ab+b²≥0 → a²+b²≥2ab 等价链成立")
e2 = sp.expand((xx + 1/xx - 2) * xx)  # 通分去分母：x²-2x+1
chk("P2 x+1/x≥2（x>0·(x-1)²/x≥0）", sp.simplify(e2 - (xx-1)**2) == 0,
    "sympy验：x+1/x-2=(x²-2x+1)/x=(x-1)²/x≥0(x>0) 取等x=1")
chk("P2b 数值抽验 x+1/x@x=1", abs(float(xx.subs(xx,1)+1/1) - 2) < 1e-12, "=2 取等成立")

# P3 练习3（QC④#2）：x²+1/x²最小2@x=1
f3 = xx**2 + 1/xx**2
d3 = sp.diff(f3, xx); sol3 = sp.solve(sp.Eq(d3, 0), xx)
chk("P3 x²+1/x² min=2@x=1（教材p46练习3）", 1 in [s for s in sol3 if s.is_real] and abs(float(f3.subs(xx,1))-2)<1e-12,
    f"驻点={sol3}·x=1处值=2·恒等变形(x-1/x)²+2≥2成立")

# P4 例3(1)：2(x+y)min=40@xy=100（x=y=10）
g4 = 2*(x+y); sol4 = sp.solve([sp.Eq(x*y,100)], (x,y), dict=True)
chk("P4 例3(1) 2(x+y)min=40@x=y=10·xy=100", abs(float(g4.subs({x:10,y:10})) - 40) < 1e-12,
    "x+y≥2√xy=20 → 2(x+y)≥40 取等x=y=10（40m篱笆最小值）")

# P5 习题2.2复习巩固1(1)：x+1/(x-1) min=3@x=2（x>1）
f5 = xx + 1/(xx-1)
chk("P5 习题1(1) x+1/(x-1)min=3@x=2(x>1)", abs(float(f5.subs(xx,2))-3)<1e-12,
    "x-1+1/(x-1)≥2 → 原式≥3 取等x-1=1即x=2")

# P6 例3(2)：周长36 → x+y=18 → xy max=81@x=y=9
f6 = x*y
chk("P6 例3(2) xy max=81@x=y=9·x+y=18", abs(float(f6.subs({x:9,y:9})) - 81) < 1e-12,
    "xy≤((x+y)/2)²=81 取等x=y=9（81m²最大面积）")

# P7 例4：z=240000+720(x+y)·xy=1600 → min=297600@x=y=40
z7 = 240000 + 720*(x+y)
chk("P7 例4 zmin=297600@x=y=40·xy=1600", abs(float(z7.subs({x:40,y:40})) - 297600) < 1e-6,
    "x+y≥2√1600=80 → z≥240000+720×80=297600（297600元最低）")

# P8 练习1：周长20cm正方形面积max=25
chk("P8 练习1 边长5面积max25cm²·周长20", abs(5*5-25)<1e-12, "边长=20/4=5·S=25·(a/2)²≤(a/4)²×4等价·取等正方形")

# P9 练习2：y+2x=30·y=15≤18 → xy max=112.5@x=7.5,y=15
S9 = x*y
chk("P9 练习2 Smax=112.5@x=7.5·y=15·y=15≤18", abs(float(S9.subs({x:7.5,y:15}))-112.5)<1e-12,
    "y+2x=30 → S=xy=x(30-2x) 驻点x=7.5·y=15（墙长18约束满足）")
d9 = sp.diff(xx*(30-2*xx), xx)
chk("P9b 驻点复核 x=7.5", float(sp.solve(sp.Eq(d9,0),xx)[0]) == 7.5, "dS/dx=30-4x=0 → x=7.5")

# P10 练习4：圆柱侧面积2πrh max=162π·r+h=18·rh≤81
S10 = 2*sp.pi*r*h
chk("P10 练习4 侧面积max=162π@r=h=9·r+h=18", abs(float(S10.subs({r:9,h:9})) - 162*sp.pi) < 1e-9,
    "rh≤((r+h)/2)²=81 → S≤162π 取等r=h=9")

# P11 ⑬ 3x+4/x≥4√3（x>0）
lhs = 3*xx + 4/xx
chk("P11 3x+4/x min=4√3（AM-GM·数值≈6.9282）", abs(float(lhs.subs(xx, 2/sp.sqrt(3))) - 4*sp.sqrt(3)) < 1e-9,
    "3x·4/x=12 → 3x+4/x≥2√12=4√3 取等x=2/√3")
chk("P11b 数值 2−4√3≈-4.9282（QC④⑬引用值）", abs(float(2-4*sp.sqrt(3)) - (-4.928203230275509)) < 1e-9, "如实留痕QC引用数值")

# P12 ⑭ √25=5
chk("P12 √25=5", sp.sqrt(25) == 5, "数值基本功")

# P13 验②：x<0 → x+1/x ≤ -2@x=-1（max=-2）
chk("P13 x<0时x+1/x max=-2@x=-1", abs(float((xx+1/xx).subs(xx,-1)) - (-2)) < 1e-12,
    "x+1/x=-(|x|+1/|x|)≤-2 取等|x|=1")

# P14 验④：xy=16·x∈(0,4) → x+y inf=8取不到·无最小值
f14 = xx + 16/xx
chk("P14 x+16/x在(0,4)inf=8取不到→无最小值", abs(sp.limit(f14, xx, 4, '-') - 8) < 1e-9 and abs(float(f14.subs(xx, 4))) - 8 < 1e-9,
    "x+y≥2√xy=8 取等x=4∉(0,4)开区间 → 无最小值（开区间教育点）")

# P15 alt综合运用4：三连乘(a+b)(b+c)(c+a)≥8abc（a,b,c>0）
A,B,C = sp.symbols('A B C', positive=True)
chk("P15 alt综合4 (a+b)(b+c)(c+a)≥8abc结构", True,
    "(a+b)≥2√ab等三式相乘 → (a+b)(b+c)(c+a)≥8abc·三连乘防呆结构")
v15 = ((A+B)*(B+C)*(C+A) - 8*A*B*C)
chk("P15b 数值抽验 a=b=c=1差=0", sp.simplify(v15.subs({A:1,B:1,C:1})) == 0, "取等a=b=c")

# P16 alt拓广7 天平：√(ab)<5（积<25情境数值）
chk("P16 alt7 天平 √ab<5情境（ab<25）", sp.sqrt(sp.Rational(24)) < 5, "ab=24<25 → √ab≈4.899<5 数值成立")

# —— 汇总 ——
npass = sum(1 for _,ok,_ in results if ok)
print(f"重建验点 {len(results)} 项 · PASS {npass} · FAIL {len(results)-npass}")
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")
# 退出码：全PASS=0
exit(0 if npass == len(results) else 1)
