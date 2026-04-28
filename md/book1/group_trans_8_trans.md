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

## 11 线性回归

### 11.1 引言

本章讨论线性回归，这是一种广泛用于预测实值输出（也称为因变量或目标）$ y \in \mathbb{R} $的方法，给定一个实值输入向量（也称为自变量、解释变量或协变量）$ \boldsymbol{x} \in \mathbb{R}^D $。该模型的关键性质是输出的期望值被假定为输入的线性函数，即 $ \mathbb{E}[y|\boldsymbol{x}] = \boldsymbol{w}^\top \boldsymbol{x} $，这使得模型易于解释且易于拟合数据。我们将在本书后续章节讨论非线性扩展。

### 11.2 最小二乘线性回归

本节讨论最常见形式的线性回归模型。

#### 11.2.1 术语

术语“线性回归”通常指具有以下形式的模型：

$$  p(y|\boldsymbol{x},\boldsymbol{\theta})=\mathcal{N}(y|w_{0}+\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x},\sigma^{2})   \tag*{(11.1)}$$

其中 $ \boldsymbol{\theta} = (w_0, \boldsymbol{w}, \sigma^2) $ 是模型的所有参数。（在统计学中，参数 $ w_0 $ 和 $ \boldsymbol{w} $ 通常记为 $ \beta_0 $ 和 $ \beta $。）

参数向量 $ w_{1:D} $ 被称为权重或回归系数。每个系数 $ w_d $ 指定了当我们改变相应的输入特征 $ x_d $ 一个单位时期望得到的输出变化。例如，假设 $ x_1 $ 是一个人的年龄，$ x_2 $ 是其教育水平（表示为连续数值），$ y $ 是其收入。那么 $ w_1 $ 对应于人增加一岁（从而获得更多经验）时期望的收入增长，$ w_2 $ 对应教育水平提高一个等级时期望的收入增长。项 $ w_0 $ 是截距或偏置项，指定所有输入为0时的输出值。它捕获了响应的无条件均值 $ w_0 = \mathbb{E}[y] $，并作为一个基线。我们通常假设 $ \boldsymbol{x} $ 写为 $ [1, x_1, \ldots, x_D] $，这样我们可以将截距项 $ w_0 $ 吸收到权重向量 $ \boldsymbol{w} $ 中。

如果输入是一维的（即 $D=1$），模型形式为 $f(\boldsymbol{x};\boldsymbol{w})=ax+b$，其中 $b=w_0$ 是截距，$a=w_1$ 是斜率。这称为简单线性回归。如果输入是多维的，即 $\boldsymbol{x}\in\mathbb{R}^D$ 且 $D>1$，则该方法称为多重线性回归。如果

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_209_133_552_377.jpg" alt="图像" width="29%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_609_118_970_400.jpg" alt="图像" width="31%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 11.1：对 21 个数据点拟合的一阶和二阶多项式。由 linreg_poly_vs_degree.ipynb 生成。</div>

输出也是多维的，$ y \in \mathbb{R}^J $，其中 $ J > 1 $，则称为多元线性回归。

$$  p(\boldsymbol{y}|\boldsymbol{x},\mathbf{W})=\prod_{j=1}^{J}\mathcal{N}(y_{j}|\boldsymbol{w}_{j}^{\mathsf{T}}\boldsymbol{x},\sigma_{j}^{2})   \tag*{(11.2)}$$

关于一个简单的数值例子，参见练习 11.1。

一般来说，直线无法很好地拟合大多数数据集。然而，我们可以通过对输入特征进行非线性变换，即用 $ \phi(\boldsymbol{x}) $ 替换 $ \boldsymbol{x} $，得到

$$  p(y|\boldsymbol{x},\boldsymbol{\theta})=\mathcal{N}(y|\boldsymbol{w}^{\top}\boldsymbol{\phi}(\boldsymbol{x}),\sigma^{2})   \tag*{(11.3)}$$

只要特征提取器 $ \phi $ 的参数是固定的，即使模型在输入上不是线性的，它在参数上仍然是线性的。（我们将在第三部分讨论学习特征提取器以及最终线性映射的方法。）

作为非线性变换的一个简单例子，考虑我们在 1.2.2.2 节中介绍的多项式回归。如果输入是一维的，并且我们使用 d 阶多项式展开，则得到 $ \phi(x) = [1, x, x^2, \ldots, x^d] $。参见图 11.1 中的示例。（另见 11.5 节，其中我们讨论了样条函数。）

#### 11.2.2 最小二乘估计

为了将线性回归模型拟合到数据，我们将最小化训练集上的负对数似然。目标函数由下式给出

$$  \begin{aligned}\mathrm{N L L}(\boldsymbol{w},\sigma^{2})&=-\sum_{n=1}^{N}\log\left[\left(\frac{1}{2\pi\sigma^{2}}\right)^{\frac{1}{2}}\exp\left(-\frac{1}{2\sigma^{2}}(y_{n}-\boldsymbol{w}^{\top}\boldsymbol{x}_{n})^{2}\right)\right]\\&=\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}(y_{n}-\hat{y}_{n})^{2}+\frac{N}{2}\log(2\pi\sigma^{2})\end{aligned}   \tag*{(11.4)}$$

---

我们已将预测响应定义为 $ \hat{y}_n \triangleq \boldsymbol{w}^\top \boldsymbol{x}_n $。最大似然估计对应 $ \nabla_{\boldsymbol{w}, \sigma} \mathrm{NLL}(\boldsymbol{w}, \sigma^2) = \mathbf{0} $ 的点。我们可以先对 $ \boldsymbol{w} $ 进行优化，再求解最优的 $ \sigma $。

在本节中，我们只关注权重 w 的估计。此时，负对数似然（忽略无关常数）等于残差平方和，其形式为

$$  \mathrm{R S S}(\boldsymbol{w})=\frac{1}{2}\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{w}^{\top}\boldsymbol{x}_{n})^{2}=\frac{1}{2}||\mathbf{X}\boldsymbol{w}-\boldsymbol{y}||_{2}^{2}=\frac{1}{2}(\mathbf{X}\boldsymbol{w}-\boldsymbol{y})^{\top}(\mathbf{X}\boldsymbol{w}-\boldsymbol{y})   \tag*{(11.6)}$$

下面我们将讨论如何对其进行优化。

##### 11.2.2.1 普通最小二乘法

由方程 (7.264) 可知，梯度为

$$  \nabla_{w}\mathrm{R S S}(w)=\mathbf{X}^{\top}\mathbf{X}w-\mathbf{X}^{\top}y   \tag*{(11.7)}$$

令梯度为零并求解可得

$$  \mathbf{X}^{\top}\mathbf{X}w=\mathbf{X}^{\top}y   \tag*{(11.8)}$$

这些方程被称为**正规方程**，因为在最优解处，$ \mathbf{y} - \mathbf{X}\mathbf{w} $ 与 $ \mathbf{X} $ 的值域正交（即法向），我们将在第 11.2.2.2 节中解释。相应的解 $ \hat{\mathbf{w}} $ 就是**普通最小二乘（OLS）解**，其形式为

$$  \hat{\boldsymbol{w}}=(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\boldsymbol{y}   \tag*{(11.9)}$$

其中 $ \mathbf{X}^\dagger = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top $ 是（非方）矩阵 $ \mathbf{X} $ 的（左）伪逆（详见第 7.5.3 节）。

我们可以通过证明 Hessian 矩阵是正定的来验证解的唯一性。此时，Hessian 矩阵为

$$  \mathbf{H}(\boldsymbol{w})=\frac{\partial^{2}}{\partial\boldsymbol{w}^{2}}\mathrm{RSS}(\boldsymbol{w})=\mathbf{X}^{\mathrm{T}}\mathbf{X}   \tag*{(11.10)}$$

如果 X 是满秩的（即 X 的列线性无关），那么 H 是正定的，因为对于任意 v > 0，有

$$  \boldsymbol{v}^{\mathrm{T}}(\mathbf{X}^{\mathrm{T}}\mathbf{X})\boldsymbol{v}=(\mathbf{X}\boldsymbol{v})^{\mathrm{T}}(\mathbf{X}\boldsymbol{v})=||\mathbf{X}\boldsymbol{v}||^{2}>0   \tag*{(11.11)}$$

因此，在满秩情况下，最小二乘目标函数存在唯一的全局最小值。如图 11.2 所示。

##### 11.2.2.2 最小二乘的几何解释

正规方程具有一个优雅的几何解释，它源自第 7.7 节，如下所述。我们将假设 N > D，即观测数多于未知数。（这被称为

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license.）

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_229_139_516_328.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_692_153_922_315.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图11.2：(a) 图11.1a示例的RSS误差曲面等高线。蓝色叉号表示MLE。(b) 对应的曲面图。由linreg_contours_sse_plot.ipynb生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_381_468_780_737.jpg" alt="Image" width="34%" /></div>


<div style="text-align: center;">图11.3：求解方程组 $\mathbf{A}\mathbf{x}=\mathbf{b}$ 时，$m=3$ 个方程和 $n=2$ 个未知数的最小二乘法的图形解释。$\mathbf{a}_{1}$ 和 $\mathbf{a}_{2}$ 是 $\mathbf{A}$ 的列，它们定义了一个嵌入 $\mathbb{R}^{3}$ 的二维线性子空间。目标向量 $\mathbf{b}$ 是 $\mathbb{R}^{3}$ 中的一个向量；其到该线性子空间的正交投影记为 $\hat{\mathbf{b}}$。从 $\mathbf{b}$ 到 $\hat{\mathbf{b}}$ 的线段是残差向量，我们想要最小化其范数。</div>


作为一个超定系统。）我们寻求一个向量 $\hat{\boldsymbol{y}} \in \mathbb{R}^N$，它位于 $\mathbf{X}$ 张成的线性子空间中，并且尽可能接近 $\boldsymbol{y}$，即我们要找到

$$  \begin{array}{c}\underset{\hat{\mathbf{y}}\in\operatorname{span}(\{\mathbf{x}_{:,1},\ldots,\mathbf{x}_{:,d}\})}{\operatorname{argmin}}\|\mathbf{y}-\hat{\mathbf{y}}\|_{2}.\end{array}   \tag*{(11.12)}$$

其中 $\boldsymbol{x}_{:,d}$ 是 $\mathbf{X}$ 的第 $d$ 列。由于 $\hat{\boldsymbol{y}} \in \text{span}(\mathbf{X})$，存在某个权重向量 $\boldsymbol{w}$ 使得

$$  \hat{\boldsymbol{y}}=w_{1}\boldsymbol{x}_{:,1}+\cdots+w_{D}\boldsymbol{x}_{:,D}=\boldsymbol{X}\boldsymbol{w}   \tag*{(11.13)}$$

为了最小化残差 $\boldsymbol{y} - \hat{\boldsymbol{y}}$ 的范数，我们希望残差向量与 $\mathbf{X}$ 的每一列正交。因此

$$  \boldsymbol{x}_{\cdot,d}^{\mathsf{T}}(\boldsymbol{y}-\hat{\boldsymbol{y}})=0\Rightarrow\mathbf{X}^{\mathsf{T}}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})=\mathbf{0}\Rightarrow\boldsymbol{w}=(\mathbf{X}^{\mathsf{T}}\mathbf{X})^{-1}\mathbf{X}^{\mathsf{T}}\boldsymbol{y}   \tag*{(11.14)}$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

因此，y 的投影值由下式给出

$$  \hat{\boldsymbol{y}}=\mathbf{X}\boldsymbol{w}=\mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\boldsymbol{y}   \tag*{(11.15)}$$

这对应于 y 到 X 列空间的正交投影。例如，考虑我们有 N=3 个训练样本的情况，每个样本的维度为 D=2。训练数据定义了一个二维线性子空间，该子空间由 X 的两个列向量定义，每个列向量是三维空间中的一个点。我们将同样是三维空间中的一个点的 y 投影到这个二维子空间上，如图 11.3 所示。

投影矩阵

$$  \mathrm{P r o j}(\mathbf{X})\triangleq\mathbf{X}(\mathbf{X}^{\mathsf{T}}\mathbf{X})^{-1}\mathbf{X}^{\mathsf{T}}   \tag*{(11.16)}$$

有时被称为帽子矩阵，因为 $\hat{\mathbf{y}} = \text{Proj}(\mathbf{X})\mathbf{y}$。在 $\mathbf{X} = \mathbf{x}$ 为列向量的特殊情况下，$\mathbf{y}$ 到直线 $\mathbf{x}$ 上的正交投影变为

$$  \mathrm{Proj}(\boldsymbol{x})\boldsymbol{y}=\boldsymbol{x}\frac{\boldsymbol{x}^{\top}\boldsymbol{y}}{\boldsymbol{x}^{\top}\boldsymbol{x}}   \tag*{(11.17)}$$

##### 11.2.2.3 算法问题

回顾一下，OLS（普通最小二乘）解为

$$  \hat{\boldsymbol{w}}=\mathbf{X}^{\dagger}\boldsymbol{y}=(\mathbf{X}^{\mathsf{T}}\mathbf{X})^{-1}\mathbf{X}^{\mathsf{T}}\boldsymbol{y}   \tag*{(11.18)}$$

然而，尽管理论上可以通过求逆 $\mathbf{X}^{\top}\mathbf{X}$ 来计算伪逆，但出于数值原因我们不应这样做，因为 $\mathbf{X}^{\top}\mathbf{X}$ 可能是病态的或奇异的。

一种更好（也更通用）的方法是使用 SVD（奇异值分解）计算伪逆。实际上，查看 `sklearn.linear_model.fit` 函数的源代码会发现，它使用了 `scipy.linalg.lstsq` 函数，而该函数又调用了 DGELSD，这是一个由 LAPACK 库实现的基于 SVD 的求解器，用 Fortran 语言编写。$^{1}$

然而，如果 $\mathbf{X}$ 是高窄矩阵（即 $N \gg D$），那么使用 QR 分解（第 7.6.2 节）会更快。为此，令 $\mathbf{X} = \mathbf{Q}\mathbf{R}$，其中 $\mathbf{Q}^\top \mathbf{Q} = \mathbf{I}$。在第 7.7 节中，我们证明了 OLS 等价于以最小化 $\|\mathbf{X} \mathbf{w} - \mathbf{y}\|^2$ 的方式求解线性方程组 $\mathbf{X} \mathbf{w} = \mathbf{y}$。（如果 $N = D$ 且 $\mathbf{X}$ 满秩，则方程组有唯一解，误差为 0。）利用 QR 分解，我们可以将这一方程组重写如下：

$$  \left(\mathbf{Q}\mathbf{R}\right)w=y   \tag*{(11.19)}$$

$$  \mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}w=\mathbf{Q}^{\top}y   \tag*{(11.20)}$$

$$  \boldsymbol{w}=\mathbf{R}^{-1}(\mathbf{Q}^{\top}\boldsymbol{y})   \tag*{(11.21)}$$

由于 $\mathbf{R}$ 是上三角矩阵，我们可以使用回代法求解最后这一组方程，从而避免矩阵求逆。演示请参见 $\text{linsys\_solve\_demo.ipynb}$。

另一种方法是使用基于矩阵分解（如 SVD 和 QR）的直接方法的替代方案，即使用迭代求解器，例如共轭梯度法（假设 X 对称）。

---

正定），以及适用于一般X的GMRES（广义最小残差法）。（在SciPy中，这由 `sparse.linalg.gmres` 实现。）这些方法仅需要执行矩阵-向量乘法（即线性算子的实现）的能力，因此非常适合X是稀疏或结构化的问题。详情参见例如 [TB97]。

最后一个重要问题是，在拟合模型之前，通常必须 $ \underline{\text{标准化}} $ 输入特征，以确保其零均值和单位方差。我们可以使用公式(10.51)实现这一点。

##### 11.2.2.4 加权最小二乘法

在某些情况下，我们希望为每个样本关联一个权重。例如，在异方差回归中，方差取决于输入，因此模型具有如下形式：

$$  p(y|\boldsymbol{x};\boldsymbol{\theta})=\mathcal{N}(y|\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x},\sigma^{2}(\boldsymbol{x}))=\frac{1}{\sqrt{2\pi\sigma^{2}(\boldsymbol{x})}}\exp\left(-\frac{1}{2\sigma^{2}(\boldsymbol{x})}(y-\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x})^{2}\right)   \tag*{(11.22)}$$

因此

$$  p(\boldsymbol{y}|\boldsymbol{x};\boldsymbol{\theta})=\mathcal{N}(\boldsymbol{y}|\mathbf{X}\boldsymbol{w},\boldsymbol{\Lambda}^{-1})   \tag*{(11.23)}$$

其中 $ \mathbf{\Lambda} = \mathrm{diag}(1/\sigma^2(\mathbf{x}_n)) $。这称为加权线性回归。可以证明，最大似然估计（MLE）由下式给出

$$  \hat{\boldsymbol{w}}=\left(\mathbf{X}^{\top}\boldsymbol{\Lambda}\mathbf{X}\right)^{-1}\mathbf{X}^{\top}\boldsymbol{\Lambda}\boldsymbol{y}   \tag*{(11.24)}$$

这称为加权最小二乘估计。

#### 11.2.3 计算MLE的其他方法

在本节中，我们讨论计算MLE的其他方法。

##### 11.2.3.1 分别求解偏移和斜率

通常我们使用形式为 $ p(y|\boldsymbol{x},\boldsymbol{\theta})=\mathcal{N}(y|w_0+\boldsymbol{w}^\top\boldsymbol{x},\sigma^2) $ 的模型，其中 $ w_0 $ 是偏移或“偏置”项。我们可以通过在 $ \mathbf{X} $ 中添加一列全1向量来同时计算 $ (w_0,\boldsymbol{w}) $，然后如上计算MLE。或者，我们可以分别求解 $ \boldsymbol{w} $ 和 $ w_0 $。（这在后续会很有用。）特别地，可以证明

$$  \hat{\boldsymbol{w}}=(\mathbf{X}_{c}^{\mathsf{T}}\mathbf{X}_{c})^{-1}\mathbf{X}_{c}^{\mathsf{T}}\boldsymbol{y}_{c}=\left[\sum_{i=1}^{N}(\boldsymbol{x}_{n}-\overline{\boldsymbol{x}})(\boldsymbol{x}_{n}-\overline{\boldsymbol{x}})^{\mathsf{T}}\right]^{-1}\left[\sum_{i=1}^{N}(y_{n}-\overline{y})(\boldsymbol{x}_{n}-\overline{\boldsymbol{x}})\right]   \tag*{(11.25)}$$

$$  \hat{w}_{0}=\frac{1}{N}\sum_{n}y_{n}-\frac{1}{N}\sum_{n}\boldsymbol{x}_{n}^{\mathsf{T}}\hat{\boldsymbol{w}}=\overline{y}-\overline{\boldsymbol{x}}^{\mathsf{T}}\hat{\boldsymbol{w}}   \tag*{(11.26)}$$

其中 $ \mathbf{X}_c $ 是中心化输入矩阵，其行包含 $ \mathbf{x}_n^c = \mathbf{x}_n - \overline{\mathbf{x}} $，而 $ \mathbf{y}_c = \mathbf{y} - \overline{\mathbf{y}} $ 是中心化输出向量。因此，我们可以先在中心化数据上计算 $ \hat{\mathbf{w}} $，然后使用 $ \overline{\mathbf{y}} - \overline{\mathbf{x}}^\top \hat{\mathbf{w}} $ 估计 $ w_0 $。

