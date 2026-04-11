
# DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

DeepSeek-AI

research@deepseek.com

## Abstract

We introduce DeepSeek-V3.2, a model that harmonizes high computational efficiency with superior reasoning and agent performance. The key technical breakthroughs of DeepSeek-V3.2 are as follows: (1) DeepSeek Sparse Attention (DSA): We introduce DSA, an efficient attention mechanism that substantially reduces computational complexity while preserving model performance in long-context scenarios. (2) Scalable Reinforcement Learning Framework: By implementing a robust reinforcement learning protocol and scaling post-training compute, DeepSeek-V3.2 performs comparably to GPT-5. Notably, our high-compute variant, DeepSeek-V3.2-Specialist, surpasses GPT-5 and exhibits reasoning proficiency on par with Gemini-3.0-Pro, achieving gold-medal performance in both the 2025 International Mathematical Olympiad (IMO) and the International Olympiad in Informatics (IOI). (3) Large-Scale Agentic Task Synthesis Pipeline: To integrate reasoning into tool-use scenarios, we developed a novel synthesis pipeline that systematically generates training data at scale. This methodology facilitates scalable agentic post-training, yielding substantial improvements in generalization and instruction-following robustness within complex, interactive environments.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_144_926_1045_1421.jpg" alt="Image" width="75%" /></div>

<div style="text-align: center;">Figure 1 | Benchmark of DeepSeek-V3.2 and its counterparts. For HMMT 2025, we report the February competition, consistent with the baselines. For HLE, we report the text-only subset.</div>

# DeepSeek-V3.2：开拓开放大语言模型的前沿

DeepSeek-AI

research@deepseek.com

## 摘要

> 我们介绍了DeepSeek-V3.2，这是一个**将高计算效率与卓越的推理和智能体性能相统一**的模型。DeepSeek-V3.2的关键技术突破如下：(1) DeepSeek稀疏注意力：我们引入了DSA，这是一种高效的注意力机制，能在长上下文场景中显著降低计算复杂度，同时保持模型性能。(2) 可扩展的强化学习框架：通过实施稳健的强化学习协议并扩展训练后计算，DeepSeek-V3.2的性能可与GPT-5相媲美。值得注意的是，我们的高计算变体DeepSeek-V3.2-Specialist超越了GPT-5，并展现出与Gemini-3.0-Pro相当的推理能力，在2025年国际数学奥林匹克竞赛和国际信息学奥林匹克竞赛中均取得了金牌成绩。(3) 大规模智能体任务合成流水线：为了将推理能力整合到工具使用场景中，我们开发了一种新颖的合成流水线，能够系统地大规模生成训练数据。这种方法促进了可扩展的智能体训练后优化，在复杂、交互式的环境中，**显著提升了模型的泛化能力和指令遵循的鲁棒性**。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_144_926_1045_1421.jpg" alt="Image" width="75%" /></div>

<div style="text-align: center;">图1 | DeepSeek-V3.2及其对应模型的基准测试。对于HMMT 2025，我们报告了2月的比赛结果，与基线保持一致。对于HLE，我们报告了纯文本子集的结果。</div>

---


## 1. Introduction

The release of reasoning models (DeepSeek-AI, 2025; OpenAI, 2024a) marked a pivotal moment in the evolution of Large Language Models (LLMs), catalyzing a substantial leap in overall performance across the verifiable fields. Since this milestone, the capabilities of LLMs have advanced rapidly. However, a distinct divergence has emerged in the past months. While the open-source community (MiniMax, 2025; MoonShot, 2025; ZhiPu-AI, 2025) continues to make strides, the performance trajectory of closed-source proprietary models (Anthropic, 2025b; DeepMind, 2025a; OpenAI, 2025) has accelerated at a significantly steeper rate. Consequently, rather than converging, the performance gap between closed-source and open-source models appears to be widening, with proprietary systems demonstrating increasingly superior capabilities in complex tasks.

Through our analysis, we identify three critical deficiencies that limit the capability of open-source models in complex tasks. First, architecturally, the predominant reliance on vanilla attention (Vaswani et al., 2017) mechanisms severely constrains efficiency for long sequences. This inefficiency poses a substantial obstacle to both scalable deployment and effective post-training. Second, regarding resource allocation, open-source models suffer from insufficient computational investment during the post-training phase, limiting their performance on hard tasks. Finally, in the context of AI agents, open-source models demonstrate a marked lag in generalization and instruction-following capabilities compared to their proprietary counterparts (EvalSys, 2025; Li et al., 2025; Luo et al., 2025), hindering their effectiveness in real deployment.

To address these critical limitations, we first introduce DSA, a highly efficient attention mechanism designed to substantially reduce computational complexity. This architecture effectively addresses the efficiency bottleneck, preserving model performance even in long-context scenarios. Second, we develop a stable and scalable RL protocol that allows for significant computational expansion during the post-training phase. Notably, this framework allocates a post-training computational budget exceeding 10% of the pre-training cost, unlocking advanced capabilities. Thirdly, we propose a novel pipeline to foster generalizable reasoning in tool-use scenarios. First, we implement a cold-start phase utilizing the DeepSeek-V3 (DeepSeek-AI, 2024) methodology to unify reasoning and tool-use within single trajectories. Subsequently, we advance to large-scale agentic task synthesis, where we generate over 1,800 distinct environments and 85,000 complex prompts. This extensive synthesized data drives the RL process, significantly enhancing the model's generalization and instruction-following capability in the agent context.

DeepSeek-V3.2 achieves similar performance with Kimi-k2-thinking and GPT-5 across multiple reasoning benchmarks. Furthermore, DeepSeek-V3.2 significantly advances the agentic capabilities of open models, demonstrating exceptional proficiency on the long-tail agent tasks introduced in EvalSys (2025); Li et al. (2025); Luo et al. (2025). DeepSeek-V3.2 emerges as a highly cost-efficient alternative in agent scenarios, significantly narrowing the performance gap between open and frontier proprietary models while incurring substantially lower costs. Notably, with the aim of pushing the boundaries of open models in the reasoning domain, we relaxed the length constraints to develop DeepSeek-V3.2-Speciale. As a result, DeepSeek-V3.2-Speciale achieves performance parity with the leading closed-source system, Gemini-3.0-Pro (DeepMind, 2025b). It shows gold-medal performance in the IOI 2025, ICPC World Final 2025, IMO 2025, and CMO 2025.
## 1. 引言

> 推理模型的发布标志着大型语言模型（LLMs）演进过程中的一个关键转折点，**极大地推动**了其在多个可验证领域的整体性能跃升。自这一里程碑以来，LLMs 的能力迅速发展。然而，在过去几个月中，一个明显的分化趋势开始显现。尽管开源社区持续取得进展，但闭源专有模型的性能提升轨迹却以**显著更陡峭的速度**在加速。因此，开源模型与闭源模型之间的性能差距非但没有缩小，反而似乎在扩大——专有系统在复杂任务上正展现出越来越**显著的优势**。

> 通过我们的分析，我们识别出限制开源模型在复杂任务中能力的三个关键缺陷。首先，在架构层面，对标准注意力机制的**过度依赖**严重限制了长序列的处理效率。这种低效性对规模化部署和有效的训练后调优都构成了巨大障碍。其次，在资源分配方面，开源模型在训练后阶段的计算投入不足，限制了其在困难任务上的表现。最后，在 AI 智能体领域，与专有模型相比，开源模型在泛化能力和指令遵循能力上表现出**明显的滞后**，这阻碍了其在真实部署中的有效性。

> 为了应对这些关键限制，我们首先引入了 DSA，这是一种旨在**大幅降低**计算复杂性的高效注意力机制。该架构有效解决了效率瓶颈，即使在长上下文场景中也能保持模型性能。其次，我们开发了一个稳定且可扩展的强化学习协议，使得在训练后阶段能够进行**大规模的计算扩展**。值得注意的是，该框架分配的训练后计算预算超过了预训练成本的 10%，从而解锁了高级能力。第三，我们提出了一种新颖的流程，以在工具使用场景中培养可泛化的推理能力。首先，我们采用 DeepSeek-V3 的方法实施冷启动阶段，将推理和工具使用统一在单一轨迹中。随后，我们推进到大规模的智能体任务合成，生成了超过 1,800 个不同的环境和 85,000 个复杂提示。这些海量的合成数据驱动了强化学习过程，**显著增强了**模型在智能体上下文中的泛化能力和指令遵循能力。

> DeepSeek-V3.2 在多个推理基准测试中，达到了与 Kimi-k2-thinking 和 GPT-5 相近的性能。此外，DeepSeek-V3.2 显著提升了开源模型的智能体能力，在 EvalSys；Li et al.；Luo et al. 引入的长尾智能体任务上展现了**卓越的熟练度**。DeepSeek-V3.2 成为了智能体场景中一个高性价比的替代方案，**在显著降低成本的同时**，大大缩小了开源模型与前沿专有模型之间的性能差距。值得注意的是，为了推动开源模型在推理领域的边界，我们放宽了长度限制，开发了 DeepSeek-V3.2-Speciale。其结果是，DeepSeek-V3.2-Speciale 实现了与领先的闭源系统 Gemini-3.0-Pro 的性能持平。它在 IOI 2025、ICPC World Final 2025、IMO 2025 和 CMO 2025 中展现了**金牌级别的表现**。

---


## 2. DeepSeek-V3.2 Architecture

### 2.1. DeepSeek Sparse Attention

DeepSeek-V3.2 uses exactly the same architecture as DeepSeek-V3.2-Exp. Compared with DeepSeek-V3.1-Terminus, the last version of DeepSeek-V3.1, the only architectural modification of DeepSeek-V3.2 is the introduction of DeepSeek Sparse Attention (DSA) through continued training.

Prototype of DSA. The prototype of DSA primarily consists of two components: a lightning indexer and a fine-grained token selection mechanism.

The lightning indexer computes the index score  $I_{t,s}$ between the query token  $\mathbf{h}_t \in \mathbb{R}^d$ and a preceding token  $\mathbf{h}_s \in \mathbb{R}^d$, determining which tokens to be selected by the query token:

$$
I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{R e L U}\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right),   \tag*{(1)}
$$

where  $H^I$ denotes the number of indexer heads;  $\mathbf{q}_{t,j}^I \in \mathbb{R}^{d^I}$ and  $w_{t,j}^I \in \mathbb{R}$ are derived from the query token  $\mathbf{h}_t$; and  $\mathbf{k}_s^I \in \mathbb{R}^{d^I}$ is derived from the preceding token  $\mathbf{h}_s$. We choose ReLU as the activation function for throughput consideration. Given that the lightning indexer has a small number of heads and can be implemented in FP8, its computational efficiency is remarkable.

Given the index scores $\{I_{t,s}\}$for each query token$\mathbf{h}_{t}$, our fine-grained token selection mechanism retrieves only the key-value entries $\{c_{s}\}$corresponding to the top-k index scores. Then, the attention output$\mathbf{u}_{t}$is computed by applying the attention mechanism between the query token$\mathbf{h}_{t}$and the sparsely selected key-value entries$\{c_{s}\}$:

$$
\mathbf{u}_{t}=\mathrm{A t t n}\big(\mathbf{h}_{t},\big\{\mathbf{c}_{s}\big|I_{t,s}\in\mathrm{T o p-k}\big(I_{t,:}\big)\big\}\big).   \tag*{(2)}
$$

Instantiate DSA Under MLA. For the consideration of continued training from DeepSeek-V3.1-Terminus, we instantiate DSA based on MLA (DeepSeek-AI, 2024) for DeepSeek-V3.2. At the kernel level, each key-value entry must be shared across multiple queries for computational efficiency (Yuan et al., 2025). Therefore, we implement DSA based on the MQA (Shazeer, 2019) mode of MLA $^{1}$, where each latent vector (the key-value entry of MLA) will be shared across all query heads of the query token. The DSA architecture based on MLA is illustrated in Figure 2. We also provide an open-source implementation of DeepSeek-V3.2 $^{2}$ to specify the details unambiguously.

#### 2.1.1. Continued Pre-Training

Starting from a base checkpoint of DeepSeek-V3.1-Terminus, whose context length has been extended to 128K, we perform continued pre-training followed by post-training to create DeepSeek-V3.2.

The continued pre-training of DeepSeek-V3.2 consists of two training stages. For both stages, the distribution of training data is totally aligned with the 128K long context extension data used for DeepSeek-V3.1-Terminus.
## 2. DeepSeek-V3.2 架构

### 2.1. DeepSeek 稀疏注意力

> DeepSeek-V3.2 使用的架构与 DeepSeek-V3.2-Exp 完全相同。与 DeepSeek-V3.1 系列的最后一个版本 DeepSeek-V3.1-Terminus 相比，DeepSeek-V3.2 在架构上**唯一的**修改是通过持续训练引入了 DeepSeek 稀疏注意力。

> **DSA 的原型**。DSA 的原型主要由两个组件构成：一个闪电索引器和一个细粒度的令牌选择机制。

> 闪电索引器计算查询令牌 $\mathbf{h}_t \in \mathbb{R}^d$ 与一个先前令牌 $\mathbf{h}_s \in \mathbb{R}^d$ 之间的索引得分 $I_{t,s}$，以确定哪些令牌将被查询令牌选中：

$$
I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{R e L U}\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right),   \tag*{(1)}
$$

> 其中 $H^I$ 表示索引器头的数量；$\mathbf{q}_{t,j}^I \in \mathbb{R}^{d^I}$ 和 $w_{t,j}^I \in \mathbb{R}$ 派生自查询令牌 $\mathbf{h}_t$；而 $\mathbf{k}_s^I \in \mathbb{R}^{d^I}$ 派生自先前令牌 $\mathbf{h}_s$。出于吞吐量的考虑，我们选择 ReLU 作为激活函数。鉴于闪电索引器头数较少且可以用 FP8 实现，其计算效率**非常出色**。

> 对于每个查询令牌 $\mathbf{h}_{t}$，给定其索引得分 $\{I_{t,s}\}$，我们的细粒度令牌选择机制仅检索与得分前 k 名对应的键值条目 $\{c_{s}\}$。然后，通过在查询令牌 $\mathbf{h}_{t}$ 与稀疏选中的键值条目 $\{c_{s}\}$ 之间应用注意力机制来计算注意力输出 $\mathbf{u}_{t}$：

$$
\mathbf{u}_{t}=\mathrm{A t t n}\big(\mathbf{h}_{t},\big\{\mathbf{c}_{s}\big|I_{t,s}\in\mathrm{T o p-k}\big(I_{t,:}\big)\big\}\big).   \tag*{(2)}
$$

> **在 MLA 框架下实例化 DSA**。考虑到从 DeepSeek-V3.1-Terminus 进行持续训练的需求，我们基于 MLA (DeepSeek-AI, 2024) 为 DeepSeek-V3.2 实例化了 DSA。在核心层面，为了计算效率，每个键值条目必须在多个查询之间共享 (Yuan et al., 2025)。因此，我们基于 MLA 的 MQA 模式 (Shazeer, 2019) 实现了 DSA $^{1}$，其中每个潜在向量（MLA 的键值条目）将在查询令牌的所有查询头之间共享。基于 MLA 的 DSA 架构如图 2 所示。我们还提供了 DeepSeek-V3.2 的开源实现 $^{2}$，以**明确无误地**说明细节。

#### 2.1.1. 持续预训练

> 我们从上下文长度已扩展至 128K 的 DeepSeek-V3.1-Terminus 基础检查点出发，通过执行持续预训练和后续训练来创建 DeepSeek-V3.2。

> DeepSeek-V3.2 的持续预训练包含两个训练阶段。对于这两个阶段，训练数据的分布与用于 DeepSeek-V3.1-Terminus 的 128K 长上下文扩展数据**完全一致**。

---


<div style="text-align: center;"><img src="imgs/img_in_image_box_156_165_1031_618.jpg" alt="Image" width="73%" /></div>

<div style="text-align: center;">Figure 2 | Attention architecture of DeepSeek-V3.2, where DSA is instantiated under MLA. The green part illustrates how DSA selects the top-k key-value entries according to the indexer.</div>

Dense Warm-up Stage. We first use a short warm-up stage to initialize the lightning indexer. In this stage, we keep dense attention and freeze all model parameters except for the lightning indexer. To align the indexer outputs with the main attention distribution, for the t-th query token, we first aggregate the main attention scores by summing across all attention heads. This sum is then L1-normalized along the sequence dimension to produce a target distribution  $p_{t,:} \in \mathbb{R}^t$. Based on  $p_{t,:}$, we set a KL-divergence loss as the training objective of the indexer:

$$
\mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,:}\left\|\mathrm{S o f t m a x}\big(I_{t,:}\big)\right).   \tag*{(3)}
$$

For warm-up, we use a learning rate of  $10^{-3}$. We train the indexer for only 1000 steps, with each step consisting of 16 sequences of 128K tokens, resulting in a total of 2.1B tokens.

Sparse Training Stage. Following indexer warm-up, we introduce the fine-grained token selection mechanism and optimize all model parameters to adapt the model to the sparse pattern of DSA. In this stage, we also keep aligning the indexer outputs to the main attention distribution, but considering only the selected token set  $S_t = \{s \mid I_{t,s} \in \text{Top-k}(I_{t,:})\}$:

$$
\mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,S_{t}}\left\|\mathrm{S o f t m a x}\big(I_{t,S_{t}}\big)\right).   \tag*{(4)}
$$

It is worth noting that we detach the indexer input from the computational graph for separate optimization. The training signal of the indexer is from only  $\mathcal{L}^I$, while the optimization of the main model is according to only the language modeling loss. In this sparse training stage, we use a learning rate of  $7.3 \times 10^{-6}$, and select 2048 key-value tokens for each query token. We train both the main model and the indexer for 15000 steps, with each step consisting of 480 sequences of 128K tokens, resulting in a total of 943.7B tokens.
<div style="text-align: center;"><img src="imgs/img_in_image_box_156_165_1031_618.jpg" alt="Image" width="73%" /></div>

