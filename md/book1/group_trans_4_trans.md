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

<div style="text-align: center;"><img src="imgs/img_in_chart_box_354_160_788_464.jpg" alt="图像" width="37%" /></div>


<div style="text-align: center;">图 5.1：在输入空间的某些区域，当类别后验不确定时，我们可能更倾向于不选择类别 1 或 2，而选择拒绝选项。改编自 [Bis06] 的图 1.26。</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td colspan="2">估计</td><td rowspan="2">行和</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td rowspan="2">真实</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>TN</td><td style='text-align: center; word-wrap: break-word;'>FP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>FN</td><td style='text-align: center; word-wrap: break-word;'>TP</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>列和</td><td style='text-align: center; word-wrap: break-word;'>$ \hat{N} $</td><td style='text-align: center; word-wrap: break-word;'>$ \hat{P} $</td><td style='text-align: center; word-wrap: break-word;'></td></tr></table>

<div style="text-align: center;">表 5.3：二分类问题的类别混淆矩阵。TP 是真阳性数，FP 是假阳性数，TN 是真阴性数，FN 是假阴性数，P 是真正的正例数，P 是预测的正例数，N 是真正的负例数，$ \hat{N} $ 是预测的负例数。</div>


该系统击败了 Jeopardy 智力竞赛的人类冠军。沃森使用了多种有趣的技巧 [Fer+10]，但与我们当前讨论最相关的是，它包含一个模块，用于估计对其答案的置信度。系统只有在足够确信答案正确时才会选择“抢答”。

关于其他方法和应用，可参见例如 [RTA18; GEY19; Nar+23]。

#### 5.1.3 ROC 曲线

在 5.1.2.2 节中，我们展示了可以通过使用来自假阳性和假阴性相对成本的阈值 $\tau$ 对概率进行阈值化，从而在二分类问题中选择最优标签。我们可以考虑使用一组不同的阈值，并比较由此产生的性能，而不是选择单个阈值，如下文所述。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_240_115_930_216.jpg" alt="图像" width="59%" /></div>


<div style="text-align: center;">表 5.4：二元分类问题的类别混淆矩阵，按行归一化以得到 $ p(\hat{y}|y) $。缩写：$ TNR = true $ 负率，$ Spec = specificity $ 特异度，$ FPR = false $ 正率，$ FNR = false $ 负率，$ Miss = miss $ 率，$ TPR = true $ 正率，$ Sens = sensitivity $ 灵敏度。注意 $ FNR=1-TPR $ 且 $ FPR=1-TNR $。</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td colspan="2"></td><td colspan="2">估计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td rowspan="2">真实</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>$ TN/\hat{N}=NPV $</td><td style='text-align: center; word-wrap: break-word;'>$ FP/\hat{P}=FDR $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>$ FN/\hat{N}=FOR $</td><td style='text-align: center; word-wrap: break-word;'>$ TP/\hat{P}=Prec=PPV $</td></tr></table>

<div style="text-align: center;">表 5.5：二元分类问题的类别混淆矩阵，按列归一化以得到 $ p(y|\hat{y}) $。缩写：NPV = 阴性预测值，FDR = 错误发现率，FOR = 错误遗漏率，PPV = 阳性预测值，Prec = 精确率。注意 FOR=1-NPV 且 FDR=1-PPV。</div>


##### 5.1.3.1 类别混淆矩阵

对于任意固定的阈值 $ \tau $，我们考虑以下决策规则：

$$  \hat{y}_{\tau}(\boldsymbol{x})=\mathbb{I}\left(p(y=1|\boldsymbol{x})\geq1-\tau\right)   \tag*{(5.16)}$$

我们可以按如下方式计算在 N 个带标签样本上使用该策略所产生的假正例（FP）的经验数量：

$$  F P_{\tau}=\sum_{n=1}^{N}\mathbb{I}\left(\hat{y}_{\tau}(\boldsymbol{x}_{n})=1,y_{n}=0\right)   \tag*{(5.17)}$$

类似地，我们可以计算假负例（FN）、真正例（TP）和真负例（TN）的经验数量。我们可以将这些结果存储在一个 $ 2 \times 2 $ 类别混淆矩阵 $ C $ 中，其中 $ C_{ij} $ 是真实类别标签为 i 的样本被（错误）分类为标签 j 的次数。在二元分类问题中，得到的矩阵如表 5.3 所示。

由此表，我们可以计算 $ p(\hat{y}|y) $ 或 $ p(y|\hat{y}) $，具体取决于我们是按行还是按列进行归一化。我们可以从这些分布中推导出各种汇总统计量，如表 5.4 和表 5.5 所示。例如，真正率（TPR），也称为灵敏度、召回率或命中率，定义为

$$  T P R_{\tau}=p(\hat{y}=1|y=1,\tau)=\frac{T P_{\tau}}{T P_{\tau}+F N_{\tau}}   \tag*{(5.18)}$$

而假正率（FPR），也称为虚警率或 I 类错误率，定义为

