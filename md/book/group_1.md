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