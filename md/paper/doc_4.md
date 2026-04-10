### 2.2. Parity Evaluation

Standard Benchmark In September 2025, we evaluate DeepSeek-V3.2-Exp on a suite of benchmarks, which focus on diverse capabilities, and compare it with DeepSeek-V3.1-Terminus showing similar performance. While DeepSeek V3.2 Exp significantly improves computational efficiency on long sequences, we do not observe substantial performance degradation compared with DeepSeek-V3.1-Terminus, on both short- and long-context tasks.

Human Preference Given that direct human preference assessments are inherently susceptible to bias, we employ ChatbotArena as an indirect evaluation framework to approximate user preferences for the newly developed base models. Both DeepSeek-V3.1-Terminus and DeepSeek-V3.2-Exp share an identical post-training strategy, and their Elo scores, obtained from evaluations conducted on 10 November 2025, are closely matched. These results suggest that the new base model achieves performance on par with the previous iteration, despite incorporating a sparse attention mechanism.

Long Context Eval Following the release of DeepSeek-V3.2-Exp, several independent long-context evaluations were conducted using previously unseen test sets. A representative benchmark is AA-LCR $ ^{3} $, in which DeepSeek-V3.2-Exp scores four points higher than DeepSeek-V3.1-Terminus in reasoning mode. In the Fiction.liveBench evaluation $ ^{4} $, DeepSeek-V3.2-Exp consistently outperforms DeepSeek-V3.1-Terminus across multiple metrics. This evidence indicates the base checkpoint of DeepSeek-V3.2-Exp does not regress on long context tasks.

### 2.3. Inference Costs

DSA reduces the core attention complexity of the main model from  $ O(L^{2}) $ to  $ O(Lk) $, where  $ k \ll L $ is the number of selected tokens. Although the lightning indexer still has a complexity of  $ O(L^{2}) $, it requires much less computation compared with MLA in DeepSeek-V3.1-Terminus. Combined with our optimized implementation, DSA achieves a significant end-to-end speedup in long-context scenarios. Figure 3 presents how token costs of DeepSeek-V3.1-Terminus and DeepSeek-V3.2 vary with the token position in the sequence. These costs are estimated from benchmarking the actual service deployed on H800 GPUs, at a rental price of 2 USD per GPU hour. Note that for short-sequence prefilling, we specially implement a masked MHA mode to simulate DSA, which can achieve higher efficiency under short-context conditions.

## 3. Post-Training

After continued pre-training, we perform post-training to create the final DeepSeek-V3.2. The post-training of DeepSeek-V3.2 also employs sparse attention in the same way as the sparse continued pre-training stage. For DeepSeek-V3.2, we maintain the same post-training pipeline as in DeepSeek-V3.2-Exp, which includes specialist distillation and mixed RL training.

Specialist Distillation For each task, we initially develop a specialized model dedicated exclusively to that particular domain, with all specialist models being fine-tuned from the same
### 2.2. 性能对等评估

标准基准测试 2025年9月，我们在涵盖多样能力的一系列基准测试上评估了DeepSeek-V3.2-Exp，并将其与DeepSeek-V3.1-Terminus进行对比，结果显示两者性能相近。尽管DeepSeek-V3.2-Exp在长序列上的计算效率显著提升，但在短上下文和长上下文任务中，我们均未观察到其相比DeepSeek-V3.1-Terminus出现明显的性能下降。

人类偏好评估 鉴于直接的人类偏好评估本质上易受偏见影响，我们采用ChatbotArena作为间接评估框架，以近似衡量用户对新开发的基础模型的偏好。DeepSeek-V3.1-Terminus和DeepSeek-V3.2-Exp采用完全相同的后训练策略，并且它们在2025年11月10日评估中获得的Elo分数非常接近。这些结果表明，尽管引入了稀疏注意力机制，新的基础模型达到了与前一版本相当的性能水平。

长上下文评估 在DeepSeek-V3.2-Exp发布后，多个独立研究使用先前未见过的测试集对其进行了长上下文评估。一个代表性基准是AA-LCR$^{3}$，其中DeepSeek-V3.2-Exp在推理模式下的得分比DeepSeek-V3.1-Terminus高出四分。在Fiction.liveBench评估$^{4}$中，DeepSeek-V3.2-Exp在多项指标上持续优于DeepSeek-V3.1-Terminus。这些证据表明，DeepSeek-V3.2-Exp的基础检查点在长上下文任务上没有出现性能倒退。

### 2.3. 推理成本

DSA将主模型的核心注意力复杂度从$O(L^{2})$降低到$O(Lk)$，其中$k \ll L$是所选令牌的数量。尽管闪电索引器的复杂度仍为$O(L^{2})$，但其所需计算量远少于DeepSeek-V3.1-Terminus中的MLA。结合我们优化的实现，DSA在长上下文场景中实现了显著的端到端加速。图3展示了DeepSeek-V3.1-Terminus和DeepSeek-V3.2的令牌成本如何随序列中令牌位置的变化而变化。这些成本基于部署在H800 GPU上的实际服务基准测试估算得出，GPU租赁价格为每小时2美元。需要注意的是，对于短序列预填充，我们专门实现了掩码MHA模式来模拟DSA，该模式在短上下文条件下能达到更高的效率。

## 3. 后训练

在持续预训练之后，我们执行后训练以创建最终的DeepSeek-V3.2。DeepSeek-V3.2的后训练同样采用稀疏注意力，方式与稀疏持续预训练阶段相同。对于DeepSeek-V3.2，我们保持了与DeepSeek-V3.2-Exp相同的后训练流程，包括专家蒸馏和混合强化学习训练。

专家蒸馏 针对每项任务，我们首先开发一个专门服务于该特定领域的专用模型，所有专家模型均基于同一个