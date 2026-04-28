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

#### 6.3.6 标准化互信息

在某些应用中，使用介于 0 和 1 之间的标准化依赖度量非常有用。下面介绍一种构建此类度量的方法。

首先，注意到

$$  \begin{aligned}\mathbb{I}\left(X;Y\right)&=\mathbb{H}\left(X\right)-\mathbb{H}\left(X|Y\right)\leq\mathbb{H}\left(X\right)\\&=\mathbb{H}\left(Y\right)-\mathbb{H}\left(Y|X\right)\leq\mathbb{H}\left(Y\right)\end{aligned}   \tag*{(6.71)}$$

因此

$$  0\leq\mathbb{I}\left(X;Y\right)\leq\min\left(\mathbb{H}\left(X\right),\mathbb{H}\left(Y\right)\right)   \tag*{(6.73)}$$

于是，我们可以将标准化互信息定义为：

$$  NMI(X,Y)=\frac{\mathbb{I}\left(X;Y\right)}{\min\left(\mathbb{H}\left(X\right),\mathbb{H}\left(Y\right)\right)}\leq1   \tag*{(6.74)}$$

该标准化互信息的值域为 0 到 1。当 $ NMI(X,Y) = 0 $ 时，有 $ \mathbb{I}(X;Y) = 0 $，因此 X 和 Y 相互独立。当 $ NMI(X,Y) = 1 $ 且 $ \mathbb{H}(X) < \mathbb{H}(Y) $ 时，有

$$  \mathbb{I}\left(X;Y\right)=\mathbb{H}\left(X\right)-\mathbb{H}\left(X|Y\right)=\mathbb{H}\left(X\right)\Longrightarrow\mathbb{H}\left(X|Y\right)=0   \tag*{(6.75)}$$

此时 X 是 Y 的确定性函数。例如，假设 X 是一个离散随机变量，其概率质量函数为 [0.5, 0.25, 0.25]。我们有 $ MI(X, X) = 1.5 $（使用以 2 为底的对数）和 $ H(X) = 1.5 $，因此标准化互信息为 1，这符合预期。

对于连续随机变量，由于需要估计对量化水平敏感的微分熵，对互信息进行标准化较为困难。进一步讨论参见第 6.3.7 节。

#### 6.3.7 最大信息系数

如第 6.3.6 节所述，拥有互信息的标准化估计值很有用，但对于实值数据，计算该值可能较为棘手。一种称为最大信息系数（MIC）的方法 [Res+11] 定义了如下量：

$$  \mathrm{MIC}(X,Y)=\max_{G}\frac{\mathbb{I}((X,Y)|_{G})}{\log\left|\left|G\right|\right|}   \tag*{(6.76)}$$

其中 $G$ 是二维网格的集合，$(X,Y)|_G$ 表示变量在该网格上的离散化，$|G|$ 是 $\min(G_x,G_y)$，而 $G_x$ 和 $G_y$ 分别为 x 方向和 y 方向的网格单元数。（网格的最大分辨率取决于样本量 $n$；他们建议限制网格使得 $G_xG_y \leq B(n)$，其中 $B(n) = n^\alpha$，$\alpha = 0.6$。）分母是均匀联合分布的熵；除以该值可确保 $0 \leq \text{MIC} \leq 1$。

该统计量的直观依据如下：如果 X 和 Y 之间存在关系，则应当存在某种二维输入空间的离散网格划分能够捕捉该关系。由于我们不知道应使用何种网格，MIC 会搜索不同的网格分辨率（例如 $ 2 \times 2 $、$ 2 \times 3 $ 等）以及网格边界的位置。给定一个网格后，可以轻松地对数据进行量化并计算

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可协议

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_139_747_359.jpg" alt="图片" width="50%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_792_167_1014_351.jpg" alt="图片" width="19%" /></div>

<div style="text-align: center;">图 6.5：最大信息系数（MIC）计算方法的示意图。(a) 我们在不同的网格分辨率和网格单元位置上进行搜索，并计算每个位置的 MI。(b) 对于每种网格分辨率 $(k, l)$，我们定义集合 $M(k, l)$ 为该尺寸下任何网格所能达到的最大 MI，并以 $\log(\min(k, l))$ 进行归一化。(c) 我们可视化矩阵 M。其中的最大值（用星号标记）被定义为 MIC。本图改编自 [Res+11] 的图 1，经 David Reshef 许可使用。</div>

MI。我们定义特征矩阵 $M(k,l)$ 为任何尺寸为 $(k,l)$ 的网格所能达到的最大 MI，并以 $\log(\min(k,l))$ 进行归一化。MIC 即为该矩阵中的最大值，$ \max_{kl \leq B(n)} M(k,l) $。图 6.5 直观展示了这一计算过程。

在 [Res+11] 中，他们证明该量具有一种称为 **公平性**（equitability）的属性，这意味着无论关系类型（如线性、非线性、非函数关系）如何，对于噪声程度相同的关系，它都会给出相似的分数。

在 [Res+16] 中，他们提出了一种改进的估计量，称为 MICE，其计算效率更高，且只需在一维网格上进行优化，可以通过动态规划在 $O(n)$ 时间内完成。他们还引入了另一个量，称为 TICe（总信息含量），它在小样本下检测关系的能力更强，但公平性较低。该量定义为 $\sum_{k \leq B(n)} M(k, l)$。他们建议使用 TICe 初步筛选大量候选关系，然后使用 MICE 量化关系强度。关于这两个指标的高效实现，可参见 [Alb+18]。

我们可以将 MIC 为 0 解释为变量之间无关系，而 MIC 为 1 表示任意形式的无噪声关系。图 6.6 对此进行了说明。与相关系数不同，MIC 不局限于寻找线性关系。因此，MIC 被称为“21 世纪的相关系数”[Spe11]。

在图 6.7 中，我们给出了一个来自 [Res+11] 的更有趣的例子。数据包含由世界卫生组织（WHO）收集的 357 个变量，测量了各种社会、经济、健康和人口统计指标。在图的左侧，我们看到所有 63,546 个变量对的相关系数（CC）与 MIC 的散点图。在图的右侧，我们看到了特定变量对的散点图，现讨论如下：

- 标记为 C 的点（图中靠近 (0,0) 的位置）具有较低的 CC 和较低的 MIC。对应的散点图清楚地表明，这两个变量（因伤害丧失的生命百分比与人口中牙医密度）之间没有关系。

- 标记为 D 和 H 的点具有较高的 CC（绝对值）和较高的 MIC，这是因为

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_281_119_882_403.jpg" alt="图像" width="52%" /></div>


<div style="text-align: center;">图 6.6：一些二维分布及其相关系数 $ R^{2} $ 和最大信息系数（MIC）的估计值图。与图 3.1 比较。由 MIC_correlation_2d.ipynb 生成。</div>


表示近似线性关系。

- 标记为 E、F 和 G 的点具有较低的相关系数但较高的 MIC。这是因为它们对应于变量之间的非线性（有时，如 E 和 F 的情况，非函数关系，即一对多）关系。

#### 6.3.8 数据加工不等式

假设我们有一个未知变量 X，并观测到它的一个带噪声的函数，记作 Y。如果我们以某种方式处理这些带噪声的观测值以创建新变量 Z，直观上显然我们无法增加关于未知量 X 的信息量。这就是所谓的数据加工不等式。下面我们更正式地陈述它，然后给出证明。

**定理 6.3.1.** 假设 $ X \to Y \to Z $ 构成一个马尔可夫链，即 $ X \perp Z|Y $。那么 $ \mathbb{I}(X;Y) \geq \mathbb{I}(X;Z) $。

**证明.** 利用互信息的链式法则（公式 (6.62)），我们可以用两种方式展开互信息：

$$  \begin{aligned}\mathbb{I}\left(X;Y,Z\right)&=\mathbb{I}\left(X;Z\right)+\mathbb{I}\left(X;Y|Z\right)\\&=\mathbb{I}\left(X;Y\right)+\mathbb{I}\left(X;Z|Y\right)\end{aligned}   \tag*{(6.77)}$$

由于 $ X \perp Z|Y $，我们有 $ \mathbb{I}(X; Z|Y) = 0 $，因此

$$  \mathbb{I}\left(X;Z\right)+\mathbb{I}\left(X;Y|Z\right)=\mathbb{I}\left(X;Y\right)   \tag*{(6.79)}$$

由于 $ \mathbb{I}(X;Y|Z)\geq0 $，我们有 $ \mathbb{I}(X;Y)\geq\mathbb{I}(X;Z) $。类似地，可以证明 $ \mathbb{I}(Y;Z)\geq\mathbb{I}(X;Z) $。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_205_127_973_467.jpg" alt="图像" width="66%" /></div>


<div style="text-align: center;">图 6.7：左图：WHO 数据中所有成对关系的相关系数 vs 最大信息准则 (MIC)。右图：某些变量对的散点图。红色线条是针对每个趋势分别拟合的非参数平滑回归。图片来自 [Res+11] 的图 4，经 David Reshef 许可使用。</div>


#### 6.3.9 充分统计量

数据处理不等式的一个重要推论如下。假设我们有链 $\theta \to \mathcal{D} \to s(\mathcal{D})$。那么

$$ \mathbb{I}\left(\theta;s(\mathcal{D})\right)\leq\mathbb{I}\left(\theta;\mathcal{D}\right) \tag*{(6.80)}$$

如果上式取等号，则称 $s(\mathcal{D})$ 是数据 $\mathcal{D}$ 关于推断 $\theta$ 的 **充分统计量**。在这种情况下，我们可以等价地写为 $\theta \to s(\mathcal{D}) \to \mathcal{D}$，因为从知道 $s(\mathcal{D})$ 重构数据与从知道 $\theta$ 重构数据同样准确。

一个充分统计量的例子是数据本身，即 $ s(\mathcal{D}) = \mathcal{D} $，但这并不实用，因为它完全没有对数据进行概括。因此，我们将 **最小充分统计量** $ s(\mathcal{D}) $ 定义为一个充分统计量，且它不包含关于 $\theta$ 的任何额外信息；即 $ s(\mathcal{D}) $ 在无损预测 $\theta$ 相关信息的前提下，最大程度地压缩了数据 $\mathcal{D}$。更正式地说，如果对于所有充分统计量 $ s'(\mathcal{D}) $，都存在某个函数 $ f $ 使得 $ s(\mathcal{D}) = f(s'(\mathcal{D})) $，则称 $ s $ 是 $\mathcal{D}$ 的 **最小充分统计量**。我们可以将情况总结如下：

$$ \theta\to s(\mathcal{D})\to s^{\prime}(\mathcal{D})\to\mathcal{D} \tag*{(6.81)}$$

这里 $ s'(\mathcal{D}) $ 在 $ s(\mathcal{D}) $ 的基础上添加了冗余信息，从而形成一对多的映射。例如，对于一组 $ N $ 次伯努利试验，其最小充分统计量就是 $ N $ 和 $ N_1 = \sum_n \mathbb{I}(X_n = 1) $，即成功次数。换句话说，我们不需要记录整个正反面序列及其顺序，只需记录正反面的总数。类似地，对于推断已知方差的高斯分布均值，我们只需要知道经验均值和样本数量。

---

#### 6.3.10 Fano不等式 *

一种常见的特征选择方法是挑选与响应变量 Y 具有高互信息的输入特征 $ X_{d} $。下面我们将论证这一做法的合理性。具体而言，我们陈述一个被称为 **Fano不等式** 的结论，该结论给出了（任意方法的）误分类概率下界，该下界用特征 X 与类别标签 Y 之间的互信息表示。

**定理 6.3.2 (Fano不等式)**。考虑一个估计量 $ \hat{Y} = f(X) $，使得 $ Y \to X \to \hat{Y} $ 构成一个马尔可夫链。令 E 表示事件 $ \hat{Y} \neq Y $，即发生错误，并令 $ P_e = P(Y \neq \hat{Y}) $ 为错误概率。那么我们有

$$  \mathbb{H}\left(Y|X\right)\leq\mathbb{H}\left(Y|\hat{Y}\right)\leq\mathbb{H}\left(E\right)+P_{e}\log\left|\mathcal{Y}\right|   \tag*{(6.82)}$$

由于 $ \mathbb{H}(E) \leq 1 $（如图 6.1 所示），我们可以将该结果弱化为

$$  1+P_{e}\log\left|\mathcal{Y}\right|\geq\mathbb{H}\left(Y|X\right)   \tag*{(6.83)}$$

进而得到

$$  P_{e}\geq\frac{\mathbb{H}(Y|X)-1}{\log|\mathcal{Y}|}   \tag*{(6.84)}$$

因此，最小化 $ \mathbb{H}(Y|X) $（可通过最大化 $ \mathbb{I}(X;Y) $ 实现）也将最小化 $ P_e $ 的下界。

**证明**。（摘自 [CT06, p38]。）利用熵的链式法则，我们有

$$  \begin{aligned}\mathbb{H}\left(E,Y|\hat{Y}\right)&=\mathbb{H}\left(Y|\hat{Y}\right)+\underbrace{\mathbb{H}\left(E|Y,\hat{Y}\right)}_{=0}\\&=\mathbb{H}\left(E|\hat{Y}\right)+\mathbb{H}\left(Y|E,\hat{Y}\right)\end{aligned}   \tag*{(6.85)}$$

由于条件作用会降低熵（参见第 6.2.4 节），我们有 $ \mathbb{H}\left(E|\hat{Y}\right) \leq \mathbb{H}(E) $。最后一项可以按如下方式界定：

$$  \begin{aligned}\mathbb{H}\left(Y|E,\hat{Y}\right)&=P(E=0)\mathbb{H}\left(Y|\hat{Y},E=0\right)+P(E=1)\mathbb{H}\left(Y|\hat{Y},E=1\right)\\&\leq(1-P_{e})0+P_{e}\log|\mathcal{Y}|\end{aligned}   \tag*{(6.87)}$$

因此

$$  \mathbb{H}\left(Y|\hat{Y}\right)\leq\underbrace{\mathbb{H}\left(E|\hat{Y}\right)}_{\leq\mathbb{H}(E)}+\underbrace{\mathbb{H}\left(Y|E,\hat{Y}\right)}_{P_{e}\log|\mathcal{Y}|}   \tag*{(6.89)}$$

最后，由数据处理不等式，我们有 $ \mathbb{I}(Y;\hat{Y})\leq\mathbb{I}(Y;X) $，故 $ \mathbb{H}(Y|X)\leq\mathbb{H}\left(Y|\hat{Y}\right) $，从而得到式 (6.82)。

作者：Kevin P. Murphy。 (C) MIT 出版社。遵循 CC-BY-NC-ND 许可协议。

---

### 6.4 习题

**习题 6.1** [用熵表示互信息 †]

证明以下恒等式：

$$  I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)   \tag*{(6.90)}$$

以及

$$  H(X,Y)=H(X|Y)+H(Y|X)+I(X;Y)   \tag*{(6.91)}$$

**习题 6.2** [ $ D(p||q) $ 与 $ \chi^{2} $ 统计量之间的关系 †]

（来源：[CT91, Q12.2]。）

证明：若 $ p(x) \approx q(x) $，则

$$  D_{\mathbb{K L}}\left(p\parallel q\right)\approx\frac{1}{2}\chi^{2}   \tag*{(6.92)}$$

其中

$$  \chi^{2}=\sum_{x}\frac{\left(p(x)-q(x)\right)^{2}}{q(x)}   \tag*{(6.93)}$$

提示：写作

$$  p(x)=\Delta(x)+q(x)   \tag*{(6.94)}$$

$$  \frac{p(x)}{q(x)}=1+\frac{\Delta(x)}{q(x)}   \tag*{(6.95)}$$

并利用 $ \log(1+x) $ 的泰勒级数展开：

$$  \log(1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}\cdots   \tag*{(6.96)}$$

其中 $ -1 < x \leq 1 $。

**习题 6.3** [熵的趣味练习 †]

（来源：Mackay。）

考虑联合分布 $  p(X, Y)  $

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td colspan="4">x</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td rowspan="4">y</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/32</td><td style='text-align: center; word-wrap: break-word;'>1/32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/32</td><td style='text-align: center; word-wrap: break-word;'>1/32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

a. 联合熵 $ H(X,Y) $ 是多少？

b. 边缘熵 $ H(X) $ 和 $ H(Y) $ 分别是多少？

c. 给定特定 y 值条件下 X 的熵定义为

$$  H(X|Y=y)=-\sum_{x}p(x|y)\log p(x|y)   \tag*{(6.97)}$$

计算每个 y 值对应的 $ H(X|y) $。在观察到 Y 后，X 的后验熵是否会增加？

---

d. 条件熵定义为

$$ H(X|Y)=\sum_{y}p(y)H(X|Y=y) \tag*{(6.98)} $$

计算该条件熵。在对 Y 的可能值取平均后，X 的后验熵是增加还是减少？

e. X 和 Y 之间的互信息是多少？

##### 习题 6.4 [前向 KL 散度与反向 KL 散度]

（来源：[Mac03] 的习题 33.7。）考虑一个对联合分布 $p(x, y)$ 的因子化近似 $q(x, y) = q(x)q(y)$。证明：为了最小化前向 KL 散度 $D_{\mathbb{K}\mathbb{L}}(p \parallel q)$，应令 $q(x) = p(x)$ 且 $q(y) = p(y)$，即最优近似是边缘分布的乘积。

现在考虑如下联合分布，其中行代表 y，列代表 x：

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/4</td></tr></table>

证明对于该 $p$，反向 KL 散度 $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ 有三个不同的极小值。找出这些极小值，并计算在每个极小值处的 $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ 值。如果令 $q(x,y) = p(x)p(y)$，那么 $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ 的值是多少？

---



---

## 7 线性代数

本章由 Zico Kolter 合著。

### 7.1 引言

线性代数是研究矩阵和向量的学科。本章总结了本书后续内容所需的核心知识。更多信息可参见其他资料，如 [Str09; Ips09; Kle13; Mol04; TB97; Axl15; Th017; Agg20; LLM14]。

#### 7.1.1 符号约定

本节定义若干符号。

##### 7.1.1.1 向量

向量 $ x \in \mathbb{R}^n $ 是由 $ n $ 个数组成的列表，通常写作列向量

$$  \begin{aligned}&\boldsymbol{x}=\begin{bmatrix}x_{1}\\x_{2}\\\vdots\\x_{n}\end{bmatrix}.\end{aligned}   \tag*{(7.1)}$$

全 1 向量记作 1。全 0 向量记作 0。单位向量 $ e_i $ 是一个除第 i 个分量为 1 外其余分量均为 0 的向量：

$$  e_{i}=(0,\ldots,0,1,0,\ldots,0)   \tag*{(7.2)}$$

这也称为**独热向量**（one-hot vector）。

##### 7.1.1.2 矩阵

矩阵 $ \mathbf{A} \in \mathbb{R}^{m \times n} $ 具有 $ m $ 行和 $ n $ 列，是一个按如下方式排列的二维数组：

$$  \mathbf{A}=\left[\begin{array}{cccc}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\\\end{array}\right].   \tag*{(7.3)}$$

---

如果 m = n，则称该矩阵为方阵。

我们使用记号 $ A_{ij} $ 或 $ A_{i,j} $ 表示矩阵 A 在第 i 行第 j 列的元素。我们使用记号 $ A_{i,:} $ 表示第 $ i $ 行，$ A_{:,j} $ 表示第 $ j $ 列。默认情况下，我们将所有向量视为列向量（因此 $ A_{i,:} $ 被视为具有 n 个元素的列向量）。我们使用粗体大写字母表示矩阵，粗体小写字母表示向量，非粗体字母表示标量。

我们可以将矩阵视为沿水平轴堆叠的一组列：

$$  \mathbf{A}=\left[\begin{array}{ccc}\mid&\mid&\\\mathbf{A}_{:,1}&\mathbf{A}_{:,2}&\cdots&\mathbf{A}_{:,n}\\\mid&\mid&&\mid\end{array}\right].   \tag*{(7.4)}$$

为简洁起见，我们将其记为

$$  \mathbf{A}=[\mathbf{A}_{:,1},\mathbf{A}_{:,2},\ldots,\mathbf{A}_{:,n}]   \tag*{(7.5)}$$

我们也可以将矩阵视为沿垂直轴堆叠的一组行：

$$  \mathbf{A}=\left[\begin{array}{ccc}-\mathbf{A}_{1,:}^{\mathsf{T}}&-\\\mathbf{A}_{2,:}^{\mathsf{T}}&-\\\vdots&\\\mathbf{A}_{m,:}^{\mathsf{T}}&-\end{array}\right].   \tag*{(7.6)}$$

为简洁起见，我们将其记为

$$  \mathbf{A}=[\mathbf{A}_{1,:};\mathbf{A}_{2,:};\cdots;\mathbf{A}_{m,:}]   \tag*{(7.7)}$$

（注意此处使用了分号。）

矩阵的转置是通过“翻转”行和列得到的。给定一个矩阵 $ \mathbf{A} \in \mathbb{R}^{m \times n} $，其转置记为 $ \mathbf{A}^\top \in \mathbb{R}^{n \times m} $，定义为

$$  (\mathbf{A}^{\mathsf{T}})_{i j}=A_{j i}   \tag*{(7.8)}$$

以下转置性质易于验证：

$$  (\mathbf{A}^{\mathsf{T}})^{\mathsf{T}}=\mathbf{A}   \tag*{(7.9)}$$

