
# DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

DeepSeek-AI

research@deepseek.com

## Abstract

We introduce DeepSeek-V3.2, a model that harmonizes high computational efficiency with superior reasoning and agent performance. The key technical breakthroughs of DeepSeek-V3.2 are as follows: (1) DeepSeek Sparse Attention (DSA): We introduce DSA, an efficient attention mechanism that substantially reduces computational complexity while preserving model performance in long-context scenarios. (2) Scalable Reinforcement Learning Framework: By implementing a robust reinforcement learning protocol and scaling post-training compute, DeepSeek-V3.2 performs comparably to GPT-5. Notably, our high-compute variant, DeepSeek-V3.2-Specialist, surpasses GPT-5 and exhibits reasoning proficiency on par with Gemini-3.0-Pro, achieving gold-medal performance in both the 2025 International Mathematical Olympiad (IMO) and the International Olympiad in Informatics (IOI). (3) Large-Scale Agentic Task Synthesis Pipeline: To integrate reasoning into tool-use scenarios, we developed a novel synthesis pipeline that systematically generates training data at scale. This methodology facilitates scalable agentic post-training, yielding substantial improvements in generalization and instruction-following robustness within complex, interactive environments.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_144_926_1045_1421.jpg" alt="Image" width="75%" /></div>

<div style="text-align: center;">Figure 1 | Benchmark of DeepSeek-V3.2 and its counterparts. For HMMT 2025, we report the February competition, consistent with the baselines. For HLE, we report the text-only subset.</div>

# DeepSeek-V3.2：开拓开源大型语言模型的新前沿

DeepSeek-AI

research@deepseek.com

## 摘要

> 我们推出 DeepSeek-V3.2，该模型在卓越的计算效率与强大的推理及智能体性能之间取得了平衡。DeepSeek-V3.2 的核心技术突破如下：（1）DeepSeek 稀疏注意力（DSA）：我们引入了 DSA，这是一种高效的注意力机制，能在长上下文场景中显著降低计算复杂度，同时保持模型性能。（2）可扩展的强化学习框架：通过实施稳健的强化学习协议并扩展训练后计算量，DeepSeek-V3.2 的表现与 GPT-5 相当。值得注意的是，我们的高计算量变体 DeepSeek-V3.2-Specialist 超越了 GPT-5，其推理能力与 Gemini-3.0-Pro 持平，在 2025 年国际数学奥林匹克（IMO）和国际信息学奥林匹克（IOI）中均取得了金牌成绩。（3）大规模智能体任务合成流程：为了将推理能力融入工具使用场景，我们开发了一种新颖的合成流程，能够系统地大规模生成训练数据。该方法促进了可扩展的智能体训练后优化，在复杂交互环境中显著提升了泛化能力和指令遵循的鲁棒性。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_144_926_1045_1421.jpg" alt="Image" width="75%" /></div>

<div style="text-align: center;">图 1 | DeepSeek-V3.2 及其对比模型的基准测试结果。对于 HMMT 2025，我们报告了与基线一致的二月份竞赛成绩。对于 HLE，我们报告了纯文本子集的结果。</div>

---


## 1. Introduction

The release of reasoning models (DeepSeek-AI, 2025; OpenAI, 2024a) marked a pivotal moment in the evolution of Large Language Models (LLMs), catalyzing a substantial leap in overall performance across the verifiable fields. Since this milestone, the capabilities of LLMs have advanced rapidly. However, a distinct divergence has emerged in the past months. While the open-source community (MiniMax, 2025; MoonShot, 2025; ZhiPu-AI, 2025) continues to make strides, the performance trajectory of closed-source proprietary models (Anthropic, 2025b; DeepMind, 2025a; OpenAI, 2025) has accelerated at a significantly steeper rate. Consequently, rather than converging, the performance gap between closed-source and open-source models appears to be widening, with proprietary systems demonstrating increasingly superior capabilities in complex tasks.

Through our analysis, we identify three critical deficiencies that limit the capability of open-source models in complex tasks. First, architecturally, the predominant reliance on vanilla attention (Vaswani et al., 2017) mechanisms severely constrains efficiency for long sequences. This inefficiency poses a substantial obstacle to both scalable deployment and effective post-training. Second, regarding resource allocation, open-source models suffer from insufficient computational investment during the post-training phase, limiting their performance on hard tasks. Finally, in the context of AI agents, open-source models demonstrate a marked lag in generalization and instruction-following capabilities compared to their proprietary counterparts (EvalSys, 2025; Li et al., 2025; Luo et al., 2025), hindering their effectiveness in real deployment.

To address these critical limitations, we first introduce DSA, a highly efficient attention mechanism designed to substantially reduce computational complexity. This architecture effectively addresses the efficiency bottleneck, preserving model performance even in long-context scenarios. Second, we develop a stable and scalable RL protocol that allows for significant computational expansion during the post-training phase. Notably, this framework allocates a post-training computational budget exceeding 10% of the pre-training cost, unlocking advanced capabilities. Thirdly, we propose a novel pipeline to foster generalizable reasoning in tool-use scenarios. First, we implement a cold-start phase utilizing the DeepSeek-V3 (DeepSeek-AI, 2024) methodology to unify reasoning and tool-use within single trajectories. Subsequently, we advance to large-scale agentic task synthesis, where we generate over 1,800 distinct environments and 85,000 complex prompts. This extensive synthesized data drives the RL process, significantly enhancing the model's generalization and instruction-following capability in the agent context.

DeepSeek-V3.2 achieves similar performance with Kimi-k2-thinking and GPT-5 across multiple reasoning benchmarks. Furthermore, DeepSeek-V3.2 significantly advances the agentic capabilities of open models, demonstrating exceptional proficiency on the long-tail agent tasks introduced in EvalSys (2025); Li et al. (2025); Luo et al. (2025). DeepSeek-V3.2 emerges as a highly cost-efficient alternative in agent scenarios, significantly narrowing the performance gap between open and frontier proprietary models while incurring substantially lower costs. Notably, with the aim of pushing the boundaries of open models in the reasoning domain, we relaxed the length constraints to develop DeepSeek-V3.2-Speciale. As a result, DeepSeek-V3.2-Speciale achieves performance parity with the leading closed-source system, Gemini-3.0-Pro (DeepMind, 2025b). It shows gold-medal performance in the IOI 2025, ICPC World Final 2025, IMO 2025, and CMO 2025.
## 1. 引言

推理模型的发布（DeepSeek-AI，2025；OpenAI，2024a）标志着大语言模型演进的关键时刻，推动其在可验证领域的整体性能实现了巨大飞跃。自这一里程碑以来，大语言模型的能力迅速发展。然而，在过去几个月中，出现了一个明显的分化趋势。尽管开源社区（MiniMax，2025；MoonShot，2025；智谱AI，2025）持续取得进展，但闭源专有模型（Anthropic，2025b；DeepMind，2025a；OpenAI，2025）的性能提升轨迹却以显著更快的速度加速。因此，闭源模型与开源模型之间的性能差距非但没有收敛，反而似乎在扩大，专有系统在复杂任务中展现出越来越优越的能力。

通过我们的分析，我们识别出三个制约开源模型在复杂任务中能力的关键不足。首先，在架构上，主要依赖于原始注意力机制严重限制了长序列的处理效率。这种低效性对可扩展部署和有效的后训练都构成了重大障碍。其次，在资源分配方面，开源模型在后训练阶段的计算投入不足，限制了其在困难任务上的表现。最后，在AI智能体领域，与专有模型相比，开源模型在泛化能力和指令遵循能力上表现出明显的滞后（EvalSys，2025；Li等人，2025；Luo等人，2025），这阻碍了其在真实部署中的有效性。

为了应对这些关键限制，我们首先引入了DSA，这是一种高效的注意力机制，旨在显著降低计算复杂度。该架构有效解决了效率瓶颈，即使在长上下文场景下也能保持模型性能。其次，我们开发了一种稳定且可扩展的强化学习协议，允许在后训练阶段进行大规模的计算扩展。值得注意的是，该框架分配的后训练计算预算超过了预训练成本的10%，从而解锁了高级能力。第三，我们提出了一种新颖的流程，以促进工具使用场景中的可泛化推理。首先，我们采用DeepSeek-V3的方法实施冷启动阶段，将推理和工具使用统一在单一轨迹中。随后，我们推进到大规模智能体任务合成，生成了超过1,800个不同的环境和85,000个复杂的提示。这些大量合成数据驱动了强化学习过程，显著增强了模型在智能体上下文中的泛化能力和指令遵循能力。

DeepSeek-V3.2在多个推理基准测试中达到了与Kimi-k2-thinking和GPT-5相近的性能。此外，DeepSeek-V3.2显著提升了开源模型的智能体能力，在EvalSys、Li等人和Luo等人引入的长尾智能体任务上展现出卓越的熟练度。DeepSeek-V3.2成为智能体场景中一个极具成本效益的替代方案，在显著降低成本的同時，大大缩小了开源模型与前沿专有模型之间的性能差距。值得注意的是，为了推动开源模型在推理领域的边界，我们放宽了长度限制，开发了DeepSeek-V3.2-Speciale。因此，DeepSeek-V3.2-Speciale实现了与领先的闭源系统Gemini-3.0-Pro相当的性能。它在IOI 2025、ICPC World Final 2025、IMO 2025和CMO 2025中展现了金牌级别的表现。

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

DeepSeek-V3.2 使用了与 DeepSeek-V3.2-Exp 完全相同的架构。与 DeepSeek-V3.1 系列的最终版本 DeepSeek-V3.1-Terminus 相比，DeepSeek-V3.2 在架构上唯一的修改是通过持续训练引入了 DeepSeek 稀疏注意力。

DSA 的原型。DSA 的原型主要由两部分组成：一个闪电索引器和一个细粒度的令牌选择机制。

闪电索引器计算查询令牌 $\mathbf{h}_t \in \mathbb{R}^d$ 与前一个令牌 $\mathbf{h}_s \in \mathbb{R}^d$ 之间的索引分数 $I_{t,s}$，以确定哪些令牌将被查询令牌选中：

$$
I_{t,s}=\sum_{j=1}^{H^{I}}w_{t,j}^{I}\cdot\mathrm{R e L U}\left(\mathbf{q}_{t,j}^{I}\cdot\mathbf{k}_{s}^{I}\right),   \tag*{(1)}
$$

其中 $H^I$ 表示索引器头的数量；$\mathbf{q}_{t,j}^I \in \mathbb{R}^{d^I}$ 和 $w_{t,j}^I \in \mathbb{R}$ 源自查询令牌 $\mathbf{h}_t$；而 $\mathbf{k}_s^I \in \mathbb{R}^{d^I}$ 源自前一个令牌 $\mathbf{h}_s$。出于吞吐量考虑，我们选择 ReLU 作为激活函数。鉴于闪电索引器头数较少且可以在 FP8 下实现，其计算效率非常显著。

给定每个查询令牌 $\mathbf{h}_{t}$ 的索引分数 $\{I_{t,s}\}$，我们的细粒度令牌选择机制仅检索与 top-k 索引分数对应的键值条目 $\{c_{s}\}$。然后，通过应用查询令牌 $\mathbf{h}_{t}$ 与稀疏选中的键值条目 $\{c_{s}\}$ 之间的注意力机制来计算注意力输出 $\mathbf{u}_{t}$：

$$
\mathbf{u}_{t}=\mathrm{A t t n}\big(\mathbf{h}_{t},\big\{\mathbf{c}_{s}\big|I_{t,s}\in\mathrm{T o p-k}\big(I_{t,:}\big)\big\}\big).   \tag*{(2)}
$$

在 MLA 框架下实例化 DSA。考虑到从 DeepSeek-V3.1-Terminus 进行持续训练的需求，我们基于 MLA 为 DeepSeek-V3.2 实例化了 DSA。在核心层面，为了计算效率，每个键值条目必须在多个查询之间共享。因此，我们基于 MLA 的 MQA 模式实现了 DSA，其中每个潜在向量（MLA 的键值条目）将在查询令牌的所有查询头之间共享。基于 MLA 的 DSA 架构如图 2 所示。我们还提供了 DeepSeek-V3.2 的开源实现，以明确指定细节。

#### 2.1.1. 持续预训练

我们从上下文长度已扩展至 128K 的 DeepSeek-V3.1-Terminus 基础检查点开始，执行持续预训练，随后进行后训练，以创建 DeepSeek-V3.2。

DeepSeek-V3.2 的持续预训练包含两个训练阶段。对于这两个阶段，训练数据的分布完全与用于 DeepSeek-V3.1-Terminus 的 128K 长上下文扩展数据保持一致。

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

<div style="text-align: center;">图 2 | DeepSeek-V3.2 的注意力架构，其中 DSA 在 MLA 下实例化。绿色部分展示了 DSA 如何根据索引器选择 top-k 键值条目。</div>

