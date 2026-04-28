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

通过对编码器输出的嵌入向量应用聚类算法（如k-means）。此外，在学习浅层[Roz+19]或图卷积[Chi+19a; CEL19]嵌入模型时，聚类可以与学习算法相结合。

##### 23.6.1.4 可视化

有许多现成的工具可以将图节点映射到二维流形上以实现可视化。可视化使网络科学家能够定性理解图的性质、节点间的关系或节点簇的分布。流行的工具包括基于力导向布局的方法，并有多种网页应用JavaScript实现。

无监督图嵌入方法也用于可视化目的：首先训练一个编码器-解码器模型（对应于浅层嵌入或图卷积网络），然后使用t-SNE（第20.4.10节）或PCA（第20.1节）将每个节点表示映射到二维空间。这种过程（嵌入→降维）通常用于定性评估图学习算法的性能。如果节点具有属性，可以利用这些属性在二维可视化图中为节点着色。优秀的嵌入算法会将具有相似属性的节点嵌入到邻近的位置，如各种方法的可视化所示[PARS14; KW16a; AEH+18]。最后，除了将每个节点映射到二维坐标外，将每个图映射到表示[ARZP19]的方法同样可以投影到二维空间，以可视化和定性分析图级别的性质。

#### 23.6.2 监督应用

本节讨论常见的监督应用。

##### 23.6.2.1 节点分类

节点分类是一项重要的监督图应用，其目标是学习能够准确预测节点标签的节点表示。（这有时被称为\textbf{统计}关系学习[GT07]。）例如，节点标签可以是引文网络中的科学主题，或社交网络中的性别及其他属性。

由于对大型图进行标注可能耗时且昂贵，半监督节点分类是一种特别常见的应用。在半监督设置中，仅一部分节点具有标签，目标是利用节点之间的链接来预测未标注节点的属性。这一设置是直推式的，因为只有一个部分标注的固定图。也可以进行归纳式节点分类，这对应于对多个图中的节点进行分类的任务。

注意，如果节点特征对目标标签具有描述性，则可以显著提升节点分类任务的性能。事实上，近年来的方法如GCN（第23.4.2节）、GraphSAGE（第23.4.3.1节）在多个节点分类基准上取得了最佳性能，因为它们能够结合结构信息和来自特征的语义信息。另一方面，其他方法如图上的随机游走无法利用特征信息，因此在这些任务上性能较低。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_114_948_266.jpg" alt="Image" width="62%" /></div>


<div style="text-align: center;">图23.9：结构相似的分子不一定具有相似的气味描述符。(A) Lyral，参考分子。(B) 结构相似的分子可以共享相似的气味描述符。(C) 然而，微小的结构变化可能使分子无味。(D) 进一步，较大的结构变化可能使分子的气味基本保持不变。摘自 [SL+19] 的图1，原图来自 [OPK12]。经 Benjamin Sanchez-Lengeling 友好许可使用。</div>


##### 23.6.2.2 图分类

图分类是一种监督学习应用，其目标是预测图的标签。图分类问题是归纳式的，一个常见的例子是对化合物进行分类（例如，根据分子预测毒性或气味，如图23.9所示）。

图分类需要某种池化的概念，以便将节点级信息聚合为图级信息。如前所述，将这种池化概念推广到任意图并非易事，因为图结构缺乏规则性，这使得图池化成为一个活跃的研究领域。除了上述监督方法外，还提出了一些用于学习图级表示的无监督方法 [Tsi+18; ARZP19; TMP20]。

---

# A 符号约定

### A.1 引言

要提出一套单一且一致的符号体系来涵盖本书中讨论的各种数据、模型和算法是非常困难的。此外，不同领域（如机器学习、统计和优化）之间的惯例各不相同，同一领域内的不同书籍和论文之间也存在差异。尽管如此，我们仍尽量保持一致性。下面我们总结了本书中使用的大部分符号，尽管个别章节可能会有新的符号引入。另外需要注意的是，同一个符号可能根据上下文具有不同的含义，尽管我们尽量避免这种情况。

### A.2 常用数学符号

下面列出一些常见符号。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \infty $</td><td style='text-align: center; word-wrap: break-word;'>无穷大</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \rightarrow $</td><td style='text-align: center; word-wrap: break-word;'>趋向于，例如 $ n \rightarrow \infty $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \propto $</td><td style='text-align: center; word-wrap: break-word;'>与...成正比，因此 $ y = ax $ 可以写作 $ y \propto x $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \triangleq $</td><td style='text-align: center; word-wrap: break-word;'>定义为</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ O(\cdot) $</td><td style='text-align: center; word-wrap: break-word;'>大 O 符号：大致表示数量级</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbb{Z}_{+} $</td><td style='text-align: center; word-wrap: break-word;'>正整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbb{R} $</td><td style='text-align: center; word-wrap: break-word;'>实数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbb{R}_{+} $</td><td style='text-align: center; word-wrap: break-word;'>正实数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{S}_{K} $</td><td style='text-align: center; word-wrap: break-word;'>$K$ 维概率单纯形</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{S}_{++}^{D} $</td><td style='text-align: center; word-wrap: break-word;'>$D \times D$ 正定矩阵锥</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \approx $</td><td style='text-align: center; word-wrap: break-word;'>约等于</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \{1,\ldots,N\} $</td><td style='text-align: center; word-wrap: break-word;'>有限集合 $ \{1,2,\ldots,N\} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1 :  $ N $</td><td style='text-align: center; word-wrap: break-word;'>有限集合 $ \{1,2,\ldots,N\} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ [\ell,u] $</td><td style='text-align: center; word-wrap: break-word;'>连续区间 $ \{\ell \leq x \leq u\} $</td></tr></table>

---

### A.3 函数

通用函数用 $f$（有时也用 $g$ 或 $h$）表示。我们会遇到许多具名函数，例如 $\tanh(x)$ 或 $\sigma(x)$。标量函数作用于向量时，假定为逐元素应用，例如 $\mathbf{x}^2 = [x_1^2, \ldots, x_D^2]$。泛函（函数的函数）使用黑板字体书写，例如用 $\mathbb{H}(p)$ 表示分布 $p$ 的熵。由固定参数 $\boldsymbol{\theta}$ 参数化的函数表示为 $f(\mathbf{x};\boldsymbol{\theta})$，有时也写作 $f_{\boldsymbol{\theta}}(\mathbf{x})$。下面列出一些常见函数（无自由参数）。

### A.3.1 单参数常见函数

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ [x] $</td><td style='text-align: center; word-wrap: break-word;'>$x$ 的向下取整，即向下舍入到最近的整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ [x] $</td><td style='text-align: center; word-wrap: break-word;'>$x$ 的向上取整，即向上舍入到最近的整数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \neg a $</td><td style='text-align: center; word-wrap: break-word;'>逻辑非</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbb{I}(x) $</td><td style='text-align: center; word-wrap: break-word;'>指示函数，若 $x$ 为真则 $\mathbb{I}(x)=1$，否则 $\mathbb{I}(x)=0$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \delta(x) $</td><td style='text-align: center; word-wrap: break-word;'>狄拉克 delta 函数，若 $x=0$ 则 $\delta(x)=\infty$，否则 $\delta(x)=0$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ |x| $</td><td style='text-align: center; word-wrap: break-word;'>绝对值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ |\mathcal{S}| $</td><td style='text-align: center; word-wrap: break-word;'>集合的大小（基数）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ n! $</td><td style='text-align: center; word-wrap: break-word;'>阶乘函数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \log(x) $</td><td style='text-align: center; word-wrap: break-word;'>$x$ 的自然对数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \exp(x) $</td><td style='text-align: center; word-wrap: break-word;'>指数函数 $e^{x}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Gamma(x) $</td><td style='text-align: center; word-wrap: break-word;'>伽马函数，$\Gamma(x)=\int_{0}^{\infty} u^{x-1} e^{-u} du$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Psi(x) $</td><td style='text-align: center; word-wrap: break-word;'>双伽马函数，$\Psi(x)=\frac{d}{dx} \log \Gamma(x)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \sigma(x) $</td><td style='text-align: center; word-wrap: break-word;'>Sigmoid（Logistic）函数，$\frac{1}{1 + e^{-x}}$</td></tr></table>

### A.3.2 双参数常见函数

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a \wedge b</td><td style='text-align: center; word-wrap: break-word;'>逻辑与</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a \vee b</td><td style='text-align: center; word-wrap: break-word;'>逻辑或</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B(a,b)</td><td style='text-align: center; word-wrap: break-word;'>Beta 函数，$B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \binom{n}{k} $</td><td style='text-align: center; word-wrap: break-word;'>二项式系数，等于 $n!/(k!(n-k)!)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \delta_{ij} $</td><td style='text-align: center; word-wrap: break-word;'>克罗内克 delta，等于 $\mathbb{I}(i=j)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \boldsymbol{u} \odot \boldsymbol{v} $</td><td style='text-align: center; word-wrap: break-word;'>两个向量的逐元素乘积</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \boldsymbol{u} \circledast \boldsymbol{v} $</td><td style='text-align: center; word-wrap: break-word;'>两个向量的卷积</td></tr></table>

### A.3.3 多参数（>2）常见函数

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B( $ \mathbf{x} $)</td><td style='text-align: center; word-wrap: break-word;'>多元 Beta 函数，$\frac{\prod_{k}\Gamma(x_{k})}{\Gamma(\sum_{k}x_{k})}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \Gamma(\mathbf{x}) $</td><td style='text-align: center; word-wrap: break-word;'>多元伽马函数，$\pi^{D(D-1)/4}\prod_{d=1}^{D}\Gamma(x+(1-d)/2)$</td></tr></table>

“Probabilistic Machine Learning: An Introduction”. 在线版本。2024年11月23日。

---

$$ \begin{array}{r l}{\operatorname{s o f t m a x}(\pmb{x})}&{{}\operatorname{S o f t m a x~f u n c t i o n},[\frac{e^{x_{c}}}{\sum_{c^{\prime}=1}^{C}e^{x_{c^{\prime}}}}]_{c=1}^{C}}\end{array} $$ 

### A.4 线性代数

在本节中，我们总结了用于线性代数的符号（详见第7章）。

### A.4.1 通用符号

向量使用粗体小写字母表示，如 **x**、**w**。矩阵使用粗体大写字母表示，如 **X**、**W**。标量使用非粗体小写字母。当从 N 个标量列表创建向量时，我们写作 $ \boldsymbol{x} = [x_1, \ldots, x_N] $；这可以是列向量或行向量，具体取决于上下文（除非另有说明，否则向量默认为列向量）。当从向量列表创建 $ M \times N $ 矩阵时，如果按列堆叠，我们写作 $ \boldsymbol{X} = [x_1, \ldots, x_N] $；如果按行堆叠，则写作 $ \boldsymbol{X} = [x_1; \ldots; x_M] $。

### A.4.2 向量

以下是一些向量运算的标准符号。（假设 **u** 和 **v** 均为 N 维向量。）

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{u}^{\top}\mathbf{v} $</td><td style='text-align: center; word-wrap: break-word;'>内积（标量积），$ \sum_{i=1}^{N} u_{i} v_{i} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{u}\mathbf{v}^{\top} $</td><td style='text-align: center; word-wrap: break-word;'>外积（$ N \times N $ 矩阵）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{u} \odot \mathbf{v} $</td><td style='text-align: center; word-wrap: break-word;'>逐元素乘积，$ [u_{1}v_{1}, \ldots, u_{N}v_{N}] $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{v}^{\top} $</td><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{v} $ 的转置</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \text{dim}(\mathbf{v}) $</td><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{v} $ 的维度（即 $ N $）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \text{diag}(\mathbf{v}) $</td><td style='text-align: center; word-wrap: break-word;'>由向量 $ \mathbf{v} $ 构成的对角 $ N \times N $ 矩阵</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{1} $ 或 $ \mathbf{1}_{N} $</td><td style='text-align: center; word-wrap: break-word;'>全1向量（长度为 $ N $）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{0} $ 或 $ \mathbf{0}_{N} $</td><td style='text-align: center; word-wrap: break-word;'>全0向量（长度为 $ N $）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ ||\mathbf{v}|| = ||\mathbf{v}||_{2} $</td><td style='text-align: center; word-wrap: break-word;'>欧几里得范数或 $ \ell_{2} $ 范数 $ \sqrt{\sum_{i=1}^{N} v_{i}^{2}} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ ||\mathbf{v}||_{1} $</td><td style='text-align: center; word-wrap: break-word;'>$ \ell_{1} $ 范数 $ \sum_{i=1}^{N} |v_{i}| $</td></tr></table>

### A.4.3 矩阵

以下是一些矩阵的标准符号。（假设 $ \mathbf{S} $ 是 $ N \times N $ 方阵，$ \mathbf{X} $ 和 $ \mathbf{Y} $ 的大小为 $ M \times N $，$ \mathbf{Z} $ 的大小为 $ M' \times N' $。）

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>符号</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{X}_{:,j} $</td><td style='text-align: center; word-wrap: break-word;'>矩阵的第 $ j $ 列</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{X}_{i,:,} $</td><td style='text-align: center; word-wrap: break-word;'>矩阵的第 $ i $ 行（视为列向量）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ X_{ij} $</td><td style='text-align: center; word-wrap: break-word;'>矩阵的 $ (i,j) $ 元素</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathbf{S} \succ 0 $</td><td style='text-align: center; word-wrap: break-word;'>当且仅当 $ \mathbf{S} $ 是正定矩阵时为真</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \operatorname{tr}(\mathbf{S}) $</td><td style='text-align: center; word-wrap: break-word;'>方阵的迹</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \det(\mathbf{S}) $</td><td style='text-align: center; word-wrap: break-word;'>方阵的行列式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ |\mathbf{S}| $</td><td style='text-align: center; word-wrap: break-word;'>方阵的行列式</td></tr></table>

---

$ S^{-1} $ 方阵的逆
$ X^{\dagger} $ 矩阵的伪逆
$ X^{T} $ 矩阵的转置
diag(S) 从方阵中提取的对角向量
I 或 $ I_{N} $ 大小为 $ N \times N $ 的单位矩阵
$ X \odot Y $ 逐元素乘积
$ X \otimes Z $ 克罗内克积（参见第7.2.5节）

### A.4.4 矩阵微积分

在本节中，我们总结用于矩阵微积分的符号（详见第7.8节）。设 $ \boldsymbol{\theta} \in \mathbb{R}^N $ 是一个向量，$ f : \mathbb{R}^N \to \mathbb{R} $ 是一个标量值函数。$ f $ 关于其自变量的导数记作：

$$  \nabla_{\boldsymbol{\theta}}f(\boldsymbol{\theta})\triangleq\nabla f(\boldsymbol{\theta})\triangleq\nabla f\triangleq\left(\begin{array}{l l l l}{\frac{\partial f}{\partial\theta_{1}}}&{\cdots}&{\frac{\partial f}{\partial\theta_{N}}}\end{array}\right)   \tag*{(A.1)}$$

梯度是一个向量，必须在空间中的某点处求值。为强调这一点，我们有时会写：

$$  g_{t}\triangleq g(\boldsymbol{\theta}_{t})\triangleq\nabla f(\boldsymbol{\theta})\bigg|_{\boldsymbol{\theta}_{t}}   \tag*{(A.2)}$$

我们还可以计算（对称的）$ N \times N $ 二阶偏导数矩阵，称为海森矩阵：

$$  \nabla^{2}f\triangleq\begin{pmatrix}\frac{\partial^{2}f}{\partial\theta_{1}^{2}}&\cdots&\frac{\partial^{2}f}{\partial\theta_{1}\partial\theta_{N}}\\&\vdots&\\ \frac{\partial^{2}f}{\partial\theta_{N}\theta_{1}}&\cdots&\frac{\partial^{2}f}{\partial\theta_{N}^{2}}\end{pmatrix}   \tag*{(A.3)}$$

海森矩阵是一个矩阵，必须在空间中的某点处求值。为强调这一点，我们有时会写：

$$  \mathbf{H}_{t}\triangleq\mathbf{H}(\boldsymbol{\theta}_{t})\triangleq\nabla^{2}f(\boldsymbol{\theta})\bigg|_{\boldsymbol{\theta}_{t}}   \tag*{(A.4)}$$

### A.5 优化

在本节中，我们总结用于优化的符号（详见第8章）。

我们常将希望最小化的目标函数或代价函数写作 $ \mathcal{L}(\boldsymbol{\theta}) $，其中 $ \boldsymbol{\theta} $ 为待优化变量（通常视为统计模型的参数）。我们将达到最小值的参数值记为 $ \boldsymbol{\theta}_* = \arg\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \mathcal{L}(\boldsymbol{\theta}) $，其中 $ \boldsymbol{\Theta} $ 是我们进行优化的集合。（注意，可能存在多个这样的最优值，因此更准确的写法应为 $ \boldsymbol{\theta}_* \in \arg\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \mathcal{L}(\boldsymbol{\theta}) $。）

在进行迭代优化时，我们用 $t$ 表示迭代次数。使用 $\eta$ 作为步长（学习率）参数。因此，梯度下降算法（详见第8.4节）可写为：$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta_t \boldsymbol{g}_t$。

---

我们经常使用帽子符号来表示估计或预测（例如，$ \hat{\theta} $，$ \hat{y} $），使用星号下标或上标表示真实（但通常未知）的值（例如，$ \theta_* $ 或 $ \theta^* $），使用上划线表示均值（例如，$ \overline{\theta} $）。

### A.6 概率

在本节中，我们总结概率论中使用的符号（详见第2章）。

我们用 p 表示概率密度函数（pdf）或概率质量函数（pmf），用 P 表示累积分布函数（cdf），用 Pr 表示二元事件的概率。我们写 $ p(X) $ 表示随机变量 X 的分布，写 $ p(Y) $ 表示随机变量 Y 的分布——即使在这两种情况下我们使用了相同的符号 p，它们指的是不同的分布。（在可能引起混淆的情况下，我们写作 $ p_X(\cdot) $ 和 $ p_Y(\cdot) $。）对分布 p 的近似通常用 q 表示，有时也用 $ \hat{p} $。

在某些情况下，我们区分随机变量（rv）及其可能取的值。此时，变量用大写字母表示（例如，X），其值用小写字母表示（例如，x）。然而，我们常常忽略变量与值之间的这种区别。例如，我们有时写 $ p(x) $ 来表示标量值（在某点评估的分布）或分布本身，具体取决于 X 是否被观测到。

我们写 $ X \sim p $ 表示 X 服从分布 p。我们写 $ X \perp Y $ | $ Z $ 表示在给定 Z 的条件下，X 与 Y 条件独立。如果 $ X \sim p $，我们用下式表示 $ f(X) $ 的期望值：

$$ \mathbb{E}\left[f(X)\right]=\mathbb{E}_{p(X)}\left[f(X)\right]=\mathbb{E}_{X}\left[f(X)\right]=\int_{x}f(x)p(x)d x \tag*{(A.5)}$$

如果 f 是恒等函数，我们写作 $ \overline{X} \triangleq \mathbb{E}[X] $。类似地，方差表示为：

$$ \mathbb{V}\left[f(X)\right]=\mathbb{V}_{p(X)}\left[f(X)\right]=\mathbb{V}_{X}\left[f(X)\right]=\int_{x}(f(x)-\mathbb{E}\left[f(X)\right])^{2}p(x)d x \tag*{(A.6)}$$

如果 x 是随机向量，协方差矩阵表示为：

$$ \mathrm{Cov}\left[\boldsymbol{x}\right]=\mathbb{E}\left[\left(\boldsymbol{x}-\overline{\boldsymbol{x}}\right)\left(\boldsymbol{x}-\overline{\boldsymbol{x}}\right)^{\mathrm{T}}\right] \tag*{(A.7)}$$

如果 $ X \sim p $，分布的众数表示为：

$$ \hat{x}=mode\left[p\right]=\underset{x}{\operatorname{argmax}}p(x) \tag*{(A.8)}$$

我们用 $p(\boldsymbol{x}|\boldsymbol{\theta})$ 表示参数化分布，其中 $\boldsymbol{x}$ 是随机变量，$\boldsymbol{\theta}$ 是参数，$p$ 是 pdf 或 pmf。例如，$\mathcal{N}(x|\mu,\sigma^{2})$ 是均值为 $\mu$、标准差为 $\sigma$ 的高斯（正态）分布。

### A.7 信息论

在本节中，我们总结信息论中使用的符号（详见第6章）。

如果 $ X \sim p $，我们用 $ \mathbb{H}(X) $ 或 $ \mathbb{H}(p) $ 表示分布的（微分）熵。如果 $ Y \sim q $，我们用 $ D_{\mathbb{K}\mathbb{L}}(p \parallel q) $ 表示从分布 p 到 q 的 KL 散度。如果 $ (X, Y) \sim p $，我们用 $ \mathbb{I}(X; Y) $ 表示 X 与 Y 之间的互信息。

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可协议。

---

### A.8 统计学与机器学习

我们简要总结一下用于统计学习的符号。

### A.8.1 监督学习

在监督学习中，我们将观测到的特征（也称为输入或协变量）记为 $\boldsymbol{x} \in \mathcal{X}$。通常 $\mathcal{X} = \mathbb{R}^D$，即特征为实数值。（注意，这包含了离散值输入的情况，可以用独热向量表示。）有时我们会手动指定输入的特征；我们将这些特征记为 $\phi(\boldsymbol{x})$。我们还有希望预测的输出（也称为目标或响应变量）$\boldsymbol{y} \in \mathcal{Y}$。我们的任务是学习一个条件概率分布 $p(\boldsymbol{y}|\boldsymbol{x}, \boldsymbol{\theta})$，其中 $\boldsymbol{\theta}$ 是模型参数。如果 $\mathcal{Y} = \{1, \ldots, C\}$，我们称之为**分类**。如果 $\mathcal{Y} = \mathbb{R}^C$，我们称之为**回归**（通常 $C = 1$，即仅预测标量响应）。

参数 $\theta$ 从训练数据中估计，训练数据记为 $\mathcal{D} = \{(\mathbf{x}_n, \mathbf{y}_n) : n \in \{1, \ldots, N\}\}$（因此 $N$ 是训练样本数）。如果 $\mathcal{X} = \mathbb{R}^D$，我们可以将训练输入存储在一个 $N \times D$ 的设计矩阵 $\mathbf{X}$ 中。如果 $\mathcal{Y} = \mathbb{R}^C$，我们可以将训练输出存储在一个 $N \times C$ 的矩阵 $\mathbf{Y}$ 中。如果 $\mathcal{Y} = \{1, \ldots, C\}$，我们可以将每个类标签表示为一个 $C$ 维的位向量，其中仅有一个元素为1（这被称为独热编码），因此我们可以将训练输出存储在一个 $N \times C$ 的二进制矩阵 $\mathbf{Y}$ 中。

### A.8.2 无监督学习与生成模型

无监督学习通常被形式化为无条件密度估计问题，即建模 $p(\boldsymbol{x}|\boldsymbol{\theta})$。在某些情况下，我们希望进行条件密度估计；我们将条件变量记为 $\boldsymbol{u}$，于是模型变为 $p(\boldsymbol{x}|\boldsymbol{u},\boldsymbol{\theta})$。这与监督学习类似，区别在于 $\boldsymbol{x}$ 通常是高维的（例如图像），而 $\boldsymbol{u}$ 通常是低维的（例如类别标签或文本描述）。

在某些模型中，我们包含潜在变量，也称为隐变量，它们在训练数据中从未被观测到。我们将这类模型称为**潜在变量模型**（LVM）。我们将第 $n$ 个数据样本的潜在变量记为 $z_n \in \mathcal{Z}$。有时潜在变量也被称为隐变量，记作 $h_n$。相反，可见变量记作 $v_n$。通常潜在变量是连续或离散的，即 $\mathcal{Z} = \mathbb{R}^L$ 或 $\mathcal{Z} = \{1, \ldots, K\}$。

大多数潜在变量模型的形式为 $p(\boldsymbol{x}_{n}, \boldsymbol{z}_{n}|\boldsymbol{\theta})$；这类模型可用于无监督学习。然而，潜在变量模型也可用于监督学习。具体而言，我们可以构建一个生成式（无条件）模型 $p(\boldsymbol{x}_{n}, \boldsymbol{y}_{n}, \boldsymbol{z}_{n}|\boldsymbol{\theta})$，或者一个判别式（条件）模型 $p(\boldsymbol{y}_{n}, \boldsymbol{z}_{n}|\boldsymbol{x}_{n}, \boldsymbol{\theta})$。

### A.8.3 贝叶斯推断

在进行贝叶斯推断时，我们将参数上的先验记为 $p(\boldsymbol{\theta}|\boldsymbol{\xi})$，其中 $\boldsymbol{\xi}$ 是超参数。对于共轭模型，后验与先验具有相同的形式（根据定义）。因此，我们可以直接将超参数从其先验值 $\boldsymbol{\xi}$ 更新到其后验值 $\widehat{\boldsymbol{\xi}}$。

在变分推断中（第4.6.8.3节），我们使用 $\psi$ 来表示变分后验的参数，即 $p(\boldsymbol{\theta}|\mathcal{D}) \approx q(\boldsymbol{\theta}|\boldsymbol{\psi})$。我们相对于 $\psi$ 优化 ELBO 以使其成为一个良好的近似。

---

在进行蒙特卡洛采样时，我们使用 $s$ 下标或上标来表示样本（例如 $\theta_{s}$ 或 $\theta^{s}$）。

### A.9 缩略语

