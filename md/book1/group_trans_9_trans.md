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

<div style="text-align: center;"><img src="imgs/img_in_chart_box_158_119_1015_334.jpg" alt="图像" width="74%" /></div>


<div style="text-align: center;">图 12.2：保险索赔预测的校准图。由 poisson regression insurance.ipynb 生成。</div>


低估了测试集中的总索赔数为 10,693，而真实值为 11,935。泊松模型的校准效果更好（即，当该模型预测样本将具有高索赔率时，它们实际上确实具有高索赔率），并且它预测的总索赔数为 11,930。

---

请提供需要翻译的英文Markdown文本。

---

第三部分

深度神经网络

---

你是一位专业的学术翻译助手，负责将英文学术论文的 Markdown 文本翻译为中文。

---

# 13 面向表格数据的神经网络

### 13.1 引言

在第二部分中，我们讨论了用于回归和分类的线性模型。特别地，在第10章中，我们讨论了逻辑回归，其在二分类情形下对应模型 $ p(y|\boldsymbol{x},\boldsymbol{w}) = \text{Ber}(y|\sigma(\boldsymbol{w}^\top\boldsymbol{x})) $，而在多分类情形下对应模型 $ p(y|\boldsymbol{x},\boldsymbol{W}) = \text{Cat}(y|\text{softmax}(\boldsymbol{W}\boldsymbol{x})) $。在第11章中，我们讨论了线性回归，其对应模型 $ p(y|\boldsymbol{x},\boldsymbol{w}) = \mathcal{N}(y|\boldsymbol{w}^\top\boldsymbol{x},\sigma^2) $。在第12章中，我们讨论了广义线性模型，将这些模型推广到其他类型的输出分布，例如泊松分布。然而，所有这些模型都假设输入-输出映射是线性的，这是一个很强的假设。

增强此类模型灵活性的一种简单方法是进行特征变换，即将 $ \boldsymbol{x} $ 替换为 $ \phi(\boldsymbol{x}) $。例如，我们可以使用多项式变换，在一维情况下由 $ \phi(x) = [1, x, x^2, x^3, \ldots] $ 给出，正如我们在第1.2.2.2节中所讨论。这有时被称为基函数展开。现在模型变为

$$  f(x;\theta)=\mathbf{W}\phi(x)+b   \tag*{(13.1)}$$

它在参数 $ \boldsymbol{\theta} = (\mathbf{W}, \mathbf{b}) $ 上仍然是线性的，这使得模型拟合变得容易（因为负对数似然是凸的）。然而，必须手动指定特征变换是非常受限的。

一个自然的扩展是赋予特征提取器自身的参数 $ \theta_{2} $，得到

$$  f(\boldsymbol{x};\boldsymbol{\theta})=\mathbf{W}\boldsymbol{\phi}(\boldsymbol{x};\boldsymbol{\theta}_{2})+\boldsymbol{b}   \tag*{(13.2)}$$

其中 $ \boldsymbol{\theta} = (\boldsymbol{\theta}_{1}, \boldsymbol{\theta}_{2}) $，且 $ \boldsymbol{\theta}_{1} = (\mathbf{W}, \mathbf{b}) $。显然，我们可以递归地重复这一过程，以创建越来越复杂的函数。若组合 L 个函数，我们得到

$$  f(x;\boldsymbol{\theta})=f_{L}(f_{L-1}(\cdots(f_{1}(x))\cdots))   \tag*{(13.3)}$$

其中 $ f_{\ell}(\boldsymbol{x}) = f(\boldsymbol{x}; \boldsymbol{\theta}_{\ell}) $ 是第 $ \ell $ 层的函数。这就是深度神经网络（DNN）背后的关键思想。

术语“DNN”实际上涵盖了一个更大的模型家族，其中我们将可微函数组合成任意类型的有向无环图（DAG），将输入映射到输出。方程(13.3)是最简单的例子，其中DAG是一条链。这被称为前馈神经网络（FFNN）或多层感知机（MLP）。

MLP假设输入是一个固定维度的向量，例如 $ \boldsymbol{x} \in \mathbb{R}^D $。通常将这类数据称为“结构化数据”或“表格数据”，因为数据通常存储为一个 $ N \times D $ 的设计矩阵中。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>$ x_{1} $</td><td style='text-align: center; word-wrap: break-word;'>$ x_{2} $</td><td style='text-align: center; word-wrap: break-word;'>y</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">表13.1：XOR（异或）函数的真值表，$ y = x_1 \perp x_2 $</div>

矩阵中，每一列（特征）都有特定含义，例如身高、体重、年龄等。在后续章节中，我们将讨论其他更适合图像和文本等“非结构化数据”的DNN类型，这些数据的输入尺寸可变，且每个单独元素（如像素或单词）通常本身并无意义。$ ^{1} $具体来说，第14章将介绍专为处理图像而设计的卷积神经网络（CNN）；第15章将介绍专为处理序列而设计的循环神经网络（RNN）和Transformer；第23章将介绍专为处理图数据而设计的图神经网络（GNN）。

尽管DNN能够表现良好，但通常需要处理大量工程细节才能获得较好的性能。其中部分细节在本书的补充材料（可访问probml.ai获取）中有所讨论。此外，还有多种其他书籍更深入地涵盖了该主题（例如[Zha+20; Cho21; Gér19; GBC16; Raf22]），以及众多在线课程。如需更理论化的处理，可参见例如[Ber+21; Cal20; Aro+21; RY21]。

### 13.2 多层感知机（MLP）

在第10.2.5节中，我们解释了感知机是逻辑回归的一种确定性版本。具体来说，它是如下形式的映射：

$$  f(\boldsymbol{x};\boldsymbol{\theta})=\mathbb{I}\left(\boldsymbol{w}^{\top}\boldsymbol{x}+b\geq0\right)=H(\boldsymbol{w}^{\top}\boldsymbol{x}+b)   \tag*{(13.4)}$$

其中$ H(a) $是Heaviside阶跃函数，也称为线性阈值函数。由于感知机所表示的决策边界是线性的，其表达能力非常有限。1969年，Marvin Minsky和Seymour Papert出版了著名的《感知机》一书[MP69]，书中列举了大量感知机无法解决的模式识别问题。下面我们给出一个具体例子，随后讨论如何解决该问题。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_234_201_519_402.jpg" alt="图像" width="24%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_603_143_969_404.jpg" alt="图像" width="31%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图13.1：(a) 说明了XOR函数不是线性可分的，但可以通过使用Heaviside激活函数的两层模型来分离。改编自[Gér19]的图10.6。由 xor\_heaviside.ipymb 生成。(b) 一个具有一个隐藏层的神经网络，其权重被手动构造以实现XOR函数。$ h_{1} $ 是AND函数，$ h_{2} $ 是OR函数。偏置项通过来自值为1的常数节点的权重实现。</div>


#### 13.2.1 XOR问题

《感知机》一书中最著名的例子之一是XOR问题。这里的目标是学习一个函数，计算其两个二进制输入的异或。该函数的真值表见表13.1。我们在图13.1a中可视化了该函数。显然，数据不是线性可分的，因此感知机无法表示这种映射。

然而，我们可以通过将多个感知机堆叠在一起来克服这个问题。这被称为多层感知机（MLP）。例如，为了解决XOR问题，我们可以使用图13.1b所示的MLP。它由三个感知机构成，分别记为 $ h_1 $、$ h_2 $ 和 $ y $。标记为 $ x $ 的节点是输入，标记为1的节点是常数项。节点 $ h_1 $ 和 $ h_2 $ 被称为隐藏单元，因为它们的值在训练数据中未被观察到。

第一个隐藏单元通过适当设置的权重计算 $ h_1 = x_1 \wedge x_2 $。（这里 $ \wedge $ 是AND操作。）具体来说，它从 $ x_1 $ 和 $ x_2 $ 接收输入，两者权重均为1.0，但有一个-1.5的偏置项（这是通过一条权重为-1.5的“线”实现的，该线来自一个值固定为1的虚拟节点）。因此，当且仅当 $ x_1 $ 和 $ x_2 $ 都为1时，$ h_1 $ 才激活，因为此时

$$  \boldsymbol{w}_{1}^{\mathsf{T}}\boldsymbol{x}-b_{1}=[1.0,1.0]^{\mathsf{T}}[1,1]-1.5=0.5>0   \tag*{(13.5)}$$

---

类似地，第二个隐藏单元计算 $h_2 = x_1 \vee x_2$，其中 $\vee$ 表示逻辑或运算，第三个隐藏单元计算输出 $y = \overline{h_1} \wedge h_2$，其中 $\overline{h} = \neg h$ 表示逻辑非运算。因此，$y$ 的计算结果为

$$ y=f(x_{1},x_{2})=\overline{(x_{1}\wedge x_{2})}\wedge(x_{1}\vee x_{2}) \tag*{(13.6)}$$

这等价于异或函数。

通过推广这一示例，我们可以证明多层感知机能够表示任意逻辑函数。然而，我们显然希望避免手动指定权重和偏置。在本章后续部分，我们将讨论如何从数据中学习这些参数。

#### 13.2.2 可微的多层感知机

我们在 13.2.1 节讨论的多层感知机被定义为一组感知机的堆叠，其中每个感知机都涉及不可微的亥维赛函数。这使得此类模型难以训练，因此它们从未被广泛使用。但假设我们将亥维赛函数 $H: \mathbb{R} \to \{0,1\}$ 替换为一个可微的激活函数 $\varphi: \mathbb{R} \to \mathbb{R}$。更准确地说，我们定义每一层 $l$ 的隐藏单元 $z_l$ 为上一层隐藏单元经过线性变换后再逐元素通过该激活函数的结果：

$$ \boldsymbol{z}_{l}=f_{l}(\boldsymbol{z}_{l-1})=\varphi_{l}\left(\boldsymbol{b}_{l}+\mathbf{W}_{l}\boldsymbol{z}_{l-1}\right) \tag*{(13.7)}$$

或者以标量形式表示为

$$ z_{kl}=\varphi_{l}\left(b_{kl}+\sum_{j=1}^{K_{l-1}}w_{lkj}z_{jl-1}\right) \tag*{(13.8)}$$

传递给激活函数的量称为预激活值：

$$ a_{l}=b_{l}+\mathbf{W}_{l}z_{l-1} \tag*{(13.9)}$$

因此 $z_{l} = \varphi_{l}(a_{l})$。

如果我们将 $L$ 个这样的函数按式 (13.3) 组合起来，那么我们可以利用链式法则（也称为反向传播，详见 13.3 节）计算输出相对于每一层参数的梯度。（这对任何类型的可微激活函数都成立，尽管某些类型的效果优于其他类型，我们将在 13.2.3 节讨论这一点。）然后，我们可以将梯度传递给优化器，从而最小化某个训练目标（详见 13.4 节）。正因如此，术语"多层感知机"几乎总是指这种可微形式的模型，而非历史上使用不可微线性阈值单元的版本。

#### 13.2.3 激活函数

我们可以自由地在每一层使用任何类型的可微激活函数。然而，如果使用线性激活函数 $\varphi_\ell(a) = c_\ell a$，那么整个模型将退化为一个普通的线性模型。原因如下：式 (13.3) 变为

$$ f(\boldsymbol{x};\boldsymbol{\theta})=\mathbf{W}_{L}c_{L}(\mathbf{W}_{L-1}c_{L-1}(\cdots(\mathbf{W}_{1}\boldsymbol{x})\cdots))\propto\mathbf{W}_{L}\mathbf{W}_{L-1}\cdots\mathbf{W}_{1}\boldsymbol{x}=\mathbf{W}^{\prime}\boldsymbol{x} \tag*{(13.10)}$$

《概率机器学习：导论》。在线版本。2024年11月23日。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_199_135_509_378.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_627_133_937_378.jpg" alt="图像" width="26%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 13.2: (a) Sigmoid 函数在输入接近 0 时呈线性，但在大的正负输入下趋于饱和的示意图。改编自 [Gér19] 的 11.1 节。(b) 一些神经网络激活函数的图像。由 activation_fun_plot.ipynb 生成。</div>


为简化符号，我们省略了偏置项。因此，使用非线性激活函数至关重要。

在神经网络早期，常用选择是使用 sigmoid（逻辑）函数，它可以看作是感知机中使用的 Heaviside 函数的平滑近似：

$$  \sigma(a)=\frac{1}{1+e^{-a}}   \tag*{(13.11)}$$

然而，如图 13.2a 所示，sigmoid 函数对于大的正输入 **饱和** 于 1，对于大的负输入饱和于 0。另一个常见选择是 tanh 函数，它具有类似形状，但在 -1 和 +1 处饱和。参见图 13.2b。

在饱和区域中，输出相对于输入的梯度接近于零，因此来自更高层的任何梯度信号都无法传播回更早的层。这称为 **梯度消失问题**，使得使用梯度下降训练模型变得困难（详见第 13.4.2 节）。训练深度模型的关键之一在于使用非饱和激活函数。已有多种不同的函数被提出。最常用的是修正线性单元（Rectified Linear Unit, ReLU），由 [GBB11; KSH12] 提出。其定义为

$$  \operatorname{ReLU}(a)=\max(a,0)=a\mathbb{I}\left(a>0\right)   \tag*{(13.12)}$$

ReLU 函数简单地“关闭”负输入，而正输入保持不变：其图像如图 13.2b 所示，更多细节见第 13.4.3 节。

当神经网络用于表示定义在连续输入空间（如时间点 $f(t)$ 或三维空间 $f(x,y,z)$）上的函数时，通常被称为 **神经隐式表示**（neural implicit representation）或基于坐标的表示（coordinate based representation）用于表示底层信号。在这种情况下，为了忠实表示信号，捕获高频信息通常很重要。不幸的是，MLP 对低频函数存在固有偏好 $ [\text{Tan}+20; \text{RML22}] $。一个简单的解决方案是使用正弦函数 $\sin(a)$ 作为非线性激活函数，以替代 ReLU，如 $ [\text{Sit}+20]^{2} $ 所述。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_176_114_989_554.jpg" alt="图像" width="70%" /></div>


<div style="text-align: center;">图 13.3: 一个带有2个隐藏层的MLP应用于来自2个类别的二维点集（左上角所示）。每个隐藏单元相关的可视化图显示了网络中该部分的决策边界。最终输出显示在右侧。输入为 $ \mathbf{x} \in \mathbb{R}^2 $，第一层激活值为 $ z_1 \in \mathbb{R}^4 $，第二层激活值为 $ z_2 \in \mathbb{R}^2 $，最终logit值为 $ a_3 \in \mathbb{R} $，通过sigmoid函数转换为概率。此截图来自交互式演示 http://playground.tensorflow.org。</div>


#### 13.2.4 示例模型

MLP可用于对多种类型的数据进行分类和回归。以下给出一些示例。

##### 13.2.4.1 用于将二维数据分为两类的MLP

图13.3展示了一个带有两个隐藏层的MLP，应用于二维输入向量（对应平面上的点），这些点来自两个同心圆。该模型具有以下形式：

$$  p(y|\boldsymbol{x};\boldsymbol{\theta})=\mathrm{Ber}(y|\sigma(a_{3}))   \tag*{(13.13)}$$

$$  a_{3}=w_{3}^{\top}z_{2}+b_{3}   \tag*{(13.14)}$$

$$  z_{2}=\varphi(\mathbf{W}_{2}z_{1}+b_{2})   \tag*{(13.15)}$$

$$  z_{1}=\varphi(\mathbf{W}_{1}\boldsymbol{x}+\boldsymbol{b}_{1})   \tag*{(13.16)}$$

