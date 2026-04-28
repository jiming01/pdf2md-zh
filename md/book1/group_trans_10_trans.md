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

该过程的可视化见图14.5。

我们可以将二维卷积理解为**模板匹配**，因为如果以 $(i, j)$ 为中心的图像块与模板 W 相似，那么点 $(i, j)$ 处的输出就会很大。如果模板 W 对应一个定向边缘，那么与之卷积后，输出的“热力图”会在包含匹配该方向边缘的区域“点亮”，如图14.6所示。更一般地，我们可以将卷积视为一种特征检测形式。由此得到的输出 $\mathbf{Y} = \mathbf{W} \otimes \mathbf{X}$ 被称为**特征图**。

##### 14.2.1.3 卷积作为矩阵向量乘法

由于卷积是线性算子，我们可以用矩阵乘法来表示它。例如，考虑方程(14.7)。我们可以通过将二维矩阵 X 展平为一维向量 $\boldsymbol{x}$，并乘以一个由核 W 导出的托普利茨矩阵 C 来将其重写为矩阵向量乘法，如下所示：

$$  \begin{aligned}\boldsymbol{y}&=\mathbf{C}\boldsymbol{x}=\left(\begin{array}{ccc|ccc|ccc}{{{w_{1}}}}&{{{w_{2}}}}&{{{0}}}&{{{w_{3}}}}&{{{w_{4}}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{w_{1}}}}&{{{w_{2}}}}&{{{0}}}&{{{w_{3}}}}&{{{w_{4}}}}&{{{0}}}&{{{0}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0}}}&{{{w_{1}}}}&{{{w_{2}}}}&{{{0}}}&{{{w_{3}}}}&{{{w_{4}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{0}}}&{{{0}}}&{{{w_{1}}}}&{{{w_{2}}}}&{{{0}}}&{{{w_{3}}}}&{{{w_{4}}}}\end{array}\right)\left(\begin{aligned}{{{x_{1}}}} \\{{{x_{2}}}} \\{{{x_{3}}}} \\{{{x_{4}}}} \\{{{x_{5}}}} \\{{{x_{6}}}} \\{{{x_{7}}}} \\{{{x_{8}}}} \\{{{x_{9}}}}\end{aligned}\right)\\&=\left(\begin{aligned}{{{w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{4}+w_{4}x_{5}}}} \\{{{w_{1}x_{2}+w_{2}x_{3}+w_{3}x_{5}+w_{4}x_{6}}}} \\{{{w_{1}x_{4}+w_{2}x_{5}+w_{3}x_{7}+w_{4}x_{8}}}} \\{{{w_{1}x_{5}+w_{2}x_{6}+w_{3}x_{8}+w_{4}x_{9}}}}\end{aligned}\right)\end{aligned}   \tag*{(14.8)}$$

我们可以通过将 $4 \times 1$ 向量 $\boldsymbol{y}$ 重新整形回 $2 \times 2$ 的 $\mathbf{Y}$ 来恢复输出。$^{1}$

由此可见，CNN 类似于权重矩阵具有特殊稀疏结构且元素在空间位置上共享的 MLP。这实现了平移不变性的思想，并且与 MLP 中使用的标准全连接层或密集层中的权重矩阵相比，极大地减少了参数数量。

##### 14.2.1.4 边界条件与填充

在方程(14.7)中，我们看到将 $3 \times 3$ 的图像与 $2 \times 2$ 的滤波器卷积，得到了 $2 \times 2$ 的输出。一般来说，将 $f_h \times f_w$ 的滤波器在大小为 $x_h \times x_w$ 的图像上进行卷积，会产生大小为 $(x_h - f_h + 1) \times (x_w - f_w + 1)$ 的输出；这被称为**有效卷积** (valid convolution)，因为我们只将滤波器应用于输入的“有效”部分，即不让它“滑出边界”。如果我们希望输出与输入具有相同的大小，可以使用**零填充** (zero-padding)，即在图像周围添加一圈 0 边界，如图14.7所示。这被称为**同卷积** (same convolution)。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_380_115_800_411.jpg" alt="图像" width="36%" /></div>


<div style="text-align: center;">图14.7: 同卷积（使用零填充）确保输出与输入尺寸相同。改编自[SAV20]的图8.3。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_217_524_538_751.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_605_532_924_759.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图14.8: 二维卷积中填充和步幅的说明。(a) 我们使用 $ 3 \times 3 $ 滤波器对 $ 5 \times 7 $ 的输入（带零填充）应用“同卷积”，生成 $ 5 \times 7 $ 的输出。(b) 现在使用步幅为2，因此输出尺寸为 $ 3 \times 4 $。改编自[Gér19]的图14.3–14.4。</div>


一般来说，如果输入尺寸为 $ x_h \times x_w $，我们使用尺寸为 $ f_h \times f_w $ 的核，每侧零填充的尺寸为 $ p_h $ 和 $ p_w $，那么输出具有以下尺寸[DV16]：

$$  \left(x_{h}+2p_{h}-f_{h}+1\right)\times\left(x_{w}+2p_{w}-f_{w}+1\right)   \tag*{(14.10)}$$

例如，考虑图14.8a。我们有 $p = 1$, $f = 3$, $x_{h} = 5$ 且 $x_{w} = 7$，因此输出尺寸为

$$  \left(5+2-3+1\right)\times\left(7+2-3+1\right)=5\times7   \tag*{(14.11)}$$

如果设置 $2p = f - 1$，那么输出将与输入具有相同的尺寸。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_248_123_922_404.jpg" alt="图像" width="58%" /></div>


<div style="text-align: center;">图 14.9：对具有 2 个通道的输入应用二维卷积的示意图。由 conv2d_jax.ipynb 生成。改编自 [Zha+20] 的图 6.4.1。</div>


##### 14.2.1.5 步长卷积

由于每个输出像素是通过其感受野内输入（基于滤波器大小）的加权组合生成的，因此相邻输出在数值上会非常相似，因为它们的输入存在重叠。我们可以通过每隔 s 个输入跳过一个来减少这种冗余（并加速计算）。这称为 **步长卷积**。图 14.8b 对此进行了说明，其中我们将一个 $5 \times 7$ 的图像与一个步长为 2 的 $3 \times 3$ 滤波器进行卷积，得到 $3 \times 4$ 的输出。

一般情况下，如果输入尺寸为 $x_h \times x_w$，使用的卷积核大小为 $f_h \times f_w$，每侧零填充的大小为 $p_h$ 和 $p_w$，步长大小为 $s_h$ 和 $s_w$，则输出尺寸如下 [DV16]：

$$  \left\lfloor\frac{x_{h}+2p_{h}-f_{h}+s_{h}}{s_{h}}\right\rfloor\times\left\lfloor\frac{x_{w}+2p_{w}-f_{w}+s_{w}}{s_{w}}\right\rfloor   \tag*{(14.12)}$$

例如，考虑图 14.8b，其中我们将步长设为 s = 2。此时输出比输入小，尺寸为

$$  \left\lfloor\frac{5+2-3+2}{2}\right\rfloor\times\left\lfloor\frac{7+2-3+2}{2}\right\rfloor=\left\lfloor\frac{6}{2}\right\rfloor\times\left\lfloor\frac{4}{1}\right\rfloor=3\times4   \tag*{(14.13)}$$

##### 14.2.1.6 多输入与多输出通道

在图 14.6 中，输入是一幅灰度图像。一般情况下，输入具有多个通道（例如，RGB 或卫星图像的高光谱波段）。我们可以通过为每个输入通道定义一个卷积核来将卷积的定义推广到这种情况；此时 $\mathbf{W}$ 是一个三维权重矩阵或张量。我们通过将输入通道 $c$ 与卷积核 $\mathbf{W}_{:,c}$ 进行卷积，然后对所有通道求和来计算输出：

