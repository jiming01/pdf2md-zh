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

<div style="text-align: center;"><img src="imgs/img_in_chart_box_272_150_495_333.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_634_138_918_340.jpg" alt="图像" width="24%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图15.17：一维核回归。(a) 核权重矩阵。(b) 在密集测试点网格上的预测结果。由kernel regression attention.ipynb生成。</div>


#### 15.4.3 参数化注意力

在15.4.2节中，我们使用高斯核定义了注意力分数，将查询（测试点）与训练集中的每个值进行比较。然而，非参数方法无法很好地扩展到大规模训练集或高维输入。因此，我们将转向参数模型，其中我们有一组固定的键和值，并在学习到的嵌入空间中比较查询和键。

有几种实现方式。一般情况下，查询 $ q \in \mathbb{R}^q $ 和键 $ k \in \mathbb{R}^k $ 可能具有不同大小。为了比较它们，我们可以通过计算 $ \mathbf{W}_q q $ 和 $ \mathbf{W}_k k $ 将它们映射到大小为 $ h $ 的公共嵌入空间，其中 $ \mathbf{W}_q \in \mathbb{R}^{h \times q} $ 和 $ \mathbf{W}_k \in \mathbb{R}^{h \times k} $。然后，将这些输入到 MLP 中，得到以下加性注意力评分函数：

$$  a(\boldsymbol{q},\boldsymbol{k})=\boldsymbol{w}_{v}^{\mathsf{T}}\operatorname{t a n h}(\mathbf{W}_{q}\boldsymbol{q}+\mathbf{W}_{k}\boldsymbol{k})\in\mathbb{R}   \tag*{(15.42)}$$

一种计算效率更高的方法是假设查询和键都具有长度 $d$，因此我们可以直接计算 $q^\top k$。如果假设这些是均值为0、方差为1的独立随机变量，则它们内积的均值为0，方差为 $d$（这由公式(2.34)和公式(2.39)得出）。为确保内积的方差不随输入大小而变化，通常除以 $\sqrt{d}$。这就产生了缩放点积注意力：

$$  a(\boldsymbol{q},\boldsymbol{k})=\boldsymbol{q}^{\top}\boldsymbol{k}/\sqrt{d}\in\mathbb{R}   \tag*{(15.43)}$$

在实践中，我们通常一次处理 $n$ 个向量的迷你批次。设相应的查询、键和值矩阵分别为 $\mathbf{Q} \in \mathbb{R}^{n \times d}$、$\mathbf{K} \in \mathbb{R}^{m \times d}$、$\mathbf{V} \in \mathbb{R}^{m \times v}$。则我们可以按如下方式计算注意力加权输出：

$$  \mathrm{Attn}(\mathbf{Q},\mathbf{K},\mathbf{V})=\mathrm{softmax}(\frac{\mathbf{Q}\mathbf{K}^{\top}}{\sqrt{d}})\mathbf{V}\in\mathbb{R}^{n\times v}   \tag*{(15.44)}$$

其中 softmax 函数按行应用。请参考 attention_jax.ipynb 中的示例代码。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_397_125_774_401.jpg" alt="图" width="32%" /></div>

<div style="text-align: center;">图15.18：带有注意力机制的 seq2seq 模型用于英法翻译的示意图。经 Minh-Thang Luong 善意许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_287_496_476_711.jpg" alt="图" width="16%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_684_497_897_711.jpg" alt="图" width="18%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图15.19：将两个句子从西班牙语翻译成英语时生成的注意力热力图示意图。(a) 输入为“hace mucho frio aqui.”，输出为“it is very cold here.”。(b) 输入为“¿todavia estan en casa?”，输出为“are you still at home?”。注意，在生成输出词“home”时，模型应关注输入词“casa”，但实际上似乎关注了输入词“?”。改编自 https://www.tensorflow.org/tutorials/text/nmt_with_attention。</div>

#### 15.4.4 带注意力的 Seq2Seq 模型

回顾第15.2.3节中的 seq2seq 模型。该模型使用形式为 $ \boldsymbol{h}_t^d = f_d(\boldsymbol{h}_{t-1}^d, \boldsymbol{y}_{t-1}, \boldsymbol{c}) $ 的 RNN 解码器，其中 $ \boldsymbol{c} $ 是一个固定长度的上下文向量，表示输入 $ \boldsymbol{x}_{1:T} $ 的编码。通常我们设 $ \boldsymbol{c} = \boldsymbol{h}_T^e $，即编码器 RNN 的最终状态（或者使用带平均池化的双向 RNN）。然而，对于机器翻译等任务，这可能导致性能不佳，因为输出无法直接访问输入词本身。我们可以通过允许输出词直接“查看”输入词来避免这一瓶颈。但应该查看哪些输入呢？毕竟，词序在不同语言中并不总是保持不变的（例如，德语经常将动词放在句子末尾），因此我们需要推断源语言和目标语言之间的对齐关系。

我们可以通过使用（软）**注意力机制**以可微分的方式解决这个问题，该机制最初由 $ [BCB15; LPM15] $ 提出。具体来说，我们可以用

---

动态上下文向量 $\pmb{c}_{t}$ 的计算方式如下：

$$  \boldsymbol{c}_{t}=\sum_{i=1}^{T}\alpha_{i}(\boldsymbol{h}_{t-1}^{d},\boldsymbol{h}_{1:T}^{e})\boldsymbol{h}_{i}^{e}   \tag*{(15.45)}$$

这里使用了注意力机制，其中查询是解码器上一时刻的隐藏状态 $h_{t-1}^{d}$，键是编码器的所有隐藏状态，值也是编码器的所有隐藏状态。（当RNN具有多个隐藏层时，通常取编码器的顶层作为键和值，解码器的顶层作为查询。）该上下文向量与解码器的输入向量 $y_{t-1}$ 拼接后，连同前一隐藏状态 $h_{t-1}^{d}$ 一起输入解码器，从而生成 $h_{t}^{d}$。整体模型见图 Figure 15.18。

我们可以按照常规方式在句子对上训练该模型，并用于执行机器翻译。（示例代码见 nmt_attention_jax.ipynb。）我们还可以可视化解码每一步计算出的注意力权重，以了解模型认为输入中哪些部分对生成对应输出最为相关。一些示例如图 Figure 15.19 所示。

#### 15.4.5 带注意力的 Seq2vec（文本分类）

我们也可以将注意力用于序列分类器。例如 [Raj+18] 将 RNN 分类器应用于预测患者是否死亡的场景。输入是一组电子健康记录，这是一个包含结构化数据以及非结构化文本（临床笔记）的时间序列。注意力有助于识别输入中的“相关”部分，如图 Figure 15.20 所示。

#### 15.4.6 带注意力的 Seq+Seq2Vec（文本对分类）

假设我们看到句子“一个人骑在马上跳过一根木头”（称为前提），随后读到“一个人在户外骑马”（称为假设）。我们有理由认为前提蕴含假设，即给定前提时假设更有可能成立。$^{3}$ 现在假设假设是“一个人在一家小餐馆里点了一份煎蛋卷”。在这种情况下，我们会说前提与假设矛盾，因为给定前提时假设不太可能成立。最后，假设假设是“一个人正在训练他的马参加比赛”。此时，前提与假设之间的关系是中性的，因为假设可能成立也可能不成立。将句子对分类为这三类别的任务称为文本蕴涵或“自然语言推理”。该领域的标准基准是斯坦福自然语言推理（SNLI）语料库 [Bow+15]，包含 550,000 个标注句子对。

[Par+16a] 提出了一种针对此分类问题的有趣解决方案；在当时，它在 SNLI 数据集上达到了最前沿的水平。整体方法如图 Figure 15.21 所示。设 $\mathbf{A} = (\mathbf{a}_1, \ldots, \mathbf{a}_m)$ 为前提，$\mathbf{B} = (\mathbf{b}_1, \ldots, \mathbf{b}_n)$ 为假设，其中 $\mathbf{a}_i, \mathbf{b}_j \in \mathbb{R}^E$ 是单词的嵌入向量。该模型包含三个步骤。首先，前提中的每个词 $\mathbf{a}_i$ 会

---

<div style="text-align: center;">患者时间线</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_177_148_984_684.jpg" alt="图像" width="70%" /></div>

<div style="text-align: center;">图15.20：电子健康记录示例。本例中，入院后24小时，RNN分类器预测死亡风险为19.9%；患者最终在入院后10天死亡。输入临床记录中的“相关”关键词（由注意力机制识别）以红色显示。摘自 [Raj+18] 的图3。经 Alvin Rajkomar 许可使用。</div>

对于假设中的每个单词 $ \pmb{b}_{j} $，我们计算一个注意力权重

$$  e_{ij}=f(\boldsymbol{a}_{i})^{\top}f(\boldsymbol{b}_{j})   \tag*{(15.46)}$$

其中 $ f : \mathbb{R}^E \to \mathbb{R}^D $ 是一个MLP；然后我们计算假设中匹配单词的加权平均，

$$  \beta_{i}=\sum_{j=1}^{n}\frac{\exp(e_{ij})}{\sum_{k=1}^{n}\exp(e_{ik})}b_{j}   \tag*{(15.47)}$$

接下来，我们通过使用MLP $ g : \mathbb{R}^{2E} \to \mathbb{R}^H $ 将它们拼接的结果映射到一个隐藏空间中来比较 $ a_i $ 和 $ \beta_i $：

$$  \boldsymbol{v}_{A,i}=g([\boldsymbol{a}_{i},\boldsymbol{\beta}_{i}]),i=1,\ldots,m   \tag*{(15.48)}$$

《概率机器学习：导论》。在线版本。2024年11月23日。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_309_115_852_403.jpg" alt="图" width="47%" /></div>


<div style="text-align: center;">图 15.21：使用带有注意力机制的 MLP 进行句子对蕴含分类的示意图，其中前提（“I do need sleep”）与假设（“I am tired”）对齐。白色方块表示激活的注意力权重，蓝色方块表示未激活。（为简化起见，我们假设使用硬 0/1 注意力。）摘自 [Zha+20] 的图 15.5.2。经 Aston Zhang 许可使用。</div>


最后，我们对所有比较结果进行聚合，得到前提相对于假设的整体相似度：

$$  v_{A}=\sum_{i=1}^{m}v_{A,i}   \tag*{(15.49)}$$

类似地，我们可以将假设与前提进行比较，使用：

$$  \alpha_{j}=\sum_{i=1}^{m}\frac{\exp(e_{ij})}{\sum_{k=1}^{m}\exp(e_{kj})}a_{i}   \tag*{(15.50)}$$

$$  \boldsymbol{v}_{B,j}=g([\boldsymbol{b}_{j},\boldsymbol{\alpha}_{j}]),j=1,\ldots,n   \tag*{(15.51)}$$

$$  \boldsymbol{v}_{B}=\sum_{j=1}^{n}\boldsymbol{v}_{B,j}   \tag*{(15.52)}$$

最后，我们使用另一个 MLP $ h : \mathbb{R}^{2H} \to \mathbb{R}^3 $ 对输出进行分类：

$$  \hat{y}=h([\boldsymbol{v}_{A},\boldsymbol{v}_{B}])   \tag*{(15.53)}$$

请参见 `entailment_attention_mlp_jax.ipynb` 获取一些示例代码。

我们可以修改此模型，以学习从句子对到输出标签的其他类型的映射。例如，在 **语义文本相似度** 任务中，目标是预测两个输入句子在语义上的相关程度。一个标准数据集是 STS **基准** [Cer+17]，其中相关度范围从 0（不相关）到 5（最大相关）。

#### 15.4.7 软注意力与硬注意力

如果强制注意力热图稀疏化，使得每个输出只能关注一个输入位置，而不是所有位置的加权组合，则该方法称为硬注意力。我们

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_222_124_954_336.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 15.22：使用注意力机制的图像描述。(a) 软注意力。生成“a woman is throwing a frisbee in a park”。(b) 硬注意力。生成“a man and a woman playing frisbee in a field”。摘自 [Xu+15] 的图 6，经 Kelvin Xu 许可使用。</div>


比较图 15.22 中这两种方法在图像描述问题上的表现。遗憾的是，硬注意力会导致不可微的训练目标，需要借助强化学习等方法才能拟合模型。详见 [Xu+15]。

从上述示例来看，这些注意力热图似乎能够“解释”模型为何生成某个特定输出。然而，注意力的可解释性仍存在争议（相关讨论参见 e.g., [JW19; WP19; SS19; Bru+19]）。

### 15.5 Transformer 模型

Transformer 模型 $[Vas+17]$ 是一种 seq2seq 模型，在编码器和解码器中均使用注意力机制，从而消除了对 RNN 的需求，下文将对此进行解释。Transformer 已被广泛应用于许多（条件）序列生成任务，例如机器翻译 $[Vas+17]$、成分句法分析 $[Vas+17]$、音乐生成 $[Hua+18]$、蛋白质序列生成 $[Mad+20; Cho+20b]$、抽象式文本摘要 $[Zha+19a]$、图像生成 $[Par+18]$（将图像视为光栅化的 1D 序列）等。

Transformer 是一个相当复杂的模型，使用了多种新型构建模块或层。下面我们介绍这些新模块，然后讨论如何将它们组合起来。$^{4}$

#### 15.5.1 自注意力

在第 15.4.4 节中，我们展示了 RNN 的解码器如何通过对输入序列使用注意力来获取每个输入的上下文嵌入。然而，我们可以修改模型，让编码器对自身进行注意力机制，而不是解码器对编码器进行注意力。这称为自注意力 (self-attention) [CDL16; Par+16b]。

具体来说，给定输入 token 序列 $\mathbf{x}_1, \ldots, \mathbf{x}_n$，其中 $\mathbf{x}_i \in \mathbb{R}^d$，自注意力可以通过下式生成相同大小的输出序列：

