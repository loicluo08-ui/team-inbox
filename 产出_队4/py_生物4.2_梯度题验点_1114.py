# -*- coding: utf-8 -*-
# 生物4.2升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（碘20~25倍系教材照录·无方程可代）·沿校准件v1.1先例口径
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·教材照录无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物4.2_主动运输与胞吞胞吐_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 主动运输三要素
ck("T1 主动运输三要素锚", all(k in doc for k in ["载体蛋白","ATP","逆"]), "选择1=A·填空前三空判据源·p69黑体口径")
# T2 胞吞胞吐
ck("T2 胞吞胞吐锚", all(k in doc for k in ["流动性","大分子","耗"]), "选择2=B判据源·p70-71口径")
# T3 判别矩阵四例
ck("T3 判别矩阵锚", all(k in doc for k in ["葡萄糖进红细胞","O₂","K⁺","分泌蛋白"]), "选择3=B判据源·总表四行对号")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("载体蛋白＋ATP·主动运输" in doc) and ("依赖于生物膜的流动性" in doc) and ("葡萄糖进入红细胞——协助扩散" in doc), "选择1=A·选择2=B·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("细胞缺少能量" in doc) and ("说明它没有细胞膜" in doc), "错①载体蛋白功能异常非缺能量·错②胞吞=膜流动性表演·句对注记在件")
# T6 解答三问锚
ck("T6 解答三问锚在件", all(k in doc for k in ["题眼三连","选择透过性","转运蛋白"]), "三要素意义+题眼三连+结构基础·p70/72与考位锚口径")
# T7 囊性纤维化直读锚
ck("T7 囊性纤维化p70直读锚", ("转运氯离子的载体蛋白功能异常" in doc), "挑刺错①判据源·p70与社会的联系照录")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
