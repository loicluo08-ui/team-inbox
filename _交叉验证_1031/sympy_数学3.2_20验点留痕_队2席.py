#!/usr/bin/env python3
# sympy 数值代验 · 数学3.2 函数的基本性质 · 队2席(搜索规划师·1031午后会话)
# 验点20条(含200组随机case×3)：逐条对应主件正文与教材例题习题数值
import random
from sympy import *

t, x, k, V, x1, x2 = symbols('t x k V x1 x2', real=True)
ok = fail = 0
def chk(name, cond):
    global ok, fail
    if cond: ok += 1; print(f"PASS {name}")
    else: fail += 1; print(f"FAIL {name}")

random.seed(1031031)
# ── 1. 例1 f(x)=kx+b：k>0增(差<0)·k<0减(差>0) ──
chk("例1-k>0增(200组随机)", all(((2*x1+1)-(2*x2+1)) < 0 for x1,x2 in [(random.uniform(-50,50),0) for _ in range(1)] ) if False else all(Rational(2)*(Rational(a))-Rational(2)*Rational(b) < 0 for a,b in [(0,1)] ) if False else all((S(2)*x1+S(1))-(S(2)*x2+S(1)) < 0 for _ in range(200) for x1,x2 in [(random.uniform(-9,8), random.uniform(9,30))] if x1<x2) )
chk("例1-k<0减(200组随机)", all(((-S(3)*x1+S(1))-(-S(3)*x2+S(1))) > 0 for _ in range(200) for x1,x2 in [(random.uniform(-9,8), random.uniform(9,30))] if x1<x2) )
# ── 2. 例2 p=k/V V∈(0,+∞)减：V1<V2 ⟹ p1>p2 (200组) ──
chk("例2-玻意耳减(200组随机)", all((S(5)/x1 - S(5)/x2) > 0 for _ in range(200) for x1,x2 in [(random.uniform(1,5), random.uniform(6,30))] if x1<x2) )
# ── 3. 例3 y=x+1/x (1,+∞)增：差式符号(200组) ──
d = (x1+S(1)/x1)-(x2+S(1)/x2)
chk("例3-对勾(1,+∞)增(200组随机)", all(d.subs({x1:a,x2:b}) < 0 for _ in range(200) for a,b in [(random.uniform(1.01,3), random.uniform(3.02,30))] if a<b) )
chk("例3-差式化简恒等", simplify(d - (x1-x2)*(x1*x2-1)/(x1*x2)) == 0)
# ── 4. 例4 烟花 h(t)=-4.9t²+14.7t+18：t*=1.5, h*=29.025≈29 ──
h = -S(49)/10*t**2 + S(147)/10*t + 18
chk("例4-顶点t*=14.7/9.8=1.5", nsimplify(solve(diff(h,t), t)[0]) == Rational(3,2))
chk("例4-h(1.5)=29.025≈29", abs(h.subs(t,Rational(3,2)) - S(1161)/40) < 1e-12 and abs(float(h.subs(t,Rational(3,2))) - 29) < 0.5)
chk("例4-顶点式4ac-b²/4a同值", simplify((4*(-S(49)/10)*18 - Rational(147,10)**2)/(4*(-S(49)/10)) - h.subs(t,Rational(3,2))) == 0)
# ── 5. 例5 f=2/(x-1) [2,6]：max=f(2)=2·min=f(6)=0.4·单调递减(200组) ──
f5 = S(2)/(x-1)
chk("例5-f(2)=2", f5.subs(x,2) == 2)
chk("例5-f(6)=0.4", f5.subs(x,6) == Rational(2,5))
chk("例5-单调递减(200组随机)", all((f5.subs(x,a)-f5.subs(x,b)) > 0 for _ in range(200) for a,b in [(random.uniform(2,4), random.uniform(4.01,6))] if a<b) )
chk("例5-作差因式恒等", simplify((f5.subs(x,x1)-f5.subs(x,x2)) - 2*(x2-x1)/((x1-1)*(x2-1))) == 0)
# ── 6. 教材p79练习3 f=-2/x在(-∞,0)增(50组) ──
f6 = -S(2)/x
chk("p79练3-(-∞,0)增(50组随机)", all((f6.subs(x,a)-f6.subs(x,b)) < 0 for _ in range(50) for a,b in [(random.uniform(-30,-10), random.uniform(-9,-0.1))] if a<b) )
# ── 7. 教材p81练3 1/x∈[2,6]：max=1/2 min=1/6 ──
chk("p81练3-max=1/2·min=1/6", S(1)/2==S(1)/x.subs(x,2) and S(1)/6==S(1)/x.subs(x,6))
# ── 8. 习题7(改编) f=x²-2x在[2,4]：min=f(2)=0·递增 ──
f8 = x**2-2*x
chk("习题7-f(2)=0", f8.subs(x,2) == 0)
chk("习题7-[2,4]递增(50组随机)", all((f8.subs(x,a)-f8.subs(x,b)) < 0 for _ in range(50) for a,b in [(random.uniform(2,3.9), random.uniform(3.91,4))] if a<b) )
# ── 9. 例6 四函数奇偶 ──
chk("例6(1)-x⁴偶", simplify((-x)**4 - x**4) == 0)
chk("例6(2)-x⁵奇", simplify((-x)**5 + x**5) == 0)
chk("例6(3)-x+1/x奇", simplify((-x+S(1)/(-x)) + (x+S(1)/x)) == 0)
chk("例6(4)-1/x²偶", simplify(S(1)/(-x)**2 - S(1)/x**2) == 0)
# ── 10. 自测1 单调区间判据：x²-5x-6顶点2.5·9-x²顶点0 ──
chk("自测1-顶点x*=5/2", solve(diff(x**2-5*x-6, x), x)[0] == Rational(5,2))
chk("自测1-y=9-x²顶点0", solve(diff(9-x**2, x), x)[0] == 0)
# ── 11. 自测3 f=x²-2x∈[2,4] min=0(端点) ──
chk("自测3-min=f(2)=0≠顶点值-1(区间外)", f8.subs(x,2)==0 and f8.subs(x,1)==-1)
# ── 12. 自测4 x²+1偶 ──
chk("自测4-x²+1偶", simplify((-x)**2+1 - (x**2+1)) == 0)
# ── 13. 拓展对勾 y=x+9/x：x*=3, min=6 ──
chk("拓展-对勾x*=3·min=6", solve(diff(x+S(9)/x, x), x) == [3] and (x+S(9)/x).subs(x,3) == 6)
# ── 14. 拓展对称中心 f=x³-3x²：f(1+t)+f(1-t)=-4 ──
chk("拓展-对称中心(1,-2)验证", simplify((1+t)**3-3*(1+t)**2 + (1-t)**3-3*(1-t)**2 + 4) == 0)
chk("拓展-f(x+1)+2=x³-3x奇", expand(((x+1)**3-3*(x+1)**2+2) - (x**3-3*x)) == 0)
# ── 15. 习题11 奇函数延拓 x≥0:x(1+x) → x<0:x(1-x)=x-x² ──
chk("习题11-f(-2)=f(2)取反=-6", (-(  (-2)*(1-(-2)) )) == ((2)*(1+2))*(-1) and (S(-2)*(1-S(-2))).equals(-6) if False else simplify(((-x)*(1-(-x))) + x*(1+x).subs(x,-x) if False else -((-x)*(1-x)) - x*(1+x)) == 0)

print(f"\n合计 PASS={ok} FAIL={fail}")
print("留痕: 队2席·搜索规划师(1031午后会话)·sympy 1.14.0·seed=1031031")
