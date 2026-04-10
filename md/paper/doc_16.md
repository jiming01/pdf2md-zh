<div style="text-align: center;"><img src="imgs/img_in_chart_box_170_177_1019_586.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">Figure 6 | Accuracy of Browsecomp with different test-time compute expansion strategies.</div>


selects the trajectory with the fewest steps.

We evaluate these strategies on the BrowseComp benchmark (Wei et al., 2025). As illustrated in Figure 6, under varying compute budgets, context management leads to significant performance gains by allowing the model to scale up test-time compute, providing more space to perform additional execution steps. For example, Summary extends the average steps from 140 to 364, improving performance from 53.4 to 60.2. However, its overall efficiency is relatively low. Despite its simplicity, Discard-all performs well in both efficiency and scalability, achieving a score of 67.6, comparable to parallel scaling while using significantly fewer steps.

In summary, test-time compute can be scaled either serially through context management or in parallel, both effectively extending the model's problem-solving capacity. However, different strategies exhibit varying efficiency and scalability. Thus, it is crucial to account for actual compute costs when benchmarking model performance. Meanwhile, finding the optimal combination of serial and parallel scaling to maximize both efficiency and scalability remains a crucial direction for future work.

## 5. Conclusion, Limitation, and Future Work

In this work, we introduced DeepSeek-V3.2, a framework that effectively bridges the gap between computational efficiency and advanced reasoning capabilities. Using DSA, we addressed critical computation complexity without sacrificing long-context performance. By increasing computational budget, DeepSeek-V3.2 achieves comparable performance with GPT-5 on reasoning benchmarks. Finally, the integration of our large-scale agentic task synthesis pipeline significantly enhances tool-use proficiency, unlocking new possibilities for robust and generalizable AI agents with open LLM. Furthermore, our high-compute variant, DeepSeek-V3.2-Speciale, validated by gold-medal achievements in the IMO and IOI, sets a milestone for open LLMs.

Despite these achievements, we acknowledge certain limitations when compared to frontier closed-source models such as Gemini-3.0-Pro. First, due to fewer total training FLOPs, the breadth of world knowledge in DeepSeek-V3.2 still lags behind that of leading proprietary
<div style="text-align: center;"><img src="imgs/img_in_chart_box_170_177_1019_586.jpg" alt="Image" width="71%" /></div>


<div style="text-align: center;">图6 | 采用不同测试时计算扩展策略时Browsecomp的准确率。</div>


> 选择步骤最少的轨迹。
> 
> 我们在BrowseComp基准测试（Wei等人，2025）上评估了这些策略。如图6所示，在不同的计算预算下，上下文管理通过允许模型扩展测试时计算，为执行额外的步骤提供了更多空间，从而带来了显著的性能提升。例如，Summary策略将平均步数从140步扩展到364步，使性能从53.4提升至60.2。然而，其整体效率相对较低。尽管Discard-all策略简单，但在效率和可扩展性方面都表现良好，达到了67.6分，与并行扩展的成绩相当，同时使用的步数显著更少。
> 
> 总而言之，测试时计算可以通过上下文管理进行串行扩展，也可以进行并行扩展，两者都能有效扩展模型的问题解决能力。然而，不同的策略在效率和可扩展性方面表现各异。因此，在对模型性能进行基准测试时，考虑实际的计算成本至关重要。同时，寻找串行和并行扩展的最佳组合，以最大限度地提高效率和可扩展性，仍然是未来工作的关键方向。

## 5. 结论、局限性与未来工作

> 在这项工作中，我们介绍了DeepSeek-V3.2，这是一个有效弥合计算效率与高级推理能力之间差距的框架。通过使用DSA，我们在不牺牲长上下文性能的前提下，解决了关键的计算复杂度问题。通过增加计算预算，DeepSeek-V3.2在推理基准测试中达到了与GPT-5相当的性能。最后，我们大规模智能体任务合成流程的集成显著提升了工具使用能力，为基于开源大语言模型构建稳健且可泛化的AI智能体开辟了新的可能性。此外，我们的高计算变体DeepSeek-V3.2-Speciale，凭借在国际数学奥林匹克竞赛（IMO）和国际信息学奥林匹克竞赛（IOI）中取得的金牌成就得到验证，为开源大语言模型树立了一个里程碑。
> 
> 尽管取得了这些成就，我们承认与前沿闭源模型（如Gemini-3.0-Pro）相比仍存在某些局限性。首先，由于总训练FLOPs较少，DeepSeek-V3.2所具备的世界知识的广度仍然落后于领先的专有模型。