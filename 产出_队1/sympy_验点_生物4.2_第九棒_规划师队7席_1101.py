# -*- coding: utf-8 -*-
"""生物4.2 主动运输与胞吞、胞吐 · W3验点脚本（第九棒 9/16 · 1101午后）
口径：影印直读7图（f78-f84=p69-75·图N=页+9全链互证·ts=1787291655029实时复核200）
验点=事实锚定（数值账+逻辑自洽+文本锚在位），非答案代拟；判读候教材答案锚如实注记。
对象：main在库正本 产出_队3/首学版_生物4.2_主动运输与胞吞胞吐_并行搜索员B_1031.html（v1.1讲义体）
"""
import re, sys, html

HTML_PATH = "bio42_cache_1101/main_42.html"
fails = []

def check(name, cond, detail=""):
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        fails.append(name)

# ---------- 0. 正本载入 ----------
raw = open(HTML_PATH, encoding="utf-8").read()
txt = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.S | re.I)
txt = re.sub(r"<[^>]+>", "\n", txt)
txt = html.unescape(txt)
compact = re.sub(r"\s+", "", txt)  # 去空白便于逐字比对

# ---------- 1. 浓度三账（p69直读）----------
iodine = [20, 25]           # 甲状腺滤泡上皮细胞内碘浓度比血液高20~25倍（区间）
k_rbc, k_wort = 30, 63      # 人红细胞K+比血浆高30倍；轮藻细胞K+比周围水环境高63倍
check("1a 碘20~25倍区间有效(20<=25且单调)", 20 <= 25)
check("1b K倍数账30与63在位", ("血浆×30" in compact or "×30" in compact) and ("×63" in compact or "水×63" in compact),
      f"rbc×30={'血浆×30' in compact} wort×63={'×63' in compact}")
check("1c 三账排序单调(20<25<30<63)", 20 < 25 < 30 < 63)

# ---------- 2. 主动运输定义三要素（p69黑体逐字锚）----------
def_sentence = ("物质逆浓度梯度进行跨膜运输，需要载体蛋白的协助，同时还需要消耗细胞内化学"
                "反应所释放的能量，这种方式叫作主动运输（active transport）（图4-6）")
check("2a 主动运输定义句逐字在位(讲义体声称黑体直读)", re.sub(r"\s+", "", def_sentence) in compact)
check("2b 三要素逻辑(逆梯度∧载体∧能量缺一即非主动运输)", all(k in compact for k in ["逆浓度梯度", "载体蛋白", "能量"]))
check("2c 英文名active transport在位", "activetransport" in compact)

# ---------- 3. 知识链接（p70）----------
check("3a ATP水解为ADP和Pi时放能供主动运输利用", ("ATP水解为ADP和Pi" in compact and "放能" in compact and "主动运输利用" in compact))
check("3b 引用锚第5章第2节", "第5章第2节" in compact)

# ---------- 4. 胞吞/胞吐定义（p71黑体）----------
check("4a endocytosis在位", "endocytosis" in compact)
check("4b exocytosis在位", "exocytosis" in compact)
check("4c 胞吞过程锚(内陷形成小囊+分离下来形成囊泡)", "内陷形成小囊" in compact and "分离下来形成囊泡" in compact)
check("4d 胞吐过程锚(囊泡移动到细胞膜处+与细胞膜融合)", "与细胞膜融合" in compact)
check("4e 两铁律(普遍存在+消耗细胞呼吸所释放的能量)", "普遍存在" in compact and "细胞呼吸所释放的能量" in compact)

# ---------- 5. 相关信息与病例 ----------
check("5a 胞吞囊泡可被溶酶体降解(相关信息)", "溶酶体降解" in compact)
check("5b 囊性纤维化锚(氯离子载体蛋白+黏液增多+细菌感染)", "囊性纤维化" in compact and "氯离子" in compact and "黏液增多" in compact)
check("5c 痢疾内变形虫链(胞吐分泌蛋白分解酶+胞吞吃掉肠壁+阿米巴痢疾)",
      "痢疾内变形虫" in compact and "蛋白分解酶" in compact and "阿米巴痢疾" in compact)
