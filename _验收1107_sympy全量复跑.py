import glob, subprocess, os
os.chdir('/home/z/my-project/output/team-inbox')
scripts = sorted(set(glob.glob('产出_队*/**/*sympy*.py', recursive=True) + glob.glob('产出_队*/**/*验点*.py', recursive=True) + glob.glob('产出_队*/**/*复算*.py', recursive=True) + glob.glob('产出_队*/**/*验算*.py', recursive=True)))
ok, fail, err, to = [], [], [], []
for s in scripts:
    try:
        r = subprocess.run(['python3', s], capture_output=True, timeout=15)
        out = (r.stdout + r.stderr).decode('utf-8', 'ignore')
        if 'Traceback' in out: err.append(s)
        elif 'FAIL' in out.upper() or r.returncode != 0: fail.append(s)
        else: ok.append(s)
    except subprocess.TimeoutExpired:
        to.append(s)
with open('/tmp/sympy_result_1107.txt', 'w') as f:
    f.write(f'总={len(scripts)} PASS={len(ok)} FAIL={len(fail)} 异常={len(err)} 超时={len(to)}\n')
    for x in fail: f.write('FAIL: ' + x + '\n')
    for x in err: f.write('ERR: ' + x + '\n')
    for x in to: f.write('TIMEOUT: ' + x + '\n')
print('DONE')