<div style="text-align: center;">图 2 | DeepSeek-V3.2 的注意力架构，其中 DSA 在 MLA 下实例化。绿色部分说明了 DSA 如何根据索引器选择 top-k 键值条目。</div>

> **密集预热阶段**。我们首先使用一个短暂的预热阶段来初始化闪电索引器。在此阶段，我们保持密集注意力，并冻结除闪电索引器外的所有模型参数。为了使索引器输出与主注意力分布对齐，对于第 t 个查询令牌，我们首先通过对所有注意力头的注意力分数求和进行聚合。然后，该总和沿序列维度进行 L1 归一化，以产生目标分布 $p_{t,:} \in \mathbb{R}^t$。基于 $p_{t,:}$，我们设定一个 KL 散度损失作为索引器的训练目标：

$$
\mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,:}\left\|\mathrm{S o f t m a x}\big(I_{t,:}\big)\right).   \tag*{(3)}
$$

> 对于预热，我们使用 $10^{-3}$ 的学习率。我们仅训练索引器 1000 步，每一步包含 16 个 128K 令牌的序列，总计 2.1B 令牌。

> **稀疏训练阶段**。在索引器预热之后，我们引入细粒度的令牌选择机制，并优化所有模型参数，以使模型适应 DSA 的稀疏模式。在此阶段，我们**同样**保持索引器输出与主注意力分布的对齐，但仅考虑被选中的令牌集合 $S_t = \{s \mid I_{t,s} \in \text{Top-k}(I_{t,:})\}$：

$$
\mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,S_{t}}\left\|\mathrm{S o f t m a x}\big(I_{t,S_{t}}\big)\right).   \tag*{(4)}
$$

> 值得注意的是，我们将索引器输入从计算图中分离出来以进行单独优化。索引器的训练信号**仅**来自 $\mathcal{L}^I$，而主模型的优化则**仅**依据语言建模损失。在此稀疏训练阶段，我们使用 $7.3 \times 10^{-6}$ 的学习率，并为每个查询令牌选择 2048 个键值令牌。我们训练主模型和索引器 15000 步，每一步包含 480 个 128K 令牌的序列，总计 943.7B 令牌。

---


### 2.2. Parity Evaluation

Standard Benchmark In September 2025, we evaluate DeepSeek-V3.2-Exp on a suite of benchmarks, which focus on diverse capabilities, and compare it with DeepSeek-V3.1-Terminus showing similar performance. While DeepSeek V3.2 Exp significantly improves computational efficiency on long sequences, we do not observe substantial performance degradation compared with DeepSeek-V3.1-Terminus, on both short- and long-context tasks.

Human Preference Given that direct human preference assessments are inherently susceptible to bias, we employ ChatbotArena as an indirect evaluation framework to approximate user preferences for the newly developed base models. Both DeepSeek-V3.1-Terminus and DeepSeek-V3.2-Exp share an identical post-training strategy, and their Elo scores, obtained from evaluations conducted on 10 November 2025, are closely matched. These results suggest that the new base model achieves performance on par with the previous iteration, despite incorporating a sparse attention mechanism.

Long Context Eval Following the release of DeepSeek-V3.2-Exp, several independent long-context evaluations were conducted using previously unseen test sets. A representative benchmark is AA-LCR $^{3}$, in which DeepSeek-V3.2-Exp scores four points higher than DeepSeek-V3.1-Terminus in reasoning mode. In the Fiction.liveBench evaluation $^{4}$, DeepSeek-V3.2-Exp consistently outperforms DeepSeek-V3.1-Terminus across multiple metrics. This evidence indicates the base checkpoint of DeepSeek-V3.2-Exp does not regress on long context tasks.

### 2.3. Inference Costs

DSA reduces the core attention complexity of the main model from  $O(L^{2})$ to  $O(Lk)$, where  $k \ll L$ is the number of selected tokens. Although the lightning indexer still has a complexity of  $O(L^{2})$, it requires much less computation compared with MLA in DeepSeek-V3.1-Terminus. Combined with our optimized implementation, DSA achieves a significant end-to-end speedup in long-context scenarios. Figure 3 presents how token costs of DeepSeek-V3.1-Terminus and DeepSeek-V3.2 vary with the token position in the sequence. These costs are estimated from benchmarking the actual service deployed on H800 GPUs, at a rental price of 2 USD per GPU hour. Note that for short-sequence prefilling, we specially implement a masked MHA mode to simulate DSA, which can achieve higher efficiency under short-context conditions.

## 3. Post-Training

After continued pre-training, we perform post-training to create the final DeepSeek-V3.2. The post-training of DeepSeek-V3.2 also employs sparse attention in the same way as the sparse continued pre-training stage. For DeepSeek-V3.2, we maintain the same post-training pipeline as in DeepSeek-V3.2-Exp, which includes specialist distillation and mixed RL training.

Specialist Distillation For each task, we initially develop a specialized model dedicated exclusively to that particular domain, with all specialist models being fine-tuned from the same
### 2.2. 对等性评估

标准基准测试
> 2025年9月，我们在**一系列**专注于多样化能力的基准测试上评估了 DeepSeek-V3.2-Exp，并将其与 DeepSeek-V3.1-Terminus 进行比较，结果显示两者性能相近。尽管 DeepSeek-V3.2-Exp 在长序列上的计算效率**显著提升**，但在短上下文和长上下文任务中，我们均未观察到与 DeepSeek-V3.1-Terminus 相比存在**显著的性能下降**。

人类偏好评估
> 鉴于直接的人类偏好评估**本身容易受偏见影响**，我们采用 ChatbotArena 作为间接评估框架，以近似衡量用户对新开发的基础模型的偏好。DeepSeek-V3.1-Terminus 和 DeepSeek-V3.2-Exp 采用完全相同的后训练策略，且它们在2025年11月10日评估中获得的 Elo 分数非常接近。这些结果表明，尽管新基础模型引入了稀疏注意力机制，但其性能达到了与前一版本**旗鼓相当**的水平。

长上下文评估
> 在 DeepSeek-V3.2-Exp 发布后，多个独立的长上下文评估使用先前未见过的测试集相继展开。一个代表性的基准是 AA-LCR$^{3}$，其中 DeepSeek-V3.2-Exp 在推理模式下的得分比 DeepSeek-V3.1-Terminus 高出四分。在 Fiction.liveBench 评估$^{4}$中，DeepSeek-V3.2-Exp 在多项指标上**持续优于** DeepSeek-V3.1-Terminus。这些证据表明，DeepSeek-V3.2-Exp 的基础检查点在长上下文任务上**并未出现性能衰退**。

### 2.3. 推理成本

> DSA 将主模型的核心注意力复杂度从 $O(L^{2})$ 降低到 $O(Lk)$，其中 $k \ll L$ 是所选令牌的数量。尽管闪电索引器仍然具有 $O(L^{2})$ 的复杂度，但与 DeepSeek-V3.1-Terminus 中的 MLA 相比，其所需计算量**大大减少**。结合我们优化的实现，DSA 在长上下文场景中实现了**显著的端到端加速**。图 3 展示了 DeepSeek-V3.1-Terminus 和 DeepSeek-V3.2 的令牌成本如何随序列中令牌位置的变化而变化。这些成本是基于部署在 H800 GPU 上的实际服务（租赁价格为每小时每 GPU 2 美元）进行基准测试估算得出的。请注意，对于短序列预填充，我们专门实现了一种掩码 MHA 模式来模拟 DSA，该模式在短上下文条件下可以实现更高的效率。

## 3. 后训练

> 在持续预训练之后，我们进行后训练以创建最终的 DeepSeek-V3.2。DeepSeek-V3.2 的后训练也采用了与稀疏持续预训练阶段相同的方式使用稀疏注意力。对于 DeepSeek-V3.2，我们保持了与 DeepSeek-V3.2-Exp 相同的后训练流程，包括专家蒸馏和混合强化学习训练。

专家蒸馏
> 针对每项任务，我们首先开发一个专门致力于该特定领域的专家模型，所有专家模型均从同一个基础检查点微调而来。

---


<div style="text-align: center;"><img src="imgs/img_in_chart_box_154_187_573_495.jpg" alt="Image" width="35%" /></div>

<div style="text-align: center;">(a) Prefilling</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_611_188_1031_498.jpg" alt="Image" width="35%" /></div>

<div style="text-align: center;">(b) Decoding</div>

<div style="text-align: center;">Figure 3 | Inference costs of DeepSeek-V3.1-Terminus and DeepSeek-V3.2 on H800 clusters.</div>

pre-trained DeepSeek-V3.2 base checkpoint. In addition to writing tasks and general question-answering, our framework encompasses six specialized domains: mathematics, programming, general logical reasoning, general agentic tasks, agentic coding, and agentic search, with all the domains supporting both thinking and non-thinking modes. Each specialist is trained with large-scale Reinforcement Learning (RL) computing. Furthermore, we employ different models to generate training data for long chain-of-thought reasoning (thinking mode) and direct response generation (non-thinking mode). Once the specialist models are prepared, they are used to produce the domain-specific data for the final checkpoint. Experimental results demonstrate that models trained on the distilled data achieve performance levels only marginally below those of domain-specific specialists, with the performance gap being effectively eliminated through subsequent RL training.

Mixed RL Training For DeepSeek-V3.2, we still adopt Group Relative Policy Optimization (GRPO) (DeepSeek-AI, 2025; Shao et al., 2024) as the RL training algorithm. As DeepSeek-V3.2-Exp, we merge reasoning, agent, and human alignment training into one RL stage. This approach effectively balances performance across diverse domains while circumventing the catastrophic forgetting issues commonly associated with multi-stage training paradigms. For reasoning and agent tasks, we employ rule-based outcome reward, length penalty, and language consistency reward. For general tasks, we employ a generative reward model where each prompt has its own rubrics for evaluation.

DeepSeek-V3.2 and DeepSeek-V3.2-Speciale DeepSeek-V3.2 integrates reasoning, agent, and human alignment data distilled from specialists, undergoing thousands of steps of continued RL training to reach the final checkpoints. To investigate the potential of extended thinking, we also developed an experimental variant, DeepSeek-V3.2-Speciale. This model was trained exclusively on reasoning data with a reduced length penalty during RL. Additionally, we incorporated the dataset and reward method from DeepSeekMath-V2 (Shao et al., 2025) to enhance capabilities in mathematical proofs.

We would like to highlight our efforts in how to create a stable recipe to scale up RL compute in Section 3.1, and how to integrate thinking into agentic tasks in Section 3.2
<div style="text-align: center;"><img src="imgs/img_in_chart_box_154_187_573_495.jpg" alt="Image" width="35%" /></div>

<div style="text-align: center;">(a) 预填充</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_611_188_1031_498.jpg" alt="Image" width="35%" /></div>

<div style="text-align: center;">(b) 解码</div>

<div style="text-align: center;">图 3 | DeepSeek-V3.1-Terminus 与 DeepSeek-V3.2 在 H800 集群上的推理成本。</div>

> 预训练的 DeepSeek-V3.2 基础检查点。除了写作任务和通用问答外，我们的框架还涵盖了六个专业领域：数学、编程、通用逻辑推理、通用智能体任务、智能体编码以及智能体搜索，所有领域均支持思考模式和非思考模式。每个专家模型都通过**大规模强化学习计算**进行训练。此外，我们采用不同的模型来生成长链思维推理和直接响应生成所需的训练数据。一旦专家模型准备就绪，它们便被用于为最终检查点生成特定领域的数据。实验结果表明，**在蒸馏数据上训练的模型，其性能水平仅略低于领域特定专家模型，且性能差距通过后续的强化学习训练得以有效消除**。

> 混合强化学习训练对于 DeepSeek-V3.2，我们仍然采用组相对策略优化作为强化学习训练算法。与 DeepSeek-V3.2-Exp 类似，我们将推理、智能体和人类对齐训练合并到一个强化学习阶段中。这种方法**有效地平衡了不同领域的性能**，同时规避了多阶段训练范式中常见的灾难性遗忘问题。对于推理和智能体任务，我们采用基于规则的结果奖励、长度惩罚和语言一致性奖励。对于通用任务，我们则采用生成式奖励模型，其中每个提示都有其自己的评估标准。

> DeepSeek-V3.2 和 DeepSeek-V3.2-Speciale DeepSeek-V3.2 整合了从专家模型蒸馏出的推理、智能体和人类对齐数据，并经过数千步的持续强化学习训练以达到最终检查点。为了探索扩展思维的潜力，我们还开发了一个实验变体，DeepSeek-V3.2-Speciale。该模型**专门在强化学习期间以降低长度惩罚的方式，在推理数据上进行训练**。此外，我们整合了 DeepSeekMath-V2 的数据集和奖励方法，以增强其数学证明能力。

> 我们想重点强调我们在 **3.1 节**中关于**如何创建稳定的方案以扩展强化学习计算**的努力，以及在 **3.2 节**中关于**如何将思考整合到智能体任务中**的努力。

---


### 3.1. Scaling GRPO

We first review the objective of GRPO. GRPO optimizes the policy model  $\pi_\theta$ by maximizing the following objective on a group of responses  $\{o_1, \cdots, o_G\}$ sampled from the old policy  $\pi_{\text{old}}$ given each question  $q$:

$$
\begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\ \left.\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*}   \tag*{(5)}
$$

where

$$
r_{i,t}(\theta)=\frac{\pi_{\theta}(o_{i,t}|q,o_{i,<t})}{\pi_{\mathrm{o l d}}(o_{i,t}|q,o_{i,<t})}   \tag*{(6)}
$$

is the importance sampling ratio between the current and old policy.  $\varepsilon$ and  $\beta$ are hyperparameters controlling the clipping range and KL penalty strength, respectively.  $\hat{A}_{i,t}$ is the advantage of  $o_{i,t}$ which is estimated by normalizing the outcome reward within each group. Specifically, a set of reward models are used to score an outcome reward  $R_i$ for each output  $o_i$ in the group, yielding  $G$ rewards  $\boldsymbol{R} = \{R_1, \cdots, R_G\}$ respectively. The advantage of  $o_{i,t}$ is calculated by subtracting the average reward of the group from the reward of output  $o_i$, i.e.,  $\hat{A}_{i,t} = R_i - \text{mean}(\boldsymbol{R})$.

In the following, we outline additional strategies that stabilize RL scaling, directly building on the GRPO algorithm.

Unbiased KL Estimate Given  $o_{i,t}$ is sampled from the old policy  $\pi_{\text{old}}(\cdot|q,o_{i,\text{st}})$, we correct the K3 estimator (Schulman, 2020) to obtain an unbiased KL estimate using the importance-sampling ratio between the current policy  $\pi_{\theta}$ and the old policy  $\pi_{\text{old}}$.

$$
\mathbb{D}_{\mathrm{K L}}\big(\pi_{\theta}(o_{i,t})\big\|\pi_{\mathrm{r e f}}(o_{i,t})\big)=\frac{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\mathrm{o l d}}\big(o_{i,t}|q,o_{i,<t}\big)}\left(\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-\log\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-1\right).   \tag*{(7)}
$$

As a direct result of this adjustment, the gradient of this KL estimator becomes unbiased, which eliminates systematic estimation errors, thereby facilitating stable convergence. This contrasts sharply with the original K3 estimator, particularly when the sampled tokens have substantially lower probabilities under the current policy than the reference policy, i.e.,  $\pi_{\theta} \ll \pi_{ref}$. In such cases, the gradient of the K3 estimator assigns disproportionately large, unbounded weights to maximize the likelihood of these tokens, resulting in noisy gradient updates that accumulate to degrade sample quality in subsequent iterations and lead to unstable training dynamics. In practice, we find that different domains benefit from varying strengths of KL regularization. For certain domains, such as mathematics, applying a relatively weak KL penalty or even omitting it entirely can yield improved performance.

Off-Policy Sequence Masking To improve the efficiency of RL systems, we typically generate a large batch of rollout data, which is subsequently split into multiple mini-batches for several gradient update steps. This practice inherently introduces off-policy behavior. Additionally, inference frameworks used for efficient data generation are often highly optimized, which may differ in implementation details from training frameworks. Such training-inference inconsistency
### 3.1. GRPO 的规模化

我们首先回顾 GRPO 的目标。GRPO 通过最大化以下目标来优化策略模型 $\pi_\theta$，该目标基于从旧策略 $\pi_{\text{old}}$ 中为每个问题 $q$ 采样得到的一组响应 $\{o_1, \cdots, o_G\}$：

$$
\begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\ \left.\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*}   \tag*{(5)}
$$

其中

$$
r_{i,t}(\theta)=\frac{\pi_{\theta}(o_{i,t}|q,o_{i,<t})}{\pi_{\mathrm{o l d}}(o_{i,t}|q,o_{i,<t})}   \tag*{(6)}
$$

是当前策略与旧策略之间的重要性采样比率。$\varepsilon$ 和 $\beta$ 是分别控制裁剪范围和 KL 惩罚强度的超参数。$\hat{A}_{i,t}$ 是 $o_{i,t}$ 的优势，通过在组内对结果奖励进行归一化来估计。具体来说，使用一组奖励模型为组中每个输出 $o_i$ 评分得到一个结果奖励 $R_i$，从而分别得到 $G$ 个奖励 $\boldsymbol{R} = \{R_1, \cdots, R_G\}$。$o_{i,t}$ 的优势通过从输出 $o_i$ 的奖励中减去该组的平均奖励来计算，即 $\hat{A}_{i,t} = R_i - \text{mean}(\boldsymbol{R})$。

