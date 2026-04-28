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

<div style="text-align: center;"><img src="imgs/img_in_chart_box_440_116_730_334.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;">图 2.22: 两次掷骰子点数之和的分布，即 $ p(y) $，其中 $ y = x_1 + x_2 $ 且 $ x_i \sim \text{Unif}(\{1, 2, \ldots, 6\}) $。图片来源于 https://en.wikipedia.org/wiki/Probability_distribution，经维基百科作者 Tim Stellmach 许可使用。</div>


我们可以将方程 $(2.170)$ 写成如下形式：

$$  p = p_{1} \circledast p_{2}   \tag*{(2.172)}$$

其中 $\otimes$ 表示卷积算子。对于有限长度向量，积分变为求和，卷积可以被视为一种“翻转并拖动”的操作，如表 2.4 所示。因此，方程 (2.170) 被称为卷积定理。

例如，假设我们掷两个骰子，那么 $p_1$ 和 $p_2$ 都是定义在 $\{1, 2, \ldots, 6\}$ 上的离散均匀分布。令 $y = x_1 + x_2$ 为骰子点数之和。我们有

$$  p(y=2) = p(x_{1}=1)p(x_{2}=1) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}   \tag*{(2.173)}$$

$$  p(y=3) = p(x_{1}=1)p(x_{2}=2) + p(x_{1}=2)p(x_{2}=1) = \frac{1}{6} \cdot \frac{1}{6} + \frac{1}{6} \cdot \frac{1}{6} = \frac{2}{36}   \tag*{(2.174)}$$

继续计算，我们得到 $p(y=4)=3/36$, $p(y=5)=4/36$, $p(y=6)=5/36$, $p(y=7)=6/36$, $p(y=8)=5/36$, $p(y=9)=4/36$, $p(y=10)=3/36$, $p(y=11)=2/36$ 以及 $p(y=12)=1/36$。其分布如图 2.22 所示。我们可以看到这个分布呈现高斯分布的形状；我们将在 2.8.6 节解释其原因。

我们也可以计算两个连续随机变量之和的概率密度函数。例如，对于高斯分布，当 $x_1 \sim \mathcal{N}(\boldsymbol{\mu}_1, \sigma_1^2)$ 且 $x_2 \sim \mathcal{N}(\boldsymbol{\mu}_2, \sigma_2^2)$ 时，可以证明（习题 2.4），若 $y = x_1 + x_2$，则

$$  p(y) = \mathcal{N}(x_{1}|\boldsymbol{\mu}_{1},\sigma_{1}^{2}) \otimes \mathcal{N}(x_{2}|\boldsymbol{\mu}_{2},\sigma_{2}^{2}) = \mathcal{N}(y|\boldsymbol{\mu}_{1}+\boldsymbol{\mu}_{2},\sigma_{1}^{2}+\sigma_{2}^{2})   \tag*{(2.176)}$$

因此，两个高斯分布的卷积仍然是高斯分布。

#### 2.8.6 中心极限定理

现在考虑 $N$ 个随机变量，其概率密度函数（不必是高斯分布）为 $p_n(x)$，每个变量的均值均为 $\mu$，方差均为 $\sigma^2$。我们假设每个变量是独立同分布的，简称 iid。

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_235_126_529_375.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_645_125_937_373.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 2.23：用图片展示中心极限定理。我们绘制了 $ \hat{\mu}_N^s = \frac{1}{N} \sum_{n=1}^N x_{ns} $ 的直方图，其中 $ x_{ns} \sim \mathrm{Beta}(1, 5) $， $ s = 1 : 10000 $。当 $ N \to \infty $ 时，分布趋向于高斯分布。(a) $ N = 1 $。(b) $ N = 5 $。改编自 [Bis06] 的图 2.6。由 centralLimitDemo.ipynb 生成。</div>


这意味着 $ X_n \sim p(X) $ 是从同一分布中独立抽取的样本。令 $ S_N = \sum_{n=1}^N X_n $ 为这些随机变量 (rv) 的和。可以证明，随着 $ N $ 增大，该和的分布趋近于

$$  p(S_{N}=u)=\frac{1}{\sqrt{2\pi N\sigma^{2}}}\exp\left(-\frac{(u-N\mu)^{2}}{2N\sigma^{2}}\right)   \tag*{(2.177)}$$

因此，量

$$  Z_{N}\triangleq\frac{S_{N}-N\mu}{\sigma\sqrt{N}}=\frac{\overline{X}-\mu}{\sigma/\sqrt{N}}   \tag*{(2.178)}$$

的分布收敛到标准正态分布，其中 $ \overline{X} = S_N/N $ 是样本均值。这被称为中心极限定理。证明可参见 [Jay03, p222] 或 [Ric95, p169]。

在 Figure 2.23 中，我们给出了一个例子，计算了从 Beta 分布中抽取的随机变量 (rv) 的样本均值。我们看到该均值的抽样分布迅速收敛到高斯分布。

#### 2.8.7 蒙特卡洛近似

假设 $ \boldsymbol{x} $ 是一个随机变量，$ \boldsymbol{y} = f(\boldsymbol{x}) $ 是 $ \boldsymbol{x} $ 的某个函数。通常难以解析计算诱导分布 $ p(\boldsymbol{y}) $。一种简单而强大的替代方法是，从 $ \boldsymbol{x} $ 的分布中抽取大量样本，然后使用这些样本（而不是分布）来近似 $ p(\boldsymbol{y}) $。

例如，假设 $ x \sim \text{Unif}(-1,1) $ 且 $ y = f(x) = x^2 $。我们可以通过从 $ p(x) $ 中抽取大量样本（使用均匀随机数生成器），对其进行平方，并计算得到的经验分布来近似 $ p(y) $，该经验分布由下式给出：

$$  p_{S}(y)\triangleq\frac{1}{N_{s}}\sum_{s=1}^{N_{s}}\delta(y-y_{s})   \tag*{(2.179)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_243_135_917_398.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">图 2.24：计算 $y = x^{2}$ 的分布，其中 $p(x)$ 是均匀分布（左图）。中间为解析结果，右侧为蒙特卡洛近似。由 change_of_vars_demo1d.ipynb 生成。</div>


这只是一个等权的“尖峰之和”，每个尖峰以其中一个样本为中心（见第 2.7.6 节）。通过使用足够多的样本，我们可以相当好地近似 $p(y)$。图 2.24 展示了这一过程。

这种方法被称为分布的蒙特卡洛近似（Monte Carlo approximation）。（“蒙特卡洛”一词来源于摩纳哥著名的赌场名称。）蒙特卡洛技术最初在统计物理学领域发展起来——特别是在原子弹研制过程中——但现在也广泛应用于统计学和机器学习。更多细节可参见本书的续篇 [Mur23]，以及该主题的专著，例如 [Liu01; RC04; KTB11; BZ20]。

### 2.9 练习

练习 2.1 [条件独立 $ \dagger $]

（来源：Koller。）

a. 令 $H \in \{1, \ldots, K\}$ 为一个离散随机变量，$e_1$ 和 $e_2$ 是另外两个随机变量 $E_1$ 和 $E_2$ 的观测值。假设我们希望计算向量

 $$ \vec{P}(H|e_{1},e_{2})=(P(H=1|e_{1},e_{2}),\ldots,P(H=K|e_{1},e_{2})) $$ 

以下哪组数字足以进行计算？

i.  $P(e_{1}, e_{2}), P(H), P(e_{1}|H), P(e_{2}|H)$

ii.  $P(e_{1}, e_{2}), P(H), P(e_{1}, e_{2}|H)$

iii.  $P(e_1|H)$, $P(e_2|H)$, $P(H)$

b. 现在假设 $E_1 \perp E_2|H$（即 $E_1$ 和 $E_2$ 在给定 $H$ 时条件独立）。那么上述三组中哪一组现在足够了？

请展示您的计算过程并给出最终结果。提示：使用贝叶斯规则。

练习 2.2 [两两独立不意味着相互独立]

如果满足下式，我们称两个随机变量是两两独立的：

$$  p(X_{2}|X_{1})=p(X_{2})   \tag*{(2.180)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

因此

$$  p(X_{2},X_{1})=p(X_{1})p(X_{2}|X_{1})=p(X_{1})p(X_{2})   \tag*{(2.181)}$$

我们说 \(n\) 个随机变量相互独立，如果

$$  p(X_{i}|X_{S})=p(X_{i})\quad\forall S\subseteq\{1,\ldots,n\}\setminus\{i\}   \tag*{(2.182)}$$

因此

$$  p(X_{1:n})=\prod_{i=1}^{n}p(X_{i})   \tag*{(2.183)}$$

证明所有变量对之间的两两独立并不一定意味着相互独立。给出一个反例即可。

##### 习题 2.3 [条件独立当且仅当联合概率可分解  $ \dagger $]

在正文中，我们说 \(X \perp Y \mid Z\) 当且仅当

$$  p(x,y|z)=p(x|z)p(y|z)   \tag*{(2.184)}$$

对于所有满足 \(p(z) > 0\) 的 \(x, y, z\)。现在证明如下等价定义：\(X \perp Y \mid Z\) 当且仅当存在函数 \(g\) 和 \(h\) 使得

$$  p(x,y|z)=g(x,z)h(y,z)   \tag*{(2.185)}$$

对于所有满足 \(p(z) > 0\) 的 \(x, y, z\)。

##### 习题 2.4 [两个高斯分布的卷积是高斯分布]

证明两个高斯分布的卷积是高斯分布，即

$$  p(y)=\mathcal{N}(x_{1}|\mu_{1},\sigma_{1}^{2})\otimes\mathcal{N}(x_{2}|\mu_{2},\sigma_{2}^{2})=\mathcal{N}(y|\mu_{1}+\mu_{2},\sigma_{1}^{2}+\sigma_{2}^{2})   \tag*{(2.186)}$$

其中 \(y = x_1 + x_2\)，\(x_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)\) 和 \(x_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)\) 是独立的随机变量。

##### 习题 2.5 [两个随机变量最小值期望 †]

假设 \(X, Y\) 是从区间 \([0,1]\) 上独立且均匀随机采样的两个点。最左边点的期望位置是多少？

##### 习题 2.6 [和的方差]

证明和的方差为

$$  \mathbb{V}\left[X+Y\right]=\mathbb{V}\left[X\right]+\mathbb{V}\left[Y\right]+2\operatorname{Cov}\left[X,Y\right],   \tag*{(2.187)}$$

其中 \(\operatorname{Cov}[X,Y]\) 是 \(X\) 和 \(Y\) 之间的协方差。

##### 习题 2.7 [推导逆伽马密度 \( \dagger \)]

设 \(X \sim \mathrm{Ga}(a,b)\)，且 \(Y = 1/X\)。推导 \(Y\) 的分布。

##### 习题 2.8 [Beta分布的均值、众数、方差]

假设 \(\theta \sim \text{Beta}(a, b)\)。证明均值、众数和方差由下式给出

$$  \mathbb{E}\left[\theta\right]=\frac{a}{a+b}   \tag*{(2.188)}$$

$$  \mathbb{V}\left[\boldsymbol{\theta}\right]=\frac{ab}{(a+b)^{2}(a+b+1)}   \tag*{(2.189)}$$

$$  \text{mode}\left[\boldsymbol{\theta}\right]=\frac{a-1}{a+b-2}   \tag*{(2.190)}$$

《概率机器学习：导论》。在线版本。2024年11月23日。

---

##### 习题 2.9 [医学诊断中的贝叶斯法则 †]

每年体检后，医生带来了坏消息和好消息。坏消息是你的某项严重疾病检测结果呈阳性，并且该检测的准确率为99%（即，如果你患有该疾病，检测呈阳性的概率为0.99；如果你未患病，检测呈阴性的概率同样为0.99）。好消息是这是一种罕见疾病，发病率仅为万分之一。那么你实际患病的概率是多少？（请展示你的计算过程并给出最终结果。）

##### 习题 2.10 [法律推理]

（来源：Peter Lee.）假设发生了一起犯罪。现场发现了一些血液，且无法给出合理解释。该血型在人口中的出现概率为1%。

a. 检察官声称：“如果被告是无辜的，那么他拥有犯罪血型的概率为1%。因此，他有99%的概率是有罪的。”这被称为检察官谬误。这一论证错在哪里？

b. 辩护律师声称：“犯罪发生在一个有80万人口的城市。该血型大约存在于8000人身上。该证据表明被告有罪的概率仅为1/8000，因此与本案无关。”这被称为辩护律师谬误。这一论证错在哪里？

##### 习题 2.11 [概率对提问方式敏感 †]

（来源：Minka.）我的邻居有两个孩子。假设孩子的性别像抛硬币一样独立等可能，那么先验地，邻居最可能有一男一女，概率为1/2。其他可能性——两个男孩或两个女孩——的概率分别为1/4和1/4。

a. 假设我问他是否有男孩，他回答有。那么其中一个孩子是女孩的概率是多少？

b. 假设我碰巧看到他的一个孩子跑过，是个男孩。那么另一个孩子是女孩的概率是多少？

##### 习题 2.12 [一维高斯分布的归一化常数]

零均值高斯分布的归一化常数由下式给出

$$  Z=\int_{a}^{b}\exp\left(-\frac{x^{2}}{2\sigma^{2}}\right)dx   \tag*{(2.191)}$$

其中 $ a = -\infty $ 且 $ b = \infty $。

为了计算该积分，考虑其平方

$$  Z^{2}=\int_{a}^{b}\int_{a}^{b}\exp\left(-\frac{x^{2}+y^{2}}{2\sigma^{2}}\right)dxdy   \tag*{(2.192)}$$

让我们从笛卡尔坐标 $ (x,y) $ 转换到极坐标 $ (r,\theta) $，利用 $ x = r \cos \theta $ 和 $ y = r \sin \theta $。由于 $ dxdy = rdrd\theta $，且 $ \cos^2\theta + \sin^2\theta = 1 $，我们有

$$  Z^{2}=\int_{0}^{2\pi}\int_{0}^{\infty}r\exp\left(-\frac{r^{2}}{2\sigma^{2}}\right)d r d\theta   \tag*{(2.193)}$$

计算该积分，并由此证明 $ Z = \sqrt{\sigma^2}2\pi $。提示1：将积分分解为两个项的乘积，第一个项（涉及 $ d\theta $）是常数，因此容易处理。提示2：如果 $ u = e^{-r^2/2\sigma^2} $，则 $ du/dr = -\frac{1}{\sigma^2}re^{-r^2/2\sigma^2} $，因此第二个积分也很容易（因为 $ \int u'(r)dr = u(r) $）。

---



---

## 3 概率：多元模型

### 3.1 多个随机变量的联合分布

在本节中，我们讨论衡量一个或多个变量之间相互依赖关系的各种方法。

#### 3.1.1 协方差

两个随机变量 X 和 Y 之间的协方差衡量了 X 和 Y 之间（线性）相关程度。协方差定义为

$$  \mathrm{Cov}\left[X,Y\right]\triangleq\mathbb{E}\left[\left(X-\mathbb{E}\left[X\right]\right)\left(Y-\mathbb{E}\left[Y\right]\right)\right]=\mathbb{E}\left[XY\right]-\mathbb{E}\left[X\right]\mathbb{E}\left[Y\right]   \tag*{(3.1)}$$

如果 x 是一个 D 维随机向量，其协方差矩阵定义为以下对称半正定矩阵：

$$  \begin{aligned}\operatorname{Cov}\left[\boldsymbol{x}\right]&\triangleq\mathbb{E}\left[\left(\boldsymbol{x}-\mathbb{E}\left[\boldsymbol{x}\right]\right)(\boldsymbol{x}-\mathbb{E}\left[\boldsymbol{x}\right])^{\mathsf{T}}\right]\triangleq\boldsymbol{\Sigma}\\&=\begin{pmatrix}\mathbb{V}\left[X_{1}\right]&\operatorname{Cov}\left[X_{1},X_{2}\right]&\cdots&\operatorname{Cov}\left[X_{1},X_{D}\right]\\\operatorname{Cov}\left[X_{2},X_{1}\right]&\mathbb{V}\left[X_{2}\right]&\cdots&\operatorname{Cov}\left[X_{2},X_{D}\right]\\\vdots&\vdots&\ddots&\vdots\\\operatorname{Cov}\left[X_{D},X_{1}\right]&\operatorname{Cov}\left[X_{D},X_{2}\right]&\cdots&\mathbb{V}\left[X_{D}\right]\end{pmatrix}\end{aligned}   \tag*{(3.3)}$$

由此我们得到重要结果

$$  \mathbb{E}\left[\boldsymbol{x}\boldsymbol{x}^{\mathsf{T}}\right]=\boldsymbol{\Sigma}+\boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf{T}}   \tag*{(3.4)}$$

另一个有用的结果是，线性变换的协方差由下式给出

$$  \mathrm{Cov}\left[\mathbf{A}\boldsymbol{x}+\boldsymbol{b}\right]=\mathbf{A}\mathrm{Cov}\left[\boldsymbol{x}\right]\mathbf{A}^{\mathrm{T}}   \tag*{(3.5)}$$

如练习 3.4 所示。

两个随机向量之间的互协方差定义为