注意，如果我们将模型写成 $ \hat{y} = \beta_0 + \beta^\top(\boldsymbol{x} - \overline{\boldsymbol{x}}) $ 的形式，那么有 $ \hat{\beta} = \hat{\boldsymbol{w}} $ 和 $ \hat{w}_0 = \hat{\beta}_0 - \hat{\beta}^\top\overline{\boldsymbol{x}} $，因此 $ \hat{\beta}_0 = \overline{y} $。

---

##### 11.2.3.2 简单线性回归（一维输入）

在一维（标量）输入的情况下，第11.2.3.1节的结果简化为以下简单形式，这可能与基础统计学课程中的内容相似：

$$  \hat{w}_{1}=\frac{\sum_{n}(x_{n}-\overline{x})(y_{n}-\bar{y})}{\sum_{n}(x_{n}-\bar{x})^{2}}=\frac{C_{xy}}{C_{xx}}=\rho_{xy}\frac{\sigma_{y}}{\sigma_{x}}   \tag*{(11.27)}$$

$$  \hat{w}_{0}=\mathbb{E}\left[y\right]-w_{1}\mathbb{E}\left[x\right]\approx\bar{y}-\hat{w}_{1}\bar{x}   \tag*{(11.28)}$$

其中 $ C_{xx} = \text{Cov}[X, X] = \mathbb{V}[X] = \sigma_x^2 $，$ C_{yy} = \text{Cov}[Y, Y] = \mathbb{V}[Y] = \sigma_y^2 $，$ C_{xy} = \text{Cov}[X, Y] $，且 $ \rho_{xy} = \frac{C_{xy}}{\sigma_x \sigma_y} $。因此预测变为 $ \hat{y} = \bar{y} - \hat{w}_1 \bar{x} + \hat{w}_1 x = \bar{y} = \rho \sigma_y \frac{(x - \bar{x})}{\sigma_y} $。我们可以如下解释这个方程：我们估计 $ x $ 距离 $ X $ 的均值有多少个标准差，然后预测结果等于 $ Y $ 的均值加上 $ \rho $ 乘以该数量的标准差（高于或低于均值）。

##### 11.2.3.3 偏回归

根据方程(11.27)，我们可以计算 Y 对 X 的回归系数如下：

$$  R_{Y X}\triangleq\frac{\partial}{\partial x}\mathbb{E}\left[Y|X=x\right]=w_{1}=\frac{C_{x y}}{C_{x x}}   \tag*{(11.29)}$$

这是给定 X 时 Y 的线性预测的斜率。

现在考虑有两个输入的情况，即 $ Y = w_0 + w_1 X_1 + w_2 X_2 + \epsilon $，其中 $ \mathbb{E}[\epsilon] = 0 $。可以证明，$ w_1 $ 的最优回归系数由 $ R_{YX_1 \cdot X_2} $ 给出，即当 $ X_2 $ 保持不变时，$ Y $ 对 $ X_1 $ 的偏回归系数：

$$  w_{1}=R_{YX_{1}.X_{2}}=\frac{\partial}{\partial x}\mathbb{E}\left[Y|X_{1}=x,X_{2}\right]   \tag*{(11.30)}$$

注意，该量不受我们条件作用的 $ X_2 $ 的特定值影响。

我们可以类似地推导 $ w_2 $。实际上，我们可以将其推广到多个输入变量。在每种情况下，最优系数都等于偏回归系数。这意味着我们可以将第 $ j $ 个系数 $ \hat{w}_j $ 解释为：在其他所有输入保持不变的情况下，输入 $ x_j $ 每变化一个单位时，输出 $ y $ 的预期变化量。

##### 11.2.3.4 递归计算MLE

OLS 是一种用于计算 MLE 的批量方法。在某些应用中，数据以连续流的形式到达，因此我们希望像第4.4.2节中讨论的那样，在线（即**递归地**）计算估计值。在本节中，我们针对简单（一维）线性回归的情况展示如何做到这一点。

回顾第11.2.3.2节，简单线性回归的批量MLE由下式给出：

$$  \hat{w}_{1}=\frac{\sum_{n}(x_{n}-\overline{x})(y_{n}-\bar{y})}{\sum_{n}(x_{n}-\bar{x})^{2}}=\frac{C_{xy}}{C_{xx}}   \tag*{(11.31)}$$

$$  \hat{w}_{0}=\bar{y}-\hat{w}_{1}\bar{x}   \tag*{(11.32)}$$

其中 $ C_{xy} = \mathrm{Cov}[X, Y] $，$ C_{xx} = \mathrm{Cov}[X, X] = \mathbb{V}[X] $。

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可。

---

We now discuss how to compute these results in a recursive fashion. To do this, let us define the following sufficient statistics:

$$  \overline{x}^{(n)}=\frac{1}{n}\sum_{i=1}^{n}x_{i},\quad\overline{y}^{(n)}=\frac{1}{n}\sum_{i=1}^{n}y_{i}   \tag*{(11.33)}$$

$$  C_{x x}^{(n)}=\frac{1}{n}\sum_{i=1}^{n}(x_{i}-\overline{x})^{2},\ C_{x y}^{(n)}=\frac{1}{n}\sum_{i=1}^{n}(x_{i}-\overline{x})(y_{i}-\overline{y}),\ C_{y y}^{(n)}=\frac{1}{n}\sum_{i=1}^{n}(y_{i}-\overline{y})^{2}   \tag*{(11.34)}$$

We can update the means online using

$$  \overline{x}^{(n+1)}=\overline{x}^{(n)}+\frac{1}{n+1}(x_{n+1}-\overline{x}^{(n)}),\overline{y}^{(n+1)}=\overline{y}^{(n)}+\frac{1}{n+1}(y_{n+1}-\overline{y}^{(n)})   \tag*{(11.35)}$$

To update the covariance terms, let us first rewrite  $ C_{xy}^{(n)} $ as follows:

$$  C_{xy}^{(n)}=\frac{1}{n}\left[(\sum_{i=1}^{n}x_{i}y_{i})+(\sum_{i=1}^{n}\overline{x}^{(n)}\overline{y}^{(n)})-\overline{x}^{(n)}(\sum_{i=1}^{n}y_{i})-\overline{y}^{(n)}(\sum_{i=1}^{n}x_{i})\right]   \tag*{(11.36)}$$

$$  =\frac{1}{n}\left[\left(\sum_{i=1}^{n}x_{i}y_{i}\right)+n\overline{x}^{(n)}\overline{y}^{(n)}-\overline{x}^{(n)}n\overline{y}^{(n)}-\overline{y}^{(n)}n\overline{x}^{(n)}\right]   \tag*{(11.37)}$$

 $$ =\frac{1}{n}\left[\left(\sum_{i=1}^{n}x_{i}y_{i}\right)-n\overline{x}^{(n)}\overline{y}^{(n)}\right] $$ 

Hence

$$  \sum_{i=1}^{n}x_{i}y_{i}=nC_{xy}^{(n)}+n\overline{x}^{(n)}\overline{y}^{(n)}   \tag*{(11.39)}$$

and so

$$  C_{x y}^{(n+1)}=\frac{1}{n+1}\left[x_{n+1}y_{n+1}+n C_{x y}^{(n)}+n\overline{x}^{(n)}\overline{y}^{(n)}-(n+1)\overline{x}^{(n+1)}\overline{y}^{(n+1)}\right]   \tag*{(11.40)}$$

We can derive the update for  $ C_{xx}^{(n+1)} $ in a similar manner.

See Figure 11.4 for a simple illustration of these equations in action for a 1d regression model.

To extend the above analysis to D-dimensional inputs, the easiest approach is to use SGD. The resulting algorithm is called the least mean squares algorithm; see Section 8.4.2 for details.

##### 11.2.3.5 Deriving the MLE from a generative perspective

Linear regression is a discriminative model of the form  $ p(y|\boldsymbol{x}) $. However, we can also use generative models for regression, by analogy to how we use generative models for classification in Chapter 9. The goal is to compute the conditional expectation

$$  f(\boldsymbol{x})=\mathbb{E}\left[y|\boldsymbol{x}\right]=\int y p(y|\boldsymbol{x})d y=\frac{\int y p(\boldsymbol{x},y)d y}{\int p(\boldsymbol{x},y)d y}   \tag*{(11.41)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_443_136_718_326.jpg" alt="图" width="23%" /></div>

<div style="text-align: center;">图 11.4：图 1.7a(a) 中一维模型的回归系数随时间变化。由 linregOnlineDemo.ipynb 生成。</div>

假设我们使用 MVN 来拟合 $ p(\boldsymbol{x}, y) $。联合分布参数的最大似然估计就是经验均值和协方差（这一结果的证明见第 4.2.6 节）：

$$  \mu_{x}=\frac{1}{N}\sum_{n}x_{n}   \tag*{(11.42)}$$

$$  \mu_{y}=\frac{1}{N}\sum_{n}y_{n}   \tag*{(11.43)}$$

$$  \mathbf{\Sigma}_{x x}=\frac{1}{N}\sum_{n}(\mathbf{x}_{n}-\overline{\mathbf{x}})(\mathbf{x}_{n}-\overline{\mathbf{x}})^{\mathsf{T}}=\frac{1}{N}\mathbf{X}_{c}^{\mathsf{T}}\mathbf{X}_{c}   \tag*{(11.44)}$$

$$  \mathbf{\Sigma}_{xy}=\frac{1}{N}\sum_{n}(\mathbf{x}_{n}-\overline{\mathbf{x}})(y_{n}-\overline{y})=\frac{1}{N}\mathbf{X}_{c}^{\mathsf{T}}\mathbf{y}_{c}   \tag*{(11.45)}$$

因此，从公式 $ (3.28) $ 可得

$$  \mathbb{E}\left[y|\boldsymbol{x}\right]=\mu_{y}+\boldsymbol{\Sigma}_{x y}^{\mathsf{T}}\boldsymbol{\Sigma}_{x x}^{-1}(\boldsymbol{x}-\boldsymbol{\mu}_{x})   \tag*{(11.46)}$$

这可以改写为 $ \mathbb{E}[y|\boldsymbol{x}]=w_{0}+\boldsymbol{w}^{\mathrm{T}}\boldsymbol{x} $，其中定义

$$  w_{0}=\mu_{y}-w^{\top}\mu_{x}=\overline{y}-w^{\top}\overline{x}   \tag*{(11.47)}$$

$$  \boldsymbol{w}=\boldsymbol{\Sigma}_{x x}^{-1}\boldsymbol{\Sigma}_{x y}=\left(\mathbf{X}_{c}^{\top}\mathbf{X}_{c}\right)^{-1}\mathbf{X}_{c}^{\top}\boldsymbol{y}_{c}   \tag*{(11.48)}$$

这与我们在第 11.2.3.1 节中展示的判别模型的最大似然估计相匹配。因此，我们看到拟合联合模型然后对其进行条件化，与拟合条件模型得到相同的结果。然而，这只对高斯模型成立（关于这一点的进一步讨论见第 9.4 节）。

##### 11.2.3.6 推导 $\sigma^{2}$ 的最大似然估计

在采用上述方法之一估计出 $\hat{w}_{mle}$ 之后，我们可以估计噪声方差。可以很容易地证明最大似然估计为

$$  \hat{\sigma}_{mle}^{2}=\underset{\sigma^{2}}{\mathrm{argmin}}\mathrm{NLL}(\hat{\boldsymbol{w}},\sigma^{2})=\frac{1}{N}\sum_{n=1}^{N}(y_{n}-\boldsymbol{x}_{n}^{\mathsf{T}}\hat{\boldsymbol{w}})^{2}   \tag*{(11.49)}$$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可协议

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_227_129_516_337.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_633_130_924_338.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 11.5：对图 1.7a(a-b) 中函数进行 1 次和 2 次多项式回归的残差图。由 linreg_poly_vs_degree.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_233_451_530_678.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_641_451_937_679.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 11.6：对图 1.7a(a-b) 中函数进行 1 次和 2 次多项式回归的拟合值 vs 实际值图。由 linreg_poly_vs_degree.ipynb 生成。</div>


这仅仅是残差的均方误差（MSE），是一个直观的结果。

#### 11.2.4 测量拟合优度

本节我们讨论一些简单的方法来评估回归模型对数据的拟合程度（即拟合优度）。

##### 11.2.4.1 残差图

对于一维输入，我们可以通过绘制残差 $ r_n = y_n - \hat{y}_n $ 相对于输入 $ x_n $ 的图形来检查模型的合理性，这称为**残差图**。模型假设残差服从 $ \mathcal{N}(0, \sigma^2) $ 分布，因此残差图应该是在水平线 0 上下大致均匀分布的点云，没有任何明显的趋势。

例如，在图 11.5(a) 中，我们绘制了图 1.7a(a) 中线性模型的残差。可以看到残差存在一定的曲线结构，表明拟合不佳。在图 11.5(b) 中，我们绘制了图 1.7a(b) 中二次模型的残差，可以看出拟合效果好得多。

---

为了将此方法扩展到多维输入，我们可以绘制预测值 $\hat{y}_n$ 与真实输出 $y_n$ 的关系图，而不是与 $x_n$ 的关系图。一个良好的模型会使得数据点落在对角线上。参见图11.6中的示例。

##### 11.2.4.2 预测精度与 $R^2$

我们可以通过在数据集上计算RSS（残差平方和）来定量评估拟合效果：$ \mathrm{RSS}(\boldsymbol{w}) = \sum_{n=1}^{N} (y_n - \boldsymbol{w}^\top \boldsymbol{x}_n)^2 $。RSS越小的模型拟合数据越好。另一个常用的度量是均方根误差（RMSE）：

$$  \mathrm{RMSE}(\boldsymbol{w})\triangleq\sqrt{\frac{1}{N}\mathrm{RSS}(\boldsymbol{w})}   \tag*{(11.50)}$$

一个更具可解释性的度量是决定系数，记为 $R^2$：

$$  R^{2}\triangleq1-\frac{\sum_{n=1}^{N}(\hat{y}_{n}-y_{n})^{2}}{\sum_{n=1}^{N}(\overline{y}-y_{n})^{2}}=1-\frac{RSS}{TSS}   \tag*{(11.51)}$$

其中 $\overline{y} = \frac{1}{N} \sum_{n=1}^{N} y_n$ 是响应的经验均值，$RSS = \sum_{n=1}^{N} (y_n - \hat{y}_n)^2$ 是残差平方和，$TSS = \sum_{n=1}^{N} (y_n - \overline{y})^2$ 是总平方和。因此我们看到 $R^2$ 衡量了相对于简单常数预测 $\hat{y}_n = \overline{y}$ 的预测方差。如果一个模型的预测效果并不比使用输出均值更好，那么 $R^2 = 0$。如果模型完美拟合数据，则RSS为0，因此 $R^2 = 1$。通常，较大的值意味着方差减少得更多（拟合更好）。图11.6对此进行了说明。

### 11.3 岭回归

正如我们在1.2.2.2节中讨论的，最大似然估计可能导致过拟合。一个简单的解决方案是使用MAP估计，在权重上施加一个零均值高斯先验 $p(\boldsymbol{w}) = \mathcal{N}(\boldsymbol{w}|\mathbf{0}, \lambda^{-1}\mathbf{I})$，正如我们在4.5.3节中讨论的。这被称为岭回归。

具体来说，我们按如下方式计算MAP估计：

$$  \hat{\boldsymbol{w}}_{\mathrm{map}}=\operatorname{argmin}\frac{1}{2\sigma^{2}}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})^{\mathrm{T}}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})+\frac{1}{2\tau^{2}}\boldsymbol{w}^{\mathrm{T}}\boldsymbol{w}   \tag*{(11.52)}$$

$$  =\arg\min\mathrm{RSS}(\boldsymbol{w})+\lambda||\boldsymbol{w}||_{2}^{2}   \tag*{(11.53)}$$

其中 $\lambda \triangleq \frac{\sigma^2}{\tau^2}$ 与先验强度成正比，且

$$  ||\boldsymbol{w}||_{2}\triangleq\sqrt{\sum_{d=1}^{D}|\boldsymbol{w}_{d}|^{2}}=\sqrt{\boldsymbol{w}^{\mathsf{T}}\boldsymbol{w}}   \tag*{(11.54)}$$

是向量 $\boldsymbol{w}$ 的 $\ell_2$ 范数。因此我们惩罚那些幅度过大的权重。通常，这种技术被称为 $\ell_2$ 正则化或权重衰减，并被广泛使用。参见图4.5中的示例。注意，我们不对偏置项 $w_0$ 进行惩罚，因为它只影响输出的全局均值，不会导致过拟合。参见习题11.2。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 11.3.1 计算 MAP 估计

本节讨论计算 MAP 估计算法。

MAP 估计对应于最小化以下带惩罚的目标函数：

$$  J(\boldsymbol{w})=(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})^{\top}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})+\lambda||\boldsymbol{w}||_{2}^{2}   \tag*{(11.55)}$$

其中 $ \lambda = \sigma^{2}/\tau^{2} $ 是正则化强度。其梯度为

$$  \nabla_{w}J(w)=2\left(\mathbf{X}^{\mathsf{T}}\mathbf{X}w-\mathbf{X}^{\mathsf{T}}y+\lambda w\right)   \tag*{(11.56)}$$

因此

$$  \hat{\boldsymbol{w}}_{\mathrm{map}}=(\mathbf{X}^{\mathrm{T}}\mathbf{X}+\lambda\mathbf{I}_{D})^{-1}\mathbf{X}^{\mathrm{T}}\boldsymbol{y}=(\sum_{n}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\mathrm{T}}+\lambda\mathbf{I}_{D})^{-1}(\sum_{n}y_{n}\boldsymbol{x}_{n})   \tag*{(11.57)}$$

##### 11.3.1.1 使用 QR 分解求解

直接使用矩阵求逆来计算原始估计 $ \boldsymbol{w} = (\boldsymbol{X}^{\top} \boldsymbol{X} + \lambda \boldsymbol{I})^{-1} \boldsymbol{X}^{\top} \boldsymbol{y} $ 是一个糟糕的做法，因为它既缓慢又数值不稳定。在本节中，我们描述一种将问题转化为标准最小二乘问题的方法，从而可以应用第 11.2.2.3 节讨论的 QR 分解。

假设先验形式为 $ p(\boldsymbol{w}) = \mathcal{N}(\mathbf{0}, \boldsymbol{\Lambda}^{-1}) $，其中 $ \boldsymbol{\Lambda} $ 是精度矩阵。在岭回归情况下，$ \boldsymbol{\Lambda} = (1/\tau^2)\mathbf{I} $。我们可以通过在训练集中添加“虚拟数据”来模拟这一先验，得到

$$  \tilde{\mathbf{X}}=\begin{pmatrix}\mathbf{X}/\sigma\\ \sqrt{\boldsymbol{\Lambda}}\end{pmatrix},\quad\tilde{\mathbf{y}}=\begin{pmatrix}\mathbf{y}/\sigma\\ \mathbf{0}_{D\times1}\end{pmatrix}   \tag*{(11.58)}$$

