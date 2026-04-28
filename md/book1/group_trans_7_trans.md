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

第二部分 线性模型

---

请提供需要翻译的英文 Markdown 文本内容，我将严格按照您的要求进行专业学术翻译。

---

# 9 线性判别分析

### 9.1 引言

本章考虑如下形式的分类模型：

$$ p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\frac{p(\boldsymbol{x}|y=c,\boldsymbol{\theta})p(y=c|\boldsymbol{\theta})}{\sum_{c^{\prime}}p(\boldsymbol{x}|y=c^{\prime},\boldsymbol{\theta})p(y=c^{\prime}|\boldsymbol{\theta})} \tag*{(9.1)} $$

项 $p(y = c|\theta)$ 是类别标签的先验概率，项 $p(\boldsymbol{x}|y = c,\boldsymbol{\theta})$ 称为类别 $c$ 的**类别条件密度**。

整体模型称为生成式分类器，因为它通过从 $p(\boldsymbol{x}|y=c,\boldsymbol{\theta})$ 中采样，为每个类别 $c$ 指定了一种生成特征 $\boldsymbol{x}$ 的方式。相比之下，判别式分类器直接对类别后验 $p(y|\boldsymbol{x},\boldsymbol{\theta})$ 进行建模。我们将在第 9.4 节讨论这两种分类方法的优缺点。

如果以特殊方式选择类别条件密度，我们会发现类别上的后验概率是 $\boldsymbol{x}$ 的线性函数，即 $\log p(y = c|\boldsymbol{x}, \boldsymbol{\theta}) = \boldsymbol{w}^{\mathrm{T}} \boldsymbol{x} + \mathrm{const}$，其中 $\boldsymbol{w}$ 由 $\boldsymbol{\theta}$ 导出。因此，该方法整体上被称为线性判别分析（Linear Discriminant Analysis）或 LDA。$^{1}$

### 9.2 高斯判别分析

本节考虑一种生成式分类器，其中类别条件密度为多元高斯分布：

$$ p(\boldsymbol{x}|y=c,\boldsymbol{\theta})=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{c},\boldsymbol{\Sigma}_{c}) \tag*{(9.2)} $$

相应的类别后验概率形式为

$$ p(y=c|\boldsymbol{x},\boldsymbol{\theta})\propto\pi_{c}\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{c},\boldsymbol{\Sigma}_{c}) \tag*{(9.3)} $$

其中 $\pi_c = p(y = c|\boldsymbol{\theta})$ 是标签 $c$ 的先验概率。（注意，我们可以忽略后验概率分母中的归一化常数，因为它与 $c$ 无关。）我们将此模型称为高斯判别分析（Gaussian Discriminant Analysis）或 GDA。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_270_124_479_332.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_679_125_886_330.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 9.1: (a) 来自三个不同类别的二维数据。 (b) 对每个类别拟合二维高斯分布。由 discrim_analysis_dboundaries_plot2.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_276_459_473_667.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_684_459_881_667.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 9.2: 对图 9.1 中数据拟合的高斯判别分析。 (a) 无约束协方差导致二次决策边界。 (b) 绑定协方差导致线性决策边界。由 discrim_analysis_dboundaries_plot2.ipynb 生成。</div>


#### 9.2.1 二次决策边界

由 Equation (9.3)，我们看到类别标签的对数后验由下式给出：

$$  \log p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\log\pi_{c}-\frac{1}{2}\log\left|2\pi\boldsymbol{\Sigma}_{c}\right|-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu}_{c})^{\top}\boldsymbol{\Sigma}_{c}^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_{c})+\mathrm{c o n s t}   \tag*{(9.4)}$$

这被称为判别函数。我们注意到，任意两个类别（比如 c 和 \(c'\)）之间的决策边界将是 x 的二次函数。因此，这被称为二次判别分析（QDA）。

例如，考虑图 9.1a 中来自三个不同类别的二维数据。我们拟合全协方差高斯类条件分布（使用第 9.2.4 节介绍的方法），并将结果绘制在图 9.1b 中。我们看到蓝色类别的特征具有一定的相关性，而绿色类别的特征是独立的，红色类别的特征是独立的且各向同性（球面协方差）。在图 9.2a 中，我们看到由此产生的决策边界是 x 的二次函数。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_457_117_706_336.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">图 9.3: 两类情况下 LDA 的几何表示，其中 $ \Sigma_1 = \Sigma_2 = \mathbf{I} $。</div>


#### 9.2.2 线性决策边界

现在我们考虑高斯判别分析的一个特例，其中协方差矩阵在各个类别之间是绑定或共享的，即 $ \mathbf{\Sigma}_c = \mathbf{\Sigma} $。如果 $ \mathbf{\Sigma} $ 与 $ c $ 无关，我们可以将公式 (9.4) 简化如下：

$$  \log p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\log\pi_{c}-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu}_{c})^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_{c})+\mathrm{c o n s t}   \tag*{(9.5)}$$

$$  \begin{aligned}&=\underbrace{\log\pi_{c}-\frac{1}{2}\boldsymbol{\mu}_{c}^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_{c}}_{\gamma_{c}}+x^{\top}\underbrace{\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_{c}}_{\beta_{c}}+\underbrace{\mathrm{c o n s t}-\frac{1}{2}x^{\top}\boldsymbol{\Sigma}^{-1}x}_{\kappa}\\&=\gamma_{c}+x^{\top}\boldsymbol{\beta}_{c}+\kappa\end{aligned}   \tag*{(9.6)}$$

最后一项与 $ c $ 无关，因此是一个可以忽略的无关加性常数。由此我们看到判别函数是 $ \boldsymbol{x} $ 的线性函数，因此决策边界将是线性的。故该方法被称为线性判别分析或 LDA。参见 Figure 9.2b 的示例。

#### 9.2.3 LDA 与逻辑回归的联系

在本节中，我们推导出 LDA 与我们在 2.5.3 节介绍的逻辑回归之间的一个有趣联系。由公式 (9.7) 可以写出

$$  p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\frac{e^{\boldsymbol{\beta}_{c}^{\top}\boldsymbol{x}+\gamma_{c}}}{\sum_{c^{\prime}}e^{\boldsymbol{\beta}_{c^{\prime}}^{\top}\boldsymbol{x}+\gamma_{c^{\prime}}}}=\frac{e^{\boldsymbol{w}_{c}^{\top}[1,\boldsymbol{x}]}}{\sum_{c^{\prime}}e^{\boldsymbol{w}_{c^{\prime}}^{\top}[1,\boldsymbol{x}]}}   \tag*{(9.8)}$$

其中 $ \boldsymbol{w}_c = [\gamma_c, \boldsymbol{\beta}_c] $。我们看到公式 (9.8) 与多项逻辑回归模型具有相同的形式。关键区别在于，在 LDA 中，我们首先拟合高斯分布（以及类先验）以最大化联合似然 $ p(\boldsymbol{x}, y | \boldsymbol{\theta}) $，如 9.2.4 节所述，然后从 $ \boldsymbol{\theta} $ 推导出 $ \boldsymbol{w} $。相比之下，在逻辑回归中，我们直接估计 $ \boldsymbol{w} $ 以最大化条件似然 $ p(y | \boldsymbol{x}, \boldsymbol{w}) $。一般来说，这两者会给出不同的结果（参见练习 10.3）。

为了进一步理解公式 $ (9.8) $，我们考虑二分类情况。在这种情况下，

---

后验概率由下式给出

$$  \begin{aligned}p(y=1|\boldsymbol{x},\boldsymbol{\theta})&=\frac{e^{\boldsymbol{\beta}_{1}^{\mathrm{T}}\boldsymbol{x}+\gamma_{1}}}{e^{\boldsymbol{\beta}_{1}^{\mathrm{T}}\boldsymbol{x}+\gamma_{1}}+e^{\boldsymbol{\beta}_{0}^{\mathrm{T}}\boldsymbol{x}+\gamma_{0}}}=\frac{1}{1+e^{(\boldsymbol{\beta}_{0}-\boldsymbol{\beta}_{1})^{\mathrm{T}}\boldsymbol{x}+(\gamma_{0}-\gamma_{1})}}\\&=\sigma\left((\boldsymbol{\beta}_{1}-\boldsymbol{\beta}_{0})^{\mathrm{T}}\boldsymbol{x}+(\gamma_{1}-\gamma_{0})\right)\end{aligned}   \tag*{(9.9)}$$

其中 $ \sigma(\eta) $ 表示 sigmoid 函数。

现在

$$  \begin{aligned}\gamma_{1}-\gamma_{0}&=-\frac{1}{2}\boldsymbol{\mu}_{1}^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_{1}+\frac{1}{2}\boldsymbol{\mu}_{0}^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_{0}+\log(\pi_{1}/\pi_{0})\\&=-\frac{1}{2}(\boldsymbol{\mu}_{1}-\boldsymbol{\mu}_{0})^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_{1}+\boldsymbol{\mu}_{0})+\log(\pi_{1}/\pi_{0})\end{aligned}   \tag*{(9.11)}$$

因此，如果我们定义

$$  \boldsymbol{w}=\boldsymbol{\beta}_{1}-\boldsymbol{\beta}_{0}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_{1}-\boldsymbol{\mu}_{0})   \tag*{(9.13)}$$

$$  \boldsymbol{x}_{0}=\frac{1}{2}(\boldsymbol{\mu}_{1}+\boldsymbol{\mu}_{0})-(\boldsymbol{\mu}_{1}-\boldsymbol{\mu}_{0})\frac{\log(\pi_{1}/\pi_{0})}{(\boldsymbol{\mu}_{1}-\boldsymbol{\mu}_{0})^{\mathrm{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_{1}-\boldsymbol{\mu}_{0})}   \tag*{(9.14)}$$

那么我们有 $ \boldsymbol{w}^{\mathrm{T}}\boldsymbol{x}_{0}=-(\gamma_{1}-\gamma_{0}) $，因此

$$  p(y=1|\boldsymbol{x},\boldsymbol{\theta})=\sigma(\boldsymbol{w}^{\top}(\boldsymbol{x}-\boldsymbol{x}_{0}))   \tag*{(9.15)}$$

这与二元逻辑回归具有相同的形式。因此，最大后验（MAP）决策规则为

$$  \hat{y}(\boldsymbol{x})=1\mathrm{~i f f~}\boldsymbol{w}^{\top}\boldsymbol{x}>c   \tag*{(9.16)}$$

其中 c = wT x0。如果 π0 = π1 = 0.5，则阈值简化为 c = 1/2wT (μ1 + μ0)

为了从几何上解释这个方程，假设 $ \Sigma = \sigma^2 \mathbf{I} $。在这种情况下，$ \boldsymbol{w} = \sigma^{-2}(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_0) $，它平行于连接两个质心 $ \boldsymbol{\mu}_0 $ 和 $ \boldsymbol{\mu}_1 $ 的直线。因此，我们可以通过将点投影到这条直线上，然后检查投影点是否更接近 $ \boldsymbol{\mu}_0 $ 或 $ \boldsymbol{\mu}_1 $ 来对点进行分类，如图 9.3 所示。它需要多近取决于类别的先验。如果 $ \pi_1 = \pi_0 $，则 $ \boldsymbol{x}_0 = \frac{1}{2}(\boldsymbol{\mu}_1 + \boldsymbol{\mu}_0) $，即位于两个均值的中点。如果 $ \pi_1 > \pi_0 $，则必须比中点更接近 $ \boldsymbol{\mu}_0 $ 才能选择类别 0。反之亦然如果 $ \pi_0 > \pi_1 $。因此，我们看到类别先验只是改变了决策阈值，但没有改变决策边界的整体形状。（类似论证适用于多类情况。）

#### 9.2.4 模型拟合

我们现在讨论如何使用最大似然估计拟合高斯判别分析（GDA）模型。似然函数如下

$$  p(\mathcal{D}|\boldsymbol{\theta})=\prod_{n=1}^{N}\mathrm{Cat}(y_{n}|\boldsymbol{\pi})\prod_{c=1}^{C}\mathcal{N}(\boldsymbol{x}_{n}|\boldsymbol{\mu}_{c},\boldsymbol{\Sigma}_{c})^{\mathbb{I}(y_{n}=c)}   \tag*{(9.17)}$$

---

因此，对数似然函数为

$$  \log p(\mathcal{D}|\boldsymbol{\theta})=\left[\sum_{n=1}^{N}\sum_{c=1}^{C}\mathbb{I}\left(y_{n}=c\right)\log\pi_{c}\right]+\sum_{c=1}^{C}\left[\sum_{n:y_{n}=c}\log\mathcal{N}(\boldsymbol{x}_{n}|\boldsymbol{\mu}_{c},\boldsymbol{\Sigma}_{c})\right]   \tag*{(9.18)}$$

由此可见，我们可以分别优化 $\pi$ 项和 $(\boldsymbol{\mu}_c,\boldsymbol{\Sigma}_c)$ 项。

根据4.2.4节，类先验的MLE为 $\hat{\pi}_c = \frac{N_c}{N}$。利用4.2.6节的结果，我们可以推导高斯的MLE如下：

$$  \hat{\mu}_{c}=\frac{1}{N_{c}}\sum_{n:y_{n}=c}x_{n}   \tag*{(9.19)}$$

$$  \hat{\boldsymbol{\Sigma}}_{c}=\frac{1}{N_{c}}\sum_{n:y_{n}=c}(\boldsymbol{x}_{n}-\hat{\boldsymbol{\mu}}_{c})(\boldsymbol{x}_{n}-\hat{\boldsymbol{\mu}}_{c})^{\mathrm{T}}   \tag*{(9.20)}$$

遗憾的是，当 $N_c$ 相对于输入特征的维度 $D$ 较小时，$\hat{\Sigma}_c$ 的MLE很容易过拟合（即估计可能不具有良好的条件数）。下面我们将讨论一些解决方案。

##### 9.2.4.1 绑定协方差

如果我们强制 $\Sigma_c = \Sigma$ 为绑定协方差，则会得到线性决策边界，如前所述。这通常也能产生更可靠的参数估计，因为我们可以汇集所有类别的样本：

$$  \hat{\boldsymbol{\Sigma}}=\frac{1}{N}\sum_{c=1}^{C}\sum_{n:y_{n}=c}(\boldsymbol{x}_{n}-\hat{\boldsymbol{\mu}}_{c})(\boldsymbol{x}_{n}-\hat{\boldsymbol{\mu}}_{c})^{\mathsf{T}}   \tag*{(9.21)}$$

##### 9.2.4.2 对角协方差

如果强制 $\Sigma_c$ 为对角矩阵，则参数数量从 $O(CD^2)$ 减少到 $O(CD)$，从而避免了过拟合问题。然而，这失去了捕捉特征间相关性的能力。（这称为朴素贝叶斯假设，我们将在9.3节进一步讨论。）尽管存在这种近似，该方法能够很好地扩展到高维。

通过使用共享（绑定）对角协方差矩阵，我们可以进一步限制模型容量。这被称为“对角LDA”[BL04]。

##### 9.2.4.3 MAP估计

强制协方差矩阵为对角阵是一个相当强的假设。另一种方法是使用（共享的）全协方差高斯的MAP估计，而不是MLE。基于4.5.2节的结果，我们发现MAP估计为

$$  \hat{\mathbf{\Sigma}}_{\mathrm{m a p}}=\lambda\mathrm{d i a g}(\hat{\mathbf{\Sigma}}_{\mathrm{m l e}})+(1-\lambda)\hat{\mathbf{\Sigma}}_{\mathrm{m l e}}   \tag*{(9.22)}$$

其中 $\lambda$ 控制正则化程度。该技术称为正则化判别分析（Regularized Discriminant Analysis, RDA）[HTF09, p656]。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license.

---

#### 9.2.5 最近质心分类器

若假设类别上的先验为均匀分布，则最可能的类别标签可计算如下：

$$  \hat{y}(\boldsymbol{x})=\underset{c}{\operatorname{argmax}}\log p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\underset{c}{\operatorname{argmin}}(\boldsymbol{x}-\boldsymbol{\mu}_{c})^{\top}\boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_{c})   \tag*{(9.23)}$$

这被称为**最近质心分类器**（nearest centroid classifier），或最近类均值分类器（NCM），因为我们将 $\boldsymbol{x}$ 分配给离 $\boldsymbol{\mu}_c$ 最近的类别，其中距离用（平方）马氏距离度量。

我们可以将其替换为任意其他距离度量，从而得到决策规则：

$$  \hat{y}(\boldsymbol{x})=\underset{c}{\mathrm{a r g m i n}}d^{2}(\boldsymbol{x},\boldsymbol{\mu}_{c})   \tag*{(9.24)}$$

我们将在第16.2节讨论如何学习距离度量，但一种简单的方法是使用：

$$  d^{2}(\boldsymbol{x},\boldsymbol{\mu}_{c})=||\boldsymbol{x}-\boldsymbol{\mu}_{c}||_{\mathbf{W}}^{2}=(\boldsymbol{x}-\boldsymbol{\mu}_{c})^{\top}(\mathbf{W}\mathbf{W}^{\top})(\boldsymbol{x}-\boldsymbol{\mu}_{c})=||\mathbf{W}(\boldsymbol{x}-\boldsymbol{\mu}_{c})||^{2}   \tag*{(9.25)}$$

相应的类别后验变为：

$$  p(y=c|\boldsymbol{x},\boldsymbol{\mu},\mathbf{W})=\frac{\exp(-\frac{1}{2}||\mathbf{W}(\boldsymbol{x}-\boldsymbol{\mu}_{c})||_{2}^{2})}{\sum_{c^{\prime}=1}^{C}\exp(-\frac{1}{2}||\mathbf{W}(\boldsymbol{x}-\boldsymbol{\mu}_{c^{\prime}})||_{2}^{2})}   \tag*{(9.26)}$$