$$  \left(\mathbf{A}\mathbf{B}\right)^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}   \tag*{(7.10)}$$

$$  \left(\mathbf{A}+\mathbf{B}\right)^{\mathrm{T}}=\mathbf{A}^{\mathrm{T}}+\mathbf{B}^{\mathrm{T}}   \tag*{(7.11)}$$

如果一个方阵满足 $ \mathbf{A} = \mathbf{A}^\top $，则称之为对称矩阵。我们将所有 $ n $ 阶对称矩阵的集合记为 $ \mathbb{S}^n $。

##### 7.1.1.3 张量

张量（在机器学习术语中）是二维数组向更多维度的推广，如 Figure 7.1 所示。例如，三维张量的元素记为 $ A_{ijk} $。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_371_125_798_402.jpg" alt="Image" width="37%" /></div>


<div style="text-align: center;">图7.1：一维向量、二维矩阵和三维张量的图示。颜色用于表示向量的各个元素；该数字列表也可以存储在一个二维矩阵中，如图所示。（在此示例中，矩阵按列主序排列，这与Python所使用的顺序相反。）我们还可以将向量重塑为三维张量，如图所示。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_283_541_482_684.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_689_548_891_688.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图7.2：(a) 行主序与 (b) 列主序的图示。来自 https://commons.wikimedia.org/wiki/File:Row_and_column_major_order.svg。经维基百科作者Cmqlee慷慨许可使用。</div>


维度的数量称为张量的阶或秩。 $^{1}$ 在数学中，张量可以看作定义多重线性映射的一种方式，正如矩阵可以用来定义线性函数一样，尽管我们不需要使用这种解释。

我们可以通过将矩阵的列依次堆叠来将其重塑为向量，如图7.1所示。这表示为

$$  \operatorname{vec}(\mathbf{A})=[\mathbf{A}_{:,1};\cdots;\mathbf{A}_{:,n}]\in\mathbb{R}^{mn\times1}   \tag*{(7.12)}$$

相反，我们可以将向量重塑为矩阵。有两种实现方式，分别称为行主序（由Python和C++等语言使用）和列主序（由Julia、Matlab、R和Fortran等语言使用）。图7.2展示了它们之间的差异。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_184_113_568_350.jpg" alt="图像" width="33%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_681_118_905_341.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 7.3: (a) 上方：向量 v（蓝色）加到另一个向量 w（红色）上。下方：w 乘以因子 2 进行缩放，得到和 v + 2w。来自 https://en.wikipedia.org/wiki/Vector_space。经维基百科作者 IkamusumeFan 许可使用。(b) 用不同基表示的  $ R^2 $ 中的向量 v（蓝色）：使用  $ R^2 $ 的标准基， $ v = xe_1 + ye_2 $（黑色）；以及使用一个不同的非正交基： $ v = f_1 + f_2 $（红色）。来自 https://en.wikipedia.org/wiki/Vector_space。经维基百科作者 Jakob.scholbach 许可使用。</div>


#### 7.1.2 向量空间

本节讨论线性代数中的一些基本概念。

##### 7.1.2.1 向量加法与缩放

我们可以将向量  $ \boldsymbol{x} \in \mathbb{R}^n $ 视为定义  $ n $ 维欧氏空间中的一个点。向量空间是这类向量的集合，这些向量可以相加，并可通过 **标量**（一维数）进行缩放，从而生成新的点。这些运算按明显的逐元素方式定义，即  $ \boldsymbol{x} + \boldsymbol{y} = (x_1 + y_1, \ldots, x_n + y_n) $ 和  $ \boldsymbol{c}\boldsymbol{x} = (c x_1, \ldots, c x_n) $，其中  $ c \in \mathbb{R} $。示意图见图 7.3a。

##### 7.1.2.2 线性无关、张成空间与基

如果一组向量 $\{x_1, x_2, \ldots, x_n\}$ 中没有一个向量可以表示为其余向量的线性组合，则称这组向量 **线性无关**。反之，如果一个向量可以表示为其余向量的线性组合，则称它是 **线性相关** 的。例如，如果存在某个 $\{ \alpha_1, \ldots, \alpha_{n-1} \}$ 使得

$$  \boldsymbol{x}_{n}=\sum_{i=1}^{n-1}\alpha_{i}\boldsymbol{x}_{i}   \tag*{(7.13)}$$

则 $x_n$ 与 $\{x_1, \ldots, x_{n-1}\}$ 线性相关；否则，它与 $\{x_1, \ldots, x_{n-1}\}$ 线性无关。

一组向量 $\{x_1, x_2, \ldots, x_n\}$ 的 **张成空间** 是能够表示为 $\{x_1, \ldots, x_n\}$ 的线性组合的所有向量的集合。即

$$  \mathrm{span}(\left\{\boldsymbol{x}_{1},\cdots,\boldsymbol{x}_{n}\right\})\triangleq\left\{\boldsymbol{v}:\boldsymbol{v}=\sum_{i=1}^{n}\alpha_{i}\boldsymbol{x}_{i},\alpha_{i}\in\mathbb{R}\right\}.   \tag*{(7.14)}$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

可以证明，如果 $\{x_1, \ldots, x_n\}$ 是一组 $n$ 个线性无关的向量，其中每个 $x_i \in \mathbb{R}^n$，那么 $\operatorname{span}(\{x_1, \ldots, x_n\}) = \mathbb{R}^n$。换句话说，任何向量 $v \in \mathbb{R}^n$ 都可以表示为 $x_1$ 到 $x_n$ 的线性组合。

基 $\mathcal{B}$ 是一组线性无关的向量，它们张成整个空间，即 $\text{span}(\mathcal{B}) = \mathbb{R}^n$。通常有多种基可供选择，如图 7.3b 所示。标准基使用坐标向量 $e_1 = (1, 0, \ldots, 0)$ 到 $e_n = (0, 0, \ldots, 0, 1)$。这使我们能够在将 $\mathbb{R}^2$ 中的向量视为“平面中的箭头”（以原点为起点）或视为一个有序数字列表（对应于每个基向量的系数）之间来回转换。

##### 7.1.2.3 线性映射与矩阵

线性映射或线性变换是指满足以下条件的任意函数 $f: \mathcal{V} \to \mathcal{W}$：对所有 $\boldsymbol{v}, \boldsymbol{w} \in \mathcal{V}$，有 $f(\boldsymbol{v} + \boldsymbol{w}) = f(\boldsymbol{v}) + f(\boldsymbol{w})$ 和 $f(a\ \boldsymbol{v}) = a\ f(\boldsymbol{v})$。一旦选定了 $\mathcal{V}$ 的基，线性映射 $f: \mathcal{V} \to \mathcal{W}$ 就由基向量的像完全确定，因为 $\mathcal{V}$ 中的任何元素都可以唯一地表示为它们的线性组合。

假设 $\mathcal{V} = \mathbb{R}^n$ 且 $\mathcal{W} = \mathbb{R}^m$。我们可以对 $\mathcal{V}$ 中的每个基向量计算 $f(\boldsymbol{v}_i) \in \mathbb{R}^m$，并将它们存储在一个 $m \times n$ 矩阵 $\mathbf{A}$ 的各列中。然后，对于任意 $\boldsymbol{x} \in \mathbb{R}^n$，我们可以按如下方式计算 $\boldsymbol{y} = f(\boldsymbol{x}) \in \mathbb{R}^m$：

$$  \boldsymbol{y}=\left(\sum_{j=1}^{n}a_{1j}x_{j},\ldots,\sum_{j=1}^{n}a_{mj}x_{j}\right)   \tag*{(7.15)}$$

这相当于将向量 $\boldsymbol{x}$ 与矩阵 $\mathbf{A}$ 相乘：

$$  y=\mathbf{A}x   \tag*{(7.16)}$$

详见第 7.2 节。

如果该函数是可逆的，我们可以写出

$$  \boldsymbol{x}=\mathbf{A}^{-1}\boldsymbol{y}   \tag*{(7.17)}$$

详见第 7.3 节。

##### 7.1.2.4 矩阵的值域与零空间

假设我们将矩阵 $\mathbf{A} \in \mathbb{R}^{m \times n}$ 视为 $\mathbb{R}^m$ 中的一组 $n$ 个向量。该矩阵的**值域**（有时也称为**列空间**）是 $\mathbf{A}$ 的各列张成的空间。换句话说，

$$  \mathrm{range}(\mathbf{A})\triangleq\{\boldsymbol{v}\in\mathbb{R}^{m}:\boldsymbol{v}=\mathbf{A}\boldsymbol{x},\boldsymbol{x}\in\mathbb{R}^{n}\}.   \tag*{(7.18)}$$

这可以理解为由 $\mathbf{A}$ 可以“到达”或“生成”的向量集合；它是 $\mathbb{R}^m$ 的一个子空间，其维度由 $\mathbf{A}$ 的**秩**给出（见第 7.1.4.3 节）。矩阵 $\mathbf{A} \in \mathbb{R}^{m \times n}$ 的**零空间**是所有与 $\mathbf{A}$ 相乘后被映射到零向量的向量集合，即

$$  \mathsf{n u l l s p a c e}(\mathbf{A})\triangleq\{\mathbf{x}\in\mathbb{R}^{n}:\mathbf{A}\mathbf{x}=\mathbf{0}\}.   \tag*{(7.19)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_388_134_781_400.jpg" alt="图片" width="34%" /></div>

<div style="text-align: center;">图7.4: 一个 $ m \times n $ 矩阵A的零空间和值域的可视化。这里 $ \mathbf{y}_1 = \mathbf{A}\mathbf{x}_1 $ 且 $ \mathbf{y}_2 = \mathbf{A}\mathbf{x}_4 $，所以 $ \mathbf{y}_1 $ 和 $ \mathbf{y}_2 $ 在A的值域中（可从某个 $ \mathbf{x} $ 到达）。此外 $ \mathbf{A}\mathbf{x}_2 = \mathbf{0} $ 且 $ \mathbf{A}\mathbf{x}_3 = \mathbf{0} $，所以 $ \mathbf{x}_2 $ 和 $ \mathbf{x}_3 $ 在A的零空间中（被映射到0）。我们看到值域通常是映射输入域的一个子集。</div>

A的行张成的空间是A的零空间的补空间。

See Figure 7.4 展示了矩阵的值域和零空间。我们将在下文第7.5.4节讨论如何数值计算矩阵的值域和零空间。

##### 7.1.2.5 线性投影

向量 $ \boldsymbol{y} \in \mathbb{R}^m $ 在 $ \{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_n\} $ 张成的空间上的投影（这里假设 $ \boldsymbol{x}_i \in \mathbb{R}^m $）是一个向量 $ \boldsymbol{v} \in \text{span}(\{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_n\}) $，使得 $ \boldsymbol{v} $ 尽可能接近 $ \boldsymbol{y} $，由欧几里得范数 $ \|\boldsymbol{v} - \boldsymbol{y}\|_2 $ 度量。我们将投影记为 $ \text{Proj}(\boldsymbol{y};\{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_n\}) $，并可以正式定义为

$$  \operatorname{P r o j}(y;\{x_{1},\dots,x_{n}\})=\operatorname{a r g m i n}_{v\in\operatorname{s p a n}(\{x_{1},\dots,x_{n}\})}\|y-v\|_{2}.   \tag*{(7.20)}$$

给定一个（满秩）矩阵 $ \mathbf{A} \in \mathbb{R}^{m \times n} $ 且 $ m \geq n $，我们可以定义向量 $ \mathbf{y} \in \mathbb{R}^m $ 在 $ \mathbf{A} $ 的值域上的投影如下：

$$  \operatorname{P r o j}(\mathbf{y};\mathbf{A})=\operatorname{a r g m i n}_{\mathbf{v}\in\mathcal{R}(\mathbf{A})}\|\mathbf{v}-\mathbf{y}\|_{2}=\mathbf{A}(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}\mathbf{y}\enspace.   \tag*{(7.21)}$$

这与第11.2.2.2节中的正规方程相同。

#### 7.1.3 向量和矩阵的范数

在本节中，我们讨论衡量向量和矩阵“大小”的方法。

##### 7.1.3.1 向量范数

向量 $ \|x\| $ 的范数，非正式地说，是对向量“长度”的一种度量。更正式地，范数是任何满足4个性质的函数 $ f: \mathbb{R}^n \to \mathbb{R} $：

• 对所有 $ x \in \mathbb{R}^n $，有 $ f(x) \geq 0 $（非负性）。

"概率机器学习：导论"。在线版本。2024年11月23日。

---

### 7.1. 引言

•  $  f(x) = 0  $ 当且仅当 $  x = 0  $ （正定性）。

• 对于所有 $ x \in \mathbb{R}^n $, $ t \in \mathbb{R} $, 有 $ f(tx) = |t|f(x) $ （绝对齐次性）。

• 对于所有 $ x, y \in \mathbb{R}^n $, 有 $ f(x + y) \leq f(x) + f(y) $ （三角不等式）。

考虑以下常见例子：

p-范数  $ \|x\|_{p} = (\sum_{i=1}^{n}|x_{i}|^{p})^{1/p} $, 其中 $ p \geq 1 $。

2-范数  $ \|x\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2} $，也称为欧几里得范数。注意 $ \|x\|_2^2 = x^\top x $。

1-范数  $ \|x\|_1 = \sum_{i=1}^n |x_i| $。

最大范数  $ \|x\|_\infty = \max_i |x_i| $。

0-范数  $ \|x\|_0 = \sum_{i=1}^n \mathbb{I}(|x_i| > 0) $。这是一个伪范数，因为它不满足齐次性。它统计 $ \mathbf{x} $ 中非零元素的个数。若定义 $ 0^0 = 0 $，则可将其写为 $ \|x\|_0 = \sum_{i=1}^n x_i^0 $。

##### 7.1.3.2 矩阵范数

假设我们将矩阵 $ \mathbf{A} \in \mathbb{R}^{m \times n} $ 视为一个线性函数 $ f(\boldsymbol{x}) = \mathbf{A}\boldsymbol{x} $。我们定义 $ \mathbf{A} $ 的**诱导范数**为 $ f $ 能够拉伸任意单位范数输入的最大幅度：

$$  \left|\left|\mathbf{A}\right|\right|_{p}=\max_{\mathbf{x}\neq\mathbf{0}}\frac{\left|\left|\mathbf{A}\mathbf{x}\right|\right|_{p}}{\left|\left|\mathbf{x}\right|\right|_{p}}=\max_{\left|\left|\mathbf{x}\right|\right|=1}\left|\left|\mathbf{A}\mathbf{x}\right|\right|_{p}   \tag*{(7.22)}$$

通常取 $ p = 2 $，此时有

$$  ||\mathbf{A}||_{2}=\sqrt{\lambda_{\max}(\mathbf{A}^{\mathsf{T}}\mathbf{A})}=\max_{i}\sigma_{i}   \tag*{(7.23)}$$

其中 $ \lambda_{\max}(\mathbf{M}) $ 是 $ \mathbf{M} $ 的最大特征值，$ \sigma_{i} $ 是第 $ i $ 个奇异值。

核范数（也称迹范数）定义为

$$  \left|\left|\mathbf{A}\right|\right|_{*}=\mathrm{tr}(\sqrt{\mathbf{A}^{\mathsf{T}}\mathbf{A}})=\sum_{i}\sigma_{i}   \tag*{(7.24)}$$

其中 $ \sqrt{A^{\top}A} $ 是矩阵平方根。由于奇异值总是非负的，我们有

$$  \left|\left|\mathbf{A}\right|\right|_{*}=\sum_{i}\left|\sigma_{i}\right|=\left|\left|\boldsymbol{\sigma}\right|\right|_{1}   \tag*{(7.25)}$$

使用该范数作为正则化项会促使许多奇异值变为零，从而得到低秩矩阵。更一般地，我们可以定义 Schatten p-范数为

$$  \left|\left|\mathbf{A}\right|\right|_{p}=\left(\sum_{i}\sigma_{i}^{p}(\mathbf{A})\right)^{1/p}   \tag*{(7.26)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

如果将矩阵视为向量，我们可以基于向量范数来定义矩阵范数：$ \|A\| = \|vec{v}c(A)\| $。若向量范数为2-范数，则对应的矩阵范数为 **Frobenius 范数**：

$$  |\mathbf{A}||_{F}=\sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}^{2}}=\sqrt{\mathrm{tr}(\mathbf{A}^{\mathsf{T}}\mathbf{A})}=||\mathrm{vec}(\mathbf{A})||_{2}   \tag*{(7.27)}$$

如果直接计算 $ \mathbf{A} $ 代价高昂，但计算 $ \mathbf{A}v $（对于随机向量 $ \mathbf{v} $）较为廉价，我们可以利用式 (7.37) 中的 Hutchinson 迹估计器来构造 Frobenius 范数的随机近似：

$$  ||\mathbf{A}||_{F}^{2}=\mathrm{tr}(\mathbf{A}^{\mathsf{T}}\mathbf{A})=\mathbb{E}\left[\mathbf{v}^{\mathsf{T}}\mathbf{A}^{\mathsf{T}}\mathbf{A}\mathbf{v}\right]=\mathbb{E}\left[||\mathbf{A}\mathbf{v}||_{2}^{2}\right]   \tag*{(7.28)}$$

其中 v ∼ N(0,1)。

#### 7.1.4 矩阵的性质

本节讨论矩阵的若干标量性质。

##### 7.1.4.1 方阵的迹

方阵 $ \mathbf{A} \in \mathbb{R}^{n \times n} $ 的迹，记为 $ \text{tr}(\mathbf{A}) $，是矩阵对角元素之和：

$$  \mathrm{tr}(\mathbf{A})\triangleq\sum_{i=1}^{n}A_{ii}.   \tag*{(7.29)}$$

迹具有以下性质，其中 $ c \in \mathbb{R} $ 为标量，$ \mathbf{A}, \mathbf{B} \in \mathbb{R}^{n \times n} $ 为方阵：

 $$ \mathrm{tr}(\mathbf{A})=\mathrm{tr}(\mathbf{A}^{\mathsf{T}}) $$ 

$$  \mathrm{tr}(\mathbf{A}+\mathbf{B})=\mathrm{tr}(\mathbf{A})+\mathrm{tr}(\mathbf{B})   \tag*{(7.30)}$$

$$  \mathrm{tr}(\boldsymbol{c}\mathbf{A})=c\mathrm{tr}(\mathbf{A})   \tag*{(7.31)}$$

$$  \mathrm{tr}(\mathbf{A}\mathbf{B})=\mathrm{tr}(\mathbf{B}\mathbf{A})   \tag*{(7.33)}$$

$$  \mathrm{tr}(\mathbf{A})=\sum_{i=1}^{n}\lambda_{i}  \quad \text{其中} \ \lambda_{i} \ \text{为} \ \mathbf{A} \ \text{的特征值}   \tag*{(7.34)}$$

此外，还有以下重要的循环置换性质：对于使得 ABC 为方阵的 A, B, C 有

 $$ \mathrm{tr}(\mathbf{ABC})=\mathrm{tr}(\mathbf{B}\mathbf{CA})=\mathrm{tr}(\mathbf{C}\mathbf{A}\mathbf{B}) $$ 

由此可导出 **迹技巧**，将标量内积 $ \boldsymbol{x}^{\top}\boldsymbol{A}\boldsymbol{x} $ 重写为

$$  \boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}=\mathrm{tr}(\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x})=\mathrm{tr}(\boldsymbol{x}\boldsymbol{x}^{\top}\mathbf{A})   \tag*{(7.36)}$$

---

在某些情况下，计算矩阵 $\mathbf{A}$ 可能代价高昂，但我们可以廉价地计算矩阵-向量积 $\mathbf{A}\mathbf{v}$。假设 $\mathbf{v}$ 是一个随机向量，且满足 $\mathbf{E}\left[\mathbf{v}\mathbf{v}^{\mathrm{T}}\right]=\mathbf{I}$。此时，我们可以利用以下恒等式构造 $\operatorname{tr}(\mathbf{A})$ 的蒙特卡罗近似：

$$  \mathrm{tr}(\mathbf{A})=\mathrm{tr}(\mathbf{A}\mathbb{E}\left[\mathbf{v}\mathbf{v}^{\mathrm{T}}\right])=\mathbb{E}\left[\mathrm{tr}(\mathbf{A}\mathbf{v}\mathbf{v}^{\mathrm{T}})\right]=\mathbb{E}\left[\mathrm{tr}(\mathbf{v}^{\mathrm{T}}\mathbf{A}\mathbf{v})\right]=\mathbb{E}\left[\mathbf{v}^{\mathrm{T}}\mathbf{A}\mathbf{v}\right]   \tag*{(7.37)}$$

这被称为哈钦森迹估计器（Hutchinson trace estimator）[Hut90]。

##### 7.1.4.2 方阵的行列式

方阵的行列式，记作 $\det(\mathbf{A})$ 或 $|\mathbf{A}|$，是衡量该矩阵作为线性变换时改变单位体积程度的量。（其正式定义相当复杂，此处无需赘述。）

行列式算子满足以下性质，其中 $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{n \times n}$：

$$  \left|\mathbf{A}\right|=\left|\mathbf{A}^{\mathrm{T}}\right|   \tag*{(7.38)}$$

$$  |c\mathbf{A}|=c^{n}|\mathbf{A}|   \tag*{(7.39)}$$

