# print渲染标准V2.2（Alex定稿1101·逸翔18:08授权按质量执行·全员print层强制标准）

**适用**：一切首学版html的print层渲染与print PDF产出。新件出print时直接按本标准内嵌CSS；存量件重出时同。

## 一、设计原则（单主色系+泄漏防护）

1. **单主色系**：海洋蓝#1B4F72家族承担全部语义（深#1B4F72/#2C6E9E/#dce9f4/#eef4f9三级）+仅两个功能性强调色：荧光黄#ffe66b（mark判据·划重点）+警示红#b03a2e（pit易错）。禁七色相并置（V1已废：认知负荷高）。
2. **明度三级梯度**（肉眼可辨阈值≥4）：key判据231（#dce9f4+双线框·权重最高）／try自测245（#f0f6fa·可书写底）／talk讲解255（纯白·最低权重）。
3. **check考位块=白底+深蓝细框（试卷框形态）**；alt拓展/box=纯灰阶降噪；step-tag/h2=深海蓝实底/边条。

## 二、print层标准CSS（@media print内·追加式嵌入）

```css
.talk, .key, .pit, .try, .box, .check, .alt, .fig svg { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.talk { background: #fff; border: 1px solid #e3e8ee; border-left: 3px solid #2C6E9E; }
.key { background: #dce9f4; border: 1px solid #b7cfe3; border-left: 4px solid #1B4F72; border-top: 2px solid #1B4F72; }
.pit { background: #fdf1f0; border: 1px solid #f0d5d3; border-left: 4px solid #b03a2e; }
.try { background: #f0f6fa; border: 1px solid #d8e3ec; border-left: 4px solid #1B4F72; }
.check { background: #fff; border: 1.5px solid #1B4F72; }
.alt { background: #f7f7f8; border: 1px solid #e2e2e5; border-left: 3px solid #9aa3ad; }
.box { background: #f5f6f7; border: 1px solid #e0e2e5; }
.fig svg { background: #fafafa; }
.step-tag { background: #1B4F72; color: #fff; }
mark.nb { background: #ffe66b; }
h2 { border-left-color: #1B4F72; }
.foot { display: none; }
```

## 三、泄漏防护条款（1101泄漏事件立法·硬闸）

**机检豁免≠视觉豁免。** 学生面（print PDF）禁止出现：
- foot区全部形态：`<div class="foot">`／"【foot·验点账】"／"素材源溯源"／裸文本影印流水——print层一律隐藏或删除
- 内部工程token：contentId/ts号/commit hash（dui*_XX/286c2b7类）/API名（ndrv2）/席位署名（"出品：XX席"）/内部工序语（"候群外终裁""候并禁直推""勘误行N联动""审查"类工作账）
- figcap/svg text内的交付状态标注（"已交付（dui1_31）"类）
- sub节头影印账+出品署名
- 真题锚候采文案中性化："真题锚：本节暂未收录对口真题，候补。"（禁"对证源卷源池vX.X候池回填"类内部语）

**出件自检**：print PDF出件后pdftotext全文检索上列token，零命中才得出库。

## 四、命名与产出规范

1. print PDF唯一命名：`print渲染V2.2_科目X.Y_节名.pdf`（双活候裁节加`_席别版`后缀候裁）
2. 双活节版本裁决：8案先例=main直产/群外管理员席版优先；无定谳账节以群外版为临时正本+候群外终裁追记
3. 旧系print（print_*.pdf/print七查_*.pdf）一律git rm防双print（v15先例延续）
4. 渲染管线：weasyprint；出件后页数/文本字符数/泄漏token三项记录

—— Alex主session · 1101 18:0x · 承逸翔"按质量你来决定"授权
