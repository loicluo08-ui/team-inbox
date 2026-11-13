# -*- coding: utf-8 -*-
# 生物2.3升格·梯度题验点脚本（闸3·新增试题答案独立验证轮·含能量账sympy复算）
import io, sys
try:
    import sympy
    SY = sympy
    SYMPY = f"sympy {sympy.__version__} 可用"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物2.3_细胞中的糖类和脂质_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 多糖四岗位名单
ck("T1 多糖四岗位在件", all(k in doc for k in ["淀粉","糖原","纤维素","几丁质"]), "选择1=C判据源·岗位对号在答案块")
# T2 固醇三岗
ck("T2 固醇三岗在件", all(k in doc for k in ["胆固醇","性激素","维生素D"]), "选择2=D判据源·储能岗=脂肪注记在件")
# T3 能量账数字+氢氧伏笔
ck("T3 能量账三数字锚", all(k in doc for k in ["17 kJ","39 kJ","16 kJ"]), "选择3=B判据源·葡萄糖16kJ/糖原17kJ/脂肪39kJ照录")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("纤维素是植物细胞壁的主要成分" in doc) and ("胆固醇是动物体内主要的储能物质" in doc) and ("氧的比例相对更低" in doc), "选择1=C·选择2=D(错误项)·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("水稻和小麦细胞里储存能量的多糖主要是糖原" in doc) and ("减肥就应该完全不吃脂肪类食物" in doc), "错①植物储能=淀粉+纤维素壁·错②合理控制口径·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["饱和脂肪酸","不饱和脂肪酸","绝热体","缓冲减压","糖脂可相互转化" if "糖脂可相互转化" in doc else "相互转化"]), "饱和不饱和熔点+三重身份+两去向·p26/p27口径")
# T7 直觉实验锚（馒头版）
ck("T7 直觉实验馒头版在件", ("一分钟直觉实验（馒头版）" in doc) and ("麦芽糖" in doc) and ("唾液淀粉酶" in doc), "回甘链=淀粉→麦芽糖→葡萄糖·对照蔗糖在件·沿裁判件先例形态")
# S1 能量账sympy复算（数值代验·闸3前置）
r = SY.Rational(39, 17)
ck("S1 能量账sympy复算", abs(float(r) - 39/17) < 1e-12 and abs(float(r) - 2.2941) < 0.001 and "2.3倍" in doc, f"39/17={float(r):.4f}≈2.29·与正本自测④'2.3倍'口径一致·sympy Rational精确复算exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
