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

<div style="text-align: center;"><img src="imgs/img_in_image_box_201_138_523_405.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_609_138_955_408.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 21.5：(a) 部分酵母基因表达数据以热图形式呈现。(b) 相同数据以时间序列形式呈现。由 yeast_data_viz.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_239_528_525_815.jpg" alt="Image" width="24%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_600_523_982_836.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 21.b：对酵母基因表达数据应用层次聚类。(a) 根据层次聚类方案（平均连接凝聚聚类）对行进行重新排序，使相似的行彼此靠近。(b) 在某个高度切割平均连接树后得到的聚类结果。由 hclust_yeast_demo.ipynb 生成。</div>


在某个高度处切割，我们得到图 21.6(b) 所示的 16 个聚类。分配给每个聚类的时间序列确实彼此“相似”。

#### 21.2.3 扩展

基本的 HAC 算法有许多扩展。例如，[Mon+21] 提出了一种更具可扩展性的自底向上算法版本，它并行构建子聚类。[Mon+19] 则讨论了该算法的在线版本，能够在数据到达时进行聚类，同时重新考虑

---

先前的聚类决策（而不仅仅是贪心决策）。在某些假设下，这种方法可以证明恢复出真实的潜在结构。这对于在流式文本数据中对“实体”（如人或事物）的“提及”进行聚类很有用（该问题称为实体发现）。

### 21.3 K均值聚类

层次凝聚聚类（第21.2节）存在几个问题。首先，它需要 $ O(N^{3}) $ 时间（平均链接方法），难以应用于大规模数据集。其次，它假设已经计算出了相异性矩阵，而“相似性”的概念通常不明确，需要学习。第三，它只是一个算法，而非模型，因此很难评估其优劣，即没有明确的目标函数进行优化。

在本节中，我们讨论K均值算法 [Mac67; Llo82]，该算法解决了上述问题。首先，它的运行时间为 $ O(NKT) $，其中 $ T $ 为迭代次数。其次，它通过计算数据点到学习到的聚类中心 $ \boldsymbol{\mu}_k \in \mathbb{R}^D $ 的欧氏距离来衡量相似性，而不需要相异性矩阵。第三，正如我们将看到的，它优化了一个定义明确的代价函数。

#### 21.3.1 算法

假设存在 $K$ 个聚类中心 $\boldsymbol{\mu}_k \in \mathbb{R}^D$，那么我们可以通过将每个数据点 $\boldsymbol{x}_n \in \mathbb{R}^D$ 分配到其最近的中心来进行聚类：

$$  z_{n}^{*}=\arg\min_{k}||\boldsymbol{x}_{n}-\boldsymbol{\mu}_{k}||_{2}^{2}   \tag*{(21.13)}$$

当然，我们不知道聚类中心，但可以通过计算分配给每个中心的所有点的平均值来估计它们：

$$  \mu_{k}=\frac{1}{N_{k}}\sum_{n:z_{n}=k}x_{n}   \tag*{(21.14)}$$

然后我们可以迭代这些步骤直至收敛。

更正式地说，我们可以将其视为寻找以下代价函数（称为畸变）的局部最小值：

$$  J(\mathbf{M},\mathbf{Z})=\sum_{n=1}^{N}||\boldsymbol{x}_{n}-\boldsymbol{\mu}_{z_{n}}||^{2}=||\mathbf{X}-\mathbf{Z}\mathbf{M}^{\mathsf{T}}||_{F}^{2}   \tag*{(21.15)}$$

其中 $\mathbf{X} \in \mathbb{R}^{N \times D}$，$\mathbf{Z} \in [0,1]^{N \times K}$，并且 $\mathbf{M} \in \mathbb{R}^{D \times K}$ 的列中包含聚类中心 $\boldsymbol{\mu}_k$。K均值通过交替最小化来优化该函数（这与高斯混合模型的EM算法密切相关，我们将在第21.4.1.1节讨论）。

#### 21.3.2 示例

在本节中，我们给出一些K均值聚类的示例。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_224_123_539_334.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">$(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_633_125_947_334.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图21.7：二维平面中K-means聚类的示意图。图中展示了使用两种不同随机种子得到的结果。改编自[Gér19]的图9.5。由kmeans_voronoi.ipynb生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_209_452_542_730.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_641_453_952_729.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图21.8：使用K-means聚类（K=16）对图21.5中的酵母数据进行聚类的结果。(a) 可视化每个簇中分配的所有时间序列。(b) 将16个簇中心可视化为典型的时间序列。由kmeans_yeast_demo.ipynb生成。</div>

##### 21.3.2.1 二维平面中点的聚类

图21.7展示了K-means聚类应用于二维平面中一些点的示例。可以看到，该方法在数据点上诱导了一个Voronoi镶嵌。聚类结果对初始化敏感。实际上，右侧质量较低的聚类具有更大的失真。默认情况下，sklearn使用10次随机重启（结合第21.3.4节所述的K-means++初始化方法），并返回失真最小的聚类结果。（在sklearn中，失真被称为“惯量”。）

##### 21.3.2.2 酵母细胞基因表达时间序列数据的聚类

在图21.8中，我们展示了将K-means聚类（K=16）应用于图21.5所示的300×7酵母时间序列矩阵的结果。可以看到，“外观相似”的时间序列被划分到了同一簇中。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_195_134_416_311.jpg" alt="图像" width="19%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_474_136_695_311.jpg" alt="图像" width="19%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_754_136_974_311.jpg" alt="图像" width="19%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图 21.9：使用码本大小为 K 的向量量化压缩后的图像。(a) K = 2。(b) K = 4。(c) 原始未压缩图像。由 vqDemo.ipynb 生成。</div>

分配到同一簇。我们还可以看到，每个簇的质心是对该簇所有数据点的一个合理概括。最后，我们注意到第 6 组没有被使用，因为没有数据点被分配到该组。然而，这只是初始化过程中的一个偶然情况，如果我们重复该算法，并不保证能得到相同的聚类结果或相同的簇数。（我们将在第 21.3.4 节讨论初始化该方法的良好方式，并在第 21.3.7 节讨论选择 K 的方法。）

#### 21.3.3 向量量化

假设我们希望对某些实值向量 $\boldsymbol{x}_n \in \mathbb{R}^D$ 进行有损压缩。一个非常简单的方法是使用**向量量化**（Vector Quantization, VQ）。其基本思想是将每个实值向量 $\boldsymbol{x}_n \in \mathbb{R}^D$ 替换为一个离散符号 $z_n \in \{1, \ldots, K\}$，该符号是码本中 $K$ 个原型 $\boldsymbol{\mu}_k \in \mathbb{R}^D$ 的索引。每个数据向量通过使用最相似原型的索引进行编码，相似度由欧氏距离度量：

$$ \mathrm{encode}(\boldsymbol{x}_{n}) = \arg\min_{k} ||\boldsymbol{x}_{n} - \boldsymbol{\mu}_{k}||^{2} \tag*{(21.16)} $$

我们可以定义一个代价函数，通过计算由编码本引起的重建误差或失真来衡量其质量：

$$ J \triangleq \frac{1}{N} \sum_{n=1}^{N} ||\boldsymbol{x}_{n} - \mathrm{decode}(\mathrm{encode}(\boldsymbol{x}_{n}))||^{2} = \frac{1}{N} \sum_{n=1}^{N} ||\boldsymbol{x}_{n} - \boldsymbol{\mu}_{z_{n}}||^{2} \tag*{(21.17)} $$

其中 $\text{decode}(k) = \boldsymbol{\mu}_k$。这恰好是 K 均值算法所最小化的代价函数。

当然，如果我们为每个数据向量分配一个原型，即令 $K = N$ 且 $\boldsymbol{\mu}_n = \boldsymbol{x}_n$，则可以实现零失真。但这样完全不会压缩数据。具体而言，它需要 $O(NDB)$ 比特，其中 $N$ 是实值数据向量的数量，每个向量的长度为 $D$，$B$ 是表示一个实值标量所需的比特数（表示每个 $\boldsymbol{x}_n$ 的量化精度）。

通过检测数据中的相似向量，为它们创建原型或质心，然后将数据表示为相对于这些原型的偏差，我们可以做得更好。这减少了空间占用。

---

所需的比特数为 $ O(N\log_2 K + KDB) $。其中 $ O(N\log_2 K) $ 项来源于每个数据向量需要指明它使用的是K个码字中的哪一个；而 $ O(KDB) $ 项则来源于我们必须存储每个码本条目，每个条目是一个D维向量。当N很大时，第一项占主导地位，因此我们可以将编码方案的码率（每个对象所需的比特数）近似为 $ O(\log_2 K) $，这通常远小于 $ O(DB) $。

VQ的一个应用是图像压缩。考虑图21.9中的 $ 200 \times 320 $ 像素图像；我们将其视为 $ N = 64,000 $ 个标量的集合。如果用一个字节表示每个像素（0到255的灰度强度），则 $ B = 8 $，因此未压缩形式表示该图像需要 $ NB = 512,000 $ 比特。对于压缩后的图像，我们需要 $ O(N \log_2 K) $ 比特。对于 $ K = 4 $，这大约是128kb，压缩比为4倍，但感知损失可忽略不计（见图21.9(b)）。

如果对像素间的空间相关性进行建模（例如，像JPEG那样编码5x5块），可以实现更高的压缩比。这是因为残差（与模型预测的差异）会更小，因而编码所需的比特数更少。这揭示了数据压缩与密度估计之间的深刻联系。更多信息请参见本书的续篇[Mur23]。

#### 21.3.4 K-means++算法

K-means优化的是一个非凸目标，因此需要仔细初始化。一种简单的方法是随机选取K个数据点作为 $ \mu_k $ 的初始值。我们可以通过多次重启来改进这一方法，即从不同的随机起始点多次运行算法，然后选择最佳解。然而，这可能会很慢。

更好的方法是顺序选取中心，以试图“覆盖”数据。具体来说，初始点均匀随机选取，然后每个后续点从剩余点中选取，选取概率与该点到其最近聚类中心的平方距离成正比。也就是说，在第t次迭代中，我们以如下概率选取下一个聚类中心 $ \boldsymbol{\mu}_{t} $ 为 $ \boldsymbol{x}_{n} $：

$$  p(\boldsymbol{\mu}_{t}=\boldsymbol{x}_{n})=\frac{D_{t-1}(\boldsymbol{x}_{n})}{\sum_{n^{\prime}=1}^{N}D_{t-1}(\boldsymbol{x}_{n^{\prime}})}   \tag*{(21.18)}$$

其中

$$  D_{t-1}(\boldsymbol{x})=\min_{k=1}^{t-1}||\boldsymbol{x}-\boldsymbol{\mu}_{k}||_{2}^{2}   \tag*{(21.19)}$$

是 $ \mathbf{x} $ 到截至第 $ t-1 $ 步的最近现存在中心的平方距离。因此，距离中心较远的点更有可能被选中，从而减少了失真。这被称为最远点聚类 [Gon85] 或 K-means++ [AV07; Bah+12; Bac+16; BLK17; LS19a]。令人惊讶的是，这一简单技巧可以证明保证重构误差从不会比最优解差超过 $ O(\log K) $ 倍 [AV07]。

#### 21.3.5 K-medoids算法

存在一种K-means的变体，称为K-medoids算法，其中我们通过选择数据示例 $ \boldsymbol{x}_n \in \mathcal{X} $ 来估计每个聚类中心 $ \mu_k $，该示例与该聚类中所有其他点的平均相异性最小；这样的点称为medoid。相比之下，在K-means中，我们取分配到该聚类的点 $ \boldsymbol{x}_n \in \mathbb{R}^D $ 的平均值来计算中心。K-medoids在处理异常值时更为鲁棒。

---

异常值（尽管该问题也可以通过使用学生t分布混合而非高斯混合来解决）。更重要的是，K-medoids 可以应用于数据不在 $\mathbb{R}^D$ 中的情况，此时求平均可能没有明确的定义。在 K-medoids 中，算法的输入是 $N \times N$ 的成对距离矩阵 $D(n, n')$，而不是 $N \times D$ 的特征矩阵。

求解 K-medoids 的经典算法是围绕中心点的划分（PAM）方法 [KR87]。在该方法中，每次迭代时，我们需要遍历所有 K 个中心点。对于每个中心点 m，我们考虑每个非中心点 o，交换 m 和 o，并重新计算代价（所有点到其中心点的距离之和）。如果代价降低，则保留这次交换。该算法的运行时间为 $O(N^{2}KT)$，其中 T 是迭代次数。

还有一种更简单且更快速的方法，称为基于 [PJ09] 的 Voronoi 迭代方法。在该方法中，每次迭代包含两个步骤，类似于 K-means。首先，对于每个簇 k，查看当前分配给该簇的所有点 $S_k = \{n : z_n = k\}$，然后设 $m_k$ 为该集合的中心点索引。（要找到中心点，需要检查所有 $|S_k|$ 个候选点，并选择到 $S_k$ 中所有其他点距离之和最小的那个。）其次，对于每个点 n，将其分配给最近的中心点，即 $z_n = \arg\min_k D(n, k)$。伪代码如算法 21.2 所示。

**算法 21.2：K-medoids 算法**

1 初始化 $m_{1:K}$ 为 $\{1,\ldots,N\}$ 中大小为 K 的随机子集

2 重复

3  $\begin{array}{l} z_{n} = \arg\min_{k} d(n, m_{k}) \text{ 对于 } n = 1 : N \\ m_{k} = \arg\min_{n:z_{n}=k} \sum_{n^{\prime}:z_{n^{\prime}}=k} d(n, n^{\prime}) \text{ 对于 } k = 1 : K \\ \end{array}$

5 直至收敛

#### 21.3.6 加速技巧

K-means 聚类的时间复杂度为 $O(NKI)$，其中 I 是迭代次数，但我们可以利用各种技巧来降低常数因子。例如，[Elk03] 展示了如何利用三角不等式来跟踪输入与质心之间距离的下界和上界，这可以消除一些冗余计算。另一种方法是使用 [Scu10] 提出的小批量近似。这种方法可能显著更快，但可能带来稍差的损失（见图 21.10）。

#### 21.3.7 选择簇数 K

在本节中，我们将讨论如何在 K-means 算法及其他相关方法中选择簇数 K。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_302_124_869_402.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图21.10：在图21.7的二维数据上，批量K-means与小批量K-means聚类的对比示意图。左图：失真度随K的变化。右图：训练时间随K的变化。改编自[Gér19]的图9.6。由kmeans_minibatch.ipynb生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_199_519_414_660.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_479_519_693_659.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_757_519_972_657.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图21.11：在图21.7的二维数据集上，K-means和GMM的性能随K的变化。(a) 验证集上的失真度随K的变化。由kmeans_silhouette.ipynb生成。(b) BIC随K的变化。由gmm_2d.ipynb生成。(c) 轮廓系数随K的变化。由kmeans_silhouette.ipynb生成。</div>


##### 21.3.7.1 最小化失真

基于监督学习的经验，选择K的一个自然方法是选取能最小化验证集上重构误差的值，其定义如下：

$$  \mathrm{err}(\mathcal{D}_{\mathrm{valid}},K)=\frac{1}{|\mathcal{D}_{\mathrm{valid}}|}\sum_{n\in\mathcal{D}_{\mathrm{valid}}}||\boldsymbol{x}_{n}-\hat{\boldsymbol{x}}_{n}||_{2}^{2}   \tag*{(21.20)}$$

其中 $\hat{x}_n = \text{decode}(\text{encode}(x_n))$ 是 $x_n$ 的重构。

遗憾的是，这一方法并不奏效。事实上，如图21.11a所示，失真度随K单调递减。原因在于，K-means模型是一种退化密度模型，由 $K$ 个位于 $\mu_k$ 中心的“尖峰”组成。随着K增大，我们“覆盖”了输入空间中更多的区域。因此，任意给定输入点更有可能找到一个接近的原型来精确表示它，从而降低重构误差。所以，与监督学习不同，我们无法利用验证集上的重构误差来选取最优的无监督模型。（这一评论也适用于为PCA选择维度，参见第20.1.4节。）

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND许可协议。

---

##### 21.3.7.2 最大化边际似然

一种可行的方法是使用合适的概率模型（如高斯混合模型 (GMM)），我们将在第 21.4.1 节中介绍。然后我们可以利用数据的对数边际似然 (LML) 进行模型选择。

如第 5.2.5.1 节所述，我们可以使用 BIC 分数来近似 LML。由公式 (5.59) 可得：

$$  \mathrm{BIC}(K)=\log p(\mathcal{D}|\hat{\boldsymbol{\theta}}_{k})-\frac{D_{K}}{2}\log(N)   \tag*{(21.21)}$$

其中 $D_K$ 是含有 $K$ 个聚类的模型中的参数数量，$\hat{\theta}_K$ 是最大似然估计 (MLE)。从图 21.11b 可以看出，该曲线呈现典型的 U 形，惩罚项先减小后增大。

这种方法之所以有效，是因为每个聚类都与一个填充输入空间一定体积的高斯分布相关联，而不是一个退化的尖峰。一旦我们有足够多的聚类来覆盖分布的真实模态，贝叶斯奥卡姆剃刀（第 5.2.3 节）就会开始发挥作用，并对过于复杂的模型进行惩罚。

关于混合模型的贝叶斯模型选择的更多讨论，请参见第 21.4.1.3 节。

##### 21.3.7.3 轮廓系数

在本节中，我们介绍一种用于选择 K 均值聚类模型中聚类数量的常见启发式方法。该方法专为球形（而非细长形）的聚类设计。首先，定义实例 $i$ 的轮廓系数为 $sc(i) = (b_i - a_i) / \max(a_i, b_i)$，其中 $a_i$ 是实例 $i$ 到其所在聚类 $k_i = \arg\min_k ||\mu_k - \boldsymbol{x}_i||$ 中其他实例的平均距离，$b_i$ 是实例 $i$ 到其最近邻聚类 $k'_i = \arg\min_{k \neq k_i} ||\mu_k - \boldsymbol{x}_i||$ 中其他实例的平均距离。因此，$a_i$ 衡量了实例 $i$ 所在聚类的紧凑程度，$b_i$ 衡量了聚类间的分离程度。轮廓系数的取值范围为 -1 到 +1。值为 +1 表示实例与自身聚类中的所有成员都很接近，且远离其他聚类；值为 0 表示实例靠近聚类边界；值为 -1 则表示实例可能被分配到了错误的聚类中。我们将所有实例的轮廓系数的均值定义为聚类 $K$ 的轮廓得分。

在图 21.11a 中，我们绘制了图 21.7 中数据的失真率随 $K$ 的变化曲线。如上所述，它随 $K$ 单调递减。曲线在 $K=3$ 处有一个轻微的“拐点”或“肘点”，但这很难检测到。在图 21.11c 中，我们绘制了轮廓得分随 $K$ 的变化曲线。现在我们在 $K=3$ 处看到了一个更明显的峰值，尽管 $K=7$ 似乎也差不多好。图 21.12 展示了一些聚类的比较结果。

观察单个轮廓系数（而不仅仅是平均得分）也能提供有用信息。我们可以将这些系数绘制成轮廓图，如图 21.13 所示，其中每个彩色区域对应一个不同的聚类。垂直虚线表示平均系数。如果某个聚类中有许多点位于该线的左侧，则该聚类很可能质量较低。我们还可以利用轮廓图观察每个聚类的大小，即使数据不是二维的。

##### 21.3.7.4 逐步增加混合成分的数量

另一种搜索最优 $K$ 值的方法是逐步“生长”GMM。我们可以从一个较小的 $K$ 值开始，在每一轮训练之后，考虑分裂具有最大

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_224_127_540_332.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_632_130_948_335.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">K=5</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_222_381_539_580.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_632_381_947_579.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图21.12：针对图21.7中二维数据集的不同K值，K-means算法的Voronoi图。由kmeans_silhouette.ipynb生成。</div>

将最大混合权重对应的簇一分为二，新质心为原始质心的随机扰动，新得分是旧得分的一半。如果新簇的得分太小或方差过窄，则将其移除。我们以这种方式继续，直到达到所需的簇数。详见[FJ02]。

##### 21.3.7.5 稀疏估计方法

另一种方法是选择较大的K值，然后使用某种稀疏性先验或推断方法（如变分贝叶斯）来“剔除”不需要的混合成分。详见本书续作[Mur23]。

### 21.4 使用混合模型的聚类

我们已看到如何使用K-means算法对 $\mathbb{R}^D$ 中的数据向量进行聚类。然而，该方法假设所有簇具有相同的球形形状，这是一个非常严格的假设。此外，K-means假设所有簇都可以用输入空间中的高斯分布来描述，因此它不能应用于离散数据。通过使用混合模型（第3.5节），我们可以克服这两个问题，如下所示。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_222_123_540_334.jpg" alt="图片" width="27%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_629_123_948_334.jpg" alt="图片" width="27%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_223_372_540_581.jpg" alt="图片" width="27%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_630_372_947_582.jpg" alt="图片" width="27%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图 21.13: 在图 21.7 的二维数据集上，对不同的 K 应用 K-means 得到的轮廓图。由 kmeans_silhouette.ipynb 生成。</div>

#### 21.4.1 高斯混合模型

回顾第 3.5.1 节，高斯混合模型 (Gaussian mixture model, GMM) 的形式为：

$$  p(\boldsymbol{x}|\boldsymbol{\theta})=\sum_{k=1}^{K}\pi_{k}\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{k},\boldsymbol{\Sigma}_{k})   \tag*{(21.22)}$$