我们可以对判别损失使用梯度下降来优化 $\mathbf{W}$。这称为**最近类均值度量学习**（nearest class mean metric learning）[Men+12]。该技术的优势在于可用于新类别的单样本学习（one-shot learning），因为只需每类看到一个带标签的原型 $\boldsymbol{\mu}_c$ 即可（假设我们已经学到了一个好的 $\mathbf{W}$）。

#### 9.2.6 Fisher线性判别分析 *

判别分析（discriminant analysis）是一种生成式分类方法，需要对特征拟合多元正态分布（MVN）。如前所述，在高维空间中这可能导致问题。另一种方法是降低特征 $\boldsymbol{x} \in \mathbb{R}^D$ 的维度，然后对得到的低维特征 $\boldsymbol{z} \in \mathbb{R}^K$ 拟合 MVN。最简单的方法是使用线性投影矩阵 $\boldsymbol{z} = \boldsymbol{W}\boldsymbol{x}$，其中 $\boldsymbol{W}$ 是一个 $K \times D$ 的矩阵。寻找 $\boldsymbol{W}$ 的一种方法是使用主成分分析（PCA，第20.1节）。然而，PCA 是一种无监督技术，未考虑类别标签。因此所得的低维特征未必对分类最优，如图 9.4 所示。

另一种方法是使用基于梯度的方法优化对数似然，该似然来源于低维空间中的类别后验，如第9.2.5节所述。

第三种方法（依赖于特征分解而非基于梯度的优化器）是寻找矩阵 $\mathbf{W}$，使得低维数据在使用高斯类条件密度模型时能够尽可能好地被分类。高斯性假设是合理的，因为我们计算的是（可能非高斯的）特征的线性组合。这种方法称为 **Fisher线性判别分析**（Fisher's linear discriminant analysis，FLDA）。

FLDA 是判别式技术与生成式技术的一种有趣混合。该技术的缺点在于，无论 $D$ 多大，它只能用 $K \leq C - 1$ 维，原因将在下文解释。在两类情况下，这意味着我们寻求单个向量 $\pmb{w}$，数据可投影到其上。下面推导两类情况下的最优 $\pmb{w}$。然后将其推广到多类情况，最后给出该技术的概率解释。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_254_142_500_329.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_663_142_909_329.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_258_380_501_576.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_666_379_908_576.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图9.4：对二维两类数据集（表示男性和女性成人的（标准化）身高和体重）应用线性判别分析。(a) PCA方向。(b) FLDA方向。(c) 投影到PCA方向显示出较差的类别分离性。(d) 投影到FLDA方向显示出良好的类别分离性。由 fisher_lda_demo.ipynb 生成。</div>


##### 9.2.6.1 最优一维投影的推导

现在，我们针对两类情况推导这一最优方向 \( \boldsymbol{w} \)，遵循 [Bis06, Sec 4.1.4] 的论述。定义类条件均值如下：

$$  \mu_{1}=\frac{1}{N_{1}}\sum_{n:y_{n}=1}x_{n},\mu_{2}=\frac{1}{N_{2}}\sum_{n:y_{n}=2}x_{n}   \tag*{(9.27)}$$

设 \( m_k = \boldsymbol{w}^\top \boldsymbol{\mu}_k \) 为每个均值在直线 \( \boldsymbol{w} \) 上的投影。同时，设 \( z_n = \boldsymbol{w}^\top \boldsymbol{x}_n \) 为数据在该直线上的投影。投影点的方差与下式成正比：

$$  s_{k}^{2}=\sum_{n:y_{n}=k}\left(z_{n}-m_{k}\right)^{2}   \tag*{(9.28)}$$

目标是找到 \( \boldsymbol{w} \)，使得在最大化均值之间距离 \( m_{2} - m_{1} \) 的同时，确保投影后的簇是“紧凑”的，这可以通过最小化其方差来实现。由此提出以下目标函数：

$$  J(\boldsymbol{w})=\frac{(m_{2}-m_{1})^{2}}{s_{1}^{2}+s_{2}^{2}}   \tag*{(9.29)}$$

作者：Kevin P. Murphy。 (C) 麻省理工学院出版社。 CC-BY-NC-ND 许可协议。

---

我们可以将上述等式右边用 \(\boldsymbol{w}\) 重写如下：

$$  J(\boldsymbol{w})=\frac{\boldsymbol{w}^{\top}\mathbf{S}_{B}\boldsymbol{w}}{\boldsymbol{w}^{\top}\mathbf{S}_{W}\boldsymbol{w}}   \tag*{(9.30)}$$

其中 \(\mathbf{S}_{B}\) 是类间散度矩阵，定义为

$$  \mathbf{S}_{B}=(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})^{\mathrm{T}}   \tag*{(9.31)}$$

而 \(\mathbf{S}_{W}\) 是类内散度矩阵，定义为

$$  \mathbf{S}_{W}=\sum_{n:y_{n}=1}(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{1})(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{1})^{\top}+\sum_{n:y_{n}=2}(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{2})(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{2})^{\top}   \tag*{(9.32)}$$

为了说明这一点，注意到

$$  \boldsymbol{w}^{\mathsf{T}}\mathbf{S}_{B}\boldsymbol{w}=\boldsymbol{w}^{\mathsf{T}}(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})^{\mathsf{T}}\boldsymbol{w}=(m_{2}-m_{1})(m_{2}-m_{1})   \tag*{(9.33)}$$

以及

$$  \begin{aligned}\boldsymbol{w}^{\mathsf{T}}\mathbf{S}_{W}\boldsymbol{w}&=\sum_{n:y_{n}=1}\boldsymbol{w}^{\mathsf{T}}(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{1})(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{1})^{\mathsf{T}}\boldsymbol{w}+\\&\sum_{n:y_{n}=2}\boldsymbol{w}^{\mathsf{T}}(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{2})(\boldsymbol{x}_{n}-\boldsymbol{\mu}_{2})^{\mathsf{T}}\boldsymbol{w}\\&=\sum_{n:y_{n}=1}(z_{n}-m_{1})^{2}+\sum_{n:y_{n}=2}(z_{n}-m_{2})\end{aligned}   \tag*{(9.34)}$$

式 (9.30) 是两个标量的比值；我们可以对其关于 \(\boldsymbol{w}\) 求导并令其为零。可以证明（见习题 9.1），当

$$  \mathbf{S}_{B}w=\lambda\mathbf{S}_{W}w   \tag*{(9.36)}$$

时，\(J(\boldsymbol{w})\) 取得最大值，其中

$$  \lambda=\frac{w^{\top}\mathbf{S}_{B}w}{w^{\top}\mathbf{S}_{W}w}   \tag*{(9.37)}$$

式 (9.36) 称为广义特征值问题。如果 \(\mathbf{S}_{W}\) 可逆，我们可以将其转换为标准特征值问题：

$$  \mathbf{S}_{W}^{-1}\mathbf{S}_{B}w=\lambda w   \tag*{(9.38)}$$

然而，在二类情况下存在一个更简单的解。特别地，由于

$$  \mathbf{S}_{B}w=(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})^{\top}w=(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})(m_{2}-m_{1})   \tag*{(9.39)}$$

因此由式 (9.38) 可得

$$  \lambda w=\mathbf{S}_{W}^{-1}(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})(m_{2}-m_{1})   \tag*{(9.40)}$$