这里 $ a_{3} $ 是最终的logit得分，通过sigmoid（逻辑）函数转换为概率。值 $ a_{3} $ 是通过对第2层的2个隐藏单元进行线性组合计算得到的。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Layer (type)</td><td style='text-align: center; word-wrap: break-word;'>Output Shape</td><td style='text-align: center; word-wrap: break-word;'>Param #</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>flatten (Flatten)</td><td style='text-align: center; word-wrap: break-word;'>(None, 784)</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dense (Dense)</td><td style='text-align: center; word-wrap: break-word;'>(None, 128)</td><td style='text-align: center; word-wrap: break-word;'>100480</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dense_1 (Dense)</td><td style='text-align: center; word-wrap: break-word;'>(None, 128)</td><td style='text-align: center; word-wrap: break-word;'>16512</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dense_2 (Dense)</td><td style='text-align: center; word-wrap: break-word;'>(None, 10)</td><td style='text-align: center; word-wrap: break-word;'>1290</td></tr><tr><td colspan="3">Total params: 118,282Trainable params: 118,282Non-trainable params: 0</td></tr></table>

表13.2：用于MNIST分类的MLP结构。注意，100,480 = (784 + 1) × 128，16,512 = (128 + 1) × 128。mlp_mnist_tf.ipynb。

$a_3 = \boldsymbol{w}_3^\top \boldsymbol{z}_2 + b_3$。相应地，第2层通过对第1层的4个隐藏单元进行非线性组合计算得到，即$\boldsymbol{z}_2 = \varphi(\boldsymbol{W}_2 \boldsymbol{z}_1 + \boldsymbol{b}_2)$。最后，第1层通过对2个输入单元进行非线性组合计算得到，即$\boldsymbol{z}_1 = \varphi(\boldsymbol{W}_1 \boldsymbol{x} + \boldsymbol{b}_1)$。通过调整参数$\boldsymbol{\theta} = (\boldsymbol{W}_1, \boldsymbol{b}_1, \boldsymbol{W}_2, \boldsymbol{b}_2, \boldsymbol{w}_3, \boldsymbol{b}_3)$以最小化负对数似然，尽管决策边界具有高度非线性，我们仍然能很好地拟合训练数据。（该图的交互式版本可在 http://playground.tensorflow.org 找到。）

##### 13.2.4.2 用于图像分类的MLP

要将MLP应用于图像分类，我们需要将二维输入“展平”为一维向量。然后，我们可以使用类似于第13.2.4.1节所述的前馈架构。例如，考虑构建一个MLP来对MNIST手写数字进行分类（第3.5.2节）。这些数字的维度为$28 \times 28 = 784$。如果我们使用两个隐藏层，每层128个单元，最后接一个10路softmax层，则得到如表13.2所示的模型。

我们在图13.4中展示了该模型的一些预测结果。仅训练了两个“epoch”（遍历数据集的次数），模型就已经表现良好，测试集准确率达到97.1%。此外，错误似乎也合理，例如将9误判为3。增加训练epoch次数可以进一步提升测试准确率。

在第14章中，我们将讨论另一种更适合图像的模型，称为卷积神经网络。该模型通过利用图像空间结构的先验知识，能够获得更好的性能且使用更少的参数。相比之下，使用MLP时，我们可以随机打乱（置换）像素而不影响输出（假设所有输入使用相同的随机置换）。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_246_118_925_338.jpg" alt="图像" width="58%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图13.4: 将MLP（含2个隐藏层，每层128个单元，以及1个输出层，含10个单元）应用于部分MNIST图像（特意挑选了一些错误样本）的结果。红色表示错误，蓝色表示正确。(a) 训练1轮后的结果。(b) 训练2轮后的结果。由 mlp_mnist_tf.ipynb 生成。</div>


##### 13.2.4.3 用于文本分类的MLP

将MLP应用于文本分类时，需要将变长的词序列 $ \mathbf{v}_1, \ldots, \mathbf{v}_T $（其中每个 $ \mathbf{v}_t $ 是长度为 $ V $ 的独热向量，$ V $ 为词汇表大小）转换为固定维度的向量 $ \mathbf{x} $。最简单的做法如下：首先将输入视为无序的词袋（第1.5.4.1节），即 $ \{\mathbf{v}_t\} $。模型的第一层是一个 $ E \times V $ 的嵌入矩阵 $ \mathbf{W}_1 $，它将每个稀疏的 $ V $ 维向量转换为稠密的 $ E $ 维嵌入 $ \mathbf{e}_t = \mathbf{W}_1 \mathbf{v}_t $（关于词嵌入的更多细节见第20.5节）。接下来，通过全局平均池化将这 $ T $ 个 $ E $ 维嵌入转换为固定大小的向量：$ \overline{\mathbf{e}} = \frac{1}{T} \sum_{t=1}^T \mathbf{e}_t $。然后将其作为MLP的输入。例如，若使用单个隐藏层和逻辑输出（用于二分类），则得到

$$  p(y|\boldsymbol{x};\boldsymbol{\theta})=\mathrm{Ber}(y|\sigma(\boldsymbol{w}_{3}^{\mathsf{T}}\boldsymbol{h}+b_{3}))   \tag*{(13.17)}$$

$$  \boldsymbol{h}=\boldsymbol{\varphi}(\mathbf{W}_{2}\overline{\boldsymbol{e}}+\boldsymbol{b}_{2})   \tag*{(13.18)}$$

$$  \overline{e}=\frac{1}{T}\sum_{t=1}^{T}e_{t}   \tag*{(13.19)}$$

$$  e_{t}=\mathbf{W}_{1}\boldsymbol{v}_{t}   \tag*{(13.20)}$$

若使用词汇表大小 V = 10,000，嵌入大小 E = 16，隐藏层大小为 16，则得到表13.3所示的模型。将该模型应用于第1.5.2.1节讨论的IMDB电影评论情感分类数据集，验证集准确率达86%。

从表13.3可以看出，该模型参数量很大，可能导致过拟合，因为IMDB训练集仅有25k个样本。然而，大多数参数集中在嵌入矩阵中，因此我们可以采用无监督预训练词嵌入模型的方法（第20.5节讨论），而非有监督学习。如果嵌入矩阵 $ W_1 $ 被固定，则只需针对这一特定标注任务微调第2层和第3层的参数，所需数据量大大减少。（另见第19章，其中讨论了在有限标注数据下训练的通用技术。）

---

<div style="text-align: center;">模型："sequential"</div>


层（类型）         输出形状           参数量

embedding（嵌入）  (None, None, 16)  160000

global_average_pooling1d（全局平均池化1D） (None, 16)  0

dense（全连接）     (None, 16)        272

dense_1（全连接_1）   (None, 1)         17

总参数量：160,289

可训练参数量：160,289

不可训练参数量：0

表13.3：用于IMDB评论分类的MLP结构。我们使用的词汇表大小为V = 10,000，嵌入维度为E = 16，隐藏层大小为16。嵌入矩阵 $\mathbf{W}_1$ 大小为10,000 × 16，隐藏层（标记为“dense”）的权重矩阵 $\mathbf{W}_2$ 大小为16 × 16，偏置 $\mathbf{b}_2$ 大小为16（注意16 × 16 + 16 = 272），最后一层（标记为“dense_1”）的权重向量 $\mathbf{w}_3$ 大小为16，偏置 $\mathbf{b}_3$ 大小为1。全局平均池化层没有自由参数。$mlp\_imdb\_tf.ipynb$。

<div style="text-align: center;"><img src="imgs/img_in_image_box_335_657_829_857.jpg" alt="图片" width="42%" /></div>


<div style="text-align: center;">图13.5：具有共享“主干”和两个输出“头”的MLP示意图，一个用于预测均值，一个用于预测方差。来自 https://brendanhasz.github.io/2019/07/23/bayesian-density-net.html。经Brendan Hasz许可使用。</div>


##### 13.2.4.4 用于异方差回归的MLP

我们也可以使用MLP进行回归。图13.5展示了如何构建一个用于异方差非线性回归的模型。（“异方差”一词仅意味着预测输出的方差与输入相关，如第2.6.3节所述。）该函数有两个输出，分别计算 $f_{\mu}(\boldsymbol{x}) = \mathbb{E}\left[y|\boldsymbol{x},\boldsymbol{\theta}\right]$ 和 $f_{\sigma}(\boldsymbol{x}) = \sqrt{\mathbb{V}\left[y|\boldsymbol{x},\boldsymbol{\theta}\right]}$。通过使用共同的“主干”和两个输出“头”（如图13.5所示），我们可以在这两个函数之间共享大部分层（以及参数）。对于 $\mu$ 头，我们使用线性激活函数 $\varphi(a) = a$。对于 $\sigma$ 头，我们使用Softplus激活函数。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_255_141_501_330.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_662_142_909_330.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 13.6：使用 MLE 拟合的 MLP 对噪声递增的一维回归数据集的预测示意图。（a）输出方差依赖于输入，如图 13.5 所示。（b）均值使用与（a）相同的模型计算，但输出方差被视为固定参数 $ \sigma^2 $，该参数在训练后通过 MLE 估计，如第 11.2.3.6 节所述。由 mlp_1d_regression_hetero_tfp.ipynb 生成。</div>


激活函数 $ \varphi(a) = \sigma_{+}(a) = \log(1 + e^{a}) $。如果我们使用线性头部和非线性主干，整体模型为

$$  p(y|\boldsymbol{x},\boldsymbol{\theta})=\mathcal{N}\left(y|\boldsymbol{w}_{\mu}^{\top}f(\boldsymbol{x};\boldsymbol{w}_{\mathrm{s h a r e d}}),\sigma_{+}(\boldsymbol{w}_{\sigma}^{\top}f(\boldsymbol{x};\boldsymbol{w}_{\mathrm{s h a r e d}}))\right)   \tag*{(13.21)}$$

图 13.6 展示了此类模型在一个数据集上的优势，该数据集的均值随时间线性增长并伴有季节性波动，方差呈二次增长。（这是随机波动率模型的一个简单例子；可用于建模金融数据，以及全球地表温度——由于气候变化，其均值和方差均呈现增长趋势。）我们看到，将输出方差 $ \sigma^{2} $ 视为固定（与输入无关）参数的回归模型有时会过度自信，因为它需要适应整体噪声水平，而无法适应输入空间中每个点的噪声水平。

#### 13.2.5 深度的重要性

可以证明，具有一个隐藏层的 MLP 是**通用函数逼近器**，即给定足够多的隐藏单元，它可以以任意期望的精度拟合任何适当光滑的函数 [HSW89; Cyb89; Hor91]。直观上，原因在于每个隐藏单元可以指定一个半平面，而足够数量的组合可以“切割”出任意空间区域，并为其关联任意响应（使用分段线性激活函数时最容易理解这一点，如图 13.7 所示）。

然而，众多实验和理论论据（例如 [Has87; Mon+14; Rag+17; Pog+17]）表明，深度网络比浅层网络效果更好。原因在于深层网络可以利用浅层网络学习到的特征，即函数以组合或层次化方式定义。例如，假设我们要对 DNA 字符串进行分类，正类与字符串 *AA??CGCG??AA* 相关，其中 ? 是通配符，表示任意单个字符，* 是通配符，表示任意字符序列（可能长度为零）。虽然我们可以使用单隐藏层模型拟合它，但直观上，如果模型先使用第一层隐藏单元学习检测 AA 和 CG“基序”，然后

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_116_550_340.jpg" alt="图像" width="29%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_623_116_956_340.jpg" alt="图像" width="28%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 13.7：由一个具有 ReLU 激活函数的 MLP 将 $ R^{2} $ 分解为有限个线性决策区域，其中 (a) 含有一个具有 25 个隐藏单元的隐藏层，(b) 含有两个隐藏层。图片来自 [HAB19] 中的图 1，经 Maksym Andriuschenko 许可使用。</div>


这些特征用于在第 2 层定义一个简单的线性分类器，类似于我们在第 13.2.1 节中解决异或（XOR）问题的方式。

#### 13.2.6 “深度学习革命”

尽管深度神经网络（DNN）背后的思想可以追溯到几十年前，但直到 2010 年代，它们才开始被广泛使用。第一个采用这些方法的领域是自动语音识别（ASR），这是基于 [Dah+11] 中的突破性成果。这一方法迅速成为标准范式，并在学术界和工业界得到广泛采用 [Hin+12]。

然而，最引人注目的时刻是 [KSH12] 证明深度卷积神经网络（CNN）能够在具有挑战性的 ImageNet 图像分类基准测试上显著提升性能，在一年内将错误率从 26% 降至 16%（见图 1.14b）；与之前每年约 2% 的进步速度相比，这是一个巨大的飞跃。

深度神经网络（DNN）使用的“爆发”有多个促成因素。其一是廉价图形处理器（GPU）的可用性；这些 GPU 最初是为了加速视频游戏的图像渲染而开发的，但它们也能大幅缩短拟合大型 CNN 所需的时间，因为 CNN 涉及类似的矩阵-向量计算。其二是大规模标注数据集的增长，这使我们能够拟合具有大量参数的复杂函数逼近器而不会过拟合（例如，ImageNet 拥有 130 万张标注图像，用于拟合具有数百万参数的模型）。事实上，如果深度学习系统被视为“火箭”，那么大型数据集就被称为燃料。 $ ^{3} $

受 DNN 杰出实证成功的推动，多家公司开始对这一技术产生兴趣。这导致了高质量开源软件库的开发，例如 Tensorflow（由 Google 开发）、PyTorch（由 Facebook 开发）和 MXNet（由 Amazon 开发）。这些库支持自动微分（见第 13.3 节）以及复杂可微函数的可扩展梯度优化（见第 8.4 节）。我们将使用其中一些

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_133_853_470.jpg" alt="图片" width="47%" /></div>


<div style="text-align: center;">图 13.8: 两个神经元在“电路”中相互连接的示意图。左侧神经元的输出轴突与右侧神经元的树突形成突触连接。以离子流形式存在的电荷使细胞能够进行通信。图片来自 https://en.wikipedia.org/wiki/Neuron，经 Wikipedia 作者 BruceBlaus 许可使用。</div>


本书中多处会用到这些库来实现各种模型，而不仅仅是深度神经网络。 $ ^{4} $

关于“深度学习革命”历史的更多细节，可参见例如 [Sej18; Met21]。

#### 13.2.7 与生物学的联系

在本节中，我们讨论上文所述神经网络（即**人工神经网络**，ANNs）与真实神经网络之间的联系。真实生物大脑的工作机制非常复杂（参见例如 [Kan+12]），但我们可以给出一个简单的“示意图”。

我们首先考虑单个神经元的模型。作为初步近似，我们可以说神经元 $k$ 是否发放（记为 $h_k \in \{0,1\}$）取决于其输入的活动（记为 $\mathbf{x} \in \mathbb{R}^D$）以及传入连接的强度（记为 $\mathbf{w}_k \in \mathbb{R}^D$）。我们可以通过 $a_k = \mathbf{w}_k^\top \mathbf{x}$ 计算输入的加权和。这些权重可视为连接输入 $x_d$ 与神经元 $h_k$ 的“导线”；它们类似于真实神经元中的树突（见图 13.8）。然后将这个加权和与阈值 $b_k$ 进行比较，如果激活值超过阈值，则神经元发放；这类似于神经元发射电输出或**动作电位**。因此，我们可以用 $h_k(\mathbf{x}) = H(\mathbf{w}_k^\top \mathbf{x} - b_k)$ 来模拟神经元的行为，其中 $H(a) = \mathbb{I}(a > 0)$ 是**赫维赛德函数**。这被称为神经元的**麦卡洛克-皮茨模型**，于 1943 年提出 [MP43]。

我们可以将多个这样的神经元组合在一起构成一个 ANN。这种组合有时也被称为

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_304_132_875_401.jpg" alt="图像" width="49%" /></div>

<div style="text-align: center;">图13.9：神经网络规模随时间的变化。模型1、2、3和4分别对应感知机[Ros58]、自适应线性单元[WH60]、新认知机[Fuk80]以及第一个通过反向传播训练的多层感知机[RHW86]。右侧标尺显示了某些生物体的大致神经元数量（海绵有0个神经元），数据来源于https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons。摘自[GBC16]的图1.11。经伊恩·古德费洛（Ian Goodfellow）许可使用。</div>

被视为大脑的模型。然而，人工神经网络与生物大脑在许多方面存在差异，包括以下几点：