如果我们知道模型参数 $\boldsymbol{\theta} = (\boldsymbol{\pi}, \{\boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\})$，就可以使用贝叶斯规则计算数据点 $x_n$ 属于簇 $k$ 的责任（后验隶属概率）：

$$  r_{nk}\triangleq p(z_{n}=k|\boldsymbol{x}_{n},\boldsymbol{\theta})=\frac{p(z_{n}=k|\boldsymbol{\theta})p(\boldsymbol{x}_{n}|z_{n}=k,\boldsymbol{\theta})}{\sum_{k^{\prime}=1}^{K}p(z_{n}=k^{\prime}|\boldsymbol{\theta})p(\boldsymbol{x}_{n}|z_{n}=k^{\prime},\boldsymbol{\theta})}   \tag*{(21.23)}$$

根据责任值，我们可以计算最可能的簇分配如下：

$$  \hat{z}_{n}=\arg\max_{k}r_{nk}=\arg\max_{k}\left[\log p(\boldsymbol{x}_{n}|z_{n}=k,\boldsymbol{\theta})+\log p(z_{n}=k|\boldsymbol{\theta})\right]   \tag*{(21.24)}$$

这被称为硬聚类。

##### 21.4.1.1 K-means 是 EM 的一个特例

我们可以使用 EM 算法（第 8.7.3 节）来估计 GMM 的参数。事实证明，K-means 算法是该算法的一个特例，其中我们做了两个近似：

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_225_130_540_328.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_634_124_947_333.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">绑定</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_224_382_541_579.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">绑定</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_633_382_947_581.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_225_626_541_827.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;"> $ (e) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_632_628_947_830.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">球状</div>


<div style="text-align: center;"> $ (f) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_225_876_541_1074.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;"> $ (g) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_635_874_947_1078.jpg" alt="Image" width="27%" /></div>


<div style="text-align: center;">(h)</div>


<div style="text-align: center;">图 21.14：使用具有 K=5 个分量的 GMM 拟合的二维数据。左列：边际分布 p(x)。右列：每个混合分布的可视化，以及数据点硬分配到最可能的簇。(a-b) 全协方差。(c-d) 绑定全协方差。(e-f) 对角协方差。(g-h) 球协方差。颜色编码是任意的。由 gmm_2d.ipynb 生成。</div>


作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND许可协议

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_461_141_719_327.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">图21.15：一些一维数据，叠加了核密度估计。改编自[Mar18]的图6.2。由gmm_identifiability_pymc3.ipynb生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_195_417_969_699.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图21.16：在GMM参数后验推断中标签切换问题的示意图。我们展示了来自4条HMC链的1000个样本的后验边际的KDE估计。(a) 无约束模型。后验是对称的。(b) 约束模型，其中我们添加惩罚项以确保 $\mu_0 < \mu_1$。改编自[Mar18]的图6.6-6.7。由gmm_identifiability_pymc3.ipynb生成。</div>


我们固定所有簇的 $\mathbf{\Sigma}_k = \mathbf{I}$ 和 $\pi_k = 1/K$（因此只需估计均值 $\boldsymbol{\mu}_k$），并通过将软责任替换为硬簇分配来近似E步，即计算 $z_n^* = \arg\max_k r_{nk}$，并设置 $r_{nk} \approx \mathbb{I}(k = z_n^*)$，而不是使用软责任 $r_{nk} = p(z_n = k | \boldsymbol{x}_n, \boldsymbol{\theta})$。利用这一近似，M步中公式(8.165)的加权MLE问题简化为公式(21.14)，从而恢复K-means。

然而，所有簇具有相同球形形状的假设是非常受限的。例如，图21.14展示了对于某些二维数据，使用不同形状协方差矩阵所得到的边际密度和聚类结果。我们看到，对这个特定数据集进行建模需要能够捕获某些簇的非对角协方差（顶行）。

##### 21.4.1.2 不可辨识性与标签切换

注意，在混合模型中我们可以自由排列标签而不改变似然函数。这被称为标签切换问题，是参数不可辨识性的一个例子。

---

如果我们希望对参数进行后验推断（而不仅仅是计算MLE或MAP估计），这可能会引发问题。例如，假设我们使用HMC对图21.15中的数据拟合一个$K=2$个分量的GMM。均值上的后验$p(\mu_1, \mu_2 | \mathcal{D})$如图21.16a所示。我们看到每个分量的边缘后验$p(\mu_k | \mathcal{D})$是双峰的。这反映了数据有两种同样合理的解释：要么$\mu_1 \approx 47$且$\mu_2 \approx 57$，要么相反。

为了打破对称性，我们可以对中心添加顺序约束，使得$\mu_1 < \mu_2$。我们可以通过在违反约束时向目标函数添加惩罚或势函数来实现这一点。更精确地，带惩罚的对数联合分布变为

$$  \ell^{\prime}(\boldsymbol{\theta})=\log p(\mathcal{D}|\boldsymbol{\theta})+\log p(\boldsymbol{\theta})+\phi(\boldsymbol{\mu})   \tag*{(21.25)}$$

其中

$$  \phi(\pmb{\mu})=\begin{cases}-\infty&if\mu_{1}<\mu_{0}\\0&otherwise\end{cases}   \tag*{(21.26)}$$

这产生了预期的效果，如图21.16b所示。

一种更通用的方法是对参数应用变换，以确保可识别性。即，我们从提议分布中采样参数$\boldsymbol{\theta}$，然后对其应用可逆变换$\boldsymbol{\theta}' = f(\boldsymbol{\theta})$，再计算对数联合分布$\log p(\mathcal{D}, \boldsymbol{\theta}')$。为了考虑变量变换（第2.8.3节），我们添加雅可比行列式的对数。在一维排序变换（仅对其输入进行排序）的情况下，雅可比行列式为1，因此对数-行列式-雅可比项消失。

不幸的是，这种方法不能扩展到一维以上的问题，因为没有明显的方法对中心$\mu_k$施加顺序约束。

##### 21.4.1.3 贝叶斯模型选择

一旦我们有可靠的方法确保可识别性，就可以使用第5.2.2节的贝叶斯模型选择技术来选择簇的数量K。在图21.17中，我们展示了将K=3到6个分量的GMM拟合到图21.15数据的结果。我们对均值使用排序变换，并使用HMC进行推断。我们将得到的GMM模型拟合与核密度估计（第16.3节）的拟合进行比较，后者通常会对数据过度平滑。我们看到相当强烈的证据表明存在两个凸起，对应不同的子群体。

我们可以通过计算它们的WAIC得分（广泛适用信息准则，是对对数边际似然的近似）来更定量地比较这些模型（详见[Wat10; Wat13; VGG17]）。结果如图21.18所示。（这种可视化方式由[McE20, p228]提出。）我们看到K=6的模型得分显著高于其他模型，尽管K=5紧随其后。这与图21.17中的图一致。

#### 21.4.2 伯努利混合模型

正如我们在第3.5.2节中讨论的，我们可以使用伯努利混合模型对二值数据进行聚类。模型形式为

