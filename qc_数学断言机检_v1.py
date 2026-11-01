# -*- coding: utf-8 -*-
"""数学断言机检 v1：提取全部 .md/.html 资料中的数学等式/数值断言，sympy/数值回代验证
用法: python3 qc_数学断言机检_v1.py <md/html文件...>  （缺省=六科全部装配册+节件）
输出: 红件清单（可疑断言+上下文）→ _数学断言红件_日期.md
"""
import re, sys, glob

def extract_assertions(text):
    """提取疑似数学断言行：含 = 且含数字/变量/运算符的文本行（剥HTML）"""
    out = []
    for ln in text.split('\n'):
        ln = ln.strip()
        if len(ln) < 8 or len(ln) > 200: continue
        # 排除非数学行
        if re.search(r'(BV\w{6,}|http|第[一二三四五六七八九十]+条|202[3-6]年|页|版本|commit|sha)', ln): continue
        # 必须含等号/比较符 + 数字运算
        if not re.search(r'[=<>≤≥≈]', ln): continue
        if not re.search(r'\d|[x₁-₉a-z]', ln): continue
        # 运算密度：至少2个运算符或1个函数
        ops = len(re.findall(r'[+\-*/×÷^√]|log|sin|cos|tan|\^', ln))
        if ops < 1: continue
        out.append(ln)
    return out

def try_verify(expr_str):
    """尝试sympy/数值验证一个断言；返回 (状态, 详情)
    状态: SKIP(无法解析/非等式断言) / OK(验证通过) / BAD(两侧不等) / AMBIG(歧义需人工)"""
    try:
        import sympy as sp
    except ImportError:
        return ('SKIP', 'no sympy')
    # 只验"数值等式"类：形如 a=b（两侧可算出具体数值）或可符号化简
    m = re.match(r'^([^=<>≈]+)=([^=<>≈]+)$', expr_str.replace('≈','='))
    if not m: return ('SKIP', 'not-pure-eq')
    L, R = m.group(1).strip(), m.group(2).strip()
    # 拒绝含自由汉字的
    if re.search(r'[\u4e00-\u9fff]', L+R): return ('SKIP', 'has-chinese')
    try:
        Ls = sp.sympify(L.replace('^','**').replace('√','sqrt'), rational=True)
        Rs = sp.sympify(R.replace('^','**').replace('√','sqrt'), rational=True)
        d = sp.simplify(Ls - Rs)
        if d == 0: return ('OK', str(d))
        # 数值抽样：含未知数时随机代入5组比对
        syms = (Ls.free_symbols | Rs.free_symbols)
        if syms:
            import random
            for _ in range(8):
                sub = {s: sp.Rational(random.randint(2,9), random.choice([1,2,4])) for s in syms}
                try:
                    lv, rv = float(Ls.subs(sub)), float(Rs.subs(sub))
                    if abs(lv-rv) > 1e-9*max(1,abs(lv)):
                        return ('BAD', f'反例{dict(sub)}: {lv}≠{rv}')
                except (ZeroDivisionError, TypeError, ValueError): continue
            return ('AMBIG', f'符号差={d}（抽样未见反例，需人工）')
        return ('BAD', f'常量差={d}')
    except Exception as e:
        return ('SKIP', f'parse:{str(e)[:30]}')

def main():
    files = sys.argv[1:]
    if not files:
        files = (glob.glob('产出_队2/装配_数学*.html') + glob.glob('产出_队4/装配_物理*.html')
                 + glob.glob('产出_队3/装配_化学*.html') + glob.glob('产出_队1/装配_生物*.html')
                 + glob.glob('产出_队2/*重制件*.md') + glob.glob('产出_队1/[BB]*.md'))
    red, scanned, total_asserts = [], 0, 0
    for f in files:
        try: t = open(f, encoding='utf-8').read()
        except: continue
        if f.endswith('.html'):
            t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
            t = re.sub(r'<[^>]+>', '\n', t)
        t = re.sub(r'[ \t]+', ' ', t)
        asserts = extract_assertions(t)
        scanned += 1
        for a in asserts:
            total_asserts += 1
            # 剥markdown标记再验
            clean = a.replace('**','').replace('*','').replace('`','')
            # 按首个比较符切出可验子式
            for seg in re.split(r'[；;。|]', clean):
                seg = seg.strip()
                if re.search(r'[=<>≈]', seg) and not re.search(r'[\u4e00-\u9fff]{2,}', seg.split('=')[0] if '=' in seg else 'x'):
                    st, info = try_verify(seg)
                    if st == 'BAD':
                        red.append((f, seg[:120], info))
    print(f'扫描{scanned}件，断言{total_asserts}条，硬伤红件{len(red)}条')
    for f, a, info in red[:60]:
        print(f'  ✗[{info}] {f.split("/")[-1][:30]} :: {a}')

if __name__ == '__main__':
    main()