$$  F P R_{\tau}=p(\hat{y}=1|y=0,\tau)=\frac{F P_{\tau}}{F P_{\tau}+T N_{\tau}}   \tag*{(5.19)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_243_140_501_336.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_651_140_913_337.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图5.2: (a) 两个假设分类系统的ROC曲线。系统A的红色曲线优于系统B的蓝色曲线。我们绘制了随着阈值 $\tau$ 变化，真正率(TPR)与假正率(FPR)的关系。还通过红点和蓝点标出了等错误率(EER)，并用阴影区域表示分类器B的曲线下面积(AUC)。由roc_plot.ipynb生成。(b) 两个假设分类系统的精确率-召回率曲线。系统A的红色曲线优于系统B的蓝色曲线。由pr_plot.ipynb生成。</div>

现在我们可以绘制TPR对FPR作为 $\tau$ 的隐函数曲线。这被称为接收者操作特征曲线，即ROC曲线。示例见Figure 5.2(a)。

##### 5.1.3.2 用标量汇总ROC曲线

ROC曲线的质量通常使用曲线下面积AUC作为一个单一数值来汇总。AUC分数越高越好；最大值显然是1。另一个常用的汇总统计量是等错误率EER，也称为交叉率，定义为满足FPR = FNR的值。由于FNR = 1 - TPR，我们可以通过从左上角到右下角画一条线，观察它与ROC曲线的交点来计算出EER（见Figure 5.2(a)中的点A和点B）。EER分数越低越好；最小值显然是0（对应左上角）。

##### 5.1.3.3 类别不平衡

在某些问题中，存在严重的类别不平衡。例如，在信息检索中，负类（无关项）的集合通常远大于正类（相关项）的集合。ROC曲线不受类别不平衡的影响，因为TPR和FPR分别是正类和负类内的比例。然而，在这种情况下，ROC曲线的实用性可能会降低，因为假正例绝对数量的大幅变化不会对假正率产生很大影响，因为FPR除以了FP+TN（参见例如[SR15]的讨论）。因此，所有的“动作”都发生在曲线的极端左侧部分。在这种情况下，我们可能选择使用其他方式来汇总混淆矩阵，例如精确率-召回率曲线，我们将在5.1.4节讨论。

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 5.1.4 精确率-召回率曲线

在某些问题中，“负例”的概念并不明确。例如，考虑图像中的目标检测：如果检测器通过分类图像块来工作，那么被检测的图像块数量——进而真负例的数量——是算法的参数，而非问题定义的一部分。类似地，信息检索系统通常可以自行选择候选项目的初始集合，然后对这些项目进行相关性排序；通过设定一个截断阈值，我们可以将其划分为正例集和负例集，但请注意，负例集的大小取决于检索到的项目总数，而这又是一个算法参数，并非问题规范的一部分。

在这类情况下，我们可能会选择使用**精确率-召回率曲线**来总结系统的性能，具体解释如下。（关于ROC曲线与PR曲线之间关系的更详细讨论，可参见[DG06]。）

##### 5.1.4.1 计算精确率和召回率

关键思想是用一个仅基于正例计算的量来替代假正例率，即**精确率**：

$$  \mathcal{P}(\tau)\triangleq p(y=1|\hat{y}=1,\tau)=\frac{T P_{\tau}}{T P_{\tau}+F P_{\tau}}   \tag*{(5.20)}$$

精确率衡量了我们检测到的样本中真正为正例的比例。我们可以将其与**召回率**（与真正例率相同）进行比较，召回率衡量了我们实际检测到的正例占所有正例的比例：

$$  \mathcal{R}(\tau)\triangleq p(\hat{y}=1|y=1,\tau)=\frac{T P_{\tau}}{T P_{\tau}+F N_{\tau}}   \tag*{(5.21)}$$

如果 $\hat{y}_n \in \{0,1\}$ 是预测标签，而 $y_n \in \{0,1\}$ 是真实标签，我们可以通过以下公式估计精确率和召回率：

$$  \mathcal{P}(\tau)=\frac{\sum_{n}y_{n}\hat{y}_{n}}{\sum_{n}\hat{y}_{n}}   \tag*{(5.22)}$$

$$  \mathcal{R}(\tau)=\frac{\sum_{n}y_{n}\hat{y}_{n}}{\sum_{n}y_{n}}   \tag*{(5.23)}$$

现在，我们可以通过改变阈值 $\tau$ 来绘制精确率随召回率变化的曲线。参见图5.2(b)。曲线越靠近右上角，说明性能越好。

##### 5.1.4.2 将PR曲线总结为标量

PR曲线可以通过多种方式总结为一个单一的数值。首先，我们可以引用在固定召回率水平上的精确率，例如前 $K=10$ 个被召回实体的精确率。这称为**前K个精确率**得分。或者，我们可以计算PR曲线下的面积。然而，精确率可能不会随召回率的增加而单调下降。例如，假设一个分类器在10%召回率时有90%的精确率，而在20%召回率时有96%的精确率。在这种情况下，我们不应测量在10%召回率处的精确率，而应测量在至少达到10%召回率时所能达到的最大精确率（即96%）。这被称为**插值精确率**。

---

精确率。插值精确率的平均值称为平均精确率（Average Precision, AP）；它等于插值PR曲线下的面积，但可能不等于原始PR曲线下的面积。$ ^{1} $ 平均精确率的均值（mean average precision, mAP）是对一组不同PR曲线计算AP后的平均值。

##### 5.1.4.3 F分数

对于固定阈值（对应于PR曲线上单一点），我们可以计算单一的精确率和召回率值，分别记为$ \mathcal{P} $和$ \mathcal{R} $。这两个值常被合并为一个称为$ F_{\beta} $的统计量，定义如下：$ ^{2} $

$$  \frac{1}{F_{\beta}}=\frac{1}{1+\beta^{2}}\frac{1}{\mathcal{P}}+\frac{\beta^{2}}{1+\beta^{2}}\frac{1}{\mathcal{R}}   \tag*{(5.24)}$$

或者等价地

$$  F_{\beta}\triangleq(1+\beta^{2})\frac{\mathcal{P}\cdot\mathcal{R}}{\beta^{2}\mathcal{P}+\mathcal{R}}=\frac{(1+\beta^{2})T P}{(1+\beta^{2})T P+\beta^{2}F N+F P}   \tag*{(5.25)}$$

若设$ \beta = 1 $，则得到精确率和召回率的调和平均数：

$$  \frac{1}{F_{1}}=\frac{1}{2}\left(\frac{1}{\mathcal{P}}+\frac{1}{\mathcal{R}}\right)   \tag*{(5.26)}$$

$$  F_{1}=\frac{2}{1/\mathcal{R}+1/\mathcal{P}}=2\frac{\mathcal{P}\cdot\mathcal{R}}{\mathcal{P}+\mathcal{R}}=\frac{T P}{T P+\frac{1}{2}(F P+F N)}   \tag*{(5.27)}$$

为了理解为何使用调和平均数而非算术平均数$ (\mathcal{P} + \mathcal{R})/2 $，考虑以下场景：假设我们召回所有条目，即对所有$ n $有$ \hat{y}_n = 1 $，且$ \mathcal{R} = 1 $。此时精确率$ \mathcal{P} $将等于**先验概率（prevalence）**$ p(y = 1) = \frac{\sum_n I(y_n = 1)}{N} $。假设先验概率很低，比如$ p(y = 1) = 10^{-4} $。那么$ \mathcal{P} $和$ \mathcal{R} $的算术平均数为$ (\mathcal{P} + \mathcal{R})/2 = (10^{-4} + 1)/2 \approx 50\% $。相比之下，该策略的调和平均数仅为$ \frac{2 \times 10^{-4} \times 1}{1 + 10^{-4}} \approx 0.02\% $。一般而言，调和平均数更为保守，要求精确率和召回率都较高。

使用$ F_{1} $分数时，精确率和召回率被同等加权。然而，如果召回率更重要，可使用$ \beta = 2 $；如果精确率更重要，可使用$ \beta = 0.5 $。

##### 5.1.4.4 类别不平衡

如[Wil20]所述，ROC曲线对类别不均衡不敏感，但PR曲线则不然。为说明这一点，设数据集中正样本比例为$ \pi = P/(P + N) $，并定义比率$ r = P/N = \pi/(1 - \pi) $。令$ n = P + N $为总体规模。ROC曲线不受$ r $变化的影响，因为TPR定义为正样本内部的比率，而FPR定义为负样本内部的比率。这意味着将哪个类别定义为正类、哪个定义为负类并不重要。

现在考虑PR曲线。精确率可写为：

$$  \mathrm{Prec}=\frac{TP}{TP+FP}=\frac{P\cdot TPR}{P\cdot TPR+N\cdot FPR}=\frac{TPR}{TPR+\frac{1}{r}FPR}   \tag*{(5.28)}$$

---

因此，当 $\pi \to 1$ 且 $r \to \infty$ 时，精确率 $\to 1$；当 $\pi \to 0$ 且 $r \to 0$ 时，精确率 $\to 0$。例如，若我们从 $r = 0.5$ 的平衡问题变为 $r = 0.1$（即正例更罕见）的不平衡问题，则每个阈值下的精确率会下降，召回率（即真正例率）保持不变，因此整体PR曲线会降低。因此，如果多个二分类问题具有不同的先验概率（例如，常见或罕见物体的目标检测），在平均它们的精确率时应格外小心 [HCD12]。

F分数同样受到类别不平衡的影响。为说明这一点，我们可将F分数重写如下：

$$  \begin{aligned}\frac{1}{F_{\beta}}&=\frac{1}{1+\beta^{2}}\frac{1}{\mathcal{P}}+\frac{\beta^{2}}{1+\beta^{2}}\frac{1}{\mathcal{R}}\\&=\frac{1}{1+\beta^{2}}\frac{TPR+\frac{N}{P}FPR}{TPR}+\frac{\beta^{2}}{1+\beta^{2}}\frac{1}{TPR}\end{aligned}   \tag*{(5.30)}$$

$$  F_{\beta}=\frac{(1+\beta^{2})TPR}{TPR+\frac{1}{r}FPR+\beta^{2}}   \tag*{(5.31)}$$

#### 5.1.5 回归问题

到目前为止，我们讨论了动作 $A$ 和自然状态 $H$ 为有限集合的情形。在本节中，我们考虑动作集合和状态集合均为实直线的情形，即 $\mathcal{A} = \mathcal{H} = \mathbb{R}$。我们将针对此情形指定几种常用的损失函数（通过逐元素计算损失，可将其推广到 $\mathbb{R}^D$ 空间）。由此得到的决策规则可用于计算估计器应返回的最优参数，或机器人应执行的最优动作等。

##### 5.1.5.1 L2损失

连续状态和动作最常用的损失是 $\ell_{2}$ 损失，也称为平方误差或二次损失，定义如下：

$$  \ell_{2}(h,a)=(h-a)^{2}   \tag*{(5.32)}$$

此时，风险为：

$$  \rho(a|\boldsymbol{x})=\mathbb{E}\left[(h-a)^{2}|\boldsymbol{x}\right]=\mathbb{E}\left[h^{2}|\boldsymbol{x}\right]-2a\mathbb{E}\left[h|\boldsymbol{x}\right]+a^{2}   \tag*{(5.33)}$$

最优动作必须满足该点处风险导数为零的条件（如第8章所述）。因此，最优动作是选择后验均值：

$$  \frac{\partial}{\partial a}\rho(a|\boldsymbol{x})=-2\mathbb{E}\left[h|\boldsymbol{x}\right]+2a=0\Rightarrow\pi(\boldsymbol{x})=\mathbb{E}\left[h|\boldsymbol{x}\right]=\int h p(h|\boldsymbol{x})d h   \tag*{(5.34)}$$

这通常称为最小均方误差估计（MMSE估计）。

##### 5.1.5.2 L1损失

$\ell_{2}$ 损失对与真实值的偏差进行二次惩罚，因此对异常值敏感。一种更稳健的替代方案是绝对值损失或 $\ell_{1}$ 损失：

$$  \ell_{1}(h,a)=|h-a|   \tag*{(5.35)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_448_121_722_340.jpg" alt="图片" width="23%" /></div>


<div style="text-align: center;">图 5.3：$\ell_2$、$\ell_1$ 和 Huber 损失函数（$\delta = 1.5$）的示意图。由 huberLossPlot.ipynb 生成。</div>


这一情况在图 5.3 中进行了示意。练习 5.4 要求你证明最优估计是后验中位数，即满足 $\Pr(h < a|\boldsymbol{x}) = \Pr(h \geq a|\boldsymbol{x}) = 0.5$ 的值 $a$。我们可以将此用于鲁棒回归，这在第 11.6.1 节中讨论。

##### 5.1.5.3 Huber 损失

另一种鲁棒损失函数是 Huber 损失 [Hub64]，定义如下：

$$  \ell_{\delta}(h,a)=\begin{cases}r^{2}/2&if|r|\leq\delta\\\delta|r|-\delta^{2}/2&if|r|>\delta\end{cases}   \tag*{(5.36)}$$

其中 $r = h - a$。对于小于 $\delta$ 的误差，该函数等价于 $\ell_2$；对于较大的误差，则等价于 $\ell_1$。其图形见图 5.3。我们可以在第 11.6.3 节讨论的鲁棒回归中使用它。

#### 5.1.6 概率预测问题

在第 5.1.2 节中，我们假设可能的动作集合是选择一个单一的类别标签（或者可能是“拒绝”或“不知道”动作）。在第 5.1.5 节中，我们假设可能的动作集合是选择一个实值标量。在本节中，我们假设可能的动作集合是选择某个感兴趣值上的概率分布。也就是说，我们希望进行**概率预测**或**概率预报**，而不是预测一个特定值。更准确地说，我们假设真实的“自然状态”是一个分布 $h = p(Y|\boldsymbol{x})$，动作是另一个分布 $a = q(Y|\boldsymbol{x})$，并且我们要针对每个给定的 $\boldsymbol{x}$ 选择 $q$ 以最小化 $\mathbb{E}[\ell(p,q)]$。为简洁起见，我们省略对 $\boldsymbol{x}$ 的条件设定。

##### 5.1.6.1 KL 散度、交叉熵与对数损失

比较两个分布的常用损失函数是 Kullback-Leibler 散度，简称 KL 散度，定义如下：

$$  D_{\mathbb{K L}}\left(p\parallel q\right)\triangleq\sum_{y\in\mathcal{Y}}p(y)\log\frac{p(y)}{q(y)}   \tag*{(5.37)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证。

---

(为了表示简洁，我们假设变量 $y$ 是离散的，但这可以推广到实值变量。) 在第6.2节中，我们展示了KL散度满足以下性质：$D_{\mathbb{K}\mathbb{L}}(p \parallel q) \geq 0$，当且仅当 $p = q$ 时取等号。注意，它对其参数是非对称的。

我们可以将KL散度展开如下：

$$  D_{\mathbb{K L}}\left(p\parallel q\right)=\sum_{y\in\mathcal{Y}}p(y)\log p(y)-\sum_{y\in\mathcal{Y}}p(y)\log q(y)   \tag*{(5.38)}$$

$$  =-\mathbb{H}(p)+\mathbb{H}_{c e}(p,q)   \tag*{(5.39)}$$

$$  \mathbb{H}(p)\triangleq-\sum_{y}p(y)\log p(y)   \tag*{(5.40)}$$

$$  \mathbb{H}_{c e}(p,q)\triangleq-\sum_{y}p(y)\log q(y)   \tag*{(5.41)}$$

其中 $\mathbb{H}(p)$ 项称为**熵**。它衡量分布 $p$ 的不确定性或方差；当 $p$ 为均匀分布时熵最大，当 $p$ 为退化或确定性 delta 函数时熵为0。熵常用于信息论领域，该领域关注数据压缩和通信的最优方式（详见第6章）。最优编码方案会将更少的比特分配给更频繁出现的符号（即 $p(y)$ 较大的 $Y$ 值），而将更多比特分配给不频繁出现的符号。一个关键结果表明，压缩由分布 $p$ 生成的数据集所需的最小比特数至少为 $\mathbb{H}(p)$；因此，熵提供了不损失信息的前提下我们能压缩数据程度的下界。**交叉熵** $\mathbb{H}_{ce}(p, q)$ 衡量的是，如果我们使用分布 $q$ 设计编码，压缩来自分布 $p$ 的数据集所需的期望比特数。因此，KL散度是由于使用错误分布 $q$ 而额外需要的比特数。若KL散度为零，则意味着我们能正确预测所有可能未来事件的概率，从而学习到了与能获取真实分布 $p$ 的“预言机”一样好的预测能力。

为找到预测未来数据时的最优分布，我们可以最小化 $D_{\mathbb{K}\mathbb{L}}(p \parallel q)$。由于 $\mathbb{H}(p)$ 相对于 $q$ 是常数，可忽略不计，因此我们等价地最小化交叉熵：

$$  q^{*}(Y)=\underset{q}{\operatorname{argmin}}\mathbb{H}_{ce}(p(Y),q(Y))   \tag*{(5.42)}$$

现在考虑一种特殊情况，其中自然状态的真实分布是退化的，它将所有质量集中在一个结果（比如 $c$）上，即 $h = p(Y) = \mathbb{I}(Y = c)$。这通常称为“独热”分布，因为它将向量的第 $c$ 个元素“开启”，而其他元素“关闭”，如图2.1所示。在这种情况下，交叉熵变为

$$  \mathbb{H}_{c e}(\delta(Y=c),q)=-\sum_{y\in\mathcal{Y}}\delta(y=c)\log q(y)=-\log q(c)   \tag*{(5.43)}$$

这称为给定目标标签 $c$ 时预测分布 $q$ 的**对数损失**。

##### 5.1.6.2 适当的评分规则

交叉熵损失是概率预测中非常常见的选择，但并非唯一的可能度量。我们希望的关键性质是，如果决策者选择

---

与真实分布 $p$ 匹配的分布 $q$，即 $\ell(p,p) \leq \ell(p,q)$，且当且仅当 $p = q$ 时等号成立。这样的损失函数 $\ell$ 称为**适当评分规则** [GR07]。我们可以证明，交叉熵损失是一种适当评分规则，因为 $0 = D_{\mathbb{K}\mathbb{L}} (p \parallel p) \leq D_{\mathbb{K}\mathbb{L}} (p \parallel q)$。

##### 5.1.6.3 Brier 分数

KL 损失中的 $\log[p(y)/q(y)]$ 项对低概率事件的误差可能相当敏感 [QC+06]。一种常见的替代方案是使用 **Brier 分数** [Bri50]，这是另一种适当评分规则，最初源于天气预报领域。其定义针对真实分布 $p$ 为 $N$ 个 delta 函数 $\boldsymbol{p}_n(\mathbf{Y}_n) = \delta(\mathbf{Y}_n - \mathbf{y}_n)$ 的特殊情况，其中 $\boldsymbol{y}_n$ 是以独热形式表示的观测结果，即如果第 $n$ 个观测结果为类别 $c$，则 $y_{nc} = 1$。相应的预测分布假设为 $N$ 个分布 $\boldsymbol{q}_n(\mathbf{Y}_n)$，当然它们可以依赖于协变量 $\boldsymbol{x}_n$。Brier 分数定义如下：

$$  \mathrm{BS}(\boldsymbol{p},\boldsymbol{q})\triangleq\frac{1}{N}\sum_{n=1}^{N}\sum_{c=1}^{C}(q_{nc}-p_{nc})^{2}=\frac{1}{N}\sum_{n=1}^{N}\sum_{c=1}^{C}(q_{nc}-y_{nc})^{2}   \tag*{(5.44)}$$

即将预测分布与真实分布视为向量时的均方误差。由于基于平方误差，Brier 分数对极罕见或极常见类别的敏感性较低。

在二分类的特殊情况下，我们使用类别标签 $c = 0$ 和 $c = 1$，定义 $y_n = y_{n1}$ 和 $q_n = q(Y_{n1})$，此时求和项变为 $(q_n - y_n)^2 + (1 - q_n - (1 - y_n))^2 = 2(q_n - y_n)^2$。因此，对于二分类情况，我们通常将多类定义除以 2，得到二分类 Brier 分数 $\mathrm{BS}(\boldsymbol{p}, \boldsymbol{q}) = \frac{1}{N} \sum_{n=1}^N (q_n - y_n)^2$，其取值范围为 $[0, 1]$，最优损失为 0。

由于绝对 Brier 分数值难以解释，有时会使用一种称为 **Brier 技能分数** 的相对性能度量，定义为 $BSS = 1 - \frac{BS}{BS_{ref}}$，其中 $BS_{ref}$ 是参考模型的 BS。该分数的取值范围为 $[-1, 1]$，1 表示最佳，0 表示相对于基线没有改进，-1 表示最差。对于二分类预测器，一种常见的参考模型是基线经验概率 $\overline{q} = \frac{1}{N} \sum_{n=1}^{N} y_n$。在气象学界，这被称为“样本内气候学”预测，其中“样本内”指基于观测数据，“气候学”指长期平均行为。然而，参考模型可以是复杂的数值天气预报模型，而目标模型（被评估的）可以是机器学习模型（例如，参见 [Pri+23]）。

### 5.2 选择“正确”的模型

在本节中，我们考虑存在多个候选（参数化）模型（例如，具有不同层数的神经网络）并希望选择“正确”模型的情形。这可以利用贝叶斯决策理论的工具来处理。

#### 5.2.1 贝叶斯假设检验

假设我们有两个假设或模型，通常称为零假设 $M_{0}$ 和备择假设 $M_{1}$，我们想知道哪一个更可能为真。这称为假设检验。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>贝叶斯因子  $ BF(1,0) $</td><td style='text-align: center; word-wrap: break-word;'>解释</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ BF < \frac{1}{100} $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{0} $ 的决定性证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ BF < \frac{1}{10} $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{0} $ 的强证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{10} < BF < \frac{1}{3} $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{0} $ 的中等证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{3} < BF < 1 $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{0} $ 的弱证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ 1 < BF < 3 $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{1} $ 的弱证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ 3 < BF < 10 $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{1} $ 的中等证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ BF > 10 $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{1} $ 的强证据</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ BF > 100 $</td><td style='text-align: center; word-wrap: break-word;'>支持 $ M_{1} $ 的决定性证据</td></tr></table>

<div style="text-align: center;">表 5.6：用于解释贝叶斯因子的杰弗里斯证据尺度。</div>


如果我们使用 0-1 损失，那么最优决策是当且仅当 $ p(M_1|\mathcal{D}) > p(M_0|\mathcal{D}) $ 时选择备择假设，等价地，当 $ p(M_1|\mathcal{D})/p(M_0|\mathcal{D}) > 1 $。如果使用均匀先验，即 $ p(M_0) = p(M_1) = 0.5 $，则决策规则变为：当且仅当 $ p(\mathcal{D}|M_1)/p(\mathcal{D}|M_0) > 1 $ 时选择 $ M_1 $。这个量是两个模型的边际似然之比，称为贝叶斯因子：

$$  B_{1,0}\triangleq\frac{p(\mathcal{D}|M_{1})}{p(\mathcal{D}|M_{0})}   \tag*{(5.45)}$$

这类似于似然比，区别在于我们对参数进行了积分，这使得我们可以比较不同复杂度的模型，这得益于第 5.2.3 节中解释的贝叶斯奥卡姆剃刀效应。

如果 $ B_{1,0} > 1 $，则我们偏好模型 1，否则偏好模型 0。当然，$ B_{1,0} $ 可能仅略大于 1。在这种情况下，我们不太确信模型 1 更好。Jeffreys [Jef61] 提出了一个证据尺度用于解释贝叶斯因子的大小，如表 5.6 所示。这是对频率学派 p 值概念的贝叶斯替代（见第 5.5.3 节）。

我们将在第 5.2.1.1 节给出一个计算贝叶斯因子的实例。

##### 5.2.1.1 示例：检验硬币是否均匀

作为示例，假设我们观察了一些硬币抛掷结果，并且想要判断数据是由公平硬币（$ \theta = 0.5 $）生成的，还是由可能有偏的硬币（$ \theta $ 可以是 [0,1] 中的任何值）生成的。记第一个模型为 $ M_0 $，第二个模型为 $ M_1 $。在 $ M_0 $ 下的边际似然简单地为

$$  p(\mathcal{D}|M_{0})=\left(\frac{1}{2}\right)^{N}   \tag*{(5.46)}$$

其中 $ N $ 是抛掷次数。根据公式 (4.143)，在 $ M_{1} $ 下使用 Beta 先验的边际似然为

$$  p(\mathcal{D}|M_{1})=\int p(\mathcal{D}|\theta)p(\theta)d\theta=\frac{B(\alpha_{1}+N_{1},\alpha_{0}+N_{0})}{B(\alpha_{1},\alpha_{0})}   \tag*{(5.47)}$$

我们在图 5.4(a) 中绘制了 $ \log p(\mathcal{D}|M_1) $ 与正面次数 $ N_1 $ 的关系，假设 $ N = 5 $ 且使用均匀先验 $ \alpha_1 = \alpha_0 = 1 $。（曲线的形状对 $ \alpha_1 $ 和 $ \alpha_0 $ 不敏感，只要先验对称，即 $ \alpha_0 = \alpha_1 $。）如果我们观察到 2 或 3 次正面，无偏硬币假设 $ M_0 $

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_205_123_554_413.jpg" alt="图像" width="30%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_610_123_961_412.jpg" alt="图像" width="30%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 5.4：(a) 抛硬币示例中对数边际似然随头部数量变化的情况。(b) BIC 近似。（垂直刻度是任意的，因为我们固定了 N。）由 coins_model_sel_demo.ipynb 生成。</div>


比 $ M_1 $ 更可能，因为 $ M_0 $ 是一个更简单的模型（它没有自由参数）——如果硬币有偏却恰好产生几乎 50/50 的正面/反面结果，这将是一个可疑的巧合。然而，随着计数结果变得更为极端，我们更倾向于有偏硬币的假设。注意，如果绘制对数贝叶斯因子 $ \log B_{1,0} $，它将具有完全相同的形状，因为 $ \log p(\mathcal{D}|M_0) $ 是一个常数。

#### 5.2.2 贝叶斯模型选择

现在假设我们有一个包含多于 2 个模型的集合 $\mathcal{M}$，并且希望选择最可能的模型。这称为模型选择。我们可以将其视为一个决策理论问题，其中行动空间要求选择一个模型 $m \in \mathcal{M}$。如果采用 0-1 损失，最优行动是选择最可能的模型：

$$  \hat{m}=\underset{m\in\mathcal{M}}{\operatorname{argmax}}p(m|\mathcal{D})   \tag*{(5.48)}$$

其中

$$  p(m|\mathcal{D})=\frac{p(\mathcal{D}|m)p(m)}{\sum_{m\in\mathcal{M}}p(\mathcal{D}|m)p(m)}   \tag*{(5.49)}$$

是模型的后验概率。如果模型的先验是均匀的，即 $ p(m) = 1/|\mathcal{M}| $，那么 MAP 模型由下式给出：

$$  \hat{m}=\underset{m\in\mathcal{M}}{\operatorname{argmax}}p(\mathcal{D}|m)   \tag*{(5.50)}$$

其中 $ p(\mathcal{D}|m) $ 由下式给出：

$$  p(\mathcal{D}|m)=\int p(\mathcal{D}|\boldsymbol{\theta},m)p(\boldsymbol{\theta}|m)d\boldsymbol{\theta}   \tag*{(5.51)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_254_130_500_329.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_657_130_909_331.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_248_379_499_578.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_648_391_907_586.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;"> $ (d) $</div>


<div style="text-align: center;">图 5.5: 多项式回归中贝叶斯模型选择的示意图。(a-c) 我们针对 N = 5 个数据点分别拟合了 1 次、2 次和 3 次多项式。绿色实曲线为真实函数，红色虚线为预测值（蓝色点虚线表示均值周围  $ \pm 2\sigma $ 的范围）。(d) 我们绘制了模型的后验  $ p(m|D) $，假设先验  $ p(m) \propto 1 $ 为均匀分布。该图由  $ \text{linreg\_eb\_modelsel\_vs\_n.ipymb} $ 生成。</div>


这被称为边际似然（marginal likelihood），或模型 m 的证据（evidence）。直观上，它是数据在所有可能参数值上的平均似然，并按先验  $ p(\boldsymbol{\theta}|m) $ 进行加权。如果  $ \boldsymbol{\theta} $ 的所有设置都赋予数据高概率，那么这很可能是一个好模型。

##### 5.2.2.1 示例：多项式回归

作为贝叶斯模型选择的一个示例，我们将考虑一维多项式回归。图 5.5 展示了三种不同模型的后验，这些模型分别对应针对 N = 5 个数据点拟合的 1 次、2 次和 3 次多项式。我们采用均匀的模型先验，并使用经验贝叶斯（empirical Bayes）估计回归权重的先验（参见第 11.7.7 节）。然后，我们计算每个模型的证据（关于如何计算的具体细节参见第 11.7 节）。可以看出，数据量不足以支持一个复杂模型，因此 MAP 模型为 m = 1。图 5.6 展示了 N = 30 个数据点时的类似结果。此时我们发现 MAP 模型为 m = 2；更大的样本量意味着我们可以安全地选择更复杂的模型。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_255_130_500_330.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_660_129_909_333.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_253_379_501_577.jpg" alt="图像" width="21%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_648_390_908_588.jpg" alt="图像" width="22%" /></div>


<div style="text-align: center;"> $ (d) $</div>


<div style="text-align: center;">图 5.6：与图 5.5 相同，但此处 N = 30。由 linreg_eb_modelsel_vs_n.ipynb 生成。</div>


#### 5.2.3 奥卡姆剃刀

考虑两个模型，一个简单的模型 $ m_1 $ 和一个更复杂的模型 $ m_2 $。假设两者都能通过适当优化其参数来解释数据，即 $ p(\mathcal{D}|\pmb{\theta}_1, m_1) $ 和 $ p(\mathcal{D}|\pmb{\theta}_2, m_2) $ 都很大。直观上，我们应偏好 $ m_1 $，因为它更简单且与 $ m_2 $ 同样有效。这一原则被称为**奥卡姆剃刀**。

现在让我们看看，基于边际似然（即对先验下的似然取平均）对模型进行排序如何产生这种表现。复杂模型会将较少的先验概率分配给能够解释数据的“好”参数 $ \hat{\theta}_2 $，因为先验在整个参数空间上的积分必须为 1.0。因此，它会在参数空间中似然较低的部分取平均。相比之下，简单模型的参数更少，因此先验集中在较小的体积内；其平均值将主要位于参数空间中靠近 $ \hat{\theta}_1 $ 的优质部分。由此，我们看到边际似然会更偏好简单模型。这被称为**贝叶斯奥卡姆剃刀效应** [Mac95; MG05]。

理解贝叶斯奥卡姆剃刀效应的另一种方式是比较简单模型与复杂模型的相对预测能力。由于概率之和必须为 1，我们有 $ \sum_{\mathcal{D}^{\prime}} p(\mathcal{D}^{\prime}|m) = 1 $，其中求和遍及所有可能的数据集。能够预测很多事物的复杂模型必须将其预测概率质量分散得很薄，因此对于任何给定的数据集，它获得的概率不如简单模型那么大。这有时被称为**概率质量守恒原理**，如图 5.7 所示。在横轴上，我们按复杂度增加顺序（以某种抽象意义衡量）绘制所有可能的数据集；在纵轴上，我们绘制

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_382_120_770_408.jpg" alt="图像" width="33%" /></div>

<div style="text-align: center;">图 5.7：贝叶斯奥卡姆剃刀的示意图。宽（绿色）曲线对应复杂模型，窄（蓝色）曲线对应简单模型，中间（红色）曲线则恰到好处。改编自 [Bis06] 的图 3.13。另见 [MG05, 图 2]，该图基于真实数据绘制了类似的图。</div>

三种可能模型的预测：简单模型 $ M_1 $，中等模型 $ M_2 $，以及复杂模型 $ M_3 $。我们还用一条竖线标出了实际观测到的数据 $ \mathcal{D}_0 $。模型 1 过于简单，给 $ \mathcal{D}_0 $ 分配的概率很低。模型 3 给 $ \mathcal{D}_0 $ 分配的概率也相对较低，因为它能预测许多数据集，因此其概率分布得相当广泛而稀疏。模型 2 “恰到好处”：它以合理的置信度预测了观测数据，但又不过度预测其他事物。因此模型 2 是最可能的模型。

#### 5.2.4 交叉验证与边际似然的联系

我们已经看到边际似然如何帮助我们选择“恰当”复杂度的模型。在非贝叶斯的模型选择方法中，通常使用交叉验证（第 4.5.5 节）来实现这一目的。

事实证明，边际似然与留一交叉验证（LOO-CV）估计密切相关，下面我们将展示这一点。我们从模型 $ m $ 的边际似然出发，将其按序贯形式写作：

$$ p(\mathcal{D}|m)=\prod_{n=1}^{N}p(y_{n}|y_{1:n-1},\boldsymbol{x}_{1:N},m)=\prod_{n=1}^{N}p(y_{n}|\boldsymbol{x}_{n},\mathcal{D}_{1:n-1},m) \tag*{(5.52)}$$

其中

$$ p(y|\boldsymbol{x},\mathcal{D}_{1:n-1},m)=\int p(y|\boldsymbol{x},\boldsymbol{\theta})p(\boldsymbol{\theta}|\mathcal{D}_{1:n-1},m)d\boldsymbol{\theta} \tag*{(5.53)}$$

假设我们对上述分布使用插件近似，得到

$$ p(y|\boldsymbol{x},\mathcal{D}_{1:n-1},m)\approx\int p(y|\boldsymbol{x},\boldsymbol{\theta})\delta(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}}_{m}(\mathcal{D}_{1:n-1}))d\boldsymbol{\theta}=p(y|\boldsymbol{x},\hat{\boldsymbol{\theta}}_{m}(\mathcal{D}_{1:n-1})) \tag*{(5.54)}$$

《概率机器学习：导论》。在线版本。2024 年 11 月 23 日

---

我们得到

$$ \log p(\mathcal{D}|m)\approx\sum_{n=1}^{N}\log p(y_{n}|\boldsymbol{x}_{n},\hat{\boldsymbol{\theta}}_{m}(\mathcal{D}_{1:n-1})) \tag*{(5.55)} $$

这类似于似然函数的留一交叉验证估计，其形式为 $ \frac{1}{N}\sum_{n=1}^{N}\log p(y_n|\boldsymbol{x}_n,\hat{\boldsymbol{\theta}}_n(\mathcal{D}_{1:n-1,n+1:N})) $，只是我们忽略了 $ \mathcal{D}_{n+1:N} $ 部分。这种联系背后的直觉是：过于复杂的模型会在“早期”样本上过拟合，进而对剩余样本预测不佳，因此也会得到较低的交叉验证分数。关于这些性能指标之间联系的更详细讨论，请参见 [FH20]。

#### 5.2.5 信息准则

边缘似然 $ p(\mathcal{D}|m) = \int p(\mathcal{D}|\boldsymbol{\theta}, m)p(\boldsymbol{\theta})d\boldsymbol{\theta} $ 是第5.2.2节讨论的贝叶斯模型选择所需要的，但计算起来可能很困难，因为它需要对整个参数空间进行积分。此外，结果可能对先验的选择相当敏感。在本节中，我们讨论一些其他相关的模型选择度量，称为信息准则。它们具有以下形式：$ \mathcal{L}(m) = -\log p(\mathcal{D}|\boldsymbol{\theta}, m) + C(m) $，其中 $ C(m) $ 是添加到负对数似然（NLL）上的复杂度惩罚项。不同方法使用不同的复杂度项 $ C(m) $，如下所述。更多细节可参见例如 [GHV14]。

关于符号的说明：在使用信息准则时，通常将 NLL 乘以 -2 得到 **偏差**，即 $ \text{deviance}(m) = -2 \log p(\mathcal{D}|\hat{\theta}, m) $。这使得某些高斯模型的数学表达式更“美观”。

##### 5.2.5.1 贝叶斯信息准则 (BIC)

贝叶斯信息准则（BIC）[Sch78] 可以被看作是对对数边缘似然的一种简单近似。特别地，如果我们像第4.6.8.2节讨论的那样对后验进行高斯近似，则从公式 (4.215) 得到：

$$ \log p(\mathcal{D}|m)\approx\log p(\mathcal{D}|\hat{\boldsymbol{\theta}}_{\mathrm{map}})+\log p(\hat{\boldsymbol{\theta}}_{\mathrm{map}})-\frac{1}{2}\log|\mathbf{H}| \tag*{(5.56)} $$

其中 $ \mathbf{H} $ 是负对数联合分布 $ -\log p(\mathcal{D}, \boldsymbol{\theta}) $ 在 MAP 估计 $ \hat{\boldsymbol{\theta}}_{\text{map}} $ 处计算的 Hessian 矩阵。我们看到公式 (5.56) 是对数似然加上一些惩罚项。如果我们采用均匀先验 $ p(\boldsymbol{\theta}) \propto 1 $，可以去掉先验项，并将 MAP 估计替换为 MLE $ \hat{\boldsymbol{\theta}} $，得到：

$$ \log p(\mathcal{D}|m)\approx\log p(\mathcal{D}|\hat{\boldsymbol{\theta}})-\frac{1}{2}\log|\mathbf{H}| \tag*{(5.57)} $$

现在我们专注于近似 $ \log |\mathbf{H}| $ 项，该项有时被称为 **奥卡姆因子**，因为它衡量了模型复杂度（后验分布的体积）。我们有 $ \mathbf{H} = \sum_{i=1}^{N} \mathbf{H}_i $，其中 $ \mathbf{H}_i = \nabla \nabla \log p(\mathbf{y}_i | \boldsymbol{\theta}) $ 是经验 Fisher 信息矩阵（第4.7.2节）。让我们用固定矩阵 $ \hat{\mathbf{H}} $ 近似每个 $ \mathbf{H}_i $。那么我们有：

$$ \log|\mathbf{H}|=\log|N\hat{\mathbf{H}}|=\log(N^{D_{m}}|\hat{\mathbf{H}}|)=D_{m}\log N+\log|\hat{\mathbf{H}}| \tag*{(5.58)} $$

作者：Kevin P. Murphy。 (C) MIT Press. CC-BY-NC-ND 许可证。

---

其中 $ D_m = \dim(\boldsymbol{\theta}) $，并且我们假设 $ \mathbf{H} $ 是满秩的。我们可以忽略 $ \log |\hat{\mathbf{H}}| $ 项，因为它与 $ N $ 无关，因此会被似然项压倒。将所有部分结合起来，我们得到希望最大化的 BIC 分数：

$$  J_{\mathrm{B I C}}(m)=\log p(\mathcal{D}|m)\approx\log p(\mathcal{D}|\hat{\boldsymbol{\theta}},m)-\frac{D_{m}}{2}\log N   \tag*{(5.59)}$$

我们也可以定义希望最小化的 BIC 损失，即乘以 -2：

$$  \mathcal{L}_{\mathrm{B I C}}(m)=-2\log p(\mathcal{D}|\hat{\boldsymbol{\theta}},m)+D_{m}\log N   \tag*{(5.60)}$$

（选择 2 作为缩放因子是为了在使用高斯似然的模型时简化表达式。）

##### 5.2.5.2 赤池信息量准则（AIC）

赤池信息量准则 [Aka74] 与 BIC 密切相关，其形式为：

$$  \mathcal{L}_{\mathrm{A I C}}(m)=-2\log p(\mathcal{D}|\hat{\boldsymbol{\theta}},m)+2D_{m}   \tag*{(5.61)}$$

该准则对复杂模型的惩罚比 BIC 更轻，因为正则项与 $ N $ 无关。该估计量可以从频率派角度推导得出。

##### 5.2.5.3 最小描述长度（MDL）

我们可以利用信息论（第6章）的工具来思考对不同模型进行评分的问题。具体而言，假设我们希望选择一个模型，使得发送方能够用最少的比特数向接收方发送某些数据。这种选择模型的方法称为最小描述长度或 MDL 原则（详见例如 [HY01b; Gru07; GR19]，以及密切相关的[最小消息长度准则] [Wal05]）。

我们现在推导一个 MDL 目标的近似。首先，发送方需要指定使用哪个模型。设 $ \hat{\theta} \in \mathbb{R}^{D_m} $ 是使用 $ N $ 个数据样本估计得到的参数。由于我们只能以 $ O(1/\sqrt{N}) $ 的精度可靠地估计每个参数（见 4.6.4.1 节），因此每个参数仅需使用 $ \log_2(1/\sqrt{N}) = \frac{1}{2} \log_2(N) $ 比特进行编码。其次，发送方需要使用该模型编码数据，这需要 $ -\log p(\mathcal{D}|\hat{\theta}, m) = -\sum_n \log p(y_n|\hat{\theta}, m) $ 比特。总代价为：

$$  \mathcal{L}_{\mathrm{M D L}}(m)=-\log p(\mathcal{D}|\hat{\boldsymbol{\theta}},m)+\frac{D_{m}}{2}\log N   \tag*{(5.62)}$$

我们看到，这种两部分编码与 BIC 具有相同的基本形式。

##### 5.2.5.4 广泛适用信息量准则（WAIC）

BIC、AIC 和 MDL 的主要问题在于：模型自由度的计算可能很困难，而这正是定义复杂度项所需的，因为大多数参数高度相关且无法从似然中唯一识别。特别地，如果参数到似然的映射不是一一对应的，则模型被称为奇异统计模型，因为相应的费舍尔信息矩阵（4.7.2节），以及上述的海森矩阵 H，可能是奇异的。

---

奇异的。（在过参数化模型中也会出现类似问题 [Dwi+23]。）一种即使在奇异情况下也适用的替代准则被称为广泛适用信息准则（widely applicable information criterion, WAIC），也称为Watanabe–Akaike信息准则 [Wat10; Wat13]。

WAIC 将边际对数似然的插件近似 $\ell(m) = \sum_n \log p(y_n | \hat{\theta}, m)$ 替换为期望逐点预测密度（expected log pointwise predictive density, ELPD），定义为 $\text{ELPD}(m) = \sum_{n=1}^N \log p(y_n | \mathcal{D}, m) = \sum_{n=1}^N \log \mathbb{E}_{\theta \mid \mathcal{D}, m} [p(y_n | \hat{\theta}, m)]$，通常通过蒙特卡洛近似。此外，复杂度项定义为 $C(m) = \sum_{n=1}^N \log \mathbb{V}_{\theta \mid \mathcal{D}, m} [p(y_n | \hat{\theta}, m)]$，同样通常通过蒙特卡洛近似。（其直观含义如下：如果对于给定的数据点 $y_n$，不同的后验样本 $\theta_s$ 做出非常不同的预测，那么模型是不确定的，且可能过于灵活。复杂度项本质上统计了这种情况发生的频率。）我们希望最小化的 WAIC 损失定义为 $\mathcal{L}_{\text{WAIC}}(m) = -2 \text{LPPD}(m) + 2C(m)$。

注意，WAIC 使用参数的后验来评估期望对数似然。相比之下，边际似然是对先验的 log 似然取平均。这使得边际似然对先验更敏感。因此，在模型选择中通常使用 WAIC 更好。高效的蒙特卡洛近似方法在 [VGG17] 中讨论。

#### 5.2.6 效应量的后验推断与贝叶斯显著性检验

第 5.2.1 节讨论的假设检验方法依赖于计算零假设与备择假设的贝叶斯因子 $p(\mathcal{D}|H_0)/p(\mathcal{D}|H_1)$。不幸的是，计算所需的边际似然可能计算困难，且结果对先验的选择敏感。此外，我们通常更关注估计效应量，即两个参数之间的幅度差异，而不是判断效应量是否为 0（零假设）或非 0（备择假设）——后者称为点零假设，通常被视为无关紧要的“稻草人”（参见例如 [Mak+19] 及其参考文献）。

例如，假设我们有两个分类器 $m_1$ 和 $m_2$，想知道哪个更好。即，我们要进行分类器的比较。设 $\mu_1$ 和 $\mu_2$ 为它们的平均准确率，$\Delta = \mu_1 - \mu_2$ 为准确率的差异。模型 1 在平均意义上比模型 2 更准确的概率为 $p(\Delta > 0|\mathcal{D})$。然而，即使这个概率很大，改进也可能不具有实际显著性。因此，最好计算诸如 $p(\Delta > \epsilon|\mathcal{D})$ 或 $p(|\Delta| > \epsilon|\mathcal{D})$ 的概率，其中 $\epsilon$ 表示当前问题有意义的最小效应量幅度。这称为单侧检验或双侧检验。

更一般地，令 $R = [-\epsilon, \epsilon]$ 表示实际等价区间（region of practical equivalence, ROPE）[Kru15; KL17]。我们可以定义三个感兴趣的事件：零假设 $H_0 : \Delta \in R$，表示两种方法实际相同（这比 $H_0 : \Delta = 0$ 更现实）；$H_A : \Delta > \epsilon$，表示 $m_1$ 优于 $m_2$；以及 $H_B : \Delta < -\epsilon$，表示 $m_2$ 优于 $m_1$。要在这三个假设中进行选择，只需计算 $p(\Delta | \mathcal{D})$，这避免了计算贝叶斯因子。在下面的小节中，我们讨论如何使用两种不同类型的模型来计算该量。

##### 5.2.6.1 均值差异的贝叶斯 t 检验

假设我们有两个分类器 $m_1$ 和 $m_2$，它们在相同的 $N$ 个测试样本上进行评估。令 $e_i^m$ 为方法 $m$ 在测试样本 $i$ 上的误差。（或者可以是条件对数似然 $e_i^m = \log p^m(y_i | \boldsymbol{x}_i)$。）由于分类器应用于相同的数据，我们可以使用配对检验来比较它们，这比仅看平均性能更敏感，因为因素

---

使一个示例容易被分类或难以分类（例如，由于标签噪声）的影响会被两种方法共享。因此，我们将关注差值  $ d_i = e_i^1 - e_i^2 $。我们假设  $ d_i \sim \mathcal{N}(\Delta, \sigma^2) $。我们关心  $ p(\Delta | \boldsymbol{d}) $，其中  $ \boldsymbol{d} = (d_1, \ldots, d_N) $。

如果我们对未知参数  $ (\Delta,\sigma) $ 使用无信息先验，可以证明均值后验边缘分布为 Student 分布：

 $$ p(\Delta|\boldsymbol{d})=\mathcal{T}_{N-1}(\Delta|\mu,s^{2}/N) $$ 

其中  $ \mu = \frac{1}{N} \sum_{i=1}^{N} d_i $ 为样本均值，$ s^2 = \frac{1}{N-1} \sum_{i=1}^{N} (d_i - \mu)^2 $ 为方差的无偏估计。因此我们可以轻松计算  $ p(|\Delta| > \epsilon|\boldsymbol{d}) $，其中 ROPE（实际等价区间，Region of Practical Equivalence）取  $ \epsilon = 0.01 $（例如）。这被称为贝叶斯 t 检验 [Ben+17]。（另见 [Rou+09] 中基于贝叶斯因子的贝叶斯 t 检验，以及 [Die98] 中用于比较分类器的非贝叶斯方法。）

形式化检验的另一种替代方法是直接绘制后验分布  $ p(\Delta|\boldsymbol{d}) $。如果该分布紧密集中在 0 附近，我们可以得出结论：两种方法之间不存在显著差异。（事实上，更简单的方法是仅绘制数据  $ \{d_i\} $ 的箱线图，这避免了任何形式化统计分析的需性。）

注意，这类问题出现在许多应用中，而不仅限于评估分类器。例如，假设我们有 $N$ 个人，每个人分别暴露于两种药物下；设 $e_i^m$ 为第 $i$ 个人暴露于药物 $m$ 后的结果（如疾病程度），$d_i^m = e_i^1 - e_i^2$ 为响应差异。那么我们可以按照上述讨论，通过计算 $p(\Delta|\mathbf{d})$ 来分析药物效果。

##### 5.2.6.2 比率差异的贝叶斯  $ \chi^{2} $ 检验

现在假设有两个分类器，它们在不同的测试集上进行评估。设 $ y_m $ 是方法 $ m \in \{1,2\} $ 在 $ N_m $ 次试验中正确分类的样本数，因此准确率为 $ y_m/N_m $。我们假设 $ y_m \sim \text{Bin}(N_m, \theta_m) $，因此关心 $ p(\Delta|\mathcal{D}) $，其中 $ \Delta = \theta_1 - \theta_2 $，$ \mathcal{D} = (y_1, N_1, y_2, N_2) $ 为所有数据。

如果对 $ \theta_1 $ 和 $ \theta_2 $ 使用均匀先验（即 $ p(\theta_j) = \text{Beta}(\theta_j | 1, 1) $），后验分布为

 $$ p(\theta_{1},\theta_{2}|\mathcal{D})=\mathrm{Beta}(\theta_{1}|y_{1}+1,N_{1}-y_{1}+1)\mathrm{Beta}(\theta_{2}|y_{2}+1,N_{2}-y_{2}+1) $$ 

$ \Delta $ 的后验分布为

 $$ \begin{align*}p(\Delta|\mathcal{D})&=\int_{0}^{1}\int_{0}^{1}\mathbb{I}(\Delta=\theta_{1}-\theta_{2})p(\theta_{1}|\mathcal{D}_{1})p(\theta_{2}|\mathcal{D}_{2})\\&=\int_{0}^{1}\mathrm{Beta}(\theta_{1}|y_{1}+1,N_{1}-y_{1}+1)\mathrm{Beta}(\theta_{1}-\Delta|y_{2}+1,N_{2}-y_{2}+1)d\theta_{1}\end{align*} $$ 

然后我们可以对任意选定的 $ \Delta $ 值计算该分布。例如，可以计算

$$  p(\Delta>\epsilon|\mathcal{D})=\int_{\epsilon}^{\infty}p(\Delta|\mathcal{D})d\Delta   \tag*{(5.63)}$$

（这可以通过一维数值积分或解析方法 [Coo05] 求得。）这被称为贝叶斯  $ \chi^{2} $ 检验。

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>左撇子</td><td style='text-align: center; word-wrap: break-word;'>右撇子</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>男性</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>43</td><td style='text-align: center; word-wrap: break-word;'>$ N_{1}=52 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>女性</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>44</td><td style='text-align: center; word-wrap: break-word;'>$ N_{2}=48 $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>总计</td><td style='text-align: center; word-wrap: break-word;'>13</td><td style='text-align: center; word-wrap: break-word;'>87</td><td style='text-align: center; word-wrap: break-word;'>100</td></tr></table>

<div style="text-align: center;">表5.7: 来自http://en.wikipedia.org/wiki/Contingency_table 的 $ 2 \times 2 $ 列联表。男性和女性左撇子比例的最大似然估计（MLE）分别为 $ \hat{\theta}_1 = 9/52 = 0.1731 $ 和 $ \hat{\theta}_2 = 4/48 = 0.0417 $。</div>

请注意，这类问题不仅出现在分类器评估中，也广泛出现在许多其他应用中。例如，假设两个组是亚马逊上销售同一产品的不同商家， $ y_m $ 是商家 $ m $ 获得的正面评价数量。或者假设这两组分别对应男性和女性， $ y_m $ 是组 $ m $ 中左撇子的人数， $ N_m - y_m $ 是右撇子的人数。 $ ^3 $ 我们可以将这些数据表示为一个 $ 2 \times 2 $ 的计数列联表，如表5.7所示。

男性和女性左撇子比例的最大似然估计（MLE）分别为 $ \hat{\theta}_1 = 9/52 = 0.1731 $ 和 $ \hat{\theta}_2 = 4/48 = 0.0417 $。差异似乎存在，但样本量较小，因此我们无法确定。因此，我们将通过计算 $ p(\Delta|\mathcal{D}) $ 来表示我们的不确定性，其中 $ \Delta = \theta_1 - \theta_2 $， $ \mathcal{D} $ 是计数表。我们得到 $ p(\theta_1 > \theta_2|\mathcal{D}) = \int_0^\infty p(\Delta|\mathcal{D}) = 0.901 $，这表明左撇子在男性中更常见，这与其它研究结果一致[PP+20]。

### 5.3 频率派决策理论

在本节中，我们讨论频率派决策理论。在这种方法中，我们将自然状态的未知量（通常用 $ \theta $ 而非 h 表示）视为固定但未知的常数，而将数据 x 视为随机的。因此，我们不基于 x 进行条件化，而是对 x 进行平均，以计算当我们的决策过程（估计量）应用于许多不同数据集时所期望的损失。下面给出详细说明。

#### 5.3.1 估计量的风险计算

我们定义一个估计量 $ \delta $ 在给定自然状态 $ \theta $ 时的频率派风险为：将该估计量应用于数据 $ \boldsymbol{x} $ 时的期望损失，其中期望是对来自 $ p(\boldsymbol{x}|\boldsymbol{\theta}) $ 的数据进行的：

$$  R(\boldsymbol{\theta},\boldsymbol{\delta})\triangleq\mathbb{E}_{p(\boldsymbol{x}|\boldsymbol{\theta})}\left[\ell(\boldsymbol{\theta},\delta(\boldsymbol{x}))\right]   \tag*{(5.64)}$$

我们在5.3.1.1节中给出了一个例子。

##### 5.3.1.1 例子

在本节中，我们考虑估计高斯均值的问题。假设数据来自 $ x_n \sim \mathcal{N}(\theta^*, \sigma^2 = 1) $，并设 $ \boldsymbol{x} = (x_1, \ldots, x_N) $。如果我们使用二次损失 $ \ell_2(\theta, \hat{\theta}) = (\theta - \hat{\theta})^2 $，则相应的风险函数就是均方误差（MSE）。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_208_125_531_385.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_614_124_938_385.jpg" alt="图像" width="28%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图5.8：估计高斯均值时的风险函数。每条曲线表示 $ R(\theta_i(\cdot), \theta^*) $ 随 $ \theta^* $ 的变化，其中 $ i $ 对应不同的估计量。每个估计量均基于来自 $ \mathcal{N}(\theta^*, \sigma^2 = 1) $ 的 $ N $ 个样本。深蓝色水平线为样本均值（MLE，最大似然估计）；红色水平线为样本中位数；黑色曲线为估计量 $ \hat{\theta} = \theta_0 = 0 $；绿色曲线为 $ \kappa = 1 $ 时的后验均值；浅蓝色曲线为 $ \kappa = 5 $ 时的后验均值。(a) $ N = 5 $ 个样本。(b) $ N = 20 $ 个样本。改编自 [BS94] 的图 B.1。由 riskFnGauss.ipynb 生成。</div>

现在考虑用于计算 $ \theta $ 的 5 种不同估计量：

• $ \delta_1(x) = \overline{x} $，样本均值。

• $ \delta_2(\boldsymbol{x}) = \text{median}(\boldsymbol{x}) $，样本中位数。

$\bullet \quad \delta_{3}(\mathbf{x})=\theta_{0} \text{，一个固定值}$

- $ \delta_{\kappa}(\boldsymbol{x}) $，在 $ \mathcal{N}(\theta|\theta_0, \sigma^2/\kappa) $ 先验下的后验均值：

$$ \delta_{\kappa}(\boldsymbol{x})=\frac{N}{N+\kappa}\overline{x}+\frac{\kappa}{N+\kappa}\theta_{0}=w\overline{x}+(1-w)\theta_{0} \tag*{(5.65)}$$

对于 $ \delta_{\kappa} $，使用 $ \theta_{0}=0 $，并考虑弱先验 $ \kappa=1 $ 与较强先验 $ \kappa=5 $。

令 $ \hat{\theta} = \hat{\theta}(\boldsymbol{x}) = \delta(\boldsymbol{x}) $ 为估计参数。该估计量的风险由均方误差（MSE）给出。在第 4.7.6.3 节中，我们展示了 MSE 可以分解为平方偏差加上方差：

$$ \mathrm{MSE}(\hat{\theta}|\theta^{*})=\mathbb{V}\left[\hat{\theta}\right]+\mathrm{bias}^{2}(\hat{\theta}) \tag*{(5.66)}$$

其中偏差定义为 $ \text{bias}(\hat{\theta}) = \mathbb{E}\left[\hat{\theta} - \theta^*\right] $。下面利用此表达式推导每个估计量的风险。

$ \delta_{1} $ 是样本均值。它是无偏的，因此其风险为

$$ \mathrm{MSE}(\delta_{1}|\theta^{*})=\mathbb{V}\left[\overline{x}\right]=\frac{\sigma^{2}}{N} \tag*{(5.67)}$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

$ \delta_2 $ 是样本中位数。它也是无偏的。此外，可以证明其方差近似为 $ \pi/(2N) $（其中 $ \pi = 3.14 $），因此风险为

$$  \mathrm{MSE}(\delta_{2}|\theta^{*})=\frac{\pi}{2N}   \tag*{(5.68)}$$

$ \delta_3 $ 返回常数 $ \theta_0 $，因此其偏差为 $ (\theta^* - \theta_0) $，方差为零。因此风险为

$$  \mathrm{MSE}(\delta_{3}|\theta^{*})=(\theta^{*}-\theta_{0})^{2}   \tag*{(5.69)}$$

最后，$ \delta_{4} $ 是高斯先验下的后验均值。我们可以按照以下方式推导其MSE：

$$  \mathrm{MSE}(\delta_{\kappa}|\theta^{*})=\mathbb{E}\left[(w\overline{x}+(1-w)\theta_{0}-\theta^{*})^{2}\right]   \tag*{(5.70)}$$

 $$ =\mathbb{E}\left[\left(w(\overline{x}-\theta^{*})+(1-w)(\theta_{0}-\theta^{*})\right)^{2}\right] $$ 

$$  =w^{2}\frac{\sigma^{2}}{N}+(1-w)^{2}(\theta_{0}-\theta^{*})^{2}   \tag*{(5.72)}$$

$$  =\frac{1}{(N+\kappa)^{2}}\left(N\sigma^{2}+\kappa^{2}(\theta_{0}-\theta^{*})^{2}\right)   \tag*{(5.73)}$$

这些函数在图 Figure 5.8 中针对 $ N \in \{5, 20\} $ 绘制。我们看到通常而言，最佳估计量取决于未知的 $ \theta^* $ 值。如果 $ \theta^* $ 非常接近 $ \theta_0 $，那么 $ \delta_3 $（仅预测 $ \theta_0 $）是最佳的。如果 $ \theta^* $ 在 $ \theta_0 $ 周围的某个合理范围内，那么结合了 $ \theta_0 $ 的先验猜测与实际数据的后验均值是最佳的。如果 $ \theta^* $ 远离 $ \theta_0 $，则 MLE 是最佳的。

##### 5.3.1.2 贝叶斯风险

一般而言，产生数据 x 的真实自然状态 $ \theta $ 是未知的，因此我们无法计算方程(5.64)中给出的风险。解决这个问题的一种方法是为 $ \theta $ 假设一个先验 $ \pi_0 $，然后对其求平均。这便得到了贝叶斯风险，也称为积分风险：

$$  R_{\pi_{0}}(\delta)\triangleq\mathbb{E}_{\pi_{0}(\boldsymbol{\theta})}\left[R(\boldsymbol{\theta},\delta)\right]=\int d\boldsymbol{\theta}\;d\boldsymbol{x}\;\pi_{0}(\boldsymbol{\theta})p(\boldsymbol{x}|\boldsymbol{\theta})\ell(\boldsymbol{\theta},\delta(\boldsymbol{x}))   \tag*{(5.74)}$$

最小化贝叶斯风险的决策规则称为贝叶斯估计量。这等价于贝叶斯决策理论在方程(5.2)中推荐的最优策略，因为

$$  \delta(\boldsymbol{x})=\underset{a}{\arg\min}\int d\boldsymbol{\theta}\pi_{0}(\boldsymbol{\theta})p(\boldsymbol{x}|\boldsymbol{\theta})\ell(\boldsymbol{\theta},a)=\underset{a}{\arg\min}\int d\boldsymbol{\theta}p(\boldsymbol{\theta}|\boldsymbol{x})\ell(\boldsymbol{\theta},a)   \tag*{(5.75)}$$

因此我们看到，在逐例基础上选择最优行动（如贝叶斯方法所做）在平均意义上是（如频率学派方法所做）最优的。换句话说，贝叶斯方法提供了实现频率学派目标的一种良好方式。关于这一点的进一步讨论，参见[BS94, p448]。

##### 5.3.1.3 最大风险

当然，在频率学派的背景下，使用先验可能看起来不可取。因此我们可以将最大风险定义如下：

$$  R_{\mathrm{m a x}}(\delta)\triangleq\operatorname*{s u p}_{\theta}R(\pmb{\theta},\delta)   \tag*{(5.76)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_454_123_709_253.jpg" alt="图片" width="22%" /></div>


<div style="text-align: center;">图 5.9：两种决策过程 $\delta_{1}$ 和 $\delta_{2}$ 的风险函数。由于 $\delta_{1}$ 具有更低的最坏情况风险，因此它是极小极大估计量，尽管对于大多数 $\theta$ 值，$\delta_{2}$ 的风险更低。这表明极小极大估计量过于保守。</div>


最小化最大风险的决策规则称为 **极小极大估计量**（minimax estimator），记作 $\delta_{MM}$。例如，在图 5.9 中，我们看到 $\delta_1$ 在所有可能的 $\theta$ 值上的最坏情况风险低于 $\delta_2$，因此它是极小极大估计量。

极小极大估计量具有一定的吸引力。然而，计算它们可能很困难。而且，它们非常悲观。事实上，可以证明所有极小极大估计量都等价于在最不利先验下的贝叶斯估计量。在大多数统计情境（排除博弈论情境）下，假设自然是对手并非合理假设。

#### 5.3.2 相合估计量

假设我们有一个数据集 $\boldsymbol{x} = \{\boldsymbol{x}_n : n = 1 : N\}$，其中样本 $\boldsymbol{x}_n \in \mathcal{X}$ 由分布 $p(\boldsymbol{x}|\boldsymbol{\theta}^*)$ 独立同分布生成，而 $\boldsymbol{\theta}^* \in \Theta$ 是真实参数。此外，假设参数是 **可识别的**（identifiable），这意味着对于任何数据集 $\boldsymbol{x}$，$p(\boldsymbol{x}|\boldsymbol{\theta}) = p(\boldsymbol{x}|\boldsymbol{\theta}')$ 当且仅当 $\boldsymbol{\theta} = \boldsymbol{\theta}'$。那么，我们说一个估计量 $\delta : \mathcal{X}^N \to \Theta$ 是 **相合估计量**（consistent estimator），如果当 $N \to \infty$ 时 $\hat{\boldsymbol{\theta}}(\boldsymbol{x}) \to \boldsymbol{\theta}^*$（这里的箭头表示依概率收敛）。换句话说，过程 $\delta$ 在数据无限时恢复出真实参数（或其子集）。这等价于最小化 0-1 损失 $\mathcal{L}(\boldsymbol{\theta}^*, \hat{\boldsymbol{\theta}}) = \mathbb{I}\left(\boldsymbol{\theta}^* \neq \hat{\boldsymbol{\theta}}\right)$。一个相合估计量的例子是最大似然估计（MLE）。

注意，一个估计量可以是无偏但不一致的。例如，考虑估计量 $\delta(\boldsymbol{x}) = \delta(\{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_N\}) = \boldsymbol{x}_N$。这是真实均值 $\boldsymbol{\mu}$ 的无偏估计量，因为 $\mathbb{E}[\delta(\boldsymbol{x})] = \mathbb{E}[\boldsymbol{x}_N] = \boldsymbol{\mu}$。但 $\delta(\boldsymbol{x})$ 的抽样分布不收敛于固定值，因此它无法收敛到点 $\boldsymbol{\theta}^*$。

尽管相合性是一个理想的性质，但在实践中其用处有限，因为大多数真实数据集并非来自我们选择的模型族（即不存在 $\theta^*$ 使得 $p(\cdot|\theta^*)$ 生成观测数据 $\mathbf{x}$）。在实践中，更有用的是寻找能够最小化经验分布与估计分布之间某种差异度量的估计量。如果我们使用 KL 散度作为差异度量，那么我们的估计就变为 MLE。

#### 5.3.3 容许估计量

如果对于所有 $\boldsymbol{\theta}$ 都有 $R(\boldsymbol{\theta}, \delta_1) \leq R(\boldsymbol{\theta}, \delta_2)$，则称 $\delta_1$ 支配 $\delta_2$。如果对于某个 $\boldsymbol{\theta}^*$ 该不等式是严格的，则称这种支配是严格的。如果一个估计量不被任何其他估计量严格支配，则称其为 **容许的**（admissible）。有趣的是，[Wal47] 证明，在某些技术条件下，所有容许决策规则都等价于某种贝叶斯决策规则。（参见 [DR21]）

---

（关于该结果的更一般版本。）

例如，在图 5.8 中，我们看到样本中位数（红色虚线）的风险始终高于样本均值（蓝色实线）。因此，样本中位数不是均值的 **可容许估计量**。更令人惊讶的是，可以证明即使在高斯似然模型和平方误差损失下，样本均值也不总是可容许的（这被称为斯坦因悖论 [Ste56]）。

然而，可容许性这一概念的价值有限。例如，设 \( X \sim \mathcal{N}(\theta, 1) \)，并在平方损失下估计 \( \theta \)。考虑估计量 \( \delta_1(x) = \theta_0 \)，其中 \( \theta_0 \) 是一个与数据无关的常数。我们接下来将证明这是一个可容许估计量。

为证明这一点，假设假设不成立。那么存在另一个估计量 \( \delta_2 \) 具有更小的风险，即 \( R(\theta^*, \delta_2) \leq R(\theta^*, \delta_1) \)，且不等式对某个 \( \theta^* \) 严格成立。考虑 \( \theta^* = \theta_0 \) 处的风险。我们有 \( R(\theta_0, \delta_1) = 0 \)，且

$$ R(\theta_{0},\delta_{2})=\int(\delta_{2}(x)-\theta_{0})^{2}p(x|\theta_{0})d x \tag*{(5.77)}$$

由于对所有 \( \theta^{*} \) 有 \( 0 \leq R(\theta^{*},\delta_{2}) \leq R(\theta^{*},\delta_{1}) \)，且 \( R(\theta_{0},\delta_{1}) = 0 \)，因此 \( R(\theta_{0},\delta_{2}) = 0 \)，从而 \( \delta_{2}(x) = \theta_{0} = \delta_{1}(x) \)。因此，能避免在 \( \theta_{0} \) 处风险高于 \( \delta_{1} \) 的唯一方式是 \( \delta_{2} \) 与 \( \delta_{1} \) 相等。故不存在另一个严格风险更低的估计量 \( \delta_{2} \)，所以 \( \delta_{2} \) 是可容许的。

由此可见，估计量 \( \delta_1(x) = \theta_0 \) 是可容许的，尽管它忽略了数据，因此作为一个估计量毫无用处。反之，也有可能构造出有用但不可容许的估计量（例如，参见 [Jay03, 第13.7节]）。

### 5.4 经验风险最小化

本节我们考虑如何在监督学习中应用频率派决策理论。

#### 5.4.1 经验风险

在统计学教材常用的频率派决策理论标准叙述中，存在一个单一的未知“自然状态”，对应于某个模型的未知参数 \( \theta^* \)，我们按式 (5.64) 定义风险，即 \( R(\delta, \theta^*) = \mathbb{E}_{p(\mathcal{D} | \theta^*)} [\ell(\theta^*, \delta(\mathcal{D}))] \)。

在监督学习中，对于每个输入 x 都有一个不同的未知自然状态（即输出 y），我们的估计量 \( \delta \) 是一个预测函数 \( \hat{y} = f(\boldsymbol{x}) \)，而自然状态则是真实分布 \( p^{*}(\boldsymbol{x}, \boldsymbol{y}) \)。因此，估计量的风险如下：

$$ R(f,p^{*})=R(f)\triangleq\mathbb{E}_{p^{*}(\pmb{x})p^{*}(\pmb{y}|\pmb{x})}\left[\ell(\pmb{y},f(\pmb{x})\right] \tag*{(5.78)}$$

这被称为 **总体风险**，因为期望是对真实联合分布 \( p^{*}(\mathbf{x}, \mathbf{y}) \) 取的。当然，\( p^{*} \) 是未知的，但我们可以利用具有 N 个样本的经验分布来近似它：

$$ p_{\mathcal{D}}(\boldsymbol{x},\boldsymbol{y}|\mathcal{D})\triangleq\frac{1}{|\mathcal{D}|}\sum_{(\boldsymbol{x}_{n},\boldsymbol{y}_{n})\in\mathcal{D}}\delta(\boldsymbol{x}-\boldsymbol{x}_{n})\delta(\boldsymbol{y}-\boldsymbol{y}_{n}) \tag*{(5.79)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

其中 $p_{\mathcal{D}}(\boldsymbol{x}, \boldsymbol{y}) = p_{\mathrm{tr}}(\boldsymbol{x}, \boldsymbol{y})$。代入得到经验风险：

$$ R(f,\mathcal{D})\triangleq\mathbb{E}_{p_{\mathcal{D}}(\boldsymbol{x},\boldsymbol{y})}\left[\ell(\boldsymbol{y},f(\boldsymbol{x})\right]=\frac{1}{N}\sum_{n=1}^{N}\ell(\boldsymbol{y}_{n},f(\boldsymbol{x}_{n})) \tag*{(5.80)}$$

注意 $R(f,\mathcal{D})$ 是一个随机变量，因为它依赖于训练集。

一种自然的选择预测器的方法是使用

$$ \hat{f}_{\mathrm{E R M}}=\underset{f\in\mathcal{H}}{\mathrm{a r g m i n}}R(f,\mathcal{D})=\underset{f\in\mathcal{H}}{\mathrm{a r g m i n}}\frac{1}{N}\sum_{n=1}^{N}\ell(\boldsymbol{y}_{n},f(\boldsymbol{x}_{n})) \tag*{(5.81)}$$

其中我们在特定的假设空间 $\mathcal{H}$ 上优化函数类。这被称为经验风险最小化（Empirical Risk Minimization, ERM）。

##### 5.4.1.1 近似误差与估计误差

本节中，我们分析使用 ERM 原则拟合函数的理论性能。令 $f^{**} = \argmin_f R(f)$ 为达到最小可能总体风险的函数，其中我们在所有可能的函数上优化。当然，我们无法考虑所有可能的函数，因此我们定义 $f^*_\mathcal{H} = \argmin_{f \in \mathcal{H}} R(f)$ 为假设空间 $\mathcal{H}$ 中的最佳函数。不幸的是，我们无法计算 $f^*_\mathcal{H}$，因为无法计算总体风险，所以最后我们定义给定固定训练集 $\mathcal{D}$ 时，在假设空间中最小化经验风险的预测函数：

$$ f_{\mathcal{D}}^{*}=\underset{f\in\mathcal{H}}{\operatorname{argmin}}R(f,\mathcal{D}) \tag*{(5.82)}$$

这是一个随机函数，因为 $\mathcal{D} \sim p^*$ 是随机的。

通过加减项，我们可以证明所选预测器的期望风险与最佳可能预测器相比可以被分解为两项，如下所示：

$$ \mathbb{E}_{\mathcal{D}\sim p^{*}}\left[R(f_{\mathcal{D}}^{*})-R(f^{**})\right]=\underbrace{R(f_{\mathcal{H}}^{*})-R(f^{**})}_{\mathcal{E}_{\mathrm{app}}(\mathcal{H})}+\underbrace{\mathbb{E}_{\mathcal{D}\sim p^{*}}\left[R(f_{\mathcal{D}}^{*})-R(f_{\mathcal{H}}^{*})\right]}_{\mathcal{E}_{\mathrm{est}}(\mathcal{H},N)} \tag*{(5.83)}$$

第一项 $\mathcal{E}_{\mathrm{app}}(\mathcal{H})$ 为近似误差，衡量 $f_{\mathcal{H}}^{*}$ 能够多好地建模真实最优函数 $f^{**}$。第二项 $\mathcal{E}_{\mathrm{est}}(\mathcal{H}, N)$ 为估计误差，衡量由于使用规模为 $N$ 的有限训练集评估性能而导致的在该类中寻找最佳函数的误差。（也可以研究训练过程引入的额外误差[BB08]。）

我们可以通过使用更具表达能力的函数族 $\mathcal{H}$ 来减小近似误差。然而，这通常会增加过拟合，从而增加估计误差。我们可以通过计算泛化差距（generalization gap）来量化任意模型 $f$ 的过拟合程度，其定义如下：

$$ \mathrm{GenGap}(f)=R(f)-R(f,\mathcal{D}_{\mathrm{train}})\approx R(f,\mathcal{D}_{\mathrm{test}})-R(f,\mathcal{D}_{\mathrm{train}}) \tag*{(5.84)}$$

因此，我们需要找到权衡近似误差和估计误差的模型。下面我们讨论这种权衡的解决方案。

---

##### 5.4.1.2 正则化风险

为避免过拟合，通常会在目标函数中添加复杂度惩罚项，从而得到正则化经验风险：

$$  R_{\lambda}(f,\mathcal{D})=R(f,\mathcal{D})+\lambda C(f)   \tag*{(5.85)}$$

其中 $C(f)$ 衡量预测函数 $f(\boldsymbol{x};\boldsymbol{\theta})$ 的复杂度，$\lambda\geq0$ 是一个超参数，控制复杂度惩罚的强度。（我们在5.4.2节讨论如何选择 $\lambda$。）

在实践中，我们通常使用参数化函数，并将正则化器应用于参数本身。这得到了如下形式的目标函数：

$$  R_{\lambda}(\boldsymbol{\theta},\mathcal{D})=R(\boldsymbol{\theta},\mathcal{D})+\lambda C(\boldsymbol{\theta})   \tag*{(5.86)}$$

注意，如果损失函数为对数损失，且正则化器为负对数先验，则正则化风险为：

$$  R_{\lambda}(\boldsymbol{\theta},\mathcal{D})=-\frac{1}{N}\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})-\lambda\log p(\boldsymbol{\theta})   \tag*{(5.87)}$$

最小化该式等价于 MAP 估计。

#### 5.4.2 结构风险

估计超参数的一种自然方式是通过最小化可达到的经验风险：

$$  \hat{\lambda}=\underset{\lambda}{\operatorname{a r g m i n}}\underset{\theta}{\operatorname{m i n}}R_{\lambda}(\boldsymbol{\theta},\mathcal{D})   \tag*{(5.88)}$$

（这是双层优化（也称为嵌套优化）的一个示例。）不幸的是，这种方法无法奏效，因为它总是会选择最小的正则化量，即 $\hat{\lambda} = 0$。为了理解这一点，请注意：

$$  \underset{\lambda}{\operatorname{argmin}}\underset{\theta}{\min}R_{\lambda}(\boldsymbol{\theta},\mathcal{D})=\underset{\lambda}{\operatorname{argmin}}\underset{\theta}{\min}R(\boldsymbol{\theta},\mathcal{D})+\lambda C(\boldsymbol{\theta})   \tag*{(5.89)}$$

该式通过设置 $\lambda = 0$ 达到最小化。问题在于经验风险低估了总体风险，导致我们在选择 $\lambda$ 时出现过拟合。这被称为训练误差的乐观性。

如果我们知道正则化总体风险 $R_{\lambda}(\boldsymbol{\theta})$ 而非正则化经验风险 $R_{\lambda}(\boldsymbol{\theta},\mathcal{D})$，就可以用它来选择具有正确复杂度的模型（例如 $\lambda$ 的值）。这被称为结构风险最小化 [Vap98]。对于给定的模型（$\lambda$ 的值），有两种主要方式估计总体风险，即交叉验证（5.4.3节）和统计学习理论（5.4.4节），我们将在下文讨论。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

#### 5.4.3 交叉验证

在本节中，我们讨论一种估计监督学习场景下总体风险的简单方法。我们将数据集简单地划分为两部分：一部分用于训练模型，另一部分称为验证集或留出集，用于评估风险。我们可以在训练集上拟合模型，并将其在验证集上的性能作为总体风险的近似。

为了更详细地解释该方法，我们需要一些符号。首先，我们将经验风险对数据集的依赖关系明确表示为：

$$ R_{\lambda}(\boldsymbol{\theta},\mathcal{D})=\frac{1}{|\mathcal{D}|}\sum_{(\mathbf{x},\mathbf{y})\in\mathcal{D}}\ell(\mathbf{y},f(\mathbf{x};\boldsymbol{\theta}))+\lambda C(\boldsymbol{\theta}) \tag*{(5.90)}$$

我们还定义 $\hat{\boldsymbol{\theta}}_{\lambda}(\mathcal{D}) = \argmin_{\boldsymbol{\theta}} R_{\lambda}(\mathcal{D}, \boldsymbol{\theta})$。最后，令 $\mathcal{D}_{\text{train}}$ 和 $\mathcal{D}_{\text{valid}}$ 是 $\mathcal{D}$ 的一个划分（通常我们使用约80%的数据作为训练集，20%作为验证集）。

对于每个模型 $\lambda$，我们在训练集上拟合它得到 $\boldsymbol{\theta}_{\lambda}(\mathcal{D}_{\mathrm{train}})$。然后，我们使用验证集上的无正则化经验风险作为总体风险的估计。这被称为验证风险：

$$ R_{\lambda}^{\mathrm{v a l}}\triangleq R_{0}(\hat{\pmb{\theta}}_{\lambda}(\mathcal{D}_{\mathrm{t r a i n}}),\mathcal{D}_{\mathrm{v a l i d}}) \tag*{(5.91)}$$

注意，我们使用不同的数据来训练和评估模型。

上述技术可能效果良好。然而，当训练样本数量较少时，该技术会遇到问题，因为模型没有足够的数据进行训练，我们也缺乏足够的数据来可靠地估计未来性能。

一种简单但流行的解决方案是使用交叉验证（CV）。其思路如下：我们将训练数据分成 $K$ 折；然后，对于每一折 $k \in \{1, \ldots, K\}$，我们在除第 $k$ 折之外的所有折上训练，并在第 $k$ 折上测试，以循环方式进行，如图4.6所示。形式上，我们有

$$ R_{\lambda}^{\mathrm{c v}}\triangleq\frac{1}{K}\sum_{k=1}^{K}R_{0}(\hat{\boldsymbol{\theta}}_{\lambda}(\mathcal{D}_{-k}),\mathcal{D}_{k}) \tag*{(5.92)}$$

其中 $\mathcal{D}_k$ 是第 $k$ 折的数据，$\mathcal{D}_{-k}$ 是所有其他数据。这被称为交叉验证风险。图4.6展示了 $K=5$ 时的过程。如果设定 $K=N$，我们得到一种称为留一法交叉验证的方法，因为我们总是在 $N-1$ 个样本上训练，并在剩余的一个样本上测试。

我们可以将交叉验证估计值作为优化过程中的目标函数，以选择最优超参数：$\hat{\lambda} = \argmin_{\lambda} R_{\lambda}^{cv}$。最后，我们合并所有可用数据（训练集和验证集），并使用 $\hat{\pmb{\theta}} = \argmin_{\pmb{\theta}} R_{\hat{\lambda}}(\pmb{\theta}, \pmb{\mathcal{D}})$ 重新估计模型参数。

#### 5.4.4 统计学习理论 *

交叉验证的主要问题是速度慢，因为我们需要多次拟合模型。这激发了计算总体风险的解析近似或上界的需求。这一研究领域属于统计学习理论（SLT）（例如，参见 [Vap98]）。

---

更精确地说，统计学习理论（SLT）的目标是以一定的概率给出泛化误差的上界。如果该界成立，那么我们有理由相信，通过最小化经验风险所选择的假设将具有较低的整体风险。对于二元分类器而言，这意味着该假设将做出正确的预测；在这种情况下，我们称其为**可能近似正确**，并且该假设类是**PAC可学习**的（详见例如[KV94]）。

##### 5.4.4.1 泛化误差的界定

在本节中，我们建立条件，使得能够证明一个假设类是PAC可学习的。首先考虑假设空间有限的情况，其大小为 \( \dim(\mathcal{H}) = |\mathcal{H}| \)。换言之，我们从一个有限列表中选取假设，而非优化实值参数。在这种情况下，我们可以证明如下定理。

**定理 5.4.1.** 对于任意数据分布 \( p^{*} \) 以及从中抽取的大小为 \( N \) 的数据集 \( \mathcal{D} \)，在最坏情况下，二元分类器的泛化误差超过 \( \epsilon \) 的概率上界为：

$$ P\left(\max_{h\in\mathcal{H}}|R(h)-R(h,\mathcal{D})|>\epsilon\right) \leq 2\dim(\mathcal{H}) e^{-2N\epsilon^{2}} \tag*{(5.93)} $$

其中 \( R(h,\mathcal{D}) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}(f(\boldsymbol{x}_i) \neq y_i) \) 是经验风险，而 \( R(h) = \mathbb{E} \left[ \mathbb{I}(f(\boldsymbol{x}) \neq y^*) \right] \) 是整体风险。

**证明.** 在证明之前，我们介绍两个有用的结果。首先，**霍夫丁不等式**（Hoeffding's inequality）：若 \( E_1, \ldots, E_N \sim \text{Ber}(\theta) \)，则对任意 \( \epsilon > 0 \) 有

$$ P(|\overline{E} - \theta| > \epsilon) \leq 2 e^{-2N\epsilon^{2}} \tag*{(5.94)} $$

其中 \( \overline{E} = \frac{1}{N} \sum_{i=1}^{N} E_i \) 是经验错误率，\( \theta \) 是真实错误率。其次，**联合界**（union bound）：若 \( A_1, \ldots, A_d \) 是一组事件，则 \( P(\bigcup_{i=1}^{d} A_i) \leq \sum_{i=1}^{d} P(A_i) \)。利用这些结果，我们有

$$ P\left(\max_{h\in\mathcal{H}}|R(h)-R(h,\mathcal{D})|>\epsilon\right) = P\left(\bigcup_{h\in\mathcal{H}} |R(h)-R(h,\mathcal{D})| > \epsilon\right) \tag*{(5.95)} $$

$$ \leq \sum_{h\in\mathcal{H}} P\left( \left|R(h)-R(h,\mathcal{D})\right| > \epsilon \right) \tag*{(5.96)} $$

$$ \leq \sum_{h\in\mathcal{H}} 2 e^{-2N\epsilon^{2}} = 2\dim(\mathcal{H}) e^{-2N\epsilon^{2}} \tag*{(5.97)} $$

该界表明，训练误差的乐观程度随 \( \dim(\mathcal{H}) \) 增大而增大，随 \( N = |\mathcal{D}| \) 增大而减小，这符合预期。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND许可证

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_293_117_471_267.jpg" alt="图像" width="15%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_706_122_880_264.jpg" alt="图像" width="15%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图5.10: (a) Neyman-Pearson假设检验范式的示意图。由neyman-Pearson2.ipynb生成。 (b) 两个假想的双边功效曲线。B占优于A。改编自[LM86]的图6.3.5。由twoPowerCurves.ipynb生成。</div>


##### 5.4.4.2 VC维

如果假设空间 $\mathcal{H}$ 是无限的（例如，我们有实值参数），则不能使用 $\dim(\mathcal{H}) = |\mathcal{H}|$。相反，我们可以使用一个称为假设类的 $\mathbf{VC}$ 维的量，以 Vapnik 和 Chervonenkis 命名；它衡量假设类的自由度（有效参数数量）。详细信息请参见 [Vap98]。

不幸的是，对于许多有趣的模型，计算VC维是困难的，并且上界通常非常宽松，使得这种方法实际价值有限。然而，最近已经设计出各种其他更实用的泛化误差估计方法，特别是针对深度神经网络，例如 [Jia+20]。

### 5.5 频率学派假设检验 *

在本节中，我们讨论根据数据D判断一个假设（模型）是否可能成立的方法。

#### 5.5.1 似然比检验

在决定一个模型是否很好地描述了某些数据时，总是要问“相对于什么”。具体来说，假设我们有两个假设，称为零假设 $H_0$ 和备择假设 $H_1$，我们想要选择我们认为更可能的一个。这可以看作是一个二分类问题，其中 $H \in \{0, 1\}$ 表示“真实”模型的身份。一种自然的方法是使用贝叶斯模型选择，如我们在第5.2.1节所讨论的，计算 $p(H|\mathcal{D})$，然后选择最可能的模型。这里我们讨论一种频率学派的方法。

假设我们有一个均匀先验，因此 $p(H=0)=p(H=1)=0.5$，并且我们使用0-1损失。那么最优决策规则是接受 $H_0$ 当且仅当 $\frac{p(\mathcal{D}|H_0)}{p(\mathcal{D}|H_1)}>1$。这称为似然比检验。下面我们给出一些例子。

##### 5.5.1.1 示例：比较高斯均值

假设我们感兴趣的是检验某些数据是来自均值为 $\mu_0$ 的高斯分布还是均值为 $\mu_1$ 的高斯分布。（我们假设已知共同的方差 $\sigma^2$）。这如图...所示。

---

图5.10a中，我们绘制了 $p(x|H_0)$ 和 $p(x|H_1)$。可以推导似然比如下：

$$  \underline{p(\mathcal{D}|H_{0})}\underline{\quad}=\frac{\exp\left(-\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}(x_{n}-\mu_{0})^{2}\right)}{}   \tag*{(5.98)}$$

 $$ p(\mathcal{D}|H_{1})\quad\overline{\quad}\exp\left(-\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}(x_{n}-\mu_{1})^{2}\right) $$ 

$$  =\exp\left(\frac{1}{2\sigma^{2}}(2N\overline{x}(\mu_{0}-\mu_{1})+N\mu_{1}^{2}-N\mu_{0}^{2})\right)   \tag*{(5.99)}$$

我们看到，该比值仅通过其均值 $\overline{x}$ 依赖于观测数据。从图5.10a可以看出，$\frac{p(\mathcal{D}|H_0)}{p(\mathcal{D}|H_1)} > 1$ 当且仅当 $\overline{x} < x^*$，其中 $x^*$ 是两个概率密度函数相交的点（假设该点唯一）。

##### 5.5.1.2 简单假设与复合假设

在5.5.1.1节中，原假设和备择假设的参数要么被完全指定（$\mu_0$ 和 $\mu_1$），要么是共享的（$\sigma^2$）。这被称为简单假设检验。一般而言，一个假设可能并未完全指定所有参数；这被称为复合假设。在这种情况下，我们可以像贝叶斯方法那样对这些未知参数进行积分，因为具有更多参数的假设总是具有更高的似然性。然而，这在计算上可能很困难，并且容易因先验设定不当而出现问题。作为一种替代方法，我们可以“最大化”这些参数，从而得到最大似然比检验：

$$  \frac{p(H_{0}|\mathcal{D})}{p(H_{1}|\mathcal{D})}=\frac{\int_{\boldsymbol{\theta}\in H_{0}}p(\boldsymbol{\theta})p_{\boldsymbol{\theta}}(\mathcal{D})}{\int_{\boldsymbol{\theta}\in H_{1}}p(\boldsymbol{\theta})p_{\boldsymbol{\theta}}(\mathcal{D})}\approx\frac{\max_{\boldsymbol{\theta}\in H_{0}}p_{\boldsymbol{\theta}}(\mathcal{D})}{\max_{\boldsymbol{\theta}\in H_{1}}p_{\boldsymbol{\theta}}(\mathcal{D})}   \tag*{(5.100)}$$

#### 5.5.2 第一类错误与第二类错误及 Neyman-Pearson 引理

假设检验是一种二元分类问题。正如我们在5.1.3节中讨论的，可能犯两种错误，分别称为**假阳性**或**第一类错误**，即当原假设为真时错误地接受备择假设（即 $p(\hat{H}=1|H=0)$）；以及**假阴性**或**第二类错误**，即当备择假设为真时错误地接受原假设（即 $p(\hat{H}=0|H=1)$）。第一类错误率 $\alpha$ 称为检验的**显著性水平**。在我们的高斯均值示例中，从图5.10a可以看出，第一类错误率为垂直蓝色阴影区域：

$$  \alpha(\mu_{0})=p(\text{第一类错误})=p(\text{拒绝}H_{0}|H_{0}\text{为真})   \tag*{(5.101)}$$

$$  =p(\overline{X}(\tilde{\mathcal{D}})>x^{*}|\tilde{\mathcal{D}}\sim H_{0})   \tag*{(5.102)}$$

$$  =p\left(\frac{\overline{X}-\mu_{0}}{\sigma/\sqrt{N}}>\frac{x^{*}-\mu_{0}}{\sigma/\sqrt{N}}\right)   \tag*{(5.103)}$$

因此，$x^* = z_\alpha \sigma / \sqrt{N} + \mu_0$，其中 $z_\alpha$ 是标准正态分布的上 $\alpha$ 分位数。第二类错误率记为 $\beta$，由下式给出：

$$  \beta(\mu_{1})=p(\text{第二类错误})=p(\text{接受}H_{0}|H_{1}\text{为真})=p(\overline{X}(\tilde{\mathcal{D}})<x^{*}|\tilde{\mathcal{D}}\sim H_{1})   \tag*{(5.104)}$$

这在图5.10a中由水平红色阴影区域表示。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可。

---

我们将检验的势定义为 $1 - \beta(\mu_1)$；这是在 $H_1$ 为真的条件下拒绝 $H_0$ 的概率（即 $p(\hat{H} = 1|H = 1)$，也就是真正例率）。换句话说，它是指正确识别零假设错误的能力。显然，当 $\mu_1 = \mu_0$ 时势最小（此时曲线重叠），此时 $1 - \beta(\mu_1) = \alpha(\mu_0)$。随着 $\mu_1$ 与 $\mu_0$ 之间的距离增大，势趋近于 1（因为红色阴影区域变小，$\beta \to 0$）。若我们有两个检验 $A$ 和 $B$，在相同的第 I 类错误率下，满足 power$(B) \geq$ power$(A)$，则称 $B$ 优于 $A$。见图 5.10b。在所有显著性水平为 $\alpha$ 的检验中，在 $H_1$ 下具有最高势的检验称为**最优势检验**。结果证明，似然比检验是一个最优势检验，这一结论被称为 Neyman-Pearson 引理。

#### 5.5.3 零假设显著性检验（NHST）与 p 值

在上述决策理论（或 Neyman-Pearson）的假设检验方法中，我们需要指定一个零假设 $H_0$ 和一个备择假设 $H_1$，以便计算 $p(\mathcal{D}|H_0)$ 和 $p(\mathcal{D}|H_1)$。但在某些情况下，很难定义备择假设，我们只想检验给定数据下某个简单零假设是否“合理”。为此，我们可以定义一个检验统计量 test$(\mathcal{D})$，然后将其观测值与数据来自零假设时的期望值（即 $\mathcal{D} \sim H_0$ 下的 test$(\mathcal{D})$）进行比较。如果观测值在 $H_0$ 下显得反常，我们就拒绝零假设。为了量化这一点，我们计算在零假设下观测到与已观测值一样大或更大检验统计值的概率（假设更大的值使 $H_1$ 更可能成立）。更精确地，我们将 p 值定义为在零假设下观测到等于或大于实际观测值的检验统计量的概率：

$$ \operatorname{pval}\triangleq\operatorname{Pr}(\operatorname{test}(\tilde{\mathcal{D}})\geq\operatorname{test}(\mathcal{D})|\tilde{\mathcal{D}}\sim H_{0}) \tag*{(5.105)}$$

换句话说，pval ≃ Pr(test_null ≥ test_obs)，其中 test_obs = test(ℛ)，test_null = test(ℛ)，ℛ ~ H₀ 表示假设的未来数据。p 值越小，表明反对 H₀ 的证据越强。

传统上，若 p 值小于 $\alpha = 0.05$，我们便拒绝零假设；这称为检验的显著性水平，整个过程称为零假设显著性检验或 NHST。根据构造，此类检验的第 I 类错误率（错误拒绝真实零假设）为 $\alpha$。注意，该决策规则对应于选取决策阈值 $t^*$ 使得 $\Pr(\text{test}(\widehat{\mathcal{D}}) \geq t^* | H_0) = \alpha$。若令 $t^* = \text{test}(\mathcal{D})$，则 $\alpha$ 将等于观测到的 p 值。因此，p 值是能拒绝 $H_0$ 的最小 $\alpha$ 值。

我们可以通过 pval = 1 - Φ(test(D)) 计算 p 值，其中 Φ 是检验统计量抽样分布的累积分布函数。这称为单侧 p 值。在某些情况下，使用双侧 p 值更为合适，其形式为 pval = Pr(test(D) ≥ test(D) | D ~ H₀) + Pr(test(D) ≤ -test(D) | D ~ H₀)，这里假设 test(D) ≥ 0。例如，假设我们使用 test(D) = (θ̂(D) - θ₀) / sθ̂(D)，其中 θ₀ 是 H₀ 下 θ* 的值，θ̂ 是最大似然估计（MLE）；这称为 Wald 统计量。根据第 4.7.2 节讨论的 MLE 渐近正态性，可得 pval = Pr(|test(D)| > |test(D)| | H₀) ≈ Pr(|Z| > |test(D)|) = 2Φ(|test(D)|)，其中 Z ∼ N(0, 1)。

由此可见，要计算 p 值，我们需要知道零假设下检验统计量的抽样分布。假设我们要比较经验分布（或结果）与期望（理论）分布（或结果）。在某些情况下，我们可以使用大样本（高斯近似）来逼近抽样分布，如上所述。若不能，则可使用非参数自助法逼近。另一个重要情形出现在当我们想要比较

---

要检验两个经验分布是否相同，我们可以使用非参数置换检验，该方法不对分布做任何假设。例如，假设我们有来自 $P_X$ 的 $m$ 个样本 $X_i$ 和来自 $P_Y$ 的 $n$ 个样本 $Y_i$，原假设为 $P_x = P_y$。定义检验统计量 $\text{test}(X_1, \ldots, X_m, Y_1, \ldots, Y_n) = |\overline{X} - \overline{Y}|$。如果对样本顺序进行置换，则在 $H_0$ 下，该统计量应保持不变。因此，我们可以通过随机抽取置换来近似 $p(\text{test}(\overline{D})|\overline{D} \sim H_0)$，进而计算出使用未打乱数据计算得到的 $\text{test}(\overline{D})$ 的尾部概率。更多细节可参见 [Was04, p162]。

请注意，p 值为 0.05 并不意味着备择假设 $H_1$ 为真的概率是 0.95。事实上，即使是大多数科学家也会误解 p 值。$^4$ 大多数人真正想计算的是贝叶斯后验概率 $p(H|\mathcal{D})$。关于这一重要区分的更多内容，请参见第 5.5.4 节。

#### 5.5.4 p 值是有害的

p 值常被解释为数据在原假设下出现的可能性，因此较小的 p 值被认为意味着 $H_0$ 不太可能成立，从而 $H_1$ 更可能成立。其推理大致如下：

如果 $H_0$ 为真，那么该检验统计量很可能不会出现。而该统计量出现了。因此，$H_0$ 很可能为假。

然而，这种推理是无效的。要理解其原因，请看以下例子（来自 [Coh94]）：

如果一个人是美国人，那么他很可能不是国会议员。这个人是国会议员。因此他很可能不是美国人。

这显然是错误的推理。相比之下，以下逻辑论证是有效的：

如果一个人是火星人，那么他不是国会议员。这个人是国会议员。因此他不是火星人。

这两种情况的区别在于，火星人的例子使用的是**演绎推理**，即从逻辑定义向前推导出结论。更准确地说，这个例子使用了逻辑学中称为**拒取式**的规则：我们从 $P \Rightarrow Q$ 这样的定义出发；当观察到 $\neg Q$ 时，我们可以得出 $\neg P$。相反，美国人的例子涉及的是**归纳推理**，即利用统计规律（而非逻辑定义）从观察到的证据向后推导出可能的（但不一定是必然的）原因。

要进行归纳推理，我们需要使用概率推断（详见 $[Jay03]$）。特别地，要计算原假设的概率，我们应该使用贝叶斯法则，如下所示：

$$  p(H_{0}|\mathcal{D})=\frac{p(\mathcal{D}|H_{0})p(H_{0})}{p(\mathcal{D}|H_{0})p(H_{0})+p(\mathcal{D}|H_{1})p(H_{1})}   \tag*{(5.106)}$$

如果先验是均匀的，即 $p(H_0) = p(H_1) = 0.5$，那么上式可以用似然比 $LR = p(\mathcal{D}|H_0)/p(\mathcal{D}|H_1)$ 改写为：

$$  p(H_{0}|\mathcal{D})=\frac{LR}{LR+1}   \tag*{(5.107)}$$

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>无效</td><td style='text-align: center; word-wrap: break-word;'>有效</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“不显著”</td><td style='text-align: center; word-wrap: break-word;'>171</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>175</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>“显著”</td><td style='text-align: center; word-wrap: break-word;'>9</td><td style='text-align: center; word-wrap: break-word;'>16</td><td style='text-align: center; word-wrap: break-word;'>25</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>180</td><td style='text-align: center; word-wrap: break-word;'>20</td><td style='text-align: center; word-wrap: break-word;'>200</td></tr></table>

<div style="text-align: center;">表 5.8：一项假设性临床试验的若干统计数据。来源：[SAM04, p74]。</div>

在美国国会例子中，$\mathcal{D}$ 是观察到该人士为国会议员这一事实。零假设 $H_0$ 是该人士是美国人，备择假设 $H_1$ 是该人士不是美国人。我们假设 $p(\mathcal{D}|H_0)$ 很低，因为大多数美国人并非国会议员。然而，$p(\mathcal{D}|H_1)$ 也很低——事实上，在这个例子中它为 0，因为只有美国人才能成为国会议员。因此 $LR = \infty$，所以 $p(H_0|D) = 1.0$，这与直觉相符。但请注意，NHST 忽略了 $p(\mathcal{D}|H_1)$ 以及先验 $p(H_0)$，因此它给出了错误的结果——不仅在这个问题中，而且在许多问题中都是如此。

一般来说，p 值与 $p(H_0|\mathcal{D})$ 之间可能存在巨大差异。特别地，[SBB01] 表明，即使 p 值低至 0.05，$H_0$ 的后验概率也可能高达 30% 甚至更高，即使使用均匀先验也是如此。

考虑来自 [SAM04, p74] 的这个具体实例。假设对某种药物进行了 200 项临床试验，我们得到了表 5.8 中的数据。假设我们对该药物是否具有显著效果进行了统计检验。该检验的第一类错误率为 $\alpha = 9/180 = 0.05$，第二类错误率为 $\beta = 4/20 = 0.2$。

我们可以计算在结果被声称“显著”的情况下，药物无效的概率，如下所示：

$$  p(H_{0}|^{\prime}significant^{\prime})=\frac{p(^{\prime}significant^{\prime}|H_{0})p(H_{0})}{p(^{\prime}significant^{\prime}|H_{0})p(H_{0})+p(^{\prime}significant^{\prime}|H_{1})p(H_{1})}   \tag*{(5.108)}$$

$$  \underline{{\phantom{x}}}\qquad\qquad p(\mathrm{第一类错误})p(H_{0})   \tag*{(5.109)}$$

 $$ p(\mathrm{第一类错误})p(H_{0})+(1-p(\mathrm{第二类错误}))p(H_{1}) $$ 

$$  =\frac{\alpha p(H_{0})}{\alpha p(H_{0})+(1-\beta)p(H_{1})}   \tag*{(5.110)}$$

如果我们基于过去的经验拥有先验知识，即大多数（例如 90%）药物无效，那么我们会发现 $p(H_0|\text{significant}) = 0.36$，这远高于人们通常与 $\alpha = 0.05$ 的 p 值相关联的 5% 概率。

因此，如果统计显著性的主张违背了我们的先验知识，我们应当对其持怀疑态度。

#### 5.5.5 为什么不是每个人都采用贝叶斯方法？

在第 4.7.5 节和第 5.5.4 节中，我们已经看到，基于频率主义原理的推理可能会表现出各种反直觉的行为，有时甚至会违反常识推理，这一点已在多篇文章中被指出（例如，参见 [Mat98; MS11; Kru13; Gel16; Hoe14; Lyu15; Cha16b; Cla21]）。

这些问题的根本原因在于，频率主义推理违反了**似然原理** [BW88]，该原理指出推理应基于观测数据的似然性。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_439_118_729_554.jpg" alt="图片" width="25%" /></div>


<div style="text-align: center;">图 5.11：形象说明频率学派与贝叶斯学派差异的漫画。（其中 p < 0.05 的评论将在第 5.5.4 节解释。关于赌博的评论则引用了荷兰赌定理，该定理本质上证明了贝叶斯方法在赌博（及其他决策理论问题）中的最优性，具体可参见例如 [Háj08]。）图片来自 https://zkcd.com/1132/。经 xkcd 作者 Rundall Munroe 友好许可使用。</div>


而非针对你尚未观察到的假设性未来数据。贝叶斯方法显然满足似然原则，因此不会出现这些病态问题。

鉴于频率统计的这些根本缺陷，以及贝叶斯方法不存在此类缺陷的事实，一个显而易见的问题是：“为什么不是每个人都采用贝叶斯方法？”（频率学派）统计学家 Bradley Efron 曾以这个标题撰写了一篇论文 [Efr86]。对于任何对这个话题感兴趣的人来说，他这篇简短的论文非常值得一读。下面我们引用他开篇的一段话：

这个标题之所以合理，至少有两个理由。首先，过去所有人都是贝叶斯学派。拉普拉斯全心全意地支持贝叶斯对推理问题的表述，而大多数 19 世纪的科学家也纷纷效仿。这包括高斯，他的统计工作通常以频率学派的术语呈现。

第二个且更重要的理由是贝叶斯论证的说服力。现代统计学家在 Savage 和 de Finetti 的引领下，提出了支持贝叶斯推断的强有力理论论据。这项工作还附带产生了一个令人不安的频率学派观点中的不一致性清单。

尽管如此，并非所有人都是贝叶斯学派。当前时代（1986 年）是统计学被广泛用于科学报告的第一个世纪，事实上，20 世纪的统计学主要不是贝叶斯学派的。然而，Lindley（1975）预测 21 世纪将发生变化。

时间会证明 Lindley 是否正确。不过，趋势似乎正朝着这个方向发展。

作者：Kevin P. Murphy。 (C) MIT 出版社。CC-BY-NC-ND 许可协议。

---

例如，一些期刊已禁止使用 p 值 [TM15; AGM19]，而由美国统计协会（American Statistical Association）主办的《美国统计学家》（The American Statistician）期刊还出版了一期专刊，警告 p 值和 NHST（零假设显著性检验）的使用 [WSL19]。

传统上，计算一直是使用贝叶斯方法的障碍，但如今由于更快的计算机和更好的算法（我们将在本书的续篇 [Mur23] 中讨论），这一问题已不那么突出。另一个更根本的担忧是，贝叶斯方法的正确性完全取决于其建模假设。然而，这一批评也适用于频率学派方法，因为估计量的抽样分布必须基于对数据生成机制的假设来推导。（事实上，[BT73] 表明，常见模型的 MLE 的抽样分布与非信息先验下的后验分布相同。）幸运的是，我们可以通过交叉验证（第 4.5.5 节）、校准和贝叶斯模型检查来经验性地检验建模假设。我们将在本书的续篇 [Mur23] 中讨论这些主题。

总之，值得引用唐纳德·鲁宾（Donald Rubin）在论文 [Rub84]《贝叶斯可证明且相关的应用统计学家频率计算》（Bayesianly Justifiable and Relevant Frequency Calculations for the Applied Statistician）中写道的：

应用统计学家在原则上应是贝叶斯式的，在实践中则应与现实世界相校准。他们应尝试使用在合理偏离其假设时仍能导致近似校准过程的规范。他们应避免被观测数据以相关方式反驳的模型——针对假设复制的频率计算可以评估模型的充分性，并有助于提出更合适的模型。

### 5.6 习题

##### 习题 5.1 [分类器中的拒绝选项]

（来源：[DHS01, Q2.13].）在许多分类问题中，我们有两种选择：要么将 $ \boldsymbol{x} $ 分配到类别 $ j $，要么在过于不确定时选择拒绝选项。如果拒绝的成本小于错误分类对象的成本，那么拒绝可能是最优行动。设 $ \alpha_i $ 表示选择动作 $ i $，其中 $ i = 1 : C + 1 $，$ C $ 是类别数，$ C + 1 $ 是拒绝动作。设 $ Y = j $ 为真实（但未知）的自然状态。定义损失函数如下：

$$  \lambda(\alpha_{i}|Y=j)=\left\{\begin{array}{cc}0&\text{if}i=j\text{and}i,j\in\{1,\ldots,C\}\\ \lambda_{r}&\text{if}i=C+1\\ \lambda_{s}&\text{otherwise}\end{array}\right.   \tag*{(5.111)}$$

换句话说，如果正确分类，则产生 0 损失；如果选择拒绝选项，则产生 $ \lambda_{r} $ 损失（成本）；如果发生替换错误（错误分类），则产生 $ \lambda_{s} $ 损失（成本）。

a. 证明：当对于所有 $ k $ 有 $ p(Y = j | \boldsymbol{x}) \geq p(Y = k | \boldsymbol{x}) $（即 $ j $ 是最可能的类别），且 $ p(Y = j | \boldsymbol{x}) \geq 1 - \frac{\lambda_r}{\lambda_s} $ 时，我们决定 $ Y = j $ 可获得最小风险；否则决定拒绝。

b. 定性地描述当 $ \lambda_{r}/\lambda_{s} $ 从 0 增加到 1 时（即拒绝的相对成本增加）会发生什么。

##### 习题 5.2 [报童问题 $ \dagger $]

考虑决策论/经济学中的以下经典问题。假设你试图决定购买某种产品（例如报纸）的数量 $ Q $ 以最大化利润。最优数量取决于你认为的产品需求 $ D $，以及你的成本 $ C $ 和售价 $ P $。假设 $ D $ 未知，但其概率密度函数为 $ f(D) $，累积分布函数为 $ F(D) $。我们可以通过考虑两种情况来评估期望利润：如果 $ D > Q $，则我们售出全部 $ Q $ 件商品，获得利润 $ \pi = (P - C)Q $；但如果 $ D < Q $，则

---

我们只销售 D 件商品，获得利润 $(P - C)D$，但在未售出的商品上浪费了 $C(Q - D)$。因此，如果订购数量为 Q，期望利润为

$$ E\pi(Q)=\int_{Q}^{\infty}(P-C)Qf(D)dD+\int_{0}^{Q}(P-C)Df(D)dD-\int_{0}^{Q}C(Q-D)f(D)dD \tag*{(5.112)}$$

简化该表达式，然后对 Q 求导，以证明最优数量 $Q^{*}$（使期望利润最大化）满足

$$ F(Q^{*})=\frac{P-C}{P} \tag*{(5.113)}$$

**练习 5.3 [贝叶斯因子与 ROC 曲线 †]**

设 $B = p(D|H_1)/p(D|H_0)$ 为模型 1 的贝叶斯因子。假设我们绘制两条 ROC 曲线，一条通过对 $B$ 设置阈值得到，另一条通过对 $p(H_1|D)$ 设置阈值得到。它们会是相同还是不同？请解释原因。

**练习 5.4 [L1 损失下后验中位数是最优估计]**

证明后验中位数是 L1 损失下的最优估计。

---

请提供您需要翻译的英文 Markdown 文本内容。

---

## 6 信息论

本章介绍信息论领域中的几个基本概念。更多细节可参见其他书籍，例如 [Mac03; CT06]，以及本书的续篇 [Mur23]。

### 6.1 熵

概率分布的熵可以解释为一种不确定性或不可预测性的度量，与从给定分布中抽取的随机变量相关，如下所述。

我们还可以用熵来定义数据源的信息量。例如，假设我们从分布 p 中观测到一系列符号 $ X_n \sim p $。如果 p 具有高熵，那么很难预测每个观测值 $ X_n $。因此，我们说数据集 $ \mathcal{D} = (X_1, \ldots, X_n) $ 具有高信息量。相反，如果 p 是一个退化分布，熵为 0（最小值），那么每个 $ X_n $ 都相同，所以 $ \mathcal{D} $ 包含的信息很少。（所有这些都可以通过数据压缩的形式化来表述，本书续篇将对此进行讨论。）

#### 6.1.1 离散随机变量的熵

定义在 K 个状态上的分布 p 的离散随机变量 X 的熵为：

$$  \mathbb{H}\left(X\right)\triangleq-\sum_{k=1}^{K}p(X=k)\log_{2}p(X=k)=-\mathbb{E}_{X}\left[\log p(X)\right]   \tag*{(6.1)}$$

（注意，我们使用符号 $ \mathbb{H}(X) $ 来表示具有分布 $ p $ 的随机变量的熵，正如人们用 $ \mathbb{V}[X] $ 表示与 $ X $ 相关的分布的方差一样；我们也可以写成 $ \mathbb{H}(p) $。）通常我们使用以 2 为底的对数，此时单位称为 **比特** (bits)（二进制数字的简称）。例如，如果 $ X \in \{1, \ldots, 5\} $ 的直方图分布为 $ p = [0.25, 0.25, 0.2, 0.15, 0.15] $，则 $ H = 2.29 $ 比特。如果使用以 $ e $ 为底的对数，单位称为 **奈特** (nats)。

具有最大熵的离散分布是均匀分布。因此，对于一个 K 元随机变量，如果 $ p(x = k) = 1/K $，则熵最大；此时 $ \mathbb{H}(X) = \log_2 K $。这是因为：

$$  \mathbb{H}\left(X\right)=-\sum_{k=1}^{K}\frac{1}{K}\log(1/K)=-\log(1/K)=\log(K)   \tag*{(6.2)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_365_112_807_337.jpg" alt="图像" width="38%" /></div>

<div style="text-align: center;">图6.1：伯努利随机变量的熵作为 $\theta$ 的函数。最大熵为 $\log_{2}2=1$。由 bernoulli_entropy_fig.ipynb 生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_207_423_394_566.jpg" alt="图像" width="16%" /></div>

<div style="text-align: center;">$(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_424_491_720_568.jpg" alt="图像" width="25%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_730_494_1022_568.jpg" alt="图像" width="25%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图6.2：(a) 一些对齐的DNA序列。每行是一个序列，每列是序列中的一个位置。(b) 对应的位置权重矩阵，可视化为一系列直方图。每列表示字母表 $\{A, C, G, T\}$ 上对应于序列中该位置的概率分布。字母的大小与概率成正比。(c) 一个序列标识。详见正文。由 seq_logo_demo.ipynb 生成。</div>

相反地，具有最小熵（即零）的分布是将所有质量集中在单一状态上的任意 delta 函数。这种分布没有不确定性。

对于二元随机变量的特例，$X \in \{0,1\}$，我们可以设 $p(X=1) = \theta$ 和 $p(X=0) = 1 - \theta$。因此熵变为

$$
\begin{aligned}\mathbb{H}\left(X\right)&=-\left[p(X=1)\log_{2}p(X=1)+p(X=0)\log_{2}p(X=0)\right]\\&=-\left[\theta\log_{2}\theta+(1-\theta)\log_{2}(1-\theta)\right]\end{aligned}
\tag*{(6.3)}
$$

这被称为二元熵函数，也记作 $\mathbb{H}(\theta)$。我们在图6.1中绘制了该函数。可以看到，1比特的最大值出现在分布均匀时，即 $\theta = 0.5$。一枚公平的硬币只需一个是否问题即可确定其状态。

## 6. $ ^{1} $

作为熵的一个有趣应用，考虑表示DNA序列基序的问题，该基序是短DNA字符串上的一个分布。我们可以通过对一组DNA序列（例如来自不同物种）进行比对，然后估计在每个位置 $t$ 上，从4字母字母表 $X \sim \{A, C, G, T\}$ 中每个可能核苷酸的经验分布来估计该分布。

---

序列如下：

$$  \mathbf{N}_{t}=\left(\sum_{i=1}^{N}\mathbb{I}\left(X_{it}=A\right),\sum_{i=1}^{N}\mathbb{I}\left(X_{it}=C\right),\sum_{i=1}^{N}\mathbb{I}\left(X_{it}=G\right),\sum_{i=1}^{N}\mathbb{I}\left(X_{it}=T\right)\right)   \tag*{(6.5)}$$

$$  \hat{\boldsymbol{\theta}}_{t}=\mathbf{N}_{t}/N,   \tag*{(6.6)}$$

$N_t$ 是一个长度为4的向量，统计序列集合中每个位置上每个字母出现的次数。该 $\hat{\theta}_t$ 分布称为位置权重矩阵或序列基序。我们可以像 Figure 6.2b 所示那样将其可视化。图中绘制了字母A、C、G和T，其中位置 $t$ 上字母 $k$ 的大小与经验频率 $\theta_{tk}$ 成正比。

另一种可视化方法称为序列标识图，如 Figure 6.2c 所示。每列按 $R_t = 2 - H_t$ 缩放，其中 $H_t$ 是 $\hat{\theta}_t$ 的熵，$2 = \log_2(4)$ 是4字母分布的最大可能熵。因此，熵为0（从而信息含量最大）的确定性分布，其高度为2。这些信息丰富的位点通常由于属于基因编码区域而在进化中高度保守。我们也可以直接计算每个位置上最可能的字母，忽略不确定性；这称为一致序列。

##### 6.1.1.2 估计熵

估计具有多种可能状态的随机变量的熵，需要估计其分布，这可能需要大量数据。例如，假设X表示英文文档中一个单词的身份。由于存在大量罕见词的拖尾，且新词不断出现，因此很难可靠地估计 $p(X)$，进而估计 $\mathbb{H}(X)$。针对此问题的一种可能解决方案，参见[VV13]。

#### 6.1.2 交叉熵

分布p与q之间的交叉熵定义为

$$  \mathbb{H}_{c e}(p,q)\triangleq-\sum_{k=1}^{K}p_{k}\log q_{k}   \tag*{(6.7)}$$

可以证明，交叉熵是使用基于分布q的码压缩从分布p中抽取的一些数据样本所需期望比特数。通过设置 $q = p$ 可以最小化该值，此时最优码的期望比特数为 $\mathbb{H}_{ce}(p, p) = \mathbb{H}(p)$ ——这称为香农信源编码定理（例如，参见[CT06]）。

#### 6.1.3 联合熵

两个随机变量X和Y的联合熵定义为

$$  \mathbb{H}\left(X,Y\right)=-\sum_{x,y}p(x,y)\log_{2}p(x,y)   \tag*{(6.8)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

例如，考虑从1到8中选择一个整数，$ n \in \{1, \ldots, 8\} $。设如果n为偶数，则 $ X(n) = 1 $，如果n为质数，则 $ Y(n) = 1 $：

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>n</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>5</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>7</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>X</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

联合分布为

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>p(X,Y)</td><td style='text-align: center; word-wrap: break-word;'>Y=0</td><td style='text-align: center; word-wrap: break-word;'>Y=1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>X=0</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>3/8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>X=1</td><td style='text-align: center; word-wrap: break-word;'>3/8</td><td style='text-align: center; word-wrap: break-word;'>1/8</td></tr></table>

因此联合熵由下式给出

$$  \mathbb{H}\left(X,Y\right)=-\left[\frac{1}{8}\log_{2}\frac{1}{8}+\frac{3}{8}\log_{2}\frac{3}{8}+\frac{3}{8}\log_{2}\frac{3}{8}+\frac{1}{8}\log_{2}\frac{1}{8}\right]=1.81bits   \tag*{(6.9)}$$

显然边际概率是均匀的：$ p(X = 1) = p(X = 0) = p(Y = 0) = p(Y = 1) = 0.5 $，因此 $ \mathbb{H}(X) = \mathbb{H}(Y) = 1 $。所以 $ \mathbb{H}(X, Y) = 1.81 $ 比特 $ < \mathbb{H}(X) + \mathbb{H}(Y) = 2 $ 比特。事实上，联合熵的这一上界在一般情况下成立。如果X和Y独立，则 $ \mathbb{H}(X, Y) = \mathbb{H}(X) + \mathbb{H}(Y) $，因此该界是紧的。这在直觉上合理：当部分以某种方式相关时，会减少系统的“自由度”，从而降低整体熵。

$ \mathbb{H}(X,Y) $ 的下界是什么？如果 $ Y $ 是 $ X $ 的确定性函数，则 $ \mathbb{H}(X,Y) = \mathbb{H}(X) $。因此

$$  \mathbb{H}\left(X,Y\right)\geq\max\left\{\mathbb{H}\left(X\right),\mathbb{H}\left(Y\right)\right\}\geq0   \tag*{(6.10)}$$

直觉上，这表明将变量组合在一起并不会使熵降低：你无法仅通过向问题中添加更多未知量来减少不确定性，而是需要观察一些数据，我们将在第6.1.4节中讨论这一主题。

我们可以显然地将联合熵的定义从两个变量扩展到n个变量。

#### 6.1.4 条件熵

给定X的条件下Y的条件熵是在观察到X之后对Y的不确定性，对所有可能的X值取平均：

$$  \mathbb{H}\left(Y|X\right)\triangleq\mathbb{E}_{p(X)}\left[\mathbb{H}\left(p(Y|X)\right)\right]   \tag*{(6.11)}$$

$$  =\sum_{x}p(x)\mathbb{H}\left(p(Y|X=x)\right)=-\sum_{x}p(x)\sum_{y}p(y|x)\log p(y|x)   \tag*{(6.12)}$$

$$  =-\sum_{x,y}p(x,y)\log p(y|x)=-\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)}   \tag*{(6.13)}$$

$$  =-\sum_{x,y}p(x,y)\log p(x,y)+\sum_{x}p(x)\log p(x)   \tag*{(6.14)}$$

$$  =\mathbb{H}\left(X,Y\right)-\mathbb{H}\left(X\right)   \tag*{(6.15)}$$

如果Y是X的确定性函数，则知道X就完全确定了Y，因此 $ \mathbb{H}(Y|X)=0 $。如果X和Y独立，则知道X无法告诉我们任何关于Y的信息，且 $ \mathbb{H}(Y|X)=\mathbb{H}(Y) $。由于

---

我们有 $ \mathbb{H}(X,Y) \leq \mathbb{H}(Y) + \mathbb{H}(X) $，因此可得

$$  \mathbb{H}\left(Y|X\right)\leq\mathbb{H}\left(Y\right)   \tag*{(6.16)}$$

当且仅当 $X$ 与 $Y$ 独立时等号成立。这说明，平均而言，基于数据条件化从不增加不确定性。之所以需要“平均”这一限定词，是因为对于任何特定的观测值（即 $X$ 的某个取值），人们可能会变得更加“困惑”（即 $ \mathbb{H}(Y|x) > \mathbb{H}(Y) $）。然而，从期望角度来说，审视数据是有益的。（另见第 6.3.8 节。）

我们可以将方程 (6.15) 重写如下：

$$  \mathbb{H}\left(X_{1},X_{2}\right)=\mathbb{H}\left(X_{1}\right)+\mathbb{H}\left(X_{2}|X_{1}\right)   \tag*{(6.17)}$$

这可以推广为熵的链式法则：

$$  \mathbb{H}\left(X_{1},X_{2},\cdots,X_{n}\right)=\sum_{i=1}^{n}\mathbb{H}\left(X_{i}|X_{1},\cdots,X_{i-1}\right)   \tag*{(6.18)}$$

#### 6.1.5 困惑度

离散概率分布 $p$ 的困惑度定义为

$$  \mathrm{p e r p l e x i t y}(p)\triangleq2^{\mathbb{H}(p)}   \tag*{(6.19)}$$

这通常被解释为一种可预测性的度量。例如，假设 $p$ 是 $K$ 个状态上的均匀分布，则困惑度为 $K$。显然，困惑度的下界是 $2^{0}=1$，当分布能够完美预测结果时达到该下界。

现在，假设我们有一个基于数据 $\mathcal{D}$ 的经验分布：

$$  p_{\mathcal{D}}(x|\mathcal{D})=\frac{1}{N}\sum_{n=1}^{N}\delta(x-x_{n})   \tag*{(6.20)}$$

我们可以通过计算下式来衡量 $p$ 对 $\mathcal{D}$ 的预测能力：

$$  \mathrm{p e r p l e x i t y}(p_{\mathcal{D}},p)\triangleq2^{\mathbb{H}_{c e}(p_{\mathcal{D}},p)}   \tag*{(6.21)}$$

困惑度常用于评估统计语言模型的质量，这类模型是令牌序列的生成模型。假设数据是长度为 $N$ 的单个长文档 $\mathbf{x}$，且 $p$ 是一个简单的一元模型。此时，交叉熵项为

$$  H=-\frac{1}{N}\sum_{n=1}^{N}\log p(x_{n})   \tag*{(6.22)}$$

因此困惑度为

$$   perplexity(p_{\mathcal{D}},p)=2^{H}=2^{-\frac{1}{N}\log(\prod_{n=1}^{N}p(x_{n}))}=\sqrt[N]{\prod_{n=1}^{N}\frac{1}{p(x_{n})}}   \tag*{(6.23)}$$

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议。

---

这有时被称为指数化交叉熵。我们看到这是逆预测概率的几何平均值。

在语言模型的情况下，我们在预测下一个词时通常以之前的词为条件。例如，在二元语法模型中，我们使用一阶马尔可夫模型，形式为 $ p(x_i | x_{i-1}) $。我们将语言模型的分支因子定义为任意给定词后可能出现的词的数量。因此，我们可以将困惑度理解为加权平均分支因子。例如，假设模型预测每个词出现的概率相等，与上下文无关，即 $ p(x_i | x_{i-1}) = 1/K $。那么困惑度为 $ (1/(K)^N)^{-1/N} = K $。如果某些符号比其他符号更可能出现，并且模型正确反映了这一点，那么其困惑度将低于 $ K $。然而，正如我们在 Section 6.2 中所示，有 $ \mathbb{H}(p^*) \leq \mathbb{H}_{ce}(p^*, p) $，因此我们永远无法将困惑度降低到基础随机过程 $ p^* $ 的熵以下。

关于困惑度及其在语言模型中的使用的进一步讨论，请参见 [JM08, p96]。

#### 6.1.6 连续随机变量的微分熵 *

如果 X 是一个具有概率密度函数（pdf）p(x) 的连续随机变量，我们定义微分熵为

$$  h(X)\triangleq-\int_{\mathcal{X}}p(x)\log p(x)dx   \tag*{(6.24)}$$

假设该积分存在。例如，假设 $ X \sim U(0, a) $。那么

$$  h(X)=-\int_{0}^{a}dx\frac{1}{a}\log\frac{1}{a}=\log a   \tag*{(6.25)}$$

请注意，与离散情况不同，微分熵可能为负。这是因为概率密度函数可能大于 1。例如，如果 $ X \sim U(0,1/8) $，我们有 $ h(X) = \log_2(1/8) = -3 $。

理解微分熵的一种方式是意识到所有实数值只能以有限精度表示。可以证明 $ [CT91, p228] $，连续随机变量 $ X $ 的 $ n $ 位量化的熵近似为 $ h(X) + n $。例如，假设 $ X \sim U(0, \frac{1}{8}) $。那么在 $ X $ 的二进制表示中，二进制小数点右侧的前 3 位必须为 0（因为该数 $ \leq 1/8 $）。因此，要以 $ n $ 位精度描述 $ X $，只需要 $ n - 3 $ 位，这与上面计算的 $ h(X) = -3 $ 一致。

##### 6.1.6.1 示例：高斯分布的熵

d 维高斯分布的熵为

$$  h(\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma}))=\frac{1}{2}\ln|2\pi e\boldsymbol{\Sigma}|=\frac{1}{2}\ln[(2\pi e)^{d}|\boldsymbol{\Sigma}|]=\frac{d}{2}+\frac{d}{2}\ln(2\pi)+\frac{1}{2}\ln|\boldsymbol{\Sigma}|   \tag*{(6.26)}$$

在一维情况下，变为

$$  h(\mathcal{N}(\mu,\sigma^{2}))=\frac{1}{2}\ln\left[2\pi e\sigma^{2}\right]   \tag*{(6.27)}$$

---

##### 6.1.6.2 与方差的联系

高斯分布的熵随着方差增大而单调递增，但情况并非总是如此。例如，考虑两个一维高斯分布的混合，中心分别位于-1和+1。当我们将均值进一步分开（例如移至-10和+10）时，方差增大（因为与全局均值的平均距离增大），但熵大致保持不变，因为我们仍然不确定样本可能落在何处，即使知道它会在-10或+10附近。（精确计算高斯混合模型的熵较为困难，但文献[Hub+08]提出了一种计算上下界的方法。）

##### 6.1.6.3 离散化

通常，计算连续随机变量的微分熵可能很困难。一种简单的近似方法是对变量进行离散化或量化。有多种方法（例如，参见[DKS95; KK06]的总结），但一种简单方法是基于经验分位数对分布进行分箱。关键问题在于使用多少个分箱[LM04]。Scott [Sco79]提出了以下启发式公式：

$$  B=N^{1/3}\frac{\max(\mathcal{D})-\min(\mathcal{D})}{3.5\sigma(\mathcal{D})}   \tag*{(6.28)}$$

其中 $ \sigma(\mathcal{D}) $ 是数据的经验标准差，$ N = |\mathcal{D}| $ 是经验分布中数据点的数量。然而，如果X是多维随机向量，由于维度灾难，离散化技术难以扩展。

### 6.2 相对熵（KL散度）  $ ^{*} $

给定两个分布 $ p $ 和 $ q $，通常需要定义一个距离度量来衡量它们之间的“接近”或“相似”程度。实际上，我们将更一般地考虑一个散度度量 $ D(p, q) $，它量化了 $ q $ 与 $ p $ 的偏离程度，而不要求 $ D $ 是一个度量。更精确地说，如果 $ D(p, q) \geq 0 $ 且等号成立当且仅当 $ p = q $，则称 $ D $ 是一个散度；而度量还要求 $ D $ 对称且满足三角不等式 $ D(p, r) \leq D(p, q) + D(q, r) $。我们可以使用许多可能的散度度量。在本节中，我们重点关注Kullback-Leibler散度或KL散度，也称为信息增益或相对熵，用于两个分布 $ p $ 和 $ q $ 之间。

#### 6.2.1 定义

对于离散分布，KL散度定义如下：

$$  D_{\mathbb{K L}}\left(p\parallel q\right)\triangleq\sum_{k=1}^{K}p_{k}\log\frac{p_{k}}{q_{k}}   \tag*{(6.29)}$$

这自然地扩展到连续分布：

$$  D_{\mathbb{K L}}\left(p\parallel q\right)\triangleq\int d x p(x)\log\frac{p(x)}{q(x)}   \tag*{(6.30)}$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 6.2.2 解释

我们可以将 KL 散度重写如下：

$$  D_{\mathbb{K L}}\left(p\parallel q\right)=\underbrace{\sum_{k=1}^{K}p_{k}\log p_{k}}_{-\mathbb{H}(p)}\underbrace{-\sum_{k=1}^{K}p_{k}\log q_{k}}_{\mathbb{H}_{c e}(p,q)}   \tag*{(6.31)}$$

其中第一项是负熵，第二项是交叉熵。可以证明，交叉熵 $\mathbb{H}_{ce}(p,q)$ 是压缩来自分布 $p$ 的数据所需比特数的下界，前提是编码方案基于分布 $q$ 设计；因此，我们可以将 KL 散度解释为：与使用真实分布 $p$ 的编码方案相比，若基于错误分布 $q$ 进行编码，在压缩数据样本时需要付出的“额外比特数”。

KL 散度还有其他多种解释。更多信息请参阅本书的续篇 [Mur23]。

#### 6.2.3 示例：两个高斯分布之间的 KL 散度

例如，可以证明两个多元高斯分布之间的 KL 散度为

$$  \begin{aligned}&D_{\mathbb{K L}}\left(\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{1},\boldsymbol{\Sigma}_{1})\parallel\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}_{2},\boldsymbol{\Sigma}_{2})\right)\\&=\frac{1}{2}\left[\mathrm{t r}(\boldsymbol{\Sigma}_{2}^{-1}\boldsymbol{\Sigma}_{1})+(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})^{\mathsf{T}}\boldsymbol{\Sigma}_{2}^{-1}(\boldsymbol{\mu}_{2}-\boldsymbol{\mu}_{1})-D+\log\left(\frac{\operatorname{d e t}(\boldsymbol{\Sigma}_{2})}{\operatorname{d e t}(\boldsymbol{\Sigma}_{1})}\right)\right]\\ \end{aligned}   \tag*{(6.32)}$$