以下是本书中使用的部分缩略语。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>缩略语</td><td style='text-align: center; word-wrap: break-word;'>含义</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cdf</td><td style='text-align: center; word-wrap: break-word;'>累积分布函数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CNN</td><td style='text-align: center; word-wrap: break-word;'>卷积神经网络</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DAG</td><td style='text-align: center; word-wrap: break-word;'>有向无环图</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DML</td><td style='text-align: center; word-wrap: break-word;'>深度度量学习</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DNN</td><td style='text-align: center; word-wrap: break-word;'>深度神经网络</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dof</td><td style='text-align: center; word-wrap: break-word;'>自由度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EB</td><td style='text-align: center; word-wrap: break-word;'>经验贝叶斯</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EM</td><td style='text-align: center; word-wrap: break-word;'>期望最大化算法</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GLM</td><td style='text-align: center; word-wrap: break-word;'>广义线性模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GMM</td><td style='text-align: center; word-wrap: break-word;'>高斯混合模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMC</td><td style='text-align: center; word-wrap: break-word;'>汉密尔顿蒙特卡洛</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMM</td><td style='text-align: center; word-wrap: break-word;'>隐马尔可夫模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iid</td><td style='text-align: center; word-wrap: break-word;'>独立同分布</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iff</td><td style='text-align: center; word-wrap: break-word;'>当且仅当</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>KDE</td><td style='text-align: center; word-wrap: break-word;'>核密度估计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>KL</td><td style='text-align: center; word-wrap: break-word;'>Kullback-Leibler 散度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>KNN</td><td style='text-align: center; word-wrap: break-word;'>K 近邻</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LHS</td><td style='text-align: center; word-wrap: break-word;'>（等式的）左侧</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LSTM</td><td style='text-align: center; word-wrap: break-word;'>长短期记忆（一种循环神经网络）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LVM</td><td style='text-align: center; word-wrap: break-word;'>潜变量模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MAP</td><td style='text-align: center; word-wrap: break-word;'>最大后验估计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCMC</td><td style='text-align: center; word-wrap: break-word;'>马尔可夫链蒙特卡洛</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MLE</td><td style='text-align: center; word-wrap: break-word;'>最大似然估计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MLP</td><td style='text-align: center; word-wrap: break-word;'>多层感知机</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MSE</td><td style='text-align: center; word-wrap: break-word;'>均方误差</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NLL</td><td style='text-align: center; word-wrap: break-word;'>负对数似然</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OLS</td><td style='text-align: center; word-wrap: break-word;'>普通最小二乘</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>psd</td><td style='text-align: center; word-wrap: break-word;'>正定（矩阵）</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pdf</td><td style='text-align: center; word-wrap: break-word;'>概率密度函数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pmf</td><td style='text-align: center; word-wrap: break-word;'>概率质量函数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PNLL</td><td style='text-align: center; word-wrap: break-word;'>惩罚负对数似然</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PGM</td><td style='text-align: center; word-wrap: break-word;'>概率图模型</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RNN</td><td style='text-align: center; word-wrap: break-word;'>循环神经网络</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RHS</td><td style='text-align: center; word-wrap: break-word;'>（等式的）右侧</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSS</td><td style='text-align: center; word-wrap: break-word;'>残差平方和</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>rv</td><td style='text-align: center; word-wrap: break-word;'>随机变量</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RVM</td><td style='text-align: center; word-wrap: break-word;'>相关向量机</td></tr></table>

<div style="text-align: center;">作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可</div>

---

SGD                      随机梯度下降

SSE                     误差平方和

SVI                      随机变分推断

SVM                     支持向量机

VB                      变分贝叶斯

wrt                      关于

---

### 索引

ADADELTA, 300

ADAGRAD, 299

ADAM, 300

PADAM, 301

RMSPROP, 299

RPROP, 299

YOGI, 301

1×1卷积, 474

抽象式摘要, 542

动作电位, 436

动作, 167

激活函数, 428

激活最大化, 495

主动, 305

主动学习, 407, 650

有效集, 399

活动正则化, 683

Adaboost.M1, 615

AdaBoostClassifier, 615

Adam, 447

Adamic/Adar, 758

适配器, 631

自适应基函数, 611

自适应实例归一化, 501

自适应学习率, 299, 301

加一平滑, 122, 132, 335

加法注意力, 521

加法模型, 611

伴随, 445

调整兰德指数, 717

可采纳, 192

ADOPT, 301

仿射函数, 8, 8

智能体, 17, 167

聚合梯度, 298

AGI, 28

AI, 28

AI伦理, 28

AI安全, 28

赤池信息准则, 186

偶然不确定性, 7, 34

AlexNet, 481

对齐, 522

对齐问题, 28

所有配对, 593

所有配对, 593

ALLS, 743

交替最小二乘, 743

备择假设, 179, 198

环境维度, 690

摊销推断, 685

锚点, 555

锚框, 490

ANN, 436

Anscombe四重奏, 43, 43

近似后验推断, 151

近似误差, 194

ARD, 411, 570, 598

ARD核, 570

曲线下面积, 173

Armijo回溯法, 286

Armijo-Goldstein, 286

人工通用智能, 28

人工智能, 28

人工神经网络, 436

结合性, 242

渐近正态性, 155

渐近最优, 160

异步训练, 454

原子弹, 73

注意力, 518, 522

注意力核, 654

注意力分数, 519

注意力权重, 519

AUC, 173

增强智能, 28

自协方差矩阵, 79

AutoAugment, 627

自相关矩阵, 79

自动微分, 438

自编码器, 679

自动微分, 438

自动相关性确定, 411, 570, 598

AutoML, 485

AutoRec, 745

自回归模型, 101

平均链接聚类, 720

平均池化, 475

平均精度, 175

轴对齐, 82

轴平行分割, 603

轴突, 436

---

B样条，399

骨干网络，433

反向拟合，402

反向传播，428

反向传播算法，438

时间反向传播，510

反斜杠运算符，267

回代，267，375

包，655

词嵌入袋，26

词袋，24，432

装袋，609

BALD，651

气球核密度估计器，563

带状对角矩阵，239

带宽，459，560，568

Barnes-Hut算法，705

重心坐标，698

基测度，93

基，233

基函数展开，425

基向量，243

批量学习，119

批量归一化，477，478

批量重归一化，478

BatchBALD，651

贝叶斯决策规则，168

贝叶斯误差，127，547

贝叶斯估计量，168，191

贝叶斯因子，180

贝叶斯模型平均，129

贝叶斯风险，191

贝叶斯规则，45

高斯变量的贝叶斯规则，87

贝叶斯法则，45，45

贝叶斯规则，45

贝叶斯学派，33

贝叶斯 $\chi^2$ 检验，188

贝叶斯主动学习分歧，651

贝叶斯决策理论，167

贝叶斯深度学习，457

贝叶斯因子回归，677

贝叶斯推断，44，46

贝叶斯信息准则，185

贝叶斯机器学习，147

贝叶斯模型选择，185

贝叶斯网络，100

贝叶斯神经网络，457

贝叶斯奥卡姆剃刀，183

贝叶斯优化，650

贝叶斯个性化排序，747

贝叶斯统计，129，154

贝叶斯t检验，188

BBO，319

束搜索，515

信念状态，46

伯克森悖论，102

伯努利分布，49

伯努利混合模型，98

BERT，538

贝塞尔函数，570

贝塔分布，63，121，131

贝塔函数，63

贝塔-二项分布，135

BFGS，290

双温度逻辑回归，362

偏差，8，159，371

偏差-方差权衡，161，459

BIC，185

BIC损失，186

BIC分数，186，728

双聚类，737

双向RNN，506

大数据，3

二元语法模型，102，212

双射器，67

双层优化，195

二分类，2，46

二进制连接，311

二元交叉熵，342

二元熵函数，208

二元逻辑回归，339

二项式系数，50

二项分布，50，50

二项回归，416

BinomialBoost，618

BIO，541

BiT，532

比特，207

双变量高斯分布，81

黑天鹅悖论，122

黑箱，319

黑箱优化，319

块对角矩阵，239

块结构矩阵，250

蓝脑计划，438

BMA，129

BMM，98

BN，477

BNN，457

玻尔兹曼分布，55

BookCrossing，742

布尔逻辑，34

提升，611

自助法，156

瓶颈，679

边界优化，312，354

边界框，489

碗形，344

箱约束，308

箱线图，44

箱形核，560，562

分支因子，212

Brier分数，179，645

Brier技能分数，179

布朗运动，571

字节对编码，26

C路N样本分类，653

C4，543

C4.5，605

微积分，269

变分法，95

校准图，420

典型相关分析，679

典范形式，94

典范连接函数，417

典范参数，93

CART，603，605

笛卡尔积，68

Caser，750

CatBoost，619

类别型，53

类别型PCA，677

---

CatPCA, 677

柯西, 62

因果, 80

因果CNN, 517

因果卷积, 518

CBOW, 707, 708, 708

CCA, 679

cdf, 37, 57

中心化, 408

中心化矩阵, 113, 247, 696

中心区间, 146

中心极限定理, 60, 72

质心, 459

熵的链式法则, 211

互信息的链式法则, 219

微积分链式法则, 273

概率的链式法则, 39

变量替换, 67

通道, 467, 473

特征方程, 254

特征长度尺度, 570

特征矩阵, 222

聊天机器人, 543

ChatGPT, 542, 543

卡方分布, 65

Cholesky分解, 382

Cholesky因式分解, 266

乔规则, 170

CIFAR, 20

城市街区距离, 718

类条件密度, 323

类别混淆矩阵, 172

类别不平衡, 173, 359, 593

类别平衡采样, 359

类别, 2

经典MDS, 692

经典统计学, 154

分类, 2, 778

分类与回归树, 603

CLIP, 635

封闭世界假设, 550

完形填空, 539

完形填空任务, 632

簇假设, 640

聚类, 715, 97

簇, 14

CNN, 3, 426, 467

协同适应, 455

协同训练, 642

协同聚类, 737

代码生成, 543

码本, 724

决定系数, 381

CoLA, 543

冷启动, 750

协同过滤, 737, 742

列秩, 237

列空间, 233

列向量, 229

列主序, 231

委员会方法, 608

可交换, 242

紧致性, 720

分类器比较, 187

互补对数-对数, 418

互补松弛性, 305

完全链接聚类, 720

配方法, 88

复杂度惩罚, 121, 185

复合目标, 282

组合式, 434

复合假设, 199

计算图, 444

计算机图形学, 493

凹函数, 278

条件数, 123, 238, 286

条件计算, 463

条件分布, 38

条件熵, 210

条件实例归一化, 500

条件混合模型, 462

条件互信息, 219

条件概率, 35

条件概率分布, 7, 50, 100

条件概率表, 100

条件方差公式, 42

条件独立, 35, 39, 99

置信区间, 146, 157

确认偏差, 639

Conformer, 533

共轭函数, 279

共轭梯度, 286, 375

共轭先验, 87, 130, 130, 131

一致性序列, 209

概率质量守恒, 183

一致性正则化, 644

一致估计量, 192, 406

约束优化, 277

约束优化问题, 302, 403

约束, 277

上下文词嵌入, 26, 537, 712

列联表, 189

持续学习, 551

延拓法, 398

连续优化, 275

连续随机变量, 36

收缩, 683

收缩自编码器, 682

矛盾, 523

对比损失, 555

对比任务, 633

控制变量, 297

凸, 344

凸组合, 133

凸函数, 278

凸优化, 277

凸松弛, 386

凸集, 277

ConvNeXt, 485, 533

卷积, 71, 468

卷积定理, 71

空洞卷积, 486

卷积马尔可夫模型, 517

卷积神经网络, 3, 21, 12, 426, 467

坐标下降, 397

坐标向量, 233

基于坐标的表示, 429

共指消解, 527

核心集, 559

语料库, 706

相关系数, 78, 82

---

相关性并不意味着因果，79

相关矩阵，78, 114

余弦核，571

余弦相似度，706

代价函数，275

协方差，77

协方差矩阵，77, 81

协变量，2, 371, 778

COVID-19，46

CPD（条件概率分布），100

CPT（条件概率表），100

克拉美-罗下界，160

可信区间，143, 146, 146

临界点，303

互相关，469

交叉熵，209, 214, 216

交叉验证，126, 196

互协方差，77

交叉熵，178

交叉率，173

交叉验证风险，126, 196

CrossCat（交叉分类），739

拥挤问题，703

三次样条，399

累积量，95

累积分布函数，37, 57

维度灾难，548

曲线拟合，14

曲指数族，94

CV（交叉验证），126, 196

循环置换性质，236

循环学习率，296

DAG（有向无环图），100, 444

数据增强，216, 627

数据压缩，16, 725

数据碎片化，605

数据挖掘，27

数据并行，454

数据处理不等式，223

数据科学，27

数据不确定性，7, 34

Datasaurus Dozen（数据龙十二），43, 44

死亡 ReLU，450

去偏，389

决策边界，5, 53, 149, 340

不确定性下的决策，1

决策规则，5

决策面，6

决策树，6

决策树，603

解码，657

解码器，679, 687

反卷积，487

演绎，201

深度 CCA（典型相关分析），679

深度分解机，748

深度图信息最大化，767

深度度量学习，552, 554

深度混合专家模型，463

深度神经网络，12, 425

DeepDream（深度梦境），497

DeepWalk（深度游走），760

默认先验，145

辩护人谬误，75

压缩矩阵，713

压缩，259

正常程度，61

自由度，13, 61, 383

增量规则，294

演示，18

树突，436

系统树图，718

去噪自编码器，681

密集预测，492

密集序列标注，507

DenseNets（密集连接网络），484

密度估计，16

密度核，520, 560

因变量，371

深度预测，492

深度可分离卷积，488

导数，269

无导数优化，319

下降方向，283, 284

设计矩阵，3, 245, 426, 778

行列式，237

开发集，124

偏差，185, 420, 606

DFO（无导数优化），319

对角协方差矩阵，83

对角矩阵，239

可对角化，255

对角占优，240

直径，720

可微决策树，606

可微分编程，444

微分熵，212

积分号下求导，70

微分，270

扩散先验，145

空洞卷积，486, 491

扩张因子，486

降维，4, 657

狄拉克δ函数，60, 148

有向无环图，100, 444

方向导数，270

狄利克雷分布，138, 334

狄利克雷能量，701

离散 AdaBoost，614

离散优化，275

离散随机变量，35

离散化，213, 220

判别函数，324

判别式分类器，323, 336

离散参数，415

距离度量，213

远程监督，655

失真，657, 722, 724

分布假设，705

分配律，242

散度测度，213

多样化束搜索，516

DNA序列模体，208

DNN（深度神经网络），12, 425

文档检索，706

文档摘要，22

领域自适应，630, 637

领域对抗学习，637

支配，192, 200

点积，242

双中心化技巧，247

双重下降，459

双指数分布，63

---

对偶可行性, 305  
对偶形式, 588  
对偶问题, 587  
对偶变量, 594  
虚拟编码, 23, 53  
荷兰赌定理, 203  
动态图, 446  
动态规划, 515  
E步, 312, 314  
早停, 126, 455  
经验贝叶斯, 145  
回声状态网络, 511  
期望最大化算法, 670  
经济型QR分解, 265  
经济型奇异值分解, 260  
边缘设备, 311, 488  
等错误率, 173  
效应量, 187  
EfficientNetv2, 485  
特征脸, 659  
特征值, 253  
特征值分解, 253  
特征值谱, 123  
特征向量, 253  
爱因斯坦求和约定, 248  
einsum, 248  
弹性嵌入, 702  
弹性网络, 390, 396  
证据下界, 153, 314, 685  
肘部, 728  
电子健康记录, 523  
ℓ2损失, 9  
极限学习机, 584  
ELMo, 538  
期望对数逐点预测密度, 187  
指数线性单元, 450  
期望最大化, 85, 312  
指数移动平均, 119  
垃圾邮件分类, 22  
令人尴尬的并行, 454  
嵌入, 657  
EMNIST, 20  
经验贝叶斯, 145, 182, 411  
经验分布, 65, 72, 109, 193, 215  
经验风险, 6, 194  
经验风险最小化, 7, 115, 194, 293  
编码, 657  
编码器, 679, 687  
编码器-解码器, 491  
编码器-解码器架构, 509  
内生变量, 2  
基于能量的模型, 635  
能量函数, 152  
集成, 296, 457  
集成学习, 608  
蕴含, 523  
实体发现, 722  
实体链接, 551  
实体解析, 542, 551  
熵, 178, 207, 314, 606  
熵最小化, 639  
熵SGD, 458  
埃帕涅奇尼科夫核, 561  
上图, 278  
认知不确定性, 7, 34  
认识论, 34  
轮次, 293  
ε不敏感损失函数, 595  
等错误率, 173  
等式约束, 277, 302  
公平性, 222  
等效样本量, 131  
等变性, 475  
经验风险最小化, 115, 194  
误差函数, 57  
估计误差, 194  
估计量, 154  
特征值分解, 253  
事件, 34, 34, 35, 35  
事件, 33  
证据, 135, 182  
证据下界, 153, 314, 685  
指数加权移动平均, 119, 299  
精确线搜索, 286  
可交换性, 102  
独占型KL散度, 216  
异或, 460  
基于样本的模型, 547  
样本, 459  
外生变量, 2  
期望最大化, 312  
期望完全数据对数似然, 315  
期望对数逐点预测密度, 187  
期望充分统计量, 315  
期望值, 40, 58  
实验设计, 650  
解释效应, 102  
解释变量, 371  
显式反馈, 741  
解释变量, 371  
显式反馈, 741  
梯度爆炸问题, 447  
探索-利用权衡, 751  
探索性数据分析, 4  
指数分散族, 415  
指数分布, 65  
指数族, 93, 96, 144  
指数族因子分析, 675  
指数族PCA, 675  
指数线性单元, 448  
指数损失, 614  
指数移动平均, 119  
指数加权移动平均, 119  
交叉熵, 212  
指数二次核, 568  
抽取式摘要, 542  
极限学习机, 584  
F得分, 175  
人脸检测, 489  
人脸识别, 489  
人脸验证, 551  
FaceNet, 557  
因子分析, 16, 666  
因子载荷矩阵, 667  
因子分解机, 748  
FAISS, 550  
虚警率, 172  
假阴性率, 46  
假阳性率, 46, 172  
扇入, 453  
扇出, 453  
Fano不等式, 225  
最远点聚类, 725

---

Fashion-MNIST, 20  

快速适应, 652  

快速哈达玛变换, 584  

fastfood, 584  

可行性, 304  

可行性问题, 277  

可行集, 277  

特征交叉, 24  

特征检测, 471  

特征工程, 12  

特征提取, 12  

特征提取器, 372  

特征重要性, 621, 621  

特征图, 471  

特征预处理, 12  

特征选择, 225, 310, 385  

特征, 1  

特征化, 4  

前馈神经网络, 425  

少样本分类, 551  

少样本学习, 653  

FFNN, 425  

填空, 27  

填空式, 539, 632  

滤波器, 469  

滤波器响应归一化, 479  

滤波器, 467  

FIM, 155  

细粒度分类, 21, 653  

细粒度视觉分类, 629  

微调, 537  

微调阶段, 629  

有限差分, 270  

有限求和问题, 293  

一阶, 346  

一阶马尔可夫条件, 101  

一阶, 282, 289  

Fisher信息矩阵, 155, 348  

Fisher评分法, 348  

Fisher线性判别分析, 328  

FISTA, 398  

FLAN-T5, 543  

平坦局部极小点, 276  

平坦极小值, 457  

平坦先验, 144  

展平, 431  

FLDA, 328  

折, 126, 196  

遗忘门, 513  

前向模式微分, 439  

前向逐步加性建模, 612  

前向KL散度, 216  

前向模型, 49  

混杂变量, 673  

解释方差比例, 665  

欺诈检测系统, 770  

频率派, 33  

频率派决策理论, 189  

频率派统计学, 154  

Frobenius范数, 236  

冻结参数, 630  

全协方差矩阵, 82  

满秩, 237  

全矩阵Adagrad, 301  

函数空间, 577  

最远邻聚类, 720  

融合批归一化, 477  

画廊, 490, 550  

GAM, 401  

伽马分布, 64  

GANs, 637  

门控图序列神经网络, 76  

门控循环单元, 512  

门控函数, 462  

高斯分布, 9  

高斯判别分析, 323  

高斯分布, 57  

高斯核, 459, 535, 560, 568  

高斯混合模型, 97  

高斯过程, 460  

高斯过程回归, 401  

高斯过程, 574  

高斯尺度混合, 105  

GCN, 763  

GDA, 323  

GELU, 448, 451  

泛化误差, 197  

泛化差距, 13, 194  

泛化, 7, 121  

广义加性模型, 401  

广义CCA, 679  

广义特征值, 330  

广义拉格朗日函数, 304, 587  

广义线性模型, 415  

广义低秩模型, 675  

广义probit近似, 367  

生成对抗网络, 647  

生成式分类器, 323, 336  

生成式图像模型, 493  

几何深度学习, 753  

几何级数, 120, 287  

基尼指数, 605  

glmnet, 397  

GLMs, 415  

全局平均池化, 432, 476  

全局优化, 275  

全局最优, 275, 344  

全局收敛, 276  

Glorot初始化, 453  

GloVe, 710  

GMM, 97  

GMRES, 376  

GNN, 426, 762  

拟合优度, 380  

GoogLeNet, 482  

GPT, 542  

GPT-2, 542  

GPT-3, 542  

GPT-4, 542  

GPU, 435, 454  

GPyTorch, 583  

梯度, 270, 283  

梯度提升回归树, 618  

梯度提升, 616  

梯度裁剪, 447  

梯度符号翻转, 637  

梯度树提升, 618  

Gram矩阵, 241, 247, 500, 568  

Gram-Schmidt, 242  

图注意力网络, 764  

图卷积网络, 763  

图分解, 759  

图拉普拉斯, 700, 735  

图神经网络, 762

---

图神经网络 (GNN), 426

图划分, 734

图表示学习, 753

图模型, 40

图互信息, 768

图形处理单元 (GPU), 454

石墨, 767

GraphNet, 763

GraphSAGE, 763

GraRep, 759

贪心解码, 515

贪心前向选择, 399

网格近似, 152

网格搜索, 125, 320

组套索, 394

组归一化, 479

组稀疏性, 393

分组效应, 396

门控循环单元 (GRU), 512

Gshard, 533

Gumbel噪声, 516

层次凝聚聚类 (HAC), 717

半柯西, 63

半空间, 340

哈密顿蒙特卡洛 (HMC), 154

硬注意力, 525

硬聚类, 98, 730

硬负样本, 556

硬阈值, 388, 391

硬件加速器, 437

调和平均数, 175

帽子矩阵, 375

最高密度区间 (HDI), 147

He初始化, 453

注意力头, 433

热力图, 471

亥维赛（阶跃）函数, 346

亥维赛阶梯函数, 443, 426

重球动量, 287

重尾, 62, 402

亥姆霍兹机, 685

黑塞矩阵, 344, 776

黑塞矩阵, 272

异方差回归, 59, 376

启发式方法, 438

隐藏, 45

隐藏共同原因, 79

隐藏单元, 427

隐变量, 102, 312, 778

层次, 434

层次凝聚聚类, 717

层次贝叶斯模型, 145

层次专家混合, 463

层次Softmax, 358

层次结构, 357

最高密度区间, 147

最高后验密度, 147

合页损失, 116, 320, 591, 747

Hinton图, 86

命中率, 172

哈密顿蒙特卡洛 (HMC), 154

霍夫丁不等式, 197

乱序训练 (Hogwild), 454

留出集, 196

同质, 101

同方差回归, 59

同伦, 398

最高后验密度 (HPD), 147

Huber损失, 177, 404, 617

哈夫曼编码, 358

人体姿态估计, 493

Hutchinson迹估计器, 236, 237

超参数, 131, 319

超列, 474

上位词, 358

超参数, 195

超参数, 145

超平面, 340

假设, 523

假设空间, 194

假设检验, 179

I-投影, 216

独立假设 (IA), 28

ID3算法, 605

可识别性, 355

可识别, 192, 355

单位矩阵, 239

独立同分布, 71, 108, 130

病态, 114, 238

不适定, 49

整数线性规划 (ILP), 307

大规模视觉识别挑战赛 (ILSVRC), 21

图像描述, 505

图像分类, 3

图像压缩, 725

图像插值, 688

图像块, 467

图像标签, 350, 488

图像到图像, 492

ImageNet, 21, 435, 481

ImageNet-21k, 533

IMDB, 128

IMDB电影评论数据集, 22

隐式反馈, 747

隐式正则化, 457

冒名者, 552

数据补全任务, 632

Inception模块, 482

Inceptionism, 497

包容性KL散度, 216

增量学习, 551

不定, 240

独立, 35, 39

独立同分布, 71, 130

自变量, 371

指示函数, 6, 36

诱导范数, 235

诱导点, 583

归纳, 122, 201

归纳偏置, 13, 427, 532

归纳学习, 643

不等式约束, 277, 302

不可行, 306

推断, 107, 129

推断网络, 684

无穷宽, 582

InfoNCE, 556

信息, 33

信息量, 207

信息准则, 185

信息图, 218

---

信息图, 219

信息抽取, 541

信息增益, 213, 650

信息收集动作, 7

信息投影, 216

信息检索, 173

信息论, 178, 207

内积, 242

输入门, 513

Instagram, 489

实例归一化, 478

实例分割, 490

实例均衡采样, 359

基于实例的学习, 547

InstructGPT, 542

指令微调, 543

整数线性规划, 307

集成风险, 191

积分边际化, 129

智能增强, 28

四分位距, 44

交互效应, 23

截距, 8

内点法, 306

内部协变量偏移, 477

插值, 12

插值精度, 175

插值器, 574

可解释的, 17

内在维度, 690

逆矩阵, 249

逆累计分布函数, 38

逆文档频率, 25

逆Gamma分布, 65

逆概率, 49

逆问题, 49

逆强化学习, 28

逆Wishart分布, 122

鸢尾花, 2

鸢尾花数据集, 3

IRLS, 348

等距映射, 694

各向同性协方差矩阵, 83

ISTA, 398

项目, 741

迭代平均, 297

迭代软阈值算法, 39

迭代重加权最小二乘, 348

雅可比矩阵, 67, 352

雅可比矩阵, 67, 352

雅可比公式, 271

雅可比矩阵, 271

雅可比向量积, 271

詹森不等式, 214, 314

Jeopardy, 170

Jester, 742

JFT, 533

抖动, 461

联合分布, 38

联合概率, 34

JPEG, 725

即时编译, 446

JVP, 271

K近邻, 547

k-d树, 550

K均值算法, 722

K均值聚类, 98

K-means++, 725

K-medoids, 725

卡尔曼滤波, 91

卡尔·波普尔, 122

卡鲁什-库恩-塔克条件, 305

Katz中心性指数, 758

KDE, 560, 562

核, 469, 560

核密度估计, 560

核密度估计器, 562

核函数, 459, 567, 567

核主成分分析, 695, 737

核回归, 520, 564, 576

