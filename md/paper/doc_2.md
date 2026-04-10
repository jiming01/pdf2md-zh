## 2. DeepSeek-V3.2 Architecture

### 2.1. DeepSeek Sparse Attention

DeepSeek-V3.2 uses exactly the same architecture as DeepSeek-V3.2-Exp. Compared with DeepSeek-V3.1-Terminus, the last version of DeepSeek-V3.1, the only architectural modification of DeepSeek-V3.2 is the introduction of DeepSeek Sparse Attention (DSA) through continued training.

Prototype of DSA. The prototype of DSA primarily consists of two components: a lightning indexer and a fine-grained token selection mechanism.

The lightning indexer computes the index score  $ I_{t,s} $ between the query token  $ \mathbf{h}_t \in \mathbb{R}^d $ and a preceding token  $ \mathbf{h}_s \in \mathbb{R}^d $, determining which tokens to be selected by the query token:

 $$ I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{R e L U}\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right), $$ 

where  $ H^I $ denotes the number of indexer heads;  $ \mathbf{q}_{t,j}^I \in \mathbb{R}^{d^I} $ and  $ w_{t,j}^I \in \mathbb{R} $ are derived from the query token  $ \mathbf{h}_t $; and  $ \mathbf{k}_s^I \in \mathbb{R}^{d^I} $ is derived from the preceding token  $ \mathbf{h}_s $. We choose ReLU as the activation function for throughput consideration. Given that the lightning indexer has a small number of heads and can be implemented in FP8, its computational efficiency is remarkable.

Given the index scores $\{I_{t,s}\}$ for each query token $\mathbf{h}_{t}$, our fine-grained token selection mechanism retrieves only the key-value entries $\{c_{s}\}$ corresponding to the top-k index scores. Then, the attention output $\mathbf{u}_{t}$ is computed by applying the attention mechanism between the query token $\mathbf{h}_{t}$ and the sparsely selected key-value entries $\{c_{s}\}$:

 $$ \mathbf{u}_{t}=\mathrm{A t t n}\big(\mathbf{h}_{t},\big\{\mathbf{c}_{s}\big|I_{t,s}\in\mathrm{T o p-k}\big(I_{t,:}\big)\big\}\big). $$ 

Instantiate DSA Under MLA. For the consideration of continued training from DeepSeek-V3.1-Terminus, we instantiate DSA based on MLA (DeepSeek-AI, 2024) for DeepSeek-V3.2. At the kernel level, each key-value entry must be shared across multiple queries for computational efficiency (Yuan et al., 2025). Therefore, we implement DSA based on the MQA (Shazeer, 2019) mode of MLA $ ^{1} $, where each latent vector (the key-value entry of MLA) will be shared across all query heads of the query token. The DSA architecture based on MLA is illustrated in Figure 2. We also provide an open-source implementation of DeepSeek-V3.2 $ ^{2} $ to specify the details unambiguously.

#### 2.1.1. Continued Pre-Training

Starting from a base checkpoint of DeepSeek-V3.1-Terminus, whose context length has been extended to 128K, we perform continued pre-training followed by post-training to create DeepSeek-V3.2.

The continued pre-training of DeepSeek-V3.2 consists of two training stages. For both stages, the distribution of training data is totally aligned with the 128K long context extension data used for DeepSeek-V3.1-Terminus.
## 2. DeepSeek-V3.2 架构

### 2.1. DeepSeek 稀疏注意力

DeepSeek-V3.2 使用的架构与 DeepSeek-V3.2-Exp 完全相同。与 DeepSeek-V3.1 系列的最后一个版本 DeepSeek-V3.1-Terminus 相比，DeepSeek-V3.2 在架构上唯一的修改是通过持续训练引入了 DeepSeek 稀疏注意力。

**DSA 的原型。** DSA 的原型主要由两个部分组成：一个闪电索引器和一个细粒度的令牌选择机制。

闪电索引器计算查询令牌 $\mathbf{h}_t \in \mathbb{R}^d$ 与前一个令牌 $\mathbf{h}_s \in \mathbb{R}^d$ 之间的索引分数 $I_{t,s}$，以确定查询令牌将选择哪些令牌：

$$ I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{R e L U}\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right), $$

其中 $H^I$ 表示索引器头的数量；$\mathbf{q}_{t,j}^I \in \mathbb{R}^{d^I}$ 和 $w_{t,j}^I \in \mathbb{R}$ 来自查询令牌 $\mathbf{h}_t$；而 $\mathbf{k}_s^I \in \mathbb{R}^{d^I}$ 来自前一个令牌 $\mathbf{h}_s$。出于吞吐量考虑，我们选择 ReLU 作为激活函数。鉴于闪电索引器头部数量少且可以用 FP8 实现，其计算效率非常出色。

给定每个查询令牌 $\mathbf{h}_{t}$ 的索引分数 $\{I_{t,s}\}$，我们的细粒度令牌选择机制仅检索与 top-k 索引分数对应的键值条目 $\{c_{s}\}$。然后，通过应用查询令牌 $\mathbf{h}_{t}$ 与稀疏选中的键值条目 $\{c_{s}\}$ 之间的注意力机制来计算注意力输出 $\mathbf{u}_{t}$：

$$ \mathbf{u}_{t}=\mathrm{A t t n}\big(\mathbf{h}_{t},\big\{\mathbf{c}_{s}\big|I_{t,s}\in\mathrm{T o p-k}\big(I_{t,:}\big)\big\}\big). $$

**在 MLA 下实例化 DSA。** 考虑到从 DeepSeek-V3.1-Terminus 进行持续训练的需求，我们基于 MLA 为 DeepSeek-V3.2 实例化了 DSA。在核心层面，为了计算效率，每个键值条目必须在多个查询之间共享。因此，我们基于 MLA 的 MQA 模式实现了 DSA，其中每个潜在向量将被查询令牌的所有查询头共享。基于 MLA 的 DSA 架构如图 2 所示。我们还提供了 DeepSeek-V3.2 的开源实现，以明确指定细节。

#### 2.1.1. 持续预训练

我们从上下文长度已扩展到 128K 的 DeepSeek-V3.1-Terminus 基础检查点开始，通过执行持续预训练和后训练来创建 DeepSeek-V3.2。

DeepSeek-V3.2 的持续预训练包含两个训练阶段。对于这两个阶段，训练数据的分布与用于 DeepSeek-V3.1-Terminus 的 128K 长上下文扩展数据完全一致。