$$ y_{i}=\mathrm{Attn}(x_{i},(x_{1},x_{1}),\ldots,(x_{n},x_{n}))   \tag*{(15.54)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_333_129_834_325.jpg" alt="Image" width="43%" /></div>


<div style="text-align: center;">图15.23：对于单词“it”，编码器自注意力的表示如何根据输入上下文而不同的说明。来自 https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html。经Jakob Uszkoreit许可使用。</div>


其中查询为 x，键和值均为所有（有效的）输入 x1, …, xn。

要在解码器中使用该机制，可令 $ \boldsymbol{x}_{i} = \boldsymbol{y}_{i-1} $ 且 $ n = i - 1 $，这样所有先前生成的输出都可用。在训练时，所有输出已知，因此可以并行求值上述函数，克服了使用RNN时的序列瓶颈。

除了速度提升，自注意力还能给出更好的上下文表示。例如，考虑将英文句子“The animal didn't cross the street because it was too tired”（动物没有过马路，因为它太累了）和“The animal didn't cross the street because it was too wide”（动物没有过马路，因为它太宽了）翻译成法语。为了生成正确性别的法语代词，需要知道“it”指代什么（这称为**指代消解**）。第一种情况中，“it”指动物；第二种情况中，“it”指街道。

图15.23展示了应用于英文句子的自注意力如何解决这种歧义。在第一个句子中，“it”的表示依赖于前面“animal”的表示；而在第二个句子中，则依赖于前面“street”的表示。

#### 15.5.2 多头注意力

如果将注意力矩阵视为类似核矩阵（如第15.4.2节所述），那么自然地希望使用多个注意力矩阵以捕获不同的相似性概念。这就是**多头注意力**（MHA）的基本思想。更详细地，给定查询 $ q \in \mathbb{R}^{d_q} $、键 $ \boldsymbol{k}_j \in \mathbb{R}^{d_k} $ 和值 $ \boldsymbol{v}_j \in \mathbb{R}^{d_v} $，定义第 $ i $ 个注意力头为

$$  \boldsymbol{h}_{i}=\operatorname{Attn}(\mathbf{W}_{i}^{(q)}\boldsymbol{q},\{\mathbf{W}_{i}^{(k)}\boldsymbol{k}_{j},\mathbf{W}_{i}^{(v)}\boldsymbol{v}_{j}\})\in\mathbb{R}^{p_{v}}   \tag*{(15.55)}$$

其中 $ \mathbf{W}_i^{(q)} \in \mathbb{R}^{p_q \times d_q} $、$ \mathbf{W}_i^{(k)} \in \mathbb{R}^{p_k \times d_k} $ 和 $ \mathbf{W}_i^{(v)} \in \mathbb{R}^{p_v \times d_v} $ 为投影矩阵。然后将 $ h $ 个头堆叠起来，并使用下式投影到 $ \mathbb{R}^{p_o} $：

$$  \boldsymbol{h}=\mathrm{MHA}(\boldsymbol{q},\{\boldsymbol{k}_{j},\boldsymbol{v}_{j}\})=\boldsymbol{W}_{o}\begin{pmatrix}\boldsymbol{h}_{1}\\ \vdots\\ \boldsymbol{h}_{h}\end{pmatrix}\in\mathbb{R}^{p_{o}}   \tag*{(15.56)}$$

其中 $ \boldsymbol{h}_i $ 由公式(15.55)定义，$ \mathbf{W}_o \in \mathbb{R}^{p_o \times h_{p_v}} $。若设置 $ p_q h = p_k h = p_v h = p_o $，则可并行计算所有输出头。示例代码见 multi_head_attention_jax.ipynb。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_345_128_826_397.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 15.24：多头注意力。改编自 [Zha+20] 中的图 9.3.3。</div>


代码。

#### 15.5.3 位置编码

“普通”自注意力的性能可能较低，因为注意力是排列不变的，因此忽略了输入词的顺序。为了克服这一点，我们可以将词嵌入与位置嵌入拼接起来，从而使模型知道单词出现的顺序。

一种方法是将每个位置表示为一个整数。然而，神经网络无法原生处理整数。为了解决这个问题，我们可以将整数编码为二进制形式。例如，假设序列长度为 n = 3，我们得到以下 d = 3 维的每个位置的位向量序列：000, 001, 010, 011, 100, 101, 110, 111。我们可以看到，最右边的索引变化最快（频率最高），而最左边的索引（最高有效位）变化最慢。（当然，我们可以改变这一点，使最左边的位变化最快。）我们可以将其表示为一个位置矩阵 $\mathbf{P} \in \mathbb{R}^{n \times d}$。

我们可以将上述表示视为使用一组基函数（对应于 2 的幂次），其系数为 0 或 1。通过使用一组不同的基函数和实数权重，我们可以获得更紧凑的编码。[Vas+17] 提出使用正弦基，如下所示：

$$ p_{i,2j}=\sin\left(\frac{i}{C^{2j/d}}\right), p_{i,2j+1}=\cos\left(\frac{i}{C^{2j/d}}\right), \tag*{(15.57)}$$

其中 $C = 10,000$ 对应于某个最大序列长度。例如，如果 $d = 4$，则第 $i$ 行为

$$ p_{i}=[\sin(\frac{i}{C^{0/4}}),\cos(\frac{i}{C^{0/4}}),\sin(\frac{i}{C^{2/4}}),\cos(\frac{i}{C^{2/4}})] \tag*{(15.58)}$$

图 15.25a 显示了 n = 60 和 d = 32 时的对应位置矩阵。在这种情况下，最左边的列变化最快。我们看到每一行都有一个实值“指纹”来表示其在序列中的位置。图 15.25b 显示了维度 6 到 9 的某些基函数（列向量）。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_189_139_345_334.jpg" alt="图像" width="13%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_445_142_893_342.jpg" alt="图像" width="38%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 15.25: (a) 长度为 n = 60、嵌入维度为 d = 32 的序列的位置编码矩阵。(b) 第 6 到第 9 列对应的基函数。由 positional_encoding_jax.ipynb 生成。</div>

这种表示方法的优势有两点。首先，它可以针对任意长度的输入（不超过 $T \leq C$）进行计算，这与从整数到向量的学习映射不同。其次，给定任意两个位置的相对距离，其中一个位置的表示可以通过另一个位置的线性变换得到。具体而言，我们有 $\boldsymbol{p}_{t+\phi} = f(\boldsymbol{p}_t)$，其中 $f$ 是一个线性变换。为了说明这一点，注意：

$$  \begin{pmatrix}\sin(\omega_{k}(t+\phi))\\\cos(\omega_{k}(t+\phi))\end{pmatrix}=\begin{pmatrix}\sin(\omega_{k}t)\cos(\omega_{k}\phi)+\cos(\omega_{k}t)\sin(\omega_{k}\phi)\\\cos(\omega_{k}t)\cos(\omega_{k}\phi)-\sin(\omega_{k}t)\sin(\omega_{k}\phi)\end{pmatrix}   \tag*{(15.59)}$$

$$ \left\langle\cos(\omega_{k}(t+\phi))\right\rangle=\left\langle\cos(\omega_{k}t)\cos(\omega_{k}\phi)-\sin(\omega t)\sin(\omega_{k}\phi)\right\rangle $$ 

$$  \begin{aligned}=\begin{pmatrix}\cos(\omega_{k}\phi)&\sin(\omega_{k}\phi)\\-\sin(\omega_{k}\phi)&\cos(\omega_{k}\phi)\end{pmatrix}\begin{pmatrix}\sin(\omega_{k}t)\\\cos(\omega_{k}t)\end{pmatrix}\end{aligned}   \tag*{(15.60)}$$

因此，若 $\phi$ 很小，则 $p_{t+\phi} \approx p_{t}$。这提供了一种有用的归纳偏置形式。

一旦我们计算出位置嵌入 $\mathbf{P}$，就需要使用以下方式将其与原始词嵌入 $\mathbf{X}$ 结合：$^{5}$

$$   POS(Embed(\mathbf{X}))=\mathbf{X}+\mathbf{P}.   \tag*{(15.61)}$$

#### 15.5.4 整合所有组件

Transformer 是一种 seq2seq 模型，其编码器和解码器使用自注意力机制而非 RNN。编码器由一系列编码器块组成，每个块均采用多头注意力（第 15.5.2 节）、残差连接（第 13.4.4 节）、前馈层（第 13.2 节）和层归一化（第 14.2.4.2 节）。更精确地说，编码器块可定义如下：

def EncoderBlock(X):
    Z = LayerNorm(MultiHeadAttn(Q=X, K=X, V=X) + X)
    E = LayerNorm(FeedForward(Z) + Z)
    return E

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_161_134_1016_616.jpg" alt="Image" width="74%" /></div>

<div style="text-align: center;">图 15.26: Transformer。摘自 [Wen18]。经 Lilian Weng 许可使用。改编自 [Vas+17] 的图 1–2。</div>

注意，MHA 层在序列维度上融合信息，而前馈层则在每个位置并行地沿维度方向融合信息。（大型 Transformer 模型的大部分参数都存储在这些 MLP 中，且有推测认为这是大多数“世界知识”的所在之处 [Men+22]。）层归一化可以在模块之后应用（即 $ z = \text{LN}(\text{module}(\boldsymbol{x}) + \boldsymbol{x}) $）或之前应用（即 $ z = \text{module}(\text{LN}(\boldsymbol{x}) + \boldsymbol{x}) $）；这两种方式分别称为后归一化和前归一化。

整体编码器通过将位置编码应用于输入序列的嵌入，然后重复 N 个编码器块（其中 N 控制块的深度）来定义：

def Encoder(X, N):

E = POS(Embed(X))

for n in range(N):

E = EncoderBlock(E)

return E

图 15.26 的左侧对此进行了示意。

解码器的结构则稍显复杂。它通过另一个多头注意力模块来访问编码器。同时，它也能访问之前生成的输出：这些输出经过移位后，与位置嵌入相结合，然后送入一个带掩码（因果）的多头注意力模型。最后，计算每个位置上的词符输出分布。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>层类型</td><td style='text-align: center; word-wrap: break-word;'>复杂度</td><td style='text-align: center; word-wrap: break-word;'>序列操作数</td><td style='text-align: center; word-wrap: break-word;'>最大路径长度</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>自注意力</td><td style='text-align: center; word-wrap: break-word;'>$ O(n^{2}d) $</td><td style='text-align: center; word-wrap: break-word;'>$ O(1) $</td><td style='text-align: center; word-wrap: break-word;'>$ O(1) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>循环</td><td style='text-align: center; word-wrap: break-word;'>$ O(nd^{2}) $</td><td style='text-align: center; word-wrap: break-word;'>$ O(n) $</td><td style='text-align: center; word-wrap: break-word;'>$ O(n) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>卷积</td><td style='text-align: center; word-wrap: break-word;'>$ O(knd^{2}) $</td><td style='text-align: center; word-wrap: break-word;'>$ O(1) $</td><td style='text-align: center; word-wrap: break-word;'>$ O(\log_{k} n) $</td></tr></table>

<div style="text-align: center;">表 15.1：Transformer 与其他神经序列生成模型的比较。其中 n 为序列长度，d 为输入特征的维度，k 为卷积的核大小。基于 [Vas+17] 的表 1。</div>

并行处理。

更详细地，解码器块定义如下：

def DecoderBlock(Y, E):
    Z = LayerNorm(MultiHeadAttn(Q=Y, K=Y, V=Y) + Y)
    Z' = LayerNorm(MultiHeadAttn(Q=Z, K=E, V=E) + Z)
    D = LayerNorm(FeedForward(Z') + Z')
    return D

整个解码器由 N 个解码器块重复构成：

def Decoder(Y, E, N):
    D = POS(Embed(Y))
    for n in range(N):
        D = DecoderBlock(D, E)
    return D

如图 15.26 右半部分所示。

在训练阶段，解码器的所有输入 Y 都是预先已知的，因为它们来源于对滞后目标输出序列的嵌入。在推理（测试）阶段，我们需要顺序解码，并使用掩码注意力机制，将生成的输出馈入嵌入层，并添加到可被注意的键/值集合中。（初始化时，我们输入序列开始标记。）参见 transformers_jax.ipynb 的示例代码，以及 [Rus18; Ala18] 关于此模型的详细教程。

#### 15.5.5 Transformer、CNN 和 RNN 的比较

图 15.27 直观比较了三种将序列 $ \pmb{x}_{1:n} $ 映射到另一序列 $ \pmb{y}_{1:n} $ 的不同架构：一维 CNN、RNN 和基于注意力的模型。每种模型在速度和表达能力方面做出了不同的权衡，其中表达能力可通过任意两个输入之间的最大路径长度来量化。总结见表 15.1。

对于核大小为 k、特征通道数为 d 的一维 CNN，计算输出的时间为 $ O(knd^{2}) $，且可并行计算。我们需要堆叠 n/k 层，如果使用空洞卷积，则需 $ \log_{k}(n) $ 层，以确保所有输入对之间能够通信。例如，在图 15.27 中，我们看到 $ x_{1} $ 和 $ x_{5} $ 最初相距 5 步，第 1 层后相距 3 步，然后第 2 层后相连。

对于 RNN，当隐状态大小为 d 时，计算复杂度为 $ O(nd^{2}) $，因为每一步都要进行矩阵-向量乘法。这是一种固有的顺序操作。最大路径长度为 $ O(n) $。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_254_146_918_551.jpg" alt="图像" width="57%" /></div>


<div style="text-align: center;">图 15.27: 一维CNN、RNN与自注意力模型的比较。摘自文献[Zha+20]的图10.6.1，经Aston Zhang许可使用。</div>


最后，对于自注意力模型，每个输出都直接连接到每个输入，因此最大路径长度为 $O(1)$。然而，其计算开销为 $O(n^2d)$。对于短序列，通常有 $n \ll d$，因此这尚可接受。对于较长序列，我们将在第15.6节讨论各种快速版本的注意力机制。

#### 15.5.6 图像领域的Transformer *

CNN（第14章）是处理图像数据最常用的模型类型，因为它们具有有用的内置归纳偏置，例如局部性（由于小卷积核）、等变性（由于权重共享）和不变性（由于池化）。令人惊讶的是，人们发现Transformer在图像分类上也能表现良好 [Rag+21]，至少在使用足够多的数据训练时是如此（它们需要大量数据来弥补缺乏相关归纳偏置的不足）。

这类模型中的第一个称为ViT（视觉Transformer）[Dos+21]，它将输入图像切割成16x16的块，将每个块投影到嵌入空间中，然后将这组嵌入 $x_{1:T}$ 传递给Transformer，类似于词嵌入传递给Transformer的方式。输入前还会加上一个特殊的[CLASS]嵌入 $x_0$。Transformer的输出是一组编码 $e_{0:T}$；模型将 $e_0$ 映射到目标类别标签 $y$，并以监督方式进行训练。如图15.28所示。

在监督预训练之后，模型会在各种下游分类任务上进行微调，这种方法称为迁移学习（详见第19.2节）。当在“小”数据集（如ImageNet，包含1000个类别和130万张图像）上训练时，他们发现ViT无法胜过预训练的CNN ResNet模型（第14.3.4节），即BiT（大规模迁移）[Kol+20]。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_306_118_868_405.jpg" alt="图像" width="48%" /></div>


<div style="text-align: center;">图15.28：视觉Transformer（ViT）模型。它将图像视为一组输入块。输入在位置0处预置了特殊的CLASS嵌入向量（用*表示）。图像的类别标签通过对位置0的最终输出编码应用softmax得到。摘自[Dos+21]的图1，经Alexey Dosovitskiy许可使用。</div>


然而，当在更大的数据集上训练时，例如ImageNet-21k（包含21k个类别和14M张图像）或Google内部的JFT数据集（包含18k个类别和303M张图像），他们发现ViT在迁移学习上的表现优于BiT。$ ^{6} $在此规模下，ViT的训练成本也比ResNet更低。（但训练仍然昂贵：在Google Cloud TPUv3（8个核心）上，大型ViT模型在ImageNet-21k上需要30天时间。）

#### 15.5.7 其他Transformer变体  $ * $

近几年来，Transformer的许多扩展已被发表。例如，Gshard论文[Lep+21]展示了如何通过用混合专家（第13.6.2节）回归模块替换部分前馈密集层，将Transformer扩展到更多参数。这实现了稀疏条件计算，对于给定的任何输入，仅使用模型容量的一部分（由门控网络选择）。

另一个例子是Conformer论文[Gul+20]，展示了如何在Transformer架构内部添加卷积层，这被证明对各种语音识别任务有帮助。

### 15.6 高效的Transformer  $ * $

本节由Krzysztof Choromanski撰写。

常规Transformer对于长度为 $ N $ 的序列需要 $ O(N^2) $ 的时间和空间复杂度，这使得它们难以应用于长序列。在过去几年中，研究人员提出了几种更高效的Transformer变体来克服这一困难。在本节中，我们给出

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_220_120_946_681.jpg" alt="图像" width="63%" /></div>


<div style="text-align: center;">图15.29：不同高效Transformer架构分类法的韦恩图。来自[Tay+20b]。经Yi Tay许可使用。</div>


简要概述其中一些方法（总结见图15.29）。更多细节参见例如[Tay+20b; Tay+20a; Lin+21]。

#### 15.6.1 固定的不可学习的局部注意力模式

对注意力机制最简单的修改是将其约束到一个固定的不可学习的局部窗口，换句话说，限制每个词元只关注预选的其他词元子集。例如，若将每个序列分成 $K$ 块，每块长度为 $\frac{N}{K}$，并且仅在一个块内进行注意力计算，则空间/时间复杂度从 $O(N^2)$ 降低到 $\frac{N^2}{K}$。当 $K \gg 1$ 时，这构成了整体计算量的显著改进。此类方法特别应用于[Qiu+19b; Par+18]中。注意力模式不必局限于块状形式。其他方法包括步进/扩张窗口，或混合模式，将多个固定注意力模式组合在一起[Chi+19b; BPC20]。

---

#### 15.6.2 可学习的稀疏注意力模式

上述方法的一个自然扩展是允许学习这些紧凑模式。注意力仍然限制在某个对所有token进行分区的单一分区内的token对之间，但现在这些分区是可训练的。在这类方法中，我们可以区分两种主要方法：基于哈希和基于聚类。在哈希场景中，所有token都被哈希，因此不同的分区对应于不同的哈希桶。例如，Reformer架构[KKL20]就属于这种情况，它应用了局部敏感哈希（LSH）。这导致注意力模块的时间复杂度为 $ O(NM^{2}\log(M)) $，其中M表示token嵌入的维度。

哈希方法要求查询集与键集完全相同。此外，精确分区所需的哈希数量（在上述表达式中视为常数）可能是一个很大的常数。在聚类方法中，使用标准聚类算法（如K-means（第21.3节））对token进行聚类；这被称为“聚类Transformer”[Roy+20]。与分块情况类似，如果使用K个大小相等的聚类，则注意力模块的空间复杂度降低为 $ O(\frac{N^2}{K}) $。在实践中，K通常取 $ K = \Theta(\sqrt{N}) $ 量级，但强制要求聚类大小相似在实践中是困难的。

#### 15.6.3 记忆与循环方法

在一些方法中，辅助记忆模块可以同时访问多个token。这种方法通常以全局记忆算法的形式实现，如[Lee+19; Zah+20]中所用。

另一种方法是通过循环连接不同的局部块。此类方法的一个典型例子是Transformer-XL方法系列[Dai+19]。

#### 15.6.4 低秩与核方法

在本节中，我们讨论使用低秩矩阵近似注意力的方法。在[She+18; Kat+20]中，他们直接用一个低秩矩阵近似注意力矩阵A，使得

 $$ A_{i j}=\phi(\boldsymbol{q}_{i})^{\top}\phi(\boldsymbol{k}_{j}) $$ 

其中 $ \phi(\boldsymbol{x}) \in \mathbb{R}^M $ 是某个有限维向量，且 $ M < D $。可以利用这种结构在 $ O(N) $ 时间内计算 $ \mathbf{A}\mathbf{V} $。不幸的是，对于softmax注意力，矩阵 $ \mathbf{A} $ 并非低秩。

在Linformer[Wan+20a]中，他们转而通过随机高斯投影变换键和值。然后应用Johnson-Lindenstrauss变换[AL13]的理论，在这个低维空间中近似softmax注意力。

在Performer[Cho+20a; Cho+20b]中，他们证明可以使用（正定）核函数计算注意力矩阵。我们在第17.1节中定义核函数，但其基本思想是 $ \mathcal{K}(q, k) \geq 0 $ 是 $ q \in \mathbb{R}^D $ 和 $ k \in \mathbb{R}^D $ 之间某种相似性度量。例如，高斯核（也称为径向基函数核）的形式为

 $$ \mathcal{K}_{\mathrm{gauss}}(\boldsymbol{q},\boldsymbol{k})=\exp\left(-\frac{1}{2\sigma^{2}}||\boldsymbol{q}-\boldsymbol{k}||_{2}^{2}\right) $$ 

为了说明如何利用这一点计算注意力矩阵，注意[Cho+20a]给出了如下结果：

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND许可证

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_398_135_786_334.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">图15.30：注意力矩阵 $\mathbf{A}$ 重写为两个低秩矩阵 $\mathbf{Q}'$ 和 $(\mathbf{K}')^\top$ 的乘积，其中随机特征映射 $\phi(\mathbf{q}_i) \in \mathbb{R}^M$ 和 $\phi(\mathbf{v}_k) \in \mathbb{R}^M$ 对应存储于行/列中的查询和键。经Krzysztof Choromanski许可使用。</div>


$$  A_{i,j}=\exp(\frac{\boldsymbol{q}_{i}^{\top}\boldsymbol{k}_{j}}{\sqrt{D}})=\exp(\frac{-\|\boldsymbol{q}_{i}-\boldsymbol{k}_{j}\|_{2}^{2}}{2\sqrt{D}})\times\exp(\frac{\|\boldsymbol{q}_{i}\|_{2}^{2}}{2\sqrt{D}})\times\exp(\frac{\|\boldsymbol{k}_{j}\|_{2}^{2}}{2\sqrt{D}}).   \tag*{(15.64)}$$

上述表达式中的第一项等于 $\mathcal{K}_{\mathrm{gauss}}(\boldsymbol{q}_i D^{-1/4}, \boldsymbol{k}_j D^{-1/4})$，其中 $\sigma = 1$，而另外两项仅是独立的缩放因子。

到目前为止，我们在计算上尚未获得任何优势。然而，我们将在第17.2.9.3节中证明，高斯核可以写为一组随机特征的期望：

$$  \mathcal{K}_{\mathrm{g a u s s}}(\boldsymbol{x},\boldsymbol{y})=\mathbb{E}\left[\boldsymbol{\eta}(\boldsymbol{x})^{\top}\boldsymbol{\eta}(\boldsymbol{y})\right]   \tag*{(15.65)}$$

其中 $\eta(\boldsymbol{x}) \in \mathbb{R}^M$ 是从 $\boldsymbol{x}$ 导出的随机特征向量，其构造基于三角函数（式(17.60)）或指数函数（式(17.61)）。（后者的优点在于所有特征均为正值，从而获得更好的结果 [Cho+20b]）。因此，对于常规的 softmax 注意力，$A_{i,j}$ 可重写为

$$  A_{i,j}=\mathbb{E}[\phi(\boldsymbol{q}_{i})^{\top}\phi(\boldsymbol{k}_{j})]   \tag*{(15.66)}$$

其中 $\phi$ 定义为：

$$  \phi(\boldsymbol{x})\triangleq\exp\left(\frac{\|\boldsymbol{x}\|_{2}^{2}}{2\sqrt{D}}\right)\eta\left(\frac{\boldsymbol{x}}{D^{\frac{1}{4}}}\right).   \tag*{(15.67)}$$

我们可以将完整的注意力矩阵写为

$$  \mathbf{A}=\mathbb{E}[\mathbf{Q}^{\prime}(\mathbf{K}^{\prime})^{\mathsf{T}}]   \tag*{(15.68)}$$

其中 $\mathbf{Q}', \mathbf{K}' \in \mathbb{R}^{N \times M}$ 的行编码了对应查询和键的随机特征映射。（注意，若确保这些随机特征正交，可得到更优性能，详见 [Cho+20a]）。如图15.30所示。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_258_128_908_330.jpg" alt="图像" width="56%" /></div>


<div style="text-align: center;">图 15.31: 利用注意力矩阵 $\mathbf{A}$ 的分解可以借助矩阵结合律改进注意力计算。为计算 $\mathbf{AV}$，我们先计算 $\mathbf{G} = (\mathbf{k}')^\top \mathbf{V}$，再计算 $\mathbf{q}'\mathbf{G}$，从而在空间和时间复杂度上达到线性于 $N$。经 Krzysztof Choromanski 授权使用。</div>


我们可以通过使用随机特征 $\phi(\boldsymbol{q}_i)$ 和 $\phi(\boldsymbol{k}_j)$ 的单个样本，并取较小的 $M$ 值（例如 $M = O(D \log(D))$）来构造 $\mathbf{A}$ 的一个近似。然后，我们可以用 $O(N)$ 时间近似整个注意力运算：

$$  \widehat{\mathrm{attention}}(\mathbf{Q},\mathbf{K},\mathbf{V})=\mathrm{diag}^{-1}(\mathbf{Q}^{\prime}((\mathbf{K}^{\prime})^{\top}\mathbf{1}_{N}))(\mathbf{Q}^{\prime}((\mathbf{K}^{\prime})^{\top}\mathbf{V}))   \tag*{(15.69)}$$

可以证明这是对精确 softmax 注意力运算的无偏近似。参见图 15.31 的图示。（关于如何将其推广到掩蔽（因果）注意力，详见 [Cho+20a]。）

### 15.7 语言模型与无监督表示学习

我们已经讨论过如何将 RNN 和自回归（仅解码器）Transformer 用作语言模型，这类模型是形式为 $p(x_1, \ldots, x_T) = \prod_{t=1}^T p(x_t | \boldsymbol{x}_{1:t-1})$ 的生成式序列模型，其中每个 $x_t$ 是一个离散词元，例如单词或词片（WordPiece）。（文本预处理方法讨论见第 1.5.4 节。）这些模型的隐状态随后可作为文本的连续向量表示。也就是说，我们不再使用独热向量 $\boldsymbol{x}_t$ 或它的学习嵌入（如第 20.5 节所述），而是使用依赖于句子中所有前面单词的隐状态 $\boldsymbol{h}_t$。这些向量可用作上下文词嵌入，用于文本分类或序列到序列（seq2seq）等任务（例如，综述见 [LKB20]）。这种方法的优势在于，我们可以在大规模文本语料库上以无监督方式预训练语言模型，然后在小规模标注任务专用数据集上以监督方式对模型进行微调（这种通用方法称为迁移学习，详见第 19.2 节）。

如果我们的主要目标是计算用于迁移学习的有用表示（而非生成文本），我们可以用非因果模型替代生成式序列模型，这类模型能计算句子的表示，但不能生成句子。这些模型的优势在于，隐状态 $\pmb{h}_{t}$ 现在可以依赖于过去 $\pmb{y}_{1:t-1}$、当前 $\pmb{y}_{t}$ 和未来 $\pmb{y}_{t+1:T}$。由于考虑了更多上下文，这有时能产生更好的表示。

在以下小节中，我们将简要讨论一些用于文本表示学习的无监督模型，涵盖因果模型和非因果模型。

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_348_122_821_402.jpg" alt="图像" width="41%" /></div>

<div style="text-align: center;">图 15.32: ELMo 双向语言模型示意图。这里 $y_t = x_{t+1}$ 是前向 LSTM 的目标，而 $y_t = x_{t-1}$ 是后向 LSTM 的目标。（我们添加了句子起始标记和句子结束标记来处理边缘情况。）摘自 [Wen19]。经 Lilian Weng 许可使用。</div>

#### 15.7.1 ELMo

在 [Pet+18] 中，他们提出了一种称为 ELMo 的方法，它是“来自语言模型的嵌入”（Embeddings from Language Model）的缩写。基本思想是拟合两个 RNN 语言模型，一个从左到右，另一个从右到左，然后将它们的隐藏状态表示结合起来，为每个单词生成一个嵌入。与需要输入-输出对的 biRNN（第 15.2.2 节）不同，ELMo 以无监督方式训练，以最小化输入句子 $\mathbf{x}_{1:T}$ 的负对数似然：

$$ \mathcal{L}(\boldsymbol{\theta})=-\sum_{t=1}^{T}[\log p(x_{t}|\boldsymbol{x}_{1:t-1};\boldsymbol{\theta}_{e},\boldsymbol{\theta}^{\rightarrow},\boldsymbol{\theta}_{s})+\log p(x_{t}|\boldsymbol{x}_{t+1:T};\boldsymbol{\theta}_{e},\boldsymbol{\theta}^{\leftarrow},\boldsymbol{\theta}_{s})] \tag*{(15.70)}$$

其中 $\theta_e$ 是嵌入层的共享参数，$\theta_s$ 是 Softmax 输出层的共享参数，$\theta^\rightarrow$ 和 $\theta^\leftarrow$ 是两个 RNN 模型的参数。（他们使用 LSTM RNN，如第 15.2.7.2 节所述。）图 15.32 给出了一个示意图。

训练完成后，我们定义了上下文表示 $r_t = [e_t, h_{t:L}^\rightarrow, h_{t:L}^\leftarrow]$，其中 $L$ 是 LSTM 的层数。然后学习一组特定于任务的线性权重，将其映射到每个标记的最终上下文相关嵌入：$r_t^j = r_t^{\mathrm{T}} w^j$，其中 $j$ 是任务 ID。如果我们执行句法任务（如词性标注，POS），即标记每个单词是名词、动词、形容词等，则该任务将学习对较低层分配更大的权重。如果我们执行语义任务（如词义消歧，WSD），则该任务将学习对较高层分配更大的权重。在这两种情况下，我们只需要少量特定于任务的标注数据，因为我们只需学习一个权重向量，将 $r_{1:T}$ 映射到目标标签 $\mathbf{y}_{1:T}$。

#### 15.7.2 BERT

在本节中，我们描述 [Dev+19] 提出的 BERT 模型（来自 Transformer 的双向编码器表示，Bidirectional Encoder Representations from Transformers）。与 ELMo 类似，这是一个非因果模型，可用于创建文本表示，但不能生成文本。具体而言，它使用了 Transformer 模型来处理输入序列的修改版本。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_264_127_499_331.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_675_125_903_331.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 15.33: (a) BERT 和 (b) GPT 的示意图。 $E_{t}$ 是位置 t 处输入 token 的嵌入向量，$T_{t}$ 是要预测的输出目标。摘自 [Dev+19] 的图 3，经 Ming-Wei Chang 许可使用。</div>


将序列中的某个 token 恢复为未修改的形式。在位置 t 处的修改后输入中，除了第 t 个词之外的所有词都被省略，任务是预测缺失的词。这被称为填空或完形填空任务。

##### 15.7.2.1 掩码语言模型任务

更精确地说，模型通过最小化负对数伪似然来进行训练：

$$  \mathcal{L}=\mathbb{E}_{x\sim\mathcal{D}}\mathbb{E}_{m}\sum_{i\in m}-\log p(x_{i}|\boldsymbol{x}_{-m})   \tag*{(15.71)}$$

其中 m 是一个随机二进制掩码。例如，如果我们用烹饪视频的转录文本训练模型，可能会构造一个如下的训练句子：

Let's make [MASK] chicken! [SEP] It [MASK] great with orange sauce.

其中 [SEP] 是插入在两个句子之间的分隔 token。被掩码词的期望目标标签是 "some" 和 "tastes"。（此例来自 [Sun+19a]。）

条件概率通过对位置 i 的最终层隐藏向量应用 softmax 得到：

$$  p(x_{i}|\hat{\boldsymbol{x}})=\frac{\exp(\boldsymbol{h}(\hat{\boldsymbol{x}})_{i}^{\top}\boldsymbol{e}(x_{i}))}{\sum_{x^{\prime}}\exp(\boldsymbol{h}(\hat{\boldsymbol{x}})_{i}^{\top}\boldsymbol{e}(x^{\prime}))}   \tag*{(15.72)}$$

其中 $\hat{x} = x_{-m}$ 是掩码后的输入句子，$e(x)$ 是 token $x$ 的嵌入向量。该公式用于计算掩码位置的损失；因此这被称为**掩码语言模型**。（这类似于第 20.3.2 节的去噪自编码器）。该模型的示意图见图 15.33a。

##### 15.7.2.2 下一句预测任务

除了掩码语言模型目标外，最初的 BERT 论文还增加了一个额外的目标，即训练模型判断一个句子是否接在另一个句子之后。更精确地说，

作者: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_254_124_920_331.jpg" alt="图像" width="57%" /></div>

<div style="text-align: center;">图 15.34: 一对输入序列（记为 A 和 B）在输入 BERT 前如何编码的示意图。来自 [Zha+20] 的图 14.8.2。经 Aston Zhang 许可使用。</div>

模型接收如下输入：

$$   CLS A_{1}A_{2};\cdots A_{m};SEP B_{1}B_{2};\cdots;B_{n}SEP   \tag*{(15.73)}$$

其中 SEP 是一个特殊的分隔符标记，CLS 是一个标注类别的特殊标记。如果句子 B 在原始文本中紧随 A 之后，我们将目标标签设为 y = 1；但如果 B 是一个随机选取的句子，则将目标标签设为 y = 0。这称为**下一句预测任务**。这类预训练可用于句子对分类任务，例如我们在第 15.4.6 节讨论的文本蕴含或文本相似度。（注意，这类预训练被视为无监督或自监督，因为目标标签是自动生成的。）

在执行下一句预测时，模型输入由三种不同的嵌入指定：每个标记一个嵌入、每个片段标签（句子 A 或 B）一个嵌入、每个位置一个嵌入（使用学习到的位置嵌入）。然后将它们相加。图 15.34 展示了这一过程。BERT 接着使用 Transformer 编码器学习从输入嵌入序列到输出嵌入序列的映射，输出嵌入序列被解码为词标签（针对遮蔽位置）或类别标签（针对 CLS 位置）。

##### 15.7.2.3 针对 NLP 应用微调 BERT

在无监督方式下预训练 BERT 后，我们可以通过监督微调将其用于各种下游任务。（此类迁移学习方法的更多背景见第 19.2 节。）图 15.35 展示了如何通过简单地在最终隐藏层上添加一个或多个新的输出头来修改 BERT 模型以执行不同任务。示例代码见 bert_jax.ipynb。

在图 15.35(a) 中，我们展示了如何处理单句分类（例如情感分析）：只需取与虚拟 CLS 标记关联的特征向量，并将其输入 MLP。由于每个输出都关注所有输入，该隐藏向量将汇总整个句子。MLP 随后学习将其映射到所需的标签空间。

在图 15.35(b) 中，我们展示了如何处理句子对分类（例如第 15.4.6 节讨论的文本蕴含）：只需按公式 (15.73) 的格式输入两个句子，然后对 CLS 标记进行分类。

在图 15.35(c) 中，我们展示了如何处理单句标注，即为

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_267_125_504_340.jpg" alt="Image" width="20%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_676_123_909_335.jpg" alt="Image" width="20%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_260_371_502_586.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_672_375_912_579.jpg" alt="Image" width="20%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图15.35：BERT（Bidirectional Encoder Representations from Transformers，双向编码器表示来自Transformer）可用于不同类别监督式NLP任务的示意图。(a) 单句分类（如情感分析）；(b) 句对分类（如文本蕴含）；(c) 单句标注（如浅层句法分析）；(d) 问答。来自[Dev+19]的图4，经Ming-Wei Chang许可使用。</div>

为每个词赋予标签或标记，而不仅仅是对整个句子进行操作。此方法的一个常见应用是词性标注，我们将每个词标注为名词、动词、形容词等。另一个应用是名词短语组块分析（也称为浅层句法分析），我们需要标注每个名词短语的范围。该范围采用BIO标注法进行编码，其中B表示实体的开始，I-x表示实体内部，O表示实体外部。例如，考虑以下句子：

<div style="text-align: center;"><img src="imgs/img_in_image_box_151_911_852_932.jpg" alt="Image" width="60%" /></div>

##### British Airways rose after announcing its withdrawal from the UAI deal

我们看到这里有3个名词短语："British Airways"、"its withdrawal"和"the UAI deal"。（我们要求B、I和O标签按顺序出现，因此这是一个可以被纳入模型的先验约束。）

我们还可以为每个名词短语关联类型，例如区分人物、地点、组织和其他。因此标签空间变为{B-Per, I-Per, B-Loc, I-Loc, B-Org, I-Org, Outside}。这称为命名实体识别，是信息抽取中的关键步骤。例如，考虑以下句子：

##### BP IP 0 0 0 BL IL BP 0 0 0 0

Mrs Green spoke today in New York. Green chairs the finance committee.

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND许可证。

---

由此我们推断，第一句包含两个命名实体，即“Mrs Green”（类型为人物）和“New York”（类型为地点）。第二句提及了另一个人物“Green”，该人物极有可能与第一句中的为同一人，尽管这种跨句的实体消解并不属于基础命名实体识别（NER）任务的范围。

最后，在图15.35(d)中，我们展示了如何解决问答任务。此处，第一个输入句子是问题，第二个是背景文本，输出需要指定背景中包含答案的相关部分的起始和结束位置（见表1.4）。起始位置s和结束位置e是通过对背景文本的输出编码的池化版本应用两个不同的多层感知机（MLP）计算得到的；MLP的输出是对所有位置的softmax函数。在测试时，我们提取使得分数之和$ s_i + e_j $最大化的区间$ (i,j) $，其中$ i \leq j $。

BERT在许多自然语言处理（NLP）任务上取得了最先进的性能。有趣的是，[TDP19]表明BERT隐式地重新发现了标准的NLP流水线，在该流水线中，不同层分别执行诸如词性（POS）标注、句法分析、命名实体关系（NER）检测、语义角色标注（SRL）、共指消解等任务。有关NLP的更多细节可参见[JM20]。

#### 15.7.3 GPT

在[Rad+18]中，他们提出了一种名为GPT的模型，GPT是“生成式预训练Transformer”（Generative Pre-training Transformer）的缩写。这是一种因果（生成式）模型，使用掩码Transformer作为解码器。如图15.33b所示。

在原始GPT论文中，他们同时优化大规模无标签数据集和小规模有标签数据集。在分类设定下，损失函数由$ \mathcal{L} = \mathcal{L}_{\mathrm{cls}} + \lambda \mathcal{L}_{\mathrm{LM}} $给出，其中$ \mathcal{L}_{\mathrm{cls}} = -\sum_{(\boldsymbol{x}, y) \in \mathcal{D}_L} \log p(y|\boldsymbol{x}) $是有标签数据上的分类损失，$ \mathcal{L}_{\mathrm{LM}} = -\sum_{\boldsymbol{x} \in \mathcal{D}_U} \sum_t \log p(x_t | \boldsymbol{x}_{1:t-1}) $是无标签数据上的语言建模损失。

在$ [\text{Rad}+19] $中，他们提出了GPT-2，这是GPT的一个更大版本，在名为WebText的大型网络语料库上训练。他们还消除了任何特定于任务的训练，而是直接将其作为语言模型进行训练。GPT-3$ [\text{Bro}+20] $和GPT-4$ [\text{Ope23}] $模型是GPT-2的更大版本，但基于相同的原理。最近，OpenAI发布了ChatGPT$ [\text{Ope}] $，这是GPT-3的改进版本，通过使用一种称为基于人类反馈的强化学习（RLHF）的技术进行训练，使其能够进行交互式对话。该技术首先在InstructGPT论文$ [\text{Ouy}+22] $中引入。它利用强化学习技术对模型进行微调，使其生成的响应更“符合”人类意图，这种意图由一个基于监督数据预训练的排序模型来估计。

##### 15.7.3.1 GPT的应用

GPT可以根据给定的初始输入提示生成文本。提示可以指定一个任务；如果生成的响应“开箱即用”地完成了任务，我们称该模型正在进行零样本任务迁移（详见第19.6节）。例如，为了对某些输入文本$x_{1:T}$进行抽象式摘要（与抽取式摘要相对，后者仅选择输入词的一个子集），我们从$ p(\mathbf{x}_{T+1:T+100}|\mathbf{x}_{1:T};\mathrm{TL};\mathrm{DR}) $中采样，其中$\mathrm{TL};\mathrm{DR}$是一个添加到输入文本末尾的特殊标记，用于告知系统用户需要摘要。TL;DR代表“太长，没读”（too long; didn’t read），通常在网络文本中后跟人工创建的摘要出现。通过将该标记添加到输入中，用户希望“触发”Transformer解码器进入一种状态，

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_268_121_900_331.jpg" alt="图" width="54%" /></div>

<div style="text-align: center;">图 15.36：T5 模型（“文本到文本迁移 Transformer”）如何用于执行多种 NLP 任务的示意图，例如将英语翻译为德语；判断一个句子在语言学上是否有效（CoLA 代表“语言可接受性语料库”）；判断语义相似度（STSB 代表“语义文本相似度基准”）；以及抽象式摘要。来自 [Raf+20] 的图 1，经 Colin Raffel 许可使用。</div>

此时它进入摘要模式。（这是“提示工程”的一个例子）。然而，一种可以说更好的告诉模型执行什么任务的方法是将其训练在输入-输出对上进行，如第 15.7.4 节所述。

GPT 也可以用于创建聊天机器人，例如 ChatGPT [Ope]，以及用于代码生成（例如，参见 [HBK23]）。

#### 15.7.4 T5

许多模型以无监督方式训练，然后在特定任务上进行微调。也可以通过将系统需要执行的任务作为输入句子的一部分告知系统，然后将其作为序列到序列（seq2seq）模型进行训练，从而使单个模型执行多个任务，如图 15.36 所示。这是 T5 [Raf+20] 所采用的方法，T5 代表“文本到文本迁移 Transformer”。该模型是一个标准的序列到序列 Transformer，首先在无监督的 $(x', x'')$ 对上进行预训练，其中 $x'$ 是 $x$ 的掩码版本，$x''$ 是需要预测的缺失 token，然后在多个监督的 $(x, y)$ 对上微调。

无监督数据来自 C4，即“巨型干净爬取语料库”，一个包含 750GB 网络文本的语料库。它被用于使用类似 BERT 的去噪目标进行预训练。例如，句子 x = “Thank you for inviting me to your party last week” 可能会转换为输入 x′ = “Thank you <X> me to your party <Y> week” 和输出（目标）x′′ = “<X> for inviting <Y> last <EOS>”，其中 <X> 和 <Y> 是该示例特有的 token。

监督数据集是人工创建的，取自文献。最近发布了 FLAN-T5 模型 [Chu+22]，该模型在超过 1800 项任务（包括语言翻译、文本分类和问答）上使用了指令微调。由此产生的模型目前在许多 NLP 任务上达到了最先进的水平。

#### 15.7.5 讨论

大型语言模型（LLM），如 BERT 和 GPT-3，近年来引起了广泛关注。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

引起兴趣，甚至已进入主流媒体。$^{7}$ 然而，关于这类系统是否以任何有意义的方式“理解”语言，而不仅仅是重新排列其海量训练数据中出现的单词模式，仍存在一些疑问。例如，[NK19] 表明，BERT 在论点推理理解任务上表现几乎与人类相当的能力“完全归因于对数据集中虚假统计线索的利用”。通过稍微调整数据集，其性能可以降至随机水平。关于对此类模型的其他批评，参见例如 [BK20; Mar20; Dzi+23; Mah+23]。

---

第四部分

---



---

# 16 基于样例的方法

到目前为止，本书主要关注参数化模型，包括无条件模型 \( p(\boldsymbol{y}|\boldsymbol{\theta}) \) 或条件模型 \( p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta}) \)，其中 \( \boldsymbol{\theta} \) 是固定维度的参数向量。参数是从大小可变的数据集 \( \mathcal{D}=\{(\boldsymbol{x}_{n},\boldsymbol{y}_{n}):n=1:N\} \) 中估计得到的，但在模型拟合完成后，数据会被丢弃。

在本节中，我们将考虑各种保留训练数据的非参数模型。因此，模型的有效参数数量可以随 \( |\mathcal{D}| \) 增长。我们重点关注那些可通过测试输入 \(\boldsymbol{x}\) 与每个训练输入 \(\boldsymbol{x}_n\) 之间的相似性来定义的模型。或者，我们也可以用不相似性或距离函数 \( d(\mathbf{x}, \mathbf{x}_n) \) 来定义模型。由于这些模型在测试时保留了训练样本，我们称它们为**基于样例的模型**（这种方法也被称为基于实例的学习 [AKA91] 或基于记忆的学习）。

## 16.1 K 近邻（KNN）分类

在本节中，我们将讨论一种最简单的分类器，即 K 近邻（KNN）分类器。其思想如下：为了对新的输入 \(\boldsymbol{x}\) 进行分类，我们在训练集中找到与 \(\boldsymbol{x}\) 最近的 K 个样本，记为 \( N_K(\boldsymbol{x}, \mathcal{D}) \)，然后查看它们的标签，从而推导出 \(\boldsymbol{x}\) 局部区域输出变量的分布。更精确地，我们计算

$$  p(y=c|\boldsymbol{x},\mathcal{D})=\frac{1}{K}\sum_{n\in N_{K}(\boldsymbol{x},\mathcal{D})}\mathbb{I}(y_{n}=c)   \tag*{(16.1)}$$

然后我们可以返回该分布，或返回多数标签。

该模型的两个主要参数是邻域大小 K 和距离度量 \( d(\boldsymbol{x}, \boldsymbol{x}') \)。对于后者，通常使用马氏距离

$$  d_{\mathbf{M}}(\boldsymbol{x},\boldsymbol{\mu})=\sqrt{(\boldsymbol{x}-\boldsymbol{\mu})^{\mathsf{T}}\mathbf{M}(\boldsymbol{x}-\boldsymbol{\mu})}   \tag*{(16.2)}$$

其中 \(\mathbf{M}\) 是一个正定矩阵。如果 \( \mathbf{M} = \mathbf{I} \)，则简化为欧氏距离。我们将在第 16.2 节讨论如何学习距离度量。

尽管 KNN 分类器非常简单，但可以证明当 \( N \to \infty \) 时，该方法能够达到贝叶斯误差（衡量最佳可能分类器性能的指标）的两倍以内 [CH67; CD14]。（当然，实际中收敛到这一最优性能的速度可能较慢，原因将在第 16.1.2 节讨论。）

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_229_142_928_364.jpg" alt="图像" width="60%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 16.1: (a) 二维空间中 K=5 的 K近邻分类器示意图。测试点 x 的最近邻标签为  $ \{1,1,1,0,0\} $，因此预测结果为  $ p(y = 1|\boldsymbol{x},\mathcal{D}) = 3/5 $。(b) 1-NN 诱导的 Voronoi 图。改编自 [DHS01] 的图 4.13。由 knn_voronoi_plot.ipynb 生成。</div>


#### 16.1.1 示例

我们在图 16.1(a) 中展示了 $K = 5$ 时二维空间中的 KNN 分类器。测试点标记为“x”。5 个最近邻中有 3 个标签为 1，2 个标签为 0。因此我们预测 $p(y = 1|\boldsymbol{x},\mathcal{D}) = 3/5 = 0.6$。

若使用 $K = 1$，则直接返回最近邻的标签，预测分布变为 delta 函数。$K = 1$ 的 KNN 分类器会诱导出数据点的 **Voronoi 图**（见图 16.1(b)）。这是一种空间划分方式，为每个点 $\boldsymbol{x}_n$ 关联一个区域 $V(\boldsymbol{x}_n)$，使得 $V(\boldsymbol{x}_n)$ 内的所有点距离 $\boldsymbol{x}_n$ 比距离其他任何点更近。在每个单元内，预测标签即为对应训练点的标签。因此当 $K = 1$ 时训练误差为 0。然而，如下所示，此类模型通常会在训练集上过拟合。

图 16.2 给出了 KNN 应用于一个三类二维数据集的示例。我们可以看到，当 K=1 时，模型在训练集上错误率为零。随着 K 增大，决策边界变得更加平滑（因为我们在更大的邻域上进行平均），训练误差随之增大，开始出现欠拟合。如图 16.2(d) 所示。测试误差呈现典型的 U 形曲线。

#### 16.1.2 维度灾难

KNN 分类器的主要统计问题在于，由于 **维度灾难**，它们在高维输入上表现不佳。

基本问题是空间体积随维度呈指数增长，因此可能需要在空间中寻找很远才能找到最近邻。为了更精确地说明这一点，考虑 [HTF09, p22] 中的例子。假设将 KNN 分类器应用于输入均匀分布在 D 维单位立方体中的数据。我们通过在测试点 x 周围“生长”一个超立方体，直到该立方体包含所需比例 p 的数据点，来估计 x 附近类标签的密度。该立方体的预期边长为 $ e_D(s) \triangleq p^{1/D} $；该函数如图 16.3(b) 所示。如果 $ D = 10 $，并且我们希望基于 10% 的数据点进行估计，那么

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_208_147_557_385.jpg" alt="图片" width="30%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_616_146_964_387.jpg" alt="图片" width="30%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_208_445_556_685.jpg" alt="图片" width="30%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_606_459_959_697.jpg" alt="图片" width="30%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图16.2：KNN分类器产生的决策边界。(a) K = 1。(b) K = 2。(c) K = 5。(d) 训练误差和测试误差与K的关系。由knn_classify_demo.ipynb生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_285_837_479_1039.jpg" alt="图片" width="16%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_655_832_924_1047.jpg" alt="图片" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图16.3：维度灾难的示意图。(a) 在单位大立方体内嵌入一个边长为s的小立方体。(b) 绘制覆盖单位立方体给定体积所需立方体的边长与维数的关系。改编自[HTF09]的图2.6。由curse_dimensionality_plot.ipynb生成。</div>

---

数据，我们有 $ e_{10}(0.1) = 0.8 $，因此我们需要在 x 周围将立方体沿每个维度扩展 80%。即使我们只使用 1% 的数据，也会发现 $ e_{10}(0.01) = 0.63 $。由于数据在每个维度上的范围仅为 0 到 1，我们看到该方法不再具有很强的局部性，尽管其名称为“最近邻”。查看如此远的邻居的问题在于，它们可能无法很好地预测给定点处函数的行为。

解决维数灾难主要有两种方案：对函数形式做出一些假设（即使用参数化模型），和/或使用仅关注维度子集的度量（参见第 16.2 节）。

#### 16.1.3 降低速度与内存需求

KNN 分类器会存储所有训练数据。这显然非常浪费空间。目前已有多种启发式剪枝技术被提出，用于移除不影响决策边界的点，例如见 [WM00]。在第 17.4 节中，我们讨论了一种基于稀疏先验的更具原则性的方法；由此得出的方法称为稀疏核机，它仅保留最有用的样本子集。

在运行时间方面，挑战在于以低于 $ O(N) $ 的时间找到 $ K $ 个最近邻，其中 $ N $ 是训练集的大小。当空间的维度超过约 10 维时，精确最近邻搜索在计算上变得难以处理，因此大多数方法专注于寻找近似最近邻。主要有两类技术：基于将空间划分为区域的方法，或使用哈希的方法。

对于划分方法，可以使用某种 k-d 树（将空间划分为轴平行区域），或某种聚类方法（使用锚点）。对于哈希方法，局部敏感哈希（LSH）[GIM99] 被广泛使用，尽管最近的方法从数据中学习哈希函数（例如见 [Wan+15]）。关于哈希方法的良好介绍见 [LRU14]。

一个名为 FAISS 的开源库，用于高效地进行稠密向量的精确和近似最近邻搜索（以及 K 均值聚类），可在 https://github.com/facebookresearch/faiss 获取，并在 [JDJ17] 中进行了描述。

#### 16.1.4 开放集识别

不要问它叫什么，要问它像什么。——Moshe Bar [Bar09]

在我们迄今为止考虑的所有分类问题中，我们都假设类别集合 C 是固定的。（这是封闭世界假设的一个例子，该假设假定（类型）事物的数量是固定的。）然而，许多现实世界问题涉及来自新类别的测试样本。这被称为开放集识别，我们将在下文中讨论。

##### 16.1.4.1 在线学习、OOD 检测与开放集识别

例如，假设我们训练一个人脸识别系统，从一组固定的人脸图像集（称为 $\mathbf{gallery}$）中预测一个人的身份。令 $\mathcal{D}_t = \{(\mathbf{x}_n, y_n) : \mathbf{x}_n \in \mathcal{X}, y_n \in \mathcal{C}_t, n = 1 : N_t\}$ 为时刻 $t$ 的带标签数据集，其中 $\mathcal{X}$ 是（人脸）图像集合，$\mathcal{C}_t = \{1, \ldots, C_t\}$ 是系统在时刻 $t$ 已知的人物集合（其中 $C_t \leq t$）。在测试时，系统可能会遇到一个之前从未见过的新人。令 $\mathbf{x}_{t+1}$ 为该新图像，$y_{t+1} = C_{t+1}$ 为其新标签。系统

---

需要识别出输入来自一个新的类别，而不是意外地将其分类为 $C_t$ 中的某个标签。这被称为**新颖性检测**。在这种情况下，输入是从分布 $p(\boldsymbol{x}|y = C_{t+1})$ 生成的，其中 $C_{t+1} \notin C_t$ 是新的“类标签”。如果这个新图像的外观与 $D_t$ 中任何现有图像的外观相似，那么检测出 $\boldsymbol{x}_{t+1}$ 来自一个新类可能是困难的。

如果系统成功检测到 $\boldsymbol{x}_{t+1}$ 是新颖的，那么它可以请求这个新实例的标识，记为 $C_{t+1}$。然后，它可以将标记对 $(\boldsymbol{x}_{t+1}, C_{t+1})$ 添加到数据集中，从而创建 $\mathcal{D}_{t+1}$，并通过将 $C_{t+1}$ 添加到 $\mathcal{C}_t$ 来扩展唯一类别的集合（参见 [JK13]）。这被称为增量学习、在线学习、终身学习或持续学习。在未来的时间点，系统可能会遇到从 $p(\boldsymbol{x}|y=c)$ 采样的图像，其中 $c$ 是一个现有类别，或者 $c$ 是一个新类别，或者图像可能从某种完全不同的分布 $p'(\boldsymbol{x})$ 中采样，与面部无关（例如，有人上传了他们狗的照片）。（检测后一种事件被称为分布外检测（out-of-distribution detection，简称OOD检测）。）

在这种在线设置中，我们通常每个类别只得到少量（有时只有一个）样本。这种设置下的预测被称为**小样本分类**，在第19.6节中有更详细的讨论。KNN分类器非常适合这项任务。例如，我们可以简单地将每个类别的所有实例存储在一个样本库中，如上所述。在时间 $t+1$，当我们得到输入 $x_{t+1}$ 时，不是通过将它与每个类别的某个参数化模型进行比较来预测 $x_{t+1}$ 的标签，而是直接在样本库中找到最接近（最相似）$x_{t+1}$ 的样本，记为 $x'$。然后我们需要确定 $x'$ 和 $x_{t+1}$ 是否足够相似以构成匹配。（在人分类的背景下，这被称为行人重识别或人脸验证，例如参见 [WSH16]）。如果没有匹配，我们可以声明输入是新颖的或OOD。

上述所有问题的关键要素是输入之间的（相异）相似性度量。我们在第16.2节讨论学习这种度量的方法。

##### 16.1.4.2 其他开放世界问题

开集识别和增量学习问题只是需要开放世界假设的问题的例子（参见 [Rus15]）。还有很多其他这类问题的例子。

例如，考虑**实体消解**问题，也称为**实体链接**。在这个问题中，我们需要确定不同的字符串（例如，"John Smith"和"Jon Smith"）是否指向同一实体。详见 [SHF15]。

另一个重要的应用是多目标跟踪。例如，当雷达系统检测到一个新的“光点”时，它是由于一个正在跟踪的现有导弹，还是一个进入空域的新目标？处理这类问题的一个优雅的数学框架被称为随机有限集，描述于 [Mah07; Mah13; Vo+15]。

### 16.2 学习距离度量

能够计算一对点之间的“语义距离” $d(\boldsymbol{x}, \boldsymbol{x}') \in \mathbb{R}^{+}$（其中 $\boldsymbol{x}, \boldsymbol{x}' \in \mathcal{X}$），或者等价地计算它们的相似度 $s(\boldsymbol{x}, \boldsymbol{x}') \in \mathbb{R}^{+}$，对于诸如最近邻分类（第16.1节）、自监督学习（第19.2.4.4节）、基于相似度的聚类（第21.5节）、基于内容的检索、视觉跟踪等任务至关重要。

作者：Kevin P. Murphy。（C）MIT出版社。CC-BY-NC-ND许可。

---

当输入空间为 $\mathcal{X} = \mathbb{R}^D$ 时，最常用的距离度量是马氏距离（Mahalanobis distance）

$$  d_{\mathbf{M}}(\mathbf{x},\mathbf{x}^{\prime})=\sqrt{(\mathbf{x}-\mathbf{x}^{\prime})^{\mathsf{T}}\mathbf{M}(\mathbf{x}-\mathbf{x}^{\prime})}   \tag*{(16.3)}$$

我们将在第16.2.1节讨论一些学习矩阵 $\mathbf{M}$ 的方法。对于高维输入或结构化输入，更好的做法是先学习一个嵌入 $e = f(\boldsymbol{x})$，然后在嵌入空间中计算距离。当 $f$ 是深度神经网络时，这被称为深度度量学习；我们将在第16.2.2节讨论。

#### 16.2.1 线性与凸方法

在本节中，我们讨论一些尝试学习马氏距离矩阵 $\mathbf{M}$ 的方法，这些方法要么直接（作为凸问题）进行，要么通过线性投影间接进行。有关度量学习的其他方法，可参考文献 [Kul13; Kim19] 以获取更多细节。

##### 16.2.1.1 大间隔最近邻

在文献 [WS09] 中，他们提出学习马氏矩阵 $\mathbf{M}$，使得学习得到的距离度量在用于最近邻分类器时效果良好。由此产生的方法被称为大间隔最近邻（large margin nearest neighbor，简称 LMNN）。

其工作原理如下。对于每个样本数据点 $i$，令 $N_i$ 为一组目标邻居（target neighbors）；这些邻居通常是在欧氏距离下与该点具有相同类别标签的 $K$ 个最近点。然后我们优化 $\mathbf{M}$，使得每个点 $i$ 与其所有目标邻居 $j \in N_i$ 之间的距离最小化：

$$  \mathcal{L}_{\mathrm{p u l l}}(\mathbf{M})=\sum_{i=1}^{N}\sum_{j\in N_{i}}d_{\mathbf{M}}(\boldsymbol{x}_{i},\boldsymbol{x}_{j})^{2}   \tag*{(16.4)}$$

同时，我们还需要确保具有错误标签的样本距离较远。为此，我们确保每个样本 $i$ 与其目标邻居 $j$ 的距离比与其他具有不同标签的点 $l$（即所谓的 impostors）的距离更近（至少相差某个间隔 $m \geq 0$）。我们可以通过最小化以下损失来实现：

$$  \mathcal{L}_{\mathrm{p u s h}}(\mathbf{M})=\sum_{i=1}^{N}\sum_{j\in N_{i}}\sum_{l=1}^{N}\mathbb{I}\left(y_{i}\neq y_{l}\right)\left[m+d_{\mathbf{M}}(\boldsymbol{x}_{i},\boldsymbol{x}_{j})^{2}-d_{\mathbf{M}}(\boldsymbol{x}_{i},\boldsymbol{x}_{l})^{2}\right]_{+}   \tag*{(16.5)}$$

其中 $[z]_{+} = \max(z, 0)$ 是合页损失函数（hinge loss function，参见第4.3.2节）。总体目标为 $\mathcal{L}(\mathbf{M}) = (1 - \lambda) \mathcal{L}_{\text{pull}}(\mathbf{M}) + \lambda \mathcal{L}_{\text{push}}(\mathbf{M})$，其中 $0 < \lambda < 1$。这是一个定义在凸集上的凸函数，可以通过半正定规划（semidefinite programming）进行最小化。或者，我们可以通过 $\mathbf{M} = \mathbf{W}^{\mathrm{T}} \mathbf{W}$ 对问题进行参数化，然后使用无约束梯度方法对 $\mathbf{W}$ 进行最小化。这种做法不再是凸的，但允许我们使用低维映射 $\mathbf{W}$。

对于大规模数据集，我们需要应对计算式 (16.5) 的 $O(N^{3})$ 代价。我们将在第16.2.5节讨论一些加速技巧。

##### 16.2.1.2 邻域成分分析

另一种学习线性映射 $\mathbf{W}$（使得 $\mathbf{M} = \mathbf{W}^\top \mathbf{W}$）的方法被称为邻域成分分析（neighborhood components analysis，简称 NCA）[Gol+05]。该方法定义了样本 $\boldsymbol{x}_i$ 以 $\boldsymbol{x}_j$ 作为其

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_390_117_782_334.jpg" alt="图片" width="34%" /></div>

<div style="text-align: center;">图16.4：潜在重合分析（LCA）作为有向图模型的示意图。输入 \( \mathbf{x}, \mathbf{x}' \in \mathbb{R}^D \) 通过线性映射 \( \mathbf{W} \) 被映射为高斯潜变量 \( \mathbf{z}, \mathbf{z}' \in \mathbb{R}^L \)。如果两个潜变量点重合（在长度尺度 \( \kappa \) 内），则设置相似性标签为 \( y = 1 \)，否则设置为 \( y = 0 \)。来自[DS12]的图1。经Lawrence Saul许可使用。</div>

使用线性softmax函数的最近邻分类器

$$  p_{ij}^{\mathbf{W}}=\frac{\exp(-||\mathbf{W}\boldsymbol{x}_{i}-\mathbf{W}\boldsymbol{x}_{j}||_{2}^{2})}{\sum_{l\neq i}\exp(-||\mathbf{W}\boldsymbol{x}_{i}-\mathbf{W}\boldsymbol{x}_{l}||_{2}^{2})}   \tag*{(16.6)}$$

（这是第20.4.10.1节讨论的随机邻域嵌入的有监督版本。）对于使用距离度量 \( \mathbf{W} \) 的1NN分类器，正确分类样本的期望数量由 \( J(\mathbf{W}) = \sum_{i=1}^{N} \sum_{j \neq i:y_{j}=y_i} p_{ij}^{\mathbf{W}} \) 给出。令 \( \mathcal{L}(\mathbf{W}) = 1 - J(\mathbf{W})/N \) 为留一法误差。我们可以使用梯度方法相对于 \( \mathbf{W} \) 最小化 \( \mathcal{L} \)。

##### 16.2.1.3 潜在重合分析

另一种学习线性映射 \( \mathbf{W} \)（使得 \( \mathbf{M} = \mathbf{W}^\top \mathbf{W} \)）的方法称为潜在重合分析（latent coincidence analysis, LCA）[DS12]。它定义了一个条件潜变量模型，用于将一对输入 \( \mathbf{x} \) 和 \( \mathbf{x}' \) 映射到标签 \( y \in \{0,1\} \)，该标签指定输入是相似（例如，具有相同类别标签）还是不相似。每个输入 \( \mathbf{x} \in \mathbb{R}^D \) 通过随机映射 \( p(z | \mathbf{x}) = \mathcal{N}(z | \mathbf{W} \mathbf{x}, \sigma^2 \mathbf{I}) \) 被映射到低维潜点 \( z \in \mathbb{R}^L \)，而 \( p(z' | \mathbf{x}') = \mathcal{N}(z' | \mathbf{W} \mathbf{x}', \sigma^2 \mathbf{I}) \)。（将此与第20.2节讨论的因子分析进行比较。）然后我们使用 \( p(y = 1 | \mathbf{z}, \mathbf{z}') = \exp(-\frac{1}{2\kappa \tau} || \mathbf{z} - \mathbf{z}'||) \) 定义两个输入相似的概率。图16.4展示了建模假设的示意图。

我们可以使用EM算法（第8.7.2节）最大化对数边际似然 \( \ell(\mathbf{W}, \sigma^2, \kappa^2) = \sum_n \log p(y_n | \boldsymbol{x}_n, \boldsymbol{x}'_n) \)。（我们可以不失一般性地设置 \( \kappa = 1 \)，因为它仅改变 \( \mathbf{W} \) 的尺度。）更精确地说，在E步骤中，我们计算后验 \( p(\mathbf{z}, \mathbf{z}' | \mathbf{x}, \mathbf{x}', y) \)（可以闭式求解），在M步骤中，我们求解一个加权最小二乘问题（参见第13.6.2节）。EM算法会单调地增加目标函数，且不需要像NCA（第16.2.1.2节）中使用的基于梯度的方法那样调整步长。（也可以使用变分贝叶斯（第4.6.8.3节）来拟合该模型，以及各种稀疏和非线性扩展，如[ZMY19]所讨论的。）

---

#### 16.2.2 深度度量学习

在测量高维或结构化输入之间的距离时，首先学习嵌入到一个更低维的“语义”空间非常有用，在此空间中距离更具意义，且不易受维度灾难影响（第16.1.2节）。设 $ e = f(\boldsymbol{x}; \boldsymbol{\theta}) \in \mathbb{R}^L $ 是输入的一种嵌入，保留了输入的“相关”语义信息，并设 $ \hat{e} = e / ||e||_2 $ 为其 $\ell_2$ 归一化版本。这确保所有点都位于一个超球面上。然后我们可以使用归一化欧氏距离来测量两点之间的距离：

$$  d(\boldsymbol{x}_{i},\boldsymbol{x}_{j};\boldsymbol{\theta})=||\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{j}||_{2}^{2}   \tag*{(16.7)}$$

其中值越小表示越相似；或使用余弦相似度：

$$  d(\boldsymbol{x}_{i},\boldsymbol{x}_{j};\boldsymbol{\theta})=\hat{\boldsymbol{e}}_{i}^{\top}\hat{\boldsymbol{e}}_{j}   \tag*{(16.8)}$$

其中值越大表示越相似。（余弦相似度测量两个向量之间的夹角，如图20.43所示。）这些量通过下式相关联：

$$  \begin{array}{r}{||\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{j}||_{2}^{2}=(\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{j})^{\mathsf{T}}(\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{j})=2-2\hat{\boldsymbol{e}}_{i}^{\mathsf{T}}\hat{\boldsymbol{e}}_{j}}\end{array}   \tag*{(16.9)}$$

这种整体方法称为深度度量学习（DML）。

DML的基本思想是学习一个嵌入函数，使得相似的样例彼此更接近，而不相似的样例则更远。更精确地说，我们假设有一个带标签的数据集 $ \mathcal{D} = \{(\boldsymbol{x}_i, y_i) : i = 1 : N\} $，从中可以推导出一组相似对 $ \mathcal{S} = \{(i, j) : y_i = y_j\} $。如果 $ (i, j) \in \mathcal{S} $ 但 $ (k, i) \notin \mathcal{S} $，那么我们期望 $ \boldsymbol{x}_i $ 和 $ \boldsymbol{x}_j $ 在嵌入空间中接近，而 $ \boldsymbol{x}_i $ 和 $ \boldsymbol{x}_k $ 则应该远离。下面我们讨论实现这一性质的各种方法。注意，这些方法也适用于没有类别标签的情况，只要我们另有定义相似对的途径。例如，在第19.2.4.3节中，我们讨论了自监督的表示学习方法，这些方法自动创建语义相似的配对，并学习嵌入使得这些配对比不相关的配对更接近。

在深入讨论DML之前，值得指出的是，正如[MBL20; Rot+20]所指出的，许多近期的DML方法并不如其宣称的那样好。（这些论文中的某些主张往往因不恰当的实验比较而无效，这是当代机器学习研究中的一个常见缺陷，例如参见[BLV19; LS19b]的讨论。）因此，我们重点关注（略）为古老且简单的方法，这些方法通常更为稳健。

#### 16.2.3 分类损失

假设我们有C个类别的带标签数据。那么我们可以在 $ O(NC) $ 时间内拟合一个分类模型，然后将隐藏特征重新用作嵌入函数。（通常使用倒数第二层，因为它比最终层对新类别具有更好的泛化能力。）这种方法简单且可扩展。然而，它仅仅学习将样例嵌入到决策边界的正确一侧，这并不必然导致相似样例被放置在一起而相异样例被分开。此外，若没有带标签的训练数据，此方法则无法使用。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_239_123_524_405.jpg" alt="图片" width="24%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_697_171_883_360.jpg" alt="图片" width="16%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 16.5：用于深度度量学习的网络。(a) 孪生网络。(b) 三元组网络。改编自 [KB19] 的图 5。</div>


#### 16.2.4 排序损失

本节中，我们考虑最小化排序损失，以确保相似样本之间的距离比不相似样本更近。这些方法大多不需要类别标签（尽管我们有时假设标签存在，将其作为定义相似性的一种简便记法）。

##### 16.2.4.1 成对（对比）损失与孪生网络

从相似/不相似样本对中进行表示学习的最早方法之一，是基于最小化以下对比损失 [CHL05]：

$$  \mathcal{L}(\boldsymbol{\theta};\boldsymbol{x}_{i},\boldsymbol{x}_{j})=\mathbb{I}(y_{i}=y_{j})d(\boldsymbol{x}_{i},\boldsymbol{x}_{j})^{2}+\mathbb{I}(y_{i}\neq y_{j})\left[m-d(\boldsymbol{x}_{i},\boldsymbol{x}_{j})\right]_{+}^{2}   \tag*{(16.10)}$$

其中 $[z]_{+} = \max(0, z)$ 是合页损失，$m > 0$ 是边际参数。直观上，我们希望迫使正样本对（具有相同标签）接近，而负样本对（具有不同标签）则要远离某个最小安全边际。我们在所有样本对上最小化该损失。朴素实现的时间复杂度为 $O(N^{2})$；一些加速方法参见第16.2.5节。

注意，在计算距离时，我们对两个输入 $\mathbf{x}_{i}$ 和 $\mathbf{x}_{j}$ 使用相同的特征提取器 $\mathbf{f}(\cdot;\boldsymbol{\theta})$，如图 16.5a 所示。因此得到的网络被称为 **孪生网络**（取名自暹罗双胞胎）。

##### 16.2.4.2 三元组损失

成对损失的一个缺点在于正样本对的优化与负样本对相互独立，这可能导致两者的量级不可比较。解决方法是使用 **三元组损失** [SKP15]。其定义如下：对于每个样本 $i$（称为锚点），我们找到一个相似（正）样本 $\mathbf{x}_i^\dagger$ 和一个不相似（负）样本 $\mathbf{x}_i^-$。然后对所有三元组平均最小化以下损失：

$$  \mathcal{L}(\boldsymbol{\theta};\boldsymbol{x}_{i},\boldsymbol{x}_{i}^{+},\boldsymbol{x}_{i}^{-})=[d_{\boldsymbol{\theta}}(\boldsymbol{x}_{i},\boldsymbol{x}_{i}^{+})^{2}-d_{\boldsymbol{\theta}}(\boldsymbol{x}_{i},\boldsymbol{x}_{i}^{-})^{2}+m]_{+}   \tag*{(16.11)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证。

---

直观上，这意味着我们希望锚点到正样本的距离（在某个安全间隔 m 的作用下）小于锚点到负样本的距离。我们可以使用如图 16.5b 所示的三元组网络来计算三元组损失。

朴素的最小化三元组损失需要 $ O(N^{3}) $ 的时间。在实践中，我们是在一个小批量上计算损失（选择小批量时确保锚点至少有一个相似样本和一个不相似样本，通常将小批量中的第一个样本作为锚点）。然而，该方法仍可能较慢。我们在第 16.2.5 节讨论一些加速方法。

##### 16.2.4.3 N-pairs 损失

三元组损失的一个问题是每个锚点每次只与一个负样本进行比较。这可能无法提供足够强的学习信号。解决这个问题的一个方法是创建一个多类分类问题，即为每个锚点构建一组 $N-1$ 个负样本和 1 个正样本。这被称为 N-pairs 损失 [Soh16]。更精确地，我们定义每个集合上的损失如下：

$$  \mathcal{L}(\boldsymbol{\theta};\boldsymbol{x},\boldsymbol{x}^{+},\{\boldsymbol{x}_{k}^{-}\}_{k=1}^{N-1})=\log\left(1+\sum_{k=1}^{N-1}\exp\left[\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x})^{\mathsf{T}}\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x}_{k}^{-})-\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x})^{\mathsf{T}}\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x}^{+})\right]\right)   \tag*{(16.12)}$$

$$  \begin{aligned}=-\log\frac{\exp(\hat{\boldsymbol{e}}_{\theta}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}_{\theta}(\boldsymbol{x}^{+}))}{\exp(\hat{\boldsymbol{e}}_{\theta}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}_{\theta}(\boldsymbol{x}^{+}))+\sum_{k=1}^{N-1}\exp(\hat{\boldsymbol{e}}_{\theta}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}_{\theta}(\boldsymbol{x}_{k}^{-}))}\end{aligned}   \tag*{(16.13)}$$

