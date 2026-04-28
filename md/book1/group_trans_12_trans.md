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

<div style="text-align: center;"><img src="imgs/img_in_image_box_263_129_481_317.jpg" alt="图像" width="18%" /></div>

<div style="text-align: center;">(a) 周期核。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_698_130_916_314.jpg" alt="图像" width="18%" /></div>

<div style="text-align: center;">(b) 余弦核。</div>

<div style="text-align: center;">图17.3：使用不同平稳周期核从高斯过程中采样的函数。由 gpKernelPlot.ipynb 生成。</div>

对于 $ \nu \in \{\frac{1}{2}, \frac{3}{2}, \frac{5}{2}\} $ 的值，该函数简化为：

$$  \mathcal{K}(r;\frac{1}{2},\ell)=\exp(-\frac{r}{\ell})   \tag*{(17.11)}$$

$$  \mathcal{K}(r;\frac{3}{2},\ell)=\left(1+\frac{\sqrt{3}r}{\ell}\right)\exp\left(-\frac{\sqrt{3}r}{\ell}\right)   \tag*{(17.12)}$$

$$  \mathcal{K}(r;\frac{5}{2},\ell)=\left(1+\frac{\sqrt{5}r}{\ell}+\frac{5r^{2}}{3\ell^{2}}\right)\exp\left(-\frac{\sqrt{5}r}{\ell}\right)   \tag*{(17.13)}$$

$ \nu = \frac{1}{2} $ 对应 Ornstein-Uhlenbeck 过程，该过程描述了布朗运动中粒子的速度。相应的函数连续但不可微，因此非常“参差不齐”。参见图17.2b的示意图。

##### 周期核

周期核捕捉重复结构，其形式为

$$  \mathcal{K}_{\mathrm{p e r}}(r;\ell,p)=\exp\left(-\frac{2}{\ell^{2}}\sin^{2}(\pi\frac{r}{p})\right)   \tag*{(17.14)}$$

其中 $p$ 是周期。参见图17.3a的示意图。

一个相关的核是余弦核：

$$  \mathcal{K}(r;p)=\cos\left(2\pi\frac{r}{p}\right)   \tag*{(17.15)}$$

参见图17.3b的示意图。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

##### 17.1.2.2 由旧核构造新核

给定两个有效核 $\mathcal{K}_1(\boldsymbol{x}, \boldsymbol{x}')$ 和 $\mathcal{K}_2(\boldsymbol{x}, \boldsymbol{x}')$，我们可以通过以下任意方法构造一个新核：

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=c\mathcal{K}_{1}(\boldsymbol{x},\boldsymbol{x}^{\prime}),\quad \text{对于任意常数 } c > 0 \tag*{(17.16)}$$

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=f(\boldsymbol{x})\mathcal{K}_{1}(\boldsymbol{x},\boldsymbol{x}^{\prime})f(\boldsymbol{x}^{\prime}),\quad \text{对于任意函数 } f \tag*{(17.17)}$$

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=q(\mathcal{K}_{1}(\boldsymbol{x},\boldsymbol{x}^{\prime})),\quad \text{对于任意非负系数多项式函数 } q \tag*{(17.18)}$$

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=\exp(\mathcal{K}_{1}(\boldsymbol{x},\boldsymbol{x}^{\prime})) \tag*{(17.19)}$$

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}^{\prime},\quad \text{对于任意半正定矩阵 } \mathbf{A} \tag*{(17.20)}$$

例如，假设我们从线性核 $\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = \boldsymbol{x}^\top \boldsymbol{x}'$ 开始。我们知道这是一个有效的 Mercer 核，因为相应的 Gram 矩阵就是数据的（缩放后的）协方差矩阵。根据上述规则，我们可以看出多项式核 $\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = (\boldsymbol{x}^\top \boldsymbol{x}')^M$ 是一个有效的 Mercer 核。它包含了所有 $M$ 阶单项式。例如，如果 $M = 2$ 且输入是二维的，我们有

$$ (\boldsymbol{x}^{\top}\boldsymbol{x}^{\prime})^{2}=(x_{1}x_{1}^{\prime}+x_{2}x_{2}^{\prime})^{2}=(x_{1}x_{1}^{\prime})^{2}+(x_{2}x_{2})^{2}+2(x_{1}x_{1}^{\prime})(x_{2}x_{2}^{\prime}) \tag*{(17.21)}$$

我们可以通过使用核 $\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = (\boldsymbol{x}^\top \boldsymbol{x}' + c)^M$ 将其推广到包含所有不超过 $M$ 阶的项。例如，如果 $M = 2$ 且输入是二维的，我们有

$$ \begin{aligned}(\boldsymbol{x}^{\top}\boldsymbol{x}^{\prime}+1)^{2}&=(x_{1}x_{1}^{\prime})^{2}+(x_{1}x_{1}^{\prime})(x_{2}x_{2}^{\prime})+(x_{1}x_{1}^{\prime})\\&+(x_{2}x_{2})(x_{1}x_{1}^{\prime})+(x_{2}x_{2}^{\prime})^{2}+(x_{2}x_{2}^{\prime})\\&+(x_{1}x_{1}^{\prime})+(x_{2}x_{2}^{\prime})+1\end{aligned} \tag*{(17.22)}$$

我们也可以利用上述规则来证明高斯核是一个有效核。为此，注意到

$$ \left|\boldsymbol{x}-\boldsymbol{x}^{\prime}\right|^{2}=\boldsymbol{x}^{\top}\boldsymbol{x}+(\boldsymbol{x}^{\prime})^{\top}\boldsymbol{x}^{\prime}-2\boldsymbol{x}^{\top}\boldsymbol{x}^{\prime} \tag*{(17.23)}$$

因此

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=\exp(-||\boldsymbol{x}-\boldsymbol{x}^{\prime}||^{2}/2\sigma^{2})=\exp(-\boldsymbol{x}^{\top}\boldsymbol{x}/2\sigma^{2})\exp(\boldsymbol{x}^{\top}\boldsymbol{x}^{\prime}/\sigma^{2})\exp(-(\boldsymbol{x}^{\prime})^{\top}\boldsymbol{x}^{\prime}/2\sigma^{2}) \tag*{(17.24)}$$

是一个有效核。

##### 17.1.2.3 通过加法和乘法组合核

我们还可以通过加法或乘法来组合核：

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=\mathcal{K}_{1}(\boldsymbol{x},\boldsymbol{x}^{\prime})+\mathcal{K}_{2}(\boldsymbol{x},\boldsymbol{x}^{\prime}) \tag*{(17.25)}$$

$$ \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=\mathcal{K}_{1}(\boldsymbol{x},\boldsymbol{x}^{\prime})\times\mathcal{K}_{2}(\boldsymbol{x},\boldsymbol{x}^{\prime}) \tag*{(17.26)}$$

将两个正定核相乘总会得到另一个正定核。这是获取每个核各自属性的合取的一种方式，如图 17.4 所示。

此外，将两个正定核相加总会得到另一个正定核。这是获取每个核各自属性的析取的一种方式，如图 17.5 所示。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_271_130_873_399.jpg" alt="Image" width="52%" /></div>

<div style="text-align: center;">图 17.4：通过对基本核进行相乘得到的一维结构示例。第一行显示 $ \mathcal{K}(x, x' = 1) $。第二行显示从 $ GP(f|0, \mathcal{K}) $ 中采样的一些函数。摘自 [Duv14] 的图 2.2，经 David Duvenaud 友好许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_264_538_885_799.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">图 17.5：通过对基本核进行相加得到的一维结构示例。此处 SE $ ^{\text{(short)}} $ 和 SE $ ^{\text{(long)}} $ 是两个具有不同长度尺度的 SE 核。摘自 [Duv14] 的图 2.4，经 David Duvenaud 友好许可使用。</div>

##### 17.1.2.4 用于结构化输入的核

当输入是结构化对象（如字符串和图）时，核特别有用，因为通常很难对可变大小的输入进行“特征化”。例如，我们可以定义一个字符串核，该核根据两个字符串共同拥有的 n-gram 数量来比较它们 $ [Lod+02; BC17] $。

我们还可以定义图上的核 [KJM19]。例如，随机游走核概念上同时在两个图上执行随机游走，然后统计两次游走产生路径的数量。如 [Vis+10] 所讨论，这可以高效计算。关于图核的更多细节，请参见 [KJM19]。

关于结构化对象核的综述，可参见例如 [Gär03]。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_399_138_770_375.jpg" alt="图17.6" width="32%" /></div>


<div style="text-align: center;">图17.6: 针对2个训练点 $ \mathbf{x}_1 $ 和 $ \mathbf{x}_2 $ 以及1个测试点 $ \mathbf{x}_* $ 的高斯过程，表示为图形模型，代表 $ p(\mathbf{y}, \mathbf{f}_X | \mathbf{X}) = \mathcal{N}(\mathbf{f}_X | m(\mathbf{X}), \mathcal{K}(\mathbf{X})) \prod_i p(y_i | f_i) $。隐藏节点 $ f_i = f(\mathbf{x}_i) $ 表示每个数据点处的函数值。这些隐藏节点通过无向边完全连接，形成高斯图形模型；边的强度表示协方差项 $ \Sigma_{ij} = \mathcal{K}(\mathbf{x}_i, \mathbf{x}_j) $。如果测试点 $ \mathbf{x}_* $ 与训练点 $ \mathbf{x}_1 $ 和 $ \mathbf{x}_2 $ 相似，那么隐藏函数 $ f_* $ 的值将与 $ f_1 $ 和 $ f_2 $ 相似，因此预测输出 $ y_* $ 将与训练值 $ y_1 $ 和 $ y_2 $ 相似。</div>


### 17.2 高斯过程

本节我们讨论高斯过程，这是一种定义形如 $ f : \mathcal{X} \to \mathbb{R} $（其中 $ \mathcal{X} $ 为任意域）的函数上分布的方法。核心假设是：在一组 $ M > 0 $ 个输入点上的函数值 $ \boldsymbol{f} = [f(\boldsymbol{x}_1), \ldots, f(\boldsymbol{x}_M)] $ 服从联合高斯分布，其均值为 $ (\boldsymbol{\mu} = m(\boldsymbol{x}_1), \ldots, m(\boldsymbol{x}_M)) $，协方差为 $ \boldsymbol{\Sigma}_{ij} = \mathcal{K}(\boldsymbol{x}_i, \boldsymbol{x}_j) $，其中 $ m $ 是均值函数，$ \mathcal{K} $ 是正定（Mercer）核。由于我们假设这对任意 $ M > 0 $ 都成立，因此包括 $ M = N + 1 $ 的情况，即包含 $ N $ 个训练点 $ \boldsymbol{x}_n $ 和 1 个测试点 $ \boldsymbol{x}_* $。这样，我们就可以通过操纵联合高斯分布 $ p(f(\boldsymbol{x}_1), \ldots, f(\boldsymbol{x}_N), f(\boldsymbol{x}_*)) $ 从已知的 $ f(\boldsymbol{x}_1), \ldots, f(\boldsymbol{x}_n) $ 推断出 $ f(\boldsymbol{x}_*) $，具体如下所述。我们还可以将其扩展到观测到 $ f(\boldsymbol{x}_n) $ 的带噪声函数的情况，例如回归或分类问题。

#### 17.2.1 无噪声观测

假设我们观测到一个训练集 $ \mathcal{D} = \{(\boldsymbol{x}_n, y_n) : n = 1 : N\} $，其中 $ y_n = f(\boldsymbol{x}_n) $ 是在 $ \boldsymbol{x}_n $ 处评估函数的无噪声观测值。如果我们要求高斯过程预测它已经见过的 $ \boldsymbol{x} $ 值处的 $ f(\boldsymbol{x}) $，我们希望高斯过程以零不确定性返回答案 $ f(\boldsymbol{x}) $。换句话说，它应该充当训练数据的插值器。

现在考虑对可能不在 $ \mathcal{D} $ 中的新输入预测输出的情况。具体来说，给定一个大小为 $ N_*\times D $ 的测试集 $ \mathbf{X}_* $，我们想要预测函数输出 $ \mathbf{f}_*=[f(\mathbf{x}_{*1}),\ldots,f(\mathbf{x}_{*N_*})] $。根据高斯过程的定义，联合分布 $ p(\mathbf{f}_X,\mathbf{f}_*|\mathbf{X},\mathbf{X}_*) $ 具有以下形式：

$$  \begin{pmatrix}\boldsymbol{f}_{X}\\ \boldsymbol{f}_{*}\end{pmatrix}\sim\mathcal{N}\left(\begin{pmatrix}\boldsymbol{\mu}_{X}\\ \boldsymbol{\mu}_{*}\end{pmatrix},\begin{pmatrix}\mathbf{K}_{X,X}&\mathbf{K}_{X,*}\\ \mathbf{K}_{X,*}^{\top}&\mathbf{K}_{*,*}\end{pmatrix}\right)   \tag*{(17.27)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_243_141_515_325.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_664_132_907_328.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_255_383_501_576.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_655_385_907_577.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 17.7: (a) 从具有平方指数核的高斯过程先验中采样的若干函数。(b-d) 在条件化于 1、2 和 4 个无噪声观测后，从高斯过程后验中采样的若干样本。阴影区域表示 $ \mathbb{E}\left[f(\mathbf{x})\right] \pm 2\mathrm{std}\left[f(\mathbf{x})\right] $。改编自 [RW06] 的图 2.2。由 gprDemoNoiseFree.ipymb 生成。</div>


其中 $ \boldsymbol{\mu}_{X} = [m(\boldsymbol{x}_{1}), \ldots, m(\boldsymbol{x}_{N})] $, $ \boldsymbol{\mu}_{*} = [m(\boldsymbol{x}_{1}^{*}), \ldots, m(\boldsymbol{x}_{N_{*}}^{*})] $, $ \mathbf{K}_{X,X} = \mathcal{K}(\mathbf{X}, \mathbf{X}) $ 是 $ N \times N $ 矩阵, $ \mathbf{K}_{X,*} = \mathcal{K}(\mathbf{X}, \mathbf{X}_{*}) $ 是 $ N \times N_{*} $ 矩阵, $ \mathbf{K}_{*,*} = \mathcal{K}(\mathbf{X}_{*}, \mathbf{X}_{*}) $ 是 $ N_{*} \times N_{*} $ 矩阵。见图 17.6 的示意图。根据高斯条件分布的标准规则（第 3.2.3 节），后验具有如下形式

$$  p(f_{*}|\mathbf{X}_{*},\mathcal{D})=\mathcal{N}(f_{*}|\boldsymbol{\mu}_{*},\boldsymbol{\Sigma}_{*})   \tag*{(17.28)}$$

$$  \boldsymbol{\mu}_{*}=m(\mathbf{X}_{*})+\mathbf{K}_{X,*}^{\top}\mathbf{K}_{X,X}^{-1}(\boldsymbol{f}_{X}-m(\mathbf{X}))   \tag*{(17.29)}$$

$$  \mathbf{\Sigma}_{*}=\mathbf{K}_{*,*}-\mathbf{K}_{X,*}^{\intercal}\mathbf{K}_{X,X}^{-1}\mathbf{K}_{X,*}   \tag*{(17.30)}$$

该过程在图 17.7 中得到了说明。左侧展示的是从先验 $ p(f) $ 中采样的若干样本，其中使用了 RBF 核（第 17.1 节）和零均值函数。右侧展示的是从后验 $ p(f|\mathcal{D}) $ 中采样的样本。可以看出，模型完美地插值了训练数据，并且随着我们远离观测数据，预测的不确定性逐渐增大。

#### 17.2.2 含噪声观测

现在考虑我们观测到的是底层函数的含噪版本的情况：$ y_n = f(\boldsymbol{x}_n) + \epsilon_n $，其中 $ \epsilon_n \sim \mathcal{N}(0, \sigma_y^2) $。在这种情况下，模型不需要对数据进行插值。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

但它必须“接近”观测数据。观测到的含噪声响应的协方差为

$$  \mathrm{Cov}\left[y_{i},y_{j}\right]=\mathrm{Cov}\left[f_{i},f_{j}\right]+\mathrm{Cov}\left[\epsilon_{i},\epsilon_{j}\right]=\mathcal{K}(\boldsymbol{x}_{i},\boldsymbol{x}_{j})+\sigma_{y}^{2}\delta_{ij}   \tag*{(17.31)}$$

其中 $ \delta_{ij} = \mathbb{I}(i = j) $。换句话说

$$  \mathrm{C o v}\left[\mathbf{y}|\mathbf{X}\right]=\mathbf{K}_{X,X}+\sigma_{y}^{2}\mathbf{I}_{N}\triangleq\mathbf{K}_{\sigma}   \tag*{(17.32)}$$

观测数据与测试点上的潜在无噪声函数的联合密度由下式给出

$$  \begin{pmatrix}\boldsymbol{y}\\ \boldsymbol{f}_{*}\end{pmatrix}\sim\mathcal{N}\left(\begin{pmatrix}\boldsymbol{\mu}_{X}\\ \boldsymbol{\mu}_{*}\end{pmatrix},\begin{pmatrix}\mathbf{K}_{\sigma}&\mathbf{K}_{X,*}\\ \mathbf{K}_{X,*}^{\top}&\mathbf{K}_{*,*}\end{pmatrix}\right)   \tag*{(17.33)}$$

因此，在测试点集 $ X_{*} $ 上的后验预测密度为

$$  p(f_{*}|\mathcal{D},\mathbf{X}_{*})=\mathcal{N}(f_{*}|\boldsymbol{\mu}_{*|X},\boldsymbol{\Sigma}_{*|X})   \tag*{(17.34)}$$

$$  \boldsymbol{\mu}_{*|X}=\boldsymbol{\mu}_{*}+\mathbf{K}_{X,*}^{\top}\mathbf{K}_{\sigma}^{-1}(\boldsymbol{y}-\boldsymbol{\mu}_{X})   \tag*{(17.35)}$$

$$  \mathbf{\Sigma}_{*|X}=\mathbf{K}_{*,*}-\mathbf{K}_{X,*}^{\top}\mathbf{K}_{\sigma}^{-1}\mathbf{K}_{X,*}   \tag*{(17.36)}$$

对于单个测试输入的情况，可简化为

$$  p(f_{*}|\mathcal{D},\boldsymbol{x}_{*})=\mathcal{N}(f_{*}|m_{*}+\boldsymbol{k}_{*}^{\top}\mathbf{K}_{\sigma}^{-1}(\boldsymbol{y}-\boldsymbol{\mu}_{X}),\;k_{**}-\boldsymbol{k}_{*}^{\top}\mathbf{K}_{\sigma}^{-1}\boldsymbol{k}_{*})   \tag*{(17.37)}$$

其中 $ \boldsymbol{k}_* = [\mathcal{K}(\boldsymbol{x}_*, \boldsymbol{x}_1), \ldots, \mathcal{K}(\boldsymbol{x}_*, \boldsymbol{x}_N)] $，$ k_{**} = \mathcal{K}(\boldsymbol{x}_*, \boldsymbol{x}_*) $。若均值函数为零，则后验均值可写为

$$  \mu_{*|X}=\boldsymbol{k}_{*}^{\mathsf{T}}(\mathbf{K}_{\sigma}^{-1}\boldsymbol{y})\triangleq\boldsymbol{k}_{*}^{\mathsf{T}}\boldsymbol{\alpha}=\sum_{n=1}^{N}\mathcal{K}(\boldsymbol{x}_{*},\boldsymbol{x}_{n})\boldsymbol{\alpha}_{n}   \tag*{(17.38)}$$

这与式(17.108)中核岭回归的预测相同。

#### 17.2.3 与核回归的比较

在第16.3.5节中，我们讨论了核回归，这是一种生成式回归方法，利用核密度估计来近似 $ p(y, \boldsymbol{x}) $。具体地，式(16.39)给出

$$  \mathbb{E}\left[y|\boldsymbol{x},\mathcal{D}\right]=\frac{\sum_{n=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})y_{n}}{\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})}=\sum_{n=1}^{N}y_{n}w_{n}(\boldsymbol{x})   \tag*{(17.39)}$$