> 密集预热阶段。我们首先使用一个简短的预热阶段来初始化闪电索引器。在此阶段，我们保持密集注意力，并冻结除闪电索引器外的所有模型参数。为了使索引器输出与主注意力分布对齐，对于第 t 个查询 token，我们首先通过对所有注意力头的注意力分数求和进行聚合。然后，该和沿序列维度进行 L1 归一化，以生成目标分布 $p_{t,:} \in \mathbb{R}^t$。基于 $p_{t,:}$，我们设置 KL 散度损失作为索引器的训练目标：
>
> $$
> \mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,:}\left\|\mathrm{S o f t m a x}\big(I_{t,:}\big)\right).   \tag*{(3)}
> $$
>
> 对于预热，我们使用 $10^{-3}$ 的学习率。我们仅训练索引器 1000 步，每一步包含 16 个长度为 128K token 的序列，总计 2.1B token。

> 稀疏训练阶段。在索引器预热之后，我们引入细粒度的 token 选择机制，并优化所有模型参数，使模型适应 DSA 的稀疏模式。在此阶段，我们继续保持索引器输出与主注意力分布的对齐，但仅考虑选定的 token 集合 $S_t = \{s \mid I_{t,s} \in \text{Top-k}(I_{t,:})\}$：
>
> $$
> \mathcal{L}^{I}=\sum_{t}\mathbb{D}_{\mathrm{K L}}\big(p_{t,S_{t}}\left\|\mathrm{S o f t m a x}\big(I_{t,S_{t}}\big)\right).   \tag*{(4)}
> $$
>
> 值得注意的是，我们将索引器输入从计算图中分离出来进行独立优化。索引器的训练信号仅来自 $\mathcal{L}^I$，而主模型的优化则仅根据语言建模损失。在此稀疏训练阶段，我们使用 $7.3 \times 10^{-6}$ 的学习率，并为每个查询 token 选择 2048 个键值 token。我们同时训练主模型和索引器 15000 步，每一步包含 480 个长度为 128K token 的序列，总计 943.7B token。

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
### 2.2. 性能评估

> 标准基准测试 2025年9月，我们在涵盖多样化能力的一系列基准测试上评估了 DeepSeek-V3.2-Exp，并与 DeepSeek-V3.1-Terminus 进行了比较，结果显示两者性能相近。虽然 DeepSeek-V3.2-Exp 在长序列上的计算效率显著提升，但在短上下文和长上下文任务上，我们均未观察到相比 DeepSeek-V3.1-Terminus 有明显的性能下降。

> 人类偏好评估 鉴于直接的人类偏好评估本身容易受到偏见影响，我们采用 ChatbotArena 作为间接评估框架，以近似衡量用户对新开发的基础模型的偏好。DeepSeek-V3.1-Terminus 和 DeepSeek-V3.2-Exp 采用了完全相同的后训练策略，并且它们在2025年11月10日评估中获得的 Elo 分数非常接近。这些结果表明，尽管引入了稀疏注意力机制，新的基础模型达到了与前一版本相当的性能水平。

> 长上下文评估 在 DeepSeek-V3.2-Exp 发布后，多个独立的长上下文评估使用先前未见过的测试集进行。一个代表性的基准是 AA-LCR$^{3}$，在该测试的推理模式下，DeepSeek-V3.2-Exp 的得分比 DeepSeek-V3.1-Terminus 高出四分。在 Fiction.liveBench 评估$^{4}$ 中，DeepSeek-V3.2-Exp 在多项指标上持续优于 DeepSeek-V3.1-Terminus。这些证据表明，DeepSeek-V3.2-Exp 的基础检查点在长上下文任务上没有出现性能倒退。

### 2.3. 推理成本

> DSA 将主模型的核心注意力复杂度从 $O(L^{2})$ 降低到 $O(Lk)$，其中 $k \ll L$ 是所选令牌的数量。尽管闪电索引器仍然具有 $O(L^{2})$ 的复杂度，但与 DeepSeek-V3.1-Terminus 中的 MLA 相比，其所需的计算量要少得多。结合我们优化的实现，DSA 在长上下文场景中实现了显著的端到端加速。图 3 展示了 DeepSeek-V3.1-Terminus 和 DeepSeek-V3.2 的令牌成本如何随令牌在序列中的位置而变化。这些成本是根据部署在 H800 GPU（租赁价格为每小时 2 美元）上的实际服务进行基准测试估算得出的。请注意，对于短序列预填充，我们专门实现了一种掩码 MHA 模式来模拟 DSA，该模式可以在短上下文条件下实现更高的效率。

## 3. 后训练

> 在持续预训练之后，我们进行后训练以创建最终的 DeepSeek-V3.2。DeepSeek-V3.2 的后训练也以与稀疏持续预训练阶段相同的方式采用稀疏注意力。对于 DeepSeek-V3.2，我们保持了与 DeepSeek-V3.2-Exp 相同的后训练流程，包括专家蒸馏和混合强化学习训练。

> 专家蒸馏 对于每项任务，我们首先开发一个专门针对该特定领域的专用模型，所有专家模型都是从同一个

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

> 基于预训练的 DeepSeek-V3.2 基础检查点。除了写作任务和通用问答外，我们的框架涵盖了六个专业领域：数学、编程、通用逻辑推理、通用智能体任务、智能体编码和智能体搜索，所有这些领域都支持思考模式和非思考模式。每个专家模型都经过大规模强化学习（RL）计算进行训练。此外，我们采用不同的模型来生成长链思维推理（思考模式）和直接响应生成（非思考模式）的训练数据。专家模型准备就绪后，便用于为最终检查点生成特定领域的数据。实验结果表明，在蒸馏数据上训练的模型性能仅略低于领域专家模型，而通过后续的 RL 训练，性能差距得以有效消除。

> **混合 RL 训练** 对于 DeepSeek-V3.2，我们仍采用组相对策略优化（GRPO）（DeepSeek-AI，2025；Shao et al., 2024）作为 RL 训练算法。与 DeepSeek-V3.2-Exp 类似，我们将推理、智能体和对齐训练合并到一个 RL 阶段。这种方法有效地平衡了不同领域的性能，同时避免了多阶段训练范式中常见的灾难性遗忘问题。对于推理和智能体任务，我们采用基于规则的结果奖励、长度惩罚和语言一致性奖励。对于通用任务，我们采用生成式奖励模型，其中每个提示都有自己的评估准则。

> **DeepSeek-V3.2 与 DeepSeek-V3.2-Speciale** DeepSeek-V3.2 整合了从专家模型蒸馏出的推理、智能体和对齐数据，并经过数千步的持续 RL 训练以达到最终检查点。为了探索扩展思考的潜力，我们还开发了一个实验性变体 DeepSeek-V3.2-Speciale。该模型仅在推理数据上进行训练，并在 RL 期间采用了降低的长度惩罚。此外，我们整合了来自 DeepSeekMath-V2（Shao et al., 2025）的数据集和奖励方法，以增强数学证明能力。

> 我们想强调的是，在第 3.1 节中我们致力于如何创建稳定的方案来扩展 RL 计算，并在第 3.2 节中探讨如何将思考整合到智能体任务中。

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
### 3.1. 扩展 GRPO

我们首先回顾 GRPO 的目标。GRPO 通过最大化以下目标来优化策略模型 $\pi_\theta$，该目标基于从旧策略 $\pi_{\text{old}}$ 中为每个问题 $q$ 采样得到的一组响应 $\{o_1, \cdots, o_G\}$：

$$
\begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\ \left.\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*}   \tag*{(5)}
$$

其中

$$
r_{i,t}(\theta)=\frac{\pi_{\theta}(o_{i,t}|q,o_{i,<t})}{\pi_{\mathrm{o l d}}(o_{i,t}|q,o_{i,<t})}   \tag*{(6)}
$$

是当前策略与旧策略之间的重要性采样比率。$\varepsilon$ 和 $\beta$ 分别是控制裁剪范围和 KL 惩罚强度的超参数。$\hat{A}_{i,t}$ 是 $o_{i,t}$ 的优势函数，通过对组内结果奖励进行归一化估计得到。具体来说，使用一组奖励模型为组中每个输出 $o_i$ 评分一个结果奖励 $R_i$，从而分别得到 $G$ 个奖励 $\boldsymbol{R} = \{R_1, \cdots, R_G\}$。$o_{i,t}$ 的优势函数通过从输出 $o_i$ 的奖励中减去该组的平均奖励来计算，即 $\hat{A}_{i,t} = R_i - \text{mean}(\boldsymbol{R})$。

接下来，我们概述一些直接基于 GRPO 算法、旨在稳定强化学习扩展的额外策略。

> **无偏 KL 估计** 给定 $o_{i,t}$ 是从旧策略 $\pi_{\text{old}}(\cdot|q,o_{i,\text{st}})$ 中采样的，我们修正了 K3 估计器（Schulman，2020），利用当前策略 $\pi_{\theta}$ 与旧策略 $\pi_{\text{old}}$ 之间的重要性采样比率，得到一个无偏的 KL 估计。

$$
\mathbb{D}_{\mathrm{K L}}\big(\pi_{\theta}(o_{i,t})\big\|\pi_{\mathrm{r e f}}(o_{i,t})\big)=\frac{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\mathrm{o l d}}\big(o_{i,t}|q,o_{i,<t}\big)}\left(\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-\log\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-1\right).   \tag*{(7)}
$$

> 作为此项调整的直接结果，该 KL 估计器的梯度变得无偏，从而消除了系统性的估计误差，有助于稳定收敛。这与原始的 K3 估计器形成鲜明对比，尤其是在采样词元在当前策略下的概率远低于参考策略（即 $\pi_{\theta} \ll \pi_{ref}$）的情况下。在这种情况下，K3 估计器的梯度会分配过大、无界的权重来最大化这些词元的似然，导致梯度更新噪声过大，这些噪声在后续迭代中累积，会降低样本质量并导致训练动态不稳定。在实践中，我们发现不同领域受益于不同强度的 KL 正则化。对于某些领域，例如数学，应用相对较弱的 KL 惩罚甚至完全省略它，可能会带来更好的性能。

> **离策略序列掩码** 为了提高强化学习系统的效率，我们通常会生成大批量的 rollout 数据，随后将其分割成多个小批次用于若干次梯度更新步骤。这种做法本质上引入了离策略行为。此外，用于高效数据生成的推理框架通常经过高度优化，其实现细节可能与训练框架存在差异。这种训练-推理的不一致性

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
> 进一步加剧了离策略性的程度。为稳定训练并提高对离策略更新的容忍度，我们根据数据采样策略 $\pi_{old}$ 与当前策略 $\pi_{\theta}$ 之间的 KL 散度度量，对引入显著策略偏差的负序列进行掩码处理。具体而言，我们在 GRPO 损失中引入二元掩码 M：

$$
\begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)&=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\&\left.\quad\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)M_{i,t}-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*}   \tag*{(8)}
$$

其中

$$
M_{i,t}=\begin{cases}0&\hat{A}_{i,t}<0,\frac{1}{\left|o_{i}\right|}\sum_{t=1}^{\left|o_{i}\right|}\log\frac{\pi_{\mathrm{old}}\left(o_{i,t}\left|q,o_{i,<t}\right.\right)}{\pi_{\theta}\left(o_{i,t}\left|q,o_{i,<t}\right.\right)}>\delta\\1&otherwise,\end{cases}   \tag*{(9)}
$$

且 $\delta$ 是控制策略偏差阈值的超参数。需注意，此处的 $\pi_{old}$ 表示推理框架直接返回的采样概率，因此新旧策略间的 KL 散度同时涵盖了上述两种离策略性来源。另外值得注意的是，我们仅对具有负优势度的序列进行掩码。直观上，模型通过从自身错误中学习获益最大，而高度离策略的负样本可能有害，可能误导或破坏优化过程的稳定性。我们通过实验观察到，这种离策略序列掩码操作在某些原本会表现出不稳定性的训练场景中提高了稳定性。

> 保持路由的混合专家模型通过在推理时仅激活部分专家模块来提高计算效率。然而，推理与训练框架间的差异，加上策略更新，可能导致即使对于相同输入，在推理和训练期间也会产生不一致的专家路由。这种不一致性会引发活跃参数子空间的突然变化，从而破坏优化稳定性并加剧离策略问题。为缓解此问题，我们保留推理框架中采样时使用的专家路由路径，并在训练期间强制执行相同的路由路径，确保优化的专家参数一致。这种保持路由的操作被发现对 MoE 模型的 RL 训练稳定性至关重要，并已自 DeepSeek-V3-0324 起应用于我们的 RL 训练流程。

> 保持采样掩码 Top-p 和 top-k 采样是广泛使用的采样策略，旨在提升大语言模型生成回复的质量。在 RL 训练中采用这些策略同样有益，因为它避免了将极低概率的 token 作为优化目标进行采样。虽然这种截断保持了样本质量，但它引入了 $\pi_{old}$ 与 $\pi_{\theta}$ 之间动作空间的不匹配，这违背了重要性采样的原则并破坏了训练稳定性。为解决此问题，我们在从 $\pi_{old}$ 采样时保留截断掩码，并在训练期间将其应用于 $\pi_{\theta}$，确保两个策略共享相同的动作子空间。根据经验，我们发现将 top-p 采样与保持采样掩码策略结合，能有效保持 RL 训练期间的语言一致性。

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