$$  p(\boldsymbol{y}|z=k,\boldsymbol{\theta})=\prod_{d=1}^{D}\operatorname{Ber}(y_{d}|\mu_{dk})=\prod_{d=1}^{D}\mu_{dk}^{y_{d}}(1-\mu_{dk})^{1-y_{d}}   \tag*{(21.27)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_389_116_785_407.jpg" alt="图像" width="34%" /></div>


<div style="text-align: center;">图21.17：用不同簇数K的高斯混合模型对图21.15中的数据进行拟合。黑色实线为KDE拟合。蓝色实线为后验均值；淡蓝色线条为后验样本。虚线显示了各个高斯混合分量（通过代入其后验均值参数进行评估）。改编自[Mar18]的图6.8。由gmm_chooseK_pymc3.ipynb生成。</div>


这里 $ \mu_{dk} $ 是位d在簇k中开启的概率。我们可以使用EM、SGD、MCMC等方法拟合该模型。例如，见图3.13，我们对某些二值化的MNIST数字进行聚类。

### 21.5 谱聚类 *

本节讨论一种基于成对相似矩阵特征值分析的聚类方法。它利用特征向量为每个数据点导出特征向量，然后使用基于特征的聚类方法（如K-means（第21.3节））进行聚类。这被称为谱聚类[SM00; Lux07]。

#### 21.5.1 归一化切割

我们首先创建一个加权无向图W，其中每个数据向量是一个节点，i-j边的强度是相似性的度量。通常，我们只将一个节点连接到其最相似的邻居，以确保图是稀疏的，从而加快计算速度。

我们的目标是找到K个相似点的簇。也就是说，我们希望找到一个图划分，将节点划分为 $ S_{1},\ldots,S_{K} $ 个不相交的集合，以最小化某种代价。

我们对代价函数的初步尝试是计算每个簇内节点与簇外节点之间的连接权重：

$$  \mathrm{c u t}(S_{1},\ldots,S_{K})\triangleq\frac{1}{2}\sum_{k=1}^{K}W(S_{k},\overline{S}_{k})   \tag*{(21.28)}$$

其中 $ W(A,B) \triangleq \sum_{i \in A, j \in B} w_{ij} $，$ \overline{S}_k = V \setminus S_k $ 是 $ S_k $ 的补集，而 $ V = \{1, \ldots, N\} $。不幸的是，这个优化问题的解往往只是将一个节点从其余节点中分割出来，因为这最小化了切割的权重。为了避免这种情况，我们可以除以每个集合的大小，以

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_368_118_801_404.jpg" alt="图像" width="37%" /></div>


<div style="text-align: center;">图 21.18：不同 GMM 的 WAIC 分数。空心圆表示每个模型的后验平均 WAIC 分数，黑色线条表示均值的标准误差。实心圆表示每个模型的样本内偏差，即未惩罚的对数似然。虚线垂直线对应最大 WAIC 值。灰色三角形表示该模型与最佳模型相比的 WAIC 分数差异。改编自 [Mar18] 的图 6.10。由 gmm_chooseK_pymc3.tpymb 生成。</div>


得到以下目标函数，称为归一化割：

$$  \mathrm{N c u t}(S_{1},\ldots,S_{K})\triangleq\frac{1}{2}\sum_{k=1}^{K}\frac{\mathrm{c u t}(S_{k},\overline{S}_{k})}{\mathrm{v o l}(S_{k})}   \tag*{(21.29)}$$

其中 $ \text{vol}(A) \triangleq \sum_{i \in A} d_i $ 是集合 $ A $ 的总权重，$ d_i = \sum_{j=1}^N w_{ij} $ 是节点 $ i $ 的加权度。这将图分割成 $ K $ 个簇，使得每个簇内的节点彼此相似，而与其它簇中的节点不同。

我们可以将 Ncut 问题表述为寻找最小化上述目标的二值向量 $ \mathbf{c}_i \in \{0,1\}^N $，其中 $ c_{ik} = 1 $ 当且仅当点 $ i $ 属于簇 $ k $。不幸的是，这是一个 NP 难问题 [WW93]。下面我们讨论该问题的一种基于特征向量方法的连续松弛，它更容易求解。

#### 21.5.2 图拉普拉斯算子的特征向量编码了聚类结构

在 20.4.9.2 节中，我们讨论了图拉普拉斯算子，定义为 $ \mathbf{L} \triangleq \mathbf{D} - \mathbf{W} $，其中 $ \mathbf{W} $ 是图的对称权重矩阵，$ \mathbf{D} = \mathrm{diag}(d_i) $ 是包含每个节点加权度 $ d_i = \sum_j w_{ij} $ 的对角矩阵。为了直观理解 $ \mathbf{L} $ 为何对基于图的聚类有用，我们注意到以下结果。

定理 21.5.1。特征值 0 对应的 $ \mathbf{L} $ 的特征向量由指示向量 $ \mathbf{1}_{S_1}, \ldots, \mathbf{1}_{S_K} $ 张成，其中 $ S_k $ 是图的 $ K $ 个连通分量。

证明。先从 $ K = 1 $ 的情况开始。如果 $ \mathbf{f} $ 是特征值 0 对应的特征向量，那么 $ 0 = \sum_{ij} w_{ij}(f_i - f_j)^2 $。如果两个节点相连，即 $ w_{ij} > 0 $，则必有 $ f_i = f_j $。因此对于图中由一条路径连接的所有顶点，$ \mathbf{f} $ 是常数。现在假设 $ K > 1 $。在此情况下，

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_237_125_508_401.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_643_126_915_402.jpg" alt="图像" width="23%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图21.19：一些数据的聚类结果。(a) K-means。 (b) 谱聚类。由 spectral clustering demo.ipynb 生成。</div>


在这种情况下，L将是分块对角的。与上述类似的论证表明，我们将得到K个指示函数，它们“选出”连通分量。

这提出了以下聚类算法。计算矩阵 $\mathbf{L}$ 的特征向量和特征值，令 $\mathbf{U}$ 为一个 $N \times K$ 的矩阵，其列是 $K$ 个最小特征值对应的特征向量。（计算这种“底部”特征向量的快速方法在[YHJ09]中讨论。）令 $\mathbf{u}_i \in \mathbb{R}^K$ 为 $\mathbf{U}$ 的第 $i$ 行。由于这些 $\mathbf{u}_i$ 将是分段常数，我们可以对它们应用K-means聚类（第21.3节）来恢复连通分量。（注意，向量 $\mathbf{u}_i$ 与第20.4.9节讨论的拉普拉斯特征映射计算的向量相同。）

真实数据可能不会表现出如此清晰的分块结构，但我们可以利用扰动理论的结果证明，一个“受扰动”的拉普拉斯矩阵的特征向量将接近这些理想的指示函数[NJW01]。

在实践中，对图拉普拉斯矩阵进行归一化是很重要的，以考虑某些节点比其他节点连接更紧密的事实。一种方法（由[NJW01]提出）是创建一个对称矩阵

$$  \mathbf{L}_{s y m}\triangleq\mathbf{D}^{-\frac{1}{2}}\mathbf{L}\mathbf{D}^{-\frac{1}{2}}=\mathbf{I}-\mathbf{D}^{-\frac{1}{2}}\mathbf{W}\mathbf{D}^{-\frac{1}{2}}   \tag*{(21.30)}$$

这次，零特征空间由 $\mathbf{D}^{\frac{1}{2}} \mathbf{1}_{S_k}$ 张成。这提出了以下算法：找到 $\mathbf{L}_{sym}$ 的 $K$ 个最小特征向量，将它们堆叠成矩阵 $\mathbf{U}$，通过计算 $t_{ij} = u_{ij} / \sqrt{\left(\sum_k u_{ik}^2\right)}$ 将每一行归一化为单位范数，得到矩阵 $\mathbf{T}$，然后使用K-means对 $\mathbf{T}$ 的行进行聚类，从而推断原始点的划分。

#### 21.5.3 示例

图21.19展示了该方法的实际效果。在图21.19(a)中，我们看到K-means的聚类效果不佳，因为它隐含地假设每个簇对应一个球状高斯分布。接下来我们尝试谱聚类。我们使用高斯核计算一个稠密的相似度矩阵W，

---

$ W_{ij} = \exp(-\frac{1}{2\sigma^2}||\boldsymbol{x}_i - \boldsymbol{x}_j||_2^2) $。然后我们计算归一化拉普拉斯矩阵 $ L_{sym} $ 的前两个特征向量。由此，我们使用 K-means 进行聚类推断，K = 2；结果如图 Figure 21.19(b) 所示。

#### 21.5.4 与其他方法的联系

谱聚类与若干其他无监督学习方法密切相关，下面我们将讨论其中几种。

##### 21.5.4.1 与 kPCA 的联系

谱聚类与核主成分分析（第 20.4.6 节）密切相关。具体来说，kPCA 使用 **W** 的最大特征向量；这些向量等价于 **I** − **W** 的最小特征向量。这与上述方法类似，后者计算 **L** = **D** − **W** 的最小特征向量。详见 [Ben+04a]。在实践中，谱聚类通常比 kPCA 产生更好的结果。

##### 21.5.4.2 与随机游走分析的联系

在实践中，通过计算归一化图拉普拉斯矩阵的特征向量能得到更好的结果。一种归一化方法由 [SM00; Mei01] 使用，定义为

$$  \mathbf{L}_{r w}\triangleq\mathbf{D}^{-1}\mathbf{L}=\mathbf{I}-\mathbf{D}^{-1}\mathbf{W}   \tag*{(21.31)}$$

可以证明，对于 $ \mathbf{L}_{rw} $，0 的特征空间仍由指示向量 $ \mathbf{1}_{S_k} $ 张成 [Lux07]，因此我们可以直接在 $ K $ 个最小特征向量 $ \mathbf{U} $ 上进行聚类。

这种方法与图上的随机游走之间存在有趣的联系。首先注意 $ \mathbf{P} = \mathbf{D}^{-1} \mathbf{W} = \mathbf{I} - \mathbf{L}_{rw} $ 是一个随机矩阵，其中 $ p_{ij} = w_{ij}/d_i $ 可以解释为从 i 到 j 的转移概率。如果图是连通且非二分的，则存在唯一的平稳分布 $ \boldsymbol{\pi} = (\boldsymbol{\pi}_1, \ldots, \boldsymbol{\pi}_N) $，其中 $ \pi_i = d_i / \text{vol}(V) $，$ \text{vol}(V) = \sum_i d_i $ 是所有节点度之和。此外，可以证明，对于大小为 2 的分割，

$$  \mathrm{N c u t}(S,\overline{S})=p(\overline{S}|S)+p(S|\overline{S})   \tag*{(21.32)}$$

这意味着我们寻找一个分割，使得随机游走花费更多时间在相似点之间转移，并且很少从 $S$ 转移到 $\overline{S}$ 或反之。这一分析可以扩展到 $K > 2$ 的情况；详见 [Mei01]。

### 21.6 双聚类 *

在某些情况下，我们有一个数据矩阵 $ \mathbf{X} \in \mathbb{R}^{N_r \times N_c} $，希望同时对行和列进行聚类；这称为双聚类或共聚类。这在生物信息学中广泛应用，其中行通常代表基因，列代表条件。它也可用于协同过滤，其中行代表用户，列代表电影。

已经提出了多种针对双聚类的特定方法；综述见 [MO04]。在第 21.6.1 节中，我们介绍一个简单的概率生成模型，其中为每一行分配一个潜在类别 ID，为每一列分配一个不同的潜在类别 ID。在第 21.6.2 节中，我们将其扩展到每个行可以属于多个类别的情况，取决于我们选择哪些特征组（列）来定义不同的对象组（行）。

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_117_549_285.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_559_122_943_286.jpg" alt="图像" width="33%" /></div>


<div style="text-align: center;">图21.20：双聚类示意图。图中展示了12个生物簇中的5个，以及33个特征簇中的6个。原始数据矩阵按发现的簇进行划分显示。摘自 $ [Kem+06] $ 的图3。经Charles Kemp许可使用。</div>


#### 21.6.1 基础双聚类

在此，我们介绍一种基于 $ [Kem+06] $ 的简单概率生成模型用于双聚类（另见 $ [SMM03] $ 的类似方法）。其思想是为每一行和每一列关联一个潜在指示变量 $ u_i \in \{1, \ldots, N_u\} $ 和 $ v_j \in \{1, \ldots, N_v\} $，其中 $ N_u $ 是行簇数量，$ N_v $ 是列簇数量。然后使用以下生成模型：

$$  p(\mathbf{U})=\prod_{i=1}^{N_{r}}\mathrm{Unif}(u_{i}|\{1,\cdots,N_{u}\})   \tag*{(21.33)}$$

$$  p(\mathbf{V})=\prod_{j=1}^{N_{c}}\mathrm{Cat}(v_{j}|\{1,\ldots,N_{v}\})   \tag*{(21.34)}$$

$$  p(\mathbf{X}|\mathbf{U},\mathbf{V},\boldsymbol{\theta})=\prod_{i=1}^{N_{r}}\prod_{j=1}^{N_{c}}p(X_{i j}|\boldsymbol{\theta}_{u_{i},v_{j}})   \tag*{(21.35)}$$

其中 $ \theta_{a,b} $ 是行簇 a 和列簇 b 的参数。

图21.20展示了一个简单示例。数据形式为 $ X_{ij} = 1 $ 当且仅当动物 i 拥有特征 j，其中 $ i = 1 : 50 $，$ j = 1 : 85 $。这些动物代表鲸、熊、马等。特征代表栖息地属性（丛林、树木、沿海）、解剖学属性（有牙齿、四足行走）或行为属性（游泳、吃肉）等。该方法发现了12个动物簇和33个特征簇（[Kem+06] 使用贝叶斯非参数方法推断簇数量）。例如，簇 O2 为 {羚羊、马、长颈鹿、斑马、鹿}，其由特征簇 F2 = {蹄、长颈、角} 和 F6 = {行走、四足行走、陆地} 刻画；而簇 O4 为 {河马、大象、犀牛}，其由特征簇 F4 = {球状体型、行动缓慢、不活跃} 和 F6 刻画。

#### 21.6.2 嵌套分区模型（Crosscat）

基础双聚类（第21.6.1节）的问题在于每个对象（行）只能属于一个簇。直观上，一个对象可以具有多重角色，并且可以根据所使用的特征子集分配到不同的簇。例如，在动物数据集中，我们可能希望基于解剖学特征（例如，哺乳动物是温血的，爬行动物是冷血的）对动物进行分组，

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_207_119_555_235.jpg" alt="图像" width="30%" /></div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>1.2</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>1.1</td><td style='text-align: center; word-wrap: break-word;'>2.2</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>2.2</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>3.2</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td><td style='text-align: center; word-wrap: break-word;'>1.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>2.1</td><td style='text-align: center; word-wrap: break-word;'>3.2</td><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'>2.3</td><td style='text-align: center; word-wrap: break-word;'>2.3</td></tr></table>

<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 21.21: (a) 双聚类示例。每一行被分配到一个唯一的簇，每一列也被分配到一个唯一的簇。(b) 使用嵌套划分模型的多聚类示例。行可以属于不同的簇，具体取决于我们所考察的列特征的子集。</div>


而不是基于行为特征（例如，捕食者与猎物）。

现在我们提出一个能够捕捉这一现象的模型。我们用一个例子来说明该方法。假设我们有一个 $ 6 \times 6 $ 矩阵，有 $ N_u = 2 $ 个行簇和 $ N_v = 3 $ 个列簇。进一步，假设潜在的列分配如下：$ \boldsymbol{v} = [1, 1, 2, 3, 3, 3] $。这意味着我们将列 1 和 2 归入组 1，列 3 归入组 2，列 4 到 6 归入组 3。对于被聚类到组 1 的列，我们对行进行如下聚类：$ \boldsymbol{u}_{:,1} = [1, 1, 1, 2, 2, 2] $；对于被聚类到组 2 的列，我们对行进行如下聚类：$ \boldsymbol{u}_{:,2} = [1, 1, 2, 2, 2, 2] $；对于被聚类到组 3 的列，我们对行进行如下聚类：$ \boldsymbol{u}_{:,3} = [1, 1, 1, 1, 1, 2] $。得到的划分如图 21.21(b) 所示。我们看到，行的聚类取决于我们选择关注哪一组列。

形式上，我们可以将模型定义如下：

$$  p(\mathbf{U})=\prod_{i=1}^{N_{r}}\prod_{l=1}^{N_{v}}\mathrm{Unif}(u_{il}|\{1,\ldots,N_{u}\})   \tag*{(21.36)}$$

$$  p(\mathbf{V})=\prod_{j=1}^{N_{c}}\mathrm{Unif}(v_{j}|\{1,\ldots,N_{v}\})   \tag*{(21.37)}$$

$$  p(\mathbf{Z}|\mathbf{U},\mathbf{V})=\prod_{i=1}^{N_{r}}\prod_{j=1}^{N_{c}}\mathbb{I}\left(Z_{ij}=(u_{i,v_{j}},v_{j})\right)   \tag*{(21.38)}$$

$$  p(\mathbf{X}|\mathbf{Z},\boldsymbol{\theta})=\prod_{i=1}^{N_{r}}\prod_{j=1}^{N_{c}}p(X_{i j}|\boldsymbol{\theta}_{z_{i j}})   \tag*{(21.39)}$$

其中 $ \theta_{k,l} $ 是共簇 $ k \in \{1, \ldots, N_u\} $ 和 $ l \in \{1, \ldots, N_v\} $ 的参数。

该模型由 [Sha+06; Man+16] 独立提出，他们称之为 crosscat（交叉分类）；[Gua+10; CFD10] 称之为 multi-clust；[RG11] 称之为嵌套划分（nested partitioning）。在这些文献中，作者们都建议使用狄利克雷过程（Dirichlet processes）以避免估计簇数的问题。这里为符号简洁起见，我们假设簇数已知，并显式地给出参数。

图 21.22 展示了将该模型应用于包含 22 种动物和 106 个特征的二值数据的结果。该图显示了（近似）最大后验（MAP）划分。列的第一个划分包含分类学特征，例如“有骨骼”、“是温血动物”、“产卵”等。这划分了

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_198_118_960_471.jpg" alt="图片" width="66%" /></div>

<div style="text-align: center;">图 21.22：将交叉分类系统应用于动物（行）按特征（列）的二元数据矩阵时产生的 MAP 估计。详见正文。摘自 [Sha+06] 的图 7。经 Vikash Mansingkha 许可使用。</div>

动物被划分为鸟类、爬行类/两栖类、哺乳类和无脊椎动物。列的第二个分区包含被视为噪声的特征，没有明显的结构（除了标记为“青蛙”的单一类别行）。列的第三个分区包含生态特征，如“危险的”、“食肉的”、“生活在水里”等。这将动物划分为猎物、陆地捕食者、海洋捕食者和空中捕食者。因此，每只动物（行）根据所考虑的特征集不同，可以属于不同的簇。

---

## 22 推荐系统

推荐系统是根据各种信息（例如用户过去的观看/购买行为，比如他们对哪些电影评价高或低，点击了哪些广告），以及可选的“辅助信息”（如用户的人口统计学信息，或物品内容的信息，如标题、类型或价格），向用户推荐物品（如电影、书籍、广告）的系统。这类系统被众多互联网公司广泛使用，例如 Facebook、Amazon、Netflix、Google 等。在本章中，我们将简要介绍这一主题。更多细节可参见例如 [DKK12; Pat12; Yan+14; AC16; Agg16; Zha+19b]。

### 22.1 显式反馈

在本节中，我们考虑最简单的场景，即用户以评分的形式向系统提供显式反馈，例如 +1 或 -1（表示喜欢/不喜欢），或 1 到 5 分。令 $Y_{ui} \in \mathbb{R}$ 表示用户 u 对物品 i 的评分。我们可以将其表示为一个 $M \times N$ 矩阵，其中 M 是用户数量，N 是物品数量。通常这个矩阵会非常大但极其稀疏，因为大多数用户不会对大多数物品提供任何反馈。示例见图 22.1(a)。我们也可以将这个稀疏矩阵视为一个二分图，其中 u-i 边的权重为 $Y_{ui}$。这反映了我们处理的是关系型数据的事实，即 u 和 i 的值本身没有内在意义（它们只是任意索引），重要的是 u 和 i 之间的连接关系。

如果 $Y_{ui}$ 缺失，可能是因为用户 u 尚未与物品 i 交互，也可能是因为用户知道自己不会喜欢该物品，因此选择不参与。在前一种情况下，部分数据是随机缺失的；在后一种情况下，缺失性携带了关于 $Y_{ui}$ 真实值的信息。（关于这一点的进一步讨论，可参见例如 [Mar+11]。）为简单起见，我们假设数据是随机缺失的。

#### 22.1.1 数据集

电影流媒体公司 Netflix 提供了一个著名的显式评分矩阵示例。2006年，他们发布了一个大型数据集，包含来自 480,189 位用户对 17,770 部电影的 100,480,507 条评分（评分范围为 1 到 5）。尽管训练集规模很大，但评分矩阵仍然有 99% 是稀疏的（未知）。与此同时，他们还设立了 100 万美元的奖金，即 Netflix Prize，奖励给那些能够比他们现有系统更准确地预测一组测试（用户，物品）对真实评分的团队。该奖项于 2009 年 9 月 21 日由一个名为“BellKor's Pragmatic Chaos”的团队获得。他们使用了多种方法的集成，具体描述见下文。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_272_134_889_384.jpg" alt="图片" width="53%" /></div>

<div style="text-align: center;">图 22.1：关系数据集的示例，表示为稀疏矩阵（左）或稀疏二分图（右）。空单元格（缺失边）对应的值未知。第 3 行和第 4 行彼此相似，表明用户 3 和用户 4 可能有相似的偏好，因此我们可以使用用户 3 的数据来预测用户 4 的偏好。然而，用户 1 的偏好似乎相当不同，似乎对所有项目都给出低评分。对于用户 2，我们观察到的数据很少，因此很难做出可靠的预测。</div>

[Kor09; BK07; FHK12]。然而，他们集成方法中的一个关键组成部分是第 22.1.3 节中描述的方法。

不幸的是，出于隐私考虑，Netflix 数据已不再可用。幸运的是，明尼苏达大学的 MovieLens 小组发布了一个匿名的公共电影评分数据集，评分范围为 1-5 分，可用于研究 [HK15]。还有各种其他公开的显式评分数据集，例如来自 [Gol+01] 的 Jester 笑话数据集和来自 [Zie+05] 的 BookCrossing 数据集。

#### 22.1.2 协同过滤

推荐问题最初的解决方法称为协同过滤 [Gol+92]。其思想是，用户通过与其他用户共享评分来协作推荐项目；这样，如果用户 u 想知道他们是否与项目 i 交互，可以查看其他用户 u' 对 i 的评分，并取加权平均值：

$$ \hat{Y}_{ui}=\sum_{u^{\prime}:Y_{u^{\prime},i}\neq?}\mathrm{sim}(u,u^{\prime})Y_{u^{\prime},i}   \tag*{(22.1)}$$

其中，如果条目未知，我们假设 $ Y_{u',i} = ? $。传统方法通过比较集合 $ S_u = \{Y_{u,i} \neq ? : i \in \mathcal{I}\} $ 和 $ S_{u'} = \{Y_{u',i} \neq ? : i \in \mathcal{I}\} $ 来衡量两个用户的相似度，其中 $ \mathcal{I} $ 是项目集合。然而，这可能会受到数据稀疏性的影响。在第 22.1.3 节中，我们讨论了一种基于学习每个项目和每个用户的密集嵌入向量的方法，从而可以在低维特征空间中计算相似度。

---

#### 22.1.3 矩阵分解

我们可以将推荐问题视为一个矩阵补全问题，即希望预测出 $\mathbf{Y}$ 的所有缺失项。该问题可表述为如下优化问题：

$$  \mathcal{L}(\mathbf{Z})=\sum_{i j:Y_{i j}\neq?}(Z_{i j}-Y_{i j})^{2}=||\mathbf{Z}-\mathbf{Y}||_{F}^{2}   \tag*{(22.2)}$$

然而，这是一个欠定问题，因为存在无数种填补 $\mathbf{Z}$ 中缺失项的方式。

我们需要添加一些约束。假设 $\mathbf{Y}$ 是低秩的，那么可以将其表示为 $\mathbf{Z} = \mathbf{U} \mathbf{V}^{\top} \approx \mathbf{Y}$ 的形式，其中 $\mathbf{U}$ 是 $M \times K$ 矩阵，$\mathbf{V}$ 是 $N \times K$ 矩阵，$K$ 是矩阵的秩，$M$ 是用户数，$N$ 是物品数。这对应如下形式的预测：

$$  \hat{y}_{u i}=\boldsymbol{u}_{u}^{\mathsf{T}}\boldsymbol{v}_{i}   \tag*{(22.3)}$$

这种方法称为矩阵分解。

如果我们观测到了所有 $Y_{ij}$ 项，则可以使用SVD（奇异值分解，见第7.5节）找到最优的 $\mathbf{Z}$。然而，当 $\mathbf{Y}$ 存在缺失项时，对应的目标函数不再是凸函数，且不存在唯一最优解 [SJ03]。我们可以使用交替最小二乘法（ALS）来拟合该模型，即先固定 $\mathbf{V}$ 估计 $\mathbf{U}$，再固定 $\mathbf{U}$ 估计 $\mathbf{V}$（具体细节可参见 [KBV09]）。另一种方法是直接使用SGD（随机梯度下降）。

实践中，添加用户特定和物品特定的偏置项非常重要，为此可以写成：

$$  \hat{y}_{u i}=\mu+b_{u}+c_{i}+\boldsymbol{u}_{u}^{\mathsf{T}}\boldsymbol{v}_{i}   \tag*{(22.4)}$$

这样能够捕捉到某些用户可能总是倾向于打低分而另一些用户可能打高分的事实；此外，一些物品（例如非常受欢迎的电影）可能拥有异常高的评分。

此外，我们可以对参数添加 $\ell_{2}$ 正则化，得到目标函数：

$$  \mathcal{L}(\boldsymbol{\theta})=\sum_{i j:Y_{i j}\neq?}(y_{i j}-\hat{y}_{i j})^{2}+\lambda(b_{u}^{2}+c_{i}^{2}+||\boldsymbol{u}_{u}||^{2}+||\boldsymbol{v}_{i}||^{2})   \tag*{(22.5)}$$

我们可以使用SGD来优化该目标函数：从观测值集合中随机采样一个 $(u,i)$ 项，并执行以下更新：

$$  b_{u}=b_{u}+\eta(e_{u i}-\lambda b_{u})   \tag*{(22.6)}$$

$$  c_{i}=c_{i}+\eta(e_{ui}-\lambda c_{i})   \tag*{(22.7)}$$

$$  \boldsymbol{u}_{u}=\boldsymbol{u}_{u}+\eta(e_{u i}\boldsymbol{v}_{i}-\lambda\boldsymbol{u}_{u})   \tag*{(22.8)}$$

$$  \boldsymbol{v}_{i}=\boldsymbol{v}_{i}+\eta(e_{u i}\boldsymbol{u}_{u}-\lambda\boldsymbol{v}_{i})   \tag*{(22.9)}$$

其中 $e_{ui} = y_{ui} - \hat{y}_{ui}$ 是误差项，$\eta \geq 0$ 是学习率。该方法由 Simon Funk 首次提出，他是 Netflix 竞赛早期表现优异的参赛者之一。$^{1}$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_349_119_814_478.jpg" alt="图像" width="40%" /></div>


<div style="text-align: center;">图22.2：从Netflix挑战数据中估计的前两个潜在电影因子的可视化。每部电影$j$被绘制在$\mathbf{v}_j$指定的位置。详情见正文。改编自[KBV09]的图3。经Yehuda Koren许可使用。</div>


##### 22.1.3.1 概率矩阵分解 (PMF)

我们可以通过定义

$$  p(y_{ui}=y)=\mathcal{N}(y|\mu+b_{u}+c_{i}+\boldsymbol{u}_{u}^{\top}\boldsymbol{v}_{i},\sigma^{2})   \tag*{(22.10)}$$

将矩阵分解转化为概率模型。这被称为**概率矩阵分解** (PMF) [SM08]。该模型的负对数似然等价于式(22.2)中的矩阵分解目标函数。然而，概率视角使我们更容易推广模型。例如，我们可以利用泊松或负二项似然（参见e.g., [GOF18]）来捕捉评分是整数（通常多为0）而非实数的事实。这与指数族PCA（第20.2.7节）类似，区别在于我们将行和列对称看待。

##### 22.1.3.2 示例：Netflix

假设我们使用 $K = 2$ 个潜在因子对Netflix数据集应用PMF。图22.2可视化了几部电影的学习嵌入向量$\boldsymbol{u}_i$。图的左侧是低俗幽默与恐怖电影（《半熟判官》、《弗莱迪大战杰森》），右侧是更严肃的剧情片（《苏菲的选择》、《月色撩人》）。顶部是广受好评的独立电影（《糊涂的爱》、《心碎度蜜月》），底部则是主流好莱坞大片（《绝世天劫》、《落跑新娘》）。《绿野仙踪》恰好位于这些轴线的中心，因为从某种意义上说它是一部“平均电影”。

用户被嵌入到与电影相同的空间中。然后，我们可以利用潜在嵌入空间中的邻近性来预测任意用户-视频对的评分。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_238_125_528_402.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_644_122_938_401.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 22.3: (a) MovieLens-1M 数据集中观测评分矩阵的一个片段。(b) 使用具有 50 个潜在分量的 SVD 得到的预测结果。由 matrix_factorization_recommender.ipynb 生成。</div>


##### 22.1.3.3 示例：MovieLens

现在，我们将 PMF 应用于包含 6040 个用户、3706 部电影和 1,000,209 个评分的 MovieLens-1M 数据集。我们使用 K = 50 个因子。为简化起见，我们使用 SVD 对稠密评分矩阵进行拟合，其中缺失值替换为 0。（这只是一个简单的近似，以保持演示代码的简洁性。）在图 22.3 中，我们展示了真实评分矩阵和预测评分矩阵的一个片段。（我们将预测结果截断在 [1,5] 范围内。）我们看到该模型并不特别准确，但确实捕捉到了数据中的某些结构。

此外，模型在定性上似乎表现合理。例如，在图 22.4 中，我们展示了给定用户评分最高的前 10 部电影，以及模型预测该用户尚未看过的前 10 部电影。该模型似乎“捕捉”到了用户的潜在偏好。例如，我们看到许多预测的电影属于动作片或黑色电影，而这两种类型都出现在用户自己的前 10 列表中，尽管模型训练过程中并未使用明确的类型信息。

#### 22.1.4 自编码器

矩阵分解是一种（双）线性模型。利用自编码器，我们可以构建非线性版本。设 $ \mathbf{y}_{:,i} \in \mathbb{R}^M $ 为评分矩阵的第 $ i $ 列，其中未知评分设为 0。我们可以使用如下形式的自编码器来预测该评分向量：

$$  f(\boldsymbol{y}_{:,i};\boldsymbol{\theta})=\mathbf{W}^{\top}\boldsymbol{\varphi}(\mathbf{V}\boldsymbol{y}_{:,i}+\boldsymbol{\mu})+\boldsymbol{b}   \tag*{(22.11)}$$

其中 $ \mathbf{V} \in \mathbb{R}^{K \times M} $ 将评分映射到嵌入空间，$ \mathbf{W} \in \mathbb{R}^{K \times M} $ 将嵌入空间映射到评分分布，$ \boldsymbol{\mu} \in \mathbb{R}^K $ 是隐藏单元的偏置，$ \mathbf{b} \in \mathbb{R}^M $ 是输出单元的偏置。这被称为 AutoRec 模型 [Sed+15] 的（基于项目的）版本。该模型有 $ 2MK + M + K $ 个参数。还有一个基于用户的版本，可以类似地推导，其参数数量为 $ 2NK + N + K $。（在 MovieLens 和 Netflix 上，作者发现基于项目的方法效果更好。）

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>电影ID</td><td style='text-align: center; word-wrap: break-word;'>标题</td><td style='text-align: center; word-wrap: break-word;'>类型</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>36</td><td style='text-align: center; word-wrap: break-word;'>858</td><td style='text-align: center; word-wrap: break-word;'>Godfather, The (1972)</td><td style='text-align: center; word-wrap: break-word;'>Action|Crime|Drama</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>35</td><td style='text-align: center; word-wrap: break-word;'>1387</td><td style='text-align: center; word-wrap: break-word;'>Jaws (1975)</td><td style='text-align: center; word-wrap: break-word;'>Action|Horror</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>65</td><td style='text-align: center; word-wrap: break-word;'>2028</td><td style='text-align: center; word-wrap: break-word;'>Saving Private Ryan (1998)</td><td style='text-align: center; word-wrap: break-word;'>Action|Drama|War</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>63</td><td style='text-align: center; word-wrap: break-word;'>1221</td><td style='text-align: center; word-wrap: break-word;'>Godfather: Part II, The (1974)</td><td style='text-align: center; word-wrap: break-word;'>Action|Crime|Drama</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11</td><td style='text-align: center; word-wrap: break-word;'>913</td><td style='text-align: center; word-wrap: break-word;'>Maltese Falcon, The (1941)</td><td style='text-align: center; word-wrap: break-word;'>Film-Noir|Mystery</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>3417</td><td style='text-align: center; word-wrap: break-word;'>Crimson Pirate, The (1952)</td><td style='text-align: center; word-wrap: break-word;'>Adventure|Comedy|Sci-Fi</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>34</td><td style='text-align: center; word-wrap: break-word;'>2186</td><td style='text-align: center; word-wrap: break-word;'>Strangers on a Train (1951)</td><td style='text-align: center; word-wrap: break-word;'>Film-Noir|Thriller</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>2791</td><td style='text-align: center; word-wrap: break-word;'>Airplane! (1980)</td><td style='text-align: center; word-wrap: break-word;'>Comedy</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>31</td><td style='text-align: center; word-wrap: break-word;'>1188</td><td style='text-align: center; word-wrap: break-word;'>Strictly Ballroom (1992)</td><td style='text-align: center; word-wrap: break-word;'>Comedy|Romance</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>28</td><td style='text-align: center; word-wrap: break-word;'>1304</td><td style='text-align: center; word-wrap: break-word;'>Butch Cassidy and the Sundance Kid (1969)</td><td style='text-align: center; word-wrap: break-word;'>Action|Comedy|Western</td></tr></table>

<div style="text-align: center;">(a)</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>电影ID</td><td style='text-align: center; word-wrap: break-word;'>标题</td><td style='text-align: center; word-wrap: break-word;'>类型</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>516</td><td style='text-align: center; word-wrap: break-word;'>527</td><td style='text-align: center; word-wrap: break-word;'>Schindler&#x27;s List (1993)</td><td style='text-align: center; word-wrap: break-word;'>Drama|War</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1848</td><td style='text-align: center; word-wrap: break-word;'>1953</td><td style='text-align: center; word-wrap: break-word;'>French Connection, The (1971)</td><td style='text-align: center; word-wrap: break-word;'>Action|Crime|Drama|Thriller</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>596</td><td style='text-align: center; word-wrap: break-word;'>608</td><td style='text-align: center; word-wrap: break-word;'>Fargo (1996)</td><td style='text-align: center; word-wrap: break-word;'>Crime|Drama|Thriller</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1235</td><td style='text-align: center; word-wrap: break-word;'>1284</td><td style='text-align: center; word-wrap: break-word;'>Big Sleep, The (1946)</td><td style='text-align: center; word-wrap: break-word;'>Film-Noir|Mystery</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2085</td><td style='text-align: center; word-wrap: break-word;'>2194</td><td style='text-align: center; word-wrap: break-word;'>Untouchables, The (1987)</td><td style='text-align: center; word-wrap: break-word;'>Action|Crime|Drama</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1188</td><td style='text-align: center; word-wrap: break-word;'>1230</td><td style='text-align: center; word-wrap: break-word;'>Annie Hall (1977)</td><td style='text-align: center; word-wrap: break-word;'>Comedy|Romance</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1198</td><td style='text-align: center; word-wrap: break-word;'>1242</td><td style='text-align: center; word-wrap: break-word;'>Glory (1989)</td><td style='text-align: center; word-wrap: break-word;'>Action|Drama|War</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>897</td><td style='text-align: center; word-wrap: break-word;'>922</td><td style='text-align: center; word-wrap: break-word;'>Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)</td><td style='text-align: center; word-wrap: break-word;'>Film-Noir</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1849</td><td style='text-align: center; word-wrap: break-word;'>1954</td><td style='text-align: center; word-wrap: break-word;'>Rocky (1976)</td><td style='text-align: center; word-wrap: break-word;'>Action|Drama</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>581</td><td style='text-align: center; word-wrap: break-word;'>593</td><td style='text-align: center; word-wrap: break-word;'>Silence of the Lambs, The (1991)</td><td style='text-align: center; word-wrap: break-word;'>Drama|Thriller</td></tr></table>

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 22.4：(a) 用户“837”已给予高评分的位列前 10 的电影（来自 69 部电影的列表）。(b) 算法给出的位列前 10 的预测（来自 3637 部电影的列表）。由 matrix_factorization_recommender.ipynb 生成。</div>


我们可以通过仅更新与 $ \mathbf{y}_{:,i} $ 观测条目相关的参数来拟合该模型。此外，我们可以在权重矩阵上添加一个 $ \ell_{2} $ 正则化项，从而得到如下目标函数：

$$  \mathcal{L}(\boldsymbol{\theta})=\sum_{i=1}^{N}\sum_{u:y_{ui}\neq?}(y_{u,i}-f(\boldsymbol{y}_{:,i};\boldsymbol{\theta})_{u})^{2}+\frac{\lambda}{2}(||\mathbf{W}||_{F}^{2}+||\mathbf{V}||_{F}^{2})   \tag*{(22.12)}$$

尽管该方法简单，但作者发现它优于诸如受限玻尔兹曼机（RBMs，[SMH07]）和局部低秩矩阵等更复杂的方法。

---

近似（LLORMA，[Lee+13]）。

### 22.2 隐式反馈

到目前为止，我们假设用户对自己交互过的每个项目都给出了明确的评分。这是一个非常严格的假设。更一般地，我们希望从用户仅通过与系统交互而提供的**隐式反馈**中学习。例如，我们可以将用户u观看的电影列表视为正样本，而将所有其他电影视为负样本。这样我们就得到了一个稀疏的、仅有正样本的评分矩阵。

或者，我们可以将用户观看了电影i但未观看电影j这一事实视为他们偏好i胜过j的隐式信号。由此产生的数据可以表示为一组形如$ y_n = (u, i, j) $的元组，其中$(u, i)$是正对，$(u, j)$是负对（或未标注对）。

#### 22.2.1 贝叶斯个性化排序

为了对形如$(u,i,j)$的数据拟合模型，我们需要使用**排序损失**，使得模型为用户u将i排在j之前。一种简单的方法是使用如下形式的**伯努利**模型：

$$  p(y_{n}=(u,i,j)|\boldsymbol{\theta})=\sigma(f(u,i;\boldsymbol{\theta})-f(u,j;\boldsymbol{\theta}))   \tag*{(22.13)}$$

如果将其与$\theta$的高斯先验结合，我们得到以下最大后验估计问题：

$$  \mathcal{L}(\boldsymbol{\theta})=\sum_{(u,i,j)\in\mathcal{D}}\log\sigma(f(u,i;\boldsymbol{\theta})-f(u,j;\boldsymbol{\theta}))-\lambda||\boldsymbol{\theta}||^{2}   \tag*{(22.14)}$$

其中$\mathcal{D} = \{(u, i, j) : i \in \mathcal{I}_u^+, j \in \mathcal{I} \setminus \mathcal{I}_u^+\}$，$\mathcal{I}_u^+$是用户$u$选择过的所有项目集合，$\mathcal{I} \setminus \mathcal{I}_u^+$是所有其他项目（用户可能不喜欢，或仅仅是没看到）。这被称为**贝叶斯个性化排序**（BPR，[Ren+09]）。

让我们考虑来自[Zha+20，第16.5节]的这个例子。总共有4个项目，$\mathcal{I} = \{i_1, i_2, i_3, i_4\}$，用户$u$选择交互的项目是$\mathcal{I}_u^+ = \{i_2, i_3\}$。在这种情况下，用户$u$的隐式项目-项目偏好矩阵形式为：

$$  \mathbf{Y}_{u}=\begin{pmatrix}\cdot&+&+&?\\-\ &.\ &?\ &-\\-\ &?\ &.\ &-\\?\ &+\ &+\ &.\end{pmatrix}   \tag*{(22.15)}$$

其中$Y_{u,i,i'} = +$表示用户$u$偏好$i'$胜过$i$，$Y_{u,i,i'} = -$表示用户$u$偏好$i$胜过$i'$，而$Y_{u,i,i'} = ?$表示我们无法判断用户的偏好。例如，观察第二列，我们看到该用户将$i_2$排在$i_1$和$i_4$之上，因为他们选择了$i_2$但未选择$i_1$或$i_4$；然而，我们无法判断他们是否偏好$i_2$胜过$i_3$，反之亦然。

当可能项目的集合很大时，$\mathcal{I} \setminus \mathcal{I}_u^+$中的负样本数量可能非常大。幸运的是，我们可以通过对负样本进行子采样来近似损失。

需要注意的是，上述对数损失的替代方案是使用**铰链损失**，类似于SVM中使用的方法（第17.3节）。其形式为：

$$  \mathcal{L}(y_{n}=(u,i,j),f)=\max\left(m-(f(u,i)-f(u,j)),0\right)=\max\left(m-f(u,i)+f(u,j),0\right)   \tag*{(22.16)}$$

其中$m \geq 0$是安全边际。这试图确保负样本项目j的得分永远不比正样本项目i高超过m。

作者：Kevin P. Murphy。（C）MIT出版社。CC-BY-NC-ND许可证。

---

#### 22.2.2 因子分解机

第 22.1.4 节的 AutoRec 方法是非线性的，但对用户和物品的处理是非对称的。本节我们将讨论一种更具对称性的判别式建模方法。首先介绍线性版本。其基本思想是利用下式预测任意给定用户-物品对 $ \boldsymbol{x} = [\text{one-hot}(u), \text{one-hot}(i)] $ 的输出（如评分）：

$$  f(\boldsymbol{x})=\mu+\sum_{i=1}^{D}w_{i}x_{i}+\sum_{i=1}^{D}\sum_{j=i+1}^{D}(\boldsymbol{v}_{i}^{\mathsf{T}}\boldsymbol{v}_{j})x_{i}x_{j}   \tag*{(22.17)}$$

其中 $ \boldsymbol{x} \in \mathbb{R}^D $，$ D = (M + N) $ 为输入数量，$ \mathbf{V} \in \mathbb{R}^{D \times K} $ 为权重矩阵，$ \boldsymbol{w} \in \mathbb{R}^D $ 为权重向量，$ \mu \in \mathbb{R} $ 为全局偏移。该模型称为**因子分解机**（Factorization Machine, FM）[Ren12]。

项 $ (v_i^\top v_j)x_i x_j $ 衡量输入中特征 $ i $ 与 $ j $ 之间的交互。这推广了式 (22.4) 的矩阵分解模型，因为它能处理输入 $ x $ 中除用户和物品之外的其他类型信息，我们将在第 22.3 节中讨论这一点。

计算式 (22.17) 需要 $ O(KD^{2}) $ 时间，因为它考虑了每一用户与每一物品之间所有可能的成对交互。幸运的是，我们可以将其重写，从而在 $ O(KD) $ 时间内完成计算，如下所示：

$$  \sum_{i=1}^{D}\sum_{j=i+1}^{D}(\boldsymbol{v}_{i}^{\mathsf{T}}\boldsymbol{v}_{j})x_{i}x_{j}=\frac{1}{2}\sum_{i=1}^{D}\sum_{j=1}^{D}(\boldsymbol{v}_{i}^{\mathsf{T}}\boldsymbol{v}_{j})x_{i}x_{j}-\frac{1}{2}\sum_{i=1}^{D}(\boldsymbol{v}_{i}^{\mathsf{T}}\boldsymbol{v}_{i})x_{i}x_{i}   \tag*{(22.18)}$$

$$  =-\frac{1}{2}\left(\sum_{i=1}^{D}\sum_{j=1}^{D}\sum_{k=1}^{K}v_{ik}v_{jk}x_{i}x_{j}-\sum_{i=1}^{D}\sum_{k=1}^{K}v_{ik}v_{ik}x_{i}x_{i}\right)   \tag*{(22.19)}$$

 $$ =-\frac{1}{2}\sum_{k=1}^{K}\left(\left(\sum_{i=1}^{D}v_{ik}x_{i}\right)^{2}-\sum_{i=1}^{D}v_{ik}^{2}x_{i}^{2}\right) $$ 

对于稀疏向量，整体复杂度与非零分量数量呈线性关系。因此，如果我们使用用户和物品 ID 的独热编码，复杂度仅为 $ O(K) $，这与原始矩阵分解目标函数式 (22.4) 类似。

我们可以拟合该模型以最小化任意损失函数。例如，若存在显式反馈，可选择均方误差（MSE）损失；若为隐式反馈，则选择排序损失。

在 [Guo+17] 中，他们提出了一种称为**深度因子分解机**（deep factorization machines）的模型，该方法将上述技术与对嵌入向量进行拼接（而非内积）后施加的 MLP 相结合。更精确地说，该模型的形式为

$$  f(\boldsymbol{x};\boldsymbol{\theta})=\sigma(\mathrm{FM}(\boldsymbol{x})+\mathrm{MLP}(\boldsymbol{x}))   \tag*{(22.21)}$$

这与 [Che+16] 中提出的宽深模型（wide and deep model）密切相关。其思想是：双线性 FM 模型捕获特定用户与物品之间的显式交互（一种记忆形式），而 MLP 则捕获用户特征与物品特征之间的隐式交互，从而使模型具备泛化能力。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_266_127_878_482.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 22.5：神经矩阵分解模型示意图。摘自 $[He+17]$ 的图 2，经 Xiangnan He 许可使用。</div>


#### 22.2.3 神经矩阵分解

本节介绍 $[He+17]$ 提出的神经矩阵分解模型。这是将双线性模型与深度神经网络相结合的另一种方式。双线性部分用于定义以下广义矩阵分解（GMF）路径，该路径为用户 u 和物品 i 计算以下特征向量：

$$  \boldsymbol{z}_{u i}^{1}=\mathbf{P}_{u,:}\odot\mathbf{Q}_{i,:}   \tag*{(22.22)}$$

其中，$\mathbf{P} \in \mathbb{R}^{MK}$ 是用户嵌入矩阵，$\mathbf{Q} \in \mathbb{R}^{NK}$ 是物品嵌入矩阵。DNN 部分则是一个应用于嵌入向量拼接（使用不同的嵌入矩阵）的 MLP：

$$  z_{u i}^{2}=\mathrm{M L P}([\tilde{\mathbf{U}}_{u,:},\tilde{\mathbf{V}}_{i,:}])   \tag*{(22.23)}$$

最后，模型将两者结合得到：

$$  f(u,i;\boldsymbol{\theta})=\sigma(\boldsymbol{w}^{\mathsf{T}}[\boldsymbol{z}_{u i}^{1},\boldsymbol{z}_{u i}^{2}])   \tag*{(22.24)}$$

示意图见图 22.5。

在 $[He+17]$ 中，该模型基于隐式反馈进行训练，其中如果用户 u 与物品 i 的交互被观测到，则 $y_{ui}=1$，否则 $y_{ui}=0$。不过，也可以采用最小化 BPR 损失的方式训练。

### 22.3 利用辅助信息

到目前为止，我们假设预测器可用的唯一信息是用户的整数 ID 和物品的整数 ID。这是一种极为贫乏的表示，将无法

作者：Kevin P. Murphy。(C) 麻省理工学院出版社。CC-BY-NC-ND 许可协议

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2">特征向量 $ \mathbf{x} $</td></tr></table>

<div style="text-align: center;">图 22.6: 电影推荐系统中设计矩阵的示意图，其中展示了用户和电影的ID，以及其他侧边信息。源自 [Ren12] 中的图 1。经 Stefen Rendle 许可使用。</div>

当我们遇到新用户或新项目时（即所谓的 **冷启动** 问题），现有模型可能无法正常工作。为了克服这一问题，我们需要利用超越用户/项目 ID 的“侧边信息”。

我们可以使用多种形式的侧边信息。对于项目，我们通常拥有丰富的元数据，例如文本（如标题）、图像（如封面）、高维类别变量（如位置）或仅标量值（如价格）。对于用户，侧边信息的可用性取决于交互系统的具体形式。对于搜索引擎，侧边信息是用户发出的查询列表，以及（如果用户已登录）从他们访问过的网站中派生出的信息（这些信息通过 cookies 追踪）。对于在线购物网站，侧边信息包括搜索记录以及过去的浏览和购买行为。对于社交网络网站，则有关于每个用户好友图的信息。

通过将 $ \pmb{x} $ 的定义扩展到两个独热向量之外，如图 22.6 所示，我们可以非常容易地在因子分解机框架中捕捉这些侧边信息。当然，相同的输入编码也可以馈送到其他类型的模型中，例如 DeepFM 或 NeuralMF。

除了用户和项目相关的特征外，还可能存在其他上下文特征，例如交互的时间（如白天或晚上）。最近浏览项目的顺序（序列）通常也是一个有用的信号。[TW18] 中提出的“卷积序列嵌入推荐”（Convolutional Sequence Embedding Recommendation，简称 Caser）模型通过嵌入最近的 M 个项目，并将 $ M \times K $ 输入视为图像，利用卷积层作为模型的一部分来捕捉这一信息。

还可以为推荐任务设计许多其他类型的神经模型。相关综述可参见 [Zha+19b]。

### 22.4 探索与利用的权衡

推荐系统与其他预测问题的一个有趣 **区别** 在于：系统所训练的数据是早期版本系统推荐的结果，因此存在一个反馈循环 [Bot+13]。例如，考虑 YouTube 视频推荐系统 [CAS16]。该网站有数百万个视频，因此系统必须为用户提供一个候选列表（或称为“slate”），以帮助他们找到所需内容（例如参见 [Ie+19]）。如果用户观看了其中某个视频，系统会将其视为正面反馈，表明推荐效果好，并据此更新模型参数。然而，可能还有用户更喜欢的其他视频未被展示？

---

除非系统冒险展示一些用户响应不确定的项目，否则无法回答这种反事实问题。这是探索-利用权衡的一个例子。

除了需要探索之外，系统可能还需要等待很长时间，才能检测到其对推荐策略所做的更改是否有利。通常使用强化学习来学习优化长期奖励的策略。详情请参见本书的续篇[Mur23]。

---

请提供需要翻译的英文学术论文 Markdown 文本。

---

# 23 图嵌入 $ ^{*} $

本章与 Bryan Perozzi、Sami Abu-El-Haija 和 Ines Chami 合著，基于 [Cha+21] 撰写。

### 23.1 引言

现在，我们将关注点转向训练样本 $\{\mathbf{x}_n\}_{n=1}^N$ 之间具有语义关系的数据。这些关系（称为边）将训练样本（节点）与应用特定意义（通常是相似性）相连。图提供了对这种关系进行数学推理的基础。

图是一种通用数据结构，能够表示复杂的关联数据（由节点和边组成），并出现在多个领域，如社交网络、计算化学 [Gil+17]、生物学 [Sta+06]、推荐系统 [KSJ09]、半监督学习 [GB18] 等。

设 $\mathbf{A} \in \{0,1\}^{N \times N}$ 为邻接矩阵，其中 $N$ 是节点数量，并设 $\mathbf{W} \in \mathbb{R}^{N \times N}$ 为其加权版本。在后续讨论的方法中，有些设定 $\mathbf{W} = \mathbf{A}$，而另一些则将 $\mathbf{W}$ 设为 $\mathbf{A}$ 的某种变换，例如行归一化。最后，设 $\mathbf{X} \in \mathbb{R}^{N \times D}$ 为节点特征矩阵。

在设计并训练应用于图数据的神经网络模型时，我们希望所设计的方法能够适用于参与不同图设置（例如具有不同的连接和社区结构）的节点。这与为图像设计的神经网络模型形成对比：在图像中，每个像素（节点）具有相同的邻域结构。相比之下，任意图没有指定的节点对齐方式，而且每个节点可能具有不同的邻域结构。对比可参见图 23.1。因此，欧几里得空间卷积等操作无法直接应用于不规则图：欧几里得卷积强烈依赖于几何先验（如平移不变性），而这些先验无法推广到非欧几里得领域。

这些挑战催生了**几何深度学习（GDL）**的研究 [Bro+17b]，其目标是将深度学习技术应用于非欧几里得数据。特别是，由于图在现实世界应用中的广泛普及，将机器学习方法应用于图结构数据引起了浓厚兴趣。其中，**图表示学习（GRL）**方法 [Cha+21] 旨在为图结构数据学习低维连续向量表示，也称为嵌入。

在此，我们将 GRL 分为两类问题：无监督 GRL 和监督（或半监督）GRL。第一类旨在学习低维欧几里得表示，优化

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_283_198_501_420.jpg" alt="图像" width="18%" /></div>

<div style="text-align: center;">(a) 网格图（欧几里得空间）。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_598_216_863_439.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;">(b) 任意图（非欧几里得空间）。</div>

<div style="text-align: center;">图 23.1: 欧几里得图与非欧几里得图的示例。经 [Cha+21] 许可使用。</div>

一个目标，例如保持输入图的结构。第二类方法也学习低维欧几里得表示，但针对特定的下游预测任务，如节点分类或图分类。此外，图结构在训练和测试过程中可以固定不变，这被称为**直推式学习设置**（例如，在大型社交网络中预测用户属性）；或者模型需要回答训练期间未见过的图的相关问题，这被称为**归纳式学习设置**（例如，对分子结构进行分类）。最后，虽然大多数监督和无监督方法在欧几里得向量空间中学习表示，但近期人们对非欧几里得表示学习产生了兴趣，其目标是学习非欧几里得嵌入空间，如双曲空间或球面空间。这一系列工作的主要动机是使用一个连续的嵌入空间，使其类似于它所试图嵌入的输入数据的底层离散结构（例如，双曲空间是树的连续版本 [Sar11]）。

### 23.2 图嵌入作为编码器/解码器问题

尽管图表示学习（GRL）有许多方法，但许多方法遵循类似的模式。首先，网络输入（节点特征 $ \mathbf{X} \in \mathbb{R}^{N \times D} $ 以及图边，以 $ \mathbf{A} $ 或 $ \mathbf{W} \in \mathbb{R}^{N \times N} $ 表示）从图的离散域编码为连续表示（嵌入）$ \mathbf{Z} \in \mathbb{R}^{N \times L} $。接下来，学习到的表示 $ \mathbf{Z} $ 用于优化特定目标（例如，重构图的链接）。在本节中，我们将使用 Chami 等人 [Cha+21] 提出的图编码器-解码器模型（GRAPHEDM）来分析图表示学习方法的流行族。

GRAPHEDM 框架（图 23.2，[Cha+21]）提供了一个通用框架，涵盖了各种监督和无监督图嵌入方法：包括将图作为正则化项的方法（例如 [ZG02]）、位置嵌入方法（例如 [PARS14]），以及基于消息传递 [Gil+17; Sca+09] 或图卷积的图神经网络方法。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_181_143_991_322.jpg" alt="图像" width="70%" /></div>


<div style="text-align: center;">图 23.2：来自 Chami 等人 [Cha+21] 的 GRAPHEDM 框架示意图。根据可用的监督信号，方法将使用部分或全部分支。特别地，无监督方法不利用标签解码进行训练，仅优化相似度解码器（下方分支）。另一方面，半监督和有监督方法利用额外的监督信号来学习模型参数（上方分支）。经 [Cha+21] 许可转载。</div>


 $$ [\mathbf{B r u}+14;\mathbf{K W16a}]). $$ 

GRAPHEDM 框架的输入为一个加权图 $\mathbf{W} \in \mathbb{R}^{N \times N}$，以及可选的节点特征 $\mathbf{X} \in \mathbb{R}^{N \times D}$。在（半）监督设置中，我们假设已知节点（记为 $N$）、边（记为 $E$）和/或整个图（记为 $G$）的训练目标标签。我们将监督信号记为 $S \in \{N, E, G\}$，如下所述。

GRAPHEDM 模型本身可以分解为以下组件：

- **图编码器网络** $\text{ENC}_{\Theta^E} : \mathbb{R}^{N \times N} \times \mathbb{R}^{N \times D} \to \mathbb{R}^{N \times L}$，由 $\Theta^E$ 参数化，它将图结构与可选的节点特征相结合，生成节点嵌入矩阵 $\mathbf{Z} \in \mathbb{R}^{N \times L}$，如下所示：

$$  \mathbf{Z}=\mathrm{ENC}(\mathbf{W},\mathbf{X};\boldsymbol{\Theta}^{E}).   \tag*{(23.1)}$$

接下来我们将看到，这个节点嵌入矩阵可能根据训练所用的监督信号捕获不同的图属性。

- **图解码器网络** $\text{DEC}_{\Theta^D} : \mathbb{R}^{N \times L} \to \mathbb{R}^{N \times N}$，由 $\Theta^D$ 参数化，它利用节点嵌入 $Z$ 计算矩阵 $\widehat{\mathbf{W}} \in \mathbb{R}^{N \times N}$ 中所有节点对的相似度得分，如下所示：

$$  \widehat{\mathbf{W}}=\operatorname{D E C}(\mathbf{Z};\boldsymbol{\Theta}^{D}).   \tag*{(23.2)}$$

- **分类网络** $\text{DEC}_{\Theta^S} : \mathbb{R}^{N \times L} \to \mathbb{R}^{N \times |\mathcal{Y}|}$，其中 $\mathcal{Y}$ 是标签空间。该网络用于（半）监督设置，由 $\Theta^S$ 参数化。输出是基于节点嵌入的标签分布 $\hat{y}^S$，如下所示：

$$  \widehat{y}^{S}=\mathrm{D E C}(\mathbf{Z};\Theta^{S}).   \tag*{(23.3)}$$

上述（编码器和解码器）网络的具体选择使 GRAPHEDM 能够实现特定的图嵌入方法，我们将在后续小节中解释。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_282_145_901_218.jpg" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 23.3：浅层嵌入方法。编码器是一个简单的嵌入查找表，图结构仅用于损失函数。经许可转载自 $[Cha+21]$。</div>


模型输出，如 GRAPHEDM 框架所述，是一个重构的图相似矩阵 $\widehat{W}$（常用于训练无监督嵌入算法），以及/或用于监督任务的标签 $\widehat{y}^S$。标签输出空间 $\mathcal{Y}$ 依赖于具体应用。例如，在节点级分类中，$\widehat{y}^N \in \mathcal{Y}^N$，其中 $\mathcal{Y}$ 表示节点标签空间。或者，对于边级标注，$\widehat{y}^E \in \mathcal{Y}^{N \times N}$，其中 $\mathcal{Y}$ 表示边标签空间。最后，我们注意到其他类型的标注也是可能的，例如图级标注（此时可以认为 $\widehat{y}^G \in \mathcal{Y}$，其中 $\mathcal{Y}$ 表示图标签空间）。

最后，必须指定一个损失函数。该损失可用于优化参数 $\Theta = \{\Theta^E, \Theta^D, \Theta^S\}$。GRAPHEDM 模型可以通过结合三种不同的项来优化。首先，一个监督损失项 $\mathcal{L}_{\text{sup}}^S$，用于比较预测标签 $\hat{y}^S$ 与真实标签 $y^S$。其次，一个图重构损失项 $\mathcal{L}_{G,\text{RECON}}$，可以利用图结构对模型参数施加正则化约束。最后，一个权重正则化损失项 $\mathcal{L}_{\text{REG}}$，用于表示可训练模型参数上的先验信息以减少过拟合。通过最小化如下定义的总损失 $\mathcal{L}$ 来训练 GRAPHEDM 框架可实现的模型：

$$ \mathcal{L}=\alpha\mathcal{L}_{\mathrm{S U P}}^{S}(y^{S},\hat{y}^{S};\Theta)+\beta\mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\Theta)+\gamma\mathcal{L}_{\mathrm{R E G}}(\Theta), \tag*{(23.4)}$$

其中 $\alpha$、$\beta$ 和 $\gamma$ 是超参数，可以调整或设置为零。注意，图嵌入方法可以以监督（$\alpha \neq 0$）或无监督（$\alpha = 0$）的方式进行训练。监督图嵌入方法利用额外的信息源（如节点或图标签）来学习嵌入。另一方面，无监督网络嵌入方法仅依赖图结构来学习节点嵌入。

### 23.3 浅层图嵌入

浅层嵌入方法是直推式图嵌入方法，其中编码器函数通过一个嵌入矩阵将类别型节点 ID 映射到欧几里得空间。每个节点 $v_i \in V$ 都有一个对应的低维可学习嵌入向量 $\mathbf{Z}_i \in \mathbb{R}^L$，浅层编码器函数为：

$$ \mathbf{Z}=\mathrm{ENC}(\Theta^{E})\triangleq\Theta^{E}\mathrm{\quad where\quad }\Theta^{E}\in\mathbb{R}^{N\times L}. \tag*{(23.5)}$$

关键之处在于，嵌入字典 Z 是直接作为模型参数学习的。在无监督情况下，嵌入 Z 被优化以恢复输入图的一些信息（例如，邻接矩阵 W 或其某种变换）。这类似于降维方法（如第 20.1 节的 PCA），但针对图数据结构。在监督情况下，嵌入被优化以预测节点、边和/或整个图的某些标签。

---

#### 23.3.1 无监督嵌入

在无监督情况下，我们将考虑两种主要的浅层图嵌入方法：基于距离的方法和基于外积的方法。基于距离的方法优化嵌入字典 $\mathbf{Z} = \Theta^E \in \mathbb{R}^{N \times L}$，使得图中相近的节点 $i$ 和 $j$（由某种图距离函数度量）在 $\mathbf{Z}$ 中被嵌入，且 $d_2(\mathbf{Z}_i, \mathbf{Z}_j)$ 很小，其中 $d_2(\cdot, \cdot)$ 是嵌入向量之间的成对距离函数。距离函数 $d_2(\cdot, \cdot)$ 可以自定义，从而得到欧几里得（第23.3.2节）或非欧几里得（第23.3.3节）嵌入。解码器输出一个节点到节点的矩阵 $\widehat{\mathbf{W}} = \text{DEC}(\mathbf{Z}; \Theta^D)$，其中 $\widehat{W}_{ij} = d_2(\mathbf{Z}_i, \mathbf{Z}_j)$。

或者，某些方法依赖成对点积来计算节点相似度。解码器网络可以写为：$\widehat{W} = \text{DEC}(\mathbf{Z}; \boldsymbol{\Theta}^D) = \mathbf{Z}\mathbf{Z}^\top$。

在两种情况下，基于距离和基于乘积的方法的无监督嵌入都是通过最小化图重构损失来学习的：

$$  \mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\boldsymbol{\Theta})=d_{1}(s(\mathbf{W}),\widehat{\mathbf{W}}),   \tag*{(23.6)}$$

其中 $s(\mathbf{W})$ 是邻接矩阵 $\mathbf{W}$ 的可选变换，$d_1$ 是矩阵之间的成对距离函数，不必与 $d_2$ 形式相同。如我们将看到的，$s, d_1, d_2$ 有许多合理的选择。例如，我们可以令 $s$ 为邻接矩阵本身，$s(\mathbf{W}) = \mathbf{W}$ 或其幂次，如 $s(\mathbf{W}) = \mathbf{W}^2$。如果输入是加权二进制矩阵 $\mathbf{W} = \mathbf{A}$，我们可以设置 $s(\mathbf{W}) = 1 - \mathbf{W}$，这样 $A_{ij} = 1$ 的相连节点权重（距离）为 0。

#### 23.3.2 基于距离：欧几里得方法

基于距离的方法最小化相似（相连）节点之间的欧几里得距离。下面给出一些例子。

多维缩放（MDS，第20.4.4节）等价于将 $s(\mathbf{W})$ 设置为某种度量节点间不相似性的距离矩阵（例如与成对最短距离成比例的距离），然后定义

$$  d_{1}(s(W),\widehat{W})=\sum_{i,j}(s(W)_{ij}-\widehat{W}_{ij})^{2}=||s(\mathbf{W})-\widehat{\mathbf{W}}||_{F}^{2}   \tag*{(23.7)}$$

其中 $\widehat{W}_{ij} = d_2(\mathbf{Z}_i, \mathbf{Z}_j) = ||\mathbf{Z}_i - \mathbf{Z}_j||$（尽管其他距离度量也是可行的）。

拉普拉斯特征映射（第20.4.9节）通过求解广义特征向量问题来学习嵌入：

$$  \min_{\mathbf{Z}\in\mathbb{R}^{|V|\times d}}\mathrm{tr}(\mathbf{Z}^{\intercal}\mathbf{L}\mathbf{\Lambda}\mathbf{Z})\quad s.t.\quad\mathbf{Z}^{\intercal}\mathbf{D}\mathbf{Z}=\mathbf{I}\quad and\quad\mathbf{Z}^{\intercal}\mathbf{D}\mathbf{1}=\mathbf{0}   \tag*{(23.8)}$$

其中 $\mathbf{L} = \mathbf{D} - \mathbf{W}$ 是图拉普拉斯矩阵（第20.4.9.2节），$\mathbf{D}$ 是对角矩阵，其对角线元素为每行列和。第一个约束消除了嵌入中的任意缩放因子，第二个约束排除了对应常数特征向量（对于连通图特征值为零）的平凡解。此外，注意 $\operatorname{tr}(\mathbf{Z}^\top \mathbf{L} \mathbf{Z}) = \frac{1}{2} \sum_{i,j} W_{ij} \| \mathbf{Z}_i - \mathbf{Z}_j \|^2$，其中 $\mathbf{Z}_i$ 是 $\mathbf{Z}$ 的第 $i$ 行；因此最小化目标可以等价地写为

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

图重构项如下：

$$  d_{1}(s(\mathbf{W}),\widehat{\mathbf{W}})=\sum_{i,j}\mathbf{W}_{ij}\times\widehat{\mathbf{W}}_{ij}   \tag*{(23.9)}$$

$$  \widehat{\mathbf{W}}_{ij}=d_{2}(\mathbf{Z}_{i},\mathbf{Z}_{j})=||\mathbf{Z}_{i}-\mathbf{Z}_{j}||_{2}^{2}   \tag*{(23.10)}$$

其中 $  s(\mathbf{W}) = \mathbf{W}  $.

#### 23.3.3 基于距离的非欧几里得方法

到目前为止，我们讨论的方法均假设嵌入位于欧几里得空间中。然而，最近的工作考虑了双曲几何用于图嵌入。特别是，双曲嵌入非常适合嵌入树状结构，并为展现层次结构的图提供了一种令人兴奋的欧几里得几何替代方案。下面我们给出一些例子。

Nickel 和 Kiela [NK17] 利用双曲空间的庞加莱模型学习层次图的嵌入。这在我们记法中很容易表示，只需将 $ d_2(\mathbf{Z}_i, \mathbf{Z}_j) $ 替换为庞加莱距离函数：

$$  d_{2}(\mathbf{Z}_{i},\mathbf{Z}_{j})=d_{\mathrm{Poincaré}}(\mathbf{Z}_{i},\mathbf{Z}_{j})=\operatorname{arcosh}\left(1+2\frac{||\mathbf{Z}_{i}-\mathbf{Z}_{j}||_{2}^{2}}{(1-||\mathbf{Z}_{i}||_{2}^{2})(1-||\mathbf{Z}_{j}||_{2}^{2})}\right).   \tag*{(23.11)}$$

优化过程学习嵌入，使连接节点之间的距离最小化，同时使未连接节点之间的距离最大化：

$$  d_{1}(\mathbf{W},\widehat{\mathbf{W}})=\sum_{i,j}\mathbf{W}_{i j}\log\frac{e^{-\widehat{\mathbf{W}}_{i j}}}{\sum_{k|\mathbf{W}_{i k}=0}e^{-\widehat{\mathbf{W}}_{i k}}}   \tag*{(23.12)}$$

其中分母通过负采样近似。注意，由于双曲空间具有流形结构，需要小心确保嵌入保持在流形上（使用黎曼优化技术 [Bon13]）。

这些方法的其他变体已被提出。Nickel 和 Kiela [NK18] 探索了双曲空间的洛伦兹模型，并表明该模型比庞加莱模型具有更好的数值稳定性。另一项工作将非欧几里得嵌入扩展到混合曲率乘积空间 [Gu+18]，为其他类型的图（例如树环）提供了更大的灵活性。最后，Chamberlain、Clough 和 Deisenroth [CCD17] 利用双曲内积的 skip-gram 损失扩展了庞加莱嵌入。

#### 23.3.4 基于外积的矩阵分解方法

矩阵分解方法学习嵌入，从而得到某个相似矩阵 $s(\mathbf{W})$ 的低秩表示，其中 $s:\mathbb{R}^{N\times N}\to\mathbb{R}^{N\times N}$。以下是常见选择：$s(\mathbf{W})=\mathbf{W}$、$s(\mathbf{W})=L$（图拉普拉斯矩阵），或其他邻近度量，如 Katz 中心性指数、共同邻居或 Adamic/Adar 指数。

矩阵分解方法中的解码器函数就是一个点积：

$$  \widehat{\mathbf{W}}=\mathrm{DEC}(\mathbf{Z};\boldsymbol{\Theta}^{D})=\mathbf{Z}\mathbf{Z}^{\mathrm{T}}   \tag*{(23.13)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_148_117_1010_275.jpg" alt="图像" width="74%" /></div>


<div style="text-align: center;">图 23.4：随机游走图嵌入方法的流水线概述。经 [God18] 许可转载。</div>


矩阵分解方法通过最小化正则化损失 $ \mathcal{L}_{G,\mathrm{RECON}}(\mathbf{W},\widehat{\mathbf{W}};\boldsymbol{\Theta})=||s(\mathbf{W})-\widehat{\mathbf{W}}||_F^2 $ 来学习 $ \mathbf{Z} $。

$[Ahm+13]$ 的图分解方法通过最小化图正则化损失 $ \mathcal{L}_{G,\mathrm{RECON}}(\mathbf{W},\widehat{\mathbf{W}};\Theta)=\sum_{(v_{i},v_{j})\in E}(\mathbf{W}_{ij}-\widehat{\mathbf{W}}_{ij})^{2} $ 来学习图的低秩分解。

注意，如果 $ \mathbf{A} $ 是二值邻接矩阵（$ \mathbf{A}_{ij} = 1$ 当且仅当 $(v_i, v_j) \in E$，否则 $ \mathbf{A}_{ij} = 0 $），则图重构损失可以用 Frobenius 范数表示：

$$  \mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\boldsymbol{\Theta})=||\mathbf{A}\odot(\mathbf{W}-\widehat{\mathbf{W}})||_{F}^{2},   \tag*{(23.14)}$$

其中 $ \odot $ 是逐元素矩阵乘法算子。因此，GF 还学习用 Frobenius 范数度量的邻接矩阵 W 的低秩分解。我们注意到这是一个稀疏操作（仅对图中存在的边求和），因此该方法具有计算复杂度 $ O(M) $。

到目前为止描述的方法都是对称的，即它们假设 $ \mathbf{W}_{ij} = \mathbf{W}_{ji} $。这在处理有向图时是一个限制，因为某些关系不是互逆的。[CLX15] 的 GraRep 方法通过为每个节点学习两个嵌入来克服这一限制：源嵌入 $ \mathbf{Z}^s $ 和目标嵌入 $ \mathbf{Z}^t $，它们捕捉有向网络中的非对称邻近性。除了非对称性之外，GraRep 还通过邻接矩阵的幂次来学习保留 $ k $ 跳邻域的嵌入，并最小化图重构损失：

$$  \widehat{\mathbf{W}}^{(k)}=\mathbf{Z}^{(k),s}\mathbf{Z}^{(k),t}^{\mathsf{T}}   \tag*{(23.15)}$$

$$  \mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}}^{(k)};\Theta)=||\mathbf{D}^{-k}\mathbf{W}^{k}-\widehat{\mathbf{W}}^{(k)}||_{F}^{2},   \tag*{(23.16)}$$