$$  \mathrm{Cov}\left[\boldsymbol{x},\boldsymbol{y}\right]=\mathbb{E}\left[\left(\boldsymbol{x}-\mathbb{E}\left[\boldsymbol{x}\right]\right)(\boldsymbol{y}-\mathbb{E}\left[\boldsymbol{y}\right])^{\mathrm{T}}\right]   \tag*{(3.6)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_330_115_837_337.jpg" alt="图像" width="44%" /></div>


<div style="text-align: center;">图 3.1：几组 $ (x,y) $ 点集，每组均标有 x 与 y 的相关系数。注意，相关系数反映线性关系的噪声程度和方向（顶行），但不反映该关系的斜率（中间行），也不反映非线性关系的许多方面（底行）。（注：中心图的斜率为 0，但此时相关系数未定义，因为 Y 的方差为零。）引自 https://en.wikipedia.org/wiki/Pearson_correlation_coefficient。经维基百科作者 Imagecreator 许可使用。</div>


#### 3.1.2 相关性

协方差可以介于负无穷和正无穷之间。有时使用一种归一化的度量更为方便，该度量具有有限的下界和上界。X 与 Y 之间的（皮尔逊）相关系数定义为

$$  \rho\triangleq\mathrm{corr}\left[X,Y\right]\triangleq\frac{\mathrm{Cov}\left[X,Y\right]}{\sqrt{\mathbb{V}\left[X\right]\mathbb{V}\left[Y\right]}}   \tag*{(3.7)}$$

可以证明（练习 3.2）$ -1 \leq \rho \leq 1 $。

还可以证明，$ \mathrm{corr}[X,Y]=1 $ 当且仅当对于某些参数 $ a $ 和 $ b $，有 $ Y=aX+b $（且 $ a>0 $），即 X 与 Y 之间存在线性关系（见练习 3.3）。直观上，人们可能认为相关系数与回归线的斜率有关，即表达式 $ Y=aX+b $ 中的系数 $ a $。然而，正如我们在方程 (11.27) 中所示，回归系数实际上由 $ a=\text{Cov}[X,Y]/\mathbb{V}[X] $ 给出。在图 3.1 中，我们展示了在强但非线性的关系中，相关系数可能为 0。（与图 6.6 比较。）因此，将相关系数理解为线性程度的一种度量更为恰当。（参见 correlation2d.ipynb 的演示以说明这一概念。）

对于由相关随机变量组成的向量 x，其相关矩阵定义为

$$  \mathrm{corr}(\boldsymbol{x})=\begin{pmatrix}1&\frac{\mathbb{E}\left[\left(X_{1}-\mu_{1}\right)\left(X_{2}-\mu_{2}\right)\right]}{\sigma_{1}\sigma_{2}}&\cdots&\frac{\mathbb{E}\left[\left(X_{1}-\mu_{1}\right)\left(X_{D}-\mu_{D}\right)\right]}{\sigma_{1}\sigma_{D}}\\\frac{\mathbb{E}\left[\left(X_{2}-\mu_{2}\right)\left(X_{1}-\mu_{1}\right)\right]}{\sigma_{2}\sigma_{1}}&1&\cdots&\frac{\mathbb{E}\left[\left(X_{2}-\mu_{2}\right)\left(X_{D}-\mu_{D}\right)\right]}{\sigma_{2}\sigma_{D}}\\\vdots&\vdots&\ddots&\vdots\\\frac{\mathbb{E}\left[\left(X_{D}-\mu_{D}\right)\left(X_{1}-\mu_{1}\right)\right]}{\sigma_{D}\sigma_{1}}&\frac{\mathbb{E}\left[\left(X_{D}-\mu_{D}\right)\left(X_{2}-\mu_{2}\right)\right]}{\sigma_{D}\sigma_{2}}&\cdots&1\end{pmatrix}   \tag*{(3.8)}$$

这可以更紧凑地写为

$$  \mathrm{corr}(\boldsymbol{x})=(\mathrm{diag}(\mathbf{K}_{xx}))^{-\frac{1}{2}}\mathbf{K}_{xx}(\mathrm{diag}(\mathbf{K}_{xx}))^{-\frac{1}{2}}   \tag*{(3.9)}$$

“概率机器学习：导论”。在线版本。2024 年 11 月 23 日

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_285_123_893_468.jpg" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 3.2：因果无关时间序列之间虚假相关性的示例。冰淇淋消费量（红色）与暴力犯罪率（黄色）随时间变化。数据来源：http://icbseverywhere.com/blog/2014/10/the-logic-of-causal-conclusions/。经 Barbara Drescher 许可使用。</div>


其中 $K_{xx}$ 是自协方差矩阵

$$ \mathbf{K}_{x x}=\boldsymbol{\Sigma}=\mathbb{E}\left[(\boldsymbol{x}-\mathbb{E}\left[\boldsymbol{x}\right])(\boldsymbol{x}-\mathbb{E}\left[\boldsymbol{x}\right])^{\mathsf{T}}\right]=\mathbf{R}_{x x}-\boldsymbol{\mu}\boldsymbol{\mu}^{\mathsf{T}} \tag*{(3.10)}$$

而 $\mathbf{R}_{xx} = \mathbb{E}\left[\boldsymbol{x}\boldsymbol{x}^{\top}\right]$ 是自相关矩阵。

#### 3.1.3 不相关并不意味着独立

如果 $X$ 与 $Y$ 独立，即 $p(X,Y) = p(X)p(Y)$，那么 $\text{Cov}[X,Y] = 0$，从而 $\text{corr}[X,Y] = 0$。因此，独立意味着不相关。然而，反之不成立：不相关并不意味着独立。例如，设 $X \sim U(-1,1)$，$Y = X^2$。显然 $Y$ 依赖于 $X$（实际上，$Y$ 由 $X$ 唯一确定），但可以证明（练习 3.1）$\text{corr}[X,Y] = 0$。图 3.1 展示了这一事实的一些显著例子。其中多个数据集显示 $X$ 与 $Y$ 之间存在明显的依赖关系，但相关系数却为 0。衡量随机变量间依赖关系的一个更通用的度量是互信息，将在第 6.3 节讨论。只有当变量真正独立时，互信息才为零。

#### 3.1.4 相关并不意味着因果

众所周知，“相关并不意味着因果”。例如，考虑图 3.2。红色曲线绘制的是 $x_{1:T}$，其中 $x_t$ 是第 $t$ 个月的冰淇淋销售量；黄色曲线绘制的是 $y_{1:T}$，其中 $y_t$ 是第 $t$ 个月的暴力犯罪率（数值已重新缩放以使曲线重叠）。我们看到这些信号之间存在强相关。事实上，有时有人声称“吃冰淇淋会导致谋杀”[Pet13]。当然，这只是一个虚假的相关性，源于一个隐藏的共同原因——天气。显而易见，炎热天气会增加冰淇淋的销量。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_150_114_1017_297.jpg" alt="图片" width="75%" /></div>


<div style="text-align: center;">图3.3：辛普森悖论在鸢尾花数据集上的图示。（左）总体而言，y（花萼宽度）随x（花萼长度）增加而减小。（右）在每个组内，y随x增加而增加。由simpsons_paradox.ipynb生成。</div>


原因。炎热天气也会增加暴力犯罪；其原因存在激烈争议；一些人声称这是由于愤怒情绪增加[And01]，但另一些人则认为只是因为更多人在户外活动[Ash18]，而大多数谋杀案发生在户外。

另一个著名的例子涉及出生率与鹳鸟（一种鸟）数量之间的正相关。这催生了关于鹳鸟送子的都市传说[Mat00]。当然，这种相关性的真正原因更可能是由于隐藏因素，如生活水平提高导致食物增多。在[Vig15]中可以找到更多关于这种虚假相关性的有趣例子。

这些例子起到了“警示”作用，即我们不应将x预测y的能力视为x导致y的指示。

#### 3.1.5 辛普森悖论

辛普森悖论指出，出现在多个不同数据组中的统计趋势或关系，当这些组合并时可能会消失或逆转符号。如果我们以因果方式误解统计依赖性的主张，就会导致违反直觉的行为。

该悖论的可视化如图3.3所示。总体来看，y随x增加而减小，但在每个子群体内，y随x增加而增加。

关于COVID-19背景下辛普森悖论的最新真实案例，请参见图3.4(a)。该图显示，在每个年龄组中，意大利的COVID-19病死率（CFR）低于中国，但总体却更高。其原因在于意大利老年人更多，如图3.4(b)所示。换言之，图3.4(a)展示了 \( p(F=1|A,C) \)，其中A为年龄，C为国家，F=1为死于COVID-19的事件；图3.4(b)展示了 \( p(A|C) \)，即国家C中年龄组A的概率。综合这两者，我们得到 \( p(F=1|C=\text{Italy}) > p(F=1|C=\text{China}) \)。详情请参见[KGS20]。

### 3.2 多元高斯（正态）分布

连续随机变量最常用的联合概率分布是多元高斯分布或多元正态分布（MVN）。这主要因为其在数学上方便处理，同时也因为高斯假设在许多情况下相当合理（参见第2.6.4节的讨论）。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_219_122_545_334.jpg" alt="图像" width="50%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_625_121_953_334.jpg" alt="图像" width="50%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 3.4：利用 COVID-19 说明辛普森悖论。(a) 按年龄组划分的意大利和中国的病死率（CFR），以及截至报告时间（见图例）的汇总形式（“总计”，最后一对柱状条）。(b) 按国家划分的每个年龄组中纳入 (a) 的确诊病例比例。来自 [KGS20] 的图 1。经 Julius von Kügelgen 许可使用。</div>


#### 3.2.1 定义

多元正态分布（MVN）密度定义如下：

$$  \mathcal{N}(\boldsymbol{y}|\boldsymbol{\mu},\boldsymbol{\Sigma})\triangleq\frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\left[-\frac{1}{2}(\boldsymbol{y}-\boldsymbol{\mu})^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{y}-\boldsymbol{\mu})\right]   \tag*{(3.11)}$$

其中 $ \boldsymbol{\mu} = \mathbb{E}[\boldsymbol{y}] \in \mathbb{R}^D $ 是均值向量，$ \boldsymbol{\Sigma} = \operatorname{Cov}[\boldsymbol{y}] $ 是 $ D \times D $ 的协方差矩阵，定义如下：

$$  \mathrm{Cov}\left[\boldsymbol{y}\right]\triangleq\mathbb{E}\left[\left(\boldsymbol{y}-\mathbb{E}\left[\boldsymbol{y}\right]\right)\left(\boldsymbol{y}-\mathbb{E}\left[\boldsymbol{y}\right]\right)^{\mathrm{T}}\right]   \tag*{(3.12)}$$

$$  \begin{aligned}=\begin{pmatrix}\mathbb{V}\left[Y_{1}\right]&\operatorname{Cov}\left[Y_{1},Y_{2}\right]&\cdots&\operatorname{Cov}\left[Y_{1},Y_{D}\right]\\\operatorname{Cov}\left[Y_{2},Y_{1}\right]&\mathbb{V}\left[Y_{2}\right]&\cdots&\operatorname{Cov}\left[Y_{2},Y_{D}\right]\\\vdots&\vdots&\ddots&\vdots\\\operatorname{Cov}\left[Y_{D},Y_{1}\right]&\operatorname{Cov}\left[Y_{D},Y_{2}\right]&\cdots&\mathbb{V}\left[Y_{D}\right]\end{pmatrix}\end{aligned}   \tag*{(3.13)}$$

其中

$$  \mathrm{Cov}\left[Y_{i},Y_{j}\right]\triangleq\mathbb{E}\left[\left(Y_{i}-\mathbb{E}\left[Y_{i}\right]\right)\left(Y_{j}-\mathbb{E}\left[Y_{j}\right]\right)\right]=\mathbb{E}\left[Y_{i}Y_{j}\right]-\mathbb{E}\left[Y_{i}\right]\mathbb{E}\left[Y_{j}\right]   \tag*{(3.14)}$$

且 $ \mathbb{V}[Y_i] = \text{Cov}[Y_i, Y_i] $。由方程 (3.12) 可得重要结果

$$  \mathbb{E}\left[y y^{\mathsf{T}}\right]=\Sigma+\mu\mu^{\mathsf{T}}   \tag*{(3.15)}$$

方程 (3.11) 中的归一化常数 $  Z = (2\pi)^{D/2}|\Sigma|^{1/2}  $ 仅用于确保概率密度函数积分为 1（参见练习 3.6）。

在二维情况下，MVN 称为二元高斯分布。其概率密度函数可表示为 $ y \sim \mathcal{N}(\mu, \Sigma) $，其中 $ y \in \mathbb{R}^2 $，$ \mu \in \mathbb{R}^2 $，且

$$  \mathbf{\Sigma}=\begin{pmatrix}\sigma_{1}^{2}&\rho\sigma_{1}\sigma_{2}\\ \rho\sigma_{1}\sigma_{2}&\sigma_{2}^{2}\end{pmatrix}   \tag*{(3.16)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_189_119_455_326.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_466_120_728_327.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_745_120_1009_327.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 3.5: 二维高斯密度作为曲面图的直观展示。(a) 使用全协方差矩阵的分布可以朝任意方向倾斜。(b) 使用对角协方差矩阵的分布必须平行于坐标轴。(c) 使用球形协方差矩阵的分布必须具有对称形状。由 gauss_plot_2d.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_198_499_442_706.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_477_496_722_704.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_782_499_977_704.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 3.6: 二维高斯密度在恒定概率密度等高线下的可视化。(a) 全协方差矩阵具有椭圆等高线。(b) 对角协方差矩阵是轴向对齐的椭圆。(c) 球形协方差矩阵具有圆形形状。由 gauss_plot_2d.ipymb 生成。</div>


其中 $ \rho $ 是相关系数，定义如下：

$$  \mathrm{corr}\left[Y_{1},Y_{2}\right]\triangleq\frac{\mathrm{Cov}\left[Y_{1},Y_{2}\right]}{\sqrt{\mathbb{V}\left[Y_{1}\right]\mathbb{V}\left[Y_{2}\right]}}=\frac{\sigma_{12}^{2}}{\sigma_{1}\sigma_{2}}   \tag*{(3.17)}$$

可以证明（练习 3.2）$ -1 \leq \text{corr}[Y_1, Y_2] \leq 1 $。将二元情况下的概率密度函数展开，会得到以下看似复杂的表达式：

$$  \begin{aligned}p(y_{1},y_{2})&=\frac{1}{2\pi\sigma_{1}\sigma_{2}\sqrt{1-\rho^{2}}}\exp\left(-\frac{1}{2(1-\rho^{2})}\times\right.\\&\left.\left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2\rho\frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}}\frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right)\end{aligned}   \tag*{(3.18)}$$

---

对称的。（椭圆形状的原因将在第7.4.4节中解释，届时我们将讨论二次型的几何形状。）对角协方差矩阵有 $D$ 个参数，且非对角线项为零。球面协方差矩阵（也称为各向同性协方差矩阵）的形式为 $\mathbf{\Sigma} = \sigma^2 \mathbf{I}_D$，因此它只有一个自由参数，即 $\sigma^2$。

#### 3.2.2 马氏距离

在本节中，我们试图深入理解多维高斯概率密度函数的几何形状。为此，我们将考察常数（对数）概率的等高线形状。

特定点 $\boldsymbol{y}$ 的对数概率由下式给出：

$$  \log p(\boldsymbol{y}|\boldsymbol{\mu},\boldsymbol{\Sigma})=-\frac{1}{2}(\boldsymbol{y}-\boldsymbol{\mu})^{\mathrm{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{y}-\boldsymbol{\mu})+\mathrm{c o n s t}   \tag*{(3.19)}$$

对 $\boldsymbol{y}$ 的依赖可以通过 $\boldsymbol{y}$ 与 $\boldsymbol{\mu}$ 之间的马氏距离 $\Delta$ 来表示，其平方定义如下：

$$  \Delta^{2}\triangleq(\boldsymbol{y}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\boldsymbol{y}-\boldsymbol{\mu})   \tag*{(3.20)}$$

因此，常数（对数）概率的等高线等价于常数马氏距离的等高线。

为了深入理解常数马氏距离的等高线，我们利用 $\boldsymbol{\Sigma}$（进而 $\mathbf{\Lambda} = \boldsymbol{\Sigma}^{-1}$）都是正定矩阵这一事实（根据假设）。考虑 $\boldsymbol{\Sigma}$ 的如下特征分解（第7.4节）：

$$  \mathbf{\Sigma}=\sum_{d=1}^{D}\lambda_{d}\mathbf{u}_{d}\mathbf{u}_{d}^{\top}   \tag*{(3.21)}$$

类似地，我们可以写出

$$  \mathbf{\Sigma}^{-1}=\sum_{d=1}^{D}\frac{1}{\lambda_{d}}\mathbf{u}_{d}\mathbf{u}_{d}^{\mathsf{T}}   \tag*{(3.22)}$$

定义 $ z_d \triangleq \boldsymbol{u}_d^\top(\boldsymbol{y} - \boldsymbol{\mu}) $，因此 $ \boldsymbol{z} = \boldsymbol{U}(\boldsymbol{y} - \boldsymbol{\mu}) $。于是我们可以将马氏距离重写如下：

$$  \begin{align*}(\boldsymbol{y}-\boldsymbol{\mu})^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{y}-\boldsymbol{\mu})&=(\boldsymbol{y}-\boldsymbol{\mu})^{\mathsf{T}}\left(\sum_{d=1}^{D}\frac{1}{\lambda_{d}}\boldsymbol{u}_{d}\boldsymbol{u}_{d}^{\mathsf{T}}\right)(\boldsymbol{y}-\boldsymbol{\mu})\\&=\sum_{d=1}^{D}\frac{1}{\lambda_{d}}(\boldsymbol{y}-\boldsymbol{\mu})^{\mathsf{T}}\boldsymbol{u}_{d}\boldsymbol{u}_{d}^{\mathsf{T}}(\boldsymbol{y}-\boldsymbol{\mu})=\sum_{d=1}^{D}\frac{z_{d}^{2}}{\lambda_{d}}\end{align*}   \tag*{(3.23)}$$

如第7.4.4节所述，这意味着我们可以将马氏距离解释为在新坐标系 $\boldsymbol{z}$ 中的欧氏距离，在该坐标系中，我们通过 $\boldsymbol{U}$ 旋转 $\boldsymbol{y}$ 并通过 $\boldsymbol{\Lambda}$ 进行缩放。

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可协议。

---

例如，在二维空间中，考虑满足如下方程的点集 $ (z_{1}, z_{2}) $：

$$  \frac{z_{1}^{2}}{\lambda_{1}}+\frac{z_{2}^{2}}{\lambda_{2}}=r   \tag*{(3.25)}$$

由于这些点具有相同的马氏距离，它们对应于等概率点。因此我们看到，二维高斯分布的等概率密度等高线沿椭圆分布。如图7.6所示。特征向量决定椭圆的方向，特征值决定椭圆的扁率。

#### 3.2.3 多元正态分布的边际与条件 $ ^{*} $

假设 $ \boldsymbol{y} = (\boldsymbol{y}_{1}, \boldsymbol{y}_{2}) $ 联合服从高斯分布，其参数为

$$  \boldsymbol{\mu}=\begin{pmatrix}\boldsymbol{\mu}_{1}\\ \boldsymbol{\mu}_{2}\end{pmatrix},\quad\boldsymbol{\Sigma}=\begin{pmatrix}\boldsymbol{\Sigma}_{11}&\boldsymbol{\Sigma}_{12}\\ \boldsymbol{\Sigma}_{21}&\boldsymbol{\Sigma}_{22}\end{pmatrix},\quad\boldsymbol{\Lambda}=\boldsymbol{\Sigma}^{-1}=\begin{pmatrix}\boldsymbol{\Lambda}_{11}&\boldsymbol{\Lambda}_{12}\\ \boldsymbol{\Lambda}_{21}&\boldsymbol{\Lambda}_{22}\end{pmatrix}   \tag*{(3.26)}$$

其中 $ \Lambda $ 是精度矩阵。则边际分布为

$$  \begin{aligned}{}&{{}}\\ {}&{{}}\\ {}&{{}}\\ \end{aligned}\begin{aligned}{p(\mathbf{y}_{1})}&{{}=\mathcal{N}(\mathbf{y}_{1}|\mathbf{\mu}_{1},\mathbf{\Sigma}_{11})}\\ {p(\mathbf{y}_{2})}&{{}=\mathcal{N}(\mathbf{y}_{2}|\mathbf{\mu}_{2},\mathbf{\Sigma}_{22})}\\ \end{aligned}   \tag*{(3.27)}$$

后验条件分布为

