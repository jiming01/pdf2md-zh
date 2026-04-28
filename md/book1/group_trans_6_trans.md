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

我们可以通过两次调用 f 来数值近似这一结果，无论 n 取何值。相比之下，标准梯度向量的数值近似需要  $ n + 1 $ 次调用（若使用中心差分法则需 2n 次）。

注意，沿 v 的方向导数是梯度 g 与向量 v 的标量积：

$$  D_{v}f(\boldsymbol{x})=\nabla f(\boldsymbol{x})\cdot\boldsymbol{v}   \tag*{(7.246)}$$

#### 7.8.4 全导数 $ * $

假设函数的某些自变量相互依赖。具体来说，假设函数形式为  $ f(t, x(t), y(t)) $。我们定义 $ f $ 关于 $ t $ 的全导数如下：

$$  \frac{df}{dt}=\frac{\partial f}{\partial t}+\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}   \tag*{(7.247)}$$

如果我们将两边乘以微分 dt，则得到全微分

$$  d f=\frac{\partial f}{\partial t}d t+\frac{\partial f}{\partial x}d x+\frac{\partial f}{\partial y}d y   \tag*{(7.248)}$$

这衡量了当我们改变 t 时 f 的变化量，既包括 t 对 f 的直接影响，也包括 t 通过 x 和 y 产生的间接影响。

#### 7.8.5 雅可比矩阵

考虑一个将向量映射到另一个向量的函数  $ f : \mathbb{R}^n \to \mathbb{R}^m $。该函数的雅可比矩阵是一个  $ m \times n $ 的偏导数矩阵：

$$  \mathbf{J}_{f}(\boldsymbol{x})=\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{x}^{\top}}\triangleq\begin{pmatrix}\frac{\partial f_{1}}{\partial x_{1}}&\cdots&\frac{\partial f_{1}}{\partial x_{n}}\\ \vdots&\ddots&\vdots\\ \frac{\partial f_{m}}{\partial x_{1}}&\cdots&\frac{\partial f_{m}}{\partial x_{n}}\end{pmatrix}=\begin{pmatrix}\nabla f_{1}(\boldsymbol{x})^{\top}\\ \vdots\\ \nabla f_{m}(\boldsymbol{x})^{\top}\end{pmatrix}   \tag*{(7.249)}$$

注意，我们按照与输出 $f$ 相同的方向排列结果；这有时被称为分子布局或雅可比公式化。$^{5}$

##### 7.8.5.1 雅可比矩阵与向量的乘法

雅可比向量积（Jacobian vector product，JVP）定义为将雅可比矩阵  $  \mathbf{J} \in \mathbb{R}^{m \times n}  $ 右乘一个向量  $  \mathbf{v} \in \mathbb{R}^n  $ 的运算：

$$  \mathbf{J}_{f}(\boldsymbol{x})\boldsymbol{v}=\begin{pmatrix}\nabla f_{1}(\boldsymbol{x})^{\top}\\ \vdots\\ \nabla f_{m}(\boldsymbol{x})^{\top}\end{pmatrix}\boldsymbol{v}=\begin{pmatrix}\nabla f_{1}(\boldsymbol{x})^{\top}\boldsymbol{v}\\ \vdots\\ \nabla f_{m}(\boldsymbol{x})^{\top}\boldsymbol{v}\end{pmatrix}   \tag*{(7.250)}$$

---

由此可见，我们只需要两次调用 $f$ 即可对其进行数值近似。

向量-雅可比积（VJP）定义为将雅可比矩阵 $\mathbf{J} \in \mathbb{R}^{m \times n}$ 左乘一个向量 $\mathbf{u} \in \mathbb{R}^m$ 的运算：

$$  \boldsymbol{u}^{\mathsf{T}}\boldsymbol{J}_{f}(\boldsymbol{x})=\boldsymbol{u}^{\mathsf{T}}\left(\frac{\partial f}{\partial x_{1}},\cdots,\frac{\partial f}{\partial x_{n}}\right)=\left(\boldsymbol{u}\cdot\frac{\partial f}{\partial x_{1}},\cdots,\boldsymbol{u}\cdot\frac{\partial f}{\partial x_{n}}\right)   \tag*{(7.251)}$$

当 $m \geq n$ 时，JVP 更高效；当 $m \leq n$ 时，VJP 更高效。关于如何利用这一点在计算图（如深度神经网络）中执行自动微分的详细信息，请参见第 13.3 节。

##### 7.8.5.2 复合函数的雅可比矩阵

有时，对两个复合函数求雅可比矩阵很有用。设 $h(\boldsymbol{x}) = g(f(\boldsymbol{x}))$。根据微积分中的链式法则，我们有：

$$  \mathbf{J}_{h}(\boldsymbol{x})=\mathbf{J}_{g}(f(\boldsymbol{x}))\mathbf{J}_{f}(\boldsymbol{x})   \tag*{(7.252)}$$

例如，假设 $f : \mathbb{R} \to \mathbb{R}^2$ 且 $g : \mathbb{R}^2 \to \mathbb{R}^2$。我们有：

$$  \frac{\partial\boldsymbol{g}}{\partial x}=\begin{pmatrix}\frac{\partial}{\partial x}g_{1}(f_{1}(x),f_{2}(x))\\ \frac{\partial}{\partial x}g_{2}(f_{1}(x),f_{2}(x))\end{pmatrix}=\begin{pmatrix}\frac{\partial g_{1}}{\partial f_{1}}\frac{\partial f_{1}}{\partial x}+\frac{\partial g_{1}}{\partial f_{2}}\frac{\partial f_{2}}{\partial x}\\ \frac{\partial g_{2}}{\partial f_{1}}\frac{\partial f_{1}}{\partial x}+\frac{\partial g_{2}}{\partial f_{2}}\frac{\partial f_{2}}{\partial x}\end{pmatrix}   \tag*{(7.253)}$$

$$  =\frac{\partial\boldsymbol{g}}{\partial\boldsymbol{f}^{\mathrm{T}}}\frac{\partial\boldsymbol{f}}{\partial x}=\begin{pmatrix}\frac{\partial g_{1}}{\partial f_{1}}&\frac{\partial g_{1}}{\partial f_{2}}\\\frac{\partial g_{2}}{\partial f_{1}}&\frac{\partial g_{2}}{\partial f_{2}}\end{pmatrix}\begin{pmatrix}\frac{\partial f_{1}}{\partial x}\\\frac{\partial f_{2}}{\partial x}\end{pmatrix}   \tag*{(7.254)}$$

#### 7.8.6 海森矩阵

对于一个二阶可微的函数 $f : \mathbb{R}^n \to \mathbb{R}$，我们将海森矩阵定义为二阶偏导数的（对称）$n \times n$ 矩阵：

$$  \mathbf{H}_{f}=\frac{\partial^{2}f}{\partial\boldsymbol{x}^{2}}=\nabla^{2}f=\begin{pmatrix}\frac{\partial^{2}f}{\partial x_{1}^{2}}&\cdots&\frac{\partial^{2}f}{\partial x_{1}\partial x_{n}}\\ &\vdots&\\ \frac{\partial^{2}f}{\partial x_{n}\partial x_{1}}&\cdots&\frac{\partial^{2}f}{\partial x_{n}^{2}}\end{pmatrix}   \tag*{(7.255)}$$

我们看到，海森矩阵就是梯度的雅可比矩阵。

#### 7.8.7 常用函数的梯度

本节中，我们将不加证明地列出某些广泛使用函数的梯度。

##### 7.8.7.1 标量到标量的函数

考虑一个可微函数 $f: \mathbb{R} \to \mathbb{R}$。以下是标量微积分中的一些有用恒等式，你应该已经熟悉了。

---

$$  \frac{d}{dx}cx^{n}=cnx^{n-1}   \tag*{(7.256)}$$

$$  \frac{d}{dx}\log(x)=1/x   \tag*{(7.257)}$$

$$  \frac{d}{dx}\exp(x)=\exp(x)   \tag*{(7.258)}$$

$$  \frac{d}{dx}\left[f(x)+g(x)\right]=\frac{df(x)}{dx}+\frac{dg(x)}{dx}   \tag*{(7.259)}$$

$$  \frac{d}{dx}\left[f(x)g(x)\right]=f(x)\frac{dg(x)}{dx}+g(x)\frac{df(x)}{dx}   \tag*{(7.260)}$$

$$  \frac{d}{dx}f(u(x))=\frac{du}{dx}\frac{df(u)}{du}   \tag*{(7.261)}$$

方程 (7.261) 被称为微积分中的**链式法则**。

##### 7.8.7.2 向量到标量的映射函数

考虑一个可微函数 $ f : \mathbb{R}^n \to \mathbb{R} $。以下是一些有用的恒等式：$ ^6 $

$$  \frac{\partial(\boldsymbol{a}^{\top}\boldsymbol{x})}{\partial\boldsymbol{x}}=\boldsymbol{a}   \tag*{(7.262)}$$

$$  \frac{\partial(\boldsymbol{b}^{\top}\mathbf{A}\boldsymbol{x})}{\partial\boldsymbol{x}}=\mathbf{A}^{\top}\boldsymbol{b}   \tag*{(7.263)}$$

$$  \frac{\partial(\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x})}{\partial\boldsymbol{x}}=(\mathbf{A}+\mathbf{A}^{\top})\boldsymbol{x}   \tag*{(7.264)}$$

通过展开二次型并应用标量微积分，可以相当容易地证明这些恒等式。

##### 7.8.7.3 矩阵到标量的映射函数

考虑一个将矩阵映射为标量的函数 $ f : \mathbb{R}^{m \times n} \to \mathbb{R} $。我们采用以下自然布局来表示导数矩阵：

$$  \frac{\partial f}{\partial\mathbf{X}}=\begin{pmatrix}\frac{\partial f}{\partial x_{11}}&\cdots&\frac{\partial f}{\partial x_{1n}}\\ &\vdots&\\ \frac{\partial f}{\partial x_{m1}}&\cdots&\frac{\partial f}{\partial x_{mn}}\end{pmatrix}   \tag*{(7.265)}$$

下面是一些有用的恒等式。

---

##### 涉及二次型的恒等式

可以证明以下结果。

$$  \frac{\partial}{\partial\mathbf{X}}(\boldsymbol{a}^{\top}\mathbf{X}\boldsymbol{b})=\boldsymbol{a}\boldsymbol{b}^{\top}   \tag*{(7.266)}$$

$$  \frac{\partial}{\partial\mathbf{X}}(\boldsymbol{a}^{\top}\mathbf{X}^{\top}\boldsymbol{b})=\boldsymbol{b}\boldsymbol{a}^{\top}   \tag*{(7.267)}$$

##### 涉及矩阵迹的恒等式

可以证明以下结果。

$$  \frac{\partial}{\partial\mathbf{X}}\mathrm{tr}(\mathbf{A}\mathbf{X}\mathbf{B})=\mathbf{A}^{\top}\mathbf{B}^{\top}   \tag*{(7.268)}$$

$$  \frac{\partial}{\partial\mathbf{X}}\mathrm{tr}(\mathbf{X}^{\top}\mathbf{A})=\mathbf{A}   \tag*{(7.269)}$$

$$  \frac{\partial}{\partial\mathbf{X}}\mathrm{tr}(\mathbf{X}^{-1}\mathbf{A})=-\mathbf{X}^{-\top}\mathbf{A}^{\top}\mathbf{X}^{-\top}   \tag*{(7.270)}$$

$$  \frac{\partial}{\partial\mathbf{X}}\mathrm{tr}(\mathbf{X}^{\mathsf{T}}\mathbf{A}\mathbf{X})=(\mathbf{A}+\mathbf{A}^{\mathsf{T}})\mathbf{X}   \tag*{(7.271)}$$

##### 涉及矩阵行列式的恒等式

可以证明以下结果。

$$  \frac{\partial}{\partial\mathbf{X}}\det(\mathbf{A}\mathbf{X}\mathbf{B})=\det(\mathbf{A}\mathbf{X}\mathbf{B})\mathbf{X}^{-\top}   \tag*{(7.272)}$$

$$  \frac{\partial}{\partial\mathbf{X}}\log(\det(\mathbf{X}))=\mathbf{X}^{-\mathsf{T}}   \tag*{(7.273)}$$

### 7.9 习题

##### 习题 7.1 [正交矩阵]

a. 绕 z 轴旋转角度 $ \alpha $ 的三维旋转由以下矩阵给出：

