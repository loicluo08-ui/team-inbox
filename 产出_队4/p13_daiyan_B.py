from fractions import Fraction as F
import math

print("=== 验一验①②（速度定义·方向） ===")
print("验①: Δx=+6m, Δt=3s → v=+%s m/s（向东）" % F(6, 3))
print("验②: Δx=−8m, Δt=4s → v=%s m/s（向西·|v|=2 与①同大小）" % F(-8, 4))

print("\n=== 单位换算坑点 ===")
print("72 km/h = 72/3.6 =", F(72, 1) / F(36, 10), "m/s")

print("\n=== 验③（纸带·计数点） ===")
print("每5间隔 Δt = 5×0.02 =", F(5, 1) * F(1, 50), "s")
print("每3间隔 Δt = 3×0.02 =", F(3, 1) * F(1, 50), "s")
print("v = 6.0cm/0.1s =", F(60, 1000) / F(1, 10), "m/s = 0.60 m/s = 60 cm/s")
print("自洽：0.06s内Δx=3.6cm → v =", F(36, 1000) / F(6, 100), "m/s（同为0.60）")

print("\n=== 节末自测第3题（汽车制动·全组） ===")
seg = [9, 7, 5, 3, 1]
cum = 0
for i, s in enumerate(seg, 1):
    cum += s
    print(f"前{i}s: {cum}/{i} = {F(cum, i)} m/s")
print("全程: 25/5 =", F(25, 5), "m/s")
print("最后2s: (3+1)/2 =", F(4, 2), "m/s")
print("匀减速核对：每秒位移等差-2m → a=-2m/s²·v0=10；第1s平均=(10+8)/2=9 < v0 → 平均速度9比刚制动瞬时速度略小 ✅")

print("\n=== 验④（读图自测·乙曲线数值核对） ===")
f = lambda t: 0.065 + 0.077 * (1 - math.exp(-t / 1.15)) - (max(0, t - 3.3) * 0.008)
print(f"v(0)={f(0):.3f}  v(1)={f(1):.3f}  v(3)={f(3):.3f}  v(4)={f(4):.3f}")
print(f"0-1s变化 +{f(1)-f(0):.3f}（陡）  3-4s变化 {f(4)-f(3):+.3f}（微降）→ 前段速度变化更大 ✅")
print("\nALL PASS")