$$  \begin{aligned}{p(\mathbf{y}_{1}|\mathbf{y}_{2})}&{{}=\mathcal{N}(\mathbf{y}_{1}|\mathbf{\mu}_{1|2},\mathbf{\Sigma}_{1|2})}\\ {\mathbf{\mu}_{1|2}}&{{}=\mathbf{\mu}_{1}+\mathbf{\Sigma}_{12}\mathbf{\Sigma}_{22}^{-1}(\mathbf{y}_{2}-\mathbf{\mu}_{2})}\\ {}&{{}=\mathbf{\mu}_{1}-\mathbf{\Lambda}_{11}^{-1}\mathbf{\Lambda}_{12}(\mathbf{y}_{2}-\mathbf{\mu}_{2})}\\ {}&{{}=\mathbf{\Sigma}_{1|2}\left(\mathbf{\Lambda}_{11}\mathbf{\mu}_{1}-\mathbf{\Lambda}_{12}(\mathbf{y}_{2}-\mathbf{\mu}_{2})\right)}\\ {\mathbf{\Sigma}_{1|2}}&{{}=\mathbf{\Sigma}_{11}-\mathbf{\Sigma}_{12}\mathbf{\Sigma}_{22}^{-1}\mathbf{\Sigma}_{21}=\mathbf{\Lambda}_{11}^{-1}}\\ \end{aligned}   \tag*{(3.28)}$$

这些方程在本书中至关重要，因此我们用方框将它们框起来，以便您以后轻松找到它们。关于这些结果的推导（依赖于计算舒尔补 $ \Sigma/\Sigma_{22} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21} $），请参见 Section 7.3.5。

我们看到边际分布和条件分布本身都是高斯分布。对于边际分布，我们只需提取对应于 $ y_{1} $ 或 $ y_{2} $ 的行和列。对于条件分布，我们需要多做一些工作。然而，这并不复杂：条件均值仅是 $ y_{2} $ 的线性函数，条件协方差则是一个与 $ y_{2} $ 无关的常数矩阵。我们给出了后验均值的三种不同（但等价）表达式，以及后验协方差的两种不同（但等价）表达式；每种表达式在不同的情况下都有用。

---

#### 3.2.4 示例：二维高斯分布的条件化

考虑一个二维示例。协方差矩阵为

$$  \mathbf{\Sigma}=\begin{pmatrix}\sigma_{1}^{2}&\rho\sigma_{1}\sigma_{2}\\ \rho\sigma_{1}\sigma_{2}&\sigma_{2}^{2}\end{pmatrix}   \tag*{(3.29)}$$

边缘分布 $ p(y_{1}) $ 是一维高斯分布，通过将联合分布投影到 $ y_{1} $ 轴上得到：

$$  p(y_{1})=\mathcal{N}(y_{1}|\mu_{1},\sigma_{1}^{2})   \tag*{(3.30)}$$

假设我们观测到 $ Y_2 = y_2 $，则条件分布 $ p(y_1 | y_2) $ 通过对联合分布沿 $ Y_2 = y_2 $ 线进行“切片”得到：

$$  p(y_{1}|y_{2})=\mathcal{N}\left(y_{1}|\mu_{1}+\frac{\rho\sigma_{1}\sigma_{2}}{\sigma_{2}^{2}}(y_{2}-\mu_{2}),\sigma_{1}^{2}-\frac{(\rho\sigma_{1}\sigma_{2})^{2}}{\sigma_{2}^{2}}\right)   \tag*{(3.31)}$$

如果 $ \sigma_{1} = \sigma_{2} = \sigma $，则得到

$$  p(y_{1}|y_{2})=\mathcal{N}\left(y_{1}|\mu_{1}+\rho(y_{2}-\mu_{2}),\sigma^{2}(1-\rho^{2})\right)   \tag*{(3.32)}$$

例如，假设 $ \rho = 0.8 $，$ \sigma_1 = \sigma_2 = 1 $，$ \mu_1 = \mu_2 = 0 $，且 $ y_2 = 1 $。我们看到 $ \mathbb{E}[y_1 | y_2 = 1] = 0.8 $，这很合理，因为 $ \rho = 0.8 $ 意味着如果 $ y_2 $ 增加 1（超过其均值），则 $ y_1 $ 增加 0.8。我们还看到 $ \mathbb{V}[y_1 | y_2 = 1] = 1 - 0.8^2 = 0.36 $。这也很有道理：我们对 $ y_1 $ 的不确定性降低了，因为通过观测 $ y_2 $（间接地）我们学到了一些关于 $ y_1 $ 的信息。如果 $ \rho = 0 $，则得到 $ p(y_1 | y_2) = \mathcal{N}(y_1 | \mu_1, \sigma_1^2) $，因为若 $ y_2 $ 与 $ y_1 $ 不相关（从而独立），则 $ y_2 $ 不传递任何关于 $ y_1 $ 的信息。

#### 3.2.5 示例：缺失值插补 *

作为上述结果的一个应用示例，假设我们观测到了 $\mathbf{y}$ 的一部分（某些维度），而其余部分缺失或未观测到。我们可以利用维度之间的相关性（由协方差矩阵编码）来推断缺失的条目；这被称为**缺失值插补**。

图 3.7 展示了一个简单示例。我们从 $D = 8$ 维高斯分布中采样了 $N = 10$ 个向量，然后故意“隐藏”了 50% 的数据。接着，根据观测到的条目和真实模型参数来推断缺失的条目。$^1$ 更精确地说，对于数据矩阵中的每个样本 $n$，我们计算 $p(\mathbf{y}_{n,\mathbf{h}}|\mathbf{y}_{n,\mathbf{v}},\boldsymbol{\theta})$，其中 $\boldsymbol{v}$ 是该样本中可见条目的索引，$\boldsymbol{h}$ 是隐藏条目的其余索引，$\boldsymbol{\theta} = (\boldsymbol{\mu}, \boldsymbol{\Sigma})$。由此，我们计算每个缺失变量 $i \in \mathbf{h}$ 的边缘分布 $p(y_{n,i}|\mathbf{y}_{n,\mathbf{v}},\boldsymbol{\theta})$。根据该边缘分布，我们计算后验均值 $\bar{y}_{n,i} = \mathbb{E}[y_{n,i}|\mathbf{y}_{n,\mathbf{v}},\boldsymbol{\theta}]$。

后验均值表示我们对那个条目真实值的“最佳猜测”，因为它在第 5 章中解释的意义上最小化了期望平方误差。我们可以使用 $ \mathbb{V}[y_{n,i}|\pmb{y}_{n,v},\pmb{\theta}] $ 作为对该猜测置信度的度量，尽管此处未展示。另一种方法是，我们可以从 $ p(\pmb{y}_{n,h}|\pmb{y}_{n,v},\pmb{\theta}) $ 中抽取多个后验样本；这被称为**多重插补**，并为后续处理“填充后”数据的下游算法提供了更稳健的估计。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_206_117_435_327.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_481_118_714_329.jpg" alt="图像" width="20%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_763_119_993_329.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图3.7：使用MVN（多变量正态分布）进行数据插补的示意图。行代表特征，列代表数据样本（与本文常用惯例的转置）。(a) 数据矩阵的可视化。空白条目表示缺失（未观测到）。蓝色表示正值，绿色表示负值。方块面积与数值大小成正比。（这被称为辛顿图，以著名机器学习研究者Geoff Hinton的名字命名。）(b) 真实数据矩阵（隐藏）。(c) 后验预测分布的均值，基于该样本（列）的部分观测数据，使用真实模型参数计算得到。由 gauss\_imputation known\_params\_demo.ipynb 生成。</div>


### 3.3 线性高斯系统 *

在第3.2.3节中，我们基于无噪声观测来推断高斯随机向量隐藏部分的后验。本节将该方法扩展到处理含噪观测。

设 $ z \in \mathbb{R}^L $ 为未知值向量，$ y \in \mathbb{R}^D $ 为 $ z $ 的某个含噪观测。我们假设这些变量由以下联合分布关联：

$$  p(z)=\mathcal{N}(z|\boldsymbol{\mu}_{z},\boldsymbol{\Sigma}_{z})   \tag*{(3.33)}$$

$$  p(\boldsymbol{y}|\boldsymbol{z})=\mathcal{N}(\boldsymbol{y}|\mathbf{W}\boldsymbol{z}+\boldsymbol{b},\boldsymbol{\Sigma}_{y})   \tag*{(3.34)}$$

其中 W 是一个大小为 $ D \times L $ 的矩阵。这是一个线性高斯系统的例子。

相应的联合分布 $ p(z, \mathbf{y}) = p(z)p(\mathbf{y}|\mathbf{z}) $ 是一个 $ L + D $ 维高斯分布，其均值和协方差由下式给出：

$$  \boldsymbol{\mu}=\begin{pmatrix}\boldsymbol{\mu}_{z}\\ \mathbf{W}\boldsymbol{\mu}_{z}+\boldsymbol{b}\end{pmatrix}   \tag*{(3.35)}$$

$$  \boldsymbol{\Sigma}=\begin{pmatrix}\boldsymbol{\Sigma}_{z}&\boldsymbol{\Sigma}_{z}\boldsymbol{W}^{\mathrm{T}}\\\boldsymbol{W}\boldsymbol{\Sigma}_{z}&\boldsymbol{\Sigma}_{y}+\boldsymbol{W}\boldsymbol{\Sigma}_{z}\boldsymbol{W}^{\mathrm{T}}\end{pmatrix}   \tag*{(3.36)}$$

将公式(3.28)中的高斯条件公式应用于联合分布 $ p(\mathbf{y}, \mathbf{z}) $，我们可以计算后验 $ p(\mathbf{z}|\mathbf{y}) $，如下文所述。这可以理解为逆转生成模型中从隐变量到观测的 $ \mathbf{z} \to \mathbf{y} $ 箭头方向。

---

#### 3.3.1 高斯变量的贝叶斯规则

隐变量的后验分布由下式给出：

$$  \begin{aligned}{p(z|\mathbf{y})}&{{}=\mathcal{N}(\mathbf{z}|\mathbf{\mu}_{z|y},\mathbf{\Sigma}_{z|y})}\\ {\mathbf{\Sigma}_{z|y}^{-1}}&{{}=\mathbf{\Sigma}_{z}^{-1}+\mathbf{W}^{\mathsf{T}}\mathbf{\Sigma}_{y}^{-1}\mathbf{W}}\\ {\mathbf{\mu}_{z|y}}&{{}=\mathbf{\Sigma}_{z|y}[\mathbf{W}^{\mathsf{T}}\mathbf{\Sigma}_{y}^{-1}(\mathbf{y}-\mathbf{b})+\mathbf{\Sigma}_{z}^{-1}\mathbf{\mu}_{z}]}\\ \end{aligned}   \tag*{(3.37)}$$

这就是所谓的高斯变量的贝叶斯规则。此外，后验分布的归一化常数为：

$$  p(\boldsymbol{y})=\int\mathcal{N}(z|\boldsymbol{\mu}_{z},\boldsymbol{\Sigma}_{z})\mathcal{N}(\boldsymbol{y}|\mathbf{W}z+\boldsymbol{b},\boldsymbol{\Sigma}_{y})d\boldsymbol{z}=\mathcal{N}(\boldsymbol{y}|\mathbf{W}\boldsymbol{\mu}_{z}+\boldsymbol{b},\boldsymbol{\Sigma}_{y}+\mathbf{W}\boldsymbol{\Sigma}_{z}\mathbf{W}^{\mathsf{T}})   \tag*{(3.38)}$$

我们看到，高斯先验 \( p(z) \) 与高斯似然 \( p(\mathbf{y}|\mathbf{z}) \) 相结合，得到了高斯后验 \( p(z|\mathbf{y}) \)。因此，高斯分布在贝叶斯条件下是封闭的。更一般地，我们说高斯先验是高斯似然的共轭先验，因为后验分布与先验具有相同的类型。我们将在第 4.6.1 节更详细地讨论共轭先验的概念。

在接下来的小节中，我们将给出这一结果的各种应用。但首先，我们给出推导过程。

#### 3.3.2 推导过程 \( * \)

现在推导方程 (3.37)。基本思想是推导联合分布 \( p(z, \mathbf{y}) = p(z)p(\mathbf{y}|\mathbf{z}) \)，然后利用第 3.2.3 节的结果计算 \( p(z|\mathbf{y}) \)。

更具体地，我们进行如下操作。联合分布的对数如下（忽略无关常数）：

$$  \log p(z,\boldsymbol{y})=-\frac{1}{2}(z-\boldsymbol{\mu}_{z})^{T}\boldsymbol{\Sigma}_{z}^{-1}(z-\boldsymbol{\mu}_{z})-\frac{1}{2}(\boldsymbol{y}-\boldsymbol{W}z-\boldsymbol{b})^{T}\boldsymbol{\Sigma}_{y}^{-1}(\boldsymbol{y}-\boldsymbol{W}z-\boldsymbol{b})   \tag*{(3.39)}$$

这显然是一个联合高斯分布，因为它是二次型的指数形式。

展开涉及 \( z \) 和 \( y \) 的二次项，并忽略线性项和常数项，我们得到：

$$  Q=-\frac{1}{2}z^{T}\Sigma_{z}^{-1}z-\frac{1}{2}\boldsymbol{y}^{T}\Sigma_{y}^{-1}\boldsymbol{y}-\frac{1}{2}(\mathbf{W}z)^{T}\Sigma_{y}^{-1}(\mathbf{W}z)+\boldsymbol{y}^{T}\Sigma_{y}^{-1}\mathbf{W}z   \tag*{(3.40)}$$

$$  =-\frac{1}{2}\begin{pmatrix}z\\ y\end{pmatrix}^{T}\begin{pmatrix}\boldsymbol{\Sigma}_{z}^{-1}+\mathbf{W}^{T}\boldsymbol{\Sigma}_{y}^{-1}\mathbf{W}&-\mathbf{W}^{T}\boldsymbol{\Sigma}_{y}^{-1}\\ -\boldsymbol{\Sigma}_{y}^{-1}\mathbf{W}&\boldsymbol{\Sigma}_{y}^{-1}\end{pmatrix}\begin{pmatrix}z\\ y\end{pmatrix}   \tag*{(3.41)}$$

$$  =-\frac{1}{2}\begin{pmatrix}z\\ y\end{pmatrix}^{T}\boldsymbol{\Sigma}^{-1}\begin{pmatrix}z\\ y\end{pmatrix}   \tag*{(3.42)}$$

其中联合分布的精度矩阵定义为：

$$  \boldsymbol{\Sigma}^{-1}=\begin{pmatrix}\boldsymbol{\Sigma}_{z}^{-1}+\boldsymbol{W}^{T}\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{W}&-\boldsymbol{W}^{T}\boldsymbol{\Sigma}_{y}^{-1}\\-\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{W}&\boldsymbol{\Sigma}_{y}^{-1}\end{pmatrix}\triangleq\boldsymbol{\Lambda}=\begin{pmatrix}\boldsymbol{\Lambda}_{z z}&\boldsymbol{\Lambda}_{z y}\\\boldsymbol{\Lambda}_{y z}&\boldsymbol{\Lambda}_{y y}\end{pmatrix}   \tag*{(3.43)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

从方程 (3.28) 出发，并利用 $ \mu_{y} = W\mu_{z} + b $ 这一事实，我们得到

$$  p(z|\pmb{y})=\mathcal{N}(\pmb{\mu}_{z|y},\pmb{\Sigma}_{z|y})   \tag*{(3.44)}$$

$$  \mathbf{\Sigma}_{z|y}=\mathbf{\Lambda}_{z z}^{-1}=(\mathbf{\Sigma}_{z}^{-1}+\mathbf{W}^{T}\mathbf{\Sigma}_{y}^{-1}\mathbf{W})^{-1}   \tag*{(3.45)}$$

$$  \boldsymbol{\mu}_{z\mid y}=\boldsymbol{\Sigma}_{z\mid y}\left(\boldsymbol{\Lambda}_{z z}\boldsymbol{\mu}_{z}-\boldsymbol{\Lambda}_{z y}(\boldsymbol{y}-\boldsymbol{\mu}_{y})\right)   \tag*{(3.46)}$$

$$  =\Sigma_{z|y}\left(\Sigma_{z}^{-1}\boldsymbol{\mu}_{z}+\mathbf{W}^{\mathrm{T}}\boldsymbol{\Sigma}_{y}^{-1}\mathbf{W}\boldsymbol{\mu}_{z}+\mathbf{W}^{\mathrm{T}}\boldsymbol{\Sigma}_{y}^{-1}(\boldsymbol{y}-\boldsymbol{\mu}_{y})\right)   \tag*{(3.47)}$$

$$  =\Sigma_{z|y}\left(\Sigma_{z}^{-1}\boldsymbol{\mu}_{z}+\mathbf{W}^{\mathsf{T}}\boldsymbol{\Sigma}_{y}^{-1}(\mathbf{W}\boldsymbol{\mu}_{z}+\boldsymbol{y}-\boldsymbol{\mu}_{y})\right)   \tag*{(3.48)}$$

$$  =\Sigma_{z|y}\left(\Sigma_{z}^{-1}\boldsymbol{\mu}_{z}+\mathbf{W}^{T}\boldsymbol{\Sigma}_{y}^{-1}(\boldsymbol{y}-\boldsymbol{b})\right)   \tag*{(3.49)}$$

##### 3.3.2.1 配方法

在处理线性高斯系统时，常用一种称为配方法（completing the square）的代数技巧。在标量情形下，该技巧表明，我们可以将如下形式的二次函数

 $$ f(x)=ax^{2}+bx+c $$ 

重写为：

 $$ ax^{2}+bx+c=a(x-h)^{2}+k $$ 

其中

 $$ h=-\frac{b}{2a} $$ 

 $$ k=c-\frac{b^{2}}{4a} $$ 

在向量情形下，该技巧表明，我们可以将如下形式的二次函数

 $$ f(\boldsymbol{x})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}+\boldsymbol{x}^{\top}\boldsymbol{b}+c $$ 

重写为：

 $$ \boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}+\boldsymbol{x}^{\top}\boldsymbol{b}+c=(\boldsymbol{x}-\boldsymbol{h})^{\top}\mathbf{A}(\boldsymbol{x}-\boldsymbol{h})+k $$ 

其中

 $$ h=-\frac{1}{2}\mathbf{A}^{-1}\mathbf{b} $$ 

 $$ k=c-\frac{1}{4}\boldsymbol{b}^{\top}\boldsymbol{A}^{-1}\boldsymbol{b} $$ 

这一技巧将在更高级的推导中使用。

#### 3.3.3 示例：推断未知标量

假设我们对某个潜在量 $z$ 进行了 $N$ 次带噪声的测量 $y_i$；设测量噪声的精度固定为 $\lambda_y = 1/\sigma^2$，则似然函数为

