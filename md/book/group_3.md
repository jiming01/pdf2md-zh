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