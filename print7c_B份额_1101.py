# -*- coding: utf-8 -*-
# 并行搜索员B·队1/3席·print七查收口13份（承群管理员00:39:07令②·v2.19分工）
# 同源重生成：以main正本html为源（原样不改动），weasyprint渲染print层 → 七查量化
import subprocess, json, os, sys, glob
from PIL import Image

BASE = "/home/z/my-project/agents/6a59c9165b94d92a3eab2300/wt_printB_1101"
OUTJ = "/home/z/my-project/agents/6a59c9165b94d92a3eab2300/print7c_B份额_1101.json"

# (目录, 源html, 输出pdf, 节名词)
JOBS = [
    ("产出_队3", "首学版_化学1.1_走进化学科学_C席_1031.html", "print七查_化学1.1_走进化学科学_首学版.pdf", "走进化学科学"),
    ("产出_队3", "首学版_化学1.2_研究物质性质的方法和程序_并行搜索员B_1031.html", "print七查_化学1.2_研究物质性质的方法和程序_首学版.pdf", "研究物质性质的方法和程序"),
    ("产出_队3", "首学版_化学1.2_研究物质性质的方法和程序_群外管理员席_1031.html", "print七查_化学1.2_研究物质性质的方法和程序_预览_群外版.pdf", "研究物质性质的方法和程序"),
    ("产出_队3", "首学版_化学1.3_化学中常用的物理量物质的量_并行搜索员C_1031.html", "print七查_化学1.3_化学中常用的物理量物质的量_首学版.pdf", "物质的量"),
    ("产出_队3", "首学版_化学2.1_元素与物质分类_C席_1031.html", "print七查_化学2.1_元素与物质分类_首学版.pdf", "元素与物质分类"),
    ("产出_队3", "首学版_化学2.2_电解质的电离离子反应_C席_1031.html", "print七查_化学2.2_电解质的电离离子反应_首学版.pdf", "电解质的电离"),
    ("产出_队1", "首学版_生物1.1_细胞是生命活动的基本单位_报告汇总员_1031.html", "print七查_生物1.1_细胞是生命活动的基本单位_首学版.pdf", "细胞是生命活动的基本单位"),
    ("产出_队1", "首学版_生物1.2_细胞的多样性和统一性_并行搜索员B_1031.html", "print七查_生物1.2_细胞的多样性和统一性_首学版.pdf", "细胞的多样性和统一性"),
    ("产出_队1", "首学版_生物1.2_细胞的多样性和统一性_群外管理员席_1031.html", "print七查_生物1.2_细胞的多样性和统一性_预览_群外版.pdf", "细胞的多样性和统一性"),
    ("产出_队1", "首学版_生物2.1_细胞中的元素和化合物_报告汇总员_1031.html", "print七查_生物2.1_细胞中的元素和化合物_首学版.pdf", "细胞中的元素和化合物"),
    ("产出_队1", "首学版_生物2.2_细胞中的无机物_报告汇总员_1031.html", "print七查_生物2.2_细胞中的无机物_首学版.pdf", "细胞中的无机物"),
    ("产出_队1", "首学版_生物2.3_细胞中的糖类和脂质_报告汇总员_1031.html", "print七查_生物2.3_细胞中的糖类和脂质_首学版.pdf", "细胞中的糖类和脂质"),
    ("产出_队1", "首学版_生物2.4_蛋白质是生命活动的主要承担者_报告汇总员_1031.html", "print七查_生物2.4_蛋白质是生命活动的主要承担者_首学版.pdf", "蛋白质是生命活动的主要承担者"),
]

def render(src, dst):
    from weasyprint import HTML
    HTML(filename=src).write_pdf(dst)

def analyze(pdf, term):
    r = {}
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    for ln in info.splitlines():
        if ln.startswith("Pages:"): r["pages"] = int(ln.split()[1])
        if ln.startswith("Page size:"):
            r["size_pts"] = ln.split(":")[1].strip().split(" pts")[0]
    txt = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    r["text_chars"] = len(txt.replace("\n", "").replace(" ", ""))
    r["term_hit"] = term in txt
    r["extra_hit"] = "首学版" in txt
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-gray", "-r", "50", pdf, os.path.join(td, "p")], check=True, timeout=600)
        files = sorted(glob.glob(os.path.join(td, "p*.pgm"))) or sorted(glob.glob(os.path.join(td, "p*.ppm")))
        dark, deep, edge_bad, deepbg, pages_n = [], [], [], [], []
        for f in files:
            im = Image.open(f).convert("L")
            w, h = im.size
            px = im.tobytes()
            n = len(px)
            dark.append(sum(1 for v in px if v < 128) / n * 100)
            deep.append(sum(1 for v in px if v < 40) / n * 100)
            deepbg.append(sum(1 for v in px if v < 200) / n * 100)
            band = 12
            e = 0
            idx = 0
            for y in range(h):
                for x in range(w):
                    if x < band or x >= w - band or y < band or y >= h - band:
                        if px[idx] < 250: e += 1
                    idx += 1
            edge_bad.append(e / (2 * band * (w + h) - 4 * band * band) * 100)
            pages_n.append(os.path.basename(f))
    r["dark_pct"] = [round(v, 2) for v in dark]
    r["deep_pct"] = [round(v, 2) for v in deep]
    r["dark_avg"] = round(sum(dark) / len(dark), 2)
    r["deep_avg"] = round(sum(deep) / len(deep), 2)
    r["edge_max"] = round(max(edge_bad), 3)
    r["deepbg_max"] = round(max(deepbg), 2)
    r["chk1_pages_a4"] = r["pages"] >= 4 and "595" in r.get("size_pts", "")
    r["chk2_text"] = r["text_chars"] > 800 and r["term_hit"] and r["extra_hit"]
    r["chk3_dark"] = r["dark_avg"] <= 8.0
    r["chk4_deep"] = r["deep_avg"] <= 3.0
    r["chk5_edge"] = r["edge_max"] <= 0.5
    r["chk6_whitebg"] = r["deepbg_max"] <= 15.0  # 浅底深字：无深色背景块
    r["chk7_struct"] = r["chk1_pages_a4"] and r["chk2_text"]
    r["ALL"] = all(r[k] for k in ["chk1_pages_a4", "chk2_text", "chk3_dark", "chk4_deep", "chk5_edge", "chk6_whitebg", "chk7_struct"])
    return r

results = {}
if os.path.exists(OUTJ):
    try: results = json.load(open(OUTJ, encoding="utf-8"))
    except Exception: results = {}
only = sys.argv[1] if len(sys.argv) > 1 else None
for d, src, dst, term in JOBS:
    if only and only not in src: continue
    if results.get(dst, {}).get("ALL"): continue
    sp = os.path.join(BASE, d, src)
    dp = os.path.join(BASE, d, dst)
    if not os.path.exists(sp):
        results[dst] = {"error": f"src missing: {src}"}
        continue
    try:
        render(sp, dp)
        results[dst] = analyze(dp, term)
        results[dst]["src"] = src
        print(f"DONE {dst}: pages={results[dst]['pages']} dark={results[dst]['dark_avg']}% deep={results[dst]['deep_avg']}% edge={results[dst]['edge_max']}% deepbg={results[dst]['deepbg_max']}% ALL={results[dst]['ALL']}", flush=True)
    except Exception as e:
        results[dst] = {"error": repr(e)[:300], "src": src}
        print(f"FAIL {dst}: {e}", flush=True)
    with open(OUTJ, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
print("ALL_JOBS_DONE", flush=True)
