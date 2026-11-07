#!/usr/bin/env python3
"""移动端显示质量机检 v1（1107夜·承逸翔"全面制定解决方案"令A2件·深度对证报告v2发现：主形态（手机暗色html）QC零专项标准·形态倒挂修复）
用法: python3 qc_移动端显示_v1.py <html文件>...  或 目录（自动glob首学版_*.html）
三判据（最小可行集·候逸翔确权后可扩）:
  M1 视口适配: <meta name="viewport" 在场（缺失=手机按980px桌面渲染=字号不可控）
  M2 公式/SVG溢出防线: <svg>或宽元素需有max-width约束（css含max-width:100%或svg带width="100%"类）——防800px长图在窄屏横向截断公式
  M3 暗色对比度底线: body/主容器背景与正文色成对提取，对比度<4.5:1计❌（WCAG AA正文线·暗色主题的最低可读底线）
出口: exit0=全过；❌计数>0=exit1
"""
import re, sys, os, glob

def 对比度(c1, c2):
    def lum(c):
        r, g, b = [int(x, 16)/255 for x in c]
        f = lambda v: v/12.92 if v <= 0.03928 else ((v+0.055)/1.055)**2.4
        return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
    l1, l2 = lum(c1), lum(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi+0.05)/(lo+0.05)

def scan_html(path):
    txt = open(path, encoding='utf-8').read()
    issues = []
    # M1 viewport
    if not re.search(r'<meta[^>]+name=["\']viewport["\']', txt, re.I):
        issues.append(('M1视口缺失', '无viewport meta→手机按桌面980px渲染'))
    # M2 SVG/宽元素溢出防线
    svgs = re.findall(r'<svg[^>]*>', txt)
    if svgs:
        has_cap = bool(re.search(r'max-width\s*:\s*(100%|96%|94%|92%)', txt)) or bool(re.search(r'svg\s*\{[^}]*max-width', txt))
        fixed_wide = [s for s in svgs if re.search(r'width\s*=\s*["\']?(\d{3,})', s)]
        if not has_cap and fixed_wide:
            issues.append(('M2溢出防线缺', f'{len(fixed_wide)}个SVG固定像素宽且无max-width约束→窄屏截断风险'))
    # M3 对比度（提取成对 color/bgcolor）
    body_m = re.search(r'body\s*\{[^}]*\}', txt)
    fg = bg = None
    if body_m:
        blk = body_m.group(0)
        m1 = re.search(r'(?:^|[;\s])color\s*:\s*(#[0-9a-fA-F]{6})', blk)
        m2 = re.search(r'background(?:-color)?\s*:\s*(#[0-9a-fA-F]{6})', blk)
        fg = m1.group(1) if m1 else None
        bg = m2.group(1) if m2 else None
    if fg and bg:
        try:
            ratio = 对比度(fg, bg)
            if ratio < 4.5:
                issues.append(('M3对比度不足', f'{fg}on{bg}={ratio:.2f}:1<4.5:1(WCAG AA正文线)'))
        except ValueError:
            pass
    return issues

if __name__ == '__main__':
    targets = []
    for a in sys.argv[1:]:
        if os.path.isdir(a):
            targets += sorted(glob.glob(os.path.join(a, '**', '首学版_*.html'), recursive=True))
        else:
            targets.append(a)
    fail = 0
    for t in targets:
        try:
            issues = scan_html(t)
        except Exception as e:
            print(f'❌{os.path.basename(t)[:28]}: 扫描异常{e}')
            fail += 1
            continue
        if issues:
            fail += 1
            print(f'❌{os.path.basename(t)[:28]}: ' + '；'.join(f'{k}({v})' for k, v in issues))
    print(f'\n=== {len(targets)}件，{fail}件有移动端显示伤 ===')
    sys.exit(1 if fail else 0)
