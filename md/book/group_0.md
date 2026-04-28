<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700;1,400;1,700&display=swap');
body, .markdown-preview, .mume {
    font-family: 'Lora', serif !important;
    font-size: 17px !important;
    line-height: 1.7 !important;
    color: #333333 !important;
}
h1, h2, h3, h4, h5, h6 {
    font-family: inherit !important;
    font-weight: bold !important;
    color: #000000 !important;
    margin-top: 1.5em !important;
    margin-bottom: 0.5em !important;
}
p { text-align: justify !important; }
</style>

# 中国科学院研究生教学丛书

测度论讲义

# (第三版)

严加安 著

北京

---

##### 内容简介

本书系统完整地介绍了测度论和概率论的基础知识。前5章介绍一般可测空间和Hausdorff空间上的测度与积分，包括局部紧拓扑群上的Haar测度。第6章介绍距离空间上测度的弱收敛和局部紧Hausdorff空间上测度的淡收敛。第7章介绍与测度论有关的概率论基础，第8章介绍离散时间鞅的基本理论。第9章介绍Hilbert空间和Banach空间上的测度，第10章内容包括容度的Choquet积分，离散集函数的Mobius反转，Shapley值和Shannon熵。书中还收录了作者在测度论和概率论基础方面的一些研究成果。

本书适合作为概率统计专业和其他数学专业的研究生教材，也可作为科研人员和高等院校教师的参考书。

图书在版编目(CIP)数据

测度论讲义/严加安著. —3版. —北京：科学出版社, 2021.3

(中国科学院研究生教学丛书)

ISBN 978-7-03-067803-4

Ⅰ. ①测… Ⅱ. ①严… Ⅲ. ①测度论-研究生-教材 Ⅳ. ①O174.12

中国版本图书馆 CIP 数据核字 (2021) 第 006096 号

责任编辑：王静 / 责任校对：杨聪敏

责任印制：张伟/封面设计：陈敬

科学出版社出版

北京东黄城根北街16号

邮政编码：100717

中国科学院印刷厂印刷

http://www.sciencep.com

科学出版社发行 各地新华书店经销

1998年10月第一版 开本:  $720 \times 1000$ 1/16

2004年8月第二版 印张：163/4

2021年3月第三版字数：338000

2021年3月第二十次印刷

定价：58.00 元

(如有印装质量问题，我社负责调换)

---

# “中国科学院研究生教学丛书”总编委会

主 任：白春礼

副主任：何岩 师昌绪 杨乐 汪尔康

沈允钢 黄荣辉 叶朝辉

委员：朱清时 叶大年 王 水 施蕴渝

余翔林 冯克勤 冯玉琳 高 文

洪友士 王东进 龚 立 吕晓澎

林鹏

# “中国科学院研究生教学丛书”数学学科编委会

主 编: 杨 乐

副主编：冯克勒

编委：王靖华 严加安 文志英 袁亚湘

李克正

---

## 第三版前言

本版是对第二版的扩充。第 5 章增加了“Haar 测度”一节，取材于 Cohn 的 Measure Theory(第二版，2013)；第 7 章增加了“平稳序列和遍历定理”一节，取材于 Shiryayev 的 Probability(第二版，1996)。此外，增加了第 10 章“Choquet 积分与离散集函数”，内容包括容度的 Choquet 积分，离散集函数的 Möbius 反转，Shapley 值和 Shannon 熵，其中有关 Choquet 积分的内容取材于 Denneberg 的 Non-Additive Measure and Integral (1994)。

严加安

2021年1月于北京

---

## 第二版前言

本版改正了第一版中的排印错误，并在内容上进行了调整和扩充。将第一版第7章中的“Kolmogorov相容性定理及Tulcea定理的推广”一节移到了第4章；在第3章增加了“空间 $L^{\infty}(\Omega,\mathcal{F})$和 $L^{\infty}(\Omega,\mathcal{F},m)$的对偶”一节；在第4章增加了“概率测度序列的投影极限”和“随机Daniell积分及其核表示”两节。此外，还新加了第8章和第9章。第8章是将第一版第7章“经典鞅论”一节加以扩充形成的，部分内容取材于Hall-Heyde所著Martingale Limit Theory and Its Application一书。第9章主要取材于黄志远和严加安所著《无穷维随机分析引论》第1章的部分内容。在本版的部分章节中还收入了Dudley所著Real Analysis and Probability和Kallenberg所著Foundations of Modern Probability书中的某些结果和作者在测度论方面的一些研究成果。

在准备新版期间, 作者得到了国家科技部 973 项目 “核心数学的若干前沿问题” 的资助, 特此感谢.

严加安

2004年3月于北京

---

## 第一版前言

测度论是现代数学的一个重要分支，它的主要奠基人是法国数学家 Lebesgue (1875—1941). 受他的老师 Borel 关于容量研究的深刻影响，他在 1902 年的论文《积分、长度与面积》中，首次把  $R^2$ 中的长度和面积概念推广为一般 Borel 集的 Lebesgue 测度，并定义了可测函数关于 Lebesgue 测度的积分. 他用累次积分计算重积分的结果后被 Fubini (1907) 完善为一般的定理. Radon (1913) 又进一步研究了  $R^d$ 中在紧集上为有穷的一般 Borel 测度 (Radon 测度). 抽象可测空间上的测度和符号测度概念是 Fréchet (1915) 最先提出的. Radon-Nikodym (1930) 给出了符号测度为一不定积分的充要条件 (Radon-Nikodym 定理). 在早期的测度论发展史中，积分概念的两个推广值得一提. 其一是 Daniell (1918) 从一类函数上的正线性泛函出发研究了测度和积分; 其二是 Bochner (1933) 和 Pettis (1938) 定义了 Banach 空间值函数关于测度的积分. 到 20 世纪 30 年代，测度与积分理论已趋于成熟，并在概率论、泛函分析和调和分析中得到广泛应用. 例如，Kolmogorov (1933) 从测度论观点出发创立了概率公理化体系，为现代概率论奠定了数学基础. 其中非常重要的条件数学期望概念就源于测度论中的 Radon-Nikodym 定理. 随着时间的推移，测度论在数学中的基础性地位愈来愈显示出来. 50 年代以后发展起来的无穷维空间中的测度和泛函积分成了研究量子物理的重要手段和工具.

本书是为概率统计专业和其他数学专业的研究生编写的一部测度论教材，它的前身是作者的《测度与积分》(陕西师大出版社，1988)。这里改正了原书中出现的错误，并对原书的第五章作了较大修改，还在第三章、第六章及第七章中增加了若干新的内容。全书内容分为三个部分：(1) 一至四章介绍一般可测空间中的测度与积分。这一部分内容与通常测度论教材大体相当，但第三章中的 Daniell 积分、Bochner 积分和 Pettis 积分以及第四章中的 Tulcea 定理在通常测度论教材中是不易找到的。(2) 第五章系统完整地介绍了 Hausdorff 空间中的测度和积分。这一部分内容对初学者有一定难度，教师在讲授时可以跳过它。(3) 第六章介绍有关测度的弱收敛和淡收敛的主要结果；第七章介绍与测度论有关的概率论基础知识，如条件数学期望，正则条件概率，一致可积性，本性上确界，解析集及经典概论等。这一部分内容是专门为概率统计专业的研究生设计的，在对其他数学专业的研究生讲授时可以略去。

---

本书几乎每一节都附有一定数量的习题, 其中不少是对正文的补充, 有些习题还在一些定理的证明中被引用.

本书的写作和出版分别得到了国家自然科学基金(项目编号 79790130)和中国科学院研究生教材出版基金的资助, 特此表示感谢.

严加安

1997年8月于北京

---

## 目 录

第三版前言  
  
第二版前言  
  
第一版前言  
  
第1章 集类与测度 ..... 1  
1.1 集合运算与集类 ..... 1  
1.2 单调类定理 (集合形式) ..... 4  
1.3 测度与非负集函数 ..... 8  
1.4 外测度与测度的扩张 ..... 11  
1.5 欧氏空间中的 Lebesgue-Stieltjes 测度 ..... 16  
1.6 测度的逼近 ..... 17  
  
第2章 可测映射 ..... 20  
2.1 定义及基本性质 ..... 20  
2.2 单调类定理 (函数形式) ..... 24  
2.3 可测函数序列的几种收敛 ..... 28  
  
第3章 积分和空间  $L^{p}$ ..... 33  
3.1 积分的基本性质 ..... 33  
3.2 积分号下取极限 ..... 37  
3.3 不定积分与符号测度 ..... 40  
3.4 空间  $L^{p}$ 及其对偶 ..... 49  
3.5 空间  $L^{\infty}(\Omega,\mathcal{F})$ 和  $L^{\infty}(\Omega,\mathcal{F},m)$ 的对偶 ..... 57  
3.6 Daniell 积分 ..... 59  
3.7 Bochner 积分和 Pettis 积分 ..... 63  
  
第4章 乘积可测空间上的测度与积分 ..... 68  
4.1 乘积可测空间 ..... 68  
4.2 乘积测度与 Fubini 定理 ..... 69  
4.3 由  $\sigma$ 有限核产生的测度 ..... 74  
4.4 无穷乘积空间上的概率测度 ..... 76  
4.5 Kolmogorov 相容性定理及 Tulcea 定理的推广 ..... 78

---

4.6 概率测度序列的投影极限 ..... 83  
4.7 随机 Daniell 积分及其核表示 ..... 85  
第 5 章 Hausdorff 空间上的测度与积分 ..... 89  
5.1 拓扑空间 ..... 89  
5.2 局部紧 Hausdorff 空间上的测度与 Riesz 表现定理 ..... 96  
5.3 Hausdorff 空间上的正则测度 ..... 101  
5.4 空间  $C_{0}(X)$ 的对偶 ..... 105  
5.5 用连续函数逼近可测函数 ..... 108  
5.6 乘积拓扑空间上的测度与积分 ..... 109  
5.7 波兰空间上有限测度的正则性 ..... 114  
5.8 Haar 测度 ..... 118  
第 6 章 测度的收敛 ..... 128  
6.1 欧氏空间上 Borel 测度的收敛 ..... 128  
6.2 距离空间上有限测度的弱收敛 ..... 130  
6.3 胎紧与 Prohorov 定理 ..... 133  
6.4 可分距离空间上概率测度的弱收敛 ..... 135  
6.5 局部紧 Hausdorff 空间上 Radon 测度的淡收敛 ..... 138  
第 7 章 概率论基础选讲 ..... 143  
7.1 独立性, 0-1 律, Bayes 公式 ..... 143  
7.2 条件数学期望与条件独立性 ..... 149  
7.3 正则条件概率 ..... 159  
7.4 随机变量族的一致可积性 ..... 164  
7.5 本性上确界 ..... 169  
7.6 平稳序列和遍历定理 ..... 174  
7.7 解析集与 Choquet 容量 ..... 177  
第 8 章 离散时间鞅 ..... 183  
8.1 鞅不等式 ..... 183  
8.2 鞅收敛定理及其应用 ..... 188  
8.3 局部鞅 ..... 197  
第 9 章 Hilbert 空间和 Banach 空间上的测度 ..... 199  
9.1  $R^{m}$ 上 Borel 测度的 Fourier 变换和 Bochner 定理 ..... 199  
9.2 测度的 Fourier 变换和 Minlos-Sazanov 定理 ..... 204

---

9.3 Minlos 定理 …… 208  
9.4 Hilbert 空间上的 Gauss 测度 …… 210  
9.5 Banach 空间上的 Gauss 测度 …… 213  
第 10 章 Choquet 积分与离散集函数 …… 219  
10.1 单调函数的积分 …… 219  
10.2 单调集函数, 共单调函数 …… 220  
10.3 Choquet 积分 …… 222  
10.4 Choquet 积分的次可加性定理 …… 226  
10.5 离散集函数 …… 231  
10.6 Shannon 熵 …… 240  
参考文献 …… 244  
索引 …… 247

---

## 第 1 章 集类与测度

## 1.1 集合运算与集类

集合是现代数学的最基本的概念之一. 任何一组彼此可以区别的事物便构成一个集合. 在测度论中, 通常在某一(或某些)给定的集合(称为空间)中讨论问题.

1.1.1 令Ω为一给定非空集合，其元素用ω记之。设A为Ω的一子集，用ω ∈ A 和ω ∉ A分别表示ω属于A和不属于A。不含任何元素的集合称为空集，以Ω记之。用A ⊃ B或B ⊂ A表示B是A的子集，用

 
$$
A\cap B,\;A\cup B,\;A\setminus B,\;A\triangle B
$$
 

分别表示A与B的交、并、差和对称差，即

 
$$
A\cap B=\{\omega\mid\omega\in A 且 \omega\in B\},A\cup B=\{\omega\mid\omega\in A 或 \omega\in B\},
$$
 

 
$$
A\setminus B=\{\omega\mid\omega\in A 且 \omega\notin B\},A\triangle B=(A\setminus B)\cup(B\setminus A).
$$
 

用 $A^c$表示 $\Omega \setminus A$，并称 $A^c$为 $A$（在 $\Omega$中）的余集，于是有 $A \setminus B = A \cap B^c$。若 $A \cap B = \varnothing$，称 $A$与 $B$互不相交。显然有 $A \cap A^c = \varnothing$， $A \cup A^c = \Omega$。

1.1.2 集合交和并运算满足如下的交换律、分配律及结合律：

 
$$
A\cap B=B\cap A,\;A\cup B=B\cup A;
$$
 

 
$$
(A\cup B)\cap C=(A\cap C)\cup(B\cap C),
$$
 

 
$$
(A\cap B)\cup C=(A\cup C)\cap(B\cup C);
$$
 

 
$$
(A\cap B)\cap C=A\cap(B\cap C),
$$
 

 
$$
(A\cup B)\cup C=A\cup(B\cup C).
$$
 

此外, 它们关于余集运算有如下的 de Morgan 公式:

 
$$
(A\cap B)^{c}=A^{c}\cup B^{c},(A\cup B)^{c}=A^{c}\cap B^{c},(A^{c})^{c}=A.
$$
 

1.1.3 以Ω的某些子集为元素的集合称为(Ω上的)集类。今后，如无特别说明，总假定集类是非空的，即至少含一个元素(可以是空集)。设 $\{A_i, i \in I\}$为一集类，其

---

中I为指标集, 它用以给集类元素“编号”, 则可如下定义集类中元素的交与并:

 
$$
\bigcap_{i\in I}A_{i}=\left\{\omega\mid\omega\in A_{i}, 对一切 i\in I\right\},
$$
 

 
$$
\bigcup_{i\in I}A_{i}=\{\omega\mid\omega\in A_{i}, 对某一 i\in I\}.
$$
 

我们有相应的交换律、分配律、结合律及de Morgan公式.

1.1.4 设  $\{A_n, n \geq 1\}$ 为一集合序列．若对每个  $n$，有  $A_n \subset A_{n+1}$（相应地， $A_n \supset A_{n+1}$），则称  $(A_n)$ 为单调增（相应地，单调降）．二者统称为单调列．对单调增或单调降序列  $(A_n)$，我们分别令  $A = \bigcup_n A_n$ 或  $A = \bigcap_n A_n$，称  $A$ 为  $(A_n)$ 的极限，通常记为  $A_n \uparrow$ 或  $A_n \downarrow$．一般地，对任一集列  $(A_n)$，令

 
$$
\limsup_{n\to\infty}A_{n}=\bigcap_{n=1}^{\infty}\bigcup_{k=n}^{\infty}A_{k},\quad\liminf_{n\to\infty}A_{n}=\bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}A_{k},
$$
 

分别称其为 $(A_{n})$的上极限和下极限. 显然有

 
$$
\limsup_{n\to\infty}A_{n}=\{\omega\mid\omega 属于无穷多个 A_{n}\},
$$
 

 
$$
\liminf_{n\to\infty}A_{n}=\{\omega\mid\omega 至多不属于有限多个 A_{n}\},
$$
 

从而恒有 $\liminf_{n\to\infty}A_n\subset\limsup_{n\to\infty}A_n$。若 $\liminf_{n\to\infty}A_n=\limsup_{n\to\infty}A_n$，称 $(A_n)$的极限存在，并用 $\lim_{n\to\infty}A_n$表示 $(A_n)$的极限（即令 $\lim_{n\to\infty}A_n=\liminf_{n\to\infty}A_n=\limsup_{n\to\infty}A_n$）。

1.1.5 设  $\{A_n, n \geq 1\}$ 为一集列. 若  $(A_n)$ 两两不相交 (即  $n \neq m \Rightarrow A_n \cap A_m = \varnothing$). 则常用  $\sum_n A_n$ 表示  $\bigcup_n A_n$. 若有  $\sum_n A_n = \Omega$, 称  $\{A_n, n \geq 1\}$ 为  $\Omega$ 的一个划分.

对任一集列 $(A_{n})$，令

 
$$
B_{1}=A_{1},\;B_{n}=A_{n}A_{1}^{c}\cdots A_{n-1}^{c},\;n\geqslant2,
$$
 

则 $\{B_n, n \geq 1\}$中集合两两不相交，且有 $\sum_n B_n = \bigcup_n A_n$。这一将可列并表示为可列不交并的技巧是很有用的。

1.1.6 设C为一集类(约定是非空的). 如果 $A,B\in C\Rightarrow A\cap B\in C$ (从而 $A_{1},A_{2},\cdots,A_{n}\in C\Rightarrow\bigcap_{i=1}^{n}A_{i}\in C$),称C对有限交封闭. 如果 $A_{n}\in C,n\geq1\Rightarrow\bigcap_{n}A_{n}\in C$,称C对可列交封闭. 类似定义“对有限并封闭”及“对单调极限封闭”等概念. 令

 
$$
\mathcal{C}_{\cap f}=\left\{A\left|\begin{array}{c}A=\bigcap\limits_{i=1}^{n}A_{i},A_{i}\in\mathcal{C},i=1,\cdots,n,n\geqslant1\end{array}\right.\right\},
$$
 

则 $C_{\cap f}$对有限交封闭，我们称 $C_{\cap f}$为用有限交运算封闭C所得的集类. 类似地，我们用

 
$$
\mathcal{C}_{\cup f},\;\mathcal{C}_{\Sigma f},\;\mathcal{C}_{\delta},\;\mathcal{C}_{\sigma},\;\mathcal{C}_{\Sigma\sigma}
$$
 

---

分别表示用有限并、有限不交并、可列交、可列并及可列不交并封闭C所得的集类。此外，我们用 $C_{\cap f,\cup f}$表示 $(\mathcal{C}_{\cap f})_{\cup f}$，用 $C_{\sigma\delta}$表示 $(\mathcal{C}_{\sigma})_{\delta}$。今后常用这些记号，读者应熟悉并牢记它们。

##### 命题1.1.7 设C为一集类, 则有如下结论:

(1)  $\mathcal{C}_{\cap f,\cup f} = \mathcal{C}_{\cup f,\cap f}$;

(2) 若 C 对有限交封闭，则  $C_{\cup f}, C_{\Sigma f}, C_{\sigma}$ 及  $C_{\Sigma \sigma}$ 亦然；

(3) 若 C 对有限并封闭，则  $C_{\cap f}$ 及  $C_{\delta}$ 亦然.

##### 证 直接从集合的交和并的分配律推得.

现在我们用对集合运算的封闭性来划分不同类型的集类。下面是测度论中常用的一些集类的定义。

定义1.1.8 设C为一集类.

(1) 称 C 为  $\pi$ 类，如果它对有限交封闭.

(2) 称 C 为半环，如果  $\varnothing \in C$，且有

 
$$
A,B\in\mathcal{C}\Rightarrow A\cap B\in\mathcal{C},A\setminus B\in\mathcal{C}_{\Sigma f}.
$$
 

(3) 称 C 为半代数，如果它是半环，且  $\Omega \in C$.

(4) 称 C 为代数 (或域)，如果它对有限交及取余集运算封闭，且有  $\Omega \in C, \quad \varnothing \in C$ (由此推知它对有限并及差运算也封闭).

(5) 称 C 为  $\sigma$ 代数，如果它对可列交及取余集运算封闭，且有  $\Omega \in C, \varnothing \in C$（由此推知它对可列并及差运算也封闭）.

(6) 称 C 为单调类，如果它对单调序列极限封闭（即  $A_n \in \mathcal{C}, n \geq 1, A_n \uparrow A$ 或  $A_n \downarrow A \Rightarrow A \in \mathcal{C}$）.

(7) 称 C 为  $\lambda$ 类，如果它满足下列条件:

(i)  $\Omega \in \mathcal{C};$

(ii)  $A, B \in \mathcal{C}, B \subset A \Rightarrow A \setminus B \in \mathcal{C};$

(iii)  $A_n \in \mathcal{C}, n \geq 1$,  $A_n \uparrow A \Rightarrow A \in \mathcal{C}$.

