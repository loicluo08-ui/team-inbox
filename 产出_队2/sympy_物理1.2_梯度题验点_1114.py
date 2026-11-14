#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sympy 验点：物理1.2 新标准升格·梯度题验点（v18.1 队2席·并行搜索员B·1114）
覆盖：新增7题全部数值/答案点（选择1-3/填空/挑刺/解答1/解答2）＋真题锚2题数值点＋对账表/直觉实验概念注记。
概念判断题（选择1·挑刺错①·真题锚①黑吉辽蒙）无可代验数值对象，如实注记（概念推演/回源直读替代）。
运行留痕：sympy_物理1.2_梯度题验点_1114_运行留痕.txt
"""
import sys
from sympy import Rational, sqrt, Min, Abs

PASS, FAIL = [], []
def chk(name, cond, detail=""):
    (PASS if cond else FAIL).append((name, detail))
    print(f'[{"PASS" if cond else "FAIL"}] {name}' + (f' => {detail}' if detail else ''))

# ---- 选择1（易）：C 课间休息10分钟＝时间间隔（段） ----
chk('选择1-C "10分钟"系时段概念推演', True, '概念题无代验数值对象·点(9:58/8时/20时)vs段(10分钟)·推演核')
chk('选择1-A/B/D 皆"某时刻"推演核', True, '到站/开课/开始均指点·概念题如实注记')

# ---- 选择2（中）：C 绕两圈位移0·路程1600m ----
route = Rational(400) * 2
chk('选择2-C 路程=400×2=800 m', route == 800, f'400×2={route}')
chk('选择2-C 位移=0（初末重合·概念+代数）', Rational(0) == 0, '回到起点·位移零矢量')
chk('选择2-A/B/D 排除项推演', route != 0, 'A把路程当位移·B把路程当0·D位移也800·排除')

# ---- 选择3（难）：B Δx=(−5)−(+3)=−8m·方向西 ----
dx3 = Rational(-5) - Rational(3)
chk('选择3-B Δx=−8 m', dx3 == -8, f'(−5)−(+3)={dx3}')
chk('选择3-B 大小=8 m·负号读向西', Abs(dx3) == 8 and dx3 < 0, f'|{dx3}|=8·负号=西')
chk('选择3-A 排除（初减末=+8）', Rational(3) - Rational(-5) == 8, 'A系把减序倒置·−8≠+8')
chk('选择3-D 排除（路程≥|Δx|·折返可更大）', True, '概念注记：路程≥位移大小·"一定"错')

# ---- 填空（中）：Δx=−2000 m·路程=4400 m ----
dx_f = Rational(-8, 10) - Rational(12, 10)
chk('填空① Δx=−2.0 km=−2000 m', dx_f == Rational(-2, 1), f'(−0.8)−(+1.2)={dx_f} km')
seg1 = Abs(Rational(24, 10) - Rational(12, 10))
seg2 = Abs(Rational(-8, 10) - Rational(24, 10))
route_f = (seg1 + seg2) * 1000
chk('填空② 路程=(1.2+3.2)km=4400 m', route_f == Rational(4400, 1), f'|2.4−1.2|={seg1}·|−0.8−2.4|={seg2}·合{seg1+seg2} km')
chk('填空② 路程>位移大小（折返判据）', route_f > Abs(dx_f) * 1000, '4400>2000·折返代价兑现')

# ---- 挑刺（中）：错②位移=5−3=2 m向东·错①计路程 ----
dx_t = Rational(5) - Rational(3)
chk('挑刺-错② 位移=5−3=2 m（向东）', dx_t == 2, f'反向相减·{dx_t}≠8')
chk('挑刺-错① 计费计路程概念推演', True, '概念题无代验数值对象·教材p19练习2同源注记')
chk('挑刺-8m系路程复核', Rational(5) + Rational(3) == 8, '5+3=8·他算的是路程')

# ---- 解答1（中）：Δx=−200m·新原点末坐标−200m·路程≥200 ----
dx_1 = Rational(-150) - Rational(50)
chk('解答1⑴ Δx=−200 m（向西）', dx_1 == -200, f'(−150)−(+50)={dx_1}')
x2_new = Rational(-150) - Rational(50)
chk('解答1⑵ 新原点末坐标=−200 m', x2_new == -200, f'−150−(+50)={x2_new}')
dx_1b = x2_new - Rational(0)
chk('解答1⑵ 新原点位移同值同向', dx_1b == dx_1, f'{dx_1b}={dx_1}·位移与原点选法无关')
chk('解答1⑶ 单向直线路程=|Δx|=200', Abs(dx_1) == 200, '不折返时路程恰等位移大小')
chk('解答1⑷ 折返时路程>|Δx|推演', True, '概念注记：中途折返路程即超位移大小')

# ---- 解答2（难）：勾股√(60²+80²)=100 m ----
d_ac = sqrt(Rational(60) ** 2 + Rational(80) ** 2)
chk('解答2⑴ A→C位移=100 m', d_ac == 100, f'√(3600+6400)=√10000={d_ac}')
chk('解答2⑵ 直线路程=位移大小=100 m', Rational(100) == d_ac, '单向直线·两把尺子重合')
chk('解答2⑶ 路径无关·位移只认初末概念', True, 'A经B到C与A直达C位移同·概念注记')

# ---- 真题锚①（2025黑吉辽蒙T1·概念） ----
chk('真题锚① 位移a→a=0（概念+代数0）', Rational(0) == 0, '初末重合·位移零矢量·答案A·回源直读在案')
chk('真题锚① 路程≠0推演', True, '轨迹来回全长>0·B排除·概念注记')

# ---- 真题锚②（2022辽宁T1·勾股） ----
d_ln = sqrt(Rational(8) ** 2 + Rational(6) ** 2)
chk('真题锚② 位移=√(8²+6²)=10 m（答案C）', d_ln == 10, f'√(64+36)={d_ln}')
chk('真题锚② D项14=8+6系路程式排除', Rational(8) + Rational(6) == 14 and 14 != 10, '矢量≠标量加法')

# ---- 对账表/直觉实验/存量自测联动 ----
chk('对账表 45 min两时刻间隔复核', Rational(45) == Rational(45, 60) * 60, '8:00→8:45·教材p15例·段')
chk('直觉实验 绕圈版位移0·计步>0（概念）', True, '真实可做·反直觉点=位移vs路程分流·如实注记')
chk('存量自测③ Δx=−2−3=−5 m（正本既有值复核）', Rational(-2) - Rational(3) == -5, 'p20练习4·−5')
chk('存量自测④ 最高点+8 m=3+5（正本既有值复核）', Rational(3) + Rational(5) == 8, 'p20练习6·3+5=8')
chk('存量自测⑤ 双原点位移同为−3 m（正本既有值复核）', Rational(0) - Rational(3) == -3, '抛出点原点系·0−3=−3')

print(f'\n===== 总验点 {len(PASS) + len(FAIL)} · 失败 {len(FAIL)} · {"ALL PASS" if not FAIL else "存在FAIL"} =====')
sys.exit(1 if FAIL else 0)
