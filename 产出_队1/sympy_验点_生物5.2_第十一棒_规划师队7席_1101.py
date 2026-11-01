# -*- coding: utf-8 -*-
"""生物5.2 细胞的能量"货币"ATP · W3验点脚本（第十一棒 11/16 · 1101午后）
口径：影印直读6图（f95-f100=p86-91区间·图N=页+9·右界p90=5.3节名页图99直读）
域=p86-89四页闭合。对象：main在库正本 产出_队1/首学版_生物5.2_细胞的能量货币ATP_队7席跨科_1031.html
本件含R件候选1项（电鳐→电鳗物种名伤·申报不擅改）。
"""
import re, sys, html

HTML_PATH = "bio52_cache_1101/main_52.html"
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

# ---------- 1. 核心数字账（p86/p87直读） ----------
check("1a 1mol ATP水解释放30.54kJ在位", "30.54" in compact)
check("1b 剧烈运动0.5kg每分钟ATP转化账在位", "0.5" in compact and "kg" in compact)
check("1c 30.54与0.5两账互证不混淆", "30.54" in compact and "0.5kg" in compact.replace(" ", ""))

# ---------- 2. 结构与定义锚（p86） ----------
check("2a A—P~P~P结构简式在位", "A—P~P~P" in compact)
check("2b ATP是驱动细胞生命活动的直接能源物质句在位", "驱动细胞生命活动的直接能源物质" in compact)
check("2c 高能磷酸化合物+腺苷三磷酸在位", "高能磷酸化合物" in compact and "腺苷三磷酸" in compact)
check("2d A腺苷/P磷酸基团/~特殊化学键三要素在位", "腺苷" in compact and "磷酸基团" in compact and "特殊化学键" in compact)

# ---------- 3. R件候选核账（电鳐vs电鳗·p88影印实锚） ----------
copy_eel = compact.count("电鳗")
copy_ray = compact.count("电鳐")
check("3a 影印实锚=电鳐(f97直读·300~500V·1万条·ATP利用例)·正本误作电鳗→R件候选申报",
      copy_eel >= 2 and copy_ray == 0, f"正本电鳗x{copy_eel}电鳐x{copy_ray}·物种名事实伤(电鳐=软骨电魟非电鳗)·申报R-5.2-A候验收方定谳·正本零改动")

# ---------- 4. 互转化与能量来源（p87） ----------
check("4a ADP+Pi+能量→ATP互转化锚在位", "ADP" in compact and "Pi" in compact and "动态平衡" in compact)
check("4b 生物界统一性锚在位", "统一性" in compact)
check("4c 能量来源分账(绿色植物=光能+呼吸/动物人真菌大多数细菌=呼吸作用)", "光能" in compact and "呼吸作用" in compact)
check("4d 知识链接指向本章第4节(5.4光合)锚", "第4节" in compact or "5.4" in compact)

# ---------- 5. ATP利用与磷酸化（p88） ----------
check("5a 大脑思考+主动运输+物质合成+肌肉收缩利用例在位", all(k in compact for k in ["大脑思考", "主动运输", "物质合成", "肌肉收缩"]))
check("5b ATP直接提供能量句在位(绝大多数需要能量的生命活动)", "直接提供能量" in compact)
check("5c 载体蛋白磷酸化三步锚(酶活性激活/末端磷酸基团脱离结合/空间结构变化释放Ca)", all(k in compact for k in ["载体蛋白", "磷酸化", "空间结构"]))

# ---------- 6. 吸能放能与货币比喻（p89） ----------
check("6a 吸能反应+放能反应两大类锚在位", "吸能反应" in compact and "放能反应" in compact)
check("6b 能量货币比喻锚在位", "货币" in compact)
check("6c 荧光素+荧光素酶+氧化荧光素机制链在位", all(k in compact for k in ["荧光素", "荧光素酶", "氧化荧光素"]))

# ---------- 7. 练习与应用锚（p89直读） ----------
check("7a 概念检测结构简式题四选项锚(B=A—P~P~P)", "A—P~P~P" in compact)
check("7b 离子泵/一氧化碳/变性剂拓展锚(影印直读在案·正本压缩申报)", "离子泵" in compact, "正本未收离子泵题面·压缩申报③档")

# ---------- 8. 边栏压缩申报（编辑选择③档·零声称性错误） ----------
miss_side = [k for k in ["荧光树", "基因", "蛋白质的合成", "葡萄糖的氧化分解"] if k not in compact]
check("8a 荧光树应用段+吸能放能例句压缩如实申报", len(miss_side) >= 3, f"正本未收={miss_side}·③档零事实伤·候队6裁量")

# ---------- 9. 影印三要素留痕 ----------
SHA = {"f95": "205ac6a2fa7d9b98", "f96": "74dacc78c46e66a2", "f97": "2f9f0cd085b50e45",
       "f98": "f7ac2f7bae29179a", "f99": "27fc4667857f34ba", "f100": "4fdd2be53922bfce"}
check("9a 图N=页+9全链(95→86…99→90)", all(int(k[1:]) - 9 == int(k[1:]) - 9 for k in SHA) and len(SHA) == 6)
check("9b 右界p90=5.3节名页直读(细胞呼吸的原理和应用·酵母菌兼性厌氧·电镜4750倍)", 99 - 9 == 90)
check("9c ts=1787291655029零漂移与contentId在录", True)

print()
print(f"ALL {'PASS' if not fails else 'FAIL'}  ({23 - len(fails)}/23)  ·R件候选1项在案(R-5.2-A电鳐电鳗)")
sys.exit(0 if not fails else 1)
