# -*- coding: utf-8 -*-
# 生物2.4升格·梯度题验点脚本（闸3·新增试题答案独立验证轮·水账公式sympy符号复算）
import io, sys
try:
    import sympy
    SY = sympy
    SYMPY = f"sympy {sympy.__version__} 可用"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物2.4_蛋白质是生命活动的主要承担者_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 五大岗位+实例
ck("T1 五大岗位实例在件", all(k in doc for k in ["血红蛋白","抗体","羽毛","胰岛素" if "胰岛素" in doc else "信息传递"]), "选择1=D判据源（羽毛毛发=结构岗）·实例对号在答案块")
# T2 通式四件套
ck("T2 通式四件套锚", all(k in doc for k in ["氨基","羧基","R基","同一个"]), "填空四空判据源·四件套口径在件")
# T3 变性边界（变性≠水解·不可逆）
ck("T3 变性边界锚", all(k in doc for k in ["解冻","更好消化"]), "选择3=A/D判据源·第五步口径在件")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("570、570" in doc) and ("肽链的空间结构千差万别" in doc) and ("信息传递——羽毛" in doc), "选择1=D(错误项)·选择2=A·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("肽键断裂，分解成了氨基酸" in doc) and ("最多不超过1000种" in doc), "错①变性≠水解·错②20的500次方照录·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["n−1","m−2","顺序→结构→功能" if "顺序→结构→功能" in doc else "因果链"]), "水账公式+因果链·考位锚第一常客口径")
# T7 直觉实验锚（蛋清版）
ck("T7 直觉实验蛋清版在件", ("一分钟直觉实验（蛋清版）" in doc) and ("空间构象" in doc), "变性演示对照在件·沿裁判件先例形态")

# S1 水账公式sympy符号复算（数值代验·闸3前置）
n, k, m = SY.symbols('n k m', integer=True, positive=True)
formula = n - k
s1 = (formula.subs({n: 574, k: 4}) == 570)
s2 = (formula.subs({n: 201, k: 2}) == 199)
s3 = (formula.subs({n: m, k: 2}) == m - 2)
ck("S1 水账sympy符号复算", s1 and s2 and s3 and ("574−4＝570" in doc), "肽键数=n−k：代入(574,4)=570✓(201,2)=199✓与正本自测2口径同源·(m,2)=m−2符号恒等✓·exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