$$  w\propto\mathbf{S}_{W}^{-1}(\mu_{2}-\mu_{1})   \tag*{(9.41)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_218_137_538_395.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_614_138_947_394.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图9.5：(a) 元音数据的PCA（主成分分析）投影到二维空间。(b) 元音数据的FLDA（Fisher线性判别分析）投影到二维空间。我们可以看到FLDA情况下的类别分离更好。改编自[HTF09]的图4.11。由fisher_discrim_vowel.ipynb生成。</div>


由于我们只关心方向性，而不关心尺度因子，因此我们可以设

$$  w=\mathbf{S}_{W}^{-1}(\mu_{2}-\mu_{1})   \tag*{(9.42)}$$

这就是两类情况下的最优解。如果 \( \mathbf{S}_W \propto \mathbf{I} \)，即合并协方差矩阵是各向同性的，那么 \( \mathbf{w} \) 与连接类均值的向量成正比。如图Figure 9.3所示，这是一个直观合理的投影方向。

##### 9.2.6.2 扩展到更高维度和多类别

我们可以通过寻找一个从 \( D \) 维映射到 \( K \) 维的投影矩阵 \( \mathbf{W} \)，将上述思想扩展到多个类别和更高维的子空间。设 \( \boldsymbol{z}_n = \mathbf{W}\boldsymbol{x}_n \) 为第 \( n \) 个数据点的低维投影。令 \( \boldsymbol{m}_c = \frac{1}{N_c} \sum_{n:y_n=c} \boldsymbol{z}_n \) 为低维空间中第 \( c \) 类的对应均值，\( \boldsymbol{m} = \frac{1}{N} \sum_{c=1}^C N_c \boldsymbol{m}_c \) 为总体均值。我们定义以下散布矩阵：

$$  \tilde{\mathbf{S}}_{W}=\sum_{c=1}^{C}\sum_{n:y_{n}=c}(\mathbf{z}_{n}-\mathbf{m}_{c})(\mathbf{z}_{n}-\mathbf{m}_{c})^{\mathsf{T}}   \tag*{(9.43)}$$

$$  \tilde{\mathbf{S}}_{B}=\sum_{c=1}^{C}N_{c}(\boldsymbol{m}_{c}-\boldsymbol{m})(\boldsymbol{m}_{c}-\boldsymbol{m})^{\intercal}   \tag*{(9.44)}$$

最后，我们将目标函数定义为最大化以下式子：$ ^{2} $

$$  J(\mathbf{W})=\frac{|\tilde{\mathbf{S}}_{B}|}{|\tilde{\mathbf{S}}_{W}|}=\frac{|\mathbf{W}^{\mathsf{T}}\mathbf{S}_{B}\mathbf{W}|}{|\mathbf{W}^{\mathsf{T}}\mathbf{S}_{W}\mathbf{W}|}   \tag*{(9.45)}$$

---

其中 $ \mathbf{S}_W $ 和 $ \mathbf{S}_B $ 以显而易见的方式定义在原高维空间中（即使用 $ \mathbf{x}_n $ 代替 $ \mathbf{z}_n $，使用 $ \mu_c $ 代替 $ \mathbf{m}_c $，使用 $ \mu $ 代替 $ \mathbf{m} $）。可以证明 [DHS01]，解为 $ \mathbf{W} = \mathbf{S}_W^{-\frac{1}{2}} \mathbf{U} $，其中 $ \mathbf{U} $ 是 $ \mathbf{S}_W^{-\frac{1}{2}} \mathbf{S}_B \mathbf{S}_W^{-\frac{1}{2}} $ 的 $ K $ 个主特征向量，假设 $ \mathbf{S}_W $ 非奇异。（若奇异，则可先对所有数据进行主成分分析（PCA））。

图 9.5 给出了将该方法应用于某些 $D=10$ 维语音数据（代表 $C=11$ 个不同元音）的示例。我们投影到 $K=2$ 维以便可视化数据。可以看到 FLDA 比 PCA 提供了更好的类别分离。

注意，FLDA 最多只能找到一个 $K \leq C - 1$ 维的线性子空间，无论 $D$ 有多大，这是因为类间散度矩阵 $ \mathbf{S}_B $ 的秩为 $C - 1$。（$-1$ 项源于 $ \mu $ 项，它是 $ \mu_c $ 的线性函数。）这是一个相当严重的限制，限制了 FLDA 的实用性。

### 9.3 朴素贝叶斯分类器

在本节中，我们讨论一种简单的生成式分类方法，其中假设特征在给定类别标签的条件下是条件独立的。这被称为**朴素贝叶斯假设**。该模型被称为“朴素”是因为我们并不期望特征独立，即使在给定类别标签的条件下也是如此。然而，即使朴素贝叶斯假设不成立，由此得到的分类器往往也表现良好 [DP97; HY01a]。原因之一是模型非常简单（对于 $C$ 个类别和 $D$ 个特征，只有 $O(CD)$ 个参数），因此相对不容易过拟合。

更精确地说，朴素贝叶斯假设对应的类条件密度形式如下：

$$  p(\boldsymbol{x}|y=c,\boldsymbol{\theta})=\prod_{d=1}^{D}p(x_{d}|y=c,\boldsymbol{\theta}_{dc})   \tag*{(9.46)}$$

其中 $ \theta_{dc} $ 是类别 $c$ 和特征 $d$ 的类条件密度参数。因此，类别标签的后验分布由下式给出：

$$  p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\frac{p(y=c|\boldsymbol{\pi})\prod_{d=1}^{D}p(x_{d}|y=c,\boldsymbol{\theta}_{dc})}{\sum_{c^{\prime}}p(y=c^{\prime}|\boldsymbol{\pi})\prod_{d=1}^{D}p(x_{d}|y=c^{\prime},\boldsymbol{\theta}_{dc^{\prime}})}   \tag*{(9.47)}$$

其中 $ \pi_c $ 是类别 $c$ 的先验概率，$ \boldsymbol{\theta} = (\boldsymbol{\pi}, \{\boldsymbol{\theta}_{dc}\}) $ 是所有参数。这被称为朴素贝叶斯分类器（NBC）。

#### 9.3.1 示例模型

我们仍需指定方程 (9.46) 中概率分布的形式。这取决于特征 $ x_{d} $ 的类型。下面给出一些例子：

- 对于二元特征，$ x_d \in \{0,1\} $，我们可以使用伯努利分布：$ p(\boldsymbol{x}|y = c, \boldsymbol{\theta}) = \prod_{d=1}^D \mathrm{Ber}(x_d | \theta_{dc}) $，其中 $ \theta_{dc} $ 是类别 $c$ 中 $ x_d = 1 $ 的概率。这有时被称为多元伯努利朴素贝叶斯模型。例如，图 9.6 展示了将该模型拟合到二值化版本的 MNIST 后，每个类别估计出的参数。

---

# 0123456789

<div style="text-align: center;">图 9.6: 朴素贝叶斯分类器在 MNIST 数据集二值化版本上拟合得到的伯努利类条件密度可视化。由 naive_bayes_mnist_jax.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_384_294_789_374.jpg" alt="Image" width="35%" /></div>


<div style="text-align: center;">图 9.7: 将图 9.6 中的模型应用于部分二值化 MNIST 测试图像时所得预测结果的可视化。标题显示最大概率的预测类别。由 naive_bayes_mnist_jax.ipynb 生成。</div>


其表现出人意料地好，测试集准确率达到 84.3%。（一些示例预测见图 9.7。）

- 对于类别特征，$ x_d \in \{1, \ldots, K\} $，我们可以使用类别分布：$ p(\boldsymbol{x} | y = c, \boldsymbol{\theta}) = \prod_{d=1}^D \operatorname{Cat}(x_d | \boldsymbol{\theta}_{dc}) $，其中 $ \theta_{dck} $ 是在给定 $ y = c $ 的条件下 $ x_d = k $ 的概率。

- 对于实值特征，$ x_d \in \mathbb{R} $，我们可以使用单变量高斯分布：$ p(\boldsymbol{x} | y = c, \boldsymbol{\theta}) = \prod_{d=1}^D \mathcal{N}(x_d | \mu_{dc}, \sigma_{dc}^2) $，其中 $ \mu_{dc} $ 是类别标签为 $ c $ 时特征 $ d $ 的均值，$ \sigma_{dc}^2 $ 是其方差。（这等价于使用对角协方差矩阵的高斯判别分析。）

#### 9.3.2 模型拟合

本节讨论如何使用最大似然估计拟合朴素贝叶斯分类器。我们可以将似然函数写为：

$$  p(\mathcal{D}|\boldsymbol{\theta})=\prod_{n=1}^{N}\left[\mathrm{Cat}(y_{n}|\boldsymbol{\pi})\prod_{d=1}^{D}p(x_{nd}|y_{n},\boldsymbol{\theta}_{d})\right]   \tag*{(9.48)}$$

$$  =\prod_{n=1}^{N}\left[\mathrm{Cat}(y_{n}|\boldsymbol{\pi})\prod_{d=1}^{D}\prod_{c=1}^{C}p(x_{nd}|\boldsymbol{\theta}_{dc})^{\mathbb{I}(y_{n}=c)}\right]   \tag*{(9.49)}$$

因此对数似然为

$$  \log p(\mathcal{D}|\boldsymbol{\theta})=\left[\sum_{n=1}^{N}\sum_{c=1}^{C}\mathbb{I}\left(y_{n}=c\right)\log\pi_{c}\right]+\sum_{c=1}^{C}\sum_{d=1}^{D}\left[\sum_{n:y_{n}=c}\log p(x_{n d}|\boldsymbol{\theta}_{d c})\right]   \tag*{(9.50)}$$

我们看到这分解为关于 $\pi$ 的一项和关于每个 $\theta_{dc}$ 的 $CD$ 项：

$$  \log p(\mathcal{D}|\boldsymbol{\theta})=\log p(\mathcal{D}_{y}|\boldsymbol{\pi})+\sum_{c}\sum_{d}\log p(\mathcal{D}_{dc}|\boldsymbol{\theta}_{dc})   \tag*{(9.51)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可。

---

其中 $\mathcal{D}_y = \{y_n : n = 1 : N\}$ 是所有标签，$\mathcal{D}_{dc} = \{x_{nd} : y_n = c\}$ 是来自类别 $c$ 的样本中特征 $d$ 的所有取值。因此，我们可以分别估计这些参数。

在 4.2.4 节中，我们展示了 $\pi$ 的 MLE 是经验计数向量 $\hat{\pi}_c = \frac{N_c}{N}$。$\theta_{dc}$ 的 MLE 依赖于特征 $d$ 的类别条件密度的选择。下面我们讨论几种常见的选择。

- 对于离散特征，我们可以使用类别分布。对 4.2.4 节结果的直接推广给出了 MLE 的以下表达式：

$$  \hat{\theta}_{d c k}=\frac{N_{d c k}}{\sum_{k^{\prime}=1}^{K}N_{d c k^{\prime}}}=\frac{N_{d c k}}{N_{c}}   \tag*{(9.52)}$$

其中 $ N_{dck} = \sum_{n=1}^{N} \mathbb{I}(x_{nd} = k, y_{n} = c) $ 是特征 $d$ 在类别 $c$ 的样本中取值为 $k$ 的次数。

- 对于二值特征，类别分布退化为伯努利分布，MLE 变为

$$  \hat{\theta}_{dc}=\frac{N_{dc}}{N_{c}}   \tag*{(9.53)}$$

这是特征 $d$ 在类别 $c$ 的样本中取值为 1 的经验比例。

- 对于实值特征，我们可以使用高斯分布。对 4.2.5 节结果的直接推广给出了 MLE 的以下表达式：

$$  \hat{\mu}_{dc}=\frac{1}{N_{c}}\sum_{n:y_{n}=c}x_{nd}   \tag*{(9.54)}$$

$$  \hat{\sigma}_{dc}^{2}=\frac{1}{N_{c}}\sum_{n:y_{n}=c}(x_{nd}-\hat{\mu}_{dc})^{2}   \tag*{(9.55)}$$

因此，我们看到拟合朴素贝叶斯分类器极其简单且高效。

#### 9.3.3 贝叶斯朴素贝叶斯

在本节中，我们将 9.3.2 节中关于朴素贝叶斯分类器 MLE 估计的讨论扩展到计算参数的后验分布。为简单起见，假设我们使用类别特征，因此 $ p(x_d|\pmb{\theta}_{dc}) = \mathrm{Cat}(x_d|\pmb{\theta}_{dc}) $，其中 $ \theta_{dck} = p(x_d = k|y = c) $。在 4.6.3.2 节中，我们展示了类别似然的共轭先验是狄利克雷分布 $ p(\pmb{\theta}_{dc}) = \mathrm{Dir}(\pmb{\theta}_{dc}|\pmb{\beta}_{dc}) $，其中 $ \beta_{dck} $ 可以解释为一组“伪计数”，对应于来自先验数据的计数 $ N_{dck} $。类似地，我们对标签频率使用狄利克雷先验 $ p(\pmb{\pi}) = \mathrm{Dir}(\pmb{\pi}|\alpha) $。通过使用共轭先验，我们可以如 4.6.3 节所述以闭合形式计算后验。特别地，我们有

$$  p(\boldsymbol{\theta}|\mathcal{D})=\mathrm{Dir}(\boldsymbol{\pi}|\hat{\boldsymbol{\alpha}})\prod_{d=1}^{D}\prod_{c=1}^{C}\mathrm{Dir}(\boldsymbol{\theta}_{dc}|\hat{\boldsymbol{\beta}}_{dc})   \tag*{(9.56)}$$

---

其中 $ \widehat{\alpha}_c = \widetilde{\alpha}_c + N_c $ 和 $ \widehat{\beta}_{dck} = \widetilde{\beta}_{dck} + N_{dck} $。

利用第4.6.3.4节的结果，我们可以推导出后验预测分布如下。对于标签先验（在观测到 $\boldsymbol{x}$ 之前，但在观测到 $\mathcal{D}$ 之后），我们有 $p(y|\mathcal{D}) = \mathrm{Cat}(y|\overline{\boldsymbol{\pi}})$，其中 $\overline{\pi}_c = \widehat{\alpha}_c / \sum_{c'} \widehat{\alpha}_{c'}$。对于 $\boldsymbol{x}$ 的特征似然（给定 $y$ 和 $\mathcal{D}$），我们有 $p(x_d = k|y = c, \mathcal{D}) = \overline{\theta}_{dck}$，其中

$$  \overline{\theta}_{d c k}=\frac{\widehat{\beta}_{d c k}}{\sum_{k^{\prime}=1}^{K}\widehat{\beta}_{d c k^{\prime}}}=\frac{\widetilde{\beta}_{d c k}+N_{d c k}}{\sum_{k^{\prime}=1}^{K}\widetilde{\beta}_{d c k^{\prime}}+N_{d c k^{\prime}}}   \tag*{(9.57)}$$

是参数的后验均值。（注意 $ \sum_{k^{\prime}=1}^{N} N_{dck^{\prime}} = N_{dc} = N_{c} $ 是类别c的样本数。）

如果 $ \breve{\beta}_{dck}=0 $，则退化为方程(9.52)中的MLE。相反，如果设置 $ \breve{\beta}_{dck}=1 $，则在归一化之前将所有经验计数加1。这称为加一平滑或拉普拉斯平滑。例如，在二值情况下，得到

$$  \overline{\theta}_{dc}=\frac{\breve{\beta}_{dc1}+N_{dc1}}{\breve{\beta}_{dc0}+N_{dc0}+\breve{\beta}_{dc1}+N_{dc1}}=\frac{1+N_{dc1}}{2+N_{dc}}   \tag*{(9.58)}$$

我们最终可以按如下方式计算标签的后验预测分布：

$$  p(y=c|\boldsymbol{x},\mathcal{D})\propto p(y=c|\mathcal{D})\prod_{d}p(x_{d}|y=c,\mathcal{D})=\overline{\pi}_{c}\prod_{d}\prod_{k}\overline{\theta}_{d c k}^{\mathbb{I}(x_{d}=k)}   \tag*{(9.59)}$$

这给出了朴素贝叶斯的完全贝叶斯形式，其中我们已将所有参数积分掉。（在这种情况下，只需代入后验均值参数即可得到预测分布。）

#### 9.3.4 朴素贝叶斯与逻辑回归之间的联系

在本节中，我们展示NBC模型的类别后验 $p(y|\boldsymbol{x},\boldsymbol{\theta})$ 具有与多项式逻辑回归相同的形式。为简单起见，我们假设特征都是离散的，且每个特征有 $K$ 个状态，尽管该结果适用于指数族中的任意特征分布。

令 $ x_{dk} = \mathbb{I}(x_d = k) $，则 $ \mathbf{x}_d $ 是特征 $ d $ 的独热编码。那么类条件密度可以写成如下形式：

$$  p(\boldsymbol{x}|y=c,\boldsymbol{\theta})=\prod_{d=1}^{D}Cat(x_{d}|y=c,\boldsymbol{\theta})=\prod_{d=1}^{D}\prod_{k=1}^{K}\theta_{d c k}^{x_{d k}}   \tag*{(9.60)}$$

因此类别的后验由下式给出

$$  p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\frac{\pi_{c}\prod_{d}\prod_{k}\theta_{d c k}^{x_{d k}}}{\sum_{c^{\prime}}\pi_{c^{\prime}}\prod_{d}\prod_{k}\theta_{d c^{\prime}k}^{x_{d k}}}=\frac{\exp[\log\pi_{c}+\sum_{d}\sum_{k}x_{d k}\log\theta_{d c k}]}{\sum_{c^{\prime}}\exp[\log\pi_{c^{\prime}}+\sum_{d}\sum_{k}x_{d k}\log\theta_{d c^{\prime}k}]}   \tag*{(9.61)}$$

这可以写成一个softmax

$$  p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\frac{e^{\boldsymbol{\beta}_{c}^{\mathsf{T}}\boldsymbol{x}+\gamma_{c}}}{\sum_{c^{\prime}=1}^{C}e^{\boldsymbol{\beta}_{c^{\prime}}^{\mathsf{T}}\boldsymbol{x}+\gamma_{c^{\prime}}}}   \tag*{(9.62)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_210_150_539_403.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_618_151_947_397.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 9.8：类条件密度 $p(\boldsymbol{x}|y=c)$（左图）可能比类后验概率 $p(y=c|\boldsymbol{x})$（右图）更复杂。图片改编自 [Bis06] 的图 1.27。由 generative VsDiscrim.ipynb 生成。</div>

通过适当定义 $\boldsymbol{\beta}_c$ 和 $\gamma_c$。这与第 2.5.3 节中的多项逻辑回归具有完全相同的形式。区别在于，朴素贝叶斯优化的是联合似然 $\prod_n p(y_n, \boldsymbol{x}_n|\boldsymbol{\theta})$，而逻辑回归优化的是条件似然 $\prod_n p(y_n|\boldsymbol{x}_n,\boldsymbol{\theta})$。通常，这两者会给出不同结果（见练习 10.3）。

### 9.4 生成式分类器与判别式分类器

形如 $p(\boldsymbol{x}, y) = p(y)p(\boldsymbol{x}|y)$ 的模型称为**生成式分类器**，因为它可用于从每个类别 $y$ 生成样本 $\boldsymbol{x}$。相比之下，形如 $p(y|\boldsymbol{x})$ 的模型称为**判别式分类器**，因为它仅能用于区分不同类别。下面我们讨论生成式和判别式分类方法的各种优缺点（另见 [BT04; UB05; LBM06; BL07a; Rot+18]）。

#### 9.4.1 判别式分类器的优势

判别式分类器的主要优势如下：

- **更高的预测精度**。判别式分类器通常比生成式分类器准确得多 [NJ02]。原因在于，条件分布 $p(y|\boldsymbol{x})$ 通常比联合分布 $p(y,\boldsymbol{x})$ 简单得多（因此更易学习），如图 9.8 所示。特别是，判别式模型无需“浪费精力”对输入特征的分布进行建模。

- **可处理特征预处理**。判别式方法的一大优点是允许我们对输入进行任意方式的预处理。例如，可以对输入特征进行多项式扩展，也可以将单词序列替换为嵌入向量（见第 20.5 节）。在预处理后的数据上定义生成式模型通常很困难，因为新特征可能以复杂的方式相互关联，难以建模。

---

- 良好校准的概率。某些生成式分类器，例如朴素贝叶斯（在第9.3节中描述），做出了通常并不成立的强独立性假设。这可能导致后验类概率非常极端（非常接近0或1）。判别式模型（如逻辑回归）在概率估计方面通常校准得更好，尽管它们有时也需要调整（参见例如[NMC05]）。

#### 9.4.2 生成式分类器的优势

生成式分类器的主要优势如下：

• 易于拟合。生成式分类器通常非常容易拟合。例如，在第9.3.2节中，我们展示了如何通过简单的计数和平均来拟合朴素贝叶斯分类器。相比之下，逻辑回归需要求解一个凸优化问题（详见第10.2.3节），而神经网络需要求解一个非凸优化问题，这两者都慢得多。

- 可以轻松处理缺失的输入特征。有时某些输入（x 的分量）未被观测到。在生成式分类器中，有一种简单的方法来处理这种情况，如第1.5.5节所示。然而，在判别式分类器中，这个问题没有原则性的解决方案，因为模型假设 x 总是可用的，可以作为条件变量。

- 可以单独拟合各个类别。在生成式分类器中，我们独立地估计每个类条件密度的参数（如第9.3.2节所示），因此在添加更多类别时无需重新训练模型。相比之下，在判别式模型中，所有参数相互作用，因此如果添加新类别，必须重新训练整个模型。

- 可以处理未标记的训练数据。生成式模型很容易用于半监督学习，其中我们结合了带标签数据 $ \mathcal{D}_{xy} = \{(\boldsymbol{x}_n, y_n)\} $ 和未标签数据 $ \mathcal{D}_x = \{\boldsymbol{x}_n\} $。然而，对于判别式模型来说，这更难做到，因为没有唯一最优的方法来利用 $ \mathcal{D}_x $。

- 可能对虚假特征更具鲁棒性。判别式模型 $ p(y|x) $ 可能会捕捉到输入 x 中能在训练集上区分不同 y 值的特征，但这些特征并不稳健且无法泛化到训练集之外。这些被称为虚假特征（参见例如[Arj21; Zho+21]）。相比之下，生成式模型 $ p(x|y) $ 可能更能捕捉底层数据生成过程的因果机制；这样的因果模型可以对分布偏移更具鲁棒性（参见例如[Sch19; LBS19; LN81]）。

#### 9.4.3 处理缺失特征

有时在训练和/或测试过程中，我们会丢失输入 x 的部分信息。在生成式分类器中，我们可以通过边缘化缺失值来处理这种情况。（我们假设特征的缺失并不提供关于其潜在值的信息。）相比之下，在使用判别式模型时，没有唯一最佳的方法来处理缺失输入，如第1.5.5节所述。

作者：Kevin P. Murphy。(C) MIT 出版社。CC-BY-NC-ND 许可证。

---

例如，假设我们缺失了 $x_{1}$ 的值。我们只需计算

$$  \begin{align*}p(y=c|\boldsymbol{x}_{2:D},\boldsymbol{\theta})&\propto p(y=c|\boldsymbol{\pi})p(\boldsymbol{x}_{2:D}|y=c,\boldsymbol{\theta})\\&=p(y=c|\boldsymbol{\pi})\sum_{x_{1}}p(x_{1},\boldsymbol{x}_{2:D}|y=c,\boldsymbol{\theta})\end{align*}   \tag*{(9.63)}$$

在高斯判别分析中，我们可以使用第 3.2.3 节的公式对 $x_{1}$ 进行边缘化。

如果我们采用朴素贝叶斯假设，事情就更加简单了，因为我们只需忽略 $x_{1}$ 的似然项。这是因为

$$  \sum_{x_{1}}p(x_{1},x_{2:D}|y=c,\boldsymbol{\theta})=\left[\sum_{x_{1}}p(x_{1}|\boldsymbol{\theta}_{1c})\right]\prod_{d=2}^{D}p(x_{d}|\boldsymbol{\theta}_{d c})=\prod_{d=2}^{D}p(x_{d}|\boldsymbol{\theta}_{d c})   \tag*{(9.65)}$$

这里我们利用了 $p(x_d|y=c,\boldsymbol{\theta}) = p(x_d|\boldsymbol{\theta}_{dc})$ 且 $\sum_{x_1}p(x_1|\boldsymbol{\theta}_{1c})=1$ 的事实。

### 9.5 习题

练习 9.1 [Fisher 线性判别函数的推导]

证明 $J(\boldsymbol{w}) = \frac{\boldsymbol{w}^T \boldsymbol{S}_B \boldsymbol{w}}{\boldsymbol{w}^T \boldsymbol{S}_W \boldsymbol{w}}$ 的最大值由 $\boldsymbol{S}_B \boldsymbol{w} = \lambda \boldsymbol{S}_W \boldsymbol{w}$ 给出

其中 $\lambda = \frac{w^T \mathbf{S}_B w}{w^T \mathbf{S}_W w}$。提示：回忆两个标量之比的导数为 $\frac{d}{dx} \frac{f(x)}{g(x)} = \frac{f'(g - f_g')}{g^2}$，其中 $f' = \frac{d}{dx} f(x)$，$g' = \frac{d}{dx} g(x)$。另外，回忆 $\frac{d}{dx} \mathbf{x}^T \mathbf{A} \mathbf{x} = (\mathbf{A} + \mathbf{A}^T) \mathbf{x}$。

---

# 10 逻辑回归

### 10.1 引言

逻辑回归是一种广泛使用的判别式分类模型  $ p(y|\boldsymbol{x};\boldsymbol{\theta}) $，其中  $ \boldsymbol{x} \in \mathbb{R}^D $ 是固定维度的输入向量，  $ y \in \{1, \ldots, C\} $ 是类别标签，  $ \boldsymbol{\theta} $ 是参数。当  $ C = 2 $ 时，称为二元逻辑回归；当  $ C > 2 $ 时，称为多项逻辑回归，或者多类逻辑回归。下面我们将详细介绍。

### 10.2 二元逻辑回归

二元逻辑回归对应于以下模型

$$  p(y|\boldsymbol{x},\boldsymbol{\theta})=\mathrm{Ber}(y|\sigma(\boldsymbol{w}^{\top}\boldsymbol{x}+b))   \tag*{(10.1)}$$

其中  $ \sigma $ 是第 2.4.2 节定义的 Sigmoid 函数，  $ \boldsymbol{w} $ 是权重，b 是偏置，  $ \boldsymbol{\theta} = (\boldsymbol{w}, b) $ 是所有参数。换言之，

$$  p(y=1|\boldsymbol{x},\boldsymbol{\theta})=\sigma(a)=\frac{1}{1+e^{-a}}   \tag*{(10.2)}$$

其中 $a = \boldsymbol{w}^{\mathrm{T}}\boldsymbol{x} + b = \log\left(\frac{p}{1-p}\right)$ 是对数几率，$p = p(y = 1|\boldsymbol{x},\boldsymbol{\theta})$。（在机器学习中，量 $a$ 通常称为 logit 或预激活值。）

有时我们选择使用标签  $ \tilde{y} \in \{-1, +1\} $ 而非  $ y \in \{0,1\} $。我们可以利用下式计算这些替代标签的概率

$$  p(\tilde{y}|\boldsymbol{x},\boldsymbol{\theta})=\sigma(\tilde{y}a)   \tag*{(10.3)}$$

因为  $ \sigma(-a) = 1 - \sigma(a) $。这种更紧凑的表示法在机器学习文献中被广泛使用。

#### 10.2.1 线性分类器

Sigmoid 函数给出了类别标签为 y = 1 的概率。如果每个类别误分类的损失相同，那么最优决策规则是当且仅当类别 1 比类别 0 更可能时预测 y = 1，正如我们在第 5.1.2.2 节中所解释的。因此

$$  f(\boldsymbol{x})=\mathbb{I}\left(p(y=1|\boldsymbol{x})>p(y=0|\boldsymbol{x})\right)=\mathbb{I}\left(\log\frac{p(y=1|\boldsymbol{x})}{p(y=0|\boldsymbol{x})}>0\right)=\mathbb{I}\left(a>0\right)   \tag*{(10.4)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_248_125_516_331.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_618_172_1007_339.jpg" alt="图像" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图10.1: (a) 三维空间中一个二维平面的可视化，该平面具有法向量 w，且经过点 $ \mathbf{x}_{0} = (x_{0}, y_{0}, z_{0}) $。详见正文。(b) 在鸢尾花数据集的二类二特征版本上，由逻辑回归诱导的最优线性决策边界可视化。由 iris_logreg.ipynb 生成。改编自 [Gér19] 中的图4.24。</div>


其中 $ a = w^{\top} x + b $.

因此，我们可以将预测函数写作如下形式：

$$  f(\boldsymbol{x};\boldsymbol{\theta})=b+\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}=b+\sum_{d=1}^{D}w_{d}x_{d}   \tag*{(10.5)}$$

其中 $ \boldsymbol{w}^\top \boldsymbol{x} = \langle \boldsymbol{w}, \boldsymbol{x} \rangle $ 是权重向量 $ \boldsymbol{w} $ 与特征向量 $ \boldsymbol{x} $ 之间的内积。该函数定义了一个线性超平面，其法向量为 $ \boldsymbol{w} \in \mathbb{R}^D $，距原点的偏移量为 $ b \in \mathbb{R} $。

从图10.1a可以看出方程(10.5)的含义。这里展示了一个三维特征空间中的平面，该平面经过点 $ x_0 $，法向量为 $ w $。平面上的点满足 $ w^\top(x - x_0) = 0 $。若定义 $ b = -w^\top x_0 $，则可重写为 $ w^\top x + b = 0 $。该平面将三维空间划分为两个半空间。这种线性平面被称为 **决策边界**。如果我们能通过这样一个线性边界完美地分离训练样本（在训练集上不产生任何分类错误），我们就说数据是 **线性可分** 的。从图10.1b可以看出，鸢尾花数据集的二类二特征版本并不是线性可分的。

通常，正确类别标签存在不确定性，因此我们需要预测标签上的概率分布，而不仅仅是判断我们在决策边界的哪一侧。在图10.2中，我们绘制了不同权重向量 $ \boldsymbol{w} $ 下的 $ p(y = 1|(x_1, x_2), \boldsymbol{w}) = \sigma(w_1 x_1 + w_2 x_2) $。向量 $ \boldsymbol{w} $ 定义了决策边界的朝向，其模长 $ \|\boldsymbol{w}\| = \sqrt{\sum_{d=1}^{D} w_d^2} $ 控制着 sigmoid 的陡峭程度，从而影响预测的置信度。

#### 10.2.2 非线性分类器

我们通常可以通过对输入进行适当的预处理来使问题线性可分。具体地，令 $ \phi(\boldsymbol{x}) $ 为输入特征向量的变换版本。例如，假设我们使用 $ \phi(x_1, x_2) = [1, x_1^2, x_2^2] $，并令 $ \boldsymbol{w} = [-R^2, 1, 1] $。那么 $ \boldsymbol{w}^\top \phi(\boldsymbol{x}) = x_1^2 + x_2^2 - R^2 $，因此决策边界（其中 $ f(\boldsymbol{x}) = 0 $）定义了一个半径为 $ R $ 的圆，如图10.3所示。由此得到的

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_361_128_799_476.jpg" alt="图像" width="38%" /></div>


<div style="text-align: center;">图10.2：$\sigma(w_1x_1 + w_2x_2)$ 的图示。其中 $\mathbf{w} = (w_1, w_2)$ 定义了决策边界的法向量。位于该边界右侧的点满足 $\sigma(\mathbf{w}^\top \mathbf{x}) > 0.5$，左侧的点满足 $\sigma(\mathbf{w}^\top \mathbf{x}) < 0.5$。改编自 [Mac03] 的图39.3，由 sigmoid_2d_plot.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_262_600_908_817.jpg" alt="图像" width="56%" /></div>


<div style="text-align: center;">图10.3：通过将特征从 $\mathbf{x} = (x_1, x_2)$ 变换为 $\phi(\mathbf{x}) = (x_1^2, x_2^2)$，将二次决策边界转换为线性边界的示意图。经 Jean-Philippe Vert 许可使用。</div>


函数 $f$ 在参数 $\boldsymbol{w}$ 上仍然是线性的，这对于简化学习问题很重要，我们将在第10.2.3节中看到这一点。然而，除了线性权重 $\boldsymbol{w}$ 之外，我们还可以通过学习特征提取器 $\phi(\boldsymbol{x})$ 的参数来获得更强的能力；我们将在第三部分讨论如何实现这一点。

在图10.3中，我们使用了特征的二次展开。我们也可以使用更高阶的多项式，如第1.2.2.2节所示。在图1.7中，我们展示了在二维逻辑回归问题上使用高达K阶多项式展开的效果。与图1.7类似，我们看到随着参数数量的增加，模型变得复杂，并最终导致过拟合。我们将在第10.2.7节讨论减少过拟合的方法。

作者：Kevin P. Murphy。 (C) MIT Press。采用CC-BY-NC-ND许可协议。

---

#### 10.2.3 最大似然估计

本节讨论如何利用最大似然估计来估计逻辑回归模型的参数。

##### 10.2.3.1 目标函数

负对数似然（按数据集大小 N 缩放）由下式给出（我们假设偏置项 b 已被吸收到权重向量 w 中）：

$$   NLL(\boldsymbol{w})=-\frac{1}{N}\log p(\mathcal{D}|\boldsymbol{w})=-\frac{1}{N}\log\prod_{n=1}^{N}Ber(y_{n}|\mu_{n})   \tag*{(10.6)}$$

$$  =-\frac{1}{N}\sum_{n=1}^{N}\log[\mu_{n}^{y_{n}}\times(1-\mu_{n})^{1-y_{n}}]   \tag*{(10.7)}$$

$$  =-\frac{1}{N}\sum_{n=1}^{N}\left[y_{n}\log\mu_{n}+(1-y_{n})\log(1-\mu_{n})\right]   \tag*{(10.8)}$$

$$  =\frac{1}{N}\sum_{n=1}^{N}\mathbb{H}_{ce}(y_{n},\mu_{n})   \tag*{(10.9)}$$

其中 $ \mu_n = \sigma(a_n) $ 是类别 1 的概率，$ a_n = \boldsymbol{w}^\top \boldsymbol{x}_n $ 是对数几率，而 $ \mathbb{H}_{ce}(y_n, \mu_n) $ 是二元交叉熵，定义为

$$  \mathbb{H}_{c e}(p,q)=-\left[p\log q+(1-p)\log(1-q)\right]   \tag*{(10.10)}$$

如果使用 $ \tilde{y}_n \in \{-1, +1\} $ 代替 $ y_n \in \{0,1\} $，则可以将其重写如下：

$$  \mathrm{N L L}(\boldsymbol{w})=-\frac{1}{N}\sum_{n=1}^{N}\left[\mathbb{I}\left(\tilde{y}_{n}=1\right)\log(\sigma(a_{n}))+\mathbb{I}\left(\tilde{y}_{n}=-1\right)\log(\sigma(-a_{n}))\right]   \tag*{(10.11)}$$

$$  =-\frac{1}{N}\sum_{n=1}^{N}\log(\sigma(\tilde{y}_{n}a_{n}))   \tag*{(10.12)}$$

$$  =\frac{1}{N}\sum_{n=1}^{N}\log(1+\exp(-\tilde{y}_{n}a_{n}))   \tag*{(10.13)}$$

然而，在本书中，我们主要使用 $ y_n \in \{0,1\} $ 的表示法，因为它更容易推广到多类情况（第 10.3 节），并且更容易看出与交叉熵的联系。

##### 10.2.3.2 优化目标函数

为了找到最大似然估计，必须求解

$$  \nabla_{w}\mathrm{N L L}(w)=g(w)=0   \tag*{(10.14)}$$

我们可以使用任何基于梯度的优化算法来求解此方程，例如第 8 章讨论的那些算法。我们在第 10.2.4 节中给出了一个具体示例。但首先，我们必须按照下面的说明推导出梯度。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_134_551_378.jpg" alt="图像" width="29%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_619_134_959_381.jpg" alt="图像" width="29%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_215_433_551_675.jpg" alt="图像" width="29%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_597_447_960_688.jpg" alt="图像" width="31%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图 10.4：对二类、二维逻辑回归问题应用多项式特征扩展。(a) 阶数 K = 1。(b) 阶数 K = 2。(c) 阶数 K = 4。(d) 训练误差与测试误差随阶数的变化。由 $ \text{logreg\_poly\_demo.ipynb} $ 生成。</div>

##### 10.2.3.3 推导梯度

虽然我们可以使用自动微分方法（第 13.3 节）来计算 NLL 的梯度，但显式地计算也很容易，如下所示。幸运的是，所得方程将具有简单直观的解释，可用于推导其他方法，我们将在后文看到。

首先，注意到

$$  \frac{d\mu_{n}}{d a_{n}}=\sigma(a_{n})(1-\sigma(a_{n}))   \tag*{(10.15)}$$

其中 $ a_n = \boldsymbol{w}^\top \boldsymbol{x}_n $ 且 $ \mu_n = \sigma(a_n) $。因此，根据链式法则（以及第 7.8 节讨论的向量微积分规则），我们有

$$  \frac{\partial}{\partial w_{d}}\mu_{n}=\frac{\partial}{\partial w_{d}}\sigma(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{n})=\frac{\partial}{\partial a_{n}}\sigma(a_{n})\frac{\partial a_{n}}{\partial w_{d}}=\mu_{n}(1-\mu_{n})x_{n d}   \tag*{(10.16)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

偏置项的梯度可以通过类似方式推导，只需在上述方程中使用输入 $x_{n0}=1$。但为简化起见，我们忽略偏置项。因此

$$  \nabla_{\boldsymbol{w}}\log(\mu_{n})=\frac{1}{\mu_{n}}\nabla_{\boldsymbol{w}}\mu_{n}=(1-\mu_{n})\boldsymbol{x}_{n}   \tag*{(10.17)}$$

类似地，

$$  \nabla_{\boldsymbol{w}}\log(1-\mu_{n})=\frac{-\mu_{n}(1-\mu_{n})\boldsymbol{x}_{n}}{1-\mu_{n}}=-\mu_{n}\boldsymbol{x}_{n}   \tag*{(10.18)}$$

因此，负对数似然（NLL）的梯度向量由下式给出

$$  \nabla_{\boldsymbol{w}}\mathrm{N L L}(\boldsymbol{w})=-\frac{1}{N}\sum_{n=1}^{N}\left[y_{n}(1-\mu_{n})\boldsymbol{x}_{n}-(1-y_{n})\mu_{n}\boldsymbol{x}_{n}\right]   \tag*{(10.19)}$$

$$  =-\frac{1}{N}\sum_{n=1}^{N}\left[y_{n}\boldsymbol{x}_{n}-y_{n}\boldsymbol{x}_{n}\mu_{n}-\boldsymbol{x}_{n}\mu_{n}+y_{n}\boldsymbol{x}_{n}\mu_{n}\right)]   \tag*{(10.20)}$$

$$  =\frac{1}{N}\sum_{n=1}^{N}(\mu_{n}-y_{n})\boldsymbol{x}_{n}   \tag*{(10.21)}$$

如果我们将 $e_n = \mu_n - y_n$ 解释为误差信号，可以看出梯度用每个输入 $\boldsymbol{x}_n$ 的误差对其进行加权，然后取平均。注意，我们可以将梯度重写为矩阵形式如下：

$$  \nabla_{w}\mathrm{N L L}(\boldsymbol{w})=\frac{1}{N}(\mathbf{1}_{N}^{\mathsf{T}}(\mathrm{d i a g}(\boldsymbol{\mu}-\boldsymbol{y})\mathbf{X}))^{\mathsf{T}}   \tag*{(10.22)}$$

其中 $\mathbf{X}$ 是 $N \times D$ 的设计矩阵，其每一行包含样本 $\boldsymbol{x}_n$。

##### 10.2.3.4 推导 Hessian 矩阵

基于梯度的优化器将找到满足 $\boldsymbol{g}(\boldsymbol{w}) = \boldsymbol{0}$ 的驻点。该驻点可能是全局最优或局部最优。为确保该驻点是全局最优，我们必须证明目标函数是 **凸函数**，其原因在第 8.1.1.1 节中阐述。直观上，这意味着 NLL 具有 **碗状**，存在唯一的最低点，实际情况确实如此，如图 10.5b 所示。

更正式地，我们必须证明 Hessian 矩阵是半正定的，下面我们进行证明。（相关线性代数背景信息请参见第 7 章。）可以证明，Hessian 矩阵由下式给出

$$  \mathbf{H}(\boldsymbol{w})=\nabla_{\boldsymbol{w}}\nabla_{\boldsymbol{w}}^{\mathsf{T}}\mathrm{N L L}(\boldsymbol{w})=\frac{1}{N}\sum_{n=1}^{N}(\mu_{n}(1-\mu_{n})\boldsymbol{x}_{n})\boldsymbol{x}_{n}^{\mathsf{T}}=\frac{1}{N}\mathbf{X}^{\mathsf{T}}\mathbf{S}\mathbf{X}   \tag*{(10.23)}$$

其中

$$  \mathbf{S}\triangleq\mathrm{diag}(\mu_{1}(1-\mu_{1}),\ldots,\mu_{N}(1-\mu_{N}))   \tag*{(10.24)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_181_116_609_410.jpg" alt="图片" width="37%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_183_118_976_422.jpg" alt="图片" width="68%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_678_140_973_414.jpg" alt="图片" width="25%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 10.5：针对包含1个特征和1个偏置项的鸢尾花数据集（Iris dataset），二元逻辑回归的NLL损失曲面。目标是使函数最小化。全局最大似然估计位于图的中心。由 iris_logreg_loss_surface.ipynb 生成。</div>

我们看到 H 是正定的，因为对于任意非零向量 v，有

$$  \boldsymbol{v}^{\mathrm{T}}\mathbf{X}^{\mathrm{T}}\mathbf{S}\mathbf{X}\boldsymbol{v}=(\boldsymbol{v}^{\mathrm{T}}\mathbf{X}^{\mathrm{T}}\mathbf{S}^{\frac{1}{2}})(\mathbf{S}^{\frac{1}{2}}\mathbf{X}\boldsymbol{v})=||\boldsymbol{v}^{\mathrm{T}}\mathbf{X}^{\mathrm{T}}\mathbf{S}^{\frac{1}{2}}||_{2}^{2}>0   \tag*{(10.25)}$$

这是因为由于使用了 sigmoid 函数，所有 $ n $ 均有 $ \mu_n > 0 $。因此，负对数似然（NLL）是严格凸的。然而在实践中，接近 0 或 1 的 $ \mu_n $ 值可能导致 Hessian 矩阵接近奇异。我们可以通过使用 $ \ell_2 $ 正则化来避免这种情况，如第 10.2.7 节所述。

#### 10.2.4 随机梯度下降

我们的目标是解决以下优化问题

$$  \hat{w}\triangleq\underset{w}{\operatorname{argmin}}\mathcal{L}(w)   \tag*{(10.26)}$$

其中 $ \mathcal{L}(\boldsymbol{w}) $ 是损失函数，在这里即负对数似然：

$$   NLL(\boldsymbol{w})=-\frac{1}{N}\sum_{n=1}^{N}\left[y_{n}\log\mu_{n}+(1-y_{n})\log(1-\mu_{n})\right]   \tag*{(10.27)}$$

这里 $ \mu_n = \sigma(a_n) $ 是类别 1 的概率，而 $ a_n = \boldsymbol{w}^\top \boldsymbol{x}_n $ 是对数几率。

我们可以使用许多算法来求解方程 (10.26)，如第 8 章所述。最简单的也许是使用随机梯度下降（第 8.4 节）。如果使用大小为 1 的小批量，则得到以下简单的更新公式：

$$  \boldsymbol{w}_{t+1}=\boldsymbol{w}_{t}-\eta_{t}\nabla_{\boldsymbol{w}}\mathrm{N L L}(\boldsymbol{w}_{t})=\boldsymbol{w}_{t}-\eta_{t}(\mu_{n}-y_{n})\boldsymbol{x}_{n}   \tag*{(10.28)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

其中，我们将方程(10.21)梯度中对所有N个样本的平均替换为随机选取的单个样本n（索引n随t变化）。

由于已知目标函数是凸的（参见第10.2.3.4节），可以证明，只要我们以适当的速度衰减学习率（参见第8.4.3节），该过程将收敛到全局最优解。我们可以使用方差缩减技术（如SAGA（第8.4.5.2节））来提高收敛速度。

#### 10.2.5 感知机算法

感知机最早由[Ros58]提出，是一种确定性的二分类器，形式如下：

$$  f(\boldsymbol{x}_{n};\boldsymbol{\theta})=\mathbb{I}\left(\boldsymbol{w}^{\top}\boldsymbol{x}_{n}+b>0\right)   \tag*{(10.29)}$$

这可以看作是二元逻辑回归分类器的一个极限情况，其中sigmoid函数 $\sigma(a)$ 被替换为Heaviside阶跃函数 $H(a) \triangleq \mathbb{I}(a > 0)$。图Figure 2.10对比了这两个函数。

由于Heaviside函数不可微，我们无法使用基于梯度的优化方法来拟合该模型。但Rosenblatt提出了感知机学习算法。其基本思想是从随机权重开始，每当模型做出错误预测时，就迭代地更新权重。更精确地说，我们使用下式更新权重：

$$  \boldsymbol{w}_{t+1}=\boldsymbol{w}_{t}-\eta_{t}(\hat{\boldsymbol{y}}_{n}-\boldsymbol{y}_{n})\boldsymbol{x}_{n}   \tag*{(10.30)}$$

其中，$(x_n, y_n)$ 是在第 $t$ 次迭代中采样的带标签样本，$\eta_t$ 是学习率或步长（我们可以将步长设为1，因为权重的幅度不影响决策边界）。该算法的简单实现参见 perceptron_demo_2d.ipynb。

方程(10.30)中的感知机更新规则有一个直观的解释：如果预测正确，则不进行任何改变；否则，我们朝着使正确答案更可能的方向移动权重。更精确地说，如果 $y_n=1$ 且 $\hat{y}_n=0$，则有 $\boldsymbol{w}_{t+1} = \boldsymbol{w}_t + \boldsymbol{x}_n$；如果 $y_n=0$ 且 $\hat{y}_n=1$，则有 $\boldsymbol{w}_{t+1} = \boldsymbol{w}_t - \boldsymbol{x}_n$。

通过比较方程(10.30)和(10.28)，我们可以看到，感知机更新规则等价于二元逻辑回归的SGD更新规则，其中使用了一个近似：我们将软概率 $\mu_n = p(y_n=1|\boldsymbol{x}_n)$ 替换为硬标签 $\hat{y}_n = f(\boldsymbol{x}_n)$。感知机方法的优点是我们不需要计算概率，这在标签空间非常大时可能很有用。缺点是该方法仅在数据线性可分时收敛[Nov62]，而用于最小化逻辑回归负对数似然(NLL)的SGD总是收敛到全局最优的最大似然估计(MLE)，即使数据不是线性可分的。

在第13.2节中，我们将感知机推广到非线性函数，从而显著增强其实用性。

#### 10.2.6 迭代加权最小二乘法

梯度下降是一种一阶优化方法，即它只使用一阶梯度来遍历损失曲面。这可能很慢，尤其是当空间中的一些方向陡峭下降，而另一些方向梯度较浅时，如图Figure 10.5a所示。对于这类问题，使用考虑曲面曲率的二阶优化方法可以快得多。

---

我们在第8.3节更详细地讨论此类方法。这里仅考虑一种对逻辑回归效果良好的简单二阶方法。我们聚焦于全批量设置（因此假设 \(N\) 较小），因为在随机设置下二阶方法更难奏效（例如，参见 [Byr+16; Liu+18b] 中的一些方法）。

经典的二阶方法是牛顿法。其更新形式如下：

$$  \boldsymbol{w}_{t+1}=\boldsymbol{w}_{t}-\boldsymbol{\eta}_{t}\mathbf{H}_{t}^{-1}\boldsymbol{g}_{t}   \tag*{(10.31)}$$

其中

$$  \mathbf{H}_{t}\triangleq\nabla^{2}\mathcal{L}(\boldsymbol{w})|_{\boldsymbol{w}_{t}}=\nabla^{2}\mathcal{L}(\boldsymbol{w}_{t})=\mathbf{H}(\boldsymbol{w}_{t})   \tag*{(10.32)}$$

被假定为正定矩阵，以确保更新定义良好。如果 Hessian 矩阵是精确的，我们可以将步长设为 \( \eta_{t}=1 \)。

现在我们将此方法应用于逻辑回归。回顾第10.2.3.3节，梯度与 Hessian 矩阵由下式给出：

$$  \nabla_{\boldsymbol{w}}\mathrm{N L L}(\boldsymbol{w})=\frac{1}{N}\sum_{n=1}^{N}(\mu_{n}-y_{n})\boldsymbol{x}_{n}   \tag*{(10.33)}$$

$$  \mathbf{H}=\frac{1}{N}\mathbf{X}^{\mathsf{T}}\mathbf{S}\mathbf{X}   \tag*{(10.34)}$$

$$  \mathbf{S}\triangleq\mathrm{diag}(\mu_{1}(1-\mu_{1}),\ldots,\mu_{N}(1-\mu_{N}))   \tag*{(10.35)}$$

因此，牛顿更新的形式为：

$$  \boldsymbol{w}_{t+1}=\boldsymbol{w}_{t}-\mathbf{H}^{-1}\boldsymbol{g}_{t}   \tag*{(10.36)}$$

$$  =w_{t}+(\mathbf{X}^{\mathsf{T}}\mathbf{S}_{t}\mathbf{X})^{-1}\mathbf{X}^{\mathsf{T}}(y-\boldsymbol{\mu}_{t})   \tag*{(10.37)}$$

$$  =\left(\mathbf{X}^{\mathsf{T}}\mathbf{S}_{t}\mathbf{X}\right)^{-1}\left[\left(\mathbf{X}^{\mathsf{T}}\mathbf{S}_{t}\mathbf{X}\right)w_{t}+\mathbf{X}^{\mathsf{T}}(y-\mu_{t})\right]   \tag*{(10.38)}$$

$$  =\left(\mathbf{X}^{\mathsf{T}}\mathbf{S}_{t}\mathbf{X}\right)^{-1}\mathbf{X}^{\mathsf{T}}\left[\mathbf{S}_{t}\mathbf{X}w_{t}+\mathbf{y}-\boldsymbol{\mu}_{t}\right]   \tag*{(10.39)}$$

$$  =\left(\mathbf{X}^{\mathsf{T}}\mathbf{S}_{t}\mathbf{X}\right)^{-1}\mathbf{X}^{\mathsf{T}}\mathbf{S}_{t}z_{t}   \tag*{(10.40)}$$

其中我们将工作响应定义为：

$$  z_{t}\triangleq\mathbf{X}w_{t}+\mathbf{S}_{t}^{-1}(\mathbf{y}-\boldsymbol{\mu}_{t})   \tag*{(10.41)}$$

且 \( \mathbf{S}_t = \mathrm{diag}(\mu_{t,n}(1 - \mu_{t,n})) \)。由于 \( \mathbf{S}_t \) 是对角矩阵，我们可以将目标值重写为分量形式如下：

$$  z_{t,n}=\boldsymbol{w}_{t}^{\mathsf{T}}\boldsymbol{x}_{n}+\frac{\boldsymbol{y}_{n}-\boldsymbol{\mu}_{t,n}}{\boldsymbol{\mu}_{t,n}(1-\boldsymbol{\mu}_{t,n})}   \tag*{(10.42)}$$

方程 (10.40) 是一个加权最小二乘问题（第11.2.2.4节）的实例，其最小化目标为：

$$  \sum_{n=1}^{N}S_{t,n}(z_{t,n}-\boldsymbol{w}_{t}^{\mathsf{T}}\boldsymbol{x}_{n})^{2}   \tag*{(10.43)}$$

作者：Kevin P. Murphy。 (C) MIT Press。采用 CC-BY-NC-ND 许可证。

---

算法 10.1：迭代重加权最小二乘 (IRLS)

1 w = 0

2 重复

3 | 对于 n = 1 到 N 执行

4 |  $ \begin{cases} a_n = w^\top x_n \\ \mu_n = \sigma(a_n) \\ s_n = \mu_n (1 - \mu_n) \\ z_n = a_n + \frac{y_n - \mu_n}{s_n} \end{cases} $

5 |  
6 |  
7 |  
8 S = diag(s_{1:N})
9 w = (X^\top S X)^{-1} X^\top S z

10 直到收敛

因此，整体方法被称为**迭代重加权最小二乘（IRLS）算法**，因为在每次迭代中，我们求解一个加权最小二乘问题，其中权重矩阵 $S_{t}$ 在每次迭代中变化。伪代码见 Algorithm 10.1。

注意，Fisher scoring 与 IRLS 相同，区别仅在于我们用对数似然的期望 Hessian 矩阵（即 Fisher 信息矩阵，见 Section 4.7.2）替代实际 Hessian 矩阵。由于 Fisher 信息矩阵与数据无关，可以预先计算，而 Hessian 矩阵必须在每次迭代中重新计算。对于参数较多的问题，这种方法可能更快。

#### 10.2.7 最大后验估计

在 Figure 10.4 中，我们观察到当参数相对于训练样本过多时，逻辑回归可能出现过拟合。这是由于最大似然能够找到迫使决策边界以合适方式“弯曲”以绕过样本的权重。为了实现这种行为，权重通常需要设置为较大的值。例如，在图 10.4 中，当使用次数 $K=1$ 时，两个输入权重（忽略偏置项）的 MLE 为

$$  \hat{w}=[0.51291712,0.11866937]   \tag*{(10.44)}$$

当使用次数 $K=2$ 时，我们得到

$$  \hat{w}=[2.27510513,0.05970325,11.84198867,15.40355969,2.51242311]   \tag*{(10.45)}$$

当 $K=4$ 时，我们得到

$$  \hat{w}=[-3.07813766,\cdots,-59.03196044,51.77152431,10.25054164]   \tag*{(10.46)}$$

减轻此类过拟合的一种方法是防止权重变得过大。我们可以采用零均值高斯先验 $p(\boldsymbol{w}) = \mathcal{N}(\boldsymbol{w}|\boldsymbol{0}, \mathrm{CI})$，然后使用 MAP 估计，如 Section 4.5.3 所述。新的训练目标变为

$$  \mathcal{L}(w)=\mathrm{N L L}(w)+\lambda||w||_{2}^{2}   \tag*{(10.47)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_134_551_379.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_620_135_959_380.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_215_433_550_675.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_600_448_958_690.jpg" alt="图像" width="31%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 10.6：方差为C的权重衰减应用于二类、二维逻辑回归问题，使用4次多项式。(a) C = 1。(b) C = 316。(c) C = 100,000。(d) 训练误差与测试误差随C的变化。由 $ \text{logreg\_poly\_demo.ipynb} $ 生成。</div>


其中 $ \|w\|_2^2 = \sum_{d=1}^D w_d^2 $，且 $ \lambda = 1/C $。这被称为 **ℓ2 正则化** 或 **权重衰减**。$ \lambda $ 的值越大，参数因“过大”（偏离零均值先验）而受到的惩罚就越重，从而模型的灵活性越低。参见图 10.6 的示例。

我们可以通过略微修改上述基于梯度的优化算法的输入来计算 **最大后验估计**。惩罚负对数似然的梯度与海森矩阵具有以下形式：

$$  \mathrm{PNLL}(\boldsymbol{w})=\mathrm{NLL}(\boldsymbol{w})+\lambda\boldsymbol{w}^{\mathrm{T}}\boldsymbol{w}   \tag*{(10.48)}$$

$$  \nabla_{w}P N L L(w)=g(w)+2\lambda w   \tag*{(10.49)}$$

$$  \nabla_{w}^{2}\mathrm{P N L L}(w)=\mathbf{H}(w)+2\lambda\mathbf{I}   \tag*{(10.50)}$$

其中 $ \boldsymbol{g}(\boldsymbol{w}) $ 是未惩罚负对数似然的梯度，$ \mathbf{H}(\boldsymbol{w}) $ 是其海森矩阵。

关于与 ℓ2 正则化逻辑回归相关的一个有趣练习，请参见习题 10.2。

作者：Kevin P. Murphy。(C) MIT 出版社。CC-BY-NC-ND 许可证。

---

#### 10.2.8 标准化

在第10.2.7节中，我们使用各向同性先验 $ \mathcal{N}(\boldsymbol{w}|\boldsymbol{0},\lambda^{-1}\mathbf{I}) $ 来防止过拟合。这隐含地编码了一个假设，即我们期望所有权重的大小相似，进而又编码了另一个假设，即我们期望所有输入特征的大小相似。然而，在许多数据集中，输入特征的尺度不同。在这种情况下，通常会对数据进行标准化，以确保每个特征均值为0、方差为1。这可以通过减去每个特征的均值并除以标准差来实现，如下所示：

$$  \mathrm{standardize}(x_{nd})=\frac{x_{nd}-\hat{\mu}_{d}}{\hat{\sigma}_{d}}   \tag*{(10.51)}$$

$$  \hat{\mu}_{d}=\frac{1}{N}\sum_{n=1}^{N}x_{nd}   \tag*{(10.52)}$$

$$  \hat{\sigma}_{d}^{2}=\frac{1}{N}\sum_{n=1}^{N}(x_{nd}-\hat{\mu}_{d})^{2}   \tag*{(10.53)}$$

另一种方法是使用最小-最大缩放，通过将输入重新缩放到区间[0,1]内。这两种方法都确保了特征在量级上可比，这有助于模型拟合和推断，即使我们不使用最大后验估计（MAP）。（关于这一点的讨论，请参见第11.7.5节。）

### 10.3 多项逻辑回归

多项逻辑回归是一种判别式分类模型，形式如下：

$$  p(y|\boldsymbol{x},\boldsymbol{\theta})=\mathrm{Cat}(y|\mathrm{softmax}(\mathbf{W}\boldsymbol{x}+\boldsymbol{b}))   \tag*{(10.54)}$$

其中，$ \boldsymbol{x} \in \mathbb{R}^D $ 是输入向量，$ y \in \{1, \ldots, C\} $ 是类别标签，$ \text{softmax}() $ 是softmax函数（见第2.5.2节），$ \mathbf{W} $ 是 $ C \times D $ 权重矩阵，$ \boldsymbol{b} $ 是 $ C $维偏置向量，$ \boldsymbol{\theta} = (\mathbf{W}, \boldsymbol{b}) $ 是所有参数。（此后我们假设在每个 $ \boldsymbol{x} $ 前添加了一个1，并将 $ \boldsymbol{b} $ 添加到 $ \mathbf{W} $ 的第一列，因此简化为 $ \boldsymbol{\theta} = \mathbf{W} $。）

设 $ \boldsymbol{a} = \boldsymbol{W} \boldsymbol{x} $ 为C维logits向量，则上式可重写为：

$$  p(y=c|\boldsymbol{x},\boldsymbol{\theta})=\frac{e^{a_{c}}}{\sum_{c^{\prime}=1}^{C}e^{a_{c^{\prime}}}}   \tag*{(10.55)}$$

由于归一化条件 $ \sum_{c=1}^{C} p(y_n = c | \boldsymbol{x}_n, \boldsymbol{\theta}) = 1 $，我们可以令 $ \boldsymbol{w}_C = \mathbf{0} $。（例如，在二元逻辑回归中，其中 $ C = 2 $，我们仅学习一个权重向量。）因此，参数 $ \boldsymbol{\theta} $ 对应于大小为 $ (C - 1) \times D $ 的权重矩阵 $ \mathbf{W} $，其中 $ \boldsymbol{x}_n \in \mathbb{R}^D $。

请注意，该模型假设标签是互斥的，即只有一个真实标签。对于某些应用（如图像标注），我们希望对一个输入预测一个或多个标签；在这种情况下，输出空间是 $\{1,\ldots,C\}$ 的子集集合。这被称为多标签分类，与多类分类相对。这可以看作是一个位向量 $\mathcal{Y}=\{0,1\}^{C}$，其中如果第 $c^{\prime}$ 个标签存在，则第 $c^{\prime}$ 个输出设置为1。我们可以使用修改版的

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_215_137_533_374.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_623_136_940_375.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图10.7：二维输入下三分类逻辑回归的示例。 (a) 原始特征。 (b) 二次特征。由 $ \text{logreg\_multiclass\_demo.ipynb} $ 生成。</div>


具有多个输出的二分类逻辑回归：

$$  p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})=\prod_{c=1}^{C}\mathrm{B e r}(\boldsymbol{y}_{c}|\sigma(\boldsymbol{w}_{c}^{\mathsf{T}}\boldsymbol{x}))   \tag*{(10.56)}$$

#### 10.3.1 线性与非线性分类器

逻辑回归在输入空间中计算线性决策边界，如图10.7(a)所示（ $\boldsymbol{x} \in \mathbb{R}^2$ 且类数 $C=3$）。然而，我们总可以通过某种方式变换输入以创建非线性边界。例如，假设将 $\boldsymbol{x} = (x_1, x_2)$ 替换为

$$  \phi(\boldsymbol{x})=[1,x_{1},x_{2},x_{1}^{2},x_{2}^{2},x_{1}x_{2}]   \tag*{(10.57)}$$

从而创建二次决策边界，如图10.7(b)所示。

#### 10.3.2 最大似然估计

本节讨论如何通过最小化负对数似然（NLL）来计算最大似然估计（MLE）。

##### 10.3.2.1 目标函数

NLL 由下式给出

$$  \mathrm{N L L}(\boldsymbol{\theta})=-\frac{1}{N}\log\prod_{n=1}^{N}\prod_{c=1}^{C}\mu_{n c}^{y_{n c}}=-\frac{1}{N}\sum_{n=1}^{N}\sum_{c=1}^{C}y_{n c}\log\mu_{n c}=\frac{1}{N}\sum_{n=1}^{N}\mathbb{H}_{c e}(\boldsymbol{y}_{n},\boldsymbol{\mu}_{n})   \tag*{(10.58)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

其中 $ \mu_{nc} = p(y_{nc} = 1|\boldsymbol{x}_{n}, \boldsymbol{\theta}) = \operatorname{softmax}(f(\boldsymbol{x}_{n}, \boldsymbol{\theta}))_{c} $，$ \boldsymbol{y}_{n} $ 是标签的独热编码（因此 $ y_{nc} = \mathbb{I}(y_{n} = c) $），而 $ \mathbb{H}_{ce}(\boldsymbol{y}_{n}, \boldsymbol{\mu}_{n}) $ 是交叉熵：

$$  \mathbb{H}_{c e}(\boldsymbol{p},\boldsymbol{q})=-\sum_{c=1}^{C}p_{c}\log q_{c}   \tag*{(10.59)}$$

##### 10.3.2.2 优化目标函数

为了找到最优解，我们需要求解 $ \nabla_w \text{NLL}(\boldsymbol{w}) = \boldsymbol{0} $，其中 $ \boldsymbol{w} $ 是权重矩阵 $ \boldsymbol{W} $ 的向量化版本，并且为简化符号暂时忽略偏置项。我们可以使用任何基于梯度的优化器来找到这样的驻点；下面给出一些例子。但首先，我们推导梯度和海森矩阵，然后证明目标函数是凸的。

##### 10.3.2.3 推导梯度

为了推导 NLL（负对数似然）的梯度，我们需要使用 softmax 函数的雅可比矩阵，如下所示（证明见练习 10.1）：

$$  \frac{\partial\mu_{c}}{\partial a_{j}}=\mu_{c}(\delta_{cj}-\mu_{j})   \tag*{(10.60)}$$

其中 $ \delta_{cj} = \mathbb{I}(c = j) $。例如，如果有 3 个类别，雅可比矩阵为：

$$  \begin{align*}\left[\frac{\partial\mu_c}{\partial a_j}\right]_{cj}=\begin{pmatrix}\mu_1(1-\mu_1)&-\mu_1\mu_2&-\mu_1\mu_3\\-\mu_2\mu_1&\mu_2(1-\mu_2)&-\mu_2\mu_3\\-\mu_3\mu_1&-\mu_3\mu_2&\mu_3(1-\mu_3)\end{pmatrix}\end{align*}   \tag*{(10.61)}$$

以矩阵形式，这可以写为：

$$  \frac{\partial\boldsymbol{\mu}}{\partial\boldsymbol{a}}=\left(\boldsymbol{\mu}\mathbf{1}^{\mathsf{T}}\right)\odot\left(\mathbf{I}-\mathbf{1}\boldsymbol{\mu}^{\mathsf{T}}\right)   \tag*{(10.62)}$$

其中 $\odot$ 是逐元素乘积，$\mu\mathbf{1}^{\top}$ 将 $\mu$ 复制到每一列，而 $\mathbf{1}\mu^{\top}$ 将 $\mu$ 复制到每一行。

我们现在推导单个样本（索引为 n）的 NLL 的梯度。为此，我们将 $ D \times C $ 的权重矩阵通过连接行并转置为列向量，展平为一个大小为 $ CD $（如果固定某一类的权重为零，则为 $ (C-1)D $）的向量 $ \boldsymbol{w} $。我们用 $ \boldsymbol{w}_j $ 表示与类别 j 相关联的权重向量。关于该向量的梯度由以下给出：

---

以下（其中我们使用克罗内克 delta 记号  $ \delta_{jc} $，当 j = c 时取 1，否则取 0）：

$$  \nabla_{\boldsymbol{w}_{j}}\mathrm{N L L}_{n}=\sum_{c}\frac{\partial\mathrm{N L L}_{n}}{\partial\mu_{n c}}\frac{\partial\mu_{n c}}{\partial a_{n j}}\frac{\partial a_{n j}}{\partial\boldsymbol{w}_{j}}   \tag*{(10.63)}$$

$$  =-\sum_{c}\frac{y_{nc}}{\mu_{nc}}\mu_{nc}(\delta_{jc}-\mu_{nj})\boldsymbol{x}_{n}   \tag*{(10.64)}$$

$$  =\sum_{c}y_{nc}(\mu_{nj}-\delta_{jc})\boldsymbol{x}_{n}   \tag*{(10.65)}$$

 $$ =(\sum_{c}y_{nc})\mu_{nj}\boldsymbol{x}_{n}-\sum_{c}\delta_{jc}y_{nj}\boldsymbol{x}_{n} $$ 

$$  =(\mu_{nj}-y_{nj})\boldsymbol{x}_{n}   \tag*{(10.67)}$$

我们可以对每个类别重复这一计算，得到完整的梯度向量。通过对所有样本求和，得到整体 NLL 的梯度，即为  $ D \times C $ 的矩阵

$$  g(w)=\frac{1}{N}\sum_{n=1}^{N}x_{n}(\mu_{n}-y_{n})^{\top}   \tag*{(10.68)}$$

其形式与二项逻辑回归情形相同，即误差项乘以输入。

##### 10.3.2.4 海森矩阵的推导

习题 10.1 要求你证明，多项逻辑回归 NLL 的海森矩阵为

$$  \mathbf{H}(\boldsymbol{w})=\frac{1}{N}\sum_{n=1}^{N}(\mathrm{diag}(\boldsymbol{\mu}_{n})-\boldsymbol{\mu}_{n}\boldsymbol{\mu}_{n}^{\mathsf{T}})\otimes(\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\mathsf{T}})   \tag*{(10.69)}$$

其中  $ \mathbf{A} \otimes \mathbf{B} $ 表示克罗内克积（参见第 7.2.5 节）。换句话说，分块  $ c, c' $ 的子矩阵为

$$  \mathbf{H}_{c,c^{\prime}}(\boldsymbol{w})=\frac{1}{N}\sum_{n}\mu_{n c}(\delta_{c,c^{\prime}}-\mu_{n,c^{\prime}})\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\mathsf{T}}   \tag*{(10.70)}$$

例如，如果我们有 3 个特征和 2 个类别，那么

$$  \mathbf{H}(\boldsymbol{w})=\frac{1}{N}\sum_{n}\begin{pmatrix}\mu_{n1}-\mu_{n1}^{2}&-\mu_{n1}\mu_{n2}\\ -\mu_{n1}\mu_{n2}&\mu_{n2}-\mu_{n2}^{2}\end{pmatrix}\otimes\begin{pmatrix}x_{n1}x_{n1}&x_{n1}x_{n2}&x_{n1}x_{n3}\\ x_{n2}x_{n1}&x_{n2}x_{n2}&x_{n2}x_{n3}\\ x_{n3}x_{n1}&x_{n3}x_{n2}&x_{n3}x_{n3}\end{pmatrix}   \tag*{(10.71)}$$

$$  =\frac{1}{N}\sum_{n}\begin{pmatrix}(\mu_{n1}-\mu_{n1}^{2})\mathbf{X}_{n}&-\mu_{n1}\mu_{n2}\mathbf{X}_{n}\\ -\mu_{n1}\mu_{n2}\mathbf{X}_{n}&(\mu_{n2}-\mu_{n2}^{2})\mathbf{X}_{n}\end{pmatrix}   \tag*{(10.72)}$$

其中  $ \mathbf{X}_n = \mathbf{x}_n \mathbf{x}_n^\top $。习题 10.1 还要求你证明这是一个正定矩阵，因此目标函数是凸的。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议.

---

#### 10.3.3 基于梯度的优化

利用第10.3.2.3节中的梯度来推导SGD（随机梯度下降）算法是直接的。类似地，我们可以使用第10.3.2.4节中的海森矩阵来推导二阶优化方法。然而，计算海森矩阵可能代价高昂，因此通常使用拟牛顿方法来近似它，例如有限内存的BFGS。（BFGS代表Broyden, Fletcher, Goldfarb and Shanno。）详见第8.3.2节。另一种与IRLS（迭代重加权最小二乘）类似的方法在第10.3.4节中描述。

所有这些方法都依赖于计算对数似然的梯度，而计算梯度又需要计算归一化概率，归一化概率可以通过 logits 向量 $ \mathbf{a} = \mathbf{W} \mathbf{x} $ 使用公式 (10.73) 计算：

$$  p(y=c|\boldsymbol{x})=\exp(a_{c}-\mathrm{l s e}(\boldsymbol{a}))   \tag*{(10.73)}$$

其中 $ l_{se} $ 是第2.5.4节定义的 log-sum-exp 函数。因此，许多软件库定义了一个交叉熵损失函数版本，该版本接受未归一化的 logits 作为输入。

#### 10.3.4 边界优化

在本节中，我们考虑使用一类称为边界优化的算法来拟合逻辑回归，这类算法在第8.7节中描述。其基本思想是迭代地在要最大化的函数上构造一个下界，然后更新这个界，使其“向上推动”真实函数。优化边界通常比直接更新函数更容易。

如果 $\ell(\boldsymbol{\theta})$ 是我们要最大化的凹函数，那么获得有效下界的一种方法是对其海森矩阵进行边界处理，即找到一个负定矩阵 $\mathbf{B}$ 使得 $\mathbf{H}(\boldsymbol{\theta}) \succ \mathbf{B}$。在这种情况下，可以证明

$$  \ell(\boldsymbol{\theta})\geq\ell(\boldsymbol{\theta}^{t})+(\boldsymbol{\theta}-\boldsymbol{\theta}^{t})^{\mathsf{T}}\boldsymbol{g}(\boldsymbol{\theta}^{t})+\frac{1}{2}(\boldsymbol{\theta}-\boldsymbol{\theta}^{t})^{\mathsf{T}}\mathbf{B}(\boldsymbol{\theta}-\boldsymbol{\theta}^{t})   \tag*{(10.74)}$$

其中 $  g(\theta^t) = \nabla \ell(\theta^t)  $。将 $  Q(\theta, \theta^t)  $ 定义为式 (10.74) 的右侧，则更新变为

$$  \boldsymbol{\theta}^{t+1}=\boldsymbol{\theta}^{t}-\mathbf{B}^{-1}\boldsymbol{g}(\boldsymbol{\theta}^{t})   \tag*{(10.75)}$$

这类似于牛顿更新，只是我们使用固定的矩阵 $\mathbf{B}$，而不是每次迭代都变化的 $\mathbf{H}(\boldsymbol{\theta}^{t})$。这可以让我们以较低的计算成本获得二阶方法的部分优势。

现在让我们将其应用到逻辑回归，参考 $ [\mathrm{Kri}+05] $。令 $ \boldsymbol{\mu}_n(\boldsymbol{w}) = [p(y_n = 1|\boldsymbol{x}_n, \boldsymbol{w}), \ldots, p(y_n = C|\boldsymbol{x}_n, \boldsymbol{w})] $ 和 $ \boldsymbol{y}_n = [\mathbb{I}(y_n = 1), \ldots, \mathbb{I}(y_n = C)] $。我们想要最大化对数似然，如下所示：

$$  \ell(\boldsymbol{w})=\sum_{n=1}^{N}\left[\sum_{c=1}^{C}y_{n c}\boldsymbol{w}_{c}^{\mathsf{T}}\boldsymbol{x}_{n}-\log\sum_{c=1}^{C}\exp(\boldsymbol{w}_{c}^{\mathsf{T}}\boldsymbol{x}_{n})\right]   \tag*{(10.76)}$$

梯度由下式给出（推导细节见第10.3.2.3节）：

$$  g(w)=\sum_{n=1}^{N}(y_{n}-\mu_{n}(w))\otimes x_{n}   \tag*{(10.77)}$$

---

其中 $ \otimes $ 表示克罗内克积（此处即为两个向量的外积）。海森矩阵由下式给出（推导细节见 10.3.2.4 节）：

$$  \mathbf{H}(\boldsymbol{w})=-\sum_{n=1}^{N}(\mathrm{diag}(\boldsymbol{\mu}_{n}(\boldsymbol{w}))-\boldsymbol{\mu}_{n}(\boldsymbol{w})\boldsymbol{\mu}_{n}(\boldsymbol{w})^{\mathsf{T}})\otimes(\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\mathsf{T}})   \tag*{(10.78)}$$

我们可以构造海森矩阵的一个下界，如文献 [Boh92] 所示：

$$  \mathbf{H}(\boldsymbol{w})\succ-\frac{1}{2}[\mathbf{I}-\mathbf{1}\mathbf{1}^{\mathsf{T}}/C]\otimes\left(\sum_{n=1}^{N}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\mathsf{T}}\right)\triangleq\mathbf{B}   \tag*{(10.79)}$$