> DeepSeek-R1 已经证明，融入思考过程可以显著增强模型解决复杂问题的能力。基于这一洞见，我们的目标是将思考能力整合到工具调用场景中。

> 我们观察到，复制 DeepSeek-R1 的策略——在第二轮消息到达时丢弃推理内容——会导致显著的 Token 效率低下。这种方法迫使模型在每次后续工具调用时，都冗余地重新对整个问题进行推理。为了缓解这个问题，我们开发了一种专为工具调用场景量身定制的上下文管理机制，如图 4 所示：

> - 仅当对话中引入新的用户消息时，才会丢弃历史推理内容。如果仅追加与工具相关的消息（例如，工具输出），则推理内容会在整个交互过程中保留。
> - 当移除推理痕迹时，工具调用的历史及其结果仍保留在上下文中。

> 值得注意的是，某些智能体框架，如 Roo Code 或 Terminus，通过用户消息来模拟工具交互。由于上述上下文管理规则，这些框架可能无法完全受益于我们增强的推理持久性。因此，我们建议在此类架构中使用非思考模型以获得最佳性能。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_819_1012_1253.jpg" alt="Image" width="70%" /></div>

<div style="text-align: center;">图 4 | 工具调用场景中的思考保留机制。</div>

#### 3.2.2. 冷启动

> 鉴于存在推理数据（非智能体性质）和非推理的智能体数据，整合这两种能力的一个直接策略是通过精心设计的提示。我们假设模型具备足够的能力来准确遵循明确的指令，从而能够在推理过程中无缝地融入工具执行。

---


To demonstrate the operation of the cold-start mechanism, we selectively sample the training data as shown in Appendix Tables 6–8. It is important to note that distinct task prompts are associated with different system prompts. Tables 6–8 present an illustrative example corresponding to a competitive programming prompt. Table 6 presents an example of our reasoning data, which uses a system prompt to explicitly ask the model to do reasoning before the final answer and uses a special tag <think></think> to label the reasoning path. Table 7 shows the prompt of non-reasoning agentic data, where the system prompt contains the guidance of toolcall. Table 8 presents the system prompt we designed to instruct the model to incorporate multiple tool calls within its reasoning process.

In this manner, although the reasoning in tool-use patterns may lack robustness, the model is occasionally able to generate the desired trajectories, thereby providing a basis for subsequent reinforcement learning stages.

#### 3.2.3. Large-Scale Agentic Tasks

A diverse set of RL tasks is crucial for enhancing model robustness. For tasks such as search, code engineering, and code interpretation, we employ real-world tools, including actual web search APIs, coding tools, and Jupyter Notebooks. While these RL environments are real, the prompts employed are either extracted from Internet sources or synthetically generated, rather than obtained from actual user interactions. For other tasks, the environment and prompts are both synthetically constructed. The agent tasks we used are described in Table 1.

<div style="text-align: center;">Table 1 | The description of different agent tasks, including the number of tasks, environment type (real or synthesized), and prompt source (extracted or synthesized).</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>number of tasks</td><td style='text-align: center; word-wrap: break-word;'>environment</td><td style='text-align: center; word-wrap: break-word;'>prompt</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>code agent</td><td style='text-align: center; word-wrap: break-word;'>24667</td><td style='text-align: center; word-wrap: break-word;'>real</td><td style='text-align: center; word-wrap: break-word;'>extracted</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>search agent</td><td style='text-align: center; word-wrap: break-word;'>50275</td><td style='text-align: center; word-wrap: break-word;'>real</td><td style='text-align: center; word-wrap: break-word;'>synthesized</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>general agent</td><td style='text-align: center; word-wrap: break-word;'>4417</td><td style='text-align: center; word-wrap: break-word;'>synthesized</td><td style='text-align: center; word-wrap: break-word;'>synthesized</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>code interpreter</td><td style='text-align: center; word-wrap: break-word;'>5908</td><td style='text-align: center; word-wrap: break-word;'>real</td><td style='text-align: center; word-wrap: break-word;'>extracted</td></tr></table>

Search Agent We employ a multi-agent pipeline based on DeepSeek-V3.2 to generate diverse, high-quality training data. We first sample informative long-tail entities across diverse domains from large-scale web corpora. A question-construction agent then explores each entity using search tools with configurable depth and breadth parameters, consolidating the discovered information into question-answer pairs. Multiple answer-generation agents with heterogeneous configurations (different checkpoints, system prompts, etc.) produce diverse candidate responses for each proposed QA pair. A verification agent with search capabilities validates all answers through multiple passes, retaining only samples where the ground-truth is correct and all candidates are verifiably incorrect. These data spans multiple languages, domains, and difficulty levels. To complement these verifiable samples and better reflect real-world usage, we also augment the dataset with filtered instances from our existing helpful RL datasets, for which the search tool provides measurable benefits. We then develop detailed evaluation rubrics across multiple quality dimensions and employ a generative reward model to score responses based on these rubrics. This hybrid approach enables optimization for both factual reliability and practical helpfulness.
> 为演示冷启动机制的操作，我们如附录表6–8所示选择性采样训练数据。需注意，不同的任务提示词对应不同的系统提示词。表6–8展示了一个对应于竞赛编程提示词的示例：表6呈现了推理数据的示例，其使用系统提示词明确要求模型在给出最终答案前进行推理，并用特殊标签 `<think></think>` 标注推理路径；表7展示了非推理智能体数据的提示词，其中系统提示词包含工具调用的引导；表8则展示了我们设计的系统提示词，用于指导模型在其推理过程中整合多次工具调用。

> 通过这种方式，尽管工具使用模式中的推理可能缺乏鲁棒性，但模型偶尔能够生成期望的轨迹，从而为后续强化学习阶段提供基础。

#### 3.2.3. 大规模智能体任务

> 多样化的强化学习任务对于增强模型鲁棒性至关重要。对于搜索、代码工程和代码解释等任务，我们使用真实世界的工具，包括实际的网络搜索 API、编码工具和 Jupyter Notebook。虽然这些强化学习环境是真实的，但所使用的提示词要么从互联网资源中提取，要么是合成生成的，而非来自真实的用户交互。对于其他任务，环境和提示词均为合成构建。我们使用的智能体任务如表1所述。

<div style="text-align: center;">表 1 | 不同智能体任务的描述，包括任务数量、环境类型（真实或合成）以及提示词来源（提取或合成）。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>任务数量</td><td style='text-align: center; word-wrap: break-word;'>环境</td><td style='text-align: center; word-wrap: break-word;'>提示词</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>代码智能体</td><td style='text-align: center; word-wrap: break-word;'>24667</td><td style='text-align: center; word-wrap: break-word;'>真实</td><td style='text-align: center; word-wrap: break-word;'>提取</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>搜索智能体</td><td style='text-align: center; word-wrap: break-word;'>50275</td><td style='text-align: center; word-wrap: break-word;'>真实</td><td style='text-align: center; word-wrap: break-word;'>合成</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>通用智能体</td><td style='text-align: center; word-wrap: break-word;'>4417</td><td style='text-align: center; word-wrap: break-word;'>合成</td><td style='text-align: center; word-wrap: break-word;'>合成</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>代码解释器</td><td style='text-align: center; word-wrap: break-word;'>5908</td><td style='text-align: center; word-wrap: break-word;'>真实</td><td style='text-align: center; word-wrap: break-word;'>提取</td></tr></table>

> **搜索智能体**：我们采用基于 DeepSeek-V3.2 的多智能体流程来生成多样化、高质量的训练数据。首先，从大规模网络语料库中跨不同领域采样信息丰富的长尾实体。接着，一个问答构建智能体使用可配置深度和广度参数的搜索工具探索每个实体，并将发现的信息整合为问答对。多个具有异构配置（不同检查点、系统提示词等）的答案生成智能体为每个提出的问答对生成多样化的候选回答。一个具备搜索能力的验证智能体通过多轮验证对所有答案进行校验，仅保留标准答案正确且所有候选答案均被验证为错误的样本。这些数据涵盖多种语言、领域和难度级别。为补充这些可验证样本并更好地反映真实使用场景，我们还从现有的有益强化学习数据集中添加了经过筛选的实例，这些实例中搜索工具能带来可衡量的益处。随后，我们制定了跨多个质量维度的详细评估标准，并采用生成式奖励模型基于这些标准对回答进行评分。这种混合方法能够同时优化事实可靠性和实际帮助性。

---


Code Agent We constructed large-scale, executable environments for software issue resolution by mining millions of issue-Pull Request (PR) pairs from GitHub. This dataset was rigorously filtered using heuristic rules and LLM-based judgments to ensure high quality, requiring that each entry contain a reasonable issue description, a correlated gold patch, and a test patch for validation. An automated environment-setup agent, powered by DeepSeek-V3.2, was employed to build executable environments for these pairs. This agent handles package installation, dependency resolution, and test execution. Test results are output in the standard JUnit format, ensuring consistent parsing across programming languages and test frameworks. An environment is deemed successfully built only when applying the gold patch results in a non-zero count of false-to-positive (F2P) test cases (indicating the issue is fixed) and a zero count of pass-to-fail (P2F) test cases (indicating no regressions). Using this pipeline, we successfully built tens of thousands of reproducible issue resolution environments spanning multiple programming languages, including Python, Java, JavaScript, TypeScript, C, C++, Go, and PHP.

Code Interpreter Agent We utilize Jupyter Notebook as a code interpreter to address complex reasoning tasks. To facilitate this, we curate a diverse set of problems spanning mathematics, logic, and data science, each requiring the model to leverage code execution capabilities to arrive at a solution.

General Agent To scale up agent environments and tasks in RL, we employ an automatic environment-synthesis agent that synthesizes 1,827 task-oriented environments. These tasks are hard to solve but easy to verify. The synthesis workflow primarily consists of environment and toolset construction, task synthesis, and solution generation. Specifically, the workflow proceeds as follows.

1. Given a task category (e.g., planning a travel itinerary) and a sandbox equipped with a bash and a search tool, the agent first uses these tools to generate or retrieve relevant data from the Internet and store them in the sandbox database.

2. The agent then synthesizes a set of task-specific tools, each implemented as a function.

3. To create tasks that are both challenging and automatically verifiable, the agent initially proposes a simple task based on the current database, along with its solution and verification functions implemented in Python. The solution function is restricted to invoking tool functions or performing logical computations, and cannot call other functions or directly access the database, ensuring the task can only be solved through the tool interface. Additionally, the results produced by the solution function must be validated by the verification function. If the solution is not validated, the agent will modify the solution or verification functions until the solution's output passes the verification. The agent then iteratively increases the difficulty of the task and updates the corresponding solution and verification functions. During this iterative process, if the current toolset is not sufficient to solve the task, the agent will augment the toolset.

Following this workflow, we obtain thousands of <environment, tools, task, verifier> tuples. We then perform RL on this dataset using DeepSeek-V3.2 and retain only instances with non-zero pass@100, resulting in 1,827 environments and their corresponding tasks (4,417 in total). A synthetic trip-planning example is illustrated below. This example highlights that, while searching the large combinatorial space for a trip plan that satisfies all constraints is challenging, checking whether a given candidate solution satisfies these constraints is relatively straightforward.
> 代码智能体 我们通过从 GitHub 挖掘数百万个 issue-拉取请求（PR）对，构建了用于软件问题解决的大规模可执行环境。该数据集经过启发式规则和基于 LLM 的判断严格筛选，以确保高质量，要求每个条目包含合理的 issue 描述、一个关联的黄金补丁以及一个用于验证的测试补丁。我们采用了一个由 DeepSeek-V3.2 驱动的自动化环境设置智能体来为这些配对构建可执行环境。该智能体负责包安装、依赖项解析和测试执行。测试结果以标准的 JUnit 格式输出，确保了跨编程语言和测试框架的一致性解析。仅当应用黄金补丁后，错误转正向（F2P）测试用例数量非零（表明问题已修复）且通过转失败（P2F）测试用例数量为零（表明没有回归）时，环境才被视为成功构建。利用此流程，我们成功构建了数万个可复现的问题解决环境，涵盖多种编程语言，包括 Python、Java、JavaScript、TypeScript、C、C++、Go 和 PHP。

> 代码解释器智能体 我们利用 Jupyter Notebook 作为代码解释器来处理复杂的推理任务。为此，我们策划了一套涵盖数学、逻辑和数据科学的多样化问题集，每个问题都需要模型利用代码执行能力来得出解决方案。

> 通用智能体 为了在强化学习中扩展智能体环境和任务，我们采用了一个自动环境合成智能体，合成了 1,827 个面向任务的环境。这些任务难以解决但易于验证。合成工作流程主要包括环境和工具集构建、任务合成以及解决方案生成。具体流程如下。