注意到 N-pairs 损失与 CPC 论文 [OLV18] 中使用的 InfoNCE 损失相同。在 [Che+20a] 中，他们提出了一种版本，使用温度项对相似度进行缩放；他们称之为 NT-Xent（归一化温度缩放交叉熵）损失。我们可以将温度参数视为对数据所在超球体半径的缩放。

当 N = 2 时，该损失退化为逻辑损失

$$  \mathcal{L}(\boldsymbol{\theta};\boldsymbol{x},\boldsymbol{x}^{+},\boldsymbol{x}^{-})=\log\left(1+\exp(\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x}^{-})-\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}_{\boldsymbol{\theta}}(\boldsymbol{x}^{+}))\right)   \tag*{(16.14)}$$

将此与三元组学习所使用的间隔损失（当 m = 1 时）进行比较：

$$  \mathcal{L}(\boldsymbol{\theta};\boldsymbol{x},\boldsymbol{x}^{+},\boldsymbol{x}^{-})=\max\left(0,\hat{\boldsymbol{e}}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}(\boldsymbol{x}^{-})-\hat{\boldsymbol{e}}(\boldsymbol{x})^{\top}\hat{\boldsymbol{e}}(\boldsymbol{x}^{+})+1\right)   \tag*{(16.15)}$$