$$  p(y_{i}|z)=\mathcal{N}(y_{i}|z,\lambda_{y}^{-1})   \tag*{(3.50)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_181_114_598_410.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_594_116_1029_411.jpg" alt="Image" width="37%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 3.8：在观察到含噪测量值 $y=3$ 后对 $z$ 的推断。(a) 强先验 $\mathcal{N}(0,1)$。后验均值被“收缩”向先验均值 0。(b) 弱先验 $\mathcal{N}(0,5)$。后验均值与MLE相近。由 gauss\_infer\_1d.ipynb 生成。</div>

现在，我们使用高斯先验来描述未知源的值：

$$  p(z)=\mathcal{N}(z|\mu_{0},\lambda_{0}^{-1})   \tag*{(3.51)}$$

我们希望计算 $ p(z|y_1,\ldots,y_N,\sigma^2) $。通过定义 $ \boldsymbol{y} = (y_1,\ldots,y_N) $，$ \mathbf{W} = \mathbf{1}_N $（一个 $ N \times 1 $ 的全1列向量）和 $ \boldsymbol{\Sigma}_y^{-1} = \mathrm{diag}(\lambda_y \mathbf{I}) $，我们可以将其转化为能够应用高斯变量贝叶斯公式的形式。于是得到：

$$  p(z|\pmb{y})=\mathcal{N}(z|\mu_{N},\lambda_{N}^{-1})   \tag*{(3.52)}$$

$$  \lambda_{N}=\lambda_{0}+N\lambda_{y}   \tag*{(3.53)}$$

$$  \mu_{N}=\frac{N\lambda_{y}\overline{y}+\lambda_{0}\mu_{0}}{\lambda_{N}}=\frac{N\lambda_{y}}{N\lambda_{y}+\lambda_{0}}\overline{y}+\frac{\lambda_{0}}{N\lambda_{y}+\lambda_{0}}\mu_{0}   \tag*{(3.54)}$$

这些公式相当直观：后验精度 $ \lambda_N $ 是先验精度 $ \lambda_0 $ 加上 $ N $ 份测量精度 $ \lambda_y $。此外，后验均值 $ \mu_N $ 是MLE $ \overline{y} $ 和先验均值 $ \mu_0 $ 的凸组合。这清楚地表明，后验均值是MLE与先验之间的折衷。如果相对于信号强度而言先验较弱（$ \lambda_0 $ 相对于 $ \lambda_y $ 很小），则MLE的权重更大。如果相对于信号强度而言先验较强（$ \lambda_0 $ 相对于 $ \lambda_y $ 很大），则先验的权重更大。如图3.8所示。

注意，后验均值用 $ N\lambda_y\overline{y} $ 表示，因此拥有 $ N $ 个精度均为 $ \lambda_y $ 的测量值，相当于拥有一个值为 $ \overline{y} $、精度为 $ N\lambda_y $ 的测量值。

我们可以用后验方差而非后验精度来重写上述结果：

---

如下：

$$  p(z|\mathcal{D},\sigma^{2})=\mathcal{N}(z|\mu_{N},\tau_{N}^{2})   \tag*{(3.55)}$$

$$  \tau_{N}^{2}=\frac{1}{\frac{N}{\sigma^{2}}+\frac{1}{\tau_{0}^{2}}}=\frac{\sigma^{2}\tau_{0}^{2}}{N\tau_{0}^{2}+\sigma^{2}}   \tag*{(3.56)}$$

$$  \mu_{N}=\tau_{N}^{2}\left(\frac{\mu_{0}}{\tau_{0}^{2}}+\frac{N\overline{y}}{\sigma^{2}}\right)=\frac{\sigma^{2}}{N\tau_{0}^{2}+\sigma^{2}}\mu_{0}+\frac{N\tau_{0}^{2}}{N\tau_{0}^{2}+\sigma^{2}}\overline{y}   \tag*{(3.57)}$$

其中 $\tau_{0}^{2}=1/\lambda_{0}$ 是先验方差，$\tau_{N}^{2}=1/\lambda_{N}$ 是后验方差。

我们还可以通过每次观测后更新来顺序计算后验。如果 $N=1$，在观察到单个观测后，我们可以将后验重写如下（定义 $\Sigma_y=\sigma^2$, $\Sigma_0=\tau_0^2$ 和 $\Sigma_1=\tau_1^2$ 分别为似然、先验和后验的方差）：

$$  p(z|y)=\mathcal{N}(z|\mu_{1},\Sigma_{1})   \tag*{(3.58)}$$

$$  \Sigma_{1}=\left(\frac{1}{\Sigma_{0}}+\frac{1}{\Sigma_{y}}\right)^{-1}=\frac{\Sigma_{y}\Sigma_{0}}{\Sigma_{0}+\Sigma_{y}}   \tag*{(3.59)}$$

$$  \mu_{1}=\Sigma_{1}\left(\frac{\mu_{0}}{\Sigma_{0}}+\frac{y}{\Sigma_{y}}\right)   \tag*{(3.60)}$$

我们可以用三种不同的方式重写后验均值：

$$  \mu_{1}=\frac{\Sigma_{y}}{\Sigma_{y}+\Sigma_{0}}\mu_{0}+\frac{\Sigma_{0}}{\Sigma_{y}+\Sigma_{0}}y   \tag*{(3.61)}$$

$$  =\mu_{0}+(y-\mu_{0})\frac{\Sigma_{0}}{\Sigma_{y}+\Sigma_{0}}   \tag*{(3.62)}$$

$$  =y-(y-\mu_{0})\frac{\Sigma_{y}}{\Sigma_{y}+\Sigma_{0}}   \tag*{(3.63)}$$

第一个方程是先验与数据的凸组合。第二个方程是先验均值向数据调整。第三个方程是数据向先验均值调整；这被称为收缩。这些都是表达似然与先验之间权衡的等价方式。如果 $\Sigma_0$ 相对于 $\Sigma_y$ 较小（对应于强先验），则收缩量较大（见图 3.8(a)）；而如果 $\Sigma_0$ 相对于 $\Sigma_y$ 较大（对应于弱先验），则收缩量较小（见图 3.8(b)）。

量化收缩量的另一种方式是使用信噪比，其定义如下：

$$  \mathrm{S N R}\triangleq\frac{\mathbb{E}\left[Z^{2}\right]}{\mathbb{E}\left[\epsilon^{2}\right]}=\frac{\Sigma_{0}+\mu_{0}^{2}}{\Sigma_{y}}   \tag*{(3.64)}$$

其中 $z \sim \mathcal{N}(\mu_0, \Sigma_0)$ 是真实信号，$y = z + \epsilon$ 是观测信号，$\epsilon \sim \mathcal{N}(0, \Sigma_y)$ 是噪声项。

#### 3.3.4 示例：推断未知向量

假设我们有一个未知的感兴趣量 $z \in \mathbb{R}^D$，我们为其赋予高斯先验 $p(z) = \mathcal{N}(\boldsymbol{\mu}_z, \boldsymbol{\Sigma}_z)$。如果我们对 $z$ 先验“一无所知”，则可以将 $\boldsymbol{\Sigma}_z = \infty \mathbf{I}$ 设为，这意味着我们

---

对于 $z$ 应取何值完全不确定。（实践中，我们可以使用一个较大但有限的协方差值。）由对称性，设定 $\boldsymbol{\mu}_{z} = \mathbf{0}$ 是合理的。

现在假设我们对 $z$ 进行了 $N$ 次独立且有噪声的测量，$\boldsymbol{y}_n \sim \mathcal{N}(\boldsymbol{z}, \boldsymbol{\Sigma}_y)$，每个测量值的大小为 $D$。可以证明，$N$ 个观测的似然可以用一个基于其平均值 $\overline{\boldsymbol{y}}$ 的单一高斯分布来表示，前提是将协方差按 $1/N$ 缩放以补偿测量精度的提高，即：

$$  p(\mathcal{D}|z)=\prod_{n=1}^{N}\mathcal{N}(\boldsymbol{y}_{n}|z,\boldsymbol{\Sigma}_{y})\propto\mathcal{N}(\overline{\boldsymbol{y}}|z,\frac{1}{N}\boldsymbol{\Sigma}_{y})   \tag*{(3.65)}$$

为了理解为什么如此，考虑两次测量的情况。对数似然可以用规范参数写成如下形式：$ ^{2} $

 $$ \begin{align*}\log(p(\boldsymbol{y}_{1}|\boldsymbol{z})p(\boldsymbol{y}_{2}|\boldsymbol{z}))&=K_{1}-\frac{1}{2}\left(z^{\top}\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{z}-2z^{\top}\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{y}_{1}\right)-\frac{1}{2}\left(z^{\top}\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{z}-2z^{\top}\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{y}_{1}\right)\\&=K_{1}-\frac{1}{2}\left(z^{\top}2\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{z}-2z^{\top}\boldsymbol{\Sigma}_{y}^{-1}\left(\boldsymbol{y}_{1}+\boldsymbol{y}_{2}\right)\right)\\&=K_{1}-\frac{1}{2}\left(z^{\top}2\boldsymbol{\Sigma}_{y}^{-1}\boldsymbol{z}-2z^{\top}2\boldsymbol{\Sigma}_{y}^{-1}\bar{\boldsymbol{y}}\right)\\&=K_{2}+\log\mathcal{N}(\boldsymbol{z}|\bar{\boldsymbol{y}},\frac{\boldsymbol{\Sigma}_{y}}{2})=K_{2}+\log\mathcal{N}(\bar{\boldsymbol{y}}|\boldsymbol{z},\frac{\boldsymbol{\Sigma}_{y}}{2})\end{align*} $$ 

其中 $K_{1}$ 和 $K_{2}$ 是与 $z$ 无关的常数。

利用这一点，并设定 $\mathbf{W} = \mathbf{I}, b = \mathbf{0}$，我们可以使用高斯分布的贝叶斯法则来计算 $z$ 的后验：

 $$ p(z|y_{1},\dots,y_{N})=\mathcal{N}(z|\hat{\mu},\hat{\Sigma}) $$ 

$$  \hat{\boldsymbol{\Sigma}}^{-1}=\boldsymbol{\Sigma}_{z}^{-1}+N\boldsymbol{\Sigma}_{y}^{-1}   \tag*{(3.66)}$$

$$  \hat{\boldsymbol{\mu}}=\hat{\boldsymbol{\Sigma}}\left(\boldsymbol{\Sigma}_{y}^{-1}(N\overline{\boldsymbol{y}})+\boldsymbol{\Sigma}_{z}^{-1}\boldsymbol{\mu}_{z}\right)   \tag*{(3.68)}$$

其中 $\hat{\mu}$ 和 $\hat{\Sigma}$ 是后验的参数。

图 Figure 3.9 给出了一个二维例子。我们可以将 $z$ 视为一个物体（例如导弹或飞机）在二维空间中的真实但未知的位置，而 $\boldsymbol{y}_n$ 则是带有噪声的观测值，比如雷达“光点”。随着我们接收到更多的光点，就能更精确地定位源。（在本系列的后续著作 [Mur23] 中，我们讨论了卡尔曼滤波算法，该算法将此思想扩展到时间序列观测。）

对于 $z$ 位置向量的每个分量，后验不确定性取决于传感器在每个维度上的可靠性。在上述例子中，维度1的测量噪声高于维度2，因此我们对 $z_{1}$（水平轴）的后验不确定性大于对 $z_{2}$（垂直轴）的后验不确定性。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_191_115_468_341.jpg" alt="图像" width="24%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_194_114_1009_357.jpg" alt="图像" width="70%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 3.9：二维高斯随机向量 $\mathbf{z}$ 的贝叶斯推断示意图。(a) 数据由 $ \mathbf{y}_n \sim \mathcal{N}(\mathbf{z}, \mathbf{\Sigma}_y) $ 生成，其中 $ \mathbf{z} = [0.5, 0.5]^\top $，$ \mathbf{\Sigma}_y = 0.1[2, 1; 1, 1] $。我们假设传感器噪声协方差 $ \mathbf{\Sigma}_y $ 已知，但 $\mathbf{z}$ 未知。黑色十字表示 $\mathbf{z}$。(b) 先验为 $ p(z) = \mathcal{N}(z|\mathbf{0}, 0.1\mathbf{I}_2) $。(c) 观测到 10 个数据点后的后验分布。由 gauss\_infer\_2d.ipynb 生成。</div>


#### 3.3.5 示例：传感器融合

本节将第 3.3.4 节扩展至多测量值情形，这些测量值来自不同传感器，且各传感器具有不同可靠性。即模型形式为

$$  p(z,\boldsymbol{y})=p(z)\prod_{m=1}^{M}\prod_{n=1}^{N_{m}}\mathcal{N}(\boldsymbol{y}_{n,m}|\boldsymbol{z},\boldsymbol{\Sigma}_{m})   \tag*{(3.69)}$$

其中 $M$ 为传感器（测量设备）数量，$N_m$ 为传感器 $m$ 的观测次数，$\boldsymbol{y} = \boldsymbol{y}_{1:N,1:M} \in \mathbb{R}^K$。我们的目标是综合所有证据，计算 $p(\boldsymbol{z}|\boldsymbol{y})$。这被称为**传感器融合**。

现在给出一个简单示例，其中仅有两个传感器，即 $ y_1 \sim \mathcal{N}(z, \Sigma_1) $ 和 $ y_2 \sim \mathcal{N}(z, \Sigma_2) $。用图示可表示为 $ y_1 \leftarrow z \rightarrow y_2 $。我们可以将 $ y_1 $ 和 $ y_2 $ 合并为单一向量 $ y $，因此模型可表示为 $ z \rightarrow [y_1, y_2] $，其中 $ p(y|z) = \mathcal{N}(y|\mathbf{W}z, \Sigma_y) $，$ \mathbf{W} = [\mathbf{I}; \mathbf{I}] $，$ \Sigma_y = [\Sigma_1, \mathbf{0}; \mathbf{0}, \Sigma_2] $ 为分块矩阵。然后可应用高斯分布的贝叶斯规则计算 $ p(z|y) $。

图 3.10(a) 给出了一个二维示例，其中设 $ \mathbf{\Sigma}_1 = \mathbf{\Sigma}_2 = 0.01\mathbf{I}_2 $，即两个传感器同样可靠。此时后验均值位于两个观测值 $ \mathbf{y}_1 $ 与 $ \mathbf{y}_2 $ 的中点。在图 3.10(b) 中，设 $ \mathbf{\Sigma}_1 = 0.05\mathbf{I}_2 $，$ \mathbf{\Sigma}_2 = 0.01\mathbf{I}_2 $，因此传感器 2 比传感器 1 更可靠。此时后验均值更接近 $ \mathbf{y}_2 $。在图 3.10(c) 中，设

$$  \mathbf{\Sigma}_{1}=0.01\begin{pmatrix}{{{10}}}&{{{1}}} \\{{{1}}}&{{{1}}}\end{pmatrix},\quad\mathbf{\Sigma}_{2}=0.01\begin{pmatrix}{{{1}}}&{{{1}}} \\{{{1}}}&{{{10}}}\end{pmatrix}   \tag*{(3.70)}$$

因此传感器 1 在第二个分量（垂直方向）上更可靠，传感器 2 在第一个分量（水平方向）上更可靠。此时后验均值采用 $ y_{1} $ 的垂直分量与 $ y_{2} $ 的水平分量。

---

### 3.4 指数族 *

<div style="text-align: center;"><img src="imgs/img_in_chart_box_172_118_439_295.jpg" alt="图片" width="23%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_451_115_717_295.jpg" alt="图片" width="23%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_731_117_995_295.jpg" alt="图片" width="22%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 3.10: 我们观测到 $ \mathbf{y}_1 = (0, -1) $（红色十字）和 $ \mathbf{y}_2 = (1, 0) $（绿色十字），并估计 $ \mathbb{E}[\mathbf{z}|\mathbf{y}_1, \mathbf{y}_2] $（黑色十字）。(a) 传感器同等可靠，因此后验均值估计位于两个圆圈之间。(b) 传感器 2 更可靠，因此估计向绿色圆圈偏移更多。(c) 传感器 1 在垂直方向上更可靠，传感器 2 在水平方向上更可靠。估计是两个测量值的适当组合。由 sensor_fusion_2d.ipynb 生成。</div>


### 3.4 指数族 *

在本节中，我们定义指数族，它包含许多常见的概率分布。指数族在统计学和机器学习中扮演着至关重要的角色。在本书中，我们主要在广义线性模型的背景下使用它，这将在第 12 章中讨论。我们将在本书的续集 [Mur23] 中看到指数族的更多应用。

#### 3.4.1 定义

考虑一族由 $ \eta \in \mathbb{R}^n $ 参数化、具有固定支撑集 $ \mathcal{Y}^D \subseteq \mathbb{R}^D $ 的概率分布。我们说分布 $ p(\boldsymbol{y}|\boldsymbol{\eta}) $ 属于指数族，如果其密度可以写成以下形式：

$$  p(\boldsymbol{y}|\boldsymbol{\eta})\triangleq\frac{1}{Z(\boldsymbol{\eta})}h(\boldsymbol{y})\exp[\boldsymbol{\eta}^{\mathsf{T}}\mathcal{T}(\boldsymbol{y})]=h(\boldsymbol{y})\exp[\boldsymbol{\eta}^{\mathsf{T}}\mathcal{T}(\boldsymbol{y})-A(\boldsymbol{\eta})]   \tag*{(3.71)}$$

其中 $h(y)$ 是一个缩放常数（也称为基测度，通常为 1），$\mathcal{T}(y) \in \mathbb{R}^K$ 是充分统计量，$\eta$ 是自然参数或规范参数，$Z(\eta)$ 是一个称为配分函数的归一化常数，$A(\eta) = \log Z(\eta)$ 是对数配分函数。可以证明，$A$ 是凸集 $\Omega \triangleq \{\eta \in \mathbb{R}^K : A(\eta) < \infty\}$ 上的凸函数。

如果自然参数相互独立，则比较方便。形式上，如果没有 $ \eta \in \mathbb{R}^K \setminus \{0\} $ 使得 $ \eta^\top \mathcal{T}(y) = 0 $，我们就说该指数族是 **最小** 的。最后一个条件在多项式分布的情况下可能被违反，因为参数存在和为 1 的约束；然而，如下文所示，很容易使用 $ K - 1 $ 个独立参数对分布进行重新参数化。

等式 (3.71) 可以通过定义 $ \eta = f(\phi) $ 来推广，其中 $ \phi $ 是另一组可能更小的参数。在这种情况下，分布的形式为

$$  p(\pmb{y}|\phi)=h(\pmb{y})\exp[f(\phi)^{\top}\mathcal{T}(\pmb{y})-A(f(\phi))]   \tag*{(3.72)}$$

作者：Kevin P. Murphy. (C) MIT 出版社. CC-BY-NC-ND 许可协议

---

如果从 $\phi$ 到 $\eta$ 的映射是非线性的，我们称之为弯曲指数族。若 $\eta = f(\phi) = \phi$，则该模型称为规范形式。此外，如果 $\mathcal{T}(y) = y$，则称其为自然指数族或NEF。此时，它可以写为

$$  p(\boldsymbol{y}|\boldsymbol{\eta})=h(\boldsymbol{y})\exp[\boldsymbol{\eta}^{\top}\boldsymbol{y}-A(\boldsymbol{\eta})]   \tag*{(3.73)}$$

#### 3.4.2 示例

作为一个简单示例，我们考虑伯努利分布。可以将其写成指数族形式如下：

$$  \mathrm{B e r}(y|\mu)=\mu^{y}(1-\mu)^{1-y}   \tag*{(3.74)}$$

$$  =\exp[y\log(\mu)+(1-y)\log(1-\mu)]   \tag*{(3.75)}$$

$$  =\exp[\mathcal{T}(y)^\intercal\boldsymbol{\eta}]   \tag*{(3.76)}$$

其中 $ \mathcal{T}(y) = [\mathbb{I}(y = 1), \mathbb{I}(y = 0)] $，$ \eta = [\log(\mu), \log(1 - \mu)] $，而 $ \mu $ 是均值参数。然而，这是一种过完备表示，因为特征之间存在线性依赖关系。这一点可以通过以下方式看出：

$$  \mathbf{1}^{\top}\mathcal{T}(y)=\mathbb{I}\left(y=0\right)+\mathbb{I}\left(y=1\right)=1   \tag*{(3.77)}$$

如果表示是过完备的，则 $ \eta $ 无法唯一确定。通常使用极小表示，这意味着每个分布有唯一的 $ \eta $ 与之关联。在这种情况下，我们可以定义

$$  \mathrm{B e r}(y|\mu)=\exp\left[y\log\left(\frac{\mu}{1-\mu}\right)+\log(1-\mu)\right]   \tag*{(3.78)}$$

通过以下定义将其转化为指数族形式：

$$  \eta=\log\left(\frac{\mu}{1-\mu}\right)   \tag*{(3.79)}$$

$$  \mathcal{T}(y)=y   \tag*{(3.80)}$$

$$  A(\eta)=-\log(1-\mu)=\log(1+e^{\eta})   \tag*{(3.81)}$$

$$  h(y)=1   \tag*{(3.82)}$$

我们可以通过规范参数 $\eta$ 恢复均值参数 $\mu$，利用

$$  \mu=\sigma(\eta)=\frac{1}{1+e^{-\eta}}   \tag*{(3.83)}$$

这即是我们熟知的逻辑（Sigmoid）函数。

更多示例请参见本书后续部分 [Mur23]。

---

#### 3.4.3 对数配分函数是累积量生成函数

分布的**一阶和二阶累积量**分别对应于均值E[Y]和方差V[Y]，而一阶和二阶矩分别为E[Y]和E[Y²]。我们还可以计算更高阶的累积量（以及矩）。指数族的一个重要性质是：**对数配分函数的导数可用于生成充分统计量的所有累积量**。具体而言，一阶和二阶累积量由下式给出：

$$  \nabla A(\boldsymbol{\eta})=\mathbb{E}\left[\mathcal{T}(\boldsymbol{y})\right]   \tag*{(3.84)}$$

$$  \nabla^{2}A(\pmb{\eta})=\mathrm{Cov}\left[\mathcal{T}(\pmb{y})\right]   \tag*{(3.85)}$$

由上述结果可知，Hessian矩阵正定，因此$ A(\boldsymbol{\eta}) $关于$ \boldsymbol{\eta} $是凸函数。由于对数似然函数的形式为$ \log p(\boldsymbol{y}|\boldsymbol{\eta}) = \boldsymbol{\eta}^{\mathrm{T}} \mathcal{T}(\boldsymbol{y}) - A(\boldsymbol{\eta}) + \mathrm{const} $，可见该函数是凹函数，因此最大似然估计具有唯一的全局最大值。

#### 3.4.4 指数族的最大熵推导

假设我们希望找到一个分布$ p(\boldsymbol{x}) $来描述某些数据，而我们所知的仅是某些特征或函数$ f_k(\boldsymbol{x}) $的期望值$ (F_k) $：

$$  \int d\boldsymbol{x}p(\boldsymbol{x})f_{k}(\boldsymbol{x})=F_{k}   \tag*{(3.86)}$$

例如，$ f_1 $可以计算$ x $，$ f_2 $可以计算$ x^2 $，从而$ F_1 $成为经验均值，$ F_2 $成为经验二阶矩。我们对分布的**先验信念**为$ q(x) $。

为了形式化表达“最少假设”的含义，我们将寻找一个分布，使其在KL散度（第6.2节）意义下尽可能接近先验$ q(\boldsymbol{x}) $，同时满足约束条件：

$$  p=\underset{p}{\operatorname{argmin}}D_{\mathbb{K L}}\left(p\parallel q\right)\text{subject to constraints}   \tag*{(3.87)}$$

如果采用均匀先验$ q(\boldsymbol{x}) \propto 1 $，则最小化KL散度等价于最大化熵（第6.1节）：

$$  p=\underset{p}{\operatorname{argmax}}\mathbb{H}(p)\text{subject to constraints}   \tag*{(3.88)}$$

其结果称为**最大熵模型**。

为了在式(3.86)的约束以及$ p(\boldsymbol{x}) \geq 0 $和$ \sum_{\boldsymbol{x}} p(\boldsymbol{x}) = 1 $的约束下最小化KL散度，我们将使用拉格朗日乘子法（见第8.5.1节）。拉格朗日函数为

$$  J(p,\boldsymbol{\lambda})=-\sum_{\boldsymbol{x}}p(\boldsymbol{x})\log\frac{p(\boldsymbol{x})}{q(\boldsymbol{x})}+\lambda_{0}\left(1-\sum_{\boldsymbol{x}}p(\boldsymbol{x})\right)+\sum_{k}\lambda_{k}\left(F_{k}-\sum_{\boldsymbol{x}}p(\boldsymbol{x})f_{k}(\boldsymbol{x})\right)   \tag*{(3.89)}$$

我们可以使用变分法对函数p求导，但这里采用更简单的方法，将p视为固定长度的向量（因为我们假设x是离散的）。于是有

$$  \frac{\partial J}{\partial p_{c}}=-1-\log\frac{p(x=c)}{q(x=c)}-\lambda_{0}-\sum_{k}\lambda_{k}f_{k}(x=c)   \tag*{(3.90)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

令每个 $c$ 的 $\frac{\partial J}{\partial p_{c}} = 0$ 可得

$$ p(\boldsymbol{x})=\frac{q(\boldsymbol{x})}{Z}\exp\left(-\sum_{k}\lambda_{k}f_{k}(\boldsymbol{x})\right) \tag*{(3.91)}$$

其中我们定义了 $Z \triangleq e^{1+\lambda_0}$。利用归一化约束，得到

$$ 1=\sum_{\boldsymbol{x}}p(\boldsymbol{x})=\frac{1}{Z}\sum_{\boldsymbol{x}}q(\boldsymbol{x})\exp\left(-\sum_{k}\lambda_{k}f_{k}(\boldsymbol{x})\right) \tag*{(3.92)}$$

因此归一化常数为

$$ Z=\sum_{\boldsymbol{x}}q(\boldsymbol{x})\exp\left(-\sum_{k}\lambda_{k}f_{k}(\boldsymbol{x})\right) \tag*{(3.93)}$$

这恰好具有指数族的形式，其中 $f(\boldsymbol{x})$ 是充分统计量向量，$-\lambda$ 是自然参数，$q(\boldsymbol{x})$ 是基测度。

例如，若特征为 $f_{1}(x) = x$ 和 $f_{2}(x) = x^{2}$，且我们希望匹配一阶矩和二阶矩，则得到高斯分布。

### 3.5 混合模型

构建更复杂概率模型的一种方法是对简单分布取凸组合，称为混合模型，其形式为

$$ p(\boldsymbol{y}|\boldsymbol{\theta})=\sum_{k=1}^{K}\pi_{k}p_{k}(\boldsymbol{y}) \tag*{(3.94)}$$

其中 $p_k$ 是第 $k$ 个混合分量，$\pi_k$ 是混合权重，满足 $0 \leq \pi_k \leq 1$ 且 $\sum_{k=1}^K \pi_k = 1$。

我们可以将该模型重新表述为层次模型，其中引入离散隐变量 $z \in \{1,\ldots,K\}$，用以指定生成输出 $\boldsymbol{y}$ 所使用的分布。该隐变量的先验为 $p(z = k|\boldsymbol{\theta}) = \pi_k$，条件分布为 $p(\boldsymbol{y}|z = k, \boldsymbol{\theta}) = p_k(\boldsymbol{y}) = p(\boldsymbol{y}|\boldsymbol{\theta}_k)$。即定义如下联合模型：

$$ p(z|\boldsymbol{\theta})=\mathrm{Cat}(z|\boldsymbol{\pi}) \tag*{(3.95)}$$

$$ p(\boldsymbol{y}|z=k,\boldsymbol{\theta})=p(\boldsymbol{y}|\boldsymbol{\theta}_{k}) \tag*{(3.96)}$$

其中 $\boldsymbol{\theta} = (\pi_1, \ldots, \pi_K, \boldsymbol{\theta}_1, \ldots, \boldsymbol{\theta}_K)$ 为所有模型参数。数据的“生成过程”为：首先采样特定分量 $z$，然后根据 $z$ 的取值选择参数生成观测 $\boldsymbol{y}$。通过对 $z$ 进行边缘化，我们得到方程 (3.94)：

$$ p(\boldsymbol{y}|\boldsymbol{\theta})=\sum_{k=1}^{K}p(z=k|\boldsymbol{\theta})p(\boldsymbol{y}|z=k,\boldsymbol{\theta})=\sum_{k=1}^{K}\pi_{k}p(\boldsymbol{y}|\boldsymbol{\theta}_{k}) \tag*{(3.97)}$$

通过改变基分布 $p_{k}$，我们可以创建不同类型的混合模型，如下文所述。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_239_188_521_413.jpg" alt="图像" width="24%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_645_200_948_390.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 3.11: 二维空间中3个高斯分布的混合。(a) 展示了混合中每个分量等概率密度轮廓线。(b) 整体密度的曲面图。改编自 [Bis06] 的图 2.23。由 gmm_plot_demo.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_226_550_538_760.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_633_551_946_761.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 3.12: (a) 二维空间中的一些数据。(b) 使用基于 GMM 计算的 K=5 个聚类得到的一种可能的聚类结果。由 gmm_2d.ipynb 生成。</div>


#### 3.5.1 高斯混合模型

高斯混合模型（Gaussian mixture model, GMM），也称为高斯分布混合（mixture of Gaussians, MoG），定义如下：

$$  p(\boldsymbol{y}|\boldsymbol{\theta})=\sum_{k=1}^{K}\pi_{k}\mathcal{N}(\boldsymbol{y}|\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})   \tag*{(3.98)}$$

图3.11展示了二维空间中由3个高斯分布混合定义的密度。每个混合分量由一组不同的椭圆轮廓线表示。当混合分量数量足够多时，GMM可以近似 $ \mathbb{R}^D $ 上的任何光滑分布。

GMM常用于对实值数据样本 $ \mathbf{y}_n \in \mathbb{R}^D $ 进行无监督聚类。这通常分两个阶段进行。首先，我们拟合模型，例如通过计算MLE $ \hat{\boldsymbol{\theta}} = \arg\max \log p(\mathcal{D}|\boldsymbol{\theta}) $，其中

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_439_135_747_379.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">图 3.13：我们在二值化 MNIST 手写数字数据上拟合了一个由 20 个伯努利分布组成的混合模型。图中展示了估计的聚类均值 $ \hat{\mu}_k $。每张图片上方的数字代表估计的混合权重 $ \hat{\pi}_k $。训练模型时未使用任何标签。由 mix_bernoulli_em_mnist.ipynb 生成。</div>


 $ \mathcal{D} = \{y_n : n = 1 : N\} $。（我们将在第 8.7.3 节讨论如何计算这个 MLE。）然后，我们将每个数据点 $ y_n $ 与一个离散的潜在变量或隐藏变量 $ z_n \in \{1, \ldots, K\} $ 相关联，该变量指定了用于生成 $ y_n $ 的混合成分或聚类的身份。这些潜在身份是未知的，但我们可以利用贝叶斯规则计算它们的后验：

$$  r_{nk}\triangleq p(z_{n}=k|\boldsymbol{y}_{n},\boldsymbol{\theta})=\frac{p(z_{n}=k|\boldsymbol{\theta})p(\boldsymbol{y}_{n}|z_{n}=k,\boldsymbol{\theta})}{\sum_{k^{\prime}=1}^{K}p(z_{n}=k^{\prime}|\boldsymbol{\theta})p(\boldsymbol{y}_{n}|z_{n}=k^{\prime},\boldsymbol{\theta})}   \tag*{(3.99)}$$

量 $ r_{nk} $ 被称为聚类 k 对数据点 n 的**责任**。在给定责任的情况下，我们可以按如下方式计算最可能的聚类分配：

$$  \hat{z}_{n}=\arg\max_{k}r_{nk}=\arg\max_{k}\left[\log p(\boldsymbol{y}_{n}|z_{n}=k,\boldsymbol{\theta})+\log p(z_{n}=k|\boldsymbol{\theta})\right]   \tag*{(3.100)}$$

这被称为**硬聚类**。（如果我们利用责任将每个数据点按比例分配到不同聚类，则称为软聚类。）示例见图 3.12。

如果我们在 $ z_n $ 上使用均匀先验，并且使用球形高斯分布且 $ \mathbf{\Sigma}_k = \mathbf{I} $，那么硬聚类问题简化为：

$$  z_{n}=\underset{k}{\arg\min}||\boldsymbol{y}_{n}-\hat{\boldsymbol{\mu}}_{k}||_{2}^{2}   \tag*{(3.101)}$$

换句话说，我们将每个数据点分配给其最近的质心（以欧几里得距离度量）。这是 K 均值聚类算法的基础，我们将在第 21.3 节讨论该算法。

#### 3.5.2 伯努利混合模型

如果数据是二值的，我们可以使用**伯努利混合模型**（BMM，也称为伯努利混合模型），其中每个混合成分具有以下形式：

$$  p(\boldsymbol{y}|z=k,\boldsymbol{\theta})=\prod_{d=1}^{D}\operatorname{Ber}(y_{d}|\mu_{dk})=\prod_{d=1}^{D}\mu_{dk}^{y_{d}}(1-\mu_{dk})^{1-y_{d}}   \tag*{(3.102)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_350_120_827_473.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 3.14：带对应二元CPT的洒水器PGM。T和F分别表示真和假。</div>


这里 $ \mu_{dk} $ 表示第 $ d $ 位在第 $ k $ 个簇中开启的概率。

例如，我们使用 $ K = 20 $ 个分量将BMM拟合到MNIST数据集（第3.5.2节）。（我们使用EM算法进行拟合，该算法类似于第8.7.3节讨论的GMM的EM算法；然而，我们也可以使用SGD来拟合模型，这对于大型数据集更高效 $ ^{3} $。）每个混合分量（即 $ \mu_k $ 和 $ \pi_k $）的最终参数如图3.13所示。我们看到模型“发现”了每个数字类别的一种表示。（某些数字被多次表示，因为模型不知道类别的“真实”数量。关于如何选择混合分量的数量 $ K $ 的更多信息，请参见第21.3.7节。）

### 3.6 概率图模型 *

我基本知道两个以简单方式处理复杂系统的原则：第一个是模块化原则，第二个是抽象原则。我是机器学习中计算概率的支持者，因为我相信概率理论以深刻且有趣的方式实现了这两个原则——即通过因子分解和通过平均。在我看来，尽可能充分利用这两种机制是机器学习的前进方向。——迈克尔·乔丹，1997年（引用于[Fre98]）。

现在我们已经介绍了一些简单的概率构建模块。在第3.3节中，我们展示了一种用一些高斯构建模块组合成高维分布 $ p(\mathbf{y}) $ 的方法，这些模块包含了边缘分布 $ p(\mathbf{y}_1) $ 和条件分布 $ p(\mathbf{y}_2|\mathbf{y}_1) $。这一思想可以扩展，用于定义多个随机变量集合上的联合分布。我们将做出的关键假设是，某些变量在给定其他变量的条件下是独立的。我们将使用图来表示我们的条件独立假设，如下文简要解释。（更多信息请参见本书续篇[Mur23]。）

---

#### 3.6.1 表示

概率图模型（Probabilistic Graphical Model，PGM）是一种利用图结构编码条件独立性假设的联合概率分布。当该图为有向无环图（Directed Acyclic Graph，DAG）时，此类模型有时被称为贝叶斯网络，尽管这类模型本质上并非贝叶斯学派。

PGM 的基本思想是：图中的每个节点代表一个随机变量，每条边代表一种直接依赖关系。更准确地说，每条缺失的边代表一个条件独立性关系。在 DAG 情形下，我们可以按拓扑顺序对节点进行编号（父节点先于子节点），然后建立连接，使得每个节点在给定其父节点时与所有前驱节点条件独立：

$$  Y_{i}\perp\mathbf{Y}_{\mathrm{p r e d}(i)\backslash\mathrm{p a}(i)}|\mathbf{Y}_{\mathrm{p a}(i)}   \tag*{(3.103)}$$

其中 $ \text{pa}(i) $ 是节点 $ i $ 的父节点，$ \text{pred}(i) $ 是该顺序中节点 $ i $ 的前驱节点（这称为**有序马尔可夫性质**）。因此，我们可以将联合分布表示为：

$$  p(\mathbf{Y}_{1:N_{G}})=\prod_{i=1}^{N_{G}}p(Y_{i}|\mathbf{Y}_{\mathrm{p a}(i)})   \tag*{(3.104)}$$

其中 $ N_{G} $ 是图中的节点数。

##### 3.6.1.1 示例：洒水器网络

假设我们要对 4 个随机变量之间的依赖关系进行建模：$ C $（是否为多云季节）、$ R $（是否下雨）、$ S $（洒水器是否开启）以及 $ W $（草是否湿润）。我们知道多云季节会增加下雨的可能性，因此添加一条 $ C \rightarrow R $ 的弧。我们知道多云季节会降低开启洒水器的可能性，因此添加一条 $ C \rightarrow S $ 的弧。最后，我们知道下雨或洒水都可能导致草地湿润，因此添加 $ S \rightarrow W $ 和 $ R \rightarrow W $ 两条边。

形式上，这定义了以下联合分布：

$$  p(C,S,R,W)=p(C)p(S|C)p(R|C,\mathcal{S})p(W|S,R,\mathcal{O})   \tag*{(3.105)}$$

其中我们删除了因模型条件独立性而不需要的项（即划掉的部分）。

每个项 $ p(Y_i | \mathbf{Y}_{\text{pa}(i)}) $ 称为节点 $ i $ 的**条件概率分布**（Conditional Probability Distribution，CPD）。这可以是任意类型的分布。在图 3.14 中，我们假设每个 CPD 是条件分类分布，可表示为**条件概率表**（Conditional Probability Table，CPT）。第 $ i $ 个 CPT 可以表示为：

$$  \theta_{i j k}\triangleq p(Y_{i}=k|\mathbf{Y}_{\mathrm{p a}(i)}=j)   \tag*{(3.106)}$$

该式满足性质 $ 0 \leq \theta_{ijk} \leq 1 $ 且对于每一行 $ j $ 有 $ \sum_{k=1}^{K_i} \theta_{ijk} = 1 $。这里 $ i $ 索引节点，$ i \in [N_G] $；$ k $ 索引节点状态，$ k \in [K_i] $，其中 $ K_i $ 是节点 $ i $ 的状态数；$ j $ 索引父节点联合状态，$ j \in [J_i] $，其中 $ J_i = \prod_{p \in \text{pa}(i)} K_p $。例如，草地湿度节点有两个二元父节点，因此共有 4 个父节点状态。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_188_119_995_259.jpg" alt="图像" width="70%" /></div>

<div style="text-align: center;">图 3.15：一阶和二阶自回归（马尔可夫）模型的示意图。</div>

##### 3.6.1.2 示例：马尔可夫链

假设我们希望构建一个关于变长序列的联合概率分布 $p(y_{1:T})$。如果每个变量 $y_t$ 表示一个来自大小为 $K$ 的词汇表中的单词，即 $y_t \in \{1, \ldots, K\}$，那么该模型刻画了长度为 $T$ 的可能句子上的分布；这通常被称为语言模型。

根据概率的链式法则，我们可以将任意 $T$ 个变量的联合分布表示为：

$$ p(\boldsymbol{y}_{1:T})=p(y_{1})p(y_{2}|y_{1})p(y_{3}|y_{2},y_{1})p(y_{4}|y_{3},y_{2},y_{1})\cdots=\prod_{t=1}^{T}p(y_{t}|\boldsymbol{y}_{1:t-1}) \tag*{(3.107)}$$

不幸的是，表示每个条件分布 $p(y_t|\pmb{y}_{1:t-1})$ 所需的参数数量随 $t$ 呈指数增长。然而，假设我们做出条件独立性假设：给定当前状态 $y_t$，未来 $\pmb{y}_{t+1:T}$ 与过去 $\pmb{y}_{1:t-1}$ 独立。这称为**一阶马尔可夫条件**，由图 3.15(a) 中的概率图模型表示。基于这一假设，我们可以将联合分布写为：

$$ p(\boldsymbol{y}_{1:T})=p(y_{1})p(y_{2}|y_{1})p(y_{3}|y_{2})p(y_{4}|y_{3})\cdots=p(y_{1})\prod_{t=2}^{T}p(y_{t}|y_{t-1}) \tag*{(3.108)}$$

这被称为**马尔可夫链**、马尔可夫模型或一阶自回归模型。

函数 $p(y_t | y_{t-1})$ 称为转移函数、转移核或马尔可夫核。它只是给定 $t-1$ 时刻状态时 $t$ 时刻状态上的条件分布，因此满足条件 $p(y_t | y_{t-1}) \geq 0$ 且 $\sum_{k=1}^K p(y_t = k | y_{t-1} = j) = 1$。我们可以将此条件概率表表示为一个随机矩阵 $A_{jk} = p(y_t = k | y_{t-1} = j)$，其中每行元素之和为 1。这被称为**状态转移矩阵**。我们假设该矩阵在所有时间步上相同，因此模型被称为齐次的、平稳的或时不变的。这是**参数共享**的一个例子，因为同一参数被多个变量共享。这一假设允许我们使用固定数量的参数对任意数量的变量进行建模。

一阶马尔可夫假设相当强。幸运的是，我们可以轻松地将一阶模型推广到依赖最近 $M$ 个观测值，从而创建阶数（记忆长度）为 $M$ 的模型：

$$ p(\boldsymbol{y}_{1:T})=p(\boldsymbol{y}_{1:M})\prod_{t=M+1}^{T}p(y_{t}|\boldsymbol{y}_{t-M:t-1}) \tag*{(3.109)}$$

这称为**$M$ 阶马尔可夫模型**。例如，当 $M = 2$ 时，$y_t$ 依赖于 $y_{t-1}$ 和 $y_{t-2}$，如图 3.15(b) 所示。这被称为三元模型，因为它刻画了分布

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证

---

词三元组。如果使用 M = 1，我们得到二元模型，其建模词对上的分布。

对于大的词汇量，估计大 M 的 M-gram 模型的条件分布所需的参数数量可能变得过大。在这种情况下，我们需要做出条件独立性之外的额外假设。例如，我们可以假设 $ p(y_t|\pmb{y}_{t-M:t-1}) $ 可以表示为低秩矩阵，或某种神经网络的形式。这被称为神经语言模型。详见第15章。

#### 3.6.2 推断

概率图模型定义了一个联合概率分布。因此，我们可以使用边缘化和条件化规则来为任意变量集合 $ i $ 和 $ j $ 计算 $ p(\mathbf{Y}_i|\mathbf{Y}_j=\mathbf{y}_j) $。高效执行此计算的算法将在本书的续篇 [Mur23] 中讨论。

例如，考虑图3.14中的喷水器示例。我们对下雨的先验信念为 $ p(R=1)=0.5 $。如果我们看到草地是湿的，那么下雨的后验信念变为 $ p(R=1|W=1)=0.7079 $。现在假设我们还注意到喷水器打开了：我们对下雨的信念降至 $ p(R=1|W=1,S=1)=0.3204 $。这种多个原因对某个观测结果的负向交互作用被称为解释效应，也被称为伯克森悖论。（参见 sprinkler_pgm.ipynb 中的代码，可复现这些计算。）

#### 3.6.3 学习

如果条件概率分布的参数未知，我们可以将它们视为额外的随机变量，作为节点添加到图中，然后将其视为待推断的隐变量。图3.16(a)展示了一个简单示例，其中我们有 $N$ 个独立同分布的随机变量 $\mathbf{y}_n$，它们都从具有共同参数 $\boldsymbol{\theta}$ 的同一分布中抽取。（阴影节点表示观测值，而无阴影（空心）节点表示隐变量或参数。）

更准确地说，该模型对数据编码了以下“生成故事”：

$$  \theta\sim p(\theta)   \tag*{(3.110)}$$

$$  y_{n}\sim p(y|\boldsymbol{\theta})   \tag*{(3.111)}$$

其中 $p(\boldsymbol{\theta})$ 是参数上的某个（未指定的）先验分布，而 $p(\boldsymbol{y}|\boldsymbol{\theta})$ 是某个指定的似然函数。对应的联合分布形式为

$$  p(\mathcal{D},\boldsymbol{\theta})=p(\boldsymbol{\theta})p(\mathcal{D}|\boldsymbol{\theta})   \tag*{(3.112)}$$

其中 $ \mathcal{D} = (\boldsymbol{y}_1, \ldots, \boldsymbol{y}_N) $。根据独立同分布假设，似然可以重写如下：

$$  p(\mathcal{D}|\boldsymbol{\theta})=\prod_{n=1}^{N}p(\boldsymbol{y}_{n}|\boldsymbol{\theta})   \tag*{(3.113)}$$

注意，数据向量的顺序对于定义此模型并不重要，即我们可以置换概率图模型中叶子节点的编号。当此性质成立时，我们说数据是可交换的。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_333_115_836_404.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图3.16：左图：给定 $\boldsymbol{\theta}$ 时，数据点 $\mathbf{y}_n$ 条件独立。右图：同一模型，使用盘符号表示。该模型与左侧模型相同，只是重复的 $\mathbf{y}_n$ 节点被置于一个称为盘的方框内；右下角的数字 N 指定了 $\mathbf{y}_n$ 节点的重复次数。</div>


##### 3.6.3.1 盘符号

在图3.16(a)中，我们看到 y 节点重复了 N 次。为避免视觉混乱，通常使用一种称为盘的语法糖形式。这是一种表示约定，即我们在重复变量周围绘制一个小方框，并理解当模型展开时，方框内的节点将被重复。我们通常将副本或重复的次数写在方框的右下角。图3.16(b)对此进行了说明。这种表示法广泛用于表示某些类型的贝叶斯模型。

图3.17展示了一个更有趣的例子，我们将 GMM（第3.5.1节）表示为一个图模型。我们看到这编码了联合分布

$$ p(\boldsymbol{y}_{1:N},\boldsymbol{z}_{1:N},\boldsymbol{\theta}) = p(\boldsymbol{\pi}) \left[ \prod_{k=1}^{K} p(\boldsymbol{\mu}_{k}) p(\boldsymbol{\Sigma}_{k}) \right] \left[ \prod_{n=1}^{N} p(z_{n}|\boldsymbol{\pi}) p(\boldsymbol{y}_{n}|z_{n},\boldsymbol{\mu}_{1:K},\boldsymbol{\Sigma}_{1:K}) \right] \tag*{(3.114)} $$

我们看到潜变量 $z_n$ 以及未知参数 $\boldsymbol{\theta} = (\boldsymbol{\pi}, \boldsymbol{\mu}_{1:K}, \boldsymbol{\Sigma}_{1:K})$ 都显示为未着色的节点。

### 3.7 习题

**习题3.1** [不相关并不意味着独立 $\dagger$]

设 $X \sim U(-1,1)$，$Y = X^2$。显然 $Y$ 依赖于 $X$（实际上 $Y$ 由 $X$ 唯一确定）。然而，请证明 $\rho(X,Y) = 0$。提示：若 $X \sim U(a,b)$，则 $E[X] = (a+b)/2$，$\mathbb{V}[X] = (b-a)^2/12$。

**习题3.2** [相关系数介于 -1 和 +1 之间]

证明 $-1 \leq \rho(X, Y) \leq 1$。

**习题3.3** [线性相关变量的相关系数为 $\pm1\dagger$]

证明：若 $Y = aX + b$，其中参数 $a > 0$ 且 $b$，则 $\rho(X, Y) = 1$。类似地，证明若 $a < 0$，则 $\rho(X, Y) = -1$。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_500_116_674_549.jpg" alt="图像" width="15%" /></div>

<div style="text-align: center;">图3.17：以图模型表示的高斯混合模型。</div>

##### 练习3.4 [随机变量的线性组合]

设 $\boldsymbol{x}$ 为一个随机向量，其均值为 $\boldsymbol{m}$，协方差矩阵为 $\boldsymbol{\Sigma}$。设 $\boldsymbol{A}$ 和 $\boldsymbol{B}$ 为矩阵。

a. 推导 $\boldsymbol{Ax}$ 的协方差矩阵。

b. 证明 $\operatorname{tr}(\boldsymbol{AB}) = \operatorname{tr}(\boldsymbol{BA})$。

c. 推导 $\mathbb{E}\left[\boldsymbol{x}^T\boldsymbol{A}\boldsymbol{x}\right]$ 的表达式。

##### 练习3.5 [高斯分布与联合高斯分布]

设 $X \sim \mathcal{N}(0,1)$，$Y = WX$，其中 $p(W = -1) = p(W = 1) = 0.5$。显然 $X$ 和 $Y$ 不独立，因为 $Y$ 是 $X$ 的函数。

a. 证明 $Y \sim \mathcal{N}(0, 1)$。

b. 证明 $\operatorname{Cov}[X,Y]=0$。因此 $X$ 和 $Y$ 不相关但不独立，尽管它们都服从高斯分布。提示：使用协方差的定义

$$ \operatorname{Cov}\left[X,Y\right]=\mathbb{E}\left[XY\right]-\mathbb{E}\left[X\right]\mathbb{E}\left[Y\right] \tag*{(3.115)}$$

以及迭代期望法则

$$ \mathbb{E}\left[XY\right]=\mathbb{E}\left[\mathbb{E}\left[XY|W\right]\right] \tag*{(3.116)}$$

##### 练习3.6 [多维高斯分布的归一化常数]

证明 $d$ 维高斯分布的归一化常数为

$$ (2\pi)^{d/2}|\boldsymbol{\Sigma}|^{\frac{1}{2}}=\int\exp\left(-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^{T}\boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})\right) d\boldsymbol{x} \tag*{(3.117)}$$