$$  w_{n}(\boldsymbol{x})\triangleq\frac{\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})}{\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})}   \tag*{(17.40)}$$

这与式(17.38)非常相似。然而，存在一些重要区别。首先，在高斯过程（GP）中，我们使用正定（Mercer）核而非密度核；Mercer核可以定义在结构化对象上，如字符串和图，而对于密度核来说这更难做到。

---

其次，GP 是一种插值器（至少在 \(\sigma^2 = 0\) 时如此），因此 \(\mathbb{E}[y|\boldsymbol{x}_n, \mathcal{D}] = y_n\)。相比之下，核回归不是插值器（尽管可以通过迭代拟合残差使其成为插值器，如 [KJ16] 所述）。第三，GP 是一种贝叶斯方法，这意味着我们可以通过最大化边际似然来估计（核的）超参数；相比之下，在核回归中，我们必须使用交叉验证来估计核参数（如带宽）。第四，计算核回归的权重 \(w_n\) 需要 \(O(N)\) 时间，其中 \(N = |\mathcal{D}|\)，而计算 GP 回归的权重 \(\alpha_n\) 需要 \(O(N^3)\) 时间（尽管存在近似方法可以将其降至 \(O(NM^2)\)，如我们在第 17.2.9 节中所讨论的）。

#### 17.2.4 权重空间 vs 函数空间

在本节中，我们展示贝叶斯线性回归是 GP 的一个特例。

考虑线性回归模型 \(y = f(\boldsymbol{x}) + \epsilon\)，其中 \(f(\boldsymbol{x}) = \boldsymbol{w}^\top \phi(\boldsymbol{x})\) 且 \(\epsilon \sim \mathcal{N}(0, \sigma_y^2)\)。如果我们使用高斯先验 \(p(\boldsymbol{w}) = \mathcal{N}(\boldsymbol{w} | \boldsymbol{0}, \boldsymbol{\Sigma}_w)\)，则后验如下（推导见第 11.7.2 节）：

$$ p(\boldsymbol{w}|\mathcal{D})=\mathcal{N}(\boldsymbol{w}|\frac{1}{\sigma_{y}^{2}}\mathbf{A}^{-1}\boldsymbol{\Phi}^{T}\boldsymbol{y},\mathbf{A}^{-1}) \tag*{(17.41)}$$

其中 \(\Phi\) 是 \(N \times D\) 设计矩阵，且

$$ \mathbf{A}=\sigma_{y}^{-2}\boldsymbol{\Phi}^{\mathsf{T}}\boldsymbol{\Phi}+\boldsymbol{\Sigma}_{w}^{-1} \tag*{(17.42)}$$

因此，\(f_{*} = f(\boldsymbol{x}_{*})\) 的后验预测分布为

$$ p(f_{*}|\mathcal{D},\boldsymbol{x}_{*})=\mathcal{N}(f_{*}|\frac{1}{\sigma_{y}^{2}}\boldsymbol{\phi}_{*}^{\mathsf{T}}\mathbf{A}^{-1}\boldsymbol{\Phi}^{\mathsf{T}}\boldsymbol{y},\boldsymbol{\phi}_{*}^{\mathsf{T}}\mathbf{A}^{-1}\boldsymbol{\phi}_{*}) \tag*{(17.43)}$$

其中 \(\phi_{*}=\phi(\boldsymbol{x}_{*})\)。这是从权重空间的角度来看待推理和预测问题。

我们现在证明这等价于使用形如 \(\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = \phi(\boldsymbol{x})^\top \boldsymbol{\Sigma}_w \phi(\boldsymbol{x}')\) 的核的 GP 所做的预测。为说明这一点，令 \(\mathbf{K} = \boldsymbol{\Phi} \boldsymbol{\Sigma}_w \boldsymbol{\Phi}^\top\)，\(\boldsymbol{k}_* = \boldsymbol{\Phi} \boldsymbol{\Sigma}_w \boldsymbol{\phi}_*\)，且 \(k_{**} = \phi_*^\top \boldsymbol{\Sigma}_w \boldsymbol{\phi}_*\)。利用这一记号和矩阵求逆引理，我们可以将方程 (17.43) 重写如下：

$$ p(f_{*}|\mathcal{D},\pmb{x}_{*})=\mathcal{N}(f_{*}|\pmb{\mu}_{*|X},\pmb{\Sigma}_{*|X}) \tag*{(17.44)}$$

$$ \boldsymbol{\mu}_{*|X}=\boldsymbol{\phi}_{*}^{\top}\boldsymbol{\Sigma}_{w}\boldsymbol{\Phi}^{\top}(\mathbf{K}+\sigma_{y}^{2}\mathbf{I})^{-1}\boldsymbol{y}=\boldsymbol{k}_{*}^{\top}\mathbf{K}_{\sigma}^{-1}\boldsymbol{y} \tag*{(17.45)}$$

$$ \mathbf{\Sigma}_{*|X}=\boldsymbol{\phi}_{*}^{\intercal}\mathbf{\Sigma}_{w}\boldsymbol{\phi}_{*}-\boldsymbol{\phi}_{*}^{\intercal}\mathbf{\Sigma}_{w}\mathbf{\Phi}^{\intercal}(\mathbf{K}+\sigma_{y}^{2}\mathbf{I})^{-1}\mathbf{\Phi}\mathbf{\Sigma}_{w}\boldsymbol{\phi}_{*}=k_{**}-\boldsymbol{k}_{*}^{\intercal}\mathbf{K}_{\sigma}^{-1}\boldsymbol{k}_{*} \tag*{(17.46)}$$

这与方程 (17.37) 中的结果一致，假设 \(m(\boldsymbol{x}) = 0\)。（非零均值可以通过在 \(\phi(\boldsymbol{x})\) 中添加一个值为 1 的常特征来捕获。）

因此，我们可以从贝叶斯线性回归导出 GP。然而，请注意，线性回归假设 \(\phi(\boldsymbol{x})\) 是有限长度向量，而 GP 允许我们直接基于核来工作，这可能对应于无限长度的特征向量（见第 17.1.1 节）。也就是说，GP 在函数空间中工作。

#### 17.2.5 数值问题

在本节中，我们讨论实现上述方程时出现的计算和数值问题。为简化记号，我们假设先验均值为零，即 \(m(\boldsymbol{x}) = 0\)。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_201_126_562_366.jpg" alt="图像" width="31%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_608_127_968_366.jpg" alt="图像" width="31%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图17.8：使用SE（平方指数）核但不同超参数的高斯过程拟合20个带噪声观测值的一维示例。超参数（ $ \ell $,  $ \sigma_f $,  $ \sigma_y $）如下：(a)  $ (1,1,0.1) $ (b)  $ (3.0, 1.16, 0.89) $。改编自[RW06]的图2.5。由gprDemoChangeHparams.ipynb生成。</div>

后验预测均值由 $ \mu_*\mathbf{k}_*\mathbf{K}_\sigma^{-1}\mathbf{y} $ 给出。出于数值稳定性的原因，直接求 $ \mathbf{K}_\sigma $ 的逆是不明智的。一种更稳健的替代方法是计算Cholesky分解 $ \mathbf{K}_\sigma = \mathbf{L}\mathbf{L}^\top $，这需要 $ O(N^3) $ 的时间。然后计算 $ \mathbf{\alpha} = \mathbf{L}^\top \setminus (\mathbf{L} \setminus \mathbf{y}) $，其中我们使用反斜杠运算符表示回代（第7.7.1节）。由此，对于每个测试用例，我们可以在 $ O(N) $ 时间内计算后验均值：

$$  \boldsymbol{\mu}_{*}=\boldsymbol{k}_{*}^{\top}\mathbf{K}_{\sigma}^{-1}\boldsymbol{y}=\boldsymbol{k}_{*}^{\top}\mathbf{L}^{-\top}(\mathbf{L}^{-1}\boldsymbol{y})=\boldsymbol{k}_{*}^{\top}\boldsymbol{\alpha}   \tag*{(17.47)}$$

对于每个测试用例，我们可以用以下公式在 $ O(N^{2}) $ 时间内计算方差：

$$  \sigma_{*}^{2}=k_{**}-k_{*}^{\top}\mathbf{L}^{-T}\mathbf{L}^{-1}k_{*}=k_{**}-v^{\top}v   \tag*{(17.48)}$$

其中 v = L \ k*。

最后，对数边际似然（用于核学习，第17.2.6节）可以用以下公式计算：

$$  \log p(\boldsymbol{y}|\mathbf{X})=-\frac{1}{2}\boldsymbol{y}^{\top}\boldsymbol{\alpha}-\sum_{n=1}^{N}\log L_{n n}-\frac{N}{2}\log(2\pi)   \tag*{(17.49)}$$

#### 17.2.6 估计核函数

大多数核都有一些自由参数，这些参数对模型的预测有很大影响。例如，假设我们使用具有如下形式RBF（径向基函数）核的高斯过程进行一维回归：

$$  \mathcal{K}(x_{p},x_{q})=\sigma_{f}^{2}\exp(-\frac{1}{2\ell^{2}}(x_{p}-x_{q})^{2})   \tag*{(17.50)}$$

这里 $ \ell $ 是函数变化的水平尺度， $ \sigma_{f}^{2} $ 控制函数的垂直尺度。我们假设观测噪声方差为 $ \sigma_{y}^{2} $。

---

We sampled 20 observations from an MVN with a covariance given by  $ \mathbf{\Sigma} = \mathcal{K}(x_i, x_j) $ for a grid of points  $ \{x_i\} $, and added observation noise of value  $ \sigma_y $. We then fit this data using a GP with the same kernel, but with a range of hyperparrameters. Figure 17.8 illustrates the effects of changing these parameters. In Figure 17.8(a), we use  $ (\ell, \sigma_f, \sigma_y) = (1, 1, 0.1) $, and the result is a good fit. In Figure 17.8(b), we increase the length scale to  $ \ell = 3 $; now the function looks overly smooth.

##### 17.2.6.1 Empirical Bayes

To estimate the kernel parameters  $ \theta $ (sometimes called hyperparameters), we could use exhaustive search over a discrete grid of values, with validation loss as an objective, but this can be quite slow. (This is the approach used by nonprobabilistic methods, such as SVMs (Section 17.3) to tune kernels.) Here we consider an empirical Bayes approach (Section 4.6.5.3), which will allow us to use gradient-based optimization methods, which are much faster. In particular, we will maximize the marginal likelihood

$$  p(\boldsymbol{y}|\mathbf{X},\boldsymbol{\theta})=\int p(\boldsymbol{y}|\boldsymbol{f},\mathbf{X})p(\boldsymbol{f}|\mathbf{X},\boldsymbol{\theta})d\boldsymbol{f}   \tag*{(17.51)}$$

(The reason it is called the marginal likelihood, rather than just likelihood, is because we have marginalized out the latent Gaussian vector  $ \mathbf{f} $.)

For notational simplicity, we assume the mean function is 0. Since  $ p(f|\mathbf{X}) = \mathcal{N}(f|\mathbf{0}, \mathbf{K}) $, and  $ p(y|\mathbf{f}) = \prod_{n=1}^{N} \mathcal{N}(y_n | f_n, \sigma_y^2) $, the marginal likelihood is given by

$$  \log p(\boldsymbol{y}|\mathbf{X},\boldsymbol{\theta})=\log\mathcal{N}(\boldsymbol{y}|\mathbf{0},\mathbf{K}_{\sigma})=-\frac{1}{2}\boldsymbol{y}^{\top}\mathbf{K}_{\sigma}^{-1}\boldsymbol{y}-\frac{1}{2}\log|\mathbf{K}_{\sigma}|-\frac{N}{2}\log(2\pi)   \tag*{(17.52)}$$

where the dependence of  $ \mathbf{K}_\sigma = \mathbf{K}_{X,X} + \sigma_2^2 \mathbf{I}_N $ on  $ \theta $ is implicit. The first term is a data fit term, the second term is a model complexity term, and the third term is just a constant. To understand the tradeoff between the first two terms, consider a SE kernel in 1D, as we vary the length scale  $ \ell $ and hold  $ \sigma_y^2 $ fixed. For short length scales, the fit will be good, so  $ \mathbf{y}^\top \mathbf{K}_\sigma^{-1} \mathbf{y} $ will be small. However, the model complexity will be high:  $ \mathbf{K} $ will be almost diagonal, (as in Figure 13.22, top right), since most points will not be considered “near” any others, so the  $ \log |\mathbf{K}_\sigma| $ term will be large. For long length scales, the fit will be poor but the model complexity will be low:  $ \mathbf{K} $ will be almost all 1's, (as in Figure 13.22, bottom right), so  $ \log |\mathbf{K}_\sigma| $ will be small.

We now discuss how to maximize the marginal likelihood. One can show that

$$  \begin{aligned}\frac{\partial}{\partial\theta_{j}}\log p(\boldsymbol{y}|\mathbf{X},\boldsymbol{\theta})&=\frac{1}{2}\boldsymbol{y}^{\top}\mathbf{K}_{\sigma}^{-1}\frac{\partial\mathbf{K}_{\sigma}}{\partial\theta_{j}}\mathbf{K}_{\sigma}^{-1}\boldsymbol{y}-\frac{1}{2}\mathrm{tr}(\mathbf{K}_{\sigma}^{-1}\frac{\partial\mathbf{K}_{\sigma}}{\partial\theta_{j}})\\&=\frac{1}{2}\mathrm{tr}\left((\boldsymbol{\alpha}\boldsymbol{\alpha}^{\top}-\mathbf{K}_{\sigma}^{-1})\frac{\partial\mathbf{K}_{\sigma}}{\partial\theta_{j}}\right)\end{aligned}   \tag*{(17.53)}$$

where  $ \alpha = K_{\sigma}^{-1}y $. It takes  $ O(N^{3}) $ time to compute  $ K_{\sigma}^{-1} $, and then  $ O(N^{2}) $ time per hyper-parameter to compute the gradient.

The form of  $ \frac{\partial \mathbf{K}_{\sigma}}{\partial \theta_j} $ depends on the form of the kernel, and which parameter we are taking derivatives with respect to. Often we have constraints on the hyper-parameters, such as  $ \sigma_y^2 \geq 0 $. In this case, we can define  $ \theta = \log(\sigma_y^2) $, and then use the chain rule.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_172_139_459_338.jpg" alt="图像" width="24%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_467_137_738_329.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_746_139_1029_327.jpg" alt="图像" width="24%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图 17.9: 边缘似然曲面中的局部极小值示意图。(a) 我们绘制了在固定信号水平 $ \sigma_f = 1 $ 下，使用图 b 和 c 中所示的 7 个数据点，对数边缘似然随核长度尺度 $ \ell $ 和观测噪声 $ \sigma_y $ 的变化情况。(b) 对应于左下角局部极小值的函数，参数约为 $ (\ell, \sigma_y) \approx (1, 0.2) $。该函数相当“波动”且噪声较低。(c) 对应于右上角局部极小值的函数，参数约为 $ (\ell, \sigma_y) \approx (10, 0.8) $。该函数相当平滑且噪声较高。数据由 $ (\ell, \sigma_f, \sigma_y) = (1, 1, 0.1) $ 生成。改编自 [RW06] 的图 5.5。由 gpr_demo_marglik.ipynb 生成。</div>

给定对数边缘似然及其导数的表达式后，我们可以使用任何标准的基于梯度的优化器来估计核参数。然而，由于目标函数不是凸函数，局部极小值可能成为一个问题（如下文所示），因此我们可能需要使用多次重启策略。

以式 (17.50) 中的 RBF 核为例，设 $ \sigma_f^2 = 1 $。在图 17.9(a) 中，我们绘制了 $ \log p(y|\mathbf{X}, \ell, \sigma_y^2) $（其中 $ \mathbf{X} $ 和 $ \mathbf{y} $ 是图 b 和 c 中所示的 7 个数据点）随 $ \ell $ 和 $ \sigma_y^2 $ 的变化情况。两个局部最优值用 + 标出。左下角的最优值对应于低噪声、短长度尺度的解（如图 b 所示）。右上角的最优值对应于高噪声、长长度尺度的解（如图 c 所示）。仅凭 7 个数据点，尚不足以有把握地判断哪个更合理，尽管更复杂的模型（图 b）的边缘似然比简单模型（图 c）高出约 60%。若数据量更大，则更复杂的模型会更受青睐。

图 17.9 还展示了一些其他有趣（且典型）的特征。$ \sigma_y^2 \approx 1 $ 的区域（图 a 顶部）对应于噪声很高的情况；在此区域内，边缘似然对长度尺度不敏感（由水平等高线表示），因为所有数据都被解释为噪声。$ \ell \approx 0.5 $ 的区域（图 a 左侧）对应于长度尺度非常短的情况；在此区域内，边缘似然对噪声水平不敏感（由垂直等高线表示），因为数据被完美插值。优秀的优化器不会选择这两个区域。

##### 17.2.6.2 贝叶斯推断

当数据点数量较少时（例如在贝叶斯优化中使用高斯过程时），对核参数进行点估计可能得到较差的结果 [Bul11; WF14]。在这种情况下，我们可能希望近似核参数的后验分布。可以使用多种方法。例如，[MA10] 展示了如何使用切片采样，[Hen+15] 展示了如何使用哈密顿蒙特卡洛，[BBV11] 展示了如何使用序列蒙特卡洛。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_219_148_581_371.jpg" alt="图像" width="31%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_626_147_987_371.jpg" alt="图像" width="31%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 17.10：基于单个输入特征（花萼长度）对鸢尾花（Setosa vs Versicolor）进行二分类的高斯过程分类器。粗竖线表示决策边界的可信区间。(a) SE 核。(b) SE 加线性核。改编自 [Mar18] 的图 7.11–7.12。由 gp_classify_iris_1d_pymc3.ipynb 生成。</div>

#### 17.2.7 用于分类的高斯过程

到目前为止，我们主要关注使用高斯似然的回归问题中的高斯过程。在这种情况下，后验也是高斯过程，所有计算都可以解析地进行。然而，如果似然是非高斯的，例如二分类中的伯努利似然，我们就无法精确计算后验。

我们可以采用多种近似方法，其中一些将在本书的后续部分 [Mur23] 中讨论。在本节中，我们使用哈密顿蒙特卡洛方法（第 4.6.8.4 节），同时处理潜在高斯函数 $f$ 和核超参数 $\theta$。基本思想是定义负对数联合分布

$$  -\mathcal{E}(\boldsymbol{f},\boldsymbol{\theta})=\log p(\boldsymbol{f},\boldsymbol{\theta}|\mathbf{X},\boldsymbol{y})=\log\mathcal{N}(\boldsymbol{f}|\mathbf{0},\mathbf{K}(\mathbf{X},\mathbf{X}))+\sum_{n=1}^{N}\log\operatorname{Ber}(y_{n}|f_{n}(\boldsymbol{x}_{n}))+\log p(\boldsymbol{\theta})   \tag*{(17.55)}$$

然后使用自动微分计算 $\nabla_f \mathcal{E}(f, \theta)$ 和 $\nabla_\theta \mathcal{E}(f, \theta)$，并将这些梯度输入到高斯提议分布中。

让我们考虑 [Mar18] 中的一个一维示例。这类似于图 4.20 中的贝叶斯逻辑回归示例，其目标是根据花萼长度 $x_n$ 的信息，将鸢尾花分类为 Setosa 或 Versicolor，$y_n \in \{0,1\}$。我们将使用长度尺度为 $\ell$ 的 SE 核，并对 $\ell$ 设置 Ga(2,0.5) 先验。

图 17.10a 展示了使用 SE 核的结果。这与线性逻辑回归的结果（见图 4.20）相似，不同之处在于边缘处（远离数据的地方）概率趋向于 0.5。这是因为先验均值函数为 $m(x) = 0$，而 $\sigma(0) = 0.5$。我们可以通过使用更灵活的核来消除这种伪影，该核编码了先验知识，即我们预期输出随输入单调增加或减小。这可以通过线性核来实现：

$$  \mathcal{K}(x,x^{\prime})=(x-c)(x^{\prime}-c)   \tag*{(17.56)}$$

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_187_151_584_391.jpg" alt="图片" width="34%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_619_150_1010_385.jpg" alt="图片" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图17.11：(a) 虚构的“太空流感”二分类问题。(b) 使用SE核的高斯过程拟合结果。改编自文献[Mar18]的图7.13-7.14，由gp_classify_spaceflu_1d_pymc3.ipynb生成。</div>


我们可以将其缩放后加到SE核上，得到

$$  \mathcal{K}(x,x^{\prime})=\tau(x-c)(x^{\prime}-c)+\exp\left[-\frac{(x-x^{\prime})^{2}}{2\ell^{2}}\right]   \tag*{(17.57)}$$

结果如图17.10b所示，看起来更合理。

有人可能会问，既然结果并不比简单的线性逻辑回归模型更好，为什么还要费心使用高斯过程？原因是高斯过程更加灵活，除了平滑性假设外，它几乎不依赖先验假设。例如，假设数据如图17.11a所示，此时线性逻辑回归模型无法拟合这些数据。理论上我们可以使用神经网络，但由于只有60个数据点，效果可能不佳。然而，高斯过程非常适合处理小样本场景。在图17.11b中，我们展示了使用SE核对这些数据进行高斯过程拟合的结果，结果看起来是合理的。

#### 17.2.8 与深度学习的关联

事实证明，高斯过程与深度神经网络之间存在许多有趣的关联和相似性。例如，可以证明，一个具有单层无限宽RBF单元的神经网络等价于一个使用RBF核的高斯过程（这源于RBF核可以表示为无限多个特征的内积）。实际上，许多类型的深度神经网络（在无限宽极限下）可以通过一种称为神经正切核的特定核转化为等价的高斯过程[JGH18]。详见本书的续作[Mur23]。

#### 17.2.9 将高斯过程扩展到大数据集

高斯过程（以及其他核方法，如17.3节讨论的支持向量机）的主要缺点在于，对 $N \times N$ 核矩阵求逆需要 $O(N^3)$ 时间，这使得该方法在处理大规模数据集时计算量过大。

---

对于大数据集而言速度较慢。人们提出了许多不同的近似方案来加速高斯过程（GPs）（可参见例如 [Liu+18a] 的综述）。本节将简要提及其中几种。更多细节请参见本书续篇 [Mur23]。

##### 17.2.9.1 稀疏（诱导点）近似

加速GP推理的一种简单方法是使用更少的数据。一种更好的方法是尝试将 $N$ 个训练点 $\mathbf{X}$ “概括”为 $M \ll N$ 个诱导点或伪输入 $\mathbf{Z}$。这使我们能够用 $p(\mathbf{f} | \mathbf{f}_Z)$ 替换 $p(\mathbf{f} | \mathbf{f}_X)$，其中 $\mathbf{f}_X = \{f(\mathbf{x}) : \mathbf{x} \in \mathbf{Z}\}$ 是训练点处观测到的函数值向量，而 $\mathbf{f}_Z = \{f(\mathbf{x}) : \mathbf{x} \in \mathbf{Z}\}$ 是诱导点处估计的函数值向量。通过优化 $(\mathbf{Z}, \mathbf{f}_Z)$，我们可以学习将训练数据 $(\mathbf{X}, \mathbf{f}_X)$ “压缩”成“瓶颈” $(\mathbf{Z}, \mathbf{f}_Z)$，从而将计算复杂度从 $O(N^3)$ 降低到 $O(M^3)$。这称为稀疏GP。整个过程可以通过变分推断的框架得到严格化。详情请参见本书续篇 [Mur23]。

##### 17.2.9.2 利用并行化与核矩阵结构

计算 $\mathbf{K}_{X,X}$ 的Cholesky分解需要 $O(N^3)$ 时间，该分解用于求解线性系统 $\mathbf{K}_\sigma \boldsymbol{\alpha} = \boldsymbol{y}$ 和计算 $|\mathbf{K}_{X,X}|$，其中 $\mathbf{K}_\sigma = \mathbf{K}_{X,X} + \sigma^2 \mathbf{I}_N$。Cholesky分解的一种替代方案是使用线性代数方法，通常称为Krylov子空间方法，这些方法仅基于矩阵向量乘法（MVM）。这些方法通常快得多，因为它们能够自然地利用核矩阵的结构。此外，即使核矩阵没有特殊结构，矩阵乘法也很容易并行化，因此可以通过GPU大大加速，这与主要基于顺序计算的Cholesky方法不同。这就是流行的GPyTorch包 [Gar+18] 的基础。更多细节请参见本书续篇 [Mur23]。

##### 17.2.9.3 随机特征近似

尽管核方法的强大之处在于能够避免使用输入的显式特征化表示，但此类核方法为了求逆Gram矩阵 $\mathbf{K}$，需要 $O(N^3)$ 的时间。这使得在大规模数据上使用这些方法变得困难。幸运的是，对于许多（平移不变的）核函数，我们可以使用随机选择的有限 $M$ 个基函数来近似其特征映射，从而将代价降低到 $O(NM + M^3)$。下面我们简要讨论这一思想。更多细节可参见例如 [Liu+20]。

##### RBF核的随机特征

我们将关注高斯RBF核的情况。可以证明：

$$
\mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})\approx\phi(\boldsymbol{x})^{\top}\phi(\boldsymbol{x}^{\prime}) \tag*{(17.58)}
$$