$$  z_{i,j}=b+\sum_{u=0}^{H-1}\sum_{v=0}^{W-1}\sum_{c=0}^{C-1}x_{si+u,sj+v,c}w_{u,v,c}   \tag*{(14.14)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_341_163_826_525.jpg" alt="Image" width="42%" /></div>

<div style="text-align: center;">图14.10：具有2个卷积层的CNN示意图。输入包含3个颜色通道。内部层的特征图具有多个通道。圆柱体对应超列（hypercolumn），即某个位置的特征向量。改编自[Gér19]的图14.6。</div>

其中 s 是步长（为简单起见，假设高度和宽度的步长相同），b 是偏置项。如图14.9所示。

每个权重矩阵可以检测单一类型的特征。我们通常希望检测多种类型的特征，如图14.2所示。可以通过将 $\mathbf{W}$ 设为 $4d$ 维权重矩阵来实现这一点。检测输入通道 $c$ 中特征类型 $d$ 的滤波器存储在 $\mathbf{W}_{:,:,c,d}$ 中。我们将卷积的定义扩展为如下形式：

$$  z_{i,j,d}=b_{d}+\sum_{u=0}^{H-1}\sum_{v=0}^{W-1}\sum_{c=0}^{C-1}x_{si+u,sj+v,c}w_{u,v,c,d}   \tag*{(14.15)}$$

如图14.10所示。每个垂直圆柱列表示给定位置处的输出特征集 $z_{i,j,1:D}$；这有时被称为超列（hypercolumn）。每个元素是下一层中每个特征图的感受野内 C 个特征的不同加权组合。 $^{2}$

##### 14.2.1.7  $1 \times 1$ （逐点）卷积

有时我们只需要对给定位置处的特征进行加权组合，而不是跨位置进行组合。这可以通过 $1\times1$ 卷积（也称为逐点卷积）实现。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_128_970_407.jpg" alt="图像" width="67%" /></div>


<div style="text-align: center;">图 14.11：使用大小为 $ 1 \times 1 \times 3 \times 2 $ 的卷积滤波器将 3 个通道映射到 2 个通道。改编自 [Zha+20] 的图 6.4.2。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_342_502_825_710.jpg" alt="图像" width="41%" /></div>


<div style="text-align: center;">图 14.12：使用 2x2 滤波器和步长为 1 的 marpooling 示意图。改编自 $ [Zha+20] $ 的图 6.5.1。</div>


这将通道数从 C 变为 D，而不改变空间维度：

$$  z_{i,j,d}=b_{d}+\sum_{c=0}^{C-1}x_{i,j,c}w_{0,0,c,d}   \tag*{(14.16)}$$

这可以看作是一个单层 MLP 并行应用于每个特征列。

#### 14.2.2 池化层

卷积会保留输入特征位置的信息（忽略分辨率降低），这一性质称为**等变性**。在某些情况下，我们希望对于位置具有**不变性**。例如，在进行图像分类时，我们可能只想知道感兴趣的物体（如人脸）是否出现在图像中的任何位置。

实现这一点的一种简单方法称为**最大池化**，它只计算输入值的最大值，如图 14.12 所示。另一种方法是使用**平均池化**，它用平均值代替最大值。无论哪种情况，输出神经元都具有相同的响应，无论

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_158_119_1008_407.jpg" alt="图像" width="73%" /></div>


<div style="text-align: center;">图 14.13：用于图像分类的简单 CNN。改编自 https://blog.floydhub.com/building-your-first-convnet/。</div>


输入模式出现在其感受野内时被激活。（注意，我们对每个特征通道独立应用池化操作。）

如果对特征图中所有位置取平均，这种方法称为**全局平均池化**。这样，我们可以将 $ H \times W \times D $ 维的特征图转换为 $ 1 \times 1 \times D $ 维的特征图；该特征图可重塑为 D 维向量，然后送入全连接层映射为 C 维向量，最后传递给 softmax 输出层。使用全局平均池化意味着我们可以对任意尺寸的图像应用分类器，因为最终的特征图总是被转换为固定的 D 维向量，再映射到 C 个类别的分布上。

#### 14.2.3 整合各部分

一种常见的设计模式是：交替使用卷积层和最大池化层，最后在末端添加一个线性分类层，从而构建 CNN。如图 14.13 所示。（此例中省略了归一化层，因为模型较浅。）该设计模式最早出现在福岛的 neocognitron [Fuk75] 中，其灵感来源于 Hubel 和 Wiesel 对人类视觉皮层中简单细胞和复杂细胞的模型 [HW62]。1998 年，Yann LeCun 在其同名的 LeNet 模型 [LeC+98] 中采用了类似设计，并使用反向传播和 SGD 来估计参数。这种设计模式至今仍在神经启发的视觉物体识别模型 [RP99] 以及各种实际应用中（见第 14.3 节和第 14.5 节）广受欢迎。

#### 14.2.4 归一化层

图 14.13 中的基本设计对于浅层 CNN 效果良好，但如第 13.4.2 节所述，由于梯度消失或爆炸问题，将其扩展到更深层的模型可能较为困难。解决这一问题的一种常见方法是向模型添加额外的层，以标准化隐藏单元的统计量（即确保其均值为零、方差为单位方差），就像我们对许多模型的输入所做的那样。下面我们讨论各种类型的归一化层。

---

##### 14.2.4.1 批量归一化

最流行的归一化层是**批量归一化**（batch normalization, BN）[IS15]。它确保层内激活值的分布在 mini-batch 的样本上具有零均值和单位方差。更准确地说，我们将样本 $ n $（在某层中）的激活向量 $ z_n $（有时是预激活向量 $ a_n $）替换为 $ \tilde{z}_n $，其计算方式如下：

$$  \tilde{z}_{n}=\gamma\odot\hat{z}_{n}+\beta   \tag*{(14.17)}$$

$$  \hat{z}_{n}=\frac{z_{n}-\mu_{\mathcal{B}}}{\sqrt{\sigma_{\mathcal{B}}^{2}+\epsilon}}   \tag*{(14.18)}$$

$$  \mu_{B}=\frac{1}{\left|\mathcal{B}\right|}\sum_{z\in\mathcal{B}}z   \tag*{(14.19)}$$

$$  \sigma_{B}^{2}=\frac{1}{|\mathcal{B}|}\sum_{z\in\mathcal{B}}(z-\mu_{B})^{2}   \tag*{(14.20)}$$

其中 $ \mathcal{B} $ 是包含样本 $ n $ 的 mini-batch，$ \mu_B $ 是该 batch 的激活值均值¹，$ \sigma_B^2 $ 是相应的方差，$ \hat{z}_n $ 是标准化后的激活向量，$ \tilde{z}_n $ 是平移和缩放后的版本（BN 层的输出），$ \beta $ 和 $ \gamma $ 是该层可学习的参数，$ \epsilon > 0 $ 是一个很小的常数。由于该变换是可微的，我们可以轻松地将梯度反向传播到层的输入以及 BN 参数 $ \beta $ 和 $ \gamma $。

当应用于输入层时，批量归一化等价于我们在 10.2.8 节讨论的常见标准化过程。注意，由于数据是静态的，输入层的均值和方差可以一次性计算。然而，随着参数调整，内部层的经验均值和方差会不断变化（这有时被称为“内部协变量偏移”）。这就是为什么我们需要在每个 mini-batch 上重新计算 $ \mu $ 和 $ \sigma^2 $。

在测试时，我们可能只有单个输入，因此无法计算 batch 统计量。对此的标准解决方案如下：训练完成后，计算训练集所有样本（即使用完整 batch）在层 $ l $ 上的 $ \mu_l $ 和 $ \sigma_l^2 $，然后“冻结”这些参数，并将其添加到该层的其他参数（即 $ \beta_l $ 和 $ \gamma_l $）列表中。测试时，我们使用冻结的训练值 $ \mu_l $ 和 $ \sigma_l^2 $，而不是从测试 batch 中计算统计量。因此，在使用 BN 的模型时，我们需要指定是用于推理还是训练（参见 batchnorm_jax.ipynb 中的示例代码）。

为了提高速度，我们可以将冻结的 batch norm 层与前一层合并。具体来说，假设前一层计算 $ \mathbf{X}\mathbf{W} + b $；将其与 BN 结合得到 $ \gamma\odot(\mathbf{X}\mathbf{W} + b - \mu)/\sigma + \beta $。如果定义 $ \mathbf{W}' = \gamma\odot\mathbf{W}/\sigma $ 和 $ b' = \gamma\odot(b - \mu)/\sigma + \beta $，则可以将合并后的层写为 $ \mathbf{X}\mathbf{W}' + b' $。这称为**融合批量归一化**（fused batchnorm）。类似技巧也可用于在训练期间加速 BN [Jun+19]。

批量归一化在训练速度和稳定性方面的优势非常显著，尤其是对于深度 CNN。其确切原因尚不明确，但 BN 似乎使优化地形变得明显更加平滑 [San+18b]。它还能降低对学习率的敏感度 [ALL18]。除了计算优势外，它还具有统计优势。

---
¹ 原文脚注：“While previous chapters used θ for all learnable parameters, we reserve θ and β for the parameters of the BN layer.” 此处未提供脚注内容，故不翻译。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_239_117_924_300.jpg" alt="图像" width="59%" /></div>

<div style="text-align: center;">图 14.14：不同激活归一化方法在 CNN 上的示意图。每个子图展示了一个特征映射张量，其中 N 为批次轴，C 为通道轴，(H, W) 为空间轴。蓝色像素通过聚合这些像素的值计算出的均值和方差进行归一化。从左到右依次为：批量归一化、层归一化、实例归一化以及组归一化（每组 3 个通道，共 2 组）。摘自 [WH18] 的图 2。经何恺明许可使用。</div>

特别地，批量归一化（BN）起到正则化器的作用；实际上，它可以被证明等价于一种近似贝叶斯推断形式 [TAS18; Luo+19]。

然而，对数据小批量的依赖会导致若干问题。尤其是在使用小批量大小进行训练时，会导致参数估计不稳定，尽管该方法的一个较新版本——批量重归一化 [Iof17] 部分解决了这一问题。下面我们讨论批量归一化的一些其他替代方案。

##### 14.2.4.2 其他类型的归一化层

在第 14.2.4.1 节中，我们讨论了批量归一化（batch normalization），它将给定特征通道内的所有激活标准化为零均值和单位方差。这能显著帮助训练，并允许使用更大的学习率（示例代码见 batchnorm_jax.ipynb）。

尽管批量归一化效果良好，但在批量大小较小时会难以应对，因为估算的均值和方差参数可能不可靠。一种解决方案是通过汇聚张量其他维度上的统计量（而非汇聚批次中的样本）来计算均值和方差。更准确地说，令 $z_i$ 表示张量的第 $i$ 个元素；对于二维图像，索引 $i$ 有四个分量，分别表示批次、高度、宽度和通道，即 $i = (i_N, i_H, i_W, i_C)$。我们按如下方式计算每个索引 $z_i$ 的均值和标准差：

$$ \mu_{i}=\frac{1}{\left|\mathcal{S}_{i}\right|}\sum_{k\in\mathcal{S}_{i}}z_{k},\quad \sigma_{i}=\sqrt{\frac{1}{\left|\mathcal{S}_{i}\right|}\sum_{k\in\mathcal{S}_{i}}(z_{k}-\mu_{i})^{2}+\epsilon} \tag*{(14.21)} $$

其中 $\mathcal{S}_i$ 是我们进行平均的元素集合。然后计算 $\hat{z}_i = (z_i - \mu_i)/\sigma_i$ 和 $\tilde{z}_i = \gamma_c\hat{z}_i + \beta_c$，这里的 $c$ 为索引 $i$ 对应的通道。

在批量归一化中，我们对批次、高度、宽度进行汇聚，因此 $\mathcal{S}_i$ 是张量中所有与 $i$ 的通道索引相匹配的位置。为了避免小批量带来的问题，我们可以改为对通道、高度、宽度进行汇聚，但匹配批次索引，这就是**层归一化**（layer normalization）[BKH16]（示例代码见 layer_norm_jax.ipynb）。另一种方案是为批次中的每个样本和每个通道分别设置独立的归一化参数，这就是**实例归一化**（instance normalization）[UVL16]。

---

上述方法的一个自然泛化是**组归一化**（group normalization）$[WH18]$，其将通道与索引 $i$ 处于同一组的所有位置进行池化。如图 14.14 所示。层归一化是其特例，此时所有通道属于单个组；实例归一化也是其特例，此时每个通道独立成一组（共 $C$ 组）。在 $[WH18]$ 中，他们通过实验表明，使用大于单通道但小于全通道的组，在训练速度、训练精度和测试精度方面可能更优。

更近期，[SK20] 提出了**滤波器响应归一化**（filter response normalization, FRN），这是一种批归一化的替代方案，即使在小批量大小为 1 时也能良好工作。其思想是将每个组定义为单个通道和批样本的所有位置（类似于实例归一化），但仅除以均方范数而非进行标准化。即，若输入（对于给定通道和批条目）为 $z = \mathbf{Z}_{b,\ldots,c} \in \mathbb{R}^N$，我们计算 $\hat{z} = z / \sqrt{\nu^2 + \epsilon}$，其中 $\nu^2 = \sum_{ij} z_{b_{ijc}}^2 / N$，然后 $\hat{z} = \gamma_c \hat{z} + \beta_c$。由于未进行均值中心化，激活值可能偏离 0，这在 ReLU 激活函数下尤其有害。为弥补这一点，作者提出在输出端添加一个**阈值线性单元**（thresholded linear unit, TLU），其形式为 $y = \max(\boldsymbol{x}, \tau)$，其中 $\tau$ 是可学习的偏移量。FRN 与 TLU 的结合使得在批量大小为 1 时仍能在图像分类和目标检测上取得良好性能。

##### 14.2.4.3 无归一化网络

近期，[Bro+21] 提出了一种称为**无归一化网络**（normalizer-free networks）的方法，可以在不使用批归一化或任何其他归一化层的情况下训练深度残差网络。其关键在于用**自适应梯度裁剪**（adaptive gradient clipping）替代归一化层，作为避免训练不稳定的另一种方式。即我们使用 Equation (13.70)，但动态调整裁剪强度。由此得到的模型训练速度更快，精度也优于使用批归一化训练的其他竞争模型。

### 14.3 图像分类的常用架构

使用 CNN 进行图像分类是常见做法，该任务估计函数 $f : \mathbb{R}^{H \times W \times K} \to \{0,1\}^C$，其中 $K$ 是输入通道数（例如 RGB 图像 $K=3$），$C$ 是类别标签数。

本节简要回顾多年来为解决图像分类任务而开发的各类 CNN。如需更全面的 CNN 综述，可参见 [Kha+20]；最新的代码和模型库（PyTorch 实现）可访问 https://github.com/rwightman/pytorch-image-models。

#### 14.3.1 LeNet

最早的 CNN 之一——LeNet [LeC+98] 诞生于 1998 年，以其创建者 Yann LeCun 命名。该网络专为手写数字图像分类而设计，并在第 3.5.2 节介绍的 MNIST 数据集上训练。模型结构如图 14.15 所示（模型更紧凑的表示见图 14.16a）。该模型的部分预测结果如图 14.17 所示。仅经过 1 个 epoch，测试准确率即达到 98.8%。相比之下，第 13.2.4.2 节中的 MLP 在 1 个 epoch 后的准确率为 95.9%。更多轮次的训练可进一步提高准确率，直至性能与标签噪声不可区分。（示例代码见 lenet_jax.ipynb。）

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_246_1033_466.jpg" alt="Image" width="76%" /></div>


<div style="text-align: center;">图14.15：LeNet5，一种用于手写数字分类的卷积神经网络。摘自 [Zha+20] 的图6.6.1。经Aston Zhang许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_308_716_873_1033.jpg" alt="Image" width="49%" /></div>


<div style="text-align: center;">图14.16：(a) LeNet5。假设输入尺寸为 $1 \times 28 \times 28$，这与MNIST数据集的情况一致。摘自 [Zha+20] 的图6.6.2。经Aston Zhang许可使用。(b) AlexNet。假设输入尺寸为 $3 \times 224 \times 224$，这与ImageNet数据集（经过裁剪和缩放）的图像情况一致。摘自 [Zha+20] 的图7.1.2。经Aston Zhang许可使用。</div>

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_246_119_925_344.jpg" alt="图像" width="58%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 14.17：对部分 MNIST 图像应用 CNN 的结果（精选了包含一些错误的情况）。红色为错误，蓝色为正确。(a) 训练 1 个 epoch 后。(b) 训练 2 个 epoch 后。由 cnn_mnist_tf.ipynb 生成。</div>


当然，对孤立数字进行分类的适用性有限：在现实世界中，人们通常书写数字串或其他字母。这同时需要分割和分类。LeCun 及其同事设计了一种方法，将卷积神经网络与类似条件随机场的模型相结合来解决该问题。该系统被美国邮政署采用。详见 [LeC+98] 对该系统的更详细描述。

#### 14.3.2 AlexNet

尽管 CNN 已存在多年，但直到 2012 年 [KSH12] 的论文才引起主流计算机视觉研究者的关注。在那篇论文中，作者展示了如何将 ImageNet 挑战赛（1.5.1.2 节）的前 5 错误率从之前最佳的 26% 降至 15%，这是一个巨大的改进。该模型被称为 AlexNet 模型，以其创建者 Alex Krizhevsky 命名。

图 14.16b(b) 展示了其架构。它与图 14.16a 所示的 LeNet 非常相似，区别如下：更深（8 层可调参数层，即剔除池化层，而非 5 层）；使用 ReLU 非线性函数而非 tanh（见 13.2.3 节解释其重要性）；使用 dropout（13.5.4 节）进行正则化而非权重衰减；以及堆叠多个卷积层，而非严格交替使用卷积和池化。堆叠多个卷积层的优势在于感受野会变大，因为一层的输出会输入到另一层（例如，连续三个 $3 \times 3$ 滤波器的感受野大小为 $7 \times 7$）。这优于使用单个具有更大感受野的层，因为多个层之间还具有非线性变换。此外，三个 $3 \times 3$ 滤波器的参数量少于一个 $7 \times 7$ 滤波器。

注意，AlexNet 拥有 6000 万个自由参数（远多于 100 万个标注样本），这主要归因于输出端的三个全连接层。训练该模型依赖于使用两个 GPU（受限于当时 GPU 的内存限制），并被广泛认为是一项工程壮举。 ^{4} 图 1.14a 展示了该模型对 ImageNet 部分图像的一些预测结果。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_117_950_334.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 14.18: Inception 模块。$ 1 \times 1 $ 卷积层减少通道数，同时保持空间维度不变。通过不同尺寸的卷积构成的并行路径，模型可以学习每个层级应使用哪种过滤器尺寸。最终的深度拼接块将所有不同路径（均具有相同空间尺寸）的输出合并。源自 [Zha+20] 的图 7.4.1。经 Aston Zhang 许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_174_514_994_721.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 14.19: GoogLeNet（较原始版本略有简化）。输入位于左侧。源自 [Zha+20] 的图 7.4.2。经 Aston Zhang 许可使用。</div>


#### 14.3.3 GoogLeNet（Inception）

谷歌开发了一个名为 GoogLeNet 的模型 [Sze+15a]（该名称是 Google 和 LeNet 的双关语）。与早期模型的主要区别在于，GoogLeNet 使用了一种新型模块——**Inception 模块** $^{5}$——该模块采用多条并行路径，每条路径包含不同尺寸的卷积过滤器。如图 14.18 所示。这让模型能够学习每个层次的最佳过滤器尺寸。整体模型由 9 个 Inception 模块后接全局平均池化构成。如图 14.19 所示。自该模型首次提出以来，已有多种扩展方案；详情可参见 [IS15; Sze+15b; SIV17]。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_377_129_826_471.jpg" alt="图片" width="38%" /></div>

<div style="text-align: center;">图 14.20：CNN 的残差块。左图：标准版本。右图：使用 1×1 卷积的版本，以允许块输入与输出之间的通道数变化。摘自 [Zha+20] 的图 7.6.3。经 Aston Zhang 许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_295_586_877_750.jpg" alt="图片" width="50%" /></div>

<div style="text-align: center;">图 14.21：ResNet-18 架构。每个虚线模块是图 14.20 中所示的残差块。摘自 [Zha+20] 的图 7.6.4。经 Aston Zhang 许可使用。</div>

#### 14.3.4 ResNet

2015 年 ImageNet 分类挑战赛的获胜者是微软的一个团队，他们提出了名为 ResNet 的模型 [He+16a]。其核心思想是将  $\boldsymbol{x}_{l+1} = \mathcal{F}_l(\boldsymbol{x}_l)$  替换为

$$  \boldsymbol{x}_{l+1}=\varphi(\boldsymbol{x}_{l}+\mathcal{F}_{l}(\boldsymbol{x}_{l}))   \tag*{(14.22)}$$

这被称为**残差块**，因为  $F_l$  只需学习该层输入与输出之间的残差（即差值），这是一个更简单的任务。在  $[He+16a]$  中，$\mathcal{F}$  的形式为 conv-BN-relu-conv-BN，其中 conv 是卷积层，BN 是批归一化层（第 14.2.4.1 节）。示意图见图 14.20（左）。

---

我们可以通过使用填充来确保卷积层输出 $\mathcal{F}_l(\boldsymbol{x}_l)$ 的空间维度与输入 $\boldsymbol{x}_l$ 相匹配。然而，如果我们希望卷积层的输出通道数不同，则需要在 $\boldsymbol{x}_l$ 的跳跃连接上添加 $1 \times 1$ 卷积。见图14.20(右)的图示。

残差块的使用使我们能够训练非常深的模型。之所以能够如此，是因为通过跳跃连接，梯度可以直接从输出流向较早的层，原因在第13.4.4节中解释。

在[He+16a]中，他们训练了一个152层的ResNet在ImageNet上。然而，使用更浅的模型更为常见。例如，图14.21展示了ResNet-18结构，它有18个可训练层：每个残差块中有两个3x3卷积层，共有8个这样的块，还有一个初始的7x7卷积（步长2）和一个最终的全连接层。

符号化地，我们可以如下定义该模型：

$$ \left(\mathrm{Conv}\quad:\mathrm{BN}\quad:\mathrm{Max}\right)\quad:\left(\mathrm{R}\quad:\mathrm{R}\right)\quad:\left(\mathrm{R}^{\prime}\quad:\mathrm{R}\right)\quad:\left(\mathrm{R}^{\prime}\quad:\mathrm{R}\right)\quad:\left(\mathrm{R}^{\prime}\quad:\mathrm{R}\right)\quad:\mathrm{Avg}\quad:\mathrm{FC} $$

其中R是一个残差块，R'是一个带有跳跃连接（由于通道数变化）且步长为2的残差块，FC是全连接层（密集层），: 表示拼接。

注意，输入的空间尺寸在每经过一个R'块时会降低2倍（再加上初始的Conv-7x7(2)和最大池化），总共降低 $2^5 = 32$ 倍，因此一张224x224的图像在进入全局平均池化层之前会变成7x7的图像。

拟合这些模型的代码可以在网上找到。$^{6}$

在[He+16b]中，他们展示了如何对该方案进行微小修改，从而训练多达1001层的模型。关键洞察在于，由于在相加步骤之后使用了非线性激活函数 $\boldsymbol{x}_{l+1} = \varphi(\boldsymbol{x}_l + \mathcal{F}(\boldsymbol{x}_l))$，跳跃连接上的信号仍然受到衰减。他们指出，更好的选择是使用：

$$  \boldsymbol{x}_{l+1}=\boldsymbol{x}_{l}+\varphi(\mathcal{F}_{l}(\boldsymbol{x}_{l}))   \tag*{(14.23)}$$

这称为预激活残差网络，简称PreResnet。现在网络很容易在给定层学习恒等函数：如果我们使用ReLU激活函数，只需确保 $\mathcal{F}_l(\boldsymbol{x}_l) = \mathbf{0}$，这可以通过将权重和偏置设为0来实现。

使用非常深的模型的另一种选择是使用非常“宽”的模型，即每层有大量特征通道。这是宽残差网络[ZK16]背后的思想，该模型非常流行。

#### 14.3.5 DenseNet（密集连接网络）

在残差网络中，我们将每个函数的输出与其输入相加。另一种方法是将输出与输入拼接起来，如图14.22a所示。如果我们将一系列这样的块堆叠起来，可以得到一个类似于图14.22b的结构。这被称为密集连接网络[DenseNets，Hua+17a]，因为每一层都密集地依赖于之前的所有层。因此，整体模型计算的是如下的函数：

$$  \boldsymbol{x}\rightarrow\left[\boldsymbol{x},f_{1}(\boldsymbol{x}),f_{2}(\boldsymbol{x},f_{1}(\boldsymbol{x})),f_{3}(\boldsymbol{x},f_{1}(\boldsymbol{x}),f_{2}(\boldsymbol{x},f_{1}(\boldsymbol{x}))),\cdots\right]   \tag*{(14.24)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_118_1015_327.jpg" alt="图像" width="69%" /></div>


<div style="text-align: center;">图 14.22: (a) 左侧：残差块将输出与输入相加。右侧：密集块将输出与输入拼接。(b) 密集连接网络示意图。来自 [Zha+20] 的图 7.7.1–7.7.2。经 Aston Zhang 许可使用。</div>


密集连接增加了参数量，因为通道会沿深度方向堆叠。我们可以通过在其中插入 $1 \times 1$ 卷积层来补偿这一点。也可以添加步长为 2 的池化层以降低空间分辨率。（示例代码见 densenet_jax.ipynb。）

由于所有先前计算的特征都能直接用于输出层，DenseNet 的性能可能优于 ResNet。然而，其计算开销也可能更大。

#### 14.3.6 神经架构搜索

我们已经看到，许多 CNN 的设计相当相似，仅仅是按不同拓扑结构重新排列各种构建模块（如卷积层或池化层），并调整各种参数设置（如步长、通道数或学习率）。事实上，最近的 ConvNeXt 模型 [Liu+22]（在撰写本文时，即 2022 年 4 月，被认为是各种视觉任务中最先进的 CNN 架构）就是通过在标准 ResNet 架构基础上组合多个此类小幅改进而创建的。

我们可以使用黑箱（无导数）优化方法来自动化这一设计过程，寻找能最小化验证损失的架构。这被称为自动机器学习 (AutoML)（例如，参见 [HKV19]）。在神经网络领域，它被称为神经架构搜索 (NAS) [EMH19]。

执行 NAS 时，我们可以同时优化多个目标，例如准确率、模型大小、训练或推理速度等（EfficientNetv2 就是通过这种方式创建的 [TL21]）。主要挑战在于计算目标函数的代价高昂（因为需要对模型空间中的每个候选点进行训练）。减少目标函数调用次数的一种方法是使用贝叶斯优化（例如，参见 [WNS19]）。另一种方法是构建损失的可微近似（例如，参见 [LSY19; Wan+21]），或者将架构转换为核函数（使用神经正切核方法，第 17.2.8 节），然后分析其特征值的性质，无需实际训练模型就能预测性能 [CGW21]。NAS 领域非常庞大且仍在发展。更全面的综述可参见 [EMH19]。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_288_122_880_336.jpg" alt="Image" width="51%" /></div>


<div style="text-align: center;">图 14.23：采用扩张率 1、2 和 3 的 3x3 滤波器进行空洞卷积。来自 [Cui+19] 的图 1，经崔希民许可使用。</div>


### 14.4 其他形式的卷积  $ * $

我们在 14.2 节讨论了卷积的基础知识。本节将讨论一些扩展形式，这些形式在图像分割和图像生成等应用中不可或缺。

#### 14.4.1 空洞卷积

卷积是一种将局部邻域内的像素值组合起来的操作。通过使用步长并将多个卷积层堆叠在一起，我们可以扩大每个神经元的感受野，即每个神经元响应的输入空间区域。然而，若要使每个神经元获得足够的上下文信息以覆盖整幅图像，我们需要很多层（除非使用非常大的滤波器，但这会导致速度缓慢且参数过多）。

作为替代方案，我们可以使用带孔的卷积 [Mal99]（有时用法语术语"à trous"表示，近期被重新命名为**空洞卷积** [YK16]）。该方法在执行卷积时，仅每隔 $r$ 个输入元素取一个，其中 $r$ 称为**扩张率**（dilation factor）。例如，在一维情况下，使用扩张率 $r = 2$ 的滤波器 $\pmb{w}$ 进行卷积，等价于使用滤波器 $\tilde{\pmb{w}} = [w_1, 0, w_2, 0, w_3]$ 进行常规卷积，其中我们插入了 0 以扩大感受野（因此得名"带孔的卷积"）。这使我们能够在不增加参数数量或计算量的情况下，获得更大的感受野。图 14.23 对此进行了说明。

更精确地，二维空洞卷积的定义如下：

$$  z_{i,j,d}=b_{d}+\sum_{u=0}^{H-1}\sum_{v=0}^{W-1}\sum_{c=0}^{C-1}x_{i+r u,j+r v,c}w_{u,v,c,d}   \tag*{(14.25)}$$

为简单起见，这里假设高度和宽度方向使用相同的扩张率 $r$。将此式与方程 (14.15) 比较，后者在步长参数中使用的是 $x_{si+u,sj+v,c}$。

#### 14.4.2 转置卷积

在卷积中，我们通过对输入像素与卷积核 K 进行加权组合，将较大的输入 X 缩减为较小的输出 Y。这在代码中最容易解释：

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_153_125_1024_287.jpg" alt="图像" width="75%" /></div>


<div style="text-align: center;">图 14.24：使用 2x2 核的转置卷积。源自文献 [Zha+20] 的图 13.10.1。经 Aston Zhang 许可使用。</div>


def conv(X, K):
    h, w = K.shape
    Y = zeros((X.shape[0] - h + 1, X.shape[1] - w + 1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            Y[i, j] = (X[i:i + h, j:j + w] * K).sum()
    return Y

在转置卷积中，我们做相反的操作，以从较小的输入产生较大的输出：

def trans_conv(X, K):
    h, w = K.shape
    Y = zeros((X.shape[0] + h - 1, X.shape[1] + w - 1))
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Y[i:i + h, j:j + w] += X[i, j] * K
    return Y

这相当于在输入图像的右下角填充 $(h-1, w-1)$ 个零（其中 $(h, w)$ 是卷积核尺寸），然后在每个输入位置放置一个加权后的核副本（权值为对应像素值），最后求和。该过程如图 14.24 所示。我们可以将卷积核视为一个“模板”，用于生成输出，并由输入中的权值进行调制。

术语“转置卷积”源于卷积的矩阵乘法解释，我们在第 14.2.1.3 节讨论过。如果 $\mathbf{W}$ 是由核 $\mathbf{K}$ 通过方程 (14.9) 所示过程导出的矩阵，那么可以证明 $\mathbf{Y} = \text{transposed-conv}(\mathbf{X}, \mathbf{K})$ 等价于 $\mathbf{Y} = \text{reshape}(\mathbf{W}^{\mathsf{T}} \text{vec}(\mathbf{X}))$。参见 \textit{transposed\_conv\_jax.ipynb} 的演示。

注意，转置卷积有时也被称为反卷积（deconvolution），但这是不正确的用法：反卷积是指利用已知的滤波器（如模糊滤波器）“撤销”卷积效果以恢复原始输入的过程，如图 14.25 所示。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_217_120_948_221.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 14.25: 卷积、反卷积与转置卷积。这里 s 为步长，p 为填充。摘自 https://tinyurl.com/ynxcxsut。经 Aqeel Anwar 许可使用。</div>


#### 14.4.3 深度可分离卷积

标准卷积使用大小为 $ H \times W \times C \times D $ 的滤波器，这需要大量数据进行学习，并且计算耗时。一种简化方法称为 **深度可分离卷积**，首先用对应的二维滤波器 $ \pmb{w} $ 对每个输入通道进行卷积，然后使用 $ 1 \times 1 $ 卷积 $ \pmb{w}' $ 将这 $ C $ 个通道映射到 $ D $ 个通道：

$$  z_{i,j,d}=b_{d}+\sum_{c=0}^{C-1}w_{c,d}^{\prime}\left(\sum_{u=0}^{H-1}\sum_{v=0}^{W-1}x_{i+u,j+v,c}w_{u,v}\right)   \tag*{(14.26)}$$

其示意图见图 14.26。

为了说明其优势，我们考虑一个简单的数值示例。$ ^{7} $ 对一个 $ 12 \times 12 \times 3 $ 输入使用 $ 5 \times 5 \times 3 \times 256 $ 滤波器进行常规卷积，得到 $ 8 \times 8 \times 256 $ 输出（假设有效卷积：$ 12-5+1=8 $），如图 14.13 所示。而使用可分离卷积时，我们从 $ 12 \times 12 \times 3 $ 输入开始，用 $ 5 \times 5 \times 1 \times 1 $ 滤波器（仅空间维度，不跨通道）卷积得到 $ 8 \times 8 \times 3 $，然后用 $ 1 \times 1 \times 3 \times 256 $ 滤波器逐点卷积（仅跨通道，不跨空间）得到 $ 8 \times 8 \times 256 $ 输出。因此输出尺寸与之前相同，但定义这一层所用的参数数量大大减少，计算量也大幅降低。出于这个原因，可分离卷积常被用于轻量级 CNN 模型，例如 MobileNet 模型 [How+17; San+18a] 及其他边缘设备。

### 14.5 用 CNN 解决其他判别式视觉任务 *

本节简要讨论如何使用 CNN 处理其他各种视觉任务。每个任务也为我们已见过的基本构建块库引入了新的架构创新。关于计算机视觉中 CNN 的更多细节，可参见例如 [Bro19]。

#### 14.5.1 图像标记

图像分类为整张图像分配一个单一标签，即假设输出是互斥的。但在许多问题中，可能存在多个物体，我们希望标记出所有物体。这称为 **图像标记**，是多标签预测的一个应用。此时，我们将输出空间定义为 $ \mathcal{Y} = \{0, 1\}^C $，其中 $ C $ 是标签类型的数量。由于输出位是独立的（给定图像），我们应将最后的 softmax 替换为一组 $ C $ 个 logistic 单元。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_365_118_798_401.jpg" alt="图像" width="37%" /></div>

<div style="text-align: center;">图14.26：深度可分离卷积：每个C个输入通道都经过一次二维卷积生成C个输出通道，这些通道再通过逐点卷积（1×1卷积）组合成D个输出通道。图片来源：https://bit.ly/2L9fm2o。经Eugenio Culurciello许可使用。</div>

像Instagram这类社交媒体网站的用户常常为他们的图像创建标签；因此，这提供了一种“免费”创建大型监督数据集的方式。当然，许多标签可能使用得非常稀疏，且其含义在视觉上可能并不明确。（例如，某人可能在接受COVID检测后给自己拍照，并将图像标记为“#covid”；然而，从视觉上看，它看起来就像任何其他人的图像一样。）因此，这种用户生成的标注通常被认为噪声很大。不过，它对于“预训练”可能很有用，正如[Mah+18]中所讨论的那样。

最后，值得注意的是，图像标注通常比图像分类更合理，因为许多图像中包含多个物体，并且很难确定我们应该标注哪一个。事实上，在ImageNet上创建“人类性能基准”的Andrej Karpathy曾指出：$ ^{8} $

[CNNs]和人类都难以处理包含多个ImageNet类别（通常超过五个）的图像，并且很难指出哪个物体是图像的焦点。这种错误只存在于分类设定中，因为每张图像都被限制为只有一个正确的标签。总体而言，我们将16%的人类错误归因于这一类别。

#### 14.5.2 目标检测

在某些情况下，我们需要生成可变数量的输出，对应于图像中可能存在的可变数量的感兴趣物体。（这是一个开放世界问题的例子，物体数量未知。）

一个典型的例子是**目标检测**，其任务是返回一组表示感兴趣物体位置的边界框，同时附带它们的类别标签。一个特例是**人脸检测**，其中只涉及一个感兴趣类别。如图14.27a所示。$ ^{9} $

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_241_119_524_332.jpg" alt="图像" width="24%" /></div>

<div style="text-align: center;">$ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_652_120_926_333.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 14.27: (a) 人脸检测示意图，这是目标检测的一个特例。（作者与妻子 Margaret 的照片，2018年2月摄于加利福尼亚州 Filoli。Jonathan Huang 使用 SSD 人脸模型处理图像。）(b) 锚框示意图。改编自 [Zha+20, Sec 12.5]。</div>

解决此类检测问题最直接的方法是将其转化为封闭世界问题，即每个物体可能的空间位置（及朝向）是有限的。这些候选位置被称为**锚框**。如图 14.27b 所示，我们可以在多个位置、尺度和长宽比下生成锚框。针对每个锚框，训练系统预测其中包含的物体类别（若有）；同时通过回归预测物体位置相对于锚框中心的偏移量（这些残差回归项实现了亚网格级别的空间定位）。

抽象地讲，我们学习的函数形式为

$$  f_{\theta}:\mathbb{R}^{H\times W\times K}\to[0,1]^{A\times A}\times\{1,\ldots,C\}^{A\times A}\times(\mathbb{R}^{4})^{A\times A}   \tag*{(14.27)}$$

其中 $K$ 是输入通道数，$A$ 是每个维度上的锚框数量，$C$ 是物体类型（类别标签）的数量。对于每个锚框位置 $(i,j)$，我们预测三个输出：物体存在概率 $p_{ij} \in [0,1]$、物体类别 $y_{ij} \in \{1,\ldots,C\}$，以及两个二维偏移向量 $\delta_{ij} \in \mathbb{R}^4$，将其加到锚框质心上可得到左上角和右下角的坐标。

目前已提出多种此类模型，包括 [Liu+16] 的单次检测器（Single Shot Detector, SSD）模型和 [Red+16] 的 YOLO（You Only Look Once）模型。多年来还涌现了许多其他目标检测方法，这些模型在速度、精度、简洁性等方面各有取舍。其实验比较可参见 [Hua+17b]，更近期的综述见 [Zha+18]。

#### 14.5.3 实例分割

在目标检测中，我们为每个物体预测标签和边界框。而在**实例分割**中，目标是预测图像中每个物体实例的标签和二维形状掩膜，如图 14.28 所示。这可以通过对每个检测到的框应用语义分割模型来实现。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_392_119_779_407.jpg" alt="Image" width="33%" /></div>

<div style="text-align: center;">图 14.28：使用 Mask R-CNN 进行目标检测和实例分割的示意图。来源：https://github.com/matterport/Mask_RCNN。经 Waleed Abdulla 友好许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_210_497_961_710.jpg" alt="Image" width="65%" /></div>

<div style="text-align: center;">图 14.29：用于语义分割的编码器-解码器（即 U-net）CNN 示意图。编码器使用卷积（进行下采样），解码器使用转置卷积（进行上采样）。来源：图 1 来自 [BKC17]。经 Alex Kendall 友好许可使用。</div>

这需要将每个像素标记为前景或背景。（关于语义分割的更多细节，请参见第 14.5.4 节。）

#### 14.5.4 语义分割

在语义分割中，我们需要为每个像素预测一个类别标签 $y_i \in \{1, \ldots, C\}$，这些类别可以代表天空、道路、汽车等。与我们在第 14.5.3 节讨论的实例分割不同，所有汽车像素获得相同的标签，因此语义分割不区分不同物体。我们可以将“物质”（如天空、道路）的语义分割与“物体”（如汽车、人）的实例分割结合成一个统一的框架，称为“全景分割”[Kir+19]。

处理语义分割的一种常见方法是使用编码器-解码器架构，如图 14.29 所示。编码器使用标准卷积将输入映射到一个较小的二维瓶颈层，该瓶颈层以粗糙的空间分辨率捕获输入的高层次属性。（这通常使用一种称为空洞卷积的技术，我们将在第 14.4.1 节中解释，以捕获一个

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_367_117_801_406.jpg" alt="图像" width="37%" /></div>


<div style="text-align: center;">图 14.30：用于语义分割的 U-Net 模型示意图。每个蓝色框对应一个多通道特征图。框上方显示通道数，左下角显示高/宽。白色框表示复制后的特征图。不同颜色的箭头对应不同的操作。来自 [RFB15] 的图 1，经 Olaf Ronenberg 许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_175_550_1001_718.jpg" alt="图像" width="71%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_818_552_1003_714.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;">图 14.31：多任务密集预测问题示意图。来自 [EF15] 的图 1，经 Rob Fergus 许可使用。</div>


较大的视野范围（即更多的上下文信息）。解码器使用一种称为转置卷积的技术（我们在第 14.4.2 节中解释）将较小的二维瓶颈映射回全尺寸的输出图像。由于瓶颈会丢失信息，我们还可以从输入层向输出层添加跳跃连接。我们可以将此模型重绘为图 14.30 所示。由于其整体结构类似于字母 U，因此也被称为 U-Net [RFB15]。

类似的编码器-解码器架构也可用于其他密集预测或图像到图像的任务，例如深度预测（预测每个像素 $ i $ 到相机的距离 $ z_i \in \mathbb{R} $）、表面法线预测（预测每个图像块处表面的方向 $ z_i \in \mathbb{R}^3 $）等。当然，我们可以使用多个输出头训练一个模型来同时解决所有这些任务，如图 14.31 所示。（详细信息可参见例如 [Kok17]。）

#### 14.5.5 人体姿态估计

我们可以训练一个目标检测器来检测人，并预测其二维形状（以掩码表示）。然而，我们也可以训练模型来预测一组固定的骨骼关键点的位置。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_440_118_731_336.jpg" alt="图像" width="25%" /></div>

<div style="text-align: center;">图14.32：使用OpenPose系统进行身体、手部和脸部关键点检测的示意图。来自$[Cao+18]$的图8。经Yaser Sheikh友好许可使用。</div>

例如，头部或手部的位置。这被称为人体姿态估计。参见图14.32的示例。有多种技术可用于此，例如PersonLab [Pap+18]和OpenPose [Cao+18]。最近的综述见[Bab19]。

我们还可以预测每个检测到的物体的3D属性。主要限制在于收集足够标记训练数据的能力，因为人类标注者很难在3D空间中标注。然而，我们可以使用$\underline{\text{计算机图形学}}$引擎来创建具有无限真实3D标注的模拟图像（例如，见$[GNK18]$）。

### 14.6 通过逆向CNN生成图像  $ ^{*} $

一个用于图像分类的$\text{UNN}$是一种判别式模型，形式为$p(y|\pmb{x})$，它接收图像作为输入，并返回C个类别标签上的概率分布作为输出。在本节中，我们讨论如何通过将其转换为形如$p(\pmb{x}|y)$的（条件）生成式图像模型来“逆向”该模型。这将使我们能够生成属于特定类别的图像。（我们在本书的后续内容[Mur23]中讨论了创建图像生成模型的更系统的方法。）

#### 14.6.1 将训练好的分类器转换为生成模型

我们可以使用$p(\boldsymbol{x}, y) = p(\boldsymbol{x}) p(y|\boldsymbol{x})$定义图像和标签的联合分布，其中$p(y|\boldsymbol{x})$是CNN分类器，$p(\boldsymbol{x})$是图像上的某个先验。如果我们将类别标签固定为一个特定值，我们就可以利用$p(\boldsymbol{x}|y) \propto p(\boldsymbol{x}) p(y|\boldsymbol{x})$创建条件生成模型。注意，判别式分类器$p(y|\boldsymbol{x})$的训练目的是“丢弃”信息，因此$p(y|\boldsymbol{x})$不是可逆函数。因此，先验项$p(\boldsymbol{x})$将在此过程中起到重要的正则化作用，正如我们在14.6.2节中看到的那样。

从该模型中采样的一种方法是使用Metropolis–Hastings算法（第4.6.8.4节），将$\mathcal{E}_c(\boldsymbol{x}) = \log p(y = c|\boldsymbol{x}) + \log p(\boldsymbol{x})$视为能量函数。由于梯度信息可用，我们可以使用形如$q(\boldsymbol{x}'|\boldsymbol{x}) = \mathcal{N}(\boldsymbol{\mu}(\boldsymbol{x}), \boldsymbol{\epsilon})$的提议分布，其中$\boldsymbol{\mu}(\boldsymbol{x}) = \boldsymbol{x} + \frac{\epsilon}{2} \nabla \log \mathcal{E}_c(\boldsymbol{x})$。这被称为Metropolis调整的Langevin算法（MALA）。作为近似，我们可以忽略拒绝步骤，接受每一个提议。这被称为未调整的Langevin算法，并在[Ngu+17]中用于条件图像生成。此外，我们可以缩放

---

对数先验和对数似然的梯度独立计算。因此，我们在图像空间上得到一种类似随机梯度下降（SGD）带噪声版本的更新，区别在于我们对输入像素求导（利用公式（13.50）），而非对参数求导：

$$  \boldsymbol{x}_{t+1}=\boldsymbol{x}_{t}+\epsilon_{1}\frac{\partial\log p(\boldsymbol{x}_{t})}{\partial\boldsymbol{x}_{t}}+\epsilon_{2}\frac{\partial\log p(y=c|\boldsymbol{x}_{t})}{\partial\boldsymbol{x}_{t}}+\mathcal{N}(\mathbf{0},\epsilon_{3}^{2}\mathbf{I})   \tag*{(14.28)}$$

我们可以解释此方程中的每一项：\( \epsilon_1 \) 项确保图像在先验下是合理的，\( \epsilon_2 \) 项确保图像在似然下是合理的，而 \( \epsilon_3 \) 项是噪声项，用于生成多样化的样本。如果设 \( \epsilon_3 = 0 \)，该方法就变成了一种确定性算法，用于（近似）生成该类别的“最可能图像”。

#### 14.6.2 图像先验

在本节中，我们讨论可用于正则化解分类器这一不适定问题的各类图像先验。这些先验与优化起始图像一起，将决定我们生成的输出类型。

##### 14.6.2.1 高斯先验

仅指定类别标签不足以明确我们想要生成的图像类型。我们还需要一个先验 \( p(\boldsymbol{x}) \) 来定义什么是“合理”的图像。如下所示，先验对生成图像的质量有显著影响。

最简单的先验可能是 \( p(\boldsymbol{x}) = \mathcal{N}(\boldsymbol{x}|\mathbf{0}, \mathbf{I}) \)，如文献 [SVZ14] 所提议。（这假设图像像素已中心化。）该先验可防止像素取极端值。在这种情况下，先验项对应的更新形式为

$$  \nabla_{\mathbf{x}}\log p(\mathbf{x}_{t})=\nabla_{\mathbf{x}}\left[-\frac{1}{2}||\mathbf{x}_{t}-\mathbf{0}||_{2}^{2}\right]=-\mathbf{x}_{t}   \tag*{(14.29)}$$

因此，整体更新（假设 \( \epsilon_{2}=1 \) 且 \( \epsilon_{3}=0 \)）形式为

 $$ \boldsymbol{x}_{t+1}=(1-\epsilon_{1})\boldsymbol{x}_{t}+\frac{\partial\log p(y=c|\boldsymbol{x}_{t})}{\partial\boldsymbol{x}_{t}} $$ 

图14.33展示了通过该方法生成的若干样本。

##### 14.6.2.2 全变分（TV）先验

如果我们使用额外的正则化项，可以生成稍显更真实的图像。文献 [MV15; MV16] 建议计算图像的全变分（TV）范数。该值等于每个像素梯度的积分，可近似如下：

 $$ \mathrm{TV}(\boldsymbol{x})=\sum_{ijk}(x_{ijk}-x_{i+1,j,k})^{2}+(x_{ijk}-x_{i,j+1,k})^{2} $$ 

其中 \( x_{ijk} \) 是第 i 行、第 j 列、第 k 通道（对于RGB图像）的像素值。我们可以利用应用于每个通道的水平与垂直Sobel边缘检测器重写该式：

$$  \mathrm{TV}(\boldsymbol{x})=\sum_{k}||\mathbf{H}(\boldsymbol{x}_{:,:,k})||_{F}^{2}+||\mathbf{V}(\boldsymbol{x}_{:,:,k})||_{F}^{2}   \tag*{(14.32)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_386_123_580_317.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">鹅</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_590_123_784_324.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">鸵鸟</div>


<div style="text-align: center;">图14.33：在简单高斯先验下，使 ImageNet 类别“鹅”和“鸵鸟”概率最大化的图像。来源：http://yosinski.com/deepvis。经 Jeff Clune 许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_176_422_420_605.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_464_423_700_608.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_752_423_983_608.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图14.34：总变分范数的示意图。(a) 输入图像：一只绿海龟（经 Wikimedia 作者 P. Lindgren 许可使用）。(b) 水平差分。(c) 垂直差分。改编自 https://www.tensorflow.org/tutorials/generative/style_transfer。</div>


关于这些边缘检测器的说明见图14.34。使用 \( p(\boldsymbol{x}) \propto \exp(-\mathrm{TV}(\boldsymbol{x})) \) 可以抑制图像中出现高频伪影。在 [Yos+15] 中，他们采用了高斯模糊而非 TV 范数，但两者效果类似。

在图14.35中，我们展示了一些优化结果：从随机噪声开始，使用 TV 先验和 CNN 似然，针对不同类别标签 c 优化 \( \log p(y = c, \boldsymbol{x}) \)。

#### 14.6.3 可视化 CNN 学到的特征

研究 CNN 中“神经元”在学什么是一个有趣的问题。一种方法是：从随机图像出发，优化输入像素以最大化特定神经元的平均激活值。这被称为**激活最大化（Activation Maximization, AM）**，其技术与14.6.1节相同，但将内部节点固定在特定值，而非限制输出类别标签。

图14.36展示了将此方法（使用 TV 先验）应用于在 ImageNet 分类上训练的 AlexNet CNN 时的输出结果。我们看到，随着网络深度增加，神经元依次学习识别简单的边缘/斑点、纹理模式、物体部件，最后是完整物体。这被认为大致类似于视觉皮层的层级结构（例如，参见 [Kan+12]）。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_205_125_968_341.jpg" alt="图片" width="66%" /></div>


<div style="text-align: center;">图14.35：在TV先验下，使某些ImageNet类别的概率最大化的图像。来自https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html。经Alexander Mordvintsev许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_222_462_947_778.jpg" alt="图片" width="62%" /></div>


<div style="text-align: center;">图14.36：我们可视化了在ImageNet数据集上训练的AlexNet架构中Conv 1、3、5和fc8层神经元的“最优刺激”。对于Conv5层，我们还展示了产生类似激活的检索到的真实图像（位于“data driven”列下）。基于[MV16]中的方法。经Donglai Wei许可使用。</div>


在像素空间中进行优化的另一种方法是搜索训练集中能够最大程度激活给定神经元的图像。图14.36以Conv5层为例展示了这一点。

有关特征可视化的更多信息，请参见例如[OMS17]。

#### 14.6.4 Deep Dream

到目前为止，我们一直专注于生成能最大化类别标签或其他感兴趣神经元的图像。在本节中，我们将探讨一种更具艺术性的应用，即生成输入图像的变体，以强调某些特征。

为此，我们将预训练的图像分类器视为特征提取器。基于第14.6.3节的结果，我们知道不同层中神经元的活性对应于不同种类的

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_177_118_419_300.jpg" alt="图片" width="21%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_464_118_706_301.jpg" alt="图片" width="21%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_752_119_994_301.jpg" alt="图片" width="21%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图14.37：DeepDream 的示意图。CNN 是在 ImageNet 上训练好的 Inception 分类器。(a) 起始图像为 Aurelia aurita（又称月亮水母）。(b) 经过10次迭代后生成的图像。(c) 经过50次迭代后生成的图像。图片来自 https://en.wikipedia.org/wiki/DeepDream，经维基百科作者 Martin Thoma 许可使用。</div>

图像中的特征。假设我们想要“放大”来自层 $ l \in \mathcal{L} $ 的特征。我们可以通过定义一个能量或损失函数来实现，其形式为 $ \mathcal{L}(\boldsymbol{x}) = \sum_{l \in \mathcal{L}} \overline{\phi}_l(\boldsymbol{x}) $，其中 $ \overline{\phi}_l = \frac{1}{HWC} \sum_{hwc} \phi_{lhwc}(\boldsymbol{x}) $ 是层 $ l $ 的特征向量。现在，我们可以使用梯度下降来优化这个能量。由此产生的过程称为 DeepDream [MOT15]，因为模型会放大原始图像中仅被暗示的特征，然后生成具有越来越多此类特征的图像。$ ^{10} $

图14.37 展示了一个例子。我们从一张水母图像开始，将其输入到一个训练用于分类 ImageNet 图像的 CNN 中。经过几次迭代后，我们生成了一张图像，它是输入图像与我们在图14.33 中看到的“幻觉”的混合体；这些幻觉包括狗的局部，因为 ImageNet 的标签集中含有许多种类的狗。详见 [Tho16]，有趣的在线演示可访问 https://deepdreamgenerator.com。

#### 14.6.5 神经风格迁移

图14.37 中的 DeepDream 系统展示了 CNN 可用于创造“艺术”的一种方式。然而，它显得有点诡异。在本节中，我们讨论一种相关方法，它赋予用户更多控制。具体来说，用户必须指定一个参考“风格图像” $ \mathbf{x}_s $ 和“内容图像” $ \mathbf{x}_c $。系统将尝试生成一幅新图像 $ \mathbf{x} $，它以 $ \mathbf{x}_s $ 的风格“重新渲染” $ \mathbf{x}_c $。这称为神经风格迁移，如图14.38 和图14.39 所示。该技术最初由 [GEB16] 提出，现在已有大量相关论文；最新综述见 [Jin+17]。

##### 14.6.5.1 工作原理

风格迁移通过优化以下能量函数实现：

$$ \mathcal{L}(\boldsymbol{x}|\boldsymbol{x}_{s},\boldsymbol{x}_{c})=\lambda_{T V}\mathcal{L}_{\mathrm{T V}}(\boldsymbol{x})+\lambda_{c}\mathcal{L}_{\mathrm{c o n t e n t}}(\boldsymbol{x},\boldsymbol{x}_{c})+\lambda_{s}\mathcal{L}_{\mathrm{s t y l e}}(\boldsymbol{x},\boldsymbol{x}_{s}) \tag*{(14.33)} $$

图14.40 给出了高层示意图。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_177_126_419_309.jpg" alt="图像" width="21%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_450_126_727_309.jpg" alt="图像" width="24%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_751_126_995_309.jpg" alt="图像" width="21%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图 14.38：神经风格迁移系统的示例输出。(a) 内容图像：一只绿海龟（经维基共享资源作者 P. Lindgren 许可使用）。(b) 风格图像：瓦西里·康定斯基的画作《作品7号》。(c) 神经风格生成的输出。改编自 https://www.tensorflow.org/tutorials/generative/style_transfer。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_174_479_1026_1059.jpg" alt="图像" width="73%" /></div>

<div style="text-align: center;">图 14.39：神经风格迁移应用于“制作团队”照片，该团队为本书及其续篇创建了代码和演示。从上到下，从左到右：Kevin Murphy（作者）、Mahmoud Soliman、Aleyna Kara、Srikar Jilugu、Drishti Patel、Ming Liang Ang、Gerardo Durán-Martín、Coco（团队犬）。每张内容照片使用了不同的艺术风格。改编自 https://www.tensorflow.org/tutorials/generative/style_transfer。</div>

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_359_151_796_451.jpg" alt="图像" width="37%" /></div>


<div style="text-align: center;">图 14.40: 神经风格迁移工作原理示意图。改编自 [Zha+20] 的图 12.12.2。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_403_551_770_825.jpg" alt="图像" width="31%" /></div>


<div style="text-align: center;">图 14.41: 三种不同输入图像对应的三种特征图示意表示。改编自 [Fos19] 的图 5.16。</div>


方程 (14.33) 中的第一项是第 14.6.2.2 节讨论的全变分先验。第二项通过比较预训练 CNN 的特征图 $\phi(\boldsymbol{x})$ 在相关"内容层" l 上的表示，来衡量 $\boldsymbol{x}$ 与 $\boldsymbol{x}_{c}$ 的相似程度：

$$ \mathcal{L}_{\mathrm{content}}(\boldsymbol{x},\boldsymbol{x}_{c})=\frac{1}{C_{\ell}H_{\ell}W_{\ell}}||\boldsymbol{\phi}_{\ell}(\boldsymbol{x})-\boldsymbol{\phi}_{\ell}(\boldsymbol{x}_{c})||_{2}^{2} \tag*{(14.34)}$$

最后，我们需要定义风格项。可以将视觉风格理解为某些类型图像特征的统计分布。这些特征在图像中的位置可能无关紧要，但其共现模式至关重要。图 14.41 展示了这一概念。对人类而言，显然图像 1 与图像 2 的风格比与图像 3 的风格更为相似。直观上，这是因为图像 1 和图像 2 都包含尖刺状绿色块，而图像 3 则含有非绿色的尖刺状物体。

---

为了捕获共现统计信息，我们使用特定层 $\ell$ 的特征图计算图像的 Gram 矩阵：

$$  G_{\ell}(\boldsymbol{x})_{c,d}=\frac{1}{H_{\ell}W_{\ell}}\sum_{h=1}^{H_{\ell}}\sum_{w=1}^{W_{\ell}}\phi_{\ell}(\boldsymbol{x})_{h,w,c}\phi_{\ell}(\boldsymbol{x})_{h,w,d}   \tag*{(14.35)}$$

Gram 矩阵是一个 $C_\ell \times C_\ell$ 的矩阵，它与在每个 $H_\ell W_\ell$ 位置上采样的 $C_\ell$ 维特征向量的**非中心协方差**成正比。

据此，我们将层 $\ell$ 的风格损失定义为：

$$  \mathcal{L}_{\mathrm{s t y l e}}^{\ell}(\boldsymbol{x},\boldsymbol{x}_{s})=||\mathbf{G}_{\ell}(\boldsymbol{x})-\mathbf{G}_{\ell}(\boldsymbol{x}_{s})||_{F}^{2}   \tag*{(14.36)}$$

最后，我们将整体风格损失定义为对一组层 $\mathcal{S}$ 的损失求和：

$$  \mathcal{L}_{\mathrm{style}}(\boldsymbol{x},\boldsymbol{x}_{s})=\sum_{\ell\in\mathcal{S}}\mathcal{L}_{\mathrm{style}}^{\ell}(\boldsymbol{x},\boldsymbol{x}_{s})   \tag*{(14.37)}$$

例如，在图 14.40 中，我们计算了第 1 层和第 3 层的风格损失。（较低层会捕获视觉纹理，较高层会捕获物体布局。）

##### 14.6.5.2 加速方法

在 [GEB16] 中，他们使用 L-BFGS（第 8.3.2 节）从白噪声开始优化方程 (14.33)。如果我们使用 Adam 等优化器代替 BFGS，并从内容图像而非白噪声初始化，则可以获得更快的收敛结果。尽管如此，对每幅新的风格图像和内容图像运行优化器仍然很慢。多篇论文（例如 [JAFF16; Uly+16; UVL16; LW16]）提出训练一个神经网络直接预测此优化的结果，而不是为每对新图像求解优化问题。（这可以视为一种摊销优化形式。）具体而言，对于每幅风格图像 $\boldsymbol{x}_s$，我们拟合一个模型 $f_s$，使得 $f_s(\boldsymbol{x}_c) = \arg\min_{\boldsymbol{x}} \mathcal{L}(\boldsymbol{x}|\boldsymbol{x}_s, \boldsymbol{x}_c)$。然后我们可以将该模型应用于新的内容图像，而无需重新优化。

最近，[DSK16] 展示了如何训练一个单一网络，该网络将内容图像和风格的离散表示 s 同时作为输入，并输出 $f(\boldsymbol{x}_c, s) = \arg\min_{\boldsymbol{x}} \mathcal{L}(\boldsymbol{x}|s, \boldsymbol{x}_c)$。这避免了为每幅风格图像训练单独的网络。其关键思想是使用特定于风格的尺度和平移参数来标准化给定层的特征。具体而言，我们使用以下条件实例归一化变换：

$$  \mathrm{C I N}(\phi(\boldsymbol{x}_{c}),s)=\gamma_{s}\left(\frac{\phi(\boldsymbol{x}_{c})-\mu(\phi(\boldsymbol{x}_{c}))}{\sigma(\phi(\boldsymbol{x}_{c}))}\right)+\beta_{s}   \tag*{(14.38)}$$

其中 $\mu(\phi(\boldsymbol{x}_{c}))$ 是给定层中特征的均值，$\sigma(\phi(\boldsymbol{x}_{c}))$ 是标准差，$\beta_{s}$ 和 $\gamma_{s}$ 是风格类型 s 的参数。（关于实例归一化的更多细节见第 14.2.4.2 节。）令人惊讶的是，这一简单的技巧足以捕获多种风格。

上述技术的缺点在于它仅适用于固定数量的离散风格。[HB17] 提出将其推广，通过将常数 $\beta_s$ 和 $\gamma_s$ 替换为另一个 CNN 的输出，该 CNN 以任意风格图像 $\boldsymbol{x}_s$ 作为输入。即在方程 (14.38) 中，我们设 $\beta_s = f_{\beta}(\phi(\boldsymbol{x}_s))$

---

以及 $ \gamma_s = f_\gamma(\phi(\boldsymbol{x}_s)) $，并且我们与其他所有参数一起学习参数 $ \beta $ 和 $ \gamma $。该模型变为

$$  \mathrm{A I N}(\phi(\boldsymbol{x}_{c}),\phi(\boldsymbol{x}_{s}))=f_{\gamma}(\phi(\boldsymbol{x}_{s}))\left(\frac{\phi(\boldsymbol{x}_{c})-\mu(\phi(\boldsymbol{x}_{c}))}{\sigma(\phi(\boldsymbol{x}_{c}))}\right)+f_{\beta}(\phi(\boldsymbol{x}_{s}))   \tag*{(14.39)}$$

他们将这种方法称为**自适应实例归一化**。

---

请提供需要翻译的英文学术论文 Markdown 文本。

---

## 15 序列的神经网络

### 15.1 引言

在本章中，我们讨论各种用于序列的神经网络。我们将考虑输入是序列、输出是序列、或两者都是序列的情况。这类模型有很多应用，例如机器翻译、语音识别、文本分类、图像描述等。我们的讲解借鉴了 $ [Zha+20] $ 的部分内容，更多细节可参考该文献。

### 15.2 循环神经网络（RNNs）

循环神经网络（RNN）是一种以有状态方式将序列输入空间映射到序列输出空间的神经网络。也就是说，输出 $ \pmb{y}_{t} $ 的预测不仅取决于输入 $ \pmb{x}_{t} $，还取决于系统的隐状态 $ \pmb{h}_{t} $，该隐状态会随着序列的处理随时间更新。此类模型可用于序列生成、序列分类和序列翻译，我们将在下文进行说明。 $ ^{1} $

#### 15.2.1 Vec2Seq（序列生成）

在本节中，我们讨论如何学习形如 $ f_{\theta} : \mathbb{R}^D \to \mathbb{R}^{N_\infty C} $ 的函数，其中 $ D $ 是输入向量的大小，输出是任意长度的向量序列，每个向量大小为 $ C $。（注意，单词是离散的标记，但可以按照第 1.5.4 节的讨论转换为实值向量。）我们将这些模型称为 $ \text{vec2seq} $ 模型，因为它们将向量映射为序列。

输出序列 $ \mathbf{y}_{1:T} $ 每次生成一个标记。在每一步，我们从模型的隐状态 $ \mathbf{h}_t $ 中采样 $ \tilde{y}_t $，然后将其“反馈”回模型以获得新状态 $ \mathbf{h}_{t+1} $（该状态也依赖于输入 $ \mathbf{x} $）。如图 15.1 所示。通过这种方式，模型定义了一种形如 $ p(\mathbf{y}_{1:T}|\mathbf{x}) $ 的条件生成模型，该模型捕捉了输出标记之间的依赖关系。我们将在下面更详细地解释这一点。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_461_115_713_334.jpg" alt="图像" width="21%" /></div>

<div style="text-align: center;">图 15.1: 循环神经网络（RNN）用于在给定可选固定长度输入向量 $\mathbf{x}$ 时生成变长输出序列 $\mathbf{y}_{1:T}$。</div>

##### 15.2.1.1 模型

为简化符号，令 T 表示输出长度（这里假设它是由动态选择的）。则 RNN 对应于以下条件生成模型：

$$  p(\boldsymbol{y}_{1:T}|\boldsymbol{x})=\sum_{h_{1:T}}p(\boldsymbol{y}_{1:T},\boldsymbol{h}_{1:T}|\boldsymbol{x})=\sum_{h_{1:T}}\prod_{t=1}^{T}p(\boldsymbol{y}_{t}|\boldsymbol{h}_{t})p(\boldsymbol{h}_{t}|\boldsymbol{h}_{t-1},\boldsymbol{y}_{t-1},\boldsymbol{x})   \tag*{(15.1)}$$

其中 $\boldsymbol{h}_t$ 是隐藏状态，并且我们将 $p(\boldsymbol{h}_1|\boldsymbol{h}_0,\boldsymbol{y}_0,\boldsymbol{x}) = p(\boldsymbol{h}_1|\boldsymbol{x})$ 定义为初始隐藏状态分布（通常是确定性的）。

输出分布通常由下式给出：

$$  p(\boldsymbol{y}_{t}|\boldsymbol{h}_{t})=Cat(\boldsymbol{y}_{t}|softmax(\boldsymbol{W}_{hy}\boldsymbol{h}_{t}+\boldsymbol{b}_{y}))   \tag*{(15.2)}$$

其中 $\mathbf{W}_{hy}$ 是隐藏层到输出层的权重，$\mathbf{b}_{y}$ 是偏置项。然而，对于实值输出，我们可以使用

$$  p(\boldsymbol{y}_{t}|\boldsymbol{h}_{t})=\mathcal{N}(\boldsymbol{y}_{t}|\mathbf{W}_{h y}\boldsymbol{h}_{t}+\boldsymbol{b}_{y},\sigma^{2}\mathbf{I})   \tag*{(15.3)}$$

我们假设隐藏状态按如下方式确定性计算：

$$  p(h_{t}|h_{t-1},y_{t-1},x)=\mathbb{I}(h_{t}=f(h_{t-1},y_{t-1},x))   \tag*{(15.4)}$$

其中 f 是一个确定性函数。通常，更新函数 f 由下式给出：

$$  \boldsymbol{h}_{t}=\varphi(\mathbf{W}_{x h}[\boldsymbol{x};\boldsymbol{y}_{t-1}]+\mathbf{W}_{h h}\boldsymbol{h}_{t-1}+\boldsymbol{b}_{h})   \tag*{(15.5)}$$

其中 $\mathbf{W}_{hh}$ 是隐藏层到隐藏层的权重，$\mathbf{W}_{xh}$ 是输入层到隐藏层的权重，$\mathbf{b}_{h}$ 是偏置项。参见图 15.1 的示意图，并参阅 $\text{rnn\_jax.ipynb}$ 获取相关代码。

注意，$y_t$ 依赖于 $h_t$，而 $h_t$ 依赖于 $y_{t-1}$，又依赖于 $h_{t-1}$，依此类推。因此，$y_t$ 隐式地依赖于所有过去的观测值（以及可选的固定输入 $\mathbf{x}$）。因此，RNN 克服了标准马尔可夫模型的局限性，因为它可以拥有无界记忆。这使得 RNN 在理论上与图灵机一样强大 [SS95; PMB19]。在实践中，

---

时间旅行者手中握着的东西是一个闪闪发光的金属框架，几乎不比一只小钟大，制作非常精致。里面有象牙，还有一些透明晶体物质。后者与 s bettyre tat howhong s ie 时间 thave ler

simk you a dimensions le ghat dionthat 可以任意在空间和时间的任何方向上旅行，由驾驶者决定。菲尔比只是笑了笑。“但我有实验验证，”时间旅行者说，“这对历史来说将非常方便。”

<div style="text-align: center;">图 15.2：给定前缀“the”时，字符级 RNN 生成的长度为 500 的示例输出。我们使用贪心解码，计算每一步最可能的字符，然后将其反馈回模型。该模型在 H. G. 威尔斯的小说《时间机器》上训练。由 rnn_jax.ipynb 生成。</div>

然而，记忆长度由潜在状态的大小和参数的强度决定；关于这一点的进一步讨论见第 15.2.7 节。

当我们从 RNN 生成时，我们从 $ \tilde{y}_t \sim p(y_t | h_t) $ 中采样，然后将采样值“馈入”隐藏状态，以确定性地计算 $ h_{t+1} = f(h_t, \tilde{y}_t, \mathbf{x}) $，进而从中采样 $ \tilde{y}_{t+1} \sim p(y_{t+1} | h_{t+1}) $，依此类推。因此，系统中唯一的随机性来自观测（输出）模型中的噪声，该噪声在每一步被反馈回系统。（然而，有一种变体称为**变分 RNN** [Chu+15]，它在 $ h_t $ 的动态中增加了与观测噪声无关的随机性。）

##### 15.2.1.2 应用

RNN 可用于无条件生成序列（通过设置 $ \boldsymbol{x} = \emptyset $）或基于 $ \boldsymbol{x} $ 条件生成。无条件序列生成通常称为**语言建模**；它指的是学习离散标记序列上的联合概率分布，即形如 $ p(y_1, \ldots, y_T) $ 的模型。（另见第 3.6.1.2 节，我们讨论了使用马尔可夫链进行语言建模。）

图 15.2 展示了一个由简单 RNN 生成的序列，该 RNN 在 H. G. 威尔斯的小说《时间机器》上训练。（这是一部短篇科幻小说，仅 32,000 个单词和 170k 个字符。）我们看到生成的序列看起来很合理，尽管意义不大。通过使用更复杂的 RNN 模型（如我们在第 15.2.7.1 节和第 15.2.7.2 节中讨论的模型），并在更多数据上训练，我们可以创建在语言建模任务上达到最先进性能的 RNN [CNB17]。（在语言建模领域，性能通常用困惑度衡量，它只是平均每个标记的负对数似然的指数；更多信息参见第 6.1.5 节。）

我们还可以让生成的序列依赖于某种输入向量 x。例如，考虑图像描述任务：在这种情况下，x 是由 CNN 计算的图像的某种嵌入，如图 15.3 所示。有关图像描述方法的综述，参见例如 [Hos+19; LXW19]，以及带有代码的教程：https://bit.ly/2Wvs1GK。

也可以使用 RNN 生成实值特征向量的序列，例如手写字符的笔划 [Gra13] 和手绘形状 [HE18]。这对于时间序列预测实值序列也很有用。

#### 15.2.2 Seq2Vec（序列分类）

在本节中，我们假设给定一个可变长度的输入序列，我们想要预测一个固定长度的输出向量 $ \mathbf{y} $。因此，我们需要学习一个形如 $ f_{\theta} : \mathbb{R}^{TD} \to \mathbb{R}^C $ 的函数。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_299_127_846_387.jpg" alt="图像" width="47%" /></div>


<div style="text-align: center;">图 15.3：图像描述生成中 CNN-RNN 模型的示意图。标有“LSTM”的粉色方框指代一种特定的 RNN，我们将在第 15.2.7.2 节讨论。标有 $ W_{emb} $ 的粉色方框指代（采样后的）独热令牌的嵌入矩阵，因此模型的输入是一个实值向量。图片来源：https://bit.ly/2FKmqHm，经 Yunjey Choi 许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_205_541_873_827.jpg" alt="图像" width="57%" /></div>


<div style="text-align: center;">图 15.4：(a) 用于序列分类的 RNN。(b) 用于序列分类的双向 RNN。</div>


我们称之为 **seq2vec 模型**。为符号简洁起见，我们重点关注输出为类别标签 $ y \in \{1, \ldots, C\} $ 的情况。

最简单的方法是将 RNN 的最终状态作为分类器的输入：

$$  p(y|\boldsymbol{x}_{1:T}) = Cat(y|softmax(\mathbf{W}\boldsymbol{h}_{T}))   \tag*{(15.6)}$$

如图 15.4a 所示。

通常，如果让 RNN 的隐藏状态同时依赖于过去和未来的上下文，我们可以获得更好的结果。为此，我们创建两个 RNN，一个沿前向方向递归计算隐藏状态，另一个沿后向方向递归计算隐藏状态。这称为 **双向 RNN** [SP97]。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_251_114_874_364.jpg" alt="图像" width="54%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 15.5: (a) 用于将一个序列转换为另一个对齐序列的 RNN。 (b) 用于同一任务的双向 RNN。</div>


更确切地说，该模型定义如下：

$$  \boldsymbol{h}_{t}^{\rightarrow}=\varphi(\mathbf{W}_{x h}^{\rightarrow}\boldsymbol{x}_{t}+\mathbf{W}_{h h}^{\rightarrow}\boldsymbol{h}_{t-1}^{\rightarrow}+\boldsymbol{b}_{h}^{\rightarrow})   \tag*{(15.7)}$$

$$  \boldsymbol{h}_{t}^{\leftarrow}=\varphi(\mathbf{W}_{x h}^{\leftarrow}\boldsymbol{x}_{t}+\mathbf{W}_{h h}^{\leftarrow}\boldsymbol{h}_{t+1}^{\leftarrow}+\boldsymbol{b}_{h}^{\leftarrow})   \tag*{(15.8)}$$

然后我们定义 $ \boldsymbol{h}_t = [\boldsymbol{h}_t^\rightarrow, \boldsymbol{h}_t^\leftarrow] $ 为时刻 $ t $ 的状态表示，该表示综合了过去和未来的信息。最后，我们对这些隐状态进行平均池化，以得到最终的分类器：

$$  p(y|\pmb{x}_{1:T})=\mathrm{Cat}(y|\mathrm{softmax}(\pmb{W}\overline{h}))   \tag*{(15.9)}$$

$$  \overline{h}=\frac{1}{T}\sum_{t=1}^{T}h_{t}   \tag*{(15.10)}$$

示意图见图 15.4b，相关代码见 rnn_sentiment_jax.ipynb。（这与第 15.3.1 节中的一维 CNN 文本分类器类似。）

#### 15.2.3 序列到序列（序列翻译）

在本节中，我们考虑学习形式为 $ f_{\theta} : \mathbb{R}^{TD} \to \mathbb{R}^{T'C} $ 的函数。我们讨论两种情形：一种是 $ T' = T $，即输入和输出序列长度相等（因此是对齐的）；另一种是 $ T' \neq T $，即输入和输出序列长度不同。这被称为序列到序列（seq2seq）问题。

##### 15.2.3.1 对齐情况

在本节中，我们考虑输入和输出序列已对齐的情形。这也可以视为密集序列标注，因为我们对每个位置预测一个标签。我们可以直接修改 RNN 来解决该任务，如图 15.5a 所示。其数学表达为：

$$  p(\boldsymbol{y}_{1:T}|\boldsymbol{x}_{1:T})=\sum_{\boldsymbol{h}_{1:T}}\prod_{t=1}^{T}p(\boldsymbol{y}_{t}|\boldsymbol{h}_{t})\mathbb{I}\left(\boldsymbol{h}_{t}=f(\boldsymbol{h}_{t-1},\boldsymbol{x}_{t})\right)   \tag*{(15.11)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_394_123_729_407.jpg" alt="图片" width="29%" /></div>

<div style="text-align: center;">图15.6：深度RNN的示意图。改编自 [Zha+20] 的图9.3.1。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_251_480_918_693.jpg" alt="图片" width="57%" /></div>

<div style="text-align: center;">图15.7：用于将序列 x1:T 映射到序列 y1:T' 的编码器-解码器RNN架构</div>

其中我们定义 $\boldsymbol{h}_{1}=f(\boldsymbol{h}_{0},\boldsymbol{x}_{1})=f_{0}(\boldsymbol{x}_{1})$ 为初始状态。

注意，$ y_t $ 依赖于 $ h_t $，而 $ h_t $ 仅依赖于过去的输入 $ x_{1:t} $。如果我们让解码器不仅查看 $ x $ 的过去，还查看其“未来”，即使用双向RNN（如图15.5b所示），我们可以获得更好的结果。

通过将多个隐藏链堆叠在一起，我们可以创建更具表达力的模型，如图15.6所示。第 $ l $ 层在时间 $ t $ 的隐藏单元通过下式计算：

$$ \boldsymbol{h}_{t}^{l}=\varphi_{l}(\mathbf{W}_{x h}^{l}\boldsymbol{h}_{t}^{l-1}+\mathbf{W}_{h h}^{l}\boldsymbol{h}_{t-1}^{l}+\boldsymbol{b}_{h}^{l}) \tag*{(15.12)} $$

输出由下式给出：

$$ \boldsymbol{o}_{t}=\mathbf{W}_{h o}\boldsymbol{h}_{t}^{L}+\boldsymbol{b}_{o} \tag*{(15.13)} $$

##### 15.2.3.2 未对齐情况

在本节中，我们讨论如何学习从长度为 $ T $ 的一个序列到长度为 $ T' $ 的另一个序列的映射。我们首先使用RNN的最后一个状态（或对双向RNN进行平均池化）对输入序列进行编码，得到上下文向量 $ \mathbf{c} = f_e(\mathbf{x}_{1:T}) $。然后，我们使用RNN生成输出序列。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_179_132_570_411.jpg" alt="图像" width="33%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_680_156_910_403.jpg" alt="图像" width="19%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 15.8: (a) 将英语翻译为法语的 seq2seq 模型示意图。字符“-”表示句子结束。摘自 [Luo16] 的图 2.4，经 Minh-Thang Luong 友好许可使用。(b) 贪心解码示意图。每一步中最可能的法语单词以绿色高亮显示，然后作为输入馈送到解码器的下一步。摘自 [Luo16] 的图 2.5，经 Minh-Thang Luong 友好许可使用。</div>

解码器 $ \mathbf{y}_{1:T'} = f_d(\mathbf{c}) $。这被称为编码器-解码器架构 [SVL14; Cho+14a]。如图 15.7 所示。

该架构的一个重要应用是机器翻译。当使用 RNN 处理时，称为神经机器翻译（区别于不使用神经网络的旧方法统计机器翻译）。基本思想见图 15.8a，更详细的代码见 nmt_jax.ipynb。关于 NMT 文献的综述，请参阅 [Luo16; Neu17]。

#### 15.2.4 教师强制

训练语言模型时，词序列 w1, w2, …, wT 的似然由下式给出：

$$  p(\boldsymbol{w}_{1:T})=\prod_{t=1}^{T}p(w_{t}|\boldsymbol{w}_{1:t-1})   \tag*{(15.14)}$$

因此，在 RNN 中，我们将输入设为 $ x_t = w_{t-1} $，输出设为 $ y_t = w_t $。注意，我们依赖于过去的历史真实标签 $ \boldsymbol{w}_{1:t-1} $，而非模型生成的标签。这被称为**教师强制**，因为教师的真实值在每个步骤被“强制”作为模型输入（即 $ x_t $ 被设为 $ w_{t-1} $）。

遗憾的是，教师强制有时会导致模型在测试时表现不佳。原因在于模型仅在“正确”输入上训练过，因此在测试阶段，若遇到由前一步生成且不同于训练数据的输入序列 $ \pmb{w}_{1:t-1} $，模型可能不知道如何处理。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_239_138_927_464.jpg" alt="图像" width="59%" /></div>


<div style="text-align: center;">图15.9: 一个RNN在时间上展开（垂直方向）3个时间步，显式展示了目标输出序列和损失节点。摘自 $[Zha+20]$ 的图8.7.2。经Aston Zhang许可使用。</div>


对此的一种常见解决方案称为**计划采样**[Ben+15a]。该方法初始时使用教师强制，但在随机时间步上，取而代之的是输入从模型生成的样本；这种替换发生的比例逐渐增加。

另一种替代方案是使用其他类型的模型，在这些模型上极大似然估计训练效果更好，例如一维卷积神经网络（第15.3节）和Transformer（第15.5节）。

#### 15.2.5 时间反向传播

我们可以通过求解 $ \boldsymbol{\theta}^* = \arg\max_{\boldsymbol{\theta}} p(\boldsymbol{y}_{1:T} | \boldsymbol{x}_{1:T}, \boldsymbol{\theta}) $ 来计算RNN参数的极大似然估计，这里为简化符号假设只有单个训练序列。要计算极大似然估计，需要计算损失相对于参数的梯度。为此，我们可以像图15.9所示那样展开计算图，然后应用反向传播算法。这被称为**时间反向传播**（BPTT）[Wer90]。

更精确地，考虑以下模型：

$$  \boldsymbol{h}_{t}=\mathbf{W}_{h x}\boldsymbol{x}_{t}+\mathbf{W}_{h h}\boldsymbol{h}_{t-1}   \tag*{(15.15)}$$

$$  \boldsymbol{o}_{t}=\mathbf{W}_{h o}\boldsymbol{h}_{t}   \tag*{(15.16)}$$

其中 $ o_t $ 是输出对数几率，为简化符号我们省略了偏置项。我们假设 $ y_y $ 是每个时间步的真实目标标签，因此定义损失为

$$  L=\frac{1}{T}\sum_{t=1}^{T}\ell(y_{t},\boldsymbol{o}_{t})   \tag*{(15.17)}$$

我们需要计算导数 $ \frac{\partial L}{\partial \mathbf{W}_{hx}} $、$ \frac{\partial L}{\partial \mathbf{W}_{hh}} $ 和 $ \frac{\partial L}{\partial \mathbf{W}_{ho}} $。最后一项比较容易，因为它仅依赖于每个时间步的局部信息。然而，前两项依赖于隐藏状态，因此需要沿时间反向计算。

---

We simplify the notation by defining

$$  \boldsymbol{h}_{t}=f(\boldsymbol{x}_{t},\boldsymbol{h}_{t-1},\boldsymbol{w}_{h})   \tag*{(15.18)}$$

$$  \boldsymbol{o}_{t}=g(\boldsymbol{h}_{t},\boldsymbol{w}_{o})   \tag*{(15.19)}$$

where  $ \boldsymbol{w}_{h} $ is the flattened version of  $ \mathbf{W}_{hh} $ and  $ \mathbf{W}_{hx} $ stacked together. We focus on computing  $ \frac{\partial L}{\partial \boldsymbol{w}_{h}} $ By the chain rule, we have

$$  \frac{\partial L}{\partial\boldsymbol{w}_{h}}=\frac{1}{T}\sum_{t=1}^{T}\frac{\partial\ell(y_{t},\boldsymbol{o}_{t})}{\partial\boldsymbol{w}_{h}}=\frac{1}{T}\sum_{t=1}^{T}\frac{\partial\ell(y_{t},\boldsymbol{o}_{t})}{\partial\boldsymbol{o}_{t}}\frac{\partial g(\boldsymbol{h}_{t},\boldsymbol{w}_{o})}{\partial\boldsymbol{h}_{t}}\frac{\partial\boldsymbol{h}_{t}}{\partial\boldsymbol{w}_{h}}   \tag*{(15.20)}$$

We can expand the last term as follows:

$$  \frac{\partial\boldsymbol{h}_{t}}{\partial\boldsymbol{w}_{h}}=\frac{\partial f(\boldsymbol{x}_{t},\boldsymbol{h}_{t-1},\boldsymbol{w}_{h})}{\partial\boldsymbol{w}_{h}}+\frac{\partial f(\boldsymbol{x}_{t},\boldsymbol{h}_{t-1},\boldsymbol{w}_{h})}{\partial\boldsymbol{h}_{t-1}}\frac{\partial\boldsymbol{h}_{t-1}}{\partial\boldsymbol{w}_{h}}   \tag*{(15.21)}$$

If we expand this recursively, we find the following result (see the derivation in [Zha+20, Sec 8.7]):

$$  \frac{\partial\boldsymbol{h}_{t}}{\partial\boldsymbol{w}_{h}}=\frac{\partial f(\boldsymbol{x}_{t},\boldsymbol{h}_{t-1},\boldsymbol{w}_{h})}{\partial\boldsymbol{w}_{h}}+\sum_{i=1}^{t-1}\left(\prod_{j=i+1}^{t}\frac{\partial f(\boldsymbol{x}_{j},\boldsymbol{h}_{j-1},\boldsymbol{w}_{h})}{\partial\boldsymbol{h}_{j-1}}\right)\frac{\partial f(\boldsymbol{x}_{i},\boldsymbol{h}_{i-1},\boldsymbol{w}_{h})}{\partial\boldsymbol{w}_{h}}   \tag*{(15.22)}$$

Unfortunately, this takes  $ O(T) $ time to compute per time step, for a total of  $ O(T^2) $ overall. It is therefore standard to truncate the sum to the most recent  $ K $ terms. It is possible to adaptively pick a suitable truncation parameter  $ K $ [AFF19]; however, it is usually set equal to the length of the subsequence in the current minibatch.

When using truncated BPTT, we can train the model with batches of short sequences, usually created by extracting non-overlapping subsequences (windows) from the original sequence. If the previous subsequence ends at time t - 1, and the current subsequence starts at time t, we can “carry over” the hidden state of the RNN across batch updates during training. However, if the subsequences are not ordered, we need to reset the hidden state. See rnn_jax.ipynb for some sample code that illustrates these details.

#### 15.2.6 Vanishing and exploding gradients

Unfortunately, the activations in an RNN can decay or explode as we go forwards in time, since we multiply by the weight matrix  $ \mathbf{W}_{hh} $ at each time step. Similarly, the gradients in an RNN can decay or explode as we go backwards in time, since we multiply the Jacobians at each time step (see Section 13.4.2 for details). A simple heuristic is to use gradient clipping (Equation (13.70)). More sophisticated methods attempt to control the spectral radius  $ \lambda $ of the forward mapping,  $ \mathbf{W}_{hh} $, as well as the backwards mapping, given by the Jacobian  $ \mathbf{J}_{hh} $.

The simplest way to control the spectral radius is to randomly initialize  $ \mathbf{W}_{hh} $ in such a way as to ensure  $ \lambda \approx 1 $, and then keep it fixed (i.e., we do not learn  $ \mathbf{W}_{hh} $). In this case, only the output matrix  $ \mathbf{W}_{ho} $ needs to be learned, resulting in a convex optimization problem. This is called an echo state network [JH04]. A closely related approach, known as a liquid state machine [MNM02], uses binary-valued (spiking) neurons instead of real-valued neurons. A generic term for both ESNs

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_307_136_840_534.jpg" alt="图像" width="46%" /></div>

<div style="text-align: center;">图15.10：GRU的示意图。改编自$[Zha+20]$的图9.1.3。</div>

而LSM属于储层计算[LJ09]。解决该问题的另一种方法是使用约束优化来确保$W_{hh}$矩阵保持正交[Vor+17]。

显式控制谱半径的另一种方法是修改RNN架构本身，使用加法而不是乘法更新隐藏状态，我们将在第15.2.7节讨论。这显著提高了训练稳定性。

#### 15.2.7 门控与长期记忆

具有足够隐藏单元的RNN原则上可以记住很久以前的输入。然而，在实践中，“普通”RNN无法做到这一点，因为存在梯度消失问题（第13.4.2节）。在本节中，我们给出了一种解决方案，即用加法方式更新隐藏状态，类似于残差网络（第14.3.4节）。

##### 15.2.7.1 门控循环单元（GRU）

在本节中，我们讨论使用门控循环单元（GRU）的模型，如[Cho+14a]所提出的。关键思想是通过使用门控单元来学习何时更新隐藏状态。这可以用来在首次看到重要信息时选择性地“记住”它们。该模型还可以学习何时重置隐藏状态，从而忘记不再有用的信息。

为了更详细地解释该模型，我们按照$[\mathrm{Zha}+20, \mathrm{Sec} \, 8.8]$的表述分两步介绍。我们假设$\mathbf{X}_t$是一个$N \times D$矩阵，其中$N$是批量大小，$D$是词汇量大小。类似地，$\mathbf{H}_t$是一个$N \times H$矩阵，其中$H$是时间$t$的隐藏单元数量。

---

重置门 $ \mathbf{R}_t \in \mathbb{R}^{N \times H} $ 和更新门 $ \mathbf{Z}_t \in \mathbb{R}^{N \times H} $ 的计算公式为：

$$  \mathbf{R}_{t}=\sigma(\mathbf{X}_{t}\mathbf{W}_{x r}+\mathbf{H}_{t-1}\mathbf{W}_{h r}+\mathbf{b}_{r})   \tag*{(15.23)}$$

$$  \mathbf{Z}_{t}=\sigma(\mathbf{X}_{t}\mathbf{W}_{xz}+\mathbf{H}_{t-1}\mathbf{W}_{hz}+\mathbf{b}_{z})   \tag*{(15.24)}$$

注意，由于 Sigmoid 函数的性质，$ \mathbf{R}_t $ 和 $ \mathbf{Z}_t $ 的每个元素都位于 $ [0,1] $ 区间内。基于此，我们使用以下公式定义“候选”下一状态向量：

$$  \tilde{\mathbf{H}}_{t}=\tanh(\mathbf{X}_{t}\mathbf{W}_{x h}+(\mathbf{R}_{t}\odot\mathbf{H}_{t-1})\mathbf{W}_{h h}+\mathbf{b}_{h})   \tag*{(15.25)}$$

该公式将未被重置的旧记忆（通过 $ \mathbf{R}_t \odot \mathbf{H}_{t-1} $ 计算得到）与新输入 $ \mathbf{X}_t $ 相结合。我们通过 tanh 函数对得到的线性组合进行变换，以确保隐藏单元保持在 $ (-1, 1) $ 区间内。如果重置门 $ \mathbf{R}_t $ 的元素接近 1，则模型退化为标准 RNN 更新规则。如果元素接近 0，则模型更像一个应用于 $ \mathbf{X}_t $ 的 MLP。因此，重置门能够捕获新的短期信息。

一旦计算出候选新状态，模型便通过更新门 $ \mathbf{Z}_t $ 和 $ 1 - \mathbf{Z}_t $ 从候选状态 $ \tilde{H}_t $ 中选择维度，同时将剩余维度保留为其旧值 $ \mathbf{H}_{t-1} $，从而计算实际新状态：

$$  \mathbf{H}_{t}=\mathbf{Z}_{t}\odot\mathbf{H}_{t-1}+\left(1-\mathbf{Z}_{t}\right)\odot\tilde{\mathbf{H}}_{t}   \tag*{(15.26)}$$

当 $ Z_{td} = 1 $ 时，我们直接传递 $ H_{t-1,d} $ 而不做改变，并忽略 $ X_t $。因此，更新门能够捕获长期依赖关系。

整体架构如图 15.10 所示，示例代码见 gru_jax.ipynb。

##### 15.2.7.2 长短期记忆（LSTM）

本节讨论 [HS97b] 提出的长短期记忆（LSTM）模型，它是 GRU 的更复杂版本（并且比 GRU 早提出近 20 年）。更详细的介绍请参见 https://colah.github.io/posts/2015-08-Understanding-LSTMs。

基本思想是用一个记忆细胞 $ c_t $ 来增强隐藏状态 $ h_t $。我们需要三个门来控制这个细胞：输出门 $ O_t $ 决定读取出什么；输入门 $ I_t $ 决定读入什么；遗忘门 $ F_t $ 决定何时重置细胞。这些门的计算如下：

$$  \mathbf{O}_{t}=\sigma(\mathbf{X}_{t}\mathbf{W}_{x o}+\mathbf{H}_{t-1}\mathbf{W}_{h o}+\mathbf{b}_{o})   \tag*{(15.27)}$$

$$  \mathbf{I}_{t}=\sigma(\mathbf{X}_{t}\mathbf{W}_{x i}+\mathbf{H}_{t-1}\mathbf{W}_{h i}+\mathbf{b}_{i})   \tag*{(15.28)}$$

$$  \mathbf{F}_{t}=\sigma(\mathbf{X}_{t}\mathbf{W}_{x f}+\mathbf{H}_{t-1}\mathbf{W}_{h f}+\mathbf{b}_{f})   \tag*{(15.29)}$$

然后计算候选细胞状态：

$$  \mathbf{\tilde{C}}_{t}=\tanh(\mathbf{X}_{t}\mathbf{W}_{xc}+\mathbf{H}_{t-1}\mathbf{W}_{hc}+\mathbf{b}_{c})   \tag*{(15.30)}$$

细胞的实际更新要么是候选细胞（如果输入门开启），要么是旧细胞（如果非遗忘门开启）：

$$  \mathbf{C}_{t}=\mathbf{F}_{t}\odot\mathbf{C}_{t-1}+\mathbf{I}_{t}\odot\tilde{\mathbf{C}}_{t}   \tag*{(15.31)}$$

作者：Kevin P. Murphy。（C）MIT 出版社。CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_306_134_849_468.jpg" alt="图片" width="47%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_297_492_837_531.jpg" alt="图片" width="46%" /></div>

<div style="text-align: center;">图 15.11: LSTM 示意图。改编自文献 [Zha+20] 中的图 9.2.4。</div>

如果 $\mathbf{F}_t = 1$ 且 $\mathbf{I}_t = 0$，则模型可以记住长期记忆。$^{2}$

最后，我们计算隐藏状态，使其成为细胞状态的变换版本，前提是输出门打开：

$$ \mathbf{H}_{t}=\mathbf{O}_{t}\odot\tanh(\mathbf{C}_{t}) \tag*{(15.32)} $$

注意，$\mathbf{H}_t$ 既作为该单元的输出，也作为下一时间步的隐藏状态使用。这使得模型能够记住刚输出的内容（短期记忆），而细胞状态 $\mathbf{C}_t$ 则充当长期记忆。整体模型的示意图见图 15.11，相关示例代码见 lstm_jax.ipynb。

有时我们会添加窥视孔连接，即将细胞状态作为额外输入传递给各门控。此外，还有许多其他变体被提出。事实上，[JZS15] 使用遗传算法测试了超过 10,000 种不同的架构。其中一些架构的效果优于 LSTM 或 GRU，但总体而言，LSTM 在大多数任务上表现稳定。类似结论也在 [Gre+17] 中得到验证。最近，[ZL17] 使用 RNN 控制器生成字符串来指定 RNN 架构，并通过强化学习训练该控制器，从而得到一种优于 LSTM 的新型细胞结构。然而，该结构相当复杂，尚未被社区广泛采用。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_212_131_571_349.jpg" alt="图像" width="31%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_620_130_979_350.jpg" alt="图像" width="31%" /></div>


<div style="text-align: center;">图15.12：两个不同序列在每一步生成每个词元的条件概率。来自  $ [Zha+20] $ 的图9.8.1–9.8.2，经Aston Zhang许可使用。</div>


#### 15.2.8 束搜索

从RNN生成序列的最简单方法是使用贪心解码，即每一步计算  $ \hat{y}_t = \arg\max_y p(y_t = y|\hat{\mathbf{y}}_{1:t}, \mathbf{x}) $。重复该过程直至生成句尾词元。图15.8b展示了此方法在神经机器翻译中的应用示例。

不幸的是，贪心解码无法生成MAP序列，该序列定义为  $ \mathbf{y}_{1:T}^{*}=\operatorname{argmax}_{\mathbf{y}_{1:T}}p(\mathbf{y}_{1:T}|\mathbf{x}) $。原因在于，第  $ t $ 步的局部最优词元可能并不在全局最优路径上。

例如，考虑图15.12a。我们在第1步贪心地选取了MAP词元A。在此基础上，假设  $ p(y_2|y_1 = A) = [0.1, 0.4, 0.3, 0.2] $（如图所示）。我们从中贪心地选取了MAP词元B。再在此基础上，假设  $ p(y_3|y_1 = A, y_2 = B) = [0.2, 0.2, 0.4, 0.2] $（如图所示）。我们从中贪心地选取了MAP词元C。接着在此基础上，假设  $ p(y_4|y_1 = A, y_2 = B, y_3 = C) = [0.0, 0.2, 0.2, 0.6] $（如图所示）。我们从中贪心地选取了MAP词元eos（句尾），于是停止生成。生成序列的总概率为  $ 0.5 \times 0.4 \times 0.4 \times 0.6 = 0.048 $。

现在考虑图15.12b。在第2步，假设我们选取了第二大概率的词元，即C。在此基础上，假设  $ p(y_3|y_1 = A, y_2 = C) = [0.1, 0.6, 0.2, 0.1] $（如图所示）。我们从中贪心地选取了MAP词元B。再在此基础上，假设  $ p(y_4|y_1 = A, y_2 = C, y_3 = B) = [0.1, 0.2, 0.1, 0.6] $（如图所示）。我们从中贪心地选取了MAP词元eos，于是停止生成。生成序列的总概率为  $ 0.5 \times 0.3 \times 0.6 \times 0.6 = 0.054 $。因此，通过降低贪心程度，我们找到了一条整体似然更高的序列。

对于隐马尔可夫模型，我们可以使用一种称为维特比解码的算法（这是动态规划的一个实例），在  $ O(TV^2) $ 时间内计算全局最优序列，其中V是词汇表中的单词数量（详见[Mur23]）。但对于RNN，计算全局最优解需要  $ O(V^T) $ 时间，因为隐藏状态并非数据的充分统计量。

**束搜索**是一种速度更快的启发式方法。在该方法中，我们每一步计算前K个候选输出；然后逐一将其扩展为所有V种可能，生成VK个候选，从中再次选取前K个。该过程如图15.13所示。

也可以将该算法扩展为不放回地采样前K个序列。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_335_127_829_406.jpg" alt="图像" width="42%" /></div>

<div style="text-align: center;">图 15.13：束搜索（beam search）示意图，束宽 K=2。词汇表为 $ \mathcal{Y} = \{A, B, C, D, E\} $，大小为 V=5。假设第 1 步得分最高的两个符号是 A 和 C。在第 2 步，对于每个 $ y \in \mathcal{Y} $，我们计算 $ p(y_1 = A, y_2 = y) $ 和 $ p(y_1 = C, y_2 = y) $。这需要 $ O(KV) $ 时间。然后选择得分最高的两个部分路径，即 $ (y_1 = A, y_2 = B) $ 和 $ (y_1 = C, y_2 = E) $，并继续以明显的方式推进。改编自 $ [Zha + 20] $ 的图 9.8.3。</div>

（即选择得分最高的一个，重新归一化，再选择新的得分最高的一个，以此类推），这种方法称为随机束搜索（stochastic beam search）。该方法在每个步骤向模型的部分概率中添加 Gumbel 噪声。详见 [KHW19]；顺序替代方案参见 [SBS20]。这些采样方法可以提高输出的多样性。（另见 [Vij+18] 的确定性多样化束搜索方法。）

### 15.3 一维卷积神经网络

卷积神经网络（第 14 章）使用共享权重为每个输入计算其局部邻域的函数，并返回一个输出。它们通常用于二维输入，但也可以应用于一维情况，如下所述。它们是循环神经网络（RNN）的一种有趣的替代方案，并且更易于训练，因为它们不需要维护长期隐藏状态。

#### 15.3.1 用于序列分类的一维卷积神经网络

本节讨论使用一维卷积神经网络学习从变长序列到定长输出的映射，即形式为 $ f_{\theta} : \mathbb{R}^{DT} \to \mathbb{R}^C $ 的函数，其中 $ T $ 为输入长度， $ D $ 为每个输入的特征数， $ C $ 为输出向量的大小（例如，类别 logits）。

一维序列上应用的基本一维卷积操作如图 Figure 14.4 所示。通常，输入序列会有 $D > 1$ 个输入通道（特征维度）。在这种情况下，我们可以分别对每个通道进行卷积，然后将结果相加，对每个输入通道使用不同的一维滤波器（核）得到 $z_i = \sum_d \mathbf{x}_{i-k:i+k,d}^\top \mathbf{w}_d$，其中 $k$ 是一维感受野的大小，$\mathbf{w}_d$ 是输入通道 $d$ 的滤波器。这产生了一个一维向量 $\mathbf{z} \in \mathbb{R}^T$，编码了输入（忽略边界效应）。我们可以通过对每个输出通道 $c$ 使用不同的权重向量，为每个位置创建一个向量表示，得到 $z_{ic} = \sum_d \mathbf{x}_{i-k:i+k,d}^\top \mathbf{w}_{d,c}$。这实现了从 $TD$ 到 $TC$ 的映射。为了将其缩减为固定大小的向量 $z \in \mathbb{R}^C$，我们可以使用时间维度的最大池化得到 $z_c = \max_i z_{ic}$。我们可以

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_250_130_890_587.jpg" alt="图片" width="55%" /></div>

<div style="text-align: center;">图15.14：TextCNN模型在二元情感分类中的示意图。改编自文献[Zha+20]的图15.3.5。</div>

然后将结果传入softmax层。

在[Kim14]中，他们将此模型应用于序列分类。其思想是使用嵌入层对每个单词进行嵌入，然后使用不同宽度的一维核计算各种特征，以捕获不同长度尺度的模式。之后对时间维度进行最大池化，拼接结果，并传入全连接层。图15.14给出了示意图，代码见`cnn1d_sentiment_jax.ipynb`。

#### 15.3.2 用于序列生成的因果一维CNN

在生成式场景中使用一维CNN时，必须将其转换为因果CNN，其中每个输出变量仅依赖于先前生成的变量（这也称为卷积马尔可夫模型）。具体而言，我们将模型定义如下：

$$  p(\boldsymbol{y})=\prod_{t=1}^{T}p(y_{t}|\boldsymbol{y}_{1:t-1})=\prod_{t=1}^{T}Cat(y_{t}|softmax(\varphi(\sum_{\tau=1}^{t-k}\boldsymbol{w}^{\mathsf{T}}\boldsymbol{y}_{\tau:\tau+k})))   \tag*{(15.33)}$$

其中$\boldsymbol{w}$是大小为$k$的卷积滤波器，为简化符号，我们假设使用单个非线性函数$\varphi$和分类输出。这类似于常规的一维卷积，不同之处在于我们“屏蔽”了未来输入，使得$y_t$仅依赖于过去的值，而非过去和未来的值。这是

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_277_135_898_341.jpg" alt="图像" width="53%" /></div>


<div style="text-align: center;">图 15.15: 使用膨胀（空洞）卷积的 WaveNet 模型示意图，膨胀因子分别为 1、2、4 和 8。摘自 [Oor+16] 的图 3，经 Aaron van den Oord 许可使用。</div>


这被称为因果卷积。我们当然可以使用更深的模型，并且可以以输入特征 x 为条件。

为了捕捉长距离依赖关系，我们可以使用膨胀卷积（第 14.4.1 节），如图 15.15 所示。该模型已成功用于创建先进的文本到语音合成系统，即 WaveNet [Oor+16]。具体来说，他们堆叠了 10 个因果一维卷积层，膨胀率分别为 1, 2, 4, ..., 256, 512，从而得到一个有效感受野为 1024 的卷积块（他们在每层之前对输入序列进行左侧填充，填充的零的数量等于膨胀率，因此每层长度相同）。然后他们将这个块重复 3 次以计算更深层的特征。

在 WaveNet 中，条件信息 x 是一组从输入单词序列中导出的语言特征；该模型随后使用上述模型生成原始音频。也可以创建一种完全端到端的方法，该方法从原始单词而非语言特征开始（参见 [Wan+17]）。

尽管 WaveNet 能生成高质量的语音，但其速度太慢，无法用于生产系统。不过，它可以被“蒸馏”成并行生成模型 [Oor+18]。我们将在本书的续篇 [Mur23] 中讨论这类并行生成模型。

### 15.4 注意力机制

到目前为止，在我们考虑的所有神经网络中，隐藏激活都是输入激活的线性组合，随后是非线性变换： $ \mathbf{Z} = \varphi(\mathbf{X}\mathbf{W}) $，其中 $ \mathbf{X} \in \mathbb{R}^{m \times v} $ 是隐藏特征向量，$ \mathbf{W} \in \mathbb{R}^{v \times v'} $ 是在训练集上学习得到的一组固定权重，用于产生输出 $ \mathbf{Z} \in \mathbb{R}^{m \times v'} $。

然而，我们可以想象一种更灵活的模型，其中权重依赖于输入，即 $ \mathbf{Z} = \varphi(\mathbf{X}\mathbf{W}(\mathbf{X})) $。这种乘法交互被称为**注意力机制**。更一般地，我们可以写作 $ \mathbf{Z} = \varphi(\mathbf{V}\mathbf{W}(\mathbf{Q},\mathbf{K})) $，其中 $ \mathbf{Q} \in \mathbb{R}^{m \times q} $ 是一组查询（从 $ \mathbf{X} $ 导出），用于描述每个输入在“寻找”什么；$ \mathbf{K} \in \mathbb{R}^{m \times q} $ 是一组键（从 $ \mathbf{X} $ 导出），用于描述每个输入向量包含什么；$ \mathbf{V} \in \mathbb{R}^{m \times v} $ 是一组值（从 $ \mathbf{X} $ 导出），用于描述每个输入应如何传递到输出。我们通常通过输入的线性投影来计算这些量：$ \mathbf{Q} = \mathbf{W}_q\mathbf{X} $、$ \mathbf{K} = \mathbf{W}_k\mathbf{X} $ 和 $ \mathbf{V} = \mathbf{W}_v\mathbf{X} $。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_314_121_858_405.jpg" alt="Image" width="47%" /></div>

<div style="text-align: center;">图 15.16：注意力机制计算一组值的加权平均，其中权重通过将查询向量与一组键进行比较而得到。来自 [$Zha+20$] 的图 10.3.1。经 Aston Zhang 友好许可使用。</div>

当使用注意力计算输出 $z_j$ 时，我们使用其对应的查询 $q_j$，并将其与每个键 $\mathbf{k}_i$ 进行比较，得到一个相似度分数 $0 \leq \alpha_{ij} \leq 1$，其中 $\sum_i \alpha_{ij} = 1$；然后我们设置 $z_j = \sum_i \alpha_{ij} \mathbf{v}_i$。（我们假设 $\varphi(u) = u$ 是恒等函数。）例如，假设 $\mathbf{V} = \mathbf{X}$，且查询 $q_j$ 同等匹配键 1 和 2，因此 $\alpha_{1j} = \alpha_{2j} = 0.5$；那么我们有 $z_j = 0.5\mathbf{x}_1 + 0.5\mathbf{x}_2$。因此输出变成了输入的动态加权组合，而不是固定的加权组合。而且我们不是学习权重矩阵，而是学习投影矩阵 $\mathbf{W}_q$、$\mathbf{W}_k$ 和 $\mathbf{W}_v$。下面我们将更详细地解释这一点。

注意，注意力最初是为自然语言序列模型开发的。然而，如今它被应用于各种模型，包括视觉模型。我们在以下章节中的阐述基于 [$Zha+20$，第 10 章]。

#### 15.4.1 注意力作为软字典查找

我们将关注单个输出向量及其对应的查询向量 $\boldsymbol{q}$。我们可以将注意力视为一种字典查找，其中我们将查询 $\boldsymbol{q}$ 与每个键 $\boldsymbol{k}_{i}$ 进行比较，然后检索相应的值 $\boldsymbol{v}_{i}$。为了使这种查找操作可微，我们不检索单个值 $\boldsymbol{v}_{i}$，而是计算这些值的凸组合，如下所示：

$$ \mathrm{Attn}(\boldsymbol{q},(\boldsymbol{k}_{1},\boldsymbol{v}_{1}),\ldots,(\boldsymbol{k}_{m},\boldsymbol{v}_{m}))=\mathrm{Attn}(\boldsymbol{q},(\boldsymbol{k}_{1:m},\boldsymbol{v}_{1:m}))=\sum_{i=1}^{m}\alpha_{i}(\boldsymbol{q},\boldsymbol{k}_{1:m})\boldsymbol{v}_{i}\in\mathbb{R}^{v} \tag*{(15.34)}$$

其中 $\alpha_i(q, k_{1:m})$ 是第 $i$ 个注意力权重；这些权重满足对于每个 $i$ 有 $0 \leq \alpha_i(q, k_{1:m}) \leq 1$，且 $\sum_i \alpha_i(q, k_{1:m}) = 1$。

注意力权重可以通过一个*注意力***分数**函数 $a(q, k_i) \in \mathbb{R}$ 来计算，该函数计算查询 $q$ 与键 $k_i$ 的相似度。我们将在下面讨论几种这样的分数函数。给定分数后，我们可以使用 softmax 函数计算注意力权重：

$$ \alpha_{i}(\boldsymbol{q},\boldsymbol{k}_{1:m})=softmax_{i}([a(\boldsymbol{q},\boldsymbol{k}_{1}),\cdots,a(\boldsymbol{q},\boldsymbol{k}_{m})])=\frac{\exp(a(\boldsymbol{q},\boldsymbol{k}_{i}))}{\sum_{j=1}^{m}\exp(a(\boldsymbol{q},\boldsymbol{k}_{j}))} \tag*{(15.35)}$$

作者：Kevin P. Murphy。 (C) MIT Press。CC-BY-NC-ND 许可。

---

见图15.16的示意图。

在某些情况下，我们希望将注意力限制在字典的子集上，即仅关注有效条目。例如，我们可能希望将序列填充到固定长度（以实现高效的小批量处理），此时应“掩蔽”掉填充位置。这被称为**掩蔽注意力**。我们可以通过将被掩蔽条目的注意力分数设置为一个很大的负数（如 $ -10^{6} $）来高效实现，这样对应的softmax权重将为0（这类似于第15.3.2节讨论的因果卷积）。

#### 15.4.2 核回归作为非参数注意力

我们可以从核回归的角度理解注意力机制，核回归是一种非参数模型，我们将在第16.3.5节讨论。简而言之，该模型在查询点 $\boldsymbol{x}$ 处的预测输出是所有目标标签 $y_i$ 的加权组合，权重取决于查询点 $\boldsymbol{x}$ 与每个训练点 $\boldsymbol{x}_i$ 的相似度：

$$  f(\boldsymbol{x})=\sum_{i=1}^{n}\alpha_{i}(\boldsymbol{x},\boldsymbol{x}_{1:n})y_{i}   \tag*{(15.36)}$$

其中 $\alpha_i(\boldsymbol{x}, \boldsymbol{x}_{1:n}) \geq 0$ 衡量测试输入 $\boldsymbol{x}$ 与训练输入 $\boldsymbol{x}_i$ 的归一化相似度。该相似度度量通常通过使用密度核（如高斯核）定义注意力分数来计算：

$$  \mathcal{K}_{\sigma}(u)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{1}{2\sigma^{2}}u^{2}}   \tag*{(15.37)}$$

其中 $\sigma$ 称为带宽。然后我们定义 $a(x, x_i) = K_\sigma(x - x_i)$。

由于分数经过归一化处理，我们可以去掉 $\frac{1}{\sqrt{2\pi\sigma^2}}$ 项。此外，我们用 $\beta^2 = 1/\sigma^2$ 重写核函数，得到：

$$  \mathcal{K}(u;\beta)=\exp(-\frac{\beta^{2}}{2}u^{2})   \tag*{(15.38)}$$

将其代入方程 $ (15.36) $，得到：

$$  f(\boldsymbol{x})=\sum_{i=1}^{n}\alpha_{i}(\boldsymbol{x},\boldsymbol{x}_{1:n})y_{i}   \tag*{(15.39)}$$

$$  =\sum_{i=1}^{n}\frac{\exp[-\frac{1}{2}((\boldsymbol{x}-\boldsymbol{x}_{i})\boldsymbol{\beta})^{2}]}{\sum_{j=1}^{n}\exp[-\frac{1}{2}((\boldsymbol{x}-\boldsymbol{x}_{j})\boldsymbol{\beta})^{2}]}y_{i}   \tag*{(15.40)}$$

$$  =\sum_{i=1}^{n}\mathrm{softmax}_{i}\left[-\frac{1}{2}((\boldsymbol{x}-\boldsymbol{x}_{1})\boldsymbol{\beta})^{2},\cdots,-\frac{1}{2}((\boldsymbol{x}-\boldsymbol{x}_{n})\boldsymbol{\beta})^{2}\right]y_{i}   \tag*{(15.41)}$$

我们可以将其解释为一种**非参数注意力**形式，其中查询是测试点 $\boldsymbol{x}$，键是训练输入 $\boldsymbol{x}_i$，值是训练标签 $y_i$。如果令 $\beta = 1$，则对于测试输入 $j$，得到的注意力矩阵 $A_{ji} = \alpha_i(\boldsymbol{x}_j, \boldsymbol{x}_{1:n})$ 如图15.17a所示。最终的预测曲线如图15.17b所示。

图15.17a中对角带的大小（即注意力机制的稀疏性）取决于参数 $\beta$。如果增大 $\beta$（相当于减小核带宽），对角带会变窄，但模型将开始过拟合。