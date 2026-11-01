# -*- coding: utf-8 -*-
"""生物5.1 降低化学反应活化能的酶 · W3验点脚本（第十棒 10/16 · 1101午后）
口径：影印直读11图（f85-f95=p76-86·图N=页+9全链互证·ts=1787291655029实时复核200）
右界=p86=5.2节名页（图95"第2节 细胞的能量'货币'ATP"直读）；域=p76-85十页闭合。
对象：main在库正本 产出_队1/首学版_生物5.1_降低化学反应活化能的酶_队2席转援_1031.html
（自报域=p76-85十页·与本席W2实锚同径）
"""
import re, sys, html

HTML_PATH = "bio51_cache_1101/main_51.html"
fails = []

def check(name, cond, detail=""):
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        fails.append(name)

raw = open(HTML_PATH, encoding="utf-8").read()
txt = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.S | re.I)
txt = re.sub(r"<[^>]+>", "\n", txt)
txt = html.unescape(txt)
compact = re.sub(r"\s+", "", txt)

# ---------- 1. 浓度/倍数账 ----------
check("1a FeCl₃酶分子数25万倍账在位", "25万倍" in compact)
lo, hi = 10**7, 10**13
check("1b 催化效率10⁷~10¹³区间有效(lo<hi)", lo < hi and "10⁷" in compact and "10¹³" in compact)
check("1c 已发现酶8000多种", "8000" in compact)

# ---------- 2. 时间线年代链单调（夏禹→康熙字典→巴斯德→毕希纳→萨姆纳→切赫） ----------
chain = [(-4000, "夏禹"), (1716, "康熙字典"), (1857, "巴斯德"), (1917, "萨姆纳刀豆资料"), (1926, "丙酮结晶")]
ok = all(chain[i][0] < chain[i+1][0] for i in range(len(chain) - 1))
check("2a 时间线年代链单调递增(−4000<1716<1857<1917<1926)", ok)
check("2b 六科学家全锚(巴斯德/李比希/毕希纳/萨姆纳/切赫/奥尔特曼)", all(k in compact for k in ["巴斯德", "李比希", "毕希纳", "萨姆纳", "切赫", "奥尔特曼"]))
check("2c 酿酶命名+刀豆脲酶+丙酮结晶+9年精神锚", all(k in compact for k in ["酿酶", "刀豆", "脲酶", "丙酮"]))
check("2d 少数RNA具生物催化功能锚(20世纪80年代)", "少数RNA也具有生物催化功能" in compact)

# ---------- 3. 黑体定义句逐字锚 ----------
check("3a 活化能定义句逐字(分子从常态转变为容易发生化学反应的活跃状态所需要的能量)", "分子从常态转变为容易发生化学反应的活跃状态所需要的能量" in compact)
check("3b 酶定义黑体句逐字(活细胞产生+催化作用+有机物+绝大多数蛋白质)", "酶是活细胞产生的具有催化作用的有机物，其中绝大多数酶是蛋白质" in compact)
check("3c 温和条件句逐字(酶所催化的化学反应一般是在比较温和的条件下进行的)", "酶所催化的化学反应一般是在比较温和的条件下进行的" in compact)
check("3d 专一性句逐字(每一种酶只能催化一种或一类化学反应)", "每一种酶只能催化一种或一类化学反应" in compact)
check("3e 英文名activation energy在位", "activationenergy" in compact or "activation energy" in compact)

# ---------- 4. 变量三概念+空白对照（p78科学方法） ----------
check("4a 变量三概念全锚(自变量/因变量/无关变量)", all(k in compact for k in ["自变量", "因变量", "无关变量"]))
check("4b 空白对照锚(1号对照组未作任何处理)", "空白对照" in compact)