● 大多数人工神经网络使用**反向传播**来修改其连接强度（见第13.3节）。然而，真实的大脑并不使用反向传播，因为不存在沿轴突反向传递信息的途径[Ben+15b; BS16; KH19]。相反，它们使用**局部更新规则**来调整突触强度。

● 大多数人工神经网络是严格**前馈**的，但真实大脑具有许多反馈连接。人们认为这种反馈类似于先验，可以与来自感觉系统的自下而上的似然结合，从而计算关于世界隐状态的后验，进而用于最优决策（例如，参见[Doy+07]）。

● 大多数人工神经网络使用简化的神经元，即通过非线性函数的加权和，但真实生物神经元具有复杂的**树突树结构**（见图13.8），并伴有复杂的时空动力学。

- 大多数人工神经网络在规模和连接数量上小于生物大脑（见图13.9）。当然，在各种新型硬件加速器（如GPU和TPU（张量处理单元）等）的推动下，人工神经网络每周都在变大。然而，即使人工神经网络在单元数量上与生物大脑相匹配，这种比较也具有误导性，因为生物神经元的处理能力远高于人工神经元（见上一点）。

- 大多数人工神经网络被设计用于建模单一功能，例如将图像映射到标签，或将一个词序列映射到另一个词序列。相比之下，生物大脑是非常复杂的系统，由多个专门化的、相互作用的模块组成，这些模块实现不同种类的功能或行为，如感知、控制、记忆、语言等（例如，参见[Sha88; Kan+12]）。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND许可协议。

---

当然，人们也在尝试构建生物大脑的逼真模型（例如，蓝脑计划 [Mar06; Yon19]）。然而，一个有趣的问题是，在如此精细的层面上研究大脑是否有助于“解决人工智能”。普遍认为，如果我们的目标是构建“智能机器”，生物大脑的底层细节并不重要，就像飞机并不会扑动翅膀一样。不过，可以推测，“人工智能”将遵循与智能生物体类似的“智能法则”，正如飞机和鸟类遵循相同的空气动力学法则。

遗憾的是，我们尚不清楚“智能法则”是什么，甚至不确定是否存在这样的法则。在本书中，我们假设任何智能体都应遵循信息处理与贝叶斯决策理论的基本原则，后者被公认为在不确定性下进行最优决策的方法（见第5.1节）。

在实践中，最优贝叶斯方法往往在计算上难以处理。在自然界中，生物体进化出了各种算法层面的“捷径”来逼近最优解；这可以解释人们在日常推理中使用的许多启发式方法 [KST82; GTA00; Gri20]。随着我们希望机器解决的任务变得越来越困难，我们或许能从神经科学和认知科学中获得启示，了解如何以近似方式解决这类任务（例如，参见 [SC16; MWK16; Has+17; Lak+17; HG21]）。然而，我们也应牢记，人工智能/机器学习系统越来越多地用于安全关键型应用，在这些应用中，我们可能希望并期望机器比人类做得更好。在这种情况下，我们可能需要的不仅仅是常能奏效的启发式解，而是类似于其他工程领域那样，需要可证明可靠的方法（进一步讨论见第1.6.3节）。

### 13.3 反向传播

本节与 Mathieu Blondel 合作撰写。

在本节中，我们将介绍著名的反向传播算法，该算法可用于计算作用于网络输出的损失函数关于每层参数的梯度。然后，该梯度可以传递给基于梯度的优化算法，我们将在第13.4节中讨论这一点。

反向传播算法最初由 [BH69] 发现，并由 [Wer74] 独立发现。然而，是 [RHW86] 将该算法引入“主流”机器学习社区的关注。更多历史细节可参见维基百科页面 $ ^{5} $。

我们最初假设计算图是简单的堆叠层线性链，如 MLP 中那样。在这种情况下，反向传播等价于反复应用微积分中的链式法则（见公式 (7.261)）。然而，该方法可以推广到任意有向无环图（DAG），我们将在第13.3.4节中讨论。这一通用过程通常称为自动微分或 autodiff。

#### 13.3.1 正向模式与反向模式微分

考虑形如 $ \boldsymbol{o} = \boldsymbol{f}(\boldsymbol{x}) $ 的映射，其中 $ \boldsymbol{x} \in \mathbb{R}^n $，$ \boldsymbol{o} \in \mathbb{R}^m $。我们假设 $ \boldsymbol{f} $ 定义为若干函数的复合：

$$ f=f_{4}\circ f_{3}\circ f_{2}\circ f_{1} \tag*{(13.22)} $$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_159_119_1020_295.jpg" alt="图像" width="74%" /></div>


<div style="text-align: center;">图 13.10：一个具有 4 层的简单线性链前馈模型。其中 x 为输入，o 为输出。摘自 [Blo20]。</div>


其中 $ f_1: \mathbb{R}^n \to \mathbb{R}^{m_1} $, $ f_2: \mathbb{R}^{m_1} \to \mathbb{R}^{m_2} $, $ f_3: \mathbb{R}^{m_2} \to \mathbb{R}^{m_3} $, $ f_4: \mathbb{R}^{m_3} \to \mathbb{R}^m $。计算 $ o = f(x) $ 所需的中间步骤为 $ x_2 = f_1(x) $, $ x_3 = f_2(x_2) $, $ x_4 = f_3(x_3) $, $ o = f_4(x_4) $。

我们可以利用链式法则计算雅可比矩阵 $ \mathbf{J}_f(\mathbf{x}) = \frac{\partial \mathbf{o}}{\partial \mathbf{x}} \in \mathbb{R}^{m \times n} $：

$$  \begin{aligned}\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}}&=\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{4}}\frac{\partial\boldsymbol{x}_{4}}{\partial\boldsymbol{x}_{3}}\frac{\partial\boldsymbol{x}_{3}}{\partial\boldsymbol{x}_{2}}\frac{\partial\boldsymbol{x}_{2}}{\partial\boldsymbol{x}}=\frac{\partial\boldsymbol{f}_{4}(\boldsymbol{x}_{4})}{\partial\boldsymbol{x}_{4}}\frac{\partial\boldsymbol{f}_{3}(\boldsymbol{x}_{3})}{\partial\boldsymbol{x}_{3}}\frac{\partial\boldsymbol{f}_{2}(\boldsymbol{x}_{2})}{\partial\boldsymbol{x}_{2}}\frac{\partial\boldsymbol{f}_{1}(\boldsymbol{x})}{\partial\boldsymbol{x}}\\&=\mathbf{J}_{f_{4}}(\boldsymbol{x}_{4})\mathbf{J}_{f_{3}}(\boldsymbol{x}_{3})\mathbf{J}_{f_{2}}(\boldsymbol{x}_{2})\mathbf{J}_{f_{1}}(\boldsymbol{x})\end{aligned}   \tag*{(13.23)}$$

现在我们讨论如何高效计算雅可比矩阵 $ \mathbf{J}_{f}(\mathbf{x}) $。回顾

$$  \mathbf{J}_{f}(\boldsymbol{x})=\frac{\partial\boldsymbol{f}(\boldsymbol{x})}{\partial\boldsymbol{x}}=\begin{pmatrix}\frac{\partial f_{1}}{\partial x_{1}}&\cdots&\frac{\partial f_{1}}{\partial x_{n}}\\ \vdots&\ddots&\vdots\\ \frac{\partial f_{m}}{\partial x_{1}}&\cdots&\frac{\partial f_{m}}{\partial x_{n}}\end{pmatrix}=\begin{pmatrix}\nabla f_{1}(\boldsymbol{x})^{\top}\\ \vdots\\ \nabla f_{m}(\boldsymbol{x})^{\top}\end{pmatrix}=\left(\frac{\partial\boldsymbol{f}}{\partial x_{1}},\cdots,\frac{\partial\boldsymbol{f}}{\partial x_{n}}\right)\in\mathbb{R}^{m\times n}   \tag*{(13.25)}$$

其中，$\nabla f_i(\boldsymbol{x})^\top \in \mathbb{R}^{1 \times n}$ 是第 $i$ 行（$ i = 1 : m $），$\frac{\partial f}{\partial x_j} \in \mathbb{R}^m$ 是第 $j$ 列（$ j = 1 : n $）。注意，在我们的记法中，当 $ m = 1 $ 时，梯度记作 $\nabla f(\boldsymbol{x})$，其形状与 $\boldsymbol{x}$ 相同，因此它是一个列向量，而 $\mathbf{J}_f(\boldsymbol{x})$ 是一个行向量。此时，我们严格来说有 $\nabla f(\boldsymbol{x}) = \mathbf{J}_f(\boldsymbol{x})^\top$。

我们可以通过形如 $e_i^\top \mathbf{J}_f(\boldsymbol{x})$ 的**向量-雅可比乘积（VJP）**来提取 $\mathbf{J}_f(\boldsymbol{x})$ 的第 $i$ 行，其中 $e_i \in \mathbb{R}^m$ 是单位基向量。类似地，通过形如 $\mathbf{J}_f(\boldsymbol{x})e_j$ 的**雅可比-向量乘积（JVP）**可提取第 $j$ 列，其中 $e_j \in \mathbb{R}^n$。这表明计算 $\mathbf{J}_f(\boldsymbol{x})$ 可归结为 $n$ 个 JVP 或 $m$ 个 VJP。

若 $n < m$，通过从右到左使用 JVP 逐列（$j = 1 : n$）计算 $\mathbf{J}_f(\boldsymbol{x})$ 更为高效。与列向量 $\boldsymbol{v}$ 的右乘为

$$  \mathbf{J}_{f}(\boldsymbol{x})\boldsymbol{v}=\underbrace{\mathbf{J}_{f_{4}}(\boldsymbol{x}_{4})}_{m\times m_{3}}\underbrace{\mathbf{J}_{f_{3}}(\boldsymbol{x}_{3})}_{m_{3}\times m_{2}}\underbrace{\mathbf{J}_{f_{2}}(\boldsymbol{x}_{2})}_{m_{2}\times m_{1}}\underbrace{\mathbf{J}_{f_{1}}(\boldsymbol{x}_{1})}_{m_{1}\times n}\underbrace{\boldsymbol{v}}_{n\times1}   \tag*{(13.26)}$$

这可以通过前向模式微分计算；伪代码见算法 13.1。假设 $m = 1$ 且 $ n = m_1 = m_2 = m_3 $，计算 $\mathbf{J}_f(\boldsymbol{x})$ 的代价为 $ O(n^2) $。

若 $n > m$（例如输出为标量时），通过从左到右使用 VJP 逐行（$i = 1 : m$）计算 $\mathbf{J}_f(\boldsymbol{x})$ 更为高效。与行向量 $\boldsymbol{u}^\top$ 的左乘为

$$  \boldsymbol{u}^{\top}\boldsymbol{J}_{f}(\boldsymbol{x})=\underbrace{\boldsymbol{u}^{\top}}_{1\times m}\underbrace{\boldsymbol{J}_{f_{4}}(\boldsymbol{x}_{4})}_{m\times m_{3}}\underbrace{\boldsymbol{J}_{f_{3}}(\boldsymbol{x}_{3})}_{m_{3}\times m_{2}}\underbrace{\boldsymbol{J}_{f_{2}}(\boldsymbol{x}_{2})}_{m_{2}\times m_{1}}\underbrace{\boldsymbol{J}_{f_{1}}(\boldsymbol{x}_{1})}_{m_{1}\times n}   \tag*{(13.27)}$$

作者：Kevin P. Murphy。 (C) MIT 出版社。 CC-BY-NC-ND 许可协议。

---

算法 13.1：前向模式微分

1  $ x_{1} := x $
2  $ v_{j} := e_{j} \in \mathbb{R}^{n} $ for  $ j = 1 : n $
3 for  $ k = 1 : K $ do
4  $ \left.\begin{array}{l}x_{k+1} = f_{k}(x_{k})\\v_{j} := \mathbf{J} f_{k}(x_{k})v_{j}\end{array}\right. $ for  $ j = 1 : n $
6 Return  $ o = x_{K+1}, [\mathbf{J} f(x)]_{:,j} = v_{j} $ for  $ j = 1 : n $

这可以通过反向模式微分实现；伪代码见算法 13.2。假设 $ m = 1 $ 且 $ n = m_1 = m_2 = m_3 $，计算 $ \mathbf{J}_f(\boldsymbol{x}) $ 的代价为 $ O(n^2) $。

算法 13.2：反向模式微分

1  $ x_{1} := x $
2 for  $ k = 1 : K $ do
3  $ \bigsqcup x_{k+1} = f_{k}(x_{k}) $
4  $ u_{i} := e_{i} \in \mathbb{R}^{m} $ for  $ i = 1 : m $
5 for  $ k = K : 1 $ do
6  $ \bigsqcup u_{i}^{\top} := u_{i}^{\top} J_{f_{k}}(x_{k}) $ for  $ i = 1 : m $
7 Return  $ o = x_{K+1}, [J_{f}(x)]_{i,:} = u_{i}^{\top} $ for  $ i = 1 : m $

算法 13.1 和 13.2 都可以通过接受 $ \{v_j\}_{j=1,\ldots,n} $ 和 $ \{u_i\}_{i=1,\ldots,m} $ 作为相应输入，来适应计算任意输入向量集合的雅可比-向量乘积（JVP）和向量-雅可比乘积（VJP）。将这些向量初始化为标准基对于生成完整的雅可比矩阵作为输出特别有用。

#### 13.3.2 多层感知机的反向模式微分

在上一节中，我们考虑了一个简单的线性链式前馈模型，其中每一层没有可学习的参数。在本节中，每一层现在可以拥有（可选的）参数 $ \boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{4} $。见图 13.10 的示意。我们关注映射形式为 $ \mathcal{L} : \mathbb{R}^{n} \to \mathbb{R} $ 的情况，即输出是一个标量。例如，考虑一个具有一个隐藏层的 MLP 的 $ \ell_{2} $ 损失：

$$  \mathcal{L}((x,y),\theta)=\frac{1}{2}||y-\mathbf{W}_{2}\varphi(\mathbf{W}_{1}x)||_{2}^{2}   \tag*{(13.28)}$$

---

我们可以将其表示为以下前馈模型：

$$  \mathcal{L}=f_{4}\circ f_{3}\circ f_{2}\circ f_{1}   \tag*{(13.29)}$$

$$  \boldsymbol{x}_{2}=\boldsymbol{f}_{1}(\boldsymbol{x},\boldsymbol{\theta}_{1})=\mathbf{W}_{1}\boldsymbol{x}   \tag*{(13.30)}$$

$$  \boldsymbol{x}_{3}=\boldsymbol{f}_{2}(\boldsymbol{x}_{2},\varnothing)=\varphi(\boldsymbol{x}_{2})   \tag*{(13.31)}$$

$$  \boldsymbol{x}_{4}=\boldsymbol{f}_{3}(\boldsymbol{x}_{3},\boldsymbol{\theta}_{3})=\mathbf{W}_{2}\boldsymbol{x}_{3}   \tag*{(13.32)}$$

$$  \mathcal{L}=\boldsymbol{f}_{4}(\boldsymbol{x}_{4},\boldsymbol{y})=\frac{1}{2}||\boldsymbol{x}_{4}-\boldsymbol{y}||^{2}   \tag*{(13.33)}$$

我们使用符号 $ \boldsymbol{f}_{k}(\boldsymbol{x}_{k}, \boldsymbol{\theta}_{k}) $ 表示第 $ k $ 层处的函数，其中 $ \boldsymbol{x}_{k} $ 是前一个输出，$ \boldsymbol{\theta}_{k} $ 是该层的可选参数。

在此示例中，最后一层返回一个标量，因为它对应于损失函数 $ \mathcal{L} \in \mathbb{R} $。因此，使用反向模式微分计算梯度向量更为高效。

我们首先讨论如何计算标量输出关于每层参数的梯度。我们可以轻松计算关于最后一层预测的梯度 $ \frac{\partial \mathcal{L}}{\partial \mathbf{x}_4} $。对于关于更早层参数的梯度，我们可以利用链式法则得到

 $$ \begin{array}{r l}{\partial\mathcal{L}}&{{}\quad\partial\mathcal{L}\partial\boldsymbol{x}_{4}}\end{array} $$ 