在标量情形下，上式变为

$$  D_{\mathbb{K L}}\left(\mathcal{N}(x|\mu_{1},\sigma_{1})\parallel\mathcal{N}(x|\mu_{2},\sigma_{2})\right)=\log\frac{\sigma_{2}}{\sigma_{1}}+\frac{\sigma_{1}^{2}+\left(\mu_{1}-\mu_{2}\right)^{2}}{2\sigma_{2}^{2}}-\frac{1}{2}   \tag*{(6.33)}$$

#### 6.2.4 KL 散度的非负性

本节证明 KL 散度总是非负的。

为此，我们使用 Jensen 不等式。该不等式指出，对于任意凸函数 $f$，有

$$  f(\sum_{i=1}^{n}\lambda_{i}\boldsymbol{x}_{i})\leq\sum_{i=1}^{n}\lambda_{i} f(\boldsymbol{x}_{i})   \tag*{(6.34)}$$

其中 $\lambda_i \geq 0$ 且 $\sum_{i=1}^n \lambda_i = 1$。换句话说，该结果说明“平均值的 $f$ 小于等于 $f$ 的平均值”。当 $n=2$ 时这一结论显然成立，因为凸函数在连接两端点的直线上方向上弯曲（见第 8.1.3 节）。对于一般 $n$ 的情况，我们可以使用归纳法证明。

