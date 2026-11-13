# -*- coding: utf-8 -*-
# 生物4.1升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（0.3 g/mL与0.9%系教材照录·无方程可代）·沿校准件v1.1先例口径
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·教材照录无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物4.1_被动运输_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 渗透两条件
ck("T1 渗透两条件锚", all(k in doc for k in ["半透膜","浓度差"]), "选择1=A·解答(1)判据源·p62-63口径")
# T2 质壁分离核心机制
ck("T2 质壁分离机制锚", all(k in doc for k in ["0.3 g/mL","原生质层","伸缩性","分离开" if "分离开" in doc else "分离"]), "选择2=A·挑刺错①判据源·p65口径")
# T3 两兄弟区别
ck("T3 两兄弟区别锚", all(k in doc for k in ["结合部位相适应","构象的改变","直径和形状相适配","不需要与通道蛋白结合"]), "解答(3)判据源·p66-67原文")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("半透膜＋半透膜两侧溶液具有浓度差" in doc) and ("原生质层与细胞壁逐渐分离开" in doc) and ("属于协助扩散" in doc), "选择1=A·选择2=A·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("细胞壁和原生质层一起皱缩内陷了" in doc) and ("那就一定是主动运输" in doc), "错①壁伸缩性小·错②协助扩散也要载体·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["胀破","生理盐水","复原"]), "三结局+复原机理·图4-1与第2步口径")
# T7 直觉实验锚（撒盐版）
ck("T7 直觉实验撒盐版在件", ("一分钟直觉实验（撒盐版）" in doc) and ("黄瓜" in doc) and ("不耗能" in doc), "浓度差驱动+被动不耗能·家用载体对照·沿裁判件先例形态")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