对于每个 $ 1 \leq k \leq K $。GraRep 将所有表示拼接起来得到源嵌入 $ \mathbf{Z}^s = [\mathbf{Z}^{(1),s}|...|\mathbf{Z}^{(K),s}] $ 和目标嵌入 $ \mathbf{Z}^t = [\mathbf{Z}^{(1),t}|...|\mathbf{Z}^{(K),t}] $。不幸的是，GraRep 的可扩展性不好，因为它使用了矩阵幂 $ \mathbf{D}^{-1}\mathbf{W} $，使其变得越来越稠密。这一限制可以通过使用隐式矩阵分解 [Per+17] 来规避，如下所述。

#### 23.3.5 基于外积的：Skip-gram 方法

Skip-gram 图嵌入模型受自然语言处理研究的启发，用于建模词的分布行为 $ [Mik+13c; PSM14b] $。Skip-gram 词嵌入经过优化，可以预测句子中每个目标词在其上下文（周围词）中的词。给定

---

给定一个单词序列 $(w_{1},\ldots,w_{T})$，skip-gram 模型将最小化如下目标函数：

$$ \mathcal{L}=-\sum_{-K\leq i\leq K,i\neq0}\log\mathbb{P}(w_{k-i}|w_{k}), $$

对于每个目标词 $w_{k}$。这些条件概率可以通过神经网络高效估计，详见第 20.5.2.2 节。