> 1.  给定一个任务类别（例如，规划旅行行程）和一个配备 bash 和搜索工具的沙盒，智能体首先使用这些工具从互联网生成或检索相关数据，并将其存储在沙盒数据库中。
> 2.  然后，智能体合成一组特定于任务的工具，每个工具都实现为一个函数。
> 3.  为了创建既具挑战性又可自动验证的任务，智能体首先基于当前数据库提出一个简单任务，并提供其解决方案以及用 Python 实现的验证函数。解决方案函数仅限于调用工具函数或执行逻辑计算，不能调用其他函数或直接访问数据库，确保任务只能通过工具接口解决。此外，解决方案函数产生的结果必须通过验证函数的验证。如果解决方案未通过验证，智能体将修改解决方案或验证函数，直到解决方案的输出通过验证。然后，智能体迭代地增加任务难度，并更新相应的解决方案和验证函数。在此迭代过程中，如果当前工具集不足以解决任务，智能体将扩充工具集。

> 遵循此工作流程，我们获得了数千个<环境, 工具, 任务, 验证器>元组。然后，我们使用 DeepSeek-V3.2 在此数据集上进行强化学习，并仅保留 pass@100 不为零的实例，最终得到 1,827 个环境及其对应的任务（总计 4,417 个）。下面展示了一个合成的旅行规划示例。此示例强调，虽然在大组合空间中搜索满足所有约束的旅行计划具有挑战性，但检查给定候选解决方案是否满足这些约束则相对简单。

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
#### 综合任务示例：旅行规划

> 我正在规划一次从杭州出发的三天行程，需要你帮忙制定一份2025年10月1日至10月3日的行程单。有几个重要要求：整个旅程中，任何城市、酒店、景点或餐厅都不能重复。另外，请确保你推荐的每家酒店、餐厅和景点都确实位于我当天所停留的城市。关于第二天还有一点——我想在预算上精打细算。如果我最终预订了一家每晚800元人民币或以上的豪华酒店，那么我在其他开销上就需要更谨慎：两家餐厅（午餐和晚餐）的总花费必须控制在350元人民币以下，两家餐厅的评分都至少为4.0星，并且下午景点的门票需要低于120元人民币。如果第二天的酒店属于中高档（500-800元人民币），那么我就有更多灵活性——我只需要确保至少一家我选择的餐厅评分在4.0或以上，且景点门票低于180元人民币。对于更经济实惠的酒店（200-500元人民币范围），我只需要确保至少一家餐厅的评分在3.2或以上。你能帮我整理出这份行程吗？

##### 提交结果格式

{ "time": "2025-10-01", "city": "城市名称", "hotel": "酒店名称", "afternoon_restaurant": "餐厅名称", "afternoon_attraction": "景点名称", "evening_restaurant": "餐厅名称" },

{ "time": "2025-10-02", "city": "城市名称", "hotel": "酒店名称", "afternoon_restaurant": "餐厅名称", "afternoon_attraction": "景点名称", "evening_restaurant": "餐厅名称" },

{ "time": "2025-10-03", "city": "城市名称", "hotel": "酒店名称", "afternoon_restaurant": "餐厅名称", "afternoon_attraction": "景点名称", "evening_restaurant": "餐厅名称" }

### 旅行规划工具集

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>函数名称</td><td style='text-align: center; word-wrap: break-word;'>描述</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_attractions_by_city(城市)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市的所有景点。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_cities()</td><td style='text-align: center; word-wrap: break-word;'>从数据库获取所有城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_hotels_by_city(城市)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市的所有酒店。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_all_restaurants_by_city(城市)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市的所有餐厅。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_attraction(景点)</td><td style='text-align: center; word-wrap: break-word;'>根据给定景点名称获取其所在城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_hotel(酒店)</td><td style='text-align: center; word-wrap: break-word;'>根据给定酒店名称获取其所在城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_by_restaurant(餐厅)</td><td style='text-align: center; word-wrap: break-word;'>根据给定餐厅名称获取其所在城市。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_city_transport(城市)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市的所有市内交通选项。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_attraction(信息关键词, 景点)</td><td style='text-align: center; word-wrap: break-word;'>获取指定景点的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_city(信息关键词, 城市)</td><td style='text-align: center; word-wrap: break-word;'>获取指定城市的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_hotel(信息关键词, 酒店)</td><td style='text-align: center; word-wrap: break-word;'>获取指定酒店的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_infos_by_restaurant(信息关键词, 餐厅)</td><td style='text-align: center; word-wrap: break-word;'>获取指定餐厅的特定信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_inter_city_transport(出发城市, 目的城市)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市对之间的所有交通方式。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>get_weather_by_city_date(城市, 日期)</td><td style='text-align: center; word-wrap: break-word;'>获取给定城市-日期对的天气信息。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>submit_result(答案文本)</td><td style='text-align: center; word-wrap: break-word;'>提交最终答案内容。</td></tr></table>

## 4. 评估

### 4.1. 主要结果

我们在 MMLU-Pro (Wang et al., 2024)、GPQA Diamond (Rein et al., 2023)、Human Last Exam (HLE) Text-only (Phan et al., 2025)、LiveCodeBench (2024.08-2025.04)、Code 上评估模型。

---


forces, Aider-Polyglot, AIME 2025, HMMT Feb 2025, HMMT Nov 2025 (Balunović et al., 2025), IMOAnswerBench (Luong et al., 2025), Terminal Bench 2.0, SWE-Verified (OpenAI, 2024b), SWE Multilingual (Yang et al., 2025), BrowseComp (Wei et al., 2025), BrowseCompZh (Zhou et al., 2025),  $\tau^{2}$-bench (Barres et al., 2025), MCP-Universe (Luo et al., 2025), MCP-Mark (EvalSys, 2025), and Tool-Decathlon (Li et al., 2025). Tool-use benchmarks are evaluated using the standard function call format, wherein models are configured to thinking mode. For MCP-Universe (Luo et al., 2025) and MCP-Mark (EvalSys, 2025), we evaluate all models with our internal environment, because the search and playwright environment might be slightly different from the official setting. We set the temperature to 1.0, and the context window to 128K tokens. For math-related tasks such as AIME, HMMT, IMOAnswerBench, and HLE, we eval with the following template: "{\question}\nPlease reason step by step, and put your final answer within \boxed{}." In the case of HLE, we additionally assessed DeepSeek-V3.2-Thinking using the official template, resulting in a score of 23.9.

