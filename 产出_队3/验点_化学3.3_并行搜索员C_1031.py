# -*- coding: utf-8 -*-
"""化学3.3 sympy机器代验·16式配平+数值验点 v2"""
import re
from sympy import Matrix, Rational as R

CASES = [
 ("C01","N₂+O₂=放电=2NO","N2 + O2 = 2 NO","教材p113"),
 ("C02","2NO+O₂=2NO₂","2 NO + O2 = 2 NO2","教材p113"),
 ("C03","3NO₂+H₂O=2HNO₃+NO","3 NO2 + H2O = 2 HNO3 + NO","教材p113"),
 ("C04","N₂+3H₂⇌2NH₃","N2 + 3 H2 = 2 NH3","教材p113"),
 ("C05","4NH₃+5O₂=4NO+6H₂O","4 NH3 + 5 O2 = 4 NO + 6 H2O","教材p117"),
 ("C06","NH₄HCO₃=Δ=NH₃↑+CO₂↑+H₂O","NH4HCO3 = NH3 + CO2 + H2O","教材p117"),
 ("C07","NH₄Cl=Δ=NH₃↑+HCl↑","NH4Cl = NH3 + HCl","教材p117"),
 ("C08","NH₄⁺+OH⁻=Δ=NH₃↑+H₂O","NH4 + OH = NH3 + H2O","教材p117"),
 ("C09","2NH₄Cl+Ca(OH)₂=2NH₃↑+CaCl₂+2H₂O","2 NH4Cl + Ca(OH)2 = 2 NH3 + CaCl2 + 2 H2O","教材p117"),
 ("C10","NH₃+HCl=NH₄Cl","NH3 + HCl = NH4Cl","教材p116"),
 ("C11","NH₃·H₂O⇌NH₄⁺+OH⁻","NH3.H2O = NH4 + OH","教材p116"),
 ("C12","4HNO₃=4NO₂↑+O₂↑+2H₂O","4 HNO3 = 4 NO2 + O2 + 2 H2O","教材p120"),
 ("C13","4HNO₃(浓)+Cu=Cu(NO₃)₂+2NO₂↑+2H₂O","4 HNO3 + Cu = Cu(NO3)2 + 2 NO2 + 2 H2O","教材p120"),
 ("C14","8HNO₃(稀)+3Cu=3Cu(NO₃)₂+2NO↑+4H₂O","8 HNO3 + 3 Cu = 3 Cu(NO3)2 + 2 NO + 4 H2O","教材p120"),
 ("C15","4HNO₃(浓)+C=Δ=CO₂↑+4NO₂↑+2H₂O","4 HNO3 + C = CO2 + 4 NO2 + 2 H2O","教材p120"),
 ("C16","NH₃+H₂O⇌NH₃·H₂O","NH3 + H2O = NH3.H2O","教材p116"),
]
els = ["N","O","H","Cl","Ca","Cu","C"]
def parse(side):
    counts = {e:0 for e in els}
    side = side.replace(" ","")
    for part in side.split("."):
        for seg in part.split("+"):
            if not seg: continue
            m = re.match(r"^(\d+)(.*)$", seg)
            coef = int(m.group(1)) if m else 1
            body = m.group(2) if m else seg
            while "(" in body:
                i = body.index("("); j = body.index(")", i)
                inner = body[i+1:j]
                k = j+1; num = ""
                while k < len(body) and body[k].isdigit():
                    num += body[k]; k += 1
                mult = int(num) if num else 1
                def _exp(mm):
                    a,b = mm.group(1), mm.group(2)
                    c = (int(b) if b else 1)*mult
                    return a+(str(c) if c>1 else "")
                inner = re.sub(r"([A-Z][a-z]?)(\d*)", _exp, inner)
                body = body[:i] + inner + body[k:]
            for e,n in re.findall(r"([A-Z][a-z]?)(\d*)", body):
                counts[e] += coef*(int(n) if n else 1)
    return counts
def vec(c): return [c[e] for e in els]

log=[]; allok=True
for cid,title,expr,src in CASES:
    lhs,rhs = expr.split("=")
    lv,rv = vec(parse(lhs)), vec(parse(rhs))
    if lv==rv:
        st="PASS"; ok=True
        dL={}; dR={}
    else:
        M = Matrix([vec(parse(lhs)), vec(parse(rhs))]).T
        ns = M.nullspace()
        ok = (len(ns)==1)
        st = "零空间复核"+("PASS" if ok else "FAIL")
        dL=dict((e,v) for e,v in zip(els,lv) if v); dR=dict((e,v) for e,v in zip(els,rv) if v)
    allok &= ok
    log.append(f"{cid} [{st}] {title} {'| L='+str(dL)+' R='+str(dR) if dL else ''} | {src}")

u_n = 2*R(14007,1000)
u_m = R(12011,1000)+R(15999,1000)+u_n+4*R(1008,1000)
pct = float(u_n/u_m*100)
log.append(f"N01 [{'PASS' if abs(pct-46.65)<0.05 else 'FAIL'}] 尿素含氮量复算 2N/CO(NH₂)₂=28.014/60.056×100={pct:.2f}% ≈ 教材46.65%（原子量取整差如实注记）| 教材p118")
log.append("N02 [照录] 氨标况密度0.771 g·L⁻¹·1体积水溶约700体积氨·市售硝酸68%~70%·1.42 g·cm⁻³·发烟硝酸95%以上·硝酸熔点-42℃沸点83℃密度1.5 g·cm⁻³·稀4mol·L⁻¹浓15mol·L⁻¹——教材原生数值逐字照录（p115/p119/p120）")
log.append("N03 [照录] 生物固氮约占自然固氮总量90%·闪电约占10%·合成氨对粮食增产贡献率50%左右·哈伯测得0.012%体积（p112/p114）")
log.append(f"SYMPY-16式配平+数值总判：{'ALL PASS' if allok and abs(pct-46.65)<0.05 else 'HAS FAIL'}")
out = "\n".join(log)
open("/home/z/my-project/agents/6a9cf52e26f40cafe9f060ac/wt_c1028/产出_队3/验点_化学3.3_并行搜索员C_1031.log","w",encoding="utf-8").write(out+"\n")
print(out)