$$  \mathbf{R}(\alpha)=\begin{pmatrix}{{{\cos(\alpha)}}}&{{{-\sin(\alpha)}}}&{{{0}}} \\{{{\sin(\alpha)}}}&{{{\cos(\alpha)}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{pmatrix}   \tag*{(7.274)}$$

证明对于任意 $ \alpha $，$ \mathbf{R} $ 是正交矩阵，即 $ \mathbf{R}^T\mathbf{R} = \mathbf{I} $。

b. $ \mathbf{R} $ 的唯一特征向量 $ \boldsymbol{v} $ 是什么，其对应的特征值为 1.0 且具有单位范数（即 $ \|\boldsymbol{v}\|^2 = 1 $）？（你的答案应对于任意 $ \alpha $ 都相同。）提示：考虑特征向量的几何解释。

##### 习题 7.2 [手算特征向量 †]

求以下矩阵的特征值和特征向量：

$$  \boldsymbol{A}=\begin{pmatrix}{{{2}}}&{{{0}}} \\{{{0}}}&{{{3}}}\end{pmatrix}   \tag*{(7.275)}$$

手算你的结果并用 Python 验证。

---

## 8 优化

本章部分内容由 Frederik Kunstner、Si Yi Meng、Aaron Mishkin、Sharan Vaswani 和 Mark Schmidt 撰写。

### 8.1 引言

我们在第 4 章中看到，机器学习的核心问题是参数估计（又称模型拟合）。这需要求解一个优化问题，即找到一组变量 $ \theta \in \Theta $ 的值，使得标量损失函数或代价函数 $ \mathcal{L} : \Theta \to \mathbb{R} $ 最小化：

$$  \theta^{*}\in\operatorname{argmin}_{\theta\in\Theta}\mathcal{L}(\theta)   \tag*{(8.1)}$$

我们假设参数空间为 $ \Theta \subseteq \mathbb{R}^D $，其中 $ D $ 是待优化变量的数量。因此，我们重点关注的是连续优化，而非离散优化。

如果我们要最大化某个得分函数或奖励函数 $ R(\theta) $，则可以等价地最小化 $ \mathcal{L}(\theta) = -R(\theta) $。我们将使用术语“目标函数”泛指需要最大化或最小化的函数。能够找到目标函数最优点的算法通常称为求解器。

在本章剩余部分，我们将针对不同类型的目标函数讨论不同的求解器，重点关注机器学习社区中使用的方法。有关优化的更多详细信息，请参阅一些优秀的教科书，例如 [KW19b; BV04; NW06; Ber15; Ber16] 以及各种综述文章，如 [BCN18; Sun+19b; PPS18; Pey20]。优化算法分类的可视化可参见 https://neos-guide.org/guide/types。

#### 8.1.1 局部优化与全局优化

满足方程 (8.1) 的点称为**全局最优点**。寻找这样的点称为全局优化。

通常，寻找全局最优解在计算上是棘手的 [Neu04]。在这种情况下，我们将只尝试寻找局部最优点。对于连续问题，局部最优点定义为这样一个点 $ \theta^{*} $，其代价低于（或等于）“附近”的点。形式上，如果满足以下条件，则称 $ \theta^{*} $ 为**局部极小值点**：

$$  \exists\delta>0,\forall\theta\in\Theta\text{s.t.}\left|\left|\theta-\theta^{*}\right|<\delta,\mathcal{L}(\theta^{*})\leq\mathcal{L}(\theta)   \tag*{(8.2)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_222_195_539_404.jpg" alt="图片" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_663_149_936_393.jpg" alt="图片" width="23%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 8.1：(a) 一维情况下局部极小值与全局极小值的示意图。由 extrema_fig_1d.ipynb 生成。(b) 二维情况下鞍点的示意图。由 saddle.ipynb 生成。</div>


局部极小值周围可能存在其他具有相同目标函数值的局部极小值，这被称为**平坦局部极小值**。若某点的代价严格低于其邻域内其他点的代价，则该点被称为**严格局部极小值**：

$$  \exists\delta>0,\forall\theta\in\Theta,\theta\neq\theta^{*}:||\theta-\theta^{*}||<\delta,\mathcal{L}(\theta^{*})<\mathcal{L}(\theta)   \tag*{(8.3)}$$

类似地，我们可以定义（严格）局部极大值。参见图 8.1a 的示意图。

最后关于术语的说明：如果一种算法从任何起始点出发都能保证收敛到一个驻点，则称其为**全局收敛**。然而，这（相当令人困惑地）并不意味着它会收敛到全局最优点；它仅意味着会收敛到某个驻点。

##### 8.1.1.1 局部与全局最优点的最优性条件

对于连续且二阶可微的函数，我们可以精确刻画对应于局部极小值的点的特征。令 $ g(\theta) = \nabla \mathcal{L}(\theta) $ 为梯度向量， $ \mathbf{H}(\theta) = \nabla^2 \mathcal{L}(\theta) $ 为海森矩阵（如有必要，可参见第 7.8 节复习相关概念）。考虑点 $ \theta^* \in \mathbb{R}^D $，令 $ g^* = g(\theta) |_{\theta^*} $ 为该点的梯度， $ \mathbf{H}^* = \mathbf{H}(\theta) |_{\theta^*} $ 为对应的海森矩阵。可以证明，以下条件刻画了每一个局部极小值：

- **必要条件**：若 $ \theta^* $ 是局部极小值，则必有 $ g^* = 0 $（即 $ \theta^* $ 必须是驻点），且 $ H^* $ 必须是半正定的。

- **充分条件**：若 $ g^* = 0 $ 且 $ H^* $ 是正定的，则 $ \theta^* $ 是局部最优点。

为了理解为何第一个条件是必要的，假设我们处于某点 $ \theta^* $ 且梯度非零：在这样的点上，我们可以沿负梯度方向移动一小段距离来减小函数值，因此该点不是最优点。所以梯度必须为零。（在非光滑情形下，

---

函数中，必要条件是在最小值处零是局部次梯度。要理解为什么零梯度不充分，需注意驻点可能是局部极小值、极大值或**鞍点**，鞍点处某些方向向下，某些向上（see Figure 8.1b）。更精确地说，在鞍点处，Hessian矩阵的特征值既有正也有负。然而，如果某点处的Hessian矩阵是半正定的，则某些方向可能向上，而其他方向平坦。此外，如果Hessian矩阵是**严格正定**的，则我们处于一个“碗”的底部，所有方向都向上，这足以保证该点是最小值。

#### 8.1.2 约束优化与无约束优化

在无约束优化中，我们将优化任务定义为在参数空间$\Theta$中寻找任何使损失最小化的值。然而，我们通常对允许的数值有一组约束。通常将约束集$\mathcal{C}$划分为不等式约束$g_j(\boldsymbol{\theta}) \leq 0$（$j \in \mathcal{I}$）和等式约束$h_k(\boldsymbol{\theta}) = 0$（$k \in \mathcal{E}$）。例如，我们可以将和为1的约束表示为等式约束$h(\boldsymbol{\theta}) = (1 - \sum_{i=1}^D \theta_i) = 0$，并利用$D$个形如$g_i(\boldsymbol{\theta}) = -\theta_i \leq 0$的不等式约束来表示参数的非负性约束。

我们将**可行集**定义为满足约束的参数空间子集：

$$  \mathcal{C}=\left\{\boldsymbol{\varTheta}:g_{j}(\boldsymbol{\varTheta})\leq0:j\in\mathcal{I},h_{k}(\boldsymbol{\varTheta})=0:k\in\mathcal{E}\right\}\subseteq\mathbb{R}^{D}   \tag*{(8.4)}$$

我们的约束优化问题现在变为：

$$  \theta^{*}\in\operatorname{argmin}_{\theta\in\mathcal{C}}\mathcal{L}(\theta)   \tag*{(8.5)}$$

如果$C = \mathbb{R}^D$，则称为**无约束优化**。

添加约束会改变函数的最优解数量。例如，原本无界（因此没有定义明确的全局最大值或最小值）的函数在添加约束后可能“获得”多个极大值或极小值，如 Figure 8.2 所示。然而，如果添加过多约束，可行集可能变为空集。在可行集中寻找任意点（不考虑其代价）的任务称为**可行性问题**；这本身可能就是一个困难的子问题。

解决约束优化问题的一种常见策略是创建惩罚项来度量每个约束的违反程度。然后将这些项添加到目标函数中，并求解一个无约束优化问题。**拉格朗日函数**就是这种组合目标的一个特例（详见第8.5节）。

#### 8.1.3 凸优化与非凸优化

在**凸优化**中，我们要求目标函数是定义在凸集上的凸函数（下文将定义这些术语）。在这类问题中，每个局部最小值同时也是全局最小值。因此许多模型的设计使其训练目标是凸的。

##### 8.1.3.1 凸集

如果对于任意$x, x' \in S$，有

$$  \lambda\boldsymbol{x}+(1-\lambda)\boldsymbol{x}^{\prime}\in\mathcal{S},\forall\lambda\in[0,1]   \tag*{(8.6)}$$

则称$S$为**凸集**。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_155_122_1006_617.jpg" alt="图像" width="73%" /></div>


<div style="text-align: center;">图 8.2：非凸一维函数受约束最大化的示意图。虚线竖线之间的区域表示可行集。(a) 由于函数在可行集支撑集内是凹的，因此存在唯一全局最大值。(b) 存在两个全局最大值，均出现在可行集的边界上。(c) 在无约束情况下，该函数没有全局最大值，因为它无界。</div>


<div style="text-align: center;">图 8.3：一些凸集和非凸集的示意图。</div>

也就是说，如果我们从 x 到 $x'$ 画一条线，线上的所有点都在该集合内。参见 Figure 8.3 了解凸集和非凸集的一些示例。

##### 8.1.3.2 凸函数

我们称 $f$ 是一个凸函数，如果它的上境图（函数上方的点集，如图 Figure 8.4a 所示）定义了一个凸集。等价地，函数 $f(\boldsymbol{x})$ 称为凸函数，如果它定义在一个凸集上，并且对于任意 $\boldsymbol{x}, \boldsymbol{y} \in \mathcal{S}$ 和任意 $0 \leq \lambda \leq 1$，有

$$  f(\lambda\boldsymbol{x}+(1-\lambda)\boldsymbol{y})\leq\lambda f(\boldsymbol{x})+(1-\lambda)f(\boldsymbol{y})   \tag*{(8.7)}$$

参见 Figure 8.5(a) 了解凸函数的一维示例。如果不等式是严格的，则称该函数为严格凸函数。函数 $f(\boldsymbol{x})$ 是 $\mathbf{concave}$ 如果 $-f(\boldsymbol{x})$ 是凸的，并且是严格 $\mathbf{concave}$ 如果 $-f(\boldsymbol{x})$ 是严格凸的。参见 Figure 8.5(b) 了解一个既非凸也非凹的函数的一维示例。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_262_123_505_335.jpg" alt="图" width="21%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_678_138_911_322.jpg" alt="图" width="20%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图8.4：(a) 函数上境图的示意图。(b) 对于凸函数 $ f(x) $，其**上境图**可以表示为由共轭函数 $ f^{*}(\lambda) = \max_{x} \lambda x - f(x) $ 定义的线性下界所确定的半空间的交集。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_249_476_518_701.jpg" alt="图" width="23%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_657_479_923_699.jpg" alt="图" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图8.5：(a) 凸函数的示意图。可以看到连接 $ (x, f(x)) $ 和 $ (y, f(y)) $ 的弦位于函数之上。(b) 一个既非凸也非凹的函数。A是局部最小值，B是全局最小值。</div>

以下是一些一维凸函数的示例：

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_910_325_1087.jpg" alt="图" width="13%" /></div>

 $$ |x|^{a},a\geq1 $$ 

##### 8.1.3.3 凸函数的刻画

直观上，凸函数的形状像一个碗。正式地，可以证明以下重要结论：

作者：Kevin P. Murphy。© MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_372_131_586_329.jpg" alt="图像" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_591_127_812_322.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_373_371_587_539.jpg" alt="图像" width="18%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_592_370_811_537.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">图 8.6：二次型 $ f(\mathbf{x}) = \mathbf{x}^{\top} \mathbf{A} \mathbf{x} $ 在二维空间中的图像。(a) A 为正定矩阵，因此 f 是凸函数。(b) A 为负定矩阵，因此 f 是凹函数。(c) A 为半正定但奇异，因此 f 是凸函数，但不严格。注意中间高度不变的山谷。(d) A 为不定矩阵，因此 f 既不是凸函数也不是凹函数。曲面中间的驻点是鞍点。源自 [She94] 的图 5。</div>


定理 8.1.1. 假设 $ f : \mathbb{R}^n \to \mathbb{R} $ 在其定义域上二次可微。则 $ f $ 是凸函数当且仅当对于所有 $ \mathbf{x} \in \operatorname{dom}(f) $，$ \mathbf{H} = \nabla^2 f(\mathbf{x}) $ 是半正定矩阵（见第 7.1.5.3 节）。此外，若 $ \mathbf{H} $ 是正定矩阵，则 $ f $ 是严格凸函数。

例如，考虑二次型

$$  f(\boldsymbol{x})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}   \tag*{(8.8)}$$

当 $ \mathbf{A} $ 是半正定矩阵时该函数是凸的，当 $ \mathbf{A} $ 是正定矩阵时是严格凸的。如果 $ \mathbf{A} $ 的特征值符号混合，则它既非凸也非凹。见图 8.6。

##### 8.1.3.4 强凸函数

如果对于 $ f $ 定义域内的所有 $ \boldsymbol{x}, \boldsymbol{y} $，满足下式，则称函数 $ f $ 是参数为 $ m > 0 $ 的强凸函数：

$$  (\nabla f(\boldsymbol{x})-\nabla f(\boldsymbol{y}))^{\top}(\boldsymbol{x}-\boldsymbol{y})\geq m||\boldsymbol{x}-\boldsymbol{y}||_{2}^{2}   \tag*{(8.9)}$$

强凸函数也是严格凸函数，但反之不一定成立。

如果函数 $f$ 是二次连续可微的，那么它是以 $m$ 为参数的强凸函数当且仅当对于定义域内的所有 $\boldsymbol{x}$，有 $\nabla^2 f(\boldsymbol{x}) \succeq m \mathbf{I}$，其中 $\mathbf{I}$ 是单位矩阵，$\nabla^2 f$ 是 Hessian 矩阵，且不等式 $\succeq$ 表示 $\nabla^2 f(\boldsymbol{x}) - m \mathbf{I}$ 是半正定矩阵。这等价于

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_254_130_502_325.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_659_130_910_327.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图8.7：(a) 光滑一维函数。(b) 非光滑一维函数。(在原点处存在不连续。) 由smooth-vs-nonsmooth-1d.ipynb生成。</div>


这等价于要求对于所有 $\boldsymbol{x}$，$\nabla^2 f(\boldsymbol{x})$ 的最小特征值至少为 $m$。如果定义域为实数轴，那么 $\nabla^2 f(x)$ 就是二阶导数 $f''(x)$，因此条件变为 $f''(x) \geq m$。如果 $m = 0$，则意味着Hessian矩阵是半正定的（或者在实数轴情况下，意味着 $f''(x) \geq 0$），这表示函数是凸的，甚至可能是严格凸的，但不是强凸的。

凸函数、严格凸函数和强凸函数之间的区别相当微妙。为了更好地理解这一点，考虑 $f$ 二阶连续可微且定义域为实数轴的情况。那么我们可以将差异刻画如下：

*   $f$ 是凸的当且仅当对所有 $x$ 有 $f''(x) \geq 0$。
*   $f$ 是严格凸的如果对所有 $x$ 有 $f''(x) > 0$（注意：这是充分条件，但不是必要条件）。
*   $f$ 是强凸的当且仅当对所有 $x$ 有 $f''(x) \geq m > 0$。

注意，可以证明函数 $f$ 关于参数 $m$ 强凸当且仅当函数

$$ J(\boldsymbol{x})=f(\boldsymbol{x})-\frac{m}{2}||\boldsymbol{x}||^{2} \tag*{(8.10)}$$

是凸的。

#### 8.1.4 光滑优化与非光滑优化

在光滑优化中，目标函数和约束都是连续可微的。对于光滑函数，我们可以使用Lipschitz常数来量化光滑程度。在一维情形下，Lipschitz常数定义为任意常数 $L \geq 0$，使得对所有实数 $x_1$ 和 $x_2$，有

$$ |f(x_{1})-f(x_{2})|\leq L|x_{1}-x_{2}| \tag*{(8.11)}$$

如图8.8所示：对于给定的常数 $L$，当函数输入变化1个单位时，函数输出的变化不能超过 $L$。这可以通过适当的范数推广到向量输入。

在非光滑优化中，至少在某些点上，目标函数或约束的梯度无定义。参见图8.7中的例子。在某些优化

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_462_116_708_337.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 8.8: 对于 Lipschitz 连续函数 f，存在一个双锥（白色），其顶点可沿 f 的图像移动，使得整个图像始终位于双锥外部。图片来源：https://en.wikipedia.org/wiki/Lipschitz_continuity。经 Wikipedia 作者 Taschee 许可使用。</div>


对于问题，我们可以将目标函数划分为仅包含光滑项的部分和包含非光滑项的部分：

$$  \mathcal{L}(\boldsymbol{\theta})=\mathcal{L}_{s}(\boldsymbol{\theta})+\mathcal{L}_{r}(\boldsymbol{\theta})   \tag*{(8.12)}$$

其中 $ \mathcal{L}_s $ 是光滑的（可微），$ \mathcal{L}_r $ 是非光滑的（“粗糙的”）。这通常被称为复合目标。在机器学习应用中，$ \mathcal{L}_s $ 通常是训练集损失，$ \mathcal{L}_r $ 是正则化项，例如 $ \theta $ 的 $ \ell_1 $ 范数。各种算法可以利用这种复合结构。

##### 8.1.4.1 次梯度

在本节中，我们将导数的概念推广到具有局部不连续性的函数。特别地，对于多元凸函数 $ f : \mathbb{R}^n \to \mathbb{R} $，如果对于所有 $ z \in \text{dom}(f) $ 都有

$$  f(z)\geq f(x)+g^{\top}(z-x)   \tag*{(8.13)}$$

则称 $ g \in \mathbb{R}^n $ 为 $ f $ 在 $ x \in \text{dom}(f) $ 处的次梯度。注意，即使函数 $f$ 在某点不可微，次梯度也可能存在，如图 8.9 所示。如果 $\boldsymbol{x}$ 处至少存在一个次梯度，则称函数 $f$ 在 $\boldsymbol{x}$ 处是次可微的。所有次梯度的集合称为 $f$ 在 $\boldsymbol{x}$ 处的次微分，记作 $\partial f(\boldsymbol{x})$。

例如，考虑绝对值函数 $ f(x) = |x| $。其次微分为

$$  \partial f(x)=\left\{\begin{array}{ll}\left\{-1\right\}&\text{if }x<0\\ \left[-1,1\right]&\text{if }x=0\\ \left\{+1\right\}&\text{if }x>0\end{array}\right.   \tag*{(8.14)}$$

其中记号 $ [-1,1] $ 表示 -1 到 1 之间的任意值（含端点）。图 8.10 给出了图示。

### 8.2 一阶方法

在本节中，我们考虑利用目标函数的一阶导数（即计算哪些方向是“下坡”方向，但忽略曲率信息）的迭代优化方法。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_208_158_968_394.jpg" alt="Image" width="65%" /></div>

<div style="text-align: center;">图8.9：次梯度的图示。在 $ \mathbf{x}_{1} $ 处，凸函数 $ f $ 是可微的，$ \mathbf{g}_{1} $（即 $ f $ 在 $ \mathbf{x}_{1} $ 处的导数）是 $ \mathbf{x}_{1} $ 处唯一的次梯度。在点 $ \mathbf{x}_{2} $ 处，由于存在“拐点”，$ f $ 不可微。然而，该点处存在多个次梯度，图中展示了其中两个。来源：https://web.stanford.edu/class/ee364b/lectures/subgradients_slides.pdf。经Stephen Boyd友好许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_183_577_992_829.jpg" alt="Image" width="70%" /></div>

<div style="text-align: center;">图8.10：绝对值函数（左）及其次微分（右）。来源：https://web.stanford.edu/class/ee364b/lectures/subgradients_slides.pdf。经Stephen Boyd友好许可使用。</div>

信息。所有这些算法都要求用户指定一个起始点 $ \theta_0 $。然后在每次迭代 $ t $ 中，它们执行如下形式的更新：

$$  \boldsymbol{\theta}_{t+1}=\boldsymbol{\theta}_{t}+\boldsymbol{\eta}_{t}\boldsymbol{d}_{t}   \tag*{(8.15)}$$

其中 $ \eta_t $ 被称为步长或学习率，$ d_t $ 是下降方向，例如由 $ g_t = \nabla_\theta \mathcal{L}(\theta) |_{\theta_t} $ 给出的负梯度方向。这些更新步骤持续进行，直到方法达到一个驻点（梯度为零）。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 8.2.1 下降方向

我们说方向 $d$ 是一个下降方向，如果存在一个足够小（但非零）的量 $\eta$，我们沿着方向 $d$ 移动该量，并且能保证函数值减小。形式上，我们要求存在一个 $\eta_{\max} > 0$，使得对于所有 $0 < \eta < \eta_{\max}$ 都有

$$  \mathcal{L}(\boldsymbol{\theta}+\eta\boldsymbol{d})<\mathcal{L}(\boldsymbol{\theta})   \tag*{(8.16)}$$

当前迭代点 $\theta_t$ 处的梯度由下式给出

$$  g_{t}\triangleq\nabla\mathcal{L}(\boldsymbol{\theta})|_{\boldsymbol{\theta}_{t}}=\nabla\mathcal{L}(\boldsymbol{\theta}_{t})=g(\boldsymbol{\theta}_{t})   \tag*{(8.17)}$$

该梯度指向 $f$ 的最大增加方向，因此负梯度是一个下降方向。可以证明，任何方向 $d$ 也构成下降方向，如果 $d$ 与 $-g_t$ 之间的夹角 $\theta$ 小于90度，且满足

$$  \boldsymbol{d}^{\top}\boldsymbol{g}_{t}=||\boldsymbol{d}||~||\boldsymbol{g}_{t}||~\cos(\theta)<0   \tag*{(8.18)}$$

似乎最佳选择是取 $d_t = -g_t$。这被称为最速下降方向。然而，这种方法可能非常缓慢。我们将在后面考虑更快的版本。

#### 8.2.2 步长（学习率）

在机器学习中，步长序列 $\{\eta_t\}$ 被称为学习率调度。存在几种广泛使用的方法来选择它，我们将在下面讨论其中一些。（另见第8.4.3节，其中我们讨论了随机优化的调度。）

##### 8.2.2.1 恒定步长

最简单的方法是使用恒定步长 $\eta_t = \eta$。然而，如果步长太大，该方法可能无法收敛；如果步长太小，该方法会收敛但非常缓慢。

例如，考虑凸函数

$$  \mathcal{L}(\boldsymbol{\theta})=0.5(\theta_{1}^{2}-\theta_{2})^{2}+0.5(\theta_{1}-1)^{2}   \tag*{(8.19)}$$

让我们选择下降方向 $\boldsymbol{d}_t = -\boldsymbol{g}_t$。Figure 8.11 展示了从 $(0,0)$ 出发，使用该下降方向并采用固定步长时发生的情况。在 Figure 8.11(a) 中，我们使用小步长 $\eta = 0.1$；我们看到迭代点沿着山谷缓慢移动。在 Figure 8.11(b) 中，我们使用较大步长 $\eta = 0.6$；我们看到迭代点开始在山谷两侧上下振荡，并且从未收敛到最优点，尽管这是一个凸问题。

在某些情况下，我们可以推导出可使用的最大步长的理论上界。例如，考虑二次目标函数 $\mathcal{L}(\boldsymbol{\theta}) = \frac{1}{2} \boldsymbol{\theta}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\theta} + \boldsymbol{b}^{\mathrm{T}} \boldsymbol{\theta} + c$，其中 $\mathbf{A} \succeq \mathbf{0}$。可以证明，最速下降法将全局收敛当且仅当步长满足

$$  \eta<\frac{2}{\lambda_{max}(\mathbf{A})}   \tag*{(8.20)}$$

其中 $\lambda_{\max}(\mathbf{A})$ 是 $\mathbf{A}$ 的最大特征值。直观原因可以通过想象一个球滚下山谷来理解：我们希望确保它不会迈出比最陡方向坡度更大的步伐，而最大特征值度量的正是这一点（参见第3.2.2节）。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_207_133_551_375.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_615_134_960_374.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 8.11: 在简单凸函数上使用最速下降法，从 $(0,0)$ 出发，步长固定，共 20 步。全局最小值位于 $(1,1)$。 $(a)$ $\eta = 0.1$。 $(b)$ $\eta = 0.6$。由 steepestDescentDemo.ipynb 生成。</div>


更一般地，设置 $\eta < 2/L$（其中 $L$ 是梯度的利普希茨常数，参见第 8.1.4 节）可以保证收敛。由于该常数通常未知，我们往往需要自适应调整步长，下文将对此进行讨论。

##### 8.2.2.2 线搜索

最优步长可通过求解以下一维最小化问题来确定，即找到沿选定方向使目标函数下降最大的值：

$$  \eta_{t}=\underset{\eta>0}{\operatorname{argmin}}\phi_{t}(\eta)=\underset{\eta>0}{\operatorname{argmin}}\mathcal{L}(\boldsymbol{\theta}_{t}+\eta\boldsymbol{d}_{t})   \tag*{(8.21)}$$

该方法被称为线搜索，因为我们是在由 $d$ 定义的直线上进行搜索。

若损失函数是凸的，则此子问题也是凸的，因为对于固定的 $\pmb{\theta}_t$ 和 $\pmb{d}_t$，$\phi_t(\eta) = \mathcal{L}(\pmb{\theta}_t + \eta \pmb{d}_t)$ 是 $\eta$ 的一个仿射函数的凸函数。例如，考虑二次损失：

$$  \mathcal{L}(\boldsymbol{\theta})=\frac{1}{2}\boldsymbol{\theta}^{\mathrm{T}}\mathbf{A}\boldsymbol{\theta}+\boldsymbol{b}^{\mathrm{T}}\boldsymbol{\theta}+c   \tag*{(8.22)}$$

计算 $\phi$ 的导数得到：

$$  \frac{d\phi(\eta)}{d\eta}=\frac{d}{d\eta}\left[\frac{1}{2}(\boldsymbol{\theta}+\eta\boldsymbol{d})^{\top}\mathbf{A}(\boldsymbol{\theta}+\eta\boldsymbol{d})+\boldsymbol{b}^{\top}(\boldsymbol{\theta}+\eta\boldsymbol{d})+c\right]   \tag*{(8.23)}$$

$$  \begin{aligned}&=d^{\intercal}\mathbf{A}(\boldsymbol{\theta}+\boldsymbol{\eta}d)+d^{\intercal}\mathbf{b}\\&=d^{\intercal}(\mathbf{A}\boldsymbol{\theta}+\mathbf{b})+\boldsymbol{\eta}d^{\intercal}\mathbf{A}d\end{aligned}   \tag*{(8.24)}$$

求解 $\frac{d\phi(\eta)}{d\eta}=0$ 得到：

$$  \eta=-\frac{d^{\mathrm{T}}(\mathbf{A}\boldsymbol{\theta}+\mathbf{b})}{d^{\mathrm{T}}\mathbf{A}d}   \tag*{(8.26)}$$

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可证。

---

使用最优步长被称为精确线搜索。然而，通常并不需要如此精确。有几种方法，例如Armijo回溯法，试图在确保目标函数充分下降的同时，避免花费过多时间求解方程(8.21)。具体而言，我们可以从当前步长（或某个最大值）开始，然后每次迭代将其缩小一个因子 0 < c < 1，直到满足以下条件，即Armijo-Goldstein检验：

$$  \mathcal{L}(\boldsymbol{\theta}_{t}+\eta\boldsymbol{d}_{t})\leq\mathcal{L}(\boldsymbol{\theta}_{t})+c\eta\boldsymbol{d}_{t}^{\intercal}\nabla\mathcal{L}(\boldsymbol{\theta}_{t})   \tag*{(8.27)}$$

其中 $ c \in [0,1] $ 是一个常数，通常取 $ c = 10^{-4} $。在实践中，线搜索的初始化方式以及回溯策略会显著影响性能。详见[NW06, Sec 3.1]。

#### 8.2.3 收敛率

我们希望找到能够快速收敛到（局部）最优解的优化算法。对于某些凸问题，若梯度的Lipschitz常数有界，可以证明梯度下降以**线性速率**收敛。这意味着存在一个数 $ 0 < \mu < 1 $ 使得

$$  |\mathcal{L}(\boldsymbol{\theta}_{t+1})-\mathcal{L}(\boldsymbol{\theta}_{*})|\leq\mu|\mathcal{L}(\boldsymbol{\theta}_{t})-\mathcal{L}(\boldsymbol{\theta}_{*})|   \tag*{(8.28)}$$

这里 $ \mu $ 称为收敛率。

对于一些简单问题，我们可以显式推导收敛率。例如，考虑二次目标函数 $ \mathcal{L}(\boldsymbol{\theta}) = \frac{1}{2} \boldsymbol{\theta}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{\theta} + \boldsymbol{b}^{\mathrm{T}} \boldsymbol{\theta} + c $，其中 $ \mathbf{A} \succ 0 $。假设我们使用精确线搜索的最速下降法。可以证明（例如见[Ber15]），收敛率由下式给出：

$$  \mu=\left(\frac{\lambda_{\max}-\lambda_{\min}}{\lambda_{\max}+\lambda_{\min}}\right)^{2}   \tag*{(8.29)}$$

其中 $ \lambda_{\max} $ 是 $ \mathbf{A} $ 的最大特征值，$ \lambda_{\min} $ 是最小特征值。我们可以将其重写为 $ \mu = \left(\frac{\kappa-1}{\kappa+1}\right)^2 $，其中 $ \kappa = \frac{\lambda_{\max}}{\lambda_{\min}} $ 是 $ \mathbf{A} $ 的**条件数**。直观上，条件数衡量了空间的“倾斜”程度，即远离对称“碗状”的程度。（关于条件数的更多信息，参见第7.1.4.4节。）

图8.12展示了条件数对收敛率的影响。左图展示了 $ \mathbf{A} = [20, 5; 5, 2] $，$ \mathbf{b} = [-14; -6] $，$ c = 10 $ 的示例，此时 $ \kappa(\mathbf{A}) = 30.234 $。右图展示了 $ \mathbf{A} = [20, 5; 5, 16] $，$ \mathbf{b} = [-14; -6] $，$ c = 10 $ 的示例，此时 $ \kappa(\mathbf{A}) = 1.8541 $。可以看出，当条件数较小时，最速下降法的收敛速度快得多。

在更一般的非二次函数情形下，目标函数在局部最优点附近通常近似为二次函数。因此，收敛率取决于该点处Hessian矩阵 $ \mathbf{H} $ 的条件数 $ \kappa(\mathbf{H}) $。我们常常可以通过在每一步优化一个替代目标（或模型）来改善收敛速度，该替代目标的Hessian矩阵接近目标函数的Hessian矩阵，正如我们在第8.3节中讨论的那样。

尽管线搜索效果良好，但从图8.12中可以看出，精确线搜索的最速下降路径呈现出典型的锯齿形行为，效率低下。这一问题可以通过称为共轭梯度下降的方法（例如见[She94]）来克服。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_221_123_539_334.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_631_125_948_334.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 8.12: 条件数 $ \kappa $ 对精确线搜索最速下降收敛速度影响的示意图。(a) $ \kappa $ 较大。(b) $ \kappa $ 较小。由 lineSearchConditionNum.ipynb 生成。</div>


#### 8.2.4 动量方法

正如我们在 Figure 8.11 中所示，梯度下降在损失平面的平坦区域可能移动得非常缓慢。下面我们将讨论一些解决方法。

##### 8.2.4.1 动量

一个简单的启发式方法，称为重球法或动量方法 [Ber99]，其思想是沿着过去梯度较好的方向加速移动，而在梯度突然改变的方向上减速，就像球滚下山坡一样。具体实现如下：

$$  \boldsymbol{m}_{t}=\beta\boldsymbol{m}_{t-1}+\boldsymbol{g}_{t-1}   \tag*{(8.30)}$$

$$  \boldsymbol{\theta}_{t}=\boldsymbol{\theta}_{t-1}-\boldsymbol{\eta}_{t}\boldsymbol{m}_{t}   \tag*{(8.31)}$$

其中 $ m_t $ 是动量（质量乘以速度），且 $ 0 < \beta < 1 $。典型的 $ \beta $ 值为 0.9。当 $ \beta = 0 $ 时，该方法退化为梯度下降。

我们看到 $ m_t $ 类似于过去梯度的指数加权移动平均（参见第 4.4.2.2 节）：

$$  \boldsymbol{m}_{t}=\beta\boldsymbol{m}_{t-1}+\boldsymbol{g}_{t-1}=\beta^{2}\boldsymbol{m}_{t-2}+\beta\boldsymbol{g}_{t-2}+\boldsymbol{g}_{t-1}=\cdots=\sum_{\tau=0}^{t-1}\beta^{\tau}\boldsymbol{g}_{t-\tau-1}   \tag*{(8.32)}$$

如果所有过去的梯度都是一个常数，比如 g，则简化为：

$$  m_{t}=g\sum_{\tau=0}^{t-1}\beta^{\tau}   \tag*{(8.33)}$$

缩放因子是一个几何级数，其无穷和由下式给出：

$$  1+\beta+\beta^{2}+\cdots=\sum_{i=0}^{\infty}\beta^{i}=\frac{1}{1-\beta}   \tag*{(8.34)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_395_125_764_402.jpg" alt="Image" width="32%" /></div>


<div style="text-align: center;">图8.13：Nesterov更新的示意图。改编自[Gér19]的图11.6。</div>


因此，在极限情况下，我们将梯度乘以 $ 1/(1-\beta) $。例如，如果 $ \beta = 0.9 $，我们将梯度放大10倍。

由于我们使用梯度平均值 $ \pmb{m}_{t-1} $ 而非仅最近梯度 $ \pmb{g}_{t-1} $ 来更新参数，因此过去的梯度会对当前产生一定影响。此外，当动量与第8.4节中讨论的SGD结合时，我们将看到它可以模拟更大小批量（minibatch）的效果，而无需额外的计算成本。

##### 8.2.4.2 Nesterov动量

标准动量方法的一个问题是，它在谷底可能无法充分减速，从而导致振荡。[Nes04]提出的Nesterov加速梯度方法则通过引入外推步骤来修改梯度下降，如下所示：

$$  \tilde{\boldsymbol{\theta}}_{t+1}=\boldsymbol{\theta}_{t}+\boldsymbol{\beta}(\boldsymbol{\theta}_{t}-\boldsymbol{\theta}_{t-1})   \tag*{(8.35)}$$

$$  \boldsymbol{\theta}_{t+1}=\tilde{\boldsymbol{\theta}}_{t+1}-\boldsymbol{\eta}_{t}\nabla\mathcal{L}(\tilde{\boldsymbol{\theta}}_{t+1})   \tag*{(8.36)}$$

这实质上是一种“向前看”的单步形式，可以减少振荡量，如图8.13所示。

Nesterov加速梯度也可以重写为标准动量的形式。在这种情况下，动量项使用预测新位置处的梯度进行更新，

$$  \pmb{m}_{t+1}=\beta\pmb{m}_{t}-\eta_{t}\nabla\mathcal{L}(\pmb{\theta}_{t}+\beta\pmb{m}_{t})   \tag*{(8.37)}$$

$$  \theta_{t+1}=\theta_{t}+m_{t+1}   \tag*{(8.38)}$$

这解释了为什么Nesterov加速梯度方法有时被称为Nesterov动量。同时也说明了该方法为何比标准动量更快：动量向量已经大致指向正确的方向，因此在新位置 $ \boldsymbol{\theta}_{t} + \beta \boldsymbol{m}_{t} $（而非当前位置 $ \boldsymbol{\theta}_{t} $）处测量梯度，可以获得更高的准确性。

当 $ \beta $ 和 $ \eta_{t} $ 选择适当时，Nesterov加速梯度方法在凸函数上被证明比最速下降法更快。它之所以被称为“加速”，正是由于这种改进。

---

收敛速率，对于仅使用一阶梯度的优化方法而言，在目标函数为凸且具有Lipschitz连续梯度时是最优的。然而，在实际应用中，使用Nesterov动量可能比最速下降法更慢，甚至如果 $\beta$ 或 $\eta_{t}$ 设置不当，还可能导致不稳定。

### 8.3 二阶方法

仅使用梯度的优化算法称为一阶方法。其优势在于梯度计算和存储成本较低，但无法建模空间的曲率，因此可能收敛缓慢，如图8.12所示。二阶优化方法通过多种方式（例如利用Hessian矩阵）引入曲率信息，从而可能实现更快的收敛。下面我们讨论其中一些方法。

#### 8.3.1 牛顿法

经典的二阶方法是牛顿法。其更新形式如下：

$$  \boldsymbol{\theta}_{t+1}=\boldsymbol{\theta}_{t}-\boldsymbol{\eta}_{t}\mathbf{H}_{t}^{-1}\boldsymbol{g}_{t}   \tag*{(8.39)}$$

其中

$$  \mathbf{H}_{t}\triangleq\nabla^{2}\mathcal{L}(\boldsymbol{\theta})|_{\boldsymbol{\theta}_{t}}=\nabla^{2}\mathcal{L}(\boldsymbol{\theta}_{t})=\mathbf{H}(\boldsymbol{\theta}_{t})   \tag*{(8.40)}$$

被假定为正定矩阵，以确保更新过程定义良好。牛顿法的伪代码如算法8.1所示。该方法比梯度下降更快的直观解释是：矩阵逆 $\mathbf{H}^{-1}$ “消除”了局部曲率中的任何扭曲，将类似图8.12a的拓扑结构转换为类似图8.12b的拓扑结构。

算法8.1：用于最小化函数的牛顿法

1 初始化 $\theta_0$

2 for $t = 0, 1, 2, \ldots$ 直到收敛 do

3 $\left\{\begin{array}{l} \text{计算 } g_t = \nabla \mathcal{L}(\theta_t) \\ \text{计算 } \mathbf{H}_t = \nabla^2 \mathcal{L}(\theta_t) \\ \text{解方程 } \mathbf{H}_t \mathbf{d}_t = -\mathbf{g}_t \text{ 得到 } \mathbf{d}_t \\ \text{沿方向 } \mathbf{d}_t \text{ 使用线搜索确定步长 } \eta_t \\ \theta_{t+1} = \theta_t + \eta_t \mathbf{d}_t\end{array}\right. $

该算法可推导如下。考虑在 $\boldsymbol{\theta}_{t}$ 附近对 $\mathcal{L}(\boldsymbol{\theta})$ 进行二阶泰勒级数展开：

$$  \mathcal{L}_{\mathrm{quad}}(\boldsymbol{\theta})=\mathcal{L}(\boldsymbol{\theta}_{t})+\boldsymbol{g}_{t}^{\mathrm{T}}(\boldsymbol{\theta}-\boldsymbol{\theta}_{t})+\frac{1}{2}(\boldsymbol{\theta}-\boldsymbol{\theta}_{t})^{\mathrm{T}}\mathbf{H}_{t}(\boldsymbol{\theta}-\boldsymbol{\theta}_{t})   \tag*{(8.41)}$$

$L_{quad}$ 的最小值位于

$$  \boldsymbol{\theta}=\boldsymbol{\theta}_{t}-\mathbf{H}_{t}^{-1}\boldsymbol{g}_{t}   \tag*{(8.42)}$$

作者：Kevin P. Murphy。（C）MIT出版社。CC-BY-NC-ND许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_257_121_507_336.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_668_125_910_331.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图8.14：牛顿法用于最小化一维函数的示意图。(a) 实线曲线是函数  $ \mathcal{L}(x) $。虚线  $ \mathcal{L}_{\text{quad}}(\theta) $ 是其位于  $ \theta_t $ 处的二阶近似。牛顿步长  $ d_t $ 是需要加到  $ \theta_t $ 上以达到  $ \mathcal{L}_{\text{quad}}(\theta) $ 最小值的量。改编自[Van06]的图13.4。由 newtonsMethodMinQuad.ipynb 生成。(b) 牛顿法应用于非凸函数的示意图。我们在当前点  $ \theta_t $ 附近拟合一个二次函数，并移动到其驻点  $ \theta_{t+1} = \theta_t + d_t $。不幸的是，这将我们带到  $ f $ 的局部最大值附近，而非最小值。这意味着我们需要小心处理二次近似的范围。改编自[Van06]的图13.11。由 newtonsMethodNonConvex.ipynb 生成。</div>


因此，如果二次近似是好的，那么我们应该选择 $ \mathbf{d}_t = -\mathbf{H}_t^{-1} \mathbf{g}_t $ 作为我们的下降方向。见图8.14(a)的示意图。注意，在“纯”牛顿法中，我们使用 $ \eta_t = 1 $ 作为步长。然而，我们也可以使用线搜索来寻找最佳步长；这通常更加稳健，因为使用 $ \eta_t = 1 $ 可能并不总是全局收敛。

如果我们将此方法应用于线性回归，只需一步即可达到最优，因为（如我们在第11.2.2.1节所示）我们有 $ \mathbf{H} = \mathbf{X}^\top \mathbf{X} $ 和 $ g = \mathbf{X}^\top \mathbf{X} w - \mathbf{X}^\top y $，因此牛顿更新变为

$$  w_{1}=w_{0}-\mathbf{H}^{-1}\boldsymbol{g}=w_{0}-(\mathbf{X}^{\top}\mathbf{X})^{-1}(\mathbf{X}^{\top}\mathbf{X}w_{0}-\mathbf{X}^{\top}\boldsymbol{y})=w_{0}-w_{0}+(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}\boldsymbol{y}   \tag*{(8.43)}$$

这正是OLS估计。然而，当我们将此方法应用于逻辑回归时，可能需要多次迭代才能收敛到全局最优，正如我们在第10.2.6节中所讨论的。

#### 8.3.2 BFGS及其他拟牛顿方法

拟牛顿方法，有时称为变度量方法，通过利用每一步梯度向量中获取的信息，迭代地构建对黑塞矩阵的近似。最常见的方法称为BFGS（以其同时的发明者Broyden、Fletcher、Goldfarb和Shanno命名），该方法按如下方式更新对黑塞矩阵 $ \mathbf{B}_t \approx \mathbf{H}_t $ 的近似：

$$  \mathbf{B}_{t+1}=\mathbf{B}_{t}+\frac{\boldsymbol{y}_{t}\boldsymbol{y}_{t}^{\top}}{\boldsymbol{y}_{t}^{\top}\boldsymbol{s}_{t}}-\frac{(\mathbf{B}_{t}\boldsymbol{s}_{t})(\mathbf{B}_{t}\boldsymbol{s}_{t})^{\top}}{\boldsymbol{s}_{t}^{\top}\mathbf{B}_{t}\boldsymbol{s}_{t}}   \tag*{(8.44)}$$

$$  s_{t}=\theta_{t}-\theta_{t-1}   \tag*{(8.45)}$$

$$  y_{t}=g_{t}-g_{t-1}   \tag*{(8.46)}$$

这是对矩阵的秩二更新。如果 $ \mathbf{B}_0 $ 是正定的，并且通过线搜索选择的步长 $ \eta $ 同时满足方程(8.27)中的Armijo条件以及以下曲率条件，则更新有效。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_432_118_737_337.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">图 8.15：信赖域方法示意图。虚线表示原始非凸目标函数的等高线。圆表示逐次二次逼近。源自文献 [Pas14] 的图 4.2。经 Razvan Pascanu 许可使用。</div>


条件

$$  \nabla\mathcal{L}(\boldsymbol{\theta}_{t}+\eta\boldsymbol{d}_{t})\geq c_{2}\eta\boldsymbol{d}_{t}^{\intercal}\nabla\mathcal{L}(\boldsymbol{\theta}_{t})   \tag*{(8.47)}$$

则 $ \mathbf{B}_{t+1} $ 保持正定。常数 $ c_2 $ 选取在 $ (c,1) $ 内，其中 $ c $ 是方程 (8.27) 中的可调参数。这两个步长条件统称为 Wolfe 条件。我们通常从对角近似 $ \mathbf{B}_0 = \mathbf{I} $ 开始。因此，BFGS 可被视为 Hessian 矩阵的**“对角加低秩”近似**。

另外，BFGS 可以迭代更新逆 Hessian 的近似 $ \mathbf{C}_t \approx \mathbf{H}_t^{-1} $，如下所示：

$$  \mathbf{C}_{t+1}=\left(\mathbf{I}-\frac{\boldsymbol{s}_{t}\boldsymbol{y}_{t}^{\top}}{\boldsymbol{y}_{t}^{\top}\boldsymbol{s}_{t}}\right)\mathbf{C}_{t}\left(\mathbf{I}-\frac{\boldsymbol{y}_{t}\boldsymbol{s}_{t}^{\top}}{\boldsymbol{y}_{t}^{\top}\boldsymbol{s}_{t}}\right)+\frac{\boldsymbol{s}_{t}\boldsymbol{s}_{t}^{\top}}{\boldsymbol{y}_{t}^{\top}\boldsymbol{s}_{t}}   \tag*{(8.48)}$$

由于存储 Hessian 近似仍然需要 $ O(D^2) $ 空间，对于非常大的问题，可以使用有限内存 BFGS（L-BFGS），其中我们仅利用最近的 $ M $ 个 $ (s_t, y_t) $ 对来控制近似的秩，并忽略旧信息。我们不显式存储 $ \mathbf{B}_t $，而是将这些向量存入内存，然后通过与存储的 $ s_t $ 和 $ y_t $ 向量进行一系列内积来近似 $ \mathbf{H}_t^{-1} \mathbf{g}_t $。因此存储需求为 $ O(MD) $。通常选取 $ M $ 在 5 到 20 之间即可获得良好性能 [NW06, p177]。

注意，sklearn 默认使用 LBFGS 作为逻辑回归的求解器。$ ^{1} $

#### 8.3.3 信赖域方法

如果目标函数是非凸的，那么 Hessian 矩阵 $ \mathbf{H}_t $ 可能不是正定的，因此 $ \mathbf{d}_t = -\mathbf{H}_t^{-1} \mathbf{g}_t $ 可能不是下降方向。图 8.14(b) 以一维情形展示了这一点，表明牛顿法可能终止于局部最大值而非局部最小值。

一般而言，只要牛顿法所做的二次近似失效，我们就会陷入困境。然而，在当前迭代点周围通常存在一个局部区域，在该区域内我们可以安全地进行逼近。

---

用二次函数来逼近目标函数。我们称这个区域为 $\mathcal{R}_t$，并称 $M(\boldsymbol{\delta})$ 为目标函数的模型（或近似），其中 $\boldsymbol{\delta} = \boldsymbol{\theta} - \boldsymbol{\theta}_t$。于是，在每一步中，我们可以求解

$$  \delta^{*}=\underset{\delta\in\mathcal{R}_{t}}{\operatorname{argmin}}M_{t}(\delta)   \tag*{(8.49)}$$

这被称为信赖域优化。（这可以被视为线搜索的“对立面”，因为它先选定一个要移动的距离（由 $\mathcal{R}_{t}$ 决定），再求解最优方向，而不是先选定方向再求解最优距离。）

通常我们假设 $M_t(\boldsymbol{\delta})$ 是一个二次近似：

$$  M_{t}(\boldsymbol{\delta})=\mathcal{L}(\boldsymbol{\theta}_{t})+\boldsymbol{g}_{t}^{\top}\boldsymbol{\delta}+\frac{1}{2}\boldsymbol{\delta}^{\top}\mathbf{H}_{t}\boldsymbol{\delta}   \tag*{(8.50)}$$

其中 $\boldsymbol{g}_t = \nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta})|_{\boldsymbol{\theta}_t}$ 是梯度，$\mathbf{H}_t = \nabla_{\boldsymbol{\theta}}^2 \mathcal{L}(\boldsymbol{\theta})|_{\boldsymbol{\theta}_t}$ 是海森矩阵。此外，通常假设 $\mathcal{R}_t$ 是半径为 $r$ 的球体，即 $\mathcal{R}_t = \{\boldsymbol{\delta} : ||\boldsymbol{\delta}||_2 \leq r\}$。基于此，我们可以将有约束问题转化为无约束问题，如下所示：

$$  \boldsymbol{\delta}^{*}=\underset{\delta}{\arg\min}M(\boldsymbol{\delta})+\lambda||\boldsymbol{\delta}||_{2}^{2}=\underset{\delta}{\arg\min}\boldsymbol{g}^{\mathrm{T}}\boldsymbol{\delta}+\frac{1}{2}\boldsymbol{\delta}^{\mathrm{T}}(\mathbf{H}+\lambda\mathbf{I})\boldsymbol{\delta}   \tag*{(8.51)}$$

其中 $\lambda > 0$ 是与半径 $r$ 相关的拉格朗日乘子（有关拉格朗日乘子的讨论，请参见第 8.5.1 节）。我们可以通过下式求解：

$$  \delta=-(\mathbf{H}+\lambda\mathbf{I})^{-1}g   \tag*{(8.52)}$$

这被称为 Tikhonov 阻尼或 Tikhonov 正则化。见图 8.15 的图示。

注意到，向 $\mathbf{H}$ 添加充分大的 $\lambda \mathbf{I}$ 可以确保得到的矩阵总是正定的。当 $\lambda \to 0$ 时，该信赖域方法退化为牛顿法；但当 $\lambda$ 足够大时，它会将所有负特征值变为正（并使所有零特征值等于 $\lambda$）。

### 8.4 随机梯度下降

本节我们考虑随机优化，其目标是使函数平均值最小化：

$$  \mathcal{L}(\boldsymbol{\theta})=\mathbb{E}_{q(z)}\left[\mathcal{L}(\boldsymbol{\theta},z)\right]   \tag*{(8.53)}$$

其中 $z$ 是目标函数的随机输入。它可以来自环境的“噪声”项，也可以如我们下文所述，是随机从训练集中抽取的训练样本。

在每次迭代中，我们假设观测到 $\mathcal{L}_t(\boldsymbol{\theta}) = \mathcal{L}(\boldsymbol{\theta}, \boldsymbol{z}_t)$，其中 $\boldsymbol{z}_t \sim q$。我们还假设可以计算 $\mathcal{L}$ 梯度的无偏估计。如果分布 $q(z)$ 与我们正在优化的参数独立，则我们可以使用 $\boldsymbol{g}_t = \nabla_{\boldsymbol{\theta}} \mathcal{L}_t(\boldsymbol{\theta}_t)$。在这种情况下，得到的算法可以写成：

$$  \theta_{t+1}=\theta_{t}-\eta_{t}\nabla\mathcal{L}(\theta_{t},z_{t})=\theta_{t}-\eta_{t}g_{t}   \tag*{(8.54)}$$

这种方法被称为随机梯度下降或 SGD。只要梯度估计是无偏的，并且在以一定速率衰减步长 $\eta_{t}$ 的条件下（我们将在第 8.4.3 节讨论），该方法将收敛到一个驻点。

---

#### 8.4.1 应用于有限和问题

随机梯度下降在机器学习中应用非常广泛。为了理解其原因，回顾第4.3节可知，许多模型拟合过程基于经验风险最小化，即最小化以下损失函数：

$$  \mathcal{L}(\boldsymbol{\theta}_{t})=\frac{1}{N}\sum_{n=1}^{N}\ell(\boldsymbol{y}_{n},f(\boldsymbol{x}_{n};\boldsymbol{\theta}_{t}))=\frac{1}{N}\sum_{n=1}^{N}\mathcal{L}_{n}(\boldsymbol{\theta}_{t})   \tag*{(8.55)}$$

这被称为有限和问题。该目标的梯度形式为

$$  \boldsymbol{g}_{t}=\frac{1}{N}\sum_{n=1}^{N}\nabla_{\theta}\mathcal{L}_{n}(\boldsymbol{\theta}_{t})=\frac{1}{N}\sum_{n=1}^{N}\nabla_{\theta}\ell(\boldsymbol{y}_{n},f(\boldsymbol{x}_{n};\boldsymbol{\theta}_{t}))   \tag*{(8.56)}$$

这需要对所有 $N$ 个训练样本求和，因此当 $N$ 很大时计算可能很慢。幸运的是，我们可以通过采样一个大小为 $B \ll N$ 的小批量来近似，得到

$$  \boldsymbol{g}_{t}\approx\frac{1}{\left|\mathcal{B}_{t}\right|}\sum_{n\in\mathcal{B}_{t}}\nabla_{\theta}\mathcal{L}_{n}(\boldsymbol{\theta}_{t})=\frac{1}{\left|\mathcal{B}_{t}\right|}\sum_{n\in\mathcal{B}_{t}}\nabla_{\theta}\ell(\boldsymbol{y}_{n},f(\boldsymbol{x}_{n};\boldsymbol{\theta}_{t}))   \tag*{(8.57)}$$

其中 $\mathcal{B}_{t}$ 是在迭代 $t$ 时随机选取的一组样本 $^{2}$。这是对式（8.56）中经验平均的无偏近似。因此，我们可以安全地将其用于SGD。

尽管SGD的理论收敛速度比批量GD慢（特别地，SGD具有次线性收敛速度），但在实践中SGD往往更快，因为每步的计算开销要低得多 [BB08; BB11]。为了理解为什么SGD能比全批量GD更快地取得进展，假设我们有一个数据集，其中包含单个样本重复K次。批量训练至少比SGD慢K倍，因为它会浪费时间计算重复样本的梯度。即使没有重复样本，批量训练也可能是浪费的，因为在训练早期，参数估计尚不准确，因此不值得仔细计算梯度。

#### 8.4.2 示例：用于拟合线性回归的SGD

本节将展示如何使用SGD拟合线性回归模型。回顾第4.2.7节，目标函数的形式为

$$  \mathcal{L}(\boldsymbol{\theta})=\frac{1}{2N}\sum_{n=1}^{N}(\boldsymbol{x}_{n}^{\top}\boldsymbol{\theta}-y_{n})^{2}=\frac{1}{2N}||\mathbf{X}\boldsymbol{\theta}-\boldsymbol{y}||_{2}^{2}   \tag*{(8.58)}$$

其梯度为

$$  \boldsymbol{g}_{t}=\frac{1}{N}\sum_{n=1}^{N}(\boldsymbol{\theta}_{t}^{\mathsf{T}}\boldsymbol{x}_{n}-y_{n})\boldsymbol{x}_{n}   \tag*{(8.59)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_242_137_503_394.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_654_138_910_395.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 8.16: LMS 算法示意图。左图：我们从 $\pmb{\theta}=(-0.5,2)$ 出发，逐步收敛到最小二乘解 $\hat{\pmb{\theta}}=(1.45,0.93)$（红色叉号）。右图：目标函数随时间变化的曲线。注意它并非单调递减。由 lms_demo.ipynb 生成。</div>


现在考虑使用小批量大小为 B = 1 的 SGD。更新公式变为

$$  \boldsymbol{\theta}_{t+1}=\boldsymbol{\theta}_{t}-\boldsymbol{\eta}_{t}(\boldsymbol{\theta}_{t}^{\intercal}\boldsymbol{x}_{n}-y_{n})\boldsymbol{x}_{n}   \tag*{(8.60)}$$

其中 $ n = n(t) $ 是在第 t 次迭代中选择的样本索引。整个算法称为最小均方（LMS）算法，也称为 Delta 规则或 Widoff-Hoff 规则。

Figure 8.16 显示了将该算法应用于 Figure 11.2 所示数据的结果。我们从 $\boldsymbol{\theta} = (-0.5, 2)$ 出发，并在约 26 次迭代后收敛（收敛条件为 $\|\boldsymbol{\theta}_t - \boldsymbol{\theta}_{t-1}\|_2^2$ 下降到阈值 $10^{-2}$ 以下）。注意，SGD（因此 LMS）可能需要多次遍历数据才能找到最优解。

#### 8.4.3 选择步长（学习率）

使用 SGD 时，我们需要谨慎选择学习率以实现收敛。例如，在 Figure 8.17 中，我们绘制了将 SGD 应用于深度神经网络分类器时损失随学习率的变化曲线（详见第 13 章）。我们观察到一条 U 形曲线：过小的学习率会导致欠拟合，而过大的学习率会导致模型不稳定（参见 Figure 8.11(b)）；在这两种情况下，我们都无法收敛到局部最优。

[Smi18] 提出的一种选择良好学习率的启发式方法是，从一个较小的学习率开始，逐渐增加它，并使用少量小批量来评估性能。然后绘制类似 Figure 8.17 的曲线，并选择损失最低的学习率。（在实践中，最好选择一个比损失最低点稍小（即位于其左侧）的学习率，以确保稳定性。）

与其选择单个恒定学习率，不如使用学习率调度，即随时间调整步长。从理论上讲，SGD 达到收敛的一个充分条件是

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_381_150_762_409.jpg" alt="图像" width="33%" /></div>


<div style="text-align: center;">图 8.17：损失 vs 学习率（横轴）。在 FashionMNIST 上使用普通 SGD 拟合一个小型 MLP 时的训练损失与学习率关系。（蓝色为原始损失，橙色为 EWMA 平滑版本）。由 lrschedule_tf.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_189_527_460_727.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_473_527_739_726.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_752_527_1029_725.jpg" alt="图像" width="24%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 8.18：一些常见学习率调度的示意图。(a) 分段常数。(b) 指数衰减。(c) 多项式衰减。由 learning_rate_plot.ipynb 生成。</div>


当学习率调度满足 Robbins-Monro 条件时，算法收敛：

$$  \eta_{t}\to0,\frac{\sum_{t=1}^{\infty}\eta_{t}^{2}}{\sum_{t=1}^{\infty}\eta_{t}}\to0   \tag*{(8.61)}$$

下面列出了一些常见的学习率调度示例：

$$  \eta_{t}=\eta_{i}\mathrm{~i f~}t_{i}\leq t\leq t_{i+1}\quad\mathrm{p i e c e w i s e~c o n s t a n t}   \tag*{(8.62)}$$

$$  \eta_{t}=\eta_{0}e^{-\lambda t}\mathrm{e x p o n e n t i a l}\mathrm{d e c a y}   \tag*{(8.63)}$$

$$  \eta_{t}=\eta_{0}(\beta t+1)^{-\alpha}polynomial decay   \tag*{(8.64)}$$

在分段常数调度中，$t_i$ 是一组时间点，我们在这些点上将学习率调整到指定值。例如，我们可以设置 $\eta_i = \eta_0 \gamma^i$，即每经过一个阈值（或里程碑）就将初始学习率缩小 $\gamma$ 倍。图 8.18a 展示了 $\eta_0 = 1$ 时的情形。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_256_122_505_299.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_615_136_970_305.jpg" alt="图像" width="30%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 8.19：(a) 线性预热后接余弦冷却。(b) 循环学习率调度。</div>


以及 $ \gamma = 0.9 $。这称为**步长衰减**（step decay）。有时阈值时刻是自适应计算的，通过估计训练损失或验证损失何时进入平台期来实现；这称为**平台期衰减**（reduce-on-plateau）。指数衰减通常过快，如图 8.18b 所示。一种常见选择是**多项式衰减**，取 $ \alpha = 0.5 $ 和 $ \beta = 1 $，如图 8.18c 所示；这对应于平方根调度 $ \eta_t = \eta_0 \frac{1}{\sqrt{t+1}} $。

在深度学习社区中，另一种常见调度是先快速提高学习率，然后再逐渐降低，如图 8.19a 所示。这称为**学习率预热**（learning rate warmup），或**单周期学习率调度** [Smi18]。其动机如下：初始时参数可能处于损失景观中条件较差的区域，因此较大的步长会导致"震荡"过多（比较图 8.11(b)），无法沿下降方向取得进展。然而，通过使用较小的学习率，算法可以探索更平坦的空间区域，在这些区域可以使用较大的步长。一旦到达那里，就可以快速取得进展。但为了确保收敛到某一点，我们必须将学习率降至 0。更多细节参见 [Got+19; Gil+21]。

也可以多次以循环方式提高和降低学习率。这称为**循环学习率** [Smi18]，由 fast.ai 课程推广。图 8.19b 给出了使用三角形形状的示例。该方法背后的动机是逃离局部极小值。最小和最大学习率可以基于上述初始"试运行"来找到，而半周期可以根据训练预算中希望进行的重启次数来选择。一种相关方法称为**带热重启的随机梯度下降**，由 [LH17] 提出；他们建议存储每次冷却后访问的所有检查点，并将它们全部用作模型集成的成员。（集成学习的讨论见第 18.2 节。）

除了使用启发式方法估计学习率之外，另一种选择是**线搜索**（第 8.2.2.2 节）。这一方法在使用 SGD 时较为棘手，因为梯度噪声使得 Armijo 条件的计算变得困难 [CS20]。然而，[Vas+19] 表明，如果梯度噪声的方差随时间趋近于零，则可以使该方法有效。当模型足够灵活以至于能够完美插值训练集时，这种情况可能发生。

---

#### 8.4.4 迭代平均

SGD 产生的参数估计随时间可能会非常不稳定。为了降低估计的方差，我们可以通过以下公式计算平均值：

$$  \overline{{\boldsymbol{\theta}}}_{t}=\frac{1}{t}\sum_{i=1}^{t}\boldsymbol{\theta}_{i}=\frac{1}{t}\boldsymbol{\theta}_{t}+\frac{t-1}{t}\overline{{\boldsymbol{\theta}}}_{t-1}   \tag*{(8.65)}$$

其中 $\theta_{t}$ 是常规的 SGD 迭代结果。这种方法称为**迭代平均**或 **Polyak-Ruppert 平均** [Rup88]。

在文献 [PJ92] 中，作者证明了估计量 $\overline{\theta}_{t}$ 在 SGD 算法中达到了**最佳的渐近收敛速率**，与使用二阶信息（如 Hessian 矩阵）的变体相当。

这种平均方法还具有统计上的优势。例如，文献 [NR18] 中证明，在线性回归的情况下，该方法等价于 $\ell_{2}$ 正则化（即岭回归）。

与 SGD 迭代的指数移动平均不同，**随机权重平均 (SWA)** [Izm+18] 采用等权平均并结合修改后的学习率调度。与标准 Polyak-Ruppert 平均（其动机是为了获得更快的收敛速度）相比，SWA 利用了训练深度神经网络时目标函数的平坦性，从而找到泛化能力更好的解。

#### 8.4.5 方差缩减 $ * $

本节讨论降低 SGD 方差的各种方法。在某些情况下，这可以将理论收敛速率从次线性提升到线性（即与全批量梯度下降相同）[SLRB17; JZ13; DBLJ14]。这些方法旨在减小梯度本身的方差，而非参数的方差，并且专门用于解决有限和问题。

##### 8.4.5.1 SVRG

**随机方差缩减梯度 (SVRG)** [JZ13] 的基本思想是使用控制变量法，即基于全批量估计一个梯度基线值，然后用该基线来对比随机梯度。

更精确地说，我们每隔一段时间（例如，每轮 epoch）在模型参数的“快照” $\hat{\theta}$ 处计算一次全梯度；因此对应的“精确”梯度为 $\nabla\mathcal{L}(\hat{\theta})$。在第 $t$ 步，我们计算当前参数处的常规随机梯度 $\nabla\mathcal{L}_t(\theta_t)$，同时也计算快照参数处的随机梯度 $\nabla\mathcal{L}_t(\hat{\theta})$，并将其作为基线。然后使用以下改进的梯度估计：

$$  \boldsymbol{g}_{t}=\nabla\mathcal{L}_{t}(\boldsymbol{\theta}_{t})-\nabla\mathcal{L}_{t}(\tilde{\boldsymbol{\theta}})+\nabla\mathcal{L}(\tilde{\boldsymbol{\theta}})   \tag*{(8.66)}$$

来计算 $\boldsymbol{\theta}_{t+1}$。该估计是无偏的，因为 $\mathbb{E}\left[\nabla\mathcal{L}_{t}(\tilde{\boldsymbol{\theta}})\right] = \nabla\mathcal{L}(\tilde{\boldsymbol{\theta}})$。此外，该更新只涉及两次梯度计算，因为 $\nabla\mathcal{L}(\tilde{\boldsymbol{\theta}})$ 每轮 epoch 只需计算一次。在 epoch 结束时，我们根据 $\boldsymbol{\theta}_{t}$ 的最新值或迭代结果的运行平均值来更新快照参数 $\tilde{\boldsymbol{\theta}}$，并更新期望基线。（可以降低快照更新频率，但如文献 [DB18] 所示，基线若与目标函数相关性降低，可能会损害性能。）

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可证。

---

SVRG 的迭代计算速度比全批量 GD 更快，但 SVRG 仍能达到与 GD 相同的理论收敛速率。

##### 8.4.5.2 SAGA

在本节中，我们介绍 [DBLJ14] 提出的随机平均梯度加速（SAGA）算法。与 SVRG 不同，它仅在算法开始时需要计算一次全批量梯度。然而，它通过使用更多内存来“补偿”这种时间上的节省。具体而言，该方法必须存储 N 个梯度向量。这使得它可以通过从总和中移除旧的局部梯度并替换为新的局部梯度，来保持对全局梯度的近似。这被称为聚合梯度方法。

更精确地说，我们首先初始化，计算所有  $ n $ 的  $ g_{n}^{\text{local}} = \nabla \mathcal{L}_{n}(\boldsymbol{\theta}_{0}) $，以及均值  $ g^{\text{avg}} = \frac{1}{N} \sum_{n=1}^{N} g_{n}^{\text{local}} $。然后，在第  $ t $ 次迭代中，我们使用梯度估计

$$  \boldsymbol{g}_{t}=\nabla\mathcal{L}_{n}(\boldsymbol{\theta}_{t})-\boldsymbol{g}_{n}^{\mathrm{l o c a l}}+\boldsymbol{g}^{\mathrm{a v g}}   \tag*{(8.67)}$$

其中  $ n \sim \text{Unif}\{1, \ldots, N\} $ 是第  $ t $ 次迭代中采样的样本索引。接着，我们更新  $ g_n^{\text{local}} = \nabla \mathcal{L}_n(\boldsymbol{\theta}_t) $ 和  $ g^{\text{avg}} $，将旧的  $ g_n^{\text{local}} $ 替换为其新值。

相比 SVRG，此方法的一个优势在于，它只需在开始时进行一次全批次扫描。（实际上，初始扫描并非必要，因为我们可以通过仅纳入已见过的梯度来“惰性”计算  $ g^{avg} $。）缺点是需要大量额外内存。然而，如果特征（以及梯度）是稀疏的，内存开销是合理的。实际上，当 N 很大且 x 稀疏时，scikit-learn 的逻辑回归代码推荐使用 SAGA 算法。$ ^{3} $

##### 8.4.5.3 在深度学习中的应用

方差缩减方法被广泛用于拟合具有凸目标的机器学习模型，例如线性模型。然而，将 SVRG 应用于常规深度学习训练实践存在多种困难。例如，批归一化（第 14.2.4.1 节）、数据增强（第 19.1 节）和 dropout（第 13.5.4 节）的使用都打破了该方法的假设，因为损失会以不仅取决于参数和数据索引 n 的方式随机变化。更多细节可参考 [DB18; Arn+19]。

#### 8.4.6 预条件 SGD

在本节中，我们考虑预条件 SGD，其更新公式如下：

$$  \boldsymbol{\theta}_{t+1}=\boldsymbol{\theta}_{t}-\boldsymbol{\eta}_{t}\mathbf{M}_{t}^{-1}\boldsymbol{g}_{t},   \tag*{(8.68)}$$

其中  $ M_t $ 是预条件矩阵，或简称为预条件子，通常选择为正定矩阵。不幸的是，梯度估计中的噪声使得难以可靠地估计 Hessian 矩阵，从而难以使用第 8.3 节中的方法。此外，使用完整的预条件矩阵求解更新方向代价高昂。因此，大多数从业者使用对角预条件子  $ M_t $。此类预条件子未必利用二阶信息，但往往比普通 SGD 带来加速。另见 [Roo+21]。

---

针对这些启发式方法的概率解释，以及关于一些简单数据集的实证比较，请参见 sgd_comparison.ipynb。

##### 8.4.6.1 ADAGRAD

ADAGRAD（“自适应梯度”的缩写）方法由 [DHS11] 提出，最初设计用于优化凸目标函数，其中梯度向量的许多元素为零；这些元素可能对应于输入中极少出现的特征，例如罕见词。其更新形式如下：

$$  \theta_{t+1,d}=\theta_{t,d}-\eta_{t}\frac{1}{\sqrt{s_{t,d}+\epsilon}}g_{t,d}   \tag*{(8.69)}$$

其中 $d = 1 : D$ 表示参数向量的维度索引，且

$$  s_{t,d}=\sum_{i=1}^{t}g_{i,d}^{2}   \tag*{(8.70)}$$

为平方梯度的累加和，$\epsilon > 0$ 是一个小项，用于避免除零。等价地，我们可以将更新写成向量形式：

$$  \Delta\theta_{t}=-\eta_{t}\frac{1}{\sqrt{s_{t}+\epsilon}}g_{t}   \tag*{(8.71)}$$

其中平方根和除法按元素执行。从预处理 SGD 的角度看，这等价于取 $\mathbf{M}_t = \mathrm{diag}(\mathbf{s}_t + \boldsymbol{\epsilon})^{1/2}$。这就是自适应学习率的一个例子；整体步长 $\eta_t$ 仍需选择，但相比普通 GD，结果对其敏感度更低。通常我们固定 $\eta_t = \eta_0$。

##### 8.4.6.2 RMSProp 与 AdaDelta

ADAGRAD 的一个显著特征是分母项随时间增大，从而有效学习率不断下降。虽然这对于保证收敛性是必要的，但分母增长过快可能会损害性能。

另一种做法是使用过去平方梯度的**指数加权移动平均**（EWMA，见第 4.4.2.2 节），而非它们的累加和：

$$  s_{t+1,d}=\beta s_{t,d}+(1-\beta)g_{t,d}^{2}   \tag*{(8.72)}$$

实际中通常取 $\beta\sim0.9$，这使得更近期的样本获得更大权重。此时，

$$  \sqrt{s_{t,d}}\approx RMS(\boldsymbol{g}_{1:t,d})=\sqrt{\frac{1}{t}\sum_{\tau=1}^{t}g_{\tau,d}^{2}}   \tag*{(8.73)}$$

其中 RMS 代表“均方根”。因此，该方法（基于 [RB93] 中早期的 RPROP 方法）被称为 RMSProp [Hin14]。RMSProp 的整体更新为

$$  \Delta\theta_{t}=-\eta_{t}\frac{1}{\sqrt{s_{t}+\epsilon}}g_{t}.   \tag*{(8.74)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可。

---

ADADELTA 方法由 [Zei12] 独立提出，与 RMSprop 类似。然而，除了对梯度 $ \hat{s} $ 累积指数加权移动平均 (EWMA) 外，它还对更新量 $ \delta_{t} $ 保留 EWMA，从而得到如下形式的更新：

$$  \Delta\theta_{t}=-\eta_{t}\frac{\sqrt{\delta_{t-1}+\epsilon}}{\sqrt{s_{t}+\epsilon}}g_{t}   \tag*{(8.75)}$$

其中

$$  \boldsymbol{\delta}_{t}=\beta\boldsymbol{\delta}_{t-1}+(1-\beta)(\Delta\boldsymbol{\theta}_{t})^{2}   \tag*{(8.76)}$$

而 $s_t$ 与 RMSPROP 中的定义相同。这样做的好处是分子和分母的“单位”相互抵消，因此我们只需将梯度逐元素乘以一个标量。这消除了调整学习率 $\eta_t$ 的必要性，意味着我们可以直接设置 $\eta_t = 1$，尽管 ADADELTA 的常用实现仍然将 $\eta_t$ 保留为可调超参数。然而，由于这些自适应学习率不一定会随时间减小（除非我们显式地让 $\eta_t$ 衰减），因此这些方法不能保证收敛到解。

##### 8.4.6.3 ADAM

我们可以将 RMSPROP 与动量结合起来。具体地，我们计算梯度的指数加权移动平均（如动量方法）和平方梯度的指数加权移动平均（如 RMSPROP 方法）：

$$  \boldsymbol{m}_{t}=\beta_{1}\boldsymbol{m}_{t-1}+(1-\beta_{1})\boldsymbol{g}_{t}   \tag*{(8.77)}$$

$$  \boldsymbol{s}_{t}=\beta_{2}\boldsymbol{s}_{t-1}+(1-\beta_{2})\boldsymbol{g}_{t}^{2}   \tag*{(8.78)}$$

然后执行如下更新：

$$  \theta_{t}=\theta_{t}-\eta_{t}\frac{m_{t}}{\sqrt{s_{t}}+\epsilon}   \tag*{(8.79)}$$

由此得到的方法称为 ADAM，其全称为“自适应矩估计”（adaptive moment estimation）[KB15]。

各个常数的标准取值为 $\beta_1 = 0.9$、$\beta_2 = 0.999$ 和 $\epsilon = 10^{-6}$。（若设置 $\beta_1 = 0$ 且不进行偏差校正，则恢复为不使用动量的 RMSPROP。）对于全局学习率，通常使用固定值如 $\eta_t = 0.001$。同样地，由于自适应学习率可能不随时间衰减，因此不能保证收敛（见第 8.4.6.4 节）。

如果初始化为 $\boldsymbol{m}_{0} = \boldsymbol{s}_{0} = \mathbf{0}$，那么初始估计会偏向于较小值。因此，作者建议使用偏差校正后的矩，这会在优化过程的早期增大这些估计值。这些校正后的估计由下式给出：

$$  \hat{\boldsymbol{m}}_{t}=\boldsymbol{m}_{t}/(1-\beta_{1}^{t})   \tag*{(8.80)}$$

$$  \hat{\boldsymbol{s}}_{t}=\boldsymbol{s}_{t}/(1-\beta_{2}^{t})   \tag*{(8.81)}$$

偏差校正的优势如图 4.3 所示。

---

##### 8.4.6.4 自适应学习率的问题

当使用对角缩放方法时，整体学习率由随时间变化的 $\eta_0M_t^{-1}$ 决定，因此这些方法通常被称为自适应学习率方法。然而，它们仍需要设置基础学习率 $\eta_0$。

由于指数加权移动平均（EWMA）方法通常在梯度估计存在噪声的随机环境下使用，其学习率自适应即使在凸问题上也可能导致不收敛 [RKK18]。在文献 [Zha+22] 中，他们通过实验表明，只要针对每个数据集分别调整 $\beta_1$ 和 $\beta_2$ 参数，标准 Adam 算法就能收敛，但更好的做法是找到一种自动且鲁棒的方法。针对这一问题已提出了多种解决方案，包括 AMSGRAD [RKK18]、PADAM [CG18; Zho+18] 和 YOGI [Zah+18]。例如，YOGI 更新通过将

$$  \boldsymbol{s}_{t}=\beta_{2}\boldsymbol{s}_{t-1}+(1-\beta_{2})\boldsymbol{g}_{t}^{2}=\boldsymbol{s}_{t-1}+(1-\beta_{2})(\boldsymbol{g}_{t}^{2}-\boldsymbol{s}_{t-1})   \tag*{(8.82)}$$

替换为

$$  \boldsymbol{s}_{t}=\boldsymbol{s}_{t-1}+(1-\beta_{2})\boldsymbol{g}_{t}^{2}\odot\operatorname{sgn}(\boldsymbol{g}_{t}^{2}-\boldsymbol{s}_{t-1})   \tag*{(8.83)}$$

来修改 Adam 算法。

最近，文献 [tan+24] 提出了 ADOPT，该方法不仅具有可证明的收敛性，而且在实践中似乎也更有效。其基本思想是在计算动量更新之前先对梯度进行归一化（预处理），即使用 $m_t = \beta_1 m_{t-1} + (1 - \beta_1) \frac{g_t}{\sqrt{s_{t-1} + \epsilon}}$ 替代 $m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$。同时，参数更新使用 $\theta_t = \theta_t - \eta_t m_t$ 而非 $\theta_t = \theta_t - \eta_t \frac{m_t}{\sqrt{s_{t} + \epsilon}}$。

##### 8.4.6.5 非对角预处理矩阵

尽管上述方法能够自适应每个参数的学习率，但它们并未解决由参数相关性导致的更根本的病态问题，因此有时并不能像预期的那样比标准 SGD 带来更大的加速。

一种实现更快收敛的方法是使用以下预处理矩阵，即全矩阵 Adagrad [DHS11]：

$$  \mathbf{M}_{t}=[(\mathbf{G}_{t}\mathbf{G}_{t}^{\mathsf{T}})^{\frac{1}{2}}+\epsilon\mathbf{I}_{D}]^{-1}   \tag*{(8.84)}$$

其中

$$  \mathbf{G}_{t}=[g_{t},\ldots,g_{1}]   \tag*{(8.85)}$$

这里 $g_i = \nabla_{\psi} c(\psi_i)$ 是第 $i$ 步计算得到的 $D$ 维梯度向量。不幸的是，$M_t$ 是一个 $D \times D$ 的矩阵，存储和求逆的成本很高。

Shampoo 算法 [GKS18] 对 $\mathbf{M}$ 进行了块对角近似，每层模型一个块，并利用克罗内克积结构高效地求逆。（该算法之所以称为“shampoo”，是因为它使用了“护发素”（preconditioner）。）最近，[Ani+20] 将该方法扩展到可在创纪录的时间内拟合超大型深度模型。

作者：Kevin P. Murphy。(C) MIT出版社。CC-BY-NC-ND许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_178_123_996_375.jpg" alt="图" width="71%" /></div>


<div style="text-align: center;">图 8.20：一些约束优化问题的示意图。红色等高线为目标函数  $ \mathcal{L}(\boldsymbol{\theta}) $ 的等值线。最优约束解为黑点；(a) 蓝色线为等式约束  $ h(\boldsymbol{\theta}) = 0 $；(b) 蓝色线表示不等式约束  $ |\theta_1| + |\theta_2| \leq 1 $。（可与图 11.8（左）对比。）</div>


### 8.5 约束优化

在本节中，我们考虑如下约束优化问题：

$$  \theta^{*}=\arg\min_{\theta\in\mathcal{C}}\mathcal{L}(\theta)   \tag*{(8.86)}$$

其中可行集或约束集为：

$$  \mathcal{C}=\{\boldsymbol{\theta}\in\mathbb{R}^{D}:h_{i}(\boldsymbol{\theta})=0,i\in\mathcal{E},g_{j}(\boldsymbol{\theta})\leq0,j\in\mathcal{I}\}   \tag*{(8.87)}$$

这里 $ \mathcal{E} $ 是等式约束的集合，$ \mathcal{I} $ 是不等式约束的集合。

例如，假设有一个二次目标函数 $ \mathcal{L}(\boldsymbol{\theta}) = \theta_1^2 + \theta_2^2 $，且受线性等式约束 $ h(\boldsymbol{\theta}) = 1 - \theta_1 - \theta_2 = 0 $。图 8.20(a) 绘制了 $ \mathcal{L} $ 的等值线以及约束曲面。我们要做的是找到位于该直线上且距离原点最近的点 $ \boldsymbol{\theta}^* $。从几何上可以明显看出，最优解为 $ \boldsymbol{\theta} = (0.5, 0.5) $，用实心黑点表示。

在接下来的几节中，我们将简要介绍约束优化的一些基本理论和算法。更详细的内容可参考其他著作，如 [BV04; NW06; Ber15; Ber16]。

#### 8.5.1 拉格朗日乘子法

本节讨论如何求解等式约束优化问题。我们首先假设只有一个等式约束 $ h(\boldsymbol{\theta}) = 0 $。

首先注意到，约束曲面上的任意一点处，$ \nabla h(\boldsymbol{\theta}) $ 都垂直于约束曲面。原因如下：考虑另一个也位于曲面上的邻近点 $ \boldsymbol{\theta} + \boldsymbol{\epsilon} $。在 $ \boldsymbol{\theta} $ 附近进行一阶泰勒展开，得到：

$$  h(\boldsymbol{\theta}+\boldsymbol{\epsilon})\approx h(\boldsymbol{\theta})+\boldsymbol{\epsilon}^{\mathsf{T}}\nabla h(\boldsymbol{\theta})   \tag*{(8.88)}$$

---

由于 $\theta$ 和 $\theta + \epsilon$ 都在约束曲面上，必须有 $h(\theta) = h(\theta + \epsilon)$，因此 $\epsilon^\top \nabla h(\theta) \approx 0$。由于 $\epsilon$ 平行于约束曲面，$\nabla h(\theta)$ 必须垂直于约束曲面。

我们在约束曲面上寻找一个点 $\boldsymbol{\theta}^*$，使得 $\mathcal{L}(\boldsymbol{\theta})$ 最小化。我们刚刚表明，它必须满足 $\nabla h(\boldsymbol{\theta}^*)$ 正交于约束曲面的条件。此外，这样的点还必须具有性质：$\nabla \mathcal{L}(\boldsymbol{\theta})$ 也正交于约束曲面，否则我们可以沿着约束曲面移动一小段距离来减小 $\mathcal{L}(\boldsymbol{\theta})$。由于在 $\boldsymbol{\theta}^*$ 处 $\nabla h(\boldsymbol{\theta})$ 和 $\nabla \mathcal{L}(\boldsymbol{\theta})$ 都正交于约束曲面，它们必须相互平行（或反平行）。因此，存在一个常数 $\lambda^* \in \mathbb{R}$ 使得

$$  \nabla\mathcal{L}(\boldsymbol{\theta}^{*})=\lambda^{*}\nabla h(\boldsymbol{\theta}^{*})   \tag*{(8.89)}$$

（我们不能直接令梯度向量相等，因为它们的大小可能不同。）常数 $\lambda^*$ 称为**拉格朗日乘子**，可以为正、负或零。后一种情况发生在 $\nabla\mathcal{L}(\theta^*) = 0$ 时。

我们可以将方程 (8.89) 转化为一个目标函数，称为**拉格朗日函数**，我们需要找到以下函数的驻点：

$$  L(\boldsymbol{\theta},\lambda)\triangleq\mathcal{L}(\boldsymbol{\theta})+\lambda h(\boldsymbol{\theta})   \tag*{(8.90)}$$

在拉格朗日函数的驻点处，有

$$  \nabla_{\theta,\lambda}L(\theta,\lambda)=\mathbf{0}\iff\lambda\nabla_{\theta}h(\theta)=\nabla\mathcal{L}(\theta),h(\theta)=0   \tag*{(8.91)}$$

这被称为**临界点**，它满足原始约束 $ h(\boldsymbol{\theta}) = 0 $ 和方程 (8.89)。如果存在 m > 1 个约束，我们可以通过加法构造一个新的约束函数，如下所示：

$$  L(\boldsymbol{\theta},\boldsymbol{\lambda})=\mathcal{L}(\boldsymbol{\theta})+\sum_{j=1}^{m}\lambda_{j}h_{j}(\boldsymbol{\theta})   \tag*{(8.92)}$$

现在我们有了 $ D+m $ 个方程和 $ D+m $ 个未知数，可以使用标准的无约束优化方法来寻找驻点。下面给出一些例子。

##### 8.5.1.1 示例：二维二次目标函数带一个线性等式约束

考虑在约束 $\theta_1 + \theta_2 = 1$ 下最小化 $\mathcal{L}(\boldsymbol{\theta}) = \theta_1^2 + \theta_2^2$。（这是图 8.20(a) 中所示的问题。）拉格朗日函数为

$$  L(\theta_{1},\theta_{2},\lambda)=\theta_{1}^{2}+\theta_{2}^{2}+\lambda(\theta_{1}+\theta_{2}-1)   \tag*{(8.93)}$$

驻点的条件如下：

$$  \frac{\partial}{\partial\theta_{1}}L(\theta_{1},\theta_{2},\lambda)=2\theta_{1}+\lambda=0   \tag*{(8.94)}$$

$$  \frac{\partial}{\partial\theta_{2}}L(\theta_{1},\theta_{2},\lambda)=2\theta_{2}+\lambda=0   \tag*{(8.95)}$$

$$  \frac{\partial}{\partial\lambda}L(\theta_{1},\theta_{2},\lambda)=\theta_{1}+\theta_{2}-1=0   \tag*{(8.96)}$$

由方程 (8.94) 和 (8.95) 可得 $2\theta_1 = -\lambda = 2\theta_2$，因此 $\theta_1 = \theta_2$。另外，由方程 (8.96) 可得 $2\theta_1 = 1$。所以 $\theta^* = (0.5, 0.5)$，正如我们之前所说。此外，由于目标函数是凸的且约束是仿射的，这是全局最小值。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 8.5.2 KKT 条件

在本节中，我们将拉格朗日乘子的概念推广到处理不等式约束。

首先考虑只有一个不等式约束 $ g(\boldsymbol{\theta}) \leq 0 $ 的情况。为了找到最优解，一种方法是考虑一个无约束问题，其中我们引入一个无限阶跃函数作为惩罚项：

$$  \hat{\mathcal{L}}(\boldsymbol{\theta})=\mathcal{L}(\boldsymbol{\theta})+\infty\mathbb{I}\left(g(\boldsymbol{\theta})>0\right)   \tag*{(8.97)}$$

然而，这是一个不连续的函数，难以优化。

相反，我们构造一个形如 $ \mu g(\boldsymbol{\theta}) $ 的下界，其中 $ \mu \geq 0 $。这给出了如下的拉格朗日函数：

$$  L(\boldsymbol{\theta},\mu)=\mathcal{L}(\boldsymbol{\theta})+\mu g(\boldsymbol{\theta})   \tag*{(8.98)}$$

注意到阶跃函数可以通过下式恢复：

$$  \hat{\mathcal{L}}(\boldsymbol{\theta})=\max_{\mu\geq0}L(\boldsymbol{\theta},\mu)=\begin{cases}\infty&如果 g(\boldsymbol{\theta})>0,\\ \mathcal{L}(\boldsymbol{\theta})&否则\end{cases}   \tag*{(8.99)}$$

因此，我们的优化问题变为

$$  \min_{\boldsymbol{\theta}}\max_{\mu\geq0}L(\boldsymbol{\theta},\mu)   \tag*{(8.100)}$$

现在考虑一般情况，其中有多个不等式约束 $ g(\theta) \leq 0 $ 和多个等式约束 $ h(\theta) = 0 $。广义拉格朗日函数变为

$$  L(\boldsymbol{\theta},\boldsymbol{\mu},\boldsymbol{\lambda})=\mathcal{L}(\boldsymbol{\theta})+\sum_{i}\mu_{i}g_{i}(\boldsymbol{\theta})+\sum_{j}\lambda_{j}h_{j}(\boldsymbol{\theta})   \tag*{(8.101)}$$

（我们可以自由地将 $ -\lambda_j h_j $ 改为 $ + \lambda_j h_j $，因为符号是任意的。）我们的优化问题变为

$$  \min_{\theta}\max_{\mu\geq0,\lambda}L(\theta,\mu,\lambda)   \tag*{(8.102)}$$

当 $L$ 和 $g$ 是凸函数时，该问题的所有临界点必须满足以下条件（在某些条件下 [BV04, Sec.5.2.3]）：

• 所有约束都被满足（这称为可行性）：

$$  g(\theta)\leq0,\quad h(\theta)=0   \tag*{(8.103)}$$

• 解是一个驻点：

$$  \nabla\mathcal{L}(\boldsymbol{\theta}^{*})+\sum_{i}\mu_{i}\nabla g_{i}(\boldsymbol{\theta}^{*})+\sum_{j}\lambda_{j}\nabla h_{j}(\boldsymbol{\theta}^{*})=\mathbf{0}   \tag*{(8.104)}$$

“概率机器学习：导论”。在线版本。2024年11月23日

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_397_133_557_294.jpg" alt="图像" width="13%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_622_162_774_307.jpg" alt="图像" width="13%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 8.21: (a) 二维中由线性约束的交集定义的凸多面体。(b) 可行集以及线性目标函数的描绘。红线是目标函数的水平集，箭头表示其改进方向。我们看到最优解位于多面体的一个顶点上。</div>

- 不等式约束的罚项指向正确方向（这称为对偶可行性）：

$$  \mu\geq0   \tag*{(8.105)}$$

- 拉格朗日乘子拾取了非活跃约束中的任何松弛部分，即要么 $ \mu_i = 0 $，要么 $ g_i(\boldsymbol{\theta}^*) = 0 $，因此

$$  \mu\odot g=0   \tag*{(8.106)}$$

这称为互补松弛性。

为了理解最后一个条件为何成立，考虑（为简单起见）单个不等式约束的情况：$ g(\boldsymbol{\theta}) \leq 0 $。它要么是 **活跃的**（即 $ g(\boldsymbol{\theta}) = 0 $），要么是非活跃的（即 $ g(\boldsymbol{\theta}) < 0 $）。在活跃情况下，解位于约束边界上，且 $ g(\boldsymbol{\theta}) = 0 $ 变为一个等式约束；那么根据方程 (8.89)，我们有 $ \nabla \mathcal{L} = \mu \nabla g $，其中常数 $ \mu \neq 0 $。在非活跃情况下，解不在约束边界上；我们仍然有 $ \nabla \mathcal{L} = \mu \nabla g $，但此时 $ \mu = 0 $。

这些被称为卡罗需-库恩-塔克（KKT）条件。如果 L 是凸函数，且约束定义了一个凸集，那么 KKT 条件是（全局）最优性的充分必要条件。

#### 8.5.3 线性规划

考虑在线性约束下优化一个线性函数。写成标准形式时，可表示为

$$  \min_{\boldsymbol{\theta}}\boldsymbol{c}^{\mathrm{T}}\boldsymbol{\theta}\qquad\mathrm{s.t.}\quad\mathbf{A}\boldsymbol{\theta}\leq\boldsymbol{b},\boldsymbol{\theta}\geq0   \tag*{(8.107)}$$

可行集定义了一个凸多面体，即由半空间交集定义的凸集。二维示例如图 8.21(a) 所示。图 8.21(b) 显示了一个线性代价函数，该函数

作者：Kevin P. Murphy。 (C) MIT 出版社。 CC-BY-NC-ND 许可证

---

随着我们向右下角移动而减小。我们看到可行集中的最低点是一个顶点。事实上，可以证明（假设解唯一）最优点总是出现在多面体的顶点处。如果存在多个解，则等值线将与某个面平行。也可能在可行集内没有最优点；在这种情况下，问题被称为不可行。

##### 8.5.3.1 单纯形法

可以证明，线性规划的最优点位于定义可行集的多面体的顶点处（例如，参见图8.21(b)）。单纯形法通过从顶点移动到顶点来求解线性规划，每次寻找能使目标函数改善最大的边。

在最坏情况下，单纯形法可能需要关于维度 $D$ 的指数时间，尽管在实践中它通常非常高效。还有其他多项式时间算法，例如内点法，尽管这些方法在实践中往往较慢。

##### 8.5.3.2 应用

线性规划在科学、工程和商业中有许多应用。它在一些机器学习问题中也很有用。例如，第11.6.1.1节展示了如何使用它来解决稳健线性回归。它还可用于图形模型中的状态估计（例如，参见[SGJ11]）。

#### 8.5.4 二次规划

考虑在满足线性等式和不等式约束的条件下最小化一个二次目标函数。这类问题称为二次规划（quadratic program, QP），可以写成如下形式：

$$  \min_{\boldsymbol{\theta}}\frac{1}{2}\boldsymbol{\theta}^{\mathrm{T}}\mathbf{H}\boldsymbol{\theta}+\boldsymbol{c}^{\mathrm{T}}\boldsymbol{\theta}\qquad\mathrm{s.t.}\quad\mathbf{A}\boldsymbol{\theta}\leq\boldsymbol{b},\mathbf{C}\boldsymbol{\theta}=\boldsymbol{d}   \tag*{(8.108)}$$

如果 $\mathbf{H}$ 是半正定的，那么这是一个凸优化问题。

##### 8.5.4.1 示例：带线性不等式约束的二维二次目标函数

作为一个具体例子，假设我们想要最小化

$$  \mathcal{L}(\boldsymbol{\theta})=(\theta_{1}-\frac{3}{2})^{2}+(\theta_{2}-\frac{1}{8})^{2}=\frac{1}{2}\boldsymbol{\theta}^{\mathrm{T}}\mathbf{H}\boldsymbol{\theta}+\boldsymbol{c}^{\mathrm{T}}\boldsymbol{\theta}+\mathrm{c o n s t}   \tag*{(8.109)}$$

其中 $\mathbf{H}=2\mathbf{I}$ 且 $\mathbf{c}=-(3,1/4)$，满足约束

$$  \left|\theta_{1}\right|+\left|\theta_{2}\right|\leq1   \tag*{(8.110)}$$

参见图8.20(b)的示意图。

我们可以将约束重写为

$$  \theta_{1}+\theta_{2}\leq1,\ \theta_{1}-\theta_{2}\leq1,\ -\theta_{1}+\theta_{2}\leq1,\ -\theta_{1}-\theta_{2}\leq1   \tag*{(8.111)}$$

我们可以将其更紧凑地写为

$$  \mathbf{A}\theta\leq b   \tag*{(8.112)}$$

---

其中 b = 1 且

$$  \mathbf{A}=\begin{pmatrix}{{{1}}}&{{{1}}} \\{{{1}}}&{{{-1}}} \\{{{-1}}}&{{{1}}} \\{{{-1}}}&{{{-1}}}\end{pmatrix}   \tag*{(8.113)}$$

现在这已经是标准的二次规划形式。

从问题的几何结构（如图 8.20(b) 所示）可以看出，对应于菱形左侧两个面的约束是非活跃的（因为我们试图尽可能靠近圆心，而圆心位于约束可行域外部且右侧）。记 $ g_i(\boldsymbol{\theta}) $ 为矩阵 $ \mathbf{A} $ 第 $ i $ 行对应的不等式约束，这意味着 $ g_3(\boldsymbol{\theta}^*) > 0 $ 和 $ g_4(\boldsymbol{\theta}^*) > 0 $，因此由互补性可得 $ \mu_3^* = \mu_4^* = 0 $。于是我们可以移除这些非活跃约束。

根据 KKT 条件，我们有

$$  \mathbf{H}\boldsymbol{\theta}+\boldsymbol{c}+\mathbf{A}^{\mathrm{T}}\boldsymbol{\mu}=\mathbf{0}   \tag*{(8.114)}$$

将其应用于活跃约束子问题，得到

$$  \begin{pmatrix}{{{2}}}&{{{0}}}&{{{1}}}&{{{1}}} \\{{{0}}}&{{{2}}}&{{{1}}}&{{{-1}}} \\{{{1}}}&{{{1}}}&{{{0}}}&{{{0}}} \\{{{1}}}&{{{-1}}}&{{{0}}}&{{{0}}}\end{pmatrix}\begin{pmatrix}{{{\theta_{1}}}} \\{{{\theta_{2}}}} \\{{{\mu_{1}}}} \\{{{\mu_{2}}}}\end{pmatrix}=\begin{pmatrix}{{{3}}} \\{{{1/4}}} \\{{{1}}} \\{{{1}}}\end{pmatrix}   \tag*{(8.115)}$$

因此解为

$$  \boldsymbol{\theta}_{*}=\left(1,0\right)^{\mathrm{T}},\boldsymbol{\mu}_{*}=\left(0.625,0.375,0,0\right)^{\mathrm{T}}   \tag*{(8.116)}$$

注意，θ 的最优值出现在 ℓ1 "球"（菱形）的一个顶点上。

##### 8.5.4.2 应用

二次规划在机器学习中有多种应用。例如，在第 11.4 节中，我们讨论了用于稀疏线性回归的 lasso 方法，该方法归结为优化 $ \mathcal{L}(\mathbf{w}) = ||\mathbf{X}\mathbf{w} - \mathbf{y}||_2^2 + \lambda||\mathbf{w}||_1 $，可以重新表述为一个二次规划问题。在第 17.3 节中，我们展示了如何将二次规划用于支持向量机。

#### 8.5.5 混合整数线性规划 $ * $

整数线性规划（ILP）是指在满足线性约束的条件下最小化线性目标函数，其中优化变量是离散整数而非实数。其标准形式如下：

$$  \min_{\boldsymbol{\theta}}\boldsymbol{c}^{\top}\boldsymbol{\theta}\qquad s.t.\quad\mathbf{A}\boldsymbol{\theta}\leq\boldsymbol{b},\boldsymbol{\theta}\geq0,\boldsymbol{\theta}\in\mathbb{Z}^{D}   \tag*{(8.117)}$$

其中 Z 表示整数集。如果部分优化变量是实数值，则称为混合整数线性规划，通常简称为 MIP。（如果所有变量均为实数值，则退化为标准线性规划。）

作者：Kevin P. Murphy。(C) MIT Press. CC-BY-NC-ND 许可协议

---

MIPs（混合整数规划）在车辆路径规划、调度和装箱等领域有大量应用。它们对于某些机器学习（ML）应用也很有用，例如形式化验证某类深度神经网络（DNN）的行为[And+18]，以及证明DNN对对抗性（最坏情况）扰动的鲁棒性属性[TXT19]。

### 8.6 近端梯度法 \*

我们通常关注优化如下形式的目标函数

$$  \mathcal{L}(\boldsymbol{\theta})=\mathcal{L}_{s}(\boldsymbol{\theta})+\mathcal{L}_{r}(\boldsymbol{\theta})   \tag*{(8.118)}$$

其中 \( \mathcal{L}_s \) 是可微的（光滑的），而 \( \mathcal{L}_r \) 是凸的但未必可微（即可能是非光滑或“粗糙”的）。例如，\( \mathcal{L}_s \) 可能是负对数似然（NLL），\( \mathcal{L}_r \) 可能是一个指示函数，当约束被违反时取无穷大（参见 Section 8.6.1）；或者 \( \mathcal{L}_r \) 可能是某些参数的 \( \ell_1 \) 范数（参见 Section 8.6.2）；又或者 \( \mathcal{L}_r \) 可能衡量参数与一组允许量化值的距离（参见 Section 8.6.3）。

处理这类问题的一种方法是使用近端梯度法（参见 e.g., [PB+14; PSW15]）。通俗地说，该方法沿着梯度方向迈出步长为 \( \eta \) 的一步，然后将得到的参数更新投影到尊重 \( L_r \) 的空间中。更精确地，更新如下

$$  \theta_{t+1}=\operatorname{prox}_{\eta_{t}\mathcal{L}_{r}}(\boldsymbol{\theta}_{t}-\boldsymbol{\eta}_{t}\nabla\mathcal{L}_{s}(\boldsymbol{\theta}_{t}))   \tag*{(8.119)}$$

其中 \( \text{prox}_{\eta\mathcal{L}_{r}}(\boldsymbol{\theta}) \) 是 \( \mathcal{L}_{r} \)（按 \( \eta \) 缩放）在 \( \boldsymbol{\theta} \) 处的近端算子：

$$  \mathrm{prox}_{\eta\mathcal{L}_{r}}(\boldsymbol{\theta})\triangleq\underset{z}{\arg\min}\left(\mathcal{L}_{r}(z)+\frac{1}{2\eta}||z-\boldsymbol{\theta}||_{2}^{2}\right)   \tag*{(8.120)}$$

（“因子 \( \frac{1}{2} \) 是一种任意约定。”）我们可以将近端算子重新表述为求解一个约束优化问题，如下：

$$  \operatorname{prox}_{\eta\mathcal{L}_{r}}(\boldsymbol{\theta})=\underset{z}{\operatorname{argmin}}\mathcal{L}_{r}(z)\text{ s.t. } \||z-\boldsymbol{\theta}||_{2}\leq\rho   \tag*{(8.121)}$$

其中界 \( \rho \) 取决于缩放因子 \( \eta \)。因此我们看到，近端投影在最小化函数的同时，保持与当前迭代点接近（即近端）。下面给出一些例子。

#### 8.6.1 投影梯度下降

假设我们想求解问题

$$  \underset{\boldsymbol{\theta}}{\operatorname{argmin}}\mathcal{L}_{s}(\boldsymbol{\theta})\quad s.t.\quad\boldsymbol{\theta}\in\mathcal{C}   \tag*{(8.122)}$$

其中 \( \mathcal{C} \) 是一个凸集。例如，我们可能具有箱子约束 \( \mathcal{C} = \{\theta : l \leq \theta \leq u\} \)，其中我们指定每个元素的上下界。这些界对某些元素可以是无穷大。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_375_157_820_400.jpg" alt="图" width="38%" /></div>


<div style="text-align: center;">图 8.22：投影梯度下降法示意图。w 是当前参数估计值，w' 是经过一个梯度步后的更新值，$ P_C(\mathbf{w}') $ 将其投影到约束集 C 上。来源：https://bit.ly/3eJ3BhZ，经 Martin Jaggi 许可使用。</div>


如果我们不希望约束某一维度上的值，则可以忽略该维度的约束。例如，若只想确保参数非负，则针对每个维度 $ d $ 设置 $ l_d = 0 $ 和 $ u_d = \infty $。

我们可以通过在原始目标函数中添加惩罚项，将带约束的优化问题转化为无约束问题：

$$  \mathcal{L}(\boldsymbol{\theta})=\mathcal{L}_{s}(\boldsymbol{\theta})+\mathcal{L}_{r}(\boldsymbol{\theta})   \tag*{(8.123)}$$

其中 $ \mathcal{L}_{r}(\boldsymbol{\theta}) $ 是凸集 $ \mathcal{C} $ 的指示函数，即：

$$  \mathcal{L}_{r}(\boldsymbol{\theta})=I_{\mathcal{C}}(\boldsymbol{\theta})=\begin{cases}0&\text{若}\boldsymbol{\theta}\in\mathcal{C}\\\infty&\text{若}\boldsymbol{\theta}\notin\mathcal{C}\end{cases}   \tag*{(8.124)}$$

我们可以使用近端梯度下降法求解方程 (8.123)。指示函数的近端算子等价于到集合 C 的投影：

$$  \operatorname{proj}_{\mathcal{C}}(\boldsymbol{\theta})=\underset{\boldsymbol{\theta}^{\prime}\in\mathcal{C}}{\operatorname{argmin}}||\boldsymbol{\theta}^{\prime}-\boldsymbol{\theta}||_{2}   \tag*{(8.125)}$$

该方法称为**投影梯度下降法**。图 8.22 给出了示意图。

例如，考虑箱型约束 $ \mathcal{C} = \{\theta : l \leq \theta \leq \boldsymbol{u}\} $。此情况下的投影算子可以通过在边界处进行简单的阈值截断来逐元素计算：

$$  \mathrm{proj}_{\mathcal{C}}(\boldsymbol{\theta})_{d}=\begin{cases}l_{d}&\text{若}\theta_{d}\leq l_{d}\\\theta_{d}&\text{若}l_{d}\leq\theta_{d}\leq u_{d}\\u_{d}&\text{若}\theta_{d}\geq u_{d}\end{cases}   \tag*{(8.126)}$$

例如，若想确保所有元素非负，可以使用

$$  \mathrm{proj}_{\mathcal{C}}(\boldsymbol{\theta})=\boldsymbol{\theta}_{+}=[\max(\theta_{1},0),\ldots,\max(\theta_{D},0)]   \tag*{(8.127)}$$

关于该方法在稀疏线性回归中的应用，请参见第 11.4.9.2 节。

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可协议。

---

#### 8.6.2  ℓ1 范数正则化器的近端算子

考虑一个形式为  $ f(\boldsymbol{x}; \boldsymbol{\theta}) = \sum_{d=1}^{D} \theta_d x_d $  的线性预测器。如果对于任意维度  $ d $  有  $ \theta_d = 0 $，则对应的特征  $ x_d $  被忽略。这是一种特征选择形式，既能减少过拟合，也能提高模型的可解释性。通过惩罚  ℓ1  范数，我们可以鼓励权重变为零（而不仅仅是变小），

$$  \left|\left|\boldsymbol{\theta}\right|\right|_{1}=\sum_{d=1}^{D}\left|\boldsymbol{\theta}_{d}\right|   \tag*{(8.128)}$$

这被称为诱导稀疏性的正则化器。

为了理解它为何能诱导稀疏性，考虑两个可能的参数向量：一个稀疏向量  $ \boldsymbol{\theta} = (1, 0) $，以及一个非稀疏向量  $ \boldsymbol{\theta}' = (1/\sqrt{2}, 1/\sqrt{2}) $。两者具有相同的  ℓ2  范数

$$  \left|\left|(1,0)\right|\right|_{2}^{2}=\left|\left|(1/\sqrt{2},1/\sqrt{2})\right|\right|_{2}^{2}=1   \tag*{(8.129)}$$

因此  ℓ2  正则化（Section 4.5.3）不会偏好稀疏解而非稠密解。然而，当使用  ℓ1  正则化时，稀疏解的代价更低，因为

$$  \left|\left|(1,0)\right|\right|_{1}=1<\left|\left|(1/\sqrt{2},1/\sqrt{2})\right|\right|_{1}=\sqrt{2}   \tag*{(8.130)}$$

关于稀疏回归的更多细节见 Section 11.4。

如果将该正则化器与光滑损失结合，我们得到

$$  \mathcal{L}(\boldsymbol{\theta})=\mathrm{N L L}(\boldsymbol{\theta})+\lambda||\boldsymbol{\theta}||_{1}   \tag*{(8.131)}$$

我们可以使用近端梯度下降法优化该目标。关键问题在于如何计算函数  $ f(\boldsymbol{\theta}) = ||\boldsymbol{\theta}||_1 $  的近端算子。由于该函数可分解为各维度  $ d $，因此近端投影可以按分量计算。由式(8.120)，取  $ \eta = 1 $，我们有

$$  \mathrm{prox}_{\lambda f}(\theta)=\underset{z}{\arg\min}|z|+\frac{1}{2\lambda}(z-\theta)^{2}=\underset{z}{\arg\min}\lambda|z|+\frac{1}{2}(z-\theta)^{2}   \tag*{(8.132)}$$

在 Section 11.4.3 中，我们给出该问题的解为

$$  \mathrm{prox}_{\lambda f}(\theta)=\begin{cases}\theta-\lambda&if\theta\geq\lambda\\0&if|\theta|\leq\lambda\\\theta+\lambda&if\theta\leq-\lambda\end{cases}   \tag*{(8.133)}$$

这被称为软阈值算子，因为绝对值小于  $ \lambda $  的值以连续方式被设为零（阈值化）。注意，软阈值可以更紧凑地写为

$$   SoftThreshold(\theta,\lambda)=sign(\theta)\left(|\theta|-\lambda\right)_{+}   \tag*{(8.134)}$$

其中  $ \theta_{+} = \max(\theta, 0) $  是  $ \theta $  的正部。在向量情形下，我们逐元素执行该操作：

 $$  SoftThreshold(\boldsymbol{\theta},\lambda)=sign(\boldsymbol{\theta})\odot(|\boldsymbol{\theta}|-\lambda)_{+} $$ 

该方法在稀疏线性回归中的应用见 Section 11.4.9.3。

---

#### 8.6.3 量化的近端算子

在某些应用中（例如，训练深度神经网络以在内存受限的边缘设备（如手机）上运行时），我们希望确保参数被量化。例如，在极端情况下，每个参数只能取 -1 或 +1，那么状态空间变为 $ C = \{-1, +1\}^D $。

我们定义一个正则化项来衡量参数向量到其最近量化版本的距离：

$$  \mathcal{L}_{r}(\boldsymbol{\theta})=\inf_{\boldsymbol{\theta}_{0}\in\mathcal{C}}||\boldsymbol{\theta}-\boldsymbol{\theta}_{0}||_{1}   \tag*{(8.136)}$$

（也可使用 $ \ell_2 $ 范数。）对于 $ \mathcal{C} = \{-1, +1\}^D $ 的情况，上式变为

$$  \mathcal{L}_{r}(\boldsymbol{\theta})=\sum_{d=1}^{D}\inf_{[\theta_{0}]_{d}\in\{\pm1\}}|\theta_{d}-[\theta_{0}]_{d}|=\sum_{d=1}^{D}\min\{|\theta_{d}-1|,|\theta_{d}+1|\}=||\boldsymbol{\theta}-\mathrm{sign}(\boldsymbol{\theta})||_{1}   \tag*{(8.137)}$$

我们定义对应的量化算子为

$$  q(\boldsymbol{\theta})=\operatorname{proj}_{\mathcal{C}}(\boldsymbol{\theta})=\operatorname{argmin}\mathcal{L}_{r}(\boldsymbol{\theta})=\operatorname{sign}(\boldsymbol{\theta})   \tag*{(8.138)}$$

量化学习的核心困难在于量化不是一个可微操作。一个流行的解决方案是使用 **直通估计器**，它采用近似 $\frac{\partial \mathcal{L}}{\partial q(\theta)} \approx \frac{\partial \mathcal{L}}{\partial \theta}$（参见例如 [Yin+19]）。相应的更新可分为两步：首先在当前参数的量化版本处计算梯度向量，然后使用这个近似梯度更新无约束参数：

$$  \tilde{\boldsymbol{\theta}}_{t}=\operatorname{proj}_{\mathcal{C}}(\boldsymbol{\theta}_{t})=q(\boldsymbol{\theta}_{t})   \tag*{(8.139)}$$

$$  \boldsymbol{\theta}_{t+1}=\boldsymbol{\theta}_{t}-\boldsymbol{\eta}_{t}\nabla\mathcal{L}_{s}(\tilde{\boldsymbol{\theta}}_{t})   \tag*{(8.140)}$$

当应用于 $ C = \{-1, +1\}^D $ 时，这被称为 **二元连接方法** [CBD15]。

使用近端梯度下降可以得到更好的结果，其中我们将量化视为一个正则化项，而非硬约束；这被称为 **ProxQuant** [BWL19]。更新变为

$$  \tilde{\theta}_{t}=\mathrm{p r o x}_{\lambda\mathcal{L}_{r}}\left(\boldsymbol{\theta}_{t}-\boldsymbol{\eta}_{t}\nabla\mathcal{L}_{s}(\boldsymbol{\theta}_{t})\right)   \tag*{(8.141)}$$

在 $ \mathcal{C} = \{-1, +1\}^D $ 的情况下，可以证明近端算子是公式 (8.135) 中软阈值算子的推广：

$$  \begin{aligned}\mathrm{prox}_{\lambda\mathcal{L}_{r}}(\boldsymbol{\theta})&=SoftThreshold(\boldsymbol{\theta},\lambda,\mathrm{sign}(\boldsymbol{\theta}))\\&=\mathrm{sign}(\boldsymbol{\theta})+\mathrm{sign}(\boldsymbol{\theta}-\mathrm{sign}(\boldsymbol{\theta}))\odot(|\boldsymbol{\theta}-\mathrm{sign}(\boldsymbol{\theta})|-\lambda)_{+}\end{aligned}   \tag*{(8.142)}$$

这可以推广到其他形式的量化；详见 [Yin+19]。

#### 8.6.4 增量（在线）近端方法

许多机器学习问题的目标函数是每个样本损失之和。这类问题可以增量求解；这是在线学习的一个特例。可以将近端方法扩展到这种设置。关于这些方法的概率视角（从卡尔曼滤波角度），参见 [AEM18; Aky+19]。

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可证。

---

### 8.7 边界优化 *

本节讨论一类称为边界优化或MM算法的算法。在最小化问题中，MM代表上界-最小化（majorize-minimize）。在最大化问题中，MM代表下界-最大化（minorize-maximize）。我们将在8.7.2节讨论MM的一个特例，即期望最大化（EM）算法。

#### 8.7.1 通用算法

本节简要概述MM方法。（更多细节可参见例如[HL04; Mai15; SBP17; Nad+19]。）为与文献一致，假设我们的目标是最大化某个关于参数 $ \boldsymbol{\theta} $ 的函数 $ \ell(\boldsymbol{\theta}) $（如对数似然）。MM方法的基本思路是构造一个代理函数 $ Q(\boldsymbol{\theta}, \boldsymbol{\theta}^t) $，该函数是 $ \ell(\boldsymbol{\theta}) $ 的紧下界，满足 $ Q(\boldsymbol{\theta}, \boldsymbol{\theta}^t) \leq \ell(\boldsymbol{\theta}) $ 且 $ Q(\boldsymbol{\theta}^t, \boldsymbol{\theta}^t) = \ell(\boldsymbol{\theta}^t) $。若满足这些条件，则称 $ Q $ 是 $ \ell $ 的下界。随后我们执行如下更新步骤：

$$  \theta^{t+1}=\underset{\theta}{\operatorname{argmax}}Q(\theta,\theta^{t})   \tag*{(8.144)}$$

这保证了原始目标函数的单调递增：

$$  \ell(\boldsymbol{\theta}^{t+1})\geq Q(\boldsymbol{\theta}^{t+1},\boldsymbol{\theta}^{t})\geq Q(\boldsymbol{\theta}^{t},\boldsymbol{\theta}^{t})=\ell(\boldsymbol{\theta}^{t})   \tag*{(8.145)}$$

其中第一个不等式成立是因为对于任意 $ \pmb{\theta}^{\prime} $，$ Q(\pmb{\theta}^{t+1}, \pmb{\theta}^{\prime}) $ 是 $ \ell(\pmb{\theta}^{t+1}) $ 的下界；第二个不等式由式(8.144)得到；最后一个等式源自紧性条件。因此，若未观察到目标函数的单调递增，则数学推导和/或代码中必然存在错误——这是一个极其强大的调试工具。

该过程示意于Figure 8.23。红色虚线曲线为原始函数（例如观测数据的对数似然）。蓝色实线曲线为在 $ \theta^t $ 处求值的下界；该下界在 $ \theta^t $ 处与目标函数相切。随后将 $ \theta^{t+1} $ 设为下界（蓝色曲线）的最大值点，并在该点拟合一个新的下界（绿色点线曲线）。该新下界的最大值点成为 $ \theta^{t+2} $，依此类推。

若 $ Q $ 为二次下界，则整个方法类似于牛顿法，后者反复拟合并优化二次近似，如Figure 8.14(a)所示。区别在于，优化 $ Q $ 可保证目标函数改进（即使目标函数非凸），而牛顿法可能过冲或导致目标函数下降（如Figure 8.24所示），因其使用的是二次近似而非界。

#### 8.7.2 EM算法

本节讨论期望最大化（expectation maximization, EM）算法[DLR77; MK97]。该算法是一种边界优化算法，旨在针对含有缺失数据和/或隐变量的概率模型，计算最大似然估计（MLE）或最大后验估计（MAP）参数估计值。令 $ y_n $ 表示第 $ n $ 个样本的观测数据，$ z_n $ 表示其隐数据。

EM的基本思路是在E步（期望步）估计隐变量（或缺失值），然后在M步（最大化步）利用完全观测数据计算MLE。由于期望值依赖于参数，而参数又依赖于期望值，因此需要迭代进行该过程。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_462_125_706_333.jpg" alt="图像" width="21%" /></div>

<div style="text-align: center;">图 8.23：边界优化算法示意图。改编自 [Bis06] 的图 9.14。由 emLogLikelihoodMax.ipynb 生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_288_433_551_647.jpg" alt="图像" width="22%" /></div>

<div style="text-align: center;">(a) 过冲。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_605_430_867_646.jpg" alt="图像" width="22%" /></div>

<div style="text-align: center;">(b) 寻找错误的根。</div>

<div style="text-align: center;">图 8.24：MM 算法的二次下界（实线）与牛顿法的二次近似（虚线）叠加在经验密度估计（点线）上。两种算法的起始点均为圆圈。方块表示一次 MM 更新的结果，菱形表示一次牛顿更新的结果。(a) 牛顿法过冲全局最大值。(b) 牛顿法导致目标函数下降。来自 [FT05] 的图 4。经 Carlo Tomasi 许可使用。</div>

在第 8.7.2.1 节中，我们证明了 EM 是一种 MM 算法，这意味着该迭代过程将收敛到对数似然的局部极大值。收敛速度取决于缺失数据的数量，而缺失数据会影响边界的紧致性 [XJ96; MD97; SRG03; KKS20]。

##### 8.7.2.1 下界

EM 的目标是最大化观测数据的对数似然：

$$  \ell(\boldsymbol{\theta})=\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta})=\sum_{n=1}^{N}\log\left[\sum_{\boldsymbol{z}_{n}}p(\boldsymbol{y}_{n},\boldsymbol{z}_{n}|\boldsymbol{\theta})\right]   \tag*{(8.146)}$$

其中 $ y_{n} $ 是可见变量，$ z_{n} $ 是隐藏变量。不幸的是，这很难优化，因为对数不能直接放入求和内部。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

EM 通过以下方式解决该问题。首先，考虑一组关于每个隐变量 $z_n$ 的任意分布 $q_n(z_n)$。观测数据的对数似然可以写作：

$$  \ell(\boldsymbol{\theta})=\sum_{n=1}^{N}\log\left[\sum_{z_{n}}q_{n}(z_{n})\frac{p(\boldsymbol{y}_{n},z_{n}|\boldsymbol{\theta})}{q_{n}(z_{n})}\right]   \tag*{(8.147)}$$

利用 Jensen 不等式 (Equation (6.34))，我们可以将对数（一个凹函数）推入期望内部，从而得到对数似然的如下下界：

$$  \ell(\boldsymbol{\theta})\geq\sum_{n}\sum_{\boldsymbol{z}_{n}}q_{n}(\boldsymbol{z}_{n})\log\frac{p(\boldsymbol{y}_{n},\boldsymbol{z}_{n}|\boldsymbol{\theta})}{q_{n}(\boldsymbol{z}_{n})}   \tag*{(8.148)}$$

$$  =\sum_{n}\underbrace{\mathbb{E}_{q_{n}}\left[\log p(\boldsymbol{y}_{n},\boldsymbol{z}_{n}|\boldsymbol{\theta})\right]+\mathbb{H}(q_{n})}_{\boldsymbol{\Sigma}(\boldsymbol{\theta},q_{n})}   \tag*{(8.149)}$$

$$  =\sum_{n}\mathbb{L}(\boldsymbol{\theta},q_{n})\triangleq\mathbb{L}(\boldsymbol{\theta},\{q_{n}\})=\mathbb{L}(\boldsymbol{\theta},q_{1:N})   \tag*{(8.150)}$$

其中 $\mathbb{H}(q)$ 是概率分布 $q$ 的熵，而 $\mathbb{L}(\boldsymbol{\theta},\{q_n\})$ 被称为**证据下界**（evidence lower bound, ELBO），因为它是**对数边际似然** $\log p(\boldsymbol{y}_{1:N}|\boldsymbol{\theta})$（也称为证据）的下界。优化该下界是**变分推断**的基础，我们将在第 4.6.8.3 节中讨论。

##### 8.7.2.2 E步

我们看到，该下界是 N 项之和，每一项具有如下形式：

$$  \mathrm{E}(\boldsymbol{\theta},q_{n})=\sum_{z_{n}}q_{n}(z_{n})\log\frac{p(\boldsymbol{y}_{n},z_{n}|\boldsymbol{\theta})}{q_{n}(z_{n})}   \tag*{(8.151)}$$

$$  =\sum_{z_{n}}q_{n}(z_{n})\log\frac{p(z_{n}|\boldsymbol{y}_{n},\boldsymbol{\theta})p(\boldsymbol{y}_{n}|\boldsymbol{\theta})}{q_{n}(z_{n})}   \tag*{(8.152)}$$

$$  =\sum_{z_{n}}q_{n}(z_{n})\log\frac{p(z_{n}|\boldsymbol{y}_{n},\boldsymbol{\theta})}{q_{n}(z_{n})}+\sum_{z_{n}}q_{n}(z_{n})\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta})   \tag*{(8.153)}$$