$$  \left|\mathbf{A}\mathbf{B}\right|=\left|\mathbf{A}\right|\left|\mathbf{B}\right|   \tag*{(7.40)}$$

$$  \left|\mathbf{A}\right|=0 \text{ 当且仅当 } \mathbf{A} \text{ 是奇异矩阵}   \tag*{(7.41)}$$

$$  \left|\mathbf{A}^{-1}\right|=1/\left|\mathbf{A}\right| \text{ 若 } \mathbf{A} \text{ 是非奇异矩阵}   \tag*{(7.42)}$$

$$  \left|\mathbf{A}\right|=\prod_{i=1}^{n}\lambda_{i} \text{，其中 } \lambda_{i} \text{ 是 } \mathbf{A} \text{ 的特征值}   \tag*{(7.43)}$$

对于正定矩阵 $\mathbf{A}$，我们可以写作 $\mathbf{A} = \mathbf{L}\mathbf{L}^{\top}$，其中 $\mathbf{L}$ 是下三角乔列斯基分解（Cholesky decomposition）。此时有：

$$  \det(\mathbf{A})=\det(\mathbf{L})\det(\mathbf{L}^{\top})=\det(\mathbf{L})^{2}   \tag*{(7.44)}$$

因此：

$$  \log\det(\mathbf{A})=2\log\det(\mathbf{L})=2\log\prod_{i}L_{ii}=2\operatorname{tr}(\log(\operatorname{diag}(\mathbf{L})))   \tag*{(7.45)}$$

##### 7.1.4.3 矩阵的秩

矩阵 $\mathbf{A}$ 的列秩（column rank）是其列向量所张成空间的维数，行秩（row rank）是其行向量所张成空间的维数。线性代数中的一个基本事实（可利用第7.5节讨论的SVD加以证明）是：对任意矩阵 $\mathbf{A}$，恒有 $\text{列秩}(\mathbf{A}) = \text{行秩}(\mathbf{A})$，因此这一量值简称为 $\mathbf{A}$ 的秩，记作 $\text{rank}(\mathbf{A})$。以下是秩的一些基本性质：

* 对于 $\mathbf{A} \in \mathbb{R}^{m \times n}$，$\text{rank}(\mathbf{A}) \leq \min(m, n)$。若 $\text{rank}(\mathbf{A}) = \min(m, n)$，则称 $\mathbf{A}$ 为满秩（full rank）矩阵，否则称为秩亏（rank deficient）矩阵。

 $$ \bullet\quad \text{对于 } \mathbf{A} \in \mathbb{R}^{m \times n}，\text{rank}(\mathbf{A}) = \text{rank}(\mathbf{A}^{\mathsf{T}}) = \text{rank}(\mathbf{A}^{\mathsf{T}}\mathbf{A}) = \text{rank}(\mathbf{A}\mathbf{A}^{\mathsf{T}}). $$ 

* 对于 $A \in \mathbb{R}^{m \times n}$，$B \in \mathbb{R}^{n \times p}$，有 $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$。

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可协议。

---

• 对于 $ \mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n} $，有 $\operatorname{rank}(\mathbf{A} + \mathbf{B}) \leq \operatorname{rank}(\mathbf{A}) + \operatorname{rank}(\mathbf{B})$。

可以证明，一个方阵如果是满秩的，则是可逆的。

##### 7.1.4.4 条件数

矩阵 A 的条件数是衡量涉及 A 的任何计算数值稳定性的一种度量。其定义如下：

$$  \kappa(\mathbf{A})\triangleq||\mathbf{A}||\cdot||\mathbf{A}^{-1}||   \tag*{(7.46)}$$

其中 $ \|\mathbf{A}\| $ 是矩阵的范数。我们可以证明 $ \kappa(\mathbf{A}) \geq 1 $。（条件数取决于我们使用的范数；除非另有说明，否则我们假定为 $ \ell_2 $ 范数。）

我们称 A 是良态的，如果 $ \kappa(\mathbf{A}) $ 很小（接近 1）；称 A 是病态的，如果 $ \kappa(\mathbf{A}) $ 很大。大的条件数意味着 A 接近奇异。与行列式的大小相比，这是衡量接近奇异程度的更好度量。例如，假设 $ \mathbf{A} = 0.1\mathbf{I}_{100 \times 100} $。那么 $ \det(\mathbf{A}) = 10^{-100} $，这表明 A 接近奇异，但 $ \kappa(\mathbf{A}) = 1 $，这意味着 A 是良态的，反映了这样一个事实：$ \mathbf{A}x $ 只是将 $ \mathbf{x} $ 的元素缩放 0.1 倍。

为了更好地理解条件数，考虑线性方程组 $ \mathbf{A}\mathbf{x}=\mathbf{b} $。如果 $ \mathbf{A} $ 非奇异，唯一解是 $ \mathbf{x}=\mathbf{A}^{-1}\mathbf{b} $。假设我们将 $ \mathbf{b} $ 改为 $ \mathbf{b}+\Delta\mathbf{b} $；这会对 $ \mathbf{x} $ 产生什么影响？新的解必须满足

$$  \mathbf{A}(x+\Delta x)=b+\Delta b   \tag*{(7.47)}$$

其中

$$  \Delta x=\mathbf{A}^{-1}\Delta b   \tag*{(7.48)}$$

我们说 A 是良态的，如果小的 $ \Delta b $ 导致小的 $ \Delta x $；否则称 A 是病态的。

例如，假设

$$  \mathbf{A}=\frac{1}{2}\begin{pmatrix}{{{1}}}&{{{1}}} \\{{{1+10^{-10}}}}&{{{1-10^{-10}}}}\end{pmatrix},\mathbf{A}^{-1}=\begin{pmatrix}{{{1-10^{10}}}}&{{{10^{10}}}} \\{{{1+10^{10}}}}&{{{-10^{10}}}}\end{pmatrix}   \tag*{(7.49)}$$

对于 $ \boldsymbol{b} = (1, 1) $ 的解是 $ \boldsymbol{x} = (1, 1) $。如果我们将 $ \boldsymbol{b} $ 改变 $ \Delta\boldsymbol{b} $，解变为

$$  \Delta\boldsymbol{x}=\boldsymbol{A}^{-1}\Delta\boldsymbol{b}=\begin{pmatrix}\Delta b_{1}-10^{10}(\Delta b_{1}-\Delta b_{2})\\\Delta b_{1}+10^{10}(\Delta b_{1}-\Delta b_{2})\end{pmatrix}   \tag*{(7.50)}$$

因此 $b$ 的一个微小变化会导致 $x$ 的极大变化，因为 $A$ 是病态的 $(\kappa(\mathbf{A})=2\times10^{10})$。

对于 $ \ell_2 $ 范数，条件数等于最大奇异值与最小奇异值之比（参见第 7.5 节）；此外，$ \mathbf{A} $ 的奇异值是 $ \mathbf{A}^\top \mathbf{A} $ 的特征值的平方根，因此

$$  \kappa(\mathbf{A})=\sigma_{max}/\sigma_{min}=\sqrt{\frac{\lambda_{\max}}{\lambda_{\min}}}   \tag*{(7.51)}$$

---

通过考虑一个二次目标函数 $ f(\boldsymbol{x}) = \boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x} $，我们可以进一步深入理解条件数。绘制该函数的等高线将得到椭圆形，如第7.4.4节所示。随着矩阵 $ \boldsymbol{A} $ 的条件数增大，椭圆沿某些方向会变得愈加狭长，对应于函数空间中一条非常狭窄的山谷。若 $ \kappa = 1 $（最小可能值），则等高线将为圆形。

#### 7.1.5 特殊类型的矩阵

本节将列出几种常见且具有特定结构形式的矩阵。

##### 7.1.5.1 对角矩阵

对角矩阵是指所有非对角线元素均为0的矩阵。通常记作 $ \mathbf{D} = \mathrm{diag}(d_1, d_2, \ldots, d_n) $，其形式为

$$  \mathbf{D}=\begin{pmatrix}d_{1}&&&\\&d_{2}&&\\&&\ddots&\\&&&d_{n}\end{pmatrix}   \tag*{(7.52)}$$

单位矩阵记作 $ \mathbf{I} \in \mathbb{R}^{n \times n} $，是一个对角线上元素为1、其余位置均为0的方阵，即 $ \mathbf{I} = \text{diag}(1, 1, \ldots, 1) $。它具有如下性质：对所有 $ \mathbf{A} \in \mathbb{R}^{n \times n} $，

$$  \mathbf{A}\mathbf{I}=\mathbf{A}=\mathbf{I}\mathbf{A}   \tag*{(7.53)}$$

其中 $ \mathbf{I} $ 的大小由 $ \mathbf{A} $ 的维度决定，以确保矩阵乘法可行。

我们可以通过 $ \boldsymbol{d} = \mathrm{diag}(\boldsymbol{D}) $ 从矩阵中提取对角向量。通过 $ \boldsymbol{D} = \mathrm{diag}(\boldsymbol{d}) $ 可将向量转换为对角矩阵。

块对角矩阵是指主对角线上放置矩阵、其余位置均为0的矩阵，例如

$$  \begin{pmatrix}{{{\mathbf{A}}}}&{{{0}}} \\{{{0}}}&{{{\mathbf{B}}}}\end{pmatrix}   \tag*{(7.54)}$$

带状对角矩阵只有对角线及其两侧共 $ k $ 条对角线上有非零元素，其中 $ k $ 为带宽。例如，一个三对角的 $ 6 \times 6 $ 矩阵如下所示：

$$  \begin{bmatrix}{{{A_{11}}}}&{{{A_{12}}}}&{{{0}}}&{{{\cdots}}}&{{{\cdots}}}&{{{0}}} \\{{{A_{21}}}}&{{{A_{22}}}}&{{{A_{23}}}}&{{{\ddots}}}&{{{\ddots}}}&{{{\vdots}}} \\{{{0}}}&{{{A_{32}}}}&{{{A_{33}}}}&{{{A_{34}}}}&{{{\ddots}}}&{{{\vdots}}} \\{{{\vdots}}}&{{{\ddots}}}&{{{A_{43}}}}&{{{A_{44}}}}&{{{A_{45}}}}&{{{0}}} \\{{{\vdots}}}&{{{\ddots}}}&{{{\ddots}}}&{{{A_{54}}}}&{{{A_{55}}}}&{{{A_{56}}}} \\{{{0}}}&{{{\cdots}}}&{{{\cdots}}}&{{{0}}}&{{{A_{65}}}}&{{{A_{66}}}}\end{bmatrix}   \tag*{(7.55)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可协议。

---

##### 7.1.5.2 三角矩阵

**上三角矩阵**仅在对角线及其上方有非零元素，**下三角矩阵**仅在对角线及其下方有非零元素。

三角矩阵具有一个有用的性质：$ \mathbf{A} $ 的对角线元素即为 $ \mathbf{A} $ 的特征值，因此行列式等于对角线元素的乘积：$ \det(\mathbf{A}) = \prod_i A_{ii} $。

##### 7.1.5.3 正定矩阵

给定一个方阵 $ \mathbf{A} \in \mathbb{R}^{n \times n} $ 和一个向量 $ \boldsymbol{x} \in \mathbb{R}^n $，标量值 $ \boldsymbol{x}^\top \mathbf{A} \boldsymbol{x} $ 被称为**二次型**。明确写出其形式为

$$  \boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}=\sum_{i=1}^{n}\sum_{j=1}^{n}A_{i j}x_{i}x_{j}\quad.   \tag*{(7.56)}$$

注意，

$$  \boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}=(\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x})^{\mathsf{T}}=\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x}=\boldsymbol{x}^{\mathsf{T}}(\frac{1}{2}\boldsymbol{A}+\frac{1}{2}\boldsymbol{A}^{\mathsf{T}})\boldsymbol{x}   \tag*{(7.57)}$$

因此，我们通常隐式假设二次型中出现的矩阵是对称的。

我们给出以下定义：

- 对称矩阵 $ \mathbf{A} \in \mathbb{S}^n $ 是**正定的**，当且仅当对于所有非零向量 $ \boldsymbol{x} \in \mathbb{R}^n $，有 $ \boldsymbol{x}^\top \mathbf{A} \boldsymbol{x} > 0 $。这通常记作 $ \mathbf{A} \succ 0 $（或简记为 $ \mathbf{A} > 0 $）。如果可能存在 $ \boldsymbol{x}^\top \mathbf{A} \boldsymbol{x} = 0 $，则称该矩阵是**半正定的**，或简称为 PSD。所有正定矩阵的集合记为 $ \mathbb{S}_{++}^n $。

- 对称矩阵 $ \mathbf{A} \in \mathbb{S}^n $ 是**负定的**，记作 $ \mathbf{A} \prec 0 $（或简记为 $ \mathbf{A} < 0 $），当且仅当对于所有非零 $ \mathbf{x} \in \mathbb{R}^n $，有 $ \mathbf{x}^\top \mathbf{A} \mathbf{x} < 0 $。如果可能存在 $ \mathbf{x}^\top \mathbf{A} \mathbf{x} = 0 $，则称该矩阵是**半负定的**。

- 对称矩阵 $ A \in \mathbb{S}^n $ 是**不定的**，如果它既不是半正定也不是半负定——即存在 $ x_1, x_2 \in \mathbb{R}^n $，使得 $ x_1^\top A x_1 > 0 $ 且 $ x_2^\top A x_2 < 0 $。

显然，如果 $ \mathbf{A} $ 是正定的，那么 $ -\mathbf{A} $ 就是负定的，反之亦然。同样地，如果 $ \mathbf{A} $ 是半正定的，那么 $ -\mathbf{A} $ 就是半负定的，反之亦然。如果 $ \mathbf{A} $ 是不定的，那么 $ -\mathbf{A} $ 也是不定的。此外，还可以证明正定矩阵和负定矩阵总是可逆的。

在第 7.4.3.1 节中，我们将证明对称矩阵是正定的当且仅当其所有特征值为正。需要注意的是，即使 $ \mathbf{A} $ 的所有元素均为正，也不能保证 $ \mathbf{A} $ 一定是正定的。例如，$ \mathbf{A} = \begin{pmatrix} 4 & 3 \\ 3 & 2 \end{pmatrix} $ 就不是正定的。相反，正定矩阵也可以包含负元素，例如 $ \mathbf{A} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} $。

（实对称）矩阵为正定的一个充分条件是它**对角占优**，即矩阵的每一行中，该行对角元素的绝对值

---

大于该行所有其他（非对角）元素的模之和。更精确地说，

$$  |a_{ii}|>\sum_{j\neq i}|a_{ij}|\quad \forall i   \tag*{(7.58)}$$

在二维情形下，任何实对称 $2 \times 2$ 矩阵 $\begin{pmatrix} a & b \\ b & d \end{pmatrix}$ 是正定的当且仅当 $a > 0$，$d > 0$ 且 $ad > b^2$。

最后，有一类正定矩阵经常出现，因此值得特别提及。给定任意矩阵 $\mathbf{A} \in \mathbb{R}^{m \times n}$（不必对称或方阵），矩阵 $\mathbf{G} = \mathbf{A}^{\top}\mathbf{A}$ 总是半正定的。此外，如果 $m \geq n$（为方便起见我们假设 $\mathbf{A}$ 是满秩的），则 $\mathbf{G} = \mathbf{A}^{\top}\mathbf{A}$ 是正定的。

##### 7.1.5.4 正交矩阵

两个向量 $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$ 是正交的，如果 $\boldsymbol{x}^\top \boldsymbol{y} = 0$。一个向量 $\boldsymbol{x} \in \mathbb{R}^n$ 是归一化的，如果 $\|\boldsymbol{x}\|_2 = 1$。一个两两正交且归一化的向量集合称为**标准正交**。一个方阵 $\mathbf{U} \in \mathbb{R}^{n \times n}$ 是**正交**的，如果它的所有列都是标准正交的。（注意，在谈论向量与矩阵时，“正交”一词的含义有所不同。）如果 $\mathbf{U}$ 的元素是复数值，我们使用**酉**代替正交。

从正交性和归一性的定义立即得出：$\mathbf{U}$ 是正交的当且仅当

$$  \mathbf{U}^{\mathsf{T}}\mathbf{U}=\mathbf{I}=\mathbf{U}\mathbf{U}^{\mathsf{T}}.   \tag*{(7.59)}$$

换句话说，正交矩阵的逆等于它的转置。注意如果 $\mathbf{U}$ 不是方阵——即 $\mathbf{U} \in \mathbb{R}^{m \times n}$，$n < m$——但其列仍然是标准正交的，那么 $\mathbf{U}^\top \mathbf{U} = \mathbf{I}$，但 $\mathbf{U} \mathbf{U}^\top \neq \mathbf{I}$。我们通常只将“正交”一词用于描述前一种情况，即 $\mathbf{U}$ 是方阵的情形。

正交矩阵的一个例子是旋转矩阵（见习题 7.1）。例如，在三维空间中绕 $z$ 轴旋转角度 $\alpha$ 的矩阵为

