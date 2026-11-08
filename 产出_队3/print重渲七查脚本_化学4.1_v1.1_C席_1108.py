# -*- coding: utf-8 -*-
# 并行搜索员C·队3席C线·化学4.1 v1.1修复重渲+print七查复验（承1108全检回执D1修复令）
# 同源重生成：weasyprint渲染print层 → 七查量化 → print工序语泄漏grep（D1硬闸复验）
import subprocess, json, os, sys, glob, tempfile
from PIL import Image
from weasyprint import HTML

SRC = "/home/z/my-project/team-inbox/产出_队3/首学版_化学4.1_原子结构与元素周期表_并行搜索员C_1108.html"
PDF = "/home/z/my-project/team-inbox/产出_队3/print渲染V2.2_化学4.1_原子结构与元素周期表.pdf"
OUTJ = "/home/z/my-project/agents/6a9cf5659142687cba2de6b9/print七查_化学4.1_v1.1修复_1108.json"
TERM = "原子结构与元素周期表"

HTML(filename=SRC).write_pdf(PDF)
print("render ok:", PDF)

info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
r = {}
for line in info.splitlines():
    if line.startswith("Pages"): r["pages"] = int(line.split(":")[1].strip())
    if line.startswith("Page size"): r["size_pts"] = line.split(":", 1)[1].strip()
txt = subprocess.run(["pdftotext", PDF, "-"], capture_output=True, text=True).stdout
r["text_chars"] = len(txt.replace("\n", "").replace(" ", ""))
r["term_hit"] = TERM in txt
r["extra_hit"] = "首学版" in txt
# D1硬闸：print学生面工序语泄漏七词grep（sympy/留痕/验点/随件/工序/自拟申报语/席）
leaks = {}
for w in ["sympy", "留痕", "验点", "随件", "附件2", "5/5过", "全检"]:
    leaks[w] = txt.count(w)
r["print_leaks"] = leaks
r["print_leak_total"] = sum(leaks.values())

with tempfile.TemporaryDirectory() as td:
    subprocess.run(["pdftoppm", "-gray", "-r", "50", PDF, os.path.join(td, "p")], check=True, timeout=600)
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
r["chk6_whitebg"] = r["deepbg_max"] <= 15.0
r["chk7_struct"] = r["chk1_pages_a4"] and r["chk2_text"]
r["chk8_print_leak"] = r["print_leak_total"] == 0
r["ALL"] = all(r[k] for k in ["chk1_pages_a4","chk2_text","chk3_dark","chk4_deep","chk5_edge","chk6_whitebg","chk7_struct","chk8_print_leak"])
with open(OUTJ, "w", encoding="utf-8") as f:
    json.dump(r, f, ensure_ascii=False, indent=1)
print(json.dumps({k: r[k] for k in ["pages","size_pts","text_chars","term_hit","extra_hit","dark_avg","deep_avg","edge_max","deepbg_max","print_leaks","print_leak_total","ALL"]}, ensure_ascii=False))
sys.exit(0 if r["ALL"] else 2)