$$  =-D_{\mathbb{K}\mathbb{L}}\left(q_{n}(z_{n})\mid p(z_{n}|\boldsymbol{y}_{n},\boldsymbol{\theta})\right)+\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta})   \tag*{(8.154)}$$

其中 $D_{\mathbb{K}\mathbb{L}}(q \parallel p) \triangleq \sum_z q(z) \log \frac{q(z)}{p(z)}$ 是概率分布 $q$ 与 $p$ 之间的 **Kullback-Leibler 散度**（简称 KL 散度）。我们将在第 6.2 节中更详细地讨论，但这里需要的关键性质是 $D_{\mathbb{K}\mathbb{L}}(q \parallel p) \geq 0$，且 $D_{\mathbb{K}\mathbb{L}}(q \parallel p) = 0$ 当且仅当 $q = p$。因此，我们可以通过将每个 $q_n$ 设置为 $q_n^* = p(\mathbf{z}_n|\mathbf{y}_n, \boldsymbol{\theta})$ 来最大化关于 $\{q_n\}$ 的下界 $\mathbf{L}(\boldsymbol{\theta}, \{q_n\})$。这称为 **E步**。这确保了 ELBO 是紧下界：

$$  \mathbb{L}(\boldsymbol{\theta},\{q_{n}^{*}\})=\sum_{n}\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta})=\ell(\boldsymbol{\theta})   \tag*{(8.155)}$$

