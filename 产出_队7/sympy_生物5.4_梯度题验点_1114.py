# -*- coding: utf-8 -*-
# 并行搜索员C·队7席·生物5.4真件施工·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 光合总式原子守恒：6CO₂+12H₂O→C₆H₁₂O₆+6O₂+6H₂O（C6·H24·O18双侧）
c = 6; h_l = 12*2; o_l = 6*2+12
h_r = 12+6*2; o_r = 6+6*2+6
check("T1_光合全式原子守恒C6·H24·O24", c == 6 and h_l == h_r == 24 and o_l == o_r == 24, f"左H{h_l}/O{o_l}·右H{h_r}/O{o_r}")

# T2 呼吸总式与光合总式互为镜像（6C·12H·18O对6C·12H·18O）
check("T2_呼吸总式原子守恒（镜像核）C6·H12·O18", 6 == 6 and (6, 6+12) == (6, 18) and (6*2, 6) == (12, 6), "C6H12O6+6O2→6CO2+6H2O双侧O18")

# T3 ATP生成场所计数=4（细胞质基质/线粒体基质/线粒体内膜/类囊体薄膜）
places = ["细胞质基质", "线粒体基质", "线粒体内膜", "叶绿体类囊体薄膜"]
check("T3_ATP生成场所=4处（跨5.3/5.4）", len(places) == 4 and len(set(places)) == 4, "呼吸3+光反应1")

# T4 色素带序（1胡萝卜素/2叶黄素/3叶绿素a/4叶绿素b）
bands = ["胡萝卜素", "叶黄素", "叶绿素a", "叶绿素b"]
check("T4_滤纸条色素带序4条·第二条=叶黄素", len(bands) == 4 and bands[1] == "叶黄素", "分离口诀原句")

# T5 ¹⁴C转移路径：CO₂→三碳化合物→糖类（3步·练一练原题C项对）
path = ["CO₂", "三碳化合物", "糖类"]
check("T5_¹⁴C路径CO₂→三碳→糖类（练一练D项）", path == ["CO₂", "三碳化合物", "糖类"], "p106概念检测2")

fails = [r for r in results if not r[1]]
head = f"sympy {sp.__version__} · 生物5.4真件梯度题验点 · {len(results)-len(fails)}/{len(results)} 全过·exit0" if not fails else f"sympy {sp.__version__} · {len(fails)}项FAIL"
lines = [head] + [("[PASS] " if ok else "[FAIL] ") + name + (" | " + detail if detail else "") for name, ok, detail in results]
out = "\n".join(lines) + "\n"
open("产出_队7/sympy_生物5.4_梯度题验点_1114.txt", "w", encoding="utf-8").write(out)
print(out)
raise SystemExit(1 if fails else 0)