$$  \overline{\partial\theta_{3}}=\overline{\partial x_{4}}\overline{\partial\theta_{3}}   \tag*{(13.34)}$$

 $$ \partial\mathcal{L}_{\mathrm{~\scriptsize~\textsc~{~}~}}\partial\mathcal{L}\partial\boldsymbol{x}_{4}\partial\boldsymbol{x}_{3} $$ 

$$  \overline{{\partial\theta_{2}}}=\overline{{\partial x_{4}}}\overline{{\partial x_{3}}}\overline{{\partial\theta_{2}}}   \tag*{(13.35)}$$

$$  \frac{\partial\mathcal{L}}{\partial\theta_{1}}=\frac{\partial\mathcal{L}}{\partial x_{4}}\frac{\partial x_{4}}{\partial x_{3}}\frac{\partial x_{3}}{\partial x_{2}}\frac{\partial x_{2}}{\partial\theta_{1}}   \tag*{(13.36)}$$

其中每个 $ \frac{\partial \mathcal{L}}{\partial \theta_k} = (\nabla_{\theta_k} \mathcal{L})^\top $ 是一个 $ d_k $ 维梯度行向量，$ d_k $ 是第 $ k $ 层的参数数量。我们可以看到，这些可以递归计算，通过将第 $ k $ 层的梯度行向量乘以雅可比矩阵 $ \frac{\partial \mathbf{x}_k}{\partial \mathbf{x}_{k-1}} $，该矩阵是一个 $ n_k \times n_{k-1} $ 的矩阵，其中 $ n_k $ 是第 $ k $ 层的隐藏单元数。参见算法 13.3 的伪代码。

该算法计算损失关于每层参数的梯度。它还计算损失关于输入的梯度 $ \nabla_x \mathcal{L} \in \mathbb{R}^n $，其中 $ n $ 是输入的维度。后一个量对于参数学习并非必需，但对于生成模型的输入可能有用（参见第 14.6 节的一些应用）。

剩下的就是如何计算所有支持层的向量-雅可比乘积（VJP）。其具体细节取决于每层函数的形式。下面我们讨论一些示例。

#### 13.3.3 常见层的向量-雅可比乘积

回想一下，对于形如 $ f: \mathbb{R}^n \to \mathbb{R}^m $ 的层，其雅可比矩阵定义为

$$  \mathbf{J}_{f}(\boldsymbol{x})=\frac{\partial f(\boldsymbol{x})}{\partial\boldsymbol{x}}=\begin{pmatrix}\frac{\partial f_{1}}{\partial x_{1}}&\cdots&\frac{\partial f_{1}}{\partial x_{n}}\\ \vdots&\ddots&\vdots\\ \frac{\partial f_{m}}{\partial x_{1}}&\cdots&\frac{\partial f_{m}}{\partial x_{n}}\end{pmatrix}=\begin{pmatrix}\nabla f_{1}(\boldsymbol{x})^{\top}\\ \vdots\\ \nabla f_{m}(\boldsymbol{x})^{\top}\end{pmatrix}=\left(\frac{\partial f}{\partial x_{1}},\cdots,\frac{\partial f}{\partial x_{n}}\right)\in\mathbb{R}^{m\times n}   \tag*{(13.37)}$$

其中 $ \nabla f_i(\boldsymbol{x})^\top \in \mathbb{R}^n $ 是第 $ i $ 行（$ i = 1 : m $），$ \frac{\partial f}{\partial x_j} \in \mathbb{R}^m $ 是第 $ j $ 列（$ j = 1 : n $）。在本节中，我们描述如何计算常见层的 VJP $ \boldsymbol{u}^\top \boldsymbol{J}_f(\boldsymbol{x}) $。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

算法 13.3：含 K 层 MLP 的反向传播

1 // 前向传播
2  $ x_1 := x $
3 for  $ k = 1 : K $ do
4  $ \lfloor x_{k+1} = f_k(x_k, \theta_k) $
5 // 反向传播
6  $ u_{K+1} := 1 $
7 for  $ k = K : 1 $ do
8  $ \left\lfloor g_k := u_{k+1}^{\top} \frac{\partial f_k(x_k, \theta_k)}{\partial \theta_k}\right. $
9  $ \left\lfloor u_k^{\top} := u_{k+1}^{\top} \frac{\partial f_k(x_k, \theta_k)}{\partial x_k}\right. $
10 // 输出
11 返回  $ \mathcal{L} = x_{K+1}, \nabla_x \mathcal{L} = u_1, \{\nabla_{\theta_k} \mathcal{L} = g_k : k = 1 : K\} $

##### 13.3.3.1 交叉熵层

考虑一个交叉熵损失层，它以 logits x 和目标标签 y 作为输入，并返回一个标量：

$$  z=f(\boldsymbol{x})=\text{CrossEntropyWithLogits}(\boldsymbol{y},\boldsymbol{x})=-\sum_{c}y_{c}\log(\text{softmax}(\boldsymbol{x})_{c})=-\sum_{c}y_{c}\log p_{c}   \tag*{(13.38)}$$

其中 $ p = \text{softmax}(x) = \frac{e^{x_c}}{\sum_{c' = 1}^{C} e^{x_{c'}}}  $ 是预测的类别概率，而 $ y $ 是标签的真实分布（通常是独热向量）。关于输入的雅可比矩阵为

$$  \mathbf{J}=\frac{\partial z}{\partial\mathbf{x}}=\left(\mathbf{p}-\mathbf{y}\right)^{\mathsf{T}}\in\mathbb{R}^{1\times C}   \tag*{(13.39)}$$

为了说明这一点，假设目标标签为类别 c。我们有

$$  z=f(\boldsymbol{x})=-\log(p_{c})=-\log\left(\frac{e^{x_{c}}}{\sum_{j}e^{x_{j}}}\right)=\log\left(\sum_{j}e^{x_{j}}\right)-x_{c}   \tag*{(13.40)}$$

因此

$$  \frac{\partial z}{\partial x_{i}}=\frac{\partial}{\partial x_{i}}\log\sum_{j}e^{x_{j}}-\frac{\partial}{\partial x_{i}}x_{c}=\frac{e^{x_{i}}}{\sum_{j}e^{x_{j}}}-\frac{\partial}{\partial x_{i}}x_{c}=p_{i}-\mathbb{I}\left(i=c\right)   \tag*{(13.41)}$$

如果定义 $ \mathbf{y} = [\mathbb{I}(i = c)] $，我们便得到公式 (13.39)。注意该层的雅可比矩阵是一个行向量，因为输出是标量。

---

##### 13.3.3.2 逐元素非线性

考虑一个应用逐元素非线性的层，$z = f(x) = \varphi(x)$，因此 $z_i = \varphi(x_i)$。雅可比矩阵的 $(i,j)$ 元素由下式给出

$$  \frac{\partial z_{i}}{\partial x_{j}}=\begin{cases}\varphi^{\prime}(x_{i})&if i=j\\0&otherwise\end{cases}   \tag*{(13.42)}$$

其中 $\varphi'(a) = \frac{d}{da}\varphi(a)$。换句话说，关于输入的雅可比矩阵为

$$  \mathbf{J}=\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{x}}=\mathrm{diag}(\boldsymbol{\varphi}^{\prime}(\boldsymbol{x}))   \tag*{(13.43)}$$

对于任意向量 $\boldsymbol{u}$，我们可以通过将 $\boldsymbol{J}$ 的对角线与 $\boldsymbol{u}$ 进行逐元素乘法来计算 $\boldsymbol{u}^{\mathrm{T}} \boldsymbol{J}$。例如，如果

$$  \varphi(a)=\operatorname{ReLU}(a)=\max(a,0)   \tag*{(13.44)}$$

我们有

$$  \varphi^{\prime}(a)=\begin{cases}0&a<0\\1&a>0\end{cases}   \tag*{(13.45)}$$

在 $a = 0$ 处的次导数（第 8.1.4.1 节）是 $[0, 1]$ 中的任意值。通常取为 0。因此

$$  \mathrm{ReLU}^{\prime}(a)=H(a)   \tag*{(13.46)}$$

其中 $H$ 是赫维赛德阶跃函数。

##### 13.3.3.3 线性层

现在考虑一个线性层，$z = f(x, \mathbf{W}) = \mathbf{W}x$，其中 $\mathbf{W} \in \mathbb{R}^{m \times n}$，因此 $x \in \mathbb{R}^n$ 且 $z \in \mathbb{R}^m$。我们可以计算关于输入向量的雅可比矩阵 $\mathbf{J} = \frac{\partial z}{\partial x} \in \mathbb{R}^{m \times n}$ 如下。注意

$$  z_{i}=\sum_{k=1}^{n}W_{ik}x_{k}   \tag*{(13.47)}$$

所以雅可比矩阵的 $(i,j)$ 条目为

$$  \frac{\partial z_{i}}{\partial x_{j}}=\frac{\partial}{\partial x_{j}}\sum_{k=1}^{n}W_{ik}x_{k}=\sum_{k=1}^{n}W_{ik}\frac{\partial}{\partial x_{j}}x_{k}=W_{ij}   \tag*{(13.48)}$$

因为 $\frac{\partial}{\partial x_j}x_k=\mathbb{I}(k=j)$。因此关于输入的雅可比矩阵为

$$  \mathbf{J}=\frac{\partial\mathbf{z}}{\partial\mathbf{x}}=\mathbf{W}   \tag*{(13.49)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

向量 $\boldsymbol{u}^\top \in \mathbb{R}^{1 \times m}$ 与 $\boldsymbol{J} \in \mathbb{R}^{m \times n}$ 之间的向量-雅可比乘积（VJP）为：

$$  \boldsymbol{u}^{\top}\frac{\partial\boldsymbol{z}}{\partial\boldsymbol{x}}=\boldsymbol{u}^{\top}\mathbf{W}\in\mathbb{R}^{1\times n}   \tag*{(13.50)}$$

现在考虑关于权重矩阵的雅可比矩阵 $\mathbf{J} = \frac{\partial \mathbf{z}}{\partial \mathbf{W}}$。它可以表示为一个 $m \times (m \times n)$ 的矩阵，处理起来较为复杂。因此，我们转而关注针对单个权重 $W_{ij}$ 的梯度。由于 $\frac{\partial \mathbf{z}}{\partial W_{ij}}$ 是一个向量，计算起来更为简便。为计算该梯度，注意到：

$$  z_{k}=\sum_{l=1}^{n}W_{kl}x_{l}   \tag*{(13.51)}$$

$$  \frac{\partial z_{k}}{\partial W_{ij}}=\sum_{l=1}^{n}x_{l}\frac{\partial}{\partial W_{ij}}W_{kl}=\sum_{l=1}^{n}x_{l}\mathbb{I}\left(i=k \text{且} j=l\right)   \tag*{(13.52)}$$

因此：

$$  \frac{\partial\boldsymbol{z}}{\partial W_{i j}}=\left(\begin{matrix}0&\cdots&0&x_{j}&0&\cdots&0\end{matrix}\right)^{\mathrm{T}}   \tag*{(13.53)}$$

其中非零项位于第 $i$ 个位置。向量 $\boldsymbol{u}^{\mathrm{T}} \in \mathbb{R}^{1 \times m}$ 与 $\frac{\partial \boldsymbol{z}}{\partial \boldsymbol{W}} \in \mathbb{R}^{m \times (m \times n)}$ 之间的 VJP 可以表示为一个形状为 $1 \times (m \times n)$ 的矩阵。注意到：

$$  \boldsymbol{u}^{\top}\frac{\partial\boldsymbol{z}}{\partial W_{ij}}=\sum_{k=1}^{m}u_{k}\frac{\partial z_{k}}{\partial W_{ij}}=u_{i}x_{j}   \tag*{(13.54)}$$

因此：

$$  \left[u^{\top}\frac{\partial z}{\partial\mathbf{W}}\right]_{1,:}=u x^{\top}\in\mathbb{R}^{m\times n}   \tag*{(13.55)}$$

##### 13.3.3.4 综合应用

如需练习将上述内容综合运用，请参见练习 13.1。

#### 13.3.4 计算图

MLP 是 DNN 的一种简单形式，其中每一层直接馈入下一层，形成链式结构，如图 13.10 所示。然而，现代 DNN 可以以更复杂的方式组合可微组件，从而创建计算图，类似于程序员组合基本函数以构建更复杂函数的方式。（事实上，有人建议将“深度学习”称为“可微编程”。）唯一的限制是所得计算图对应一个**有向无环图（DAG）**，其中每个节点都是其所有输入的可微函数。

例如，考虑函数：

$$  f(x_{1},x_{2})=x_{2}e^{x_{1}}\sqrt{x_{1}+x_{2}e^{x_{1}}}   \tag*{(13.56)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_216_136_951_332.jpg" alt="图像" width="63%" /></div>


<div style="text-align: center;">图 13.11：一个有 2 个（标量）输入和 1 个（标量）输出的计算图示例。来自 [Blo20]。</div>


我们可以利用图 13.11 中的 DAG 通过以下中间函数进行计算：

$$  x_{3}=f_{3}(x_{1})=e^{x_{1}}   \tag*{(13.57)}$$

 $$ x_{4}=f_{4}(x_{2},x_{3})=x_{2}x_{3} $$ 

$$  x_{5}=f_{5}(x_{1},x_{4})=x_{1}+x_{4}   \tag*{(13.58)}$$

$$  x_{6}=f_{6}(x_{5})=\sqrt{x_{5}}   \tag*{(13.60)}$$

$$  x_{7}=f_{7}(x_{4},x_{6})=x_{4}x_{6}   \tag*{(13.61)}$$

注意，我们已按拓扑顺序（父节点在前，子节点在后）对节点进行了编号。在反向传播过程中，由于图不再是一条链，我们可能需要沿多条路径对梯度求和。例如，由于 $ x_{4} $ 影响 $ x_{5} $ 和 $ x_{7} $，我们有

$$  \frac{\partial\boldsymbol{o}}{\partial x_{4}}=\frac{\partial\boldsymbol{o}}{\partial x_{5}}\frac{\partial x_{5}}{\partial x_{4}}+\frac{\partial\boldsymbol{o}}{\partial x_{7}}\frac{\partial x_{7}}{\partial x_{4}}   \tag*{(13.62)}$$

我们可以通过逆拓扑顺序工作来避免重复计算。例如：

$$  \frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{7}}=\frac{\partial\boldsymbol{x}_{7}}{\partial\boldsymbol{x}_{7}}=\mathbf{I}_{m}   \tag*{(13.63)}$$

$$  \frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{6}}=\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{7}}\frac{\partial\boldsymbol{x}_{7}}{\partial\boldsymbol{x}_{6}}   \tag*{(13.64)}$$

$$  \frac{\partial\boldsymbol{o}}{\partial x_{5}}=\frac{\partial\boldsymbol{o}}{\partial x_{6}}\frac{\partial x_{6}}{\partial x_{5}}   \tag*{(13.65)}$$

$$  \frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{4}}=\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{5}}\frac{\partial\boldsymbol{x}_{5}}{\partial\boldsymbol{x}_{4}}+\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{7}}\frac{\partial\boldsymbol{x}_{7}}{\partial\boldsymbol{x}_{4}}   \tag*{(13.66)}$$

一般情况下，我们使用

$$  \frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{j}}=\sum_{k\in\mathrm{Ch}(j)}\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{k}}\frac{\partial\boldsymbol{x}_{k}}{\partial\boldsymbol{x}_{j}}   \tag*{(13.67)}$$

其中对节点 $j$ 的所有子节点 $k$ 求和，如图 13.12 所示。对于每个子节点 $k$，梯度向量 $\frac{\partial\boldsymbol{o}}{\partial\boldsymbol{x}_{k}}$ 已经计算完毕；这个量称为**伴随量**。它乘以每个子节点的雅可比矩阵 $\frac{\partial\boldsymbol{x}_{k}}{\partial\boldsymbol{x}_{i}}$。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_310_124_862_337.jpg" alt="图片" width="47%" /></div>


