#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全册总验·S10全表批跑（对齐qc_v1.1版·拓跋·队6）
授权: 任务包_必修一收官批_1024晚§二-B工具债单 + 管理员20:45:44直派（承办：队6拓跋）
修法（按派单执行）: 机检子模块不再自持任何词表——直接import根目录qc_金融语域机检_v1.py
  的scan函数作单一信源（黑名单/白名单/自检区剥离规则全部随源），弃subprocess+stdout
  字符串判读与一切内嵌/旁挂词表形态。qc_v1.1本体零触碰（其白名单增补纪律=须经汇总员
  裁定后入列，本席不越权）。
白名单机制同步: 经import自动继承qc_v1.1白名单（敞口瓶/稳定存在）整词占位机制。
批跑级白名单豁免（1项·留痕）:
  '一套现成' —— 地理2.1装配件「闽西的汀江就是一套现成的活教材」中"套现"系跨词假阳性。
    留痕=任务包§一队7行(19:1x轮实跑qc_v1.1复核定性)+C席预跑报告豁免备案同例
    (claim_队7 L180"一套现成/缺席")+任务包§二-B验收条款(2.1「套现」经白名单级豁免逻辑
    处理)。实现与qc_v1.1白名单同机制（整词占位'◇'后过scan），仅作用于本批跑机检层，
    不改内容、不改qc_v1.1词表；若汇总员后续裁定将该词升入qc_v1.1白名单本体，本条可退役。
验收（管理员条款）: 修后S10重跑地理2.1/2.2/3.2/3.3四件机检应全零命中——实测正件+装配件
  八件全零（唯一delta=装配2.1套现⚠️→✅），回归三关+豁免双测过，详见
  产出_队6/验收记录_S10对齐qc_v1.1_拓跋_1024.md。
canonical确权: 原脚本系C席canonical（产出_队7/全册总验预研_C席_1024/全册总验_S10全表
  批跑.py），本席未动其一字节；本对齐版暂驻产出_队6/，canonical替换候Alex确权并留痕。
  队7-B分工申报（claim_队7 L195⑤"候C席/队6表态"）以本交付为队6表态件，勿重复开工。
用法: python3 全册总验_S10全表批跑_对齐qc_v1.1_拓跋.py <a.html> [b.html ...] [--skip-machine]
（A2词面/B组结构/D组标签逻辑与C席版逐字节同源，仅机检子模块按派单改造）"""
import io, importlib.util, os, re, sys, tempfile

CIWORDS = ['队7', '首件', 'claim', 'commit', '待核', '帧验', '底本', '席', 'canonical', '连跑', '升格', '认领', '装配件']
STATEWORDS = ['候补', '补装', '候装', '待装', '候裁', '占位', '骨架']

# ---- 机检单一信源装载（向上探测，位置无关；找不到即致命退出，宁停不代） ----
def _locate_qc_module():
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        cand = os.path.join(d, 'qc_金融语域机检_v1.py')
        if os.path.isfile(cand):
            return cand
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    sys.exit('[S10对齐版]致命: 向上找不到qc_金融语域机检_v1.py——机检单一信源缺失，'
             '宁停不代（严禁内嵌词表回潮）')

_QC_PATH = _locate_qc_module()
try:
    _spec = importlib.util.spec_from_file_location('qc_finance_v11', _QC_PATH)
    _QC = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_QC)
except Exception as e:
    sys.exit(f'[S10对齐版]致命: qc_v1.1模块装载失败({e})——拒绝以本地词表替代')
if not hasattr(_QC, 'scan'):
    sys.exit('[S10对齐版]致命: qc_v1.1无scan函数——接口漂移，候人工对齐，宁停不代')

_BL = getattr(_QC, '黑名单', [])
_WL = getattr(_QC, '白名单', [])

# ---- 批跑级白名单豁免（整词占位·与qc_v1.1同机制·留痕见脚本头） ----
EXEMPT_WORDS = ['一套现成']

def machine_scan(path):
    """机检=qc_v1.1 scan单一信源。批跑级豁免词先整词占位'◇'再过scan（临时掩蔽件，
    不触原文件）；掩蔽只删命中不造命中。返回[(词, 上下文)]。"""
    txt = io.open(path, encoding='utf-8').read()
    masked = txt
    for w in EXEMPT_WORDS:
        masked = masked.replace(w, '◇')
    if masked == txt:
        return list(_QC.scan(path))
    tmp = tempfile.NamedTemporaryFile('w', encoding='utf-8', suffix='.html', delete=False)
    tmp.write(masked)
    tmp.close()
    try:
        return list(_QC.scan(tmp.name))
    finally:
        os.unlink(tmp.name)

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
        hits = machine_scan(path)
        if hits:
            r.append(f'🄰3机检⚠️待修{len(hits)}处')
            for w, ctx in hits[:8]:
                r.append(f'    [{w}] {ctx}')
            hard += 1
        else:
            r.append('🄰3机检✅')
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
    print(f'[机检信源] qc_v1.1单一import <{_QC_PATH}>')
    print(f'[词表现状] 黑名单{len(_BL)}·白名单{len(_WL)}:{"/".join(_WL) if _WL else "无"}'
          f'·批跑级豁免{len(EXEMPT_WORDS)}:{"、".join(EXEMPT_WORDS)}(留痕见脚本头)')
    nfail = 0
    for f in files:
        hard, r = audit(f, skip)
        nfail += hard
        print(f"[硬伤{hard}] {os.path.basename(f)}")
        for x in r: print('   ', x)
    print(f'---\nS10批跑(对齐qc_v1.1): {len(files)}件·硬伤{nfail}（软项数据行供启用时判读）')
    sys.exit(1 if nfail else 0)
