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

<div style="text-align: center;"><img src="imgs/img_in_image_box_471_149_804_376.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图18.8：随机森林分类器的特征重要性，该分类器用于区分MNIST数字类别0和8。改编自[Gér19]的图7.6。由rf_feature_importance_mnist.ipynb生成。</div>


#### 18.6.1 特征重要性

对于单个决策树T，[BFO84]提出了以下用于特征k的特征重要性的度量：

$$  R_{k}(T)=\sum_{j=1}^{J-1}G_{j}\mathbb{I}\left(v_{j}=k\right)   \tag*{(18.57)}$$

其中求和覆盖所有非叶（内部）节点，$G_j$是节点$j$处的准确率增益（成本减少），如果节点$j$使用特征$k$，则$v_j=k$。通过对集成中所有树的平均，我们可以获得更可靠的估计：

$$  R_{k}=\frac{1}{M}\sum_{m=1}^{M}R_{k}(T_{m})   \tag*{(18.58)}$$

计算这些分数后，我们可以对其进行归一化，使最大值为100%。下面给出一些示例。

图18.8给出了一个示例，展示了一个为区分MNIST数字类别0和8而训练的分类器的特征重要性估计。我们看到，它关注的是这些类别之间图像中不同的部分。

在图18.9中，我们绘制了垃圾邮件数据集（第18.4节）中每个特征的相对重要性。毫不奇怪，我们发现最重要的特征是单词“george”（收件人姓名）和“hp”（他工作的公司），以及字符!和$。（注意，这些特征的存在或缺失都可能提供信息。）

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_394_139_765_631.jpg" alt="图片" width="32%" /></div>


<div style="text-align: center;">图18.9：训练用于区分垃圾邮件和非垃圾邮件的梯度提升分类器的特征重要性。该数据集有X个训练样本和Y个特征，对应词频。改编自[HTF09]的图10.6。由spam_tree_ensemble_interpret.ipynb生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_195_770_379_897.jpg" alt="图片" width="15%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_384_770_566_897.jpg" alt="图片" width="15%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_195_906_379_1035.jpg" alt="图片" width="15%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_383_906_567_1037.jpg" alt="图片" width="15%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_609_775_953_1034.jpg" alt="图片" width="29%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图18.10：(a) 四个重要预测因子的垃圾邮件类别对数几率的部分依赖图。图底部的红色刻度线是该特征经验分布的十分位数。(b) 特征 hp 和 ! 上对数比值的联合部分依赖图。改编自[HTF09]的图10.6–10.8。由spam_tree_ensemble_interpret.ipynb生成。</div>

---

#### 18.6.2 部分依赖图

在识别出最相关的输入特征后，我们可以尝试评估它们对输出的影响。特征 $k$ 的部分依赖图是以

$$  \overline{f}_{k}(x_{k})=\frac{1}{N}\sum_{n=1}^{N}f(\boldsymbol{x}_{n,-k},x_{k})   \tag*{(18.59)}$$

为纵轴、$x_k$ 为横轴绘制的图形。因此，我们除特征 $k$ 之外的所有特征进行边缘化处理。对于二分类器，我们可以在绘图前将其转换为对数几率 $\log p(y = 1|x_k)/p(y = 0|x_k)$。我们以垃圾邮件示例中的四个不同特征在图 18.10a 中展示这一方法。可以看到，随着 "!" 和 "remove" 的出现频率增加，垃圾邮件的概率也相应增加。相反，随着 "edu" 或 "hp" 的频率增加，垃圾邮件的概率则降低。

我们还可以通过计算

$$  \overline{f}_{jk}(x_{j},x_{k})=\frac{1}{N}\sum_{n=1}^{N}f(\boldsymbol{x}_{n,-jk},x_{j},x_{k})   \tag*{(18.60)}$$

来捕捉特征 $j$ 和 $k$ 之间的交互效应。我们在图 18.10b 中对垃圾邮件示例中的 "hp" 和 "!" 进行了展示。可以看到，"!" 的高频率会使邮件更可能是垃圾邮件，但如果缺少单词 "hp"，这种效应会更为显著。

---

（用户未提供需要翻译的文本，请提供英文学术论文的 Markdown 内容。）

---

第五部分

超越监督学习

---

好的，我明白了。我将按照您的要求，将英文学术论文的 Markdown 文本翻译为中文，保留所有非自然语言元素，确保术语统一、语言流畅。请提供需要翻译的文本。

---

# 19 使用更少标注样本的学习

许多机器学习模型，尤其是神经网络，其参数数量往往远多于我们拥有的标注训练样本数。例如，一个具有50层的ResNet CNN（第14.3.4节）有2300万个参数。Transformer模型（第15.5节）可能更大。当然，这些参数高度相关，因此它们不是独立的“自由度”。尽管如此，这类大模型训练缓慢，更重要的是，它们容易过拟合。当您没有大规模标注训练集时，这尤其成问题。在本章中，我们将讨论解决此问题的一些方法，除了我们在第13.5节中讨论的通用正则化技术（如早停、权重衰减和丢弃法）之外。

### 19.1 数据增强

假设我们只有一个小型标注数据集。在某些情况下，我们可以创建输入向量的人工修改版本，这些版本捕捉我们在测试时预期看到的各种变化，同时保持原始标签不变。这称为**数据增强**。$ ^{1} $ 下面我们给出一些例子，然后讨论该方法为何有效。

#### 19.1.1 示例

对于图像分类任务，标准的数据增强方法包括随机裁剪、缩放和镜像翻转，如图19.1所示。[GVZ16]给出了一个更复杂的例子，他们以逼真的方式将文本字符渲染到图像上，从而创建了一个非常大的“野外”文本数据集。他们利用该数据集训练了最先进的视觉文本定位与阅读系统。数据增强的其他例子包括：人为地向干净语音信号中添加背景噪声，以及人为地随机替换文本文档中的字符或单词。

如果我们有能力使用数据的不同版本多次训练和测试模型，我们可以使用黑箱优化方法（如强化学习（例如 [Cub+19]）或贝叶斯优化（例如 [Lim+19]））来学习哪种增强效果最好；这称为**自动增强**。我们还可以学习将多种增强组合在一起；这称为AutoAugment [Cub+19]。

关于NLP中增强的一些示例，请参见例如 [Fen+21]。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_177_135_362_321.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_389_135_576_320.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_601_135_789_320.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_814_135_1000_320.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;">图 19.1：左侧图像的随机裁剪和缩放示意图。由 image_augmentation_jax.ipynb 生成。</div>


#### 19.1.2 理论依据

数据增强通常能显著提升性能（如预测准确性、鲁棒性等）。乍看之下，这似乎是不劳而获，因为并未提供额外数据。然而，数据增强机制可视为一种算法层面注入先验知识的方法。

为理解这一点，回顾标准经验风险最小化（ERM，Empirical Risk Minimization）训练中，我们最小化经验风险

$$  R(f)=\int\ell(f(\boldsymbol{x}),\boldsymbol{y})p^{*}(\boldsymbol{x},\boldsymbol{y})d\boldsymbol{x}d\boldsymbol{y}   \tag*{(19.1)}$$

其中用经验分布近似 $p^{*}(\boldsymbol{x},\boldsymbol{y})$

$$  p_{\mathcal{D}}(\boldsymbol{x},\boldsymbol{y})=\frac{1}{N}\sum_{n=1}^{N}\delta(\boldsymbol{x}-\boldsymbol{x}_{n})\delta(\boldsymbol{y}-\boldsymbol{y}_{n})   \tag*{(19.2)}$$

可将数据增强视为用以下算法平滑后的分布代替经验分布

$$  p_{\mathcal{D}}(\boldsymbol{x},\boldsymbol{y}|A)=\frac{1}{N}\sum_{n=1}^{N}p(\boldsymbol{x}|\boldsymbol{x}_{n},A)\delta(\boldsymbol{y}-\boldsymbol{y}_{n})   \tag*{(19.3)}$$

其中 $A$ 是数据增强算法，它从训练样本 $\boldsymbol{x}_n$ 生成样本 $\boldsymbol{x}$，且不改变标签（“语义”）。一个非常简单的例子是高斯核 $p(\boldsymbol{x}|\boldsymbol{x}_n, A) = \mathcal{N}(\boldsymbol{x}|\boldsymbol{x}_n, \sigma^2 \mathbf{I})$。这被称为邻域风险最小化（Vicinal Risk Minimization）[Cha+01]，因为我们在每个训练点 $\boldsymbol{x}$ 的邻域内最小化风险。关于该视角的更多细节，参见 [Zha+17b; CDL19; Dao+19]。

### 19.2 迁移学习

本节由 Colin Raffel 合著。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_338_125_830_407.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图 19.2：在新数据集上微调模型的示意图。最终输出层从头开始训练，因为它可能对应不同的标签集合。其他层用之前的参数初始化，然后使用较小的学习率进行可选更新。来自 [Zha+20] 的图 13.2.1，经 Aston Zhang 许可使用。</div>


许多数据匮乏的任务与其他数据丰富的任务之间存在某些高层次的结构相似性。例如，考虑对濒危鸟类进行细粒度视觉分类的任务。由于濒危鸟类本身就罕见，不太可能拥有大量多样化的标注图像。然而，不同物种的鸟类在结构上有许多相似之处——例如，大多数鸟类都有翅膀、羽毛、喙、爪子等。因此，我们可能预期，先在非濒危鸟类的大数据集上训练一个模型，然后继续在濒危鸟类的小数据集上训练，能比仅在小数据集上训练获得更好的性能。

这被称为**迁移学习**，因为我们通过共享参数集将信息从一个数据集转移到另一个数据集。更准确地说，我们首先执行一个**预训练**阶段，在大规模源数据集 $ D_p $（可能带有标签或未标注）上训练一个参数为 $ \theta $ 的模型。然后，我们在感兴趣的小规模标注目标数据集 $ D_q $ 上执行第二个**微调**阶段。下面我们详细讨论这两个阶段，但更多信息可参阅最近的综述，例如 [\text{Tan}+18; Zhu+21]。

#### 19.2.1 微调

现在假设我们已经有一个预训练的分类器 $ p(y|\boldsymbol{x},\boldsymbol{\theta}_{p}) $（例如 CNN），它对于来自分布 $ p(\boldsymbol{x}, y) $（与训练时使用的分布相似）的输入 $ \boldsymbol{x} \in \mathcal{X}_p $（例如自然图像）和输出 $ y \in \mathcal{Y}_p $（例如 ImageNet 标签）表现良好。现在我们要创建一个新模型 $ q(y|\boldsymbol{x}, \boldsymbol{\theta}_q) $，对于来自分布 $ q(\boldsymbol{x}, y) $（可能与 $ p $ 不同）的输入 $ \boldsymbol{x} \in \mathcal{X}_q $（例如鸟类图像）和输出 $ y \in \mathcal{Y}_q $（例如细粒度鸟类标签）表现良好。

我们假设可能的输入集合相同，即 $ \mathcal{X}_q \approx \mathcal{X}_p $（例如两者都是 RGB 图像），或者我们可以轻松地将输入从域 $ p $ 转换到域 $ q $（例如，通过丢弃色度通道只保留亮度，可以将 RGB 图像转换为灰度图像）。（如果情况并非如此，

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_195_125_912_418.jpg" alt="图像" width="62%" /></div>


<div style="text-align: center;">图 19.3: (a) 在 transformer 中添加适配器层。来自 [Hou+19] 的图 2，经 Neil Houlsby 许可使用。(b) 在 resnet 中添加适配器层。来自 [RBV18] 的图 2，经 Sylvestre-Alvise Rebuffi 许可使用。</div>


在这种情况下，我们可能需要使用一种称为域适应的方法，该方法修改模型以在不同模态之间进行映射，如第 19.2.5 节所述。

然而，输出域通常是不同的，即 $ \mathcal{Y}_q \neq \mathcal{Y}_p $。例如，$ \mathcal{Y}_p $ 可能是 ImageNet 标签，而 $ \mathcal{Y}_q $ 可能是医学标签（例如糖尿病视网膜病变的类型 [Arc+19]）。在这种情况下，我们需要将预训练模型的输出“翻译”到新的域。使用神经网络很容易做到：我们只需“切除”原始模型的最后一层，并添加一个新的“头部”来建模新的类别标签，如图 19.2 所示。例如，假设 $ p(y|\boldsymbol{x}, \boldsymbol{\theta}_p) = \text{softmax}(y|\mathbf{W}_2\boldsymbol{h}(\boldsymbol{x}; \boldsymbol{\theta}_1) + \boldsymbol{b}_2) $，其中 $ \boldsymbol{\theta}_p = (\mathbf{W}_2, \boldsymbol{b}_2, \boldsymbol{\theta}_1) $。那么我们可以构建 $ q(y|\boldsymbol{\theta}_q) = \text{softmax}(y|\mathbf{W}_3\boldsymbol{h}(\boldsymbol{x}; \boldsymbol{\theta}_1) + \boldsymbol{b}_3) $，其中 $ \boldsymbol{\theta}_q = (\mathbf{W}_3, \boldsymbol{b}_3, \boldsymbol{\theta}_1) $，而 $ \boldsymbol{h}(\boldsymbol{x}; \boldsymbol{\theta}_1) $ 是共享的非线性特征提取器。

在执行了这种“模型手术”之后，我们可以用参数 $ \boldsymbol{\theta}_q = (\boldsymbol{\theta}_1, \boldsymbol{\theta}_3) $ 来微调新模型，其中 $ \boldsymbol{\theta}_1 $ 参数化特征提取器，$ \boldsymbol{\theta}_3 $ 参数化将特征映射到新标签集合的最终线性层。如果我们将 $ \boldsymbol{\theta}_1 $ 视为“冻结参数”，那么得到的模型 $ q(y|\boldsymbol{x}, \boldsymbol{\theta}_q) $ 在其参数上是线性的，因此我们面临一个凸优化问题，存在许多简单高效的求解方法（见第二部分）。这在长尾设置中尤其有用，因为某些类别非常罕见 [Kan+20]。然而，线性“解码器”可能过于受限，因此我们也可以允许 $ \boldsymbol{\theta}_1 $ 同时被微调，但使用较低的学习率，以防止参数值偏离在 $ \mathcal{D}_p $ 上估计的值太远。

#### 19.2.2 适配器

微调预训练模型所有参数的一个缺点是，它可能很慢，因为通常参数很多，并且我们可能需要使用较小的学习率，以防止低级特征提取器过度偏离其先验值。此外，每个新任务都需要训练一个新模型，这使得任务共享变得困难。另一种方法是保持预训练模型不变，但添加新参数来修改其内部行为，从而……

---

为每个任务定制特征提取过程。这一思想被称为适配器（adapters），已在多篇论文中得到探索（例如，[RBV17; RBV18; Hou+19]）。

图19.3a展示了[Hou+19]提出的用于变压器网络（第15.5节）的适配器。其基本思想是在每个Transformer层内部插入两个浅层瓶颈式MLP，一个放在多头注意力之后，另一个放在前馈层之后。注意，这些MLP带有跳跃连接，因此可以初始化为实现恒等映射。如果Transformer层的特征维度为 \(D\)，适配器使用大小为 \(M\) 的瓶颈，则每层引入 \(O(DM)\) 个新参数。这些适配器MLP以及层归一化参数和最终输出头，会针对每个新任务进行训练，但所有其余参数保持冻结。经验上，在多个NLP基准上，这种方法比微调表现更好，且仅需原始参数的约1-10%。

图19.3b展示了[RBV17; RBV18]提出的用于残差网络（第14.3.4节）的适配器。其基本思想是在CNN的内部层添加一个 \(1\times1\) 卷积层 \(\boldsymbol{\alpha}\)，这类似于Transformer情况下的MLP适配器。如图所示，该层可以串联或并联添加。如果我们将适配器层记为 \(\rho(\boldsymbol{x})\)，则串联适配器可定义为

$$  \rho(\boldsymbol{x})=\boldsymbol{x}+\mathrm{diag}_{1}(\boldsymbol{\alpha})\circledast\boldsymbol{x}=\mathrm{diag}_{1}(\mathbf{I}+\boldsymbol{\alpha})\circledast\boldsymbol{x}   \tag*{(19.4)}$$

其中 \(\text{diag}_1(\boldsymbol{\alpha}) \in \mathbb{R}^{1 \times 1 \times C \times D}\) 将矩阵 \(\boldsymbol{\alpha} \in \mathbb{R}^{C \times D}\) 重塑为可并行应用于每个空间位置的矩阵（为简化起见，我们省略了批归一化）。如果我们将它插入常规卷积层 \(\boldsymbol{f} \otimes \boldsymbol{x}\) 之后，得到

$$  \boldsymbol{y}=\rho(\boldsymbol{f}\circledast\boldsymbol{x})=(\operatorname{diag}_{1}(\mathbf{I}+\boldsymbol{\alpha})\circledast\boldsymbol{f})\circledast\boldsymbol{x}   \tag*{(19.5)}$$

这可以解释为对原始滤波器 \(\boldsymbol{f}\) 的低秩乘法扰动。并联适配器可定义为

$$  y=f\circledast x+\mathrm{diag}_{1}(\boldsymbol{\alpha})\circledast x=(f+\mathrm{diag}_{L}(\boldsymbol{\alpha}))\circledast x   \tag*{(19.6)}$$

这可以解释为对原始滤波器 \(\mathbf{f}\) 的低秩加法扰动。在两种情况下，设置 \(\boldsymbol{\alpha} = \mathbf{0}\) 可确保适配器层初始化为恒等变换。此外，两种方法每层都需要 \(O(C^2)\) 个参数。