$$  \mathbf{R}(\alpha)=\begin{pmatrix}{{{\cos(\alpha)}}}&{{{-\sin(\alpha)}}}&{{{0}}} \\{{{\sin(\alpha)}}}&{{{\cos(\alpha)}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{pmatrix}   \tag*{(7.60)}$$

若 $\alpha = 45^{\circ}$，则变为

$$  \mathbf{R}(45)=\begin{pmatrix}{{{\frac{1}{\sqrt{2}}}}}&{{{-\frac{1}{\sqrt{2}}}}}&{{{0}}} \\{{{\frac{1}{\sqrt{2}}}}}&{{{\frac{1}{\sqrt{2}}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{pmatrix}   \tag*{(7.61)}$$

其中 $\frac{1}{\sqrt{2}} = 0.7071$。我们可以看到 $\mathbf{R}(-\alpha) = \mathbf{R}(\alpha)^{-1} = \mathbf{R}(\alpha)^{\top}$，因此这是一个正交矩阵。

正交矩阵的一个优良性质是，用正交矩阵作用在一个向量上不会改变其欧几里得范数，即

$$  \left\| \mathbf{U} \mathbf{x} \right\|_{2}=\left\| \mathbf{x} \right\|_{2}   \tag*{(7.62)}$$

对于任意非零 $x \in \mathbb{R}^n$ 以及正交矩阵 $\mathbf{U} \in \mathbb{R}^{n \times n}$ 成立。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

类似地，可以证明两个向量经正交矩阵变换后，它们之间的夹角保持不变。x 与 y 之间夹角的余弦由下式给出

$$  \cos(\alpha(\boldsymbol{x},\boldsymbol{y}))=\frac{\boldsymbol{x}^{\top}\boldsymbol{y}}{\left|\left|\boldsymbol{x}\right|\right|\left|\boldsymbol{y}\right|}   \tag*{(7.63)}$$

因此

$$  \cos(\alpha(\mathbf{U}\boldsymbol{x},\mathbf{U}\boldsymbol{y}))=\frac{(\mathbf{U}\boldsymbol{x})^{\top}(\mathbf{U}\boldsymbol{y})}{||\mathbf{U}\boldsymbol{x}||||\mathbf{U}\boldsymbol{y}||}=\frac{\boldsymbol{x}^{\top}\boldsymbol{y}}{||\boldsymbol{x}||||\boldsymbol{y}||}=\cos(\alpha(\boldsymbol{x},\boldsymbol{y}))   \tag*{(7.64)}$$

总之，正交矩阵变换是旋转（若 \( \det(\mathbf{U})=1 \)）和反射（若 \( \det(\mathbf{U})=-1 \)）的推广，因为它们保持长度和角度不变。

注意，有一种称为 Gram-Schmidt 正交化的方法，可以将任意方阵转化为正交矩阵，但我们在此不做介绍。

### 7.2 矩阵乘法

两个矩阵 \( \mathbf{A} \in \mathbb{R}^{m \times n} \) 和 \( \mathbf{B} \in \mathbb{R}^{n \times p} \) 的乘积为矩阵

$$  \mathbf{C}=\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times p},   \tag*{(7.65)}$$

其中

$$  C_{i j}=\sum_{k=1}^{n}A_{i k}B_{k j}.   \tag*{(7.66)}$$

注意，矩阵乘积存在的前提是 A 的列数必须等于 B 的行数。

矩阵乘法通常需要 \( O(mnp) \) 的时间，尽管存在更快的算法。此外，可以利用专用硬件（如 GPU 和 TPU）通过对行（或列）并行执行运算来显著加速矩阵乘法。

了解矩阵乘法的一些基本性质是很有用的：

• 矩阵乘法满足结合律：\( (AB)C = A(BC) \)。

• 矩阵乘法满足分配律：\( \mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C} \)。

• 矩阵乘法通常不满足交换律，即可能出现 \( AB \neq BA \) 的情况。

（在上述每种情况下，我们都假设矩阵维度匹配。）

矩阵乘法有许多重要的特例，下面进行讨论。

#### 7.2.1 向量-向量乘积

给定两个向量 \( \boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n \)，量 \( \boldsymbol{x}^\top \boldsymbol{y} \) 称为向量的内积（inner product）、点积（dot product）或标量积（scalar product），是一个实数，由下式给出

$$  \langle\boldsymbol{x},\boldsymbol{y}\rangle\triangleq\boldsymbol{x}^{\top}\boldsymbol{y}=\sum_{i=1}^{n}x_{i}y_{i}.   \tag*{(7.67)}$$

---

注意，总是有 $ x^{\top}y = y^{\top}x $。

给定向量 $ \boldsymbol{x} \in \mathbb{R}^m $, $ \boldsymbol{y} \in \mathbb{R}^n $（它们不再需要具有相同大小），则 $ \boldsymbol{x}\boldsymbol{y}^\top $ 称为向量的外积。它是一个矩阵，其元素由 $ (\boldsymbol{x}\boldsymbol{y}^\top)_{ij} = x_i y_j $ 给出，即：

$$  \boldsymbol{x}\boldsymbol{y}^{\top}\in\mathbb{R}^{m\times n}=\left[\begin{array}{c c c c}x_{1}y_{1}&x_{1}y_{2}&\cdots&x_{1}y_{n}\\ x_{2}y_{1}&x_{2}y_{2}&\cdots&x_{2}y_{n}\\ \vdots&\vdots&\ddots&\vdots\\ x_{m}y_{1}&x_{m}y_{2}&\cdots&x_{m}y_{n}\end{array}\right].   \tag*{(7.68)}$$

#### 7.2.2 矩阵-向量乘积

给定矩阵 $ \mathbf{A} \in \mathbb{R}^{m \times n} $ 和向量 $ \mathbf{x} \in \mathbb{R}^n $，它们的乘积是一个向量 $ \mathbf{y} = \mathbf{A}\mathbf{x} \in \mathbb{R}^m $。有几种方式可以看待矩阵-向量乘法，下面我们将逐一介绍。

如果按行写出 A，则我们可以如下表示 y = Ax：

$$  \boldsymbol{y}=\mathbf{A}\boldsymbol{x}=\left[\begin{array}{ccc}-\quad\boldsymbol{a}_{1}^{\top}&-\quad\\-\quad\boldsymbol{a}_{2}^{\top}&-\quad\\\vdots&\quad\\\quad-\quad\boldsymbol{a}_{m}^{\top}&-\quad\end{array}\right]\boldsymbol{x}=\left[\begin{array}{c}\boldsymbol{a}_{1}^{\top}\boldsymbol{x}\\\boldsymbol{a}_{2}^{\top}\boldsymbol{x}\\\vdots\\\boldsymbol{a}_{m}^{\top}\boldsymbol{x}\\\end{array}\right].   \tag*{(7.69)}$$

换句话说，$ \mathbf{y} $ 的第 $ i $ 个元素等于 $ \mathbf{A} $ 的第 $ i $ 行与 $ \mathbf{x} $ 的内积，即 $ y_i = \mathbf{a}_i^\top \mathbf{x} $。另一种方式，将 $ \mathbf{A} $ 按列写出。在这种情况下，我们看到

$$  \begin{aligned}\boldsymbol{y}&=\mathbf{A}\boldsymbol{x}=\left[\begin{array}{ccc}\mid&&\mid\\ \boldsymbol{a}_{1}&\boldsymbol{a}_{2}&\cdots&\boldsymbol{a}_{n}\\\mid&&\mid&\end{array}\right]\left|\begin{array}{c}x_{1}\\x_{2}\\\vdots\\x_{n}\end{array}\right|=\left[\begin{array}{c}\mid\\ \boldsymbol{a}_{1}\\ \mid\end{array}\right]x_{1}+\left[\begin{array}{c}\mid\\ \boldsymbol{a}_{2}\\ \mid\end{array}\right]x_{2}+\cdots+\left[\begin{array}{c}\mid\\ \boldsymbol{a}_{n}\\ \mid\end{array}\right]x_{n}.\end{aligned}   \tag*{(7.70)}$$

也就是说，y 是 A 的各列的线性组合，其中线性组合的系数由 x 的元素给出。我们可以将 A 的各列视为定义了一个线性子空间的一组基向量。通过基向量的线性组合，我们可以构造该子空间中的向量。详细信息参见第 7.1.2 节。

#### 7.2.3 矩阵-矩阵乘积

下面我们考察四种不同（当然，它们是等价的）看待矩阵-矩阵乘法 C = AB 的方式。

首先，我们可以将矩阵-矩阵乘法视为一组向量-向量乘积。最直观的观点（直接来自定义）是，C 的第 i,j 个元素等于 A 的第 i 行与 B 的第 j 列的内积。符号表示如下：

$$  \mathbf{C}=\mathbf{A}\mathbf{B}=\left[\begin{array}{ccc}-\quad a_{1}^{\top}&-\quad\\-\quad a_{2}^{\top}&-\quad\\\quad\vdots&\\\quad-a_{m}^{\top}&-\quad\end{array}\right]\left[\begin{array}{ccc}\mid&|\quad&|\\b_{1}&b_{2}&\cdots&b_{p}\\\mid&|\quad&|\end{array}\right]=\left[\begin{array}{cccc}a_{1}^{\top}b_{1}&a_{1}^{\top}b_{2}&\cdots&a_{1}^{\top}b_{p}\\a_{2}^{\top}b_{1}&a_{2}^{\top}b_{2}&\cdots&a_{2}^{\top}b_{p}\\\vdots&\vdots&\ddots&\vdots\\a_{m}^{\top}b_{1}&a_{m}^{\top}b_{2}&\cdots&a_{m}^{\top}b_{p}\end{array}\right].   \tag*{(7.71)}$$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_461_118_676_326.jpg" alt="图像" width="18%" /></div>


<div style="text-align: center;">图 7.5：矩阵乘法的示意图。来自 https://en.wikipedia.org/wiki/Matrix_multiplication。经 Wikipedia 作者 Bilou 友好许可使用。</div>


请记住，由于 $\mathbf{A} \in \mathbb{R}^{m \times n}$ 和 $\mathbf{B} \in \mathbb{R}^{n \times p}$，$\mathbf{a}_i \in \mathbb{R}^n$ 且 $\mathbf{b}_j \in \mathbb{R}^n$，所以这些内积都是有意义的。当我们按行表示 $\mathbf{A}$、按列表示 $\mathbf{B}$ 时，这是最“自然”的表示方式，见 Figure 7.5 的图示。

另外，我们可以按列表示 A、按行表示 B，从而将 AB 解释为外积之和。符号表示为：

$$  \mathbf{C}=\mathbf{A}\mathbf{B}=\left[\begin{array}{ccc}\mid&&\mid\\a_{1}&a_{2}&\cdots&a_{n}\\\mid&&\mid&\end{array}\right]\left[\begin{array}{ccc}-\quad b_{1}^{\top}&-\quad\\-\quad b_{2}^{\top}&-\quad\\\vdots&\quad\\\quad\vdots&\quad\\-\quad b_{n}^{\top}&-\end{array}\right]=\sum_{i=1}^{n}a_{i}b_{i}^{\top}.   \tag*{(7.72)}$$

换言之，$\mathbf{A}\mathbf{B}$ 等于对所有 $i$ 求和，即 $\mathbf{A}$ 的第 $i$ 列与 $\mathbf{B}$ 的第 $i$ 行的外积之和。由于在这种情况下 $\mathbf{a}_i \in \mathbb{R}^m$ 且 $\mathbf{b}_i \in \mathbb{R}^p$，外积 $\mathbf{a}_i \mathbf{b}_i^\top$ 的维度是 $m \times p$，与 $\mathbf{C}$ 的维度一致。

我们也可以将矩阵-矩阵乘法视为一组矩阵-向量乘积。具体来说，如果我们按列表示 B，则 C 的列可以看作 A 与 B 各列的矩阵-向量乘积。符号表示为：

$$  \mathbf{C}=\mathbf{A}\mathbf{B}=\mathbf{A}\left[\begin{array}{ccc}\mid&\mid&\\\mathbf{b}_{1}&\mathbf{b}_{2}&\cdots\\\mid&&\mid\end{array}\right.\mathbf{\Lambda}\mathbf{\Lambda}\mathbf{\Lambda}\mathbf{\Lambda}_{p}=\left[\begin{array}{ccc}\mid&\mid&\\\mathbf{A}\mathbf{b}_{1}&\mathbf{A}\mathbf{b}_{2}&\cdots\\\mid&&\mid\end{array}\right.\mathbf{\Lambda}\mathbf{\Lambda}\mathbf{\Lambda}_{p}\mathbf{\Lambda}\mathbf{\Lambda}.   \tag*{(7.73)}$$

此处 C 的第 i 列由右侧向量的矩阵-向量乘积给出，即 $c_i = A b_i$。这些矩阵-向量乘积又可利用前一子节给出的两种视角进行解释。

最后，我们有一个类似的视角：按行表示 $\mathbf{A}$，并将 C 的行视为 $\mathbf{A}$ 的各行与矩阵 $\mathbf{B}$ 的矩阵-向量乘积。符号表示为：

$$  \mathbf{C}=\mathbf{A}\mathbf{B}=\left[\begin{array}{ccc}-\quad a_{1}^{\top}&-\quad\\-\quad a_{2}^{\top}&-\quad\\\quad\vdots&\\\quad\vdots&\\\quad a_{m}^{\top}&-\quad\end{array}\right]\mathbf{B}=\left[\begin{array}{ccc}-\quad a_{1}^{\top}\mathbf{B}&-\quad\\-\quad a_{2}^{\top}\mathbf{B}&-\quad\\\quad\vdots&\\\quad\vdots&\\\quad a_{m}^{\top}\mathbf{B}&-\quad\end{array}\right].   \tag*{(7.74)}$$

---

这里 C 的第 i 行由左侧向量与矩阵的乘积给出。

将矩阵乘法如此细致地剖析似乎有些小题大做，尤其是所有这些观点都直接源自我们在本节开头给出的初始定义（仅用了一行数学公式）。然而，几乎所有线性代数都在处理某种形式的矩阵乘法，因此花些时间培养对这里所提观点的直观理解是值得的。

最后，关于符号说明。我们用 $\mathbf{A}^2$ 作为 $\mathbf{A}\mathbf{A}$ 的简写，即矩阵乘积。要表示矩阵元素的逐元素平方，我们写作 $\mathbf{A}^{\odot 2} = [A_{ij}^2]$。（如果 $\mathbf{A}$ 是对角矩阵，那么 $\mathbf{A}^2 = \mathbf{A}^{\odot 2}$。）

我们还可以通过矩阵平方根定义 $A^2$ 的逆：如果 $A^2 = M$，则称 $A = \sqrt{M}$。要表示矩阵元素的逐元素平方根，我们写作 $[\sqrt{M_{ij}}]$。

#### 7.2.4 应用：操作数据矩阵

作为上述结果的一个应用，考虑 $\mathbf{X}$ 是 $N \times D$ 设计矩阵的情况，其行代表数据样本。以下总结了几种常见的对该矩阵的预处理操作。（将这些操作以矩阵形式写出很有用，因为它在符号上非常紧凑，并且能让我们利用快速的矩阵代码快速实现这些方法。）

##### 7.2.4.1 矩阵分片求和

假设 $\mathbf{X}$ 是一个 $N \times D$ 矩阵。我们可以通过对行求和：左乘一个 $1 \times N$ 的全 1 矩阵，得到一个 $1 \times D$ 矩阵：

$$ \mathbf{1}_{N}^{\mathsf{T}}\mathbf{X}=\left(\sum_{n}x_{n1}\quad\cdots\quad\sum_{n}x_{nD}\right) \tag*{(7.75)}$$

因此数据向量的均值由下式给出：

$$ \overline{{\boldsymbol{x}}}^{\mathsf{T}}=\frac{1}{N}\mathbf{1}_{N}^{\mathsf{T}}\mathbf{X} \tag*{(7.76)}$$

我们可以通过对列求和：右乘一个 $D \times 1$ 的全 1 矩阵，得到一个 $N \times 1$ 矩阵：

$$ \mathbf{X1}_{D}=\begin{pmatrix}\sum_{d}x_{1d}\\ \vdots\\ \sum_{d}x_{Nd}\end{pmatrix} \tag*{(7.77)}$$

我们可以通过同时左乘和右乘一个全 1 向量来求和矩阵中的所有元素：

$$ \mathbf{1}_{N}^{\top}\mathbf{X}\mathbf{1}_{D}=\sum_{ij}X_{ij} \tag*{(7.78)}$$

因此总均值由下式给出：

$$ \overline{x}=\frac{1}{ND}\mathbf{1}_{N}^{\top}\mathbf{X}\mathbf{1}_{D} \tag*{(7.79)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可证。

---

##### 7.2.4.2 矩阵的行和列缩放

我们经常需要对数据矩阵的行或列进行缩放（例如，将其标准化）。现在，我们将展示如何用矩阵符号来表示这一操作。

如果我们将一个数据矩阵 \( \mathbf{X} \) 左乘一个对角矩阵 \( \mathbf{S} = \mathrm{diag}(\mathbf{s}) \)，其中 \( \mathbf{s} \) 是一个 \( N \) 维向量，那么实际上就是将 \( \mathbf{X} \) 的每一行乘以 \( \mathbf{s} \) 中对应的缩放因子：

$$  \mathrm{diag}(\boldsymbol{s})\boldsymbol{X}=\begin{pmatrix}{{{s_{1}}}}&{{{\cdots}}}&{{{0}}} \\{{{\ddots}}} \\{{{0}}}&{{{\cdots}}}&{{{s_{N}}}}\end{pmatrix}\begin{pmatrix}{{{x_{1,1}}}}&{{{\cdots}}}&{{{x_{1,D}}}} \\{{{\ddots}}} \\{{{x_{N,1}}}}&{{{\cdots}}}&{{{x_{N,D}}}}\end{pmatrix}=\begin{pmatrix}{{{s_{1}x_{1,1}}}}&{{{\cdots}}}&{{{s_{1}x_{1,D}}}} \\{{{\ddots}}} \\{{{s_{N}x_{N,1}}}}&{{{\cdots}}}&{{{s_{N}x_{N,D}}}}\end{pmatrix}   \tag*{(7.80)}$$

如果我们将 \( \mathbf{X} \) 右乘一个对角矩阵 \( \mathbf{S} = \mathrm{diag}(\mathbf{s}) \)，其中 \( \mathbf{s} \) 是一个 \( D \) 维向量，那么实际上就是将 \( \mathbf{X} \) 的每一列乘以 \( \mathbf{s} \) 中对应的元素：

$$  \mathbf{X}\mathrm{diag}(\boldsymbol{s})=\begin{pmatrix}{{{x_{1,1}}}}&{{{\cdots}}}&{{{x_{1,D}}}} \\{{{\ddots}}} \\{{{x_{N,1}}}}&{{{\cdots}}}&{{{x_{N,D}}}}\end{pmatrix}\begin{pmatrix}{{{s_{1}}}}&{{{\cdots}}}&{{{0}}} \\{{{\ddots}}} \\{{{0}}}&{{{\cdots}}}&{{{s_{D}}}}\end{pmatrix}=\begin{pmatrix}{{{s_{1}x_{1,1}}}}&{{{\cdots}}}&{{{s_{D}x_{1,D}}}} \\{{{\ddots}}} \\{{{s_{1}x_{N,1}}}}&{{{\cdots}}}&{{{s_{D}x_{N,D}}}}\end{pmatrix}   \tag*{(7.81)}$$

因此，我们可以将10.2.8节的标准化操作重写为如下矩阵形式：

$$  \mathrm{standardize}(\mathbf{X})=(\mathbf{X}-\mathbf{1}_{N}\boldsymbol{\mu}^{T})\mathrm{diag}(\boldsymbol{\sigma})^{-1}   \tag*{(7.82)}$$

其中 \( \mu = \overline{x} \) 是经验均值，而 \( \sigma \) 是经验标准差构成的向量。

##### 7.2.4.3 平方和与散布矩阵

平方和矩阵是一个 \( D \times D \) 矩阵，定义为：

$$  \mathbf{S}_{0}\triangleq\mathbf{X}^{\top}\mathbf{X}=\sum_{n=1}^{N}\mathbf{x}_{n}\mathbf{x}_{n}^{\top}=\sum_{n=1}^{N}\begin{pmatrix}x_{n,1}^{2}&\cdots&x_{n,1}x_{n,D}\\ &\ddots&\\ x_{n,D}x_{n,1}&\cdots&x_{n,D}^{2}\end{pmatrix}   \tag*{(7.83)}$$

散布矩阵是一个 \( D \times D \) 矩阵，定义为：

$$  \mathbf{S}_{\overline{\mathbf{x}}}\triangleq\sum_{n=1}^{N}(\mathbf{x}_{n}-\overline{\mathbf{x}})(\mathbf{x}_{n}-\overline{\mathbf{x}})^{\top}=\left(\sum_{n}\mathbf{x}_{n}\mathbf{x}_{n}^{\top}\right)-N\overline{\mathbf{x}}\overline{\mathbf{x}}^{\top}   \tag*{(7.84)}$$

可以看出，这相当于对均值中心化后的数据应用平方和矩阵。更精确地说，定义 \( \tilde{\mathbf{X}} \) 为从 \( \mathbf{X} \) 的每一行减去均值 \( \overline{\mathbf{x}} = \frac{1}{N} \mathbf{X}^\top \mathbf{1}_N \) 后得到的版本。因此，我们可以使用下式计算中心化后的数据矩阵：

$$  \tilde{\mathbf{X}}=\mathbf{X}-\mathbf{1}_{N}\overline{\mathbf{x}}^{\mathsf{T}}=\mathbf{X}-\frac{1}{N}\mathbf{1}_{N}\mathbf{1}_{N}^{\mathsf{T}}\mathbf{X}=\mathbf{C}_{N}\mathbf{X}   \tag*{(7.85)}$$

其中

$$  \mathbf{C}_{N}\triangleq\mathbf{I}_{N}-\frac{1}{N}\mathbf{J}_{N}   \tag*{(7.86)}$$

---

是中心化矩阵，而 $ \mathbf{J}_N = \mathbf{1}_N \mathbf{1}_N^\top $ 是全 1 矩阵。现在可以如下计算散度矩阵：

$$  \mathbf{S}_{\overline{{x}}}=\tilde{\mathbf{X}}^{\top}\tilde{\mathbf{X}}=\mathbf{X}^{\top}\mathbf{C}_{N}^{\top}\mathbf{C}_{N}\mathbf{X}=\mathbf{X}^{\top}\mathbf{C}_{N}\mathbf{X}   \tag*{(7.87)}$$

这里我们利用了 $ \mathbf{C}_N $ 是对称且幂等的事实，即对于 $ k = 1, 2, \ldots $ 有 $ \mathbf{C}_N^k = \mathbf{C}_N $（因为一旦减去了均值，再次减去它不会产生任何影响）。

##### 7.2.4.4 Gram 矩阵

$ N \times N $ 矩阵 $ XX^{\top} $ 是一个内积矩阵，称为 Gram 矩阵：

$$  \mathbf{K}\triangleq\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}\boldsymbol{x}_{1}^{\top}\boldsymbol{x}_{1}&\cdots&\boldsymbol{x}_{1}^{\top}\boldsymbol{x}_{N}\\ &\ddots&\\ \boldsymbol{x}_{n}^{\top}\boldsymbol{x}_{1}&\cdots&\boldsymbol{x}_{N}^{\top}\boldsymbol{x}_{N}\end{pmatrix}   \tag*{(7.88)}$$

有时我们需要计算均值中心化数据向量的内积，即 $ \mathbf{\tilde{K}} = \mathbf{\tilde{X}} \mathbf{\tilde{X}}^T $。然而，如果我们在处理特征相似性矩阵而非原始特征，则只能访问 $ \mathbf{K} $ 而非 $ \mathbf{X} $。（我们将在第 20.4.4 节和第 20.4.6 节中看到这样的例子。）幸运的是，我们可以通过双重中心化技巧从 $ \mathbf{K} $ 计算出 $ \mathbf{\tilde{K}} $：

$$  \tilde{\mathbf{K}}=\tilde{\mathbf{X}}\tilde{\mathbf{X}}^{\mathsf{T}}=\mathbf{C}_{N}\mathbf{K}\mathbf{C}_{N}=\mathbf{K}-\frac{1}{N}\mathbf{J}\mathbf{K}-\frac{1}{N}\mathbf{K}\mathbf{J}+\frac{1}{N^{2}}\mathbf{1}^{\mathsf{T}}\mathbf{K}\mathbf{1}   \tag*{(7.89)}$$

这从 $ \mathbf{K} $ 中减去了行均值和列均值，并加回了被减去了两次的全局均值，从而使得 $ \tilde{\mathbf{K}} $ 的行均值和列均值都为零。

为了理解方程 (7.89) 为何成立，考虑其标量形式：

$$  \begin{aligned}\tilde{K}_{ij}&=\tilde{\boldsymbol{x}}_{i}^{\top}\tilde{\boldsymbol{x}}_{j}=(\boldsymbol{x}_{i}-\frac{1}{N}\sum_{k=1}^{N}\boldsymbol{x}_{k})(\boldsymbol{x}_{j}-\frac{1}{N}\sum_{l=1}^{N}\boldsymbol{x}_{l})\\&=\boldsymbol{x}_{i}^{\top}\boldsymbol{x}_{j}-\frac{1}{N}\sum_{k=1}^{N}\boldsymbol{x}_{i}^{\top}\boldsymbol{x}_{k}-\frac{1}{N}\sum_{k=1}^{N}\boldsymbol{x}_{j}^{\top}\boldsymbol{x}_{k}+\frac{1}{N^{2}}\sum_{k=1}^{N}\sum_{l=1}^{N}\boldsymbol{x}_{k}^{\top}\boldsymbol{x}_{l}\end{aligned}   \tag*{(7.91)}$$

##### 7.2.4.5 距离矩阵

设 $ \mathbf{X} $ 为 $ N_x \times D $ 的数据矩阵，$ \mathbf{Y} $ 为另一个 $ N_y \times D $ 的数据矩阵。我们可以使用下式计算它们之间的成对平方距离：

$$  \mathbf{D}_{ij}=(\boldsymbol{x}_{i}-\boldsymbol{y}_{j})^{\mathrm{T}}(\boldsymbol{x}_{i}-\boldsymbol{y}_{j})=||\boldsymbol{x}_{i}||^{2}-2\boldsymbol{x}_{i}^{\mathrm{T}}\boldsymbol{y}_{j}+||\boldsymbol{y}_{j}||^{2}   \tag*{(7.92)}$$

现在将其写成矩阵形式。设 $ \hat{\mathbf{x}} = [||\mathbf{x}_1||^2; \cdots; ||\mathbf{x}_{N_x}||^2] = \text{diag}(\mathbf{X}\mathbf{X}^\top) $ 是一个向量，其中每个元素是 $ \mathbf{X} $ 中样本的平方范数，类似地定义 $ \hat{\mathbf{y}} $。于是我们有

$$  \mathbf{D}=\hat{\mathbf{x}}\mathbf{1}_{N_{y}}^{\mathsf{T}}-2\mathbf{X}\mathbf{Y}^{\mathsf{T}}+\mathbf{1}_{N_{x}}\hat{\mathbf{y}}^{\mathsf{T}}   \tag*{(7.93)}$$

在 $ \mathbf{X} = \mathbf{Y} $ 的情况下，有

$$  \mathbf{D}=\hat{\mathbf{x}}\mathbf{1}_{N}^{\top}-2\mathbf{X}\mathbf{X}^{\top}+\mathbf{1}_{N}\hat{\mathbf{x}}^{\top}   \tag*{(7.94)}$$

这种向量化计算通常比使用 for 循环快得多。

作者：Kevin P. Murphy。(C) MIT 出版社。CC-BY-NC-ND 许可。

---

#### 7.2.5 Kronecker 积 *

若 $ \mathbf{A} $ 为 $ m \times n $ 矩阵，$ \mathbf{B} $ 为 $ p \times q $ 矩阵，则 Kronecker 积 $ \mathbf{A} \otimes \mathbf{B} $ 是一个 $ mp \times nq $ 的分块矩阵

$$  \mathbf{A}\otimes\mathbf{B}=\begin{bmatrix}a_{11}\mathbf{B}&\cdots&a_{1n}\mathbf{B}\\ \vdots&\ddots&\vdots\\ a_{m1}\mathbf{B}&\cdots&a_{mn}\mathbf{B}\end{bmatrix}   \tag*{(7.95)}$$

例如，

$$  \begin{bmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\\ a_{31}&a_{32}\end{bmatrix}\otimes\begin{bmatrix}b_{11}&b_{12}&b_{13}\\ b_{21}&b_{22}&b_{23}\end{bmatrix}=\begin{bmatrix}a_{11}b_{11}&a_{11}b_{12}&a_{11}b_{13}&a_{12}b_{11}&a_{12}b_{12}&a_{12}b_{13}\\ a_{11}b_{21}&a_{11}b_{22}&a_{11}b_{23}&a_{12}b_{21}&a_{12}b_{22}&a_{12}b_{23}\\ a_{21}b_{11}&a_{21}b_{12}&a_{21}b_{13}&a_{22}b_{11}&a_{22}b_{12}&a_{22}b_{13}\\ a_{21}b_{21}&a_{21}b_{22}&a_{21}b_{23}&a_{22}b_{21}&a_{22}b_{22}&a_{22}b_{23}\\ a_{31}b_{11}&a_{31}b_{12}&a_{31}b_{13}&a_{32}b_{11}&a_{32}b_{12}&a_{32}b_{13}\\ a_{31}b_{21}&a_{31}b_{22}&a_{31}b_{23}&a_{32}b_{21}&a_{32}b_{22}&a_{32}b_{23}\end{bmatrix}   \tag*{(7.96)}$$

以下是一些有用的恒等式：

$$  \left(\mathbf{A}\otimes\mathbf{B}\right)^{-1}=\mathbf{A}^{-1}\otimes\mathbf{B}^{-1}   \tag*{(7.97)}$$

$$  (\mathbf{A}\otimes\mathbf{B})\mathrm{vec}(\mathbf{C})=\mathrm{vec}(\mathbf{B}\mathbf{C}\mathbf{A}^{\mathrm{T}})   \tag*{(7.98)}$$

其中 $ \text{vec}(\mathbf{M}) $ 表示将 $\mathbf{M}$ 的各列纵向堆叠。（若按行堆叠，则得到 $ (\mathbf{A} \otimes \mathbf{B})\text{vec}(\mathbf{C}) = \text{vec}(\mathbf{ACB}^\top $。）其他有用性质可参见文献 [Loa00]。

#### 7.2.6 爱因斯坦求和约定 *

爱因斯坦求和约定（简称 einsum）是一种用于张量运算的简写符号。该约定由爱因斯坦 [Ein16, sec 5] 提出，后来他曾对朋友开玩笑说：“我做出了一项伟大的数学发现；每当求和需要对一个出现两次的指标进行时，我便省去求和符号……” [Pai05, p.216]。例如，矩阵乘法 $ C_{ij} = \sum_k A_{ik} B_{kj} $ 可以简写为 $ C_{ij} = A_{ik} B_{kj} $，即省略 $ \sum_k $。

考虑一个更复杂的例子：假设有一个三维张量 $ S_{ntk} $，其中 $ n $ 索引批次中的样本，$ t $ 索引序列中的位置，$ k $ 索引独热表示中的单词。设 $ W_{kd} $ 为嵌入矩阵，它将稀疏独热向量 $ R^k $ 映射为 $ R^d $ 中的密集向量。我们可以按如下方式将批次中的独热序列转换为批次中的嵌入序列：

$$  E_{n t d}=\sum_{k}S_{n t k}W_{k d}   \tag*{(7.99)}$$

按如下方式计算每个序列的嵌入向量之和（以获得每个词袋的全局表示）：

$$  E_{nd}=\sum_{k}\sum_{t}S_{ntk}W_{kd}   \tag*{(7.100)}$$

---

最后，我们可以将每个序列的向量表示通过另一个线性变换 $ V_{dc} $，映射到一个具有 c 个标签的分类器的 logits 上：

$$  L_{nc}=\sum_{d}E_{nd}V_{dc}=\sum_{d}\sum_{k}\sum_{t}S_{ntk}W_{kd}V_{dc}   \tag*{(7.101)}$$

在 einsum 表示法中，我们写作 $ L_{nc} = S_{ntk} W_{kd} V_{dc} $。我们对 k 和 d 求和，因为这些索引在右侧出现了两次。我们对 t 求和，因为该索引未出现在左侧。

Einsum 在 NumPy、TensorFlow、PyTorch 等中实现。它特别有用之处在于，能够以最优顺序执行复杂表达式中的相关张量乘法，从而最小化时间和中间内存分配。$ ^{2} $ 该库的最佳说明见 einsum_demo.ipynb 中的示例。

注意，einsum 的速度取决于运算的执行顺序，而执行顺序又取决于相关参数的形状。如 [GASG18] 所述，最优顺序最小化所得计算图的树宽。通常，计算最优顺序的时间随参数数量呈指数增长，因此常用贪心近似。然而，如果预期多次重复相同的计算（使用形状相同但内容可能不同的张量），我们可以计算一次最优顺序并多次复用。

### 7.3 矩阵求逆

#### 7.3.1 方阵的逆

方阵 $ \mathbf{A} \in \mathbb{R}^{n \times n} $ 的逆记为 $ \mathbf{A}^{-1} $，是满足如下条件的唯一矩阵：

$$  \mathbf{A}^{-1}\mathbf{A}=\mathbf{I}=\mathbf{A}\mathbf{A}^{-1}.   \tag*{(7.102)}$$

注意，$ A^{-1} $ 存在当且仅当 $ \det(\mathbf{A}) \neq 0 $。若 $ \det(\mathbf{A}) = 0 $，则称其为**奇异矩阵**。以下是逆矩阵的性质；均假设 $ A, B \in \mathbb{R}^{n \times n} $ 非奇异：

$$  \left(\mathbf{A}^{-1}\right)^{-1}=\mathbf{A}   \tag*{(7.103)}$$

$$  \left(\mathbf{A}\mathbf{B}\right)^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}   \tag*{(7.104)}$$

$$  (\mathbf{A}^{-1})^{\mathsf{T}}=(\mathbf{A}^{\mathsf{T}})^{-1}\triangleq\mathbf{A}^{-T}   \tag*{(7.105)}$$

对于 2×2 矩阵的情况，$ A^{-1} $ 的表达式足够简单，可以显式给出。我们有

$$  \mathbf{A}=\begin{pmatrix}{{{a}}}&{{{b}}} \\{{{c}}}&{{{d}}}\end{pmatrix},\mathbf{A}^{-1}=\frac{1}{|\mathbf{A}|}\begin{pmatrix}{{{d}}}&{{{-b}}} \\{{{-c}}}&{{{a}}}\end{pmatrix}   \tag*{(7.106)}$$

对于分块对角矩阵，其逆可通过分别对每一块求逆得到，例如：

$$  \begin{pmatrix}\mathbf{A}&\mathbf{0}\\\mathbf{0}&\mathbf{B}\end{pmatrix}^{-1}=\begin{pmatrix}\mathbf{A}^{-1}&\mathbf{0}\\\mathbf{0}&\mathbf{B}^{-1}\end{pmatrix}   \tag*{(7.107)}$$

2. 这些优化在 opt-einsum 库 [GASG18] 中实现。其核心功能包含在 NumPy 和 JAX 的 einsum 函数中，但需设置 optimize=True 参数。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 7.3.2  Schur 补  $ * $

本节中，我们回顾一些关于块结构矩阵的有用结果。

**定理 7.3.1（分块矩阵的逆）.** 考虑一个一般分块矩阵

$$  \mathbf{M}=\begin{pmatrix}\mathbf{E}&\mathbf{F}\\ \mathbf{G}&\mathbf{H}\end{pmatrix}   \tag*{(7.108)}$$

其中我们假设 $\mathbf{E}$ 和 $\mathbf{H}$ 可逆。我们有

$$  \begin{aligned}\mathbf{M}^{-1}&=\begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1}&-(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\\-\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}&\mathbf{H}^{-1}+\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\end{pmatrix}\\&=\begin{pmatrix}\mathbf{E}^{-1}+\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&-\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\\-(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&(\mathbf{M}/\mathbf{E})^{-1}\end{pmatrix}\end{aligned}   \tag*{(7.109)}$$

其中

$$  \mathbf{M}/\mathbf{H}\triangleq\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}   \tag*{(7.111)}$$

$$  \mathbf{M}/\mathbf{E}\triangleq\mathbf{H}-\mathbf{G}\mathbf{E}^{-1}\mathbf{F}   \tag*{(7.112)}$$

我们称 $\mathbf{M}/\mathbf{H}$ 是 $\mathbf{M}$ 关于 $\mathbf{H}$ 的 Schur 补，$\mathbf{M}/\mathbf{E}$ 是 $\mathbf{M}$ 关于 $\mathbf{E}$ 的 Schur 补。

式 (7.109) 和式 (7.110) 被称为**分块求逆公式**。

**证明.** 如果我们可以将 $\mathbf{M}$ 块对角化，那么求逆会更容易。为了消去 $\mathbf{M}$ 的右上角块，我们可以进行如下左乘：

$$  \begin{pmatrix}{{{\mathbf{I}}}}&{{{-\mathbf{F}\mathbf{H}^{-1}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{I}}}}\end{pmatrix}\begin{pmatrix}{{{\mathbf{E}}}}&{{{\mathbf{F}}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}=\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{0}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}   \tag*{(7.113)}$$

类似地，为了消去左下角块，我们可以进行如下右乘：

$$  \begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}\begin{pmatrix}{{{\mathbf{I}}}}&{{{\mathbf{0}}}} \\{{{-\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{I}}}}\end{pmatrix}=\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{H}}}}\end{pmatrix}   \tag*{(7.114)}$$

综合起来，我们得到

$$  \underbrace{\begin{pmatrix}{{{\mathbf{I}}}}&{{{-\mathbf{F}\mathbf{H}^{-1}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{I}}}}\end{pmatrix}}_{X}\underbrace{\begin{pmatrix}{{{\mathbf{E}}}}&{{{\mathbf{F}}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}}_{M}\underbrace{\begin{pmatrix}{{{\mathbf{I}}}}&{{{\mathbf{0}}}} \\{{{-\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{I}}}}\end{pmatrix}}_{Z}=\underbrace{\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{H}}}}\end{pmatrix}}_{W}   \tag*{(7.115)}$$