其中 $\mathbf{I}$ 是 $C$ 维单位矩阵，$\mathbf{1}$ 是元素全为 1 的 $C$ 维向量。$^{1}$ 在二分类情形下，该下界变为

$$  \mathbf{H}(\boldsymbol{w})\succ-\frac{1}{2}\left(1-\frac{1}{2}\right)\left(\sum_{n=1}^{N}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\top}\right)=-\frac{1}{4}\mathbf{X}^{\top}\mathbf{X}   \tag*{(10.80)}$$

这是因为 $\mu_n \leq 0.5$，因此 $-(\mu_n - \mu_n^2) \geq -0.25$。

我们可以利用这个下界来构建一个 MM 算法以求解最大似然估计。其更新公式为：

$$  \boldsymbol{w}^{t+1}=\boldsymbol{w}^{t}-\mathbf{B}^{-1}\boldsymbol{g}(\boldsymbol{w}^{t})   \tag*{(10.81)}$$

该迭代过程可能比 IRLS（第 10.2.6 节）更快，因为我们可以独立于 $N$ 的时间预计算 $\mathbf{B}^{-1}$，而无需在每次迭代中求逆海森矩阵。例如，考虑二分类情形，此时 $\mathbf{g}^t = \nabla \ell(\mathbf{w}^t) = \mathbf{X}^\top(\mathbf{y} - \boldsymbol{\mu}^t)$，其中 $\boldsymbol{\mu}^t = [p_n(\mathbf{w}^t), (1 - p_n(\mathbf{w}^t))]_{n=1}^N$。更新公式变为：