易知： $\sigma$ 代数为  $\lambda$ 类， $\lambda$ 类为单调类。

例子1.1.9 设R为实直线(即 $R=(-\infty,\infty)$), 令

 
$$
\mathcal{C}_{1}=\{(-\infty,a]\mid a\in\mathbb{R}\},\mathcal{C}_{2}=\{(a,\infty)\mid a\in\mathbb{R}\},
$$
 

 
$$
\mathcal{C}_{3}=\{(a,b)\mid a\leqslant b,a,b\in\mathbb{R}\},
$$
 

则 $C_1, C_2$及 $C_3$为 $\pi$类， $C_1 \cup C_2 \cup C_3$为半环， $C_1 \cup C_2 \cup C_3 \cup \{\mathbb{R}\}$为半代数。

---

##### 习题

1.1.1 证明：

(1)  $(A\triangle B)\triangle C = A\triangle(B\triangle C)$;

(2)  $(A\triangle B)\cap C=(A\cap C)\triangle(B\cap C);$

(3)  $(A_1 \cup A_2) \triangle(B_1 \cup B_2) \subset (A_1 \triangle B_1) \cup (A_2 \triangle B_2)$.

1.1.2 证明：

 
$$
(\operatorname*{l i m}\operatorname*{i n f}_{n\to\infty}A_{n})\cap(\operatorname*{l i m}\operatorname*{s u p}_{n\to\infty}B_{n})\subset\operatorname*{l i m}\operatorname*{s u p}_{n\to\infty}(A_{n}\cap B_{n}).
$$
 

1.1.3 证明对可列不交并封闭的代数为 $\sigma$代数.

1.1.4 若 C 同时为代数和单调类或同时为  $\pi$ 类和  $\lambda$ 类，则 C 为  $\sigma$ 代数.

1.1.5 设C为半代数，则 $C_{\Sigma f}$为代数.

1.1.6 λ类定义中的条件(i)及(ii)等价于如下两条件:

(i) $^{\prime}$  $A \in C \Rightarrow A^{c} \in C;$

(ii) $^{\prime}$  $A,B\in\mathcal{C},A\cap B=\varnothing\Rightarrow A\cup B\in\mathcal{C}.$

1.1.7 设C为一集类，且 $\varnothing\in\mathcal{C}$，令

 
$$
\mathcal{G}=\left\{A\left|A=\left(\bigcap_{i=1}^{n}A_{i}\right)\cap\left(\bigcap_{j=1}^{m}B_{j}^{c}\right),A_{i},B_{j}\in\mathcal{C},\right.\right.
$$
 

 
$$
1\leqslant i\leqslant n,\;1\leqslant j\leqslant m,\;n,m\geqslant1\Big\},
$$
 

则 $\mathcal{G} \supset \mathcal{C}$，且 $\mathcal{G}$为半环。特别若 $\mathcal{C}$对有限并及有限交封闭，则 $\{A \cap B^c \mid A, B \in \mathcal{C}\}$为半环。

### 1.2 单调类定理(集合形式)

设$\{C_i \mid i \in I\}$为$\Omega$上一族集类，若每个集类$C_i$对某种集合运算封闭，则其交$\cap_i C_i$亦然。于是对$\Omega$上的任一非空集类$C_i$，存在包含$C$的最小$\sigma$代数、最小$\lambda$类和最小单调类，我们分别称之为由$\mathcal{C}$生成的$\sigma$代数、$\lambda$类和单调类，并分别用$\sigma(\mathcal{C}), \lambda(\mathcal{C})$和$m(\mathcal{C})$记之。我们恒有$m(\mathcal{C}) \subset \lambda(\mathcal{C}) \subset \sigma(\mathcal{C})$。本节主要研究在什么条件下有$m(\mathcal{C}) = \sigma(\mathcal{C})$或$\lambda(\mathcal{C}) = \sigma(\mathcal{C})$。

定理1.2.1 设C为一集类.

(1) 若 C 为代数, 则  $m(\mathcal{C}) = \sigma(\mathcal{C})$.

(2) 若 C 为  $\pi$ 类，则  $\lambda(\mathcal{C}) = \sigma(\mathcal{C})$.

证 $⑴$令

 
$$
\mathcal{G}_{1}=\left\{A\mid A\in m(\mathcal{C}),\;A^{c}\in m(\mathcal{C}),\;A\cap B\in m(\mathcal{C}),\forall B\in\mathcal{C}\right\},
$$
 

则 $C \subset G_1$，且 $G_1$为单调类，故 $G_1 = m(C)$。令

 
$$
\mathcal{G}_{2}=\{A\mid A\in m(\mathcal{C}),\;A\cap B\in m(\mathcal{C}),\forall B\in m(\mathcal{C})\}.
$$
 

---

则由上所证 $\mathcal{G}_1 = m(\mathcal{C})$知， $\mathcal{C} \subset \mathcal{G}_2$。但 $\mathcal{G}_2$为单调类，故 $\mathcal{G}_2 = m(\mathcal{C})$。综上所述，我们有

 
$$
A\in m(\mathcal{C})\Rightarrow A^{c}\in m(\mathcal{C});~A,B\in m(\mathcal{C})\Rightarrow A\cap B\in m(\mathcal{C}),
$$
 

即 $m(C)$为一代数，从而 $m(C)$为 $\sigma$代数(习题1.1.4)，因此有 $m(C) \supset \sigma(C)$。但相反的包含关系恒成立，故最终有 $m(C) = \sigma(C)$。

(2) 令

 
$$
\mathcal{G}_{1}=\left\{A\mid A\in\lambda(\mathcal{C}),A\cap B\in\lambda(\mathcal{C}),\forall B\in\mathcal{C}\right\},
$$
 

则 $C \subset G_1$，且 $G_1$为 $\lambda$类，故 $G_1 = \lambda(C)$。令

 
$$
\mathcal{G}_{2}=\{A\mid A\in\lambda(\mathcal{C}),\;A\cap B\in\lambda(\mathcal{C}),\;\forall B\in\lambda(\mathcal{C})\},
$$
 

则由上所证 $G_1 = \lambda(C)$知， $C \subset G_2$。但 $G_2$为 $\lambda$类，故 $G_2 = \lambda(C)$。于是 $\lambda(C)$为 $\pi$类，从而 $\lambda(C)$为 $\sigma$代数(习题1.1.4)，因此有 $\lambda(C) \supset \sigma(C)$。但相反的包含关系恒成立，故最终有 $\lambda(C) = \sigma(C)$。

此定理称为单调类定理. 它表明: 为验证某σ代数F中元素有某种性质, 只需验证: (1)有一生成F的代数(π类)C, 其元素有该性质; (2)有该性质的集合全体构成一单调类(相应地, λ类). 而这后二者的验证往往比较容易. 单调类定理是测度论中的一个重要的证明工具. 今后我们将陆续给出它的应用.

作为定理1.2.1的一个简单推论, 我们有单调类定理的如下更有用的形式.

定理1.2.2 设C, F为两个集类, 且C ⊂ F.

(1) 若 C 为代数，且 F 为单调类，则  $\sigma(C) \subset \mathcal{F}$;

(2) 若 C 为  $\pi$ 类且 F 为  $\lambda$ 类，则  $\sigma(C) \subset F$.

从定理1.2.1的证明看出, 我们可以给出使 $m(C)=\sigma(C)$或 $\lambda(C)=\sigma(C)$成立的充要条件.

定理1.2.3 设C为一集类.

(1) 为要  $m(\mathcal{C}) = \sigma(\mathcal{C})$，必须且只需：

 
$$
A\in\mathcal{C}\Rightarrow A^{c}\in m(\mathcal{C});~A,B\in\mathcal{C}\Rightarrow A\cap B\in m(\mathcal{C}).
$$
 

(2) 为要  $\lambda(\mathcal{C}) = \sigma(\mathcal{C})$，必须且只需：

 
$$
A,B\in\mathcal{C}\Rightarrow A\cap B\in\lambda(\mathcal{C}).
$$
 

由此定理, 我们还可推得如下定理.

定理1.2.4 设C为一集类.

(1) 为要  $m(\mathcal{C}) = \sigma(\mathcal{C})$，必须且只需：

 
$$
A\in\mathcal{C}\Rightarrow A^{c}\in m(\mathcal{C});~A,B\in\mathcal{C}\Rightarrow A\cup B\in m(\mathcal{C}).
$$
 

---

(2) 为要  $\lambda(\mathcal{C}) = \sigma(\mathcal{C})$，必须且只需：

 
$$
A,B\in\mathcal{C}\Rightarrow A\cup B\in\lambda(\mathcal{C}).
$$
 

证 (1) 条件的必要性显然，往证条件的充分性。设条件成立。令  $\mathcal{D} = \{A^c | A \in \mathcal{C}\}, \mathcal{G} = \{A | A^c \in m(\mathcal{C})\}$。则  $\mathcal{G}$ 为单调类，且  $\mathcal{D} \subset \mathcal{G}$，故  $m(\mathcal{D}) \subset \mathcal{G}$。这表明  $A \in m(\mathcal{D}) \Rightarrow A^c \in m(\mathcal{C})$。同理有  $A \in m(\mathcal{C}) \Rightarrow A^c \in m(\mathcal{D})$。于是有  $m(\mathcal{D}) = \{A | A^c \in m(\mathcal{C})\}$。故由定理1.2.3(1)推得  $m(\mathcal{D}) = \sigma(\mathcal{D})$。但依假定， $\mathcal{D} \subset m(\mathcal{C}), \mathcal{C} \subset m(\mathcal{D})$。于是有  $m(\mathcal{C}) = m(\mathcal{D})$，从而最终有  $m(\mathcal{C}) = \sigma(\mathcal{D}) = \sigma(\mathcal{C})$。(2)的证明类似。

上述两个定理过于一般, 实际难以应用, 但它们的下述推论是有用的(例如见下面的例子1.2.6及定理1.6.3). 需要指出: 如果不首先建立定理1.2.3及定理1.2.4, 那么是不易发现定理1.2.5的.

定理1.2.5 设C为一集类. 若它满足下列条件之一, 则有 $m(\mathcal{C})=\sigma(\mathcal{C})$:

(1)  $A, B \in \mathcal{C} \Rightarrow A \cap B \in \mathcal{C}, A \in \mathcal{C} \Rightarrow A^c \in \mathcal{C}_\delta;$

(2)  $A, B \in \mathcal{C} \Rightarrow A \cup B \in \mathcal{C}, A \in \mathcal{C} \Rightarrow A^c \in \mathcal{C}_\sigma.$

(关于记号 $C_{\delta}$及 $C_{\sigma}$见1.1.6.)

证 若C对有限交封闭，则 $C_{\delta} \subset m(C)$；若C对有限并封闭，则 $C_{\sigma} \subset m(C)$。因此条件(1)及(2)分别蕴含定理1.2.3及1.2.4的(1)中条件，定理得证。

例子1.2.6 设X为一距离空间，F表示X中闭集全体，G表示X中开集全体。显然有 $\sigma(F)=\sigma(G)$，我们称它为X的Borel  $\sigma$代数，记为 $\mathcal{B}(X)$。显然G及F分别满足定理1.2.5的条件(1)及(2)，于是我们有 $m(F)=m(G)=\mathcal{B}(X)$。但这一结果并不能从定理1.2.1推得。由此可见，我们将经典的单调类定理进行推广是有意义的。

下面引进可测空间、可分 $\sigma$代数及原子集合概念.

定义1.2.7 设F为Ω上的一σ代数，称序偶(Ω, F)为一可测空间，F中的元称为F可测集．称σ代数F为可分的(或可数生成的)，如果存在F的一可数子类C，使得σ(C) = F．若F可分，称(Ω, F)为可分可测空间．

注意: 可分 $\sigma$代数的元素未必是可数多个.

由习题1.1.7及1.1.5易知：若F可分，则存在一代数C，其元素个数至多可数，使得 $\sigma(\mathcal{C})=\mathcal{F}$.

定义1.2.8 设 $(\Omega,\mathcal{F})$为可测空间，对任一 $\omega\in\Omega$，令

 
$$
\mathcal{F}_{\omega}=\{B\in\mathcal{F}\mid\omega\in B\},A(\omega)=\bigcap_{B\in\mathcal{F}_{\omega}}B,
$$
 

称 $A(\omega)$为含 $\omega$的F原子.

请读者证明下述结论：