核岭回归, 576, 595

核平滑, 564

核技巧, 590

键, 518

关键词, 261

折点, 728

KKT, 305

KL散度, 109, 177, 213, 314

KNN, 547

结点, 399

知识蒸馏, 649

知识图谱, 770

克罗内克积, 248

Krylov子空间方法, 583

KSG估计器, 220

Kullback-Leibler散度, 109, 177

Kullback-Leibler散度, 213, 314

L-BFGS, 291

L0范数, 385, 386

L1损失, 176

L1正则化, 385

L1VM, 598

L2损失, 176

L2正则化, 123, 349, 381

L2VM, 597

标签, 2

标签噪声, 360, 655

标签传播, 643, 761

标签涂抹, 358

标签平滑, 650, 655

标签扩展, 761

标签交换问题, 319, 732

拉格朗日乘子, 303

拉格朗日乘子, 95, 111

拉格朗日记法, 270

拉格朗日函数, 95, 259, 277, 303, 386

Lanczos算法, 671

语言模型, 101

语言建模, 22, 505

语言模型, 211, 537

拉普拉斯, 385

拉普拉斯近似, 152, 363

拉普拉斯分布, 63

拉普拉斯平滑, 335

拉普拉斯向量机, 598

拉普拉斯继承规则, 134

拉普拉斯特征映射, 699, 736, 757

LAR, 399

大型语言模型, 543

大间隔分类器, 585

大间隔最近邻, 552

大间隔最近邻, 552

---

LASSO, 398

lasso, 307, 385

潜在巧合分析, 553

潜在因子, 15, 659

潜在语义分析, 707

潜在语义索引, 706

潜在空间插值, 688

潜变量, 96

潜变量模型, 778

潜变量, 778

潜向量, 659

迭代期望定律, 41

全期望定律, 41

全方差定律, 42

层归一化, 478

层序单位方差, 453

LCA, 553

LDA, 323, 325

Leaky ReLU, 448

leaky ReLU, 450

学习曲线, 127

学习率, 283

学习率调度, 284, 294, 295

学习率预热, 296

学会学习, 652

带批评的学习, 18

带教师的学习, 18

最小角回归, 399

最不利先验, 192

最小均方, 294, 378

最小二乘提升, 399, 612

最小二乘目标, 268

最小二乘解, 10

留一交叉验证, 126, 196

LeCun 初始化, 453

左伪逆, 269

莱布尼茨记号, 270

LeNet, 476, 479

水平集, 82, 83

终身学习, 551

LightGBM, 619

似然, 45

似然函数, 129

似然原理, 202

似然比, 180, 201

似然比检验, 198

有限内存 BFGS, 291, 354

线搜索, 285

**线性代数**, 229

线性自编码器, 680

线性组合, 243

线性判别分析, 323, 325

线性函数, 8

线性高斯系统, 86

线性核, 581

线性映射, 233

线性算子, 376

线性规划, 403

线性速率, 286

线性回归, 59, 371, 415, 425

线性子空间, 243

线性阈值函数, 426

线性变换, 233

期望的线性性, 40

线性相关, 232

线性无关, 232

线性可分, 340

Link Former, 535

连接函数, 415, 417

链接预测, 769

Lipschitz 常数, 281

液态状态机, 511

LLMs, 543

LMNN, 552

LMS, 294

局部线性嵌入, 697

局部最大值, 276

局部最小值, 275

局部最优, 275, 344

局部敏感哈希, 550

局部线性回归, 565

局部加权散点图平滑, 565

LOESS, 565

对数双线性语言模型, 711

对数似然, 108

对数损失, 178, 592

对数几率, 52

对数配分函数, 93

对数求和指数技巧, 56

logistic, 51

logistic 函数, 52, 148

**Logistic 回归**, 339

logistic 回归, 8, 53, 148, 415

logit, 51, 339, 342

logit 调整, 359

logit 函数, 52

logitBoost, 616

logits, 7, 55, 350

长短期记忆, 513

长尾, 151, 358

Lorentz, 62

Lorentz 模型, 758

损失函数, 6, 9, 167, 275

有损压缩, 724

下三角矩阵, 240

LOWESS, 565

LSA, 707

lse, 56

LSH, 550

LSI, 706

LSTM, 513

M 步, 312

M 阶马尔可夫模型, 101

M-投影, 216

M1, 646

M2, 646

**机器学习**, 1

机器翻译, 22, 509

马氏距离, 83, 547

马氏白化, 258

主效应, 23

最大化-最小化, 312

MALA, 493

MAML, 652

流形, 689, 689

流形假设, 643

流形假设, 689

流形学习, 689

mAP, 175

MAP 估计, 169

MAP 估计, 121, 195

MAR, 27

---

边缘误差, 590

边缘分布, 38

边缘似然, 45, 129, 135, 137, 145, 182

边缘化, 129, 148

边缘化求和, 129

边缘独立, 39

马尔可夫链, 101

马尔可夫链蒙特卡洛, 153

马尔可夫核, 101

马尔可夫模型, 101

MART, 618

掩码注意力, 520

掩码语言模型, 539

匹配滤波, 468

匹配网络, 654

马特恩核, 570

矩阵, 229

矩阵补全, 743

矩阵行列式引理, 252

矩阵分解, 743

矩阵求逆引理, 251, 594

矩阵平方根, 235, 245, 266

矩阵向量乘法, 583

最大池化, 475

最大熵分类器, 357

最大信息系数, 221

最大后验估计, 121

最大后验, 169

最大熵, 60, 207

最大熵分类器, 357

最大熵模型, 95

最大熵采样, 651

最大期望效用原则, 168

最大似然估计, 8

最大似然估计, 107

最大风险, 191

最大方差展开, 697

完全随机缺失, 27

麦卡洛克-皮茨模型, 436

McKernel, 584

MCMC, 153

MDL, 186

MDN, 463

MDS, 691

均值, 40, 58

平均精度均值, 175

均值函数, 415

均方误差, 9, 115

均值插补, 27

中位数, 38, 57

中位数绝对偏差, 563

中心点, 725

记忆单元, 513

基于记忆的学习, 547

默瑟核, 567

默瑟定理, 568

消息传递神经网络, 762

元学习, 652, 654

矩估计, 117

度量MDS, 693

Metropolis调整的Langevin算法, 493

MICE, 222

最小最大缩放, 350

小批量, 293

最小, 3

最小表示, 94

最小充分统计量, 224

最小信息先验, 145  

最小最大估计量, 192  

最小描述长度, 186  

最小均方误差, 176  

最小消息长度, 186  

最小生成树, 719  

MM算法, 312  

MIP, 307  

误分类率, 6, 116  

随机缺失, 27, 741  

完全随机缺失, 27  

缺失数据, 26, 312  

缺失数据机制, 27, 647  

缺失值插补, 85  

混合整数线性规划, 307  

混合权重, 137  

混合匹配, 640  

混合密度网络, 463  

混合模型, 96  

伯努利混合, 98  

贝塔分布混合, 136  

专家混合, 462, 533  

因子分析器混合, 674  

高斯混合, 97  

ML, 1  

MLE, 8, 107  

MLP, 425, 427  

MLP混合器, 427  

MM, 312  

MMSE, 176  

MNIST, 19, 479  

MobileNet, 488  

MoCo, 635  

众数, 41, 169  

覆盖众数, 216  

寻求众数, 217  

模型压缩, 455  

模型拟合, 7, 107  

模型并行, 454  

模型选择, 181  

模型选择一致, 392  

模型不确定性, 7, 34  

模型无关元学习, 652  

拒取式, 201  

MoE, 462  

MoG, 97  

矩投影, 216  

动量, 287  

动量对比学习, 635  

MoNet, 765  

蒙特卡洛近似, 73, 153, 3  

蒙特卡洛丢弃法, 457  

蒙提霍尔问题, 47  

Moore-Penrose伪逆, 261  

最大功效检验, 200  

微点, 11  

MovieLens, 742  

移动平均, 119  

MSE, 9, 115  

多类分类, 350  

多聚类, 739  

多维缩放, 757  

多头注意力, 527  

多实例学习, 655  

多标签分类, 350  

多标签分类器, 358

---

多目标跟踪, 551

多类逻辑回归, 339

多维缩放, 691

多层感知机, 425, 427

多模态, 41

多项式系数, 54

多项式分布, 53, 54

多项式逻辑回归, 350

多项式逻辑回归, 55, 339

多项式logit, 54

多重插补, 85

多元线性回归, 10, 371

多重重启, 725

乘法交互, 518

多元伯努利朴素贝叶斯, 332

多元高斯分布, 80

多元线性回归, 372

多元正态分布, 80

互信息, 79, 217

相互独立, 74

MVM, 583

MVN, 80

短视的, 651

N-pair损失, 556

Nadaraya-Watson, 564

朴素贝叶斯假设, 327, 332

朴素贝叶斯分类器, 332

命名实体识别, 541

NAS, 485

nats, 207

自然指数族, 94

自然语言推理, 523

自然语言处理, 21, 357

自然语言理解, 49

自然参数, 93

NBC, 332

NCA, 552

NCM, 328

最近质心分类器, 328

最近类均值分类器, 328, 359

最近类均值度量学习, 328

最近邻聚类, 719

NEF, 94

负定, 240

负对数似然, 8, 108

半负定, 240

邻域成分分析, 552

新认知机, 476

嵌套优化, 195

嵌套划分, 739

涅斯捷罗夫加速梯度, 288

Netflix奖, 741

NetMF, 760

神经架构搜索, 485

神经隐式表示, 429

神经语言模型, 102

神经机器翻译, 509

神经矩阵分解, 749

神经风格迁移, 497

神经正切核, 582

NeurIPS, 18

神经的, 523

牛顿法, 289, 347

下一句预测, 540

内曼-皮尔逊引理, 200

NHST, 200

NHWC, 474

NIPS, 18

NLL, 108

NLP, 21

NMAR, 27

没有免费午餐定理, 13

node2vec, 760

噪声基底, 127

不可识别性, 732

不可识别的, 410

非度量MDS, 693

非参数自助法, 157

非参数方法, 689

非参数模型, 460

非饱和激活函数, 429, 449

无信息的, 144

非线性降维, 689

非线性因子分析, 674

非参数方法, 567

非参数模型, 547

非光滑优化, 281

范数, 234, 238

正态, 9

正态分布, 57

正规方程, 269, 373

正态-逆威沙特分布, 318

归一化层, 476

归一化的, 241

归一化切割, 735

归一化互信息, 221, 717

无归一化网络, 479

归一化流, 648

非随机缺失, 27

名词短语组块, 541

新颖性检测, 551

NT-Xent, 556

ν-SVM分类器, 590

核范数, 235

核苷酸, 208

零假设, 179, 187, 198

零假设显著性检验, 200

零空间, 233

分子布局, 271

目标检测, 489

目标, 144

目标函数, 108, 275

观测分布, 45

奥卡姆因子, 185

奥卡姆剃刀, 183

偏移, 10, 371

老忠实泉, 316

Olivetti人脸数据集, 658

OLS, 115, 269, 373

单周期学习率调度, 296

独热, 178

独热编码, 23, 352, 778

独热向量, 53, 229

一次性学习, 328, 653

单侧p值, 200

单侧检验, 187

一倍标准误规则, 126

一对多函数, 461

一对一, 593

一对多, 593

一对多, 593

在线学习, 119, 311, 551

---

OOV（词汇外）, 24, 26

开放类, 26

开放集识别, 550

开放世界, 489

开放世界假设, 551

OpenPose, 493

opt-einsum, 249

最优策略, 168

训练误差的乐观估计, 195

优化问题, 275

阶, 231

顺序统计量, 118

有序马尔可夫性, 100

顺序约束, 733

普通最小二乘法, 115, 269, 373

奥恩斯坦-乌伦贝克过程, 571

正统统计学, 154

正交, 241, 255

正交投影, 375

正交随机特征, 584

标准正交, 241, 255

词汇外, 26

袋外实例, 609

分布外, 551

样本外泛化, 689

词汇外, 24

外积, 243

异常值, 61, 176, 360, 402

输出门, 513

过完备表示, 94

过参数化, 55, 459

过完备表示, 679

超定, 266

超定方程组, 374

过拟合, 13, 120, 133

p值, 180, 200

PAC可学习, 197

PageRank, 258

配对图, 4

配对检验, 187

两两独立, 73

PAM（围绕中心点划分）, 726

全景分割, 491

参数空间, 275

参数绑定, 101

参数, 6

参数自助法, 157

参数模型, 547

参数化ReLU, 450

词性标注, 541

词性, 538

部分依赖图, 623

偏导数, 270

偏最小二乘法, 678

部分选主元, 264

偏回归系数, 377

部分观测, 167

配分函数, 56, 93, 635

分块逆公式, 250

围绕中心点划分, 726

Parzen窗密度估计量, 562

病态, 203

模式识别, 2

PCA（主成分分析）, 16, 657, 658

PCA白化, 257

pdf（概率密度函数）, 37, 58

窥视孔连接, 514

惩罚项, 309

百分点函数, 38

感知机, 346, 426

感知机学习算法, 346

Performer, 535

周期核, 571

置换检验, 201

困惑度, 211, 505

行人重识别, 551

PersonLab, 493

扰动理论, 736

PGM（概率图模型）, 100

Planetoid, 768

板（图模型中的板符号）, 103

Platt缩放, 591

PLS（偏最小二乘法）, 678

插件近似, 133, 148

插件近似, 366

PMF（概率质量函数）, 744

pmf（概率质量函数）, 36

PMI（点互信息）, 707

庞加莱模型, 758

点估计, 107

点原假设, 187

逐点卷积, 474

点互信息, 707

泊松回归, 417

极坐标, 68

策略, 17

Polyak-Ruppert平均, 297

多项式展开, 372

多项式回归, 10, 123, 372

多面体, 305

基于池的主动学习, 650

总体风险, 13, 125, 193

POS（词性）, 538

位置权重矩阵, 208, 209

位置嵌入, 528

正定, 240

正定核, 567

正PMI（正点互信息）, 707

半正定, 240

后归一化, 530

后验, 129

后验分布, 46, 129

后验期望损失, 167

后验推断, 46

后验均值, 176

后验中位数, 177

后验预测分布, 129, 134, 148, 366, 200

功效, 200

幂法, 258

PPCA（概率主成分分析）, 668

ppf（百分点函数）, 38

预激活, 339

预激活（值）, 428

前归一化, 530

预训练, 537

预训练词嵌入, 26

预训练阶段, 629

预激活残差网络, 484

精度, 57, 141, 174, 174

前K精度, 174

精度矩阵, 84, 112

精度-召回曲线, 174

---

预条件随机梯度下降, 298

预条件子, 298

预条件矩阵, 298

预测分析, 27

预测变量, 2

偏好, 167

前提, 523

PreResnet, 484

前置任务, 633

发生率, 46, 175

原始问题, 587

原始变量, 595

主成分分析, 16, 657

主成分回归, 384

先验, 121, 129

先验分布, 45

概率预测, 177

概率图模型, 100

概率推断, 46

概率矩阵分解, 744

概率主成分分析, 657

概率视角, 1

概率预测, 177

概率主成分分析, 668

概率密度函数, 37, 58

概率分布, 177

概率分布, 1

概率质量函数, 36

概率单纯形, 138

概率论, 45

可能近似正确, 197

Probit近似, 367

Probit函数, 57, 367

Probit链接函数, 418

乘积规则, 39

概率乘积法则, 45

轮廓似然, 665

轮廓对数似然, 666

投影梯度下降, 309, 398

投影, 234

投影矩阵, 375

提示, 542

提示工程, 543, 637

恰当评分规则, 179

检察官谬误, 75

代理变量, 557

近端梯度下降, 398

近端梯度法, 308

近端算子, 308

ProxQuant, 311

代理任务, 633

剪枝, 606

半正定, 240

伪计数, 131, 334

伪输入, 583

伪逆, 373

伪范数, 235

伪标签, 639

伪似然, 539

纯, 606

纯度, 716

毕达哥拉斯定理, 268

QALY, 167

QP, 306

二次近似, 152

二次型, 240, 256

二次核, 568

二次损失, 9, 176

二次规划, 306, 386, 596

质量调整生命年, 167

分位数, 38, 57

分位函数, 38

量化, 212

量化, 213, 220

量化, 311

四分位数, 38, 57

拟牛顿, 290

拟牛顿, 354

查询, 518

查询合成, 650

问答, 22, 542

径向基函数, 560

径向基函数核, 460, 535

Rand指数, 716

RAND-WALK, 711

随机有限集, 551

随机森林, 610

随机傅里叶特征, 584

随机数生成器, 72

随机洗牌, 293

随机变量, 35

随机变量, 1

随机游走核, 573

值域, 233

秩, 231, 237

秩亏, 237

秩一更新, 251

秩-零度定理, 262

排序损失, 555, 747

RANSAC, 404

速率, 486, 725

收敛速率, 286

评分, 741

瑞利商, 258

RBF, 560

RBF核, 460, 568

RBF网络, 460

实AdaBoost, 614

召回率, 172, 174

受试者工作特征, 173

感受野, 473, 486

识别网络, 684

推荐系统, 770

推荐系统, 741

重构误差, 657, 659, 724

修正线性单元, 448

修正线性单元, 429, 449

循环神经网络, 503

循环神经网络, 12, 426

递归更新, 119

递归地, 377

学习率衰减, 296

缩减QR, 265

Reformer, 535

实际等价区域, 187

回归, 8, 778

回归系数, 377

回归系数, 8, 371

正则化, 121

正则化参数, 121

正则化路径, 384, 389, 398

---

正则化判别分析，327

正则化经验风险，195

强化学习，17，751

基于人类反馈的强化学习，542

拒绝选项，170

拒绝原假设，200

关系数据，741

相对熵，213

相关向量机，598

ReLU，429，449

重参数化技巧，686

表示学习，633

蓄水池计算，512

重置门，513

重塑，231

残差块，451，483

残差误差，115

残差网络，451

残差图，380

残差平方和，115，373

残差，9，380

ResNet，451，483

ResNet-18，484

响应，2

响应变量，778

责任，98，315，463

反向KL散度，216

反向模式微分，440

奖励，18

奖励函数，275

奖励破解，28

RFF，584

岭回归，123，162，381，455

黎曼流形，689

黎曼度量，689

右伪逆，268

风险，167，189

风险厌恶，169，170

风险中性，169

风险敏感，169

RL，17

RLHF，542

均方根误差，115，381

RNN，426，503

Robbins-Monro条件，295

鲁棒，9，61，176

鲁棒线性回归，306

鲁棒逻辑回归，360

鲁棒性，402

ROC曲线，173

均方根误差，115，381

ROPE，187

旋转矩阵，241

行秩，237

行主序，231

RSS，115

迭代期望法则，104

全概率法则，38

运行和，119

随机变量，35

RVM，598

鞍点，277，280

SAGA，298，346

相同卷积，471

SAMME算法，615

Sammon映射，694

样本效率，17

样本均值，160

样本量，2，110，130

样本空间，35

样本方差，143

抽样分布，154

SARS-CoV-2，46

饱和模型，420

饱和，429

标量场，270

标量积，242

标量，232

证据强度，180

缩放点积注意力，521

散布矩阵，113，246

Schatten p-范数，235

计划采样，510

舒尔补，84，250

得分函数，155，275，682

碎石图，664

二阶，346

二阶，289

自注意力，526

自归一化性质，711

自监督，632

自监督学习，16

自训练，638，650

SELU，450

语义角色标注，357

语义分割，491

语义文本相似度，525

半难负样本，557

半监督嵌入，768

半监督学习，638

半监督学习，337

半正定嵌入，697

半正定规划，552，697

敏感主成分分析，668

敏感性，46，172

传感器融合，92

情感分析，22

序列到序列，507

序列到序列模型，22

序列到向量，506

序列标志，209

序列模体，209

序列最小优化，588

SGD，292

SGNS，709

阴影节点，102

浅层句法分析，541

Shampoo优化器，301

香农信源编码定理，209

共享，325

尖锐极小值，457

锐度感知最小化，458

Sherman-Morrison公式，251

Sherman-Morrison-Woodbury公式，2

射击算法，397

矮胖型，3

收缩，90，143，384

收缩估计，122

收缩因子，390，617

孪生网络，555，633

辅助信息，750

筛选性质，61，148

sigmoid函数，51，52，148，326

---

信噪比，90

显著性，199

显著性水平，200

轮廓系数，728, 728

轮廓图，728

轮廓分数，728

SiLU，451

SimCLR，633

相似性，547

简单假设，199

简单线性回归，9, 371

简单算法，306

辛普森悖论，80

模拟退火，43

单链聚类，719

单次检测器，490

奇异，249

奇异统计模型，186

奇异值分解，260

奇异值，238, 260

奇异向量，260

跳跃连接，484

负采样跳元，709

跳元，707

跳元模型，709

松弛变量，589, 596

推荐展板，750

斜率，10

SMACOF，693

SMO，588

光滑优化，281

光滑样条，401

SNLI，523

索贝尔边缘检测器，494

社交网络，770

软聚类，98

软决策树，606

软间隔约束，589

软阈值化，388, 391

软阈值算子，310

软三元组，557

softmax，54

softmax函数，7

Softplus，448

softplus，59

求解器，275

源数据集，629

源领域，637

张成，232

稀疏，138, 385

稀疏贝叶斯学习，411

稀疏因子分析，673

稀疏高斯过程，583

稀疏核机器，460, 550

稀疏线性回归，307

稀疏向量机，597

稀疏性诱导正则化器，310

特异度，46

谱聚类，734

谱卷积神经网络，763

谱嵌入，699

谱图理论，701

谱半径，447

球形协方差矩阵，83

球形嵌入约束，559

分裂变量技巧，397

虚假相关，79

虚假相关性，80  

虚假特征，337  

平方，230  

平方根采样，359  

平方根调度，296  

平方误差，176  

平方指数核，568  

堆叠，609  

标准基，233  

标准差，41, 58  

标准误差，133, 156  

均值标准误差，126, 143  

标准形式，305  

标准正态，57  

标准化操作，246  

标准化，350, 376  

经标准化的，316  

标准化（动名词），256  

斯坦福自然语言推理，523  

自然状态，167  

状态空间，35  

状态转移矩阵，101  

静态图，446  

平稳，101  

平稳核，569  

驻点，276  

统计学习理论，196  

统计机器翻译，509  

统计关系学习，771  

统计学，27  

最速下降，284  

斯坦悖论，193  

步长衰减，296  

阶跃函数，65  

步长，283  

随机平均梯度加速，298  

随机束搜索，516  

随机梯度提升，618  

随机梯度下降，292, 345  

带热重启的随机梯度下降，296  

随机矩阵，101  

随机邻域嵌入，701  

随机优化，292  

随机方差缩减梯度，297  

随机波动率模型，434  

随机权重平均，297  

随机权重平均，458, 645  

停用词移除，24  

鹳鸟案例，80  

直通估计器，311  

应变，692  

基于流的主动学习，650  

应力函数，692  

严格，192  

严格局部最小值，276  

严格凹，278  

严格凸，278  

步长卷积，473  

字符串核，573  

强学习器，612  

强凸，280  

结构化深度网络嵌入，766  

结构风险最小化，195  

结构化数据，425  

语义文本相似度基准，525  

STSB，543  

学生分布，61

---

学生t分布, 61

次导数, 443

次可微的, 282

次微分, 282

次梯度, 282

子模, 651

子词单元, 26

充分统计量, 224

充分统计量, 93, 110, 112, 130

平方和矩阵, 246

求和规则, 38

监督学习, 1

监督PCA, 677

支持向量机, 585

支持向量机回归, 597

支持向量, 585, 588, 597

表面法向预测, 492

代理函数, 312

替代损失函数, 116

替代分裂, 606

可疑巧合, 181

SVD, 260, 383

SVM, 307, 585

SVM回归, 597

SVRG, 297

Swish, 448

swish, 450

瑞士卷, 690

对称, 230

对称SNE, 702

突触连接, 436

同步训练, 454

语法糖, 103

线性方程组, 266

t-SNE, 701

T5, 543

表格数据, 3, 425

高瘦型, 3

切空间, 689

目标, 2, 371

目标数据集, 629

目标域, 637

目标邻居, 552

目标, 778

分类学, 357

泰勒级数, 152

泰勒级数展开, 226

教师强制, 509

温度, 55

调节交叉熵, 361

调节Softmax, 361

模板匹配, 467, 471

张量, 230, 473

张量处理单元, 437, 454

词频矩阵, 25

词项-文档频率矩阵, 706

测试风险, 13

测试集, 13

检验统计量, 200

文本转语音, 518

文本蕴含, 523

TF-IDF, 25

瘦SVD, 260

阈值线性单元, 479

TICE, 222

捆绑, 325

Tikhonov阻尼, 292

Tikhonov正则化, 292

时间序列预测, 505

时不变, 101

TinyImages, 20

TL;DR, 542

词元, 24

拓扑不稳定性, 694

拓扑顺序, 100

全导数, 271

全微分, 271

总变差, 494

TPUs, 437, 454

迹, 236

迹范数, 235

迹技巧, 236

追踪, 446

训练, 7, 107

训练数据, 778

训练集, 2

直推学习, 643

迁移学习, 537, 559, 629

Transformer, 526

Transformer, 426

转移函数, 101

转移核, 101

平移不变性, 467

转置, 230

转置卷积, 487, 492

树宽, 249

三次核, 561

三训练, 642

三角不等式, 213

三对角, 239

三元组模型, 101

三元组损失, 555

真负率, 46

真正率, 46, 172

截断, 511

截断SVD, 264

信赖域优化, 292

管道, 596

图灵机, 504

TV, 494

两部分编码, 186

双尾p值, 200

双尾检验, 187

第一类错误, 199

第一类错误率, 172

第二类错误, 199

第二类极大似然, 145

典型模式, 16

U-Net, 491, 492

U形曲线, 13

UMAP, 705

未调整的Langevin算法, 493

无偏, 160

不确定性, 33

无条件独立, 39

无约束优化, 277

不完备表示, 679

欠定, 266

欠拟合, 13, 124, 127

不可辨识, 356

无信息, 132, 144

无信息先验, 143

---

联合界, 197

唯一性, 667

单位向量, 229

单位向量, 53

酉矩阵, 241

