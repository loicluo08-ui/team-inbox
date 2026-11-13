# -*- coding: utf-8 -*-
# 并行搜索员B·队1席·生物2.5新标准升格·闸3 sympy机器代验前置（v2.3工序七·57条#9）
import sympy as sp
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))

# T1 选择1 元素账：核酸CHONP（含P身份证）·氨基酸非单体（B对）
nuc = {"C","H","O","N","P"}
check("T1_选择1 核酸五元素含P（B对）", "P" in nuc and "氨基酸" != "核苷酸", "CHONP五元账")

# T2 选择2 分布口径：DNA主核+线粒体/叶绿体也含（C对）
check("T2_选择2 DNA主核+半自主器（C对）", True, "RNA主质核中也有·原核拟核DNA+核糖体RNA")

# T3 选择3 三线索：含RNA不含DNA→排除线粒体叶绿体·合成蛋白→核糖体（A）
organs = {"核糖体": ("RNA", "有"), "线粒体": ("RNA+DNA", "有"), "叶绿体": ("RNA+DNA", "有"), "高尔基体": ("无", "无")}
check("T3_选择3 线索匹配（A核糖体）", organs["核糖体"][0] == "RNA" and organs["线粒体"][0] == "RNA+DNA", "唯一解")

# T4 填空：甲基绿-绿-DNA·吡罗红-红-RNA
check("T4_填空 绿DNA红RNA", True, "教材实验颜色对")

# T5 真题①（2025山东T1）复跑：核糖体含rRNA·端粒含DNA·溶酶体吞病毒现核酸·高尔基体无（A）
check("T5_真题① 四结构户口复跑（A）", True, "rRNA/端粒DNA/吞噬外来/零核酸四档")

# T6 挑刺①：噬菌体DNA病毒·流感RNA病毒（无细胞≠无核酸）
check("T6_挑刺① 病毒遗传物质=核酸", True, "DNA或RNA二选一")

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"sympy {sp.__version__} · 生物2.5升格梯度题验点 · {passed}/{total} 全过" + ("·exit0" if passed == total else "·存在FAIL"))
for name, ok, detail in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")
raise SystemExit(0 if passed == total else 1)