<div style="text-align: center;">图13.12：计算图中节点j处自动微分的符号表示。引自[Blo20]。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_250_397_923_617.jpg" alt="图片" width="58%" /></div>


<div style="text-align: center;">图13.13：一个多层感知机的计算图，其中输入为 $\mathbf{x}$，隐藏层为 $\mathbf{h}$，输出为 $\mathbf{o}$，损失函数 $L = \ell(\mathbf{o}, y)$，权重上的 $\ell_2$ 正则化项 $s$，总损失 $J = L + s$。改编自[Zha+20]的图4.7.1，经Aston Zhang许可使用。</div>


可以通过使用API定义静态图来预先计算计算图。（这就是TensorFlow 1的工作方式。）或者，也可以通过跟踪函数在输入参数上的执行来“即时”计算图。（这就是TensorFlow Eager模式以及JAX和PyTorch的工作方式。）后一种方法更容易处理动态图，其形状可以根据函数计算出的值而变化。

图13.13展示了一个带权重衰减的单隐藏层MLP对应的计算图。更准确地说，该模型计算线性预激活值 $z = \mathbf{W}^{(1)}x$，隐藏层激活值 $\mathbf{h} = \phi(\mathbf{z})$，线性输出 $\mathbf{o} = \mathbf{W}^{(2)}\mathbf{h}$，损失 $L = \ell(\mathbf{o}, y)$，正则化项 $s = \frac{\lambda}{2}(||\mathbf{W}^{(1)}||_F^2 + ||\mathbf{W}^{(2)}||_F^2)$，以及总损失 $J = L + s$。

### 13.4 训练神经网络

本节讨论如何将深度神经网络拟合到数据上。标准方法是使用最大似然估计，即最小化负对数似然：

$$  \mathcal{L}(\boldsymbol{\theta})=-\log p(\mathcal{D}|\boldsymbol{\theta})=-\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n};\boldsymbol{\theta})   \tag*{(13.68)}$$

通常还会添加一个正则化项（如负对数先验），我们将在第13.5节中讨论。

---

原则上，我们可以直接使用反向传播算法（第13.3节）计算该损失的梯度，并将其传递给现成的优化器（例如第8章讨论的那些）。**Adam优化器（第8.4.6.3节）是一个常见选择**，因为它既能扩展到大规模数据集（作为随机梯度下降（SGD）变体算法），又能通过对角预条件和动量快速收敛。然而，在实践中这种方法可能效果不佳。本节将讨论可能出现的各种问题及其解决方案。关于训练深度神经网络（DNN）实践细节的更多内容，可参考其他书籍，例如 [HG20; Zha+20; Gér19]。

除了实践问题，还存在重要的理论问题。特别地，我们注意到 DNN 损失函数并非凸目标，因此通常无法找到全局最优解。然而，SGD 往往能找到出乎意料的好解。关于这一现象的原因仍在研究中；参见 [Bah+20] 以获取近期部分研究综述。

#### 13.4.1 调优学习率

调优学习率（步长）对确保收敛到优质解至关重要。我们将在第 8.4.3 节讨论该问题。

#### 13.4.2 梯度消失与梯度爆炸

在训练极深模型时，由于误差信号经过一系列会放大或缩小它的层传递，梯度往往会变得非常小（即梯度消失问题）或非常大（即梯度爆炸问题）[Hoc+01]。（类似问题也出现在长序列的循环神经网络（RNN）中，见第 15.2.6 节）

为更详细地解释该问题，考虑损失相对于第 l 层节点的梯度：

$$  \frac{\partial\mathcal{L}}{\partial\boldsymbol{z}_{l}}=\frac{\partial\mathcal{L}}{\partial\boldsymbol{z}_{l+1}}\frac{\partial\boldsymbol{z}_{l+1}}{\partial\boldsymbol{z}_{l}}=\mathbf{J}_{l}\boldsymbol{g}_{l+1}   \tag*{(13.69)}$$

其中 $\mathbf{J}_l = \frac{\partial \mathbf{z}_{l+1}}{\partial \mathbf{z}_l}$ 是雅可比矩阵，$g_{l+1} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}_{l+1}}$ 是下一层的梯度。若 $\mathbf{J}_l$ 在各层间恒定，则最后一层梯度 $g_L$ 对第 l 层梯度的贡献显然为 $\mathbf{J}^{L-l} g_L$。因此，系统的行为取决于 $\mathbf{J}$ 的特征向量。

尽管 J 是实矩阵，但一般不对称，其特征值和特征向量可以是复数，虚部对应振荡行为。设 $\lambda$ 为 J 的谱半径（即特征值绝对值最大值）。若 $\lambda > 1$，梯度可能爆炸；若 $\lambda < 1$，梯度可能消失。（类似地，连接 $z_l$ 与 $z_{l+1}$ 的权重矩阵 W 的谱半径决定了前向模式下动力系统的稳定性。）

梯度爆炸问题可通过**梯度裁剪**缓解，即当梯度过大时将其幅度限制在某个阈值内：

$$  g^{\prime}=\min(1,\frac{c}{\left|\left|g\right|\right|})g   \tag*{(13.70)}$$

这样，$g'$ 的范数永远不会超过 $c$，且向量方向与 $g$ 始终保持一致。

然而，梯度消失问题更难解决。有以下几种常见解决方案：

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称</td><td style='text-align: center; word-wrap: break-word;'>定义</td><td style='text-align: center; word-wrap: break-word;'>范围</td><td style='text-align: center; word-wrap: break-word;'>参考文献</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Sigmoid</td><td style='text-align: center; word-wrap: break-word;'>$ \sigma(a)=\frac{1}{1+e^{-a}} $</td><td style='text-align: center; word-wrap: break-word;'>[0,1]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Hyperbolic tangent</td><td style='text-align: center; word-wrap: break-word;'>$ \tanh(a)=2\sigma(2a)-1 $</td><td style='text-align: center; word-wrap: break-word;'>[-1,1]</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Softplus</td><td style='text-align: center; word-wrap: break-word;'>$ \sigma_{+}(a)=\log(1+e^{a}) $</td><td style='text-align: center; word-wrap: break-word;'>[0,\infty]</td><td style='text-align: center; word-wrap: break-word;'>[GBB11]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Rectified linear unit</td><td style='text-align: center; word-wrap: break-word;'>$ \text{ReLU}(a)=\max(a,0) $</td><td style='text-align: center; word-wrap: break-word;'>[0,\infty]</td><td style='text-align: center; word-wrap: break-word;'>[GBB11; KSH12]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Leaky ReLU</td><td style='text-align: center; word-wrap: break-word;'>$ \max(a,0)+\alpha\min(a,0) $</td><td style='text-align: center; word-wrap: break-word;'>[-∞,∞]</td><td style='text-align: center; word-wrap: break-word;'>[MHN13]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Exponential linear unit</td><td style='text-align: center; word-wrap: break-word;'>$ \max(a,0)+\min(\alpha(e^{a}-1),0) $</td><td style='text-align: center; word-wrap: break-word;'>[-∞,∞]</td><td style='text-align: center; word-wrap: break-word;'>[CUH16]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Swish</td><td style='text-align: center; word-wrap: break-word;'>$ a\sigma(a) $</td><td style='text-align: center; word-wrap: break-word;'>[-∞,∞]</td><td style='text-align: center; word-wrap: break-word;'>[RZL17]</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GELU</td><td style='text-align: center; word-wrap: break-word;'>$ a\Phi(a) $</td><td style='text-align: center; word-wrap: break-word;'>[-∞,∞]</td><td style='text-align: center; word-wrap: break-word;'>[HG16]</td></tr></table>

<div style="text-align: center;">表13.4：一些常用的神经网络激活函数列表。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_186_412_535_645.jpg" alt="图像" width="30%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_617_415_964_645.jpg" alt="图像" width="30%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图13.14：(a) 一些常用的激活函数。(b) 它们的梯度曲线。由 activation_fun_deriv_jax.ipynb 生成。</div>

- 修改每一层的激活函数，以防止梯度过大或过小；参见第13.4.3节。

- 修改网络架构，使更新是加性的而非乘性的；参见第13.4.4节。

- 修改网络架构，使每一层的激活值标准化，从而在训练过程中数据集上的激活值分布保持恒定；参见第14.2.4.1节。

- 仔细选择参数的初始值；参见第13.4.5节。

#### 13.4.3 非饱和激活函数

在第13.2.3节中，我们提到Sigmoid激活函数在输入很大为负时饱和于0，在输入很大为正时饱和于1。结果表明在这些区域中梯度信号为0，从而阻止了反向传播的正常工作。

为了理解梯度消失的原因，考虑一个计算 $ \boldsymbol{z} = \sigma(\mathbf{W}\boldsymbol{x}) $ 的层，其中激活函数

---

函数为S型函数：

$$  \varphi(a)=\sigma(a)=\frac{1}{1+\exp(-a)}   \tag*{(13.71)}$$

如果权重初始化为较大值（正或负），则  $ \mathbf{a} = \mathbf{W}\mathbf{x} $ 很容易取较大值，从而导致  $ \mathbf{z} $ 在  $ \mathbf{0} $ 或  $ \mathbf{1} $ 附近饱和，因为S型函数会饱和，如图13.14a所示。

现在考虑梯度如何在该层中传播。激活函数（逐元素）的导数为

$$  \varphi^{\prime}(a)=\sigma(a)(1-\sigma(a))   \tag*{(13.72)}$$

图13.14b给出了其图示。根据链式法则，我们可以通过将S型非线性层  $ \mathbf{z} = \sigma(\mathbf{a}) $ 的雅可比矩阵（使用公式(13.43)）与线性层  $ \mathbf{a} = \mathbf{W}\mathbf{x} $ 的雅可比矩阵（使用公式(13.49)）相乘，得到该层关于输入的雅可比矩阵：

$$  \frac{\partial\boldsymbol{z}}{\partial\boldsymbol{x}}=\mathrm{diag}(\boldsymbol{z}(1-\boldsymbol{z})^{\top})\boldsymbol{W}   \tag*{(13.73)}$$

因此，如果 z 接近 0 或 1，关于输入的梯度将趋于 0。

类似地，该层关于参数的雅可比矩阵可以通过将公式(13.43)与公式(13.55)相乘得到：

$$  \frac{\partial z}{\partial\mathbf{W}}=z(1-z)\boldsymbol{x}^{\top}   \tag*{(13.74)}$$

因此，如果 z 接近 0 或 1，关于参数的梯度将趋于 0。

能够训练极深模型的关键之一在于使用非饱和激活函数。目前已经提出了几种不同的函数：表13.4给出了总结，更多细节请参见 https://mlfromscratch.com/activation-functions-explained。

##### 13.4.3.1 ReLU

最常用的是线性整流单元（rectified linear unit，简称ReLU），由[GBB11; KSH12]提出。其定义为

$$  \operatorname{ReLU}(a)=\max(a,0)=a\mathbb{I}\left(a>0\right)   \tag*{(13.75)}$$

ReLU函数简单地将负输入“关闭”，而正输入则保持不变。其梯度形式如下：

$$  \mathrm{ReLU}^{\prime}(a)=\mathbb{I}\left(a>0\right)   \tag*{(13.76)}$$

现在假设我们在某一层中使用它来计算  $ z = \text{ReLU}(\mathbf{W}x) $。利用第13.3.3节的结果，我们可以证明该层关于输入的雅可比矩阵形式为

$$  \frac{\partial\boldsymbol{z}}{\partial\boldsymbol{x}}=\mathbf{W}^{\mathsf{T}}\mathbb{I}\left(\boldsymbol{z}>\mathbf{0}\right)   \tag*{(13.77)}$$

作者：Kevin P. Murphy。 (C) MIT 出版社。CC-BY-NC-ND 许可协议。

---

对参数的梯度形式为

$$ \frac{\partial\boldsymbol{z}}{\partial\mathbf{W}}=\mathbb{I}\left(\boldsymbol{z}>\mathbf{0}\right)\boldsymbol{x}^{\top}   \tag*{(13.78)}$$

因此，只要 $\boldsymbol{z}$ 为正，梯度就不会消失。

不幸的是，当使用 ReLU 时，如果权重被初始化为大的负值，那么（某些分量上的）$\mathbf{a} = \mathbf{W} \mathbf{x}$ 很容易取大的负值，从而导致 $\mathbf{z}$ 变为 0。这将导致权重的梯度变为 0。算法将永远无法摆脱这种情况，因此隐藏单元（$\mathbf{z}$ 的分量）将永久关闭。这被称为“死亡 ReLU”问题 [Lu+19]。

##### 13.4.3.2 非饱和 ReLU

死亡 ReLU 问题可以通过使用 ReLU 的非饱和变体来解决。一种替代方案是 [MHN13] 提出的 leaky ReLU。其定义如下：

$$ \mathrm{LReLU}(a;\alpha)=\max(\alpha a,a)   \tag*{(13.79)}$$

其中 $0 < \alpha < 1$。该函数对正输入的斜率为 1，对负输入的斜率为 $\alpha$，从而确保即使输入为负，也有某些信号传递回前层。其图像见图 13.14b。如果允许参数 $\alpha$ 被学习而非固定，则 leaky ReLU 称为参数化 ReLU [He+15]。

另一个流行的选择是 [CUH16] 提出的 ELU。其定义如下：

$$ ELU(a;\alpha)=\begin{cases}\alpha(e^{a}-1)&若 a\leq0\\a&若 a>0\end{cases}   \tag*{(13.80)}$$

与 leaky ReLU 相比，其优势在于它是一个光滑函数。$^{6}$ 其图像见图 13.14。

ELU 的一个轻微变体称为 SELU（自归一化 ELU），由 [Kla+17] 提出。其形式如下：

$$ SELU(a;\alpha,\lambda)=\lambda ELU(a;\alpha)   \tag*{(13.81)}$$

令人惊讶的是，他们证明，通过将 $\alpha$ 和 $\lambda$ 设置为精心选取的值，该激活函数能够保证每一层的输出都是标准化的（前提是输入也是标准化的），即使没有使用诸如 batchnorm（第 14.2.4.1 节）等技术。这有助于模型拟合。

##### 13.4.3.3 其他选择

作为手动发现良好激活函数的替代方案，我们可以使用黑箱优化方法在函数形式空间中进行搜索。[RZL17] 采用了这种方法，发现了一种称为 swish 的函数，该函数在某些图像分类基准上表现良好。其定义如下：

