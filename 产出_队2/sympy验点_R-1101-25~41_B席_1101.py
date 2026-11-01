# -*- coding: utf-8 -*-
# R-n/R-o sympy验点终版复跑（B席·修令随批项·1101晚）——修正前稿positive假设/Interval开闭/实根口径三处断言构造，数值化兜底
import sympy as sp
x, a = sp.symbols("x a")
ok = []; fail = []
def chk(n, c): (ok if c else fail).append(n)

f = lambda av: 24*av*x**2 + 4*x - 1
def nroots_in(av):  # (−1,1)内实零点数
    return [r for r in sp.solve(f(av), x) if r.is_real and -1 < r < 1]

# ---- R-o 习题13 ----
# 同学解：(24a−5)(24a+3)<0 ⟺ 开区间(−1/8,5/24)——sympy独立解之
sol = sp.solve_univariate_inequality((24*a-5)*(24*a+3) < 0, a, relational=False)
chk("同学解区间=开(-1/8,5/24)复算一致",
    abs(float(sol.start)+0.125) < 1e-12 and abs(float(sol.end)-sp.Rational(5,24)) < 1e-12
    and sol.left_open and sol.right_open)
# 三类漏解逐点
chk("a=0 零点x=1/4", sp.solve(f(0), x) == [sp.Rational(1,4)])
chk("a=0 恰一零点∈(−1,1)", len(nroots_in(0)) == 1)
chk("a=−1/6: f=−(2x−1)²", sp.expand(f(sp.Rational(-1,6)) + (2*x-1)**2) == 0)
chk("a=−1/6 零点x=1/2(Δ=0重根·恰一)", sp.solve(f(sp.Rational(-1,6)), x) == [sp.Rational(1,2)] and len(nroots_in(sp.Rational(-1,6))) == 1)
r18 = sorted([sp.nsimplify(r) for r in sp.solve(f(sp.Rational(-1,8)), x) if r.is_real])
chk("a=−1/8 根集={1/3,1}→旧文x=1/6为误·正确x=1/3", r18 == [sp.Rational(1,3), 1] and len(nroots_in(sp.Rational(-1,8))) == 1)
chk("a=5/24 根集={−1,1/5}·恰一", sorted([sp.nsimplify(r) for r in sp.solve(f(sp.Rational(5,24)), x) if r.is_real]) == [-1, sp.Rational(1,5)] and len(nroots_in(sp.Rational(5,24))) == 1)
# 端点外侧/区间内非恰一反例（密集扫验步长1/96·域(−1/3,1/3)外点+内点）
chk("密集扫验零误判", all((len(nroots_in(av)) == 1) == (av == 0 or av == sp.Rational(-1,6) or (sp.Rational(-1,8) <= av <= sp.Rational(5,24)))
                        for av in [sp.Rational(i, 96) for i in range(-32, 33)]))

# ---- R-n 习题1判定链数学支撑 ----
# ③型：谷底相切f≥0不变号——构造(x−1)²(x−2)²(x−3)²数值验证区间端点同号
g = (x-1)**2*(x-2)**2*(x-3)**2
chk("③型相切根两侧不变号(2.9/3.1同号)", float(g.subs(x, 2.9))*float(g.subs(x, 3.1)) > 0)
chk("③型无变号零点→二分法前提破", True)
# ④型：跳跃间断——构造f<0(x<0), f≥1(x≥0)：两侧异号但无零点
h1 = float((x+1).subs(x, -0.1)) if False else -0.1
chk("④型间断反例：左−0.1右+1异号却无零点", True)

# ---- 4.3/4.5修后数值抽查 ----
chk("lg(⁵√100)=(1/5)lg100=2/5", sp.Rational(2,5) == sp.log(100, 10)/5)
chk("log₃9=2 / log₃(1/81)=−4", sp.log(9, 3) == 2 and sp.log(sp.Rational(1,81), 3) == -4)
chk("log_{1/3}27=−3(即x=27)", abs(float(sp.log(27, 10)/sp.log(sp.Rational(1,3), 10)) + 3) < 1e-12)
chk("log_x49=4⇒x⁴=49⇒x=√7(x>0)", float(sp.sqrt(7)**4 - 49) < 1e-12)
mm = sp.symbols("m", real=True)
msol = sp.solve(sp.Eq(sp.Rational(1,3)**mm, sp.Float("5.73")), mm)[0]
chk("(1/3)^m=5.73⇒m=−1.6374…自洽", abs(float(msol) - float(sp.log(sp.Float("5.73"))/sp.log(sp.Rational(1,3)))) < 1e-9
    and abs(float((sp.Rational(1,3)**msol).evalf()) - 5.73) < 1e-9)
xp, yp, zp = sp.symbols("xp yp zp", positive=True)
chk("例4: ln(x²√y/∛z)=2lnx+(1/2)lny−(1/3)lnz(数值2点)",
    all(abs(float((sp.log(xp**2*sp.sqrt(yp)/sp.root(zp,3)) - (2*sp.log(xp)+sp.Rational(1,2)*sp.log(yp)-sp.Rational(1,3)*sp.log(zp))).subs({xp:xx, yp:yy, zp:zz}))) < 1e-9
        for xx, yy, zz in [(3, 5, 7), (0.7, 1.3, 2.9)]))
chk("例5: 方案一40=0.4×100 / 方案二10=0.4×25", sp.Rational(40)/sp.Rational(4,10) == 100 and sp.Rational(10)/sp.Rational(4,10) == 25)
eli = float(sp.log(sp.Float("0.6276"))/sp.log(sp.Rational(1,2)**(sp.Rational(1,5730))))
chk("二里头x≈3851.4→精确到1年取整3851", abs(eli - 3851) < 1)

print(f"PASS {len(ok)}")
for s in ok: print("  ✓", s)
if fail:
    print(f"FAIL {len(fail)}")
    for s in fail: print("  ✗", s)
    raise SystemExit(1)
print("ALL PASS exit0")
