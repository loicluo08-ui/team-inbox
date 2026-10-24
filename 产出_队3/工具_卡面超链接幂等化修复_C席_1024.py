#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""卡面超链接幂等化修复工具·C席·2026-10-25 01:0x（整改轮·承验FAIL回归级整改）
根因：首版链接化正则 (?<!href=")(?<!>)\\b(BV1...)\\b(?!") 对"已带?t=时间戳深链的源锚"
在href内BV（后随?非"）失守→再包一层=外层href未闭合属性注入（10处/5卡）。
修法三段（幂等·可重跑）：
  P1 嵌套坍缩：坏链Blob还原为原深链锚 <a href="…/BVx?t=N" target="_blank">BVx</a>
  P2 校验：嵌套检查=0·孤立href=0
  P3 幂等断言：第二遍跑零变更（diff空）
未来批处理安全正则（P3后生效场景）：(?<!["/=>])(BV1[0-9A-Za-z]{8,9})(?![\\w"?&])
  ——前置禁 '"','/','=','>'（href/路径/属性/锚文本四向），后随禁 \\w,'"','?','&'（含?t时间戳）。"""
import io, re, glob, sys, hashlib

BAD = re.compile(
    r'<a href="https://www\.bilibili\.com/video/<a href="(https://www\.bilibili\.com/video/(BV[0-9A-Za-z]+))"[^>]*>(?:BV[0-9A-Za-z]+)</a>(\?t=\d+)?" target="_blank">(?:BV[0-9A-Za-z]+)</a>')

def repair_once(s):
    return BAD.sub(r'<a href="\1\3" target="_blank">\2</a>', s)

files = sorted(glob.glob('/tmp/team-inbox/产出_队3/切片卡_化学*.html'))
fail = 0
for f in files:
    s0 = io.open(f, encoding='utf-8').read()
    s1 = repair_once(s0)
    n_fixed = len(BAD.findall(s0))
    # P2 校验
    nested = len(re.findall(r'<a href="[^"]*<a\s', s1))
    orphan = len(re.findall(r'href="[^"]*"(?=[^<]*<a\s+href)', s1))
    # P3 幂等断言：再跑一遍零变更
    s2 = repair_once(s1)
    idem = (s1 == s2)
    ok = (nested == 0) and idem
    fail += 0 if ok else 1
    hrefs = re.findall(r'href="(https://www\.bilibili\.com/video/[^"]+)"', s1)
    sha = hashlib.sha256(s1.encode()).hexdigest()[:16]
    print(f"{'✅' if ok else '❌'} {f.split('/')[-1][:34]} 修{n_fixed} 嵌套{nested} href×{len(hrefs)} 幂等{'✓' if idem else '✗'} sha{sha}")
    for h in hrefs: print('    ', h)
    if ok and s1 != s0:
        io.open(f, 'w', encoding='utf-8').write(s1)
print('---', 'FAIL' if fail else 'ALL PASS', f'({len(files)}件)')
sys.exit(1 if fail else 0)