$$ \mathrm{swish}(a;\beta)=a\sigma(\beta a)   \tag*{(13.82)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_197_127_974_409.jpg" alt="Image" width="67%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 13.15：(a) 残差块的示意图。(b) 在训练极深模型时添加残差连接为何有帮助的示意图。改编自 [Gér19] 的图 14.16。</div>


（同一函数，在 [HG16] 中独立提出，称为 SiLU（Sigmoid Linear Unit）。）其图形见图 13.14。

另一种流行的激活函数是 GELU，全称为“高斯误差线性单元”（Gaussian Error Linear Unit）[HG16]。其定义如下：

$$  \mathrm{GELU}(a)=a\Phi(a)   \tag*{(13.83)}$$

其中 $ \Phi(a) $ 是标准正态分布的累积分布函数：

$$  \Phi(a)=\Pr(\mathcal{N}(0,1)\leq a)=\frac{1}{2}\left(1+\operatorname{erf}(a/\sqrt{2})\right)   \tag*{(13.84)}$$

从图 13.14 可以看出，与大多数其他激活函数不同，该函数既不是凸函数也不是单调函数。

我们可以将 GELU 视为 ReLU 的一种“软”版本，因为它用高斯累积分布函数 $ \Phi(a) $ 替代了阶跃函数 $ \mathbb{I}(a > 0) $。另一种理解是，GELU 可被看作 dropout（第 13.5.4 节）的自适应版本，其中我们将输入乘以一个二值标量掩码 $ m \sim \text{Ber}(\Phi(a)) $，被丢弃的概率为 $ 1 - \Phi(a) $。因此期望输出为

$$  \mathbb{E}[a]=\Phi(a)\times a+(1-\Phi(a))\times0=a\Phi(a)   \tag*{(13.85)}$$

我们可以通过特定参数设置下的 swish 函数来近似 GELU，即

$$  \mathrm{GELU}(a)\approx a\sigma(1.702a)   \tag*{(13.86)}$$

#### 13.4.4 残差连接

解决深度神经网络梯度消失问题的一种方法是使用残差网络或 ResNet [He+16a]。这是一种前馈模型，其中每一层采用残差块的形式，其定义为

作者：Kevin P. Murphy。(C) MIT 出版社。CC-BY-NC-ND 许可。

---

由

$$  \mathcal{F}_{l}^{\prime}(\boldsymbol{x})=\mathcal{F}_{l}(\boldsymbol{x})+\boldsymbol{x}   \tag*{(13.87)}$$

其中 $ J_l $ 是一个标准的浅层非线性映射（例如，线性-激活-线性）。内部的 $ F_l $ 函数计算需要添加到输入 x 上的残差项或增量，以生成期望的输出；学习生成对输入的小扰动通常比直接预测输出更容易。（残差连接通常与 CNN 结合使用，如第 14.3.4 节所述，但也可用于 MLP。）

具有残差连接的模型与没有残差连接的模型具有相同数量的参数，但更易于训练。原因是梯度可以直接从输出流向较早的层，如图 13.15b 所示。为了理解这一点，注意到输出层的激活可以用任意前一层 l 表示为

$$  z_{L}=z_{l}+\sum_{i=l}^{L-1}\mathcal{F}_{i}(z_{i};\boldsymbol{\theta}_{i}).   \tag*{(13.88)}$$

因此，我们可以计算损失相对于第 l 层参数的梯度如下：

$$  \frac{\partial\mathcal{L}}{\partial\boldsymbol{\theta}_{l}}=\frac{\partial z_{l}}{\partial\boldsymbol{\theta}_{l}}\frac{\partial\mathcal{L}}{\partial z_{l}}   \tag*{(13.89)}$$

$$  =\frac{\partial z_{l}}{\partial\theta_{l}}\frac{\partial\mathcal{L}}{\partial z_{L}}\frac{\partial z_{L}}{\partial z_{l}}   \tag*{(13.90)}$$

$$  =\frac{\partial z_{l}}{\partial\boldsymbol{\theta}_{l}}\frac{\partial\mathcal{L}}{\partial z_{L}}\left(1+\sum_{i=l}^{L-1}\frac{\partial\mathcal{F}_{i}(z_{i};\boldsymbol{\theta}_{i})}{\partial z_{l}}\right)   \tag*{(13.91)}$$

$$  =\frac{\partial z_{l}}{\partial\theta_{l}}\frac{\partial\mathcal{L}}{\partial z_{L}}+其他项   \tag*{(13.92)}$$

因此我们看到，第 l 层的梯度直接依赖于第 L 层的梯度，且该依赖关系与网络的深度无关。

#### 13.4.5 参数初始化

由于 DNN 训练的目标函数是非凸的，初始化 DNN 参数的方式对最终解的类型以及函数训练的难易程度（即信息在模型中向前和向后传播的效果）起着重要作用。在本节的其余部分，我们将介绍一些用于初始化参数的常用启发式方法。

##### 13.4.5.1 启发式初始化方案

在 [GB10] 中，他们表明从具有固定方差的标准正态分布中采样参数可能导致激活值或梯度爆炸。为了理解原因，考虑一个没有激活函数的线性单元，其输出为 $ o_i = \sum_{j=1}^{n_{\text{in}}} w_{ij} x_j $；假设 $ w_{ij} \sim \mathcal{N}(0, \sigma^2) $，且 $ \mathbb{E}[x_j] = 0 $ 以及 $ \mathbb{V}[x_j] = \gamma^2 $，其中

---

我们假设 $x_j$ 与 $w_{ij}$ 独立。输出的均值和方差为

$$  \mathbb{E}\left[o_{i}\right]=\sum_{j=1}^{n_{\mathrm{i n}}}\mathbb{E}\left[w_{i j}x_{j}\right]=\sum_{j=1}^{n_{\mathrm{i n}}}\mathbb{E}\left[w_{i j}\right]\mathbb{E}\left[x_{j}\right]=0   \tag*{(13.93)}$$

$$  \mathbb{V}\left[o_{i}\right]=\mathbb{E}\left[o_{i}^{2}\right]-\left(\mathbb{E}\left[o_{i}\right]\right)^{2}=\sum_{j=1}^{n_{\mathrm{i n}}}\mathbb{E}\left[w_{i j}^{2}x_{j}^{2}\right]-0=\sum_{j=1}^{n_{\mathrm{i n}}}\mathbb{E}\left[w_{i j}^{2}\right]\mathbb{E}\left[x_{j}^{2}\right]=n_{\mathrm{i n}}\sigma^{2}\gamma^{2}   \tag*{(13.94)}$$

为了防止输出方差爆炸，我们需要确保 $n_{\mathrm{in}}\sigma^2 = 1$（或某个其他常数），其中 $n_{\mathrm{in}}$ 是一个单元的 **扇入**（传入连接数）。

现在考虑反向传播。通过类似推理，我们发现除非 $n_{\text{out}} \sigma^2 = 1$，否则梯度的方差可能爆炸，其中 $n_{\text{out}}$ 是一个单元的 **扇出**（传出连接数）。为了同时满足这两个要求，我们设置 $\frac{1}{2}(n_{\text{in}} + n_{\text{out}}) \sigma^2 = 1$，等价地

$$  \sigma^{2}=\frac{2}{n_{in}+n_{out}}   \tag*{(13.95)}$$

这被称为 **Xavier 初始化** 或 **Glorot 初始化**，以 [GB10] 的第一作者命名。

一个特例是使用 $\sigma^2 = 1/n_{\text{in}}$；这被称为 **LeCun 初始化**，以 Yann LeCun 的名字命名，他在 1990 年代提出了该方法。当 $n_{\text{in}} = n_{\text{out}}$ 时，它等价于 Glorot 初始化。如果使用 $\sigma^2 = 2/n_{\text{in}}$，该方法称为 **He 初始化**，以 Kaiming He 的名字命名，他在 [He+15] 中提出。

注意，不一定要使用高斯分布。实际上，上述推导仅涉及前两个矩（均值和方差），并未假设高斯性。例如，假设我们从均匀分布中采样权重 $w_{ij} \sim \text{Unif}(-a, a)$。均值为 0，方差为 $\sigma^2 = a^2 / 3$。因此我们应该设置 $a = \sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}$。

尽管上述推导假设了线性输出单元，但该技术即使对于非线性单元在经验上也能很好地工作。最佳初始化方法的选择取决于使用的激活函数。对于线性、tanh、logistic 和 softmax，推荐使用 Glorot。对于 ReLU 及其变体，推荐使用 He。对于 SELU，推荐使用 LeCun。更多启发式规则可参考 [Gér19]，相关理论可参考 [HDR19]。

##### 13.4.5.2 数据驱动的初始化

我们也可以采用数据驱动的方法进行参数初始化。例如，[MM16] 提出了一种简单但有效的方案，称为 **层序单位方差（LSUV）初始化**，其工作方式如下。首先，我们使用正交矩阵初始化每个（全连接或卷积）层的权重，如 [SMG14] 所提议的。（这可以通过从 $\mathbf{w} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 中采样，将 $\mathbf{w}$ 重塑为矩阵 $\mathbf{W}$，然后使用 QR 分解或 SVD 分解计算正交基来实现。）然后，对于每一层 $l$，我们计算小批量上激活值的方差 $v_l$；接着使用 $\mathbf{W}_l := \mathbf{W}_l / \sqrt{v_l}$ 进行重新缩放。该方案可以看作是正交初始化与仅在第一个小批次上执行的批量归一化的结合。这比完整的批量归一化更快，但有时效果同样好。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_303_119_876_377.jpg" alt="图片" width="49%" /></div>


<div style="text-align: center;">图13.16: 使用数据并行和两个GPU计算小批量随机梯度。来自 [Zha+20] 的图12.5.2，经Aston Zhang许可使用。</div>


#### 13.4.6 并行训练

在大数据集上训练大模型可能会非常缓慢。加速这一过程的一种方法是使用专用硬件，例如图形处理单元（GPU）和张量处理单元（TPU），这些硬件在执行矩阵-矩阵乘法时非常高效。如果我们拥有多个GPU，有时可以进一步加速。主要有两种方法：**模型并行**，即在不同机器间划分模型；以及**数据并行**，即每台机器拥有模型的一个副本，并将其应用于不同的数据子集。

模型并行可能相当复杂，因为它要求机器之间进行紧密通信以确保计算结果正确。我们不再进一步讨论。数据并行通常简单得多，因为它是一种**易并行**（embarassingly parallel）任务。为了利用这种方法加速训练，在每个训练步骤 $t$，我们执行以下操作：1) 将小批量划分到 $K$ 台机器上，得到 $\mathcal{D}_t^k$；2) 每台机器 $k$ 计算其自身的梯度 $g_t^k = \nabla_\theta \mathcal{L}(\theta; \mathcal{D}_t^k)$；3) 在中央机器（如设备0）上收集所有局部梯度，并使用 $g_t = \sum_{k=1}^K g_t^k$ 求和；4) 将求和后的梯度广播回所有设备，即 $\tilde{g}_t^k = g_t$；5) 每台机器使用 $\theta_t^k := \theta_t^k - \eta_t \tilde{g}_t^k$ 更新其自身的参数副本。参见图13.16的图示以及 multi_gpu_training_jax.ipynb 中的示例代码。

注意步骤3和步骤4通常合并为一个原子步骤；这被称为**全规约**（all-reduce）操作（我们使用求和将一组（梯度）向量归约成一个向量）。如果每台机器都阻塞直到接收到集中聚合后的梯度 $g_t$，该方法称为**同步训练**。这将得到与单台机器（使用更大的批量大小）训练相同的结果，只是速度更快（假设忽略任何批归一化层）。如果让每台机器使用自己的局部梯度估计更新参数，而不等待与其它机器的广播/接收，则该方法称为**异步训练**。这并不能保证有效，因为不同机器可能不同步，从而更新不同版本的参数；因此这种方法被称为**野性训练**（hogwild training）[Niu+11]。然而，如果更新是稀疏的，即每台机器“触及”参数向量的不同部分，则可以证明野性训练的行为类似于标准的同步SGD。

---

### 13.5 正则化

在第13.4节中，我们讨论了训练（大型）神经网络时涉及的计算问题。在本节中，我们将讨论统计问题。具体而言，我们重点关注避免过拟合的方法。这一点至关重要，因为大型神经网络很容易拥有数百万个参数。

#### 13.5.1 早停

防止过拟合最简单的方法或许是**早停**，这是一种启发式方法，指在验证集上的误差开始增大时停止训练过程（见图4.8中的示例）。该方法之所以有效，是因为它限制了优化算法从训练样本中向参数传递信息的能力，如[AS19]所述。

#### 13.5.2 权重衰减

减少过拟合的常用方法是对参数施加先验，然后使用最大后验估计。通常对权重使用高斯先验 $ \mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^2\mathbf{I}) $，对偏置使用 $ \mathcal{N}(\mathbf{b}|\mathbf{0},\beta^2\mathbf{I}) $。这等价于对目标函数进行 $ \ell_2 $ 正则化。在神经网络文献中，这被称为**权重衰减**，因为它鼓励较小的权重，从而得到更简单的模型，类似于岭回归（第11.3节）。

#### 13.5.3 稀疏深度神经网络

由于神经网络中有大量权重，因此鼓励稀疏性通常很有帮助。这使我们能够进行模型压缩，从而节省内存和时间。为此，我们可以使用 $ \ell_1 $ 正则化（如第11.4节）、ARD（如第11.7.7节）或其他几种方法（例如，近期综述见[Hoe+21; Bha+20]）。作为一个简单示例，图13.17展示了一个5层MLP，该网络通过对权重使用 $ \ell_1 $ 正则化器拟合某些一维回归数据。我们看到，结果图拓扑结构是稀疏的。

Illegal unit of measure (pt inserted). LaTeX Error: Environment subfigure undefined. Missing number, treated as zero.

尽管稀疏拓扑具有直观的吸引力，但在实践中这些方法并未得到广泛使用，因为现代GPU是针对密集矩阵乘法优化的，而稀疏权重矩阵带来的计算收益很小。然而，如果我们使用鼓励组稀疏性的方法，则可以剪除模型的整个层。这会产生块稀疏权重矩阵，从而带来速度提升和内存节省（例如，参见[Sca+17; Wen+16; MAV17; LUW17]）。

#### 13.5.4 随机失活

假设我们以概率p（针对每个样本随机地）关闭每个神经元的所有传出连接，如图13.18所示。这种技术被称为**随机失活**[Sri+14]。

随机失活可以显著减少过拟合，并且被广泛应用。直观上，随机失活之所以有效，是因为它防止了隐藏单元的复杂协同适应。换句话说，每个单元必须学会在即使其他单元随机缺失的情况下也能表现良好。这防止了

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND许可证。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_280_116_482_407.jpg" alt="Image" width="17%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_624_150_987_394.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图13.17：(a) 一个深而稀疏的神经网络。连接通过 $\ell_1$ 正则化进行剪枝。在每一层中，编号为0的节点被固定为1，因此其输出权重对应偏置项。(b) 模型在训练集上的预测结果。由 sparse_mlp.ipynb 生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_247_546_518_842.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_653_546_926_858.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图13.18：Dropout 示意图。(a) 一个具有两个隐藏层的标准神经网络。(b) 应用 dropout（$p_0 = 0.5$）后得到的稀疏网络示例。被丢弃的单元用 x 标记。图片源自 [Sri+14] 的图1，经 Geoff Hinton 许可使用。</div>

防止单元学习彼此之间复杂但脆弱的依赖关系。$^{7}$ 一种更正式的解释（基于高斯尺度混合先验）可参见 [NHLS19]。

我们可以将 dropout 视为对权重的一种带噪声版本的估计，即 $\theta_{lji} = w_{lji} \epsilon_{li}$，其中 $\epsilon_{li} \sim \mathrm{Ber}(1 - p)$ 是伯努利噪声项。（因此，如果采样得到 $\epsilon_{li} = 0$，那么从第 $l-1$ 层的单元 $i$ 指向第 $l$ 层任意单元 $j$ 的所有权重都将被置为零。）在测试阶段，我们通常关闭噪声。

---

为了确保测试时的权重期望与训练时相同（即神经元的输入激活在平均意义上保持一致），测试时应使用 $w_{lij} = \theta_{lji} \mathbb{E}[\epsilon_{li}]$。对于伯努利噪声，有 $\mathbb{E}[\epsilon] = 1 - p$，因此在预测前应将权重乘以保留概率 $1 - p$。

不过，如果愿意，我们也可以在测试时使用丢弃法。其结果是一个集成网络，每个网络具有略有不同的稀疏图结构。这被称为**蒙特卡洛丢弃法**[GG16; KG17]，其形式为

$$  p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})\approx\frac{1}{S}\sum_{s=1}^{S}p(\boldsymbol{y}|\boldsymbol{x},\hat{\boldsymbol{W}}\epsilon^{s}+\hat{\boldsymbol{b}})   \tag*{(13.96)}$$

其中 $S$ 是样本数，我们用 $\mathbf{W}\epsilon^{s}$ 表示将所有估计的权重矩阵乘以一个采样噪声向量。这有时能很好地近似贝叶斯后验预测分布 $p(\mathbf{y}|\mathbf{x},\mathcal{D})$，尤其是在噪声率经过优化的情况下[GHK17]。

#### 13.5.5 贝叶斯神经网络