通用函数逼近器, 434

UNK, 26

展开的, 103

不稳定的, 608

非结构化数据, 426

无监督学习, 14

无监督预训练, 632

更新门, 513

上三角矩阵, 240

用户, 741

效用函数, 168

VAE, 683

有效卷积, 471

验证风险, 125, 196

验证集, 13, 124, 196

信息价值, 650

值, 518

梯度消失问题, 429, 447

可变度量, 290

变量选择, 392

方差, 40, 58

信息变化量, 717

变分自编码器, 16, 646, 683

变分自编码器, 674

变分EM, 315

变分推断, 153

变分RNN, 505

方差最大旋转, 673

VC维, 198

vec2seq, 503

向量, 229

向量加法, 710

向量场, 270, 682

向量雅可比积, 272

向量量化, 724

向量空间, 232

向量空间模型, 24

VI, 153

邻域风险最小化, 628

小提琴图, 44

虚拟对抗训练, 644

可见变量, 778

视觉n-gram, 637

视觉场景理解, 49

ViT, 532

维特比解码, 515

VJP, 272

沃罗诺伊迭代, 726

沃罗诺伊镶嵌, 548, 723

VQ, 724

WAIC, 733

唤醒睡眠, 685

沃尔德区间, 159

沃尔德统计量, 200

热启动, 384

热启动, 398

渡边-赤池信息准则, 187

Watson, 170

wavenet, 518

弱学习器, 612

弱监督学习, 655

WebText, 542

权重衰减, 123, 349, 381, 455

权重空间, 577

加权最小二乘法, 376

加权最小二乘问题, 347

加权线性回归, 376

权重, 8, 371

良态的, 238

白化, 256

宽深模型, 748

宽数据, 3

宽格式, 24

宽残差网络, 484

广泛适用信息准则, 187

Widrow-Hoff规则, 294

胜者全取, 55

WMT数据集, 22

Wolfe条件, 291

词语类比问题, 710

词嵌入, 26, 705, 705

词义消歧, 538

词干提取, 24

word2vec, 707

词片, 26

工作响应, 347

世界卫生组织, 222

WSD, 538

Xavier初始化, 453

XGBoost, 619

XOR问题, 427

##### YOLO, 490

ZCA, 258

零计数, 122

零避免, 216

零强制, 217

0-1损失, 6, 169

零填充, 471

零样本分类, 637

零样本学习, 653

零样本任务迁移, 542

锯齿形, 286

---

请提供需要翻译的英文 Markdown 文本。

---

### 参考文献

[AAB21] A. Agrawal, A. Ali, and S. Boyd. "最小失真嵌入". 英文版. 收录于：机器学习基础与趋势 14.3 (2021), 第211–378页.

[AB08] C. Archambeau and F. Bach. "稀疏概率投影". 收录于：NIPS. 2008.

[AB14] G. Alain and Y. Bengio. "正则化自编码器从数据生成分布学到的内容". 收录于：JMLR (2014).

[AC16] D. K. Agarwal and B.-C. Chen. 推荐系统统计方法. 英文版. 第一版. 剑桥大学出版社, 2016.

[Ace] "图灵测试对商业不利". 收录于：(2021).

[AEH+18] S. Abu-El-Haija, B. Perozzi, R. Al-Rfou, and A. A. Alemi. "注意你的步伐：通过图注意力学习节点嵌入". 收录于：神经信息处理系统进展. 2018, 第9180–9190页.

[AEHPAR17] S. Abu-El-Haija, B. Perozzi, and R. Al-Rfou. "通过低秩非对称投影学习边表示". 收录于：2017年ACM信息与知识管理会议论文集. CIKM '17. 2017, 第1787–1796页.

[AEM18] Ö. D. Akyildiz, V. Elvira, and J. Miguez. "增量近端方法：一个概率视角". 收录于：ICASSP. 2018.

[AFF19] C. Aicher, N. J. Foti, and E. B. Fox. "自适应截断时间反向传播以控制梯度偏差". 收录于：(2019). arXiv: 1905.07473 [cs.LG].

[Agg16] C. C. Aggarwal. 推荐系统：教材. 英文版. 第一版, 2016年版. Springer, 2016.

[Agg20] C. C. Aggarwal. 机器学习线性代数与优化：教材. 英文版. 第一版, 2020年版. Springer, 2020.

[AGM19] V. Amrhein, S. Greenland, and B. McShane. "科学家奋起反对统计显著性". 收录于：自然 567.7748 (2019), 第305页.

[Agr70] A. Agrawala. "使用概率教师学习". 收录于：IEEE信息论汇刊 16.4 (1970), 第373–379页.

[AH19] C. Allen and T. Hospedales. "类比解释：迈向理解词嵌入". 收录于：ICML. 2019.

[AHK12] A. Anandkumar, D. Hsu, and S. M. Kakade. "混合模型与隐马尔可夫模型的矩方法". 收录于：COLT. 第23卷. 机器学习研究会议论文集. PMLR, 2012, 第33.1–33.34页.

[Ahm+13] A. Ahmed, N. Shervashidze, S. Narayanamurthy, V. Josifovski, and A. J. Smola. "分布式大规模自然图分解". 收录于：第22届万维网国际会议论文集. ACM. 2013, 第37–48页.

[AK15] J. Andreas and D. Klein. "对数线性模型何时以及为何自归一化？" 收录于：ACL会议论文集. 计算语言学协会, 2015, 第244–249页.

[Aka74] H. Akaike. "统计模型识别的新视角". 收录于：IEEE自动控制汇刊 19.6 (1974).

[AKA91] D. W. Aha, D. Kibler, and M. K. Albert. "基于实例的学习算法". 收录于：机器学习 6.1 (1991), 第37–66页.

[Aky+19] Ö. D. Akyildiz, É. Chouzenoux, V. Elvira, and J. Míguez. "一种概率增量近端梯度方法". 收录于：IEEE信号处理快报 26.8 (2019).

[AL13] N. Ailon and E. Liberty. "一种接近最优的无限制快速Johnson-Lindenstrauss变换". 收录于：ACM算法汇刊 9.3 (2013), 第21:1–21:12页.

[Ala18] J. Alammar. 图解Transformer. 技术报告. 2018.

[Alb+17] M. Alber, P.-J. Kindermans, K. Schütt, K.-R. Müller, and F. Sha. "核方法的随机基属性实证研究". 收录于：NIPS. Curran Associates, Inc., 2017, 第2763–2774页.

[Alb+18] D. Albanese, S. Riccadonna, C. Donati, and P. Franceschi. "最大信息系数分析的实用工具". 英文版. 收录于：GigaScience 7.4 (2018), 第1–8页.

[ALL18] S. Arora, Z. Li, and K. Lyu. "批归一化自动速率调节的理论分析". 收录于：(2018). arXiv: 1812.03981 [cs.LG].

[Alm87] L. B. Almeida. "组合环境中带反馈异步感知器的学习规则". 收录于：第一届国际神经会议论文集. 第2卷. IEEE. 1987, 第609–618页.

[Alo+09] D. Aloise, A. Deshpande, P. Hansen, and P. Popat. "欧几里得平方和聚类的NP难度". 收录于：机器学习 75 (2009), 第245–249页.

[Alp04] E. Alpaydin. 机器学习导论. MIT出版社, 2004.

[Ami+19] E. Amid, M. K. Warmuth, R. Anil, and T. Koren. "基于Bregman散度的鲁棒双温度逻辑损失". 收录于：NIPS. 2019.

[Amo+16] D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané. "具体的"

---

[问题] "人工智能安全问题". In: (2016). arXiv:1606.06565 [cs.AI].

[Amo17] Amoeba. ZCA白化与PCA白化有何区别. Stack Exchange. 2017.

[And01] U. A. Anderson. "炎热与暴力". In: 心理科学当前方向 10.1 (2001), 第33–38页.

[And+18] R. Anderson, J. Huchette, C. Tjandraatmadja, 和 J. P. Vielma. "训练神经网络的强凸松弛与混合整数规划公式". In: (2018). arXiv: 1811.01988 [math.OC].

[Ani+20] R. Anil, V. Gupta, T. Koren, K. Regan, 和 Y. Singer. "深度学习可扩展二阶优化". In: (2020). arXiv:2002.09018 [cs.LG].

[Ans73] F. J. Anscombe. "统计分析中的图形". In: 美国统计学家 27.1 (1973), 第17–21页.

[Arc+19] F. Arcadu, F. Benmansour, A. Maunz, J. Willis, Z. Haskova, 和 M. Prunotto. "深度学习算法预测个体患者糖尿病视网膜病变进展". en. In: NPJ数字医学 2 (2019), 第92页.

[AO03] J.-H. Ahn 和 J.-H. Oh. "主成分分析的有约束EM算法". In: 神经计算 15 (2003), 第57–65页.

[Ard+20] R. Ardila, M. Branson, K. Davis, M. Kohler, J. Meyer, M. Henretty, R. Morais, L. Saunders, F. Tyers, 和 G. Weber. "Common Voice：大规模多语言语音语料库". In: 第12届语言资源与评估会议论文集. 2020, 第4218–4222页.

[Arj21] M. Arjovsky. "机器学习中的分布外泛化". In: (2021). arXiv:2103.02667 [stat.ML].

[Arn+19] S. M. R. Arnold, P.-A. Manzagol, R. Babanezhad, I. Mitliagkas, 和 N. Le Roux. "通过传递历史梯度降低在线优化的方差". In: NIPS. 2019.

[Aro+16] S. Arora, Y. Li, Y. Liang, T. Ma, 和 A. Risteski. "基于PMI的词嵌入的潜变量模型方法". In: 计算语言学协会汇刊 4 (2016), 第385–399页.

[Aro+19] L. Aroyo, A. Dumitrache, O. Inel, Z. Szlávik, B. Timmermans, 和 C. Welty. "众包包容性：处理标注数据中的观点多样性、视角多样性和歧义性". In: 万维网大会. WWW '19. 计算机协会, 2019, 第1294–1295页.

[Aro+21] R. Arora 等. 深度学习理论. 2021.

[ARZP19] R. Al-Rfou, D. Zelle, 和 B. Perozzi. "DDGK：用于深度散度图核的图表示学习". In: 2019年世界万维网大会论文集 (2019).

[AS17] A. Achille 和 S. Soatto. "深度表示中不变性和解缠性的涌现". In: (2017). arXiv: 1706.01350 [cs.LG].

[AS19] A. Achille 和 S. Soatto. "深度神经网络中的信息在哪里？" In: (2019). arXiv: 1905.12213 [cs.LG].

[Ash18] J. Asher. "谋杀案上升？让我们谈谈天气". In: 纽约时报 (2018).

[ASR15] A. Ali, S. M. Shamsuddin, 和 A. L. Ralescu. "类别不平衡问题的分类：综述". In: 国际高级软计算与应用杂志 7.3 (2015).

[Ath+19] B. Athiwaratkun, M. Finzi, P. Izmailov, 和 A. G. Wilson. "未标记数据存在许多一致的解释：为什么应该取平均". In: 国际学习表征会议. 2019.

[AV07] D. Arthur 和 S. Vassilvitskii. "k-means++：谨慎初始化的优势". In: 第18届ACM-SIAM离散算法研讨会论文集. 2007, 第1027–1035页.

[AWS19] E. Amid, M. K. Warmuth, 和 S. Srinivasan. "基于Tsallis散度的两温度逻辑回归". In: 人工智能与统计国际会议. 2019.

[Axl15] S. Axler. 线性代数应该这样学. 2015.

[BA10] R. Bailey 和 J. Addison. Nadaraya-Watson估计的平滑分布形式. 技术报告 10-30. 伯明翰大学, 2010.

[BA97a] A. Bowman 和 A. Azzalini. 数据分析应用平滑技术. 牛津, 1997.

[BA97b] L. A. Breslow 和 D. W. Aha. "简化决策树：综述". In: 知识工程评论 12.1 (1997), 第1–40页.

[Bab19] S. Babu. 2019年基于深度学习的人体姿态估计指南. 2019.

[Bac+16] O. Bachem, M. Lucic, H. Hassani, 和 A. Krause. "快速且理论上保证的k均值初始种子". In: NIPS. 2016, 第55–63页.

[Bah+12] B. Bahmani, B. Moseley, A. Vattani, R. Kumar, 和 S. Vassilvitskii. "可扩展的k-Means++". In: VLDB. 2012.

[Bah+20] Y. Bahri, J. Kadmon, J. Pennington, S. Schoenholz, J. Sohl-Dickstein, 和 S. Ganguli. "深度学习的统计力学". In: 凝聚态物理年度综述 (2020).

[BAP14] P. Bachman, O. Alsharif, 和 D. Precup. "基于伪集成的学习". In: 神经信息处理系统进展. 2014, 第3365–3373页.

[Bar09] M. Bar. "主动大脑：预测的记忆". en. In: 皇家学会哲学汇刊B辑：生物科学 364.1521 (2009), 第1235–1243页.

[Bar19] J. T. Barron. "通用且自适应的鲁棒损失函数". In: 计算机视觉与模式识别会议. 2019.

[Bat+18] P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V. Zambaldi, M. Malinowski, A. Tacchetti, D. Raposo, A. Santoro, R. Faulkner, 等. "关系归纳偏置、深度学习与图网络". In: arXiv预印本 arXiv:1806.01261 (2018).

[BB08] O. Bousquet 和 L. Bottou. "大规模学习的权衡". In: NIPS. 2008, 第161–168页.

---

[BB11] L. Bottou 和 O. Bousquet。“大规模学习的权衡”。载于：《机器学习优化》。S. Sra、S. Nowozin 和 S. J. Wright 编。MIT出版社，2011年，第351–368页。

1. esian

    -ate Carlo”。

    -math.OC]。

[BC17] D. Beck 和 T. Cohn。“使用高斯过程学习字符串上的核”。载于：《第八届国际自然语言处理联合会议论文集（第2卷：短论文）》。第2卷。2017年，第67–73页。

[BCB15] D. Bahdanau、K. Cho 和 Y. Bengio。“通过联合学习对齐和翻译的神经机器翻译”。载于：ICLR。2015年。

[BCD01] L. Brown、T. Cai 和 A. DasGupta。“二项比例区间估计”。载于：《统计科学》16.2（2001年），第101–133页。

[BCN18] L. Bottou、F. E. Curtis 和 J. Nocedal。“大规模机器学习的优化方法”。载于：《SIAM评论》60.2（2018年），第223–311页。

[BCV13] Y. Bengio、A. Courville 和 P. Vincent。“表示学习：综述与新视角”。英文。载于：《IEEE模式分析与机器智能》35.8（2013年），第1798–1828页。

[BD20] B. Barz 和 J. Denzler。“我们是在测试数据上训练的吗？清除CIFAR中的近重复”。载于：《成像杂志》6.6（2020年）。

[BD21] D. G. T. Barrett 和 B. Dherin。“隐式梯度正则化”。载于：ICLR。2021年。

[BD87] G. Box 和 N. Draper。《经验模型构建与响应曲面》。Wiley，1987年。

[BDEL03] S. Ben-David、N. Eiron 和 P. M. Long。“关于近似最大化一致性的难度”。载于：《计算机与系统科学杂志》66.3（2003年），第496–514页。

[Bel+19] M. Belkin、D. Hsu、S. Ma 和 S. Mandal。“调和现代机器学习实践与经典偏差-方差权衡”。载于：《美国国家科学院院刊》116.32（2019年），第15849–15854页。

[Ben+04a] Y. Bengio、O. Delalleau、N. Roux、J. Paiement、P. Vincent 和 M. Ouimet。“学习特征函数连接谱嵌入与核PCA”。载于：《神经计算》16（2004年），第2197–2219页。

[Ben+04b] Y. Bengio、J.-F. Paiement、P. Vincent、O. Delalleau、N. L. Roux 和 M. Ouimet。“LLE、Isomap、MDS、特征映射与谱聚类的样本外扩展”。载于：NIPS。MIT出版社，2004年，第177–184页。

[Ben+15a] S. Bengio、O. Vinyals、N. Jaitly 和 N. Shazeer。“用于循环神经网络序列预测的调度采样”。载于：NIPS。2015年。

[Ben+15b] Y. Bengio、D.-H. Lee、J. Bornschein、T. Mesnard 和 Z. Lin。“迈向生物合理的深度学习”。载于：（2015年）。arXiv: 1502.04156 [cs.LG]。

[Ben+17] A. Benavoli、G. Corani、J. Demsar 和 M. Zaffalon。“是时候改变了：通过贝叶斯分析比较多个分类器的教程”。载于：JMLR（2017年）。

[Ber15] D. Bertsekas。《凸优化算法》。Athena Scientific，2015年。

[Ber16] D. Bertsekas。《非线性规划》。第三版。Athena Scientific，2016年。

[Ber+19a] D. Berthelot、N. Carlini、E. D. Cubuk、A. Kurakin、K. Sohn、H. Zhang 和 C. Raffel。“Remixmatch：基于分布对齐与增强锚定的半监督学习”。载于：《arXiv预印本 arXiv:1911.09785》（2019年）。

[Ber+19b] D. Berthelot、N. Carlini、I. Goodfellow、N. Papernot、A. Oliver 和 C. Raffel。“Mixmatch：一种整体性的半监督学习方法”。载于：《神经信息处理系统进展》。2019年，第5049–5059页。

[Ber+21] J. Berner、P. Grohs、G. Kutyniok 和 P. Petersen。“深度学习的现代数学”。载于：（2021年）。arXiv: 2105.04026 [cs.LG]。

[Ber85] J. Berger。“贝叶斯推销术”。载于：《贝叶斯推断与决策技术及其应用：Bruno de Finetti纪念文集》。P. K. Goel 和 A. Zellner 编。North-Holland，1985年。

[Ber99] D. Bertsekas。《非线性规划》。第二版。Athena Scientific，1999年。

[Bey+19] M. Beyeler、E. L. Rounds、K. D. Carlson、N. Dutt 和 J. L. Krichmar。“稀疏编码和降维的神经关联”。英文。载于：《PLoS计算生物学》15.6（2019年），e1006908。

[Bey+20] L. Beyer、O. J. Hénaff、A. Kolesnikov、X. Zhai 和 A. van den Oord。“我们完成ImageNet了吗？”载于：（2020年）。arXiv: 2006.07159 [cs.CV]。

[BFO84] L. Breiman、J. Friedman 和 R. Olshen。《分类与回归树》。Wadsworth，1984年。

[BG11] P. Buhlmann 和 S. van de Geer。《高维数据统计：方法、理论与应用》。Springer，2011年。

[BH07] P. Buhlmann 和 T. Hothorn。“提升算法：正则化、预测与模型拟合”。载于：《统计科学》22.4（2007年），第477–505页。

[BH69] A. Bryson 和 Y.-C. Ho。《应用最优控制：优化、估计与控制》。Blaisdell出版公司，1969年。

[BH86] J. Barnes 和 P. Hut。“一种分层O(N log N)力计算算法”。载于：《自然》324.6096（1986年），第446–449页。

[BH89] P. Baldi 和 K. Hornik。“神经网络与主成分分析：无局部极小值的示例学习”。载于：《神经网络》2（1989年），第53–58页。

[Bha+19] A. Bhadra、J. Datta、N. G. Polson 和 B. T. Willard。“Lasso与Horseshoe相遇：综述”。载于：《贝叶斯分析》34.3（2019年），第405–427页。

[Bha+20] A. Bhadra、J. Datta、Y. Li 和 N. Polson。“用于机器学习的Horseshoe正则化”

---

在复杂且深度模型中”。载于：《国际统计评论》88.2（2020年），第302–320页。

[BHM92] J. S. Bridle、A. J. Heading 和 D. J. MacKay。“无监督分类器、互信息与‘幻影目标’”。载于：《神经信息处理系统进展》。1992年，第1096–1101页。

[BI19] P. Barham 和 M. Isard。“机器学习系统陷入困境”。载于：《操作系统热点主题研讨会论文集》。HotOS '19。美国计算机协会，2019年，第177–183页。

[Bis06] C. Bishop。《模式识别与机器学习》。Springer，2006年。

[Bis94] C. M. Bishop。《混合密度网络》。技术报告。NCRG 4288。神经计算研究组，阿斯顿大学计算机科学系，1994年。

[Bis99] C. Bishop。“贝叶斯主成分分析”。载于：《NIPS》。1999年。

[BJ05] F. Bach 和 M. Jordan。《典型相关分析的概率解释》。技术报告。688。加州大学伯克利分校，2005年。

[BJM06] P. Bartlett、M. Jordan 和 J. McAuliffe。“凸性、分类与风险界”。载于：《美国统计协会杂志》101.473（2006年），第138–156页。

[BK07] R. M. Bell 和 Y. Koren。“Netflix Prize 挑战赛的教训”。载于：《SIGKDD探索通讯》9.2（2007年），第75–79页。

[BK20] E. M. Bender 和 A. Koller。“攀登 NLU：数据时代的意义、形式与理解”。载于：《ACL 会议论文集》。2020年，第5185–5198页。

[BKCl7] V. Badrinarayanan、A. Kendall 和 R. Cipolla。“SegNet：用于图像分割的深度卷积编码器-解码器架构”。载于：《IEEE PAMI》39.12（2017年）。

[BKH16] J. L. Ba、J. R. Kiros 和 G. E. Hinton。“层归一化”。载于：（2016年）。arXiv: 1607.06450 [stat.ML]。

[BKL10] S. Bird、E. Klein 和 E. Loper。《使用 Python 进行自然语言处理：用自然语言工具包分析文本》。2010年。

[BL04] P. Bickel 和 E. Levina。“Fisher 线性判别函数、‘朴素贝叶斯’以及当变量远多于观测值时的一些替代方案的理论”。载于：《伯努利》10（2004年），第989–1010页。

[BL07a] C. M. Bishop 和 J. Lasserre。“生成式还是判别式？兼得两者之长”。载于：《贝叶斯统计 8》。2007年。

[BL07b] J. A. Bullinaria 和 J. P. Levy。“从词共现统计中提取语义表示：一项计算研究”。英文。载于：《行为研究方法》39.3（2007年），第510–526页。

[BL12] J. A. Bullinaria 和 J. P. Levy。“从词共现统计中提取语义表示：停用词表、词干提取和奇异值分解”。英文。载于：《行为研究方法》44.3（2012年），第890–907页。

[BL88] D. S. Broomhead 和 D Lowe。“多变量函数插值与自适应网络”。载于：《复杂系统》（1988年）。

[BLK17] O. Bachem、M. Lucic 和 A. Krause。“在常数轮内实现分布式且可证明良好的 k-means 初始化”。载于：《ICML》。2017年，第292–300页。

[Blo20] M. Blondel。《自动微分》。2020年。

[BLV19] X. Bouthillier、C. Laurent 和 P. Vincent。“不可重现的研究是可重现的”。载于：《ICML》。第97卷。机器学习研究论文集。PMLR，2019年，第725–734页。

[BM98] A. Blum 和 T. Mitchell。“利用协同训练结合标记与未标记数据”。载于：《第十一届计算学习理论年度会议论文集》。1998年，第92–100页。

[BN01] M. Belkin 和 P. Niyogi。“拉普拉斯特征映射与用于嵌入和聚类的谱技术”。载于：《NIPS》。2001年，第585–591页。

[BNJ03] D. Blei、A. Ng 和 M. Jordan。“潜在狄利克雷分配”。载于：《JMLR》3（2003年），第993–1022页。

[Bo+08] L. Bo、C. Sminchisescu、A. Kanaujia 和 D. Metaxas。“大规模条件三维预测的快速算法”。载于：《CVPR》。2008年。

[Boh92] D. Bohning。“多项逻辑回归算法”。载于：《统计数学研究所年鉴》44（1992年），第197–200页。

[Bon13] S. Bonnabel。“黎曼流形上的随机梯度下降”。载于：《IEEE 自动控制汇刊》58.9（2013年），第2217–2229页。

[Bos+16] D. Boscaini、J. Masci、E. Rodolà 和 M. Bronstein。“利用各向异性卷积神经网络学习形状对应”。载于：《神经信息处理系统进展》。2016年，第3189–3197页。

[Bot+13] L. Bottou、J. Peters、J. Quiñonero-Candela、D. X. Charles、D. M. Chickering、E. Portugal、D. Ray、P. Simard 和 E. Snelson。“反事实推理与学习系统：以计算广告为例”。载于：《JMLR》14（2013年），第3207–3260页。

[Bow+15] S. R. Bowman、G. Angeli、C. Potts 和 C. D. Manning。“用于学习自然语言推理的大规模标注语料库”。载于：《EMNLP》。计算语言学协会，2015年，第632–642页。

[BPC20] I. Beltagy、M. E. Peters 和 A. Cohan。“Longformer：长文档 Transformer”。载于：《CoRR》abs/2004.05150（2020年）。arXiv: 2004.05150。

[Bre01] L. Breiman。“随机森林”。载于：《机器学习》45.1（2001年），第5–32页。

[Bre96] L. Breiman。“Bagging 预测器”。载于：《机器学习》24（1996年），第123–140页。

[Bri50] G. W. Brier。“用概率形式表达的预测验证”。载于：《每月天气评论》78.1（1950年），第1–3页。

[Bri90] J. Bridle。“前馈分类网络输出的概率解释及其与统计模式识别的关系”。

---

"tion". 载于：神经计算：算法、架构与应用. 由 F. F. Soulie 和 J. Herault 编辑. Springer Verlag, 1990, pp. 227–236.

[Bro+17a] M. M. Bronstein, J Bruna, Y LeCun, A Szlam, and P Vandergheynst. "几何深度学习：超越欧几里得数据". 载于：IEEE Signal Process. Mag. 34.4 (2017), pp. 18–42.

[Bro+17b] M. M. Bronstein, J. Bruna, Y. LeCun, A. Szlam, and P. Vandergheynst. "几何深度学习：超越欧几里得数据". 载于：IEEE Signal Processing Magazine 34.4 (2017), pp. 18–42.

[Bro19] J. Brownlee. 计算机视觉深度学习 - 机器学习精通. 访问日期：2020年6月30日. Machine Learning Mastery, 2019.

[Bro+20] T. B. Brown et al. "语言模型是少样本学习者". 载于：(2020). arXiv: 2005.14165 [cs.CL].