$$  \boldsymbol{w}^{t+1}=\boldsymbol{w}^{t}-4(\mathbf{X}^{\mathsf{T}}\mathbf{X})^{-1}\boldsymbol{g}^{t}   \tag*{(10.82)}$$

将其与方程 $(10.37)$ 对比，后者具有如下形式：

$$  \boldsymbol{w}^{t+1}=\boldsymbol{w}^{t}-\mathbf{H}^{-1}\boldsymbol{g}(\boldsymbol{w}^{t})=\boldsymbol{w}^{t}-(\mathbf{X}^{\mathrm{T}}\mathbf{S}^{t}\mathbf{X})^{-1}\boldsymbol{g}^{t}   \tag*{(10.83)}$$

其中 $\mathbf{S}^t = \mathrm{diag}(\boldsymbol{\mu}^t \odot (1 - \boldsymbol{\mu}^t))$。我们看到方程 (10.82) 的计算速度更快，因为我们可以预计算常数矩阵 $(\mathbf{X}^\top \mathbf{X})^{-1}$。

#### 10.3.5 最大后验估计

在第 10.2.7 节中，我们讨论了 $\ell_2$ 正则化对于二分类逻辑回归的好处。这些好处在多分类情形下同样适用。然而，如文献 [HTF09, Ex.18.3] 所指出的，还存在一个额外且令人惊讶的好处——参数的可识别性。（如果存在唯一的值使得似然函数最大化，我们就称参数是可识别的；等价地，我们要求负对数似然函数是严格凸的。）

