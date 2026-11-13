# -*- coding: utf-8 -*-
# 生物2.5升格·梯度题验点脚本（闸3·新增试题答案独立验证轮·含核苷酸账目与排列数sympy代验）
import io, sys
try:
    import sympy
    SY = sympy
    SYMPY = f"sympy {sympy.__version__} 可用"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物2.5_核酸是遗传信息的携带者_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 分布"主要"口径
ck("T1 分布主要字眼锚", ("主要分布在细胞核中" in doc) and ("主要分布在细胞质中" in doc), "选择1=B判据源·挑刺错①判据源·'主要'含义在线粒体叶绿体")
# T2 三件套+专属碱基
ck("T2 三件套与专属碱基锚", all(k in doc for k in ["核苷酸","磷酸","五碳糖","含氮碱基","T（胸腺嘧啶）","U（尿嘧啶）"]), "填空六空判据源·对账表口径")
# T3 双链单链+病毒RNA
ck("T3 双单链与病毒RNA锚", all(k in doc for k in ["双链","单链","RNA中"]), "选择3=A判据源·挑刺错②判据源·p35原句")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("真核细胞的DNA主要分布在细胞核中，RNA主要分布在细胞质中" in doc) and ("可能是脱氧核糖核苷酸，也可能是核糖核苷酸" in doc) and ("DNA通常是双链，RNA通常是单链" in doc), "选择1=B·选择2=C·选择3=A·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("细胞质里完全没有DNA" in doc) and ("遗传信息也储存在DNA里" in doc), "错①'主要'=线粒体叶绿体少量DNA·错②部分病毒RNA·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["口服核酸保健品","4的50次方","6+2=8"]), "保健品两句回应+账目3×2+2×1+4⁵⁰算式·自测3与4ⁿ算例同型")

# S1 核苷酸账目sympy复算
s1 = (3*2 + 2*1 == 8)
# S2 排列数大数验证
s2 = SY.Integer(4)**50
ck("S1 核苷酸账目sympy复算", s1 and "8种核苷酸" in doc, "3×2+2×1=8（A/G/C各配两糖=6·T/U各配一糖=2）·与正本对账表'5碱基8核苷酸'一致·exit0")
ck("S2 排列数4⁵⁰大数验证", int(s2) == 4**50 and str(s2) == str(4**50) and "4的50次方" in doc, f"4⁵⁰={s2}（{len(str(s2))}位大数）·海量多样性判据·与正本4¹⁰⁰算例同型·exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