这一思想被 [PARS14] 的 DeepWalk 框架用于图嵌入。他们通过实验证明，真实图上随机游走产生的频率统计与自然语言中单词的分布类似。在 GRAPHEDM 框架下，skip-gram 图嵌入方法使用外积（公式 23.13）作为解码函数，并基于图上的随机游走计算图重构项。

具体而言，DeepWalk 训练节点嵌入，以最大化每个中心节点预测其上下文节点的概率。上下文节点是在模拟图 $\mathbf{A}$ 上随机游走时与中心节点相邻出现的节点。为训练嵌入，DeepWalk 使用截断无偏随机游走在图上生成节点序列——可类比于自然语言模型中的句子——然后最大化其对数似然。每个随机游走从节点 $v_{i_1} \in V$ 开始，并重复均匀随机采样下一个节点：$v_{i_{j+1}} \in \{v \in V \mid (v_{i_j}, v) \in E\}$。游走长度是一个超参数。所有生成的随机游走序列可由一个序列模型编码。[PARS14] 引入的这一两步范式被后续许多工作沿用，如 node2vec [GL16]。

我们注意到，底层实现通常为每个节点使用两种不同的表示：一种用于节点作为截断随机游走的中心，另一种用于节点处于上下文时。该建模选择的影响在 [AEHPAR17] 中有进一步研究。