---

为了理解可辨识性为何是个问题，回顾一下多分类逻辑回归的形式为

$$  p(y=c|\boldsymbol{x},\mathbf{W})=\frac{\exp(\boldsymbol{w}_{c}^{T}\boldsymbol{x})}{\sum_{k=1}^{C}\exp(\boldsymbol{w}_{k}^{T}\boldsymbol{x})}   \tag*{(10.84)}$$

其中 $\mathbf{W}$ 是一个 $C \times D$ 的权重矩阵。我们可以任意地将其中一个类别（例如 $c = C$）的 $\boldsymbol{w}_c$ 定义为 $\mathbf{0}$，因为 $p(y = C|\boldsymbol{x}, \mathbf{W}) = 1 - \sum_{c=1}^{C-1} p(y = c|\boldsymbol{x}, \boldsymbol{w})$。在这种情况下，模型的形式为

$$  p(y=c|\boldsymbol{x},\mathbf{W})=\frac{\exp(\boldsymbol{w}_{c}^{T}\boldsymbol{x})}{1+\sum_{k=1}^{C-1}\exp(\boldsymbol{w}_{k}^{T}\boldsymbol{x})}   \tag*{(10.85)}$$

如果我们不将其中一个向量“钳制”为某个常数值，参数将是不可辨识的。然而，假设我们不将 $\boldsymbol{w}_c$ 钳制为 $\mathbf{0}$，因此我们使用的是公式 10.84，但通过优化以下目标函数添加了 $\ell_2$ 正则化：

$$  \mathrm{PNLL}(\mathbf{W})=-\sum_{n=1}^{N}\log p(y_{n}|\boldsymbol{x}_{n},\mathbf{W})+\lambda\sum_{c=1}^{C}||\boldsymbol{w}_{c}||_{2}^{2}   \tag*{(10.86)}$$

其中我们将 $1/N$ 项吸收进了 $\lambda$。在最优解处，我们有 $\sum_{c=1}^{C} \hat{w}_{cj} = 0$ 对于 $j = 1 : D$，因此权重自动满足零和约束，从而使其具有唯一可辨识性。

为了理解原因，注意在最优解处我们有

$$  \nabla NLL(\boldsymbol{w})+2\lambda\boldsymbol{w}=\mathbf{0}   \tag*{(10.87)}$$

$$  \sum_{n}(y_{n}-\mu_{n})\otimes\boldsymbol{x}_{n}=\lambda\boldsymbol{w}   \tag*{(10.88)}$$

因此对于任意特征维度 j，我们有

$$  \lambda\sum_{c}w_{cj}=\sum_{n}\sum_{c}(y_{nc}-\mu_{nc})x_{nj}=\sum_{n}(\sum_{c}y_{nc}-\sum_{c}\mu_{nc})x_{nj}=\sum_{n}(1-1)x_{nj}=0   \tag*{(10.89)}$$

因此如果 $\lambda > 0$，我们有 $\sum_c \hat{w}_{cj} = 0$，所以对于每个特征维度，权重在类别上求和为零。

#### 10.3.6 最大熵分类器

回顾一下，多项逻辑回归模型可以写为

$$  p(y=c|\boldsymbol{x},\mathbf{W})=\frac{\exp(\boldsymbol{w}_{c}^{\mathsf{T}}\boldsymbol{x})}{Z(\boldsymbol{w},\boldsymbol{x})}=\frac{\exp(\boldsymbol{w}_{c}^{\mathsf{T}}\boldsymbol{x})}{\sum_{c^{\prime}=1}^{C}\exp(\boldsymbol{w}_{c^{\prime}}^{\mathsf{T}}\boldsymbol{x})}   \tag*{(10.90)}$$

其中 $Z(\boldsymbol{w}, \boldsymbol{x}) = \sum_{c} \exp(\boldsymbol{w}_{c}^{\top} \boldsymbol{x})$ 是配分函数（归一化常数）。该模型对每个类别使用相同的特征，但使用不同的权重向量。该模型有一个轻微的扩展，允许我们使用依赖于类别的特征。这个模型可以写为

$$  p(y=c|\boldsymbol{x},\boldsymbol{w})=\frac{1}{Z(\boldsymbol{w},\boldsymbol{x})}\exp(\boldsymbol{w}^{\top}\phi(\boldsymbol{x},c))   \tag*{(10.91)}$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_331_124_840_406.jpg" alt="图像" width="44%" /></div>