[Bro+21] A. Brock, S. De, S. L. Smith, and K. Simonyan. "无归一化的高性能大规模图像识别". 载于：(2021). arXiv: 2102.06171 [cs.CV].

[BRR18] T. D. Bui, S. Ravi, and V. Ramavajjala. "神经图机器：利用图学习神经网络". 载于：WSDM. 2018.

[Bru+14] J. Bruna, W. Zaremba, A. Szlam, and Y. Lecun. "图上的谱网络和局部连接网络 国际学习表征会议(ICLR2014)". 载于：CBLS, April (2014).

[Bru+19] G. Brunner, Y. Liu, D. Pascual, O. Richter, and R. Wattenhofer. "关于Transformer模型中自注意力作为解释的有效性". 载于：(2019). arXiv:1908.04211 [cs.CL].

[BS02] M. Balasubramanian and E. L. Schwartz. "Isomap算法与拓扑稳定性". 英文. 载于：Science 295.5552 (2002), p. 7.

[BS16] P. Baldi and P. Sadowski. "局部学习理论、学习信道与反向传播的最优性". 载于：Neural Netw. 83 (2016), pp. 51–74.

[BS17] D. M. Blei and P. Smyth. "科学与数据科学". 英文. 载于：Proc. Natl. Acad. Sci. U. S. A. (2017).

[BS21] S. Bubeck and M. Sellke. "通过等周不等式的鲁棒性普遍定律". 载于：NIPS 34 (Dec. 2021), pp. 28811–28822.

[BS94] J. Bernardo and A. Smith. 贝叶斯理论. John Wiley, 1994.

[BS97] A. J. Bell and T. J. Sejnowski. "自然场景的“独立成分”是边缘滤波器". 英文. 载于：Vision Res. 37.23 (1997), pp. 3327–3338.