接下来，我们将概述在 GRPO 算法基础上直接构建的、用于稳定强化学习规模化的额外策略。

> **无偏 KL 估计** 给定 $o_{i,t}$ 是从旧策略 $\pi_{\text{old}}(\cdot|q,o_{i,\text{st}})$ 中采样的，我们修正了 K3 估计器（Schulman，2020），利用当前策略 $\pi_{\theta}$ 与旧策略 $\pi_{\text{old}}$ 之间的重要性采样比率来获得一个无偏的 KL 估计。

$$
\mathbb{D}_{\mathrm{K L}}\big(\pi_{\theta}(o_{i,t})\big\|\pi_{\mathrm{r e f}}(o_{i,t})\big)=\frac{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\mathrm{o l d}}\big(o_{i,t}|q,o_{i,<t}\big)}\left(\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-\log\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-1\right).   \tag*{(7)}
$$

> 作为这一调整的直接结果，该 KL 估计器的梯度变得无偏，从而消除了系统性估计误差，促进了稳定收敛。这与原始的 K3 估计器形成了鲜明对比，尤其是在采样到的词元在当前策略下的概率远低于参考策略下的概率（即 $\pi_{\theta} \ll \pi_{ref}$）的情况下。在这种情况下，K3 估计器的梯度会分配**不成比例的大且无界的权重**来最大化这些词元的似然，导致梯度更新噪声过大，这些噪声累积起来会降低后续迭代中的样本质量，并导致训练动态不稳定。在实践中，我们发现不同领域受益于不同强度的 KL 正则化。对于某些领域，例如数学，应用相对较弱的 KL 惩罚甚至完全省略它，可能会带来更好的性能。

> **离策略序列掩码** 为了提高强化学习系统的效率，我们通常会生成**大批量的 rollout 数据**，随后将其分割成多个小批次进行若干步梯度更新。这种做法本质上引入了离策略行为。此外，用于高效数据生成的推理框架通常经过高度优化，其实现细节可能与训练框架有所不同。这种训练-推理的不一致性

---


further exacerbates the degree of off-policyness. To stabilize training and improve tolerance for off-policy updates, we mask negative sequences that introduce significant policy divergence, as measured by the KL divergence between the data-sampling policy  $\pi_{old}$ and the current policy  $\pi_{\theta}$. More specifically, we introduce a binary mask M into the GRPO loss:

$$
\begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)&=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\&\left.\quad\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)M_{i,t}-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*}   \tag*{(8)}
$$

where

$$
M_{i,t}=\begin{cases}0&\hat{A}_{i,t}<0,\frac{1}{\left|o_{i}\right|}\sum_{t=1}^{\left|o_{i}\right|}\log\frac{\pi_{\mathrm{old}}\left(o_{i,t}\left|q,o_{i,<t}\right.\right)}{\pi_{\theta}\left(o_{i,t}\left|q,o_{i,<t}\right.\right)}>\delta\\1&otherwise,\end{cases}   \tag*{(9)}
$$

and  $\delta$ is a hyper-parameter that controls the threshold of policy divergence. Note that  $\pi_{old}$ here denotes the sampling probability directly returned by the inference framework, thus the KL divergence between the old and current policy accounts for both sources of off-policyness mentioned above. It is also worth noting that we only mask sequences with negative advantages. Intuitively, the model benefits the most by learning from its own mistakes, whereas highly off-policy negative samples can be detrimental, potentially misleading or destabilizing the optimization process. We empirically observe that this Off-Policy Sequence Masking operation improves stability in certain training scenarios that would otherwise exhibit instability.

Keep Routing Mixture-of-Experts (MoE) models improve computational efficiency by activating only a subset of expert modules during inference. However, discrepancies between inference and training frameworks, compounded by policy updates, can result in inconsistent expert routing during inference and training even for identical inputs. Such inconsistency induces abrupt shifts in the active parameter subspace, which destabilizes optimization and exacerbates off-policy issues. To mitigate this, we preserve the expert routing paths used during sampling in the inference framework and enforce the same routing paths during training, ensuring that identical expert parameters are optimized. This Keep Routing operation was found crucial for RL training stability of MoE models, and has been adopted in our RL training pipeline since DeepSeek-V3-0324.

Keep Sampling Mask Top-p and top-k sampling are widely used sampling strategies to enhance the quality of responses generated by LLMs. Employing these strategies in RL training is also advantageous, as it avoids sampling extremely low-probability tokens that would be used as optimization targets. While such truncation preserves sample quality, it introduces a mismatch between the action spaces of  $\pi_{old}$ and  $\pi_{\theta}$, which violates the principles of importance sampling and destabilizes training. To address this, we preserve the truncation masks during sampling from  $\pi_{old}$ and apply them to  $\pi_{\theta}$ during training, ensuring both policies share identical action subspaces. Empirically, we find that combining top-p sampling with the Keep Sampling Mask strategy effectively preserves language consistency during RL training.
> **进一步加剧了离策略的程度。** 为稳定训练并提升对离策略更新的容忍度，我们屏蔽了那些引入显著策略差异的负样本序列，该差异通过数据采样策略 $\pi_{old}$ 与当前策略 $\pi_{\theta}$ 之间的 KL 散度来衡量。具体而言，我们在 GRPO 损失中引入了一个二元掩码 M：

$$
\begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)&=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\&\left.\quad\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)M_{i,t}-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*}   \tag*{(8)}
$$

其中

$$
M_{i,t}=\begin{cases}0&\hat{A}_{i,t}<0,\frac{1}{\left|o_{i}\right|}\sum_{t=1}^{\left|o_{i}\right|}\log\frac{\pi_{\mathrm{old}}\left(o_{i,t}\left|q,o_{i,<t}\right.\right)}{\pi_{\theta}\left(o_{i,t}\left|q,o_{i,<t}\right.\right)}>\delta\\1&otherwise,\end{cases}   \tag*{(9)}
$$

且 $\delta$ 是一个控制策略差异阈值的超参数。需要注意的是，此处的 $\pi_{old}$ 表示推理框架直接返回的采样概率，因此新旧策略间的 KL 散度同时涵盖了上述两种离策略来源。同样值得注意的是，我们仅屏蔽具有负优势值的序列。直观上，模型从自身错误中学习获益最大，而高度离策略的负样本可能有害，可能误导或破坏优化过程的稳定性。我们通过实验观察到，这种**离策略序列掩码**操作在原本会表现出不稳定性的某些训练场景中提高了稳定性。

> **保持专家路由** 混合专家（MoE）模型通过在推理时仅激活部分专家模块来提高计算效率。然而，推理与训练框架之间的差异，加上策略更新，可能导致即使对于相同的输入，推理和训练过程中的专家路由也不一致。这种不一致性会引起激活参数子空间的突变，从而破坏优化稳定性并加剧离策略问题。为缓解此问题，我们保留了推理框架在采样期间使用的专家路由路径，并在训练期间强制使用相同的路由路径，确保优化的是相同的专家参数。这一**保持路由**操作被发现对 MoE 模型的强化学习训练稳定性至关重要，并已自 DeepSeek-V3-0324 起被纳入我们的强化学习训练流程。

> **保持采样掩码** Top-p 和 top-k 采样是广泛使用的采样策略，旨在提升大语言模型生成响应的质量。在强化学习训练中采用这些策略同样有益，因为它避免了将极低概率的 token 作为优化目标。虽然这种截断保持了样本质量，但它引入了 $\pi_{old}$ 与 $\pi_{\theta}$ 之间动作空间的不匹配，这违反了重要性采样的原则并破坏了训练稳定性。为解决此问题，我们在从 $\pi_{old}$ 采样时保留截断掩码，并在训练时将其应用于 $\pi_{\theta}$，确保两个策略共享相同的动作子空间。经验上，我们发现将 top-p 采样与**保持采样掩码**策略结合，能有效保持强化学习训练期间的语言一致性。

---


### 3.2. Thinking in Tool-Use

#### 3.2.1. Thinking Context Management

DeepSeek-R1 has demonstrated that incorporating a thinking process can significantly enhance a model's ability to solve complex problems. Building on this insight, we aim to integrate thinking capabilities into tool-calling scenarios.

We observed that replicating DeepSeek-R1's strategy—discarding reasoning content upon the arrival of the second round of messages—results in significant token inefficiency. This approach forces the model to redundantly re-reason through the entire problem for each subsequent tool call. To mitigate this, we developed a context management strictly tailored for tool-calling scenarios as shown in Fig 4:

- Historical reasoning content is discarded only when a new user message is introduced to the conversation. If only tool-related messages (e.g., tool outputs) are appended, the reasoning content is retained throughout the interaction.

- When reasoning traces are removed, the history of tool calls and their results remains preserved in the context.

Notably, certain agent frameworks, such as Roo Code or Terminus, simulate tool interactions via user messages. These frameworks may not fully benefit from our enhanced reasoning persistence due to the context management rules outlined above. Therefore, we recommend utilizing non-thinking models for optimal performance with such architectures.

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_819_1012_1253.jpg" alt="Image" width="70%" /></div>

<div style="text-align: center;">Figure 4 | Thinking retention mechanism in tool-calling scenarios.</div>

#### 3.2.2. Cold-Start

Given the availability of reasoning data (non-agentic) and non-reasoning agentic data, a straightforward strategy for integrating these two capabilities is through carefully designed prompting. We posit that the model possesses sufficient ability to accurately follow explicit instructions, thereby enabling the seamless incorporation of tool execution within the reasoning process.
### 3.2. 工具使用中的思考

#### 3.2.1. 思考上下文管理

DeepSeek-R1 已经证明，融入思考过程能显著提升模型解决复杂问题的能力。基于这一洞见，我们旨在将思考能力整合到工具调用场景中。

> 我们观察到，复制 DeepSeek-R1 的策略——在第二轮消息到来时丢弃推理内容——会导致显著的令牌使用效率低下。这种方法迫使模型在每次后续工具调用时，都**需要冗余地重新对整个问题进行推理**。为了缓解这个问题，我们开发了一种严格为工具调用场景定制的上下文管理机制，如图 4 所示：

- 仅当对话中引入新的用户消息时，历史推理内容才会被丢弃。如果仅追加与工具相关的消息（例如，工具输出），则推理内容会在整个交互过程中保留。

- 当推理轨迹被移除时，工具调用的历史及其结果仍会保留在上下文中。

> 值得注意的是，某些智能体框架，如 Roo Code 或 Terminus，通过用户消息来模拟工具交互。由于上述上下文管理规则，这些框架可能无法完全从我们增强的推理持久性中获益。因此，我们建议在此类架构中**使用非思考模型以获得最佳性能**。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_819_1012_1253.jpg" alt="Image" width="70%" /></div>

<div style="text-align: center;">图 4 | 工具调用场景中的思考保留机制。</div>

#### 3.2.2. 冷启动

> 鉴于已有推理数据（非智能体式）和非推理智能体数据可用，整合这两种能力的一个直接策略是通过精心设计的提示工程。我们假设模型**具备足够的能力来准确遵循明确的指令**，从而能够在推理过程中无缝地融入工具执行。

---


To demonstrate the operation of the cold-start mechanism, we selectively sample the training data as shown in Appendix Tables 6–8. It is important to note that distinct task prompts are associated with different system prompts. Tables 6–8 present an illustrative example corresponding to a competitive programming prompt. Table 6 presents an example of our reasoning data, which uses a system prompt to explicitly ask the model to do reasoning before the final answer and uses a special tag <think></think> to label the reasoning path. Table 7 shows the prompt of non-reasoning agentic data, where the system prompt contains the guidance of toolcall. Table 8 presents the system prompt we designed to instruct the model to incorporate multiple tool calls within its reasoning process.

In this manner, although the reasoning in tool-use patterns may lack robustness, the model is occasionally able to generate the desired trajectories, thereby providing a basis for subsequent reinforcement learning stages.

#### 3.2.3. Large-Scale Agentic Tasks

A diverse set of RL tasks is crucial for enhancing model robustness. For tasks such as search, code engineering, and code interpretation, we employ real-world tools, including actual web search APIs, coding tools, and Jupyter Notebooks. While these RL environments are real, the prompts employed are either extracted from Internet sources or synthetically generated, rather than obtained from actual user interactions. For other tasks, the environment and prompts are both synthetically constructed. The agent tasks we used are described in Table 1.

<div style="text-align: center;">Table 1 | The description of different agent tasks, including the number of tasks, environment type (real or synthesized), and prompt source (extracted or synthesized).</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>number of tasks</td><td style='text-align: center; word-wrap: break-word;'>environment</td><td style='text-align: center; word-wrap: break-word;'>prompt</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>code agent</td><td style='text-align: center; word-wrap: break-word;'>24667</td><td style='text-align: center; word-wrap: break-word;'>real</td><td style='text-align: center; word-wrap: break-word;'>extracted</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>search agent</td><td style='text-align: center; word-wrap: break-word;'>50275</td><td style='text-align: center; word-wrap: break-word;'>real</td><td style='text-align: center; word-wrap: break-word;'>synthesized</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>general agent</td><td style='text-align: center; word-wrap: break-word;'>4417</td><td style='text-align: center; word-wrap: break-word;'>synthesized</td><td style='text-align: center; word-wrap: break-word;'>synthesized</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>code interpreter</td><td style='text-align: center; word-wrap: break-word;'>5908</td><td style='text-align: center; word-wrap: break-word;'>real</td><td style='text-align: center; word-wrap: break-word;'>extracted</td></tr></table>

Search Agent We employ a multi-agent pipeline based on DeepSeek-V3.2 to generate diverse, high-quality training data. We first sample informative long-tail entities across diverse domains from large-scale web corpora. A question-construction agent then explores each entity using search tools with configurable depth and breadth parameters, consolidating the discovered information into question-answer pairs. Multiple answer-generation agents with heterogeneous configurations (different checkpoints, system prompts, etc.) produce diverse candidate responses for each proposed QA pair. A verification agent with search capabilities validates all answers through multiple passes, retaining only samples where the ground-truth is correct and all candidates are verifiably incorrect. These data spans multiple languages, domains, and difficulty levels. To complement these verifiable samples and better reflect real-world usage, we also augment the dataset with filtered instances from our existing helpful RL datasets, for which the search tool provides measurable benefits. We then develop detailed evaluation rubrics across multiple quality dimensions and employ a generative reward model to score responses based on these rubrics. This hybrid approach enables optimization for both factual reliability and practical helpfulness.
>为演示冷启动机制的工作原理，我们如附录表6–8所示对训练数据进行选择性采样。需注意的是，**不同的任务提示词对应着不同的系统提示词**。表6–8展示了针对竞争性编程提示词的示例说明：表6呈现了推理数据的示例，其系统提示词明确要求模型在给出最终答案前进行推理，并使用特殊标签`<think></think>`标注推理路径；表7展示了非推理智能体数据的提示词，其系统提示词包含工具调用的引导说明；表8则给出了我们设计的系统提示词，用于指导模型在其推理过程中整合多次工具调用。

>通过这种方式，**尽管工具使用模式中的推理可能缺乏稳健性**，但模型仍能偶尔生成符合期望的行为轨迹，从而为后续强化学习阶段提供基础。

#### 3.2.3. 大规模智能体任务

>多样化的强化学习任务对于提升模型鲁棒性至关重要。针对搜索、代码工程及代码解释等任务，我们采用了真实工具环境，包括实际网络搜索API、编程工具和Jupyter Notebook。**虽然这些强化学习环境是真实的**，但所用提示词均来自网络提取或人工合成，而非真实用户交互数据。对于其他任务，其环境与提示词均为合成构建。表1展示了我们所使用的智能体任务详情。

<div style="text-align: center;">表1 | 不同智能体任务的描述，包括任务数量、环境类型（真实/合成）及提示词来源（提取/合成）</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>任务数量</td><td style='text-align: center; word-wrap: break-word;'>环境</td><td style='text-align: center; word-wrap: break-word;'>提示词</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>代码智能体</td><td style='text-align: center; word-wrap: break-word;'>24667</td><td style='text-align: center; word-wrap: break-word;'>真实</td><td style='text-align: center; word-wrap: break-word;'>提取</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>搜索智能体</td><td style='text-align: center; word-wrap: break-word;'>50275</td><td style='text-align: center; word-wrap: break-word;'>真实</td><td style='text-align: center; word-wrap: break-word;'>合成</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>通用智能体</td><td style='text-align: center; word-wrap: break-word;'>4417</td><td style='text-align: center; word-wrap: break-word;'>合成</td><td style='text-align: center; word-wrap: break-word;'>合成</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>代码解释器</td><td style='text-align: center; word-wrap: break-word;'>5908</td><td style='text-align: center; word-wrap: break-word;'>真实</td><td style='text-align: center; word-wrap: break-word;'>提取</td></tr></table>

>搜索智能体：我们采用基于DeepSeek-V3.2的多智能体流程生成多样化高质量训练数据。首先从大规模网络语料库中采样跨领域的长尾实体信息，随后通过问题构建智能体利用可配置深度与广度参数的搜索工具探索每个实体，并将发现的信息整合为问答对。**配置异构的多个答案生成智能体**（不同检查点、系统提示词等）为每个问答对生成多样候选响应，具备搜索能力的验证智能体通过多轮验证筛选答案，仅保留标准答案正确且所有候选答案均被验证为错误的样本。这些数据涵盖多语言、多领域及多难度层级。为补充可验证样本并更好反映实际使用场景，我们还从现有辅助性强化学习数据集中筛选实例进行增强，这些实例经证实可通过搜索工具获得可衡量的效益。最终我们制定了多维度的详细评估标准，并采用生成式奖励模型基于这些标准对响应进行评分。**这种混合方法能同步优化事实可靠性与实际帮助性**。

---