其中 $ \mathbf{\Lambda} = \sqrt{\mathbf{\Lambda}} \sqrt{\mathbf{\Lambda}}^{-1} $ 是 $ \mathbf{\Lambda} $ 的 Cholesky 分解。我们看到 $ \tilde{\mathbf{X}} $ 是 $ (N + D) \times D $ 的，其中额外的行表示来自先验的伪数据。

现在我们证明，在这个扩展数据上的 RSS 等价于原始数据上的带惩罚 RSS：

$$  f(\boldsymbol{w})=(\tilde{\boldsymbol{y}}-\tilde{\mathbf{X}}\boldsymbol{w})^{\top}(\tilde{\boldsymbol{y}}-\tilde{\mathbf{X}}\boldsymbol{w})   \tag*{(11.59)}$$

$$  =\left(\begin{pmatrix}\boldsymbol{y}/\sigma\\ \mathbf{0}\end{pmatrix}-\begin{pmatrix}\mathbf{X}/\sigma\\ \sqrt{\boldsymbol{\Lambda}}\end{pmatrix}\boldsymbol{w}\right)^{\top}\left(\begin{pmatrix}\boldsymbol{y}/\sigma\\ \mathbf{0}\end{pmatrix}-\begin{pmatrix}\mathbf{X}/\sigma\\ \sqrt{\boldsymbol{\Lambda}}\end{pmatrix}\boldsymbol{w}\right)   \tag*{(11.60)}$$

$$  =\begin{pmatrix}\frac{1}{\sigma}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})\\ -\sqrt{\Lambda}\boldsymbol{w}\end{pmatrix}^{\top}\begin{pmatrix}\frac{1}{\sigma}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})\\ -\sqrt{\Lambda}\boldsymbol{w}\end{pmatrix}   \tag*{(11.61)}$$

$$  =\frac{1}{\sigma^{2}}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})^{\mathsf{T}}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})+(\sqrt{\boldsymbol{\Lambda}}\boldsymbol{w})^{\mathsf{T}}(\sqrt{\boldsymbol{\Lambda}}\boldsymbol{w})   \tag*{(11.62)}$$

$$  =\frac{1}{\sigma^{2}}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})^{\top}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w})+\boldsymbol{w}^{\top}\boldsymbol{\Lambda}\boldsymbol{w}   \tag*{(11.63)}$$

因此，MAP 估计由下式给出

$$  \hat{w}_{\mathrm{m a p}}=(\tilde{\mathbf{X}}^{\mathsf{T}}\tilde{\mathbf{X}})^{-1}\tilde{\mathbf{X}}^{\mathsf{T}}\tilde{\mathbf{y}}   \tag*{(11.64)}$$

这可以使用标准 OLS 方法求解。特别地，我们可以计算 $ \tilde{X} $ 的 QR 分解，然后按照第 11.2.2.3 节的方法进行。这需要 $ O((N + D)D^2) $ 的时间。

---

##### 11.3.1.2 使用SVD求解

本节中，我们假设 $D > N$，这是岭回归中的常见情形。此时，使用SVD比QR更快。具体而言，令 $\mathbf{X} = \mathbf{USV}^\top$ 为 $\mathbf{X}$ 的SVD，其中 $\mathbf{V}^\top \mathbf{V} = \mathbf{I}_N$，$\mathbf{U} \mathbf{U}^\top = \mathbf{U}^\top \mathbf{U} = \mathbf{I}_N$，而 $\mathbf{S}$ 是一个 $N \times N$ 的对角矩阵。再令 $\mathbf{R} = \mathbf{US}$ 为一个 $N \times N$ 矩阵。可以证明（参见 [HTF09] 的练习18.4）：

$$  \hat{\boldsymbol{w}}_{\mathrm{m a p}}=\mathbf{V}(\mathbf{R}^{\mathsf{T}}\mathbf{R}+\lambda\mathbf{I}_{N})^{-1}\mathbf{R}^{\mathsf{T}}\boldsymbol{y}   \tag*{(11.65)}$$

换言之，我们可以将 $D$ 维向量 $\mathbf{x}_i$ 替换为 $N$ 维向量 $\mathbf{r}_i$，然后像之前一样进行惩罚拟合。总运算量现在为 $O(DN^2)$，当 $D > N$ 时，这比 $O(D^3)$ 更小。

#### 11.3.2 岭回归与PCA的联系

本节中，我们将讨论岭回归与PCA（在第20.1节描述）之间一个有趣的关联，以进一步理解岭回归为何表现良好。本节的讨论基于 [HTF09, p66]。

令 $\mathbf{X} = \mathbf{USV}^\top$ 为 $\mathbf{X}$ 的SVD，其中 $\mathbf{V}^\top \mathbf{V} = \mathbf{I}_N$，$\mathbf{U}\mathbf{U}^\top = \mathbf{U}^\top \mathbf{U} = \mathbf{I}_N$，而 $\mathbf{S}$ 是一个 $N \times N$ 的对角矩阵。利用公式(11.65)可以看出，训练集上的岭回归预测值为：

$$  \hat{\mathbf{y}}=\mathbf{X}\hat{\mathbf{w}}_{\mathrm{m a p}}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}}\mathbf{V}(\mathbf{S}^{2}+\lambda\mathbf{I})^{-1}\mathbf{S}\mathbf{U}^{\mathsf{T}}\mathbf{y}   \tag*{(11.66)}$$

$$  =\mathbf{U}\tilde{\mathbf{S}}\mathbf{U}^{\mathsf{T}}\mathbf{y}=\sum_{j=1}^{D}\mathbf{u}_{j}\tilde{S}_{j j}\mathbf{u}_{j}^{\mathsf{T}}\mathbf{y}   \tag*{(11.67)}$$

其中

$$  \tilde{S}_{j j}\triangleq[\mathbf{S}(\mathbf{S}^{2}+\lambda I)^{-1}\mathbf{S}]_{j j}=\frac{\sigma_{j}^{2}}{\sigma_{j}^{2}+\lambda}   \tag*{(11.68)}$$

而 $\sigma_{j}$ 是 $\mathbf{X}$ 的奇异值。因此

$$  \hat{\boldsymbol{y}}=\mathbf{X}\hat{\boldsymbol{w}}_{\mathrm{map}}=\sum_{j=1}^{D}\boldsymbol{u}_{j}\frac{\sigma_{j}^{2}}{\sigma_{j}^{2}+\lambda}\boldsymbol{u}_{j}^{\mathsf{T}}\boldsymbol{y}   \tag*{(11.69)}$$

与之对比，最小二乘预测值为：

$$  \hat{\boldsymbol{y}}=\mathbf{X}\hat{\boldsymbol{w}}_{\mathrm{m l e}}=(\mathbf{U}\mathbf{S}\mathbf{V}^{\mathrm{T}})(\mathbf{V}\mathbf{S}^{-1}\mathbf{U}^{\mathrm{T}}\boldsymbol{y})=\mathbf{U}\mathbf{U}^{\mathrm{T}}\boldsymbol{y}=\sum_{j=1}^{D}\boldsymbol{u}_{j}\boldsymbol{u}_{j}^{\mathrm{T}}\boldsymbol{y}   \tag*{(11.70)}$$

如果 $\sigma_j^2$ 相对于 $\lambda$ 较大，则 $\sigma_j^2/(\sigma_j^2 + \lambda) \approx \sigma_j^2/\sigma_j^2 = 1$，因此方向 $\boldsymbol{u}_j$ 不受影响；但如果 $\sigma_j^2$ 相对于 $\lambda$ 较小，且 $\lambda$ 较大，则 $\sigma_j^2/(\sigma_j^2 + \lambda) \approx 1/\lambda \approx 0$，因此方向 $\boldsymbol{u}_j$ 会被降权。据此，我们定义模型的有效自由度如下：

$$  \mathrm{d o f}(\lambda)=\sum_{j=1}^{D}\frac{\sigma_{j}^{2}}{\sigma_{j}^{2}+\lambda}   \tag*{(11.71)}$$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_465_122_706_336.jpg" alt="图像" width="20%" /></div>


<div style="text-align: center;">图 11.7：岭回归的几何解释。似然函数以椭圆表示，先验以原点为中心的圆表示。改编自 [Bis06] 的图 3.15。由 geom_ridge.ipynb 生成。</div>


当 $ \lambda = 0 $ 时，$ \mathrm{dof}(\lambda) = D $，而当 $ \lambda \to \infty $ 时，$ \mathrm{dof}(\lambda) \to 0 $。

让我们尝试理解为何这种行为是理想的。在第 11.7 节中，我们展示了若对 $ \boldsymbol{w} $ 采用均匀先验，则 $ \text{Cov}[\boldsymbol{w}|\mathcal{D}] \propto (\boldsymbol{X}^{\mathrm{T}}\boldsymbol{X})^{-1} $。因此，如图 7.6 所示，我们对 $ \boldsymbol{w} $ 最不确定的方向由 $ (\boldsymbol{X}^{\mathrm{T}}\boldsymbol{X})^{-1} $ 的最大特征值所对应的特征向量决定。这些方向对应于 $ \boldsymbol{X}^{\mathrm{T}}\boldsymbol{X} $ 的最小特征值（进而由第 7.5.2 节可知，即最小奇异值）所对应的特征向量。因此，若 $ \sigma_j^2 $ 相对于 $ \lambda $ 较小，岭回归会降低方向 $ \boldsymbol{u}_j $ 的权重。

该过程如图 11.7 所示。水平方向参数 $ w_1 $ 由数据确定的不充分（具有较高的后验方差），而垂直方向参数 $ w_2 $ 则确定得较好。因此，$ w_{\text{map}}(2) $ 接近 $ w_{\text{mle}}(2) $，但 $ w_{\text{map}}(1) $ 则显著地向先验均值（即 0）偏移。通过这种方式，确定得不充分的参数的大小会向 0 收缩。这被称为 **收缩**。

还有一种相关但不同的技术称为 **主成分回归**，它是 PCA 的有监督版本，我们将在第 20.1 节中解释。其思想是：首先使用 PCA 将维度降至 K 维，然后将这些低维特征作为回归的输入。然而，在预测精度方面，该技术不如岭回归 [HTF01, p70]。原因在于，在主成分回归中，仅保留前 K 个（派生）维度，而其余 D-K 个维度完全被忽略。相比之下，岭回归对所有维度采用“软”加权。

#### 11.3.3 选择正则化强度

为找到 $ \lambda $ 的最优值，我们可以尝试有限个不同的值，并使用交叉验证来估计其期望损失，如第 4.5.5.2 节所述。图 4.5d 给出了一个示例。

如果有很多值需要选择，这种方法可能相当昂贵。幸运的是，我们通常可以热启动优化过程，即将 $ \hat{w}(\lambda_k) $ 的值作为 $ \hat{w}(\lambda_{k+1}) $ 的初始值，其中 $ \lambda_{k+1} < \lambda_k $；换句话说，我们从高度约束的模型（强正则化）开始，然后逐渐放松约束（减少正则化量）。以这种方式扫描得到的参数集 $ \hat{w}_k $ 称为 **正则化路径**。图 11.10(a) 给出了一个示例。

我们还可以使用经验贝叶斯方法来选择 $ \lambda $。具体来说，通过计算 $ \hat{\lambda} = \arg\max_{\lambda} \log p(\mathcal{D}|\lambda) $ 来选择超参数，其中 $ p(\mathcal{D}|\lambda) $ 是边际似然或证据。

---

图4.7b表明，这一结果与交叉验证估计基本一致。然而，贝叶斯方法具有若干优势：计算 $ p(\mathcal{D}|\lambda) $ 只需拟合单个模型，而交叉验证需将同一模型拟合K次；此外，$ p(\mathcal{D}|\lambda) $ 是 $ \lambda $ 的光滑函数，因此我们可以使用基于梯度的优化代替离散搜索。

### 11.4 Lasso回归

在第11.3节中，我们在拟合线性回归模型时假设回归系数服从高斯先验。这通常是一个不错的选择，因为它鼓励参数取值较小，从而防止过拟合。然而，有时我们希望参数不仅小，而且要恰好为零，即希望 $ \hat{w} $ 是稀疏的，从而最小化L0范数：

$$  ||\boldsymbol{w}||_{0}=\sum_{d=1}^{D}\mathbb{I}\left(|w_{d}|>0\right)   \tag*{(11.72)}$$

这一性质很有用，因为它可用于执行特征选择。具体而言，注意到预测形式为 $ f(\boldsymbol{x};\boldsymbol{w})=\sum_{d=1}^{D}w_{d}x_{d} $，因此若任一 $ w_{d}=0 $，我们便忽略对应的特征 $ x_{d} $。（同样的思想可通过鼓励第一层权重稀疏而应用于非线性模型，例如深度神经网络。）

#### 11.4.1 基于拉普拉斯先验的MAP估计（ $ \ell_{1} $ 正则化）

有多种方法可以计算此类稀疏估计（例如，参见 [Bha+19]）。本节我们聚焦于使用拉普拉斯分布（已在第11.6.1节讨论）作为先验的MAP估计：

$$  p(\boldsymbol{w}|\lambda)=\prod_{d=1}^{D}Laplace(w_{d}|0,1/\lambda)\propto\prod_{d=1}^{D}e^{-\lambda|w_{d}|}   \tag*{(11.73)}$$

其中 $ \lambda $ 是稀疏性参数，而

$$  \mathrm{Laplace}(w|\mu,b)\triangleq\frac{1}{2b}\exp\left(-\frac{|w-\mu|}{b}\right)   \tag*{(11.74)}$$

这里 $ \mu $ 是位置参数，$ b > 0 $ 是尺度参数。图2.15表明，即使固定方差相同，Laplace( $ w|0,b $) 也比 $ \mathcal{N}(w|0,\sigma^2) $ 在0处赋予更大密度。

为了对该先验下的线性回归模型进行MAP估计，我们只需最小化以下目标：

$$  \mathrm{PNLL}(\boldsymbol{w})=-\log p(\mathcal{D}|\boldsymbol{w})-\log p(\boldsymbol{w}|\boldsymbol{\lambda})=||\mathbf{X}\boldsymbol{w}-\boldsymbol{y}||_{2}^{2}+\lambda||\boldsymbol{w}||_{1}   \tag*{(11.75)}$$

其中 $ \|\boldsymbol{w}\|_{1} \triangleq \sum_{d=1}^{D} |w_d| $ 是 $ \boldsymbol{w} $ 的 $ \ell_1 $ 范数。此方法称为lasso，即“最小绝对收缩与选择算子”（least absolute shrinkage and selection operator）[Tib96]。（我们将在下文解释此名称的由来。）更一般地，基于拉普拉斯先验的MAP估计称为 $ \ell_1 $ 正则化。

作者：Kevin P. Murphy。 (C) MIT Press。采用CC-BY-NC-ND许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_375_129_794_310.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图11.8：最小二乘问题的 $ \ell_{1} $（左）与 $ \ell_{2} $（右）正则化示意图。改编自 [HTF01] 的图3.12。</div>


注意，我们也可以对权重向量使用其他范数。通常，q-范数定义如下：

$$  \|\boldsymbol{w}\|_{q}=\left(\sum_{d=1}^{D}\left|w_{d}\right|^{q}\right)^{1/q}   \tag*{(11.76)}$$

当 q < 1 时，我们可以得到更稀疏的解。在极限情况 q = 0 时，我们得到 $ \ell_{0} $-范数：

$$  \|\boldsymbol{w}\|_{0}=\sum_{d=1}^{D}\mathbb{I}\left(\left|w_{d}\right|>0\right)   \tag*{(11.77)}$$

然而，可以证明对于任意 $q < 1$，问题变为非凸的（例如参见 [HTW15]）。因此，$\ell_{1}$-范数是 $\ell_{0}$-范数最紧的凸松弛。

#### 11.4.2 为什么 $ \ell_{1} $ 正则化会产生稀疏解？

我们现在解释为什么 $ \ell_{1} $ 正则化会产生稀疏解，而 $ \ell_{2} $ 正则化则不会。我们以线性回归为例，尽管类似的论证也适用于其他模型。

Lasso 的目标函数是如下的非光滑目标函数（关于光滑性的讨论请参见第8.1.4节）：

$$  \min_{w}NLL(w)+\lambda||w||_{1}   \tag*{(11.78)}$$

这是如下二次规划问题的拉格朗日函数（参见第8.5.4节）：

$$  \min_{w}NLL(w)\quad s.t.\quad||w||_{1}\leq B   \tag*{(11.79)}$$

其中 B 是权重 $ \ell_{1} $-范数的一个上界：较小的（紧）界 B 对应于较大的惩罚 $ \lambda $，反之亦然。

类似地，我们可以将岭回归的目标函数 $ \min_w \mathrm{NLL}(\boldsymbol{w}) + \lambda||\boldsymbol{w}||_2^2 $ 写成带界约束的形式：

$$  \min_{w}\mathrm{N L L}(w)\quad s.t.\quad||w||_{2}^{2}\leq B   \tag*{(11.80)}$$

---

在 Figure 11.8 中，我们绘制了 NLL 目标函数的等高线，以及 $ \ell_2 $ 和 $ \ell_1 $ 约束面的等高线。根据约束优化理论（第 8.5 节），最优解出现在目标函数的最低水平集与约束面相交的点（假设约束是活跃的）。从几何上显而易见，当我们放松约束 $ B $ 时，$ \ell_1 $“球”会逐渐“膨胀”直到与目标函数相遇；球的角点比边更有可能与椭圆相交，尤其是在高维空间中，因为角点“突出”更多。这些角点对应于位于坐标轴上的稀疏解。相比之下，当我们膨胀 $ \ell_2 $ 球时，它可以在任意点与目标函数相交；不存在“角点”，因此没有对稀疏性的偏好。

#### 11.4.3 硬阈值与软阈值

Lasso 目标函数的形式为 $ \mathcal{L}(\boldsymbol{w}) = \mathrm{NLL}(\boldsymbol{w}) + \lambda||\boldsymbol{w}||_1 $。可以证明（练习 11.3），光滑 NLL 部分的梯度由下式给出：

$$  \frac{\partial}{\partial w_{d}}NLL(\boldsymbol{w})=a_{d}w_{d}-c_{d}   \tag*{(11.81)}$$

$$  a_{d}=\sum_{n=1}^{N}x_{nd}^{2}   \tag*{(11.82)}$$

$$  c_{d}=\sum_{n=1}^{N}x_{n d}(y_{n}-\boldsymbol{w}_{-d}^{\mathsf{T}}\boldsymbol{x}_{n,-d})   \tag*{(11.83)}$$

其中 $ \boldsymbol{w}_{-d} $ 是去掉分量 $ d $ 后的 $ \boldsymbol{w} $，类似地，$ \boldsymbol{x}_{n,-d} $ 是去掉分量 $ d $ 后的特征向量 $ \boldsymbol{x}_{n} $。我们看到，$ c_{d} $ 与第 $ d $ 列特征 $ \boldsymbol{x}_{:,d} $ 和使用所有其他特征进行预测得到的残差 $ \boldsymbol{r}_{-d} = \boldsymbol{y} - \boldsymbol{X}_{:,d} \boldsymbol{w}_{-d} $ 之间的相关性成正比。因此，$ c_{d} $ 的大小指示了相对于其他特征和当前参数，特征 $ d $ 对预测 $ \boldsymbol{y} $ 的相关程度。将梯度设为 0，可得到固定其他权重时 $ w_{d} $ 的最优更新：

