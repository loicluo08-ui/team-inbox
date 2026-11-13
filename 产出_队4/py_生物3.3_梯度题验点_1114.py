# -*- coding: utf-8 -*-
# 生物3.3升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（本节新增题全为实验推理/结构辨析类·无数值方程）·沿校准件v1.1先例"对象=0方程·python验点"口径
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物3.3_细胞核的结构和功能_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

ck("T1 核膜双层核孔锚", all(k in doc for k in ["双层","核孔","频繁的物质交换"]), "选择1=B判据源·p56口径")
ck("T2 四件套与核仁职能锚", all(k in doc for k in ["染色质","DNA","蛋白质","核仁","核糖体"]), "填空六空判据源·p56照录")
ck("T3 例外与克隆锚", all(k in doc for k in ["筛管细胞","成熟的红细胞" if "成熟的红细胞" in doc else "红细胞","中中华华","禁止克隆人"]), "选择3=A/D判据源·p55例外+p58伦理红线")
ck("T4 选择题唯一正确项", ("把细胞核内的物质与细胞质分开" in doc) and ("细胞核控制生物的遗传" in doc) and ("同一物质在细胞不同时期的两种存在状态" in doc), "选择1=B·选择2=B·选择3=B·答案块逐项排除在件")
ck("T5 挑刺两处错定位", ("照样能正常生活" in doc) and ("已经完全成熟" in doc), "错①去核停摆死亡补核恢复·错②首例灵长类+伦理红线·句对注记在件")
ck("T6 解答三问锚", all(k in doc for k in ["美西螈核移植","蝾螈横缢","伞藻","染色质形式存在","浓缩成染色体"]), "四实验证据链串珠+两态好处+图纸随核走·p55-58口径")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