两边取逆得到

$$  \mathbf{Z}^{-1}\mathbf{M}^{-1}\mathbf{X}^{-1}=\mathbf{W}^{-1}   \tag*{(7.116)}$$

$$  \mathbf{M}^{-1}=\mathbf{Z}\mathbf{W}^{-1}\mathbf{X}   \tag*{(7.117)}$$

---

代入定义，我们得到

$$  \begin{pmatrix}\mathbf{E}&\mathbf{F}\\\mathbf{G}&\mathbf{H}\end{pmatrix}^{-1}=\begin{pmatrix}\mathbf{I}&\mathbf{0}\\-\mathbf{H}^{-1}\mathbf{G}&\mathbf{I}\end{pmatrix}\begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1}&\mathbf{0}\\\mathbf{0}&\mathbf{H}^{-1}\end{pmatrix}\begin{pmatrix}\mathbf{I}&-\mathbf{F}\mathbf{H}^{-1}\\\mathbf{0}&\mathbf{I}\end{pmatrix}   \tag*{(7.118)}$$

$$  \begin{aligned}=\begin{pmatrix}{{{(\mathbf{M}/\mathbf{H})^{-1}}}}&{{{\mathbf{0}}}} \\{{{-\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}}}}&{{{\mathbf{H}^{-1}}}}\end{pmatrix}\begin{pmatrix}{{{\mathbf{I}}}}&{{{-\mathbf{F}\mathbf{H}^{-1}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{I}}}}\end{pmatrix}\end{aligned}   \tag*{(7.119)}$$

$$  \begin{aligned}=\begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1}&-(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\\-\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}&\mathbf{H}^{-1}+\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\end{pmatrix}\end{aligned}   \tag*{(7.120)}$$

另一种方式，我们可以用 $\mathbf{E}$ 和 $\mathbf{M}/\mathbf{E} = (\mathbf{H} - \mathbf{G}\mathbf{E}^{-1}\mathbf{F})$ 来分解矩阵 $\mathbf{M}$，从而得到

$$  \begin{pmatrix}\mathbf{E}&\mathbf{F}\\\mathbf{G}&\mathbf{H}\end{pmatrix}^{-1}=\begin{pmatrix}\mathbf{E}^{-1}+\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&-\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\\-(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&(\mathbf{M}/\mathbf{E})^{-1}\end{pmatrix}   \tag*{(7.121)}$$

☐

#### 7.3.3 矩阵求逆引理  $ * $

 $$ \left(\mathbf{M}/\mathbf{H}\right)^{-1}=\left(\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}\right)^{-1}=\mathbf{E}^{-1}+\mathbf{E}^{-1}\mathbf{F}(\mathbf{H}-\mathbf{G}\mathbf{E}^{-1}\mathbf{F})^{-1}\mathbf{G}\mathbf{E}^{-1} $$ 

将方程(7.119)中第一个矩阵的左上角块与方程(7.121)中矩阵的左上角块相等，可得

这被称为 **矩阵求逆引理** 或 Sherman-Morrison-Woodbury 公式。

机器学习中的一个典型应用如下。设 $\mathbf{X}$ 为 $N \times D$ 数据矩阵，$\mathbf{\Sigma}$ 为 $N \times N$ 对角矩阵。则我们有（利用替换 $\mathbf{E} = \mathbf{\Sigma}$，$\mathbf{F} = \mathbf{G}^{\mathrm{T}} = \mathbf{X}$，以及 $\mathbf{H}^{-1} = -\mathbf{I}$）如下结果：

$$  (\boldsymbol{\Sigma}+\mathbf{X}\mathbf{X}^{\mathrm{T}})^{-1}=\boldsymbol{\Sigma}^{-1}-\boldsymbol{\Sigma}^{-1}\mathbf{X}(\mathbf{I}+\mathbf{X}^{\mathrm{T}}\boldsymbol{\Sigma}^{-1}\mathbf{X})^{-1}\mathbf{X}^{\mathrm{T}}\boldsymbol{\Sigma}^{-1}   \tag*{(7.123)}$$

左端计算需 $ O(N^{3}) $ 时间，右端计算需 $ O(D^{3}) $ 时间。

另一个应用涉及逆矩阵的秩一更新。设 $ \mathbf{E} = \mathbf{A} $，$ \mathbf{F} = \mathbf{u} $，$ \mathbf{G} = \mathbf{v}^\top $，以及 $ H = -1 $。则我们有

$$  (\mathbf{A}+\mathbf{u}\mathbf{v}^{\mathsf{T}})^{-1}=\mathbf{A}^{-1}+\mathbf{A}^{-1}\mathbf{u}(-1-\mathbf{v}^{\mathsf{T}}\mathbf{A}^{-1}\mathbf{u})^{-1}\mathbf{v}^{\mathsf{T}}\mathbf{A}^{-1}   \tag*{(7.124)}$$

$$  =\mathbf{A}^{-1}-\frac{\mathbf{A}^{-1}\mathbf{u}\mathbf{v}^{\top}\mathbf{A}^{-1}}{1+\mathbf{v}^{\top}\mathbf{A}^{-1}\mathbf{u}}   \tag*{(7.125)}$$

这被称为 Sherman-Morrison 公式。

#### 7.3.4 矩阵行列式引理  $ * $

现在我们利用上述结果推导一种高效计算分块矩阵行列式的方法。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

由式 $(7.115)$ 可得

$$  \left\| \mathbf{X} \right\| \left\| \mathbf{M} \right\| \left\| \mathbf{Z} \right\|= \left\| \mathbf{W} \right\|= \left\| \mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G} \right\| \left\| \mathbf{H} \right\|   \tag*{(7.126)}$$

$$  \left|\begin{pmatrix}\mathbf{E}&\mathbf{F}\\\mathbf{G}&\mathbf{H}\\\end{pmatrix}\right|=|\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}||\mathbf{H}|   \tag*{(7.127)}$$

$$  \left|M\right|=\left|M/H\right|\left|H\right|   \tag*{(7.128)}$$

$$  \left|\mathbf{M}/\mathbf{H}\right|=\frac{\left|\mathbf{M}\right|}{\left|\mathbf{H}\right|}   \tag*{(7.129)}$$

因此我们可以看到 $M/H$ 的作用类似于除法运算符（这也是该符号的由来）。

 $$ \left\| \mathbf{M} \right\|= \left\| \mathbf{M}/\mathbf{H} \right\| \left\| \mathbf{H} \right\|= \left\| \mathbf{M}/\mathbf{E} \right\| \left\| \mathbf{E} \right\| $$ 

此外，我们有

$$  \left|\mathbf{M}/\mathbf{H}\right|=\frac{\left|\mathbf{M}/\mathbf{E}\right|\left|\mathbf{E}\right|}{\left|\mathbf{H}\right|}   \tag*{(7.131)}$$

$$  \left|\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}\right|=\left|\mathbf{H}-\mathbf{G}\mathbf{E}^{-1}\mathbf{F}\right|\left|\mathbf{H}^{-1}\right|\left|\mathbf{E}\right|   \tag*{(7.132)}$$

因此（设 $\mathbf{E}=\mathbf{A}$, $\mathbf{F}=-\boldsymbol{u}$, $\mathbf{G}=\boldsymbol{v}^{\mathsf{T}}$, $\mathbf{H}=1$）可得

$$  |\mathbf{A}+u\boldsymbol{v}^{\mathsf{T}}|=(1+v^{\mathsf{T}}\mathbf{A}^{-1}\boldsymbol{u})|\mathbf{A}|   \tag*{(7.133)}$$

这被称为矩阵行列式引理。

#### 7.3.5 应用：推导多元正态分布的条件分布 *

考虑联合高斯分布 $p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu},\boldsymbol{\Sigma})$，其中

$$  \boldsymbol{\mu}=\begin{pmatrix}\boldsymbol{\mu}_{1}\\ \boldsymbol{\mu}_{2}\end{pmatrix},\quad\boldsymbol{\Sigma}=\begin{pmatrix}\boldsymbol{\Sigma}_{11}&\boldsymbol{\Sigma}_{12}\\ \boldsymbol{\Sigma}_{21}&\boldsymbol{\Sigma}_{22}\end{pmatrix}   \tag*{(7.134)}$$

在 3.2.3 节中，我们曾指出

