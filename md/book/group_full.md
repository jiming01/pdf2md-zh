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

(3)  $f_n \xrightarrow{\mu} f$，当且仅当对  $(f_n)$ 的任何子列  $(f_{n'})$，存在其子列  $(f_{n'}_k)$，使得  $f_{n'}_k \xrightarrow{\text{a.un.}} f, k \to \infty$.

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

---

 $\nu(B) = -\infty$. 我们有  $A \cup B = (A \setminus B) \cup B = (B \setminus A) \cup A$, 依假定, 有

 
$$
\nu(A\cup B)=\nu(A\setminus B)+\nu(B),
$$
 

 
$$
\nu(A\cup B)=\nu(B\setminus A)+\nu(A).
$$
 

为了使第一个等式右边有意义, 必须有  $\nu(A \setminus B) < \infty$. 为了使第二个等式右边有意义, 必须有  $\nu(B \setminus A) > -\infty$. 这时分别从两个等式得  $\nu(A \cup B) = -\infty, \nu(A \cup B) = \infty$, 这导致矛盾.

由引理3.3.1知, 不定积分这一特殊的符号测度可以表示为两个测度之差, 且其中之一为有限测度. 下一定理表明: 这一结论对一切符号测度成立.

定理3.3.4 (Jordan-Hahn分解定理) 设ν为(Ω, F)上的一符号测度. 对A ∈ F, 定义

$$
\begin{aligned}&\nu^{+}(A)=\sup\{\nu(B)\mid B\subset A,B\in\mathcal{F}\},\\&\nu^{-}(A)=\sup\{-\nu(B)\mid B\subset A,B\in\mathcal{F}\}.\\ \end{aligned}   \tag*{(3.3.4)}
$$

则 $\nu^{+}$及 $\nu^{-}$为测度，其中之一为有限测度，且有 $\nu=\nu^{+}-\nu^{-}$。此外，存在 $D\in\mathcal{F}$，使得

$$
\nu^{+}(A)=\nu(A\cap D),\;\nu^{-}(A)=-\nu(A\cap D^{c}).   \tag*{(3.3.5)}
$$

证 不妨设  $\nu(A) > -\infty, \forall A \in \mathcal{F}$. 令  $\nu^{+}, \nu^{-}$ 如 (3.3.4) 式定义. 首先, 我们证明存在  $D \in \mathcal{F}$, 使得

$$
A\in\mathcal{F},A\subset D\Rightarrow\nu(A)\geqslant0,A\subset D^{c}\Rightarrow\nu(A)\leqslant0.   \tag*{(3.3.6)}
$$

为此, 令

 
$$
\mathcal{B}=\{B\in\mathcal{F}|\nu^{+}(B)=0\},
$$
 

则 $\mathcal{B} = \{B \in \mathcal{F} \mid \forall C \in \mathcal{F}, C \subset B, \nu(C) \leqslant 0\}$. 易见 $\mathcal{B}$对可列并运算封闭. 此外, 设 $B \in \mathcal{B}, G \in \mathcal{F}, G \subset B$, 则 $G \in \mathcal{B}$. 令 $B_n \in \mathcal{B}, n \geqslant 1$, 使

 
$$
\lim_{n\to\infty}\nu(B_{n})=\inf\{\nu(B)\mid B\in\mathcal{B}\}\hat{=}\beta,
$$
 

则有 $\bigcup_{n}B_{n}\in\mathcal{B}$，且有

 
$$
\beta\leqslant\nu(\bigcup_{n}B_{n})=\nu(B_{m})+\nu(\bigcup_{n}B_{n}\setminus B_{m})\leqslant\nu(B_{m}),\ m\geqslant1,
$$
 

故 $\nu(\bigcup_n B_n) = \beta$。令 $D = (\bigcup_n B_n)^c$，则 $D^c \in \mathcal{B}, \nu(D^c) = \beta$，于是由 $\mathcal{B}$的定义知(3.3.6)式的第二个蕴含关系成立。

再证(3.3.6)式的第一个蕴含关系成立. 我们用反证法. 假定存在 $A \in \mathcal{F}, A \subset D$, 使 $\nu(A) < 0$, 我们断言: 必有 $\nu^+(A) > 0$. 事实上, 若 $\nu^+(A) = 0$, 则 $A \in \mathcal{B}$, 故 $A \cup D^c \in$

---

B. 但有  $\nu(A \cup D^c) = \nu(A) + \nu(D^c) < \nu(D^c) = \beta$，这与  $\beta$ 的定义矛盾。因此必须有  $\nu^+(A) > 0$。由  $\nu^+$ 的定义知，存在  $A_1 \in \mathcal{F}$， $A_1 \subset A$，使得

 
$$
\nu(A_{1})\geqslant\frac{1}{2}(\nu^{+}(A)\wedge1)>0.
$$
 

这时， $A \setminus A_1 \subset D$， $\nu(A \setminus A_1) = \nu(A) - \nu(A_1) < 0$，因此由上所证知 $\nu^+(A \setminus A_1) > 0$。

由归纳法，存在 $A_n \in \mathcal{F}$， $A_n \subset D$， $n \geq 1$，使得 $A_n \subset A \setminus \sum_{k=1}^{n-1} A_k$，且有

$$
\nu(A_{n})\geqslant\frac{1}{2}\big[\nu^{+}\big(A\setminus\sum_{k=1}^{n-1}A_{k}\big)\wedge1\big]>0.   \tag*{(3.3.7)}
$$

由于 $\nu(A)<0$，且有

$$
\nu(A)=\nu\big(A\setminus\sum_{k=1}^{\infty}A_{k}\big)+\sum_{k=1}^{\infty}\nu(A_{k}).   \tag*{(3.3.8)}
$$

故 $\sum_{k=1}^{\infty}\nu(A_{k})<\infty,$特别有 $\lim_{k\to\infty}\nu(A_{k})=0.$因此由(3.3.7)式得

 
$$
\lim_{n\to\infty}\nu^{+}\big(A\setminus\sum_{k=1}^{n-1}A_{k}\big)\wedge1=0,
$$
 

从而有  $\lim_{n\to\infty}\nu^{+}(A\setminus\sum_{k=1}^{n-1}A_{k})=0$ 。由于  $\nu^{+}(A\setminus\sum_{k=1}^{\infty}A_{k})\leqslant\nu^{+}(A\setminus\sum_{k=1}^{n-1}A_{k}),n\geqslant1$ ，故有  $\nu^{+}(A\setminus\sum_{k=1}^{\infty}A_{k})=0$ 。因此，由前面所证，必须有  $\nu(A\setminus\sum_{k=1}^{\infty}A_{k})\geqslant0$ （否则有  $\nu^{+}(A\setminus\sum_{k=1}^{\infty}A_{k})>0$ ） 。这样一来，由(3.3.8)式知  $\nu(A)>0$ ，这与假定  $\nu(A)<0$ 矛盾。因此，(3.3.6)式的第一个蕴含关系成立。

现在证明定理的结论. 设  $A \in \mathcal{F}, B \in \mathcal{F}, B \subset A$, 则

 
$$
\begin{align*}\nu(B)+\nu((A\setminus B)\cap D)&=\nu((A\cap D)\cup B)\\&=\nu(A\cap D)+\nu(B\cap D^{c}).\end{align*}
$$
 

故由(3.3.6)式知 $\nu(B) \leqslant \nu(A \cap D)$，从而有 $\nu^+(A) = \nu(A \cap D^c)$。同理可证 $\nu^-(A) = -\nu(A \cap D^c)$。因此， $\nu^+$及 $\nu^-$为 $(\Omega, \mathcal{F})$上的测度，且 $\nu^-(Q) = -\nu(D^c) < \infty$，此外有 $\nu = \nu^++ \nu^-$。

注3.3.5 (1) 我们称  $\nu$ 的分解  $\nu = \nu^{+} - \nu^{-}$ 为  $\nu$ 的 Jordan 分解， $\nu^{+}$ 及  $\nu^{-}$ 分别称为  $\nu$ 的正部及负部；称  $\Omega$ 的分解  $\Omega = D \cup D^{c}$ 为  $\nu$ 的 Hahn 分解。Hahn 分解不一定唯一。

(2) 令  $|\nu| = \nu^+ + \nu^-$，称  $|\nu|$ 为  $\nu$ 的变差 (测度)，称  $|\nu|(\Omega)$ 为  $\nu$ 的全变差，记为  $||\nu||_{\text{var}}$。若  $|\nu|$ 为  $\sigma$ 有限测度，则称  $\nu$ 为  $\sigma$ 有限符号测度。

(3) 设  $\nu$ 为一符号测度,  $f \in \overline{\mathcal{L}}$. 若  $f$ 关于  $|\nu|$ 的积分存在, 则称  $f$ 关于  $\nu$ 的积分存在, 并令  $f \cdot \nu = f \cdot \nu^+ - f \cdot \nu^-$.

---

(4) 设  $\nu$ 为一符号测度,  $\Omega = D \cup D^c$ 为其 Hahn 分解. 令  $h = I_D - I_{D^c}$, 则  $h$ 关于  $|\nu|$ 及  $\nu$ 积分存在, 且  $\nu = h.|\nu|, |\nu| = h.\nu$.

命题3.3.6 设ν为(Ω, F)上的符号测度, 则ν在F上达到其上、下界. 确切地说, 设Ω = D ∪ Dᵏ为其Hahn分解, 则

$$
\nu(D)=\sup\{\nu(B)\mid B\in\mathcal{F}\},\ \nu(D^{c})=\inf\{\nu(B)\mid B\in\mathcal{F}\}.   \tag*{(3.3.9)}
$$

特别, 实值符号测度必然为有界符号测度.

证 设 $B \in \mathcal{F}$，则由定理3.3.4知

 
$$
\begin{aligned}&\nu(B)=\nu^{+}(B)-\nu^{-}(B)\leqslant\nu^{+}(B)\leqslant\nu^{+}(\Omega)=\nu(D),\\&\nu(B)=\nu^{+}(B)-\nu^{-}(B)\geqslant-\nu^{-}(B)\geqslant-\nu^{-}(\Omega)=\nu(D^{c}).\\ \end{aligned}
$$
 

由此推得3.3.9式.

下面我们引进测度的绝对连续性及奇异性概念.

定义3.3.7 设 $\nu_{1},\nu_{2}$为 $(\Omega,\mathcal{F})$上的两个符号测度. 如果

$$
A\in\mathcal{F},|\nu_{2}|(A)=0\Rightarrow|\nu_{1}|(A)=0,   \tag*{(3.3.10)}
$$

则称 $\nu_1$关于 $\nu_2$绝对连续(记为 $\nu_1 \ll \nu_2$). 若 $\nu_1 \ll \nu_2$且 $\nu_2 \ll \nu_1$, 则称 $\nu_1$与 $\nu_2$等价, 记为 $\nu_1 \sim \nu_2$. 若存在 $N \in \mathcal{F}$, 使得 $|\nu_1|(N^c) = 0, |\nu_2|(N) = 0$, 则称 $\nu_1$与 $\nu_2$相互奇异(记为 $\nu_1 \perp \nu_2$).

设 $\nu$为 $(\Omega, \mathcal{F})$上的一符号测度，若 $N \in \mathcal{F}$，使得 $|\nu|(N^c) = 0$，则称 $N$为 $\nu$的支撑。一般说来，支撑并非唯一确定。

由上述定义知,  $\nu_1 \ll \nu_2 \Leftrightarrow$ 凡  $\nu_2$ 的支撑必为  $\nu_1$ 的支撑;  $\nu_1 \perp \nu_2 \Leftrightarrow \nu_1$ 与  $\nu_2$ 有不相交的支撑.

注3.3.8 (1)由(3.3.4)式易知，(3.3.10)式等价于如下条件：

$$
A\in\mathcal{F},\;|\nu_{2}|(A)=0\Rightarrow\nu_{1}(A)=0.   \tag*{(3.3.11)}
$$

(2) 设  $\nu_{1} \ll \nu_{2}$，且  $\nu_{1} \perp \nu_{2}$，则  $\nu_{1} = 0$ (即对一切  $A \in \mathcal{F}$，有  $\nu_{1}(A) = 0$)，此外，恒有  $\nu \perp 0$.

(3) 设  $\nu$ 为一符号测度,  $f \in \overline{\mathcal{L}}$. 若  $f$ 关于  $\nu$ 的积分存在, 则  $f \cdot \nu \ll \nu$.

引理3.3.9 设 $(\Omega,\mathcal{F},\mu)$为测度空间， $h$为一非负可测函数，令 $h.\mu$表示 $h$关于 $\mu$的不定积分（从而 $h.\mu$为一测度）。设 $g\in\overline{\mathcal{L}}$，则 $g$关于 $h.\mu$的积分存在，当且仅当 $gh$关于 $\mu$的积分存在。这时有

$$
\int_{A}g d(h.\mu)=\int_{A}g h d\mu,\quad\forall A\in\mathcal{F}.   \tag*{(3.3.12)}
$$


---

证 首先, 设  $g$ 为非负简单函数, 则由  $h.\mu$ 的定义知  $(3.3.12)$ 式成立. 于是由积分的单调收敛定理知, 对一切  $g \in \overline{\mathcal{L}}^{+}$,  $(3.3.12)$ 式成立. 由此立刻推得引理的结论. ☐

下一定理表明：任一σ有限符号测度ν总可以唯一地分解为关于另一σ有限符号测度μ的绝对连续部分和奇异部分之和.

定理3.3.10 设 $\mu$与 $\nu$为 $(\Omega,\mathcal{F})$上的两个 $\sigma$有限符号测度，则 $\nu$有如下唯一分解(称为Lebesgue分解):

$$
\nu=\nu_{s}+\nu_{c},   \tag*{(3.3.13)}
$$

其中$\nu_s \perp \mu, \nu_c \ll \mu$. 此外，$\nu_s$及$\nu_c$均为$\sigma$有限的，并且存在$N \in \mathcal{F}, g \in \mathcal{L}$，使得$|\mu|(N) = 0, \nu_s(A) = \nu_s(A \cap N)$，$g$关于$|\mu|$的积分存在，$\nu_c$为$g$关于$\mu$的不定积分。

证 首先不妨假定μ为测度(否则以 $|\mu|$代替 $\mu$), 且 $\mu(\Omega)>0$. 这时由 $\mu$的 $\sigma$有限性知, 存在 $\Omega$的一个可数划分 $\Omega=\sum_{n=1}^{\infty}A_{n}$, 使得 $A_{n}\in\mathcal{F}, 0<\mu(A_{n})<\infty,\forall n\geq1$. 令

 
$$
h=\sum_{n=1}^{\infty}\frac{1}{2^{n}\mu(A_{n})}I_{A_{n}},
$$
 

则$h$处处严格正，且$\mu(h)=1$。令$\widetilde{\mu}=h.\mu$，则$\widetilde{\mu}$为测度，且$\widetilde{\mu}(\Omega)=1$。由于$\widetilde{\mu}$与$\mu$等价，故由引理3.3.9知，可以$\widetilde{\mu}$代替$\mu$来证明定理的结论。因此，不妨设$\mu$为有限测度。

下面先假定 $\nu$也为有限测度. 令

 
$$
\mathcal{H}=\Big\{h\in\overline{{\mathcal{L}}}^{+}\mid\forall A\in\mathcal{F},\int_{A}h d\mu\leqslant\nu(A)\Big\},
$$
 

设 $h_1, h_2 \in \mathcal{H}, h = h_1 \lor h_2$，则

 
$$
\begin{align*}\int_{A}h d\mu&=\int_{A\cap[h_{1}\geqslant h_{2}]}h_{1}d\mu+\int_{A\cap[h_{1}<h_{2}]}h_{2}d\mu\\&\leqslant\nu(A\cap[h_{1}\geqslant h_{2}])+\nu(A\cap[h_{1}<h_{2}])=\nu(A),\end{align*}
$$
 

这表明H对有限上端运算封闭. 现设 $h_n \in \mathcal{H}, h_n \uparrow g$, 使得

 
$$
\int_{\Omega}g d\mu=\sup\Big\{\int_{\Omega}h d\mu\mid h\in\mathcal{H}\Big\},
$$
 

则由积分单调收敛定理易知 $g \in \mathcal{H}$。令

 
$$
\nu_{s}(A)=\nu(A)-\int_{A}g d\mu,\quad A\in\mathcal{F},
$$
 

则 $\nu_s$为一有限测度。往证 $\nu_s \perp \mu$。令 $\Omega = D_n + D_n^c$为符号测度 $\nu_s - \frac{1}{n}\mu$的Hahn分解，则对一切 $A \in \mathcal{F}$，

 
$$
\nu_{s}(A\cap D_{n})\geqslant n^{-1}\mu(A\cap D_{n})=n^{-1}\int_{A}I_{D_{n}}d\mu.
$$
 

---

于是 $\forall A \in \mathcal{F}$有

 
$$
\int_{A}(g+n^{-1}I_{D_{n}})d\mu\leqslant\int_{A}g d\mu+\nu_{s}(A\cap D_{n})\leqslant\nu(A),
$$
 

这表明 $g+n^{-1}I_{D_n}\in\mathcal{H}$. 但另一方面 $\mu(g)=\sup\{\mu(h)\mid h\in\mathcal{H}\}$，故必须有 $\mu(D_n)=0$.

令 $N=\bigcup_{n}D_{n}$，则 $\mu(N)=0$。此外我们有(注意 $\left(\nu_{s}-\frac{1}{n}\mu\right)\left(D_{n}^{c}\right)\leqslant0$)

 
$$
\nu_{s}(N^{c})\leqslant\nu_{s}(D_{n}^{c})\leqslant n^{-1}\mu(D_{n}^{c})\leqslant n^{-1}\mu(\Omega)\to0,\quad n\to\infty,
$$
 

这表明 $\nu_{s} \perp \mu$. 令

 
$$
\nu_{c}(A)=\int_{A}g d\mu,
$$
 

则 $\nu_{c}\ll\mu$（见定理3.1.6(3)）。此外，由于 $g$为 $\mu$可积的，故 $g$可取为实值可测函数。

现设ν为σ有限符号测度. 为证定理结论, 不妨假定ν为σ有限测度(否则分别考虑ν^{+}及ν^{-}). 取Ω的一个可数划分Ω = ∑n A_n, 使得A_n ∈ ℝ, ν(A_n) < ∞, n ≥ 1. 令ν^n(A) = ν(A ∩ A_n), 则每个ν^n为有限测度, 故由上所证, ν^n有如下分解:

 
$$
\nu^{n}=\nu_{s}^{n}+\nu_{c}^{n},\quad n\geqslant1,
$$
 

其中 $\nu_s^n \perp \mu, \nu_c^n \ll \mu$，且存在非负实值可测函数 $g_n$，使得 $\nu_c^n = g_n \cdot \mu$。显然， $g_n$在 $A_n^c$上可取为0，令

 
$$
\nu_{s}=\sum_{n}\nu_{s}^{n},\quad\nu_{c}=\sum_{n}\nu_{c}^{n},\quad g=\sum_{n}g_{n},
$$
 

则有 $\nu_s \perp \mu, \nu_c \ll \mu, \nu_c = g. \mu$，且(3.3.13)式成立。 $\nu$的分解唯一性容易由注3.3.8(2)看出。

设 $\mu$为一测度, $\nu$为某 $f\in\overline{L}$关于 $\mu$的不定积分,则 $\nu$关于 $\mu$绝对连续(见注3.3.8(2)).

下一定理表明:若 $\mu$为 $\sigma$有限测度,则逆命题成立.

定理3.3.11 (Radon-Nikodym定理) 设$(\Omega,\mathcal{F})$为一可测空间，$\mu$为一$\sigma$有限测度，$\nu$为一符号测度（不必为$\sigma$有限）。如果$\nu$关于$\mu$绝对连续，则存在一关于$\mu$积分存在的可测函数$g$，使得$\nu=g.\mu$. 此外，$g$在$\mu$等价意义下是唯一的（称$g_1,g_2$为$\mu$等价的，是指$\mu([g_1\neq g_2])=0$），为要$g$为$\mu$-a.e.有限，必须且只需$\nu$为$\sigma$有限的。

证 若  $\nu$ 为  $\sigma$ 有限符号测度，则由定理3.3.10立刻推得本定理结论(因为这时由注3.3.8(2)知(3.3.13)式中的  $\nu_s = 0$)。为证定理，可设  $\nu$ 为测度(否则分别考虑  $\nu^+$ 及  $\nu^-$)，且  $\nu(\Omega) = \infty$。此外由  $\mu$ 的  $\sigma$ 有限性及引理3.3.9知，不妨假定  $\mu$ 为有限测度(参看定理3.3.10证明的开头部分)。令

 
$$
\mathcal{G}=\{C\in\mathcal{F}\mid\nu(C)<\infty\},
$$
 

---

显然 $\mathcal{G}$对有限并运算封闭. 于是存在 $C_n \in \mathcal{G}, C_n \uparrow C$, 使得

$$
\mu(C)=\sup\{\mu(G)\mid G\in\mathcal{G}\}.   \tag*{(3.3.14)}
$$

令

 
$$
\nu^{\prime}(B)=\nu(B\cap C),\quad\nu^{\prime\prime}(B)=\nu(B\cap C^{c}),\quad B\in\mathcal{F},
$$
 

则 $\nu'$为 $\sigma$有限测度，且 $\nu' \ll \mu$，故存在非负实值可测函数 $g'$，使得 $\nu' = g'\cdot\mu$。另一方面，由 $\mathcal{G}$的定义及(3.3.14)式知

 
$$
\mu\big(B\cap C^{c})>0\Rightarrow\nu\big(B\cap C^{c}\big)=\infty.
$$
 

因此, 若令 $g'' = (+\infty)I_{Cc}$,  $g = g' + g''$, 则 $\nu'' = g''\cdot\mu$,  $\nu = g\cdot\mu$. 其余结论显然.

定义3.3.12 我们用 $\frac{d\nu}{d\mu}$表示定理3.3.11中的 $g($它在 $\mu$等价意义下唯一确定 $)$，并称 $\frac{d\nu}{d\mu}$为 $\nu$关于 $\mu$的Radon-Nikodym导数.

定理3.3.13 设 $(\Omega,\mathcal{F},\mu)$为一 $\sigma$有限测度空间， $\nu$为 $\mathcal{F}$上的一符号测度，且 $\nu\ll\mu$。令 $g\in\overline{\mathcal{L}}$，则 $g$关于 $\nu$积分存在，当且仅当 $g\frac{d\nu}{d\mu}$关于 $\mu$积分存在，并且这时有

$$
\int_{A}g d\nu=\int_{A}(g\frac{d\nu}{d\mu})d\mu,\forall A\in\mathcal{F}.   \tag*{(3.3.15)}
$$

证 若  $\nu$ 为测度, 则定理的结论由引理3.3.9推得. 现设  $\nu$ 为符号测度. 令  $h = g \frac{d\nu}{d\mu}$, 则有

 
$$
h^{+}=g^{+}\frac{d\nu^{+}}{d\mu}+g^{-}\frac{d\nu^{-}}{d\mu},\quad h^{-}=g^{-}\frac{d\nu^{+}}{d\mu}+g^{+}\frac{d\nu^{-}}{d\mu}.
$$
 

设$g$关于$\nu$积分存在，则$g$关于$\nu^{+}$及$\nu^{-}$积分存在，且$\nu^{+}(g)-\nu^{-}(g)$有意义。于是$g\frac{d\nu^{+}}{d\mu}$及$g\frac{d\nu^{-}}{d\mu}$关于$\mu$积分存在，且有

 
$$
\nu^{+}(g)=\int\left(g\frac{d\nu^{+}}{d\mu}\right)d\mu,\nu^{-}(g)=\int\left(g\frac{d\nu^{-}}{d\mu}\right)d\mu.
$$
 

于是有

 
$$
\begin{align*}\nu^{+}(g)&=\int\big(g^{+}\frac{d\nu^{+}}{d\mu}\big)d\mu-\int\big(g^{-}\frac{d\nu^{+}}{d\mu}\big)d\mu,\\\nu^{-}(g)&=\int\big(g^{+}\frac{d\nu^{-}}{d\mu}\big)d\mu-\int\big(g^{-}\frac{d\nu^{-}}{d\mu}\big)d\mu.\end{align*}
$$
 

由于 $\nu^{+}(g)-\nu^{-}(g)$有意义，则必须有 $\mu(h^{+})<\infty$，或 $\mu(h^{-})<\infty$（请读者自行验证）。因此， $h$关于 $\mu$积分存在，且 $\mu(h)=\nu^{+}(g)-\nu^{-}(g)=\nu(g)$。对 $gI_A$应用这一结果即

---

得(3.3.15)式. 反之, 设$h$关于$\mu$积分存在, 则$\mu(h^+) < \infty$, 或$\mu(h^-) < \infty$, 由此推知$g$关于$\mu^+$及$\mu^-$积分存在, $\nu^+(g) - \nu^-(g)$有意义, 且$\nu(g) = \mu(h)$. 对$gI_A$应用这一结果即得(3.3.15)式.

定理3.3.14 设 $(\Omega,\mathcal{F})$为一可测空间， $\mu$及 $\nu$为 $\mathcal{F}$上的两个 $\sigma$有限测度， $\varphi$为 $\mathcal{F}$上的一符号测度。如果 $\varphi\ll\nu,\nu\ll\mu$，则 $\varphi\ll\mu$，且有

$$
\frac{d\varphi}{d\mu}=\frac{d\varphi}{d\nu}\frac{d\nu}{d\mu},\quad\mu\mathrm{-a.e.}.   \tag*{(3.3.16)}
$$

证 显然有  $\varphi \ll \mu$，故由定理3.3.13，对  $\forall A \in \mathcal{F}$，有

 
$$
\int_{A}\frac{d\varphi}{d\nu}\frac{d\nu}{d\mu}d\mu=\int_{A}\frac{d\varphi}{d\nu}d\nu=\varphi(A)=\int_{A}\frac{d\varphi}{d\mu}d\mu,
$$
 

于是由系3.1.9(2)知(3.3.16)式成立.

下一定理称为Vitali-Hahn-Saks定理. 我们将在3.4节和7.4节中用到这一定理.

定理3.3.15 设 $(\Omega,\mathcal{F})$为一可测空间， $(\mu_{n})$为其上的一列有限符号测度. 如果对每个 $A\in\mathcal{F}$，极限 $\mu(A)=\lim\mu_{n}(A)$存在且有限，则

(1) $\mu$为一符号测度;

(2)  $\sup_{n} \|\mu_n\| < \infty$，这里  $\|\mu_n\|$ 表示  $\mu_n$ 的全变差， $|\mu_n|$ 为  $\mu_n$ 的变差测度；

(3) 设  $\lambda$ 为一有限测度，使得对一切  $n \geq 1$，有  $\mu_n \ll \lambda$（注：这样的测度总存在，例如令  $\lambda = \sum_{n=1}^{\infty} \frac{1}{2^n \|\mu_n\|} |\mu_n|$）。则对任给  $\varepsilon > 0$，存在  $\eta > 0$，使得

 
$$
A\in\mathcal{F},\lambda(A)\leqslant\eta\Rightarrow\sup_{n}|\mu_{n}|(A)\leqslant\varepsilon.
$$
 

证 令Φ表示 $L^{1}(\Omega,\mathcal{F},\lambda)$中由F可测集的示性函数等价类所成的子集，则Φ是闭集。从而作为子空间，Φ为完备距离空间。设 $A\in\mathcal{F}$，令A表示A所相应的等价类，我们用F表示F中元素等价类全体，则 $(\mathcal{F},d)$为完备距离空间，其中

 
$$
d(\dot{A},\dot{B})=\lambda(A\triangle B).
$$
 

设 $\alpha>0,$ 令

 
$$
L_{j}=\{\dot{A}\in\mathcal{F}\mid\forall n\geqslant j,m\geqslant j,\left|\mu_{n}(A)-\mu_{m}(A)\right|\leqslant\alpha\},
$$
 

由于函数 $A \mapsto \mu_n(A)$在 $\mathcal{F}$上连续，故 $L_j$为闭集。显然 $\bigcup_j L_j = \mathcal{F}$（因 $\forall A \in \mathcal{F}, \mu_n(A)$收敛）。由Baire定理（见定理5.1.27），存在某 $j$，使 $L_j$有一内点 $\dot{A}$，即对某 $h > 0$，有

 
$$
B\in\mathcal{F},\lambda(B\triangle A)\leqslant h\Rightarrow|\mu_{n}(B)-\mu_{m}(B)|\leqslant\alpha,\forall n\geqslant j,\ \forall m\geqslant j.
$$
 

---

取 $0<\eta<h$，使得(见习题3.3.3)

 
$$
C\in\mathcal{F},\lambda(C)\leqslant\eta\Rightarrow|\mu_{i}|(C)\leqslant\alpha,\quad i=1,\cdots,j.
$$
 

对于 $n \geqslant j$，我们有

 
$$
\begin{align*}\left|\mu_{n}(C)\right|&\leqslant\left|\mu_{n}(A\cup C)-\mu_{n}(A)\right|+\left|\mu_{n}(A\backslash C)-\mu_{n}(A)\right|\\&\leqslant\left|\mu_{n}(A\cup C)-\mu_{j}(A\cup C)\right|+\left|\mu_{j}(A\cup C)-\mu_{j}(A)\right|\\&\quad+\left|\mu_{j}(A)-\mu_{n}(A)\right|+\left|\mu_{n}(A\backslash C)-\mu_{j}(A\backslash C)\right|\\&\quad+\left|\mu_{j}(A\backslash C)-\mu_{j}(A)\right|+\left|\mu_{j}(A)-\mu_{n}(A)\right|.\end{align*}
$$
 

于是 $\lambda(C) \leqslant \eta \Rightarrow \sup_n |\mu(C)| \leqslant 6\alpha$。从而由习题3.3.7知： $\lambda(C) \leqslant \eta \Rightarrow \sup_n |\mu_n|(C) \leqslant 12\alpha$。由此立刻推得(3)(令 $\alpha = \varepsilon/12$)。

下面我们证明(2). 我们将空间Ω分为有限多个λ测度>η的原子及有限多个λ测度≤η的集合. 由于 $|\mu_n|\ll\lambda$, 故λ的原子必为每个 $|\mu_n|$的原子. 于是在λ的原子集A上, 有 $|\mu_n|(A)=|\mu_n(A)|$, 从而 $\sup_n|\mu_n|(A)<\infty$. 由此并利用前段的结果推得(2).

最后， $\mu$在 $\mathcal{F}$上显然是有限可加的．现设 $E_k \in \mathcal{F}, E_k \downarrow \varnothing$，则 $\lambda(E_k) \to 0$，从而由(3)知 $\mu(E_k) \to 0$．由此推知 $\mu$是 $\sigma$可加的，故 $\mu$是有限符号测度．

系3.3.16 设 $(\Omega,\mathcal{F},\mu)$为一有限测度空间， $\xi_{n}\in L^{1}(\Omega,\mathcal{F},\mu),\quad n\geqslant1.$ 若 $\forall A\in\mathcal{F},\quad\int_{A}\xi_{n}d\mu$ 的极限存在且有穷，则存在唯一的 $\xi\in L^{1}(\Omega,\mathcal{F},\mu)$，使

 
$$
\lim_{n\to\infty}\int_{A}\xi_{n}d\mu=\int_{A}\xi d\mu,\quad A\in\mathcal{F}.
$$
 

##### 习题

3.3.1 设ν为一符号测度, f关于ν的积分存在(见注3.3.5(3)). 则对一切 $A \in \mathcal{F}$,  $fI_A$关于ν的积分存在, 且 $A \mapsto \nu(fI_A)$定义了 $\mathcal{F}$上的一符号测度(记为 $f.\nu$).

3.3.2 设  $\nu$ 及  $\mu$ 为两个符号测度， $f$ 关于  $\nu$ 的积分存在. 若  $\nu \ll \mu$ (相应地  $\nu \perp \mu$)，则  $f \cdot \nu \ll \mu$ (相应地， $f \cdot \nu \perp \mu$).

3.3.3 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $\nu$为 $\mathcal{F}$上的一有限符号测度.则下列二断言等价：

(1)  $\nu \ll \mu;$

(2)  $\forall \varepsilon > 0, \exists \delta > 0$, 使得  $A \in \mathcal{F}, \mu(A) < \delta \Rightarrow |\nu|(A) < \varepsilon$.

3.3.4 举例说明定理3.3.11中 $\mu$的 $\sigma$有限性假定不能去掉(提示: 令 $\Omega = [0,1]$,  $\mathcal{F} = \{A \subset [0,1] \mid A$或 $A^c$为至多可数集 $\}}$.

3.3.5 设μ及ν为两个σ有限测度，则为要ν～μ，必须且只需存在可测函数g：0 < g(ω) < ∞, ∀ω ∈ Ω, 使得ν = g.μ.

---

3.3.6 设 $\mu_{1}$， $\mu_{2}$为可测空间 $(\Omega,\mathcal{F})$上的有限符号测度，令

 
$$
\mu_{1}\vee\mu_{2}=\mu_{1}+\left(\mu_{2}-\mu_{1}\right)^{+},\mu_{1}\wedge\mu_{2}=\mu_{1}-\left(\mu_{1}-\mu_{2}\right)^{+},
$$
 

则 $\mu_1 \vee \mu_2$为满足 $\nu \geq \mu_1$且 $\nu \geq \mu_2$的最小符号测度 $\nu$;  $\mu_1 \wedge \mu_2$为满足 $\nu \leq \mu_1$且 $\nu \leq \mu_2$的最大符号测度 $\nu$.

3.3.7 设  $\mu$ 为  $(\Omega, \mathcal{F})$ 上符号测度，则  $\|\mu\|_{\text{var}} \leqslant 2 \sup_{A \in \mathcal{F}} |\mu(A)|$。若  $\mu(\Omega) = 0$，则  $\mu$ 为有限符号测度，且有  $\|\mu\|_{\text{var}} = 2 \sup_{A \in \mathcal{F}} |\mu(A)|$。

3.3.8 设 $B(\Omega, \mathcal{F})$表示 $\Omega$上有界 $\mathcal{F}$可测函数全体， $\mathcal{M}(\Omega, \mathcal{F})$表示 $(\Omega, \mathcal{F})$上有限符号测度全体。对 $f \in B(\Omega, \mathcal{F})$，令 $\|f\| = \sup_{\omega \in \Omega} |f(\omega)|$，

(1)  $B(\Omega, \mathcal{F})$ 按范数  $\|\cdot\|$ 为一 Banach 空间 (完备赋范线性空间).

(2) 设  $\mu \in \mathcal{M}(\Omega, \mathcal{F})$，令  $I_{\mu}(f) = \mu(f)$， $f \in B(\Omega, \mathcal{F})$，则  $\mu$ 为  $B(\Omega, \mathcal{F})$ 上的一有界线性泛函，且有  $\|I_{\mu}\| = \|\mu\|_{\mathrm{var}}$（提示：设  $\Omega = D \cup D^c$ 为  $\mu$ 的 Hahn 分解，令  $f = I_D - I_D^c$，考虑  $\mu(f)$）.

(3)  $\mathcal{M}(\Omega, \mathcal{F})$ 按范数  $\|\cdot\|_{\text{var}}$ 为一 Banach 空间.

3.3.9 设  $\mu$ 为  $(\Omega, \mathcal{F})$ 上的测度， $f_1$ 和  $f_2$ 关于  $\mu$ 的积分存在，则  $f_1 \cdot \mu \wedge f_2 \cdot \mu = (f_1 \wedge f_2) \cdot \mu$； $f_1 \cdot \mu \vee f_2 \cdot \mu = (f_1 \vee f_2) \cdot \mu$。

### 3.4 空间 $L^{p}$及其对偶

设 $(\Omega,\mathcal{F},\mu)$为一测度空间. 对任一p:0<p<\infty, 我们令

$$
L^{p}(\Omega,\mathcal{F},\mu)=\{f\in\mathcal{L}(\Omega,\mathcal{F})\mid\mu(|f|^{p})<\infty\}   \tag*{(3.4.1)}
$$

(简记为 $L^p$)，其中 $\mathcal{L}(\Omega,\mathcal{F})$表示 $\Omega$上 $\mathcal{F}$可测实值函数全体。设 $f,g\in\mathcal{L}(\Omega,\mathcal{F})$，如果 $f=g$， $\mu$-a.e.，称 $f$与 $g$是 $\mu$等价的。今后，我们将 $L^p$中a.e.相等的元素不加区别，即把 $L^p$视为按 $\mu$等价关系所作的商空间。令

$$
\|f\|_{p}=\mu(|f|^{p})^{\frac{1}{p}},   \tag*{(3.4.2)}
$$

我们将证明：对 $p \geqslant 1$， $(L^{p}, \|\cdot\|_{p})$为一Banach空间(见定理3.4.5).

首先, 我们建立空间  $L^{p}$ 的一些基本不等式. 为此, 我们需要如下两个分析不等式, 其证明可在任何一本数学分析书中找到: 设 a, b 为实数, r > 0, 1 < p, q < \infty, 且  $\frac{1}{p} + \frac{1}{q} = 1$, 则有

$$
|a+b|^{r}\leqslant\max(1,2^{r-1})(|a|^{r}+|b|^{r}),   \tag*{(3.4.3)}
$$

$$
|a b|\leqslant\frac{|a|^{p}}{p}+\frac{|b|^{q}}{q}.   \tag*{(3.4.4)}
$$

定理3.4.1 设 $f,g\in\mathcal{L}(\Omega,\mathcal{F}),r>0,1<p,q<\infty,$ 且 $\frac{1}{p}+\frac{1}{q}=1,s\geqslant1.$ 则有

$$
\mu(|f+g|^{r})\leqslant C_{r}\mu(|f|^{r}+|g|^{r}),   \tag*{(3.4.5)}
$$


---


$$
\mu(|f g|)\leqslant\|f\|_{p}\|g\|_{q},   \tag*{(3.4.6)}
$$

$$
\left\|f+g\right\|_{s}\leqslant\left\|f\right\|_{s}+\left\|g\right\|_{s},   \tag*{(3.4.7)}
$$

其中 $C_r = \max(1, 2^{r-1})$。我们分别称(3.4.5)、(3.4.6)及(3.4.7)式为 $C_r$不等式、Hölder不等式及Minkowski不等式。对 $p = q = 2$情形，(3.4.6)式亦称为Schwarz不等式。

证 (3.4.5)式可直接从(3.4.3)式推得. 现证(3.4.6)式. 不妨设 $\|f\|_{p}<\infty,\|g\|_{q}<\infty$, 令 $\varphi=f/\|f\|_{p},\psi=g/\|g\|_{q}$, 则由(3.4.4)式得

 
$$
\mu(|\varphi\psi|)\leqslant\frac{\mu(|\varphi|^{p})}{p}+\frac{\mu(|\psi|^{q})}{q}=\frac{1}{p}+\frac{1}{q}=1,
$$
 

此即3.4.6式.

最后证明(3.4.7)式. 不妨设 $f,g\in L^{s}$，由(3.4.5)式知 $f+g\in L^{s}$，且当s=1时(3.4.7)式成立. 现设s>1，我们有

 
$$
\begin{align*}\int\left|f+g\right|^{s}d\mu&=\int\left|f+g\right|\left|f+g\right|^{s-1}d\mu\\&\leqslant\int\left|f\right|\left|f+g\right|^{s-1}d\mu+\int\left|g\right|\left|f+g\right|^{s-1}d\mu.\end{align*}
$$
 

令 $s^{\prime}>1$使 $\frac{1}{s}+\frac{1}{s^{\prime}}=1$，对上一不等式右端应用(3.4.6)式得(注意 $s^{\prime}(s-1)=s$)

 
$$
\begin{align*}\int|f+g|^{s}d\mu&\leqslant\|f\|_{s}\Big(\int|f+g|^{s}d\mu\Big)^{1/s^{\prime}}\\&\quad+\|g\|_{s}\Big(\int|f+g|^{s}d\mu\Big)^{1/s^{\prime}},\end{align*}
$$
 

由此立得 $(3.4.7)$式.

定理3.4.2 设$(\Omega,\mathcal{F},\mu)$为一概率空间，$\varphi$为一连续凸函数（即$\forall\alpha:0\leqslant\alpha\leqslant1,\forall x,y\in\mathbb{R},\varphi(\alpha x+(1-\alpha)y)\leqslant\alpha\varphi(x)+(1-\alpha)\varphi(y)$），又设$f\in L^{1}(\Omega,\mathcal{F},\mu)$，则$\varphi(f)$关于$\mu$的积分存在，且有

$$
\varphi(\mu(f))\leqslant\mu(\varphi(f)).   \tag*{(3.4.8)}
$$

(3.4.8)式称为Jensen不等式.

证 令  $\varphi'$ 表示  $\varphi$ 的右导数，则  $\forall x, y \in \mathbb{R}$，有

 
$$
\varphi^{\prime}(x)(y-x)\leqslant\varphi(y)-\varphi(x).
$$
 

于是有

 
$$
\varphi^{\prime}(\mu(f))(f-\mu(f))\leqslant\varphi(f)-\varphi(\mu(f)),
$$
 

两边关于 $\mu$积分即得欲证不等式.

---

定义3.4.3 设 $r>0,\{f,f_{n},n\geq1\}\subset L^{r}$. 如果 $\mu(|f_{n}-f|^{r})\to0,n\to\infty$，则称 $(f_{n})$ r次平均收敛于 $f(\text{简称}(f_{n})L^{r}\text{收敛于}f)$，或称 $(f_{n})$ 在 $L^{r}$ 中强收敛于f，记为 $f_{n}\xrightarrow{L^{r}}f$.

显然， $L^{r}$ 收敛的极限是唯一确定的(在 $\mu$等价意义下)，此外， $L^{r}$ 收敛蕴含依测度收敛.事实上，设 $\varepsilon>0$，则

 
$$
\mu(|f_{n}-f|\geqslant\varepsilon)=\mu(|f_{n}-f|^{r}\geqslant\varepsilon^{r})\leqslant\frac{1}{\varepsilon^{r}}\mu(|f_{n}-f|^{r}).
$$
 

引理3.4.4 设 $r>0,f_{n}\in L^{r},n\geq1$，则为要 $(f_{n})L^{r}$收敛于某 $f\in L^{r}$，必须且只需 $(f_{n})$为 $L^{r}$收敛的基本列.

证 先证必要性. 设  $f_{n} \xrightarrow{L^{r}} f$, 则由(3.4.3)式得

 
$$
|f_{n}-f_{m}|^{r}\leqslant C_{r}(|f_{n}-f|^{r}+|f_{m}-f|^{r}),
$$
 

故有  $\lim_{n,m\to\infty}\mu(|f_n-f_m|^r)=0.$ 往证充分性. 设  $(f_n)$ 为  $L^r$ 收敛基本列, 则易知  $f_n$ 为依测度收敛的基本列, 故存在  $f\in\mathcal{L}$, 使  $f_n\xrightarrow{\mu}f$ (习题2.3.1). 于是由 Fatou 引理知

 
$$
\mu(|f_{n}-f|^{r})\leqslant\lim_{m\to\infty}\mu(|f_{n}-f_{m}|^{r}),
$$
 

从而有  $\lim_{n\to\infty}\mu(|f_n-f|^r)=0$，显然有  $f\in L^r$。

定理3.4.5 设 $p \geqslant 1$，则 $(L^{p}, \|\cdot\|_{p})$为一Banach空间.

证 首先，由定理3.1.6(6)知， $\|f\|_{p}=0\Leftrightarrow f=0$，a.e.，此外，对任一实数 $\alpha$，有  $\|\alpha f\|_{p}=|\alpha|\|f\|_{p}$，故由(3.4.7)式知， $\|\cdot\|_{p}$为 $L^{p}$上的一范数。再由引理3.4.5知， $(L^{p},\|\cdot\|_{p})$为一Banach空间。

定理3.4.6 设 $p \geqslant 1$,  $\{f, f_n, n \geqslant 1\} \subset L^p$, 则下列二条件等价:

(1)  $\|f_n - f\|_p \to 0$;

(2)  $f_n \xrightarrow{\mu} f, \|f_n\|_p \to \|f\|_p$.

此外，若 $f_{n} \xrightarrow{a.e.} f, \|f_{n}\|_{p} \to \|f\|_{p}$，则也有 $\|f_{n} - f\|_{p} \to 0$。

证  $(1)\Rightarrow(2)$ 显然. 由于

 
$$
|f_{n}-f|^{p}\leqslant2^{p-1}(|f_{n}|^{p}+|f|^{p}),
$$
 

故由定理3.2.7推知 $(2)\Rightarrow(1)$及另一结论.

下面我们研究空间 $L^{p}$的可分性,为此,先证明一个引理.

引理3.4.7 令 $S(\Omega,\mathcal{F})$表示 $\Omega$上的 $\mathcal{F}$可测简单函数全体，设 $p \geqslant 1$，则 $S(\Omega,\mathcal{F}) \cap L^p$在 $L^p$中稠密.

证 设  $f \in L^{p}$，由定理2.1.8知：存在  $f_{n} \in \mathcal{S}(\Omega, \mathcal{F}), |f_{n}| \leqslant |f|$，使得  $\lim_{n \to \infty} f_{n} = f$。于是  $f_{n} \in L^{p}$，且  $|f_{n} - f|^{p} \leqslant 2^{p} |f|^{p}$，故由控制收敛定理（定理3.2.5）知：当  $n \to \infty$，有  $\mu(|f_{n} - f|^{p}) \to 0$。

---

定义3.4.8 设 $(\Omega,\mathcal{F},\mu)$为一测度空间，称 $\mathcal{F}$为 $\mu$可分，如果存在一可分的 $\mathcal{F}$的子 $\sigma$代数 $\mathcal{F}_{0}$，使 $\forall A\in\mathcal{F}$，存在 $B\in\mathcal{F}_{0}$，满足 $\mu(A\triangle B)=0$。

定理3.4.9 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $\mu$为 $\sigma$有限测度.则下列断言等价：

(1)  $\mathcal{F}$ 为  $\mu$ 可分;

(2) 对一切  $p \geqslant 1$， $L^{p}$ 为可分 Banach 空间；

(3) 对某个  $p \geqslant 1$,  $L^{p}$ 为可分 Banach 空间.

证 (1)⇒(2). 设F为μ可分，令 $F_0$为Ω上的一可分σ代数，使得 $F_0 \subset F$，且 $\forall A \in F$，存在 $B \in F_0$，满足 $\mu(A \triangle B) = 0$。可以假定存在Ω的一个可数划分： $\Omega = \sum_n A_n$，使得 $A_n \in F_0$， $\mu(A_n) < \infty$， $n = 1, 2, \cdots$，由定义1.2.7知，存在一代数 $\mathcal{L} \subset F_0$，其元素个数至多可数，使得 $A_n \in \mathcal{L}$， $n \geq 1$， $\sigma(\mathcal{L}) = \mathcal{F}_0$。令

 
$$
\mathcal{H}=\{\sum_{i=1}^{n}a_{i}I_{B_{i}},B_{i}\in\mathcal{L},a_{i} 为有理数 ,1\leqslant i\leqslant n,n\geqslant1\}.
$$
 

由习题1.3.4知，对一切 $p \geq 1$， $\mathcal{H}$在 $\mathcal{S}(\Omega, \mathcal{F}) \cap L^p$中按 $L^p$范数稠密，从而由引理3.4.7知， $\mathcal{H}$在 $L^p$中稠密。但 $\mathcal{H}$的元素为可数多个，故 $L^p$为可分Banach空间。

剩下只需证(3)⇒(1).设对某个$p \geqslant 1$，$L^p$为可分Banach空间，则存在$L^p$的一可数稠子集$\mathcal{H}$。令$\mathcal{F}_0 = \sigma(\mathcal{H})$（即$\mathcal{F}_0$为使$\mathcal{H}$中元素为可测的最小$\sigma$代数）。则显然$\mathcal{F}_0$为可分$\sigma$代数，且$\mathcal{F}_0 \subset \mathcal{F}$。现设$A \in \mathcal{F}$，且$\mu(A) < \infty$，则$I_A \in L^p$。于是存在$f_n \in \mathcal{H}$，使$f_n \xrightarrow{L^p} I_A$，特别有$f_n' \xrightarrow{\mu} I_A$。令$B_n = \left[\frac{1}{2} < f_n < \frac{3}{2}\right]$，则$B_n \in \mathcal{F}_0$，且$B_n \triangleq A \subset \left[\left|f_0 - I_A\right| \geqslant \frac{1}{2}\right]$。故有$\mu(B_n \triangleq A) \to 0(n \to \infty)$。即$I_B_n \xrightarrow{\mu} I_A$。于是存在子列$(B_n')$，使$I_{B_n'} \xrightarrow{\text{ae.}} I_A$。令$B = \limsup_{n' \to \infty} B_n'$，则$B \in \mathcal{F}_0$，且$I_B = I_A$，a.e.，即$\mu(B \triangleq A) = 0$。由于$\mu$是$\sigma$有限的，于是我们证明了$\mathcal{F}$的$\mu$可分性。

注3.4.10 定理中关于  $\mu$ 为  $\sigma$ 有限的条件不能去掉. 例如: 设  $\Omega = \mathbb{R}, \mathcal{F} = \mathcal{B}(\mathbb{R})$, 对  $A \in \mathcal{F}$, 令  $\mu(A)$ 表示 A 中元素个数 (若 A 含无穷多元素, 令  $\mu(A) = \infty$), 则  $L^{1}(\Omega, \mathcal{F}, \mu)$ 不可分 (请读者证明这一事实).

作为定理3.4.9的一个推论, 我们有

定理3.4.11 设 $(\Omega,\mathcal{F},\mu)$为一测度空间, $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数, $\mu$在 $\mathcal{F}$和 $\mathcal{G}$上均为 $\sigma$有限.若 $\mathcal{F}$为 $\mu$可分,则 $\mathcal{G}$也为 $\mu$可分.

证  $L^{1}(\Omega,\mathcal{G},\mu)$ 可视为  $L^{1}(\Omega,\mathcal{F},\mu)$ 的子空间。依假定， $\mathcal{F}$ 为  $\mu$ 可分，故由定理 3.4.9 知， $L^{1}(\Omega,\mathcal{F},\mu)$ 为可分。因此，作为它的子空间， $L^{1}(\Omega,\mathcal{G},\mu)$ 亦可分，再由定理 3.4.9 即知， $\mathcal{G}$ 为  $\mu$ 可分。

下面我们定义空间 $L^{\infty}(\Omega,\mathcal{F},\mu)$.

定义3.4.12 设 $(\Omega,\mathcal{F},\mu)$为一测度空间，令 $f\in\mathcal{L}(\Omega,\mathcal{F})$，称f为本性有界的，如果存在非负实数c，使得 $\mu(||f|>c|)=0$，我们用 $L^{\infty}(\Omega,\mathcal{F},\mu)$表示本性有界可测函数

---

全体. 设  $f \in L^{\infty}(\Omega, \mathcal{F}, \mu)$，令

 
$$
\|f\|_{\infty}=\inf\{c\geqslant0\mid\mu([|f|>c])=0\}.
$$
 

下一定理的证明是不足道的.

定理3.4.13  $\|\cdot\|_{\infty}$ 是 $L^{\infty}(\Omega,\mathcal{F},\mu)$ 上的范数， $L^{\infty}(\Omega,\mathcal{F},\mu)$ 按范数 $\|\cdot\|_{\infty}$ 成为一Banach空间.

设X为一赋范线性空间.若f为X上一有界线性泛函,令

 
$$
\|f\|=\sup_{\|x\|\leqslant1}|f(x)|,
$$
 

称\|f\|为f的范数.熟知,X上的有界线性泛函全体按上述范数构成一Banach空间,我们称它为X的对偶空间,记为X*.下面将研究 $L^{p}(\Omega,\mathcal{F},\mu)$的对偶空间 $L^{p}(\Omega,\mathcal{F},\mu)^{*}$.

定理3.4.14 设 $1<p,q<\infty,\frac{1}{p}+\frac{1}{q}=1$，则 $L^{p}(\Omega,\mathcal{F},\mu)^{*}$与 $L^{q}(\Omega,\mathcal{F},\mu)$保范线性同构：设 $g\in L^{q}(\Omega,\mathcal{F},\mu)$。令

$$
T_{g}(f)=\mu(f g),\quad f\in L^{p}(\Omega,\mathcal{F},\mu),   \tag*{(3.4.9)}
$$

则 $T_g \in L^p(\Omega, \mathcal{F}, \mu)^*$， $g \mapsto T_g$为 $L^q(\Omega, \mathcal{F}, \mu)$到 $L^p(\Omega, \mathcal{F}, \mu)^*$上的一对一映射，且 $\|g\|_q = \|T_g\|$。

证 设  $g \in L^q(\Omega, \mathcal{F}, \mu)$，由Hölder不等式知，(3.4.9)式定义了  $L^p(\Omega, \mathcal{F}, \mu)$ 上的一有界线性泛函  $T_g$，且  $\|T_g\| \leqslant \|g\|_q$。往证  $\|T_g\| = \|g\|_q$。不妨设  $\|g\|_q > 0$，令

 
$$
f=|g|^{q-1}\mathrm{s g n}(g),
$$
 

其中 $\mathrm{sgn}(x)$为x的符号，即 $\mathrm{sgn}(x)=I_{(0,\infty)}(x)-I_{(-\infty,0)}(x)$。由于 $(q-1)p=q$，故有 $\|f\|_{p}^{p}=\|g\|_{q}^{q}$，从而

 
$$
\begin{align*}T_{g}(f)=\mu(|g|^{q})&=\|g\|_{q}^{q}=\|g\|_{q}\|g\|_{q}^{q-1}\\&=\|g\|_{q}\|f\|_{p}.\end{align*}
$$
 

这表明 $\|T_g\| \geq \|g\|_q$，故有 $\|T_g\| = \|g\|_q$。显然， $g \longmapsto T_g$为 $L^q(\Omega, \mathcal{F}, \mu)$到 $L^p(\Omega, \mathcal{F}, \mu)$中的线性单射。剩下要证明它是满射。

设 $T \in L^{p}(\Omega, \mathcal{F}, \mu)^*$，往证存在 $g \in L^{q}(\Omega, \mathcal{F}, \mu)$，使 $T_g = T$。为此，令 $\mathcal{G} = \{A \in \mathcal{F} \mid \mu(A) < \infty\}$，对每个 $A \in \mathcal{G}$，令

 
$$
T_{A}(f)=T(f I_{A}),f\in L^{p}(\Omega,\mathcal{F},\mu),
$$
 

则 $T_A \in L^p(\Omega, \mathcal{F}, \mu)^*$，且 $\|T_A\| \leqslant \|T\|$。令

 
$$
\nu_{A}(B)=T_{A}(I_{B})=T(I_{A\cap B}),~\mu_{A}(B)=\mu(A\cap B),\quad B\in\mathcal{F},
$$
 

---

则 $\nu_{A}$为 $(\Omega,\mathcal{F})$上一有限符号测度，且 $\nu_{A}\ll\mu_{A}$。令 $g_{A}=\frac{d\nu_{A}}{d\mu_{A}}$，则显然有 $g_{A}I_{A^{c}}=0$，

a.e.. 下面证 $g_{A}\in L^{q}(\Omega,\mathcal{F},\mu)$，且 $T_{g_{A}}=T_{A}$。为此，令 $E_{n}=[|g_{A}|\leq n]\cap A$，则 $E_{n}\uparrow A$。

记 $h_{n}=g_{A}I_{E_{n}}$，则 $h_{n}\in L^{q}(\Omega,\mathcal{F},\mu)$，且对一切 $f\in L^{p}(\Omega,\mathcal{F},\mu)$有

 
$$
\begin{align*}T_{h_{n}}(f)&=\mu(fh_{n})=\mu(fg_{A}I_{E_{n}})=\mu_{A}(g_{A}fI_{E_{n}})\\&=\nu_{A}(fI_{E_{n}})=T_{A}(fI_{E_{n}})=T_{A\cap E_{n}}(f)=T_{E_{n}}(f).\end{align*}
$$
 

这表明 $T_{h_{n}}=T_{E_{n}}$，于是有

 
$$
\|h_{n}\|_{q}=\|T_{h_{n}}\|=\|T_{E_{n}}\|\leqslant\|T\|.
$$
 

由于 $h_n \to g_A$，故由Fatou引理知 $\|g_A\|_q \leq \|T\|$，从而 $g_A \in L^q(\Omega, \mathcal{F}, \mu)$。于是有

 
$$
T_{g_{A}}(f)=\mu(g_{A}f)=\mu_{A}(g_{A}f)=\nu_{A}(f)=T_{A}(f).
$$
 

这表明 $T_{g_A} = T_A$.特别，我们有 $\|g_A\|_q = \|T_A\|$. 下面我们证明存在 $g \in L^q(\Omega, \mathcal{F}, \mu)$，使 $T_g = T$. 设 $A \subset B, A, B \in \mathcal{G}$，易见 $\|T_A\| \leqslant \|T_B\|$，且 $g_B I_A = g_A$，a.e.，于是可取 $A_n \in \mathcal{G}, A_n \uparrow$，使得

 
$$
\sup_{n}\left\|T_{A_{n}}\right\|=\sup\{\left\|T_{A}\right\|\mid A\in\mathcal{G}\}.
$$
 

令 $g = \lim_{n \to \infty} g_{A_n}$，a.e.，由于 $\|g_{A_n}\|_q \leq \|T\|$，故由Fatou引理知 $g \in L^q(\Omega, \mathcal{F}, \mu)$。现证 $T_g = T$。令 $A = \bigcup_n A_n$，则对任何 $f \in L^p(\Omega, \mathcal{F}, \mu)$，我们有

 
$$
\begin{aligned}T_{g}(f)&=\mu(fg)=\lim_{n\to\infty}\mu(fg_{A_{n}})=\lim_{n\to\infty}T_{A_{n}}(f)\\&=\lim_{n\to\infty}T(fI_{A_{n}})=T(fI_{A}).\end{aligned}
$$
 

因此，为证$T_g = T$，只需证明$T(fI_{Ac}) = 0, \forall f \in L^q(\Omega, \mathcal{F}, \mu)$。我们用反证法，假定存在某$f \in L^p(\Omega, \mathcal{F}, \mu)$，使得$T(fI_{Ac}) \neq 0$。令$D_n = [|f| > \frac{1}{n}] \cap A^c$，则$\mu(D_n) < \infty$，且由控制收敛定理知$fI_{D_n} \xrightarrow{L^p} fI_{Ac}$，故存在某$n_0$，使$T(fI_{D_n_0})$非$0$，即$T_{D_n_0}(f) \neq 0$。于是$\|T_{D_{n_0}}\| > 0$。令$C_n = A_n \cup D_{n_0}$，则

 
$$
\begin{aligned}\|T_{C_{n}}\|^{q}&=\|g_{C_{n}}\|^{q}_{q}=\|g_{A_{n}}+g_{D_{n_{0}}}\|^{q}_{q}\\&=\|g_{A_{n}}\|^{q}_{q}+\|g_{D_{n_{0}}}\|^{q}_{q}=\|T_{A^{n}}\|^{q}+\|T_{D_{n_{0}}}\|^{q}\end{aligned}
$$
 

(这里用到如下事实:  $A_n \cap D_{n_0} = \varnothing \Rightarrow g_{A_n} + g_{D_{n_0}} = g_{C_n}$, a.e.). 因此有  $\sup_n \|T_{C_n}\| > \sup_n \|T_{A_n}\|$，这与  $(A_n)$ 的选取矛盾.

上述定理表明：如果 $1<p,q<\infty,\frac{1}{p}+\frac{1}{q}=1$，可将 $L^{q}(\Omega,\mathcal{F},\mu)$视为 $L^{p}(\Omega,\mathcal{F},\mu)$的对偶。下一定理表明：如果 $\mu$为 $\sigma$有限测度，则 $L^{\infty}(\Omega,\mathcal{F},\mu)$可视为 $L^{1}(\Omega,\mathcal{F},\mu)$的对偶。

---

定理3.4.15 设 $(\Omega,\mathcal{F},\mu)$为一 $\sigma$有限测度空间，则 $L^{1}(\Omega,\mathcal{F},\mu)^{*}$与 $L^{\infty}(\Omega,\mathcal{F},\mu)$保范线性同构，其同构映射为：设 $g\in L^{\infty}(\Omega,\mathcal{F},\mu)$，令

 
$$
T_{g}(f)=\mu(f g),f\in L^{1}(\Omega,\mathcal{F},\mu),
$$
 

则 $T_g \in L^1(\Omega, \mathcal{F}, \mu)^*$， $g \longmapsto T_g$为一对一满射，且 $\|g\|_\infty = \|T_g\|$。特别有 $\|fg\|_1 \leq \|g\|_\infty \|f\|_1$。

证 设  $g \in L^{\infty}(\Omega, \mathcal{F}, \mu)$，易见  $T_{g} \in L^{1}(\Omega, \mathcal{F}, \mu)^{*}$，且  $\|T_{g}\| \leqslant \|g\|_{\infty}$。为证  $\|T_{g}\| = \|g\|_{\infty}$，不妨设  $\|g\|_{\infty} > 0$。则对  $\forall \varepsilon : 0 < \varepsilon < \|g\|_{\infty}$，我们有  $\mu(|g| > \|g\|_{\infty} - \varepsilon) > 0$。给定  $\varepsilon > 0$，取  $A \subset [|g| > \|g\|_{\infty} - \varepsilon]$，使  $0 < \mu(A) < \infty$。令  $f = I_{A}\mathrm{sgn}(g)$，则  $f \in L^{1}(\Omega, \mathcal{F}, \mu)$，且有

 
$$
\|f\|_{1}=\mu(|f|)=\mu(A),
$$
 

 
$$
T_{g}(f)=\mu(f g)=\mu(I_{A}|g|)\geqslant(\|g\|_{\infty}-\varepsilon)\mu(A).
$$
 

这表明 $\|T_g\| \geqslant \|g\|_\infty - \varepsilon$。由于 $\varepsilon > 0$是任意的，故有 $\|T_g\| \geqslant \|g\|_\infty$，从而 $\|T_g\| = \|g\|_\infty$。

现设 $T \in L^{1}(\Omega, \mathcal{F}, \mu)^*$。往证存在 $g \in L^\infty(\Omega, \mathcal{F}, \mu)$，使 $T_g = T$。令 $\mathcal{G} = \{A \in \mathcal{F} | \mu(A) < \infty\}$，由于假定 $\mu$是 $\sigma$有限的，故存在 $A_n \in \mathcal{G}$，使 $A_n \uparrow \Omega$。令

 
$$
\nu_{n}(B)=T(I_{A_{n}\cap B}),\mu_{n}=\mu(A_{n}\cap B),B\in\mathcal{F},
$$
 

并令 $g_{n}=\frac{d\nu_{n}}{d\mu_{n}}$，则显然有 $g_{n}\in L^{1}(\Omega,\mathcal{F},\mu)$，且对 $f\in L^{1}(\Omega,\mathcal{F},\mu)$有

 
$$
T_{A_{n}}(f)=T(f I_{A_{n}})=\nu_{n}(f)=\mu_{n}(f g_{n})=\mu(f g_{n})=T_{g_{n}}(f).
$$
 

由于 $\|g_n\|_\infty = \|T_{A_n}\| \leqslant \|T|, g_n \uparrow g, a.e.,$ 故 $g \in L^\infty(\Omega, \mathcal{F}, \mu)$，且有

 
$$
T_{g}(f)=\mu(f g)=\lim_{n\to\infty}\mu(f g_{n})=\lim_{n\to\infty}T(f I_{A_{n}})=T(f),
$$
 

即有 $T_{g}=T.$

定理3.4.15中关于 $\mu$的 $\sigma$有限性的假定不能去掉。例如令 $\Omega = \mathbb{R}$， $\mathcal{F} = \{A \subset \mathbb{R} \mid A \text{ 或 } A^c \text{ 为至多可数集}\}$， $\mu$为 $(\Omega, \mathcal{F})$上的计数测度，则 $f \in L^1(\Omega, \mathcal{F}, \mu)$当且仅当 $f$在一可数集外为零，且 $\|f\|_1 = \sum_x |f(x)| < \infty$。在 $L^1(\Omega, \mathcal{F}, \mu)$上定义一线性泛函 $F$: $F(f) = \sum_x > 0 f(x)$，则 $F$连续，且 $g = I_{(0,\infty)}$是唯一的函数 $g$使得 $F(f) = \int f g\,d\mu$，但 $g$不是 $\mathcal{F}$可测函数。

定义3.4.16 设  $1 \leqslant p, q \leqslant \infty, \frac{1}{p} + \frac{1}{q} = 1, \{f, f_{n}, n \geqslant 1\} \subset L^{p}$. 如果  $\forall g \in L^{q}, \mu(f_{n}g) \to \mu(fg)$，则称  $(f_{n})$ 在  $L^{p}$ 中弱收敛于 f.

定理3.4.17 设 $1 < p, q < \infty, \frac{1}{p} + \frac{1}{q} = 1, \{f, f_n, n \geq 1\} \subset L^p.$ 如果 $f_n \xrightarrow{\text{ae.}}$  $f$ 或 $f_n \xrightarrow{\mu} f$ 且 $\{\|f_n\|_p\}$ 有界，则 $(f_n)$ 在 $L^p$ 中弱收敛于 $f$.

---

证 只需证明a.e.收敛情形. 设$f_n \xrightarrow{\text{a.e.}}$ $f$ 且$\sup_n \|f_n\|_p = C$. 由Fatou引理, $\|f\|_p \leqslant C$. 设$g \in L^q$. 令$A_n = [1/n \leqslant |g|^q \leqslant n]$. 给定$\varepsilon > 0$, 存在$\delta > 0$, 使得当$\mu(A) < \delta$时有$\|g I_A\|_q < \varepsilon$. 由Egorov定理(定理2.3.5(2)), 对每个$n$存在$B_n \in \mathcal{F}, B_n \subset A_n$, 使得$\mu(A_n \setminus B_n) < \delta$, 且$(f_k)$在$B_n$上一致收敛于$f$. 另一方面, 存在$n_0$使得对一切$n \geqslant n_0$有$\|g I_{A_n^c}\|_q < \varepsilon$. 于是当$n \geqslant n_0$有

 
$$
\begin{align*}\left|\mu((f_{k}-f)g)\right|&\leqslant\left|\mu((f_{k}-f)gI_{A_{n}})\right|+\left|\mu((f_{k}-f)gI_{A_{n}^{c}})\right|\\&\leqslant\mu(|f_{k}-f||g|I_{B_{n}})+\mu(|f_{k}-f||g|I_{A_{n}\setminus B_{n}})+\|f_{k}-f\|_{p}\|gI_{A_{n}^{c}}\|_{q}\\&\leqslant\mu(|f_{k}-f||g|I_{B_{n}})+\|f_{k}-f\|_{p}(\|gI_{A_{n}\setminus B_{n}}\|_{q}+\|gI_{A_{n}^{c}}\|_{q})\\&<\mu(|f_{k}-f||g|I_{B_{n}})+4C\varepsilon.\end{align*}
$$
 

由此推知 $\mu(f_{k}g)\to\mu(fg)$.从而 $(f_{n})$在 $L^{p}$中弱收敛于f.

需要指出: 该定理对p = 1不成立. 例如设 $\Omega = [0,1]$,  $\mathcal{F} = \mathcal{B}([0,1])$,  $\mu$为 $[0,1]$上的Lebesgue测度. 令 $f_n = nI_{[0,1/n]}$, 则 $\|f_n\|_1 = 1$,  $f_n \to 0$, a.e., 但 $(f_n)$不弱收敛到0.

定理3.4.18 设  $\Omega = \mathbb{N} := \{1, 2, \cdots\}$， $\mathcal{F}$ 为  $\mathbb{N}$ 的子集全体， $\mu$ 为  $\mathbb{N}$ 上计数测度，则在  $L^1$ 中强收敛与弱收敛等价。

证 设 $(f_{n})$在 $L^{1}$中弱收敛于f. 令

 
$$
\mu_{n}(A)=\sum_{i\in A}f_{n}(i),\quad\mu(A)=\sum_{i\in A}f(i),
$$
 

则 $\mu_{n}(A)\to\mu(A),\forall A\in\mathcal{F}$.由Vitali-Hahn-Saks定理(定理3.3.15)知， $\sup_{n}\sum_{i}|f_{n}(i)|<\infty$，且对任给 $\varepsilon>0$，存在 $\eta>0$，使得

 
$$
A\in\mathcal{F},\sum_{i\in A}\frac{1}{2^{i}}\leqslant\eta\Rightarrow\sup_{n}\sum_{i\in A}\left|f_{n}(i)\right|\leqslant\varepsilon.
$$
 

取m充分大，使得

 
$$
\sum_{i=m+1}^{\infty}\frac{1}{2^{i}}<\eta,\sum_{i=m+1}^{\infty}\left|f(i)\right|<\varepsilon,
$$
 

则有

 
$$
\begin{align*}\sum_{i=1}^{\infty}\left|f_{n}(i)-f(i)\right|&\leqslant\sum_{i=1}^{m}\left|f_{n}(i)-f(i)\right|+\sum_{i=m+1}^{\infty}\left(\left|f_{n}(i)\right|+\left|f(i)\right|\right)\\&\leqslant\sum_{i=1}^{m}\left|f_{n}(i)-f(i)\right|+2\varepsilon.\end{align*}
$$
 

由于 $f_{n}$逐点收敛于f，故由上式推知 $(f_{n})$在 $L^{1}$中强收敛于f.

---

注3.4.19 在定理的框架下，对p>1情形， $L^{p}$中的强收敛与弱收敛不等价．事实上，令 $f_{n}(i)=0,i\neq n;f_{n}(n)=1$，则 $\|f_{n}\|_{p}=1$，但 $(f_{n})$弱收敛于0.

##### 习题

3.4.1 证明简单可测函数全体在  $L^{\infty}(\Omega, \mathcal{F}, \mu)$ 中稠密. 提示: 对任给  $\varepsilon > 0$, 将  $[-\|f\|_{\infty}, \|f\|_{\infty}]$ 分成有限多个其长度小于  $\varepsilon$ 的区间:  $[a_{0}, a_{1}], \cdots, (a_{n-1}, a_{n}]$. 令  $f_{\varepsilon} = \sum_{i=1}^{n} a_{i} I_{A_{i}}$, 其中

 
$$
A_{1}=f^{-1}([a_{0},a_{1}]),A_{k}=f^{-1}((a_{k-1},a_{k}]),k\geqslant2.
$$
 

3.4.2 设  $[a, b]$ 为一闭区间， $\mu$ 为  $[a, b]$ 上的 Lebesgue 测度。则对任何  $p: 1 \leqslant p < \infty$， $[a, b]$ 上的阶梯函数全体在  $L^{p}([a, b], \mu)$ 中稠密。由此进一步证明  $[a, b]$ 上的连续函数全体在  $L^{p}([a, b], \mu)$ 中稠密。此外证明  $L^{\infty}([a, b], \mu)$ 不是可分的 Banach 空间。

3.4.3 设 $(\Omega,\mathcal{F},P)$为概率空间， $1\leqslant p_{1}<p_{2}<\infty$，则 $\|f\|_{p_{1}}\leqslant\|f\|_{p_{2}}$。此外，有 $\|f\|_{p}\rightarrow\|f\|_{\infty}(p\rightarrow\infty)$（提示：利用Hölder不等式及Jensen不等式）。

3.4.4 (Hölder不等式的推广) (1) 设  $1 < p, q, r < \infty, \frac{1}{n} + \frac{1}{a} = \frac{1}{r}$，则有  $\|fg\|_{r} \leqslant \|f\|_{p} \|g\|_{q}$.

(2) 设  $1 < p_{1}, p_{2}, \cdots, p_{m} < \infty, m \geqslant 2,$ 且  $\frac{1}{p_{1}} + \frac{1}{p_{2}} + \cdots + \frac{1}{p_{m}} = 1,$ 则有

 
$$
\left\|f_{1}\cdots f_{m}\right\|_{1}\leqslant\left\|f_{1}\right\|_{p_{1}}\cdots\left\|f_{m}\right\|_{p_{m}}.
$$
 

3.4.5 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $f\in L^{1}\cap L^{\infty}$.试证： $\forall p\geqslant1,f\in L^{p}$，且 $\lim_{p\to\infty}\|f\|_{p}=\|f\|_{\infty}$.

3.4.6 设λ为₣上的Lebesgue测度， $1 \leqslant p < \infty$， $f \in L^p(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$。对每个 $x \in \mathbb{R}$，令 $f_x(t) = f(t - x)$。试证： $\forall x_0 \in \mathbb{R}$，有 $\lim_{x \to x_0} \|f_x - f_{x_0}\|_p = 0$。

3.4.7 设 $(\Omega,\mathcal{F},\mu)$为一测度空间，g为一实值 $\mu$可积函数，在 $L^{\infty}(\Omega,\mathcal{F},\mu)$上定义 $T_{g}$如下：

 
$$
T_{g}(f)=\int_{\Omega}f g d\mu,\;f\in L^{\infty}(\Omega,\mathcal{F},\mu).
$$
 

试证 $\|g\|_{1}=\sup\{|T_{g}(f)|\mid\|f\|_\infty\leqslant1\}$.

### 3.5 空间 $L^{\infty}(\Omega,\mathcal{F})$和 $L^{\infty}(\Omega,\mathcal{F},m)$的对偶

设 $(\Omega,\mathcal{F})$为一可测空间,我们用 $L^{\infty}(\Omega,\mathcal{F})$表示 $(\Omega,\mathcal{F})$上的有界可测函数全体.对任 $f\in L^{\infty}(\Omega,\mathcal{F})$,令

 
$$
\|f\|=\sup_{\omega\in\Omega}|f(\omega)|,
$$
 

则 $L^{\infty}(\Omega,\mathcal{F})$按此范数为一Banach空间.

设 $\mu$为 $\mathcal{F}$上的一有限可加集函数. 令

$$
\|\mu\|_{\mathrm{var}}=\sup\Big\{\sum_{i=1}^{n}\left|\mu(A_{i})\right|\Big|\{A_{i}\}\subset\mathcal{F} 为 \Omega 的可数划分 \Big\},   \tag*{(3.5.1)}
$$


---

称 $\|\mu\|_{\mathrm{var}}$为 $\mu$的全变差．我们用 $ba(\Omega,\mathcal{F})$表示全变差有穷的有限可加集函数全体．此外，设 $\mu\in ba(\Omega,\mathcal{F}),f=\sum_{i=1}^{n}a_{i}I_{A_{i}}$为一简单可测函数，其中 $a_{i}\in\mathbb{R},A_{i}\in\mathcal{F}$．令

$$
\int_{\Omega}f d\mu=\sum_{i=1}^{n}a_{i}\mu(A_{i}),   \tag*{(3.5.2)}
$$

易证 $\int_{\Omega}f d\mu$不依赖于f的具体表达，且有

$$
\left|\int_{\Omega}f d\mu\right|\leqslant\left\|f\right\|\left\|\mu\right\|_{\mathrm{v a r}}.   \tag*{(3.5.3)}
$$

由于简单可测函数全体在 $L^\infty(\Omega,\mathcal{F})$中按范数稠密，(3.5.3)式允许我们将上述定义推广成为 $L^\infty(\Omega,\mathcal{F})$上一连续线性泛函，且(3.5.3)式成立。我们称 $\int_\Omega f\,d\mu$为 $f$关于 $\mu$的积分，通常，我们用 $\mu(f)$简记 $\int_\Omega f\,d\mu$。

下一定理表明 $ba(\Omega,\mathcal{F})$可以视为 $L^{\infty}(\Omega,\mathcal{F})$的对偶空间.

定理3.5.1 设 $\mu \in ba(\Omega, \mathcal{F})$，令

 
$$
T_{\mu}(f)=\mu(f),\;f\in L^{\infty}(\Omega,\mathcal{F}).
$$
 

则 $T_{\mu}$为从 $ba(\Omega,\mathcal{F})$到 $L^{\infty}(\Omega,\mathcal{F})^{*}$上的保范线性同构映射.

证 由(3.5.3)式知,  $T_{\mu} \in L^{\infty}(\Omega, \mathcal{F})^{*}$, 且有  $\|T_{\mu}\| \leqslant \|\mu\|_{\mathrm{var}}$. 反之, 设  $l \in L^{\infty}(\Omega, \mathcal{F})^{*}$.

如下定义 $\mu$:

 
$$
\mu(A)=l(I_{A}),\ A\in\mathcal{F},
$$
 

则μ为ℐ上的一有限可加集函数, 显然有‖μ‖var ≤ ‖l‖, 于是μ ∈ ba(Ω, ℐ), 且有Tμ = l.

因此最终有‖Tμ‖ = ‖μ‖var.

设 $(\Omega,\mathcal{F},m)$为一测度空间， $\mu\in ba(\Omega,\mathcal{F})$。如果 $m(A)=0\Rightarrow\mu(A)=0,A\in\mathcal{F}$，称 $\mu$关于m绝对连续，记为 $\mu\ll m$。令

 
$$
b a(\Omega,\mathcal{F},m)=\{\mu\in b a(\Omega,\mathcal{F})\mid\mu\ll m\}.
$$
 

设$\mu \in ba(\Omega, \mathcal{F}, m), f \in L^\infty(\Omega, \mathcal{F}, m)$，显然我们可以任选$L^\infty(\Omega, \mathcal{F})$ 中一元素$\tilde{f}$作为$f$的代表，定义$\mu(\tilde{f})$为$f$关于$\mu$的积分，仍记为$\int_\Omega f\,d\mu$，简记为$\mu(f)$。这时有

$$
\left|\int_{\Omega}f\dot{d\mu}\right|\leqslant\|f\|_{\infty}\|\mu\|_{\mathrm{var}}.   \tag*{(3.5.4)}
$$

下一定理表明 $ba(\Omega,\mathcal{F},m)$可以视为 $L^{\infty}(\Omega,\mathcal{F},m)$的对偶空间，其证明与定理3.5.1类似，留给读者完成.

定理3.5.2 设 $\mu \in ba(\Omega, \mathcal{F}, m)$，令

 
$$
T_{\mu}(f)=\mu(f),~f\in L^{\infty}(\Omega,\mathcal{F},m).
$$
 

则 $T_{\mu}$为从 $ba(\Omega,\mathcal{F},m)$到 $L^{\infty}(\Omega,\mathcal{F},m)^{*}$上的保范线性同构映射.

---

## 3.6 Daniell积分

积分的一个基本性质是线性性, 因此积分可视为  $L^{1}(\Omega, \mathcal{F}, \mu)$ 上的线性泛函. 这一思想可以用来给出定义积分的另一途径——Daniell积分.

定义3.6.1 设 $\Omega$为一抽象集合, $\mathcal{H}$为 $\Omega$上的一族实值函数组成的线性空间.如果

$$
f\in\mathcal{H}\Rightarrow|f|\in\mathcal{H},f\wedge1\in\mathcal{H},   \tag*{(3.6.1)}
$$

则称H为一向量格.

注3.6.2 在上述定义中, 条件  $f \in \mathcal{H} \Rightarrow |f| \in \mathcal{H}$ 等价于下列条件之一:

$$
f,g\in\mathcal{H}\Rightarrow f\wedge g\in\mathcal{H};   \tag*{(3.6.2)}
$$

$$
f,g\in\mathcal{H}\Rightarrow f\vee g\in\mathcal{H}.   \tag*{(3.6.3)}
$$

事实上， $|f|=f\vee0+(-f)\vee0$，故 $(3.6.3)\Rightarrow(3.6.1)$。又由于

 
$$
f\wedge g=\frac{g+f-\left|g-f\right|}{2},
$$
 

故 $(3.6.1)\Rightarrow(3.6.2)$. 由于 $f\vee g=f+g-f\wedge g$, 故 $(3.6.2)\Rightarrow(3.6.3)$.

定义3.6.3 设H为Ω上的一向量格，I为H上的正线性泛函：即 $f,g\in\mathcal{H},\alpha,\beta\in\mathbb{R}\Rightarrow I(\alpha f+\beta g)=\alpha I(f)+\beta I(g)$;  $f\in\mathcal{H},f\geq0\Rightarrow I(f)\geq0$。如果I满足如下条件：

$$
f_{n}\in\mathcal{H},f_{n}\downarrow0\Rightarrow I(f_{n})\rightarrow0,   \tag*{(3.6.4)}
$$

或者等价地

$$
f_{n}\in\mathcal{H},f_{n}\uparrow f\in\mathcal{H}\Rightarrow I(f)=\lim_{n\rightarrow\infty}I(f_{n}),   \tag*{(3.6.5)}
$$

则称I为H上的Daniell积分.

例子3.6.4 设A为Ω上的一代数, $\mu$为A上的一测度,令

 
$$
\mathcal{H}=\Big\{\sum_{i=1}^{n}a_{i}I_{A_{i}}\left|a_{i}\in\mathbb{R},A_{i}\in\mathcal{A},\mu(A_{i})<\infty,1\leqslant i\leqslant n,n\geqslant1\right\},
$$
 

则H为一向量格. 设 $f=\sum_{i=1}^{n}a_{i}I_{A_{i}}\in\mathcal{H}$，令 $I(f)=\sum_{i}a_{i}\mu(A_{i})$，则I为H上的Daniell积分.

例子3.6.5 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $\mathcal{H}=L^{1}(\Omega,\mathcal{F},\mu)$， $I(f)=\mu(f)$， $f\in\mathcal{H}$。则 $\mathcal{H}$为向量格， $I$为 $\mathcal{H}$上的Daniell积分。

下面我们将证明：Daniell积分可以延拓成为通常的可测函数关于测度的积分。为此我们先引进若干记号。

---

记号3.6.6 设H为Ω上的一向量格，令

 
$$
\mathcal{H}_{+}=\{f\in\mathcal{H}\mid f\geqslant0\},
$$
 

 $\mathcal{H}_+^* = \{f \mid \exists f_n \in \mathcal{H}_+, \text{使} f_n \uparrow f\}$,

 
$$
\mathcal{C}=\{C\subset\Omega\vert I_{C}\in\mathcal{H}_{+}^{*}\}.
$$
 

引理3.6.7 我们有

 
$$
f,g\in\mathcal{H}_{+}^{*},a,b\geqslant0\Rightarrow af+bg\in\mathcal{H}_{+}^{*},f\vee g,f\wedge g\in\mathcal{H}_{+}^{*};
$$
 

(2)  $f_n \in \mathcal{H}_+, f_n \uparrow f \Rightarrow f \in \mathcal{H}_+$;

(3) C对可列并运算封闭, 对有限交运算封闭;

(4)  $f \in \mathcal{H}_+ \Rightarrow \forall \alpha \in \mathbb{R}, [f > \alpha] \in \mathcal{C}$;

(5)  $f \in \mathcal{H}_+^* \Rightarrow \forall \alpha \geq 0, [f > \alpha] \in \mathcal{C}$;

(6)  $\sigma(\mathcal{C}) = \sigma(f \mid f \in \mathcal{H}).$

证 (1)及(2)显然. (3)由(1)及(2)推得. 往证(4). 设  $f \in \mathcal{H}_{+}, \alpha \in \mathbb{R}$, 则  $(f - \alpha)^{+} = f - f \wedge \alpha \in \mathcal{H}_{+}$. 但

 
$$
[n(f-\alpha)^{+}]\wedge1\uparrow I_{[f>\alpha]},\quad n\to\infty,
$$
 

故 $I_{[f>\alpha]}\in\mathcal{H}_{+}^{*}$，即 $[f>\alpha]\in\mathcal{C}$.

现证(5). 设  $f \in \mathcal{H}_{+}^{*}$，令  $f_{n} \in \mathcal{H}_{+}, f_{n} \uparrow f$，则由(4)知

 
$$
[f>\alpha]=\bigcup_{n}[f_{n}>\alpha]\in\mathcal{C}.
$$
 

最后，(6)容易由(4)看出.

定理3.6.8 (Daniell-Stone定理) 设H为Ω上的一向量格，I为H上的一Daniell积分，则存在 $\mathcal{F} \hat{=}\sigma(f | f \in \mathcal{H})$上的一测度 $\mu$使得 $\mathcal{H} \subset L^1(\Omega, \mathcal{F}, \mu)$，且对一切 $f \in \mathcal{H}$有 $I(f) = \mu(f)$。若进一步 $1 \in \mathcal{H}_+$，这样的测度 $\mu$是唯一确定的，且为 $\sigma$有限的。

证 我们将证明分为三个步骤.

 $1^\circ$ 对  $f \in \mathcal{H}_+$，令

 
$$
I^{*}(f)=\sup\{I(g)\mid g\leqslant f,g\in\mathcal{H}_{+}\},
$$
 

则易知有如下事实：

 
$$
f_{n}\in\mathcal{H}_{+},f_{n}\uparrow f\Rightarrow I^{*}(f)=\lim_{n\rightarrow\infty}I(f_{n});
$$
 

 
$$
f,g\in\mathcal{H}_{+}^{*},a,b\geqslant0\Rightarrow I^{*}(af+bg)=aI^{*}(f)+bI^{*}(g);
$$
 

 
$$
f_{n}\in\mathcal{H}_{+}^{*},f_{n}\uparrow f\Rightarrow I^{*}(f)=\lim_{n\rightarrow\infty}I^{*}(f_{n});
$$
 

 
$$
f,g\in\mathcal{H}_{+}^{*},f\leqslant g\Rightarrow I^{*}(f)\leqslant I^{*}(g).
$$
 

---

此外，对 $f\in\mathcal{H}_{+}$，有 $I^{*}(f)=I(f)$。现令

$$
\begin{aligned}\mu^{*}(C)&=I^{*}(I_{C}),C\in\mathcal{C},\\\mu^{*}(A)&=\inf\{\mu^{*}(C)\mid C\supset A,C\in\mathcal{C}\},A\subset\Omega\end{aligned}   \tag*{(3.6.6)}
$$

(约定 $\inf\varnothing=+\infty$). 往证 $\mu^{*}$为 $\Omega$上的外测度.

首先， $\mu^*(\varnothing)=0.$ 此外，设 $C_n\in\mathcal{C},n\geqslant1$，则 $\bigcup_n C_n\in\mathcal{C}$，故有

 
$$
\begin{align*}\mu^{*}(\bigcup_{n}C_{n})&=I^{*}(I_{\bigcup_{n}C_{n}})\leqslant I^{*}(\sum_{n=1}^{\infty}I_{C_{n}})\\&=\sum_{n=1}^{\infty}I^{*}(I_{C_{n}})=\sum_{n=1}^{\infty}\mu^{*}(C_{n}).\end{align*}
$$
 

现设 $A_{n}\subset\Omega,n\geq1,A=\bigcup_{n}A_{n}$.对给定 $\varepsilon>0$，存在 $C_{n}\in\mathcal{C},C_{n}\supset A_{n}$，使 $\mu^{*}(C_{n})\leq\mu^{*}(A_{n})+\frac{\varepsilon}{2^{n}}$.令 $C=\bigcup_{n}C_{n}$，则 $C\in\mathcal{C},C\supset A$，且有

 
$$
\mu^{*}(A)\leqslant\mu^{*}(C)\leqslant\sum_{n}\mu^{*}(C_{n})\leqslant\sum_{n}\mu^{*}(A_{n})+\varepsilon.
$$
 

由于 $\varepsilon>0$是任意的，故有 $\mu^{*}(A)\leqslant\sum_{n}\mu^{*}(A_{n})$，这表明 $\mu^{*}$为外测度.

2° 令  $M^*$ 为  $\mu^*$ 可测集全体，往证  $C \subset M^*$ (从而有  $\sigma(C) \subset M^*$)。由于 C 对可列并运算封闭，由 (3.6.6) 式易知，若将  $\mu^*$ 在 C 上的限制记为  $\mu'$，则  $\mu^*$ 为  $\mu'$ 引出的外测度。于是设  $A \in C$，由引理 1.4.5 知，为证  $A \in M^*$，只需证  $\forall C \in C, \mu^*(C) < \infty$，有

$$
\mu^{*}(C)\geqslant\mu^{*}(A\cap C)+\mu^{*}(A^{c}\cap C).   \tag*{(3.6.7)}
$$

令 $g_n \in \mathcal{H}_+$，使 $g_n \uparrow I_{A \cap C}$，令 $h_n \in \mathcal{H}_+$，使 $h_n \uparrow I_C$，则对固定 $n$，当 $m \to \infty$时有

 
$$
(h_{m}-g_{n})^{+}\uparrow I_{C}-g_{n}\in\mathcal{H}_{+}^{*}.
$$
 

令 $f_{n}=I_{C}-g_{n}$，则 $f_{n}\downarrow I_{C}-I_{A\cap C}=I_{A^{c}\cap C}$。设 $0<\varepsilon<1$，令 $G_{n}=[f_{n}>1-\varepsilon]$，则由引理3.6.7(5)知 $G_{n}\in\mathcal{C}$，且有

 
$$
G_{n}\supset A^{c}\cap C,\;f_{n}\geqslant(1-\varepsilon)I_{G_{n}},
$$
 

于是有

 
$$
\begin{align*}\mu^{*}(A^{c}\cap C)&\leqslant\mu^{*}(G_{n})\leqslant\frac{1}{1-\varepsilon}I^{*}(f_{n})\\&=\frac{1}{1-\varepsilon}(\mu^{*}(C)-I(g_{n})).\end{align*}
$$
 

---

注意到 $I(g_{n})\uparrow I^{*}(I_{A\cap C})=\mu^{*}(A\cap C)$，我们有

 
$$
\begin{align*}\mu^{*}(A^{c}\cap C)&\leqslant\lim_{n\to\infty}\mu^{*}(G_{n})\\&\cdot\leqslant\frac{1}{1-\varepsilon}[\mu^{*}(C)-\mu^{*}(A\cap C)].\end{align*}
$$
 

令 $\varepsilon\downarrow0$, 得

 
$$
\mu^{*}(A^{c}\cap C)\leqslant\mu^{*}(C)-\mu^{*}(A\cap C),
$$
 

故3.6.7式得证.

3° 令  $\mu$ 为  $\mu^*$ 到  $\sigma(\mathcal{C})$ 上的限制，则  $\mu$ 为测度，往证定理的结论成立。设  $f \in \mathcal{H}_+$，令

 
$$
f_{n}=\sum_{k=1}^{\infty}\frac{k}{2^{n}}(I_{[f>\frac{k}{2^{n}}]}-I_{[f>\frac{k+1}{2^{n}}]})=\frac{1}{2^{n}}\sum_{k=1}^{\infty}I_{[f>\frac{k}{2^{n}}]},
$$
 

则 $f_{n}\in\mathcal{H}_{+}^{*}$，且 $f_{n}\uparrow f$。我们有

 
$$
\begin{align*}I(f)&=\lim_{n\to\infty}I^{*}(f_{n})=\lim_{n\to\infty}\frac{1}{2^{n}}\sum_{k=1}^{\infty}\mu([f>\frac{k}{2^{n}}])\\&=\lim_{n\to\infty}\mu(f_{n})=\mu(f).\end{align*}
$$
 

这表明 $\mathcal{H}_+\subset L^1(\Omega,\mathcal{F},\mu)$，且对 $f\in\mathcal{H}_+$，有 $I(f)=\mu(f)$。再由线性性推知对一般 $f\in\mathcal{H}$，有 $I(f)=\mu(f)$。

最后，若 $1\in\mathcal{H}_{+}^{*}$，则存在 $f_{n}\in\mathcal{H}_{+}$使 $f_{n}\uparrow1$，于是 $[f_{n}>\frac{1}{2}]\uparrow\Omega$，但 $\mu([f_{n}>\frac{1}{2}])\leq\frac{1}{2}\mu(f_{n})=\frac{1}{2}I(f_{n})<\infty$，故 $\mu$为 $\sigma$有限测度。此外，设 $\nu$为一测度，使得

 
$$
\mu(f)=I(f)=\nu(f),\ f\in\mathcal{H}_{+},
$$
 

则由积分单调收敛定理推知： $\mu(f) = \nu(f), \forall f \in \mathcal{H}_+^\ast$，特别， $\nu$与 $\mu$在 $\mathcal{C}$上一致。由于 $\mathcal{C}$是 $\pi$类，且存在 $C_n \in \mathcal{C}$，使 $C_n \uparrow \Omega, \mu(C_n) < \infty, n \geq 1$，故 $\mu$与 $\nu$在 $\sigma(\mathcal{C})$上一致（见引理1.4.6）， $\mu$的唯一性得证。

注3.6.9 在定理中, 如果不假定  $1 \in \mathcal{H}_{+}^{*}$, 但要求测度  $\mu$ 满足:

$$
\mu(A)=\inf\{\mu(C)\mid C\supset A,C\in\mathcal{C}\},\quad A\in\mathcal{F}   \tag*{(3.6.8)}
$$

则μ也是唯一确定的．事实上，设另有测度ν使对一切 $f \in \mathcal{H}$有 $I(f) = \nu(f)$，且满足 $(3.6.8)$式（以ν代替μ），则 $\forall C \in \mathcal{C}$，令 $f_n \in \mathcal{H}^+$， $f_n \uparrow I_C$，我们有

 
$$
\nu(C)=\lim_{n\to\infty}\nu(f_{n})=\lim_{n\to\infty}I(f_{n})=\lim_{n\to\infty}\mu(f_{n})=\mu(C).
$$
 

于是由(3.6.8)式知， $\nu$与 $\mu$在 $\mathcal{F}$上一致.

---

##### 习题

3.6.1 设$M$为一$n$维Riemann流形，$\mathcal{U}$是$M$的一个坐标邻域，$\{x^i\}$是$\mathcal{U}$中的坐标函数，$\{g_{ij}\}$为在$\mathcal{U}$中的Riemann度量系数，$G = \det[g_{ij}](\det$表示矩阵的行列式).令$C_c(M)$表示$M$上具紧支撑的连续泛函全体.设$f \in C_c(M)$，其支撑含于$\mathcal{U}$，定义

 
$$
\int_{\mathcal{U}}f=\int_{\mathcal{U}}f\sqrt{G}d x^{1}\cdots d x^{n}.
$$
 

对一般的 $f \in C_c(M)$，可利用上式及 $M$的一个单位分解来定义 $\int_M f$。试证 $f \mapsto \int_M f$为 $C_c(M)$上的Daniell积分。

3.6.2 设  $\nu$ 为  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 上一非负有限可加集函数， $\lim_{n \to \infty} \nu([-n, n]) = 1$，则存在  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 上唯一的概率测度  $\mu$，使得对  $\mathbb{R}$ 上任何有界连续函数  $f$ 有  $\nu(f) = \mu(f)$.

## 3.7 Bochner积分和Pettis积分

本节介绍两种常用的Banach空间值函数的积分——Bochner积分和Pettis积分。假定E为数域K(实域R或复域C)上的Banach空间，∥·∥为E上的范数，B(E)为E上的Borel σ代数，E*为E的对偶空间。此外，我们用s-lim表示E中的强收敛。

定义3.7.1 设$(\Omega, \mathcal{F})$为一可测空间，$X : \Omega \longrightarrow E$为$\Omega$上的$E$值函数。如果$X$关于$\mathcal{F}$及$\mathcal{B}(E)$可测（即$X^{-1}(\mathcal{B}(E)) \subset \mathcal{F}$），则称$X$为Borel可测；如果$\forall f \in E^*, f(X)$为$\Omega$上$\mathcal{F}$可测（$K$值）函数，则称$X$为弱可测；如果$X$为弱可测且有可分的值域（即$X(\Omega)$在$E$中有可数稠子集），则称$X$为强可测；如果$X$只取有限个值（即$X(\Omega)$为$E$的有限子集），则称$X$为简单函数。

令μ为(Ω, F)上一测度, ℬ为F关于μ的完备化. 如果在上述定义中将F换成ℬ, 则相应的Borel可测(弱可测)称为μ可测(弱μ可测). 这时, 称X : Ω → E为强μ可测, 是指X为弱μ可测, 且有μ可分的值域(即存在μ零测集N, 使得X(Ω \ N)在E中有可数稠子集).

显然: Borel可测蕴含弱可测; 对简单函数而言, Borel可测与弱可测等价; 若E为可分Banach空间, 则弱可测与强可测等价. 若X为Borel可测, 则作为X与E上连续函数 $x \mapsto \|x\|$的复合,  $\|X\|$为F可测实值函数.

下面我们将证明强可测函数必为Borel可测，并且研究强可测函数的结构．为此，先证明一个引理.

引理3.7.2 设E为可分Banach空间， $S_{1}(E^{*})$ 为 $E^{*}$ 的单位球．则存在 $S_{1}(E^{*})$ 中一序列 $\{f_{n}\}$，满足如下条件： $\forall f \in S_{1}(E^{*})$，可选取 $\{f_{n}\}$ 的一子列 $\{f_{n^{\prime}}\}$，使得 $\forall x \in E$ 有 $\lim_{n\to\infty} f_{n^{\prime}}(x) = f(x)$.

证 令  $\{x_{n}, n \geqslant 1\}$ 为 E 的可数稠子集.  $\forall n \geqslant 1$, 考虑  $S_{1}(E^{*})$ 到  $K^{n}$ 中的连续映射:  $f \mapsto \varphi_{n}(f) = \{f(x_{1}), \cdots, f(x_{n})\}$. 由于  $K^{n}$ 可分, 存在  $S_{1}(E^{*})$ 中序列  $\{f_{n,k}, k \geqslant 1\}$, 使

---

得 $\{\varphi_{n}(f_{n,k}),k\geqslant1\}$在 $\varphi_{n}(S_{1}(E^{*}))$中稠.现设 $f\in S_{1}(E^{*})$.对每个 $n\geqslant1$，选取 $m_{n}$，使得

 
$$
\left|f_{n,m_{n}}(x_{i})-f(x_{i})\right|<\frac{1}{n},\quad1\leqslant i\leqslant n.
$$
 

则有 $\lim_{n}f_{n,m_n}(x_i)=f(x_i),i=1,2,\cdots$。由于 $\|f_{n,m_n}\|\leq1,\forall n\geq1$，故容易推知： $\forall x\in E$，有 $\lim_{n}f_{n,m_n}(x)=f(x)$。

定理3.7.3 设 $(\Omega,\mathcal{F})$为一可测空间， $X:\Omega\longrightarrow E$强可测，则存在Borel可测简单函数序列 $\{X_{n}\}$，使得

$$
\|X_{n}(\omega)\|\leqslant2\|X(\omega)\|,\ n\geqslant1,\ \mathrm{s}\mathrm{-}\lim_{n\rightarrow\infty}X_{n}(\omega)=X(\omega),\ \omega\in\Omega.   \tag*{(3.7.1)}
$$

特别, X 为 Borel 可测. 此外, 强可测函数全体构成一向量空间, 且对序列的逐点强极限封闭.

证 首先证明  $\omega \mapsto \|X(\omega)\|$ 为  $\mathcal{F}$ 可测函数. 令  $E_0$ 为包含  $X(\Omega)$ 的  $E$ 的最小闭子空间, 则  $E_0$ 为可分 Banach 空间. 由于  $E_0^*$ 的元素是  $E^*$ 的元素在  $E_0$ 上的限制 (由 Hahn-Banach 定理知), 易知  $X : \Omega \longrightarrow E_0$ 亦为弱可测的. 设  $a \in \mathbb{R}_+$. 令

 
$$
A=\{\omega\mid\|X(\omega)\|\leqslant a\},A_{f}=\{\omega\mid|f(X(\omega))|\leqslant a\},f\in S_{1}(E_{0}^{*}),
$$
 

则有  $A \subset \bigcap_{f \in S_1(E_0^\star)} A_f$。另一方面， $\forall \omega \in \Omega$，由Hahn-Banach定理知，存在  $f \in E_0^\star$， $\|f\| = 1$，使得  $f(X(\omega)) = \|X(\omega)\|$。于是有  $A \supset \bigcap_{f \in S_1(E_0^\star)} A_f$，从而有  $A = \bigcap_{f \in S_1(E_0^\star)} A_f$。设序列  $\{f_n\} \subset S_1(E_0^\star)$ 满足引理3.7.2中的条件，则易知  $A = \bigcap_n A_{f_n} \in \mathcal{F}$。这表示  $\|X\|$ 为  $\mathcal{F}$ 可测的。

由于 $X(\Omega)$可分，对任意 $n\geq1,X(\Omega)$可以被至多可数多个半径不超过1/n的开球 $\{S_{j,n},j\geq1\}$覆盖.设 $x_{j,n}$为 $S_{j,n}$的球心， $r_{j,n}$为 $S_{j,n}$的半径，令

 
$$
B_{j,n}=\{\omega\left|X(\omega)\in S_{j,n}\right\},
$$
 

则有

 
$$
\bigcup_{j=1}^{\infty}B_{j,n}=\Omega,
$$
 

且由前面所证， $B_{j,n} = \{\omega \mid \|X(\omega) - x_{j,n}\| < r_{j,n}\}$ 为  $\mathcal{F}$ 可测．令  $B_{1,n}^{\prime} = B_{1,n}, B_{i,n}^{\prime} = B_{i,n} - \cup_{j=1}^{i-1} B_{j,n}, i \geq 2$，定义

 
$$
Y_{n}(\omega)=x_{i,n},\mathrm{~ 如果 ~}\omega\in B_{i,n}^{\prime},
$$
 

则 $\{Y_n\}$为可测简单函数序列，且 $s_n = \lim_{n \to \infty} Y_n(\omega) = X(\omega)$。当 $\|Y_n(\omega)\| \leq 2\|X(\omega)\|$时，令 $X_n(\omega) = Y_n(\omega)$，当 $\|Y_n(\omega)\| > 2\|X(\omega)\|$时，令 $X_n(\omega) = 0$，其中0是 $E$中的0元素，则Borel可测简单函数序列 $\{X_n\}$满足(3.7.1)式。定理中另一结论显然。

---

有了上述准备后，现在可定义强 $\mu$可测函数关于测度的积分.

定理3.7.4 设 $(\Omega,\mathcal{F},\mu)$为一测度空间，X为 $\Omega$到E的一强 $\mu$可测函数. 如果 $\|X\|$为 $\mu$可积，则存在E中唯一的元素，记为 $\int_{\Omega}Xd\mu$，使得

$$
f\Big(\int_{\Omega}X d\mu\Big)=\int_{\Omega}f(X)d\mu,\ \forall f\in E^{*}.   \tag*{(3.7.2)}
$$

这时有

$$
\|\int_{\Omega}X d\mu\|\leqslant\int_{\Omega}\|X\|d\mu.   \tag*{(3.7.3)}
$$

我们称X关于μ为Bochner可积，并称∫ΩXdμ为X关于μ的Bochner积分，简记为μ(X).

证 如果在完备测度空间( $\Omega,\overline{F},\mu$)中考虑，则存在一强可测函数 $\overline{X}$，它与 $X\mu$-a.e.相等。因此，为证明定理，不妨假定 $X$本身是 $(\Omega,\mathcal{F})$上一强可测函数。首先设 $X=\sum_{i=1}^{n}x_iI_{A_i}$为简单可测函数，其中 $x_i\neq0$， $A_i\in\mathcal{F}_i,1\leqslant i\leqslant n,A_i\cap A_j=\varnothing,i\neq j$，则 $\|X\|=\sum_{i=1}^{n}\|x_i\|I_{A_i}$。如果 $\|X\|$为 $\mu$可积，则对每个 $1\leqslant i\leqslant n$， $\mu(A_i)<\infty$。这时令

$$
\int_{\Omega}X d\mu=\sum_{i=1}^{n}\mu(A_{i})x_{i},   \tag*{(3.7.4)}
$$

易知它不依赖X的具体表示.对一般的强可测函数X，令 $\{X_n, n \geq 1\}$为满足(3.7.1)式的简单可测函数序列.假定 $\|X\|$为 $\mu$可积，则每个 $\|X_n\|$为 $\mu$可积，且有

$$
\|\int_{\Omega}X_{n}d\mu-\int_{\Omega}X_{m}d\mu\|\leqslant\int_{\Omega}\|X_{n}-X_{m}\|d\mu.   \tag*{(3.7.5)}
$$

由于 $\|X_n - X_m\| \leq 4\|X\|$，故由上式及控制收敛定理知， $\{\int_\Omega X_n \, d\mu\}$ 为 $E$中基本列，从而强收敛于一元素，记为 $\int_\Omega X \, d\mu$。显然， $\int_\Omega X \, d\mu$ 不依赖于满足 $(3.7.1)$式的序列 $\{X_n\}$的选取。现设 $f \in E^*$，显然有

 
$$
f\Big(\int_{\Omega}X_{n}d\mu\Big)=\int_{\Omega}f(X_{n})d\mu,
$$
 

两边令 $n \to \infty$即得(3.7.2)式. 由于 $f(x) = 0, \forall f \in E^* \Rightarrow x = 0$，故满足(3.7.2)式的 $\int_{\Omega} X d\mu$是唯一的.

最后，对简单可测函数 $X_{n}$，显然有

 
$$
\|\int_{\Omega}X_{n}d\mu\|\leqslant\int_{\Omega}\|X_{n}\|d\mu,
$$
 

故两边令 $n\to\infty$即得(3.7.3)式.

---

注3.7.5 (1) 设F为另一Banach空间, T为E到F中的有界线性算子. 由上述证明中关于 $\int_{\Omega}Xd\mu$的定义容易推知

$$
T\Big(\int_{\Omega}X d\mu\Big)=\int_{\Omega}T X d\mu,   \tag*{(3.7.6)}
$$

其中右端为TX关于 $\mu$的Bochner积分.

(2)由3.7.2式推知,Bochner积分具有通常积分的线性性.

(3)设X关于μ为Bochner可积, 则∀A ∈ ℝ, XIₐ仍为Bochner 可积, 其Bochner积分记为∫ₐ Xdμ. 令

$$
\nu(A)=\int_{A}X d\mu,\;A\in\mathcal{F},   \tag*{(3.7.7)}
$$

则 $\nu$为 $(\Omega,\mathcal{F})$上的下述意义下的E值测度：

(i) $\nu(\varnothing)=0;$

(ii) 对 A 中两两不相交集合序列  $\{A_i\}$，有  $\nu(\sum_{i=1}^{\infty}A_i) = \sum_{i=1}^{\infty}\nu(A_i)$.

我们称 $\nu$为X关于 $\mu$的不定积分. 显然 $\nu$关于 $\mu$在下述意义下是绝对连续的, 即 $\mu(A)=0\Rightarrow\nu(A)=0$. 此外, 令

$$
\|\nu\|_{\mathrm{var}}=\sup\Big\{\sum_{i=1}^{\infty}\left\|\nu(A_{i})\right\|\Big|\{A_{i}\}\subset\mathcal{F} 为 \Omega 的可数划分 \Big\},   \tag*{(3.7.8)}
$$

称 $\|\nu\|_{\mathrm{var}}$为 $\nu$的全变差，则有

$$
\|\nu\|_{\mathrm{v a r}}=\int_{\Omega}\|X\|d\mu.   \tag*{(3.7.9)}
$$

(4) 对Bochner积分, 有相应的控制收敛定理(见习题3.7.2), 但没有相应的Radon-Nikodym定理(见习题3.7.3).

最后, 作为本节的结束, 我们定义弱 $\mu$可测函数的Pettis积分.

定义3.7.6 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $X:\Omega\longrightarrow E$为一弱 $\mu$可测函数， $A\in\mathcal{F}$。如果 $\forall f\in E^{*},f(X)$为 $\mu$可积函数，且存在 $x_{A}\in E$，使得

 
$$
f(x_{A})=\int_{A}f(X)d\mu,\forall f\in E^{*},
$$
 

则称X为关于μ，在A上Pettis可积，并称 $x_A$为X关于μ，在A上的Pettis积分，记为 $(P)\int_A X \, d\mu$。设 $F_0$为F的子σ代数，在每个 $F_0$可测集上可积的弱μ可测函数称为在 $F_0$上Pettis可积。特别，在F上Pettis可积的弱μ可测函数简称为Pettis可积。这时我们称 $x \to x_A$为X的Pettis不定积分。

显然, Bochner可积的函数必为Pettis可积, 且 $\forall A \in \mathcal{F}$, 在A上的两种积分一致.

---

##### 习题

3.7.1 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $X:\Omega\longrightarrow E$为一强 $\mu$可测函数。试证：为使XBochner可积，必须且只需存在一列简单可测函数 $\{X_{n},n\geq1\}$，使得对a.e. $\omega\in\Omega,\quad\operatorname{s}-\lim_{n\to\infty}X_{n}(\omega)=X(\omega)$，且 $\lim_{n,m\to\infty}\int_{\Omega}\|X_{n}-X_{m}\|d\mu=0$。

3.7.2 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $\{X_{n}\}$为一列Bochner可积函数，X为一强 $\mu$可测函数。试证：如果对a.e. $\omega$, s- $\lim_{n\to\infty}X_{n}(\omega)=X(\omega)$，且存在一非负 $\mu$可积函数g，使得 $\|X_{n}\|\leq g$, a.e.,  $\forall n\geq1$，则X为Bochner可积，且有s- $\lim_{n\to\infty}\int_{\Omega}X_{n}d\mu=\int_{\Omega}Xd\mu$（提示： $\|X_{n}-X\|\leq2g$, a.e.).

3.7.3 设  $\mu$ 为 [0, 1] 上的 Lebesgue 测度,  $E = L^{1}([0,1], \mathcal{B}([0,1]), \mu)$. 对  $A \in \mathcal{B}([0,1])$, 令  $\nu(A) = I_{A}$. 试证:

(1)  $\nu$ 为关于  $\mu$ 绝对连续的 E 值测度；

(2) 不存在Bochner可积函数X:  $[0,1]\longrightarrow E$，使得

 
$$
\nu(A)=\int_{A}X d\mu,\ \forall A\in\mathcal{B}([0,1]).
$$
 

3.7.4 证明注3.7.5(3).

3.7.5 设 $(\Omega, \mathcal{F}, \mu)$为一测度空间， $E$为一自反的Banach空间（即 $E^{**} = E$）， $X : \Omega \longrightarrow E$为一弱 $\mu$可测函数。试证：如果 $\forall f \in E^*$， $f(X)$为 $\mu$可积，则 $X$为Pettis可积。

3.7.6 设 $(\Omega,\mathcal{F},\mu)$为一测度空间， $E$为一Banach空间， $X:\Omega \longrightarrow E$为一 $\mu$ Pettis可积函数。试证 $X$的Pettis不定积分为一 $E$值测度。

---

## 第 4 章 乘积可测空间上的测度与积分

## 4.1 乘积可测空间

定义4.1.1 设 $\Omega_{1},\Omega_{2}$为两个集合，令

 
$$
\Omega_{1}\times\Omega_{2}=\left\{\left(\omega_{1},\omega_{2}\right)\mid\omega_{1}\in\Omega_{1},\omega_{2}\in\Omega_{2}\right\},
$$
 

称 $\Omega_{1}\times\Omega_{2}$为 $\Omega_{1}$与 $\Omega_{2}$的乘积. 若 $(\Omega_{1},\mathcal{F}_{1})$及 $(\Omega_{2},\mathcal{F}_{2})$为两个可测空间, 我们在 $\Omega_{1}\times\Omega_{2}$上定义如下 $\sigma$代数:

 
$$
\mathcal{F}_{1}\times\mathcal{F}_{2}=\sigma\big\{A_{1}\times A_{2}\big|A_{1}\in\mathcal{F}_{1},A_{2}\in\mathcal{F}_{2}\big\},
$$
 

称 $F_{1}\times F_{2}$为乘积 $\sigma$代数， $(\Omega_{1}\times\Omega_{2},\mathcal{F}_{1}\times\mathcal{F}_{2})$为乘积可测空间.

上述定义容易推广到任意有限多个可测空间的乘积情形,下面我们将进一步定义一族可测空间的乘积.

定义4.1.2 设 $(\Omega_{i})_{i\in I}$为一族集合, $\Omega=\bigcup_{i\in I}\Omega_{i},\Omega^{I}$表示I到 $\Omega$中的映射全体.我们令

 
$$
\prod_{i\in I}\Omega_{i}=\{\omega\in\Omega^{I}\mid\omega(i)\in\Omega_{i},\forall i\in I\},
$$
 

称 $\prod_{i\in I}\Omega_{i}$为 $(\Omega_{i})_{i\in I}$的乘积.此外，对每个 $i\in I$，令

 
$$
\pi_{i}(\omega)=\omega(i),\quad\omega\in\prod_{i\in I}\Omega_{i},
$$
 

我们称 $\pi_i$为 $\prod_{i \in I} \Omega_i$到 $\Omega_i$上的投影(映射). 更一般地, 设 $\varnothing \neq S \subset I$, 令 $\pi_S$为 $\prod_{i \in I} \Omega_i$到 $\prod_{i \in S} \Omega_i$上的投影(映射), 即令

 
$$
\pi_{S}(\omega)=(\omega(i),i\in S),\omega\in\prod_{i\in I}\Omega_{i},
$$
 

这里 $(\omega(i),i\in S)$表示 $\prod_{i\in S}\Omega_{i}$中的一个元素，它在指标i处取值为 $\omega(i)$.

设 $(\Omega_i, \mathcal{F}_i)_{i \in I}$为一族可测空间，则在 $\prod_{i \in I} \Omega_i$上定义一 $\sigma$代数如下：

 
$$
\prod_{i\in I}\mathcal{F}_{i}=\sigma(\bigcup_{i\in I}\pi_{i}^{-1}(\mathcal{F}_{i})).
$$
 

称 $\prod_{i\in I}\mathcal{F}_i$为乘积 $\sigma$代数， $(\prod_{i\in I}\Omega_i,\prod_{i\in I}\mathcal{F}_i)$为乘积可测空间。

---

显然，乘积 $\sigma$代数是使每个投影 $\pi_{i}$为可测的最小 $\sigma$代数.

定理4.1.3 设  $\varnothing \neq S \subset I$，则  $\pi_{S}$ 为  $(\prod_{i \in I} \Omega_i, \prod_{i \in I} \mathcal{F}_i)$ 到  $(\prod_{i \in S} \Omega_i, \prod_{i \in S} \mathcal{F}_i)$ 上的可测映射.

证 由于  $\prod_{i\in S}F_{i}=\sigma(\bigcup_{i\in S}(\pi_{i}^{S})^{-1}(F_{i}))$ (这里  $\pi_{i}^{S}$ 表示  $\prod_{i\in S}\Omega_{i}$ 到  $\Omega_{i}$ 上的投影), 故由命题2.1.3知, 只需证

 
$$
\pi_{S}^{-1}(\bigcup_{i\in S}(\pi_{i}^{S})^{-1}(\mathcal{F}_{i}))\subset\prod_{i\in I}\mathcal{F}_{i}.
$$
 

但这由如下等式推得

 
$$
\pi_{S}^{-1}(\pi_{i}^{S})^{-1}(\mathcal{F}_{i})=\pi_{i}^{-1}(\mathcal{F}_{i}).
$$
 

□

定理4.1.4 令 $\mathcal{P}_{0}$(相应地, $\mathcal{P}$)表示I的非空有穷(相应地,至多可数)子集全体,则

(1) 可测矩形全体

 
$$
\mathcal{I}=\left\{\pi_{S}^{-1}(\prod_{i\in S}A_{i})\mid A_{i}\in\mathcal{F}_{i},i\in S;S\in\mathcal{P}_{0}\right\}
$$
 

为 $\prod_{i\in I}\Omega_i$上的一半代数，且 $\sigma(\mathcal{I})=\prod_{i\in I}\mathcal{F}_i;$

(2) 可测柱集全体

 
$$
\mathcal{Z}=\left\{\pi_{S}^{-1}(\prod_{i\in S}\mathcal{F}_{i})\mid S\in\mathcal{P}_{0}\right\}
$$
 

为 $\prod_{i\in I}\Omega_{i}$上的一代数，且 $\sigma(\mathcal{Z})=\prod_{i\in I}\mathcal{F}_{i};$

(3)  $\prod_{i\in I}\mathcal{F}_i = \{\pi_S^{-1}(\prod_{i\in S}\mathcal{F}_i) \mid S\in\mathcal{P}\}$.

我们将这一定理的证明留给读者完成.

##### 习题

4.1.1 设  $I$ 为一可数集， $(\Omega_i, \mathcal{F}_i)$ 为一族可测空间。若每个  $\mathcal{F}_i$ 可分，则  $\prod_{i \in I} \mathcal{F}_i$ 也可分。

4.1.2 设 $(\Omega_i, \mathcal{F}_i)_{i \in I}$为一族可测空间， $C_i$为 $\mathcal{F}_i$的子类， $i \in I$。若对每个 $i \in I$， $\sigma(C_i) = \mathcal{F}_i$，则有 $\prod_{i \in I} \mathcal{F}_i = \sigma(\bigcup_{i \in I} \pi_i^{-1}(C_i))$。

## 4.2 乘积测度与Fubini定理

设 $(X, \mathcal{A}, \mu)$及 $(Y, \mathcal{B}, \nu)$为两个 $\sigma$有限测度空间。本节将在乘积可测空间 $(X \times Y, \mathcal{A} \times \mathcal{B})$上定义一乘积测度 $\mu \times \nu$，并讨论关于测度 $\mu \times \nu$的积分。

定义4.2.1 设X及Y是两个集合, E是 $X \times Y$的子集. 令

 
$$
E_{x}=\{y\in Y\mid(x,y)\in E\},
$$
 

---

 
$$
E^{y}=\{x\in X\mid(x,y)\in E\},
$$
 

分别称 $E_{x}$及 $E^{y}$为E在x及y处的截口.

设 $f(x,y)$为 $X\times Y$上的一函数，我们将使用如下记号：

 
$$
f_{x}(y)=f(x,y),\quad f^{y}(x)=f(x,y).
$$
 

引理4.2.2 设 $(X,A)$及 $(Y,B)$为可测空间.

(1) 若  $E \in \mathcal{A} \times \mathcal{B}$，则  $\forall x \in X, y \in Y$，有  $E_x \in \mathcal{B}, E^y \in \mathcal{A}$.

(2) 若  $f$ 为  $X \times Y$ 上的  $A \times B$ 可测函数，则对一切  $x \in X, y \in Y, f_x$ 为  $Y$ 上的  $B$ 可测函数， $f^y$ 为  $X$ 上的  $A$ 可测函数。

证 (1) 令  $C = \{A \times B \mid A \in \mathcal{A}, B \in \mathcal{B}\}$. 则对一切  $E \in \mathcal{C}$，引理的结论显然成立. 令  $G = \{E \in \mathcal{A} \times B \mid \forall x \in X, y \in Y, E_x \in \mathcal{B}, E^y \in \mathcal{A}\}$，则  $G$ 为  $\lambda$ 类. 由于  $C$ 为  $\pi$ 类，且  $\sigma(C) = A \times B$，故由单调类定理 (定理1.2.2) 知，对一切  $E \in A \times B$，引理结论成立.

(2) 容易由定理2.2.1推得.

引理4.2.3 令 $(X, \mathcal{A}, \mu)$及 $(Y, \mathcal{B}, \nu)$为两个 $\sigma$有限测度空间. 设  $E \in \mathcal{A} \times \mathcal{B}$，则函数  $x \mapsto \nu(E_x)$为 $\mathcal{A}$可测，函数  $y \mapsto \mu(E^y)$为 $\mathcal{B}$可测.

证 首先设$\nu$为有限测度，令$\mathcal{C}=\{A\times B\mid A\in\mathcal{A},B\in\mathcal{B}\}$，令$\mathcal{G}=\{E\in\mathcal{A}\times\mathcal{B}\mid x\mapsto\nu(E_x)$为$\mathcal{A}$可测$\{x\}$，则显然有$\mathcal{C}\subset\mathcal{G}$（因$\nu((A\times B)_x)=I_A(x)\nu(B)$），且$\mathcal{G}$为$\lambda$类。故由单调类定理知$\mathcal{G}\supset\sigma(\mathcal{C})=\mathcal{A}\times\mathcal{B}$，即$\mathcal{G}=\mathcal{A}\times\mathcal{B}$。现设$\nu$为$\sigma$有限测度，任取$Y$的可数划分$\{D_n\}$，使$D_n\in\mathcal{B},\nu(D_n)<\infty,n\geq1$，令$\nu_n(B)=\nu(B\cap D_n),B\in\mathcal{B}$，则$\nu_n$为有限测度，$\nu=\sum_{n=1}^{\infty}\nu_n$。于是

 
$$
\nu(E_{x})=\sum_{n=1}^{\infty}\nu_{n}(E_{x}),\ E\in\mathcal{A}\times\mathcal{B},
$$
 

从而函数 $x \to \nu(E_x)$为 $\mathcal{A}$可测，同理可证函数 $y \to \mu(E^y)$为 $\mathcal{B}$可测。

定理4.2.4 设 $(X,\mathcal{A},\mu)$及 $(Y,\mathcal{B},\nu)$为两个 $\sigma$有限测度空间.则在 $\mathcal{A}\times\mathcal{B}$上存在唯一的测度 $\mu\times\nu$，使得

$$
(\mu\times\nu)(A\times B)=\mu(A)\nu(B),\ A\in\mathcal{A},\ B\in\mathcal{B}.   \tag*{(4.2.1)}
$$

(从而 $\mu \times \nu$亦为 $\sigma$有限.) 此外, 对任何 $E \in \mathcal{A} \times \mathcal{B}$, 有

$$
(\mu\times\nu)(E)=\int_{X}\nu(E_{x})\mu(d x)=\int_{Y}\mu(E^{y})\nu(d y).   \tag*{(4.2.2)}
$$

测度 $\mu \times \nu$称为 $\mu$与 $\nu$的乘积.

证 由引理4.2.3, 可在 $A \times B$上定义如下集函数 $\lambda_1$及 $\lambda_2$:

 
$$
\lambda_{1}(E)=\int_{X}\nu(E_{x})\mu(d x),\qquad E\in\mathcal{A}\times\mathcal{B},
$$
 

---

 
$$
\lambda_{2}(E)=\int_{Y}\mu(E^{y})\nu(d y),\qquad E\in\mathcal{A}\times\mathcal{B},
$$
 

显然， $\lambda_{1}$ 及  $\lambda_{2}$ 均为测度，且有

$$
\lambda_{1}(A\times B)=\lambda_{2}(A\times B)=\mu(A)\nu(B),\ A\in\mathcal{A},\ B\in\mathcal{B}.   \tag*{(4.2.3)}
$$

令 $C = \{A \times B \mid A \in \mathcal{A}, B \in \mathcal{B}\}$，则 $C$为半代数(见定理4.1.4)。依假定， $\mu$及 $\nu$为 $\sigma$有限测度，故满足(4.2.1)式的测度在 $C$上也是 $\sigma$有限的。因此，由测度扩张的唯一性(见定理1.4.7)知，满足(4.2.1)式的测度是唯一的。特别，我们有 $\lambda_1 = \lambda_2$，令 $\mu \times \nu = \lambda_1 = \lambda_2$，即有(4.2.2)式。

下面我们研究关于乘积测度的积分.

定理4.2.5 令 $(X,A,\mu)$及 $(Y,B,\nu)$为 $\sigma$有限测度空间， $f$为 $X\times Y$上的非负 $A\times B$可测函数。则函数 $x\mapsto\int_Y f_x\,d\nu$为 $A$可测， $y\mapsto\int_X f^y\,d\mu$为 $B$可测，且有

$$
\int_{X\times Y}f d(\mu\times\nu)=\int_{Y}\Big(\int_{X}f^{y}d\mu\Big)\nu(d y)=\int_{X}\Big(\int_{Y}f_{x}d\nu\Big)\mu(d x).   \tag*{(4.2.4)}
$$

证 不妨假定μ及ν均为有限测度. 令 $C = \{A \times B \mid A \in \mathcal{A}, B \in \mathcal{B}\}$. 由定理4.2.4知: C中集合的示性函数满足定理的结论. 故由定理2.2.1知: 对一切有界的 $A \times B$可测函数f, 定理的结论成立. 因此, 对一切非负 $A \times B$可测函数f, 定理结论亦成立.

系4.2.6 在定理4.2.5的假设下，若f是一非负可积函数，则 $\mu\{x\mid\nu(f_{x})=\infty\}=\nu\{y\mid\mu(f^{y})=\infty\}=0.$

证 直接由4.2.4式看出.

下一定理称为Fubini定理. 它使我们可以用叠积分来表达关于乘积测度的积分.

定理4.2.7 设 $(X,A,\mu)$及 $(Y,B,\nu)$为 $\sigma$有限测度空间， $f$为 $X\times Y$上一 $\mathcal{A}\times\mathcal{B}$可测函数。若 $f$关于 $\mu\times\nu$可积（相应地，积分存在），则有下列结论：

(1) 对  $\mu$-a.e. x,  $f_{x}$ 为  $\nu$ 可积 (相应地, 关于  $\nu$ 积分存在); 对  $\nu$-a.e. y,  $f^{y}$ 为  $\mu$ 可积 (相应地, 关于  $\mu$ 积分存在);

(2) 令

 
$$
\begin{aligned}I_{f}(x)&=\left\{\begin{aligned}&\int_{Y}f_{x}d\nu,& 若 f_{x} 为 \nu 可积 ( 相应地 , 积分存在 ),\\&0,& 其他情形 ,\end{aligned}\right.\\I^{f}(y)&=\left\{\begin{aligned}&\int_{X}f^{y}d\mu,& 若 f^{y} 为 \mu 可积 ( 相应地 , 积分存在 ),\\&0,& 其他情形 ,\end{aligned}\right.\end{aligned}
$$
 

则 $I_{f}$为 $\mu$可积(相应地,积分存在),  $I^{f}$为 $\nu$可积(相应地,积分存在),且有

$$
\int_{X\times Y}f d(\mu\times\nu)=\int_{X}I_{f}(x)\mu(d x)=\int_{Y}I^{f}(y)\nu(d y).   \tag*{(4.2.5)}
$$


---

证 首先设f为非负且为 $\mu\times\nu$可积.则由系4.2.6知结论(1)成立,且有

 
$$
I_{f}(x)=\nu(f_{x}),\ \mu\mathrm{-a.e.}\ x,
$$
 

 
$$
I^{f}(y)=\mu(f^{y}),\ \nu\mathrm{-a.e.}\ y.
$$
 

于是结论(2)由(4.2.4)式推得. 对一般f, 分别考虑 $f^{+}$及 $f^{-}$, 即得定理结论.

由于 $\nu(f_{x})$是 $\mu$-a.e.有定义的， $\mu(f^{y})$是 $\nu$-a.e.有定义的，所以通常也将(4.2.5)式写成(4.2.4)式的形式.

Fubini定理有很多的应用.我们将通过下面的习题向读者介绍一些应用的例子.

##### 习题

4.2.1 设R为实直线，试证 $\mathcal{B}(\mathbb{R}) \times \mathcal{B}(\mathbb{R}) = \mathcal{B}(\mathbb{R}^2)$. (注意：对一般拓扑空间X，不一定有 $\mathcal{B}(X) \times \mathcal{B}(X) = \mathcal{B}(X \times X)$，一般只有 $\mathcal{B}(X) \times \mathcal{B}(X) \subset \mathcal{B}(X \times X)$，参见引理5.6.4.)

4.2.2 设 $(X, A, \mu)$及 $(Y, B, \nu)$为 $\sigma$有限测度空间， $E \in A \times B$，则下列条件等价：

(1)  $(\mu \times \nu)(E) = 0;$

(2)  $\mu(E^y) = 0, \nu\text{-a.e.} \, y;$

(3)  $\nu(E_x) = 0$,  $\mu$-a.e. x.

4.2.3 设 $(X,A)$及 $(Y,B)$为可测空间， $\mu_{1}$及 $\nu_{1}$为 $(X,A)$上的 $\sigma$有限测度， $\mu_{2}$及 $\nu_{2}$为 $(Y,B)$上的 $\sigma$有限测度.若 $\nu_{1}\ll\mu_{1}$且 $\nu_{2}\ll\mu_{2}$，则 $\nu_{1}\times\nu_{2}\ll\mu_{1}\times\mu_{2}$，且有

 
$$
\frac{d(\nu_{1}\times\nu_{2})}{d(\mu_{1}\times\mu_{2})}(x,y)=\frac{d\nu_{1}}{d\mu_{1}}(x)\frac{d\nu_{2}}{d\mu_{2}}(y),\quad\mu_{1}\times\mu_{2}\mathrm{-a.e.}.
$$
 

4.2.4 设 $\sum_{m,n}a_{m,n}$为绝对收敛的双重级数.试用Fubini定理证明

 
$$
\sum_{m=1}^{\infty}\sum_{n=1}^{\infty}a_{m,n}=\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}a_{m,n}.
$$
 

4.2.5 试用Fubini定理证明 $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp(-\frac{x^{2}}{2})dx=1.$ (提示：考虑

 
$$
\int_{-\infty}^{\infty}\exp(-\frac{x^{2}}{2})dx\int_{-\infty}^{\infty}\exp(-\frac{y^{2}}{2})dy,
$$
 

并令 $r^{2}=x^{2}+y^{2}.$

4.2.6 设 $(X,A,\mu)$为 $\sigma$有限测度空间，f为X上的一非负A可测函数.试证

 
$$
\int_{X}f(x)\mu(dx)=\int_{0}^{\infty}\mu([f>y])dy.
$$
 

(提示: 设  $\lambda$ 为  $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 上的 Lebesgue 测度, 令

 
$$
E=\left\{(x,y)\in X\times\mathbb{R}\mid0\leqslant y<f(x)\right\},
$$
 

---

则 $\lambda(E_{x})=f(x).$

4.2.7 设  $f(t)$ 及  $g(t)$ 为  $[0, \infty)$ 上的两个右连续增函数. 我们用  $\mu_f$ 及  $\mu_g$ 分别表示它们在  $[0, \infty)$ 上诱导出的测度(见定理1.5.4). 试证: 对  $0 \leqslant a < b < \infty$, 有

 
$$
f(b)g(b)-f(a)g(a)=\int_{a}^{b}f(s)\mu_{g}(ds)+\int_{a}^{b}g(s-)\mu_{f}(ds),
$$
 

其中 $g(s-)=\lim_{t\uparrow\uparrow s}g(t)$（记号 $t\uparrow\uparrow s$表示 $t\rightarrow s$，且 $t<s$）（提示：将 $(a,b]\times(a,b]$表示为 $\{(x,y)\mid a<x\leqslant y\leqslant b\}\cup\{(x,y)\mid a<y<x\leqslant b\}$并分别计算它们的 $\mu_f\times\mu_g$测度）.

4.2.8 设  $f \in L^{1}(\mathbb{R}), g \in L^{p}(\mathbb{R})$，则有下列结论：

(1)  $(x,t) \mapsto f(x - t)g(t)^p$ 为  $\mathcal{B}(\mathbb{R}^2)$ 可测，且 Lebesgue 可积；

(2) 对 a.e.  $x, t \mapsto f(x - t)g(t)$ 为 Lebesgue 可积.

定义 $f$与 $g$的卷积如下： $\forall x \in \mathbb{R}$，令

 
$$
f*g(x)=\left\{\begin{aligned}&\int_{-\infty}^{\infty}f(x-t)g(t)dt,& 可积情形 ,\\ &0,& 其他情形 ,\end{aligned}\right.
$$
 

则  $f * g \in L^p(\mathbb{R})$，且有如下的Young不等式： $\| f * g \|_p \leqslant \| f \|_1 \| g \|_p$（提示：对  $1 \leqslant p \leqslant \infty$ 情形，利用Hölder不等式及Fubini定理）。

(3) 若 g 有界，则  $f \ast g$ 连续（提示：利用习题 3.4.8）.

4.2.9 (Steinhaus 引理) 设E为R的一Borel子集，令 $D(E) = \{x - y \mid x, y \in E\}$，如果E的Lebesgue测度 $\lambda(E) > 0$，则 $D(E)$包含一含原点的开区间。(提示：不妨设 $\lambda(E) < \infty$，以 $x + E$表示 $\{x + y \mid y \in E\}$，以 $-E$表示 $\{-x \mid x \in E\}$。令 $F(x) = \lambda(E \cap (x + E))$，则 $F(x) = I_{-E} * I_{E}(x)$。由习题4.2.8(3)知 $F(x)$连续，又依假定 $F(0) > 0$。

4.2.10 (Steinhaus引理的推广) 设A, B为R的两个Borel子集, 令

 
$$
D(A,B)=\{y-z\mid y\in A,z\in B\},
$$
 

若$\lambda(A) > 0$，且$\lambda(B) > 0$，则$D(A, B)$包含一非空开区间。（提示：不妨设$\lambda(A) < \infty, \lambda(B) < \infty$，令$F(x) = \lambda(A \cap (x + B))$，则$F(x) = I_{-A} * I_B(x)$，且由Fubini定理知$\int F(x) \lambda(dx) = \lambda(A) \lambda(B)$。于是存在某$x$，使$F(x) > 0$。）

4.2.11 设 $f(x,y)$为定义于 $V=(a,b)\times(c,d)$上的一实值连续函数. 如果f满足下列条件:

(1) $\frac{\partial f}{\partial x}$在V上存在且连续;

(2) 对某个  $x_{0} \in (a, b)$,  $\frac{d}{dy}[f(x_{0}, y)]$ 对一切  $y \in (c, d)$ 存在;

 $\frac{\partial^{2}f}{\partial y\partial x}$ 在 V 上存在且连续，

则 $\frac{\partial f}{\partial y},\frac{\partial^{2}f}{\partial x\partial y}$在V上存在，且有 $\frac{\partial^{2}f}{\partial x\partial y}=\frac{\partial^{2}f}{\partial y\partial x}$

(提示: 任取  $y_0 \in (c, d)$，由Fubini定理得)

 
$$
f(\overline{x},\overline{y})-f(x_{0},\overline{y})-f(\overline{x},y_{0})+f(x_{0},y_{0})=\int_{y_{0}}^{\overline{y}}\int_{x_{0}}^{\overline{x}}\frac{\partial^{2}f}{\partial y\partial x}dxdy,
$$
 

其中对每个 $\overline{x}\in(a,b)$， $\int_{x_{0}}^{\overline{x}}\frac{\partial^{2}f}{\partial y\partial x}dx$为y的连续函数.)

---

### 4.3 由 $\sigma$有限核产生的测度

本节将推广4.2节的结果.

定义4.3.1 令 $(X,A)$及 $(Y,B)$为两个可测空间.一函数 $K:X\times B\longrightarrow[0,\infty]$称为从 $(X,A)$到 $(Y,B)$的一个核(kernel)，如果它满足下列条件：

(1)  $\forall x \in X, K(x, \cdot)$ 为  $(Y, \mathcal{B})$ 上的测度;

(2)  $\forall B \in \mathcal{B}, K(\cdot, B)$ 为 X 上的 A 可测函数.

称K为有限核，如果 $\forall x \in X, K(x, Y) < \infty$；称K为概率核，如果 $\forall x \in X, K(x, Y) = 1$；称K为 $\sigma$有限的，如果存在Y的一个可数划分 $Y = \sum_n B_n$，使得 $B_n \in \mathcal{B}, n \geq 1$，且对一切 $x \in X$及 $n \geq 1$，有 $K(x, B_n) < \infty$。

命题4.3.2 设K为从 $(X,A)$到 $(Y,B)$的一个核， $\mu$为 $(X,A)$上的一测度，f为Y上的一非负B可测函数.

(1) 令  $\nu(B) = \int_X K(x, B) \mu(dx)$,  $B \in \mathcal{B}$, 则  $\nu$ 为  $(Y, \mathcal{B})$ 上的一测度.

(2) $x\mapsto\int_{Y}f(y)K(x,dy)$为X上的一A可测函数.

(3) 我们有

$$
\int f(y)\nu(d y)=\int\big[\int f(y)K(x,d y)\big]\mu(d x).   \tag*{(4.3.1)}
$$

证 (1)显然. 为证(2)及(3), 首先考虑非负简单可测函数f, 然后利用定理2.1.8(2)立即推得结论.

下一定理推广了定理4.2.4.

定理4.3.3 设K为 $(X,A)$到 $(Y,B)$的一个 $\sigma$有限核， $\mu$为 $(X,A)$上的一测度.

(1) 令  $N(x, E) = K(x, E_x)$,  $E \in \mathcal{A} \times \mathcal{B}$，则 N 为从  $(X, \mathcal{A})$ 到  $(X \times Y, \mathcal{A} \times \mathcal{B})$ 的一个  $\sigma$ 有限核.

(2) 令

$$
\mu K(E)=\int_{X}K(x,E_{x})\mu(d x),\ E\in\mathcal{A}\times\mathcal{B},   \tag*{(4.3.2)}
$$

则 $\mu K$为 $A \times B$上的一测度，且有

$$
\mu K(A\times B)=\int_{A}K(x,B)\mu(dx),\ A\in\mathcal{A},B\in\mathcal{B}.   \tag*{(4.3.3)}
$$

(3) 若  $\mu$ 为  $\sigma$ 有限测度，则  $\mu K$ 亦为  $\sigma$ 有限测度，且它是  $(X \times Y, A \times B)$ 上唯一满足 (4.3.3) 式的测度.

证 (1)首先，对任何 $x\in X,N(x,\cdot)$显然是 $(X\times Y,\mathcal{A}\times B)$上的测度. 令 $\{B_{n},n\geq1\}$为Y的一可数划分，使得 $B_{n}\in\mathcal{B},n\geq1$，且对一切 $x\in X$，及 $n\geq1$，有 $K(x,B_{n})<\infty$. 令

 
$$
\mathcal{B}_{n}=B_{n}\cap\mathcal{B},\quad\mathcal{C}_{n}=\left\{A\times C\mid A\in\mathcal{A},C\in\mathcal{B}_{n}\right\},
$$
 

---

 
$$
\mathcal{G}_{n}=\{E\in\mathcal{A}\times\mathcal{B}_{n}\mid N(\cdot,E) 为 \mathcal{A} 可测 \},
$$
 

则 $C_n$为 $X \times B_n$上的 $\pi$类，且生成 $\sigma$代数 $A \times B_n$。显然 $G_n$为 $X \times B_n$上的 $\lambda$类，且 $G_n \supset C_n$，故由单调类定理知 $G_n = A \times B_n$。现设 $E \in A \times B$，令 $E_n = E \cap (X \times B_n)$，则易知 $E_n \in A \times B_n$，且 $E = \sum_{n=1}^{\infty} E_n$。于是我们有

 
$$
N(x,E)=\sum_{n}N(x,E_{n}),\ x\in X,
$$
 

从而 $N(\cdot,E)$为 $\mathcal{A}$可测．此外，我们有 $N(x,X\times B_{n})=K(x,B_{n})<\infty$，因此N为 $\left(X,\mathcal{A}\right)$到 $(X\times Y,\mathcal{A}\times\mathcal{B})$的 $\sigma$有限核.

(2) 显然. 往证(3). 设  $\mu$ 为  $\sigma$ 有限测度, 令  $\{A_n, n \geq 1\}$ 为  $X$ 的一可数划分, 使得  $A_n \in A, \mu(A_n) < \infty, n \geq 1$. 令  $\{B_n\}$ 如在(1)的证明中所取的  $Y$ 的划分, 再令

 
$$
A_{m,k,l}=\left[l-1\leqslant K(\cdot,B_{k})<l\right]\cap A_{m},\ m,k,l\geqslant1,
$$
 

则对一切 $k\geqslant1$，我们有 $\sum_{m,l}A_{m,k,l}=X$，且有

 
$$
\mu K(A_{m,k,l}\times B_{k})=\int_{A_{m,k,l}}K(x,B_{k})\mu(dx)<\infty.
$$
 

由于 $\sum_{m,k,l}A_{m,k,l}\times B_k=X\times Y$，故 $\mu K$限于半代数 $\mathcal{C}=\{A\times B\mid A\in\mathcal{A},B\in\mathcal{B}\}$为 $\sigma$有限。因此，由定理1.4.7知，满足(4.3.3)式的测度 $\mu K$是唯一的。

如果对每个  $x \in X$ 有  $K(x, \cdot) = \nu$，则  $\mu K = \mu \times \nu$。因此，下一定理推广了定理4.2.5.

定理4.3.4 设K为 $(X,A)$到 $(Y,B)$的一个 $\sigma$有限核， $\mu$为 $(X,A)$上的一 $\sigma$有限测度， $f$为 $X \times Y$上的一非负 $A \times B$可测函数，则

(1)  $x \to \int_{Y} f(x, y) K(x, dy)$ 为 A 可测函数;

(2) 我们有

$$
\int_{X\times Y}f d(\mu K)=\int_{X}\Big[\int_{Y}f(x,y)K(x,d y)\Big]\mu(d x).   \tag*{(4.3.4)}
$$

证 令  $C = \{A \times B \mid A \in A, B \in B\}$，不妨假定  $\mu$ 为有限测度，且  $\forall x \in X, K(x, \cdot)$ 也为有限测度（如若不然，分别取 X 及 Y 的可数划分  $\{A_n\}$ 及  $\{B_n\}$，使得  $\forall x \in X, n \geq 1$ 有  $K(x, B_n) < \infty, \mu(A_n) < \infty$，并在每个  $A_n \times B_m$ 上考虑问题）。由命题 4.3.2 及 (4.3.3) 式易知：对 C 中集合的示性函数定理的结论成立。故由定理 2.2.1 知：对一切有界的  $A \times B$ 可测函数 f 结论成立。最后，由积分的单调收敛定理推知：对一切非负  $A \times B$ 可测函数 f 结论成立。

---

##### 习题

4.3.1 (Fubini定理的推广形式) 设K为从 $(X,A)$到 $(Y,B)$的一个 $\sigma$有限核， $\mu$为 $(X,A)$上的 $\sigma$有限测度， $\mu K$为 $(4.3.2)$式定义的测度. 若 $f$为 $X \times Y$上一 $\mathcal{A} \times \mathcal{B}$可测函数，它关于 $\mu K$可积(相应地，积分存在)，则有下列结论：

(1) 对  $\mu$-a.e. x,  $f_{x}$ 关于  $K(x, \cdot)$ 可积 (相应地, 积分存在);

(2)  $\forall x \in X$, 令

 
$$
I_{f}(x)=\left\{\begin{aligned}&\int_{Y}f_{x}(y)K(x,dy),& 可积 ( 相应地 , 积分存在 ) 情形 ,\\ &0,& 其他情形 ,\end{aligned}\right.
$$
 

则 $I_{f}$为 $\mu$可积(相应地,积分存在),且有

 
$$
\int_{X\times Y}f d(\mu K)=\int_{X}I_{f}(x)\mu(d x).
$$
 

4.3.2 设 $(X_{j},A_{j}),j=1,\cdots,n$为可测空间， $\mu_{1}$为 $(X_{1},\mathcal{A}_{1})$上的一 $\sigma$有限测度.对 $2\leqslant i\leqslant n$,设 $K(x_{1},\cdots,x_{i-1},dx_{i})$为从 $\left(\prod_{i=1}^{i-1}X_{j},\prod_{i=1}^{i-1}\mathcal{A}_{i}\right)$到 $(X_{i},\mathcal{A}_{i})$的一个 $\sigma$有限核.证明下列结论：

(1) 在 $\left(\prod_{j=1}^{n} X_{j}, \prod_{j=1}^{n} A_{j}\right)$上存在唯一的测度 $\mu$，使得对一切可测矩形 $\prod_{j=1}^{n} A_{j} \in \prod_{j=1}^{n} A_{j}$有

 
$$
\mu(\prod_{j=1}^{n}A_{j})=\int_{A_{1}}\mu_{1}(d x_{1})\int_{A_{2}}K(x_{1},d x_{2})\cdots\int_{A_{n}}K(x_{1},\cdots,x_{n-1},d x_{n}).
$$
 

此外， $\mu$ 是  $\sigma$ 有限测度；

(2) 设  $f$ 为  $(\prod_{j=1}^{n} X_{j}, \prod_{i=1}^{n} A_{j})$ 上的非负可测函数，则有

 
$$
\begin{align*}\int f d\mu=&\int_{X_{1}}\mu_{1}(dx_{1})\int_{X_{2}}K(x_{1},dx_{2})\cdots\int_{X_{n-1}}K(x_{1},\cdots,x_{n-2},dx_{n-1})\\&\cdot\int_{X_{n}}f(x_{1},\cdots,x_{n})K(x_{1},\cdots,x_{n-1},dx_{n}).\end{align*}
$$
 

4.3.3 设  $K_{1}, K_{2}$ 为从  $(X, A)$ 到  $(Y, B)$ 的  $\sigma$ 有限核， $\mu_{1}, \mu_{2}$ 为  $(X, A)$ 上的测度. 为要  $\mu_{1}K_{1}$ 关于  $\mu_{2}K_{2}$ 绝对连续，必须且只需  $\mu_{1}$ 关于  $\mu_{2}$ 绝对连续，且对  $\mu_{1}$-a.e.  $x \in X, K_{1}(x, \cdot)$ 关于  $K_{2}(x, \cdot)$ 绝对连续. 此外，这时有

 
$$
\frac{d(\mu_{1}K_{1})}{d(\mu_{2}K_{2})}(x,y)=\frac{d K_{1}(x,\cdot)}{d K_{2}(x,\cdot)}(y)\frac{d\mu_{1}}{d\mu_{2}}(x).
$$
 

### 4.4 无穷乘积空间上的概率测度

在概率论中, 我们经常要讨论任意有限多个试验(不一定相互独立). 为了能在同一概率空间中考虑它们, 我们需要在无穷乘积可测空间上构造概率测度. 下一定理(Tulcea定理)解决了这一问题.

---

定理4.4.1 令$\{(\Omega_j, \mathcal{F}_j), j \geq 1\}$为一列可测空间，$\Omega = \prod_{j=1}^{\infty} \Omega_j, \mathcal{F} = \prod_{j=1}^{\infty} \mathcal{F}_j, \mathbb{P}_1$为$(\Omega_1, \mathcal{F}_1)$上的一概率测度。$\forall i \geq 2, P(\omega_1, \cdots, \omega_{i-1}, d\omega_i)$为从$(\prod_{j=1}^{i-1} \Omega_j, \prod_{j=1}^{i-1} \mathcal{F}_j)$到$(\Omega_i, \mathcal{F}_i)$的一个概率核。则存在$(\Omega, \mathcal{F})$上唯一的概率测度$P$，使得对一切$n \geq 1$，有

$$
\mathbb{P}(B^{n}\times\prod_{j=n+1}^{\infty}\Omega_{j})=\mathbb{P}_{n}(B^{n}),\quad B^{n}\in\prod_{j=1}^{n}\mathcal{F}_{j},   \tag*{(4.4.1)}
$$

其中 $P_{n}$为 $\prod_{j=1}^{n}F_{j}$上如下定义的概率测度(见习题4.3.2):

 
$$
\begin{align*}\mathbb{P}_{n}(B^{n})=&\int_{\Omega_{1}}\mathbb{P}(d\omega_{1})\int_{\Omega_{2}}P(\omega_{1},d\omega_{2})\cdots\int_{\Omega_{n-1}}P(\omega_{1},\cdots,\omega_{n-2},d\omega_{n-1})\\&\cdot\int_{\Omega_{n}}I_{B^{n}}(\omega_{1},\cdots,\omega_{n})P(\omega_{1},\cdots,\omega_{n-1},d\omega_{n}).\end{align*}
$$
 

证 设n>m为两个自然数,则显然有

 
$$
\mathbb{P}_{n}(B^{m}\times\prod_{j=m+1}^{n}\Omega_{j})=\mathbb{P}_{m}(B^{m}),
$$
 

于是可按(4.4.1)式在可测柱集全体Z上定义一集函数IP。令 $F^n = \{B^n \times \prod_{j=n+1}^\infty \Omega_j \mid B^n \in \prod_{j=1}^n F_j\}$，则 $F^n \subset F^{n+1}$，且 $\bigcup_n F^n = \mathcal{Z}$。由于IP限于每个 $F^n$为概率测度，故IP在代数Z上是有限可加的。往证IP为Z上的概率测度，为此只需证IP在空集 $\emptyset$处连续。我们用反证法。假定有 $A_n \in \mathcal{Z}, n \geq 1, A_n \downarrow \emptyset$，使得 $\lim_{n \to \infty} \mathbb{P}(A_n) > 0$。必要时在序列 $(A_n)$首项前添加若干项 $\Omega$，且在两个集 $A_n$及 $A_{n+1}$之间适当重复若干项 $A_n$，我们可以进一步假定 $A_n \in \mathcal{F}^n$。因此有 $A_n = B^n \times \prod_{j=n+1}^\infty \Omega_j$。由于 $A_{n+1} \subset A_n$，我们有 $B^{n+1} \subset B^n \times \Omega_{n+1}$。此外，对每个 $n > 1$，

 
$$
\mathbb{P}(A_{n})=\int_{\Omega_{1}}g_{n}^{(1)}(\omega_{1})\mathbb{P}_{1}(d\omega_{1}),
$$
 

其中

 
$$
g_{n}^{(1)}(\omega_{1})=\int_{\Omega_{2}}P(\omega_{1},d\omega_{2})\cdots\int_{\Omega_{n}}I_{B^{n}}(\omega_{1},\cdots\omega_{n})P(\omega_{1},\cdots,d\omega_{n}).
$$
 

由于 $I_{B^{n+1}}(\omega_{1},\cdots,\omega_{n+1})\leqslant I_{B^{n}}(\omega_{1},\cdots,\omega_{n})$，故对给定 $\omega_{1},g_{n}^{(1)}(\omega_{1})$单调下降趋于某极限 $h_{1}(\omega_{1})$。由控制收敛定理，我们有

 
$$
\int_{\Omega_{1}}h_{1}(\omega_{1})\mathbb{P}_{1}(d\omega_{1})=\lim_{n\to\infty}\mathbb{P}(A_{n})>0.
$$
 

于是存在 $\omega_{1}^{\prime}\in\Omega_{1}$，使 $h_{1}(\omega_{1}^{\prime})>0$。实际上，必有 $\omega_{1}^{\prime}\in B^{1}$。否则，对一切n>1有 $I_{B^{n}}(\omega_{1}^{\prime},\omega_{1},\cdots,\omega_{n})=0$，从而 $g_{n}^{(1)}(\omega_{1}^{\prime})=0$，这导致 $h_{1}(\omega_{1}^{\prime})=0$。

---

现设n>2，则

 
$$
g_{n}^{(1)}(\omega_{1}^{\prime})=\int g_{n}^{(2)}(\omega_{2})P(\omega_{1}^{\prime},d\omega_{2}),
$$
 

其中

 
$$
\begin{align*}g_{n}^{(2)}(\omega_{2})=\int_{\Omega_{3}}P(\omega_{1}^{\prime},\omega_{2},d\omega_{3})\cdots\int_{\Omega_{n}}I_{B^{n}}(\omega_{1}^{\prime},\omega_{2},\cdots,\omega_{n}).\\P(\omega_{1}^{\prime},\omega_{2},\cdots,\omega_{n-1},d\omega_{n}).\end{align*}
$$
 

如上所证，可知 $g_{n}^{(2)}(\omega_{2})\downarrow h_{2}(\omega_{2})$。由于 $g_{n}^{(1)}(\omega_{1}^{\prime})\rightarrow h_{1}(\omega_{1}^{\prime})>0$，故存在 $\omega_{2}^{\prime}\in\Omega_{2}$，使 $h_{2}(\omega_{2}^{\prime})>0$。如上所证，可知 $(\omega_{1}^{\prime},\omega_{2}^{\prime})\in B^{2}$。

最后，由归纳法可得到一点列 $\{\omega_1', \omega_2', \cdots\}$，使得 $\omega_j' \in \Omega_j$且 $(\omega_1', \cdots, \omega_n') \in B^n$。因此，最终有 $(\omega_1', \omega_2', \cdots) \in \bigcap_{n=1}^{\infty} A_n = \varnothing$，这导致矛盾。这样一来，我们证明了IP为代数Z上的概率测度。由测度扩张定理知，它可唯一地扩张成为 $\mathcal{F} = \sigma(\mathcal{Z})$上的概率测度。

系4.4.2 (Kolmogorov定理) 设 $(\Omega_{j},\mathcal{F}_{j},\mathbb{P}_{j})$为一列概率空间，令 $\Omega=\prod_{j=1}^{\infty}\Omega_{j}$， $\mathcal{F}=\prod_{j=1}^{\infty}\mathcal{F}_{j}$，则存在 $(\Omega,\mathcal{F})$上的唯一概率测度 $P$，使得对一切 $n\geq1$，对一切 $A_{j}\in\mathcal{F}_{j},1\leq j\leq n$，有

$$
\mathbb{P}(\prod_{j=1}^{n}A_{j}\times\prod_{j=n+1}^{\infty}\Omega_{j})=\prod_{j=1}^{n}\mathbb{P}_{j}(A_{j}).   \tag*{(4.4.2)}
$$

##### 习题

4.4.1 设 $\{(\Omega_i, \mathcal{F}_i, \mathbb{P}_i), i \in I\}$为一族概率空间，令 $\mathcal{P}_0(I)$表示 $I$的非空有限子集全体，则在 $\left(\prod_{i \in I} \Omega_i, \prod_{i \in I} \mathcal{F}_i\right)$上存在唯一的概率测度 $P$，使得对任何 $S \in \mathcal{P}_0(I)$，有

 
$$
\mathbb{P}(\prod_{i\in S}A_{i}\times\prod_{i\in I\setminus S}\Omega_{i})=\prod_{i\in S}\mathbb{P}_{i}(A_{i}),~A_{i}\in\mathcal{F}_{i},i\in S.
$$
 

(提示: 利用定理4.1.4(3).)

4.4.2 试将定理4.4.1推广到任意无穷多个可测空间乘积情形.

### 4.5 Kolmogorov相容性定理及Tulcea定理的推广

本节将给出Kolmogorov相容性定理及Tulcea定理的一个推广形式,为此我们先引入紧类概念,它是Hausdorff空间中的紧集类概念的抽象化.

定义4.5.1 设C为E上一集类. 如果下列条件满足:

 
$$
\{C_{n},n\geqslant1\}\subset\mathcal{C},\bigcap_{n=1}^{\infty}C_{n}=\varnothing\Rightarrow 对某个 m,\bigcap_{n=1}^{m}C_{n}=\varnothing,
$$
 

---

则称C为紧类.

引理4.5.2 设C为E上的紧类，则 $C_{Uf}$及 $C_{\delta}$都是紧类。这里 $C_{Uf}$及 $C_{\delta}$分别表示用有限并及可列交运算封闭C所得的集类。

证  $\mathcal{C}_{\delta}$ 显然是紧类，只需证  $\mathcal{C}_{\cup f}$ 是紧类. 设  $D_{n} = \bigcup_{m=1}^{M_{n}} C_{n}^{m} \in \mathcal{C}_{\cup f}, n \geq 1$，使得对一切  $p \geq 1, \bigcap_{n \leq p} D_{n} \neq \varnothing$. 令 J 表示那些对每个 n 满足  $1 \leq m_{n} \leq M_{n}$ 的自然数序列  $\{m_{1}, m_{2}, \cdots\}$ 全体. 令

 
$$
J_{p}=\big\{\{m_{n},n\geqslant1\}\in J\mid\bigcap_{n\leqslant p}C_{n}^{m_{n}}\neq\varnothing\big\}.
$$
 

由于

 
$$
\bigcap_{n\leqslant p}D_{n}=\bigcap_{n\leqslant p}\bigcup_{m=1}^{M_{n}}C_{n}^{m}=\bigcup_{\{m_{n}\}\in J}\big(\bigcap_{n\leqslant p}C_{n}^{m_{n}}\big),
$$
 

于是对每个$p \geqslant 1$，$J_p$非空。显然有$J_p \supset J_{p+1}, p \geqslant 1$。往证$\bigcap_p J_p \neq \varnothing$。对每个$n \geqslant 1$，任取$J_q$中元素$\{m_n^{(q)}, n \geqslant 1\}$。由于对固定的$n, 1 \leqslant m_n^{(q)} \leqslant M_n$对一切$q$成立，从而对任一由无穷多个自然数组成的集合$\Lambda$，必有无穷多个$q$属于$\Lambda$，使得$m_n^{(q)}$取相同值。因此，由归纳法可构造一序列$\{m_n^*, n \geqslant 1\}$，使得它属于$J$，且对一切$p \geqslant 1$，及$1 \leqslant n \leqslant p$，$m_n^* = m_n^{(q)}$对无穷多个$q$成立。故对任意$p \geqslant 1$，存在$q > p$，使$m_n^* = m_n^{(q)}, 1 \leqslant n \leqslant p$。由于$\{m_n^*, n \geqslant 1\} \in J_q \subset J_p$，故由$J_p$的定义知$\{m_n^*, n \geqslant 1\} \in J_p$，于是$\{m_n^*, n \geqslant 1\} \in \bigcap_p J_p$。从而对一切$p$，$\bigcap_{n \leqslant p} C_n^{m_n^*} \neq \varnothing$。但依假定，$\mathcal{C}$为紧类，故$\bigcap_{n=1}^{\infty} C_n^{m_n^*} \neq \varnothing$，从而$\bigcap_n D_n \neq \varnothing$（注意：$\bigcap_{n} D_n \supset \bigcap_{n} D_n^{m_n^*}$）。这表明$\mathcal{C}_{\cup f}$为紧类。

引理4.5.3 设A及A₁为E上的半代数, A₁ ⊃ A, C为E上一紧类, 且C ⊂ A₁. 令μ为A₁上的一非负有限可加集函数, 且μ(E) < ∞. 若对一切A ∈ A, 有

 
$$
\mu(A)=\sup\{\mu(C)\mid C\subset A,\;C\in\mathcal{C}\},
$$
 

则 $\mu$限于A为 $\sigma$可加的.

证 首先假定A及A₁为E上的代数．由定理1.3.4知：为了证μ在A上为σ可加，只需证μ在空集σ处连续．设Aₙ ∈ A, Aₙ ↓ ∅．给定ε > 0，依假定，对每个n，存在Cₙ ⊂ Aₙ, Cₙ ∈ C，使μ(Aₙ) ≤ μ(Cₙ) + ε/2ᵗ．由于∩ₙCₙ ⊂ ∩ₙAₙ = ∅，故由C是紧类的假定，存在正整数m，使∩ₙₐ₁ = ∅，即有∪ₙₐ₁ = ∅，于是有

 
$$
A_{m}=\bigcap_{n=1}^{m}A_{n}=\big(\bigcap_{n=1}^{m}A_{n}\big)\cap\big(\bigcup_{n=1}^{m}C_{n}^{c}\big)\subset\bigcup_{n=1}^{m}(A_{n}\setminus C_{n}).
$$
 

---

因此，对 $k \geqslant m$，我们有

 
$$
\mu(A_{k})\leqslant\mu(A_{m})\leqslant\sum_{n=1}^{m}\mu(A_{n}\setminus C_{n})<\varepsilon.
$$
 

这表明  $\lim_{k\to\infty}\mu(A_{k})<\varepsilon$ 。但  $\varepsilon>0$ 是任意的，故  $\lim_{k\to\infty}\mu(A_{n})=0$ 。因此， $\mu$ 限于 A 为  $\sigma$ 可加的。

现设A及 $A_1$为E上的半代数。令 $\overline{A}_1$及 $\overline{A}$为分别由 $A_1$及 $A_2$产生的代数，则 $\mu$可以唯一地扩张成为 $\overline{A}_1$上的有限可加集函数，且对一切 $A \in \overline{A}$，有

 
$$
\mu(A)=\sup\{\mu(C)\mid C\subset A,\;C\in\mathcal{C}_{\cup f}\}.
$$
 

但由引理4.5.2知， $C_{\cup f}$ 为紧类，故由已证结果知： $\mu$ 限于  $\overline{A}$ 为  $\sigma$ 可加的．特别， $\mu$ 限于  $A$ 为  $\sigma$ 可加的．

定义4.5.4 设 $(E, \mathcal{E}, \mu)$为一测度空间。称 $\mu$为 $\mathcal{E}$上的紧测度，如果存在紧类 $\mathcal{C} \subset \mathcal{E}$，使得对一切 $A \in \mathcal{E}$，有

 
$$
\mu(A)=\sup\{\mu(C):C\subset A,C\in\mathcal{C}\}.
$$
 

下一定理是经典的Kolmogorov相容性定理的推广形式.

定理4.5.5 设$I$为一无穷集，$\mathcal{P}_0(I)$为$I$的非空有限子集全体。设$(\Omega_i, \mathcal{F}_i)_{i \in I}$为一族可测空间。对每个$T \in \mathcal{P}_0(I)$，设$I\mathcal{P}_T$为$(\prod_{i \in T} \Omega_i, \prod_{i \in T} \mathcal{F}_i)$上的一概率测度。假定：(1)每个$I\mathcal{P}_i$为$(\Omega_i, \mathcal{F}_i)$上的紧概率测度；(2)$\{P_T, T \in \mathcal{P}_0(I)\}$满足如下相容性条件：对$T_1 \subset T_2$，有

$$
\mathbb{P}_{T_{1}}(A_{T_{1}})=\mathbb{P}_{T_{2}}\Big(A_{T_{1}}\times\prod_{i\in T_{2}\backslash T_{1}}\Omega_{i}\Big),\quad A_{T_{1}}\in\prod_{i\in T_{1}}\mathcal{F}_{i},   \tag*{(4.5.1)}
$$

则在 $\left(\prod_{i\in JU}\Omega_{i},\prod_{i\in I}\mathcal{F}_{i}\right)$上存在唯一概率测度 $P$，使得 $\forall T\in\mathcal{P}_{0}(I)$，有

$$
\mathbb{P}\Big(A_{T}\times\prod_{i\in I\backslash T}\Omega_{i}\Big)=\mathbb{P}_{T}(A_{T}),\ A_{T}\in\prod_{i\in T}\mathcal{F}_{i}.   \tag*{(4.5.2)}
$$

证令

 
$$
\mathcal{S}=\bigcup_{T\in\mathcal{P}_{0}(I)}\Big\{\prod_{i\in T}A_{i}\times\prod_{i\notin T}\Omega_{i}\mid A_{i}\in\mathcal{F}_{i},i\in T\Big\},
$$
 

则S为半代数，且 $\sigma(S)=\prod_{i\in I}F_i$。令

 
$$
\mathbb{P}\Big(\prod_{i\in T}A_{i}\times\prod_{i\notin T}\Omega_{i}\Big)=\mathbb{P}_{T}\Big(\prod_{i\in T}A_{i}\Big),
$$
 

---

由$\{P_T, T \in \mathcal{P}_0\}$的相容性知，如上定义的$P$在$\mathcal{S}$上唯一确定，有限可加，且有$P(\prod_{i \in I} \Omega_i)$

= 1. 因此，由引理4.5.3，为证$P$在$\mathcal{S}$上$\sigma$可加，只需证存在一紧类$\mathcal{C} \subset \mathcal{S}$，使得对一切$A \in \mathcal{S}$，有

$$
\mathbb{P}(A)=\sup\{\mathbb{P}(C)\mid C\subset A,C\in\mathcal{C}\}.   \tag*{(4.5.3)}
$$

依假定，对每个 $i \in I$，存在 $\Omega_i$上一紧类 $\mathcal{C}_i \subset \mathcal{F}_i$，使得对一切 $A_i \in \mathcal{F}_i$，有 $\mathbb{P}_i(A_i) = \sup\{\mathbb{P}_i(C) \mid C \subset A_i, C \in C_i\}$。不妨设每个 $\mathcal{C}_i$对可列交运算封闭。令

 
$$
\mathcal{D}=\big\{C\times\prod_{j\neq i}\Omega_{j},C\in\mathcal{C}_{i},i\in I\big\},
$$
 

则D为紧类. 事实上, 设 $A_n = C_n \times \prod_{j \neq i_n} \Omega_j$,  $C_n \in \mathcal{C}_n$, 则 $\bigcap_n A_n$有如下形式:  $\prod_{i \in S} B_i \times \prod_{i \notin S} \Omega_i$, 其中S为可数集, 且 $B_i \in C_i$,  $i \in S$. 若 $\bigcap_n A_n = \varnothing$, 则存在 $s \in S$, 使 $B_s = \varnothing$. 由于 $B_s = \bigcap_{i_n = s} C_n$, 故由 $\mathcal{C}_s$的紧性知, 存在 $\{n \mid i_n = s\}$的有限子集J, 使 $\bigcap_n C_n = \varnothing$, 从而 $\bigcap_{n \in J} A_n = \varnothing$. 因此, D为紧类. 现令 $\mathcal{C} = \mathcal{D}_{\cap f}$, 则 $\mathcal{C}$为紧类, 且 $\mathcal{C} \subset \mathcal{S}$. 设 $A = \prod_{i \in T} A_i \times \prod_{i \in T} \Omega_i \in \mathcal{S}$. 对任给 $\varepsilon > 0$, 取 $C_i \in \mathcal{C}_i$,  $C_i \subset A_i$, 使得

 
$$
\mathbb{P}_{i}(A_{i})\leqslant\mathbb{P}_{i}(C_{i})=\frac{\varepsilon}{|T|},
$$
 

这里 $|T|$表示T中元素的个数. 令

 
$$
C=\prod_{i\in T}C_{i}\times\prod_{i\notin T}\Omega_{i}=\bigcap_{i\in T}\left(C_{i}\times\prod_{j\neq i}\Omega_{j}\right)\in\mathcal{C},
$$
 

则 $C\subset A$，且有 $A\setminus C\subset\bigcup_{i\in T}\{(A_{i}\setminus C_{i})\times\prod_{j\neq i}\Omega_{i}\}$。故由IP的半有限可加性得

 
$$
\mathbb{P}(A)-\mathbb{P}(C)\leqslant\sum_{i\in T}\mathbb{P}_{i}(A_{i}\setminus C_{i})\leqslant\varepsilon.
$$
 

由于$\varepsilon > 0$是任意的，故有$(4.5.3)$式。因此，$P$在$S$上是$\sigma$可加的，从而可唯一地扩张成为$\sigma(\mathcal{S}) = \prod_{i \in I} \mathcal{F}_i$上的一概率测度，仍记为$P$。显然$P$满足$(4.5.2)$式（利用单调类定理）。$P$的唯一性显然。

在随机过程理论中，有时遇到如下的概率测度的扩张问题：设 $(\Omega,\mathcal{F})$为一可测空间， $(\mathcal{F}_n)$为 $\mathcal{F}$的一列上升的子 $\sigma$代数，使得 $\sigma(\bigcup_{n}\mathcal{F}_n)=\mathcal{F}$。令 $P_n$为 $\mathcal{F}_n$上的概率，使得 $P_{n+1}$限于 $\mathcal{F}_n$与 $P_n$一致。是否存在 $\mathcal{F}$上的唯一概率测度 $\mathbb{P}$，使得 $\mathbb{P}$限于每个 $\mathcal{F}_n$与 $\mathbb{P}_n$一致？

下一定理回答了这一问题, 它推广了 Tulcea 定理(定理 4.4.1).

---

定理4.5.6 设$(\Omega,\mathcal{F})$为一可测空间，$(\mathcal{F}_{n},n\geq1)$为$\mathcal{F}$的一列上升子$\sigma$代数，使得$\sigma(\bigcup\mathcal{F}_{n})=\mathcal{F}$。令$\mathbb{P}_{n}$为$\mathcal{F}_{n}$上的概率测度，$n\geq1$。如果对一切$n\geq2$，存在$(\Omega,\mathcal{F}_{n-1})$到$(\Omega,\mathcal{F}_{n})$的概率核（见定义4.3.1）$Q_{n}(\omega,\cdot)$，使得

$$
\mathbb{P}_{n}(B_{n})=\int Q_{n}(\omega,B_{n})\mathbb{P}_{n-1}(d\omega),\forall B_{n}\in\mathcal{F}_{n},   \tag*{(4.5.4)}
$$

$$
G\in\mathcal{F}_{n},Q_{n}(\omega,G)>0\Rightarrow A_{n-1}(\omega)\cap G\neq\varnothing\;,   \tag*{(4.5.5)}
$$

这里 $A_{k}(\omega)$表示包含 $\omega$的 $F_{k}$原子，则对一切 $n\geq1$， $P_{n+1}$限于 $F_{n}$与 $P_{n}$一致。如果进一步有

$$
\{\omega^{(n)},n\geqslant1\}\subset\Omega,\;A_{n}(\omega^{(n)})\downarrow\Rightarrow\bigcap_{n}A_{n}(\omega^{(n)})\neq\varnothing,   \tag*{(4.5.6)}
$$

则存在F上的唯一概率测度P，使得P限于每个 $F_{n}$与 $P_{n}$一致.

证 容易由(4.5.5)式推知，对 $n \geqslant 2, B \in \mathcal{F}_{n-1}$，有 $Q_n(\omega, B) = I_B(\omega)$。由此再由(4.5.4)式推知，对一切 $n \geqslant 1$， $P_{n+1}$限于 $\mathcal{F}_n$与 $P_n$一致。于是若令 $\mathcal{A} = \bigcup \mathcal{F}_n$，则 $(\mathbb{P}_n, n \geqslant 1)$在代数 $\mathcal{A}$上唯一确定一可加集函数 $P$，使得 $P$限于每个 $\mathcal{F}_n$与 $P_n$一致。

现在假定条件(4.5.5)和(4.5.6)成立.为证IP在A上是σ可加的,只需证IP在空集处连续.设 $B_{n}\in\mathcal{A},B_{n}\downarrow\varnothing$,我们用反证法证明 $\lim_{n\to\infty}IP(B_{n})=0$.假定 $\lim_{n\to\infty}IP(B_{n})>0$.不妨设对每个 $n\geq1$,有 $B_{n}\in\mathcal{F}_{n}$(否则,可以在序列 $\{B_{n},n\geq1\}$中添加某些相同的 $B_{n}$,使新序列具有这一性质).由(4.5.4)式知,对每个 $n\geq2$,

 
$$
\mathbb{P}(B_{n})=\int_{\Omega}q_{n}^{(1)}(\omega)\mathbb{P}_{1}(d\omega),
$$
 

其中 $q_{2}^{(1)}(\omega)=Q_{2}(\omega,B_{2}),$

 
$$
q_{n}^{(1)}(\omega)=\int_{\Omega}Q_{2}(\omega,d\omega^{(2)})\cdots Q_{n}(\omega^{(n-1)},B_{n}),\;n\geqslant3.
$$
 

由于 $B_{n}\downarrow,\quad g q_{n}^{(1)}(\omega)\downarrow h_{1}(\omega).$由控制收敛定理，我们有

 
$$
\int_{\Omega}h_{1}(\omega)\mathbb{P}_{1}(d\omega)=\lim_{n\to\infty}\mathbb{P}(B_{n})>0,
$$
 

于是存在 $\omega^{(1)}$，使 $h_{1}(\omega^{(1)})>0$。实际上，必有 $\omega^{(1)}\in B_{1}$，因为不然的话，由(4.5.5)式知

 
$$
q_{2}^{(1)}(\omega^{(1)})=Q_{2}(\omega^{(1)},B_{2})\leqslant Q_{2}(\omega^{(1)},B_{1})=0,
$$
 

这将导致 $h_{1}(\omega^{(1)})=0.$

现设n>2，则

 
$$
q_{n}^{(1)}(\omega^{(1)})=\int_{\Omega}q_{n}^{(2)}(\omega)Q_{2}(\omega^{(1)},d\omega),
$$
 

---

其中 $q_{3}^{(2)}(\omega)=Q_{3}(\omega,B_{3}),$

 
$$
q_{n}^{(2)}(\omega)=\int_{\Omega}Q_{3}(\omega,d\omega^{(3)})\cdots Q_{n}(\omega^{(n-1)},B_{n}),\;n\geqslant4.
$$
 

于是 $q_{n}^{(2)}(\omega)\downarrow h_{2}(\omega)$，且

 
$$
\int_{\Omega}h_{2}(\omega)Q_{2}(\omega^{(1)},d\omega)=h_{1}(\omega^{(1)})>0.
$$
 

因此， $Q_{2}(\omega^{(1)}, [h_{2} > 0]) > 0$。从而由(4.5.5)式知，存在 $\omega^{(2)}$，使 $\omega^{(2)} \in A_{1}(\omega^{(1)})$，且 $h_{2}(\omega^{(2)}) > 0$。与上述同理可证 $\omega^{(2)} \in B_{2}$。

由归纳法得Ω中一列点 $\omega^{(1)},\omega^{(2)},\cdots$，使得 $\omega^{(n)}\in B_{n},\omega^{(n+1)}\in A_{n}(\omega^{(n)}),n\geqslant1$。由于 $\mathcal{F}_{n}\downarrow$，故易知 $A_{n+1}(\omega^{(n+1)})\subset A_{n}(\omega^{(n)})$。因此，由条件(3)知 $\bigcap_{n}\left(A_{n}(\omega^{(n)})\neq\varnothing.\right.$但显然有 $A_{n}(\omega^{(n)})\subset B_{n}$，故 $\bigcap_{n}B_{n}\neq\varnothing$。这与假定矛盾。这表明，必须有 $\lim_{n\to\infty}P(B_{n})=0$，因此， $\mathbb{P}$在 $\mathcal{A}$上是 $\sigma$可加的，从而 $\mathbb{P}$可以唯一扩张成为 $\mathcal{F}$上的一概率测度。

##### 习题

4.5.1 为什么说定理4.5.6是Tulcea定理的推广形式？

### 4.6 概率测度序列的投影极限

定义4.6.1 设 $(\Omega_{j},\mathcal{F}_{j}),j=1,2,\cdots$为一列可测空间，且对 $j>k,p_{k}^{j}$为 $\Omega_{j}$到 $\Omega_{k}$上的可测满射，使得对 $j>k>l$有 $p_{l}^{k}\circ p_{k}^{j}=p_{l}^{j}$，则称 $(\Omega_{j},\mathcal{F}_{j}),p_{k}^{j}$为一投影序列。设 $\Omega=\prod_{j=1}^{\infty}\Omega_{j},\mathcal{F}=\prod_{j=1}^{\infty}\mathcal{F}_{j}$，令

$$
E=\left\{\left(\omega_{j}\right)\in\Omega\mid p_{k}^{j}(\omega_{j})=\omega_{k},\forall j>k\right\},\ \mathcal{E}=\mathcal{F}\cap E,   \tag*{(4.6.1)}
$$

称 $(E,\mathcal{E})$为投影可测空间.

引理4.6.2 设 $\left(\left(\Omega_{j},\mathcal{F}_{j}\right),p_{k}^{j}\right)$为一投影序列， $(E,\mathcal{E})$为相应的投影可测空间. 令 $\pi_{j}$为从 $\Omega$到 $\Omega_{j}$上的投影映射， $p_{j}$为 $\pi_{j}$到E上的局限，令

$$
\mathcal{G}=\bigcup_{j=1}^{\infty}p_{j}^{-1}(\mathcal{F}_{j}),   \tag*{(4.6.2)}
$$

则 $\mathcal{G}$为E上的代数，且 $\sigma(\mathcal{G})=\mathcal{E}$

证 首先由(4.6.1)式知，$p_j$为$E$到$\Omega_j$上的满射．事实上对任何给定的$\omega_j \in \Omega_j$，对 $n < j$，令 $\omega_n = p_n^j \omega_j$；对 $m \geq j$，依次选取 $\omega_{m+1} \in \Omega_{m+1}$，使得 $\omega_m = p_m^{m+1} \omega_{m+1}$，则 $\omega = (\omega_k) \in E$，且 $p_j(\omega) = \omega_j$．再由(4.6.1)式知，对 $j > k$，$p_k = p_k^j \circ p_j$，从而

---

有 $p_{k}^{-1}(\mathcal{F}_{k})=p_{j}^{-1}(p_{k}^{j})^{-1}(\mathcal{F}_{k})\subset p_{j}^{-1}(\mathcal{F}_{j})$。这表明 $\sigma$代数序列 $p_{j}^{-1}(\mathcal{F}_{j})$单调增，故 $\mathcal{G}$为代数。此外我们有

 
$$
\begin{align*}\sigma(\mathcal{G})&=\sigma\Big(\bigcup_{j=1}^{\infty}p_{j}^{-1}(\mathcal{F}_{j})\Big)=\sigma\Big(\bigcup_{j=1}^{\infty}(\pi_{j}^{-1}(\mathcal{F}_{j})\cap E)\Big)\\&=\sigma\Big(\big(\bigcup_{j=1}^{\infty}\pi_{j}^{-1}(\mathcal{F}_{j})\big)\cap E\Big)=\sigma\big(\bigcup_{j=1}^{\infty}\pi_{j}^{-1}(\mathcal{F}_{j})\big)\cap E=\mathcal{F}\cap E=\mathcal{E}.\end{align*}
$$
 

如果对每个$j \geq 1$, $P_j$为$(\Omega_j, \mathcal{F}_j)$上的一概率测度, 且满足如下相容性条件:$P_k = P_j(p_k^j)^{-1}$, $\forall j > k$, 则通过映射 $p_j$可在$p_j^{-1}(\mathcal{F}_j)$上定义测度$\mathcal{Q}_j: \mathcal{Q}_j(p_j^{-1}(A)) = \mathcal{P}_j(A)$, $A \in \mathcal{F}_j$. 对 $j > k$, $\mathcal{Q}_j$限于$p_k^{-1}(\mathcal{F}_k)$显然与$\mathcal{Q}_k$一致, 因此我们在$\mathcal{G}$上得到了一个有限可加的非负集函数, 记为$\mathcal{Q}$. 如果 $\mathcal{Q}$可唯一扩张成$\mathcal{E}$上的一个概率测度 (即$\mathcal{Q}$在$\mathcal{G}$上是可列可加的), 则有$P_j = \mathcal{Q} \circ p_j^{-1}$, $\forall j \geq 1$. 这时称 $\mathcal{Q}$是$\mathcal{Q}_j$的投影极限.

一个自然的问题是: 在什么条件下Q可唯一扩张成E的一个概率测度?下面我们利用Kolmogorov相容性定理给出一个答案.

定理4.6.3 设$ \left(\left(\Omega_{j},\mathcal{F}_{j}\right),p_{k}^{j}\right) $为一投影序列， $\left(E,\mathcal{E}\right)$为相应的投影可测空间， $p_{j}$为 $\Omega$到 $\Omega_{j}$上的投影映射 $\pi_{j}$在 $E$上的局限。如果对每个 $j\geq1$， $\mathbb{P}_{j}$为 $\left(\Omega_{j},\mathcal{F}_{j}\right)$上的一紧概率测度，且满足如下相容性条件： $\mathbb{P}_{k}=\mathbb{P}_{j}(p_{k}^{j})^{-1},\forall j>k$，则存在 $\left(E,\mathcal{E}\right)$上的唯一概率测度 $\mathbb{Q}$，使得 $\mathbb{P}_{j}=\mathbb{Q}\circ p_{j}^{-1},\forall j\geq1$。

证令

 
$$
E_{n}=\prod_{j=1}^{n}\Omega_{j},\ \mathcal{E}_{n}=\prod_{j=1}^{n}\mathcal{F}_{j},\ n\geqslant1.
$$
 

定义 $(\Omega_{n},\mathcal{F}_{n})$到 $(E_{n},\mathcal{E}_{n})$的可测映射 $f_{n}$:

 
$$
f_{n}(\omega_{n})=(p_{1}^{n}(\omega_{n}),p_{2}^{n}(\omega_{n}),\cdots,p_{n-1}^{n}(\omega_{n}),\omega_{n}).
$$
 

令 $\mu_{n}=\mathbb{P}_{n}\circ f_{n}^{-1},n\geqslant1$，则 $\mu_{n}$为 $(E_{n},\mathcal{E}_{n})$上的概率测度，且 $\forall A_{n}\in\mathcal{E}_{n}$，有

 
$$
\begin{align*}\mu_{n+1}(A_{n}\times\Omega_{n+1})&=\mathbb{P}_{n+1}(f_{n+1}^{-1}(A_{n}\times\Omega_{n+1}))\\&=\mathbb{P}_{n+1}\circ(p_{n}^{n+1})^{-1}(f_{n}^{-1}(A_{n}))=\mathbb{P}_{n}\circ f_{n}^{-1}(A_{n})=\mu_{n}(A_{n}).\end{align*}
$$
 

于是由定理4.5.5知存在 $(\Omega,\mathcal{F})=(\prod_{j=1}^{\infty}\Omega_{j},\prod_{j=1}^{\infty}\mathcal{F}_{j})$上的唯一概率测度 $\mu$，使得 $\mathbb{P}_{j}=\mu\circ\pi_{j}^{-1},\forall j\geq1$。由 $f_{n}$及 $\mu_{n}$的定义容易推知，集合 $E$关于 $\mu$的外测度为1，又由于 $\mathcal{E}=\mathcal{F}\cap E$，故由习题1.4.1知，若令 $Q$为 $\mu$到 $(E,\mathcal{E})$上的限制，则 $Q$是 $(E,\mathcal{E})$上的唯一概率测度，使得 $P_{j}=Q\circ p_{j}^{-1},\forall j\geq1$。

---

### 4.7 随机Daniell 积分及其核表示

本节将引进随机Daniell积分, 给出Daniell-Stone定理的随机版本和随机Daniell积分的核表示. 本节内容取自严加安(1991).

定义4.7.1 设 $(\Omega,\mathcal{F})$为一可测空间， $\mathcal{P}$为其上的一族概率测度.令

$$
\mathcal{N}=\{A\in\mathcal{F}\mid\mathbb{I}P(A)=0,\;\forall\mathbb{P}\in\mathcal{P}\},   \tag*{(4.7.1)}
$$

我们指定N为F中“可略集”全体，称三元体( $\Omega, \mathcal{F}, \mathcal{N}$)为一(由P确定的)随机空间。一依赖 $\omega \in \Omega$的性质称为N-a.e.成立，如果除去某个可略集外它处处成立。

下面用 $L(\Omega,\mathcal{F})$（相应地， $\overline{L}(\Omega,\mathcal{F})$）表示 $\Omega$上实值（数值）函数全体.

定义4.7.2 设E为一抽象集合，A为E上的一代数， $\mu$为一从A到 $\overline{L}_{+}(\Omega,\mathcal{F})$中的映射，满足如下条件：

(1)  $\mu(\varnothing) = 0, \mathcal{N}\text{-a.e.};$

(2) 如果 $(A_n) \subset \mathcal{A}, A_n \cap A_m = \varnothing, \forall n \neq m$，则 $\mu(\sum_{n=1}^{\infty} A_n) = \sum_{n=1}^{\infty} \mu(A_n), \mathcal{N}$ a.e.,

则称 $\mu$为一N随机测度. 如果P只有单个元素P, 则称N随机测度为IP随机测度.

有限随机测度和 $\sigma$有限随机测度概念是不讲自明的.

定义4.7.3 设 $(E,\mathcal{E})$为一可测空间， $\mu$为 $\mathcal{E}$上一 $\mathcal{N}$随机测度， $f$为 $E$上一非负 $\mathcal{E}$可测函数.令

 
$$
\mu(f)=\lim_{n\to\infty}\frac{1}{2^{n}}\sum_{k=0}^{\infty}\mu\Big(\big[f>\frac{k}{2^{n}}\big]\Big),
$$
 

称 $\mu(f)$为f关于 $\mu$的积分. 对一般f, 可令 $\mu(f)=\mu(f^{+})-\mu(f^{-})$.

定义4.7.4 设H为E上一向量格，T为H到 $L(\Omega,\mathcal{F})$中的映射。称T为H上的N随机Daniell积分，如果T是N-a.e.线性、保正、在0处从上连续，即T满足如下条件：

(1)  $T(\alpha f + \beta g) = \alpha T(f) + \beta T(g)$,  $\mathcal{N}$-a.e.,  $\forall f, g \in \mathcal{H}, \alpha, \beta \in \mathbb{R}$;

(2)  $f \geqslant 0, f \in \mathcal{H} \Longrightarrow T(f) \geqslant 0, \mathcal{N} - a.e.;$

(3)  $f_n \in \mathcal{H}, f_n \downarrow 0 \Longrightarrow T(f_n) \to 0, \mathcal{N} \text{-a.e.}$

下一定理是Carathéodory测度扩张定理(定理1.4.7)的随机版本.

定理4.7.5 设 $(\Omega,\mathcal{F},\mathcal{N})$为一随机空间， $\mathcal{A}$为E上的一代数， $\mu$为 $\mathcal{A}$上的一 $\sigma$有限 $\mathcal{N}$随机测度，则 $\mu$可以唯一地(在 $\mathcal{N}$等价意义下)扩张成为 $\sigma(\mathcal{A})$上的 $\mathcal{N}$-随机测度.

证 与引理1.3.5类似, 我们可以把与σ有限N随机测度有关的问题化为有限N随机测度情形来处理, 因此不妨假定μ为A上的一有限N随机测度. 由于N由(4.7.1)式给出, 对每个$\mathbb{P}\in\mathcal{P}$, μ为A上的一有限$\mathbb{P}$随机测度. 这时容易证明μ可以唯一地扩张成为σ(A)上的$\mathbb{P}$随机测度(习题4.7.1), 记为μ$\mathbb{P}$. 令$\mathcal{X}$为E上那些包含A但含于σ(A)的代数A'全体, 使得限于$A'\{\mu_{\mathbb{P}}, \mathbb{P}\in\mathcal{P}\}$有一个统一的版本. 我们在$\mathcal{X}$上按集合的包

---

含关系定义一个半序. 如果 $\{A_\alpha, \alpha \in \Lambda\}$是$\mathcal{X}$的一个全序子集, 令$\overline{\mathcal{A}} = \cup_{\alpha \in \Lambda} A_\alpha$, 则易知 $\overline{\mathcal{A}} \in \mathcal{X}$. 于是由集合论中著名的 Zorn 引理知, $\mathcal{X}$有一极大元$\widetilde{\mathcal{A}}$. 往证 $\widetilde{\mathcal{A}} = \sigma(\mathcal{A})$. 事实上, 如果 $\widetilde{\mathcal{A}} \neq \sigma(\mathcal{A})$, 则 $\widetilde{\mathcal{A}}$不是$\sigma$代数, 因为$\sigma(\mathcal{A})$是包含$\mathcal{A}$的最小$\sigma$代数. 令$\mathcal{B} = \{A \cap B^c | A, B \in \widetilde{\mathcal{A}}_b\}, \mathcal{A}' = \mathcal{B}_{\Sigma f}$, 则 $\mathcal{A}'$为$E$上的一代数, 且$\widetilde{\mathcal{A}} \neq \mathcal{A}'$, 因为如果相等就可证明 $\widetilde{\mathcal{A}}$是一$\sigma$代数. 对每个$B \in \widetilde{\mathcal{A}}_b$, 我们选取一个序列 $(B_n) \subset \mathcal{A}$, 使得 $B_n \downarrow B$, 且令

 
$$
\overline{\mu}(B)=\limsup_{n\to\infty}\mu(B_{n}).
$$
 

则容易看出 $\overline{\mu}(B)$可以扩张成为 $\{\mu_P, \mathbb{P} \in \mathcal{P}\}$在 $\mathcal{A}'$上的一个统一版本．这表明 $\mathcal{A}' \in \mathcal{X}$．这与 $\tilde{\mathcal{A}}$是极大元矛盾．

下一定理是Daniell-Stone 定理的随机版本.

定理4.7.6 令 $(\Omega, \mathcal{F}, \mathcal{N})$为一随机空间，其中 $N$如(4.7.1)式给出， $\mathcal{H}$为 $E$上的一同量格。假定存在 $\mathcal{H}_+$中一处处单调上升于1的序列，则对 $\mathcal{H}$上的任一 $\mathcal{N}$随机Daniell积分 $T$，存在 $\sigma(\mathcal{H})$上的一 $\mathcal{N}$随机测度 $\mu$，使得 $\mu(f) = T(f)$， $\mathcal{N}$-a.e.,  $\forall f \in \mathcal{H}$。

证 对每个固定的$IP \in \mathcal{P}$, $T$可视为$\mathcal{H}$上的$IP$随机Daniell积分. 在Daniell-Stone定理的证明中用将在第7章定义7.5.1给出的ess.inf和ess.sup代替inf和sup, 可以证明: 存在$\sigma(\mathcal{H})$上的一$IP$随机测度$\mu_P$, 使得$\mu_P(f) = T(f)$, $P$-a.e., $\forall f \in \mathcal{H}$. 因此, 由定理4.7.5知, 为了证明定理的结论, 只要证明存在生成$\sigma(\mathcal{H})$的一代数$\mathcal{A}$使得$\{\mu_P, P \in \mathcal{P}\}$在$\mathcal{A}$上有一个统一的版本$\mu$. 令

 
$$
\mathcal{H}_{+}^{*}=\{f\mid\exists f_{n}\in\mathcal{H}_{+}, 使 f_{n}\uparrow f\},\mathcal{D}=\{A\subset E\mid I_{A}\in\mathcal{H}_{+}^{*}\}.
$$
 

对每个 $f \in \mathcal{H}_+$，我们选取一个序列 $(f_n) \subset \mathcal{H}_+$，使得 $f_n \downarrow f$，且令

 
$$
\begin{aligned}&T^{*}(f)=\limsup_{n\to\infty}T(f_{n}),\\&\mathcal{D}_{1}=\{A\in\mathcal{D}\mid T^{*}(I_{A})<\infty,\mathcal{N}-a.e.\}.\\ \end{aligned}
$$
 

则 $(\mathcal{D}_{1})_{\sigma}=\mathcal{D}$，并由引理3.5.7知 $\sigma(\mathcal{D})=\sigma(\mathcal{H})$。令

 
$$
\mathcal{C}=\left\{A\cap B^{c}\left|A,B\in\mathcal{D}\right.\right\},\ \mathcal{A}=\mathcal{C}_{\Sigma f}.
$$
 

则A为E上的代数，且有 $\sigma(\mathcal{A})=\sigma(\mathcal{H})$。令

 
$$
\overline{{\mu}}(A)=T^{*}(I_{A}),\quad A\in\mathcal{D}.
$$
 

则易见 $\overline{\mu}$为 $\{\mu_P, P \in \mathcal{P}\}$在 $\mathcal{D}$上的一个统一版本。设 $C \in \mathcal{C}, C = A \cap B^c, A, B \in \mathcal{D}$。任取 $A_n \in \mathcal{D}_1, n \geq 1$，使得 $A_n \uparrow A$。对一切 $P \in \mathcal{P}$，显然有

 
$$
\mu_{\mathbb{P}}(C)=\lim_{n\to\infty}\mu_{\mathbb{P}}(A_{n}\cap B^{c})=\lim_{n\to\infty}[\mu_{\mathbb{P}}(A_{n})-\mu_{\mathbb{P}}(A_{n}\cap B^{c})],\quad\mathbb{P}\mathrm{-a.e.}.
$$
 

---

于是若令

 
$$
\mu(C)=\limsup_{n\to\infty}[\overline{\mu}_{P}(A_{n})-\overline{\mu}_{P}(A_{n}\cap B^{c})],
$$
 

则如此定义的μ是{μ_P, ℝ ∈ ℝ}在ℝ上的一个统一版本．从而μ可唯一地延拓到ℝ上成为{μ_ℝ, ℝ ∈ ℝ}在ℝ上的一个统一版本．

定义4.7.7 设 $(\Omega,\mathcal{F},\mathcal{N})$为一由概率族 $P$确定的随机空间，其中 $N$由(4.7.1)给出。又设 $(\mathcal{E},\mathcal{E})$为一可测空间。称 $(\Omega,\mathcal{F})$到 $(\mathcal{E},\mathcal{E})$的两个核 $K_1$和 $K_2$是 $N$等价的，如果存在 $N\in\mathcal{N}$，使得对每个 $\omega\in\Omega\setminus N$，有 $K_1(\omega,\cdot)=K_2(\omega,\cdot)$成立。

定义4.7.8 设 $(\Omega,\mathcal{F},\mathcal{N})$为一随机空间，其中 $\mathcal{N}$由(4.7.1)给出.

(1) 设  $\mu$ 为  $(E, \mathcal{E})$ 上的一  $\mathcal{N}$ 随机测度。如果存在从  $(\Omega, \mathcal{F})$ 到  $(E, \mathcal{E})$ 的一个核  $K$ 和  $N \in \mathcal{N}$，使得对每个  $\omega \in \Omega \setminus N$，对一切  $A \in \mathcal{E}$，有  $K(\omega, A) = \mu(A)(\omega)$，则称  $K$ 为  $\mu$ 的核表示。

(2) 设H为E上的一向量格, T为H上的一N随机Daniell积分. 如果存在从( $\Omega$, F)到(E, E)的一个核K, 使得对一切 $f \in H$, 有 $T(f) = K(\cdot, f)$, N-a.e., 则称K为T的核表示.

在概率论和马氏过程理论中, 构造概率转移核是一个重要问题. 一个自然的问题是: 在什么条件下H上的N随机Daniell积分有核表示? 为了回答这一问题, 我们首先给出N随机测度有核表示的一个充分条件.

定理4.7.9 设 $(\Omega,\mathcal{F},\mathcal{N})$为一随机空间， $(E,\mathcal{E})$为一可分可测空间， $\mu$为 $(E,\mathcal{E})$上的N随机测度。如果存在E上一紧类 $\mathcal{D}\subset\mathcal{E}$，满足如下条件：

(1) 对任何  $(E, \mathcal{E})$ 上的有限测度  $\nu$，对一切  $A \in \mathcal{E}$，有

 
$$
\nu(A)=\sup\{\nu(C):C\subset A,C\in\mathcal{D}\};
$$
 

(2)  $D_\sigma$ 包含生成  $\varepsilon$ 的一可数代数  $A = \{A_1, A_2, \cdots\}$，则  $\mu$ 有核表示，且在  $N$ 等价意义下是唯一的。

证 不妨假定μ为有限N随机测度.  $\forall i \geqslant 1$, 选取 $\mathcal{D}_{\cup f}$中的一列元素 $\{C_{i,k}, k \geqslant 1\}$, 使得 $C_{i,k}$单调上升趋于 $A_{i}$. 令 $\mathcal{C} = \{C_{i,k}, i, k \geqslant 1\}$,  $A_{1}$为由 $\mathcal{A} \cup \mathcal{C}$生成的代数. 于是存在 $N \in \mathcal{N}$, 使得对每个 $\omega \in \Omega \setminus N$,  $\mu(E)(\omega) < \infty$, 且 $\mu(\cdot)(\omega)$为有限可加的. 由于 $\mathcal{C} \subset \mathcal{A}_{1}$, 且有

 
$$
\mu(A)(\omega)=\sup\{\mu(C)(\omega):C\subset A,C\in\mathcal{C}\},\ \forall A\in\mathcal{A}.
$$
 

于是由引理4.5.3知，对每个 $\omega \in \Omega \setminus N$， $\mu(\cdot)(\omega)$可以扩张成为 $(E, \mathcal{E})$上的一有限测度，记为 $K(\omega, \cdot)$。对 $\omega \in N$，令 $K(\omega, \cdot)$为零测度，则 $K$为从 $(\Omega, \mathcal{F})$到 $(E, \mathcal{E})$的一个核，且由单调类定理知， $K$是随机测度 $\mu$在 $(E, \mathcal{E})$上的限制的核表示。

基于这一定理, 由Daniell-Stone定理的随机版本立刻得到如下定理.

---

定理4.7.10 设 $(\Omega,\mathcal{F},\mathcal{N})$为一随机空间，其中 $\mathcal{N}$由(4.7.1)给出， $\mathcal{H}$为E上的一向量格。令 $\mathcal{E}=\sigma(\mathcal{H})$。假定 $(E,\mathcal{E})$满足定理4.7.9的条件，且存在 $\mathcal{H}_{+}$中一处处单调上升于1的序列，则 $\mathcal{H}$上的任一 $\mathcal{N}$随机Daniell积分都有核表示，且在 $\mathcal{N}$等价意义下唯一。

##### 习题

4.7.1 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{A}$为E上的一代数， $\mu$为 $\mathcal{A}$上的一有限 $\mathbb{P}$随机测度。则 $\mu$可以唯一地扩张成为 $\sigma(\mathcal{A})$上的 $\mathbb{P}$随机测度。

---

## 第 5 章 Hausdorff 空间上的测度与积分

## 5.1 拓扑空间

本节介绍拓扑空间的一些基本概念和结果, 这是为本章其余各节作准备的. 这里我们假定读者熟悉有关距离空间的概念和基本结果.

定义5.1.1 设X为一非空集合， $\mathcal{G}$为X的一子集族。如果 $X,\varnothing\in\mathcal{G}$，且 $\mathcal{G}$对有限交及任意并运算封闭，则称 $\mathcal{G}$为X的一个拓扑，称序偶 $(X,\mathcal{G})$为拓扑空间。当拓扑 $\mathcal{G}$自明或无需指出时，直接称X为拓扑空间。 $\mathcal{G}$中的元素称为开集。设 $F$为X的一子集，若其补集 $F^c$为开集，则称 $F$为闭集。我们用 $\mathcal{F}$表示X中的闭集全体，则 $\mathcal{F}$对有限并及任意交运算封闭。

定义5.1.2 设 $(X,G)$为一拓扑空间， $B$为 $G$的子类，如果 $G$中每一元素都是 $B$中某些元素的并，则称 $B$为拓扑 $G$的基。若有 $G$的可数子类 $B$成为拓扑 $G$的基，则称 $(X,G)$为具可数基或满足第二可数性公理的拓扑空间。若集类 $D$中元素的有限交全体 $\mathcal{D}_{\cap f}$为拓扑 $G$的基，则称 $D$为拓扑 $G$的子基。

定义5.1.3 设 $(X, \mathcal{G})$为一拓扑空间，Y为X的一子集，令 $\mathcal{G}_Y = \{G \cap Y \mid G \in \mathcal{G}\}$，则 $\mathcal{G}_Y$为Y的一个拓扑，我们称 $(Y, \mathcal{G}_Y)$为 $(X, \mathcal{G})$的(拓扑)子空间，称拓扑 $\mathcal{G}_Y$为由拓扑 $\mathcal{G}$在Y上诱导的拓扑。

定义5.1.4 设 $(X,G)$为一拓扑空间，A为X的一子集，称包含A的最小闭集为A的闭包，并以 $\overline{A}$记之；称含于A的最大开集为A的内核，并以 $A^{\circ}$记之。令 $\partial A=\overline{A}\setminus A^{\circ}$，称 $\partial A$为A的边界。

容易证明：

$$
\overline{{A}}\cup\overline{{B}}=\overline{{A}}\cup\overline{{B}},\ (A\cap B)^{\circ}=A^{\circ}\cap B^{\circ},\ (A^{\circ})^{c}=\overline{{A^{c}}}.   \tag*{(5.1.1)}
$$

定义5.1.5 设 $(X, \mathcal{G})$为一拓扑空间。设 $x \in V \subset X$，称V为x的一个邻域，如果存在 $U \in \mathcal{G}$，使 $x \in U \subset V$；如果V是开集，称V为x的一个开邻域。点 $x \in X$的所有邻域构成的集类称为点x的邻域系，记为 $\mathcal{U}_x$。设 $\mathcal{V}_x$为 $\mathcal{U}_x$的子类，如果对每一 $U \in \mathcal{U}_x$，存在 $V \in \mathcal{V}_x$，使 $V \subset U$，则称 $\mathcal{V}_x$为点x的邻域系的基（或局部基）。若X中的每个点有可数局部基，则称X满足第一可数性公理。

定义5.1.6 设 $(X,G)$为一拓扑空间，A为X的一子集. 如果 $\overline{A}=X$，则称A在X中稠密. 若X有可数稠子集，则称X为可分(拓扑)空间.

---

满足第二可数性公理的空间必满足第一可数性公理，并且为可分空间.

定义5.1.7 设A为X上一集类，B为X的一子集。若 $B \subset \bigcup_{A \in A} A$，则称A为B的一个覆盖。若A为可数或有限类，分别称A为B的可数或有限覆盖。若A是B的覆盖， $A_1$是A的子类且也是B的覆盖，则称 $A_1$为A的（关于B的）子覆盖。

定义5.1.8 设 $(X, \mathcal{G})$为一拓扑空间，如果X的每一开覆盖都有有限(相应地，可数)子覆盖，则称X为紧空间(相应地，Lindelöf空间)。设K为X的子集，若K的每一开覆盖都有有限子覆盖，则称K为紧集。如果X的每个点有一紧邻域，则称X为局部紧空间。如果X可表为紧集的可数并，则称X为σ紧空间。

紧空间中的闭集必为紧集. 但在一般拓扑空间中, 紧集未必是闭集.

定义5.1.9 设 $(X, \mathcal{G})$为一拓扑空间，令 $\Delta$为任一不属于 $X$的元素，令 $X^\Delta = X \cup \{\Delta\}$，令 $\mathcal{G}^\Delta = \mathcal{G} \cup \mathcal{G}_1$，其中

 
$$
\mathcal{G}_{1}=\{E\subset X^{\Delta}\mid X^{\Delta}\backslash E 为 X 的紧闭集 \},
$$
 

则 $(X^{\triangle}, \mathcal{G}^{\triangle})$为紧拓扑空间，称其为 $(X, \mathcal{G})$的单点紧化。

定义5.1.10 设 $(X, \mathcal{G})$为一拓扑空间，如果 $X$的任意两个不同的点 $x$及 $y$都可以用两个不交开集 $U$及 $V$分离（即 $x \in U, y \in V$，且 $U \cap V = \varnothing$），则称 $X$为Hausdorff空间。如果 $X$是Hausdorff空间，且任意两个不交闭集可用两个不交开集分离，则称 $X$为正规空间。

在一Hausdorff空间中, 聚集必为闭集.

定义5.1.11 设 $(X, \mathcal{G})$及 $(Y, \mathcal{H})$为拓扑空间， $f$为从 $X$到 $Y$的一映射，若 $f^{-1}(\mathcal{H}) \subset \mathcal{G}$（即开集的原象为开集），则称 $f$为连续映射。设 $x \in X$，若 $f(x)$在 $Y$中的任意邻域 $W$的原象 $f^{-1}(W)$为 $x$在 $X$中的邻域，则称 $f$在点 $x$处连续。设 $f: X \to Y$为 $X$到 $Y$上的一对一映射，若 $f$及 $f^{-1}$都是连续映射，则称 $f$为从 $X$到 $Y$上的同胚映射。如果在两个拓扑空间之间存在同胚映射，则称这两个拓扑空间同胚。

定义5.1.12 设X为一拓扑空间. 函数 $f:X\to(-\infty,+\infty]$称为下半连续的, 如果对每个实数a, $[f>a]$为开集; 称函数 $f:X\to[-\infty,+\infty)$为上半连续的, 如果-f为下半连续.

显然, 上(下)半连续函数为Borel可测, 既下半连续又上半连续的函数为连续函数. 此外, 一族下半连续函数的上端为下半连续函数, 一族上半连续函数的下端为上半连续函数.

定理5.1.13(Dini定理) 设X为一紧拓扑空间, $f_{n}$为X上的一列非负上半连续函数,且 $f_{n}\downarrow0$,则 $f_{n}$一致收敛于0.

证  $\forall\varepsilon>0,G_{n}=\{x\mid f_{n}(x)<\varepsilon\}$ 为覆盖 X 的单调非降的开集列. 由于 X 为一紧拓扑空间, 故存在某 N, 使  $X=G_{N}$. 于是  $\forall n\geq N,$ 有  $X=G_{n}$. 这表明  $f_{n}$ 一致收敛于 0.

---

定义5.1.14 设$f$为拓扑空间$X$上的实值函数. 称集合$\{x \in X \mid f(x) \neq 0\}$的闭包为$f$的支撑, 记为$\text{supp}(f)$. 若$\text{supp}(f)$为紧集, 则称$f$具有紧支撑.

记号5.1.15 设X为一拓扑空间，分别用$g, \mathcal{F}$及$K$表示$X$中的全体开集、全体闭集及全体紧集所成的集类；用$G_\delta$表示$G$中元素的可列交全体；用$F_\sigma(K_\sigma)$表示$F(K)$中元素的可列并全体。$G_\delta$中的元称为$G_\delta$集，$F_\sigma$中的元称为$F_\sigma$集，$K_\sigma$中的元称为$K_\sigma$集（或称为$\sigma$紧集）。此外，我们用$C(X)$，$C_b(X)$及$C_c(X)$分别表示$X$上的连续函数、有界连续函数及具紧支撑的连续函数全体。

引理5.1.16 (Urysohn引理) 设X为一正规空间, E及F为X的不交闭子集. 则存在X上的一连续函数f, 使得 $0 \leqslant f \leqslant 1$, 且f在E上取值为0, 在F上取值为1.

证 令D为区间(0,1)中二进小数全体 $(D=\{m/2^{n}\mid1\leqslant m<2^{n},n=1,2,\cdots\}$，由X的正规性，存在不交开集 $U_{1/2}$及 $V_{1/2}$使 $E\subset U_{1/2},F\subset V_{1/2}$。由于 $V_{1/2}^{c}$为闭集，且 $U_{1/2}\subset V_{1/2}^{c}$，故 $\overline{U}_{1/2}\subset V_{1/2}^{c}\subset F^{c}$。因此我们有 $E\subset U_{1/2}\subset\overline{U}_{1/2}\subset F^{c}$。同理，存在开集 $U_{1/4}$及 $U_{3/4}$使得

 
$$
E\subset U_{1/4}\subset\overline{U}_{1/4}\subset U_{1/2},\ \overline{U}_{1/2}\subset U_{3/4}\subset\overline{U}_{3/4}\subset F^{c}.
$$
 

由归纳法知，存在一族开集 $\{U_r\}_{r\in D}$，使得

 
$$
E\subset U_{r}\subset\overline{U}_{r}\subset U_{s}\subset\overline{U}_{s}\subset F^{c},\quad r<s,r,s\in D.
$$
 

令

 
$$
f(x)=\left\{\begin{aligned}&1,&x\notin\bigcup_{r}U_{r},\\&\inf\{r\mid x\in U_{r}\},&x\in\bigcup_{r}U_{r},\end{aligned}\right.
$$
 

则 $0\leqslant f\leqslant1$。显然f在E上为0，在F上为1。往证f为连续函数。设 $0\leqslant\alpha<1,0<\beta\leqslant1$，我们有

 
$$
f^{-1}([0,\beta))=\bigcup_{r<\beta}U_{r},
$$
 

 
$$
f^{-1}((\alpha,1])=f^{-1}([0,\alpha])^{c}=(\bigcap_{r>\alpha}U_{r})^{c}=(\bigcap_{r>\alpha}\overline{U}_{r})^{c}.
$$
 

这表明 $f^{-1}([0,\beta))$及 $f^{-1}((\alpha,1])$为开集，从而对 $0<\alpha<\beta<1$， $f^{-1}((\alpha,\beta))$也为开集。但 $[0,\beta)$， $(\alpha,1]$及 $(\alpha,\beta)$这三种类型开集全体构成 $[0,1]$的基（即 $[0,1]$作为一拓扑空间，其中开集都可表为这三类开集的并），故 $f$为连续函数。

定理5.1.17 (Tietze扩张定理) 令X为一正规空间, E为X 的一闭子集, 如果f为定义于E的有界实值连续函数(E按X诱导的拓扑为一拓扑空间), 则存在X上的有界连续函数g, 使g在E上的限制为f, 且 $\sup_{x\in X}|g(x)|=\sup_{x\in E}|f(x)|$.

---

证 不妨假定 $\sup|f(x)|=1$。令 $E_{1}=[f\leqslant-\frac{1}{3}],F_{1}=[f\geqslant\frac{1}{3}]$，由Urysohn引理，可取X上的一连续函数 $g_{1}$使得 $-1/3\leqslant g_{1}\leqslant1/3$，且 $g_{1}$在 $E_{1}$上为 $-1/3$，在 $F_{1}$上为 $1/3$。这时显然有

 
$$
\left|f(x)-g_{1}(x)\right|\leqslant\frac{2}{3},\quad\forall x\in E.
$$
 

依归纳法，可取X上的连续函数 $g_{2},g_{3},\cdots$，使得 $\left|g_{n}\right|\leqslant2^{n-1}/3^{n}$，且有

 
$$
|f(x)-\sum_{i=1}^{n}g_{i}(x)|\leqslant\left(\frac{2}{3}\right)^{n},\quad\forall x\in E.
$$
 

令 $g=\sum_{i=1}^{\infty}g_{i}$，则g即为满足定理要求的连续函数.

下面我们研究局部紧Hausdorff空间的性质.

引理5.1.18 设X为一Hausdorff空间, K及L为X的两个不交紧子集, 则存在X的两个不交开子集U及V, 使得 $K \subset U, L \subset V$.

证 不妨设K及L非空. 首先任意取定某 $x \in K$，则对任何 $y \in L$，存在不交开集 $U_y$及 $V_y$，使 $x \in U_y, y \in V_y$，由于L为紧集；故存在 $y_1, \cdots, y_n \in L$，使 $L \subset \bigcup_{i=1}^n V_{y_i}$。令

 
$$
U_{x}=\bigcap_{i=1}^{n}U_{y_{i}},\quad V_{x}=\bigcup_{i=1}^{n}V_{y_{i}},
$$
 

则 $U_x$和 $V_x$为不交开集，且 $x \in U_x, L \subset V_x$。对每个 $x \in K$，我们可以找到这样的一对开集。由于 $K$是紧集，故存在 $x_1, \cdots, x_m \in K$，使 $K \subset \bigcup_{i=1}^m U_x_i$。令

 
$$
U=\bigcup_{i=1}^{m}U_{x_{i}},\quad V=\bigcap_{i=1}^{m}V_{x_{i}},
$$
 

则 $K \subset U, L \subset V$，且U和V为不交开集。

作为该引理的一个推论, 我们有如下命题.

命题5.1.19 紧Hausdorff空间为正规空间.

命题5.1.20 设X为一局部紧Hausdorff空间, K为X的紧子集, U为包含K的一开集, 则有如下结论:

(1) 存在开集 V，其闭包为紧集，使得

 
$$
K\subset V\subset\overline{V}\subset U;
$$
 

(2) 存在一具紧支撑的连续函数  $f$，使得  $\sup p(f) \subset U$，且  $I_K \leqslant f \leqslant I_U$;

(3) 如果  $K \in \mathcal{G}_\delta$，则 (2) 中的  $f$ 在  $K^c$ 上可取为  $<1$;

(4) 存在紧集  $K_1$ 及开集  $U_1$，使得  $K_1 \in \mathcal{G}_\delta$， $U_1$ 为  $\mathcal{G}_\delta$ 中紧集的可列并，且使  $K \subset U_1 \subset K_1 \subset U$。

---

证 (1) 设  $x \in K$，由于 X 的局部紧性，存在 x 的开邻域  $W_x$，其闭包为紧集。不妨设  $W_x \subset U$，对紧集  $\{x\}$ 及  $\overline{W}_x \setminus W_x$ 应用引理 5.1.18，存在不交开集  $V_1$ 及  $V_2$，使  $x \in V_1$， $\overline{W}_x \setminus W_x \subset V_2$。令  $V_x = V_1 \cap W_x$。由于  $\overline{V}_1 \subset V_2^c$，故易知  $\overline{V}_x \cap U^c = \varnothing$，即  $\overline{V}_x \subset U$。显然  $x \in V_x$，且  $\overline{V}_x$ 为紧集。由于 K 是紧集，故存在  $x_1, \cdots, x_n \in K$，使  $K \subset \bigcup_{i=1}^n V_{x_i}$。令  $V = \bigcup_{i=1}^n V_{x_i}$，则  $\overline{V}$ 为紧集，且  $K \subset V \subset \overline{V} \subset U$。

(2) 令V为(1)中的开集，作为子空间， $\overline{V}$为紧Hausdorff空间，从而为正规空间。由Urysohn引理，存在 $\overline{V}$上的连续函数g，使 $0 \leqslant g \leqslant 1$，且g在K上为1，在 $\overline{V}\backslash V$为0。令

 
$$
f(x)=\left\{\begin{aligned}&g(x),&\quad&x\in V,\\ &0,&\quad&x\in X\backslash\overline{V},\end{aligned}\right.
$$
 

则f在 $\overline{V}$上连续，在 $X\backslash V$上为0(从而连续)。由于 $\overline{V}$及 $X\backslash V$为闭集，且 $\overline{V}\cup(X\backslash V)=X$，故f在X上连续。显然有 $I_K\leqslant f\leqslant I_U$，且 $\operatorname{supp}(f)\subset\overline{V}\subset U$。

(3) 令 V 为 (1) 中的开集，设  $K \in \mathcal{G}_\delta$，则存在一列下降开集  $G_n \subset V$，使得  $\bigcap_n G_n = K$。由 (2)，存在连续函数  $f_n$，使  $0 \leqslant f_n \leqslant 1$，且  $f_n$ 在 K 上为 1，在  $G_n^c$ 上为 0。令

 
$$
f=\sum_{n=1}^{\infty}\frac{1}{2^{n}}f_{n},
$$
 

则 $f$为连续函数， $0 \leqslant f \leqslant 1$，且 $f$在 $K$上为 $1$，在 $K^c$上 $< 1$。此外有 $\sup p(f) \subset \overline{V} \subset U$。

(4) 由(1)不妨设 $\overline{U}$为紧集，令 $f$为(2)中的函数，使得 $0 \leqslant f \leqslant 1$， $f$在 $K$上为1，在 $V^c$上为0。令

 
$$
K_{1}=\left[f\geqslant\frac{1}{2}\right]=\bigcap_{n=1}^{\infty}\left[f>\frac{1}{2}-\frac{1}{n}\right],
$$
 

 
$$
U_{1}=\left[f>\frac{1}{2}\right]=\bigcup_{n=1}^{\infty}\left[f\geqslant\frac{1}{2}+\frac{1}{n}\right],
$$
 

则 $K_{1}$及 $U_{1}$满足(4)的要求.

引理5.1.21 设X为一Hausdorff空间，K为X的一紧子集， $U_{1}$及 $U_{2}$为X的开子集，使得 $K \subset U_{1} \cup U_{2}$，则存在紧集 $K_{1}$及 $K_{2}$，使得 $K = K_{1} \cup K_{2}$， $K_{1} \subset U_{1}$， $K_{2} \subset U_{2}$。

证 令  $L_1 = K \setminus U_1, L_2 = K \setminus U_2$，则  $L_1$ 和  $L_2$ 为不交紧集。由引理5.1.18，存在不交开集  $V_1$ 及  $V_2$，使  $V_1 \supset L_1, V_2 \supset L_2$。令  $K_1 = K \setminus V_1, K_2 = K \setminus V_2$，则易证  $K_1$ 及  $K_2$ 满足引理要求。

命题5.1.22 设X为局部紧Hausdorff空间, $f\in C_{c}(X)$， $U_{1},\cdots,U_{n}$为X的开子集，使得 $\sup_{}(f)\subset\bigcup_{i=1}^{n}U_{i}$.则存在 $C_{c}(X)$中的函数 $f_{1},\cdots,f_{n}$，使得 $f=f_{1}+\cdots+f_{n}$，且 $\sup_{}(f_{i})\subset U_{i},1\leqslant i\leqslant n$.进一步，若f非负，则每个 $f_{i}$也可取为非负.

---

证 由归纳法, 只需考虑 n = 2 情形. 由引理 5.1.21, 存在紧集  $K_{1}$ 及  $K_{2}$, 使  $\operatorname{supp}(f) = K_{1} \cup K_{2}, K_{1} \subset U_{1}, K_{2} \subset U_{2}$. 由命题 5.1.20(2), 存在  $h_{1}, h_{2} \in C_{c}(X)$, 使得

 
$$
I_{K_{i}}\leqslant h_{i}\leqslant I_{U_{i}},\quad\operatorname{supp}(h_{i})\subset U_{i},\quad i=1,2.
$$
 

令 $g_1 = h_1, g_2 = h_2 - (h_1 \wedge h_2)$，则 $g_1$及 $g_2$非负，其支撑分别含于 $U_1$及 $U_2$，且在 $\text{supp}(f)$上， $g_1(x) + g_2(x) = h_1(x) \vee h_2(x) = 1$。最后，令 $f_i = fg_i, i = 1, 2$，则 $f = f_1 + f_2$， $\text{supp}(f_i) \subset U_i, i = 1, 2$。

命题5.1.23 设X为一局部紧Hausdorff空间, $K_{1},\cdots,K_{n}$为X的不交紧子集, $\alpha_{1},\cdots,\alpha_{n}$为实数.则存在一具紧支撑的连续函数f,使得

(1)  $f(x) = \alpha_i$, 如果  $x \in K_i$,  $i = 1, \cdots, n$;

(2)  $\|f\|_\infty = \max\{|\alpha_1|, \cdots, |\alpha_n|\}$，其中  $\|f\|_\infty \hat{=} \sup_{x \in X} |f(x)|$.

证 由引理5.1.18不难归纳证明：存在不交开集 $U_1,\cdots,U_n$，使 $K_i\subset U_i,1\leqslant i\leqslant n$。由命题5.1.20(2)知，对每个 $i$，存在 $f_i\in C_c(X),0\leqslant f_i\leqslant1$，使得 $I_{K_i}\leqslant f_i\leqslant I_{U_i}$。令 $f=\sum_{i=1}^n\alpha_i f_i$，则 $f$满足命题要求。

系5.1.24 设X为一局部紧Hausdorff空间, K及L为X的两个不交紧子集, 则存在两个不交的 $F_\sigma$开集U及V, 使得 $K \subset U, L \subset V$.

证 由命题5.1.23, 存在  $f \in C_c(X)$, 使  $0 \leqslant f \leqslant 1$, 且 f 在 K 上为 1, 在 L 上为 0. 令

 
$$
U=\left[f>\frac{1}{2}\right]=\bigcup_{n=1}^{\infty}\left[f\geqslant\frac{1}{2}+\frac{1}{n}\right],
$$
 

 
$$
V=\left[f<\frac{1}{2}\right]=\bigcup_{n=1}^{\infty}\left[f\leqslant\frac{1}{2}-\frac{1}{n}\right],
$$
 

则U及V为 $F_\sigma$开集， $U \cap V = \varnothing$，且 $U \supset K, V \supset L$。

引理5.1.25 设X为一局部紧Hausdorff空间，K为X的一紧子集， $U_{1},\cdots,U_{n}$ 为X的开子集，使得 $K\subset\bigcup_{i=1}^{n}U_{i}$。如果 $K\in\mathcal{G}_{\delta}$，则存在 $\mathcal{G}_{\delta}$ 紧集 $K_{1},\cdots,K_{n}$，使得 $K_{i}\subset U_{i},1\leqslant i\leqslant n$，且 $K=\bigcup_{i=1}^{n}K_{i}$。

证 由归纳法知, 只需对  $n = 2$ 情形证明结论. 令  $L_1 = K \setminus U_1$,  $L_2 = K \setminus U_2$, 则  $L_1$ 和  $L_2$ 为不相交紧集. 由系 5.1.24 知, 存在不相交  $\mathcal{F}_\sigma$ 开集  $V_1$ 及  $V_2$, 使  $V_1 \supset L_1$,  $V_2 \supset L_2$. 令  $K_1 = K \setminus V_1$,  $K_2 = K \setminus V_2$, 则  $K_1$ 及  $K_2$ 满足引理要求.

定义5.1.26 设$(X,\rho)$为一距离空间，$A$为$X$的一子集。如果$\sup_{x,y\in A}\rho(x,y)<\infty$，称$A$为有界集；如果$\forall\varepsilon>0$，存在$X$的有穷子集$B$，满足如下条件：$\forall x\in A$，存在$y\in B$，使$\rho(x,y)<\varepsilon$，称$A$为全有界集；如果$A$中任一点列在$X$中有一收敛子列，称$A$为列紧集。$X$中的一点列$(x_n)$称为基本列$(Cauchy$列)，如果$\rho(x_n,x_m)\to0,n,m\to\infty$。称距离空间$(X,\rho)$为完备的，如果$X$中的任一基本列皆收敛。

---

注意: 完备性概念不是拓扑概念. 一个完备距离空间可以改赋以一等价距离变成非完备空间.

定理5.1.27 (Baire定理) 设X为一完备距离空间或局部紧Hausdorff空间. 令 $(V_{n})$为一列在X中稠密的开子集, 则其交集也在X中稠.

证 我们只对完备距离空间情形证明，将另一情形的证明留给读者．任取X中一非空开集 $B_0$，则存在一半径小于1的开球 $B_1$，使得 $\overline{B}_1 \subset V_1 \cap B_0$．由归纳法，对每个 $n \geq 1$，存在半径小于1/n的开球，使得 $\overline{B}_n \subset V_n \cap B_{n-1}$．令 $K = \bigcap_{n=1}^{\infty} \overline{B}_n$， $B_n$的球心 $x_n$构成X中的一基本列，从而收敛于X中某一点 $x$。显然有 $x \in K$．但 $K \subset B_0 \cap \bigcap_{n=1}^{\infty} V_n$，于是 $B_0$与 $\bigcap_{n=1}^{\infty} V_n$的交非空．这表明 $\bigcap_{n=1}^{\infty} V_n$在X中稠．

定义5.1.28 设 $(X,G)$为拓扑空间，A为X的子集. 如果 $(\overline{A})^{\circ}=\varnothing$，则称A在X中无处稠密. 称空间X为第一纲的，如果它可表为可数多个无处稠密集的并. 称空间X为第二纲的，如果它不能表为可数多个无处稠密集的并.

由(5.1.1)推知，一集合A为X中无处稠密集，当且仅当 $(\overline{A})^{c}$在X中稠.

定理5.1.29 完备距离空间或局部紧Hausdorff空间为第二纲的.

证 我们用反证法来证明定理. 设X为一完备距离空间或局部紧Hausdorff空间, 假定它是第一纲的, 即它可表为一列无处稠密集 $(A_{n})$ 的并. 令 $V_{n}=(\overline{A}_{n})^{c}$, 则 $(V_{n})$ 为一列在X中稠密的开子集, 从而由Baire定理知, 它们的交集也在X中稠. 于是有

 
$$
X=\overline{{\cap_{n}V_{n}}}=\cap_{n}(\overline{{A}}_{n})^{c}=(\cup_{n}\overline{{A}}_{n})^{c}.
$$
 

另一方面，由假定 $\cup_{n}\overline{A}_{n}=X$，故由(5.1.1)式得

 
$$
\overline{{(\cup_{n}\overline{{A}}_{n})^{c}}}=\left(\left(\cup_{n}\overline{{A}}_{n}\right)^{\circ}\right)^{c}=\varnothing.
$$
 

这导致矛盾.

##### 习题

5.1.1 试证：(1) 紧空间中每个闭集为紧集；(2) Hausdorff空间中的紧集为闭集(提示：利用引理5.1.18)；(3) 含于一紧集的闭集为紧集；(4) 设F为一紧空间中的一族闭集，如果它具有“有限交性质”(F中任何有限多个集合的交非空)，则F中所有集合的交非空.

5.1.2 设X和Y为拓扑空间，f为X到Y中的连续映射，K为X的紧子集，则 $f(K)$为Y的紧子集。设X为一紧空间，Y为一Hausdorff空间，f为X到Y上的一对一连续映射，则f为X到Y上的同胚映射。

5.1.3 设X和Y为拓扑空间，令 $F_1, \cdots, F_n$为X的闭子集，使得 $X = \bigcup_{i=1}^{n} F_i$。设f为X到Y中的一个映射，若f限于每个 $F_i$为连续，则f在X上连续。

5.1.4 证明5.1.9，并证明：为要一拓扑空间X为紧空间，必须且只需单点集 $\{\Delta\}$是单点紧化 $X \cup \{\Delta\}$中的开集.

---

5.1.5 设X为一局部紧Hausdorff空间，F为X的一闭子集或开子集，则作为X的子空间，F是局部紧Hausdorff空间.

5.1.6 (Lindelőf定理) 具有可数基的空间为Lindelőf空间.

5.1.7 设X为一距离空间，则下列三个断言等价：(1)X为Lindelöf空间；(2)X为可分的；(3)X具可数基.

5.1.8 具有可数基的局部紧Hausdorff空间必为 $\sigma$紧空间(提示: 利用Lindelöf定理).

5.1.9 设X为一σ紧的局部紧Hausdorff空间，则存在一列 $G_{\delta}$紧集 $K_{n}$，使 $K_{n}\subset K_{n+1}^{\circ},n\geqslant1$，且 $X=\mid\bot_{n}K_{n}$（提示：利用命题5.1.20(4)）.

5.1.10（Urysohn嵌入定理）具有可数基的正规Hausdorff空间必同胚于Hilbert空间R∞的某一子空间。这里R∞={(x₁,x₂,…), x₁ ∈ R, i ≥ 1, ∑ᵢₖ₁ xᵢ² < ∞}, 内积(x,y)为: (x,y) = ∑ᵢₖ₁ xᵢy₁ (提示: 分以下三个步骤证明定理: (1) 设C为X的可数基(假定∅ ∉ C). 令A = {(U,V) | U,V ∈ C, ∪ C V}, 将A的成员排列为: (U₁,V₁), (U₂,V₂), … 由Urysohn引理, 对每个i ≥ 1, 存在连续映射f₁ : X → [0,1], 使f₁在∪上为0, 在V⁽¹⁾上为1. (2) 在X 上定义映射: f(x) = (f₁(x), (1/2)f₂(x), (1/3)f₃(x), …), 证明f为X到R∞中的一对一连续映射. (3) 证明对X的每一开集W, f(W) 是f(X)的开集).

5.1.11 具有可数基的局部紧Hausdorff空间X必可距离化(即其拓扑可由一距离引出)(提示: X的单点紧化 $X \cup \{\Delta\}$仍具可数基).

5.1.12 距离空间中列紧集是全有界集，完备距离空间中的全有界集为列紧集.

5.1.13 距离空间为紧的，当且仅当它是全有界的和完备的.

## 5.2 局部紧Hausdorff空间上测度与Riesz表示定理

设X为一拓扑空间， $C_{c}(X)$表示X上具有紧支撑的连续函数全体．易知 $C_{c}(X)$为一向量格(见定义4.6.1)．本节将用Daniell积分研究当X为局部紧Hausdorff空间时 $C_{c}(X)$上的正线性泛函的积分表示(即Riesz表示定理)．

首先, 我们研究拓扑空间上由某些集类生成的 $\sigma$代数及它们之间的关系.

定义5.2.1 设X为一拓扑空间. 令

 
$$
C_{c}(X)_{+}^{*}=\{f\mid\exists f_{n}\in C_{c}(X)_{+}, 使 f_{n}\uparrow f\},
$$
 

 
$$
\mathcal{O}_{c}=\{C\subset X\mid I_{C}\in C_{c}(X)_{+}^{*}\},
$$
 

称 $O_{c}$中的元素为 $C_{c}(X)$开集. 类似定义 $C(X)$开集及 $C_{b}(X)$开集.

由引理3.5.7(6)知, $\sigma(\mathcal{O}_{c})=\sigma(C_{c}(X))$.

当X为局部紧Hausdorff空间时，下一命题给出了 $C_{c}(X)$开集的一个刻画.

命题5.2.2 设X为一局部紧Hausdorff空间. 则X的一子集为 $C_{c}(X)$开集, 当且仅当它为 $K_{\sigma}$开集. 特别, 有 $\sigma\left(K_{\sigma}\right)=\sigma\left(C_{c}(X)\right)$.

---

证 设G为 $C_{c}(X)$开集. 依定义, 存在 $C_{c}(X)$中一列非负函数 $f_{n}$单调上升趋于 $I_{G}$. 于是

 
$$
G=\bigcup_{n=1}^{\infty}[f_{n}>0]=\bigcup_{n,k=1}^{\infty}[f_{n}\geqslant\frac{1}{k}]\in\mathcal{K}_{\sigma}.
$$
 

反之，设$G$为一$\mathcal{K}_\sigma$开集，即$G = \bigcup_{n=1}^\infty K_n$，其中每个$K_n$为紧集。由命题5.1.20(2)，对每个$n$，存在$f_n \in C_c(X), 0 \leqslant f_n \leqslant 1$，使$f_n$在$K_n$上为1，且$\operatorname{supp}(f_n) \subset G$。令$g_n = \bigvee_1^n f_i$，则$g_n \in C_c(X), g_n \uparrow I_G$，于是$G$为$C_c(X)$开集。

命题5.2.3 设X为一局部紧Hausdorff空间，则有 $\sigma(C_{c}(X))=\sigma(\mathcal{G}_{\delta}$紧集).

证 设  $f \in C_c(X)$，则对一切  $a \in \mathbb{R}$，

 
$$
[f\geqslant a]=\bigcap_{n=1}^{\infty}\left[f>a-\frac{1}{n}\right]\in\mathcal{G}_{\delta},
$$
 

故$[f \geqslant a]$为$\mathcal{G}_\delta$紧集，从而$\sigma(C_c(X)) \subset \sigma(\mathcal{G}_\delta)$紧集。反之，设$K$为$\mathcal{G}_\delta$紧集，则由命题5.1.20(3)，存在$f \in C_c(X)$，使$K = [f = 1]$，故有$\sigma(\mathcal{G}_\delta)$紧集$(\subset \sigma(C_c(X)))$。

定义5.2.4 设X为一拓扑空间，由全体开集生成的σ代数称为Borel σ代数，记为B(X)。B(X)中的元称为Borel集。由全体G₈紧集生成的σ代数称为强Baire σ代数，记为Bₐ(X)。Bₐ(X)中的元称为强Baire集。使全体连续函数为可测的最小σ代数称为Baire σ代数，记为B₀(X)。B₀(X)中的元称为Baire集。

命题5.2.5 设X为一局部紧Hausdorff空间，则每个强Baire紧集为 $G_{\delta}$集.

证 设C为强Baire紧集，由于 $\mathcal{B}_{a}(X)=\sigma\left(\mathcal{G}_{\delta}\right)$，故存在一列 $\mathcal{G}_{\delta}$紧集 $\left(C_{n}\right)$，使 $C\in\sigma\left(C_{1},C_{2},\cdots\right)$（习题1.2.3）。由命题5.1.20(3)，对每个n，存在 $f_{n}\in C_{c}(X)$，使 $0\leqslant f_{n}\leqslant1$，且 $C_{n}=\left[f_{n}=1\right]$。令

 
$$
d(x,y)=\sum_{n=1}^{\infty}\frac{1}{2^{n}}|f_{n}(x)-f_{n}(y)|.
$$
 

对每个 $x \in X$，令 $[x] = \{y \in X \mid d(x, y) = 0\}$，则 $[x]$是 $x$的等价类，其等价关系是： $x \sim y$当且仅当 $d(x, y) = 0$。令 $\hat{X}$表示等价类全体，在 $\hat{X}$上定义距离 $\delta$：

 
$$
\delta([x],[y])=d(x,y),
$$
 

则 $\widehat{X}, \delta$为距离空间．令 $\eta(x) = [x]$．设 $r > 0, E = \{[y] \mid \delta([y], [x]) < r\}$，则 $\eta^{-1}(E) = \{y \mid d(y, x) < r\}$为X中的开集（因 $d(\cdot, x)$为X上的连续函数）．由习题5.1.2， $\eta(C)$为 $\widehat{X}$的紧子集．由于 $\widehat{X}$是距离空间， $\eta(C)$为 $\widehat{X}$中的 $\mathcal{G}_\delta$集，即 $\eta(C) = \bigcap_{n=1}^{\infty} \widehat{O}_n$，其中每个 $\widehat{O}_n$为 $\widehat{X}$的开子集．令 $O_n = \eta^{-1}(\widehat{O}_n)$，则 $O_n$为X的开子集，且 $C = \bigcap_{n=1}^{\infty} O_n$，即 $C$为 $\mathcal{G}_\delta$集．

---

下面我们研究 $C_{c}(X)$上的正线性泛函的积分表示. 为此, 我们先回顾Daniell积分的定义(见定义3.6.3). 设X为一拓扑空间, $C_{c}(X)$上的一线性泛函I称为正的, 如果 $f\in C_{c}(X)$, $f\geq0\Rightarrow I(f)\geq0$. $C_{c}(X)$上一正线性泛函I称为Daniell积分, 如果

 
$$
f_{n}\in C_{c}(X),f_{n}\geqslant0,f_{n}\downarrow0\Rightarrow\lim_{n\rightarrow\infty}I(f_{n})=0.
$$
 

引理5.2.6 设X为局部紧Hausdorff空间, I为 $C_{c}(X)$上的一正线性泛函, 则I为 $C_{c}(X)$上的Daniell积分.

证 设  $f_{n} \in C_{c}(X)$,  $f_{n} \downarrow 0$, 令  $S_{1} = \operatorname{supp}(f_{1})$, 则  $\operatorname{supp}(f_{n}) \subset S_{1}$. 由 Dini 定理 (定理 5.1.13),  $f_{n}$ 在  $S_{1}$ 上一致趋于 0, 从而在 X 上一致趋于 0. 因此, 对给定  $\varepsilon > 0$, 存在自然数 N, 使当  $n \geqslant N$ 时,  $f_{n}(x) < \varepsilon$, 对一切  $x \in X$ 成立. 另一方面, 由命题 5.1.20(2), 存在  $g \in C_{c}(X)$,  $0 \leqslant g \leqslant 1$, 使 g 在  $S_{1}$ 上为 1. 于是当  $n \geqslant N$, 有  $f_{n} \leqslant \varepsilon g$,  $I(f_{n}) \leqslant \varepsilon I(g)$. 由于  $\varepsilon > 0$ 是任意的, 故  $\lim_{n \to \infty} I(f_{n}) = 0$, 这表明 I 为  $C_{c}(X)$ 上的 Daniell 积分.

定义5.2.7 设X为一拓扑空间，A为一子集。称A为有界集，如果存在一紧集K，使K⊃A；称A为σ有界集，如果存在一列紧集 $(K_n)$，使 $A \subset \bigcup_{n=1}^{\infty} K_n$。

下一定理的第(2)部分是所谓的Riesz表示定理(也见下面的定理5.3.2).

定理5.2.8 设X为一局部紧Hausdorff空间, I为 $C_{c}(X)$上的一正线性泛函. 则有下列结论:

(1) 存在  $\mathcal{B}(X)$ 上的唯一测度  $\mu_{1}$，满足如下条件：

(i)  $C_c(X) \subset L^1(X, \mathcal{B}(X), \mu_1)$，且  $\forall f \in C_c(X)$，有  $I(f) = \mu_1(f)$;

(ii) 对任意 $\sigma$有界开集O，有

$$
\mu_{1}(O)=\sup\{\mu_{1}(K)\mid K\subset O,K\in\mathcal{K}\},   \tag*{(5.2.1)}
$$

对一切Borel集A, 有

$$
\mu_{1}(A)=\inf\{\mu_{1}(O),O\supset A,O 为 \sigma 有界开集 \}.   \tag*{(5.2.2)}
$$

此外，对任一紧集K，有 $\mu_{1}(K)<\infty$.

(2) 存在  $\mathcal{B}(X)$ 上的唯一测度  $\mu_{2}$，满足如下条件：

(i) $C_{c}(X)\subset L^{1}(X,\mathcal{B}(X),\mu_{2})$，且 $\forall f\in C_{c}(X)$，有 $I(f)=\mu_{2}(f)$;

(ii) $^{\prime}$ 对任何开集O，有

$$
\mu_{2}(O)=\sup\{\mu_{2}(K)\mid K\subset O,\;K\in\mathcal{K}\},   \tag*{(5.2.3)}
$$

对一切Borel集A, 有

$$
\mu_{2}(A)=\operatorname*{i n f}\{\mu_{2}(O)\mid O\supset A,\;O\in\mathcal{G}\}.   \tag*{(5.2.4)}
$$


---

此外，对任一紧集K，有 $\mu_{2}(K)<\infty$.

证 分别用  $G_{0}$ 及  $G_{1}$ 表示  $C_{c}(X)$ 开集及  $\sigma$ 有界开集全体. 显然有  $G_{0} \subset G_{1}$，且  $G_{0}$ 和  $G_{1}$ 对可列并及有限交封闭. 令

 
$$
\mu_{1}^{*}(O)=\sup\{I(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1,\operatorname{supp}(f)\subset O\},~O\in\mathcal{G}_{1},
$$
 

 
$$
\mu_{1}^{*}(A)=\inf\{\mu^{*}(O)\mid O\supset A,O\in\mathcal{G}_{1}\},A\subset X.
$$
 

往证  $\mu_{1}^{*}$ 为 X 上的外测度. 设  $O_{i} \in \mathcal{G}_{1}, i = 1, 2, \cdots$. 若  $f \in C_{c}(X), 0 \leqslant f \leqslant 1$, 且  $\operatorname{supp}(f) \subset \bigcup_{i=1}^{\infty} O_{i}$, 则存在 n, 使  $\operatorname{supp}(f) \subset \bigcup_{i=1}^{n} O_{i}$. 故由命题 5.1.22, 存在  $f_{i} \in C_{c}(X), 1 \leqslant i \leqslant n$, 使得  $0 \leqslant f_{i} \leqslant 1, f = f_{1} + \cdots + f_{n}$, 且  $\operatorname{supp}(f_{i}) \subset O_{i}$. 因此

 
$$
I(f)=\sum_{i=1}^{n}I(f_{i})\leqslant\sum_{i=1}^{n}\mu_{1}^{*}(O_{i})\leqslant\sum_{i=1}^{\infty}\mu_{1}^{*}(O_{i}).
$$
 

于是

 
$$
\mu_{1}^{*}(\bigcup_{i=1}^{\infty}O_{i})\leqslant\sum_{i=1}^{\infty}\mu_{1}^{*}(O_{i}).
$$
 

由于 $G_{1}$对可列并封闭，故由命题1.4.3易知 $\mu_{1}^{*}$为X上的外测度.

再证每个Borel集为 $\mu_1^*$可测集. 为此, 只需证每个开集为 $\mu_1^*$可测集. 设V为一开集, 由引理1.4.5知, 为证V为 $\mu_1^*$可测集, 只需证: 对一切 $O \in \mathcal{G}_1$, 有

$$
\mu_{1}^{*}(O)\geqslant\mu_{1}^{*}(O\cap V)+\mu_{1}^{*}(O\cap V^{c}).   \tag*{(5.2.5)}
$$

下面证明这一事实. 不妨设 $\mu_1(O) < \infty$，从而 $\mu_1(O \cap V) < \infty$。由于 $O \cap V \in \mathcal{G}_1$，依定义，对给定 $\varepsilon > 0$，存在 $f_1 \in C_c(X), 0 \leq f_1 \leq 1$， $\operatorname{supp}(f_1) \subset O \cap V$，使得 $I(f_1) \geq \mu_1^*(O \cap V) - \varepsilon$。令 $K = \operatorname{supp}(f_1)$，则 $O \cap K^c \in \mathcal{G}_1$，故存在 $f_2 \in C_c(X), 0 \leq f_2 \leq 1$， $\operatorname{supp}(f_2) \subset O \cap K^c$，使得 $I(f_2) \geq \mu_1^*(O \cap K^c) - \varepsilon$。由于 $O \cap K^c \supset O \cap V^c$，故 $I(f_2) \geq \mu_1^*(O \cup V^c) - \varepsilon$。令 $f = f_1 + f_2$，则 $f \in C_c(X), 0 \leq f \leq 1$，且 $\operatorname{supp}(f) \subset O$。因此有

 
$$
\mu_{1}^{*}(O)\geqslant I(f)=I(f_{1})+I(f_{2})\geqslant\mu_{1}^{*}(O\cap V)+\mu_{1}^{*}(O\cap V^{c})-2\varepsilon,
$$
 

不等式 $(5.2.5)$得证.

令$\mu_1$为$\mu_1^*$在$\mathcal{B}(X)$上的限制，往证$\forall f\in C_c(X)$，有$I(f)=\mu_1(f)$。首先，由Daniell-Stone定理（定理3.6.8）知，存在$\sigma(C_c(X))$上的测度$\mu$，使对一切$f\in C_c(X)$，有$I(f)=\mu(f)$。下面先证对一切$C_c(X)$开集$O$，有$\mu(O)=\mu_1(O)$。设$O$是$C_c(X)$开集，则存在$f_n\in C_c(X)$，$n\geq1$，使$O\leq f_n\uparrow I_O$，于是$K_n\triangleq[f_n\geq1/n]\uparrow O, K_n$为紧集。由命题5.1.20(2)，存在$g_n\in C_c(X)$，使$I_{K_n}\leq g_n\leq I_O$，且$\mathrm{supp}(g_n)\subset O$。由于$O\in\mathcal{G}_0\subset\mathcal{G}_1$，于是有

 
$$
\mu(O)=\sup_{n}\mu(K_{n})\leqslant\sup_{n}\mu(g_{n})=\sup_{n}I(g_{n})\leqslant\mu_{1}^{*}(O)=\mu_{1}(O).
$$
 

---

另一方面，由 $\mu_{1}^{*}$的定义易知 $\mu_{1}^{*}(O) \leqslant \mu(O)$，故 $\mu(O) = \mu_{1}(O)$。现设 $f \in C_{c}(X)_{+}$，令

 
$$
f_{n}=\sum_{k=1}^{\infty}\frac{k}{2^{n}}I_{\left[\frac{k+1}{2^{n}}\geqslant f>\frac{k}{2^{n}}\right]}=\frac{1}{2^{n}}\sum_{k=1}^{\infty}I_{\left[f>\frac{k}{2^{n}}\right]},
$$
 

则 $f_{n}\uparrow f,$ 且 $[f>k/2^{n}]$ 为 $C_{c}(X)$ 开集，于是我们有

 
$$
\begin{align*}I(f)&=\mu(f)=\lim_{n\to\infty}\mu(f_{n})=\lim_{n\to\infty}\frac{1}{2^{n}}\sum_{k=1}^{\infty}\mu\left(\left[f>\frac{k}{2^{n}}\right]\right)\\&=\lim_{n\to\infty}\frac{1}{2^{n}}\sum_{k=1}^{\infty}\mu_{1}\left(\left[f>\frac{k}{2^{n}}\right]\right)=\lim_{n\to\infty}\mu_{1}(f_{n})=\mu_{1}(f).\end{align*}
$$
 

现在证明(5.2.1)式. 设  $O \in \mathcal{G}_1$, 令  $f \in C_c(X), 0 \leq f \leq 1$,  $\operatorname{supp}(f) \subset O$, 则  $I(f) = \mu_1(f) \leq \mu_1(\operatorname{supp}(f))$, 故(5.2.1)式得证.

下面证明满足条件(i)及(ii)的测度唯一性．设另有测度 $\nu$满足(i)及(ii)，则 $\forall f \in C_c(X)$，有 $\nu(f) = I(f) = \mu_1(f)$．设 $O \in \mathcal{G}_1$，则对任何紧集 $K \subset O$，存在 $f \in C_c(X)$，使 $I_K \leqslant f \leqslant I_O$， $\operatorname{supp}(f) \subset O$．故有

 
$$
\begin{aligned}\nu(O)&=\sup\{\nu(K)\mid K\subset O,K\in\mathcal{K}\}\\&\leqslant\sup\{\nu(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1,\operatorname{supp}(f)\subset O\}\\&=\sup\{I(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1,\operatorname{supp}(f)\subset O\}\\&\leqslant\mu_{1}(O)\\&=\sup\{\mu_{1}(K)\mid K\subset O,\ K\in\mathcal{K}\}\\&\leqslant\sup\{\mu_{1}(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1,\operatorname{supp}(f)\subset O\}\\&=\sup\{\nu(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1,\operatorname{supp}(f)\subset O\}\\&\leqslant\nu(O).\end{aligned}
$$
 

于是有 $\nu(O)=\mu_1(O)$。从而由(5.2.2)式知： $\nu(A)=\mu_1(A)$，对一切 $A\in\mathcal{B}(X)$成立。唯一性得证。最后，设 $K$为一紧集，由命题5.1.20(2)知 $\mu_1(K)<\infty$。

综上所述，(1)得证。(2)的证明完全类似(在定义 $\mu_{2}^{*}$时用 $\mathcal{G}$代替 $\mathcal{G}_{1}$).

注5.2.9 由 $\mu_{1}^{*}$及 $\mu_{2}^{*}$的定义知 $\mu_{1}\geqslant\mu_{2}$. 此外, 由命题5.1.20(4)知: (5.2.1)式及(5.2.3)式分别等价于

 
$$
\mu_{1}(O)=\sup\{\mu_{1}(K)\mid K\subset O,K 为 \mathcal{G}_{\delta} 紧集 \},
$$
 

 
$$
\mu_{2}(O)=\sup\{\mu_{2}(K)\mid K\subset O,K 为 \mathcal{G}_{\delta} 紧集 \}.
$$
 

最后, 若 X 为  $\sigma$ 紧的, 则  $\mu_{1} = \mu_{2}$.

---

##### 习题

5.2.1 设X为一拓扑空间，则 $\sigma(C(X))=\sigma(C_b(X))\subset\sigma(\mathcal{G}_\delta$闭集).

5.2.2 设X为一止规拓扑空间， $B_0(X)$为Baire  $\sigma$ 代数， $\mu$ 为 $B_0(X)$上的一 $\sigma$有限测度，则(1) $B_0(X)=\sigma(\mathcal{G}_\delta$闭集);

(2) 为要G为 $F_{\delta}$开集，必须且只需存在一非负有界连续函数f，使得 $G=[f>0]$;

(3) 对一切  $A \in \mathcal{B}_0(X)$，有

 
$$
\mu(A)=\sup\{\mu(B)\mid B\subset A,B 为 \mathcal{G}_{\delta} 闭集 \}.
$$
 

若进一步 $\mu$为有限测度，则对一切 $A\in\mathcal{B}_0(X)$，还有

 
$$
\mu(A)=\inf\{\mu(G)\mid G\supset A,G 为 \mathcal{F}_\sigma 开集 \}.
$$
 

## 5.3 Hausdorff空间上的正则测度

定义5.3.1 令X为一Hausdorff空间， $B(X)$为其Borel  $\sigma$ 代数， $A \supset B(X)$为X上的 $\sigma$代数， $\mu$为A上一测度。称 $\mu$为内正则的(相应地，强内正则的)，如果对每个开集(相应地， $\mathcal{A}$可测集)O，有 $\mu(O) = \sup\{\mu(K) \mid K \subset O, K$为紧集 $；称 $\mu$为外正则的，如果对每个 $A \in \mathcal{A}$，有 $\mu(A) = \inf\{\mu(O) \mid O \supset A, O$为开集 $。既内正则又外正则的测度称为正则测度。

设μ为Hausdorff空间X上的一正则测度. 如果对一切非负 $f \in C_c(X)$，有 $\mu(f) < \infty$，则称 $\mu$为Radon测度. 若X为局部紧的，则由命题5.1.20知，一正则测度 $\mu$为Radon测度，当且仅当对一切紧集K，有 $\mu(K) < \infty$.

由定理5.2.8(2)立刻推得下述定理.

定理5.3.2 设X为一局部紧Hausdorff空间，则 $C_{c}(X)$上的正线性泛函与 $\mathcal{B}(X)$上的Radon测度之间有如下一一对应关系：设 $\mu$为 $\mathcal{B}(X)$上的Radon测度，令

 
$$
L_{\mu}(f)=\int_{X}f d\mu,\quad f\in C_{c}(X),
$$
 

则 $L_{\mu}$为 $C_{c}(X)$上的正线性泛函. 反之, $C_{c}(X)$上的正线性泛函必具有这种形式.

定理5.3.3 设X为一拓扑空间，G及F表示X的开集类和闭集类，μ为B(X)上的σ有限测度. 若每个开集为Fσ集，则对每个A∈B(X)，有

$$
\mu(A)=\sup\{\mu(F)\mid F\subset A,F\in\mathcal{F}\}.   \tag*{(5.3.1)}
$$

若进一步 $\mu$为有限测度，则对每个 $A\in\mathcal{B}(X)$，还有

$$
\mu(A)=\inf\{\mu(G)\mid G\supset A,\;G\in\mathcal{G}\}.   \tag*{(5.3.2)}
$$


---

证 由于  $F_{\delta} = F$，故由定理1.6.3及命题1.6.4推得定理的结论.

系5.3.4 设X为一距离空间,  $\mu$ 为 $\mathcal{B}(X)$上的一有限测度, 则对一切 $A \in \mathcal{B}(X)$, (5.3.1)式及(5.3.2)式成立.

证 由于距离空间中每个开集为 $F_{\sigma}$集，故由定理5.3.3立得系的结论.

定理5.3.5 设X为一Hausdorff空间, A为包含B(X)的一σ代数, μ为A上的正则测度. 若A∈A, 且μ(A) < ∞, 则有

$$
\mu(A)=\sup\{\mu(K)\mid K\subset A,\;K\in\mathcal{K}\}.   \tag*{(5.3.3)}
$$

证 对任给  $\varepsilon > 0$，存在开集  $V \supset A$，使  $\mu(V) < \mu(A) + \varepsilon$。取紧集  $L \subset V$，使  $\mu(L) > \mu(V) - \varepsilon$。由于  $\mu(V \setminus A) < \varepsilon$，故有开集  $W \supset V \setminus A$，使  $\mu(W) < \varepsilon$。令  $K = L \setminus W$，则  $K \subset A$ 为紧集，且有

 
$$
\mu(K)=\mu(L)-\mu(L\cap W)>\mu(V)-2\varepsilon\geqslant\mu(A)-2\varepsilon,
$$
 

故有 $(5.3.3)$式.

下一定理表明: 有限测度的正则性与强内正则性等价.

定理5.3.6 设X为一Hausdorff空间, A为包含B(X)的一σ代数, μ为A上的有限测度. 则μ为A上的正则测度, 当且仅当μ是强内正则的.

证 只需证充分性. 设μ是强内正则的, 这蕴含μ的内正则性. 对 $A^{c}$应用(5.3.1)式便得μ的外正则性.

定理5.3.7 设X为一具可数基的局部紧Hausdorff空间,  $\mu$ 为  $\mathcal{B}(X)$ 上的一测度.

(1) 设  $A \in \mathcal{B}(X)$，且 A 关于  $\mu$ 为  $\sigma$ 有限集，则

 
$$
\mu(A)=\sup\{\mu(K)\mid K\subset A,K\in\mathcal{K}\}.
$$
 

(2) 若对每个  $K \in \mathcal{H}$，有  $\mu(K) < \infty$，则  $\mu$ 为 Radon 测度。

证 (1) 设 G 为 X 中的一开集，则由习题 5.1.4 及 5.1.8 知，G 为  $K_{\sigma}$ 集，故由定理 1.6.3 立得 (1) 的结论.

(2) 由于 X 中每个开集为  $K_{\sigma}$ 集，故由(1)知  $\mu$ 为内正则的．往证  $\mu$ 是外正则的．由习题 5.1.8 及 5.1.9 知，存在一列开集  $G_{n}$，使得  $\overline{G}_{n}$ 为紧集，且  $\bigcup_{n} G_{n} = X$．于是，对每个  $n$，有  $\mu(G_{n}) < \infty$．令

 
$$
\mu_{n}(A)=\mu(A\cap G_{n}),\quad n\geqslant1,
$$
 

则$\mu_n$为$\mathcal{B}(X)$上的有限测度，故由定理5.3.3知，$\mu_n$是外正则的。设$A \in \mathcal{B}(X)$，对任给$\varepsilon > 0$，存在开集$V_n \supset A$，使得$\mu(G_n \cap V_n) \geq \mu(A \cap G_n) + \varepsilon / 2^n$。令$V = \bigcup_{n=1}^\infty (G_n \cap V_n)$，则$V \supset A$，且有

 
$$
\mu(V\setminus A)\leqslant\sum_{n=1}^{\infty}\mu(G_{n}\cap V_{n}\setminus A)\leqslant\varepsilon,
$$
 

---

从而 $\mu(V)\leqslant\mu(A)+\varepsilon,\quad\mu$的外正则性得证.

下面讨论符号测度的正则性.

定义5.3.8 设X为一Hausdorff空间，A为包含B(X)的一σ代数，μ为A上的一符号测度. 如果μ的变差测度|μ|是正则的，则称μ是正则的.

下一命题给出了有限符号测度 $\mu$的正则性的另一等价描述.

命题5.3.9 为要一有限符号测度 $\mu$是正则的, 必须且只需 $\mu^{+}$及 $\mu^{-}$是正则的. 这里 $\mu^{+}$及 $\mu^{-}$分别是 $\mu$的正部及负部.

证 充分性显然, 现证必要性. 设  $|\mu|$ 为正则测度, 令  $A \in \mathcal{A}, \varepsilon > 0$, 取开集  $U \supset A$, 使  $|\mu|(U) < |\mu|(A) + \varepsilon$. 则  $\mu^{-}(U \setminus A) \leqslant |\mu|(U \setminus A) < \varepsilon$, 从而

 
$$
\mu^{-}(U)=\mu^{-}(A)+\mu^{-}(U\setminus A)<\mu^{-}(A)+\varepsilon,
$$
 

 $\mu^{-}$的外正则性得证. $\mu^{-}$的内正则性证明类似.同理可证 $\mu^{+}$的正则性.

命题5.3.10 设X为一Hausdorff空间， $\mathcal{A}$为包含 $\mathcal{B}(X)$的一 $\sigma$代数， $\mu$为 $\mathcal{A}$上一正则符号测度。设 $A \in \mathcal{A}$，且 $\mu(A)$为有限值，则对任给 $\varepsilon > 0$，存在紧集 $K \subset A$，使对任何满足 $K \subset B \subset A$的 $B \in \mathcal{A}$，有 $|\mu(A) - \mu(B)| < \varepsilon$。

证 由  $|\mu|$ 的正则性及定理 5.3.5，存在紧集  $K \subset A$，使  $|\mu|(A \setminus K) < \varepsilon$，于是对任何满足  $K \subset B \subset A$ 的  $B \in A$，有

 
$$
|\mu(A)-\mu(B)|=|\mu(A\setminus B)|\leqslant|\mu|(A\setminus B)\leqslant|\mu|(A\setminus K)<\varepsilon.
$$
 

记号5.3.11 设X为一Hausdorff空间，用M(X,B(X))表示B(X)上的有限符号测度全体，用M_{r}(X,B(X))表示B(X)上的有限正则符号测度全体.

由习题3.3.8(3)， $\mathcal{M}(X,\mathcal{B}(X))$按符号测度的全变差范数 $\|\cdot\|_{\text{var}}$为一Banach空间.另一方面，易知 $\mathcal{M}_{r}(X,\mathcal{B}(X))$是 $\mathcal{M}(X,\mathcal{B}(X))$的闭线性子空间，故 $\mathcal{M}_{r}(X,\mathcal{B}(X))$按范数 $\|\cdot\|_{\text{var}}$也为一Banach空间.

下面研究关于正则测度的不定积分. 为此先证明一引理.

引理5.3.12 设X为一Hausdorff空间， $\mathcal{A}$为包含 $\mathcal{B}(X)$的一 $\sigma$代数， $\mu$为 $\mathcal{A}$上的一正则测度。设 $B \in \mathcal{A}$，且 $\mu(B) < \infty$。令 $\nu(A) = \mu(B \cap A)$， $A \in \mathcal{A}$，则 $\nu$也为 $\mathcal{A}$上的正则测度。

证 由定理5.3.5, 对任何 $A \in A$, 有

 
$$
\begin{aligned}\nu(A)&=\mu(B\cap A)=\sup\{\mu(K)\mid K\subset B\cap A,K\in\mathcal{K}\}\\&=\sup\{\nu(K)\mid K\subset B\cap A,K\in\mathcal{K}\},\end{aligned}
$$
 

故有

 
$$
\nu(A)=\sup\{\nu(K)\mid K\subset A,K\in\mathcal{K}\},
$$
 

---

从而由定理5.3.6知 $\nu$为A上的正则测度.

命题5.3.13 设X为一Hausdorff空间,  $\mu$ 为  $\mathcal{B}(X)$ 上的一正则测度. 若 f 关于  $\mu$ 可积, 则 f 关于  $\mu$ 的不定积分  $f.\mu$ 是有限正则符号测度.

证 令  $\nu = f. \mu$，由于  $|\nu| = |f| \cdot \mu$，故由符号测度正则性的定义，为证  $\nu$ 正则，不妨设  $f$ 非负。首先设  $f = I_B$，其中  $B \in \mathcal{B}(X)$，且  $\mu(B) < \infty$。令  $\nu_1(A) = \mu(A \cap B)$， $A \in \mathcal{B}(X)$，则由引理 5.3.12 知， $\nu_1$ 为正则测度。因此，对  $\mu$ 可积的非负简单函数  $f$， $f \cdot \mu$ 也是正则测度。对一般的非负  $\mu$ 可积函数  $f$，令  $f_n$ 为非负简单函数，使  $f_n \uparrow$  $f$，则有

 
$$
\|f.\mu-f_{n}.\mu\|_{\mathrm{v a r}}=\int_{X}(f-f_{n})d\mu\to0,\quad n\to\infty.
$$
 

由 $\mathcal{M}_r(X,\mathcal{B}(X))$的完备性知 $f.\mu\in\mathcal{M}_r(X,\mathcal{B}(X))$.

命题5.3.14 设X为局部紧Hausdorff空间, $\mu$为 $\mathcal{B}(X)$上一Radon测度, $\nu$为 $\mathcal{B}(X)$上一有限正则符号测度.则下列断言等价:

(1)  $\nu$ 为某  $f \in L^1(X, \mathcal{B}(X), \mu)$ 关于  $\mu$ 的不定积分；

(2)  $\nu$ 关于  $\mu$ 绝对连续;

(3) 设 K 为紧集，且  $\mu(K) = 0$，则有  $\nu(K) = 0$.

证 显然有(1)  $\Rightarrow$ (2)  $\Rightarrow$ (3). 下证(3)  $\Rightarrow$ (2). 设(3)成立. 令  $A \in \mathcal{B}(X)$, 且  $\mu(A) = 0$, 则对一切紧集  $K \subset A$, 有  $\mu(K) = 0$. 往证  $\nu(A) = 0$. 假定  $|\nu(A)| = \alpha > 0$, 则由命题5.3.10知, 存在紧集  $K \subset A$, 使  $|\nu(A) - \nu(K)| < \alpha / 2$. 特别有  $\nu(K) \neq 0$, 但有  $\mu(K) = 0$, 这与(3)矛盾. 因此, 必须有  $\nu(A) = 0$, 这表明  $\nu \ll \mu$.

往证(2)⇒(1). 设(2)成立. 由 $|\nu|$的内正则性, 存在一列紧集 $K_n$, 使 $\sup_n |\nu|(K_n) = |\nu|(X)$. 令 $X_0 = \bigcup_n K_n$, 则有 $|\nu|(X \setminus X_0) = 0$. 令 $\mu_0(A) = \mu(A \cap X_0)$, 则因空间局部紧, 有 $\mu(K_n) < \infty$, 故 $\mu_0$为 $\sigma$有限测度, 且 $\nu \ll \mu_0$. 于是由Radon-Nikodym定理知, 存在 $f_0 \in L^1(X, \mathcal{B}(X), \mu_0)$, 使 $\nu = f_0 \cdot \mu_0$. 令 $f = f_0 I X_0$, 则 $f \in L^1(X, \mathcal{B}(X), \mu)$, 且 $\nu = f \cdot \mu$.

注 只在证明 $(2)\Rightarrow(1)$时用到空间“局部紧”假定.

##### 习题

5.3.1 设X为一局部紧Hausdorff空间，A为包含B(X)的σ代数，μ为A上的内正则测度.试证：

(1) 对每个开集 O，有

 
$$
\begin{aligned}\mu(O)&=\sup\{\mu(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1,\sup p(f)\subset O\}\\&=\sup\{\mu(f)\mid f\in C_{c}(X),0\leqslant f\leqslant I_{O}\}.\end{aligned}
$$
 

(提示: 利用命题5.1.20(2).)

---

(2) 令  $G_1 = \{O \mid O$ 为开集，且  $\mu(O) = 0\}$，并令  $U$ 为  $G_1$ 中全体集合的并，则  $\mu(U) = 0$（注：通常称  $U^c$ 为  $\mu$ 的支撑，记为  $\text{supp}[\mu]$）.

5.3.2 设X为一Hausdorff空间， $\mathcal{A} \supset \mathcal{B}(X)$为一σ代数，μ为 $\mathcal{A}$上的σ有限正则测度，则 $\mathcal{A} \subset \overline{\mathcal{B}(X)}^{\mu}$。这里 $\overline{\mathcal{B}(X)}^{\mu}$表示 $\mathcal{B}(X)$关于μ的完备化。

5.3.3 设X为一紧Hausdorff空间,  $\mu$ 为Baire  $\sigma$ 代数  $\mathcal{B}_{0}(X)$ 上的一有限测度, 则  $\mu$ 可以唯一扩张成为  $\mathcal{B}(X)$ 上的正则测度(提示: 用Riesz表现定理).

5.3.4 设X为一局部紧Hausdorff空间,  $\mu$ 为  $\mathcal{B}(X)$ 上的一正则测度, 则为  $\mu$ 为 Radon测度, 必须且只需对一切紧集 K, 有  $\mu(K) < \infty$.

5.3.5 证明  $\mathcal{M}_{r}(X,\mathcal{B}(X))$ 是  $\mathcal{M}(X,\mathcal{B}(X))$ 的闭线性子空间.

5.3.6 给出系5.3.4的一个直接证明(提示：令C表示 $\mathcal{B}(X)$中满足(5.3.1)式及(5.3.2)式的集A全体.显然 $A\in\mathcal{C}\Rightarrow A^{c}\in\mathcal{C}$.为证 $\mathcal{C}=\mathcal{B}(X)$，只需证C对可列并运算封闭，且 $\mathcal{G}\subset\mathcal{C}$.

5.3.7 设X为一Hausdorff空间, $\mu$为 $\mathcal{B}(X)$上Radon测度.令

 
$$
\mathcal{M}_{r}(\mu)=\{\nu\in\mathcal{M}_{r}(X,\mathcal{B}(X))\mid\nu\ll\mu\},
$$
 

则  $f \mapsto f.\mu$ 为从  $L^{1}(X,\mathcal{B}(X),\mu)$ 到  $\mathcal{M}_{r}(\mu)$ 上的线性保范同构映射 (提示:  $\|f.\mu\|_{\mathrm{var}} = \|f\|_{L^{1}(\mu)}$).

### 5.4 空间 $C_{0}(X)$的对偶

设X为局部紧Hausdorff空间，用 $C_c(X)$表示X上具紧支撑连续函数全体。X上的实值连续函数 $f$称为在无穷远处为零，是指对任给 $\varepsilon > 0$，存在紧集 $K$使 $f$在 $K^c$上有 $|f(x)| < \varepsilon$。用 $C_0(X)$表示无穷远处为零的连续函数全体，下面证明 $\mathcal{M}_r(X, \mathcal{B}(X))$可以视为 $C_0(X)$的对偶。

设 $f \in C_0(X)$，令

 
$$
\|f\|_\infty=\sup\{|f(x)|\mid x\in X\},
$$
 

则 $(C_{0}(X), \parallel \cdot \parallel_{\infty})$为赋范线性空间.

引理5.4.1 设X为局部紧Hausdorff空间, 则 $C_{0}(X)$为Banach空间, 且 $C_{c}(X)$在 $C_{0}(X)$中稠密.

证 设 $(f_n)$为 $C_0(X)$中一基本列，则对每个 $x \in X$， $(f_n(x))$为一实数基本列，故有极限 $f(x)$。显然 $f_n$在 $X$上一致收敛于 $f$，故 $f$为 $X$上的连续函数。往证 $f$在无穷远处为零。任给 $\varepsilon > 0$，先取一自然数 $n$，使对一切 $x \in X$有 $|f(x) - f_n(x)| < \varepsilon$。由于 $f_n \in C_0(X)$。故存在紧集 $K$，使 $|f_n(x)| < \varepsilon$， $\forall x \in K^c$。于是有

 
$$
|f(x)|\leqslant|f(x)-f_{n}(x)|+|f_{n}(x)|<2\varepsilon,\quad x\in K^{c},
$$
 

依定义,  $f \in C_0(X)$. 这表明  $C_0(X)$ 为一Banach空间.

---

现证$C_c(X)$在$C_0(X)$中稠密. 设$f \in C_0(X)$, 对任给$\varepsilon > 0$, 存在紧集$K$, 使$\forall x \in K^c$有$|f(x)| \leqslant \varepsilon$. 另一方面, 由命题5.1.20, 存在$g \in C_c(X)$, 使$I_K \leqslant g \leqslant 1$. 令$h = gf$, 则$h \in C_c(X)$, 且有$\|f - h\|_\infty \leqslant \varepsilon$. 这表明$C_c(X)$在$C_0(X)$中稠密.

引理5.4.2 设X为一局部紧Hausdorff空间，L为 $C_{0}(X)$上的一连续线性泛函，则存在 $C_{0}(X)$上的两个正连续线性泛函 $L_{+}$及 $L_{-}$，使 $L=L_{+}-L_{-}$.

证 设  $f \in C_{0}(X)$ 且  $f \geqslant 0$ (简记为  $f \in C_{0}(X)_{+}$)，令

$$
L_{+}(f)=\sup\{L(g)\mid g\in C_{0}(X),0\leqslant g\leqslant f\},   \tag*{(5.4.1)}
$$

则易知 $|L_{+}(f)|\leq\|L\|\|f\|_{\infty}$，其中 $\|L\|$表示L的范数。此外，显然有 $L_{+}(f)\geq0$，且 $\forall\alpha\geq0$，有 $L_{+}(\alpha f)=\alpha L_{+}(f)$。下面证明： $\forall f_{1},f_{2}\in C_{0}(X)$，有

$$
L_{+}(f_{1}+f_{2})=L_{+}(f_{1})+L_{+}(f_{2}).   \tag*{(5.4.2)}
$$

由(5.4.1)式不难看出： $L_{+}(f_{1}) + L_{+}(f_{2}) \leqslant L_{+}(f_{1} + f_{2})$。为证相反的不等式，取 $g \in C_{0}(X)$，使 $0 \leqslant g \leqslant f_{1} + f_{2}$。令

 
$$
g_{1}=g\wedge f_{1},\;g_{2}=g-g_{1},
$$
 

则 $g_{1},g_{2}\in C_{0}(X),0\leqslant g_{1}\leqslant f_{1},0\leqslant g_{2}\leqslant f_{2}.$ 于是有

 
$$
L(g)=L(g_{1})+L(g_{2})\leqslant L_{+}(f_{1})+L_{+}(f_{2}),
$$
 

由此得 $L_{+}(f_{1}+f_{2})\leqslant L_{+}(f_{1})+L_{+}(f_{2})$。故(5.4.2)式得证。

设 $f \in C_0(X)$，令

 
$$
L_{+}(f)=L_{+}(f^{+})-L_{+}(f^{-}),
$$
 

则 $L_{+}$为 $C_{0}(X)$上的线性泛函，且有

 
$$
|L_{+}(f)|\leqslant L_{+}(f^{+})\vee L_{+}(f^{-})\leqslant\|L\|\|f\|_{\infty},
$$
 

于是 $L_{+}$为连续线性泛函. 最后, 令 $L_{-}=L_{+}-L$, 则 $L_{-}$为连续线性泛函, 并由(5.4.1)式知: 对 $f\in C_{0}(X)_{+}, L_{-}(f)\geq0$. 从而 $L_{-}$为正泛函.

定理5.4.3 设X为一局部紧Hausdorff空间. 令 $\mathcal{M}_r(X,\mathcal{B}(X))$表示 $\mathcal{B}(X)$上的有限正则符号测度全体. 对 $\mu\in\mathcal{M}_r(X,\mathcal{B}(X))$, 令

 
$$
L_{\mu}(f)=\int f d\mu,f\in C_{0}(X),
$$
 

则 $\mu\mapsto L_{\mu}$为从 $\mathcal{M}_{r}(X,\mathcal{B}(X))$到 $C_{0}(X)^{*}$上的保范同构映射.

---

证 设  $\mu \in \mathcal{M}_r(X, \mathcal{B}(X))$，显然有  $L_\mu \in C_0(X)^*$，且

 
$$
\|L_{\mu}(f)\|_{\infty}\leqslant\|\mu\|_{\mathrm{v a r}}\|f\|_{\infty},\ f\in C_{0}(X),
$$
 

于是有 $\|L_\mu\|\leq\|\mu\|_{\mathrm{var}}.$ 往证等号成立. 设 $X=D\cup D^c$为 $\mu$的Jordan分解, 即 $\mu^+(A)=\mu(A\cap D),\mu^-(A)=-\mu(A\cap D^c)$. 对任给 $\varepsilon>0$, 由 $\mu^+$及 $\mu^-$的正则性及定理5.3.5, 存在紧集 $K_1\subset D$及紧集 $K_2\subset D^c$, 使得

 
$$
\mu(K_{1})-\mu(K_{2})=|\mu|\left(K_{1}\cup K_{2}\right)>|\mu|(X)-\varepsilon=\|\mu\|_{\mathrm{var}}-\varepsilon.
$$
 

另一方面，由命题5.1.23，存在 $f\in C_{c}(X)$，使 $\|f\|_{\infty}=1$，且

 
$$
f I_{K_{1}\cup K_{2}}=I_{K_{1}}-I_{K_{2}}.
$$
 

于是我们有

 
$$
\begin{align*}\|L_{\mu}\|\geq L_{\mu}(f)&=\int f d\mu=\int f I_{K_{1}\cup K_{2}}d\mu+\int f I_{(K_{1}\cup K_{2})^{c}}d\mu\\&\geq\mu(K_{1})-\mu(K_{2})-|\mu|((K_{1}\cup K_{2})^{c})>\|\mu\|_{\mathrm{var}}-2\varepsilon.\end{align*}
$$
 

由于 $\varepsilon > 0$是任意的，故有 $\|L_\mu\| \geq \|\mu\|_{\mathrm{var}}$，从而有 $\|L_\mu\| = \|\mu\|_{\mathrm{var}}$。

现在证明映射$\mu \mapsto L_\mu$是$\mathcal{M}_r(X, \mathcal{B}(X))$到$C_0(X)^*$的满射。为此，设$L \in C_0(X)^*,$即设$L$为$C_0(X)$上的一连续线性泛函。由引理5.4.2，存在$C_0(X)$上的两个正连续线性泛函$L_+$及$L_-$，使得 $L = L_+ - L_-$。$L_+$及$L_-$限于$C_c(X)$为正线性泛函，故由 Riesz 表现定理 (定理5.2.8(2))，存在$\mathcal{B}(X)$上的 Radon 测度$\mu_1$及$\mu_2$，使得 $\forall f \in C_c(X)$，有 $L_+(f) = \int f d\mu_1, L_-(f) = \int f d\mu_2$。习题5.3.1蕴含

 
$$
\mu_{1}(X)=\sup\{L_{+}(f)\mid f\in C_{c}(X),0\leqslant f\leqslant1\}\leqslant\|L_{+}\|<\infty,
$$
 

同理 $\mu_2(X) < \infty$，故 $\mu = \mu_1 - \mu_2 \in \mathcal{M}_r(X, \mathcal{B}(X))$。显然有 $L = L_\mu$，且映射 $\mu \mapsto L_\mu$是线性的。

##### 习题

5.4.1 设X为一局部紧Hausdorff空间，令 $X^{\Delta}$为X的单点紧化(见5.1.11)，对X上的函数f，定义

 
$$
f_{\Delta}(x)=\left\{\begin{aligned}{}&{{}f(x),}&{\quad}&{{}x\in X,}\\ {}&{{}0,}&{\quad}&{{}x=\Delta,}\\ \end{aligned}\right.
$$
 

则为要 $f \in C_0(X)$，必须且只需 $f_\Delta$为 $X^\Delta$上的连续函数。

5.4.2 设X为一具可数基的局部紧Hausdorff空间，则 $C_{0}(X)$为一可分Banach空间(提示：先考虑X为紧空间情形，然后利用习题5.4.1).

---

### 5.5 用连续函数逼近可测函数

在许多情况下, 连续函数比可测函数容易处理, 本节介绍有关用连续函数逼近可测函数的一些结果.

下一定理的一个特殊情形见习题3.4.2.

定理5.5.1 设X为一局部紧Hausdorff空间，A为包含B(X)的一σ代数，μ为A上的一Radon测度. 令1≤p＜∞，则C_{c}(X)在L^{p}(X,A,μ)中稠密.

证 显然$C_c(X) \subset L^p(X, \mathcal{A}, \mu)$。由于$L^p(X, \mathcal{A}, \mu)$中的简单函数在$L^p(X, \mathcal{A}, \mu)$中稠密(见引理3.4.7)，故为证定理只需证明如下事实：若$A \in \mathcal{A}, \mu(A) < \infty$，则有$f \in C_c(X)$，使$\|I_A - f\|_p$任意小。为此，设$\varepsilon > 0$，由$\mu$的外正则性，先取开集$U \supset A$，使$\mu(U) < \mu(A) + \varepsilon$，再由定理5.3.5，取一紧集$K \subset A$，使$\mu(K) > \mu(A) - \varepsilon$。由命题5.1.20(2)，存在$f \in C_c(X)$，使$I_K \leqslant f \leqslant I_U$，则$|I_A - f| \leqslant I_U - I_K$，故有

 
$$
\|I_{A}-f\|_{p}\leqslant\|I_{U}-I_{K}\|_{p}=\mu(U-K)^{\frac{1}{p}}<\left(2\varepsilon\right)^{\frac{1}{p}}.
$$
 

定理得证.

下一定理称为Lusin定理.

定理5.5.2 设X为一Hausdorff空间，A为包含B(X)的一σ代数，μ为A上的一正则测度，f为X上的一A可测实值函数。如果A∈A，0＜μ(A)＜∞，则V∈σ＞0，存在紧集K⊂A，使μ(A∖K)＜ε，且f限于K连续。若进一步，X为局部紧，则存在g∈Cₑ(X)，使g与f在K上一致，且使

$$
\sup\{|g(x)||x\in X\}\leqslant\sup\{|f(x)||x\in A\}.   \tag*{(5.5.1)}
$$

证 首先设$f$只取可数多个值，即$f = \sum_{i=1}^{\infty} a_i I_{A_i}$，其中$a_i \neq a_j$，$A_i \cap A_j = \varnothing$，$i \neq j$，且$\sum_{i} A_i = X$。取正整数$n$，使得$\mu(A \cap (\sum_{i=1}^{n} A_i)^c) < \varepsilon/2$。由定理5.3.5，存在$A \cap A_1, \cdots, A \cap A_n$的紧子集$K_1, \cdots, K_n$，使得$\sum_{i=1}^{n} \mu((A \cap A_i) \setminus K_i) < \varepsilon/2$。令$K = \sum_{i=1}^{n} K_i$，则$K$为$A$的紧子集，且有

 
$$
\begin{align*}\mu(A\setminus K)&=\mu\Big(A\cap(\sum_{i=1}^{n}A_{i})^{c}\Big)+\sum_{i=1}^{n}\mu((A\cap A_{i})\setminus K_{i})\\&<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.\end{align*}
$$
 

由于 f 限于每个  $K_{i}$ 为常数，从而 f 限于 K 为连续（见习题 5.1.1）.

现设f为任一实值A可测函数, 令

 
$$
f_{n}(x)=\frac{k}{2^{n}}, 若 \frac{k}{2^{n}}\leqslant f(x)<\frac{k+1}{2^{n}},\quad k=0,\pm1,\pm2,\cdots
$$
 

---

由前所证，对每个 $n \geq 1$，存在紧集 $K_n \subset A$，使 $\mu(A \setminus K_n) < \varepsilon/2^n$，且 $f_n$限于 $K_n$为连续。令 $K = \bigcap_n K_n$，则由于 $f$是 $(f_n)$的一致极限，故 $f$限于 $K$连续，此外有

 
$$
\mu(A\setminus K)\leqslant\sum_{n}\mu(A\setminus K_{n})<\varepsilon.
$$
 

最后证明定理的第二部分. 假定X为局部紧Hausdorff空间, 令 $X^{\Delta} = X \cup \{\Delta\}$为X的单点紧化, 则 $X^{\Delta}$是正规空间(见命题5.1.19). 故由Tietze扩张定理, 存在 $X^{\Delta}$上的连续函数 $h^*$, 使 $h^*$在K上与f一致, 且使

 
$$
\sup\{|h^{*}(x)||x\in X\}=\sup\{|f(x)||x\in K\}.
$$
 

取 $p \in C_c(X)$，使得 $I_K \leqslant p \leqslant 1$（见命题5.1.20(2)），并令 $g = ph$，其中 $h$为 $h^*$在 $X$上的限制，则 $g \in C_c(X)$， $g$与 $f$在 $K$上一致，且(5.5.1)式成立。

##### 习题

5.5.1 设X为一Hausdorff空间，A为包含B(X)的一σ代数，μ为A上的一有限正则测度，f为X上的一实值函数. 证明下列三断言等价：

(1)  $f$ 为  $\overline{A}^\mu$ 可测 (即  $\overline{B}(X)^\mu$ 可测, 见习题 5.3.2);

(2)  $\forall A \in \mathcal{A}, \forall \varepsilon > 0$, 存在紧集  $K \subset A$, 使  $\mu(A \setminus K) < \varepsilon$, 且  $f$ 限于  $K$ 连续;

(3) 存在X的划分:  $X = (\sum_{n} K_{n}) \cup N$，其中每个 $K_{n}$为紧集，N为 $\mu$零测集，使得f限于每个 $K_{n}$为连续函数.

5.5.2 设$f$为$\mathbb{R}$上的实函数，且对一切$a,b\in\mathbb{R}$，有$f(a+b)=f(a)+f(b)$。试证：(1)$f$在$\mathbb{R}$上连续当且仅当它在一点连续；(2)若$f$为Lebesgue可测，则$f$连续(提示：利用Lusin定理)。

## 5.6 乘积拓扑空间上的测度与积分

本节研究的中心问题是：给定两个局部紧Hausdorff空间X和Y，以及其上的两个Radon测度μ和ν，如何在乘积拓扑空间X × Y上构造一Radon测度μ × ν，使其在X及Y上的边缘测度分别是μ及ν？进一步，是否有相应的Fubini定理？这里遇到的困难是：μ及ν一般并非σ有限，且B(X) × B(Y)一般严格比B(X × Y)小。因此，第四章的结果不再适用。为了克服这一困难，我们将求助于Riesz表示定理。

下面首先研究拓扑空间的乘积.

定义5.6.1 设 $(X_{1},\mathcal{G}_{1}),\cdots,(X_{n},\mathcal{G}_{n})$为拓扑空间，令 $X=X_{1}\times X_{2}\times\cdots\times X_{n}$

 
$$
\mathcal{B}=\{U_{1}\times U_{2}\times\cdots\times U_{n}\mid U_{i}\in\mathcal{G}_{i},i=1,2,\cdots,n\},
$$
 

则 $\mathcal{B}$对有限交运算封闭．以 $\mathcal{B}$为基的拓扑 $\mathcal{G}$称为 $X$的乘积拓扑；称 $(X,\mathcal{G})$为 $\{(X_i,\mathcal{G}_i), 1 \leqslant i \leqslant n\}$的乘积拓扑空间．

---

令 $\mathcal{B}_0 = \{\pi_i^{-1}(U_i) \mid U_i \in \mathcal{G}_i, i = 1, 2, \cdots, n\}$，其中 $\pi_i$为 $X$到 $X_i$的投影映射，则易见 $\mathcal{B}_0$为 $\mathcal{G}$的子基，且 $\mathcal{G}$是使每个投影映射为连续的最小拓扑。

定义5.6.2 设 $\{(X_{\alpha},\mathcal{G}_{\alpha}),\alpha\in\Lambda\}$为一族拓扑空间， $X=\prod_{\alpha\in\Lambda}X_{\alpha}$， $\mathcal{G}$为X上使每个投影映射 $\pi_{\alpha}$为连续的最小拓扑，称 $(X,\mathcal{G})$为 $(X_{\alpha},\mathcal{G}_{\alpha}),\alpha\in\Lambda$的乘积拓扑空间.

设 $P_{0}$为 $\Lambda$的非空有穷子集全体，令

 
$$
\mathcal{B}=\bigcup_{S\in\mathcal{P}_{0}}\left\{\pi_{S}^{-1}\big(\prod_{i\in S}U_{i}\big)\mid U_{i}\in\mathcal{G}_{i},i\in S\right\},
$$
 

则易知B为拓扑G的基.

定理5.6.3 (Tychonoff定理) 设 $(X_{\alpha}, \mathcal{G}_{\alpha})$为一族紧拓扑空间，则其乘积拓扑空间 $(X, \mathcal{G})$亦为紧拓扑空间.

关于该定理的证明, 读者可以参看任何一本有关点集拓扑的书, 这里从略.

下面我们研究乘积拓扑空间上的Borel  $\sigma$ 代数. 为方便起见, 我们只讨论两个拓扑空间乘积情形. 关于集合和函数的截口概念见4.2节.

引理5.6.4 设X及Y为Hausdorff空间,  $X \times Y$ 为其乘积拓扑空间(也是Hausdorff空间).

(1) 我们有  $\mathcal{B}(X) \times \mathcal{B}(Y) \subset \mathcal{B}(X \times Y)$. 若 X 及 Y 都有可数基, 则  $\mathcal{B}(X) \times \mathcal{B}(Y) = \mathcal{B}(X \times Y)$;

(2) 设  $E \in \mathcal{B}(X \times Y)$，则对每个  $x \in X$ 及每个  $y \in Y$，有  $E_x \in \mathcal{B}(Y)$， $E^y \in \mathcal{B}(X)$。这里  $E_x = \{y \in Y \mid (x, y) \in E\}$， $E^y = \{x \in X \mid (x, y) \in E\}$；

(3) 设  $f$ 为  $X \times Y$ 上的  $\mathcal{B}(X \times Y)$ 可测函数，则对每个  $x \in X$ 及  $y \in Y$， $f_x$ 为  $Y$ 上的  $\mathcal{B}(Y)$ 可测函数， $f^y$ 为  $X$ 上的  $\mathcal{B}(X)$ 可测函数。这里记号  $f_x$ 及  $f^y$ 见定义4.2.1。

证 (1) 第一部分显然. 现设C及D分别为X及Y的可数基. 令 $\mathcal{H} = \{U \times V \mid U \in \mathcal{C}, V \in \mathcal{D}\}$, 则 $\mathcal{H}$为 $X \times Y$的可数基. 由于 $\mathcal{H} \subset \mathcal{B}(X) \times \mathcal{B}(Y)$, 且 $X \times Y$的每个开集为 $\mathcal{H}$中元素的可列并, 故有 $\mathcal{B}(X \times Y) \subset \mathcal{B}(X) \times \mathcal{B}(Y)$. 从而有 $\mathcal{B}(X \times Y) = \mathcal{B}(X) \times \mathcal{B}(Y)$.

(2) 设  $x \in X$，令  $g_x(y) = (x, y)$，则  $g_x$ 为  $Y$ 到  $X \times Y$ 上的连续函数，从而关于  $\mathcal{B}(Y)$ 及  $\mathcal{B}(X \times Y)$ 可测。但  $E_x = g^{-1}(E)$，故  $E_x \in \mathcal{B}(Y)$。同理可证  $E^y \in \mathcal{B}(X)$。

(3)注意： $(f_{x})^{-1}(B)=(f^{-1}(B))_{x},(f^{y})^{-1}(B)=(f^{-1}(B))^{y}$，故(3)由(2)推得. □

下一引理的证明留给读者完成.

引理5.6.5 设S及T为拓扑空间, T为紧空间. 令f为 $S \times T$上的实值连续函数. 则对任一 $s_0 \in S$及任一 $\varepsilon > 0$, 存在 $s_0$的一开邻域U, 使得对一切 $s \in U$及一切 $t \in T$, 有 $|f(s,t) - f(s_0,t)| < \varepsilon$.

命题5.6.6 设X及Y为局部紧Hausdorff空间,  $\mu$ 及 $\nu$分别为X及Y上的Radon测度, 令 $f\in C_{c}(X\times Y)$, 则

---

(1) 对任何  $x \in X, y \in Y$，有  $f_x \in C_c(Y), f^y \in C_c(X)$;

(2) 函数  $x \to \int_{Y} f(x, y) \nu(dy)$ 及  $y \to \int_{X} f(x, y) \mu(dx)$ 分别属于  $C_{c}(X)$ 及  $C_{c}(Y)$;

(3)  $\int_{X} \int_{Y} f(x,y)\nu(dy)\mu(dx) = \int_{Y} \int_{X} f(x,y)\mu(dx)\nu(dy).$

证 (1) 令  $K = \text{supp}(f)$，设  $K_1$ 及  $K_2$ 分别为  $K$ 在  $X$ 及  $Y$ 上的投影，则  $K_1$ 及  $K_2$ 为紧集。显然  $f_x$ 在  $Y$ 上连续，且  $\text{supp}(f_x) \subset K_2$，故  $f_x \in C_c(Y)$。同理  $f^y \in C_c(X)$。

(2) 分别对  $X \times K_{2}$ 及  $K_{1} \times Y$ 应用引理 5.6.5 即可推得 (2) 的结论 (注意  $\nu(K_{2}) < \infty, \mu(K_{1}) < \infty$).

(3) 对任给  $\varepsilon > 0$，由引理5.6.5知：对每个  $x \in K_1$，存在  $x$ 的开邻域  $U_x$，使对一切  $x' \in U_x$ 及一切  $y \in K_2$ 有  $|f(x', y) - f(x, y)| < \varepsilon$。由于  $K_1$ 为紧集，故存在  $K_1$ 的有限覆盖  $\{U_{x_1}, \cdots, U_{x_n}\}$。令  $(A_i, 1 \leqslant i \leqslant n)$ 为两两不交Borel集，使得  $A_i \subset U_{x_i}, 1 \leqslant i \leqslant n$，且  $\sum_{i=1}^n A_i = K_1$。令  $g(x, y) = \sum_{i=1}^n f(x_i, y) I_{A_i}(x)$，则容易验证

 
$$
\begin{align*}\int\int g(x,y)\mu(dx)\nu(dy)&=\int\int g(x,y)\nu(dy)\mu(dx)\\&=\sum_{i=1}^{n}\mu(A_{i})\int f(x_{i},y)\nu(dy).\end{align*}
$$
 

此外，f及g在 $K_{1}\times K_{2}$的余集上为0，且 $|f-g|<\varepsilon$。于是有

 
$$
\begin{aligned}&\left|\int\int f(x,y)\mu(dx)\nu(dy)-\int\int f(x,y)\nu(dy)\mu(dx)\right|\\ &\leqslant\left|\int\int(f(x,y)-g(x,y))\mu(dx)\nu(dy)\right|\\ &\quad+\left|\int\int(f(x,y)-g(x,y))\nu(dy)\mu(dx)\right|\\ &\leqslant2\varepsilon\mu(K_{1})\nu(K_{2}).\\ \end{aligned}
$$
 

由于 $\varepsilon>0$是任意的，故(3)得证.

命题5.6.6导致如下的定义.

定义5.6.7 设 $\mu$及 $\nu$分别为局部紧Hausdorff空间X及Y上的Radon测度. 由命题5.6.6(3)知, 可在 $C_{c}(X \times Y)$上定义一正线性泛函I:

 
$$
I(f)=\int\int f(x,y)\mu(dx)\nu(dy)=\int\int f(x,y)\nu(dy)\mu(dx).
$$
 

由于 $X \times Y$是局部紧Hausdorff空间，由Riesz表示定理知，有 $X \times Y$上唯一的Radon测度与 $I$对应。称此Radon测度为 $\mu$与 $\nu$的Radon乘积，记为 $\mu \times \nu$。

若X及Y都有可数基，则Radon乘积 $\mu \times \nu$即为通常的乘积测度(见习题5.6.5).

下面的任务是要证明与Radon乘积测度 $\mu \times \nu$有关的Fubini定理. 为此, 需要有关下半连续函数积分的一个结果.

---

引理5.6.8 设X为一局部紧Hausdorff空间，A为包含B(X)的一σ代数，μ为A上的一Radon测度。设H为一族非负下半连续函数，使得 $\forall h_1, h_2 \in \mathcal{H}$，存在 $h \in \mathcal{H}$，满足 $h \geq h_1 \vee h_2$。令

 
$$
f(x)=\sup\{h(x)\mid h\in\mathcal{H}\},x\in X,
$$
 

则  $\int f\,d\mu = \sup\{\int h\,d\mu \mid h \in \mathcal{H}\}$.

证 显然对  $h \in \mathcal{H}$ 有  $\int h \, d\mu \leqslant \int f \, d\mu$。为证引理，只需证：对任一实数  $a < \int f \, d\mu$，存在  $h \in \mathcal{H}$，使  $a < \int h \, d\mu$。为此，先用简单函数逼近  $f$。令  $U_{n,i} = [f > i/2^n]$，

 
$$
f_{n}=\frac{1}{2^{n}}\sum_{i=1}^{n2^{n}}I_{U_{n,i}}=\sum_{i=1}^{n2^{n}-1}\frac{i}{2^{n}}I_{\left[\frac{i}{2^{n}}<f\leqslant\frac{i+1}{2^{n}}\right]}+n I_{[f>n]},
$$
 

则$f_n$为Borel可测，$f_n \uparrow$，故有$\int f_n d\mu \uparrow \int f d\mu$。于是存在自然数$N$，使$\int f_N d\mu > a$。由于$\int f_N d\mu = \frac{1}{2^N} \sum_i \mu(U_N, i)$，由$\mu$的正则性，存在$U_N, i$的紧子集$K_i, i = 1, \cdots, N2^N$，使得$\frac{1}{2^N} \sum_i \mu(K_i) > a$。令$g = \frac{1}{2^N} \sum_{i=1}^{N2^N} I_{K_i}$，则对每个$x \in \bigcup_{i=1}^{N2^N} K_i$，有$g(x) \leqslant f_N(x) < f(x)$。于是由$f$的定义，对每个$x \in \bigcup_{i=1}^{N2^N} K_i$，存在$h_x \in \mathcal{H}$，使$g(x) < h_x(x)$。由于$h_x - g$为下半连续（见习题5.6.2），故存在$x$的一开邻域$U_x$，使对一切$y \in U_x$，有$h_x(y) - g(y) > 0$。现取$U_{x_1}, \cdots, U_{x_m}$，使$\bigcup_{i=1}^{m} U_{x_i} \supset \bigcup_{i=1}^{N2^N} K_i$，并取$h \in \mathcal{H}$，使$h \geqslant \bigvee_{i=1}^{m} h_{x_i}$，则$h \geqslant g$，从而有

 
$$
a<\frac{1}{2^{N}}\sum_{i=1}^{N2^{N}}\mu(K_{i})=\int g d\mu\leqslant\int h d\mu.
$$
 

引理得证.

命题5.6.9 设X及Y为局部紧Hausdorff空间, $\mu$及 $\nu$分别是X及Y上的Radon测度, $\mu\times\nu$为其Radon乘积.令U为 $X\times Y$的开子集,则

(1) 函数  $x \mapsto \nu(U_x)$ 及  $y \mapsto \mu(U^y)$ 为下半连续函数；

 
$$
(\mu\times\nu)(U)=\int_{X}\nu(U_{x})\mu(d x)=\int_{Y}\mu(U^{y})\nu(d y).
$$
 

证 $⑴$令

 
$$
\mathcal{H}_{x}=\{f_{x}\mid f\in C_{c}(X\times Y)\mid0\leqslant f\leqslant I_{U}\},
$$
 

 
$$
\mathcal{H}^{y}=\{f^{y}\mid f\in C_{c}(X\times Y)\mid0\leqslant f\leqslant I_{U}\},
$$
 

则 $\mathcal{H}_x \subset C_c(Y)$， $\mathcal{H}^y \subset C_c(X)$，且 $\mathcal{H}_x$及 $\mathcal{H}^y$满足引理5.6.8的条件。故由引理5.6.8得

$$
\nu(U_{x})=\sup\{\int_{Y}f_{x}d\nu\mid f_{x}\in\mathcal{H}_{x}\},   \tag*{(5.6.1)}
$$

$$
\mu(U^{y})=\sup\{\int_{X}f^{y}d\mu\mid f^{y}\in\mathcal{H}^{y}\}.   \tag*{(5.6.2)}
$$


---

但由命题5.6.6， $x \mapsto \int f_xd\nu$及 $y \mapsto \int f^yd\mu$是连续函数，故 $x \mapsto \nu(U_x)$及 $y \mapsto \mu(U^y)$是下半连续函数。

(2) 令  $\mathcal{H} = \{ f \in C_c(X \times Y) \mid 0 \leqslant f \leqslant I_U \}$，则相继由习题 5.3.1，引理 5.6.8 及 (5.6.1) 式得

 
$$
\begin{align*}(\mu\times\nu)(U)&=\sup_{f\in\mathcal{H}}\int_{X\times Y}f d(\mu\times\nu)\\&=\sup_{f\in\mathcal{H}}\int_{X}\int_{Y} f(x,y)\nu(dy)\mu(dx)\\&=\int_{X}(\sup_{f\in\mathcal{H}}\int_{Y} f_{x} d\nu)\mu(dx)\\&=\int_{X}\nu(U_{x})\mu(dx).\end{align*}
$$
 

(2)的第一部分得证. 同理可证(2)的另一半.

下一定理是有关Radon乘积测度 $\mu \times \nu$积分的Fubini定理.

定理5.6.10 设X及Y为局部紧Hausdorff空间，μ及ν分别为X及Y上的Radon测度，μ×ν为其Radon乘积. 设 $f \in L^{1}(X \times Y, \mathcal{B}(X \times Y), \mu \times \nu)$，且存在分别关于μ及ν为σ有限的Borel集 $X_{0}$及 $Y_{0}$，使f在 $X_{0} \times Y_{0}$的余集上为0，则

(1) 对  $\mu$-a.e. x,  $f_{x}$ 为  $\nu$ 可积，对  $\nu$-a.e. y,  $f^{y}$ 为  $\mu$ 可积；

(2) 令

 
$$
I_{f}(x)=\left\{\begin{aligned}&\int_{Y}f_{x}d\nu,& 若 f_{x}\in L^{1}(Y,\mathcal{B}(Y),\nu),\\ &0,& 其他情形 ;\end{aligned}\right.
$$
 

 
$$
I^{f}(y)=\left\{\begin{aligned}&\int_{X}f^{y}d\mu,\quad& 若 f^{y}\in L^{1}(X,\mathcal{B}(X),\mu),\\ &0,\quad& 其他情形 ,\end{aligned}\right.
$$
 

则 $I_{f}$为 $\mu$可积， $I^{f}$为 $\nu$可积，且有

 
$$
\int_{X\times Y}f d(\mu\times\nu)=\int_{X}I_{f}(x)\mu(d x)=\int_{Y}I^{f}(y)\nu(d y).
$$
 

证 首先假定  $E \in \mathcal{B}(X \times Y)$，并假定存在  $A \in \mathcal{B}(X)$， $B \in \mathcal{B}(Y)$，使  $\mu(A) < \infty, \nu(B) < \infty$，且  $E \subset A \times B$。往证：

(a) 函数  $x \mapsto \nu(E_x)$ 及  $y \mapsto \mu(E^y)$ 为 Borel 可测；

 
$$
(\mu\times\nu)(E)=\int_{X}\nu(E_{x})\mu(d x)=\int_{Y}\mu(E^{y})\nu(d y).
$$
 

由μ及ν的外正则性, 存在开集U ⊃ A及开集V ⊃ B, 使μ(U) < ∞, ν(V) < ∞. 令W = U × V,

 
$$
\mathcal{S}=\{D\in\mathcal{B}(X\times Y)\mid D\subset W,D 满足性质 (a) 及 (b)\},
$$
 

---

则易见S为W上的λ类.另一方面,由命题5.6.9, W的一切开子集属于S,故由单调类定理(定理1.2.2),  $S = \mathcal{B}(W) = W \cap \mathcal{B}(X)$ (后一等号见习题1.2.1). 特别,  $E \in S$.

由上所证容易推知：对  $E \in \mathcal{B}(X \times Y)$，假定存在关于  $\mu$ 的  $\sigma$ 有限集  $A \in \mathcal{B}(X)$ 及关于  $\nu$ 的  $\sigma$ 有限集  $B \in \mathcal{B}(Y)$，使  $E \subset A \times B$，则 E 满足性质(a)及(b)。于是，用通常的方法从简单函数过渡到非负可测函数，即可推得定理的结论。

##### 习题

5.6.1 设X为一拓扑空间，A为X的一子集，则为要 $I_{A}$为下半连续函数（相应地，上半连续函数），必须且只需A为开集（相应地，闭集）.

5.6.2 设X为一拓扑空间，f及g为下半连续函数，则 $f+g$为下半连续函数.

5.6.3 设  $X, Y, \mu, \nu$ 及  $\mu \times \nu$ 如定理 5.6.10. 令  $f$ 为  $X \times Y$ 上的非负下半连续函数，则

(1) 函数  $x \to \int f(x, y) \nu(dy)$ 及  $y \to \int f(x, y) \mu(dx)$ 为 Borel 可测；

 
$$
(2)\int f d(\mu\times\nu)=\int\int f(x,y)\nu(d y)\mu(d x)=\int\int f(x,y)\mu(d x)\nu(d y).
$$
 

5.6.4 设X及Y为具可数基的局部紧Hausdorff空间，μ及ν分别为X及Y上的Radon测度。则μ及ν为σ有限测度， $B(X \times Y) = B(X) \times B(Y)$，且 $B(X \times Y)$上通常意义下的乘积测度 $\mu \times \nu$就是Radon乘积测度。

5.6.5 设 $\{X_{n}, n \geqslant 1\}$为一列有可数基的拓扑空间，则 $\mathcal{B}(\prod_{n} X_{n}) = \prod_{n} \mathcal{B}(X_{n})$.

## 5.7 波兰空间上有限测度的正则性

波兰(Polish)空间是概率论中经常用到的一类拓扑空间. 本节介绍波兰空间的基本性质, 波兰空间上有限测度的正则性, 以及乘积波兰空间上概率测度族的投影极限. 有关波兰空间的进一步性质可参看Cohn (2013).

定义5.7.1 设X为Hausdorff空间. 如果存在X上与拓扑相容的距离 $\rho$，使 $(X,\rho)$为一完备可分距离空间，则称X为波兰空间.

命题5.7.2 设X为一波兰空间, F及U分别为X的非空闭子集和开子集. 则作为X的子空间, F及U都是波兰空间.

证 设  $\rho$ 为与拓扑相容的距离，使  $(X,\rho)$ 为一可分完备距离空间。显然，作为 X 的闭子空间， $(F,\rho)$ 为可分且完备的，故 F 为波兰空间。

下面证明U为波兰空间. 为此, 设U不等于全空间. 在U上定义 $\rho_{0}(x,y)$如下

 
$$
\rho_{0}(x,y)=\rho(x,y)+\left|\frac{1}{\rho(x,U^{c})}-\frac{1}{\rho(y,U^{c})}\right|,
$$
 

其中

 
$$
\rho(x,U^{c})=\inf\{\rho(x,z)\mid z\in U^{c}\}.
$$
 

---

容易看出： $\rho_{0}$ 定义了 U 上的一个距离，且 U 中序列  $\{x_{n}\}$ 按  $\rho_{0}$ 收敛于 U 中的点 x 等价于  $\{x_{n}\}$ 按  $\rho$ 收敛于 x 。这表明：距离  $\rho_{0}$ 与 U 的拓扑相容。特别， $(U, \rho_{0})$ 是可分的。

现证$(U,\rho_0)$是完备距离空间．设$(x_n)$是$U$中序列，且按$\rho_0$为基本列．依$\rho_0$的定义知，$(x_n)$按距离$\rho$亦为基本列．故由$(X,\rho)$的完备性，存在$x\in X$，使$\rho(x_n,x)\to0,n\to\infty$．$x$必属于$U$．因为否则的话，有$\lim_{n\to\infty}\rho(x_n,U^c)=0$，这将导致$\limsup_{n,m\to\infty}\rho_0(x_n,x_m)=\infty$，这与假定$(x_n)$关于$\rho_0$为基本列矛盾．既然$x\in U$，由$\rho(x_n,x)\to0$推出$\rho_0(x_n,x)\to0,(U,\rho_0)$的完备性得证．因此，$U$为波兰空间．

##### 命题5.7.3 具可数基的局部紧Hausdorff空间是波兰空间.

证 设X为一具可数基的局部紧Hausdorff空间，令 $X^{\triangle}$为其单点紧化，则 $X^{\triangle}$为具可数基的紧Hausdorff空间。从而存在 $X^{\triangle}$上一与拓扑相容的距离 $\rho$，使 $(X^{\triangle},\rho)$为可分紧距离空间(习题5.1.11)。但紧距离空间显然是完备的，故 $X^{\triangle}$为波兰空间。由于X是 $X^{\triangle}$中的开子集，故由命题5.7.2知，X为波兰空间。

命题5.7.4 设 $X_{1}, X_{2}, \cdots$为波兰空间的有限或可数序列，则其乘积空间 $\prod_{n} X_{n}$为波兰空间，序列的不交并 $\sum X_{n}$也为波兰空间.

证 设 $d_{n}$为 $X_{n}$上的与拓扑相容的距离，使 $(X_{n},d_{n})$为可分完备距离空间。不妨设对一切 $x,y\in X_{n}$，有 $d_{n}(x,y)\leqslant1$（否则令 $d_{n}^{\prime}(x,y)=d_{n}(x,y)\wedge1$，则 $d_{n}^{\prime}$与 $d_{n}$等价，且 $(X_{n},d_{n}^{\prime})$仍完备）。令

 
$$
d(x,y)=\sum_{n}\frac{1}{2^{n}}d_{n}(x_{n},y_{n}),
$$
 

其中 $x,y\in\prod_{n}X_{n}$，则 $d$为 $\prod_{n}X_{n}$上与拓扑相容的距离，且 $\left(\prod_{n}X_{n},d\right)$为可分完备距离空间。因此， $\prod_{n}X_{n}$为波兰空间。

对每个n，令 $D_{n}$是 $X_{n}$的可数稠子集， $d_{n}$是 $X_{n}$的完备化距离，满足 $\forall x,y\in X_{n}$，有 $d_{n}(x,y)\leq1$。则 $\sum_{n}D_{n}$是 $\sum_{n}X_{n}$的可数稠子集。令

 
$$
d(x,y)=\left\{\begin{aligned}&d_{n}(x,y),&\quad&\exists n,x,y\in G_{n},\\ &1,&\quad&x\in G_{m},y\in G_{n},m\neq n,\end{aligned}\right.
$$
 

则d定义了 $\sum_{n}X_{n}$上一个完备化距离，从而 $\sum_{n}X_{n}$为波兰空间.

下一命题推广了命题5.7.2.

命题5.7.5 设X为一波兰空间, Y为X的一子空间, 则Y为波兰空间, 当且仅当它是 $G_{\delta}$集. 这里G表示X的开子集全体.

证 充分性.设 $Y=\bigcap_{n}U_{n}$，其中每个 $U_{n}$为X的开子集.由于每个 $U_{n}$为波兰空

---

间(命题5.7.2)，故 $\prod U_{n}$为波兰空间(命题5.7.4).令

 
$$
\Delta=\left\{u=(u_{1},u_{2},\cdots)\in\prod_{n}U_{n}\Bigm|u_{j}=u_{k},\forall j,k\geqslant1\right\},
$$
 

则 $\Delta$为 $\prod U_n$中的闭集，从而为波兰空间(命题5.7.2)。令

 
$$
i(y)=(y,y,\cdots),y\in\bigcap_{n}U_{n}=Y,
$$
 

则i为Y到 $\Delta$的同胚映射. 故Y是波兰空间.

必要性．设Y为X的波兰子空间，d及 $d_{0}$分别是X及Y上与拓扑相容的距离，使其为可分完备距离空间．设V为Y的子集，我们用 $d_{0}(V)$表示V在 $d_{0}$下的直径，即 $d_{0}(V)=\sup_{x,y\in V}d_{0}(x,y)$．令

 
$$
V_{n}=\bigcup\left\{W\mid W\in\mathcal{G},W\cap Y\neq\varnothing,d_{0}(W\cap Y)\leqslant1/n\right\},\ n\geqslant1,
$$
 

则每个 $V_{n}$为开集. 往证

$$
Y=\overline{Y}\cap\bigcap_{n}V_{n}.   \tag*{(5.7.1)}
$$

由于$d$与$d_0$在$Y$上诱导同一拓扑，故易见$Y \subset \overline{Y} \cap (\bigcap_n V_n)$。再证相反的包含关系。设$x \in \overline{Y} \cap (\bigcap_n V_n)$，则由$V_n$的定义知，对每个$n$，存在$x$的开邻域$W_n$，使$W_n \cap Y \neq \varnothing$，且$d_0(W_n \cap Y) \leqslant 1/n$。不妨设$(W_n)$是单调下降的集列。另一方面，对每个$n$，存在$x$的开邻域$G_n$，使$d(G_n) \leqslant 1/n$，不妨设$(G_n)$也是单调下降的。由于$x \in \overline{Y}$，故$G_n \cap Y \neq \varnothing$。令$U_n = W_n \cap G_n$，则对每个$n$，有

 
$$
x\in U_{n},\ U_{n}\cap Y\neq\varnothing,\ d(U_{n})\leqslant\frac{1}{n},\ d_{0}(U_{n}\cap Y)\leqslant\frac{1}{n}.
$$
 

由于$(Y,d_0)$完备，$U_n \cap Y$单调下降，故存在唯一的$y \in Y$，使$\bigcap_n F_n = \{y\}$（Cantor定理），这里$F_n$为$U_n \cap Y$在$Y$中的闭包。另一方面，由于$(X,d)$是完备的，$U_n$单调下降，且$x \in U_n, n \geq 1$，故$\bigcap_n \overline{U}_n = \{x\}$。但显然有$F_n \subset \overline{U}_n \cap Y$（因后者是$Y$中闭集，且包含$U_n \cap Y$），故$y \in \bigcap_n \overline{U}_n$，从而$y = x$，特别，有$x \in Y$。因此，我们证明了$\overline{Y} \cap (\bigcap_n V_n) \subset Y$。（5.7.1）式得证。由（5.7.1）式知：$Y$为$\mathcal{G}_\delta$集（因$\overline{Y}$作为距离空间$X$中的闭集是$\mathcal{G}_\delta$集，$\bigcap_n V_n$也是$\mathcal{G}_\delta$集）。

定理5.7.6 设X为一波兰空间, $\mu$为 $\mathcal{B}(X)$上的一有限测度,则 $\mu$为正则的.

证 令  $\rho$ 为 X 上与拓扑相容的距离，使  $(X, \rho)$ 为一可分完备距离空间。由定理 5.3.6，为证  $\mu$ 的正则性，只需证： $\forall A \in \mathcal{B}(X)$，有

$$
\mu(A)=\sup\{\mu(K)\mid K\subset A,\;K\in\mathcal{K}\}.   \tag*{(5.7.2)}
$$


---

设$\{x_n\}$为$X$的一个可数稠子集，令$B(x,\delta)$表示以$x$为球心，半径为$\delta$的开球．由于$X=\bigcup_{k=1}^\infty B(x_k,1/n)$，故对任给$\varepsilon>0$，存在正整数$k_n$，使

 
$$
\mu\Big(\bigcup_{j=1}^{k_{n}}B(x_{j},\frac{1}{n})\Big)>\mu(X)-\frac{\varepsilon}{2^{n}},\quad n\geqslant1.
$$
 

令K为全有界集 $\bigcap_{n=1}^{\infty}\bigcup_{j=1}^{\infty}B(x_{j},1/n)$的闭包，则K为紧集(因 $(X,\rho)$为完备的).我们有

 
$$
\mu(K^{c})\leqslant\sum_{n}\mu\Big(\big(\bigcup_{j=1}^{k_{n}}B(x_{j},\frac{1}{n})\big)^{c}\Big)<\sum_{n}\frac{\varepsilon}{2^{n}}=\varepsilon,
$$
 

即有$\mu(K) > \mu(X) - \varepsilon$. 但$\varepsilon > 0$是任意的, 故(5.7.2)式对$A = X$成立. 现设$A \in \mathcal{B}(X)$, 对任给$\varepsilon > 0$, 先取紧集$K$, 使$\mu(K^c) < \varepsilon$. 此外, 由系5.3.4知, 存在$A$的闭子集$F$, 使$\mu(F) > \mu(A) - \varepsilon$. 令$K_1 = K \cap F$, 则$K_1$为紧集, $K_1 \subset A$, 且有$\mu(K_1) > \mu(A) - 2\varepsilon$, 故(5.7.2)式得证.

需要指出: 在定理5.7.6中, 如果 $\mu$不有限(即使有 $\mu(K) < \infty, \forall K \in \mathcal{K}$), 则 $\mu$不一定正则. 例如, 设 $X$不是 $\sigma$紧的波兰空间,  $\forall B \in \mathcal{B}(X)$, 若 $B$为 $\sigma$有界集, 令 $\mu(B) = 0$, 否则令 $\mu(B) = \infty$, 则(5.7.2)式对 $A = X$不成立.

定义5.7.7 设X为Hausdorff空间. 令M表示B(X)上有限测度全体,  $\bigcap_{\mu\in\mathcal{M}}\overline{B}(X)^{\mu}$ 中的集称为普遍可测集.

定义5.7.8 设 $(E,\mathcal{E})$为一可分可离可测空间. 如果存在R的一Borel可测集(相应地,普遍可测集)A, 使 $(E,\mathcal{E})$与 $(A,\mathcal{B}(A))$同构, 则称 $(E,\mathcal{E})$为Lusin可测空间(相应地, Radon可测空间).

可以证明：设A为波兰空间X的Borel可测集(相应地,普遍可测集),则 $(A,\mathcal{B}(A))$为Lusin可测空间(相应地,Radon可测空间)(参见Cohn(2013)).

令X为波兰空间. X的子集A称为解析集, 如果存在波兰空间Z和一连续函数f:  $Z \longrightarrow X$, 使得 $f(Z) = A$. 由命题5.7.2知, 波兰空间的开子集和闭子集都是解析集.

命题5.7.9 令X为波兰空间, $\{A_{1},A_{2},\cdots\}$为X的解析子集.则 $\bigcup_{k}A_{k}$和 $\bigcap_{k}A_{k}$都是解析集.

证 对每个k，选择波兰空间 $Z_{k}$和连续函数 $f_{k}:Z_{k}\longrightarrow X$，使得 $f_{k}(Z_{k})=A_{k}$。令 $Z=\sum_{n}Z_{n}$为空间 $\{Z_{1},Z_{2},\cdots\}$的不交并，则Z是波兰空间(命题5.7.4)。定义 $f:Z\longrightarrow X$，使得对于每个k在 $Z_{k}$上与 $f_{k}$一致。则f是一个连续函数， $f(Z)=\bigcup_{k}A_{k}$，因此 $\bigcup_{k}A_{k}$是解析集。

下面考虑乘积空间 $\prod Z_{k}$，它是波兰空间(命题5.7.4). 令

 
$$
Y=\{\{z_{k}\}\in\prod_{k}Z_{k}:\forall i,j,f_{i}(z_{i})=f_{j}(z_{j})\},
$$
 

---

则 $Y$是 $\prod_{k} Z_k$的一个闭子空间，从而 $Y$是波兰空间(命题5.7.2)。容易看出： $\bigcap_k A_k = \{f_1(z_1) : \{z_k\} \in Y\}$，从而作为波兰空间 $Y$在连续映射下的像集， $\bigcap_k A_k$是解析集。

命题5.7.10 设 $X_{1}, X_{2}, \cdots$ 为波兰空间的有限或可数序列. 对每个 $k,$ 令 $A_{k}$ 为 $X_{k}$ 的非空解析子集, 则 $\prod A_{k}$ 是乘积空间 $\prod X_{k}$ 的一个解析子集.

证 对每个k，选择波兰空间 $Z_{k}$和连续函数 $f_{k}:Z_{k}\longrightarrow X_{k}$，使得 $f_{k}(Z_{k})=A_{k}$.通过 $f(\{z_{k}\})=\{f_{k}(z_{k})\}$定义函数 $f:\prod_{k}Z_{k}\longrightarrow\prod_{k}X_{k}$，则f是连续的，并且 $f(\prod_{k}Z_{k})=\prod_{k}A_{k}$，因此 $\prod_{n}X_{n}$是解析集.

可以证明：解析集是普遍可测集；解析集的余集不一定是解析集；当且仅当解析集A的余集也是解析集时A是Borel集(参见Cohn (2013)).

##### 习题

5.7.1 设X为R中无理数全体，则X按R诱导出的拓扑为波兰空间.

5.7.2 设E为一波兰空间X的普遍可测集，则 $\mathcal{B}(E)$上的任何有限测度 $\mu$为紧测度.更确切地说，令 $\mathcal{K}(E)$表示含于E的全体紧集，则对任何 $A\in\mathcal{B}(E)$，有

 
$$
\mu(A)=\sup\{\mu(C)\mid C\subset A,C\in\mathcal{K}(E)\}.
$$
 

5.7.3 设E为一波兰空间X的Borel可测集，令 $\mathcal{E}=\mathcal{B}(E)$，则可测空间 $(E,\mathcal{E})$满足定理4.7.9的条件.

## 5.8 Haar测度

容易看出， $R^{d}$ 上的Lebesgue测度是平移不变的： $\lambda(A+x)=\lambda(A)$ 对于  $\mathcal{B}(\mathbb{R}^{d})$ 中的每个  $A$ 和  $R^{d}$ 中的每个  $x$ 都成立。可以证明，不计常数乘子，Lebesgue测度是  $R^{d}$ 上的唯一平移不变测度。在本章我们将证明：局部紧拓扑群上存在与  $R^{d}$ 上的Lebesgue测度类似的测度（称为Haar测度），并且如果不计常数乘子，Haar测度是唯一的。5.8.1节介绍拓扑群的基本定义和事实；5.8.2节给出Haar测度存在性和唯一性的证明；5.8.3节介绍Haar测度的其他基本性质。本节内容主要参考Cohn (2013)。

#### 5.8.1 拓扑群

拓扑群是一个具有群结构的拓扑空间$G$，其群运算是从乘积空间$G \times G$到$G$中的一个连续映射：$(x, y) \mapsto xy$。并且映射$x \mapsto x^{-1}$也是连续的。拓扑结构是局部紧和Hausdorff的拓扑群称为局部紧拓扑群。例如，具有通常的拓扑结构和加法运算的$\mathbb{R}^d$和$\mathbb{Z}^d$都是局部紧拓扑群。

命题5.8.1 令G为拓扑群，e为G的恒等元素，a为G的任意元素.

---

(1)  $x \mapsto ax$,  $x \mapsto xa$ 和  $x \mapsto x^{-1}$ 是 G 到 G 的同胚映射.

(2) 如果  $\mathcal{U}$ 是  $e$ 的邻域基，则  $\{aU : U \in \mathcal{U}\}$ 和  $\{Ua : U \in \mathcal{U}\}$ 是  $a$ 的邻域基。

(3) 如果 K 和 L 是 G 的紧子集，则 aK, Ka, KL 和  $K^{-1}$ 是 G 的紧子集.

证 (1)由拓扑群的定义推知，(2)是(1)的直接推论，(3)是基于如下事实：在连续映射下紧集的像是紧的， $K \times L$ 的紧性由 Tychonoff定理(定理5.6.3)推知. ☐

命题5.8.2 令G为拓扑群, e为G的恒等元素, U为e的一个开邻域.

(1) 存在一个 e 的开放邻域 V，使得  $V V \subset U$.

(2) U 中包含 e 的一个对称开邻域.

证 (1) 由于映射  $(x, y) \mapsto xy$ 是连续的，如下定义的集合  $W = \{(x, y) : xy \in U\}$ 是  $G \times G$ 中  $(e, e)$ 的开邻域。因此，存在满足  $V_1 \times V_2 \subset W$ 的 e 的邻域  $V_1$ 和  $V_2$。则  $V = V_1 \cap V_2$ 是满足  $VV \subset U$ 的 e 的开邻域。

(2) 映射  $x \mapsto x^{-1}$ 的连续性意味着，如果  $U$ 是一个  $e$ 的开邻域，则  $U^{-1}$ 也是  $e$ 的开邻域，从而  $U \cap U^{-1}$ 是  $U$ 中包含的  $e$ 的对称开邻域。

命题5.8.3 令G为拓扑群，K为G的紧子集，U为包含K的G的开子集．则存在e的 $V_R$和 $V_L$的邻域，使得 $KV_R \subset U$和 $V_L K \subset U$．

证　对于K中的每个x，选择e的开邻域 $W_x$和 $V_x$，使得 $xW_x \subset U$和 $V_xV_x \subset W_x$（见命题5.8.1和命题5.8.2）。则 $\{xV_x\}_{x \in K}$是紧集K一个开覆盖，从而在K中存在点的有限集合 $\{x_1, \cdots, x_n\}$，使得集类 $\{x_i V_xi, i = 1, \cdots, n\}$覆盖K。令 $V_R = \cap_{i=1}^n V_{xi}$。如果 $x \in K$，则存在i，使得 $x \in x_i V_{xi}$，所以有

 
$$
x V_{R}\subset x_{i}V_{x_{i}}V_{x_{i}}\subset x_{i}W_{x_{i}}\subset U.
$$
 

由于x是K的任意元素, 因此 $KV_{R} \subset U$.  $V_{L}$的构造是类似的.

令$G$为拓扑群，$f$为实值或复值函数。如果对每个正数$\varepsilon$，存在$e$的开邻域$U$，使得只要$x$和$y$属于$G$且满足$y \in xU$，就有$|f(x) - f(y)| < \varepsilon$，则称$f$是左一致连续。类似定义右一致连续。注意：我们可以用较小的$e$的对称邻域替换定义中出现的$e$的邻域（命题5.8.2），而关于此对称邻域$U$，条件$x \in yU$等价于条件$y \in Uy$等价于条件$y \in Ux$。因此，$x$和$y$实际上对称地进入我们的定义。

命题5.8.4 设G为局部紧拓扑群. $C_{c}(G)$中的每个函数是左一致连续和右一致连续的.

证 令  $f \in C_c(G)$， $K$ 为  $f$ 的紧支撑。设  $\varepsilon > 0$，对每个  $x \in K$，首先选择  $e$ 的一个开邻域  $U_x$，使得对任何  $y \in xU_x$，有  $|f(x) - f(y)| < \varepsilon/2$ 成立，然后选择  $e$ 的一个开邻域  $V_x$，使得  $V_xV_x \subset U_x$（见命题5.8.1和命题5.8.2）。集类  $\{xV_x\}_{x \in K}$ 是紧集  $K$ 的开覆盖，因此，存在一个有限集合  $\{x_1, \cdots, x_n\} \subset K$，使得集类  $\{x_iV_{x_i}, i = 1, \cdots, n\}$ 覆盖  $K$。设  $V \subset \cap_{i=1}^n V_xi$ 为  $e$ 的对称开邻域（命题5.8.2），我们将证明：如果  $x$ 和  $y$ 属于  $G$ 且满足  $y \in xV$，则  $|f(x) - f(y)| < \varepsilon$。

---

如果x和y都不属于K，则 $f(x)=f(y)=0$。现设 $x\in K$和 $y\in xV$，则存在某i，使得 $x\in x_iV_{x_i}$，从而x和y都属于 $x_iU_{x_i}$（请注意， $x\in x_iV_{x_i}\subset x_iU_{x_i}$和 $y\in xV_{x_i}\subset x_iV_{x_i}$  $V_{x_i}\subset x_iU_{x_i}$）。于是 $|f(x)-f(x_i)|<\varepsilon/2$和 $|f(y)-f(x_i)|<\varepsilon/2$。因此， $|f(x)-f(y)|<\varepsilon/2$。剩下要处理的情况是 $y\in K,y\in xV$。由于V是对称的，这正是 $y\in K,x\in yV$这种情况，按照刚刚处理的细节(x和y互换)就可以解决这个问题。f的左一致连续性得证。类似可证f的右一致连续性。

系5.8.5 令G为局部紧致群，μ为G上的Radon测度， $f \in C_c(G)$。则函数 $x \mapsto \int f(xy)\mu(dy)$和 $x \mapsto \int f(yx)\mu(dy)$是连续的。

证 我们只证函数  $x \mapsto \int f(xy)\mu(dy)$ 的连续性，类似可证  $x \mapsto \int f(yx)\mu(dy)$ 的连续性。设  $K$ 为  $f$ 的紧支撑。任取  $x_0 \in G$，令  $W$ 为  $x_0$ 的开邻域，其闭包  $\overline{W}$ 为紧集。容易证明，对  $W$ 中的每个  $x$，函数  $y \mapsto f(yx)$ 是连续的，并且在紧集  $K(\overline{W})^{-1}$ 之外为零。给定  $\varepsilon > 0$，取  $-\varepsilon' > 0$，使  $\varepsilon' \mu(K(\overline{W})^{-1}) < \varepsilon$，则利用  $f$ 的左一致连续性（命题5.8.4），选择  $e$ 的一个开邻域  $V$，使得对任何满足  $s \in tV$ 的  $s, t \in G$，有  $|f(s) - f(t)| < \varepsilon'$。于是对每个  $x \in W \cap x_0V$ 和  $y \in G$，我们有  $yx \in yx_0V$，从而

 
$$
\begin{align*}\Big|\int f(yx)\mu(dy)-\int f(yx_{0})\mu(dy)\Big|&\leq\int|f(yx)-f(yx_{0})|\mu(dy)\\&\leq\varepsilon^{\prime}\mu(K(\overline{W})^{-1})<\varepsilon.\end{align*}
$$
 

函数 $x \mapsto \int f(xy)\mu(dy)$在 $x_0$的连续性得证.

命题5.8.6 设G为拓扑群, H为G的开子群, 则H也是闭的.

证 我们有 $H^c = \cup_{x \in H^c} x H$。命题5.8.1蕴含每个 $x H$是开集，从而 $H^c$是开的，因此 $H$是闭的。

命题5.8.7 令G为局部紧群，则存在G的一个既开又闭且σ紧的子群H.

证 由于$G$是局部紧的，可以选择$e$的开邻域$U$，使得其闭包是紧的．利用命题5.8.2，选择含于$U$的一个$e$的对称开邻域$V$．当然，$\overline{V}$是紧的．令$V_1 = V$，归纳定义$V_n = V_{n-1}V, n \geq 2$，以及$H = \cup_n V_n$．如果$x \in V_m, y \in V_n$，则$xy \in V_{m+n}, x^{-1} \in V_m$（注意$V$是对称的）．因此，$H$是$G$的子群．很明显，$H$既开又闭的．由于$\overline{V}$是紧的，$H$是闭的，每个$V_n$的闭包是紧的，且包含在$H$中，从而$H$是$\sigma$紧的．

### 5.8.2 Haar测度的存在唯一性

令G为局部紧群， $\mu$为G上的非零Radon测度。如果 $\mu$按如下意义为左转换不变（相应地，右转换不变）： $\mu(xA) = \mu(A)$（相应地， $\mu(Ax) = \mu(A)$）对于G中的每个x和 $\mathcal{B}(G)$中的每个A成立，则称 $\mu$是左Haar测度（相应地，右Haar测度）。以下将左Haar测度简称为Haar测度，将左转换不变简称为转换不变。

在本节中, 我们将证明: 不计一个常数乘子, 在每个局部紧群上都存在唯一的左Haar测度. Haar测度的性质以及左、右Haar测度之间的关系将在5.8.3节讨论.

---

我们引进一些符号. 令G为群, x为G的元素, f是G上的一个函数. f的x左转换, 记为xf, 定义为 $x f(t) = f(x^{-1} t)$; f的x右转换, 记为 $f_{x}$, 定义为 $f_{x}(t) = f(tx^{-1})$. 函数 $\check{f}$由 $\check{f}(t) = f(t^{-1})$定义. 请注意, 如果x, y和t属于G, 则

 
$$
x y f(t)=f((x y)^{-1}t)=f(y^{-1}x^{-1}t)=_{y}f(x^{-1}t)=_{x}(_{y}f)(t);
$$
 

因此 $xyf=x(yf)$. 类似可证 $f_{xy}=(fx)_{y}$. 如果A是G的子集, 则集合A, xA 和Ax的示性函数由如下等式关联:  $(I_{A})_{x}=I_{Ax}, x(I_{A})=I_{xA}$.

如果G是局部紧群，并且 $\mu$是G上的左Haar测度，则由积分的线性性和单调收敛定理推知：对于每个非负或 $\mu$可积的Borel函数f，

 
$$
\int_{}^{}x f d\mu=\int f d\mu.
$$
 

令K为G的一紧子集，V为G的一子集，其内部 $V^0$是非空的。则 $\{xV^0\}_{x\in G}$是紧集K的一个开覆盖，故存在G元素的有限序列 $\{x_i\}_{i=1}^n$，使得 $K\subset\cup_{i=1}^n x_iV$。设 $\#(K:V)$是存在这样一个序列 $\{x_i\}_{i=1}^n$的最小非负整数n。显然，当且仅当 $K=\varnothing$时， $\#(K:V)=0$。

我们取一个内部为非空的紧集 $K_0$，它将用于度量 $G$的各个子集大小的标准。粗略地说，我们将通过计算当 $e$的开邻域 $U$变小时比率 $\#(K : U) / \#(K_0 : U)$的极限来度量 $G$的各个紧子集 $K$的大小，将使用此“极限”在 $G$上构造外测度 $\mu^*$，然后证明 $\mu^*$到 $\mathcal{B}(G)$的限制就是左Haar测度。

我们先准备两个引理.

引理5.8.8 令C为G的紧子集的全体, U是e的开邻域全体. 对于U中的每个U, 通过 $h_{U}(K)=\#(K:U)/\#(K_{0}:U)$ 定义 $h_{U}:C \mapsto R$. 则对所有U, K,  $K_{1}, K_{2}$ 和x, 如下关系成立:

(1)  $0 \leqslant h_{U}(K) \leqslant \#(K : K_{0}),$

(2) $h_{U}(K_{0})=1,$

(3)  $h_{U}(xK) = h_{U}(K)$,

(4) 如果  $K_1 \subset K_2$，则  $h_U(K_1) \leqslant h_U(K_2)$，

(5)  $h_U(K_1 \cup K_2) \leqslant h_U(K_1) + h_U(K_2)$,

(6) 如果  $K_1U^{-1} \cap K_2U^{-1} = \varnothing$，则  $h_U(K_1 \cup K_2) = h_U(K_1) + h_U(K_2)$.

证 令  $\{x_{i}\}_{i=1}^{m}$ 和  $\{y_{j}\}_{j=1}^{n}$ 是 G 中元素序列，使得  $K \subset \cup_{i=1}^{m} x_{i} K_{0}$ 和  $K_{0} \subset \cup_{j=1}^{n} y_{j} U$，则  $K \subset \cup_{i=1}^{m} \cup_{j=1}^{n} x_{i} y_{j} U$。于是

 
$$
\#(K:U)\leqslant\#(K:K_{0})\#(K_{0}:U)
$$
 

---

对所有K和U成立. 将上式两边除以 $\#(K_0:U)$即得断言(1). 断言(2)-(5)显然. 现在假定 $K_1U^{-1}\cap K_2U^{-1}=\varnothing$. 令 $\{x_i\}_{i=1}^n$是一个点序列, 使得

 
$$
n=\#(K_{1}\cup K_{2}:U),~K_{1}\cup K_{2}\subset\cup_{i=1}^{n}x_{i}U.
$$
 

每个集合 $x_iU$至多与 $K_1$和 $K_2$中之一有交集，因此可将序列 $\{x_i\}_{i=1}^n$划分为序列 $\{y_i\}_{i=1}^j$和 $\{zi\}_{i=1}^k$，使得 $K_1 \subset \cup_{i=1}^j y_iU$和 $K_2 \subset \cup_{i=1}^k z_iU$。于是有

 
$$
\#(K_{1}\cup K_{2}:U)\geqslant\#(K_{1}:U)+\#(K_{2}:U),
$$
 

从而 $h_{U}(K_{1}\cup K_{2})\geqslant h_{U}(K_{1})+h_{U}(K_{2})$，有鉴于(5)，我们推得(6).

下面将通过构建某个包含所有函数$h_U$的乘积空间，并利用紧性推理来定义函数$f\{h_U\}_{U\in\mathcal{U}}$的“极限”。对$C$中每个$K$，令$I(K)$为$\mathbb{R}$中的区间$[0,\#(K:K_0)]$。令$X$为乘积拓扑空间$\prod_{K\in\mathcal{C}}I(K)$。由于每个$I(K)$是紧的，Tychonoff定理(定理5.6.3)表明$X$是紧的。根据引理5.8.8的(1)，每个函数$h_U$都属于$X$。对于$e$的每个开邻域$V$，令$S(V)$为集合$\{h_U:U\in\mathcal{U},U\subset V\}$在$X$中的闭包。如果$V_1,\cdots,V_n$属于$\mathcal{U}$，并令$V=\cap_{i=1}^n V_i$，则$h_V\in\cap_{i=1}^n S(V_i)$；由于$V_1,\cdots,V_n$是任意的，这意味着闭集族$\{S(V)\}_{V\in\mathcal{U}}$满足有限交性质。$X$的紧性蕴含$\cap_{V\in\mathcal{U}}S(V)$非空。于是可以选择$\cap_{V\in\mathcal{U}}S(V)$中一元素$h_*\$为函数族$\{h_U\}_{U\in\mathcal{U}}$的“极限”。

引理5.8.9 对于G中的所有x和C中的任意K, $K_{1},K_{2}$，函数 $h_{*}$满足

(1)  $h_{*}(K) \geqslant 0,$

(2)  $h_{*}(\varnothing) = 0$,

(3)  $h_{*}(K_{0})=1,$

(4)  $h_{*}(xK) = h_{*}(K),$

(5) 如果  $K_1 \subset K_2$，则  $h_*(K_1) \leqslant h_*(K_2)$，

(6)  $h_{*}(K_{1} \cup K_{2}) \leqslant h_{*}(K_{1}) + h_{*}(K_{2}),$

(7) 如果  $K_1 \cap K_2 = \varnothing$，则  $h_*(K_1 \cup K_2) = h_*(K_1) + h_*(K_2)$.

证 (1)显然．下面先证(7)．回想X作为乘积空间 $\prod_{K\in C}I(K)$是C上的一族特定函数，其拓扑是使得每个G的紧子集K(即对于指标集C的每个元素K)，由 $h\mapsto h(K)$定义的从X到R中的投影是连续的．因此，对G的任意一对紧子集 $(K_1,K_2)$，如下定义的从X到R中的映射

$$
h\mapsto h(K_{1})+h(K_{2})-h(K_{1}\cup K_{2})   \tag*{(5.8.1)}
$$

是连续的. 此外, 由引理5.8.8的(5), 该映射在每个 $h_{U}$处是非负的, 故在每个集合 $S(V)$中的每个点都是非负的. 特别, 在 $h_{*}$处为非负, (6) 得证. 用类似推理可证(2)至(5).

往证(7). 假设 $K_{1}$和 $K_{2}$是G的不相交紧子集. 根据引理5.1.18, 存在不相交的开集 $U_{1}$和 $U_{2}$. 使得 $K_{1} \subset U_{1}$和 $K_{2} \subset U_{2}$, 并且根据命题5.8.3, 有e的开邻域 $V_{1}$和 $V_{2}$, 使

---

得 $K_1V_1 \subset U_1$和 $K_2V_2 \subset U_2$。令 $V = V_1 \cap V_2$，则 $K_1V \cap K_2V = \varnothing$，从而对于每个满足 $U \subset V^{-1}$的 $U \in \mathcal{U}$，有

 
$$
h_{U}(K_{1}\cup K_{2})=h_{U}(K_{1})+h_{U}(K_{2})
$$
 

(参见引理5.8.8的(6)). 故由(5.8.1)定义的映射在每个 $S(V^{-1})$的元素上取值为零. 由于 $h_*\in S(V^{-1})$, 因此(7)成立.

定理5.8.10 令G为局部紧群. 则在G上存在一个左Haar测度.

证 令O为G的开子集的全体，在O上如下定义集函数 $\mu$:

 
$$
\mu(U)=\sup\{h_{*}(K):K\subset U,K\in\mathcal{C}\}.
$$
 

往证μ在在O上有次σ可加性. 设 $\{U_i, i \geq 1\} \subset \mathcal{O}$. 令 $K$是 $\cup_i U_i$的紧子集, 则存在一个正整数 $n$, 使得 $K \subset \cup_i^n U_i$. 利用引理5.1.21和数学归纳法推知, 存在紧子集 $\{K_i, 1 \leq i \leq n\}$, 使得 $K = \cup_i^n K_i$, 并且对每个 $i, K_i \subset U_i$. 从而由引理5.8.9的(6)推知

 
$$
h_{*}(K)\leqslant\sum_{i=1}^{n}h_{*}(K_{i})\leqslant\sum_{i=1}^{n}\mu(U_{i})\leqslant\sum_{i=1}^{\infty}\mu(U_{i}).
$$
 

由于 $K$是 $\cup_i U_i$的任意紧子集， $\mu$的次 $\sigma$可加性得证。

现将 $\mu$扩展到G的所有子集：

 
$$
\mu^{*}(A)=\inf\{\mu^{*}(U):A\subset U,U\in\mathcal{O}\}.
$$
 

显然， $\mu^*$ 是  $G$ 上的外测度。为要证明  $G$ 的每个 Borel 子集都是  $\mu^*$ 可测的，只需证明  $G$ 的每个开子集是  $\mu^*$ 可测的。为此，由引理 1.4.5，只需证明：对任何开子集  $U$ 和  $V$，其中  $\mu^*(V) < \infty$，有

$$
\mu(V)\geqslant\mu(V\cap U)+\mu^{*}(V\cap U^{c}).   \tag*{(5.8.2)}
$$

任给$\varepsilon > 0$，选择$V \cap U$的紧子集$K$，使得$h_*(K) > \mu(V \cap U) - \varepsilon$，然后选择$V \cap K^c$的紧子集$L$，使得$h_*(L) > \mu(V \cap K^c) - \varepsilon$。则$K \cap L = \varnothing$，并且由于$V \cap U^c \subset V \cap K^c$，$L$满足$h_*(L) > \mu^*(V \cap U^c) - \varepsilon$。从这些不等式和引理5.8.9可以得出：

 
$$
h_{*}(K\cup L)=h_{*}(K)+h_{*}(L)\geqslant\mu(V\cap U)+\mu^{*}(V\cap U^{c})-2\varepsilon.
$$
 

由于ε是任意的，并且 $h_{*}(K \cup L) \leqslant \mu^*(V)$，从而不等式(5.8.2)成立。因此， $\mathcal{B}(G)$包含在 $\mu^*$可测集的 $\sigma$代数中， $\mu^*$到 $\mathcal{B}(G)$的限制为一测度，并在 $\mathcal{O}$上与 $\mu$吻合，故将 $\mu^*$到 $\mathcal{B}(G)$的限制仍记为 $\mu$。

容易证明 $\mu$是非零的Radon测度. 又由引理5.8.9的(4)推知,  $\mu$为左转换不变的.

---

下一引理给出了Haar测度的一个基本性质, 在证明Haar测度的唯一性时将要用到它.

引理5.8.11 令G为局部紧群，μ为G上的左Haar测度。则G的每个非空开子集U满足μ(U)>0，并且每个属于K(G)且不完全为零的非负函数f，有∫fdμ>0。

证 任意选择一个紧集K使得 $\mu(K) > 0$。令U为G的非空开子集。则 $\{xU\}_{x\in G}$为紧集K的开覆盖，所以存在G中元素序列 $\{x_i\}_{i=1}^n$，使得 $K \subset \cup_{i=1}^n x_i U$。从而 $\mu(K) \leq \sum_{i=1}^n \mu(x_i U)$， $\mu$的转换不变性蕴含 $\mu(K) \leq n\mu(U)$。因此， $\mu(U) > 0$。这证明了引理的前半部分。现设 $f \in \mathcal{K}(G)$是非恒为零的非负函数，则存在 $\varepsilon > 0$和一个非空开集U，使得 $f \geq \varepsilon I_U$，由此推得 $\int f d\mu \geq \varepsilon\mu(U) > 0$。

定理5.8.12 令G为局部紧群,  $\mu$ 和  $\nu$ 为G上的左Haar测度, 则存在一正实数c, 使得  $\nu = c\mu$.

证 令  $g \in \mathcal{K}(G)$ 是非恒为零的非负函数 ( $g$ 在整个证明中将保持不变)，并令  $f$ 为  $\mathcal{K}(G)$ 中的任意函数。由于  $\int g \, d\mu \neq 0$ (引理5.8.11)，我们可以做比率  $\int f \, d\mu / \int g \, d\mu$。往证该比率仅依赖函数  $f$ 和  $g$，而不依赖在计算中使用的特定 Haar 测度  $\mu$。对  $h \in \mathcal{K}(G \times G)$，利用迭代积分的 Fubini 定理颠倒积分顺序，再利用左 Haar 测度的左转换不变性 (将  $x$ 替换为  $y^{-1} x$，将  $y$ 替换为  $xy$)，我们得到

$$
\begin{align*}\int h(x,y)\nu(dy)\mu(dx)&=\int h(y^{-1}x,y)\mu(dx)\nu(dy)\\&=\int h(y^{-1},xy)\nu(dy)\mu(dx).\end{align*}   \tag*{(5.8.3)}
$$

现将此恒等式应用于如下由定义的函数 $h$:

 
$$
h(x,y)=\frac{f(x)g(y x)}{\int g(t x)\nu(d t)},
$$
 

由系5.8.5和引理5.8.11容易验证$h$确实属于$\mathcal{K}(G\times G)$. 对于此函数$h$, 有$h(y^{-1},xy)=f(y^{-1})g(x)/\int g(ty^{-1})\nu(dt)$, (5.8.3) 蕴含

 
$$
\int f(x)\mu(dx)=\int g(x)\mu(dx)\int\frac{f(y^{-1})}{\int g(ty^{-1})\nu(dt)}\nu(dy).
$$
 

这表明比率 $\int f d\mu / \int g d\mu$仅依赖函数 $f$和 $g$，而不依赖Haar测度 $\mu$。因此，对任何Haar测度 $\nu$，我们有

 
$$
\frac{\int f d\nu}{\int g d\nu}=\frac{\int f d\mu}{\int g d\mu}.
$$
 

因此满足∫fdν = c∫fdμ,其中c = ∫gdv/ ∫gdμ. 由于此等式对K(G)中的每个f成立, 故由Riesz表示定理(定理5.2.8)推知ν = cμ.

---

#### 5.8.3 Haar测度的性质

令G为局部紧群， $\mu$为G上的Radon测度。映射 $x \mapsto x^{-1}$是G到自身的同胚(命题5.8.1)。因此， $A \in \mathcal{B}(G)$等价于 $A^{-1} \in \mathcal{B}(G)$。在 $\mathcal{B}(G)$上通过 $\check{\mu}(A) = \mu(A^{-1})$定义函数 $\check{\mu}$。易知 $\check{\mu}$是G上的Radon测度。由积分的线性性和单调收敛定理推知：对于每个非负或 $\check{\mu}$可积的Borel函数 $f$，

$$
\int f d\breve{\mu}=\int\breve{f}d\mu.   \tag*{(5.8.4)}
$$

命题5.8.13 令G为局部紧群,  $\mu$ 为G上的Radon测度. 则 $\mu$ 是左Haar测度, 当且仅当 $\tilde{\mu}$ 是右Haar测度;  $\mu$ 是右Haar测度, 当且仅当 $\tilde{\mu}$ 是左Haar测度.

证 对每个 $x\in G,A\in\mathcal{B}(G)$，恒等式 $(Ax)^{-1}=x^{-1}A^{-1}$蕴含 $\check{\mu}(Ax)=\check{\mu}(A)$成立，当且仅当 $\mu(x^{-1}A^{-1})=\mu(A^{-1})$。命题的前半部分得证。将 $\mu$替换为 $\check{\mu}$并注意 $\check{\check{\mu}}=\mu$，从命题的前半部分部分即可推得后半部分。

系5.8.14 令G为局部紧群. 不计一常数乘子, 在G上存在唯一的右Haar测度.

命题5.8.15 令G为局部紧群，μ为左(或右)Haar测度. 当且仅当G是紧的，μ是有限测度. 特别，在紧群上存在μ(G)=1的“标准化”左(或右)Haar测度.

证 我们只对  $\mu$ 为左Haar测度情形证明．由于  $\mu$ 是 Radon测度，如果  $G$ 是紧的，则  $\mu(G) < \infty$．反之，设  $0 < \mu(G) < \infty$．令  $K$ 为  $G$ 的紧子集，使得  $\mu(K) > 0$（由  $\mu$ 的正则性）．由于  $\cup_{x \in G} xK = G$，且  $\mu(G) < \infty$，存在  $G$ 中元素的有限序列  $\{x_i\}_{i=1}^n$，使得  $\{x_i K, 1 \leqslant i \leqslant n\}$ 互不相交，且对其他  $x \in G$， $xK$ 与  $\cup_{i=1}^n x_i K$ 交集非空，即  $x \in (\cup_{i=1}^n x_i K) K^{-1}$．由于  $K^{-1}$ 是紧集， $G = (\cup_{i=1}^n x_i K) K^{-1}$ 也为紧集．

令$G$为局部紧群，$\mu$为左Haar测度。映射$u \mapsto ux$是$G$到自身的同胚(命题5.8.1)。因此，$\forall x \in G$，公式$\mu_x(A) = \mu(Ax)$定义了$G$上的Radon测度$\mu_x$。易知$\mu_x$是左Haar测度，故由定理5.8.12，对每个$x$，存在一个正数，记为$\Delta(x)$，使得$\mu_x = \Delta(x)\mu$。以这种方式定义的函数$\Delta : G \mapsto \mathbb{R}$被称为$G$的模函数。如果$\nu$是$G$上的另一个左Haar测度，则有一个正常数$c$，使得$\nu = c\mu$，因此$\nu_x = c\mu_x = c\Delta(x)\mu = \Delta(x)\nu$对$G$中的每个$x$成立。这表明模函数$\Delta$由群$G$确定，不依赖于用于定义它的左Haar测度。

由于 $(I_{A})_{x}=I_{Ax}$对G中的每个x和G的每个子集A成立，由积分的线性性和单调收敛定理推知：对每个非负或 $\mu$可积的Borel函数f，

$$
\int f_{x}d\mu=\Delta(x)\int f d\mu.   \tag*{(5.8.5)}
$$

命题5.8.16 令G为局部紧群, $\Delta$为G的模函数,则

(1)  $\Delta$ 是连续的，

(2)  $\Delta(xy) = \Delta(x)\Delta(y)$ 对于 G 中的每个 x 和 y 成立.

证 令  $\mu$ 为 G 上的左 Haar 测度， $f \in \mathcal{K}(G)$ 为一非恒为零的非负函数，则  $\int f \, d\mu \neq 0$（引理 5.8.11）。于是系 5.8.5 和等式 (5.8.5) 蕴含  $\Delta$ 的连续性。关系  $\Delta(xy) = \Delta(x)\Delta(y)$

---

由如下计算得出:

 
$$
\Delta(x y)\mu(A)=\mu(A x y)=\Delta(y)\mu(A x)=\Delta(y)\Delta(x)\mu(A).
$$
 

如果局部紧群G的模函数满足 $\Delta(x)=1,\forall x\in G$，则称G是单模的。因此，一个局部紧群G是单模的，当且仅当G上的每个左Haar测度是一个右Haar测度。当然，每个交换局部紧群都是单模的。

##### 命题5.8.17 每个紧群都是单模的.

此令G为一个紧群， $\Delta$为模函数。 $\Delta$的连续性和G的紧性蕴含 $\Delta$是有界的。此外，关系 $\Delta(x^n) = (\Delta(x))^n$对于每个正整数 $n$和 $G$的每个元素 $x$都成立(命题5.8.16)。因此， $\Delta(x) \leqslant 1$。如果 $G$的某元素 $x$满足 $0 < \Delta(x) < 1$，则 $x^{-1}$满足 $\Delta(x^{-1}) > 1$，这不可能。因此必须有 $\Delta(x) = 1$， $\forall x \in G$。

命题5.8.18 令G为局部紧群, $\mu$为左Haar测度.则对G的每个Borel子集A,有

 
$$
\breve{\mu}(A)=\int_{A}\Delta(x^{-1})\mu(d x).
$$
 

证 在 $B(G)$上定义测度 $\nu$:

 
$$
\nu(A)=\int_{A}\Delta(x^{-1})\mu(d x).
$$
 

我们将证明ν是右Haar测度, 且ν = μ. 先证ν是Radon测度. 对于每个正整数n, 令 $G_n$为如下定义的G的开子集:

 
$$
G_{n}=\{x\in G:1/n<\Delta(x^{-1})<n\}.
$$
 

令U为G的一个开子集. 由 $\mu$的正则性推知, 对每个n,

 
$$
\nu\bigl(U\cap G_{n}\bigr)=\operatorname*{s u p}\bigl\{\nu\bigl(K\bigr):K\subset U\cap G_{n},K\in\mathcal{K}(G)\bigr\}.
$$
 

由于 $\nu(U)=\lim_{n}\nu(U\cap G_{n})$，容易证明

 
$$
\nu(U)=\sup\{\nu(K):K\subset U,K\in\mathcal{K}(G)\}.
$$
 

现设A是G的任意Borel子集，满足 $\nu(A)<\infty$。我们需要证明

$$
\nu(A)=\inf\{\nu(U):A\subset U,U\in\mathcal{O}(G)\}.   \tag*{(5.8.6)}
$$

令$\varepsilon$为一正数。基于$\mu$是Radon测度和在$G_n$上有$1/n < \Delta(x^{-1}) < n$这一事实，对于每个$n$，可以选择$G_n$的一个开子集$U_n$，包含$A \cap G_n$，并满足$\nu(U_n) < \nu(A \cap G_n) + \varepsilon/2^n$。

---

令 $U = \cup_n U_n$，则 $U$包含 $A$，且满足 $\nu(U) < \nu(A) + \varepsilon$。由于 $\varepsilon > 0$是任意的，因此有 $(5.8.6)$。不难看出， $G$的每个紧致子集 $K$都满足 $\nu(K) < \infty$（因为 $\mu(K)$是有限的，并且函数 $x \to \Delta(x^{-1})$在 $K$上有界）。因此， $\nu$是Radon测度。

利用5.8.5和命题5.8.16的(2)，我们可以做如下运算：

 
$$
\begin{align*}\nu(Ay)&=\int I_{Ay}(x)\Delta(x^{-1})\mu(dx)\\&=\int I_{Ay}(x)\Delta(y^{-1})\Delta((xy^{-1})^{-1})\mu(dx)\\&=\int\Delta(y^{-1})(I_{A})_{y}(x)\Delta((xy^{-1})^{-1})\mu(dx)\\&=\int\Delta(y^{-1})\Delta(y)I_{A}(x)\Delta(x^{-1})\mu(dx)=\nu(A).\end{align*}
$$
 

这表明ν是右Haar测度.

因此，存在一个正数c，使得 $\nu = c\dot{\mu}$（见命题5.8.13和系5.8.14）。于是有

 
$$
c=\frac{\nu(A)}{\breve{\mu}(A)}=\frac{\nu(A)}{\mu(A^{-1})}=\frac{1}{\mu(A^{-1})}\int_{A}\Delta(x^{-1})\mu(d x),
$$
 

只要A是满足0 <  $\check{\mu}(A)$ <  $\infty$的Borel集．由于 $\Delta$是连续的并且在e处取值1，通过让A为e的足够小的对称邻域，我们可以使等式的右侧任意接近1．因此，c = 1，从而 $\nu = \check{\mu}$．

系5.8.19 令G为局部紧群， $\mu$和 $\nu$分别为G上的为左和右Haar测度. 则对G的Borel子集A, $\mu(A)=0$, 当且仅当 $\nu(A)=0$.

证 公式  $A \rightarrow \int_A \Delta(t^{-1}) \mu(dt)$ 定义了 G 上的一右 Haar 测度 (命题 5.8.18). 因此，存在一个正常数  $c$，使得对于  $\mathcal{B}(G)$ 中的每个  $A$，我们有  $\nu(A) = c \int_A \Delta(t^{-1}) \mu(dt)$. 由于  $\Delta$ 在  $G$ 上处处为正，因此  $\mu$ 和  $\nu$ 有相同的零测集.

---

## 第 6 章 测度的收敛

本章研究测度序列的收敛, 其中包括欧氏空间上Borel测度的收敛, 距离空间上有限测度的弱收敛及局部紧Hausdorff空间上Radon测度的淡收敛.

## 6.1 欧氏空间上Borel测度的收敛

设μ为欧氏空间R^{d}上的Radon测度，a, b ∈ R^{d}, a < b. 如果μ([a, b] \setminus (a, b)) = 0，则称(a, b)为μ的连续区间. 我们用I(μ)表示μ的连续区间全体.

定义6.1.1 设 $\mu_{n}$及 $\mu$为 $R^{d}$上的Radon测度. 如果

 
$$
\lim_{n\to\infty}\mu_{n}((a,b])=\mu((a,b]),\ \forall(a,b]\in\mathcal{I}(\mu),
$$
 

则称序列 $(\mu_n)$淡收敛于 $\mu$，记为 $\mu_n \to \mu$（我们将英文“vague convergence”译为淡收敛）；如果进一步还有 $\lim_{n \to \infty} \mu_n(\mathbb{R}^d) = \mu(\mathbb{R}^d) < \infty$，则称 $(\mu_n)$弱收敛于 $\mu$，记为 $\mu_n \to \mu$。

下面两个定理分别给出了淡收敛及弱收敛的积分刻画．这一刻画允许我们将这两个收敛概念推广到一般拓扑空间情形．

定理6.1.2 为要 $\mu_{n}\xrightarrow{v}\mu$，必须且只需

$$
\lim_{n\to\infty}\int_{\mathbb{R}^{d}}f d\mu_{n}=\int_{\mathbb{R}^{d}}f d\mu,\ \forall f\in C_{c}(\mathbb{R}^{d}).   \tag*{(6.1.1)}
$$

这里 $C_{c}(\mathbb{R}^{d})$表示 $\mathbb{R}^{d}$上有紧支撑的连续函数全体.

证明 必要性. 设  $\mu_n \xrightarrow{\nu} \mu$. 依淡收敛的定义, 当  $(a, b] \in \mathcal{I}(\mu), f = I_{(a, b]}$ 时 (6.1.1) 式成立. 现设  $f \in C_c(\mathbb{R}^d)$. 取  $(a, b] \in \mathcal{I}(\mu)$, 使  $f$ 的支撑含于  $(a, b)$. 对给定  $\varepsilon > 0$, 则易知存在  $\mathbb{R}^d$ 上的简单函数  $f_\varepsilon$, 使得  $[f_\varepsilon \neq 0] \subset (a, b)$, 且为  $\mathcal{I}(\mu)$ 中元素的有限不交并, 满足  $\sup_{x \in \mathbb{R}^d} |f(x) - f_\varepsilon(x)| \leqslant \varepsilon$. 则

 
$$
\begin{align*}&\limsup_{n\to\infty}\left|\int_{\mathbb{R}^{d}}f d\mu_{n}-\int_{\mathbb{R}^{d}}f d\mu\right|\\\leq&\limsup_{n\to\infty}\left[\int_{\mathbb{R}^{d}}|f-f_\varepsilon|d\mu_{n}+\left|\int_{\mathbb{R}^{d}}f_\varepsilon d\mu_{n}-\int_{\mathbb{R}^{d}}f_\varepsilon d\mu\right|\right]+\int_{\mathbb{R}^{d}}|f_\varepsilon-f|d\mu\\\leq&2\varepsilon\mu((a,b)).\end{align*}
$$
 

故6.1.1式成立.

---

充分性. 设(6.1.1)式成立. 令 $(a,b] \in \mathcal{I}(\mu)$. 对给定 $\varepsilon > 0$, 存在 $\delta \in \mathbb{R}^d, \delta > 0$, 使得 $\mu(U) < \varepsilon$, 此处

 
$$
U=(a-\delta,a+\delta)\cup(b-\delta,b+\delta).
$$
 

令 $g = I_{(a,b]}$．易知存在 $g_{1}, g_{2} \in C_{c}(\mathbb{R}^{d})$，使得 $g_{1} \leqslant g \leqslant g_{2}, g_{2} - g_{1} \leqslant I_{U}$．我们有

 
$$
\begin{aligned}\int g_{1}d\mu\leftarrow&\int g_{1}d\mu_{n}\leqslant\mu_{n}((a,b])\leqslant\int g_{2}d\mu_{n}\rightarrow\int g_{2}d\mu\\&\int g_{1}d\mu\leqslant\mu((a,b])\leqslant\int g_{2}d\mu\\&\int(g_{2}-g_{1})d\mu\leqslant\mu(U)<\varepsilon,\end{aligned}
$$
 

故有 $\mu_{n}((a,b])\to\mu((a,b])$，即 $\mu_{n}\xrightarrow{v}\mu.$

定理6.1.3 假定 $\sup\mu_{n}(\mathbb{R}^{d})<\infty,\mu(\mathbb{R}^{d})<\infty$。为要 $\mu_{n}\xrightarrow{w}\mu$，必须且只需

$$
\lim_{n\to\infty}\int_{\mathbb{R}^{d}}f d\mu_{n}=\int_{\mathbb{R}^{d}}f d\mu,\quad\forall f\in C_{b}(\mathbb{R}^{d}).   \tag*{(6.1.2)}
$$

证明 由于$\mathbb{R}^d$上常值函数$1$属于$C_b(\mathbb{R}^d)$，且$C_c(\mathbb{R}^d) \subset C_b(\mathbb{R}^d)$，故条件的充分性显然。往证必要性。设$\mu_n \stackrel{w}{\to} \mu$。对给定$\varepsilon > 0$，存在$(a, b] \in \mathcal{I}(\mu)$，使得$\mu((a, b]^c) < \varepsilon$。由于$\mu_n((a, b]) \to \mu((a, b)]$，且$\mu_n(\mathbb{R}^d) \to \mu(\mathbb{R}^d)$，故存在$n_0(\varepsilon)$，使得$\forall n \geq n_0(\varepsilon)$，有$\mu_n((a, b]^c) < \varepsilon$。现设$f \in C_b(\mathbb{R}^d)$，$|f| \leq M < \infty$。显然存在$f_\varepsilon \in C_c(\mathbb{R}^d)$，使得$f_\varepsilon$在$(a, b]$上等于$f$，且$|f - f_\varepsilon| \leq 2M$。由定理6.1.2知，$(6.1.2)$式对$f_\varepsilon$成立，故有

 
$$
\begin{align*}&\limsup_{n\to\infty}\left|\int_{\mathbb{R}^{d}}f d\mu_{n}-\int_{\mathbb{R}^{d}}f d\mu\right|\\\leq&\limsup_{n\to\infty}\left[\int_{\mathbb{R}^{d}}|f-f_{\varepsilon}|d\mu_{n}+\left|\int_{\mathbb{R}^{d}}f_{\varepsilon}d\mu_{n}-\int_{\mathbb{R}^{d}}f_{\varepsilon}d\mu\right|\right]+\int_{\mathbb{R}^{d}}|f_{\varepsilon}-f|d\mu\\\leq&4M\varepsilon,\end{align*}
$$
 

这表明 $(6.1.2)$式成立.

下一结果是Helly定理.

定理6.1.4 设 $(\mu_{n})$为 $R^{d}$上一列有限Borel测度， $\sup_{n}\mu_{n}(\mathbb{R}^{d})<\infty$，则存在 $(\mu_{n})$的一子列 $(\mu_{n_{k}})$，使得 $\mu_{n_{k}}\xrightarrow{v} 某 \mu$.

证明  $\forall x \in \mathbb{R}^d$，令

$$
F_{n}(x)=\mu_{n}((-\infty,x]).   \tag*{(6.1.3)}
$$

任取 $\mathbb{R}^d$中一可数稠子集 $\{x_1, x_2, \cdots\}$。由对角线原理，可选取 $(F_n)$的一子列 $(F_{n_k})$，使得 $\forall m \geq 1$， $\lim_{k \to \infty} F_{n_k}(x_m)$存在，记为 $G(x_m)$。令

 
$$
F(x)=\inf\{G(x_{m})\mid x_{m}>x\},
$$
 

---

则 $F$为 $\mathbb{R}^d$上的右连续增函数。容易证明：对 $F$的一切连续点 $x$，有 $\lim_{k\to\infty}F_{n_k}(x)=F(x)$。令 $\mu$为由 $F$产生的 $\mathbb{R}^d$上的测度(见1.5节)，则显然有 $\mu_{n_k}\xrightarrow{v}\mu$。

注6.1.5 设 $(\mu_n)$为 $R^d$上一列概率测度， $(F_n)$为由(6.1.3)式定义的右连续增函数(称为 $\mu_n$的分布函数)。则 $(\mu_n)$淡收敛于某测度 $\mu$ ( $\mu$不一定是概率测度)等价于相应的分布函数序列 $(F_n)$弱收敛于某一右连续增函数 $F$ ( $F(x)$ 不一定等于 $\mu((-\infty,x])$)； $(\mu_n)$弱收敛于某概率测度 $\mu$等价于 $(F_n)$全收敛于 $F$(这时 $F$是 $\mu$的分布函数)。

下面的例子表明 $\mu_{n} \rightarrow \mu$不蕴含 $F_{n} \rightarrow F$。令 $\mu_{n}$为 $\mathbb{R}$上负荷于 $\{-n\}$的概率测度，则 $(\mu_{n})$淡收敛于零测度 $\mu$，但是有 $\lim_{n \to \infty} F_{n}(x) = 1, \forall x \in \mathbb{R}$，而 $F(x) = 0, \forall x \in \mathbb{R}$。

##### 习题

6.1.1 设  $\mu_n \xrightarrow{v} \mu$，且  $\sup \mu_n (\mathbb{R}^d) < \infty$，则  $\forall f \in C_0 (\mathbb{R}^d)$，有

 
$$
\lim_{n\to\infty}\int_{\mathbb{R}^{d}}f d\mu_{n}=\int_{\mathbb{R}^{d}}f d\mu.
$$
 

这里 $C_{0}(\mathbb{R}^{d})$表示 $\mathbb{R}^{d}$上在无穷远处为0的连续函数全体.

6.1.2 设  $\mu_n \xrightarrow{v} \mu$,  $(a, b] \in \mathcal{I}(\mu)$. 则对  $\mathbb{R}^d$ 上一切连续函数  $f$ 有

 
$$
\lim_{n\to\infty}\int_{a}^{b}f d\mu_{n}=\int_{a}^{b}f d\mu.
$$
 

### 6.2 距离空间上有限测度的弱收敛

设X为一距离空间(或可距离化的拓扑空间)， $C_{b}(X)$表示X上有界连续函数全体.由定理6.1.3我们自然引进如下的定义：

定义6.2.1 设 $(X,\rho)$为一距离空间， $\mu,\mu_{1},\mu_{2},\cdots$为 $\mathcal{B}(X)$上的有限测度. 如果对一切 $f\in C_{b}(X)$，有

 
$$
\lim_{n\to\infty}\int_{X}f d\mu_{n}=\int_{X}f d\mu,
$$
 

则称 $(\mu_{n})$弱收敛于 $\mu$，记为 $\mu_{n}\xrightarrow{w}\mu$.

显然, 弱收敛的极限是唯一的. 此外, 由于  $C_{b}(X)$ 只与 X 的拓扑有关, 所以测度弱收敛概念并不依赖于距离的选取.

下一引理允许我们将有限测度的弱收敛归结为概率测度的弱收敛, 其证明是不足道的.

引理6.2.2 设 $(X,\rho)$为一距离空间， $\mu,\mu_{1},\mu_{2},\cdots$为 $\mathcal{B}(X)$上的有限测度.令

 
$$
\mathbb{P}(A)=\frac{\mu(A)}{\mu(X)},\quad\mathbb{P}_{n}(A)=\frac{\mu_{n}(A)}{\mu_{n}(X)},\quad A\in\mathcal{B}(X).
$$
 

---

则下列二断言等价:

(1)  $\mu_n \xrightarrow{w} \mu;$

(2)  $\mathbb{P}_n \xrightarrow{w} \mathbb{P}, \mu_n(X) \to \mu(X).$

定义6.2.3 设X为一拓扑空间，μ为B(X)上一测度，A ∈ B(X)。若μ(∂A) = 0(∂A = ∇A/∇A)为A的边界)，则称A为μ连续集。

下一定理给出了测度弱收敛的若干刻画.

定理6.2.4  $(X,\rho)$为一距离空间, $\mathcal{U}_{\rho}(X)$表示X上关于 $\rho$一致连续的有界函数全体(从而有 $\mathcal{U}_{\rho}(X)\subset C_{b}(X)$).令 $\mu,\mu_{1},\mu_{2},\cdots$为 $\mathcal{B}(X)$上的有限测度,则下列条件等价:

(1)  $\mu_n \xrightarrow{w} \mu;$

(2)  $\forall f \in \mathcal{U}_\rho(X), \lim_{n \to \infty} \int f\,d\mu_n = \int f\,d\mu;$

(3) ∀闭集  $F$,  $\limsup_{n\to\infty}\mu_n(F)\leqslant\mu(F)$, 且  $\lim_{n\to\infty}\mu_n(X)=\mu(X)$;

(4) ∀开集G,  $\liminf_{n\to\infty}\mu_n(G)\geq\mu(G)$, 且  $\lim_{n\to\infty}\mu_n(X)=\mu(X)$;

(5) 对任何  $\mu$ 连续集  $A \in \mathcal{B}(X)$，有  $\lim_{n \to \infty} \mu_n(A) = \mu(A)$.

证 (1)  $\Rightarrow$ (2) 显然. 往证 (2)  $\Rightarrow$ (3). 假设 (2) 成立. 令 F 为闭集,  $f_{n}(x) = \left(\frac{1}{1 + \rho(x, F)}\right)^{n}$.  $n \geqslant 1$, 则  $f_{n} \in \mathcal{U}_{\rho}(X)$, 且  $f_{n} \downarrow I_{F}$, 故有

 
$$
\mu(F)=\lim_{k\to\infty}\int f_{k}d\mu=\lim_{k\to\infty}\lim_{n\to\infty}\int f_{k}d\mu_{n}\geq\limsup_{n\to\infty}\mu_{n}(F).
$$
 

此外，令 $f\equiv1$得 $\lim_{n\to\infty}\mu_{n}(X)=\mu(X)$，故(3)成立。(3) $\Leftrightarrow(4)$显然。(3) $(4)\Rightarrow(5)$由下式看出：

 
$$
\begin{align*}\limsup_{n\to\infty}\mu_{n}(A)&\leqslant\limsup_{n\to\infty}\mu_{n}(\overline{A})\leqslant\mu(\overline{A})=\mu(A^{\circ})\\&\leqslant\liminf_{n\to\infty}\mu_{n}(A^{\circ})\leqslant\liminf_{n\to\infty}\mu_{n}(A).\end{align*}
$$
 

剩下只需证(5)⇒(1). 设(5)成立. 令  $f \in C_b(X)$, 给定  $\varepsilon > 0$, 选取 N 及实数  $a_i, 1 \leq i \leq N - 1$, 使得

 
$$
-\|f\|-1=a_{0}<a_{1}<\cdots<a_{N-1}<a_{N}=\|f\|+1,
$$
 

且使

 
$$
\sup_{i}(a_{i}-a_{i-1})<\varepsilon,\quad\mu([f=a_{i}])=0,\quad1\leqslant i\leqslant N-1,
$$
 

这里 $\|f\| = \sup_{x} |f(x)|$。令 $B_i = [a_{i-1} \leqslant f(x) < a_i], i = 1, 2, \cdots, N$。则 $(B_i)$两两不相交，且 $\sum_i B_i = X, \mu(\partial B_i) = 0, 1 \leqslant i \leqslant N$。此外，对一切 $x \in X$，有 $|f(x)-$

---

 $\sum_{i=1}^{N}a_{i}I_{B_{i}}(x)|<\varepsilon.$ 于是

 
$$
\begin{align*}&\limsup_{n\to\infty}\big|\int f d\mu_{n}-\int f d\mu\big|\\\leq&\lim_{n\to\infty}(\mu_{n}(X)+\mu(X))\varepsilon+\limsup_{n\to\infty}\big|\int\sum_{i=1}^{N} a_{i} I_{B_{i}}d(\mu_{n}-\mu)\big|\\\leq&2\mu(X)\varepsilon+\sum_{i=1}^{N}|a_{i}|\limsup_{n\to\infty}|\mu_{n}(B_{i})-\mu(B_{i})|=2\mu(X)\varepsilon.\end{align*}
$$
 

由于 $\varepsilon>0$是任意的，故(1)成立.

从现在起, 我们只讨论概率测度的弱收敛.

引理6.2.5 设h为距离空间 $(X,\rho)$到另一距离空间 $(Y,d)$中的映射，令 $D(h)$表示h的不连续点全体，则 $D(h)$为X中的Borel可测集.

证  $\forall n,m\geq1,$ 令

 
$$
\begin{aligned}A_{n,m}=&\left\{x\in X\mid 存在 y,z\in X, 使 \rho(x,y)<\frac{1}{n},\right.\\&\left.\rho(x,z)<\frac{1}{n},d(h(y),h(z))\geqslant\frac{1}{m}\right\},\end{aligned}
$$
 

则 $A_{n,m}$为X的开子集．显然有 $D(h)=\bigcup_{m}\bigcap_{n}A_{n,m}$，故 $D(h)$为X中的Borel可测集．

定义6.2.6 设 $(X,\rho)$为一距离空间，IP为 $\beta(X)$上一概率测度，h为 $(X,\rho)$到另一距离空间 $(Y,d)$的映射. 如果 $\mathbb{P}(D(h))=0$，则称h为IP连续的.

命题6.2.7 设 $(X,\rho)$及 $(Y,d)$为两个距离空间， $\mathbb{P},\mathbb{P}_{1},\mathbb{P}_{2},\cdots$为 $\mathcal{B}(X)$上的概率测度， $h$为 $X$到 $Y$中的Borel可测映射．如果 $\mathbb{P}_n\xrightarrow{w}\mathbb{P}$，且 $h$为 $\mathbb{P}$连续，则有 $\mathbb{P}_n h^{-1}\xrightarrow{w}\mathbb{P}h^{-1}$．这里 $\mathbb{P}h^{-1}$为由 $h$在 $(Y,\mathcal{B}(Y))$上导出的概率测度．

证 设 F 为 Y 中的闭集, 则有

$$
\overline{{h^{-1}(F)}}\subset D(h)\cup h^{-1}(F).   \tag*{(6.2.1)}
$$

于是由假定  $\mathbb{P}(D(h)) = 0$ 知  $\mathbb{P}(\overline{h^{-1}(F)}) = \mathbb{P}(h^{-1}(F))$。再由假定  $\mathbb{P}_n \xrightarrow{w} \mathbb{P}$ 及定理 6.2.4 知：

 
$$
\begin{align*}\limsup_{n\to\infty}\mathbb{P}_{n} h^{-1}(F)&=\limsup_{n\to\infty}\mathbb{P}_{n}(h^{-1}(F))\\&\leqslant\limsup_{n\to\infty}\mathbb{P}_{n}(\overline{h^{-1}(F)})\leqslant\mathbb{P}(\overline{h^{-1}(F)})\\&=\mathbb{P}(h^{-1}(F))=\mathbb{P}h^{-1}(F).\end{align*}
$$
 

这表明 $P_{n}h^{-1}\xrightarrow{w}Ph^{-1}$ (见定理6.2.4).

---

下一命题是上一命题的重要推论, 它使我们对测度的弱收敛有进一步的认识.

命题6.2.8 设 $(X,\rho)$为一距离空间, $IP,IP_{1},IP_{2},\cdots$为 $\mathcal{B}(X)$上的概率测度.若 $IP_{n}\xrightarrow{w}IP$,则对一切IP连续的有界Borel可测实值函数f,有

 
$$
\lim_{n\to\infty}\int f d\boldsymbol{P}_{n}=\int f d\boldsymbol{P}.
$$
 

证 设$f$为$X$上有界Borel可测函数，则存在$a>0$，使$|f|\leq a$，于是$f$为$(X,\mathcal{B}(X))$到$([-a,a],\mathcal{B}([-a,a]))$中的可测映射．假定$f$为$P$连续，则由命题6.2.7，$P_n f^{-1}\xrightarrow{w}P f^{-1}$．令$g(t)=t,t\in[-a,a]$，则$g$为$[-a,a]$上的有界连续函数．故由弱收敛定义知

 
$$
\lim_{n\to\infty}\int g d(\mathbb{P}_{n} f^{-1})=\int g d(\mathbb{P}f^{-1}).
$$
 

因此，由习题3.1.6知(注意 $g\circ f=f$)

 
$$
\lim_{n\to\infty}\int f d\boldsymbol{P}_{n}=\int f d\boldsymbol{P}.
$$
 

##### 习题

6.2.1 证明命题6.2.7的如下推广：设 $(X,\rho)$及 $(Y,d)$为距离空间， $\mathbb{P}$， $\mathbb{P}_1$， $\mathbb{P}_2$， $\cdots$为 $\mathcal{B}(X)$上的概率测度，且 $\mathbb{P}_n \xrightarrow{w} \mathbb{P}$。又设 $h,h_1,h_2,\cdots$为X到Y中的Borel可测映射，如果存在X中的Borel可测集 $B,B_1,B_2,\cdots$，使得：

 
$$
\left(1\right)\mathbb{P}(B^{c})=0,\mathbb{P}_{n}(B_{n}^{c})=0,n=1,2,\cdots
$$
 

(2)  $x_{n} \in B_{n}, x \in B, \rho(x_{n}, x) \to 0 \Rightarrow h_{n}(x_{n}) \to h(x),$

则 $P_{n}h_{n}^{-1}\xrightarrow{w}Ph^{-1}$

6.2.2 证明(6.2.1)式.

6.2.3 设 $(X,\rho)$为距离空间，A为X的一子集， $\mathbb{P}$为 $\mathcal{B}(X)$上的一概率测度，则为要A为 $\mathbb{P}$连续，必须且只需A的示性函数 $I_{A}$为 $\mathbb{P}$连续函数.

## 6.3 胎紧与Prohorov定理

在本节中, 我们恒假定 $(X,\rho)$为可分距离空间. 我们用 $\mathcal{P}(X)$表示 $\mathcal{B}(X)$上概率测度全体, 这时, 我们可以在 $\mathcal{P}(X)$上引入距离d, 使得按距离d收敛等价于上一节定义的测度弱收敛. 本节的主要任务在于给出 $\mathcal{P}(X), d$中相对紧集的一个刻画.

命题6.3.1 在 $\mathcal{P}(X)$上可以引入距离 $d$，使得 $\mathbb{P}_n \xrightarrow{w} \mathbb{P} \Leftrightarrow d(\mathbb{P}_n, \mathbb{P}) \to 0$.

证 由于 $(X,\rho)$是可分距离空间，由Tychonoff嵌入定理，X与一紧距离空间 $(Y,\rho^{\prime})$的某一子空间同胚。不妨设X为该子空间，于是距离 $\rho^{\prime}$限于X与 $\rho$等价。令 $\overline{X}$为X在

---

(Y,ρ′)中的闭包，则(X,ρ′)为紧空间，且为可分的，从而C(X)为可分Banach空间(见习题5.4.1)。这里C(X)表示X上连续函数全体(即有界连续函数全体)。另一方面，令Uρ′(X)表示X上按距离ρ′一致连续有界函数全体，则易知:f∈Uρ′(X)，当且仅当存在f∈C(X)，使f为f在X上的限制。这时还有\|f\|=\|f\|。因此，Uρ′(X)与C(X)同构，从而Uρ′(X)可分。令{f₁,f₂,…}为Uρ′(X)的可数稠子集。对IP,Q∈P(X)，令

 
$$
d(\mathbb{P},\mathbb{Q})=\sum_{j=1}^{\infty}\frac{1}{2^{j}}\Big(1\wedge\Big|\int f_{j}d\mathbb{P}-\int f_{j}d\mathbb{Q}\Big|\Big),
$$
 

则 $d$为 $\mathcal{P}(X)$上的距离，且由定理6.2.4知 $d(\mathbb{P}_n,\mathbb{P})\to0\Leftrightarrow\mathbb{P}_n\xrightarrow{w}\mathbb{P}$.

注6.3.2 若X为一波兰空间, 则可证明 $\mathcal{P}(X)$按测度弱收敛拓扑也是波兰空间. 由于下面不需要这一结果, 我们不在这里给出它的证明.

称 $\mathcal{P}(X)$的一子集H为相对紧的, 如果H的闭包 $\overline{H}$为 $\mathcal{P}(X)$中的紧集. 下面我们将给出 $\mathcal{P}(X)$中相对紧集的刻画. 为此, 先引进胎紧的概念.

定义6.3.3 设H为P(X)的一子集, 如果对任给ε > 0, 存在X的一紧子集K, 使得inf{P(K):IP ∈ H} ≥ 1 - ε, 则称H为胎紧的(tight).

定理6.3.4 (Prohorov定理) 设 $\mathcal{H} \subset \mathcal{P}(X)$.

(1) 若 H 是胎紧的，则 H 在  $\mathcal{P}(X)$ 中是相对紧的.

(2) 若 X 是波兰空间，则 H 的相对紧性蕴含 H 的胎紧性.

证 (1)首先，将X嵌入到一紧距离空间 $(Y, \rho')$中，并令 $\overline{X}$为X在 $(Y, \rho')$中的闭包(见命题6.3.1的证明)，则 $(\overline{X}, \rho')$为紧空间。现设 $\mathcal{H}$为胎紧的，令 $(\mathbb{P}_n)$为 $\mathcal{H}$中的一序列，要证存在一子列 $(\mathbb{P}_{n_k})$，使得 $\mathbb{P}_{n_k} \xrightarrow{w} \mathbb{P}$（这等价于 $\mathcal{H}$的相对紧性，因为 $\mathcal{P}(X)$是可分距离空间）。对 $A \in \mathcal{B}(\overline{X})$，令

 
$$
\mathcal{Q}_{n}(A)=\mathbb{P}_{n}(A\cap X),
$$
 

则易知 $Q_n$为 $(\overline{X}, \mathcal{B}(\overline{X}))$上的测度(注意 $\mathcal{B}(X) = X \cap \mathcal{B}(\overline{X})$).

设$\{f_1, f_2, \cdots\}$为$C(\overline{X})$的一可数稠子集，我们不妨设$f_1(x) = 1, \forall x \in \overline{X}$。用对角线法则，可选取$(Q_n)$的子列$(Q_{n_k})$，使得对每个$j = 1, 2, \cdots$，下述极限存在且有穷：

$$
\lim_{k\to\infty}\int f_{j}d\mathcal{Q}_{n_{k}}=l(f_{j}).   \tag*{(6.3.1)}
$$

l可唯一扩张成为 $C(\overline{X})$上的一正线性泛函．由于 $l(1) = 1$，故由Riesz表现定理，存在 $Q \in \mathcal{P}(\overline{X})$，使对一切 $f \in C(\overline{X})$，有 $Q(f) = l(f)$．由(6.3.1)式不难看出， $Q_{n_k} \xrightarrow{w} Q$.下面将证明：存在 $P \in \mathcal{P}(X)$，使 $P_{n_k} \xrightarrow{w} P$.

由于假定H是胎紧的，故对每个 $m=1,2,\cdots$，存在X的紧子集 $K_{m}$（从而也是 $\overline{X}$的紧子集），使得 $\mathbb{P}_{n_{k}}(K_{m})>1-1/m,k=1,2,\cdots$。显然有 $\mathbb{Q}_{n_{k}}(K_{m})=\mathbb{P}_{n_{k}}(K_{m})$，于

---

是有(注意 $Q_{n_k} \xrightarrow{w} Q$)

 
$$
\mathcal{Q}(K_{m})\geqslant\limsup_{k\to\infty}\mathcal{Q}_{k_{k}}(K_{m})\geqslant1-\frac{1}{m},\quad m=1,2,\cdots
$$
 

设 $X_{0}=\bigcup_{m}K_{m}$，则 $\varnothing(X_{0})=1$。令

 
$$
\mathbb{P}(A)=\mathbb{Q}(A\cap X_{0}),\;A\in\mathcal{B}(X),
$$
 

则 $P \in \mathcal{P}(X)$，且 $P(X_0) = 1$。设 $F$为 $X$中的闭集，则存在 $\overline{X}$中的闭集 $A$，使 $F = A \cap X$，于是我们有

 
$$
\begin{align*}\mathbb{P}(F)&=\mathbb{P}(A\cap X)=\mathbb{P}(A\cap X_{0})=\mathbb{Q}(A\cap X_{0})=\mathbb{Q}(A)\\&\geq\limsup_{k\to\infty}\mathbb{Q}_{n_{k}}(A)=\limsup_{k\to\infty}\mathbb{P}_{n_{k}}(A\cap X)=\limsup_{k\to\infty}\mathbb{P}_{n_{k}}(F).\end{align*}
$$
 

故由定理6.2.4知， $IP_{n_{k}} \xrightarrow{w} IP.$ (1)得证.

(2) 不妨设  $(X, \rho)$ 本身是完备的．设  $\mathcal{H}$ 是  $\mathcal{P}(X)$ 中的相对紧集．对任给  $\delta > 0$，因 X 是可分的，存在可数多个直径为  $\delta$ 的开球  $A_1, A_2, \cdots$，使得  $\bigcup_{i=1}^{\infty} A_i = X$．令  $B_n = \bigcup_{i \leq n} A_i$，则  $\forall \varepsilon > 0$，存在 n，使得  $\inf\{ \mathbb{P}(B_n) : \mathbb{P} \in \mathcal{H} \} \geq 1 - \varepsilon$．因为如若不然，对每个 n，存在  $\mathbb{P}_n \in \mathcal{H}$，使  $\mathbb{P}_n(B_n) < 1 - \varepsilon$．由于  $(\mathbb{P}_n)$ 的相对紧性，存在子列  $(\mathbb{P}_{n_k})$ 使  $\mathbb{P}_{n_k} \xrightarrow{w} \mathbb{P}$，这时有（注意  $B_n$ 为开集，且  $B_n \uparrow X$）

 
$$
\mathbb{P}(B_{n})\leqslant\liminf_{k\to\infty}\mathbb{P}_{n_{k}}(B_{n})\leqslant\liminf_{k\to\infty}\mathbb{P}_{n_{k}}(B_{n_{k}})\leqslant1-\varepsilon.
$$
 

由上式得$\mathbb{P}(X) \leqslant 1 - \varepsilon$，这不可能。由上所证，给定$\varepsilon > 0$，对每个$k = 1, 2, \cdots$，存在有限多个直径为$1/k$的开球$A_{k1}, \cdots, A_{kn_k}$，使得$\inf\{P(\bigcup_{i=1}^{n_k} A_{ki}) : P \in \mathcal{H}\} \geqslant 1 - \varepsilon/2^k$。如果令$K$为全有界集$\bigcap_{k=1}^{\infty} \bigcup_{i=1}^{n_k} A_{ki}$的闭包，则$K$为紧集（因$(X, \rho)$是完备的），且有$\inf\{P(K) \mid P \in \mathcal{H}\} \geqslant 1 - \varepsilon$。依定义，$\mathcal{H}$是胎紧的。（2）得证。

##### 习题

6.3.1 设 $(P_n) \subset \mathcal{P}(X)$. 若 $(P_n)$为相对紧的，且只有唯一的极限点 $P$，则 $P_n \xrightarrow{w} P$.

## 6.4 可分距离空间上概率测度的弱收敛

设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $(S,\rho)$为一可分距离空间。 $\Omega$到S中的Borel可测映射称为S值随机元。对随机元X，令

 
$$
\mu(A)=\mathbb{P}(X^{-1}(A)),\quad A\in\mathcal{B}(S),
$$
 

---

则 $\mu$为 $(S,\mathcal{B}(S))$上的概率测度.称 $\mu$为X的分布,记为 $\mathcal{L}(X)$.

定义6.4.1 设 $(\Omega_{n},\mathcal{F}_{n},\mathbb{P}_{n})_{n\geqslant1}$为一列概率空间， $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $X_{n}$及X分别为 $(\Omega_{n},\mathcal{F}_{n},\mathbb{P}_{n})$及 $(\Omega,\mathcal{F},\mathbb{P})$上的S值随机元，其分布为 $\mu_{n}$及 $\mu$。如果 $\mu_{n}\xrightarrow{w}\mu$，则称 $(X_{n})$依分布收敛于X，记为 $X_{n}\xrightarrow{d}X$。

设 $X_{n}$及X都是定义于同一概率空间 $(\Omega,\mathcal{F},\mathbb{P})$上的S值随机元．若 $\rho(X_{n},X)\stackrel{\mathrm{a.s.}}{\rightarrow}0$，则称 $(X_{n})$a.s.收敛于X，记为 $X_{n}\stackrel{\mathrm{a.s.}}{\rightarrow}X$；如果 $\rho(X_{n},X)\stackrel{\mathrm{p}}{\rightarrow}0$，则称 $(X_{n})$依概率收敛于X，记为 $X_{n}\stackrel{\mathrm{p}}{\rightarrow}X$.

显然 $X_n \xrightarrow{a.s.} X \Rightarrow X_n \xrightarrow{d} X$。下一命题表明 $X_n \xrightarrow{p} X \Rightarrow X_n \xrightarrow{d} X$。

命题6.4.2 设 $(X_n)$及 $X$为 $(\Omega, \mathcal{F}, \mathbb{P})$上的 $S$值随机元. 若 $X_n \xrightarrow{p} X$, 则对任何 $f \in C_b(S)$, 有 $\lim_{n \to \infty} \mathbb{P}(|f(X_n) - f(X)|) = 0$. 特别有 $X_n \xrightarrow{d} X$.

证 由定理2.3.4及2.3.5知： $X_{n} \stackrel{\mathrm{p}}{\rightarrow} X$，当且仅当对 $(X_{n})$ 的任一子列 $(X_{n'})$ 存在其子列 $(X_{n_k'})$，使 $X_{n_k'} \stackrel{\mathrm{a.s.}}{\rightarrow} X$。于是 $X_{n} \stackrel{\mathrm{p}}{\rightarrow} X$ 蕴含 $f(X_{n}) \stackrel{\mathrm{p}}{\rightarrow} f(X)$， $\forall f \in C_b(S)$。又由于 $f$ 有界，故有 $\lim_{n \to \infty} \mathbb{P}(|f(X_n) - f(X)|) = 0$。特别，令 $\mu_n$ 及 $\mu$ 分别为 $X_n$ 及 $X$ 的分布，则有

 
$$
\mu_{n}(f)=\mathbb{P}(f(X_{n}))\to\mathbb{P}(f(X))=\mu(f).
$$
 

这表明 $\mu_{n}\xrightarrow{w}\mu,$即 $X_{n}\xrightarrow{d}X.$

下一定理称为Skorohod-Dudley表示定理，它表明可分距离空间上的概率测度的弱收敛可以表示为随机元序列的a.s.收敛。这样一来可以使一些结果的证明变得简单和清晰。原先结果是1956年Skorohod在Theor. Probab. Apps. 1中对波兰空间情形给出的，下面的一般结果是1968年Dudley在Ann. Math. Statist. 39中给出的。这里的证明取自Dudley(2002).

定理6.4.3 设$(S,d)$为一可分距离空间，$(P_n)$为$(S,\mathcal{B}(S))$上的一列概率测度。如果$P_n\xrightarrow{w}P$，则存在一概率空间及其上的一列$S$值随机元$X_0,X_1,X_2,\cdots$，使得$P$为$X_0$的分布，$P_n$为$X_n$的分布，且$X_n\xrightarrow{\text{a.s.}}X_0$。

证 由于$S$有可数稠密子集，且除了至多可数多个$r>0$外，开球$B(x,r)=\{y\mid d(x,y)<r\}$为$P$连续集，故容易证明：对任意$m=1,2,\cdots$，我们能够将$S$分为互不相交直径小于$m^{-2}$的$P$连续可测集$A_{1m},A_{2m},\cdots$。不妨假定对一切$j,m,P(A_{jm})>0$。取$k(m)$足够大，使得$P(\sum_{i\leq k(m)}A_{im})>1-m^{-2}$。由定理6.2.4知，对一切$j$和$m$，有$\lim_{n\to\infty}P_n(A_{jm})=P(A_{jm})$。于是可取$n_m$足够大，使得$\forall j=1,\cdots,k(m),n\geq n_m$，有$P_n(A_{jm})>(1-m^{-2})P(A_{jm})$。我们可以假定$n_m$严格单调增且趋于$\infty$。对$n\geq n_1$存在唯一的$m=m(n)$，使得$n_m\leq n<n_{m+1}$。令

 
$$
\eta_{n}(B)=(1-m^{-2})\sum_{1\leqslant j\leqslant k(m)}\mathbb{P}(A_{j m})\mathbb{P}_{n}(B|A_{j m}),B\in\mathcal{B}(S),
$$
 

---

其中 $\mathbb{P}(B|A) = \mathbb{P}(BA)/\mathbb{P}(A)$. 又令 $\alpha_n = \mathbb{P}_n - \eta_n$, 则 $\eta_n$和非负测度. 再令 $I = (0,1], S_n = S, \mathcal{F}_n = \mathcal{B}(S), n \geq 0$, 定义

 
$$
\Omega=I\times\prod_{n\geqslant0}S_{n},\mathcal{F}=\mathcal{B}(I)\times\prod_{n\geqslant0}\mathcal{F}_{n}.
$$
 

我们将在 $(\Omega, \mathcal{F})$上构造一概率测度 $Q$，使得坐标 $X_n$的分布为 $P_n, X_0$的分布为 $P$，且 $d(X_n, X_0) \to 0, Q$-a.s..为此，给空间 $(I, \mathcal{B}(I))$和 $(S_0, \mathcal{F}_0)$分别赋予Lebesgue测度和概率测度 $P$。对 $(t, x) \in I \times S_0$，定义 $(S_n, \mathcal{B}(S_n))$上的概率测度如下：

 
$$
\mu_{n}(t,x)(\cdot)=P_{n},\  如果 \;n<n_{1};
$$
 

 
$$
\mu_{n}(t,x)(\cdot)=\mathbb{P}_{n}(\cdot|A_{jm(n)}), 如果 t\geqslant m(n)^{-2},x\in A_{jm(n)},1\leqslant j\leqslant k_{m(n)};
$$
 

 
$$
\mu_{n}(t,x)(\cdot)=\alpha_{n}/\alpha_{n}(S), 其他情形 .
$$
 

令 $E=\prod_{n\geq1}S_n,\mathcal{E}=\prod_{n\geq1}\mathcal{F}_n$。对 $(t,x)\in I\times S_0$，用 $\mu(t,x,\cdot)$表示 $(E,\mathcal{E})$上由 $\mu_n(t,x,\cdot)$产生的乘积概率测度，则 $\mu(t,x,\cdot)$为从 $(I\times S_0,\mathcal{B}(I)\times\mathcal{F}_0)$到 $(E,\mathcal{E})$上的概率核。

在 $(\Omega,\mathcal{F})$上构造一概率测度Q如下：

 
$$
\mathcal{Q}(W)=\int_{I}\int_{S}\int_{E}I_{W}(t,x,y)\mu(t,x,d y)I P(d x)d t,\quad W\in\mathcal{F}.
$$
 

对 $y=(x_{1},x_{2},\cdots)\in E$，令 $X_{0}(t,x,y)=x$， $X_{n}(t,x,y)=x_{n}$， $n\geqslant1$。则当 $n<n_{1}$时，显然有 $QX_{n}^{-1}=P_{n}$。对 $n\geqslant n_{1}$，由于

 
$$
\alpha_{n}(S)=1-(1-m^{-2})\sum_{1\leqslant j\leqslant k(m)}IP(A_{jm}),
$$
 

这里 $m=m(n)$，我们有

 
$$
\begin{align*}\mathbb{Q}X_{n}^{-1}(B)=&(1-m^{-2})\sum_{1\leq j\leq k(m)}\mathbb{P}(A_{jm})\mathbb{P}_{n}(B|A_{jm})\\&+(1-m^{-2})\Big(1-\sum_{1\leq j\leq k(m))}\mathbb{P}(A_{jm})\alpha_{n}(B)/\alpha_{n}(S)\Big)\\&+m^{-2}\alpha_{n}(B)/\alpha_{n}(S)\\=&\eta_{n}(B)+\alpha_{n}(B)=\mathbb{P}_{n}(B).\end{align*}
$$
 

由于当 $n \geqslant n_{1}$时有

 
$$
\mu_{n}(t,x)(A_{jm(n)})=1, 如果 t\geqslant m(n)^{-2},x\in A_{jm(n)},1\leqslant j\leqslant k_{m(n)},
$$
 

且 $A_{jm}$的直径小于 $m^{-2}$，于是有

 
$$
\left[(t,X_{0})\in[m(n)^{-2},1]\times\Sigma_{j=1}^{k_{m(n)}}A_{j,m(n)}\right]\subset[d(X_{0},X_{n})<m(n)^{-2}].
$$
 

---

注意左边的集合只依赖于 $m(n)$（不直接依赖于 $n$）。为了方便，将其余集记为 $E_{m(n)}$。于是 $[d(X_0, X_n) > m(n)^{-2}] \subset E_{m(n)}$，从而有

 
$$
\bigcap_{k=1}^{\infty}\bigcup_{n=k}^{\infty}[d(X_{0},X_{n})>m(n)^{-2}]\subset\bigcap_{k=1}^{\infty}\bigcup_{n=k}^{\infty}E_{m(n)}=\bigcap_{k=1}^{\infty}\bigcup_{m=k}^{\infty}E_{m}.
$$
 

由 $k_{m}$的选取, 我们知道  $Q(E_{m}) \leqslant 1 - (1 - m^{-2})^{2} \leqslant 2m^{-2}$. 由Borel-Cantelli引理, 我们得到

 
$$
\begin{array}{r l}&{\mathcal{Q}(\bigcap_{k=1}^{\infty}\bigcup_{n=k}^{\infty}[d(X_{0},X_{n})>m(n)^{-2}])=0,}\end{array}
$$
 

从而 $d(X_{n},X_{0})\to0,\mathbb{Q}-\mathrm{a.s.}$

##### 习题

6.4.1 设 $X_n$为 $(\Omega_n, \mathcal{F}_n, \mathbb{P}_n)$上的 $S$值随机元， $a \in S$。则 $X_n \xrightarrow{d} a \Longleftrightarrow X_n \xrightarrow{p} a$。

6.4.2 设  $X_{n}$ 及  $Y_{n}$ 是  $(\Omega_{n}, \mathcal{F}_{n}, \mathbb{P}_{n})$ 上的 S 值随机元，X 为  $(\Omega, \mathcal{F}, \mathbb{P})$ 上的随机元。如果  $\forall \varepsilon > 0$，有  $\lim_{n \to \infty} \mathbb{P}_{n}(\rho(X_{n}, Y_{n}) \geq \varepsilon) = 0$，则  $X_{n} \xrightarrow{d} X \Longleftrightarrow Y_{n} \xrightarrow{d} X$。

6.4.3 证明命题6.2.7的如下推广：设 $(X,\rho)$及 $(Y,d)$为两个距离空间， $\mathbb{P}, \mathbb{P}_1, \mathbb{P}_2, \cdots$为 $\mathcal{B}(X)$上的概率测度， $\mathbb{P}_n \xrightarrow{w} \mathbb{P}$。又设 $C \in \mathcal{B}(X)$， $f_1, f_2, \cdots$为X到Y中的Borel可测映射。如果 $\mathbb{P}(\xi \in C) = 1$，且对 $s_n \to s \in C$有 $f(s_n) \to f(s)$，则 $\mathbb{P}_n f_n^{-1} \xrightarrow{w} \mathbb{P} f^{-1}$。

### 6.5 局部紧Hausdorff空间上Radon测度的淡收敛

由定理6.1.2我们自然引进如下的定义：

定义6.5.1 设X为一局部紧Hausdorff空间， $\mu,\mu_{1},\mu_{2},\cdots$ 为  $\mathcal{B}(X)$ 上的Radon测度. 如果对一切  $f\in C_{c}(X)$，有

 
$$
\lim_{n\to\infty}\int f d\mu_{n}=\int f d\mu,
$$
 

则称 $(\mu_{n})$淡收敛于 $\mu$，记为 $\mu_{n}\xrightarrow{v}\mu$.

由Riesz表示定理知，淡收敛的极限是唯一的.

命题6.5.2 设X为局部紧Hausdorff空间， $\mu_{1},\mu_{2},\cdots$ 为 $\mathcal{B}(X)$ 上的Radon测度. 如果对一切 $f\in C_{c}(X)$，下述极限存在且有穷：

$$
\lim_{n\to\infty}\int f d\mu_{n}=l(f),   \tag*{(6.5.1)}
$$

则存在 $\mathcal{B}(X)$上唯一的Radon测度 $\mu$，使得 $\mu_n \xrightarrow{v} \mu$.

---

证 $l$为$C_c(X)$上的正线性泛函，故由 Riesz 表示定理，存在唯一的 Radon 测度$\mu$使$\forall f \in C_c(X)$，有 $l(f) = \mu(f)$。由 (6.5.1) 式知 $\mu_n \xrightarrow{v} \mu$。

引理6.5.3 设X为一具可数基的局部紧Hausdorff空间, $\mu$为 $\mathcal{B}(X)$上一Radon测度,则对任一紧集K,存在一包含K的 $\mu$连续紧集.

证 由习题5.1.9知，存在一列紧集 $(K_n)$，使 $K_n \subset K_{n+1}, n \geq 1$，且 $X = \bigcup_n K_n$。于是存在某个 $n$，使 $K \subset K_n^\circ$。令 $\rho$为X上与拓扑相容的距离（见习题5.1.11），则存在 $\delta > 0$，使 $\{x \mid \rho(x, K) \leq \delta\} \subset K_n^\circ$。令 $T_t = \{x \mid \rho(x, K) \leq t\}$，则 $\partial F_t = \{x \mid \rho(x, K) = t\}$。由于 $\partial F_t \cap \partial F_s = \varnothing, t \neq s$，且 $\partial F_t \subset K_n^\circ, 0 < t \leq \delta$，故存在某 $t_0 \in (0, \delta)$，使 $\mu(\partial F_{t_0}) = 0$（注意： $\mu(K_n^\circ) = \mu(K_n) < \infty$）。于是 $F_{t_0}$为包含 $K$的 $\mu$连续紧集。

定理6.5.4 设X为一局部紧Hausdorff空间, $\mu,\mu_{1},\mu_{2},\cdots$ 为 $\mathcal{B}(X)$上的Radon测度.考虑下列命题:

(1)  $\mu_n \xrightarrow{v} \mu;$

(2) 对一切紧集 K，有  $\limsup_{n\to\infty}\mu_{n}(K)\leqslant\mu(K)$，对一切相对紧开集 G，有  $\mu(G)\leqslant\liminf_{n\to\infty}\mu_{n}(G)$;

(3) 对一切  $\mu$ 连续相对紧 Borel 集 B, 有  $\lim_{n\to\infty}\mu_{n}(B)=\mu(B)$.

(1) $\Rightarrow(2)\Rightarrow(3)$. 若X具有可数基, 则上述三命题等价.

证 (1)  $\Rightarrow$ (2). 设  $\mu_{n} \xrightarrow{v} \mu$, K 为紧集. 对任给  $\varepsilon > 0$, 由  $\mu$ 的正则性, 存在开集  $U \supset K$, 使  $\mu(U) < \mu(K) + \varepsilon$. 于是由命题 5.1.20(2), 存在  $f \in C_{c}(X)$, 使得  $I_{K} \leqslant f \leqslant I_{U}$. 因此, 我们有

 
$$
\limsup_{n\to\infty}\mu_{n}(K)\leqslant\lim_{n\to\infty}\mu_{n}(f)\leqslant\mu(U)<\mu(K)+\varepsilon.
$$
 

由于 $\varepsilon$是任意的，故有 $\limsup_{n\to\infty}\mu_{n}(K)\leq\mu(K)$。现设G为相对紧开集。对任给 $\varepsilon>0$，存在紧集 $K\subset G$，使 $\mu(G)<\mu(K)+\varepsilon$。取 $f\in C_{c}(X)$，使 $I_{K}\leq f\leq I_{G}$，则有

 
$$
\liminf_{n\to\infty}\mu_{n}(G)\geqslant\lim_{n\to\infty}\mu_{n}(f)=\mu(f)\geqslant\mu(K)>\mu(G)-\varepsilon.
$$
 

由于 $\varepsilon>0$是任意的，故有 $\liminf_{n\to\infty}\mu_{n}(G)\geq\mu(G)$.

(2)⇒(3)由下式看出(注意 $\overline{B}$为紧集, $B^{\circ}$为相对紧开集):

 
$$
\begin{align*}\limsup_{n\to\infty}\mu_{n}(B)&\leqslant\limsup_{n\to\infty}\mu_{n}(\overline{B})\leqslant\mu(\overline{B})=\mu(B^{\circ})\\&\leqslant\liminf_{n\to\infty}\mu_{n}(B^{\circ})\leqslant\liminf_{n\to\infty}\mu_{n}(B).\end{align*}
$$
 

现在假定X为具有可数基的局部紧Hausdorff空间. 为证(1)、(2)、(3)等价, 只需证(3)⇒(1). 设(3)成立, 令 $f \in C_c(X)$, 由引理6.5.3, 存在 $\mu$连续紧集C, 使 $C \supset \operatorname{supp}(f)$. 令

 
$$
\nu_{n}(B)=\mu_{n}(B\cap C),\;\nu(B)=\mu(B\cap C).
$$
 

---

则对任何 $B \subset X$,

 
$$
\begin{align*}\partial(B\cap C)&=\overline{B\cap C}\setminus(B^{\circ}\cap C^{\circ})\\&\subset\overline{B}\cap C\setminus(B^{\circ}\cap C^{\circ})\\&\subset(\partial B\cap C)\cup\partial C).\end{align*}
$$
 

于是对任何ν连续集B, B ∩ C为μ连续集. 从而由(3)知,

 
$$
\lim_{n\to\infty}\nu_{n}(B)=\lim_{n\to\infty}\mu_{n}(B\cap C)=\mu(B\cap C)=\nu(B).
$$
 

但X为可距离化空间，故由命题6.2.4知 $\nu_n \xrightarrow{w} \nu$。由于 $\text{supp}(f) \subset C$，因此有

 
$$
\lim_{n\to\infty}\mu_{n}(f)=\lim_{n\to\infty}\nu_{n}(f)=\nu(f)=\mu(f).
$$
 

由于 $f\in C_{c}(X)$是任意的，故依定义有 $\mu_{n}\to v\mu.$

下一命题用弱收敛来刻画淡收敛.

命题6.5.5 设X为一具有可数基的局部紧Hausdorff空间，$\mu_{1},\mu_{2},\cdots$ 为$\mathcal{B}(X)$ 上的Radon测度. 令$(G_{k})$ 为一列相对紧开集，使$G_{k}\uparrow X.(G_{k})$ 的存在性见习题5.1.9). 任取$f_{k}\in C_{c}(X)$，使$I_{G_{k}}\leqslant f_{k}\leqslant1$ （见命题5.1.20(2)）. 令$\nu_{k,n}=f_{k}.\mu_{n}$，则下列二断言等价：

(1)  $\mu_n \xrightarrow{v} \mu;$

(2)  $\forall k, \nu_{k,n} \xrightarrow{w} \nu_{k}, n \to \infty.$

此外，这时有 $\nu_{k}=f_{k}.\mu.$

证 (1)  $\Rightarrow$ (2) 显然. 往证 (2)  $\Rightarrow$ (1). 设 (2) 成立, 令  $f \in C_c(X)$, 则由于  $\sup p(f)$ 为紧集, 故存在某  $k_0$, 使  $\sup p(f) \subset G_{k_0}$. 又由于  $I_{G_{k_0}} \leqslant f_{k_0} \leqslant 1$, 故有  $fG_{k_0} = f$. 因此, 下述极限存在且有穷:

 
$$
\lim_{n\to\infty}\mu_{n}(f)=\lim_{n\to\infty}\mu_{n}(f f_{k_{0}})=\lim_{n\to\infty}\nu_{k_{0},n}(f),
$$
 

故由命题6.5.2知， $(\mu_{n})$ 淡收敛于某Radon测度 $\mu$。命题最后一断言显然。

作为命题6.5.5的一个重要推论, 我们得到一族Radon测度关于淡收敛拓扑为相对紧的准则.

定理6.5.6 设X为一具有可数基的局部紧Hausdorff空间，M为 $\mathcal{B}(X)$上的一族Radon测度。则为要M关于淡收敛拓扑为相对紧的(即M中的任一序列有淡收敛子列)，必须且只需对任何紧集K，有 $\sup_{u\in M}\mu(K)<\infty$。

证 由定理6.5.4知必要性显然. 现证充分性. 设对任何紧集K,  $\sup_{\mu\in M}\mu(K)<\infty$. 令 $(G_{k})$为一列相对紧开集,  $G_{k}\uparrow X$,  $(f_{k})\subset C_{c}(X)$, 使 $I_{G_{k}}\leqslant f_{k}\leqslant1,k\geqslant1$.

---

对$\mu \in M$，令$\widetilde{\mu}_k = f_k \cdot \mu$。则对每个$k$及$\mu \in M$，$\widetilde{\mu}_k$在紧集supp$(f_k)$的余集上为0。又由于$\sup_{\mu \in M} \widetilde{\mu}_k(X) < \infty$，故由Prohorov定理(定理6.3.4)易知：每个$\widetilde{M}_k = \{\widetilde{\mu}_k \mid \mu \in M\}$按弱收敛拓扑是相对紧的(参见引理6.2.2)。现设$(\mu_n)$为$M$中的一序列，则用对角线法则，可选其一子列$(\mu_{n_j})$，使得$\forall k \geq 1$，$f_k \cdot \mu_{n_j} \xrightarrow{w} \text{某}\mu_k, j \to \infty$。故由命题6.5.5知$\mu_{n_j} \xrightarrow{w} \text{某}\mu$。这表明$M$按淡收敛相对紧。

为了进一步研究Radon测度的淡收敛, 我们需要下述引理.

引理6.5.7 设X为一具有可数基的局部紧Hausdorff空间, 令B为一紧集(相应地, 开集). 则存在紧集(相应地, 相对紧开集) $B_n$ 和 $f_n \in C_c(X), n \geq 1$, 使得

 
$$
I_{B}\leqslant f_{n}\leqslant I_{B_{n}}\downarrow I_{B}( 相应地 ,I_{B}\geqslant f_{n}\geqslant I_{B_{n}}\uparrow I_{B}).
$$
 

证 由习题5.1.9, 存在相对紧开集序列 $(G_n, n \geq 1)$, 使 $G_n \uparrow X$. 设B为紧集, 则存在某 $n_0$, 使 $B \subset G_{n_0}$. 任取X上与拓扑相容的距离 $\rho$, 令

 
$$
B^{\varepsilon}=\{x\mid\rho(x,B)\leqslant\varepsilon\},
$$
 

则当 $\varepsilon>0$足够小，有 $B^{\varepsilon}\subset G_{n_{0}}.$ 记 $B_{n}=B^{\frac{\varepsilon}{n}},n\geqslant1,$ 令

 
$$
f_{n}(x)=1-\frac{n}{\varepsilon}\big(\rho(x,B)\wedge\frac{\varepsilon}{n}\big),
$$
 

则 $f_n \in C_c(X)$， $I_B \leqslant f_n \leqslant I_{B_n} \downarrow I_B$。对相对紧开集 $B$，类似可证引理结论。对一般开集 $B$，可考虑相对紧开集 $G_n$。我们将证明细节留给读者。

下一定理表明: 淡收敛拓扑是可以距离化的.

定理6.5.8 设X为有可数基的局部紧Hausdorff空间, 令R表示B(X)上Radon测度全体, 则R按淡收敛拓扑为波兰空间.

证 设C为X的可数基，不妨设C对有限并闭，且C 中的元为相对紧的．由引理6.5.7，对 $C \in \mathcal{C}$，存在 $g_n \in C_c(X)$，使 $0 \leqslant g_n \uparrow I_C$．由于C中元素是可数的，我们可以把相应于所有 $C \in \mathcal{C}$的序列 $(g_n)$合并排列为 $f_1, f_2, \cdots$，则Radon测度 $\mu$显然由 $\{\mu(f_k), k = 1, 2, \cdots\}$唯一决定，因后者决定了 $\mu$在 $\mathcal{C}$上的值．

由定理6.5.6易证： $\mu_{n} \rightarrow$ 某 $\mu$，当且仅当对一切 $k \geqslant 1, \mu_{n}(f_{k})$收敛于某实数 $c_{k}$。于是若令

 
$$
d(\mu,\mu^{\prime})=\sum_{k=1}^{\infty}2^{-k}\Big[1-\exp\{-|\mu(f_{k})-\mu^{\prime}(f_{k})|\}\Big],\quad\mu,\mu^{\prime}\in\mathcal{R},
$$
 

则$d$为$\mathcal{R}$上的距离，且$\mu_n \xrightarrow{v} \mu \Leftrightarrow d(\mu_n, \mu) \to 0$。此外，容易验证$(\mathcal{R}, d)$为可分完备距离空间。

---

##### 习题

6.5.1 补足引理6.5.7及定理6.5.8的证明细节.

6.5.2 设X为一具有可数基局部紧Hausdorff空间， $\mu, \mu_1, \mu_2, \cdots$ 为 $\mathcal{B}(X)$ 上的Radon测度，且 $\mu_n \to \nu \mu$。则对任何有紧支撑的 $\mu$ 连续有界Borel可测函数 $f$，有 $\mu_n(f) \to \mu(f)$（提示：利用命题6.5.5及命题6.2.8）。

6.5.3 设X为一具有可数基局部紧Hausdorff空间, $\mu,\mu_{1},\mu_{2},\cdots$ 为 $\mathcal{B}(X)$ 上的有限测度(从而为Radon测度)，则下列断言等价：

(1)  $\mu_n \xrightarrow{w} \mu;$

(2) $\mu_{n}\xrightarrow{v}\mu,$且 $\mu_{n}(X)\rightarrow\mu(X);$

(3)  $\mu_n \xrightarrow{v} \mu$,  $\inf\{\limsup\mu_n(K^c) \mid K$ 为紧集} = 0.

---

## 第 7 章 概率论基础选讲

由于本书不是一部概率论教材, 我们不打算系统介绍概率论的内容. 本章着重介绍与测度论有关的一些重要概率论基础问题.

## 7.1 独立性, 0-1 律, Bayes 公式

设$(\Omega, \mathcal{F}, \mathbb{P})$为一概率空间。在概率论中，我们称$\mathcal{F}$中的元为(随机)事件，称$\Omega$为必然事件，$\Omega$上的$\mathcal{F}$可测函数称为随机变量。设$\xi$为一随机变量，若$\xi$关于$\mathbb{P}$的积分存在，则称积分$\int_{\Omega} \xi \, d\mathbb{P}$为$\xi$的数学期望，记为$\mathbb{E}[\xi]$。概率为1成立的性质称为几乎必然成立，简称为a.s.成立。

事件的独立性概念是概率论的最重要的概念之一.

定义7.1.1 设A, B为二事件, 如果 $IP(A \cap B) = IP(A)IP(B)$, 称A与B独立. 更一般地, 设 $A_{1}, A_{2}, \cdots, A_{n}$为n个事件, 如果对任何 $m \leqslant n$及 $1 \leqslant k_{1} < k_{2} < \cdots < k_{m} \leqslant n$, 有

 
$$
\mathbb{P}(\bigcap_{j=1}^{m}A_{k_{j}})=\prod_{j=1}^{m}\mathbb{P}(A_{k_{j}}),
$$
 

称 $(A_{1},A_{2},\cdots,A_{n})$相互独立. 注意： $(A_{1},A_{2},\cdots,A_{n})$两两独立不一定相互独立.

定义7.1.2 设  $D = \{A_t, t \in T\}$ 为一族事件。如果对  $T$ 的任何非空有限子集  $S$，有  $\mathbb{P}(\bigcap_{s \in S} A_s) = \prod_{s \in S} \mathbb{P}(A_s)$，则称  $\mathcal{D}$ 中事件相互独立。设  $\{C_t, t \in T\}$ 为一族事件类，如果从每个事件类  $C_t$ 中任取一事件  $A_t$， $\{A_t, t \in T\}$ 中事件相互独立，则称  $\{C_t, t \in T\}$ 为独立（事件）类。设  $\{\xi_t, t \in T\}$ 为一族随机变量。若  $\{\sigma(\xi_t), t \in T\}$ 为独立事件类，则称  $\{\xi_t, t \in T\}$ 相互独立。

定理7.1.3(独立类的扩张) 设 $\{C_t, t \in T\}$为一独立事件类, 如果每个 $C_t$为 $\pi$类, 则 $\{\sigma(C_t), t \in T\}$为独立事件类.

证 不妨设Ω属于每个 $C_{t}$(因为添加必然事件Ω不影响独立性). 设 $n\geqslant2,S=\{s_{1},\cdots,s_{n}\}$为T的有限子集, 令

 
$$
\mathcal{D}=\Big\{A\in\mathcal{F}\Big|\mathbb{P}\big(A\cap\bigcap_{j=2}^{n}C_{j}\big)=\mathbb{P}(A)\cdot\prod_{j=2}^{n}\mathbb{P}(C_{j}),C_{j}\in\mathcal{C}_{s_{j}},2\leqslant j\leqslant n\Big\},
$$
 

则$\mathcal{D}\supset\mathcal{C}_{s_1},\mathcal{D}$为$\lambda$类，故由单调类定理知$\mathcal{D}\supset\sigma(\mathcal{C}_{s_1})$. 这表明$\{\sigma(\mathcal{C}_{s_1}),\mathcal{C}_{s_2},\cdots,\mathcal{C}_{s_n}\}$为独立事件类．依此类推，$\{\sigma(\mathcal{C}_{s_1}),\cdots,\sigma(\mathcal{C}_{s_n})\}$为独立事件类．由于$S$为$T$的任意非空

---

有限子集，故 $\{\sigma(\mathcal{C}_t), t \in T\}$为独立事件类。

下一命题给出了随机变量相互独立性的判别准则.

命题7.1.4 设$\{\xi_t, t \in T\}$为一族随机变量，则为要它们相互独立，必须且只需对$T$的任一有限子集$S = \{s_1, \cdots, s_n\}$，及$x_1, \cdots, x_n \in \mathbb{R}$，有

 
$$
\mathbb{P}(\xi_{s_{1}}\leqslant x_{1},\cdots,\xi_{s_{n}}\leqslant x_{n})=\prod_{j=1}^{n}\mathbb{P}(\xi_{s_{j}}\leqslant x_{j}).
$$
 

证 令  $C_t = \{[\xi_t \leqslant x], x \in \mathbb{R}\}, t \in T$，则  $C_t$ 为  $\pi$ 类。于是由定理7.1.3立刻推得命题的结论。

下一定理称为Borel-Cantelli引理, 它在概率论中非常有用. 它的推广形式见定理7.1.8和系8.2.18.

定理7.1.5 设 $\{A_{n}, n \geqslant 1\}$为一列事件.

(1) 若  $\sum_{n=1}^{\infty} \mathbb{P}(A_{n}) < \infty$，则  $\mathbb{P}(A_{n}, \mathrm{i.o.})=0;$

(2) 若进一步  $\{A_n, n \geq 1\}$ 为相互独立，则  $\sum_{n=1}^{\infty} \mathbb{P}(A_n) = \infty$ 蕴涵  $\mathbb{P}(A_n, \mathrm{i.o.}) = 1$。这里  $\{A_n, \mathrm{i.o.}\}$ 表示  $\{A_n, n \geq 1\}$ 中有无穷多个事件发生 (i.o. 是 infinitely often 的缩写)，即有  $\{A_n, \mathrm{i.o.}\} = \bigcap_{n=1}^{\infty} \bigcup_{n=1}^{\infty} A_n$。

 
$$
k=1\ n=k
$$
 

证 (1) 设  $\sum_{n=1}^{\infty} \mathbb{P}(A_n) < \infty$，由于  $\forall k \geq 1, \{A_n, \text{i.o.}\} \subset \bigcup_{n=k}^{\infty} A_n$，从而

 
$$
\mathbb{P}(A_{n},\mathrm{i.o.})\leqslant\mathbb{P}(\bigcup_{n=k}^{\infty}A_{n})\leqslant\sum_{n=k}^{\infty}\mathbb{P}(A_{n})\to0,\ k\to\infty.
$$
 

(2) 设  $\{A_{n}, n \geqslant 1\}$ 相互独立. 假定  $\sum_{n=1}^{\infty} \mathbb{P}(A_{n}) = \infty$, 则对任何 m > k 有(注意:  $1 - x \leqslant e^{-x}, \forall 0 \leqslant x \leqslant 1$)

 
$$
\begin{align*}1-I P(\bigcup_{n=k}^{m}A_{n})&=I P(\bigcap_{n=k}^{m}A_{n}^{c})=\prod_{n=k}^{m}(1-I P(A_{n}))\\&\leq\exp\{-\sum_{n=k}^{m}I P(A_{n})\}.\end{align*}
$$
 

因此，对一切 $k\geq1$，有

 
$$
\begin{aligned}&0\leqslant1-\mathbb{P}(\bigcup_{n=k}^{\infty}A_{n})=1-\lim_{m\rightarrow\infty}\mathbb{P}(\bigcup_{n=k}^{m}A_{n})\\&\leqslant\lim_{m\rightarrow\infty}\exp\{-\sum_{n=k}^{m}\mathbb{P}(A_{n})\}=0,\\ \end{aligned}
$$
 

---

从而有

 
$$
\mathbb{P}(A_{n},\mathrm{i.o.})=\mathbb{P}(\bigcap_{k=1}^{\infty}\bigcup_{n=k}^{\infty}A_{n})=\lim_{k\to\infty}\mathbb{P}(\bigcup_{n=k}^{\infty}A_{n})=1.
$$
 

系7.1.6 (Borel 0-1律) 设 $\{A_{n}, n \geqslant 1\}$为相互独立事件，则依 $\sum_{n} P(A_{n}) < \infty$或 $\infty$而有 $P(A_{n}, \text{i.o.})=0$或1.

引理7.1.7 设 $\{A_{k},1\leqslant k\leqslant n\}$为一列事件，则有

$$
\mathbb{P}(\bigcup_{k=1}^{n}A_{k})\geqslant\frac{(\sum_{k=1}^{n}\mathbb{P}(A_{k}))^{2}}{\sum_{i,k=1}^{n}\mathbb{P}(A_{i}A_{k})}.   \tag*{(7.1.1)}
$$

(7.1.1)式称为Chung-Erdős不等式(见Trans. Amer. Math. Soc. 72(1952), 179-186).

证 令  $X_{k}=I_{A_{k}}$ ，由 Schwarz 不等式得

 
$$
\Big(\mathbb{E}(\sum_{k=1}^{n}X_{k})\Big)^{2}\leqslant\mathbb{P}(\sum_{k=1}^{n}X_{k}>0)\mathbb{E}[(\sum_{k=1}^{n}X_{k})^{2}].
$$
 

由于 $\mathbb{P}(\sum_{k=1}^{n} X_{k} > 0) = \mathbb{P}(\bigcup_{i=k}^{n} A_{k})$，故(7.1.1)式得证.

下一定理是Borel-Cantelli引理的一个推广，由Kochen-Stone 在Illinois Journal of Mathematics 8(1964), 248-251 中给出。下面的简化证明来自严加安(2006)。

定理7.1.8 设 $\{A_{n},n\geqslant1\}$为一列事件，满足 $\sum_{n=1}^{\infty}IP(A_{n})=\infty$，则

$$
\begin{align*}\mathbb{P}(A_{n},\mathrm{i.o.})\geq&\limsup_{n\to\infty}\frac{(\sum_{k=1}^{n}\mathbb{P}(A_{k}))^{2}}{\sum_{i,k=1}^{n}\mathbb{P}(A_{i} A_{k})}\\=&\limsup_{n\to\infty}\frac{\sum_{1\leq i<k\leq n}\mathbb{P}(A_{i})\mathbb{P}(A_{k})}{\sum_{1\leq i<k\leq n}\mathbb{P}(A_{i} A_{k})}.\end{align*}   \tag*{(7.1.2)}
$$

特别地，若 $\{A_n, n \geq 1\}$中事件两两独立或负相关（即 $\mathbb{P}(A_i A_k) \leq \mathbb{P}(A_i)(\mathbb{P}(A_k), \forall i \neq k)$，则 $\mathbb{P}(A_n, i.o.) = 1$。

证 令 $a_{n}=(\sum_{k=1}^{n}P(A_{k}))^{2}$， $b_{n}=\sum_{i,k=1}^{n}P(A_{i}A_{k})$，则由 $\lim_{n\to\infty}a_{n}=\infty$及(7.1.1)式知 $\lim_{n\to\infty}b_{n}=\infty$。于是再由(7.1.1)式及 $\sum_{i,k=m+1}^{n}P(A_{i}A_{k})\leq b_{n}-b_{m}$推得

 
$$
\begin{align*}\mathbb{P}(\bigcup_{k=m+1}^{\infty}A_{k})&=\lim_{n\to\infty}\mathbb{P}(\bigcup_{k=m+1}^{n}A_{k})\\&\geq\limsup_{n\to\infty}\frac{(\sqrt{a_{n}}-\sqrt{a_{m}})^{2}}{b_{n}-b_{m}}=\limsup_{n\to\infty}\frac{a_{n}}{b_{n}}.\end{align*}
$$
 

在上式中令 $m \to \infty$ 即得(7.1.2)中的不等式. 由于 $\sum_{k=1}^{\infty} \mathbb{P}(A_k) = \infty$ 且

 
$$
\Big(\sum_{k=1}^{n}\mathbb{P}\big(A_{k}\big)\Big)^{2}\leqslant2\sum_{1\leqslant i<k\leqslant n}\mathbb{P}\big(A_{i}\big)\mathbb{P}\big(A_{k}\big)+\sum_{k=1}^{n}\mathbb{P}\big(A_{k}\big),
$$
 

---

故有

 
$$
\lim_{n\to\infty}\frac{\sum_{k=1}^{n}\mathbb{P}(A_{k})}{\sum_{1\leq i<k\leq n}\mathbb{P}(A_{i})\mathbb{P}(A_{k})}=0.
$$
 

由此推知7.1.2中的等式成立.

定义7.1.9 设 $\{\xi_{n}, n \geqslant 1\}$为一列随机变量，令

 
$$
\mathcal{D}=\bigcap_{n=1}^{\infty}\sigma\{\xi_{j},j>n\},
$$
 

称D为 $\{\xi_n, n \geq 1\}$的尾 $\sigma$代数，D中的元素称为 $\{\xi_n, n \geq 1\}$的尾事件。

下一定理称为Kolmogorov 0-1律.

定理7.1.10 独立随机变量序列的尾事件的概率为0或1.

证 设$\{\xi_n, n \geqslant 1\}$为独立随机变量序列。对任何$n \geqslant 1$，由定理7.1.3知：$\sigma(X_j, 1 \leqslant j \leqslant n)$与$\sigma(X_j, j > n)$独立。从而$\sigma(\xi_j, 1 \leqslant j \leqslant n)$与$\mathcal{D}$独立（$\mathcal{D}$是尾$\sigma$代数）。令$\mathcal{A} = \bigcup_{n=1}^{\infty} \sigma(\xi_j, 1 \leqslant j \leqslant n)$，则$\mathcal{A}$与$\mathcal{D}$独立。但$\mathcal{A}$为$\pi$类，故由定理7.1.3知，$\sigma(\mathcal{A})$与$\mathcal{D}$独立。显然$\mathcal{D} \subset \sigma(\mathcal{A}) = \sigma(\xi_j, j \geqslant 1)$，故$\mathcal{D}$与$\mathcal{D}$独立。于是对任何$D \in \mathcal{D}$，我们有$IP(D) = IP(D \cap D) = IP(D)^2$，从而$IP(D) = 0$或1。

下面介绍Hewitt-Savage 0-1律. 设 $(S,S)$为一可测空间, 令 $(S^{n},S^{n})$和 $(S^{\infty},S^{\infty})$分别表示n次乘积和无穷乘积空间. 令 $p:\mathbb{N}\to\mathbb{N}$为一双方单值映射, 如果除有限多个n外, 恒有 $p(n)=n$, 则称 $\mathbb{P}$为 $\mathbb{N}$的一个有限置换. 对任一有限置换 $\mathbb{P}$, 在 $S^{\infty}$上定义一置换 $T_{p}$如下:

 
$$
T_{p}(s)=(s_{p(1)},s_{p(2)},\cdots),\ s=(s_{1},s_{2},\cdots)\in S^{\infty}.
$$
 

关于所有有限置换不变的集合称为对称集， $S^{\infty}$ 中对称集全体构成  $S^{\infty}$ 的一子  $\sigma$ 代数，称为置换不变  $\sigma$ 代数.

下一定理称为Hewitt-Savage 0-1律.

定理7.1.11 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\xi=(\xi_{1},\xi_{2},\cdots)$为定义在 $(\Omega,\mathcal{F},\mathbb{P})$上，取值于 $(S,\mathcal{S})$的一列独立同分布随机元， $\mathcal{G}$为 $S^{\infty}$置换不变 $\sigma$代数，则 $\xi^{-1}(\mathcal{G})$中元素的概率为0或1.

证 令  $\pi_{n}$ 为  $(S^{\infty}, S^{\infty})$ 到  $(S^{n}, S^{n})$ 的投影映射， $\mathcal{F}_{n} = \pi_{n}^{-1}(S^{n})$，则  $S^{\infty} = \sigma(\cup_{n} \mathcal{F}_{n})$。设  $\mu$ 为  $\xi$ 在  $(S^{\infty}, S^{\infty})$ 上的分布。令  $A \in \mathcal{G}$，则由习题 1.3.4 知，存在  $B_{n} \in S^{n}$ 使得

 
$$
\operatorname*{l i m}_{n\to\infty}\mu(A\triangle\pi_{n}^{-1}(B_{n}))=0.
$$
 

令 $\widetilde{B}_{n}=S^{n}\times B_{n}$，则存在一有限置换 $p_{n}$，使得 $T_{p_{n}}\pi_{n}^{-1}(B_{n})=\pi_{2n}^{-1}(\widetilde{B}_{n})$。由于A为对称集，我们有

 
$$
\mu(A\triangle\pi_{2n}^{-1}(\widetilde{B}_{n}))=\mu(A\triangle\pi_{n}^{-1}(B_{n}))\to0.
$$
 

---

于是有

 
$$
\mu(A\triangle(\pi_{n}^{-1}(B_{n})\cap\pi_{2n}^{-1}(\widetilde{B}_{n}))\leqslant\mu(A\triangle\pi_{n}^{-1}(B_{n}))+\mu(A\triangle\pi_{2n}^{-1}(\widetilde{B}_{n}))\to0,
$$
 

从而

 
$$
\mu(\pi_{n}^{-1}(B_{n})\cap\pi_{2n}^{-1}(\widetilde{B}_{n}))\to\mu(A).
$$
 

但 $\pi_{n}^{-1}(B_{n})$与 $\pi_{2n}^{-1}(\widetilde{B}_{n})$在 $\mu$下独立，

 
$$
\mu(\pi_{n}^{-1}(B_{n})\cap\pi_{2n}^{-1}(\widetilde{B}_{n}))=\mu(\pi_{n}^{-1}(B_{n}))\mu(\pi_{2n}^{-1}(\widetilde{B}_{n}))\to\mu(A)^{2},
$$
 

这表明 $\mu(A)=0$或1. 由于 $A\in\mathcal{G}$是任意的, $\mu(A)=\mathbb{P}(\xi^{-1}(A))$, 故 $\xi^{-1}(\mathcal{G})$中元素的概率为0或1.

下一定理称为Neyman-Pearson引理, 它是统计学中似然比检验的理论基础.

定理7.1.12 设P和Q是可测空间( $\Omega,\mathcal{F}$)为上的两个概率测度, $\mathbb{P}(A)=\mathbb{P}(A\cap N)+\int_{A}g dQ$为IP关于Q的Lebesgue分解,这里 $Q(N)=0$,在N上约定 $g=\infty$.设a>0.令 $A(c)=[g>c]$,则F中任何满足 $Q(A)\leq Q(A(c))$的A,有 $P(A)\leq P(A(c))$.

证 设 $A\in\mathcal{F}$. 令 $F=I_{A(c)}-I_{A}$. 则 $F(g-c)\geq0$, 且在N上 $F\geq0$. 于是有

 
$$
\begin{align*}\mathbb{P}(A(c))-\mathbb{P}(A)&=\int Fd\mathbb{P}=\int_{N}Fd\mathbb{P}+\int Fgd\mathbb{Q}\\&\geq c\int Fd\mathbb{Q}=c(\mathbb{Q}(A(c))-\mathbb{Q}(A)).\end{align*}
$$
 

定义7.1.13 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间，A和B为两个事件，且 $\mathbb{P}(A)>0$。在A发生的条件下B发生的概率等于 $\mathbb{P}(AB)/\mathbb{P}(A)$，我们称之为B关于A的条件概率，记为 $\mathbb{P}(B|A)$。

设$\{H_1, \cdots, H_m\}$和$\{A_1, \cdots, A_n\}$是空间$\Omega$的两个有限可测划分，满足$P(H_j) > 0, P(A_i) > 0, \forall 1 \leqslant j \leqslant m, 1 \leqslant i \leqslant n$。如果$\{H_1, \cdots, H_m\}$为可能导致$\{A_1, \cdots, A_n\}$中某事件发生的“原因”事件，则将$P(H_j)$称为事件$H_j$的先验概率，假定它们是已知的。另外，假定在由事件$H_j$引发事件$A_i$发生的条件概率$P(A_i|H_j)$也是已知的，则事件$A_i$的发生是由事件$H_j$引发的概率$P(H_j|A_i)$为

$$
\mathbb{P}(H_{j}|A_{i})=\frac{\mathbb{P}(H_{j}\cap A_{i})}{\mathbb{P}(A_{i})}=\frac{\mathbb{P}(A_{i}|H_{j})\mathbb{P}(H_{j})}{\sum_{k=1}^{m}\mathbb{P}(A_{i}|H_{k})\mathbb{P}(H_{k})}.   \tag*{(7.1.3)}
$$

这就是18世纪中叶英国学者贝叶斯(Bayes)提出的“由结果推测原因”的概率公式，即著名的Bayes公式. 这里 $IP(H_{j}|A_{i})$称为事件 $A_{i}$发生条件下 $H_{j}$的后验概率.

自然提出如下问题: 假定条件概率 $\mathbb{P}(A_i|H_j), 1 \leqslant j \leqslant m, 1 \leqslant i \leqslant n$ 和后验概率 $\mathbb{P}(H_j|A_i), 1 \leqslant j \leqslant m, 1 \leqslant i \leqslant n$都已知, 如何确定先验概率 $\mathbb{P}(H_j), 1 \leqslant j \leqslant m, 1 \leqslant n$都已知.

---

 $m)$? 为了解决这一问题, 我们引进下列记号: 记  $p_i = \mathbb{P}(A_i)$,  $q_j = \mathbb{P}(H_j)$. 假定存在某个  $i^*$, 使得对所有  $j, 1 \leq j \leq m$, 有  $\mathbb{P}(A_i \cdot H_j) > 0$, 令

 
$$
p_{i^{*}j}=\mathbb{P}(H_{j}|A_{i^{*}}),~q_{i^{*}j}=\mathbb{P}(A_{i^{*}}|H_{j}),~r_{i^{*}j}=\frac{p_{i^{*}j}}{q_{i^{*}j}}.
$$
 

由于 $p_{i} \cdot p_{i} \cdot j = IP(A_{i} \cdot H_{j}) = q_{j} q_{i} \cdot j$，我们有 $\frac{q_{j}}{p_{i} \cdot s} = r_{i} \cdot j, 1 \leqslant j \leqslant m$，于是有

 
$$
\frac{q_{k}}{q_{j}}=\frac{r_{i^{*}k}}{r_{i^{*}j}},\quad1\leqslant j,k\leqslant m.
$$
 

因此，

 
$$
\frac{1}{q_{j}}=\frac{\sum_{k=1}^{m}r_{i^{*}k}}{r_{i^{*}j}},1\leqslant j\leqslant m,
$$
 

即有

$$
q_{j}=\frac{r_{i^{*}j}}{\sum_{k=1}^{m}r_{i^{*}k}},1\leqslant j\leqslant m.   \tag*{(7.1.4)}
$$

这一公式最先由K.W. Ng(1995)给出, 称为逆Bayes公式.

##### 习题

7.1.1 设 $(X_{n}, n \geqslant 1)$为独立随机变量序列，则

(1)  $\limsup_{n\to\infty}X_n$ 与  $\liminf_{n\to\infty}X_n$ 为退化随机变量(即 a.s. 等于某一常数);

(2) 为要  $P(\lim_{n\to\infty}X_n=0)=1$，必须且只需对任何 C>0，有  $\sum_{n}IP(|X_n|>C)<\infty$（提示：利用 Borel-Cantelli 引理）.

7.1.2 设 $(X_i, 1 \leq i \leq n)$为独立随机变量序列。若每个 $X_i$非负或可积，则有 $E[\prod_{i=1}^n X_i] = \prod_{i=1}^n E[X_i]$（提示：从简单随机变量过渡到非负随机变量）。

7.1.3 设X及Y为相互独立可积随机变量，且 $E[X]=0$，则 $E[|X+Y|]\geq E[|Y|]$（提示： $|y|=|E(y+X)|\leq E|y+X|$）.

7.1.4 设 $\left(\xi_{n}\right)$为一列非负实值随机变量，则存在一正实数序列 $\left(c_{n}\right)$，使得 $\sum_{n=1}^{\infty}c_{n}\xi_{n}<\infty$

a.s. （提示：取一正实数列 $(a_{n})$，使得 $\sum_{n=1}^{\infty}IP(\xi_{n}>a_{n})<\infty$，然后利用Borel-Cantelli引理并令 $c_{n}=(2^{n}a_{n})^{-1}$.）

7.1.5 设 $(\Omega,\mathcal{F},\mathbb{P})$为概率空间， $\xi_{1},\cdots,\xi_{n}$为非负随机变量，且 $E[\xi_{i}]=1,1\leqslant i\leqslant n$.

证明 $\prod_{i=1}^{n}\sum_{j=1}^{n}E[\xi_{i}\xi_{j}]\geqslant n$（提示：令 $\xi=\sum_{j=1}^{n}\xi_{j}$，将 $\prod_{i=1}^{n}\sum_{j=1}^{n}E[\xi_{i}\xi_{j}]$写成 $\exp\{\sum_{i=1}^{n}\log E[\xi_{i}\xi]\}$，然后用Jensen不等式，最后再用不等式 $x\log x\geqslant x-1,x>0$.

7.1.6 设 $(\Omega,\mathcal{F},\mathbb{P})$为概率空间， $A_{1},\cdots,A_{n}\in\mathcal{F},\mathbb{P}(A_{i})>0,1\leqslant i\leqslant n$。令 $A=\bigcup_{i=1}^{n}A_{i}$，证明 $\prod_{i=1}^{n}\frac{1}{n}\sum_{j=1}^{n}\frac{\mathbb{P}(A_{i}A_{j})}{\mathbb{P}(A_{i})\mathbb{P}(A_{j})}\geqslant\left(\frac{1}{\mathbb{P}(A)}\right)^{n}$（提示：利用上一题的结果）.

---

### 7.2 条件数学期望与条件独立性

设 $(B_j)_{1 \leq j \leq m}$为 $\Omega$的一个有限划分，且 $B_j \in \mathcal{F}$， $\mathbb{P}(B_j) > 0, 1 \leq j \leq m$。令 $\mathcal{G}$为由 $(B_j)$生成的 $\sigma$代数。对一可积随机变量 $X$，令

 
$$
\begin{array}{r}{\mathbb{E}[X|\mathcal{G}]=\displaystyle\sum_{j=1}^{m}\frac{\mathbb{E}[X I_{B_{j}}]}{\mathbb{P}(B_{j})}I_{B_{j}},}\end{array}
$$
 

称  $\mathbb{E}[X|\mathcal{G}]$ 为  $X$ 关于  $\mathcal{G}$ 的条件 (数学) 期望. 如果  $(A_i)_{1\leq i\leq n}$ 是  $\Omega$ 的一个有限划分, 且  $A_i \in \mathcal{F}, 1 \leq i \leq n$,  $X = \sum_{i=1}^n a_i I_{A_i}$ 为一简单随机变量, 则易知

 
$$
\mathbb{E}[X|\mathcal{G}]=\sum_{j=1}^{m}\sum_{i=1}^{n}a_{i}\mathbb{P}(A_{i}|B_{j})I_{B_{j}}.
$$
 

 $E(X|\mathcal{G})$ 是一  $\mathcal{G}$ 可测随机变量，满足：

$$
\mathbb{E}[\mathbb{E}[X|\mathcal{G}]I_{B}]=\mathbb{E}[X I_{B}],\quad\forall B\in\mathcal{G}.   \tag*{(7.2.1)}
$$

下面我们将条件期望推广到一般随机变量及σ代数情形. 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间, $\mathcal{G}$为 $\mathcal{F}$的一子σ代数. 设X为数学期望存在的随机变量, 令 $\nu=X$.IP为X关于IP的不定积分, 即

 
$$
\nu(A)=\int_{A}X d\mathbb{P},\ A\in\mathcal{F},
$$
 

则ν为符号测度，且ν关于IP绝对连续。若将ν及IP都限于(Ω,ζ)，则仍有ν ⇔ IP。令Y为ν关于IP在(Ω,ζ)上的Radon-Nikodym导数(见定理3.3.11)，则Y为ζ可测随机变量，且有

 
$$
\mathbb{E}[Y I_{B}]=\mathbb{E}[X I_{B}],\quad\forall B\in\mathcal{G},
$$
 

我们称随机变量Y为X关于G的条件(数学)期望．由命题3.1.8知：在IP等价意义下，条件期望Y是唯一确定的，我们把它记为E[X|G]，它由(7.2.1)式所刻画.

定理7.2.1 条件期望有如下基本性质：

(1)  $\mathbb{E}[\mathbb{E}[X|\mathcal{G}]]=\mathbb{E}[X];$

(2) 若 X 为 G 可测，则  $E[X | G] = X$，a.s.;

(3) 设  $\mathcal{G} = \{\varnothing, \Omega\}$，则  $E[X | \mathcal{G}] = E[X]$，a.s.;

(4)  $\mathbb{E}[X|\mathcal{G}]=\mathbb{E}[X^{+}|\mathcal{G}]-\mathbb{E}[X^{-}|\mathcal{G}],\text{ a.s.}$;

(5)  $X \geqslant Y$, a.s.  $\Rightarrow E[X|G] \geqslant E[Y|G]$, a.s.;

(6) 设  $c_{1}, c_{2}$ 为实数， $X, Y, c_{1}X + c_{2}Y$ 的期望存在，则

 
$$
\begin{array}{r}{\mathbb{E}[c_{1}X+c_{2}Y|\mathcal{G}]=c_{1}\mathbb{E}[X|\mathcal{G}]+c_{2}\mathbb{E}[Y|\mathcal{G}],\mathrm{a.s.},}\end{array}
$$
 

---

如果右边和式有意义;

(7)  $|E[X|\mathcal{G}]| \leqslant E[|X|\mid\mathcal{G}],\text{ a.s.}$;

(8) 设  $0 \leqslant X_n \uparrow X$, a.s., 则  $E[X_n|G] \uparrow E[X|G]$, a.s.;

(9) 设 X 及 XY 的期望存在，且 Y 为 G 可测，则

$$
\mathbb{E}[X Y|\mathcal{G}]={Y\mathbb{E}[X|\mathcal{G}],\mathrm{a.s.}};   \tag*{(7.2.2)}
$$

(10) (条件期望的平滑性) 设  $G_1, G_2$ 为  $F$ 的子  $\sigma$ 代数，且  $G_1 \subset G_2$，则

$$
\begin{array}{r}{\mathbb{E}[\mathbb{E}[X|\mathcal{G}_{2}]|\mathcal{G}_{1}]=\mathbb{E}[X|\mathcal{G}_{1}],\mathrm{a.s.};}\end{array}   \tag*{(7.2.3)}
$$

(11) 若  $X$ 与  $\mathcal{G}$ 相互独立 (即  $\sigma(X)$ 与  $\mathcal{G}$ 相互独立), 则有  $E[X|G] = E[X]$, a.s..

证 (1)-(7)容易由条件期望定义直接看出.

(8) 由(5)知,  $\mathbb{E}[X_n|\mathcal{G}] \uparrow Y$, a.s.,  $Y$ 为  $\mathcal{G}$ 可测随机变量.于是, 对一切  $B \in \mathcal{G}$,

 
$$
\int_{B}Y d\boldsymbol{P}=\lim_{n\rightarrow\infty}\int_{B}\boldsymbol{E}[\boldsymbol{X}_{n}|\boldsymbol{\mathcal{G}}]d\boldsymbol{P}=\lim_{n\rightarrow\infty}\int_{B}\boldsymbol{X}_{n}d\boldsymbol{P},
$$
 

从而 $Y=\mathbb{E}[X|\mathcal{G}],\mathrm{a.s.}$

(9) 不妨设X及Y皆为非负随机变量. 首先设 $Y = I_A, A \in \mathcal{G}$, 则 $\mathbb{E}[X | \mathcal{G}]$为 $\mathcal{G}$可测, 且对一切 $B \in \mathcal{G}$, 有

 
$$
\begin{align*}\int_{B}Y\mathbb{E}[X|\mathcal{G}]d\mathbb{P}&=\int_{A\cap B}\mathbb{E}[X|\mathcal{G}]d\mathbb{P}=\int_{A\cap B}X d\mathbb{P}\\&=\int_{B}X I_{A}d\mathbb{P}=\int_{B}Y X d\mathbb{P},\end{align*}
$$
 

故7.2.2式成立. 然后利用8即可由简单随机变量过渡到一般非负随机变量.

(10) 设  $B \in \mathcal{G}_1$，则

 
$$
\int_{B}\mathbb{E}[\mathbb{E}[X|\mathcal{G}_{2}]|\mathcal{G}_{1}]d\mathbb{P}=\int_{B}\mathbb{E}[X|\mathcal{G}_{2}]d\mathbb{P}=\int_{B}X d\mathbb{P},
$$
 

故有7.2.3式.

(11) 不妨设  $X$ 为非负随机变量. 设  $A \in \mathcal{G}$, 由于  $I_A$ 与  $X$ 相互独立, 故由习题 7.1.1 知

 
$$
\int_{A}\mathbb{E}[X]d\mathbb{P}=\mathbb{E}[X]\mathbb{P}(A)=\mathbb{E}[X I_{A}]=\int_{A}X d\mathbb{P},
$$
 

故 $E[X]=E[X|\mathcal{G}],\mathrm{a.s.}$

关于条件期望, 我们有相应的单调收敛定理, Fatou引理, 控制收敛定理, Hölder不等式及Minkowski不等式, 它们的证明与第三章关于积分情形相应结果的证明类

---

似．因此，下面我们只叙述结果而略去证明．注意：对概率空间情形，a.s.收敛总蕴含依概率收敛.

在下面几个定理中， $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数.

定理7.2.2 (单调收敛定理) 设 $(X_{n})$为随机变量序列，且每个 $X_{n}$的期望存在.

(1) 设  $X_n \uparrow X$, a.s., 且  $E[X_1] > -\infty$, 则  $X$ 的期望存在, 且  $E[X_n | \mathcal{G}] \uparrow E[X | \mathcal{G}]$, a.s.;

(2) 设  $X_n \downarrow X$, a.s., 且  $E[X_1] < \infty$, 则  $X$ 的期望存在, 且  $E[X_n | \mathcal{G}] \downarrow E[X | \mathcal{G}]$, a.s..

定理7.2.3 (Fatou引理) 设 $(X_{n})$为随机变量序列，且每个 $X_{n}$的期望存在.

(1) 若存在随机变量  $Y$，使  $E[Y] > -\infty$，且  $\forall n \geq 1$，有  $X_n \geq Y$，a.s.，则  $\liminf_{n \to \infty} X_n$ 的期望存在，且有

 
$$
\begin{array}{r}{\mathbb{E}[\operatorname*{l i m}\operatorname*{i n f}_{n\to\infty}X_{n}|\mathcal{G}]\leqslant\operatorname*{l i m}\operatorname*{i n f}_{n\to\infty}\mathbb{E}[X_{n}|\mathcal{G}];}\end{array}
$$
 

(2) 若存在随机变量Y，使E[Y] < ∞，且  $\forall n \geq 1$，有  $X_n \leq Y$，a.s.，则  $\limsup_{n \to \infty} X_n$ 的期望存在，且有

 
$$
\mathbb{E}[\limsup_{n\to\infty}X_{n}|\mathcal{G}]\geqslant\limsup_{n\to\infty}\mathbb{E}[X_{n}|\mathcal{G}].
$$
 

定理7.2.4 (控制收敛定理) 设 $X_n \xrightarrow{\text{a.s.}} X$ (相应地,  $X_n \xrightarrow{\text{p}} X$), 若存在非负可积随机变量 $Y$, 使 $|X_n| \leqslant Y$, a.s., 则 $X$可积, 且有 $\lim_{n \to \infty} E[X_n | \mathcal{G}] = E[X | \mathcal{G}]$, a.s. (相应地,  $E[X_n | \mathcal{G}] \xrightarrow{\text{p}} E[X | \mathcal{G}]$).

下一定理是控制收敛定理的推广形式.

定理7.2.5 设 $X_n \xrightarrow{\text{a.s.}} X, Y_n \xrightarrow{\text{a.s.}} Y$（相应地， $X_n \xrightarrow{\text{p}} X, Y_n \xrightarrow{\text{p}} Y$），其中 $Y$及每个 $Y_n$为非负可积随机变量。如果对 $n \geq 1$， $|X_n| \leq Y_n$， $\text{a.s.}$， $\mathbb{E}[Y_n | \mathcal{G}] \xrightarrow{\text{a.s.}} E[Y | \mathcal{G}]$（相应地， $\mathbb{E}[Y_n | \mathcal{G}] \xrightarrow{\text{p}} E[Y | \mathcal{G}]$），则有 $\mathbb{E}[|X_n - X||\mathcal{G}] \xrightarrow{\text{a.s.}} 0$（相应地， $\mathbb{E}[|X_n - X||\mathcal{G}] \xrightarrow{\text{p}} 0$）。特别有 $\mathbb{E}[X_n | \mathcal{G}] \xrightarrow{\text{a.s.}} E[X | \mathcal{G}]$（相应地， $\mathbb{E}[X_n | \mathcal{G}] \xrightarrow{\text{p}} E[X | \mathcal{G}]$）。

证 只需考虑a.s.收敛情形. 令 $Z_{n}=Y_{n}+Y-|X_{n}-X|$，则 $Z_{n}\geq0$，且 $Z_{n}\xrightarrow{\text{a.s.}}2Y$. 故由Fatou引理得

 
$$
2\mathbb{E}[Y|\mathcal{G}]\leqslant\liminf_{n\to\infty}\mathbb{E}[Z_{n}|\mathcal{G}]=2\mathbb{E}[Y|\mathcal{G}]-\limsup_{n\to\infty}\mathbb{E}[\left|X_{n}-X\right|\left|\mathcal{G}\right],
$$
 

于是有  $\lim_{n\to\infty}E[|X_n-X||\mathcal{G}]=0.$

定理7.2.6 (Hölder不等式) 设 $1<p,q<\infty,\quad1/p+1/q=1$，则

 
$$
\begin{array}{r}{\mathbb{E}[\left|X Y\right|\left|\mathcal{G}\right]\leqslant\left(\mathbb{E}[\left|X\right|^{p}|\mathcal{G}]\right)^{1/p}(\mathbb{E}[\left|Y\right|^{q}|\mathcal{G}])^{1/q}.}\end{array}
$$
 

---

定理7.2.7 (Minkowski不等式) 设 $p \geqslant 1$，则

 
$$
(\mathbb{E}[|X+Y|^{p}|\mathcal{G}])^{1/p}\leqslant(\mathbb{E}[|X|^{p}|\mathcal{G}])^{1/p}+(\mathbb{E}[|Y|^{p}|\mathcal{G}])^{1/p}.
$$
 

下面将条件期望概念推广到最一般情形(见严加安(1990)).

定义7.2.8 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $X$为一随机变量， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数。若 $\mathbb{E}[X^+|\mathcal{G}]-\mathbb{E}[X^-|\mathcal{G}]$ a.s.有定义，即

 
$$
\begin{array}{r}{\mathbb{P}(\mathbb{E}[X^{+}|\mathcal{G}]=\infty,\mathbb{E}[X^{-}|\mathcal{G}]=\infty)=0,}\end{array}
$$
 

则称X关于G的条件期望存在，并令(约定 $\infty-\infty=0$)

 
$$
\mathbb{E}[X|\mathcal{G}]=\mathbb{E}[X^{+}|\mathcal{G}]-\mathbb{E}[X^{-}|\mathcal{G}].
$$
 

我们称  $\mathbb{E}[X|\mathcal{G}]$ 为 X 关于  $\mathcal{G}$ 的条件期望.

若$\mathcal{G}=\{\varnothing,\Omega\}$, 则$X$关于$\mathcal{G}$的条件期望存在, 当且仅当$X$的期望存在. 此外, 任何$\mathcal{G}$可测的随机变量$X$关于$\mathcal{G}$的条件期望存在, 且$E[X|\mathcal{G}]=X$, a.s..

下一定理给出了条件期望存在的随机变量的一个有用刻画.

定理7.2.9 下列二断言等价：

(1) X关于 $\mathcal{G}$的条件期望存在;

(2) 存在  $\mathcal{G}$ 可测实值随机变量  $\xi$， $|\xi| > 0$，a.s.，使  $\xi X$ 的期望存在。

证  $(1)\Rightarrow(2)$. 设(1)成立. 令

 
$$
A=[{\mathbb{I}}E[X^{+}|{\mathcal{G}}]=\infty],\qquad B=[{\mathbb{I}}E[X^{-}|{\mathcal{G}}]=\infty],
$$
 

则 $\mathbb{P}(A \cap B) = 0$. 令 $\eta = I_{A^c} - I_A$, 则 $|\eta| = 1$,  $\eta$为 $\mathcal{G}$可测, 且有 $(\eta X)^+ = \eta^+ X^+ + \eta^- X^-$, 故有

 
$$
\begin{array}{r}{\mathbb{E}[(\eta X)^{+}|\mathcal{G}]=I_{A^{c}}\mathbb{E}[X^{+}|\mathcal{G}]+I_{A}\mathbb{E}[X^{-}|\mathcal{G}]<\infty,\mathrm{~a.s.~}.}\end{array}
$$
 

令 $\xi = \eta/(1 + \mathbb{E}[(\eta X)^+|\mathcal{G}])$，则 $\mathbb{E}[(\xi X)^+|\mathcal{G}] < 1$，a.s.。特别有 $\mathbb{E}[(\xi X)^+] < 1$，于是 $\xi X$的期望存在。

 $(2)\Rightarrow(1)$由下一定理的 $(1)$推得.

下一定理是定理7.2.1的推广.

定理7.2.10 7.2.8定义的条件期望有下列性质：

(1) 设 X 关于 G 的条件期望存在，则对任何 G 可测实值随机变量  $\xi, \xi X$ 关于 G 的条件期望也存在，且有

$$
\mathbb{E}[\xi X|\mathcal{G}]=\xi\mathbb{E}[X|\mathcal{G}],\mathrm{a.s.}.   \tag*{(7.2.4)}
$$


---

(2) 设  $X_1, X_2$ 关于  $\mathcal{G}$ 的条件期望存在. 若  $X_1 + X_2$ 及  $\mathbb{E}[X_1|\mathcal{G}] + \mathbb{E}[X_2|\mathcal{G}]$ a.s. 有意义, 则  $X_1 + X_2$ 关于  $\mathcal{G}$ 的条件期望存在, 且有

$$
\begin{array}{r}{\mathbb{E}[X_{1}+X_{2}|\mathcal{G}]=\mathbb{E}[X_{1}|\mathcal{G}]+\mathbb{E}[X_{2}|\mathcal{G}],\mathrm{a.s.}.}\end{array}   \tag*{(7.2.5)}
$$

(3) 设  $G_1$ 及  $G_2$ 为  $F$ 的子  $\sigma$ 代数，且  $G_1 \subset G_2$。若  $X$ 关于  $G_1$ 的条件期望存在，则  $X$ 关于  $G_2$ 的条件期望存在， $E[X|G_2]$ 关于  $G_1$ 的条件期望存在，且有

$$
\mathbb{E}[\mathbb{E}[X|\mathcal{G}_{2}]|\mathcal{G}_{1}]=\mathbb{E}[X|\mathcal{G}_{1}].   \tag*{(7.2.6)}
$$

证 (1) 我们有 $(\xi X)^{+}=\xi^{+}X^{+}+\xi^{-}X^{-},(\xi X)^{-}=\xi^{+}X^{-}+\xi^{-}X^{+}$. 于是有

$$
\begin{array}{r}{\mathbb{E}[(\xi X)^{+}|\mathcal{G}]=\xi^{+}\mathbb{E}[X^{+}|\mathcal{G}]+\xi^{-}\mathbb{E}[X^{-}|\mathcal{G}],}\end{array}   \tag*{(7.2.7)}
$$

$$
\mathbb{E}[(\xi X)^{-}|\mathcal{G}]=\xi^{-}\mathbb{E}[X^{+}|\mathcal{G}]+\xi^{+}\mathbb{E}[X^{-}|\mathcal{G}].   \tag*{(7.2.8)}
$$

由于假定  $\mathbb{E}[X^+|\mathcal{G}]-\mathbb{E}[X^-|\mathcal{G}]$ a.s. 有意义，故  $\xi X$ 关于  $\mathcal{G}$ 的条件期望存在。由(7.2.7)式及(7.2.8)式推得(7.2.4)式。

(2) 令

 
$$
A=[{\mathbb{I}}E[X_{1}|\mathcal{G}]=-\infty],\quad B=[{\mathbb{I}}E[X_{2}|\mathcal{G}]=-\infty],
$$
 

则依假定,  $E[X_1|\mathcal{G}] + E[X_2|\mathcal{G}]$ a.s.有意义, 故在A上a.s.有  $E[X_1|\mathcal{G}] < \infty$, 在B上a.s.有  $E[X_2|\mathcal{G}] < \infty$, 于是有

$$
I_{A}\mathbb{E}[X_{1}^{+}|\mathcal{G}]<\infty,\mathrm{a.s.},\quad I_{B}\mathbb{E}[X_{2}^{+}|\mathcal{G}]<\infty,\mathrm{a.s.}.   \tag*{(7.2.9)}
$$

令 $\xi=I_{A\cup B}-I_{A^{c}\cap B^{c}}$，则 $|\xi|=1$， $\xi$为 $\mathcal{G}$可测。记 $Y=\xi(X_{1}+X_{2})$，我们有

 
$$
Y^{+}\leqslant\xi^{+}(X_{1}^{+}+X_{2}^{+})+\xi^{-}(X_{1}^{-}+X_{2}^{-}),
$$
 

$$
\begin{align*}\mathbb{E}[Y^{+}|\mathcal{G}]&\leq\mathbb{E}[\xi^{+}(X_{1}^{+}+X_{2}^{+})+\xi^{-}(X_{1}^{-}+X_{2}^{-})|\mathcal{G}]\\&=I_{A\cup B}(\mathbb{E}[X_{1}^{+}|\mathcal{G}]+\mathbb{E}[X_{2}^{+}|\mathcal{G}])\\&+I_{A^{c}\cap B^{c}}(\mathbb{E}[X_{1}^{-}|\mathcal{G}]+\mathbb{E}[X_{2}^{-}|\mathcal{G}])<\infty,\mathrm{a.s.}.\end{align*}   \tag*{(7.2.10)}
$$

特别，Y关于G的条件期望存在. 于是由(1)知， $X_{1}+X_{2}$关于G的条件期望存在. 令

 
$$
\begin{aligned}&Z_{1}=\xi^{+}(X_{1}^{+}+X_{2}^{+})+\xi^{-}(X_{1}^{-}+X_{2}^{-}),\\&Z_{2}=\xi^{-}(X_{1}^{+}+X_{2}^{+})+\xi^{+}(X_{1}^{-}+X_{2}^{-}),\\ \end{aligned}
$$
 

则 $Y = Z_1 - Z_2$，且由 $(7.2.10)$知， $\mathbb{E}[Z_1|\mathcal{G}] < \infty$，a.s.。令 $\eta = \frac{1}{1 + \mathbb{E}[Z_1|\mathcal{G}]}$，则 $\mathbb{E}[\eta Z_1] = \mathbb{E}[\eta \mathbb{E}[Z_1|\mathcal{G}]] \leq 1$，因此 $\eta Y$的期望存在。故由 $(7.2.4)$式及定理 $7.2.1(6)$有

---

 
$$
\begin{align*}\mathbb{E}[Y|\mathcal{G}]&=\frac{1}{\eta}\mathbb{E}[\eta Y|\mathcal{G}]=\frac{1}{\eta}(\mathbb{E}[\eta Z_{1}|\mathcal{G}]-\mathbb{E}[\eta Z_{2}|\mathcal{G}])\\&=\frac{1}{\eta}(\eta\mathbb{E}[Z_{1}|\mathcal{G}]-\eta\mathbb{E}[Z_{2}|\mathcal{G}])=\mathbb{E}[Z_{1}|\mathcal{G}]-\mathbb{E}[Z_{2}|\mathcal{G}]\\&=\xi(\mathbb{E}[X_{1}|\mathcal{G}]+\mathbb{E}[X_{2}|\mathcal{G}]),\end{align*}
$$
 

由此及 $(7.2.4)$式便得 $(7.2.5)$式.

(3) 设 X 关于  $G_{1}$ 的条件期望存在. 由定理 7.2.9 知, 存在  $G_{1}$ 可测实值随机变量  $\xi$,  $|\xi| > 0$, a.s., 且  $\xi X$ 的期望存在. 由于  $\xi$ 为  $G_{2}$ 可测, 故仍由定理 7.2.9 知, X 关于  $G_{2}$ 的条件期望存在, 且由 (7.2.4) 式得

 
$$
\mathbb{E}[X|\mathcal{G}_{2}]=\frac{1}{\xi}\mathbb{E}[\xi X|\mathcal{G}_{2}].
$$
 

由于 $E[\xi X|\mathcal{G}_2]$的期望存在，故由(1)及上式知 $E[X|\mathcal{G}_2]$关于 $\mathcal{G}_1$的条件期望存在，且有(利用(7.2.3)式)

 
$$
\mathbb{E}[\mathbb{E}[X|\mathcal{G}_{2}]|\mathcal{G}_{1}]=\frac{1}{\xi}\mathbb{E}[\mathbb{E}[\xi X|\mathcal{G}_{2}]|\mathcal{G}_{1}]=\frac{1}{\xi}\mathbb{E}[\xi X|\mathcal{G}_{1}]=\mathbb{E}[X|\mathcal{G}_{1}].
$$
 

(7.2.6)式得证.

下面讨论一类特殊的关于 $\mathcal{G}$条件期望存在的随机变量.

定义7.2.11 设 $(\Omega, \mathcal{F}, \mathbb{P})$为一概率空间， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数。称随机变量X关于 $\mathcal{G}$为 $\sigma$可积，如果存在 $\Omega_n \in \mathcal{G}$， $\Omega_n \uparrow \Omega$，使每个 $X I_{\Omega_n}$为可积。

下一定理给出了关于 $\pmb{\mathscr{G}}$为 $\sigma$可积的随机变量的一个刻画.

定理7.2.12 设X为一随机变量, 则下列断言等价:

(1) X关于 $\mathcal{G}$为 $\sigma$可积;

(2) X关于 $\mathcal{G}$的条件期望存在，且 $\mathbb{E}[X|\mathcal{G}]$ a.s.有穷；

(3) 存在一 $G$可测实值随机变量 $\xi$， $|\xi| > 0$，a.s.，使 $\xi X$为可积随机变量。

证 (1)  $\Rightarrow$ (3). 设(1)成立. 选取  $\Omega_n \in \mathcal{G}, \Omega_n \uparrow \Omega$, 使每个  $XI_{\Omega_n}$ 为可积. 令

 
$$
\xi=\sum_{n=1}^{\infty}\frac{1}{2^{n}(1+\mathbb{E}[|X|I_{\Omega_{n}}])}I_{\Omega_{n}}\;,
$$
 

则 $\xi>0$， $\xi$为 $\mathcal{G}$可测实值随机变量，且 $\xi X$为可积。

(3)⇒(2)显然．往证(2)⇒(1)．设E[X|G] a.s.有穷，由于E[X|G] = E[X+|G] - E[X-|G]，故E[|X||G] < ∞，a.s.. 令Ωₙ = [E[|X||G] ≤ n]，则Ωₙ ↑ Ω，a.s., Ωₙ ∈ G，且XIΩₙ 为可积随机变量，故X关于G为σ可积．

下一定理给出了条件期望的Jensen不等式的最一般形式.

---

定理7.2.13 (Jensen不等式) 设$\varphi: \mathbb{R} \to \mathbb{R}$为一连续凸函数, $X$为一关于$\mathcal{G} \sigma$可积的随机变量, 则$\varphi(X)$关于$\mathcal{G}$的条件期望存在, 且有

$$
\varphi(\mathbb{E}[X|\mathcal{G}])\leqslant\mathbb{E}[\varphi(X)|\mathcal{G}],\mathrm{a.s.}.   \tag*{(7.2.11)}
$$

证 令 $\varphi'$为 $\varphi$的右导数，则对任意实数x,y有

 
$$
\varphi^{\prime}(x)(y-x)\leqslant\varphi(y)-\varphi(x).
$$
 

以 $E[X|\mathcal{G}]$及X代替上式中的x及y得

 
$$
\varphi^{\prime}(\mathbb{E}[X|\mathcal{G}])(X-\mathbb{E}[X|\mathcal{G}])+\varphi(\mathbb{E}[X|\mathcal{G}])\leqslant\varphi(X).
$$
 

记左边的随机变量为Y，则Y关于 $\mathcal{G}$的条件期望存在，且 $\mathbb{E}[Y|\mathcal{G}] = \varphi(\mathbb{E}[X|\mathcal{G}])$。由于 $\varphi(X)^{-} \leqslant Y^{-}$，故 $\mathbb{E}[\varphi(X)^{-}|\mathcal{G}] \leqslant \mathbb{E}[Y^{-}|\mathcal{G}] < \infty$，a.s.。因此， $\varphi(X)$关于 $\mathcal{G}$的条件期望存在，且有(7.2.11)式。

下面我们推广有关条件期望的单调收敛定理、Fatou引理、控制收敛定理和 $L^{r}$收敛定理.

定理7.2.14 设G为F的一子σ代数, $(X_{n},n\geq1)$为一列关于G条件期望存在的随机变量.

(1) (单调收敛定理) 设  $X_n \uparrow X$, a.s., 且  $E[X_1^+ | G] < \infty$, a.s., 则 X 关于  $\mathcal{G}$ 的条件期望存在 (实际有  $E[X^- | \mathcal{G}] < \infty$, a.s.), 且有  $E[X_n | \mathcal{G}] \uparrow E[X | \mathcal{G}]$, a.s..

(2) (Fatou引理) 若存在随机变量Y，使 $E[Y^{-}|G]<\infty$，a.s.，且对每个 $n\geq1$，有 $X_{n}\geq Y$，a.s.，则 $\liminf_{n\to\infty}X_{n}$关于G的条件期望存在(实际有 $E[(\liminf_{n\to\infty}X_{n})^{-}|G]<\infty$，a.s.)，且有

 
$$
\begin{array}{r}{\mathbb{I}E[\operatorname*{l i m}\operatorname*{i n f}_{n\to\infty}X_{n}|\mathcal{G}]\leqslant\operatorname*{l i m}\operatorname*{i n f}_{n\to\infty}\mathbb{I}E[X_{n}|\mathcal{G}],\mathrm{a.s.}.}\end{array}
$$
 

(3) (控制收敛定理) 设  $X_n \xrightarrow{\text{a.s.}} X, Y_n \xrightarrow{\text{a.s.}} Y$ (相应地,  $X_n \xrightarrow{P} X, Y_n \xrightarrow{P} Y$), 其中每个  $Y_n$ 为非负随机变量, 且  $Y$ 及每个  $Y_n$ 关于  $\mathcal{G}$ 为  $\sigma$ 可积. 如果对  $n \geq 1, |X_n| \leq Y_n$, a.s., 且  $E[Y_n| \mathcal{G}] \xrightarrow{\text{a.s.}} E[Y| \mathcal{G}]$ (相应地,  $E[Y_n| \mathcal{G}] \xrightarrow{P} E[Y| \mathcal{G}]$), 则有  $E[|X_n - X|| \mathcal{G}] \xrightarrow{\text{a.s.}} 0$ (相应地,  $E[|X_n - X|| \mathcal{G}] \xrightarrow{P} 0$), 特别有  $E[X_n| \mathcal{G}] \xrightarrow{\text{a.s.}} E[X| \mathcal{G}]$ (相应地,  $E[X_n| \mathcal{G}] \xrightarrow{P} E[X| \mathcal{G}]$).

(4)  $(L^{r}$收敛定理 $设$ \infty>r\geqslant1 $. 若 $X_{n}\stackrel{L^{r}}{\to}X$, 则 $E[X_{n}|\mathcal{G}]\stackrel{L^{r}}{\to}E[X|\mathcal{G}]$.

证 (1) 令  $\xi > 0$ 为一  $\mathcal{G}$ 可测实值随机变量，使  $\xi X_1^-$ 为可积，则  $\xi X_n$ 的期望存在，且  $\xi X_n \uparrow \xi X$，a.s.，故由定理7.2.2得  $\mathbb{E}[\xi X_n|\mathcal{G}] \uparrow \mathbb{E}[\xi X|\mathcal{G}]$，a.s.，但有  $\mathbb{E}[\xi X_n|\mathcal{G}] = \xi \mathbb{E}[X_n|\mathcal{G}]$， $\mathbb{E}[\xi X|\mathcal{G}] = \xi \mathbb{E}[X|\mathcal{G}]$，从而有  $\mathbb{E}[X_n|\mathcal{G}] \uparrow \mathbb{E}[X|\mathcal{G}]$，a.s.。

(2) 容易由(1)推得.

---

(3) 只需考虑a.s.收敛情形.令 $Z_{n}=Y_{n}+Y-|X_{n}-X|$，则 $Z_{n}\geq0$，且 $Z_{n}\xrightarrow{\mathrm{a.s.}}2Y$，故由(2)得

 
$$
2\mathbb{E}[Y|\mathcal{G}]\leqslant\liminf_{n\to\infty}\mathbb{E}[Z_{n}|\mathcal{G}]=2\mathbb{E}[Y|\mathcal{G}]-\limsup_{n\to\infty}\mathbb{E}[\left|X_{n}-X\right|\left|\mathcal{G}\right].
$$
 

于是有  $\lim_{n\to\infty}E[|X_n-X||\mathcal{G}]=0.$

(4) 令  $f(x) = |x|^{r}$，则 f 为  $\mathbb{R}$ 上的连续凸函数。故由 (7.2.11) 式得

 
$$
|\mathbb{E}[X_{n}|\mathcal{G}]-\mathbb{E}[X|\mathcal{G}]|^{r}\leqslant\mathbb{E}[|X_{n}-X|^{r}|\mathcal{G}].
$$
 

在不等式两边取期望即得欲证结论.

下一定理给出了计算一类条件期望的有用公式.

定理7.2.15 设$(\Omega, \mathcal{F}, \mathbb{P})$为一概率空间，$\mathcal{G}$为$\mathcal{F}$的一子$\sigma$代数；$(S, S)$和$(E, \mathcal{E})$为可测空间，$X$为一$\mathcal{G}$可测$S$值随机元，$Y$为一$E$值随机元。假定$Y$和$\mathcal{G}$独立（即$Y^{-1}(\mathcal{E})$与$\mathcal{G}$独立）。令$g(x, y)$为$S \times E$上的$\mathcal{S} \times \mathcal{E}$可测函数，使得$E[|g(X, Y)|] < \infty$，则有

$$
\mathbb{E}[g(X,Y)\mid\mathcal{G}]=\mathbb{E}[g(x,Y)]|_{x=X}.   \tag*{(7.2.12)}
$$

证 不妨假定 $g(x,y)$为非负 $S\times\mathcal{E}$可测函数. 令 $f(x)=\mathbb{E}[g(x,Y)]$. 为证(7.2.12), 只需证明对任意非负 $\mathcal{G}$可测随机变量Z, 有 $\mathbb{E}[g(X,Y)Z]=\mathbb{E}[f(X)Z]$. 为此令

 
$$
\begin{align*}\mu_{Y}(A)&=\mathbb{P}(Y^{-1}(A)),\quad A\in\mathcal{E};\\\mu_{X,Z}(B)&=\mathbb{P}((X,Z)^{-1}(B)),\quad B\in\mathcal{S}\times\mathcal{B}(\mathbb{R}).\end{align*}
$$
 

则有

 
$$
f(x)=\int g(x,y)\mu_{Y}(d y).
$$
 

由于Y和 $(X,Z)$独立,我们有

 
$$
\begin{align*}\mathbb{E}[g(X,Y)Z]&=\int zg(x,y)\mu_{Y}(dy)\mu_{X,Z}(dx,dz)\\&=\int zf(x)\mu_{X,Z}(dx,dz)=\mathbb{E}[Zf(X)].\end{align*}
$$
 

下一定理是条件期望的Bayes法则.

定理7.2.16 设Q为一关于IP绝对连续的概率测度, $\mathcal{G}$为F的一子 $\sigma$代数.令

 
$$
\xi=\frac{d\mathcal{Q}}{d\mathbb{P}},\qquad\eta=\mathbb{E}[\xi|\mathcal{G}].
$$
 

---

则 $\eta > 0$  $Q$-a.s.. 如果 $X$为一 $Q$可积的随机变量，则有

$$
E_{\mathcal{Q}}[X|\mathcal{G}]=\eta^{-1}\mathbb{I}E[X\xi|\mathcal{G}],\quad\mathcal{Q}\mathrm{-a.s.}.   \tag*{(7.2.13)}
$$

证 首先, 由于  $[\eta > 0] \in \mathcal{G}$, 我们有

 
$$
\begin{aligned}{\mathcal{Q}([\eta>0])=\mathbb{E}[\xi I_{[\eta>0]}]=\mathbb{E}[\eta I_{[\eta>0]}]=\mathbb{E}[\eta]=\mathbb{E}[\xi]=1.}\\ \end{aligned}
$$
 

设X为一Q可积的随机变量, 则有

 
$$
\begin{align*}\mathbb{E}[X\xi I_{A}]&=\mathbb{E}_{\mathcal{Q}}[X I_{A}]=E_{\mathcal{Q}}[\mathbb{E}_{\mathcal{Q}}[X|\mathcal{G}]I_{A}]\\&=\mathbb{E}[\mathbb{E}_{\mathcal{Q}}[X|\mathcal{G}]\xi I_{A}]=\mathbb{E}[\mathbb{E}_{\mathcal{Q}}[X|\mathcal{G}]\eta I_{A}],\ \forall A\in\mathcal{G}.\end{align*}
$$
 

这表明

 
$$
\mathbb{E}[X\xi|\mathcal{G}]=\mathbb{E}_{\mathcal{Q}}[X|\mathcal{G}]\eta,\;\mathbb{P}\mathrm{-a.s.},
$$
 

从而上一等式Q-a.s.成立. 由此立刻推得7.2.13.

设$\xi$为一可积随机变量，$Y$为由$(\Omega,\mathcal{F})$到$(E,\mathcal{E})$的一可测映射。常将$E[\xi|\sigma(Y)]$记为$E[\xi|Y]$。这时令

 
$$
\mu(A)=\mathbb{P}(Y^{-1}(A)),\ \nu(A)=\mathbb{E}[\xi I_{Y^{-1}(A)}],\ A\in\mathcal{E}.
$$
 

显然 $\nu$关于 $\mu$绝对连续. 令 $g=\frac{d\nu}{du}$，则由习题3.1.6知： $\forall A\in\mathcal{E}$，我们有

 
$$
\begin{aligned}{\mathbb{E}[g(Y)I_{Y^{-1}(A)}]=\int_{A}g(y)\mu(d y)=\nu(A)=\mathbb{E}[\xi I_{Y^{-1}(A)}].}\\ \end{aligned}
$$
 

这表明 $\mathbb{E}[\xi|Y]=g(Y)$。我们常用记号 $\mathbb{E}[\xi|Y=y]$形式上表示 $g(y)$，尽管函数 $g$只是 $\mu$-a.e.唯一确定，且 $[Y=y]$的概率可能为零。作为这一结果的推论，我们得到如下有用的结果。

定理7.2.17 设  $X = (X_{1}, \cdots, X_{m})$ 和  $Y = (Y_{1}, \cdots, Y_{n})$ 为两个随机向量， $h$ 为  $R^{m}$ 上的一Borel 函数，使得  $h(X_{1}, \cdots, X_{m})$ 可积。令  $\mu$ 为  $Y$ 在  $R^{n}$ 上诱导的测度，

 
$$
\nu(A)=\int_{\mathbb{R}^{m}\times A}h(x_{1},\cdots,x_{m})d F(x_{1},\cdots,x_{m},y_{1},\cdots,y_{n}),A\in\mathcal{B}(\mathbb{R}^{n}),
$$
 

其中 $F(x_{1},\cdots,x_{m},y_{1},\cdots,y_{n})$为X和Y的联合分布，则 $\nu$关于 $\mu$绝对连续，且有

$$
\mathbb{E}[h(X)|Y_{1},\cdots,Y_{n}]=g(Y_{1},\cdots,Y_{n}),   \tag*{(7.2.14)}
$$

其中$g$为$\nu$关于$\mu$的Radon-Nikodym导数. 如果分布函数$F$有密度函数$f(x_1,\cdots,x_m$, $y_1,\cdots,y_n)$, 则$g$有如下表达式:

 
$$
g(y_{1},\cdots,y_{n})=\frac{\int_{\mathbb{R}^{m}}h(x_{1},\cdots,x_{m})f(x_{1},\cdots,x_{m},y_{1},\cdots,y_{n})d x_{1}\cdots d x_{m}}{\int_{\mathbb{R}^{m}}f(x_{1},\cdots,x_{m},y_{1},\cdots,y_{n})d x_{1}\cdots d x_{m}},
$$
 

---

这里约定0/0=0.

定义7.2.18 设 $(\Omega, \mathcal{F}, \mathbb{P})$为概率空间， $B \in \mathcal{F}$。令 $P[B|G] = \mathbb{E}[I_B|G]$，并称之为 $B$关于 $G$的条件概率。设 $G, G_1$及 $G_2$为 $F$的子 $\sigma$代数。如果对任意 $B_1 \in G_1$及 $B_2 \in G_2$，有

$$
\mathbb{P}[B_{1}\cap B_{2}|\mathcal{G}]=\mathbb{P}[B_{1}|\mathcal{G}]\mathbb{P}[B_{2}|\mathcal{G}],\mathrm{a.s.},   \tag*{(7.2.15)}
$$

则称 $G_{1}$与 $G_{2}$关于G条件独立.

设 $G_{1}$与 $G_{2}$关于G条件独立，则对任意 $G_{1}$可测非负随机变量 $X_{1}$及 $G_{2}$可测非负随机变量 $X_{2}$，有

$$
\begin{array}{r}{\mathbb{E}[X_{1}X_{2}|\mathcal{G}]=\mathbb{E}[X_{1}|\mathcal{G}]\mathbb{E}[X_{2}|\mathcal{G}],\mathrm{a.s.}.}\end{array}   \tag*{(7.2.16)}
$$

设X及Y为随机变量. 若 $\sigma(X)$与 $\sigma(Y)$关于G条件独立, 则称X与Y关于G条件独立. 类似可定义一随机变量与一子 $\sigma$代数关于G的条件独立性.

下一定理给出了条件独立性的一个判别准则.

定理7.2.19 设 $(\Omega,\mathcal{F},\mathbb{P})$为概率空间, $\mathcal{G},\mathcal{G}_{1}$及 $\mathcal{G}_{2}$为 $\mathcal{F}$的子 $\sigma$代数.则为要 $\mathcal{G}_{1}$与 $\mathcal{G}_{2}$关于 $\mathcal{G}$条件独立,必须且只需对任意 $B_{2}\in\mathcal{G}_{2}$有

$$
\begin{array}{r}{\mathbb{P}[B_{2}|\mathcal{G}_{1}\vee\mathcal{G}]=\mathbb{P}[B_{2}|\mathcal{G}],\mathrm{a.s.}}\end{array}   \tag*{(7.2.17)}
$$

(或等价地, 对任意  $B_1 \in \mathcal{G}_1$, 有  $IP[B_1] \not\subseteq \mathcal{G}_2 \lor \mathcal{G}] = IP[B_1] \not\subseteq \mathcal{G}$, a.s.)

证 首先(7.2.17)式右边为 $\mathcal{G}_1 \vee \mathcal{G}$可测且 $\{B_1 \cap B \mid B_1 \in \mathcal{G}_1, B \in \mathcal{G}\}$为生成 $\mathcal{G}_1 \vee \mathcal{G}$的 $\pi$类，由条件期望的定义易知(7.2.17)等价于

$$
\int_{B\cap B_{1}}\mathbb{P}[B_{2}|\mathcal{G}]d\mathbb{P}=\int_{B}I_{B_{1}}I_{B_{2}}d\mathbb{P},\quad B\in\mathcal{G},\;B_{1}\in\mathcal{G}_{1}.   \tag*{(7.2.18)}
$$

另一方面，7.2.15等价于

$$
\int_{B}\mathbb{P}[B_{1}|\mathcal{G}]\mathbb{P}[B_{2}|\mathcal{G}]d\mathbb{P}=\int_{B}I_{B_{1}\cap B_{2}}d\mathbb{P},\quad B\in\mathcal{G}.   \tag*{(7.2.19)}
$$

但对 $B \in \mathcal{G}, B_1 \in \mathcal{G}_1, B_2 \in \mathcal{G}_2$，我们有

 
$$
\begin{align*}\int_{B\cap B_{1}}\mathbb{P}[B_{2}|\mathcal{G}]d\mathbb{P}&=\int_{B}I_{B_{1}}\mathbb{P}(B_{2}|\mathcal{G})d\mathbb{P}\\&=\int_{B}\mathbb{E}[I_{B_{1}}\mathbb{P}[B_{2}|\mathcal{G}]|\mathcal{G}]d\mathbb{P}\\&=\int_{B}\mathbb{P}[B_{1}|\mathcal{G}]\mathbb{P}[B_{2}|\mathcal{G}]d\mathbb{P},\end{align*}
$$
 

即7.2.18的左边与7.2.19的左边相等，因此定理得证.

---

##### 习题

7.2.1 设  $X \in L^1(\Omega, \mathcal{F}, \mathbb{P})$， $\mathcal{G}$ 为  $\mathcal{F}$ 的一子  $\sigma$ 代数， $Y \in L^1(\Omega, \mathcal{G}, \mathbb{P})$。为要  $Y = \mathbb{E}[X | \mathcal{G}]$，必须且只需  $EX = EY$ 且对生成  $\mathcal{G}$ 的某  $\pi$ 类  $C$ 中的所有集合  $A$ 有  $\mathbb{E}[X I_A] = \mathbb{E}[Y I_A]$。

7.2.2 设  $X, Y \in L^1(\Omega, \mathcal{F}, \mathbb{P})$. 若  $E(X|Y) = Y$, a.s.,  $\mathbb{E}[Y|X] = X$, a.s., 则  $X = Y$. a.s..

7.2.3 设  $X \in L^2(\Omega, \mathcal{F}, \mathbb{P})$， $\mathcal{G}$ 为  $\mathcal{F}$ 的一子  $\sigma$ 代数，则

 
$$
\mathbb{E}(\mathbb{E}[X|\mathcal{G}]-X)^{2}=\operatorname*{i n f}\{\mathbb{E}(Y-X)^{2}\mid Y\in L^{2}(\Omega,\mathcal{G},\mathbb{P})\}.
$$
 

7.2.4 设X及Y为(Ω, F, ℝ)上的实值随机变量,  $f(x, y)$ 为ℝ²上的非负或有界Borel可测函数. 令 $G_1$及 $G_2$为F的子σ代数, 若X与 $G_1 \vee G_2$独立, Y关于 $G_1 \cap G_2$可测, 则有

 
$$
\begin{aligned}\mathbb{E}[f(X,Y)|\mathcal{G}_{1}]&=\mathbb{E}[f(X,Y)|\mathcal{G}_{2}]\\&=\mathbb{E}[f(X,Y)|\mathcal{G}_{1}\cap\mathcal{G}_{2}],\mathrm{a.s.}.\end{aligned}
$$
 

(提示: 利用定理2.2.1.)

7.2.5 设X及Y为 $(\Omega,\mathcal{F},\mathbb{P})$上的实值随机变量, $\mathcal{G}_{1}$及 $\mathcal{G}_{2}$为F的子 $\sigma$代数,若X及 $\mathcal{G}_{1}$与Y及 $\mathcal{G}_{2}$独立,则有

 
$$
\mathbb{E}[X Y|\mathcal{G}_{1}\vee\mathcal{G}_{2}]=\mathbb{E}[X|\mathcal{G}_{1}]\mathbb{E}[Y|\mathcal{G}_{2}],\mathrm{a.s.}.
$$
 

7.2.6 设 $(\Omega, \mathcal{F}, \mathbb{P})$为一概率空间， $\mathcal{F}_1 \subset \mathcal{F}_2$为 $\mathcal{F}$的两个子 $\sigma$代数。如果 $A \in \mathcal{F}_1$，满足 $A \cap \mathcal{F}_1 = A \cap \mathcal{F}_2$，则对任何可积随机变量 $\xi$，有 $E[\xi | \mathcal{F}_1] I_A = E[\xi | \mathcal{F}_2] I_A$。

7.2.7 1) 设 X, Y, Z, W 为随机变量,  $(X, Z)$ 与  $(Y, W)$ 有相同的联合分布, 设 f 为非负 Borel 可测函数, 证明  $\mathbb{E}[f(X)|Z]$ 与  $\mathbb{E}[f(Y)|W]$ 同分布. 若 Z = W, 则  $\mathbb{E}[f(X)|Z] = \mathbb{E}[f(Y)|W]$, a.s.

2) 设 X, Y 为独立同分布可积随机变量, 试求  $E[X|X+Y]$.

7.2.8 设 $(X,Y)$服从二维标准正态分布，试求 $E[X^{2}|XY]$.

7.2.9 设 $(\Omega, \mathcal{F}, \mathbb{P})$为概率空间， $\mathcal{G}, \mathcal{H}, \mathcal{F}_n, n \geq 1$为 $\mathcal{F}$的子 $\sigma$代数。则为要 $\mathcal{H}$与 $(\mathcal{F}_n, n \geq 1)$关于 $\mathcal{G}$条件独立，必须且只需 $\mathcal{H}$与 $\mathcal{F}_1$关于 $\mathcal{G}$条件独立，且对一切 $n \geq 1$， $\mathcal{H}$与 $\mathcal{F}_{n+1}$关于 $\mathcal{G}$和 $(\mathcal{F}_n, n \geq 1)$条件独立。

7.2.10 设 $(\Omega, \mathcal{F}, \mathbb{P})$为概率空间， $(\xi_n, n \geq 1)$为一列非负可积随机变量， $(\mathcal{F}_n, n \geq 1)$为一列 $\mathcal{F}$的子 $\sigma$代数，使得 $E[\xi_n | \mathcal{F}_n]$依概率趋于0，证明 $\xi_n$也依概率趋于0（提示：利用习题3.1.7）.

## 7.3 正则条件概率

设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间, $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数.由条件期望的性质知, $\mathbb{P}(A|\mathcal{G})$有如下性质:

 
$$
\begin{aligned}&\mathbb{P}[\Omega|\mathcal{G}]=1,\mathrm{a.s.},\qquad\mathbb{P}[A|\mathcal{G}]\geqslant0,\mathrm{a.s.},\\&\mathbb{P}\Big[\sum_{j}A_{j}|\mathcal{G}\Big]=\sum_{j}\mathbb{P}[A_{j}|\mathcal{G}],\mathrm{a.s.}.\\ \end{aligned}
$$
 

---

这些性质与概率测度的性质很相似，不同之处在于出现了例外集。若对每个 $A \in \mathcal{F}$，可选取 $\mathbb{P}[A \mid \mathcal{G}]$的一个版本 $P(\omega, A)$，使得对一切 $\omega \in \Omega$， $P(\omega, \cdot)$为 $(\Omega, \mathcal{F})$上的概率测度，这时称 $\{P(\omega, A), \omega \in \Omega, A \in \mathcal{F}\}$为 $\mathbb{P}$关于 $\mathcal{G}$的正则条件概率。一般说来，即使 $(\Omega, \mathcal{F})$为可分可测空间，正则条件概率未必存在。本节将对可分可测空间情形给出使正则条件概率存在的一个充分条件(定理7.3.10)及一个充要条件(定理7.3.15)。

定义7.3.1 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数。令 $\{P(\omega,\cdot),\omega\in\Omega\}$为 $(\Omega,\mathcal{F})$上的一族概率测度，称它为 $\mathbb{P}$关于 $\mathcal{G}$的正则条件概率，如果：

(1)  $\forall A \in \mathcal{F}, P(\cdot, A)$ 为  $\Omega$ 上的  $\mathcal{G}$ 可测函数;

(2)  $\forall A \in \mathcal{F}, P(\omega, A)$ 为  $\mathbb{P}[A|\mathcal{G}]$ 的一个版本，即  $\forall B \in \mathcal{G}$ 有

 
$$
\int_{B}P(\omega,A)\mathbb{P}(d\omega)=\mathbb{P}(A\cap B).
$$
 

正则条件概率的第一个应用是: 条件期望算子成了关于正则条件概率的积分.

定理7.3.2 设 $\{P(\omega,\cdot),\omega\in\Omega\}$为 $P$关于 $\mathcal{G}$的正则条件概率。设 $X$为一随机变量，其期望存在，则对几乎所有 $\omega,X$关于 $P(\omega,\cdot)$的积分存在，且有

$$
\mathbb{E}[X|\mathcal{G}](\omega)=\int_{\Omega}X(\omega^{\prime})P(\omega,d\omega^{\prime}),\mathrm{a.s.}\omega.   \tag*{(7.3.1)}
$$

证 从示性函数过渡到非负可测函数, 证明细节从略.

在上述定理中, 如有从 $(\Omega, \mathcal{F})$到另一可测空间 $(\mathcal{E}, \mathcal{E})$的可测映射 $\xi$, 则可在 $(\mathcal{E}, \mathcal{E})$上引出一族概率测度 $\{Q(\omega, \cdot), \omega \in \Omega\}$:

$$
Q(\omega,A)=P(\omega,\xi^{-1}(A)),   \tag*{(7.3.2)}
$$

这时，对形如 $f(\xi)$的存在期望的随机变量 $(f\text{为}(E,\mathcal{E})$上的Borel可测函数)，有(见习题3.1.6)

$$
\mathbb{E}[f(\xi)|\mathcal{G}](\omega)=\int_{E}f(x)Q(\omega,d x).   \tag*{(7.3.3)}
$$

在许多情况下，正则条件概率并不存在，但满足(7.3.3)式的概率测度族 $\{Q(\omega,\cdot),\omega \in \Omega\}$存在。我们称 $\{Q(\omega,\cdot),\omega \in \Omega\}$为 $\xi$关于 $\mathcal{G}$的混合条件分布。

下面我们给出混合条件分布的确切定义.

定义7.3.3 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数。又设 $(E,\mathcal{E})$为一可测空间， $\xi$为 $(\Omega,\mathcal{F})$到 $(E,\mathcal{E})$中的可测映射。令 $\{Q(\omega,\cdot),\omega\in\Omega\}$为 $(E,\mathcal{E})$上的一族概率测度。称它为 $\xi$关于 $\mathcal{G}$的混合条件分布，如果：

(1)  $\forall A \in \mathcal{E}, Q(\cdot, A)$ 为  $\mathcal{G}$ 可测;

(2)  $\forall A \in \mathcal{E}, Q(\omega, A)$ 为  $\mathbb{P}[\xi^{-1}(A) | \mathcal{G}]$ 的一个版本，即  $\forall B \in \mathcal{G}$,

 
$$
\int_{B}Q(\omega,A)\mathbb{P}(d\omega)=\mathbb{P}(B\cap\xi^{-1}(A)),
$$
 

---

或者等价地，7.3.3式对 $(E,\mathcal{E})$上非负或有界的Borel可测函数成立.

注7.3.4 若 $(E,\mathcal{E})=(\Omega,\mathcal{F})$， $\xi$为 $\Omega$上的恒等映射，则 $\xi$关于 $\mathcal{G}$的混合条件分布就是 $\mathbb{P}$关于 $\mathcal{G}$的正则条件概率。因此，正则条件概率存在性的研究可以归结为混合条件分布存在性的研究。

下一定理给出了混合条件分布存在的一个有用的充分条件.

定理7.3.5 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $(E,\mathcal{E})$为一可分可测空间， $\xi$为 $(\Omega,\mathcal{F})$到 $(E,\mathcal{E})$中的一可测映射。令 $\mu=\mathbb{P}\xi^{-1}$，若 $\mu$是 $\mathcal{E}$上的紧测度(见定义4.5.4)，则对 $\mathcal{F}$的任一子 $\sigma$代数 $\mathcal{G}$，存在 $\xi$关于 $\mathcal{G}$的混合条件分布。

证 由第1章知：存在E上一代数A，其元素个数至多可数，使得 $\sigma(A)=\varepsilon$。此外，依假定，存在E上的一紧类 $C\subset\varepsilon$，使得对每个 $A\in\varepsilon$，有

 
$$
\mu(A)=\sup\{\mu(C)\mid C\subset A,C\in\mathcal{C}\}.
$$
 

因此，设 $A = \{A_1, A_2, \cdots\}$，则 $\forall i \geq 1$，存在 $C_{ik} \in \mathcal{C}$， $C_{ik} \subset A_i$， $k \geq 1$，使得

$$
\mu(A_{i})=\sup_{k}\mu(C_{i k}),i=1,2,\cdots.   \tag*{(7.3.4)}
$$

对每个 $A\in\mathcal{E}$，令 $\widetilde{Q}(\omega,A)$为 $\mathbb{E}[\xi^{-1}(A)|\mathcal{G}]$的一个版本，则

 
$$
\begin{align*}\mu(A_{i})&=\sup_{k}\mu(C_{ik})=\sup_{k}\mathbb{P}(\xi^{-1}(C_{ik}))\\&=\sup_{k}\int\widetilde{Q}(\omega,C_{ik})d\mathbb{P}\leqslant\int\sup_{k}\widetilde{Q}(\omega,C_{ik})d\mathbb{P}\\&\leqslant\int\widetilde{Q}(w,A_{i})d\mathbb{P}=\mathbb{P}(\xi^{-1}(A_{i}))=\mu(A_{i}).\end{align*}
$$
 

因此有

$$
\sup_{k}\widetilde{Q}(\omega,C_{i k})=\widetilde{Q}(\omega,A_{i}),\mathrm{a.s.}   \tag*{(7.3.5)}
$$

现令 $D = \{C_{ik}, i, k = 1, 2, \cdots\}$，并令 $A_1$为由 $A$及 $D$生成的代数，则 $A_1$的元素仍为至多可数，且 $\sigma(A_1) = E$。令

 
$$
\begin{aligned}&\Omega_{1}=\{\omega\mid\widetilde{Q}(\omega,E)=1,\widetilde{Q}(\omega,A)\geq0,\forall A\in\mathcal{A}_{1}\}\\&\Omega_{2}=\{\omega\mid\widetilde{Q}(\omega,\cdot) 在 \mathcal{A}_{1} 上有限可加 \},\\&\Omega_{3}=\{\omega\mid\forall i\geq1,\sup_{k}\widetilde{Q}(\omega,C_{ik})=\widetilde{Q}(\omega,A_{i})\},\\ \end{aligned}
$$
 

则$\Omega_1, \Omega_2$及$\Omega_3$都为$\mathcal{G}$可测集，且$\mathbb{P}(\Omega_1) = \mathbb{P}(\Omega_2) = \mathbb{P}(\Omega_3) = 1$。由于$\mathcal{D}$是紧集类，故由引理4.5.3知，对$\omega \in \Omega_1 \cap \Omega_2 \cap \Omega_3 \hat{=} \Omega_0, \widetilde{Q}(\omega, \cdot)$限于$\mathcal{A}$为$\sigma$可加的，从而可以唯一地扩张成为$\mathcal{E}$上的一概率测度，我们用$Q(\omega, \cdot)$表示之。对$\omega \in \Omega \setminus \Omega_0$，我们令$Q(\omega, \cdot) = \mu$，

---

则 $\{Q(\omega,\cdot),\omega\in\Omega\}$为 $(E,\mathcal{E})$上的一族概率测度。下面证明它为 $\xi$关于 $\mathcal{G}$的混合条件分布。令

 
$$
\begin{aligned}\mathcal{H}=\Big\{A\in\mathcal{E}\mid Q(\cdot,A) 为 \mathcal{G} 可测 , 且 \forall B\in\mathcal{G} 有 \\\int_{B}Q(\omega,A)\mathbb{P}(d\omega)=\mathbb{P}(B\cap\xi^{-1}(A))\Big\}.\end{aligned}
$$
 

依 $Q(\omega, A)$的定义，显然有 $\mathcal{A} \subset \mathcal{H}$。此外，易见 $\mathcal{H}$为单调类，故 $\mathcal{H} = \mathcal{E}$（因 $\sigma(\mathcal{A}) = \mathcal{E}$）。这表明 $\{Q(\omega, \cdot), \omega \in \Omega\}$为 $\xi$关于 $\mathcal{G}$的混合条件分布。

下一定理是定理7.3.5的直接推论(见注7.3.4)，它给出了正则条件概率存在的一个充分条件.

定理7.3.6 设 $(\Omega,\mathcal{F})$为一可分可测空间， $\mathit{IP}$为 $\mathcal{F}$上的一紧概率测度，则对 $\mathcal{F}$的任一子 $\sigma$代数 $\mathcal{G}$，存在 $\mathit{IP}$关于 $\mathcal{G}$的正则条件概率.

下面两个定理是定理7.3.5及7.3.6的直接推论.

定理7.3.7 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $(E,\mathcal{E})$为一Radon可测空间．则对任何取值于 $(E,\mathcal{E})$的随机元 $\xi$及 $\mathcal{F}$的任一子 $\sigma$代数 $\mathcal{G}$，存在 $\xi$关于 $\mathcal{G}$的混合条件分布．

定理7.3.8 设 $(\Omega,\mathcal{F})$为一Radon可测空间，IP为F上的一概率测度，则对F的任一子 $\sigma$代数 $\mathcal{G}$，存在IP关于 $\mathcal{G}$的正则条件概率.

对可分可测空间情形, 下一定理进一步给出了正则条件概率存在的一个充要条件(见马志明(1985)).

定理7.3.9 设 $(\Omega, \mathcal{F})$为一可分可测空间， $f$为 $(\Omega, \mathcal{F})$上的一实值可测映射，使得 $f$在不同原子上取不同值，且使 $f^{-1}(\mathcal{B}(f(\Omega))) = \mathcal{F}$。令 $IP$为 $(\Omega, \mathcal{F})$上的概率测度， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数， $\{Q(\omega, \cdot), \omega \in \Omega\}$为 $f$关于 $\mathcal{G}$混合条件分布。则为要 $IP$关于 $\mathcal{G}$的正则条件概率存在，必须且只需存在 $\mathcal{G}$可测的概率为1的集合 $\Omega_0$，使得对每个 $\omega \in \Omega_0$， $Q^*(\omega, f(\Omega)) = 1$。这里 $Q^*(\omega, \cdot)$表示 $Q(\omega, \cdot)$的外测度。

证 充分性. 设定理中所给条件满足. 对  $A \in \mathcal{F}$, 令

 
$$
P(\omega,A)=\left\{\begin{aligned}{}&{{}Q^{*}(\omega,f(A)),}&{\quad\omega\in\Omega_{0},}\\ {}&{{}P(A),}&{\quad\omega\notin\Omega_{0},}\\ \end{aligned}\right.
$$
 

往证$\{P(\omega, \cdot), \omega \in \Omega\}$为$IP$关于$\mathcal{G}$的正则条件概率。首先，对$\omega \in \Omega_0$，由于$Q^*(\omega, f(\Omega)) = 1$，故由习题1.4.1知，$Q^*(\omega, \cdot)$限于$f(\Omega) \cap \mathcal{B}(R) = \mathcal{B}(f(\Omega))$为一概率测度，从而$P(\omega, \cdot)$为$\mathcal{F}$上的概率测度（由于依假定，$A \cap B = \varnothing \Rightarrow f(A) \cap f(B) = \varnothing$）。此外，对任何$A \in \mathcal{F}$，存在$B \in \mathcal{B}(R)$，使$f(A) = f(\Omega) \cap B$，故有

 
$$
P(\omega,A)=Q^{*}(\omega,f(A))=Q^{*}(\omega,f(\Omega)\cap B)=Q(\omega,B),\quad\omega\in\Omega_{0}.
$$
 

因此, $P(\cdot,A)$为 $\mathcal{G}$可测的,并且有

 
$$
P(\omega,A)=Q(\omega,B)=\mathbb{P}[f^{-1}(B)|\mathcal{G}]=\mathbb{P}[A|\mathcal{G}],\quad\mathrm{a.s.}.
$$
 

---

这表明 $\{P(\omega,\cdot),\omega\in\Omega\}$为 $\mathbb{P}$关于 $\mathcal{G}$的正则条件概率.

必要性. 设存在 $P$关于 $\mathcal{G}$的正则条件概率 $\{P(\omega,\cdot),\omega\in\Omega\}$. 令

 
$$
\widetilde{Q}(\omega,A)=P(\omega,f^{-1}(A)),A\in\mathcal{B}(f(\Omega)),
$$
 

则易见$\{\widetilde{Q}(\omega,\cdot),\omega\in\Omega\}$为$f$关于$G$的混合条件分布。对任何满足$G\supset f(\Omega)$的$G\in\mathcal{B}(R)$，我们有$f^{-1}(G)=\Omega$，从而$\widetilde{Q}(\omega,G)=1$。因此，对一切$\omega\in\Omega,\widetilde{Q}^{*}(\omega,f(\Omega))=1$。设$A=\{A_{1},A_{2},\cdots\}$为生成$F$的可数代数，令

 
$$
\Omega_{0}=\{\omega\mid Q(\omega,A_{n})=\widetilde{Q}(\omega,A_{n}),\forall n\geqslant1\},
$$
 

则$\Omega_0$为$\mathcal{G}$可测集，且$IP(\Omega_0) = 1$。此外，对$\omega \in \Omega_0, Q(\omega, \cdot)$与$\widetilde{Q}(\omega, \cdot)$限于$\mathcal{A}$一致，从而在$\mathcal{F}$上一致。特别，对$\omega \in \Omega_0$有$Q^*(\omega, f(\Omega)) = 1$。

下一结果称为测度的分拆(desintegration of measures)，它部分地推广了定理7.2.15.

定理7.3.10 设(Ω, F, P)为一概率空间, G 为F的一子σ代数; (S, S)和(E, E)为可测空间, X 为G可测S值随机元, Y 为一E值随机元. 假定Y关于G的混合条件分布Q(ω, ·)存在(例如, 若(E, E)为Radon空间, 则该条件成立). 令g(x, y)为S × E上的S × E可测函数, 使得E[|g(X, Y)|] < ∞, 则对几乎所有ω ∈ Ω, g(X(ω), ·)关于概率测度Q(ω, ·)可积, 且有

$$
\mathbb{E}[g(X,Y)|\mathcal{G}]=\int_{E}g(X,y)Q(\cdot,d y),\mathrm{~a.s.}.   \tag*{(7.3.6)}
$$

证 不妨假定 $g(x,y)$为非负 $S\times\varepsilon$可测函数.令

 
$$
G(x,\omega)=\int_{E}g(x,y)Q(\omega,d y),\ x\in S.
$$
 

则 $G(x,\omega)$为 $S\times\mathcal{G}$可测，并且对一切 $x\in E$有

 
$$
G(x,\cdot)=\mathbb{E}[g(x,Y)|\mathcal{G}],\quad\mathrm{a.s.}.
$$
 

在空间 $(S \times E, S \times \mathcal{E})$上用函数形式的单调类定理容易证明:对任意非负 $\mathcal{G}$可测随机变量Z，有

 
$$
\mathbb{E}[g(X,Y)Z]=\mathbb{E}[G(X,\cdot)Z].
$$
 

于是有

 
$$
\begin{array}{r}{\mathbb{E}[g(X,Y)|\mathcal{G}]=G(X,\cdot)=\int_{E}g(X,y)Q(\cdot,d y),\mathrm{~a.s.~}.}\end{array}
$$
 

##### 习题

### 7.3.1 补足定理7.3.12的证明.

---

## 7.4 随机变量族的一致可积性

定义7.4.1 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{H}$为一族可积随机变量。称 $\mathcal{H}$为一致可积族，如果当 $C\to\infty$时，积分

 
$$
\int_{[\mid\xi\mid\geqslant C]}\mid\xi\mid d\mathbb{P},\quad\xi\in\mathcal{H}
$$
 

一致趋于零.

下一定理给出了一个一致可积性准则.

定理7.4.2 令 $\mathcal{H} \subset L^1(\Omega, \mathcal{F}, \mathbb{P})$，则为要 $\mathcal{H}$为一致可积族，必须且只需下列条件成立：

(1)  $a = \sup\{E|\xi|, \xi \in \mathcal{H}\} < +\infty$;

(2) 对任给  $\varepsilon > 0$，存在  $\delta > 0$，使得对任何满足  $\mathbb{P}(A) \leqslant \delta$ 的  $A \in \mathcal{F}$，有

$$
\sup_{\xi\in\mathcal{H}}\int_{A}|\xi|d\boldsymbol{I}\boldsymbol{P}\leqslant\varepsilon.   \tag*{(7.4.1)}
$$

证 必要性. 设H为一致可积族. 对给定 $\varepsilon>0$, 取C足够大, 使得

 
$$
\sup_{\xi\in\mathcal{H}}\int_{[\mid\xi\mid\geqslant C]}\mid\xi\mid d\mathbb{P}\leqslant\frac{\varepsilon}{2}.
$$
 

另一方面，我们有

$$
\int_{A}|\xi|d\mathbb{P}\leqslant C\mathbb{P}(A)+\int_{[\mid\xi\mid\geqslant C]}\mid\xi\mid d\mathbb{P}.   \tag*{(7.4.2)}
$$

在(7.4.2)式中令 $A=\Omega$得到条件(1);令 $\delta=\varepsilon/2C$得到条件(2).

充分性. 设条件(1)及(2)成立. 对任给  $\varepsilon > 0$, 选取  $\delta > 0$ 使条件(2)中结论成立. 令  $C \geqslant a/\delta$, 则

 
$$
\mathbb{P}([|\xi|\geqslant C])\leqslant\frac{1}{C}\mathbb{E}[|\xi|]\leqslant\frac{a}{C}\leqslant\delta,\quad\xi\in\mathcal{H},
$$
 

故由条件(2)知

 
$$
\int_{[\mid\xi\mid\geqslant C]}\mid\xi\mid d\mathbb{P}\leqslant\varepsilon,\quad\xi\in\mathcal{H}.
$$
 

这表明H是一致可积族.

定理7.4.3 设H是一致可积族，则H在 $L^{1}(\Omega,\mathcal{F},\mathbb{P})$中的闭凸包也是一致可积的.

证 由定理7.4.2易知一致可积族在 $L^{1}$中的闭包是一致可积的，因此只需证H的凸包 $H_{1}$是一致可积的．显然 $H_{1}$满足定理7.4.2的条件(1)．往证 $H_{1}$满足条件(2)．对

---

给定  $\varepsilon > 0$，选取  $\delta > 0$，使条件(2)中的结论对  $\mathcal{H}$ 成立。则对任何  $n \geqslant 2$， $\xi_1$， $\xi_2$， $\cdots$， $\xi_n \in \mathcal{H}$ 及满足  $\sum_{i=1}^{n} \alpha_i = 1$ 的非负实数  $\alpha_1, \alpha_2, \cdots, \alpha_n$ 和对任何满足  $\mathbb{P}(A) \leqslant \delta$ 的  $A \in \mathcal{F}$，有

 
$$
\int_{A}\big|\sum_{i=1}^{n}\alpha_{i}\xi_{i}\big|d\boldsymbol{I}\boldsymbol{P}\leqslant\sum_{i=1}^{n}\alpha_{i}\int_{A}\big|\xi_{i}\big|d\boldsymbol{I}\boldsymbol{P}\leqslant\varepsilon.
$$
 

这表明 $H_{1}$满足条件(2)，故 $H_{1}$为一致可积族.

下一定理给出了 $L^{1}$收敛准则.

定理7.4.4 设 $(\xi_{n})$为一可积随机变量序列， $\xi$为一实值随机变量. 则下列条件等价：

(1)  $\xi_n \xrightarrow{L^1} \xi;$

(2)  $\xi_{n} \xrightarrow{\mathrm{p}} \xi$，且 $(\xi_{n})$为一致可积；

(3)  $\xi_n \xrightarrow{\mathrm{p}} \xi$，且  $|E| \xi_n| \to |E| \xi| < \infty$.

证 (1) $\Leftrightarrow$(3)见定理3.2.9. 只需证(1) $\Leftrightarrow$(2).

(1) $\Rightarrow(2)$. 设 $\xi_{n}\xrightarrow{L^{1}}\xi$. 令 $A\in\mathcal{F}$, 我们有

$$
\int_{A}|\xi_{n}|d\mathbb{P}\leqslant\int_{A}|\xi|d\mathbb{P}+\mathbb{E}[\left|\xi_{n}-\xi\right|].   \tag*{(7.4.3)}
$$

给定$\varepsilon > 0$, 取一正数$N$, 使得当$n > N$时, 有$E[|\xi_n - \xi|] \leq \varepsilon/2$. 再选取$\delta > 0$, 使得对任何满足$P(A) \leq \delta$的$A \in \mathcal{F}$, 有

$$
\int_{A}|\xi|d\boldsymbol{P}\leqslant\frac{\varepsilon}{2},\quad\int_{A}|\xi_{n}|d\boldsymbol{P}\leqslant\frac{\varepsilon}{2},\quad n=1,2,\cdots,N.   \tag*{(7.4.4)}
$$

于是由(7.4.3)式及(7.4.4)式知，对任何满足 $P(A) \leq \delta$的 $A \in \mathcal{F}$，有 $\sup_n \int_A |\xi_n| dP \leq \varepsilon$。此外有 $\sup_n E[|\xi_n|] < \infty$。故由定理7.4.2知， $(\xi_n)$为一致可积族。最后，显然有 $\xi_n \xrightarrow{\mathrm{p}} \xi$。

(2)⇒(1). 设 $\left(\xi_{n}\right)$一致可积，且 $\xi_{n}\xrightarrow{\mathrm{p}}\xi$. 由Fatou引理， $\mathbb{E}\left[\left|\xi\right|\right]\leq\sup_{n}\mathbb{E}\left[\left|\xi_{n}\right|\right]<+\infty$，故 $\xi$可积. 从而 $\left(\xi_{n}-\xi\right)$为一致可积. 对任给 $\varepsilon>0$，由定理7.4.2知，存在 $\delta>0$，使得对任何满足 $\mathbb{P}(A)<\delta$的 $A\in\mathcal{F}$，有

 
$$
\sup_{n}\int_{A}|\xi_{n}-\xi|d\mathbb{P}\leqslant\varepsilon.
$$
 

取N充分大，使得当 $n \geq N$时，有 $IP([|\xi_n - \xi| \geq \varepsilon]) < \delta$。于是当 $n \geq N$时，我们有

 
$$
\begin{align*}\mathbb{E}[\left|\xi_{n}-\xi\right|]=\int_{\left[\left|\xi_{n}-\xi\right|<\varepsilon\right]}\left|\xi_{n}-\xi\right|dIP+\int_{\left[\left|\xi_{n}-\xi\right|\geqslant\varepsilon\right]}\left|\xi_{n}-\xi\right|dIP\leqslant2\varepsilon,\end{align*}
$$
 

这表明 $\xi_{n}\xrightarrow{L^{1}}\xi.$

---

下一定理给出了一致可积性的又一准则.

定理7.4.5 设 $\mathcal{H} \subset L^1(\Omega, \mathcal{F}, \mathbb{P})$，则下列条件等价：

(1) H是一致可积的;

(2) 存在  $\mathbb{R}_{+}$ 上满足  $\lim_{t\to\infty}\frac{\varphi(t)}{t}=\infty$ 的非负 Borel 函数  $\varphi$，使得

 
$$
\operatorname*{s u p}_{\xi\in\mathcal{H}}\mathbb{E}[\varphi\circ|\xi|]<\infty.
$$
 

证  $(1)\Rightarrow(2)$. 设H为一致可积族. 由于对任何a>0, 有

 
$$
\int_{\Omega}(|\xi|-a)^{+}d\mathbb{P}\leqslant\int_{[\mid\xi\mid>a]}\mid\xi\mid d\mathbb{P},
$$
 

故存在自然数 $n_{k}\uparrow\infty$，使得

 
$$
\sup_{\xi\in\mathcal{H}}\int_{\Omega}(|\xi|-n_{k})^{+}d\mathbb{P}<2^{-k},\ k\geqslant1.
$$
 

令

 
$$
\varphi(t)=\sum_{k\geqslant1}(n-n_{k})^{+},\ n\leqslant t<n+1,\ n=0,1,2,\cdots
$$
 

则 $\varphi$非负，单调非降且右连续.此外有

 
$$
\lim_{n\to\infty}\frac{\varphi(n)}{n}=\lim_{n\to\infty}\sum_{k\geq1}(1-\frac{n_{k}}{n})^{+}=\infty,
$$
 

从而  $\lim_{t\to\infty}\frac{\varphi(t)}{t}=\infty.$ 最后

 
$$
\begin{align*}\mathbb{E}[\varphi\circ|\xi|]&=\sum_{n=0}^{\infty}\sum_{k=1}^{\infty}(n-n_{k})^{+}\mathbb{P}([n\leqslant|\xi|<n+1])\\&=\sum_{k=1}^{\infty}\sum_{n=0}^{\infty}(n-n_{k})^{+}\mathbb{P}([n\leqslant|\xi|<n+1])\\&=\sum_{k=1}^{\infty}\int_{\Omega}(|\xi|-n_{k})^{+}d\mathbb{P}<1.\end{align*}
$$
 

 $(1)\Rightarrow(2)$得证.

(2)⇒(1). 设(2)成立. 对给定ε > 0, 令  $a = M/\varepsilon$, 其中  $M = \sup_{\xi \in \mathcal{H}} E[\varphi \circ |\xi|]$. 选取充分大的 C, 使得当  $t \geq C$ 时, 有  $\varphi(t)/t \geq a$. 则在  $[|\xi| \geq C]$ 上, 我们有  $|\xi| \leq \varphi \circ |\xi|/a$, 故有

 
$$
\int_{[\mid\xi\mid\geqslant C]}\mid\xi\mid d\boldsymbol{P}\leqslant\frac{1}{a}\int_{[\mid\xi\mid\geqslant C]}\varphi\circ\mid\xi\mid d\boldsymbol{P}\leqslant\frac{M}{a}=\varepsilon,\quad\xi\in\mathcal{H}.
$$
 

---

因此H为一致可积族.

系7.4.6 设 $p > 1$,  $\mathcal{H} \subset L^p(\Omega, \mathcal{F}, \mathbb{P})$. 若 $\sup \mathbb{E}[|\xi|^p] < \infty$, 则 $\mathcal{H}$为一致可积族.

证 令  $\varphi(t) = t^{p}, t \geqslant 0$。由定理7.4.5立得系的结论。另一直接证明如下：令  $a = \sup_{\xi \in \mathcal{H}} |E[|\xi|^{p}]$，则  $\forall C > 0$，有

 
$$
\xi\in\bar{\mathcal{H}}
$$
 

 
$$
\int_{[\mid\xi\mid>C]}\mid\xi\mid d\boldsymbol{P}\leqslant\int_{[\mid\xi\mid>C]}\frac{\mid\xi\mid^{p}}{C^{p-1}}d\boldsymbol{P}\leqslant\frac{1}{C^{p-1}}\boldsymbol{I}E\left[\mid\xi\mid^{p}\right]\leqslant\frac{a}{C^{p-1}},
$$
 

故由定义知, $H$为一致可积族.

定理7.4.7 设 $(\Omega,\mathcal{F},\mathbb{P})$为概率空间， $\xi$为一可积随机变量， $(\mathcal{G}_{i})_{i\in I}$为一族 $\mathcal{F}$的子 $\sigma$代数。令 $\eta_{i}=\mathbb{E}[\xi|\mathcal{G}_{i}]$，则 $(\eta_{i},i\in I)$为一致可积族。

证 对任何C>0,我们有

 
$$
\mathbb{P}([|\eta_{i}|\geqslant C])\leqslant\frac{1}{C}\mathbb{E}[|\eta_{i}|]\leqslant\frac{1}{C}\mathbb{E}[|\xi|],\quad i\in I,
$$
 

于是有(注意 $|\eta_{i}|\geq C\in\mathcal{G}_{i}$)

 
$$
\begin{align*}\int_{[\mid\eta_{i}\mid\geqslant C]}\mid\eta_{i}\mid d\boldsymbol{P}&\leqslant\int_{[\mid\eta_{i}\mid\geqslant C]}\mid\xi\mid d\boldsymbol{P}\leqslant\delta\boldsymbol{P}([\mid\eta_{i}\mid\geqslant C])+\int_{[\mid\xi\mid\geqslant\delta]}\mid\xi\mid d\boldsymbol{P}\\&\leqslant\frac{\delta}{C}\mathbb{E}[{\mid\xi\mid}]+\int_{[\mid\xi\mid\geqslant\delta]}\mid\xi\mid d\boldsymbol{P}.\end{align*}
$$
 

对$\varepsilon > 0$, 取$\delta > 0$, 使得$\int_{[|\xi| \geqslant \delta]} |\xi| dP \leqslant \varepsilon/2$. 则当$C \geqslant (2\delta/\varepsilon)E[|\xi|]$ 时, 有$\int_{[|\eta_i| \geqslant C]} |\eta_i| dP \leqslant \varepsilon$, $i \in I$. 这表明$(\eta_i, i \in I)$为一致可积族.

下面进一步研究一致可积随机变量族的性质. 设$ \xi_{1}, \xi_{2}, \cdots $为可积随机变量. 如果对一切有界随机变量$ \eta $, 有  $\lim_{n \to \infty} E[\xi_{n} \eta] = E[\xi \eta]$, 则称  $\xi_{n}$ 在  $L^{1}$ 中弱收敛于  $\xi$ (见定义3.4.16).

引理7.4.8 设 $(\xi_n)$为 $(\Omega, \mathcal{F}, \mathbb{P})$上一可积随机变量序列，则为要 $\xi_n$在 $L^1$中弱收敛于某可积随机变量 $\xi$，必须且只需对每个 $A \in \mathcal{F}$， $\mathbb{E}[\xi_n I_A]$的极限存在且有穷。

证 必要性显然，往证充分性。设引理的条件成立。令  $\mu_n$ 为  $\xi_n$ 关于  $\mathbb{P}$ 的不定积分，由 Vitali-Hahn-Saks 定理 (3.3.15)， $\sup_{n} \|\mu_n\| = \sup_{n} \mathbb{E}[|\xi_n|] < \infty$。此外，存在  $\mathcal{F}$ 上一有限测度  $\mu$，使对一切  $A \in \mathcal{F}$，有  $\mu(A) = \lim_{n \to \infty} \mu_n(A)$，且有  $\mu \ll \mathbb{P}$。令  $\xi = \frac{d\mu}{d\mathbb{P}}$。则易见  $\xi_n$ 弱收敛于  $\xi$。(这里用到习题 2.1.3 及  $\sup \mathbb{E}[|\xi_n|] < \infty$ 这一事实。)

下一定理是著名的Dunford-Pettis 弱紧性准则的一个部分(对概率论最有用的部分).

定理7.4.9 设 $\mathcal{H} \subset L^1(\Omega, \mathcal{F}, \mathbb{P})$，则下列条件等价：

(1) H 为一致可积族;

---

(2) 对 H 中的任一序列  $(\xi_{n})$，存在其子列  $(\xi_{n_{k}})$，使之在  $L^{1}$ 中弱收敛.

证 (1)  $\Rightarrow$ (2). 设H为一致可积族. 令 $(\xi_{n})$ 为H中的一序列,  $G = \sigma(\xi_{1}, \xi_{2}, \cdots)$, 则G为一可分的σ代数, 故存在一可数代数 $A = \{A_{1}, A_{2}, \cdots\}$, 使 $\sigma(A) = G$. 由对角线法则, 可选 $(\xi_{n})$ 的子列 $(\xi_{n_{k}})$ 使得对一切 $j \geq 1$, 极限 $\lim_{k \to \infty} \mathbb{E}[\xi_{n_{k}} I_{A_{j}}]$ 存在且有穷. 令

 
$$
\mathcal{H}=\{A\in\mathcal{G}\mid\lim_{k\to\infty}\mathbb{E}[\xi_{n_{k}}I_{A}] 存在且有穷 \}.
$$
 

利用$(\xi_{n_k})$的一致可积性(见定理7.4.2)不难看出$\mathcal{H}$为一单调类。由于$\mathcal{A}\subset\mathcal{H}$，故由单调类定理知$\mathcal{H}=\mathcal{G}$。于是由引理7.4.8知，$(\xi_{n_k})$在$L^1(\Omega,\mathbb{F},\mathbb{P})$中弱收敛。因此，对一切有界$\mathcal{G}$可测随机变量$\eta$，极限$\lim_{k\to\infty}\mathbb{E}[\xi_{n_k}\eta]$存在且有穷。现设$A\in\mathcal{F}$，令$\eta=\mathbb{E}[I_A|\mathcal{G}]$，则有$E[\xi_{n_k}I_A]=E[E[\xi_{n_k}I_A|\mathcal{G}]]=E[\xi_{n_k}\eta]$，从而极限$\lim_{k\to\infty}\mathbb{E}[\xi_{n_k}I_A]$存在且有穷。再由引理7.4.8知，$(\xi_{n_k})$在$L^1(\Omega,\mathbb{F},\mathbb{P})$中弱收敛。

(2)⇒(1). 我们用反证法. 假定(1)不成立, 则存在H中一序列( $\xi_{n}$), 使得: 或者  $\lim_{n\to\infty}E\left[\left|\xi_{n}\right|\right]=\infty$; 或者存在某  $\varepsilon>0$ 和 F 中的一列集合  $(A_{n},n\geq1)$, 使得

 
$$
\lim_{n\to\infty}\mathbb{P}(A_{n})=0,\ \inf_{n}\int_{A_{n}}\left|\xi_{n}\right|\geqslant\varepsilon.
$$
 

由Vitali-Hahn-Saks定理(定理3.3.15)知, 该序列不可能有弱收敛子列.

##### 习题

7.4.1 设 $(\xi_{n})$ 为一致可积随机变量序列，则有

 
$$
\lim_{n\to\infty}\mathbb{E}[\frac{1}{n}\sup_{1\leqslant k\leqslant n}\left|\xi_{k}\right|]=0.
$$
 

7.4.2 设  $\mathcal{H} \subset L^1(\Omega, \mathcal{F}, \mathbb{P})$，若  $\mathcal{H}$ 满足如下条件：

 
$$
A_{n}\in\mathcal{F},\;A_{n}\downarrow\phi\Rightarrow\lim_{n\rightarrow\infty}\sup_{\xi\in\mathcal{H}}\int_{A_{n}}|\xi|d\mathbb{P}=0,
$$
 

则对任给 $\varepsilon>0$，存在 $\delta>0$，使得

 
$$
A\in\mathcal{F},\;\mathbb{P}(A)<\delta\Rightarrow\sup_{\xi\in\mathcal{H}}\int_{A}|\xi|d\mathbb{P}\leqslant\varepsilon.
$$
 

7.4.3 设 $H_{1}$及 $H_{2}$为一致可积随机变量族. 令

 
$$
\mathcal{H}=\{\xi_{1}+\xi_{2}\mid\xi_{1}\in\mathcal{H}_{1},\xi_{2}\in\mathcal{H}_{2}\},
$$
 

则H为一致可积族.

7.4.4 设p > 0,  $(\xi_{n})$ 为  $L^{p}$ 中的序列, 且  $\xi_{n} \xrightarrow{P} \xi$. 则下列三条件等价:

(1)  $\xi_n \xrightarrow{L^p} \xi;$

(2)  $\|\xi_n\|_p \to \|\xi\|_p;$

(3) 序列 $\left(\left|\xi_{n}\right|^{p}\right)$是一致可积的.

---

## 7.5 本性上确界

定义7.5.1 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{H}$为随机变量的非空族．称随机变量 $\eta$为 $\mathcal{H}$的本性上确界，如果 $\eta$满足下列条件：

(1) 对一切  $\xi \in \mathcal{H}$，有  $\xi \leqslant \eta$，a.s.;

(2) 设  $\eta'$ 为任一随机变量，使得对一切  $\xi \in \mathcal{H}$ 有  $\xi \leqslant \eta'$，a.s.，则有  $\eta \leqslant \eta'$，a.s..

容易看出: 若H的本性上确界存在, 则必唯一(不计a.s.相等的两个随机变量的差别), 我们用ess.sup  $\xi$ 或ess.sup H表示之.

 
$$
\xi\in\mathcal{H}
$$
 

在上述(1)及(2)中将不等号反向, 就得到本性下确界的定义. H的本性下确界记为ess. $\inf_{\xi\in H}\xi$或ess. $\inf_{H}$

下一定理表明, 随机变量的非空族的本性上(下)确界总存在.

定理7.5.2 令H为随机变量的非空族. 则H的本性上(下)确界存在, 且有H中的至多可数个元素 $\xi_{n}$, 使得

 
$$
\mathrm{ess.sup}\mathcal{H}=\bigvee_{n}\xi_{n},(\mathrm{ess.inf}\mathcal{H}=\bigwedge_{n}\xi_{n}).
$$
 

若进一步，H对取有限上(下)端运算封闭(即： $\xi, \eta \in \mathcal{H} \Rightarrow \exists f \in \mathcal{H}$，使得 $f = \xi \lor \eta$ ( $f = \xi \land \eta$)，a.s.，则 $(\xi_n)$可取为一a.s.单调增(降)序列。

证 只考虑本性上确界情形.第二结论显然. 为证第一结论, 不妨设H 中的元一致有界, 否则可以考虑随机变量族 $\overline{H} = \{\operatorname{arctg}\xi \mid \xi \in \mathcal{H}\}$.此外, 显然可以进一步假定H对取有限上端运算封闭. 这时, 令 $(\xi_n) \subset \mathcal{H}$为一单调增序列, 使得

 
$$
\lim_{n\to\infty}\mathbb{E}[\xi_{n}]=\sup_{\xi\in\mathcal{H}}\mathbb{E}[\xi].
$$
 

令 $\eta = \bigvee_n \xi_n$，往证 $\eta$为 $\mathcal{H}$的本性上确界。为此只需验证定义7.5.1中的两个条件。条件(2)显然成立，故只需证条件(1)成立。设 $\xi \in \mathcal{H}$，令 $\xi_n' = \xi_n \vee \xi$，则 $(\xi_n') \subset \mathcal{H}$， $(\xi_n')$单调增，且 $\lim_{n \to \infty} \xi_n' = \eta \vee \xi$，我们有

 
$$
\mathbb{E}[\eta\vee\xi]=\lim_{n\to\infty}\mathbb{E}[\xi_{n}^{\prime}]\leqslant\sup_{\xi\in\mathcal{H}}\mathbb{E}[\xi]=\mathbb{E}[\eta].
$$
 

由于 $\eta \vee \xi \geqslant \eta$，上式表明 $\eta \vee \xi = \eta$，a.s.，此即 $\eta \geqslant \xi$，a.s.。条件(1)得证。

注7.5.3 令 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间. 设 $C\subset\mathcal{F}$，且C非空. 令

 
$$
\mathcal{H}=\{I_{C}\mid C\in\mathcal{C}\},
$$
 

则由定理知，存在 $(C_{n})\subset C$，使得

 
$$
I_{\cup_{n}C_{n}}=\forall I_{C_{n}}=\mathrm{ess.sup}\mathcal{H}.
$$
 

---

我们称 $\bigcup C_n$为 $C$的本性上确界，并用 $\text{ess.sup}$  $C$记之。类似定义 $C$的本性下确界。

下一定理称为Halmos-Savage定理.

定理7.5.4 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\mathcal{M}$为 $\mathcal{F}$上的一族关于 $\mathbb{P}$绝对连续的概率测度，且对可列凸组合封闭．如果对任一 $\mathbb{P}(A)>0$的 $A\in\mathcal{F}$，存在 $\mathcal{Q}\in\mathcal{M}$，使得 $\mathbb{Q}(A)>0$，则存在 $\mathbb{Q}_{0}\in\mathcal{M}$，使得 $\mathbb{Q}_{0}$与 $\mathbb{P}$等价．

证 令  $S = \left\{ \left| \frac{dQ}{dP} > 0 \right| \mid Q \in \mathcal{M} \right\}$. 由于 M 对可列凸组合封闭, S 对集合可列并运算 a.s. 封闭. 于是存在  $Q_0 \in \mathcal{M}$, 使得  $\left| \frac{dQ_0}{dP} > 0 \right| = \text{ess.sup} S$, 即有

 
$$
\mathbb{P}\Big(\Big[\frac{d\mathcal{Q}_{0}}{d\mathbb{P}}>0\Big]\Big)=\sup\Big\{\mathbb{P}(S)\mid S\in\mathcal{S}\Big\}.
$$
 

往证$\mathbb{Q}_0$与$\mathbb{P}$等价．令$S_0 = \left[\frac{dQ_0}{d\mathbb{P}} > 0\right]$，只需证$P(S_0) = 1$．如果$P(S_0) < 1$，则依假定，存在$\mathbb{Q}_1 \in \mathcal{M}$，使得$Q_1(\Omega \setminus S_0) > 0$．于是若令$Q = \frac{Q_0 + Q_1}{2}$，则$Q \in \mathcal{M}$，且$P\left(\left[\frac{dQ_0}{d\mathbb{P}} > 0\right]\right) > \mathbb{P}\left(\left[\frac{dQ_0}{d\mathbb{P}} > 0\right]\right)$，这导致矛盾．

下一定理(归于严加安(1980))在鞅论及金融数学中有重要应用.

定理7.5.5 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $K$为 $L^1$中的一凸集，且 $0\in K$。则下列三个条件等价：

(1) 对任一  $\eta \in (L^{1})^{+} \setminus \{0\}$，存在  $c > 0$，使  $c \eta \notin \overline{K - (L^{\infty})^{+}}$；

(2) 对任一非不足道  $A \in \mathcal{F}$，存在 c > 0，使  $cI_A \notin \overline{K - (L^\infty)^+}$；

(3) 存在  $\zeta \in L^\infty$ 使得  $\zeta > 0$，a.s.，且  $\sup_{\xi \in K} \mathbb{E}[\zeta \xi] < \infty$。这里  $\overline{B}$ 表示  $B$ 在  $L^1$ 中的闭包。

证 (1)  $\Rightarrow$ (2) 显然. 往证 (2)  $\Rightarrow$ (3). 令  $A \in \mathcal{F}$ 且  $P(A) > 0$. 由假设, 存在 c > 0 使  $c I_{A} \notin \overline{K - (L^{\infty})^{+}}$. 由于  $K - (L^{\infty})^{+}$ 是  $L^{1}$ 中的凸集,  $L^{\infty}$ 是  $L^{1}$ 的对偶空间, 由泛函分析中的 Hahn-Banach 定理知, 存在  $\theta \in L^{\infty}$ 使

$$
\sup_{\xi\in K,\eta\in(L^{\infty})^{+}}\mathbb{E}[\theta(\xi-\eta)]<c\mathbb{E}[\theta I_{A}].   \tag*{(7.5.1)}
$$

在7.5.1式中取 $\xi=0,\eta=a\theta^{-}$，及a>0得到

$$
a\mathbb{I}E[(\theta^{-})^{2}]<c\mathbb{I}E[\theta I_{A}].   \tag*{(7.5.2)}
$$

由于(7.5.2)式对一切a > 0成立, 必有 $\theta^{-} = 0$, a.s., 即 $\theta \in (L^{\infty})^{+}$. 此外, 显然有 $P(\theta > 0) > 0$. 若以 $\frac{\theta}{E[\theta]}$代替 $\theta$, 可假定 $E[\theta] = 1$. 于是由(7.5.1)式得 $\sup_{\xi \in K} E[\theta \xi] < c$. 令

 
$$
H=\{\theta\in(L^{\infty})^{+}\mid\mathbb{E}[\theta]=1,\sup_{\xi\in K}\mathbb{E}[\theta\xi]<\infty\}.
$$
 

我们已证H非空. 令 $C = \{[\theta = 0] \mid \theta \in H\}$. 往证C对可列交封闭. 设 $(\theta_n) \subset H$, 令

 
$$
c_{n}=\operatorname*{s u p}_{\xi\in K}\mathbb{E}[\theta_{n}\xi],\quad d_{n}=\|\theta_{n}\|_{L^{\infty}}.
$$
 

---

取严格正实数列 $(b_{n})$，满足

 
$$
\sum_{n}b_{n}=1,\quad\sum_{n}c_{n}b_{n}<\infty,\quad\sum_{n}b_{n}d_{n}<\infty.
$$
 

设 $\theta = \sum_n b_n \theta_n$。显然 $\theta \in H$且 $[\theta = 0] = \bigcap_n [\theta_n = 0]$。这表明 $C$对可列交封闭。于是存在 $\zeta \in H$，使

$$
\mathbb{P}([\zeta=0])=\inf_{\theta\in H}\mathbb{P}([\theta=0]).   \tag*{(7.5.3)}
$$

往证  $\zeta > 0$, a.s.. 假定  $\mathbb{P}([\zeta = 0]) > 0$. 令  $A = [\zeta = 0]$, 由上所证, 存在  $\theta \in H$ 使 (7.5.1) 式成立. 特别有  $\mathbb{E}[\theta I_{[\zeta=0]}] > 0$. 这蕴含  $\mathbb{P}([\theta > 0] \cap [\zeta = 0]) > 0$. 从而有

 
$$
\mathbb{P}([\theta=0]\cap[\zeta=0])<\mathbb{P}([\zeta=0]).
$$
 

但 $[\theta=0]\cap[\zeta=0]\in\mathcal{C}$，这与7.5.3式矛盾. $(2)\Rightarrow(3)$得证.

(3)  $\Rightarrow$ (1). 设(1)不成立. 则存在  $\eta \in (L^{1})^{+} \setminus \{0\}$ 使对所有  $c > 0$ 都有  $c\eta \in \overline{K - (L^{\infty})^{+}}$. 对每个  $n$ 存在  $\xi_{n} \in K, \eta_{n} \in (L^{\infty})^{+}$ 及  $\delta_{n} \in L^{1}$ 使  $n\eta = \xi_{n} - \eta_{n} - \delta_{n}$, 且  $\|\delta_{n}\|_{L^{1}} < \frac{1}{n}$. 我们有  $\xi_{n} \geq n\eta + \delta_{n}$, 且对任一严格正的随机变量  $\zeta$, 有

 
$$
\sup_{\xi\in K}\mathbb{E}[\zeta\xi]\geqslant\sup_{n}\mathbb{E}[\zeta\xi_{n}]=+\infty,
$$
 

这表明(3)不成立. $(3)\Rightarrow(1)$得证.

系7.5.6 设K是 $L^1$中一凸集. 若对K中的任一点列 $(\xi_n)$，有 $(1/n)\xi_n^+ \xrightarrow{P} 0$（或者等价地， $\forall \varepsilon > 0$，存在 $c > 0$使 $\forall \xi \in K$， $\mathbb{P}(\xi > c) < \varepsilon.$），则存在 $\zeta \in L^\infty$，使 $\zeta > 0$，a.s.，且 $\sup_{\xi \in K} \mathbb{E}[\zeta \xi] < \infty$.

证 只需证明定理7.5.5的条件(1)成立. 不妨设 $0 \in K$，否则任取 $\eta \in K$，以 $\{x - \eta | x \in K\}$代替K. 从定理7.5.4 (3)  $\Rightarrow$ (1) 的证明看出，若(1)不成立，则存在 $\eta \in (L^1)^+\setminus \{0\}$， $(\xi_n) \subset K$ 及 $(\delta_n) \subset L^1$，使得对每个n，有 $\|\delta_n\|_{L^1} \leqslant 1/n$ 及 $\xi_n/n \geqslant \eta + \delta_n/n$. 这与 $(1/n)\xi_n^+ \xrightarrow{p} 0$矛盾.

下一定理(归于严加安(1985))给出了本性下确界与条件期望可交换的一个充要条件.

定理7.5.7 设 $\mathcal{H} \subset L^1$满足 $\inf\{\mathbb{E}[\xi] \mid \xi \in \mathcal{H}\} > -\infty$，则下列条件等价：

(1) 对任意的  $\eta_1, \eta_2 \in \mathcal{H}$ 及  $\varepsilon > 0$，存在  $\eta_3 \in \mathcal{H}$，使得

 
$$
\begin{array}{r}{\mathbb{E}[(\eta_{3}-\eta_{1}\wedge\eta_{2})^{+}]<\varepsilon;}\end{array}
$$
 

(2)  $E[\text{ess.inf } \mathcal{H}] = \inf\{\mathbb{E}[\xi] \mid \xi \in \mathcal{H}\};$

(3) ess.inf H可积, 且对每个F的子σ代数G, 有

$$
\mathbb{I}E[\mathrm{e s s.i n f}\mathcal{H}|\mathcal{G}]=\mathrm{e s s.i n f}\left\{\mathbb{I}E[\xi|\mathcal{G}]\mid\xi\in\mathcal{H}\right\}.   \tag*{(7.5.4)}
$$


---

证 (1)  $\Rightarrow$ (2). 设(1)成立. 取 $(\xi_n) \subset \mathcal{H}$, 使  $\lim_{n \to \infty} \mathbb{E}[\xi_n] = \inf_{\xi \in \mathcal{H}} \mathbb{E}[\xi] \hat{=} h$. 对给定  $\varepsilon > 0$, 令  $\eta_1 = \xi_1$, 并归纳选取  $\eta_n \in \mathcal{H}$, 使

 
$$
\begin{array}{r}{\mathbb{I}E[(\eta_{n}-\eta_{n-1}\wedge\xi_{n})^{+}]<1/2^{n-1},\quad n\geqslant2.}\end{array}
$$
 

令

 
$$
\delta_{n}=(\eta_{n}-\eta_{n-1}\wedge\xi_{n})^{+},\ n\geqslant2,\ \delta_{1}=0,
$$
 

并令

 
$$
\gamma_{n}=\sum_{k=n+1}^{\infty}\delta_{k},\quad\eta_{n}^{\prime}=\eta_{n}+\gamma_{n},\quad n\geqslant1.
$$
 

则有

 
$$
\eta_{n+1}^{\prime}=\eta_{n+1}+\gamma_{n+1}\leqslant(\eta_{n}+\delta_{n+1})+\gamma_{n+1}=\eta_{n}^{\prime},\ n\geqslant1.
$$
 

于是 $\eta_{n}^{\prime}$单调下降趋于一极限 $\eta^{\prime}$. 由于

 
$$
h\leqslant\mathbb{E}[\eta_{n}]\leqslant\mathbb{E}[\xi_{n}]+\mathbb{E}[\delta_{n}],\ \mathbb{E}[\eta_{n}^{\prime}]=\mathbb{E}[\eta_{n}]+\mathbb{E}[\gamma_{n}],
$$
 

且  $\lim_{n\to\infty}E[\delta_{n}]=\lim_{n\to\infty}E[\gamma_{n}]=0$，我们有

 
$$
\mathbb{E}[\eta^{\prime}]=\lim_{n\to\infty}\mathbb{E}[\eta_{n}^{\prime}]=\lim_{n\to\infty}\mathbb{E}[\xi_{n}]=h.
$$
 

现令 $\xi^{*}=\Lambda_{n=1}^{\infty}\xi_{n}$，往证 $E[\xi^{*}]=h$及 $\xi^{*}=\mathrm{ess.inf}$H，由此推得(2). 我们有(注意 $\delta_{1}=0$)

 
$$
\eta_{n}^{\prime}=\eta_{n}+\gamma_{n}\leqslant\xi_{n}+\delta_{n}+\gamma_{n}\leqslant\xi_{n}+\gamma_{1},\ n\geqslant1,
$$
 

从而

 
$$
\eta^{\prime}=\bigwedge_{n}\eta_{n}^{\prime}\leqslant\bigwedge_{n}(\xi_{n}+\gamma_{1})=\xi^{*}+\gamma_{1}.
$$
 

因此有

 
$$
\mathbb{E}[\xi^{*}]\geqslant\mathbb{E}[\eta^{\prime}]-\mathbb{E}[\gamma_{1}]\geqslant h-\varepsilon.
$$
 

由于$\varepsilon > 0$是任意的，且$E[\xi^*] \leqslant \inf_n E[\xi_n] = h$，故有$E[\xi^*] = h$。另一方面，对任一$\xi_0 \in \mathcal{H}$，考虑序列$(\xi_n, n \geqslant 0)$。由已证结果得

 
$$
\mathbb{E}[\xi_{0}\wedge\xi^{*}]=\mathbb{E}[\bigwedge_{k=0}^{\infty}\xi_{k}]=h=\mathbb{E}[\xi^{*}],
$$
 

由此知 $\xi_{0}\geq\xi^{*}$，a.s..于是最终有 $\xi^{*}=\mathrm{ess.inf}$  $\mathcal{H}$.(1) $\Rightarrow$(2)得证.

(2)  $\Rightarrow$ (1). 设(2)成立. 令  $\xi^* = \text{ess.inf} \mathcal{H}$. 依假定有  $\mathbb{E}[\xi^*] = \inf_{\xi \in \mathcal{H}} \mathbb{E}[\xi] \hat{=} h$. 于是对任给  $\varepsilon > 0$, 存在  $\xi \in \mathcal{H}$ 使  $\mathbb{E}[\xi] \leqslant h + \varepsilon$, 即  $\mathbb{E}[\xi - \xi^*] \leqslant \varepsilon$, 这蕴含(1).

---

(1)  $\Rightarrow$ (3). 设(1)成立. 令  $\mathcal{H}' = \{\mathbb{E}[\xi | \mathcal{G}] | \xi \in \mathcal{H}\}$. 对任给  $\eta_1, \eta_2, \eta_3 \in \mathcal{H}$, 由 Jensen 不等式,

 
$$
\begin{align*}(\mathbb{E}[\eta_{3}|\mathcal{G}]-\mathbb{E}[\eta_{1}|\mathcal{G}]\wedge\mathbb{E}[\eta_{2}|\mathcal{G}])^{+}&\leqslant(\mathbb{E}[\eta_{3}-\eta_{1}\wedge\eta_{2}|\mathcal{G}])^{+}\\&\leqslant\mathbb{E}[(\eta_{3}-\eta_{1}\wedge\eta_{2})^{+}|\mathcal{G}],\end{align*}
$$
 

从而 $\mathcal{H}'$满足条件(1). 对任给 $A\in\mathcal{H}$，令

 
$$
\mathcal{H}_{A}=\{I_{A}\xi\mid\xi\in\mathcal{H}\},\mathcal{H}_{A}^{\prime}=\{I_{A}\xi\mid\xi\in\mathcal{H}^{\prime}\}.
$$
 

显然 $H_{A}$及 $H_{A}^{\prime}$满足(1). 因此由(1) $\Rightarrow$(2)有

 
$$
\begin{aligned}{\mathbb{E}[I_{A}\mathbf{e s s.i n f}\mathcal{H}]}&{{}=\mathbb{E}[\mathbf{e s s.i n f}\mathcal{H}_{A}]}\\ {}&{{}=\operatorname*{i n f}_{\xi\in\mathcal{H}}\mathbb{E}[\xi I_{A}]}\\ {}&{{}=\operatorname*{i n f}_{\xi\in\mathcal{H}}\mathbb{E}[\mathbb{E}[\xi|\mathcal{G}]I_{A}]}\\ {}&{{}=\operatorname*{i n f}_{\eta\in\mathcal{H}_{A}^{\prime}}\mathbb{E}[\eta]}\\ {}&{{}=\mathbb{E}[\mathbf{e s s.i n f}\mathcal{H}_{A}^{\prime}]}\\ {}&{{}=\mathbb{E}[I_{A}\mathbf{e s s.i n f}\mathcal{H}^{\prime}],}\\ \end{aligned}
$$
 

由此推得 $(7.5.4)$式.

(3)  $\Rightarrow$ (2). 在(7.5.4)式中令  $\mathcal{G} = \{\varnothing, \Omega\}$ 即得(2).

##### 习题

7.5.1 设 $(\Omega, \mathcal{F}, \mathbb{P})$为一概率空间， $\mathcal{G}$为 $\mathcal{F}$的一子 $\sigma$代数， $A \in \mathcal{F}$，则

 
$$
[\mathbb{E}[I_{A}|\mathcal{G}]>0]=\operatorname{e s s.i n f}\left\{B\in\mathcal{G}\mid B\supset A\right\},
$$
 

 
$$
[\mathbb{E}[I_{A}|\mathcal{G}]=1]=\operatorname{e s s.s u p}\left\{B\in\mathcal{G}\mid B\subset A\right\}.
$$
 

7.5.2 设 $(\xi,\xi_{n},n\geqslant1)$为一列实值随机变量，令

 
$$
\begin{aligned}&s\text{-}\limsup_{n}\xi_{n}=\text{ess.inf}\left\{\eta\mid\lim_{n}\mathbb{P}(\xi_{n}>\eta)=0\right\},\\&s\text{-}\liminf_{n}\xi_{n}=\text{ess.sup}\left\{\eta\mid\lim_{n}\mathbb{P}(\xi_{n}<\eta)=0\right\},\\ \end{aligned}
$$
 

则有

 
$$
\begin{aligned}\liminf_{n}\xi_{n}&\leqslant s-\liminf_{n}\xi_{n}\leqslant s-\limsup_{n}\xi_{n}\leqslant\limsup_{n}\xi_{n},\\\xi_{n}&\xrightarrow{P}\xi\Leftrightarrow s-\limsup_{n}\xi_{n}=s-\liminf_{n}\xi_{n}.\end{aligned}
$$
 

---

7.5.3 设定理7.5.6中的三个等价条件之一成立. 令  $K \subset H$, 使得  $\inf_{\xi \in K} E[\xi] = \inf_{\xi \in H} E[\xi]$, 则  $\mathrm{ess.inf} K = \mathrm{ess.inf} H$, 且有

 
$$
\mathbb{E}[\mathrm{e s s.i n f}\mathcal{H}|\mathcal{G}]=\mathrm{e s s.i n f}\{\mathbb{E}[\xi|\mathcal{G}]\mid\xi\in\mathcal{K}\}.
$$
 

## 7.6 平稳序列和遍历定理

定义7.6.1 设 $(\Omega,\mathcal{F},\mathbb{P})$是一概率空间，T是由 $(\Omega,\mathcal{F})$到自身的可测映射，称T是保测变换，如果 $P\circ T^{-1}=P$，即对每个 $A\in\mathcal{F}$， $P(T^{-1}(A))=P(A)$.

定理7.6.2 设 $(\Omega,\mathcal{F},\mathbb{P})$是一概率空间， $T$是一保测变换， $\xi$为一可积随机变量。则有 $E[\xi]=E[\xi(T)]$。

证 设  $A \in \mathcal{F}$，令  $\eta(\omega) = I_A(\omega)$，则  $\eta(T(\omega)) = I_A(T(\omega)) = I_{T^{-1}(A)}(\omega)$。由于 T 是保测变换，我们有  $E[\eta] = P(A) = P(T^{-1}(A)) = E[\eta(T)]$。这表明定理对简单随机变量成立，从而对可积随机变量成立。

定义7.6.3 设 $(\Omega,\mathcal{F},P)$是一概率空间，T是一保测变换。称一集合 $A\in\mathcal{F}$为T不变的，如果 $P(A\triangle T^{-1}(A))=0$。称一随机变量 $\xi$为T不变的，如果对几乎所有 $\omega\in\Omega$， $\xi(T(\omega))=\xi(\omega)$。

容易验证: T 不变集合全体构成一  $\sigma$ 代数, 称为 T 不变  $\sigma$ 代数, 记为 T. 随机变量  $\xi$ 为 T 不变的, 当且仅当它是 T 可测.

定义7.6.4 设 $(\Omega, \mathcal{F}, \mathbb{P})$是一概率空间， $T$是一保测变换。称 $T$是遍历的，如果任何 $T$不变集合具有概率测度 $0$或 $1$。称 $T$是混合的，如果对所有 $A, B \in \mathcal{F}$，

$$
\lim_{n\to\infty}\mathbb{P}(A\cap T^{-n}(B))=\mathbb{P}(A)\mathbb{P}(B).   \tag*{(7.6.1)}
$$

定理7.6.5 每个混合保测变换都是遍历的.

证 设 $B \in \mathcal{T}$. 由(7.6.1)和 $B$的 $T$不变性(即 $T^{-n}(B) = B$, a.s.),

 
$$
\mathbb{P}(B)^{2}=\lim_{n\to\infty}\mathbb{P}(B\cap T^{-n}(B))=\lim_{n\to\infty}\mathbb{P}(B\cap B)=\mathbb{P}(B),
$$
 

从而 $IP(B)=0$或1.

定义7.6.6 设 $(\Omega,\mathcal{F},\mathbb{P})$是一概率空间， $(\xi_{1},\xi_{2},\cdots)$为一随机变量序列. 称其为平稳的，如果对每个 $k\geq1,m\geq1$，

$$
\mathbb{P}((\xi_{1},\cdots,\xi_{m})\in B)=\mathbb{P}((\xi_{k+1},\cdots,\xi_{k+m})\in B),\quad B\in\mathcal{B}(\mathbb{R}^{m}).   \tag*{(7.6.2)}
$$

由单调类定理容易推知, 随机序列是平稳的, 当且仅当对每个  $k \geqslant 1$,

$$
\mathbb{P}((\xi_{1},\xi_{2},\cdots)\in B)=\mathbb{P}((\xi_{k+1},\xi_{k+2},\cdots)\in B),\quad B\in\mathcal{B}(\mathbb{R}^{\infty}).   \tag*{(7.6.3)}
$$


---

设$(\Omega, \mathcal{F}, \mathbb{P})$是一概率空间，$T$是一保测变换，$T^k$表示$T$的$k$次迭代。设$\xi_1$为一随机变量，令$\xi_n(\omega) = \xi_1(T^{n-1}(\omega))$，则对任何$k \geq 1, m \geq 1$，$\mathbb{R}^m$中的任何可测矩形$B = \prod_{i=1}^m B_i$，$(7.6.2)$成立。由单调类定理推知，对每个$B \in \mathcal{B}(\mathbb{R}^m)$，$(7.6.2)$成立。因此，由保测变换迭代产生的随机变量序列是平稳序列。

下一定理是著名的von Neumann-Birkhoff遍历定理.

定理7.6.7 设 $(\Omega,\mathcal{F},\mathbb{P})$是一概率空间，T是一保测变换， $\xi_{1}\in L^{p}(\Omega,\mathcal{F},\mathbb{P})$， $p\geqslant1$。令 $\xi_{n}(\omega)=\xi_{1}(T^{n-1}(\omega)),S_{n}=\sum_{k=1}^{n}\xi_{k}$，则当 $n\to\infty$， $S_{n}/n$ a.s.和 $L^{p}$收敛于 $E[\xi_{1}|\mathcal{T}]$，这里T是T不变 $\sigma$代数。

为了证明定理, 我们首先证明如下的Hopf最大遍历定理.

定理7.6.8 沿用定理7.6.7记号，令 $M_{n}=\max\{0,S_{1},\cdots,S_{n}\}$，则对 $n\geqslant1$，

$$
\begin{array}{r}{\varPi E[\xi_{1}I_{[M_{n}>0}]]\geqslant0.}\end{array}   \tag*{(7.6.4)}
$$

证 对  $k \leqslant n,$ 有  $M_{n}(T(\omega)) \geqslant S_{k}(T(\omega)),$ 故有  $\xi_{1}(\omega) + M_{n}(T(\omega)) \geqslant \xi_{1}(\omega) + S_{k}(T(\omega)) = S_{k+1}(\omega).$ 另一方面，恒有  $\xi_{1}(\omega) = S_{1}(\omega) \geqslant S_{1}(\omega) - M_{n}(T(\omega)),$ 从而有

 
$$
\xi_{1}(\omega)\geqslant\max\{S_{1}(\omega),\cdots,S_{n}(\omega)\}-M_{n}(T(\omega)).
$$
 

但是，恒有 $M_n(T) \geq 0$，且在集合 $[M_n > 0]$上， $\max\{S_1, \cdots, S_n\} = M_n$，故有

 
$$
\begin{align*}\mathbb{E}[\xi_{1}I_{[M_{n}>0]}&\geqslant\mathbb{E}[(M_{n}-M_{n}(T)I_{[M_{n}>0]}]\\&\geqslant\mathbb{E}[(M_{n}-M_{n}(T)]=0.\end{align*}
$$
 

(7.6.4)式得证.

证 (定理7.6.7的证明) 不妨假定  $E[\xi_{1}|\mathcal{T}] = 0$，否则用  $\xi_{1} - E[\xi_{1}|\mathcal{T}]$ 代替  $\xi_{1}$.

令  $\eta = \limsup_{n \to \infty} S_n / n$，则  $\eta$ 是 T 不变随机变量，从而对任给  $\varepsilon > 0$ 和  $k \geq 1$,  $A_{\varepsilon} = [\eta > \varepsilon]$ 是 T 不变集合. 令

 
$$
\xi_{1}^{*}(\omega)=(\xi_{1}(\omega)-\varepsilon)I_{A_{\varepsilon}}(\omega),
$$
 

对 $k\geqslant1$，相应地定义 $\xi_{k}^{*}$， $S_{k}^{*}$和 $M_{k}^{*}$，我们有

 
$$
\begin{aligned}&\xi_{k}^{*}(\omega)=(\xi_{1}(T^{k-1}(\omega))-\varepsilon)I_{A_{\varepsilon}}(T^{k-1}(\omega))=(\xi_{k}(\omega)-\varepsilon)I_{A_{\varepsilon}}(\omega).\\ &\\ &\quad S_{k}^{*}I_{A_{\varepsilon}}=(S_{k}-\varepsilon)I_{A_{\varepsilon}},M_{n}^{*}I_{A_{\varepsilon}}=(M_{n}-\varepsilon)I_{A_{\varepsilon}}.\\ \end{aligned}
$$
 

从而有

 
$$
\lim_{n\to\infty}\left[M_{n}^{*}>0\right]=\left[\sup_{k\geqslant1}S_{k}^{*}>0\right]=\left[\sup_{k\geqslant1}\frac{S_{k}^{*}}{k}>0\right]
$$
 

---

 
$$
=\left[\sup_{k\geq1}\frac{S_{k}}{k}>\varepsilon\right]\cap A_{\varepsilon}=A_{\varepsilon}.
$$
 

由定理7.6.9,  $\mathbb{E}[\xi_{1}^{*}I_{[M_{n}^{*}>0}]}\geq0$. 因此,

 
$$
\begin{align*}0&\leqslant\lim_{n\to\infty}\mathbb{E}[\xi_{1}^{*}I_{[M_{n}^{*}>0]}]=\mathbb{E}[\xi_{1}^{*}I_{A_{\varepsilon}}]=\mathbb{E}[(\xi_{1}-\varepsilon)I_{A_{\varepsilon}}]\\&=\mathbb{E}[\xi_{1}I_{A_{\varepsilon}}]-\varepsilon\mathbb{P}(A_{\varepsilon})=\mathbb{E}[\mathbb{E}[\xi_{1}|\mathcal{T}]I_{A_{\varepsilon}}]-\varepsilon\mathbb{P}(A_{\varepsilon})=-\varepsilon\mathbb{P}(A_{\varepsilon}).\end{align*}
$$
 

于是有 $P(A_{\varepsilon})=0$。由于 $\varepsilon>0$是任意的，故有 $P(\eta\leqslant0)=1$。

现令$\zeta=\liminf_{n\to\infty}S_n/n$，则$-\zeta=\limsup_{n\to\infty}(-S_n)/n$。对$-\xi_1$应用已证结果可得$P(\zeta\geq0)=1$，最终有$S_n/n$ a.s。收敛于$0$。在不假定$E[\xi_1|\mathcal{T}]=0$的情形下，我们有$S_n/n$ a.s。收敛于$E[\xi_1|\mathcal{T}]$。

往证 $S_n/n\ L^p$收敛于 $\mathbb{E}[\xi_1|\mathcal{T}]$。为此令 $\eta_1$为一有界随机变量，使得 $\|\xi_1 - \eta_1\|_p \leq \varepsilon$。则有

 
$$
\begin{align*}\Big\|\frac{1}{n}\sum_{k=1}^{n}\xi_{1}(T^{k-1})-\mathbb{E}[\xi_{1}|\mathcal{T}]\Big\|_{p}&\leq\Big\|\frac{1}{n}\sum_{k=1}^{n}[\xi_{1}(T^{k-1})-\eta_{1}(T^{k-1})]\Big\|_{p}\\+\Big\|\frac{1}{n}\sum_{k=1}^{n}\eta_{1}(T^{k-1})-\mathbb{E}[\eta_{1}|\mathcal{T}]\Big\|_{p}&+\big\|\mathbb{E}[\eta_{1}|\mathcal{T}]-\mathbb{E}[\xi_{1}|\mathcal{T}]\big\|_{p}.\end{align*}
$$
 

上式右端第一、三两项都不超过ε，第二项当n → ∞时趋于0(由控制收敛定理). 由于ε > 0是任意的，于是Sₙ/n Lᵖ收敛于E[ξ₁|T].

下面研究遍历定理是否对一般的平稳随机序列成立？答案是肯定的。因为对给定一概率空间( $\Omega$,  $\mathcal{F}$,  $\mathbb{P}$)上任一平稳随机序列 $\xi = (\xi_1, \xi_2, \cdots)$，我们可以构造另一概率空间( $\hat{\Omega}$,  $\hat{\mathcal{F}}$,  $\tilde{\mathbb{P}}$)和其上的随机序列 $\tilde{\xi} = (\tilde{\xi}_1, \tilde{\xi}_2, \cdots)$，以及一保测变换 $T$，使得 $\tilde{\xi}_n(\tilde{\omega}) = \tilde{\xi}_1(T^{n-1}(\tilde{\omega}))$，并且 $\xi$与 $\tilde{\xi}$同分布。事实上，令 $\tilde{\Omega}$为坐标空间 $R^\infty$， $\tilde{\mathcal{F}} = \mathcal{B}(R^\infty)$， $\tilde{P}(B) = \mathbb{P}(\xi \in B)$， $B \in \mathcal{B}(R^\infty)$。设 $\tilde{\omega} = (x_1, x_2, \cdots)$，令

 
$$
T(x_{1},x_{2},\cdots)=(x_{2},x_{3},\cdots),
$$
 

 
$$
\tilde{\xi}_{1}(\tilde{\omega})=x_{1},\tilde{\xi}_{n}(\tilde{\omega})=\xi_{1}(T^{n-1}\tilde{\omega}),\ n\geqslant2.
$$
 

由于ξ是平稳序列，易知T是(R∞, B(R∞), ℱ)上的保测变换，且ξ与ξ同分布。此外有T = {B : B ∈ B(R), ℱ(T⁻n(B)△B) = 0}。

因此, 我们证明了如下的定理.

定理7.6.9 (遍历定理) 设 $(\Omega,\mathcal{F},\mathbb{P})$ 为概率空间， $\xi=(\xi_{1},\xi_{2},\cdots)$ 为 $L^{p}(\Omega,\mathcal{F},\mathbb{P})$ 中的一平稳随机变量序列。则当 $n\to\infty$， $S_{n}/n$ a.s. 和 $L^{p}$ 收敛于 $E[\xi_{1}|\xi^{-1}(\mathcal{T})]$.

下面我们将遍历定理推广到连续时间情形.

---

定理7.6.10 设$(\Omega, \mathcal{F}, \mathbb{P})$是一概率空间，$\{T_t, t \geq 0\}$是一族保测变换，构成一个半群（即满足：$T_t T_s = T_{t+s}, \forall t, s \geq 0, T_0$是恒等映射）。如果$(\omega, t) \mapsto T_t(\omega)$是$(\Omega \times \mathbb{R}_+)'$上的$\mathcal{F} \times \mathcal{B}(\mathbb{R}_+)'$可测映射，则对任一$\xi \in L^p(\Omega, \mathcal{F}, \mathbb{P})$，$p \geq 1$，当$n \to \infty, t^{-1} \int_0^t \xi(T_s) ds$a.s. 和$L^p$收敛于$E[\xi | \mathcal{G}]$，其中$\mathcal{G} = \cap_{t \in \mathbb{R}_+} T_t$。

证 不妨设 $\xi$为非负随机变量, 则由Jensen不等式和Fubini定理,

 
$$
\begin{align*}\mathbb{E}\big|t^{-1}&\int_{0}^{t}\xi(T_{s})ds\big|^{p}\leqslant t^{-1}\mathbb{E}\int_{0}^{t}\xi^{p}(T_{s})\\&=t^{-1}\int_{0}^{t}\mathbb{E}[\xi^{p}(T_{s})]=\mathbb{E}[\xi^{P}]<\infty.\end{align*}
$$
 

令 $\xi_{1}=\int_{0}^{1}\xi(T_{s})ds$,  $T=T_{1}$，则由定理7.6.7,  $t^{-1}\int_{0}^{t}\xi(T_{s})ds$ a.s. 和  $L^{p}$ 收敛于  $\mathbb{E}[\xi_{1}|\mathcal{T}]$.

下面证明  $E[\xi_1|\mathcal{T}] = E[\xi|\mathcal{G}]$。令  $\eta = E[\xi_1|\mathcal{T}]$，则

 
$$
\eta=\lim_{r\to\infty}\limsup_{n\to\infty}n^{-1}\int_{r}^{r+n}\xi(T_{s})ds,\mathrm{~a.s.},
$$
 

从而η是G可测的. 由于对所有s ≥ 0, ξ(T_s) 与ξ 同分布, 我们有E[ξ|G] = E[ξ(T_s)|G], a.s., 于是由Fubini定理,

 
$$
\mathbb{E}[\xi|\mathcal{G}]=\mathbb{E}\Big[t^{-1}\int_{0}^{t}\xi(T_{s})d s|\mathcal{G}\Big]\xrightarrow{\mathrm{~\tiny~P~}}\mathbb{E}[\eta|\mathcal{G}]=\eta,\mathrm{~\tiny~a.s.~}.
$$
 

### 7.7 解析集与Choquet 密度

设 $(\Omega,\mathcal{F})$为一可测空间．本节主要介绍 $\mathcal{F}$解析集的概念和基本性质，并借助于Choquet容度证明 $\mathcal{F}$解析集是普遍可测集.

定义7.7.1 设$F$为一抽象集合，$\mathcal{F}$为$F$上一集类，且$\emptyset \in \mathcal{F}$。令$A$为$F$的一子集，如果存在一可距离化紧拓扑空间$E$及$E \times F$的一子集$B \in (\mathcal{K}(E) \otimes \mathcal{F})_{\sigma\delta}$，使得$A$为$B$在$F$上的投影，则称$A$为$\mathcal{F}$解析集。这里$\mathcal{K}(E)$表示$E$中紧子集全体，$\mathcal{K}(E) \otimes \mathcal{F} = \{K \times G \mid K \in \mathcal{K}(E), G \in \mathcal{F}\}$。

今后用 $A(\mathcal{F})$表示 $\mathcal{F}$解析集全体，由定义立刻推知如下

引理7.7.2 设F为F上一集类，且 $\varnothing \in \mathcal{F}$.则

(1)  $\mathcal{F} \subset \mathcal{A}(\mathcal{F})$;

(2)  $A \in \mathcal{A}(\mathcal{F}) \Rightarrow$ 存在  $B \in \mathcal{F}_\sigma$，使  $B \supset A$;

(3)  $F \in \mathcal{A}(\mathcal{F}) \Leftrightarrow F \in \mathcal{F}_\sigma$;

(4) 若  $\mathcal{G}$ 为  $F$ 上一集类，且  $\mathcal{G} \supset \mathcal{F}$，则  $\mathcal{A}(\mathcal{G}) \supset \mathcal{A}(\mathcal{F})$。

---

定理7.7.3 设F为F上一集类，且 $\varnothing\in\mathcal{F}$，则 $\mathcal{A}(\mathcal{F})$对可列并及可列交运算封闭。证 设 $A_{n}\in\mathcal{A}(\mathcal{F}),n\geq1$。依定义，对每个n，存在一可距离化紧空间 $E_{n}$及 $E_{n}\times F$的一子集 $B_{n}\in(\mathcal{K}(E_{n})\otimes\mathcal{F})_{\sigma\delta}$，使得 $A_{n}$为 $B_{n}$在F上的投影。令E为乘积拓扑空间 $\prod_{n}E_{n}$，则易知E是可距离化的紧空间。令 $C_{n}=E_{1}\times\cdots\times E_{n-1}\times B_{n}\times E_{n+1}\cdots$（下面简记为 $\prod E_{m}\times B_{n}$），则有

$$
\bigcap_{n}A_{n}=\bigcap_{n}\pi(C_{n})=\pi(\bigcap_{n}C_{n}),   \tag*{(7.7.1)}
$$

这里 $\pi$表示 $E \times F$到 $F$上的投影，并将 $C_n$视为 $E \times F$的子集。设 $B_n = \bigcap_{k} B_{n,k}$，其中 $B_{n,k} \in (K(E_n) \otimes \mathcal{F})_{\sigma}, k \geq 1$。由于 $\prod_{m \neq n} E_m \times B_{n,m} \in (\mathcal{K}(E) \otimes \mathcal{F})_{\sigma}$，故 $C_n \in (\mathcal{K}(E) \otimes \mathcal{F})_{\sigma\delta}$，从而 $\bigcap_{n} C_n \in (\mathcal{K}(E) \otimes \mathcal{F})_{\sigma\delta}$。由(7.7.1)式知 $\bigcap_{n} A_n \in \mathcal{A}(\mathcal{F})$，这表明 $\mathcal{A}(\mathcal{F})$对可列交运算封闭。

现令 $E$为 $(E_n)$的拓扑和 $\sum_n E_n$的单点紧化，则 $E$为可距离化紧空间。将 $\sum_n (E_n \times F)$与 $(\sum_n E_n) \times F$视为同一，并用 $\pi$表示 $E \times F$到 $F$上的投影，则有

$$
\pi(\sum_{n}B_{n})=\bigcup_{n}A_{n}.   \tag*{(7.7.2)}
$$

由于 $\sum_{n}B_{n,k}\in(\mathcal{K}(E)\otimes\mathcal{F})_{\sigma}$，且 $\forall n\neq m,\quad B_{n,k}\cap B_{m,j}=\varnothing$，故有

 
$$
\sum_{n}B_{n}=\sum_{n}\bigcap_{k}B_{n,k}=\bigcap_{k}\sum_{n}B_{n,k}\in(\mathcal{K}(E)\otimes\mathcal{F})_{\sigma\delta}.
$$
 

于是由(7.7.2)式知， $\bigcup A_n \in \mathcal{A}(\mathcal{F})$。这表明 $\mathcal{A}(\mathcal{F})$对可列并运算封闭。

引理7.7.4 设F为F上一集类，且 $\varnothing \in \mathcal{F}$，令E为一可距离化紧空间。则 $\forall A \in \mathcal{A}(\mathcal{K}(E) \otimes \mathcal{F})$，A到F上投影为 $\mathcal{F}$解析集。

证 依定义, 存在一可距离化紧空间  $G$ 及  $\mathcal{K}(G) \otimes \mathcal{K}(E) \otimes \mathcal{F}$  $\sigma\delta$ 的一元素  $A_1$, 使得  $A$ 为  $A_1$ 在  $E \times F$ 上的投影。但  $G \times E$ 为可距离化紧空间,  $\mathcal{K}(G) \otimes \mathcal{K}(E) \subset \mathcal{K}(G \times E)$, 且  $A_1$ 在  $F$ 上的投影与  $A$ 在  $F$ 上的投影一致, 故  $\pi(A)$ 为  $\mathcal{F}$ 解析集（因为依定义  $\pi(A_1)$ 为  $\mathcal{F}$ 解析集）。

定理7.7.5 设F为F上一集类，且 $\varnothing \in \mathcal{F}$，则有

(1)  $\mathcal{A}(\mathcal{A}(\mathcal{F})) = \mathcal{A}(\mathcal{F});$

(2) 为要  $\sigma(\mathcal{F}) \subset \mathcal{A}(\mathcal{F})$，必须且只需： $A \in \mathcal{F} \Rightarrow A^{c} \in \mathcal{A}(\mathcal{F})$.

证 (1) 设  $A \in \mathcal{A}(\mathcal{A}(\mathcal{F}))$，则存在一可距离化紧空间  $E$ 及  $-A' \in (\mathcal{K}(E) \otimes \mathcal{A}(\mathcal{A}(\mathcal{F})))$  $\sigma_{\delta}$，使得  $A$ 为  $A'$ 在  $F$ 上的投影。但显然有

 
$$
\mathcal{K}(E)\otimes\mathcal{A}(\mathcal{F})\subset\mathcal{A}(\mathcal{K}(E)\otimes\mathcal{F}),
$$
 

---

故由定理7.7.3知 $A' \in \mathcal{A}(\mathcal{K}(E) \otimes \mathcal{F})$。因此，由引理7.7.4知 $A \in \mathcal{A}(\mathcal{F})$。(1)得证。

(2) 只需证充分性. 设(2)中条件成立, 令

 
$$
\mathcal{G}=\{A\in\mathcal{A}(\mathcal{F})\mid A^{c}\in\mathcal{A}(\mathcal{F})\},
$$
 

则  $F \subset \mathcal{G}$，并由定理7.7.3知， $\mathcal{G}$ 为  $\sigma$ 代数，故  $\sigma(\mathcal{F}) \subset \mathcal{G} \subset \mathcal{A}(\mathcal{F})$.

定理7.7.6 设 $(\Omega,\mathcal{F})$为一可测空间，X为一具可数基的局部紧Hausdorff空间.则有

(1)  $\mathcal{B}(X) \subset \mathcal{A}(\mathcal{K}(X)), \mathcal{A}(\mathcal{B}(X)) = \mathcal{A}(\mathcal{K}(X));$

(2)  $\mathcal{A}(\mathcal{K}(X) \otimes \mathcal{F}) = \mathcal{A}(\mathcal{B}(X) \times \mathcal{F});$

(3)  $\forall A \in \mathcal{A}(\mathcal{K}(X) \otimes \mathcal{F}), A$ 在  $\Omega$ 上的投影为  $\mathcal{F}$ 解析集.

证 (1) 设  $K \in \mathcal{K}(X)$，则  $K^c$ 为开集。令  $\mathcal{U}$ 为  $X$ 的可数基，则对每个  $x \in K^c$，存在开集  $U$，其闭包为紧集，使得  $x \in U \subset \overline{U} \subset K^c$。于是存在  $V \in \mathcal{U}$，使得  $\overline{V}$ 为紧集，且  $x \in V \subset \overline{V} \subset K^c$。令  $\mathcal{V} = \{V \in \mathcal{U} \mid \overline{V}$ 为紧集，且  $\overline{V} \subset K^c\}$，则  $V$ 为可数类，且  $K^c = \bigcup_{V \in \mathcal{V}} \overline{V}$，故  $K^c \in \mathcal{K}(X)_{\sigma}$，从而  $K^c \in \mathcal{A}(\mathcal{K}(X))$。由于  $\sigma(\mathcal{K}(X)) = \mathcal{B}(X)$，故由定理7.7.5知， $\mathcal{K}(X) \subset \mathcal{B}(X) \subset \mathcal{A}(\mathcal{K}(X))$，从而有  $\mathcal{A}(\mathcal{B}(X)) = \mathcal{A}(\mathcal{K}(X))$。

(2)  $B \in \mathcal{K}(X) \otimes \mathcal{F}$，则  $B^c \in (\mathcal{K}(X) \otimes \mathcal{F})_\sigma \subset \mathcal{A}(\mathcal{K}(X) \otimes \mathcal{F})$。又由于  $\sigma(\mathcal{K}(X) \otimes \mathcal{F}) = \mathcal{B}(X) \times \mathcal{F}$，故  $\mathcal{K}(X) \otimes \mathcal{F} \subset \mathcal{B}(X) \times \mathcal{F} \subset \mathcal{A}(\mathcal{K}(X) \otimes \mathcal{F})$（定理7.7.5(2)）。因此由定理7.7.5(1)知， $\mathcal{A}(\mathcal{K}(X) \otimes \mathcal{F}) = \mathcal{A}(\mathcal{B}(X) \times \mathcal{F})$。

(3) 由于 X 是 σ 紧的 (习题 5.1.8)，存在  $K_{n} \in \mathcal{K}(X), n \geq 1$，使  $X = \bigcup_{n} K_{n}$。对每个 n，我们有 (见习题 7.7.1)

 
$$
\begin{aligned}{}&{{}\quad(K_{n}\times\Omega)\cap\mathcal{A}(\mathcal{K}(X)\otimes\mathcal{F})}\\ {}&{{}=\mathcal{A}((K_{n}\times\Omega)\cap(\mathcal{K}(X)\otimes\mathcal{F}))}\\ {}&{{}=\mathcal{A}((K_{n}\cap\mathcal{K}(X))\otimes\mathcal{F}).}\\ \end{aligned}
$$
 

由于 $K_n$为可距离化紧空间，且 $\mathcal{K}(K_n) = K_n \cap \mathcal{K}(X)$，故对任何 $A \in \mathcal{A}(\mathcal{K}(X) \otimes \mathcal{F})$， $(K_n \times \Omega) \cap A$在 $\Omega$上的投影为 $\mathcal{F}$解析集(引理7.7.4)。但 $A = \bigcup_n[(K_n \times \Omega) \cap A]$，故 $A$在 $\Omega$上的投影也是 $\mathcal{F}$解析集。

下面我们定义Choquet容度.

定义7.7.7 设F为F上一集类，对有限并及有限交运算封闭，且 $\varnothing \in \mathcal{F}$。令 $\mathcal{A}(F)$表示F的所有子集全体，I为 $\mathcal{A}(F)$上的一非负集函数。称I为F上的Choquet $\mathcal{F}$容度，如果I具有下列性质：

(1) I单调非降:  $A \subset B \Rightarrow I(A) \leqslant I(B);$

(2) I从下连续:  $A_{n} \uparrow A \Rightarrow I(A_{n}) \uparrow I(A)$;

---

(3)  $I$ 沿  $\mathcal{F}$ 从上连续:  $A_n \in \mathcal{F}, A_n \downarrow A \Rightarrow I(A_n) \downarrow I(A)$.

F的子集A称为I可容的, 如果

$$
I(A)=\sup\{I(B)\mid B\subset A,B\in\mathcal{F}_\delta\}.   \tag*{(7.7.3)}
$$

引理7.7.8 设I为F上的Choquet F容度，则 $F_{\sigma\delta}$中每个元素都是I可容的.

证 设  $A \in \mathcal{F}_{\sigma\delta}$，若  $I(A) = -\infty$，则  $I(\varnothing) = -\infty$。故(7.7.3)式成立。现设  $I(A) > -\infty$，令  $A_{n,m} \in \mathcal{F}$，使得  $A = \bigcap_{n \quad m} A_{n,m}$。由于  $\mathcal{F}$ 对有限并运算封闭，故不妨设对固定  $n$， $(A_{n,m}, m \geq 1)$ 为非降序列。令  $A_{n} = \bigcup_{m=1}^{\infty} A_{n,m}, n \geq 1$。为证(7.7.3)式，只需证明：对任何  $a < I(A)$，存在  $B \in \mathcal{F}_{\delta}, B \subset A$，使  $I(B) \geq a$。

现设 $a<I(A)$，由I的从下连续性，我们有

 
$$
I(A)=I(A\cap A_{1})=\lim_{m\to\infty}I(A\cap A_{1,m}).
$$
 

故存在 $m_{1}$，使 $I(A\cap A_{1,m_{1}})>a$。这时有

 
$$
I(A\cap A_{1,m_{1}})=I(A\cap A_{1,m_{1}}\cap A_{2})=\lim_{m\to\infty}I(A\cap A_{1,m_{1}}\cap A_{2,m}),
$$
 

于是存在 $m_{2}$，使 $I(A\cap A_{1},m_{1}\cap A_{2},m_{2})>a$。依此类推，我们得到一自然数列 $(m_{k})_{k\geq1}$，使得对一切 $k\geq1$，有

 
$$
I(A\cap A_{1,m_{1}}\cap\cdots\cap A_{k,m_{k}})>a.
$$
 

令 $B_{n}=\bigcup_{k=1}^{n}A_{k,m_{k}},B=\bigcap_{n=1}^{\infty}B_{n}$，则 $B_{n}\in\mathcal{F},B_{n}\downarrow B\in\mathcal{F}_{\delta}$。由于 $I(B_{n})>a$，故由I沿 $\mathcal{F}$的从上连续性知， $I(B)=\lim_{n\to\infty}I(B_{n})\geq a$。由于 $B_{n}\subset A_{n}$，故 $B\subset A$。

定理7.7.9 设I为F上的Choquet F容度，则一切F解析集都是I可容的.

证 设  $A \in \mathcal{A}(\mathcal{F})$，则存在一可距离化紧空间  $E$ 及  $-B \in (\mathcal{K}(E) \otimes \mathcal{F})_{\sigma\delta}$，使得  $A = \pi(B)$。这里  $\pi$ 为  $E \times F$ 到  $F$ 上的投影。令  $\mathcal{H} = (\mathcal{H}(E) \otimes \mathcal{F})_{\cup f}(\mathcal{C}_{\cup f}$ 表示用有限并运算封闭  $\mathcal{C}$ 所得集类），由于  $\mathcal{K}(E) \otimes \mathcal{F}$ 对有限交运算封闭，故  $\mathcal{H}$ 亦然。此外有  $\mathcal{H}_{\sigma\delta} = (\mathcal{K}(E) \otimes \mathcal{F})_{\sigma\delta}$。令

 
$$
J(H)=I(\pi(H)),\ H\supset E\times F,
$$
 

往证J为 $E \times F$上的Choquet H容度. 显然J满足定义7.7.7中的性质(1)及(2). 剩下只需验证性质(3).

设 $H\in\mathcal{H},H=\bigcup_{k=1}^{m}(C_{k}\times D_{k})$，其中 $C_{k}\in\mathcal{K}(E)$， $D_{k}\in\mathcal{F}$，则对 $x\in\pi(H)$，我们有 $(E\times\{x\})\cap H=C\times\{x\}$，其中 $C\neq\varnothing$，且

 
$$
C=\bigcup_{\{k\mid x\in D_{k}\}}C_{k}\in\mathcal{K}(E).
$$
 

---

现设 $B_n \in \mathcal{H}, B_n \downarrow$。令 $x \in \bigcap_{n=1}^\infty \pi(B_n)$，则对每个 $n$，存在 $C_n \in \mathcal{K}(E)$，使得

 
$$
\left(E\times\{x\}\right)\cap B_{n}=C_{n}\times\{x\}.
$$
 

由于 $B_n \downarrow$，故 $C_n \downarrow$。又因 $C_n$为 $E$的非空紧子集，故 $\bigcap C_n \neq \varnothing$，于是

 
$$
(E\times\{x\})\cap\bigcap_{n}B_{n}=\bigcap_{n}C_{n}\times\{x\}\neq\varnothing,
$$
 

即有 $x \in \pi(\bigcap_n B_n)$。这表明 $\bigcap_n \pi(B_n) \subset \pi(\bigcap_n B_n)$。但相反的包含关系恒成立，故有

$$
\bigcap_{n}\pi(B_{n})=\pi(\bigcap_{n}B_{n}).   \tag*{(7.7.4)}
$$

由于 $\pi(B_n) \in \mathcal{F}, \pi(B_n) \downarrow$，故由 $I$沿 $\mathcal{F}$的从上连续性得

 
$$
\begin{align*}J(\bigcap_{n}B_{n})&=I\big(\pi(\bigcap_{n}B_{n})\big)=I(\bigcap_{n}\pi(B_{n}))\\&=\lim_{n\to\infty}I(\pi(B_{n}))=\lim_{n\to\infty}J(B_{n}),\end{align*}
$$
 

这表明J沿H从上连续. 因此J为 $E \times F$上的Choquet H容度.

下面借助于容度$J$证明$A$是$I$可容的。由于$B \in \mathcal{H}_{\sigma\delta}$，故由引理7.7.8，$B$为$J$可容的。但由(7.7.4)式看出：$C \in \mathcal{H}_{\delta} \Rightarrow \pi(C) \in \mathcal{F}_{\delta}$，于是有

 
$$
\begin{aligned}I(A)&=I(\pi(B))=J(B)=\sup(J(C)\mid C\subset B,C\in\mathcal{H}_{\delta}\}\\&=\sup\{I(\pi(C))\mid C\subset B,C\in\mathcal{H}_{\delta}\}\\&\leqslant\sup\{I(D)\mid D\subset A,D\in\mathcal{F}_{\delta}\}.\end{aligned}
$$
 

但恒有 $I(A) \geq \sup\{I(D) \mid D \subset A, D \in \mathcal{F}_\delta\}$，故该式实际上等号成立。这表明 $A$是 $I$可容的。

作为Choquet定理的一个重要应用, 我们证明可测空间 $(\Omega,\mathcal{F})$ 中一切 $\mathcal{F}$ 解析集都是普遍可测的.

定理7.7.10 设 $(\Omega,\mathcal{F})$为一可测空间，令 $\widehat{\mathcal{F}}$表示 $\mathcal{F}$的普遍完备化（即 $\widehat{\mathcal{F}}=\bigcap_{\mathbb{P}\in\mathcal{P}}\overline{\mathcal{F}^{P}}$，其中 $\mathcal{P}$为 $(\Omega,\mathcal{F})$上概率测度全体），则有 $\mathcal{A}(\mathcal{F})\subset\widehat{\mathcal{F}}=\mathcal{A}(\widehat{\mathcal{F}})$.

证 设IP为 $(\Omega,\mathcal{F})$上一概率测度，令

$$
I(A)=\inf\{IP(B)\mid B\supset A,B\in\mathcal{F}\},A\subset\Omega,   \tag*{(7.7.5)}
$$

易证I是Ω上的Choquet F容度. 由定理7.7.9知,  $\forall A \in \mathcal{A}(\mathcal{F})$, 有(注意:  $\mathcal{F} = \mathcal{F}_\delta$)

$$
I(A)=\sup\{IP(B)\mid B\subset A,B\in\mathcal{F}\}.   \tag*{(7.7.6)}
$$


---

由(7.7.5)式及(7.7.6)式知 $A \in \overline{F}^P$，但概率测度 $P$是任意的，故 $A \in \widehat{F}$。这表明 $A(\mathcal{F}) \subset \widehat{F}$，进一步有

 
$$
\widehat{\mathcal{F}}\subset\mathcal{A}(\widehat{\mathcal{F}})\subset(\widehat{\mathcal{F}})\widehat{=}\widehat{\mathcal{F}},
$$
 

从而 $A(\widehat{F})=\widehat{F}.$

注7.7.11 设 $(\Omega, \mathcal{F})$为一可分且可离的可测空间. 若存在 $A \in \mathcal{A}(\mathcal{B}(R))$使 $(\Omega, \mathcal{F})$与 $(A, \mathcal{B}(A))$同构, 则称 $(\Omega, \mathcal{F})$为Souslin可测空间. 由定理7.7.10知Souslin可测空间为Radon可测空间.

##### 习题

7.7.1 设F为F上一集类，且 $\varnothing \in \mathcal{F}$，设A为F的一子集，令 $A \cap \mathcal{F} = \{A \cap B \mid B \in \mathcal{F}\}$，则有 $A(A \cap \mathcal{F}) = A \cap A(\mathcal{F})$。这里 $A \cap \mathcal{F}$考虑为A上的集类。

7.7.2 设I为F上的Choquet F容度，则I为F上的Choquet  $F_{\delta}$ 容度.

---

## 第 8 章 离散时间鞅

鞅(martingale)这一概念是J. Ville于1939年首先引进概率论的，他借用了法文martingale有“倍赌策略”(即赌输后加倍赔注)这一含义。中译名“鞅”(马颔缰)则是该法文词的另一含义。Lévy最早研究了鞅序列。1953年Doob在Stochastic Processes这部历史性专著中首次系统总结了Lévy和他自己有关鞅的理论及应用成果，使鞅论成了随机过程理论的一个独立分支。

本章介绍有关离散时间鞅的主要结果, 如鞅不等式、Snell包络、鞅的Doob停止定理、Doob收敛定理、鞅极限定理和局部鞅等.

## 8.1 鞅不等式

设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $(\mathcal{F}_{n},n\geq0)$为 $\mathcal{F}$子 $\sigma$代数单调增列。令 $\mathcal{F}_{\infty}\hat{=}\sigma(\cup_{n}\mathcal{F}_{n})$。随机变量序列 $(X_{n},n\geq0)$称为关于 $(\mathcal{F}_{n})$适应的，如果每个 $X_{n}$为 $\mathcal{F}_{n}$可测的。

定义8.1.1 设 $(X_{n},n\geq0)$为一关于 $(\mathcal{F}_{n})$适应的随机变量序列，称 $(X_{n},n\geq0)$为鞅(上鞅,下鞅)，如果每个 $X_{n}$为可积，且

 
$$
\mathbb{E}[X_{n+1}\mid\mathcal{F}_{n}]=X_{n}(\leqslant X_{n},\geqslant X_{n}),\mathrm{~a.s.~}.
$$
 

如果进一步每个 $X_{n}$为平方可积，称 $(X_{n},n\geq0)$为平方可积鞅(上鞅，下鞅).

定理8.1.2 (1) 设 $(X_{n}),(Y_{n})$ 为鞅(上鞅)，则 $(X_{n}+Y_{n})$ 为鞅(上鞅)， $(X_{n}\wedge Y_{n})$ 为上鞅.

(2) 设 $(X_{n})$为鞅(下鞅). f为 $\mathbb{R}$上一连续(连续非降)凸函数. 如果每个 $f(X_{n})$可积, 则 $(f(X_{n}))$为下鞅.

证 (1)显然. (2)由Jensen不等式推得.

定义8.1.3 令  $\mathbb{N}_0 = \{0,1,2,\cdots\}$， $\overline{\mathbb{N}}_0 = \{0,1,2,\cdots,\infty\}$。设  $T$ 为  $\overline{\mathbb{N}}_0$ 值随机变量。如果对每个  $n \in \mathbb{N}_0$， $[T = n] \in \mathcal{F}_n$，则称  $T$ 为关于  $(\mathcal{F}_n)$ 的停时。对停时  $T$，令

 
$$
\mathcal{F}_{T}=\left\{A\in\mathcal{F}_{\infty}\mid A\cap[T=n]\in\mathcal{F}_{n},\forall n\geqslant0\right\},
$$
 

称 $F_{T}$为T前事件 $\sigma$代数.

下一定理列出了有关停时的一些基本结果, 其证明都是不足道的, 故从略.

定理8.1.4 设S, T为停时, $(S_{n})$为停时列.

(1)  $\Lambda_{n}S_{n}$ 和  $\forall_{n}S_{n}$ 为停时；

---

(2)  $A \in \mathcal{F}_S \Rightarrow A \cap [S \leqslant T] \in \mathcal{F}_T$,  $A \cap [S = T] \in \mathcal{F}_T$;

(3)  $S \leqslant T \Rightarrow \mathcal{F}_S \subset \mathcal{F}_T$;

(4) 设  $A \in \mathcal{F}_S$，令  $S_A = SI_A + \infty I_{A^c}$，则  $S_A$ 为停时，且  $\mathcal{F}_{S_A} \cap A = \mathcal{F}_S \cap A$。我们称  $S_A$ 为  $S$ 到  $A$ 上的局限。

定理8.1.5 设 $(X_{n})$为一适应随机序列，T为停时，则 $X_{T}I_{[T<\infty]}$为 $F_{T}$可测.

证 设B为一Borel集, $n\geqslant0$,则

 
$$
[X_{T}I_{[T<\infty]}\in B]\cap[T=\infty]=\emptyset~,
$$
 

 
$$
[X_{T}I_{[T<\infty]}\in B]\cap[T=n]=[X_{n}\in B]\cap[T=n]\in\mathcal{F}_{n}~,
$$
 

这表明 $[X_T I_{[T<\infty]}\in B]\in\mathcal{F}_T$，即 $X_T I_{[T<\infty]}$为 $\mathcal{F}_T$可测。

下一定理是有界停时的Doob停止定理. 它是证明下面的鞅不等式的基础.

定理8.1.6 设 $(X_{n})$为鞅(上鞅)，S,T为有界停时，且 $S\leqslant T$，则有

$$
\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]=X_{S}(\leqslant X_{S}),\mathrm{a.s.}.   \tag*{(8.1.1)}
$$

证 只需证上舆情形. 设  $T \leqslant n$, 由于  $\left|X_{T}\right| \leqslant \sum_{j=1}^{n} \left|X_{j}\right|$,  $\left|X_{S}\right| \leqslant \sum_{j=1}^{n} \left|X_{j}\right|$, 故  $X_{S}, X_{T}$ 可积. 令  $A \in F_{S}, j \geqslant 0$, 则

 
$$
A_{j}{\hat{=}}A\cap[S=j]\cap[T>j]\in\mathcal{F}_{j}~.
$$
 

首先假定 $T-S\leqslant1$。这时由上鞅性质

 
$$
\int_{A}(X_{S}-X_{T})d\boldsymbol{P}=\sum_{j=0}^{n}\int_{A_{j}}(X_{j}-X_{j+1})d\boldsymbol{P}\geqslant0.
$$
 

对一般情形，令 $R_j = T \wedge (S + j)$， $1 \leqslant j \leqslant n$。则每个 $R_j$为停时，且 $S \leqslant R_1 \leqslant \cdots \leqslant R_n$， $R_1 - S \leqslant 1$， $R_{j+1} - R_j \leqslant 1$（ $1 \leqslant j \leqslant n-1$）。令 $A \in \mathcal{F}_S$。由定理8.1.4(3)知 $A \in \mathcal{F}_{R_j}$， $1 \leqslant j \leqslant n$。故由前面已证结果得

$$
\int_{A}X_{S}d\mathbb{P}\geqslant\int_{A}X_{R_{1}}d\mathbb{P}\geqslant\cdots\geqslant\int_{A}X_{T}d\mathbb{P}.   \tag*{(8.1.2)}
$$

由于 $X_{S}$为 $\mathcal{F}_{S}$可测(定理8.1.5)，故由(8.1.2)式推得(8.1.1)式.

定理8.1.7 设 $k \geqslant 1$， $(X_n)_{n \leqslant k}$为一上轴。则对 $\lambda > 0$有

$$
\lambda\mathbb{P}\Big(\sup_{n\leqslant k}X_{n}\geqslant\lambda\Big)\leqslant\mathbb{E}[X_{0}]-\int_{[sup_{n\leqslant k}X_{n}<\lambda]}X_{k}d\mathbb{P},   \tag*{(8.1.3)}
$$

$$
\lambda\boldsymbol{IP}\Big(\inf_{n\leqslant k}X_{n}\leqslant-\lambda\Big)\leqslant\int_{\left[\inf_{n\leqslant k}X_{n}\leqslant-\lambda\right]}(-X_{k})d\boldsymbol{IP},   \tag*{(8.1.4)}
$$


---


$$
\lambda\mathbb{P}\Big(\sup_{n\leqslant k}\mid X_{n}\mid\geqslant\lambda\Big)\leqslant\mathbb{E}[X_{0}]+2\mathbb{E}[X_{k}^{-}].   \tag*{(8.1.5)}
$$

证 令  $T = \inf\{n \geq 0 \mid X_n \geq \lambda\} \land k$，则 T 为有界停时，且在  $\sup_{n \leq k} X_n \geq \lambda$ 上有  $X_T \geq \lambda$，在  $\left[\sup_{n \leq k} X_n < \lambda\right]$ 上有 T = k。于是由定理8.1.6得

 
$$
\begin{align*}\mathbb{E}[X_{0}]&\geqslant\mathbb{E}[X_{T}]=\int_{[\sup_{n\leqslant k}X_{n}\geqslant\lambda]}X_{T} d\mathbb{P}+\int_{[\sup_{n\leqslant k}X_{n}<\lambda]}X_{T} d\mathbb{P}\\&\geqslant\lambda\mathbb{P}(\sup_{n\leqslant k}X_{n}\geqslant\lambda)+\int_{[\sup_{n\leqslant k}X_{n}<\lambda]}X_{k} d\mathbb{P},\end{align*}
$$
 

此即8.1.3. 同理可证8.1.4. 由8.1.3及8.1.4立得8.1.5.

定理8.1.8 设 $k \geqslant 1$， $(X_n)_{n \leqslant k}$为一鞅或非负下鞅，令 $X_k^* = \sup_{n \leqslant k} |X_n|$.

(1) 对任何  $\lambda > 0$ 及  $p \geqslant 1$ 有

$$
\mathbb{P}(X_{k}^{*}\geqslant\lambda)\leqslant\lambda^{-p}\mathbb{E}[\mid X_{k}\mid^{p}].   \tag*{(8.1.6)}
$$

(2) 对任何 p > 1 有

$$
\|X_{k}^{*}\|_{p}\leqslant\frac{p}{p-1}\|X_{k}\|_{p}.   \tag*{(8.1.7)}
$$

其中 $\|\cdot\|_{p}$为 $L^{p}$范数.

不等式(8.1.6)及(8.1.7)分别称为极大值不等式及Doob不等式. 对p=2情形, 不等式(8.1.6)称为Kolmogorov不等式.

证 不妨设 $E[|X_{k}|^{p}]<\infty$。由Jensen不等式易知 $E[|X_{n}|^{p}]<\infty,0\leqslant n\leqslant k-1$。故由定理8.1.2(2)， $(|X_{n}|^{p},n\leqslant k)$为下鞅。对上鞅 $\left(-|X_{n}|^{p},0\leqslant n\leqslant k\right)$及 $\lambda^{p}$应用不等式(8.1.4)即得(8.1.6)式。

往证(8.1.7)式. 设 $\Phi$为 $R_{+}$上一右连续增函数且 $\Phi(0)=0$. 由Fubini定理及(8.1.4)式得

$$
\begin{align*}\mathbb{E}[\Phi(X_{k}^{*})]&=\int_{\Omega}\int_{[0,X_{k}^{*}]}d\Phi(\lambda)dIP=\int_{[0,\infty]}IP(X_{k}^{*}\geqslant\lambda)d\Phi(\lambda)\\&\leqslant\int_{0}^{\infty}(\lambda^{-1}\int_{[X_{k}^{*}\geqslant\lambda]}|X_{k}|dIP)d\Phi(\lambda)\\&=\mathbb{E}\Big[\Big|X_{k}\Big|\Big(\int_{0}^{X_{k}^{*}}\lambda^{-1}d\Phi(\lambda)\Big)\Big].\end{align*}   \tag*{(8.1.8)}
$$

在(8.1.8)式中令 $\Phi(\lambda)=\lambda^{p},p>1$，则由(8.1.8)式及Hölder不等式得

$$
\begin{align*}\mathbb{E}[(X_{k}^{*})^{p}]\leqslant&\frac{p}{p-1}\mathbb{E}[|X_{k}|(X_{k}^{*})^{p-1}]\\ \leqslant&\frac{p}{p-1}\Big(\mathbb{E}[|X_{k}|^{p}]\Big)^{\frac{1}{p}}\Big(\mathbb{E}[(X_{k}^{*})^{p}]\Big)^{\frac{p-1}{p}}.\end{align*}   \tag*{(8.1.9)}
$$


---

由于 $\left(|X_{n}|^{p},n\leqslant k\right)$为一下鞅，有

 
$$
\|X_{k}^{*}\|_{p}\leqslant\|\sum_{n=0}^{k}|X_{n}|\|_{p}\leqslant(k+1)\|X_{k}\|_{p}<\infty.
$$
 

在(8.1.9)式两边同乘 $\left(\mathbb{E}\left[\left(X_{k}^{*}\right)^{p}\right]\right)^{\frac{1-p}{p}}$即得(8.1.7)式.

下面我们将证明上鞅的上穿不等式. 为此, 先交代一些记号.

设 $(X_{n})$为一 $(\mathcal{F}_{n})$适应随机序列， $[a,b]$为一闭区间.令

 
$$
\begin{aligned}&T_{0}=\inf\{n\geqslant0\mid X_{n}\leqslant a\},\quad&T_{1}=\inf\{n>T_{0}\mid X_{n}\geqslant b\},\\&T_{2j}=\inf\{n>T_{2j-1}\mid X_{n}\leqslant a\},\quad&T_{2j+1}=\inf\{n>T_{2j}\mid X_{n}\geqslant b\},\\ \end{aligned}
$$
 

则 $(T_{k})$为一停时上升列.我们用 $U_{a}^{b}[X,k]$表示序列 $(X_{0},\cdots,X_{k})$上穿 $[a,b]$的次数,则显然有

 
$$
\left[U_{a}^{b}[X,k]=j\right]=\left[T_{2j-1}\leqslant k<T_{2j+1}\right]\in\mathcal{F}_{k},
$$
 

从而 $U_{a}^{b}[X,k]$为 $\mathcal{F}_{k}$可测随机变量.

定理8.1.9 设 $N \geqslant 1$， $(X_{n})_{n \leqslant N}$为一上鞅，则

$$
\mathbb{E}[U_{a}^{b}[X,N]]\leqslant\frac{1}{b-a}\mathbb{E}[(X_{N}-a)^{-}].   \tag*{(8.1.10)}
$$

证 由定理8.1.6, 对 $k \geq 0$有

 
$$
\begin{align*}0&\geq\mathbb{E}[X_{T_{2k+1}\wedge N}-X_{T_{2k}\wedge N}]\\&=\mathbb{E}[(X_{T_{2k+1}\wedge N}-X_{T_{2k}\wedge N})(I_{[T_{2k}\leq N<T_{2k+1}]}+I_{[N\geq T_{2k+1}]})]\\&\geq\mathbb{E}[(X_{N}-a)I_{[T_{2k}\leq N<T_{2k+1}]}+(b-a)I_{[N\geq T_{2k+1}]}].\end{align*}
$$
 

由于

 
$$
\left[U_{a}^{b}[X,N]\geqslant k+1\right]\subset\left[N\geqslant T_{2k+1}\right],\quad\left[T_{2k}\leqslant N<T_{2k+1}\right]\subset\left[U_{a}^{b}[X,N]=k\right],
$$
 

故有

$$
\begin{array}{r}{\mathbb{P}(U_{a}^{b}[X,N]\geqslant k+1)\leqslant\frac{1}{b-a}\mathbb{E}[(X_{N}-a)^{-}I_{[U_{a}^{b}[X,N]=k]}]~.}\end{array}   \tag*{(8.1.11)}
$$

在8.1.11式两边对k求和得8.1.10.

定理8.1.10 设 $(Z_{n},0\leqslant n\leqslant N)$为一可积随机变量的适应序列,我们倒向归纳定义序列 $(U_{n})$如下:令 $U_{N}=Z_{N}$,

 
$$
U_{n}=\operatorname{M a x}(Z_{n},\mathbb{E}[U_{n+1}|\mathcal{F}_{n}]),\ n\leqslant N-1.
$$
 

---

则有如下结论:

(1) $(U_{n})$为一上鞅，且它是控制 $(Z_{n})$（即 $U_{n}\geq Z_{n},\forall n\geq0$）的最小上鞅.称 $(U_{n})$为 $(Z_{n})$的Snell包络.

(2) 令  $T_{j,N}$ 表示在  $\{j,\cdots,N\}$ 中取值的停时全体，并令  $T_{j}=\inf\{l\geq j\mid U_{l}=Z_{l}\}$，这里约定  $\inf\varnothing:=N$，则每个  $T_{i}$ 为停时， $(U_{n}^{T_{j}})$ 为鞅，且对一切  $i\leq N$.

 
$$
U_{j}=\mathbb{E}[Z_{T_{j}}\mid\mathcal{F}_{j}]=\operatorname{e s s}\operatorname*{s u p}\big\{\mathbb{E}[Z_{T}\mid\mathcal{F}_{j}]\big|T\in\mathcal{T}_{j,N}\big\}.
$$
 

特别， $\mathbb{E}[Z_{T}]$ 在  $T_{j,N}$ 上的最大值在  $T_{j}$ 达到，且等于  $\mathbb{E}[U_{j}]$，即有

 
$$
\mathbb{E}[U_{j}]=\mathbb{E}[Z_{T_{j}}]=\operatorname*{s u p}\{\mathbb{E}[Z_{T}]\mid T\in\mathcal{T}_{j,N}\}.
$$
 

证 (1) 由于 $U_{n} \geqslant E[U_{n+1} \mid \mathcal{F}_{n}]$，且 $U_{n} \geqslant Z_{n}$， $(U_{n})$为一控制 $(Z_{n})$的上鞅。令 $(V_{n})$为一控制 $(Z_{n})$的上鞅。由倒向归纳易知 $(V_{n})$控制 $(U_{n})$。于是 $(U_{n})$控制 $(Z_{n})$的最小上鞅。

(2) 易知 $T_{n}$为停时. 由于 $U_{n}^{T_{j}}=U_{n\wedge T_{j}}$, 对 $n\leqslant N-1$有

 
$$
U_{n+1}^{T_{j}}-U_{n}^{T_{j}}=I[T_{j}\geqslant n+1](U_{n+1}-U_{n}).
$$
 

另一方面，由 $T_{j}$和 $U_{n}$的定义知，在 $[T_{j}\geq n+1]$上有

 
$$
U_{n}=\mathbb{E}[U_{n+1}\mid\mathcal{F}_{n}].
$$
 

于是有

 
$$
U_{n+1}^{T_{j}}-U_{n}^{T_{j}}=I_{[T_{j}\geqslant n+1]}(U_{n+1}-\mathbb{E}[U_{n+1}\mid\mathcal{F}_{n}]).
$$
 

注意到 $[T_j \geqslant n + 1] = [T_j \leqslant n]^c \in \mathcal{F}_n$，上一等式蕴涵

 
$$
\begin{array}{r}{\mathbb{I}E[U_{n+1}^{T_{j}}-U_{n}^{T_{j}}\mid\mathcal{F}_{n}]=0.}\end{array}
$$
 

因此对每个 $j,\left(U_{n}^{T_{j}}\right)$为鞅.由于 $U_{T_{j}}=Z_{T_{j}}$，我们有

 
$$
U_{j}=U_{j}^{T_{j}}=\mathbb{E}[U_{N}^{T_{j}}\mid\mathcal{F}_{j}]=\mathbb{E}[Z_{T_{j}}\mid\mathcal{F}_{j}].
$$
 

现在对每个 $T\in\mathcal{T}_{j,N}$，由于 $U_{T}\geq Z_{T}$且 $(U_{n})$为上鞅，我们有

 
$$
\mathbb{E}[Z_{T}\mid\mathcal{F}_{j}]\leqslant\mathbb{E}[U_{T}\mid\mathcal{F}_{j}]\leqslant U_{j}.
$$
 

(2) 得证.

---

##### 习题

8.1.1 设 $\left(\xi_{n}\right)$为一独立随机变量序列， $E\left[\xi_{1}\right]=0$，且 $\sum_{i=1}^{\infty}E\left[\xi_{i}^{2}\right]<\infty$。试证： $\sum_{i=1}^{\infty}\xi_{i}$ a.s.收敛(提示：考虑鞍 $\left(X_{n}=\sum_{i=1}^{n},n\geqslant1\right)$，利用Kolmogorov不等式及定理2.3.4证明 $\left(X_{n}\right)$ a.s.收敛).

8.1.2 设 $(X_{n})$为一鞍，T为一有穷停时，使得 $|E|X_{T}|<\infty$。试证： $|E[X_{T}]|=|E[X_{1}]|$，当且仅当 $\lim_{n\to\infty}|E[X_{n}I_{[T>n}]|=0$。

## 8.2 鞅收敛定理及其应用

下一定理是鞅的Doob收敛定理.

定理8.2.1 设 $(X_n)$为一上鞅. 如果 $\sup_n \mathbb{E}[X_n^-] < \infty$ (或者等价地,  $\sup_n \mathbb{E}[|X_n|] < \infty$, 因为 $\mathbb{E}[|X_n|] = \mathbb{E}[X_n] + 2\mathbb{E}[X_n^-]$), 则当 $n \to \infty$时,  $X_n$ a.s.收敛于一可积随机变量 $X_\infty$. 若 $(X_n)$为非负上鞅, 则对一切 $n \geq 0$有

$$
\mathbb{E}[X_{\infty}\mid\mathcal{F}_{n}]\leqslant X_{n},\mathrm{a.s.}.   \tag*{(8.2.1)}
$$

证 令Q表示有理数全体. 设 $a,b\in\mathbb{Q},a<b$. 令 $U_{a}^{b}(X)$为序列 $(X_{n})_{n\geq0}$上穿区间 $[a,b]$的次数, 即 $U_{a}^{b}(X)=\lim_{N\to\infty}U_{a}^{b}(X,N)$, 由(8.7)我们有

 
$$
\begin{align*}\mathbb{E}[U_{a}^{b}(X)]&\leqslant\frac{1}{b-a}\sup_{N}\mathbb{E}[(X_{N}-a)^{-}]\\&\leqslant\frac{1}{b-a}(a^{+}+\sup_{N}\mathbb{E}[X_{N}^{-}])<\infty.\end{align*}
$$
 

于是 $U_{a}^{b}(X)<\infty,\mathrm{a.s.}$ 令

 
$$
\begin{aligned}W_{a,b}&=[liminf_{n\to\infty}X_{n}<a,\limsup_{n\to\infty}X_{n}>b],\\W&=\bigcup_{a,b\in Q,a<b}W_{a,b}.\end{aligned}
$$
 

由于 $W_{a,b}\subset[U_{a}^{b}(X)=+\infty]$，故 $\mathbb{P}(W_{a,b})=0$，从而 $\mathbb{P}(W)=0$。若 $\omega\notin W$，则 $\lim_{n\to\infty}X_{n}(\omega)$存在，记为 $X_{\infty}(\omega)$；若 $\omega\in W$，令 $X_{\infty}(\omega)=0$。于是 $X_{n}\longrightarrow X_{\infty}$，a.s.，且由Fatou引理，

 
$$
\mathbb{E}[\left|X_{\infty}\right|]\leqslant\sup_{n}\mathbb{E}[\left|X_{n}\right|]<\infty.
$$
 

另一结论由条件期望的Fatou引理推得.

系8.2.2 设 $(X_{n})$为一鞅(上鞅). 如果 $(X_{n})$一致可积, 则 $X_{n}$ a.s. 且 $L^{1}$ 收敛于 $X_{\infty}$.

此外， $\forall n \geqslant 0$

$$
\mathbb{E}[X_{\infty}\mid\mathcal{F}_{n}]=X_{n}(\leqslant X_{n}),\mathrm{a.s.}.   \tag*{(8.2.2)}
$$


---

系8.2.3 设  $\xi$ 为一可积随机变量，令  $\xi_{n} = E[\xi \mid \mathcal{F}_{n}], \eta = E[\xi \mid \mathcal{F}_{\infty}]$，则  $\xi_{n}$ a.s. 且  $L^{1}$ 收敛于  $\eta$.

证 由于 $(\xi_{n})$一致可积(定理7.4.7)，故由定理8.2.1知， $\xi_{n}$ a.s. 且 $L^{1}$ 收敛于某 $\zeta$。设 $A\in\bigcup_{n}\mathcal{F}_{n}$，则存在某 $n$，使 $A\in\mathcal{F}_{n}$，于是有

 
$$
\begin{array}{r}{\mathbb{E}[\zeta I_{A}]=\mathbb{E}[\xi_{n}I_{A}]=\mathbb{E}[\xi I_{A}]=\mathbb{E}[\eta I_{A}].}\end{array}
$$
 

由于ζ和η均为F∞可测，故由习题7.2.1知，ζ = η，a.s..

系8.2.4 设 $1 < p < \infty$。如果 $(X_{n})$为一鞅，且 $\sup_{n} E|X_{n}|^{p} < \infty$，则 $X_{n}$ a.s. 且 $L^{p}$ 收敛于 $X_{\infty}$.

证 由Doob不等式及已知条件知 $E[\sup_n|X_n|^p]<\infty$，这蕴涵 $(|X_n|^p,p\geq1)$为一致可积。于是 $X_n$ a.s. 且 $L^p$ 收敛于 $X_\infty$。

现在我们研究“反向上鞅”(即以 $-N_{0}=\{\cdots,-2,-1,0\}$为参数集的上鞅)的收敛性.

设 $(F_n)_{n\in-\mathbb{N}_0}$为一列 $\mathcal{F}$的子 $\sigma$域，对一切 $n\in-\mathbb{N}_0$， $\mathcal{F}_{n-1}\subset\mathcal{F}_n$，关于 $(F_n)_{n\in-\mathbb{N}_0}$适应的随机序列 $(X_n)_{n\in-\mathbb{N}_0}$称为鞅(上鞅)，如果对每个 $n\in-\mathbb{N}_0$， $X_n$可积，且有

 
$$
\mathbb{E}[X_{n}\mid\mathcal{F}_{n-1}]=X_{n-1}(\leqslant X_{n-1}),\quad\mathrm{a.s.}.
$$
 

定理8.2.5 设 $(X_n)_{n\in\mathbb{N}_0}$为上鞅，则极限 $\lim_{n\to-\infty}X_n$a.s.存在.如果 $\lim_{n\to-\infty}E[X_n]<+\infty$，则 $(X_n)$一致可积， $X_n$a.s.且 $L^1$收敛于 $X_{-\infty}$.

证 我们用 $U_{a}^{b}[X,-N]$表示序列 $(X_{-N},X_{-N+1},\cdots,X_{0})$上穿区间 $[a,b]$的次数，则由(8.1.7)式得

 
$$
\mathbb{E}[U_{a}^{b}[X,-N]]\leqslant\frac{1}{b-a}\mathbb{E}[(X_{0}-a)^{-}].
$$
 

令 $U_{a}^{b}(X)=\lim_{N\to+\infty}U_{a}^{b}[X,-N]$，我们有

 
$$
\mathbb{E}U_{a}^{b}(X)\leqslant\frac{1}{b-a}\mathbb{E}[(X_{0}-a)^{-}]<+\infty.
$$
 

由于 $U_{a}^{b}(X)$为序列 $(-X_{0},-X_{-1},-X_{-2},\cdots)$上穿区间 $[-b,-a]$的次数，故由定理8.2.1的证明知 $X_{n}\to X_{-\infty},\mathrm{a.s.}$，但不必有 $|X|_{-\infty}<\infty,\mathrm{a.s.}$

当$n \to -\infty$时，$\mathbb{E}[X_n] \uparrow A > -\infty$。假定$A < +\infty$。往证$(X_n)_{n \in -N_0}$一致可积。由于$(E[X_0 | F_n])_{n \in -N_0}$一致可积，只需证$(X_n - E[X_0 | F_n])$一致可积。于是，不妨假定$(X_n)$为非负上鞅。给定$\varepsilon > 0$，取自然数$k$足够大，使得$A - E[X_{-k}] < \varepsilon / 2$。对$c > 0$及$n < -k$，由上鞅性，我们有

 
$$
\int_{[X_{n}>c]}X_{n}d\mathbb{P}=\mathbb{E}[X_{n}]-\int_{[X_{n}\leqslant c]}X_{n}d\mathbb{P}
$$
 

---

 
$$
\begin{aligned}&\leqslant\mathbb{E}[X_{n}]-\int_{[X_{n}\leqslant c]}X_{-k}d\mathbb{P}\\&=\mathbb{E}[X_{n}]-\mathbb{E}[X_{-k}]+\int_{[X_{n}>c]}X_{-k}d\mathbb{P}.\\ \end{aligned}
$$
 

由于 $A \geqslant E[X_n] \geqslant E[X_{-k}]$，故对 $n < -k$， $E[X_n] - E[X_{-k}] < \frac{\varepsilon}{2}$。另一方面，由于 $P(X_n > c) \leqslant \frac{1}{c}E[X_n] \leqslant \frac{A}{c}$。故当 $c$足够大时，对一切 $n \in \mathbb{N}_0$有

 
$$
\int_{[X_{n}>c]}X_{-k}d\mathbb{P}<\frac{\varepsilon}{2}
$$
 

及

 
$$
\int_{[X_{j}>\varepsilon]}X_{j}d\mathbb{P}<\varepsilon,\ j=0,-1,\cdots,-k.
$$
 

于是当c足够大时，有

 
$$
\sup_{n}\int_{[X_{n}>c]}X_{n}d\mathbb{P}<\varepsilon,
$$
 

这表明 $(X_{n})$一致可积. 既然 $X_{n}\to X_{-\infty}$，a.s.，故 $(X_{n})\;L^{1}$收敛于 $X_{-\infty}$.

系8.2.6 设  $\xi$ 为一可积随机变量， $(\mathcal{G}_n)_{n\in\mathbb{N}_0}$ 为一列单调下降的  $\mathcal{F}$ 的子  $\sigma$ 域。令  $\xi_n = E[\xi \mid \mathcal{G}_n]$，则  $\xi_n$ a.s. 且  $L^1$ 收敛于  $E[\xi \mid \bigcap_n \mathcal{G}_n]$。

证 对一切  $n \in -N_0$，令  $\mathcal{F}_n = \mathcal{G}_{-n}$， $\eta_n = \xi_{-n}$，则  $(\eta_n)_{n \in -N_0}$ 关于  $(\mathcal{F}_n)$ 为一致可积。

鞅。故由定理8.2.5推得结论。

作为鞅收敛定理的一个应用, 我们介绍Lévy给出的Kolmogorov强大数定律的一个简单证明.

定理8.2.7 (Kolmogorov强大数定律) 设  $\xi = (\xi_1, \xi_2, \cdots)$ 为一独立同分布随机变量序列，且  $E[|\xi_1|] < \infty$。令  $X_n = \sum_{i=1}^{n} \xi_i$，则  $\frac{X_n}{n} \to E[\xi_1]$，a.s.

证 由假定, $\forall1\leqslant i\leqslant n,\mathbb{E}[\xi_{i}\mid X_{n}]=\mathbb{E}[\xi_{1}\mid X_{n}]$，故有

 
$$
\begin{align*}\frac{X_{n}}{n}&=\frac{1}{n}\sum_{i=1}^{n}\mathbb{E}[\xi_{i}\mid X_{n}]=\mathbb{E}[\xi_{1}\mid X_{n}]\\&=\mathbb{E}[\xi_{1}\mid X_{n},\xi_{n+1},\xi_{n+2},\cdots]=\mathbb{E}[\xi_{1}\mid X_{n},X_{n+1},\cdots].\end{align*}
$$
 

令 $\mathcal{G}_n = \sigma(X_n, X_{n+1}, \cdots), Z = \mathbb{E}[\xi_1 \mid \cap_n \mathcal{G}_n]$，则由系8.2.6知 $\frac{X_n}{n}$ a.s.且 $L^1$收敛于 $Z$。 $Z$作为极限，显然有 $Z \in \cap_n \sigma(\xi_n, \xi_{n+1}, \cdots)$，故由Kolmogorov 0-1律知 $Z$ a.s.等于一常数。由于 $\mathbb{E}[\frac{X_n}{n}] = \mathbb{E}[\xi_1]$，从而有 $Z = \mathbb{E}[\xi_1]$。

定义8.2.8 一鞅(上鞅) $(X_n, n \in \mathbb{N}_0)$称为可右闭的，如果存在一可积随机变量 $X_\infty \in \mathcal{F}_\infty$，使得对一切 $n \in \mathbb{N}_0$， $\mathbb{E}[X_\infty | \mathcal{F}_n] = X_n (\leqslant X_n)$，a.s.，这时 $(X_n, n \in \mathbb{N}_0)$称为右闭鞅(上鞅)， $X_\infty$称为 $(X_n, n \in \mathbb{N}_0)$的右闭元。

---

下一定理是右闭鞅及右闭上鞅的Doob停止定理.

定理8.2.9 设 $(X_{n}, n \in \mathbb{N}_{0})$为一鞅(上鞅)，S, T为两个停时，且 $S \leqslant T$。则 $X_{S}$和 $X_{T}$可积，并且有

$$
\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]=X_{S}(\leqslant X_{S}),\mathrm{a.s.}.   \tag*{(8.2.3)}
$$

证 设 $(X_{n},n\in\overline{\mathbb{N}}_{0})$为鞅. 令 $S_{n}=SI_{[S\leqslant n]}+\infty I_{[S>n]}$，由于集合 $\{0,1,\cdots,n,\infty\}$与集合 $\{0,1,\cdots,n,n+1\}$保序同构，故由定理8.1.6，

 
$$
X_{S_{n}}=\mathbb{E}[X_{\infty}\mid\mathcal{F}_{S_{n}}],\mathrm{a.s.}.
$$
 

令 $n\rightarrow\infty$得

 
$$
\mathbb{E}[X_{\infty}\mid\mathcal{F}_{S}]=X_{S},\mathrm{a.s.}.
$$
 

特别, 这表明  $X_{S}$ 可积, 对停时 T 也有同样等式, 故有

 
$$
\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]=\mathbb{E}[\mathbb{E}[X_{\infty}\mid\mathcal{F}_{T}]\mid\mathcal{F}_{S}]=X_{S},\mathrm{a.s.}.
$$
 

现在设 $(X_n, n \in \mathbb{N}_0)$为上鞅，令 $Y_n = \mathbb{E}[X_\infty | \mathcal{F}_n]$， $Z_n = X_n - Y_n$， $Y_\infty = X_\infty$及 $Z_\infty = 0$，则 $(Z_n, n \in \mathbb{N}_0)$为非负上鞅，由于 $\mathbb{E}[Z_{S_n}] \leqslant \mathbb{E}[Z_0]$（定理8.1.6），故由Fatou引理， $Z_S$可积，从而 $X_S = Y_S + Z_S$可积。令 $T_n = TI_{[T \leqslant n]} + \infty I_{[T > n]}$，则由定理8.1.6，

 
$$
Z_{S_{n}}\geqslant\mathbb{E}[Z_{T_{n}}\mid\mathcal{F}_{S_{n}}],\mathrm{a.s.}.
$$
 

但由于 $\mathcal{F}_{S_{n}}\cap[S\leqslant n]=\mathcal{F}_{S}\cap[S\leqslant n]$，由习题7.2.6有

 
$$
\mathbb{E}[Z_{T_{n}}\mid\mathcal{F}_{S_{n}}]I_{[S\leqslant n]}=\mathbb{E}[Z_{T_{n}}\mid\mathcal{F}_{S}]I_{[S\leqslant n]}.
$$
 

从而有

$$
Z_{S}I_{[S\leqslant n]}=Z_{S_{n}}I_{[S\leqslant n]}\geqslant\mathbb{E}[Z_{T_{n}}\mid\mathcal{F}_{S}]I_{[S\leqslant n]}.   \tag*{(8.2.4)}
$$

由于 $Z_{T_{n}}\uparrow Z_{T}$，在(8.2.4)中令 $n\to\infty$得

 
$$
Z_{S}I_{[S<\infty]}\geqslant\mathbb{E}[Z_{T}\mid\mathcal{F}_{S}]I_{[S<\infty]},{\mathrm{a.s.}}.
$$
 

由于 $Z_{\infty}=0$，故有 $Z_{S}\geq E[Z_{T}\mid\mathcal{F}_{S}]$，a.s..但由已证结果， $Y_{S}=\mathbb{E}[Y_{T}\mid\mathcal{F}_{S}]$，a.s.，所以最终有

 
$$
X_{S}\geqslant\mathbb{E}[X_{T}\mid\mathcal{F}_{S}],\mathrm{a.s.}.
$$
 

定理8.2.10 设 $(X_n, n \in \mathbb{N}_0)$为一鞅(上鞅)， $S, T$为两个停时，则

$$
\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]=X_{T\wedge S}\left(\leqslant X_{T\wedge S}\right),\;\mathbf{a.s.}.   \tag*{(8.2.5)}
$$


---

证 由于 $X_{T}I_{[T\leqslant S]}$为 $F_{S}$可测，故由(8.2.3)式得

 
$$
\begin{aligned}\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]&=\mathbb{E}[X_{T}I_{[T\leqslant S]}+X_{S\vee T}I_{[T>S]}\mid\mathcal{F}_{S}]\\&=X_{T}I_{[T\leqslant S]}+X_{S}I_{[T>S]}\left(\leqslant X_{T}I_{[T\leqslant S]}+X_{S}I_{[T>S]}\right)\\&=X_{T\wedge S}\left(\leqslant X_{T\wedge S}\right),a.s..\\ \end{aligned}
$$
 

系8.2.11 设 $\xi$为一可积随机变量，S,T为两个有穷停时，则

 
$$
\begin{array}{r}{\mathbb{I}E[\mathbb{I}E[\xi\mid\mathcal{F}_{S}]\mid\mathcal{F}_{T}]=\mathbb{I}E[\xi\mid\mathcal{F}_{S\wedge T}],\mathrm{a.s.}.}\end{array}
$$
 

下一定理是一般鞅及上鞅关于有穷停时的Doob 停止定理.

定理8.2.12 (1) 设 $(X_{n}, n \geqslant 0)$为一轴，S, T为两个有穷停时. 如果 $X_{T}$可积，则

 
$$
\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]=X_{T\wedge S},\mathrm{a.s.},
$$
 

当且仅当

 
$$
\lim_{n\to\infty}\mathbb{E}[X_{n}I_{[T>n]}\mid\mathcal{F}_{S}]=0,\mathrm{a.s.}.
$$
 

(2) 设 $(X_{n}, n \geqslant 0)$为一上轴，S, T为两个有穷停时，如果 $X_{T}$可积且

 
$$
\limsup_{n\to\infty}\mathbb{E}[X_{n}I_{[T>n]}\mid\mathcal{F}_{S}]\geqslant0,\mathrm{a.s.},
$$
 

则

 
$$
\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]\leqslant X_{T\wedge S},\mathrm{a.s.}
$$
 

证 我们只证(1),(2)的证明类似. 设 $(X_{n},n\geq0)$为一鞅, 由系8.2.11和定理8.1.6知,

 
$$
\begin{align*}\mathbb{E}[X_{T}\mid\mathcal{F}_{S}]&=\lim_{n\to\infty}\mathbb{E}[X_{T}I_{[T<n]}\mid\mathcal{F}_{S}]\\&=\lim_{n\to\infty}\mathbb{E}[X_{T\wedge n}-X_{n}I_{[T\geqslant n]}\mid\mathcal{F}_{S}]\\&=\lim_{n\to\infty}(X_{T\wedge S\wedge n}-\mathbb{E}[X_{n}\dot{I}_{[T\geqslant n]}\mid\mathcal{F}_{S}])\\&=X_{T\wedge S}-\lim_{n\to\infty}\mathbb{E}[X_{n}I_{[T\geqslant n]}\mid\mathcal{F}_{S}].\end{align*}
$$
 

下一定理称为上鞅的Doob分解定理.

定理8.2.13 设 $X=(X_{n})$为一上鞅，则X可唯一地分解为

$$
X_{n}=M_{n}-A_{n},   \tag*{(8.2.6)}
$$


---

其中 $(M_{n})$为一鞅， $(A_{n})$为一增过程，满足 $A_{0}=0,A_{n}$为 $\mathcal{F}_{n-1}$可测， $n\geqslant1$.

证 设有满足定理要求的分解(8.2.5)，则

 
$$
\begin{aligned}A_{n+1}-A_{n}&=\mathbb{E}[A_{n+1}-A_{n}\mid\mathcal{F}_{n}]=\mathbb{E}[X_{n}-X_{n+1}\mid\mathcal{F}_{n}]\\&=X_{n}-\mathbb{E}[X_{n+1}\mid\mathcal{F}_{n}].\end{aligned}
$$
 

从而有

$$
A_{n}=\sum_{j=0}^{n-1}(X_{j}-\mathbb{E}[X_{j+1}\mid\mathcal{F}_{j}]),\ n\geqslant1.   \tag*{(8.2.7)}
$$

这表明：满足要求的分解如果存在，则它是唯一的．另一方面，由(8.2.6)定义 $(A_n)$，再令 $M_n = X_n + A_n$，则易知 $(M_n)$为鞅，从而 $X_n = M_n - A_n$为满足要求的分解．

系8.2.14 设 $X=(X_{n},n\geq1)$为一平方可积鞅，令

$$
[X]_{n}=\sum_{i=1}^{n}\Delta X_{i}^{2};\quad\langle X\rangle_{n}=\sum_{i=1}^{n}\mathbb{E}[\Delta X_{i}^{2}\mid\mathcal{F}_{i-1}],\quad n\geqslant1,   \tag*{(8.2.8)}
$$

其中 $X_{0}=0,\Delta X_{i}^{2}=(X_{i}-X_{i-1})^{2}$，则 $(X_{n}^{2}-\langle X\rangle_{n},n\geqslant1)$和 $(X_{n}^{2}-[X]_{n},n\geqslant1)$为鞅.

证 由上鞅 $\left(-X_{n}^{2}\right)$的Doob分解定理的证明推知 $\left(X_{n}^{2}-\langle X\rangle_{n}\right)$为鞅. 由于 $\left(\left[X\right]_{n}-\langle X\rangle_{n}\right)$为鞅, 故 $\left(X_{n}^{2}-\left[X\right]_{n}\right)$为鞅.

定理8.2.15 设 $X = (X_n, n \geq 1)$为一平方可积鞅，则序列 $(X_n)$在 $[(X)_\infty < \infty]$上a.s.收敛.

证 对任意a>0，令 $T_a=\inf\{n\mid\langle X\rangle_n>a\}$，则 $(X_{T_a\wedge n},n\geq1)$为一鞅，且由系8.2.13知 $\mathbb{E}[X_{T_a\wedge n}^2]=\mathbb{E}[\langle X\rangle_{T_a\wedge n}]\leq a$。故由鞅收敛定理知：当 $n\to\infty$时， $X_{T_a\wedge n}$ a.s.收敛。特别，在 $[T_a=\infty]$上， $X_n$ a.s.收敛。由于a是任意的，且 $[\langle X\rangle_\infty<\infty]=\cup_{k=1}^\infty[\langle X\rangle_\infty\leq k]$，故 $(X_n,n\geq1)$在 $[\langle X\rangle_\infty<\infty]$上a.s.收敛。

定理8.2.16 设 $(X_n, n \geq 1)$为一零均值轴，且 $E[\sup_n |X_n - X_{n-1}|] < \infty$。令 $\Omega_0 = [\sup_n X_n < \infty] \cup [\inf_n X_n > -\infty]$，则 $(X_n, n \geq 1)$在 $\Omega_0$上a.s.收敛。

证 令  $\xi_{n}=X_{n}-X_{n-1}$. 对任意 a>0, 令  $T_{a}=\inf\{n\mid X_{n}>a\}$, 则  $(X_{T_{a}\wedge n},n\geqslant1)$ 为一零均值鞅, 且有

 
$$
X_{T_{a}\wedge n}^{+}\leqslant X_{T_{a}\wedge(n-1)}^{+}+\xi_{T_{a}\wedge n}^{+}\leqslant a+\sup_{n}(\xi_{n}^{+}).
$$
 

由于$\mathbb{E}[|X_{t_a \wedge n}|] = 2\mathbb{E}[X_{T_a \wedge n}^+]$且$\mathbb{E}[\sup_n |\xi_n|] < \infty$，故$\mathbb{E}[|X_{T_a \wedge n}|]$关于$n$一致有界，从而当$n \to \infty$，$X_{T_a \wedge n}$a.s.收敛。特别，在$\sup_n X_n \leq a$上，$X_n$a.s.收敛。由于$a$是任意的，故$(X_n, n \geq 1)$在$\sup_n X_n < \infty$上a.s.收敛。对$(-X_n)$应用已证结果知$(X_n, n \geq 1)$在$\left[\inf_n X_n > -\infty\right]$上也a.s.收敛。

定理8.2.17 设 $(Z_n, n \geq 1)$为一关于 $(\mathcal{F}_n)$适应的随机变量序列，且 $0 \leq Z_n \leq 1$。令 $\mathcal{F}_0 = \{\varnothing, \Omega\}$，则 $[\sum_{n=1}^{\infty} Z_n < \infty] = [\sum_{n=1}^{\infty} \mathbb{E}[Z_n | \mathcal{F}_{n-1}] < \infty$，a.s.

---

证令

 
$$
\xi_{n}=Z_{n}-\mathbb{E}[Z_{n}\mid\mathcal{F}_{n-1}];\ X_{n}=\sum_{i=1}^{n}\xi_{i},\ n\geqslant1,
$$
 

则 $(X_{n},n\geqslant1)$为一零均值轴，且 $\sup_{n}|X_{n}-X_{n-1}|\leqslant2$．由于

 
$$
\Big[\sum_{n=1}^{\infty}Z_{n}<\infty\Big]\subset\big[\sup_{n}X_{n}<\infty\big],
$$
 

故由定理8.2.16知， $(X_{n}, n \geqslant 1)$在 $[\sum_{n=1}^{\infty} Z_{n} < \infty]$上a.s.收敛.因此由

 
$$
\sum_{n=1}^{\infty}\mathbb{E}[Z_{n}|\mathcal{F}_{n-1}=\sum_{n=1}^{\infty}Z_{n}<\infty-\lim_{n\to\infty}X_{n}
$$
 

推知 $[\sum_{n=1}^{\infty} Z_n < \infty] \subset [\sum_{n=1}^{\infty} \mathbb{E}[Z_n | \mathcal{F}_{n-1}] < \infty]$，a.s.，对 $(-X_n)$应用上述推理可证相反的包含关系。

作为定理的一个推论, 我们得到Borel-Cantelli引理的如下推广.

系8.2.18 设 $A_n \in \mathcal{F}_n, n \geq 1$，则

 
$$
\limsup_{n\to\infty}A_{n}=\left[\sum_{n=1}^{\infty}\mathbb{P}[A_{n+1}|\mathcal{F}_{n}]<\infty\right],a.s..
$$
 

证 在定理中令 $Z_n = I_{A_n}$，由 $\limsup A_n = [\sum_{n=1}^{\infty} I_{A_n} < \infty]$推得欲证结论。□

利用推广了的Borel-Cantelli引理和定理8.2.16, 我们得到如下Kolmogorov三级数定理的条件形式(见Hall-Heyde (1980)).

定理8.2.19 设 $(X_{n},n\geq1)$为一关于 $(\mathcal{F}_{n})$适应的随机变量序列， $S_{n}=\sum_{i=1}^{n}X_{i}$， $n\geq1$，c>0为一常数，则 $S_{n}$在满足如下三个条件的集合上a.s.收敛：

 
$$
(1)\;\sum_{i=1}^{\infty}\mathbb{P}(|X_{i}|\leqslant c\mid\mathcal{F}_{i-1})<\infty;
$$
 

(2)  $\sum_{i=1}^{\infty} E[X_i I_{|X_i| \leqslant c|} |\mathcal{F}_{i-1}]$ 收敛;

(3)  $\sum_{i=1}^{\infty}\{\mathbb{E}[X_{i}^{2}I_{|[X_{i}|\leqslant c]}|\mathcal{F}_{i-1}]-(\mathbb{E}[X_{i}I_{|[X_{i}|\leqslant c]}|\mathcal{F}_{i-1})])^{2}\}<\infty.$

证 令A表示使(1)、(2)和(3)成立的集合,由(1)和推广了的Borel-Cantelli引理得

 
$$
[S_{n} 收敛 ]=\left[\sum_{i=1}^{\infty}\mathbb{E}[X_{i}I_{|\left|X_{i}\right|\leqslant c}] 收敛 \right]=\left[\sum_{i=1}^{\infty}Y_{i} 收敛 \right],
$$
 

其中

 
$$
Y_{i}=X_{i}I_{[\mid X_{i}\mid\leqslant c]}-\mathbb{E}[X_{i}I_{[\mid X_{i}\mid\leqslant c]}\mid\mathcal{F}_{i-1}],\quad i\geqslant1.
$$
 

由于 $(\sum_{i=1}^{n}Y_{i},n\geqslant1)$为一零均值鞅，且

 
$$
\begin{array}{r}{\mathbb{E}(Y_{i}^{2}\mid\mathcal{F}_{i-1}]=\mathbb{E}[X_{i}^{2}I_{[\mid X_{i}\mid\leqslant c]}\mid\mathcal{F}_{i-1}]-(\mathbb{E}[X_{i}I_{[\mid X_{i}\mid\leqslant c]}\mid\mathcal{F}_{i-1}]))^{2},}\end{array}
$$
 

---

故由定理8.2.16知 $\sum_{i=1}^{\infty}Y_{i}$在A上a.s.收敛.

定理8.2.20 设 $(X_{n},n\geq1)$为一关于 $(\mathcal{F}_{n})$适应的随机变量序列， $(S_{n}=\sum_{i=1}^{n}X_{i},n\geq1)$为鞅， $(U_{n},n\geq1)$为一非降的非负随机变量序列，每个 $U_{n}$关于 $\mathcal{F}_{n-1}$可测.若 $1\leq p\leq2$，令

 
$$
\Omega_{1}=\Big[\sum_{i=1}^{\infty}U_{i}^{-p}\mathbb{E}[|X_{i}|^{p}\mid\mathcal{F}_{i-1}]<\infty\Big],
$$
 

 
$$
\Omega_{2}=\Big[\lim_{n\to\infty}U_{n}=\infty,\sum_{i=1}^{\infty}U_{i}^{-p}\mathbb{E}[|X_{i}|^{p}\mid\mathcal{F}_{i-1}]<\infty\Big],
$$
 

则在 $\Omega_{1}$上有 $\sum_{i=1}^{n}U_{I}^{-1}X_{i}$ a.s.收敛，在 $\Omega_{2}$上有 $\lim_{n\to\infty}U_{n}^{-1}S_{n}=0,$ a.s.. 若 $2<p<\infty$，令

 
$$
\Omega_{3}=\Big[\sum_{i=1}^{\infty}U_{n}^{-1}<\infty,\sum_{i=1}^{\infty}U_{i}^{-1-p/2}\mathbb{E}[|X_{i}|^{p}\mid\mathcal{F}_{i-1}]<\infty\Big],
$$
 

则在 $\Omega_{3}$上有 $\sum_{i=1}^{n}U_{I}^{-1}X_{i}$ a.s.收敛和 $\lim_{n\to\infty}U_{n}^{-1}S_{n}=0$, a.s..

为了证明这一定理, 我们先证明如下的Kronecker引理.

引理8.2.21 设 $(x_{i},i\geqslant1)$为实数序列， $(b_{n},n\geqslant1)$为正实数序列，且 $\lim_{n\to\infty}b_{n}=\infty$。令 $s_{n}=\sum_{i=1}^{n}x_{i},r_{n}=\sum_{i=1}^{n}b_{i}x_{i}$。如果极限 $\lim_{n\to\infty}s_{n}=s$存在且有穷，则 $\lim_{n\to\infty}r_{n}/b_{n}=0$。证令 $s_{0}=0$。由于 $b_{i}x_{i}=b_{i}(s_{i}-s_{i-1})$，我们有

 
$$
r_{n}=b_{n}s_{n}-\sum_{i=1}^{n-1}(b_{i+1}-b_{i})s_{i},\ n\geqslant2,
$$
 

 
$$
\limsup_{n\to\infty}\frac{r_{n}}{b_{n}}\leqslant\lim_{n\to\infty}\left|s_{n}-s\right|+\limsup_{n\to\infty}\left|\frac{1}{b_{n}}\sum_{i=1}^{n-1}(b_{i+1}-b_{i})s_{i}-s\right|.
$$
 

对给定 $\varepsilon>0$，存在 $n_{0}\geq1$，使得对 $n\geq n_{0}$，有 $|s_{n}-s|<\varepsilon$。故有

 
$$
\begin{align*}\left|\frac{1}{b_{n}}\sum_{i=1}^{n-1}(b_{i+1}-b_{i})s_{i}-s\right|&=\left|\frac{1}{b_{n}}\sum_{i=1}^{n-1}(b_{i+1}-b_{i})(s_{i}-s)+\frac{b_{1}}{b_{n}}s\right|\\\leqslant\varepsilon+\frac{1}{b_{n}}\sum_{i=1}^{n_{0}-1}(b_{i+1}-b_{i})|s_{i}-s|+\frac{b_{1}}{b_{n}}|s|.\end{align*}
$$
 

因此有 $\lim_{n\to\infty}r_n/b_n=0.$

证 (定理8.2.20之证) 令 $Y_{n}=U_{n}^{-1}X_{n},n\geqslant1$，则 $\left(\sum_{i=1}^{n}Y_{i},n\geqslant1\right)$为鞅. 当 $1\leqslant p\leqslant2$，由定理8.2.11推知，在 $\Omega_{1}$上 $\sum_{i=1}^{n}U_{I}^{-1}X_{i}$ a.s.收敛，从而又由Kronecker引理推知，在 $\Omega_{2}$上 $\lim_{n\to\infty}U_{n}^{-1}S_{n}=0,$ a.s..

---

下面考虑2 < p < ∞情形. 由于当 $[E[|X_n|^p | \mathcal{F}_{n-1}]^{2/p} > U_n$时，有

 
$$
[\mathbb{E}[|X_{n}|^{p}\mid\mathcal{F}_{n-1}]^{2/p}<U_{n}^{1-p/2}\mathbb{E}[|X_{n}|^{p}\mid\mathcal{F}_{n-1}],
$$
 

故有

 
$$
\begin{align*}\mathbb{E}[Y_{n}^{2}\mid\mathcal{F}_{n-1}]&=U_{n}^{-2}\mathbb{E}[X_{n}^{2}\mid\mathcal{F}_{n-1}]\leqslant[U_{n}^{-p}\mathbb{E}(|X_{n}|^{p}\mid\mathcal{F}_{n-1})]^{2/p}\\&\leqslant\max\{U_{n}^{-1},U_{n}^{-1-p/2}\mathbb{E}[|X_{n}|^{p}\mid\mathcal{F}_{n-1}]\}.\end{align*}
$$
 

余下证明与上面相同.

##### 习题

8.2.1 设 $(\xi,\xi_{n},n\geq1)\subset L^{1}(\Omega,\mathcal{F},\mathbb{P}),\xi_{n}\to\xi_{\infty},\mathrm{a.s.},\mathrm{ 且 }|\xi_{n}|\leq|\xi|,\forall n\geq1,\mathrm{ 则 }\mathbb{E}[\xi_{n}|\mathcal{F}_{n}]\mathrm{a.s.}$ 且  $L^{1}$ 收敛于  $\mathbb{E}[\xi_{\infty}|\mathcal{F}_{\infty}]$.

8.2.2 设 $(X_n, n \geq 0)$为一鞅(上鞅)，T为一有穷停时，且 $E[T] < \infty$。如果存在常数C > 0，使得对一切 $n \geq 1$，在 $[T \geq n + 1]$上a.s.有 $E[|X_{n+1} - X_n| \mid \mathcal{F}_n] \leq C$，则 $E[X_T] = \mathbb{E}[X_0](\leq \mathbb{E}[X_0])$。(提示：利用定理8.2.12.)

8.2.3 设  $\xi = (\xi_1, \xi_2, \cdots)$ 为一独立同分布随机变量序列，且  $E[|\xi_1|] < \infty$。令  $\mathcal{F}_n = \sigma(\xi_1, \cdots, \xi_n)$， $T \geq 1$ 为关于  $(\mathcal{F}_n)$ 的有穷停时，且  $E[T] < \infty$。证明如下的 Wald 等式：

 
$$
\mathbb{E}[\sum_{i=1}^{T}\xi_{i}]=\mathbb{E}[\xi_{1}]\mathbb{E}[T].
$$
 

如果进一步假定  $E[\xi_{1}^{2}] < \infty$，证明另一 Wald 等式：

 
$$
\mathbb{E}[(\sum_{i=1}^{T}\xi_{i}-T\mathbb{E}[\xi_{1}])^{2}]=\mathbb{E}[(\xi_{1}-\mathbb{E}[\xi_{1}])^{2}]\mathbb{E}[T].
$$
 

(提示: 利用习题8.2.2.)

8.2.4 利用Kolmogorov三级数定理证明如下结果(见Chow, Ann. Math. Statist. 36, 552-558): 设  $1 \leqslant p \leqslant 2$,  $(X_n)$ 为一关于  $(\mathcal{F}_n)$ 适应的随机变量序列,  $(S_n = \sum_{i=1}^n X_i, n \geqslant 1)$ 为鞅, 则  $S_n$ 在  $[\sum_{i=1}^{\infty} \mathbb{E}[|X_i|^p | \mathcal{F}_{i-1}] < \infty]$ 上 a.s. 收敛.

8.2.5 设  $X = (X_n, n \geq 1)$ 为一平方可积轴，证明在  $[(X)_\infty = \infty]$ 上有  $\lim_{n \to \infty} \langle X \rangle_n^{-1} X_n = 0$，a.s.

8.2.6 设  $X = (X_{n}, n \geq 1)$ 为一上鞅， $X_{n} = M_{n} - A_{n}$ 为其 Doob 分解．证明在  $[A_{\infty} < \infty]$ 上  $X_{n}$ a.s. 收敛.

8.2.7 设  $X = (X_n, n \geq 1)$ 为一平方可积轴，证明在  $[X_\infty < \infty]$ 上  $X_n$ a.s. 收敛。（提示：考虑下轴  $(X_n^2)$ 和  $((X_n + 1)^2)$ 并利用习题 8.2.6.）

8.2.8 设  $\xi = (\xi_1, \xi_2, \cdots)$ 为一独立随机变量序列，且  $E[\xi_n] < \infty, \forall n \geq 1$。令  $X_n = \sum_{i=1}^n \xi_i$。如果  $b_n \uparrow \infty$ 使得  $\sum_{n=1}^{\infty} \frac{E[(\xi_n - E[\xi_n])^2]}{b_n^2} < \infty$，证明  $\frac{X_n - E[X_n]}{b_n} \to 0$，a.s.（提示：利用习题8.1.1和Kronecker 引理。）

---

## 8.3 局部鞅

下面我们对鞅的概念作三种推广，并将证明这三种推广的等价性.

定义8.3.1 设 $X=(X_{n},n\geq0)$为 $(\mathcal{F}_{n})$适应的随机变量序列，称X为局部鞅，如果存在一列停时 $T_{k}\uparrow\infty$，使得对每个 $k\geq1\quad(X_{n\wedge T_{k}}I_{[T_{k}>0]},n\geq0)$为一鞅；称X为广义鞅，如果对每个n， $X_{n+1}$关于 $\mathcal{F}_{n}$为 $\sigma$可积，且有 $\mathbb{E}[X_{n+1}\mid\mathcal{F}_{n}]=X_{n}$，a.s..

定义8.3.2 设 $(M_n, n \geq 0)$为一适应序列， $(H_n)$为一可料序列(即每个 $(H_n)$为 $\mathcal{F}_{n-1}$可测， $n \geq 0$， $\mathcal{F}_{-1} \hat{=} \mathcal{F}_0$)。令 $\Delta M_n = M_n - M_{n-1}$，并令

$$
X_{0}=H_{0}M_{0},\;X_{n}=H_{0}M_{0}+\sum_{i=1}^{n}H_{i}\Delta M_{i},\;n\geqslant1,   \tag*{(8.3.1)}
$$

记为H.M. 如果 $(M_{n}, n \geqslant 0)$为一鞅，称H.M为M关于H的鞅变换.

下一定理归于Meyer (1972).

定理8.3.3 设 $X=(X_{n},n\geq0)$为一适应序列，则下列断言等价：

(1) X 为局部鞅；(2) X 为广义鞅；(3) X 为鞅变换.

证  $(1)\Rightarrow(2)$. 设X为局部鞅. 令 $T_{k}\uparrow\infty$为一列停时, 使得对每个 $k\geq1$,  $(X_{n\wedge T_{k}}I_{[T_{k}>0]},n\geq0)$为一鞅. 故有

 
$$
\begin{array}{r}{\mathbb{E}[X_{(n+1)\wedge T_{k}}I_{[T_{k}>0]}\mid\mathcal{F}_{n}]=X_{n\wedge T_{k}}I_{[T_{k}>0]},\quad n\geqslant0,}\end{array}
$$
 

从而有

 
$$
\begin{array}{r}{\mathbb{E}[X_{n+1}I_{[T_{k}>n]}\mid\mathcal{F}_{n}]=X_{n}I_{[T_{k}>n]},\quad n\geqslant0.}\end{array}
$$
 

由于当 $k \to \infty$时 $[T_k > n] \uparrow \Omega$，我们推得X为广义鞅。

 $(2)\Rightarrow(3)$. 设X为广义鞅. 令

 
$$
H_{0}=|X_{0}|,H_{n}=\mathbb{E}[|X_{n}-X_{n-1}|\mid\mathcal{F}_{n-1}],\ n\geqslant1,
$$
 

 
$$
V_{n}=\frac{1}{H_{n}}I_{[H_{n}>0]},\ n\geqslant0,
$$
 

则 $(V_{n})$为一可料序列. 令M=V.X, 则M为鞅, 且有X=H.M. 这表明X为鞅变换.

(3) $\Rightarrow$ (1). 设X=H.M 为一鞅变换, 其中M为一鞅, $(H_{n})$ 为一可料序列. 令

 
$$
T_{k}=\inf\{n\mid\left|H_{n+1}\right|\geqslant k\},\ k\geqslant1,
$$
 

则每个 $T_k$为停时， $T_k \uparrow \infty$，且 $H^{T_k}$在 $[T_k > 0]$上被 $k$界住。于是每个 $X_{n \wedge T_k} I_{[T_k > 0]}$为可积，且有

 
$$
\mathbb{E}[(X_{(n+1)\wedge T_{k}}-X_{n\wedge T_{k}})I_{[T_{k}>0]}\mid\mathcal{F}_{n}]
$$
 

---

 
$$
=H_{n}I_{[T_{k}>0]}E\big[\big(M_{n+1\wedge T_{k}}-M_{n\wedge T_{k}}\big)\big|\mathcal{F}_{n}\big]=0.
$$
 

这表明 $(X_{n\wedge T_{k}}I_{[T_{k}>0]},n\geqslant0)$ 为鞅.于是X为局部鞅.

系8.3.4 设M为局部鞅. 如果每个 $M_{n}$可积, 则M为鞅. 特别, 如果M为非负局部鞅, 且 $M_{0}$可积, 则M为鞅.

系8.3.5 设X为局部鞅, $(K_{n})$为一可料序列.则K.X为鞅变换.

证 由定理8.3.3, X = H.M 为一鞅变换, 其中M为鞅, $(H_{n})$ 为一可料序列. 令W = HK, 则W为一可料序列, 且容易验证K.X = W.M, 故K.X为鞅变换. ☐

定理8.3.6 如果 $(M_n, 0 \leqslant n \leqslant N)$为一可积随机变量的适应序列，使得对任一有界可料序列 $(H_n, 0 \leqslant n \leqslant N)$，对任意 $1 \leqslant j \leqslant N$，有 $E[\sum_{j=1}^{N} H_j \Delta M_j] = 0$，则 $(M_n, 0 \leqslant n \leqslant N)$为一鞅.

证 对 $1 \leqslant j \leqslant N, A \in \mathcal{F}_{j-1}$，令 $H_n = 0, n \neq j, H_j = I_A$。则 $(H_n)$为一有界可料序列，且依假定 $\mathbb{E}[I_A(M_j - M_{j-1})] = 0$。这表明 $\mathbb{E}[M_j | \mathcal{F}_{j-1}] = M_{j-1}$。于是 $(M_n)$为一鞅。

##### 习题

8.3.1 设 M 为一局部轴. 令  $X_{0}=1, X_{n}=\prod_{k=1}^{n}(1+\Delta M_{k}), n \geqslant 1$. 则 X 为一轴变换. 特别, 若对每个  $k \geqslant 1, \Delta M_{k} \geqslant -1$, 则 X 为一轴.

---

## 第 9 章 Hilbert空间和Banach空间上的测度

本章首先介绍欧氏空间上有限Borel测度的Fourier变换和Bochner定理，然后介绍Hilbert空间上有限Borel测度Fourier变换的刻画(Minlos-Sazanov定理)和它的一个更加常用的形式——Minlos定理，给出Hilbert空间上Gauss测度Fourier变换的刻画，最后介绍Hilbert空间上Gauss测度到Banach空间上的提升(Gross定理)和一个有关Banach空间上对称Gauss测度的Fernique定理. 本章的9.2至9.5节内容取材于黄志远、严加安(1997)第1章的部分内容.

## 9.1  $R^{m}$ 上 Borel 测度的 Fourier 变换和 Bochner 定理

定义9.1.1 设 $\mu$为 $R^{m}$上的一有限Borel测度. 令

$$
\widehat{\mu}(t)=\int_{\mathbb{R}^{m}}e^{i t\cdot x}\mu(d x),\ t\in\mathbb{R}^{m},   \tag*{(9.1.1)}
$$

称 $\hat{\mu}$为 $\mu$的Fourier变换.

显然， $\hat{\mu}$ 具有如下几条性质：

(1)  $\widehat{\mu}(0) = \mu(\mathbb{R}^m);$

(2)  $\hat{\mu}$ 在  $R^m$ 上连续;

(3)  $\hat{\mu}$ 是非负定的，即对任意自然数  $n \geqslant 2$ 及  $t_{1}, \cdots, t_{n} \in \mathbb{R}^{m}$ 和复数  $\alpha_{1}, \cdots, \alpha_{n}$，有

$$
\sum_{l,k=1}^{n}\widehat{\mu}(t_{l}-t_{k})\alpha_{l}\bar{\alpha}_{k}\geqslant0.   \tag*{(9.1.2)}
$$

事实上，(9.1.2)式可由下式推得

 
$$
\sum_{l,k=1}^{n}\widehat{\mu}(t_{l}-t_{k})\alpha_{l}\bar{\alpha}_{k}=\int_{\mathbb{R}^{m}}\left|\sum_{k=1}^{n}\alpha_{k}e^{i t_{k}\cdot x}\right|^{2}\mu(d x).
$$
 

定义9.1.2 设F是R^{m}上的一非负右连续增函数，且 $F(-\infty):=\lim_{x\to-\infty}F(x)\geq0,F(\infty)<\infty.$ 假定 $\mu_{F}$为与F联系的Lebesgue-Stieltjes测度(见定理1.5.4). 令

 
$$
f(t)=\widehat{\mu}_{F}=\int_{\mathbb{R}^{m}}e^{i t\cdot x}d F(x),\ t\in\mathbb{R}^{m},
$$
 

也称f为F的Fourier变换.

---

定义9.1.3 设 $(\Omega,\mathcal{F},\mathbb{P})$为一概率空间， $\xi=\{\xi_{i},1\leqslant i\leqslant m\}$为m维实值随机变量， $F(x_{1},\cdots,x_{m})=\mathbb{P}(\xi_{1}\leqslant x_{1},\cdots,\xi_{m}\leqslant x_{m}),x=(x_{1},\cdots,x_{m})\in\mathbb{R}^{n}$为其分布函数，令

 
$$
f(t)=\widehat{\mu}_{F}=\mathbb{E}[e^{it\cdot\xi}]=\int_{\mathbb{R}^{m}}e^{it\cdot x}dF(x),\ t=(t_{1},\cdots,t_{m})\in\mathbb{R}^{m},
$$
 

称f为随机变量 $\xi$(或分布函数F)的特征函数.

下一定理是Lévy关于增函数的Fourier变换的反演公式. 特别地, 由该定理知特征函数唯一决定其相应的分布函数.

定理9.1.4 设F是R^{m}上的一非负右连续增函数，且 $F(-\infty)=0,F(\infty)<\infty$，f为F的Fourier变换，则对任意满足a<b的F的连续点a,b有

 
$$
\begin{align*}\Delta_{b,a}F=\left(\frac{1}{2\pi}\right)^{m}\lim_{T\to\infty}\int_{[-T,T]^{m}}\prod_{j=1}^{m}\left(\frac{e^{-it_{j} b_{j}}-e^{-it_{j} a_{j}}}{-it_{j}}\right)\\\times f(t_{1},\cdots,t_{m})dt_{1}\cdots dt_{m},\end{align*}
$$
 

其中记号 $\Delta_{b,a}F$ 见定义1.5.3.

证 考虑积分

 
$$
\begin{align*}I_{T}&=\int_{[-T,T]^{m}}\prod_{j=1}^{m}\left(\frac{e^{-it_{j} b_{j}}-e^{-it_{j} a_{j}}}{-it_{j}}\right)f(t_{1},\cdots,t_{m})dt_{1}\cdots dt_{m}\\&=\int_{[-T,T]^{m}}\prod_{j=1}^{m}\left(\frac{e^{-it_{j} b_{j}}-e^{-it_{j} a_{j}}}{-it_{j}}\right)\\&\quad\int_{\mathbb{R}^{m}}e^{i\sum_{j=1}^{m} t_{j} x_{j}}dF(x_{1},\cdots,x_{m})dt_{1}\cdots dt_{m}\\&=\int_{\mathbb{R}^{m}}\int_{[-T,T]^{m}}\prod_{j=1}^{m}\left(\frac{e^{-it_{j}(b_{j}-x_{j})}-e^{-it_{j}(a_{j}-x_{j})}}{-it_{j}}\right)\\&\quad dt_{1}\cdots dt_{m} dF(x_{1},\cdots,x_{m})\\&=\int_{\mathbb{R}^{m}}\int_{[-T,T]^{m}}\prod_{j=1}^{m}\left(\frac{\sin t_{j}(b_{j}-x_{j})}{t_{j}}-\frac{\sin t_{j}(a_{j}-x_{j})}{t_{j}}\right)\\&\quad dt_{1}\cdots dt_{m} dF(x_{1},\cdots,x_{m}).\end{align*}
$$
 

于是我们有

 
$$
\begin{align*}\lim_{T\to\infty}I_{T}&=\int_{\mathbb{R}^{m}}\prod_{j=1}^{m}\left(\pi\mathrm{sgn}(b_{j}-x_{j})-\pi\mathrm{sgn}(a_{j}-x_{j})\right)dF(x_{1},\cdots,x_{m})\\&=(2\pi)^{m}\Delta_{b,a}F.\end{align*}
$$
 

---

下一定理是Lévy关于特征函数的连续性定理.

定理9.1.5 设 $(F_n)$为 $\mathbb{R}^m$上的一列分布函数， $(f_n)$为相应的特征函数列。则为要 $F_n$全收敛于 $\mathbb{R}^m$上的一分布函数 $F($即测度序列 $\left(\mu_{F_n}\right)$弱收敛于 $\mu_F$，必须且只需 $(f_n)$在 $\mathbb{R}^m$上处处收敛于一在0处连续的函数 $f$。这时 $f$必为 $F$的特征函数。特别，若特征函数列 $(f_n)$在 $\mathbb{R}^m$上处处收敛于一在0处连续的函数 $f$，则 $f$必为特征函数。

证 必要性显然，因为若 $(F_n)$全收敛于一分布函数 $F$，则由定理6.1.3知，其特征函数 $(f_n)$在 $\mathbb{R}^m$上处处收敛于 $f$。往证充分性。设 $(F_n)$为一列分布函数， $(f_n)$为相应的特征函数列。设 $(f_n)$在 $\mathbb{R}^m$上处处收敛于一在0处连续的函数 $f$。我们只需证 $(F_n)$全收敛于一分布函数 $F$。由Helly定理(定理6.1.4)知，存在 $(F_n)$的一子序列 $(F_{n_k})$弱收敛于一非负右连续增函数 $F$（即测度 $(\mu_{F_{n_k}})$淡收敛于 $\mu_F$）。下面我们证明 $F$是一分布函数，且序列 $(F_n)$本身全收敛于分布函数 $F$。

首先考虑m=1情形. 假定F不是分布函数, 即 $F(\infty)-F(-\infty)=\delta<1$. 令 $\varepsilon>0$ 使得 $\delta<1-\varepsilon$. 由于 $f(0)=\lim_{n\to\infty}f_{n}(0)=1$, 且f在0处连续, 可取 $\tau>0$ 足够小, 使得

 
$$
\left|\frac{1}{2\tau}\int_{-\tau}^{\tau}f(t)d t\right|>\delta+\frac{\varepsilon}{2}.
$$
 

现取 $x>2/(\tau\varepsilon)$，使得x和-x都是F的连续点，则

 
$$
\begin{align*}\left|\frac{1}{2\tau}\int_{-\tau}^{\tau}f_{n_{k}}(t)dt\right|&\leq\left|\frac{1}{2\tau}\int_{|y|<x}dF_{n_{k}}(y)\int_{-\tau}^{\tau}e^{ity}dt\right|\\&\quad+\left|\frac{1}{2\tau}\int_{|y|\geq x}dF_{n_{k}}(y)\int_{-\tau}^{\tau}e^{ity}dt\right|\\&\leq F_{n_{k}}(x)-F_{n_{k}}(-x)+\frac{1}{\tau}\Big|\int_{|y|\geq x}\frac{\sin\tau y}{y}dF_{n_{k}}(y)\Big|\\&<F_{n_{k}}(x)-F_{n_{k}}(-x)+\frac{\varepsilon}{2}.\end{align*}
$$
 

在上式中令 $k\rightarrow\infty$得

 
$$
\left|\frac{1}{2\tau}\int_{-\tau}^{\tau}f(t)d t\right|<F(x)-F(-x)+\frac{\varepsilon}{2}<\delta+\frac{\varepsilon}{2},
$$
 

这导致矛盾．因此F必须是一分布函数．于是 $(F_{n_{k}})$全收敛于分布函数F，且f为F的特征函数．由于特征函数唯一决定分布函数，故 $(F_{n})$的任一弱收敛子序列都全收敛于同一分布函数F．再由Helly定理推知，序列 $(F_{n})$本身全收敛于分布函数F．

现在考虑 $m > 1$情形. 任取$t_j \in \mathbb{R}, t_j \neq 0, 1 \leq j \leq m$. 令 $t = (t_1, \cdots, t_m), S_x = \{y \in \mathbb{R}^m \mid t \cdot y \leq x\}, x \in \mathbb{R}$. 又令 $G_n(x) = \mu_{F_n}(S_x)$. 如果 $F_n$是$m$维随机变量$\xi(n) = (\xi_1(n), \cdots, \xi_m(n))$的分布函数, 令$X_n = t \cdot \xi(n)$, 则 $P(X_n \leq x) = P(\xi(n) \in S_x) = \mu_{F_n}(S_x)$, 从而 $G_n$是$X_n$的分布函数, 其特征函数$\phi_n(u) = \mathbb{E}[e^{iuX_n}] = \mathbb{E}[e^{iu(t \cdot \xi(n))}] =$

---

 $f_{n}(ut),u\in\mathbb{R}.$ 令  $\phi(u)=f(ut)$，依假定， $\phi_{n}$ 处处收敛于在0处连续的函数  $\phi$，于是由上面已证结果， $G_{n}$ 全收敛于一分布函数 G. 另一方面，设  $(F_{n_{k}})$ 弱收敛于一非负右连续增函数 F，即  $(\mu_{F_{n_{k}}})$ 淡收敛于  $\mu_{F}$，则对 F 的连续点 x，有

 
$$
\lim_{k\to\infty}G_{n_{k}}(x)=\lim_{k\to\infty}\mu_{F_{n_{k}}}(S_{x})=\mu_{F}(S_{x}).
$$
 

于是对F的连续点x有 $G(x)=\mu_{F}(S_{x})$。最终有

 
$$
\mu_{F}(\mathbb{R}^{m})=\lim_{x\to\infty}\mu_{F}(S_{x})=\lim_{x\to\infty}G(x)=1.
$$
 

因此F是一分布函数，且 $(F_{n_{k}})$全收敛于分布函数F. 再由Helly定理推知，序列 $(F_{n})$本身全收敛于分布函数F. ☐

引理9.1.6 设 $m \geqslant 1, 0 < T < \infty, \phi_T$为 $\mathbb{R}^m$上的一复值连续函数，满足

 
$$
\phi_{T}(0)=1,\;\phi_{T}(t)=0,\;\forall t\in\mathbb{R}^{m}\setminus[-T,T]^{m}.
$$
 

如果对一切 $x \in \mathbb{R}^m$,

 
$$
P_{T}(x)=\left(\frac{1}{2\pi}\right)^{m}\int_{\mathbb{R}^{m}}e^{-i t\cdot x}\phi_{T}(t)d t\geqslant0
$$
 

则 $\int_{\mathbb{R}^{m}}P_{T}(x)dx=1,\phi_{T}(t)=\int_{\mathbb{R}^{m}}e^{it\cdot x}P_{T}(x)dx$为一特征函数.

证 对N>0，令 $\psi_{N}(x)=\prod_{j=1}^{m}[1-(|x_{j}|/N)]I_{[-N,N]}(x_{j}),x\in\mathbb{R}^{m}$，则

 
$$
\begin{align*}\int_{\mathbb{R}^{m}}P_{T}(x)dx&=\lim_{N\to\infty}\int_{\mathbb{R}^{m}}\psi_{N}(x)P_{T}(x)dx\\&=\lim_{N\to\infty}\left(\frac{1}{2\pi}\right)^{m}\int_{\mathbb{R}^{m}}\phi_{T}(t)\int_{\mathbb{R}^{m}}e^{-it\cdot x}\psi_{N}(x)dx dt\\&=\lim_{N\to\infty}\left(\frac{1}{2\pi}\right)^{m}\int_{\mathbb{R}^{m}}\phi_{T}(t)\prod_{j=1}^{m}\frac{(\sin(t_{j} N/2))^{2}}{t_{j}^{2}N/4}dt_{1}\cdots dt_{m}\\&=\lim_{N\to\infty}\left(\frac{1}{\pi}\right)^{m}\int_{\mathbb{R}^{m}}\phi_{T}(2v)\prod_{j=1}^{m}\frac{\sin^{2}v_{j}}{v_{j}^{2}}dv_{1}\cdots dv_{m}\\&=\left(\frac{1}{\pi}\right)^{m}\int_{\mathbb{R}^{m}}\phi_{T}(0)\prod_{j=1}^{m}\frac{\sin^{2}v_{j}}{v_{j}^{2}}dv_{1}\cdots dv_{m}=\phi_{T}(0)=1.\end{align*}
$$
 

在上述推导中我们用了单调收敛定理和控制收敛定理．这表明 $P_{T}(x)$为 $R^{m}$上一分布函数的密度函数．类似可证

 
$$
\int_{\mathbb{R}^{m}}e^{i t\cdot x}P_{T}(x)d x=\left(\frac{1}{\pi}\right)^{m}\int_{\mathbb{R}^{m}}\phi_{T}\Big(t-\frac{2v}{N}\Big)\prod_{j=1}^{m}\frac{\sin^{2}v_{j}}{v_{j}^{2}}d v_{1}\cdots d v_{m}=\phi_{T}(t).
$$
 

---

从而 $\phi_{T}(t)$为一特征函数.

下一定理是著名的Bochner定理,它给出了 $R^{m}$上有限Borel测度Fourier变换的一个刻画.

定理9.1.7 设f为 $R^{m}$上的有界复值连续函数，则f为有限Borel测度的Fourier变换，当且仅当f是非负定的.

证 只需证充分性. 不妨假定  $f(0)=1$ ，这时只需证 f 为特征函数. 令

 
$$
P_{T}(x)=\left(\frac{1}{2\pi T}\right)^{m}\int_{[0,T]^{2m}}f(u-v)e^{-i u\cdot x}e^{i v\cdot x}d u d v,\ x\in\mathbb{R}^{m}.
$$
 

将 $P_{T}(x)$视为Riemann和的极限，由f的非负定性知 $P_{T}(x)\geq0$。在上述多重积分中做如下变量代换： $u=u,v=u-t$，则变换Jacobi行列式为 $J=(a_{i,j})$，其中

 
$$
a_{i,j}=a_{i,j+m}=\delta_{i,j},\;a_{i+m,j}=0,\;a_{i+m,j+m}=-\delta_{i,j},\;1\leqslant i,j\leqslant m.
$$
 

于是有

 
$$
\begin{aligned}P_{T}(x)&=\left(-\frac{1}{2\pi T}\right)^{m}\int_{0}^{T}\cdots\int_{0}^{T}d u\int_{u_{m}}^{u_{m}-T}\cdots\int_{u_{1}}^{u_{1}-T}f(t)e^{-i t\cdot x}d t\\&=\left(\frac{1}{2\pi T}\right)^{m}\int_{0}^{T}\cdots\int_{0}^{T}d t\int_{t_{m}}^{T}\cdots\int_{t_{1}}^{T}f(t)e^{-i t\cdot x}d u\\&\quad+\left(\frac{1}{2\pi T}\right)^{m}\int_{-T}^{0}\cdots\int_{-T}^{0}d t\int_{0}^{T-|t_{m}|}\cdots\int_{0}^{T-|t_{1}|}f(t)e^{-i t\cdot x}d u\\&=\left(\frac{1}{2\pi}\right)^{m}\int_{-T}^{T}\cdots\int_{-T}^{T}e^{-i t\cdot x}\prod_{i=1}^{m}\left(1-\frac{|t_{j}|}{T}\right)f(t)d t\geqslant0.\\ \end{aligned}
$$
 

由引理9.1.6知， $\phi_{T}(t)=\prod_{j=1}^{m}\left(1-\frac{|t_{j}|}{T}\right)I_{[-T,T]^{m}}f(t)$为特征函数．由于 $\lim_{T\to\infty}\phi_{T}(t)=f(t),t\in\mathbb{R}^{m}$，且 $f$为一 $\mathbb{R}^{m}$上的复值连续函数，故由特征函数的连续性定理知 $f$为特征函数．

系9.1.8 设 $f$为 $\mathbb{R}^m$上的一复值连续函数，且 $f(0)=1$，则 $f$为特征函数，当且仅当 $f$是非负定的。

由定理9.1.7的证明我们得到 $R^{m}$上有限Borel测度Fourier变换的另一个刻画(属于Cramér).

定理9.1.9 设 $f$为 $\mathbb{R}^m$上的有界复值连续函数，则 $f$为有限Borel测度的Fourier变换，当且仅当对一切 $T > 0$，

 
$$
P_{T}(x)=\int_{[0,T]^{2m}}f(u-v)e^{i(u-v)\cdot x}d u d v\geqslant0,\quad x\in\mathbb{R}^{m}.
$$
 

---

## 9.2 测度的Fourier变换和Minlos-Sazanov定理

设H为一实可分Hilbert空间， $\mathcal{B}(H)$为它的Borel  $\sigma$代数．易知 $\mathcal{B}(H)$为可分 $\sigma$代数(即 $\mathcal{B}(H)$是可数生成的)．可测空间 $(H,\mathcal{B}(H))$上的测度称为H上的Borel测度．下面我们只讨论H上的有限Borel测度．

定义9.2.1 设 $\mu$为H上的一有限Borel测度. 令

 
$$
\widehat{\mu}(x)=\int_{H}e^{i(x,y)}\mu(d y),x\in H,
$$
 

称 $\hat{\mu}$为 $\mu$的Fourier变换.

显然， $\hat{\mu}$ 具有如下几条性质：

(1)  $\widehat{\mu}(0) = \mu(H);$

(2)  $\hat{\mu}$ 在 H 上连续 (甚至关于 H 的弱拓扑连续);

(3)  $\hat{\mu}$ 是非负定的.

自然要问：是否与有穷维欧氏空间情形类似，无穷维Hilbert空间上的任何非负定连续泛函都是某一有限Borel测度的Fourier变换？答案是否定的。下面我们将致力于给出Hilbert空间上有限Borel测度的Fourier变换的一个刻画(Minlos-Sazanov定理)。为此先证明若干引理。

引理9.2.2 设 $\varphi$为H上一非负定泛函. 则

(1)  $|\varphi(x)| \leqslant \varphi(0), \overline{\varphi(x)} = \varphi(-x), \forall x \in H;$

 
$$
|\varphi(x)-\varphi(y)|\leqslant2\sqrt{\varphi(0)}\sqrt{|\varphi(0)-\varphi(x-y)|},\ \forall x,y\in H;
$$
 

 
$$
|\varphi(0)-\varphi(x)|\leqslant\sqrt{2\varphi(0)(\varphi(0)-\operatorname{Re}\varphi(x))},\ \forall x\in H.
$$
 

证 设  $x, y \in H$. 令

 
$$
\begin{array}{r}{\boldsymbol{A}=\left(\begin{array}{l l}{\varphi(0)}&{\varphi(x)}\\ {\varphi(-x)}&{\varphi(0)}\end{array}\right),\quad\boldsymbol{B}=\left(\begin{array}{l l l}{\varphi(0)}&{\varphi(x)}&{\varphi(y)}\\ {\varphi(-x)}&{\varphi(0)}&{\varphi(y-x)}\\ {\varphi(-y)}&{\varphi(x-y)}&{\varphi(0)}\end{array}\right).}\end{array}
$$
 

由 $\varphi$的非负定性推知A和B为非负定矩阵. 特别有 $\overrightarrow{A^{T}}=A$, 这里 $A^{T}$表示A的转置. 故有 $\overline{\varphi(x)}=\varphi(-x)$. 此外由 $\det A\geq0$推知 $|\varphi(x)|\leq\varphi(0)$. (1)得证. 由(1)知, 矩阵B中的元素 $\varphi(-x)$,  $\varphi(-y)$及 $\varphi(y-x)$可用 $\overline{\varphi(x)},\overline{\varphi(y)}$及 $\overline{\varphi(x-y)}$替换. 计算B的行列式可得

 
$$
\begin{aligned}\det B&=\varphi(0)^{3}-\varphi(0)|\varphi(x-y)|^{2}-\varphi(x)[\varphi(0)\overline{\varphi(x)}-\overline{\varphi(x-y)}\varphi(y)]\\&\quad+\varphi(y)[\overline{\varphi(x)}\varphi(x-y)-\varphi(0)\overline{\varphi(y)}]\\&=\varphi(0)^{3}-\varphi(0)|\varphi(x-y)|^{2}-\varphi(0)|\varphi(x)-\varphi(y)|^{2}\\&\quad+2\mathrm{Re}[\varphi(y)\overline{\varphi(x)}(\varphi(x-y)-\varphi(0))].\end{aligned}
$$
 

---

因为

 
$$
\varphi(0)^{3}-\varphi(0)|\varphi(x-y)|^{2}\leqslant2\varphi(0)^{2}|\varphi(0)-\varphi(x-y)|,
$$
 

所以

 
$$
0\leqslant\det B\leqslant4\varphi(0)^{2}|\varphi(0)-\varphi(x-y)|-\varphi(0)|\varphi(x)-\varphi(y)|^{2},
$$
 

由此推得(2). (3)式可由如下不等式推出

 
$$
\begin{align*}|\varphi(0)-\varphi(x)|^{2}&=(\varphi(0)-\varphi(x))(\varphi(0)-\overline{\varphi(x)})\\&=\varphi(0)^{2}-2\varphi(0)\mathrm{Re}\varphi(x)+|\varphi(x)|^{2}\\&\leqslant2\varphi(0)^{2}-2\varphi(0)\mathrm{Re}\varphi(x).\end{align*}
$$
 

设A为H上线性算子，若 $(Ax,x)\geq0,(Ax,y)=(x,Ay),\forall x,y\in H$，则称A为非负对称算子。若进一步有 $(Ax,x)>0,\forall x\neq0$，则称A为正对称算子。设A为H上的一非负对称算子，令 $\{e_n\}$为H的一组标准正交基，则 $\mathrm{Tr}A:=\sum_n(Ae_n,e_n)$不依赖标准正交基的选取。若 $\mathrm{Tr}A<\infty$，则称A为对称迹算子，并称 $\mathrm{Tr}A$为A的迹。

设A为H上的非负对称迹算子，则存在H中的一个标准正交系 $\{e_{n}\}$及一列非负实数 $\{\lambda_{n}\}$，满足 $\sum_{n=1}^{\infty}\lambda_{n}<\infty$，使得 $Ae_{n}=\lambda_{n}e_{n}$，且有

$$
A x=\sum_{n}\lambda_{n}(x,e_{n})e_{n},\quad\forall x\in H.   \tag*{(9.2.1)}
$$

称(9.2.1)式为对称迹算子A的谱分解. 这时有 $\mathrm{Tr}A=\sum_{n=1}^{\infty}\lambda_{n}$

引理9.2.3 设 $\mu$为H上的有限Borel测度，则下列断言等价：

(1)  $\int_H \|x\|^2 \mu(dx) < \infty$;

(2) 存在一正对称迹算子 S，使得  $\forall x, y \in H$ 有

$$
(S x,y)=\int_{H}(x,z)(y,z)\mu(d z).   \tag*{(9.2.2)}
$$

如果(2)成立, 则

$$
\mathrm{T r}S=\int_{H}\|x\|^{2}\mu(d x).   \tag*{(9.2.3)}
$$

证 设(2)成立. 令 $\{e_{n}\}$为H的一组标准正交基, 则有

$$
\int_{H}\|x\|^{2}\mu(d x)=\sum_{j=1}^{\infty}\int_{H}(x,e_{j})^{2}\mu(d x)=\sum_{j=1}^{\infty}(S e_{j},e_{j})=\operatorname{T r}S.   \tag*{(9.2.4)}
$$

这表明(1)成立, 并有(9.2.3)式. 反之, 设(1)成立, 则

 
$$
\int_{H}|(x,z)(y,z)|\mu(d z)\leqslant\|x\|\|y\|\int_{H}\|z\|^{2}\mu(d z).
$$
 

---

于是存在H上一有界线性算子S，使得(9.2.2)式成立. 显然S是正的和对称的. 此外，由(9.2.4)式知

 
$$
\mathrm{Tr}S=\int_{H}\|x\|^{2}\mu(dx)<\infty.
$$
 

从而S是迹算子.

下一定理是Minlos-Sazanov定理,它给出了有限Borel测度的Fourier变换的一个刻画.

定理9.2.4 设 $\varphi$是H上的一正定泛函，则下列断言等价：

(1)  $\varphi$ 为 H 上某一有限 Borel 测度  $\mu$ 的 Fourier 变换；

(2) $\forall\varepsilon>0$, 存在对称运算子 $S_{\varepsilon}$, 使得

$$
(S_{\varepsilon}x,x)<1\Longrightarrow\operatorname{R e}(\varphi(0)-\varphi(x))<\varepsilon;   \tag*{(9.2.5)}
$$

(3) 存在H上对称迹算子S，使得 $\varphi$关于H的如下范数 $\|\cdot\|_{*}$连续(或只在x=0处连续):

$$
\|x\|_{*}=(S x,x)^{1/2}=\|S^{1/2}x\|.   \tag*{(9.2.6)}
$$

证 (1)  $\Longrightarrow(2)$. 设  $\varphi = \hat{\mu}$. 对一切  $\gamma > 0$, 我们有

 
$$
\begin{align*}\mathrm{Re}(\varphi(0)-\varphi(x))&=\int_{H}(1-\cos(x,z))\mu(dz)\\&\leqslant\frac{1}{2}\int_{\|z\|\leqslant\gamma}(x,z)^{2}\mu(dz)+2\mu(\{z\mid\|z\|>\gamma\}).\end{align*}
$$
 

令 $\mu_1(A) = \mu(A \cap [\|z\| \leqslant \gamma])$。对 $\mu_1$应用引理9.2.3知，存在一正的对称逆算子 $B_\gamma$使得

 
$$
(B_{\gamma}z_{1},z_{2})=\int_{\|z\|\leqslant\gamma}(z,z_{1})(z,z_{2})\mu(d z).
$$
 

对给定 $\varepsilon > 0$，先选取 $\gamma > 0$使得 $\mu([\|z\| > \gamma]) < \varepsilon/4$，再令 $S_{\varepsilon} = \varepsilon^{-1}B_{\gamma}$，则有

 
$$
\mathrm{R e}(\varphi(0)-\varphi(x))<\frac{\varepsilon}{2}(S_{\varepsilon}x,x)+\frac{\varepsilon}{2}.
$$
 

(2)  $\Longrightarrow$ (1). 设(2)成立，则  $\mathrm{Re}\varphi(x)$ 在 x = 0 处连续。故由引理9.2.2知  $\varphi$ 在 H 上连续。现在任意取定 H 上的一组标准正交基  $\{e_{n}\}$，并对每个自然数  $n \geqslant 1$，令

$$
f_{i_{1},\cdots,i_{n}}(\omega_{1},\cdots,\omega_{n})=\varphi(\omega_{1}e_{i_{1}}+\cdots+\omega_{n}e_{i_{n}}),\quad\omega_{j}\in\mathbb{R},\quad1\leqslant j\leqslant n,   \tag*{(9.2.7)}
$$

则 $f_{i_1},\ldots,i_n$为 $\mathbb{R}^n$上的一正定函数．由Bochner定理知， $f_{i_1},\ldots,i_n$为 $\mathbb{R}^n$上一有限Borel测度 $\mu_{i_1},\ldots,i_n$的Fourier变换．测度族 $\{\mu_{i_1},\ldots,i_n\}$满足Kolmogorov测度扩张定理的相容性条件．于是存在 $(\mathbb{R}^\infty,\mathcal{B}(\mathbb{R}^\infty))$上唯一的有限测度 $\nu$使得

$$
\mu_{i_{1},\dots,i_{n}}=\nu\circ(X_{i_{1}},\dots,X_{i_{n}})^{-1},   \tag*{(9.2.8)}
$$


---

其中 $X_j(\omega) = \omega_j$,  $\omega = (\omega_1, \omega_2, \cdots) \in \mathbb{R}^\infty$.

下面我们要证明 $\sum_{k=1}^{\infty}X_{k}^{2}<\infty,\nu\text{-a.e.}$为此，令 $P_{n}$为 $R^{n}$上标准Gauss测度.则

$$
\int_{\mathbb{R}^{n}}e^{i(a_{1}y_{1}+\cdots+a_{n}y_{n})}P_{n}(d y)=\exp\Big\{-\frac{1}{2}\sum_{j=1}^{n}a_{j}^{2}\Big\}.   \tag*{(9.2.9)}
$$

任给 $\varepsilon>0$，依据假定，存在正的对称迹算子 $S_{\varepsilon}$使(9.2.5)式成立。于是有

$$
\varphi(0)-\operatorname{R e}\varphi(x)\leqslant\varepsilon+2\varphi(0)(S_{\varepsilon}x,x),\quad\forall x\in H.   \tag*{(9.2.10)}
$$

由Fubini定理得

 
$$
\begin{aligned}&\varphi(0)-\int_{\mathbb{R}^{\infty}}\exp\Big\{-\frac{1}{2}\sum_{j=1}^{n}X_{k+j}^{2}\Big\}d\nu\\&=\varphi(0)-\int_{\mathbb{R}^{\infty}}d\nu\int_{\mathbb{R}^{n}}\exp\Big\{i\sum_{j=1}^{n}y_{j}X_{k+j}\Big\}\mathbb{P}_{n}(dy)\\&=\varphi(0)-\int_{\mathbb{R}^{n}}\varphi\Big(\sum_{j=1}^{n}y_{j}e_{k+j}\Big)\mathbb{P}_{n}(dy)\\&=\int_{\mathbb{R}^{n}}\Big[\varphi(0)-\operatorname{Re}\varphi\Big(\sum_{j=1}^{n}y_{j}e_{k+j}\Big)\Big]\mathbb{P}_{n}(dy),\\ \end{aligned}
$$
 

由9.2.10式, 上式不超过

 
$$
\begin{aligned}&\varepsilon+2\varphi(0)\int_{\mathbb{R}^{n}}\left(S_{\varepsilon}\sum_{j=1}^{n}y_{j}e_{k+j},\sum_{j=1}^{n}y_{j}e_{k+j}\right)\mathbb{P}_{n}(d y)\\&=\varepsilon+2\varphi(0)\sum_{j=1}^{n}(S_{\varepsilon}e_{k+j},e_{k+j}).\\ \end{aligned}
$$
 

由于 $n \geqslant 1$是任意的，故由上式推知

$$
\varphi(0)-\int_{\mathbb{R}^{\infty}}\exp\Big\{-\frac{1}{2}\sum_{j=k+1}^{\infty}X_{j}^{2}\Big\}d\nu\leqslant\varepsilon+2\varphi(0)\sum_{j=k+1}^{\infty}(S_{\varepsilon}e_{j},e_{j}).   \tag*{(9.2.11)}
$$

在(9.2.11)中先令 $k \to \infty$再令 $\varepsilon \downarrow 0$即得(注意 $\varphi(0) = \nu(\mathbb{R}^{\infty})$)

 
$$
\varphi(0)-\lim_{k\to\infty}\int_{\mathbb{R}^{\infty}}\exp\Big\{-\frac{1}{2}\sum_{i=k+1}^{\infty}X_{j}^{2}\Big\}d\nu=0,
$$
 

这表明 $\sum_{j=1}^{\infty}X_{j}^{2}<\infty,\nu-\mathrm{a.e.}$

---

最后，令 $X(\omega)=\sum_{j=1}^{\infty}X_{j}(\omega)e_{j}$，则X在 $\mathbb{R}^{\infty}$上 $\nu$-a.e.有定义，且X为H-值可测函数。令 $\mu=\nu\circ X^{-1}$，则 $\mu$为H上的有限Borel测度，且由(9.2.8)式知

 
$$
\begin{align*}\widehat{\mu}\Big(\sum_{j=1}^{n}(x,e_{j})e_{j}\Big)&=f_{1,\cdots,n}((x,e_{1}),\cdots,(x,e_{n}))\\&=\varphi\Big(\sum_{j=1}^{n}(x,e_{j})e_{j}\Big).\end{align*}
$$
 

令 $n\to\infty$即得 $\hat{\mu}=\varphi.$ (2) $\Longrightarrow(1)$证毕.

(2)  $\Longleftrightarrow$ (3). 设(2)成立. 令  $S_{1/k}$ 为与  $\varepsilon = 1/k$ 相应的正的对称迹算子, 选取  $\lambda_{k} > 0$, 使得  $\sum_{k} \lambda_{k} \operatorname{Tr} S_{1/k} < \infty$. 令  $S = \sum_{k} \lambda_{k} S_{1/k}$, 则 S 为正的对称迹算子. 显然有

 
$$
\begin{align*}(Sx,x)<\lambda_{k}&\Longrightarrow(S_{1/k}x,x)<1\\&\Longrightarrow\mathrm{Re}(\varphi(0)-\varphi(x))<\frac{1}{k}.\end{align*}
$$
 

于是Reφ(x)在x = 0处关于范数∥·∥*连续，从而由引理9.2.2知，φ在H上关于范数∥·∥*连续.这表明(2)⇒(3).反之，设(3)成立.对给定ε > 0，存在δ > 0，使得∥∥* < δ ⇒ Re(φ(0) - φ(x)) < ε.令Sε = δ⁻¹S，则(9.2.5)式成立.从而(3)⇒(2)得证.

## 9.3 Minlos 定理

下面我们将给出Minlos-Sazanov定理的一个更加常用形式——Minlos定理．为此，先引进若干记号和准备一些引理.

设B为H上一正对称可逆运算子. 在H上引进新的内积 $\left(\cdot,\cdot\right)$ 及范数 $\|\cdot\|_{\text{如下}}$

 
$$
(x,y)_{-}=(B x,y),\qquad\|x\|_{-}=(B x,x)^{1/2}=\|B^{1/2}x\|.
$$
 

我们用 $H_{-}$表示 $H$关于 $\|\cdot\|_{-}$的完备化，则内积 $(\cdot,\cdot)_-$可以连续扩张到 $H_-$，且 $H_-$关于 $(\cdot,\cdot)_-$为一可分Hilbert空间。另一方面，令 $H_+$表示 $B^{-1/2}$的定义域，则 $H_+$为 $B^{1/2}$的值域（即 $H_+$ =  $B^{1/2}(H)$）。在 $H_+$上引进内积 $(\cdot,\cdot)_+$及范数 $\|\cdot\|_{+}$如下：

$$
(x,y)_{+}=(B^{-1/2}x,B^{-1/2}y),\quad\|x\|_{+}=\|B^{-1/2}x\|,\quad x,y\in H_{+},   \tag*{(9.3.1)}
$$

则显然有

$$
\|B x\|_{+}=\|x\|_{-},\quad x\in H,   \tag*{(9.3.2)}
$$

$$
\|B^{-1}x\|_{-}=\|x\|_{+},\quad x\in B(H),   \tag*{(9.3.3)}
$$


---


$$
\|x\|\leqslant\|B\|^{1/2}\|x\|_{+},\quad x\in H_{+}.   \tag*{(9.3.4)}
$$

关于空间 $H_{-}$及 $H_{+}$，我们有如下结果：

引理9.3.1 在上述假定及记号下, 我们有

(1) $H_{+}$按内积 $(\cdot,\cdot)_{+}$为一可分Hilbert空间;

(2) B可延拓成为 $H_{-}$到 $H_{+}$上的保范算子， $B^{-1}$可延拓成为 $H_{+}$到 $H_{-}$上的保范算子；

(3) 作为 $H_{-}$中的线性算子，B是正的对称迹算子，并且有 $Tr_{B}=Tr_{-}B$．这里 $Tr_{-}B$表示在 $H_{-}$中计算B的迹；

(4)  $H_{+}$与 $H_{-}$互为对偶， $H_{+} \times H_{-}$上的典则双线性型 $\langle\cdot,\cdot\rangle$为

$$
\langle x,y\rangle=(B^{-1}x,y)_{-},\quad x\in H_{+},y\in H_{-}.   \tag*{(9.3.5)}
$$

证 设 $\{x_{n}\}$为 $H_{+}$中按范数 $\|\cdot\|_{+}$的基本列. 由(9.3.4)式知, $\{x_{n}\}$亦为H中的基本列, 记其极限为x. 令 $y_{n}=B^{-1/2}x_{n}$, 则 $\{y_{n}\}$为H中的基本列, 其极限为y. 于是有

 
$$
x=\lim_{n\to\infty}x_{n}=\lim_{n\to\infty}B^{1/2}y_{n}=B^{1/2}y.
$$
 

这表明 $x\in H_{+}$，且有

 
$$
\|x_{n}-x\|_{+}=\|B^{-1/2}(x_{n}-x)\|=\|y_{n}-y\|\to0.
$$
 

于是， $H_{+}$按范数 $\|\cdot\|_{+}$是完备的，即 $H_{+}$按内积 $(\cdot,\cdot)_{+}$为Hilbert空间。(1)得证.

(2) 直接由(9.3.2)式及(9.3.3)式推得.

下面证(3). 作为 $H_{-}$上的线性算子, B的正性及对称性容易验证. 往证B是 $H_{-}$上的迹算子. 设B在H上的谱分解为

 
$$
B x=\sum_{n}\lambda_{n}(x,e_{n})e_{n},\quad x\in H.
$$
 

由于假定B可逆， $\{e_{n}\}$构成H的一组基。令 $f_{n}=e_{n}/\sqrt{\lambda_{n}}$，则

 
$$
(B f_{n},f_{m})=(\lambda_{n}\lambda_{m})^{-1/2}(B e_{n},e_{m})=\delta_{n,m}.
$$
 

故 $\{f_{n}\}$为 $H_{-}$的一组基.我们有

 
$$
\mathrm{Tr}_{-}B=\sum_{n=1}^{\infty}(B f_{n},f_{n})_{-}=\sum_{n=1}^{\infty}\left\|B f_{n}\right\|^{2}=\sum_{n=1}^{\infty}\lambda_{n}=\mathrm{Tr}B.
$$
 

往证(4). 由(2)知(9.3.5)式定义的双线性型 $\langle\cdot,\cdot\rangle$有意义, 此外有

 
$$
|\langle x,y\rangle|\leqslant\|B^{-1}x\|_{-}\|y\|_{-}=\|x\|_{+}\|y\|_{-}.
$$
 

---

这表明 $\langle\cdot,\cdot\rangle$为使 $H_{+}$和 $H_{-}$相互对偶的典则双线性型.

有了上面的准备以后, 我们可以证明如下的Minlos定理.

定理9.3.2 设φ为H上一连续正定泛函，B为H上一正对称可逆迹算子，H_如前面所定义. 则存在H_上唯一的有限Borel测度μ，使得

$$
\int_{H_{-}}e^{i\langle x,z\rangle}\mu(d z)=\varphi(x),\quad\forall x\in H_{+}\;.   \tag*{(9.3.6)}
$$

证 对  $x \in H_{-}$，令  $\psi(x) = \varphi(Bx)$。则显然  $\psi$ 为  $H_{-}$ 上的正定泛函。由引理9.2.1知， $B$ 为  $H_{-}$ 上的正的对称可逆迹算子。在  $H_{-}$ 上定义新范数  $\|\cdot\|_{*}$ 如下：

 
$$
\|x\|_{*}=\|B^{1/2}x\|_{-}=\|B x\|.
$$
 

由φ在H上连续性推知ψ在H_上关于范数∥·∥*的连续性. 故由定理9.2.4知ψ为H_上某一有限Borel测度μ的Fourier变换, 即有

$$
\int_{H_{-}}e^{i(y,z)-}\mu(d z)=\psi(y),\quad\forall y\in H_{-}.   \tag*{(9.3.7)}
$$

在(9.3.7)式中令 $y = B^{-1}x, x \in H_{+}$，则由(9.3.5)式推得(9.3.6)式.

## 9.4 Hilbert空间上的Gauss测度

下面我们研究H上的一类特殊的Borel概率测度——Gauss测度. 首先, 我们对H上一般的Borel概率测度引进均值向量和协方差算子概念.

定义9.4.1 设μ为H上的一Borel概率测度. 如果对一切 $x\in H$，函数 $z\mapsto(x,z)$关于 $\mu$可积，且存在H的一元素m，使得

$$
(m,x)=\int_{H}(x,z)\mu(d z),\quad x\in H,   \tag*{(9.4.1)}
$$

则称 $m$为 $\mu$的均值向量。如果进一步存在 $H$上的一正的对称线性算子 $B$，使得

$$
(B x,y)=\int_{H}(z-m,x)(z-m,y)\mu(d z),\quad\forall x,y\in H,   \tag*{(9.4.2)}
$$

则称B为 $\mu$的协方差算子.

均值向量和协方差算子一般未必存在. 但若  $\int_{H}\|x\|\mu(dx)<\infty$, 则由Riesz表示定理知均值向量m存在, 且  $\|m\|\leq\int_{H}\|x\|\mu(dx)$. 如果进一步有  $\int_{H}\|x\|^{2}\mu(dx)<\infty$, 则由引理9.2.3知, 存在一正的对称迹算子S, 使得

$$
(S x,y)=\int_{H}(x,z)(y,z)\mu(d z),\quad\forall x,y\in H.   \tag*{(9.4.3)}
$$


---

令

$$
Bx=Sx-(m,x)m\;.   \tag*{(9.4.4)}
$$

容易验证B满足(9.4.2)式，即B为μ的协方差算子．这时B亦为正对称迹算子．

定义9.4.2 设μ为H上的一Borel概率测度. 如果对每个 $x \in H$，随机变量 $(x,\cdot)$服从Gauss分布，则称μ为Gauss测度.

下面我们将通过Fourier变换来刻画Gauss测度. 为此, 我们需要一个分析引理.

引理9.4.3 设 $\{\alpha_{j}\}$为一列实数，满足 $\sum_{j=1}^{\infty}\alpha_{j}^{2}=\infty$。则存在一列实数 $\{\beta_{j}\}$，使得 $\alpha_{j}\beta_{j}\geq0,\forall j\geq1,\sum_{j=1}^{\infty}\beta_{j}^{2}<\infty$且 $\sum_{j=1}^{\infty}\alpha_{j}\beta_{j}=\infty$。

证明 令 $n_{0}=0$，并归纳定义 $n_{k}$如下：

 
$$
n_{k}=\inf\left\{l\mid\sum_{j=n_{k-1}+1}^{l}\alpha_{j}^{2}\geqslant1\right\},\quad k\geqslant1.
$$
 

显然有 $n_{k}\uparrow\infty$. 令

 
$$
\beta_{j}=\frac{\alpha_{j}}{k+1}\Big(\sum_{j=n_{k}+1}^{n_{k+1}}\alpha_{j}^{2}\Big)^{-1/2},n_{k}+1\leqslant j\leqslant n_{k+1},\quad k=0,1,2,\cdots
$$
 

则 $\alpha_{j}\beta_{j}\geqslant0,\forall j\geqslant1$，且有

 
$$
\sum_{j=1}^{\infty}\beta_{j}^{2}=\sum_{k=0}^{\infty}\sum_{j=n_{k}+1}^{n_{k+1}}\beta_{j}^{2}=\sum_{k=0}^{\infty}\frac{1}{(k+1)^{2}}<\infty,
$$
 

 
$$
\begin{align*}\sum_{j=1}^{\infty}\alpha_{j}\beta_{j}&=\sum_{k=0}^{\infty}\sum_{j=n_{k}+1}^{n_{k+1}}\alpha_{j}\beta_{j}=\sum_{k=0}^{\infty}\frac{1}{k+1}\bigg(\sum_{j=n_{k}+1}^{n_{k+1}}\alpha_{j}^{2}\bigg)^{1/2}\\&\geqslant\sum_{k=0}^{\infty}\frac{1}{k+1}=\infty.\end{align*}
$$
 

下一定理给出了Gauss测度的一个刻画.

定理9.4.4 H上的Borel概率测度 $\mu$是Gauss测度的必要充分条件,是其Fourier变换 $\hat{\mu}$有如下表达式:

$$
\widehat{\mu}(x)=\exp\{i(m,x)-\frac{1}{2}(B x,x)\},   \tag*{(9.4.5)}
$$

其中 $m \in H$，B为H上的一正的对称迹算子。这时， $m$为 $\mu$的均值向量，B为 $\mu$的协方差算子。此外还有

$$
\int_{H}\|x\|^{2}\mu(d x)=\mathrm{T r}B+\|m\|^{2}.   \tag*{(9.4.6)}
$$


---

证 必要性. 设  $\mu$ 为一 Gauss 测度. 先证  $\int_{H} \|x\|^2 \mu(dx) < \infty$. 依假定, 对每个  $x$,  $(x, \cdot)$ 服从 Gauss 分布, 于是存在实数  $m_x$ 及正数  $\sigma_x$, 使得

$$
\widehat{\mu}(x)=\int_{H}e^{i(x,z)}\mu(d z)=\exp\{i m_{x}-\frac{1}{2}\sigma_{x}^{2}\}\;.   \tag*{(9.4.7)}
$$

令 $\{e_{j}\}$为H的标准正交基，则

$$
\int_{H}\|x\|^{2}\mu(d x)=\sum_{j=1}^{\infty}\int_{H}(e_{j},x)^{2}\mu(d x)=\sum_{j=1}^{\infty}(\sigma_{e_{j}}^{2}+m_{e_{j}}^{2}).   \tag*{(9.4.8)}
$$

设 $\{\beta_{j}\}$为一列实数，使得

 
$$
\forall j\geqslant1,\beta_{j}m_{e_{j}}\geqslant0,\sum_{j=1}^{\infty}\beta_{j}^{2}<\infty.
$$
 

定义

$$
\xi(x)=\sum_{j=1}^{\infty}\beta_{j}(e_{j},x),   \tag*{(9.4.9)}
$$

则$\xi$为一Gauss随机变量(因由Schwarz不等式，上述级数绝对收敛)，其均值必有限，即$\sum_{j=1}^{\infty}\beta_{j}m_{e_{j}}<\infty$。于是由引理9.4.3知，必有$\sum_{j=1}^{\infty}m_{e_{j}}^{2}<\infty$。为证$\int_{H}\|x\|^{2}\mu(dx)<\infty$，只需证$\sum_{j=1}^{\infty}\sigma_{e_{j}}^{2}<\infty$。由定理9.2.4知，存在正的对称迹算子$S$，使得$(Sx,x)<1\implies1-\operatorname{Re}\widehat{\mu}(x)<1/3$。于是我们有

$$
1-\exp\{-\frac{1}{2}\sigma_{x}^{2}\}\leqslant1-\operatorname{R e}\widehat{\mu}(x)\leqslant(S x,x)+\frac{1}{3},\forall x\in H.   \tag*{(9.4.10)}
$$

不妨设S的零空间为{0}. 对 $x\in H,x\neq0,$ 令 $y=[3(Sx,x)]^{-1/2}x,$ 则 $\sigma_{y}^{2}=[3(Sx,x)]^{-1}$  $\sigma_{x}^{2},(Sy,y)=1/3$ . 用y代替(9.4.10)中的x,得到

 
$$
1-\exp\left\{-\frac{\sigma_{x}^{2}}{6(S x,x)}\right\}\leqslant\frac{2}{3},
$$
 

即有 $\sigma_{x}^{2}\leqslant(6\log3)(Sx,x),\forall x\in H.$由此推知

 
$$
\sum_{j=1}^{\infty}\sigma_{e_{j}}^{2}\leqslant(6\log3)\mathrm{T r}S<\infty.
$$
 

因此, 最终证明了  $\int_H \|x\|^2 \mu(dx) < \infty$. 由定义9.4.1下面的说明知,  $\mu$ 的均值向量  $m$ 及协方差算子  $B$ 存在. 采用前面的记号, 我们有

 
$$
m_{x}=\int_{H}(x,z)\mu(d z)=(m,x),
$$
 

---

 
$$
\begin{align*}\sigma_{x}^{2}&=\int_{H}(x,z)^{2}\mu(dz)-m_{x}^{2}=\int_{H}[(x,z)^{2}-(m,x)^{2}]\mu(dz)\\&=\int_{H}(x,z-m)^{2}\mu(dz)=(Bx,x).\end{align*}
$$
 

故由 $(9.4.7)$式推得 $(9.4.5)$式，由 $(9.4.8)$式推得 $(9.4.6)$式.

充分性. 设  $m \in H$,  $B$ 为  $H$ 上的一正的对称迹算子,

 
$$
\varphi(x)=\exp\{i(m,x)-\frac{1}{2}(B x,x)\},
$$
 

则容易验证 $\varphi$是H上的正定泛函. 令

 
$$
Sx=Bx+(m,x)m,
$$
 

则S为H上正对称迹算子. 在H上定义范数 $\|\cdot\|_{*}$如下:

 
$$
\|x\|_{*}=\|S^{1/2}x\|=\left((B x,x)+(m,x)^{2}\right)^{1/2}.
$$
 

显然 $\varphi(x)$在 $x = 0$处关于范数 $\|\cdot\|_{*}$连续，故由定理9.2.4知 $\varphi$为 $H$上某一Borel概率测度 $\mu$的Fourier变换。显然在测度 $\mu$下，对一切 $x \in H$， $(x,\cdot)$服从均值为 $(m,x)$、方差为 $(Bx,x)$的Gauss分布。于是，依定义 $\mu$为Gauss测度。

## 9.5 Banach空间上的Gauss测度

现在我们转向研究Banach空间上的Gauss测度. 首先引进柱集及柱测度等基本概念.

设X为一实可分Banach空间， $X^*$为其对偶空间。令 $\|\cdot\|$和 $\|\cdot\|_{X^*}$分别表示X和 $X^*$上的范数，并用 $\langle\cdot,\cdot\rangle$表示 $X \times X^*$上的典则双线性型。令 $\mathcal{F}(X^*)$表示 $X^*$的有限维线性子空间的全体。令 $K \in \mathcal{F}(X^*)$， $E$为 $\mathbb{R}^n$的Borel子集，我们称形如

$$
C=\{x\in X\mid(\langle x,y_{1}\rangle,\cdots,\langle x,y_{n}\rangle)\in E\}   \tag*{(9.5.1)}
$$

的集为以K为底的柱集，这里 $n \geqslant 1, y_{1}, \cdots, y_{n} \in K$。我们用 $C(K)$表示由以K为底的柱集在X上生成的 $\sigma$代数。令

$$
\mathcal{R}(X)=\bigcup_{K\in\mathcal{F}(X^{*})}\mathcal{C}(K),   \tag*{(9.5.2)}
$$

则 $R(X)$为代数.

引理9.5.1 设X为一实可分Banach空间，则 $\sigma(\mathcal{R}(X))=\mathcal{B}(X)$。这里 $\mathcal{B}(X)$为X的Borel $\sigma$代数。

---

证 首先, 显然有  $\sigma(\mathcal{R}(X)) \subset \mathcal{B}(X)$. 由于 X 为可分距离空间. 每个开集可表示为可数个闭球的并. 因此, 为证  $\sigma(\mathcal{R}(X)) = \mathcal{B}(X)$, 只需证每个闭球属于  $\sigma(\mathcal{R}(X))$. 设  $S = \{x \mid \|x - x_0\| \leqslant r\}$, 其中  $x_0 \in X, r > 0$. 令  $\{a_n\}$ 为 X 的可数稠子集. 由 Hahn-Banach 定理, 对每个  $n \geqslant 1$, 存在  $z_n \in X^*$, 使得  $\|z_n\|_X^* = 1, \langle a_n, z_n \rangle = \|a_n\|$. 令

 
$$
T=\bigcap_{n=1}^{\infty}\left\{x\in X\mid\left|\langle x-x_{0},z_{n}\rangle\right|\leqslant r\right\}.
$$
 

显然 $S \subset T, T \in \sigma(\mathcal{R}(X))$。往证 $S = T$。如果 $x \notin S$，即 $\|x - x_0\| = r_1 > r$，则存在某个 $n$，使得 $\|x - x_0 - a_n\| < (r_1 - r)/2$。这时必有 $\|a_n\| > (r_1 + r)/2$，且有

 
$$
\begin{align*}|\langle x-x_{0},z_{n}\rangle|&\geqslant|\langle a_{n},z_{n}\rangle|-|\langle x-x_{0}-a_{n},z_{n}\rangle|\\&\geqslant\|a_{n}\|-\|x-x_{0}-a_{n}\|>r.\end{align*}
$$
 

这表明 $x \notin T$。于是 $T \subset S$。最终有 $S = T \in \sigma(\mathcal{R}(X))$。

定义9.5.2 设μ为R(X)上的非负集函数. 如果μ(X)=1, 且对一切K∈F(X*), μ限于σ-代数C(K)为一测度, 则称μ为X上的柱(概率)测度. X上的复值函数f, 如果存在某个K∈F(X*), 使得f关于C(K)为可测, 则f称为柱函数.

有界柱函数$f$关于柱测度$\mu$的积分是有意义的, 只要把柱测度看成使$f$可测的$\sigma$-代数$\mathcal{C}(K)$上的测度. 我们用$\int_{X}f(x)\mu(dx)$表示这一积分. 特别, 对柱测度$\mu$, 令

$$
\widehat{\mu}(z)=\int_{X}e^{i\langle x,z\rangle}\mu(d x),\ z\in X^{*},   \tag*{(9.5.3)}
$$

称 $\hat{\mu}$为 $\mu$的特征泛函.

显然, 柱测度的特征泛函是  $X^{*}$ 上的连续正定泛函. 反之, 设  $\varphi$ 为  $X^{*}$ 上的连续正定泛函, 且  $\varphi(0) = 1$, 则存在唯一的柱测度  $\mu$, 使得  $\varphi$ 为  $\mu$ 的特征泛函.

一个自然的问题是：什么样的柱测度可以扩张成为X上的一Borel测度？下面我们将对一种特殊情形回答这一问题. 这一特殊情形是：Banach空间X是某个实可分Hilbert空间H关于某个较弱范数的完备化，而X上的柱测度是由H上的某个柱测度“提升”得到的.

设H为一实可分Hilbert空间。我们用 $(\cdot,\cdot)$及 $|\cdot|$分别表示H中的内积及范数。设 $\|\cdot\|$为H上的另一范数，满足如下条件：存在一常数 $c > 0$，使得 $\|x\| \leqslant c|x|$。这时称范数 $\|\cdot\|$比范数 $|\cdot|$弱。令X为H关于范数 $\|\cdot\|$的完备化，则X为一可分Banach空间，H可视为X的一线性子空间。如果将H的对偶 $H^*$与H等同，则X的对偶空间 $X^*$可以视为H的如下子集：

$$
X^{*}=\left\{y\in H\mid\sup_{x\in H,\|x\|=1}\left|(x,y)\right|<\infty\right\}.   \tag*{(9.5.4)}
$$


---

我们用 $\langle\cdot,\cdot\rangle$ 表示 $X \times X^*$上的典则双线性型，则  $\langle\cdot,\cdot\rangle$ 在 $H \times X^*$上与内积 $(\cdot,\cdot)$ 吻合，即有

$$
\langle x,y\rangle=(x,y)\;,\quad\forall x\in H,\;y\in X^{*}.   \tag*{(9.5.5)}
$$

我们用$\mathcal{F}(X^*)$及$\mathcal{F}(H)$分别表示$X^*$及$H$的有限维子空间全体。由于$\mathcal{F}(X^*) \subset \mathcal{F}(H)$，且对每个$K \in \mathcal{F}(X^*)$，若以$\mathcal{C}_X(K)$及$\mathcal{C}_H(K)$分别表示以$K$为底的柱集在$X$及$H$上生成的$\sigma$代数，则$\mathcal{C}_X(K) \cap H \subset \mathcal{C}_H(K)$。因此，我们有$\mathcal{R}(X) \cap H \subset \mathcal{R}(H)$。这样一来，对$H$上的每个柱测度$\mu$，我们可以定义$X$上的一柱测度$\mu^*$如下：

$$
\mu^{*}(C)=\mu(C\cap H),\quad C\in\mathcal{R}(X),   \tag*{(9.5.6)}
$$

我们称 $\mu^*$为 $\mu$到 $X$上的提升。显然，对 $x \in X^*$，我们有 $\widehat{\mu^*}(x) = \widehat{\mu}(x)$。这表明 $\mu^*$的特征泛函是 $\mu$的特征泛函在 $X^*$上的限制。今后我们用 $(H, X, \mu)$表示上面引进的Hilbert空间、Banach空间及 $H$上的柱测度，并称它为基本三元组。在回答前面提出的问题之前，我们还需要引进可测范数概念，它是Gross (1965) 最早提出的。

下面我们用$\mathcal{P}$表示$H$中有限维(正交)投影算子全体. 对$\mathbb{P}\in\mathcal{P}$, 令$f(x)=\|\mathbb{P}x\|$, $x\in H$, 则$f$是$H$上的柱函数.

定义9.5.3 设 $(H,|\cdot|)$为一Hilbert空间， $\mu$为H上的柱测度， $\|\cdot\|$为H上的另一范数，且比范数 $|\cdot|$弱。如果对于每个 $\varepsilon > 0$，存在 $P_\varepsilon \in \mathcal{P}$，使得对任何与 $P_\varepsilon$正交的 $P \in \mathcal{P}$有

 
$$
\mu\{x\in H\mid\left\|{\mathbb{I}P x}\right\|>\varepsilon\}<\varepsilon,
$$
 

则称 $\|\cdot\|$关于 $\mu$可测.

定义9.5.4 设μ为H上的柱测度. 如果 $\hat{\mu}(x)=\exp\{-\frac{1}{2}|x|^{2}\}$，则称μ为H上的(标准)Gauss柱测度.

显然,  $\mu$ 为 Gauss 柱测度, 当且仅当  $\forall P \in \mathcal{P}, \mu \circ P^{-1}$ 为  $\mathbb{P}(H)$ 上的 Gauss 测度.

下一定理是著名的Gross定理(见Gross (1965)). 下面的简化证明是Kallianpur (1971) 中给出的.

定理9.5.5 设 $(H, X, \mu)$为基本三元组. 如果 $\mu$是Gauss柱测度, 且范数 $\|\cdot\|$为 $\mu$可测, 则 $\mu$到X上的提升 $\mu^*$可以扩张成为X上的Borel测度, 称它为X上的Gauss测度.

证 令$\{\xi_n\}$为某个概率空间$(\Omega, \mathcal{F}, \lambda)$上的一列相互独立的标准正态随机变量。由范数$\|\cdot\|$的$\mu$可测性，存在$H$的一列有限维正交投影$\{P_n\}$，使得$P_n \uparrow I(I$为恒等算子)且对任何与$P_n$正交的$P \in \mathcal{P}$有

 
$$
\mu\{x\in H\mid\|P x\|>2^{-n}<2^{-n}.
$$
 

我们可以选H的一组标准正交基 $\{e_{n}\}$，使得 $\{e_{1},\cdots,e_{n_{k}}\}$为 $\mathbb{P}_{k}(H)$的标准正交基。令

 
$$
\eta_{k}(\omega)=\sum_{j=1}^{n_{k}}\xi_{j}(\omega)e_{j},
$$
 

---

则我们有

 
$$
\eta_{k+1}-\eta_{k}=\sum_{j=n_{k}+1}^{n_{k+1}}\xi_{j}(\omega)e_{j}.
$$
 

由于 $IP_{k+1}x - IP_{k}x = \sum_{j=n_{k}+1}^{n_{k}+1}(x, e_{j})e_{j}$，且 $\forall E \in \mathcal{B}(\mathbb{R}^{n_{k}+1-n_{k}})$，

 
$$
\begin{aligned}&\lambda\{\omega\mid(\xi_{n_{k}+1}(\omega),\cdots,\xi_{n_{k+1}}(\omega))\in E\}\\&=\mu\{x\in H\mid\left((e_{n_{k}+1},x),\cdots,(e_{n_{k+1}},x)\right)\in E\},\\ \end{aligned}
$$
 

于是有

 
$$
\lambda(\|\eta_{k+1}-\eta_{k}\|>2^{-k})=\mu\{x\in H\mid\|\mathbb{P}_{k+1}x-\mathbb{P}_{k}x\|>2^{-k}\}<2^{-k}.
$$
 

因此， $\{\eta_k\}$ 依概率收敛于一X值随机元 $\eta$。令 $\nu$为 $\eta$的分布，即 $\nu = \lambda \circ \eta^{-1}$，则对每个 $z \in X^*$，

 
$$
\begin{align*}\widehat{\nu}(z)&=\int_{X}e^{i\langle x,z\rangle}\nu(dx)=\int_{\Omega}e^{i\langle\eta(\omega),z\rangle}\lambda(d\omega)\\&=\lim_{k\to\infty}\int_{\Omega}\exp\Big\{i\langle\sum_{j=1}^{n_{k}}\xi_{j}(\omega)e_{j},z\rangle\Big\}\lambda(d\omega)\\&=\lim_{k\to\infty}\prod_{j=1}^{n_{k}}e^{-\langle e_{j},z\rangle^{2}/2}=e^{-|z|^{2}/2}=\widehat{\mu}^{*}(z).\end{align*}
$$
 

这表明 $\mu^{*}$与 $\nu$在 $\mathcal{R}(X)$上一致，即 $\nu$为 $\mu^{*}$的扩张。

定义9.5.6 设X为一实可分Banach空间， $\mu$为X上的Borel概率测度，如果对一切 $z \in X^*$， $\langle\cdot, z\rangle$为X上的零均值正态随机变量，则称 $\mu$为X上的对称Gauss测度。这时称 $(X, \mathcal{B}(X), \mu)$为Gauss测度空间。

设 $(X, \mathcal{B}(X), \mu)$为一Gauss测度空间． $H$为一Hilbert空间，它在 $X$中稠， $X$的范数 $\|\cdot\|$限于 $H$比 $H$的Hilbert范数 $|\cdot|$弱，这时将 $H$的对偶空间与 $H$等同，则 $X$的对偶空间 $X^*$可视为 $H$的子集．若 $\mu$的特征泛函 $\widehat{\mu}(z) = \exp\{-\frac{1}{2}|z|^2\}$， $z \in X^*$，则称三元组 $(H, X, \mu)$为抽象Wiener空间．

最后, 我们以有关Banach空间上对称Gauss测度的Fernique定理结束这一节.

定理9.5.7 设E为一实可分Banach空间, $\mu$为 $(E,\mathcal{B}(E))$上的对称Gauss测度.则存在 $\lambda>0$,使得

$$
\int_{E}e^{\lambda\|x\|^{2}}\mu(d x)<\infty.   \tag*{(9.5.7)}
$$

证 设X,Y为某个概率空间( $\Omega,\mathcal{F},\mathbb{P}$)上的两个独立E值随机元,其分布都是 $\mu$.

令

 
$$
\widetilde{X}=\frac{1}{\sqrt{2}}(X+Y),\quad\widetilde{Y}=\frac{1}{\sqrt{2}}(X-Y).
$$
 

---

容易看出， $\tilde{X}$ 与  $\tilde{Y}$ 相互独立，且其分布仍为  $\mu$。设  $t \geq s \geq 0$，则有

$$
\begin{aligned}&\mathbb{P}(\|X\|\leqslant s)\mathbb{P}(\|X\|>t)\\=&\mathbb{P}(\|\widetilde{Y}\|\leqslant s)\mathbb{P}(\|\widetilde{X}\|>t)\\=&\mathbb{P}\left(\frac{\|X-Y\|}{\sqrt{2}}\leqslant s\right)\mathbb{P}\left(\frac{\|X+Y\|}{\sqrt{2}}>t\right)\\=&\mathbb{P}\left(\frac{\|X-Y\|}{\sqrt{2}}\leqslant s,\frac{\|X+Y\|}{\sqrt{2}}>t\right)\\\leqslant&\mathbb{P}(\mid\|X\|-\|Y\|\mid\leqslant\sqrt{2}s,\|X\|+\|Y\|>\sqrt{2}t)\\\leqslant&\mathbb{P}\left(\|X\|>\frac{t-s}{\sqrt{2}},\|Y\|>\frac{t-s}{\sqrt{2}}\right)\\=&\left[\mathbb{P}\left(\|X\|>\frac{t-s}{\sqrt{2}}\right)\right]^{2}.\end{aligned}   \tag*{(9.5.8)}
$$

固定r>0. 令 $t_{0}=r,\quad t_{n+1}=r+\sqrt{2}t_{n},n\geqslant1,$ 定义

 
$$
\alpha_{n}(r)=\frac{\mathbb{P}(\|X\|>t_{n})}{\mathbb{P}(\|X\|\leqslant r)},\quad n=0,1,2,\cdots,
$$
 

则由 $(9.5.8)$式得到

 
$$
\begin{align*}\alpha_{n+1}(r)&=\frac{\mathbb{P}(\|X\|>r+\sqrt{2}t_{n})}{\mathbb{P}(\|X\|\leqslant r)}\\&\leqslant\left[\frac{\mathbb{P}(\|X\|>t_{n})}{\mathbb{P}(\|X\|\leqslant r)}\right]^{2}=\alpha_{n}(r)^{2},\quad n=0,1,2,\cdots.\end{align*}
$$
 

于是有

 
$$
\alpha_{n}(r)\leqslant\exp\{2n\log\alpha_{0}(r)\},\ n=0,1,\cdots.
$$
 

此外，由于 $(\sqrt{2})^{n+4}r>t_{n}$，故有

 
$$
\begin{align*}\mathbb{P}(\|X\|>(\sqrt{2})^{n+4}r)&\leqslant\mathbb{P}(\|X\|>t_{n})\\&=\alpha_{n}(r)\mathbb{P}(\|X\|\leqslant r)\\&\leqslant\exp\{2n\log\alpha_{0}(r)\},\quad n=0,1,2,\cdots.\end{align*}
$$
 

因此，对 $\lambda>0$，令

 
$$
\Sigma_{n}=\left\{x\in E\mid(\sqrt{2})^{n+4}r<\|x\|\leqslant(\sqrt{2})^{n+5}r\right\},
$$
 

我们有

---

 
$$
\begin{align*}\int_{\|x\|>4r}e^{\lambda\|x\|^{2}}\mu(dx)&=\sum_{n=0}^{\infty}\int_{\Sigma_{n}}e^{\lambda\|x\|^{2}}\mu(dx)\\&\leqslant\sum_{n=0}^{\infty}\mathbb{P}(\|X\|>(\sqrt{2})^{n+4}r)\exp\{\lambda r^{2}2^{n+5}\}\\&\leqslant\sum_{n=0}^{\infty}\exp\{2n(\log\alpha_{0}(r)+32\lambda r^{2})\}\;.\end{align*}
$$
 

先取r充分大，使 $P(\|X\| > r) < e^{-1}P(\|X\| \leqslant r)$，再取λ充分小，使得

 
$$
\log\frac{\mathbb{P}(\|X\|>r)}{\mathbb{P}(\|X\|\leqslant r)}+32\lambda r^{2}\leqslant-1,
$$
 

由于 $2n \leqslant 2^{n}$，故有

 
$$
\int_{E}e^{\lambda\|x\|^{2}}\mu(d x)\leqslant e^{16\lambda r^{2}}+\frac{e^{2}}{e^{2}-1}.
$$
 

---

## 第 10 章 Choquet 积分与离散集函数

密度和Choquet积分是由Choquet(1953)引入的，最初用于统计力学和位势理论。离散密度是许多应用领域的基础，例如Dempster-Shafer的证据推理理论、合作博弈理论和多标准决策理论等。在证据推理理论中，密度被解释为信任函数和似真函数；在合作博弈理论中，密度被解释为子联盟的贡献；而在多标准决策理论中，密度被解释为对联合标准的重视程度。

本章前4节基于Yan (2010)介绍Choquet积分理论，内容来自Denneberg(1994)；第5节介绍离散集函数的Möbius反转和Shapley值，以及证据推理中的信任函数和质量函数；第6节介绍Shannon熵.

## 10.1 单调函数的积分

假设$I$为$\mathbb{R}$的(开,闭或半闭)区间. 令$f:I\to\mathbb{R}$是$I$上的递减函数. 令$a=\inf\{x:x\in I\}$, $J=[\inf_{x\in I}f(x),\sup_{x\in I}f(x)]$. 则存在一个递减函数$g:J\to\mathbb{R}$, 使得

 
$$
a\vee\sup\{x|f(x)>y\}\leqslant g(y)\leqslant a\vee\sup\{x|f(x)\geqslant y\}.
$$
 

称这样的$g$为$f$的伪逆，记为$\check{f}$．注意：除去一个至多可数集(简记为e.c.)，$\check{f}$是唯一的．我们有$(\check{f})^\sim = f$，e.c.，并且$f \leqslant g$等价于$\check{f} \leqslant \check{g}$．如果$f(x)$是$\check{f}$的一个连续点，则$\check{f}(f(x)) = x$．

命题10.1.1 对于满足 $\lim_{x\to\infty}f(x)=0$的递减函数 $f:\overline{\mathbb{R}}_{+}\to\overline{\mathbb{R}}_{+}$和 $f$的任何伪逆 $\tilde{f}$，我们有

 
$$
\int_{0}^{\infty}\tilde{f}(y)d y=\int_{0}^{\infty}f(x)d x,
$$
 

这里通过对 $x > f(0)$令 $\tilde{f}(x) = 0$，将 $\tilde{f}$从 $[0, f(0)]$扩展到了 $\mathbb{R}_+$。对于递减函数 $f: [0, b] \to \mathbb{R}$，其中 $0 < b < \infty$，并对 $f$的任何伪逆 $\tilde{f}$，我们有

 
$$
\int_{0}^{b}f(x)dx=\int_{0}^{\infty}\check{f}(y)dy+\int_{-\infty}^{0}(\check{f}(y)-b)dy,
$$
 

其中把 $\tilde{f}$从 $[f(b), f(0)]$扩展到了 $\mathbb{R}$，方法是对 $x > f(0)$，令 $\tilde{f}(x) = 0$，对 $x < f(b)$，令 $\tilde{f}(x) = f(b)$。

证 为证第一个结论, 令

 
$$
S_{f}=\{(x,y)\in\mathbb{R}_{+}^{2}:0\leqslant y\leqslant f(x),x\in\mathbb{R}_{+}\},
$$
 

---

 
$$
S_{\check{f}}=\{(x,y)\in\mathbb{R}_{+}^{2}:0\leqslant x\leqslant\check{f}(y),y\in\mathbb{R}_{+}\}.
$$
 

则$S_f$和$S_{\bar{f}}$在$\mathbb{R}^2$中的闭包$\overline{S}_f$和$\overline{S}_{\bar{f}}$是相同的。但$f$和$\bar{f}$的积分分别是$\overline{S}_f$和$\overline{S}_{\bar{f}}$的面积，因此它们相等。

现在假设 $f:[0,b]\to\mathbb{R}$是一递减函数，其中 $0<b<\infty$。存在一个点 $a\in[0,b]$，使得对 $x<a$， $f(x)\geq0$，对 $x>a$， $f(x)\leq0$。定义

 
$$
g(x)=f(x)I_{[0,a)}(x),\quad h(x)=-f(bx)I_{(0,ba)}(x),\quad x\in[0,\infty].
$$
 

则在 $\mathbb{R}_{+}$上， $\check{f}=\check{g},\check{h}(x)=b-\check{f}(-x)$，e.c.. 由上述已证结论得：

 
$$
\int_{0}^{a}f(x)dx=\int_{0}^{\infty}g(x)dx=\int_{0}^{\infty}\check{g}(y)dy=\int_{0}^{\infty}\check{f}(y)dy,
$$
 

 
$$
\begin{align*}\int_{a}^{b}f(x)dx&=-\int_{0}^{\infty}h(x)dx=-\int_{0}^{\infty}\check{h}(x)dx\\&=-\int_{0}^{\infty}(b-\check{f}(-x))dx=\int_{-\infty}^{0}(\check{f}(y)-b)dy.\end{align*}
$$
 

将两个等式相加就得到所需的结果.

### 10.2 单调集函数, 共单调函数

令Ω为非空集，我们用 $2^\Omega$表示Ω的所有子集构成的集类。令 $S$包含 $\varnothing$和 $\Omega$的集类。称函数 $\mu:S \to \mathbb{R}_+ = [0, \infty]$为 $S$上的集函数，如果它满足 $\mu(\varnothing) = 0$。

定义10.2.1 S上的集函数μ称为单调的，如果每当A ⊂ B, A, B ∈ S 时，有  $\mu(A) \leqslant \mu(B)$.  $\mu$ 称为次模(相应地，超模, 模)，如果A, B ∈ S 且A ∪ B, A ∩ B ∈ S 蕴含  $\mu(A \cup B) + \mu(A \cap B) \leqslant (\text{相应地}, \geqslant, =)\mu(A) + \mu(B)$.  $\mu$ 称为次可加(相应地，超可加), 如果A, B ∈ S 且A ∪ B ∈ S, A ∩ B =  $\varnothing$ 蕴含  $\mu(A \cup B) \leqslant (\text{相应地}, \geqslant)\mu(A) + \mu(B)$.

如果S是代数, 则μ是模, 当且仅当μ是可加的. 如果S是σ-代数, 则μ是σ-可加的, 当且仅当它是可加和从下连续的.

以下我们恒假定S是 $\sigma$-代数, $\mu$为S上的单调集函数.

定义10.2.2 设 $(\Omega,S)$为一可测空间，X是 $\Omega$上的一可测函数. 令

 
$$
G_{\mu,X}(x)=\mu(X>x).
$$
 

称 $G_{\mu,X}$为X关于 $\mu$的(递减)分布函数，称其伪逆函数 $\check{G}_{\mu,X}$为X关于 $\mu$的分位数函数.

由于 $0\leqslant G_{\mu,X}\leqslant\mu(\Omega)$， $\check{G}_{\mu,X}$是在 $[0,\mu(\Omega)]$上定义的.

---

命题10.2.3 设μ是S上的单调集函数, X是S可测函数. 如果u是一个递增函数, 且u和 $G_{\mu,X}$没有共同的不连续点, 则

 
$$
\check{G}_{\mu,u(X)}=u\circ\check{G}_{\mu,X}\;,\;\mathrm{e.c.}.
$$
 

证 令 $u^{-1}(y)=\inf\{x\mid u(x)>y\}$. 则

 
$$
\{x\mid u(x)>y\}\subset\{x\mid x\geqslant u^{-1}(y)\}.
$$
 

因此，如果 $[X = u^{-1}(y), u(X) > y] = \varnothing$，则有 $[u(X) > y] = [X > u^{-1}(y)]$；否则 $u^{-1}(y)$是 $u$的不连续点，从而 $G_{\mu,X}$在 $u^{-1}(y)$处连续。在这种情况下，我们有 $\mu([X > u^{-1}(y)]) = \mu([X \geq u^{-1}(y)])$，这意味着 $\mu([u(X) > y]) = \mu([X > u^{-1}(y)])$，即有

 
$$
G_{\mu,u(X)}=G_{\mu,X}\circ u^{-1}.
$$
 

因此，为证命题，只需证

 
$$
\begin{align*}\sup&\Big\{x\mid G_{\mu,X}\circ u^{-1}(x)>y\Big\}\leqslant u\circ\check{G}_{\mu,X}(y)\\&\leqslant\sup\Big\{x\mid G_{\mu,X}\circ u^{-1}(x)\geqslant y\Big\}.\end{align*}
$$
 

先证第一个不等式. 假设 $G_{\mu,X}\circ u^{-1}(x)>y$，则 $u^{-1}(x)\leqslant\tilde{G}_{\mu,X}(y)$. 我们分别考虑两种情况：当 $u^{-1}(x)<\tilde{G}_{\mu,X}(y)$时， $x<u\circ\tilde{G}_{\mu,X}(y)$; 当 $u^{-1}(x)=\tilde{G}_{\mu,X}(y)$，则 $G_{\mu,X}$在 $\tilde{G}_{\mu,X}(y)$处是不连续的. 因此， $u$在 $\tilde{G}_{\mu,X}(y)$处连续. 在后一情况下，有 $x=u(u^{-1}(x))=u\circ\tilde{G}_{\mu,X}(y)$. 这证明了第一个不等式.

现证第二个不等式. 如果  $x < u \circ \check{G}_{\mu,X}(y)$，则  $u^{-1}(x) \leqslant \check{G}_{\mu,X}(y)$. 我们考虑两种情况: 当  $u^{-1}(x) < \check{G}_{\mu,X}(y)$ 时， $G_{\mu,X} \circ u^{-1}(x) > y$; 当  $u^{-1}(x) = \check{G}_{\mu,X}(y)$ 时， $u \in \check{G}_{\mu,X}(y)$ 处不连续. 因此， $G_{\mu,X}$ 在  $\check{G}_{\mu,X}(y)$ 处连续. 在后一种情况下，有  $G_{\mu,X} \circ u^{-1}(x) = G_{\mu,X} \circ \check{G}_{\mu,X}(y) = y$. 这证明了第二个不等式.

定义10.2.4 两个函数X,Y : Ω → ℝ称为共单调的,是指不存在ω₁,ω₂ ∈ Ω使得X(ω₁) < X(ω₂) 且Y(ω₁) > Y(ω₂).

命题10.2.5 设 $X,Y:\Omega\to\mathbb{R}$，以下两条件是等价的：

(1) X 和 Y 是共单调的;

(2) 存在 $\mathbb{R}$上的连续非降函数 $u$和 $v$，使得 $u(z) + v(z) = z$， $z \in \mathbb{R}$，且 $X = u(X + Y)$， $Y = v(X + Y)$。

证 只需证(1) $\Rightarrow$(2). 设X,Y 共单调. 令 $Z=X+Y$. 易知任一 $z\in Z(\Omega)$ 有唯一分解: 存在某个 $\omega\in\Omega$, 使得 $z=Z(\omega), x=X(\omega), y=Y(\omega), z=x+y$. 我们用 $u(z)$ 和 $v(z)$ 分别记x 和y. 则由X 和Y 的共单调性易知u 和v 为 $Z(\Omega)$ 上的非降函数.

---

往证u,v 在 $Z(\Omega)$上连续. 首先注意对 $h>0$和 $z,z+h\in Z(\Omega)$, 我们有

 
$$
z+h=u(z+h)+v(z+h)\geqslant u(z+h)+v(z)=u(z+h)+z-u(z).
$$
 

于是有

 
$$
u(z)\leqslant u(z+h)\leqslant u(z)+h.
$$
 

类似地，对 $h>0$和 $z,z-h\in Z(\Omega)$，我们有

 
$$
u(z)-h\leqslant u(z-h)\leqslant u(z).
$$
 

这两个不等式蕴含u的连续性，从而v也连续.

下面只需证明u和v可以延拓成为R上的连续非降函数．先将它们延拓到Z(Ω)的闭包Z(Ω)上．如果z是Z(Ω)的单向边界点，由于u和v是非降函数，则可通过取极限来连续延拓．如果z是Z(Ω)的双向极限点，则上面两个不等式蕴含双向极限吻合，从而可以连续延拓．最后，通过在开集R  $\backslash$ Z(Ω)的每个联通区间上进行线性延拓，可以将u和v从Z(Ω)延拓到R，而且保持u(z) + v(z) = z成立．

系10.2.6 令 $\mu$是S上的单调集函数. 如果X,Y是 $\Omega$上的实值共单调函数, 则

 
$$
\check{G}_{\mu,X+Y}=\check{G}_{\mu,X}+\check{G}_{\mu,Y},\mathrm{~e.c.~}.
$$
 

证 使用命题10.2.5 (2)中的记号, 我们有 $X = u(X + Y)$,  $Y = v(X + Y)$. 由命题10.2.3我们得到

 
$$
\begin{align*}\check{G}_{\mu,X+Y}&=(u+v)\circ\check{G}_{\mu,X+Y}=u\circ\check{G}_{\mu,X+Y}+v\circ\check{G}_{\mu,X+Y}\\&=\check{G}_{\mu,X}+\check{G}_{\mu,Y},\mathrm{e.c.}.\end{align*}
$$
 

## 10.3 Choquet 积分

在本节中，令Ω为非空集，S是Ω上的σ代数，S上的单调集函数μ称为容度或模糊测度。我们将定义S可测函数关于μ的Choquet积分，并研究其基本性质。作为模糊测度的例子，我们介绍扭曲概率和λ-模糊测度。

### 10.3.1 Choquet积分的定义和基本性质

令X是S可测函数. 如果下面的勒贝格积分

 
$$
\int_{0}^{\mu(\Omega)}\check{G}_{\mu,X}(t)d t
$$
 

---

存在, 其中  $\check{G}_{\mu,X}$ 是 X 的分位数函数, 则我们说 X 关于  $\mu$ 是可积的, 并将其定义为 X 关于  $\mu$ 的 Choquet 积分. 我们用  $\int X d\mu$ 或  $\mu(X)$ 表示之.

如果 $\mu(\Omega)<\infty$，由命题10.1.1并利用 $(\check{f})^{\sim}=f$，e.c.，我们有

 
$$
\mu(X)=\int_{0}^{\infty}G_{\mu,X}(x)d x+\int_{-\infty}^{0}(G_{\mu,X}(x)-\mu(\Omega))d x.
$$
 

回想一下, 如果 $\mu$是概率测度, 而X是随机变量, 则X关于 $\mu$的期望可以如下表示:

 
$$
\mu(X)=\int_{0}^{\infty}\mu(X\geqslant t)dt+\int_{-\infty}^{0}(\mu(X\geqslant t)-1)dt.
$$
 

因此，X关于概率测度 $\mu$的Choquet积分与它的期望值相符。

如果X是形如 $X=\sum_{i=1}^{n}x_{i}I_{A_{i}}$的简单函数，其中 $A_{1},\cdots,A_{n}$互不相交，并且 $(x_{i})$按降序排列，即 $x_{1}\geqslant\cdots\geqslant x_{n}$，则

 
$$
\mu(X)=\sum_{i=1}^{n}(x_{i}-x_{i+1})\mu(S_{i})=\sum_{i=1}^{n}x_{i}(\mu(S_{i})-\mu(S_{i-1})),
$$
 

其中 $S_{i}=A_{1}\cup\cdots\cup A_{i},i=1,\cdots,n,S_{0}=\varnothing,\quad x_{n+1}=0.$

现在我们研究Choquet积分的基本性质.

命题10.3.1 令μ是代数S上的单调集函数, X, Y : Ω → ₪ 是S可测函数, 则

(1)  $\int I_A d\mu = \mu(A), \quad A \in \mathcal{S}.$

(2) (正齐次性) 对 c > 0, 有  $\int cXd\mu = c\int Xd\mu$.

(3) (不对称性) 如果  $\mu(\Omega) < \infty$，则

 
$$
\int X d\mu=-\int(-X)d\bar{\mu},
$$
 

其中 $\bar{\mu}(A)=\mu(\Omega)-\mu(A)$

(4) (单调性) 如果  $X \leqslant Y$，则  $\int X \, d\mu \leqslant \int Y \, d\mu$.

(5) 如果  $\mu(\Omega) < \infty$，则

 
$$
\int(X+c)d\mu=\int X d\mu+c\mu(\Omega),\quad c\in\mathbb{R}.
$$
 

(6)(共单调可加性)如果X,Y是共单调和实值的,则

 
$$
\int(X+Y)d\mu=\int Xd\mu+\int Yd\mu.
$$
 

(7) (转换规则) 对于  $T : \Omega \to \Omega'$，满足  $T^{-1}(S') \subset S$，令  $\mu^T(A) = \mu(T^{-1}(A))$， $A \in S'$。则对上  $\mu^T$-可测函数  $Z : \Omega' \to \mathbb{R}$，我们有  $G_{\mu, Z \circ T} = G_{\mu^T, Z}$ 和

 
$$
\int Z d\mu^{T}=\int Z\circ T d\mu.
$$
 

---

证 (1) 是不足道的. 对 c > 0, 有  $\check{G}_{\mu,cX} = c\check{G}_{\mu,X}$ (命题10.2.5). 由此推得 (2).

(3)是由于如下事实： $G_{\bar{\mu},X}(x)=\mu(\Omega)-G_{\mu,-X}(-x)$. (4)由系10.2.6推出.其他性质容易验证.

命题10.3.2 令 $X:\Omega \to \mathbb{R}$为 $S$可测函数， $\mu$和 $\nu$是 $S$上的单调集函数。则

(1) 对 c > 0,  $G_{c\mu,X} = cG_{\mu,X}$,  $\int Xd(c\mu) = c\int Xd\mu.$

(2) 如果  $\mu$ 和  $\nu$ 是有限的，则

 
$$
G_{\mu+\nu,X}=G_{\mu,X}+G_{\nu,X},\mathrm{e.c.},\quad\int X d(\mu+\nu)=\int X d\mu+\int X d\nu.
$$
 

(3) 如果  $\mu(\Omega) = \nu(\Omega)$ 或  $X \geqslant 0$，则  $\mu \leqslant \nu$ 蕴含

 
$$
G_{\mu,X}\leqslant G_{\nu,X},\mathrm{e.c.},\int X d\mu\leqslant\int X d\nu.
$$
 

(4) 如果 $(\mu_{n})$ 是 S 上的单调集函数的增序列，且

 
$$
\lim_{n\to\infty}\mu_{n}(A)=\mu(A),\quad A\in\mathcal{S},
$$
 

则对下有界的可测函数X,

 
$$
\lim_{n\to\infty}\int X d\mu_{n}=\int X d\mu.
$$
 

证 (1)-(3)显然. 往证(4). 如果 $X \geqslant 0$, 则 $\int X d\mu_{n} = \int G_{\mu_{n}, X}(x) dx$, 从而单调收敛定理给出所要的断言. 减去一常数表明该断言对于下有界函数X成立. ☐

注10.3.3 由于 $X^{+}$和 $-X^{-}$是共单调的, 如果X是实值的, 则

 
$$
\int X d\mu=\int X^{+}d\mu+\int(-X^{-})d\mu.
$$
 

如果进一步 $\mu(\Omega)<\infty$，则

 
$$
\int X d\mu=\int X^{+}d\mu-\int X^{-}d\bar{\mu}.
$$
 

命题10.3.4 令μ是S上的单调集函数. 对于任何q, 0 < q < μ(Ω), 定义

 
$$
\mu_{q}(A)=q\wedge\mu(A),\;A\in\mathcal{S}.
$$
 

则 $(\mu_{q})$是单调增的，并对任意 $\mu$可积的S可测函数X，

 
$$
\lim_{q\to\mu(\Omega)}\int X d\mu_{q}=\int X d\mu.
$$
 

---

证 由于

 
$$
G_{\mu_{q},X}(x)=\mu_{q}(X>x)=q\wedge\mu(X>x)=q\wedge G_{\mu,X},
$$
 

 $\check{G}_{\mu,X}$ 和  $\check{G}_{\mu_{q},X}$ 在  $[0,q)$ 上重合. 因此, 我们有

 
$$
\begin{align*}\int X d\mu_{q}&=\int_{0}^{q}\check{G}_{\mu_{q},X}(t)dt=\int_{0}^{q}\check{G}_{\mu,X}(t)dt\\&\to\int_{0}^{\mu(\Omega)}\check{G}_{\mu,X}(t)dt=\int X d\mu.\end{align*}
$$
 

### 10.3.2 扭曲概率

定义10.3.5 设P是可测空间 $(\Omega,S)$上的概率测度， $\gamma:[0,1]\to[0,1]$是增函数，且 $\gamma(0)=0,\gamma(1)=1$。则 $\mu=\gamma\circ P$是单调集函数。称 $\mu$为扭曲概率，称 $\gamma$为相应的扭曲函数。

如果γ是凹(凸)函数，则γ ∩ Ψ是次模(超模)。我们只考虑凹函数情形，凸函数情形类似。令A, B ∈ S。设a := Ψ(A) ≤ Ψ(B) =: b。记c = Ψ(A ∩ B)，d = Ψ(A ∪ B)。则c ≤ a ≤ b ≤ d。由于Ψ是模，我们有c + d = a + b。因此，γ的凹性蕴含γ(c) + γ(d) ≤ γ(a) + γ(b)。这证明了γ ∩ Ψ是次模。

X关于 $g \circ \mathbb{P}$的Choquet积分 $(g \circ \mathbb{P})(X)$可以如下表示：

 
$$
(g\circ\mathbb{P})(X)=\int_{0}^{1}q_{X}(1-x)d g(x)=\int_{0}^{1}q_{X}(t)d\gamma(t),
$$
 

其中 $q_{X}(t)$是X的分布函数 $F_{X}$右连续逆， $\gamma(t)=1-g(1-t)$.

### 10.3.3 λ-模糊测度

本节结果可参见Berres (1988).

定义10.3.6 设  $\lambda \in (-1, \infty)$. 在 S 上定义的归一化单调集函数  $\mu_{\lambda}$ 称为  $\lambda$-模糊测度, 如果对于 S 中每对不相交集 A 和 B, 有

 
$$
\mu_{\lambda}(A\cup B)=\mu_{\lambda}(A)+\mu_{\lambda}(B)+\lambda\mu_{\lambda}(A)\mu_{\lambda}(B).
$$
 

如果 $\lambda=0$，则 $\mu_{0}$是可加的。对 $\lambda\in(-1,\infty)$和 $\lambda\neq0$，我们定义

 
$$
\psi_{\lambda}(r)=\log_{(1+\lambda)}(1+\lambda r).
$$
 

 $\psi_{\lambda}$的逆是

 
$$
\psi_{\lambda}^{-1}(r)=\frac{1}{\lambda}[(1+\lambda)^{r}-1].
$$
 

---

容易验证 $\psi_\lambda \circ \mu_\lambda$是可加的。由于当 $\lambda > 0$（相应地， $\lambda \in (-1, 0)$）时， $\psi_\lambda^{-1}$是凹（相应地，凸）函数，所以 $\mu_\lambda$是次模（相应地，超模）。

对 $\Omega$中互不相交的子集的有限序列 $A_{1}, A_{2}, \cdots, A_{n}$，有

 
$$
\mu_{\lambda}\left(\bigcup_{i=1}^{n}A_{i}\right)=\psi_{\lambda}^{-1}\left[\sum_{i=1}^{n}\psi_{\lambda}(\mu_{\lambda}(A_{i}))\right].
$$
 

从而，

 
$$
\begin{align*}\mu_{\lambda}\left(\bigcup_{i=1}^{n}A_{i}\right)&=\psi_{\lambda}^{-1}\left[\sum_{i=1}^{n}\log_{(1+\lambda)}(1+\lambda\mu_{\lambda}(A_{i}))\right]\\&=\frac{1}{\lambda}\left(\prod_{i=1}^{n}[1+\lambda\mu_{\lambda}(A_{i})]-1\right).\end{align*}
$$
 

设$P$是可测空间$(\Omega,S)$上的概率测度，则集函数$\psi_{\lambda}^{-1}\circ P$是一$\lambda$-模糊测度。对$\Omega$上的$S$可测函数$X$，把它关于该$\lambda$-模糊测度的Choquet积分定义为它的$\lambda$-期望$E_{\lambda}(X)$：

 
$$
\begin{array}{r}{\varPi E_{\lambda}[X]=\int X d(\psi_{\lambda}^{-1}\circ\varPi).}\end{array}
$$
 

λ-期望有下列性质：

(1) 如果  $\lambda \leqslant \lambda'$，则  $E_{\lambda}[X] \geqslant E_{\lambda'}[X]$.

(2)  $\lim_{\lambda \to -1} E_{\lambda}[X] = \operatorname{esssup}_{\omega \in \Omega} X(\omega).$

(3)  $\lim_{\lambda \to \infty} \mathbb{E}_{\lambda}[X] = \operatorname{essinf}_{\omega \in \Omega} X(\omega).$

对决策问题,  $\lambda$ 表示风险追求的区域是  $(-1,0)$, 表示风险厌恶的区域是  $(0,\infty)$. 当  $\lambda = 0$, 决策者是风险中性的.

对$\lambda\in(-1,\infty)$, 令$\bar{\lambda}=-\lambda/(1+\lambda)$, 则两个$\lambda$-模糊测度$\psi_{\lambda}^{-1}\circ\mathbb{P}$ 和$\psi_{\bar{\lambda}}^{-1}\circ\mathbb{P}$ 是互为共轭的, 即有

 
$$
\psi_{\bar{\lambda}}^{-1}\circ\mathbb{P}(A)=1-\psi_{\lambda}^{-1}\circ\mathbb{P}(A^{c}),
$$
 

以及

 
$$
\mathbb{E}_{\lambda}(X)=-\mathbb{E}_{\bar{\lambda}}(-X).
$$
 

## 10.4 Choquet积分的次可加性定理

设 $\mu$是S上的单调集函数. 关于 $\mu$的Choquet积分称为次可加的, 如果对任意 $\mu$可积可测函数X和Y, 有

 
$$
\int(X+Y)d\mu\leqslant\int Xd\mu+\int Yd\mu.
$$
 

---

关于 $\mu$的Choquet积分具有次可加性的必要条件是 $\mu$为次模，因为 $I_{A\cup B}$和 $I_{A\cap B}$是共单调的，我们有

 
$$
\begin{align*}\int(I_{A}+I_{B})d\mu&=\int(I_{A\cup B}+I_{A\cap B})d\mu=\int I_{A\cup B}d\mu+\int I_{A\cap B}d\mu\\&=\mu(A\cup B)+\mu(A\cap B),\ A,B\subset\Omega.\end{align*}
$$
 

我们将证明集函数的次模性也是使Choquet积分具有次可加性的充分条件.

以下引理包含证明的核心.

引理10.4.1 令$\{A_1, \cdots, A_n\}$是$\Omega$的划分，$A$是$\{A_1, \cdots, A_n\}$生成的代数，$\mu : A \to [0,1]$是单调集函数，且$\mu(\Omega) = 1$。对于$\{1, \cdots, n\}$的任何置换$\pi$，定义

 
$$
S_{i}^{\pi}=\bigcup_{j=1}^{i}A_{\pi_{j}},\quad i=1,\cdots,n,\quad S_{0}^{\pi}=\varnothing.
$$
 

我们通过

 
$$
\begin{array}{r}{\mathbb{P}^{\pi}(A_{\pi_{i}}):=\mu(S_{i}^{\pi})-\mu(S_{i-1}^{\pi}),\quad i=1,\cdots,n,}\end{array}
$$
 

定义A上的概率测度 $P^\pi$。现令 $X : \Omega \to \mathbb{R}$为A可测的，即在每个 $A_i$上为常数。假设 $\mu$是次模，则

 
$$
\int X d\mu\geqslant\int X d P^{\pi},
$$
 

等式成立, 如果

 
$$
X(A_{\pi_{1}})\geqslant X(A_{\pi_{2}})\geqslant\cdots\geqslant X(A_{\pi_{n}}).
$$
 

证 只需对恒等置换  $\pi = id$ 情形证明．我们把  $S_{i}^{id}$ 记为  $S_{i}$，把  $IP^{id}$ 记为 IP，并令  $x_{i} = X(A_{i})$．我们首先证明关于等式的断言．假设  $x_{1} \geqslant x_{2} \geqslant \cdots \geqslant x_{n}$．由于  $S_{1} \subset S_{2} \subset \cdots \subset S_{n}$，类  $\{I_{S_{1}}, \cdots I_{S_{n}}\}$ 是共单调的．因此，我们有  $\left(\frac{1}{2}x_{i+1} = 0, S_{0} = \varnothing\right)$

 
$$
\begin{aligned}\int X d\mu&=\int\sum_{i=1}^{n}x_{i}I_{A_{i}}d\mu=\int\sum_{i=1}^{n}(x_{i}-x_{i+1})I_{S_{i}}\\&=\sum_{i=1}^{n}(x_{i}-x_{i+1})\mu(S_{i})=\sum_{i=1}^{n}x_{i}(\mu(S_{i})-\mu(S_{i-1}))\\&=\int X d\boldsymbol{P}.\end{aligned}
$$
 

现在假设对于某个i < n有 $x_{i} < x_{i+1}$。令 $\varphi$是只将i和 $i+1$对调的置换。则 $S_{i-1}^{\varphi} = S_{i-1} = S_{i}^{\varphi} \cap S_{i}$， $S_{i+1}^{\varphi} = S_{i+1} = S_{i}^{\varphi} \cup S_{i}$。 $\mu$的次模性蕴含

 
$$
\boldsymbol{P}(A_{i+1})=\mu(S_{i+1})-\mu(S_{i})\leqslant\mu(S_{i}^{\varphi})-\mu(S_{i-1}^{\varphi})
$$
 

---

 
$$
=\mathbb{P}^{\varphi}(A_{\varphi_{i}})=\mathbb{P}^{\varphi}(A_{i+1}).
$$
 

在等式两端同乘以 $x_{i+1}-x_{i}>0$给出

 
$$
(x_{i+1}-x_{i})\mathbb{P}(A_{i+1})\leqslant(x_{i+1}-x_{i})\mathbb{P}^{\varphi}(A_{i+1}).
$$
 

另一方面, 我们有

 
$$
\begin{align*}\mathbb{P}(A_{i})+\mathbb{P}(A_{i+1})&=\mu(S_{i+1})-\mu(S_{i-1})=\mu(S_{i+1}^{\varphi})-\mu(S_{i-1}^{\varphi})\\&=\mathbb{P}^{\varphi}(A_{i+1})+\mathbb{P}^{\varphi}(A_{i}).\end{align*}
$$
 

乘以 $x_{i}$与上面的不等式相加给出

 
$$
x_{i}\mathbb{P}^{\varphi}(A_{i})+x_{i+1}\mathbb{P}^{\varphi}(A_{i+1})\geqslant x_{i}\mathbb{P}(A_{i})+x_{i+1}\mathbb{P}(A_{i+1}),
$$
 

这蕴含

 
$$
\int X d\mathbb{P}^{\varphi}\geqslant\int X d\mathbb{P}.
$$
 

通过归纳,我们可以从有限的多个 $\varphi$型的置换构造出一个置换 $\theta$,使得

 
$$
X(A_{\theta_{1}})\geqslant X(A_{\theta_{2}})\geqslant\cdots\geqslant X(A_{\theta_{n}})
$$
 

和

 
$$
\int X d\mathbb{P}^{\theta}\geqslant\int X d\mathbb{P}.
$$
 

由于我们已经证明左边的积分即为 $\int Xd\mu$，我们完成了所要结果的证明。

为了方便起见，我们说可测函数X的一个属性 $\mu$-本质上成立，是指其分位数函数 $\check{G}_{\mu,X}$ e.c. 具有相同的属性。例如，我们说X是 $\mu$-本质上 $>-\infty$，是指对所有 $t\in[0,\mu(\Omega)]$，有 $G_{\mu,X}(t)>-\infty$，e.c..

以下是次可加性定理.

定理10.4.2 令μ为S上的单调次模集函数, X, Y为Ω上的S可测函数. 如果X, Y 是μ-本质上> -∞, 并且

 
$$
\lim_{x\to-\infty}G_{\mu,X}(x)=\mu(\Omega),\quad\lim_{x\to-\infty}G_{\mu,Y}(x)=\mu(\Omega),
$$
 

则

 
$$
\int(X+Y)d\mu\leqslant\int Xd\mu+\int Yd\mu.
$$
 

如果 $\mu$是从下连续的，有关X和Y的 $\mu$-本质上 $>-\infty$假设可以取消。

证 首先, 我们假设  $\mu(\Omega) = 1$. 如果 X, Y 是简单函数, 则  $Z := X + Y$ 也是简单函数. 令  $A_{1}, A_{2}, \cdots, A_{n}$ 是  $\Omega$ 的划分, 使得 X 和 Y 在每个  $A_{i}$ 上为常数, 且有  $Z(A_{1}) \geq$

---

 $Z(A_{2}) \geqslant \cdots \geqslant Z(A_{n})$ 。根据引理10.4.1，存在A上概率测度P，其中A是 $A_{1}, A_{2}, \cdots, A_{n}$ 生成的代数，使得

 
$$
\int Zd\mu=\int Zd\mathbb{P}=\int Xd\mathbb{P}+\int Yd\mathbb{P}.
$$
 

引理10.4.1蕴含

 
$$
\int(X+Y)d\mu\leqslant\int Xd\mu+\int Yd\mu.
$$
 

现在假设X,Y是有界的. 令 $Z=X+Y$,  $X_{n}=u_{n}(X)$,  $Y_{n}=u_{n}(Y)$,  $Z_{n}=u_{n}(Z)$. 其中

 
$$
u_{n}=\inf\left\{\frac{k}{n}\mid k\in\mathbb{Z},\frac{k}{n}\geqslant x\right\},\ n\in\mathbb{N},
$$
 

Z表示整数全体的集合，则 $X_{n},Y_{n},Z_{n}$是简单函数的序列，并且

 
$$
X\leqslant X_{n}\leqslant X+\frac{1}{n},\ Y\leqslant Y_{n}\leqslant Y+\frac{1}{n},
$$
 

 
$$
X_{n}+Y_{n}-\frac{2}{n}\leqslant Z_{n}\leqslant X_{n}+Y_{n}.
$$
 

命题10.3.1的(4)和(5)蕴含

 
$$
\int X d\mu\leqslant\int X_{n}d\mu\leqslant\int X d\mu+\frac{1}{n}.
$$
 

因此，

 
$$
\lim_{n\to\infty}\int X_{n}d\mu=\int X d\mu.
$$
 

这对Y和Z同样适用. 但是, 积分的单调性和对简单函数次可加性蕴含

 
$$
\int Z_{n}d\mu\leqslant\int(X_{n}+Y_{n})d\mu\leqslant\int X_{n}d\mu+\int Y_{n}d\mu,
$$
 

由此推得所要的不等式.

假设 $\mu(\Omega)=1$，且X,Y是下有界的。通过加一个常数，我们可以假设X,Y≥0。

令 $X_{n}=n\wedge X,Y_{n}=n\wedge Y$。由于递增序列 $G_{\mu,X_{n}+Y_{n}}$收敛到 $G_{\mu,X+Y}$，我们有

 
$$
\int(X_{n}+Y_{n})d\mu=\int_{0}^{\infty}G_{\mu,X_{n}+Y_{n}}(x)dx\rightarrow\int_{0}^{\infty}(X+Y)d\mu.
$$
 

另一方面, 积分的单调性和对有界函数的次可加性蕴含

 
$$
\int(X_{n}+Y_{n})d\mu\leqslant\int X_{n}d\mu+\int Y_{n}d\mu\leqslant\int X d\mu+\int Y d\mu,
$$
 

从中我们得到期望的不等式.

---

假设 $\mu(\Omega)=1$，且 $\check{G}_{\mu,X}(t)$和 $\check{G}_{\mu,Y}$是e.c.下有界的。在这种情况下，存在 $a\in\mathbb{R}$，使得 $G_{\mu,X}(a)=1$， $G_{\mu,Y}(a)=1$。定义 $\overline{X}=a\vee X$，它是下有界的。从而 $G_{\mu,\overline{X}}=G_{\mu,X}$，因此 $\int Xd\mu=\int\overline{X}d\mu$。对Y做同样处理我们得到

 
$$
\int(X+Y)d\mu\leqslant\int(\overline{X}+\overline{Y})d\mu\leqslant\int\overline{X}d\mu+\int\overline{Y}d\mu=\int Xd\mu+\int Yd\mu.
$$
 

现在考虑一般情况. 首先, 命题10.3.2(1)将所要的不等式从归一化的 $\mu$扩展到有限的 $\mu$. 我们将利用 $\mu_{q}=q\wedge\mu,0<q<\mu(\Omega)$把结论扩展对无界的X,Y和无限的 $\mu(\Omega)$. 事实上, 由于

 
$$
\lim_{t\to-\infty}G_{\mu,X}(t)=\mu(\Omega)>q,
$$
 

可以找到具有 $G_{\mu,X}(a)\geq q$的 $a\in\mathbb{R}$，使得 $G_{\mu_{q},X}=q\wedge G_{\mu,X}(a)=q=\mu_{q}(\Omega)$。这意味着 $\check{G}_{\mu_{q},X}(t)$，和类似的 $\check{G}_{\mu_{q},Y}$，是e.c.下有界的。由已证结果推得

 
$$
\int(X+Y)d\mu_{q}\leqslant\int Xd\mu_{q}+\int Yd\mu_{q}.
$$
 

令 $q\to\mu(\Omega)$，命题10.3.4蕴含

 
$$
\int(X+Y)d\mu\leqslant\int Xd\mu+\int Yd\mu.
$$
 

最后，讨论μ是从下连续情形，分别处理两种情况。1）如果μ(X + Y > -∞) < μ(Ω)，或f(X + Y)dμ不存在，或是-∞。这时无须证明或断言是不足道的。2）假设μ(X + Y > -∞) = μ(Ω)。由于{X + Y > -∞} = {X > -∞} ∩ {Y > -∞}，μ的单调性蕴含μ(X > -∞) = μ(Ω)和μ(Y > -∞) = μ(Ω)。于是容易看出，对于所有t ∈ [0, μ(Ω)]，有 $\tilde{G}_{\mu,X}(t) > -\infty, \tilde{G}_{\mu,Y}(t) > -\infty$，e.c.。因此，我们又处于已经证明的情况。

系10.4.3 令μ为S上的单调次模集函数, X, Y为Ω上的S可测函数. 如果X, Y, X - Y和Y - X是μ本质上 > -∞, 则

 
$$
\left|\int X d\mu-\int Y d\mu\right|\leqslant\int|X-Y|d\mu.
$$
 

特别有

 
$$
\left|\int X d\mu\right|\leqslant\int|X|d\mu.
$$
 

证 可以假设  $\int X d\mu \geqslant \int Y d\mu$. 由定理10.4.1 我们有

 
$$
\int X d\mu=\int(X-Y+Y)d\mu\leqslant\int(X-Y)d\mu+\int Y d\mu,
$$
 

---

再利用 $X-Y\leqslant|X-Y|$推得

 
$$
0\leqslant\int X d\mu-\int Y d\mu\leqslant\int(X-Y)d\mu\leqslant\int|X-Y|d\mu,
$$
 

这就是欲证的不等式.

### 10.5 离散集函数

在本节中, 我们考虑一个只含有限个元素的基本集合E和定义在 $2^E$上的实值集函数(唯一要求是在空集处取值为零). 我们将对实值集函数定义它的Möbius反转和Shapley值; 介绍证据推理中的信任函数和质量函数. 作为离散容度Choquet积分的应用, 给出多标准决策的一个例子, 和对Ellsberg悖论的一个解释.

### 10.5.1 实值集函数的Möbius反转

为方便起见，令 $E = \{1, 2, \cdots, n\}$，对任意 $A \subset E$，用 $|A|$表示 $A$的元素个数。

引理10.5.1 设 $A \subset E$,  $A \neq \varnothing$,  $T \subset A$, 则有

$$
\sum_{F\subset A}(-1)^{|F|}=0,\quad\sum_{T\subset F\subset A}(-1)^{|F|}=0,\;T\neq A;=(-1)^{|A|},\;T=A,   \tag*{(10.5.1)}
$$

$$
\sum_{T\subset F\subset A}(-1)^{|F|-|T|}\frac{1}{|F|}=\frac{(|A|-|T|)!(|T|-1)!}{|A|!}.   \tag*{(10.5.2)}
$$

证 设 $i \leqslant |A|$，则总共有 $\binom{|A|}{i}$个A的子集，其元素个数等于i，故有

 
$$
\sum_{F\subset A}(-1)^{|F|}=\sum_{i=0}^{|A|}\binom{|A|}{i}(-1)^{i}=(1-1)^{|A|}=0.
$$
 

如果 $T \neq A$，则有

 
$$
\sum_{T\subset F\subset A}(-1)^{|F|}=\sum_{D\subset A\backslash T}(-1)^{|D\cup T|}=(-1)^{|T|}\sum_{D\subset A\backslash T}(-1)^{|D|}=0;
$$
 

如果T = A，上面和式只有单独一项 $(-1)^{|A|}$， $(10.5.1)$得证．往证 $(10.5.2)$．记 $|A| = a$， $|T| = t$．如果T = A， $(10.5.2)$自动成立(约定 $0!=1$)，两边都是 $1/|A|$．如果T ≠ A，在 $\{F : T \subset F \subset A\}$中，有 $\binom{a-t}{k-t}$个不同子集F其元素个数等于k．此外，注意到 $(-1)^{t-a+2j} = (-1)^{t-a} = (-1)^{a-t}$，我们有

 
$$
\sum_{T\subset F\subset A}(-1)^{|F|-|T|}\frac{1}{|F|}=\sum_{k=t}^{a}\binom{a-t}{k-t}(-1)^{k-t}\frac{1}{k}
$$
 

---

 
$$
\begin{aligned}&=\sum_{j=0}^{a-t}\binom{a-t}{j}(-1)^{j}\frac{1}{j+t}=\sum_{j=0}^{a-t}\binom{a-t}{j}(-1)^{j}\int_{0}^{1}x^{j+t-1}dx\\&=\int_{0}^{1}(x-1)^{a-t}x^{t-1}(-1)^{t-a+2j}dx=\int_{0}^{1}(1-x)^{a-t}x^{t-1}dx\\&=\frac{(a-t)!(t-1)!}{a!}=\frac{(|A|-|T|)!(|T|-1)!}{|A|!}.\end{aligned}
$$
 

(10.5.2) 得证.

下一引理通常被归于Shafer (1976)，但实际上该引理的充分性部分已经存在于Shapley(1953)的主要定理证明之中了。

引理10.5.2 设 $\mu$和 $m$是 $2^E$上的实值集函数，则

$$
\mu(A)=\sum_{X\subset A}m(X),\ A\subset E,   \tag*{(10.5.3)}
$$

当且仅当

$$
m(A)=\sum_{X\subset A}(-1)^{|A\setminus X|}\mu(X),\ A\subset E.   \tag*{(10.5.4)}
$$

称 $m$为 $\mu$的Möbius反转.

证 设m由10.5.4给定, 则由10.5.1推知

 
$$
\begin{align*}\sum_{X\subset A}m(X)&=\sum_{X\subset A}\sum_{Y\subset X}(-1)^{|X\setminus Y|}\mu(Y)\\&=\sum_{Y\subset A}\left[(-1)^{|Y|}\mu(Y)\sum_{Y\subset X\subset A}(-1)^{|X|}\right]\\&=(-1)^{|A|}\mu(A)(-1)^{|A|}=\mu(A).\end{align*}
$$
 

即有 $(10.5.3)$. 反之，设 $(10.5.3)$成立，则由 $(10.5.1)$推知

 
$$
\begin{align*}\sum_{X\subset A}(-1)^{|A\setminus X|}\mu(X)&=\sum_{X\subset A}\left[(-1)^{|X|+|A|}\sum_{Y\subset X}m(Y)\right]\\&=\sum_{Y\subset A}\left[(-1)^{|A|}m(Y)\sum_{Y\subset X\subset A}(-1)^{|X|}\right]\\&=(-1)^{|A|}m(A)(-1)^{|A|}=m(A).\end{align*}
$$
 

即有 $(10.5.4)$.

### 10.5.2 实值集函数的Shapley值

在一个合作博弈中, 每个参与者从合作中获得收入的一部分. 如何公平地分配收入? 问题的关键在于如何合理评价每个参与者的实际贡献. Shapley(1953)通过公

---

理化方法提出了Shapley值概念，用来表示参与者对一个合作博弈的平均边际贡献。在Shapley提出该概念时，并没有意识到它与决策理论的联系。直到二十世纪八十年代，Shapley值才被广泛应用于多标准决策等领域。

定义10.5.3 如果实值集函数 $\mu$满足如下的超可加性：

 
$$
\mu(S\cup T)\geqslant\mu(S)+\mu(T),\ \forall S,T\subset E,S\cap T=\varnothing,
$$
 

则称 $\mu$为E上的一个博弈.

Shapley(1953)对博弈定义了如下的“值函数”，实际上该定义适用于一般实值集函数。下面定义中的公理1替换了Shapley(1953)的“置换不变性”。

定义10.5.4 设 $\mu$是E上的一个实值集函数. $\mu$的Shapley值是定义于E上满足如下四条公理的实值函数 $\phi$:

公理1. 对称性：设 $i,j\in E$，如果 $\forall S\subset E\setminus\{i,j\}$，有 $\mu(S\cup\{i\})=\mu(S\cup\{j\})$，则 $\phi_i(\mu)=\phi_j(\mu)$；

公理2. 有效性： $\sum_{i=1}^{n}\phi_{i}(\mu)=\mu(E);$

公理3. 如果 $\{i\}$是一个零元素(即 $\forall S \subset E$, 有 $\mu(S \cup \{i\}) = \mu(S)$), 则 $\phi_i(\mu) = 0$;

公理4. 可加性：对任意两个E上的实值集函数 $\mu$和 $\nu$，有 $\phi(\mu+\nu)=\phi(\mu)+\phi(\nu)$.

Shapley(1953)只在“博弈”范围证明“博弈”的值函数存在性是有错误的(因为一个博弈乘上-1就不再是博弈了), 应该在一般的实值集函数范围讨论. 下一定理是对Shapley(1953)的一个修正.

定理10.5.5 设 $\mu$是E上的实值集函数, 满足定义10.5.4中四条公理的函数 $\phi$是唯一的, 它由下式给出:

$$
\phi_{i}(\mu)=\sum_{T\subset E}\gamma_{n}(|T|)[\mu(T)-\mu(T\setminus\{i\})],\quad i=1,\cdots,n.   \tag*{(10.5.5)}
$$

其中

 
$$
\gamma_{n}(|T|)=\frac{(n-|T|)!(|T|-1)!}{n!}.
$$
 

证 在测度论中有集合的“示性函数”概念. 类似地, 我们引进“示性集函数”概念: 设  $R \subset E, R \neq \varnothing$. 对  $S \subset E$, 如果  $R \subset S$, 令  $\mu_R(S) = 1$, 否则令  $\mu_R(S) = 0$. 称  $\mu_R$ 是  $R$ 的示性集函数. 令  $c$ 为一实数, 对集函数  $c\mu_R$ 而言, 唯一满足上述前三条公理的函数  $\phi$ 显然为:  $\phi_i(c\mu_R) = (c/|R|)I_R(i)$, 其中  $I_R$ 是集合  $R$ 的示性函数. 由于

 
$$
\sum_{X\subset A}m(X)=\sum_{R\subset E}m(R)\mu_{R}(A),
$$
 

由引理10.5.2知， $\mu$ 是示性集函数的线性组合：

 
$$
\mu=\sum_{R\subset E}c_{R}(\mu)\mu_{R},
$$
 

---

其中

$$
c_{R}(\mu)=\sum_{T\subset R}(-1)^{|R|-|T|}\mu(T).   \tag*{(10.5.6)}
$$

由于 $\phi_{i}(c\mu_{R})=(c/|R|)I_{R}(i)$，故于是由公理4有

 
$$
\begin{align*}\phi_{i}(\mu)&=\sum_{R\subset E}\phi_{i}(c_{R}(\mu)\mu_{R})=\sum_{R\subset E,i\in R}c_{R}(\mu)\frac{1}{|R|}\\&=\sum_{R\subset E,i\in R}\frac{1}{|R|}\sum_{T\subset R}(-1)^{|R|-|T|}\mu(T)\\&=\sum_{T\subset E}\sum_{T\cup\{i\}\subset R\subset E}(-1)^{|R|-|T|}\frac{1}{|R|}\mu(T).\end{align*}
$$
 

应用 $(10.5.2)$即得

 
$$
\begin{align*}\phi_{i}(\mu)&=\sum_{T\subset E,i\in T}\gamma_{n}(|T|)\mu(T)-\sum_{T\subset E,i\notin T}\gamma_{n}(|T|+1)\mu(T)\\&=\sum_{T\subset E}\gamma_{n}(|T|)[\mu(T)-\mu(T\setminus\{i\})].\end{align*}
$$
 

定理证毕.

注10.5.6 从证明看出, 如果用 $\mu$的Möbius反转 $m$来表达 $\mu$的Shapley值, 则有

$$
\phi_{i}(\mu)=\sum_{R\subset E,i\in R}\frac{m(R)}{|R|},\quad i=1,\cdots,n.   \tag*{(10.5.7)}
$$

从合作博弈观点考虑, 如果把 $m(R)$理解为子联盟R的“综合贡献”, 则(10.5.7)表明: 每个参与者的Shapley值恰好是他所在子联盟平均“综合贡献”的总和.

系10.5.7 实值集函数 $\mu$的Shapley值还具有如下性质：

(1) 置换不变性:  $\phi_{\pi i}(\pi\mu)=\phi_{i}(\mu)$, 其中  $\pi$ 是 E 上的一个置换;

(2) 齐次性: 对任何实数  $c, \phi_{i}(c\mu) = c\phi_{i}(\mu)$;

(3) 如果  $\mu$ 是容度，函数  $\phi$ 是非负的；

(4) 如果  $\mu$ 是博弈，对所有  $i \in E$，有  $\phi_i(\mu) \geq \mu(\{i\})$.

例十10.5.8 假设有一投资者出资创办一个公司，他雇佣了有同等能力的$n-1$个工人，编号记为$2,\cdots,n$. 对年度收入如何合理分配？在这个合作博弈中，参与者的集合是$E$（其中编号1为雇主），博弈$\mu$是$\mu(E)=1,\mu(S)=0,\forall S\subset E\setminus\{1\}$. 容易计算该博弈的Shapley值为$\{1/2,1/2(n-1),\cdots,1/2(n-1)\}$. 因此，雇主得到总收入的一半，而工人们平均分配总收入的另一半.

例子10.5.9 设 $\{1,2,\cdots,n\}$是参与投票表决的机构代表，投票规则规定某些组合投赞成票且总数超过规定数量时决议才通过。问题是如何正确评估这一投票规

---

则中的权力分配？从合作联盟考虑，对那些使得决议通过的子联盟贡献定为1，否则定为0。下面是三个投票规则例子：

(1) 联合国安理会由5个常任理事国和10个非常任理事国组成，提案仅当全部常任理事国和至少4个非常任理事国赞成时方可通过。计算Shapley值，每个常任理事的权力是0.196，每个非常任理事的权力只有0.002。如果表决规则改为提案仅当全部常任理事国和至少7个非常任理事国赞成时方可通过，则每个常任理事的权力降为0.170，每个非常任理事的权力上升为0.015。

(2) 1958年欧洲经济共同体6国在罗马签署了关于投票表决规则的协议，规定了各国的投票权：法国、联邦德国、意大利各4票，比利时和荷兰各2票，卢森堡为1票。任何决议至少要得到12票才能通过。计算Shapley值，得到在这一投票规则中的权力分配为：法国、联邦德国、意大利各为0.233，比利时和荷兰各为0.15，卢森堡为0。这表明，在这投票规则中，卢森堡的1票权实际不起任何作用。

(3) 假定一家公司有甲乙丙丁4个大股东，他们所占公司资产份额之比是1:2:3:4，所以投票权分别是1、2、3、4票。任何决议赞成票数超过6才能通过。计算Shapley值，得到在这一投票规则中甲乙丙丁的权力分别为：1/12，1/6，1/6，7/12。这表明，尽管丙的资产是乙的1.5倍，在这投票规则中，两者地位相同。但是，如果投票规则更改为“任何决议至少要得到7张赞成票才能通过”，甲乙丙丁的权力分别为：1/12，1/12，1/6，2/3，这时甲乙地位相同了。

### 10.5.3 信任函数和质量函数

证据推理在20世纪60年代由Dempster(1967)奠基, 尔后Shafer(1976)对其进行了整体构建. 该方法得到工程界与人工智能学者的采用与关注. 证据推理首先要处理的是信任函数和质量函数.

定义10.5.10 设E是一有限集, $2^{E}$是E的全体子集族,如集函数Bel: $2^{E}\rightarrow[0,1]$满足以下条件:

(1)  $Bel(\varnothing) = 0$;

(2) Bel(E) = 1;

(3)  $\infty$ 阶单调性: 对任意正整数 m 和 E 的子集  $A_{1}, \cdots, A_{m}$ 有

 
$$
B e l\big(\bigcup_{i=1}^{m}A_{i}\big)\geqslant\sum_{\varnothing\neq I\subset\{1,\cdots,m\}}(-1)^{|I|+1}B e l\big(\bigcap_{i\in I}A_{i}\big),
$$
 

则Bel称为E上的一信任函数,E称为识别框架.

概率测度是信任函数的一种特殊情况(条件(3)中等号成立, 见第3章习题3.1.4), 称为Bayes信任函数. 在证据推理理论中, Shafer认为对信任函数的赋值是由“人”或“信息源”在一定的证据基础上做出的力求体现客观的主观判断. 在Shafer的理论中,

---

信任又认为是可以分割的. 把一个人的所有信任分到E不同的子集上应是可能的. 给每一E的子集A一部分信任, 这部分信任是恰恰分给A的, 而不给A的子集.

定义10.5.11 设E是一识别框架, 如果函数 $m:2^{E}\to[0,1]$满足

(1)  $m(\varnothing) = 0$;

(2)  $\sum_{A\subset E}m(A)=1,$

则称$m$为$E$上的基本概率分配或质量函数. 令$A \subset E$, $m(A)$称为$A$的基本概率或质量. 若$m(A) > 0$, 则称$A$为$m$的焦元.

下一定理归于Shafer (1976), 其证明也可见Chateauneuf and Jaffray (1989).

定理10.5.12 如果m是识别框架E上的质量函数,则如下定义的Bel:

$$
Bel(A)=\sum_{X\subset A}m(X),\ A\subset E,   \tag*{(10.5.8)}
$$

是E上的一个信任函数，且满足如下关系：

$$
m(A)=\sum_{X\subset A}(-1)^{|A\setminus X|}B e l(X),\ A\subset E.   \tag*{(10.5.9)}
$$

反之, 如果Bel是识别框架E上的信任函数, 则由(10.5.9)定义的m是E上的一个质量函数, 并且由它按(10.5.8)定义的信任函数正是原来的信任函数.

证 由  $\sum_{X\subset A}m(X)=\sum_{R\subset E}m(R)\mu_{R}(A)$ 及引理10.5.2知，(10.5.8)成立当且仅当(10.5.9)成立. 往证由(10.5.8)定义的Bel有 $\infty$阶单调性. 给定 $\{A_{i}\subset E,1\leqslant i\leqslant m\}$. 对 $X\subset E$, 令 $I(X)=\{i:1\leqslant i\leqslant m,X\subset A_{i}\}$. 由(10.5.1)推得

 
$$
\begin{align*}&\sum_{\varnothing\neq I\subset\{1,\cdots,m\}}(-1)^{|I|+1}Bel\big(\bigcap_{i\in I}A_{i}\big)\\&=\sum_{\varnothing\neq I\subset\{1,\cdots,m\}}\Big[(-1)^{|I|+1}\sum_{\substack{X\subset\bigcap_{i\in I}A_{i}}}m(X)\Big]\\&=\sum_{X:I(X)\neq\varnothing}\Big[m(X)\sum_{\varnothing\neq I\subset I(X)}(-1)^{|I|+1}\Big]\\&=\sum_{X:I(X)\neq\varnothing}m(X)\leqslant\sum_{\substack{X\subset\bigcup_{i}^{m}A_{i}}}m(X)=Bel\big(\bigcup_{i=1}^{m}A_{i}\big).\end{align*}
$$
 

另一方面，根据(10.5.8)，由(10.5.9)定义的 $m$满足 $m(\varnothing) = 0$和 $\sum_{A \subset E} m(A) = 1$。为证 $m$是质量函数，只需证 $m$的非负性。设 $A = \{k_1, \cdots, k_m\} \subset E$，令 $A_i = A \setminus \{k_i\}$， $1 \leq i \leq m$，则 $A = \cup_{i=1}^{m} A_i$，故由(10.5.9)和 $Bel$的 $\infty$阶单调性得

 
$$
m(A)=\sum_{X\subset A}(-1)^{|A\setminus X|}B e l(X)
$$
 

---

 
$$
=m(\bigcup_{i=1}^{m}A_{i})-\sum_{\varnothing\neq I\subset\{1,\cdots,m\}}(-1)^{|I|+1}B e l(\bigcap_{i\in I}A_{i})\geqslant0.
$$
 

证毕.

对A所持有的态度不太可能完全由Bel(A)描述出来, 所以又有如下定义:

定义10.5.13 设识别框架为E,  $A \subset E$，对A的补集的信任度称为对A的怀疑度，对A不怀疑程度称为A的似真度，记为Pl(A)，即

$$
P l(A)=1-B e l(A^{c}).   \tag*{(10.5.10)}
$$

称模糊测度Pl为似真函数.

命题10.5.14 我们有

$$
\begin{aligned}Pl(A)&=\sum_{B\cap A\neq\varnothing}m(B),\quad A\subset E,\\ Bel(A)&\leqslant Pl(A),\quad A\subset E.\end{aligned}   \tag*{(10.5.11)}
$$

证 由 $(10.5.10)$式,

 
$$
P l(A)=1-B e l(A^{c})=\sum_{B\subset E}m(B)-\sum_{B\subset A^{c}}m(B)=\sum_{B\cap A\neq\varnothing}m(B).
$$
 

下一命题归于Yager(1999).

命题10.5.15 设m为E上的质量函数， $\{B_{1},\cdots,B_{q}\}$ 是m的全体焦元. 对每个 $i:1\leqslant i\leqslant q$，任取 $|B_{i}|$ 维的一个概率分布 $\{w_{i}(1),\cdots,w_{i}(|B_{i}|)\}$，如下定义一个集函数：

 
$$
m_{w}(A)=\sum_{i=1}^{q}\sum_{j=1}^{|B_{i}\cap A|}w_{i}(j),\quad A\subset E,
$$
 

则 $m_{w}$是一容度，且有 $Bel \leqslant m_{w} \leqslant Pl.$

证 显然μ是容度. 容易看出: 如果令 $\hat{w}_{i}(1)=1,\hat{w}_{i}(j)=0,j\geqslant2$, 则 $m_{\hat{w}}=Bel;$ 如果令 $\bar{w}_{i}(|B_{i}|)=1,\bar{w}_{i}(j)=0,j<|B_{i}|$, 则 $m_{\bar{w}}=Pl$, 由此推得 $Bel\leqslant m_{w}\leqslant Pl.$

注10.5.16 (1) 设 m 为 E 上的质量函数,  $\{B_{1},\cdots,B_{q}\}$ 是 m 的全体焦元, 则由注10.5.6知, 信任函数 Bel 的 Shapley 值为

 
$$
\phi_{i}(Bel)=\sum_{j:i\in B_{j}}\frac{m(B_{j})}{|B_{j}|},\quad i=1,\cdots,n.
$$
 

Yager(2000)用了很长篇幅推导才获得这一结果, 并用类似推导证明了似真函数与信任函数有相同的Shapley值. 我们未发现似真函数Shapley值的简单推导.

---

(2) 似真函数Pl是次可加的, 且有从下连续性. 信任函数Bel是超可加的, 且有从上连续性.

(3) 似真函数Pl具有 $\infty$阶交替性: 对任意正整数m和E的子集 $A_{i},1\leqslant i\leqslant m$, 有

 
$$
P l\big(\bigcap_{i=1}^{m}A_{i}\big)\leqslant\sum_{\varnothing\neq I\subset\{1,\cdots,m\}}(-1)^{|I|+1}P l\big(\bigcup_{i\in I}A_{i}\big).
$$
 

(4) 对λ-模糊测度μλ而言，可以证明(见Berres (1988))：当 $-1 < \lambda \leqslant 0$时，μλ为似真函数；当 $0 \leqslant \lambda < \infty$时，μλ为信任函数.

### 10.5.4 多标准决策的一个例子

下面是一个多标准决策的例子, 来自Grabisch(1996). 在某中学, 通常采用加权平均来计算三门科目的成绩来评价学生. 这三门科目分别为数学(M)、物理(P)、文学(L). 假设该中学更重视理科成绩, 给这三门科目的权重分别为  $(3/8, 3/8, 2/8)$. 由于数学和物理的成绩有很强的相关性, 在这个权重矢量中, 数学和物理的权重都很高. 这就产生了重叠效应. 为解决这个问题, 可以选取一个合适的Choquet 密度  $\mu$, 利用对这三门成绩的Choquet 积分来对学生给与综合评判. 出发点是考虑如下因素: (1)  $\mu$ 在每个科目的取值保持初始权重的比例; (2) 为避免数学和物理的重叠效应,  $\mu$ 在  $\{M, P\}$ 的取值应该小于  $\mu$ 分别在  $\{M\}$ 和  $\{P\}$ 的取值之和; (3) 为了重视理科和文学得都好的学生,  $\mu$ 在  $\{M, L\}$ 和  $\{L, P\}$ 的取值应比分别在两科取值之和要大. 因此, 可考虑如下态度:

 
$$
\begin{aligned}&\mu(\{M\})=\mu(\{P\})=0.45,\mu(\{L\})=0.3,\\&\mu(\{M,P\})=0.5,\mu(\{M,L\})=\mu(\{P,L\})=0.9,\\ \end{aligned}
$$
 

利用加权平均和Choquet积分对学生的成绩进行评估, 得到如下结果:

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>学生</td><td style='text-align: center; word-wrap: break-word;'>M</td><td style='text-align: center; word-wrap: break-word;'>P</td><td style='text-align: center; word-wrap: break-word;'>L</td><td style='text-align: center; word-wrap: break-word;'>加权和</td><td style='text-align: center; word-wrap: break-word;'>Choquet 积分</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>15.25</td><td style='text-align: center; word-wrap: break-word;'>13.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>b</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>12</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>12.75</td><td style='text-align: center; word-wrap: break-word;'>13.6</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>c</td><td style='text-align: center; word-wrap: break-word;'>14</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>15</td><td style='text-align: center; word-wrap: break-word;'>14.625</td><td style='text-align: center; word-wrap: break-word;'>14.9</td></tr></table>

利用Shapley值的定义式(10.5.5)，可以计算出密度 $\mu$的Shapley值： $\phi_{M}(\mu)=\phi_{P}(\mu)=0.2916,\phi_{L}(\mu)=0.4167$。这表明，用Choquet积分对学生的成绩进行汇总计算时，文学这一科目的重要性被强化了，这导致对学生c的综合评价高于学生a。

#### 10.5.5 用Choquet积分解释Ellsberg悖论

Kninght 对风险(Risk)与不确定性(Ambiguity)进行了区分: 所谓“不确定性”是指那些发生概率尚不知的随机事件, 所谓“风险”是指那些已知概率分布的随机事

---

件. Ellsberg悖论是在不确定性下决策的一个典型例子. 下面的内容取自Narukawa and Murofushi(2004).

例子10.5.17 (Ellisberg悖论) 假设一罐中有90颗球，其中30颗是红球，60颗是黑球或白球，但黑白球的数量不知道。现在轮到您从罐子里随机取一个球。面对两个下注： $X_R$ 和  $X_B$，其中  $X_R$（或  $X_B$）表示如果您拿出的是一个红球（相应的，黑球），您将获得100美元。大多数人会选择  $X_R$，因为罐子里可能只有为数不多的黑球。另一方面，面对如下两个下注： $X_{RW}$ 和  $X_{BW}$，其中  $X_{RW}$（或  $X_{BW}$）表示如果您拿出的是红球或白球（相应的，黑球或白球），您将获得100美元。大多数人会选择  $X_{BW}$，因罐子里可能只有为数不多的白球。所以我们有  $X_B \prec X_R$ 和  $X_{RW} \prec X_{BW}$。这里  $X \prec Y$ 表示Y优于X。

用于在风险情况下决策的期望效用理论无法解释这种偏好. 事实上, 令  $E = \{R, B, W\}$ 为状态空间,  $\mathcal{M} = \{0, 100\}$ 为可能的结果. 假定在 E 上有一概率  $\mathbb{P}$, 在 M 上有一效用函数 U, 使得  $X \prec Y \iff \mathbb{E}[U(X)] < \mathbb{E}[U(Y)]$. 则由  $X_{RW} \prec X_{BW}$ 推得

 
$$
\begin{align*}U(100)\mathbb{P}(\{B\})&=U(100)\big(\mathbb{P}(\{B,W\})-\mathbb{P}(\{W\})\big)\\&>U(100)\big(\mathbb{P}(\{R,W\})-\mathbb{P}(\{W\})=U(100)\mathbb{P}(\{R\})\big),\end{align*}
$$
 

这与 $X_{B}\prec X_{R}$矛盾.

上述偏好的确立是基于如下事实： $\{R\}$ 和  $\{B, W\}$ 有确定概率，而  $\{B\}$ 和  $\{W\}$ 的概率未知，偏好隐含有“不确定性厌恶”，即低估不确定事件的概率。所以，在状态空间上定义密度  $\mu$ 要做如下考虑：由于事件  $\{B\}$ 和  $\{W\}$ 地位相同， $\mu(\{B\})$ 与  $\mu(\{W\})$ 应该相等，但两者之和应小于  $\mu(\{B, W\})$；另外， $\mu(\{B, R\})$ 和  $\mu(\{W, R\})$ 也应相等，合理的选择是  $\mu(\{B, R\}) = \mu(\{B\}) + \mu(\{R\})$ 和  $\mu(\{W, R\}) = \mu(\{W\}) + \mu(\{R\})$。基于上述考虑，可以如下定义密度  $\mu$：

 
$$
\mu(\{R\})=\frac{1}{3},\mu(\{B\})=\mu(\{W\})=\frac{2}{9},
$$
 

 
$$
\mu(\{B,W\})=\frac{2}{3},\mu(\{R,W\})=\mu(\{R,B\})=\frac{5}{9},
$$
 

且 $\mu(\{R,B,W\})=1$。则X关于 $\mu$的Choquet积分如下：

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>$X_{R}$</td><td style='text-align: center; word-wrap: break-word;'>$X_{B}$</td><td style='text-align: center; word-wrap: break-word;'>$X_{RW}$</td><td style='text-align: center; word-wrap: break-word;'>$X_{BW}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mu(X)$</td><td style='text-align: center; word-wrap: break-word;'>$(1/3) \times 100$</td><td style='text-align: center; word-wrap: break-word;'>$(2/9) \times 100$</td><td style='text-align: center; word-wrap: break-word;'>$(5/9) \times 100$</td><td style='text-align: center; word-wrap: break-word;'>$(2/3) \times 100$</td></tr></table>

于是有 $\mu(X_{B})<\mu(X_{R})$ 和  $\mu(X_{RW})<\mu(X_{BW})$，不再有任何矛盾.

---

## 10.6 Shannon 熵

Shannon于1948年通过公理化方法建立了一种测量不确定性程度的函数, 这就是Shannon熵(entropy). 熵值越大, 它所代表的信息的不确定性就越大, 或相应的概率分布均匀程度越高. 均匀分布的Shannon熵值最大.

定义10.6.1 对离散分布 $P=(p_{1},\cdots,p_{n})(n\geqslant2)$，Shannon熵定义为

$$
S_{n}(p_{1},\cdots,p_{n})=-\sum_{i=1}^{n}p_{i}\log p_{i},   \tag*{(10.6.1)}
$$

其中对数底取为2或e，并约定 $0\log0=0$.

 $S_{n}(p_{1},\cdots,p_{n})$ 具有如下基本性质：

(1) 连续性： $S_{n}(p_{1},\cdots,p_{n})$ 是  $(p_{1},\cdots,p_{n})$ 的连续函数；

(2) 置换不变性：设 $\sigma$是 $(1,\cdots,n)$上的一个置换，则有

 
$$
S_{n}(p_{1},\cdots,p_{n})=S_{n}(p_{\sigma(1)},\cdots,p_{\sigma(n)});
$$
 

(3) 递归性:

 
$$
\begin{aligned}S_{n}(p_{1},\cdots,p_{n})&=S_{n-1}(p_{1}+p_{2},p_{3},\cdots,p_{n})\\&+(p_{1}+p_{2})S_{2}(p_{1}/(p_{1}+p_{2}),p_{2}/(p_{1}+p_{2}));\end{aligned}
$$
 

Shannon(1948)证明了：满足上述三条性质的函数只可能是

$$
S_{n}(p_{1},\cdots,p_{n})=-C\sum_{i=1}^{n}p_{i}\ln p_{i},   \tag*{(10.6.2)}
$$

其中C是一正常数. 如果用熵表示不确定性程度来解释的话, 性质1表明当概率分布只有微小变化时, 整个分布所蕴含的不确定性变化也很小; 性质2成立也是自然的, 指标本身除了用作记号外, 与整个分布的不确定性没有关系; 性质3要求熵函数满足某种递归性质, 但这一性质的直观含义不太明显.

自从Shannon引进熵概念以后，有许多文章从不同的“公理系统”出发推导出Shannon熵的表达式(10.6.2). 下面借助于Chaundy and Mcleod(1960)的一个结果给出(10.6.2)的一个推导. 首先假定离散分布 $P=(p_{1},\cdots,p_{n})$的熵具有如下形式：

$$
S_{n}(p_{1},\cdots,p_{n})=\sum_{i=1}^{n}f(p_{i}),   \tag*{(10.6.3)}
$$

其中$f$为一非负连续函数. 如果离散分布$P=(p_{1},\cdots,p_{n})$和$Q=(q_{1},\cdots,q_{m})$分别是两个相互独立的随机变量$X$和$Y$的分布, 关于熵的一个合理的假定, 是$(X,Y)$的联合

---

分布的熵应该是两者边缘分布熵的和, 即有

$$
\sum_{i=1}^{n}\sum_{j=1}^{m}f(p_{i}q_{j})=\sum_{i=1}^{n}f(p_{i})+\sum_{j=1}^{m}f(q_{j}).   \tag*{(10.6.4)}
$$

下面证明满足 $(10.6.4)$的连续函数f必然具有如下形式:

$$
f(x)=-Cx\log x,\ 0\leqslant x\leqslant1,   \tag*{(10.6.5)}
$$

其中C是一正常数，并约定 $0\log0=0$.

令p,q,r,s为正整数，满足 $1\leqslant r\leqslant p,1\leqslant s\leqslant q$。在(10.6.4)中令

 
$$
\begin{aligned}n&=p-r+1,\quad m=q-s+1,\\p_{i}&=1/p,\quad1\leqslant i\leqslant n-1,\quad p_{n}=r/p,\\q_{j}&=1/q,\quad1\leqslant j\leqslant m-1,\quad q_{m}=s/q,\end{aligned}
$$
 

则有

 
$$
\begin{align*}(p-r)(q-s)f(1/pq)&+(p-r)f(s/pq)+(q-s)f(r/pq)+f(rs/pq)\\\cdot\quad&=(p-r)f(1/p)+f(r/p)+(q-s)f(1/q)+f(s/q).\end{align*}
$$
 

令 $h(x)=xf(1/x)$，且在上式两边同乘pq推得

$$
\begin{aligned}(p-r)(q-s)h(pq)&+s(p-r)h(pq/s)+r(q-s)h(pq/r)+rsh(pq/rs)\\&=q(p-r)h(p)+qrh(p/r)+p(q-s)h(q)+psh(q/s).\end{aligned}   \tag*{(10.6.6)}
$$

在10.6.6中令s=1得到

$$
(p-r)q h(p q)+r q h(p q/r)=q(p-r)h(p)+q r h(p/r)+p q h(q).   \tag*{(10.6.7)}
$$

在 $(10.6.7)$中令r=1得到 $h(pq)=h(p)+h(q)$，将此表达式代入 $(10.6.7)$即得

 
$$
h(p q/r)=h(p/r)+h(q).
$$
 

由对称性也有

 
$$
h(p q/s)=h(p/r)+h(q/s).
$$
 

将上述 $h(pq), h(pq/r)$和 $h(pq/s)$的表达式代入(10.6.6)给出

 
$$
h(p q/r s)=h(p/r)+h(q/s).
$$
 

---

于是对任何有理数 $x,y\geq1$，有 $h(xy)=h(x)+h(y)$。由h的连续性假定推知对任何实数 $x,y\geq1$，有 $h(xy)=h(x)+h(y)$。因此，由数学分析的一个熟知结果得 $h(y)=C\log y,y\geq1$。由于 $f(x)=xh(1/x),0<x\leq1$，最终有(10.6.5)式。

下面研究Shannon熵的性质．为方便起见, 我们定义一取值于有限点集X的离散随机变量X的熵 $H(X)$为它的离散分布P的熵, 即令

$$
H(X)=-\sum_{x\in\mathcal{X}}p(x)\log p(x),   \tag*{(10.6.8)}
$$

其中 $p(x)=IP(X=x)$

设X和Y分别是取值于有限点集X和Y的随机变量, 它们的联合熵 $H(X,Y)$由其联合分布给出:

$$
H(X,Y)=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(x,y),   \tag*{(10.6.9)}
$$

其中 $p(x,y)=\mathbb{P}(X=x,Y=y)$。如果X和Y独立， $\mathbb{P}(Y=y)=q(y)$，则 $p(x,y)=p(x)q(y)$，从而有 $H(X,Y)=H(X)+H(Y)$。对一般情形，我们有

定理10.6.2 设X和Y分别是取值于有限点集X和Y的两个随机变量, 它们的联合熵 $H(X,Y)$有如下表达式:

$$
H(X,Y)=H(X)+H(Y|X),   \tag*{(10.6.10)}
$$

 $H(Y|X)$称为Y关于X的条件熵, 它由如下公式给出:

$$
H(Y|X)=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(y|x),   \tag*{(10.6.11)}
$$

其中 $p(y|x)=IP(Y=y|X=x).$

证 由于  $p(x,y) = p(x)p(y|x)$，故有  $\log p(x,y) = \log p(x) + \log p(y|x)$；又由于  $\sum_{y\in\mathcal{Y}}p(x,y) = p(x)$，因此由(10.6.9)立得(10.6.10).

定义10.6.3 设X和Y是取值于同一有限点集X的两个随机变量, 其离散分布分别是P和Q. X关于Y的相对熵  $R(X,Y)$ 定义为

$$
R(X,Y)=\sum_{x\in\mathcal{X}}p(x)\log\frac{p(x)}{q(x)},   \tag*{(10.6.12)}
$$

其中对数 $\log$以e为底.  $R(X,Y)$亦称为离散分布P关于离散分布Q的相对熵.

定义10.6.4 设X和Y分别是取值于有限点集X和Y的两个随机变量，其离散分布分别是P和Q，他们的联合分布为 $p(x,y),x\in\mathcal{X},y\in\mathcal{Y}$。X与Y的互信息 $I(X:Y)$定义为联合分布 $\{p(x,y)\}$关于乘积分布 $\{p(x)q(y)\}$的相对熵，即为

$$
I(X:Y)=\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log\frac{p(x,y)}{p(x)q(y)}.   \tag*{(10.6.13)}
$$


---

一般说来, $R(X,Y)\neq R(Y,X)$，但恒有 $I(X:Y)=I(Y:X)$.

定理10.6.5 恒有 $R(X,Y)\geq0$，等号成立的充要条件是P=Q.

证 由于 $\log x \leqslant x - 1$，我们有

 
$$
\log\frac{p(x)}{q(x)}=-\log\frac{q(x)}{p(x)}\geqslant1-\frac{q(x)}{p(x)},
$$
 

从而由10.6.12有

 
$$
R(X,Y)\geqslant\sum_{x\in\mathcal{X}}p(x)\Big[1-\frac{q(x)}{p(x)}\Big]=\sum_{x\in\mathcal{X}}\big[p(x)-q(x)\big]=0.
$$
 

由于 $\log x \leqslant x - 1 = 0$的充要条件是x = 1，故 $R(X,Y) = 0$等价于P = Q。

定理10.6.6 我们有 $I(X:Y)\geq0$，等号成立，当且仅当X与Y独立。此外有

$$
I(X:Y)=H(X)+H(Y)-H(X,Y)=H(X)-H(X|Y),   \tag*{(10.6.14)}
$$

$$
H(X)\geqslant H(X|Y);\ H(X)+H(Y)\geqslant H(X,Y).   \tag*{(10.6.15)}
$$

证 由  $\sum_{y\in\mathcal{Y}}p(x,y)=p(x),\sum_{x\in\mathcal{X}}p(x,y)=q(y)$，由(10.6.13)立刻推得(10.6.14)的第一个等式，再由(10.6.10)推得(10.6.14)的第二个等式．既然  $I(X:Y)$ 是联合分布  $\{p(x,y)\}$ 关于乘积分布  $\{p(x)q(y)\}$ 的相对熵，故由定理10.6.5推知  $I(X:Y)\geqslant0$ ，从而有(10.6.15)式．此外，再由(10.6.14)的第一个等式知： $I(X:Y)=0$ ，当且仅当 X 与 Y 独立．

相对熵和互信息是信息论中的两个基本概念．相对熵可以用来度量一个离散分布与另一个离散分布之间差异的大小，但这一度量关于两个离散分布是非对称的．互信息可以看成是一个随机变量包含另一个随机变量的信息量，或者说是一个随机变量由于已知另一个随机变量而减少的不确定性．互信息也是两个随机变量统计相关性的一种度量，这一度量关于两个随机变量是对称的．

---

## 参考文献

严加安, 1981. 鞅与随机积分引论. 上海: 上海科技出版社.

黄志远, 严加安, 1997. 无穷维随机分析引论. 北京: 科学出版社.

Berres, M., 1988.  $\lambda$-additive measures on measure spaces. Fuzzy Sets and Systems, 27, 159-169.

Chateauneuf, A., Jaffray, J.Y., 1989. Some Characterizations of Lower Probabilities and Other Monotone Capacities Through the Use of Möbius Inversion. Mathematical Social Sciences, 17(3), 263-283.

Chaundy, T.W., Mcleod, J.B., 1960. On a functional equation. Edinburgh Math. Notes, 43, 7-8.

Choquet, G., 1953. Theory of Capacity. Ann. Inst. Fourier, 5, 131-295.

Cohn, D.L., 2013. Measure Theory, Second Edition. Basle: Birkhäuser.

Dempster, A., 1967. Upper and lower probability induced by a multi-valued mapping. Annals of Mathematical Statistics, 38, 325-339.

Denneberg, D., 1994. Non-Additive Measure and Integral. Boston: Kluwer Academic Publishers.

Dudley, R.M., 2002. Real Analysis and Probability. London: Cambridge University Press.

Grabisch, M., 1996. The application of fuzzy integrals in multi-criteria decision making. European Journal of Operational Research, 89, 445-456.

Gross, L., 1965. Abstract Wiener spaces. In: Proc. Fifth Berkeley Symp. Math. Stat. Probab. II, Oakland: University of California Press, Part 1, 31-41.

Hall, P., Heyde, C.C., 1980. Martingale Limit Theory and Its Application. New York: Academic Press.

Kallianpur, G., 1971. Abstract Wiener processes and their reproducing kernel Hilbert spaces. Z. Wahrsch. Verw. Gebiete, 17, 113-123.

Ma, Z.M. (马志明), 1985. Some Results on Regular Conditional Probabilities. Acta Math. Sinica, New Series, 1(4), 128-133.

---

Meyer, P.A., 1972. Martingales and Stochastic Integrals I, LN in Math., 284, Berlin: Springer-Verlag.

Narukawa, Y., Murofushi, T., 2004. Decision modeling using the Choquet integral. Proc. Modeling Decisions for Artificial Intelligence, LN in Computer Science, 3131, 183-193.

Ng, K.W., 1995. On the inversion of Bayes theorem. Presentation in The 3rd ICSA Statistical Conference, August 17-20, 1995. Beijing, China.

Shafer, G., 1976. A Mathematical Theory of Evidence. Princeton: Princeton University Press.

Shannon, C.E., 1948. A Mathematical Theory of Communication. Bell Syst. Tech. J., 27, 379-423, 623-656.

Shapely, L.S., 1953. A value for n-person games. In: Contributions to Game Theory, Kuhn, H. W., Tucker, A. W.(eds.), Princeton: Princeton University Press, 307-317.

Shirayayev, A.N., 1996. Probability. Second Edition. Berlin: Springer-Verlag.

Yager, R.R., 1999. A class of fuzzy measures generated from a Dempster-Shafer belief structure. International Journal of Intelligent Systems, 14 (12), 1239-1247.

Yager, R.R., 2000. On the entropy of fuzzy measures. IEEE Transactions on Fuzzy Systems, 8(4), 453-461.

Yan, J.A. (严加安), 1980. Characterisation d'une classe d'ensembles convex de  $L^{1}$ ou  $\mathcal{H}^{1}$. Séminaire de Probabilités XIV, LN in Math., 784, Berlin: Springer-Verlag, 220-222.

Yan, J.A. (严加安), 1985. On the communitability of essential infimum and conditional expectation operations. Chinese Science Bulletin, 30(8), 1013-1018.

Yan, J.A. (严加安), 1990. A remark on conditional expectations. Chinese Science Bulletin, 35(9), 719-722.

Yan, J.A. (严加安), 1991. Constructing Kernels via Stochastic Measures. In: Gaussian Random Fields, Hida, T et al. (eds.), River Edge: World Scientific Publishing, 396-405.

---

Yan, J.A. (严加安), 2006. A simple proof of two generalized Borel-Cantelli lemmas. Séminaire de Probabilités XXV, LN in Math., 1874, Berlin: Springer-Verlag, 77-79.

Yan, J.A. (严加安), 2010. A short presentation of Choquet integral. In: Recent Development in Stochastic Dynamics and Stochastic Analysis, Interdisciplinary Mathematical Science, Vol. 8, Duan, J. et al. (eds.), River Edge: Wold Scientific Publishing, 269-291.

---

##### 一至四画

## 索引

一致可积 164

上(下)半连续 90

几乎一致(a.un.)收敛 28

几乎处处(a.e.)收敛 28

几乎必然(a.s.) 143

广义鞅 197

不定积分 40

互信息 242

无处稠密 95

开集 89

开邻域 89

从上(下)连续 9

分布函数 130, 157

分位数函数 220

不等式

上穿～186

极大值～185

Chung-Erdős～145

 $C_{r} \sim 50$

Doob～185

Hölder～50, 151

Jensen～50, 155

Kolmogorov～185

Minkowski～50, 152

Schwarz～50

Young～73

引理

Borel-Cantelli～144

Fatou～38, 155

Kronecker～195

Neyman-Pearson～147

Scheffé～39

Steinhaus～73

Urysohn～91

五画

正齐次性 223

正则条件概率 160

正规空间 90

正线性泛函 59

本性上确界 169, 170

本性有界的 52

示性函数 22

示性集函数 233

左(右)一致连续 119

左(右)转换 120

左(右)转换不变 120

可分σ代数 6

可分拓扑空间 89

可测空间 6

可测映射, 可测函数 20

可测同构 7

可测柱集 69

可测矩形 69

可离可测空间 7

右闭靺, 右闭元 190

平稳序列 174

对称差 1

对称集 146

对称算子 205

对偶空间 53

生成的σ代数 4, 23

半环, 半代数, 代数 3

半σ可加 9

六画

有限可加 9

有限置换 146

有界集 94, 98

有限交性质 95

有限核 74

共单调 221

共单调可加 223

---

列紧集 94

协方差算子 210

均值向量 210

在空集处连续 9

同胚，同胚映射 90

先验概率 147

后验概率 148

全收敛 130

全有界集 94

伪逆 219

似真度，似真函数 237

次可加 220

次  $\sigma$ 可加 10

次模 220

向量格 59

七画

投影映射 68

投影可测空间 83

投影序列 83

投影极限 84

扭曲概率 225

扭曲函数 225

局部紧空间 89

局部鞅 197

尾事件，尾  $\sigma$ 代数 146

条件(数学)期望 149, 152

条件概率 147

条件独立 158

条件熵 242

邻域 89

完备测度空间 8

完备距离空间 94

识别框架 235

八画

拓扑空间 89

拓扑群 118

抽象Wiener空间 217

转换规则 223

函数的卷积 73

函数的支撑 91

典则双线性型 209

非负定 199

依测度收敛 28

依分布收敛, 依概率收敛 136

质量函数 235

波兰(Polish)空间 114

单调类 3

单调族 26

单点紧化 90

单模的 126

##### 定理

控制收敛～38,155

次可加性～228

单调类～5,24

单调收敛～38,155

遍历～176

Baire～95

Bochner～203

Bolzano-Weierstrass～31

Carathéodory～14

Carathéodory～(随机版本)85

Choquet～180

Daniell-Stone～60

Daniell-Stone～(随机版本)86

Doob收敛～188

Doob停止～191,192

Doob分解～192

Dini～90

Egoroff～31

Fernique～216

Fubini～71,113

Gross～215

Halmos-Savage～170

Helly～129

Hopf最大遍历～175

Jordan-Hahn分解～41

---

Kolmogorov(相容性)～78

Kolmogorov三级数～194

Lévy连续性～201

Skorohod-Dudley表示～136

L'收敛～155

Lindelöf～96

Lusin～108

Minlos～210

Minlos-Sazanov～206

Prohorov～134

Radon-Nikodym～45

Riesz表示～98

Tietze扩张～91

Tulcea～77

Tychonoff～110

Urysohn嵌入～96

Vitali-Hahn-Saks～47

von Neumann-Birkhoff 遍历～175

##### 九画

柱集 69

柱函数 214

相对紧的 134

相对熵 242

保测变换 174

信任函数 235

胎紧的(tight) 134

独立性 143

独立事件类 143

独立类的扩张 143

迹 205

迹算子 205

逆Bayes公式 148

诱导的拓扑 89

测度

~空间 8

~空间的完备化 15

~的限制 17

～的绝对连续，相互奇异 43

～的Lebesgue分解 44

～的乘积 71

～的弱收敛 128

～的淡收敛 128

～的分拆 163

～的支撑 43, 105

左(右)Haar ~ 120

正则的，内(外)正则的～ 101

对称Gauss ~ 216

引出的外～ 12

外～ 11

有限～，σ有限～ 8

强内正则的～ 101

随机～ 85

概率～ 8

符号～ 40

符号～的正部，负部 42

符号～的全变差 42

符号～的Jordan(Hahn)分解 42

变差～ 42

紧～ 80

像～ 37

模糊～ 222

Borel ~ 199

Gauss ~ 211

Gauss 柱～ 215

Gauss ~空间 216

Haar ~ 120

Lebesgue-Stieltjes ~ 17

Radon ~ 101

Radon乘积～ 109

##### 十画及以上

核, 概率核 74

核表示 87

容度 222

---

基本三元组 215

基本列 28

基本概率分配 235

焦元 236

原子 6

紧类 79

混合的 174

混合条件分布 160

停时 183

随机Daniell积分 85

随机元 135

随机变量 143

随机测度 85

弱可测，强可测 63

弱收敛 55

强收敛 51

乘积σ代数 68

乘积可测空间 68

乘积拓扑空间 110

遍历的 174

混合 175

提升 215

普遍可测集 117

数学期望 143

截口 70

简单函数 22

解析集 117, 177

特征函数 200

特征泛函 214

谱分解 205

置换不变σ代数 146

鞅，上(下)鞅 183

鞅变换 197

第一(二)可数性公理 89

第一(二)纲空间 95

模，超模 220

模函数 125

超可加 220

递减分布函数 220

联合熵 242

其他

Baire集, 强Baire集 97

Bayes公式 148

Bayes法则 156

Bochner积分 65

Borel 0-1律 145

Borel  $\sigma$代数 6, 99

 $C_{0}(X)$的对偶 105

 $C_{c}(X)$开集 96

Choquet  $\mathcal{F}$容度 179

Choque积分 223

Daniell积分 59

de Morgan 公式 1

Dunford-Pettis 弱紧性准则 167

Ellsberg 悖论 239

Fourier变换 199, 204

Hausdorff空间 90

Hevitt-Savage 0-1律 146

I可容 180

Kolmogorov 0-1律 146

Kolmogorov 强大数定律 190

Lebesgue可测 17

Lusin可测空间 117

Möbius反转 222

Pettis积分 66

 $\mathbb{P}$连续的 132

Radon-Nikodym导数 46

Radon可测空间 117

Radon乘积测度 111

r次平均收敛 51

Shannon熵 240

Shapley值 233

---

Snell包络 187  
Souslin可测空间 182  
T不变的 174  
Wald等式 196  
μ连续集 131  
μ可测集 11  
μ可测函数 33  
μ可分σ代数 52  
μ可积 34  
σ可加 8  
σ代数 3  
σ可积 154  
σ紧空间 90  
σ有限核 74  
σ有界集 98  
π类 3  
λ类 3  
λ族 26  
λ-模糊测度 225  
λ-期望 226  
∞-阶单调性 235  
∞-阶交替性 239