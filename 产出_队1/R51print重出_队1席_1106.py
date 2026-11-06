#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R-51 print重出：print(旧)文本比select源html→重渲染→页数守恒+12族复扫"""
import subprocess, re, os, sys, unicodedata, difflib, glob

T12 = ['sympy','影印','卷源','本席','留痕','施工','候锚','随件','裁定','已交付','在产','池标']
def norm(s): return re.sub(r'\s+','',unicodedata.normalize('NFKC',s))
def ptext(p):
    r = subprocess.run(['pdftotext',p,'-'],capture_output=True,text=True)
    return norm(r.stdout)
def pages(p):
    r = subprocess.run(['pdfinfo',p],capture_output=True,text=True)
    m = re.search(r'Pages:\s+(\d+)', r.stdout); return int(m.group(1))

# (print路径, 候选html列表——按序试)
B='产出_队1'; G='产出_队7'
JOBS = [
 (f'{B}/print渲染V2.2_生物1.1_细胞是生命活动的基本单位.pdf',
  [f'{B}/首学版_生物1.1_细胞是生命活动的基本单位_队1席B线_1031.html']),
 (f'{B}/print渲染V2.2_生物2.1_细胞中的元素和化合物.pdf',
  [f'{B}/首学版_生物2.1_细胞中的元素和化合物_报告汇总员_1031.html', f'{B}/首学版_生物2.1_细胞中的元素和化合物_群外管理员席_1031.html']),
 (f'{B}/print渲染V2.2_生物2.1_细胞中的元素和化合物_群外管理员席_临时正本版.pdf',
  [f'{B}/首学版_生物2.1_细胞中的元素和化合物_群外管理员席_1031.html']),
 (f'{B}/print渲染V2.2_生物2.3_细胞中的糖类和脂质.pdf',
  [f'{B}/首学版_生物2.3_细胞中的糖类和脂质_报告汇总员_1031.html']),
 (f'{B}/print渲染V2.2_生物2.4_蛋白质是生命活动的主要承担者.pdf',
  [f'{B}/首学版_生物2.4_蛋白质是生命活动的主要承担者_报告汇总员_1031.html']),
 (f'{B}/print渲染V2.2_生物2.5_核酸是遗传信息的携带者.pdf',
  [f'{B}/首学版_生物2.5_核酸是遗传信息的携带者_并行搜索员B_1031.html']),
 (f'{B}/print渲染V2.2_生物2.5_核酸是遗传信息的携带者_报告汇总员_临时正本版.pdf',
  [f'{B}/首学版_生物2.5_核酸是遗传信息的携带者_报告汇总员_1031.html']),
 (f'{B}/print渲染V2.2_生物3.1_细胞膜的结构和功能.pdf',
  [f'{B}/首学版_生物3.1_细胞膜的结构和功能_报告汇总员_1031.html']),
 (f'{B}/print渲染V2.2_生物3.2_细胞器之间的分工合作.pdf',
  [f'{B}/首学版_生物3.2_细胞器之间的分工合作_队7席接手_1031.html']),
 (f'{B}/print渲染V2.2_生物5.2_细胞的能量货币ATP.pdf',
  [f'{B}/首学版_生物5.2_细胞的能量货币ATP_队7席跨科_1031.html']),
 (f'{B}/print渲染V2.2_生物5.3_细胞呼吸的原理和应用.pdf',
  [f'{B}/首学版_生物5.3_细胞呼吸的原理和应用_队7席跨科_1031.html']),
 (f'{B}/print渲染V2.2_生物6.1_细胞的增殖.pdf',
  [f'{B}/首学版_生物6.1_细胞的增殖_队2席转援_1031.html']),
 (f'{G}/print渲染V2.2_地理1.1_地球的宇宙环境.pdf',
  [f'{G}/首学版_地理1.1_地球的宇宙环境_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理1.2_太阳对地球的影响.pdf',
  [f'{G}/首学版_地理1.2_太阳对地球的影响_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理1.2_太阳对地球的影响_群外管理员席版.pdf',
  [f'{G}/首学版_地理1.2_太阳对地球的影响_群外管理员席_1031.html']),
 (f'{G}/print渲染V2.2_地理1.3地球的圈层结构.pdf',
  [f'{G}/首学版_地理1.3地球的圈层结构_群外管理员席_1031.html']),
 (f'{G}/print渲染V2.2_地理2.1_流水地貌.pdf',
  [f'{G}/首学版_地理2.1_流水地貌_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理2.1_流水地貌_群外管理员席版.pdf',
  [f'{G}/首学版_地理2.1_流水地貌_群外管理员席_1031.html']),
 (f'{G}/print渲染V2.2_地理2.3_喀斯特海岸和冰川地貌.pdf',
  [f'{G}/首学版_地理2.3_喀斯特海岸和冰川地貌_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理3.2_大气受热过程.pdf',
  [f'{G}/首学版_地理3.2_大气受热过程_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理3.3_大气热力环流.pdf',
  [f'{G}/首学版_地理3.3_大气热力环流_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理4.1_水循环.pdf',
  [f'{G}/首学版_地理4.1_水循环_队7席_1031.html']),
 (f'{G}/print渲染V2.2_地理4.2_海水的性质和运动.pdf',
  [f'{G}/首学版_地理4.2_海水的性质和运动_队7席_1031.html']),
]

bad = 0
for pf, cands in JOBS:
    old_t = ptext(pf); old_pg = pages(pf)
    best = None
    for h in cands:
        tmp = f'/tmp/r51_render_{os.getpid()}.pdf'
        r = subprocess.run(['weasyprint', h, tmp], capture_output=True, text=True)
        if r.returncode != 0:
            print(f'✗ RENDER FAIL {os.path.basename(h)}: {r.stderr[:120]}'); bad += 1; continue
        t = ptext(tmp)
        ratio = difflib.SequenceMatcher(None, old_t, t, autojunk=False).ratio()
        if best is None or ratio > best[1]:
            best = (tmp, ratio, h, t)
    if best is None:
        print(f'✗ {os.path.basename(pf)} 无可用渲染'); bad += 1; continue
    tmp, ratio, h, new_t = best
    new_pg = pages(tmp)
    hits = sum(new_t.count(tok) for tok in T12)
    pg_ok = (old_pg == new_pg)
    tag = '✓' if (pg_ok and hits == 0) else '⚠'
    if not (pg_ok and hits == 0): bad += 1
    print(f'{tag} {os.path.basename(pf)[:52]}')
    print(f'    源={os.path.basename(h)[:50]} ratio={ratio:.4f} 页数{old_pg}→{new_pg} 12族残留={hits}')
    os.replace(tmp, pf)
print('BAD =', bad)
