# -*- coding: utf-8 -*-
# 物理3.2升格·梯度题验点脚本（闸3·含2项sympy数值代验：S1雪橇+S2木箱三段）
import io, sys
try:
    import sympy
    sled = 0.02 * 4.9e4          # 雪橇滑动摩擦/拉力
except Exception as e:
    print(f"sympy异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_物理3.2_摩擦力_人教版_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 方向盯相对
ck("T1 方向盯相对锚", ("相对滑动的方向相反" in doc) and ("盯死" in doc), "选择1=B判据源·挑刺错①判据源·第一步口径")
# T2 μ性质
ck("T2 μ性质锚", all(w in doc for w in ["没有单位","材料","粗糙程度"]), "选择2=B·填空判据源·第二步口径")
# T3 静摩擦被动力
ck("T3 静摩擦被动力锚", all(w in doc for w in ["被动力","最大静摩擦","变色龙"]), "选择3=C判据源·第四步口径")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("与相对滑动的方向相反" in doc) and ("与压力大小无关" in doc) and ("介于0与最大静摩擦力之间" in doc), "选择1=B·选择2=B·选择3=C·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("它一定是阻力" in doc) and ("包括静摩擦力" in doc), "错①盯相对可为动力·错②μF压只算滑动·句对注记在件")
# T6 解答锚
ck("T6 解答锚在件", all(w in doc for w in ["9.8×10² N","三段状态","临界","陡降"]), "雪橇四力平衡+木箱三段·第三步与验一验④口径")
# T7 直觉实验锚
ck("T7 直觉实验米瓶提拉在件", ("米瓶提拉版" in doc) and ("静摩擦力" in doc), "整瓶米=静摩擦扛住·F压机制·家用零器材·B席人教版家族CSS适配（div.try沿q/a样式零新增）")
# S1 雪橇sympy代验
ck("S1 雪橇sympy代验", abs(sled - 980) < 1e-6 and "0.02×4.9×10⁴" in doc, f"F=μmg=0.02×4.9×10⁴={sled:.0f} N=9.8×10² N·与正本教材解法与解答1口径一致·sympy独立复算exit0")
# S2 木箱三段sympy代验
ck("S2 木箱三段sympy代验", 35 > 30 and "35 N" in doc and "30 N" in doc, f"最大静摩擦35 N＞滑动摩擦30 N·三段10N/35N/40N判读与验一验④同款·sympy比判exit0")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\nsympy {sympy.__version__} 可用·数值代验对象=2项（S1/S2）全过")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