其中（实值）特征向量由下式给出：

$$
\phi(\boldsymbol{x})\triangleq\frac{1}{\sqrt{T}}[(\sin(\boldsymbol{\omega}_{1}^{\mathsf{T}}\boldsymbol{x}),...,\sin(\boldsymbol{\omega}_{T}^{\mathsf{T}}\boldsymbol{x}),\cos(\boldsymbol{\omega}_{1}^{\mathsf{T}}\boldsymbol{x}),...,\cos(\boldsymbol{\omega}_{T}^{\mathsf{T}}\boldsymbol{x}))] \tag*{(17.59)}
$$

$$
=\frac{1}{\sqrt{T}}\left[\sin(\Omega x),\cos(\Omega x)\right] \tag*{(17.60)}
$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND license。

---

其中 $ T = M/2 $，$ \Omega \in \mathbb{R}^{T \times D} $ 是一个随机高斯矩阵，其元素独立同分布地采样自 $ \mathcal{N}(0,1/\sigma^2) $，其中 $ \sigma $ 是核带宽。随着 $ M $ 增大，近似的偏差会减小。在实际应用中，我们使用有限的 $ M $，并通过抽取单个随机矩阵来计算期望的单一蒙特卡洛近似。方程(17.60)中的特征被称为**随机傅里叶特征** (RFF) [RR08] 或“随机厨房水槽的加权和” [RR09]。

我们也可以使用正随机特征，而不是三角随机特征，这在某些应用中可能更可取，例如使用注意力机制的模型（见第15.6.4节）。具体地，我们可以使用

