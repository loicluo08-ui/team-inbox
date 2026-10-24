#!/usr/bin/env python3
# 装配净化器 v1（队4·B席·1024）——承16:07裁定②W2：入装v18挂接注/簇编制名/装配批注按S10 A2净化口径清除留痕
# 口径：canonical零触碰（本器在装配管线内对读入的md做净化转换）；清除留痕=逐规则命中计数输出，供工作单申报对账
# 对齐先例：地理装配13词面零命中（S10 A2"制作层词0在册"）+化学首件装配级净化（canonical不动·剔除799字节）
import re

RULES_REPORT = []  # (规则名, 命中数, 样例)

def _hit(name, n, samples):
    if n: RULES_REPORT.append((name, n, samples))

def purify_md(md):
    """md文本→净化后md。规则顺序敏感：挂接注删除→批注清除→簇编制名映射→栏目名同义替换→空括号清理"""
    R = []  # (规则名, 净化后文本, 命中数, 样例)

    # B1/B2/B3 装配批注"供装配层渲染真图"清除
    t, n = re.subn(r'（供装配层渲染真图）', '', md); _hit('B1批注整括号', n, [])
    t2, n2 = re.subn(r'，供装配层渲染真图', '', t); _hit('B2批注逗号段', n2, [])
    t3, n3 = re.subn(r'供装配层渲染真图', '', t2); _hit('B3批注兜底', n3, [])
    R.append(('B1-B3批注清除', t3, n + n2 + n3, []))

    # A1 v18挂接注整括号删除（含"源自v18"前缀形态）
    samples = re.findall(r'（(?:源自)?v18[^（）]{0,60}', t3)[:3]
    t4, n4 = re.subn(r'（(?:源自)?v18[^（）]*）', '', t3); _hit('A1挂接注括号', n4, samples)
    # A2 破折号后挂接段（括号内"——v18原话：…"形态）
    samples = re.findall(r'——v18[^）]{0,40}', t4)[:3]
    t5, n5 = re.subn(r'——v18[^）]*', '', t4); _hit('A2破折号挂接段', n5, samples)
    # A3 "·v18"结尾挂接（"（先做再看答案·v18）"）
    t6, n6 = re.subn(r'·v18(?=[）)])', '', t5); _hit('A3顿点v18', n6, [])
    R.append(('A1-A3挂接注删除', t6, n4 + n5 + n6, samples))

    # C7 裸簇⑦（本册无对应节·删编制名留概念名："簇⑤图像法与簇⑦配方在此会师"→"1.5图像法与配方在此会师"）
    t7, n7 = re.subn(r'簇⑦', '', t6); _hit('C7簇⑦删名', n7, [])
    # C8 回簇NN→回1.N节
    t8 = re.sub(r'回簇(0[1-9])', lambda m: f'回1.{m.group(1)[1]}节', t7)
    t8, n8b = re.subn(r'回簇([①②③④⑤⑥])', lambda m: f'回1.{"①②③④⑤⑥".index(m.group(1))+1}节', t8)
    _hit('C8回簇映射', n8b, [])
    # C9 簇编制名→节号映射（簇02→1.2…簇⑥→1.6）
    MAP = {'①': '1.1', '②': '1.2', '③': '1.3', '④': '1.4', '⑤': '1.5', '⑥': '1.6'}
    t9, n9 = re.subn(r'簇(?:0([1-9])|([①②③④⑤⑥]))', lambda m: f'1.{m.group(1) or ("①②③④⑤⑥".index(m.group(2))+1)}', t8)
    _hit('C9簇→节映射', n9, [])
    R.append(('C7-C9簇编制名净化', t9, n7 + n8b + n9, []))

    # D 栏目名/修辞同义替换（编制名"簇"→本册编制"节"）
    t10, n10 = re.subn(r'跨簇连接题', '跨节连接题', t9); _hit('D1跨簇→跨节', n10, [])
    t11, n11 = re.subn(r'本簇', '本节', t10); _hit('D2本簇→本节', n11, [])
    t12, n12 = re.subn(r'三簇联演', '三节联演', t11); _hit('D3三簇联演→三节联演', n12, [])
    R.append(('D栏目名同义替换', t12, n10 + n11 + n12, []))

    # E 空括号清理（净化删除后的残壳）
    t13, n13 = re.subn(r'（[ 　]*）', '', t12); _hit('E空括号清理', n13, [])
    R.append(('E空括号清理', t13, n13, []))
    return t13

def residual_report(text):
    """残留词面报告：返回{词: [(上下文,)]}，供人工复核兜底"""
    out = {}
    for w in ['v18', '簇', '供装配层渲染真图']:
        ctx = []
        for m in re.finditer(re.escape(w), text):
            s = max(0, m.start() - 16)
            ctx.append(text[s:m.end() + 22].replace('\n', ' '))
        out[w] = ctx
    return out

def verify_zero(text):
    """A4.3自检断言：词面全零返回(True,0)，否则返回(False,总数)"""
    return all(text.count(w) == 0 for w in ['v18', '簇', '供装配层渲染真图']), \
           sum(text.count(w) for w in ['v18', '簇', '供装配层渲染真图'])
