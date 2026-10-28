#!/usr/bin/env python3
"""照录diff v3（1028试点定版·物4章三卡标定候选率10%）
用法: python3 qc_照录diff_v3.py <切片卡或装配html> <v18原册html> [节件字段块md...]
角色=候选生成器：候漂移≠漂移，全部进人工复核。三源=v18原册+节件字段块+同章装配册。
"""
import re, html, sys, glob, os
def norm(s): return re.sub(r'\s+','',s)
card, v18 = sys.argv[1], sys.argv[2]
jie = sys.argv[3:] or sorted(glob.glob(os.path.join(os.path.dirname(card),'物理-4.*.md')))
src_v18 = norm(re.sub(r'<[^>]+>','',open(v18,encoding='utf-8').read()))
src_jie = norm(''.join(open(f,encoding='utf-8').read() for f in jie))
asm = os.path.join(os.path.dirname(card),'装配_物理必修一_第4章_1024.html')
src_asm = norm(re.sub(r'<[^>]+>','',open(asm,encoding='utf-8').read())) if os.path.exists(asm) else ''
skip=['本件按双段卡','源注汇总','出品基准','高考接口（','缺段豁免','probe实测','池候选','实采留痕','装配层插桩','费曼检验','怎么用这张卡','切片卡｜','分工账：','承办：','生成：','注记（v18']
raw=re.sub(r'<style[^>]*>.*?</style>',' ',open(card,encoding='utf-8').read(),flags=re.S)
txt=html.unescape(re.sub(r'<[^>]+>','\n',raw))
lines=[l.strip() for l in txt.split('\n') if len(l.strip())>=10]
hit=miss=0; misses=[]
for i,l in enumerate(lines):
    if re.search(r'(照录|v18原话|v18口径|钉死（v18|口诀（v18|锚（v18)',l):
        if any(k in l for k in skip): continue
        cand=l+(lines[i+1] if i+1<len(lines) else '')
        segs=[s for s in re.split(r'[：:（）()｜｜。；;，,]',cand) if 4<=len(norm(s)) and 'v18' not in s and 'BV' not in s]
        found=False
        for s in segs:
            ns=norm(s)
            for source in (src_v18,src_jie,src_asm):
                probe=ns[len(ns)//4:len(ns)//4+20] if len(ns)>30 else ns
                if probe and probe in source: found=True; break
            if found: break
        if found: hit+=1
        else: miss+=1; misses.append(cand[:90])
print(f"声称照录块={hit+miss} 命中={hit} 候漂移={miss}（候选率{miss/(hit+miss)*100:.0f}%·全进人工复核）")
for m in misses: print("  候漂移:",m)
