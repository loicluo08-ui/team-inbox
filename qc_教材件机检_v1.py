#!/usr/bin/env python3
"""教材件专用机检 v1.1（1031晚全面修复轮·双层信号版）
用法: python3 qc_教材件机检_v1.py <html文件>...
双层信号：词面检=import金融机检v1.2词表（单一事实源·命中=⚠️已知候裁账不计FAIL·裁定二候裁账不重复报）
         结构四检=❌真伤计FAIL（占位符/div配平/table配平/print层/svg aria）
教材件=首学版_*.html（工作件走qc_金融语域机检_v1.py分工）
"""
import re, sys, os
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('qc_fin', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qc_金融语域机检_v1.py'))
_qcfin = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_qcfin)
红线词 = _qcfin.黑名单
白名单 = _qcfin.白名单
占位符模式 = re.compile(r'(TODO|FIXME|XXX|待补|待填|【候补】|\?\?\?|占位)')

def scan_html(path):
    word_hits, issues = [], []
    txt = open(path, encoding='utf-8').read()
    body = txt
    for w in 白名单: body = body.replace(w, '◇')
    for w in 红线词:
        for ln in body.split('\n'):
            if w in ln and not re.search(r'换血声明|自检|对照', ln):
                word_hits.append(w); break
    m = 占位符模式.search(re.sub(r'<[^>]+>', '', body))
    if m: issues.append(('占位符', m.group(0)))
    d1, d2 = txt.count('<div'), txt.count('</div>')
    t1, t2 = txt.count('<table'), txt.count('</table>')
    if d1 != d2: issues.append(('div配平', f'{d1}/{d2}'))
    if t1 != t2: issues.append(('table配平', f'{t1}/{t2}'))
    if 'print' not in txt and '@media print' not in txt: issues.append(('print层', '缺失'))
    if 'aria-label' not in txt and '<svg' in txt: issues.append(('svg无aria', '位置图机检口径'))
    return word_hits, issues

if __name__ == '__main__':
    fail = 0
    for t in sys.argv[1:]:
        name = os.path.basename(t)[:28]
        word_hits, issues = scan_html(t)
        warn = f' ⚠️词面{len(word_hits)}处已知候裁账({",".join(word_hits[:3])})' if word_hits else ''
        if issues:
            fail += 1
            print(f'❌{name}:{warn}')
            for tag, ctx in issues[:6]: print(f'    [{tag}] {ctx}')
        else:
            print(f'✅{name}: 结构四检全过{warn}')
    print(f'\n=== {len(sys.argv)-1}件，{fail}件结构真伤 ===')
    sys.exit(1 if fail else 0)
