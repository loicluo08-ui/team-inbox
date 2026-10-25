#!/usr/bin/env python3
"""低耗快学机检 v1（低耗快学条款v2的机器化执行·队1贡献金融机检同构）
用法: python3 qc_低耗快学机检_v1.py <md文件或目录>...
判据（源自低耗快学条款v2）:
  A. 疲劳三件套检查（切片卡必查）: ①判定口令(≤20字·"口令"标记) ②荧光判据句(≤30字·mark/荧光标记)
     ③易错收口独立成块——缺一即❌
  B. 回指依赖黑名单: 如前所述/见上文/前文提到/前面说过/如前文——门槛低判据（块内自足）
  C. 无信息铺垫黑名单: 在学习本节之前/让我们先来/众所周知/值得一提的是/不妨先/相信大家
  D. 叙述层长句: 剥结构元素后>75字句≥3处→⚠️候人工定性（75=退回线，40=写作目标线）
  E. 装饰冗余: emoji/符号连排≥3
边界声明: 剥结构元素依赖人工维护清单（卡头/源注/申报表/照录注记），新形态出新结构时机检可能
  漏——故D类结果一律⚠️候人工定性，不自动退回；A/B/C/E类为机器硬判据。
"""
import glob, re, sys, os

回指黑名单 = ['如前所述', '见上文', '前文提到', '前面说过', '如前文', '上文提到']
铺垫黑名单 = ['在学习本节之前', '让我们先来', '众所周知', '值得一提的是', '不妨先', '相信大家', '接下来我们将']
装饰模式 = re.compile(r'[✅✨🌟🔥💡⚡⭐]{3,}|[—…]{4,}')

def strip_structure(txt):
    """剥结构元素：源注/出处/申报表/照录注记/导航行（人工维护清单·2025-10-25版）"""
    txt = re.sub(r'<style[^>]*>.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<script[^>]*>.*?</script>', ' ', txt, flags=re.S)
    lines = txt.split('\n')
    keep = []
    for ln in lines:
        s = ln.strip()
        if any(k in s for k in ['源：', '出处', 'sha256', '照录（', '登记', '申报', '留痕', 'manifest', '节名照录', '节名', '人教版', '鲁科版', '批2校准', '批3', '双段版', '切片卡 ·', '易错收口（', '锚点布局']):
            continue
        if s.count('｜') >= 2 or (s.count('·') >= 3 and len(s) < 80):
            continue
        if 'BV' in s or 'http' in s:
            continue
        keep.append(ln)
    return '\n'.join(keep)

def scan(path):
    txt = open(path, encoding='utf-8').read()
    is_card = os.path.basename(path).startswith('切片卡')
    body = strip_structure(txt)
    plain = re.sub(r'<[^>]+>', ' ', body)
    plain = re.sub(r'\s+', ' ', plain)
    hits = []
    # A. 疲劳三件套（仅切片卡）
    if is_card:
        has_kouling = bool(re.search(r'(判定)?口令[：:]?', plain)) or bool(re.search(r'纠偏动作|判定要点|判定动作', plain)) or bool(re.search(r'只翻|三步|三问|第一查|开关|三连问|两步走|口诀', plain))
        has_fluo = ('<mark' in txt) or ('荧光' in txt) or ('判据句' in plain) or bool(re.search(r'<(strong|b)[^>]*>[^<]{1,30}</(strong|b)>', txt)) or bool(re.search(r'\*\*[^*]{1,30}\*\*', txt))
        has_block = bool(re.search(r'易错收口|易错卡', plain))
        missing = [n for n, ok in [('判定口令', has_kouling), ('荧光判据句', has_fluo), ('易错收口块', has_block)] if not ok]
        if missing:
            hits.append(('疲劳三件套缺' + '/'.join(missing), '（切片卡必查·条款v2硬判据）'))
    # B. 回指依赖
    for w in 回指黑名单:
        if w in plain:
            hits.append((w, '回指依赖·破坏块自足'))
    # C. 无信息铺垫
    for w in 铺垫黑名单:
        if w in plain:
            hits.append((w, '无信息铺垫'))
    # D. 叙述层长句
    longs = [s for s in re.split(r'[。！？]', plain) if len(s.strip()) > 75 and 'BV' not in s and 'http' not in s]
    if len(longs) >= 3:
        hits.append((f'长句≥3处(实测{len(longs)})', longs[0][:60]))
    # E. 装饰冗余
    deco = 装饰模式.findall(plain)
    if deco:
        hits.append(('装饰冗余', str(deco[:2])))
    return hits

if __name__ == '__main__':
    targets = []
    for a in sys.argv[1:]:
        if os.path.isdir(a):
            targets += sorted(glob.glob(os.path.join(a, '*.html'))) + sorted(glob.glob(os.path.join(a, '*.md')))
        else:
            targets.append(a)
    fail = 0
    warn = 0
    for t in targets:
        hits = scan(t)
        name = os.path.basename(t)[:28]
        # 条款v2分级：硬判据（疲劳三件套/回指/铺垫/装饰）计fail；长句=D类⚠️候人工定性只warn
        hard = [h for h in hits if not str(h[0]).startswith('长句')]
        soft = [h for h in hits if str(h[0]).startswith('长句')]
        if hard:
            fail += 1
            print(f'❌{name}: {len(hard)}处')
            for w, ctx in hard[:6]:
                print(f'    [{w}] {ctx}')
        elif soft:
            warn += 1
            print(f'⚠️{name}: {len(soft)}处（长句候人工定性）')
            for w, ctx in soft[:3]:
                print(f'    [{w}] {ctx}')
        else:
            print(f'✅{name}: 四判据零命中')
    print(f'\n=== {len(targets)}文件，{fail}个待修，{warn}个候定性 ===')
    sys.exit(1 if fail else 0)
