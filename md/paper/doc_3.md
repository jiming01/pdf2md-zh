<div style="text-align: center;"><img src="imgs/img_in_image_box_156_165_1031_618.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">Figure 2 | Attention architecture of DeepSeek-V3.2, where DSA is instantiated under MLA. The green part illustrates how DSA selects the top-k key-value entries according to the indexer.</div>


Dense Warm-up Stage. We first use a short warm-up stage to initialize the lightning indexer. In this stage, we keep dense attention and freeze all model parameters except for the lightning indexer. To align the indexer outputs with the main attention distribution, for the t-th query token, we first aggregate the main attention scores by summing across all attention heads. This sum is then L1-normalized along the sequence dimension to produce a target distribution  $ p_{t,:} \in \mathbb{R}^t $. Based on  $ p_{t,:} $, we set a KL-divergence loss as the training objective of the indexer:

 $$ \mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,:}\left\|\mathrm{S o f t m a x}\big(I_{t,:}\big)\right). $$ 

For warm-up, we use a learning rate of  $ 10^{-3} $. We train the indexer for only 1000 steps, with each step consisting of 16 sequences of 128K tokens, resulting in a total of 2.1B tokens.

Sparse Training Stage. Following indexer warm-up, we introduce the fine-grained token selection mechanism and optimize all model parameters to adapt the model to the sparse pattern of DSA. In this stage, we also keep aligning the indexer outputs to the main attention distribution, but considering only the selected token set  $ S_t = \{s \mid I_{t,s} \in \text{Top-k}(I_{t,:})\} $:

 $$ \mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,S_{t}}\left\|\mathrm{S o f t m a x}\big(I_{t,S_{t}}\big)\right). $$ 

It is worth noting that we detach the indexer input from the computational graph for separate optimization. The training signal of the indexer is from only  $ \mathcal{L}^I $, while the optimization of the main model is according to only the language modeling loss. In this sparse training stage, we use a learning rate of  $ 7.3 \times 10^{-6} $, and select 2048 key-value tokens for each query token. We train both the main model and the indexer for 15000 steps, with each step consisting of 480 sequences of 128K tokens, resulting in a total of 943.7B tokens.
<div style="text-align: center;"><img src="imgs/img_in_image_box_156_165_1031_618.jpg" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 2 | DeepSeek-V3.2 的注意力架构，其中 DSA 在 MLA 下实例化。绿色部分展示了 DSA 如何根据索引器选择 top-k 的键值对条目。</div>


> 密集预热阶段。我们首先使用一个简短的预热阶段来初始化闪电索引器。在此阶段，我们保持密集注意力，并冻结除闪电索引器之外的所有模型参数。为了使索引器输出与主注意力分布对齐，对于第 t 个查询令牌，我们首先通过在所有注意力头上求和来聚合主注意力分数。然后，该和沿序列维度进行 L1 归一化，以产生目标分布 $ p_{t,:} \in \mathbb{R}^t $。基于 $ p_{t,:} $，我们设定一个 KL 散度损失作为索引器的训练目标：
>
> $$ \mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,:}\left\|\mathrm{S o f t m a x}\big(I_{t,:}\big)\right). $$
>
> 对于预热，我们使用 $ 10^{-3} $ 的学习率。我们仅训练索引器 1000 步，每一步包含 16 个序列，每个序列有 128K 个令牌，总计 2.1B 个令牌。

> 稀疏训练阶段。在索引器预热之后，我们引入细粒度的令牌选择机制，并优化所有模型参数，以使模型适应 DSA 的稀疏模式。在此阶段，我们同样保持索引器输出与主注意力分布的对齐，但仅考虑选定的令牌集合 $ S_t = \{s \mid I_{t,s} \in \text{Top-k}(I_{t,:})\} $：
>
> $$ \mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,S_{t}}\left\|\mathrm{S o f t m a x}\big(I_{t,S_{t}}\big)\right). $$
>
> 值得注意的是，我们将索引器输入从计算图中分离出来进行单独优化。索引器的训练信号仅来自 $ \mathcal{L}^I $，而主模型的优化则仅根据语言建模损失。在此稀疏训练阶段，我们使用 $ 7.3 \times 10^{-6} $ 的学习率，并为每个查询令牌选择 2048 个键值令牌。我们同时训练主模型和索引器 15000 步，每一步包含 480 个序列，每个序列有 128K 个令牌，总计 943.7B 个令牌。