$$  \phi(\boldsymbol{x})\triangleq e^{-||\boldsymbol{x}||^{2}/2}\frac{1}{\sqrt{M}}\left[(\exp(\boldsymbol{\omega}_{1}^{\mathsf{T}}\boldsymbol{x}),\cdots,(\exp(\boldsymbol{\omega}_{M}^{\mathsf{T}}\boldsymbol{x}))\right.   \tag*{(17.61)}$$

其中 $ \omega_{m} $ 的采样方式同上。详见 [Cho+20b]。

无论使用三角特征还是正特征，我们都可以通过确保 $ \Omega $ 的行是随机但正交的来获得更低方差的估计；这些被称为**正交随机特征**。这种采样可以通过对非结构化高斯矩阵进行 Gram-Schmidt 正交化 [Yu+16] 或几种更快的近似方法（参见 [CRW17; Cho+19]）来高效实现。

##### 快餐近似

遗憾的是，存储随机矩阵 $ \Omega $ 需要 $ O(DM) $ 的空间，计算 $ \Omega \times \text{向量} $ 需要 $ O(DM) $ 的时间，其中 $ D $ 是输入维度，$ M $ 是随机特征的数量。当 $ M \gg D $ 时，这会变得不可行，而为了在原始特征集上获得优势，我们可能需要 $ M $ 很大。幸运的是，我们可以使用快速 **Hadamard 变换** 将内存从 $ O(MD) $ 减少到 $ O(M) $，并将时间从 $ O(MD) $ 减少到 $ O(M \log D) $。这种方法被称为 **fastfood [LSS13]**，这个名称源于最初术语“厨房水槽”。

##### 极限学习机

我们可以利用核的随机特征近似，将高斯过程转换为如下形式的线性模型：

$$  f(x;\boldsymbol{\theta})=\mathbf{W}\boldsymbol{\phi}(x)=\mathbf{W}h(\boldsymbol{\Omega}x)   \tag*{(17.62)}$$

其中对于 RBF 核，$ h(a) = \sqrt{1/M}[\sin(a), \cos(a)] $。这等价于一个具有随机（且固定）输入到隐藏层权重的单层 MLP。当 $ M > N $ 时，这对应于一个过参数化模型，可以完美插值训练数据。

在 [Cur+17] 中，他们应用该方法通过 SGD 拟合形如 $ f(\boldsymbol{x};\boldsymbol{\theta}) = \boldsymbol{W}^{\top}h(\hat{\Omega}\boldsymbol{x}) + \boldsymbol{b} $ 的逻辑回归模型，并将所得方法称为“McKernel”。我们也可以同时优化 $ \Omega $ 和 $ \mathbf{W} $，正如 [Alb+17] 中所讨论的，尽管此时问题不再是凸的。

另一种方案是使用 $ M < N $，但堆叠多个这样的随机非线性层，仅优化输出权重。这被称为**极限学习机** (ELM)（例如参见 [Hua14]），尽管这项工作尚存争议。$^{1}$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_368_121_801_329.jpg" alt="图像" width="37%" /></div>

<div style="text-align: center;">图 17.12：大间隔原理的图示。左：大间隔分离超平面。右：小间隔分离超平面。</div>

### 17.3 支持向量机（SVMs）

在本节中，我们讨论一种用于分类和回归问题的（非概率性）预测器，其形式如下：

$$  f(\boldsymbol{x})=\sum_{i=1}^{N}\alpha_{i}\mathcal{K}(\boldsymbol{x},\boldsymbol{x}_{i})   \tag*{(17.63)}$$

通过添加适当的约束，我们可以确保许多系数 $\alpha_{i}$ 为零，从而在测试时预测仅依赖于训练点的一个子集，这些点被称为“支持向量”。因此，得到的模型称为支持向量机（support vector machine，简称SVM）。下面我们给出简要总结。更多细节可参见例如 [VGS97; SS01]。

#### 17.3.1 大间隔分类器

考虑一个形如 $h(\boldsymbol{x}) = \mathrm{sign}(f(\boldsymbol{x}))$ 的二元分类器，其中决策边界由以下线性函数给出：

$$  f(\boldsymbol{x})=\boldsymbol{w}^{\top}\boldsymbol{x}+w_{0}   \tag*{(17.64)}$$

（在SVM文献中，通常假设类别标签为-1和+1，而非0和1。为避免混淆，我们用 $\bar{y}$ 而非 $y$ 表示这些目标标签。）可能存在许多条能够分隔数据的直线。然而，直觉上我们希望选择具有最大 **间隔（margin）** 的那一条，即距离决策边界最近的点到边界的距离，因为这能给出最鲁棒的解。这一想法在图17.12中得到了说明：左侧的解具有比右侧更大的间隔，因此它对数据扰动的敏感度更低。

如何计算这样的大间隔分类器？首先，我们需要推导一个点到决策边界距离的表达式。参考图17.13(a)，我们看到

$$  x=x_{\perp}+r\frac{w}{\left\|\boldsymbol{w}\right\|}   \tag*{(17.65)}$$

其中 $r$ 是 $\boldsymbol{x}$ 到决策边界（其法向量为 $\boldsymbol{w}$）的距离，而 $\boldsymbol{x}_{\perp}$ 是 $\boldsymbol{x}$ 在该边界上的正交投影。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_175_112_939_588.jpg" alt="图像" width="66%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图17.13: (a) 二维空间中线性决策边界几何的示意图。如果 $ f(\mathbf{x}) > 0 $，则点 $\mathbf{x}$ 被分类为属于决策区域 $R_1$，否则属于决策区域 $R_0$；$\mathbf{w}$ 是一个与决策边界垂直的向量。项 $w_0$ 控制决策边界与原点之间的距离。$x_{\perp}$ 是 $\mathbf{x}$ 在边界上的正交投影。$\mathbf{x}$ 到边界的带符号距离为 $f(\mathbf{x}) / ||\mathbf{w}||$。改编自[Bis06]的图4.1。(b) 带有圆点的点是支持向量，其对偶变量 $\alpha_n > 0$。在软间隔情况下，我们为每个样本关联一个松弛变量 $\xi_n$。如果 $0 < \xi_n < 1$，则该点位于间隔内部，但在决策边界的正确一侧。如果 $\xi_n > 1$，则该点位于边界的错误一侧。改编自[Bis06]的图7.3。</div>


我们希望最大化 $r$，因此需要将其表示为 $\mathbf{w}$ 的函数。首先，注意到

$$  f(\boldsymbol{x})=\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}+w_{0}=(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{\perp}+w_{0})+r\frac{\boldsymbol{w}^{\mathsf{T}}\boldsymbol{w}}{||\boldsymbol{w}||}=(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{\perp}+w_{0})+r||\boldsymbol{w}||   \tag*{(17.66)}$$

由于 $ 0 = f(\boldsymbol{x}_{\perp}) = \boldsymbol{w}^{\mathrm{T}}\boldsymbol{x}_{\perp} + w_{0} $，我们有 $ f(\boldsymbol{x}) = r||\boldsymbol{w}|| $，因此 $ r = \frac{f(\boldsymbol{x})}{||\boldsymbol{w}||} $。

由于我们希望确保每个点都位于边界的正确一侧，我们还需要 $ f(\boldsymbol{x}_n)\tilde{y}_n > 0 $。我们想要最大化最近点的距离，因此最终目标变为

$$  \max_{\boldsymbol{w},w_{0}}\frac{1}{\left|\left|\boldsymbol{w}\right|\right|}\min_{n=1}^{N}\left[\tilde{y}_{n}(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{n}+w_{0})\right]   \tag*{(17.67)}$$

注意，通过使用 $ \boldsymbol{w} \to k\boldsymbol{w} $ 和 $ w_0 \to k w_0 $ 对参数进行重新缩放，我们不会改变任何点到边界的距离，因为当我们除以 $ \|\boldsymbol{w}\| $ 时，因子 $ k $ 会抵消。因此，让我们定义尺度因子，使得对于距离决策边界最近的点，有 $ \tilde{y}_n f_n = 1 $。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_257_120_879_336.jpg" alt="图像" width="53%" /></div>


<div style="text-align: center;">图 17.14：在计算最大间隔分类器之前对输入特征进行缩放的好处的示意图。改编自 [Gér19] 的图 5.2。由 svm_classifier_feature_scaling.ipynb 生成。</div>


因此，我们要求对所有 $n$ 都有 $ \tilde{y}_n f_n \geq 1 $。最后，注意到最大化 $ 1/||\mathbf{w}|| $ 等价于最小化 $ ||\mathbf{w}||^2 $。于是我们得到新的目标函数：

$$  \min_{\boldsymbol{w},w_{0}}\frac{1}{2}||\boldsymbol{w}||^{2}\text{s.t.}\tilde{y}_{n}(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{n}+w_{0})\geq1,n=1:N   \tag*{(17.68)}$$

（系数 $ \frac{1}{2} $ 是为了方便添加，不影响最优参数。）该约束表明我们希望所有点位于决策边界正确的一侧，且间隔至少为 1。

注意，在使用支持向量机（SVM）之前对输入变量进行缩放非常重要，否则间隔会平等地使用所有输入维度来衡量点到边界的距离。参见图 17.14 的说明。

#### 17.3.2 对偶问题

式 (17.68) 中的目标是一个标准的二次规划问题（见第 8.5.4 节），因为它是在线性约束下的二次目标。该问题有 $N + D + 1$ 个变量和 $N$ 个约束，称为原始问题。

在凸优化中，对于每个原始问题，我们都可以推导出对偶问题。令 $ \alpha \in \mathbb{R}^N $ 为对偶变量，对应于强制执行 $N$ 个不等式约束的拉格朗日乘子。广义拉格朗日函数如下（有关约束优化的相关背景知识，请参见第 8.5.2 节）：

$$  \mathcal{L}(\boldsymbol{w},w_{0},\boldsymbol{\alpha})=\frac{1}{2}\boldsymbol{w}^{\top}\boldsymbol{w}-\sum_{n=1}^{N}\alpha_{n}(\tilde{y}_{n}(\boldsymbol{w}^{\top}\boldsymbol{x}_{n}+w_{0})-1)   \tag*{(17.69)}$$

为了优化该函数，我们必须找到一个满足下式的驻点：

$$  (\hat{\boldsymbol{w}},\hat{w}_{0},\hat{\boldsymbol{\alpha}})=\min_{\boldsymbol{w},w_{0}}\max_{\boldsymbol{\alpha}}\mathcal{L}(\boldsymbol{w},w_{0},\boldsymbol{\alpha})   \tag*{(17.70)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可协议。

---

我们可以通过对 w 和 w0 计算偏导数并设为零来实现。我们有

$$  \nabla_{\boldsymbol{w}}\mathcal{L}(\boldsymbol{w},w_{0},\boldsymbol{\alpha})=\boldsymbol{w}-\sum_{n=1}^{N}\alpha_{n}\tilde{y}_{n}\boldsymbol{x}_{n}   \tag*{(17.71)}$$

$$  \frac{\partial}{\partial w_{0}}\mathcal{L}(\boldsymbol{w},w_{0},\boldsymbol{\alpha})=-\sum_{n=1}^{N}\alpha_{n}\tilde{y}_{n}   \tag*{(17.72)}$$

因此

$$  \hat{\boldsymbol{w}}=\sum_{n=1}^{N}\hat{\alpha}_{n}\tilde{y}_{n}\boldsymbol{x}_{n}   \tag*{(17.73)}$$

$$  0=\sum_{n=1}^{N}\hat{\alpha}_{n}\tilde{y}_{n}   \tag*{(17.74)}$$

将这些代入拉格朗日函数，得到

$$  \mathcal{L}(\hat{\boldsymbol{w}},\hat{w}_{0},\boldsymbol{\alpha})=\frac{1}{2}\hat{\boldsymbol{w}}^{\top}\hat{\boldsymbol{w}}-\sum_{n=1}^{N}\alpha_{n}\tilde{y}_{n}\hat{\boldsymbol{w}}^{\top}\boldsymbol{x}_{n}-\sum_{n=1}^{N}\alpha_{n}\tilde{y}_{n}w_{0}+\sum_{n=1}^{N}\alpha_{n}   \tag*{(17.75)}$$

$$  =\frac{1}{2}\hat{\boldsymbol{w}}^{\mathsf{T}}\hat{\boldsymbol{w}}-\hat{\boldsymbol{w}}^{\mathsf{T}}\hat{\boldsymbol{w}}-0+\sum_{n=1}^{N}\alpha_{n}   \tag*{(17.76)}$$

$$  =-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}\alpha_{i}\alpha_{j}\tilde{y}_{i}\tilde{y}_{j}\boldsymbol{x}_{i}^{\mathsf{T}}\boldsymbol{x}_{j}+\sum_{n=1}^{N}\alpha_{n}   \tag*{(17.77)}$$

这被称为目标函数的对偶形式。我们希望关于 $\alpha$ 最大化这个函数，约束条件为 $\sum_{n=1}^{N} \alpha_n \tilde{y}_n = 0$ 且对于 $n = 1,\dots,N$，有 $0 \leq \alpha_n$。

上述目标函数是一个包含 $N$ 个变量的二次规划问题。标准的二次规划求解器需要 $O(N^3)$ 时间。然而，针对这个问题，已经开发出了一些专用算法，避免了使用通用的二次规划求解器，例如序列最小优化（SMO）算法 [Pla98]，其时间复杂度为 $O(N)$ 到 $O(N^2)$。

由于这是一个凸目标函数，解必须满足 KKT 条件（第 8.5.2 节），这表明以下性质成立：

$$  \alpha_{n}\geq0   \tag*{(17.78)}$$

$$  \tilde{y}_{n}f(\boldsymbol{x}_{n})-1\geq0   \tag*{(17.79)}$$

$$  \alpha_{n}(\tilde{y}_{n}f(\boldsymbol{x}_{n})-1)=0   \tag*{(17.80)}$$

因此，要么 $\alpha_n = 0$（此时样本 $n$ 在计算 $\hat{w}$ 时被忽略），要么约束条件 $\tilde{y}_n(\hat{\mathbf{w}}^\top \mathbf{x}_n + \hat{w}_0) = 1$ 是活跃的。后一种条件意味着样本 $n$ 位于决策边界上；这些点被称为**支持向量**，如图 17.13(b) 所示。我们将支持向量的集合记为 $\mathcal{S}$。

---

为了进行预测，我们使用

$$  f(\boldsymbol{x};\hat{\boldsymbol{w}},\hat{w}_{0})=\hat{\boldsymbol{w}}^{\top}\boldsymbol{x}+\hat{w}_{0}=\sum_{n\in\mathcal{S}}\alpha_{n}\tilde{y}_{n}\boldsymbol{x}_{n}^{\top}\boldsymbol{x}+\hat{w}_{0}   \tag*{(17.81)}$$

为了求解 $ \hat{w}_0 $，我们可以利用对于任意支持向量，有 $ \tilde{y}_n f(\boldsymbol{x}; \hat{\boldsymbol{w}}, \hat{w}_0) = 1 $ 这一事实。将两边同时乘以 $ \tilde{y}_n $，并利用 $ \tilde{y}_n^2 = 1 $，可得 $ \hat{w}_0 = \tilde{y}_n - \hat{\boldsymbol{w}}^\top \boldsymbol{x}_n $。实际中，通过在所有支持向量上取平均可以得到更好的结果：

$$  \hat{w}_{0}=\frac{1}{|\mathcal{S}|}\sum_{n\in\mathcal{S}}\big(\tilde{y}_{n}-\hat{\boldsymbol{w}}^{\mathsf{T}}\boldsymbol{x}_{n}\big)=\frac{1}{|\mathcal{S}|}\sum_{n\in\mathcal{S}}\big(\tilde{y}_{n}-\sum_{m\in\mathcal{S}}\alpha_{m}\tilde{y}_{m}\boldsymbol{x}_{m}^{\mathsf{T}}\boldsymbol{x}_{n}\big)   \tag*{(17.82)}$$

#### 17.3.3 软间隔分类器

如果数据不是线性可分的，则不存在对所有 $ n $ 都满足 $ \tilde{y}_n f_n \geq 1 $ 的可行解。因此我们引入松弛变量 $ \xi_n \geq 0 $，并将硬约束 $ \tilde{y}_n f_n \geq 0 $ 替换为软间隔约束 $ \tilde{y}_n f_n \geq 1 - \xi_n $。新的目标函数变为

$$  \min_{\boldsymbol{w},w_{0},\boldsymbol{\xi}}\frac{1}{2}||\boldsymbol{w}||^{2}+C\sum_{n=1}^{N}\xi_{n}\text{s.t.}\xi_{n}\geq0,\tilde{y}_{n}(\boldsymbol{x}_{n}^{\mathsf{T}}\boldsymbol{w}+w_{0})\geq1-\xi_{n}   \tag*{(17.83)}$$

其中 $ C \geq 0 $ 是一个超参数，控制允许违反间隔约束的点的数量。（如果 $ C = \infty $，则退化为无正则化的硬间隔分类器。）

软间隔分类器对应的拉格朗日函数变为

$$  \mathcal{L}(\boldsymbol{w},w_{0},\boldsymbol{\alpha},\boldsymbol{\xi},\boldsymbol{\mu})=\frac{1}{2}\boldsymbol{w}^{\top}\boldsymbol{w}+C\sum_{n=1}^{N}\xi_{n}-\sum_{n=1}^{N}\alpha_{n}(\tilde{y}_{n}(\boldsymbol{w}^{\top}\boldsymbol{x}_{n}+w_{0})-1+\xi_{n})-\sum_{n=1}^{N}\mu_{n}\xi_{n}   \tag*{(17.84)}$$

其中 $ \alpha_n \geq 0 $ 和 $ \mu_n \geq 0 $ 是拉格朗日乘子。关于 $ \boldsymbol{w} $、$ w_0 $ 和 $ \boldsymbol{\xi} $ 进行优化，得到对偶形式

$$  \mathcal{L}(\boldsymbol{\alpha})=\sum_{i=1}^{N}\alpha_{i}-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}\alpha_{i}\alpha_{j}\tilde{y}_{i}\tilde{y}_{j}\boldsymbol{x}_{i}^{\top}\boldsymbol{x}_{j}   \tag*{(17.85)}$$

这与硬间隔情形相同；然而，约束条件不同。具体而言，KKT 条件隐含

$$  0\leq\alpha_{n}\leq C   \tag*{(17.86)}$$

$$  \sum_{n=1}^{N}\alpha_{n}\tilde{y}_{n}=0   \tag*{(17.87)}$$

如果 $ \alpha_n = 0 $，则该点被忽略。如果 $ 0 < \alpha_n < C $，则 $ \xi_n = 0 $，因此该点位于间隔边界上。如果 $ \alpha_n = C $，则该点可以位于间隔内部，并且当 $ \xi_n \leq 1 $ 时被正确分类，当 $ \xi_n > 1 $ 时被错误分类。参见 Figure 17.13(b) 的图示。因此 $ \sum_n \xi_n $ 是误分类点数量的上界。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

与之前一样，偏置项可通过下式计算：

$$  \hat{w}_{0}=\frac{1}{|\mathcal{M}|}\sum_{n\in\mathcal{M}}\left(\tilde{y}_{n}-\sum_{m\in\mathcal{S}}\alpha_{m}\tilde{y}_{m}\boldsymbol{x}_{m}^{\mathsf{T}}\boldsymbol{x}_{n}\right)   \tag*{(17.88)}$$

其中 M 是满足 $ 0 < \alpha_{n} < C $ 的点的集合。

软间隔SVM还有一种替代形式，称为 ν-SVM 分类器 [Sch+00]。该形式的目标是最大化

$$  \mathcal{L}(\boldsymbol{\alpha})=-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}\alpha_{i}\alpha_{j}\tilde{y}_{i}\tilde{y}_{j}\boldsymbol{x}_{i}^{\top}\boldsymbol{x}_{j}   \tag*{(17.89)}$$

满足约束条件：

$$  0\leq\alpha_{n}\leq1/N   \tag*{(17.90)}$$

$$  \sum_{n=1}^{N}\alpha_{n}\tilde{y}_{n}=0   \tag*{(17.91)}$$

$$  \sum_{n=1}^{M}\alpha_{n}\geq\nu   \tag*{(17.92)}$$

该方法的优势在于，参数 $\nu$（代替 $C$）可以解释为 margin errors（即 $\xi_n > 0$ 的点）比例的上界，同时也是支持向量数量的下界。

#### 17.3.4 核技巧

到目前为止，我们已经将大间隔二分类问题转化为一个包含 $N$ 个未知数（$\mathbf{a}$）的对偶问题，其求解通常需要 $O(N^3)$ 的时间，这可能会比较慢。然而，对偶问题的主要优势在于，我们可以将所有内积运算 $\mathbf{x}^{\top}\mathbf{x}^{\prime}$ 替换为调用一个正定（Mercer）核函数 $\mathcal{K}(\mathbf{x},\mathbf{x}^{\prime})$。这被称为 **核技巧**。

特别地，我们可以将式 (17.81) 中的预测函数重写为：

$$  f(\boldsymbol{x})=\hat{\boldsymbol{w}}^{\top}\boldsymbol{x}+\hat{w}_{0}=\sum_{n\in\mathcal{S}}\alpha_{n}\tilde{y}_{n}\boldsymbol{x}_{n}^{\top}\boldsymbol{x}+\hat{w}_{0}=\sum_{n\in\mathcal{S}}\alpha_{n}\tilde{y}_{n}\mathcal{K}(\boldsymbol{x}_{n},\boldsymbol{x})+\hat{w}_{0}   \tag*{(17.93)}$$

我们还需要对偏置项进行核化。这可以通过对式 (17.82) 进行核化实现：

$$  \hat{w}_{0}=\frac{1}{|\mathcal{S}|}\sum_{i\in\mathcal{S}}\left(\tilde{y}_{i}-(\sum_{j\in\mathcal{S}}\hat{\alpha}_{j}\tilde{y}_{j}\boldsymbol{x}_{j})^{\top}\boldsymbol{x}_{i}\right)=\frac{1}{|\mathcal{S}|}\sum_{i\in\mathcal{S}}\left(\tilde{y}_{i}-\sum_{j\in\mathcal{S}}\hat{\alpha}_{j}\tilde{y}_{j}\mathcal{K}(\boldsymbol{x}_{j},\boldsymbol{x}_{i})\right)   \tag*{(17.94)}$$

核技巧使我们无需处理数据的显式特征表示，并能轻松地将分类器应用于结构化对象，例如字符串和图。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_447_118_723_338.jpg" alt="图" width="23%" /></div>


<div style="text-align: center;">图 17.15：三种不同方法下对数几率与 x 的关系。改编自 [Tip01] 的图 10。经 Mike Tipping 许可使用。</div>


#### 17.3.5 将 SVM 输出转换为概率

SVM 分类器产生硬标签 $ \hat{y}(\boldsymbol{x}) = \text{sign}(f(\boldsymbol{x})) $。然而，我们通常希望获得对预测置信度的一种度量。一种启发式方法是将 $ f(\boldsymbol{x}) $ 解释为对数几率比 $ \log \frac{p(y=1|\boldsymbol{x})}{p(y=0|\boldsymbol{x})} $。然后，我们可以使用以下公式将 SVM 的输出转换为概率：

$$  p(y=1|\boldsymbol{x},\boldsymbol{\theta})=\sigma(af(\boldsymbol{x})+b)   \tag*{(17.95)}$$

其中参数 $a, b$ 可以通过在一个独立的验证集上进行最大似然估计得到。（使用训练集估计 $a$ 和 $b$ 会导致严重的过拟合。）该技术最早在 [Pla00] 中提出，称为 Platt 缩放。

然而，得到的概率并非特别校准，因为 SVM 的训练过程中没有任何依据可以将 $ f(\boldsymbol{x}) $ 解释为对数几率比。为了说明这一点，考虑来自 [Tip01] 的一个示例。假设我们有 1 维数据，其中 $ p(x|y=0) = \text{Unif}(0,1) $ 且 $ p(x|y=1) = \text{Unif}(0.5,1.5) $。由于类条件分布在 [0.5,1] 区间重叠，因此在该区域内类别 1 相对于类别 0 的对数几率应为零，而在该区域外则为无穷大。我们从模型中采样了 1000 个点，然后拟合了一个概率核分类器（RVM，详见第 17.4.1 节）和一个高斯核宽度为 0.1 的 SVM。两个模型都能完美地捕捉决策边界，并达到 25% 的泛化误差，这是该问题中的贝叶斯最优误差。RVM 的概率输出是对真实对数几率的一个良好近似，但 SVM 并非如此，如图 17.15 所示。

#### 17.3.6 与逻辑回归的联系

我们已经看到，位于决策边界正确一侧的数据点满足 $ \xi_n = 0 $；对于其他点，我们有 $ \xi_n = 1 - \tilde{y}_n f(\boldsymbol{x}_n) $。因此，公式 (17.83) 中的目标函数可以重写如下：

$$  \mathcal{L}(\boldsymbol{w})=\sum_{n=1}^{N}\ell_{\mathrm{hinge}}(\tilde{y}_{n},f(\boldsymbol{x}_{n})))+\lambda|\boldsymbol{w}||^{2}   \tag*{(17.96)}$$

其中 $ \lambda = (2C)^{-1} $，而 $ \ell_{\mathrm{hinge}}(y, \eta) $ 是铰链损失函数，定义为：

$$  \ell_{\mathrm{h i n g e}}(\tilde{y},\eta)=\max(0,1-\tilde{y}\eta)   \tag*{(17.97)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_283_202_478_397.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_669_129_899_390.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 17.16: (a) 一对多方法。绿色区域被预测同时属于类别 1 和类别 2。(b) 一对一方法。绿色区域的标签是模糊的。改编自 [Bis06] 的图 4.2。</div>


从图 4.2 中可以看出，这是一个凸的、分段可微的对 0-1 损失的上界，其形状类似于部分打开的门铰链。

相比之下，（惩罚）逻辑回归优化的是

$$  \mathcal{L}(\boldsymbol{w})=\sum_{n=1}^{N}\ell_{l l}(\tilde{y}_{n},f(\boldsymbol{x}_{n})))+\lambda|\boldsymbol{w}||^{2}   \tag*{(17.98)}$$

其中对数损失定义为

$$  \ell_{l l}(\tilde{y},\eta)=-\log p(y|\eta)=\log(1+e^{-\tilde{y}\eta})   \tag*{(17.99)}$$

该损失函数也绘制在图 4.2 中。我们看到它与铰链损失相似，但有两个重要区别。首先，铰链损失是分段线性的，因此不能用常规梯度方法对其优化。（不过，我们可以在 $\tilde{y}\eta = 1$ 处计算次梯度。）其次，铰链损失存在一个严格为零的区域，这导致了稀疏估计。

我们看到，这两个函数都是 0-1 损失的凸上界，0-1 损失定义为

$$  \ell_{01}(\tilde{y},\hat{y})=\mathbb{I}\left(\tilde{y}\neq\hat{y}\right)=\mathbb{I}\left(\tilde{y}\hat{y}<0\right)   \tag*{(17.100)}$$

这些上界更容易优化，可以视为 0-1 损失的替代函数。详见第 4.3.2 节。

