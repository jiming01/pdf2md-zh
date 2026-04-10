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

> 预训练的 DeepSeek-V3.2 基础检查点。除了写作任务和通用问答，我们的框架还涵盖了六个专业领域：数学、编程、通用逻辑推理、通用智能体任务、智能体编码和智能体搜索，所有领域均支持思维模式和非思维模式。每个专家模型都通过大规模强化学习（RL）计算进行训练。此外，我们采用不同的模型来生成长链思维推理（思维模式）和直接响应生成（非思维模式）的训练数据。一旦专家模型准备就绪，它们便用于生成最终检查点所需的领域特定数据。实验结果表明，在蒸馏数据上训练的模型，其性能水平仅略低于领域特定的专家模型，而通过后续的 RL 训练，这一性能差距得以有效消除。
>
> **混合 RL 训练** 对于 DeepSeek-V3.2，我们仍然采用组相对策略优化（GRPO）（DeepSeek-AI, 2025; Shao et al., 2024）作为 RL 训练算法。与 DeepSeek-V3.2-Exp 类似，我们将推理、智能体和人类对齐训练合并到一个 RL 阶段。这种方法有效地平衡了不同领域的性能，同时规避了多阶段训练范式常伴随的灾难性遗忘问题。对于推理和智能体任务，我们采用基于规则的结果奖励、长度惩罚和语言一致性奖励。对于通用任务，我们采用生成式奖励模型，其中每个提示都有其自身的评估标准。
>
> **DeepSeek-V3.2 与 DeepSeek-V3.2-Speciale** DeepSeek-V3.2 整合了从专家模型蒸馏而来的推理、智能体和人类对齐数据，并经过数千步的持续 RL 训练以达到最终检查点。为了探究扩展思维的潜力，我们还开发了一个实验变体 DeepSeek-V3.2-Speciale。该模型专门在 RL 训练期间使用降低的长度惩罚，针对推理数据进行训练。此外，我们整合了来自 DeepSeekMath-V2（Shao et al., 2025）的数据集和奖励方法，以增强数学证明能力。
>
> 我们希望强调我们在 3.1 节中关于如何创建稳定方案以扩展 RL 计算，以及在 3.2 节中关于如何将思维整合到智能体任务中的努力。