$$  w_{d}=c_{d}/a_{d}=\frac{\boldsymbol{x}_{\cdot,d}^{\top}\boldsymbol{r}_{-d}}{\left|\left|\boldsymbol{x}_{\cdot,d}\right|\right|_{2}^{2}}   \tag*{(11.84)}$$

相应的对 $ \pmb{r}_{-d} $ 的新预测变为 $ \hat{\pmb{r}}_{-d}=w_{d}\pmb{x}_{:,d} $，即残差到列向量 $ \pmb{x}_{:,d} $ 上的正交投影，与式 (11.15) 一致。

现在加入 $ \ell_1 $ 项。不幸的是，当 $ w_d = 0 $ 时，$ \|w\|_1 $ 项不可微。幸运的是，我们仍可以在该点处计算次梯度。利用式 (8.14) 可得：

$$  \begin{aligned}\partial_{w_{d}}\mathcal{L}(\boldsymbol{w})&=(a_{d}w_{d}-c_{d})+\lambda\partial_{w_{d}}||\boldsymbol{w}||_{1}\\&=\left\{\begin{array}{ll}\left\{a_{d}w_{d}-c_{d}-\lambda\right\}&\text{if}w_{d}<0\\ \left[-c_{d}-\lambda,-c_{d}+\lambda\right]&\text{if}w_{d}=0\\ \left\{a_{d}w_{d}-c_{d}+\lambda\right\}&\text{if}w_{d}>0\end{array}\right.\end{aligned}   \tag*{(11.86)}$$

根据 $c_d$ 的值，$\partial_{w_d}\mathcal{L}(\boldsymbol{w})=0$ 的解可能出现在 $w_d$ 的三个不同取值处，如下所示：

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_266_134_500_322.jpg" alt="图像" width="20%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_658_118_927_331.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 11.9：左图：软阈值化。右图：硬阈值化。在这两种情况下，横轴是使用除 $ w_k $ 以外的所有系数进行预测时产生的残差误差，纵轴是使该惩罚残差最小化的估计系数 $ \hat{w}_k $。中间平坦区域是区间 $ [-\lambda, +\lambda] $。</div>


1. 如果 $ c_d < -\lambda $，即该特征与残差呈强负相关，那么次梯度在 $ \hat{w}_d = \frac{c_d + \lambda}{a_d} < 0 $ 处为零。

2. 如果 $ c_d \in [-\lambda, \lambda] $，即该特征与残差仅弱相关，那么次梯度在 $ \hat{w}_d = 0 $ 处为零。

3. 如果 $ c_d > \lambda $，即该特征与残差呈强正相关，那么次梯度在 $ \hat{w}_d = \frac{c_d - \lambda}{a_d} > 0 $ 处为零。

综上，我们有

$$  \hat{w}_{d}(c_{d})=\left\{\begin{array}{cc}(c_{d}+\lambda)/a_{d}&如果 c_{d}<-\lambda\\0&如果 c_{d}\in[-\lambda,\lambda]\ (c_{d}-\lambda)/a_{d}&如果 c_{d}>\lambda\end{array}\right.   \tag*{(11.87)}$$

我们可以将其写为：

$$  \hat{w}_{d}=SoftThreshold(\frac{c_{d}}{a_{d}},\lambda/a_{d})   \tag*{(11.88)}$$

其中

$$   SoftThreshold(x,\delta)\triangleq sign(x)\left(|x|-\delta\right)_{+}   \tag*{(11.89)}$$

而 $ x_{+} = \max(x, 0) $ 表示 $ x $ 的正部。这被称为**软阈值化**（另见第 8.6.2 节）。图 11.9(a) 展示了这一过程，其中我们绘制了 $ \hat{w}_d $ 随 $ c_d $ 的变化。黑色虚线对应最小二乘拟合的直线 $ w_d = c_d / a_d $。代表正则化估计值 $ \hat{w}_d $ 的实线红线将该虚线向下（或向上）平移了 $ \lambda $，除非 $ -\lambda \leq c_d \leq \lambda $，此时它将 $ w_d $ 设置为 0。

相比之下，我们在图 11.9(b) 中展示了**硬阈值化**。当 $ -\lambda \leq c_d \leq \lambda $ 时，它将 $ w_d $ 的值设为 0，但在此区间之外，它不会对 $ w_d $ 的值进行收缩。软阈值化的斜率是

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_194_125_563_423.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_614_123_961_413.jpg" alt="Image" width="30%" /></div>


<div style="text-align:center;">(b)</div>


<div style="text-align: center;">图11.10：(a) 前列腺癌示例中岭回归系数随 $ \boldsymbol{w} $ 的 $ \ell_2 $ 范数约束 $ B $ 变化的轮廓图，因此较小的 $ B $（较大的 $ \lambda $）位于左侧。竖线为使用一倍标准误规则的五折交叉验证选定的值。改编自[HTF09]的图3.8，由 ridgePathProstate.ipynb 生成。(b) 与(a)相同，但使用 $ \boldsymbol{w} $ 的 $ \ell_1 $ 范数。x轴显示临界值 $ \lambda = 1/B $，此处正则化路径是不连续的。改编自[HTF09]的图3.10，由 lassoPathProstate.ipynb 生成。</div>


阈值线并未与对角线重合，这意味着即便是大的系数也被向零收缩。这就是 lasso （最小绝对收缩与选择算子）名称的由来。因此，lasso 是一种有偏估计量（参见 4.7.6.1 节）。

对于有偏估计问题，一种简单的解决方案称为**去偏**，即使用两阶段估计过程：首先利用 lasso 估计权重向量的支撑集（即识别哪些元素非零）；然后使用最小二乘法重新估计选中的系数。实际应用示例见图11.13。

#### 11.4.4 正则化路径

若 $ \lambda = 0 $，则得到 OLS 解，该解是稠密的。随着 $ \lambda $ 增大，解向量 $ \hat{\boldsymbol{w}}(\lambda) $ 趋于稀疏。若 $ \lambda $ 大于某个临界值，则得到 $ \hat{\boldsymbol{w}} = \mathbf{0} $。该临界值出现在负对数似然的梯度与惩罚项的梯度相互抵消时：

$$  \lambda_{\max}=\max_{d}|\nabla_{w_{d}}\mathrm{NLL}(\mathbf{0})|=\max_{d}c_{d}(\boldsymbol{w}=0)=\max_{d}|\boldsymbol{y}^{\top}\boldsymbol{x}_{:,d}|=||\mathbf{X}^{\top}\boldsymbol{y}||_{\infty}   \tag*{(11.90)}$$

或者，我们也可以使用 $ \ell_1 $ 范数的约束 $ B $。当 $ B = 0 $ 时，有 $ \hat{\boldsymbol{w}} = \mathbf{0} $。随着 $ B $ 增大，解变得更稠密。使得任何分量均为零的最大 $ B $ 值为 $ B_{\max} = ||\hat{\boldsymbol{w}}_{\text{mle}}||_1 $。

随着 $ \lambda $ 增大，解向量 $ \hat{w} $ 变得更稀疏，尽管并非单调递减。我们可以针对每个特征 $ d $ 绘制 $ \hat{w}_d $ 随 $ \lambda $（或约束 $ B $）变化的曲线；这被称为**正则化路径**。图11.10(b)展示了这一结果，其中我们将 lasso 应用于[HTF09]中的前列腺癌回归数据集（我们将特征 gleason 和 svi 视为数值型而非分类型）。在左侧，

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.4279</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.5015</td><td style='text-align: center; word-wrap: break-word;'>0.0735</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.5610</td><td style='text-align: center; word-wrap: break-word;'>0.1878</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0930</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.5622</td><td style='text-align: center; word-wrap: break-word;'>0.1890</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0036</td><td style='text-align: center; word-wrap: break-word;'>0.0963</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.5797</td><td style='text-align: center; word-wrap: break-word;'>0.2456</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.1435</td><td style='text-align: center; word-wrap: break-word;'>0.2003</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.0901</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.5864</td><td style='text-align: center; word-wrap: break-word;'>0.2572</td><td style='text-align: center; word-wrap: break-word;'>-0.0321</td><td style='text-align: center; word-wrap: break-word;'>0.1639</td><td style='text-align: center; word-wrap: break-word;'>0.2082</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.1066</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.6994</td><td style='text-align: center; word-wrap: break-word;'>0.2910</td><td style='text-align: center; word-wrap: break-word;'>-0.1337</td><td style='text-align: center; word-wrap: break-word;'>0.2062</td><td style='text-align: center; word-wrap: break-word;'>0.3003</td><td style='text-align: center; word-wrap: break-word;'>-0.2565</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.2452</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0.7164</td><td style='text-align: center; word-wrap: break-word;'>0.2926</td><td style='text-align: center; word-wrap: break-word;'>-0.1425</td><td style='text-align: center; word-wrap: break-word;'>0.2120</td><td style='text-align: center; word-wrap: break-word;'>0.3096</td><td style='text-align: center; word-wrap: break-word;'>-0.2890</td><td style='text-align: center; word-wrap: break-word;'>-0.0209</td><td style='text-align: center; word-wrap: break-word;'>0.2773</td></tr></table>

<div style="text-align: center;">表11.1：随着 $\ell_{1}$ 正则化强度的变化，拟合前列腺癌数据集的线性回归模型系数值。这些数值绘制在图11.10(b)中。</div>

当 B=0 时，所有系数都为零。随着 B 增加，系数逐渐“激活”。$^{2}$ 岭回归的类似结果如图11.10(a)所示。对于岭回归，我们看到所有系数都非零（假设 λ>0），因此解不是稀疏的。

值得注意的是，可以证明lasso的解路径是 $\lambda$ 的分段线性函数 [Efr+04; GL15]。也就是说，存在一组 $\lambda$ 的临界值，在此处非零系数的活动集发生变化。对于这些临界值之间的 $\lambda$，每个非零系数线性增加或减少。如图11.10(b)所示。此外，可以解析地求解这些临界值 [Efr+04]。在表11.1中，我们展示了沿着正则化路径在每个临界步骤处的实际系数值（最后一行是最小二乘解）。

通过将 $\lambda$ 从 $\lambda_{\text{max}}$ 改变到 0，我们可以从所有权重为零的解过渡到所有权重都非零的解。不幸的是，并非所有子集大小都可以通过lasso实现。特别地，可以证明，如果 $D > N$，在达到对应于最小 $\ell_1$ 范数的OLS解的完整集合之前，最优解中最多可以有 $N$ 个变量。在第11.4.8节中，我们将看到通过同时使用 $\ell_2$ 正则化器和 $\ell_1$ 正则化器（一种称为弹性网络的方法），我们可以获得包含比训练样本更多变量的稀疏解。这使我们能够探索介于 $N$ 和 $D$ 之间的模型大小。

#### 11.4.5 最小二乘法、lasso、岭回归和子集选择的比较

在本节中，我们比较最小二乘法、lasso、岭回归和子集选择。为简单起见，我们假设 $\mathbf{X}$ 的所有特征都是标准正交的，因此 $\mathbf{X}^{\top}\mathbf{X} = \mathbf{I}$。在这种情况下，NLL 由下式给出：

$$  \begin{aligned}\mathrm{N L L}(\boldsymbol{w})&=||\boldsymbol{y}-\boldsymbol{X}\boldsymbol{w}||^{2}=\boldsymbol{y}^{\top}\boldsymbol{y}+\boldsymbol{w}^{\top}\boldsymbol{X}^{\top}\boldsymbol{X}\boldsymbol{w}-2\\&=\mathrm{c o n s t}+\sum_{d}w_{d}^{2}-2\sum_{d}\sum_{n}w_{d}x_{n d}y_{n}\end{aligned}   \tag*{(11.92)}$$

因此我们看到这分解为每个维度一项的和。因此我们可以分别对每个 $w_d$ 解析写出 MAP 和 ML 估计，如下所示。

• MLE 由方程 (11.85)，OLS 解为：

$$  \hat{w}_{d}^{\mathrm{m l e}}=c_{d}/a_{d}=\boldsymbol{x}_{:d}^{\mathsf{T}}\boldsymbol{y}   \tag*{(11.93)}$$

其中 $\boldsymbol{x}_{:d}$ 是 $\mathbf{X}$ 的第 $d$ 列。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>项</td><td style='text-align: center; word-wrap: break-word;'>普通最小二乘 (OLS)</td><td style='text-align: center; word-wrap: break-word;'>最优子集 (Best Subset)</td><td style='text-align: center; word-wrap: break-word;'>岭回归 (Ridge)</td><td style='text-align: center; word-wrap: break-word;'>套索 (Lasso)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>截距</td><td style='text-align: center; word-wrap: break-word;'>2.465</td><td style='text-align: center; word-wrap: break-word;'>2.477</td><td style='text-align: center; word-wrap: break-word;'>2.467</td><td style='text-align: center; word-wrap: break-word;'>2.465</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lcalvol</td><td style='text-align: center; word-wrap: break-word;'>0.676</td><td style='text-align: center; word-wrap: break-word;'>0.736</td><td style='text-align: center; word-wrap: break-word;'>0.522</td><td style='text-align: center; word-wrap: break-word;'>0.548</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lweight</td><td style='text-align: center; word-wrap: break-word;'>0.262</td><td style='text-align: center; word-wrap: break-word;'>0.315</td><td style='text-align: center; word-wrap: break-word;'>0.255</td><td style='text-align: center; word-wrap: break-word;'>0.224</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>age</td><td style='text-align: center; word-wrap: break-word;'>-0.141</td><td style='text-align: center; word-wrap: break-word;'>0.000</td><td style='text-align: center; word-wrap: break-word;'>-0.089</td><td style='text-align: center; word-wrap: break-word;'>0.000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lbph</td><td style='text-align: center; word-wrap: break-word;'>0.209</td><td style='text-align: center; word-wrap: break-word;'>0.000</td><td style='text-align: center; word-wrap: break-word;'>0.186</td><td style='text-align: center; word-wrap: break-word;'>0.129</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>svi</td><td style='text-align: center; word-wrap: break-word;'>0.304</td><td style='text-align: center; word-wrap: break-word;'>0.000</td><td style='text-align: center; word-wrap: break-word;'>0.259</td><td style='text-align: center; word-wrap: break-word;'>0.186</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>lcp</td><td style='text-align: center; word-wrap: break-word;'>-0.287</td><td style='text-align: center; word-wrap: break-word;'>0.000</td><td style='text-align: center; word-wrap: break-word;'>-0.095</td><td style='text-align: center; word-wrap: break-word;'>0.000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>gleason</td><td style='text-align: center; word-wrap: break-word;'>-0.021</td><td style='text-align: center; word-wrap: break-word;'>0.000</td><td style='text-align: center; word-wrap: break-word;'>0.025</td><td style='text-align: center; word-wrap: break-word;'>0.000</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pgg45</td><td style='text-align: center; word-wrap: break-word;'>0.266</td><td style='text-align: center; word-wrap: break-word;'>0.000</td><td style='text-align: center; word-wrap: break-word;'>0.169</td><td style='text-align: center; word-wrap: break-word;'>0.083</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>测试误差</td><td style='text-align: center; word-wrap: break-word;'>0.521</td><td style='text-align: center; word-wrap: break-word;'>0.492</td><td style='text-align: center; word-wrap: break-word;'>0.487</td><td style='text-align: center; word-wrap: break-word;'>0.457</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>标准误差</td><td style='text-align: center; word-wrap: break-word;'>0.176</td><td style='text-align: center; word-wrap: break-word;'>0.141</td><td style='text-align: center; word-wrap: break-word;'>0.157</td><td style='text-align: center; word-wrap: break-word;'>0.146</td></tr></table>

<div style="text-align: center;">图 11.11：不同方法在前列腺癌数据上的结果，该数据包含 8 个特征和 67 个训练样本。方法包括：OLS = 普通最小二乘，Subset = 最优子集回归，Ridge = 岭回归，Lasso = 套索。行表示系数；可以看出子集回归和套索给出了稀疏解。最下面一行是测试集（30 个样本）上的均方误差。改编自 [HTF09] 的表 3.3。由 prostate_comparison.ipymb 生成。</div>

• 岭回归 可以证明岭估计为

$$  \hat{w}_{d}^{\text{ridge}}=\frac{\hat{w}_{d}^{\text{mle}}}{1+\lambda}   \tag*{(11.94)}$$

• 套索 根据式 (11.88)，并利用 $\hat{w}_d^{\mathrm{mle}} = c_d / a_d$，有

$$  \hat{w}_{d}^{\text{lasso}}=\operatorname{sign}(\hat{w}_{d}^{\mathrm{mle}})\left(|\hat{w}_{d}^{\mathrm{mle}}|-\lambda\right)_{+}   \tag*{(11.95)}$$

这对应于软阈值化，如图 11.9(a) 所示。

- 子集选择 若通过子集选择挑选最优的 K 个特征，参数估计如下：

$$  \hat{w}_{d}^{\mathrm{ss}}=\left\{\begin{array}{cc}\hat{w}_{d}^{\mathrm{mle}} & \text{if } \operatorname{rank}(|\hat{w}_{d}^{\mathrm{mle}}|)\leq K \\ 0 & \text{otherwise}\end{array}\right.   \tag*{(11.96)}$$

其中 rank 指在权重绝对值排序列表中的位置。这对应于硬阈值化，如图 11.9(b) 所示。

我们现在通过实验比较这些方法在 [HTF09] 的前列腺癌回归数据集上的预测性能。（我们将特征 gleason 和 svi 视为数值型而非分类型。）图 11.11 显示了在通过交叉验证选定的 $\lambda$（或 K）值下估计的系数；可以看到子集方法最稀疏，其次是套索。在预测性能方面，所有方法非常相似，如图 11.12 所示。

作者：Kevin P. Murphy。(C) MIT 出版社。遵循 CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_411_151_742_393.jpg" alt="图" width="28%" /></div>

<div style="text-align: center;">图 11.12: 箱线图展示了不同回归方法在前列腺癌测试集上的预测误差（绝对值）。由 prostate comparison.ipynb 生成。</div>

#### 11.4.6 变量选择一致性

使用 $\ell_1$ 正则化来估计相关变量集合是一种常见做法，该过程称为变量选择。能够在 $N \to \infty$ 极限下恢复真实相关变量集（即 $\boldsymbol{w}^*$ 的支撑集）的方法称为模型选择一致性。（这是一个理论概念，假设数据来自该模型。）

我们举一个例子。首先，生成一个大小为 $D = 4096$ 的稀疏信号 $\boldsymbol{w}^*$，由160个随机放置的 $\pm 1$ 尖峰组成。接着，生成一个 $N \times D$ 的随机设计矩阵 $\boldsymbol{X}$，其中 $N = 1024$。最后，生成一个带噪声的观测值 $\boldsymbol{y} = \boldsymbol{X} \boldsymbol{w}^* + \epsilon$，其中 $\epsilon_n \sim \mathcal{N}(0, 0.01^2)$。然后，从 $\boldsymbol{y}$ 和 $\boldsymbol{X}$ 中估计 $\boldsymbol{w}$。原始 $\boldsymbol{w}^*$ 显示在图 Figure 11.13 的第一行。第二行是使用 $\lambda = 0.1\lambda_{\max}$ 得到的 $\ell_1$ 估计 $\hat{\boldsymbol{w}}_{L1}$。我们看到它在正确的位置上有“尖峰”，因此正确识别了相关变量。然而，尽管 $\hat{\boldsymbol{w}}_{L1}$ 正确识别了非零分量，但由于收缩作用，它们太小了。第三行展示了使用 Section 11.4.3 讨论的去偏技术的结果。这表明我们可以恢复原始的权重向量。相比之下，最后一行显示了OLS估计，它是稠密的。此外，从视觉上可以明显看出，不存在一个单一的阈值可以应用于 $\hat{\boldsymbol{w}}_{mle}$ 来恢复正确的稀疏权重向量。

要使用lasso进行变量选择，我们必须选择 $\lambda$。通常使用交叉验证来选取正则化路径上的最优值。然而，需要注意的是，交叉验证选取的 $\lambda$ 值能使预测准确性良好。这个值通常与可能恢复“真实”模型的值不同。原因在于，$\ell_1$ 正则化同时执行选择和收缩，即所选系数被拉近于0。为了防止相关系数以这种方式被收缩，交叉验证倾向于选择一个不太大的 $\lambda$ 值。当然，这会导致模型不够稀疏，包含不相关变量（假阳性）。实际上，[MB06] 证明了预测最优的 $\lambda$ 值并不能实现模型选择一致性。然而，人们已设计出基本方法的多种扩展，这些扩展具有模型选择一致性（例如 [BG11; HTW15]）。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_338_147_839_527.jpg" alt="图片" width="43%" /></div>

<div style="text-align: center;">图 11.13：使用 lasso 恢复稀疏信号的示例。详见正文。改编自 [FNW07] 的图 1。由 sparse_sensing_demo.ipynb 生成。</div>

#### 11.4.7 组 lasso

在标准的 $ \ell_1 $ 正则化中，我们假设参数与变量之间是一一对应的，因此当 $ \hat{w}_d = 0 $ 时，我们将其解释为变量 $ d $ 被排除。但在更复杂的模型中，一个变量可能关联多个参数。具体来说，每个变量 $ d $ 可能对应一个权重向量 $ \boldsymbol{w}_d $，因此整个权重向量具有块结构：$ \boldsymbol{w} = [\boldsymbol{w}_1, \boldsymbol{w}_2, \ldots, \boldsymbol{w}_d] $。如果要排除变量 $ d $，必须迫使整个子向量 $ \boldsymbol{w}_d $ 为零。这称为**组稀疏性**。

##### 11.4.7.1 应用

以下是一些组稀疏性有用的例子：

- **含分类输入的线性回归**：如果第 $ d $ 个变量是取 K 个可能水平的分类变量，那么它将被表示为一个长度为 K 的独热向量（第 1.5.3.1 节），因此要排除变量 d，必须将整个输入权重向量置为 0。

- **多项逻辑回归**：第 $ d $ 个变量将关联 C 个不同的权重，每个类别一个（第 10.3 节），因此要排除变量 d，必须将整个输出权重向量置为 0。

- **神经网络**：第 k 个神经元可能有多个输入，如果要“关闭该神经元”，必须将所有输入权重置为 0。这使得我们可以利用组稀疏性来学习神经网络结构（详见例如 [GEH19]）。

作者：Kevin P. Murphy。(C) 麻省理工学院出版社。CC-BY-NC-ND 许可。

---

- 多任务学习：每个输入特征关联 C 个不同的权重，每个输出任务对应一个权重。如果我们希望某个特征要么用于所有任务、要么完全不用于任何任务，那么应当在组级别上选择权重 [OTJ07]。

##### 11.4.7.2 对二范数施加惩罚

为了鼓励组稀疏性，我们将参数向量划分为 $G$ 个组：$\boldsymbol{w} = [\boldsymbol{w}_1, \ldots, \boldsymbol{w}_G]$。然后我们最小化以下目标函数：

$$  \mathrm{PNLL}(\boldsymbol{w})=\mathrm{NLL}(\boldsymbol{w})+\lambda\sum_{g=1}^{G}||\boldsymbol{w}_{g}||_{2}   \tag*{(11.97)}$$

其中 $ \|w_g\|_2 = \sqrt{\sum_{d \in g} w_d^2} $ 是组权重向量的二范数。如果 NLL 是最小二乘，则该方法称为 **组套索** [YL06; Kyu+10]。

注意，如果在公式 (11.97) 中使用平方二范数的和，则模型将等价于岭回归，因为

$$  \sum_{g=1}^{G}||\boldsymbol{w}_{g}||_{2}^{2}=\sum_{g}\sum_{d\in g}w_{d}^{2}=||\boldsymbol{w}||_{2}^{2}   \tag*{(11.98)}$$

通过使用平方根，我们实际上是在惩罚包含该组权重向量的球的半径：要使半径变小，唯一方法是所有元素都很小。

另一种理解平方根版本如何在组级别强制稀疏性的方式，是考虑目标函数的梯度。假设只有一组且包含两个变量，则惩罚项形式为 $ \sqrt{w_1^2 + w_2^2} $。对 $ w_1 $ 的导数为

$$  \frac{\partial}{\partial w_{1}}(w_{1}^{2}+w_{2}^{2})^{\frac{1}{2}}=\frac{w_{1}}{\sqrt{w_{1}^{2}+w_{2}^{2}}}   \tag*{(11.99)}$$

如果 $ w_{2} $ 接近零，则导数趋近于 1，$ w_{1} $ 也会被推向零，且作用力与 $ \lambda $ 成正比。然而，如果 $ w_{2} $ 很大，则导数趋近于 0，$ w_{1} $ 也可以保持较大的值。因此，组内所有系数的大小将趋于一致。

##### 11.4.7.3 对无穷范数施加惩罚

该技术的一个变体是将二范数替换为无穷范数 [TVW05; ZRY05]：

$$  \left|\left|\boldsymbol{w}_{g}\right|\right|_{\infty}=\max_{d\in g}\left|w_{d}\right|   \tag*{(11.100)}$$

显然，这也会导致组稀疏性，因为如果组内最大元素被强制为零，那么所有更小的元素也会随之归零。

##### 11.4.7.4 示例

图 11.14 和图 11.15 展示了这些技术的示例。我们有一个大小为 $ D = 2^{12} = 4096 $ 的真实信号 w，被分为 64 个组，每组大小 64。我们随机选择 8 个组

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_226_125_543_396.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_634_125_950_394.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_226_446_543_717.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_634_447_950_716.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 11.14：组套索的示意图，其中原始信号是分段高斯分布。(a) 原始信号。(b) 普通套索估计。(c) 使用块上 $ \ell_{2} $ 范数的组套索估计。(d) 使用块上 $ \ell_{\infty} $ 范数的组套索估计。改编自 [WNF09] 中的图 3-4。由 groupLassoDemo.ipynb 生成。</div>


将 $\boldsymbol{w}$ 中的元素赋予非零值。在图 11.14 中，这些值来自 $\mathcal{N}(0,1)$；在图 11.15 中，所有值都设为 1。然后我们对大小为 $N \times D$ 的随机设计矩阵 $\mathbf{X}$ 进行采样，其中 $N = 2^{10} = 1024$。最后，我们生成 $\boldsymbol{y} = \mathbf{X}\boldsymbol{w} + \boldsymbol{\epsilon}$，其中 $\boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, 10^{-4} \mathbf{I}_N)$。给定这些数据，我们使用 $\ell_1$ 或组 $\ell_1$ 估计 $\boldsymbol{w}$ 的支撑集，然后使用最小二乘法（去偏估计）估计非零值。

从这些图中可以看出，组套索比普通套索效果好得多，因为它尊重已知的组结构。我们还看到，$ \ell_{\infty} $ 范数倾向于使一个块内的所有元素具有相似的幅度。这在第二个例子中是合适的，但在第一个例子中则不然。（所有例子中的 $\lambda$ 值相同，并且是手动选择的。）

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_219_125_544_395.jpg" alt="图片" width="28%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_626_125_950_395.jpg" alt="图片" width="28%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_219_446_543_717.jpg" alt="图片" width="28%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_627_446_951_716.jpg" alt="图片" width="28%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图 11.15：与图 11.14 相同，只是原始信号为分段常数。由 groupLassoDemo.ipynb 生成。</div>

#### 11.4.8 弹性网络（岭回归与套索回归的结合）

在组套索回归中，我们需要预先指定组结构。对于某些问题，我们不知道组结构，但仍希望将高度相关的系数视为一个隐式组。文献 [ZH05] 提出的一种实现这一效果的方法是使用弹性网络，它是套索回归和岭回归的混合体。$^{3}$ 这对应于最小化以下目标函数：

$$  \mathcal{L}(w,\lambda_{1},\lambda_{2})=||y-\mathbf{X}w||^{2}+\lambda_{2}||w||_{2}^{2}+\lambda_{1}||w||_{1}   \tag*{(11.101)}$$

该惩罚函数是严格凸的（假设 $\lambda_2 > 0$），因此即使 $\mathbf{X}$ 不是满秩的，也存在唯一的全局最小值。文献 [ZH05] 表明，任何关于 $\mathbf{w}$ 的严格凸惩罚都会表现出 **分组效应**，这意味着高度相关变量的回归系数倾向于

---

相等。特别地，若两个特征完全相同，即 $\mathbf{X}_{:j} = \mathbf{X}_{:k}$，则其估计值也相等，即 $\hat{w}_j = \hat{w}_k$。相比之下，使用套索（lasso）时，可能出现 $\hat{w}_j = 0$ 而 $\hat{w}_k \neq 0$ 或相反的情况，导致估计结果不够稳定。

除了其软分组（soft grouping）特性外，弹性网（elastic net）还具有其他优势。特别地，若 $D > N$，所能选择的最大非零元素个数（不包括含 $D$ 个非零元素的 MLE）为 $N$。相比之下，弹性网在其通往稠密估计的路径上可以选取超过 $N$ 个非零变量，从而探索更多可能的变量子集。

#### 11.4.9 优化算法

已有大量算法被提出用于求解套索问题及其他 $\ell_1$ 正则化的凸目标函数。本节我们简要介绍几种最常用的方法。

##### 11.4.9.1 坐标下降

有时同时优化所有变量很困难，但逐一优化较为容易。具体而言，我们可以在固定其他所有系数的情况下，求解第 $j$ 个系数，如下所示：

$$ w_{j}^{*}=\underset{\eta}{\operatorname{argmin}}\mathcal{L}(\boldsymbol{w}+\eta\boldsymbol{e}_{j})   \tag*{(11.102)}$$

其中 $\boldsymbol{e}_{j}$ 是第 $j$ 个单位向量。该方法称为**坐标下降**。我们可以按确定性顺序循环遍历各坐标，也可以随机采样，或者选择梯度最陡的坐标进行更新。

如果每个一维优化问题都能解析求解（如套索情形，见式 (11.87)），则该方法尤为吸引人。这就是所谓的**射击算法** [Fu98; WL08]。（“射击”一词源于“套索”所蕴含的牛仔主题。）详见算法 11.1。

这种坐标下降方法已被推广至 GLM 情形 [FHT10]，并且是流行的 glmnet 软件库的基础。

**算法 11.1：套索的坐标下降（又称射击算法）**

1. 初始化 $ w = (X^{\top}X + \lambda I)^{-1}X^{\top}y $
2. repeat
3. | for $ d = 1, \ldots, D $ do
4. | $ a_{d} = \sum_{n=1}^{N} x_{nd}^{2} $
5. | $ c_{d} = \sum_{n=1}^{N} x_{nd}(y_{n} - w^{\top}x_{n} + w_{d}x_{nd}) $
6. | $ w_{d} = \text{SoftThreshold}(\frac{c_{d}}{a_{d}}, \lambda / a_{d}) $
7. until converged

##### 11.4.9.2 投影梯度下降

在本节中，我们将不可微的 $\ell_1$ 惩罚项转化为一个光滑的正则化项。为此，首先使用变量分裂技巧定义 $ w = w^+ - w^- $，其中 $ w^+ = \max\{w, 0\} $，且

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证

---

$ \boldsymbol{w}^{-} = -\min\{\boldsymbol{w}, 0\} $。现在我们可以将 $ ||\boldsymbol{w}||_1 $ 替换为 $ \sum_d(w_d^+ + w_d^-) $。同时，还需将 $ \mathrm{NLL}(\boldsymbol{w}) $ 替换为 $ \mathrm{NLL}(\boldsymbol{w}^+ + \boldsymbol{w}^-) $。由此得到如下光滑但带约束的优化问题：

$$  \min_{\boldsymbol{w}^{+}\geq0,\boldsymbol{w}^{-}\geq0}\mathrm{N L L}(\boldsymbol{w}^{+}-\boldsymbol{w}^{-})+\lambda\sum_{d=1}^{D}(w_{d}^{+}+w_{d}^{-})   \tag*{(11.103)}$$

在高斯似然情况下，NLL退化为最小二乘损失，目标函数变为一个二次规划（第8.5.4节）。求解此类问题的一种方法是使用投影梯度下降（第8.6.1节）。具体地，我们可以通过向正象限投影来施加约束，即使用 $ w_d := \max(w_d, 0) $；此操作记为 $ P_+ $。因此，投影梯度更新形式如下：

$$  \begin{pmatrix}\boldsymbol{w}_{t+1}^{+}\\\boldsymbol{w}_{t+1}^{-}\end{pmatrix}=P_{+}\left(\begin{bmatrix}\boldsymbol{w}_{t}^{+}-\eta_{t}\nabla\mathrm{N L L}(\boldsymbol{w}_{t}^{+}-\boldsymbol{w}_{t}^{-})-\eta_{t}\lambda\boldsymbol{e}\\\boldsymbol{w}_{t}^{-}+\eta_{t}\nabla\mathrm{N L L}(\boldsymbol{w}_{t}^{+}-\boldsymbol{w}_{t}^{-})-\eta_{t}\lambda\boldsymbol{e}\end{bmatrix}\right)   \tag*{(11.104)}$$

其中 $\boldsymbol{e}$ 为单位向量。

##### 11.4.9.3 近端梯度下降

在第8.6节中，我们介绍了近端梯度下降，该方法可用于优化带有非光滑惩罚（如 $\ell_{1}$）的光滑函数。在第8.6.2节中，我们指出 $\ell_{1}$ 惩罚的近端算子对应于软阈值化。因此，近端梯度下降更新可写为

$$  \boldsymbol{w}_{t+1}=SoftThreshold(\boldsymbol{w}_{t}-\boldsymbol{\eta}_{t}\nabla NLL(\boldsymbol{w}_{t}),\boldsymbol{\eta}_{t}\boldsymbol{\lambda})   \tag*{(11.105)}$$

其中软阈值算子（式(8.134)）逐元素应用。这被称为迭代软阈值算法（ISTA）[DDDM04; Don95]。若将其与Nesterov加速结合，则得到“快速ISTA”（FISTA）[BT09]，该方法被广泛用于拟合稀疏线性模型。

##### 11.4.9.4 LARS算法

本节讨论能够针对不同 $\lambda$ 值生成一组解（从空集开始）的方法，即计算完整的正则化路径（第11.4.4节）。这些算法利用了如下事实：当 $\lambda_k \approx \lambda_{k-1}$ 时，可以快速从 $\dot{\mathbf{w}}(\lambda_{k-1})$ 计算 $\dot{\mathbf{w}}(\lambda_k)$；这称为热启动（warm starting）。事实上，即使我们只需求解单个 $\lambda$（记为 $\lambda_*$）的解，有时通过热启动，从 $\lambda_{\max}$ 向下计算至 $\lambda_*$ 的一组解反而在计算上更高效；这称为延续方法或同伦方法。这通常比直接在 $\lambda_*$ 处“冷启动”快得多，尤其在 $\lambda_*$ 较小时。

LARS算法（“最小角回归与收缩”）[Efr+04]是用于lasso问题的同伦方法的一个实例。它能够高效地计算所有可能 $\lambda$ 值下的 $\hat{\boldsymbol{w}}(\lambda)$。（类似算法也在[OPT00b; OPT00a]中独立提出）。

LARS的工作方式如下：从一个较大的 $\lambda$ 值开始，此时仅选择与响应向量 y 相关性最强的变量。然后逐渐减小 $\lambda$，直到找到第二个变量，该变量与当前残差的相关性（按绝对值）与第一个变量相同。

---

在路径第 $k$ 步的残差定义为 $\boldsymbol{r}_k = \boldsymbol{y} - \boldsymbol{X}_{:,F_k} \boldsymbol{w}_k$，其中 $F_k$ 是当前的 **活跃集**（参见公式 (11.83)）。值得注意的是，通过几何论证（因此得名“最小角”），可以解析地求解 $\lambda$ 的这个新值。这使得算法能够快速“跳转”到正则化路径上活跃集发生变化的下一位置。这一过程重复进行，直到所有变量都被添加。

为了使得解序列对应于 Lasso 的正则化路径，即使当 $\lambda$ 增加时，也需要允许变量从当前活跃集中移除。如果不允许变量移除，则会得到一种略有不同的算法，称为最小角回归（LAR）。LAR 与贪婪前向选择以及一种称为最小二乘提升的方法非常相似（参见例如 [HTW15]）。

### 11.5 回归样条  $ * $

我们已经看到如何利用多项式基函数来创建从输入到输出的非线性映射，尽管模型在参数上仍是线性的。多项式的一个问题是它们是对函数的全局逼近。通过使用一系列局部逼近，我们可以获得更高的灵活性。为此，我们只需定义一组具有局部支撑的基函数。在高维输入空间中，“局域性”的概念难以定义，因此在本节中，我们限制输入为一维。然后我们可以使用下式来逼近函数：

$$  f(x;\boldsymbol{\theta})=\sum_{i=1}^{m}w_{i}B_{i}(x)   \tag*{(11.106)}$$

其中 $ B_{i} $ 是第 $ i $ 个基函数。

定义此类基函数的一种常用方法是使用 B 样条（“B”代表“基”，“样条”指艺术家用来绘制曲线的柔性条状材料）。我们将在第 11.5.1 节中更详细地讨论这一点。

#### 11.5.1 B 样条基函数

样条是次数为 $D$ 的分段多项式，各段的位点由一组 **结点** $t_1 < \cdots < t_m$ 定义。更精确地说，多项式定义在每个区间 $(-\infty, t_1)$、$[t_1, t_2]$、...、$[t_m, \infty)$ 上。该函数在结点处连续，且具有连续的 $1, \ldots, D-1$ 阶导数。通常使用 **三次** 样条，即 $D = 3$。这保证了函数连续，并且在每个结点处具有连续的一阶和二阶导数。

我们将跳过 B 样条如何计算的细节，因为这与我们当前的目的无关。只需说明，我们可以调用 patsy.bs 函数，将 $ N \times 1 $ 的数据矩阵 $ \mathbf{X} $ 转换为 $ N \times (K + D + 1) $ 的设计矩阵 $ \mathbf{B} $，其中 $ K $ 是结点数，$ D $ 是次数。（或者，您可以指定所需的基函数数量，让 patsy 自动计算结点的数量和位置。）

图 Figure 11.16 展示了这种方法，我们使用了次数为 0、1 和 3 的 B 样条，并设置了 3 个结点。通过对这些基函数进行加权组合，我们可以得到越来越平滑的函数，如底行所示。

从图 Figure 11.16 可以看出，每个单独的基函数都具有局部支撑。在任意给定的输入点 $x$ 处，只有 $ D+1 $ 个基函数是“活跃的”。如果我们绘制设计矩阵，这一点会更加明显。

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_280_143_878_457.jpg" alt="Image" width="51%" /></div>

<div style="text-align: center;">图 11.16：0 次、1 次和 3 次 B 样条的示意图。顶行：未加权的基函数。圆点标记了 [0.25, 0.5, 0.75] 处的三个内部结点位置。底行：使用随机权重对基函数进行加权组合。由 splines_basis_weighted.ipynb 生成。改编自文献 [MKL11] 的图 5.4。经 Osvaldo Martin 许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_182_624_441_800.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_460_624_722_802.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_740_624_999_799.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图 11.17：(a) 0 次、(b) 1 次和 (c) 3 次 B 样条的设计矩阵。我们在从 0 到 1 的 20 个输入上评估样条。由 splines_basis_heatmap.ipynb 生成。改编自文献 [MKL11] 的图 5.6。经 Osvaldo Martin 许可使用。</div>

B 本身。我们首先考虑分段常数样条，如图 11.17(a) 所示。第一个 B 样条（列 1）在前 5 个观测上为 1，其余为 0。第二个 B 样条（列 0）在前 5 个观测上为 0，在第二个 5 个观测上为 1，然后又变为 0。以此类推。现在考虑线性样条，如图 11.17(b) 所示。第一个 B 样条（列 0）从 1 下降到 0，接下来的三个样条从 0 上升到 1 再下降到 0；最后一个样条（列 4）从 0 上升到 1；这反映了图 11.16 顶部中间面板所示的三角形形状。最后考虑三次样条，如图 11.17(c) 所示。这里的激活模式更加平滑，因此得到的模型拟合也会更平滑。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_383_131_786_392.jpg" alt="图像" width="34%" /></div>


<div style="text-align: center;">图 11.18: 对一维数据集拟合具有15个结点的三次样条回归模型。由 splines_cherry_blossoms.ipynb 生成。改编自 [McE20] 的图 5.3。</div>


#### 11.5.2 使用样条基函数拟合线性模型

一旦计算出设计矩阵 B，我们就可以使用最小二乘法或岭回归来拟合线性模型（通常最好使用某种正则化）。例如，我们考虑来自 [McE20, Sec 4.5] 的一个数据集，该数据集记录了标志着日本樱花季开始的一年中的第一天以及相应的温度（我们使用这个数据集是因为它具有有趣的半周期结构）。我们使用三次样条对数据进行拟合。我们选择了 15 个结点，按照数据的分位数进行间隔。结果如图 11.18 所示。可以看到拟合效果较为合理。使用更多结点可以提高拟合质量，但最终会导致过拟合。我们可以使用模型选择方法（如网格搜索加交叉验证）来选择结点数量。

#### 11.5.3 平滑样条

平滑样条与回归样条相关，但使用 N 个结点，其中 N 是数据点的数量。也就是说，它们是**非参数模型**，因为参数数量随数据规模增长，而不是事先固定的。为了避免过拟合，平滑样条依赖于 $\ell_{2}$ 正则化。该技术与我们将在第 17.2 节讨论的高斯过程回归密切相关。

#### 11.5.4 广义加性模型

广义加性模型（GAM）将样条回归扩展到多维输入的情况 [HT90]。它通过忽略输入之间的交互作用，并假设函数具有以下加性形式来实现这一扩展：

$$ f(\boldsymbol{x};\boldsymbol{\theta})=\alpha+\sum_{d=1}^{D}f_{d}(x_{d}) \tag*{(11.107)}$$

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_235_125_531_381.jpg" alt="图像" width="25%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_619_123_959_405.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 11.19: (a) 鲁棒线性回归的示意图。由 linregRobustDemoCombined.ipynb 生成。(b) $\ell_{2}$、$\ell_{1}$ 和 Huber 损失函数（$\delta = 1.5$）的示意图。由 huberLossPlot.ipynb 生成。</div>


其中每个 $f_{d}$ 是一个回归样条或平滑样条。该模型可以通过后退拟合（backfitting）进行拟合，该方法迭代地将每个 $f_{d}$ 拟合到由其他项产生的偏残差上。我们可以通过使用连接函数将广义可加模型（GAMs）扩展到回归之外的情况（例如分类），如同广义线性模型（第12章）一样。

### 11.6 鲁棒线性回归 *

在回归模型中，通常使用均值为零且方差恒定的高斯分布来建模噪声，即 $r_n \sim \mathcal{N}(0, \sigma^2)$，其中 $r_n = y_n - \boldsymbol{w}^\top \boldsymbol{x}_n$。在这种情况下，最大化似然等价于最小化残差平方和，正如我们之前所见。然而，如果数据中存在异常值，这可能会导致拟合效果不佳，如图11.19(a)所示。（异常值是图底部的点。）这是因为平方误差对偏差进行二次惩罚，因此远离直线的点对拟合的影响比靠近直线的点更大。

实现鲁棒性的一种方法是使用具有重尾的分布替换响应变量的高斯分布。这样的分布会给异常值分配更高的似然，而无需扰动直线来“解释”它们。下面我们将讨论几种可能的响应变量备选概率分布；总结见表11.2。

#### 11.6.1 Laplace 似然

在第2.7.3节中，我们注意到 Laplace 分布对异常值也具有鲁棒性。如果我们将此分布用作回归的观测模型，则得到以下似然：

$$  p(y|\boldsymbol{x},\boldsymbol{w},b)=\mathrm{Laplace}(y|\boldsymbol{w}^{\mathrm{T}}\boldsymbol{x},b)\propto\exp(-\frac{1}{b}|y-\boldsymbol{w}^{\mathrm{T}}\boldsymbol{x}|)   \tag*{(11.108)}$$

鲁棒性源于使用 $|y - \boldsymbol{w}^\top \boldsymbol{x}|$ 而非 $(y - \boldsymbol{w}^\top \boldsymbol{x})^2$。图11.19(a)给出了该方法的一个实际示例。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>似然</td><td style='text-align: center; word-wrap: break-word;'>先验</td><td style='text-align: center; word-wrap: break-word;'>后验</td><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>章节</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高斯</td><td style='text-align: center; word-wrap: break-word;'>均匀</td><td style='text-align: center; word-wrap: break-word;'>点估计</td><td style='text-align: center; word-wrap: break-word;'>最小二乘</td><td style='text-align: center; word-wrap: break-word;'>11.2.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>学生</td><td style='text-align: center; word-wrap: break-word;'>均匀</td><td style='text-align: center; word-wrap: break-word;'>点估计</td><td style='text-align: center; word-wrap: break-word;'>稳健回归</td><td style='text-align: center; word-wrap: break-word;'>11.6.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>拉普拉斯</td><td style='text-align: center; word-wrap: break-word;'>均匀</td><td style='text-align: center; word-wrap: break-word;'>点估计</td><td style='text-align: center; word-wrap: break-word;'>稳健回归</td><td style='text-align: center; word-wrap: break-word;'>11.6.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高斯</td><td style='text-align: center; word-wrap: break-word;'>高斯</td><td style='text-align: center; word-wrap: break-word;'>点估计</td><td style='text-align: center; word-wrap: break-word;'>岭回归</td><td style='text-align: center; word-wrap: break-word;'>11.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高斯</td><td style='text-align: center; word-wrap: break-word;'>拉普拉斯</td><td style='text-align: center; word-wrap: break-word;'>点估计</td><td style='text-align: center; word-wrap: break-word;'>套索</td><td style='text-align: center; word-wrap: break-word;'>11.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高斯</td><td style='text-align: center; word-wrap: break-word;'>高斯-伽马</td><td style='text-align: center; word-wrap: break-word;'>高斯-伽马</td><td style='text-align: center; word-wrap: break-word;'>贝叶斯线性回归</td><td style='text-align: center; word-wrap: break-word;'>11.7</td></tr></table>

<div style="text-align: center;">表11.2：用于线性回归的各种似然、先验和后验的总结。似然指的是 $ p(y|\mathbf{x},\mathbf{w},\sigma^{2}) $ 的分布形式，先验指的是 $ p(\mathbf{w}) $ 的分布形式。后验指的是 $ p(\mathbf{w}|\mathcal{D}) $ 的分布形式。“点估计”表示退化分布 $ \delta(\mathbf{w}-\hat{\mathbf{w}}) $，其中 $ \hat{\mathbf{w}} $ 是MAP估计。MLE等价于使用点后验和均匀先验。</div>

##### 11.6.1.1 使用线性规划计算MLE

我们可以使用线性规划来计算该模型的MLE。正如我们在第8.5.3节中所解释的，这是一种求解如下形式的约束优化问题的方法：

$$  \underset{v}{\operatorname{a r g m i n}}c^{\top}v\quad s.t.\quad\mathbf{A}v\leq b   \tag*{(11.109)}$$

其中 $ \boldsymbol{v} \in \mathbb{R}^n $ 是 $ n $ 个未知参数的集合， $ \boldsymbol{c}^T \boldsymbol{v} $ 是我们想要最小化的线性目标函数， $ \boldsymbol{a}_i^\top \boldsymbol{v} \leq b_i $ 是一组必须满足的 $ m $ 个线性约束。为了将其应用于我们的问题，定义 $ \boldsymbol{v} = (w_1, \ldots, w_D, e_1, \ldots, e_N) \in \mathbb{R}^{D+N} $，其中 $ e_i = |y_i - \hat{y}_i| $ 是样本 $ i $ 的残差误差。我们希望最小化残差之和，因此定义 $ \boldsymbol{c} = (0, \cdots, 0, 1, \cdots, 1) \in \mathbb{R}^{D+N} $，其中前 $ D $ 个元素为 $ 0 $，后 $ N $ 个元素为 $ 1 $。

我们需要强制约束 $ e_i = |\hat{y}_i - y_i| $。实际上，强制约束 $ |\boldsymbol{w}^\top \boldsymbol{x}_i - y_i| \leq e_i $ 就足够了，因为最小化 $ e_i $ 的和会“压紧”该约束使其满足等式。由于 $ |a| \leq b \implies -b \leq a \leq b $，我们可以将 $ |\boldsymbol{w}^\top \boldsymbol{x}_i - y_i| \leq e_i $ 编码为两个线性约束：

$$  e_{i}\geq\boldsymbol{w}^{\top}\boldsymbol{x}_{i}-y_{i}   \tag*{(11.110)}$$

$$  e_{i}\geq-(w^{\top}x_{i}-y_{i})   \tag*{(11.111)}$$

我们可以将方程(11.110)写为

$$  \left(\boldsymbol{x}_{i},0,\cdots,0,-1,0,\cdots,0\right)^{\top}\boldsymbol{v}\leq y_{i}   \tag*{(11.112)}$$

其中前 $ D $ 个条目填充 $ \mathbf{x}_{i} $，而 $-1$ 位于向量的第 $(D+i)$ 个条目。类似地，我们可以将方程(11.111)写为

$$  \left(-\boldsymbol{x}_{i},0,\cdots,0,-1,0,\cdots,0\right)^{\top}\boldsymbol{v}\leq-y_{i}   \tag*{(11.113)}$$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可协议

---

我们可以将这些约束写成 $\mathbf{A}\mathbf{v} \leq \mathbf{b}$ 的形式，通过如下定义 $\mathbf{A} \in \mathbb{R}^{2N \times (N+D)}$：

$$  \mathbf{A}=\begin{pmatrix}{{{x_{1}}}}&{{{-1}}}&{{{0}}}&{{{0\cdots}}}&{{{0}}} \\{{{-x_{1}}}}&{{{-1}}}&{{{0}}}&{{{0\cdots}}}&{{{0}}} \\{{{x_{2}}}}&{{{0}}}&{{{-1}}}&{{{0\cdots}}}&{{{0}}} \\{{{-x_{2}}}}&{{{0}}}&{{{-1}}}&{{{0\cdots}}}&{{{0}}} \\\end{pmatrix}   \tag*{(11.114)}$$

并定义 $b \in \mathbb{R}^{2N}$ 为

$$  \boldsymbol{b}=\left(y_{1},-y_{1},y_{2},-y_{2},\cdots,y_{N},-y_{N}\right)   \tag*{(11.115)}$$

#### 11.6.2 Student-t 似然

在 2.7.1 节中，我们讨论了 Student 分布的稳健性特性。为了将其用于回归问题，我们可以像 [Zel76] 中提出的那样，将均值设为输入的线性函数：

$$  p(y|\boldsymbol{x},\boldsymbol{w},\sigma^{2},\nu)=\mathcal{T}(y|\boldsymbol{w}^{\top}\boldsymbol{x},\sigma^{2},\nu)   \tag*{(11.116)}$$

我们可以使用 SGD 或 EM 来拟合该模型（详见 [Mur23]）。

#### 11.6.3 Huber 损失

使用 Laplace 或 Student 似然来最小化 NLL 的另一种方法是使用 Huber 损失，其定义如下：

$$  \ell_{\mathrm{h u b e r}}(r,\delta)=\left\{\begin{matrix}r^{2}/2&\mathrm{i f}|r|\leq\delta\\ \delta|r|-\delta^{2}/2&\mathrm{i f}|r|>\delta\end{matrix}\right.   \tag*{(11.117)}$$

对于小于 $\delta$ 的误差，这等价于 $\ell_{2}$；对于更大的误差，等价于 $\ell_{1}$。参见 Figure 5.3。

该损失函数的优点在于它处处可微。因此，优化 Huber 损失比使用 Laplace 似然要快得多，因为我们可以使用标准的平滑优化方法（如 SGD）而不是线性规划。Figure 11.19 展示了 Huber 损失函数在实际中的应用。结果在定性上与 Laplace 和 Student 方法相似。

参数 $\delta$ 控制稳健性程度，通常手动设置或通过交叉验证设置。然而，[Bar19] 展示了如何近似 Huber 损失，从而可以通过梯度方法优化 $\delta$。

#### 11.6.4 RANSAC

在计算机视觉领域，一种常见的稳健回归方法是使用 RANSAC，即“随机抽样一致”（random sample consensus）[FB81]。其工作原理如下：我们采样一小部分初始点，对其拟合模型，识别相对于该模型的离群点（基于较大的残差），移除

---

我们将剔除异常值，然后仅对内点重新拟合模型。我们对多个随机初始集重复此过程，并选择最佳模型。

RANSAC的一个确定性替代方案是以下迭代方案：初始时我们假设所有数据点都是内点，并拟合模型计算 $\hat{w}_0$；然后在每次迭代 $t$ 中，我们将残差较大的点识别为异常点，将其移除，并基于剩余点重新拟合模型得到 $\hat{w}_{t+1}$。尽管这种硬阈值方案使问题非凸，但在一些合理假设下，可以证明该简单方案能快速收敛到最优估计 [Muk+19; Sug+19]。

### 11.7 贝叶斯线性回归 *

我们已经看到如何在各种先验下计算线性回归模型的 MLE 和 MAP 估计。本节我们将讨论如何计算参数的后验分布 $p(\boldsymbol{\theta}|\mathcal{D})$。为简化起见，我们假设方差已知，因此只需计算 $p(\boldsymbol{w}|\mathcal{D},\sigma^2)$。更一般的情况请参见本系列著作 [Mur23]。

#### 11.7.1 先验

为简化，我们使用高斯先验：

$$ p(\boldsymbol{w})=\mathcal{N}(\boldsymbol{w}|\check{\boldsymbol{w}},\check{\boldsymbol{\Sigma}}) \tag*{(11.118)}$$

这是岭回归中使用的先验（第 11.3 节）的一个小推广。其他先验的讨论请参见本系列著作 [Mur23]。

#### 11.7.2 后验

我们可以将似然函数重写为 MVN 形式：

$$ p(\mathcal{D}|\boldsymbol{w},\sigma^{2})=\prod_{n=1}^{N}p(y_{n}|\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x},\sigma^{2})=\mathcal{N}(\boldsymbol{y}|\mathbf{X}\boldsymbol{w},\sigma^{2}\mathbf{I}_{N}) \tag*{(11.119)}$$

其中 $\mathbf{I}_N$ 是 $N \times N$ 单位矩阵。然后我们利用高斯分布的贝叶斯公式（方程 (3.37)）推导后验，结果如下：

$$ p(w|\mathbf{X},y,\sigma^{2})\propto\mathcal{N}(w|\breve{w},\breve{\Sigma})\mathcal{N}(y|\mathbf{X}w,\sigma^{2}\mathbf{I}_{N})=\mathcal{N}(w|\hat{w},\hat{\Sigma}) \tag*{(11.120)}$$

$$ \hat{\boldsymbol{w}}\triangleq\hat{\boldsymbol{\Sigma}}(\breve{\boldsymbol{\Sigma}}^{-1}\breve{\boldsymbol{w}}+\frac{1}{\sigma^{2}}\mathbf{X}^{\mathsf{T}}\boldsymbol{y}) \tag*{(11.121)}$$

$$ \hat{\mathbf{\Sigma}}\triangleq(\breve{\mathbf{\Sigma}}^{-1}+\frac{1}{\sigma^{2}}\mathbf{X}^{\mathsf{T}}\mathbf{X})^{-1} \tag*{(11.122)}$$

其中 $\hat{\boldsymbol{w}}$ 是后验均值，$\hat{\mathbf{\Sigma}}$ 是后验协方差。

如果 $\breve{\mathbf{w}} = \mathbf{0}$ 且 $\breve{\mathbf{\Sigma}} = \tau^2 \mathbf{I}$，那么后验均值变为 $\widehat{\mathbf{w}} = \frac{1}{\sigma^2} \widehat{\mathbf{\Sigma}} \mathbf{X}^\top \mathbf{y}$。若定义 $\lambda = \frac{\sigma^2}{\tau^2}$，我们得到岭回归估计 $\widehat{\mathbf{w}} = (\lambda \mathbf{I} + \mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$，这与方程 (11.57) 一致。

作者：Kevin P. Murphy。 (C) 麻省理工学院出版社。遵循 CC-BY-NC-ND 许可协议。

---

#### 11.7.3 示例

假设我们有一个形如 $ f(x; \boldsymbol{w}) = w_0 + w_1 x_1 $ 的一维回归模型，其中真实参数为 $ w_0 = -0.3 $ 和 $ w_1 = 0.5 $。现在我们执行推断 $ p(\boldsymbol{w}|\mathcal{D}) $，并随着训练集大小 $ N $ 的增加，可视化二维先验和后验。

特别地，在图 11.20（该书封面设计的灵感来源）中，我们绘制了似然、后验以及后验预测分布的一个近似。$ ^{4} $ 每一行描绘了当我们增加训练数据量 N 时这些分布的变化。我们现在解释每一行：

● 在第一行中，N = 0，因此后验与先验相同。在这种情况下，我们的预测“分散各处”，因为先验本质上是均匀的。

- 在第二行中，$N = 1$，因此我们看到了一个数据点（第三列图中的蓝色圆圈）。我们的后验受到相应似然的约束，预测结果接近观测数据。然而，我们看到后验呈脊状形状，反映了存在许多可能的解，具有不同的斜率/截距。这很合理，因为我们无法从一个观测中唯一地推断出两个参数（$w_0$ 和 $w_1$）。

- 在第三行中，N = 2。在这种情况下，后验变得窄得多，因为似然提供了两个约束。我们对未来的预测现在都更接近训练数据。

● 在第四行（最后一行），$ N = 100 $。现在后验基本上是一个 delta 函数，中心位于真实值 $ \boldsymbol{w}_* $ = (-0.3, 0.5) 处，第一列和第二列的图中用白色十字标记。预测中的变化源于大小为 $ \sigma^2 $ 的固有高斯噪声。

这个例子说明，随着数据量的增加，后验均值估计 $ \hat{\mu} = \mathbb{E} \left[ \mathbf{w} | \mathcal{D} \right] $ 收敛到生成数据的真实值 $ \mathbf{w}_* $。因此我们说贝叶斯估计是一个一致估计量（详见第 5.3.2 节）。我们还看到后验不确定性随时间减小。这就是我们所指的，随着看到更多数据而“学习”参数的含义。

#### 11.7.4 计算后验预测

我们已经讨论了如何计算对模型参数 $ p(\boldsymbol{w}|\mathcal{D}) $ 的不确定性。但关于未来输出的预测的不确定性呢？利用公式 (3.38)，我们可以证明在测试点 $ \boldsymbol{x} $ 处的后验预测分布也是高斯的：

$$  \begin{align*}p(y|\boldsymbol{x},\mathcal{D},\sigma^{2})&=\int\mathcal{N}(y|\boldsymbol{x}^{\top}\boldsymbol{w},\sigma^{2})\mathcal{N}(\boldsymbol{w}|\hat{\boldsymbol{\mu}},\hat{\boldsymbol{\Sigma}})d\boldsymbol{w}\\&=\mathcal{N}(y|\hat{\boldsymbol{\mu}}^{\top}\boldsymbol{x},\hat{\sigma}^{2}(\boldsymbol{x}))\end{align*}   \tag*{(11.123)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_376_121_794_545.jpg" alt="图像" width="36%" /></div>


<div style="text-align: center;">图 11.20: 线性回归模型 $ p(y|w_0) = \mathcal{N}(y|w_0 + w_1|x_1, \sigma^2) $ 参数的序贯贝叶斯推断。左列：当前数据点的似然函数。中列：给定前 N 个数据点后的后验分布 $ p(w_0, w_1 | \mathbf{x}_{1:N}, y_{1:N}, \sigma^2) $。右列：当前后验预测分布中的样本。第 1 行：先验分布 $ (N = 0) $。第 2 行：1 个数据点之后。第 3 行：2 个数据点之后。第 4 行：100 个数据点之后。第 1 列和第 2 列中的白色交叉表示真实参数值；我们可以看到后验的众数迅速收敛到该点。第 3 列中的蓝色圆圈是观测到的数据点。改编自 [Bis06] 的图 3.7。由 $ \text{linreg}_2d\_bayes\_demo.ipynb $ 生成。</div>


其中 $ \hat{\sigma}^2(\boldsymbol{x}) \triangleq \sigma^2 + \boldsymbol{x}^\top \hat{\boldsymbol{\Sigma}} \boldsymbol{x} $ 是观测到 $ N $ 个训练样本后，在点 $ \boldsymbol{x} $ 处的后验预测分布的方差。预测方差取决于两个项：观测噪声的方差 $ \sigma^2 $ 和参数的方差 $ \hat{\boldsymbol{\Sigma}} $。后者通过依赖于 $ \boldsymbol{x} $ 与训练数据 $ \mathcal{D} $ 接近程度的方式，转化为观测值的方差。如图 11.21(b) 所示，我们注意到随着远离训练点，误差条会变大，表示不确定性增加。这对于某些应用（如主动学习，需选择收集训练数据的位置）可能非常重要（见第 19.4 节）。

在某些情况下，计算参数后验 $ p(\pmb{w}|\mathcal{D}) $ 在计算上难以处理。此时，我们可以选择使用点估计 $ \hat{\pmb{w}} $，然后采用插件近似。这给出

$$  p(y|\boldsymbol{x},\mathcal{D},\sigma^{2})=\int\mathcal{N}(y|\boldsymbol{x}^{\mathsf{T}}\boldsymbol{w},\sigma^{2})\delta(\boldsymbol{w}-\hat{\boldsymbol{w}})d\boldsymbol{w}=p(y|\boldsymbol{x}^{\mathsf{T}}\hat{\boldsymbol{w}},\sigma^{2}).   \tag*{(11.125)}$$

我们看到后验预测方差是常数，与数据无关，如图 11.21(a) 所示。如果从此后验中采样一个参数，我们总会得到一个单一的函数，如图 11.21(c) 所示。相比之下，如果从真实后验 $ \boldsymbol{w}_s \sim p(\boldsymbol{w}|\mathcal{D}, \sigma^2) $ 中采样，我们将得到一系列不同的函数，如图 11.21(d) 所示，这更准确地反映了我们的不确定性。

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_239_130_516_334.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_645_130_923_334.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_239_378_517_575.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_644_376_924_575.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 11.21: (a) 在将二次多项式拟合至一维数据时，预测密度的插件近似（我们将参数的极大似然估计代入）。(b) 后验预测密度，通过对参数积分得到。黑色曲线为后验均值，误差条为后验预测密度的2个标准差。(c) 后验预测分布的插件近似的10个样本。(d) 真实后验预测分布的10个样本。由 $ \text{linreg\_post\_pred\_plot.ipynb} $ 生成。</div>


#### 11.7.5 中心化的优势

敏锐的读者可能会注意到，图 11.20 中二维后验的形状是一个拉长的椭圆（最终会随着 $ N \to \infty $ 收缩为一个点）。这意味着两个参数之间存在很强的后验相关性，这可能导致计算上的困难。

要理解其原因，注意每个数据点都会引出一个似然函数，对应一条经过该数据点的直线。当我们将所有数据放在一起观察时，我们看到似然最大的预测必须对应于经过数据均值 $ (\overline{x}, \overline{y}) $ 的直线。存在许多这样的直线，但如果增加斜率，就必须减小截距。因此，我们可以将高概率直线的集合视为围绕数据均值旋转，像一个命运之轮。$ ^{5} $ 这种 $ w_{0} $ 和 $ w_{1} $ 之间的相关性正是后验呈现对角线形式的原因。（高斯先验将其转化为拉长的椭圆，但后验相关性仍然存在，直到样本量足够大，后验收缩为一个点为止。）

计算这种拉长的后验分布可能很困难。一个简单的解决方案是对输入数据进行中心化，即使用 $ x_n' = x_n - \overline{x} $。此时直线可以围绕原点旋转，从而减少后验

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_217_118_546_336.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_625_118_953_335.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 11.22：一维线性回归模型 $ p(y|x, \boldsymbol{\theta}) = \mathcal{N}(y|w_0 + w_1x, \sigma^2) $ 在 Gaussian 先验下的 $ p(w_0, w_1|\mathcal{D}) $ 的后验样本。(a) 原始数据。(b) 中心化数据。由 $ \text{linreg}_{2d\_bayes\_centering\_pymc3.ipymb} $ 生成。</div>

$ w_{0} $ 与 $ w_{1} $ 之间的相关性。参见图 11.22 的示例。（我们也可以选择将每个 $ x_{n} $ 除以该特征的标准差，如第 10.2.8 节所述。）

请注意，我们可以将通过拟合中心化数据得到的后验转换回原始坐标，具体方法是：

$$  y^{\prime}=w_{0}^{\prime}+w_{1}^{\prime}x^{\prime}=w_{0}^{\prime}+w_{1}^{\prime}(x-\overline{x})=(w_{0}^{\prime}-w_{1}^{\prime}\overline{x})+w_{1}^{\prime}x   \tag*{(11.126)}$$

因此，非中心化数据上的参数为 $ w_0 = w_0' - w_1'\overline{x} $ 和 $ w_1 = w_1' $。

#### 11.7.6 处理多重共线性

在许多数据集中，输入变量之间可能存在高度相关性。同时包含所有变量通常不会损害预测准确性（前提是使用合适的先验或正则化来防止过拟合），但会使系数的解释变得更加困难。

为了说明这一点，我们使用 [McE20, 第 6.1 节] 中的一个玩具示例。假设我们有一个包含 $N$ 个人的数据集，记录了他们的身高 $h_i$，以及左腿长度 $l_i$ 和右腿长度 $r_i$。假设 $h_i \sim \mathcal{N}(10,2)$，因此平均身高为 $\bar{h} = 10$（单位未指定）。假设腿长是身高的一定比例 $\rho_i \sim \text{Unif}(0.4,0.5)$，外加少量 Gaussian 噪声，具体地，$l_i \sim \mathcal{N}(\rho_i h_i,0.02)$ 和 $r_i \sim \mathcal{N}(\rho_i h_i,0.02)$。

现在假设我们希望根据腿长测量值预测一个人的身高。（我说过这是一个玩具示例！）由于左右腿都是未知量的带噪声测量值，同时使用两者是有益的。因此，我们使用线性回归拟合 $ p(h|l,r) = \mathcal{N}(h|\alpha + \beta_l l + \beta_r r, \sigma^2) $。我们使用模糊先验：$ \alpha, \beta_l, \beta_r \sim \mathcal{N}(0, 100) $，以及 $ \sigma \sim \text{Expon}(1) $。

由于平均腿长为 $ l = 0.45h = 4.5 $，我们可能会预期每个 $ \beta $ 系数大约为 $ \overline{h}/\overline{l} = 10/4.5 = 2.2 $。然而，图 11.23 中显示的后验边缘分布却呈现出不同的情况：我们看到 $ \beta_l $ 的后验均值接近 2.6，但 $ \beta_r $ 的后验均值接近 -0.6。因此，右腿特征似乎是不必要的。这是因为，如第 11.2.2.1 节所讨论的，特征 $ j $ 的回归系数编码了在已知其他所有特征 $ \boldsymbol{x}_{-j} $ 的情况下知道 $ x_j $ 的价值。如果我们已经知道左腿，那么知道右腿的边际价值很小。然而，如果我们

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_315_116_858_360.jpg" alt="图像" width="47%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">图11.23: 多腿示例中参数的后验边缘分布。由multi_collinear_legs_numpyro.ipynb生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_480_516_679.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_636_471_942_684.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图11.24: 多腿示例的后验分布。(a) 联合后验  $ p(\beta_l, \beta_r | \mathcal{D}) $ (b)  $ p(\beta_l + \beta_r | \text{data}) $ 的后验。由multi_collinear_legs_numpyro.ipynb生成。</div>


如果使用略有不同的数据重新运行此示例，我们可能会得出相反的结论，并偏好右腿而非左腿。

通过查看图11.24a所示的联合分布 $ p(\beta_l, \beta_r | \mathcal{D}) $，我们可以获得更多见解。我们观察到参数之间高度相关，因此如果 $ \beta_r $ 较大，则 $ \beta_l $ 较小，反之亦然。每个参数的边缘分布并未捕捉到这一点。然而，它确实表明每个参数存在很大的不确定性，表明它们是不可识别的。但它们的和是确定的，如图11.24b所示，我们绘制了 $ p(\beta_l + \beta_r | \mathcal{D}) $，该分布以2.2为中心，正如我们所预期的那样。

这个例子表明，我们在尝试解释模型中单个系数估计的显著性时必须谨慎，因为它们在孤立情况下意义不大。

#### 11.7.7 自动相关性确定 (ARD) $ ^{*} $

考虑一个具有已知观测噪声但未知回归权重的线性回归模型： $ \mathcal{N}(y|\mathbf{X}w,\sigma^2\mathbf{I}) $。假设我们对权重使用高斯先验： $ w_j \sim \mathcal{N}(0,1/\alpha_j) $，其中 $ \alpha_j $ 是

---

第j个参数的精度。现在我们假设按照以下方式估计先验精度：

$$  \hat{\alpha}=\underset{\alpha}{\operatorname{argmax}}p(\boldsymbol{y}|\mathbf{X},\boldsymbol{\alpha})   \tag*{(11.127)}$$

其中

$$  p(\boldsymbol{y}|\mathbf{X},\boldsymbol{\alpha})=\int p(\boldsymbol{y}|\mathbf{X}\boldsymbol{w},\sigma^{2})p(\boldsymbol{w}|\mathbf{0},\mathrm{diag}(\boldsymbol{\alpha})^{-1})d\boldsymbol{w}   \tag*{(11.128)}$$

是边际似然。这是一个经验贝叶斯的例子，因为我们是从数据中估计先验。我们可以将其视为完全贝叶斯方法的一种计算捷径。然而，它还有额外优势。特别地，假设在估计出$\alpha$之后，我们计算MAP估计

$$  \hat{w}=\underset{w}{\operatorname{argmax}}\mathcal{N}(w|\mathbf{0},\hat{\alpha}^{-1})   \tag*{(11.129)}$$

这将得到$\hat{w}$的稀疏估计，这或许令人惊讶，因为w的高斯先验并非稀疏促进的。其原因将在本书后续部分解释。

该技术被称为**稀疏贝叶斯学习**[Tip01]或**自动相关性确定** (ARD) [Mac95; Nea96]。它最初是为神经网络开发的（其中稀疏性应用于第一层权重），但此处我们将其应用于线性模型。另请参见第17.4.1节，我们将其应用于核化线性模型。

### 11.8 练习

练习11.1 [多输出线性回归 †]

（来源：Jaakkola。）

考虑一个具有二维响应向量$\mathbf{y}_i \in \mathbb{R}^2$的线性回归模型。假设我们有部分二值输入数据$x_i \in \{0,1\}$。训练数据如下：

 $$ \begin{array}{c|c}{{{\bf{x}}}}&{{{\bf{y}}}} \\{{{\hline0}}}&{{{(-1,-1)^{T}}}} \\{{{0}}}&{{{(-1,-2)^{T}}}} \\{{{0}}}&{{{(-2,-1)^{T}}}} \\{{{1}}}&{{{(1,1)^{T}}}} \\{{{1}}}&{{{(1,2)^{T}}}} \\{{{1}}}&{{{(2,1)^{T}}}}\end{array} $$ 

让我们使用以下基函数将每个$x_{i}$嵌入到二维空间中：

$$  \phi(0)=(1,0)^{T},\ \phi(1)=(0,1)^{T}   \tag*{(11.130)}$$

模型变为

$$  \hat{\boldsymbol{y}}=\mathbf{W}^{T}\boldsymbol{\phi}(\boldsymbol{x})   \tag*{(11.131)}$$

其中W是一个$2 \times 2$矩阵。根据上述数据计算W的MLE。

练习11.2 [数据中心化与岭回归]

假设$\overline{x}=0$，即输入数据已被中心化。证明以下优化目标的最优解

$$  J(\boldsymbol{w},w_{0})=(\boldsymbol{y}-\mathbf{X}\boldsymbol{w}-w_{0}\mathbf{1})^{T}(\boldsymbol{y}-\mathbf{X}\boldsymbol{w}-w_{0}\mathbf{1})+\lambda\boldsymbol{w}^{T}\boldsymbol{w}   \tag*{(11.132)}$$

作者：Kevin P. Murphy。（C）MIT出版社。CC-BY-NC-ND许可。

---

$$  \hat{w}_{0}=\overline{y}   \tag*{(11.133)}$$

$$  \boldsymbol{w}=(\mathbf{X}^{T}\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^{T}\boldsymbol{y}   \tag*{(11.134)}$$

练习 11.3 [RSS 的偏导数 $ \dagger $]

令 $ RSS(w) = ||Xw - y||_2^2 $ 为残差平方和。

 $$ \frac{\partial}{\partial w_{k}}R S S(\boldsymbol{w})=a_{k}w_{k}-c_{k} $$ 

a. 证明

$$  a_{k}=2\sum_{i=1}^{n}x_{ik}^{2}=2||\boldsymbol{x}_{:,k}||^{2}   \tag*{(11.136)}$$

$$  c_{k}=2\sum_{i=1}^{n}x_{ik}(y_{i}-\boldsymbol{w}_{-k}^{T}\boldsymbol{x}_{i,-k})=2\boldsymbol{x}_{:,k}^{T}\boldsymbol{r}_{k}   \tag*{(11.137)}$$

其中 $ \boldsymbol{w}_{-k} $ 是去除了第 $ k $ 个分量的 $ \boldsymbol{w} $，$ \boldsymbol{x}_{i,-k} $ 是去除了第 $ k $ 个分量的 $ \boldsymbol{x}_{i} $，而 $ \boldsymbol{r}_{k} = \boldsymbol{y} - \boldsymbol{w}_{-k}^{T} \boldsymbol{x}_{:,-k} $ 是使用除特征 $ k $ 之外的所有特征得到的残差。提示：将权重分为涉及 $ k $ 的部分和不涉及 $ k $ 的部分。

b. 证明若 $ \frac{\partial}{\partial w_{k}}RSS(\boldsymbol{w})=0 $，则

$$  \hat{w}_{k}=\frac{\boldsymbol{x}_{:,k}^{T}\boldsymbol{r}_{k}}{\left\|\boldsymbol{x}_{:,k}\right\|^{2}}   \tag*{(11.138)}$$

因此，当我们顺序添加特征时，特征 k 的最优权重通过计算 $ \boldsymbol{x}_{:,k} $ 在当前残差上的正交投影来得到。

##### 练习 11.4 [将弹性网络化简为 Lasso]

定义

$$  J_{1}(w)=\|y-\mathbf{X}w\|^{2}+\lambda_{2}\|w\|_{2}^{2}+\lambda_{1}\|w\|_{1}   \tag*{(11.139)}$$

以及

$$  J_{2}(w)=\|\tilde{y}-\tilde{\mathbf{X}}w\|^{2}+c\lambda_{1}\|w\|_{1}   \tag*{(11.140)}$$

其中 $ \|w\|^2 = \|w\|_2^2 = \sum_i w_i^2 $ 是平方 2-范数，$ \|w\|_1 = \sum_i |w_i| $ 是 1-范数，$ c = (1 + \lambda_2)^{-\frac{1}{2}} $，并且

$$  \tilde{\mathbf{X}}=c\begin{pmatrix}\mathbf{X}\\ \sqrt{\lambda}_{2}\mathbf{I}_{d}\end{pmatrix},\quad\tilde{\mathbf{y}}=\begin{pmatrix}\mathbf{y}\\ \mathbf{0}_{d\times1}\end{pmatrix}   \tag*{(11.141)}$$

证明

$$  \operatorname{a r g m i n}J_{1}(\boldsymbol{w})=c(\operatorname{a r g m i n}J_{2}(\boldsymbol{w}))   \tag*{(11.142)}$$

即

$$  J_{1}(c w)=J_{2}(w)   \tag*{(11.143)}$$

从而表明可以通过在修改后的数据上使用 Lasso 求解器来解决弹性网络问题。

---

##### 练习 11.5 [线性回归中的收缩 †]

（来源：Jaakkola。）考虑使用正交设计矩阵进行线性回归，使得每个列（特征）$k$ 有 $\| \boldsymbol{x}_{:,k} \|_2^2 = 1$，并且 $\boldsymbol{x}_{:,k}^T \boldsymbol{x}_{:,j} = 0$，因此我们可以分别估计每个参数 $w_k$。

图 10.15b 绘制了 $\hat{w}_k$ 与 $c_k = 2\mathbf{y}^T\mathbf{x}_{:,k}$（特征 $k$ 与响应变量的相关性）之间的关系，针对三种不同的估计方法：普通最小二乘法（OLS）、参数为 $\lambda_2$ 的岭回归和参数为 $\lambda_1$ 的套索。

a. 不幸的是我们忘记给图添加标签。实线（1）、点线（2）和虚线（3）分别对应哪种方法？

b. $\lambda_{1}$ 的值是多少？

c. $\lambda_{2}$ 的值是多少？

##### 练习 11.6 [混合线性回归专家的 EM 算法]

推导拟合混合线性回归专家的 EM 方程。

---

请提供需要翻译的英文学术论文Markdown文本。

---

### 12.1 引言

在第10章中，我们讨论了逻辑回归，在二分类情况下，该模型对应于 $ p(y|\boldsymbol{x},\boldsymbol{w})=\mathrm{Ber}(y|\sigma(\boldsymbol{w}^{\top}\boldsymbol{x})) $。在第11章中，我们讨论了线性回归，该模型对应于 $ p(y|\boldsymbol{x},\boldsymbol{w})=\mathcal{N}(y|\boldsymbol{w}^{\top}\boldsymbol{x},\sigma^{2}) $。这两种模型显然非常相似。特别是，输出的均值 $ \mathbb{E}[y|\boldsymbol{x},\boldsymbol{w}] $ 在两种情况下都是输入 $ \boldsymbol{x} $ 的线性函数。

事实上，存在一大类具有此性质的模型，称为**广义线性模型**（generalized linear models, GLMs）[MN89]。

GLM 是指数族分布（第3.4节）的条件版本，其中自然参数是输入的线性函数。更准确地说，该模型具有以下形式：

$$  p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w},\sigma^{2})=\exp\left[\frac{y_{n}\eta_{n}-A(\eta_{n})}{\sigma^{2}}+\log h(y_{n},\sigma^{2})\right]   \tag*{(12.1)}$$

其中 $ \eta_n \triangleq \boldsymbol{w}^\top \boldsymbol{x}_n $ 是（依赖于输入的）自然参数，$ A(\eta_n) $ 是对数归一化因子，$ \mathcal{T}(y) = y $ 是充分统计量，$ \sigma^2 $ 是散度项。$ ^1 $

我们用 $ \mu_n = \ell^{-1}(\eta_n) $ 表示从线性输入到输出均值的映射，其中函数 $ \ell $ 称为**连接函数**（link function），$ \ell^{-1} $ 称为**均值函数**（mean function）。

基于第3.4.3节的结果，我们可以证明响应变量的均值和方差如下：

$$  \mathbb{E}\left[y_{n}|\boldsymbol{x}_{n},\boldsymbol{w},\sigma^{2}\right]=A^{\prime}(\eta_{n})\triangleq\ell^{-1}(\eta_{n})   \tag*{(12.2)}$$

$$  \mathbb{V}\left[y_{n}|\boldsymbol{x}_{n},\boldsymbol{w},\sigma^{2}\right]=A^{\prime\prime}(\eta_{n})\sigma^{2}   \tag*{(12.3)}$$

### 12.2 示例

本节给出一些广泛使用的 GLM 的示例。

---

#### 12.2.1 线性回归

回顾线性回归的形式如下：

$$  p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w},\sigma^{2})=\frac{1}{\sqrt{2\pi\sigma^{2}}}\exp(-\frac{1}{2\sigma^{2}}(y_{n}-\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}_{n})^{2})   \tag*{(12.4)}$$

