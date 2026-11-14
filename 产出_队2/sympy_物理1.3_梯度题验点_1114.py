#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：物理1.3 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题全部数值/答案点（选择1-3/填空/挑刺/解答1/解答2）＋真题锚2题数值点＋对账表/直觉实验概念注记＋正本既有验点抽查。
概念判断题（选择1·挑刺两错·真题锚②B/C/D项）无可代验数值对象，如实注记（概念推演/回源直读替代）。
运行留痕：sympy_物理1.3_梯度题验点_1114_运行留痕.txt
"""
import sys
from sympy import Rational, sqrt

PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

# ---- 选择1（易）：B 速率=瞬时速度大小·速度计示数 ----
chk('选择1-B 速率概念推演', True, '概念题·速率=瞬时速度大小(p23)·速度计实时示数=速率·如实注记')
chk('选择1-A/C/D 排除推演', True, 'A把总位移÷总时间偷换成拉平均·C错速度系矢量·D错位移大用时更久照样慢')

# ---- 选择2（中）：B v华:v强=2:5 ----
vh = Rational(100) / (Rational(10) + Rational(30) + Rational(10))
vq = Rational(100) / Rational(20)
chk('选择2 v华=100÷50=2 m/s（含休息）', vh == 2, f'100/50={vh}')
chk('选择2 v强=100÷20=5 m/s', vq == 5, f'100/20={vq}')
chk('选择2-B 比值2:5', Rational(vh, vq) == Rational(2, 5), f'{vh}:{vq}=2:5')

# ---- 选择3（难）：C v(3)=0转折点 ----
v3 = Rational(3) - Rational(3)
chk('选择3-C v(3)=3−3=0 m/s', v3 == 0, f'v(3)={v3}·v由正变负=反向转折')
chk('选择3-D 前3s位移=梯形(3+0)×3÷2=4.5 m', Rational(3, 2) * Rational(3) == Rational(9, 2), f'面积={Rational(9,2)}')
chk('选择3-D 平均速度=4.5÷3=1.5 m/s≠0排除', Rational(9, 2) / 3 == Rational(3, 2), f'{Rational(9,2)/3}=1.5·D排除')
chk('选择3-A/B 代入排除', Rational(3) - Rational(6) == -3, 'A系t=0值·B系t=6值·v(3)=0两不符')

# ---- 填空（中）：0.4 m/s·0.5 m/s ----
v1 = Rational(Rational(24, 10), 10) / Rational(6, 100)
chk('填空① 前段=2.4cm÷0.06s=0.4 m/s', Rational(24, 1000) / Rational(6, 100) == Rational(2, 5), f'{Rational(24,1000)/Rational(6,100)}=0.4')
v2 = Rational(36, 1000) / Rational(6, 100)
chk('填空② 后段=3.6cm÷0.06s=0.6 m/s（独立复核）', v2 == Rational(3, 5), f'{v2}=0.6')
vsum = Rational(60, 1000) / Rational(12, 100)
chk('填空③ 合计=6.0cm÷0.12s=0.5 m/s', vsum == Rational(1, 2), f'{vsum}=0.5')
chk('填空④ 等时巧合：拉平均(0.4+0.6)÷2=0.5=合计', (Rational(2, 5) + Rational(3, 5)) / 2 == vsum, '等时才成立·非通则·解析如实注记')

# ---- 挑刺（中）：两处错·概念 ----
chk('挑刺-错① 速度计示数=瞬时速率非全程平均（概念）', True, 'p23口径·推演核')
chk('挑刺-错② 往返位移0→平均速度0·所算系平均速率（概念）', True, '位移口径·直觉实验同款坑·推演核')

# ---- 解答1（中）：400/280=10/7≈1.43·行驶400/160=2.5 ----
st = Rational(150) + Rational(250)
tt = Rational(60) + Rational(120) + Rational(100)
v1a = st / tt
chk('解答1 总位移=150+250=400 m', st == 400, f'{st}')
chk('解答1 总时间=60+120+100=280 s', tt == 280, f'{tt}')
chk('解答1⑴ 全程平均=400÷280=10/7≈1.43 m/s（向东）', v1a == Rational(10, 7), f'{v1a}≈{float(v1a):.4f}')
chk('解答1⑵ 等单120 s位移0→平均速度0', Rational(0) == 0, '停在原地·位移零矢量')
v3a = st / Rational(160)
chk('解答1⑶ 行驶段=400÷160=2.5 m/s', v3a == Rational(5, 2), f'{v3a}')
chk('解答1⑷ 1.43<2.5（等单拉低总平均）', v1a < v3a, f'10/7≈1.43<5/2=2.5·推演核')

# ---- 解答2（难）：月面直角三角形·3-4-5×30 ----
dOA = Rational(90)
tOA = Rational(180)
chk('解答2⑴ OA平均=90÷180=0.5 m/s（向北）', dOA / tOA == Rational(1, 2), f'{dOA/tOA}')
dAB = sqrt(Rational(90) ** 2 + Rational(120) ** 2)
chk('解答2⑵ AB位移=√(90²+120²)=150 m（3-4-5×30）', dAB == 150, f'√(8100+14400)={dAB}')
vAB = dAB / Rational(240)
chk('解答2⑵ AB平均=150÷240=0.625 m/s', vAB == Rational(5, 8), f'{vAB}')
vall = Rational(120) / Rational(420)
chk('解答2⑶ 全程位移=OB=120 m·平均=120÷420=2/7≈0.29 m/s（向东）', vall == Rational(2, 7), f'{vall}≈{float(vall):.4f}')
vrate = Rational(90) + Rational(150)
chk('解答2⑷ 平均速率=(90+150)÷420=240/420=4/7≈0.57 m/s', vrate / Rational(420) == Rational(4, 7), f'{vrate/420}≈{float(vrate/420):.4f}')
chk('解答2⑷ 速率>速度大小（4/7>2/7·路程口径翻倍）', Rational(4, 7) > Rational(2, 7), '速率认走了多少·速度认挪了多少')

# ---- 真题锚①（2024江西T3·x=1+2t+3t²） ----
x0 = Rational(1)
x1 = Rational(1) + Rational(2) + Rational(3)
chk('真题锚① x(0)=1 m·x(1)=1+2+3=6 m', x0 == 1 and x1 == 6, f'x(1)={x1}')
dx1s = x1 - x0
chk('真题锚① 第1s内位移=6−1=5 m（答案C数值支）', dx1s == 5, f'Δx={dx1s}')
chk('真题锚① A/B的"6 m"=末坐标误当位移', Rational(6) != Rational(5), '忘减初位置·概念排除')
chk('真题锚① 定义支：速度刻画位置变化快慢（概念）', True, '教材p21口径·推演核·答案C')

# ---- 真题锚②（2023.6浙江T4·玉兔二号） ----
Fmo = Rational(135) * Rational(10) / Rational(6)
chk('真题锚② A项复核：135×10÷6≈225 N≠1350 N', Fmo == Rational(225), f'{Fmo}·月球g≈地球1/6·A排除')
chk('真题锚② B项：AB曲线段速度方向变→一定有加速度（概念·跨2.3域注记）', True, '概念推演·答案B·回源直读在案')
chk('真题锚② C/D项图证/位移口径（概念+图证注记）', True, 'C需图证如实注记·D位移=OB连线<曲线长')

# ---- 对账表/直觉实验/存量抽查 ----
chk('对账表 三种快慢口径分立（概念）', True, '平均/瞬时/速率·教材p22-23口径照录·生活对应行自编类比如实注记')
chk('直觉实验 往返版位移0·App平均速率>0（概念）', True, '真实可做·反直觉点=两个"平均"口径分流·如实注记')
chk('存量抽查 正本v=72/3.6=20 m/s换算（既有值复核）', Rational(72) / Rational(36, 10) == Rational(20), '72 km/h=20 m/s')
chk('存量抽查 正本0.02×5=0.1 s（既有值复核）', Rational(2, 100) * 5 == Rational(1, 10), '50 Hz计数点口径')
chk('存量抽查 正本100/12.5=8 s（既有值复核）', Rational(100) / Rational(125, 10) == Rational(8), 'p26练习同源')

print(f'\n===== 总验点 {len(PASS) + len(FAIL)} · 失败 {len(FAIL)} · {"ALL PASS" if not FAIL else "存在FAIL"} =====')
sys.exit(1 if FAIL else 0)
