# -*- coding: utf-8 -*-
"""数学第4章补装配：4.1-4.5升格重制件 → 章级装配HTML（第3章同款模板）
节件md块结构 → HTML；表格转HTML table；数学Unicode符号原样保留
"""
import re, html as H

BASE = '/home/z/my-project/output/team-inbox/产出_队2/'
SECTIONS = [
    ('4.1·队2_指数_升格重制件.md', '4.1 指数'),
    ('4.2·队2_指数函数_升格重制件.md', '4.2 指数函数'),
    ('4.3·队2_对数_升格重制件.md', '4.3 对数'),
    ('4.4·队2_对数函数_升格重制件.md', '4.4 对数函数'),
    ('4.5·队2_函数的应用（二）_升格重制件.md', '4.5 函数的应用（二）'),
]
SKIP_BLOCKS = {'源注（溯源补全·严格全检10/25）'}
TITLE = '数学必修一·第4章（指数函数与对数函数·升格重制件装配版）'

CSS = '''body{max-width:800px;margin:0 auto;padding:20px 16px;background:#111418;color:#e8e6e3;
font:12.6px/1.85 Georgia,'Noto Serif SC',serif;}
h1{font-size:22px;color:#fff;border-bottom:2px solid #4da3ff;padding-bottom:8px;}
h1.chap{text-align:center;}
h2{font-size:18px;color:#4da3ff;margin-top:34px;}
h3{font-size:15.5px;color:#7ec9a0;}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:12px;}
th{background:#1c2430;color:#4da3ff;} th,td{border:1px solid #2a3140;padding:8px 10px;text-align:left;vertical-align:top;}
tr:nth-child(even) td{background:#161b22;}
hr{border:0;border-top:1px dashed #2a3140;margin:26px 0;}
code{background:#1c2430;color:#e0a34d;padding:1px 5px;border-radius:4px;}
strong{color:#fff;} em{color:#e0a34d;}
p{margin:10px 0;}
blockquote{border-left:3px solid #4da3ff;margin:10px 0;padding:6px 12px;background:#161b22;}
@media print{body{background:#fff !important;color:#111 !important;} h1{color:#000 !important;} h2{color:#1a4d8f !important;} h3{color:#14532d !important;} th{background:#e8eef5 !important;color:#1a4d8f !important;} tr:nth-child(even) td{background:#f5f7fa !important;} strong{color:#000 !important;} em{color:#7a4d00 !important;}}'''

def md_block_to_html(name, body):
    """一个◆块 → HTML片段"""
    out = []
    if name.startswith('课时开篇页'):
        out.append('<h2>课时开篇页</h2>')
        body = re.sub(r'^本节知识点清单[：:]?', '**本节知识点清单**：', body)
    elif name.startswith('速览卡'):
        out.append('<h2>速览卡（10秒版）</h2>')
    elif name.startswith('正文'):
        out.append('<h2>正文</h2>')
    elif name.startswith('经典例题'):
        out.append('<h2>经典例题精讲</h2>')
    elif name.startswith('易错卡'):
        out.append(f'<h2>{H.escape(name)}</h2>')
    elif name.startswith('应试打法'):
        out.append('<h2>应试打法（本节题型通用思路）</h2>')
    elif name.startswith('深读区'):
        out.append(f'<h2>{H.escape(name)}</h2>')
    elif name.startswith('费曼检验'):
        out.append('<h2>费曼检验（学完立即做 · 2分钟）</h2>')
    elif name.startswith('本节串联图'):
        out.append('<h2>本节串联图（文字版）</h2>')
    elif name.startswith('升维'):
        out.append(f'<h2>{H.escape(name)}</h2>')
    else:
        out.append(f'<h2>{H.escape(name)}</h2>')
    # 行级渲染
    in_table = False
    table_rows = []
    def flush_table():
        nonlocal in_table, table_rows
        if table_rows:
            out.append('<table>' + ''.join(table_rows) + '</table>')
            table_rows = []
        in_table = False
    for line in body.split('\n'):
        ls = line.strip()
        if not ls:
            flush_table(); continue
        # 表格行
        if ls.startswith('|') and ls.count('|') >= 2:
            cells = [c.strip() for c in ls.strip('|').split('|')]
            if all(re.fullmatch(r'[-: ]+', c) for c in cells if c): continue  # 分隔行
            tds = ''.join(f'<td>{inline(c)}</td>' for c in cells)
            table_rows.append(f'<tr>{tds}</tr>')
            in_table = True
            continue
        flush_table()
        # 标题/引用/列表/段落
        if ls.startswith('#### '): out.append(f'<h3>{inline(ls[5:])}</h3>')
        elif ls.startswith('### '): out.append(f'<h3>{inline(ls[4:])}</h3>')
        elif ls.startswith('## '): out.append(f'<h3>{inline(ls[3:])}</h3>')
        elif ls.startswith('> '): out.append(f'<blockquote>{inline(ls[2:])}</blockquote>')
        elif re.match(r'^[-*] ', ls): out.append(f'<p>· {inline(ls[2:])}</p>')
        elif re.match(r'^\d+[.、] ', ls): out.append(f'<p>{inline(ls)}</p>')
        elif ls == '---': out.append('<hr>')
        else: out.append(f'<p>{inline(ls)}</p>')
    flush_table()
    return '\n'.join(out)

def inline(s):
    s = H.escape(s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

def parse_section(path):
    t = open(path, encoding='utf-8').read()
    # 去掉一级标题行
    t = re.sub(r'^#[^\n]*\n', '', t)
    parts = re.split(r'^## ([^\n]+)$', t, flags=re.M)
    blocks = []
    i = 1
    while i < len(parts):
        name, body = parts[i].strip(), parts[i+1]
        base = re.sub(r'[（(][^)）]*[)）]\s*$', '', name).strip()
        if any(base.startswith(k) or name.startswith(k) for k in SKIP_BLOCKS):
            i += 2; continue
        blocks.append((name, body))
        i += 2
    return blocks

def main():
    out = [f'<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8"><title>{TITLE}</title><style>{CSS}</style></head><body>']
    out.append(f'<h1 class="chap">{H.escape(TITLE)}</h1>')
    out.append('<div class="map" style="border:1px solid #2a3140"><strong>章首地图</strong>：4.1 指数（分数指数幂·根式化）→ 4.2 指数函数（增长衰减族）→ 4.3 对数（指数的逆运算）→ 4.4 对数函数（增长尺）→ 4.5 函数的应用（二）——主线：指数式→指数函数→问"几次方"（对数）→对数函数→真数对数齐上阵解应用题。每节末尾的深读区不读不影响做题；趣味与背景在节末。</div>')
    for path, sec_title in SECTIONS:
        blocks = parse_section(BASE + path)
        out.append(f'<h1>{H.escape(sec_title)}</h1>')
        for name, body in blocks:
            out.append(md_block_to_html(name, body))
        out.append('<hr>')
    out.append('<div class="feedback">本册由4.1-4.5升格重制件（10/26 00:28全检战役版）装配，数学断言已过推导链机检v3（2084链层），构造层审计轮候排产。</div>')
    out.append('</body></html>')
    html = '\n'.join(out)
    dst = BASE + '装配_数学必修一_第4章_升格版_1026.html'
    open(dst, 'w', encoding='utf-8').write(html)
    print('写出:', dst, len(html), '字节')

if __name__ == '__main__':
    main()