#### 19.2.3 监督预训练

预训练任务可以是监督的或无监督的；主要要求是，它能教会模型关于问题领域的基本结构，并且与下游微调任务足够相似。任务相似性这一概念没有严格定义，但在实践中，预训练任务的领域通常比微调任务的领域更宽泛（例如，在所有鸟类物种上预训练，在濒危物种上微调）。

迁移学习最直接的形式是使用大型标注数据集进行预训练。例如，使用ImageNet数据集（第1.5.1.2节）预训练CNN非常常见，然后可将其用于各种下游任务和数据集（例如，参见[Kol+19]）。ImageNet包含128万张自然图像，每张图像关联一个来自1000个类别的标签。这些类别涵盖了广泛的不同概念，包括动物、食物、建筑、乐器、服装等。图像本身在意义上也具有多样性

---

它们包含来自多种角度、多种尺寸、背景多样的物体。这种多样性和规模可能部分解释了它为何成为计算机视觉迁移学习中事实上的预训练任务。（示例代码见 finetune_cnn_jax.ipynb。）

然而，当微调任务的领域与自然图像差异较大时（例如医学图像 [Rag+19]），ImageNet 预训练被证明帮助不大；而在某些有帮助的情况下（例如训练目标检测系统），它似乎更像是一种加速技巧（通过在良好点进行暖启动优化），而非必要手段，因为如果训练时间足够长，从头训练也能在下游任务上达到相当的性能 [HGD19]。

有监督预训练在非视觉应用中较为少见。一个显著的例外是在自然语言推理数据（即判断一个句子是否蕴含或矛盾另一个句子）上进行预训练以学习句子向量表示 [Con+17]，不过这种方法在很大程度上已被无监督方法所取代（第19.2.4节）。另一个迁移学习的非视觉应用是在大型英文标注语料库上预训练语音识别模型，再对低资源语言进行微调 [Ard+20]。

#### 19.2.4 无监督预训练（自监督学习）

使用无监督预训练越来越普遍，因为无标签数据通常容易获取，例如来自网络的无标签图像或文本文档。

在短时期内，常见做法是在进行标准有监督训练之前，使用无监督目标（例如重建误差，详见第20.3节）对有标签数据集（即忽略标签）进行深度神经网络预训练 [HOT06; Vin+10b; Erh+10]。尽管该技术也被称为无监督预训练，但它与本节讨论的用于迁移学习的预训练形式不同，后者使用（大型）无标签数据集进行预训练，然后在不同（较小）的有标签数据集上进行微调。

使用无标签数据的预训练任务通常被称为 **自监督** 而非无监督。这一术语的使用是因为标签由算法自行生成，而非像标准有监督学习那样由人类外部提供。有监督学习和自监督学习都是判别性任务，因为它们需要根据输入预测输出。相反，其他无监督方法（例如第20章中讨论的一些方法）是生成性的，因为它们无条件地预测输出。

已有许多不同的自监督学习启发式方法被尝试过（例如，综述见 [GR18; JT19; Ren19]，以及论文列表见 https://github.com/jason718/awesome-self-supervised-learning）。我们至少可以识别出三大类，下面进行讨论。

##### 19.2.4.1 填补任务

一种自监督学习方法是通过解决 \textit{填补} 任务来实现。在该方法中，我们将输入向量 $ \boldsymbol{x} $ 划分为两部分，$ \boldsymbol{x} = (\boldsymbol{x}_h, \boldsymbol{x}_v) $，然后尝试根据可见部分 $ \boldsymbol{x}_v $ 预测隐藏部分 $ \boldsymbol{x}_h $，使用形如 $ \hat{\boldsymbol{x}}_h = f(\boldsymbol{x}_v, \boldsymbol{x}_h = \boldsymbol{0}) $ 的模型。我们可以将其视为“填空”任务；在自然语言处理社区中，这被称为 \textit{完形填空} 任务。视觉示例见图19.4，NLP示例见第15.7.2节。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_119_952_283.jpg" alt="图像" width="66%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图19.4: (a) 用于自监督学习的上下文编码器。引自 $ [Pat+16] $，经Deepak Pathak许可使用。(b) 自监督学习的其他一些代理任务。引自 $ [LeC18] $，经Yann LeCun许可使用。</div>


##### 19.2.4.2 代理任务

SSL的另一种方法是解决代理任务（也称为前置任务）。在这种设置中，我们创建输入对 $ (x_1, x_2) $，然后训练一个形式为 $ p(y|x_1, x_2) = p(y|r[f(x_1), f(x_2)]) $ 的孪生网络分类器（图16.5a），其中 $ f(x) $ 是执行“表示学习”[BCV13] 的某种函数，$ y $ 是捕捉 $ x_1 $ 与 $ x_2 $ 之间关系的标签，由 $ r(f_1, f_2) $ 预测。例如，假设 $ x_1 $ 是一个图像块，$ x_2 = t(x_1) $ 是我们控制的某种变换（如随机旋转）；那么我们将 $ y $ 定义为所使用的旋转角度[GSK18]。

##### 19.2.4.3 对比任务

当前最流行的自监督学习方法使用各种类型的对比任务。其基本思想是通过数据增强方法（第19.1节）创建语义相似的样本对，然后确保它们的表示在嵌入空间中的距离比两个无关样本之间的距离更近。这与深度度量学习（第16.2.2节）中使用的思想完全相同——唯一的区别在于算法自行创建相似对，而非依赖外部提供的相似度度量（如标签）。我们在第19.2.4.4节和第19.2.4.5节中给出了一些示例。

##### 19.2.4.4 SimCLR

在本节中，我们讨论SimCLR，即“视觉表示的简单对比学习”[Che+20b; Che+20c]。该方法在迁移学习和半监督学习上展示了最先进的性能。其基本思想如下：每个输入 $ \boldsymbol{x} \in \mathbb{R}^D $ 被转换为两个增强的“视图” $ \boldsymbol{x}_1 = t_1(\boldsymbol{x}) $、$ \boldsymbol{x}_2 = t_2(\boldsymbol{x}) $，它们是通过某些变换 $ t_1, t_2 $ 生成的输入“语义等价”版本。例如，若 $ \boldsymbol{x} $ 为图像，这些可以是图像的微小扰动（如随机裁剪），详见第19.1节。此外，我们从数据集中采样“负”样本 $ \boldsymbol{x}_1^- $, ..., $ \boldsymbol{x}_n^-\in N(\boldsymbol{x}) $，代表“语义不同”的图像（实践中为小批量中的其他样本）。接着定义某个特征映射 $ F : \mathbb{R}^D \to \mathbb{R}^E $，其中 $ D $ 为输入的大小，$ E $ 为嵌入的大小。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_170_157_477_392.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_510_226_678_392.jpg" alt="图像" width="14%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_787_227_956_393.jpg" alt="图像" width="14%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 19.5: (a) SimCLR 训练示意图。T 是一组保持语义的随机变换（数据增强）。(b-c) 随机裁剪优势的说明。实线矩形表示原始图像，虚线矩形表示随机裁剪。在 (b) 中，模型被迫从全局视图 B 预测局部视图 A（反之亦然）。在 (c) 中，模型被迫预测相邻视图 (C, D) 的外观。摘自 [Che+20b] 的图 2–3。经 Ting Chen 许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_199_649_554_982.jpg" alt="图像" width="30%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_624_642_935_981.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 19.6: SimCLR 训练可视化。小批量中的每个输入图像被随机以两种不同方式修改（使用裁剪（随后调整大小）、翻转和颜色失真），然后输入到孪生网络。源自同一图像的每一对嵌入（最后一层）被迫靠近，而所有其他对的嵌入被迫远离。来自 https://ai.googleblog.com/2020/04/advancing-self-supervised-and-semi.html。经 Ting Chen 许可使用。</div>

---

接着，我们试图对于每个输入 x，最大化相似视图的相似性，同时最小化不同视图的相似性：

$$  J=F(t_{1}(\boldsymbol{x}))^{\top}F(t_{2}(\boldsymbol{x}))-\log\sum_{\boldsymbol{x}_{i}^{-}\in N(\boldsymbol{x})}\exp\left[F(\boldsymbol{x}_{i}^{-})^{\top}F(t_{1}(\boldsymbol{x}))\right]   \tag*{(19.7)}$$

在实践中，我们使用余弦相似度，因此在对表示进行内积之前，先对 F 产生的表示进行 $\ell_2$ 归一化，但在上述公式中省略了这一步骤。具体说明见图 19.5a。（在该图中，我们假设 $F(\boldsymbol{x}) = g(r(\boldsymbol{x}))$，其中中间表示 $\boldsymbol{h} = r(\boldsymbol{x})$ 将在后续用于微调，而 $g$ 是训练过程中额外施加的变换。）

有趣的是，我们可以将此解释为一种条件能量基模型，其形式为

$$  p(\boldsymbol{x}_{2}|\boldsymbol{x}_{1})=\frac{\exp[-\mathcal{E}(\boldsymbol{x}_{2}|\boldsymbol{x}_{1})]}{Z(\boldsymbol{x}_{1})}   \tag*{(19.8)}$$

其中 $\mathcal{E}(\boldsymbol{x}_2|\boldsymbol{x}_1) = -F(\boldsymbol{x}_2)^\top F(\boldsymbol{x}_1)$ 是能量，而

$$  Z(\boldsymbol{x})=\int\exp[-\mathcal{E}(\boldsymbol{x}^{-}|\boldsymbol{x})]d\boldsymbol{x}^{-}=\int\exp[F(\boldsymbol{x}^{-})^{\top}F(\boldsymbol{x})]d\boldsymbol{x}^{-}   \tag*{(19.9)}$$

是归一化常数，也称为配分函数。在该模型下，条件对数似然的形式为

$$  \log p(\boldsymbol{x}_{2}|\boldsymbol{x}_{1})=F(\boldsymbol{x}_{2})^{\top}F(\boldsymbol{x}_{1})-\log\int\exp[F(\boldsymbol{x}^{-})^{\top}F(\boldsymbol{x}_{1})]d\boldsymbol{x}^{-}   \tag*{(19.10)}$$

它与公式 (19.7) 的唯一区别在于，我们使用基于负样本推导出的蒙特卡洛上界来替代积分。因此，我们可以将对比学习视为对条件能量基生成模型 [Gra+20] 的近似最大似然估计。有关此类模型的更多细节，可参见本书的续篇 [Mur23]。

SimCLR 成功的一个关键因素是数据增强方法的选择。通过使用随机裁剪，他们可以强制模型从全局视图预测局部视图，以及预测同一图像的相邻视图（见图 19.5）。裁剪后，所有图像都被调整回相同的大小。此外，他们还在部分时间随机翻转图像。$^{2}$

SimCLR 依赖于大批量训练，以确保有足够多样化的负样本集。当这无法实现时，我们可以使用一个由过去（负）嵌入组成的存储库，该存储库可通过指数移动平均（第 4.4.2.2 节）进行更新。这被称为动量对比学习或 MoCo [He+20]。

##### 19.2.4.5 CLIP

在本节中，我们描述 CLIP，它代表“对比语言-图像预训练” [Rad+]。这是一种对比性的表示学习方法，它使用一个庞大的语料库

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_186_121_982_426.jpg" alt="图像" width="69%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图19.7：CLIP模型示意图。来自 $ [Rad^{+}] $ 的图1。经Alec Radford许可使用。</div>


从网络提取了4亿对（图像，文本）数据。设 $ \pmb{x}_{i} $ 为第 $ i $ 张图像，$ \pmb{y}_{i} $ 为其匹配文本。相比于试图预测与图像关联的确切单词，更简单的方法是仅判断，对于小批量中的其他文本字符串 $j$，$\pmb{y}_{i}$ 是否比 $\pmb{y}_{j}$ 更可能是正确的文本。类似地，模型可以尝试判断，对于给定文本 $ \pmb{y}_{i} $，图像 $ \pmb{x}_{i} $ 是否比 $ \pmb{x}_{j} $ 更可能是匹配的。

更精确地，令 $ \mathbf{f}_I(\mathbf{x}_i) $ 为图像的嵌入，$ \mathbf{f}_T(\mathbf{y}_j) $ 为文本的嵌入，$ \mathbf{I}_i = \mathbf{f}_I(\mathbf{x}_i)/||\mathbf{f}_I(\mathbf{x}_i)||_2 $ 为图像嵌入的单位范数版本，$ \mathbf{T}_j = \mathbf{f}_T(\mathbf{y}_j)/||\mathbf{f}_T(\mathbf{y}_j)||_2 $ 为文本嵌入的单位范数版本。定义成对logits（相似度分数）向量为：

$$  L_{i j}=\mathbf{I}_{i}^{\mathsf{T}}\mathbf{T}_{j}   \tag*{(19.11)}$$

现在我们训练两个嵌入函数 $ f_I $ 和 $ f_T $ 的参数，以最小化以下损失，该损失在大小为 $ N $ 的小批量上平均：

$$  J=\frac{1}{2}\left[\sum_{i=1}^{N}CE(\mathbf{L}_{i,:},\mathbf{1}_{i})+\sum_{j=1}^{N}CE(\mathbf{L}_{:,j},\mathbf{1}_{j})\right]   \tag*{(19.12)}$$

其中CE是交叉熵损失

$$  \mathrm{CE}(\boldsymbol{p},\boldsymbol{q})=-\sum_{k=1}^{K}p_{k}\log q_{k}   \tag*{(19.13)}$$

而 $ 1_{i} $ 是标签 i 的独热编码。参见 Figure 19.7a 中的示意图。（在实践中，归一化的嵌入会乘以一个温度参数，该参数也是学习得到的；这控制了softmax的尖锐程度。）

---

在他们的论文中，作者考虑了使用 ResNet（第 14.3.4 节）和视觉 Transformer（第 15.5.6 节）来建模函数 $ f_I $，并使用文本 Transformer（第 15.5 节）来建模 $ f_T $。他们采用了非常大的小批量，大小为 $ N \sim 32k $，并在数百个 GPU 上训练了数天。

模型训练完成后，可用于对图像 $ \mathbf{x} $ 进行零样本分类，具体步骤如下。首先，将给定数据集的 K 个可能的类别标签分别转换为可能在网络上出现的文本字符串 $ y_k $。例如，“狗”变成“一张狗的照片”。其次，计算归一化嵌入 $ \mathbf{I} \propto f_I(\mathbf{x}) $ 和 $ \mathbf{T}_k \propto f_T(\mathbf{y}_k) $。第三，计算 softmax 概率

$$  p(y=k|\boldsymbol{x})=\operatorname{softmax}([\mathbf{I}^{\mathsf{T}}\mathbf{T}_{1},\dots,\mathbf{I}^{\mathsf{T}}\mathbf{T}_{k}])_{k}   \tag*{(19.14)}$$

图 19.7b 对此进行了说明。（视觉 n-gram 论文 [Li+17] 中也采用了类似的方法。）

值得注意的是，这种方法在 ImageNet 分类等任务上的表现可以与标准监督学习相媲美，而无需在特定的标注数据集上显式训练。当然，ImageNet 中的图像来自网络，并且是通过基于文本的网络搜索找到的，因此模型之前已经见过类似的数据。尽管如此，它对新任务的泛化能力以及对分布偏移的鲁棒性仍然令人印象深刻（具体示例见原论文）。

然而，该方法的一个缺点是它对类别标签转换为文本形式的方式很敏感。例如，为了使模型在食物分类任务上有效，需要使用诸如“一张鳄梨酱的照片，一种食物”、“一张酸橘汁腌鱼的照片，一种食物”等形式的文本字符串。诸如“一种食物”之类的消歧短语目前是按数据集手动添加的。这被称为**提示工程**，之所以需要这样做，是因为原始类别名称在数据集之间（有时甚至在数据集内部）可能存在歧义。

#### 19.2.5 域自适应

考虑一个输入来自不同域的问题，例如源域 $ \mathcal{X}_s $ 和目标域 $ \mathcal{X}_t $，但输出标签集合 $ \mathcal{Y} $ 是共同的。（这是迁移学习的“对偶”问题，因为输入域不同，但输出域相同。）例如，域可能是计算机图形系统的图像和真实图像，或者产品评论和电影评论。我们假设目标域中没有标注样本。我们的目标是在源域上拟合模型，然后修改其参数，使其能在目标域上工作。这被称为（无监督）**域自适应**（参见例如 [KL21] 的综述）。

解决此问题的一种常用方法是训练源域分类器，使其无法区分输入来自源域还是目标域分布；在这种情况下，它将只能使用两个域共同的特征。这被称为**域对抗学习** [Gan+16]。更形式化地，设 $ d_n \in \{s, t\} $ 是一个标签，指示数据样本 $ n $ 来自域 $ s $ 还是 $ t $。我们优化以下目标：

$$  \min_{\phi}\max_{\boldsymbol{\theta}}\frac{1}{N_{s}+N_{t}}\sum_{n\in\mathcal{D}_{s},\mathcal{D}_{t}}\ell(d_{n},f_{\boldsymbol{\theta}}(\boldsymbol{x}_{n}))+\frac{1}{N_{s}}\sum_{m\in\mathcal{D}_{s}}\ell(y_{m},g_{\phi}(f_{\boldsymbol{\theta}}(\boldsymbol{x}_{m})))   \tag*{(19.15)}$$