为了理解这与边界优化的联系，我们定义

$$  Q(\boldsymbol{\theta},\boldsymbol{\theta}^{t})=\operatorname{L}(\boldsymbol{\theta},\{p(z_{n}|\boldsymbol{y}_{n};\boldsymbol{\theta}^{t})\})   \tag*{(8.156)}$$

---

那么我们有 $ Q(\boldsymbol{\theta}, \boldsymbol{\theta}^t) \leq \ell(\boldsymbol{\theta}) $ 和 $ Q(\boldsymbol{\theta}^t, \boldsymbol{\theta}^t) = \ell(\boldsymbol{\theta}^t) $，正如所要求的。

然而，如果我们无法精确计算后验 $p(z_n|y_n;\theta^t)$，我们仍然可以使用一个近似分布 $q(z_n|y_n;\theta^t)$；这将在对数似然上产生一个非紧的下界。这个广义版本的EM被称为变分EM [NH98]。详见本书的续篇 [Mur23]。

##### 8.7.2.3 M步

在M步中，我们需要关于 $ \boldsymbol{\theta} $ 最大化 $ \mathcal{L}(\boldsymbol{\theta},\{q_n^t\}) $，其中 $ q_n^t $ 是在第t次迭代的E步中计算得到的分布。由于熵项 $ \mathbb{H}(q_n) $ 关于 $ \boldsymbol{\theta} $ 是常数，因此在M步中我们可以忽略它们。我们剩下

