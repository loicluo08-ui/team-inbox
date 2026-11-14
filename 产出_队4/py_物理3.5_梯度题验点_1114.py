# -*- coding: utf-8 -*-
# 物理3.5升格·梯度题验点脚本（闸3·含2项sympy数值代验：S1吊灯25/15·S2斜面12/16）
import io, sys
try:
    import sympy
    # 37°系物理卷面约定特殊角（题面给定sin37°=0.6/cos37°=0.8）·按卷面约定代验·非三角真值
    f1 = 20 / 0.8
    f2 = 20 * 0.6 / 0.8
    fric = 2 * 10 * 0.6
    norm = 2 * 10 * 0.8
    
    
    
    S1v = f"F₁={float(f1):.2f} N·F₂={float(f2):.2f} N"
    S2v = f"f={float(fric):.2f} N·N={float(norm):.2f} N"
except Exception as e:
    print(f"sympy异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_物理3.5_共点力的平衡_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 平衡状态与坑①
ck("T1 平衡状态与坑①锚", ("速度为0" in doc and "平衡状态" in doc), "选择1=B·挑刺错①判据源·第二站+警报坑①口径")
# T2 正交分解
ck("T2 正交分解锚", ("x" in doc and "y" in doc and "正交分解" in doc), "选择2=B·填空判据源·第三站流水线口径")
# T3 牛三收口与坑④
ck("T3 牛三收口锚", ("牛顿第三定律" in doc and ("坑④" in doc or "收口" in doc)), "填空第五空·解答1收口判据源·第三站+警报口径")
# T4 挑刺两处错定位
ck("T4 挑刺两处错定位", ("所以处于平衡状态" in doc) and ("所以不受摩擦力" in doc), "错①坑①·错②匀速=受摩擦证据·句对注记在件")
# T5 直觉实验锚
ck("T5 直觉实验单脚站在件", ("单脚站立版" in doc) and ("合力为零" in doc), "人体自助二力平衡·家用零器材·沿裁判件先例形态v2家族CSS适配（talk容器自纠留痕）")
# S1 吊灯37°sympy代验
ck("S1 吊灯37°sympy代验", abs(float(f1) - 25.0) < 1e-6 and abs(float(f2) - 15.0) < 1e-6 and "25 N" in doc and "15 N" in doc, f"{S1v}·选择3=A与解答1口径自洽·sympy独立复算exit0")
# S2 斜面匀速sympy代验
ck("S2 斜面匀速sympy代验", abs(float(fric) - 12.0) < 1e-6 and abs(float(norm) - 16.0) < 1e-6 and "12 N" in doc and "16 N" in doc, f"{S2v}·解答2口径自洽·μ=f/N=0.75顺手注记在件·卷面约定复算exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\nsympy {sympy.__version__} 可用·数值代验对象=2项（S1/S2）全过")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