#### 17.3.7 支持向量机的多类分类

支持向量机本质上是二分类器。将其转换为多类分类模型的一种方法是训练 $C$ 个二分类器，其中类别 $c$ 的数据被视为正类，所有其他类别的数据被视为负类。然后使用规则 $\hat{y}(\boldsymbol{x}) = \arg\max_{c} f_{c}(\boldsymbol{x})$ 进行预测。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_297_151_849_536.jpg" alt="图像" width="47%" /></div>


<div style="text-align: center;">图 17.17：使用 RBF 核（精度为 $ \gamma $）和正则化参数 C 的 SVM 分类器应用于双月数据。改编自 [Gér19] 的图 5.9。由 svm_classifier_2d.ipynb 生成。</div>


预测最终标签，其中 $ f_c(\boldsymbol{x}) = \log \frac{p(c=1|\boldsymbol{x})}{p(c=0|\boldsymbol{x})} $ 是分类器 c 给出的得分。这被称为**一对多方法**（也称一对全）。

遗憾的是，这种方法存在几个问题。首先，它可能导致输入空间中某些区域被模糊地标记。例如，图 17.16(a) 顶部的绿色区域同时被预测为类别 2 和类别 1。第二个问题是，各 $ f_c $ 得分的量级之间未进行校准，因此难以相互比较。最后，每个二分类子问题都可能遇到类别不平衡问题（第 10.3.8.2 节）。例如，假设我们有 10 个均匀分布的类别。在训练 $ f_1 $ 时，正例仅占 10%，负例占 90%，这会损害性能。

另一种方法是使用**一对一方法**（也称全对），即训练 $ C(C-1)/2 $ 个分类器来区分所有成对类别 $ f_{c,c'} $。然后根据得票最多的类别对点进行分类。然而，如图 17.16(b) 所示，这同样可能导致歧义。此外，该方法需要拟合 $ O(C^2) $ 个模型。

#### 17.3.8 如何选择正则化参数 C

支持向量机需要指定核函数和参数 C。通常通过交叉验证来选择 C。但请注意，C 与核参数之间存在很强的相互影响。例如，假设我们使用精度为 $ \gamma = \frac{1}{2\sigma^2} $ 的 RBF 核。若 $ \gamma $ 较大（对应窄核），则可能需要强正则化，因此 C 应较小。若 $ \gamma $ 较小，则应使用较大的 C 值。由此可见，$ \gamma $ 与 C 紧密耦合，如图 17.17 所示。

Libsvm [HCL03] 的作者建议在二维网格上进行交叉验证，其中 C ∈ {2^{-5}, 2^{-3}, …, 2^{15}}。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_123_536_413.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">$ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_630_196_947_404.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图17.18: (a) 对于使用RBF核的SVM分类器，在不同精度 $\gamma = 1/(2\sigma^2)$ 和不同正则化参数 $\lambda = 1/C$ 下的0-1误差的交叉验证估计，应用于从两个高斯混合中抽取的合成数据集。(b) 在 $\gamma = 5$ 处穿过该曲面的切片。红色虚线是贝叶斯最优误差，根据生成数据所用的模型通过贝叶斯规则计算得到。改编自[HTF09]的图12.6。由svmCgammaDemo.ipynb生成。</div>


且 $\gamma \in \{2^{-15}, 2^{-13}, \ldots, 2^3\}$。见图17.18，该图展示了作为 $C$ 和 $\gamma$ 函数的0-1风险的CV估计。

为了高效选择 $C$，可以开发一种类似于Lars算法（第11.4.4节）的路径跟踪算法。基本思想是从较小的 $C$ 开始，此时边界很宽，所有点都位于边界内且 $\alpha_i = 1$。通过缓慢增大 $C$，一小部分点会从边界内部移到外部，其 $\alpha_i$ 值从1变为0，因为它们不再是支持向量。当 $C$ 达到最大值时，边界为空，不再有支持向量。详见[Has+04]。

#### 17.3.9 核岭回归

回顾式(11.55)中的岭回归方程：

$$  \hat{\boldsymbol{w}}_{\mathrm{map}}=(\mathbf{X}^{\top}\mathbf{X}+\lambda\mathbf{I}_{D})^{-1}\mathbf{X}^{\top}\boldsymbol{y}=(\sum_{n}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\top}+\lambda\mathbf{I}_{D})^{-1}(\sum_{n}\tilde{y}_{n}\boldsymbol{x}_{n})   \tag*{(17.101)}$$

利用矩阵求逆引理（第7.3.3节），我们可以将岭估计重写如下：

$$  \boldsymbol{w}=\mathbf{X}^{\top}(\mathbf{X}\mathbf{X}^{\top}+\lambda\mathbf{I}_{N})^{-1}\boldsymbol{y}=\sum_{n}\boldsymbol{x}_{n}((\sum_{n}\boldsymbol{x}_{n}^{\top}\boldsymbol{x}_{n}+\lambda\mathbf{I}_{N})^{-1}\boldsymbol{y})_{n}   \tag*{(17.102)}$$

定义以下对偶变量：

$$  \boldsymbol{\alpha}\triangleq(\mathbf{X}\mathbf{X}^{\mathsf{T}}+\lambda\mathbf{I}_{N})^{-1}\boldsymbol{y}=(\sum_{n}\boldsymbol{x}_{n}^{\mathsf{T}}\boldsymbol{x}_{n}+\lambda\mathbf{I}_{N})^{-1}\boldsymbol{y}   \tag*{(17.103)}$$

“概率机器学习：导论”。在线版本。2024年11月23日

---

于是，我们可以将原始变量重写如下

$$  \boldsymbol{w}=\boldsymbol{X}^{\top}\boldsymbol{\alpha}=\sum_{n=1}^{N}\alpha_{n}\boldsymbol{x}_{n}   \tag*{(17.104)}$$

这表明解向量仅仅是 N 个训练向量的线性组合。在测试阶段代入该式来计算预测均值时，我们得到

$$  f(\boldsymbol{x};\boldsymbol{w})=\boldsymbol{w}^{\top}\boldsymbol{x}=\sum_{n=1}^{N}\alpha_{n}\boldsymbol{x}_{n}^{\top}\boldsymbol{x}   \tag*{(17.105)}$$

然后，我们可以利用核技巧将其改写为

$$  f(\boldsymbol{x};\boldsymbol{w})=\sum_{n=1}^{N}\alpha_{n}\mathcal{K}(\boldsymbol{x}_{n},\boldsymbol{x})   \tag*{(17.106)}$$

其中

$$  \boldsymbol{\alpha}=(\mathbf{K}+\lambda\mathbf{I}_{N})^{-1}\boldsymbol{y}   \tag*{(17.107)}$$

换句话说，

$$  f(\boldsymbol{x};\boldsymbol{w})=\boldsymbol{k}^{\mathrm{T}}(\mathbf{K}+\lambda\mathbf{I}_{N})^{-1}\boldsymbol{y}   \tag*{(17.108)}$$

其中 $ k = [\mathcal{K}(x, x_1), \ldots, \mathcal{K}(x, x_N)] $。这被称为核岭回归。

上述方法的问题在于解向量 $ \alpha $ 不是稀疏的，因此测试时的预测需要 $ O(N) $ 时间。我们将在第 17.3.10 节讨论一个解决方案。

#### 17.3.10 支持向量机回归

考虑以下 $ \ell_2 $ 正则化的经验风险最小化（ERM）问题：

$$  J(\boldsymbol{w},\lambda)=\lambda||\boldsymbol{w}||^{2}+\sum_{n=1}^{N}\ell(\tilde{y}_{n},\hat{y}_{n})   \tag*{(17.109)}$$

其中 $ \hat{y}_n = \boldsymbol{w}^\top \boldsymbol{x}_n + w_0 $。若采用二次损失 $ \ell(y, \hat{y}) = (y - \hat{y})^2 $（其中 $ y, \hat{y} \in \mathbb{R} $），则得到岭回归（第 11.3 节）。再应用核技巧，则得到核岭回归（第 17.3.9 节）。

核岭回归的问题在于解依赖于所有 N 个训练点，这使得计算难以处理。然而，通过改变损失函数，我们可以使最优基函数系数集 $ \alpha^{*} $ 变得稀疏，如下所示。

具体来说，考虑 Huber 损失函数（第 5.1.5.3 节）的一种变体，称为 epsilon 不敏感损失函数：