为了在 GRAPHEDM 框架下描述 DeepWalk，我们可以定义：

$$  s(\mathbf{W})=\mathbb{E}_{q}\left[\left(\mathbf{D}^{-1}\mathbf{W}\right)^{q}\right]\mathrm{with} q\sim P(Q)=\mathrm{Categorical}([1,2,\ldots,T_{\mathrm{max}}])   \tag*{(23.17)}$$

其中 $P(Q = q) = \frac{T_{\max} - 1 + q}{T_{\max}}$（推导见 [AEH+18]）。

训练 DeepWalk 等价于最小化：

$$  \mathcal{L}_{G,\mathrm{RECON}}(W,\widehat{W};\Theta)=\log Z(\mathbf{Z})-\sum_{v_{i}\in V,v_{j}\in V}s(\mathbf{W})_{ij}\widehat{\mathbf{W}}_{ij},   \tag*{(23.18)}$$

其中 $\widehat{\mathbf{W}} = \mathbf{Z}\mathbf{Z}^\top$，配分函数 $Z(\mathbf{Z}) = \prod_i \sum_j \exp(\widehat{\mathbf{W}}_{ij})$ 可以通过层次化 softmax 在 $O(N)$ 时间内近似（见第 20.5.2 节）。（对于有向图，通常使用嵌入字典 $\mathbf{Z}_{\text{out}}, \mathbf{Z}_{\text{in}} \in \mathbb{R}^{N \times L}$ 建模 $\widehat{\mathbf{W}} = \mathbf{Z}_{\text{out}}\mathbf{Z}_{\text{in}}^\top$。）

