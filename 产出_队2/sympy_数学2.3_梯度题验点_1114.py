# -*- coding: utf-8 -*-
# 数学2.3 新标准升格·新增试题29验点全量sympy代验（1114批2·并行搜索员B·队2席）
import sympy as sp
x, y, m, a, b = sp.symbols('x y m a b', real=True)
n = fail = 0
def chk(name, cond):
    global n, fail
    n += 1
    ok = bool(cond)
    if not ok: fail += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")

# 选择1: x²−5x+6>0 解集 x<2或x>3（B）
chk("选择1-x=1时2>0(左域)", (x**2-5*x+6).subs(x,1) > 0)
chk("选择1-x=2时=0(等号排除C)", (x**2-5*x+6).subs(x,2) == 0)
chk("选择1-x=2.5时<0(中间出局)", (x**2-5*x+6).subs(x,sp.Rational(5,2)) < 0)
chk("选择1-x=4时2>0(右域)", (x**2-5*x+6).subs(x,4) > 0)
# 选择2: −x²+2x+3≥0 解集 [−1,3]（A）
chk("选择2-x=0时3>0(内部)", (-x**2+2*x+3).subs(x,0) >= 0)
chk("选择2-x=-1时0(端点含)", (-x**2+2*x+3).subs(x,-1) == 0)
chk("选择2-x=3时0(端点含)", (-x**2+2*x+3).subs(x,3) == 0)
chk("选择2-x=4时-5<0(外部出局)", (-x**2+2*x+3).subs(x,4) < 0)
# 选择3: ax²+bx+2>0 解集(−1,2) => a=−1,b=1, a+b=0（C）
sol = sp.solve([a-b+2, 4*a+2*b+2], [a,b], dict=True)[0]
chk("选择3-联立零点解得a=-1", sol[a] == -1)
chk("选择3-联立零点解得b=1", sol[b] == 1)
chk("选择3-a+b=0", sol[a]+sol[b] == 0)
chk("选择3-x=0时代2>0(解集内)", (-x**2+x+2).subs(x,0) > 0)
chk("选择3-x=3时代-4<0(解集外)", (-x**2+x+2).subs(x,3) < 0)
# 填空: x²+(m−2)x+1>0恒成立 => 0<m<4
chk("填空-m=2时x²+1恒正", sp.simplify((x**2+(m-2)*x+1).subs(m,2) - (x**2+1)) == 0 and (x**2+1).subs(x,0) > 0)
chk("填空-m=0时x=1处=0不恒正(排除)", (x**2+(m-2)*x+1).subs({m:0,x:1}) == 0)
chk("填空-m=4时x=-1处=0不恒正(排除)", (x**2+(m-2)*x+1).subs({m:4,x:-1}) == 0)
chk("填空-m=5时Δ=9>0两根间有负(排除)", sp.discriminant(x**2+(m-2)*x+1, x).subs(m,5) > 0)
# 挑刺: ①Δ<0⇒∅太绝对(开口向上>0解集R) ②同乘-1忘翻号
chk("挑刺①-x=0时x²+1=1>0恒成立(解集R非∅)", (x**2+1).subs(x,0) > 0)
chk("挑刺②-x=2时-4+8-3=1>0(2在解集·小明答案域不含2)", (-x**2+4*x-3).subs(x,2) > 0)
# 解答1: (x−40)(200−2x)≥1600 => 60≤x≤80
chk("解答1-零点解得60,80", sorted(sp.solve((x-40)*(200-2*x)-1600, x)) == [60,80])
chk("解答1-x=60时恰1600", ((x-40)*(200-2*x)).subs(x,60) == 1600)
chk("解答1-x=80时恰1600", ((x-40)*(200-2*x)).subs(x,80) == 1600)
chk("解答1-x=70时1800≥1600", ((x-40)*(200-2*x)).subs(x,70) == 1800)
chk("解答1-x=50时1000<1600出局", ((x-40)*(200-2*x)).subs(x,50) < 1600)
# 解答2⑴: x²−2ax+2>0恒成立 => −√2<a<√2
d = 4*a**2-8
chk("解答2⑴-a=1.4时Δ<0", d.subs(a,sp.Rational(7,5)) < 0)
chk("解答2⑴-a=1.5时Δ=1>0(出局)", d.subs(a,sp.Rational(3,2)) > 0)
chk("解答2⑴-a=-1.5时Δ=1>0(出局)", d.subs(a,sp.Rational(-3,2)) > 0)
f = x**2-2*a*x+2
# 解答2⑵: 对一切x∈[1,3]恒成立 => a<√2
chk("解答2⑵-a=-10时f(1)=23>0(宽域含)", f.subs({a:-10,x:1}) == 23)
chk("解答2⑵-a=1.4时顶点值0.04>0", f.subs({a:sp.Rational(7,5),x:sp.Rational(7,5)}) > 0)
chk("解答2⑵-a=1.5时f(1.5)=-0.25<0(出局)", f.subs({a:sp.Rational(3,2),x:sp.Rational(3,2)}) < 0)
chk("解答2⑵-a<1时x=1为最小·a=0时f(1)=3>0", f.subs({a:0,x:1}) == 3)
print("===== 汇总 =====")
print(f"总验点 {n} · 失败 {fail} · " + ("ALL PASS" if fail==0 else "HAS FAIL"))
import sys; sys.exit(1 if fail else 0)
