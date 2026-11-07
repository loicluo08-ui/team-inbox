import glob, subprocess, os, re
os.chdir('/home/z/my-project/output/team-inbox')
scripts = sorted(set(glob.glob('产出_队*/**/*sympy*.py', recursive=True) + glob.glob('产出_队*/**/*验点*.py', recursive=True) + glob.glob('产出_队*/**/*复算*.py', recursive=True) + glob.glob('产出_队*/**/*验算*.py', recursive=True)))
ok, realfail, err, to = [], [], [], []
for s in scripts:
    try:
        r = subprocess.run(['python3', s], capture_output=True, timeout=15)
        out = (r.stdout + r.stderr).decode('utf-8', 'ignore')
        if 'Traceback' in out:
            err.append(s); continue
        # 提取 FAIL=N 汇总行
        m = re.findall(r'FAIL\s*=\s*(\d+)', out)
        n_fail = max(int(x) for x in m) if m else None
        bad = (r.returncode != 0) or (n_fail is not None and n_fail > 0) or re.search(r'FAIL\s*\|', out)
        if bad:
            realfail.append((s, r.returncode, n_fail))
        else:
            ok.append(s)
    except subprocess.TimeoutExpired:
        to.append(s)
with open('/tmp/sympy_result2_1107.txt', 'w') as f:
    f.write(f'总={len(scripts)} PASS={len(ok)} 真FAIL={len(realfail)} 异常={len(err)} 超时={len(to)}\n')
    for s, rc, nf in realfail:
        f.write(f'REAL_FAIL: {s} rc={rc} FAIL计数={nf}\n')
    for x in err: f.write('ERR: ' + x + '\n')
    for x in to: f.write('TIMEOUT: ' + x + '\n')
print('DONE')