例如，若 $f(x) = \log(x)$ 是一个凹函数，则有

$$  \log(\mathbb{E}_{x}g(x))\geq\mathbb{E}_{x}\log(g(x))   \tag*{(6.35)}$$

我们将在下文使用该结果。

---

##### 定理 6.2.1.（信息不等式） $ D_{\mathbb{K}\mathbb{L}}\left(p\parallel q\right)\geq0 $，当且仅当 $ p=q $ 时等号成立。

**证明.** 我们按照 [CT06, p28] 的方法证明该定理。令 $ A = \{x : p(x) > 0\} $ 为 $ p(x) $ 的支撑集。利用对数函数的凹性和詹森不等式（第 6.2.4 节），可得

$$  -D_{\mathbb{K L}}\left(p\parallel q\right)=-\sum_{x\in A}p(x)\log\frac{p(x)}{q(x)}=\sum_{x\in A}p(x)\log\frac{q(x)}{p(x)}   \tag*{(6.36)}$$

$$  \leq\log\sum_{x\in A}p(x)\frac{q(x)}{p(x)}=\log\sum_{x\in A}q(x)   \tag*{(6.37)}$$

$$  \leq\log\sum_{x\in\mathcal{X}}q(x)=\log1=0   \tag*{(6.38)}$$

