### 3.1. Scaling GRPO

We first review the objective of GRPO. GRPO optimizes the policy model  $ \pi_\theta $ by maximizing the following objective on a group of responses  $ \{o_1, \cdots, o_G\} $ sampled from the old policy  $ \pi_{\text{old}} $ given each question  $ q $:

 $$ \begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\ \left.\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*} $$ 

where

 $$ r_{i,t}(\theta)=\frac{\pi_{\theta}(o_{i,t}|q,o_{i,<t})}{\pi_{\mathrm{o l d}}(o_{i,t}|q,o_{i,<t})} $$ 

is the importance sampling ratio between the current and old policy.  $ \varepsilon $ and  $ \beta $ are hyperparameters controlling the clipping range and KL penalty strength, respectively.  $ \hat{A}_{i,t} $ is the advantage of  $ o_{i,t} $ which is estimated by normalizing the outcome reward within each group. Specifically, a set of reward models are used to score an outcome reward  $ R_i $ for each output  $ o_i $ in the group, yielding  $ G $ rewards  $ \boldsymbol{R} = \{R_1, \cdots, R_G\} $ respectively. The advantage of  $ o_{i,t} $ is calculated by subtracting the average reward of the group from the reward of output  $ o_i $, i.e.,  $ \hat{A}_{i,t} = R_i - \text{mean}(\boldsymbol{R}) $.

In the following, we outline additional strategies that stabilize RL scaling, directly building on the GRPO algorithm.

Unbiased KL Estimate Given  $ o_{i,t} $ is sampled from the old policy  $ \pi_{\text{old}}(\cdot|q,o_{i,\text{st}}) $, we correct the K3 estimator (Schulman, 2020) to obtain an unbiased KL estimate using the importance-sampling ratio between the current policy  $ \pi_{\theta} $ and the old policy  $ \pi_{\text{old}} $.

 $$ \mathbb{D}_{\mathrm{K L}}\big(\pi_{\theta}(o_{i,t})\big\|\pi_{\mathrm{r e f}}(o_{i,t})\big)=\frac{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\mathrm{o l d}}\big(o_{i,t}|q,o_{i,<t}\big)}\left(\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-\log\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-1\right). $$ 

As a direct result of this adjustment, the gradient of this KL estimator becomes unbiased, which eliminates systematic estimation errors, thereby facilitating stable convergence. This contrasts sharply with the original K3 estimator, particularly when the sampled tokens have substantially lower probabilities under the current policy than the reference policy, i.e.,  $ \pi_{\theta} \ll \pi_{ref} $. In such cases, the gradient of the K3 estimator assigns disproportionately large, unbounded weights to maximize the likelihood of these tokens, resulting in noisy gradient updates that accumulate to degrade sample quality in subsequent iterations and lead to unstable training dynamics. In practice, we find that different domains benefit from varying strengths of KL regularization. For certain domains, such as mathematics, applying a relatively weak KL penalty or even omitting it entirely can yield improved performance.

Off-Policy Sequence Masking To improve the efficiency of RL systems, we typically generate a large batch of rollout data, which is subsequently split into multiple mini-batches for several gradient update steps. This practice inherently introduces off-policy behavior. Additionally, inference frameworks used for efficient data generation are often highly optimized, which may differ in implementation details from training frameworks. Such training-inference inconsistency
### 3.1. 扩展 GRPO

我们首先回顾 GRPO 的目标。GRPO 通过最大化以下目标来优化策略模型 $ \pi_\theta $，该目标基于从旧策略 $ \pi_{\text{old}} $ 中为每个问题 $ q $ 采样得到的一组响应 $ \{o_1, \cdots, o_G\} $：

$$ \begin{align*}\mathcal{J}_{\mathrm{GRPO}}(\theta)=\mathbb{E}_{q\sim P(Q),\{o_{i}\}_{i=1}^{G}\sim\pi_{\mathrm{old}}(\cdot|q)}\left[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\right.\\ \left.\min\left(r_{i,t}(\theta)\hat{A}_{i,t},\mathrm{clip}\left(r_{i,t}(\theta),1-\varepsilon,1+\varepsilon\right)\hat{A}_{i,t}\right)-\beta\mathbb{D}_{\mathrm{KL}}\left(\pi_{\theta}(o_{i,t})\left\|\pi_{\mathrm{ref}}(o_{i,t})\right.\right)\right],\end{align*} $$ 

其中

$$ r_{i,t}(\theta)=\frac{\pi_{\theta}(o_{i,t}|q,o_{i,<t})}{\pi_{\mathrm{o l d}}(o_{i,t}|q,o_{i,<t})} $$ 

是当前策略与旧策略之间的重要性采样比率。$ \varepsilon $ 和 $ \beta $ 是超参数，分别控制裁剪范围和 KL 惩罚强度。$ \hat{A}_{i,t} $ 是 $ o_{i,t} $ 的优势函数，通过组内结果奖励的归一化来估计。具体来说，使用一组奖励模型对组中每个输出 $ o_i $ 评分，得到一个结果奖励 $ R_i $，从而分别得到 $ G $ 个奖励 $ \boldsymbol{R} = \{R_1, \cdots, R_G\} $。$ o_{i,t} $ 的优势函数通过从输出 $ o_i $ 的奖励中减去该组的平均奖励来计算，即 $ \hat{A}_{i,t} = R_i - \text{mean}(\boldsymbol{R}) $。

接下来，我们将概述在 GRPO 算法基础上直接构建的、用于稳定 RL 扩展的额外策略。

**无偏 KL 估计** 给定 $ o_{i,t} $ 是从旧策略 $ \pi_{\text{old}}(\cdot|q,o_{i,\text{st}}) $ 中采样的，我们修正 K3 估计器 (Schulman, 2020)，利用当前策略 $ \pi_{\theta} $ 与旧策略 $ \pi_{\text{old}} $ 之间的重要性采样比率，得到一个无偏的 KL 估计。

$$ \mathbb{D}_{\mathrm{K L}}\big(\pi_{\theta}(o_{i,t})\big\|\pi_{\mathrm{r e f}}(o_{i,t})\big)=\frac{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\mathrm{o l d}}\big(o_{i,t}|q,o_{i,<t}\big)}\left(\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-\log\frac{\pi_{\mathrm{r e f}}\big(o_{i,t}|q,o_{i,<t}\big)}{\pi_{\theta}\big(o_{i,t}|q,o_{i,<t}\big)}-1\right). $$ 

作为此调整的直接结果，该 KL 估计器的梯度变为无偏，从而消除了系统估计误差，有助于稳定收敛。这与原始的 K3 估计器形成鲜明对比，尤其是在采样出的词元在当前策略下的概率远低于参考策略时，即 $ \pi_{\theta} \ll \pi_{ref} $。在这种情况下，K3 估计器的梯度会分配不成比例的巨大、无界权重来最大化这些词元的似然，导致梯度更新噪声过大，这些噪声累积起来会降低后续迭代中的样本质量，并导致训练动态不稳定。在实践中，我们发现不同领域受益于不同强度的 KL 正则化。对于某些领域，例如数学，应用相对较弱的 KL 惩罚甚至完全省略它，可能会带来更好的性能。

**离策略序列掩码** 为了提高 RL 系统的效率，我们通常会生成大批量的 rollout 数据，随后将其分割成多个小批量用于多步梯度更新。这种做法本质上引入了离策略行为。此外，用于高效数据生成的推理框架通常是高度优化的，其实现细节可能与训练框架不同。这种训练与推理的不一致性