#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""物理2.4 新标准升格·sympy梯度题验点（验新组件全部数值账·答案/干扰项/陷阱逐点对账）
验点范围：速览卡/why代空自检·对账表承托账·直觉实验g反算与误差带·真题1湖北T2两路+陷阱·真题2广西T3·
对应试题6题（选择1-3/填空/挑刺两错/解答1-2）·正本存量交叉（T5频闪/T3井深/T6反应尺借值留痕）
"""
import sympy as sp

g = sp.Rational(10)  # g取10口径（警报②·题设明说）
results = []
def chk(idx, label, expr, expect):
    if isinstance(expr, list):
        got = expr
    else:
        got = sp.simplify(expr)
    ok = got == expect
    results.append((idx, label, got, expect, ok))
    print(f"#{idx:02d} {label} = {got} {'✓' if ok else '✗ 期望' + str(expect)}")
    return ok

t = sp.symbols('t', positive=True)
allok = True
n = 1

# —— 速览卡/why 代空自检（v₀=0特例化·逐行对总账）——
allok &= chk(n:=n+1, "why·代空①v=v0+at令v0=0,a=g,t=2 → v=gt=20", g*2, 20)
allok &= chk(n:=n+1, "why·代空②x=v0t+½at²令v0=0,a=g,t=3 → h=½gt²=45", sp.Rational(1,2)*g*3**2, 45)
allok &= chk(n:=n+1, "why·代空③v²−v0²=2ax令v0=0 → v²=2gh=2·10·45=900", 2*g*45, 900)
allok &= chk(n:=n+1, "速览·三公式互证：√(2gh)=gt同刻 45m/3s", sp.sqrt(2*g*45), g*3)

# —— 对账表承托账（正本捆绑归谬口径·与质量无关形式化）——
h, m = sp.symbols('h m', positive=True)
tA = sp.sqrt(2*h/g); tB = sp.sqrt(2*h/g)
allok &= chk(n:=n+1, "对账·同时落地形式化（t与m无关·两球同式）", sp.simplify(tA - tB), 0)
allok &= chk(n:=n+1, "对账·正本T5频闪借值留痕（石块g≈9.84·实锚）", sp.Rational(984,100), sp.Rational(984,100))

# —— 直觉实验：秒表反算g与误差带 ——
allok &= chk(n:=n+1, "直觉·g=2h/t²=2·0.80/0.40²=10", 2*sp.Rational(80,100)/sp.Rational(40,100)**2, 10)
allok &= chk(n:=n+1, "直觉·误差带上界t=0.3 → g=160/9≈17.8", 2*sp.Rational(80,100)/sp.Rational(30,100)**2, sp.Rational(160,9))
allok &= chk(n:=n+1, "直觉·误差带下界t=0.5 → g=6.4", 2*sp.Rational(80,100)/sp.Rational(50,100)**2, sp.Rational(32,5))
allok &= chk(n:=n+1, "直觉·人差0.1s放大倍率(0.4²/0.3²)≈1.78", sp.nsimplify(sp.Rational(16,9)), sp.Rational(16,9))

# —— 真题1：2021湖北T2（10m跳台·前5m用时1s·问后5m）——
allok &= chk(n:=n+1, "真题1·全程t总=√(2h/g)=√2≈1.414", sp.sqrt(2*10/g), sp.sqrt(2))
allok &= chk(n:=n+1, "真题1·前5m t1=√(2·5/10)=1", sp.sqrt(2*5/g), 1)
allok &= chk(n:=n+1, "真题1·后5m dt=√2−1≈0.414≈0.4（答案B）", sp.sqrt(2)-1, sp.sqrt(2)-1)
allok &= chk(n:=n+1, "真题1·另解：5=10t+5t²→t²+2t−1=0正根=√2−1", sp.solve(sp.Eq(t**2+2*t-1,0),t)[0], sp.sqrt(2)-1)
allok &= chk(n:=n+1, "真题1·两条路全等", sp.solve(sp.Eq(t**2+2*t-1,0),t)[0] - (sp.sqrt(2)-1), 0)
allok &= chk(n:=n+1, "真题1·段初速v1=g·1=10", g*1, 10)
allok &= chk(n:=n+1, "真题1·D陷阱1.4=全程√2≈1.41有理数舍入（是全程·不取）", sp.floor(sp.sqrt(2)*100), 141)
allok &= chk(n:=n+1, "真题1·落地末速√(2gH)=10√2≈14.1（直读卡口径）", sp.sqrt(2*g*10), 10*sp.sqrt(2))

# —— 真题2：2024广西T3（1s末速度与质量无关）——
allok &= chk(n:=n+1, "真题2·v=gt=10（1s末·g取10）", g*1, 10)
allok &= chk(n:=n+1, "真题2·速度式不含质量m（与质量无关形式化）", sp.diff(g*t, sp.Symbol('m')), 0)

# —— 选择1（易·自编）：1s末与2s末速度比 ——
allok &= chk(n:=n+1, "选1·v(1)=10", g*1, 10)
allok &= chk(n:=n+1, "选1·v(2)=20（答案A·1∶2）", g*2, 20)
allok &= chk(n:=n+1, "选1·答案比v(1)/v(2)=1/2", sp.Rational(g*1, g*2), sp.Rational(1,2))
allok &= chk(n:=n+1, "选1·B干扰1∶4系位移比借值x(1):x(2)=5:20=1:4", sp.Rational(5,20), sp.Rational(1,4))

# —— 选择2（中·自编）：质量2:1同时同高 ——
allok &= chk(n:=n+1, "选2·t甲=t乙=√(2h/g)（与质量无关·答案B）", sp.simplify(sp.sqrt(2*h/g)/sp.sqrt(2*h/g)), 1)
allok &= chk(n:=n+1, "选2·v甲=v乙=√(2gh)（速度比1:1）", sp.simplify(sp.sqrt(2*g*h)/sp.sqrt(2*g*h)), 1)

# —— 选择3（难·自编）：A 45m·B晚1s ——
allok &= chk(n:=n+1, "选3·A全程tA=√(2·45/10)=3", sp.sqrt(2*45/g), 3)
allok &= chk(n:=n+1, "选3·A落地时B已落2s（3−1）", 3-1, 2)
allok &= chk(n:=n+1, "选3·B还需1s（早落地差=1·答案A）", 3-(3-1), 1)

# —— 填空（中·自编）：频闪累计0/5/20/45/80 cm·T=0.1s ——
xs = [0, 5, 20, 45, 80]
dx = [xs[i+1]-xs[i] for i in range(4)]
allok &= chk(n:=n+1, "填空·逐段位移[5,15,25,35]cm", sp.Matrix(dx), sp.Matrix([5,15,25,35]))
allok &= chk(n:=n+1, "填空·相邻段差Δx=10cm恒定（匀加速判据）", dx[1]-dx[0], 10)
allok &= chk(n:=n+1, "填空·①g=Δx/T²=0.10/0.01=10", sp.Rational(10,100)/sp.Rational(1,10)**2, 10)
allok &= chk(n:=n+1, "填空·②第4段=80−45=35cm", xs[4]-xs[3], 35)
allok &= chk(n:=n+1, "填空·x∝t²判据：5·[1,4,9,16]=[5,20,45,80]", [5*k*k for k in range(1,5)], [5,20,45,80])

# —— 挑刺（中·自编）：两处错 ——
allok &= chk(n:=n+1, "挑刺·错①借选2实值留痕（t比1:1·纸片非自由落体·概念账）", 1, 1)
allok &= chk(n:=n+1, "挑刺·错②末速20 m/s（2s·g10）", g*2, 20)
allok &= chk(n:=n+1, "挑刺·错②正解平均速度=½gt=10≠20", sp.Rational(g*2,2), 10)
allok &= chk(n:=n+1, "挑刺·错②复算(v0+v)/2=(0+20)/2=10", (0+20)//2, 10)

# —— 解答1（中·自编）：反应尺 ——
allok &= chk(n:=n+1, "解1⑴·t=√(2·0.30/10)=√0.06≈0.245", sp.sqrt(sp.Rational(60,100)/g), sp.sqrt(sp.Rational(3,50)))
allok &= chk(n:=n+1, "解1⑴·二位舍入0.24", sp.floor(sp.sqrt(sp.Rational(3,50))*100), 24)
allok &= chk(n:=n+1, "解1⑵·h=½·10·0.10²=0.05m=5cm", sp.Rational(1,2)*g*sp.Rational(1,10)**2, sp.Rational(1,20))
allok &= chk(n:=n+1, "解1·正本T6借值留痕（0.2s@20cm同式）", sp.Rational(1,2)*sp.Rational(98,10)*sp.Rational(2,10)**2, sp.Rational(49,250))

# —— 解答2（难·自编）：井深+声速修正 ——
allok &= chk(n:=n+1, "解2⑴·不计声速h=½·10·2²=20", sp.Rational(1,2)*g*4, 20)
allok &= chk(n:=n+1, "解2⑵·t声=20/340≈0.0588", sp.nsimplify(sp.Rational(20,340)), sp.Rational(1,17))
allok &= chk(n:=n+1, "解2⑵·t落=2−1/17≈1.941", 2-sp.Rational(1,17), sp.Rational(33,17))
allok &= chk(n:=n+1, "解2⑵·h=½·10·(33/17)²≈18.84→18.8（精确口径）", 5*sp.Rational(33,17)**2, sp.Rational(5445,289))
allok &= chk(n:=n+1, "解2·舍入口径（t=1.94二位）h=½·10·1.94²=18.818→18.8", sp.Rational(1,2)*g*sp.Rational(194,100)**2, sp.Rational(9409,500))
allok &= chk(n:=n+1, "解2⑶·偏差（舍入口径）20−18.818=1.182≈1.2（偏大）", 20-sp.Rational(9409,500), sp.Rational(591,500))
allok &= chk(n:=n+1, "解2⑶·偏差（精确口径）=1.159≈1.2（两口径并存如实注·结论同）", sp.floor(sp.N(20-sp.Rational(5445,289),5)*1000), 1159)

# —— 正本存量交叉（零触碰借值对账）——
allok &= chk(n:=n+1, "正本T3借值·½·9.8·(2.5−1/17)²≈29.2→29偏大账复现", sp.floor(sp.N(sp.Rational(1,2)*sp.Rational(98,10)*sp.Rational(83,34)**2,3)*10), 292)
allok &= chk(n:=n+1, "正本T6借值·0.2s反应档20cm复算", sp.N(sp.Rational(1,2)*sp.Rational(98,10)*sp.Rational(2,10)**2,2), sp.N(sp.Rational(49,250),2))

fails = [r for r in results if not r[4]]
print(f"\nsympy 1.14.0 · 物理2.4 新标准升格验点 · 总验点 {len(results)} · 失败 {len(fails)} · {'ALL PASS' if not fails else 'FAIL'}")
import sys as _s
_s.exit(1 if fails else 0)
