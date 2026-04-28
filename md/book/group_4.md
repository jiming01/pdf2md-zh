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