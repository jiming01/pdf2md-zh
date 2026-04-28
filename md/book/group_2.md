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