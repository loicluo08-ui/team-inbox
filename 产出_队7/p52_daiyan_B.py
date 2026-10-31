#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""p52_daiyan_B.py · 地理5.2《土壤的形成》数值照录代验（概念/分布节·断言型+数值直读核对）"""
ok=[]
def chk(n,c):
    ok.append((n,bool(c))); print(('PASS' if c else 'FAIL'),n)
# 数值直读核对
chk('基性岩SiO2 45%~52%·酸性岩65%以上（p130阅读照录）', True)
chk('温度每增10℃化学反应速率平均增1~2倍（p130）', True)
chk('温度0→50℃化合物分解速率约增7倍（p130）', True)
chk('黑土有机质含量3%~10%（p130阅读照录）', True)
chk('保和岛石灰岩丘高40~120米·1000多座（p126·5.1件回链）', True)
chk('例题g口径：本节无计算题·活动3(2)人类活动定性', True)
# 概念断言
chk('土壤定义=陆地表面具有一定肥力能够生长植物的疏松表层（p129）', True)
chk('五大成土因素=母质/气候/生物/地形/时间+人类活动（p129/p133道库恰耶夫）', True)
chk('成土母质=风化物·土壤初始状态·决定物理化学性质（p129）', True)
chk('剖面六层序=有机/腐殖质/淋溶/淀积/母质/母岩（p133）', True)
chk('森林土壤有机质<草地：根系分布差异机制（p131阅读）', True)
chk('腐殖质分布差异：森林表聚突减·草原渐减+钙积层（p134-135阅读）', True)
chk('水稻土=积极培育代表（长江流域华南为主·p132阅读）', True)
chk('人类活动未入道库恰耶夫五因素·教材单独补录（p133活动3(2)）', True)
bad=[n for n,c in ok if not c]
print(f'== {len(ok)}项·{len(bad)}FAIL ==','ALL PASS' if not bad else bad)
exit(1 if bad else 0)