<div style="text-align: center;">图 10.8：一个简单的标签层次结构示例。同一个椭圆内的节点之间存在互斥关系。</div>


其中 $ \phi(x,c) $ 是类别 c 的特征向量。这被称为最大熵分类器，简称 maxent 分类器。（该术语的来源在第 3.4.4 节中解释。）

Maxent 分类器将多项逻辑回归作为特例。为了说明这一点，令 $ \boldsymbol{w} = [\boldsymbol{w}_1, \ldots, \boldsymbol{w}_C] $，并如下定义特征向量：

$$  \phi(\boldsymbol{x},c)=[\mathbf{0},\ldots,\boldsymbol{x},\ldots,\mathbf{0}]   \tag*{(10.92)}$$

其中 $\boldsymbol{x}$ 嵌入在第 $c$ 个块中，其余块为零。此时，$\boldsymbol{w}^{\mathrm{T}}\phi(\boldsymbol{x},c)=\boldsymbol{w}_{c}^{\mathrm{T}}\boldsymbol{x}$，因此我们恢复了多项逻辑回归。

Maxent 分类器在自然语言处理领域应用非常广泛。例如，考虑语义角色标注问题，将单词 x 分类为语义角色 y，如人、地点或事物。我们可以定义如下（二值）特征：

$$  \phi_{1}(\boldsymbol{x},y)=\mathbb{I}\left(y=person\wedge\boldsymbol{x}occurs after“Mr.”or“Mrs”\right)   \tag*{(10.93)}$$

$$  \phi_{2}(\boldsymbol{x},y)=\mathbb{I}(y=\mathrm{person}\land\boldsymbol{x}\mathrm{is\ in\ whitelist\ of\ common\ names})   \tag*{(10.94)}$$

$$  \phi_{3}(\boldsymbol{x},y)=\mathbb{I}\left(y=place\wedge\boldsymbol{x}is in Google maps\right)   \tag*{(10.95)}$$

我们看到，所使用的特征依赖于标签。

创建这些特征主要有两种方式。第一种是使用各种模板手动指定许多可能有用的特征，然后使用特征选择算法，例如第 11.4.7 节的群组套索方法。第二种是使用启发式特征生成方法，逐步向模型添加特征。

#### 10.3.7 层次分类

有时，可能标签集合可以被组织成层次结构或分类法。例如，我们可能想要预测图像中是什么动物：可能是狗或猫；如果它是

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

狗，可能是金毛寻回犬或德国牧羊犬等。直观上，尝试预测我们最有把握的最精确标签是有意义的 [Den+12]，也就是说，系统应当"对冲其赌注"。

实现这一目标的一种简单方法（由 [RF17] 提出）如下：首先，为树中每个可能的节点创建一个带有二元输出标签的模型。在训练模型之前，我们会使用标签涂抹（label smearing），使标签传播到其所有父节点（上位词）。例如，如果一张图片被标注为"金毛寻回犬"，我们也会将其标注为"狗"。如果我们在这样涂抹后的数据上训练一个多标签分类器（生成一个二元标签向量 $ p(\mathbf{y}|\mathbf{x}) $），它将执行层级分类，预测出不同抽象层次上的一组标签。

然而，这种方法可能同时以概率 1.0 预测出"金毛寻回犬"、"猫"和"鸟"，因为模型没有捕捉到某些标签互斥的事实。为防止这种情况，我们可以为所有兄弟标签节点添加互斥约束，如图 10.8 所示。例如，该模型强制要求 $ p(\text{哺乳动物}|\boldsymbol{x}) + p(\text{鸟}|\boldsymbol{x}) = 1 $，因为这两个标签是根节点的子节点。我们还可以进一步将哺乳动物的概率划分为狗和猫，因此有 $ p(\text{狗}|\boldsymbol{x}) + p(\text{猫}|\boldsymbol{x}) = p(\text{哺乳动物}|\boldsymbol{x}) $。

[Den+14; Din+15] 通过使用条件图模型对上述方法进行了推广，该模型中的图结构可以比树更复杂。此外，除了硬约束外，他们还允许标签之间具有软约束。

#### 10.3.8 处理大量类别

在本节中，我们讨论当存在大量潜在标签时出现的一些问题，例如，标签对应某种语言的词汇。

##### 10.3.8.1 层级softmax

在常规的softmax分类器中，计算归一化常数（计算对数似然梯度所需）需要 $ O(C) $ 时间，当 $ C $ 很大时，这可能成为瓶颈。然而，如果我们把标签组织成一棵树，则可以通过将根节点到叶子节点路径上每条边的概率相乘，以 $ O(\log C) $ 时间计算出任意标签的概率。例如，考虑图 10.9 中的树，我们有：

$$  p(y=\mathrm{I}^{\prime}\mathrm{m}|C)=0.57\times0.68\times0.72=0.28   \tag*{(10.96)}$$

因此，我们将"平坦"的输出softmax替换为树结构的二元分类器序列。这被称为层级softmax [Goo01; MB05]。

构造这种树的一个好方法是使用霍夫曼编码，如 [Mik+13a] 中建议的那样，将最频繁的标签放置在树的顶部附近。（关于基于最常见的标签聚类的不同方法，请参见 [Gra+17]。关于另一种基于采样标签的方法，请参见 [Tit16]。）

##### 10.3.8.2 类别不平衡与长尾

当存在大量类别时，另一个常见问题是：对于大多数类别，我们可能只有很少的样本。更精确地说，如果 $ N_c $ 是类别 $ c $ 的样本数，那么经验分布 $ p(N_1, \ldots, N_C) $ 可能具有长尾。结果就是类别的极端不平衡。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_179_117_622_342.jpg" alt="Image" width="38%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_631_117_1012_341.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图10.9：平坦与层次化softmax模型 $ p(w|C) $，其中 $ C $ 为输入特征（上下文），$ w $ 为输出标签（词）。改编自 https://www.quora.com/What-is-hierarchical-softmax。</div>


类别不平衡（参见例如 [ASR15]）。由于稀有类别对整体损失的影响小于常见类别，模型可能会“将注意力集中在”常见类别上。

一种可用的方法是通过设置偏置项 $ \boldsymbol{b} $ 使得 $ \text{softmax}(\boldsymbol{b})_c = N_c/N $；即使使用 $ \boldsymbol{w} = \mathbf{0} $ 的权重，该模型也能匹配经验标签先验。然后我们可以通过使用 **logit调整（logit adjustment）** [Men+21] 来“减去”先验项，从而确保所有组别的良好性能。

另一种常见方法是在训练之前（或期间）对数据进行重采样，使其更均衡。具体来说，假设我们从类别 $ c $ 中采样一个数据点的概率为

$$  p_{c}=\frac{N_{c}^{q}}{\sum_{i}^{C}N_{i}^{q}}   \tag*{(10.97)}$$

如果设置 $ q = 1 $，则恢复标准实例平衡采样，此时 $ p_c \propto N_c $；常见类别将被更频繁地采样，稀有类别则较少。如果设置 $ q = 0 $，则恢复类别平衡采样，其中 $ p_c = 1/C $；这可以看作先均匀随机采样一个类别，再采样该类别的一个实例。最后，我们还可以考虑其他选项，例如 $ q = 0.5 $，这被称为平方根采样 [Mah+18]。

另一种简单且能有效处理长尾分布的方法是使用 **最近类均值分类器**。其形式为

$$  f(\boldsymbol{x})=\underset{c}{\arg\min}||\boldsymbol{x}-\boldsymbol{\mu}_{c}||_{2}^{2}   \tag*{(10.98)}$$

其中 $ \boldsymbol{\mu}_c = \frac{1}{N_c} \sum_{n:y_n = c} \boldsymbol{x}_n $ 是属于类别 $ c $ 的特征均值。如我们在 9.2.5 节中所讨论，该分类器可诱导出softmax后验概率。如果先在原始非平衡数据上使用交叉熵损失训练一个DNN分类器（参见第三部分），通过神经网络学习良好特征，然后将公式(10.98)中的 $ \boldsymbol{x} $ 替换为 $ \phi(\boldsymbol{x}) $，则能获得更优结果。这种简单方法在长尾分布上可以达到非常出色的性能 [Kan+20]。

作者：Kevin P. Murphy。 (C) MIT Press。 采用CC-BY-NC-ND许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_193_126_564_372.jpg" alt="图像" width="32%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_601_127_971_372.jpg" alt="图像" width="32%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 10.10: (a) 对包含异常值（用 x 标记）的数据进行逻辑回归。训练点在垂直方向进行了微扰抖动以避免过度重叠。垂直线是决策边界及其后验置信区间。(b) 与 (a) 相同，但使用混合似然的鲁棒模型。改编自 [Mar18] 的图 4.13。由 logreg_iris_bayes_robust_1d_pymc3.ipynb 生成。</div>

### 10.4 鲁棒逻辑回归 *

有时数据中存在异常值，这通常源于标注错误，也称为标签噪声。为了防止模型受到此类污染的不利影响，我们将使用鲁棒逻辑回归。本节讨论一些解决该问题的方法。（注意，这些方法也可应用于深度神经网络。关于标签噪声及其对深度学习影响的更全面综述，请参见 [Han+20]。）

#### 10.4.1 混合似然模型

定义鲁棒逻辑回归模型的最简单方法之一是修改似然，使其以概率 $\pi$ 均匀随机地生成每个输出标签 $y$，否则使用通常的条件模型生成。在二分类情况下，这变为

$$ p(y|\boldsymbol{x}) = \pi \mathrm{Ber}(y|0.5) + (1-\pi) \mathrm{Ber}(y|\sigma(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x})) \tag*{(10.99)} $$

这种使用观测模型的混合模型来增强鲁棒性的方法，可应用于许多不同的模型（例如深度神经网络）。

我们可以使用标准方法拟合该模型，例如 SGD 或 MCMC 等贝叶斯推断方法。例如，我们创建一个在第 4.6.7.2 节讨论的一维两类鸢尾花数据集的“污染”版本。我们添加了 6 个第 1 类（维吉尼亚鸢尾）但具有异常低花萼长度的样本。在图 10.10a 中，我们展示了将标准（贝叶斯）逻辑回归模型拟合到该数据集的结果。在图 10.10b 中，我们展示了拟合上述鲁棒模型的结果。在后一种情况下，我们看到决策边界与我们从未污染数据推断出的结果相似，如图 4.20b 所示。我们还看到，与使用非鲁棒模型相比，决策边界位置的后验不确定性更小。

---

#### 10.4.2 双温度损失

在本节中，我们介绍由 [Ami+19] 提出的鲁棒逻辑回归方法。

第一个观察是，距离决策边界较远但标签错误的样本，如果损失函数是凸的，将会对模型产生过度的不利影响 [LS10]。这一问题可以通过将通常的交叉熵损失替换为“温度调节版”来克服，该版本使用温度参数 $0 \leq t_1 < 1$ 确保来自异常值的损失有界。特别地，考虑标准相对熵损失函数：

$$  \mathcal{L}(\boldsymbol{y},\hat{\boldsymbol{y}})=\mathbb{H}_{c e}(\boldsymbol{y},\hat{\boldsymbol{y}})=\sum_{c}y_{c}\log\hat{y}_{c}   \tag*{(10.100)}$$

其中 $\boldsymbol{y}$ 是真实标签分布（通常是 one-hot 形式），$\hat{\boldsymbol{y}}$ 是预测分布。我们定义温度调节交叉熵损失如下：

$$  \mathcal{L}(\boldsymbol{y},\hat{\boldsymbol{y}})=\sum_{c}\left[y_{c}(\log_{t_{1}}y_{c}-\log_{t_{1}}\hat{y}_{c})-\frac{1}{2-t_{1}}(y_{c}^{2-t_{1}}-\hat{y}_{c}^{2-t_{1}})\right]   \tag*{(10.101)}$$

当真实分布 $\boldsymbol{y}$ 是 one-hot 形式且其所有质量都在类别 $c$ 上时，上述损失简化为：

$$  \mathcal{L}(c,\hat{\mathbf{y}})=-\log_{t_{1}}\hat{y}_{c}-\frac{1}{2-t_{1}}\left(1-\sum_{c^{\prime}=1}^{C}\hat{y}_{c^{\prime}}^{2-t_{1}}\right)   \tag*{(10.102)}$$

这里 $\log_{t}$ 是对数函数的温度调节版：

$$  \log_{t}(x)\triangleq\frac{1}{1-t}(x^{1-t}-1)   \tag*{(10.103)}$$

该函数单调递增且为凹函数，当 $t = 1$ 时退化为标准（自然）对数。（类似地，当 $t = 1$ 时，温度调节交叉熵退化为标准交叉熵。）然而，对于 $0 \leq t < 1$，温度调节对数函数的下界为 $\-1/(1-t)$，因此交叉熵损失的上界有界（见图 10.11）。

第二个观察是，距离决策边界较近但标签错误的样本，需要使用比基于指数函数的 softmax 具有更重尾部的传递函数（该函数将激活值 $\mathbb{R}^C$ 映射到概率 $[0,1]^C$），从而能够“越过”邻近样本的局部区域。特别地，标准 softmax 定义为

$$  \hat{y}_{c}=\frac{a_{c}}{\sum_{c^{\prime}=1}^{C}\exp(a_{c^{\prime}})}=\exp\left[a_{c}-\log\sum_{c^{\prime}=1}^{C}\exp(a_{c^{\prime}})\right]   \tag*{(10.104)}$$

其中 $\boldsymbol{a}$ 是 logits 向量。我们可以通过使用温度调节 softmax 来得到重尾版本，该版本使用温度参数 $t_2 > 1 > t_1$ 如下：

$$  \hat{y}_{c}=\exp_{t_{2}}(a_{c}-\lambda_{t_{2}}(\boldsymbol{a}))   \tag*{(10.105)}$$

其中