Code Agent We constructed large-scale, executable environments for software issue resolution by mining millions of issue-Pull Request (PR) pairs from GitHub. This dataset was rigorously filtered using heuristic rules and LLM-based judgments to ensure high quality, requiring that each entry contain a reasonable issue description, a correlated gold patch, and a test patch for validation. An automated environment-setup agent, powered by DeepSeek-V3.2, was employed to build executable environments for these pairs. This agent handles package installation, dependency resolution, and test execution. Test results are output in the standard JUnit format, ensuring consistent parsing across programming languages and test frameworks. An environment is deemed successfully built only when applying the gold patch results in a non-zero count of false-to-positive (F2P) test cases (indicating the issue is fixed) and a zero count of pass-to-fail (P2F) test cases (indicating no regressions). Using this pipeline, we successfully built tens of thousands of reproducible issue resolution environments spanning multiple programming languages, including Python, Java, JavaScript, TypeScript, C, C++, Go, and PHP.

Code Interpreter Agent We utilize Jupyter Notebook as a code interpreter to address complex reasoning tasks. To facilitate this, we curate a diverse set of problems spanning mathematics, logic, and data science, each requiring the model to leverage code execution capabilities to arrive at a solution.

General Agent To scale up agent environments and tasks in RL, we employ an automatic environment-synthesis agent that synthesizes 1,827 task-oriented environments. These tasks are hard to solve but easy to verify. The synthesis workflow primarily consists of environment and toolset construction, task synthesis, and solution generation. Specifically, the workflow proceeds as follows.

1. Given a task category (e.g., planning a travel itinerary) and a sandbox equipped with a bash and a search tool, the agent first uses these tools to generate or retrieve relevant data from the Internet and store them in the sandbox database.

2. The agent then synthesizes a set of task-specific tools, each implemented as a function.

3. To create tasks that are both challenging and automatically verifiable, the agent initially proposes a simple task based on the current database, along with its solution and verification functions implemented in Python. The solution function is restricted to invoking tool functions or performing logical computations, and cannot call other functions or directly access the database, ensuring the task can only be solved through the tool interface. Additionally, the results produced by the solution function must be validated by the verification function. If the solution is not validated, the agent will modify the solution or verification functions until the solution's output passes the verification. The agent then iteratively increases the difficulty of the task and updates the corresponding solution and verification functions. During this iterative process, if the current toolset is not sufficient to solve the task, the agent will augment the toolset.

Following this workflow, we obtain thousands of <environment, tools, task, verifier> tuples. We then perform RL on this dataset using DeepSeek-V3.2 and retain only instances with non-zero pass@100, resulting in 1,827 environments and their corresponding tasks (4,417 in total). A synthetic trip-planning example is illustrated below. This example highlights that, while searching the large combinatorial space for a trip plan that satisfies all constraints is challenging, checking whether a given candidate solution satisfies these constraints is relatively straightforward.
> 我们通过从 GitHub 挖掘数百万个 issue-拉取请求（PR）对，构建了用于软件问题解决的大规模可执行环境。该数据集经过启发式规则和基于 LLM 的判断严格筛选，以确保高质量，要求每个条目包含合理的 issue 描述、关联的黄金补丁以及用于验证的测试补丁。我们采用一个由 DeepSeek-V3.2 驱动的**自动化环境设置代理**来为这些配对构建可执行环境。该代理处理软件包安装、依赖项解析和测试执行。测试结果以标准 JUnit 格式输出，确保了跨编程语言和测试框架的一致解析。**只有当应用黄金补丁后，错误转正确（F2P）的测试用例数量非零（表明问题已修复），且正确转错误（P2F）的测试用例数量为零（表明没有回归）时，环境才被视为成功构建**。利用这一流程，我们成功构建了数万个可重现的问题解决环境，涵盖多种编程语言，包括 Python、Java、JavaScript、TypeScript、C、C++、Go 和 PHP。

> 我们利用 Jupyter Notebook 作为代码解释器来处理复杂的推理任务。为此，我们策划了一系列涵盖数学、逻辑和数据科学的多样化问题，每个问题都要求模型利用代码执行能力来得出解决方案。

> 为了在强化学习中扩展代理环境和任务规模，我们采用了一个**自动环境合成代理**，合成了 1,827 个面向任务的环境。这些任务**解决起来困难，但验证起来容易**。合成工作流主要包括环境和工具集构建、任务合成以及解决方案生成。具体流程如下。

1.  给定一个任务类别（例如，规划旅行行程）和一个配备 bash 和搜索工具的沙盒，代理首先使用这些工具从互联网生成或检索相关数据，并将其存储在沙盒数据库中。

2.  然后，代理合成一组特定于任务的工具，每个工具都实现为一个函数。

3.  为了创建既具有挑战性又可自动验证的任务，代理首先基于当前数据库提出一个简单的任务，并附上其解决方案和用 Python 实现的验证函数。解决方案函数被限制为只能调用工具函数或执行逻辑计算，不能调用其他函数或直接访问数据库，从而确保任务只能通过工具接口解决。此外，解决方案函数产生的结果必须通过验证函数的检验。如果解决方案未通过验证，代理将修改解决方案或验证函数，直到解决方案的输出通过验证。随后，代理会迭代地增加任务难度，并更新相应的解决方案和验证函数。在此迭代过程中，如果当前工具集不足以解决任务，代理将扩充工具集。

> 遵循此工作流，我们获得了数千个<环境、工具、任务、验证器>元组。然后，我们使用 DeepSeek-V3.2 在该数据集上进行强化学习，并仅保留 pass@100 非零的实例，最终得到 1,827 个环境及其对应的任务（总计 4,417 个）。下面展示了一个合成的旅行规划示例。此示例突显了，**虽然在庞大的组合空间中搜索满足所有约束的旅行计划具有挑战性，但检查给定候选解决方案是否满足这些约束则相对简单**。

---


#### An Example of Synthesized Task: Trip Planning

I'm planning a three-day trip starting from Hangzhou, and I need help creating an itinerary from October 1st to October 3rd, 2025. A few important requirements: I don't want to repeat any cities, hotels, attractions, or restaurants during the entire trip. Also, please make sure that every hotel, restaurant, and attraction you recommend is actually located in the city where I'll be staying that day. One more thing about the second day - I'm trying to be smart about my budget. If I end up booking a luxury hotel that costs 800 CNY or more per night, then I need to be more careful with other expenses: my total spending on both restaurants (lunch and dinner) should stay under 350 CNY, both restaurants should be rated at least 4.0 stars, and the afternoon attraction ticket needs to be less than 120 CNY. If the hotel on day 2 is in the mid-to-high range (500-800 CNY), then I have a bit more flexibility - I just need to make sure at least one of my restaurant choices is rated 4.0 or higher, and the attraction ticket should be below 180 CNY. For more affordable hotels (200-500 CNY range), I only need to ensure that at least one restaurant has a rating of 3.2 or above. Can you help me put together this itinerary?

##### Submit Result Format

{ "time": "2025-10-01", "city": "cite_name", "hotel": "hotel_name", "afternoon_restaurant": "restaurant_name", "afternoon_attraction": "attraction_name", "evening_restaurant": "restaurant_name" },

{ "time": "2025-10-02", "city": "cite_name", "hotel": "hotel_name", "afternoon_restaurant": "restaurant_name", "afternoon_attraction": "attraction_name", "evening_restaurant": "restaurant_name" },

{ "time": "2025-10-03", "city": "cite_name", "hotel": "hotel_name", "afternoon_restaurant": "restaurant_name", "afternoon_attraction": "attraction_name", "evening_restaurant": "restaurant_name" }

### Tool Set for Trip Planning

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Function Name</td><td style='text-align: center; word-wrap: break-word;'>Description</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_attractions_by_city(city)</td><td style='text-align: center; word-wrap: break-word;'>Get all attractions for given city.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_cities()</td><td style='text-align: center; word-wrap: break-word;'>Get all cities from the database.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_hotels_by_city(city)</td><td style='text-align: center; word-wrap: break-word;'>Get all hotels for given city.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_restaurants_by_city(city)</td><td style='text-align: center; word-wrap: break-word;'>Get all restaurants for given city.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_attraction(attraction)</td><td style='text-align: center; word-wrap: break-word;'>Get city for given attraction name.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_hotel(hotel)</td><td style='text-align: center; word-wrap: break-word;'>Get city for given hotel name.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_restaurant(restaurant)</td><td style='text-align: center; word-wrap: break-word;'>Get city for given restaurant name.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_transport(city)</td><td style='text-align: center; word-wrap: break-word;'>Get all intra-city transport options for given city.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_attraction(info_keywords, attraction)</td><td style='text-align: center; word-wrap: break-word;'>Get specified infos for given attraction.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_city(info_keywords, city)</td><td style='text-align: center; word-wrap: break-word;'>Get specified infos for given city.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_hotel(info_keywords, hotel)</td><td style='text-align: center; word-wrap: break-word;'>Get specified infos for given hotel.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_restaurant(info_keywords, restaurant)</td><td style='text-align: center; word-wrap: break-word;'>Get specified infos for given restaurant.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_inter_city_transport(from_city, to_city)</td><td style='text-align: center; word-wrap: break-word;'>Get all transports between given city pair.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_weather_by_city_date(city, date)</td><td style='text-align: center; word-wrap: break-word;'>Get weather for given city-date pair.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>submit_result(answer_text)</td><td style='text-align: center; word-wrap: break-word;'>Submit the final answer content.</td></tr></table>

## 4. Evaluation

### 4.1. Main Results

We evaluate models on MMLU-Pro (Wang et al., 2024), GPQA Diamond (Rein et al., 2023), Human Last Exam (HLE) Text-only (Phan et al., 2025), LiveCodeBench (2024.08-2025.04), Code
#### 合成任务示例：旅行规划

> 我正在规划一次从杭州出发的三天行程，需要你帮我制定一份2025年10月1日至10月3日的行程计划。有几个重要的要求：在整个旅行期间，我不想重复访问任何城市、酒店、景点或餐厅。同时，请确保你推荐的每家酒店、餐厅和景点都确实位于我当天所停留的城市。关于第二天还有一点——我想**精打细算**地控制预算。如果我最终预订了每晚价格在800元人民币或以上的豪华酒店，那么我在其他开销上就需要**格外谨慎**：两家餐厅（午餐和晚餐）的总花费必须控制在350元人民币以内，且两家餐厅的评分都至少为4.0星，下午游览的景点门票价格需低于120元人民币。如果第二天的酒店属于中高档（500-800元人民币），那么我的预算就**相对灵活**一些——我只需要确保至少有一家餐厅的评分在4.0或以上，并且景点门票低于180元人民币即可。对于更经济的酒店（200-500元人民币范围），我只需要保证至少有一家餐厅的评分在3.2或以上。你能帮我制定这份行程吗？

##### 提交结果格式

{ "time": "2025-10-01", "city": "城市名称", "hotel": "酒店名称", "afternoon_restaurant": "餐厅名称", "afternoon_attraction": "景点名称", "evening_restaurant": "餐厅名称" },

{ "time": "2025-10-02", "city": "城市名称", "hotel": "酒店名称", "afternoon_restaurant": "餐厅名称", "afternoon_attraction": "景点名称", "evening_restaurant": "餐厅名称" },

{ "time": "2025-10-03", "city": "城市名称", "hotel": "酒店名称", "afternoon_restaurant": "餐厅名称", "afternoon_attraction": "景点名称", "evening_restaurant": "餐厅名称" }

### 旅行规划工具集

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>函数名称</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_attractions_by_city(city)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市的所有景点。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_cities()</td><td style='text-align: center; word-wrap: break-word;'>从数据库中获取所有城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_hotels_by_city(city)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市的所有酒店。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_restaurants_by_city(city)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市的所有餐厅。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_attraction(attraction)</td><td style='text-align: center; word-wrap: break-word;'>获取指定景点名称所在的城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_hotel(hotel)</td><td style='text-align: center; word-wrap: break-word;'>获取指定酒店名称所在的城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_restaurant(restaurant)</td><td style='text-align: center; word-wrap: break-word;'>获取指定餐厅名称所在的城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_transport(city)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市的所有市内交通选项。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_attraction(info_keywords, attraction)</td><td style='text-align: center; word-wrap: break-word;'>获取指定景点的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_city(info_keywords, city)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_hotel(info_keywords, hotel)</td><td style='text-align: center; word-wrap: break-word;'>获取指定酒店的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_restaurant(info_keywords, restaurant)</td><td style='text-align: center; word-wrap: break-word;'>获取指定餐厅的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_inter_city_transport(from_city, to_city)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市对之间的所有交通方式。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_weather_by_city_date(city, date)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市和日期的天气信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>submit_result(answer_text)</td><td style='text-align: center; word-wrap: break-word;'>提交最终答案内容。</td></tr></table>

## 4. 评估

### 4.1. 主要结果

我们在 MMLU-Pro (Wang et al., 2024)、GPQA Diamond (Rein et al., 2023)、Human Last Exam (HLE) Text-only (Phan et al., 2025)、LiveCodeBench (2024.08-2025.04)、Code 等基准上对模型进行了评估。

---


forces, Aider-Polyglot, AIME 2025, HMMT Feb 2025, HMMT Nov 2025 (Balunović et al., 2025), IMOAnswerBench (Luong et al., 2025), Terminal Bench 2.0, SWE-Verified (OpenAI, 2024b), SWE Multilingual (Yang et al., 2025), BrowseComp (Wei et al., 2025), BrowseCompZh (Zhou et al., 2025),  $\tau^{2}$-bench (Barres et al., 2025), MCP-Universe (Luo et al., 2025), MCP-Mark (EvalSys, 2025), and Tool-Decathlon (Li et al., 2025). Tool-use benchmarks are evaluated using the standard function call format, wherein models are configured to thinking mode. For MCP-Universe (Luo et al., 2025) and MCP-Mark (EvalSys, 2025), we evaluate all models with our internal environment, because the search and playwright environment might be slightly different from the official setting. We set the temperature to 1.0, and the context window to 128K tokens. For math-related tasks such as AIME, HMMT, IMOAnswerBench, and HLE, we eval with the following template: "{\question}\nPlease reason step by step, and put your final answer within \boxed{}." In the case of HLE, we additionally assessed DeepSeek-V3.2-Thinking using the official template, resulting in a score of 23.9.