$$  L_{\epsilon}(y,\hat{y})\triangleq\begin{cases}{\begin{array}{c c}{0}&{\mathrm{i f~}|y-\hat{y}|<\epsilon}\\ {|y-\hat{y}|-\epsilon}&{\mathrm{o t h e r w i s e}}\\ \end{array}}\\ \end{cases}   \tag*{(17.110)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_211_121_552_399.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;"> $ y(x) $</div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_630_117_946_389.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图17.19：(a) $\ell_2$、Huber和$\epsilon$-不敏感损失函数的示意图，其中$\epsilon = 1.5$。由huberLossPlot.ipynb生成。(b) SVM回归中使用的$\epsilon$-带的示意图。带上方的点满足$\xi_i^+ > 0$且$\xi_i^- = 0$。带下方的点满足$\xi_i^+ = 0$且$\xi_i^- > 0$。带内的点满足$\xi_i^+ = \xi_i^- = 0$。改编自[Bis06]的图7.7。</div>


这意味着，如图17.19所示，位于预测值周围$\epsilon$-带内的任何点都不会受到惩罚。

相应的目标函数通常写成以下形式

$$  J=\frac{1}{2}||\boldsymbol{w}||^{2}+C\sum_{n=1}^{N}L_{\epsilon}(\tilde{y}_{n},\hat{y}_{n})   \tag*{(17.111)}$$

其中 $\hat{y}_n = f(\boldsymbol{x}_n) = \boldsymbol{w}^\top \boldsymbol{x}_n + w_0$，且 $C = 1/\lambda$ 是一个正则化常数。该目标函数是凸且无约束的，但由于损失项中的绝对值函数，它不可微。如我们在第11.4.9节讨论套索问题时所述，有几种可能的算法可供使用。一种流行的方法是将问题表述为一个约束优化问题。具体而言，我们引入松弛变量来表示每个点位于带外的程度：

$$  \tilde{y}_{n}\leq f(\boldsymbol{x}_{n})+\epsilon+\xi_{n}^{+}   \tag*{(17.112)}$$

$$  \tilde{y}_{n}\geq f(\boldsymbol{x}_{n})-\epsilon-\xi_{n}^{-}   \tag*{(17.113)}$$

由此，我们可以将目标函数重写如下：

$$  J=\frac{1}{2}||\boldsymbol{w}||^{2}+C\sum_{n=1}^{N}(\xi_{n}^{+}+\xi_{n}^{-})   \tag*{(17.114)}$$

这是关于 $\boldsymbol{w}$ 的二次函数，需要在满足式(17.112)-(17.113)的线性约束以及 $\xi_n^+ \geq 0$ 和 $\xi_n^- \geq 0$ 的正性约束下最小化。这是一个包含 $2N + D + 1$ 个变量的标准二次规划问题。

---

通过构造拉格朗日函数并优化，如上所述，可以证明最优解具有如下形式：

$$  \hat{w}=\sum_{n}\alpha_{n}x_{n}   \tag*{(17.115)}$$

其中 $ \alpha_n \geq 0 $ 为对偶变量（详情见例如 [SS02]）。幸运的是，$ \alpha $ 向量是稀疏的，即其许多分量为0。这是因为损失函数不关心小于 $ \epsilon $ 的误差。稀疏程度由 $ C $ 和 $ \epsilon $ 控制。

满足 $ \alpha_n > 0 $ 的 $ \mathbf{x}_n $ 被称为**支持向量**；这些点对应的误差位于 $ \epsilon $ 管道上或外部。在测试时，我们只需保留这些训练样本用于预测，因为

$$  f(\boldsymbol{x})=\hat{w}_{0}+\hat{\boldsymbol{w}}^{\mathrm{T}}\boldsymbol{x}=\hat{w}_{0}+\sum_{n:\alpha_{n}>0}\alpha_{n}\boldsymbol{x}_{n}^{\mathrm{T}}\boldsymbol{x}   \tag*{(17.116)}$$

最后，利用核技巧可得

$$  f(\boldsymbol{x})=\hat{w}_{0}+\sum_{n:\alpha_{n}>0}\alpha_{n}\mathcal{K}(\boldsymbol{x}_{n},\boldsymbol{x})   \tag*{(17.117)}$$

这一整体技术称为支持向量机回归，或简称SVM回归，最早由 [VGS97] 提出。

图17.20给出了一个使用RBF核（$ \gamma = 1 $）的示例。当C较小时，模型被高度正则化；当C较大时，模型正则化较弱，能更好地拟合数据。我们还可看到，当 $ \epsilon $ 较小时，管道变窄，因此支持向量增多。

### 17.4 稀疏向量机

高斯过程是非常灵活的模型，但在预测时的时间复杂度为 $ O(N) $，这可能难以承受。SVM通过估计稀疏权重向量解决了这一问题，但SVM无法输出校准的概率结果。

我们可以通过使用参数化模型来兼得两者优势，其中特征向量基于以每个训练点为中心的基函数定义，如下所示：

$$  \phi(\boldsymbol{x})=[\mathcal{K}(\boldsymbol{x},\boldsymbol{x}_{1}),\ldots,\mathcal{K}(\boldsymbol{x},\boldsymbol{x}_{N})]   \tag*{(17.118)}$$

这里 $ \mathcal{K} $ 是任意相似性核，不一定是Mercer核。方程(17.118)将 $ \boldsymbol{x} \in \mathcal{X} $ 映射到 $ \phi(\boldsymbol{x}) \in \mathbb{R}^N $。我们可以将这个新特征向量用于任何判别模型，例如逻辑回归。由于参数维度 $ D = N $，我们需要某种正则化来防止过拟合。如果使用 $ \ell_2 $ 正则化（我们称之为L2VM，即 $ \ell_2 $-向量机）来拟合此类模型，结果通常具有良好的预测性能，但权重向量 $ \boldsymbol{w} $ 是稠密的，且依赖于所有 $ N $ 个训练点。一个自然的解决方案是对 $ \boldsymbol{w} $ 施加稀疏性先验，从而无需保留所有样本。我们将此类方法称为**稀疏向量机**。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_302_126_857_701.jpg" alt="图" width="48%" /></div>


<div style="text-align: center;">图 17.20：支持向量回归的示意图。改编自文献 [Gér19] 中的图 5.11。由 svm_regression_1d.ipynb 生成。</div>


#### 17.4.1 相关向量机 (RVMs)

确保 w 稀疏的最简单方式是使用 $\ell_{1}$ 正则化，如第 11.4 节所述。我们称其为 L1VM 或拉普拉斯向量机，因为该方法等价于对 w 使用拉普拉斯先验进行最大后验估计。

然而，有时 $\ell_1$ 正则化在给定精度水平下无法达到足够的稀疏度。另一种方法是基于 ARD（自动相关判定），它利用第二类最大似然（也称为经验贝叶斯）来估计稀疏权重向量 [Mac95; Nea96]。若将该技术应用于如式 (17.118) 所示的核函数特征向量，便得到一种称为**相关向量机 (RVM)** 的方法 [Tip01; TF03]。

#### 17.4.2 稀疏与稠密核方法的比较

在图 17.21 中，我们比较了 L2VM、L1VM、RVM 以及使用 RBF 核的 SVM 在二维二分类问题上的表现。我们通过交叉验证为 SVM 选取 $C = 1/\lambda$（参见第 17.3.8 节）。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_212_132_988_736.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"> $ (d) $</div>


<div style="text-align: center;">图 17.21：使用带宽  $ \sigma = 0.3 $ 的 RBF 核进行非线性二分类的示例。(a) L2VM。(b) L1VM。(c) RVM。(d) SVM。绿色圆圈表示支持向量。由 kernelBinaryClassifDemo.ipynb 生成。</div>


然后对 L2VM 和 L1VM 使用相同的正则化参数值。我们看到所有方法都给出了相似的预测性能。然而，RVM 是最稀疏的模型，因此在运行时速度最快。

在图 17.22 中，我们在一个一维回归问题上比较了 L2VM、L1VM、RVM 以及使用 RBF 核的 SVM。再次看到，预测结果相当接近，但 RVM 最稀疏，其次是 L1VM，然后是 SVM。图 17.23 进一步说明了这一点。

除了这些小型经验示例外，我们在表 17.1 中给出了不同方法的更通用总结。该表的各列含义如下：

- 优化  $ w $：一个关键问题是目标函数  $ \mathcal{L}(\boldsymbol{w}) = -\log p(\mathcal{D}|\boldsymbol{w}) - \log p(\boldsymbol{w}) $ 是否为凸函数。L2VM、L1VM 和 SVM 具有凸目标函数。RVM 则不是。高斯过程是贝叶斯方法，其对权重  $ w $ 进行积分。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_253_131_503_328.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_659_133_910_328.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;">RVM</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_243_379_523_583.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_651_378_931_582.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"> $ (d) $</div>

<div style="text-align: center;">图17.22：使用带宽为 $ \sigma = 0.3 $ 的RBF核对含噪声sinc函数进行基于核的回归的模型拟合。(a) 采用 $ \lambda = 0.5 $ 的L2VM。(b) 采用 $ \lambda = 0.5 $ 的L1VM。(c) RVM。(d) 通过交叉验证选择 $ C = 1/\lambda $ 的SVM回归。红色圆圈表示保留的训练样本。由rum_regression_1d.ipynb生成。</div>

- 优化核：所有方法都需要“调节”核参数，例如RBF核的带宽以及正则化程度。对于基于高斯先验的方法（包括L2VM、RVM和GP），我们可以使用高效的基于梯度的优化器来最大化边际似然。对于SVM和L1VM，我们必须使用交叉验证，这比较慢（参见第17.3.8节）。

• 稀疏性：L1VM、RVM和SVM是稀疏核方法，因为它们只使用训练样本的一个子集。GP和L2VM不稀疏：它们使用所有训练样本。稀疏性的主要优点是测试时的预测通常更快。然而，这通常会导致预测过于自信。

- 概率输出：除SVM外，所有方法都产生形式为 $ p(y|\boldsymbol{x}) $ 的概率输出。SVM产生一个可以转换为概率的“置信度”值，但这种概率通常校准得很差（参见第17.3.5节）。

• 多分类：除SVM外，所有方法都自然地适用于多分类设置，通过使用类别分布而不是伯努利分布。SVM可以制成多分类器，但这种方法存在各种困难，如第17.3.7节所述。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_243_123_522_336.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_649_122_931_336.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">RVM</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">SVM</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_243_379_522_583.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_651_381_931_585.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 17.23：图 17.22 中各模型估计的系数。由 rvm_regression_1d.ipynb 生成。</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>方法</td><td style='text-align: center; word-wrap: break-word;'>最优 w</td><td style='text-align: center; word-wrap: break-word;'>最优核函数</td><td style='text-align: center; word-wrap: break-word;'>稀疏性</td><td style='text-align: center; word-wrap: break-word;'>概率输出</td><td style='text-align: center; word-wrap: break-word;'>多分类</td><td style='text-align: center; word-wrap: break-word;'>非 Mercer 核</td><td style='text-align: center; word-wrap: break-word;'>章节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SVM</td><td style='text-align: center; word-wrap: break-word;'>凸优化</td><td style='text-align: center; word-wrap: break-word;'>交叉验证</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>间接</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>17.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>L2VM</td><td style='text-align: center; word-wrap: break-word;'>凸优化</td><td style='text-align: center; word-wrap: break-word;'>经验贝叶斯</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>17.4.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>L1VM</td><td style='text-align: center; word-wrap: break-word;'>凸优化</td><td style='text-align: center; word-wrap: break-word;'>交叉验证</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>17.4.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RVM</td><td style='text-align: center; word-wrap: break-word;'>非凸</td><td style='text-align: center; word-wrap: break-word;'>经验贝叶斯</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>17.4.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GP</td><td style='text-align: center; word-wrap: break-word;'>不适用</td><td style='text-align: center; word-wrap: break-word;'>经验贝叶斯</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>是</td><td style='text-align: center; word-wrap: break-word;'>否</td><td style='text-align: center; word-wrap: break-word;'>17.2.7</td></tr></table>

<div style="text-align: center;">表 17.1：多种基于核的分类器比较。EB = 经验贝叶斯，CV = 交叉验证。详见正文。</div>


● Mercer 核：SVM 和 GP 要求核函数正定；其他技术则无此要求，因为方程 (17.118) 中的核函数可以是两个输入的任意函数。

### 17.5 练习

**练习 17.1** [手工拟合 SVM 分类器 †]

（来源：Jaakkola。）考虑一个一维数据集，包含两个点： $ x_1 = 0 $，标签 $ y_1 = -1 $； $ x_2 = \sqrt{2} $，标签 $ y_2 = 1 $。将每个点通过特征向量 $ \phi(x) = [1, \sqrt{2}x, x^2]^T $ 映射到三维空间。（这是

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可证。

---

等价于使用二阶多项式核。）最大间隔分类器具有如下形式：

$$  \min||\boldsymbol{w}||^{2}\text{s.t.}   \tag*{(17.119)}$$

$$  y_{1}(\boldsymbol{w}^{T}\phi(\boldsymbol{x}_{1})+w_{0})\geq1   \tag*{(17.120)}$$

$$  y_{2}(\boldsymbol{w}^{T}\phi(\boldsymbol{x}_{2})+w_{0})\geq1   \tag*{(17.121)}$$

a. 写出一个与最优向量 **w** 平行的向量。提示：回顾图 17.12(a)，**w** 垂直于三维特征空间中两点之间的决策边界。

b. 这个 **w** 实现的间隔值是多少？提示：间隔是每个支持向量到决策边界的距离。提示2：考虑空间中两个点的几何关系，以及分隔两点的直线。

c. 利用间隔等于 $1/||\boldsymbol{w}||$ 这一事实，求解 **w**。

d. 使用你求出的 **w** 以及公式 17.119 至 17.121，求解 $w_{0}$。提示：这些点将位于决策边界上，因此不等式取等号。

e. 写出判别函数 $f(x) = w_0 + \boldsymbol{w}^T \phi(x)$ 关于 $x$ 的显式形式。

---

### 18.1 分类与回归树 (CART)

分类与回归树（Classification and regression trees，简称CART模型 [BFO84]），也称为决策树 [Qui86; Qui93]，通过递归划分输入空间，并在每个划分得到的区域中定义一个局部模型来进行定义。整体模型可以用一棵树表示，每个叶节点对应一个区域，具体说明如下。

#### 18.1.1 模型定义

我们首先考虑回归树，其中所有输入均为实数值。该树由一组嵌套的决策规则组成。在每个节点 $i$ 处，将输入向量 $\boldsymbol{x}$ 的特征维度 $d_i$ 与阈值 $t_i$ 进行比较，然后根据比较结果将输入传递到左分支或右分支（取决于输入是高于还是低于阈值）。在树的叶节点处，模型为落入该部分输入空间的任意输入指定预测输出。

例如，考虑图 18.1(a) 中的回归树。第一个节点询问 $x_{1}$ 是否小于某个阈值 $t_{1}$。如果是，则继续询问 $x_{2}$ 是否小于另一个阈值 $t_{2}$。如果是，则进入左下角的叶节点。这对应于由下式定义的输入空间区域：

$$ R_{1}=\left\{\boldsymbol{x}:x_{1}\leq t_{1},x_{2}\leq t_{2}\right\} \tag*{(18.1)} $$

我们可以将该区域与预测输出关联起来，例如 $y=2$。类似地，通过使用轴平行分割，我们可以将整个输入空间划分为 5 个区域，如图 18.1(b) 所示。$^{1}$

形式上，回归树可以定义为：

$$ f(\boldsymbol{x};\boldsymbol{\theta})=\sum_{j=1}^{J}w_{j}\mathbb{I}\left(\boldsymbol{x}\in R_{j}\right) \tag*{(18.2)} $$

其中 $R_{j}$ 是第 $j$ 个叶节点指定的区域，$w_{j}$ 是该节点的预测输出：

$$ w_{j}=\frac{\sum_{n=1}^{N}y_{n}\mathbb{I}\left(\boldsymbol{x}_{n}\in R_{j}\right)}{\sum_{n=1}^{N}\mathbb{I}\left(\boldsymbol{x}_{n}\in R_{j}\right)} \tag*{(18.3)} $$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_182_259_599_425.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_650_140_932_403.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 18.1: (a) 一个基于两个输入的回归树。(b) 对应的分段常数曲面，其中区域的高度为 2, 4, 6, 8 和 10。改编自 [HTF09] 的图 9.2。由 regtreeSurfaceDemo.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_192_569_594_756.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_651_600_931_764.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 18.2: (a) 一组带有相应二值标签的形状。特征包括：颜色（取值“蓝色”、“红色”、“其他”），形状（取值“椭圆形”、“其他”），以及大小（实数值）。(b) 一个假设的分类树，拟合了这些数据。标记为 $ (n_1, n_0) $ 的叶子节点表示有 $ n_1 $ 个正例落入该分区，以及 $ n_0 $ 个负例。</div>


并且 $ \boldsymbol{\theta}=\{(R_j,w_j):j=1:J\} $，其中 $ J $ 是节点数量。这些区域本身由从根节点到叶子节点路径上每次分裂所用的特征维度和相应阈值定义。例如，在图 18.1(a) 中，我们有 $ R_1=[(x_1\leq t_1),(x_2\leq t_2)] $，$ R_4=[(x_1\leq t_1),(x_2>t_2),(x_3\leq t_3)] $ 等。(对于类别型输入，我们可以通过将特征 $ x_i $ 与该特征的每个可能取值进行比较来定义分裂，而不是与数值阈值比较。) 我们将在第 18.1.2 节讨论如何学习这些区域。

对于分类问题，叶节点包含类标签的分布，而不仅仅是均值响应。参见图 18.2 的分类树示例。

---

#### 18.1.2 模型拟合

为了拟合模型，我们需要最小化以下损失函数：

$$  \mathcal{L}(\boldsymbol{\theta})=\sum_{n=1}^{N}\ell(y_{n},f(\boldsymbol{x}_{n};\boldsymbol{\theta}))=\sum_{j=1}^{J}\sum_{\boldsymbol{x}_{n}\in R_{j}}\ell(y_{n},w_{j})   \tag*{(18.4)}$$

遗憾的是，该函数不可微，因为需要学习离散的树结构。事实上，找到数据的最优划分是NP完全的[HR76]。标准做法是采用贪心过程，即每次迭代地生长树的一个节点。这种方法被CART [BF084]、C4.5 [Qui93]和ID3 [Qui86]这三个流行的实现所采用。

其思路如下。假设我们位于节点$i$；令$\mathcal{D}_i = \{(\boldsymbol{x}_n, y_n) \in N_i\}$为到达该节点的样本集合。我们将考虑如何将该节点分裂为左分支和右分支，以最小化每个子树的误差。

如果第$j$个特征是实值标量，我们可以通过与阈值$t$比较来划分节点$i$处的数据。特征$j$的可能阈值集合$\mathcal{T}_j$可通过排序$\{x_{nj}\}$的唯一值得到。例如，若特征1的值集为$\{4.5, -12, 72, -12\}$，则设置$\mathcal{T}_1 = \{-12, 4.5, 72\}$。对于每个可能的阈值，我们定义左分裂和右分裂：$\mathcal{D}_i^L(j, t) = \{(\boldsymbol{x}_n, y_n) \in N_i : x_{n,j} \leq t\}$和$\mathcal{D}_i^R(j, t) = \{(\boldsymbol{x}_n, y_n) \in N_i : x_{n,j} > t\}$。

如果第$j$个特征是分类变量，有$K_j$个可能取值，则我们检查该特征是否等于每个取值。这定义了$K_j$个可能的二元分裂：$\mathcal{D}_i^L(j,t) = \{(\mathbf{x}_n,y_n) \in N_i \mid x_{n,j} = t\}$和$\mathcal{D}_i^R(j,t) = \{(\mathbf{x}_n,y_n) \in N_i : x_{n,j} \neq t\}$。（或者，我们可以允许如Figure 18.2(b)所示的多路分裂。但这可能导致数据碎片化，即每个子树中落入的数据过少，从而引起过拟合。因此更常见的是使用二元分裂。）

一旦对于节点$i$处的每个$j$和$t$计算了$\mathcal{D}_i^L(j,t)$和$\mathcal{D}_i^R(j,t)$，我们按照如下方式选择最佳分裂特征$j_i$及其最佳值$t_i$：

$$ \left(j_{i},t_{i}\right)=\arg\min_{j\in\{1,\ldots,D\}}\min_{t\in\mathcal{T}_{j}}\frac{\left|\mathcal{D}_{i}^{L}(j,t)\right|}{\left|\mathcal{D}_{i}\right|}c(\mathcal{D}_{i}^{L}(j,t))+\frac{\left|\mathcal{D}_{i}^{R}(j,t)\right|}{\left|\mathcal{D}_{i}\right|}c(\mathcal{D}_{i}^{R}(j,t)) $$

现在讨论用于评估节点$i$代价的代价函数$c(\mathcal{D}_i)$。对于回归，我们可以使用均方误差：

$$  \mathrm{cost}(\mathcal{D}_{i})=\frac{1}{|\mathcal{D}|}\sum_{n\in\mathcal{D}_{i}}(y_{n}-\overline{y})^{2}   \tag*{(18.6)}$$

其中$\overline{y} = \frac{1}{|\mathcal{D}|} \sum_{n \in \mathcal{D}_i} y_n$是到达节点$i$的样本中响应变量的均值。

对于分类，我们首先计算该节点上类别标签的经验分布：

$$  \hat{\pi}_{i c}=\frac{1}{\left|\mathcal{D}_{i}\right|}\sum_{n\in\mathcal{D}_{i}}\mathbb{I}\left(y_{n}=c\right)   \tag*{(18.7)}$$

据此，我们可以计算基尼指数：

$$  G_{i}=\sum_{c=1}^{C}\hat{\pi}_{ic}(1-\hat{\pi}_{ic})=\sum_{c}\hat{\pi}_{ic}-\sum_{c}\hat{\pi}_{ic}^{2}=1-\sum_{c}\hat{\pi}_{ic}^{2}   \tag*{(18.8)}$$

作者：Kevin P. Murphy。(C) MIT出版社。遵循CC-BY-NC-ND许可协议。

---

这就是期望的误差率。为了理解这一点，请注意 $\hat{\pi}_{ic}$ 是叶子中随机一个样本属于类别 $c$ 的概率，而 $1 - \hat{\pi}_{ic}$ 是其被错误分类的概率。

另一种方式是将代价定义为节点的熵或偏差：

$$  H_{i}=\mathbb{H}(\hat{\boldsymbol{\pi}}_{i})=-\sum_{c=1}^{C}\hat{\pi}_{ic}\log\hat{\pi}_{ic}   \tag*{(18.9)}$$

一个 **纯节点**（即只包含某一类别的样本）的熵为 0。

给定上述某个代价函数后，我们可以利用公式 (18.5) 在每个节点上选择最优特征和最佳阈值。接着对数据进行划分，并递归地在每个数据子集上调用拟合算法。

在 [SL99] 中，他们提出使用二元逻辑回归模型来软化每个节点上的硬分割决策，这种方法被称为 **可微决策树** 或 **软决策树**。对于固定的树结构，这允许通过基于梯度的优化方法来拟合模型。

#### 18.1.3 正则化

如果让树生长到足够深，它可以在训练集上达到 0 误差（假设没有标签噪声），方法是将输入空间划分成足够小的区域，使得每个区域内的输出为常数。然而，这通常会导致过拟合。为了防止这一点，主要有两种方法。第一种是根据某些启发式规则停止树的生长过程，例如节点中样本数量过少，或达到最大深度。第二种方法是让树生长到最大深度（即无法再进行分裂时），然后通过将分裂子树合并回其父节点来进行剪枝（参见例如 [BA97b]）。这可以在一定程度上克服自顶向下树生长的贪心性质。（例如，考虑将自顶向下方法应用于图 13.1 中的异或数据：算法永远不会进行任何分裂，因为每个特征单独不具有预测能力。）然而，前向生长和后向剪枝比贪心的自顶向下方法更慢。

#### 18.1.4 处理缺失输入特征

一般来说，判别模型（如神经网络）难以处理缺失输入特征，这一点我们在第 1.5.5 节中讨论过。然而，对于树模型，有一些简单的启发式方法效果不错。

处理决策树中缺失输入的标准启发式方法是寻找一系列“后备”变量，这些变量可以在任意给定的分裂点诱导出与所选变量相似的分区；当所选变量在测试时缺失时，可以使用这些后备变量。这种方法称为 **替代分裂**。该方法找到高度相关的特征，可以被视为学习输入的局部联合模型。与生成模型相比，其优势在于不需要建模输入的全部联合分布，但缺点是完全是启发式的。对于分类变量，一种更简单的方法是将“缺失”编码为一个新值，然后将数据视为完全观测的。

#### 18.1.5 优缺点

树模型因其若干优点而广受欢迎：

• 它们易于解释。

---

### 18.1. 分类与回归树（CART）

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_126_571_403.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_598_151_986_412.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_190_472_579_732.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_598_472_986_733.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 18.3: (a) 仅使用花瓣长度和花瓣宽度特征，对鸢尾花数据拟合的深度为2的决策树。叶节点根据多数类别进行颜色编码。每个框内显示从根节点传递到该节点的训练样本数量，以及这些值落入每个类别的数量。可将其归一化，得到每个节点的类别标签分布。(b) 由 (a) 导出的决策面。(c) 在省略单个数据点（以红星标示）的数据上拟合的结果。(d) (b) 和 (c) 中两个模型的集成。由 dtree_sensitivity.ipynb 生成。</div>


• 它们可以轻松处理混合的离散和连续输入。

• 它们对输入的单调变换不敏感（因为分裂点基于数据点的排序），因此无需对数据进行标准化。

• 它们会自动进行变量选择。

• 它们对异常值相对鲁棒。

• 它们拟合速度快，且能很好地扩展到大规模数据集。

• 它们可以处理缺失的输入特征。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证

---

然而，树模型也存在一些缺点。主要问题在于，与其他类型的模型相比，它们的预测精度不高。这部分是由于树构建算法的贪婪性质所致。

一个相关问题是树模型的不稳定性：由于树生长过程的层级特性，输入数据的微小变动可能对树的结构产生较大影响，导致顶部的错误向下传播，影响整棵树。例如，考虑图18.3b中的树。由于使用了轴平行划分，即使从训练集中删除一个数据点，也可能导致决策面发生剧烈变化，如图18.3c所示。（删除特征也会导致不稳定性。）在第18.3节和第18.4节中，我们将把这种不稳定性转化为优点。

### 18.2 集成学习

在第18.1节中，我们看到决策树可能相当不稳定，即如果训练数据发生扰动，它们的预测可能会存在较大差异。换句话说，决策树是一种高方差估计器。降低方差的一种简单方法是对多个模型进行平均。这称为**集成学习**。得到的模型形式为

$$  f(y|\boldsymbol{x})=\frac{1}{|\mathcal{M}|}\sum_{m\in\mathcal{M}}f_{m}(y|\boldsymbol{x})   \tag*{(18.10)}$$

其中 $ f_{m} $ 是第 $ m $ 个基模型。集成模型的偏差与基模型相似，但方差更低，通常会提升整体性能（有关偏差-方差权衡的详细信息，请参见第4.7.6.3节）。

对回归模型的预测进行平均是一种合理的组合方式。对于分类器，有时对输出进行多数投票效果更好（这有时被称为**委员会方法**）。为了理解其益处，假设每个基模型是一个二分类器，准确率为 $ \theta $，并且类别1是正确类别。设 $ Y_m \in \{0,1\} $ 为第 $ m $ 个模型的预测值，$ S = \sum_{m=1}^M Y_m $ 为类别1的票数。我们将最终预测定义为多数投票，即如果 $ S > M/2 $ 则预测为类别1，否则为类别0。集成模型选择类别1的概率为

$$  p=\Pr(S>M/2)=1-B(M/2,M,\theta)   \tag*{(18.11)}$$

其中 $ B(x, M, \theta) $ 是参数为M和 $ \theta $ 的二项分布在x处的累积分布函数。对于 $ \theta = 0.51 $ 和 M = 1000，我们得到 p = 0.73；当 M = 10,000 时，p = 0.97。

投票方法的性能显著提升，是因为我们假设每个预测器独立地犯错误。在实践中，它们的错误可能相关，但只要集成足够多样化的模型，我们仍然可以取得更好的效果。

#### 18.2.1 堆叠

与使用未加权平均或多数投票相比，另一种替代方法是学习如何组合基模型，通过使用

$$  f(y|\boldsymbol{x})=\sum_{m\in\mathcal{M}}w_{m}f_{m}(y|\boldsymbol{x})   \tag*{(18.12)}$$

---

这被称为 \textbf{堆叠}（stacking），即“堆叠泛化”（stacked generalization）[Wol92]。需要注意的是，堆叠所使用的组合权重需要在独立的数据集上进行训练，否则它们会将所有权重集中到表现最好的基模型上。

#### 18.2.2 集成不等同于贝叶斯模型平均

值得指出的是，如 [Min00] 所述，模型的集成与对模型进行贝叶斯模型平均（第 4.6 节）并不相同。集成考虑了一个形式更宽的假设类：

$$  p(y|\boldsymbol{x},\boldsymbol{w},\boldsymbol{\theta})=\sum_{m\in\mathcal{M}}w_{m}p(y|\boldsymbol{x},\boldsymbol{\theta}_{m})   \tag*{(18.13)} $$

而 BMA 则使用：

$$  p(y|\boldsymbol{x},\mathcal{D})=\sum_{m\in\mathcal{M}}p(m|\mathcal{D})p(y|\boldsymbol{x},m,\mathcal{D})   \tag*{(18.14)} $$

关键区别在于：在 BMA 中，权重 $ p(m|\mathcal{D}) $ 之和为 1，并且在数据量趋于无穷时，仅会选定一个模型（即 MAP 模型）。相比之下，集成权重 $ w_m $ 是任意的，不会以这种方式收缩到单一模型上。

### 18.3 袋装

本节我们讨论 **袋装**（bagging）[Bre96]，其全称为“自助聚合”（bootstrap aggregating）。这是一种简单的集成学习形式，对数据的多个不同随机版本分别拟合 M 个不同的基模型；这促使不同模型做出多样化的预测。数据集采用有放回抽样（一种称为自助采样法的技术，第 4.7.3 节），因此一个给定样本可能多次出现，直至每个模型总共获得 N 个样本（其中 N 是原始数据点的数量）。

自助法的缺点在于每个基模型平均只能看到约 63% 的独特输入样本。原因如下：从一个大小为 N 的集合中，在 N 次抽取中单个项目未被选中的概率为 $ (1 - 1/N)^N $。当 N 很大时，该值趋近于 $ e^{-1} \approx 0.37 $，这意味着仅有 $ 1 - 0.37 = 0.63 $ 的数据点被选中。

未被特定基模型使用的 37% 的训练实例称为袋外实例（out-of-bag instances，oob）。我们可以利用基模型在这些 oob 实例上的预测表现来估计测试集性能，这为交叉验证提供了一种有用的替代方案。

自助法的主要优势在于它防止集成过度依赖任何单个训练样本，从而增强了鲁棒性和泛化能力 [Gra04]。例如，比较图 18.3b 和图 18.3c 可以发现，从训练集中删除单个样本可能对学习的决策树产生重大影响（即使决策树生长算法本身是确定性的）。通过平均这两个模型的预测，我们得到了图 18.3d 中更为合理的预测模型。这种优势通常随集成规模的增大而增强，如图 18.4 所示（当然，更大的集成需要更多的内存和时间）。

袋装并不总能提升性能。具体而言，它依赖于基模型是不稳定估计量这一前提，即删除部分数据会显著改变最终的模型拟合结果。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_220_130_517_348.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_128_925_603.jpg" alt="Image" width="61%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_627_132_924_346.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_221_378_517_589.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_628_379_924_589.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图18.4：(a) 单棵决策树。(b-c) 包含10棵和50棵树的Bagging集成。(d) 包含50棵树的随机森林。改编自[Gér19]的图7.5。由bagging_trees.ipynb和rf_demo_2d.ipynb生成。</div>

决策树的情况如此，但其他模型（如最近邻分类器）则不然。对于神经网络，情况更为复杂。它们对训练集可能不稳定。另一方面，如果深度网络仅看到63%的数据，其性能会下降，因此Bagged深度神经网络通常效果不佳[NTL20]。

### 18.4 随机森林

Bagging依赖于一个假设：对数据的不同子集重复运行相同的学习算法，会产生足够多样化的基模型。随机森林技术[Bre01]试图进一步降低基学习器之间的相关性，其方法是在树的每个节点处基于随机选择的输入变量子集以及随机选择的数据实例子集来学习树。它通过修改公式(18.5)来实现这一点，使得特征分裂维度j在特征的随机子集 $ S_i \subset \{1, \ldots, D\} $ 上进行优化。

例如，考虑电子邮件垃圾数据集[HTF09, p301]。该数据集包含4601封电子邮件，每封邮件被分类为垃圾邮件(1)或非垃圾邮件(0)。该数据由惠普(HP)实验室的George Forman开源。

共有57个定量（实值）特征，如下所示：

- 48个特征对应于邮件中与给定单词（例如“remove”或“labs”）匹配的单词百分比。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_377_129_792_397.jpg" alt="图像" width="36%" /></div>


<div style="text-align: center;">图 18.5: 装袋、随机森林和梯度提升（使用对数损失）的预测准确率与树集成大小的关系。改编自 [HTF09] 的图 15.1。由 spam_tree_ensemble_compare.ipynb 生成。</div>


• 6 个特征，对应邮件中匹配特定字符的字符百分比，分别是 ; . [ ! $ #

• 3 个特征，对应连续大写字母序列的平均长度、最大长度和总长度。（这些特征分别称为 CAPAVE、CAPMAX 和 CAPTOT。）

图 18.5 显示，随机森林的效果远好于装袋决策树，因为许多输入特征是无关的。（我们还可以看到，一种称为“提升”的方法（将在第 18.5 节讨论）效果更好；然而，该方法需要顺序拟合树，而随机森林可以并行拟合。）

### 18.5 提升

无论是通过装袋还是随机森林算法拟合的树集成，都符合如下形式的模型：

$$  f(\boldsymbol{x};\boldsymbol{\theta})=\sum_{m=1}^{M}\beta_{m}F_{m}(\boldsymbol{x};\boldsymbol{\theta}_{m})   \tag*{(18.15)}$$

其中 $ F_m $ 是第 $ m $ 棵树，$ \beta_m $ 是对应的权重，通常设为 $ \beta_m = 1/M $。我们可以对此进行推广，允许 $ F_m $ 函数为通用的函数逼近器（例如神经网络），而不仅仅是树。这样得到的结果称为 **加性模型** [HTF09]。我们可以将其视为具有自适应基函数的线性模型。通常的目标是最小化经验损失（可带有正则化项）：

$$  \mathcal{L}(f)=\sum_{i=1}^{N}\ell(y_{i},f(\boldsymbol{x}_{i}))   \tag*{(18.16)}$$

**提升** [Sch90; FS96] 是一种顺序拟合加性模型的算法，其中每个 $ F_m $ 是一个二元分类器，返回 $ F_m \in \{-1, +1\} $。特别地，我们首先在原始数据上拟合 $ F_1 $，

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证。

---

然后我们根据 $F_1$ 产生的误差对数据样本进行加权，因此被错误分类的样本获得更大的权重。接下来我们将 $F_2$ 拟合到这个加权数据集上。我们重复这个过程，直到拟合了所需数量的 M 个组件。（M 是一个控制整体模型复杂度的超参数，可以通过监控验证集上的性能并采用早停法来选择。）

可以证明，只要每个 $F_m$ 的准确率优于随机猜测（即使在加权数据集上也是如此），那么最终的集成分类器将比任何一个单独组件具有更高的准确率。也就是说，如果 $F_m$ 是一个弱学习器（其准确率仅略高于50%），那么我们可以通过上述过程提升其性能，使得最终的 $f$ 成为一个强学习器。（更多关于Boosting学习理论方法的细节可参见文献[SF12]。）

注意，Boosting通过拟合相互依赖的树来降低强学习器的偏差，而Bagging和RF通过拟合独立的树来降低方差。在很多情况下，Boosting能取得更好的效果。示例见图18.5。

原始的Boosting算法专注于二分类，使用一个特定的损失函数，我们将在第18.5.3节解释，它源于PAC学习理论框架（见第5.4.4节）。在本节的剩余部分，我们将关注一种更具统计意义的Boosting版本，它由[FHT00; Fri01]提出，适用于任意损失函数，从而使该方法适用于回归、多类分类、排序等。我们的阐述基于[HTF09, ch10]和[BH07]，详细信息可参考这些文献。

#### 18.5.1 前向分步加性建模

在本节中，我们讨论前向分步加性建模，该方法针对一般的（可微）损失函数，序贯地优化方程(18.16)中的目标函数，其中 $f$ 是一个如方程(18.15)所示的加性模型。具体地，在第 $m$ 次迭代中，我们计算

$$  (\beta_{m},\boldsymbol{\theta}_{m})=\underset{\beta,\boldsymbol{\theta}}{\mathrm{a r g m i n}}\sum_{i=1}^{N}\ell(y_{i},f_{m-1}(\boldsymbol{x}_{i})+\beta F(\boldsymbol{x}_{i};\boldsymbol{\theta}))   \tag*{(18.17)}$$

然后设置

$$  f_{m}(\boldsymbol{x})=f_{m-1}(\boldsymbol{x})+\beta_{m}F(\boldsymbol{x};\boldsymbol{\theta}_{m})=f_{m-1}(\boldsymbol{x})+\beta_{m}F_{m}(\boldsymbol{x})   \tag*{(18.18)}$$

（注意，我们不会调整先前添加模型的参数。）如何执行这一优化步骤的细节取决于我们选择的损失函数，并且在某些情况下还取决于弱学习器 $F$ 的形式，我们将在下文讨论。

#### 18.5.2 二次损失与最小二乘提升

假设我们使用平方误差损失 $ \ell(y, \hat{y}) = (y - \hat{y})^2 $。在这种情况下，第 $m$ 步目标函数中的第 $i'$ 项变为

$$  \ell(y_{i},f_{m-1}(\boldsymbol{x}_{i})+\beta F(\boldsymbol{x}_{i};\boldsymbol{\theta}))=(y_{i}-f_{m-1}(\boldsymbol{x}_{i})-\beta F(\boldsymbol{x}_{i};\boldsymbol{\theta}))^{2}=(r_{i m}-\beta F(\boldsymbol{x}_{i};\boldsymbol{\theta}))^{2}   \tag*{(18.19)}$$

其中 $ r_{im} = y_i - f_{m-1}(\boldsymbol{x}_i) $ 是当前模型在第 $i'$ 个观测上的残差。我们可以通过简单设置 $ \beta = 1 $ 并将 $F$ 拟合到残差上来最小化上述目标函数。这被称为最小二乘提升 [BY03]。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_289_120_869_690.jpg" alt="图像" width="50%" /></div>

<div style="text-align: center;">图 18.6：使用深度为2的回归树对一维数据集进行提升的示意图。改编自[Gér19]的图7.9。由 boosted_regr_trees.ipynb 生成。</div>

我们在图18.6中给出了这一过程的一个示例，其中使用深度为2的回归树作为弱学习器。左侧展示了将弱学习器拟合到残差的结果，右侧展示了当前强学习器。我们可以看到，每个加入集成的新弱学习器如何修正先前模型版本所犯的错误。

#### 18.5.3 指数损失与AdaBoost

假设我们关注二元分类问题，即预测 $\tilde{y}_i \in \{-1, +1\}$。假设弱学习器计算

$$  p(y=1|\boldsymbol{x})=\frac{e^{F(\boldsymbol{x})}}{e^{-F(\boldsymbol{x})}+e^{F(\boldsymbol{x})}}=\frac{1}{1+e^{-2F(\boldsymbol{x})}}   \tag*{(18.20)}$$

因此 $F(\boldsymbol{x})$ 返回对数几率的一半。根据式(10.13)可知，负对数似然为

$$  \ell(\tilde{y},F(\pmb{x}))=\log(1+e^{-2\tilde{y}F(\pmb{x})})   \tag*{(18.21)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND许可证

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_416_152_741_393.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 18.7：二分类中各种损失函数的示意图。横轴为间隔 $ m(\mathbf{x}) = \tilde{y}F(\mathbf{x}) $，纵轴为损失值。对数损失使用以2为底的对数。由 hinge_loss_plot.ipynb 生成。</div>


我们可以通过确保间隔 $ m(\boldsymbol{x}) = \tilde{y} F(\boldsymbol{x}) $ 尽可能大来最小化损失。从图 18.7 中可以看出，对数损失是 0-1 损失的一个平滑上界。同时，它也如预期地更重地惩罚负间隔（因为正间隔已被正确分类）。

然而，我们也可以使用其他损失函数。在本节中，我们考虑指数损失

$$  \ell(\tilde{y},F(\pmb{x}))=\exp(-\tilde{y}F(\pmb{x}))   \tag*{(18.22)}$$

从图 18.7 中可以看出，这也是 0-1 损失的一个平滑上界。在总体设定下（无限样本量），指数损失的最优解与对数损失相同。为说明这一点，我们令期望损失（对每个 $\mathbf{x}$）的导数为零：

$$  \frac{\partial}{\partial F(\boldsymbol{x})}\mathbb{E}\left[e^{-\tilde{y}f(\boldsymbol{x})}|\boldsymbol{x}\right]=\frac{\partial}{\partial F(\boldsymbol{x})}[p(\tilde{y}=1|\boldsymbol{x})e^{-F(\boldsymbol{x})}+p(\tilde{y}=-1|\boldsymbol{x})e^{F(\boldsymbol{x})}]   \tag*{(18.23)}$$

$$  =-p(\tilde{y}=1|\boldsymbol{x})e^{-F(\boldsymbol{x})}+p(\tilde{y}=-1|\boldsymbol{x})e^{F(\boldsymbol{x})}   \tag*{(18.24)}$$

$$  =0\Rightarrow\frac{p(\tilde{y}=1|\boldsymbol{x})}{p(\tilde{y}=-1|\boldsymbol{x})}=e^{2F(\boldsymbol{x})}   \tag*{(18.25)}$$

然而，在提升方法（boosting）的背景下，指数损失更易于优化，如下所示（我们在 18.5.4 节讨论对数损失情况）。

下面我们讨论在使用指数损失时，如何求解第 $m$ 个弱学习器 $F_m$。我们假定基分类器 $F_m$ 返回一个二值类别标签；由此得到的算法称为离散 AdaBoost [FHT00]。如果 $F_m$ 返回的是概率，则可以使用一种改进的算法，即实值 AdaBoost [FHT00]。

在第 m 步，我们需要最小化

$$  L_{m}(F)=\sum_{i=1}^{N}\exp[-\tilde{y}_{i}(f_{m-1}(\boldsymbol{x}_{i})+\beta F(\boldsymbol{x}_{i}))]=\sum_{i=1}^{N}\omega_{i,m}\exp(-\beta\tilde{y}_{i}F(\boldsymbol{x}_{i}))   \tag*{(18.26)}$$

---

其中 $ \omega_{i,m} \triangleq \exp(-\tilde{y}_i f_{m-1}(\boldsymbol{x}_i)) $ 是应用于数据样本 $ i $ 的权重，且 $ \tilde{y}_i \in \{-1, +1\} $。我们可以将该目标函数重写如下：

$$  \begin{align*}L_{m}&=e^{-\beta}\sum_{\tilde{y}_{i}=F(\boldsymbol{x}_{i})}\omega_{i,m}+e^{\beta}\sum_{\tilde{y}_{i}\neq F(\boldsymbol{x}_{i})}\omega_{i,m}\\&=(e^{\beta}-e^{-\beta})\sum_{i=1}^{N}\omega_{i,m}\mathbb{I}\left(\tilde{y}_{i}\neq F(\boldsymbol{x}_{i})\right)+e^{-\beta}\sum_{i=1}^{N}\omega_{i,m}\end{align*}   \tag*{(18.28)}$$

因此，需要添加的最佳函数为

$$  F_{m}=\underset{F}{\mathrm{a r g m i n}}\sum_{i=1}^{N}\omega_{i,m}\mathbb{I}\left(\tilde{y}_{i}\neq F(\boldsymbol{x}_{i})\right)   \tag*{(18.29)}$$

这可以通过将弱学习器应用于数据集的加权版本（权重为 $ \omega_{i,m} $）来得到。

剩下的问题就是求解更新的步长 $ \beta $。将 $ F_{m} $ 代入 $ L_{m} $ 并求解 $ \beta $，可得

$$  \beta_{m}=\frac{1}{2}\log\frac{1-\mathrm{err}_{m}}{\mathrm{err}_{m}}   \tag*{(18.30)}$$

其中

$$  \mathrm{err}_{m}=\frac{\sum_{i=1}^{N}\omega_{i,m}\mathbb{I}\left(\tilde{y}_{i}\neq F_{m}(\boldsymbol{x}_{i})\right)}{\sum_{i=1}^{N}\omega_{i,m}}   \tag*{(18.31)}$$

因此，整体更新变为

$$  f_{m}(\boldsymbol{x})=f_{m-1}(\boldsymbol{x})+\beta_{m}F_{m}(\boldsymbol{x})   \tag*{(18.32)}$$

在更新强学习器之后，需要重新计算下一轮迭代的权重，如下所示：

$$  \omega_{i,m+1}=e^{-\tilde{y}_{i}f_{m}(\boldsymbol{x}_{i})}=e^{-\tilde{y}_{i}f_{m-1}(\boldsymbol{x}_{i})-\tilde{y}_{i}\beta_{m}F_{m}(\boldsymbol{x}_{i})}=\omega_{i,m}e^{-\tilde{y}_{i}\beta_{m}F_{m}(\boldsymbol{x}_{i})}   \tag*{(18.33)}$$

如果 $ \tilde{y}_i = F_m(\boldsymbol{x}_i) $，则 $ \tilde{y}_i F_m(\boldsymbol{x}_i) = 1 $；如果 $ \tilde{y}_i \neq F_m(\boldsymbol{x}_i) $，则 $ \tilde{y}_i F_m(\boldsymbol{x}_i) = -1 $。因此 $ -\tilde{y}_i F_m(\boldsymbol{x}_i) = 2\mathbb{I}(\tilde{y}_i \neq F_m(\boldsymbol{x}_i)) - 1 $，所以权重更新变为

$$  \omega_{i,m+1}=\omega_{i,m}e^{\beta_{m}\left(2\mathbb{I}(\bar{y}_{i}\neq F_{m}(\boldsymbol{x}_{i}))-1\right)}=\omega_{i,m}e^{2\beta_{m}\mathbb{I}(\bar{y}_{i}\neq F_{m}(\boldsymbol{x}_{i}))}e^{-\beta_{m}}   \tag*{(18.34)}$$

由于 $ e^{-\beta_m} $ 对所有样本都是常数，因此可以省略。如果定义 $ \alpha_m = 2\beta_m $，则更新变为

$$  \omega_{i,m+1}=\begin{cases}\omega_{i,m}e^{\alpha_{m}}&\text{若 } \tilde{y}_{i}\neq F_{m}(\boldsymbol{x}_{i})\\\omega_{i,m}&\text{否则}\end{cases}   \tag*{(18.35)}$$

由此可见，我们以指数方式增加了错分样本的权重。由此得到的算法如算法 18.1 所示，称为 Adaboost.M1 [FS96]。

指数损失的多分类推广以及一种类似于 AdaBoost 的极小化算法，称为 SAMME（使用多分类指数损失函数的逐阶段加性建模），在 [Has+09] 中有所描述。该算法已在 scikit-learn 中实现（AdaBoostClassifier 类）。

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可协议。

---

算法 18.1: Adaboost.M1 —— 用于二分类的指数损失

1 初始化权重 $\omega_{i}=1/N$

2 for $m=1$ 到 $M$ do

3  $\begin{cases} \text{使用权重 } \boldsymbol{w} \text{ 在训练集上拟合分类器 } F_{m}(\boldsymbol{x}) \\ \text{计算 } \text{err}_{m}=\frac{\sum_{i=1}^{N} \omega_{i,m} \mathbb{I}(\tilde{y}_{i} \neq F_{m}(\boldsymbol{x}_{i}))}{\sum_{i=1}^{N} \omega_{i,m}} \\ \text{计算 } \alpha_{m}=\log[(1-\text{err}_{m})/\text{err}_{m}] \\ \text{更新 } \omega_{i} \leftarrow \omega_{i} \exp[\alpha_{m} \mathbb{I}(\tilde{y}_{i} \neq F_{m}(\boldsymbol{x}_{i}))] \end{cases} $

7 返回 $f(\boldsymbol{x})=\text{sgn}\left[\sum_{m=1}^{M} \alpha_{m} F_{m}(\boldsymbol{x})\right]$

#### 18.5.4 LogitBoost

指数损失的麻烦在于它对误分类样本施加了过大的权重，这一点从图 18.7 左侧的指数爆炸可以清楚看出。这使得该方法对异常值（错误标注的样本）非常敏感。此外，$e^{-\tilde{y}f}$ 并不是二值变量 $\tilde{y} \in \{-1, +1\}$ 的任何 pmf（概率质量函数）的对数，因此我们无法从 $f(\mathbf{x})$ 中恢复概率估计。

一个自然的替代方案是使用对数损失（log loss），正如我们在第 18.5.3 节中讨论的那样。从图 18.7 中可以清楚地看到，对数损失仅对错误进行线性惩罚。此外，这意味着我们将能够从最终学习到的函数中提取概率，其形式为

$$ p(y=1|\boldsymbol{x})=\frac{e^{f(\boldsymbol{x})}}{e^{-f(\boldsymbol{x})}+e^{f(\boldsymbol{x})}}=\frac{1}{1+e^{-2f(\boldsymbol{x})}} \tag*{(18.36)}$$

目标是使期望的对数损失最小化，其表达式为

$$ L_{m}(F)=\sum_{i=1}^{N}\log\left[1+\exp\left(-2\tilde{y}_{i}(f_{m-1}(\boldsymbol{x})+F(\boldsymbol{x}_{i}))\right)\right] \tag*{(18.37)}$$

通过对该目标进行牛顿更新（类似于 IRLS（迭代重加权最小二乘法）），可以推导出算法 18.2 所示的算法。这被称为 logitBoost [FHT00]。其关键子程序是弱学习器 $F$ 能够解决一个加权最小二乘问题。该方法可以推广到多类设定，详见 [FHT00]。

#### 18.5.5 梯度提升（Gradient boosting）

与其针对每个不同的损失函数推导新的提升版本，不如推导一个通用版本，称为梯度提升 [Fri01; Mas+00]。为解释这一点，设想在函数空间中执行梯度下降来求解 $\hat{f} = \argmin_f \mathcal{L}(f)$。由于函数是无限维对象，我们通过它们在训练集上的值 $\boldsymbol{f} = (f(\boldsymbol{x}_1), \ldots, f(\boldsymbol{x}_N))$ 来表示它们。在第 $m$ 步，令 $g_m$ 为 $\mathcal{L}(f)$ 在 $\boldsymbol{f} = \boldsymbol{f}_{m-1}$ 处的梯度：

$$ g_{i m}=\left[\frac{\partial\ell(y_{i},f(\boldsymbol{x}_{i}))}{\partial f(\boldsymbol{x}_{i})}\right]_{f=f_{m-1}} \tag*{(18.38)}$$

---

算法 18.2：LogitBoost，用于对数损失的二分类

1  $ \omega_i = 1/N $,  $ \pi_i = 1/2 $

2  for  $ m = 1:M $ do

3  $ \begin{cases} \text{计算工作响应 } z_i = \frac{y_i^* - \pi_i}{\pi_i(1 - \pi_i)} \\ \text{计算权重 } \omega_i = \pi_i(1 - \pi_i) \\ F_m = \arg\min_F \sum_{i=1}^N \omega_i(z_i - F(\boldsymbol{x}_i))^2 \\ \text{更新 } f(\boldsymbol{x}) \leftarrow f(\boldsymbol{x}) + \frac{1}{2}F_m(\boldsymbol{x}) \\ \text{计算 } \pi_i = 1/(1 + \exp(-2f(\boldsymbol{x}_i))); \end{cases} $

4  $ \begin{cases} \text{更新 } f(\boldsymbol{x}) \leftarrow f(\boldsymbol{x}) + \frac{1}{2}F_m(\boldsymbol{x}) \\ \text{计算 } \pi_i = 1/(1 + \exp(-2f(\boldsymbol{x}_i))); \end{cases} $

5  $ \begin{cases} \text{返回 } f(\boldsymbol{x}) = \text{sgn} \left[\sum_{m=1}^M F_m(\boldsymbol{x})\right] \\ \text{名称} \quad \text{损失} \quad -\partial\ell(y_i, f(\boldsymbol{x}_i))/ \partial f(\boldsymbol{x}_i) \\ \text{平方误差} \quad \frac{1}{2}(y_i - f(\boldsymbol{x}_i))^2 \quad y_i - f(\boldsymbol{x}_i) \\ \text{绝对误差} \quad |y_i - f(\boldsymbol{x}_i)| \quad \text{sgn}(y_i - f(\boldsymbol{x}_i)) \\ \text{指数损失} \quad \exp(-\tilde{y}_i f(\boldsymbol{x}_i)) \quad -\tilde{y}_i \exp(-\tilde{y}_i f(\boldsymbol{x}_i)) \\ \text{二分类对数损失} \quad \log(1 + e^{-\tilde{y}_i f_i}) \quad y_i - \pi_i \\ \text{多分类对数损失} \quad -\sum_c y_ic \log \pi_{ic} \quad y_{ic} - \pi_{ic} \end{cases} $

<div style="text-align: center;">表 18.1：一些常用损失函数及其梯度。对于二分类问题，我们假设  $ \tilde{y}_i \in \{-1, +1\} $，且  $ \pi_i = \sigma(2f(\mathbf{x}_i)) $。对于回归问题，我们假设  $ y_i \in \mathbb{R} $。改编自 [HTF09, p360] 和 [BH07, p483]。</div>

一些常见损失函数的梯度如表 18.1 所示。然后我们进行如下更新

$$  f_{m}=f_{m-1}-\beta_{m}g_{m}   \tag*{(18.39)}$$

其中 $ \beta_{m} $ 是步长，通过下式确定

$$  \beta_{m}=\underset{\beta}{\mathrm{a r g m i n}}\mathcal{L}(\boldsymbol{f}_{m-1}-\beta\boldsymbol{g}_{m})   \tag*{(18.40)}$$

在目前的形式下，这并没有太大用处，因为它只优化了固定 N 个点上的 f，因此我们无法学习到一个能够泛化的函数。不过，我们可以通过拟合一个弱学习器来近似负梯度信号，从而修改该算法。也就是说，我们使用以下更新

$$  F_{m}=\underset{F}{\arg\min}\sum_{i=1}^{N}(-g_{i m}-F(\boldsymbol{x}_{i}))^{2}   \tag*{(18.41)}$$

整个算法总结在算法 18.3 中。我们省略了针对 $ \beta_m $ 的线性搜索步骤，如 [BH07] 所述，该步骤并非严格必要。然而，我们引入了学习率或收缩因子 $ 0 < \nu \leq 1 $，以控制更新的大小，用于正则化目的。

如果我们使用平方损失来应用该算法，则会得到 L2Boosting，因为 $ -g_{im} = y_i - f_{m-1}(\boldsymbol{x}_i) $ 正是残差误差。我们也可以将该算法应用于其他损失函数，例如绝对损失或 Huber 损失（第 5.1.5.3 节），这对于稳健回归问题十分有用。

---

算法18.3：梯度提升

1 初始化 $f_0(\boldsymbol{x}) = \argmin_F \sum_{i=1}^N L(y_i, F(\boldsymbol{x}_i))$

2 for $m = 1 : M$ do

3  $\begin{cases} \text{使用 } r_{im} = -\left[\frac{\partial L(y_i, f(\boldsymbol{x}_i))}{\partial f(\boldsymbol{x}_i)}\right]_{f(\boldsymbol{x}_i) = f_{m-1}(\boldsymbol{x}_i)} \text{ 计算梯度残差} \\ \text{使用弱学习器计算 } F_m = \argmin_F \sum_{i=1}^N (r_{im} - F(\boldsymbol{x}_i))^2 \\ \text{更新 } f_m(\boldsymbol{x}) = f_{m-1}(\boldsymbol{x}) + \nu F_m(\boldsymbol{x}) \end{cases}$

4  $\begin{cases} \text{更新 } f_m(\boldsymbol{x}) = f_{m-1}(\boldsymbol{x}) + \nu F_m(\boldsymbol{x}) \\ \end{cases}$

5  $\begin{cases} \text{返回 } f(\boldsymbol{x}) = f_M(\boldsymbol{x}) \end{cases}$

对于分类问题，我们可以使用对数损失。此时，得到一种称为二项式提升（BinomialBoost）的算法[BH07]。它相比 LogitBoost 的优势在于，不需要进行加权拟合：只需将任意黑箱回归模型直接应用于梯度向量。要将其应用于多分类问题，我们可以拟合 C 个独立的回归树，使用如下形式的伪残差：

$$ -g_{i c m}=\frac{\partial\ell(y_{i},f_{1m}(\boldsymbol{x}_{i}),\ldots,f_{C m}(\boldsymbol{x}_{i}))}{\partial f_{c m}(\boldsymbol{x}_{i})}=\mathbb{I}\left(y_{i}=c\right)-\pi_{i c} \tag*{(18.42)}$$

尽管树是分别拟合的，但其预测结果通过 softmax 变换进行组合：

$$ p(y=c|\boldsymbol{x})=\frac{e^{f_{c}(\boldsymbol{x})}}{\sum_{c^{\prime}=1}^{C}e^{f_{c^{\prime}}(\boldsymbol{x})}} \tag*{(18.43)}$$

当数据集较大时，我们可以使用随机化变体：在每次迭代中，对数据进行无放回的子采样，将随机抽取的一部分数据传递给回归树。这种方法称为**随机梯度提升**（stochastic gradient boosting）[Fri99]。它不仅速度更快，而且通常具有更好的泛化能力，因为子采样作为一种正则化手段发挥作用。

##### 18.5.5.1 梯度树提升

在实际应用中，梯度提升几乎总是假设弱学习器为回归树，其形式为：

$$ F_{m}(\boldsymbol{x})=\sum_{j=1}^{J_{m}}w_{jm}\mathbb{I}\left(\boldsymbol{x}\in R_{jm}\right) \tag*{(18.44)}$$

其中 $w_{jm}$ 是区域 $R_{jm}$ 的预测输出。（一般地，$w_{jm}$ 可以是一个向量。）这种组合称为**梯度提升回归树**（gradient boosted regression trees），或**梯度树提升**（gradient tree boosting）。（相关版本称为 MART，即“多元加性回归树”[FM03]。）

要在梯度提升中使用该模型，我们首先利用标准回归树学习（参见第18.1节）基于残差为第 m 棵树寻找合适的区域 $R_{jm}$；然后通过求解下式（重新）确定每个叶子节点的权重：

$$ \hat{w}_{jm}=\underset{w}{\arg\min}\sum_{\substack{\boldsymbol{x}_{i}\in R_{jm}}}\ell(y_{i},f_{m-1}(\boldsymbol{x}_{i})+w) \tag*{(18.45)}$$

---

对于平方误差（如梯度提升所使用的），最优权重 $\hat{w}_{jm}$ 就是该叶子节点中残差的均值。

##### 18.5.5.2 XGBoost

XGBoost（https://github.com/dmlc/xgboost）代表“极端梯度提升”，是一种非常高效且广泛使用的梯度提升树实现，它在第18.5.5.1节描述的基础上增加了若干改进。详细信息可参见[CG16]，但简要来说，其扩展包括：对树复杂度添加正则化项、使用损失函数的二阶近似（来自[FHT00]）而非仅线性近似、在内部节点处对特征进行采样（如同随机森林），以及利用多种计算机科学方法（例如处理大规模数据集的核外计算）来确保可扩展性。[^2]

更详细地，XGBoost优化以下正则化目标函数：

$$ \mathcal{L}(f)=\sum_{i=1}^{N}\ell(y_{i},f(\boldsymbol{x}_{i}))+\Omega(f)   \tag*{(18.46)} $$

其中

$$ \Omega(f)=\gamma J+\frac{1}{2}\lambda\sum_{j=1}^{J}w_{j}^{2}   \tag*{(18.47)} $$

是正则化项，$J$ 为叶子节点数，$\gamma \geq 0$ 和 $\lambda \geq 0$ 是正则化系数。在第 $m$ 步，损失函数为

$$ \mathcal{L}_{m}(F_{m})=\sum_{i=1}^{N}\ell(y_{i},f_{m-1}(\boldsymbol{x}_{i})+F_{m}(\boldsymbol{x}_{i}))+\Omega(F_{m})+\mathrm{const}   \tag*{(18.48)} $$

我们可以按如下方式进行二阶泰勒展开：

$$ \mathcal{L}_{m}(F_{m})\approx\sum_{i=1}^{N}\left[\ell(y_{i},f_{m-1}(\boldsymbol{x}_{i}))+g_{i m}F_{m}(\boldsymbol{x}_{i})+\frac{1}{2}h_{i m}F_{m}^{2}(\boldsymbol{x}_{i})\right]+\Omega(F_{m})+const   \tag*{(18.49)} $$

其中 $ h_{im} $ 是海森矩阵（Hessian）：

$$ h_{i m}=\left[\frac{\partial^{2}\ell(y_{i},f(\boldsymbol{x}_{i}))}{\partial f(\boldsymbol{x}_{i})^{2}}\right]_{f=f_{m-1}}   \tag*{(18.50)} $$

对于回归树，我们有 $ F(\boldsymbol{x}) = w_q(\boldsymbol{x}) $，其中 $ q : \mathbb{R}^D \to \{1, \ldots, J\} $ 指明 $\boldsymbol{x}$ 属于哪个叶子节点，$\boldsymbol{w} \in \mathbb{R}^J$ 为叶子权重。因此，我们可以将方程（18.49）重写为

---

接下来，我们忽略与 $F_m$ 无关的项：

$$  \begin{align*}\mathcal{L}_{m}(q,\boldsymbol{w})&\approx\sum_{i=1}^{N}\left[g_{im}F_{m}(\boldsymbol{x}_{i})+\frac{1}{2}h_{im}F_{m}^{2}(\boldsymbol{x}_{i})\right]+\gamma J+\frac{1}{2}\lambda\sum_{j=1}^{J}w_{j}^{2}\\&=\sum_{j=1}^{J}\left[(\sum_{i\in I_{j}}g_{im})w_{j}+\frac{1}{2}(\sum_{i\in I_{j}}h_{i}+\lambda)w_{j}^{2}\right]+\gamma J\end{align*}   \tag*{(18.51)}$$

其中 $ I_j = \{i : q(\boldsymbol{x}_i) = j\} $ 是被分配到第 $j$ 个叶子的数据点索引集合。

定义 $ G_{jm} = \sum_{i \in I_i} g_{im} $ 和 $ H_{jm} = \sum_{i \in I_i} h_{im} $，则上式可简化为：

$$  \mathcal{L}_{m}(q,\boldsymbol{w})=\sum_{j=1}^{J}\left[G_{j m}w_{j}+\frac{1}{2}(H_{j m}+\lambda)w_{j}^{2}\right]+\gamma J   \tag*{(18.53)}$$

对于每个 $w_{j}$ 这是一个二次函数，因此最优权重为：

$$  w_{j}^{*}=-\frac{G_{jm}}{H_{jm}+\lambda}   \tag*{(18.54)}$$

于是，用于评估不同树结构 $q$ 的损失函数变为：

$$  \mathcal{L}_{m}(q,\boldsymbol{w}^{*})=-\frac{1}{2}\sum_{j=1}^{J}\frac{G_{j m}^{2}}{H_{j m}+\lambda}+\gamma J   \tag*{(18.55)}$$

我们可以使用递归节点分裂过程（如第18.1节所述）来贪婪地优化该损失。具体而言，对于给定的叶子 $j$，我们考虑将其分裂为左右两部分，即 $ I = I_L \cup I_R $。这种分裂的增益（损失减少量）可计算如下：

$$  \mathrm{gain}=\frac{1}{2}\left[\frac{G_{L}^{2}}{H_{L}+\lambda}+\frac{G_{R}^{2}}{H_{R}+\lambda}-\frac{(G_{L}+G_{R})^{2}}{(H_{L}+H_{R})+\lambda}\right]-\gamma   \tag*{(18.56)}$$

其中 $ G_L = \sum_{i \in I_L} g_{im} $，$ G_R = \sum_{i \in I_R} g_{im} $，$ H_L = \sum_{i \in I_L} h_{im} $，$ H_R = \sum_{i \in I_R} h_{im} $。由此可知，如果增益为负（即第一项小于 $\gamma$），则分裂该节点是不值得的。

一种用于评估该目标的快速近似方法（无需对特征进行排序来选择最优分裂阈值）在 [CG16] 中进行了描述。

### 18.6 解释树集成

树模型因可解释性强而受欢迎。不幸的是，树集成（无论是装袋、随机森林还是提升方法）却丧失了这一特性。幸运的是，我们可以使用一些简单方法来解释已经学到的函数。