由于 $ \log(x) $ 是严格凹函数（$ -\log(x) $ 是凸函数），式 (6.37) 中的等号成立当且仅当存在某个常数 $ c $，使得 $ p(x) = cq(x) $，其中 $ c $ 表示整个空间 $ X $ 中包含在 $ A $ 中的比例。式 (6.38) 中的等号成立当且仅当 $ \sum_{x \in A} q(x) = \sum_{x \in X} q(x) = 1 $，这意味着 $ c = 1 $。因此，$ D_{\mathbb{K}L}(p \parallel q) = 0 $ 当且仅当对所有 $ x $ 有 $ p(x) = q(x) $。

该定理有许多重要推论，本书后续将陆续展示。例如，我们可以证明均匀分布是熵最大的分布：

**推论 6.2.1.（均匀分布最大化熵）** $ \mathbb{H}(X) \leq \log|\mathcal{X}| $，其中 $ |\mathcal{X}| $ 是 $ X $ 的状态数，当且仅当 $ p(x) $ 为均匀分布时等号成立。

**证明.** 令 $ u(x) = 1/|\mathcal{X}| $。则

$$  0\leq D_{\mathbb{K L}}\left(p\parallel u\right)=\sum_{x}p(x)\log\frac{p(x)}{u(x)}=\log|\mathcal{X}|-\mathbb{H}\left(X\right)   \tag*{(6.39)}$$

