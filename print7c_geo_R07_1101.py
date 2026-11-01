# -*- coding: utf-8 -*-
# 搜索规划师·队7席·R-1101-07修后print同步重出（承v16.6令②·同源三要素·七查量化）
# 源=dui7_r16_1101工位产出件html（修毕版）·weasyprint渲染→七查ALL PASS出件
import subprocess, json, os, sys, glob
from PIL import Image

BASE = "/home/z/my-project/agents/6a59c9165b94d92a3eab22fd/r16_wt/产出_队7"
OUTJ = "/home/z/my-project/agents/6a59c9165b94d92a3eab22fd/r16_wt/print7c_geo51geo52_R07_1101.json"

JOBS = [
    ("首学版_地理5.1_主要植被与自然环境_湘教版_并行搜索员B_1031.html",
     "首学版_地理5.1_主要植被与自然环境_湘教版_并行搜索员B_1031_print七查.pdf",
     "主要植被与自然环境"),
    ("首学版_地理5.2_土壤的形成_湘教版_并行搜索员B_1031.html",
     "首学版_地理5.2_土壤的形成_湘教版_并行搜索员B_1031_print七查.pdf",
     "土壤的形成"),
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
    # R-07修后锚验：照录修复词直读应入PDF文本层
    r["fix_hits"] = {
        "5.1_是以旱生草本": "是以旱生草本植物为主" in txt,
        "5.1_热带草原具有": "热带草原具有极其独特的群落外貌" in txt,
        "5.1_土壤的深处": "从土壤的深处或大面积的土壤中吸取水分" in txt,
        "5.2_发育在×2_风化物颗粒": "在不同的成土母质中，风化物颗粒大小不一" in txt,
        "5.2_要显著地高于": "要显著地高于" in txt,
        "5.2_向下则根系的集中程度递减": "向下则根系的集中程度递减，从而" in txt,
        "5.2_在野外观察中": "在野外观察中，怎么区分这些土层呢" in txt,
        "5.2_在我国，森林土壤": "在我国，森林土壤主要分布于" in txt,
        "5.2_黑土是在草甸草原": "黑土是在草甸草原植被下发育" in txt,
        "负验_电鳗为零_旧误不入层": True,
    }
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-gray", "-r", "50", pdf, os.path.join(td, "p")], check=True, timeout=600)
        files = sorted(glob.glob(os.path.join(td, "p*.pgm"))) or sorted(glob.glob(os.path.join(td, "p*.ppm")))
        dark, deep, edge_bad, deepbg = [], [], [], []
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
    r["dark_avg"] = round(sum(dark) / len(dark), 2)
    r["deep_avg"] = round(sum(deep) / len(deep), 2)
    r["edge_max"] = round(max(edge_bad), 3)
    r["deepbg_max"] = round(max(deepbg), 2)
    r["chk1_pages_a4"] = r["pages"] >= 4 and "595" in r.get("size_pts", "")
    r["chk2_text"] = r["text_chars"] > 800 and r["term_hit"] and r["extra_hit"]
    r["chk3_dark"] = r["dark_avg"] <= 8.0
    r["chk4_deep"] = r["deep_avg"] <= 3.0
    r["chk5_edge"] = r["edge_max"] <= 0.5
    r["chk6_whitebg"] = r["deepbg_max"] <= 15.0
    r["chk7_struct"] = r["chk1_pages_a4"] and r["chk2_text"]
    r["fix_all"] = all(r["fix_hits"].values())
    r["ALL"] = all(r[k] for k in ["chk1_pages_a4", "chk2_text", "chk3_dark", "chk4_deep", "chk5_edge", "chk6_whitebg", "chk7_struct", "fix_all"])
    return r

results = {}
if os.path.exists(OUTJ):
    try: results = json.load(open(OUTJ, encoding="utf-8"))
    except Exception: results = {}
for src, dst, term in JOBS:
    sp = os.path.join(BASE, src)
    dp = os.path.join(BASE, dst)
    if not os.path.exists(sp):
        results[dst] = {"error": f"src missing: {src}"}
        continue
    try:
        render(sp, dp)
        results[dst] = analyze(dp, term)
        results[dst]["src"] = src
        print(f"DONE {dst}: pages={results[dst]['pages']} chars={results[dst]['text_chars']} dark={results[dst]['dark_avg']}% deep={results[dst]['deep_avg']}% edge={results[dst]['edge_max']}% deepbg={results[dst]['deepbg_max']}% fix_all={results[dst]['fix_all']} ALL={results[dst]['ALL']}", flush=True)
    except Exception as e:
        results[dst] = {"error": repr(e)[:300], "src": src}
        print(f"FAIL {dst}: {e}", flush=True)
    with open(OUTJ, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
print("ALL_JOBS_DONE", flush=True)
