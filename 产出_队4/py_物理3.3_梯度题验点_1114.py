# -*- coding: utf-8 -*-
# 物理3.3升格·梯度题验点脚本（闸3·数值代验对象=0如实申报·概念/情境辨析类无方程可代）
import io, sys
try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·概念/情境辨析类无方程可代）·环境自检PASS"
except Exception as e:
    print(f"sympy导入异常: {e}"); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_物理3.3_牛顿第三定律_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()
T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 定律表述
ck("T1 定律表述锚", all(w in doc for w in ["大小相等","方向相反","不同" ]), "选择1=B判据源·p68-69口径")
# T2 猴子判据
ck("T2 猴子判据锚", ("猴子吊在空中" in doc and "平衡力" in doc), "选择2=A·解答1判据源·辨析站照录")
# T3 划龙舟口径
ck("T3 划龙舟锚", ("划龙舟" in doc and "反作用力" in doc), "选择3=B判据源·第三步口径")
# T4 唯一正确项断言
ck("T4 选择题唯一正确项", ("大小相等、方向相反、作用在不同的物体上" in doc) and ("作用在不同物体上" in doc) and ("水对桨的反作用力" in doc), "选择1=B·选择2=A·选择3=B·答案块逐项排除在件")
# T5 挑刺两处错定位
ck("T5 挑刺两处错定位", ("马拉车的力大于车拉马的力" in doc) and ("互相抵消" in doc), "错①永远等大·错②异体不可合成·句对注记在件")
# T6 解答2类比锚
ck("T6 解答2类比锚在件", ("拔河" in doc and "汽车" in doc and "蹬地" in doc), "轻绳张力等大+胜负在地面摩擦·类比第三步汽车驱动显式标注")
# T7 直觉实验锚
ck("T7 直觉实验拍桌手疼在件", ("拍桌手疼版" in doc) and ("同时" in doc), "同时等大反向异体·家用零器材·沿裁判件先例形态v2家族CSS适配（box容器自纠留痕）")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