其中 $ N_s = |\mathcal{D}_s| $，$ N_t = |\mathcal{D}_t| $，$ f $ 将 $ \mathcal{X}_s \cup \mathcal{X}_t $ 映射到 $ \mathcal{H} $，$ g $ 将 $ \mathcal{H} $ 映射到 $ \mathcal{Y}_t $。公式 (19.15) 中的目标最小化分类 $ y $ 这一目标任务上的损失，但最大化分类源域 $ d $ 这一辅助任务上的损失。这可以通过梯度符号反转技巧实现，并且与生成对抗网络（GAN）相关。关于域自适应的其他方法，可参见例如 [Csu17; Wu+19]。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_230_115_952_361.jpg" alt="图像" width="62%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 19.8：半监督学习在二分类问题中的优势示意图。来自每个类别的标记点分别显示为黑色和白色圆圈。(a) 仅根据标记数据可能学到的决策边界。(b) 如果我们还有大量未标记数据点（显示为较小的灰色圆圈）可能学到的决策边界。</div>


### 19.3 半监督学习

##### 本节由 Colin Raffel 合著。

近年来，许多成功的机器学习应用都属于监督学习场景，其中需要大量带标签的样本数据集来训练模型。然而，在许多实际应用中，获取这类带标签的数据成本高昂。以自动语音识别为例：现代数据集包含数千小时的录音 [Pan+15; Ard+20]。对录音中口语词汇进行标注的过程比实时慢很多倍，可能导致漫长（且昂贵）的标注流程。更糟糕的是，在某些应用中，数据必须由专家（如医疗应用中的医生）进行标注，这进一步增加了成本。

半监督学习通过利用未标记数据，可以减轻对标记数据的需求。半监督学习的总体目标是让模型能够从未标记数据中学习数据分布的高层结构，而仅依靠标记数据来学习给定任务的细粒度细节。在标准监督学习中，我们假设可以访问数据与标签的联合分布样本 $ \boldsymbol{x}, y \sim p(\boldsymbol{x}, y) $，而半监督学习假设我们额外可以访问 $\boldsymbol{x}$ 的边缘分布样本，即 $ \boldsymbol{x} \sim p(\boldsymbol{x}) $，如图 19.8 所示。此外，通常假设我们拥有更多的未标记样本，因为获取这些样本通常更便宜。继续以自动语音识别为例，简单记录人们说话（产生未标记数据）通常比转录录音便宜得多。半监督学习非常适用于已收集大量未标记数据、且实践者希望避免标注所有数据的情景。

#### 19.3.1 自训练与伪标签

自训练是一种早期且直接的半监督学习方法 [Scu65; Agr70; McL75]。自训练背后的基本思想是使用模型本身来推断未标记上的预测

---

数据，然后将这些预测作为后续训练的标签。自训练因其简单性和通用适用性而一直作为一种半监督学习方法存在；即它适用于任何能够为未标注数据生成预测的模型。近年来，将这种方法称为“伪标签”[Lee13]已变得常见，因为与监督学习中使用的真实、准确的标注目标相比，为未标注数据推断出的标签仅是“伪正确”的。

在算法上，自训练通常采用以下两种流程之一。第一种方法首先为整个未标注数据集合预测伪标签，然后在标注数据和（伪标签）未标注数据的组合上重新训练模型（可能从头开始）直至收敛。接着，由模型重新对未标注数据进行标注，该过程不断重复直至找到合适的解。第二种方法则不断在随机选取的未标注数据批次上生成预测，并立即用这些伪标签训练模型。这两种方法目前在实践中都很常见；第一种“离线”变体在利用大规模未标注数据集合时已被证明特别有效[Yal+19; Xie+20]，而“在线”方法常被用作更复杂半监督学习方法的一个组成部分[Soh+20]。两种变体在根本上并无优劣之分。离线自训练可能导致模型基于“过时”的伪标签进行训练，因为这些标签仅在每次模型收敛时更新。然而，在线伪标签可能会带来更大的计算开销，因为它涉及不断“重新标注”未标注数据。

自训练存在一个明显的问题：如果模型为未标注数据生成了错误的预测，然后在这些错误预测上重新训练，它在目标任务上的表现可能会逐渐变差，直至最终学到完全无效的解。这个问题被称为**确认偏差**[TV17]，因为模型在不断确认其自身关于决策规则的（错误）偏差。

缓解确认偏差的一种常见方法是使用“选择度量”[RHS05]，它启发式地尝试仅保留正确的伪标签。例如，假设模型为每个可能的类别输出概率，一种常用的选择度量是仅保留最大类别概率超过某个阈值的伪标签[Yar95; RHS05]。如果模型的类别概率估计校准良好，那么这种选择度量将仅保留极有可能正确（至少根据模型判断）的标签。可以根据问题领域设计更复杂的选择度量。

#### 19.3.2 熵最小化

自训练具有促使模型输出低熵（即高置信度）预测的隐含效果。这种效果在使用交叉熵损失的在线设置中最为明显，此时模型在未标注数据上最小化以下损失函数 L：

$$  \mathcal{L}=-\max_{c}\log p_{\theta}(y=c|\boldsymbol{x})   \tag*{(19.16)}$$

其中 $ p_{\theta}(y|\boldsymbol{x}) $ 是模型在给定输入 $ \boldsymbol{x} $ 下的类别概率分布。当模型将其所有类别概率分配给单一类别 $ c^{*} $ 时，即 $ p(y = c^{*} | \boldsymbol{x}) = 1 $ 且 $ p(y \neq c^{*} | \boldsymbol{x}) = 0 $，该函数最小化。

一种密切相关的半监督学习方法是**熵最小化**[GB05]，它

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_431_126_747_323.jpg" alt="图片" width="27%" /></div>


<div style="text-align: center;">图 19.9：对于二分类问题，熵最小化、自训练和“锐化”熵最小化损失函数的比较。</div>


最小化如下损失函数：

$$  \mathcal{L}=-\sum_{c=1}^{C}p_{\theta}(y=c|\boldsymbol{x})\log p_{\theta}(y=c|\boldsymbol{x})   \tag*{(19.17)}$$

注意，当模型将所有类别概率分配给单个类别时，该函数也被最小化。我们可以通过将方程 (19.17) 中的第一个 $p_{\theta}(y = c|\mathbf{x})$ 项替换为一个“独热”向量（该向量将概率 1 分配给被赋予最高概率的类别），从而使得方程 (19.17) 中的熵最小化损失与方程 (19.16) 中的在线自训练损失等价。换句话说，在线自训练最小化的是模型输出与“硬”目标 $\arg\max p_{\theta}(y|\mathbf{x})$ 之间的交叉熵，而熵最小化使用的是“软”目标 $p_{\theta}(y|\mathbf{x})$。在这两个极端之间进行权衡的一种方法是调整目标分布的“温度”：将每个概率提高到 $1/T$ 次幂并进行重新归一化；这是 [Ber+19b; Ber+19a; Xie+19] 中 mixmatch 方法的基础。当 $T = 1$ 时，这等价于熵最小化；当 $T \to 0$ 时，它变为硬在线自训练。这些损失函数的比较如图 19.9 所示。

##### 19.3.2.1 聚类假设

为什么熵最小化是一个好主意？许多半监督学习方法的一个基本假设是，类别之间的决策边界应位于数据流形的低密度区域。这实际上假设了不同类别的数据是聚类在一起的。因此，一个好的决策边界不应穿过聚类，而应仅仅分离它们。利用“聚类假设”的半监督学习方法可以理解为：使用未标记数据来估计数据流形的形状，并将决策边界从其附近移开。

熵最小化就是其中一种方法。要理解这一点，首先假设两个类别之间的决策边界是“平滑的”，即模型在其域内的任何位置都不会突然改变其类别预测。对于简单模型和/或正则化模型，这一假设在实践中成立。在这种情况下，如果决策边界穿过数据的高密度区域，它必然会为数据分布中的某些样本产生高熵预测。因此，熵最小化将促使模型将其决策边界置于输入空间的低密度区域，从而

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_218_119_544_336.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_627_118_952_337.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图19.10：可视化展示熵最小化如何强化聚类假设。分类器在红色或蓝色区域分别将更高概率分配给类别1（黑点）或类别2（白点）。条形图显示了某个特定未标注数据点的预测类别概率。在(a)中，决策边界穿过数据的高密度区域，因此分类器被迫输出高熵预测。在(b)中，分类器避开高密度区域，能够为大部分未标注数据分配低熵预测。</div>


避免在可能采样到数据的空间区域中从一个类别过渡到另一个类别。该行为的可视化如图19.10所示。

##### 19.3.2.2 输入-输出互信息

Bridle、Heading和MacKay [BHM92] 提出了熵最小化目标的另一种理论依据，他们表明该目标自然源于最大化数据与标签（即模型的输入与输出）之间的互信息（第6.3节）。记 x 为输入，y 为目标，则输入-输出互信息可写为

$$  \mathcal{I}(y;\boldsymbol{x})=\iint p(y,\boldsymbol{x})\log\frac{p(y,\boldsymbol{x})}{p(y)p(\boldsymbol{x})}d y d\boldsymbol{x}   \tag*{(19.18)}$$

$$  =\iint p(y|\boldsymbol{x})p(\boldsymbol{x})\log\frac{p(y,\boldsymbol{x})}{p(y)p(\boldsymbol{x})}dyd\boldsymbol{x}   \tag*{(19.19)}$$

$$  =\int p(\boldsymbol{x})\int p(y|\boldsymbol{x})\log\frac{p(y|\boldsymbol{x})}{p(y)}dyd\boldsymbol{x}   \tag*{(19.20)}$$

$$  =\int p(\boldsymbol{x})\int p(y|\boldsymbol{x})\log\frac{p(y|\boldsymbol{x})}{\int p(\boldsymbol{x})p(y|\boldsymbol{x})d\boldsymbol{x}}d y d\boldsymbol{x}   \tag*{(19.21)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

请注意，第一个积分等价于对 \( x \) 求期望，而第二个积分等价于对所有可能的类别 \( y \) 求和。利用这些关系，我们得到

$$  \mathcal{I}(y;\boldsymbol{x})=\mathbb{E}_{\boldsymbol{x}}\left[\sum_{i=1}^{L}p(y_{i}|\boldsymbol{x})\log\frac{p(y_{i}|\boldsymbol{x})}{\mathbb{E}_{\boldsymbol{x}}[p(y_{i}|\boldsymbol{x})]}\right]   \tag*{(19.22)}$$

$$  =\mathbb{E}_{\boldsymbol{x}}\left[\sum_{i=1}^{L}p(y_{i}|\boldsymbol{x})\log p(y_{i}|\boldsymbol{x})\right]-\mathbb{E}_{\boldsymbol{x}}\left[\sum_{i=1}^{L}p(y_{i}|\boldsymbol{x})\log\mathbb{E}_{\boldsymbol{x}}[p(y_{i}|\boldsymbol{x})]\right]   \tag*{(19.23)}$$

$$  =\mathbb{E}_{\mathbf{x}}\left[\sum_{i=1}^{L}p(y_{i}|\mathbf{x})\log p(y_{i}|\mathbf{x})\right]-\sum_{i=1}^{L}\mathbb{E}_{\mathbf{x}}[p(y_{i}|\mathbf{x})\log\mathbb{E}_{\mathbf{x}}[p(y_{i}|\mathbf{x})]]   \tag*{(19.24)}$$

由于我们最初的目标是最大化互信息，而通常我们是要最小化损失函数，因此可以通过取负值将其转化为合适的损失函数：

$$  \mathcal{L}(y;\boldsymbol{x})=-\mathbb{E}_{\boldsymbol{x}}\left[\sum_{i=1}^{L}p(y_{i}|\boldsymbol{x})\log p(y_{i}|\boldsymbol{x})\right]+\sum_{i=1}^{L}\mathbb{E}_{\boldsymbol{x}}[p(y_{i}|\boldsymbol{x})\log\mathbb{E}_{\boldsymbol{x}}[p(y_{i}|\boldsymbol{x})]]   \tag*{(19.25)}$$

第一项恰好是期望形式下的**熵最小化**目标。第二项指定我们应最大化期望类别预测的熵，即训练集上平均类别预测的熵。这促使模型以等概率预测每个可能的类别，但仅当我们先验地知道所有类别等可能时，这种做法才是合适的。

#### 19.3.3 协同训练

协同训练 [BM98] 也与自训练类似，但额外假设数据存在两个互补的“视图”（即独立的特征集），每个视图均可单独用于训练一个合理的模型。分别在每个视图上训练两个模型后，每个模型对未标注数据进行分类以获得候选伪标签。如果某个伪标签从一个模型得到低熵预测（表示高置信度），而从另一个模型得到高熵预测（表示低置信度），则该伪标签数据点被加入低置信度模型的训练集。然后，使用新的、更大的训练数据集重复这一过程。这种只保留其中一个模型置信度高的伪标签的做法，理想情况下能通过正确标注的数据逐步扩充训练集。

协同训练假设数据存在两个信息丰富且相互独立的视图，这一强假设对许多问题不一定成立。**三重训练**算法 [ZL05] 通过使用三个模型来规避这一问题：这三个模型首先在从标注数据中独立采样（有放回）的子集上训练。理想情况下，在不同标注数据集合上的初始训练使得模型在预测时不会总是一致。随后，三个模型各自独立地为未标注数据生成伪标签。对于给定的未标注数据点，如果其中两个模型对其伪标签达成一致，则将该数据点加入第三个模型的训练集。这可以看作一种选择标准，因为它只保留了两个（不同初始化的）模型对正确标签达成一致的伪标签。然后，模型在标注数据和新伪标签的组合上重新训练，整个流程迭代重复。

---

#### 19.3.4 图上的标签传播

如果两个数据点在某种有意义的方式下“相似”，我们可能会认为它们共享同一个标签。这一想法被称为 **流形假设**。标签传播是一种半监督学习技术，它利用流形假设为未标注数据分配标签。标签传播首先构建一个图，其中节点是数据样本，边权重表示相似程度。已知标签的节点对应于标注数据，而未知标签的节点对应于未标注数据。然后，标签传播以使得给定节点的邻居标签间分歧最小化的方式，沿着图的边传播已知标签。这为未标注数据提供了标签猜测，随后可以按照常规方式用于模型的监督训练。

更具体地说，基本的标签传播算法 [ZG02] 步骤如下：首先，设 $ w_{i,j} $ 为 $ \mathbf{x}_i $ 与 $ \mathbf{x}_j $ 之间的非负边权重，它衡量这两个（标注或未标注）数据点的相似度。假设我们有 $ M $ 个标注数据点和 $ N $ 个未标注数据点，定义 $ (M + N) \times (M + N) $ 的转移矩阵 $ \mathbf{T} $，其元素为

$$  \mathbf{T}_{i,j}=\frac{w_{i,j}}{\sum_{k}w_{k,j}}   \tag*{(19.26)}$$

$ T_{i,j} $ 表示将标签从节点 $ j $ 传播到节点 $ i $ 的概率。进一步，定义 $ (M+N) \times C $ 的标签矩阵 $ \mathbf{Y} $，其中 $ C $ 是可能类别的数量。$ \mathbf{Y} $ 的第 $ i $ 行表示数据点 $ i $ 的类别概率分布。然后，重复以下步骤直至 $ \mathbf{Y} $ 中的值不再显著变化：首先，使用转移矩阵 $ \mathbf{T} $ 通过设置 $ \mathbf{Y} \leftarrow \mathbf{T}\mathbf{Y} $ 来传播 $ \mathbf{Y} $ 中的标签。然后，通过设置 $ \mathbf{Y}_{i,c} \leftarrow \mathbf{Y}_{i,c} / \sum_k \mathbf{Y}_{i,k} $ 对 $ \mathbf{Y} $ 的行进行重新归一化。最后，将 $ \mathbf{Y} $ 中对应于标注数据点的行替换为其独热表示（即如果数据点 $ i $ 的真实标签为 $ c $ 则 $ \mathbf{Y}_{i,c} = 1 $，否则为 $ 0 $）。收敛后，根据 $ \mathbf{Y} $ 中每个数据点的最高类别概率选择猜测的标签。

该算法迭代地利用数据点的相似性（编码在用于构建转移矩阵的权重中）将信息从（固定的）标签传播到未标注数据上。在每次迭代中，给定数据点的标签分布计算为其所有连接数据点标签分布的加权平均，其中权重对应于 T 中的边权重。可以证明，该过程收敛到一个固定点，其计算成本主要涉及对未标注到未标注转移概率矩阵求逆 [ZG02]。

整个方法可以看作是一种 **直推式学习** 形式，因为它学习的是为固定的未标注数据集预测标签，而不是学习一个能够泛化的模型。然而，基于所诱导出的标签，我们可以按照常规方式进行归纳式学习。

标签传播的成功在很大程度上取决于用于构建不同节点（数据点）之间权重的 **相似性定义**。对于简单数据，测量数据点之间的欧几里得距离就足够了。然而，对于复杂的高维数据，欧几里得距离可能无法有意义地反映两个数据点共享同一类别的可能性。相似性权重也可以根据问题特定的知识任意设定。关于构建相似图的不同方式的一些示例，请参见 Zhu [Zhu05, 第3章]。关于近期将这种方法与深度学习结合使用的论文，可参见 [BRR18; Isc+19]。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

#### 19.3.5 一致性正则化

一致性正则化利用了一个简单的思想：对给定的数据点（或模型本身）施加扰动不应导致模型输出发生剧烈变化。由于这种度量一致性仅利用模型的输出（而非真实标签），因此它易于应用于未标记数据，从而可用于为半监督学习构造合适的损失函数。这一思想最初在“伪集成学习”框架下提出 [BAP14]，随后不久出现了类似的变体 [LA16; SJT16]。

在最一般的形式中，模型 $ p_{\theta}(y|\boldsymbol{x}) $ 和应用到输入上的变换都可以是随机的。例如，在计算机视觉问题中，我们可以通过数据增强（如随机旋转或向输入图像添加噪声）来变换输入，并且网络可能包含随机成分，如 dropout（第13.5.4节）或权重噪声 [Gra11]。一种常见且简单的一致性正则化形式首先采样 $ \boldsymbol{x}^{\prime} \sim q(\boldsymbol{x}^{\prime}|\boldsymbol{x}) $（其中 $ q(\boldsymbol{x}^{\prime}|\boldsymbol{x}) $ 是由随机输入变换诱导的分布），然后最小化损失 $ \|p_{\theta}(y|\boldsymbol{x}) - p_{\theta}(y|\boldsymbol{x}^{\prime})\|^2 $。在实践中，第一项 $ p_{\theta}(y|\boldsymbol{x}) $ 通常被视为固定的（即梯度不通过它传播）。在半监督设置中，一个批次的有标记数据 $ (\boldsymbol{x}_1, y_1), (\boldsymbol{x}_2, y_2), \ldots, (\boldsymbol{x}_M, y_M) $ 和无标记数据 $ \boldsymbol{x}_1, \boldsymbol{x}_2, \ldots, \boldsymbol{x}_N $ 的组合损失函数为

$$  \mathcal{L}(\boldsymbol{\theta})=-\sum_{i=1}^{M}\log p_{\theta}(y=y_{i}|\boldsymbol{x}_{i})+\lambda\sum_{j=1}^{N}\|p_{\theta}(y|\boldsymbol{x}_{j})-p_{\theta}(y|\boldsymbol{x}_{j}^{\prime})\|^{2}   \tag*{(19.27)}$$

其中 $ \lambda $ 是一个标量超参数，用于平衡无标记数据损失的重要性，为简单起见，我们用 $ \boldsymbol{x}_j' $ 表示从 $ q(\boldsymbol{x}'|\boldsymbol{x}_j) $ 中采样的样本。