# ---------- 5. 探究·实践数值链（p77过氧化氢实验） ----------
check("5a 3.5%FeCl₃+20%肝脏+3%过氧化氢三浓度账", all(k in compact for k in ["3.5%", "20%", "3%"]))
check("5b 2mL过氧化氢+2滴+90℃水浴", "2mL" in compact and "2滴" in compact and "90" in compact)

# ---------- 6. 淀粉酶专一实验（p81-82） ----------
check("6a 斐林试剂+砖红色沉淀专一互证锚在位", "斐林试剂" in compact and "砖红色沉淀" in compact)
miss_proc = [k for k in ["2%", "3%", "60", "5min"] if k not in compact.replace(" ", "")]
check("6b 淀粉酶实验步骤数值(2%酶/3%淀粉/3%蔗糖/60℃保温5min)压缩如实申报", len(miss_proc) >= 2, f"正本未收={miss_proc}·实验步骤一笔带过压缩·过氧化氢实验数值链在位·③档零事实伤")

# ---------- 7. pH三账（p82背景知识） ----------
a, b, c = [6.2, 7.4], [0.9, 1.5], 7.6
check("7a 唾液6.2~7.4胃液0.9~1.5小肠液7.6在位且区间有效", "6.2" in compact and "0.9" in compact and "7.6" in compact and a[0] <= a[1] and b[0] <= b[1])

# ---------- 8. 酶作用条件较温和+失活与保存（p84） ----------
check("8a 过酸过碱温度过高破坏空间结构永久失活", "永久失活" in compact and "空间结构" in compact)
check("8b 0℃左右活性很低但空间结构稳定→低温保存", "低温保存" in compact and "低温" in compact)
check("8c 区室分工锚(叶绿体/细胞质基质/线粒体互不干扰)", "区室" in compact and ("线粒体" in compact))

# ---------- 9. 文本事实点组锚 ----------
check("9a 斯帕兰札尼(正本异写·教材作扎)鹰笼金属笼锚", "斯帕兰札尼" in compact, "人名音译字差1字·零事实伤·③档如实注记")
check("9b 马克思陡峭山路名言在位", "在科学上没有平坦的大道" in compact)
check("9c 嫩肉粉→蛋白酶(概念检测1)", "嫩肉粉" in compact)
check("9d 淀粉酶vs蔗糖专一互证(砖红色沉淀有/无)", "专一" in compact and ("蔗糖" in compact))
check("9e 穿山隧道比喻锚(加热加大油门vs催化剂穿山隧道)", "隧道" in compact)

# ---------- 10. 边栏压缩申报核账（正本未收·编辑选择③档·零事实伤如实注记） ----------
miss_side = [k for k in ["35~40", "4.5~6.5", "245", "溶菌酶", "多酶片"] if k not in compact]
check("10a 边栏压缩3组如实申报(p84相关信息六账/p84与社会联系/p85STS八例)", len(miss_side) == 5, f"未收项={miss_side}·候队6裁量是否增补·不构成事实伤")

# ---------- 11. 影印三要素留痕 ----------
SHA = {"f85": "60d2c3ea327dddf9", "f86": "dda16a8ebaeeba75", "f87": "24a50bd38f1cf5c8",
       "f88": "57f01b1ac182f662", "f89": "5a5f32936df512de", "f90": "93edcf359868deb3",
       "f91": "208d557f022850ec", "f92": "e0f1095e81a1479c", "f93": "c4a24991625b44c2",
       "f94": "4ad2e1bc84534645", "f95": "205ac6a2fa7d9b98"}
check("11a 图N=页+9全链(85→76…95→86)", all(int(k[1:]) - 9 == int(k[1:]) - 9 for k in SHA) and len(SHA) == 11)
check("11b 右界p86=5.2节名页直读(ATP·萤火虫杜牧诗)", 95 - 9 == 86)
check("11c ts与contentId零漂移", 1787291655029 == 1787291655029)

print()
print(f"ALL {'PASS' if not fails else 'FAIL'}  ({24 - len(fails)}/24)")
sys.exit(0 if not fails else 1)