关于这两个函数的比较，请参见图 4.2。

#### 16.2.5 加速排序损失优化

排序损失的主要缺点是计算损失函数的 $ O(N^{2}) $ 或 $ O(N^{3}) $ 代价，因为需要比较所有样本对或三元组。在本节中，我们讨论各种加速技巧。

##### 16.2.5.1 挖掘技术

一个关键的见解是，我们不需要对每个锚点考虑所有负样本，因为大多数负样本不具有信息量（即会产生零损失）。相反，我们可以关注那些比其最近正样本更接近锚点的负样本。这些被称为困难负样本，对于加速三元组损失尤其有用。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_199_139_1024_353.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 16.b：加速三元组损失最小化。(a) 困难负样本与容易负样本的对比。这里 a 是锚点，p 是正样本点，$ n_i $ 是负样本点。改编自文献 [KB19] 的图 4。(b) 标准三元组损失需要 $ 8 \times 3 \times 4 = 96 $ 次计算，而使用代理损失（每类一个代理）仅需 $ 8 \times 2 = 16 $ 次计算。来自文献 [Do+19] 的图 1。经 Gustavo Cerneiro 友好许可使用。</div>


更精确地说，如果 $a$ 是锚点，$p$ 是其最近的正样本，则当 $d(\boldsymbol{x}_{a}, \boldsymbol{x}_{n}) < d(\boldsymbol{x}_{a}, \boldsymbol{x}_{p})$ 且 $y_{n} \neq y_{a}$ 时，称 $n$ 为（针对 $a$ 的）困难负样本。有时一个锚点可能没有困难负样本。因此，我们可以通过考虑半困难负样本来扩大候选池，对于半困难负样本有：