现代深度神经网络通常使用（带惩罚的）最大似然目标进行训练，以找到单一参数设置。然而，对于大型模型，参数数量往往远多于数据点，因此可能存在多个模型在训练数据上拟合得同样好，但泛化方式却不同。捕获后验预测分布中的不确定性通常很有用。这可以通过对参数进行边缘化来实现，即计算

$$  p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})=\int p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})p(\boldsymbol{\theta}|\mathcal{D})d\boldsymbol{\theta}   \tag*{(13.97)}$$

其结果称为**贝叶斯神经网络**（BNN）。它可以被看作是一个由不同权重的神经网络构成的无限集成。通过边缘化参数，我们可以避免过拟合[Mac95]。贝叶斯边缘化对于大型神经网络具有挑战性，但也能带来显著的性能提升[WI20]。关于贝叶斯深度学习的更多细节，请参见本书的续作[Mur23]。

#### 13.5.6 （随机）梯度下降的正则化效应 *

某些优化方法（尤其是二阶批量方法）能够找到“大海捞针”般的解，即损失景观中狭窄但深的“洞”，对应参数设置的极低损失。这些被称为**尖锐最小值**，见图13.19（右）。从最小化经验损失的角度看，优化器做得很好。然而，这类解通常对应过拟合数据的模型。更好的选择是找到对应平坦最小值的点，如图13.19（左）所示；这类解更鲁棒，泛化能力更强。原因在于，平坦最小值对应参数空间中后验不确定性较大的区域，因此从该区域采样的模型不太可能精确记忆训练集中无关的细节[AS17]。随机梯度下降（SGD）通常通过添加噪声来找到这样的平坦最小值，这阻止了它“进入”损失景观中的狭窄区域（例如，参见[SL18]）。这被称为**隐式正则化**。我们也可以显式地鼓励

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_266_113_909_338.jpg" alt="图像" width="55%" /></div>

<div style="text-align: center;">图 13.19：平坦极小值与尖锐极小值。摘自文献 [HS97a] 的图 1 和图 2。经 Jürgen Schmidhuber 许可使用。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_240_434_516_631.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_648_435_924_631.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 13.20：每条曲线展示了给定小批量下损失随参数值的变化。(a) 稳定的局部极小值。(b) 不稳定的局部极小值。由 sgd_minima_variance.ipynb 生成。改编自 https://bit.ly/3wTc1L6。</div>

使用熵 SGD [Cha+17]、锐度感知最小化 [For+21]、随机权重平均 (SWA) [Izm+18] 及其他相关技术，SGD 可以找到这样的**平坦极小值**。

当然，损失景观不仅取决于参数值，还取决于数据。由于我们通常无法承受全批量梯度下降，因此会得到一组损失曲线，每条曲线对应一个小批量。如果每条曲线都对应于一个宽盆地，如图 13.20a 所示，那么我们就处于参数空间中一个对扰动鲁棒的点，并且很可能具有良好的泛化性能。然而，如果整体宽盆地是由多个不同窄盆地平均得到的，如图 13.20b 所示，那么得到的估计很可能泛化性能较差。

这可以通过文献 [Smi+21; BD21] 中的分析进行形式化。具体来说，他们考虑了近似 (S)GD 行为的连续时间梯度流。在 [BD21] 中，他们考虑了全批量 GD，并表明该梯度流的形式为 $ \dot{\boldsymbol{w}} = -\nabla_{\boldsymbol{w}} \tilde{\mathcal{L}}_{GD}(\boldsymbol{w}) $，其中

$$  \tilde{\mathcal{L}}_{G D}(\boldsymbol{w})=\mathcal{L}(\boldsymbol{w})+\frac{\epsilon}{4}||\nabla\mathcal{L}(\boldsymbol{w})||^{2}   \tag*{(13.98)}$$

这里 $ \mathcal{L}(\boldsymbol{w}) $ 是原始损失，$ \epsilon $ 是学习率，第二项是一个隐式正则化项，它惩罚具有大梯度（高曲率）的解。

---

在文献 [Smi+21] 中，他们将这一分析扩展到 SGD（随机梯度下降）情形。他们证明了该流的形式为 $ \dot{\boldsymbol{w}} = -\nabla_{\boldsymbol{w}} \tilde{\mathcal{L}}_{SGD}(\boldsymbol{w}) $，其中

$$  \tilde{\mathcal{L}}_{S G D}(\boldsymbol{w})=\mathcal{L}(\boldsymbol{w})+\frac{\epsilon}{4m}\sum_{k=1}^{m}||\nabla\mathcal{L}_{k}(\boldsymbol{w})||^{2}   \tag*{(13.99)}$$

这里 $m$ 是小批量的数量，$\mathcal{L}_{k}(\boldsymbol{w})$ 是第 $k$ 个小批量上的损失。将其与全批量梯度下降的损失比较，我们得到

$$  \tilde{\mathcal{L}}_{S G D}(\boldsymbol{w})=\tilde{\mathcal{L}}_{G D}(\boldsymbol{w})+\frac{\epsilon}{4m}\sum_{k=1}^{m}||\nabla\mathcal{L}_{k}(\boldsymbol{w})-\nabla\mathcal{L}(\boldsymbol{w})||^{2}   \tag*{(13.100)}$$

第二项估计了小批量梯度的方差，这是稳定性的度量，进而反映泛化能力。

上述分析表明，SGD 不仅具有计算优势（因为它比全批量梯度下降或二阶方法更快），还具备统计优势。

#### 13.5.7 过参数化模型

现代神经网络使用的参数数 $P$ 通常远多于训练样本数 $N$。这类模型被称为过参数化模型。因此，它们通常能达到零训练损失（至少在分类问题中如此）。尽管如此，它们往往泛化得比 $P \ll N$ 的模型更好。特别地，观察到当 $P < N$ 时，模型呈现常见的 U 型曲线：测试误差随 $P$ 增加先下降，然后随着模型开始过拟合而上升，这与第 4.7.6.3 节讨论的偏差-方差权衡预测一致。然而，当 $P > N$ 时，测试误差再次下降；这被称为 **双重下降现象** [HK92; Bel+19; Nak+19]。直观上，原因如下：当 $P = N$ 时，模型可能需要表示一个非常不光滑的函数来插值数据（见图 1.7c），但当 $P \gg N$ 时，模型可以用光滑函数插值数据（从而得到零训练误差）[BS21]。详情参见 [DMB21]。

### 13.6 其他类型的前馈网络  $ * $

#### 13.6.1 径向基函数网络

考虑一个单层神经网络，其隐藏层由特征向量给出

$$  \phi(\boldsymbol{x})=[\mathcal{K}(\boldsymbol{x},\boldsymbol{\mu}_{1}),\ldots,\mathcal{K}(\boldsymbol{x},\boldsymbol{\mu}_{K})]   \tag*{(13.101)}$$

其中 $\mu_k \in \mathcal{X}$ 是一组 $K$ 个质心或样本，$\mathcal{K}(\boldsymbol{x}, \boldsymbol{\mu}) \geq 0$ 是一个核函数。我们将在第 17.1 节详细描述核函数。这里仅给出一个例子，即高斯核

$$  \mathcal{K}_{\mathrm{gauss}}(\boldsymbol{x},\boldsymbol{c})\triangleq\exp\left(-\frac{1}{2\sigma^{2}}||\boldsymbol{c}-\boldsymbol{x}||_{2}^{2}\right)   \tag*{(13.102)}$$

参数 $\sigma$ 称为核的带宽。注意这个核是平移不变的，即它仅依赖于距离 $r = \| \boldsymbol{x} - \boldsymbol{c} \|_2$，因此我们可以等价地写成