方程 (19.27) 中一致性正则化的基本形式揭示了影响这种半监督学习方法成功的许多设计选择。首先，为超参数 $ \lambda $ 选择的值很重要。如果它太大，则模型可能不会给予监督学习任务足够的权重，反而会开始强化自身的错误预测（类似于自训练中的确认偏差）。由于模型在训练初期、尚未接触大量有标记数据时通常表现较差，实践中常见做法是先将 $ \lambda $ 设为零，然后在训练过程中逐步增加其值。

第二个重要的考虑因素是应用于输入的随机变换，即 $ q(\boldsymbol{x}| \boldsymbol{x}) $。一般来说，这些变换应设计为不改变 $ \boldsymbol{x} $ 的标签。如上所述，常见的选择是使用特定领域的数据增强。最近的研究表明，使用强力破坏输入（但可以说仍不改变标签）的强数据增强可以产生特别强大的结果 $ [X_{ie}+19; \text{Ber}+19a; \text{Soh}+20] $。

使用数据增强需要专家知识来确定哪些变换是保持标签且适用于给定问题的。另一种称为虚拟对抗训练（VAT）的技术，则使用一种通过分析找到的、旨在最大程度改变模型输出的扰动来变换输入。具体来说，VAT 计算一个扰动 $ \delta $，近似为 $ \delta = \arg\max_{\delta} D_{\mathbb{K}\mathbb{L}} (p_{\theta}(y|\mathbf{x}) \parallel p_{\theta}(y|\mathbf{x} + \delta)) $。近似方法是从多元高斯分布中采样 $ \mathbf{d} $，初始化 $ \delta = \mathbf{d} $，然后进行