(1) 设  $\omega, \omega' \in \Omega$，则或者  $A(\omega) = A(\omega')$，或者  $A(\omega) \cap A(\omega') = \varnothing$;

---

(2) 设C为生成F的代数. 对任何 $\omega \in \Omega$，令 $C_{\omega} = \{B \in C \mid \omega \in B\}$，则有

 
$$
A(\omega)=\bigcap_{B\in\mathcal{C}_{\omega}}B.
$$
 

特别, 若 F 可分, 则每个 F 原子属于 F.

定义1.2.9 一可测空间 $(E,\mathcal{E})$称为可离的, 如果它的每个原子都是单点集. 两个可测空间称为同构, 如果在两者之间存在一双方单值双方可测的满射(这样的映射称为可测同构).

下一引理表明: 任一可分且可离的可测空间同构于 $(\mathbb{R},\mathcal{B}(\mathbb{R}))$ 的某可测子空间.

引理1.2.10 设 $(E,\mathcal{E})$为一可分且可离的可测空间，则 $(E,\mathcal{E})$同构于 $(\mathbb{R},\mathcal{B}(\mathbb{R}))$的某可测子空间。更确切地说，设 $\{A_{n},n\geq1\}$为E上生成 $\mathcal{E}$的代数，令

 
$$
f(x)=\sum_{n=1}^{\infty}3^{-n}I_{A_{n}}(x),
$$
 

则 $f$为 $(E, \mathcal{E})$到 $(f(E), \mathcal{B}(f(E)))$上的可测同构．这里， $\mathcal{B}(f(E)) = f(E) \cap \mathcal{B}(\mathbb{R})$（见下面的习题1.2.1）．

证 显然  $f$ 为  $(E, \mathcal{E})$ 到  $(f(E), \mathcal{B}(f(E)))$ 上的双方单值可测映射. 为证  $f^{-1}$ 可测, 只需证  $f^{-1}(\mathcal{B}(f(E))) = \mathcal{E}$. 由于  $(A_n)$ 在  $E$ 上生成  $\mathcal{E}$, 只需证每个  $A_n$ 属于  $f^{-1}(\mathcal{B}(f(E)))$. 令  $G_n$ 表示  $[0, \frac{1}{2}]$ 中三进位展开中第  $n$ 项为 1 的实数全体, 即  $G_1 = [\frac{1}{3}, \frac{1}{2}]$,

 
$$
\begin{align*}G_{n}=&\Big[\frac{1}{3^{n}},\frac{1}{2\cdot3^{n-1}}\Big]\bigcup\Big[\frac{1}{3^{n}}+\frac{1}{3^{n-1}},\frac{1}{2\cdot3^{n-1}}+\frac{1}{3^{n-1}}\Big]\\&\bigcup\cdots\bigcup\Big[\frac{1}{3^{n}}+\cdots+\frac{1}{3},\frac{1}{2\cdot3^{n-1}}+\cdots+\frac{1}{3}\Big],\ n\geqslant2,\end{align*}
$$
 

则 $G_n \in \mathcal{B}(\mathbb{R})$，从而 $G_n \cap f(E) \in \mathcal{B}(f(E))$。我们有 $A_n = f^{-1}(G_n) = f^{-1}(G_n \cap f(E))$，由此推得引理的结论。

##### 习题

1.2.1 设C为Ω上的一集类， $A \subset \Omega$。令

 
$$
A\cap\mathcal{C}=\{A\cap B\mid B\in\mathcal{C}\}
$$
 

(这一记号以后常用到)，并用 $\sigma_{A}(A\cap C)$表示 $A\cap C$（视为A上集类）在A上生成的 $\sigma$代数，则有

 
$$
\sigma_{A}(A\cap\mathcal{C})=A\cap\sigma(\mathcal{C}).
$$
 

对 $m(C)$和 $\lambda(C)$亦有类似结果.

---

1.2.2 设F为Ω上的一σ代数,  $C = \{A_1, A_2, \cdots\}$ 为Ω的一个可数划分(即 $A_n \cap A_m = \varnothing$,  $n \neq m$,  $\sum_n A_n = \Omega$), 则对任何 $B \in \sigma(\mathcal{F} \cup \mathcal{C})$, 存在 $B_n \in \mathcal{F}$,  $n = 1, 2, \cdots$, 使得

 
$$
B=\sum_{n=1}^{\infty}(B_{n}\cap A_{n}).
$$
 

1.2.3 设C为一集类. 则对任何 $A \in \sigma(\mathcal{C})$, 存在C的可数子类 $\mathcal{D}$, 使得 $A \in \sigma(\mathcal{D})$.

1.2.4 设C为一集类，则对任何 $A \in m(\mathcal{C})$，存在 $B \in \mathcal{C}_\sigma$，使得 $B \supset A$（提示：令 $\mathcal{G}$表示具有所说性质的集合A全体，证明 $\mathcal{G}$为单调类）。

1.2.5 设 C 为一集类. 如果

 
$$
A,B\in\mathcal{C}\Rightarrow A\cup B\in\mathcal{C}_{\Sigma\sigma},
$$
 

则有 $\lambda(\mathcal{C})=\sigma(\mathcal{C})$ (提示: 利用习题1.1.6).

## 1.3 测度与非负集函数

学过实分析的人都知道: Lebesgue测度是线段长度概念的延伸(或更一般地, 是欧氏空间中面积或体积概念的延伸). 下面我们将要引入的测度概念则是Lebesgue测度的抽象化.

定义1.3.1 设 $(\Omega,\mathcal{F})$为一可测空间， $\mu$为定义于 $\mathcal{F}$取值于 $\mathbb{R}_{+}=[0,\infty]$的函数。如果 $\mu(\varnothing)=0$且 $\mu$有可数可加性或 $\sigma$可加性，即

 
$$
\begin{aligned}A_{n}\in\mathcal{F},n\geqslant1,A_{n}\cap A_{m}=\varnothing,n\neq m\Rightarrow\\\mu\big(\sum_{n=1}^{\infty}A_{n}\big)=\sum_{n=1}^{\infty}\mu(A_{n}),\end{aligned}
$$
 

则称 $\mu$为 $\Omega$上的(或 $(\Omega,\mathcal{F})$上的)测度.

设 $\mu$为可测空间 $(\Omega,\mathcal{F})$上的测度，称三元组 $(\Omega,\mathcal{F},\mu)$为测度空间。若 $\mu(\Omega)<\infty$，则称 $\mu$为有限测度，并称 $(\Omega,\mathcal{F},\mu)$为有限测度空间。若 $\mu(\Omega)=1$，则称 $\mu$为概率测度，并称 $(\Omega,\mathcal{F},\mu)$为概率空间。若存在 $A_{n}\in\mathcal{F},n\geq1$，使得 $\bigcup_{n}A_{n}=\Omega$，且使 $\mu(A_{n})<\infty$对一切 $n\geq1$成立（由1.5知，可取 $(A_{n})$为 $\Omega$的一个划分），则称 $\mu$为 $\sigma$有限测度，并称 $(\Omega,\mathcal{F},\mu)$为 $\sigma$有限测度空间。

设 $(\Omega,\mathcal{F},\mu)$为一测度空间. 若 $A\in\mathcal{F}$，且 $\mu(A)=0$，称 $A$为 $\mu$零测集. 如果任何 $\mu$零测集的子集皆属于 $\mathcal{F}$，称 $\mathcal{F}$关于 $\mu$是完备的，称 $(\Omega,\mathcal{F},\mu)$为完备测度空间.

为了下节研究测度的扩张的需要, 我们引进一般的非负集函数的概念. 设C为任一集类. 定义于C取值于 $\mathbb{R}_+$的函数称为C上的非负集函数. 在下面的定义叙述中, 我们总约定 $\varnothing \in \mathcal{C}$, 且非负集函数 $\mu$满足  $\mu(\varnothing) = 0$及单调性 :

 
$$
A,\;B\in\mathcal{C},A\subset B\Rightarrow\mu(A)\leqslant\mu(B).
$$
 

---

定义1.3.2 设 $\mu$为C上非负集函数.

(1) 称  $\mu$ 为有限可加的，如果对一切  $n \geqslant 2$，

 
$$
A_{i}\in\mathcal{C},1\leqslant i\leqslant n,\sum_{i=1}^{n}A_{i}\in\mathcal{C}\Rightarrow\mu\big(\sum_{i=1}^{n}A_{i}\big)=\sum_{i=1}^{n}\mu(A_{i}).
$$
 

(2) 称  $\mu$ 为  $\sigma$ 可加的, 如果

 
$$
A_{i}\in\mathcal{C},i\geqslant1,\sum_{i=1}^{\infty}A_{i}\in\mathcal{C}\Rightarrow\mu\big(\sum_{i=1}^{\infty}A_{i}\big)=\sum_{i=1}^{\infty}\mu(A_{i}).
$$
 

(3) 称  $\mu$ 为半  $\sigma$ 可加的，如果

 
$$
A\in\mathcal{C};A_{i}\in\mathcal{C},i\geqslant1, 且 A\subset\bigcup_{i=1}^{\infty}A_{i}\Rightarrow\mu(A)\leqslant\sum_{i=1}^{\infty}\mu(A_{i}).
$$
 

(4) 称  $\mu$ 从下连续, 如果

 
$$
A_{n}\in\mathcal{C},A_{n}\uparrow A\in\mathcal{C}\Rightarrow\mu(A)=\lim_{n\to\infty}\mu(A_{n}).
$$
 

(5) 称  $\mu$ 从上连续, 如果

 
$$
A_{n}\in\mathcal{C},A_{n}\downarrow A\in\mathcal{C}, 且 \mu(A_{1})<\infty\Rightarrow\mu(A)=\lim_{n\to\infty}\mu(A_{n}).
$$
 

(6) 称  $\mu$ 在空集处连续, 如果

 
$$
A_{n}\in\mathcal{C},A_{n}\downarrow\varnothing, 且 \mu(A_{1})<\infty\Rightarrow\lim_{n\rightarrow\infty}\mu(A_{n})=0.
$$
 

(7) 称  $\mu$ 在  $\mathcal{C}$ 上有限，如果对一切  $A \in \mathcal{C}$，有  $\mu(A) < \infty$.

(8) 称  $\mu$ 在  $\mathcal{C}$ 上  $\sigma$ 有限，如果对任一  $A \in \mathcal{C}$，存在  $A_n \in \mathcal{C}, n \geq 1$，使得  $A \subset \bigcup_n A_n$，且  $\mu(A_n) < \infty$ 对一切  $n$ 成立。

这些概念都是可以“顾名思义”的，读者很容易记住它们。

下一定理概括了测度的最基本性质.

定理1.3.3 设 $\mu$为可测空间 $(\Omega,\mathcal{F})$上一测度，则 $\mu$从下连续且从上连续(从而也在 $\varnothing$处连续).此外， $\mu$有单调性及如下的可减性：

 
$$
A,B\in\mathcal{F},A\subset B, 且 \mu(B)<\infty\Rightarrow\mu(B\setminus A)=\mu(B)-\mu(A).
$$
 

证 单调性及可减性是显然的. 由可减性及从下连续性立刻推得从上连续性, 只需证  $\mu$ 的从下连续性. 设  $A_{n} \in \mathcal{F}, n \geq 1, A_{n} \uparrow A.$ 为证  $\lim_{n \to \infty} \mu(A_{n}) = \mu(A)$, 不妨设  $\forall n \geq 1$, 有  $\mu(A_{n}) < \infty$, 则有

 
$$
\mu(A_{n+1}\setminus A_{n})=\mu(A_{n+1})-\mu(A_{n}).
$$
 

---

由于 $A=\bigcup_{n}A_{n}=A_{1}\cup\sum_{n=1}^{\infty}(A_{n+1}\setminus A_{n})$，故有

 
$$
\mu(A)=\mu(A_{1})+\sum_{n=1}^{\infty}[\mu(A_{n+1})-\mu(A_{n})]=\lim_{n\to\infty}\mu(A_{n}).
$$
 

下一定理推广了定理1.3.3的结论.

定理1.3.4 设C为一代数，μ为C上的有限可加非负集函数，则μ有单调性及可减性. 此外，μ为σ可加⇔μ从下连续⇒μ从上连续⇒μ在σ处连续. 若进一步μ(Ω)＜∞，则上述诸条件等价.

证 设μ从下连续，往证μ为σ可加的. 令 $A_{n}\in\mathcal{C},n\geq1$，且 $\sum_{n=1}^{\infty}A_{n}\in\mathcal{C}$，则 $B_{m}=\sum_{n=1}^{m}A_{n}\in\mathcal{C}$，且 $B_{m}\uparrow\sum_{n=1}^{\infty}A_{n}$. 于是由μ的有限可加性及从下连续性得

 
$$
\mu\big(\sum_{n=1}^{\infty}A_{n}\big)=\lim_{m\to\infty}\mu\big(\sum_{n=1}^{m}A_{n}\big)=\lim_{m\to\infty}\sum_{n=1}^{m}\mu(A_{n})=\sum_{n=1}^{\infty}\mu(A_{n}).
$$
 

这表明 $\mu$有 $\sigma$可加性.其余结论显然(参见上一定理的证明).

下一引理将使我们在许多场合把与 $\sigma$有限测度有关的问题归结为与概率测度有关的问题.

引理1.3.5 设μ为可测空间(Ω, F)上的σ有限测度. 若μ(Ω) > 0, 令{Aₙ, n ≥ 1}为Ω的一个可数划分, 使得∀n, Aₙ ∈ ℝ, 且0 < μ(Aₙ) < ∞. 又令

$$
\nu(A)=\sum_{n=1}^{\infty}\frac{\mu(A\cap A_{n})}{2^{n}\mu(A_{n})},\;A\in\mathcal{F},   \tag*{(1.3.1)}
$$

则ν为(Ω, F)上的一概率测度, 此外有ν(A) = 0 ⇔ μ(A) = 0, 并且对任何A ∈ F, 有

$$
\mu(A)=\sum_{n=1}^{\infty}2^{n}\nu(A\cap A_{n})\mu(A_{n}).   \tag*{(1.3.2)}
$$

证 只需证(1.3.2)式, 其余结论显然. 在(1.3.1)式中令  $A \cap A_{m}$ 代替 A, 得

 
$$
\nu(A\cap A_{m})=\frac{\mu(A\cap A_{m})}{2^{m}\mu(A_{m})}.
$$
 

由此立得 $(1.3.2)$式.

##### 习题

1.3.1 设  $\mu$ 为半环 C 上的一有限可加非负函数，则  $\mu$ 有单调性及可减性．此外，设  $A_n \in C$， $n \geq 1$， $A \in C$，且  $\sum_n A_n \subset A$，则有  $\sum_{n=1}^{\infty} \mu(A_n) \leq \mu(A)$．

---

1.3.2 设 $(I, \prec)$为一定向集， $(\mu_i, i \in I)$为 $\sigma$代数 $\mathcal{F}$上的一族测度，满足 $i \prec j \Rightarrow \mu_i \leqslant \mu_j$。令

 
$$
\mu(A)=\sup_{i}\mu_{i}(A),\quad A\in\mathcal{F},
$$
 

则 $\mu$为 $\mathcal{F}$上的测度.

1.3.3 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $\mu(\Omega)<\infty$， $\mathcal{C}$为生成 $\mathcal{F}$的一个代数，则对任何 $A\in\mathcal{F}$，我们有

 
$$
\mu(A)=\sup\{\mu(B)\mid B\in\mathcal{C}_{\delta},B\subset A\}=\inf\{\mu(B)\mid B\in\mathcal{C}_{\sigma},B\supset A\}.
$$
 

(提示: 令 G 表示 F 中使上式成立的集 A 全体, 证明 G 为单调类, 再利用单调类定理.)

1.3.4 设 $(\Omega, \mathcal{F}, \mu)$为一有限测度空间， $C$为生成 $\mathcal{F}$的一个代数．若 $A \in \mathcal{F}$，则 $\forall \varepsilon > 0$，存在 $B \in \mathcal{C}$，使得 $\mu(A \triangle B) < \varepsilon$（提示：利用习题1.3.3）.

## 1.4 外测度与测度的扩张

本节研究如何把一半环C上的一σ可加非负集函数扩张成为σ代数σ(C)上的测度, 通常采用的方法是外测度方法.

定义1.4.1 令  $\mathcal{A}(\Omega)$ 表示  $\Omega$ 的所有子集 (包括空集) 所构成的集类，设  $\mu$ 为  $\mathcal{A}(\Omega)$ 上的一非负集函数 (约定  $\mu(\varnothing) = 0$)。如果  $\mu$ 有单调性并满足如下的次  $\sigma$ 可加性：

 
$$
A_{n}\subset\Omega,n\geqslant1\Rightarrow\mu\big(\bigcup_{n}A_{n}\big)\leqslant\sum_{n}\mu(A_{n}),
$$
 

则称 $\mu$为 $\Omega$上的一外测度.

下一定理是测度扩张的基础.

定理1.4.2 设 $\mu$为 $\Omega$上的一外测度. 令

$$
\mathcal{U}=\{A\subset\Omega\mid\forall D\subset\Omega, 有 \mu(D)=\mu(A\cap D)+\mu(A^{c}\cap D)\},   \tag*{(1.4.1)}
$$

则 $u$为 $\Omega$上的一 $\sigma$代数，且 $\mu$限于 $u$为一测度。我们称 $u$中的元素为 $\mu$可测集。

证 首先注意: 为要  $A \in \mathcal{U}$, 当且仅当  $\forall D \subset \Omega$.

$$
\mu(D)\geqslant\mu(A\cap D)+\mu(A^{c}\cap D).   \tag*{(1.4.2)}
$$

设 $A, B \in \mathcal{U}$，则由(1.4.1)式及 $\mu$的次可加性知： $\forall D \subset \Omega$，

 
$$
\begin{align*}\mu(D)&=\mu(A\cap D)+\mu(A^{c}\cap D)\\&=\mu(A\cap D)+\mu(B\cap A^{c}\cap D)+\mu(B^{c}\cap A^{c}\cap D)\\&\geqslant\mu((A\cup B)\cap D)+\mu((A\cup B)^{c}\cap D).\end{align*}
$$
 

这表明 $A \cup B \in \mathcal{U}$. 此外，由(1.4.1)式知， $A \in \mathcal{U} \Rightarrow A^c \in \mathcal{U}$，故 $\mathcal{U}$为一代数.

---

往证U为σ代数，且μ限于U为一测度.为此，设 $A_n \in \mathcal{U}, n \geq 1, A_n \cap A_m = \varnothing,$  $n \neq m$，则对任何 $D \subset \Omega$，我们有(注意 $A_k \cap A_{k-1}^c \cap \cdots \cap A_1^c = A_k$)

 
$$
\begin{align*}\mu(D)&=\mu(A_{1}\cap D)+\mu(A_{1}^{c}\cap D)\\&=\mu(A_{1}\cap D)+\mu(A_{2}\cap D)+\mu(A_{2}^{c}\cap A_{1}^{c}\cap D)=\cdots\\&=\sum_{k=1}^{n}\mu(A_{k}\cap D)+\mu\big(\big(\sum_{k=1}^{n}A_{k})^{c}\cap D\big)\\&\geq\sum_{k=1}^{n}\mu(A_{k}\cap D)+\mu\big(\big(\sum_{k=1}^{\infty}A_{k})^{c}\cap D\big).\end{align*}
$$
 

在上式中令 $n \to \infty$，并由 $\mu$的次 $\sigma$可加性立得

 
$$
\begin{align*}\mu(D)&\geq\sum_{k=1}^{\infty}\mu(A_{k}\cap D)+\mu\big((\sum_{k=1}^{\infty}A_{k})^{c}\cap D\big)\\&\geq\mu\big((\sum_{k=1}^{\infty}A_{k})\cap D\big)+\mu\big((\sum_{k=1}^{\infty}A_{k})^{c}\cap D\big).\end{align*}
$$
 

这表明 $\sum_{k=1}^{\infty}A_{k}\in\mathcal{U}$. 此外，在上式中令 $D=\sum_{k=1}^{\infty}A_{k}$得

 
$$
\mu(\sum_{k=1}^{\infty}A_{k})=\sum_{k=1}^{\infty}\mu(A_{k}).
$$
 

因此, $u$为一 $\sigma$代数,且 $\mu$限于 $u$为一测度.

下一命题的证明是不足道的, 故从略.

命题1.4.3 设C为Ω上一集类, 且∅∈C. 又设μ为C上的一半σ可加非负集函数, 且μ(∅)=0. 令

$$
\mu^{*}(A)=\inf\Big\{\sum_{n=1}^{\infty}\mu(A_{n})\Big|A_{n}\in\mathcal{C},A\subset\bigcup_{n=1}^{\infty}A_{n}\Big\},A\subset\Omega   \tag*{(1.4.3)}
$$

(这里及今后, 约定 $\inf \varnothing = +\infty$), 则 $\mu^*$为 $\Omega$上的外测度, 且 $\mu^*$限于 $\mathcal{C}$与 $\mu$一致, 我们称 $\mu^*$为由 $\mu$引出的外测度.

命题1.4.4 设μ为半环C上的一非负集函数(约定μ(∅)=0). 则为要μ是σ可加的, 必须且只需μ为有限可加且半σ可加的.

证 先证必要性. 设  $\mu$ 为  $\sigma$ 可加, 显然  $\mu$ 为有限可加. 令  $A \in C, A_n \in C, n \geq 1$, 且  $A \subset \bigcup_n A_n$, 往证  $\mu(A) \leq \sum_{n=1}^{\infty} \mu(A_n)$. 令

 
$$
B_{1}=A_{1},B_{n}=A_{n}A_{1}^{c}\cdots A_{n-1}^{c},\quad n\geqslant2,
$$
 

---

则由半环定义知 $B_n \in \mathcal{C}_{\Sigma f}$（记号见1.1.6），且有 $\bigcup_n A_n = \sum_n B_n$，从而 $A = \sum_{n=1}^{\infty} (B_n \cap A)$。由于 $B_n \cap A \in \mathcal{C}_{\Sigma f}$，故存在 $C_{n,m} \in \mathcal{C}, 1 \leqslant m \leqslant k(n)$，使得

 
$$
B_{n}\cap A=\sum_{m=1}^{k(n)}C_{n,m},\quad n\geqslant1.
$$
 

由 $\mu$的 $\sigma$可加性推知

 
$$
\mu(A)=\sum_{n=1}^{\infty}\sum_{m=1}^{k(n)}\mu(C_{n,m}).
$$
 

但由于 $A_n \supset \sum_m C_{n,m}, A_n \setminus \sum_m C_{n,m} = A_n \cap (\bigcap_m C_{n,m}^c) \in \mathcal{C}_{\Sigma f}$，故由 $\mu$的有限可加性易知

 
$$
\mu(A_{n})\geqslant\sum_{m=1}^{k(n)}\mu(C_{n,m}).
$$
 

因此有 $\mu(A)\leqslant\sum_{n=1}^{\infty}\mu(A_{n})$，此即 $\mu$的半 $\sigma$可加性.

现证充分性. 设  $\mu$ 有限可加且半  $\sigma$ 可加. 设  $A_{n} \in \mathcal{C}, n \geqslant 1$,  $\sum_{n} A_{n} = A \in \mathcal{C}$, 我们要证  $\mu(A) = \sum_{n} \mu(A_{n})$. 由于对一切  $k \geqslant 1$,  $A \setminus \sum_{n=1}^{k} A_{n} \in \mathcal{C}_{\Sigma f}$, 故由  $\mu$ 的有限可加性知  $\mu(A) \geqslant \sum_{n=1}^{k} \mu(A_{n})$. 但 k 是任意的, 故  $\mu(A) \geqslant \sum_{n=1}^{\infty} \mu(A_{n})$. 再由  $\mu$ 的半  $\sigma$ 可加性知  $\mu(A) = \sum_{n=1}^{\infty} \mu(A_{n})$.

下一引理给出了 $\mu^{*}$可测集的一个刻画.

引理1.4.5 设C为Ω上的一集类，且 $\varnothing \in C$。又设 $\mu$为C上的一半 $\sigma$可加非负集函数，且 $\mu(\varnothing) = 0$， $\mu^*$为 $\mu$引出的外测度。则为要A为 $\mu^*$可测集，必须且只需对一切 $C \in C$，有

$$
\mu(C)\geqslant\mu^{*}(C\cap A)+\mu^{*}(C\cap A^{c})( 或者等价地 , 等号成立 ).   \tag*{(1.4.4)}
$$

证 只需证充分性. 设  $A \subset \Omega$, 且对一切  $C \in \mathcal{C}$,  $(1.4.4)$ 式成立. 任取  $D \subset \Omega$. 若  $\mu^{*}(D) = \infty$, 显然  $(1.4.2)$ 式成立  $(\mu^{*}$ 代替  $\mu)$. 若  $\mu^{*}(D) < \infty$, 则由  $\mu^{*}$ 的定义, 对任给  $\varepsilon > 0$, 可取  $A_{n} \in \mathcal{C}, n \geq 1$, 使得  $\bigcup_{n} A_{n} \supset D$, 且  $\mu^{*}(D) \geq \sum_{n=1}^{\infty} \mu(A_{n}) - \varepsilon$. 于是由  $(1.4.4)$ 式及  $\mu^{*}$ 的次  $\sigma$ 可加性有

 
$$
\begin{align*}\mu^{*}(D)&\geq\sum_{n}\Big[\mu^{*}(A_{n}\cap A)+\mu^{*}(A_{n}\cap A^{c})\Big]-\varepsilon\\&\geq\mu^{*}\Big(\big(\bigcup_{n}A_{n}\big)\cap A\Big)+\mu^{*}\Big(\big(\bigcup_{n}A_{n}\big)\cap A^{c}\Big)-\varepsilon\\&\geq\mu^{*}(D\cap A)+\mu^{*}(D\cap A^{c})-\varepsilon.\end{align*}
$$
 

由于ε > 0是任意的, 故有(1.4.2)式成立(以μ*代替μ). 这表明A为μ*可测集.

下一引理是应用单调类定理的一个典型例子,我们在讨论测度扩张的唯一性时将用到它.

---

引理1.4.6 设C为Ω上的一π类，μ₁及μ₂为σ(C)上的两个有限测度. 若Ω ∈ C, 且μ₁与μ₂限于C一致, 则μ₁与μ₂在σ(C)上一致.

证 令  $\mathcal{G} = \{A \in \sigma(\mathcal{C}) \mid \mu_1(A) = \mu_2(A)\}$，则由定理1.3.3知  $\mathcal{G}$ 为  $\lambda$ 类。但依假定，有  $\mathcal{G} \supset \mathcal{C}$，故由单调类定理知  $\mathcal{G} \supset \sigma(\mathcal{C})$，从而  $\mathcal{G} = \sigma(\mathcal{C})$。

下一定理称为Carathéodory 测度扩张定理.

定理1.4.7 设C为Ω上的一半环，μ为C上的一σ可加非负集函数，则μ可以扩张成为σ(C)上的一测度。若进一步μ在C上为σ有限，且Ω ∈ Cσ，则这一扩张是唯一的，并且扩张所得的测度在σ(C)上也是σ有限的。

证 由命题1.4.4，μ在C上有半σ可加性．令μ*为μ按(1.4.3)式引出的外测度，令U为μ*可测集全体．现设A∈C，往证A∈U．对任何C∈C，我们有C∩A²=∑n=1nBₙ，其中B₁，⋯，Bₙ∈C，B₁∩Bₙ=∅，i≠j，于是有

 
$$
\mu^{*}(C\cap A^{c})\leqslant\sum_{i=1}^{n}\mu(B_{i}).
$$
 

但我们有 $C=(C\cap A)\cup\sum_{i=1}^{n}B_{i}$，故由 $\mu$的有限可加性得

 
$$
\begin{align*}\mu(C)&=\mu(C\cap A)+\sum_{i=1}^{n}\mu(B_{i})\\&\geqslant\mu^{*}(C\cap A)+\mu^{*}(C\cap A^{c}),\end{align*}
$$
 

由引理1.4.5便知 $A \in \mathcal{U}$. 最终我们有 $\sigma(\mathcal{C}) \subset \mathcal{U}$. 令 $\tilde{\mu}$为 $\mu^*$在 $\sigma(\mathcal{C})$上的限制，则 $\tilde{\mu}$为 $\sigma(\mathcal{C})$上的测度. 显然 $\tilde{\mu}$与 $\mu$在 $\mathcal{C}$上一致，即 $\tilde{\mu}$为 $\mu$到 $\sigma(\mathcal{C})$上的扩张.

现假定μ在C上σ有限，且Ω ∈ Cσ。由于C是半环，不难证明存在Ω的一个可数划分(Aₙ)，使得Aₙ ∈ C, μ(Aₙ) < ∞, n ≥ 1，且Ω = ∑ₙ=₁ Aₙ。设μ₁与μ₂为μ到σ(C)上的两个测度扩张，则由于Aₙ ∩ C为π类，且Aₙ ∩ C ⊂ C，故由习题1.2.1和引理1.4.6知，μ₁与μ₂在Aₙ ∩ σ(C)上一致，从而μ₁与μ₂在σ(C)上一致。

定理1.4.8 设 $(\Omega,\mathcal{F},\mu)$为一测度空间, $\mathcal{N}$为 $\Omega$上的一集类.假定 $\mathcal{N}$满足如下条件: $(1)$  $A\in\mathcal{N},B\subset A\Rightarrow B\in\mathcal{N};(2)\mathcal{N}_\sigma=\mathcal{N};(3)$  $A\in\mathcal{N}\cap\mathcal{F}\Rightarrow\mu(A)=0.$ 令

 
$$
\overline{\mathcal{F}}=\{A\subset\Omega\mid\exists B\in\mathcal{F}, 使 A\triangle B\in\mathcal{N}\},
$$
 

 
$$
\overline{{\mu}}(A)=\mu(B),~B\in\mathcal{F},~A\triangle B\in\mathcal{N},\quad A\in\overline{{\mathcal{F}}},
$$
 

则 $\overline{F}$为 $\sigma$代数， $\overline{\mu}$为 $\overline{F}$上的测度.

证 我们只证 $\overline{\mu}$在 $\overline{F}$上的定义是唯一确定的,其余结论容易证明.为此,设 $A\in\overline{F}$, $B_{1},B_{2}\in\mathcal{F}$,使得 $A\triangle B_{1}\in\mathcal{N},A\triangle B_{2}\in\mathcal{N}$.由于

 
$$
(B_{1}\triangle B_{2})\cap A^{c}\subset(B_{1}\cup B_{2})\cap A^{c}\subset(A\triangle B_{1})\cup(A\triangle B_{2}),
$$
 

---

 
$$
(B_{1}\triangle B_{2})\cap A\subset(B_{1}^{c}\cup B_{2}^{c})\cap A\subset(A\triangle B_{1})\cup(A\triangle B_{2}),
$$
 

故有 $(B_1\triangle B_2) \in \mathcal{N}$. 但 $(B_1\triangle B_2) \in \mathcal{F}$, 于是 $\mu(B_1\triangle B_2) = 0$, 从而有 $\mu(B_1) = \mu(B_2)$.

定义1.4.9 设 $(\Omega,\mathcal{F},\mu)$为一测度空间. 令

 
$$
\mathcal{N}=\{N\subset\Omega\mid\exists A\in\mathcal{F},\mu(A)=0, 使 A\supset N\},
$$
 

则N满足定理1.4.8的条件.于是 $(\Omega,\overline{F},\overline{\mu})$为一测度空间，它是包含 $(\Omega,\mathcal{F},\mu)$的最小完备测度空间.我们称 $(\Omega,\overline{F},\overline{\mu})$为 $(\Omega,\mathcal{F},\mu)$的完备化，称 $\overline{F}$为 $\mathcal{F}$的 $\mu$完备化.此外，我们有

 
$$
\overline{{\mathcal{F}}}=\{A\cup N\mid A\in\mathcal{F},N\in\mathcal{N}\},
$$
 

 
$$
\overline{{\mu}}(A\cup N)=\mu(A),\quad A\in\mathcal{F},N\in\mathcal{N}.
$$
 

##### 习题

1.4.1 (测度的限制) 设 $(\Omega, \mathcal{F}, \mu)$为一有限测度空间， $\Omega_0 \subset \Omega, \mu^*(\Omega_0) = \mu(\Omega)$。则 $\forall A \in \mathcal{F}$有 $\mu^*(A \cap \Omega_0) = \mu(A)$，并且 $\mu^*$限于 $\Omega_0 \cap \mathcal{F}$为一测度。称 $\mu^*$为 $\mu$到 $(\Omega_0, \Omega_0 \cap \mathcal{F})$上的限制。

1.4.2 设 $(\Omega,\mathcal{F},\mu)$为一有限测度空间， $\Omega_{0}\subset\Omega$。令 $\mathcal{F}_{0}=\Omega_{0}\cap\mathcal{F}$，

 
$$
\nu(A)=\inf\{\mu(G)\mid G\in\mathcal{F},G\cap\Omega_{0}=A\},\ A\in\mathcal{F}_{0},
$$
 

则 $\nu$为 $(\Omega_{0},\mathcal{F}_{0})$上一测度.令

 
$$
\tilde{\mu}(B)=\nu(B\cap\Omega_{0}),\ \forall B\in\mathcal{F},
$$
 

则 $\tilde{\mu}$为 $(\Omega,\mathcal{F})$上一测度，且 $\tilde{\mu}\leq\mu$.

1.4.3 设 $(\Omega,\mathcal{F},\mu)$为一有限测度空间， $\{A_{n},n\geq1\}$为 $\mathcal{F}$中的极限存在的序列，则

 
$$
\lim_{n\to\infty}\mu(A_{n})=\mu(\lim_{n\to\infty}A_{n}).
$$
 

1.4.4 设 $(\Omega,\mathcal{F},\mu)$为一测度空间. 令

 
$$
\mu^{*}(A)=\inf\{\mu(B)\mid B\supset A,B\in\mathcal{F}\},A\subset\Omega,
$$
 

则 $\mu^*$为 $\Omega$上的外测度。令 $\mathcal{U}$为 $\mu^*$可测集全体，则 $(\Omega,\mathcal{U},\mu^*)$为完备测度空间。若 $(\Omega,\mathcal{F},\mu)$为一 $\sigma$有限测度空间，则 $\mathcal{U}$为 $\mathcal{F}$的 $\mu$完备化。

1.4.5 设 $(\Omega,\mathcal{F},\mu)$为一完备测度空间, $\mathcal{N}=\{A\in\mathcal{F}|\mu(A)=0\}$. 设 $\mathcal{G}$为 $\mathcal{F}$的子 $\sigma$代数,令

 
$$
\widetilde{\mathcal{G}}=\{A\subset\Omega\mid\exists B\in\mathcal{G}, 使 A\triangle B\in\mathcal{N}\},
$$
 

 
$$
\widetilde{\mu}(A)=\mu(B),B\in\mathcal{G},A\triangle B\in\mathcal{N},\quad A\in\widetilde{\mathcal{G}},
$$
 

则 $\widetilde{\mathcal{G}}=\sigma(\mathcal{G}\cup\mathcal{N})$，且 $\widetilde{\mu}$为 $\widetilde{\mathcal{G}}$上的测度。

---

### 1.5 欧氏空间中的Lebesgue-Stieltjes测度

本节将利用上节的结果来建立 $^{R^{n}}$上的Lebesgue-Stieltjes 测度. 为此, 我们先引进若干记号.

设 $a=(a_{1},\cdots,a_{n})$与 $b=(b_{1},\cdots,b_{n})$为 $\mathbb{R}^{n}$中的两个点.若对一切 $i\in\mathbb{R}^{n}$的 $\frac{a_{i}}{b_{i}}\leq b_{i}$ (相应地, $a_{i}<b_{i}$),则记为 $a\leq b$ (相应地, $a<b$).设 $a\leq b$,我们令

 
$$
\mathcal{C}=\{(a,b)\mid a\leqslant b,\;a,b\in\mathbb{R}^{n}\},
$$
 

 
$$
\mu((a,b])=\prod_{i=1}^{n}(b_{i}-a_{i}).
$$
 

引理1.5.1 C为 $R^{n}$上的半环，且 $\mu$为C上的 $\sigma$可加非负集函数.

证 C显然为半环. 由归纳法易证μ在C上是有限可加的(直观上看, 体积具有有限可加性). 为证μ在C上为σ可加的, 只需证μ为半σ可加的(命题1.4.4). 为此, 设

 
$$
I=(a,b],I_{i}=(a^{(i)},b^{(i)}],
$$
 

其中 $a < b, a^{(i)} < b^{(i)}$，且 $I \subset \bigcup_i I_i$。对任给 $\varepsilon > 0$，存在 $\overline{a}, \overline{b}^{(i)}$，满足 $a < \overline{a} < b$及 $\overline{b}^{(i)} > b^{(i)}, i \geq 1$，使得

 
$$
\mu((\overline{a},b])\geqslant\mu((a,b])-\varepsilon,
$$
 

 
$$
\mu((a^{(i)},\overline{{b}}^{(i)}])\leqslant\mu((a^{(i)},b^{(i)}])+2^{-i}\varepsilon,\quad i=1,2,\cdots.
$$
 

由有限覆盖定理，存在自然数 $N \geq 1$，使得 $[\overline{a}, b] \subset \bigcup_{i=1}^{N} (a^{(i)}, \overline{b}^{(i)})$，从而有 $[\overline{a}, b] \subset \bigcup_{i=1}^{N} (a^{(i)}, \overline{b}^{(i)})]$，故有

 
$$
\begin{align*}\mu((a,b])-\varepsilon&\leqslant\mu((\overline{a},b])\leqslant\sum_{i=1}^{N}\mu((a^{(i)},\overline{b}^{(i)}])\\&\leqslant\sum_{i=1}^{\infty}\mu((a^{(i)},b^{(i)}))+\varepsilon.\end{align*}
$$
 

