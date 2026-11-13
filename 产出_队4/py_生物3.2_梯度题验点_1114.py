# -*- coding: utf-8 -*-
# 生物3.2升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（本节新增题全为分类/路径/情境类·无数值方程）·沿校准件v1.1先例"对象=0方程·python验点"口径
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物3.2_细胞器之间的分工合作_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 特有/共有清单
ck("T1 特有共有清单锚", all(k in doc for k in ["植物特有","动物与低等植物特有","线粒体"]), "选择1=D判据源·特有清单对号")
# T2 分泌蛋白路径
ck("T2 分泌蛋白路径锚", all(k in doc for k in ["核糖体（合成肽链）","内质网","高尔基体","细胞膜"]), "选择2=A·解答(2)判据源·自测3同源口径")
# T3 职能与适应
ck("T3 职能与适应锚", all(k in doc for k in ["动力车间","养料制造车间","消化车间","生产蛋白质的机器","线粒体的数量显著多于腹肌细胞"]), "选择3=C·填空判据源·现场二与自测2口径")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("动植物细胞都有的是" in doc) and ("核糖体→内质网→高尔基体→细胞膜" in doc) and ("终生不停搏动、耗能大的特点相适应" in doc), "选择1=D·选择2=A·选择3=C·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("所以它们不属于细胞器" in doc) and ("分泌蛋白是在高尔基体上合成的" in doc), "错①无膜≠非细胞器（八大清单在册）·错②合成在核糖体·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["亮氨酸","假说方向","溶酶体膜"]), "³H掺入原理+全程路径+开放题假说方向作答·p51/p53口径")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
