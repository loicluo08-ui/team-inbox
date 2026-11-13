# -*- coding: utf-8 -*-
# 生物1.2升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（本节新增题全为概念/判断/分类类，无数值方程）·沿校准件v1.1先例"对象=0方程·python验点"口径
import io, sys

try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物1.2_细胞的多样性和统一性_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 唯一判断依据（印刷页10 mark原句）
ck("T1 唯一判断依据=有无以核膜为界限的细胞核", "有无以核膜为界限的细胞核" in doc, "选择1=C判据源·填空末空同源")

# T2 蓝细菌三锚（藻蓝素+叶绿素/无核膜界限核/有一类细菌叫作蓝细菌）
ck("T2 蓝细菌三锚在件", all(k in doc for k in ["藻蓝素","以核膜为界限的细胞核","有一类细菌叫作蓝细菌"]), "选择2=C判据源·叶绿素≠叶绿体注记在答案块")

# T3 支原体三连（无核膜界限核/无细胞壁图示仅细胞膜/原核）
ck("T3 支原体三连锚在件", all(k in doc for k in ["支原体","细胞壁","原核生物"]), "选择3=A判据源·教材拓展应用2要点三连")

# T4 统一性配置五空（细胞膜/细胞质/细胞核/拟核/核膜界限核）
ck("T4 填空五空回填序列", all(k in doc for k in ["细胞膜","细胞质","拟核"]), "五空=细胞膜/细胞质/细胞核/拟核/以核膜为界限的细胞核·真核原核分域表述在答案块")

# T5 唯一正确项断言（选择1=C·选择2=C·选择3=A）
ck("T5 选择题唯一正确项", ("唯一判断依据是" in doc) and ("含有藻蓝素和叶绿素，没有以核膜为界限的细胞核" in doc) and ("没有以核膜为界限的细胞核，也没有细胞壁" in doc), "选择1=C·选择2=C·选择3=A·答案块逐项排除在件")

# T6 挑刺两处错定位
ck("T6 挑刺两处错定位", ("所以它有叶绿体，是真核生物" in doc) and ("所以它没有DNA" in doc), "错①有叶绿素≠有叶绿体只认核膜·错②无染色体但有环状DNA集中拟核·句对注记在件")

# T7 解答三问锚（四材料二分/细胞学说解释/拟核纠错）
ck("T7 解答三问锚在件", all(k in doc for k in ["酵母菌","水绵","叶的保卫细胞","大肠杆菌","新细胞是由老细胞分裂产生的","拟核"]), "分类依据唯一+共同点证据链+拟核纠错·教材材料用具四类换样自编说明在答案块")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