令 $\varepsilon\downarrow0$得 $\mu(I)\leqslant\sum_{i=1}^{\infty}\mu(I_{i})$， $\mu$的半 $\sigma$可加性得证.

令 $\mathcal{B}(\mathbb{R}^n)$为 $\mathbb{R}^n$上的Borel  $\sigma$代数. 易知： $\sigma(C) = \mathcal{B}(\mathbb{R}^n)$. 于是由测度扩张定理立得如下的定理.

定理1.5.2  $\mu$可以唯一地扩张成为 $B(\mathbb{R}^n)$上的 $\sigma$有限测度(称之为Lebesgue测度).

令 $\overline{B(\mathbb{R}^n)}$为 $\mathcal{B}(\mathbb{R}^n)$的 $\mu$完备化，称 $\overline{B(\mathbb{R}^n)}$中元为Lebesgue可测集，而 $\mathcal{B}(\mathbb{R}^n)$中的元称为Borel可测集。

---

定义1.5.3 设 $F$为 $\mathbb{R}^n$上的一右连续实值函数，对 $a,b\in\mathbb{R}^n$， $a\leq b$，令

 
$$
\triangle_{b,a}F=\triangle_{b_{1},a_{1}}\triangle_{b_{2},a_{2}}\cdots\triangle_{b_{n},a_{n}}F,
$$
 

其中

 
$$
\triangle_{b_{i},a_{i}}G(\cdot)=G(\cdot,b_{i})-G(\cdot,a_{i}),\quad1\leqslant i\leqslant n.
$$
 

如果对一切 $a \leqslant b$，有 $\triangle_{b,a}F \geqslant 0$，称F为增函数.

设 $\mu$为 $\mathcal{B}(\mathbb{R}^n)$上一 $\sigma$有限测度。称 $\mu$为Lebesgue-Stieltjes测度（简称为L-S测度），如果对任何 $C \in \mathcal{C}$，有 $\mu(C) < \infty$（即 $\mu$在 $\mathcal{C}$上有限）。下一定理表明： $\mathbb{R}^n$上的L-S测度与 $\mathbb{R}^n$上的右连续增函数之间有某种对应关系。

定理1.5.4 设 $F$为 $\mathbb{R}^n$上的一右连续增函数. 令

 
$$
\mu_{F}(\varnothing)=0,\ \mu_{F}((a,b])=\triangle_{b,a}F,\ a\leqslant b,\ a,b\in\mathbb{R}^{n},
$$
 

则$\mu_F$可以唯一地扩张成为$\mathbb{R}^n$上的Lebesgue-Stieltjes测度。反之，假设$\mu$为$\mathbb{R}^n$上的一L-S测度，则存在$\mathbb{R}^n$上的一右连续增函数$F$（但不唯一），使得$\mu$为$\mu_F$从$\mathcal{C}$到$\mathcal{B}(\mathbb{R}^n)$上的唯一扩张。

证 设 $F$ 为右连续增函数。与引理1.5.1类似可证：$\mu_F$为$C$上的一$\sigma$可加集函数，从而可以唯一地扩张成为$\mathcal{B}(\mathbb{R}^n)$上的测度。定理后半部分证明比较复杂，我们就省略了（如果$\mu$比较特殊，满足$\mu((-\infty, x]) < \infty, \forall x \in \mathbb{R}^n$，则令 $F(x) = \mu((-\infty, x])$即得所要的增函数，这至少对概率论来说是够用了）。

##### 习题

1.5.1 设$ \mu $为$ B(\mathbb{R}^n) $上一 Lebesgue-Stieltjes 测度,$ K $和$ G $分别为$ R^n $ 的紧子集和开子集全体, 则有

 
$$
\begin{align*}\mu(B)&=\sup\{\mu(K)\mid K\subset B,K\in\mathcal{K}\}\\&=\inf\{\mu(G)\mid B\subset G,G\in\mathcal{G}\},B\in\mathcal{B}(X).\end{align*}
$$
 

## 1.6 测度的逼近

设 $(\Omega,\mathcal{F},\mu)$为一测度空间．本节研究在什么条件下， $\mathcal{F}$可测集的测度可以通过 $\mathcal{F}$的一子类 $C$中的元素的测度来逼近．我们将在第5章研究拓扑空间上测度的正则性时用到这一结果．

---

引理1.6.1 设 $(\Omega,\mathcal{F},\mu)$为一测度空间，C为F的一子类. 令

 
$$
\mathcal{H}=\{A\in\mathcal{F}\mid\mu(A)=\operatorname*{s u p}[\mu(B)\mid B\in\mathcal{C}_{\delta},B\subset A]\},
$$
 

则 $H \supset C_\delta$，且 $H$有如下性质：

(1)  $A_n \in \mathcal{H}, n \geq 1, A_n \uparrow A \Rightarrow A \in \mathcal{H};$

 
$$
(2)A_{n}\in\mathcal{H},\mu(A_{n})<\infty,n\geqslant1\Rightarrow\bigcap A_{n}\in\mathcal{H}.
$$
 

特别, 若  $\mu$ 为有限测度, 则 H 为单调类, 且对可列交封闭.

证 (1) 设  $A_n \in \mathcal{H}, n \geq 1, A_n \uparrow A.$ 若  $\mu(A) = \infty$，则  $\mu(A_n) \uparrow \infty$，于是易从  $\mathcal{H}$ 的定义知  $A \in \mathcal{H}$。现设  $\mu(A) < \infty$。对任给  $\varepsilon > 0$，先取  $n_0$，使得  $\mu(A_{n_0}) \geq \mu(A) - \frac{\varepsilon}{2}$。再取  $B \in \mathcal{C}_\delta, B \subset A_{n_0}$，使得  $\mu(B) \geq \mu(A_{n_0}) - \frac{\varepsilon}{2}$。则有  $B \subset A$，且  $\mu(B) \geq \mu(A) - \varepsilon$，这表明  $A \in \mathcal{H}$。

(2) 设  $A_n \in \mathcal{H}$,  $\mu(A_n) < \infty, n \geq 1$. 对每个  $n \geq 1$, 令  $B_n \in \mathcal{C}_\delta, B_n \subset A_n$, 使得  $\mu(B_n) \geq \mu(A_n) - 2^{-n}\varepsilon$. 令  $B = \bigcap_n B_n$, 则  $B \in \mathcal{C}_\delta, B \subset \bigcap_n A_n$, 且有

 
$$
\begin{align*}\mu\big(\bigcap_{n}A_{n}\big)-\mu(B)&=\mu\big(\bigcap_{n}A_{n}\setminus\bigcap_{n}B_{n}\big)\leqslant\mu\big(\bigcup_{n}(A_{n}\setminus B_{n})\big)\\&\leqslant\sum_{n}[\mu(A_{n})-\mu(B_{n})]\leqslant\varepsilon,\end{align*}
$$
 

这表明 $\bigcap_n A_n \in \mathcal{H}$.

引理1.6.2 设 $(\Omega,\mathcal{F},\mu)$为一有限测度空间， $\mathcal{D}$为 $\mathcal{F}$的一子类.令

 
$$
\mathcal{G}=\Big\{A\in\mathcal{F}\big|\mu(A)=\operatorname*{i n f}\{\mu(B)\mid B\in\mathcal{D}_{\sigma},B\supset A\}\Big\},
$$
 

则 $\mathcal{G} \supset \mathcal{D}_\sigma$,  $\mathcal{G}$为单调类, 且对可列并封闭.

证 令  $C = \{D^c, D \in \mathcal{D}\}$，并如引理1.6.1中定义  $\mathcal{H}$，则易见  $A \in \mathcal{G} \Leftrightarrow A^c \in \mathcal{H}$。故由引理1.6.1立得本引理结论。

下一定理是测度逼近定理, 它的证明依赖于推广了的单调类定理(定理1.2.5).

定理1.6.3 设 $(\Omega,\mathcal{F},\mu)$为一测度空间，C为F的子类，且 $\sigma(\mathcal{C})=\mathcal{F}$. 此外设C满足如下条件：

 
$$
A,B\in\mathcal{C}\Rightarrow A\cup B\in\mathcal{C};\ A\in\mathcal{C}\Rightarrow A^{c}\in(\mathcal{C}_{\delta})_{\sigma}.
$$
 

若 $A \in \mathcal{F}$，且 $\mu$在A上为 $\sigma$有限，则有

$$
\mu(A)=\sup\{\mu(B)\mid B\subset A,B\in\mathcal{C}_{\delta}\}.   \tag*{(1.6.1)}
$$

证 首先假定 $\mu(A)<\infty$，令

 
$$
\nu(B)=\mu(A\cap B),\quad B\in\mathcal{F},
$$
 

---

则 $\nu$为 $(\Omega,\mathcal{F})$上的有限测度.令

 
$$
\mathcal{H}=\left\{C\in\mathcal{F}\mid\nu(C)=\sup\{\nu(B)\mid B\subset C,B\in\mathcal{C}\delta\}\right\},
$$
 

由引理1.6.1知，H为单调类，且 $H \supset C_\delta$。由C满足的条件推得

 
$$
A,B\in\mathcal{C}_{\delta}\Rightarrow A\cup B\in\mathcal{C}_{\delta};A\in\mathcal{C}_{\delta}\Rightarrow A^{c}\in(\mathcal{C}_{\delta})_{\sigma}.
$$
 

于是由定理1.2.5知， $\mathcal{H} \supset m(\mathcal{C}_\delta) = \sigma(\mathcal{C}_\delta) = \mathcal{F}$，从而对 $A \in \mathcal{F}$，有

 
$$
\nu(A)=\sup\{\nu(B)\mid B\subset A,B\in\mathcal{C}_{\delta}\},
$$
 

此即 $(1.6.1)$式.

现设 $\mu(A)=\infty$。令 $A_n\in\mathcal{F}$， $\mu(A_n)<\infty$， $n\geq1$，使得 $A_n\uparrow A$，则由上所证得到

 
$$
\sup\{\mu(B)\mid B\subset A,B\in\mathcal{C}_\delta\}\geqslant\sup\{\mu(B)\mid B\subset A_{n},B\in\mathcal{C}_\delta\}=\mu(A_{n}).
$$
 

但  $\lim_{n\to\infty}\mu(A_n)=\infty$，故(1.6.1)式成立.

作为定理的推论, 我们有如下命题, 它推广了习题1.3.8.

命题1.6.4 在定理1.6.3条件下，假定μ为有限测度，则对一切 $A \in \mathcal{F}$，有

 
$$
\mu(A)=\sup\{\mu(B)\mid B\subset A,B\in\mathcal{C}_\delta\}=\inf\{\mu(C)\mid C\supset A,C\in\mathcal{D}_\sigma\},
$$
 

其中 $\mathcal{D}=\{C^c \mid C \in \mathcal{C}\}$

##### 习题

1.6.1 设X为一距离空间， $B(X)$为Borel  $\sigma$-代数，F和G分别为X的闭子集和开子集全体， $\mu$为 $(X,B(X))$上的 $\sigma$-有限测度，则有

 
$$
\begin{align*}\mu(B)&=\sup\{\mu(F)\mid F\subset B,F\in\mathcal{F}\}\\&=\inf\{\mu(G)\mid B\subset G,G\in\mathcal{G}\},B\in\mathcal{B}(X).\end{align*}
$$
 

---

## 第2章 可测映射

## 2.1 定义及基本性质

定义2.1.1 设 $(\Omega,\mathcal{F})$及 $(E,\mathcal{E})$为两个可测空间， $f$为 $\Omega$到 $E$中的映射（简记为 $f:\Omega \longrightarrow E$）。如果对一切 $A \in \mathcal{E}$，有 $f^{-1}(A) \in \mathcal{F}$，则称 $f$为 $\mathcal{F}$可测映射。

今后, 我们用  $f^{-1}(\mathcal{E})$ 表示集类  $\{f^{-1}(A) \mid A \in \mathcal{E}\}$. 于是,  $f$ 为  $\mathcal{F}$ 可测映射  $\Leftrightarrow f^{-1}(\mathcal{E}) \subset \mathcal{F}$.