因此

$$  \log p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w},\sigma^{2})=-\frac{1}{2\sigma^{2}}(y_{n}-\eta_{n})^{2}-\frac{1}{2}\log(2\pi\sigma^{2})   \tag*{(12.5)}$$

其中 $\eta_n = \boldsymbol{w}^\top \boldsymbol{x}_n$。我们可以将其写成如下 GLM 形式：

$$  \log p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w},\sigma^{2})=\frac{y_{n}\eta_{n}-\frac{\eta_{n}^{2}}{2}}{\sigma^{2}}-\frac{1}{2}\left(\frac{y_{n}^{2}}{\sigma^{2}}+\log(2\pi\sigma^{2})\right)   \tag*{(12.6)}$$

我们看到 $A(\eta_{n})=\eta_{n}^{2}/2$，因此

$$  \mathbb{E}\left[y_{n}\right]=\eta_{n}=w^{\top}x_{n}   \tag*{(12.7)}$$

$$  \mathbb{V}\left[y_{n}\right]=\sigma^{2}   \tag*{(12.8)}$$

#### 12.2.2 二项式回归

若响应变量是 $N_n$ 次试验中的成功次数，即 $y_n \in \{0, \ldots, N_n\}$，则我们可以使用二项式回归，其定义为

$$  p(y_{n}|\boldsymbol{x}_{n},N_{n},\boldsymbol{w})=\mathrm{Bin}(y_{n}|\sigma(\boldsymbol{w}^{\top}\boldsymbol{x}_{n}),N_{n})   \tag*{(12.9)}$$

