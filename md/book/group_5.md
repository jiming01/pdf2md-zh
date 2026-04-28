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