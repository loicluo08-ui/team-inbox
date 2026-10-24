#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全库跨科总验·跨科词面一致性检查（ff2140e扩展·管理员16:33点名维度）
用法: python3 全库总验_跨科词面一致性.py <装配html...>（跨科混传·按目录自动分科）
输出: 分科词面命中矩阵（制作词/状态词·逐文件明细）＋跨科一致性结论＋豁免备案对照
口径: 词面族=CIWORDS(制作)+STATEWORDS(状态)·豁免备案=已判内容语言案例表（随全库总验扩展）"""
import re, sys, io, os, glob
from collections import defaultdict

CIWORDS = ['队7', '首件', 'claim', 'commit', '待核', '帧验', '底本', '席', 'canonical', '连跑', '升格', '认领', '装配件']
STATEWORDS = ['候补', '补装', '候装', '待装', '候裁', '占位', '骨架']
# 已判豁免备案（各轮QC判读沉淀·跨科一致性对照用）
EXEMPT = {
    '升格': '内容动词（"升格为公式铁门槛"物理教学语言/v18出处标注混排·1字级归出品席）',
    '骨架': '内容语言（"母题骨架/逐差法骨架/思维骨架"方法比喻）',
    '席': '跨词假阳性（"缺席"·候qc owner词边界升级）',
    '套现': '跨词假阳性（"一套现成"·候qc owner词边界升级）',
}

def subject_of(path):
    for k, v in [('地理', '地理'), ('物理', '物理'), ('数学', '数学'), ('化学', '化学'), ('生物', '生物'), ('语文', '语文'), ('英语', '英语')]:
        if k in path: return v
    return '其他'

if __name__ == '__main__':
    files = [a for a in sys.argv[1:] if a.endswith('.html')]
    matrix = defaultdict(list)
    for f in files:
        s = io.open(f, encoding='utf-8').read()
        subj = subject_of(f)
        hits = defaultdict(int)
        for w in CIWORDS + STATEWORDS:
            n = s.count(w)
            if n: hits[w] += n
        matrix[subj].append((os.path.basename(f), dict(hits)))
    print('═══ 跨科词面命中矩阵 ═══')
    for subj in sorted(matrix):
        total = defaultdict(int)
        for fn, hits in matrix[subj]:
            for w, n in hits.items(): total[w] += n
        clean = sum(1 for _, h in matrix[subj] if not h)
        print(f'[{subj}] 件数{len(matrix[subj])}·净件{clean}·科内词面合计{dict(total) if total else "零"}')
        for fn, hits in matrix[subj]:
            if hits:
                detail = '·'.join(f'{w}×{n}' for w, n in sorted(hits.items()))
                exem = [w for w in hits if w in EXEMPT]
                print(f'   {fn}: {detail}' + (f'（豁免备案:{exem}）' if exem else '（候判读）'))
    print('---\n一致性结论: 豁免备案外的新词面命中=候人工判读；同词面跨科处置不一=候对表统一')
    sys.exit(0)