$$  p(\boldsymbol{x}_{1}|\boldsymbol{x}_{2})=\mathcal{N}(\boldsymbol{x}_{1}|\boldsymbol{\mu}_{1}+\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}),\ \boldsymbol{\Sigma}_{11}-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21})   \tag*{(7.135)}$$

在本节中，我们将利用舒尔补来推导该结果。

将联合分布 $p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})$ 分解为 $p(\boldsymbol{x}_{2})p(\boldsymbol{x}_{1}|\boldsymbol{x}_{2})$ 如下：

$$  p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})\propto\exp\left\{-\frac{1}{2}\begin{pmatrix}\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}\\ \boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}\end{pmatrix}^{\top}\begin{pmatrix}\boldsymbol{\Sigma}_{11}&\boldsymbol{\Sigma}_{12}\\ \boldsymbol{\Sigma}_{21}&\boldsymbol{\Sigma}_{22}\end{pmatrix}^{-1}\begin{pmatrix}\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}\\ \boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}\end{pmatrix}\right\}   \tag*{(7.136)}$$

---

使用公式 (7.118)，上述指数变为

$$  p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})\propto\exp\left\{-\frac{1}{2}\begin{pmatrix}{{{\boldsymbol{x}_{1}-\mu_{1}}}} \\{{{\boldsymbol{x}_{2}-\mu_{2}}}}\end{pmatrix}^{\top}\begin{pmatrix}{{{\mathbf{I}}}}&{{{\mathbf{0}}}} \\{{{-\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}}}}&{{{\mathbf{I}}}}\end{pmatrix}\begin{pmatrix}{{{(\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22})^{-1}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{0}}}}&{{{\boldsymbol{\Sigma}_{22}^{-1}}}}\end{pmatrix}\right.   \tag*{(7.137)}$$

$$  \times\begin{pmatrix}\mathbf{I}&-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\\\mathbf{0}&\mathbf{I}\end{pmatrix}\begin{pmatrix}\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}\\\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}\end{pmatrix}   \tag*{(7.138)}$$

$$  =\exp\left\{-\frac{1}{2}(\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}))^{\top}(\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22})^{-1}\right.   \tag*{(7.139)}$$

$$  \left(\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})\right)\times\exp\left\{-\frac{1}{2}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})^{\top}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})\right\}   \tag*{(7.140)}$$

这可以写成如下形式

$$  \exp(\boldsymbol{x}_{1},\boldsymbol{x}_{2}的二次型)\times\exp(\boldsymbol{x}_{2}的二次型)   \tag*{(7.141)}$$

因此，我们成功地将联合分布分解为

$$  p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})=p(\boldsymbol{x}_{1}|\boldsymbol{x}_{2})p(\boldsymbol{x}_{2})   \tag*{(7.142)}$$

$$  =\mathcal{N}(\boldsymbol{x}_{1}|\boldsymbol{\mu}_{1|2},\boldsymbol{\Sigma}_{1|2})\mathcal{N}(\boldsymbol{x}_{2}|\boldsymbol{\mu}_{2},\boldsymbol{\Sigma}_{22})   \tag*{(7.143)}$$

其中条件分布的参数可从上述公式中读出，使用

$$  \boldsymbol{\mu}_{1|2}=\boldsymbol{\mu}_{1}+\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})   \tag*{(7.144)}$$

$$  \mathbf{\Sigma}_{1|2}=\mathbf{\Sigma}/\mathbf{\Sigma}_{22}=\mathbf{\Sigma}_{11}-\mathbf{\Sigma}_{12}\mathbf{\Sigma}_{22}^{-1}\mathbf{\Sigma}_{21}   \tag*{(7.145)}$$

我们还可以利用 $ |\mathbf{M}| = |\mathbf{M}/\mathbf{H}||\mathbf{H}| $ 这一事实来验证归一化常数是否正确：

$$  \begin{align*}(2\pi)^{(d_{1}+d_{2})/2}|\boldsymbol{\Sigma}|^{\frac{1}{2}}&=(2\pi)^{(d_{1}+d_{2})/2}(|\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22}|\;|\boldsymbol{\Sigma}_{22}|)^{\frac{1}{2}}\\ &=(2\pi)^{d_{1}/2}|\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22}|^{\frac{1}{2}}\;(2\pi)^{d_{2}/2}|\boldsymbol{\Sigma}_{22}|^{\frac{1}{2}}\end{align*}   \tag*{(7.146)}$$

其中 $ d_{1}=\dim(\boldsymbol{x}_{1}) $ 且 $ d_{2}=\dim(\boldsymbol{x}_{2}) $。

### 7.4 特征值分解（EVD）

本节回顾关于方阵（实值）特征值分解（EVD）的一些标准内容。

#### 7.4.1 基础

给定一个方阵 $ \mathbf{A} \in \mathbb{R}^{n \times n} $，如果 $ \lambda \in \mathbb{R} $ 是 $ \mathbf{A} $ 的一个特征值，且 $ \boldsymbol{u} \in \mathbb{R}^n $ 是对应的特征向量，那么满足

$$  \mathbf{A}\boldsymbol{u}=\lambda\boldsymbol{u},\quad\boldsymbol{u}\neq\boldsymbol{0}.   \tag*{(7.148)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可。

---

直观上，该定义意味着矩阵 $ \mathbf{A} $ 与向量 $ \mathbf{u} $ 相乘得到的新的向量与 $ \mathbf{u} $ 方向相同，但缩放因子为 $ \lambda $。例如，如果 $ \mathbf{A} $ 是旋转矩阵，则 $ \mathbf{u} $ 是旋转轴，且 $ \lambda = 1 $。

注意，对于任意特征向量 $ \boldsymbol{u} \in \mathbb{R}^n $ 和标量 $ c \in \mathbb{R} $，有

$$  \mathbf{A}(c\mathbf{u})=c\mathbf{A}\mathbf{u}=c\lambda\mathbf{u}=\lambda(c\mathbf{u})   \tag*{(7.149)}$$

因此 $ \mathbf{c}\mathbf{u} $ 也是特征向量。因此，当我们谈论与 $ \lambda $ 对应的“特征向量”时，通常假设特征向量被归一化为长度为 1（这仍然会产生一些歧义，因为 $ \mathbf{u} $ 和 $ -\mathbf{u} $ 都是特征向量，但我们不得不接受这一点）。

我们可以将上述方程重写为：如果满足

$$  (\lambda\mathbf{I}-\mathbf{A})\boldsymbol{u}=\mathbf{0},\quad\boldsymbol{u}\neq\boldsymbol{0}.   \tag*{(7.150)}$$

则 (λ, x) 是 A 的一个特征值-特征向量对。现在 $(\lambda\mathbf{I}-\mathbf{A})\boldsymbol{u}=\mathbf{0}$ 存在非零解 $\boldsymbol{u}$ 当且仅当 $(\lambda\mathbf{I}-\mathbf{A})$ 具有非空的零空间，而这只有在 $(\lambda\mathbf{I}-\mathbf{A})$ 是奇异矩阵时才成立，即

$$  \det(\lambda\mathbf{I}-\mathbf{A})=0\quad.   \tag*{(7.151)}$$

这被称为 A 的特征方程（参见练习 7.2）。该方程的 n 个解即为 n 个（可能是复数值的）特征值 $\lambda_{i}$，而 $u_{i}$ 是对应的特征向量。标准做法是按照特征值的降序对特征向量进行排序，模最大的特征向量排在首位。

以下是特征值和特征向量的一些性质。

• 矩阵的迹等于其特征值之和，

$$  \mathrm{tr}(\mathbf{A})=\sum_{i=1}^{n}\lambda_{i}\quad.   \tag*{(7.152)}$$

• 矩阵 A 的行列式等于其特征值之积，

$$  \det(\mathbf{A})=\prod_{i=1}^{n}\lambda_{i}\quad.   \tag*{(7.153)}$$

• 矩阵 A 的秩等于其非零特征值的个数。

• 如果 A 是非奇异矩阵，则 $ 1/\lambda_i $ 是 $ A^{-1} $ 的特征值，对应的特征向量为 $ u_i $，即 $ A^{-1}u_i = (1/\lambda_i)u_i $。

• 对角矩阵或三角矩阵的特征值即为其对角线元素。

#### 7.4.2 对角化

我们可以将所有特征向量方程同时写为

$$  \mathbf{A}\mathbf{U}=\mathbf{U}\mathbf{\Lambda}   \tag*{(7.154)}$$

---

其中矩阵 $ \mathbf{U} \in \mathbb{R}^{n \times n} $ 的列为 $ \mathbf{A} $ 的特征向量，$ \mathbf{\Lambda} $ 是对角矩阵，其对角线元素为 $ \mathbf{A} $ 的特征值，即

$$  \mathbf{U}\in\mathbb{R}^{n\times n}=\left[\begin{array}{ccc}\mid&|\ &\\\mathbf{u}_{1}&\mathbf{u}_{2}&\cdots&\mathbf{u}_{n}\\\mid&|\ &|\end{array}\right],\mathbf{\Lambda}=diag(\lambda_{1},\ldots,\lambda_{n})\ .   \tag*{(7.155)}$$

如果 $\mathbf{A}$ 的特征向量线性无关，则矩阵 $\mathbf{U}$ 可逆，因此

$$  \mathbf{A}=\mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{-1}   \tag*{(7.156)}$$

可以写成这种形式的矩阵称为可对角化矩阵。

#### 7.4.3 对称矩阵的特征值和特征向量

当 $\mathbf{A}$ 是实对称矩阵时，可以证明所有特征值均为实数，且特征向量是标准正交的，即若 $i \neq j$，则 $\mathbf{u}_i^\top \mathbf{u}_j = 0$，且 $\mathbf{u}_i^\top \mathbf{u}_i = 1$，其中 $\mathbf{u}_i$ 是特征向量。用矩阵形式表示为 $\mathbf{U}^\top \mathbf{U} = \mathbf{U} \mathbf{U}^\top = \mathbf{I}$；因此 $\mathbf{U}$ 是一个正交矩阵。

于是我们可以将 $\mathbf{A}$ 表示为

$$  \begin{aligned}\mathbf{A}&=\mathbf{U}\mathbf{\Lambda}\mathbf{U}^{\mathsf{T}}=\begin{pmatrix}|\quad|&\quad|\\\mathbf{u}_{1}&\mathbf{u}_{2}&\cdots&\mathbf{u}_{n}\\\end{pmatrix}\begin{pmatrix}\lambda_{1}&&\\&\lambda_{2}&\\&&\ddots&\\&&&\lambda_{n}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{u}_{1}^{\mathsf{T}}&-&\\-\quad\mathbf{u}_{2}^{\mathsf{T}}&-&\\&\vdots&\\-\quad\mathbf{u}_{n}^{\mathsf{T}}&-&\\&\end{pmatrix}\\&=\lambda_{1}\begin{pmatrix}|\quad|\\\mathbf{u}_{1}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{u}_{1}^{\mathsf{T}}&-\end{pmatrix}+\cdots+\lambda_{n}\begin{pmatrix}|\quad|\\\mathbf{u}_{n}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{u}_{n}^{\mathsf{T}}&-\end{pmatrix}=\sum_{i=1}^{n}\lambda_{i}\mathbf{u}_{i}\mathbf{u}_{i}^{\mathsf{T}}\\\end{aligned}   \tag*{(7.157)}$$

因此，与任意对称矩阵 $\mathbf{A}$ 相乘可以解释为先乘以旋转矩阵 $ \mathbf{U}^{\top} $，再乘以缩放矩阵 $ \Lambda $，最后乘以逆旋转矩阵 $ \mathbf{U} $。

一旦对角化一个矩阵，求逆就变得容易了。由于 $ \mathbf{A} = \mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{\mathrm{T}} $，其中 $ \mathbf{U}^{\mathrm{T}} = \mathbf{U}^{-1} $，我们有

$$  \mathbf{A}^{-1}=\mathbf{U}\boldsymbol{\Lambda}^{-1}\mathbf{U}^{\mathrm{T}}=\sum_{i=1}^{d}\frac{1}{\lambda_{i}}\boldsymbol{u}_{i}\boldsymbol{u}_{i}^{\mathrm{T}}   \tag*{(7.159)}$$

这对应于先旋转，再逆缩放，最后旋转回来。

##### 7.4.3.1 检查正定性

我们也可以利用对角化性质来证明：如果对称矩阵的所有特征值都为正，则该矩阵是正定的。为了说明这一点，注意到

$$  \boldsymbol{x}^{\mathrm{T}}\mathbf{A}\boldsymbol{x}=\boldsymbol{x}^{\mathrm{T}}\mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{\mathrm{T}}\boldsymbol{x}=\boldsymbol{y}^{\mathrm{T}}\boldsymbol{\Lambda}\boldsymbol{y}=\sum_{i=1}^{n}\lambda_{i}y_{i}^{2}   \tag*{(7.160)}$$

其中 $ \mathbf{y} = \mathbf{U}^\top \mathbf{x} $。由于 $ y_i^2 $ 总是非负的，该表达式的符号完全取决于 $ \lambda_i $。如果所有 $ \lambda_i > 0 $，则矩阵为正定；如果所有 $ \lambda_i \geq 0 $，则为半正定。类似地，如果所有 $ \lambda_i < 0 $ 或 $ \lambda_i \leq 0 $，则 $ \mathbf{A} $ 分别为负定或半负定。最后，如果 $ \mathbf{A} $ 同时具有正特征值和负特征值，则为不定矩阵。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_378_127_793_394.jpg" alt="图像" width="36%" /></div>


<div style="text-align: center;">图7.6: 二维空间中二次型 $ (\mathbf{x} - \boldsymbol{\mu})^{\top} \mathbf{A}(\mathbf{x} - \boldsymbol{\mu}) $ 水平集的可视化。椭圆的长轴和短轴由 $ \mathbf{A} $ 的前两个特征向量 $ \mathbf{u}_1 $ 和 $ \mathbf{u}_2 $ 定义。改编自文献[Bis06]的图2.7。由 gaussEvec.ipynb 生成。</div>


#### 7.4.4 二次型的几何特性

二次型是一种可以写为如下形式的函数：

$$  f(\boldsymbol{x})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}   \tag*{(7.161)}$$

其中 $ x \in \mathbb{R}^n $，且 $ A $ 是一个正定对称的 $ n \times n $ 矩阵。令 $ A = U \Lambda U^\top $ 为 $ A $ 的对角化分解（参见7.4.3节）。因此我们可以写出：

$$  f(\boldsymbol{x})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}=\boldsymbol{x}^{\top}\mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{\top}\boldsymbol{x}=\boldsymbol{y}^{\top}\boldsymbol{\Lambda}\boldsymbol{y}=\sum_{i=1}^{n}\lambda_{i}y_{i}^{2}   \tag*{(7.162)}$$

其中 $ y_i = \boldsymbol{x}^t \boldsymbol{u}_i $，且 $ \lambda_i > 0 $（因为 $ \mathbf{A} $ 是正定的）。$ f(\boldsymbol{x}) $ 的水平集定义了超椭球。例如，在二维空间中，我们有

$$  \lambda_{1}y_{1}^{2}+\lambda_{2}y_{2}^{2}=r   \tag*{(7.163)}$$

这正是二维椭圆的方程，如图7.6所示。特征向量决定了椭圆的方向，特征值决定了椭圆的拉长程度。特别地，椭圆的半长轴和半短轴满足 $ a^{-2} = \lambda_1 $ 和 $ b^{-2} = \lambda_2 $。对于高斯分布，我们有 $ \mathbf{A} = \Sigma^{-1} $，因此较小的 $ \lambda_i $ 值对应后验精度较低、方差较大的方向。

#### 7.4.5 数据标准化与白化

假设我们有一个数据集 $ \mathbf{X} \in \mathbb{R}^{N \times D} $。通常会对数据进行预处理，使得每一列具有零均值和单位方差。这称为数据的**标准化**，我们将在10.2.8节中讨论。虽然标准化强制方差为1，但并未消除列之间的相关性。要消除相关性，需要对数据进行**白化**。为定义白化，令经验协方差矩阵

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_209_139_540_395.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_606_138_947_399.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_213_460_541_721.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_617_460_949_724.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图7.7: (a) 身高/体重数据. (b) 标准化. (c) PCA白化. (d) ZCA白化. 数字指前4个数据点，但总共有73个数据点。由 height_weight_whiten_plot.ipynb 生成。</div>


设 $\mathbf{S} = \frac{1}{N} \mathbf{X}^{\mathrm{T}} \mathbf{X}$，并令 $\mathbf{S} = \mathbf{E} \mathbf{D} \mathbf{E}^{\mathrm{T}}$ 为其对角化。等价地，令 $[\mathbf{U}, \mathbf{S}, \mathbf{V}]$ 为 $\frac{1}{\sqrt{N}} \mathbf{X}$ 的 SVD（因此 $\mathbf{E} = \mathbf{V}$ 且 $\mathbf{D} = \mathbf{S}^2$，如我们在第20.1.3.3节所述）。现在定义

$$  \mathbf{W}_{p c a}=\mathbf{D}^{-\frac{1}{2}}\mathbf{E}^{\mathsf{T}}   \tag*{(7.164)}$$

这被称为 PCA 白化矩阵。（我们在第20.1节讨论 PCA。）令 $\boldsymbol{y} = \boldsymbol{W}_{pca} \boldsymbol{x}$ 为一个变换后的向量。我们可以如下检查其协方差是否为白化：

$$  \mathrm{Cov}\left[\boldsymbol{y}\right]=\mathbf{W}\mathbb{E}\left[\boldsymbol{x}\boldsymbol{x}^{\mathrm{T}}\right]\mathbf{W}^{\mathrm{T}}=\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^{\mathrm{T}}=(\mathbf{D}^{-\frac{1}{2}}\mathbf{E}^{\mathrm{T}})(\mathbf{E}\mathbf{D}\mathbf{E}^{\mathrm{T}})(\mathbf{E}\mathbf{D}^{-\frac{1}{2}})=\mathbf{I}   \tag*{(7.165)}$$

白化矩阵不是唯一的，因为它的任何旋转 $\mathbf{W} = \mathbf{R} \mathbf{W}_{pca}$ 仍将保持白化性质，即 $\mathbf{W}^\top \mathbf{W} = \boldsymbol{\Sigma}^{-1}$。例如，取 $\mathbf{R} = \mathbf{E}$，我们得到

