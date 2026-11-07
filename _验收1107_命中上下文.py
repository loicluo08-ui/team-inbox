#!/usr/bin/env python3
# 1107验收：print扫描6处命中上下文逐处判读
import subprocess, re, os
os.chdir('/home/z/my-project/output/team-inbox')
cases = [
    ('产出_队4/print渲染V2.2_生物3.3_细胞核的结构和功能.pdf', '施工'),
    ('产出_队7/print渲染V2.2_地理1.3地球的圈层结构.pdf', '施工'),
    ('产出_队1/print渲染V2.2_生物1.1_细胞是生命活动的基本单位.pdf', '教材配套'),
    ('产出_队2/print渲染V2.2_数学1.3_集合的基本运算.pdf', '教材配套'),
    ('产出_队4/print渲染V2.2_物理1.2_时间位移.pdf', '教材配套'),
    ('产出_队2/print渲染V2.2_数学4.5_函数的应用（二）.pdf', '55196e0'),
]
for f, w in cases:
    if not os.path.exists(f):
        print(f'FILE_MISSING {f}')
        continue
    txt = subprocess.run(['pdftotext', f, '-'], capture_output=True, timeout=10).stdout.decode('utf-8', 'ignore')
    flat = re.sub(r'\s+', '', txt)
    hits = []
    i = flat.find(w)
    while i >= 0:
        hits.append(flat[max(0, i-30):i+30])
        i = flat.find(w, i+1)
    print(f'== {f} [{w}] {len(hits)}处')
    for h in hits:
        print('   …' + h + '…')