《概率机器学习：导论》。在线版本。2024年11月23日

---

提示：对角化 $\mathbf{\Sigma}$，并利用 $|\mathbf{\Sigma}| = \prod_i \lambda_i$ 这一事实，将联合概率密度函数写为在变换后的坐标系中 $d$ 个一维高斯的乘积。（需要用到变量变换公式。）最后，利用单变量高斯的归一化常数。

##### 练习 3.7 [一维中已知方差下的传感器融合]

假设我们有两个传感器，其已知（且不同）的方差分别为 $v_1$ 和 $v_2$，但未知（且相同）的均值 $\mu$。假设我们从第一个传感器观测到 $n_1$ 个观测值 $y_i^{(1)} \sim \mathcal{N}(\mu, v_1)$，从第二个传感器观测到 $n_2$ 个观测值 $y_i^{(2)} \sim \mathcal{N}(\mu, v_2)$。（例如，假设 $\mu$ 是室外的真实温度，传感器1是一个精确的（低方差）数字温度传感设备，传感器2是一个不精确的（高方差）水银温度计。）令 $\mathcal{D}$ 表示来自两个传感器的所有数据。在 $\mu$ 采用无信息先验（我们可以使用精度为0的高斯来模拟）的情况下，后验 $p(\mu|\mathcal{D})$ 是什么？给出后验均值和方差的显式表达式。

