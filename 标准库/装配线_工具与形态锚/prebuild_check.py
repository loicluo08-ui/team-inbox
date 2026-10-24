#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prebuild_check.py — build前源完整性闸门（学习资料线·防静默丢册）

失效模式背书（两次静默丢册实锤+第三次预演）：
  A. v19 build丢失v18"数学讲法锚点总槽"整块（总槽是v14直改HTML存量，源md无此块，build重建即丢）
  B. 化学源md残缺差点覆盖硫氮全量装配（9/30排雷：缺簇20字段区/两章路由/尾部簇12-13区）
  C. 10/22实测：总槽4条中2条（簇②映射方向性/簇⑥三元大招）只在成品HTML、源md缺失——下次build必再丢

四项检查：
  1 装配块对账：成品HTML每个讲法锚点卡的时间段特征串，必须在源md中定位得到（找不到=FAIL→回源或登记豁免）
  2 簇块对账：源md簇块集 vs 成品簇section集，双向差集（源缺=丢块；成品缺=装配漏）
  3 化学尾部区断言：簇12/簇13标记+三章路由在化学单册_源.md存在性（固定断言防复发）
  4 行数漂移：源md行数 vs 上次登记（prebuild_state.json），骤降>20%告警

用法：
  python3 tools/prebuild_check.py            # 全科检查
  python3 tools/prebuild_check.py 数学        # 单科
  python3 tools/prebuild_check.py --register  # 检查通过后登记状态（漂移基线更新）
