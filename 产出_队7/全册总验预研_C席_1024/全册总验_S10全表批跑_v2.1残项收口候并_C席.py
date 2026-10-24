#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全册总验·S10全表批跑 v2.1残项收口候并件（A2词面/A3机检/B组结构/D组标签·硬伤=REJECT级·软项=数据行）
身份=1024晚任务包§二-B工具债单的**残项收口候并件**（C席·独立落盘不覆盖现行态）：
  ⚠ 工具债主诉办结归队6（70276d4·管理员20:47令承办·import scan单一信源+白名单'一套现成'依令入列
    ·2.1套现机检域归零——现行态批跑py=队6版，本件不覆盖不替换，候管理层择用/合并/弃）；
  本件在队6版同向修法（import qc_v1.1 scan单一信源）上补齐残差三项（队6版实测仍各报硬伤1）：
  ①A2词面残差：2.2"席"←"本地缺席"跨词假阳性（备案粘连词整词占位·豁免明细随行可审计）；
  ②D组残差：3.2/3.3 div失衡=纯sec开标签未闭合装配器家族自愈结构（收窄豁免+栈匹配定位·
    备案=预跑甄别"单节件家族div归属出品席"+任务包§一地理0真伤判定双源·多余闭合/他标签失衡仍硬伤）；
  ③审计力：豁免明细+备案依据随行输出·信源版本行随跑打印（黑/白名单词数防漂移）；
  兼容态：EXEMPT'套现←一套现成'与队6依令入列qc白名单'一套现成'双保险冗余无害（本件占位先于scan）。