##### 练习 3.8 [证明学生t分布可以写成高斯尺度混合]

证明学生t分布可以写成高斯尺度混合，其中我们使用伽马分布作为精度 $\alpha$ 的混合分布，即

$$  p(x|\mu,a,b)=\int_{0}^{\infty}\mathcal{N}(x|\mu,\alpha^{-1})\mathrm{Ga}(\alpha|a,b)d\alpha   \tag*{(3.118)}$$

这可以被视为一个具有不同精度的无限个高斯的混合。

---

请提供需要翻译的 Markdown 文本内容。

---

# 4 统计学

### 4.1 引言

在第2章至第3章中，我们假设概率模型的所有参数 $\theta$ 都是已知的。本章将讨论如何从数据中学习这些参数。

从数据 $D$ 中估计 $\theta$ 的过程称为模型拟合或训练，这是机器学习的核心。有许多方法可以生成此类估计，但大多数方法归结为如下形式的优化问题：

$$  \hat{\boldsymbol{\theta}}=\underset{\boldsymbol{\theta}}{\arg\min}\mathcal{L}(\boldsymbol{\theta})   \tag*{(4.1)}$$

其中 $\mathcal{L}(\boldsymbol{\theta})$ 是某种损失函数或目标函数。本章将讨论几种不同的损失函数。在某些情况下，我们还会讨论如何以闭式解形式求解优化问题。但一般而言，我们需要使用某种通用优化算法，这将在第8章中讨论。

除了计算点估计 $\theta$ 之外，我们还讨论如何对该估计的不确定性或置信度进行建模。在统计学中，基于有限数据样本对未知量估计的不确定性进行量化的过程称为推断。我们将讨论贝叶斯推断和频率学派推断两种方法。$^{1}$

### 4.2 最大似然估计 (MLE)

参数估计最常用的方法是选择为训练数据赋予最高概率的参数；这称为最大似然估计或MLE。下文将给出更详细的说明，并通过一系列实例进行演示。

#### 4.2.1 定义

我们将MLE定义如下：

$$  \hat{\theta}_{\mathrm{m l e}}\triangleq\operatorname*{a r g m a x}_{\theta}p(\mathcal{D}|\boldsymbol{\theta})   \tag*{(4.2)}$$

---

我们通常假设训练样本独立地来自同一分布，因此（条件）似然变为

$$  p(\mathcal{D}|\boldsymbol{\theta})=\prod_{n=1}^{N}p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})   \tag*{(4.3)}$$

这就是著名的 iid 假设，即“独立同分布”。我们通常使用对数似然，其形式为

$$  \ell(\boldsymbol{\theta})\triangleq\log p(\mathcal{D}|\boldsymbol{\theta})=\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})   \tag*{(4.4)}$$

它将分解为各项之和，每个样本对应一项。因此，MLE 为

$$  \hat{\theta}_{mle}=\underset{\theta}{\operatorname{argmax}}\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})   \tag*{(4.5)}$$

由于大多数优化算法（如第 8 章讨论的那些）都是为最小化代价函数而设计的，我们可以将目标函数重新定义为（条件）负对数似然（NLL）：

$$  \mathrm{N L L}(\boldsymbol{\theta})\triangleq-\log p(\mathcal{D}|\boldsymbol{\theta})=-\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})   \tag*{(4.6)}$$

最小化该函数将得到 MLE。如果模型是无条件的（无监督），则 MLE 变为

$$  \hat{\theta}_{mle}=\underset{\theta}{\mathrm{argmin}}-\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta})   \tag*{(4.7)}$$

因为我们有输出 $ y_{n} $ 但没有输入 $ x_{n} $。^2

另一种方式是我们可能希望最大化输入和输出的联合似然。此时 MLE 为

$$  \hat{\theta}_{mle}=\underset{\theta}{\mathrm{argmin}}-\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n},\boldsymbol{x}_{n}|\boldsymbol{\theta})   \tag*{(4.8)}$$

#### 4.2.2 MLE 的合理性论证

有多种方法可以论证 MLE 的合理性。一种方法是将其视为使用均匀先验对贝叶斯后验 $ p(\boldsymbol{\theta}|\mathcal{D}) $ 进行简单的点近似，如第 4.6.7.1 节所述。

---

具体而言，假设我们用一个δ函数来近似后验，即 $ p(\boldsymbol{\theta}|\mathcal{D}) = \delta(\boldsymbol{\theta} - \hat{\boldsymbol{\theta}}_{\mathrm{map}}) $，其中 $ \hat{\boldsymbol{\theta}}_{\mathrm{map}} $ 是后验众数，由下式给出：

$$  \hat{\boldsymbol{\theta}}_{\mathrm{map}}=\underset{\boldsymbol{\theta}}{\mathrm{argmax}}\log p(\boldsymbol{\theta}|\mathcal{D})=\underset{\boldsymbol{\theta}}{\mathrm{argmax}}\log p(\mathcal{D}|\boldsymbol{\theta})+\log p(\boldsymbol{\theta})   \tag*{(4.9)}$$

如果我们采用均匀先验 $ p(\boldsymbol{\theta}) \propto 1 $，则MAP估计等于最大似然估计（MLE），即 $ \hat{\boldsymbol{\theta}}_{\mathrm{map}} = \hat{\boldsymbol{\theta}}_{\mathrm{mle}} $。

使用MLE的另一种合理性论证是：由此得到的预测分布 $ p(\mathbf{y}|\boldsymbol{\theta}_{\mathrm{mle}}) $ 与数据的经验分布在某种意义（下文定义）上尽可能接近。在无条件情形下，经验分布定义为

$$  p_{\mathcal{D}}(\boldsymbol{y})\triangleq\frac{1}{N}\sum_{n=1}^{N}\delta(\boldsymbol{y}-\boldsymbol{y}_{n})   \tag*{(4.10)}$$

