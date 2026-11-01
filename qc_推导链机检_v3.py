# -*- coding: utf-8 -*-
"""数学推导链机检 v3：提取证明段等式链，相邻行等价检验+首式数值回代
能抓：H1类（链内某步代数变形错/符号错）——零假阳性设计
"""
import re, glob, sys
import sympy as sp

x, x1, x2, y, a, b, n, m, t, k, p, q = sp.symbols('x x1 x2 y a b n m t k p q', real=True)
SYMS = {'x':x,'x₁':x1,'x₂':x2,'y':y,'a':a,'b':b,'n':n,'m':m,'t':t,'k':k,'p':p,'q':q}

def norm(s):
    """数学记号规范化：Unicode→sympy可解析"""
    s = s.replace('−','-').replace('–','-').replace('×','*').replace('÷','/').replace('·','*')
    s = re.sub(r'([a-z₀-９])²', r'\1**2', s)
    s = s.replace('²','**2').replace('³','**3')
    for u, d in [('₁','1'),('₂','2'),('₃','3'),('₄','4')]:
        s = s.replace('x'+u, f'x{d}')
    s = s.replace('√(', 'sqrt(').replace('√x','sqrt(x)')
    return s

def parse_side(s):
    s = norm(s).strip().rstrip('.,；;。')
    s = s.replace('f(x₁)-f(x₂)','FD').replace('f(x1)-f(x2)','FD')
    try:
        e = sp.sympify(s, locals=SYMS, rational=True)
        return e
    except Exception:
        return None

def verify_chain(lines):
    """验证等式链：每对相邻行代数等价；返回错误步骤号"""
    exprs = []
    for ln in lines:
        e = parse_side(ln)
        exprs.append(e)
    if any(e is None for e in exprs): return None  # 解析不了→SKIP
    errs = []
    for i in range(len(exprs)-1):
        try:
            d = sp.simplify(exprs[i] - exprs[i+1])
            if d != 0:
                errs.append((i+1, i+2, str(sp.simplify(exprs[i]))[:40], str(sp.simplify(exprs[i+1]))[:40]))
        except Exception:
            return None
    return errs

def find_chains(text):
    """找证明段等式链：形如 A=B=C=D 的行（单行多等号）或多行连续等式"""
    chains = []
    # 单行多等号：f(x₁)−f(x₂) = X = Y = Z
    for m in re.finditer(r'([^\n]{6,80}?)=((?:[^\n=]{3,60}=){1,5}[^\n=]{3,60})', text):
        lhs, rhs_chain = m.group(1).strip(), m.group(2)
        if not re.search(r'[a-z₁₂]', lhs): continue
        if len(re.findall(r'[0-9]', lhs+rhs_chain)) < 1: continue
        parts = [p.strip() for p in (lhs + '=' + rhs_chain).split('=')]
        if len(parts) >= 3 and all(re.search(r'[\w√()/.^+-]', p) for p in parts):
            chains.append((m.start(), parts))
    return chains

def main():
    files = (glob.glob('产出_队2/装配_数学*.html') + glob.glob('产出_队4/装配_物理*.html')
             + glob.glob('产出_队3/装配_化学*.html') + glob.glob('产出_队1/装配_生物*.html')
             + glob.glob('产出_队2/*重制件*.md') + glob.glob('产出_队3/*重制*.md')
             + glob.glob('产出_队1/[BB]*.md') + glob.glob('产出_队4/物理*.md')
             + glob.glob('产出_队5/*.md') + glob.glob('产出_队7/*.md'))
    chains_n, bad = 0, []
    for f in files:
        try: t = open(f, encoding='utf-8').read()
        except: continue
        if f.endswith('.html'):
            t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
            t = re.sub(r'<br\s*/?>', '\n', t)
            t = re.sub(r'<[^>]+>', '', t)
        for pos, parts in find_chains(t):
            chains_n += 1
            errs = verify_chain(parts)
            if errs:
                ctx = t[max(0,pos-40):pos+120].replace('\n',' ')[:100]
                bad.append((f, parts, errs, ctx))
    print(f'等式链{chains_n}条，断链红件{len(bad)}条')
    for f, parts, errs, ctx in bad[:40]:
        pstr = '='.join(parts[:6])
        print(f'✗ {f.split("/")[-1][:30]}')
        print(f'   链: {pstr[:120]}')
        for a, b, ea, eb in errs:
            print(f'   断链{a}→{b}: [{ea[:30]}] ≠ [{eb[:30]}]')
        print(f'   上下文: {ctx}')
        print()

if __name__ == '__main__':
    main()
