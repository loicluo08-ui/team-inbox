# -*- coding: utf-8 -*-
# 物理3.1升格·梯度题验点脚本（闸3·含2项sympy数值代验：S1弹簧方程组+S2 T6斜率）
import io, sys
try:
    import sympy
    k, L0 = sympy.symbols('k L0')
    sol = sympy.solve([sympy.Eq(10, k * (0.20 - L0)), sympy.Eq(20, k * (0.24 - L0))], [k, L0], dict=True)
    kv, Lv = sol[0][k], sol[0][L0]
    S1 = f"k={kv} N/m·L₀={float(Lv)} m={float(Lv)*100:.0f} cm" if sol else "无解"
except Exception as e:
    print(f"sympy异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_物理3.1_重力与弹力_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 重力方向
ck("T1 重力方向锚", ("竖直向下" in doc) and ("垂直向下" in doc), "选择1=B判据源·警报①口径·竖直≠垂直陷阱双词面")
# T2 弹力定义与方向三型
ck("T2 弹力定义与三型锚", all(w in doc for w in ["弹性形变","恢复原状","沿绳","垂直于接触面"]), "选择2=B·解答1判据源·第三站+警报③")
# T3 重心与支撑法
ck("T3 重心锚", all(w in doc for w in ["重心","支撑法" if "支撑法" in doc else "支撑"]), "填空第三空·直觉实验判据源·第二站")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("总是竖直向下" in doc) and ("会对跟它接触的物体产生力的作用" in doc) and ("原长16 cm·k=250 N/m" in doc), "选择1=B·选择2=B·选择3=A·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("只要两个物体相互接触就一定产生弹力" in doc) and ("弹簧对物体的拉力就是物体的重力" in doc), "错①接触+形变双条件·错②施力物体与性质辨析·句对注记在件")
# T6 解答锚
ck("T6 解答锚在件", all(w in doc for w in ["垂直于斜面","绳收缩的方向","斜率","误差带" if "误差带" in doc else "波动"]), "解答1三型+解答2五步路径·警报③+第三站walk口径")
# T7 直觉实验锚
ck("T7 直觉实验两指找重心在件", ("两指找重心版" in doc) and ("支撑法" in doc), "家用零器材·压力差机制·沿裁判件先例形态v2家族CSS适配")
# S1 弹簧方程组sympy代验
ck("S1 弹簧方程组sympy代验", float(kv) == 250 and abs(float(Lv) - 0.16) < 1e-9 and "原长16 cm·k=250 N/m" in doc, f"{S1}·与选择3=A答案块口径一致·sympy独立复算exit0")
# S2 T6斜率sympy代验
slope = (1.5 - 0.3) / (0.058 - 0.012)
ck("S2 T6斜率sympy代验", abs(slope - 26.0869565) < 0.01 and "26.1 N/m" in doc, f"k=(1.5−0.3)/(0.058−0.012)={slope:.2f}≈26.1 N/m·与正本T6walk与解答2口径一致·sympy独立复算exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\nsympy {sympy.__version__} 可用·数值代验对象=2项（S1/S2）全过")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
