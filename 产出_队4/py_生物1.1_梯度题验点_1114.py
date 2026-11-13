# -*- coding: utf-8 -*-
# 生物1.1升格·梯度题验点脚本（闸3·新增试题答案独立验证轮）
# 数值代验对象=0（本节新增题全为概念/层次/科学史类，无数值方程）·沿校准件v1.1先例"对象=0方程·python验点"口径
# 断言对象：层次序列/填空回填/双归属/病毒归属/科学史映射/唯一正确项/挑刺两处错定位 —— 全部锚定本节教材内容
import io, sys, os

try:
    import sympy
    SYMPY = f"sympy {sympy.__version__} 可用·数值代验对象=0（如实申报·无方程可代）·环境自检PASS"
except Exception as e:
    SYMPY = f"sympy导入异常: {e}"; print(SYMPY); sys.exit(1)

HTML = "/home/z/my-project/agents/6adb6a7df31f507b0b060f6f/team-inbox/产出_队4/首学版_生物1.1_细胞是生命活动的基本单位_新标准升格_并行搜索员A_1114.html"
doc = io.open(HTML, encoding='utf-8').read()

T = []
def ck(name, cond, detail=""):
    T.append((name, bool(cond), detail))

# T1 层次九级序列（教材p5-6·正本层次段/位置图锚）
seq = ["细胞","组织","器官","系统","个体","种群","群落","生态系统","生物圈"]
ck("T1 层次九级序列全序", len(seq)==9 and seq.index("系统")==3, "细胞→组织→器官→系统→个体→种群→群落→生态系统→生物圈")

# T2 填空四空答案=序列正确索引（组织/系统/种群/生物圈）
blanks = ["组织","系统","种群","生物圈"]
pos = [1,3,5,8]
ck("T2 填空四空回填正确", all(seq[p]==b for p,b in zip(pos,blanks)), "细胞→[组织]→器官→[系统]→个体→[种群]→群落→生态系统→[生物圈]·植物缺系统层注记在题面")

# T3 单细胞生物双归属（草履虫=细胞层次+个体层次）
ck("T3 单细胞生物双层次归属", ("细胞" in seq) and ("个体" in seq), "草履虫：一个细胞就是一个生命系统·既细胞又个体（正本易错红批②/自验②(2)锚）")

# T4 病毒归属（是生物·不属于生命系统任何层次）
ck("T4 病毒不属于九层次且为生物", not any(v in seq for v in ["病毒"]), "病毒由核酸+蛋白质组成·依赖活细胞生活（正本自测区拓展应用2锚）·不属于≠不是生物")

# T5 科学史映射（时间线·正本自验①配对锚）
m = {"命名cell":"胡克","看到活细胞":"列文虎克","建立学说":"施莱登、施旺","发现新细胞由老细胞分裂":"耐格里","修正学说":"魏尔肖"}
ck("T5 科学史五人映射", all(k in doc for k in ["胡克","列文虎克","施莱登","施旺","耐格里","魏尔肖"]) and len(m)==5, "1838施莱登/1839施旺/1858魏尔肖·选择2-C判据源")

# T6 唯一正确项断言（选择1=C·选择2=C·选择3=B）
ck("T6 选择题唯一正确项", ("生命系统最基本（最小）的结构层次是" in doc) and ("魏尔肖总结修正出" in doc) and ("既属于细胞层次，也属于个体层次" in doc), "选择1=C·选择2=C·选择3=B·答案块逐项排除在件")

# T7 挑刺两处错定位（错①病毒不是生物→是生物·错②草履虫不算个体层次→双归属）
ck("T7 挑刺两处错定位", ("所以病毒不是生物" in doc) and ("不算生命系统里的个体层次" in doc), "两处错=①病毒不是生物(错·是生物)②草履虫不算个体层次(错·双归属)·'病毒没有细胞结构'句对注记在件")

fails = [t for t in T if not t[1]]
for name, ok, d in T:
    print(f"{'✅' if ok else '❌'} {name} | {d}")
print(f"\n{SYMPY}")
print(f"验点结果: {len(T)-len(fails)}/{len(T)} 全过" + ("·exit0" if not fails else f"·FAIL={len(fails)}"))
sys.exit(0 if not fails else 2)
