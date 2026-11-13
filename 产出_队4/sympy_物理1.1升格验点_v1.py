#!/usr/bin/env python3
# sympy_物理1.1升格验点_v1.py（队4席·并行搜索员A·1114）
# 升格新增数值点逐项独立复算（先例：附件2 机器可验数值点汇总口径·sympy 1.14.0）
from sympy import Rational
import sys

results = []
ok = True

# 点1：解答1——地球直径/地日距离 不到万分之一（教材p12数据·复算）
r1 = Rational(13000, 150000000)          # 1.3e4 / 1.5e8
p1 = float(r1) < 1e-4 and abs(float(r1) - 0.87e-4) < 0.01e-4
results.append(("点1 地球直径/地日距离=8.67e-5<1e-4（0.87×10⁻⁴）", str(r1)[:22], p1))

# 点2：填空——反向相对速度 10+6=16
r2 = Rational(10) + Rational(6)
p2 = r2 == 16
results.append(("点2 填空 反向相对速度 10+6=16", str(r2), p2))

# 点3：解答2⑵——参考系变换 20-5=15
r3 = Rational(20) - Rational(5)
p3 = r3 == 15
results.append(("点3 解答2 车厢向后抛球5 地面系 20-5=15", str(r3), p3))

# 点4：选择1过桥时间式逻辑自洽（过桥=(桥长+车长)/v>桥长/v·车长不可忽略）
t_bridge = Rational(1000 + 200, 20)       # 桥1km 车200m v=20m/s
t_nopoint = Rational(1000, 20)
p4 = t_bridge > t_nopoint
results.append(("点4 过桥时间=(桥长+车长)/v>桥长/v（车长进算式不可忽略）", f"{t_bridge} > {t_nopoint}", p4))

for name, val, passed in results:
    print(f"{'✅' if passed else '❌'} {name} · sympy={val}")
    ok = ok and passed

print(f"\n=== 升格新增数值点 {len(results)} 项，{'全过 exit0' if ok else '有伤 exit1'} ===")
sys.exit(0 if ok else 1)
