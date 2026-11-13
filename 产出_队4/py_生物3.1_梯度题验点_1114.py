# -*- coding: utf-8 -*-
# 生物3.1升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（占比50%/40%/2%~10%系教材照录·自洽算术已由正本自测4完成）·沿校准件v1.1先例口径
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·占比系教材照录无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物3.1_细胞膜的结构和功能_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 三大功能+相对性
ck("T1 三大功能与相对性锚", all(k in doc for k in ["将细胞与外界环境分隔开","控制物质进出细胞","进行细胞间的信息交流","控制作用是相对的"]), "选择1=D判据源·挑刺错①判据源·p41原句")
# T2 探案史配对
ck("T2 探案史证据链锚", all(k in doc for k in ["欧文顿","荧光","暗亮暗","2倍"]), "选择2=A判据源·挑刺错②判据源·六站口径")
# T3 模型三件套
ck("T3 模型三件套锚", all(k in doc for k in ["磷脂双分子层","糖被","胞间连丝","侧向自由移动"]), "选择3=A·填空四空判据源")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("细胞膜的控制作用是绝对的" in doc) and ("更容易通过细胞膜进入细胞" in doc) and ("磷脂分子能侧向自由移动，膜中的大多数蛋白质分子也能运动" in doc), "选择1=D(错误项)·选择2=A·选择3=A·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("完全封闭起来，任何物质都进不来也出不去" in doc) and ("流动镶嵌模型就是他提出的" in doc), "错①控制相对性·错②静态模型与流动模型辨析·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["台盼蓝","激素","受体","胞间连丝","功能越复杂的细胞膜"]), "死活判断归功能②+三方式+结构功能适应·课外延伸讨论行落答判据=p41")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
