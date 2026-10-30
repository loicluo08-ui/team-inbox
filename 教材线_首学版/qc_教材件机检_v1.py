#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
教材件专用机检 v1.1（首学版_*.html 出库闸机器层·v1.1=1030晚扩结构检查项：T12节首清单/T11考位锚/节末导图在场+alt块外课外内容检查——标准v2.3配套）
口径（标准模板v2.2验收节）：
  - 生产语域词 出现在【正文】（foot区豁免）= 红（真泄漏·退回）
  - 投资/金融内容词 出现在【正文】= 黄（候管理员席人工裁·不自动退回，输出上下文）
  - foot区（<div class="foot">…</div>）= 元信息区豁免（素材源溯源行允许v18/簇字样）
  - 工作件（工作单/报告/台账）请用 qc_金融语域机检_v1.py（本脚本只管教材件）
用法：python3 qc_教材件机检_v1.py <文件.html>
输出：首行判定（✅绿/🟡黄N处/❌红N处）+ 命中明细；exit 0=绿或黄（黄候裁非阻断）exit 2=红
"""
import sys, re

# 生产语域词（正文零容忍·真泄漏）
PROD_WORDS = ["v18", "v19", "簇⑴", "簇⑫", "簇①", "簇②", "簇③", "簇④", "簇⑤", "簇⑥", "簇⑦",
              "工作单", "认领", "落池", "帧验", "对位表", "claim", "CLAIM", "出品席", "复扫三件套",
              "批量批", "放量件", "终验报告", "QC", "质检席", "代推"]
# 投资/金融内容词（正文=黄候裁·类比锚段正当）
FIN_WORDS = ["投资", "持仓", "净值", "股票", "多因子", "选股", "打板", "低吸", "建仓", "仓位",
             "基金", "K线", "大盘", "牛市", "熊市", "止损", "涨停"]

def strip_foot(text):
    """剥离 foot 区（豁免），返回 (正文, foot)"""
    m = re.search(r'(<div class="foot">.*?</div>)', text, re.S)
    if m:
        return text[:m.start()] + text[m.end():], m.group(1)
    return text, ""

def hits(text, words):
    out = []
    for w in words:
        for m in re.finditer(re.escape(w), text):
            s = max(0, m.start() - 25)
            ctx = re.sub(r'<[^>]+>', '', text[s:m.end() + 25]).strip().replace('\n', ' ')
            out.append((w, ctx))
    return out

def main():
    if len(sys.argv) < 2:
        print("用法: python3 qc_教材件机检_v1.py <教材件.html>"); sys.exit(1)
    path = sys.argv[1]
    text = open(path, encoding='utf-8', errors='replace').read()
    body, foot = strip_foot(text)
    reds = hits(body, PROD_WORDS)
    yellows = hits(body, FIN_WORDS)
    name = path.split('/')[-1]
    # v1.1 结构检查项（标准v2.3 T11/T12/节末导图/alt纪律）
    struct_missing = []
    if '读完这节你能' not in body: struct_missing.append('T12节首清单缺失')
    if '高考怎么考' not in body: struct_missing.append('T11考位锚块缺失')
    if 'aria-label="本节位置图' not in body: struct_missing.append('节末位置图缺失')
    # alt纪律：课外拓展类标题不得出现在alt可选块之外
    alt_zone = re.search(r'<div class="alt">.*?</div>', text, re.S)
    alt_text = alt_zone.group(0) if alt_zone else ''
    body_no_alt = body.replace(alt_text, '') if alt_text else body
    for kw in ['课外拓展', '知识拓展', '延伸阅读']:
        if kw in body_no_alt: reds.append((kw, '课外内容出现在alt可选块之外（#17/#30红线）'))
    if reds:
        print(f"❌{name}: {len(reds)}处生产语域/结构红线（红·退回）")
        for w, c in reds: print(f"    [生产/结构] {w}: …{c}…")
        sys.exit(2)
    if struct_missing:
        print(f"🟡{name}: 结构缺项{len(struct_missing)}处（黄·候管理员席裁——历史版本/特殊节型可豁免）")
        for s in struct_missing: print(f"    [结构] {s}")
        sys.exit(0)
    if yellows or struct_missing:
        parts = []
        if yellows: parts.append(f"{len(yellows)}处投资词候裁")
        if struct_missing: parts.append(f"{len(struct_missing)}处结构缺项")
        print(f"🟡{name}: " + "·".join(parts) + "（黄·候管理员席裁）")
        for w, c in yellows: print(f"    [投资] {w}: …{c}…")
        for s in struct_missing: print(f"    [结构] {s}")
        print(f"（foot区已豁免{len(foot)}字节·素材源溯源行不检）")
        sys.exit(0)
    print(f"✅{name}: 正文零命中·结构全过")
    sys.exit(0)

if __name__ == "__main__":
    main()
