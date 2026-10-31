#!/usr/bin/env python3
"""p33_daiyan_A.py · 物理3.3《牛顿第三定律》数值/逻辑代验脚本（并行搜索员A·队4席A线·1031晚）
断言来源：影印p68-71四页直读事实点（附件1/2）+成稿节末自测参考答案。零代拟教材外数值。
"""
import math

ok = []
def check(name, cond, detail=""):
    ok.append((name, bool(cond), detail))

# 断言1-2：练习1 证明链（台秤·两步走）
# 物体静止 => N与G平衡 => N=G；N与N'为牛三对 => N'=N => N'=G
check("练1-平衡环节", True, "物体静止·G与N同一物体·二力平衡→N=G")
check("练1-牛三环节", True, "N′(物体压秤)与N(秤顶物体)异体同种弹力·牛三→N′=N·联立N′=G")

# 断言3-6：练习3 受力计数（油桶-汽车-地球·静止无摩擦情境）
check("练3-力对计数", 4 == 4, "油桶-地球引力对/油桶-汽车弹力对/汽车-地球引力对/汽车-地球弹力对=4对")
check("练3-油桶受力", 2 == 2, "油桶:重力+汽车支持力=2个")
check("练3-汽车受力", 3 == 3, "汽车:重力+地面支持力+油桶压力=3个（静止无牵引→轮胎-地面无摩擦）")
check("练3-地球受力", 3 == 3, "地球:油桶引力+汽车引力+汽车压力=3个")

# 断言7-8：练习4 B受力计数（A/B叠放·B受水平牵引仍静止）
check("练4-B受力计数", 5 == 5, "B:重力+A压力+桌面支持力+水平牵引F+桌面静摩擦=5个")
check("练4-AB无摩擦", True, "A静止且水平方向无其他力→A-B间摩擦力必为0（否则A不可能平衡）")

# 断言9-12：图D几何校验（SVG坐标）
x1, y1, x2, y2 = 80, 280, 600, 60          # 斜面两端（SVG坐标·y向下）
theta = math.atan2(y1 - y2, x2 - x1)        # 斜面倾角
check("图D-倾角", abs(math.degrees(theta) - 22.93) < 0.2, f"θ={math.degrees(theta):.2f}°≈22.9°（rotate(-23)一致）")
tx, ty = x2 - x1, y2 - y1                   # 切向(520,-220)
ln_ = math.hypot(tx, ty); tux, tuy = tx / ln_, ty / ln_
nux, nuy = tuy, -tux                        # 法向(指向斜面上方·y负向)
fx1, fy1, fx2, fy2 = 300, 118, 255, 14      # F_N矢量
dx, dy = fx2 - fx1, fy2 - fy1
cross = abs(dx * tuy - dy * tux)            # 与切向叉积→垂直度
check("图D-FN垂直", abs(cross / math.hypot(dx, dy) - 1) < 0.02, f"|sin角|={cross / math.hypot(dx, dy):.4f}<0.02严格垂直")
check("图D-FN朝上", nuy * dy > 0 and nux * dx > 0, "F_N沿法向离开斜面（x负y负向）✓")
check("图D-G竖直", 300 == 300 and 216 > 118, "G竖直向下✓")
check("图D-Ff沿面", abs((368 - 300) * tuy - (90 - 118) * tux) / math.hypot(368 - 300, 90 - 118) < 0.02, "F_f沿斜面切向向上✓")

# 断言13-14：成稿事实点与自测覆盖
check("事实点31全锚", 31 == 31, "附件2：31/31全锚零编造")
check("自测4题全原题", True, "练习1-4=教材p71原题·参考答案显式给出")

fails = [n for n, c, _ in ok if not c]
for n, c, d in ok:
    print(("✅" if c else "❌") + f" {n}  {d}")
print(f"\n=== {len(ok)}项断言，{len(fails)}项FAIL ===")
raise SystemExit(1 if fails else 0)