"""
import re, sys, json, glob, os

ROOT = "/home/z/my-project/output/加速学习册"
STATE_F = os.path.join(ROOT, "tools", "prebuild_state.json")
CN = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔"

# 科目配置：源md清单 + 成品HTML + 簇块pattern
CONFIG = {
    "数学": {
        "src": "上传源/数学必修一/output/必修一讲解库/*.md",
        "book": "数学必修第一册_24簇讲解库_精进版.html",
        "cluster_pat_src": r"^#+\s*簇\s*([①-㉔])",
        "cluster_pat_book": r"簇\s*([①-㉔])",
        "cluster_expect": list(CN),
    },
    "物理": {
        "src": "上传源/物理必修一/shared/物理必修一/队2/*.md",
        "book": "单册_0925/物理_必修第一册_讲解库_v19.html",
        "cluster_pat_src": r"^#+\s*簇\s*(0[1-9]|1[0-4])",
        "cluster_pat_book": r"簇\s*(0[1-9]|1[0-4])",
        "cluster_expect": [f"{i:02d}" for i in range(1, 15)],
    },
    "化学": {
        "src": "上传源/化学必修第一册/鲁科版装配/化学单册_源.md",
        "book": "单册_0925/化学_必修第一册_讲解库_鲁科版.html",
        "cluster_pat_src": r"^#+ .*§([123]\.\d)",
        "cluster_pat_book": r"§([123]\.\d)",
        "cluster_expect": ["1.1", "1.2", "1.3", "2.1", "2.2", "2.3", "3.1", "3.2", "3.3"],
        "tail_assert": ["簇12", "簇13", "第一章", "第二章", "第三章", "路由"],
    },
    # ===== 以下两科=直改HTML类管线（无源md重建），闸门=结构断言防直改误删 =====
    "生物": {
        "src": "上传源/生物必修一/output/必修一讲解库/*.md",
        "book": "单册_0925/生物_必修第一册_讲解库_v18.html",
        "structure_assert": {
            "B5锚点装配源在场": ("上传源/生物必修一/output/必修一讲解库/B5_5.1讲法锚点装配_v1.md", ["讲法锚点", "【概念打底】", "【本质定案】"]),
            "生物六章成品HTML": ("上传源/生物必修一/output/必修一讲解库/B[1-6]_*章成品*.html", ["细胞"]),
            "成品v18锚点卡在场": ("单册_0925/生物_必修第一册_讲解库_v18.html", ["讲法锚点"]),
        },
    },
    "英语": {
        "src": "上传源/英语方法_高考60分止损路线_增补层.md",
        "book": "英语方法_高考60分止损路线_打印版.html",
        "structure_assert": {
            "英语源综合报告在场": ("上传源/英语方法_高考60分止损路线_综合报告.html", ["词汇", "听力", "语法", "阅读"]),
            "英语增补层在场": ("上传源/英语方法_高考60分止损路线_增补层.md", ["增补"]),
        },
    },
    "语文": {
        "src": "上传源/语文方法/shared/语文方法_整合版/*.md",
        "book": "语文方法_高考60分止损路线_打印版.html",
        "cluster_pat_src": r"^#+\s*(文言文|作文|现代文阅读|默写与古诗文|诗歌)",
        "cluster_pat_book": r"(文言文|作文|现代文阅读|默写与古诗文|诗歌)",
        "cluster_expect": ["文言文", "作文", "现代文阅读", "默写与古诗文"],
        "structure_assert": {
            "语文方法整合版四件": ("上传源/语文方法/shared/语文方法_整合版/语文方法_*.md", ["方法"]),
            "语文增补层在场": ("上传源/语文方法/shared/语文方法_整合版/增补层_语文.md", ["增补"]),
        },
    },
}
ALL = list(CONFIG.keys())

def read(p):
    return open(p, encoding="utf-8", errors="ignore").read()

def load_state():
    if os.path.exists(STATE_F):
        return json.load(open(STATE_F, encoding="utf-8"))
    return {"exemptions": {}, "lines": {}}

FAILS, WARNS = [], []
def chk(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    line = f"  {tag} | {name}" + (f" | {detail}" if detail else "")
    print(line)
    if not ok:
        FAILS.append(f"{name}: {detail}")

def warn(name, detail):
    print(f"  WARN | {name} | {detail}")
    WARNS.append(f"{name}: {detail}")

def check_assembly_blocks(name, cfg, src_text, book_html):
    """检查1：成品讲法锚点卡的时间段特征必须在源md可定位
    只从锚点卡结构内提取（fd-anchor/anchor-item/f-讲法锚点块），防全书regex误抓非锚点数字对"""
    anchor_blocks = re.findall(
        r'<div class="fd fd-anchor">.*?(?=<div class="fd |<section|</body>)|<div class="fd f-讲法锚点">.*?(?=<div class="fd |<section)',
        book_html, re.S)
    cards = []
    for blk in anchor_blocks:
        cards += re.findall(r"(\d{1,2}:\d{2}→\d{1,2}:\d{2}|\d{1,4}(?:\.\d)?→\d{1,4}(?:\.\d)?)", blk)
    cards = sorted(set(cards))
    if not cards:
        print(f"  PASS | 装配块对账 | 成品无讲法锚点时间段，跳过")
        return
    missing = [c for c in cards if c not in src_text]
    st = load_state()
    exem = st.get("exemptions", {}).get(name, [])
    real_missing = [c for c in missing if c not in exem]
    if real_missing:
        chk(f"装配块对账（{len(cards)}卡全溯源）", False,
            f"成品有而源md无{len(real_missing)}条：{real_missing[:8]} → 处置：反提取回源 或 prebuild_state.json登记豁免")
    else:
        n_ex = len(missing) - len(real_missing)
        chk(f"装配块对账（{len(cards)}卡全溯源）", True,
            (f"（{n_ex}条已登记豁免）" if n_ex else ""))

def check_clusters(name, cfg, src_text, book_html):
    """检查2：簇块双向对账"""
    src_clusters = set(re.findall(cfg["cluster_pat_src"], src_text, re.M))
    book_clusters = set(re.findall(cfg["cluster_pat_book"], book_html))
    expect = set(cfg["cluster_expect"])
    src_missing = expect - src_clusters      # 源缺=丢块风险
    book_missing = expect - book_clusters    # 成品缺=装配漏
    ok_src = not (src_missing - set(load_state().get("exemptions", {}).get(name + "_clusters", [])))
    chk(f"簇块对账·源md（{len(src_clusters & expect)}/{len(expect)}）", ok_src,
        f"源缺：{sorted(src_missing)}" if src_missing else "")
    chk(f"簇块对账·成品（{len(book_clusters & expect)}/{len(expect)}）", not book_missing,
        f"成品缺：{sorted(book_missing)}" if book_missing else "")

def check_chem_tail(cfg, src_text):
    """检查3：尾部区固定断言（9/30化学实锤失效模式；tail_assert通用化）"""
    if not cfg.get("tail_assert"):
        return
    miss = [k for k in cfg["tail_assert"] if k not in src_text]
    chk(cfg.get("tail_label", "尾部区断言"), not miss, f"缺：{miss}" if miss else "")

def check_structure(name, cfg):
    """检查2b：直改HTML类管线的结构断言（防直改误删，161行功能误删实锤同族）
    structure_assert: {说明: [(文件相对路径, 必含标记list)]}"""
    sa = cfg.get("structure_assert")
    if not sa:
        return
    for label, (fpat, marks) in sa.items():
        files = sorted(glob.glob(os.path.join(ROOT, fpat)))
        if not files:
            chk(f"结构断言·{label}", False, f"无匹配文件：{fpat}")
            continue
        missing_files = [os.path.relpath(f, ROOT) for f in files
                         if not all(m in read(f) for m in marks)]
        chk(f"结构断言·{label}（{len(files)}件）", not missing_files,
            f"缺标记：{missing_files}" if missing_files else "")

def check_drift(name, cfg):
    """检查4：行数漂移 vs 上次登记"""
    st = load_state()
    files = sorted(glob.glob(os.path.join(ROOT, cfg["src"])))
    if not files:
        chk("源文件存在性", False, f"无匹配：{cfg['src']}")
        return 0
    total = 0; drift = []
    for f in files:
        rel = os.path.relpath(f, ROOT)
        n = read(f).count("\n")
        total += n
        old = st.get("lines", {}).get(rel)
        if old and old > 0 and n < old * 0.8:
            drift.append(f"{rel}: {old}→{n}")
    if drift:
        warn("行数骤降（>20%）", "；".join(drift) + " → 确认是有意删改还是丢块")
    return total, files

def main():
    subjects = [a for a in sys.argv[1:] if not a.startswith("--")]
    register = "--register" in sys.argv
    subjects = [s for s in (subjects or ALL) if s in CONFIG]
    st = load_state()
    print(f"== prebuild_check 学习线build前闸门 == {', '.join(subjects)}\n")
    for name in subjects:
        cfg = CONFIG[name]
        print(f"【{name}】")
        src_text = ""
        files = sorted(glob.glob(os.path.join(ROOT, cfg["src"])))
        for f in files:
            src_text += read(f) + "\n"
        book_html = read(os.path.join(ROOT, cfg["book"]))
        check_assembly_blocks(name, cfg, src_text, book_html)
        if cfg.get("cluster_expect"):
            check_clusters(name, cfg, src_text, book_html)
        check_chem_tail(cfg, src_text)
        check_structure(name, cfg)
        total, files = check_drift(name, cfg)
        if register and not any(n.startswith(name) for n in FAILS):
            for f in files:
                st.setdefault("lines", {})[os.path.relpath(f, ROOT)] = read(f).count("\n")
        print()
    if register:
        json.dump(st, open(STATE_F, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"[已登记漂移基线 → {os.path.relpath(STATE_F, ROOT)}]")
    print(f"== 结果：{'❌ FAIL×' + str(len(FAILS)) if FAILS else '✅ 全PASS'}{' ⚠️×' + str(len(WARNS)) if WARNS else ''} ==")
    if FAILS:
        print("\n处置路径：①反提取回源（首选）②登记豁免（tools/prebuild_state.json exemptions，须带理由）③修源后重跑")
        sys.exit(1)

if __name__ == "__main__":
    main()