$$  \delta\leftarrow\nabla_{\delta}D_{\mathbb{K L}}\left(p_{\theta}(y|\boldsymbol{x})\parallel p_{\theta}(y|\boldsymbol{x}+\boldsymbol{\delta})\right)|\delta=\xi\boldsymbol{d}   \tag*{(19.28)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_431_122_756_323.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">图 19.11：一致性正则化中平方误差与 KL 散度损失的比较。该可视化针对一个二分类问题，假设模型对未扰动输入的输出为 1。图中绘制了当扰动输入的对数值（即输入到输出 sigmoid 非线性单元前的激活值）取特定值时产生的损失。当对数值趋向正无穷时，模型预测类别标签为 1（与未扰动输入的预测一致）；当趋向负无穷时，模型预测类别为 0。平方误差损失在模型以高概率预测某一类别时会饱和（且梯度为零），而 KL 散度则在模型越来越确信地预测类别 0 时无界增长。</div>


其中 $ \xi $ 是一个小常数，通常取 $ 10^{-6} $。随后，VAT 设定：

$$  \boldsymbol{x}^{\prime}=\boldsymbol{x}+\epsilon\frac{\delta}{\left\|\boldsymbol{\delta}\right\|_{2}}   \tag*{(19.29)}$$

并像通常一样采用一致性正则化（如公式 (19.27) 所示），其中 $ \epsilon $ 是设置应用于 x 的扰动的 L2 范数的标量超参数。

一致性正则化还会深刻影响训练目标的几何性质以及 SGD 的轨迹，使得模型性能尤其受益于非标准训练流程。例如，使用一致性正则化的目标函数在不同训练轮次间的权重欧氏距离显著更大。Athiwaratkun 等人 [Ath+19] 表明，通过利用一致性正则化的几何特性，随机权重平均（SWA）[Izm+18] 的一个变体可以在半监督学习任务上达到最先进的性能。

使用一致性正则化时的最后一个考虑因素是用于衡量网络在有扰动和无扰动情况下输出差异的函数。公式 (19.27) 使用了平方 L2 距离（也称为 Brier 分数），这是一个常见的选择 [SJT16; TV17; LA16; Ber+19b]。另一个常见做法是使用 KL 散度 $ D_{\mathbb{K}\mathbb{L}}(p_{\theta}(y|\boldsymbol{x}) \parallel p_{\theta}(y|\boldsymbol{x}') $，这与用于有标签样本的交叉熵损失（即真实标签与预测之间的 KL 散度）类似 [Miy+18; Ber+19a; Xie+19]。假设模型在其输出上使用 softmax 非线性，则当模型在扰动和未扰动输入上的预测差异越来越大时，平方误差损失的梯度趋近于零。因此，使用平方误差损失的一个潜在优势是当模型预测非常不稳定时不会进行更新。然而，KL 散度与用于有标签数据的交叉熵损失具有相同的尺度，这使得对无标签损失超参数 $ \lambda $ 的调节更加直观。两种损失函数的比较如图 19.11 所示。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

#### 19.3.6 深度生成模型 *

生成模型通过最小化 $ \mathcal{L}_{U} = -\sum_{n} \log p_{\theta}(\boldsymbol{x}_{n}) $ 来学习边际分布的模型，从而提供了一种自然利用无标签数据的方式。已有多种方法通过利用 $ p_{\theta}(\boldsymbol{x}_{n}) $ 的模型来帮助构建更好的监督模型，从而将生成模型用于半监督学习。

##### 19.3.6.1 变分自编码器

在第20.3.5节中，我们描述了变分自编码器（VAE），它定义了数据 $ \boldsymbol{x} $ 和潜变量 $ \boldsymbol{z} $ 联合分布的概率模型。假设数据生成过程为：首先采样 $ \boldsymbol{z} \sim p(\boldsymbol{z}) $，然后采样 $ \boldsymbol{x} \sim p(\boldsymbol{x}|\boldsymbol{z}) $。在训练时，VAE 使用编码器 $ \boldsymbol{q}_{\lambda}(\boldsymbol{z}|\boldsymbol{x}) $ 来近似后验，并使用解码器 $ p_{\theta}(\boldsymbol{x}|\boldsymbol{z}) $ 来近似似然。编码器和解码器通常是深度神经网络。可以通过最大化数据的证据下界（ELBO）来联合训练编码器和解码器的参数。

潜变量 $ p(z) $ 的边际分布通常选择简单的分布，例如对角协方差的高斯分布。在实践中，由于 $ \boldsymbol{z} $ 通常比 $ \boldsymbol{x} $ 具有更低的维度，$ \boldsymbol{z} $ 是通过级联的非线性变换构建的，并且其各维度设计为相互独立，因此这些因素使得潜变量 $ \boldsymbol{z} $ 更适合下游分类任务。换句话说，潜变量可以提供一种（学习到的）表示，使得数据更容易分离。在 [Kin+14] 中，这种方法被称为 M1，并且确实表明在标签稀缺时，潜变量可用于训练更强的模型。（无监督学习表示以帮助下游分类任务的一般思想在第19.2.4节中有进一步描述。）

另一种利用 VAE 的方法也在 [Kin+14] 中提出，称为 M2，其形式为：

$$  p_{\theta}(\boldsymbol{x},y)=p_{\theta}(y)p_{\theta}(\boldsymbol{x}|y)=p_{\theta}(y)\int p_{\theta}(\boldsymbol{x}|y,\boldsymbol{z})p_{\theta}(\boldsymbol{z})d\boldsymbol{z}   \tag*{(19.30)}$$

其中 $z$ 是潜变量，$p_{\theta}(z) = \mathcal{N}(z|\mu_{\theta}, \Sigma_{\theta})$ 是潜先验（通常我们固定 $\mu_{\theta} = 0$ 和 $\Sigma_{\theta} = \mathbf{I}$），$p_{\theta}(y) = \mathrm{Cat}(y|\pi_{\theta})$ 是标签先验，$p_{\theta}(x|y, z) = p(x|f_{\theta}(y, z))$ 是似然（例如高斯分布），其参数由 $f$（一个深度神经网络）计算得到。该方法的主要创新在于假设数据同时由一个潜类别变量 $y$ 和一个连续潜变量 $z$ 生成。类别变量 $y$ 在标签数据中被观测到，而在无标签数据中未被观测到。

为了计算标签数据的似然 $ p_{\theta}(\boldsymbol{x}, y) $，我们需要对 $z$ 进行边际化，这可以通过使用如下形式的推理网络来实现：

$$  q_{\phi}(z|y,\boldsymbol{x})=\mathcal{N}(z|\boldsymbol{\mu}_{\phi}(y,\boldsymbol{x}),\mathrm{d i a g}(\sigma_{\phi}^{2}(\boldsymbol{x}))   \tag*{(19.31)}$$

然后我们使用如下的变分下界：

$$  \log p_{\theta}(\boldsymbol{x},y)\geq\mathbb{E}_{q_{\phi}(z|\boldsymbol{x},y)}\left[\log p_{\theta}(\boldsymbol{x}|y,z)+\log p_{\theta}(y)+\log p_{\theta}(z)-\log q_{\phi}(z|\boldsymbol{x},y)\right]=-\mathcal{L}(\boldsymbol{x},y)   \tag*{(19.32)}$$

这与标准 VAE 的做法一致（参见第20.3.5节）。唯一的区别是我们观测到两种类型的数据：$\boldsymbol{x}$ 和 $y$。

---

为了计算无标签数据的似然 $ p_{\theta}(\boldsymbol{x}) $，我们需要对 $z$ 和 $y$ 进行边缘化，这可以通过使用如下形式的推理网络来实现：

$$ q_{\phi}(z,y|\boldsymbol{x})=q_{\phi}(z|\boldsymbol{x})q_{\phi}(y|\boldsymbol{x}) \tag*{(19.33)}$$

$$ q_{\phi}(z|\boldsymbol{x})=\mathcal{N}(z|\boldsymbol{\mu}_{\phi}(\boldsymbol{x}),\mathrm{diag}(\sigma_{\phi}^{2}(\boldsymbol{x})) \tag*{(19.34)}$$

$$ q_{\phi}(y|\boldsymbol{x})=\mathrm{Cat}(y|\boldsymbol{\pi}_{\phi}(\boldsymbol{x})) \tag*{(19.35)}$$

注意， $ q_{\phi}(y|\pmb{x}) $ 扮演了判别式分类器的角色，用于填充缺失的标签。然后我们使用以下变分下界：

$$ \log p_{\theta}(\boldsymbol{x})\geq\mathbb{E}_{q_{\phi}(\boldsymbol{z},y|\boldsymbol{x})}\left[\log p_{\theta}(\boldsymbol{x}|y,\boldsymbol{z})+\log p_{\theta}(y)+\log p_{\theta}(\boldsymbol{z})-\log q_{\phi}(\boldsymbol{z},y|\boldsymbol{x})\right] \tag*{(19.36)}$$

$$ =-\sum_{y}q_{\phi}(y|\boldsymbol{x})\mathcal{L}(\boldsymbol{x},y)+\mathbb{H}\left(q_{\phi}(y|\boldsymbol{x})\right)=-\mathcal{U}(\boldsymbol{x}) \tag*{(19.37)}$$

需要注意的是，判别式分类器 $ q_{\phi}(y|\boldsymbol{x}) $ 仅用于计算无标签数据的对数似然，这是不理想的。因此，我们可以在有标签数据上增加一个额外的分类损失，得到如下的整体目标函数：

$$ \mathcal{L}(\boldsymbol{\theta})=\mathbb{E}_{(\boldsymbol{x},y)\sim\mathcal{D}_{L}}\left[\mathcal{L}(\boldsymbol{x},y)\right]+\mathbb{E}_{\boldsymbol{x}\sim\mathcal{D}_{U}}\left[\mathcal{U}(\boldsymbol{x})\right]+\alpha\mathbb{E}_{(\boldsymbol{x},y)\sim\mathcal{D}_{L}}\left[-\log q_{\phi}(y|\boldsymbol{x})\right] \tag*{(19.38)}$$

其中 $ \alpha $ 是一个超参数，用于控制生成学习和判别学习的相对权重。

当然，M2 中使用的概率模型只是分解观测数据、类别标签和连续隐变量之间依赖关系的众多方式之一。除了变分推断之外，还有许多其他近似推断方法。最佳技术将取决于具体问题，但总体而言，生成式方法的主要优势在于我们可以融入领域知识。例如，我们可以对缺失数据机制进行建模，因为标签的缺失可能包含关于底层数据的信息（例如，如果人们身体不适，他们可能不愿意回答关于健康的调查问题）。

##### 19.3.6.2 生成对抗网络

生成对抗网络（GANs，将在本书续集 [Mur23] 中详细描述）是一类流行的生成模型，它们学习数据分布的隐式模型。GANs 由一个生成器网络和一个判别器网络组成：生成器将来自简单隐分布的样本映射到数据空间，判别器则试图区分生成器的输出与真实数据分布中的样本。生成器被训练为生成能被判别器分类为“真实”的样本。

由于标准 GANs 既不能学习给定数据点的隐表示，也不学习数据分布的显式模型，因此我们不能使用与 VAEs 相同的方法。相反，使用 GANs 进行半监督学习通常通过修改判别器来实现，使其输出一个类别标签或“虚假”，而不是简单地对真实与虚假进行分类 [Sal+16; Ode16]。对于有标签的真实数据，判别器被训练为输出适当的类别标签；对于无标签的真实数据，它被训练为提高任一类别标签的概率。与标准 GAN 训练一样，判别器被训练为将生成器的输出分类为虚假，而生成器则被训练为欺骗判别器。

作者：Kevin P. Murphy。 (C) MIT 出版社。CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_307_124_867_330.jpg" alt="图像" width="48%" /></div>


<div style="text-align: center;">图 19.12: 半监督 GAN 框架示意图。判别器被训练以输出标记数据点（红色）的类别、生成器输出（黄色）的“虚假”标签，以及未标记数据（绿色）的任意标签。</div>


更详细地，设 $p_{\theta}(y|\boldsymbol{x})$ 为判别器，具有 $C+1$ 个输出，对应 C 个类别加上一个“虚假”类别；设 $G(z)$ 为生成器，它从先验分布 $p(z)$ 中采样输入。假设我们使用最初在 [Goo+14] 中提出的标准交叉熵 GAN 损失。则判别器的损失为

$$ -\mathbb{E}_{\boldsymbol{x},y\sim p(\boldsymbol{x},y)}\log p_{\theta}(y|\boldsymbol{x})-\mathbb{E}_{\boldsymbol{x}\sim p(\boldsymbol{x})}\log[1-p_{\theta}(y=C+1|\boldsymbol{x})]-\mathbb{E}_{\boldsymbol{z}\sim p(\boldsymbol{z})}\log p_{\theta}(y=C+1|G(\boldsymbol{z})) \tag*{(19.39)}$$

该损失旨在最大化标记示例的正确类别概率，最小化真实未标记示例的虚假类别概率，并最大化生成示例的虚假类别概率。生成器的损失更简单，即

$$ \mathbb{E}_{z\sim p(z)}\log p_{\theta}(y=C+1|G(z)) \tag*{(19.40)}$$

图 19.12 展示了半监督 GAN 框架的可视化示意图。

##### 19.3.6.3 归一化流

归一化流（详见本书后续部分 [Mur23]）是一种定义深度生成模型的可处理方法。更准确地说，它定义了一个可逆映射 $f_{\theta} : \mathcal{X} \to \mathcal{Z}$，参数为 $\theta$，从数据空间 $\mathcal{X}$ 映射到潜空间 $\mathcal{Z}$。利用变量变换公式，数据空间的密度可以从潜空间的密度出发写为：

$$ p(x)=p(f(x))\cdot\left|\det\left(\frac{\partial f}{\partial x}\right)\right|. \tag*{(19.41)}$$

我们可以将其扩展到半监督学习，如 [Izm+20] 所提出的。对于类别标签 $y \in \{1 \ldots \mathcal{C}\}$，我们可以将条件于标签 $k$ 的潜变量分布指定为均值为 $\mu_k$、协方差为 $\Sigma_k$ 的高斯分布：$p(z|y = k) = \mathcal{N}(z|\mu_k, \Sigma_k)$。那么 $z$ 的边缘分布即为高斯混合。标记数据的似然为

$$ p_{\mathcal{X}}(x|y=k)=\mathcal{N}\left(f(x)|\mu_{k},\Sigma_{k}\right)\cdot\left|\det\left(\frac{\partial f}{\partial x}\right)\right|, \tag*{(19.42)}$$

“概率机器学习：导论”。在线版本，2024 年 11 月 23 日

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_349_133_835_397.jpg" alt="图像" width="42%" /></div>


<div style="text-align: center;">图 19.13：结合在无标签数据上的自监督学习（左）、监督微调（中）以及在伪标签数据上的自训练（右）。来自 [Che+20c] 的图 3。经 Ting Chen 许可使用。</div>


以及数据标签未知时的似然为 $ p(x) = \sum_{k} p(x|y = k)p(y = k) $。

对于半监督学习，我们可以最大化有标签数据 $ D_{\ell} $ 和无标签数据 $ D_{u} $ 的联合似然：

$$  p(\mathcal{D}_{\ell},\mathcal{D}_{u}|\theta)=\prod_{(x_{i},y_{i})\in\mathcal{D}_{\ell}}p(x_{i},y_{i})\prod_{x_{j}\in\mathcal{D}_{u}}p(x_{j}),   \tag*{(19.43)}$$

其中参数 $ \theta $ 属于双射函数 f，该函数学习贝叶斯分类器的密度模型。给定测试点 x，模型预测分布为

$$  p_{X}(y=c|x)=\frac{p(x|y=c)p(y=c)}{p(x)}=\frac{p(x|y=c)p(y=c)}{\sum_{k=1}^{C}p(x|y=k)p(y=k)}=\frac{\mathcal{N}(f(x)|\mu_{c},\Sigma_{c})}{\sum_{k=1}^{C}\mathcal{N}(f(x)|\mu_{k},\Sigma_{k})},   \tag*{(19.44)}$$

其中我们假设 $ p(y = c) = 1/C $。对于测试点 $ x $，我们可以通过贝叶斯决策规则 $ y = \arg\max_{c \in \{1, \ldots, C\}} p(y = c|x) $ 进行预测。

#### 19.3.7 结合自监督与半监督学习

自监督学习与半监督学习可以结合。例如，[Che+20c] 使用 SimCLR（第 19.2.4.4 节）在无标签数据上进行自监督表示学习，然后在小规模有标签数据集上微调该表示（如第 19.2 节中的迁移学习），最后将训练好的模型重新应用于原始无标签数据集，并将教师模型 T 的预测蒸馏到学生模型 S 中。（知识蒸馏是指用一个模型训练另一个模型预测的方法，最初由 [HVD14] 提出。）即，在微调 T 后，通过最小化以下损失来训练 S：

$$  \mathcal{L}(T)=-\sum_{\boldsymbol{x}_{i}\in\mathcal{D}}\left[\sum_{y}p^{T}(y|\boldsymbol{x}_{i};\tau)\log p^{S}(y|\boldsymbol{x}_{i};\tau)\right]   \tag*{(19.45)}$$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可。

---

其中 $ \tau > 0 $ 是应用于 softmax 输出的温度参数，用于执行标签平滑。如果 $ S $ 与 $ T $ 具有相同的形式，则这被称为自训练，详见第 19.3.1 节。然而，通常学生模型 $ S $ 比教师模型 $ T $ 更小（例如，$ T $ 可能是高容量模型，而 $ S $ 是运行在手机上的轻量版本）。整体方法如图 Figure 19.13 所示。

### 19.4 主动学习

在主动学习中，目标是通过尽可能少地查询 $ (\boldsymbol{x}, y) $ 数据点来识别真实的预测映射 $ y = f(\boldsymbol{x}) $。主要有三种变体。在查询合成中，算法可以选择任意输入 $ \boldsymbol{x} $，并询问其对应的输出 $ y = f(\boldsymbol{x}) $。在基于池的主动学习中，存在一个规模较大但固定的未标注数据点集合，算法可以请求其中一个或多个点的标签。最后，在基于流的主动学习中，输入数据持续到达，算法必须决定是否要为当前输入请求标签。

存在若干密切相关的问题。在贝叶斯优化中，目标是通过尽可能少的查询来估计全局最优 $ \boldsymbol{x}^* = \arg\min_{\boldsymbol{x}} f(\boldsymbol{x}) $ 的位置；通常我们为中间查询 $ (\boldsymbol{x}, y) $ 拟合一个代理（响应面）模型，以决定下一步询问哪个问题。在实验设计中，目标是使用精心选择的数据样本 $ \mathcal{D} = \{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_N\} $ 来推断某个模型的参数向量，即我们希望用尽可能少的数据估计 $ p(\boldsymbol{\theta}|\mathcal{D}) $（这可以被视为主动学习的一种无监督或广义形式）。

在本节中，我们简要回顾基于池的主动学习方法。更多细节可参见例如 [Set12] 的综述。

#### 19.4.1 决策理论方法

在 [KHB07; RM01] 提出的主动学习决策理论方法中，我们根据信息价值定义查询 x 的效用。具体而言，我们将发出查询 x 的效用定义为

$$  U(\boldsymbol{x})\triangleq\mathbb{E}_{p(y|\boldsymbol{x},\mathcal{D})}\left[\min_{a}\left(\rho(a|\mathcal{D})-\rho(a|\mathcal{D},(\boldsymbol{x},y))\right)\right]   \tag*{(19.46)}$$

其中 $ \rho(a|\mathcal{D}) = \mathbb{E}_{p(\theta|\mathcal{D})}[\ell(\theta,a)] $ 是给定迄今为止观测到的数据 $ \mathcal{D} $ 下采取某个未来行动 a 的后验期望损失。不幸的是，为每个 $ \boldsymbol{x} $ 计算 $ U(\boldsymbol{x}) $ 相当昂贵，因为对于可能观测到的每个响应 y，我们都必须根据 $ (\boldsymbol{x}, y) $ 更新信念，以了解其对未来决策可能产生的影响（类似于应用于信念状态的前瞻搜索技术）。

#### 19.4.2 信息论方法

在主动监督学习的信息论方法中，我们避免使用任务特定的损失函数，而是专注于尽可能好地学习模型。具体而言，[Lin56] 提出根据关于参数 $ \theta $ 的信息增益（即熵的减少）来定义查询 x 的效用：

$$  U(\pmb{x})\triangleq\mathbb{H}\left(p(\pmb{\theta}|\mathcal{D})\right)-\mathbb{E}_{p(y|\pmb{x},\mathcal{D})}\left[\mathbb{H}\left(p(\pmb{\theta}|\mathcal{D},\pmb{x},y)\right)\right]   \tag*{(19.47)}$$

---

(第一项相对于 $\boldsymbol{x}$ 是常数，但为了后续便利我们仍将其纳入。) 练习19.1要求你证明该目标函数等价于参数后验的期望变化，其表达式为

$$  U^{\prime}(\pmb{x})\triangleq\mathbb{E}_{p(y|\pmb{x},\mathcal{D})}\left[D_{\mathbb{K L}}\left(p(\pmb{\theta}|\mathcal{D},\pmb{x},y)\parallel p(\pmb{\theta}|\mathcal{D})\right)\right]   \tag*{(19.48)}$$

利用互信息的对称性，我们可以将方程 (19.47) 重写如下：

$$  U(\boldsymbol{x})=\mathbb{H}\left(p(\boldsymbol{\theta}|\mathcal{D})\right)-\mathbb{E}_{p(y|\boldsymbol{x},\mathcal{D})}\left[\mathbb{H}\left(p(\boldsymbol{\theta}|\mathcal{D},\boldsymbol{x},y)\right)\right]   \tag*{(19.49)}$$

$$  =\mathbb{I}(\boldsymbol{\theta},y|\mathcal{D},\boldsymbol{x})   \tag*{(19.50)}$$

$$  =\mathbb{H}\left(p(y|\pmb{x},\mathcal{D})\right)-\mathbb{E}_{p(\pmb{\theta}|\mathcal{D})}\left[\mathbb{H}\left(p(y|\pmb{x},\pmb{\theta})\right)\right]   \tag*{(19.51)}$$

该方法的一个优势在于，我们现在只需考虑输出 $y$ 的预测分布的不确定性，而无需考虑参数 $\theta$ 的不确定性。

方程 (19.51) 有一个有趣的解释。第一项倾向于选择那些预测标签存在不确定性的样本 $\boldsymbol{x}$。仅以此作为选择准则的方法称为**最大熵采样**[SW87]。然而，这对于本身具有模糊性或错误标注的样本可能会产生问题。方程 (19.51) 中的第二项会抑制这种行为，因为它倾向于选择那些在已知 $\theta$ 时预测标签相当确定的样本 $\boldsymbol{x}$；这将避免选取本身难以预测的样本。换句话说，方程 (19.51) 会选择那些模型能做出**自信且高度多样化**预测的样本 $\boldsymbol{x}$。因此，这种方法被称为**基于分歧的贝叶斯主动学习**或 BALD [Hou+12]。

该方法可用于训练其他领域（如医学图像或天文图像 [Wal+20]）中专家标签难以获取的分类器。

#### 19.4.3 批量主动学习

到目前为止，我们假设了一种贪婪或短视的策略，即每次只选择一个样本 $\mathbf{x}$，仿佛它是最后一个待选数据点。但有时我们有一个预算，需要收集一组 $B$ 个样本，记为 $(\mathbf{X}, \mathbf{Y})$。在这种情况下，信息增益准则变为 $U(\mathbf{x}) = \mathbb{H}(p(\boldsymbol{\theta}|\mathcal{D})) - \mathbb{E}_{p(\mathbf{Y}|\mathbf{x}, \mathcal{D})} [\mathbb{H}(p(\boldsymbol{\theta}|\mathbf{Y}, \mathbf{x}, \mathcal{D}))]$。不幸的是，对这个准则进行优化在时间范围 $B$ 上是 NP-难的 [KLQ95; KG05]。

幸运的是，在某些条件下，贪婪策略是近似最优的，下面我们来解释这一点。固定查询 $\boldsymbol{x}$，定义 $f(\boldsymbol{y}) \triangleq \mathbb{H}(p(\boldsymbol{\theta} \mid \mathcal{D})) - \mathbb{H}(p(\boldsymbol{\theta} \mid \mathbf{Y}, \boldsymbol{x}, \mathcal{D}))$ 为信息增益函数，因此 $U(\boldsymbol{x}) = \mathbb{E}_{\boldsymbol{y}} [f(\boldsymbol{y}, \boldsymbol{x})]$。显然 $f(\boldsymbol{\theta}) = 0$，并且根据“信息越多越好”的原则，$f$ 是非递减的，即 $f(Y^{\text{large}}) \geq f(Y^{\text{small}})$。此外，[KG05] 证明了 $f$ 是子模的。因此，顺序贪婪方法在常数因子内是最优的。如果将这种贪婪技术与 BALD 目标结合，就得到了一种称为 **BatchBALD** 的方法 [KAG19]。

### 19.5 元学习

我们可以将学习算法视为一个函数 $A$，它将数据映射到参数估计 $\theta = A(\mathcal{D})$。函数 $A$ 通常有自己的参数——记为 $\phi$——例如 $\theta$ 的初始值或学习率等。我们用 $\theta = A(\mathcal{D}; \phi)$ 表示这一点。我们可以设想学习 $\phi$ 本身，

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_363_124_812_401.jpg" alt="图片" width="38%" /></div>

<div style="text-align: center;">图19.14：元学习的层次贝叶斯模型示意图。由 hbayes_maml.ipynb 生成。</div>

给定一组数据集 $ \mathcal{D}_{1:J} $ 和某个元学习算法 $ M $，即 $ \phi = M(\mathcal{D}_{1:J}) $。然后我们可以应用 $ A(\cdot;\phi) $ 在新的数据集 $ \mathcal{D}_{J+1} $ 上学习参数 $ \theta_{J+1} $。元学习有很多技术——例如，参见最近的综述 [Van18; HRP21]。下面我们讨论一种特别流行的方法。（注意，元学习也称为学会学习 [TP97]。）

#### 19.5.1 模型无关的元学习（MAML）

元学习的一种自然方法是使用层次贝叶斯模型，如图 Figure 19.14 所示。每个任务的参数 $ \theta_j $ 假设来自一个共同的先验 $ p(\theta_j|\xi) $，这有助于汇集多个数据匮乏问题的统计强度。元学习等价于学习先验 $ \phi $。在该模型上，不进行完整的贝叶斯推断，更高效的方法是使用以下经验贝叶斯（第 4.6.5.3 节）近似：

$$  \boldsymbol{\xi}^{*}=\underset{\boldsymbol{\xi}}{\operatorname{argmax}}\frac{1}{J}\sum_{j=1}^{J}\log p(\mathcal{D}_{valid}^{j}|\hat{\boldsymbol{\theta}}_{j}(\boldsymbol{\xi},\mathcal{D}_{train}^{j}))   \tag*{(19.52)}$$

其中 $ \hat{\boldsymbol{\theta}}_j = \hat{\boldsymbol{\theta}}(\boldsymbol{\xi}, \mathcal{D}_{\mathrm{train}}^j) $ 是基于 $ \mathcal{D}_{\mathrm{train}}^j $ 和先验 $ \boldsymbol{\xi} $ 的任务 $ j $ 参数的点估计，并且我们使用边际似然的交叉验证近似（第 5.2.4 节）。

为了计算目标任务 $ \theta_{J+1} $ 的参数的点估计，我们使用从 $ \xi $ 开始、学习率为 $ \eta $ 的 $ K $ 步梯度上升过程。这被称为模型无关的元学习（model-agnostic meta-learning）或 MAML [FAL17]。可以证明，这等价于使用以 $ \xi $ 为中心的高斯先验的近似 MAP 估计，其中先验的强度由梯度步数控制 [San96; Gra+18]。（这是从共享先验 $ \xi $ 开始对任务特定权重进行快速适应的一个例子。）

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_265_115_902_409.jpg" alt="Image" width="55%" /></div>


<div style="text-align: center;">图 19.15：元学习用于少样本学习的示意图。这里，每个任务都是一个 3 路 2 样本分类问题，因为每个训练任务包含一个具有三个类别、每类两个样本的支撑集。来自 https://bit.ly/3rrvSjw。版权 (2019) Borealis AI。经 Simon Prince 和 April Cooper 许可使用。</div>


### 19.6 少样本学习

人类能够从极少的标记样本中进行预测学习。这被称为**少样本学习**。在极端情况下，人或系统从每类单个样本中学习，称为单样本学习；如果没有任何标记样本，则称为零样本学习。

评估少样本学习方法的一种常见方式是使用 **C 路 N 样本分类**，即系统需要仅用每类 N 个训练样本学会对 C 个类别进行分类。通常 N 和 C 非常小，例如图 19.15 展示了 C=3 个类别、每类 N=2 个样本的情况。由于新领域（这里是鸭子、海豚和母鸡）的数据量极小，我们无法期望从头开始学习，因此借助元学习。

在训练过程中，元算法 M 对来自第 j 组的标记支撑集进行训练，返回一个预测器 $ f^j $，然后在同样来自第 j 组的一个不相交的查询集上对其进行评估。我们对所有 J 组优化 M。最后，将 M 应用于新的标记支撑集，得到 $ f^{\text{test}} $，并将其应用于测试域的查询集。图 19.15 展示了这一过程。我们看到，两个训练任务中的类别（$ \{\text{猫}, \text{羔羊}, \text{猪}\} $ 和 $ \{\text{狗}, \text{鲨鱼}, \text{狮子}\} $）与测试任务中的类别（$ \{\text{鸭子}, \text{海豚}, \text{母鸡}\} $）之间没有重叠。因此，算法 M 必须学会通用地预测图像类别，而不是任何特定的标签集。

少样本学习有多种方法。我们在 19.6.1 节讨论其中一种方法。更多方法可参见例如 [Wan+20b]。

#### 19.6.1 匹配网络

少样本学习的一种方法是在其他数据集上学习一个距离度量，然后在最近邻分类器中使用 $ d_{\theta}(\boldsymbol{x},\boldsymbol{x}^{\prime}) $。这本质上定义了一个半参数模型，形式为 $ p_{\theta}(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{S}) $，其中 $ \mathcal{S} $ 是小的标记数据集（称为支撑集），$ \theta $ 是距离函数的参数。该方法广泛用于细粒度分类。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_411_114_760_338.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">图 19.16: 用于单样本学习的匹配网络示意图。改编自 [Vin+16] 的图 1，经 Oriol Vinyals 许可使用。</div>


在许多视觉上相似的不同类别任务中，例如来自人脸库的人脸图像或来自商品目录的产品图像。

这种方法的一种扩展是学习一个如下形式的函数：

$$ p_{\theta}(y|\boldsymbol{x},\mathcal{S})=\mathbb{I}\left(y=\sum_{n\in\mathcal{S}}a_{\theta}(\boldsymbol{x},\boldsymbol{x}_{n};\mathcal{S})y_{n}\right)   \tag*{(19.53)}$$

其中 $a_{\theta}(\boldsymbol{x},\boldsymbol{x}_{n};\mathcal{S}) \in \mathbb{R}^{+}$ 是一种自适应相似性核。例如，我们可以使用一个注意力核：

$$ a(\boldsymbol{x},\boldsymbol{x}_{n};\mathcal{S})=\frac{\exp(c(f(\boldsymbol{x}),g(\boldsymbol{x}_{n})))}{\sum_{n^{\prime}=1}^{N}\exp(c(f(\boldsymbol{x}),g(\boldsymbol{x}_{n^{\prime}})))}   \tag*{(19.54)}$$

其中 $c(\boldsymbol{u}, \boldsymbol{v})$ 是余弦距离。（如果需要，我们可以让 $f$ 和 $g$ 是同一个函数。）直观上，注意力核会将 $\boldsymbol{x}$ 与 $\boldsymbol{x}_n$ 在所有标注样本的上下文中进行比较，从而提供关于哪些特征维度是相关的隐含信号。（我们在第 15.4 节中更详细地讨论注意力机制。）这被称为**匹配网络（matching network）**[Vin+16]。图 19.16 展示了其示意图。

我们可以像元学习（第 19.5 节）那样，使用多个小数据集训练 $f$ 和 $g$ 函数。更精确地，设 $\mathcal{D}$ 是一个大型标注数据集（例如 ImageNet），$p(\mathcal{L})$ 是标签上的一个分布。我们通过采样一小部分标签（例如 25 个）$\mathcal{L} \sim p(\mathcal{L})$，然后从 $\mathcal{D}$ 中采样这些标签下的一小组支持样例 $\mathcal{S} \sim \mathcal{L}$，最后采样这些相同标签下的一小组测试集 $\mathcal{T} \sim \mathcal{L}$ 来创建一个任务。然后训练模型，使其根据支持集预测测试标签，即优化以下目标：

$$ \mathcal{L}(\boldsymbol{\theta};\mathcal{D})=\mathbb{E}_{\mathcal{L}\sim p(\mathcal{L})}\left[\mathbb{E}_{\mathcal{S}\sim\mathcal{L},\mathcal{T}\sim\mathcal{L}}\left[\sum_{(\boldsymbol{x},y)\in\mathcal{T}}\log p_{\boldsymbol{\theta}}(y|\boldsymbol{x},\mathcal{S})\right]\right]   \tag*{(19.55)}$$

训练后，我们固定 $\theta$，并将公式 (19.53) 应用于测试支持集 S。

---

### 19.7 弱监督学习

“弱监督学习”一词指的是训练集中每个特征向量没有精确标签的场景。

一种场景是每个样本对应一个标签分布，而非单一标签。幸运的是，我们仍然可以进行最大似然训练：只需最小化交叉熵，

$$  \mathcal{L}(\boldsymbol{\theta})=-\sum_{n}\sum_{y}p(y|\boldsymbol{x}_{n})\log q_{\boldsymbol{\theta}}(y|\boldsymbol{x}_{n})   \tag*{(19.56)}$$

其中 $ p(y|\pmb{x}_{n}) $ 是样本 $ n $ 的标签分布，$ q_{\theta}(y|\pmb{x}_{n}) $ 是预测分布。实际上，将精确标签替换为“软”版本通常很有用，即用某个分布替代狄拉克函数，例如将 90% 的质量置于观测标签上，其余质量均匀分配给其他选项。这称为**标签平滑**，是一种有效的正则化形式（参见 e.g., [MKH19]）。

另一种场景是拥有一组或一包（bag）实例 $ \mathbf{x}_n = \{\mathbf{x}_{n,1}, \ldots, \mathbf{x}_{n,B}\} $，但只有整个包的标签 $ y_n $，而没有包内成员 $ y_{nb} $ 的标签。我们通常假设：若包中任一成员为正，则整个包标记为正，即 $ y_n = \sqrt[B]{b=1} $，但不知道具体是哪个成员“导致”了正结果。然而，若所有成员均为负，则整个包为负。这称为**多实例学习** [DLLP97]。（在 COVID-19 风险评分学习中的一个近期例子见 [MKS21]。）根据对包内标签相关性以及预期正成员比例的假设，可以使用多种算法解决多实例学习问题（参见 e.g., [KF05]）。

另一种场景称为**远程监督** [Min+09]，常用于训练信息抽取系统。其思想是：我们已知某个事实（如“已婚(B,M)”）为真（因为存储在数据库中）。然后利用这一事实，将未标注训练语料中所有提及实体 B 和 M 的句子都标注为“已婚”关系的正例。例如，句子“B 和 M 邀请了 100 人参加他们的婚礼”会被标注为正例。但这种启发式方法可能包含假正例，例如“B 和 M 出去吃晚饭”也会被标注为正例。因此，生成的标签会带有噪声。我们在第 10.4 节讨论处理标签噪声的一些方法。

### 19.8 习题

习题 19.1 [信息增益等式]

考虑以下两个用于评估主动学习环境下查询数据点 $x$ 效用的目标函数：

$$  U(\pmb{x})\triangleq\mathbb{H}\left(p(\pmb{\theta}|\mathcal{D})\right)-\mathbb{E}_{p(y|\pmb{x},\mathcal{D})}\left[\mathbb{H}\left(p(\pmb{\theta}|\mathcal{D},\pmb{x},y)\right)\right]   \tag*{(19.57)}$$

$$  U^{\prime}(\boldsymbol{x})\triangleq\mathbb{E}_{p(y|\boldsymbol{x},\mathcal{D})}\left[D_{\mathbb{K L}}\left(p(\boldsymbol{\theta}|\mathcal{D},\boldsymbol{x},y)\parallel p(\boldsymbol{\theta}|\mathcal{D})\right)\right]   \tag*{(19.58)}$$

证明这两个等式相等。

---



---

## 20 降维

一种常见的无监督学习形式是降维，即学习从高维可见空间 $\boldsymbol{x} \in \mathbb{R}^D$ 到低维潜空间 $\boldsymbol{z} \in \mathbb{R}^L$ 的映射。该映射可以是参数化模型 $\boldsymbol{z} = f(\boldsymbol{x}; \boldsymbol{\theta})$，适用于任意输入；也可以是非参数化映射，其中我们为数据集中的每个输入 $\boldsymbol{x}_n$ 计算一个嵌入 $\boldsymbol{z}_n$，但不针对其他任何点。后一种方法主要用于数据可视化，而前一种方法也可作为其他学习算法的预处理步骤。例如，我们可以先通过学习从 $\boldsymbol{x}$ 到 $\boldsymbol{z}$ 的映射来降低维度，然后通过将 $\boldsymbol{z}$ 映射到 $\boldsymbol{y}$，在此嵌入上学习一个简单的线性分类器。

### 20.1 主成分分析（PCA）

最简单且应用最广泛的降维形式是主成分分析（PCA）。其基本思想是找到高维数据 $\boldsymbol{x} \in \mathbb{R}^D$ 到低维子空间 $\boldsymbol{z} \in \mathbb{R}^L$ 的线性正交投影，使得低维表示在以下意义上成为原始数据的“良好近似”：将 $\boldsymbol{x}$ 投影或编码为 $\boldsymbol{z} = \boldsymbol{W}^T \boldsymbol{x}$，然后将 $\boldsymbol{z}$ 反向投影或解码为 $\hat{\boldsymbol{x}} = \boldsymbol{W} \boldsymbol{z}$，我们希望 $\hat{\boldsymbol{x}}$ 在 $\ell_2$ 距离上接近 $\boldsymbol{x}$。具体地，我们可以定义如下重构误差或失真度：

$$  \mathcal{L}(\mathbf{W})\triangleq\frac{1}{N}\sum_{n=1}^{N}||\boldsymbol{x}_{n}-\mathrm{decode}(\mathrm{encode}(\boldsymbol{x}_{n};\mathbf{W});\mathbf{W})||_{2}^{2}   \tag*{(20.1)}$$

其中编码和解码阶段均为线性映射，具体如下所述。

在第20.1.2节中，我们将证明可以通过令 $\hat{\mathbf{W}} = \mathbf{U}_L$ 来最小化该目标函数，其中 $\mathbf{U}_L$ 包含经验协方差矩阵特征值最大的 $L$ 个特征向量：

$$  \hat{\mathbf{\Sigma}}=\frac{1}{N}\sum_{n=1}^{N}(\mathbf{x}_{n}-\overline{\mathbf{x}})(\mathbf{x}_{n}-\overline{\mathbf{x}})^{\mathsf{T}}=\frac{1}{N}\mathbf{X}_{c}^{\mathsf{T}}\mathbf{X}_{c}   \tag*{(20.2)}$$

其中 $\mathbf{X}_{c}$ 是 $N \times D$ 设计矩阵的中心化版本。在第20.2.2节中，我们将证明这等价于最大化概率PCA（即潜在线性高斯模型）的似然函数。

#### 20.1.1 示例

在详细阐述之前，我们先展示一些例子。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_459_150_704_387.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">图 20.1：PCA 的示意图，将数据从二维投影到一维。红色圆圈是原始数据点，蓝色圆圈是重构点。红点是数据均值。由 pcaDemo2d.ipynb 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_341_509_642_775.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_660_550_819_708.jpg" alt="图像" width="13%" /></div>


<div style="text-align: center;">图 20.2：PCA 应用于类别 9 的 MNIST 手写数字的示意图。网格点位于数据分布沿每个维度的 5%、25%、50%、75%、95% 分位数处。圆圈标记的点是距网格顶点最近的投影图像。改编自 [HTF09] 的图 14.23。由 pca digits.ipynb 生成。</div>


图 20.1 展示了一个非常简单的例子，我们将二维数据投影到一条一维线上。该方向捕捉了数据中的大部分变异。

在图 20.2 中，我们展示了将数字 9 的 MNIST 图像投影到二维空间时发生的情况。尽管输入是高维的（具体为 $28 \times 28 = 784$ 维），但由于像素间存在相关性且许多数字看起来相似，“有效自由度”的数量要少得多。因此，我们可以将每幅图像表示为低维线性空间中的一个点。

通常，解释数据投影到的潜在维度是困难的。然而，通过观察沿某个方向的若干投影点及其所源自的示例，我们可以看到第一主成分（水平方向）似乎捕捉了数字的朝向，而第二主成分（垂直方向）似乎捕捉了线条的粗细。

在图 20.3 中，我们展示了 PCA 应用于另一个图像数据集，即 Olivetti face dataset。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_240_118_912_346.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 20.3: (a) 从奥利维蒂人脸数据库中随机选取的一些 $ 64 \times 64 $ 像素图像。(b) 以图像形式呈现的均值及前三个 PCA 分量。由 pcaImageDemo.ipynb 生成。</div>


这是一组 $ 64 \times 64 $ 的灰度图像。我们将它们投影到一个三维子空间。所得的基向量（投影矩阵 $ \mathbf{W} $ 的列）以图像形式展示在图 20.3b 中；这些基向量被称为 **特征脸**（eigenfaces）[Tur13]，其原因将在第 20.1.2 节中解释。我们看到数据的主要变异模式与整体光照有关，其次是面部眉毛区域的差异。如果我们使用足够的维度（但少于最初的 4096 维），就可以将表示 $ \mathbf{z} = \mathbf{W}^\top \mathbf{x} $ 作为最近邻分类器的输入来执行人脸识别；这比在像素空间中操作更快且更可靠 [MWP98]。

#### 20.1.2 算法的推导

假设我们有一个（无标签）数据集 $\mathcal{D} = \{\boldsymbol{x}_n : n = 1 : N\}$，其中 $\boldsymbol{x}_n \in \mathbb{R}^D$。我们可以将其表示为一个 $N \times D$ 的数据矩阵 $\mathbf{X}$。我们假设 $\overline{\boldsymbol{x}} = \frac{1}{N} \sum_{n=1}^N \boldsymbol{x}_n = \mathbf{0}$，这可以通过数据中心化来保证。

我们希望用低维表示 $ z_n \in \mathbb{R}^L $ 来近似每个 $ x_n $。我们假设每个 $ x_n $ 都可以用基函数 $ w_1, \ldots, w_L $（其中每个 $ w_k \in \mathbb{R}^D $）的加权组合来“解释”，权重由 $ z_n \in \mathbb{R}^L $ 给出，即我们假设 $ x_n \approx \sum_{k=1}^{L} z_{nk} w_k $。向量 $ z_n $ 是 $ x_n $ 的低维表示，被称为**潜在向量**，因为它由未在数据中观测到的潜在或“隐藏”值组成。这些潜在变量的集合被称为**潜在因子**。

这种近似所产生的误差可以如下度量：

$$  \mathcal{L}(\mathbf{W},\mathbf{Z})=\frac{1}{N}||\mathbf{X}-\mathbf{Z}\mathbf{W}^{\mathsf{T}}||_{F}^{2}=\frac{1}{N}||\mathbf{X}^{\mathsf{T}}-\mathbf{W}\mathbf{Z}^{\mathsf{T}}||_{F}^{2}=\frac{1}{N}\sum_{n=1}^{N}||\mathbf{x}_{n}-\mathbf{W}\mathbf{z}_{n}||^{2}   \tag*{(20.3)}$$

其中 $\mathbf{Z}$ 的行包含 $\mathbf{X}$ 的行的低维版本。这被称为（平均）**重构误差**，因为我们用 $ \hat{\boldsymbol{x}}_n = \boldsymbol{W}\boldsymbol{z}_n $ 来近似每个 $ \boldsymbol{x}_n $。

我们希望最小化该误差，同时约束 $ \mathbf{W} $ 为正交矩阵。下面我们将展示，最优解可通过令 $ \hat{\mathbf{W}} = \mathbf{U}_L $ 得到，其中 $ \mathbf{U}_L $ 包含经验协方差矩阵的 $ L $ 个最大特征值对应的特征向量。

---

##### 20.1.2.1 基本情况

我们首先估计最佳的一维解 $\boldsymbol{w}_1 \in \mathbb{R}^D$。其余的基向量 $\boldsymbol{w}_2$、$\boldsymbol{w}_3$ 等将在后续求解。

设每个数据点对应于第一个基向量的系数为 $\tilde{\mathbf{z}}_1 = [z_{11}, \ldots, z_{N1}] \in \mathbb{R}^N$。重构误差由下式给出：

$$ \mathcal{L}(\boldsymbol{w}_{1},\tilde{\boldsymbol{z}}_{1})=\frac{1}{N}\sum_{n=1}^{N}||\boldsymbol{x}_{n}-z_{n1}\boldsymbol{w}_{1}||^{2}=\frac{1}{N}\sum_{n=1}^{N}(\boldsymbol{x}_{n}-z_{n1}\boldsymbol{w}_{1})^{\top}(\boldsymbol{x}_{n}-z_{n1}\boldsymbol{w}_{1})   \tag*{(20.4)}$$

$$ =\frac{1}{N}\sum_{n=1}^{N}[\boldsymbol{x}_{n}^{\mathsf{T}}\boldsymbol{x}_{n}-2z_{n1}\boldsymbol{w}_{1}^{\mathsf{T}}\boldsymbol{x}_{n}+z_{n1}^{2}\boldsymbol{w}_{1}^{\mathsf{T}}\boldsymbol{w}_{1}]   \tag*{(20.5)}$$

$$ =\frac{1}{N}\sum_{n=1}^{N}[\boldsymbol{x}_{n}^{\mathsf{T}}\boldsymbol{x}_{n}-2z_{n1}\boldsymbol{w}_{1}^{\mathsf{T}}\boldsymbol{x}_{n}+z_{n1}^{2}]   \tag*{(20.6)}$$

因为 $\boldsymbol{w}_1^\top \boldsymbol{w}_1 = 1$（根据正交归一性假设）。对 $z_{n1}$ 求导并令其为零，得到：

$$ \frac{\partial}{\partial\cdot}\mathbf{r}^{\prime}\quad\mathbf{\nabla}-w_{1}^{\mathsf{T}}\mathbf{x}_{n}   \tag*{(20.7)}$$

因此，最优嵌入是通过将数据正交投影到 $\boldsymbol{w}_{1}$ 上获得的（参见 Figure 20.1）。将其代回，得到关于权重的损失函数：

$$ \mathcal{L}(\boldsymbol{w}_{1})=\mathcal{L}(\boldsymbol{w}_{1},\tilde{\boldsymbol{z}}_{1}^{*}(\boldsymbol{w}_{1}))=\frac{1}{N}\sum_{n=1}^{N}[\boldsymbol{x}_{n}^{\top}\boldsymbol{x}_{n}-z_{n1}^{2}]=\mathrm{c o n s t}-\frac{1}{N}\sum_{n=1}^{N}z_{n1}^{2}   \tag*{(20.8)}$$

为了求解 $w_{1}$，注意到：

$$ \mathcal{L}(\boldsymbol{w}_{1})=-\frac{1}{N}\sum_{n=1}^{N}\boldsymbol{z}_{n1}^{2}=-\frac{1}{N}\sum_{n=1}^{N}\boldsymbol{w}_{1}^{\mathsf{T}}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\mathsf{T}}\boldsymbol{w}_{1}=-\boldsymbol{w}_{1}^{\mathsf{T}}\hat{\boldsymbol{\Sigma}}\boldsymbol{w}_{1}   \tag*{(20.9)}$$

其中 $\Sigma$ 是经验协方差矩阵（因为我们假设数据已中心化）。我们可以简单地通过令 $\|\mathbf{w}_1\| \to \infty$ 来优化该损失，因此我们施加约束 $\|\mathbf{w}_1\| = 1$，转而优化：

$$ \tilde{\mathcal{L}}(\boldsymbol{w}_{1})=\boldsymbol{w}_{1}^{\top}\hat{\boldsymbol{\Sigma}}\boldsymbol{w}_{1}-\lambda_{1}(\boldsymbol{w}_{1}^{\top}\boldsymbol{w}_{1}-1)   \tag*{(20.10)}$$

其中 $\lambda_{1}$ 是拉格朗日乘子（参见第 8.5.1 节）。求导并令其为零，我们得到：

$$ \frac{\partial}{\partial\boldsymbol{w}_{1}}\tilde{\mathcal{L}}(\boldsymbol{w}_{1})=2\hat{\boldsymbol{\Sigma}}\boldsymbol{w}_{1}-2\lambda_{1}\boldsymbol{w}_{1}=0   \tag*{(20.11)}$$

$$ \hat{\Sigma}w_{1}=\lambda_{1}w_{1}   \tag*{(20.12)}$$

因此，数据应投影的最优方向是协方差矩阵的一个特征向量。左乘 $\boldsymbol{w}_1^\top$（并利用 $\boldsymbol{w}_1^\top \boldsymbol{w}_1 = 1$），我们得到：

$$ \boldsymbol{w}_{1}^{\top}\hat{\boldsymbol{\Sigma}}\boldsymbol{w}_{1}=\lambda_{1}   \tag*{(20.13)}$$

由于我们希望最大化该量（即最小化损失），我们选择对应于最大特征值的特征向量。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_304_127_866_397.jpg" alt="图像" width="48%" /></div>


<div style="text-align: center;">图 20.4：不同一维向量上投影点的方差示意图。$ v_1 $ 是第一主成分，它最大化投影的方差。$ v_2 $ 是第二主成分，方向与 $ v_1 $ 正交。$ v' $ 是介于 $ v_1 $ 和 $ v_2 $ 之间的某个其他向量。改编自 [Gér19] 的图 8.7。由 pca_projected_variance.ipynb 生成。</div>


##### 20.1.2.2 最优权重向量最大化投影数据的方差

在继续之前，我们做一个有趣的观察。由于数据已经中心化，我们有

$$  \mathbb{E}\left[z_{n1}\right]=\mathbb{E}\left[\boldsymbol{x}_{n}^{\mathsf{T}}\boldsymbol{w}_{1}\right]=\mathbb{E}\left[\boldsymbol{x}_{n}\right]^{\mathsf{T}}\boldsymbol{w}_{1}=0   \tag*{(20.14)}$$

因此，投影数据的方差为

$$  \mathbb{V}\left[\tilde{\mathbf{z}}_{1}\right]=\mathbb{E}\left[\tilde{\mathbf{z}}_{1}^{2}\right]-\left(\mathbb{E}\left[\tilde{\mathbf{z}}_{1}\right]\right)^{2}=\frac{1}{N}\sum_{n=1}^{N}z_{n1}^{2}-0=-\mathcal{L}(\boldsymbol{w}_{1})+\mathrm{c o n s t}   \tag*{(20.15)}$$

由此可知，最小化重构误差等价于最大化投影数据的方差：

$$  \arg\min_{\boldsymbol{w}_{1}}\mathcal{L}(\boldsymbol{w}_{1})=\arg\max_{\boldsymbol{w}_{1}}\mathbb{V}\left[\tilde{\mathbf{z}}_{1}(\boldsymbol{w}_{1})\right]   \tag*{(20.16)}$$

这就是为什么常说 PCA 寻找最大方差方向的原因。（See Figure 20.4 for an illustration.）然而，最小误差形式更容易理解且更具一般性。

##### 20.1.2.3 归纳步骤

现在让我们寻找另一个方向 $ w_2 $，以进一步最小化重构误差，约束条件为 $ w_1^\top w_2 = 0 $ 和 $ w_2^\top w_2 = 1 $。误差为

$$  \mathcal{L}(\boldsymbol{w}_{1},\tilde{\boldsymbol{z}}_{1},\boldsymbol{w}_{2},\tilde{\boldsymbol{z}}_{2})=\frac{1}{N}\sum_{n=1}^{N}||\boldsymbol{x}_{n}-z_{n1}\boldsymbol{w}_{1}-z_{n2}\boldsymbol{w}_{2}||^{2}   \tag*{(20.17)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_215_124_532_385.jpg" alt="图像" width="27%" /></div>

<div style="text-align: center;">$ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_629_124_938_387.jpg" alt="图像" width="26%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图20.5：标准化对身高/体重数据集上PCA的影响。（红色=女性，蓝色=男性。）左图：原始数据的PCA。右图：标准化数据的PCA。由pcaStandardization.ipynb生成。</div>

关于 $w_1$ 和 $z_1$ 的优化得到与之前相同的解。练习20.3要求你证明 $\frac{\partial \mathcal{L}}{\partial \mathbf{z}_2} = 0$ 给出 $z_{n2} = \mathbf{w}_2^\top \mathbf{x}_n$。代入得到

$$ \mathcal{L}(\boldsymbol{w}_{2})=\frac{1}{N}\sum_{n=1}^{N}[\boldsymbol{x}_{n}^{\top}\boldsymbol{x}_{n}-\boldsymbol{w}_{1}^{\top}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\top}\boldsymbol{w}_{1}-\boldsymbol{w}_{2}^{\top}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{\top}\boldsymbol{w}_{2}]=\mathrm{const}-\boldsymbol{w}_{2}^{\top}\hat{\boldsymbol{\Sigma}}\boldsymbol{w}_{2} \tag*{(20.18)}$$

去掉常数项，代入最优的 $w_1$ 并添加约束得到

$$ \tilde{\mathcal{L}}(\boldsymbol{w}_{2})=-\boldsymbol{w}_{2}^{\top}\hat{\boldsymbol{\Sigma}}\boldsymbol{w}_{2}+\lambda_{2}(\boldsymbol{w}_{2}^{\top}\boldsymbol{w}_{2}-1)+\lambda_{12}(\boldsymbol{w}_{2}^{\top}\boldsymbol{w}_{1}-0) \tag*{(20.19)}$$

练习20.3要求你证明解由第二大特征值对应的特征向量给出：

$$ \hat{\Sigma}w_{2}=\lambda_{2}w_{2} \tag*{(20.20)}$$

证明继续下去，表明 $\hat{\mathbf{W}} = \mathbf{U}_L$。

#### 20.1.3 计算问题

本节我们讨论与使用PCA相关的各种实际问题。

##### 20.1.3.1 协方差矩阵与相关系数矩阵

我们一直在使用协方差矩阵的特征分解。然而，更好的做法是使用相关系数矩阵。原因在于，否则PCA可能会被那些仅仅由于测量尺度不同而方差较大的方向“误导”。图20.5显示了这样一个例子。左图中，我们看到纵轴的范围大于横轴，导致第一主成分看起来有些“不自然”。右图展示了标准化数据后的PCA结果（这等价于使用相关系数矩阵而非协方差矩阵）；结果看起来好得多。

---

##### 20.1.3.2 高维数据的处理

我们将PCA表述为求解 $ D \times D $ 协方差矩阵 $ \mathbf{X}^\top \mathbf{X} $ 的特征向量的问题。如果 $ D > N $，则使用 $ N \times N $ 格拉姆矩阵 $ \mathbf{X} \mathbf{X}^\top $ 计算更快。下面展示具体方法。

首先，令 $\mathbf{U}$ 为包含 $\mathbf{XX}^{\top}$ 特征向量的标准正交矩阵，对应特征值在 $\mathbf{\Lambda}$ 中。根据定义有 $(\mathbf{XX}^{\top})\mathbf{U}=\mathbf{U}\mathbf{\Lambda}$。左乘 $\mathbf{X}^{\top}$ 得到

$$  (\mathbf{X}^{\mathsf{T}}\mathbf{X})(\mathbf{X}^{\mathsf{T}}\mathbf{U})=(\mathbf{X}^{\mathsf{T}}\mathbf{U})\mathbf{\Lambda}   \tag*{(20.21)}$$

从中可见 $\mathbf{X}^\top \mathbf{X}$ 的特征向量为 $\mathbf{V} = \mathbf{X}^\top \mathbf{U}$，特征值仍由 $\Lambda$ 给出。然而这些特征向量未归一化，因为 $\|\mathbf{v}_j\|^2 = \mathbf{u}_j^\top \mathbf{X} \mathbf{X}^\top \mathbf{u}_j = \lambda_j \mathbf{u}_j^\top \mathbf{u}_j = \lambda_j$。归一化后的特征向量为

$$  \mathbf{V}=\mathbf{X}^{\mathsf{T}}\mathbf{U}\mathbf{\Lambda}^{-\frac{1}{2}}   \tag*{(20.22)}$$

这提供了计算PCA基的另一种方式。同时也使得我们可以使用核技巧，如第20.4.6节所述。

##### 20.1.3.3 使用SVD计算PCA

在本节中，我们展示使用特征向量方法（第20.1节）计算的PCA与截断SVD之间的等价性。¹

令 $\mathbf{U}_{\Sigma} \mathbf{\Lambda}_{\Sigma} \mathbf{U}_{\Sigma}^{\mathrm{T}}$ 为协方差矩阵 $\mathbf{\Sigma} \propto \mathbf{X}^{\mathrm{T}} \mathbf{X}$ 的前 $L$ 个特征分解（假设 $\mathbf{X}$ 已中心化）。由第20.1.2节可知，投影权重 $\mathbf{W}$ 的最优估计由前 $L$ 个特征值给出，因此 $\mathbf{W} = \mathbf{U}_{\Sigma}$。

现在令 $\mathbf{U}_X \mathbf{S}_X \mathbf{V}_X^\top \approx \mathbf{X}$ 为数据矩阵 $\mathbf{X}$ 的 $L$ 截断SVD近似。由等式(7.184)可知，$\mathbf{X}$ 的右奇异向量是 $\mathbf{X}^\top \mathbf{X}$ 的特征向量，因此 $\mathbf{V}_X = \mathbf{U}_\Sigma = \mathbf{W}$。（此外，协方差矩阵的特征值与数据矩阵的奇异值通过 $\lambda_k = s_k^2 / N$ 关联。）

现在假设我们关心投影点（也称为主成分或PC得分），而非投影矩阵。我们有

$$  \mathbf{Z}=\mathbf{X}\mathbf{W}=\mathbf{U}_{X}\mathbf{S}_{X}\mathbf{V}_{X}^{\top}\mathbf{V}_{X}=\mathbf{U}_{X}\mathbf{S}_{X}   \tag*{(20.23)}$$

最后，如果我们要近似重构数据，则有

$$  \hat{\mathbf{X}}=\mathbf{Z}\mathbf{W}^{\mathsf{T}}=\mathbf{U}_{X}\mathbf{S}_{X}\mathbf{V}_{X}^{\mathsf{T}}   \tag*{(20.24)}$$

这与截断SVD近似（第7.5.5节）完全相同。

因此我们看到，可以通过 $\Sigma$ 的特征分解或 $\mathbf{X}$ 的SVD分解来进行PCA。由于计算上的原因，后者通常更可取。对于非常高维的问题，我们可以使用随机化SVD算法，例如参见 [HMT11; SKT14; DM16]。例如，sklearn 使用的随机化求解器对于 $N$ 个样本和 $L$ 个主成分所需时间为 $O(NL^2) + O(L^3)$，而精确SVD需要 $O(ND^2) + O(D^3)$ 时间。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_251_121_506_334.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_658_122_914_335.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图20.6: MNIST上重构误差与PCA使用的潜在维度数的关系。(a)训练集。(b)测试集。由pcaOverfitDemo.ipynb生成。</div>


#### 20.1.4 选择潜在维度数

本节讨论如何为PCA选择潜在维度数L。

##### 20.1.4.1 重构误差

定义模型在使用L个维度时，在数据集D上产生的重构误差：

$$  \mathcal{L}_{L}=\frac{1}{|\mathcal{D}|}\sum_{n\in\mathcal{D}}||\boldsymbol{x}_{n}-\hat{\boldsymbol{x}}_{n}||^{2}   \tag*{(20.25)}$$

其中重构由 $ \hat{\mathbf{x}}_n = \mathbf{W}\mathbf{z}_n + \boldsymbol{\mu} $ 给出，这里 $ \mathbf{z}_n = \mathbf{W}^\top(\mathbf{x}_n - \boldsymbol{\mu}) $， $ \boldsymbol{\mu} $ 是经验均值， $ \mathbf{W} $ 按上述方式估计。图20.6(a)绘制了MNIST训练数据上 $ \mathcal{L}_L $ 随 $ L $ 变化的曲线。我们看到误差下降得相当快，表明我们能够用少量因子捕获像素的大部分经验相关性。

当然，如果我们使用 $ L = \text{rank}(\mathbf{X}) $，则训练集上的重构误差为零。为了避免过拟合，通常会在测试集上绘制重构误差。如图20.6(b)所示。这里我们看到，即使模型变得更复杂，误差仍在继续下降！因此，我们没有得到监督学习中通常预期的U形曲线。问题在于PCA并非一个真正的数据生成模型：如果提供更多潜在维度，它就能更准确地逼近测试数据。（类似的问题也会出现在使用K-means聚类时绘制测试集上的重构误差，如第21.3.7节所述。）下面我们讨论一些解决方案。

##### 20.1.4.2 碎石图

一种常见的替代方案（替代绘制重构误差与L的关系）是使用称为碎石图的方法，即按降序绘制特征值 $ \lambda_{j} $ 与 j 的关系。可以证明

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_248_121_505_334.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_656_126_913_336.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图20.7：(a) 训练集的碎石图，对应图20.6(a)。(b) 方差解释比例。由pcaOverfitDemo.ipynb生成。</div>


（习题20.4）可得

$$  \mathcal{L}_{L}=\sum_{j=L+1}^{D}\lambda_{j}   \tag*{(20.26)}$$

因此，随着维度数量的增加，特征值变小，重构误差也随之减小，如图20.7a所示。 $ ^{2} $ 一个相关的量是方差解释比例，定义如下

$$  F_{L}=\frac{\sum_{j=1}^{L}\lambda_{j}}{\sum_{j^{\prime}=1}^{L^{\max}}\lambda_{j^{\prime}}}   \tag*{(20.27)}$$

该量捕捉了与碎石图相同的信息，但随 $L$ 增加而增大（见图20.7b）。

##### 20.1.4.3 轮廓似然

尽管重构误差图中没有U形，但曲线有时会出现“膝盖”或“肘部”，即误差突然从相对较大的值变为相对较小的值。其思想是，对于 $L < L^*$，其中 $L^*$ 是“真实”的潜在维度（或簇数），误差函数的下降速率将很高；而对于 $L > L^*$，增益将较小，因为模型已经足够复杂以捕捉真实分布。

自动化检测曲线梯度变化的一种方法是计算轮廓似然，如[ZG06]所述。其思想如下：令 $\lambda_L$ 为模型大小 $L$ 所产生误差的某种度量，且满足 $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_{L^{\max}}$。在PCA中，这些是特征值，但该方法也可以应用于K-means聚类的重构误差（见第21.3.7节）。现在考虑将这些值分为两组，取决于 $k < L$ 还是 $k > L$，其中 $L$ 是我们将要确定的某个阈值。为了衡量 $L$ 的质量，

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_444_129_707_333.jpg" alt="图像" width="22%" /></div>

<div style="text-align: center;">图20.8：对应图20.6(a)中主成分分析(PCA)模型的轮廓似然。由pcaOverfit-Demo.ipynb生成。</div>

我们将使用一个简单的变点模型，其中若 \(k \leq L\)，则 \(\lambda_k \sim \mathcal{N}(\mu_1, \sigma^2)\)；若 \(k > L\)，则 \(\lambda_k \sim \mathcal{N}(\mu_2, \sigma^2)\)。（重要的是，两个模型的 \(\sigma^2\) 必须相同，以防止在某个区域的数据少于另一个区域时出现过拟合。）在每个区域内，我们假设 \(\lambda_k\) 独立同分布（iid），这显然不正确，但对当前目的来说足够。我们可以通过划分数据并计算最大似然估计（MLEs），使用方差的合并估计来拟合每个 \(L = 1 : L^{\max}\) 的模型：

$$  \mu_{1}(L)=\frac{\sum_{k\leq L}\lambda_{k}}{L}   \tag*{(20.28)}$$

$$  \mu_{2}(L)=\frac{\sum_{k>L}\lambda_{k}}{L^{\max}-L}   \tag*{(20.29)}$$

$$  \sigma^{2}(L)=\frac{\sum_{k\leq L}(\lambda_{k}-\mu_{1}(L))^{2}+\sum_{k>L}(\lambda_{k}-\mu_{2}(L))^{2}}{L^{\max}}   \tag*{(20.30)}$$

然后我们可以评估轮廓对数似然：

$$  \ell(L)=\sum_{k=1}^{L}\log\mathcal{N}(\lambda_{k}|\mu_{1}(L),\sigma^{2}(L))+\sum_{k=L+1}^{L^{\max}}\log\mathcal{N}(\lambda_{k}|\mu_{2}(L),\sigma^{2}(L))   \tag*{(20.31)}$$

这在Figure 20.8中得以说明。我们看到峰值 \(L^{*}=\arg\max\ell(L)\) 确定得很好。

### 20.2 因子分析 *

主成分分析(PCA)是一种计算数据线性低维表示的简单方法。在本节中，我们介绍一种称为因子分析(FA)的概率模型的推广。它基于概率模型，这意味着我们可以将其视为更复杂模型的构建块，例如20.2.6节中的混合因子分析模型，或20.3.5节中的非线性因子分析模型。正如我们在20.2.2节中讨论的，我们可以将PCA恢复为FA的一个特殊极限情况。

---

#### 20.2.1 生成模型

因子分析对应于以下线性-高斯潜变量生成模型：

$$  p(z)=\mathcal{N}(z|\mu_{0},\Sigma_{0})   \tag*{(20.32)}$$

$$  p(x|z,\theta)=\mathcal{N}(x|\mathbf{W}z+\mu,\Psi)   \tag*{(20.33)}$$

其中 $\mathbf{W}$ 是一个 $D \times L$ 矩阵，称为因子载荷矩阵，$\Psi$ 是一个对角 $D \times D$ 协方差矩阵。

FA 可以视为高斯分布的低秩版本。为了理解这一点，注意到推导出的边缘分布 $p(\boldsymbol{x}|\boldsymbol{\theta})$ 是一个高斯分布（推导见公式(3.38)）：

$$  \begin{align*}p(\boldsymbol{x}|\boldsymbol{\theta})&=\int\mathcal{N}(\boldsymbol{x}|\mathbf{W}\boldsymbol{z}+\boldsymbol{\mu},\boldsymbol{\Psi})\mathcal{N}(z|\boldsymbol{\mu}_{0},\boldsymbol{\Sigma}_{0})dz\\&=\mathcal{N}(\boldsymbol{x}|\mathbf{W}\boldsymbol{\mu}_{0}+\boldsymbol{\mu},\boldsymbol{\Psi}+\mathbf{W}\boldsymbol{\Sigma}_{0}\mathbf{W}^{\top})\end{align*}   \tag*{(20.34)}$$

因此 $\mathbb{E}[\boldsymbol{x}] = \mathbf{W}\boldsymbol{\mu}_{0} + \boldsymbol{\mu}$ 且 $\operatorname{Cov}[\boldsymbol{x}] = \mathbf{W}\operatorname{Cov}[\boldsymbol{z}] \mathbf{W}^{\top} + \boldsymbol{\Psi} = \mathbf{W}\boldsymbol{\Sigma}_{0} \mathbf{W}^{\top} + \boldsymbol{\Psi}$。由此可知，我们可以不失一般性地设 $\boldsymbol{\mu}_{0} = \mathbf{0}$，因为总可以将 $\mathbf{W}\boldsymbol{\mu}_{0}$ 吸收进 $\boldsymbol{\mu}$。类似地，可以不失一般性地设 $\boldsymbol{\Sigma}_{0} = \mathbf{I}$，因为总是可以通过使用新的权重矩阵 $\tilde{\mathbf{W}} = \mathbf{W}\boldsymbol{\Sigma}_{0}^{-\frac{1}{2}}$ 来吸收相关先验。经过这些简化，我们得到：

$$  p(\boldsymbol{z})=\mathcal{N}(\boldsymbol{z}|\mathbf{0},\mathbf{I})   \tag*{(20.36)}$$

$$  p(\boldsymbol{x}|\boldsymbol{z})=\mathcal{N}(\boldsymbol{x}|\mathbf{W}\boldsymbol{z}+\boldsymbol{\mu},\boldsymbol{\Psi})   \tag*{(20.37)}$$

$$  p(\boldsymbol{x})=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu},\mathbf{W}\mathbf{W}^{\mathrm{T}}+\boldsymbol{\Psi})   \tag*{(20.38)}$$

例如，假设 $L = 1$，$D = 2$ 且 $\Psi = \sigma^2\mathbf{I}$。我们在此情形下的生成过程如图20.9所示。可以将其想象为一个各向同性高斯“喷漆罐”，代表似然 $p(\mathbf{x}|\mathbf{z})$，当我们变化一维潜变量先验 $z$ 时，它沿着由 $\mathbf{w}z + \mu$ 定义的一维线“滑动”。这就在二维空间中生成了一个拉伸（因而相关）的高斯分布。即，推导出的分布形式为 $v(\mathbf{x}) = \mathcal{N}(\mathbf{x}|\mathbf{u}. \mathbf{w}\mathbf{w}^\top + \sigma^2\mathbf{I})$。

一般来说，FA 使用低秩分解来逼近可见向量的协方差矩阵：

$$  \mathbf{C}=\mathrm{Cov}\left[\mathbf{x}\right]=\mathbf{W}\mathbf{W}^{\top}+\boldsymbol{\Psi}   \tag*{(20.39)}$$

这仅使用 $O(LD)$ 个参数，在全协方差高斯（$O(D^{2})$ 个参数）和对角协方差（$O(D)$ 个参数）之间提供了一个灵活的折中方案。

从公式(20.39)可以看出，我们应该限制 $\Psi$ 为对角矩阵，否则可以设 $\mathbf{W} = \mathbf{0}$，从而忽略潜因子，同时仍能建模任意协方差。每个可见变量的边缘方差由 $\mathbb{V}[x_d] = \sum_{k=1}^L w_d^2 + \psi_d$ 给出，其中第一项是由公共因子引起的方差，第二项 $\psi_d$ 称为独特性，是该维度特有的方差项。

我们可以使用 EM 算法（见第20.2.3节）估计 FA 模型的参数。模型拟合后，我们可以利用 $p(z|\pmb{x})$ 计算概率潜嵌入。根据高斯分布的贝叶斯规则，我们有：

$$  p(z|\boldsymbol{x})=\mathcal{N}(z|\mathbf{W}^{\mathsf{T}}\mathbf{C}^{-1}(\boldsymbol{x}-\boldsymbol{\mu}),\mathbf{I}-\mathbf{W}^{\mathsf{T}}\mathbf{C}^{-1}\mathbf{W})   \tag*{(20.40)}$$

其中 C 在公式(20.39)中定义。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_193_130_982_389.jpg" alt="图像" width="68%" /></div>


<div style="text-align: center;">图 20.9: FA 生成过程的示意图，其中我们使用 $L = 1$ 个潜伏维度生成 $D = 2$ 个观测维度；假设 $\Psi = \sigma^2 \mathbf{I}$。潜伏因子的取值为 $z \in \mathbb{R}$，从 $p(z)$ 中采样得到；该值被映射为一个 $2$ 维偏移量 $\delta = zw$，其中 $\mathbf{w} \in \mathbb{R}^2$，该偏移量被加到 $\mu$ 上，从而定义了一个高斯分布 $p(\mathbf{x}|z) = \mathcal{N}(\mathbf{x}|\boldsymbol{\mu} + \delta, \sigma^2 \mathbf{I})$。通过对 $z$ 进行积分，我们沿着主成分轴 $\mathbf{w}$ “滑动”这个圆形高斯“喷罐”，从而在 $\mathbf{x}$ 空间中诱导出以 $\boldsymbol{\mu}$ 为中心的椭圆高斯等值线。改编自 [Bis06] 的图 12.9。</div>


#### 20.2.2 概率主成分分析

在本节中，我们考虑因子分析模型的一个特例，其中 $\mathbf{W}$ 具有标准正交列，且 $\mathbf{\Psi} = \sigma^2 \mathbf{I}$。该模型称为**概率主成分分析**（probabilistic principal components analysis, PPCA）[TB99]，或称为合理的 PCA（sensible PCA）[Row97]。可见变量的边缘分布的形式为

$$  p(\boldsymbol{x}|\boldsymbol{\theta})=\int\mathcal{N}(\boldsymbol{x}|\mathbf{W}\boldsymbol{z},\sigma^{2}\mathbf{I})\mathcal{N}(\boldsymbol{z}|\mathbf{0},\mathbf{I})d\boldsymbol{z}=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu},\mathbf{C})   \tag*{(20.41)}$$