$$  \ell^{t}(\boldsymbol{\theta})=\sum_{n}\mathbb{E}_{q_{n}^{t}(\boldsymbol{z}_{n})}\left[\log p(\boldsymbol{y}_{n},\boldsymbol{z}_{n}|\boldsymbol{\theta})\right]   \tag*{(8.157)}$$

这被称为期望完全数据对数似然。如果联合概率属于指数族（第3.4节），我们可以将其重写为

$$  \ell^{t}(\boldsymbol{\theta})=\sum_{n}\mathbb{E}\left[\mathcal{T}(\boldsymbol{y}_{n},\boldsymbol{z}_{n})^{\mathsf{T}}\boldsymbol{\theta}-A(\boldsymbol{\theta})\right]=\sum_{n}(\mathbb{E}\left[\mathcal{T}(\boldsymbol{y}_{n},\boldsymbol{z}_{n})\right]^{\mathsf{T}}\boldsymbol{\theta}-A(\boldsymbol{\theta}))   \tag*{(8.158)}$$

其中 $ \mathbb{E}\left[\mathcal{T}(y_n, z_n)\right] $ 被称为期望充分统计量。

在M步中，我们最大化期望完全数据对数似然，得到

$$  \theta^{t+1}=\arg\max_{\theta}\sum_{n}\mathbb{E}_{q_{n}^{t}}\left[\log p(\boldsymbol{y}_{n},\boldsymbol{z}_{n}|\boldsymbol{\theta})\right]   \tag*{(8.159)}$$