$$  \mathbf{W}_{zca}=\mathbf{E}\mathbf{D}^{-\frac{1}{2}}\mathbf{E}^{\mathsf{T}}=\boldsymbol{\Sigma}^{-\frac{1}{2}}=\mathbf{V}\mathbf{S}^{-1}\mathbf{V}^{\mathsf{T}}   \tag*{(7.166)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

这被称为马氏白化或ZCA（ZCA代表“零相位成分分析”，由[BS97]引入）。与PCA白化相比，ZCA白化的优势在于，变换后的数据尽可能接近于原始数据（在最小二乘意义上）[Amo17]。如图7.7所示。当应用于图像时，ZCA变换后的数据向量仍然看起来像图像。这在深度学习中应用该方法时非常有用[KH09]。

#### 7.4.6 幂法

我们现在描述一种简单的迭代方法，用于计算实对称矩阵最大特征值对应的特征向量；这称为幂法。当矩阵非常大但稀疏时，该方法非常有用。例如，谷歌的PageRank用它来计算万维网转移矩阵的平稳分布（一个规模约为30亿乘30亿的矩阵！）。在7.4.7节中，我们将看到如何使用这种方法计算后续的特征向量和特征值。

令 $\mathbf{A}$ 是一个具有标准正交特征向量 $\mathbf{u}_i$ 和特征值 $|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_m| \geq 0$ 的矩阵，因此 $\mathbf{A} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^\top$。令 $\mathbf{v}_{(0)}$ 是 $\mathbf{A}$ 值域中的任意向量，因此存在某个 $\mathbf{x}$ 使得 $\mathbf{A}\mathbf{x} = \mathbf{v}_{(0)}$。因此我们可以将 $\mathbf{v}_{(0)}$ 写为

$$  \boldsymbol{v}_{0}=\mathbf{U}(\boldsymbol{\Lambda}\mathbf{U}^{\top}\boldsymbol{x})=a_{1}\boldsymbol{u}_{1}+\cdots+a_{m}\boldsymbol{u}_{m}   \tag*{(7.167)}$$

其中 $a_i$ 为常数。现在我们可以反复将 $\mathbf{v}$ 乘以 $\mathbf{A}$ 并重新归一化：

$$  \boldsymbol{v}_{t}\propto\mathbf{A}\boldsymbol{v}_{t-1}   \tag*{(7.168)}$$

（我们在每次迭代中进行归一化以保证数值稳定性。）

由于 $\boldsymbol{v}_t$ 是 $\mathbf{A}^t \boldsymbol{v}_0$ 的倍数，我们有

$$  \begin{aligned}\boldsymbol{v}_{t}&\propto a_{1}\lambda_{1}^{t}\boldsymbol{u}_{1}+a_{2}\lambda_{2}^{t}\boldsymbol{u}_{2}+\cdots+a_{m}\lambda_{m}^{t}\boldsymbol{u}_{m}\\&=\lambda_{1}^{t}\left(a_{1}\boldsymbol{u}_{1}+a_{1}(\lambda_{2}/\lambda_{1})^{t}\boldsymbol{u}_{2}+\cdots+a_{m}(\lambda_{m}/\lambda_{1})^{t}\boldsymbol{u}_{m}\right)\\&\rightarrow\lambda_{1}^{t}a_{1}\boldsymbol{u}_{1}\end{aligned}   \tag*{(7.170)}$$

因为对于 $k > 1$ 有 $\left|\frac{\lambda_k}{\lambda_1}\right| < 1$（假设特征值按降序排列）。因此我们看到它收敛到 $\boldsymbol{u}_1$，尽管速度不快（每次迭代误差大约减少 $|\lambda_2/\lambda_1|$ 倍）。唯一的要求是初始猜测满足 $\boldsymbol{v}_0^\top \boldsymbol{u}_1 \neq 0$，这对于随机选取的 $\boldsymbol{v}_0$ 以高概率成立。

现在我们讨论如何计算相应的特征值 $\lambda_1$。定义瑞利商为

$$  R(\mathbf{A},x)\triangleq\frac{x^{\top}\mathbf{A}x}{x^{\top}x}   \tag*{(7.172)}$$

因此

$$  R(\mathbf{A},\boldsymbol{u}_{i})=\frac{\boldsymbol{u}_{i}^{\top}\mathbf{A}\boldsymbol{u}_{i}}{\boldsymbol{u}_{i}^{\top}\boldsymbol{u}_{i}}=\frac{\lambda_{i}\boldsymbol{u}_{i}^{\top}\boldsymbol{u}_{i}}{\boldsymbol{u}_{i}^{\top}\boldsymbol{u}_{i}}=\lambda_{i}   \tag*{(7.173)}$$

于是我们可以从 $\boldsymbol{u}_1$ 和 $\mathbf{A}$ 轻松计算 $\lambda_1$。演示请参见 power_method_demo.ipynb。

---

#### 7.4.7 收缩法

假设我们已通过幂法计算了第一个特征向量和特征值 $ \boldsymbol{u}_{1}, \lambda_{1} $。现在我们描述如何计算后续的特征向量和特征值。由于特征向量是正交归一化的，且特征值是实数，我们可以按如下方式从矩阵中投影出 $ \boldsymbol{u}_{1} $ 分量：

$$  \mathbf{A}^{(2)}=(\mathbf{I}-\boldsymbol{u}_{1}\boldsymbol{u}_{1}^{\top})\mathbf{A}^{(1)}=\mathbf{A}^{(1)}-\boldsymbol{u}_{1}\boldsymbol{u}_{1}^{\top}\mathbf{A}^{(1)}=\mathbf{A}^{(1)}-\lambda_{1}\boldsymbol{u}_{1}\boldsymbol{u}_{1}^{\top}   \tag*{(7.174)}$$

这称为矩阵收缩。然后我们可以对 $ \mathbf{A}^{(2)} $ 应用幂法，它将在与 $ \mathbf{u}_{1} $ 正交的子空间中找到最大的特征向量/特征值。

在 20.1.2 节中，我们展示了 PCA 模型（在 20.1 节中描述）的最优估计 $ \mathbf{W} $ 由经验协方差矩阵的前 $ K $ 个特征向量给出。因此收缩法可用于实现 PCA。它也可以被修改来实现稀疏 PCA [Mac09]。

#### 7.4.8 特征向量优化二次型

我们可以使用矩阵微积分以直接导向特征值/特征向量分析的方式求解一个优化问题。考虑如下等式约束的优化问题：

$$  \max_{\boldsymbol{x}\in\mathbb{R}^{n}}\ \boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}\quad subject to\|\boldsymbol{x}\|_{2}^{2}=1   \tag*{(7.175)}$$

对于一个对称矩阵 $ \mathbf{A} \in \mathbb{S}^n $。求解带有等式约束的优化问题的一种标准方法是构造拉格朗日函数，即包含等式约束的目标函数（见第 8.5.1 节）。此情况下的拉格朗日函数可写为：

$$  \mathcal{L}(\boldsymbol{x},\lambda)=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}+\lambda(1-\boldsymbol{x}^{\top}\boldsymbol{x})   \tag*{(7.176)}$$

其中 $ \lambda $ 称为与等式约束相关联的拉格朗日乘子。可以证明，要使 $ x^{*} $ 成为该问题的最优点，拉格朗日函数在 $ x^{*} $ 处的梯度必须为零（这不是唯一条件，但是必要条件）。即：

$$  \nabla_{x}\mathcal{L}(x,\lambda)=2\mathbf{A}^{\top}x-2\lambda x=\mathbf{0}.   \tag*{(7.177)}$$

注意这正是线性方程 $ \mathbf{A}\mathbf{x} = \lambda\mathbf{x} $。这表明，在 $ \mathbf{x}^\top \mathbf{x} = 1 $ 的条件下，可能最大化（或最小化）$ \mathbf{x}^\top \mathbf{A}\mathbf{x} $ 的点只能是 $ \mathbf{A} $ 的特征向量。

### 7.5 奇异值分解（SVD）

现在我们讨论 SVD，它将 EVD 推广到矩形矩阵。

#### 7.5.1 基本概念

任何一个（实的）$ m \times n $ 矩阵 A 可以分解为：

$$  \mathbf{A}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}}=\sigma_{1}\begin{pmatrix}|\\\mathbf{u}_{1}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{v}_{1}^{\mathsf{T}}&-\end{pmatrix}+\cdots+\sigma_{r}\begin{pmatrix}|\\\mathbf{u}_{r}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{v}_{r}^{\mathsf{T}}&-\end{pmatrix}   \tag*{(7.178)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_121_1016_275.jpg" alt="图片" width="68%" /></div>


<div style="text-align: center;">图 7.8：矩阵的 SVD 分解，$\mathbf{A} = \mathbf{USV}^\top$。每个矩阵中的阴影部分在精简版（economy-sized version）中不会被计算。(a) 高型矩阵。(b) 宽型矩阵。</div>


其中 $\mathbf{U}$ 是一个 $m \times m$ 的矩阵，其列是标准正交的（因此 $\mathbf{U}^\top \mathbf{U} = \mathbf{I}_m$）；$\mathbf{V}$ 是一个 $n \times n$ 的矩阵，其行和列都是标准正交的（因此 $\mathbf{V}^\top \mathbf{V} = \mathbf{V} \mathbf{V}^\top = \mathbf{I}_n$）；$\mathbf{S}$ 是一个 $m \times n$ 的矩阵，其主对角线上包含 $r = \min(m, n)$ 个奇异值 $\sigma_i \geq 0$，其余元素均为 0。$\mathbf{U}$ 的列称为左奇异向量，$\mathbf{V}$ 的列称为右奇异向量。这称为矩阵的奇异值分解，即 SVD。示例如图 7.8 所示。

从图 7.8a 可以明显看出，如果 $m > n$，则最多有 $n$ 个奇异值，因此 $\mathbf{U}$ 的最后 $m - n$ 列是无关的（因为它们将与 0 相乘）。**精简版 SVD**（economy sized SVD），也称为 **瘦版 SVD**（thin SVD），避免了计算这些不必要的元素。换句话说，如果将 $\mathbf{U}$ 矩阵写为 $\mathbf{U} = [\mathbf{U}_1, \mathbf{U}_2]$，我们只计算 $\mathbf{U}_1$。图 7.8b 展示了相反的情况，其中 $m < n$，此时将 $\mathbf{V}$ 表示为 $\mathbf{V} = [\mathbf{V}_1; \mathbf{V}_2]$，并且只计算 $\mathbf{V}_1$。

计算 SVD 的代价为 $O(\min(mn^2, m^2n))$。其工作原理的详细信息可参见标准线性代数教材。

#### 7.5.2 SVD 与 EVD 的联系

如果 $\mathbf{A}$ 是实对称正定矩阵，则奇异值等于特征值，左、右奇异向量等于特征向量（相差一个符号变化）：

$$  \mathbf{A}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathrm{T}}=\mathbf{U}\mathbf{S}\mathbf{U}^{\mathrm{T}}=\mathbf{U}\mathbf{S}\mathbf{U}^{-1}   \tag*{(7.179)}$$

但需要注意的是，NumPy 总是按降序返回奇异值，而特征值则不一定需要排序。

一般来说，对于任意实矩阵 $\mathbf{A}$，如果 $\mathbf{A} = \mathbf{U} \mathbf{S} \mathbf{V}^{\mathrm{T}}$，则有

$$  \mathbf{A}^{\mathsf{T}}\mathbf{A}=\mathbf{V}\mathbf{S}^{\mathsf{T}}\mathbf{U}^{\mathsf{T}}\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}}=\mathbf{V}(\mathbf{S}^{\mathsf{T}}\mathbf{S})\mathbf{V}^{\mathsf{T}}   \tag*{(7.180)}$$

因此

$$  (\mathbf{A}^{\top}\mathbf{A})\mathbf{V}=\mathbf{V}\mathbf{D}_{n}   \tag*{(7.181)}$$

所以 $\mathbf{A}^\top \mathbf{A}$ 的特征向量等于 $\mathbf{V}$，即 $\mathbf{A}$ 的右奇异向量，而 $\mathbf{A}^\top \mathbf{A}$ 的特征值等于 $\mathbf{D}_n = \mathbf{S}^\top \mathbf{S}$，这是一个 $n \times n$ 的对角矩阵，包含奇异值的平方。类似地，

$$  \mathbf{A}\mathbf{A}^{\mathrm{T}}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathrm{T}}\mathbf{V}\mathbf{S}^{\mathrm{T}}\mathbf{U}^{\mathrm{T}}=\mathbf{U}(\mathbf{S}\mathbf{S}^{\mathrm{T}})\mathbf{U}^{\mathrm{T}}   \tag*{(7.182)}$$

$$  (\mathbf{A}\mathbf{A}^{\mathrm{T}})\mathbf{U}=\mathbf{U}\mathbf{D}_{m}   \tag*{(7.183)}$$

---

因此，$ \mathbf{A}\mathbf{A}^{\top} $ 的特征向量等于 $ \mathbf{U} $，即 $ \mathbf{A} $ 的左奇异向量，而 $ \mathbf{A}\mathbf{A}^{\top} $ 的特征值等于 $ \mathbf{D}_{m}=\mathbf{S}\mathbf{S}^{\top} $，这是一个 $ m\times m $ 的对角矩阵，包含奇异值的平方。总结如下：

$$  \mathbf{U}=\mathrm{e v e c}(\mathbf{A}\mathbf{A}^{\mathsf{T}}),\mathbf{V}=\mathrm{e v e c}(\mathbf{A}^{\mathsf{T}}\mathbf{A}),\mathbf{D}_{m}=\mathrm{e v a l}(\mathbf{A}\mathbf{A}^{\mathsf{T}}),\mathbf{D}_{n}=\mathrm{e v a l}(\mathbf{A}^{\mathsf{T}}\mathbf{A})   \tag*{(7.184)}$$

如果我们仅使用经济型 SVD 中计算出的（非零）部分，那么可以定义

$$  \mathbf{D}=\mathbf{S}^{2}=\mathbf{S}^{\mathsf{T}}\mathbf{S}=\mathbf{S}\mathbf{S}^{\mathsf{T}}   \tag*{(7.185)}$$

另外需要注意的是，即使对于方阵 $\mathbf{A}$，特征值分解 (EVD) 也并非总是存在，而 SVD 总是存在的。

#### 7.5.3 伪逆

矩阵 $\mathbf{A}$ 的 Moore-Penrose 伪逆，记作 $ A^{\dagger} $，定义为满足以下 4 个性质的唯一矩阵：

$$  \mathbf{A}\mathbf{A}^{\dagger}\mathbf{A}=\mathbf{A},\mathbf{A}^{\dagger}\mathbf{A}\mathbf{A}^{\dagger}=\mathbf{A}^{\dagger},(\mathbf{A}\mathbf{A}^{\dagger})^{\mathsf{T}}=\mathbf{A}\mathbf{A}^{\dagger},(\mathbf{A}^{\dagger}\mathbf{A})^{\mathsf{T}}=\mathbf{A}^{\dagger}\mathbf{A}   \tag*{(7.186)}$$

如果 $\mathbf{A}$ 是方阵且非奇异，则 $ A^\dagger = A^{-1} $。

如果 $m > n$（高瘦形）且 $\mathbf{A}$ 的列线性无关（即 $\mathbf{A}$ 满秩），那么

$$  \mathbf{A}^{\dagger}=(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}   \tag*{(7.187)}$$

这与正规方程（参见第 11.2.2.1 节）中出现的表达式相同。在这种情况下，$ \mathbf{A}^{\dagger} $ 是 $ \mathbf{A} $ 的左逆，因为

$$  \mathbf{A}^{\dagger}\mathbf{A}=(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}\mathbf{A}=\mathbf{I}   \tag*{(7.188)}$$

但它不是右逆，因为

$$  \mathbf{A}\mathbf{A}^{\dagger}=\mathbf{A}(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}   \tag*{(7.189)}$$

的秩仅为 $n$，因此不可能成为 $ m \times m $ 的单位矩阵。

如果 $m < n$（矮胖形）且 $\mathbf{A}$ 的行线性无关（即 $\mathbf{A}^{\mathrm{T}}$ 满秩），那么伪逆为

$$  \mathbf{A}^{\dagger}=\mathbf{A}^{\mathsf{T}}(\mathbf{A}\mathbf{A}^{\mathsf{T}})^{-1}   \tag*{(7.190)}$$

在这种情况下，$\mathbf{A}^{\dagger}$ 是 $\mathbf{A}$ 的右逆。

我们可以使用 SVD 分解 $ \mathbf{A} = \mathbf{USV}^\top $ 来计算伪逆。具体来说，可以证明

$$  \mathbf{A}^{\dagger}=\mathbf{V}[\mathrm{diag}(1/\sigma_{1},\cdots,1/\sigma_{r},0,\cdots,0)]\mathbf{U}^{\top}=\mathbf{V}\mathbf{S}^{-1}\mathbf{U}^{\top}   \tag*{(7.191)}$$

其中 $r$ 是矩阵的秩，并且我们定义 $\mathbf{S}^{-1} = \mathrm{diag}(\sigma_1^{-1}, \ldots, \sigma_r^{-1}, 0, \ldots, 0)$。实际上，如果矩阵是方阵且满秩，那么

$$  (\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}})^{-1}=\mathbf{V}\mathbf{S}^{-1}\mathbf{U}^{\mathsf{T}}   \tag*{(7.192)}$$

作者: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 7.5.4 奇异值分解与矩阵的值域和零空间*

本节将证明左奇异向量和右奇异向量分别构成了值域和零空间的标准正交基。

由式 $(7.178)$ 可得：

$$  \mathbf{A}\boldsymbol{x}=\sum_{j:\sigma_{j}>0}\sigma_{j}(\boldsymbol{v}_{j}^{\mathsf{T}}\boldsymbol{x})\boldsymbol{u}_{j}=\sum_{j=1}^{r}\sigma_{j}(\boldsymbol{v}_{j}^{\mathsf{T}}\boldsymbol{x})\boldsymbol{u}_{j}   \tag*{(7.193)}$$

其中 $r$ 为 $\mathbf{A}$ 的秩。因此，任意 $\mathbf{A}\mathbf{x}$ 均可表示为左奇异向量 $\mathbf{u}_{1},\ldots,\mathbf{u}_{r}$ 的线性组合，故 $\mathbf{A}$ 的值域为：

$$  \mathrm{range}(\mathbf{A})=\mathrm{span}\left(\left\{\boldsymbol{u}_{j}:\sigma_{j}>0\right\}\right)   \tag*{(7.194)}$$

其维数为 $r$。

为求得零空间的一组基，现定义另一个向量 $\mathbf{y} \in \mathbb{R}^n$，它仅由对应于零奇异值的右奇异向量线性组合而成：

$$  \boldsymbol{y}=\sum_{j:\sigma_{j}=0}c_{j}\boldsymbol{v}_{j}=\sum_{j=r+1}^{n}c_{j}\boldsymbol{v}_{j}   \tag*{(7.195)}$$

由于 $\boldsymbol{v}_{j}$ 是标准正交的，故有：

$$  \mathbf{A}\boldsymbol{y}=\mathbf{U}\left(\begin{array}{c}\sigma_{1}\boldsymbol{v}_{1}^{\top}\boldsymbol{y}\\ \vdots\\ \sigma_{r}\boldsymbol{v}_{r}^{\top}\boldsymbol{y}\\ \sigma_{r+1}\boldsymbol{v}_{r+1}^{\top}\boldsymbol{y}\\ \vdots\\ \sigma_{n}\boldsymbol{v}_{n}^{\top}\boldsymbol{y}\end{array}\right)=\mathbf{U}\left(\begin{array}{c}\sigma_{1}0\\ \vdots\\ \sigma_{r}0\\ 0\boldsymbol{v}_{r+1}^{\top}\boldsymbol{y}\\ \vdots\\ 0\boldsymbol{v}_{n}^{\top}\boldsymbol{y}\end{array}\right)=\mathbf{U}\mathbf{0}=\mathbf{0}   \tag*{(7.196)}$$

因此，右奇异向量构成零空间的标准正交基：

$$  \mathrm{nullspace}(\mathbf{A})=\mathrm{span}\left(\{\boldsymbol{v}_{j}:\sigma_{j}=0\}\right)   \tag*{(7.197)}$$

其维数为 $n - r$。于是我们有：

$$  \mathrm{dim}(\mathrm{range}(\mathbf{A}))+\mathrm{dim}(\mathrm{nullspace}(\mathbf{A}))=r+(n-r)=n   \tag*{(7.198)}$$

用文字表述，常记为：

$$   \text{秩}+\text{零化度}=n   \tag*{(7.199)}$$

这称为**秩-零化度定理**。由此可知，矩阵的秩等于其非零奇异值的个数。

---

<div style="text-align: center;">秩 200</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_236_183_536_373.jpg" alt="图像" width="26%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;">秩 2</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_644_176_944_373.jpg" alt="图像" width="26%" /></div>

<div style="text-align: center;">秩 5</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_236_506_536_695.jpg" alt="图像" width="26%" /></div>

<div style="text-align: center;">秩 20</div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_645_505_944_694.jpg" alt="图像" width="25%" /></div>

<div style="text-align: center;"> $ (d) $</div>

<div style="text-align: center;">图 7.9：图像的低秩近似。左上角：原始图像大小为 $ 200 \times 320 $，因此秩为 200。后续图像的秩分别为 2、5 和 20。由 svd_image_demo.ipynb 生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_451_902_705_1091.jpg" alt="图像" width="22%" /></div>

<div style="text-align: center;">图 7.10：小丑图像的前 100 个对数奇异值（红线）与随机打乱像素后的数据矩阵的对数奇异值（蓝线）。由 svd_image_demo.ipynb 生成。改编自 [HTF09] 中的图 14.24。</div>

---

#### 7.5.5 截断奇异值分解

设 $\mathbf{A} = \mathbf{U} \mathbf{S} \mathbf{V}^T$ 为 $\mathbf{A}$ 的奇异值分解，并设 $\hat{\mathbf{A}}_K = \mathbf{U}_K \mathbf{S}_K \mathbf{V}_K^T$，其中我们使用 $\mathbf{U}$ 和 $\mathbf{V}$ 的前 $K$ 列。可以证明，这是最优的秩 $K$ 近似，因为它最小化了 $\|\mathbf{A} - \hat{\mathbf{A}}_K\|_F^2$。

如果 $K = r = \text{rank}(\mathbf{A})$，则该分解不会引入误差。但如果 $K < r$，我们会引入一些误差。这被称为 **截断奇异值分解**。如果奇异值快速衰减（这在自然数据中很典型，例如见图7.10），误差将会很小。使用秩 $K$ 近似表示一个 $N \times D$ 矩阵所需的总参数数量为

$$ NK+KD+K=K(N+D+1)   \tag*{(7.200)}$$

例如，考虑图7.9（左上角）中 $200 \times 320$ 像素的图像。它包含64,000个数值。我们观察到，一个秩为20的近似仅需要 $(200 + 320 + 1) \times 20 = 10,420$ 个数值，却是一个非常优秀的近似。

可以证明，该秩K近似的误差由下式给出

$$  \left|\left|\mathbf{A}-\hat{\mathbf{A}}\right|\right|_{F}=\sum_{k=K+1}^{r}\sigma_{k}   \tag*{(7.201)}$$

其中 $\sigma_{k}$ 是 $\mathbf{A}$ 的第 $k$ 个奇异值。

### 7.6 其他矩阵分解 *

在本节中，我们简要回顾其他一些有用的矩阵分解。

#### 7.6.1 LU分解

我们可以将任意方阵 $\mathbf{A}$ 分解为一个下三角矩阵 $\mathbf{L}$ 和一个上三角矩阵 $\mathbf{U}$ 的乘积。例如，

$$  \begin{bmatrix}{{{a_{11}}}}&{{{a_{12}}}}&{{{a_{13}}}} \\{{{a_{21}}}}&{{{a_{22}}}}&{{{a_{23}}}} \\{{{a_{31}}}}&{{{a_{32}}}}&{{{a_{33}}}}\end{bmatrix}=\begin{bmatrix}{{{l_{11}}}}&{{{0}}}&{{{0}}} \\{{{l_{21}}}}&{{{l_{22}}}}&{{{0}}} \\{{{l_{31}}}}&{{{l_{32}}}}&{{{l_{33}}}}\end{bmatrix}\begin{bmatrix}{{{u_{11}}}}&{{{u_{12}}}}&{{{u_{13}}}} \\{{{0}}}&{{{u_{22}}}}&{{{u_{23}}}} \\{{{0}}}&{{{0}}}&{{{u_{33}}}}\end{bmatrix}.   \tag*{(7.202)}$$