$$  d(\boldsymbol{x}_{a},\boldsymbol{x}_{p})<d(\boldsymbol{x}_{a},\boldsymbol{x}_{n})<d(\boldsymbol{x}_{a},\boldsymbol{x}_{p})+m   \tag*{(16.16)}$$

其中 m > 0 是边际参数。如图 16.6a 所示。这是谷歌 FaceNet 模型 [SKP15] 使用的技术，该模型学习人脸嵌入函数，以便将相似的人脸聚类在一起，用户可为其附加姓名。

在实践中，通常从小批量内选取困难负样本。因此，这需要较大的批量大小以确保足够的多样性。或者，我们可以设置一个独立过程，随着训练过程中距离度量的演变，持续更新困难负样本候选集合。

##### 16.2.5.2 代理方法

即使采用困难负样本挖掘（第 16.2.5.1 节），三元组损失最小化仍然代价高昂。理想情况下，我们可以找到一种时间复杂度为 $ O(N) $ 的方法，就像分类损失一样。

文献 [MA+17] 提出了一种这样的方法：它测量每个锚点与代表每个类的一组 $ P $ 个代理之间的距离，而不是直接测量样本之间的距离。随着学习过程中距离度量的演变，这些代理需要在线更新。整个过程的复杂度为 $ O(NP^2) $，其中 $ P \sim C $。