在指数族的情况下，可以通过匹配期望充分统计量的矩来闭式求解最大化问题。

从上述内容可以看出，E步实际上不需要返回完整的后验分布集 $ \{q(z_n)\} $，而只需返回期望充分统计量的和 $ \sum_n \mathbb{E}_{q(z_n)} [\mathcal{T}(y_n, z_n)] $。这将在下面的例子中变得更加清晰。

#### 8.7.3 示例：用于GMM的EM

在本节中，我们展示如何使用EM算法来计算高斯混合模型（GMM）参数的MLE和MAP估计。

##### 8.7.3.1 E步

E步简单地计算簇k对生成数据点n的责任，使用当前参数估计 $ \boldsymbol{\theta}^{(t)} $ 进行估计：

$$  r_{n k}^{(t)}=p^{*}(z_{n}=k|\boldsymbol{y}_{n},\boldsymbol{\theta}^{(t)})=\frac{\pi_{k}^{(t)}p(\boldsymbol{y}_{n}|\boldsymbol{\theta}_{k}^{(t)})}{\sum_{k^{\prime}}\pi_{k^{\prime}}^{(t)}p(\boldsymbol{y}_{n}|\boldsymbol{\theta}_{k^{\prime}}^{(t)})}   \tag*{(8.160)}$$

