# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·数学4.5新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
# 结果留痕：sympy_数学4.5_梯度题验点_1114.txt
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
x = sp.symbols('x', real=True)

# T1 选择1：x²−3x+2零点=1和2（答案B）
check("T1_选择1 零点{1,2}（答案B）", sorted(sp.solve(x**2-3*x+2, x)) == [1, 2], "因式分解(x−1)(x−2)")

# T2 选择2：f(x)=lnx+2x−6 变号区间(2,3)（答案B）
f2 = sp.log(x) + 2*x - 6
check("T2_选择2 f(2)<0·f(3)>0→(2,3)（答案B）", float(f2.subs(x, 2).evalf(4)) < 0 < float(f2.subs(x, 3).evalf(4)), f"f(2)={float(f2.subs(x,2).evalf(4))}·f(3)={float(f2.subs(x,3).evalf(4))}")

# T3 选择3：f(3)<0→新笼(3,4)→第二次中点3.5（答案D）
check("T3_选择3 第二次中点3.5（答案D）", sp.Rational(3+4, 2) == sp.Rational(7,2), "(3+4)/2=3.5")

# T4 填空：0.5/2^k<0.1 → 2^k>5 → k=3
lens = [sp.Rational(1,2)/(2**k) for k in [1,2,3]]
check("T4_填空 至少3次（0.0625<0.1）", lens[2] == sp.Rational(1,16) and float(lens[1]) >= 0.1 and float(lens[2]) < 0.1, f"三次后长={lens[2]}")

# T5 挑刺②：f(1.5)=0.25>0·f(1)=−1<0→变号区间(1,1.5)（小华说(1.5,2)错）
f5 = x**2 - 2
check("T5_挑刺② f(1.5)=0.25>0·f(1)<0→零点在(1,1.5)", float(f5.subs(x, sp.Rational(3,2))) == 0.25 and f5.subs(x, 1) == -1 and f5.subs(x, 2) == 2, "异号区间=(1,1.5)")

# T6 解答1：x³−4x=x(x−2)(x+2)→零点{−2,0,2}·f(1)=−3<0·f(3)=15>0→(1,3)内存在
f6 = x**3 - 4*x
check("T6_解答1 零点{−2,0,2}·(1,3)内存在x=2", sorted(sp.solve(f6, x)) == [-2, 0, 2] and f6.subs(x, 1) == -3 and f6.subs(x, 3) == 15 and 2 in sp.solve(f6, x), "因式分解+变号核")

# T7 解答2：2⁹=512<1000<1024=2¹⁰·增量1024−512=512
check("T7_解答2 第10天突破·增量512台", sp.Integer(2)**9 == 512 and sp.Integer(2)**10 == 1024 and 1024-512 == 512, "指数爆炸特征")

# T8 真题①（2020新高考ⅠT6）：r=(3.28−1)/6=0.38·t=ln2/0.38≈1.82≈1.8（答案B）
r8 = sp.Rational(228, 100)/6
t8 = float(sp.log(2).evalf(6))/0.38
check("T8_真题① r=0.38·t≈1.82≈1.8天（答案B）", r8 == sp.Rational(19,50) and 1.7 < t8 < 1.9, f"r={float(r8)}·t={t8:.4f}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 数学4.5升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
