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

DeepSeek-R1 已证明，融入思考过程能显著提升模型解决复杂问题的能力。基于此洞见，我们旨在将思考能力整合到工具调用场景中。

我们观察到，复制 DeepSeek-R1 的策略——在第二轮消息到达时丢弃推理内容——会导致显著的 Token 效率低下。这种方法迫使模型在每次后续工具调用时，都需要对整个问题进行冗余的重新推理。为了缓解这个问题，我们开发了一种严格为工具调用场景定制的上下文管理机制，如图 4 所示：

- 仅当对话中引入新的用户消息时，历史推理内容才会被丢弃。如果仅追加与工具相关的消息（例如，工具输出），则推理内容将在整个交互过程中保留。

- 当推理痕迹被移除时，工具调用的历史及其结果仍会保留在上下文中。

值得注意的是，某些智能体框架，如 Roo Code 或 Terminus，通过用户消息来模拟工具交互。由于上述上下文管理规则，这些框架可能无法充分利用我们增强的推理持久性优势。因此，我们建议在此类架构中使用非思考模型以获得最佳性能。

<div style="text-align: center;"><img src="imgs/img_in_image_box_172_819_1012_1253.jpg" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 4 | 工具调用场景中的思考保留机制。</div>


#### 3.2.2. 冷启动

鉴于可获得推理数据（非智能体）和非推理的智能体数据，整合这两种能力的一个直接策略是通过精心设计的提示。我们认为模型具备足够的能力来准确遵循明确的指令，从而能够在推理过程中无缝地融入工具执行。