我们看到，当 $N_n=1$ 时，二值逻辑回归是其特例。

对数概率密度函数为

$$  \log p(y_{n}|\boldsymbol{x}_{n},N_{n},\boldsymbol{w})=y_{n}\log\mu_{n}+(N_{n}-y_{n})\log(1-\mu_{n})+\log\binom{N_{n}}{y_{n}}   \tag*{(12.10)}$$

$$  =y_{n}\log(\frac{\mu_{n}}{1-\mu_{n}})+N_{n}\log(1-\mu_{n})+\log\binom{N_{n}}{y_{n}}   \tag*{(12.11)}$$

其中 $\mu_{n}=\sigma(\eta_{n})$。为了将其重写为 GLM 形式，我们定义

$$  \eta_{n}\triangleq\log\left[\frac{\mu_{n}}{\left(1-\mu_{n}\right)}\right]=\log\left[\frac{1}{1+e^{-w^{\top}\boldsymbol{x}_{n}}}\frac{1+e^{-w^{\top}\boldsymbol{x}_{n}}}{e^{-w^{\top}\boldsymbol{x}_{n}}}\right]=\log\frac{1}{e^{-w^{\top}\boldsymbol{x}_{n}}}=\boldsymbol{w}^{\top}\boldsymbol{x}_{n}   \tag*{(12.12)}$$

