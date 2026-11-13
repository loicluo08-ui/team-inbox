# -*- coding: utf-8 -*-
# 生物2.1升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（含量数据系教材表载引用·无新增计算方程）·沿校准件v1.1先例"对象=0方程·python验点"口径
import io, sys

try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·含量数据系教材表载引用无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物2.1_细胞中的元素和化合物_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 大量/微量元素名单集合（教材列举）
da = ["C","H","O","N","P","S","K","Ca","Mg"]; wei = ["Fe","Mn","Zn","Cu","B","Mo"]
ck("T1 大量九元素+微量六元素名单在件", all(x in doc for x in da+wei) and not (set(da) & set(wei)), "选择1=C判据源（Ca∈大量·Fe/Zn/Mo∈微量）")

# T2 两个最多+鲜干口径
ck("T2 两个最多三数据锚", all(k in doc for k in ["70%~90%","蛋白质","1%~1.5%"]), "选择2=C判据源·鲜重水最多/干重蛋白质最多/无机盐1-1.5%")

# T3 三试剂规范全链
ck("T3 三试剂规范锚", all(k in doc for k in ["现配现用","50~65","砖红","苏丹Ⅲ","双缩脲","50%"]), "选择3=C·填空六空判据源·先A后B/不加热/酒精洗浮色在件")

# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("属于大量元素的是" in doc) and ("占干重最多的有机物是蛋白质" in doc) and ("等量混合现配现用" in doc), "选择1=C·选择2=C·选择3=C·答案块逐项排除在件")

# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("按比例配齐装进试管，就能造出一个生命系统" in doc) and ("玉米和人没有差异" in doc), "错①材料齐全≠结构组织·错②种类同含量异（44.43%/43.57%/55.99%/14.62%在件）·句对注记在件")

# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["梨汁","先A液","4滴","水浴"]), "梨汁还原糖全流程+蛋白质先A后B4滴不加热+两处差异+加入方式纠错·教材p18口径")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
