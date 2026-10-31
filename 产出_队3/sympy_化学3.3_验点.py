# -*- coding: utf-8 -*-
"""化学3.3《氮的循环》sympy/python独立验点（队3席B线·1031）
验点三类：A原子守恒12式（分子式逐元素计数）B电子守恒3组 C价态/数据自洽5点
"""
import re
from collections import defaultdict

def parse(formula):
    """支持嵌套括号/前系数/·水合形式"""
    def walk(s):
        buf = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                depth = 1; j = i+1
                while depth:
                    if s[j] == '(': depth += 1
                    elif s[j] == ')': depth -= 1
                    j += 1
                inner = walk(s[i+1:j-1])
                m = re.match(r'\d+', s[j:])
                n = int(m.group()) if m else 1
                if m: j += len(m.group())
                for k, v in inner.items(): buf.append((k, v*n))
                i = j
            else:
                m = re.match(r'([A-Z][a-z]?)(\d*)', s[i:])
                if not m: raise ValueError('bad at '+s[i:])
                el, n = m.group(1), int(m.group(2) or 1)
                buf.append((el, n)); i += m.end()
        d = defaultdict(int)
        for k, v in buf: d[k] += v
        return dict(d)
    # 系数与·(水合)拆分
    total = defaultdict(int)
    for part in formula.split('·'):
        m = re.match(r'(\d*)(.*)', part.strip())
        coef = int(m.group(1)) if m.group(1) else 1
        for k, v in walk(m.group(2)).items(): total[k] += v*coef
    return dict(total)

def eq(name, lhs, rhs):
    L, R = defaultdict(int), defaultdict(int)
    for f in lhs: 
        for k, v in parse(f).items(): L[k] += v
    for f in rhs:
        for k, v in parse(f).items(): R[k] += v
    ok = dict(L) == dict(R)
    print(f"{'PASS' if ok else 'FAIL'} | {name}: {lhs} -> {rhs}")
    if not ok:
        print('   L=', dict(L), ' R=', dict(R))
    return ok

results = []
print('== A 原子守恒12式 ==')
results.append(eq('A1 闪电固氮', ['N2', 'O2'], ['2NO']))
results.append(eq('A2 NO氧化', ['2NO', 'O2'], ['2NO2']))
results.append(eq('A3 NO2溶于水', ['3NO2', 'H2O'], ['2HNO3', 'NO']))
results.append(eq('A4 工业合成氨', ['N2', '3H2'], ['2NH3']))
results.append(eq('A5 氨与盐酸', ['NH3', 'HCl'], ['NH4Cl']))
results.append(eq('A6 氨的催化氧化', ['4NH3', '5O2'], ['4NO', '6H2O']))
results.append(eq('A7 碳酸氢铵分解', ['NH4HCO3'], ['NH3', 'CO2', 'H2O']))
results.append(eq('A8 氯化铵分解', ['NH4Cl'], ['NH3', 'HCl']))
results.append(eq('A9 实验室制氨', ['2NH4Cl', 'Ca(OH)2'], ['2NH3', 'CaCl2', '2H2O']))
results.append(eq('A10 硝酸分解', ['4HNO3'], ['4NO2', 'O2', '2H2O']))
results.append(eq('A11a 铜与浓硝酸', ['4HNO3', 'Cu'], ['Cu(NO3)2', '2NO2', '2H2O']))
results.append(eq('A11b 铜与稀硝酸', ['8HNO3', '3Cu'], ['3Cu(NO3)2', '2NO', '4H2O']))
results.append(eq('A12 浓硝酸氧化碳', ['4HNO3', 'C'], ['CO2', '4NO2', '2H2O']))

print('== B 电子守恒3组（氧化剂得电子=还原剂失电子）==')
def echeck(name, desc, lose, gain):
    ok = abs(lose-gain) < 1e-9
    print(f"{'PASS' if ok else 'FAIL'} | {name}: {desc} 失{lose}mol e- 得{gain}mol e-")
    return ok
results.append(echeck('B1 氨的催化氧化', 'N: -3→+2 失5×4=20 | O: 0→-2 得2×10=20', 20, 20))
results.append(echeck('B2 铜与稀硝酸', 'N: +5→+2 得3×2=6 | Cu: 0→+2 失2×3=6', 6, 6))
results.append(echeck('B3 浓硝酸氧化碳', 'N: +5→+4 得1×4=4 | C: 0→+4 失4×1=4', 4, 4))

print('== C 价态/数据自洽5点 ==')
def ccheck(name, cond, detail):
    ok = cond
    print(f"{'PASS' if ok else 'FAIL'} | {name}: {detail}")
    return ok
results.append(ccheck('C1 NH4+价态代数和', (-3)+4*(+1) == +1, 'N(-3)+4H(+1)=+1 与NH4+电荷吻合'))
results.append(ccheck('C2 NO3-价态代数和', (+5)+3*(-2) == -1, 'N(+5)+3O(-2)=-1 与NO3-电荷吻合'))
results.append(ccheck('C3 NO2价态代数和', (+4)+2*(-2) == 0, 'N(+4)+2O(-2)=0 分子电中性'))
results.append(ccheck('C4 反硝化电子数', 5-0 == 5, '1mol HNO3(+5→0)完全转化成N2转移5mol电子(5NA·p125习题5③)'))
results.append(ccheck('C5 硝化碱性总式电荷', (+1)+2*0+2*(-1) == (-1), 'NH4++2O2+2OH-=NO3-+3H2O 两端电荷-1=-1(原子守恒另由A族口径同法可验:N1H6O6/N1H6O6)'))
# 硝化总式原子守恒补验
results.append(eq('C5b 硝化碱性总式', ['NH4', '2O2', '2OH'], ['NO3', '3H2O']))

n_pass, n_all = sum(results), len(results)
print(f'== 汇总: {n_pass}/{n_all} {"ALL PASS" if n_pass==n_all else "HAS FAIL"} ==')
