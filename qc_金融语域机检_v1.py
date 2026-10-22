#!/usr/bin/env python3
"""金融语域黑名单机检 v1（队1贡献·全队复用）
用法: python3 qc_金融语域机检_v1.py <md文件或目录>...
规则:
  - 正文区扫描（自动剥离"附：自检记录"段——对照区引用原词是必要留痕，不算命中）
  - 黑名单=作业卡铁律2零容忍词表+扩展词（资产/存款/审计/财报/营销/并购/做市/敞口等）
  - 命中=❌需换血；全绿=✅
教训背景: 黄金样本⑯与队1首件均出现"自检声明零命中、实扫抓出残留"的旧语域惯性复发
  （⑯:快钱/存款/变现；队1⑥:硬通货/账本/营销话术）——自检声明必须有机检兜底。
"""
import glob, re, sys, os

黑名单 = ['票据','汇率','变现','造币','收购','存货','现金流','风控','押注','本金','结算','清算',
          '收支','开源','投资','回报率','负债','套利','通货','交易','筹码','对冲','做空','增持',
          '折现','套现','头寸','账本','复利','报表','货币','资产','存款','大额存单','净资产',
          '财务','审计','财报','营销','并购','做市','敞口','定存','货基','预算']

def scan(path):
    txt = open(path, encoding='utf-8').read()
    body = re.split(r'\n## 附[：:]', txt)[0]          # 剥离自检留痕区
    body = re.sub(r'^>.*换血声明.*$', '', body, flags=re.M)  # 剥离文件头换血声明行
    hits = []
    for w in 黑名单:
        if w in body:
            for ln in body.split('\n'):
                if w in ln:
                    hits.append((w, ln.strip()[:60]))
    return hits

if __name__ == '__main__':
    targets = []
    for a in sys.argv[1:]:
        if os.path.isdir(a):
            targets += sorted(glob.glob(os.path.join(a, '*.md')))
        else:
            targets.append(a)
    fail = 0
    for t in targets:
        hits = scan(t)
        name = os.path.basename(t)[:24]
        if hits:
            fail += 1
            print(f'❌{name}: {len(hits)}处')
            for w, ctx in hits[:8]:
                print(f'    [{w}] {ctx}')
        else:
            print(f'✅{name}: 正文零命中')
    print(f'\n=== {len(targets)}文件，{fail}个待修 ===')
    sys.exit(1 if fail else 0)