$$  \mathcal{K}_{\mathrm{gauss}}(r)\triangleq\exp\left(-\frac{1}{2\sigma^{2}}r^{2}\right)   \tag*{(13.103)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_137_400_322.jpg" alt="图片" width="15%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_486_121_715_318.jpg" alt="图片" width="19%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_769_123_999_320.jpg" alt="图片" width="19%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图13.21: (a) xor（异或）真值表。(b) 使用10次多项式扩展拟合线性逻辑回归分类器。(c) 相同模型，但使用质心由4个黑色十字指定的RBF核。由logregXorDemo.ipynb生成。</div>

因此这被称为径向基函数核（radial basis function kernel）或RBF核。

一个使用方程(13.101)作为隐藏层且采用RBF核的单层神经网络称为RBF网络（RBF network）[BL88]。其形式为

$$  p(y|\boldsymbol{x};\boldsymbol{\theta})=p(y|\boldsymbol{w}^{\top}\boldsymbol{\phi}(\boldsymbol{x}))   \tag*{(13.104)}$$

其中 $\theta = (\mu, w)$。如果质心 $\mu$ 是固定的，我们可以使用（正则化）最小二乘法求解最优权重 $w$，如第11章所述。如果质心未知，我们可以通过无监督聚类方法（如K-means（第21.3节））对其进行估计。或者，我们可以为训练集中的每个数据点关联一个质心，得到 $\mu_n = x_n$，此时 $K = N$。这是一个非参数模型的例子，因为参数数量随着数据量增长（此处为线性增长），且不独立于 $N$。如果 $K = N$，模型可以完美插值数据，因此可能过拟合。然而，通过确保输出权重向量 $w$ 是稀疏的，模型只会使用输入训练样例的一个有限子集；这被称为稀疏核机（sparse kernel machine），将在第17.4.1节和第17.3节中详细讨论。另一种避免过拟合的方法是采用贝叶斯方法，通过对权重 $w$ 进行积分；这产生了称为高斯过程（Gaussian process）的模型，将在第17.2节中进一步讨论。

##### 13.6.1.1 用于回归的RBF网络

我们可以通过定义 $p(y|\boldsymbol{x},\boldsymbol{\theta}) = \mathcal{N}(\boldsymbol{w}^T \phi(\boldsymbol{x}), \sigma^2)$ 将RBF网络用于回归。例如，图13.22展示了一个一维数据集，使用 $K = 10$ 个均匀间隔的RBF原型进行拟合，但带宽从小到大变化。较小的值会导致函数非常曲折，因为预测函数值仅对靠近某个原型 $\mu_k$ 的点 $x$ 为非零。如果带宽非常大，则设计矩阵退化为全1常数矩阵，因为每个点与每个原型的距离几乎相同；因此对应的函数只是一条直线。

##### 13.6.1.2 用于分类的RBF网络

我们可以通过定义 $p(y|\boldsymbol{x},\boldsymbol{\theta}) = \mathrm{Ber}(\sigma(\boldsymbol{w}^{T}\phi(\boldsymbol{x})))$ 将RBF网络用于二分类。例如，考虑来自异或函数（exclusive or function）的数据。这是一个二值函数。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_373_124_799_549.jpg" alt="Image" width="36%" /></div>


<div style="text-align: center;">图13.22：一维中使用10个等间距RBF基函数的线性回归。左列：拟合函数。中列：在网格上评估的基函数。右列：设计矩阵。从上到下展示了核函数的不同带宽：$ \sigma = 0.5, 10, 50 $。由linregRbfDemo.ipynb生成。</div>


两个二进制输入的函数。其真值表如图13.21(a)所示。在图13.21(b)中，我们展示了一些用异或函数标记的数据，但为了图片更清晰，我们对点进行了抖动。$ ^{8} $我们看到，即使使用10次多项式也无法分离这些数据。然而，使用RBF核和仅4个原型就轻松解决了问题，如图13.21(c)所示。

#### 13.6.2 专家混合

当考虑回归问题时，通常假设输出分布是单峰的，例如高斯分布或学生t分布，其中均值和方差是输入的某个函数，即：

$$  p(\boldsymbol{y}|\boldsymbol{x})=\mathcal{N}(\boldsymbol{y}|f_{\mu}(\boldsymbol{x}),\mathrm{d i a g}(\sigma_{+}(f_{\sigma}(\boldsymbol{x})))   \tag*{(13.105)}$$

其中 $f$ 函数可以是MLP（可能具有一些共享隐藏单元，如图13.5所示）。然而，这对于一对多函数（每个输入可以有多个可能的输出）效果不佳。

图13.23a给出了这样一个函数的简单示例。我们看到，在图的中部，某些x值对应两个等概率的y值。这类问题在现实世界中很常见，例如从单张图像进行人体3D姿势预测$ [Bo+08] $，以及图像着色。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_254_131_501_330.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_662_132_909_330.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_254_380_501_576.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_662_384_908_577.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(d)</div>


<div style="text-align: center;">图 13.23：(a) 一个“一对多”函数的部分数据。横轴为输入 x，纵轴为目标 y = f(x)。(b) 每个专家在输入域上的责任。(c) 每个专家的预测（彩色线条）叠加在训练数据上。(d) 整体预测。均值为红色叉号，众数为黑色方块。改编自 [Bis06] 的图 5.20 和图 5.21。由 mixexpDemoOneToMany.ipynb 生成。</div>


黑白图像的着色 [Gua+17]、视频序列的未来帧预测 [VT17] 等，都属于此类问题。任何使用单峰输出密度最大化似然训练的模型——即便是灵活的**非线性模型**（如神经网络）——在处理此类“一对多”函数时都会表现不佳，因为这只会产生模糊的平均输出。

为了防止这种回归到均值的问题，我们可以采用 **条件混合模型**。即，假设输出是 K 个不同输出的加权混合，对应于每个输入 x 下输出分布的不同模态。在高斯情形下，该模型可表示为

$$  p(\boldsymbol{y}|\boldsymbol{x})=\sum_{k=1}^{K}p(\boldsymbol{y}|\boldsymbol{x},z=k)p(z=k|\boldsymbol{x})   \tag*{(13.106)}$$

$$  p(\boldsymbol{y}|\boldsymbol{x},z=k)=\mathcal{N}(\boldsymbol{y}|f_{\mu,k}(\boldsymbol{x}),\mathrm{d i a g}(f_{\sigma,k}(\boldsymbol{x})))   \tag*{(13.107)}$$

$$  p(z=k|\boldsymbol{x})=Cat(z|softmax(f_{z}(\boldsymbol{x})))   \tag*{(13.108)}$$

其中 $f_{\mu,k}$ 预测第 $k$ 个高斯分布的均值，$f_{\sigma,k}$ 预测其方差项，$f_{z}$ 则预测选用哪个混合分量。该模型称为 **混合专家模型** (MoE) [Jac+91; JJ94; YWG12; ME14]。其思想是：第 $k$ 个子模型 $p(\mathbf{y}|\mathbf{x},z=k)$ 被视为输入空间某一特定区域的“专家”，而函数 $p(z=k|\mathbf{x})$ 则称为 **门控函数**。

---

根据输入的值来决定使用哪个专家。通过为给定的输入x选择最可能的专家，我们可以“激活”模型的子集。这是**条件计算**的一个示例，因为我们根据门控网络先前计算的结果来决定运行哪个专家[Sha+17]。

我们可以使用 SGD 或 EM 算法来训练此模型（关于后者的详细信息，请参见第 8.7.3 节）。

##### 13.6.2.1 线性专家混合

在本节中，我们考虑一个简单的示例，其中使用线性回归专家和线性分类门控函数，即模型具有如下形式：

$$  p(y|\boldsymbol{x},z=k,\boldsymbol{\theta})=\mathcal{N}(y|\boldsymbol{w}_{k}^{\top}\boldsymbol{x},\sigma_{k}^{2})   \tag*{(13.109)}$$

$$  p(z=k|\boldsymbol{x},\boldsymbol{\theta})=\mathrm{Cat}(z|\mathrm{softmax}_{k}(\mathbf{V}\boldsymbol{x}))   \tag*{(13.110)}$$

其中 $\text{softmax}_k$ 是 softmax 函数的第 $k$ 个输出。单个权重项 $ p(z = k | \boldsymbol{x}) $ 称为专家 $k$ 对输入 $\boldsymbol{x}$ 的**责任度**。在图 13.23b 中，我们展示了门控网络如何在 $K = 3$ 个专家之间软性地划分输入空间。

每个专家 $ p(y|\boldsymbol{x},z=k) $ 对应一个具有不同参数的线性回归模型。这些在图 13.23c 中显示。

如果我们取专家的加权组合作为输出，会得到图 13.23d 中的红色曲线，显然这是一个糟糕的预测器。相反，如果我们只使用最活跃的专家（即责任度最高的专家）进行预测，会得到不连续的黑色曲线，这是一个好得多的预测器。

##### 13.6.2.2 混合密度网络

门控函数和专家可以是任意类型的条件概率模型，而不仅仅是线性模型。如果将它们都设为 DNN，则得到的模型称为**混合密度网络** (MDN) [Bis94; ZS14] 或**深度专家混合** [CGG17]。该模型的示意图见图 13.24。

##### 13.6.2.3 层次化 MOE

如果每个专家本身就是一个 MoE 模型，则得到的模型称为**层次化专家混合** [JJ94]。图 13.25 展示了一个具有两层层次结构的此类模型。

具有 L 层的 HME 可以看作是一棵深度为 L 的“软”决策树，其中每个样本都会经过树的每一个分支，最终预测是加权平均。（我们在第 18.1 节讨论决策树。）

### 13.7 习题

习题 13.1 [MLP 的反向传播]

（基于 Kevin Clark 的一道习题。）

作者：Kevin P. Murphy。(C) 麻省理工学院出版社。CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_325_193_828_505.jpg" alt="图片" width="43%" /></div>


<div style="text-align: center;">图13.24：包含m个专家的深度混合专家模型（Deep MOE），表示为神经网络。源自文献[CGG17]的图1，经Jacob Goldberger友好许可使用。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_383_703_789_1053.jpg" alt="图片" width="35%" /></div>


<div style="text-align: center;">图13.25：一个两层的层次化混合专家模型，表示为神经网络。顶层门控网络在左侧和右侧专家之间进行选择（由大框表示）；左侧和右侧专家自身又在其左子专家和右子专家之间进行选择。</div>

---

### 13.7. 练习

考虑如下具有一个隐藏层的分类MLP（多层感知机）：

$$  \boldsymbol{x}=\mathrm{i n p u t}\in\mathbb{R}^{D}   \tag*{(13.111)}$$

$$  z=\mathbf{W}\boldsymbol{x}+\boldsymbol{b}_{1}\in\mathbb{R}^{K}   \tag*{(13.112)}$$

$$  \boldsymbol{h}=\operatorname{ReLU}(\boldsymbol{z})\in\mathbb{R}^{K}   \tag*{(13.113)}$$

$$  \boldsymbol{a}=\mathbf{U}\boldsymbol{h}+\boldsymbol{b}_{2}\in\mathbb{R}^{C}   \tag*{(13.114)}$$

$$  \mathcal{L}=\operatorname{CrossEntropy}(\pmb{y},\operatorname{softmax}(\pmb{a}))\in\mathbb{R}   \tag*{(13.115)}$$

其中 $ \boldsymbol{x} \in \mathbb{R}^D $,  $ \boldsymbol{b}_1 \in \mathbb{R}^K $,  $ \boldsymbol{W} \in \mathbb{R}^{K \times D} $,  $ \boldsymbol{b}_2 \in \mathbb{R}^C $,  $ \boldsymbol{U} \in \mathbb{R}^{C \times K} $，这里 $ D $ 是输入大小， $ K $ 是隐藏单元数量， $ C $ 是类别数量。证明参数和输入的梯度如下：

$$  \nabla_{\mathbf{V}}\mathcal{L}=\left[\frac{\partial\mathcal{L}}{\partial\mathbf{V}}\right]_{1,:}=\boldsymbol{\delta}_{1}\boldsymbol{h}^{\top}\in\mathbb{R}^{C\times K}   \tag*{(13.116)}$$

$$  \nabla_{b_{2}}\mathcal{L}=\left(\frac{\partial\mathcal{L}}{\partial\boldsymbol{b}_{2}}\right)^{\top}=\boldsymbol{\delta}_{1}\in\mathbb{R}^{C}   \tag*{(13.117)}$$

$$  \nabla_{\mathbf{W}}\mathcal{L}=\left[\frac{\partial\mathcal{L}}{\partial\mathbf{W}}\right]_{1,:}=\boldsymbol{\delta}_{2}\mathbf{x}^{\top}\in\mathbb{R}^{K\times D}   \tag*{(13.118)}$$

$$  \nabla_{b_{1}}\mathcal{L}=\left(\frac{\partial\mathcal{L}}{\partial\boldsymbol{b}_{1}}\right)^{\top}=\boldsymbol{\delta}_{2}\in\mathbb{R}^{K}   \tag*{(13.119)}$$

$$  \nabla_{\mathbf{x}}\mathcal{L}=\left(\frac{\partial\mathcal{L}}{\partial\mathbf{x}}\right)^{\top}=\mathbf{W}^{\top}\;\boldsymbol{\delta}_{2}\in\mathbb{R}^{D}   \tag*{(13.120)}$$

其中损失函数关于两层（logit 层和隐藏层）的梯度由下式给出：

$$  \delta_{1}=\nabla_{a}\mathcal{L}=\left(\frac{\partial\mathcal{L}}{\partial\boldsymbol{a}}\right)^{\top}=\left(\boldsymbol{p}-\boldsymbol{y}\right)\in\mathbb{R}^{C}   \tag*{(13.121)}$$

$$  \delta_{2}=\nabla_{z}\mathcal{L}=\left(\frac{\partial\mathcal{L}}{\partial z}\right)^{\top}=\left(\mathbf{V}^{\top}\;\boldsymbol{\delta}_{1}\right)\odot H(\mathbf{z})\in\mathbb{R}^{K}   \tag*{(13.122)}$$

其中 $ H $ 是 Heaviside 函数（阶跃函数）。注意，在我们的符号中，梯度（与被求导变量形状相同）当变量是向量时等于雅可比矩阵的转置，当变量是矩阵时等于雅可比矩阵的第一切片。

---

请提供需要翻译的英文学术论文 Markdown 文本。

---

## 14 图像神经网络

### 14.1 引言

在第十三章中，我们讨论了多层感知机（MLPs）作为学习将“非结构化”输入向量 $ \boldsymbol{x} \in \mathbb{R}^D $ 映射到输出的函数的一种方式。在本章中，我们将扩展到输入 $ \boldsymbol{x} $ 具有二维空间结构的情况。（类似的想法适用于一维时间结构或三维时空结构。）

为了理解为什么将MLPs直接应用于图像数据不是一个好主意，请回想一下，MLP中每个隐藏层的核心操作是计算激活值 $ z = \varphi(\mathbf{W}\mathbf{x}) $，其中 $ x $ 是该层的输入，$ \mathbf{W} $ 是权重，$ \varphi() $ 是非线性激活函数。因此，隐藏层的第 $ j $ 个元素的值为 $ z_j = \varphi(\mathbf{w}_j^\top\mathbf{x}) $。我们可以将这个内积操作视为将输入 $ x $ 与学习到的模板或模式 $ \mathbf{w}_j $ 进行比较；如果匹配良好（大的正内积），则该单元被激活（假设使用ReLU非线性），表明输入中出现了第 $ j $ 个模式。

然而，当输入是可变大小的图像时，这种方法效果不佳，$ \boldsymbol{x} \in \mathbb{R}^{WHC} $，其中 $ W $ 是宽度，$ H $ 是高度，$ C $ 是输入通道数（例如，RGB颜色时 $ C = 3 $）。问题在于，对于不同大小的输入图像，我们需要学习不同大小的权重矩阵 $ \mathbf{W} $。此外，即使输入是固定大小的，对于合理大小的图像，所需的参数数量也是令人望而却步的，因为权重矩阵的大小为 $ (W \times H \times C) \times D $，其中 $ D $ 是输出数量（隐藏单元）。最后一个问题是，出现在一个位置的模式在另一个位置出现时可能无法被识别——即模型可能不具备平移不变性——因为权重不在位置之间共享（见图 Figure 14.1）。

为了解决这些问题，我们将使用卷积神经网络（CNNs），其中我们用卷积操作替代矩阵乘法。我们将在第 14.2 节中详细解释这一点，但基本思想是将输入划分为重叠的二维图像块，并将每个块与一组小的权重矩阵（或称滤波器）进行比较，这些滤波器表示物体的部分；这在图 Figure 14.2 中进行了说明。我们可以将其视为一种模板匹配。正如我们下面解释的那样，我们将从数据中学习这些模板。由于模板很小（通常仅为 3x3 或 5x5），参数数量显著减少。而且，由于我们使用卷积而非矩阵乘法来进行模板匹配，模型将具有平移不变性。这对于图像分类等任务非常有用，其目标是判断物体是否存在，而不管其位置如何。

除了图像分类之外，CNNs 还有许多其他应用，我们将在本章后面讨论。它们也可以应用于一维输入（见第 15.3 节）和三维输入；然而，我们主要

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_238_114_934_300.jpg" alt="图像" width="60%" /></div>


<div style="text-align: center;">图14.1：使用非结构化的MLP检测2D图像中的模式效果不佳，因为该方法不具备平移不变性。我们可以设计一个权重向量作为匹配滤波器来检测所需的十字形状。如果物体在左侧，这将产生5的强响应，但如果物体向右移动，则仅产生1的弱响应。改编自[SAV20]的图7.16。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_506_436_666_643.jpg" alt="图像" width="13%" /></div>


<div style="text-align: center;">图14.2：我们可以通过寻找出现在正确（相对）位置上的某些判别性特征（图像模板）来对数字进行分类。来自[Cho17]的图5.1。经Francois Chollet友好许可使用。</div>


本章重点讨论二维情况。

### 14.2 常见层

#### 14.2.1 卷积层

我们首先描述一维卷积的基本概念，然后介绍二维卷积，最后说明它们如何被用作CNN的关键组成部分。

##### 14.2.1.1 一维卷积

两个函数（例如 $f, g : \mathbb{R}^D \to \mathbb{R}$）之间的卷积定义为

$$  [f\circledast g](z)=\int_{\mathbb{R}^{D}}f(\boldsymbol{u})g(z-\boldsymbol{u})d\boldsymbol{u}   \tag*{(14.1)}$$

现在假设我们将函数替换为有限长度的向量，我们可以将这些向量视为定义在有限点集上的函数。例如，假设 $f$ 在点 $[-L, -L + \]$ 处求值

---

### 14.2. 常见层

$$ \begin{array}{l l l l l l l } \underline{ - & - & 1 & 2 & 3 & 4 & - & - } \\ 7 & 6 & 5 & - & - & - & - & - \\ - & 7 & 6 & 5 & - & - & - & - \\ - & - & 7 & 6 & 5 & - & - & - \\ - & - & - & 7 & 6 & 5 & - & - \\ - & - & - & - & 7 & 6 & 5 & - \\ - & - & - & - & - & 7 & 6 & 5 \\ \hline \end{array} \quad \begin{aligned} z_{0}&=x_{0}w_{0}=5\\z_{1}&=x_{0}w_{1}+x_{1}w_{0}=16\\z_{2}&=x_{0}w_{2}+x_{1}w_{1}+x_{2}w_{0}=34\\z_{3}&=x_{1}w_{2}+x_{2}w_{1}+x_{3}w_{0}=52\\z_{4}&=x_{2}w_{2}+x_{3}w_{1}=45\\z_{5}&=x_{3}w_{2}=28 \end{aligned} $$ 

<div style="text-align: center;">图 14.3：对 $\mathbf{x} = [1, 2, 3, 4]$ 与 $\mathbf{w} = [5, 6, 7]$ 进行离散卷积，得到 $\mathbf{z} = [5, 16, 34, 52, 45, 28]$。可以看出，该操作先“翻转” $\mathbf{w}$，然后将其在 $\mathbf{x}$ 上“滑动”，逐元素相乘，再求和得到结果。</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_218_406_952_502.jpg" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 14.4：一维互相关。引自文献 $[Zha+20]$ 的图 15.3.2。经 Aston Zhang 许可使用。</div>


在定义域 $\{ -L, \dots, 0, \dots, L\}$ 上对权重函数求值，得到权重向量（也称为滤波器或卷积核）$w_{-L}=f(-L)$ 至 $w_{L}=f(L)$。同样地，在点集 $\{-N, \dots, N\}$ 上对 $g$ 求值，得到特征向量 $x_{-N}=g(-N)$ 至 $x_{N}=g(N)$。于是上述方程变为

$$ [\boldsymbol{w}\circledast\boldsymbol{x}](i)=w_{-L}x_{i+L}+\cdots+w_{-1}x_{i+1}+w_{0}x_{i}+w_{1}x_{i-1}+\cdots+w_{L}x_{i-L} \tag*{(14.2)} $$

（我们稍后讨论边界条件（边缘效应）。）可以看出，我们先“翻转”权重向量 $\boldsymbol{w}$（因为 $\boldsymbol{w}$ 的索引被反转），然后将其在 $\boldsymbol{x}$ 向量上“滑动”，在每个位置对局部窗口求和，如图 14.3 所示。

有一种非常相关的运算，不先翻转 $\boldsymbol{w}$：

$$ [w*x](i)=w_{-L}x_{i-L}+\cdots+w_{-1}x_{i-1}+w_{0}x_{i}+w_{1}x_{i+1}+\cdots+w_{L}x_{i+L} \tag*{(14.3)} $$

这称为**互相关**；如果权重向量是对称的（常见情况），则互相关与卷积相同。在深度学习文献中，“卷积”通常指互相关；我们将遵循这一约定。

我们也可以将权重 $\boldsymbol{w}$ 定义在域 $\{0,1,\ldots,L-1\}$ 上，特征 $\boldsymbol{x}$ 定义在域 $\{0,1,\ldots,N-1\}$ 上，以消除负索引。于是上述方程变为

$$ [\boldsymbol{w}\circledast\boldsymbol{x}](i)=\sum_{u=0}^{L-1}w_{u}x_{i+u} \tag*{(14.4)} $$

示例如图 14.4 所示。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_222_132_946_404.jpg" alt="图像" width="62%" /></div>

<div style="text-align: center;">图14.5：二维互相关的示意图。由conv2d_jax.ipynb生成。改编自文献[Zha+20]的图6.2.1。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_328_497_847_706.jpg" alt="图像" width="45%" /></div>

<div style="text-align: center;">图14.6：将一个二维图像（左）与一个 $3 \times 3$ 的滤波器（中）进行卷积，产生一个二维响应图（右）。响应图中的亮斑对应于图像中包含向右下倾斜对角线的位置。改编自文献[Cho17]的图5.3。经Francois Chollet友好许可使用。</div>

##### 14.2.1.2 二维卷积

$$ [\mathbf{W}\circledast\mathbf{X}](i,j)=\sum_{u=0}^{H-1}\sum_{v=0}^{W-1}w_{u,v}x_{i+u,j+v} \tag*{(14.5)} $$

在二维情况下，方程(14.4)变为

其中二维滤波器W的大小为 $H \times W$。例如，考虑将一个 $3 \times 3$ 的输入X与一个 $2 \times 2$ 的核W进行卷积，计算得到一个 $2 \times 2$ 的输出Y：

$$ \begin{aligned}\mathbf{Y}&=\begin{pmatrix}w_{1}&w_{2}\\w_{3}&w_{4}\end{pmatrix}\circledast\begin{pmatrix}x_{1}&x_{2}&x_{3}\\x_{4}&x_{5}&x_{6}\\x_{7}&x_{8}&x_{9}\end{pmatrix}\\&=\begin{pmatrix}(w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{4}+w_{4}x_{5})&(w_{1}x_{2}+w_{2}x_{3}+w_{3}x_{5}+w_{4}x_{6})\\ (w_{1}x_{4}+w_{2}x_{5}+w_{3}x_{7}+w_{4}x_{8})&(w_{1}x_{5}+w_{2}x_{6}+w_{3}x_{8}+w_{4}x_{9})\end{pmatrix}\end{aligned} \tag*{(14.6)}$$

《概率机器学习：导论》。在线版本，2024年11月23日。