其中

$$  \mathbf{C}=\mathbf{W}\mathbf{W}^{\mathsf{T}}+\sigma^{2}\mathbf{I}   \tag*{(20.42)}$$

PPCA 的对数似然由下式给出

$$  \log p(\mathbf{X}|\boldsymbol{\mu},\mathbf{W},\sigma^{2})=-\frac{N D}{2}\log(2\pi)-\frac{N}{2}\log|\mathbf{C}|-\frac{1}{2}\sum_{n=1}^{N}(\boldsymbol{x}_{n}-\boldsymbol{\mu})^{\mathsf{T}}\mathbf{C}^{-1}(\boldsymbol{x}_{n}-\boldsymbol{\mu})   \tag*{(20.43)}$$

$\mu$ 的 MLE 为 $\overline{x}$。代入后得到

$$  \log p(\mathbf{X}|\boldsymbol{\mu},\mathbf{W},\sigma^{2})=-\frac{N}{2}\left[D\log(2\pi)+\log|\mathbf{C}|+\mathrm{tr}(\mathbf{C}^{-1}\mathbf{S})\right]   \tag*{(20.44)}$$

其中 $\mathbf{S} = \frac{1}{N} \sum_{n=1}^{N} (\boldsymbol{x}_{n} - \overline{\boldsymbol{x}}) (\boldsymbol{x}_{n} - \overline{\boldsymbol{x}})^{\top}$ 是经验协方差矩阵。

