#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""净面复跑器·S10全量74件（队6·报告汇总员·2025-10-25午）
授权链: 用户12:09:12令【管理员令·收线附加项】①③ + 管理员12:11:24队6块派单①②
  ①各队修复件随到随验（只动工序词断言+内容锚/引文零变更+幂等sha比对+出码留痕）
  ②预备统一词表版工具复跑方案（全量74件清单+复跑口径先备齐）
词表定版权: 候Alex《词表确权单》三选一（A4.3原文/CIWORDS字面/合并版）——本器将三候
  词表并列内置、scan默认info模式只并列计数不判定；确权落地后以 rerun --wordlist <版>
  出正式复跑码。本器不内嵌任何"定版"词表声明。
单一信源: S10结构/机检层直接import canonical批跑（队7驻留版=
  产出_队7/全册总验预研_C席_1024/全册总验_S10全表批跑.py·对齐qc_v1.1·§九3裁定+队7-B替换），
  机检词表随qc_金融语域机检_v1.py自动继承，本器零复制零旁挂。
铁律: 只读扫描零触碰正件（verify-commit --script 的幂等复跑除外，且带快照回滚保护）。
用法:
  python3 复跑器_S10全量74件_队6.py baseline                       # 出74件清单+sha256基线
  python3 复跑器_S10全量74件_队6.py scan [--scope core74|wide|both] [--out LOG]
  python3 复跑器_S10全量74件_队6.py rerun --wordlist a43|ciwords|merged [--out LOG]
  python3 复跑器_S10全量74件_队6.py verify-commit <sha> [--script PATH] [--out LOG]
