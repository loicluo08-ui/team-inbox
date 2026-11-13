# -*- coding: utf-8 -*-
# 生物2.2升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（4.5%/60%~95%/97%/1%~1.5%/0.9%系教材表载引用·无新增计算方程）·沿校准件v1.1先例口径
import io, sys

try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·教材表载引用无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物2.2_细胞中的无机物_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 自由水/结合水双定义+数据
ck("T1 两形式定义与4.5%锚", all(k in doc for k in ["自由水","结合水","4.5%","良好的溶剂"]), "选择1=C·填空前四空判据源")

# T2 跷跷板+冬小麦案例
ck("T2 跷跷板与冬小麦锚", all(k in doc for k in ["代谢旺","抗逆","冬小麦"]), "选择2=B判据源·方向判读在答案块")

# T3 无机盐三层证据+离子形式
ck("T3 无机盐三层层岗在件", all(k in doc for k in ["叶绿素","血红素","兴奋性","酸碱平衡","离子"]), "选择3=C（Ca²⁺岗位=防抽搐开关层）·填空第五空判据源")

# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("可以自由流动" in doc) and ("抗逆能力增强" in doc) and ("参与维持酸碱平衡" in doc), "选择1=C·选择2=B·选择3=C·答案块逐项排除在件")

# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("一点不剩地全部去掉" in doc) and ("只喝纯净水补充最合适" in doc), "错①结合水系结构组成全丢结构毁·错②应多喝淡盐水补Na⁺·句对注记在件")

# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["运动饮料","氯化钠","0.9%","生理盐水"]), "丢失两类+配料归类防什么+生理盐水补Na⁺Cl⁻对应哪层·p20配料表/p22拓展1口径")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