在 [TB99; Row97] 中，他们证明该目标的最大值必须满足

$$  \mathbf{W}=\mathbf{U}_{L}(\mathbf{L}_{L}-\sigma^{2}\mathbf{I})^{\frac{1}{2}}\mathbf{R}   \tag*{(20.45)}$$

---

其中 $\mathbf{U}_L$ 是一个 $D \times L$ 矩阵，其列由 $\mathbf{S}$ 的 $L$ 个具有最大特征值的特征向量给出，$\mathbf{L}_L$ 是特征值的 $L \times L$ 对角矩阵，$\mathbf{R}$ 是一个任意的 $L \times L$ 正交矩阵，不失一般性，我们可以取 $\mathbf{R} = \mathbf{I}$。在无噪声极限 $\sigma^2 = 0$ 下，我们得到 $\mathbf{W}_{\text{mle}} = \mathbf{U}_L \mathbf{L}_L^{\frac{1}{2}}$，这与 PCA 解成正比。

观测方差的极大似然估计为

$$  \sigma^{2}=\frac{1}{D-L}\sum_{i=L+1}^{D}\lambda_{i}   \tag*{(20.46)}$$

这是与被舍弃维度相关的平均失真。如果 $L = D$，则估计噪声为 0，因为模型退化为 $z = x$。