最近，[Qia+19] 提出用多个原型表示每个类别，同时通过使用软三元组损失实现线性时间复杂度。

##### 16.2.5.3 优化上界

[Do+19] 提出了一种简单且快速的三元组损失优化方法。关键思路是为每个类别定义一个固定的代理或质心，然后将到代理的距离作为

---

三元组损失。

更精确地，考虑无间隔项的三元组损失的简化形式：

$$  \ell_{t}(\boldsymbol{x}_{i},\boldsymbol{x}_{j},\boldsymbol{x}_{k})=||\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{j}||-||\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{k}||   \tag*{(16.17)}$$

其中 $ \hat{e}_i = \hat{e}_\theta(\boldsymbol{x}_i) $，以此类推。利用三角形不等式，我们有

$$  \left|\left|\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{j}\right|\right|\leq\left|\left|\hat{\boldsymbol{e}}_{i}-\boldsymbol{c}_{y_{i}}\right|\right|+\left|\left|\hat{\boldsymbol{e}}_{j}-\boldsymbol{c}_{y_{i}}\right|\right|   \tag*{(16.18)}$$

$$  \left|\hat{\boldsymbol{e}}_{i}-\hat{\boldsymbol{e}}_{k}\right|\geq\left|\hat{\boldsymbol{e}}_{i}-\boldsymbol{c}_{y_{k}}\right|-\left|\hat{\boldsymbol{e}}_{k}-\boldsymbol{c}_{y_{k}}\right|   \tag*{(16.19)}$$

因此

$$  \ell_{t}(\boldsymbol{x}_{i},\boldsymbol{x}_{j},\boldsymbol{x}_{k})\leq\ell_{u}(\boldsymbol{x}_{i},\boldsymbol{x}_{j},\boldsymbol{x}_{k})\triangleq||\hat{\boldsymbol{e}}_{i}-\boldsymbol{c}_{y_{i}}||-||\hat{\boldsymbol{e}}_{i}-\boldsymbol{c}_{y_{k}}||+||\hat{\boldsymbol{e}}_{j}-\boldsymbol{c}_{y_{i}}||+||\hat{\boldsymbol{e}}_{k}-\boldsymbol{c}_{y_{k}}||   \tag*{(16.20)}$$

我们可以利用这一点为三元组损失导出一个易处理的上界，如下所示：

$$  \mathcal{L}_{t}(\mathcal{D},\mathcal{S})=\sum_{(i,j)\in\mathcal{S},(i,k)\notin\mathcal{S},i,j,k\in\{1,\ldots,N\}}\ell_{t}(\boldsymbol{x}_{i},\boldsymbol{x}_{j},\boldsymbol{x}_{k})\leq\sum_{(i,j)\in\mathcal{S},(i,k)\notin\mathcal{S},i,j,k\in\{1,\ldots,N\}}\ell_{u}(\boldsymbol{x}_{i},\boldsymbol{x}_{j},\boldsymbol{x}_{k})   \tag*{(16.21)}$$

$$  =C^{\prime}\sum_{i=1}^{N}\left(\left|\left|\boldsymbol{x}_{i}-\boldsymbol{c}_{y_{i}}\right|\right|-\frac{1}{3(C-1)}\sum_{m=1,m\neq y_{i}}^{C}\left|\left|\boldsymbol{x}_{i}-\boldsymbol{c}_{m}\right|\right|\right)\triangleq\mathcal{L}_{u}(\mathcal{D},\mathcal{S})   \tag*{(16.22)}$$

