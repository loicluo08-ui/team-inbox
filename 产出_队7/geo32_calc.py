#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""geo32_calc.py · 地理3.2 大气受热过程 · SVG坐标代验（队7席·1031晚）
1) 图3-14不同性质地面的反射率条形图：SVG y坐标换算（教材p80逐值直读）
2) -18℃→15℃保温意义温差代验（教材p81阅读）
"""
# ---------- 1) 反射率条形图（教材p80 图3-14 逐值） ----------
# SVG绘图区：y_top=60(100%), y_base=460(0%)  => 1% = 4px
Y_TOP, Y_BASE = 60.0, 460.0
SCALE = (Y_BASE - Y_TOP) / 100.0  # 4.0 px/%

bars = [
    ("城市水泥路面", "40~50", 45),   # 区间取中值45作条高，标注写区间
    ("沙土", "29~35", 32),
    ("黏土", "20", 20),
    ("浅色土", "22~32", 27),
    ("深色土", "10~15", 12.5),
    ("草地", "26", 26),
    ("耕地", "14", 14),
    ("新雪", "84~95", 89.5),
    ("冰", "50", 50),
    ("海洋(平均)", "7", 7),
    ("海洋(赤道)", "2", 2),
]
print("== 图3-14 反射率条形 y坐标（svg top = %.0f - v*%.1f） ==" % (Y_BASE, SCALE))
for name, label, v in bars:
    h = v * SCALE
    top = Y_BASE - h
    print(f"  {name:8s} {label:>6s}% 条高={h:6.1f}px top_y={top:6.1f} 标注y={top-8:.1f}")
# 校验：新雪最高、海洋赤道最低
hs = {n: v for n, _, v in bars}
assert hs["新雪"] == 89.5 and max(hs.values()) == hs["新雪"], "新雪应为最高"
assert hs["海洋(赤道)"] == 2 and min(hs.values()) == hs["海洋(赤道)"], "海洋赤道应为最低"
print("  [OK] 极值校验：新雪84~95最高 / 海洋赤道2最低 —— 与教材图3-14一致")

# ---------- 2) 保温意义温差代验（教材p81 阅读） ----------
no_atm = -18.0   # 无大气保温：地球表面平均气温
with_atm = 15.0  # 有大气保温：地球表面平均气温
delta = with_atm - no_atm
print(f"\n== 保温作用温差代验 ==\n  无大气 {no_atm}℃ → 有大气 {with_atm}℃，提升 {delta}℃")
assert delta == 33.0
# 截留比例区间（教材p80：75%~95%）
lo, hi = 75.0, 95.0
print(f"  地面辐射被截留比例 {lo}%~{hi}%（教材p80原话'绝大部分（75%~95%）都被截留在大气中'）")
# 月球昼夜温差（教材p82活动）
moon_day, moon_night = 127.0, -183.0
moon_range = moon_day - moon_night
print(f"  月球赤道午间{moon_day}℃/夜最低{moon_night}℃，昼夜温差{moon_range}℃（活动2(1)）")
assert moon_range == 310.0
print("\n[ALL OK] geo32_calc.py 三组代验全部通过")
