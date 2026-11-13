# -*- coding: utf-8 -*-
# 并行搜索员A·队4席·物理1.3升格·闸3 sympy机器代验（v2.3工序七·57条#9）
# 对象=升格新增试题与真题全部可机器验数值点 · 结果留痕sympy_物理1.3_梯度题验点_1114.txt
import sympy as sp

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择2：后8s位移=60-30=30 m → v=30/8=3.75 m/s
r1 = sp.Rational(60 - 30, 8)
check("T1_选择2 30/8=3.75 m/s", r1 == sp.Rational(15, 4) and float(r1) == 3.75, f"30/8={r1}")

# T2 选择3：往返平均速度=0；平均速率=2/(1/8+1/2)=3.2 m/s（调和平均·B陷阱）
s = sp.Symbol('s', positive=True)
v_avg_rate = 2*s / (s/8 + s/2)
check("T2_选择3 平均速度0·平均速率3.2", sp.simplify(v_avg_rate) == sp.Rational(16, 5) and float(v_avg_rate) == 3.2, f"2s/(s/8+s/2)={sp.simplify(v_avg_rate)}")

# T3 填空：5间隔×0.02s=0.1s；v=0.060/0.1=0.6 m/s
r3t = 5 * sp.Rational(2, 100)
r3v = sp.Rational(60, 1000) / r3t
check("T3_填空 0.060/0.1=0.6 m/s", r3t == sp.Rational(1, 10) and r3v == sp.Rational(3, 5) and float(r3v) == 0.6, f"t={r3t}·v={r3v}")

# T4 解答1：总位移80 m/总时间15 s→80/15=16/3≈5.33；加段后90/20=4.5
r4a = sp.Rational(6*10 + 4*5, 15)
r4b = sp.Rational(80 + 2*5, 20)
check("T4_解答1 80/15≈5.33·90/20=4.5", r4a == sp.Rational(16, 3) and r4b == sp.Rational(9, 2), f"80/15={r4a}≈{float(r4a):.2f}·90/20={r4b}")

# T5 解答2：OA 40/20=2；总位移√(40²+30²)=50；平均速度50/50=1；平均速率(40+36)/50=1.52
r5a = sp.Rational(40, 20)
r5d = sp.sqrt(40**2 + 30**2)
r5b = r5d / 50
r5c = sp.Rational(40 + 36, 50)
check("T5_解答2 2·50·1·1.52", r5a == 2 and r5d == 50 and r5b == 1 and r5c == sp.Rational(38, 25) and float(r5c) == 1.52, f"v_OA={r5a}·d={r5d}·v_全={r5b}·v率={r5c}")

# T6 真题玉兔T4解析数值：135×1.6=216 N（月面g≈1.6）·135×10=1350 N（地球g=10误用）
r6a = sp.Rational(135, 1) * sp.Rational(16, 10)
r6b = 135 * 10
check("T6_玉兔T4 135×1.6=216·135×10=1350", r6a == 216 and r6b == 1350, f"月面≈{r6a} N·地球误算={r6b} N")

# T7 既有账复跑（1031账维持）：48 km/h反例=2/(1/60+1/40)=48
s2 = sp.Symbol('s2', positive=True)
r7 = 2*s2 / (s2/60 + s2/40)
check("T7_既有pit反例 48km/h复跑", sp.simplify(r7) == 48, f"2/(1/60+1/40)={sp.simplify(r7)}")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 物理1.3升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
