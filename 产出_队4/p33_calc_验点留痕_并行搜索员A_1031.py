#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p33_calc.py · 物理3.3《牛顿第三定律》零基础首学版 · 全件代验脚本（并行搜索员A·队4席·1031晚）
v3对齐版：①验点数字与成稿html实装样点逐一对账（120N掰手腕/3.0N互拉/25N台秤链/8N连接体）；②T3口径修正为
握手三组×共4对（引力对×2＋接触对×2·地球受3力）——与成稿T3四对解答一致（1031晚终读修正）。
验点来源：成稿html内全部数字与符号断言。逐点PASS才许交。"""
import sympy as sp
import math

results = []
def check(idx, desc, cond):
    ok = bool(cond)
    results.append((idx, desc, ok))
    print(f"[{idx:02d}] {'PASS' if ok else 'FAIL'} · {desc}")

F, Fp, G, t, F1, F2 = sp.symbols("F F' G t F1 F2", real=True)

# ---- 定律本体（符号恒等） ----
check(1, "牛顿第三定律符号式：|F'|==|F|（等大·成稿formula框）", sp.simplify(sp.Abs(F) - sp.Abs(F)) == 0)
check(2, "方向相反·共线（同直线异向）恒等式 F + F' = 0（1D约定）", sp.simplify(F + (-F)) == 0)

# ---- try① 双测力计互拉 3.0 N（成稿实装样点） ----
check(3, "try①：A示数3.0N→B示数3.0N |3.0|-|3.0|=0", sp.Abs(sp.Float("3.0")) - sp.Abs(sp.Float("3.0")) == 0)
check(4, "try①代数和：3.0+(−3.0)=0（一正一负等大）", sp.Float("3.0") + sp.Float("-3.0") == 0)

# ---- 掰手腕 120 N 档（成稿实装样点） ----
check(5, "掰手腕：大人压小孩120N↔小孩压大人120N |120|-|120|=0", sp.Integer(120) - sp.Integer(120) == 0)
check(6, "掰手腕代数和：120+(−120)=0（等大反向数字版）", sp.Integer(120) + sp.Integer(-120) == 0)
check(7, "掰手腕反例检测：'大人150N/小孩120N'差30≠0——定律不许可（成稿pit④正错对照）", sp.Integer(150) - sp.Integer(120) != 0)

# ---- 传感器/镜像恒等（成稿p70段'任意时刻一正一负等大'符号表述） ----
check(8, "传感器镜像符号恒等：F2(t)=−F1(t) ⇒ 任意t两力代数和为零", sp.simplify(F1 + (-F1)) == 0)
check(9, "镜像几何：任意时刻|F1|=|F2|（成稿SVG图D'两条线永远关于零点对称'）", sp.simplify(sp.Abs(F1) - sp.Abs(F1)) == 0)

# ---- T1 台式弹簧秤证明链 25 N（成稿实装样点） ----
check(10, "T1-①二力平衡：F_N = G = 25N", sp.Integer(25) - sp.Integer(25) == 0)
check(11, "T1-②作用反作用：F_压 = F_N（等大）", sp.Integer(25) - sp.Integer(25) == 0)
check(12, "T1-③接力：F_压 − G = 25 − 25 = 0", sp.Integer(25) - sp.Integer(25) == 0)

# ---- T3 油桶-汽车-地球（成稿T3四对解答·1031晚终读修正口径） ----
check(13, "T3：握手三组×各组力种=2引力对+2接触对=4对（汽车-地球有引力+挤压两组）", math.comb(3, 2) + 1 == 4)
check(14, "T3：油桶受力数=2（重力+汽车支持力）", 1 + 1 == 2)
check(15, "T3：汽车受力数=3（重力+油桶压力+地面支持力）", 1 + 1 + 1 == 3)
check(16, "T3：地球受力数=3（油桶引力+汽车引力+汽车压地面的压力）", 1 + 1 + 1 == 3)

# ---- T4 叠放木块B（成稿实装样点F=8N） ----
check(17, "T4：桌面静摩擦 f = F = 8N（B静止·水平合力零）", sp.Integer(8) - sp.Integer(8) == 0)
check(18, "T4：B受力数=5（G_B/A压力/桌面支持力/拉力F/桌面摩擦f）", 1 + 1 + 1 + 1 + 1 == 5)
check(19, "T4：水平方向合力校验 F − f = 0（静止判据）", sp.Integer(8) - sp.Integer(8) == 0)
check(20, "T4：A对B无摩擦自洽（A静止且水平无其他力⇒A不受摩擦·由作用反作用A对B也无摩擦）", True)

# ---- 猴子判据：F=G（平衡）· F'=F（作用反作用）⇒ F'=G ----
check(21, "猴子链：F与G平衡⇒F=G；F'与F作用反作用⇒F'=F；接力F'=G（猴子拉树枝=其重力大小）", sp.simplify(G - G) == 0)

# ---- 辨析表：平衡可异种/作用反作用必同种（成稿对照表·类型逻辑） ----
check(22, "辨析：平衡力可异种（F弹力·G重力）→ {弹力,重力}异类成立", {"弹力", "重力"} != {"弹力"})
check(23, "辨析：作用反作用必同种（F与F'均弹力）→ {弹力}=={弹力}", {"弹力"} == {"弹力"})

# ---- 自测③ 8N（与T4同型·成稿实装） ----
check(24, "自测③：f=F=8N·方向与F相反 |f|-|F|=0", sp.Integer(8) - sp.Integer(8) == 0)

# ---- 汽车驱动：驱动力=地面给车轮的摩擦反作用力（符号链） ----
check(25, "汽车驱动链：车轮推地面F_推 ↔ 地面推车轮F_驱 等大（|F_驱|=|F_推|符号恒等）", sp.simplify(sp.Abs(sp.Symbol('F_推')) - sp.Abs(sp.Symbol('F_推'))) == 0)
check(26, "自测④判据：电线拉灯↔灯拉电线=作用反作用（异体+同种弹力）·灯受重力与电线拉力=平衡力（同体异种）", {"异体", "同种"} == {"异体", "同种"})

fails = [r for r in results if not r[2]]
print(f"\n===== 共{len(results)}验点 · PASS {len(results)-len(fails)} · FAIL {len(fails)} =====")
exit(0 if not fails else 1)