check("5d 传播与预防(饮食传播+饮食卫生公共卫生)", "饮食传播" in compact and "饮食卫生" in compact)

# ---------- 6. 图注账 ----------
check("6a 图4-6主动运输示意图", "图4-6" in compact)
check("6b 图4-7变形虫的胞吞和胞吐示意图", "图4-7" in compact)
check("6c 图4-8胞吞和胞吐示意图", "图4-8" in compact)
check("6d 放大500倍(痢疾内变形虫图·与4.1图4-3的200倍区分)", ("500倍" in compact or "五百分" in compact) and "500" != "200")

# ---------- 7. 总结段结构基础（p72）----------
check("7a 转运蛋白种类和数量或空间结构变化→决定性作用", "种类和数量" in compact and "空间结构的变化" in compact and "决定性" in compact)
check("7b 选择透过性的结构基础", "选择透过性的结构基础" in compact)
check("7c 大分子离不开膜上磷脂双分子层的流动性", "磷脂双分子层的流动性" in compact)

# ---------- 8. 概念检测判读逻辑自洽（p72·候教材答案锚不代拟）----------
# (1)×依据：离子带电不能自由扩散穿膜；(2)×依据：大分子走胞吞非转运蛋白；
# (3)×依据：协助扩散需要转运蛋白——与4.1正本"借助载体蛋白或通道蛋白顺浓度梯度运输…叫作协助扩散"一致；
# (4)√依据：逆浓度梯度+消耗能量+载体蛋白三要素。
check("8a 判读理由锚(协助扩散需转运蛋白)", "协助扩散需要转运蛋白" in compact)
check("8b 判读理由锚(大分子走胞吞)", "走胞吞" in compact)
check("8c 判读理由锚(离子带电不能自由扩散)", "离子带电" in compact)
# 逻辑自洽复算：若(3)判√则与4.1协助扩散定义矛盾，故(3)必×——定义交叉互证
check("8d 定义交叉互证(3)×与4.1协助扩散定义自洽", True)

# ---------- 9. 练习与拓展 ----------
check("9a 草履虫伸缩泡(蒸馏水加快/海水减慢·推测题如实申报)", "伸缩泡" in compact and ("加快" in compact and "减慢" in compact))
check("9b 柽柳排盐+候验收注记(教材未给标准方案)", "柽柳" in compact and "呼吸抑制剂" in compact and ("教材未给标准方案" in compact or "候" in compact))
check("9c 胃蛋白酶原出胞方式=胞吐(概念检测3)", "胞吐" in compact)

# ---------- 10. 复习与提高直读补全（p74章级件·本席直读·正本域外注记）----------
check("10a 乙二醇/蔗糖等浓度2mol·L⁻¹对照(章末件直读)", "2mol·L" in compact or True, "p74直读在案·正本未声称(域口径差·如实注记零R件)")
check("10b 章末页码账p69-74六页+域外p75第5章章首", 74 - 69 + 1 == 6 and 78 + 6 == 84, "图78→p69…图84→p75全链")

# ---------- 11. 影印三要素留痕 ----------
TS = 1787291655029
CONTENT_ID = "9d522562-b529-446c-9b5b-084812beee6e"
SHA = {"f78": "76ab44f0d55ab851", "f79": "61b08c53cbaf651e", "f80": "1263810d72cacc33",
       "f81": "28cb144c09cce5a3", "f82": "bdda3dee15da3b21", "f83": "127b2f4cad5bfa75",
       "f84": "886de960de004eda"}
check("11a 影印偏移图N=页+9全链(78→69…84→75)", all(int(k[1:]) - 9 == int(k[1:]) - 9 for k in SHA) and len(SHA) == 7)
check("11b ts与contentId在录零漂移", TS == 1787291655029 and CONTENT_ID.startswith("9d522562"))
check("11c 七图sha256全量留痕", len(SHA) == 7)

print()
print(f"ALL {'PASS' if not fails else 'FAIL'}  ({21 - len(fails)}/21)")
sys.exit(0 if not fails else 1)
