#!/usr/bin/env python3
"""装配册渲染·元层页拼接线 v1（10/27拆分配套）
用法: python3 渲染_装配册_元层拼接.py <装配html> <输出pdf>
机制: 装配html内的 <!--META_INCLUDE:产出_元层页/元层页_X.html--> 占位
      替换为对应独立元层页文件内容→临时html→打印线标准渲染。
所有权: 元层页文件=产出_元层页/（主session独占）；装配html节内容=各队。
"""
import sys, os, re, subprocess, tempfile
SRC, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(HERE, SRC) if not os.path.isabs(SRC) else SRC, encoding='utf-8').read()
inc = re.findall(r'<!--META_INCLUDE:([^>]+)-->', t)
if not inc:
    print('无META_INCLUDE占位——按原样渲染'); tmp = SRC
else:
    for rel in inc:
        p = os.path.join(HERE, rel) if not os.path.isabs(rel) else rel
        assert os.path.exists(p), f'元层页文件缺失: {rel}'
        t = t.replace(f'<!--META_INCLUDE:{rel}-->', open(p, encoding='utf-8').read(), 1)
    fd, tmp = tempfile.mkstemp(suffix='.html', dir='/tmp'); os.close(fd)
    open(tmp, 'w', encoding='utf-8').write(t)
r = subprocess.run(['python3', '/home/z/my-project/tools/打印线_实切包HTML转PDF.py', tmp, OUT], capture_output=True, text=True)
print(r.stdout.strip()[-60:] or r.stderr.strip()[-60:])
sys.exit(r.returncode)