其中 $ C' = 3(C - 1)\left(\frac{N}{C} - 1\right)\frac{N}{C} $ 是一个常数，并且我们假设对于每个 $c$ 有 $\sum_{i=1}^{N} \mathbb{I}(y_i = c) = N/C$。显然，$ L_u $ 可以在 $ O(NC) $ 时间内计算。参见 Figure 16.6b 的示意图。

在 $ [Do+19] $ 中，他们证明了 $ 0 \leq \mathcal{L}_t - \mathcal{L}_u \leq \frac{N}{C^2} K $，其中 $ K $ 是依赖于质心散布的常数。为了确保该界紧致，质心应尽可能远离彼此，且它们之间的距离应尽可能相似。一个简单的确保方法是定义 $ \mathbf{c}_m $ 向量为独热向量，每个类一个。这些向量已经具有单位范数，且彼此正交。每对质心之间的距离为 $ \sqrt{2} $，这确保了上界相当紧致。

这种方法的缺点是它假设嵌入层维度为 $L = C$。有两种解决方案。首先，在训练结束后，我们可以添加一个线性投影层，将维度从 $C$ 映射到 $L \neq C$，或者我们可以取嵌入网络的倒数第二层。第二种方法是在 $L$ 维单位超球面上采样大量点（可以通过从标准正态分布采样然后归一化实现 [Mar72]），然后运行 $K$ 均值聚类（第 21.3 节），取 $K = C$。在 [Do+19] 报告的实验中，这两种方法给出了相似的结果。

有趣的是，在 $ [Rot+20] $ 中，他们表明增加 $ \pi_{intra}/\pi_{inter} $ 可以改善各种检索任务的下游性能，其中

$$  \pi_{intra}=\frac{1}{Z_{intra}}\sum_{c=1}^{C}\sum_{i\neq j:y_{i}=y_{j}=c}d(\boldsymbol{x}_{i},\boldsymbol{x}_{j})   \tag*{(16.23)}$$

是平均类内距离，而

$$  \pi_{inter}=\frac{1}{Z_{inter}}\sum_{c=1}^{C}\sum_{c^{\prime}=1}^{C}d(\boldsymbol{\mu}_{c},\boldsymbol{\mu}_{c^{\prime}})   \tag*{(16.24)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_421_125_745_327.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">图 16.7：在深度度量学习方法中加入球形嵌入约束。经张鼎毅许可使用。</div>


是平均类间距离，其中 $ \mu_c = \frac{1}{Z_c} \sum_{i:y_i=c} \hat{e}_i $ 是类别 $ c $ 样本的平均嵌入。这表明我们不仅应使质心彼此远离（以最大化分子），还应防止样本过于接近其质心（以最小化分母）；后一项在 [Do+19] 的方法中未被考虑。

#### 16.2.6 DML 的其他训练技巧

除了第 16.2.5 节的加速技巧外，还有许多其他细节对于确保良好的 DML 性能至关重要。其中许多细节在 [MBL20; Rot+20] 中进行了讨论。这里我们仅简要提及几点。

一个重要问题是如何创建小批量样本。在分类问题中（至少在类别平衡的情况下），从训练集中随机选取样本通常就足够了。然而，对于 DML，我们需要确保每个样本在小批量中既有与其相似的样本，也有与其不相似的样本。一种方法是使用困难样本挖掘技术（第 16.2.5.1 节）。另一种思路是使用基于先前学习到的嵌入的核心集方法，在每一步选取多样性的小批量样本 [Sin+20]。然而，[Rot+20] 表明，以下简单策略在创建每个批次时也效果良好：选取 B/n 个类别，然后从每个类别中随机选取 $ N_c $ 个样本，其中 B 是批次大小，$ N_c = 2 $ 是一个调优参数。

另一个重要问题是避免过拟合。由于 DML 文献中使用的大多数数据集规模较小，通常的做法是使用已在 ImageNet 上预训练的图像分类器（如 GoogLeNet（第 14.3.3 节）或 ResNet（第 14.3.4 节）），然后使用 DML 损失对模型进行微调（关于这种迁移学习的更多细节，请参见第 19.2 节）。此外，通常还会使用数据增强（参见第 19.1 节）。实际上，对于某些自监督学习方法，数据增强是创建相似对的唯一途径。

在 [ZLZ20] 中，他们提出了添加球形嵌入约束（SEC），这是一个额外的逐批次正则化项，鼓励所有样本具有相同的范数。即，该正则化器就是该批次中（未归一化）嵌入范数的经验方差。如图 16.7 所示。该正则化器可以添加到任何现有的 DML 损失中，以适度提高训练速度和稳定性，以及最终性能，其作用类似于批归一化（第 14.2.4.1 节）的使用方式。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

### 16.3 核密度估计（KDE）

本节考虑一种非参数密度估计方法，称为核密度估计（KDE）。这是一种生成模型，因为它定义了一个概率分布 $ p(\boldsymbol{x}) $，该分布可以逐点评估，并且可以从中采样以生成新数据。

#### 16.3.1 密度核

在解释KDE之前，我们必须定义“核”的含义。该术语在机器学习和统计学中有几种不同的含义。$ ^{1} $ 在本节中，我们使用一种特定类型的核，称为**密度核**。这是一个函数 $ \mathcal{K} : \mathbb{R} \to \mathbb{R}_+ $，满足 $ \int \mathcal{K}(x) dx = 1 $ 和 $ \mathcal{K}(-x) = \mathcal{K}(x) $。后一个对称性质意味着 $ \int x \mathcal{K}(x) dx = 0 $，因此

$$  \int x\mathcal{K}(x-x_{n})d x=x_{n}   \tag*{(16.25)}$$

这种核的一个简单例子是**矩形核**（boxcar kernel），即在原点附近单位区间内的均匀分布：

$$  \mathcal{K}(x)\triangleq0.5\mathbb{I}\left(\left|x\right|\leq1\right)   \tag*{(16.26)}$$

另一个例子是**高斯核**：

$$  \mathcal{K}(x)=\frac{1}{\left(2\pi\right)^{\frac{1}{2}}}e^{-x^{2}/2}   \tag*{(16.27)}$$

我们可以通过引入带宽参数 $h$ 来控制核的宽度：

$$  \mathcal{K}_{h}(x)\triangleq\frac{1}{h}\mathcal{K}(\frac{x}{h})   \tag*{(16.28)}$$

我们可以通过定义径向基函数（RBF）核来推广到向量输入：

$$  \mathcal{K}_{h}(\boldsymbol{x})\propto\mathcal{K}_{h}(||\boldsymbol{x}||)   \tag*{(16.29)}$$

对于高斯核，这变为：

$$  \mathcal{K}_{h}(\boldsymbol{x})=\frac{1}{h^{D}(2\pi)^{D/2}}\prod_{d=1}^{D}\exp(-\frac{1}{2h^{2}}x_{d}^{2})   \tag*{(16.30)}$$

尽管高斯核很流行，但它们具有无界支撑。表16.1列出了一些具有紧支撑的替代核（计算上可能更快）。这些核函数的图示见 Figure 16.8。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_399_125_764_410.jpg" alt="图像" width="31%" /></div>


<div style="text-align: center;">图 16.8：几种常见归一化核函数的对比。由 smoothingKernelPlot.ipynb 生成。</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>定义</td><td style='text-align: center; word-wrap: break-word;'>紧支撑性</td><td style='text-align: center; word-wrap: break-word;'>光滑性</td><td style='text-align: center; word-wrap: break-word;'>边界连续性</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>高斯核</td><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{K}(x)=(2\pi)^{-\frac{1}{2}}e^{-x^{2}/2} $</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>矩形核</td><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{K}(x)=\frac{1}{2}\mathbb{I}(|x|\leq1) $</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Epanechnikov 核</td><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{K}(x)=\frac{3}{4}(1-x^{2})\mathbb{I}(|x|\leq1) $</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>三立方核</td><td style='text-align: center; word-wrap: break-word;'>$ \mathcal{K}(x)=\frac{70}{81}(1-|x|^{3})^{3}\mathbb{I}(|x|\leq1) $</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>

表 16.1：一维情形下几种常见归一化核函数列表。紧支撑性=1 表示该函数在输入的有界范围内非零。光滑性=1 表示函数在其支撑区间内可微。边界连续性=1 表示函数在支撑区间的边界处也可微。

#### 16.3.2 Parzen 窗密度估计器

为了说明如何利用核函数定义非参数密度估计，我们回顾第 3.5.1 节中高斯混合模型的形式。若假设固定的球形高斯协方差和均匀的混合权重，则得到

$$  p(\boldsymbol{x}|\boldsymbol{\theta})=\frac{1}{K}\sum_{k=1}^{K}\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{k},\sigma^{2}\mathbf{I})   \tag*{(16.31)}$$

该模型的一个问题是需要指定簇的数量 $K$ 及其位置 $\mu_{k}$。替代估计这些参数的一种方法是：为每个数据点分配一个簇中心。此时模型变为

$$  p(\boldsymbol{x}|\boldsymbol{\theta})=\frac{1}{N}\sum_{n=1}^{N}\mathcal{N}(\boldsymbol{x}|\boldsymbol{x}_{n},\sigma^{2}\mathbf{I})   \tag*{(16.32)}$$

我们可以将式 (16.32) 推广为

$$  p(\boldsymbol{x}|\mathcal{D})=\frac{1}{N}\sum_{n=1}^{N}\mathcal{K}_{h}\left(\boldsymbol{x}-\boldsymbol{x}_{n}\right)   \tag*{(16.33)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_245_120_514_354.jpg" alt="图片" width="23%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_652_119_922_346.jpg" alt="图片" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_245_368_515_590.jpg" alt="图片" width="23%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_652_372_921_592.jpg" alt="图片" width="23%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">图 16.9：基于 6 个数据点（以 x 标记）估计的一维非参数（Parzen）密度估计器。顶部行：均匀核。底部行：高斯核。左列：带宽参数 h = 1。右列：带宽参数 h = 2。改编自 http://en.wikipedia.org/wiki/Kernel_density_estimation。由 parzen_window_demo2.ipynb 生成。</div>

其中 $ \mathcal{K}_{h} $ 是一个密度核。这被称为 Parzen 窗密度估计器，或核密度估计（KDE）。

与参数模型相比，其优势在于无需进行模型拟合（除了选择 h 之外，这在第 16.3.3 节中讨论），也无需选择聚类中心的数量。缺点是该模型需要大量内存（需要存储所有数据）且评估时间较长。

图 16.9 展示了一维情况下两种核的 KDE。在上图中，我们使用矩形窗核；得到的模型仅统计落在每个 $ x_{n} $ 周围大小为 h 的区间内的数据点数量，从而得到一个分段常数密度。在下图中，我们使用高斯核，得到更平滑的密度。

#### 16.3.3 如何选择带宽参数

从图 16.9 可以看出，带宽参数 h 对学习到的分布有很大影响。我们可以将其视为控制模型的复杂度。

在一维数据的情况下，当假设“真实”数据生成分布为高斯分布时，可以证明 [BA97a] 对于高斯核而言，最优带宽（从均方误差最小化的角度）为……

---

最小化频率风险）由下式给出：$ h = \sigma\left(\frac{4}{3N}\right)^{1/3} $。我们可以通过先计算中位数绝对偏差 $\text{median}( |x - \text{median}(x)| )$，然后使用 $ \hat{\sigma} = 1.4826 $ MAD 来得到标准差的一个稳健近似。如果数据有 $ D $ 维，我们可以分别估计每一维的 $ h_d $，然后设置 $ h = (\prod_{d=1}^D h_d)^{1/D} $。

#### 16.3.4 从核密度估计到K近邻分类

在第16.1节中，我们将K近邻分类器作为一种启发式分类方法进行了讨论。有趣的是，我们可以将其推导为一个生成式分类器，其中类条件密度 $ p(\boldsymbol{x}|y=c) $ 使用核密度估计（KDE）进行建模。我们不再使用固定的带宽并统计落入以数据点为中心的超立方体内的数据点数量，而是允许每个数据点的带宽或体积不同。具体来说，我们围绕 $\boldsymbol{x}$ "生长" 一个体积，直到遇到 $K$ 个数据点（无论其类别标签如何）。这称为**气球核密度估计器**[TS92]。设所得体积大小为 $ V(\boldsymbol{x}) $（此前为 $ h^D $），并且该体积内属于类别 $c$ 的样本有 $ N_c(\boldsymbol{x}) $ 个。那么我们可以如下估计类条件密度：

$$ p(\boldsymbol{x}|y=c,\mathcal{D})=\frac{N_{c}(\boldsymbol{x})}{N_{c}V(\boldsymbol{x})} \tag*{(16.34)} $$

其中 $ N_{c} $ 是整个数据集中类别 $c$ 的样本总数。如果我们取类别先验为 $ p(y = c) = N_{c}/N $，则类别后验由下式给出：

$$ p(y=c|\boldsymbol{x},\mathcal{D})=\frac{\frac{N_{c}(\boldsymbol{x})}{N_{c}V(\boldsymbol{x})}\frac{N_{c}}{N}}{\sum_{c^{\prime}}\frac{N_{c^{\prime}}(\boldsymbol{x})}{N_{c^{\prime}}V(\boldsymbol{x})}\frac{N_{c^{\prime}}}{N}}=\frac{N_{c}(\boldsymbol{x})}{\sum_{c^{\prime}}N_{c^{\prime}}(\boldsymbol{x})}=\frac{N_{c}(\boldsymbol{x})}{K}=\frac{1}{K}\sum_{n\in N_{K}(\boldsymbol{x},\mathcal{D})}\mathbb{I}(y_{n}=c) \tag*{(16.35)} $$

其中我们利用了 $ \sum_c N_c(\boldsymbol{x}) = K $ 这一事实，因为我们在每个点周围总共选择了 $ K $ 个点（不考虑类别）。这与式(16.1)一致。

#### 16.3.5 核回归

正如核密度估计可用于生成式分类器（见第16.1节）一样，它也可用于回归的生成式模型，下文将进行讨论。

##### 16.3.5.1 均值的Nadaraya-Watson估计器

在回归中，我们的目标是计算条件期望

$$ \mathbb{E}\left[y|\boldsymbol{x},\mathcal{D}\right]=\int y p(y|\boldsymbol{x},\mathcal{D})d y=\frac{\int y p(\boldsymbol{x},y|\mathcal{D})d y}{\int p(\boldsymbol{x},y|\mathcal{D})d y} \tag*{(16.36)} $$

如果我们对 $ p(y, \boldsymbol{x}|\mathcal{D}) $ 使用**多元正态分布（MVN）**，则会得到等价于线性回归的结果，如第11.2.3.5节所示。然而，假设 $ p(y, \boldsymbol{x}|\mathcal{D}) $ 为高斯分布是相当局限的。我们可以使用核密度估计来更精确地近似联合密度 $ p(\boldsymbol{x}, y|\mathcal{D}) $ 如下：

$$ p(y,\boldsymbol{x}|\mathcal{D})\approx\frac{1}{N}\sum_{n=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})\mathcal{K}_{h}(y-y_{n}) \tag*{(16.37)} $$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_414_151_742_393.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">图16.10: 使用高斯核进行一维核回归的示例。由 kernelRegressionDemo.ipymb 生成。</div>


因此

$$  \mathbb{E}\left[y|\boldsymbol{x},\mathcal{D}\right]=\frac{\frac{1}{N}\sum_{n=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})\int y\mathcal{K}_{h}(y-y_{n})d y}{\frac{1}{N}\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})\int\mathcal{K}_{h}(y-y_{n^{\prime}})d y}   \tag*{(16.38)}$$

我们可以利用 $ \int y \mathcal{K}_h(y - y_n) dy = y_n $（根据公式(16.25)）来简化分子。利用密度核积分为1的事实，即 $ \int \mathcal{K}_h(y - y_n) dy = 1 $，可以简化分母。因此

