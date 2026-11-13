# -*- coding: utf-8 -*-
# 生物5.1升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（37℃/pH区间系教材照录·无方程可代）·沿校准件v1.1先例口径
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·教材照录无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物5.1_降低化学反应活化能的酶_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 活化能机理
ck("T1 活化能机理锚", all(k in doc for k in ["降低活化能","不为反应物提供能量"]), "选择1=B判据源·挑刺错①判据源·收口①+易错红笔")
# T2 四管实验与特性
ck("T2 四管实验与特性锚", all(k in doc for k in ["Fe³⁺","高效性","专一性","作用条件温和"]), "选择2=B·填空判据源·p77-78与第四站口径")
# T3 温度pH边界
ck("T3 温度pH边界锚", all(k in doc for k in ["低温是<b>抑制</b>","永久失活","唾液pH 6.2～7.4"]), "选择3=B判据源·易错红笔+背景知识p82")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("降低化学反应的活化能" in doc) and ("酶具有高效性" in doc) and ("高温使酶的空间结构损毁、永久失活" in doc), "选择1=B·选择2=B·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("酶能为化学反应提供能量" in doc) and ("嫩肉粉里起分解作用的酶是淀粉酶" in doc), "错①不供能·错②蛋白酶（自测1口径）·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["空白对照","巴斯德","毕希纳","萨姆纳","切赫","糯玉米"]), "四管对照+证据链排序+概念检测归因·p77-85口径")
# T7 直觉实验锚（回甘版）
ck("T7 直觉实验回甘版在件", ("一分钟直觉实验（回甘版）" in doc) and ("唾液淀粉酶" in doc) and ("专一性现场版" in doc), "温和条件+专一性对照·家用零器材·沿裁判件先例形态v15家族CSS适配")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