<div style="text-align: center;">Table 2 | Comparison between DeepSeek-V3.2 and closed/open models. For open models, we just compare with models supports thinking in tooluse. Numbers in bold represent the best scores within each model class (open-source and closed-source). The  $\tau^{2}$-Bench result is computed by the average of each category. Regarding BrowseComp, the performance with the context management technique is noted with  $*$.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>Benchmark (Metric)</td><td style='text-align: center; word-wrap: break-word;'>Claude-4.5-Sonnet</td><td style='text-align: center; word-wrap: break-word;'>GPT-5 High</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0 Pro</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2 Thinking</td><td style='text-align: center; word-wrap: break-word;'>MiniMax M2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2 Thinking</td></tr><tr><td rowspan="3">English</td><td style='text-align: center; word-wrap: break-word;'>MMLU-Pro (EM)</td><td style='text-align: center; word-wrap: break-word;'>88.2</td><td style='text-align: center; word-wrap: break-word;'>87.5</td><td style='text-align: center; word-wrap: break-word;'>90.1</td><td style='text-align: center; word-wrap: break-word;'>84.6</td><td style='text-align: center; word-wrap: break-word;'>82.0</td><td style='text-align: center; word-wrap: break-word;'>85.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>83.4</td><td style='text-align: center; word-wrap: break-word;'>85.7</td><td style='text-align: center; word-wrap: break-word;'>91.9</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>77.7</td><td style='text-align: center; word-wrap: break-word;'>82.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>13.7</td><td style='text-align: center; word-wrap: break-word;'>26.3</td><td style='text-align: center; word-wrap: break-word;'>37.7</td><td style='text-align: center; word-wrap: break-word;'>23.9</td><td style='text-align: center; word-wrap: break-word;'>12.5</td><td style='text-align: center; word-wrap: break-word;'>25.1</td></tr><tr><td rowspan="2">Code</td><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>64.0</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>90.7</td><td style='text-align: center; word-wrap: break-word;'>82.6</td><td style='text-align: center; word-wrap: break-word;'>83.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Codeforces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>1480</td><td style='text-align: center; word-wrap: break-word;'>2537</td><td style='text-align: center; word-wrap: break-word;'>2708</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386</td></tr><tr><td rowspan="4">Math</td><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>87.0</td><td style='text-align: center; word-wrap: break-word;'>94.6</td><td style='text-align: center; word-wrap: break-word;'>95.0</td><td style='text-align: center; word-wrap: break-word;'>94.5</td><td style='text-align: center; word-wrap: break-word;'>78.3</td><td style='text-align: center; word-wrap: break-word;'>93.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>79.2</td><td style='text-align: center; word-wrap: break-word;'>88.3</td><td style='text-align: center; word-wrap: break-word;'>97.5</td><td style='text-align: center; word-wrap: break-word;'>89.4</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>92.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>81.7</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>93.3</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>90.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>76.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td><td style='text-align: center; word-wrap: break-word;'>78.6</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>78.3</td></tr><tr><td rowspan="3">Code Agent</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0 (Acc)</td><td style='text-align: center; word-wrap: break-word;'>42.8</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>54.2</td><td style='text-align: center; word-wrap: break-word;'>35.7</td><td style='text-align: center; word-wrap: break-word;'>30.0</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>74.9</td><td style='text-align: center; word-wrap: break-word;'>76.2</td><td style='text-align: center; word-wrap: break-word;'>71.3</td><td style='text-align: center; word-wrap: break-word;'>69.4</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>68.0</td><td style='text-align: center; word-wrap: break-word;'>55.3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>61.1</td><td style='text-align: center; word-wrap: break-word;'>56.5</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="3">Search Agent</td><td style='text-align: center; word-wrap: break-word;'>BrowseComp (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>24.1</td><td style='text-align: center; word-wrap: break-word;'>54.9</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>$-/60.2^{*}$</td><td style='text-align: center; word-wrap: break-word;'>44.0</td><td style='text-align: center; word-wrap: break-word;'>51.4/67.6*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BrowseCompZh (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>42.4</td><td style='text-align: center; word-wrap: break-word;'>63.0</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>62.3</td><td style='text-align: center; word-wrap: break-word;'>48.5</td><td style='text-align: center; word-wrap: break-word;'>65.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>32.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>45.8</td><td style='text-align: center; word-wrap: break-word;'>44.9</td><td style='text-align: center; word-wrap: break-word;'>31.8</td><td style='text-align: center; word-wrap: break-word;'>40.8</td></tr><tr><td rowspan="4">ToolUse</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-Bench(Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>84.7</td><td style='text-align: center; word-wrap: break-word;'>80.2</td><td style='text-align: center; word-wrap: break-word;'>85.4</td><td style='text-align: center; word-wrap: break-word;'>74.3</td><td style='text-align: center; word-wrap: break-word;'>76.9</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe (Success Rate)</td><td style='text-align: center; word-wrap: break-word;'>46.5</td><td style='text-align: center; word-wrap: break-word;'>47.9</td><td style='text-align: center; word-wrap: break-word;'>50.7</td><td style='text-align: center; word-wrap: break-word;'>35.6</td><td style='text-align: center; word-wrap: break-word;'>29.4</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>33.3</td><td style='text-align: center; word-wrap: break-word;'>50.9</td><td style='text-align: center; word-wrap: break-word;'>43.1</td><td style='text-align: center; word-wrap: break-word;'>20.4</td><td style='text-align: center; word-wrap: break-word;'>24.4</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>29.0</td><td style='text-align: center; word-wrap: break-word;'>36.4</td><td style='text-align: center; word-wrap: break-word;'>17.6</td><td style='text-align: center; word-wrap: break-word;'>16.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

DeepSeek-V3.2 achieves similar performance with GPT-5-high on reasoning tasks, but is slightly worse than Gemini-3.0-Pro. Compared to K2-Thinking, DeepSeek-V3.2 achieves comparable scores with substantially fewer output tokens, as shown in Table 3. These performance gains can be attributed to the increased computational resources allocated to RL training. Over recent months, we have observed consistent performance improvements correlating with extended RL training budget, which already exceeds 10% of the pre-training cost. We hypothesize that reasoning capabilities could be further enhanced with additional computational budget allocation. Notably, the performance of DeepSeek-V3.2 presented herein is constrained by a length constraint reward model; upon removal of the restriction, we observe further improvement in
> forces, Aider-Polyglot, AIME 2025, HMMT Feb 2025, HMMT Nov 2025 (Balunović et al., 2025), IMOAnswerBench (Luong et al., 2025), Terminal Bench 2.0, SWE-Verified (OpenAI, 2024b), SWE Multilingual (Yang et al., 2025), BrowseComp (Wei et al., 2025), BrowseCompZh (Zhou et al., 2025), $\tau^{2}$-bench (Barres et al., 2025), MCP-Universe (Luo et al., 2025), MCP-Mark (EvalSys, 2025), 以及 Tool-Decathlon (Li et al., 2025)。工具使用基准测试采用标准函数调用格式进行评估，其中模型被配置为思考模式。对于 MCP-Universe (Luo et al., 2025) 和 MCP-Mark (EvalSys, 2025)，我们使用内部环境评估所有模型，因为搜索和 playwright 环境可能与官方设置略有不同。我们将温度设置为 1.0，上下文窗口设置为 128K 个标记。对于 AIME、HMMT、IMOAnswerBench 和 HLE 等数学相关任务，我们使用以下模板进行评估："{\question}\n请逐步推理，并将最终答案放在 \boxed{} 中。" 对于 HLE，我们还使用官方模板评估了 DeepSeek-V3.2-Thinking，其得分为 23.9。

<div style="text-align: center;">表 2 | DeepSeek-V3.2 与闭源/开源模型的比较。对于开源模型，我们仅与支持工具使用中思考功能的模型进行比较。加粗数字代表每个模型类别（开源和闭源）中的最佳分数。$\tau^{2}$-Bench 的结果通过计算每个类别的平均值得出。关于 BrowseComp，采用上下文管理技术后的性能以 $*$ 标注。</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>基准测试（指标）</td><td style='text-align: center; word-wrap: break-word;'>Claude-4.5-Sonnet</td><td style='text-align: center; word-wrap: break-word;'>GPT-5 High</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0 Pro</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2 Thinking</td><td style='text-align: center; word-wrap: break-word;'>MiniMax M2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2 Thinking</td></tr><tr><td rowspan="3">英语</td><td style='text-align: center; word-wrap: break-word;'>MMLU-Pro (EM)</td><td style='text-align: center; word-wrap: break-word;'>88.2</td><td style='text-align: center; word-wrap: break-word;'>87.5</td><td style='text-align: center; word-wrap: break-word;'>90.1</td><td style='text-align: center; word-wrap: break-word;'>84.6</td><td style='text-align: center; word-wrap: break-word;'>82.0</td><td style='text-align: center; word-wrap: break-word;'>85.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>83.4</td><td style='text-align: center; word-wrap: break-word;'>85.7</td><td style='text-align: center; word-wrap: break-word;'>91.9</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>77.7</td><td style='text-align: center; word-wrap: break-word;'>82.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>13.7</td><td style='text-align: center; word-wrap: break-word;'>26.3</td><td style='text-align: center; word-wrap: break-word;'>37.7</td><td style='text-align: center; word-wrap: break-word;'>23.9</td><td style='text-align: center; word-wrap: break-word;'>12.5</td><td style='text-align: center; word-wrap: break-word;'>25.1</td></tr><tr><td rowspan="2">代码</td><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>64.0</td><td style='text-align: center; word-wrap: break-word;'>84.5</td><td style='text-align: center; word-wrap: break-word;'>90.7</td><td style='text-align: center; word-wrap: break-word;'>82.6</td><td style='text-align: center; word-wrap: break-word;'>83.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Codeforces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>1480</td><td style='text-align: center; word-wrap: break-word;'>2537</td><td style='text-align: center; word-wrap: break-word;'>2708</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386</td></tr><tr><td rowspan="4">数学</td><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>87.0</td><td style='text-align: center; word-wrap: break-word;'>94.6</td><td style='text-align: center; word-wrap: break-word;'>95.0</td><td style='text-align: center; word-wrap: break-word;'>94.5</td><td style='text-align: center; word-wrap: break-word;'>78.3</td><td style='text-align: center; word-wrap: break-word;'>93.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>79.2</td><td style='text-align: center; word-wrap: break-word;'>88.3</td><td style='text-align: center; word-wrap: break-word;'>97.5</td><td style='text-align: center; word-wrap: break-word;'>89.4</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>92.5</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>81.7</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>93.3</td><td style='text-align: center; word-wrap: break-word;'>89.2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>90.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>76.0</td><td style='text-align: center; word-wrap: break-word;'>83.3</td><td style='text-align: center; word-wrap: break-word;'>78.6</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>78.3</td></tr><tr><td rowspan="3">代码智能体</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0 (Acc)</td><td style='text-align: center; word-wrap: break-word;'>42.8</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>54.2</td><td style='text-align: center; word-wrap: break-word;'>35.7</td><td style='text-align: center; word-wrap: break-word;'>30.0</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>74.9</td><td style='text-align: center; word-wrap: break-word;'>76.2</td><td style='text-align: center; word-wrap: break-word;'>71.3</td><td style='text-align: center; word-wrap: break-word;'>69.4</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual (Resolved)</td><td style='text-align: center; word-wrap: break-word;'>68.0</td><td style='text-align: center; word-wrap: break-word;'>55.3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>61.1</td><td style='text-align: center; word-wrap: break-word;'>56.5</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="3">搜索智能体</td><td style='text-align: center; word-wrap: break-word;'>BrowseComp (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>24.1</td><td style='text-align: center; word-wrap: break-word;'>54.9</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>$-/60.2^{*}$</td><td style='text-align: center; word-wrap: break-word;'>44.0</td><td style='text-align: center; word-wrap: break-word;'>51.4/67.6*</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>BrowseCompZh (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>42.4</td><td style='text-align: center; word-wrap: break-word;'>63.0</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>62.3</td><td style='text-align: center; word-wrap: break-word;'>48.5</td><td style='text-align: center; word-wrap: break-word;'>65.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>32.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td><td style='text-align: center; word-wrap: break-word;'>45.8</td><td style='text-align: center; word-wrap: break-word;'>44.9</td><td style='text-align: center; word-wrap: break-word;'>31.8</td><td style='text-align: center; word-wrap: break-word;'>40.8</td></tr><tr><td rowspan="4">工具使用</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-Bench(Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>84.7</td><td style='text-align: center; word-wrap: break-word;'>80.2</td><td style='text-align: center; word-wrap: break-word;'>85.4</td><td style='text-align: center; word-wrap: break-word;'>74.3</td><td style='text-align: center; word-wrap: break-word;'>76.9</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe (Success Rate)</td><td style='text-align: center; word-wrap: break-word;'>46.5</td><td style='text-align: center; word-wrap: break-word;'>47.9</td><td style='text-align: center; word-wrap: break-word;'>50.7</td><td style='text-align: center; word-wrap: break-word;'>35.6</td><td style='text-align: center; word-wrap: break-word;'>29.4</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>33.3</td><td style='text-align: center; word-wrap: break-word;'>50.9</td><td style='text-align: center; word-wrap: break-word;'>43.1</td><td style='text-align: center; word-wrap: break-word;'>20.4</td><td style='text-align: center; word-wrap: break-word;'>24.4</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>29.0</td><td style='text-align: center; word-wrap: break-word;'>36.4</td><td style='text-align: center; word-wrap: break-word;'>17.6</td><td style='text-align: center; word-wrap: break-word;'>16.0</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

> DeepSeek-V3.2 在推理任务上与 GPT-5-high 表现相近，但略逊于 Gemini-3.0-Pro。与 K2-Thinking 相比，DeepSeek-V3.2 以显著更少的输出标记取得了可比的分数，如表 3 所示。这些性能提升可归因于强化学习训练所分配的计算资源增加。最近几个月，我们观察到性能的持续提升与强化学习训练预算的延长相关，该预算已超过预训练成本的 10%。我们假设，通过分配额外的计算预算，推理能力可能得到进一步增强。值得注意的是，本文展示的 DeepSeek-V3.2 性能受限于一个长度约束奖励模型；在移除该限制后，我们观察到其在……方面有进一步的提升。

---


model performance, as detailed in Section 4.2.

In code agent evaluations, DeepSeek-V3.2 significantly outperforms open-source LLMs on both SWE-bench Verified and Terminal Bench 2.0, demonstrating its potential within real-world coding workflows. Regarding Terminal Bench 2.0, as previously noted, our context management strategy for the 'thinking mode' is currently incompatible with Terminus; consequently, the reported score of 46.4 was achieved using the Claude Code framework. We also evaluated DeepSeek-V3.2 with Terminus in non-thinking mode, yielding a score of 39.3. For SWE-bench Verified, the primary score was obtained using our internal framework. Robustness tests across other settings—including the Claude Code and RooCode frameworks, as well as non-thinking mode—produced consistent results, ranging from 72 to 74.

For the search agent evaluation, we assess our models using a standard commercial search API. Since DeepSeek-V3.2 supports a maximum context length of only 128K, approximately 20%+ of the test cases exceed this limit. To address this, we employ a context management method to derive the final score. For reference, the score is 51.4 without context management. Further details are provided in Section 4.4.

On tool-use benchmarks, DeepSeek-V3.2 substantially narrows the performance gap between open-source and closed-source LLMs, though it remains below frontier models. For  $\tau^{2}$-bench, we employ the model itself as the user agent, achieving final category scores of 63.8 (Airline), 81.1 (Retail), and 96.2 (Telecom). For the MCP benchmarks, we employ the function calling format and place tool outputs within messages designated with the 'tool' role, rather than the 'user' role. During our testing, we observed that DeepSeek-V3.2 frequently engages in redundant self-verification, generating excessively long trajectories. This tendency often causes the context length to exceed the 128K limit, particularly in tasks such as MCP-Mark GitHub and Playwright evaluation. Consequently, this phenomenon hinders the final performance of DeepSeek-V3.2. However, integrating context management strategies can further enhance performance. We identify this as a direction for future work and a practical consideration for users. Even if DeepSeek-V3.2 suffers from the issue, it still significantly outperforms existing open models. Notably, since the environments and toolsets employed in these benchmarks were not encountered during RL training, the observed improvements demonstrate DeepSeek-V3.2's capacity to generalize its reasoning strategies to out-of-domain agentic scenarios. The evaluation of non-thinking model in the agent scenario is shown in Appendix Table 9.

### 4.2. Results of DeepSeek-V3.2-Speciale

Table 3 demonstrates that DeepSeek-V3.2-Speciale achieves superior performance by leveraging increased reasoning tokens, surpassing the state-of-the-art Gemini-3.0-Pro across multiple benchmarks. Remarkably, as shown in Table 4, this general-purpose model attains gold-medal level performance in the 2025 International Olympiad in Informatics (IOI) and the ICPC World Finals (ICPC WF) without targeted training. Furthermore, by incorporating techniques from Shao et al. (2025), the model excels in complex proof tasks, reaching gold-medal thresholds in the 2025 International Mathematical Olympiad (IMO) and China Mathematical Olympiad (CMO) $^{5}$. Detailed evaluation protocols are provided in Appendix D.

However, the token efficiency of DeepSeek-V3.2-Speciale remains significantly inferior to that of Gemini-3.0-Pro. To mitigate deployment costs and latency, we imposed stricter token constraints during the training of the official DeepSeek-V3.2, aiming to optimize the trade-off
> 模型性能详见第4.2节。

> 在代码智能体评估中，DeepSeek-V3.2 在 SWE-bench Verified 和 Terminal Bench 2.0 上均显著优于开源大语言模型，展现了其在真实世界编码工作流中的潜力。关于 Terminal Bench 2.0，如前所述，我们用于“思考模式”的上下文管理策略目前与 Terminus 不兼容；因此，报告的 46.4 分是使用 Claude Code 框架实现的。我们也评估了 DeepSeek-V3.2 在 Terminus 非思考模式下的表现，得分为 39.3。对于 SWE-bench Verified，主要分数是使用我们内部框架获得的。在其他设置（包括 Claude Code 和 RooCode 框架，以及非思考模式）下的鲁棒性测试产生了一致的结果，范围在 72 到 74 之间。

> 对于搜索智能体评估，我们使用标准的商业搜索 API 来评估我们的模型。由于 DeepSeek-V3.2 仅支持最大 128K 的上下文长度，大约 20%+ 的测试用例超出了此限制。为了解决这个问题，我们采用了一种上下文管理方法来得出最终分数。作为参考，不使用上下文管理时的分数是 51.4。更多细节见第4.4节。

> 在工具使用基准测试上，DeepSeek-V3.2 大幅缩小了开源与闭源大语言模型之间的性能差距，尽管仍低于前沿模型。对于 $\tau^{2}$-bench，我们使用模型本身作为用户代理，获得的最终类别分数为 63.8（航空）、81.1（零售）和 96.2（电信）。对于 MCP 基准测试，我们采用函数调用格式，并将工具输出放在指定为“tool”角色的消息中，而非“user”角色。在我们的测试中，我们观察到 DeepSeek-V3.2 频繁进行冗余的自我验证，生成了过长的轨迹。这种倾向常常导致上下文长度超过 128K 的限制，特别是在 MCP-Mark GitHub 和 Playwright 评估等任务中。因此，这种现象阻碍了 DeepSeek-V3.2 的最终表现。然而，集成上下文管理策略可以进一步提升性能。我们将此确定为未来的工作方向，也是用户的实际考量点。即使 DeepSeek-V3.2 存在此问题，它仍然显著优于现有的开源模型。值得注意的是，由于这些基准测试中使用的环境和工具集在强化学习训练期间并未遇到，观察到的改进证明了 DeepSeek-V3.2 将其推理策略泛化到领域外智能体场景的能力。非思考模型在智能体场景中的评估见附录表9。

### 4.2. DeepSeek-V3.2-Speciale 的结果

> 表3表明，DeepSeek-V3.2-Speciale 通过利用更多的推理 token 实现了卓越的性能，在多个基准测试上超越了最先进的 Gemini-3.0-Pro。值得注意的是，如表4所示，这个通用模型在没有针对性训练的情况下，在 2025 年国际信息学奥林匹克竞赛（IOI）和国际大学生程序设计竞赛世界总决赛（ICPC WF）中达到了金牌级别的表现。此外，通过结合 Shao 等人（2025）的技术，该模型在复杂证明任务中表现出色，达到了 2025 年国际数学奥林匹克竞赛（IMO）和中国数学奥林匹克竞赛（CMO）的金牌阈值 $^{5}$。详细的评估方案见附录 D。

> 然而，DeepSeek-V3.2-Speciale 的 token 效率仍然显著低于 Gemini-3.0-Pro。为了降低部署成本和延迟，我们在官方 DeepSeek-V3.2 的训练中施加了更严格的 token 约束，旨在优化权衡。

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
> 表3 | 推理模型的基准性能与效率。每个基准测试的单元格中展示了准确率和输出token数量（以千计）。每个基准测试的最高准确率以粗体标出；次高准确率以下划线标出。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2">Benchmark</td><td style='text-align: center; word-wrap: break-word;'>GPT-5</td><td style='text-align: center; word-wrap: break-word;'>Gemini-3.0</td><td style='text-align: center; word-wrap: break-word;'>Kimi-K2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2</td><td style='text-align: center; word-wrap: break-word;'>DeepSeek-V3.2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>High</td><td style='text-align: center; word-wrap: break-word;'>Pro</td><td style='text-align: center; word-wrap: break-word;'>Thinking</td><td style='text-align: center; word-wrap: break-word;'>Thinking</td><td style='text-align: center; word-wrap: break-word;'>Speciale</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>AIME 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>94.6 (13k)</td><td style='text-align: center; word-wrap: break-word;'>95.0 (15k)</td><td style='text-align: center; word-wrap: break-word;'>94.5 (24k)</td><td style='text-align: center; word-wrap: break-word;'>93.1 (16k)</td><td style='text-align: center; word-wrap: break-word;'>96.0 (23k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Feb 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>88.3 (16k)</td><td style='text-align: center; word-wrap: break-word;'>97.5 (16k)</td><td style='text-align: center; word-wrap: break-word;'>89.4 (31k)</td><td style='text-align: center; word-wrap: break-word;'>92.5 (19k)</td><td style='text-align: center; word-wrap: break-word;'>99.2 (27k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMMT Nov 2025 (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>89.2 (20k)</td><td style='text-align: center; word-wrap: break-word;'>93.3 (15k)</td><td style='text-align: center; word-wrap: break-word;'>89.2 (29k)</td><td style='text-align: center; word-wrap: break-word;'>90.2 (18k)</td><td style='text-align: center; word-wrap: break-word;'>94.4 (25k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMOAnswerBench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>76.0 (31k)</td><td style='text-align: center; word-wrap: break-word;'>83.3 (18k)</td><td style='text-align: center; word-wrap: break-word;'>78.6 (37k)</td><td style='text-align: center; word-wrap: break-word;'>78.3 (27k)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (45k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LiveCodeBench (Pass@1-COT)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (13k)</td><td style='text-align: center; word-wrap: break-word;'>90.7 (13k)</td><td style='text-align: center; word-wrap: break-word;'>82.6 (29k)</td><td style='text-align: center; word-wrap: break-word;'>83.3 (16k)</td><td style='text-align: center; word-wrap: break-word;'>88.7 (27k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CodeForces (Rating)</td><td style='text-align: center; word-wrap: break-word;'>2537 (29k)</td><td style='text-align: center; word-wrap: break-word;'>2708 (22k)</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>2386 (42k)</td><td style='text-align: center; word-wrap: break-word;'>2701 (77k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GPQA Diamond (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>85.7 (8k)</td><td style='text-align: center; word-wrap: break-word;'>91.9 (8k)</td><td style='text-align: center; word-wrap: break-word;'>84.5 (12k)</td><td style='text-align: center; word-wrap: break-word;'>82.4 (7k)</td><td style='text-align: center; word-wrap: break-word;'>85.7 (16k)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HLE (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>26.3 (15k)</td><td style='text-align: center; word-wrap: break-word;'>37.7 (15k)</td><td style='text-align: center; word-wrap: break-word;'>23.9 (24k)</td><td style='text-align: center; word-wrap: break-word;'>25.1 (21k)</td><td style='text-align: center; word-wrap: break-word;'>30.6 (35k)</td></tr></table>

> 在性能与成本之间。我们相信token效率仍然是未来研究的一个关键领域。

> 表4 | DeepSeek-V3.2-Speciale在顶级数学和编程竞赛中的表现。对于ICPC WF 2025，我们报告了每个成功解决问题的提交次数。DeepSeek-V3.2-Speciale在ICPC WF 2025中排名第2，在IOI 2025中排名第10。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Competition</td><td style='text-align: center; word-wrap: break-word;'>P1</td><td style='text-align: center; word-wrap: break-word;'>P2</td><td style='text-align: center; word-wrap: break-word;'>P3</td><td style='text-align: center; word-wrap: break-word;'>P4</td><td style='text-align: center; word-wrap: break-word;'>P5</td><td style='text-align: center; word-wrap: break-word;'>P6</td><td style='text-align: center; word-wrap: break-word;'>Overall</td><td style='text-align: center; word-wrap: break-word;'>Medal</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IMO 2025</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>35/42</td><td style='text-align: center; word-wrap: break-word;'>Gold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CMO 2025</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>21</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>18</td><td style='text-align: center; word-wrap: break-word;'>102/126</td><td style='text-align: center; word-wrap: break-word;'>Gold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>IOI 2025</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>82</td><td style='text-align: center; word-wrap: break-word;'>72</td><td style='text-align: center; word-wrap: break-word;'>100</td><td style='text-align: center; word-wrap: break-word;'>55</td><td style='text-align: center; word-wrap: break-word;'>83</td><td style='text-align: center; word-wrap: break-word;'>492/600</td><td style='text-align: center; word-wrap: break-word;'>Gold</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Competition</td><td style='text-align: center; word-wrap: break-word;'>A</td><td style='text-align: center; word-wrap: break-word;'>B</td><td style='text-align: center; word-wrap: break-word;'>C</td><td style='text-align: center; word-wrap: break-word;'>E</td><td style='text-align: center; word-wrap: break-word;'>F</td><td style='text-align: center; word-wrap: break-word;'>H</td><td style='text-align: center; word-wrap: break-word;'>J</td><td style='text-align: center; word-wrap: break-word;'>L</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ICPC WF 2025</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>10/12</td></tr></table>

### 4.3. 合成智能体任务

> 在本节中，我们进行了消融实验，以研究合成智能体任务的效果。我们主要关注两个问题。首先，合成任务对于强化学习来说是否足够具有挑战性？其次，这些合成任务的泛化能力如何，即它们能否迁移到不同的下游任务或真实世界环境中？

> 针对第一个问题，我们从通用合成智能体任务中随机抽取50个实例，并评估用于合成的模型以及前沿闭源大语言模型。如表5所示，DeepSeek-V3.2-Exp的准确率仅为12%，而前沿闭源模型的最高准确率也仅为62%。这些结果表明，合成数据中包含的智能体任务对于DeepSeek-V3.2-Exp和前沿闭源模型都具有挑战性。

> 为了研究在合成数据上进行强化学习能否泛化到不同任务或真实世界环境，我们将强化学习应用于DeepSeek-V3.2的SFT检查点（记为DeepSeek-V3.2-SFT）。为了排除长链思维和其他强化学习数据的影响，我们仅在非思维模式下对合成智能体任务进行强化学习。然后，我们将该模型与DeepSeek-V3.2-SFT和DeepSeek-V3.2-Exp进行比较，其中DeepSeek-V3.2-Exp仅在搜索和代码环境中进行了强化学习训练。如图5所示，在合成数据上进行大规模强化学习带来了显著的性能提升。

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
> 表5 | 不同模型在通用合成任务上的准确率。

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

> 图5 | 使用纯合成通用智能体数据对DeepSeek-V3.2-SFT进行的强化学习训练。
> 
> 在Tau2Bench、MCP-Mark和MCP-Universe基准测试上，相较于DeepSeek-V3.2-SFT模型取得了显著的性能提升。相反，将强化学习限制在代码和搜索场景中，并不能提升模型在这些基准测试上的表现，这进一步凸显了合成数据的潜力。

### 4.4. 搜索智能体的上下文管理

> 即使拥有诸如128k这样的扩展上下文窗口，智能体工作流（特别是在基于搜索的场景中）仍经常遇到最大长度限制，导致推理过程被过早截断。这一瓶颈抑制了测试时计算潜力的充分发挥。为了解决这个问题，我们引入了上下文管理机制，采用简单的策略在测试时（当令牌使用量超过上下文窗口长度的80%时）扩展令牌预算。这些策略包括：（1）摘要，即对溢出的轨迹进行总结并重新启动展开过程；（2）丢弃-75%，即丢弃轨迹中前75%的工具调用历史以释放空间；（3）全部丢弃，即通过丢弃所有先前的工具调用历史来重置上下文（类似于新的上下文工具（Anthropic, 2025a））。为了进行比较，我们还实现了一个并行扩展基线，即“并行-最少步骤”，该方法采样N个独立的轨迹并

---


<div style="text-align: center;"><img src="imgs/img_in_chart_box_170_177_1019_586.jpg" alt="Image" width="71%" /></div>

<div style="text-align: center;">Figure 6 | Accuracy of Browsecomp with different test-time compute expansion strategies.</div>

selects the trajectory with the fewest steps.

We evaluate these strategies on the BrowseComp benchmark (Wei et al., 2025). As illustrated in Figure 6, under varying compute budgets, context management leads to significant performance gains by allowing the model to scale up test-time compute, providing more space to perform additional execution steps. For example, Summary extends the average steps from 140 to 364, improving performance from 53.4 to 60.2. However, its overall efficiency is relatively low. Despite its simplicity, Discard-all performs well in both efficiency and scalability, achieving a score of 67.6, comparable to parallel scaling while using significantly fewer steps.

In summary, test-time compute can be scaled either serially through context management or in parallel, both effectively extending the model's problem-solving capacity. However, different strategies exhibit varying efficiency and scalability. Thus, it is crucial to account for actual compute costs when benchmarking model performance. Meanwhile, finding the optimal combination of serial and parallel scaling to maximize both efficiency and scalability remains a crucial direction for future work.

## 5. Conclusion, Limitation, and Future Work

In this work, we introduced DeepSeek-V3.2, a framework that effectively bridges the gap between computational efficiency and advanced reasoning capabilities. Using DSA, we addressed critical computation complexity without sacrificing long-context performance. By increasing computational budget, DeepSeek-V3.2 achieves comparable performance with GPT-5 on reasoning benchmarks. Finally, the integration of our large-scale agentic task synthesis pipeline significantly enhances tool-use proficiency, unlocking new possibilities for robust and generalizable AI agents with open LLM. Furthermore, our high-compute variant, DeepSeek-V3.2-Speciale, validated by gold-medal achievements in the IMO and IOI, sets a milestone for open LLMs.

Despite these achievements, we acknowledge certain limitations when compared to frontier closed-source models such as Gemini-3.0-Pro. First, due to fewer total training FLOPs, the breadth of world knowledge in DeepSeek-V3.2 still lags behind that of leading proprietary
> <div style="text-align: center;"><img src="imgs/img_in_chart_box_170_177_1019_586.jpg" alt="Image" width="71%" /></div>

> <div style="text-align: center;">图 6 | 采用不同测试时计算扩展策略时 Browsecomp 的准确率。</div>

> 选择步骤最少的轨迹。

> 我们在 BrowseComp 基准测试（Wei et al., 2025）上评估了这些策略。如图 6 所示，在不同的计算预算下，上下文管理通过允许模型扩展测试时计算，为执行额外步骤提供了更多空间，从而带来了显著的性能提升。例如，摘要策略将平均步骤数从 140 步扩展到 364 步，性能从 53.4 提升至 60.2。然而，其整体效率相对较低。尽管方法简单，但“全部丢弃”策略在效率和可扩展性方面都表现良好，得分达到 67.6，与并行扩展相当，同时使用的步骤数显著减少。

> 总之，测试时计算可以通过上下文管理进行串行扩展，也可以并行扩展，两者都能有效扩展模型的问题解决能力。然而，不同的策略表现出不同的效率和可扩展性。因此，在对模型性能进行基准测试时，考虑实际的计算成本至关重要。同时，寻找串行和并行扩展的最佳组合，以最大化效率和可扩展性，仍然是未来工作的关键方向。

## 5. 结论、局限性与未来工作

> 在这项工作中，我们介绍了 DeepSeek-V3.2，一个有效弥合计算效率与高级推理能力之间差距的框架。通过使用 DSA，我们在不牺牲长上下文性能的前提下解决了关键的计算复杂度问题。通过增加计算预算，DeepSeek-V3.2 在推理基准测试中取得了与 GPT-5 相当的性能。最后，我们大规模智能体任务合成管线的集成显著增强了工具使用能力，为基于开源 LLM 构建鲁棒且可泛化的 AI 智能体开辟了新的可能性。此外，我们的高计算变体 DeepSeek-V3.2-Speciale，凭借在国际数学奥林匹克竞赛（IMO）和国际信息学奥林匹克竞赛（IOI）中取得的金牌成就得到了验证，为开源 LLM 树立了一个里程碑。

> 尽管取得了这些成就，与 Gemini-3.0-Pro 等前沿闭源模型相比，我们承认存在某些局限性。首先，由于总训练 FLOPs 较少，DeepSeek-V3.2 所涵盖的世界知识的广度仍然落后于领先的专有模型。

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
模型。我们计划在未来的迭代中，通过扩大预训练计算规模来解决这一知识差距。其次，令牌效率仍然是一个挑战；DeepSeek-V3.2 通常需要更长的生成轨迹（即更多的令牌）才能达到像 Gemini-3.0-Pro 这类模型的输出质量。未来的工作将集中于优化模型推理链的智能密度以提高效率。第三，在解决复杂任务方面，我们仍逊色于前沿模型，这促使我们进一步优化基础模型和后训练方案。

## 参考文献

> Anthropic. System card: Claude opus 4.5, 2025a. URL https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf.
> 
> Anthropic. Introducing claude sonnet 4.5, 2025b. URL https://www.anthropic.com/news/claude-sonnet-4-51.
> 
> M. Balunović, J. Dekoninck, I. Petrov, N. Jovanović, and M. Vechev. Matharena: Evaluating llms on uncontaminated math competitions. Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmark, 2025.
> 
> V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan.  $\tau^{2}$-bench: Evaluating conversational agents in a dual-control environment, 2025. URL https://arxiv.org/abs/2506.07982.
> 
> DeepMind. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025a.
> 
> G. DeepMind. Gemini 3 pro model card, 2025b. URL https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf.
> 
> DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language model. CoRR, abs/2405.04434, 2024. doi: 10.48550/ARXIV.2405.04434. URL https://doi.org/10.48550/arXiv.2405.04434.
> 
> DeepSeek-AI. Deepseek-v3 technical report, 2024. URL https://arxiv.org/abs/2412.19437.
> 
> DeepSeek-AI. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nature, 645(8081):633–638, 2025.
> 
> EvalSys. Mcpmark leaderboard, 2025. URL https://mcpmark.ai/leaderboard.
> 
> J. Li, W. Zhao, J. Zhao, W. Zeng, H. Wu, X. Wang, R. Ge, Y. Cao, Y. Huang, W. Liu, et al. The tool decathlon: Benchmarking language agents for diverse, realistic, and long-horizon task execution. arXiv preprint arXiv:2510.25726, 2025.
> 
> Z. Luo, Z. Shen, W. Yang, Z. Zhao, P. Jwalapuram, A. Saha, D. Sahoo, S. Savarese, C. Xiong, and J. Li. Mcp-universe: Benchmarking large language models with real-world model context protocol servers. arXiv preprint arXiv:2508.14704, 2025.
> 
> T. Luong, D. Hwang, H. H. Nguyen, G. Ghiasi, Y. Chervonyi, I. Seo, J. Kim, G. Bingham, J. Lee, S. Mishra, A. Zhai, C. H. Hu, H. Michalewski, J. Kim, J. Ahn, J. Bae, X. Song, T. H. Trinh, Q. V. Le, and J. Jung. Towards robust mathematical reasoning. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025. URL https://aclanthology.org/2025.emnlp-main.1794/.

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
> MiniMax. https://www.minimax.io/news/minimax-m2, 2025. URL https://www.minimax.io/news/minimax-m2.

> MoonShot. Introducing kimi k2 thinking, 2025. URL https://moonshotai.github.io/Kimi-K2/thinking.html.

> OpenAI. Learning to reason with llms, 2024a. URL https://openai.com/index/learning-to-reason-with-llms/.

> OpenAI. Introducing SWE-bench verified we're releasing a human-validated subset of swe-bench that more, 2024b. URL https://openai.com/index/introducing-swe-bench-verified/.

> OpenAI. Introducing gpt-5, 2025. URL https://openai.com/index/introducing-gpt-5/.

> L. Phan, A. Gatti, Z. Han, N. Li, J. Hu, H. Zhang, C. B. C. Zhang, M. Shaaban, J. Ling, S. Shi, et al. Humanity's last exam.  $\underline{\text{arXiv preprint arXiv:2501.14249, 2025.}}$

> D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. arXiv preprint arXiv:2311.12022, 2023.

> J. Schulman. Approximating KL divergence, 2020. URL http://joschu.net/blog/kl-approx.html.

> Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo. Deepseek-math: Pushing the limits of mathematical reasoning in open language models. CoRR, abs/2402.03300, 2024. doi: 10.48550/ARXIV.2402.03300. URL https://doi.org/10.48550/arXiv.2402.03300.

> Z. Shao, Y. Luo, C. Lu, Z. Ren, J. Hu, T. Ye, Z. Gou, S. Ma, and X. Zhang. Deepseekmath-v2: Towards self-verifiable mathematical reasoning, 2025.

> N. Shazeer. Fast transformer decoding: One write-head is all you need.  $\underline{\text{CoRR}}$, abs/1911.02150, 2019. URL http://arxiv.org/abs/1911.02150.

> A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. pages 5998–6008, 2017. URL https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.

> Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, T. Li, M. Ku, K. Wang, A. Zhuang, R. Fan, X. Yue, and W. Chen. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. CoRR, abs/2406.01574, 2024. URL https://doi.org/10.48550/arXiv.2406.01574.

> J. Wei, Z. Sun, S. Papay, S. McKinney, J. Han, I. Fulford, H. W. Chung, A. T. Passos, W. Fedus, and A. Glaese. Browsecomp: A simple yet challenging benchmark for browsing agents.  $\underline{\text{arXiv preprint arXiv:2504.12516}}$, 2025.

> J. Yang, K. Lieret, C. E. Jimenez, A. Wettig, K. Khandpur, Y. Zhang, B. Hui, O. Press, L. Schmidt, and D. Yang. Swe-smith: Scaling data for software engineering agents, 2025. URL https://arxiv.org/abs/2504.21798.

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

### A. MLA 的 MHA 与 MOA 模式

<div style="text-align: center;"><img src="imgs/img_in_image_box_149_705_586_1015.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">(a) MLA 的 MHA 模式。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_605_697_1037_1017.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">(b) MLA 的 MQA 模式。</div>

<div style="text-align: center;">图 7 | MLA 的 MHA 与 MQA 模式示意图。对于 DeepSeek-V3.1-Terminus，训练和预填充阶段使用 MHA 模式，而解码阶段使用 MQA 模式。</div>

图 7 阐释了 MLA 的两个方面——MHA 与 MQA 模式——以及它们之间的转换。

### B. 冷启动模板

---


<div style="text-align: center;">Table 6 | An example of the reasoning data system prompt. The system prompt requires the model to output the reasoning process in the tag <think></think>.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reasoning System Prompt</td><td style='text-align: center; word-wrap: break-word;'>You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. Please first reason before giving the final answer. The reasoning process enclosed within  $\langle think\rangle$  $\langle/think\rangle$. The final answer is output after the  $\langle/think\rangle$ tag.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>Given a linked list, swap every two adjacent nodes and return its head ...</td></tr><tr><td rowspan="2">Reasoning Response</td><td style='text-align: center; word-wrap: break-word;'>$\langle think\rangle$ ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\langle/think\rangle$ [FINAL ANSWER]</td></tr></table>

<div style="text-align: center;">Table 7 | {TOOL-DESCRIPTIONS} and {TOOLCALL-FORMAT} will be replaced with the specific tools and our designed toolcall format.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Agent</td><td style='text-align: center; word-wrap: break-word;'>Use Python interpreter tool to execute Python code. The code will not be shown to the user. This tool should be used for internal reasoning, but not for code that is intended to be visible to the user (e.g. when creating plots, tables, or files). When you send a message containing Python code to python, it will be executed in a stateful Jupyter notebook environment. Python will respond with the output of the execution or time out after 120.0 seconds.</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>System</td><td style='text-align: center; word-wrap: break-word;'># Tools</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>You have access to the following tools: {TOOL-DESCRIPTIONS} Important: ALWAYS adhere to this exact format for tool use: {TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>Given a linked list, swap every two adjacent nodes and return its head ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Agent Response</td><td style='text-align: center; word-wrap: break-word;'>[MULTI-TURN TOOLCALL] [FINAL ANSWER]</td></tr></table>

<div style="text-align: center;">Table 8 | The model executes tool calls in thinking process.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Reasoning Required Agent System Prompt</td><td style='text-align: center; word-wrap: break-word;'>You are a helpful assistant with access to a Python interpreter. - You may use the Python tool **multiple times** during your reasoning, a.k.a in &lt;think&gt;&lt;/think&gt;, with a maximum of 20 code executions. - Call the Python tool early in your reasoning to aid in solving the task. Continue reasoning and invoking tools as needed until you reach the final answer. Once you have the answer, stop reasoning and present your solution using Markdown and LaTeX. - Do NOT invoke any tools in your presented final solution steps. - To improve efficiency and accuracy, you should prefer code execution over language-based reasoning whenever possible. Keep your reasoning succinct; let the code do the heavy lifting. ## Tools You have access to the following tools: {TOOL-DESCRIPTIONS} Important: ALWAYS adhere to this exact format for tool use: {TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Prompt</td><td style='text-align: center; word-wrap: break-word;'>Given a linked list, swap every two adjacent nodes and return its head ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Agent Response with Thinking</td><td style='text-align: center; word-wrap: break-word;'>&lt;think&gt; [MULTI-TURN Thinking-Then-TOOLCALL] &lt;/think&gt; [FINAL ANSWER]</td></tr></table>
> 表6 | 推理数据系统提示示例。系统提示要求模型在标签 `<think></think>` 中输出推理过程。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>推理系统提示</td><td style='text-align: center; word-wrap: break-word;'>你是一名专业的 Python 程序员。你将收到一个问题（问题说明），并生成一个符合说明且通过所有测试的正确 Python 程序。请在给出最终答案前进行推理。推理过程需包含在 $\langle think\rangle$  $\langle/think\rangle$ 中。最终答案在 $\langle/think\rangle$ 标签后输出。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>给定一个链表，交换每两个相邻节点并返回其头节点...</td></tr><tr><td rowspan="2">推理响应</td><td style='text-align: center; word-wrap: break-word;'>$\langle think\rangle$ ...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\langle/think\rangle$ [最终答案]</td></tr></table>

> 表7 | {TOOL-DESCRIPTIONS} 和 {TOOLCALL-FORMAT} 将被替换为具体的工具和我们设计的工具调用格式。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>智能体</td><td style='text-align: center; word-wrap: break-word;'>使用 Python 解释器工具来执行 Python 代码。代码不会显示给用户。此工具应用于内部推理，而非用于意图向用户展示的代码（例如创建图表、表格或文件时）。当你向 python 发送包含 Python 代码的消息时，它将在有状态的 Jupyter notebook 环境中执行。Python 将响应执行输出，或在 120.0 秒后超时。</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>系统</td><td style='text-align: center; word-wrap: break-word;'># 工具</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>你可以使用以下工具：{TOOL-DESCRIPTIONS} 重要：请务必严格遵守此工具使用格式：{TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>给定一个链表，交换每两个相邻节点并返回其头节点...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>智能体响应</td><td style='text-align: center; word-wrap: break-word;'>[多轮工具调用] [最终答案]</td></tr></table>

> 表8 | 模型在思考过程中执行工具调用。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>需推理的智能体系统提示</td><td style='text-align: center; word-wrap: break-word;'>你是一个拥有 Python 解释器访问权限的助手。- 你可以在推理过程中（即在 &lt;think&gt;&lt;/think&gt; 内）**多次**使用 Python 工具，最多执行 20 次代码。- 在推理早期调用 Python 工具以辅助完成任务。根据需要继续推理和调用工具，直到得出最终答案。一旦获得答案，停止推理并使用 Markdown 和 LaTeX 呈现你的解决方案。- 在呈现的最终解决方案步骤中**不要**调用任何工具。- 为提高效率和准确性，应尽可能优先使用代码执行而非基于语言的推理。保持推理简洁；让代码承担繁重的工作。## 工具你可以使用以下工具：{TOOL-DESCRIPTIONS} 重要：请务必严格遵守此工具使用格式：{TOOLCALL-FORMAT}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>提示</td><td style='text-align: center; word-wrap: break-word;'>给定一个链表，交换每两个相邻节点并返回其头节点...</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>含思考的智能体响应</td><td style='text-align: center; word-wrap: break-word;'>&lt;think&gt; [多轮思考-然后-工具调用] &lt;/think&gt; [最终答案]</td></tr></table>

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
### C. DeepSeek-V3.2 非思考模式智能体评估

> 表 9 | DeepSeek-V3.2 非思考模式与思考模式对比。表中的终端基准分数使用 Claude Code 框架评估。使用 Terminus 框架的 Terminal Bench 2.0 非思考模式得分为 39.3。

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>基准测试 (指标)</td><td style='text-align: center; word-wrap: break-word;'>非思考 思考</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">代码智能体</td><td style='text-align: center; word-wrap: break-word;'>Terminal Bench 2.0 (准确率)</td><td style='text-align: center; word-wrap: break-word;'>37.1</td><td style='text-align: center; word-wrap: break-word;'>46.4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Verified (解决率)</td><td style='text-align: center; word-wrap: break-word;'>72.1</td><td style='text-align: center; word-wrap: break-word;'>73.1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>SWE Multilingual (解决率)</td><td style='text-align: center; word-wrap: break-word;'>68.9</td><td style='text-align: center; word-wrap: break-word;'>70.2</td></tr><tr><td rowspan="4">工具使用</td><td style='text-align: center; word-wrap: break-word;'>$\tau^{2}$-bench (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>77.2</td><td style='text-align: center; word-wrap: break-word;'>80.3</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Universe (成功率)</td><td style='text-align: center; word-wrap: break-word;'>38.6</td><td style='text-align: center; word-wrap: break-word;'>45.9</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCP-Mark (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>26.5</td><td style='text-align: center; word-wrap: break-word;'>38.0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Tool-Decathlon (Pass@1)</td><td style='text-align: center; word-wrap: break-word;'>25.6</td><td style='text-align: center; word-wrap: break-word;'>35.2</td></tr></table>

> 非思考模式的性能略逊于思考模式，但仍具有竞争力。

### D. IOI、ICPC 世界总决赛、IMO 和 CMO 的评估方法

> 对于所有竞赛，模型的最大生成长度设置为 128k。不使用任何工具或互联网访问，测试严格遵守竞赛的时间和提交次数限制。
>
> 对于 IOI 评估，我们根据官方竞赛规则设计提交策略，该规则允许每个问题最多提交 50 次，并根据所有子任务中获得的最高分对每次提交进行评分。具体而言，我们首先为每个问题采样 500 个候选解决方案，然后应用多阶段筛选流程。在初始阶段，我们淘汰了未能通过提供的样例测试用例或超出长度限制的无效提交。随后，我们使用 DeepSeek-V32-Exp 模型来识别并删除模型明确表示无法或拒绝解决问题的样本。从剩余的有效候选方案中，我们选取了 50 个具有最长思考轨迹的样本进行最终提交。
>
> 对于 ICPC 评估，我们采用了相同的筛选方法，但初始样本量较小。我们为每个问题生成 32 个候选解决方案，并应用相同的筛选标准来选择提交。
>
> 在 IMO 和 CMO 任务中，我们采用生成-验证-优化的循环。模型会迭代改进其解决方案，直到获得完美的自我评估或达到最大修订上限，此过程与 Shao 等人（2025）的研究相同。

---


### E. Author List

Research & Engineering: Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu, Bowei Zhang, Chaofan Lin, Chen Dong, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenhao Xu, Chong Ruan*, Damai Dai, Daya Guo, Dejian Yang, Deli Chen, Erhang Li, Fangqi Zhou*, Fangyun Lin, Fucong Dai, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Hao Li, Haofen Liang, Haoran Wei, Haowei Zhang, Haowen Luo, Haozhe Ji, Honghui Ding, Hongxuan Tang, Huanqi Cao, Huazuo Gao, Hui Qu, Hui Zeng, Jialiang Huang, Jiashi Li, Jiaxin Xu, Jiewen Hu, Jingchang Chen, Jingting Xiang, Jingyang Yuan, Jingyuan Cheng, Jinhua Zhu, Jun Ran*, Junguang Jiang, Junjie Qiu, Junlong Li*, Junxiao Song, Kai Dong, Kaige Gao, Kang Guan, Kexin Huang*, Kexing Zhou, Kezhao Huang, Kuai Yu, Lean Wang, Lecong Zhang, Lei Wang, Liang Zhao, Liangsheng Yin*, Lihua Guo, Lingxiao Luo, Linwang Ma, Litong Wang, Liyue Zhang, M.S. Di, M.Y Xu, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingxu Zhou, Panpan Huang, Peixin Cong, Peiyi Wang, Qiancheng Wang, Qihao Zhu, Qingyang Li, Qinyu Chen, Qiushi Du, Ruiling Xu, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runqiu Yin, Runxin Xu, Ruomeng Shen, Ruoyu Zhang, S.H. Liu, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaofei Cai, Shaoyuan Chen, Shengding Hu, Shengyu Liu, Shiqiang Hu, Shirong Ma, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, Songyang Zhou, Tao Ni, Tao Yun, Tian Pei, Tian Ye, Tianyuan Yue, Wangding Zeng, Wen Liu, Wenfeng Liang, Wenjie Pang, Wenjing Luo, Wenjun Gao, Wentao Zhang, Xi Gao, Xiangwen Wang, Xiao Bi, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaokang Zhang, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xingkai Yu, Xingyou Li, Xinyu Yang, Xinyuan Li*, Xu Chen, Xuecheng Su, Xuehai Pan, Xuheng Lin, Xuwei Fu, Y.Q. Wang, Yang Zhang, Yanhong Xu, Yanru Ma, Yao Li, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Qian, Yi Yu, Yichao Zhang, Yifan Ding, Yifan Shi, Yiliang Xiong, Ying He, Ying Zhou, Yinmin Zhong, Yishi Piao, Yisong Wang, Yixiao Chen, Yixuan Tan, Yixuan Wei, Yiyang Ma, Yiyuan Liu, Yonglun Yang, Yongqiang Guo, Yongtong Wu, Yu Wu, Yuan Cheng, Yuan Ou, Yuanfan Xu, Yuduan Wang, Yue Gong*, Yuhan Wu, Yuheng Zou, Yukun Li, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Z.F. Wu, Z.Z. Ren, Zehua Zhao, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhibin Gou, Zhicheng Ma, Zhigang Yan, Zhihong Shao, Zhixian Huang, Zhiyu Wu, Zhuoshu Li, Zhuping Zhang, Zian Xu, Zihao Wang, Zihui Gu, Zijia Zhu, Zilin Li, Zipeng Zhang, Ziwei Xie, Ziyi Gao, Zizheng Pan, Zongqing Yao

Data Annotation: Bei Feng, Hui Li, J.L. Cai, Jiaqi Ni, Lei Xu, Meng Li, Ning Tian, R.J. Chen, R.L. Jin, S.S. Li, Shuang Zhou, Tianyu Sun, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xinnan Song, Xinyi Zhou, Y.X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Zhen Huang, Zhipeng Xu, Zhongyu Zhang

Business & Compliance: Dongjie Ji, Jian Liang, Jianzhong Guo, Jin Chen, Leyi Xia, Miaojun Wang, Mingming Li, Peng Zhang, Ruyi Chen, Shangmian Sun, Shaoqing Wu, Shengfeng Ye, T.Wang, W.L. Xiao, Wei An, Xianzu Wang, Xiaowen Sun, Xiaoxiang Wang, Ying Tang, Yukun Zha, Zekai Zhang, Zhe Ju, Zhen Zhang, Zihua Qu

Authors are listed alphabetically by their first name. Names marked with * denote individuals who have departed from our team.
### E. 作者列表

研究及工程：Aixin Liu、Aoxue Mei、Bangcai Lin、Bing Xue、Bingxuan Wang、Bingzheng Xu、Bochao Wu、Bowei Zhang、Chaofan Lin、Chen Dong、Chengda Lu、Chenggang Zhao、Chengqi Deng、Chenhao Xu、Chong Ruan*、Damai Dai、Daya Guo、Dejian Yang、Deli Chen、Erhang Li、Fangqi Zhou*、Fangyun Lin、Fucong Dai、Guangbo Hao、Guanting Chen、Guowei Li、H. Zhang、Hanwei Xu、Hao Li、Haofen Liang、Haoran Wei、Haowei Zhang、Haowen Luo、Haozhe Ji、Honghui Ding、Hongxuan Tang、Huanqi Cao、Huazuo Gao、Hui Qu、Hui Zeng、Jialiang Huang、Jiashi Li、Jiaxin Xu、Jiewen Hu、Jingchang Chen、Jingting Xiang、Jingyang Yuan、Jingyuan Cheng、Jinhua Zhu、Jun Ran*、Junguang Jiang、Junjie Qiu、Junlong Li*、Junxiao Song、Kai Dong、Kaige Gao、Kang Guan、Kexin Huang*、Kexing Zhou、Kezhao Huang、Kuai Yu、Lean Wang、Lecong Zhang、Lei Wang、Liang Zhao、Liangsheng Yin*、Lihua Guo、Lingxiao Luo、Linwang Ma、Litong Wang、Liyue Zhang、M.S. Di、M.Y Xu、Mingchuan Zhang、Minghua Zhang、Minghui Tang、Mingxu Zhou、Panpan Huang、Peixin Cong、Peiyi Wang、Qiancheng Wang、Qihao Zhu、Qingyang Li、Qinyu Chen、Qiushi Du、Ruiling Xu、Ruiqi Ge、Ruisong Zhang、Ruizhe Pan、Runji Wang、Runqiu Yin、Runxin Xu、Ruomeng Shen、Ruoyu Zhang、S.H. Liu、Shanghao Lu、Shangyan Zhou、Shanhuang Chen、Shaofei Cai、Shaoyuan Chen、Shengding Hu、Shengyu Liu、Shiqiang Hu、Shirong Ma、Shiyu Wang、Shuiping Yu、Shunfeng Zhou、Shuting Pan、Songyang Zhou、Tao Ni、Tao Yun、Tian Pei、Tian Ye、Tianyuan Yue、Wangding Zeng、Wen Liu、Wenfeng Liang、Wenjie Pang、Wenjing Luo、Wenjun Gao、Wentao Zhang、Xi Gao、Xiangwen Wang、Xiao Bi、Xiaodong Liu、Xiaohan Wang、Xiaokang Chen、Xiaokang Zhang、Xiaotao Nie、Xin Cheng、Xin Liu、Xin Xie、Xingchao Liu、Xingkai Yu、Xingyou Li、Xinyu Yang、Xinyuan Li*、Xu Chen、Xuecheng Su、Xuehai Pan、Xuheng Lin、Xuwei Fu、Y.Q. Wang、Yang Zhang、Yanhong Xu、Yanru Ma、Yao Li、Yao Li、Yao Zhao、Yaofeng Sun、Yaohui Wang、Yi Qian、Yi Yu、Yichao Zhang、Yifan Ding、Yifan Shi、Yiliang Xiong、Ying He、Ying Zhou、Yinmin Zhong、Yishi Piao、Yisong Wang、Yixiao Chen、Yixuan Tan、Yixuan Wei、Yiyang Ma、Yiyuan Liu、Yonglun Yang、Yongqiang Guo、Yongtong Wu、Yu Wu、Yuan Cheng、Yuan Ou、Yuanfan Xu、Yuduan Wang、Yue Gong*、Yuhan Wu、Yuheng Zou、Yukun Li、Yunfan Xiong、Yuxiang Luo、Yuxiang You、Yuxuan Liu、Yuyang Zhou、Z.F. Wu、Z.Z. Ren、Zehua Zhao、Zehui Ren、Zhangli Sha、Zhe Fu、Zhean Xu、Zhenda Xie、Zhengyan Zhang、Zhewen Hao、Zhibin Gou、Zhicheng Ma、Zhigang Yan、Zhihong Shao、Zhixian Huang、Zhiyu Wu、Zhuoshu Li、Zhuping Zhang、Zian Xu、Zihao Wang、Zihui Gu、Zijia Zhu、Zilin Li、Zipeng Zhang、Ziwei Xie、Ziyi Gao、Zizheng Pan、Zongqing Yao

> 数据标注：Bei Feng、Hui Li、J.L. Cai、Jiaqi Ni、Lei Xu、Meng Li、Ning Tian、R.J. Chen、R.L. Jin、S.S. Li、Shuang Zhou、Tianyu Sun、X.Q. Li、Xiangyue Jin、Xiaojin Shen、Xiaosha Chen、Xinnan Song、Xinyi Zhou、Y.X. Zhu、Yanping Huang、Yaohui Li、Yi Zheng、Yuchen Zhu、Yunxian Ma、Zhen Huang、Zhipeng Xu、Zhongyu Zhang

> 业务与合规：Dongjie Ji、Jian Liang、Jianzhong Guo、Jin Chen、Leyi Xia、Miaojun Wang、Mingming Li、Peng Zhang、Ruyi Chen、Shangmian Sun、Shaoqing Wu、Shengfeng Ye、T.Wang、W.L. Xiao、Wei An、Xianzu Wang、Xiaowen Sun、Xiaoxiang Wang、Ying Tang、Yukun Zha、Zekai Zhang、Zhe Ju、Zhen Zhang、Zihua Qu

> 作者按名字首字母顺序排列。标有 * 的姓名表示已离开团队的成员。