因此我们可以将二项式回归写成如下 GLM 形式

$$  \log p(y_{n}|\boldsymbol{x}_{n},N_{n},\boldsymbol{w})=y_{n}\eta_{n}-A(\eta_{n})+h(y_{n})   \tag*{(12.13)}$$

其中 $h(y_{n})=\log\binom{N_{n}}{y_{n}}$ 且

$$  A(\eta_{n})=-N_{n}\log(1-\mu_{n})=N_{n}\log(1+e^{\eta_{n}})   \tag*{(12.14)}$$

---

因此

$$  \mathbb{E}\left[y_{n}\right]=\frac{d A}{d\eta_{n}}=\frac{N_{n}e^{\eta_{n}}}{1+e^{\eta_{n}}}=\frac{N_{n}}{1+e^{-\eta_{n}}}=N_{n}\mu_{n}   \tag*{(12.15)}$$

以及

$$  \mathbb{V}\left[y_{n}\right]=\frac{d^{2}A}{d\eta_{n}^{2}}=N_{n}\mu_{n}(1-\mu_{n})   \tag*{(12.16)}$$

#### 12.2.3 泊松回归

如果响应变量是整数计数，$ y_n \in \{0, 1, \ldots\} $，我们可以使用泊松回归，其定义如下

$$  p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w})=\mathrm{Poi}(y_{n}|\exp(\boldsymbol{w}^{\top}\boldsymbol{x}_{n}))   \tag*{(12.17)}$$