一般来说，在生成这种分解之前，我们可能需要置换矩阵中的元素。为了理解这一点，假设 $a_{11} = 0$。由于 $a_{11} = l_{11}u_{11}$，这意味着 $l_{11}$ 或 $u_{11}$ 或两者都必须为零，但这将导致 $\mathbf{L}$ 或 $\mathbf{U}$ 奇异。为了避免这种情况，算法的第一步可以直接重新排序各行，使得第一个元素非零。后续步骤重复此过程。我们可以将此过程表示为

$$   PA=LU   \tag*{(7.203)}$$

其中 $\mathbf{P}$ 是一个置换矩阵，即一个方阵二元矩阵，当第 $j$ 行被置换到第 $i$ 行时 $P_{ij} = 1$。这被称为 **部分主元法**。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_198_118_552_279.jpg" alt="图像" width="30%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_607_215_964_287.jpg" alt="图像" width="30%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 7.11：QR 分解示意图， $ \mathbf{A} = \mathbf{Q}\mathbf{R} $，其中 $ \mathbf{Q}^{\top}\mathbf{Q} = \mathbf{I} $，且 $ \mathbf{R} $ 为上三角矩阵。(a) 高瘦矩阵。在精简版本（economy-sized）中，阴影部分不计算，因为它们不需要。(b) 矮胖矩阵。</div>

#### 7.6.2 QR 分解

假设我们有 $ \mathbf{A} \in \mathbb{R}^{m \times n} $ 表示一组线性无关的基向量（因此 $ m \geq n $），我们希望找到一系列正交向量 $ \mathbf{q}_1, \mathbf{q}_2, \ldots $，它们张成 $ \text{span}(\mathbf{a}_1) $、$ \text{span}(\mathbf{a}_1, \mathbf{a}_2) $ 等的逐次子空间。换句话说，我们希望找到向量 $ \mathbf{q}_j $ 和系数 $ r_{ij} $，使得

$$  \begin{pmatrix}|\quad|&&&\\a_{1}&a_{2}&\cdots&a_{n}\\\end{pmatrix}=\begin{pmatrix}|\quad|&&&|\\q_{1}&q_{2}&\cdots&q_{n}\\\end{pmatrix}\begin{pmatrix}r_{11}&r_{12}&\cdots&r_{1n}\\&r_{22}&\cdots&r_{2n}\\\end{pmatrix}   \tag*{(7.204)}$$

我们可以将其写作

$$  a_{1}=r_{11}q_{1}   \tag*{(7.205)}$$

$$  \boldsymbol{a}_{2}=r_{12}\boldsymbol{q}_{1}+r_{22}\boldsymbol{q}_{2}   \tag*{(7.206)}$$

$$ \therefore $$ 

$$  \boldsymbol{a}_{n}=r_{1n}\boldsymbol{q}_{1}+\cdots+r_{n n}\boldsymbol{q}_{n}   \tag*{(7.207)}$$

因此我们看到，q1 张成 a1 的空间，q1 和 q2 张成 {a1, a2} 的空间，以此类推。

用矩阵符号表示，我们有

$$  \mathbf{A}=\hat{\mathbf{Q}}\hat{\mathbf{R}}   \tag*{(7.208)}$$

其中 $ \hat{Q} $ 是 $ m \times n $ 且列正交的矩阵，$ \hat{R} $ 是 $ n \times n $ 的上三角矩阵。这被称为 A 的简化 QR 分解（reduced QR）或精简版 QR 分解（economy sized QR factorization）；参见图 7.11。

完整 QR 分解对 $ \mathbf{Q} $ 附加额外的 $ m-n $ 个正交列，使其成为方阵正交矩阵 $ \mathbf{Q} $，满足 $ \mathbf{QQ}^{\mathrm{T}}=\mathbf{Q}^{\mathrm{T}}\mathbf{Q}=\mathbf{I} $。同时，我们对 $ \mathbf{R} $ 附加由零组成的行，使其成为 $ m \times n $ 的矩阵，仍然保持上三角，称为 $ \mathbf{R} $：参见图 7.11。$ \mathbf{R} $ 中的零元素“消去”了 $ \mathbf{Q} $ 中的新列，因此结果与 $ \mathbf{\hat{Q}}\mathbf{\hat{R}} $ 相同。

QR 分解常用于求解线性方程组，我们将在第 11.2.2.3 节中讨论。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

#### 7.6.3 乔列斯基分解（Cholesky decomposition）

任意对称正定矩阵都可以分解为 $\mathbf{A} = \mathbf{R}^\top \mathbf{R}$，其中 $\mathbf{R}$ 是上三角矩阵且对角元素为正实数。（也可写作 $\mathbf{A} = \mathbf{L} \mathbf{L}^\top$，其中 $\mathbf{L} = \mathbf{R}^\top$ 是下三角矩阵。）这称为乔列斯基分解或矩阵平方根。在NumPy中，通过 `np.linalg.cholesky` 实现。该操作的计算复杂度为 $O(V^3)$，其中 $V$ 是变量数，但对于稀疏矩阵复杂度可能更低。下面给出该分解的一些应用。

##### 7.6.3.1 应用：从多元正态分布中采样

协方差矩阵的乔列斯基分解可用于从多元高斯分布中采样。设 $\mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 且 $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$。首先采样 $\boldsymbol{x} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$，这很容易，因为它只需从 $d$ 个独立的 $1d$ 高斯分布中采样。然后令 $\mathbf{y} = \mathbf{L}\mathbf{x} + \boldsymbol{\mu}$。这是有效的，因为

$$ \mathrm{Cov}\left[\boldsymbol{y}\right]=\mathrm{L}\mathrm{Cov}\left[\boldsymbol{x}\right]\boldsymbol{L}^{\top}=\mathrm{L}\mathrm{~I~L}^{\top}=\boldsymbol{\Sigma} \tag*{(7.209)}$$

相关代码见 `cholesky_demo.ipynb`。

### 7.7 求解线性方程组 *

线性代数的一个重要应用是研究线性方程组。例如，考虑以下三个方程构成的方程组：

$$ 3x_{1}+2x_{2}-x_{3}=1 \tag*{(7.210)}$$

$$ 2x_{1}-2x_{2}+4x_{3}=-2 \tag*{(7.211)}$$

$$ -x_{1}+\frac{1}{2}x_{2}-x_{3}=0 \tag*{(7.212)}$$

我们可以用矩阵-向量形式表示为：

$$ \mathbf{A}\boldsymbol{x}=\boldsymbol{b} \tag*{(7.213)}$$

其中

$$ \mathbf{A}=\begin{pmatrix}{{{3}}}&{{{2}}}&{{{-1}}} \\{{{2}}}&{{{-2}}}&{{{4}}} \\{{{-1}}}&{{{\frac{1}{2}}}}&{{{-1}}}\end{pmatrix},\mathbf{b}=\begin{pmatrix}{{{1}}} \\{{{-2}}} \\{{{0}}}\end{pmatrix} \tag*{(7.214)}$$

解为 $ x = [1, -2, -2] $。

一般地，如果有 $m$ 个方程和 $n$ 个未知数，则 $\mathbf{A}$ 是 $m \times n$ 矩阵，$\mathbf{b}$ 是 $m \times 1$ 向量。若 $m = n$（且 $\mathbf{A}$ 满秩），则存在唯一解；若 $m < n$，则方程组欠定，不存在唯一解；若 $m > n$，则方程组超定，因为约束多于未知数，并非所有直线都交于同一点。图7.12展示了这一情况。下面我们讨论每种情况下如何计算解。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_304_125_861_251.jpg" alt="图像" width="48%" /></div>

<div style="text-align: center;">图 7.12：一组包含 n=2 个变量的 m 个线性方程的解。(a) m=1<n，因此系统是欠定的。我们将最小范数解用蓝色圆圈表示。（红色虚线垂直于直线，其长度表示到原点的距离。）(b) m=n=2，因此存在唯一解。(c) m=3>n，因此不存在唯一解。我们给出了最小二乘解。</div>

#### 7.7.1 求解正方形系统

当 m=n 时，我们可以通过计算 LU 分解 $\mathbf{A} = \mathbf{L} \mathbf{U}$ 来求解 $\boldsymbol{x}$，然后按如下步骤进行：

$$ \mathbf{A}\boldsymbol{x}=\boldsymbol{b} \tag*{(7.215)}$$

$$ \mathbf{L}\mathbf{U}\mathbf{x}=\mathbf{b} \tag*{(7.216)}$$

$$ \mathbf{U}\mathbf{x}=\mathbf{L}^{-1}\mathbf{b}\triangleq\mathbf{y} \tag*{(7.217)}$$

$$ x=\mathrm{U}^{-1}y \tag*{(7.218)}$$

关键在于 $\mathbf{L}$ 和 $\mathbf{U}$ 均为三角矩阵，因此我们可以避免求矩阵逆，改用一种称为**回代**的方法。

具体地，我们可以通过如下方式不解逆而求得 $y = L^{-1}b$。首先写出：

$$ \begin{pmatrix}L_{11}&&&\\L_{21}&L_{22}&&\\&&\ddots&\\&&&L_{n1}&L_{n2}\quad\cdots\quad L_{nn}\end{pmatrix}\begin{pmatrix}y_{1}\\ \vdots\\ y_{n}\end{pmatrix}=\begin{pmatrix}b_{1}\\ \vdots\\ b_{n}\end{pmatrix} \tag*{(7.219)}$$

我们首先求解 $L_{11}y_{1}=b_{1}$ 得到 $y_{1}$，然后代入求解

$$ L_{21}y_{1}+L_{22}y_{2}=b_{2} \tag*{(7.220)}$$

得到 $y_2$。重复此递归过程。该过程常用反斜杠运算符表示，即 $y = \mathbf{L} \setminus b$。得到 $y$ 后，我们可以通过类似的回代法求解 $x = \mathbf{U}^{-1} y$。

#### 7.7.2 求解欠定系统（最小范数估计）

本节考虑欠定情形，即 $m < n$。我们假设行向量线性无关，因此 $\mathbf{A}$ 满秩。

---

当 $m < n$ 时，存在多个可能的解，其形式为

$$  \{x:\mathbf{A}x=b\}=\{x_{p}+z:z\in\mathrm{nullspace}(\mathbf{A})\}   \tag*{(7.221)}$$

其中 $\pmb{x}_{p}$ 是任意一个特解。通常选择具有最小 $\ell_2$ 范数的特解，即

$$  \hat{x}=\underset{\mathbf{x}}{\operatorname{argmin}}\left|\left|\mathbf{x}\right|\right|_{2}^{2}\text{ s.t. } \mathbf{A}\mathbf{x}=\mathbf{b}   \tag*{(7.222)}$$

我们可以利用右伪逆来计算最小范数解：

$$  \boldsymbol{x}_{\mathrm{pinv}}=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\boldsymbol{b}   \tag*{(7.223)}$$

（更多细节见第 7.5.3 节。）

为证明这一点，假设 $\mathbf{x}$ 是另一个解，因此 $\mathbf{A}\mathbf{x}=\mathbf{b}$，且 $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm{pinv}})=0$。于是

$$  (\boldsymbol{x}-\boldsymbol{x}_{\mathrm{pinv}})^{\top}\boldsymbol{x}_{\mathrm{pinv}}=(\boldsymbol{x}-\boldsymbol{x}_{\mathrm{pinv}})^{\top}\boldsymbol{A}^{\top}(\boldsymbol{A}\boldsymbol{A}^{\top})^{-1}\boldsymbol{b}=(\boldsymbol{A}(\boldsymbol{x}-\boldsymbol{x}_{\mathrm{pinv}}))^{\top}(\boldsymbol{A}\boldsymbol{A}^{\top})^{-1}\boldsymbol{b}=0   \tag*{(7.224)}$$

因此 $(\mathbf{x}-\mathbf{x}_{\mathrm{pinv}}) \perp \mathbf{x}_{\mathrm{pinv}}$。根据毕达哥拉斯定理，$\mathbf{x}$ 的范数为

$$  ||\boldsymbol{x}||^{2}=||\boldsymbol{x}_{\mathrm{pinv}}+\boldsymbol{x}-\boldsymbol{x}_{\mathrm{pinv}}||^{2}=||\boldsymbol{x}_{\mathrm{pinv}}||^{2}+||\boldsymbol{x}-\boldsymbol{x}_{\mathrm{pinv}}||^{2}\geq||\boldsymbol{x}_{\mathrm{pinv}}||^{2}   \tag*{(7.225)}$$

因此，除 $\mathbf{x}_{\mathrm{pinv}}$ 之外的任何解都具有更大的范数。

我们也可以通过最小化以下无约束目标来求解式 (7.222) 中的约束优化问题：

$$  \mathcal{L}(\boldsymbol{x},\boldsymbol{\lambda})=\boldsymbol{x}^{\top}\boldsymbol{x}+\boldsymbol{\lambda}^{\top}(\mathbf{A}\boldsymbol{x}-\boldsymbol{b})   \tag*{(7.226)}$$

根据第 8.5.1 节，最优性条件为

$$  \nabla_{x}\mathcal{L}=2\boldsymbol{x}+\mathbf{A}^{\top}\boldsymbol{\lambda}=\mathbf{0},\quad \nabla_{\boldsymbol{\lambda}}\mathcal{L}=\mathbf{A}\boldsymbol{x}-\boldsymbol{b}=\mathbf{0}   \tag*{(7.227)}$$

由第一个条件可得 $\boldsymbol{x} = -\boldsymbol{A}^{\top}\boldsymbol{\lambda}/2$。代入第二个条件得

$$  \mathbf{A}\boldsymbol{x}=-\frac{1}{2}\mathbf{A}\mathbf{A}^{\top}\boldsymbol{\lambda}=\boldsymbol{b}   \tag*{(7.228)}$$

这意味着 $\boldsymbol{\lambda} = -2(\mathbf{A}\mathbf{A}^{\top})^{-1}\boldsymbol{b}$。因此 $\boldsymbol{x} = \mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\boldsymbol{b}$，即右伪逆解。

#### 7.7.3 求解过约束系统（最小二乘估计）

若 $m > n$，则得到超定系统，通常不存在精确解，但我们会尝试寻找尽可能接近满足 $\mathbf{A}\mathbf{x} = \mathbf{b}$ 所有约束的解。这可以通过最小化以下代价函数（称为最小二乘目标）来实现⁴。

$$  f(\boldsymbol{x})=\frac{1}{2}||\boldsymbol{A}\boldsymbol{x}-\boldsymbol{b}||_{2}^{2}   \tag*{(7.233)}$$

---

使用第7.8节的矩阵微积分结果，梯度由下式给出

$$  \boldsymbol{g}(\boldsymbol{x})=\frac{\partial}{\partial\boldsymbol{x}}\boldsymbol{f}(\boldsymbol{x})=\boldsymbol{A}^{\top}\boldsymbol{A}\boldsymbol{x}-\boldsymbol{A}^{\top}\boldsymbol{b}   \tag*{(7.234)}$$

最优解可通过求解 $ \boldsymbol{g}(\boldsymbol{x})=\boldsymbol{0} $ 得到。这给出

$$  \mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\mathbf{A}^{\top}\mathbf{b}   \tag*{(7.235)}$$

这些方程被称为正规方程，因为在最优解处，$ \mathbf{b} - \mathbf{A}\mathbf{x} $ 与 $ \mathbf{A} $ 的值域正交（垂直），我们将在第11.2.2.2节中解释。对应的解 $ \hat{\mathbf{x}} $ 是普通最小二乘（OLS）解，由下式给出

$$  \hat{\boldsymbol{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\boldsymbol{b}   \tag*{(7.236)}$$

量 $ \mathbf{A}^\dagger = (\mathbf{A}^\top \mathbf{A})^{-1} \mathbf{A}^\top $ 是（非方阵）矩阵 $ \mathbf{A} $ 的左伪逆（详见第7.5.3节）。

我们可以通过证明海森矩阵正定来验证解的唯一性。此时，海森矩阵由下式给出

$$  \mathbf{H}(\boldsymbol{x})=\frac{\partial^{2}}{\partial\boldsymbol{x}^{2}}f(\boldsymbol{x})=\mathbf{A}^{\top}\mathbf{A}   \tag*{(7.237)}$$

如果 $ \mathbf{A} $ 是满秩的（即 $ \mathbf{A} $ 的列线性无关），则 $ \mathbf{H} $ 是正定的，因为对于任意 $ \mathbf{v} > \mathbf{0} $，有

$$  \boldsymbol{v}^{\mathrm{T}}(\mathbf{A}^{\mathrm{T}}\mathbf{A})\boldsymbol{v}=(\mathbf{A}\boldsymbol{v})^{\mathrm{T}}(\mathbf{A}\boldsymbol{v})=||\mathbf{A}\boldsymbol{v}||^{2}>0   \tag*{(7.238)}$$

因此在满秩情况下，最小二乘目标函数有唯一的全局最小值。

### 7.8 矩阵微积分

微积分的研究主题是当我们改变函数输入时，函数“变化率”的计算。它对机器学习以及几乎所有其他数值学科都至关重要。本节中，我们回顾一些标准结果。在某些情况下，我们使用第7章中介绍的一些矩阵代数概念和符号。关于这些结果在深度学习视角下的更多细节，请参见[PH18]。

#### 7.8.1 导数

考虑一个标量自变量函数 $ f : \mathbb{R} \to \mathbb{R} $。我们在点 $ x $ 处将其导数定义为量

$$  f^{\prime}(x)\triangleq\lim_{h\to0}\frac{f(x+h)-f(x)}{h}   \tag*{(7.239)}$$

假设该极限存在。这衡量了当我们在输入空间中从x移动一小段距离时，输出变化的快慢（即函数的“变化率”）。我们可以将 $ f'(x) $ 解释为 $ f(x) $ 处切线的斜率，因此有

$$  f(x+h)\approx f(x)+f^{\prime}(x)h   \tag*{(7.240)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND许可协议。

---

对于较小的 h。

我们可以使用有限步长 h 来计算导数的有限差分近似，如下所示：

$$  f^{\prime}(x)\equiv\underbrace{\lim_{h\to0}\frac{f(x+h)-f(x)}{h}}_{forward difference}=\underbrace{\lim_{h\to0}\frac{f(x+h/2)-f(x-h/2)}{h}}_{central difference}=\underbrace{\lim_{h\to0}\frac{f(x)-f(x-h)}{h}}_{backward difference}   \tag*{(7.241)}$$

步长 h 越小，估计值越精确，但若 h 过小，则可能因数值抵消而导致误差。

我们可以将微分视为一个将函数映射到函数的算子，$ D(f) = f' $，其中 $ f'(x) $ 计算在 $ x $ 处的导数（假设该点导数存在）。使用撇号符号 $ f' $ 表示导数称为拉格朗日记号。二阶导数函数（衡量梯度变化快慢）记为 $ f'' $。第 $ n' $ 阶导数函数记为 $ f^{(n)} $。

或者，我们可以使用 $ \mathbf{Leibniz} $ 记号，其中函数记为 $ y = f(x) $，其导数记为 $ \frac{dy}{dx} $ 或 $ \frac{d}{dx}f(x) $。要表示在点 $ a $ 处的导数值，我们写作 $ \left.\frac{df}{dx}\right|_{x=a} $。

#### 7.8.2 梯度

我们可以将导数的概念推广到向量参数函数 $ f : \mathbb{R}^n \to \mathbb{R} $，通过定义 $ f $ 关于 $ x_i $ 的偏导数为

$$  \frac{\partial f}{\partial x_{i}}=\lim_{h\to0}\frac{f(\boldsymbol{x}+h\boldsymbol{e}_{i})-f(\boldsymbol{x})}{h}   \tag*{(7.242)}$$

其中 $ e_i $ 是第 $ i' $ 个单位向量。

函数在点 x 处的梯度是其偏导数组成的向量：

$$  \boldsymbol{g}=\frac{\partial f}{\partial\boldsymbol{x}}=\nabla f=\begin{pmatrix}\frac{\partial f}{\partial x_{1}}\\ \vdots\\ \frac{\partial f}{\partial x_{n}}\end{pmatrix}   \tag*{(7.243)}$$

为强调梯度在何处求值，我们可以写为

$$  g(x^{*})\triangleq\left.\frac{\partial f}{\partial x}\right|_{x^{*}}   \tag*{(7.244)}$$

我们看到算子 $ \nabla $（读作“nabla”）将函数 $ f : \mathbb{R}^n \to \mathbb{R} $ 映射为另一个函数 $ g : \mathbb{R}^n \to \mathbb{R}^n $。由于 $ g() $ 是向量值函数，它被称为向量场。相比之下，导数函数 $ f' $ 是一个标量场。

#### 7.8.3 方向导数

方向导数衡量函数 $ f : \mathbb{R}^n \to \mathbb{R} $ 沿空间方向 $ v $ 的变化程度。其定义如下

$$  D_{v}f(\boldsymbol{x})=\lim_{h\to0}\frac{f(\boldsymbol{x}+h\boldsymbol{v})-f(\boldsymbol{x})}{h}   \tag*{(7.245)}$$