我们看到经验分布是一系列位于观测训练点处的δ函数（即“尖峰”）。我们希望构建一个模型，使其分布 $ q(\boldsymbol{y}) = p(\boldsymbol{y}|\boldsymbol{\theta}) $ 与 $ p_{\mathcal{D}}(\boldsymbol{y}) $ 相似。

衡量概率分布 $p$ 和 $q$ 之间（不）相似性的标准方法是Kullback-Leibler散度，简称KL散度。我们在第6.2节给出详细说明，但此处简要定义如下：

$$  \begin{align*}D_{\mathbb{K L}}\left(p\parallel q\right)&=\sum_{y}p(\boldsymbol{y})\log\frac{p(\boldsymbol{y})}{q(\boldsymbol{y})}\\&=\underbrace{\sum_{y}p(\boldsymbol{y})\log p(\boldsymbol{y})}_{-\mathbb{H}(p)}\underbrace{-\sum_{y}p(\boldsymbol{y})\log q(\boldsymbol{y})}_{\mathbb{H}_{ce}(p,q)}\end{align*}   \tag*{(4.12)}$$

其中 $ \mathbb{H}(p) $ 是 $ p $ 的熵（见第6.1节），$ \mathbb{H}_{ce}(p,q) $ 是 $ p $ 和 $ q $ 的交叉熵（见第6.1.2节）。可以证明 $ D_{\mathbb{K}\mathbb{L}}(p\parallel q)\geq0 $，当且仅当 $ p=q $ 时等号成立。

若令 $ q(\boldsymbol{y}) = p(\boldsymbol{y}|\boldsymbol{\theta}) $ 且 $ p(\boldsymbol{y}) = p_{\mathcal{D}}(\boldsymbol{y}) $，则KL散度变为

$$  D_{\mathbb{K L}}\left(p\parallel q\right)=\sum_{\boldsymbol{y}}\left[p_{\mathcal{D}}(\boldsymbol{y})\log p_{\mathcal{D}}(\boldsymbol{y})-p_{\mathcal{D}}(\boldsymbol{y})\log q(\boldsymbol{y})\right]   \tag*{(4.13)}$$

$$  =-\mathbb{H}(p_{\mathcal{D}})-\frac{1}{N}\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta})   \tag*{(4.14)}$$

$$  =\mathrm{const}+\mathrm{NLL}(\boldsymbol{\theta})   \tag*{(4.15)}$$

第一项为常数，可忽略，仅剩下负对数似然（NLL）。因此最小化KL等价于最小化NLL，进而等价于计算MLE，如式(4.7)所示。

我们可以将上述结果推广到有监督（条件）情形，使用如下经验分布：

$$  p_{\mathcal{D}}(\boldsymbol{x},\boldsymbol{y})=p_{\mathcal{D}}(\boldsymbol{y}|\boldsymbol{x})p_{\mathcal{D}}(\boldsymbol{x})=\frac{1}{N}\sum_{n=1}^{N}\delta(\boldsymbol{x}-\boldsymbol{x}_{n})\delta(\boldsymbol{y}-\boldsymbol{y}_{n})   \tag*{(4.16)}$$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可协议。

---

期望的KL散度由此变为

$$  \mathbb{E}_{p_{\mathcal{D}}(\boldsymbol{x})}\left[D_{\mathbb{K L}}\left(p_{\mathcal{D}}(Y|\boldsymbol{x})\parallel q(Y|\boldsymbol{x})\right)\right]=\sum_{\boldsymbol{x}}p_{\mathcal{D}}(\boldsymbol{x})\left[\sum_{\boldsymbol{y}}p_{\mathcal{D}}(\boldsymbol{y}|\boldsymbol{x})\log\frac{p_{\mathcal{D}}(\boldsymbol{y}|\boldsymbol{x})}{q(\boldsymbol{y}|\boldsymbol{x})}\right]   \tag*{(4.17)}$$

$$  =\mathrm{const}-\sum_{\boldsymbol{x},\boldsymbol{y}}p_{\mathcal{D}}(\boldsymbol{x},\boldsymbol{y})\log q(\boldsymbol{y}|\boldsymbol{x})   \tag*{(4.18)}$$

$$  =\mathrm{const}-\frac{1}{N}\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})   \tag*{(4.19)}$$

最小化该值等价于最小化式(4.6)中的条件负对数似然。

#### 4.2.3 示例：伯努利分布的最大似然估计

设Y表示抛硬币这一随机变量，其中事件Y=1对应正面，Y=0对应反面。令$\theta = p(Y=1)$为正面概率。该随机变量的概率分布为伯努利分布，我们在第2.4节曾介绍过。

伯努利分布的负对数似然由下式给出

$$   NLL(\theta)=-\log\prod_{n=1}^{N}p(y_{n}|\theta)   \tag*{(4.20)}$$

$$  =-\log\prod_{n=1}^{N}\theta^{\mathbb{I}(y_{n}=1)}(1-\theta)^{\mathbb{I}(y_{n}=0)}   \tag*{(4.21)}$$

$$  =-\sum_{n=1}^{N}\left[\mathbb{I}\left(y_{n}=1\right)\log\theta+\mathbb{I}\left(y_{n}=0\right)\log(1-\theta)\right]   \tag*{(4.22)}$$

$$  =-\left[N_{1}\log\theta+N_{0}\log(1-\theta)\right]   \tag*{(4.23)}$$

其中我们定义了$N_1 = \sum_{n=1}^N \mathbb{I}(y_n = 1)$和$N_0 = \sum_{n=1}^N \mathbb{I}(y_n = 0)$，分别表示正面和反面的次数。（二项分布的NLL与伯努利分布相同，只是多了无关的$\binom{N}{c}$项，该项是与$\theta$无关的常数。）这两个数称为数据的充分统计量，因为它们概括了关于$\mathcal{D}$所需的一切信息。总计数$N = N_0 + N_1$称为样本量。

通过求解$\frac{d}{d\theta}\mathrm{NLL}(\theta)=0$可得到最大似然估计。NLL的导数为

$$  \frac{d}{d\theta}N L L(\theta)=\frac{-N_{1}}{\theta}+\frac{N_{0}}{1-\theta}   \tag*{(4.24)}$$

因此MLE由下式给出

$$  \hat{\theta}_{mle}=\frac{N_{1}}{N_{0}+N_{1}}   \tag*{(4.25)}$$

可以看出，这仅仅是正面的经验比例，是一个直观的结果。

---

#### 4.2.4 示例：类别分布的极大似然估计

假设我们掷一个 \(K\) 面骰子 \(N\) 次。令 \(Y_n \in \{1, \ldots, K\}\) 表示第 \(n\) 次的结果，其中 \(Y_n \sim \text{Cat}(\boldsymbol{\theta})\)。我们希望从数据集 \(\mathcal{D} = \{y_n : n = 1 : N\}\) 中估计概率 \(\boldsymbol{\theta}\)。负对数似然（NLL）为

$$   NLL(\boldsymbol{\theta})=-\sum_{k}N_{k}\log\theta_{k}   \tag*{(4.26)}$$

其中 \(N_{k}\) 是观测到事件 \(Y = k\) 的次数。（多项式分布的 NLL 与此相同，仅相差无关的比例因子。）

为了计算极大似然估计，我们必须在约束 \(\sum_{k=1}^{K}\theta_{k}=1\) 下最小化 NLL。为此，我们使用拉格朗日乘子法（参见第 8.5.1 节）\(^{3}\)。

拉格朗日函数如下：

$$  \mathcal{L}(\boldsymbol{\theta},\lambda)\triangleq-\sum_{k}N_{k}\log\theta_{k}-\lambda\left(1-\sum_{k}\theta_{k}\right)   \tag*{(4.27)}$$

对 \(\lambda\) 求导得到原始约束：

$$  \frac{\partial\mathcal{L}}{\partial\lambda}=1-\sum_{k}\theta_{k}=0   \tag*{(4.28)}$$

对 \(\theta_{k}\) 求导得到

$$  \frac{\partial\mathcal{L}}{\partial\theta_{k}}=-\frac{N_{k}}{\theta_{k}}+\lambda=0\implies N_{k}=\lambda\theta_{k}   \tag*{(4.29)}$$

利用求和为 1 的约束可以解出 \(\lambda\)：

$$  \sum_{k}N_{k}=N=\lambda\sum_{k}\theta_{k}=\lambda   \tag*{(4.30)}$$

因此，极大似然估计为

$$  \hat{\theta}_{k}=\frac{N_{k}}{\lambda}=\frac{N_{k}}{N}   \tag*{(4.31)}$$

即事件 \(k\) 发生的经验频率。

#### 4.2.5 示例：单变量高斯分布的极大似然估计

假设 \(Y \sim \mathcal{N}(\mu, \sigma^2)\)，令 \(\mathcal{D} = \{y_n : n = 1 : N\}\) 为大小为 \(N\) 的独立同分布样本。我们可以通过极大似然估计来估计参数 \(\boldsymbol{\theta} = (\mu, \sigma^2)\)。首先，推导负对数似然：

$$   NLL(\mu,\sigma^{2})=-\sum_{n=1}^{N}\log\left[\left(\frac{1}{2\pi\sigma^{2}}\right)^{\frac{1}{2}}\exp\left(-\frac{1}{2\sigma^{2}}(y_{n}-\mu)^{2}\right)\right]   \tag*{(4.32)}$$

$$  =\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}(y_{n}-\mu)^{2}+\frac{N}{2}\log(2\pi\sigma^{2})   \tag*{(4.33)}$$

---

该函数的最小值必须满足以下条件，我们将在第8.1.1.1节中加以说明：

$$  \frac{\partial}{\partial\mu}\mathrm{N L L}(\mu,\sigma^{2})=0,\frac{\partial}{\partial\sigma^{2}}\mathrm{N L L}(\mu,\sigma^{2})=0   \tag*{(4.34)}$$

因此，我们只需找到这个驻点即可。通过简单的微积分运算（练习4.1）可知，解由下式给出：

$$  \hat{\mu}_{mle}=\frac{1}{N}\sum_{n=1}^{N}y_{n}=\overline{y}   \tag*{(4.35)}$$

$$  \hat{\sigma}_{mle}^{2}=\frac{1}{N}\sum_{n=1}^{N}(y_{n}-\hat{\mu}_{mle})^{2}=\frac{1}{N}\sum_{n=1}^{N}\left[y_{n}^{2}+\hat{\mu}_{mle}^{2}-2y_{n}\hat{\mu}_{mle}\right]=s^{2}-\overline{y}^{2}   \tag*{(4.36)}$$

$$  s^{2}\triangleq\frac{1}{N}\sum_{n=1}^{N}y_{n}^{2}   \tag*{(4.37)}$$

量 $ \overline{y} $ 和 $ s^{2} $ 被称为数据的**充分统计量**，因为它们足以计算最大似然估计，且在信息无损的意义上可替代原始数据本身。

请注意，您可能习惯于将方差的估计量写作

$$  \hat{\sigma}_{\mathrm{unb}}^{2}=\frac{1}{N-1}\sum_{n=1}^{N}(y_{n}-\hat{\mu}_{\mathrm{m l e}})^{2}   \tag*{(4.38)}$$

其中我们除以 $ N - 1 $。这不是最大似然估计，而是另一种类型的估计量，它恰好是无偏的（与最大似然估计不同）；详细信息参见第4.7.6.1节。$ ^{4} $

#### 4.2.6 示例：多元高斯的最大似然估计

本节我们将推导多元高斯参数的最大似然估计。

首先，写出对数似然函数，省略无关常数：

$$  \ell(\boldsymbol{\mu},\boldsymbol{\Sigma})=\log p(\mathcal{D}|\boldsymbol{\mu},\boldsymbol{\Sigma})=\frac{N}{2}\log|\boldsymbol{\Lambda}|-\frac{1}{2}\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{\mu})^{\top}\boldsymbol{\Lambda}(\boldsymbol{y}_{n}-\boldsymbol{\mu})   \tag*{(4.39)}$$

其中 $ \Lambda = \Sigma^{-1} $ 是**精度矩阵**（协方差矩阵的逆矩阵）。

---

##### 4.2.6.1 均值的最大似然估计

利用代换 $\boldsymbol{z}_n = \boldsymbol{y}_n - \boldsymbol{\mu}$、二次型的导数（公式 (7.264)）以及微积分链式法则，我们有

$$ \frac{\partial}{\partial\boldsymbol{\mu}}(\boldsymbol{y}_n - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\boldsymbol{y}_n - \boldsymbol{\mu}) = \frac{\partial}{\partial \boldsymbol{z}_n} \boldsymbol{z}_n^\top \boldsymbol{\Sigma}^{-1} \boldsymbol{z}_n \frac{\partial \boldsymbol{z}_n}{\partial \boldsymbol{\mu}^\top} \tag*{(4.40)} $$

$$ = -1 (\boldsymbol{\Sigma}^{-1} + \boldsymbol{\Sigma}^{-\top}) \boldsymbol{z}_n \tag*{(4.41)} $$

因为 $\frac{\partial \boldsymbol{z}_n}{\partial \boldsymbol{\mu}^\top} = -\boldsymbol{I}$。因此

$$ \frac{\partial}{\partial \boldsymbol{\mu}} \ell(\boldsymbol{\mu}, \boldsymbol{\Sigma}) = -\frac{1}{2} \sum_{n=1}^{N} -2 \boldsymbol{\Sigma}^{-1} (\boldsymbol{y}_n - \boldsymbol{\mu}) = \boldsymbol{\Sigma}^{-1} \sum_{n=1}^{N} (\boldsymbol{y}_n - \boldsymbol{\mu}) = 0 \tag*{(4.42)} $$

$$ \hat{\boldsymbol{\mu}} = \frac{1}{N} \sum_{n=1}^{N} \boldsymbol{y}_n = \overline{\boldsymbol{y}} \tag*{(4.43)} $$

所以 $\boldsymbol{\mu}$ 的最大似然估计就是经验均值。

##### 4.2.6.2 协方差矩阵的最大似然估计

我们可以利用迹技巧（公式 (7.36)）将对数似然重新用精度矩阵 $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ 表示如下：

$$ \ell(\hat{\boldsymbol{\mu}}, \boldsymbol{\Lambda}) = \frac{N}{2} \log |\boldsymbol{\Lambda}| - \frac{1}{2} \sum_n \mathrm{tr} \left[ (\boldsymbol{y}_n - \hat{\boldsymbol{\mu}})(\boldsymbol{y}_n - \hat{\boldsymbol{\mu}})^\top \boldsymbol{\Lambda} \right] \tag*{(4.44)} $$

$$ = \frac{N}{2} \log |\boldsymbol{\Lambda}| - \frac{1}{2} \mathrm{tr} \left[ \mathbf{S}_{\overline{y}} \boldsymbol{\Lambda} \right] \tag*{(4.45)} $$

$$ \mathbf{S}_{\overline{y}} \triangleq \sum_{n=1}^{N} (\boldsymbol{y}_n - \overline{\boldsymbol{y}})(\boldsymbol{y}_n - \overline{\boldsymbol{y}})^\top = \left( \sum_n \boldsymbol{y}_n \boldsymbol{y}_n^\top \right) - N \overline{\boldsymbol{y}} \, \overline{\boldsymbol{y}}^\top \tag*{(4.46)} $$

其中 $\mathbf{S}_{\overline{y}}$ 是以 $\bar{y}$ 为中心的散布矩阵。

我们可以将散布矩阵更紧凑地重写如下：

$$ \mathbf{S}_{\overline{y}} = \tilde{\mathbf{Y}}^\top \tilde{\mathbf{Y}} = \mathbf{Y}^\top \mathbf{C}_N^\top \mathbf{C}_N \mathbf{Y} = \mathbf{Y}^\top \mathbf{C}_N \mathbf{Y} \tag*{(4.47)} $$

其中

$$ \mathbf{C}_N \triangleq \mathbf{I}_N - \frac{1}{N} \mathbf{1}_N \mathbf{1}_N^\top \tag*{(4.48)} $$

是中心化矩阵，它通过从每一行中减去均值 $\overline{y} = \frac{1}{N} \mathbf{Y}^\top \mathbf{1}_N$ 将 $\mathbf{Y}$ 转换为 $\tilde{\mathbf{Y}}$。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_209_124_555_334.jpg" alt="图像" width="30%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_617_124_962_334.jpg" alt="图像" width="29%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 4.1：(a) 第 1.2.1.1 节中鸢尾花数据集特征的协方差矩阵。(b) 相关矩阵。由于矩阵是对称的且对角线元素为 1，我们只显示下三角。将此图与图 1.3 比较。由 iris_cov_mat.ipymb 生成。</div>

利用第 7.8 节的结果，我们可以计算损失对 $ \Lambda $ 的导数，得到

$$  \frac{\partial\ell(\hat{\boldsymbol{\mu}},\boldsymbol{\Lambda})}{\partial\boldsymbol{\Lambda}}=\frac{N}{2}\boldsymbol{\Lambda}^{-T}-\frac{1}{2}\mathbf{S}\frac{\boldsymbol{\tau}}{\boldsymbol{y}}=\mathbf{0}   \tag*{(4.49)}$$

$$  \mathbf{\Lambda}^{-\top}=\mathbf{\Lambda}^{-1}=\mathbf{\Sigma}=\frac{1}{N}\mathbf{S}_{\overline{y}}   \tag*{(4.50)}$$

$$  \hat{\mathbf{\Sigma}}=\frac{1}{N}\sum_{n=1}^{N}(\mathbf{y}_{n}-\overline{\mathbf{y}})(\mathbf{y}_{n}-\overline{\mathbf{y}})^{\mathsf{T}}=\frac{1}{N}\mathbf{Y}^{\mathsf{T}}\mathbf{C}_{N}\mathbf{Y}   \tag*{(4.51)}$$

因此，协方差矩阵的最大似然估计（MLE）即为经验协方差矩阵。参见 Figure 4.1a 的示例。

有时使用公式 (3.8) 定义的相关矩阵更为方便。这可以通过下式计算：

$$  \mathrm{corr}(\mathbf{Y})=(\mathrm{diag}(\boldsymbol{\Sigma}))^{-\frac{1}{2}}\boldsymbol{\Sigma}\left(\mathrm{diag}(\boldsymbol{\Sigma})\right)^{-\frac{1}{2}}   \tag*{(4.52)}$$

其中 $ \text{diag}(\boldsymbol{\Sigma})^{-\frac{1}{2}} $ 是对角矩阵，其元素为 $ 1/\sigma_i $。参见 Figure 4.1b 的示例。

然而，需要注意的是，MLE 可能会过拟合或数值不稳定，尤其是当样本数 $ N $ 相对于维度数 $ D $ 较小时。主要问题在于 $ \boldsymbol{\Sigma} $ 有 $ O(D^2) $ 个参数，因此我们可能需要大量数据才能可靠地估计它。具体而言，从公式 (4.51) 可以看出，当 $ N < D $ 时，满秩协方差矩阵的 MLE 是奇异的。即使当 $ N > D $ 时，MLE 也可能病态，即接近奇异。我们将在第 4.5.2 节讨论此问题的解决方案。