其中

$$  \mathrm{P o i}(y|\mu)=e^{-\mu}\frac{\mu^{y}}{y!}   \tag*{(12.18)}$$

是泊松分布。泊松回归广泛应用于生物统计学应用中，其中 $ y_{n} $ 可能代表特定人员或地点的疾病数量，或高通量测序背景下某个基因组位置的读数数量（参见例如 [Kua+09]）。

对数概率密度函数由下式给出

$$  \log p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w})=y_{n}\log\mu_{n}-\mu_{n}-\log(y_{n}!)   \tag*{(12.19)}$$

其中 $ \mu_n = \exp(\boldsymbol{w}^\top \boldsymbol{x}_n) $。因此在广义线性模型形式下，我们有

$$  \log p(y_{n}|\boldsymbol{x}_{n},\boldsymbol{w})=y_{n}\eta_{n}-A(\eta_{n})+h(y_{n})   \tag*{(12.20)}$$

其中 $ \eta_n = \log(\mu_n) = \boldsymbol{w}^\top \boldsymbol{x}_n $，$ A(\eta_n) = \mu_n = e^{\eta_n} $，以及 $ h(y_n) = -\log(y_n!) $。因此

$$  \mathbb{E}\left[y_{n}\right]=\frac{d A}{d\eta_{n}}=e^{\eta_{n}}=\mu_{n}   \tag*{(12.21)}$$

以及

$$  \mathbb{V}\left[y_{n}\right]=\frac{d^{2}A}{d\eta_{n}^{2}}=e^{\eta_{n}}=\mu_{n}   \tag*{(12.22)}$$

### 12.3 具有非规范连接函数的广义线性模型

我们已经看到输出分布的均值参数由 $ \mu = \ell^{-1}(\eta) $ 给出，其中函数 $ \ell $ 是连接函数。该函数有几种选择，我们现在讨论这些选择。

规范连接函数 $\ell$ 满足性质 $\theta = \ell(\mu)$，其中 $\theta$ 是规范（自然）参数。因此

$$  \theta=\ell(\mu)=\ell(\ell^{-1}(\eta))=\eta   \tag*{(12.23)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

目前我们已作出上述假设。例如，对于伯努利分布，典范参数是对数几率 $ \theta = \log(\mu/(1 - \mu)) $，即通过 logit 变换给出

$$  \theta=\ell(\mu)=\mathrm{logit}(\mu)=\log\left(\frac{\mu}{1-\mu}\right)   \tag*{(12.24)}$$

其逆变换是 Sigmoid 或逻辑函数 $ \mu = \sigma(\theta) = 1/(1 + e^{-\theta}) $。

然而，我们可以自由使用其他类型的连接函数。例如，probit 连接函数的形式为

$$  \eta=\ell(\mu)=\Phi^{-1}(\mu)   \tag*{(12.25)}$$

另一种有时用于二元响应的连接函数是互补 log-log 函数

$$  \eta=\ell(\mu)=\log(-\log(1-\mu))   \tag*{(12.26)}$$

该函数常用于以下应用场景：我们观察到事件数为 0（记为 y = 0）或至少一个事件（记为 y = 1），其中事件被认为服从速率为 $ \lambda $ 的泊松分布。设 E 为事件数。泊松假设意味着 $ p(E = 0) = \exp(-\lambda) $，因此

$$  p(y=0)=(1-\mu)=p(E=0)=\exp(-\lambda)   \tag*{(12.27)}$$

从而 $ \lambda = -\log(1 - \mu) $。当 $ \lambda $ 是协变量的函数时，需要确保其为正，因此我们使用 $ \lambda = e^\eta $，进而得到

$$  \eta=\log(\lambda)=\log(-\log(1-\mu))   \tag*{(12.28)}$$

### 12.4 极大似然估计

GLM 的拟合可以使用与逻辑回归类似的方法。特别地，负对数似然具有如下形式（忽略常数项）：

$$   NLL(\boldsymbol{w})=-\log p(\mathcal{D}|\boldsymbol{w})=-\frac{1}{\sigma^{2}}\sum_{n=1}^{N}\ell_{n}   \tag*{(12.29)}$$

其中

$$  \ell_{n}\triangleq\eta_{n}y_{n}-A(\eta_{n})   \tag*{(12.30)}$$

且 $ \eta_{n}=w^{\top}x_{n} $。为简化符号，我们假设 $ \sigma^{2}=1 $。

我们可以按如下方式计算单个项的梯度：

$$  \boldsymbol{g}_{n}\triangleq\frac{\partial\ell_{n}}{\partial\boldsymbol{w}}=\frac{\partial\ell_{n}}{\partial\eta_{n}}\frac{\partial\eta_{n}}{\partial\boldsymbol{w}}=(y_{n}-A^{\prime}(\eta_{n}))\boldsymbol{x}_{n}=(y_{n}-\mu_{n})\boldsymbol{x}_{n}   \tag*{(12.31)}$$

其中 $ \mu_n = f(\boldsymbol{w}^\top \boldsymbol{x}) $，$ f $ 是从典范参数映射到均值参数的逆连接函数。例如，在逻辑回归中，$ f(\eta_n) = \sigma(\eta_n) $，因此我们得到

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_157_119_1013_332.jpg" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 12.1：测试集上保险索赔率的预测。(a) 数据。(b) 常数预测器。(c) 线性回归。(d) 泊松回归。由 poisson\_regression\_insurance.ipynb 生成。</div>


公式 (10.21)。该梯度表达式可以直接用于 SGD 或其他梯度方法中。

 $$ \mathbf{H}=\frac{\partial^{2}}{\partial w\partial w^{\mathsf{T}}}\mathrm{N L L}(\boldsymbol{w})=-\sum_{n=1}^{N}\frac{\partial\boldsymbol{g}_{n}}{\partial\boldsymbol{w}^{\mathsf{T}}} $$ 

Hessian 矩阵由下式给出：

其中

$$  \frac{\partial\boldsymbol{g}_{n}}{\partial\boldsymbol{w}^{\top}}=\frac{\partial\boldsymbol{g}_{n}}{\partial\mu_{n}}\frac{\partial\mu_{n}}{\partial\boldsymbol{w}^{\top}}=-\boldsymbol{x}_{n}f^{\prime}(\boldsymbol{w}^{\top}\boldsymbol{x}_{n})\boldsymbol{x}_{n}^{\top}   \tag*{(12.33)}$$

因此

$$  \mathbf{H}=\sum_{n=1}^{N}f^{\prime}(\eta_{n})\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\top}   \tag*{(12.34)}$$

例如，在逻辑回归中，$ f(\eta_n) = \sigma(\eta_n) $，且 $ f'((\eta_n) = \sigma(\eta_n)(1 - \sigma(\eta_n)) $，由此我们得到公式 (10.23)。一般而言，我们注意到 Hessian 矩阵是正定的，因为 $ f'((\eta_n) > 0 $；因此负对数似然是凸函数，故 GLM 的极大似然估计是唯一的（假设对所有 $ n $ 有 $ f(\eta_n) > 0 $）。

基于上述结果，我们可以使用基于梯度的求解器来拟合 GLM，其方式与拟合逻辑回归模型非常相似。

### 12.5 实例：预测保险索赔

本节中，我们给出一个使用线性回归和泊松回归预测保险索赔的示例。$ ^{2} $ 目标是预测每年因车祸产生的预期保险索赔次数。该数据集包含 678k 个样本，共有 9 个特征，例如驾驶员年龄、车辆年龄、车辆功率等。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>MSE</td><td style='text-align: center; word-wrap: break-word;'>MAE</td><td style='text-align: center; word-wrap: break-word;'>偏差</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Dummy</td><td style='text-align: center; word-wrap: break-word;'>0.564</td><td style='text-align: center; word-wrap: break-word;'>0.189</td><td style='text-align: center; word-wrap: break-word;'>0.625</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Ridge</td><td style='text-align: center; word-wrap: break-word;'>0.560</td><td style='text-align: center; word-wrap: break-word;'>0.177</td><td style='text-align: center; word-wrap: break-word;'>0.601</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Poisson</td><td style='text-align: center; word-wrap: break-word;'>0.560</td><td style='text-align: center; word-wrap: break-word;'>0.186</td><td style='text-align: center; word-wrap: break-word;'>0.594</td></tr></table>

<div style="text-align: center;">表12.1：测试集上的性能指标。MSE = 均方误差。MAE = 平均绝对误差。偏差 = 泊松偏差。</div>

等等。目标是索赔频率，即每份保单的索赔数量除以风险暴露（即保单的年限）。

我们在图12.1(a)中绘制了测试集。可以看到，94%的保单没有发生索赔，因此数据包含大量零值，这与计数数据和率数据的典型特征相符。平均索赔频率为10%。这可以转化为一个始终预测该常数的虚模型，其预测结果如图12.1(b)所示。目标是做得比这更好。

一个简单的方法是使用线性回归，结合一些简单的特征工程（对连续变量进行分箱，对分类变量进行独热编码）。（我们使用了少量 $\ell_{2}$ 正则化，因此严格来说这是岭回归。）这得到了图12.1(c)所示的结果。这比基线更好，但仍然不够理想。特别是，它可能预测出负值，并且无法捕捉长尾分布。

我们可以使用泊松回归做得更好，使用相同的特征但采用对数链接函数。结果如图12.1(d)所示。可以看到预测结果好得多。

一个有趣的问题是如何量化此类问题中的性能。如果使用均方误差或平均绝对误差，从表12.1中可能会得出岭回归优于泊松回归的结论，但这显然不正确，如图12.1所示。相反，更常见的是使用**偏差**来度量性能，其定义为

$$ D(\pmb{y},\hat{\pmb{\mu}})=2\sum_{i}\left(\log p(y_{i}|\mu_{i}^{*})-\log p(y_{i}|\mu_{i})\right)   \tag*{(12.35)}$$

其中 $\mu_i$ 是第 $i$ 个样本的预测参数（基于输入特征 $\boldsymbol{x}_i$ 和训练集 $\mathcal{D}$），而 $\mu_i^*$ 是通过仅拟合真实输出 $y_i$ 来估计的最优参数（这称为饱和模型，完美拟合测试集）。在泊松回归的情况下，有 $\mu_i^* = y_i$。因此

$$ \begin{align*}D(\boldsymbol{y},\boldsymbol{\mu})&=2\sum_{i}\left[(y_{i}\log y_{i}-y_{i}-\log(y_{i}!))-(y_{i}\log\hat{\mu}_{i}-\hat{\mu}_{i}-\log(y_{i}!))\right]\\&=2\sum_{i}\left[(y_{i}\log\frac{y_{i}}{\hat{\mu}_{i}}+\hat{\mu}_{i}-y_{i}\right]\end{align*}   \tag*{(12.37)}$$

根据这一指标，泊松模型显然更好（见表12.1的最后一列）。

我们还可以绘制**校准图**，即实际频率与预测频率的关系图。为了计算该图，我们将预测值分箱，然后统计所有预测频率落入该箱的样本的经验索赔频率。结果如图12.2所示。可以看到常数基线校准良好，但显然精度不高。岭模型在低频区域存在**校准偏差**，特别是它