定义2.1.2 设$\mathbb{R}$为实数域，$\mathbb{R}=\mathbb{R}\cup\{-\infty,\infty\}$。分别用$\mathcal{B}(\mathbb{R})$及$\mathcal{B}(\mathbb{R})$表示$\mathbb{R}$及$\mathbb{R}$上的Borel $\sigma$代数。令$(\Omega,\mathcal{F})$为一可测空间，$f$为$\Omega$到$\mathbb{R}$中的映射。如果$f^{-1}(\mathcal{B}(\mathbb{R}))\subset\mathcal{F}$，称$f$为Borel可测函数，简称可测函数。若进一步$f$只取实值，则称$f$为实值可测函数。设$\mathbb{C}$为复数域，$f:\Omega\longrightarrow\mathbb{C}$称为复值可测函数，是指它的实部和虚部同时为实值可测函数。

容易看出:  $f$ 为  $(\Omega, \mathcal{F})$ 上的实值可测函数, 当且仅当  $f$ 为  $(\Omega, \mathcal{F})$ 到  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 中的可测映射.

下一命题给出了可测映射的一个有用刻画.

命题2.1.3 设 $(\Omega,\mathcal{F})$及 $(E,\mathcal{E})$为两个可测空间， $\mathcal{C}$为生成 $\sigma$代数 $\mathcal{E}$的一集类。如果 $f$为 $\Omega$到 $E$中的一个映射，使得 $f^{-1}(\mathcal{C})\subset\mathcal{F}$，则 $f$为可测映射。

证 令  $\mathcal{G} = \{A \subset E \mid f^{-1}(A) \in \mathcal{F}\}$，则  $\mathcal{G}$ 为  $E$ 上的一  $\sigma$ 代数。由假定， $\mathcal{G} \supset \mathcal{C}$，从而  $\mathcal{G} \supset \sigma(\mathcal{C}) = \mathcal{E}$，这表明  $f^{-1}(\mathcal{E}) \subset \mathcal{F}$，即  $f$ 为可测映射。

系2.1.4 设f为可测空间 $(\Omega,\mathcal{F})$上的一数值函数(即取值于 $\overline{R}$)，则下列条件等价：

(1) f 为可测函数;

(2)  $\forall a \in \mathbb{R}, [f < a] \in \mathcal{F};$

(3)  $\forall a \in \mathbb{R}, [f \leqslant a] \in \mathcal{F};$

(4)  $\forall a \in \mathbb{R}, [f > a] \in \mathcal{F};$

(5)  $\forall a \in \mathbb{R}, [f \geq a] \in \mathcal{F}.$

这里及今后， $[f < a]$表示集合 $\{\omega | f(\omega) < a\}$.

证 令  $C_1 = \{[-\infty, a) \mid a \in \mathbb{R}\}$，则易知  $\sigma(C_1) = \mathcal{B}(\mathbb{R})$，故由命题2.1.3知(2)⇔(1)。类似可证(3)⇔(1)。此外，显然有(2)⇔(5)及(3) ⇔(4)。

由于可测函数可取 $+\infty$和 $-\infty$，我们在研究可测函数的算术运算(即加、减、乘、除)时，作如下约定：

---

 
$$
\left(1\right)\left(\pm\infty\right)+x=x+\left(\pm\infty\right)=x-\left(\mp\infty\right)=\pm\infty,\left|x\right|<\infty;
$$
 

(2) $(\pm\infty)+(\pm\infty)=(\pm\infty)-(\mp\infty)=\pm\infty;$

(3)  $x/\pm\infty=0,\ |x|<\infty;$

 
$$
\begin{aligned}&(4)x\cdot(\pm\infty)=(\pm\infty)\cdot x=\left\{\begin{aligned}&\pm\infty,&\quad&x>0,\\&0,&\quad&x=0,\\&\mp\infty,&\quad&x<0;\end{aligned}\right.\end{aligned}
$$
 

(5) 下列运算被认为无意义:

 
$$
(\pm\infty)-(\pm\infty),(\pm\infty)+(\mp\infty),\pm\infty/\pm\infty,\pm\infty/\mp\infty,x/0.
$$
 

命题2.1.5  $(\Omega, \mathcal{F})$ 上实值(复值)可测函数全体构成实域(复域)上的一向量空间.

证 只需考虑实值可测函数情形. 令Q表示R中的有理数全体. 设f,g为实值可测函数, 则 $\forall a \in \mathbb{R}$, 有

 
$$
[f+g<a]=\bigcup_{r\in\mathbb{Q}}([f<r]\cap[g<a-r]),
$$
 

从而 $f+g$为实值可测函数. 此外, 对任何 $a\in\mathbb{R}$,  $af$显然为实值可测函数.

命题2.1.6 设 $f, g, \{f_n, n \geq 1\}$都为 $(\Omega, \mathcal{F})$上的可测函数.

(1) fg 为可测函数;

(2) 若  $f + g$ 处处有意义，则  $f + g$ 为可测函数；

(3) 若 f/g 处处有意义，则 f/g 为可测函数；

(4)  $\inf_{n} f_{n}, \sup_{n} f_{n}, \liminf_{n \to \infty} f_{n}$ 及  $\limsup_{n \to \infty} f_{n}$ 均为可测函数；

(5) $[f=g]$及 $[f\leqslant g]$为可测集.

证 (1) 首先假定 f 及 g 非负，则  $\forall a \in \mathbb{R}, a > 0$ 有

 
$$
[f g<a]=[f=0]\cup[g=0]\cup\bigg(\bigcup_{r\in\mathbb{Q}_{+}}[f<r]\cap[g<\frac{a}{r}]\in\mathcal{F}\bigg),
$$
 

故 $f_{g}$为可测函数.对一般的可测函数f及g,令

 
$$
f^{+}=f\vee0,\qquad f^{-}=(-f)\vee0,
$$
 

显然 $f^{+}$及 $f^{-}$为可测函数.于是fg的可测性由下式及(2)推得

 
$$
f g=(f^{+}-f^{-})(g^{+}-g^{-})=(f^{+}g^{+}+f^{-}g^{-})-(f^{+}g^{-}+f^{-}g^{+}).
$$
 

(2) 由命题2.1.5的证明看出.

(3)设 $|g| > 0$处处成立，则易知 $g^{-1}$为可测函数．若 $f/g$处处有意义，则 $f/g = f \cdot g^{-1}$，故 $f/g$为可测函数．

---

(4)  $\forall a \in \mathbb{R},$ 我们有

 
$$
[\operatorname*{i n f}_{n}f_{n}<a]=\bigcup_{n}[f_{n}<a],\quad[\operatorname*{s u p}_{n}f_{n}\leqslant a]=\bigcap_{n}[f_{n}\leqslant a],
$$
 

故由(1)和(3)推得(4).

(5) 令  $f_{n} = (f \wedge n) \vee (-n)$,  $g_{n} = (g \wedge n) \vee (-n)$, 则

 
$$
[f=g]=\bigcap_{n}[f_{n}=g_{n}],\quad[f\leqslant g]=\bigcap_{n}[f_{n}\leqslant g_{n}].
$$
 

由于 $[f_n = g_n] = [f_n - g_n = 0]$， $[f_n \leqslant g_n] = [f_n - g_n \leqslant 0]$，从而 $[f = g]$及 $[f \leqslant g]$为可测集。

下面我们研究可测函数的构造.

定义2.1.7 设 $A \subset \Omega$，令

 
$$
I_{A}=\left\{\begin{aligned}&1,&\qquad\omega\in A,\\ &0,&\qquad\omega\notin A,\end{aligned}\right.
$$
 

称 $I_{A}$为集A的示性函数. 设f为 $\Omega$上的一实函数, 若f只取有限多个值, 则称f为简单函数.

设$f$为一简单函数，其值域为$\{a_1, \cdots, a_n\}$．令$A_i = f^{-1}(\{a_i\})$，$i = 1, \cdots, n$，则$f = \sum_{i=1}^n a_i I_{A_i}$．若$(\Omega, \mathcal{F})$为一可测空间，则$f$为$\mathcal{F}$可测，当且仅当每个$A_i$为$\mathcal{F}$可测集．

定理2.1.8 设 $(\Omega,\mathcal{F})$为一可测空间，f为一可测函数.

(1) 存在一简单可测函数序列 $(f_{n}, n \geqslant 1)$，使得对一切  $n \geqslant 1$，有  $\left|f_{n}\right| \leqslant \left|f\right|$，且  $\lim_{n \to \infty} f_{n} = f$.

(2) 若 f 非负，则存在非负简单可测函数的增序列  $(f_{n})$，使得  $\lim_{n\to\infty}f_{n}=f.$

证 将 $f$表为 $f^+ - f^-$，易知(1)是(2)的推论。往证(2)。对 $n \geq 1$，令

 
$$
f_{n}=\sum_{k=0}^{n2^{n}-1}\frac{k}{2^{n}}I_{\left[\frac{k}{2^{n}}\leqslant f<\frac{k+1}{2^{n}}\right]}+n I_{\left[f\geqslant n\right]},
$$
 

则 $f_{n}$为非负简单可测函数，且 $f_{n}\uparrow f$.

下一定理是上一定理的简单推论,今后常被引用.

定理2.1.9 设 $(\Omega,\mathcal{F})$为一可测空间，C为生成F的一个代数. 令H为Ω上的一族非负实值函数，如果它满足下列条件：

(1)  $f, g \in \mathcal{H}, \alpha, \beta \geqslant 0 \Rightarrow \alpha f + \beta g \in \mathcal{H};$

(2)  $f_n \in \mathcal{H}, n \geq 1, f_n \uparrow$ 且  $f$ 有限 (相应地, 有界) 或  $f_n \downarrow f \Rightarrow f \in \mathcal{H}$;

---

(3)  $\forall A \in \mathcal{C}, I_A \in \mathcal{H},$

则H包含Ω上的所有非负实值(相应地, 有界)F可测函数.

证 令  $T = \{A \in \mathcal{F} \mid I_A \in \mathcal{H}\}$，则由(3)知  $T \supset C$，且由(2)知  $T$ 为单调类，故由单调类定理知  $T = \mathcal{F}$。于是由(1)、(2)及定理2.1.8推得定理的结论。

定义2.1.10 设 $(E,\mathcal{E})$为一可测空间， $\mathcal{H}$为 $\Omega$到E中的一族映射.令

 
$$
\mathcal{F}=\sigma\{\bigcup_{f\in\mathcal{H}}f^{-1}(\mathcal{E})\},
$$
 

则F为使H中所有元素为可测的最小σ代数. 我们称F为函数族H在Ω上生成的σ代数. 特别, 若(E, E) = (R, B(R)), 我们常用σ{f, f ∈ H}表示这一σ代数F.

下一定理给出了 $\sigma(f)$可测函数的一个刻画.

定理2.1.11 设$f$为$\Omega$到一可测空间$(E, \mathcal{E})$中的映射，$\sigma(f)$为$f$在$\Omega$上生成的$\sigma$代数（即$\sigma(f) = f^{-1}(\mathcal{E})$），则为要$\Omega$上的一数值函数$\varphi$为$\sigma(f)$可测，必须且只需存在$E$上的一$\mathcal{E}$可测函数$h$，使得$\varphi = h\circ f$（这里$h\circ f$表示$h$与$f$的复合，即$h\circ f(\omega) = h(f(\omega))$, $\omega \in \Omega$）。如果$\varphi$为实值（相应地，有界）$\sigma(f)$可测，则$h$可取为实值（相应地，有界）函数。

证 充分性显然(见习题2.1.2). 下证必要性. 设  $A \in \sigma(f)$, 则存在  $B \in \mathcal{E}$, 使  $A = f^{-1}(B)$, 即有  $I_A = I_B \circ f$, 于是对任一  $\sigma(f)$ 可测简单函数  $\varphi$, 存在  $E$ 上一  $\mathcal{E}$ 可测函数  $h$, 使得  $\varphi = h \circ f$. 现设  $\varphi$ 为一  $\sigma(f)$ 可测函数, 由定理2.1.8, 存在一列  $\sigma(f)$ 可测简单函数  $\varphi_n$, 使  $\lim_{n \to \infty} \varphi_n = \varphi$. 由上所证, 存在一列  $E$ 上  $\mathcal{E}$ 可测实值函数  $h_n$, 使  $\varphi_n = h_n \circ f$. 令  $h = \limsup_{n \to \infty} h_n$, 则  $\varphi = h \circ f$. 若进一步  $\varphi$ 为实值(相应地, 存在一常数  $c > 0$, 使得  $|\varphi| \leqslant c$), 令  $h' = h I_|h| < \infty$ (相应地, 令  $h' = h^+\wedge c - h^- \wedge c$), 则  $\varphi = h' \circ f$.

##### 习题

2.1.1 设 $(E, \mathcal{E})$为一可测空间，C为生成E的一集类。设H为Ω到E中的一族映射，F为H在Ω上诱导的σ代数，则

 
$$
\mathcal{F}=\sigma\{\bigcup_{f\in\mathcal{H}}f^{-1}(\mathcal{C})\}.
$$
 

设φ为F可测函数，则存在H的可数子族H₀ = {f₁, f₂, …}, 使得φ为F₀可测，其中F₀为H₀ 在Ω上诱导的σ代数。

2.1.2 设 $(\Omega, \mathcal{F})$,  $(E, \mathcal{E})$及 $(G, \mathcal{G})$为可测空间， $f$为 $\Omega$到 $E$中的 $\mathcal{F}$可测映射， $h$为 $E$到 $G$中的 $\mathcal{E}$可测映射。令 $\varphi = h \circ f$，则 $\varphi$为 $\Omega$到 $G$中的 $\mathcal{F}$可测映射。

2.1.3 设  $f$ 为  $(\Omega, \mathcal{F})$ 上的一有界可测函数，则存在简单可测函数序列  $(f_n, n \geq 1)$，使得  $|f_n| \leq |f|, n \geq 1$，且  $f_n$ 一致收敛于  $f$。

2.1.4 设 $(\Omega, \mathcal{F})$为一可测空间， $C = \{A_1, A_2, \cdots\}$为 $\Omega$的一个可数划分（即 $A_i \cap A_j = \varnothing$， $i \neq j$， $\sum_i A_i = \Omega$）。令 $T = \sigma\{F \cup C\}$，则

---

(1)  $T = \{\sum_{i=1}^{\infty}(A_i \cap B_i) \mid B_i \in \mathcal{F}, i \geq 1\}$;

(2) 设  $g$ 为  $\Omega$ 上一  $\mathcal{T}$ 可测实值函数，则存在一列  $\mathcal{F}$ 可测实函数  $(f_n, n \geq 1)$，使得  $g = \sum_{i=1}^{\infty} f_i I_{A_i}$

2.1.5 设Ω为一距离空间， $B(\Omega)$为Ω上的Borel σ代数。令 $C_b(\Omega)$表示Ω上有界连续函数全体，则 $B(\Omega) = \sigma\{f | f \in C_b(\Omega)\}$。

2.1.6 设  $\{f_{i}, 1 \leqslant i \leqslant m\}$ 为  $\mathbb{R}$ 上实值 Borel 函数，则  $(f_{1}, \cdots, f_{m})$ 为  $(\mathbb{R}^{m}, \mathcal{B}(\mathbb{R}^{m}))$ 到自身的可测映射 (提示: 利用命题 2.1.3).

2.1.7  $f : \Omega \longrightarrow \mathbb{C}$ 为  $(\Omega, \mathcal{F})$ 上的复值可测函数，当且仅当  $f$ 为  $(\Omega, \mathcal{F})$ 到  $(\mathbb{C}, \mathcal{B}(\mathbb{C}))$ 中的可测映射.

### 2.2 单调类定理(函数形式)

设 $(\Omega,\mathcal{F})$为一可测空间. 有时我们只知道有一类 $\mathcal{F}$可测函数满足某一性质, 而希望证明所有 $\mathcal{F}$可测函数满足该性质. 这时我们就要用到函数形式的单调类定理.

下一定理是与定理1.2.2(2)相应的函数形式.

定理2.2.1 设C为Ω上的一π类，H为由Ω上的一些实值函数构成的线性空间。如果它们满足下列条件：

(1)  $1 \in \mathcal{H};$

(2)  $f_n \in \mathcal{H}, n \geq 1, 0 \leq f_n \uparrow f,$ 且  $f$ 有限 (相应地, 有界)  $\Rightarrow f \in \mathcal{H};$

(3)  $\forall A \in \mathcal{C}, I_A \in \mathcal{H},$

则H包含Ω上的所有σ(C)可测实值(相应地, 有界)函数.

证 令  $\mathcal{F} = \{A \subset \Omega \mid I_A \in \mathcal{H}\}$，则易知  $\mathcal{F}$ 为  $\lambda$ 类，且  $C \subset \mathcal{F}$。于是由定理1.2.2(2)知  $\sigma(C) \subset \mathcal{F}$。设  $f$ 为  $\sigma(C)$ 可测实值（相应地，有界）函数，令

 
$$
g_{n}=\sum_{k=0}^{n2^{n}-1}\frac{k}{2^{n}}I_{\left\lfloor\frac{k}{2^{n}}\leqslant f^{+}<\frac{k+1}{2^{n}}\right\rfloor}+n I_{\left[f^{+}\geqslant n\right]},
$$
 

则 $g_n \in \mathcal{H}, g_n \uparrow f^+$，从而由(2)知 $f^+ \in \mathcal{H}$，同理 $f^- \in \mathcal{H}$，故 $f = f^+ - f^- \in \mathcal{H}$。

下面我们着手推广定理2.2.1. 为此, 首先引进 $\lambda$族概念, 它是集合的 $\lambda$类概念在函数情形下的类似物.

定义2.2.2 设H为Ω上的一族非负有界函数，称H为λ族，如果它满足下列条件：

(1)  $1 \in \mathcal{H};$

 
$$
(2)\;f\in\mathcal{H},\;\alpha\in\mathbb{R}_{+}\Rightarrow\alpha f\in\mathcal{H};
$$
 

(3)  $f, g \in \mathcal{H}, f \geqslant g \Rightarrow f - g \in \mathcal{H};$

(4)  $f_n \in \mathcal{H}, n \geq 1, f_n \uparrow f$，且  $f$ 有界  $\Rightarrow f \in \mathcal{H}$.

设C为Ω上的一族非负有界函数, 我们用 $\wedge(C)$表示包含C的最小λ族, 并称 $\wedge(C)$为由C生成的λ族.

---

注2.2.3 设H为λ族，则H还有如下性质：

 
$$
f,g\in\mathcal{H}\Rightarrow f+g\in\mathcal{H}.
$$
 

事实上，设C为一常数，使得 $f+g\leqslant C$，则由(3)知

 
$$
f+g=C-\left[(C-f)-g\right]\in\mathcal{H}.
$$
 

下一定理是与定理1.2.3(2)相应的函数形式.

定理2.2.4 设C为Ω上的一族非负有界函数. 我们用 $\mathcal{L}_{b}^{+}(\mathcal{C})$表示非负有界 $\sigma(f \mid f \in \mathcal{C})$可测函数全体, 则下面二断言等价:

(1)  $\Lambda(\mathcal{C}) = \mathcal{L}_{b}^{+}(\mathcal{C});$

(2)  $f, g \in \mathcal{C} \Rightarrow fg \in \wedge(\mathcal{C}).$

证 只需证 $(2)\Rightarrow(1)$. 设 $(2)$成立, 令

 
$$
\mathcal{G}_{1}=\{f\in\wedge(\mathcal{C})\mid\forall g\in\mathcal{C},f g\in\wedge(\mathcal{C})\},
$$
 

则易见 $G_1$为 $\lambda$族，且 $G_1 \supset C$，故有 $G_1 = \wedge(C)$。再令

 
$$
\mathcal{G}_{2}=\{f\in\wedge(\mathcal{C})\mid\forall g\in\wedge(\mathcal{C}),f g\in\wedge(\mathcal{C})\},
$$
 

则 $G_2$为 $\lambda$族，且 $G_1 \supset C(\text{因有}\mathcal{G}_1 = \wedge(\mathcal{C}))$，故有 $G_2 = \wedge(\mathcal{C})$，这表明 $\wedge(\mathcal{C})$对乘积运算封闭。令

 
$$
\mathcal{F}=\{A\subset\Omega\mid I_{A}\in\wedge(\mathcal{C})\},
$$
 

则$\mathcal{F}$既为$\lambda$类又为$\pi$类，故$\mathcal{F}$为$\sigma$代数．往证$\wedge(\mathcal{C})$对有限下端运算封闭．设$f,g\in\wedge(\mathcal{C})$，为证$f\wedge g\in\wedge(\mathcal{C})$，不妨假定$f\leq1,g\leq1$，于是有$|f-g|\leq1$，且有

 
$$
(f-g)^{2}=f^{2}+g^{2}-2f g\in\wedge(\mathcal{C}).
$$
 

我们将用到如下事实(请读者自行证明): 设 $|x|\leq1$, 令 $P_{0}(x)=0$,

 
$$
P_{n+1}(x)=P_{n}(x)+\frac{1}{2}(x^{2}-P_{n}(x)^{2}),\quad n\geqslant0,
$$
 

则 $P_{n}(x)\uparrow|x|$.于是,由于

 
$$
P_{1}(f-g)=\frac{1}{2}(f-g)^{2}\in\wedge(\mathcal{C}),
$$
 

故由归纳法知 $P_n(f - g) \in \wedge(\mathcal{C}), n \geq 1$。从而由λ族的性质(4)知 $|f - g| \in \wedge(\mathcal{C})$。最终我们有

 
$$
f\wedge g=\frac{1}{2}(f+g-|f-g|)\in\wedge(\mathcal{C}).
$$
 

---

现设 $f\in\mathcal{C},\alpha>0$为一实数.则由上所证,

 
$$
(f/\alpha)\wedge1=(1/\alpha)(f\wedge\alpha)\in\wedge(\mathcal{C}),
$$
 

故有 $1-(f/\alpha\wedge1)^{n}\in\wedge(\mathcal{C})$。从而有

 
$$
1-(\frac{f}{\alpha}\wedge1)^{n}\uparrow I_{[f<\alpha]}\in\wedge(\mathcal{C}).
$$
 

这表明 $[f < \alpha] \in \mathcal{F}$. 因此 $f$为 $\mathcal{F}$可测. 由定义1.1.10知 $\sigma(f \mid f \in \mathcal{C}) \subset \mathcal{F}$.

最后，设 $f\in\mathcal{L}_{b}^{+}(\mathcal{C})$，令

 
$$
f_{n}=\sum_{k=0}^{n2^{n}-1}\frac{k}{2^{n}}I_{\left[\frac{k}{2^{n}}\leqslant f<\frac{k+1}{2^{n}}\right]}+n I_{\left[f\geqslant n\right]},
$$
 

则由于

 
$$
I_{\left[\frac{k}{2^{n}}\leqslant f<\frac{k+1}{2^{n}}\right]}\in\wedge(\mathcal{C}),
$$
 

故有

 
$$
f_{n}\in\wedge(\mathcal{C}),f_{n}\uparrow f\in\wedge(\mathcal{C}),
$$
 

这表明 $\mathcal{L}_b^+(\mathcal{C}) \subset \wedge(\mathcal{C})$。但相反的包含关系恒成立，故有 $\mathcal{L}_b^+(\mathcal{C}) = \wedge(\mathcal{C})$。

作为推论, 我们得到与定理1.2.2(2)相应的函数形式的单调类定理.

定理2.2.5 设C为Ω上的一族非负有界函数, 且对乘积运算封闭. 若H为一λ族, 且包含C, 则H包含一切非负有界σ(f|f∈C)可测函数.

下面我们将给出其他形式的单调类定理. 它们是定理1.2.3(1)的函数形式.

定义2.2.6 设H为Ω上的一有界函数族，称H为单调族，如果它对一致有界单调序列极限封闭.

设C为Ω上的一有界函数族．我们用M(C)表示包含C的最小单调族，用ℱ₂(C)表示有界σ(f|f∈C)可测函数全体．

定理2.2.7 设C为Ω上的一有界函数族，则下列二条件等价：

(1)  $M(\mathcal{C}) = \mathcal{L}_b(\mathcal{C})$;

2)  $1 \in M(\mathcal{C}); f \in \mathcal{C}, \alpha \in \mathbb{R} \Rightarrow \alpha f \in M(\mathcal{C});$

 
$$
f,g\in\mathcal{C}\Rightarrow f+g\in M(\mathcal{C}),f\wedge g\in M(\mathcal{C}).
$$
 