#### 4.2.7 示例：线性回归的 MLE

我们在第 2.6.3 节简要提到了线性回归。回忆它对应以下模型：

$$  p(y|\boldsymbol{x};\boldsymbol{\theta})=\mathcal{N}(y|\boldsymbol{w}^{\top}\boldsymbol{x},\sigma^{2})   \tag*{(4.53)}$$

---

其中 $\boldsymbol{\theta} = (\boldsymbol{w}, \sigma^2)$。我们暂且假设 $\sigma^2$ 是固定的，并将重点放在估计权重 $\boldsymbol{w}$ 上。负对数似然（NLL）由下式给出：

$$   NLL(\boldsymbol{w})=-\sum_{n=1}^{N}\log\left[\left(\frac{1}{2\pi\sigma^{2}}\right)^{\frac{1}{2}}\exp\left(-\frac{1}{2\sigma^{2}}(y_{n}-\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{n})^{2}\right)\right]   \tag*{(4.54)}$$

去掉无关的加法常数后，得到如下简化目标函数，即残差平方和（RSS）：

$$  \mathrm{RSS}(\boldsymbol{w})\triangleq\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{n})^{2}=\sum_{n=1}^{N}r_{n}^{2}   \tag*{(4.55)}$$

其中 $r_{n}$ 是第 $n$ 个残差误差。除以样本数量 $N$ 后得到均方误差（MSE）：

$$  \mathrm{MSE}(\boldsymbol{w})=\frac{1}{N}\mathrm{RSS}(\boldsymbol{w})=\frac{1}{N}\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{w}^{\top}\boldsymbol{x}_{n})^{2}   \tag*{(4.56)}$$

最后，取平方根得到均方根误差（RMSE）：

$$  \mathrm{RMSE}(\boldsymbol{w})=\sqrt{\mathrm{MSE}(\boldsymbol{w})}=\sqrt{\frac{1}{N}\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{w}^{\mathrm{T}}\boldsymbol{x}_{n})^{2}}   \tag*{(4.57)}$$

我们可以通过最小化 NLL、RSS、MSE 或 RMSE 来计算极大似然估计（MLE）。由于这些目标函数除了无关常数外完全相同，因此它们会给出相同的结果。

现在让我们关注 RSS 目标。它可以写成矩阵形式如下：

$$  \mathrm{R S S}(\boldsymbol{w})=\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{w}^{\top}\boldsymbol{x}_{n})^{2}=||\mathbf{X}\boldsymbol{w}-\boldsymbol{y}||_{2}^{2}=(\mathbf{X}\boldsymbol{w}-\boldsymbol{y})^{\top}(\mathbf{X}\boldsymbol{w}-\boldsymbol{y})   \tag*{(4.58)}$$

在 11.2.2.1 节中，我们将证明最优解出现在 $\nabla_w \mathrm{RSS}(\boldsymbol{w}) = \mathbf{0}$ 处，并满足以下方程：

$$  \hat{\boldsymbol{w}}_{\mathrm{m l e}}\triangleq\underset{\boldsymbol{w}}{\arg\min}\mathrm{R S S}(\boldsymbol{w})=(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\boldsymbol{y}   \tag*{(4.59)}$$

这就是普通最小二乘（OLS）估计，并且等价于 MLE。

### 4.3 经验风险最小化（ERM）

我们可以通过将式(4.6)中的（条件）对数损失项 $\ell(\boldsymbol{y}_n, \boldsymbol{\theta}; \boldsymbol{x}_n) = -\log p(\boldsymbol{y}_n | \boldsymbol{x}_n, \boldsymbol{\theta})$ 替换为任意其他损失函数，来推广 MLE，从而得到

$$  \mathcal{L}(\boldsymbol{\theta})=\frac{1}{N}\sum_{n=1}^{N}\ell(\boldsymbol{y}_{n},\boldsymbol{\theta};\boldsymbol{x}_{n})   \tag*{(4.60)}$$

这被称为经验风险最小化（ERM），因为它是对经验分布取期望的期望损失。详见 5.4 节。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 4.3.1 示例：最小化误分类率

如果我们在解决一个分类问题，可能会希望使用0-1损失：

$$  \ell_{01}(\boldsymbol{y}_{n},\boldsymbol{\theta};\boldsymbol{x}_{n})=\begin{cases}0&if\boldsymbol{y}_{n}=f(\boldsymbol{x}_{n};\boldsymbol{\theta})\\1&if\boldsymbol{y}_{n}\neq f(\boldsymbol{x}_{n};\boldsymbol{\theta})\end{cases}   \tag*{(4.61)}$$

其中 $ f(\boldsymbol{x};\boldsymbol{\theta}) $ 是某种形式的预测器。经验风险变为：

$$  \mathcal{L}(\boldsymbol{\theta})=\frac{1}{N}\sum_{n=1}^{N}\ell_{01}(\boldsymbol{y}_{n},\boldsymbol{\theta};\boldsymbol{x}_{n})   \tag*{(4.62)}$$

这正是在训练集上的经验误分类率。

注意，对于二分类问题，我们可以用如下符号重写误分类率。设 $ \tilde{y} \in \{-1, +1\} $ 为真实标签，$ \hat{y} \in \{-1, +1\} = f(\boldsymbol{x}; \boldsymbol{\theta}) $ 为我们的预测。我们按如下方式定义0-1损失：

$$  \ell_{01}(\tilde{y},\hat{y})=\mathbb{I}\left(\tilde{y}\neq\hat{y}\right)=\mathbb{I}\left(\tilde{y}\hat{y}<0\right)   \tag*{(4.63)}$$

对应的经验风险变为：

$$  \mathcal{L}(\boldsymbol{\theta})=\frac{1}{N}\sum_{n=1}^{N}\ell_{01}(y_{n},\hat{y}_{n})=\frac{1}{N}\sum_{n=1}^{N}\mathbb{I}\left(\tilde{y}_{n}\hat{y}_{n}<0\right)   \tag*{(4.64)}$$

其中对 $ \pmb{x}_{n} $ 和 $ \pmb{\theta} $ 的依赖是隐含的。

#### 4.3.2 替代损失

遗憾的是，第4.3.1节中使用的0-1损失是一个非光滑的阶跃函数，如图4.2所示，这使其难以优化。（事实上，它是NP难的[BDEL03]。）在本节中，我们考虑使用替代损失函数[BJM06]。通常选择的替代损失应是一个尽可能紧的凸上界，从而易于最小化。

例如，考虑一个概率二分类器，它在标签上生成如下分布：

$$  p(\tilde{y}|\boldsymbol{x},\boldsymbol{\theta})=\sigma(\tilde{y}\eta)=\frac{1}{1+e^{-\tilde{y}\eta}}   \tag*{(4.65)}$$

其中 $ \eta = f(\boldsymbol{x}; \boldsymbol{\theta}) $ 是对数几率。因此对数损失由下式给出：

$$ \ell_{l l}(\tilde{y},\eta)=-\log p(\tilde{y}|\eta)=\log(1+e^{-\tilde{y}\eta}) $$

图4.2展示了这是0-1损失的一个光滑上界，其中我们绘制了损失随 $ \tilde{y}\eta $ 变化的曲线，后者称为“边际”（margin），因为它定义了远离阈值0的一个“安全边际”。由此可见，最小化负对数似然等价于最小化经验0-1损失的一个（相当紧的）上界。

0-1损失的另一个凸上界是铰链损失，定义如下：

$$  \ell_{\mathrm{h i n g e}}(\tilde{y},\eta)=\max(0,1-\tilde{y}\eta)\triangleq(1-\tilde{y}\eta)_{+}   \tag*{(4.67)}$$

该损失也在图4.2中绘制；我们可以看到它具有部分打开的门的铰链形状。这是0-1损失的凸上界，尽管它仅仅是分段可微的，而非处处可微。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_417_151_741_393.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">图4.2：二分类中各种损失函数的图示。横轴为间隔 $ z = \tilde{y}\eta $，纵轴为损失值。0-1损失为 $ \mathbb{I}(z < 0) $。Hinge损失为 $ \max(0, 1 - z) $。Log损失为 $ \log_2(1 + e^{-z}) $。Exp损失为 $ e^{-z} $。由 hinge_loss_plot.ipymb 生成。</div>


### 4.4 其他估计方法 *

#### 4.4.1 矩估计法

计算极大似然估计（MLE）需要求解方程 $ \nabla_{\theta}\text{NLL}(\boldsymbol{\theta}) = \mathbf{0} $。有时这在计算上很困难。在这种情况下，我们可以使用一种更简单的方法，称为矩估计法（method of moments，MOM）。该方法将分布的**理论矩**与经验矩相等，并求解由此得到的 $ K $ 个联立方程组，其中 $ K $ 是参数个数。理论矩由 $ \mu_k = \mathbb{E}\left[Y^k\right] $ 给出（ $ k = 1 : K $ ），经验矩由下式给出：

$$  \hat{\mu}_{k}=\frac{1}{N}\sum_{n=1}^{n}y_{n}^{k}   \tag*{(4.68)}$$

因此只需对每个 $ k $ 求解 $ \mu_k = \hat{\mu}_k $ 即可。下面给出一些例子。

矩估计法虽然简单，但在理论上劣于MLE方法，因为它可能无法有效利用所有数据（关于这些理论结果的细节，参见例如[CB02]）。此外，它有时会产生不一致的估计（参见第4.4.1.2节）。不过，当它能给出有效估计时，可用来初始化用于优化负对数似然（NLL）的迭代算法（参见例如[AHK12]），从而将MOM的计算效率与MLE的统计准确性结合起来。

##### 4.4.1.1 示例：一元高斯分布的矩估计法

例如，考虑一元高斯分布的情况。由第4.2.5节可知：

$$  \mu_{1}=\mu=\overline{y}   \tag*{(4.69)}$$

$$  \mu_{2}=\sigma^{2}+\mu^{2}=s^{2}   \tag*{(4.70)}$$

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND许可。

---

其中 $ \overline{y} $ 是经验均值，$ s^2 $ 是经验平均平方和。因此 $ \hat{\mu} = \overline{y} $，$ \hat{\sigma}^2 = s^2 - \overline{y}^2 $。在这种情况下，矩估计与最大似然估计相同，但情况并非总是如此。

##### 4.4.1.2 示例：均匀分布的矩估计

本节给出矩估计应用于均匀分布的一个示例，介绍内容参考了维基百科页面。$ ^{5} $ 设 $ Y \sim \text{Unif}(\theta_1, \theta_2) $ 为均匀随机变量，则

$$  p(y|\theta)=\frac{1}{\theta_{2}-\theta_{1}}\mathbb{I}\left(\theta_{1}\leq y\leq\theta_{2}\right)   \tag*{(4.71)}$$

其前两阶矩为

$$  \mu_{1}=\mathbb{E}\left[Y\right]=\frac{1}{2}(\theta_{1}+\theta_{2})   \tag*{(4.72)}$$

$$  \mu_{2}=\mathbb{E}\left[Y^{2}\right]=\frac{1}{3}(\theta_{1}^{2}+\theta_{1}\theta_{2}+\theta_{2}^{2})   \tag*{(4.73)}$$

求解上述方程可得

$$  (\theta_{1},\theta_{2})=\left(\mu_{1}-\sqrt{3(\mu_{2}-\mu_{1}^{2})},2\mu_{1}-\theta_{1}\right)   \tag*{(4.74)}$$

遗憾的是，该估计量有时会产生无效结果。例如，假设 $ \mathcal{D} = \{0, 0, 0, 0, 1\} $。经验矩为 $ \hat{\mu}_1 = \frac{1}{5} $ 和 $ \hat{\mu}_2 = \frac{1}{5} $，因此估计参数为 $ \hat{\theta}_1 = \frac{1}{5} - \frac{2\sqrt{3}}{5} = -0.493 $ 和 $ \hat{\theta}_2 = \frac{1}{5} + \frac{2\sqrt{3}}{5} = 0.893 $。然而，这不可能是正确的参数，因为若 $ \theta_2 = 0.893 $，则无法生成像 1 这样大的样本。

相比之下，考虑最大似然估计。令 $ y_{(1)} \leq y_{(2)} \leq \cdots \leq y_{(N)} $ 为数据的顺序统计量（即按递增顺序排列的值）。令 $ \theta = \theta_2 - \theta_1 $。则似然函数为

$$  p(\mathcal{D}|\boldsymbol{\theta})=(\boldsymbol{\theta})^{-N}\mathbb{I}\left(y_{(1)}\geq\theta_{1}\right)\mathbb{I}\left(y_{(N)}\leq\theta_{2}\right)   \tag*{(4.75)}$$

在 $ \theta $ 的允许范围内，对数似然的导数为

$$  \frac{d}{d\theta}\log p(\mathcal{D}|\theta)=-\frac{N}{\theta}<0   \tag*{(4.76)}$$

因此似然函数是 $ \theta $ 的递减函数，故应选取

$$  \hat{\theta}_{1}=y_{(1)},\hat{\theta}_{2}=y_{(N)}   \tag*{(4.77)}$$

在上述示例中，得到 $ \hat{\theta}_{1}=0 $ 和 $ \hat{\theta}_{2}=1 $，这与预期一致。

---

#### 4.4.2 在线（递归）估计

如果整个数据集 D 在训练开始前就已全部可用，我们称之为**批量学习**。然而，在某些情况下，数据集是顺序到达的，例如 $\mathcal{D} = \{y_1, y_2, \ldots\}$ 构成一个无界流。此时，我们希望进行**在线学习**。

设 $\hat{\theta}_{t-1}$ 是基于 $\mathcal{D}_{1:t-1}$ 得到的估计（如MLE）。为确保学习算法每次更新耗时恒定，我们需要找到如下形式的学习规则：

$$  \boldsymbol{\theta}_{t}=f(\hat{\boldsymbol{\theta}}_{t-1},\boldsymbol{y}_{t})   \tag*{(4.78)}$$

这称为**递归更新**。下面给出一些此类在线学习方法的示例。

##### 4.4.2.1 示例：高斯均值的递归MLE

我们重新审视第4.2.5节的示例，其中计算了单变量高斯分布的MLE。已知均值的批量估计为：

$$  \hat{\boldsymbol{\mu}}_{t}=\frac{1}{t}\sum_{n=1}^{t}\boldsymbol{y}_{n}   \tag*{(4.79)}$$

这仅仅是数据的累积和，因此可以轻松将其转换为递归估计：

$$  \begin{aligned}\hat{\boldsymbol{\mu}}_{t}&=\frac{1}{t}\sum_{n=1}^{t}\boldsymbol{y}_{n}=\frac{1}{t}\left((t-1)\hat{\boldsymbol{\mu}}_{t-1}+\boldsymbol{y}_{t}\right)\\&=\hat{\boldsymbol{\mu}}_{t-1}+\frac{1}{t}(\boldsymbol{y}_{t}-\hat{\boldsymbol{\mu}}_{t-1})\end{aligned}   \tag*{(4.80)}$$

这被称为**移动平均**。

从式(4.81)可以看出，新估计值等于旧估计值加上一个修正项。修正项的幅度随时间（即随着获得更多样本）逐渐减小。然而，如果分布是变化的，我们希望给更新的数据赋予更大的权重。我们将在第4.4.2.2节讨论如何实现这一点。

##### 4.4.2.2 指数加权移动平均

式(4.81)展示了如何计算信号的**移动平均**。在本节中，我们将展示如何调整它以赋予最近样本更大的权重。具体来说，我们将计算以下**指数加权移动平均**（EWMA，亦称指数移动平均或EMA）：

$$  \hat{\boldsymbol{\mu}}_{t}=\beta\boldsymbol{\mu}_{t-1}+(1-\beta)\boldsymbol{y}_{t}   \tag*{(4.82)}$$

其中 $0 < \beta < 1$。过去 $k$ 步的数据点的贡献会被权重 $\beta^k(1 - \beta)$ 加权。因此，旧数据的贡献呈指数衰减。具体地，有：

$$  \hat{\boldsymbol{\mu}}_{t}=\beta\boldsymbol{\mu}_{t-1}+(1-\beta)\boldsymbol{y}_{t}   \tag*{(4.83)}$$

$$  =\beta^{2}\pmb{\mu}_{t-2}+\beta(1-\beta)\pmb{y}_{t-1}+(1-\beta)\pmb{y}_{t}   \tag*{...}$$

$$  =\beta^{t}\boldsymbol{y}_{0}+(1-\beta)\beta^{t-1}\boldsymbol{y}_{1}+\cdots+(1-\beta)\beta\boldsymbol{y}_{t-1}+(1-\beta)\boldsymbol{y}_{t}   \tag*{(4.85)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_221_119_542_338.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_632_121_950_339.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图4.3：有偏修正和无偏修正的指数加权移动平均示意图。(a) 短记忆：$ \beta = 0.9 $。(b) 长记忆：$ \beta = 0.99 $。由 ema_demo.ipynb 生成。</div>


几何级数的和由下式给出：

$$  \beta^{t}+\beta^{t-1}+\cdots+\beta^{1}+\beta^{0}=\frac{1-\beta^{t+1}}{1-\beta}   \tag*{(4.86)}$$

因此

$$  \left(1-\beta\right)\sum_{k=0}^{t}\beta^{k}=\left(1-\beta\right)\frac{1-\beta^{t+1}}{1-\beta}=1-\beta^{t+1}   \tag*{(4.87)}$$

由于 $ 0 < \beta < 1 $，当 $ t \to \infty $ 时，有 $ \beta^{t+1} \to 0 $，因此较小的 $ \beta $ 会更快地遗忘过去，更迅速地适应最近的数据。如图4.3所示。

由于初始估计从 $ \hat{\mu}_0 = 0 $ 开始，存在初始偏差。可以通过如下缩放进行修正[KB15]：

$$  \tilde{\mu}_{t}=\frac{\hat{\mu}_{t}}{1-\beta^{t}}   \tag*{(4.88)}$$

（注意，式(4.82)中的更新仍然应用于未修正的EMA $ \hat{\mu}_{t-1} $，然后再对当前时间步进行修正。）其好处如图4.3所示。

### 4.5 正则化

MLE和ERM的一个基本问题是，它们会试图选择在训练集上损失最小的参数，但这可能不会导致模型在未来数据上具有低损失。这被称为过拟合。

举一个简单的例子，假设我们想预测抛硬币时正面朝上的概率。我们抛了 $N=3$ 次，观察到 $3$ 次正面。MLE为 $\hat{\theta}_{\text{mle}} = N_1/(N_0 + N_1) = 3/(3 + 0) = 1$（参见第4.2.3节）。然而，如果使用 $\text{Ber}(y|\hat{\theta}_{\text{mle}})$ 进行预测，我们将预测未来所有抛硬币结果都是正面，这似乎不太可能。