作者：Kevin P. Murphy。(C) MIT Press. CC-BY-NC-ND 许可证

---

##### 8.7.3.2 M步

M步最大化期望完整数据对数似然，其表达式为

$$  \ell^{t}(\boldsymbol{\theta})=\mathbb{E}\left[\sum_{n}\log p(z_{n}|\boldsymbol{\pi})+\sum_{n}\log p(\boldsymbol{y}_{n}|z_{n},\boldsymbol{\theta})\right]   \tag*{(8.161)}$$

$$  =\mathbb{E}\left[\sum_{n}\log\left(\prod_{k}\pi_{k}^{z_{nk}}\right)+\sum_{n}\log\left(\prod_{k}\mathcal{N}(\boldsymbol{y}_{n}|\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})^{z_{nk}}\right)\right]   \tag*{(8.162)}$$

$$  =\sum_{n}\sum_{k}\mathbb{E}\left[z_{nk}\right]\log\pi_{k}+\sum_{n}\sum_{k}\mathbb{E}\left[z_{nk}\right]\log\mathcal{N}(\boldsymbol{y}_{n}|\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})   \tag*{(8.163)}$$

$$  =\sum_{n}\sum_{k}r_{nk}^{(t)}\log(\pi_{k})-\frac{1}{2}\sum_{n}\sum_{k}r_{nk}^{(t)}\left[\log\left|\boldsymbol{\Sigma}_{k}\right|+(\boldsymbol{y}_{n}-\boldsymbol{\mu}_{k})^{\mathsf{T}}\boldsymbol{\Sigma}_{k}^{-1}(\boldsymbol{y}_{n}-\boldsymbol{\mu}_{k})\right]+\mathrm{const}   \tag*{(8.164)}$$