证 只需证 $(2)\Rightarrow(1)$. 设 $(2)$成立, 令

 
$$
\mathcal{H}_{1}=\{f\in M(\mathcal{C})\mid\forall\alpha\in\mathbb{R},\alpha f\in M(\mathcal{C});\forall g\in\mathcal{C},f+g,f\wedge g\in M(\mathcal{C})\}
$$
 

则 $H_{1}$为单调族，且 $H_{1} \supset C$，故 $H_{1} = M(C)$。再令

 
$$
\mathcal{H}_{2}=\big\{f\in M(\mathcal{C})\;|\forall g\in M(\mathcal{C}),f+g,f\wedge g\in M(\mathcal{C})\big\},
$$
 

---

则 $H_2$为单调族，且 $H_2 \supset C$（因为 $H_1 = M(C)$，故 $H_2 = M(C)$。由上所证， $M(C)$为一线性空间，且对有限下端运算封闭（从而也对有限上端运算封闭）。此外，依假定 $1 \in M(C)$。令

 
$$
\mathcal{F}=\{A\subset\Omega\mid I_{A}\in M(\mathcal{C})\},
$$
 

则 $\pmb{F}$为 $\Omega$上的一 $\sigma$代数.

往证C中的每个元为F可测. 设 $f \in \mathcal{C}, a \in \mathbb{R}$, 令 $f_n = n(f - a)^+ \wedge 1$, 则 $f_n \in M(\mathcal{C})$, 且 $f_n \uparrow I_{[f > a]}$. 故 $I_{[f > a]} \in M(\mathcal{C})$, 即有 $[f > a] \in \mathcal{F}$. 这表明f为F可测, 于是有

 
$$
\sigma(f\mid f\in\mathcal{C})\subset\mathcal{F}.
$$
 

最后，设 $f\in\mathcal{L}_{b}^{+}(\mathcal{C})$，令

 
$$
f_{n}=\sum_{k=0}^{n2^{n}-1}\frac{k}{2^{n}}I_{\left[\frac{k}{2^{n}}\leqslant f<\frac{k+1}{2^{n}}\right]}+n I_{\left[f\geqslant n\right]}.
$$
 

由于 $M(\mathcal{C})$为线性空间，故 $f_n \in M(\mathcal{C})$。但 $f_n \uparrow f$，于是 $f \in M(\mathcal{C})$，这表明 $\mathcal{L}_b^+(\mathcal{C}) \subset M(\mathcal{C})$，因此有 $\mathcal{L}_b(\mathcal{C}) \subset M(\mathcal{C})$。但相反的包含关系恒成立，故有 $M(\mathcal{C}) = \mathcal{L}_b(\mathcal{C})$。

作为定理的一个有用的推论, 我们有下面的定理.

定理2.2.8 设H为Ω上的一有界函数的单调族, C为H的一子族. 则H ⊃ L_b(C), 如果下列条件之一成立:

(1) H为线性空间,  $1 \in H$, 且C对乘积运算封闭;

(2) C 为一代数(即 C 为一线性空间, 且对乘积运算封闭), 且存在 C 中某个一致有界的单调序列, 其极限为 1;

(3) C为一线性空间, C对有限下端运算封闭, 且存在C中某个一致有界的单调序列, 其极限为1.

证 设(1)成立．令$\mathcal{D}$为由1和$C$生成的代数，则$\mathcal{D}\subset\mathcal{H}$，从而$M(\mathcal{D})\subset\mathcal{H}$．易证$M(\mathcal{D})$为一线性空间(见习题2.2.1)．设$f\in\mathcal{D}$，且$|f|\leq1$．采用定理2.2.4的证明中的记号，令$f_n=P_n(f)$，则$f_n\in\mathcal{D}$，且$0\leq f_n\uparrow|f|$，故$|f|\in M(\mathcal{D})$．于是对一般的$f\in\mathcal{D}$，亦有$|f|\in M(\mathcal{D})$．设$f,g\in\mathcal{D}$，则有

 
$$
f\wedge g=\frac{1}{2}(f+g-|f-g|)\in M(\mathcal{D}).
$$
 

故由定理2.2.7知 $\mathcal{L}_b(\mathcal{D}) = M(\mathcal{D})$。但显然有 $\mathcal{L}_b(\mathcal{D}) = \mathcal{L}_b(\mathcal{C})$，故有 $\mathcal{L}_b(\mathcal{C}) = M(\mathcal{D}) \subset \mathcal{H}$。

设(2)成立，则 $1 \in M(\mathcal{C})$， $M(\mathcal{C}) \subset \mathcal{H}$，且 $M(\mathcal{C})$为一线性空间。余下证明同上。

设(3)成立，则定理2.2.7中的条件(2)成立，故有 $\mathcal{L}_{b}(\mathcal{C})=M(\mathcal{C})\subset\mathcal{H}$.

---

##### 习题

2.2.1 设C为Ω上的一有界函数族. 若C为线性空间, 则M(C)亦为线性空间.

2.2.2 设C为Ω上的一非负有界函数族，则下列二条件等价：

(1)  $M(\mathcal{C}) = \mathcal{L}_{b}^{+}(\mathcal{C})$;

 
$$
2)\ f,g\in\mathcal{C}\Rightarrow f\land g\in M(\mathcal{C});f\in\mathcal{C},a\in\mathbb{R}\Rightarrow af,a-f\land a\in M(\mathcal{C}).
$$
 

2.2.3 (定理2.2.1的另一种形式) 设C为Ω上的一π类, H为Ω上的一非负实值函数族. 如果下列条件被满足:

(1)  $1 \in \mathcal{H};$

 
$$
(2)f\in\mathcal{H},a\in\mathbb{R}_{+}\Rightarrow af\in\mathcal{H};f,g\in\mathcal{H},f\geq g\Rightarrow f-g\in\mathcal{H};
$$
 

(3)  $f_n \in \mathcal{H}, n \geq 1, 0 \leq f_n \uparrow f$，且  $f$ 有限（相应地，有界） $\Rightarrow f \in \mathcal{H}$;

(4)  $\forall A \in \mathcal{C}, I_A \in \mathcal{H},$

则H包含Ω上的所有非负σ(C)可测实值(相应地, 有界)函数.

## 2.3 可测函数序列的几种收敛

设 $(\Omega,\mathcal{F},\mu)$为一测度空间. 本节将研究 $(\Omega,\mathcal{F},\mu)$上实值可测函数序列的几种收敛及它们之间的关系. 为了叙述方便, 我们将采用如下术语: 如果某一性质在 $\Omega$上除了一零测度集外成立, 则称它几乎处处成立, 简称a.e.成立.

定义2.3.1 设 $(f_{n})_{n\geq1}$，f均为实值可测函数.

(1) 如果存在一零测集 N，使得  $\forall \omega \in N^c$ 有  $\lim_{n \to \infty} f_n(\omega) = f(\omega)$，则称  $(f_n)$ 几乎处处收敛于  $f(\text{或a.e. 收敛于 } f)$，记为  $\lim_{n \to \infty} f_n = f$，a.e.，或  $f_n \xrightarrow{\text{a.e.}} f$。

(2) 如果对任给  $\varepsilon > 0$，存在  $N \in \mathcal{F}, \mu(N) < \varepsilon$，使得  $(f_n)$ 在  $N^c$ 上一致收敛于  $f$，则称  $(f_n)$ 几乎一致收敛于  $f$，并记为  $\lim_{n \to \infty} f_n = f$，a.un.，或  $f_n \xrightarrow{\text{a.un.}} f$。

(3) 如果对任给  $\varepsilon > 0, \lim_{n \to \infty} \mu([|f_n - f| > \varepsilon]) = 0$，则称  $(f_n)$ 依测度收敛于  $f$，并记为  $f_n \xrightarrow{\mu} f$。当  $\mu$ 是概率测度时，称  $(f_n)$ 依概率收敛于  $f$。

更一般地, 对一定向序列 $(f_{a})$也可定义上述几种收敛概念, 特别, 对双指标序列 $(f_{nm})$可定义上述收敛概念.

定义2.3.2 设 $(f_{n})$为一列实值可测函数. 如果当 $n,m\to\infty,(f_{n}-f_{m})$ a.e.收敛于0,则称 $(f_{n})$为a.e.收敛基本列. 类似可以定义其他各类收敛的基本列.

注2.3.3 由定义看出，上述各类收敛的极限是a.e.唯一确定的。例如：设 $f_{n}\xrightarrow{a.e.}g$，则 $f=g$，a.e..另一方面，设 $f_{n}\xrightarrow{a.e.}f$， $f=g$，a.e.,则 $f_{n}\xrightarrow{a.e.}g$。此外，对各类收敛序列 $(f_{n})$，若对每个n，用一与 $f_{n}$ a.e.相等的实值可测函数 $g_{n}$代替 $f_{n}$，则 $(g_{n})$亦为同类收敛序列，其极限与 $(f_{n})$的极限a.e.相等。

下一定理给出了上述几种收敛的刻画.

---

定理2.3.4 设 $(f_{n})$及f均为实值可测函数.

(1)  $f_n \xrightarrow{\text{a.e.}} f$，当且仅当  $\forall \varepsilon > 0$ 有

$$
\mu\big(\bigcap_{n=1}^{\infty}\bigcup_{i=n}^{\infty}[|f_{i}-f|\geqslant\varepsilon]\big)=0.   \tag*{(2.3.1)}
$$

(2)  $f_n \xrightarrow{\text{a.un.}} f$，当且仅当  $\forall \varepsilon > 0$ 有

$$
\lim_{n\to\infty}\mu\big(\bigcup_{i=n}^{\infty}[|f_{i}-f|\geqslant\varepsilon]\big)=0.   \tag*{(2.3.2)}
$$

