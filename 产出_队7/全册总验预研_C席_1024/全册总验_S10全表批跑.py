#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全册总验·S10全表批跑（A2词面/A3机检/B组结构/D组标签·硬伤=REJECT级·软项=数据行）
用法: python3 全册总验_S10全表批跑.py <a.html> [b.html ...] [--skip-machine]
说明: B组因学科形态差异输出数据行不硬判（语英碎片簇/单节/章级同跑）；硬伤=词面命中+机检待修+标签失衡"""
import re, sys, io, os, subprocess

CIWORDS = ['队7', '首件', 'claim', 'commit', '待核', '帧验', '底本', '席', 'canonical', '连跑', '升格', '认领', '装配件']
STATEWORDS = ['候补', '补装', '候装', '待装', '候裁', '占位', '骨架']

def audit(path, skip_machine):
    s = io.open(path, encoding='utf-8').read()
    r, hard = [], 0
    cmark = len(re.findall(r'^(<{7}|={7}|>{7})', s, re.M))
    if cmark: r.append(f'🔴冲突标记{cmark}处'); hard += 1
    ci = [w for w in CIWORDS if w in s]
    if ci: r.append(f'🄰2制作词命中{ci}'); hard += 1
    sw = [w for w in STATEWORDS if w in s]
    if sw: r.append(f'🄰2状态词(软)命中{sw}·候人工判读（内容短语如"母题骨架"系合法课程语言）')  # 软项不计入硬伤
    if not skip_machine:
        qc = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'qc_金融语域机检_v1.py')
        p = subprocess.run(['python3', qc, path], capture_output=True, text=True)
        ok = '0 个待修' in p.stdout or '0个待修' in p.stdout
        r.append(f'🄰3机检{"✅" if ok else "⚠️待修"}')
        if not ok: hard += 1
    h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', s)
    plain = [re.sub(r'<[^>]+>', '', x) for x in h2]
    r.append(f'🄱1开篇页{"✅" if plain and "开篇" in plain[0] else "无"}')
    r.append(f'🄱2速览卡{"✅" if any("速览" in x for x in plain[:2]) else "无"}')
    xh = [m for m in re.findall(r'<h[123][^>]*>([^<]*(?:第?[一二三四五六七八九1-9]+)[、.．][^<]{0,14})', s)
          if not re.match(r'^\s*\d\.\d\s', m) and '–' not in m and '—' not in m and not re.match(r'^\s*第.{1,3}章', m)]
    if xh: r.append(f'🄱3序号残留{len(xh)}:{[x[:16] for x in xh[:2]]}'); hard += 1
    else: r.append('🄱3序号残留0(节号照录/版本词/章序豁免)')
    r.append(f'🄱4四要素=题干{s.count("【题干】")}/解答{s.count("【解答】")}/怎么想到{s.count("怎么想到的")}/定级{s.count("定级")}')
    r.append(f'🄱5易错卡{"✅" if any("易错卡" in x for x in plain) else "无"}')
    r.append(f'🄱7深读区句{"✅" if "不读不影响" in s else "无"}')
    r.append(f'🄱8费曼{"✅" if any("费曼" in x for x in plain) else "无"}')
    r.append(f'🄱9glow×{len(re.findall(chr(34)+"(?:mark )?glow"+chr(34), s))}/SVG×{s.count("<svg")}·toc{"✅" if s.count(chr(34)+"toc"+chr(34)) else "无"}')
    for t in ['div', 'table', 'svg', 'h2', 'h3', 'p', 'ul', 'li', 'a']:
        o = len(re.findall(f'<{t}[ >]', s)); c = len(re.findall(f'</{t}>', s))
        if o != c: r.append(f'🄳标签失衡{t}:{o}/{c}'); hard += 1
    return hard, r

if __name__ == '__main__':
    args = sys.argv[1:]
    skip = '--skip-machine' in args
    files = [a for a in args if a.endswith('.html')]
    nfail = 0
    for f in files:
        hard, r = audit(f, skip)
        nfail += hard
        print(f"[硬伤{hard}] {os.path.basename(f)}")
        for x in r: print('   ', x)
    print(f'---\nS10批跑: {len(files)}件·硬伤{nfail}（软项数据行供启用时判读）')
    sys.exit(1 if nfail else 0)
