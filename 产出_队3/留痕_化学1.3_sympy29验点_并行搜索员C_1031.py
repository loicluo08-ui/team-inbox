from sympy import Rational
ok=[];bad=[]
def chk(name,got,exp,tol=None):
    d=abs(Rational(str(got))-Rational(str(exp)))
    passed = d<=Rational(str(tol)) if tol else d==0
    (ok if passed else bad).append((name,got,exp))
chk('p24例1',3.01e23/6.02e23,0.5,'1e-12')
chk('p24例2',9.03e23/6.02e23,1.5,'1e-12')
chk('p26例1',64/32,2); chk('p26例2',0.4*58.5,23.4,'1e-12')
chk('p26例3',33.6/22.4,1.5,'1e-12'); chk('p26例4',2*22.4,44.8)
chk('p29例',2*0.2,0.4,'1e-12')
chk('Zn n',0.65/65,0.01,'1e-12'); chk('Zn HCl',2*0.65/65,0.02,'1e-12')
chk('Zn V(L)',(2*0.65/65)/2,0.01,'1e-12'); chk('Zn H2L',0.01*22.4,0.224,'1e-12'); chk('ZnCl2g',0.01*136,1.36)
chk('KOH n',28/56,0.5); chk('KOH c',28/56/0.25,2)
chk('CO2mol',33.6/22.4,1.5,'1e-12'); chk('CO2N',1.5*6.02,9.03,'1e-12')
chk('S1e',8*6.02,48.16); chk('S2比',5*3/(8*3),5/8)
chk('S3M',8*12+10*1+4*14+2*16,194); chk('S3n',0.194/194,0.001,'1e-12')
chk('S4mol',4.48/22.4,0.2,'1e-12'); chk('S4N',0.2*6.02,1.204,'1e-12')
chk('S5n',0.08*3,0.24); chk('S5纯g',0.24*98,23.52); chk('S5浓g',0.24*98/0.98,24.0); chk('S5mL',round(0.24*98/0.98/1.84,1),13.0)
chk('alt2(1e21)',round(0.05/18*6.02*100,2),1.67)
chk('NA雏形(1e22)',round(1.83e18*22330/1e22,2),4.09)
chk('实验m',0.04*58.5,2.34)
print('PASS=%d FAIL=%d'%(len(ok),len(bad)))
for b in bad: print('  FAIL:',b)