如 [LG14] 所指出的，Skip-gram 方法可被视为隐式矩阵分解，此处讨论的方法与矩阵分解方法（见第 23.3.4 节）相关。该关系在 [Qiu+18] 中得到深入探讨，他们提出了一个通用的矩阵分解框架 NetMF，该框架使用了与 DeepWalk、LINE [Tan+15] 和 node2vec [GL16] 相同的基础图邻近信息。将节点嵌入问题转化为矩阵分解，可以继承高效稀疏矩阵运算的优势 [Qiu+19a]。

---

#### 23.3.6 监督嵌入

在许多应用中，除了节点特征和图结构外，我们还有标注数据。虽然可以先学习无监督表示，然后将其作为特征用于辅助模型，从而处理监督任务，但这并非理想的工作流程。无监督节点嵌入可能无法保留对下游监督任务最有用的图的关键属性（例如节点邻居或属性）。

鉴于这一局限性，人们提出了一些将这两个步骤（即学习嵌入和预测节点或图标签）相结合的方法。在此，我们聚焦于简单的浅层方法。深度非线性嵌入将在后续讨论。

##### 23.3.6.1 标签传播（Label propagation, LP）

标签传播（Label propagation, LP）[ZG02] 是一种非常流行的基于图的半监督节点分类算法。其编码器是一个由查找表 Z 表示的浅层模型。LP 直接使用标签空间来表示节点嵌入（即 LP 中的解码器就是恒等函数）：

$$ \hat{y}^{N}=\mathrm{D E C}(\mathbf{Z};\boldsymbol{\Theta}^{C})=\mathbf{Z}. $$ 

具体而言，LP 利用图结构通过向损失函数添加正则化项来平滑标签分布，其基本假设是邻居节点应具有相似的标签（即连接节点之间存在某种标签一致性）。正则化项中使用拉普拉斯特征映射来强制实现这种平滑性：

$$  \mathcal{L}_{G,\mathrm{RECON}}(\mathbf{W},\widehat{\mathbf{W}};\Theta)=\sum_{i,j}\mathbf{W}_{i j}||y_{i}^{N}-\hat{y}_{j}^{N}||_{2}^{2}   \tag*{(23.19)}$$

LP 通过一种迭代算法，在标记节点上取固定值的函数空间（即 $ \hat{y}_i^N = y_i^N \forall i | v_i \in V_L $）中最小化该能量函数，该算法利用其邻居标签的加权平均来更新未标记节点的标签分布。

标签扩散（Label spreading, LS）[Zho+04] 是标签传播的一种变体，它最小化以下能量函数：

$$  \mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\Theta)=\sum_{i,j}\mathbf{W}_{i j}\left|\left|\frac{\hat{y}_{i}^{N}}{\sqrt{D_{i}}}-\frac{\hat{y}_{j}^{N}}{\sqrt{D_{j}}}\right|\right|_{2}^{2},   \tag*{(23.20)}$$

其中 D i = ∑ i W i j 是节点 vi 的度数。

在两种方法中，监督损失仅仅是预测标签与真实标签（独热向量）之间的距离之和：

$$  \mathcal{L}_{\mathrm{S U P}}^{N}(y^{N},\hat{y}^{N};\Theta)=\sum_{i|v_{i}\in V_{L}}||y_{i}^{N}-\hat{y}_{i}^{N}||_{2}^{2}.   \tag*{(23.21)}$$

注意，正则化项是在图中所有节点上计算的，而监督损失仅对标记节点计算。这些方法预期在一致性图上表现良好，即图中节点邻近度与标签相似度正相关的图。

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可证。

---

### 23.4 图神经网络

一个广泛的研究领域致力于定义图数据上的卷积。在 Chami 等人 [Cha+21] 的符号体系下，这些（半）监督邻域聚合方法可以用如下形式的编码器表示：$ \mathbf{Z} = \text{ENC}(\mathbf{X}, \mathbf{W}; \boldsymbol{\Theta}^E) $，以及如下形式的解码器：$ \widehat{\mathbf{W}} = \text{DEC}(\mathbf{Z}; \boldsymbol{\Theta}^D) $ 和/或 $ \widehat{\mathbf{y}}^S = \text{DEC}(\mathbf{Z}; \boldsymbol{\Theta}^S) $。该家族中有许多模型；下面我们将回顾其中一部分。

#### 23.4.1 消息传递图神经网络

[GMS05; Sca+09] 提出的原始图神经网络（GNN）模型是图结构数据深度学习方法的首个形式化描述。它将有监督的图嵌入问题视为一种信息扩散机制，其中节点向其邻居发送信息，直至达到某种稳定平衡态。具体而言，给定随机初始化的节点嵌入 $ \mathbf{Z}^0 $，它应用如下递归：

$$  \mathbf{Z}^{t+1}=\mathrm{ENC}(\mathbf{X},\mathbf{W},\mathbf{Z}^{t};\Theta^{E}),   \tag*{(23.22)}$$

其中参数 $ \Theta^{E} $ 在每次迭代中被重用。收敛后 $ (t = T) $，节点嵌入 $ \mathbf{Z}^{T} $ 用于预测最终输出，例如节点或图标签：

$$  \hat{y}^{S}=\mathrm{D E C}(\mathbf{X},\mathbf{Z}^{T};\Theta^{S}).   \tag*{(23.23)}$$

该过程重复若干次，GNN 参数 $ \Theta^E $ 和 $ \Theta^D $ 通过 Almeda-Pineda 算法 [Alm87; Pin88] 利用反向传播进行学习。根据巴拿赫不动点定理，当递归提供收缩映射时，该过程保证收敛到唯一解。鉴于此，Scarselli 等人 [Sca+09] 探索了可以用消息传递网络表示的映射：

$$  \mathbf{Z}_{i}^{t+1}=\sum_{j\mid(v_{i},v_{j})\in E}f(\mathbf{X}_{i},\mathbf{X}_{j},\mathbf{Z}_{j}^{t};\Theta^{E}),   \tag*{(23.24)}$$

其中 $ f(\cdot) $ 是一个受约束为收缩映射的多层感知器（MLP）。然而，解码器函数没有约束，可以是任意 MLP。

Li 等人 [Li+15] 提出了门控图序列神经网络（Gated Graph Sequence Neural Networks, GGSNNs），该模型去除了 GNN 中的收缩映射要求。在 GGSNNs 中，通过应用固定步数的映射函数来放宽式(23.22)中的递归算法，每个映射函数是一个门控循环单元 [Cho+14b]，其参数在每次迭代中共享。GGSNN 模型在每一步都会输出预测，因此特别适用于具有序列结构的任务（如时态图）。

Gilmer 等人 [Gil+17] 提出了一个称为消息传递神经网络（Message Passing Neural Networks, MPNNs）的图神经网络框架，该框架封装了许多近期模型。与运行不定迭代次数的 GNN 模型不同，MPNNs 为现代方法提供了一种抽象，这些方法由具有固定层数的多层神经网络组成。在每一层 $\ell$ 中，消息函数 $f^{\ell}(\cdot)$ 从邻居处接收消息（基于邻居的隐藏状态），

---

然后将其传递给聚合函数 \( h^{\ell}(\cdot) \)：

$$ \mathbf{m}_{i}^{\ell+1}=\sum_{j|(v_{i},v_{j})\in E}f^{\ell}(\mathbf{H}_{i}^{\ell},\mathbf{H}_{j}^{\ell}) \tag*{(23.25)}$$

$$ \mathbf{H}_{i}^{\ell+1}=h^{\ell}(\mathbf{H}_{i}^{\ell},\mathbf{m}_{i}^{\ell+1}), \tag*{(23.26)}$$

其中 \( \mathbf{H}^{0} = \mathbf{X} \)。经过 \( \ell \) 层消息传递后，节点的隐藏表示编码了 \( \ell \) 跳邻域内的信息。

Battaglia 等人 [Bat+18] 提出了 **GraphNet**，它通过使用消息传递函数进一步扩展了 MPNN 框架，以学习边、节点和整个图的表示。显式添加边和图表示增强了 MPNN 模型的表达能力，并允许将图模型应用于更多领域。

#### 23.4.2 谱图卷积

谱方法利用图拉普拉斯矩阵的谱域来定义图卷积。这些方法大致分为两类：**基于谱的方法**，显式计算拉普拉斯矩阵的特征分解（例如，谱 CNN [Bru+14]）；**免谱方法**，受谱图理论启发但实际不进行谱分解（例如，图卷积网络或 GCN [KW16a]）。

基于谱方法的一个主要缺点是它们依赖于图拉普拉斯矩阵的谱，因此是域相关的（即无法推广到新图）。此外，计算拉普拉斯矩阵的谱分解在计算上代价高昂。免谱方法通过利用这些谱滤波器的近似来克服这些限制。然而，免谱方法需要使用整个图 \( W \)，因此可扩展性不佳。

有关谱方法的更多细节，请参见例如 [Bro+17b; Cha+21]。

#### 23.4.3 空间图卷积

基于谱的方法具有固有的域依赖性，这限制了在一个图上训练的模型应用于新数据集的可能性。此外，免谱方法（例如 GCN）需要使用整个图 \( A \)，随着图规模的增长，这很快变得不可行。

为了克服这些限制，图卷积的另一分支（**空间方法**）借鉴了标准 CNN 的思想——在图拓扑定义的空间域中应用卷积。例如，在计算机视觉中，卷积滤波器通过在每个像素周围使用固定的矩形块来实现空间局部化。结合图像中像素的自然顺序（上、左、下、右），可以在每个位置复用滤波器的权重。这一过程显著减少了模型所需的参数总数。虽然这种空间卷积无法直接应用于图域，但空间图卷积从中汲取灵感。其核心思想是使用邻域采样和注意力机制来创建固定大小的图块，从而克服图的不规则性。

##### 23.4.3.1 基于采样的空间方法

为克服 GCN 的域依赖性和存储限制，Hamilton、Ying 和 Leskovec [HYL17] 提出了 **GraphSAGE**，一个学习归纳式节点嵌入的框架。而非

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_246_125_453_315.jpg" alt="图像" width="17%" /></div>


<div style="text-align: center;">1. 采样邻域</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_477_121_684_308.jpg" alt="图像" width="17%" /></div>


<div style="text-align: center;">2. 从邻居聚合特征信息</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_708_124_934_302.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">3. 利用聚合信息预测图上下文和标签</div>


<div style="text-align: center;">图23.5：GraphSAGE模型示意图。经[HYL17]许可转载。</div>


与通过对所有一跳邻居的信号取平均（通过与拉普拉斯矩阵相乘）不同，SAGE为每个节点采样固定大小的邻域（大小为q）。这消除了对固定图结构的强依赖，并允许泛化到新图。在每个SAGE层，节点从其邻域中采样的节点聚合信息（见Figure 23.5）。在GRAPHEDM记法中，传播规则可写为：

$$  \mathbf{H}_{:,i}^{\ell+1}=\sigma(\Theta_{1}^{\ell}\mathbf{H}_{:,i}^{\ell}+\Theta_{2}^{\ell}\mathrm{A G G}(\{\mathbf{H}_{:,j}^{\ell}\mid v_{j}\in\mathrm{S a m p l e}(\mathrm{n b r}(v_{i}),q)\})),   \tag*{(23.27)}$$

其中 $ AGG(\cdot) $ 是聚合函数。该聚合函数可以是任何置换不变算子，例如取均值（SAGE-mean）或最大池化（SAGE-pool）。由于SAGE处理固定大小的邻域（而非整个邻接矩阵），因此它也降低了GCN训练的计算复杂度。

##### 23.4.3.2 基于注意力的空间方法

注意力机制（第15.4节）已成功应用于语言模型，例如使模型能够识别长序列输入中的相关部分。受其在语言领域成功的启发，类似的想法已被提出用于图卷积网络。这种基于图的注意力模型通过基于节点特征学习的参数化补丁，在消息传递步骤中学习将注意力集中在重要邻居上。与依赖固定权重（如GCN）的方法相比，这为归纳式设置提供了更大的灵活性。

[Vel+18]提出的图注意力网络（GAT）模型是GCN的注意力版本。在每个GAT层，模型关注每个节点的邻域，并学习选择能为下游任务带来最优性能的节点。其背后的直觉与SAGE [HYL17]类似，使得GAT适用于归纳式和直推式问题。然而，与SAGE将卷积步骤限制为固定大小邻域不同，GAT允许每个节点关注其所有邻居——为每个邻居分配不同的权重。注意力参数通过反向传播进行训练，注意力分数随后通过softmax激活进行行归一化。

---

##### 23.4.3.3 几何空间方法

Monti 等人 [Mon+17] 提出了 MoNet，这是一个通用框架，在节点特征位于几何空间（例如 3D 点云或网格）中时尤其有效。MoNet 在预定义的空间域（例如空间坐标）中使用参数函数学习注意力块，然后在得到的图域中应用卷积滤波器。

MoNet 推广了那些引入流形上卷积构造的空间方法，例如测地线 CNN（GCNN）[Mas+15] 和各向异性 CNN（ACNN）[Bos+16]。GCNN 和 ACNN 都使用定义在特定坐标系上的固定块，因此无法推广到图结构数据。然而，MoNet 框架更为通用；任何伪坐标（即节点特征）都可以用来导出这些块。更正式地，如果 $ U^s $ 是伪坐标，$ \mathbf{H}^\ell $ 是来自另一个域的特征，那么 MoNet 层可以用我们的符号表示为：

