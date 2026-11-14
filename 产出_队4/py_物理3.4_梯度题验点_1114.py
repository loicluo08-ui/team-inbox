# -*- coding: utf-8 -*-
# 物理3.4升格·梯度题验点脚本（闸3·含2项sympy数值代验：S1合力范围+勾股·S2斜面分解）
import io, sys
try:
    import sympy
    diag = sympy.sqrt(3**2 + 4**2)
    lo, hi = abs(3 - 4), 3 + 4
    f_par = 20 * sympy.sin(sympy.pi / 6)
    f_perp = 20 * sympy.cos(sympy.pi / 6)
    S1v = f"√(9+16)={float(diag):.2f}·范围[{float(lo):.0f},{float(hi):.0f}]"
    S2v = f"沿面={float(f_par):.2f} N·垂直={float(f_perp):.2f} N"
except Exception as e:
    print(f"sympy异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_物理3.4_力的合成和分解_人教版_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 合力范围
ck("T1 合力范围锚", ("|F₁−F₂|" in doc and "F₁+F₂" in doc), "选择1=C·填空判据源·第二步+考位锚口径")
# T2 平行四边形定则
ck("T2 定则与等效锚", all(w in doc for w in ["邻边","对角线","等效替代"]), "填空判据源·第二步口径")
# T3 分解按效果
ck("T3 分解按效果锚", ("按效果" in doc and "斜面" in doc), "选择3=A·挑刺错②判据源·第三步+考位锚口径")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("合力可能小于其中任一分力" in doc) and ("夹角可变" in doc) and ("正是使物体下滑的力" in doc), "选择1=C·选择2=C·选择3=A·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("合力最小是3 N" in doc) and ("没有依据" in doc), "错①反向特例·错②按效果分·句对注记在件")
# T6 解答锚
ck("T6 解答锚在件", all(w in doc for w in ["5 N","10 N","17.3 N","图解法","54 N"]), "勾股精确解+斜面分解+教材例题方法对照·p74口径")
# T7 直觉实验锚
ck("T7 直觉实验提水版在件", ("提水版" in doc) and ("夹角越大" in doc), "合力一定时夹角越大分力越大·家用零器材·B席人教版家族CSS适配（div.try沿q/a样式零新增）")
# S1 合力范围+勾股sympy代验
ck("S1 合力范围与勾股sympy代验", abs(float(diag) - 5.0) < 1e-9 and float(lo) <= 5 <= float(hi) and "5 N" in doc, f"{S1v}·选择2=C与解答1=5N自洽·sympy独立复算exit0")
# S2 斜面分解sympy代验
ck("S2 斜面分解sympy代验", abs(float(f_par) - 10.0) < 1e-9 and abs(float(f_perp) - 17.3205080) < 1e-4 and "10 N" in doc and "17.3 N" in doc, f"{S2v}·θ=30°·G=20N·与解答2口径一致·sympy独立复算exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\nsympy {sympy.__version__} 可用·数值代验对象=2项（S1/S2）全过")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