<div style="text-align: center;">Table 2 | Comparison between DeepSeek-V3.2 and closed/open models. For open models, we just compare with models supports thinking in tooluse. Numbers in bold represent the best scores within each model class (open-source and closed-source). The  $\tau^{2}$-Bench result is computed by the average of each category. Regarding BrowseComp, the performance with the context management technique is noted with  $*$.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Benchmark (Metric)</td><td style='text-align: center; word-wrap: break-word;'>Claude-4.5-Sonnet</td><td style='text-align: center; word-wrap: break-word;'>GPT-5 High</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0 Pro</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2 Thinking</td><td style='text-align: center; word-wrap: break-word;'>MiniMax M2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2 Thinking</td></tr><tr><td rowspan="3">English</td><td style='text-align: center; word-wrap: break-word;'>MMLU-Pro (EM)</td><td style='text-align: center; word-wrap: break-word;'>88.2</td><td style='text-align: center; word-wrap: break-word;'>87.5</td><td style='text-align: center; word-wrap: break-word;'>90.1</td><td style='text-align: center; word-wrap: break-word;'>84.6</td><td style='text-align: center; word-wrap: break-word;'>82.0</td><td style='text-align: center; word-wrap: break-word;'>85.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>83.4</td><td style='text-align: center; word-wrap: break-word;'>85.7</td><td style='text-align: center; word-wrap: break-word;'>91.9</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>77.7</td><td style='text-align: center; word-wrap: break-word;'>82.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>13.7</td><td style='text-align: center; word-wrap: break-word;'>26.3</td><td style='text-align: center; word-wrap: break-word;'>37.7</td><td style='text-align: center; word-wrap: break-word;'>23.9</td><td style='text-align: center; word-wrap: break-word;'>12.5</td><td style='text-align: center; word-wrap: break-word;'>25.1</td></tr><tr><td rowspan="2">Code</td><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>64.0</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>90.7</td><td style='text-align: center; word-wrap: break-word;'>82.6</td><td style='text-align: center; word-wrap: break-word;'>83.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Codeforces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>1480</td><td style='text-align: center; word-wrap: break-word;'>2537</td><td style='text-align: center; word-wrap: break-word;'>2708</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386</td></tr><tr><td rowspan="4">Math</td><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>87.0</td><td style='text-align: center; word-wrap: break-word;'>94.6</td><td style='text-align: center; word-wrap: break-word;'>95.0</td><td style='text-align: center; word-wrap: break-word;'>94.5</td><td style='text-align: center; word-wrap: break-word;'>78.3</td><td style='text-align: center; word-wrap: break-word;'>93.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>79.2</td><td style='text-align: center; word-wrap: break-word;'>88.3</td><td style='text-align: center; word-wrap: break-word;'>97.5</td><td style='text-align: center; word-wrap: break-word;'>89.4</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>92.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>81.7</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>93.3</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>90.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>76.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td><td style='text-align: center; word-wrap: break-word;'>78.6</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>78.3</td></tr><tr><td rowspan="3">Code Agent</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0 (Acc)</td><td style='text-align: center; word-wrap: break-word;'>42.8</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>54.2</td><td style='text-align: center; word-wrap: break-word;'>35.7</td><td style='text-align: center; word-wrap: break-word;'>30.0</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>74.9</td><td style='text-align: center; word-wrap: break-word;'>76.2</td><td style='text-align: center; word-wrap: break-word;'>71.3</td><td style='text-align: center; word-wrap: break-word;'>69.4</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>68.0</td><td style='text-align: center; word-wrap: break-word;'>55.3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>61.1</td><td style='text-align: center; word-wrap: break-word;'>56.5</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="3">Search Agent</td><td style='text-align: center; word-wrap: break-word;'>BrowseComp (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>24.1</td><td style='text-align: center; word-wrap: break-word;'>54.9</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>$-/60.2^{*}$</td><td style='text-align: center; word-wrap: break-word;'>44.0</td><td style='text-align: center; word-wrap: break-word;'>51.4/67.6*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BrowseCompZh (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>42.4</td><td style='text-align: center; word-wrap: break-word;'>63.0</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>62.3</td><td style='text-align: center; word-wrap: break-word;'>48.5</td><td style='text-align: center; word-wrap: break-word;'>65.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>32.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>45.8</td><td style='text-align: center; word-wrap: break-word;'>44.9</td><td style='text-align: center; word-wrap: break-word;'>31.8</td><td style='text-align: center; word-wrap: break-word;'>40.8</td></tr><tr><td rowspan="4">ToolUse</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-Bench(Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>84.7</td><td style='text-align: center; word-wrap: break-word;'>80.2</td><td style='text-align: center; word-wrap: break-word;'>85.4</td><td style='text-align: center; word-wrap: break-word;'>74.3</td><td style='text-align: center; word-wrap: break-word;'>76.9</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe (Success Rate)</td><td style='text-align: center; word-wrap: break-word;'>46.5</td><td style='text-align: center; word-wrap: break-word;'>47.9</td><td style='text-align: center; word-wrap: break-word;'>50.7</td><td style='text-align: center; word-wrap: break-word;'>35.6</td><td style='text-align: center; word-wrap: break-word;'>29.4</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>33.3</td><td style='text-align: center; word-wrap: break-word;'>50.9</td><td style='text-align: center; word-wrap: break-word;'>43.1</td><td style='text-align: center; word-wrap: break-word;'>20.4</td><td style='text-align: center; word-wrap: break-word;'>24.4</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>29.0</td><td style='text-align: center; word-wrap: break-word;'>36.4</td><td style='text-align: center; word-wrap: break-word;'>17.6</td><td style='text-align: center; word-wrap: break-word;'>16.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

DeepSeek-V3.2 achieves similar performance with GPT-5-high on reasoning tasks, but is slightly worse than Gemini-3.0-Pro. Compared to K2-Thinking, DeepSeek-V3.2 achieves comparable scores with substantially fewer output tokens, as shown in Table 3. These performance gains can be attributed to the increased computational resources allocated to RL training. Over recent months, we have observed consistent performance improvements correlating with extended RL training budget, which already exceeds 10% of the pre-training cost. We hypothesize that reasoning capabilities could be further enhanced with additional computational budget allocation. Notably, the performance of DeepSeek-V3.2 presented herein is constrained by a length constraint reward model; upon removal of the restriction, we observe further improvement in
> 工具使用基准测试采用标准函数调用格式进行评估，其中模型被配置为思考模式。对于 MCP-Universe (Luo et al., 2025) 和 MCP-Mark (EvalSys, 2025)，我们使用内部环境评估所有模型，因为搜索和 playwright 环境可能与官方设置略有不同。我们将温度设置为 1.0，上下文窗口设置为 128K 个 token。对于 AIME、HMMT、IMOAnswerBench 和 HLE 等数学相关任务，我们使用以下模板进行评估："{\question}\n请逐步推理，并将最终答案放在 \boxed{} 中。" 对于 HLE，我们还使用官方模板评估了 DeepSeek-V3.2-Thinking，**最终得分为 23.9**。

<div style="text-align: center;">表 2 | DeepSeek-V3.2 与闭源/开源模型的比较。对于开源模型，我们仅比较支持在工具使用中思考的模型。粗体数字代表每个模型类别（开源和闭源）中的最佳分数。$\tau^{2}$-Bench 的结果由每个类别的平均值计算得出。关于 BrowseComp，使用上下文管理技术的性能用 $*$ 标注。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>基准测试（指标）</td><td style='text-align: center; word-wrap: break-word;'>Claude-4.5-Sonnet</td><td style='text-align: center; word-wrap: break-word;'>GPT-5 High</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0 Pro</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2 Thinking</td><td style='text-align: center; word-wrap: break-word;'>MiniMax M2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2 Thinking</td></tr><tr><td rowspan="3">英语</td><td style='text-align: center; word-wrap: break-word;'>MMLU-Pro (EM)</td><td style='text-align: center; word-wrap: break-word;'>88.2</td><td style='text-align: center; word-wrap: break-word;'>87.5</td><td style='text-align: center; word-wrap: break-word;'>90.1</td><td style='text-align: center; word-wrap: break-word;'>84.6</td><td style='text-align: center; word-wrap: break-word;'>82.0</td><td style='text-align: center; word-wrap: break-word;'>85.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>83.4</td><td style='text-align: center; word-wrap: break-word;'>85.7</td><td style='text-align: center; word-wrap: break-word;'>91.9</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>77.7</td><td style='text-align: center; word-wrap: break-word;'>82.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>13.7</td><td style='text-align: center; word-wrap: break-word;'>26.3</td><td style='text-align: center; word-wrap: break-word;'>37.7</td><td style='text-align: center; word-wrap: break-word;'>23.9</td><td style='text-align: center; word-wrap: break-word;'>12.5</td><td style='text-align: center; word-wrap: break-word;'>25.1</td></tr><tr><td rowspan="2">代码</td><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>64.0</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>90.7</td><td style='text-align: center; word-wrap: break-word;'>82.6</td><td style='text-align: center; word-wrap: break-word;'>83.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Codeforces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>1480</td><td style='text-align: center; word-wrap: break-word;'>2537</td><td style='text-align: center; word-wrap: break-word;'>2708</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386</td></tr><tr><td rowspan="4">数学</td><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>87.0</td><td style='text-align: center; word-wrap: break-word;'>94.6</td><td style='text-align: center; word-wrap: break-word;'>95.0</td><td style='text-align: center; word-wrap: break-word;'>94.5</td><td style='text-align: center; word-wrap: break-word;'>78.3</td><td style='text-align: center; word-wrap: break-word;'>93.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>79.2</td><td style='text-align: center; word-wrap: break-word;'>88.3</td><td style='text-align: center; word-wrap: break-word;'>97.5</td><td style='text-align: center; word-wrap: break-word;'>89.4</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>92.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>81.7</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>93.3</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>90.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>76.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td><td style='text-align: center; word-wrap: break-word;'>78.6</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>78.3</td></tr><tr><td rowspan="3">代码智能体</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0 (Acc)</td><td style='text-align: center; word-wrap: break-word;'>42.8</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>54.2</td><td style='text-align: center; word-wrap: break-word;'>35.7</td><td style='text-align: center; word-wrap: break-word;'>30.0</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>74.9</td><td style='text-align: center; word-wrap: break-word;'>76.2</td><td style='text-align: center; word-wrap: break-word;'>71.3</td><td style='text-align: center; word-wrap: break-word;'>69.4</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>68.0</td><td style='text-align: center; word-wrap: break-word;'>55.3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>61.1</td><td style='text-align: center; word-wrap: break-word;'>56.5</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="3">搜索智能体</td><td style='text-align: center; word-wrap: break-word;'>BrowseComp (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>24.1</td><td style='text-align: center; word-wrap: break-word;'>54.9</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>$-/60.2^{*}$</td><td style='text-align: center; word-wrap: break-word;'>44.0</td><td style='text-align: center; word-wrap: break-word;'>51.4/67.6*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BrowseCompZh (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>42.4</td><td style='text-align: center; word-wrap: break-word;'>63.0</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>62.3</td><td style='text-align: center; word-wrap: break-word;'>48.5</td><td style='text-align: center; word-wrap: break-word;'>65.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>32.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>45.8</td><td style='text-align: center; word-wrap: break-word;'>44.9</td><td style='text-align: center; word-wrap: break-word;'>31.8</td><td style='text-align: center; word-wrap: break-word;'>40.8</td></tr><tr><td rowspan="4">工具使用</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-Bench(Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>84.7</td><td style='text-align: center; word-wrap: break-word;'>80.2</td><td style='text-align: center; word-wrap: break-word;'>85.4</td><td style='text-align: center; word-wrap: break-word;'>74.3</td><td style='text-align: center; word-wrap: break-word;'>76.9</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe (Success Rate)</td><td style='text-align: center; word-wrap: break-word;'>46.5</td><td style='text-align: center; word-wrap: break-word;'>47.9</td><td style='text-align: center; word-wrap: break-word;'>50.7</td><td style='text-align: center; word-wrap: break-word;'>35.6</td><td style='text-align: center; word-wrap: break-word;'>29.4</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>33.3</td><td style='text-align: center; word-wrap: break-word;'>50.9</td><td style='text-align: center; word-wrap: break-word;'>43.1</td><td style='text-align: center; word-wrap: break-word;'>20.4</td><td style='text-align: center; word-wrap: break-word;'>24.4</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>29.0</td><td style='text-align: center; word-wrap: break-word;'>36.4</td><td style='text-align: center; word-wrap: break-word;'>17.6</td><td style='text-align: center; word-wrap: break-word;'>16.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

> DeepSeek-V3.2 在推理任务上取得了与 GPT-5-high 相似的性能，但略逊于 Gemini-3.0-Pro。与 K2-Thinking 相比，DeepSeek-V3.2 在**输出 token 数量显著减少**的情况下取得了可比的分数，如表 3 所示。这些性能提升可归因于为强化学习训练分配了更多的计算资源。近几个月来，我们观察到性能的持续提升与延长的强化学习训练预算相关，该预算已超过预训练成本的 10%。我们假设，通过分配额外的计算预算，推理能力**有望得到进一步增强**。值得注意的是，本文呈现的 DeepSeek-V3.2 性能受到长度约束奖励模型的限制；**一旦移除该限制**，我们观察到其在...

---


model performance, as detailed in Section 4.2.

In code agent evaluations, DeepSeek-V3.2 significantly outperforms open-source LLMs on both SWE-bench Verified and Terminal Bench 2.0, demonstrating its potential within real-world coding workflows. Regarding Terminal Bench 2.0, as previously noted, our context management strategy for the 'thinking mode' is currently incompatible with Terminus; consequently, the reported score of 46.4 was achieved using the Claude Code framework. We also evaluated DeepSeek-V3.2 with Terminus in non-thinking mode, yielding a score of 39.3. For SWE-bench Verified, the primary score was obtained using our internal framework. Robustness tests across other settings—including the Claude Code and RooCode frameworks, as well as non-thinking mode—produced consistent results, ranging from 72 to 74.

For the search agent evaluation, we assess our models using a standard commercial search API. Since DeepSeek-V3.2 supports a maximum context length of only 128K, approximately 20%+ of the test cases exceed this limit. To address this, we employ a context management method to derive the final score. For reference, the score is 51.4 without context management. Further details are provided in Section 4.4.

On tool-use benchmarks, DeepSeek-V3.2 substantially narrows the performance gap between open-source and closed-source LLMs, though it remains below frontier models. For  $\tau^{2}$-bench, we employ the model itself as the user agent, achieving final category scores of 63.8 (Airline), 81.1 (Retail), and 96.2 (Telecom). For the MCP benchmarks, we employ the function calling format and place tool outputs within messages designated with the 'tool' role, rather than the 'user' role. During our testing, we observed that DeepSeek-V3.2 frequently engages in redundant self-verification, generating excessively long trajectories. This tendency often causes the context length to exceed the 128K limit, particularly in tasks such as MCP-Mark GitHub and Playwright evaluation. Consequently, this phenomenon hinders the final performance of DeepSeek-V3.2. However, integrating context management strategies can further enhance performance. We identify this as a direction for future work and a practical consideration for users. Even if DeepSeek-V3.2 suffers from the issue, it still significantly outperforms existing open models. Notably, since the environments and toolsets employed in these benchmarks were not encountered during RL training, the observed improvements demonstrate DeepSeek-V3.2's capacity to generalize its reasoning strategies to out-of-domain agentic scenarios. The evaluation of non-thinking model in the agent scenario is shown in Appendix Table 9.

### 4.2. Results of DeepSeek-V3.2-Speciale

Table 3 demonstrates that DeepSeek-V3.2-Speciale achieves superior performance by leveraging increased reasoning tokens, surpassing the state-of-the-art Gemini-3.0-Pro across multiple benchmarks. Remarkably, as shown in Table 4, this general-purpose model attains gold-medal level performance in the 2025 International Olympiad in Informatics (IOI) and the ICPC World Finals (ICPC WF) without targeted training. Furthermore, by incorporating techniques from Shao et al. (2025), the model excels in complex proof tasks, reaching gold-medal thresholds in the 2025 International Mathematical Olympiad (IMO) and China Mathematical Olympiad (CMO) $^{5}$. Detailed evaluation protocols are provided in Appendix D.

However, the token efficiency of DeepSeek-V3.2-Speciale remains significantly inferior to that of Gemini-3.0-Pro. To mitigate deployment costs and latency, we imposed stricter token constraints during the training of the official DeepSeek-V3.2, aiming to optimize the trade-off
> 模型性能详述见第4.2节。

在代码智能体评估中，DeepSeek-V3.2 在 SWE-bench Verified 和 Terminal Bench 2.0 上均显著优于开源大语言模型，展现了其在真实世界编码工作流中的潜力。关于 Terminal Bench 2.0，如前所述，我们针对“思考模式”的上下文管理策略目前与 Terminus 不兼容；因此，报告的 46.4 分是使用 Claude Code 框架实现的。我们也评估了 DeepSeek-V3.2 在 Terminus 非思考模式下的表现，得分为 39.3。对于 SWE-bench Verified，主要分数是使用我们内部框架获得的。在其他设置（包括 Claude Code 和 RooCode 框架，以及非思考模式）下的鲁棒性测试结果一致，范围在 72 到 74 之间。

对于搜索智能体评估，我们使用标准的商业搜索 API 来评估模型。由于 DeepSeek-V3.2 仅支持最大 128K 的上下文长度，大约有 20% 以上的测试用例超出了此限制。为解决此问题，我们采用了一种上下文管理方法来得出最终分数。作为参考，在不使用上下文管理的情况下，分数为 51.4。更多细节详见第4.4节。

在工具使用基准测试上，DeepSeek-V3.2 **大幅缩小了开源与闭源大语言模型之间的性能差距**，尽管仍落后于前沿模型。对于 $\tau^{2}$-bench，我们使用模型本身作为用户代理，获得的最终类别分数为 63.8（航空）、81.1（零售）和 96.2（电信）。对于 MCP 基准测试，我们采用函数调用格式，并将工具输出放置在标记为“工具”角色的消息中，而非“用户”角色。在测试中，我们观察到 DeepSeek-V3.2 经常进行冗余的自我验证，生成了过长的轨迹。这种倾向常常导致上下文长度超过 128K 的限制，特别是在 MCP-Mark GitHub 和 Playwright 评估等任务中。因此，这种现象阻碍了 DeepSeek-V3.2 的最终性能。然而，整合上下文管理策略可以进一步提升性能。我们将此视为未来工作的方向以及用户的实际考量。即使 DeepSeek-V3.2 存在此问题，其表现仍显著优于现有的开源模型。值得注意的是，由于这些基准测试中使用的环境和工具集在 RL 训练期间并未遇到，观察到的改进证明了 DeepSeek-V3.2 将其推理策略**泛化到领域外智能体场景**的能力。非思考模型在智能体场景下的评估见附录表9。

### 4.2. DeepSeek-V3.2-Speciale 的结果

表3表明，DeepSeek-V3.2-Speciale 通过利用更多的推理标记实现了卓越性能，在多个基准测试上超越了当前最先进的 Gemini-3.0-Pro。值得注意的是，如表4所示，这个通用模型在没有针对性训练的情况下，在 2025 年国际信息学奥林匹克竞赛（IOI）和国际大学生程序设计竞赛世界总决赛（ICPC WF）中达到了金牌级别的表现。此外，通过结合 Shao 等人（2025）的技术，该模型在复杂证明任务上表现出色，达到了 2025 年国际数学奥林匹克竞赛（IMO）和中国数学奥林匹克竞赛（CMO）的金牌阈值$^{5}$。详细的评估方案见附录D。

然而，DeepSeek-V3.2-Speciale 的标记效率仍显著低于 Gemini-3.0-Pro。为了降低部署成本和延迟，我们在训练官方 DeepSeek-V3.2 时施加了更严格的标记约束，旨在优化权衡。

---


<div style="text-align: center;">Table 3 | Benchmark performance and efficiency of reasoning models. For each benchmark, cells show accuracy and output token count (in thousands). The highest accuracy per benchmark is in bold; the second-highest is underlined.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Benchmark</td><td style='text-align: center; word-wrap: break-word;'>GPT-5</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Pro</td><td style='text-align: center; word-wrap: break-word;'>Thinking</td><td style='text-align: center; word-wrap: break-word;'>Thinking</td><td style='text-align: center; word-wrap: break-word;'>Speciale</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>94.6 (13k)</td><td style='text-align: center; word-wrap: break-word;'>95.0 (15k)</td><td style='text-align: center; word-wrap: break-word;'>94.5 (24k)</td><td style='text-align: center; word-wrap: break-word;'>93.1 (16k)</td><td style='text-align: center; word-wrap: break-word;'>96.0 (23k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>88.3 (16k)</td><td style='text-align: center; word-wrap: break-word;'>97.5 (16k)</td><td style='text-align: center; word-wrap: break-word;'>89.4 (31k)</td><td style='text-align: center; word-wrap: break-word;'>92.5 (19k)</td><td style='text-align: center; word-wrap: break-word;'>99.2 (27k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>89.2 (20k)</td><td style='text-align: center; word-wrap: break-word;'>93.3 (15k)</td><td style='text-align: center; word-wrap: break-word;'>89.2 (29k)</td><td style='text-align: center; word-wrap: break-word;'>90.2 (18k)</td><td style='text-align: center; word-wrap: break-word;'>94.4 (25k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>76.0 (31k)</td><td style='text-align: center; word-wrap: break-word;'>83.3 (18k)</td><td style='text-align: center; word-wrap: break-word;'>78.6 (37k)</td><td style='text-align: center; word-wrap: break-word;'>78.3 (27k)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (45k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (13k)</td><td style='text-align: center; word-wrap: break-word;'>90.7 (13k)</td><td style='text-align: center; word-wrap: break-word;'>82.6 (29k)</td><td style='text-align: center; word-wrap: break-word;'>83.3 (16k)</td><td style='text-align: center; word-wrap: break-word;'>88.7 (27k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CodeForces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>2537 (29k)</td><td style='text-align: center; word-wrap: break-word;'>2708 (22k)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386 (42k)</td><td style='text-align: center; word-wrap: break-word;'>2701 (77k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>85.7 (8k)</td><td style='text-align: center; word-wrap: break-word;'>91.9 (8k)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (12k)</td><td style='text-align: center; word-wrap: break-word;'>82.4 (7k)</td><td style='text-align: center; word-wrap: break-word;'>85.7 (16k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>26.3 (15k)</td><td style='text-align: center; word-wrap: break-word;'>37.7 (15k)</td><td style='text-align: center; word-wrap: break-word;'>23.9 (24k)</td><td style='text-align: center; word-wrap: break-word;'>25.1 (21k)</td><td style='text-align: center; word-wrap: break-word;'>30.6 (35k)</td></tr></table>

<div style="text-align: center;">between performance and cost. We believe that token efficiency remains a critical area for future investigation.</div>

<div style="text-align: center;">Table 4 | Performance of DeepSeek-V3.2-Speciale in top-tier mathematics and coding competitions. For ICPC WF 2025, we report the number of submissions for each successfully solved problem. DeepSeek-V3.2-Speciale ranked 2nd in ICPC WF 2025 and 10th in IOI 2025.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Competition</td><td style='text-align: center; word-wrap: break-word;'>P1</td><td style='text-align: center; word-wrap: break-word;'>P2</td><td style='text-align: center; word-wrap: break-word;'>P3</td><td style='text-align: center; word-wrap: break-word;'>P4</td><td style='text-align: center; word-wrap: break-word;'>P5</td><td style='text-align: center; word-wrap: break-word;'>P6</td><td style='text-align: center; word-wrap: break-word;'>Overall</td><td style='text-align: center; word-wrap: break-word;'>Medal</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMO 2025</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>35/42</td><td style='text-align: center; word-wrap: break-word;'>Gold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CMO 2025</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>102/126</td><td style='text-align: center; word-wrap: break-word;'>Gold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IOI 2025</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>82</td><td style='text-align: center; word-wrap: break-word;'>72</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>83</td><td style='text-align: center; word-wrap: break-word;'>492/600</td><td style='text-align: center; word-wrap: break-word;'>Gold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Competition</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>H</td><td style='text-align: center; word-wrap: break-word;'>J</td><td style='text-align: center; word-wrap: break-word;'>L</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ICPC WF 2025</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>10/12</td></tr></table>

### 4.3. Synthesis Agentic Tasks

In this section, we perform ablation experiments to study the effect of synthetic agentic tasks. We focus on two questions. First, are synthetic tasks sufficiently challenging for reinforcement learning? Second, how well do these synthetic tasks generalize, i.e., can they transfer to different downstream tasks or real-world environments?

To address the first question, we randomly sample 50 instances from the general synthesized agentic tasks and evaluate both the model used for synthesis and frontier closed-source LLMs. As shown in Table 5, DeepSeek-V3.2-Exp attains an accuracy of only 12%, while frontier closed-source models achieve at most 62%. These results indicate that the synthetic data include agentic tasks that are challenging for both DeepSeek-V3.2-Exp and frontier closed-source models.

To investigate whether RL on synthetic data can generalize to different tasks or real-world environments, we apply RL to the SFT checkpoint of DeepSeek-V3.2 (denoted DeepSeek-V3.2-SFT). To exclude the effects of long CoT and other RL data, we conduct RL only on synthetic agentic tasks in non-thinking mode. We then compare the model with DeepSeek-V3.2-SFT and DeepSeek-V3.2-Exp, where DeepSeek-V3.2-Exp is trained with RL only in search and code environments. As shown in Figure 5, large-scale RL on synthetic data yields substantial improve-
<div style="text-align: center;">表3 | 推理模型的基准性能与效率。对于每个基准测试，单元格中显示的是准确率与输出标记数量（以千计）。每个基准测试中**最高**的准确率以粗体标出；**次高**的准确率以下划线标出。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">基准测试</td><td style='text-align: center; word-wrap: break-word;'>GPT-5</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Pro</td><td style='text-align: center; word-wrap: break-word;'>Thinking</td><td style='text-align: center; word-wrap: break-word;'>Thinking</td><td style='text-align: center; word-wrap: break-word;'>Speciale</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>94.6 (13k)</td><td style='text-align: center; word-wrap: break-word;'>95.0 (15k)</td><td style='text-align: center; word-wrap: break-word;'>94.5 (24k)</td><td style='text-align: center; word-wrap: break-word;'>93.1 (16k)</td><td style='text-align: center; word-wrap: break-word;'>96.0 (23k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>88.3 (16k)</td><td style='text-align: center; word-wrap: break-word;'>97.5 (16k)</td><td style='text-align: center; word-wrap: break-word;'>89.4 (31k)</td><td style='text-align: center; word-wrap: break-word;'>92.5 (19k)</td><td style='text-align: center; word-wrap: break-word;'>99.2 (27k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>89.2 (20k)</td><td style='text-align: center; word-wrap: break-word;'>93.3 (15k)</td><td style='text-align: center; word-wrap: break-word;'>89.2 (29k)</td><td style='text-align: center; word-wrap: break-word;'>90.2 (18k)</td><td style='text-align: center; word-wrap: break-word;'>94.4 (25k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>76.0 (31k)</td><td style='text-align: center; word-wrap: break-word;'>83.3 (18k)</td><td style='text-align: center; word-wrap: break-word;'>78.6 (37k)</td><td style='text-align: center; word-wrap: break-word;'>78.3 (27k)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (45k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (13k)</td><td style='text-align: center; word-wrap: break-word;'>90.7 (13k)</td><td style='text-align: center; word-wrap: break-word;'>82.6 (29k)</td><td style='text-align: center; word-wrap: break-word;'>83.3 (16k)</td><td style='text-align: center; word-wrap: break-word;'>88.7 (27k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CodeForces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>2537 (29k)</td><td style='text-align: center; word-wrap: break-word;'>2708 (22k)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386 (42k)</td><td style='text-align: center; word-wrap: break-word;'>2701 (77k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>85.7 (8k)</td><td style='text-align: center; word-wrap: break-word;'>91.9 (8k)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (12k)</td><td style='text-align: center; word-wrap: break-word;'>82.4 (7k)</td><td style='text-align: center; word-wrap: break-word;'>85.7 (16k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>26.3 (15k)</td><td style='text-align: center; word-wrap: break-word;'>37.7 (15k)</td><td style='text-align: center; word-wrap: break-word;'>23.9 (24k)</td><td style='text-align: center; word-wrap: break-word;'>25.1 (21k)</td><td style='text-align: center; word-wrap: break-word;'>30.6 (35k)</td></tr></table>

<div style="text-align: center;">> 性能与成本之间。我们认为，**标记效率**仍然是未来研究的一个关键领域。</div>

<div style="text-align: center;">表4 | DeepSeek-V3.2-Speciale 在顶级数学与编程竞赛中的表现。对于 ICPC WF 2025，我们报告了每个成功解题的提交次数。DeepSeek-V3.2-Speciale 在 ICPC WF 2025 中排名第 2，在 IOI 2025 中排名第 10。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>竞赛</td><td style='text-align: center; word-wrap: break-word;'>P1</td><td style='text-align: center; word-wrap: break-word;'>P2</td><td style='text-align: center; word-wrap: break-word;'>P3</td><td style='text-align: center; word-wrap: break-word;'>P4</td><td style='text-align: center; word-wrap: break-word;'>P5</td><td style='text-align: center; word-wrap: break-word;'>P6</td><td style='text-align: center; word-wrap: break-word;'>总分</td><td style='text-align: center; word-wrap: break-word;'>奖牌</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMO 2025</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>35/42</td><td style='text-align: center; word-wrap: break-word;'>金牌</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CMO 2025</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>102/126</td><td style='text-align: center; word-wrap: break-word;'>金牌</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IOI 2025</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>82</td><td style='text-align: center; word-wrap: break-word;'>72</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>83</td><td style='text-align: center; word-wrap: break-word;'>492/600</td><td style='text-align: center; word-wrap: break-word;'>金牌</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>竞赛</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>H</td><td style='text-align: center; word-wrap: break-word;'>J</td><td style='text-align: center; word-wrap: break-word;'>L</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ICPC WF 2025</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>10/12</td></tr></table>

### 4.3. 合成智能体任务

> 在本节中，我们进行了消融实验，以研究合成智能体任务的效果。我们主要关注两个问题。首先，合成任务对于强化学习来说是否足够具有挑战性？其次，这些合成任务的泛化能力如何，即它们能否迁移到不同的下游任务或现实世界环境中？

> 为了回答第一个问题，我们从通用的合成智能体任务中随机抽取了 50 个实例，并评估了用于合成的模型以及前沿的闭源大语言模型。如表 5 所示，DeepSeek-V3.2-Exp 的准确率仅为 12%，而前沿闭源模型最多也只能达到 62%。这些结果表明，合成数据中包含了对 DeepSeek-V3.2-Exp 和前沿闭源模型都具有挑战性的智能体任务。

> 为了探究在合成数据上进行强化学习是否能泛化到不同的任务或现实世界环境，我们将强化学习应用于 DeepSeek-V3.2 的 SFT 检查点（记为 DeepSeek-V3.2-SFT）。为了排除长思维链和其他强化学习数据的影响，我们仅在非思维模式下对合成智能体任务进行强化学习。然后，我们将该模型与 DeepSeek-V3.2-SFT 和 DeepSeek-V3.2-Exp 进行比较，其中 DeepSeek-V3.2-Exp 仅在搜索和代码环境中进行了强化学习训练。如图 5 所示，在合成数据上进行大规模强化学习带来了**显著**的提

---


<div style="text-align: center;">Table 5 | Accuracy of general synthesized tasks on different models.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Pass@K</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-v3.2-Exp</td><td style='text-align: center; word-wrap: break-word;'>Sonnet-4.5</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0 Pro</td><td style='text-align: center; word-wrap: break-word;'>GPT-5-Thinking</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>12%</td><td style='text-align: center; word-wrap: break-word;'>34%</td><td style='text-align: center; word-wrap: break-word;'>51%</td><td style='text-align: center; word-wrap: break-word;'>62%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>18%</td><td style='text-align: center; word-wrap: break-word;'>47%</td><td style='text-align: center; word-wrap: break-word;'>65%</td><td style='text-align: center; word-wrap: break-word;'>75%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>26%</td><td style='text-align: center; word-wrap: break-word;'>62%</td><td style='text-align: center; word-wrap: break-word;'>74%</td><td style='text-align: center; word-wrap: break-word;'>82%</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_162_396_449_588.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_449_392_739_591.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_745_398_1027_590.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_167_595_450_789.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_451_598_737_791.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_738_599_1027_790.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_162_794_449_987.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_448_797_737_987.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_741_797_1026_986.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">Figure 5 | RL training of DeepSeek-V3.2-SFT using exclusively synthetic general agent data.</div>

ments over DeepSeek-V3.2-SFT on Tau2Bench, MCP-Mark, and MCP-Universe benchmarks. In contrast, restricting RL to code and search scenarios does not improve performance on these benchmarks, further highlighting the potential of synthetic data.

### 4.4. Context Management of Search Agent

Even with extended context windows such as 128k, agentic workflows, particularly in search-based scenarios, frequently encounter maximum length limitations that prematurely truncate the reasoning process. This bottleneck inhibits the full realization of test-time compute potential. To address this, we introduce context management employing simple strategies to extend token budgets at test time, when the token usage exceeds 80% of the context window length. These strategies include (1) Summary, which summarizes the overflowed trajectory and re-initiates the rollout; (2) Discard-75%, which discards the first 75% tool call history in the trajectory to free up spaces; (3) Discard-all, which resets the context by discarding all previous tool call history (similar to the new context tool (Anthropic, 2025a)). For comparison, we also implement a parallel scaling baseline, Parallel-fewest-step, which samples N independent trajectories and
<div style="text-align: center;">表 5 | 不同模型在通用合成任务上的准确率。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Pass@K</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-v3.2-Exp</td><td style='text-align: center; word-wrap: break-word;'>Sonnet-4.5</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0 Pro</td><td style='text-align: center; word-wrap: break-word;'>GPT-5-Thinking</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>12%</td><td style='text-align: center; word-wrap: break-word;'>34%</td><td style='text-align: center; word-wrap: break-word;'>51%</td><td style='text-align: center; word-wrap: break-word;'>62%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>18%</td><td style='text-align: center; word-wrap: break-word;'>47%</td><td style='text-align: center; word-wrap: break-word;'>65%</td><td style='text-align: center; word-wrap: break-word;'>75%</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>26%</td><td style='text-align: center; word-wrap: break-word;'>62%</td><td style='text-align: center; word-wrap: break-word;'>74%</td><td style='text-align: center; word-wrap: break-word;'>82%</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_162_396_449_588.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_449_392_739_591.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_745_398_1027_590.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_167_595_450_789.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_451_598_737_791.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_738_599_1027_790.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_162_794_449_987.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_448_797_737_987.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_741_797_1026_986.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">图 5 | **仅使用**合成通用智能体数据对 DeepSeek-V3.2-SFT 进行 RL 训练。</div>

>在 Tau2Bench、MCP-Mark 和 MCP-Universe 基准测试中，相较于 DeepSeek-V3.2-SFT 模型，**我们观察到了显著的性能提升**。相比之下，将 RL 训练**仅限制在代码和搜索场景中**，并未在这些基准测试上带来性能改进，这进一步突显了合成数据的潜力。

### 4.4. 搜索智能体的上下文管理

>尽管当前模型已具备 128k 等扩展的上下文窗口，但在智能体工作流中，尤其是在基于搜索的场景下，**仍然频繁遭遇**最大长度限制，导致推理过程被过早截断。这一瓶颈**阻碍了**测试时计算潜力的**充分发挥**。为了解决这个问题，我们引入了上下文管理机制，当令牌使用量超过上下文窗口长度的 80% 时，采用简单的策略在测试时扩展令牌预算。这些策略包括：
>
>> (1) **摘要**：对溢出的轨迹进行摘要，然后重新开始执行。
>
>> (2) **丢弃-75%**：丢弃轨迹中前 75% 的工具调用历史以释放空间。
>
>> (3) **丢弃-全部**：通过丢弃所有先前的工具调用历史来重置上下文（类似于新的上下文工具 (Anthropic, 2025a)）。
>
>为了进行比较，我们还实现了一个并行扩展基线 **Parallel-fewest-step**，它并行采样 N 条独立的轨迹并...

---


<div style="text-align: center;"><img src="imgs/img_in_chart_box_170_177_1019_586.jpg" alt="Image" width="71%" /></div>

<div style="text-align: center;">Figure 6 | Accuracy of Browsecomp with different test-time compute expansion strategies.</div>

selects the trajectory with the fewest steps.

We evaluate these strategies on the BrowseComp benchmark (Wei et al., 2025). As illustrated in Figure 6, under varying compute budgets, context management leads to significant performance gains by allowing the model to scale up test-time compute, providing more space to perform additional execution steps. For example, Summary extends the average steps from 140 to 364, improving performance from 53.4 to 60.2. However, its overall efficiency is relatively low. Despite its simplicity, Discard-all performs well in both efficiency and scalability, achieving a score of 67.6, comparable to parallel scaling while using significantly fewer steps.

In summary, test-time compute can be scaled either serially through context management or in parallel, both effectively extending the model's problem-solving capacity. However, different strategies exhibit varying efficiency and scalability. Thus, it is crucial to account for actual compute costs when benchmarking model performance. Meanwhile, finding the optimal combination of serial and parallel scaling to maximize both efficiency and scalability remains a crucial direction for future work.

## 5. Conclusion, Limitation, and Future Work

In this work, we introduced DeepSeek-V3.2, a framework that effectively bridges the gap between computational efficiency and advanced reasoning capabilities. Using DSA, we addressed critical computation complexity without sacrificing long-context performance. By increasing computational budget, DeepSeek-V3.2 achieves comparable performance with GPT-5 on reasoning benchmarks. Finally, the integration of our large-scale agentic task synthesis pipeline significantly enhances tool-use proficiency, unlocking new possibilities for robust and generalizable AI agents with open LLM. Furthermore, our high-compute variant, DeepSeek-V3.2-Speciale, validated by gold-medal achievements in the IMO and IOI, sets a milestone for open LLMs.

Despite these achievements, we acknowledge certain limitations when compared to frontier closed-source models such as Gemini-3.0-Pro. First, due to fewer total training FLOPs, the breadth of world knowledge in DeepSeek-V3.2 still lags behind that of leading proprietary
<div style="text-align: center;"><img src="imgs/img_in_chart_box_170_177_1019_586.jpg" alt="Image" width="71%" /></div>

<div style="text-align: center;">图 6 | 采用不同测试时计算扩展策略时 Browsecomp 的准确率。</div>

> 选择步骤最少的轨迹。

> 我们在 BrowseComp 基准测试（Wei 等人，2025）上评估了这些策略。如图 6 所示，在不同的计算预算下，上下文管理通过允许模型扩展测试时计算，为执行更多额外步骤提供了空间，从而带来了显著的性能提升。例如，Summary 策略将平均步骤数从 140 步扩展到 364 步，将性能从 53.4 提升至 60.2。然而，其整体效率相对较低。尽管 Discard-all 策略很简单，但它在效率和可扩展性方面都表现良好，获得了 67.6 的分数，与并行扩展的性能相当，同时使用的步骤数显著更少。

> **总而言之**，测试时计算可以通过上下文管理进行串行扩展，也可以并行扩展，两者都能有效扩展模型的问题解决能力。然而，不同的策略表现出不同的效率和可扩展性。因此，在对模型性能进行基准测试时，**充分考虑**实际的计算成本至关重要。同时，寻找串行与并行扩展的最佳组合，以最大化效率和可扩展性，仍然是未来工作的**关键方向**。

## 5. 结论、局限性与未来工作

> 在本工作中，我们介绍了 DeepSeek-V3.2，这是一个有效弥合计算效率与高级推理能力之间差距的框架。通过使用 DSA，我们在不牺牲长上下文性能的前提下，解决了关键的计算复杂度问题。通过增加计算预算，DeepSeek-V3.2 在推理基准测试中达到了与 GPT-5 相当的性能。最后，我们大规模智能体任务合成流程的集成，显著提升了工具使用能力，为基于开源 LLM 构建鲁棒且可泛化的 AI 智能体开辟了新的可能性。此外，我们的高计算变体 DeepSeek-V3.2-Speciale，凭借在 IMO 和 IOI 中获得的金牌成就得到验证，为开源 LLMs 树立了一个里程碑。

> 尽管取得了这些成就，我们承认与前沿闭源模型（如 Gemini-3.0-Pro）相比仍存在一些局限性。首先，由于总训练 FLOPs 较少，DeepSeek-V3.2 的世界知识广度仍然落后于领先的专有模型。

---


models. We plan to address this knowledge gap in future iterations by scaling up the pre-training compute. Second, token efficiency remains a challenge; DeepSeek-V3.2 typically requires longer generation trajectories (i.e., more tokens) to match the output quality of models like Gemini-3.0-Pro. Future work will focus on optimizing the intelligence density of the model's reasoning chains to improve efficiency. Third, solving complex tasks is still inferior to frontier models, motivating us to further refine our foundation model and post-training recipe.

## References

Anthropic. System card: Claude opus 4.5, 2025a. URL https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf.

Anthropic. Introducing claude sonnet 4.5, 2025b. URL https://www.anthropic.com/news/claude-sonnet-4-51.

M. Balunović, J. Dekoninck, I. Petrov, N. Jovanović, and M. Vechev. Matharena: Evaluating llms on uncontaminated math competitions. Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmark, 2025.

V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan.  $\tau^{2}$-bench: Evaluating conversational agents in a dual-control environment, 2025. URL https://arxiv.org/abs/2506.07982.

DeepMind. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025a.

G. DeepMind. Gemini 3 pro model card, 2025b. URL https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf.

DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model. CoRR, abs/2405.04434, 2024. doi: 10.48550/ARXIV.2405.04434. URL https://doi.org/10.48550/arXiv.2405.04434.

DeepSeek-AI. Deepseek-v3 technical report, 2024. URL https://arxiv.org/abs/2412.19437.

DeepSeek-AI. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nature, 645(8081):633–638, 2025.

EvalSys. Mcpmark leaderboard, 2025. URL https://mcpmark.ai/leaderboard.

J. Li, W. Zhao, J. Zhao, W. Zeng, H. Wu, X. Wang, R. Ge, Y. Cao, Y. Huang, W. Liu, et al. The tool decathlon: Benchmarking language agents for diverse, realistic, and long-horizon task execution. arXiv preprint arXiv:2510.25726, 2025.

Z. Luo, Z. Shen, W. Yang, Z. Zhao, P. Jwalapuram, A. Saha, D. Sahoo, S. Savarese, C. Xiong, and J. Li. Mcp-universe: Benchmarking large language models with real-world model context protocol servers. arXiv preprint arXiv:2508.14704, 2025.

T. Luong, D. Hwang, H. H. Nguyen, G. Ghiasi, Y. Chervonyi, I. Seo, J. Kim, G. Bingham, J. Lee, S. Mishra, A. Zhai, C. H. Hu, H. Michalewski, J. Kim, J. Ahn, J. Bae, X. Song, T. H. Trinh, Q. V. Le, and J. Jung. Towards robust mathematical reasoning. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025. URL https://aclanthology.org/2025.emnlp-main.1794/.
> 模型。我们计划在未来的迭代中通过扩大预训练计算规模来弥补这一知识缺口。其次，**令牌效率仍然是一个挑战**；DeepSeek-V3.2 通常需要更长的生成轨迹（即更多的令牌）才能达到与 Gemini-3.0-Pro 等模型相当的输出质量。未来的工作将侧重于优化模型推理链的**智能密度**以提高效率。第三，在解决复杂任务方面，其表现仍落后于前沿模型，这激励我们进一步精炼基础模型及后训练方案。

## 参考文献

Anthropic. System card: Claude opus 4.5, 2025a. URL https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf.

Anthropic. Introducing claude sonnet 4.5, 2025b. URL https://www.anthropic.com/news/claude-sonnet-4-51.

M. Balunović, J. Dekoninck, I. Petrov, N. Jovanović, and M. Vechev. Matharena: Evaluating llms on uncontaminated math competitions. Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmark, 2025.

V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan.  $\tau^{2}$-bench: Evaluating conversational agents in a dual-control environment, 2025. URL https://arxiv.org/abs/2506.07982.

DeepMind. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025a.

G. DeepMind. Gemini 3 pro model card, 2025b. URL https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf.

DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model. CoRR, abs/2405.04434, 2024. doi: 10.48550/ARXIV.2405.04434. URL https://doi.org/10.48550/arXiv.2405.04434.

DeepSeek-AI. Deepseek-v3 technical report, 2024. URL https://arxiv.org/abs/2412.19437.

DeepSeek-AI. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nature, 645(8081):633–638, 2025.

EvalSys. Mcpmark leaderboard, 2025. URL https://mcpmark.ai/leaderboard.

J. Li, W. Zhao, J. Zhao, W. Zeng, H. Wu, X. Wang, R. Ge, Y. Cao, Y. Huang, W. Liu, et al. The tool decathlon: Benchmarking language agents for diverse, realistic, and long-horizon task execution. arXiv preprint arXiv:2510.25726, 2025.

Z. Luo, Z. Shen, W. Yang, Z. Zhao, P. Jwalapuram, A. Saha, D. Sahoo, S. Savarese, C. Xiong, and J. Li. Mcp-universe: Benchmarking large language models with real-world model context protocol servers. arXiv preprint arXiv:2508.14704, 2025.

T. Luong, D. Hwang, H. H. Nguyen, G. Ghiasi, Y. Chervonyi, I. Seo, J. Kim, G. Bingham, J. Lee, S. Mishra, A. Zhai, C. H. Hu, H. Michalewski, J. Kim, J. Ahn, J. Bae, X. Song, T. H. Trinh, Q. V. Le, and J. Jung. Towards robust mathematical reasoning. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025. URL https://aclanthology.org/2025.emnlp-main.1794/.

---


MiniMax. https://www.minimax.io/news/minimax-m2, 2025. URL https://www.minimax.io/news/minimax-m2.

MoonShot. Introducing kimi k2 thinking, 2025. URL https://moonshotai.github.io/Kimi-K2/thinking.html.

OpenAI. Learning to reason with llms, 2024a. URL https://openai.com/index/learning-to-reason-with-llms/.

OpenAI. Introducing SWE-bench verified we're releasing a human-validated subset of swe-bench that more, 2024b. URL https://openai.com/index/introducing-swe-bench-verified/.

OpenAI. Introducing gpt-5, 2025. URL https://openai.com/index/introducing-gpt-5/.

L. Phan, A. Gatti, Z. Han, N. Li, J. Hu, H. Zhang, C. B. C. Zhang, M. Shaaban, J. Ling, S. Shi, et al. Humanity's last exam.  $\underline{\text{arXiv preprint arXiv:2501.14249, 2025.}}$

D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. arXiv preprint arXiv:2311.12022, 2023.

J. Schulman. Approximating KL divergence, 2020. URL http://joschu.net/blog/kl-approx.html.

Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo. Deepseek-math: Pushing the limits of mathematical reasoning in open language models. CoRR, abs/2402.03300, 2024. doi: 10.48550/ARXIV.2402.03300. URL https://doi.org/10.48550/arXiv.2402.03300.

Z. Shao, Y. Luo, C. Lu, Z. Ren, J. Hu, T. Ye, Z. Gou, S. Ma, and X. Zhang. Deepseekmath-v2: Towards self-verifiable mathematical reasoning, 2025.

N. Shazeer. Fast transformer decoding: One write-head is all you need.  $\underline{\text{CoRR}}$, abs/1911.02150, 2019. URL http://arxiv.org/abs/1911.02150.

A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. pages 5998–6008, 2017. URL https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.

Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, T. Li, M. Ku, K. Wang, A. Zhuang, R. Fan, X. Yue, and W. Chen. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. CoRR, abs/2406.01574, 2024. URL https://doi.org/10.48550/arXiv.2406.01574.

J. Wei, Z. Sun, S. Papay, S. McKinney, J. Han, I. Fulford, H. W. Chung, A. T. Passos, W. Fedus, and A. Glaese. Browsecomp: A simple yet challenging benchmark for browsing agents.  $\underline{\text{arXiv preprint arXiv:2504.12516}}$, 2025.

J. Yang, K. Lieret, C. E. Jimenez, A. Wettig, K. Khandpur, Y. Zhang, B. Hui, O. Press, L. Schmidt, and D. Yang. Swe-smith: Scaling data for software engineering agents, 2025. URL https://arxiv.org/abs/2504.21798.
MiniMax. https://www.minimax.io/news/minimax-m2, 2025. URL https://www.minimax.io/news/minimax-m2.

MoonShot. Introducing kimi k2 thinking, 2025. URL https://moonshotai.github.io/Kimi-K2/thinking.html.

OpenAI. Learning to reason with llms, 2024a. URL https://openai.com/index/learning-to-reason-with-llms/.

OpenAI. Introducing SWE-bench verified we're releasing a human-validated subset of swe-bench that more, 2024b. URL https://openai.com/index/introducing-swe-bench-verified/.

OpenAI. Introducing gpt-5, 2025. URL https://openai.com/index/introducing-gpt-5/.

> L. Phan, A. Gatti, Z. Han, N. Li, J. Hu, H. Zhang, C. B. C. Zhang, M. Shaaban, J. Ling, S. Shi, 等. 人类的终极考验. $\underline{\text{arXiv preprint arXiv:2501.14249, 2025.}}$

> D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, 和 S. R. Bowman. GPQA: 一个研究生级别的、能**难倒谷歌**的问答基准. arXiv preprint arXiv:2311.12022, 2023.

> J. Schulman. 近似KL散度, 2020. URL http://joschu.net/blog/kl-approx.html.

> Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, 和 D. Guo. Deepseek-math: 在开源语言模型中**突破**数学推理的极限. CoRR, abs/2402.03300, 2024. doi: 10.48550/ARXIV.2402.03300. URL https://doi.org/10.48550/arXiv.2402.03300.

> Z. Shao, Y. Luo, C. Lu, Z. Ren, J. Hu, T. Ye, Z. Gou, S. Ma, 和 X. Zhang. Deepseekmath-v2: 迈向可自我验证的数学推理, 2025.

> N. Shazeer. 快速Transformer解码: 一个写头就**足够了**. $\underline{\text{CoRR}}$, abs/1911.02150, 2019. URL http://arxiv.org/abs/1911.02150.

> A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, 和 I. Polosukhin. 注意力机制就是**全部所需**. pages 5998–6008, 2017. URL https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.

> Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, T. Li, M. Ku, K. Wang, A. Zhuang, R. Fan, X. Yue, 和 W. Chen. MMLU-Pro: 一个**更鲁棒、更具挑战性**的多任务语言理解基准. CoRR, abs/2406.01574, 2024. URL https://doi.org/10.48550/arXiv.2406.01574.

> J. Wei, Z. Sun, S. Papay, S. McKinney, J. Han, I. Fulford, H. W. Chung, A. T. Passos, W. Fedus, 和 A. Glaese. Browsecomp: 一个**看似简单却极具挑战性**的浏览智能体基准. $\underline{\text{arXiv preprint arXiv:2504.12516}}$, 2025.

> J. Yang, K. Lieret, C. E. Jimenez, A. Wettig, K. Khandpur, Y. Zhang, B. Hui, O. Press, L. Schmidt, 和 D. Yang. Swe-smith: 为软件工程智能体**扩展数据**, 2025. URL https://arxiv.org/abs/2504.21798.

---


J. Yuan, H. Gao, D. Dai, J. Luo, L. Zhao, Z. Zhang, Z. Xie, Y. Wei, L. Wang, Z. Xiao, Y. Wang, C. Ruan, M. Zhang, W. Liang, and W. Zeng. Native sparse attention: Hardware-aligned and natively trainable sparse attention. In W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, pages 23078–23097. Association for Computational Linguistics, 2025. URL https://aclanthology.org/2025.acl-long.1126/.

ZhiPu-AI. Glm-4.5: Agentic, reasoning, and coding (arc) foundation models. arXiv preprint arXiv:2508.06471, 2025.

P. Zhou, B. Leon, X. Ying, C. Zhang, Y. Shao, Q. Ye, D. Chong, Z. Jin, C. Xie, M. Cao, et al. Browsecomp-zh: Benchmarking web browsing ability of large language models in chinese. arXiv preprint arXiv:2504.19314, 2025.

## Appendices

### A. MHA and MOA Modes of MLA

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_705_586_1015.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">(a) MHA mode of MLA.</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_605_697_1037_1017.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">(b) MQA mode of MLA.</div>

<div style="text-align: center;">Figure 7 | Illustration of the MHA and MQA modes of MLA. For DeepSeek-V3.1-Terminus, the MHA mode is used for training and prefilling, while the MQA mode is used for decoding.</div>

Figure 7 illustrates two aspects of MLA – the MHA and MQA modes – as well as the transformation between them.

### B. Cold Start Template
> J. Yuan, H. Gao, D. Dai, J. Luo, L. Zhao, Z. Zhang, Z. Xie, Y. Wei, L. Wang, Z. Xiao, Y. Wang, C. Ruan, M. Zhang, W. Liang, and W. Zeng. Native sparse attention: Hardware-aligned and natively trainable sparse attention. In W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2025, pages 23078–23097. Association for Computational Linguistics, 2025. URL https://aclanthology.org/2025.acl-long.1126/.

> ZhiPu-AI. Glm-4.5: Agentic, reasoning, and coding (arc) foundation models. arXiv preprint arXiv:2508.06471, 2025.

> P. Zhou, B. Leon, X. Ying, C. Zhang, Y. Shao, Q. Ye, D. Chong, Z. Jin, C. Xie, M. Cao, et al. Browsecomp-zh: Benchmarking web browsing ability of large language models in chinese. arXiv preprint arXiv:2504.19314, 2025.

## 附录

### A. MLA 的 MHA 与 MQA 模式

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_705_586_1015.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">(a) MLA的MHA模式。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_605_697_1037_1017.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">(b) MLA的MQA模式。</div>

<div style="text-align: center;">图 7 | MLA的MHA与MQA模式示意图。对于DeepSeek-V3.1-Terminus，MHA模式用于训练和预填充阶段，而MQA模式则用于解码阶段。</div>

> 图7展示了MLA的两个方面——MHA模式和MQA模式——以及它们之间的转换。

### B. 冷启动模板

---


<div style="text-align: center;">Table 6 | An example of the reasoning data system prompt. The system prompt requires the model to output the reasoning process in the tag <think></think>.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reasoning System Prompt</td><td style='text-align: center; word-wrap: break-word;'>You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. Please first reason before giving the final answer. The reasoning process enclosed within  $\langle think\rangle$  $\langle/think\rangle$. The final answer is output after the  $\langle/think\rangle$ tag.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>Given a linked list, swap every two adjacent nodes and return its head ...</td></tr><tr><td rowspan="2">Reasoning Response</td><td style='text-align: center; word-wrap: break-word;'>$\langle think\rangle$ ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\langle/think\rangle$ [FINAL ANSWER]</td></tr></table>

<div style="text-align: center;">Table 7 | {TOOL-DESCRIPTIONS} and {TOOLCALL-FORMAT} will be replaced with the specific tools and our designed toolcall format.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Agent</td><td style='text-align: center; word-wrap: break-word;'>Use Python interpreter tool to execute Python code. The code will not be shown to the user. This tool should be used for internal reasoning, but not for code that is intended to be visible to the user (e.g. when creating plots, tables, or files). When you send a message containing Python code to python, it will be executed in a stateful Jupyter notebook environment. Python will respond with the output of the execution or time out after 120.0 seconds.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>System</td><td style='text-align: center; word-wrap: break-word;'># Tools</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>You have access to the following tools: {TOOL-DESCRIPTIONS} Important: ALWAYS adhere to this exact format for tool use: {TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>Given a linked list, swap every two adjacent nodes and return its head ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Agent Response</td><td style='text-align: center; word-wrap: break-word;'>[MULTI-TURN TOOLCALL] [FINAL ANSWER]</td></tr></table>

<div style="text-align: center;">Table 8 | The model executes tool calls in thinking process.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reasoning Required Agent System Prompt</td><td style='text-align: center; word-wrap: break-word;'>You are a helpful assistant with access to a Python interpreter. - You may use the Python tool **multiple times** during your reasoning, a.k.a in &lt;think&gt;&lt;/think&gt;, with a maximum of 20 code executions. - Call the Python tool early in your reasoning to aid in solving the task. Continue reasoning and invoking tools as needed until you reach the final answer. Once you have the answer, stop reasoning and present your solution using Markdown and LaTeX. - Do NOT invoke any tools in your presented final solution steps. - To improve efficiency and accuracy, you should prefer code execution over language-based reasoning whenever possible. Keep your reasoning succinct; let the code do the heavy lifting. ## Tools You have access to the following tools: {TOOL-DESCRIPTIONS} Important: ALWAYS adhere to this exact format for tool use: {TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>Given a linked list, swap every two adjacent nodes and return its head ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Agent Response with Thinking</td><td style='text-align: center; word-wrap: break-word;'>&lt;think&gt; [MULTI-TURN Thinking-Then-TOOLCALL] &lt;/think&gt; [FINAL ANSWER]</td></tr></table>
<div style="text-align: center;">表 6 | 推理数据系统提示词示例。该提示词要求模型在标签 <think></think> 中输出推理过程。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>推理系统提示词</td><td style='text-align: center; word-wrap: break-word;'>> 你是一位专家级的 Python 程序员。你将收到一个问题（问题描述），并需要生成一个符合规范且能通过所有测试的正确 Python 程序。请在给出最终答案前**先进行推理**。推理过程需包含在 $\langle think\rangle$  $\langle/think\rangle$ 标签内。最终答案在 $\langle/think\rangle$ 标签后输出。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>给定一个链表，交换每两个相邻的节点并返回其头节点...</td></tr><tr><td rowspan="2">推理响应</td><td style='text-align: center; word-wrap: break-word;'>$\langle think\rangle$ ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\langle/think\rangle$ [最终答案]</td></tr></table>

<div style="text-align: center;">表 7 | {TOOL-DESCRIPTIONS} 和 {TOOLCALL-FORMAT} 将被替换为特定的工具和我们设计的工具调用格式。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>智能体</td><td style='text-align: center; word-wrap: break-word;'>> 使用 Python 解释器工具来执行 Python 代码。代码不会显示给用户。此工具应用于内部推理，**而不是**用于意图对用户可见的代码（例如，创建图表、表格或文件时）。当你向 python 发送包含 Python 代码的消息时，它将在有状态的 Jupyter notebook 环境中执行。Python 将响应执行输出，或在 120.0 秒后超时。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>系统</td><td style='text-align: center; word-wrap: break-word;'># 工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>> 你可以使用以下工具：{TOOL-DESCRIPTIONS} 重要：**必须始终**严格遵守此工具使用格式：{TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>给定一个链表，交换每两个相邻的节点并返回其头节点...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>智能体响应</td><td style='text-align: center; word-wrap: break-word;'>[多轮工具调用] [最终答案]</td></tr></table>

<div style="text-align: center;">表 8 | 模型在思考过程中执行工具调用。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>需要推理的智能体系统提示词</td><td style='text-align: center; word-wrap: break-word;'>> 你是一位乐于助人的助手，并且可以使用 Python 解释器。
> - 你可以在推理过程中（即在 &lt;think&gt;&lt;/think&gt; 内）**多次**使用 Python 工具，最多执行 20 次代码。
> - **尽早**在推理中调用 Python 工具以帮助解决任务。根据需要持续推理和调用工具，直到得出最终答案。一旦获得答案，就停止推理，并使用 Markdown 和 LaTeX 呈现你的解决方案。
> - **切勿**在你呈现的最终解决方案步骤中调用任何工具。
> - 为了提高效率和准确性，**应尽可能优先使用代码执行**，而非基于语言的推理。保持推理简洁；让代码完成繁重的工作。
> ## 工具
> 你可以使用以下工具：{TOOL-DESCRIPTIONS}
> 重要：**必须始终**严格遵守此工具使用格式：{TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>给定一个链表，交换每两个相邻的节点并返回其头节点...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>带思考的智能体响应</td><td style='text-align: center; word-wrap: break-word;'>&lt;think&gt; [多轮 思考-然后-工具调用] &lt;/think&gt; [最终答案]</td></tr></table>

---


### C. Non-thinking DeepSeek-V3.2 Agentic Evaluation

<div style="text-align: center;">Table 9 | Comparison between DeepSeek-V3.2 non-thinking and thinking modes. The terminal bench scores are evaluated with the Claude Code framework in the table. Non-thinking score of Terminal Bench 2.0 with Terminus framework is 39.3.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Benchmark (Metric)</td><td style='text-align: center; word-wrap: break-word;'>non-thinking thinking</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">Code Agent</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0 (Acc)</td><td style='text-align: center; word-wrap: break-word;'>37.1</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>72.1</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>68.9</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="4">ToolUse</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-bench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe (Success Rate)</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>26.5</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>25.6</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

The performance of non-thinking mode is slightly worse than the thinking mode, but still competitive.

### D. Evaluation Method of IOI, ICPC World Final, IMO, and CMO

For all competitions, the model’s maximum generation length is set to 128k. No tools or internet access are used, and testing strictly adheres to the contest’s time and attempt limits.

For the IOI evaluation, we designed our submission strategy in accordance with the official competition rules, which permit up to 50 submissions per problem and score each submission based on the maximum points achieved across all subtasks. Specifically, we first sampled 500 candidate solutions for each problem, then applied a multi-stage filtering pipeline. In the initial stage, we eliminated invalid submissions that failed to pass the provided sample test cases or exceeded the length constraints. Subsequently, we employed the DeepSeek-V32-Exp model to identify and remove samples in which the model explicitly indicated an inability or refusal to solve the problem. From the remaining valid candidates, we selected the 50 samples with the longest thinking traces for final submission.

For the ICPC evaluation, we adapted the same filtering methodology but with a smaller initial sample size. We generated 32 candidate solutions per problem and applied the identical filtering criteria to select submissions.

In the IMO and CMO tasks, we employ a generate-verify-refine loop. The model iteratively improves its solution until it achieves a perfect self-evaluation or hits the maximum revision cap, identical to the process in Shao et al. (2025).
### C. DeepSeek-V3.2 非思考模式的智能体评估

<div style="text-align: center;">表 9 | DeepSeek-V3.2 非思考模式与思考模式的对比。表中的终端基准分数是使用 Claude Code 框架评估的。采用 Terminus 框架的 Terminal Bench 2.0 非思考模式得分为 39.3。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>基准测试（指标）</td><td style='text-align: center; word-wrap: break-word;'>非思考模式 思考模式</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">代码智能体</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0（准确率）</td><td style='text-align: center; word-wrap: break-word;'>37.1</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified（已解决率）</td><td style='text-align: center; word-wrap: break-word;'>72.1</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual（已解决率）</td><td style='text-align: center; word-wrap: break-word;'>68.9</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="4">工具使用</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-bench（Pass@1）</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe（成功率）</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark（Pass@1）</td><td style='text-align: center; word-wrap: break-word;'>26.5</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon（Pass@1）</td><td style='text-align: center; word-wrap: break-word;'>25.6</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

> 非思考模式的性能**略逊于**思考模式，但仍然具有竞争力。

### D. IOI、ICPC 世界总决赛、IMO 和 CMO 的评估方法

> 对于所有竞赛，模型的**最大生成长度**设置为 128k。不使用任何工具或互联网访问，并且测试**严格遵循**竞赛的时间和提交次数限制。

> 对于 IOI 评估，我们根据官方竞赛规则设计了提交策略，该规则允许每个问题最多提交 50 次，并根据所有子任务中达到的最高分数对每次提交进行评分。具体来说，我们首先为每个问题采样 500 个候选解决方案，然后应用一个多阶段过滤流程。在初始阶段，我们**剔除**了未能通过提供的样例测试用例或超出长度限制的无效提交。随后，我们使用 DeepSeek-V32-Exp 模型来识别并移除那些模型明确表示无法或拒绝解决问题的样本。从剩余的有效候选方案中，我们选择思考轨迹最长的 50 个样本进行最终提交。

> 对于 ICPC 评估，我们采用了相同的过滤方法，但初始样本量较小。我们为每个问题生成 32 个候选解决方案，并应用相同的过滤标准来选择提交。

> 在 IMO 和 CMO 任务中，我们采用一个生成-验证-优化的循环。模型会**迭代地改进**其解决方案，直到达到完美的自我评估或触及最大修订次数上限，此过程与 Shao 等人（2025）的研究相同。

---


### E. Author List

Research & Engineering: Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang, Chaofan Lin, Chen Dong, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenhao Xu, Chong Ruan*, Damai Dai, Daya Guo, Dejian Yang, Deli Chen, Erhang Li, Fangqi Zhou*, Fangyun Lin, Fucong Dai, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Hao Li, Haofen Liang, Haoran Wei, Haowei Zhang, Haowen Luo, Haozhe Ji, Honghui Ding, Hongxuan Tang, Huanqi Cao, Huazuo Gao, Hui Qu, Hui Zeng, Jialiang Huang, Jiashi Li, Jiaxin Xu, Jiewen Hu, Jingchang Chen, Jingting Xiang, Jingyang Yuan, Jingyuan Cheng, Jinhua Zhu, Jun Ran*, Junguang Jiang, Junjie Qiu, Junlong Li*, Junxiao Song, Kai Dong, Kaige Gao, Kang Guan, Kexin Huang*, Kexing Zhou, Kezhao Huang, Kuai Yu, Lean Wang, Lecong Zhang, Lei Wang, Liang Zhao, Liangsheng Yin*, Lihua Guo, Lingxiao Luo, Linwang Ma, Litong Wang, Liyue Zhang, M.S. Di, M.Y Xu, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingxu Zhou, Panpan Huang, Peixin Cong, Peiyi Wang, Qiancheng Wang, Qihao Zhu, Qingyang Li, Qinyu Chen, Qiushi Du, Ruiling Xu, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runqiu Yin, Runxin Xu, Ruomeng Shen, Ruoyu Zhang, S.H. Liu, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaofei Cai, Shaoyuan Chen, Shengding Hu, Shengyu Liu, Shiqiang Hu, Shirong Ma, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, Songyang Zhou, Tao Ni, Tao Yun, Tian Pei, Tian Ye, Tianyuan Yue, Wangding Zeng, Wen Liu, Wenfeng Liang, Wenjie Pang, Wenjing Luo, Wenjun Gao, Wentao Zhang, Xi Gao, Xiangwen Wang, Xiao Bi, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaokang Zhang, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xingkai Yu, Xingyou Li, Xinyu Yang, Xinyuan Li*, Xu Chen, Xuecheng Su, Xuehai Pan, Xuheng Lin, Xuwei Fu, Y.Q. Wang, Yang Zhang, Yanhong Xu, Yanru Ma, Yao Li, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Qian, Yi Yu, Yichao Zhang, Yifan Ding, Yifan Shi, Yiliang Xiong, Ying He, Ying Zhou, Yinmin Zhong, Yishi Piao, Yisong Wang, Yixiao Chen, Yixuan Tan, Yixuan Wei, Yiyang Ma, Yiyuan Liu, Yonglun Yang, Yongqiang Guo, Yongtong Wu, Yu Wu, Yuan Cheng, Yuan Ou, Yuanfan Xu, Yuduan Wang, Yue Gong*, Yuhan Wu, Yuheng Zou, Yukun Li, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Z.F. Wu, Z.Z. Ren, Zehua Zhao, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhibin Gou, Zhicheng Ma, Zhigang Yan, Zhihong Shao, Zhixian Huang, Zhiyu Wu, Zhuoshu Li, Zhuping Zhang, Zian Xu, Zihao Wang, Zihui Gu, Zijia Zhu, Zilin Li, Zipeng Zhang, Ziwei Xie, Ziyi Gao, Zizheng Pan, Zongqing Yao

Data Annotation: Bei Feng, Hui Li, J.L. Cai, Jiaqi Ni, Lei Xu, Meng Li, Ning Tian, R.J. Chen, R.L. Jin, S.S. Li, Shuang Zhou, Tianyu Sun, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xinnan Song, Xinyi Zhou, Y.X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Zhen Huang, Zhipeng Xu, Zhongyu Zhang

Business & Compliance: Dongjie Ji, Jian Liang, Jianzhong Guo, Jin Chen, Leyi Xia, Miaojun Wang, Mingming Li, Peng Zhang, Ruyi Chen, Shangmian Sun, Shaoqing Wu, Shengfeng Ye, T.Wang, W.L. Xiao, Wei An, Xianzu Wang, Xiaowen Sun, Xiaoxiang Wang, Ying Tang, Yukun Zha, Zekai Zhang, Zhe Ju, Zhen Zhang, Zihua Qu

Authors are listed alphabetically by their first name. Names marked with * denote individuals who have departed from our team.
### E. 作者列表

研发与工程：> 刘爱欣、> 梅傲雪、> 林邦才、> 薛冰、> 王炳轩、> 徐炳政、> 吴博超、> 张博伟、> 林超凡、> 董晨、> 卢成达、> 赵成刚、> 邓承启、> 徐晨昊、> 阮冲*、> 戴达迈、> 郭大雅、> 杨德建、> 陈德立、> 李尔航、> 周芳奇*、> 林方云、> 戴富聪、> 郝光波、> 陈冠廷、> 李国伟、> H. 张、> 徐汉威、> 李昊、> 梁浩奋、> 魏浩然、> 张浩伟、> 骆浩文、> 季昊喆、> 丁洪辉、> 唐宏轩、> 曹焕奇、> 高华佐、> 曲辉、> 曾辉、> 黄嘉亮、> 李佳时、> 徐佳欣、> 胡杰文、> 陈景昌、> 向景婷、> 袁景阳、> 程景元、> 朱锦华、> 冉骏*、> 蒋俊光、> 邱俊杰、> 李俊龙*、> 宋俊晓、> 董凯、> 高凯歌、> 关康、> 黄可欣*、> 周可星、> 黄可钊、> 余快、> 王乐安、> 张乐聪、> 王磊、> 赵亮、> 尹良胜*、> 郭立华、> 罗凌霄、> 马林旺、> 王立通、> 张立岳、> M.S. 狄、> M.Y 徐、> 张明川、> 张明华、> 唐明辉、> 周铭旭、> 黄盼盼、> 丛培鑫、> 王培祎、> 王千乘、> 朱启浩、> 李庆阳、> 陈钦宇、> 杜秋实、> 徐瑞玲、> 葛瑞琪、> 张瑞松、> 潘瑞哲、> 王润基、> 殷润秋、> 徐润欣、> 沈若梦、> 张若愚、> S.H. 刘、> 卢尚昊、> 周尚炎、> 陈善煌、> 蔡少飞、> 陈少渊、> 胡胜鼎、> 刘圣宇、> 胡世强、> 马士荣、> 王士宇、> 于水萍、> 周顺丰、> 潘淑婷、> 周松阳、> 倪涛、> 云涛、> 裴天、> 叶甜、> 岳天元、> 曾旺鼎、> 刘雯、> 梁文峰、> 庞文杰、> 骆文静、> 高文俊、> 张文涛、> 高希、> 王祥文、> 毕啸、> 刘晓东、> 王晓寒、> 陈晓康、> 张晓康、> 聂晓涛、> 程欣、> 刘欣、> 谢欣、> 刘星超、> 于星凯、> 李星佑、> 杨欣宇、> 李新元*、> 陈旭、> 苏学成、> 潘学成、> 林旭恒、> 付旭伟、> Y.Q. 王、> 张阳、> 徐艳红、> 马艳茹、> 李尧、> 李耀、> 赵尧、> 孙耀峰、> 王耀辉、> 钱毅、> 余毅、> 张艺超、> 丁逸凡、> 石逸凡、> 熊一良、> 何颖、> 周颖、> 钟寅旻、> 朴一石、> 王奕松、> 陈奕晓、> 谭逸轩、> 魏逸轩、> 马一扬、> 刘一源、> 杨永伦、> 郭永强、> 吴永桐、> 吴宇、> 程远、> 区元、> 徐远帆、> 王玉端、> 宫悦*、> 吴宇涵、> 邹宇恒、> 李宇坤、> 熊云帆、> 罗宇翔、> 游宇翔、> 刘宇轩、> 周宇阳、> Z.F. 吴、> Z.Z. 任、> 赵泽华、> 任泽辉、> 沙章力、> 傅哲、> 徐哲安、> 谢振达、> 张正言、> 郝哲文、> 勾志斌、> 马志程、> 颜志刚、> 邵志宏、> 黄志贤、> 吴志宇、> 李卓书、> 张竹平、> 徐子安、> 王子豪、> 顾子辉、> 朱子嘉、> 李子琳、> 张子鹏、> 谢子威、> 高子怡、> 潘子政、> 姚宗庆

数据标注：> 冯蓓、> 李辉、> J.L. 蔡、> 倪佳琪、> 徐磊、> 李萌、> 田宁、> R.J. 陈、> R.L. 金、> S.S. 李、> 周爽、> 孙天宇、> X.Q. 李、> 金香月、> 沈晓瑾、> 陈晓莎、> 宋心南、> 周欣怡、> Y.X. 朱、> 黄艳萍、> 李耀辉、> 郑毅、> 朱雨晨、> 马云贤、> 黄震、> 徐志鹏、> 张仲宇

商务与合规：> 季冬杰、> 梁健、> 郭建忠、> 陈瑾、> 夏乐怡、> 王妙君、> 李明铭、> 张鹏、> 陈如意、> 孙上棉、> 吴少卿、> 叶胜锋、> T.王、> W.L. 肖、> 安伟、> 王贤祖、> 孙晓雯、> 王晓翔、> 唐颖、> 查宇坤、> 张泽凯、> 琚哲、> 张震、> 屈子华

作者按**姓氏首字母顺序**排列。标有 * 的姓名表示**已离开团队**的人员。