[BT04] G. Bouchard and B. Triggs. "生成式与判别式分类器之间的权衡". 载于：IASC International Symposium on Computational Statistics (COMPSTAT '04). 2004.

[BT08] D. Bertsekas and J. Tsitsiklis. 概率导论. 第二版. Athena Scientific, 2008.

[BT09] A Beck and M Teboulle. "一种用于线性逆问题的快速迭代收缩阈值算法". 载于：SIAM J. Imaging Sci. 2.1 (2009), pp. 183–202.

[BT73] G. Box and G. Tiao. 统计分析中的贝叶斯推断. Addison-Wesley, 1973.

[Bul11] A. D. Bull. “高效全局优化算法的收敛速率”. 载于：JMLR 12 (2011), 2879–2904.

[Bur10] C. J. C. Burges. "降维：导览". 英文. 载于：Foundations and Trends in Machine Learning (2010).

[BV04] S. Boyd and L. Vandenberghe. 凸优化. Cambridge, 2004.

[BW08] P. L. Bartlett and M. H. Wegkamp. "使用铰链损失的可拒绝分类". 载于：JMLR 9.Aug (2008), pp. 1823–1840.

[BW88] J. Berger and R. Wolpert. 似然原理. 第二版. The Institute of Mathematical Statistics, 1988.

[BWL19] Y. Bai, Y.-X. Wang, and E. Liberty. "ProxQuant：通过近端算子实现量化神经网络". 载于：ICLR. 2019.

[BY03] P. Buhlmann and B. Yu. “使用L2损失的Boosting：回归与分类”. 载于：JASA 98.462 (2003), pp. 324–339.

[Byr+16] R Byrd, S Hansen, J Nocedal, and Y Singer. "一种用于大规模优化的随机拟牛顿方法". 载于：SIAM J. Optim. 26.2 (2016), pp. 1008–1031.

[BZ20] A. Barbu and S.-C. Zhu. 蒙特卡洛方法. 英文. Springer, 2020.

[Cal20] O. Calin. 深度学习架构：一种数学方法. 英文. 第一版. Springer, 2020.

[Cao+18] Z. Cao, G. Hidalgo, T. Simon, S.-E. Wei, and Y. Sheikh. "OpenPose：使用部分亲和场的实时多人二维姿态估计". 载于：(2018). arXiv: 1812.08008 [cs.CV].

[CAS16] P. Covington, J. Adams, and E. Sargin. "用于YouTube推荐的深度神经网络". 载于：第10届ACM推荐系统会议论文集. RecSys'16. Association for Computing Machinery, 2016, pp. 191–198.

[CB02] G. Casella and R. Berger. 统计推断. 第二版. Duxbury, 2002.

[CBD15] M. Courbariaux, Y. Bengio, and J.-P. David. "BinaryConnect：在传播过程中使用二值权重训练深度神经网络". 载于：NIPS. 2015.

[CC07] H. Choi and S. Choi. "鲁棒核Isomap". 载于：Pattern Recognit. 40.3 (2007), pp. 853–862.

[CCD17] B. P. Chamberlain, J. Clough, and M. P. Deisenroth. "双曲空间中的图神经嵌入". 载于：arXiv preprint arXiv:1705.10359 (2017).

---

[CD14] K. Chaudhuri 和 S. Dasgupta。"最近邻分类的收敛速度"。载于：NIPS. 2014年。

[CD88] W. Cleveland 和 S. Devlin。"局部加权回归：一种通过局部拟合进行回归分析的方法"。载于：JASA 83.403 (1988年)，第596–610页。

[CDL16] J. Cheng、L. Dong 和 M. Lapata。"用于机器阅读的长短期记忆网络"。载于：EMNLP。计算语言学协会，2016年，第551–561页。

[CDL19] S. Chen、E. Dobriban 和 J. H. Lee。"不变性降低方差：理解深度学习及更广泛领域中的数据增强"。载于：(2019年)。 arXiv: 1907.10905 [stat.ML]。

[CDS02] M. Collins、S. Dasgupta 和 R. E. Schapire。"主成分分析在指数族上的推广"。载于：NIPS-14. 2002年。

[CEL19] Z. Chen、J. B. Estrach 和 L. Li。"使用线图神经网络的监督社区检测"。载于：第七届国际学习表征会议 ICLR 2019. 2019年。

[Cer+17] D. Cer、M. Diab、E. Agirre、I. Lopez-Gazpio 和 L. Specia。"SemEval-2017任务1：语义文本相似度的多语言与跨语言聚焦评测"。载于：第11届语义评测国际研讨会论文集(SemEval-2017)。计算语言学协会，2017年，第1–14页。

[CFD10] Y. Cui、X. Z. Fern 和 J. G. Dy。"学习多个非冗余聚类"。载于：ACM 知识发现与数据挖掘汇刊 4.3 (2010年)。

[CG16] T. Chen 和 C. Guestrin。"XGBoost：一种可扩展的树提升系统"。载于：KDD. ACM，2016年，第785–794页。

[CG18] J. Chen 和 Q. Gu。"缩小训练深度神经网络中自适应梯度方法的泛化差距"。载于：(2018年)。 arXiv: 1806.06763 [cs.LG]。

[CGG17] S. E. Chazan、J. Goldberger 和 S. Gannot。"使用深度专家混合模型的语音增强"。载于：(2017年)。 arXiv: 1703.09302 [cs.SD]。

[CGW21] W. Chen、X. Gong 和 Z. Wang。"在四个GPU小时内完成ImageNet上的神经架构搜索：一个受理论启发的视角"。载于：ICLR. 2021年。

[CH67] T. Cover 和 P. Hart。"最近邻模式分类"。载于：IEEE 信息论汇刊 13.1 (1967年)，第21–27页。

[CH90] K. W. Church 和 P. Hanks。"词语联想规范、互信息与词典学"。载于：计算语言学 (1990年)。

[Cha+01] O. Chapelle、J. Weston、L. Bottou 和 V. Vapnik。"邻域风险最小化"。载于：NIPS. MIT Press，2001年，第416–422页。

[Cha+17] P. Chaudhari、A. Choromanska、S. Soatto、Y. LeCun、C. Baldassi、C. Borgs、J. Chayes、L. Sagun 和 R. Zecchina。"熵-SGD：将梯度下降偏向宽谷"。载于：ICLR. 2017年。

[Cha+19a] I. Chami、Z. Ying、C. Ré 和 J. Leskovec。"双曲图卷积神经网络"。载于：神经信息处理系统进展。2019年，第4869–4880页。

[Cha+19b] J. J. Chandler、I. Martinez、M. M. Finucane、J. G. Terziev 和 A. M. Resch。"代表数据发言：研究者说什么以及观众如何选择"。中文。载于：评价评论 (2019年)，第193841X19834968页。

[Cha+21] I. Chami、S. Abu-El-Haija、B. Perozzi、C. Ré 和 K. Murphy。"图上的机器学习：一个模型与综合分类法"。载于：JMLR (2021年)。

[Cha21] S. H. Chan。数据科学概率导论。密歇根出版社，2021年。

[Che+16] H.-T. Cheng 等人。"推荐系统的广度和深度学习"。载于：(2016年)。 arXiv:1606.07792 [cs.LG]。

[Che+20a] T. Chen、S. Kornblith、M. Norouzi 和 G. Hinton。"视觉表征对比学习的一个简单框架"。载于：ICML. 2020年。

[Che+20b] T. Chen、S. Kornblith、M. Norouzi 和 G. Hinton。"视觉表征对比学习的一个简单框架"。载于：ICML. 2020年。

[Che+20c] T. Chen、S. Kornblith、K. Swersky、M. Norouzi 和 G. Hinton。"大型自监督模型是强大的半监督学习者"。载于：NIPS. 2020年。

[Chi+19a] W.-L. Chiang、X. Liu、S. Si、Y. Li、S. Bengio 和 C.-J. Hsieh。"Cluster-GCN：训练深度大规模图卷积网络的高效算法"。载于：ACM SIGKDD 知识发现与数据挖掘会议(KDD)。2019年。

[Chi+19b] R. Child、S. Gray、A. Radford 和 I. Sutskever。"使用稀疏 Transformer 生成长序列"。载于：CoRR abs/1904.10509 (2019年)。 arXiv: 1904.10509。

[CHL05] S. Chopra、R. Hadsell 和 Y. LeCun。"判别式学习相似度度量及其在人脸验证中的应用"。中文。载于：CVPR. 2005年。

[Cho+14a] K. Cho、B. van Merrienboer、C. Gulcehre、D. Bahdanau、F. Bougares、H. Schwenk 和 Y. Bengio。"使用 RNN 编码器-解码器学习短语表征用于统计机器翻译"。载于：EMNLP. 2014年。

[Cho+14b] K. Cho、B. Van Merriënboer、D. Bahdanau 和 Y. Bengio。"神经机器翻译的性质：编码器-解码器方法"。载于：arXiv 预印本 arXiv:1409.1259 (2014年)。

[Cho+15] Y. Chow、A. Tamar、S. Mannor 和 M. Pavone。"风险敏感与稳健决策：一种 CVaR 优化方法"。载于：NIPS. 2015年，第1522–1530页。

[Cho17] F. Chollet。Python 深度学习。Manning，2017年。

[Cho+19] K. Choromanski、M. Rowland、W. Chen 和 A. Weller。"统一正交蒙特卡洛方法"。载于：第36届国际机器学习会议论文集，ICML 2019，2019年6月9-15日，长滩。

---

加利福尼亚州，美国。由K. Chaudhuri和R. Salakhutdinov编辑。第97卷。机器学习研究论文集。PMLR，2019年，第1203–1212页。

[Cho+20a] K. Choromanski等。 "面向蛋白质的线性可扩展长上下文Transformer掩码语言建模"。载于：(2020)。arXiv: 2006.03555 [cs.LG]。

[Cho+20b] K. Choromanski等。 "使用Performers重新思考注意力机制"。载于：CoRR abs/2009.14794 (2020)。arXiv:2009.14794。

[Cho21] F. Chollet。 《Python深度学习（第二版）》。Manning出版社，2021年。

[Cho70] C Chow。 "关于最优识别错误与拒绝折衷"。英文。载于：IEEE信息论汇刊 16.1 (1970年1月)，第41–46页。

[Chr20] B. Christian。 《对齐问题：机器学习与人类价值观》。英文。第一版。W. W. Norton & Company，2020年。

[Chu+15] J. Chung, K. Kastner, L. Dinh, K. Goel, A. Courville, 和 Y. Bengio。 "面向序列数据的循环潜变量模型"。载于：NIPS（神经信息处理系统大会）。2015年。

[Chu+22] H. W. Chung等。 "扩展指令微调语言模型"。载于：(2022年10月)。arXiv: 2210.11416 [cs.LG]。

[Chu97] F. Chung。 《谱图理论》。AMS（美国数学学会），1997年。

[Cir+10] D. C. Ciresan, U. Meier, L. M. Gambardella, 和 J. Schmidhuber。 "用于手写数字识别的深度大型简单神经网络"。载于：神经计算 22.12 (2010年)，第3207–3220页。

[Cir+11] D. C. Ciresan, U. Meier, J. Masci, L. M. Gambardella, 和 J. Schmidhuber。 "用于图像分类的灵活高性能卷积神经网络"。载于：IJCAI（国际人工智能联合会议）。2011年。

[CL96] B. P. Carlin 和 T. A. Louis。 《数据分析的贝叶斯与经验贝叶斯方法》。Chapman and Hall出版社，1996年。

[Cla21] A. Clayton。 《伯努利谬误：统计逻辑谬误与现代科学危机》。英文。哥伦比亚大学出版社，2021年。

[CLX15] S. Cao, W. Lu, 和 Q. Xu。 "Grarep：利用全局结构信息学习图表示"。载于：第24届ACM国际信息与知识管理会议论文集。ACM（美国计算机协会）。2015年，第891–900页。

[CNB17] C. Chelba, M. Norouzi, 和 S. Bengio。 "使用循环神经网络估计的N-gram语言建模"。载于：(2017)。arXiv:1703.10724 [cs.CL]。

[Coh+17] G. Cohen, S. Afshar, J. Tapson, 和 A. van Schaik。 "EMNIST：MNIST到手写字母的扩展"。载于：(2017)。arXiv: 1702.05373 [cs.CV]。

[Coh94] J. Cohen。 "地球是圆的（p < .05）"。载于：美国心理学家 49.12 (1994年)，第997–1003页。

[Con+17] A. Conneau, D. Kiela, H. Schwenk, L. Barrault, 和 A. Bordes。 "从自然语言推理数据监督学习通用句子表示"。载于：arXiv预印本 arXiv:1705.02364 (2017)。

[Coo05] J. Cook。 《Beta不等式的精确计算》。技术报告。M. D. Anderson癌症中心，生物统计系，2005年。

[CP10] M. A. Carreira-Perpinan。 "用于降维的弹性嵌入算法"。载于：ICML（国际机器学习大会）。2010年。

[CP19] A. Coenen 和 A. Pearce。 《理解UMAP》。2019年。

[CPS06] K. Chellapilla, S. Puri, 和 P. Simard。 "用于文档处理的高性能卷积神经网络"。载于：第10届国际手写识别前沿研讨会。2006年。

[CRW17] K. Choromanski, M. Rowland, 和 A. Weller。 "结构化随机正交嵌入的不合理有效性"。载于：NIPS（神经信息处理系统大会）。2017年。

[CS20] F. E. Curtis 和 K Scheinberg。 "自适应随机优化：分析随机优化算法的框架"。载于：IEEE信号处理杂志 37.5 (2020年)，第32–42页。

[Csu17] G. Csurka。 "视觉应用的域自适应：综合综述"。载于：计算机视觉应用中的域自适应。由G. Csurka编辑。2017年。

[CT06] T. M. Cover 和 J. A. Thomas。 《信息论基础》。第二版。John Wiley出版社，2006年。

[CT91] T. M. Cover 和 J. A. Thomas。 《信息论基础》。John Wiley出版社，1991年。

[Cub+19] E. D. Cubuk, B. Zoph, D. Mane, V. Vasudevan, 和 Q. V. Le。 "AutoAugment：从数据中学习增强策略"。载于：CVPR（计算机视觉与模式识别大会）。2019年。

[CUH16] D.-A. Clevert, T. Unterthiner, 和 S. Hochreiter。 "通过指数线性单元（ELUs）实现快速准确的深度网络学习"。载于：ICLR（国际学习表征大会）。2016年。

[Cui+19] X. Cui, K. Zheng, L. Gao, B. Zhang, D. Yang, 和 J. Ren。 "基于图像框架的多尺度空间-光谱卷积网络用于高光谱影像分类"。英文。载于：遥感 11.19 (2019年)，第2220页。

[Cur+17] J. D. Curtó, I. C. Zarza, F Yang, A Smola, F Torre, C. W. Ngo, 和 L Gool。 "McKernel：用于对数线性时间近似核扩展的库"。载于：(2017)。arXiv:1702.08159v14 [cs.LG]。

[Cyb89] G. Cybenko。 "S型函数叠加的逼近"。载于：控制、信号与系统数学 2 (1989年)，第303–331页。

[D'A+20] A. D'Amour等。 "欠规范对现代机器学习可信度构成挑战"。载于：(2020)。arXiv: 2011.03395 [cs.LG]。

[Dah+11] G. E. Dahl, D. Yu, L. Deng, 和 A. Acero。 "基于上下文相关DBN-HMM的大词汇量连续语音识别"。载于：ICASSP（国际声学、语音与信号处理大会）。IEEE（电气电子工程师学会），2011年，第4688–4691页。

---

[Dai+19] Z. Dai, Z. Yang, Y. Yang, J. G. Carbonell, Q. V. Le, 和 R. Salakhutdinov. "Transformer-XL：超越固定长度上下文的注意力语言模型". 收录于：Proc. ACL. 2019, pp. 2978–2988.

[Dao+19] T. Dao, A. Gu, A. J. Ratner, V. Smith, C. De Sa, 和 C. Re. "现代数据增强的核理论". 收录于：ICML. 2019.

[Daul7] J. Daunizeau. "正态变量Sigmoid和Softmax映射统计矩的半解析近似". 收录于：(2017). arXiv: 1703.00091 [stat.ML].

[Day+95] P. Dayan, G. Hinton, R. Neal, 和 R. Zemel. "Helmholtz机". 收录于：Neural Networks 9.8 (1995).

[DB18] A. Defazio 和 L. Bottou. "论方差缩减优化对深度学习无效性的研究". 收录于：(2018). arXiv: 1812.04529 [cs.LG].

[DBLJ14] A. Defazio, F. Bach, 和 S. Lacoste-Julien. "SAGA：一种支持非强凸复合目标的快速增量梯度方法". 收录于：NIPS. Curran Associates, Inc., 2014, pp. 1646–1654.

[DDDM04] I Daubechies, M Defrise, 和 C De Mol. "带有稀疏约束的线性逆问题的迭代阈值算法". 收录于：Commun. Pure Appl. Math. Advances in E 57.11 (2004), pp. 1413–1457.

[Dee+90] S. Deerwester, S. Dumais, G. Furnas, T. Landauer, 和 R. Harshman. "基于潜在语义分析的索引". 收录于：J. of the American Society for Information Science 41.6 (1990), pp. 391–407.

[DeG70] M. DeGroot. 最优统计决策. McGraw-Hill, 1970.

[Den+12] J. Deng, J Krause, A. C. Berg, 和 L. Fei-Fei. "规避风险：在大规模视觉识别中优化准确率与特异性的权衡". 收录于：CVPR. 2012, pp. 3450–3457.

[Den+14] J. Deng, N. Ding, Y. Jia, A. Frome, K. Murphy, S. Bengio, Y. Li, H. Neven, 和 H. Adam. "使用标签关系图的大规模目标分类". 收录于：ECCV. 2014.

[Dev+19] J. Devlin, M.-W. Chang, K. Lee, 和 K. Toutanova. "BERT：深度双向Transformer语言理解的预训练". 收录于：NAACL. 2019.

[DG06] J. Davis 和 M. Goadrich. "精确率-召回率曲线与ROC曲线之间的关系". 收录于：ICML. 2006, pp. 233–240.

[DHM07] P. Diaconis, S. Holmes, 和 R. Montgomery. "抛硬币中的动态偏差". 收录于：SIAM Review 49.2 (2007), pp. 211–235.

[DHS01] R. O. Duda, P. E. Hart, 和 D. G. Stork. 模式分类. 第二版. Wiley Interscience, 2001.

[DHS11] J. Duchi, E. Hazan, 和 Y. Singer. "自适应次梯度方法用于在线学习和随机优化". 收录于：JMLR 12 (2011), pp. 2121–2159.

[Die98] T. G. Dietterich. "比较监督分类学习算法的近似统计检验". 收录于：Neural Computation. 10.7 (1998), pp. 1895–1923.

[Din+15] N. Ding, J. Deng, K. Murphy, 和 H. Neven. "基于Ising模型的概率标签关系图". 收录于：ICCV. 2015.

[DJ15] S. Dray 和 J. Josse. "含缺失值的主成分分析：方法的比较综述". 收录于：Plant Ecol. 216.5 (2015), pp. 657–667.

[DKK12] G Dror, N Koenigstein, 和 Y Koren. "网络规模的媒体推荐系统". 收录于：Proc. IEEE 100.9 (2012), pp. 2722–2736.

[DKS95] J. Dougherty, R. Kohavi, 和 M. Sahami. "连续特征的有监督和无监督离散化". 收录于：ICML. 1995.

[DLLP97] T. Dietterich, R. Lathrop, 和 T. Lozano-Perez. "用轴平行矩形解决多实例问题". 收录于：Artificial Intelligence 89 (1997), pp. 31–71.

[DLR77] A. P. Dempster, N. M. Laird, 和 D. B. Rubin. "通过EM算法从不完整数据中求最大似然". 收录于：J. of the Royal Statistical Society, Series B 34 (1977), pp. 1–38.

[DM01] D. van Dyk 和 X.-L. Meng. "数据增强的艺术". 收录于：J. Computational and Graphical Statistics 10.1 (2001), pp. 1–50.

[DM16] P. Drineas 和 M. W. Mahoney. "RandNLA：随机化数值线性代数". 收录于：CACM (2016).

[DMB21] Y. Dar, V. Muthukumar, 和 R. G. Baraniuk. "告别偏差-方差权衡？过参数化机器学习理论概述". 收录于：(Sept. 2021). arXiv:2109.02355 [stat.ML].

[Do+19] T.-T. Do, T. Tran, I. Reid, V. Kumar, T. Hoang, 和 G. Carneiro. "一个理论上可靠的三元组损失上界以提高深度距离度量学习的效率". 收录于：CVPR. 2019, pp. 10404–10413.

[Doe16] C. Doersch. "变分自编码器教程". 收录于：(2016). arXiv: 1606.05908 [stat.ML].

[Don95] D. L. Donoho. "通过软阈值去噪". 收录于：IEEE Trans. Inf. Theory 41.3 (1995), pp. 613–627.

[Dos+21] A. Dosovitskiy 等. "一张图像相当于16x16个词：用于大规模图像识别的Transformer". 收录于：ICLR. 2021.

[Doy+07] K. Doya, S. Ishii, A. Pouget, 和 R. P. N. Rao, 编. 贝叶斯大脑：神经编码的概率方法. MIT Press, 2007.

[DP97] P. Domingos 和 M. Pazzani. "零一损失下简单贝叶斯分类器的最优性". 收录于：Machine Learning 29 (1997), pp. 103–130.

[DR21] H. Duanmu 和 D. M. Roy. "关于扩展容许程序及其非标准贝叶斯风险". 收录于：Annals of Statistics (2021).

---

[Dri+04] P. Drineas, A. Frieze, R. Kannan, S. Vempala, and V. Vinay. "通过奇异值分解对大型图进行聚类". In: Machine Learning 56 (2004), pp. 9–33.

[DS12] M. Der and L. K. Saul. "潜在巧合分析：距离度量学习的隐变量模型". In: NIPS. Curran Associates, Inc., 2012, pp. 3230–3238.

[DSK16] V. Dumoulin, J. Shlens, and M. Kudlur. "一种学习得到的艺术风格表示". In: (2016). arXiv: 1610.07629 [cs.CV].

[Dum+18] A. Dumitrache, O. Inel, B. Timmermans, C. Ortiz, R.-J. Sips, L. Aroyo, and C. Welty. "众包真实标注的经验方法论". In: Semantic Web Journal (2018).

[Duv14] D. Duvenaud. "使用高斯过程自动构建模型". PhD thesis. Computational and Biological Learning Laboratory, University of Cambridge, 2014.

[DV16] V. Dumoulin and F. Visin. "深度学习卷积运算指南". In: (2016). arXiv: 1603.07285 [stat.ML].

[Dwi+23] R. Dwivedi, C. Singh, B. Yu, and M. J. Wainwright. "重访过参数化模型中的最小描述长度复杂性". In: J. Mach. Learn. Res. (2023).

[Dzi+23] N. Dziri et al. "信仰与命运：Transformer在组合性上的局限". In: (May 2023). arXiv: 2305.18654 [cs.CL].

[EDH19] K. Ethayarajh, D. Duvenaud, and G. Hirst. "理解线性词类比". In: Proc. ACL. Association for Computational Linguistics, 2019, pp. 3253–3262.

[EF15] D. Eigen and R. Fergus. "使用共同的多尺度卷积架构预测深度、表面法线和语义标签". In: ICCV. 2015.

[Efr+04] B. Efron, I. Johnstone, T. Hastie, and R. Tibshirani. "最小角回归". In: Annals of Statistics 32.2 (2004), pp. 407–499.

[Efr86] B. Efron. "为什么不是每个人都是贝叶斯主义者？" In: The American Statistician 40.1 (1986).

[Efr87] B. Efron. 刀切法、自助法及其他重抽样计划 (CBMS-NSF区域会议系列应用数学). en. Society for Industrial and Applied Mathematics, 1987.

[EH16] B. Efron and T. Hastie. 计算机时代的统计推断：算法、证据与数据科学. en. Cambridge University Press, June 2016.

[Ein16] A Einstein. "广义相对论的基础". In: Ann. Phys. 354.7 (1916), pp. 769–822.

[Eis19] J. Eisenstein. 自然语言处理导论. 2019.

[Elk03] C. Elkan. "利用三角不等式加速k均值聚类". In: ICML. 2003.

[EMH19] T. Elsken, J. H. Metzen, and F. Hutter. "神经架构搜索：综述". In: JMLR 20 (2019), pp. 1–21.

[Erh+10] D. Erhan, Y. Bengio, A. Courville, P.-A. Manzagol, P. Vincent, and S. Bengio. "为什么无监督预训练有助于深度学习？" In: JMLR 11 (2010), pp. 625–660.

[FAL17] C. Finn, P. Abbeel, and S. Levine. "模型无关的元学习：深度网络的快速适应". In: ICML. 2017.

[FB81] M. A. Fischler and R. Bolles. "随机采样一致性：模型拟合的范式及其在图像分析和自动制图中的应用". In: Comm. ACM 24.6 (1981), pp. 381–395.

[Fen+21] S. Y. Feng, V. Gangal, J. Wei, S. Chandar, S. Vosoughi, T. Mitamura, and E. Hovy. "NLP数据增强方法综述". In: (2021). arXiv: 2105.03075 [cs.CL].

[Fer+10] D. Ferrucci et al. "构建沃森：DeepQA项目概述". In: AI Magazine (2010), pp. 59–79.

[FH20] E. Fong and C. Holmes. "关于边际似然与交叉验证". In: Biometrika 107.2 (2020).

[FHK12] A. Feuerverger, Y. He, and S. Khatri. "Netflix挑战的统计显著性". In: Stat. Sci. 27.2 (2012), pp. 202–231.

[FHT00] J. Friedman, T. Hastie, and R. Tibshirani. "加性逻辑回归：提升的统计观点". In: Annals of statistics 28.2 (2000), pp. 337–374.

[FHT10] J. Friedman, T. Hastie, and R. Tibshirani. "通过坐标下降的广义线性模型的正则化路径". In: J. of Statistical Software 33.1 (2010).

[Fir57] J. Firth. "语言学理论概要 1930-1955". In: Studies in Linguistic Analysis. Ed. by F. Palmer. 1957.

[FJ02] M. A. T. Figueiredo and A. K. Jain. "有限混合模型的无监督学习". In: IEEE PAMI 24.3 (2002), pp. 381–396.

[FM03] J. H. Friedman and J. J. Meulman. "多变量加性回归树及其在流行病学中的应用". en. In: Stat. Med. 22.9 (2003), pp. 1365–1381.

[FMN16] C. Fefferman, S. Mitter, and H. Narayanan. "检验流形假设". In: J. Amer. Math. Soc. 29.4 (2016), pp. 983–1049.

[FNW07] M. Figueiredo, R. Nowak, and S. Wright. "稀疏重构的梯度投影方法：在压缩感知及其他逆问题中的应用". In: IEEE. J. on Selected Topics in Signal Processing (2007).

[For+21] P. Foret, A. Kleiner, H. Mobahi, and B. Neyshabur. "锐度感知最小化：有效提升泛化能力". In: ICLR. 2021.

[Fos19] D. Foster. 生成式深度学习：教机器绘画、写作、作曲与演奏. 1 edition. O'Reilly Media, 2019.

[FR07] C. Fraley and A. Raftery. "正态混合估计与基于模型聚类的贝叶斯正则化". In: J. of Classification 24 (2007), pp. 155–181.

---

[Fra+17] L. Franceschi, M. Donini, P. Frasconi, 和 M. Pontil. "基于前向和反向梯度的超参数优化". 收录于：ICML. 2017.

[Fre98] B. Frey. 《机器学习和数字通信的图模型》. MIT Press, 1998.

[Fri01] J. Friedman. “贪婪函数逼近：梯度提升机”. 收录于：《统计学年鉴》29 (2001), 第 1189–1232 页.

[Fri97a] J. Friedman. “关于偏差、方差、0-1损失和维度灾难”. 收录于：《数据挖掘与知识发现》1 (1997), 第 55–77 页.

[Fri97b] J. H. Friedman. "数据挖掘与统计学：有何关联". 收录于：第29届计算机科学与统计接口研讨会论文集. 1997.

[Fri99] J. Friedman. 《随机梯度提升》. 技术报告. 1999.

[FS96] Y. Freund 和 R. R. Schapire. "一种新的提升算法实验". 收录于：ICML. 1996.

[FT05] M. Fashing 和 C. Tomasi. "均值漂移是一种边界优化". en. 收录于：《IEEE模式分析与机器智能汇刊》27.3 (2005), 第 471–474 页.

[Fu98] W. Fu. “惩罚回归：桥回归与套索”. 收录于：《计算与图形统计》7 (1998), 第 397–416 页.

[Fuk75] K. Fukushima. “Cognitron：一种自组织多层神经网络”. 收录于：《生物控制论》20.6 (1975), 第 121–136 页.

[Fuk80] K Fukushima. “Neocognitron：一种不受位置偏移影响的模式识别机制的自组织神经网络模型”. en. 收录于：《生物控制论》36.4 (1980), 第 193–202 页.

[Fuk90] K. Fukunaga. 《统计模式识别导论》. 第二版. Academic Press, 1990.

[Gag94] P. Gage. "一种新的数据压缩算法". 收录于：《Dr Dobbs 期刊》(1994).

[Gan+16] Y Ganin, E Ustinova, H Ajakan, P Germain, 等. "神经网络的领域对抗训练". 收录于：JMLR (2016).

[Gär03] T. Gärtner. "结构化数据的核方法综述". 收录于：SIGKDD 探索通讯 5.1 (2003), 第 49–58 页.

[Gar+18] J. Gardner, G. Pleiss, K. Q. Weinberger, D. Bindel, 和 A. G. Wilson. "GPyTorch：基于 GPU 加速的黑箱矩阵-矩阵高斯过程推理". 收录于：NIPS. 编辑：S Bengio, H Wallach, H Larochelle, K Grauman, N Cesa-Bianchi, 和 R Garnett. Curran Associates, Inc., 2018, 第 7576–7586 页.

[GASG18] D. G. A. Smith 和 J. Gray. "opt-einsum - 一种优化 einsum 表达式收缩顺序的 Python 包". 收录于：JOSS 3.26 (2018), 第 753 页.

[GB05] Y. Grandvalet 和 Y. Bengio. "基于熵最小化的半监督学习". 收录于：Advances in neural information processing systems. 2005, 第 529–536 页.

[GB10] X. Glorot 和 Y. Bengio. "理解训练深度前馈神经网络的困难". 收录于：AISTATS. 2010, 第 249–256 页.

[GB18] V. Garcia 和 J. Bruna. "基于图神经网络的少样本学习". 收录于：国际学习表征会议 (ICLR). 2018.

[GBB11] X. Glorot, A. Bordes, 和 Y. Bengio. "深度稀疏整流器神经网络". 收录于：AISTATS. 2011.

[GBC16] I. Goodfellow, Y. Bengio, 和 A. Courville. 《深度学习》. http://www.deeplearningbook.org. MIT Press, 2016.

[GBD92] S. Geman, E. Bienenstock, 和 R. Dour-sat. "神经网络与偏差-方差困境". 收录于：《神经计算》4 (1992), 第 1–58 页.

[GC20] A. Gelman 和 B. Carpenter. "未知特异性和敏感性检验的贝叶斯分析". 收录于：J. of Royal Stat. Soc. Series C medrxiv;2020.05.22.20108944v2 (2020).

[GEB16] L. A. Gatys, A. S. Ecker, 和 M. Bethge. "基于卷积神经网络的图像风格迁移". 收录于：CVPR. 2016, 第 2414–2423 页.

[GEH19] T. Gale, E. Elsen, 和 S. Hooker. "深度神经网络中稀疏性的现状". 收录于：(2019). arXiv: 1902.09574 [cs.LG].

[Gel+04] A. Gelman, J. Carlin, H. Stern, 和 D. Rubin. 《贝叶斯数据分析》. 第二版. Chapman and Hall, 2004.

[Gel+14] A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, 和 D. B. Rubin. 《贝叶斯数据分析》第三版. 第三版. Chapman and Hall/CRC, 2014.

[Gel16] A. Gelman. "p值的问题不仅仅是p值本身". 收录于：《美国统计学家》(2016).

[Gér17] A. Géron. 《Scikit-Learn 与 TensorFlow 机器学习实战：构建智能系统的概念、工具与技术》. en. O'Reilly Media, Incorporated, 2017.

[Gér19] A. Géron. 《Scikit-Learn 与 TensorFlow 机器学习实战：构建智能系统的概念、工具与技术（第二版）》. en. O'Reilly Media, Incorporated, 2019.

[GEY19] Y. Geifman 和 R. El-Yaniv. "SelectiveNet：一种带有集成拒绝选项的深度神经网络". 收录于：ICML. 2019.

[GG16] Y. Gal 和 Z. Ghahramani. "作为贝叶斯近似的 Dropout：表示深度学习中的模型不确定性". 收录于：ICML. 2016.

[GH96] Z. Ghahramani 和 G. Hinton. 《因子分析混合模型的 EM 算法》. 技术报告. 多伦多大学计算机科学系, 1996.

[GHK17] Y. Gal, J. Hron, 和 A. Kendall. "具体 Dropout". 收录于：(2017). arXiv: 1705.07832 [stat.ML].

---

[GHV14] A. Gelman, J. Hwang, and A. Vehtari. "理解贝叶斯模型的预测信息准则". In: Statistics and Computing 24.6 (2014), pp. 997–1016.

[Gib97] M. Gibbs. "用于回归与分类的贝叶斯高斯过程". PhD thesis. U. Cambridge, 1997.

[Gil+17] J. Gilmer, S. S. Schoenholz, P. F. Riley, O. Vinyals, and G. E. Dahl. "面向量子化学的神经消息传递". In: ICML. 2017, pp. 1263–1272.

[Gil+21] J. Gilmer, B. Ghorbani, A. Garg, S. Kudugunta, B. Neyshabur, D. Cardoze, G. Dahl, Z. Nado, and O. Firat. "深度学习训练不稳定性的损失曲率视角". In: (2021). arXiv: 2110.04369 [cs.LG].

[GIM99] A. Gionis, P. Indyk, and R. Motwani. "基于哈希的高维相似性搜索". In: Proc. 25th Intl. Conf. on Very Large Data Bases. VLDB '99. 1999, pp. 518–529.

[GKS18] V. Gupta, T. Koren, and Y. Singer. "Shampoo：预条件随机张量优化". In: ICML. 2018.

[GL15] B. Gu and C. Ling. "一种用于模型选择的新广义误差路径算法". In: ICML. 2015.

[GL16] A. Grover and J. Leskovec. "node2vec：面向网络的可扩展特征学习". In: Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining. ACM. 2016, pp. 855–864.

[GMS05] M. Gori, G. Monfardini, and F. Scarselli. "一种在图域中学习的新模型". In: Proceedings. 2005 IEEE International Joint Conference on Neural Networks, 2005. Vol. 2. IEEE. 2005, pp. 729–734.

[GNK18] R. A. Güler, N. Neverova, and I. Kokkinos. "Densepose：野外密集人体姿态估计". In: CVPR. 2018, pp. 7297–7306.

[God18] P. Godec. 图嵌入：总结. https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007. 2018.

[GOF18] O. Gouvert, T. Oberlin, and C. Févotte. "用于推荐系统的负二项矩阵分解". In: (2018). arXiv: 1801.01708 [cs.LG].

[Gol+01] K. Goldberg, T. Roeder, D. Gupta, and C. Perkins. "Eigentaste：一种常数时间协同过滤算法". In: Information Retrieval 4.2 (2001), pp. 133–151.

[Gol+05] J. Goldberger, S. Roweis, G. Hinton, and R. Salakhutdinov. "邻域成分分析". In: NIPS. 2005.

[Gol+92] D. Goldberg, D. Nichols, B. M. Oki, and D. Terry. "利用协同过滤编织信息挂毯". In: Commun. ACM 35.12 (1992), pp. 61–70.

[Gon85] T. Gonzales. "最小化最大类间距离的聚类". In: Theor. Comp. Sci. 38 (1985), pp. 293–306.

[Goo01] N. Goodman. "用于快速最大熵训练的类别". In: ICASSP. 2001.

[Goo+14] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio. "生成对抗网络". In: NIPS. 2014.

[Gor06] P. F. Gorder. "神经网络为机器视觉带来新希望". In: Computing in science & engineering 8.6 (2006), pp. 4–8.

[Got+19] A. Gotmare, N. S. Keskar, C. Xiong, and R. Socher. "深度学习启发式方法的细致审视：学习率重启、预热与蒸馏". In: ICLR. 2019.

[GOV18] W Gao, S Oh, and P Viswanath. "揭示固定k近邻信息估计器的奥秘". In: IEEE Trans. Inf. Theory 64.8 (2018), pp. 5629–5661.

[GR07] T. Gneiting and A. E. Raftery. "严格适当的评分规则、预测与估计". In: JASA 102.477 (2007), pp. 359–378.

[GR18] A. Graves and M.-A. Ranzato. "无监督深度学习教程：第二部分". In: NIPS. 2018.

[GR19] P. Grünwald and T. Roos. "最小描述长度再探". In: Int. J. Math. Ind. 11.01 (Dec. 2019), p. 1930001.

[Gra04] Y. Grandvalet. "Bagging均衡影响". In: Mach. Learn. 55 (2004), pp. 251–270.

[Grall] A. Graves. "神经网络的实用变分推理". In: Advances in neural information processing systems. 2011, pp. 2348–2356.

[Gra13] A. Graves. "用循环神经网络生成序列". In: (2013). arXiv:1308.0850 [cs.NE].

[Gra+17] E. Grave, A. Joulin, M. Cissé, D. Grangier, and H. Jégou. "面向GPU的高效softmax近似". In: ICML. 2017.

[Gra+18] E. Grant, C. Finn, S. Levine, T. Darrell, and T. Griffiths. "将基于梯度的元学习重构为层次贝叶斯". In: ICLR. 2018.

[Gra+20] W. Grathwohl, K.-C. Wang, J.-H. Jacobsen, D. Duvenaud, M. Norouzi, and K. Swersky. "你的分类器其实是一个基于能量的模型，你应该像对待它一样对待它". In: ICLR. 2020.

[Gre+17] K. Greff, R. K. Srivastava, J. Koutnik, B. R. Steunebrink, and J. Schmidhuber. "LSTM：搜索空间奥德赛". In: IEEE Transactions on Neural Networks and Learning Systems 28.10 (2017).

[Gri20] T. L. Griffiths. "通过人类局限理解人类智能". en. In: Trends Cogn. Sci. 24.11 (2020), pp. 873–883.

[Gru07] P. Grunwald. 最小描述长度原理. MIT Press, 2007.

[GS08] Y Guo and D Schuurmans. "指数族PCA和低秩矩阵分解的高效全局优化". In: 2008 46th Annual Allerton Conference on Communication, Control, and Computing. 2008, pp. 1100–1107.

---

[GS97] C. M. Grinstead 和 J. L. Snell.《概率论导论》（第二版）. 美国数学会, 1997.

[GSK18] S. Gidaris、P. Singh 和 N. Komodakis."通过预测图像旋转进行无监督表征学习". 载于：ICLR. 2018.

[GT07] L. Getoor 和 B. Taskar 编.《关系统计学习导论》. MIT 出版社, 2007.

[GTA00] G. Gigerenzer、P. M. Todd 和 ABC 研究组.《让我们变得聪明的简单启发式方法》. 英文. 插图版. 牛津大学出版社, 2000.

[Gu+18] A. Gu、F. Sala、B. Gunel 和 C. Ré."在乘积空间中学习混合曲率表征". 载于：国际学习表征会议 (2018).

[Gua+10] Y. Guan、J. Dy、D. Niu 和 Z. Ghahramani."非参数多重聚类的变分推断". 载于：第一届发现、总结与利用多重聚类国际研讨会 (MultiClust). 2010.

[Gua+17] S. Guadarrama、K. Dahl、D. Bieber、M. Norouzi、J. Shlens 和 K. Murphy."PixColor：像素递归着色". 载于：BMVC. 2017.

[Gul+20] A. Gulati 等."Conformer：用于语音识别的卷积增强 Transformer". 载于：(2020). arXiv: 2005.08100 [eess.AS].

[Guo09] Y. Guo."通过凸优化的监督指数族主成分分析". 载于：NIPS. 2009.

[Guo+17] H. Guo、R. Tang、Y. Ye、Z. Li 和 X. He."DeepFM：基于因子分解机的 CTR 预测神经网络". 载于：IJCAI. IJCAI'17. AAAI 出版社, 2017, 第 1725–1731 页.

[Gus01] M. Gustafsson."偏最小二乘算法的概率推导". 载于：化学信息与建模杂志 41 (2001), 第 288–294 页.

[GVZ16] A. Gupta、A. Vedaldi 和 A. Zisserman."自然图像中文本定位的合成数据". 载于：CVPR. 2016.

[GZE19] A. Grover、A. Zweig 和 S. Ermon."Graphite：图的迭代生成建模". 载于：国际机器学习大会. 2019, 第 2434–2444 页.

[HA85] L. Hubert 和 P. Arabie."比较划分". 载于：分类学杂志 2 (1985), 第 193–218 页.

[HAB19] M. Hein、M. Andriushchenko 和 J. Bitterwolf."为什么 ReLU 网络在远离训练数据处产生高置信度预测以及如何缓解该问题". 载于：CVPR. 2019.

[Hac75] I. Hacking.《概率的涌现：关于概率、归纳与统计推断早期思想的哲学研究》. 剑桥大学出版社, 1975.

[Háj08] A. Hájek."荷兰赌论证". 载于：《理性与社会选择牛津手册》. P. Anand、P. Pattanaik 和 C. Puppe 编. 牛津大学出版社, 2008.

[Han+20] B. Han、Q. Yao、T. Liu、G. Niu、I. W. Tsang、J. T. Kwok 和 M. Sugiyama."标签噪声表征学习综述：过去、现在与未来". 载于：(2020). arXiv: 2011.04406 [cs.LG].

[Har54] Z. Harris."分布结构". 载于：词汇 10.23 (1954), 第 146–162 页.

[Has+04] T. Hastie、S. Rosset、R. Tibshirani 和 J. Zhu."支持向量机的完整正则化路径". 载于：JMLR 5 (2004), 第 1391–1415 页.

[Has+09] T. Hastie、S. Rosset、J. Zhu 和 H. Zou."多类 AdaBoost". 载于：统计学及其接口 2.3 (2009), 第 349–360 页.

[Has+17] D. Hassabis、D. Kumaran、C. Summerfield 和 M. Botvinick."神经科学启发的人工智能". 英文. 载于：神经元 95.2 (2017), 第 245–258 页.

[Has87] J. Hastad.《小深度电路的计算限制》. MIT 出版社, 1987.

[HB17] X. Huang 和 S. Belongie."利用自适应实例归一化的实时任意风格迁移". 载于：ICCV. 2017.

[HBK23] P. Haluptzok、M. Bowers 和 A. T. Kalai."语言模型可以自学编程". 载于：ICLR. 2023 年 2 月.

[HCD12] D. Hoiem、Y. Chodpathumwan 和 Q. Dai."目标检测器的误差诊断". 载于：ECCV. 2012.

[HCL03] C.-W. Hsu、C.-C. Chang 和 C.-J. Lin.《支持向量分类实用指南》. 技术报告. 国立台湾大学资讯工程系, 2003.

[HDR19] S. Hayou、A. Doucet 和 J. Rousseau."激活函数对深度神经网络训练的影响". 载于：(2019). arXiv:1902.06853 [stat.ML].

[He+15] K. He、X. Zhang、S. Ren 和 J. Sun."深入探究整流器：在 ImageNet 分类上超越人类水平". 载于：ICCV. 2015.

[He+16a] K. He、X. Zhang、S. Ren 和 J. Sun."深度残差学习用于图像识别". 载于：CVPR. 2016.

[He+16b] K. He、X. Zhang、S. Ren 和 J. Sun."深度残差网络中的恒等映射". 载于：ECCV. 2016.

[He+17] X. He、L. Liao、H. Zhang、L. Nie、X. Hu 和 T.-S. Chua."神经协同过滤". 载于：WWW. 2017.

[HE18] D. Ha 和 D. Eck."草图绘制的神经表征". 载于：ICLR. 2018.

[He+20] K. He、H. Fan、Y. Wu、S. Xie 和 R. Girshick."用于无监督视觉表征学习的动量对比". 载于：CVPR. 2020, 第 9729–9738 页.

[Hen+15] J. Hensman、A. Matthews、M. Filippone 和 Z. Ghahramani."变分稀疏高斯过程的 MCMC". 载于：NIPS. 2015, 第 1648–1656 页.

---

[HG16] D. Hendrycks 和 K. Gimpel。“高斯误差线性单元（GELUs）”。载于：arXiv [cs.LG] (2016年)。

[HG20] J. Howard 和 S. Gugger。《面向程序员的深度学习：使用 Fastai 和 PyTorch 的 AI 应用（无需博士学位）》。英文。第1版。O'Reilly Media，2020年。

[HG21] M. K. Ho 和 T. L. Griffiths。“认知科学作为人类决策正向与逆向模型的来源：面向机器人与控制”。载于：《控制、机器人与自主系统年度综述》。2021年。

[HGD19] K. He、R. Girshick 和 P. Dollár。“重新思考 ImageNet 预训练”。载于：CVPR。2019年。

[Hin+12] G. E. Hinton 等。“深度神经网络在语音识别中的声学建模：四个研究组的共同观点”。载于：《IEEE 信号处理杂志》29.6 (2012年)，第82–97页。

[Hin13] G. Hinton。CSC 2535 第11讲：非线性降维。2013年。

[Hin14] G. Hinton。第6e讲：神经网络（RMSprop：用梯度最近幅度的滑动平均值除以梯度）。2014年。

[HK15] F. M. Harper 和 J. A. Konstan。“MovieLens 数据集：历史与背景”。载于：《ACM 交互式智能系统汇刊》5.4 (2015年)，第1–19页。

[HK92] A Hertz 和 J Krogh。“含噪情况下线性感知机的泛化”。载于：《物理学杂志 A》(1992年)。

[HKV19] F. Hutter、L. Kotthoff 和 J. Vanschoren 编。《自动化机器学习——方法、系统与挑战》。Springer，2019年。

[HL04] D. R. Hunter 和 K. Lange。“MM 算法教程”。载于：《美国统计学家》58 (2004年)，第30–37页。

[HMT11] N. Halko、P.-G. Martinsson 和 J. A. Tropp。“用随机性发现结构：构造近似矩阵分解的概率算法”。载于：《SIAM 评论》，综述与评述部分 53.2 (2011年)，第217–288页。

[HN19] C. M. Holmes 和 I. Nemenman。“实值数据的互信息估计：带有误差条和可控偏差”。英文。载于：《物理评论 E》100.2-1 (2019年)，第022404页。

[Hoc+01] S. Hochreiter、Y. Bengio、P. Frasconi 和 J. Schmidhuber。“循环网络中的梯度流：学习长期依赖的困难”。载于：《动力循环神经网络实用指南》。S. C. Kremer 和 J. F. Kolen 编。2001年。

[Hoe+14] R. Hoekstra、R. D. Morey、J. N. Rouder 和 E.-J. Wagenmakers。“置信区间的稳健误解”。英文。载于：《心理计量学通报与评论》21.5 (2014年)，第1157–1164页。

[Hoe+21] T. Hoefler、D. Alistarh、T. Ben-Nun、N. Dryden 和 A. Peste。“深度学习中的稀疏性：面向神经网络高效推理与训练的剪枝与增长”。载于：(2021年)。arXiv:2102.00554 [cs.LG]。

[Hof09] P. D. Hoff。《贝叶斯统计方法初级教程》。Springer，2009年。

[Hor61] P Horst。“广义典型相关及其在实验数据中的应用”。英文。载于：《临床心理学杂志》17 (1961年)，第331–347页。

[Hor91] K. Hornik。“多层前馈网络的逼近能力”。载于：《神经网络》4.2 (1991年)，第251–257页。

[Hos+19] M. Z. Hossain、F. Sohel、M. F. Shiratuddin 和 H. Laga。“深度学习在图像描述中的全面综述”。载于：《ACM 计算调查》(2019年)。

[HOT06] G. Hinton、S. Osindero 和 Y. Teh。“深度信念网的快速学习算法”。载于：《神经计算》18 (2006年)，第1527–1554页。

[Hot36] H. Hotelling。“两组变量之间的关系”。载于：《生物计量学》28.3/4 (1936年)，第321–377页。

[Hou+12] N. Houlsby、F. Huszar、Z. Ghahramani 和 J. M. Hernández-lobato。“协同高斯过程用于偏好学习”。载于：NIPS。2012年，第2096–2104页。

[Hou+19] N. Houlsby、A. Giurgiu、S. Jastrzebski、B. Morrone、Q. de Laroussilhe、A. Gesmundo、M. Attariyan 和 S. Gelly。“面向 NLP 的参数高效迁移学习”。载于：ICML。2019年。

[How+17] A. G. Howard、M. Zhu、B. Chen、D. Kalenichenko、W. Wang、T. Weyand、M. Andreetto 和 H. Adam。“MobileNets：面向移动视觉应用的高效卷积神经网络”。载于：CVPR。2017年。

[HR03] G. E. Hinton 和 S. T. Roweis。“随机邻居嵌入”。载于：NIPS。2003年，第857–864页。

[HR76] L. Hyafil 和 R. Rivest。“构造最优二叉决策树是 NP 完全的”。载于：《信息处理快报》5.1 (1976年)，第15–17页。

[HRP21] M. Huisman、J. N. van Rijn 和 A. Plaat。“深度元学习综述”。载于：《人工智能评论》(2021年)。

[HS19] J. Haochen 和 S. Sra。“有限轮次后随机打乱优于 SGD”。载于：ICML。第97卷。机器学习研究会议录。PMLR，2019年，第2624–2633页。

[HS97a] S Hochreiter 和 J Schmidhuber。“平坦极小值”。英文。载于：《神经计算》9.1 (1997年)，第1–42页。

[HS97b] S. Hochreiter 和 J. Schmidhuber。“长短期记忆”。载于：《神经计算》9.8 (1997年)，第1735–1780页。

[HSW89] K. Hornik、M. Stinchcombe 和 H. White。“多层前馈网络是通用逼近器”。载于：《神经网络》2.5 (1989年)，第359–366页。

[HT90] T. Hastie 和 R. Tibshirani。《广义可加模型》。Chapman and Hall，1990年。

[HTF01] T. Hastie、R. Tibshirani 和 J. Friedman。《统计学习基础》。Springer，2001年。

---

[HTF09] T. Hastie, R. Tibshirani, and J. Friedman.《统计学习基础》. 第2版. Springer, 2009.

[HTW15] T. Hastie, R. Tibshirani, and M. Wainwright.《稀疏统计学习：Lasso及其推广》. CRC Press, 2015.

[Hual4] G.-B. Huang. “极端学习机洞察：随机神经元、随机特征与核”. In: Cognit. Comput. 6.3 (2014), pp. 376–390.

[Hua+17a] G. Huang, Z. Liu, K. Q. Weinberger, and L. van der Maaten. “密集连接卷积网络”. In: CVPR. 2017.

[Hua+17b] J. Huang et al. “现代卷积目标检测器的速度与精度权衡”. In: CVPR. 2017.

[Hua+18] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon, C. Hawthorne, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck. “音乐Transformer”. In: (2018). arXiv:1809.04281 [cs.LG].

[Hub+08] M. F. Huber, T Bailey, H Durrant-Whyte, and U. D. Hanebeck. “关于高斯混合随机向量的熵近似”. In: 2008 IEEE International Conference on Multisensor Fusion and Integration for Intelligent Systems. 2008, pp. 181–188.

[Hub64] P. Huber. “位置参数的稳健估计”. In: Annals of Statistics 53 (1964), 73–101.

[Hut90] M. F. Hutchinson. “拉普拉斯平滑样条影响矩阵迹的随机估计量”. In: Communications in Statistics - Simulation and Computation 19.2 (1990), pp. 433–450.

[HVD14] G. Hinton, O. Vinyals, and J. Dean. “蒸馏神经网络中的知识”. In: NIPS Deep Learning Workshop. 2014.

[HW62] D. Hubel and T. Wiesel. “猫视觉皮层中的感受野、双眼交互和功能架构”. In: J. Physiology 160 (1962), pp. 106–154.

[HY01a] D. J. Hand and K. Yu. “傻瓜贝叶斯：并非如此愚蠢？” In: Int. Stat. Rev. 69.3 (2001), pp. 385–398.

[HY01b] M. Hansen and B. Yu. “模型选择与最小描述长度原则”. In: JASA (2001).

[HYL17] W. Hamilton, Z. Ying, and J. Leskovec. “大图上的归纳式表示学习”. In: Advances in Neural Information Processing Systems. 2017, pp. 1024–1034.

[Idr+17] H. Idrees, A. R. Zamir, Y.-G. Jiang, A. Gorban, I. Laptev, R. Sukthankar, and M. Shah. “THUMOS挑战赛：自然场景视频动作识别”. In: Comput. Vis. Image Underst. 155 (2017), pp. 1–23.

[Ie+19] E. Ie, V. Jain, J. Wang, S. Narvekar, R. Agarwal, R. Wu, H.-T. Cheng, T. Chandra, and C. Boutilier. “SlateQ：推荐集合强化学习的可处理分解”. In: IJCAI. International Joint Conferences on Artificial Intelligence Organization, 2019.

[Iof17] S. Ioffe. “批重归一化：减少批归一化模型中对小批次的依赖”. In: (2017). arXiv: 1702.03275 [cs.LG].

[Ips09] I. Ipsen.《数值矩阵分析：线性系统与最小二乘》. SIAM, 2009.

[IR10] A. Ilin and T. Raiko. “缺失值存在下主成分分析的实用方法”. In: JMLR 11 (2010), pp. 1957–2000.

[IS15] S. Ioffe and C. Szegedy. “批归一化：通过减少内部协变量偏移加速深度网络训练”. In: ICML 2015, pp. 448–456.

[Isc+19] A. Iscen, G. Tolias, Y. Avrithis, and O. Chum. “深度半监督学习的标签传播”. In: CVPR. 2019.

[Izm+18] P. Izmailov, D. Podoprikhin, T. Garipov, D. Vetrov, and A. G. Wilson. “权重平均导致更宽的优化和更好的泛化”. In: UAI. 2018.

[Izm+20] P. Izmailov, P. Kirichenko, M. Finzi, and A. G. Wilson. “利用归一化流的半监督学习”. In: ICML. 2020, pp. 4615–4630.

[Jac+91] R. Jacobs, M. Jordan, S. Nowlan, and G. Hinton. “局部专家自适应混合”. In: Neural Computation (1991).

[JAFF16] J. Johnson, A. Alahi, and L. Fei-Fei. “实时风格迁移与超分辨率的感知损失”. In: ECCV. 2016.

[Jan18] E. Jang. 归一化流教程. https://blog.evjang.com/2018/01/nfl.html. 2018.

[Jay03] E. T. Jaynes.《概率论：科学的逻辑》. Cambridge university press, 2003.

[Jay76] E. T. Jaynes. “置信区间与贝叶斯区间”. In: Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science, vol II. Ed. by W. L. Harper and C. A. Hooker. Reidel Publishing Co., 1976.

[JD88] A. Jain and R. Dubes.《数据聚类算法》. Prentice Hall, 1988.

[JDJ17] J. Johnson, M. Douze, and H. Jégou. “基于GPU的十亿级相似性搜索”. In: (2017). arXiv: 1702.08734 [cs.CV].

[Jef61] H. Jeffreys.《概率论》. Oxford, 1961.

[Jef73] H. Jeffreys.《科学推理》. Third edition. Cambridge, 1973.

[JGH18] A. Jacot, F. Gabriel, and C. Hongler. “神经正切核：神经网络中的收敛与泛化”. In: NIPS. 2018.

[JH04] H. Jaeger and H. Haas. “驾驭非线性：预测混沌系统与无线通信节能”. In: Science 304.5667 (2004).

[JHG00] N. Japkowicz, S. Hanson, and M. Gluck. “非线性自关联不等于PCA”. In: Neural Computation 12 (2000), pp. 531–545.

---

[Jia+20] Y. Jiang, B. Neyshabur, H. Mobahi, D. Krishnan, 和 S. Bengio. “惊人的泛化度量及其寻找方法”. 载于: ICLR. 2020.

[Jin+17] Y. Jing, Y. Yang, Z. Feng, J. Ye, Y. Yu, 和 M. Song. “神经风格迁移：综述”. 载于: arXiv [cs.CV] (2017).

[JJ94] M. I. Jordan 和 R. A. Jacobs. “专家层次混合与EM算法”. 载于: Neural Computation 6 (1994), 页 181–214.

[JK13] A. Jern 和 C. Kemp. “样例与类别生成的概率解释”. en. 载于: Cogn. Psychol. 66.1 (2013), 页 85–125.

[JM08] D. Jurafsky 和 J. H. Martin. 语音与语言处理：自然语言处理、计算语言学和语音识别导论. 第2版. Prentice-Hall, 2008.

[JM20] D. Jurafsky 和 J. H. Martin. 语音与语言处理：自然语言处理、计算语言学和语音识别导论 (第三版). 第3版草案. 2020.

[Jor19] M. Jordan. “人工智能——革命尚未发生”. 载于: Harvard Data Science Review 1.1 (2019).

[JT19] L. Jing 和 Y. Tian. “基于深度神经网络的自监督视觉特征学习：综述”. 载于: (2019). arXiv: 1902.06162 [cs.CV].

[Jun+19] W. Jung, D. Jung, B. Kim, S. Lee, W. Rhee, 和 J. Anh. “重构批归一化以加速CNN训练”. 载于: SysML 2019.

[JW19] S. Jain 和 B. C. Wallace. “注意力不是解释”. 载于: NAACL. 2019.

[JZ13] R. Johnson 和 T. Zhang. “利用预测方差缩减加速随机梯度下降”. 载于: NIPS. Curran Associates, Inc., 2013, 页 315–323.

[JZS15] R. Jozefowicz, W. Zaremba, 和 I. Sutskever. “循环网络架构的实证探索”. 载于: ICML. 2015, 页 2342–2350.

[KAG19] A. Kirsch, J. van Amersfoort, 和 Y. Gal. “BatchBALD：深度贝叶斯主动学习的高效且多样的批次获取”. 载于: NIPS. 2019.

[Kai58] H. Kaiser. “因子分析中正交旋转的最大方差准则”. 载于: Psychometrika 23.3 (1958).

[Kan+12] E. Kandel, J. Schwartz, T. Jessell, S. Siegelbaum, 和 A. Hudspeth, 编. 神经科学原理. 第五版. 2012.

[Kan+20] B. Kang, S. Xie, M. Rohrbach, Z. Yan, A. Gordo, J. Feng, 和 Y. Kalantidis. “长尾识别中表示与分类器的解耦”. 载于: ICLR. 2020.

[Kap16] J. Kaplan. 人工智能：每个人都需要知道的事. en. 第1版. Oxford University Press, 2016.

[Kat+20] A. Katharopoulos, A. Vyas, N. Pappas, 和 F. Fleuret. “Transformer即RNN：具有线性注意力的快速自回归Transformer”. 载于: ICML. 2020.

[KB15] D. Kingma 和 J. Ba. “Adam：一种随机优化方法”. 载于: ICLR. 2015.

[KB19] M. Kaya 和 H. S. Bilge. “深度度量学习：综述”. en. 载于: Symmetry 11.9 (2019), 页 1066.

[KBV09] Y. Koren, R. Bell, 和 C. Volinsky. “基于矩阵分解的推荐系统技术”. 载于: IEEE Computer 42.8 (2009), 页 30–37.

[KD09] A. D. Kiureghian 和 O. Ditlevsen. “偶然不确定性还是认知不确定性？有关系吗？”. 载于: Structural Safety 31.2 (2009), 页 105–112.

[Kem+06] C. Kemp, J. Tenenbaum, T. Y. T. Griffiths 和, 和 N. Ueda. “使用无限关系模型学习概念系统”. 载于: AAAI. 2006.

[KF05] H. Kuck 和 N. de Freitas. “从群体统计中学习个体信息”. 载于: UAI. 2005.

[KG05] A. Krause 和 C. Guestrin. “图模型中信息的近最优价值”. 载于: UAI. 2005.

[KG17] A. Kendall 和 Y. Gal. “计算机视觉的贝叶斯深度学习需要哪些不确定性？”. 载于: NIPS. Curran Associates, Inc., 2017, 页 5574–5584.

[KGS20] J. von Kügelgen, L. Gresele, 和 B. Schölkopf. “Covid-19病死率中的辛普森悖论：年龄相关因果效应的中介分析”. 载于: (2020). arXiv: 2005.07180 [stat.AP].

[KH09] A Krizhevsky 和 G Hinton. 从小图像中学习多层特征. 技术报告. U. Toronto, 2009.

[KH19] D. Krotov 和 J. J. Hopfield. “通过竞争隐藏单元的无监督学习”. en. 载于: PNAS 116.16 (2019), 页 7723–7731.

[Kha+10] M. E. Khan, B. Marlin, G. Bouchard, 和 K. P. Murphy. “混合数据因子分析的变分界”. 载于: NIPS. 2010.

[Kha+20] A. Khan, A. Sohail, U. Zahoora, 和 A. S. Qureshi. “深度卷积神经网络的最新架构综述”. 载于: AI Review (2020).

[KHB07] A. Kapoor, E. Horvitz, 和 S. Basu. “选择性监督：用决策论主动学习指导监督学习”. 载于: IJCAI. 2007.

[KHW19] W. Kool, H. van Hoof, 和 M. Welling. “随机束及其寻找方法：用于无放回序列采样的Gumbel-Top-k技巧”. 载于: ICML. 2019.

[Kim14] Y. Kim. “用于句子分类的卷积神经网络”. 载于: EMNLP. 2014.

[Kim19] D. H. Kim. 深度度量学习综述. 2019.

[Kin+14] D. P. Kingma, D. J. Rezende, S. Mohamed, 和 M. Welling. “半监督学习”. 载于: NIPS. 2014.

---

[Kir+19] A. Kirillov, K. He, R. Girshick, C. Rother, 和 P. Dollár. "全景分割". 收录于：CVPR. 2019.

[KJ16] L Kang 和 V Joseph. "核近似：从回归到插值". 收录于：SIAM/ASA J. Uncertainty Quantification 4.1 (2016), 第112–129页.

[KJ95] J. Karhunen 和 J. Joutsensalo. "主成分分析、优化问题和神经网络的推广". 收录于：Neural Networks 8.4 (1995), 第549–562页.

[KJM19] N. M. Kriege, F. D. Johansson, 和 C. Morris. "图核综述". 收录于：(2019). arXiv: 1903.11835 [cs.LG].

[KK06] S. Kotsiantis 和 D. Kanellopoulos. "离散化技术：近期综述". 收录于：GESTS Intl. Trans. on Computer Science and Engineering 31.1 (2006), 第47–58页.

[KKH20] I. Khemakhem, D. P. Kingma, 和 A. Hyvari-nen. "变分自编码器与非线性ICA：统一框架". 收录于：AISTATS. 2020.

[KKL20] N. Kitaev, L. Kaiser, 和 A. Levskaya. "Reformer：高效的Transformer". 收录于：8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020. OpenReview.net, 2020.

[KKS20] F. Kunstner, R. Kumar, 和 M. Schmidt. "EM算法的同胚不变性：基于镜像下降的指数族KL散度非渐近收敛". 收录于：(2020). arXiv: 2011.01170 [cs.LG].

[KL17] J. K. Kruschke 和 T. M. Liddell. "贝叶斯新统计：从贝叶斯视角进行假设检验、估计、元分析和功效分析". 收录于：Psychon. Bull. Rev. (2017).

[KL21] W. M. Kouw 和 M. Loog. "无目标标签的领域自适应综述". 英文. 收录于：IEEE PAMI (2021).

[Kla+17] G. Klambauer, T. Unterthiner, A. Mayr, 和 S. Hochreiter. "自归一化神经网络". 收录于：NIPS. 2017.

[Kle02] J. Kleinberg. "聚类的不可能定理". 收录于：NIPS. 2002.

[Kle+11] A. Kleiner, A. Talwalkar, P. Sarkar, 和 M. I. Jordan. 大规模数据的可扩展自助法. 技术报告. UC Berkeley, 2011.

[Kle13] P. N. Klein. 编码矩阵：通过计算机科学应用学习线性代数. 英文. 第1版. Newtonian Press, 2013.

[KLQ95] C. Ko, J. Lee, 和 M. Queyranne. "最大熵抽样的精确算法". 收录于：Operations Research 43 (1995), 第684–691页.

[Kok17] I. Kokkinos. "UberNet：使用多样化数据集和有限内存训练用于低层、中层和高层视觉的通用卷积神经网络". 收录于：CVPR. 第2卷. 2017, 第8页.

[Kol+19] A. Kolesnikov, L. Beyer, X. Zhai, J. Puigcerver, J. Yung, S. Gelly, 和 N. Houlsby. "用于迁移的通用视觉表示的大规模学习". 收录于：(2019). arXiv:1912.11370 [cs.CV].

[Kol+20] A. Kolesnikov, L. Beyer, X. Zhai, J. Puigcerver, J. Yung, S. Gelly, 和 N. Houlsby. "用于迁移的通用视觉表示的大规模学习". 收录于：ECCV. 2020.

[Kon20] M. Konnikova. 最大的虚张声势：我如何学会专注、掌控自我并获胜. 英文. Penguin Press, 2020.

[Kor09] Y. Koren. Netflix大奖赛的BellKor解决方案. 技术报告. Yahoo! Research, 2009.

[KR19] M. Kearns 和 A. Roth. 道德算法：社会感知算法设计科学. 英文. Oxford University Press, 2019.

[KR87] L. Kaufman 和 P. Rousseeuw. "基于中位数的聚类". 收录于：基于L1范数及相关方法的统计数据分析. 编辑：Y. Dodge. North-Holland, 1987, 第405–416页.

[KR90] L. Kaufman 和 P. Rousseeuw. 在数据中发现组：聚类分析导论. Wiley, 1990.

[Kri+05] B. Krishnapuram, L. Carin, M. Figueiredo, 和 A. Hartemink. "学习稀疏贝叶斯分类器：多类公式、快速算法和泛化界". 收录于：IEEE Transaction on Pattern Analysis and Machine Intelligence (2005).

[Kru13] J. K. Kruschke. "贝叶斯估计取代t检验". 收录于：J. Experimental Psychology: General 142.2 (2013), 第573–603页.

[Kru15] J. Kruschke. 执行贝叶斯数据分析：使用R、JAGS和STAN的教程. 第二版. Academic Press, 2015.

[KS15] H. Kaya 和 A. A. Salah. "因子分析器的自适应混合模型". 收录于：(2015). arXiv: 1507.02801 [stat.ML].

[KSG04] A. Kraskov, H. Stögbauer, 和 P. Grassberger. "估计互信息". 英文. 收录于：Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 69.6 Pt 2 (2004), 第066138页.

[KSH12] A. Krizhevsky, I. Sutskever, 和 G. Hinton. "使用深度卷积神经网络的ImageNet分类". 收录于：NIPS. 2012.

[KSJ09] I. Konstas, V. Stathopoulos, 和 J. M. Jose. "社交网络与协同推荐". 收录于：Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval. 2009, 第195–202页.

[KST82] D. Kahneman, P. Slovic, 和 A. Tversky, 编. 不确定性下的判断：启发式与偏差. Cambridge, 1982.

[KTB11] D. P. Kroese, T. Taimre, 和 Z. I. Botev. 蒙特卡洛方法手册. 英文. 第1版. Wiley, 2011.

[Kua+09] P. Kuan, G. Pan, J. A. Thomson, R. Stewart, 和 S. Keles. 用于检测富集的层次半马尔可夫模型，

---

[Kull13] B. Kulis. "度量学习综述". 载于: 《机器学习基础与趋势》 5.4 (2013), 第287–364页.

[KV94] M. J. Kearns 和 U. V. Vazirani. 《计算学习理论导论》. MIT Press, 1994.

[KVK10] A. Klami, S. Virtanen 和 S. Kaski. "耦合数据源的贝叶斯指数族投影". 载于: UAI. 2010.

[KW14] D. P. Kingma 和 M. Welling. "自编码变分贝叶斯". 载于: ICLR. 2014.

[KW16a] T. N. Kipf 和 M. Welling. "基于图卷积网络的半监督分类". 载于: arXiv预印本 arXiv:1609.02907 (2016).

[KW16b] T. N. Kipf 和 M. Welling. "变分图自编码器". 载于: arXiv预印本 arXiv:1611.07308 (2016).

[KW19a] D. P. Kingma 和 M. Welling. "变分自编码器导论". 载于: 《机器学习基础与趋势》 12.4 (2019), 第307–392页.

[KW19b] M. J. Kochenderfer 和 T. A. Wheeler. 《优化算法》. 英文. The MIT Press, 2019.

[KWW22] M. J. Kochenderfer, T. A. Wheeler 和 K. Wray. 《决策算法》. The MIT Press, 2022.

[Kyu+10] M. Kyung, J. Gill, M. Ghosh 和 G. Casella. "惩罚回归、标准误差与贝叶斯Lasso". 载于: 《贝叶斯分析》 5.2 (2010), 第369–412页.

[LA16] S. Laine 和 T. Aila. "半监督学习的时间集成". 载于: arXiv预印本 arXiv:1610.02242 (2016).

[Lak+17] B. M. Lake, T. D. Ullman, J. B. Tenenbaum 和 S. J. Gershman. "构建像人一样学习和思考的机器". 英文. 载于: 《行为与脑科学》 (2017), 第1–101页.

[Lam18] B. Lambert. 《贝叶斯统计学学生指南》. 英文. 第一版. SAGE Publications Ltd, 2018.

[Law12] N. D. Lawrence. "谱降维的统一概率视角：见解与新模型". 载于: JMLR 13.May (2012), 第1609–1638页.

[LBM06] J. A. Lasserre, C. M. Bishop 和 T. P. Minka. "生成模型与判别模型的原理性混合". 载于: CVPR. 第1卷. 2006年6月, 第87–94页.

[LBS19] Y. Li, J. Bradshaw 和 Y. Sharma. "生成分类器是否对对抗攻击更鲁棒？" 载于: ICML. 编辑: K. Chaudhuri 和 R. Salakhutdinov. 第97卷. Proceedings of Machine Learning Research. PMLR, 2019, 第3804–3814页.

[LeC18] Y. LeCun. 自监督学习：机器能像人类一样学习吗？ 2018.

[LeC+98] Y. LeCun, L. Bottou, Y. Bengio 和 P. Haffner. "基于梯度的学习应用于文档识别". 载于: 《IEEE会议录》 86.11 (1998), 第2278–2324页.

[Lee13] D.-H. Lee. "伪标签：面向深度神经网络的简单高效半监督学习方法". 载于: ICML表示学习挑战研讨会. 2013.

[Lee+13] J. Lee, S. Kim, G. Lebanon 和 Y. Singer. "局部低秩矩阵近似". 载于: ICML. 第28卷. Proceedings of Machine Learning Research. PMLR, 2013, 第82–90页.

[Lee+19] J. Lee, Y. Lee, J. Kim, A. R. Kosiorek, S. Choi 和 Y. W. Teh. "Set Transformer：基于注意力的置换不变神经网络框架". 载于: ICML. 2019.

[Lee77] J. de Leeuw. "凸分析在多维缩放中的应用". 载于: 《统计学近期进展》. 编辑: J. R. Barra, F Brodeau, G Romier 和 B Van Cutsem. 1977.

[Lep+21] D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer 和 Z. Chen. "GShard：利用条件计算和自动分片扩展巨型模型". 载于: ICLR. 2021.

[LG14] O. Levy 和 Y. Goldberg. "神经词嵌入作为隐式矩阵分解". 载于: NIPS. 2014.

[LH17] I. Loshchilov 和 F. Hutter. "SGDR：带热启动的随机梯度下降". 载于: ICLR. 2017.

[Li+15] Y. Li, D. Tarlow, M. Brockschmidt 和 R. Zemel. "门控图序列神经网络". 载于: arXiv预印本 arXiv:1511.05493 (2015).

[Li+17] A. Li, A. Jabri, A. Joulin 和 L. van der Maaten. "从网络数据学习视觉N-gram". 载于: ICCV. 2017.

[Lia20] S. M. Liao, 编. 《人工智能伦理学》. 英文. 第一版. Oxford University Press, 2020.

[Lim+19] S. Lim, I. Kim, T. Kim, C. Kim 和 S. Kim. "快速自动增强". 载于: (2019). arXiv: 1905.00397 [cs.LG].

[Lin06] D. Lindley. 《理解不确定性》. Wiley, 2006.

[Lin+21] T. Lin, Y. Wang, X. Liu 和 X. Qiu. "Transformer综述". 载于: (2021). arXiv:2106.04554 [cs.LG].

[Lin56] D. Lindley. "关于实验提供信息的度量". 载于: 《数理统计年鉴》 (1956), 第986–1005页.

[Liu01] J. Liu. 《科学计算中的蒙特卡洛策略》. Springer, 2001.

[Liu+16] W. Liu, D. Anguelov, D. Erhan, C. Szegedy 和 S. Reed. "SSD：单次多框检测器". 载于: ECCV. 2016.

[Liu+18a] H. Liu, Y.-S. Ong, X. Shen 和 J. Cai. "当高斯过程遇上大数据：可扩展高斯过程综述". 载于: (2018). arXiv:1807.01065 [stat.ML].

---

[Liu+18b] L. Liu, X. Liu, C.-J. Hsieh, and D. Tao. “非精确海森矩阵和梯度下的非凸优化随机二阶方法”. In: (2018). arXiv: 1809.09853 [math.OC].

[Liu+20] F. Liu, X. Huang, Y. Chen, and J. A. K. Suykens. “核近似中的随机特征：算法、理论与展望综述”. In: (2020). arXiv: 2004.11154 [stat.ML].

[Liu+22] Z. Liu, H. Mao, C.-Y. Wu, C. Feichtenhofer, T. Darrell, and S. Xie. “面向2020年代的卷积网络”. In: (2022). arXiv: 2201.03545 [cs.CV].

[LJ09] H. Lukosevicius and H. Jaeger. “递归神经网络训练的储备池计算方法”. In: Computer Science Review 3.3 (2009), 127–149.

[LKB20] Q. Liu, M. J. Kusner, and P. Blunsom. “上下文嵌入综述”. In: (2020). arXiv: 2003.07278 [cs.CL].

[LLM14] D. Lay, S. Lay, and J. McDonald. 线性代数及其应用. Pearson, 2014.

[LLT89] K. Lange, R. Little, and J. Taylor. “基于T分布的稳健统计建模”. In: JASA 84.408 (1989), pp. 881–896.

[Llo82] S Lloyd. “PCM中的最小二乘量化”. In: IEEE Trans. Inf. Theory 28.2 (1982), pp. 129–137.

[LM04] E. Learned-Miller. 超间距与信息论量的估计. 技术报告 04-104. U. Mass. Amherst Comp. Sci. Dept, 2004.

[LM86] R. Larsen and M. Marx. 数理统计及其应用导论. Prentice Hall, 1986.

[LN81] D. V. Lindley and M. R. Novick. “可交换性在推断中的作用”. en. In: Annals of Statistics 9.1 (1981), pp. 45–58.

[LNK19] Q. Liu, M. Nickel, and D. Kiela. “双曲图神经网络”. In: Advances in Neural Information Processing Systems. 2019, pp. 8228–8239.

[Loa00] C. F. V. Loan. “无处不在的克罗内克积”. In: J. Comput. Appl. Math. 123.1 (2000), pp. 85–100.

[Lod+02] H. Lodhi, C. Saunders, J. Shawe-Taylor, N. Cristianini, and C. Watkins. “使用字符串核进行文本分类”. en. In: J. Mach. Learn. Res. (2002).

[LPM15] M.-T. Luong, H. Pham, and C. D. Manning. “基于注意力的神经机器翻译有效方法”. In: EMNLP. 2015.

[LR87] R. J. Little and D. B. Rubin. 缺失数据的统计分析. Wiley and Son, 1987.

[LRU14] J. Leskovec, A. Rajaraman, and J. Ullman. 大规模数据集挖掘. Cambridge, 2014.

[LS10] P. Long and R. Servedio. “随机分类噪声击败所有凸势提升器”. In: JMLR 78.3 (2010), pp. 287–304.

[LS19a] S. Lattanzi and C. Sohler. “通过局部搜索实现更好的k-means++算法”. In: ICML. Vol. 97. Proceedings of Machine Learning Research. PMLR, 2019, pp. 3662–3671.

[LS19b] Z. C. Lipton and J. Steinhardt. “机器学习研究中的问题趋势：部分ML论文存在缺陷，可能误导公众并阻碍未来研究”. In: The Queue 17.1 (2019), pp. 45–77.

[LSS13] Q. Le, T. Sarlos, and A. Smola. “Fastfood——在线性对数时间内计算希尔伯特空间展开”. In: ICML. Vol. 28. Proceedings of Machine Learning Research. PMLR, 2013, pp. 244–252.

[LSY19] H. Liu, K. Simonyan, and Y. Yang. “DARTS：可微架构搜索”. In: ICLR. 2019.

[Lu+19] L. Lu, Y. Shin, Y. Su, and G. E. Karniadakis. “死亡ReLU与初始化：理论与数值示例”. In: (2019). arXiv: 1903.06733 [stat.ML].

[Luo16] M.-T. Luong. “神经机器翻译”. 博士论文. Stanford Dept. Comp. Sci., 2016.

[Luo+19] P. Luo, X. Wang, W. Shao, and Z. Peng. “理解批归一化中的正则化”. In: ICLR. 2019.

[LUW17] C. Louizos, K. Ullrich, and M. Welling. “深度学习的贝叶斯压缩”. In: NIPS. 2017.

[Lux07] U. von Luxburg. “谱聚类教程”. In: Statistics and Computing 17.4 (2007), pp. 395–416.

[LW04a] O. Ledoit and M. Wolf. “大维协方差矩阵的良态估计量”. In: J. of Multivariate Analysis 88.2 (2004), pp. 365–411.

[LW04b] O. Ledoit and M. Wolf. “亲爱的，我收缩了样本协方差矩阵”. In: J. of Portfolio Management 31.1 (2004).

[LW04c] H. Lopes and M. West. “因子分析中的贝叶斯模型评估”. In: Statisica Sinica 14 (2004), pp. 41–67.

[LW16] C. Li and M. Wand. “基于马尔可夫生成对抗网络的预计算实时纹理合成”. In: ECCV. 2016.

[LWG12] U. von Luxburg, R. Williamson, and I. Guyon. “聚类：科学还是艺术？” In: Workshop on Unsupervised and Transfer Learning. 2012.

[LXW19] X. Liu, Q. Xu, and N. Wang. “基于深度神经网络的图像描述综述”. In: The Visual Computer 35.3 (2019), pp. 445–470.

[Lyu+20] X.-K. Lyu, Y. Xu, X.-F. Zhao, X.-N. Zuo, and C.-P. Hu. “超越心理学：p值和置信区间误解在不同领域的普遍性”. In: Journal of Pacific Rim Psychology 14 (2020).

[MA10] I. Murray and R. P. Adams. “潜高斯模型协方差超参数的切片采样”. In: NIPS. 2010, pp. 1732–1740.

[MA+17] Y. Movshovitz-Attias, A. Toshev, T. K. Leung, S. Ioffe, and S. Singh. “无繁琐距离

---

使用代理的度量学习。载于：ICCV. 2017.

[Maa+11] A. L. Maas, R. E. Daly, P. T. Pham, D. Huang, A. Y. Ng, and C. Potts. "用于情感分析的词向量学习"。载于：ACL会议论文集. 2011, pp. 142–150.

[Maa14] L. van der Maaten. "使用基于树的算法加速t-SNE"。载于：JMLR (2014).

[Mac03] D. MacKay. 信息论、推理与学习算法. 剑桥大学出版社, 2003.

[Mac09] L. W. Mackey. "稀疏PCA的收缩方法"。载于：NIPS. 2009.

[Mac67] J MacQueen. “多元观测的分类与分析方法”. en. 载于：第五届伯克利数学统计与概率研讨会论文集，第1卷：统计学. 加州大学校务委员会, 1967.

[Mac95] D. MacKay. “概率网络与合理预测——监督神经网络实用贝叶斯方法综述”. 载于：Network: Computation in Neural Systems 6.3 (1995), pp. 469–505.

[Mad+20] A. Madani, B. McCann, N. Naik, N. S. Keskar, N. Anand, R. R. Eguchi, P.-S. Huang, and R. Socher. "ProGen: 蛋白质生成的语言模型". en. 2020.

[Mah07] R. P. S. Mahler. 统计多源多目标信息融合. Artech House出版社, 2007.

[Mah13] R Mahler. “多源多目标检测与跟踪的统计102讲”. 载于：IEEE J. Sel. Top. Signal Process. 7.3 (2013), pp. 376–389.

[Mah+18] D. Mahajan, R. Girshick, V. Ramanathan, K. He, M. Paluri, Y. Li, A. Bharambe, and L. van der Maaten. "探索弱监督预训练的极限". 载于：(2018). arXiv: 1805.00932 [cs.CV].

[Mah+23] K. Mahowald, A. A. Ivanova, I. A. Blank, N. Kanwisher, J. B. Tenenbaum, and E. Fedorenko. "大型语言模型中语言与思维的分离：认知视角". 载于：(Jan. 2023). arXiv: 2301.06627 [cs.CL].

[Mai15] J Mairal. "增量式最大化-最小化优化及其在大规模机器学习中的应用". 载于：SIAM J. Optim. 25.2 (2015), pp. 829–855.

[Mak+19] D. Makowski, M. S. Ben-Shachar, S. H. A. Chen, and D. Lüdecke. "贝叶斯框架下效应存在与显著性指标". en. 载于：Front. Psychol. 10 (2019), p. 2767.

[Mal99] S. Mallat. 信号处理的小波导论. 学术出版社, 1999.

[Man+16] V. Mansinghka, P. Shafto, E. Jonas, C. Petschulat, M. Gasner, and J. Tenenbaum. "Crosscat: 一种用于分析异质高维数据的全贝叶斯非参数方法". 载于：JMLR 17 (2016).

[Mar06] H. Markram. "蓝脑计划". en. 载于：Nat. Rev. Neurosci. 7.2 (2006), pp. 153–160.

[Mar08] B. Marlin. "机器学习中的缺失数据问题". 博士论文. 多伦多大学, 2008.

[Mar+11] B. M. Marlin, R. S. Zemel, S. T. Roweis, and M. Slaney. "推荐系统、缺失数据与统计模型估计". 载于：IJCAI. 2011.

[Mar18] O. Martin. 使用Python的贝叶斯分析. Packt出版社, 2018.

[Mar20] G. Marcus. "人工智能的下一个十年：迈向鲁棒人工智能的四步". 载于：(2020). arXiv: 2002.06177 [cs.AI].

[Mar72] G. Marsaglia. "从球面选取一点". en. 载于：Ann. Math. Stat. 43.2 (1972), pp. 645–646.

[Mas+00] L. Mason, J. Baxter, P. L. Bartlett, and M. R. Frean. "作为梯度下降的Boosting算法". 载于：NIPS. 2000, pp. 512–518.

[Mas+15] J. Masci, D. Boscaini, M. Bronstein, and P. Vandergheynst. "黎曼流形上的测地卷积神经网络". 载于：IEEE国际计算机视觉研讨会论文集. 2015, pp. 37–45.

[Mat00] R. Matthews. “鹳鸟送子（p = 0.008）. 载于：Teach. Stat. 22.2 (2000), pp. 36–38.

[Mat98] R. Matthews. 健康统计的贝叶斯批评：大健康骗局. 1998.

[MAV17] D. Molchanov, A. Ashukha, and D. Vetrov. "变分dropout稀疏化深度神经网络". 载于：ICML. 2017.

[MB05] F. Morin and Y. Bengio. "分层概率神经网络语言模型". 载于：AISTATS. 2005.

[MB06] N. Meinshausen and P. Buhlmann. "高维图与lasso变量选择". 载于：The Annals of Statistics 34 (2006), pp. 1436–1462.

[MBL20] K. Musgrave, S. Belongie, and S.-N. Lim. "度量学习现实检验". 载于：ECCV. 2020.

[McE20] R. McElreath. 统计反思：使用R和Stan的贝叶斯课程（第二版）. en. 查普曼与霍尔/CRC出版社, 2020.

[McL75] G. J. McLachlan. “构建判别分析渐近最优分配规则的迭代重分类过程”. 载于：Journal of the American Statistical Association 70.350 (1975), pp. 365–369.

[MD97] X. L. Meng and D. van Dyk. “EM算法——以快速新调子演唱的古老民歌（附讨论）”. 载于：J. Royal Stat. Soc. B 59 (1997), pp. 511–567.

[ME14] S. Masoudnia and R. Ebrahimpour. "专家混合：文献综述". 载于：Artificial Intelligence Review 42.2 (2014), pp. 275–293.

[Mei01] M. Meila. "谱分割的随机游走视角". 载于：AISTATS. 2001.

[Mei05] M. Meila. "比较聚类：公理化视角". 载于：ICML. 2005.

---

[Men+12] T. Mensink, J. Verbeek, F. Perronnin, and G. Csurka. "面向大规模图像分类的度量学习：以近乎零代价泛化到新类别". In: ECCV. Springer Berlin Heidelberg, 2012, pp. 488–501.

[Men+21] A. K. Menon, S. Jayasumana, A. S. Rawat, H. Jain, A. Veit, and S. Kumar. "通过Logit调整进行长尾学习". In: ICLR. 2021.

[Men+22] K. Meng, D. Bau, A. Andonian, and Y. Belinkov. "定位与编辑GPT中的事实关联". In: (Feb. 2022). arXiv: 2202.05262 [cs.CL].

[Met21] C. Metz. 《天才制造者：将AI带向Google、Facebook和世界的叛逆者》. en. Dutton, 2021.

[MF17] J. Matejka and G. Fitzmaurice. "相同统计量，不同图形：通过模拟退火生成具有多样外观和相同统计量的数据集". In: Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems. Association for Computing Machinery, 2017, pp. 1290–1294.

[MFR20] G. M. Martin, D. T. Frazier, and C. P. Robert. "计算贝叶斯：从1763年到21世纪的贝叶斯计算". In: (2020). arXiv: 2004.06425 [stat.CO].

[MG05] I. Murray and Z. Ghahramani. 关于证据与贝叶斯奥卡姆剃刀的说明. Tech. rep. Gatsby, 2005.

[MH07] A. Mnih and G. Hinton. "三种新的统计语言建模图模型". en. In: ICML. 2007.

[MH08] L. v. d. Maaten and G. Hinton. "使用t-SNE可视化数据". In: JMLR 9.Nov (2008), pp. 2579–2605.

[MHM18] L. McInnes, J. Healy, and J. Melville. "UMAP：用于降维的一致流形近似与投影". In: (2018). arXiv: 1802.03426 [stat.ML].

[MHN13] A. L. Maas, A. Y. Hannun, and A. Y. Ng. "修正线性单元改善神经网络声学模型". In: ICML. Vol. 28. 2013.

[Mik+13a] T. Mikolov, K. Chen, G. Corrado, and J. Dean. "向量空间中词表示的高效估计". In: ICLR. 2013.

[Mik+13b] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, and J. Dean. "词与短语的分布式表示及其组合性". In: NIPS. 2013.

[Mik+13c] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean. "词与短语的分布式表示及其组合性". In: NIPS. 2013, pp. 3111–3119.

[Min00] T. Minka. 贝叶斯模型平均并非模型组合. Tech. rep. MIT Media Lab, 2000.

[Min+09] M. Mintz, S. Bills, R. Snow, and D. Jurafsky. "无标注数据的远程监督关系抽取". In: Prof. Conf. Recent Advances in NLP. 2009.

[Mit97] T. Mitchell. 《机器学习》. McGraw Hill, 1997.

[Miy+18] T. Miyato, S.-I. Maeda, M. Koyama, and S. Ishii. "虚拟对抗训练：一种用于监督与半监督学习的正则化方法". In: IEEE PAMI (2018).

[MK97] G. J. McLachlan and T. Krishnan. 《EM算法及其扩展》. Wiley, 1997.

[MKH19] R. Müller, S. Kornblith, and G. E. Hinton. "标签平滑何时有帮助？". In: NIPS. 2019, pp. 4694–4703.

[MKL11] O. Martin, R. Kumar, and J. Lao. 《Python中的贝叶斯建模与计算》. CRC Press, 2011.

[MKL21] O. A. Martin, R. Kumar, and J. Lao. 《Python中的贝叶斯建模与计算》. CRC Press, 2021.

[MKS21] K. Murphy, A. Kumar, and S. Serghiou. "COVID-19接触者追踪应用的风险评分学习". In: Machine Learning for Healthcare. 2021.

[MM16] D. Mishkin and J. Matas. "你只需一个好的初始化". In: ICLR. 2016.

[MN89] P. McCullagh and J. Nelder. 《广义线性模型》第二版. Chapman and Hall, 1989.

[MNM02] W. Maass, T. Natschlaeger, and H. Markram. "无稳定状态的实时计算：一种基于扰动的神经计算新框架". In: Neural Computation 14.11 (2002), 2531—2560.

[MO04] S. C. Madeira and A. L. Oliveira. "生物数据分析中的双聚类算法：综述". In: IEEE/ACM Transactions on Computational Biology and Bioinformatics 1.1 (2004), pp. 24–45.

[Mol04] C. Moler. 《MATLAB数值计算》. SIAM, 2004.

[Mon+14] G. F. Montufar, R. Pascanu, K. Cho, and Y. Bengio. "关于深度神经网络线性区域的数量". In: NIPS. 2014.

[Mon+17] F. Monti, D. Boscaini, J. Masci, E. Rodola, J. Svoboda, and M. M. Bronstein. "使用混合模型CNN在图与流形上进行几何深度学习". In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2017, pp. 5115–5124.

[Mon+19] N. Monath, A. Kobren, A. Krishnamurthy, M. R. Glass, and A. McCallum. "基于树嫁接的可扩展层次聚类". In: KDD. KDD '19. Association for Computing Machinery, 2019, pp. 1438–1448.

[Mon+21] N. Monath et al. "可扩展的自底向上层次聚类". In: KDD. 2021.

[Mor+16] R. D. Morey, R. Hoekstra, J. N. Rouder, M. D. Lee, and E.-J. Wagenmakers. "对置信区间赋予置信的谬误". en. In: Psychon. Bull. Rev. 23.1 (2016), pp. 103–123.

[MOT15] A. Mordvintsev, C. Olah, and M. Tyka. “初始主义：深入神经网络”. https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html. Accessed: NĂ-NĂ-NĂ. 2015.

---

[MP43] W. McCulloch 和 W. Pitts。“神经活动中内在思想的逻辑演算”。载于：《数学生物物理学通报》5（1943 年），第 115–137 页。

[MP69] M. Minsky 和 S. Papert。《感知机》。MIT 出版社，1969 年。

[MRS08] C. Manning、P. Raghavan 和 H. Schuetze。《信息检索导论》。剑桥大学出版社，2008 年。

[MS11] D. Mayo 和 A. Spanos。“误差统计学”。载于：《科学哲学手册》。由 P. S. Bandyopadhyay 和 M. R. Forster 编辑，2011 年。

[Muk+19] B. Mukhoty、G. Gopakumar、P. Jain 和 P. Kar。“用于稳健回归问题的全局收敛迭代重加权最小二乘法”。载于：AISTATS。2019 年，第 313–322 页。

[Mur23] K. P. Murphy。《概率机器学习：高级主题》。MIT 出版社，2023 年。

[MV15] A. Mahendran 和 A. Vedaldi。“通过逆变换理解深度图像表示”。载于：CVPR。2015 年，第 5188–5196 页。

[MV16] A. Mahendran 和 A. Vedaldi。“使用自然预像可视化深度卷积神经网络”。载于：《国际计算机视觉杂志》（2016 年），第 1–23 页。

[MWK16] A. H. Marblestone、G. Wayne 和 K. P. Kording。“走向深度学习与神经科学的整合”。英文。载于：《前沿：计算神经科学》10（2016 年），第 94 页。

[MWP98] B. Moghaddam、W. Wahid 和 A. Pentland。“超越特征脸：用于人脸识别的概率匹配”。载于：第三届 IEEE 国际自动人脸与手势识别会议论文集。1998 年，第 30–35 页。

[Nad+19] S. Naderi、K. He、R. Aghajani、S. Sclaroff 和 P. Felzenszwalb。“广义最大-最小化”。载于：ICML。2019 年。

[Nak+19] P. Nakkiran、G. Kaplun、Y. Bansal、T. Yang、B. Barak 和 I. Sutskever。“深度双重下降：更大模型和更多数据为何有害”。载于：（2019 年）。arXiv: 1912.02292 [cs.LG]。

[NAM21] C. G. Northcutt、A. Athalye 和 J. Mueller。“测试集中普遍存在的标签错误破坏机器学习基准”。载于：NeurIPS 数据集与基准赛道。2021 年 3 月。

[Nar+23] H. Narasimhan、A. K. Menon、W. Jitkritum 和 S. Kumar。“用于带分布外检测的选择性分类的插件估计器”。载于：arXiv [cs.LG]（2023 年 1 月）。

[Nea96] R. Neal。《神经网络的贝叶斯学习》。Springer，1996 年。

[Nes04] Y. Nesterov。《凸优化入门讲座：基础课程》。Kluwer，2004 年。

[Neu04] A. Neumaier。“连续全局优化与约束满足中的完全搜索”。载于：《数值学年鉴》13（2004 年），第 271–369 页。

[Neu17] G. Neubig。“神经机器翻译与序列到序列模型：教程”。载于：（2017 年）。arXiv: 1703.01619 [cs.CL]。

[Ngu+17] A. Nguyen、J. Yosinski、Y. Bengio、A. Dosovitskiy 和 J. Clune。“即插即用生成网络：潜在空间中图像的条件迭代生成”。载于：CVPR。2017 年。

[NH98] R. M. Neal 和 G. E. Hinton。“对 EM 算法的一种观点，证明增量、稀疏及其他变体的合理性”。载于：《图模型中的学习》。由 M. I. Jordan 编辑。Springer 荷兰，1998 年，第 355–368 页。

[NHLs19] E. Nalisnick、J. M. Hernández-Lobato 和 P. Smyth。“作为结构化收缩先验的 Dropout”。载于：ICML。2019 年。

[Nic+15] M. Nickel、K. Murphy、V. Tresp 和 E. Gabrilovich。“面向知识图谱的关系机器学习综述”。载于：《IEEE 会刊》（2015 年）。

[Niu+11] F. Niu、B. Recht、C. Re 和 S. J. Wright。“HOGWILD!：一种无锁的随机梯度下降并行化方法”。载于：NIPS。2011 年。

[NJ02] A. Y. Ng 和 M. I. Jordan。“关于判别式与生成式分类器：逻辑回归与朴素贝叶斯的比较”。载于：NIPS-14。2002 年。

[NJW01] A. Ng、M. Jordan 和 Y. Weiss。“关于谱聚类：分析与算法”。载于：NIPS。2001 年。

[NK17] M. Nickel 和 D. Kiela。“用于学习分层表示的庞加莱嵌入”。载于：《神经信息处理系统进展》。2017 年，第 6338–6347 页。

[NK18] M. Nickel 和 D. Kiela。“在双曲几何的洛伦兹模型中学习连续层次结构”。载于：《国际机器学习大会》。2018 年，第 3779–3788 页。

[NK19] T. Niven 和 H.-Y. Kao。“探究神经网络对自然语言论证的理解”。载于：ACL 会议论文集。2019 年。

[NMC05] A. Niculescu-Mizil 和 R. Caruana。“通过监督学习预测良好概率”。载于：ICML。2005 年。

[Nou+02] M. N. Nounou、B. R. Bakshi、P. K. Goel 和 X. Shen。“通过贝叶斯潜变量回归进行过程建模”。载于：《美国化学工程师学会期刊》48.8（2002 年），第 1775–1793 页。

[Nov62] A. Novikoff。“关于感知机收敛性的证明”。载于：《自动机数学理论研讨会》12（1962 年），第 615–622 页。

[NR18] G. Neu 和 L. Rosasco。“迭代平均作为随机梯度下降的正则化”。载于：COLT。2018 年。

[NTL20] J. Nixon、D. Tran 和 B. Lakshminarayanan。“为什么自举神经网络表现不佳？”载于：NIPS 研讨会“我不敢相信它没有更好”。2020 年。

[NW06] J. Nocedal 和 S. Wright。《数值优化》。Springer，2006 年。

[Ode16] A. Odena。“基于生成对抗网络的半监督学习”。载于：arXiv 预印本 arXiv:1606.01583（2016 年）。

[OLV18] A. van den Oord、Y. Li 和 O. Vinyals。“通过对比预测进行表示学习”。

---

[OMS17] C. Olah, A. Mordvintsev, and L. Schubert. "特征可视化". In: Distill (2017).

[Oor+16] A. Van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu. "WaveNet: 一种用于原始音频的生成模型". In: (2016). arXiv: 1609.03499 [cs.SD].

[Oor+18] A. van den Oord et al. "并行WaveNet: 快速高保真语音合成". In: ICML. 编辑 J. Dy and A. Krause. 卷 80. 机器学习研究会议论文集. PMLR, 2018, pp. 3918–3926.

[Ope] OpenAI. ChatGPT: 优化对话的语言模型. 博客.

[Ope23] OpenAI. GPT4. 技术报告. 2023.

[OPK12] G. Ohloff, W. Pickenhagen, and P. Kraft. 香气与化学. 英文. Wiley, 2012.

[OPT00a] M. R. Osborne, B. Presnell, and B. A. Turlach. "最小二乘问题中变量选择的新方法". In: IMA数值分析杂志 20.3 (2000), pp. 389–403.

[OPT00b] M. R. Osborne, B. Presnell, and B. A. Turlach. "关于lasso及其对偶". In: 计算与图形统计杂志 9 (2000), pp. 319–337.

[Ort+19] P. A. Ortega et al. "序列策略的元学习". In: (2019). arXiv: 1905.03030 [cs.LG].

[Osb16] I. Osband. "深度学习中的风险与不确定性：贝叶斯、自助法与Dropout的危险". In: NIPS贝叶斯深度学习研讨会. 2016.

[OTJ07] G. Obozinski, B. Taskar, and M. I. Jordan. 分组分类的联合协变量选择. 技术报告. UC Berkeley, 2007.

[Ouy+22] L. Ouyang et al. "训练语言模型遵循人类反馈的指令". In: (2022年3月). arXiv: 2203.02155 [cs.CL].

[Pai05] A. Pais. 主是微妙的：阿尔伯特·爱因斯坦的科学与生活. 英文. 牛津大学出版社, 2005.

[Pan+15] V. Panayotov, G. Chen, D. Povey, and S. Khudanpur. "Librispeech: 基于公共领域有声读物的语音识别语料库". In: ICASSP. IEEE. 2015, pp. 5206–5210.

[Pap+18] G. Papandreou, T. Zhu, L.-C. Chen, S. Gidaris, J. Tompson, and K. Murphy. "PersonLab: 自下而上、基于部件、几何嵌入模型的人体姿态估计与实例分割". In: ECCV. 2018, pp. 269–286.

[Par+16a] A. Parikh, O. Täckström, D. Das, and J. Uszkoreit. "自然语言推理的可分解注意力模型". In: EMNLP. 计算语言学协会, 2016, pp. 2249–2255.

[Par+16b] A. Parikh, O. Täckström, D. Das, and J. Uszkoreit. "自然语言推理的可分解注意力模型". In: EMNLP. 计算语言学协会, 2016, pp. 2249–2255.

[Par+18] N. Parmar, A. Vaswani, J. Uszkoreit, L. Kaiser, N. Shazeer, A. Ku, and D. Tran. "图像Transformer". In: ICLR. 2018.

[Pas14] R. Pascanu. "关于递归和深度神经网络". 博士论文. 蒙特利尔大学, 2014.

[PARS14] B. Perozzi, R. Al-Rfou, and S. Skiena. "Deepwalk: 社交表示的在线学习". In: 第20届ACM SIGKDD国际知识发现与数据挖掘会议论文集. ACM. 2014, pp. 701–710.

[Pat12] A. Paterek. 预测电影评分与推荐系统. 2012.

[Pat+16] D. Pathak, P. Krahenbuhl, J. Donahue, T. Darrell, and A. A. Efros. "上下文编码器：通过图像修复进行特征学习". In: CVPR. 2016.

[Pau+20] A. Paullada, I. D. Raji, E. M. Bender, E. Denton, and A. Hanna. "数据及其（非）内容：机器学习研究中数据集开发与使用调查". In: NeurIPS 2020研讨会：机器学习回顾、调查与元分析 (ML-RSA). 2020.

[PB+14] N. Parikh, S. Boyd, et al. "近端算法". In: 优化基础与趋势 1.3 (2014), pp. 127–239.

[Pea18] J. Pearl. 机器学习理论障碍与因果革命的七颗火花. 技术报告. UCLA, 2018.

[Pen+20] Z. Peng, W. Huang, M. Luo, Q. Zheng, Y. Rong, T. Xu, and J. Huang. "通过图互信息最大化进行图表示学习". In: 万维网会议论文集. 2020.

[Per+17] B. Perozzi, V. Kulkarni, H. Chen, and S. Skiena. "不要走，要跳！多尺度网络嵌入的在线学习". In: 2017年IEEE/ACM国际社会网络分析与挖掘进展会议论文集 2017. ASONAM'17. 计算机协会, 2017, 258–265.

[Pet13] J. Peters. 当冰淇淋销量上升，凶杀案也上升。是巧合，还是你的下一个蛋筒会谋杀你？https://slate.com/news-and-politics/2013/07/warm-weather-homicide-rates-when-ice-cream-sales-rise-homicides-rise-coincidence.html. 访问日期：2020-5-20. 2013.

[Pet+18] M. E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee, and L. Zettlemoyer. "深层上下文化的词表示". In: NAACL. 2018.

[Pey20] G. Peyre. "机器学习优化课程笔记". 2020.

[PH18] T. Parr and J. Howard. "深度学习所需的矩阵微积分". In: (2018). arXiv: 1802.01528 [cs.LG].

[Pin88] F. J. Pineda. "反向传播到递归和高阶神经网络的推广". In: 神经信息处理系统. 1988, pp. 602–611.