#### 6.2.5 KL 散度与 MLE

假设我们希望找到与分布 $ p $ 在 KL 散度意义下最接近的分布 $ q $：

$$  q^{*}=\arg\min_{q}D_{\mathbb{K L}}\left(p\parallel q\right)=\arg\min_{q}\int p(x)\log p(x)d x-\int p(x)\log q(x)d x   \tag*{(6.40)}$$

现在假设 $ p $ 是经验分布，它在观测到的训练数据上放置概率原子，在其他地方质量为 0：

$$  p_{\mathcal{D}}(x)=\frac{1}{N}\sum_{n=1}^{N}\delta(x-x_{n})   \tag*{(6.41)}$$

作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可协议

---

利用狄拉克 delta 函数的筛选性质，我们得到

$$  D_{\mathbb{K L}}\left(p_{\mathcal{D}}\parallel q\right)=-\int p_{\mathcal{D}}(x)\log q(x)d x+C   \tag*{(6.42)}$$

$$  =-\int\left[\frac{1}{N}\sum_{n}\delta(x-x_{n})\right]\log q(x)dx+C   \tag*{(6.43)}$$

$$  =-\frac{1}{N}\sum_{n}\log q(x_{n})+C   \tag*{(6.44)}$$

其中 $C = \int p(x) \log p(x) \, dx$ 是一个与 $q$ 无关的常数。这称为**交叉熵目标**，它等于 $q$ 在训练集上的平均负对数似然。因此，我们看到最小化与经验分布的 KL 散度等价于最大化似然。