$$  \exp_{t}(x)\triangleq[1+(1-t)x]_{+}^{1/(1-t)}   \tag*{(10.106)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_228_123_535_409.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_631_121_946_411.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图10.11: (a) 逻辑损失与调和逻辑损失的示意图，其中 $ t_{1}=0.8 $。(b) Sigmoid函数与调和Sigmoid传递函数的示意图，其中 $ t_{2}=2.0 $。图片来源：https://ai.googleblog.com/2019/08/bi-tempered-logistic-loss-for-training.html。经Ehsan Amid许可使用。</div>


是指数函数的调和版本。（当 $ t \to 1 $ 时，它退化为标准指数函数。）在图10.11(右)中，我们展示了调和softmax（在二分类情形下）具有更重的尾部，这正是我们所期望的。

剩下的问题是计算 $ \lambda_{t_{2}}(\boldsymbol{a}) $ 的方法。它必须满足以下不动点方程：

$$  \sum_{c=1}^{C}\exp_{t_{2}}(a_{c}-\lambda(\boldsymbol{a}))=1   \tag*{(10.107)}$$

我们可以通过二分搜索，或使用算法10.2中的迭代过程来求解λ。

算法10.2：用于计算方程(10.107)中 $\lambda(a)$ 的迭代算法。摘自[AWS19]。

1 输入：logits值 $a$，温度 $t > 1$

2 $\mu := \max(a)$

3 $a := a - \mu$

4 while $a$ 未收敛 do

5 $\left[\begin{array}{c} Z(a) := \sum_{c=1}^{C} \exp_t(a_c) \\ a := Z(a)^{1-t}(a - \mu\mathbf{1}) \end{array}\right]$

7 返回 $-\log_t \frac{1}{Z(a)} + \mu$

将调和softmax与调和交叉熵相结合，便得到了一种称为**双调和逻辑回归**的方法。在图10.12中，我们展示了二维情况下的一个示例。第一行为标准逻辑回归，第二行为双调和逻辑回归。第一列为干净数据。第二列为边界附近存在标签噪声。鲁棒版本使用 $ t_{1}=1 $（标准交叉熵），但 $ t_{2}=4 $（具有重尾的调和softmax）。第三列为远离边界的标签噪声。

---

干净数据集

逻辑损失

<div style="text-align: center;">小边缘噪声</div>

<div style="text-align: center;">大边缘噪声</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_369_171_492_292.jpg" alt="Image" width="10%" /></div>

随机噪声

<div style="text-align: center;"><img src="imgs/img_in_image_box_648_170_770_290.jpg" alt="Image" width="10%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_785_171_906_290.jpg" alt="Image" width="10%" /></div>

双温度逻辑损失

<div style="text-align: center;"><img src="imgs/img_in_image_box_368_318_492_439.jpg" alt="Image" width="10%" /></div>

$ (t_{1}=0.2, t_{2}=4.0) $ 有界且重尾

<div style="text-align: center;"><img src="imgs/img_in_image_box_508_319_631_439.jpg" alt="Image" width="10%" /></div>

<div style="text-align: center;">(a)</div>

$ (t_{1}=1.0, t_{2}=4.0) $

仅重尾

<div style="text-align: center;"><img src="imgs/img_in_image_box_647_318_770_439.jpg" alt="Image" width="10%" /></div>

<div style="text-align: center;">(b)</div>

$ (t_{1}=0.2, t_{2}=1.0) $

仅有界

<div style="text-align: center;"><img src="imgs/img_in_image_box_785_318_906_439.jpg" alt="Image" width="10%" /></div>

<div style="text-align: center;">(c)</div>

$ (t_{1}=0.2, t_{2}=4.0) $ 有界且重尾

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图10.12：具有标签噪声的数据上标准逻辑回归与双温度逻辑回归的对比。来自 https://ai.googleblog.com/2019/08/bi-tempered-logistic-loss-for-training.html。经Ehsan Amid友善许可使用。</div>

来自边界。鲁棒版本使用 $ t_{1}=0.2 $（具有有界损失的温度调节交叉熵），但 $ t_{2}=1 $（标准softmax）。第四列包含两种噪声；在这种情况下，鲁棒版本使用 $ t_{1}=0.2 $ 和 $ t_{2}=4 $。

### 10.5 贝叶斯逻辑回归*

到目前为止，我们关注的是参数的点估计，无论是MLE（最大似然估计）还是MAP（最大后验估计）。然而，在某些情况下，我们想要计算后验 $ p(\boldsymbol{\omega}|\mathcal{D}) $ 以捕获我们的不确定性。这在数据较少且选择错误决策可能代价高昂的情况下尤其有用。

与线性回归不同，对于逻辑回归模型，无法精确计算后验。可以使用多种近似算法。在本节中，我们使用其中最简单的一种，即拉普拉斯近似（第4.6.8.2节）。更高级的近似方法请参见本书的续篇[Mur23]。

#### 10.5.1 拉普拉斯近似

如第4.6.8.2节所述，拉普拉斯近似使用高斯分布来近似后验。高斯分布的均值等于MAP估计 $ \hat{w} $，协方差等于在MAP估计处计算的Hessian矩阵H的逆，即 $ p(\boldsymbol{w}|\mathcal{D}) \approx \mathcal{N}(\boldsymbol{w}|\hat{\boldsymbol{w}}, \mathbf{H}^{-1}) $。我们可以使用标准的优化方法（见第10.2.7节）找到众数，然后使用结果

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_216_140_540_399.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_621_140_947_402.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_460_539_720.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_620_461_947_720.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 10.13: (a) 数据示意图。 (b) 逻辑回归模型的对数似然。线条从原点指向 MLE 方向（MLE 位于无穷远处）。数字对应参数空间中的 4 个点，分别对应 (a) 中的线条。 (c) 未经归一化的对数后验（假设为模糊的球形先验）。 (d) 后验的拉普拉斯近似。改编自 Mark Girolami 的图示。由 $ \logreg\_laplace\_demo.ipymb $ 生成。</div>


从第 10.2.3.4 节中计算在众数处的 Hessian 矩阵。

以图 10.13(a) 所示的数据为例。存在许多参数设定对应着完美分离训练数据的直线；我们展示了 4 条示例直线。似然曲面如图 10.13(b) 所示。对角线将原点连接到网格中具有最大似然的点，即 $ \hat{\mathbf{w}}_{\text{mle}} = (8.0, 3.4) $。（无约束的 MLE 的 $ \|\mathbf{w}\| = \infty $，正如我们在第 10.2.7 节中所讨论的；该点可通过沿对角线无限向右移动得到。）

对于图 10.13(a) 中的每条决策边界，我们在图 10.13(b) 中绘制了相应的参数向量。这些参数值分别为 $ \boldsymbol{w}_1 = (3,1) $、 $ \boldsymbol{w}_2 = (4,2) $、 $ \boldsymbol{w}_3 = (5,3) $ 和 $ \boldsymbol{w}_4 = (7,3) $。这些点均近似满足 $ \boldsymbol{w}_i(1)/\boldsymbol{w}_i(2) \approx \hat{\boldsymbol{w}}_{\mathrm{m l e}}(1)/\hat{\boldsymbol{w}}_{\mathrm{m l e}}(2) $，因此接近

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_213_140_541_400.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_620_138_947_402.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_213_459_540_721.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_619_459_948_721.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图10.14：二维逻辑回归模型的后验预测分布。(a)：$ p(y=1|\boldsymbol{x},\hat{\boldsymbol{w}}_{map}) $ 的等高线图。(b)：后验预测分布的样本。(c)：对这些样本取平均。(d)：调节后的输出（probit近似）。图片改编自 Mark Girolami。由 $ \text{logreg\_place\_demo.ipynb} $ 生成。</div>

最大似然决策边界的方向。点按权重范数递增排序：$ (3.16, 4.47, 5.83, $ 和 $ (7.62) $。

为了保证解的唯一性，我们采用一个以原点为中心的（球形）高斯先验：$ \mathcal{N}(\mathbf{w}|\mathbf{0},\sigma^2\mathbf{I}) $。$ \sigma^2 $ 的值控制先验的强度。如果令 $ \sigma^2=0 $，则强制最大后验（MAP）估计为 $ \mathbf{w}=\mathbf{0} $；这将导致预测具有最大不确定性，因为所有点 $ \mathbf{x} $ 产生的预测分布均为 $ p(y=1|\mathbf{x})=0.5 $。如果令 $ \sigma^2=\infty $，则先验变为无信息，MAP估计退化为最大似然估计（MLE），导致预测不确定性最小（特别地，由于数据可分，所有正类点的 $ p(y=1|\mathbf{x})=1.0 $，所有负类点的 $ p(y=1|\mathbf{x})=0.0 $）。作为折中（以便生成漂亮的插图），我们选择 $ \sigma^2=100 $。

将这个先验与似然函数相乘，得到图-所示的未归一化后验。

---

图10.13(c)。MAP估计以红点表示。该后验的拉普拉斯近似如图10.13(d)所示。我们看到它正确捕捉了众数（由构造决定），但后验的形状有些扭曲。（西南-东北方向捕捉了关于权重 w 幅度的不确定性，而东南-西北方向捕捉了关于决策边界方向的不确定性。）

在图10.14中，我们展示了后验预测分布的等高线。图10.14(a)显示了使用MAP估计的插件近似。我们看到决策边界不存在不确定性，尽管我们正在生成关于标签的概率预测。图10.14(b)展示了当我们从高斯后验中抽取样本并代入时的情况。现在我们看到“最佳”决策边界的方向存在相当大的不确定性。图10.14(c)显示了这些样本的平均值。通过对多个预测求平均，我们看到随着远离训练数据，决策边界的不确定性“扩散开来”。图10.14(d)显示了probit近似与蒙特卡洛近似给出了非常相似的结果。

#### 10.5.2 近似后验预测

后验 $ p(\boldsymbol{w}|\mathcal{D}) $ 告诉我们关于给定数据下的模型参数的一切信息。然而，在机器学习应用中，主要任务通常是给定输入 x 预测输出 y，而不是试图理解模型参数。因此，我们需要计算后验预测分布

$$  p(y|\boldsymbol{x},\mathcal{D})=\int p(y|\boldsymbol{x},\boldsymbol{w})p(\boldsymbol{w}|\mathcal{D})d\boldsymbol{w}   \tag*{(10.108)}$$

正如我们在第4.6.7.1节中讨论的，一种简单的方法是首先计算参数的点估计 $ \hat{w} $，例如MLE或MAP估计，然后通过假设 $ p(\boldsymbol{w}|\mathcal{D}) = \delta(\boldsymbol{w} - \hat{\boldsymbol{w}}) $ 忽略所有后验不确定性。在这种情况下，上述积分简化为以下插件近似：

$$  p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})\approx\int p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{w})\delta(\boldsymbol{w}-\hat{\boldsymbol{w}})d\boldsymbol{w}=p(\boldsymbol{y}|\boldsymbol{x},\hat{\boldsymbol{w}})   \tag*{(10.109)}$$

然而，如果我们想要计算预测中的不确定性，应该使用非退化的后验。正如我们将看到的，通常使用高斯后验。但我们仍需要近似方程(10.108)中的积分。下面我们讨论一些方法。

##### 10.5.2.1 蒙特卡洛近似

最简单的方法是使用蒙特卡洛近似来逼近积分。这意味着我们从后验中抽取 $S$ 个样本，$\boldsymbol{w}_s \sim p(\boldsymbol{w}|\mathcal{D})$，然后计算

$$  p(y=1|\boldsymbol{x},\mathcal{D})\approx\frac{1}{S}\sum_{s=1}^{S}\sigma(\boldsymbol{w}_{s}^{\mathsf{T}}\boldsymbol{x})   \tag*{(10.110)}$$

##### 10.5.2.2 Probit近似

尽管蒙特卡洛近似很简单，但它可能较慢，因为我们需要在测试时为每个输入 $\mathbf{x}$ 抽取 $S$ 个样本。幸运的是，如果 $p(\mathbf{w}|\mathcal{D})=\mathcal{N}(\mathbf{w}|\boldsymbol{\mu},\boldsymbol{\Sigma})$，存在一个简单而准确的

---

确定性近似最初由[SL90]提出。为了解释这一近似，我们遵循[Bis06, p219]的阐述。关键观察在于sigmoid函数 $\sigma(a)$ 与高斯累积分布函数（Gaussian cdf，见第2.6.1节）$\Phi(a)$ 形状相似。特别地，有 $\sigma(a) \approx \Phi(\lambda a)$，其中 $\lambda^2 = \pi/8$ 确保两个函数在原点处斜率相同。这一性质很有用，因为我们可以精确地将高斯cdf对高斯概率密度函数（Gaussian pdf）进行积分：

$$  \int\Phi(\lambda a)\mathcal{N}(a|m,v)d a=\Phi\left(\frac{m}{(\lambda^{-2}+v)^{\frac{1}{2}}}\right)=\Phi\left(\frac{\lambda m}{(1+\lambda^{2}v)^{\frac{1}{2}}}\right)\approx\sigma(\kappa(v)m)   \tag*{(10.111)}$$

其中我们定义

$$  \kappa(v)\triangleq(1+\pi v/8)^{-\frac{1}{2}}   \tag*{(10.112)}$$

因此，如果定义 $a = \boldsymbol{x}^\top \boldsymbol{w}$，则有

$$  p(y=1|\pmb{x},\mathcal{D})\approx\sigma(\kappa(v)m)   \tag*{(10.113)}$$

$$  m=\mathbb{E}\left[a\right]=x^{\top}\mu   \tag*{(10.114)}$$

$$  \boldsymbol{v}=\mathbb{V}\left[\boldsymbol{a}\right]=\mathbb{V}\left[\boldsymbol{x}^{\top}\boldsymbol{w}\right]=\boldsymbol{x}^{\top}\boldsymbol{\Sigma}\boldsymbol{x}   \tag*{(10.115)}$$

其中最后一行使用了式(2.165)。由于 $\Phi$ 是probit函数的逆，我们将此称为probit近似。

使用式(10.113)得到的预测（在置信度方面）不如插件估计极端。这是因为 $0 < \kappa(v) < 1$，从而 $\kappa(v)m < m$，所以 $\sigma(\kappa(v)m)$ 比 $\sigma(m)$ 更接近0.5。然而，决策边界本身不受影响。注意决策边界是使得 $p(y = 1|\boldsymbol{x}, \mathcal{D}) = 0.5$ 的点集 $\boldsymbol{x}$，由此可得 $\kappa(v)m = 0$，即 $m = \overline{\boldsymbol{w}}^{\top}\boldsymbol{x} = 0$，这与插件估计的决策边界相同。因此，“采用贝叶斯方法”不会改变（本例中的）误分类率，但会改变模型的置信度估计，正如我们在第10.5.1节所示，这有时非常重要。

在多分类情形下，我们可以使用广义probit近似[Gib97]：

$$  p(y=c|\boldsymbol{x},\mathcal{D})\approx\frac{\exp(\kappa(v_{c})m_{c})}{\sum_{c^{\prime}}\exp(\kappa(v_{c^{\prime}})m_{c^{\prime}})}   \tag*{(10.116)}$$

$$  m_{c}=\overline{m}_{c}^{\top}\boldsymbol{x}   \tag*{(10.117)}$$

$$  \boldsymbol{v}_{c}=\boldsymbol{x}^{\top}\mathbf{V}_{c,c}\boldsymbol{x}   \tag*{(10.118)}$$

其中 $\kappa$ 由式(10.112)定义。与二分类情形不同，考虑后验协方差会得出与插件方法不同的预测（参见[RW06]的习题3.10.3）。

关于sigmoid和softmax函数结合高斯积分的进一步近似，参见[Dau17]。

### 10.6 习题

**习题10.1** [多项逻辑回归对数似然的梯度与海森矩阵]

a. 设 $\mu_{ik} = \text{softmax}(\eta_i)_k$，其中 $\eta_i = \boldsymbol{w}^T \boldsymbol{x}_i$。证明softmax的雅可比矩阵为

$$  \frac{\partial\mu_{i k}}{\partial\eta_{i j}}=\mu_{i k}(\delta_{k j}-\mu_{i j})   \tag*{(10.119)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

其中 $ \delta_{kj}=I(k=j) $。

b. 因此证明负对数似然的梯度为

$$  \nabla_{w_{c}}\ell=\sum_{i}(y_{ic}-\mu_{ic})\boldsymbol{x}_{i}   \tag*{(10.120)}$$

提示：使用链式法则以及 $ \sum_{c} y_{ic} = 1 $ 的事实。

c. 证明类别 $c$ 和 $c'$ 对应的 Hessian 矩阵块子矩阵为

$$  \mathbf{H}_{c,c^{\prime}}=-\sum_{i}\mu_{ic}(\delta_{c,c^{\prime}}-\mu_{i,c^{\prime}})\mathbf{x}_{i}\mathbf{x}_{i}^{T}   \tag*{(10.121)}$$

因此证明负对数似然的 Hessian 矩阵是正定的。

**习题 10.2** [二维逻辑回归中单独项的正则化 $ \dagger $]

（来源：Jaakkola.）

a. 考虑图 10.15a 中的数据，拟合模型 $ p(y = 1|\boldsymbol{x}, \boldsymbol{w}) = \sigma(w_0 + w_1 x_1 + w_2 x_2) $。假设通过最大似然拟合模型，即最小化

$$  J(\boldsymbol{w})=-\ell(\boldsymbol{w},\mathcal{D}_{\mathrm{t r a i n}})   \tag*{(10.122)}$$

其中 $ \ell(\boldsymbol{w}, \mathcal{D}_{\text{train}}) $ 是训练集上的对数似然。草绘对应于 $ \hat{\boldsymbol{w}} $ 的可能的决策边界。（请先复制图形（大致草绘即可），然后将你的答案叠加在副本上，因为你将需要多个版本的该图形）。你的答案（决策边界）是唯一的吗？你的方法在训练集上造成了多少个分类错误？

b. 现在假设仅对 $ w_{0} $ 参数进行正则化，即最小化

$$  J_{0}(\boldsymbol{w})=-\ell(\boldsymbol{w},\mathcal{D}_{train})+\lambda w_{0}^{2}   \tag*{(10.123)}$$

假设 $ \lambda $ 非常大，因此将 $ w_0 $ 完全正则化到 0，但所有其他参数不进行正则化。草绘可能的决策边界。你的方法在训练集上造成了多少个分类错误？提示：考虑当 $ x_1 = x_2 = 0 $ 时简单线性回归 $ w_0 + w_1 x_1 + w_2 x_2 $ 的行为。

c. 现在假设仅对 $ w_{1} $ 参数进行强正则化，即最小化

$$  J_{1}(\boldsymbol{w})=-\ell(\boldsymbol{w},\mathcal{D}_{train})+\lambda w_{1}^{2}   \tag*{(10.124)}$$

草绘可能的决策边界。你的方法在训练集上造成了多少个分类错误？

d. 现在假设仅对 $ w_{2} $ 参数进行强正则化。草绘可能的决策边界。你的方法在训练集上造成了多少个分类错误？

##### **习题 10.3** [逻辑回归与 LDA/QDA 的比较 $ \dagger $]

（来源：Jaakkola.）假设我们通过最大似然训练以下二元分类器。

a. **GaussI**：生成式分类器，其中类条件密度为高斯分布，两个协方差矩阵均设为 $ \mathbf{I} $（单位矩阵），即 $ p(\boldsymbol{x}|y=c)=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{c},\mathbf{I}) $。假设 $ p(y) $ 是均匀分布。

b. **GaussX**：与 GaussI 相同，但协方差矩阵不受约束，即 $ p(\boldsymbol{x}|y=c)=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{c},\boldsymbol{\Sigma}_{c}) $。

c. **LinLog**：使用线性特征的逻辑回归模型。

《概率机器学习：导论》。在线版本。2024年11月23日。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_255_124_512_333.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_610_130_958_338.jpg" alt="图像" width="30%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 10.15: (a) 逻辑回归问题的数据。(b) 三种不同估计器的 $\hat{w}_k$ 随相关性 $c_k$ 变化的曲线图。</div>


d. QuadLog: 一种逻辑回归模型，使用线性和二次特征（即二次多项式基函数展开）。

训练完成后，我们按以下方式计算每个模型 $M$ 在训练集上的性能：

$$ L(M)=\frac{1}{n}\sum_{i=1}^{n}\log p(y_{i}|\boldsymbol{x}_{i},\hat{\boldsymbol{\theta}},M) \tag*{(10.125)}$$

(注意，这是条件对数似然 $p(y|\mathbf{x},\boldsymbol{\theta})$，而不是联合对数似然 $p(y,\mathbf{x}|\boldsymbol{\theta})$。) 现在，我们希望比较各个模型的性能。如果对于任意训练集，模型 $M$ 的对数似然（在训练集上）必然小于或等于模型 $M'$，则记 $L(M) \leq L(M')$（换句话说，至少就训练集对数概率而言，$M$ 比 $M'$ 差）。对于以下每一对模型，请说明 $L(M) \leq L(M')$、$L(M) \geq L(M')$，或者无法做出此类判断（即 $M$ 有时可能比 $M'$ 好，有时更差）；同时，针对每个问题，简要说明原因（1-2句话）。

a. GaussI（高斯独立模型），LinLog（线性逻辑回归模型）。

b. GaussX（高斯交叉模型），QuadLog（二次逻辑回归模型）。

c. LinLog（线性逻辑回归模型），QuadLog（二次逻辑回归模型）。

d. GaussI（高斯独立模型），QuadLog（二次逻辑回归模型）。

e. 现在假设我们以训练集上的平均误分类率来衡量性能：

$$ R(M)=\frac{1}{n}\sum_{i=1}^{n}I(y_{i}\neq\hat{y}(\boldsymbol{x}_{i})) \tag*{(10.126)}$$

一般而言，$L(M) > L(M')$ 是否意味着 $R(M) < R(M')$？请解释原因。

---