用法: python3 全册总验_S10全表批跑_v2.1残项收口候并_C席.py <a.html> [b.html ...] [--skip-machine]
说明: B组因学科形态差异输出数据行不硬判（语英碎片簇/单节/章级同跑）；硬伤=词面命中+机检待修+标签失衡"""
import re, sys, io, os, importlib.util, tempfile

# ——单一信源：qc机检v1.1（0bf57ba升版）——黑/白名单唯一信源在qc脚本，本工具零内嵌机检词表——
_QC = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'qc_金融语域机检_v1.py'))
_spec = importlib.util.spec_from_file_location('qc_scan', _QC)
qc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(qc)

CIWORDS = ['队7', '首件', 'claim', 'commit', '待核', '帧验', '底本', '席', 'canonical', '连跑', '升格', '认领', '装配件']
STATEWORDS = ['候补', '补装', '候装', '待装', '候裁', '占位', '骨架']

# ——白名单级豁免备案表：{命中词: [(粘连词, 备案依据)]}（跨词假阳性案·占位机制与qc白名单同型）——
EXEMPT = {
    '套现': [('一套现成', '预跑甄别1024+fefd293工具债单88bb3e3备案：正文"一套现成的活教材"系汉语短语非金融语域')],
    '席':   [('缺席',     '预跑甄别1024备案：正文"本地缺席"系区域认知教学表述非制作语')],
}

def _strip_exempt(text):
    """备案粘连词整词占位（先于一切词面/机检判定）；返回(净化文本, 豁免明细[(词,粘连词,处数,依据)])"""
    log = []
    for w, entries in EXEMPT.items():
        for glue, basis in entries:
            n = text.count(glue)
            if n:
                text = text.replace(glue, '◇' * len(glue))
                log.append((w, glue, n, basis))
    return text, log

def audit(path, skip_machine):
    raw = io.open(path, encoding='utf-8').read()
    s, exlog = _strip_exempt(raw)
    r, hard = [], 0
    cmark = len(re.findall(r'^(<{7}|={7}|>{7})', s, re.M))
    if cmark: r.append(f'🔴冲突标记{cmark}处'); hard += 1
    ci = [w for w in CIWORDS if w in s]
    ex_a2 = [(w, g, n) for (w, g, n, _) in exlog if w in CIWORDS or w in STATEWORDS]
    if ci: r.append(f'🄰2制作词命中{ci}'); hard += 1
    else: r.append('🄰2制作词0' + (f'（⭕豁免{[f"{g}×{n}" for w, g, n in ex_a2]}·备案粘连词占位）' if ex_a2 else ''))
    sw = [w for w in STATEWORDS if w in s]
    if sw: r.append(f'🄰2状态词(软)命中{sw}·候人工判读（内容短语如"母题骨架"系合法课程语言）')  # 软项不计入硬伤
    if not skip_machine:
        # scan单一信源：扫备案占位后的文本（临时文件承载），qc内部白名单机制照常运行
        tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8',
                                          dir=os.path.dirname(os.path.abspath(path)))
        tmp.write(s); tmp.close()
        try:
            hits = qc.scan(tmp.name)
        finally:
            os.unlink(tmp.name)
        real = [(w, ln) for w, ln in hits if w not in EXEMPT]
        ex_a3 = [(w, g, n) for (w, g, n, _) in exlog if w not in CIWORDS and w not in STATEWORDS]
        if real:
            r.append(f'🄰3机检❌待修{len(real)}处' + ''.join(f' [{w}]{ln[:36]}' for w, ln in real[:3])); hard += 1
        else:
            parts = []
            if hits: parts.append(f'scan残留{len(hits)}处:{sorted({w for w, _ in hits})}（qc白名单消化）')
            if ex_a3: parts.append(''.join(f'⭕{w}←"{g}"×{n}备案占位生效' for w, g, n in ex_a3))
            note = f'（{"·".join(parts)}）' if parts else ''
            r.append(f'🄰3机检✅0待修{note}')
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
        if o != c:
            stack, over = [], 0
            for m in re.finditer(f'<{t}[ >]|</{t}>', s):
                if m.group(0).startswith('</'):
                    if stack: stack.pop()
                    else: over += 1
                else:
                    stack.append(s[:m.start()].count('\n') + 1)
            lines = s.split('\n')
            locs = [f'L{n}:{(lines[n-1].strip()[:28] if n <= len(lines) else "?")}' for n in stack[:3]]
            tag = f'🄳标签失衡{t}:{o}/{c}' + (f'·未闭合@{locs}' if stack else '') + (f'·多余闭合{over}处' if over else '')
            # 收窄豁免：失衡=纯<div class="sec">开标签未闭合（零多余闭合·栈剩余全为sec）→装配器家族自愈结构
            # 备案依据：预跑甄别"单节件家族div归属出品席"+任务包§一地理0真伤判定·豁免可审计；他标签失衡/多余闭合仍硬伤
            pure_sec = t == 'div' and over == 0 and stack and all(
                n <= len(lines) and '<div class="sec"' in lines[n-1] for n in stack)
            if pure_sec:
                r.append(tag + '（⭕豁免：纯sec开标签未闭合系装配器家族自愈结构·预跑甄别+任务包地理0真伤双备案·归属出品席）')
            else:
                r.append(tag); hard += 1
    return hard, r

if __name__ == '__main__':
    args = sys.argv[1:]
    skip = '--skip-machine' in args
    files = [a for a in args if a.endswith('.html')]
    print(f'🄰3信源={os.path.basename(_QC)}（内容v1.1·0bf57ba升版·黑名单{len(qc.黑名单)}词+白名单{len(qc.白名单)}词:{"/".join(qc.白名单)}）·豁免备案{len(EXEMPT)}词:{"/".join(sorted(EXEMPT))}')
    nfail = 0
    for f in files:
        hard, r = audit(f, skip)
        nfail += hard
        print(f"[硬伤{hard}] {os.path.basename(f)}")
        for x in r: print('   ', x)
    print(f'---\nS10批跑v2: {len(files)}件·硬伤{nfail}（软项数据行供启用时判读·豁免明细随行可审计）')
    sys.exit(1 if nfail else 0)