$$  \mathbf{H}^{\ell+1}=\sigma\bigg(\sum_{k=1}^{K}(\mathbf{W}\odot g_{k}(\mathbf{U}^{s}))\mathbf{H}^{\ell}\Theta_{k}^{\ell}\bigg),   \tag*{(23.28)}$$

其中 $ g_k(U^s) $ 是学习到的参数化块，是 $ N \times N $ 矩阵。在实践中，MoNet 使用高斯核来学习块，使得：

$$  g_{k}(\mathbf{U}^{s})=\exp\Bigg(-\frac{1}{2}(\mathbf{U}^{s}-\boldsymbol{\mu}_{k})^{\top}\boldsymbol{\Sigma}_{k}^{-1}(\mathbf{U}^{s}-\boldsymbol{\mu}_{k})\Bigg),   \tag*{(23.29)}$$

其中 $ \mu_k $ 和 $ \Sigma_k $ 是学习到的参数，且 $ \Sigma_k $ 被限制为对角矩阵。

#### 23.4.4 非欧几里得图卷积

正如我们在第 23.3.3 节中所讨论的，双曲几何能够学习层次图的浅层嵌入，其失真比欧几里得嵌入更小。然而，浅层嵌入的一个主要缺点是它们在图之间泛化能力不佳（如果有的话）。另一方面，利用节点特征的图神经网络在许多归纳图嵌入任务上取得了良好的结果。

因此，最近人们自然地对扩展图神经网络以学习非欧几里得嵌入产生了兴趣。这样做的一个主要挑战再次围绕着卷积本身的本质。在非欧几里得空间中，内积和矩阵乘法等标准运算无法定义，我们应该如何执行卷积？

双曲图卷积网络（HGCN）[Cha+19a] 和双曲图神经网络（HGNN）[LNK19] 通过利用欧几里得切空间（提供双曲流形在一点处的一阶近似）在双曲空间中应用图卷积。对于每一步图卷积，节点嵌入被映射到原点处的欧几里得切空间，在那里应用卷积，然后再映射回双曲空间。这些方法在具有层次结构的图上取得了显著改进（图 23.6）。

### 23.5 深度图嵌入

在本节中，我们使用图神经网络为无监督和半监督情况设计图嵌入。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_211_174_564_318.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">(a) GCN 层。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_598_133_939_310.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;">(b) HGCN 层。</div>

<div style="text-align: center;">图 23.6：树图的欧几里得（左）和双曲（右）嵌入。双曲嵌入在嵌入空间中学习自然的层次结构（深度由颜色表示）。经许可转载自 [Cha+19a]。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_264_472_902_605.jpg" alt="Image" width="55%" /></div>

<div style="text-align: center;">图 23.7：无监督图神经网络。使用图神经网络编码器将图结构和输入特征映射到低维嵌入。然后对嵌入进行解码，以计算图正则化损失（无监督）。经许可转载自 [Cha+21]。</div>

#### 23.5.1 无监督嵌入

##### 23.5.1.1 结构深度网络嵌入

在本节中，我们讨论图神经网络的无监督损失，如图 23.7 所示。

[WCZ16] 提出的结构深度网络嵌入（SDNE）方法使用自编码器，保留节点的一阶和二阶邻近性。SDNE 编码器将邻接矩阵的一行作为输入（设置 $ s(\mathbf{W}) = \mathbf{W} $），并生成节点嵌入 $ \mathbf{Z} = \text{ENC}(\mathbf{W}; \theta^E) $。（注意这忽略了任何节点特征。）SDNE 解码器返回 $ \widehat{\mathbf{W}} = \text{DEC}(\mathbf{Z}; \Theta^D) $，即训练用于恢复原始图邻接矩阵的重构结果。SDNE 通过最小化以下损失来保留二阶节点邻近性：

$$  ||(s(\mathbf{W})-\widehat{\mathbf{W}})\cdot\mathbb{I}\left(s(\mathbf{W})>0\right)||_{F}^{2}+\alpha_{\mathrm{SDNE}}\sum_{ij}s(\mathbf{W})_{ij}||\mathbf{Z}_{i}-\mathbf{Z}_{j}||_{2}^{2}   \tag*{(23.30)}$$

第一项类似于矩阵分解正则化目标，不同之处在于 $ \tilde{W} $ 未使用外积计算。第二项用于基于距离的浅层嵌入方法。

---

##### 23.5.1.2 （变分）图自动编码器

Kipf 和 Welling [KW16b] 使用图卷积（参见第 23.4.2 节）来学习节点嵌入 $\mathbf{Z} = \text{GCN}(\mathbf{W}, \mathbf{X}; \Theta^E)$。解码器是一个外积：$\text{DEC}(\mathbf{Z}; \Theta^D) = \mathbf{Z}\mathbf{Z}^\top$。图重构项是真邻接矩阵与预测边相似度分数之间的 Sigmoid 交叉熵：

$$  \mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\Theta)=-\Bigg(\sum_{i,j}(1-\mathbf{W}_{i j})\log(1-\sigma(\widehat{\mathbf{W}}_{i j}))+\mathbf{W}_{i j}\log\sigma(\widehat{\mathbf{W}}_{i j})\Bigg).   \tag*{(23.31)}$$

对所有可能的节点对计算正则化项在实际中计算量很大，因此图自动编码器（GAE）模型采用负采样来克服这一困难。

GAE 是一个确定性模型，作者还引入了变分图自动编码器（VGAE），它依赖变分自动编码器（参见第 20.3.5 节）来编码和解码图结构。在 VGAE 中，嵌入 $\mathbf{Z}$ 被建模为一个潜在变量，其先验为标准多元正态分布 $p(\mathbf{Z}) = \mathcal{N}(\mathbf{Z}|\mathbf{0}, \mathbf{I})$，并使用图卷积作为摊销推理网络 $q_{\Phi}(\mathbf{Z}|\mathbf{W}, \mathbf{X})$。该模型通过最小化对应的负证据下界来训练：

$$  \mathrm{N E L B O}(\mathbf{W},\mathbf{X};\Theta)=-\mathbb{E}_{q_{\Phi}(\mathbf{Z}|\mathbf{W},\mathbf{X})}[\log p(\mathbf{W}|\mathbf{Z})]+\mathrm{K L}(q_{\Phi}(\mathbf{Z}|\mathbf{W},\mathbf{X})||p(\mathbf{Z}))   \tag*{(23.32)}$$

$$  =\mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\Theta)+\mathrm{K L}(q_{\Phi}(\mathbf{Z}|\mathbf{W},\mathbf{X})||p(\mathbf{Z})).   \tag*{(23.33)}$$

##### 23.5.1.3 图的迭代生成建模（Graphite）

[GZE19] 提出的 Graphite 模型通过引入更复杂的解码器来扩展 GAE 和 VGAE。该解码器在成对解码函数和图卷积之间迭代，具体如下：

 $$ \widehat{\mathbf{W}}^{(k)}=\frac{\mathbf{Z}^{(k)}\mathbf{Z}^{(k)^{\mathsf{T}}}}{||\mathbf{Z}^{(k)}||_{2}^{2}}+\frac{\mathbf{1}\mathbf{1}^{\mathsf{T}}}{N} $$ 

 $$ \mathbf{Z}^{(k+1)}=\mathrm{GCN}(\widehat{\mathbf{W}}^{(k)},\mathbf{Z}^{(k)}) $$ 

其中 $\mathbf{Z}^{(0)}$ 使用编码器网络的输出进行初始化。这一过程使 Graphite 能够学习更具表达力的解码器。最后，与 GAE 类似，Graphite 既可以是确定性的，也可以是变分的。

##### 23.5.1.4 基于对比损失的方法

$[\text{Vel}+19]$ 的深度图互信息最大化（Deep Graph Infomax, DGI）方法是一种类似 GAN 的方法，用于生成图级别的嵌入。给定一个或多个真实（正例）图，每个图有其邻接矩阵 $\mathbf{W} \in \mathbb{R}^{N \times N}$ 和节点特征 $\mathbf{X} \in \mathbb{R}^{N \times D}$，该方法创建假的（负例）邻接矩阵 $\mathbf{W}^- \in \mathbb{R}^{N^- \times N^-}$ 及其特征 $\mathbf{X}^- \in \mathbb{R}^{N^- \times D}$。它训练：（i）一个编码器，同时处理真实样本和假样本，分别得到 $\mathbf{Z} = \text{ENC}(\mathbf{X}, \mathbf{W}; \Theta^E) \in \mathbb{R}^{N \times L}$ 和 $\mathbf{Z}^- = \text{ENC}(\mathbf{X}^-, \mathbf{W}^-; \Theta^E) \in \mathbb{R}^{N^- \times L}$；（ii）一个（读出）图池化函数 $\mathcal{R} : \mathbb{R}^{N \times L} \to \mathbb{R}^L$；（iii）一个判别器函数 $\mathcal{D} : \mathbb{R}^L \times \mathbb{R}^L \to [0,1]$，它被训练为对于给定图的节点 $i \in V$ 输出 $\mathcal{D}(\mathbf{Z}_i, \mathcal{R}(\mathbf{Z})) \approx 1$，对于假图的节点 $j \in V^-$ 输出 $\mathcal{D}(\mathbf{Z}_j^-, \mathcal{R}(\mathbf{Z}^-)) \approx 0$。具体而言，DGI 优化以下目标：

---

$$  \min_{\Theta}-\underset{\mathbf{X},\mathbf{W}}{\mathbb{E}}\sum_{i=1}^{N}\log\mathcal{D}(\mathbf{Z}_{i},\mathcal{R}(\mathbf{Z}))-\underset{\mathbf{X}^{-},\mathbf{W}^{-}}{\mathbb{E}}\sum_{j=1}^{N^{-}}\log\left(1-\mathcal{D}(\mathbf{Z}_{j}^{-},\mathcal{R}(\mathbf{Z}^{-}))\right),   \tag*{(23.34)}$$

其中 $ \Theta $ 包含 $ \Theta^E $ 以及 $ \mathcal{R}, \mathcal{D} $ 的参数。在第一个期望中，DGI从真实（正）图中采样。如果只给出一个图，它可以从中采样一些子图（例如连通分量）。第二个期望对虚假（负）图进行采样。在DGI中，虚假样本使用真实的邻接矩阵 $ W^- := W $，但虚假特征 $ X^- $ 是真实 $ X $ 的逐行随机排列。DGI使用的ENC是图卷积网络，尽管任何GNN都可以使用。读出函数 $ \mathcal{R} $ 将整个（可变大小）图汇总为一个单一（固定维度）向量。Veličković 等人 [Vel+19] 使用逐行均值作为 $ \mathcal{R} $，但也可以使用其他图池化方法，例如那些考虑邻接矩阵的方法。

[Vel+19] 证明，式(23.34)的优化最大化编码器输出与图池化函数之间的互信息下界，即单个节点表示与图表示之间的互信息下界。

在 [Pen+20] 中，他们提出了一种称为图形互信息（Graphical Mutual Information）的变体。GMI不是最大化节点信息与整个图之间的互信息，而是最大化节点表示与其邻居之间的互信息。

#### 23.5.2 半监督嵌入

在本节中，我们讨论GNN的半监督损失。我们考虑一个简单的特例，即使用节点特征的非线性编码器，但忽略图结构，即使用 $ \mathbf{Z} = \text{ENC}(\mathbf{X}; \Theta^E) $。

##### 23.5.2.1 SemiEmb

[WRC08] 提出了一种称为半监督嵌入（SemiEmb）的方法。他们使用MLP作为X的编码器。对于解码器，我们可以使用基于距离的图解码器：$ \widehat{\mathbf{W}}_{ij} = \text{DEC}(\mathbf{Z}; \Theta^D)_{ij} = \|\mathbf{Z}_i - \mathbf{Z}_j\|_2^2 $，其中 $ \|\cdot\| $ 可以是L2或L1范数。

SemiEmb使用与式(23.19)中标签传播损失相同的正则化器对网络中的中间层或辅助层进行正则化。SemiEmb使用前馈网络从中间嵌入预测标签，然后使用Hinge损失将这些预测与真实标签进行比较。

##### 23.5.2.2 Planetoid

无监督skip-gram方法（如DeepWalk和node2vec）在多步骤流水线中学习嵌入，首先从图中生成随机游走序列，然后用它们来学习嵌入。这些嵌入可能不是下游分类任务的最优选择。[YCS16] 的Planetoid方法扩展了这类随机游走方法，以在嵌入算法中利用节点标签信息。

Planetoid首先使用神经网络（再次忽略图结构）将节点映射到嵌入 $ \mathbf{Z} = [\mathbf{Z}^c || \mathbf{Z}^F] = \text{ENC}(\mathbf{X}; \Theta^E) $。节点嵌入 $ \mathbf{Z}^c $ 捕获结构信息，而

---

节点嵌入 $\mathbf{Z}^F$ 捕获特征信息。存在两种变体：直推式版本直接学习 $\mathbf{Z}^c$（作为嵌入查找），以及归纳式模型，其中 $\mathbf{Z}^c$ 通过对输入特征 $\mathbf{X}$ 起作用的参数化映射计算得到。Planetoid 目标函数包含有监督损失和图正则化损失。图正则化损失衡量使用节点嵌入预测上下文的能力：

$$  \mathcal{L}_{G,\mathrm{R E C O N}}(\mathbf{W},\widehat{\mathbf{W}};\boldsymbol{\Theta})=-\mathbb{E}_{(i,j,\gamma)}\log\sigma\left(\gamma\widehat{\mathbf{W}}_{i j}\right),   \tag*{(23.35)}$$

其中 $\widehat{\mathbf{W}}_{ij} = \mathbf{Z}_i \mathbf{Z}_j^\top$，$\gamma \in \{-1, 1\}$，若 $(v_i, v_j) \in E$ 为正样本对则 $\gamma = 1$，若 $(v_i, v_j)$ 为负样本对则 $\gamma = -1$。期望下的分布直接通过采样过程定义。

Planetoid 中的有监督损失是预测正确标签的负对数似然：

$$  \mathcal{L}_{\mathrm{S U P}}^{N}(y^{N},\widehat{y}^{N};\Theta)=-\frac{1}{|V_{L}|}\sum_{i|v_{i}\in V_{L}}\sum_{1\leq k\leq C}y_{i k}^{N}\log\widehat{y}_{i k}^{N},   \tag*{(23.36)}$$

其中 $i$ 是节点索引，$k$ 表示标签类别，$\widehat{y}_{i}^{N}$ 使用神经网络后接 softmax 激活函数计算，将 $\mathbf{Z}_{i}$ 映射到预测标签。

### 23.6 应用

图嵌入有许多应用场景，包括无监督和有监督两种。下面几节给出一些例子。

#### 23.6.1 无监督应用

本节讨论常见的无监督应用。

##### 23.6.1.1 图重建

一种流行的无监督图应用是图重建。在此设置中，目标是学习将节点映射到能够重建图的流形上的映射函数（可以是参数化或非参数化的）。这被视为无监督，因为除了图结构外没有其他监督信息。模型可以通过最小化重建误差来训练，该误差是从学习到的嵌入中恢复原始图的误差。一些算法专门为此任务设计，重建目标函数的例子见第 23.3.1 节和第 23.5.1 节。从高层次看，图重建类似于降维，主要目标是将某些输入数据总结为低维嵌入。与标准降维方法（如 PCA）将高维向量压缩为低维向量不同，图重建模型的目标是将定义在图上的数据压缩为低维向量。

##### 23.6.1.2 链接预测

链接预测的目标是预测缺失或未观察到的链接（例如，在动态和时间网络中可能出现的未来链接）。链接预测还有助于识别虚假

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_274_141_895_543.jpg" alt="图像" width="53%" /></div>

<div style="text-align: center;">图 23.8：一些金融交易的图表示。改编自 http://pgql-lang.org/spec/1.2/。</div>

链接并进行移除。这是图学习模型在工业界的一项主要应用，常见的例子包括预测社交网络中的好友关系、推荐系统中的用户-产品交互、欺诈检测系统中的可疑链接（见图 23.8），或知识图谱中实体之间的缺失关系（例如，见 [Nic+15]）。

训练链接预测模型的一种常用方法是掩码图中的某些边（正边和负边），用剩余的边训练模型，然后在掩码的边集上进行测试。注意，**链接预测**不同于图重建。在链接预测中，我们旨在预测原始图中未观察到的链接，而在图重建中，我们仅想通过最小化重建误差来计算保留图结构的嵌入。

最后，尽管链接预测在有标签的边（正边、负边、未观察边）意义上与监督任务有相似之处，我们仍将其归入无监督应用类别，因为边标签通常在训练中不使用，仅用于衡量嵌入的预测质量。

##### 23.6.1.3 聚类

聚类对于发现社区结构尤为有用，并具有许多现实世界的应用。例如，聚类存在于生物网络（如具有相似性质的蛋白质组）或社交网络（如具有相似兴趣的人群组）中。

本章介绍的无监督方法可用于解决聚类问题。