这一视角揭示了基于似然训练的缺陷，即它过分强调训练集的重要性。在大多数应用中，我们并不真正相信经验分布是真实分布的优良表示，因为它仅在有限个点上放置“尖峰”，而其他任何地方的密度都为零。即使数据集很大（例如 100 万张图像），从中采样数据的宇宙通常更大（例如，“所有自然图像”的集合远大于 100 万张）。我们可以使用核密度估计（第 16.3 节）对经验分布进行平滑，但这需要图像空间上类似的核。另一种算法方法是使用**数据增强**，这是一种以我们认为反映合理“自然变化”的方式扰动观测数据样本的方法。在此增强数据集上应用 MLE 通常会得到更优的结果，尤其是在拟合具有许多参数的模型时（见第 19.1 节）。

#### 6.2.6 前向 KL 与反向 KL

假设我们希望用一个更简单的分布 $q$ 来近似一个分布 $p$。我们可以通过最小化 $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ 或 $D_{\mathbb{K}\mathbb{L}}(p \parallel q)$ 来实现。这会产生不同的行为，下面我们将进行讨论。

首先考虑前向 KL，也称为**包含式 KL**，定义为

$$  D_{\mathbb{K L}}\left(p\parallel q\right)=\int p(x)\log\frac{p(x)}{q(x)}d x   \tag*{(6.45)}$$