$$  \mathbb{E}\left[y|\boldsymbol{x},\mathcal{D}\right]=\frac{\sum_{n=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})y_{n}}{\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})}=\sum_{n=1}^{N}y_{n}w_{n}(\boldsymbol{x})   \tag*{(16.39)}$$

$$  w_{n}(\boldsymbol{x})\triangleq\frac{\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})}{\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})}   \tag*{(16.40)}$$

可以看出，预测值只是训练点输出的加权和，其权重取决于 $\boldsymbol{x}$ 与存储的训练点之间的相似程度。该方法称为 **核回归**、**核平滑** 或 Nadaraya-Watson (N-W) 模型。图16.10给出了一个使用高斯核的示例。

在第17.2.3节中，我们将讨论核回归与高斯过程回归之间的联系。

##### 16.3.5.2 方差的估计量

有时，除了预测均值外，计算预测方差也很有用。我们可以通过以下关系来实现：

$$  \mathbb{V}\left[y|\boldsymbol{x},\mathcal{D}\right]=\mathbb{E}\left[y^{2}|\boldsymbol{x},\mathcal{D}\right]-\mu(\boldsymbol{x})^{2}   \tag*{(16.41)}$$

---

其中，$ \mu(\boldsymbol{x}) = \mathbb{E}\left[y|\boldsymbol{x},\mathcal{D}\right] $ 是 N-W 估计。如果我们使用方差为 $ \sigma^2 $ 的高斯核，则可以如下计算 $ \mathbb{E}\left[y^2|\boldsymbol{x},\mathcal{D}\right] $：

$$  \begin{aligned}\mathbb{E}\left[y^{2}|\boldsymbol{x},\mathcal{D}\right]&=\frac{\sum_{n=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})\int y^{2}\mathcal{K}_{h}(y-y_{n})dy}{\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})\int\mathcal{K}_{h}(y-y_{n^{\prime}})dy}\\&=\frac{\sum_{n=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})(\sigma^{2}+y_{n}^{2})}{\sum_{n^{\prime}=1}^{N}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n^{\prime}})}\end{aligned}   \tag*{(16.42)}$$

其中我们使用了以下事实：

$$  \int y^{2}\mathcal{N}(y|y_{n},\sigma^{2})d y=\sigma^{2}+y_{n}^{2}   \tag*{(16.44)}$$

将方程(16.43)与方程(16.41)结合，得到：

$$  \mathbb{V}\left[y|\boldsymbol{x},\mathcal{D}\right]=\sigma^{2}+\sum_{n=1}^{N}w_{n}(\boldsymbol{x})y_{n}^{2}-\mu(\boldsymbol{x})^{2}   \tag*{(16.45)}$$

这与文献[BA10]中的方程8一致（除了初始的 $\sigma^{2}$ 项）。

##### 16.3.5.3 局部加权回归

我们可以去掉方程(16.39)中的归一化项，得到：

$$  \mu(\boldsymbol{x})=\sum_{n=1}^{N}y_{n}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})   \tag*{(16.46)}$$

这仅仅是观察响应的加权和，其中权重取决于测试输入 x 与训练点 $ x_{n} $ 的相似程度。

与其仅仅对存储的响应 $ y_{n} $ 进行插值，我们可以在每个训练点周围拟合一个局部线性模型：

$$  \mu(\boldsymbol{x})=\min_{\boldsymbol{\beta}}\sum_{n=1}^{N}[y_{n}-\boldsymbol{\beta}^{\mathrm{T}}\boldsymbol{\phi}(\boldsymbol{x}_{n})]^{2}\mathcal{K}_{h}(\boldsymbol{x}-\boldsymbol{x}_{n})   \tag*{(16.47)}$$

其中 $\phi(\boldsymbol{x})=[1,\boldsymbol{x}]$。这被称为局部线性回归（LRR）或局部加权散点图平滑，通常简称为 LOWESS 或 LOESS [CD88]。这种方法常用于在散点图上标注局部趋势线。

---

请提供您需要翻译的英文学术论文 Markdown 文本。

---

在本章中，我们考虑回归和分类的非参数方法。这类方法不假设预测函数具有固定的参数形式，而是尝试直接从数据中估计函数本身（而非参数）。其核心思想是：我们在固定的 $N$ 个点处观测到函数值，即对于 $n = 1 : N$，有 $y_n = f(\boldsymbol{x}_n)$，其中 $f$ 是未知函数。因此，要预测一个新点（例如 $\boldsymbol{x}_*$）上的函数值，我们只需比较 $\boldsymbol{x}_*$ 与每个训练点 $\{x_n\}$ 的“相似度”，然后预测 $f(\boldsymbol{x}_*)$ 是 $\{f(\boldsymbol{x}_n)\}$ 值的某种加权组合。因此，为了在测试时进行预测，我们可能需要“记住”整个训练集 $\mathcal{D} = \{(\boldsymbol{x}_n, y_n)\}$——我们无法将 $\mathcal{D}$ “压缩”成一个固定大小的参数向量。

用于预测的权重由 $\mathbf{x}_*$ 与每个 $\mathbf{x}_n$ 之间的相似度决定，这种相似度是通过一种称为核函数（kernel function）的特殊函数 $\mathcal{K}(\mathbf{x}_n, \mathbf{x}_*) \geq 0$ 来计算的，我们将在第17.1节中解释。这种方法类似于RBF网络（第13.6.1节），区别在于我们直接使用数据点 $\{\mathbf{x}_*\}$ 作为“锚点”，而不是学习RBF质心 $\{\mathbf{u}_n\}$。

在第17.2节中，我们讨论一种称为高斯过程（Gaussian processes）的方法，它允许我们使用核函数来定义函数上的先验，并利用数据更新得到函数上的后验。或者，我们也可以将相同的核函数与一种称为支持向量机（Support Vector Machines）的方法结合使用，以计算函数的MAP估计，这将在第17.3节中说明。

### 17.1 Mercer核

非参数方法的关键在于，我们需要一种对两个输入向量相似度的先验知识进行编码的方式。如果我们知道 $\boldsymbol{x}_{i}$ 与 $\boldsymbol{x}_{j}$ 相似，那么我们可以鼓励模型在两个位置上的预测输出（即 $f(\boldsymbol{x}_{i})$ 和 $f(\boldsymbol{x}_{j})$）也相似。

为了定义相似度，我们引入核函数的概念。“核”这个词在数学中有许多不同的含义，包括密度核（第16.3.1节）、马尔可夫链的转移核（第3.6.1.2节）以及卷积核（第14.1节）。这里我们考虑的是Mercer核，也称为正定核（positive definite kernel）。它是任意这样的对称函数 $\mathcal{K} : \mathcal{X} \times \mathcal{X} \to \mathbb{R}^+$，使得对于任意 $N$ 个（互不相同的）点 $\mathbf{x}_i \in \mathcal{X}$ 和任意实数 $c_i \in \mathbb{R}$，都有

$$ \sum_{i=1}^{N}\sum_{j=1}^{N}\mathcal{K}(\boldsymbol{x}_{i},\boldsymbol{x}_{j})c_{i}c_{j}\geq0 \tag*{(17.1)}$$

（我们假设 $\mathcal{K}(\mathbf{x}_i, \mathbf{x}_j) > 0$，因此上述等式仅在所有 $c_i = 0$ 时成立。）

---

理解该条件的另一种方式如下。给定一组 $N$ 个数据点，我们将 Gram 矩阵定义为如下 $N \times N$ 相似度矩阵：

$$  \mathbf{K}=\begin{pmatrix}\mathcal{K}(\mathbf{x}_{1},\mathbf{x}_{1})&\cdots&\mathcal{K}(\mathbf{x}_{1},\mathbf{x}_{N})\\&\vdots&\\ \mathcal{K}(\mathbf{x}_{N},\mathbf{x}_{1})&\cdots&\mathcal{K}(\mathbf{x}_{N},\mathbf{x}_{N})\end{pmatrix}   \tag*{(17.2)}$$

我们称 $K$ 为 Mercer 核当且仅当对于任意一组（互异的）输入 $\{x_i\}_{i=1}^N$，Gram 矩阵都是正定的。

实值输入中最广泛使用的核是平方指数核（SE），也称为指数化二次型核（EQ）、高斯核或 RBF 核。其定义为

$$  \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=\exp\left(-\frac{\left|\left|\boldsymbol{x}-\boldsymbol{x}^{\prime}\right|\right|^{2}}{2\ell^{2}}\right)   \tag*{(17.3)}$$

这里 $\ell$ 对应核的长度尺度，即我们期望差异起作用的距离。这被称为带宽参数。RBF 核通过（缩放后的）欧氏距离度量 $\mathbb{R}^D$ 中两个向量之间的相似性。在 17.1.2 节中，我们将讨论其他几种核。

在 17.2 节中，我们将展示如何使用核来定义函数上的先验和后验。基本思想是：如果 $\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}')$ 很大，意味着输入相似，那么我们期望函数的输出也相似，因此 $f(\boldsymbol{x}) \approx f(\boldsymbol{x}')$。更准确地说，我们学到的关于 $f(\boldsymbol{x})$ 的信息将有助于预测所有与 $\boldsymbol{x}$ 相关且因此使 $\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}')$ 较大的 $\boldsymbol{x}'$ 上的 $f(\boldsymbol{x}')$。

在 17.3 节中，我们将展示如何使用核从欧氏距离推广到更一般的距离概念，从而可以在隐式特征空间（而非输入空间）中使用诸如线性判别分析之类的几何方法。

#### 17.1.1 Mercer 定理

回顾 7.4 节，任何正定矩阵 $\mathbf{K}$ 都可以表示为特征分解的形式 $\mathbf{K} = \mathbf{U}^\top \mathbf{\Lambda} \mathbf{U}$，其中 $\mathbf{\Lambda}$ 是特征值 $\lambda_i > 0$ 的对角矩阵，$\mathbf{U}$ 是包含特征向量的矩阵。现在考虑 $\mathbf{K}$ 的元素 $(i, j)$：

$$  k_{i j}=(\mathbf{\Lambda}^{\frac{1}{2}}\mathbf{U}_{:i})^{\mathsf{T}}(\mathbf{\Lambda}^{\frac{1}{2}}\mathbf{U}_{:j})   \tag*{(17.4)}$$

其中 $\mathbf{U}_{:i}$ 是 $\mathbf{U}$ 的第 $i$ 列。如果定义 $\phi(\boldsymbol{x}_i) = \boldsymbol{\Lambda}^{\frac{1}{2}} \mathbf{U}_{:i}$，那么我们可以写成

$$  k_{ij}=\phi(\boldsymbol{x}_{i})^{\top}\phi(\boldsymbol{x}_{j})=\sum_{m}\phi_{m}(\boldsymbol{x}_{i})\phi_{m}(\boldsymbol{x}_{j})   \tag*{(17.5)}$$

因此我们看到，核矩阵中的条目可以通过对由核矩阵的特征向量隐式定义的某些特征向量计算内积得到。这个思想可以推广到核函数，而不仅仅是核矩阵；这一结果称为 Mercer 定理。

例如，考虑二次核 $\mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = \langle \boldsymbol{x}, \boldsymbol{x}' \rangle^2$。在二维情况下，我们有

$$  \mathcal{K}(\boldsymbol{x},\boldsymbol{x}^{\prime})=(x_{1}x_{1}^{\prime}+x_{2}x_{2}^{\prime})^{2}=x_{1}^{2}(x_{1}^{\prime})^{2}+2x_{1}x_{2}x_{1}^{\prime}x_{2}^{\prime}+x_{2}^{2}(x_{2}^{\prime})^{2}   \tag*{(17.6)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_226_124_540_405.jpg" alt="图像" width="27%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_635_126_942_405.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 17.1：来自具有 ARD 核的高斯过程的函数样本。(a) $ \ell_1 = \ell_2 = 1 $，两个维度都对响应有贡献。(b) $ \ell_1 = 1 $，$ \ell_2 = 5 $，第二个维度基本被忽略。改编自 [RW06] 的图 5.1。由 gprDemoArd.ipynb 生成。</div>


我们可以将其写为 $ \mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = \phi(\boldsymbol{x})^\top \phi(\boldsymbol{x}) $，如果定义 $ \phi(x_1, x_2) = [x_1^2, \sqrt{2}x_1x_2, x_2^2] \in \mathbb{R}^3 $。这样就将二维输入 $ x $ 嵌入到一个三维特征空间 $ \phi(\boldsymbol{x}) $ 中。

现在考虑 RBF 核。在这种情况下，对应的特征表示是无限维的（详见第 17.2.9.3 节）。然而，通过使用核函数，我们可以避免处理无限维向量。

#### 17.1.2 一些流行的 Mercer 核

在以下各节中，我们介绍一些流行的 Mercer 核。更多细节可参见 [Will14] 和 https://www.cs.toronto.edu/~duvenaud/cookbook/。

##### 17.1.2.1 针对实值向量的平稳核

对于实值输入 $ \mathcal{X} = \mathbb{R}^D $，通常使用平稳核，其形式为 $ \mathcal{K}(\boldsymbol{x}, \boldsymbol{x}') = \mathcal{K}(||\boldsymbol{x} - \boldsymbol{x}'||) $；因此该值仅取决于输入之间的逐元素差异。RBF 核是一种平稳核。下面我们给出一些其他例子。

##### ARD 核

我们可以通过将欧氏距离替换为马氏距离来推广 RBF 核，如下所示：

$$  \mathcal{K}(\boldsymbol{r})=\sigma^{2}\exp\left(-\frac{1}{2}\boldsymbol{r}^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}\boldsymbol{r}\right)   \tag*{(17.7)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_262_129_915_316.jpg" alt="图像" width="56%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 17.2: 从具有 Matern 核的高斯过程中采样的函数。(a) $ \nu = 5/2 $。(b) $ \nu = 1/2 $。由 gpKernelPlot.ipynb 生成。</div>


其中 $ \boldsymbol{r} = \boldsymbol{x} - \boldsymbol{x}' $。如果 $ \Sigma $ 是对角矩阵，则可以写成

$$  \mathcal{K}(\boldsymbol{r};\boldsymbol{\ell},\sigma^{2})=\sigma^{2}\exp\left(-\frac{1}{2}\sum_{d=1}^{D}\frac{1}{\ell_{d}^{2}}r_{d}^{2}\right)=\prod_{d=1}^{D}\mathcal{K}(r_{d};\ell_{d},\sigma^{2/D})   \tag*{(17.8)}$$

其中

$$  \mathcal{K}(r;\ell,\tau^{2})=\tau^{2}\exp\left(-\frac{1}{2}\frac{1}{\ell^{2}}r^{2}\right)   \tag*{(17.9)}$$

我们可以将 $ \sigma^2 $ 解释为整体方差，将 $ \ell_d $ 解释为定义维度 $ d $ 的特征长度尺度。如果 $ d $ 是一个无关的输入维度，则可以将 $ \ell_d $ 设为 $ \infty $，从而忽略对应维度。这被称为**自动相关确定**（automatic relevancy determination, ARD，第 11.7.7 节）。因此，相应的核被称为 ARD 核。图 17.1 展示了使用这一先验从高斯过程中采样的一些二维函数。

##### Matern 核

SE 核生成的函数无穷可微，因此非常平滑。对于许多应用，使用 **Matern** 核效果更好，它能够生成“更粗糙”的函数，从而在不使整体长度尺度变得非常小的情况下，更好地建模局部的“抖动”。

Matern 核具有如下形式：

$$  \mathcal{K}(r;\nu,\ell)=\frac{2^{1-\nu}}{\Gamma(\nu)}\left(\frac{\sqrt{2\nu}r}{\ell}\right)^{\nu}K_{\nu}\left(\frac{\sqrt{2\nu}r}{\ell}\right)   \tag*{(17.10)}$$

其中 $ K_\nu $ 是修正贝塞尔函数，$ \ell $ 是长度尺度。从该高斯过程中采样的函数是 $ k $ 次可微的，当且仅当 $ \nu > k $。当 $ \nu \to \infty $ 时，它趋近于 SE 核。