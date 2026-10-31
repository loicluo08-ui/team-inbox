#!/usr/bin/env python3
# p35_print.py · 物理3.5成稿print七查PDF生成+量化检查 · 队4席A线 2026-10-31
import sys, re, subprocess, os
from playwright.sync_api import sync_playwright

CHROME = "/home/z/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome"
SRC = "/home/z/my-project/agents/6a59c9165b94d92a3eab22fe/wt4_35_1031/产出_队4/首学版_物理3.5_共点力的平衡_并行搜索员A_1031.html"
OUT = "/home/z/my-project/agents/6a59c9165b94d92a3eab22fe/wt4_35_1031/产出_队4/首学版_物理3.5_共点力的平衡_并行搜索员A_1031_print.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    page = browser.new_page()
    page.goto(f"file://{SRC}", wait_until="networkidle")
    page.wait_for_timeout(1500)
    page.pdf(path=OUT, format="A4", margin={"top":"1cm","bottom":"1cm","left":"1cm","right":"1cm"}, print_background=True)
    browser.close()

d = open(OUT,"rb").read()
pages = len(re.findall(rb"/Type\s*/Page[^s]", d))
mb = sorted(set(re.findall(rb"/MediaBox\s*\[([^\]]+)\]", d)))
print(f"[七查·1页数] {pages} 页")
print(f"[七查·2纸型] MediaBox={mb}")
mb_ok = all(b"595" in x and b"842" in x for x in mb)
print(f"[七查·3A4吻合] {'PASS' if mb_ok else 'FAIL'}")
print(f"[七查·4体积] {len(d)/1048576:.2f} MB")
# 渲染逐页灰度量化
os.makedirs("/tmp/p35_pg", exist_ok=True)
subprocess.run(["pdftoppm","-r","60","-gray","-png",OUT,"/tmp/p35_pg/pg"],check=True)
import glob
import struct
try:
    from PIL import Image
    has_pil=True
except Exception:
    has_pil=False
if has_pil:
    files=sorted(glob.glob("/tmp/p35_pg/pg-*.png"))
    print(f"[七查·5渲染] {len(files)} 页位图渲染成功")
    worst_light=0; worst_dark=0; allp=[]
    for f in files:
        im=Image.open(f).convert("L")
        px=list(im.getdata()); n=len(px)
        light=sum(1 for v in px if v<128)/n*100
        dark=sum(1 for v in px if v<40)/n*100
        allp.append((os.path.basename(f),round(light,2),round(dark,2)))
        worst_light=max(worst_light,light); worst_dark=max(worst_dark,dark)
    print(f"[七查·6灰度量化] <128灰度占比范围 {min(x[1] for x in allp)}%–{worst_light}% · <40特深占比范围 {min(x[2] for x in allp)}%–{worst_dark}%")
    for name,l,dk in allp: print(f"    {name}: <128={l}% <40={dk}%")
    ok = worst_light<20 and worst_dark<8
    print(f"[七查·7显影安全] {'PASS' if ok else 'CHECK'}（阈值:全页<128≤20%·<40≤8%）")
else:
    print("[七查·6/7] PIL不可用·量化候补跑")
print("p35_print.py DONE")