(3)  $f_n \xrightarrow{\mu} f$，当且仅当对  $(f_n)$ 的任何子列  $(f_{n'})$，存在其子列  $(f_{{n'}_k})$，使得  $f_{{n'}_k} \xrightarrow{\text{a.un.}} f, k \to \infty$.

证 (1) 设  $(a_{n})$ 为实数列，a 为实数，则要使  $a_{n} \rightarrow a$，必须且只需对每个  $k \geq 1$，存在自然数  $n(k)$，使得当  $i \geq n(k)$ 时有  $|a_{i} - a| < \frac{1}{k}$。因此有

 
$$
\left\{\omega\mid f_{n}(\omega)\rightarrow f(\omega)\right\}=\bigcap_{k=1}^{\infty}\bigcup_{n=1}^{\infty}\bigcap_{i=n}^{\infty}\left[\left|f_{i}-f\right|<\frac{1}{k}\right].
$$
 

于是， $f_{n} \xrightarrow{a.e.} f$，当且仅当

 
$$
\mu\Big(\bigcup_{k=1}^{\infty}\bigcap_{n=1}^{\infty}\bigcup_{i=n}^{\infty}\left[|f_{i}-f|\geqslant\frac{1}{k}\right]\Big)=0,
$$
 

即 $\forall k \geqslant 1$有

 
$$
\mu\Big(\bigcap_{n=1}^{\infty}\bigcup_{i=n}^{\infty}\left[\left|f_{i}-f\right|\geqslant\frac{1}{k}\right]\Big)=0,
$$
 

(1) 得证.

(2) 必要性. 设  $f_{n} \stackrel{\mathrm{a.un.}}{\longrightarrow} f$. 则  $\forall \delta > 0, \exists F \in \mathcal{F}, \mu(F) < \delta$, 使  $f_{n}$ 在  $F^{c}$ 上一致收敛于  $f$. 于是  $\forall \varepsilon > 0$, 存在  $N$, 使得当  $i \geq N$ 时, 有

 
$$
|f_{i}(\omega)-f(\omega)|<\varepsilon,\quad\omega\in F^{c}.
$$
 

因此， $\bigcup_{i=N}^{\infty}[|f_i-f|\geq\varepsilon]\subset F$，特别有

 
$$
\limsup_{n\to\infty}\mu\Big(\bigcup_{i=n}^{\infty}[|f_{i}-f|\geqslant\varepsilon]\Big)\leqslant\mu(F)<\delta.
$$
 

必要性得证.

下证充分性. 设对任给  $\varepsilon > 0$ 有 (2.3.2) 式成立. 则  $\forall \delta > 0, \forall k \geqslant 1, \exists n(k)$, 使得

---

 
$$
\mu\Big(\bigcup_{i=n(k)}^{\infty}\left[|f_{i}-f|\geqslant\frac{1}{k}\right]\Big)<\frac{\delta}{2^{k}}.
$$
 

令

 
$$
F=\bigcup_{k=1}^{\infty}\bigcup_{i=n(k)}^{\infty}\left[\left|f_{i}-f\right|\geqslant\frac{1}{k}\right],
$$
 

则 $\mu(F)<\delta$，且有

 
$$
F^{c}=\bigcap_{k=1}^{\infty}\bigcap_{i=n(k)}^{\infty}\left[\left|f_{i}-f\right|<\frac{1}{\bar{k}}\right].
$$
 

这表明在 $F^{c}$上 $f_{n}$一致收敛于f. 依定义, $f_{n}\stackrel{a.un.}{\longrightarrow}f.$

(3) 必要性. 设  $f_{n} \xrightarrow{\mu} f$. 令  $(f_{n'})$ 为  $(f_{n})$ 的一子列, 则仍有  $f_{n'} \xrightarrow{\mu} f$. 由依测度收敛的定义, 存在  $(f_{n'})$ 的子列  $(f_{n_k}')$, 使得

 
$$
\mu\Big(\Big[|f_{n_{k}^{\prime}}-f|\geqslant\frac{1}{k}\Big]\Big)\leqslant\frac{1}{2^{k}},\quad\forall k\geqslant1.
$$
 

故 $\forall m \geqslant 1$，我们有

 
$$
\mu\Big(\bigcup_{k=m}^{\infty}\Big[|f_{n_{k}^{\prime}}-f|\geqslant\frac{1}{k}\Big]\Big)\leqslant\sum_{k=m}^{\infty}\frac{1}{2^{k}}=\frac{1}{2^{m-1}}.
$$
 

因此， $\forall\varepsilon>0$，与 $(f_{n_{k}^{\prime}})$相应的(2.3.2)式成立，从而 $f_{n_{k}^{\prime}}^{\mathrm{a.un.}}$  $\stackrel{\mathrm{a.un.}}{\longrightarrow}f.$

下证充分性. 我们用反证法. 假定 $(f_{n})$不依测度 $\mu$收敛于f, 则存在某个 $\varepsilon$, 使得

 
$$
\limsup_{n\to\infty}\mu\big([|f_{n}-f|\geqslant\varepsilon]\big)>\delta>0.
$$
 

于是存在 $(f_n)$的子列 $(f_{n'})$，使得对一切 $n'$有 $\mu([|f_{n'} - f| \geq \varepsilon]) > \delta$。显然 $(f_{n'})$不包含几乎一致收敛的子列。充分性得证。

定理2.3.5 (1)我们有

$$
f_{n}\stackrel{\mathrm{a.u n.}}{\longrightarrow}f\Rightarrow f_{n}\stackrel{\mathrm{a.e.}}{\longrightarrow}f;\quad f_{n}\stackrel{\mathrm{a.u n.}}{\longrightarrow}f\Rightarrow f_{n}\stackrel{\mu}{\longrightarrow}f.   \tag*{(2.3.3)}
$$

(2)若 $\mu$为有限测度，则有 $f_{n} \xrightarrow{\text{a.e.}} f \Leftrightarrow f_{n} \xrightarrow{\text{a.un.}} f.$

(3)设 $f_{n}\xrightarrow{\mu}f$，则存在子列 $(f_{n_{k}})$，使 $f_{n_{k}}\xrightarrow{\mathrm{a.e.}}f$.

证 (1) 直接由定理2.3.4或定义2.3.1推出.

(2) 设  $f_n \xrightarrow{\text{a.e.}} f$. 由定理2.3.4,  $\forall \varepsilon > 0$, 有(2.3.1)式成立. 于是由有限测度的从上连续性(定理1.3.4)知(2.3.2)式成立, 故有  $f_n \xrightarrow{\text{a.un.}} f$.

(3)由定理2.3.4(3)及上述(1)推得.

---

注2.3.6 (1) 定理2.3.5(2)中“⇒”部分通常称为Egoroff定理.

(2) 设 $(\Omega, \mathcal{F}, \mu)$为一有限测度空间， $f_n$， $f$为实值可测函数。则由定理2.3.4(3)及定理2.3.5(2)知，为要 $f_n \xrightarrow{\mu} f$，必须且只需对 $(f_n)$的任一子列 $(f_{n'})$，存在其子列 $(f_{n_k}')$，使 $f_{n_k}' \xrightarrow{\text{a.e.}} f$。

作为定理2.3.4(3)的一个应用, 我们有如下的

定理2.3.7 设$g$为$\mathbb{R}^m$上一实值可测函数，$D \subset \mathbb{R}^m$。又设$(f_n^{(i)})_n \geq 1$为实值可测函数序列，$f^{(i)}$为实值可测函数，$1 \leq i \leq m$。假定$(f_n^{(1)}, \cdots, f_n^{(m)})$及$(f^{(1)}, \cdots, f^{(m)})$在$D$中取值，且对$1 \leq i \leq m$，$f_n^{(i)} \xrightarrow{\mu} f^{(i)}$，则有如下结论：

(1) 设 g 在 D 上一致连续, 则

 
$$
g(f_{n}^{(1)},\cdots,f_{n}^{(m)})\xrightarrow{\mu}g(f^{(1)},\cdots,f^{(m)};
$$
 

(2) 设g在D上连续,  $\mu$ 为有限测度, 则 $g(f_{n}^{(1)},\cdots,f_{n}^{(m)})\xrightarrow{\mu}g(f^{(1)},\cdots,f^{(m)})$.

证 往证(1). 首先, 由习题2.1.6及2.1.2知  $g(f_{n}^{(1)}, \cdots, f_{n}^{(m)})$ 为实可测函数. 设  $(n')$ 为自然数列的一子序列, 由定理2.2.4(3), 并利用对角线法则, 可取  $(n')$ 的子列  $(n_{k}')$, 使得对每个  $i: 1 \leqslant i \leqslant m$, 有  $f_{n_{k}'}^{(i)} \xrightarrow{\text{a.un}} f^{(i)}$. 由于 g 在 D 上一致连续, 故易见

 
$$
g(f_{n_{k}^{\prime}}^{(1)},\cdots,f_{n_{k}^{\prime}}^{(m)})\stackrel{\mathrm{a.u n.}}{\longrightarrow}g(f^{(1)},\cdots,f^{(m)}).
$$
 

因此，由定理2.3.4(3)知， $g(f_n^{(1)}, \cdots, f_n^{(m)}) \xrightarrow{\mu} g(f^{(1)}, \cdots, f^{(m)})$。(1)得证。(2)的证明完全类似。

下一定理是数学分析中Bolzano-Weierstrass定理的随机版本(见Föllmer-Schied: Stochastic Finance, Walter de Gruyter, 2002).

定理2.3.8 设$(\Omega,\mathcal{F},\mu)$为一测度空间，$(f_{n})_{n\geq1}$为$\Omega$上$\mathbb{R}^{d}$值可测函数序列，满足$\liminf_{n\to\infty}|f_{n}|<\infty,\mu-\mathrm{a.e.}$，则存在一$\mathbb{R}^{d}$值可测函数$f$和整数值可测函数的严格增序列$\alpha_{n}\uparrow\infty$，使得

 
$$
\lim_{n\to\infty}f_{\alpha_{n}(\omega)}(\omega)=f(\omega),\quad\mu\text{-a.e.}\omega\in\Omega.
$$
 

证 令  $W = \liminf_{n \to \infty} |f_n|$，在零测集  $[W = \infty]$ 上，令  $\alpha_m = m$。下面只在  $[W < \infty]$ 上考虑问题。令  $\alpha_1^0 = 1$，归纳定义  $\alpha_m^0$ 如下：

 
$$
\alpha_{m}^{0}=\inf\left\{n>\alpha_{m-1}^{0}\mid\left|\left|f_{n}\right|-W\right|\leqslant\frac{1}{m}\right\},\ m=2,3,\cdots.
$$
 

令 $f^{1}=\liminf_{m\to\infty}f_{\alpha_{m}^{0}}^{1},\alpha_{1}^{1}=1$，归纳定义 $\alpha_{m}^{1}$如下：

 
$$
\alpha_{m}^{1}=\inf\left\{\alpha_{n}^{0}\mid\alpha_{n}^{0}>\alpha_{m-1}^{1},\left|f_{\alpha_{m}^{0}}^{1}-f^{1}\right|\leqslant\frac{1}{m}\right\},\ m=2,3,\cdots.
$$
 

---

对 $i=2,\cdots,d$，定义 $f^{i}=\liminf_{m\to\infty}f_{\alpha_{m}^{i-1}}^{i},\alpha_{1}^{i}=1$，归纳定义 $\alpha_{m}^{i}$如下：

 
$$
\alpha_{m}^{i}=\inf\left\{\alpha_{n}^{i-1}\mid\alpha_{n}^{i-1}>\alpha_{m-1}^{i},|f_{\alpha_{m}^{i-1}}^{i}-f^{i}|\leqslant\frac{1}{m}\right\},\quad m=2,3,\cdots.
$$
 

则 $f=(f^{1},\cdots,f^{d})$和 $\alpha_{m}:=\alpha_{m}^{d}$分别为要找的 $\mathbb{R}^{d}$值可测函数和整数值可测函数. □

##### 习题

2.3.1 设 $(f_{n})$为一实值可测函数序列，则为要 $(f_{n})$a.e.(相应地，几乎一致或依测度 $\mu$)收敛于某f，必须且只需 $(f_{n})$为相应的收敛基本列.

2.3.2 举例说明：若  $\mu(\Omega) = \infty$，则  $\mu$ 几乎处处收敛的序列不一定依测度收敛。

2.3.3 设  $f_{n} \xrightarrow{\mu} f$，则有  $\liminf_{n \to \infty} f_{n} \leqslant f \leqslant \limsup_{n \to \infty} f_{n}$，a.e..

2.3.4 设 $\mu$为有限测度，则

 
$$
f_{n}\stackrel{\mu}{\rightarrow}f\;\Rightarrow\;\frac{f_{n}}{1+\left|f_{n}\right|}\stackrel{\mu}{\rightarrow}\frac{f}{1+\left|f\right|}.
$$
 

2.3.5 设 $(\Omega,\mathcal{F})$为一可测空间， $(f_{n})$为一实值 $\mathcal{F}$可测函数序列，它处处收敛于某实值函数 $f$，则 $f$也为 $\mathcal{F}$可测.

2.3.6 设 $(\Omega, \mathcal{F})$为一可测空间， $A \subset \Omega$，则 $A$上的任一实值 $A \cap \mathcal{F}$可测函数可以延拓成为 $\Omega$上的实值 $\mathcal{F}$可测函数。

---

## 第 3 章 积分和空间  $L^{p}$

## 3.1 积分的基本性质

在本节给定一测度空间 $(\Omega,\mathcal{F},\mu)$。我们用 $S^+$表示 $\Omega$上 $\mathcal{F}$可测非负简单函数全体，用 $\mathcal{L}$(相应地， $\overline{\mathcal{L}}$)表示 $\Omega$上 $\mathcal{F}$可测实值(相应地，数值)函数全体。令 $\overline{\mathcal{F}}$表示 $\mathcal{F}$关于 $\mu$的完备化，称 $\overline{\mathcal{F}}$可测函数为 $\mu$可测函数。 $\mathcal{L}^+$及 $\overline{\mathcal{L}}^+$则分别表示 $\mathcal{L}$及 $\overline{\mathcal{L}}$中的非负函数全体。

显然, 为要 $f$为 $\mu$可测函数, 必须且只需存在一 $\mathcal{F}$可测函数 $g$, 使得 $f = g$, a.e..

首先, 我们定义非负简单可测函数关于测度 $\mu$的积分.

定义3.1.1 设 $f=\sum_{i=1}^{n}a_{i}I_{A_{i}}\in\mathcal{S}^{+}$，其中 $a_{i}\in\mathbb{R}_{+},A_{i}\in\mathcal{F}$。令

 
$$
\int_{\Omega}f d\mu=\sum_{i=1}^{n}a_{i}\mu(A_{i}),
$$
 

易证$\int_{\Omega}f d\mu$ 不依赖于$f$ 的具体表达. 我们称$\int_{\Omega}f d\mu$ 为$f$ 关于$\mu$ 的积分, 通常, 我们用$\mu(f)$ 简记$\int_{\Omega}f d\mu$.

下一命题列举了这一积分的基本性质.

命题3.1.2 设 $f_{n}, g_{n}, f, g$都是 $S^{+}$中的元素，则

(1)  $\mu(I_A) = \mu(A)$,  $\forall A \in \mathcal{F}$;

(2)  $\mu(\alpha f) = \alpha\mu(f), \forall\alpha \in \mathbb{R}_+;$

(3)  $\mu(f + g) = \mu(f) + \mu(g);$

(4)  $f \leqslant g \Rightarrow \mu(f) \leqslant \mu(g);$

(5)  $f_n \downarrow f, \mu(f_1) < \infty \Rightarrow \mu(f_n) \downarrow \mu(f);$

(6)  $f_n \uparrow f \Rightarrow \mu(f_n) \uparrow \mu(f)$;

(7)  $f_n \uparrow, g_n \uparrow, \lim_{n \to \infty} f_n \leqslant \lim_{n \to \infty} g_n \Rightarrow \lim_{n \to \infty} \mu(f_n) \leqslant \lim_{n \to \infty} \mu(g_n).$

证 (1)-(4) 显然. 往证(5). 令  $g_{n} = f_{n} - f$, 则  $g_{n} \in S^{+}$,  $g_{n} \downarrow 0$, 且  $\mu(g_{1}) \leqslant \mu(f_{1}) < \infty$. 令

 
$$
\beta=\sup\{g_{1}(\omega)\mid\omega\in\Omega\},
$$
 

则 $\forall\varepsilon>0$，我们有

 
$$
0\leqslant g_{n}\leqslant\beta I_{[g_{n}>\varepsilon]}+\varepsilon I_{[0<g_{n}\leqslant\varepsilon]}\leqslant\beta I_{[g_{n}>\varepsilon]}+\varepsilon I_{[g_{1}>0]}.
$$
 

由4得

 
$$
\mu(g_{n})\leqslant\beta\mu([g_{n}>\varepsilon])+\varepsilon\mu([g_{1}>0]).
$$
 

---

由于 $[g_n > \varepsilon]\downarrow \varnothing$，且 $\mu([g_1 > \varepsilon]) \leqslant \mu([g_1 > 0]) < \infty$（因 $\mu(g_1) < \infty$），故由测度的从上连续性知 $\mu([g_n > \varepsilon]) \downarrow 0$。于是有 $\lim_{n \to \infty} \mu(g_n) \leqslant \varepsilon \mu([g_1 > 0])$。但 $\varepsilon > 0$是任意的，故有 $\mu(g_n) \downarrow 0$。最终有 $\mu(f_n) = \mu(g_n) + \mu(f) \downarrow \mu(f)$，(5)得证。

现证(6). 若  $\mu(f) = +\infty$，则  $\mu([f > 0]) = \infty$。由于 f 只取有限多个值，故存在 a > 0，使  $\mu([f = a]) = \infty$。我们有  $[f_n > \frac{a}{2}] \uparrow [f > \frac{a}{2}]$， $f_n \geq \frac{a}{2} I_{[f_n > \frac{a}{2}]}$，故有

 
$$
\lim_{n\to\infty}\mu(f_{n})\geqslant\frac{a}{2}\lim_{n\to\infty}\mu\Big(\Big[f_{n}>\frac{a}{2}\Big]\Big)=\frac{a}{2}\mu\Big(\Big[f>\frac{a}{2}\Big]\Big)=\infty.
$$
 

于是 $\mu(f_{n})\uparrow\mu(f)$. 若 $\mu(f)<\infty$，令 $g_{n}=f-f_{n}$，则由(5)知 $\mu(g_{n})\downarrow0$，故 $\mu(f_{n})=\mu(f)-\mu(g_{n})\uparrow\mu(f)$. (6)得证.

最后证明(7). 先固定某个m, 令 $h_{n}=g_{n}\wedge f_{m}$，则 $h_{n}\in S^{+}$， $h_{n}\uparrow f_{m}\in S^{+}$，故由(6)知 $\lim_{n\to\infty}\mu(h_{n})=\mu(f_{m})$。但 $h_{n}\leq g_{n}$，从而有 $\lim_{n\to\infty}\mu(g_{n})\geq\mu(f_{m})$，于是最终有

 
$$
\lim_{n\to\infty}\mu(g_{n})\geqslant\lim_{m\to\infty}\mu(f_{m}).
$$
 

(7) 得证.

注3.1.3 在上述证明中, 我们用到如下事实: 对  $f \in \mathcal{S}^{+}$, 有  $\mu(f) < \infty \Leftrightarrow \mu([f > 0]) < \infty$, 但这一结论不能推广到一般非负可测函数. 因此, 我们未将其列为积分的基本性质.

借助于命题3.1.2, 我们可以给出积分的一般定义. 为方便起见, 我们只考虑F可测函数情形. 所有结果都可以改述为 $\mu$可测函数情形.

定义3.1.4 设 $f$为一非负可测函数. 任取 $f_n \in S^+$, 使 $f_n \uparrow f$(定理1.1.8), 令

 
$$
\mu(f)=\lim_{n\to\infty}\mu(f_{n}).
$$
 

则由命题3.1.2的(4)及(7)知，上述右端极限存在，且不依赖于序列 $(f_n)$的选取，称 $\mu(f)$为 $f$关于 $\mu$的积分。有时也用 $\int_\Omega f\,d\mu$表示 $\mu(f)$。

现设$f$为一可测函数. 令$f^{+}=f\vee0,f^{-}=(-f)\vee0$, 若$\mu(f^{+})<\infty$或$\mu(f^{-})<\infty$, 则称$f$(关于$\mu$的)积分存在. 令

 
$$
\mu(f)=\mu(f^{+})-\mu(f^{-}),
$$
 

称 $\mu(f)$为f关于 $\mu$的积分．若 $\mu(f^{+})<\infty$，且 $\mu(f^{-})<\infty$（或者等价地， $\mu(|f|)<\infty$），则称f关于 $\mu$可积（简称 $\mu$可积）.

设  $\xi = f + ig$ 为一复值可测函数. 如果  $f$ 和  $g$ 都  $\mu$ 可积, 则称  $\xi$ 为  $\mu$ 可积. 这时令  $\mu(\xi) = \mu(f) + i\mu(g)$, 称  $\mu(\xi)$ 为  $\xi$ 关于  $\mu$ 的积分.

注3.1.5 设  $f \in \overline{L}$. 若  $f$ 的积分存在 (相应地,  $f$ 为可积), 则对任何  $A \in \mathcal{F}$,  $fI_A$ 的积分存在 (相应地,  $fI_A$ 为可积). 我们用  $\int_A f \, d\mu$ 表示  $\int_\Omega fI_A \, d\mu$.

---

下一定理列举了积分的一些基本性质.

定理3.1.6 设f,g积分存在.

(1)  $\forall \alpha \in \mathbb{R}, \alpha f$ 的积分存在，且  $\mu(\alpha f) = \alpha \mu(f)$;

(2) 若  $f + g$ 处处有定义，且  $\mu(f) + \mu(g)$ 有意义（即不出现  $\infty - \infty$），则  $f + g$ 的积分存在，且有  $\mu(f + g) = \mu(f) + \mu(g)$;

(3)  $|\mu(f)| \leqslant \mu(|f|);$

(4) 若 N 为一零测集，则  $\mu(fI_{N}) = 0;$

(5) 若  $f \leqslant g$，a.e.，则  $\mu(f) \leqslant \mu(g)$;

(6) 若  $f \in \overline{\mathcal{L}}^{+}$，则  $f = 0$，a.e.  $\Leftrightarrow \mu(f) = 0$;

(7) 若  $f \in \overline{L}^{+}$，且  $\mu(f) < \infty$，则  $f < \infty$，a.e.，且  $[f > 0]$ 关于  $\mu$ 为  $\sigma$ 有限的。

证 (1)–(4) 直接由定义3.1.4推得. 往证(5). 令  $N = [f > g]$，则依假定  $\mu(N) = 0$，我们有

 
$$
f=fI_{N^{c}}+fI_{N},\quad g=gI_{N^{c}}+gI_{N},\quad fI_{N^{c}}\leqslant gI_{N^{c}}.
$$
 

故由4知

 
$$
\mu(f)=\mu(f I_{N^{c}}),\mu(g)=\mu(g I_{N^{c}}).
$$
 

但由积分的定义易知 $\mu(fI_{N^{c}})\leqslant\mu(gI_{N^{c}})$，从而有 $\mu(f)\leqslant\mu(g)$.

现证(6). “⇒”由(5)推得，我们反证“⇐”. 假设 $\mu([f>0])>0$. 由于 $[f>0]=\bigcup_{n=1}^{\infty}[f\geq\frac{1}{n}]$，故存在某n，使 $\mu([f\geq\frac{1}{n}])>0$. 我们有 $f\geq\frac{1}{n}I_{[f\geq\frac{1}{n}]}$，从而

 
$$
\mu(f)\geqslant\frac{1}{n}\mu\big([f\geqslant\frac{1}{n}]\big)>0.
$$
 

“ $\Leftrightarrow$”得证.

最后证明(7). 设  $f \in \overline{L}^{+}$. 假定  $\mu([f = +\infty]) > 0$, 则由于  $f \geqslant \infty I_{[f = \infty]}$, 故  $\mu(f) = \infty$, 这表明  $\mu(f) < \infty \Rightarrow f < \infty$, a.e.. 此外有  $[f > 0] = \bigcup_{n=1}^{\infty} [f \geqslant \frac{1}{n}], \mu([f \geqslant \frac{1}{n}]) \leqslant n\mu(f) < \infty$, 故  $[f > 0]$ 关于  $\mu$ 为  $\sigma$ 有限的.

系3.1.7 (1) 设f, g积分存在，且f = g，a.e.，则 $\mu(f) = \mu(g)$.

(2) 设  $f$ 为  $\mu$ 可积，则  $|f| < \infty$，a.e..

(3) 设 f, g 积分存在，且  $\mu(f) + \mu(g)$ 有意义，则  $f + g$ a.e. 有意义.

(4) 设  $f, g$ 积分存在，且  $f \leqslant g$，a.e.，则对一切  $A \in \mathcal{F}$，有  $\mu(fI_A) \leqslant \mu(gI_A)$.

下一命题表明: 在一定条件下, 上述(4)的逆命题成立.

命题3.1.8 设f,g积分存在，且对一切 $A\in\mathcal{F}$，有 $\mu(fI_A)\leq\mu(gI_A)$.

(1) 若 f, g 可积，则  $f \leqslant g$，a.e.;

(2) 若  $\mu$ 为  $\sigma$ 有限测度，则  $f \leqslant g$，a.e.

证 (1)  $\forall A \in \mathcal{F}$，由假定

 
$$
\mu((f-g)I_{A})=\mu(f I_{A})-\mu(g I_{A})\leqslant0.
$$
 

---

特别，令 $A=[f>g]$，则有 $\mu((f-g)I_{A})\geq0$，从而由上式知 $\mu((f-g)I_{A})=0$，于是 $(f-g)I_{A}=0$，a.e.(定理3.1.6(6))。由于在A上有 $f>g$，故必须有 $\mu(A)=0$，即有 $f\leq g$，a.e.

(2) 设  $\mu$ 为  $\sigma$ 有限测度. 我们用反证法证明  $f \leqslant g$, a.e.. 假定  $\mu([g < f]) > 0$, 令

 
$$
A_{n}=\left[g<f-\frac{1}{n}\right]\cap[|f|<n],B_{m}=[g<m]\cap[f=+\infty],
$$
 

则 $[g < f] = (\bigcup_n A_n) \cup (\bigcup_m B_m)$。于是存在某 $n$或 $m$，使 $\mu(A_n) > 0$或 $\mu(B_m) > 0$。假定 $\mu(A_n) > 0$，由 $\mu$的 $\sigma$有限性知，存在 $A \subset A_n, A \in \mathcal{F}$，使得 $0 < \mu(A) < \infty$，这时有

 
$$
\int_{A}g d\mu\leqslant\int_{A}(f-\frac{1}{n})d\mu=\int_{A}f d\mu-\frac{1}{n}\mu(A)<\int_{A}f d\mu.
$$
 

这与假定 $\int_A f\,d\mu \leq \int_A g\,d\mu$矛盾．若 $\mu(B_m) > 0$，类似论证可导致矛盾，因此必须有 $f \leq g$，a.e..

系3.1.9 设f,g积分存在，且对一切 $A\in\mathcal{F}$有 $\mu(fI_{A})=\mu(gI_{A})$.

(1) 若 f, g 可积，则 f = g, a.e.;

(2) 若  $\mu$ 为  $\sigma$ 有限，则  $f = g$，a.e.

##### 习题

3.1.1 举例说明命题3.1.8(2)中关于 $\mu$的 $\sigma$有限性条件不能去掉.

3.1.2 证明系3.1.7(3).

3.1.3 设 $(f_n)$为一列可测函数. 若 $(f_n)$a.e.单调增(即 $\forall n, f_n \leqslant f_{n+1}, a.e.$), 则存在一处处单调增序列 $(g_n)$, 使得 $\forall n, f_n = g_n$, a.e..

3.1.4 设 $(\Omega,\mathcal{F},\mu)$为一有限测度空间， $A_{i}\in\mathcal{F},1\leqslant i\leqslant n$。证明

 
$$
\mu\big(\bigcup_{k=1}^{n}A_{k}\big)\geqslant\sum_{k=1}^{n}\mu(A_{k})-\sum_{1\leqslant k<j\leqslant n}\mu(A_{k}\cap A_{j}),
$$
 

 
$$
\mu\big(\bigcup_{k=1}^{n}A_{k}\big)=\sum_{I\subset\{1,\cdots,n\}}(-1)^{|I|-1}\mu(\bigcap_{i\in I}A_{i}),
$$
 

其中 $|I|$表示I中元素的个数。(提示: 证明)

 
$$
\sum_{k=1}^{n}I_{A_{k}}\leqslant I_{\cup_{k=1}^{n}A_{k}}+\sum_{1\leqslant k<j\leqslant n}I_{A_{k}\cap A_{j}},
$$
 

 
$$
\bigvee_{k=1}^{n}I_{A_{k}}=\sum_{I\subset\{1,\cdots,n\}}(-1)^{|I|-1}\bigwedge_{i\in I}I_{A_{i}}.
$$
 

3.1.5 设E为一距离空间， $\mathcal{B}(E)$为其Borel  $\sigma$ 代数， $\mu$ 与  $\nu$ 为  $(E, \mathcal{B}(E))$ 上的两个有限测度。若对E上一切有界连续函数 $f$ 有  $\mu(f) = \nu(f)$，则  $\mu = \nu$（提示：利用习题2.1.5）。

---

3.1.6 设 $(\Omega,\mathcal{F})$及 $(E,\mathcal{E})$为两个可测空间， $f$为 $(\Omega,\mathcal{F})$到 $(E,\mathcal{E})$中的可测映射， $\mu$为 $(\Omega,\mathcal{F})$上一测度.

(1) 令  $\mu f^{-1}(A) = \mu(f^{-1}(A)), A \in \mathcal{E}$. 证明  $\mu f^{-1}$ 为  $(E, \mathcal{E})$ 上的测度 (通常称为由  $f$ 在  $(E, \mathcal{E})$ 上导出的测度或  $f$ 的像测度).

(2) 设  $g$ 为  $(E, \mathcal{E})$ 上的可测函数. 证明: 为要  $g$ 关于测度  $\mu f^{-1}$ 的积分存在 (相应地, 可积), 必须且只需  $g \circ f$ 关于  $\mu$ 的积分存在 (相应地, 可积). 此外, 这时有

 
$$
\int_{\Omega}g\circ f d\mu=\int_{E}g d(\mu f^{-1}).
$$
 

(3) 设  $F^{\mu}$ 和  $E^{\nu}$ 分别表示 F 和 E 关于  $\mu$ 和  $\nu$ 的完备化. 证明 f 为  $(\Omega, \mathcal{F}^{\mu})$ 到  $(E, E^{\nu})$ 中的可测映射.

3.1.7 设 $(\Omega,\mathcal{F},\mu)$为一有限测度空间，在 $\mathcal{F}$可测实值函数全体构成的线性空间 $\mathcal{L}$上定义距离 $d(f,g)=\mu(|f-g|\wedge1)$，证明按此距离收敛等价于按测度收敛.

## 3.2 积分号下取极限

本节我们将介绍有关积分号下取极限的几个定理(单调收敛定理, Fatou引理, 控制收敛定理).

引理3.2.1 设 $f_n \in \overline{\mathcal{L}}^+$,  $n \geq 1$,  $f \in \overline{\mathcal{L}}^+$.

(1) 若  $f_{n} \leqslant f_{n+1}$, a.e.,  $\forall n \geqslant 1$, 且  $f_{n} \xrightarrow{\text{a.e.}} f$, 则  $\lim_{n \to \infty} \mu(f_{n}) = \mu(f)$;

(2) 若  $f_{n} \geqslant f_{n+1}$, a.e.,  $\forall n \geqslant 1$,  $f_{n} \xrightarrow{\text{a.e.}} f$, 且  $\mu(f_{1}) < \infty$, 则  $\lim_{n \to \infty} \mu(f_{n}) = \mu(f)$.

证 (1) 不妨设 $(f_{n})$处处单调增，且 $f_{n}\uparrow$f处处成立。对每个 $n,$令 $f_{n,m}\in\mathcal{S}^{+}$，使得 $f_{n,m}\uparrow f_{n}(m\to\infty)$。令 $g_{m}=\bigvee_{i=1}^{m}f_{i,m}$，则 $g_{m}\in\mathcal{S}^{+},g_{m}\uparrow f,$且 $g_{m}\leq f_{m}$，故由积分的定义有

 
$$
\mu(f)=\lim_{m\to\infty}\mu(g_{m})\leqslant\lim_{m\to\infty}\mu(f_{m}).
$$
 

但恒有 $\mu(f)\geqslant\mu(f_{m})$，故有 $\lim_{m\to\infty}\mu(f_{m})=\mu(f)$.

(2) 不妨设 $(f_n)$处处单调降，且 $f_n \downarrow f$处处成立。由于假定 $\mu(f_1) < \infty$，故 $\mu([f_1 = \infty]) = 0$。令 $\overline{f}_n = f_n I_{[f_1 < \infty]}$， $\overline{f} = f I_{[f_1 < \infty]}$，则 $\overline{f}_n \downarrow \overline{f}$， $\overline{f}_n$为实值可测函数。令 $g_n = \overline{f}_1 - \overline{f}_n$，则 $g_n \uparrow \overline{f}_1 - \overline{f}$，故由(1)推知， $\mu(g_n) \uparrow \mu(\overline{f}_1) - \mu(\overline{f})$，即有 $\mu(f_n) = \mu(\overline{f}_n) \downarrow \mu(\overline{f})$。

系3.2.2 设 $f_{n}\in\overline{L}^{+},n\geqslant1$，则有 $\mu(\sum_{n}f_{n})=\sum_{n}\mu(f_{n})$.

证 令 $g_{n}=\sum_{i=1}^{n}f_{i},g=\sum_{i=1}^{\infty}f_{i}$，则 $g_{n}\uparrow g$，故有

 
$$
\mu(g)=\lim_{n\to\infty}\mu(g_{n})=\lim_{n\to\infty}\sum_{i=1}^{n}\mu(f_{i})=\sum_{i=1}^{\infty}\mu(f_{i}).
$$
 

---

定理3.2.3 (单调收敛定理) 设 $f_n \in \overline{\mathcal{L}}, n \geq 1$，且每个 $f_n$的积分存在，则

(1) 设 $(f_n)$ a.e. 单调增，且 $f_n \to f$，a.e.. 若 $\mu(f_1) > -\infty$，则 $f$的积分存在，且 $\mu(f_n) \uparrow \mu(f)$;

(2) 设 $(f_n)$ a.e. 单调降，且 $f_n \to f$，a.e.. 若 $\mu(f_1) < +\infty$，则 $f$的积分存在，且 $\mu(f_n) \downarrow \mu(f)$.

证 先证(1). 由假定,  $f_{n}^{+}$a.e. 单调增,  $f_{n}^{-}$a.e. 单调降, 且有  $f_{n}^{+} \xrightarrow{\text{a.e.}} f^{+}$,  $f_{n}^{-} \xrightarrow{\text{a.e.}} f^{-}$. 由于  $f_{1}^{-} \geqslant f^{-}$, 且  $\mu(f_{1}) > -\infty$,  $f_{n}^{-} > -\infty$, 故  $\mu(f^{-}) \leqslant \mu(f_{1}^{-}) < \infty$. 从而 f 的积分存在, 且由引理 3.2.1 知:  $\mu(f_{n}^{+}) \uparrow \mu(f^{+})$,  $\mu(f_{n}^{-}) \downarrow \mu(f^{-})$. 因此有  $\mu(f_{n}) \uparrow \mu(f)$. (1) 得证. 对  $(-f_{n})$ 应用(1) 即得(2).

定理3.2.4 (Fatou引理) 设 $f_n \in \overline{\mathcal{L}}, n \geq 1$，且每个 $f_n$的积分存在。

(1) 若存在  $g \in \overline{\mathcal{L}}, \mu(g) > -\infty$，使得  $\forall n \geq 1$ 有  $f_n \geq g$，a.e.，则  $\liminf_{n \to \infty} f_n$ 积分存在，且有

 
$$
\mu(\liminf_{n\to\infty}f_{n})\leqslant\liminf_{n\to\infty}\mu(f_{n}).
$$
 

(2) 若存在  $g \in \overline{\mathcal{L}}, \mu(g) < \infty$，使得  $\forall n \geq 1$ 有  $f_n \leq g$，a.e.，则  $\limsup_{n \to \infty} f_n$ 的积分存在，且有

 
$$
\mu(\limsup_{n\to\infty}f_{n})\geqslant\limsup_{n\to\infty}\mu(f_{n}).
$$
 

证 先证(1). 令  $g_{n} = \inf_{k \geq n} f_{k}$，则  $g_{n} \uparrow \liminf_{n \to \infty} f_{n}$，且  $g_{1} \geq g$，a.e. 于是  $\mu(g_{1}) \geq \mu(g) > -\infty$。故由定理3.2.3(1)， $\liminf_{n \to \infty} f_{n}$ 的积分存在，且有

 
$$
\mu(\liminf_{n\to\infty}f_{n})=\lim_{n\to\infty}\mu(g_{n})\leqslant\liminf_{n\to\infty}\mu(f_{n}).
$$
 

(1)得证. 对 $(-f_{n})$应用(1)即得(2).

定理3.2.5 (控制收敛定理) 设  $f_n \in \mathcal{L}$，且  $f \in \mathcal{L}$， $f_n \xrightarrow{\text{a.e.}} f$ 或  $f_n \xrightarrow{\mu} f$。若存在一非负可积函数  $g$，使得  $\forall n \geq 1$ 有  $|f_n| \leq g$，a.e.，则  $f$ 可积，且有  $\lim_{n \to \infty} \mu(f_n) = \mu(f)$。

证 由于  $|f| \leqslant g$, a.e., 故  $f$ 可积. 若  $f_n \xrightarrow{\text{a.e.}} f$, 则定理的结论直接由定理3.2.4推得. 现设  $f_n \xrightarrow{\mu} f$, 则对  $(f_n)$ 的任一子列  $(f_{n'})$, 存在其子列  $(f_{n'}_k)$, 使得  $f_{n'}_k \xrightarrow{\text{a.e.}} f$ (见定理2.3.4(3)及定理2.3.5). 于是有  $\lim_{n \to \infty} \mu(f_{n'}_k) = \mu(f)$. 但子列  $(f_{n'})$ 的选取是任意的, 故必须有  $\lim \mu(f_n) = \mu(f)$.

下面我们着手推广定理3.2.4及3.2.5.

定理3.2.6 设 $f_n \in \mathcal{L}, f \in \mathcal{L}$，且 $f_n \xrightarrow{\text{a.e.}} f$或 $f_n \xrightarrow{\mu} f$。又设每个 $f_n$的积分存在。

(1) 若存在  $g \in \overline{\mathcal{L}}, \mu(g) > -\infty$，使得  $\forall n \geq 1, f_n \geq g$，a.e.，则  $f$ 的积分存在，且有  $\mu(f) \leq \liminf_{n \to \infty} \mu(f_n)$.

(2) 若存在  $g \in \overline{\mathcal{L}}, \mu(g) < \infty$，使得  $\forall n \geq 1, f_n \leq g$，a.e.，则  $f$ 的积分存在，且有  $\mu(f) \geq \limsup \mu(f_n)$.

---

证 先证(1). 若  $f_{n} \xrightarrow{\sim} f$，则由 Fatou 引理立得(1)的结论. 现设  $f_{n} \xrightarrow{\sim} f$，则对  $(f_{n})$ 的任一子列  $(f_{n}^{\prime})$，存在其子列  $(f_{n_{k}^{\prime}})$，使得  $f_{n_{k}^{\prime}} \xrightarrow{\mathrm{a.e.}} f$. 于是由上所证有  $\mu(f) \leqslant \lim_{k \to \infty} \mu(f_{n_{k}^{\prime}})$. 但子列  $(f_{n^{\prime}})$ 的选取是任意的，故必须有  $\mu(f) \leqslant \liminf_{n \to \infty} \mu(f_{n})$，(1) 得证. 对  $(-f_{n})$ 应用(1)得(2).

下一定理是控制收敛定理的推广形式, 其进一步推广见习题3.2.1.

定理3.2.7 设  $f_{n} \in \mathcal{L}$，且  $f_{n} \xrightarrow{\mathrm{a.e.}} f$ 或  $f_{n} \xrightarrow{\mu} f$。又设  $g_{n} \in \mathcal{L}^{+}$， $g \in \mathcal{L}^{+}$，且  $g_{n} \xrightarrow{\mathrm{a.e.}} g$ 或  $g_{n} \xrightarrow{\mu} g$。如果 g 及每个  $g_{n}$ 可积， $\mu(g_{n}) \to \mu(g)$，且  $|f_{n}| \leq g_{n}$，a.e.， $\forall n \geq 1$，则有  $\lim_{n \to \infty} \mu(|f_{n} - f|) = 0$。特别有  $\lim_{n \to \infty} \mu(f_{n}) = \mu(f)$。

证 首先假定同时有  $f_{n} \xrightarrow{\mathrm{a.e.}} f, g_{n} \xrightarrow{\mathrm{a.e.}} g.$ 令  $h_{n} = g_{n} + g - |f_{n} - f|$，则  $h_{n} \geqslant 0$，a.e.，且  $h_{n} \xrightarrow{\mathrm{a.e.}} 2g.$ 故由定理3.2.6(1)得

 
$$
2\mu(g)\leqslant\liminf_{n\to\infty}\mu(h_{n})=2\mu(g)-\limsup_{n\to\infty}\mu(|f_{n}-f|).
$$
 

从而有  $\lim_{n\to\infty}\mu(|f_{n}-f|)=0$ 。特别有

 
$$
|\mu(f_{n})-\mu(f)|\leqslant\mu(|f_{n}-f|)\to0.
$$
 

若同时有 $f_n \xrightarrow{\mu} f, g_m \xrightarrow{\mu} g$，则 $h_n \xrightarrow{\mu} 2g$。故由定理3.2.6(1)亦可推得本定理的结论。若 $f_n \xrightarrow{\text{a.e.}} f, g_n \xrightarrow{\mu} g$，或 $f_n \xrightarrow{\mu} f, g_n \xrightarrow{\text{a.e.}} g$，则与定理3.2.6的证明类似可以证明 $\lim_{n \to \infty} \mu(|f_n - f|) = 0$。

系3.2.8 (Scheffé引理) 设 $f_n$,  $f$为可积可测函数, $f_n \xrightarrow{\text{a.e.}} f$, 则 $\mu(|f_n - f|) \to 0$, 当且仅当 $\mu(|f_n|) \to \mu(|f|)$.

证 必要性显然, 充分性由定理3.2.7推得(令 $g_{n}=|f_{n}|, g=|f|$).

定理3.2.9 设 $f_{n}, f$为可积可测函数，则下列二条件等价：

(1)  $\mu(|f_n - f|) \to 0;$

(2)  $f_n \xrightarrow{\mu} f$，且  $\mu(|f_n|) \to \mu(|f|)$.

证  $(2)\Rightarrow(1)$. 设(2)成立. 在定理3.2.7中令 $g_{n}=|f_{n}|,g=|f|$，即得(1). 现证 $(1)\Rightarrow(2)$. 设 $\mu(|f_{n}-f|)\rightarrow0$，对任给 $\varepsilon>0$，令 $A_{n}=||f_{n}-f|\geq\varepsilon|$，则有

 
$$
\varepsilon I_{A_{n}}\leqslant|f_{n}-f|I_{A_{n}}\leqslant|f_{n}-f|,
$$
 

故有

 
$$
\lim_{n\to\infty}\varepsilon\mu(A_{n})\leqslant\lim_{n\to\infty}\mu(|f_{n}-f|)=0.
$$
 

这表明 $f_{n} \xrightarrow{\mu} f$，此外，由于 $|f_{n}| - |f| \leqslant |f_{n} - f|$，故有

 
$$
|\mu(|f_{n}|)-\mu(|f|)|\leqslant\mu(|f_{n}-f|)\to0,\;n\to\infty.
$$
 

 $(1)\Rightarrow(2)$ 得证.

---

##### 习题

3.2.1 设  $f_{n}, h_{n}, g_{n}, f, h, g \in \mathcal{L}, h_{n} \leqslant f_{n} \leqslant g_{n}, \mathrm{a.e.} \forall n \geqslant 1$. 又设  $f_{n} \xrightarrow{\mathrm{a.e.}} f$ 或  $f_{n} \xrightarrow{\mu} f, g_{n} \xrightarrow{\mathrm{a.e.}} g$ 或  $g_{n} \xrightarrow{\mu} g, h_{n} \xrightarrow{\mathrm{a.e.}} h$ 或  $h_{n} \xrightarrow{\mu} h$. 如果  $h, g, h_{n}, g_{n}$ 都可积, 且  $\mu(h_{n}) \rightarrow \mu(h), \mu(g_{n}) \rightarrow \mu(g)$, 则 f 可积, 且有  $\lim_{n \to \infty} \mu(f_{n}) = \mu(f)$ (提示: 不妨设  $f_{n} \xrightarrow{\mathrm{a.e.}} f, g_{n} \xrightarrow{\mathrm{a.e.}} g, h_{n} \xrightarrow{\mathrm{a.e.}} h$. 分别对  $f_{n} - h_{n}$ 及  $g_{n} - f_{n}$ 应用 Fatou 引理).

3.2.2 若3.2.1中有 $h_{n}\leqslant0\leqslant g_{n}$，则 $\lim_{n\to\infty}\mu(|f_{n}-f|)=0$（提示：对 $|f_{n}-f|\leqslant g_{n}-h_{n}+g-h$应用定理3.2.7）.

3.2.3 设 $(f_{n})$为一可测函数列. 若 $\sum_{n=1}^{\infty}\mu(f_{n}^{+})<\infty$，或 $\sum_{n=1}^{\infty}\mu(f_{n}^{-})<\infty$，则 $\sum_{n=1}^{\infty}f_{n}$

a.e. 有意义， $\sum_{n=1}^{\infty}f_{n}$ 的积分存在，且有  $\mu(\sum_{n=1}^{\infty}f_{n})=\sum_{n=1}^{\infty}\mu(f_{n}).$

## 3.3 不定积分与符号测度

本节主要内容有：符号测度的Jordan-Hahn分解,测度的绝对连续性及奇异性,测度的Lebesgue分解及Radon-Nikodym定理,Vitali-Hahn-Saks定理.

引理3.3.1 设 $f \in \overline{\mathcal{L}}$，且f的积分存在。令

$$
\nu(A)=\mu(f I_{A}),\;A\in\mathcal{F},   \tag*{(3.3.1)}
$$

则 $\nu$为F上的 $\sigma$可加集函数，即有

$$
\{A_{n},n\geqslant1\}\subset\mathcal{F},A_{n}\cap A_{m}=\varnothing,n\neq m\Rightarrow\nu(\sum_{n}A_{n})=\sum_{n}\nu(A_{n}).   \tag*{(3.3.2)}
$$

此外，令

$$
\nu^{+}(A)=\mu(f^{+}I_{A}),\nu^{-}(A)=\mu(f^{-}I_{A}),\quad A\in\mathcal{F},   \tag*{(3.3.3)}
$$

则 $\nu^{+},\nu^{-}$为 $(\Omega,\mathcal{F})$上的测度，其中之一为有限测度，且有 $\nu=\nu^{+}-\nu^{-}$

证 令  $\nu^{+}, \nu^{-}$ 如 (3.3.2) 式所定义，由系 3.2.2 知， $\nu^{+}$ 及  $\nu^{-}$ 为 F 上的测度。由于 f 的积分存在，我们有  $\nu^{+}(\Omega) < \infty$ 或  $\nu^{-}(\Omega) < \infty$。于是  $\nu^{+} - \nu^{-}$ 在 F 上有定义，且为 F 上的  $\sigma$ 可加集函数。显然有  $\nu = \nu^{+} - \nu^{-}$。

定义3.3.2 设 $(\Omega,\mathcal{F})$为一可测空间， $\nu$为 $\mathcal{F}$上的一 $\sigma$可加集函数，且 $\nu(\varnothing)=0$，称 $\nu$为符号测度。设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $f\in\overline{\mathcal{L}}$，且f的积分存在，则由(3.3.1)式定义的符号测度 $\nu$称为f关于 $\mu$的不定积分，并记为 $\nu=f.\mu$。

设 $\nu$为F上的一 $\sigma$可加复值集函数，称 $\nu$为复测度.这时 $\nu$的实部和虚部均为实值符号测度.

注3.3.3 设  $\nu$ 为  $(\Omega, \mathcal{F})$ 上的一符号测度，则对任何  $A \in \mathcal{F}$，或者  $-\infty \leqslant \nu(A) < \infty$，或者  $-\infty < \nu(A) \leqslant \infty$。事实上，如若不然，则存在  $A \in \mathcal{F}, B \in \mathcal{F}$，使  $\nu(A) = +\infty$，