其中 $ z_{nk} = \mathbb{I}(z_n = k) $ 是类别值 $ z_n $ 的独热编码。该目标函数仅是计算多元正态分布（MVN）MLE的标准问题的加权形式（参见第4.2.6节）。可以证明，新的参数估计为

$$  \begin{aligned}\boldsymbol{\mu}_{k}^{(t+1)}&=\frac{\sum_{n}r_{nk}^{(t)}\boldsymbol{y}_{n}}{r_{k}^{(t)}}\\ \boldsymbol{\Sigma}_{k}^{(t+1)}&=\frac{\sum_{n}r_{nk}^{(t)}(\boldsymbol{y}_{n}-\boldsymbol{\mu}_{k}^{(t+1)})(\boldsymbol{y}_{n}-\boldsymbol{\mu}_{k}^{(t+1)})^{\mathsf{T}}}{r_{k}^{(t)}}\\ &=\frac{\sum_{n}r_{nk}^{(t)}\boldsymbol{y}_{n}\boldsymbol{y}_{n}^{\mathsf{T}}}{r_{k}^{(t)}}-\boldsymbol{\mu}_{k}^{(t+1)}(\boldsymbol{\mu}_{k}^{(t+1)})^{\mathsf{T}}\end{aligned}   \tag*{(8.166)}$$

其中 $ r_k^{(t)} \triangleq \sum_n r_{nk}^{(t)} $ 是分配给聚类 $ k $ 的加权点数。聚类 $ k $ 的均值仅是分配给该聚类的所有点的加权平均，协方差与加权经验散布矩阵成比例。

混合权重的M步是通常MLE的简单加权形式：

$$  \pi_{k}^{(t+1)}=\frac{1}{N}\sum_{n}r_{nk}^{(t)}=\frac{r_{k}^{(t)}}{N}   \tag*{(8.167)}$$

##### 8.7.3.3 示例

算法运行的一个示例如图8.25所示，其中我们用2分量高斯混合模型拟合了一些二维数据。该数据集来自[Bis06]，源自黄石国家公园（Yellowstone National Park）的老忠实间歇泉（Old Faithful geyser）的测量数据。具体来说，我们绘制了下次喷发的时间（分钟）与喷发持续时间（分钟）的关系图。数据在预处理前通过减去均值并除以标准差进行了标准化；这通常有助于收敛。我们从 $ \boldsymbol{\mu}_1 = (-1,1) $，$ \boldsymbol{\Sigma}_1 = \mathbf{I} $，$ \boldsymbol{\mu}_2 = (1,-1) $，$ \boldsymbol{\Sigma}_2 = \mathbf{I} $ 开始。然后我们在不同迭代次数下展示了聚类分配及相应的混合成分。

关于将高斯混合模型应用于聚类的更多细节，参见第21.4.1节。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_374_126_795_399.jpg" alt="图" width="36%" /></div>


<div style="text-align: center;">图8.25：对老忠实泉数据应用GMM的EM算法示意图。红色深浅表示数据点属于红色聚类的程度，蓝色同理；紫色点表示其责任值在两个聚类间大致为50/50。改编自[Bis06]图9.8。由mix_gauss_demo_faithful.ipynb生成。</div>


##### 8.7.3.4 最大后验估计

计算GMM的最大似然估计常会遇到数值问题和过拟合。原因在于，为简化起见，假设对所有$k$有$ \boldsymbol{\Sigma}_k = \sigma_k^2 \mathbf{I} $。若将某个中心（例如$ \boldsymbol{\mu}_k $）赋给单个数据点（例如$ \boldsymbol{y}_n $），则可能得到无限大的似然，因为该数据点的似然为

$$  \mathcal{N}(\boldsymbol{y}_{n}|\boldsymbol{\mu}_{k}=\boldsymbol{y}_{n},\sigma_{k}^{2}\mathbf{I})=\frac{1}{\sqrt{2\pi\sigma_{k}^{2}}}e^{0}   \tag*{(8.168)}$$

因此，通过令$ \sigma_k \to 0 $可使该项趋于无穷，如图8.26(a)所示。我们将此称为“方差坍缩问题”。

一个简单的解决方案是采用MAP估计。幸运的是，我们仍可使用EM来求此MAP估计。现在我们的目标是最大化期望的完整数据对数似然加上对数先验：

$$  \ell^{t}(\boldsymbol{\theta})=\left[\sum_{n}\sum_{k}r_{nk}^{(t)}\log\pi_{nk}+\sum_{n}\sum_{k}r_{nk}^{(t)}\log p(\boldsymbol{y}_{n}|\boldsymbol{\theta}_{k})\right]+\log p(\boldsymbol{\pi})+\sum_{k}\log p(\boldsymbol{\theta}_{k})   \tag*{(8.169)}$$

注意E步保持不变，但M步需作修改，下面进行说明。对于混合权重的先验，自然采用狄利克雷先验（第4.6.3.2节）$ \pi \sim \text{Dir}(\alpha) $，因其与类别分布共轭。MAP估计为

$$  \tilde{\pi}_{k}^{(t+1)}=\frac{r_{k}^{(t)}+\alpha_{k}-1}{N+\sum_{k}\alpha_{k}-K}   \tag*{(8.170)}$$

若采用均匀先验$ \alpha_{k}=1 $，则退化为MLE。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_260_142_500_324.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_654_142_907_334.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 8.26: (a) 高斯混合模型（GMM）似然函数中奇异值如何出现的示意图。这里 K = 2，但第一个混合分量是一个以单个数据点 $ x_1 $ 为中心的窄尖峰（$ \sigma_1 \approx 0 $）。改编自 [Bis06] 的图 9.7。由 mix_gauss_singularity.ipynb 生成。(b) 拟合高斯混合模型时 MAP 估计相对于 ML 估计优势的示意图。我们绘制了每种方法在 5 次随机试验中出现数值问题的比例与问题维度的关系，样本数 N = 100。实红线（上方曲线）：MLE。虚黑线（下方曲线）：MAP。由 mix_gauss_mle_vs_map.ipynb 生成。</div>


对于混合分量的先验，我们考虑如下形式的共轭先验

$$  p(\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})=\mathrm{NIW}(\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k}|\breve{m},\breve{\kappa},\breve{\nu},\breve{\mathbf{S}})   \tag*{(8.171)}$$

这被称为正态-逆威沙特分布（详见本书续作 [Mur23]）。假设我们将 $ \mu $ 的超参数设为 $ \tilde{\kappa}=0 $，使得 $ \mu_k $ 不受正则化影响；因此先验仅影响我们对 $ \Sigma_k $ 的估计。在这种情况下，MAP 估计由下式给出

$$  \tilde{\mu}_{k}^{(t+1)}=\hat{\mu}_{k}^{(t+1)}   \tag*{(8.172)}$$

$$  \tilde{\mathbf{\Sigma}}_{k}^{(t+1)}=\frac{\mathbf{\check{S}}+\hat{\mathbf{\Sigma}}_{k}^{(t+1)}}{\breve{\nu}+r_{k}^{(t)}+D+2}   \tag*{(8.173)}$$

其中 $ \hat{\mu}_k $ 是方程 (8.165) 中 $ \mu_k $ 的 MLE，$ \tilde{\Sigma}_k $ 是方程 (8.166) 中 $ \Sigma_k $ 的 MLE。现在我们讨论如何设置先验协方差 $ \check{S} $。一种可能性（见 [FR07, p163]）是使用

$$  \breve{\mathbf{S}}=\frac{1}{K^{2/D}}\mathrm{diag}(s_{1}^{2},\ldots,s_{D}^{2})   \tag*{(8.174)}$$

其中 $  s_d^2 = (1/N) \sum_{n=1}^N (x_{nd} - \overline{x}_d)^2  $ 是维度 $ d $ 的合并方差。参数 $ \breve{\nu} $ 控制我们对这一先验的置信程度。在保证先验正则的前提下，我们能使用的最弱先验是设置 $ \breve{\nu} = D + 2 $，因此这是一个常见选择。

现在我们说明在 GMM 中使用 MAP 估计而非 ML 估计的优势。我们对 D 维空间中 $ N = 100 $ 个样本的合成数据应用 EM 算法，分别使用 ML 或 MAP 估计。若出现涉及奇异矩阵的数值问题，则将该次试验计为“失败”。对每个维度，我们进行 5 次随机试验。结果如图 8.26(b) 所示。我们看到，一旦 D 变得稍大，ML 估计就会彻底失败，而使用适当先验的 MAP 估计则很少遇到数值问题。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_242_120_518_340.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_674_117_907_334.jpg" alt="图像" width="20%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 8.27：左图：从一维两个高斯混合中采样的 N = 200 个数据点，其中 $ \pi_k = 0.5 $，$ \sigma_k = 5 $，$ \mu_1 = -10 $ 且 $ \mu_2 = 10 $。右图：似然曲面 $ p(\mathcal{D}|\mu_1, \mu_2) $，所有其他参数均设为真值。我们看到两个对称的模态，反映了参数不可辨识性。由 qmm_lik_surface_plot.ipynb 生成。</div>

##### 8.7.3.5 NLL 的非凸性

混合模型的似然函数为：

$$  \ell(\boldsymbol{\theta})=\sum_{n=1}^{N}\log\left[\sum_{z_{n}=1}^{K}p(\boldsymbol{y}_{n},z_{n}|\boldsymbol{\theta})\right]   \tag*{(8.175)}$$

通常情况下，该函数存在多个模态，因此不存在唯一的全局最优。

图 8.27 以一维两个高斯混合为例说明了这一点。我们看到存在两个同样好的全局最优，分别对应于聚类的两种不同标签分配：一种左侧峰对应 z = 1，另一种左侧峰对应 z = 2。这称为**标签切换问题**；详见第 21.4.1.2 节。

似然函数中到底有多少个模态很难回答。共有 $ K! $ 种可能的标签分配，但某些峰可能会合并，具体取决于 $ \mu_k $ 之间的间距。尽管如此，模态数量仍可能是指数级的。因此，找到任何全局最优都是 NP 难的 [Alo+09; Dri+04]。我们只能满足于找到局部最优。为了找到良好的局部最优，可以使用 $ K\text{means++} $（第 21.3.4 节）来初始化 EM。

### 8.8 黑箱优化与无导数优化

在某些优化问题中，目标函数是一个黑箱，即其函数形式未知。这意味着我们无法使用基于梯度的方法对其进行优化。相反，解决此类问题需要**黑箱优化**（BBO）方法，也称为**无导数优化**（DFO）。

在机器学习中，这类问题通常出现在进行模型选择时。例如，假设我们有一些超参数 $ \boldsymbol{\lambda} \in \boldsymbol{\Lambda} $，它们控制模型的类型或复杂度。我们常将目标函数 $ \mathcal{L}(\boldsymbol{\lambda}) $ 定义为验证集上的损失（参见第 4.5.4 节）。由于验证损失依赖于通过复杂

---

算法中，该目标函数实际上是一个黑箱。$ ^{4} $

解决此类问题的一个简单方法是使用网格搜索，即评估参数空间中的每个点，并选择损失最低的点。不幸的是，由于维数灾难，这种方法无法扩展到高维空间。此外，即使在低维空间中，若评估黑箱目标的代价高昂（例如，需要先训练模型再计算验证损失），这种方式也可能非常昂贵。针对这一问题，已有多种解决方案被提出。详见本书的后续部分[Mur23]。

### 8.9 练习

练习8.1 [铰链损失函数的次梯度 $ \dagger $]

设 $ f(x) = (1 - x)_{+} $ 为铰链损失函数，其中 $ (z)_{+} = \max(0, z) $。求 $ \partial f(0) $、$ \partial f(1) $ 和 $ \partial f(2) $。

练习8.2 [Student分布的EM算法]

推导用于计算多元Student分布最大似然估计的EM方程。分别考虑自由度参数已知和未知的情况。提示：将Student分布写为高斯尺度混合形式。