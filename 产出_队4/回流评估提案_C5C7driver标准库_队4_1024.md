# 提案·C5机制/C7页码driver回流标准库评估（队4·B席·1024 15:1x·候调度确权）

> 令源：15:12令③（打印线owner=管理员席·候确权）。实证基底：物理1章装配件1fe5225（C5+C7首用全绿）＋数学2章058f75c伤1（SVG深fill·C4=3.18%）反例解剖。

## §一 提案内容（标准库打印线v1.1→v1.2增量）

1. **C5机制**（已在物理件实测）：PRINT_CSS追加`table,blockquote,.secdiv,.chapmap{page-break-inside:avoid;} tr,li{page-break-inside:avoid;} h2,h3{page-break-after:avoid;}`——孤行标题清零实证（物理1章49页孤行0·地理第3章复测孤行0）
2. **C7页码**：page.pdf增`display_header_footer=True`+footerTemplate（"书名·章名 N/total"页脚·8px居中）+bottom边距12→14mm——物理1章/地理2章双件实证逐页在座
3. **（新提案·伤1衍 生）fill全反演分支**：现INVERT_JS的invColor=保亮度排序设计（v=gr×0.82+18·对大fill面积不增白→数学2章P1=3.18%超线实证）。增补：对svg内rect/circle/path的**fill属性**（非text）若grayscale<100则映射v=255−⌊gr×0.35⌋（大块深底→近白·文字/线条仍走原invColor保对比）——a/b修法之b（治推广·免逐件改SVG调色板）

## §二 实证对账

| 件 | C5 | C7 | C4 |
|---|---|---|---|
| 物理1章（1fe5225·driver版） | 孤行0 | N/49逐页 | 0.64% |
| 地理2章（ead1e09·C席移植） | — | N/16逐页 | — |
| 数学1章（f926847·未注入） | 孤行1 | 缺 | 0.64% |
| 数学2章（058f75c·未注入） | 孤行1 | 缺 | **3.18%** |

## §三 边界

- 提案不动标准库现行文件（owner确权后由owner落库或授权落库）；driver工具已在物理1章件随件在库可直采
- 落库后四科在途装配件重出批PDF时统一受益（数学1/2章重出时顺带销C5/C7/C4三类伤）