退出码: 0=所跑检查全绿 / 2=有命中或候定版（info非失败语义）/ 3=内容锚保真FAIL / 4=幂等FAIL
"""
import io, os, re, sys, glob, hashlib, subprocess, importlib.util, datetime
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 仓库根
SELFDIR = os.path.dirname(os.path.abspath(__file__))
LIST_TXT = os.path.join(SELFDIR, '复跑74件清单.txt')

# ---- 词表（定版 2026-10-25 12:20=《词表确权单》4af2509§三：A4.3原文钉死） ----
# 钉死实现=20字面项（队N通配按字面展开队1~队7+队N，禁正则变体）；命中判据=子串包含(w in s)全文生效
# 词面出处: 标准库/S10_装配QC检查单.md L22 "13词面grep=0（队N/首件/claim/commit/待核/帧验/底本/席/canonical/连跑/升格/工作单/实切包）"
A43_LIT = ['队1', '队2', '队3', '队4', '队5', '队6', '队7', '队N',
           '首件', 'claim', 'commit', '待核', '帧验', '底本', '席',
           'canonical', '连跑', '升格', '工作单', '实切包']
A43_REG = []  # 确权单钉死：不得改用正则变体（历史稿曾用r'队[0-9]'，已按4af2509§三废弃）
# CIWORDS字面: canonical批跑脚本头 CIWORDS 原样
CIWORDS_LIT = ['队7', '首件', 'claim', 'commit', '待核', '帧验', '底本', '席', 'canonical', '连跑', '升格', '认领', '装配件']
CIWORDS_REG = []
# 合并版: A4.3∪CIWORDS 并集（去重）
MERGED_LIT = ['首件', 'claim', 'commit', '待核', '帧验', '底本', '席', 'canonical', '连跑', '升格', '工作单', '实切包', '认领', '装配件']
MERGED_REG = [r'队[0-9]']
WORDLISTS = {'a43': (A43_LIT, A43_REG), 'ciwords': (CIWORDS_LIT, CIWORDS_REG), 'merged': (MERGED_LIT, MERGED_REG)}
WORDLISTS_SNAP = dict(WORDLISTS)

# ---- 内容锚正则（随到随验·保真断言对象；锚集合新旧逐字节多集相等） ----
ANCHOR_RES = [
    ('源注', r'〔源：[^〕]*〕'),
    ('href', r'href="[^"]*"|href=\'[^\']*\''),
    ('BV', r'BV[0-9A-Za-z]{10}'),
    ('sid', r'sid\D{0,3}\d+'),
    ('t参数', r'(?<![A-Za-z0-9])t=\d+'),
]

def core74_list():
    """74件=切片卡34+装配件40（装配预备×4与其他13件html不在口径·论证见方案md§2）。"""
    if os.path.isfile(LIST_TXT):
        return [l.strip() for l in io.open(LIST_TXT, encoding='utf-8') if l.strip()]
    cards = sorted(glob.glob(os.path.join(ROOT, '产出_队*', '切片卡*.html')))
    assems = sorted(f for f in glob.glob(os.path.join(ROOT, '产出_队*', '装配*.html'))
                    if not os.path.basename(f).startswith('装配预备'))
    return sorted(cards + assems)

def wide_scope():
    extra = []
    extra += glob.glob(os.path.join(ROOT, '产出_队*', '*.md'))
    extra += glob.glob(os.path.join(ROOT, 'claim_队*.md'))
    extra += glob.glob(os.path.join(ROOT, '产出_队*', '装配预备*.html'))
    extra += glob.glob(os.path.join(ROOT, '产出_队*', '*实切包*.html'))
    extra += glob.glob(os.path.join(ROOT, '产出_队*', '正件_地理*.html'))
    extra += glob.glob(os.path.join(ROOT, 'v18原册_*.html'))
    return sorted(set(extra) - set(core74_list()))

def word_hits(text, lit, reg):
    c = Counter()
    for w in lit:
        n = text.count(w)
        if n:
            c[w] += n
    for rp in reg:
        n = len(re.findall(rp, text))
        if n:
            c['<' + rp + '>'] += n
    return c

def load_s10():
    # 信源优先级：统一词表版A43工具（确权单§三最小diff件·队6复跑执行件）＞canonical驻留件
    cands = [
        os.path.join(ROOT, '产出_队6', '全册总验_S10全表批跑_统一词表版A43_队6_1025.py'),
        os.path.join(ROOT, '产出_队7', '全册总验预研_C席_1024', '全册总验_S10全表批跑.py'),
    ]
    cand = next((p for p in cands if os.path.isfile(p)), None)
    if not cand:
        sys.exit('[复跑器]致命: S10批跑工具不在位: ' + ' | '.join(cands))
    spec = importlib.util.spec_from_file_location('s10batch', cand)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m, cand

def git(*a):
    # 字节级捕获再replace解码：兼容 git show 二进制件（PDF等）不炸会话
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True).stdout.decode('utf-8', 'replace')

def head_sha():
    return subprocess.run(['git', '-C', ROOT, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()

def now():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def emit(out, line):
    print(line)
    if out:
        out.write(line + '\n'); out.flush()

# ---------------- baseline ----------------
def do_baseline(out):
    files = core74_list()
    with io.open(LIST_TXT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(files) + '\n')
    sha_txt = os.path.join(SELFDIR, '基线sha256_74件_1025午.txt')
    with io.open(sha_txt, 'w', encoding='utf-8') as f:
        f.write('# 74件复跑前基线·HEAD=%s·时点=%s·sha256全64位\n' % (head_sha(), now()))
        for p in files:
            rel = os.path.relpath(p, ROOT)
            f.write('%s  %s\n' % (hashlib.sha256(io.open(p, 'rb').read()).hexdigest(), rel))
    emit(out, '[baseline] 清单=%s（%d件） sha256基线=%s HEAD=%s' % (
        os.path.relpath(LIST_TXT, ROOT), len(files), os.path.relpath(sha_txt, ROOT), head_sha()))
    return 0

# ---------------- scan / rerun ----------------
def scan_files(files, out, with_s10=True):
    s10 = None
    if with_s10:
        s10, s10path = load_s10()
        emit(out, '[信源] S10canonical=%s' % os.path.relpath(s10path, ROOT))
    totals = {k: Counter() for k in WORDLISTS}
    hitfiles = {k: 0 for k in WORDLISTS}
    s10_hard = 0
    for p in files:
        rel = os.path.relpath(p, ROOT)
        try:
            txt = io.open(p, encoding='utf-8').read()
        except Exception as e:
            emit(out, 'ERR\t%s\t%s' % (rel, e)); continue
        for k, (lit, reg) in WORDLISTS.items():
            c = word_hits(txt, lit, reg)
            if c:
                totals[k] += c; hitfiles[k] += 1
                emit(out, 'HITS\t%s\t%s\t%s' % (k, rel, ','.join('%s=%d' % (w, n) for w, n in sorted(c.items()))))
        if s10 is not None:
            hard, r = s10.audit(p, False)
            emit(out, 'S10\t%s\thard=%d\t%s' % (rel, hard, ' | '.join(x for x in r if ('🄱' not in x and 'glow' not in x))))
            if hard:
                s10_hard += 1
    wl_names = {'a43': 'A43', 'ciwords': 'CIWORDS', 'merged': 'MERGED'}
    emit(out, 'SUMMARY\tfiles=%d\tS10hard=%d\t%s' % (
        len(files), s10_hard,
        ' '.join('%s=%d' % (wl_names[k], hitfiles[k]) for k in WORDLISTS)))
    for k in WORDLISTS:
        emit(out, 'SUMMARY-WORDS\t%s\t%s' % (k, ','.join('%s=%d' % (w, n) for w, n in sorted(totals[k].items())) or 'ALL-ZERO'))

def do_scan(args, out):
    scope = 'both'
    if '--scope' in args:
        scope = args[args.index('--scope') + 1]
    core = core74_list(); wide = wide_scope()
    if scope in ('core74', 'both'):
        emit(out, '== SCOPE core74（复跑口径·%d件） HEAD=%s 时点=%s ==' % (len(core), head_sha(), now()))
        scan_files(core, out)
    if scope in ('wide', 'both'):
        emit(out, '== SCOPE wide（残差候选池预扫·%d件·仅供"其他归口"登记对表·非判定口径） ==' % len(wide))
        scan_files(wide, out, with_s10=False)
    emit(out, '[注] 词表模式=info三候并列·候《词表确权单》定版；判读层豁免家族（席词边界等）见豁免登记总账，本层只报原始计数。')
    return 0

def do_rerun(args, out):
    wl = 'merged'
    if '--wordlist' in args:
        wl = args[args.index('--wordlist') + 1]
    if wl not in WORDLISTS_SNAP:
        sys.exit('[复跑器]致命: 词表版未知: ' + wl)
    WORDLISTS.clear(); WORDLISTS.update({wl: WORDLISTS_SNAP[wl]})
    core = core74_list()
    emit(out, '== RERUN 词表版=%s（确权定版后正式复跑） 74件=%d HEAD=%s 时点=%s ==' % (wl, len(core), head_sha(), now()))
    scan_files(core, out)
    return 2  # 判读由调用方按SUMMARY行定，2=候判语义

# ---------------- verify-commit ----------------
def anchors(text):
    c = Counter()
    for name, rp in ANCHOR_RES:
        for m in re.findall(rp, text):
            c[(name, m)] += 1
    return c

def do_verify(args, out):
    if not args or args[0].startswith('--'):
        sys.exit('[复跑器]用法: verify-commit <sha> [--script PATH]')
    csha = args[0]
    files = [l for l in git('show', '--name-only', '--pretty=format:', csha).splitlines() if l.strip()]
    script = None
    if '--script' in args:
        script = args[args.index('--script') + 1]
    emit(out, '== VERIFY-COMMIT %s HEAD=%s 时点=%s 改动件=%d ==' % (csha[:12], head_sha(), now(), len(files)))
    verdict = 'PASS'
    for rel in files:
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            emit(out, 'SKIP(删除件)\t%s' % rel); continue
        old = git('show', '%s^:%s' % (csha, rel))
        new = io.open(p, encoding='utf-8', errors='replace').read()
        if not old:
            emit(out, 'SKIP(新文件)\t%s' % rel); continue
        if rel.lower().endswith('.pdf'):
            # 二进制重出品：文本锚断言不适用（pdftotext层候选Alex复验清单另核），blob-sha1对留痕
            ob = git('rev-parse', '%s^:%s' % (csha, rel)).strip()
            nb = git('hash-object', p).strip()
            emit(out, 'SKIP(二进制)\t%s\toldblob=%s newblob=%s（PDF重出件·blob sha1留痕）' % (rel, ob[:16], nb[:16]))
            continue
        mgmt = ('claim_队' in rel or rel.startswith('产出_队') and '工作单' in os.path.basename(rel)) or rel.endswith('.md')
        ao, an = anchors(old), anchors(new)
        d_only, a_new = ao - an, an - ao
        if d_only or a_new:
            verdict = 'FAIL-锚漂移'
            emit(out, 'FAIL-锚漂移\t%s\t消失=%s 新增=%s' % (rel,
                 [f'{k[0]}:{k[1][:40]}×{v}' for k, v in list(d_only.items())[:6]],
                 [f'{k[0]}:{k[1][:40]}×{v}' for k, v in list(a_new.items())[:6]]))
        d = git('diff', '-U0', '%s^' % csha, csha, '--', rel)
        bad_del, bad_add = [], []
        for ln in d.splitlines():
            if ln.startswith('---') or ln.startswith('+++'): continue
            body = ln[1:]
            has_word = any(w in body for w in A43_LIT) or any(re.search(rp, body) for rp in A43_REG)
            if ln.startswith('-') and not has_word: bad_del.append(body.strip()[:60])
            if ln.startswith('+') and has_word: bad_add.append(body.strip()[:60])
        if bad_del or bad_add:
            if mgmt:
                emit(out, 'NOTE-管理层文件\t%s\t增删行含工序词系申报语（不计射程外）' % rel)
            else:
                if verdict == 'PASS': verdict = 'FAIL-射程外'
                emit(out, 'FAIL-射程外\t%s\t删行无工序词=%s 增行仍含工序词=%s' % (rel, bad_del[:3], bad_add[:3]))
        co, cn = word_hits(old, A43_LIT, A43_REG), word_hits(new, A43_LIT, A43_REG)
        delta = {w: cn.get(w, 0) - co.get(w, 0) for w in set(co) | set(cn) if cn.get(w, 0) != co.get(w, 0)}
        emit(out, 'WORDS-DELTA\t%s\t%s' % (rel, delta or '∅(0)'))
        emit(out, 'SHA\t%s\told=%s new=%s' % (rel, hashlib.sha256(old.encode()).hexdigest()[:16], hashlib.sha256(io.open(p, 'rb').read()).hexdigest()[:16]))
    # 幂等复跑（--script）：快照→跑两轮→比对→回滚保护
    if script:
        emit(out, '-- 幂等复跑: %s --' % script)
        for rel in files:
            p = os.path.join(ROOT, rel)
            if not os.path.isfile(p): continue
            snap0 = io.open(p, 'rb').read()
            r1 = subprocess.run(['python3', script], cwd=ROOT, capture_output=True, text=True)
            s1 = io.open(p, 'rb').read()
            r2 = subprocess.run(['python3', script], cwd=ROOT, capture_output=True, text=True)
            s2 = io.open(p, 'rb').read()
            if not (snap0 == s1 == s2):
                if verdict == 'PASS': verdict = 'FAIL-幂等'
                io.open(p, 'wb').write(snap0)  # 回滚保护
                emit(out, 'FAIL-幂等\t%s\trun1Δ=%s run2Δ=%s（已回滚快照）' % (rel, snap0 != s1, s1 != s2))
            else:
                emit(out, 'IDEMPOTENT-OK\t%s\t复跑两轮sha零变化' % rel)
            if r1.returncode != 0:
                emit(out, 'WARN-script-exit\t%s\t%s' % (rel, r1.returncode))
    emit(out, 'VERDICT\t%s\tcommit=%s' % (verdict, csha[:12]))
    return 0 if verdict == 'PASS' else (3 if ('锚' in verdict or '射程' in verdict) else 4)

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    outpath = None
    if '--out' in rest:
        outpath = rest[rest.index('--out') + 1]
    out = io.open(outpath, 'w', encoding='utf-8') if outpath else None
    try:
        if cmd == 'baseline': rc = do_baseline(out)
        elif cmd == 'scan': rc = do_scan(rest, out)
        elif cmd == 'rerun': rc = do_rerun(rest, out)
        elif cmd == 'verify-commit': rc = do_verify(rest, out)
        else: sys.exit('未知子命令: ' + cmd)
    finally:
        if out: out.close()
    sys.exit(rc)

if __name__ == '__main__':
    main()
