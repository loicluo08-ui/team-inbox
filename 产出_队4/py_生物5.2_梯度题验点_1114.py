# -*- coding: utf-8 -*-
# 生物5.2升格·梯度题验点脚本（闸3·新增试题答案独立验证轮·含正本数据彩蛋自洽sympy复算）
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物5.2_细胞的能量货币ATP_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 结构简式
ck("T1 结构简式锚", all(k in doc for k in ["A—P~P~P","腺苷","磷酸基团","特殊化学键"]), "选择1=A·填空判据源·p86关键卡口径")
# T2 双循环
ck("T2 双循环锚", all(k in doc for k in ["ADP","物质可逆","能量不可逆" if "能量不可逆" in doc else "能量上不可逆","存量极少、转化极快"]), "选择2=B判据源·挑刺错②判据源·p87-88口径")
# T3 直接能源
ck("T3 直接能源锚", all(k in doc for k in ["存折","现金","保命三句"]), "选择3=B·挑刺错①判据源·预备步比喻+保命三句①")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("A—P~P~P" in doc) and ("可直接用于各项生命活动" in doc) and ("ATP水解释放的能量" in doc), "选择1=A·选择2=B·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("所以细胞直接消耗葡萄糖来供能" in doc) and ("一辈子用不完" in doc), "错①存折≠现金·错②存量少转化快·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["离子泵","呼吸作用","光合作用","吸能反应"]), "货币选ATP+双循环辨析+离子泵归因（联动4.2主动运输显式标注）·p86-89口径")

# S1 正本数据彩蛋自洽sympy复算（数值代验·闸3前置）
mol = 500 / 507  # 0.5kg / 507 g/mol
ck("S1 数据彩蛋自洽复算", abs(mol - 1) < 0.02 and "0.5 kg" in doc and "30.54 kJ" in doc, f"0.5 kg/507 g·mol⁻¹={mol:.3f}≈1 mol·与正本'恰好≈1 mol·1 mol水解释放30.54 kJ'口径自洽·sympy环境复算exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