为了计算似然 $ p(\mathbf{X}|\boldsymbol{\mu},\mathbf{W},\sigma^2) $，我们需要计算 $ \mathbf{C}^{-1} $ 和 $ \log|\mathbf{C}| $，其中 $ \mathbf{C} $ 是一个 $ D \times D $ 矩阵。为此，我们可以利用矩阵求逆引理写出

$$  \mathbf{C}^{-1}=\sigma^{-2}\left[\mathbf{I}-\mathbf{W}\mathbf{M}^{-1}\mathbf{W}^{\mathsf{T}}\right]   \tag*{(20.47)}$$

其中 $ L \times L $ 维矩阵 $\mathbf{M}$ 由下式给出

$$  \mathbf{M}=\mathbf{W}^{\mathsf{T}}\mathbf{W}+\sigma^{2}\mathbf{I}   \tag*{(20.48)}$$

当我们代入公式 (20.45) 中 $\mathbf{W}$ 的极大似然估计（使用 $\mathbf{R} = \mathbf{I}$）时，得到

$$  \mathbf{M}=\mathbf{U}_{L}(\mathbf{L}_{L}-\sigma^{2}\mathbf{I})\mathbf{U}_{L}^{\top}+\sigma^{2}\mathbf{I}   \tag*{(20.49)}$$

进而有

$$  \mathbf{C}^{-1}=\sigma^{-2}\left[\mathbf{I}-\mathbf{U}_{L}(\mathbf{L}_{L}-\sigma^{2}\mathbf{I})\boldsymbol{\Lambda}_{L}^{-1}\mathbf{U}_{L}^{\mathsf{T}}\right]   \tag*{(20.50)}$$

$$  \log\left|\mathbf{C}\right|=\left(D-L\right)\log\sigma^{2}+\sum_{j=1}^{L}\log\lambda_{j}   \tag*{(20.51)}$$

因此我们可以避免所有矩阵求逆（因为 $\Lambda_L^{-1} = \mathrm{diag}(1/\lambda_j)$）。

为了将 PPCA 用作 PCA 的替代方法，我们需要计算后验均值 $ \mathbb{E}[z|\boldsymbol{x}] $，这相当于编码器模型。利用高斯分布的贝叶斯规则，我们有

$$  p(z|\boldsymbol{x})=\mathcal{N}(z|\mathbf{M}^{-1}\mathbf{W}^{\mathsf{T}}(\boldsymbol{x}-\boldsymbol{\mu}),\sigma^{2}\mathbf{M}^{-1})   \tag*{(20.52)}$$

其中 $\mathbf{M}$ 由公式 (20.48) 定义。在 $\sigma^{2}=0$ 的极限下，使用极大似然估计参数的后验均值变为

$$  \mathbb{E}\left[z|x\right]=\left(\mathbf{W}^{\mathsf{T}}\mathbf{W}\right)^{-1}\mathbf{W}^{\mathsf{T}}(x-\overline{x})   \tag*{(20.53)}$$

这是将数据正交投影到潜空间，与标准 PCA 一致。

#### 20.2.3 FA/PPCA 的 EM 算法

在本节中，我们描述一种基于 [RT82; GH96] 的方法，利用 EM 算法计算 FA 模型的极大似然估计。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

##### 20.2.3.1 因子分析的EM算法

在E步中，我们计算后验嵌入

$$  p(z_{i}|\boldsymbol{x}_{i},\boldsymbol{\theta})=\mathcal{N}(z_{i}|\boldsymbol{m}_{i},\boldsymbol{\Sigma}_{i})   \tag*{(20.54)}$$

$$  \mathbf{\Sigma}_{i}\triangleq(\mathbf{I}_{L}+\mathbf{W}^{\mathsf{T}}\mathbf{\Psi}^{-1}\mathbf{W})^{-1}   \tag*{(20.55)}$$

$$  m_{i}\triangleq\Sigma_{i}(\mathbf{W}^{\mathsf{T}}\mathbf{\Psi}^{-1}(\mathbf{x}_{i}-\mathbf{\mu}))   \tag*{(20.56)}$$

在M步中，通过定义 $ \tilde{\mathbf{W}} = (\mathbf{W}, \boldsymbol{\mu}) $, $ \tilde{\mathbf{z}} = (\mathbf{z}, 1) $, 可以同时估计 $ \mu $ 和 $ \mathbf{W} $。此外，定义

$$  b_{i}\triangleq\mathbb{E}\left[\tilde{\mathbf{z}}|\mathbf{x}_{i}\right]=[m_{i};1]   \tag*{(20.57)}$$

$$  \mathbf{C}_{i}\triangleq\mathbb{E}\left[\tilde{\mathbf{z}}\tilde{\mathbf{z}}^{T}|\mathbf{x}_{i},\right]=\begin{pmatrix}\mathbb{E}\left[\mathbf{z}\mathbf{z}^{T}|\mathbf{x}_{i}\right]&\mathbb{E}\left[\mathbf{z}|\mathbf{x}_{i}\right]\\\mathbb{E}\left[\mathbf{z}|\mathbf{x}_{i}\right]^{T}&1\end{pmatrix}   \tag*{(20.58)}$$

那么M步如下：

$$  \hat{\tilde{\mathbf{W}}}=\left[\sum_{i}\boldsymbol{x}_{i}\boldsymbol{b}_{i}^{\top}\right]\left[\sum_{i}\mathbf{C}_{i}\right]^{-1}   \tag*{(20.59)}$$

$$  \hat{\boldsymbol{\Psi}}=\frac{1}{N}\mathrm{diag}\left\{\sum_{i}\left(\boldsymbol{x}_{i}-\hat{\tilde{\boldsymbol{W}}}\boldsymbol{b}_{i}\right)\boldsymbol{x}_{i}^{T}\right\}   \tag*{(20.60)}$$

注意这些更新是针对“标准”EM算法的。基于ECM的更快版本算法见[ZY08]。

##### 20.2.3.2 （概率）主成分分析的EM算法

我们也可以使用EM来拟合PPCA模型，这为特征向量方法提供了一种有用的替代方案。该算法依赖于PCA的概率公式。然而，如[Row97]所示，该算法在零噪声极限 $ \sigma^2 = 0 $ 下仍然有效。

特别地，设 $ \mathbf{Z} = \mathbf{Z}^\top $ 是一个 $ L \times N $ 的矩阵，其列存储后验均值（低维表示）。类似地，设 $ \tilde{\mathbf{X}} = \mathbf{X}^\top $ 存储原始数据。根据方程(20.52)，当 $ \sigma^2 = 0 $ 时，我们有

$$  \tilde{\mathbf{Z}}=(\mathbf{W}^{T}\mathbf{W})^{-1}\mathbf{W}^{T}\tilde{\mathbf{X}}   \tag*{(20.61)}$$

这构成了E步。注意这仅是数据的一个正交投影。

根据方程20.59，M步由下式给出

$$  \hat{\mathbf{W}}=\left[\sum_{i}\mathbf{x}_{i}\mathbb{E}\left[\mathbf{z}_{i}\right]^{T}\right]\left[\sum_{i}\mathbb{E}\left[\mathbf{z}_{i}\right]\mathbb{E}\left[\mathbf{z}_{i}\right]^{T}\right]^{-1}   \tag*{(20.62)}$$

其中我们利用了当 $ \sigma^2 = 0 $ 时 $ \Sigma = \mathrm{Cov}\left[z_i | x_i, \theta\right] = 0 $ 这一事实。

值得将这个表达式与多输出线性回归的MLE（方程11.2）进行比较，其形式为 $ \mathbf{W} = (\sum_i \mathbf{y}_i \mathbf{x}_i^T)(\sum_i \mathbf{x}_i \mathbf{x}_i^T)^{-1} $。因此我们看到，M步类似于线性回归，只是将观测到的输入替换为潜在变量的期望值。