关于 $q$ 最小化该量被称为 M-投影或矩投影。

通过考虑那些 $p(x) > 0$ 但 $q(x) = 0$ 的输入 $x$，我们可以理解最优 $q$ 的特性。在这种情况下，项 $\log p(x)/q(x)$ 将是无穷大。因此，最小化 KL 散度将迫使 $q$ 包含 $p$ 具有非零概率的所有空间区域。换句话说，$q$ 将是**避开零**或**覆盖模式**的，并且通常会高估 $p$ 的支撑集。图 6.3(a) 展示了模式覆盖的情况，其中 $p$ 是一个双峰分布，而 $q$ 是单峰的。

现在考虑反向 KL，也称为**排他性 KL**：

$$  D_{\mathbb{K L}}\left(q\parallel p\right)=\int q(x)\log\frac{q(x)}{p(x)}d x   \tag*{(6.46)}$$

关于 $q$ 最小化该量被称为 I-投影或信息投影。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_195_118_416_336.jpg" alt="图像" width="19%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_452_118_720_338.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_731_121_1000_337.jpg" alt="图像" width="23%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;">图 6.3：在双峰分布上说明前向KL与反向KL的区别。蓝色曲线为真实分布 $p$ 的等高线。红色曲线为单峰近似分布 $q$ 的等高线。(a) 相对于 $q$ 最小化前向KL， $ D_{\text{KL}}(p \parallel q) $，导致 $q$ “覆盖” $p$。(b-c) 相对于 $q$ 最小化反向KL， $ D_{\text{KL}}(q \parallel p) $ ，导致 $q$ “锁定” $p$ 的两个模态之一。改编自 [Bis06] 的图 10.3。由 KLfwdReverseMixGauss.ipynb 生成。</div>

通过考虑 $p(x) = 0$ 但 $q(x) > 0$ 的输入 $x$，我们可以理解最优 $q$ 的行为。此时，项 $\log q(x)/p(x)$ 会趋于无穷大。因此，最小化排他性KL会迫使 $q$ 排除所有 $p$ 概率为零的区域。实现这一点的一种方式是让 $q$ 将概率质量集中在空间的极少数部分；这称为**零强制**或**模式寻求**行为。在这种情况下，$q$ 通常会低估 $p$ 的支撑集。我们在图 6.3(b-c) 中展示了当 $p$ 是双峰而 $q$ 是单峰时的模式寻求行为。

### 6.3 互信息 *

KL散度为我们提供了一种衡量两个分布相似程度的方法。那么，应该如何衡量两个随机变量的相关程度呢？一种方法是将测量两个随机变量相关性的问题转化为它们分布相似性的问题。由此引入了两个随机变量之间的**互信息**概念，定义如下。

#### 6.3.1 定义

随机变量 $X$ 和 $Y$ 之间的互信息定义如下：

$$  \mathbb{I}\left(X;Y\right)\triangleq D_{\mathbb{K L}}\left(p(x,y)\parallel p(x)p(y)\right)=\sum_{y\in Y}\sum_{x\in X}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}   \tag*{(6.47)}$$

（我们使用 $\mathbb{I}(X;Y)$ 而非 $\mathbb{I}(X,Y)$，以避免 $X$ 和/或 $Y$ 表示变量集合时的歧义；例如，可以用 $\mathbb{I}(X;Y,Z)$ 表示 $X$ 与 $(Y,Z)$ 之间的互信息。）对于连续随机变量，只需将求和替换为积分。

显然，互信息总是非负的，即使对于连续随机变量也是如此，因为

$$  \mathbb{I}\left(X;Y\right)=D_{\mathbb{K L}}\left(p(x,y)\parallel p(x)p(y)\right)\geq0   \tag*{(6.48)}$$

作者：Kevin P. Murphy。 (C) MIT Press。 CC-BY-NC-ND 许可。

---

当且仅当 $ p(x,y)=p(x)p(y) $ 时，我们达到边界 0。

#### 6.3.2 解释

互信息是联合分布与因式化边缘分布之间的KL散度，这一事实表明，如果我们从将两个变量视为独立的模型 $ p(x)p(y) $ 更新为建模其真实联合密度 $ p(x,y) $ 的模型，互信息衡量的是信息增益。

为了更深入地理解互信息的含义，将其用联合熵和条件熵重新表达是有帮助的，如下所示：

$$  \mathbb{I}\left(X;Y\right)=\mathbb{H}\left(X\right)-\mathbb{H}\left(X|Y\right)=\mathbb{H}\left(Y\right)-\mathbb{H}\left(Y|X\right)   \tag*{(6.49)}$$

因此，我们可以将 X 与 Y 之间的互信息解释为在观察到 Y 后 X 的不确定性的减少，或者由对称性，在观察到 X 后 Y 的不确定性的减少。顺便提一下，这个结果提供了条件作用平均降低熵的另一种证明。特别地，我们有 $ 0 \leq \mathbb{I}(X; Y) = \mathbb{H}(X) - \mathbb{H}(X|Y) $，因此 $ \mathbb{H}(X|Y) \leq \mathbb{H}(X) $。

我们还可以得到另一种解释。可以证明：

$$  \mathbb{I}\left(X;Y\right)=\mathbb{H}\left(X,Y\right)-\mathbb{H}\left(X|Y\right)-\mathbb{H}\left(Y|X\right)   \tag*{(6.50)}$$

最后，可以证明：

$$  \mathbb{I}\left(X;Y\right)=\mathbb{H}\left(X\right)+\mathbb{H}\left(Y\right)-\mathbb{H}\left(X,Y\right)   \tag*{(6.51)}$$

参见图 6.4，这些方程以信息图的形式进行了总结（形式上，这是一个将集合表达式映射到其信息论对应物的有符号测度 [Yeu91]）。

#### 6.3.3 示例

作为示例，让我们重新考虑第 6.1.3 节中关于素数和偶数的例子。回忆一下，$ \mathbb{H}(X) = \mathbb{H}(Y) = 1 $。条件分布 $ p(Y|X) $ 通过对每一行归一化给出：

 $$ \begin{array}{c|cc}{{{Y=0}}}&{{{Y=1}}} \\{{{\hline X=0}}}&{{{\frac{1}{4}}}}&{{{\frac{3}{4}}}} \\{{{X=1}}}&{{{\frac{3}{4}}}}&{{{\frac{1}{4}}}} \\\end{array} $$ 

因此条件熵为：

$$  \mathbb{H}\left(Y|X\right)=-\left[\frac{1}{8}\log_{2}\frac{1}{4}+\frac{3}{8}\log_{2}\frac{3}{4}+\frac{3}{8}\log_{2}\frac{3}{4}+\frac{1}{8}\log_{2}\frac{1}{4}\right]=0.81\text{ 比特}   \tag*{(6.52)}$$

互信息为：

$$  \mathbb{I}\left(X;Y\right)=\mathbb{H}\left(Y\right)-\mathbb{H}\left(Y|X\right)=\left(1-0.81\right)\text{ 比特}=0.19\text{ 比特}   \tag*{(6.53)}$$

你可以很容易地验证：

$$  \begin{aligned}\mathbb{H}\left(X,Y\right)&=\mathbb{H}\left(X|Y\right)+\mathbb{I}\left(X;Y\right)+\mathbb{H}\left(Y|X\right)\\&=\left(0.81+0.19+0.81\right)\text{ 比特}=1.81\text{ 比特}\end{aligned}   \tag*{(6.54)}$$

“概率机器学习：导论”。在线版本。2024 年 11 月 23 日

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_324_126_853_538.jpg" alt="图片" width="45%" /></div>


<div style="text-align: center;">图 6.4：边际熵、联合熵、条件熵与互信息的信息图表示。经 Katie Everett 友好许可使用。</div>


#### 6.3.4 条件互信息

我们可以自然地定义条件互信息如下：

$$  \mathbb{I}\left(X;Y|Z\right)\triangleq\mathbb{E}_{p(Z)}\left[\mathbb{I}(X;Y)|Z\right]   \tag*{(6.56)}$$

$$  =\mathbb{E}_{p(x,y,z)}\left[\log\frac{p(x,y|z)}{p(x|z)p(y|z)}\right]   \tag*{(6.57)}$$

$$  =\mathbb{H}\left(X|Z\right)+\mathbb{H}\left(Y|Z\right)-\mathbb{H}\left(X,Y|Z\right)   \tag*{(6.58)}$$

$$  =\mathbb{H}\left(X|Z\right)-\mathbb{H}\left(X|Y,Z\right)=\mathbb{H}\left(Y|Z\right)-\mathbb{H}\left(Y|X,Z\right)   \tag*{(6.59)}$$

$$  =\mathbb{H}\left(X,Z\right)+\mathbb{H}\left(Y,Z\right)-\mathbb{H}\left(Z\right)-\mathbb{H}\left(X,Y,Z\right)   \tag*{(6.60)}$$

$$  =\mathbb{I}(Y;X,Z)-\mathbb{I}(Y;Z)   \tag*{(6.61)}$$

最后一个等式表明，条件互信息是 $X$ 关于 $Y$ 所提供的额外（残余）信息，排除了在仅给定 $Z$ 时我们已经知道的关于 $Y$ 的信息。

我们可以将式 (6.61) 重写如下：

$$  \mathbb{I}(Z,Y;X)=\mathbb{I}(Z;X)+\mathbb{I}(Y;X|Z)   \tag*{(6.62)}$$

推广到 $N$ 个变量，得到互信息的链式法则：

$$  \mathbb{I}\left(Z_{1},\cdots,Z_{N};X\right)=\sum_{n=1}^{N}\mathbb{I}\left(Z_{n};X|Z_{1},\cdots,Z_{n-1}\right)   \tag*{(6.63)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可协议。

---

#### 6.3.5 互信息作为“广义相关系数”

假设 $ (x, y) $ 是联合高斯的：

$$  \begin{pmatrix}x\\ y\end{pmatrix}\sim\mathcal{N}\left(\mathbf{0},\begin{pmatrix}\sigma^{2}&\rho\sigma^{2}\\ \rho\sigma^{2}&\sigma^{2}\end{pmatrix}\right)   \tag*{(6.64)}$$

现在我们展示如何计算 $ X $ 和 $ Y $ 之间的互信息。利用公式 (6.26)，我们发现熵为

$$  h(X,Y)=\frac{1}{2}\log\left[(2\pi e)^{2}\det\Sigma\right]=\frac{1}{2}\log\left[(2\pi e)^{2}\sigma^{4}(1-\rho^{2})\right]   \tag*{(6.65)}$$

由于 $ X $ 和 $ Y $ 各自服从方差为 $ \sigma^{2} $ 的正态分布，我们有

$$  h(X)=h(Y)=\frac{1}{2}\log\left[2\pi e\sigma^{2}\right]   \tag*{(6.66)}$$

因此

$$  I(X,Y)=h(X)+h(Y)-h(X,Y)   \tag*{(6.67)}$$

$$  =\log[2\pi e\sigma^{2}]-\frac{1}{2}\log[(2\pi e)^{2}\sigma^{4}(1-\rho^{2})]   \tag*{(6.68)}$$

$$  =\frac{1}{2}\log[(2\pi e\sigma^{2})^{2}]-\frac{1}{2}\log[(2\pi e\sigma^{2})^{2}(1-\rho^{2})]   \tag*{(6.69)}$$

$$  =\frac{1}{2}\log\frac{1}{1-\rho^{2}}=-\frac{1}{2}\log[1-\rho^{2}]   \tag*{(6.70)}$$

现在我们讨论一些有趣的特例。

1. $ \rho = 1 $。此时 $ X = Y $，且 $ I(X, Y) = \infty $，这很合理。观测 $ Y $ 告诉我们关于 $ X $ 的无穷多信息（因为我们精确知道它的真实值）。

2. $ \rho = 0 $。此时 $ X $ 和 $ Y $ 独立，且 $ I(X, Y) = 0 $，这很合理。观测 $ Y $ 不提供任何关于 $ X $ 的信息。

3. $ \rho = -1 $。此时 $ X = -Y $，且 $ I(X, Y) = \infty $，同样合理。观测 $ Y $ 允许我们以无限精度预测 $ X $。

现在考虑 $ X $ 和 $ Y $ 是标量但不联合高斯的情况。通常，计算连续随机变量之间的互信息可能很困难，因为我们必须估计联合密度 $ p(X,Y) $。对于标量变量，一种简单的近似方法是离散化或量化它们：将每个变量的取值范围划分为若干 bin，并统计落入每个直方图 bin 中的值个数 [Sco79]。然后我们可以利用经验概率质量函数轻松计算互信息。

不幸的是，使用的 bin 数量以及 bin 边界的位置可能会对结果产生显著影响。避免这一问题的一种方法是使用 K 近邻距离以非参数自适应方式估计密度。这是 [KSG04] 中提出的 KSG 互信息估计量的基础。该估计量已在 sklearn.feature_selection.mutual_info_regression 函数中实现。有关该估计量的论文，请参见 [GOV18; HN19]。