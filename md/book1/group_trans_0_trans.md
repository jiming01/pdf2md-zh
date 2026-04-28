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

概率机器学习

---

# Adaptive Computation and Machine Learning

Thomas Dietterich, 编辑

Christopher Bishop, David Heckerman, Michael Jordan, and Michael Kearns, 副编辑

Bioinformatics: The Machine Learning Approach, Pierre Baldi and Søren Brunak

Reinforcement Learning: An Introduction, Richard S. Sutton and Andrew G. Barto

Graphical Models for Machine Learning and Digital Communication, Brendan J. Frey

Learning in Graphical Models, Michael I. Jordan

Causation, Prediction, and Search, 第二版, Peter Spirtes, Clark Glymour, and Richard Scheines

Principles of Data Mining, David Hand, Heikki Mannila, and Padhraic Smyth

Bioinformatics: The Machine Learning Approach, 第二版, Pierre Baldi and Søren Brunak

Learning Kernel Classifiers: Theory and Algorithms, Ralf Herbrich

Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond, Bernhard Schölkopf and Alexander J. Smola

Introduction to Machine Learning, Ethem Alpaydin

Gaussian Processes for Machine Learning, Carl Edward Rasmussen and Christopher K.I. Williams

Semi-Supervised Learning, Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien, 编辑

The Minimum Description Length Principle, Peter D. Grünwald

Introduction to Statistical Relational Learning, Lise Getoor and Ben Taskar, 编辑

Probabilistic Graphical Models: Principles and Techniques, Daphne Koller and Nir Friedman

Introduction to Machine Learning, 第二版, Ethem Alpaydin

Boosting: Foundations and Algorithms, Robert E. Schapire and Yoav Freund

Machine Learning: A Probabilistic Perspective, Kevin P. Murphy

Foundations of Machine Learning, Mehryar Mohri, Afshin Rostami, and Ameet Talwalker

Probabilistic Machine Learning: An Introduction, Kevin P. Murphy

---

# 概率机器学习导论

Kevin P. Murphy

The MIT Press

Cambridge, Massachusetts

London, England

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_150_266_173_288.jpg" alt="Image" width="1%" /></div>


© 2022 麻省理工学院

本作品遵循知识共享 CC-BY-NC-ND 许可协议。

<div style="text-align: center;"><img src="imgs/img_in_image_box_152_417_239_449.jpg" alt="Image" width="7%" /></div>


在该许可协议下，保留所有权利。

麻省理工学院出版社感谢匿名同行评审人对本书初稿提出的宝贵意见。学术专家的慷慨工作是确立我们出版物权威性和质量的关键。我们衷心感谢这些未具名读者的贡献。

在美国印刷并装订。

美国国会图书馆出版编目数据

著者：Kevin P. Murphy

书名：概率机器学习：导论 / Kevin P. Murphy

描述：马萨诸塞州剑桥：麻省理工学院出版社，[2022]

丛书：自适应计算与机器学习系列

含参考文献与索引。

标识符：LCCN 2021027430 | ISBN 9780262046824（精装）

主题：机器学习 | 概率

分类：LCC Q325.5 .M872 2022 | DDC 006.3/1–dc23

LC记录可在 https://lccn.loc.gov/2021027430 获取

10 9 8 7 6 5 4 3 2 1

---

这本书献给我的母亲 Brigid Murphy，是她让我领略到学习和教学的乐趣。

---

请提供您需要翻译的英文学术论文 Markdown 文本。

---

### 简明目录

1 引言 1  
  
I 基础 31  
2 概率论：单变量模型 33  
3 概率论：多变量模型 77  
4 统计学 107  
5 决策论 167  
6 信息论 207  
7 线性代数 229  
8 最优化 275  
  
II 线性模型 321  
9 线性判别分析 323  
10 逻辑回归 339  
11 线性回归 371  
12 广义线性模型 * 415  
  
III 深度神经网络 423  
13 面向表格数据的神经网络 425  
14 面向图像的神经网络 467  
15 面向序列的神经网络 503  
  
IV 非参数模型 545  
16 基于样本的方法 547  
17 核方法 * 567  
18 决策树、随机森林、Bagging 与 Boosting 603

---

V 超越监督学习 625  
19 使用更少标注样本的学习 627  
20 降维 657  
21 聚类 715  
22 推荐系统 741  
23 图嵌入 * 753  
A 符号表 773

---

## 目录

前言 xxvii  
1 引言 1  
1.1 什么是机器学习？ 1  
1.2 监督学习 1  
1.2.1 分类 2  
1.2.2 回归 8  
1.2.3 过拟合与泛化 12  
1.2.4 没有免费午餐定理 13  
1.3 无监督学习 14  
1.3.1 聚类 14  
1.3.2 发现潜在的“变异因素” 15  
1.3.3 自监督学习 16  
1.3.4 评估无监督学习 16  
1.4 强化学习 17  
1.5 数据 19  
1.5.1 一些常见的图像数据集 19  
1.5.2 一些常见的文本数据集 21  
1.5.3 离散输入数据的预处理 23  
1.5.4 文本数据的预处理 24  
1.5.5 处理缺失数据 26  
1.6 讨论 27  
1.6.1 机器学习与其他领域的关系 27  
1.6.2 本书的结构 28  
1.6.3 注意事项 28  

I 基础 31  
2 概率：单变量模型 33  
2.1 引言 33  
2.1.1 什么是概率？ 33

---

2.1.2 不确定性的类型 33  
2.1.3 概率作为逻辑的延伸 34  
2.2 随机变量 35  
2.2.1 离散随机变量 35  
2.2.2 连续随机变量 36  
2.2.3 相关随机变量的集合 38  
2.2.4 独立性与条件独立性 39  
2.2.5 分布的矩 40  
2.2.6 汇总统计量的局限性 * 43  
2.3 贝叶斯规则 44  
2.3.1 示例：COVID-19检测 46  
2.3.2 示例：蒙提霍尔问题 47  
2.3.3 逆问题 * 49  
2.4 伯努利分布与二项分布 49  
2.4.1 定义 49  
2.4.2 S型（逻辑）函数 50  
2.4.3 二元逻辑回归 52  
2.5 分类分布与多项分布 53  
2.5.1 定义 53  
2.5.2 Softmax函数 54  
2.5.3 多类逻辑回归 55  
2.5.4 对数-求和-指数技巧 56  
2.6 单变量高斯（正态）分布 57  
2.6.1 累积分布函数 57  
2.6.2 概率密度函数 58  
2.6.3 回归 59  
2.6.4 高斯分布为何如此广泛使用？ 60  
2.6.5 狄拉克δ函数作为极限情形 60  
2.7 其他常见单变量分布 * 61  
2.7.1 学生t分布 61  
2.7.2 柯西分布 62  
2.7.3 拉普拉斯分布 63  
2.7.4 贝塔分布 63  
2.7.5 伽马分布 64  
2.7.6 经验分布 65  
2.8 随机变量的变换 * 66  
2.8.1 离散情形 66  
2.8.2 连续情形 66  
2.8.3 可逆变换（双射） 67  
2.8.4 线性变换的矩 69  
2.8.5 卷积定理 70  
2.8.6 中心极限定理 71  
2.8.7 蒙特卡洛近似 72  
2.9 习题 73  
《概率机器学习：导论》。在线版本。十一月

---

3 概率：多元模型 77  
3.1 多个随机变量的联合分布 77  
3.1.1 协方差 77  
3.1.2 相关性 78  
3.1.3 不相关并不意味着独立 79  
3.1.4 相关性并不意味着因果关系 79  
3.1.5 辛普森悖论 80  
3.2 多元高斯（正态）分布 80  
3.2.1 定义 81  
3.2.2 马氏距离 83  
3.2.3 MVN 的边缘分布与条件分布 * 84  
3.2.4 示例：二维高斯分布的条件化 85  
3.2.5 示例：缺失值插补 * 85  
3.3 线性高斯系统 * 86  
3.3.1 高斯分布的贝叶斯规则 87  
3.3.2 推导 * 87  
3.3.3 示例：推断未知标量 88  
3.3.4 示例：推断未知向量 90  
3.3.5 示例：传感器融合 92  
3.4 指数族 * 93  
3.4.1 定义 93  
3.4.2 示例 94  
3.4.3 对数配分函数是累积生成函数 95  
3.4.4 指数族的最大熵推导 95  
3.5 混合模型 96  
3.5.1 高斯混合模型 97  
3.5.2 伯努利混合模型 98  
3.6 概率图模型 * 99  
3.6.1 表示 100  
3.6.2 推理 102  
3.6.3 学习 102  
3.7 习题 103  
4 统计学 107  
4.1 引言 107  
4.2 最大似然估计（MLE）107  
4.2.1 定义 107  
4.2.2 MLE 的合理性 108  
4.2.3 示例：伯努利分布的 MLE 110  
4.2.4 示例：类别分布的 MLE 111  
4.2.5 示例：一元高斯分布的 MLE 111  
4.2.6 示例：多元高斯分布的 MLE 112  
4.2.7 示例：线性回归的 MLE 114  
4.3 经验风险最小化（ERM）115  
4.3.1 示例：最小化误分类率 116  
作者：Kevin P. Murphy。（C）MIT Press。CC-BY-NC-ND 许可协议

---

4.3.2 替代损失 116  
4.4 其他估计方法 * 117  
4.4.1 矩估计法 117  
4.4.2 在线（递归）估计 119  
4.5 正则化 120  
4.5.1 示例：伯努利分布的MAP估计 121  
4.5.2 示例：多元高斯的MAP估计 * 122  
4.5.3 示例：权重衰减 123  
4.5.4 使用验证集选择正则化器 124  
4.5.5 交叉验证 125  
4.5.6 早停法 126  
4.5.7 使用更多数据 127  
4.6 贝叶斯统计 * 129  
4.6.1 共轭先验 129  
4.6.2 Beta-二项模型 130  
4.6.3 Dirichlet-多项模型 137  
4.6.4 高斯-高斯模型 141  
4.6.5 超越共轭先验 144  
4.6.6 可信区间 146  
4.6.7 贝叶斯机器学习 147  
4.6.8 计算问题 151  
4.7 频率学派统计 * 154  
4.7.1 抽样分布 154  
4.7.2 MLE抽样分布的高斯近似 155  
4.7.3 任意估计量抽样分布的Bootstrap近似 156  
4.7.4 置信区间 157  
4.7.5 警告：置信区间并非可信区间 158  
4.7.6 偏差-方差权衡 159  
4.8 习题 164  
5 决策理论 167  
5.1 贝叶斯决策理论 167  
5.1.1 基础知识 167  
5.1.2 分类问题 169  
5.1.3 ROC曲线 171  
5.1.4 精确率-召回率曲线 174  
5.1.5 回归问题 176  
5.1.6 概率预测问题 177  
5.2 选择"正确"模型 179  
5.2.1 贝叶斯假设检验 179  
5.2.2 贝叶斯模型选择 181  
5.2.3 奥卡姆剃刀 183  
5.2.4 交叉验证与边际似然的联系 184  
5.2.5 信息准则 185  
5.2.6 效应量的后验推断与贝叶斯显著性检验 187  
"概率机器学习：导论"。在线版本。2024年11月23日

---

5.3 频率学派决策理论 189  
5.3.1 计算估计量的风险 189  
5.3.2 一致估计量 192  
5.3.3 可容许估计量 192  
5.4 经验风险最小化 193  
5.4.1 经验风险 193  
5.4.2 结构风险 195  
5.4.3 交叉验证 196  
5.4.4 统计学习理论 * 196  
5.5 频率学派假设检验 * 198  
5.5.1 似然比检验 198  
5.5.2 第一类错误与第二类错误及奈曼-皮尔逊引理 199  
5.5.3 零假设显著性检验 (NHST) 与 p 值 200  
5.5.4 p 值的危害 201  
5.5.5 为何不全是贝叶斯学派？ 202  
5.6 习题 204  
6 信息论 207  
6.1 熵 207  
6.1.1 离散随机变量的熵 207  
6.1.2 交叉熵 209  
6.1.3 联合熵 209  
6.1.4 条件熵 210  
6.1.5 困惑度 211  
6.1.6 连续随机变量的微分熵 * 212  
6.2 相对熵 (KL 散度) * 213  
6.2.1 定义 213  
6.2.2 解释 214  
6.2.3 示例：两个高斯分布之间的 KL 散度 214  
6.2.4 KL 散度的非负性 214  
6.2.5 KL 散度与极大似然估计 215  
6.2.6 前向 KL 与反向 KL 216  
6.3 互信息 * 217  
6.3.1 定义 217  
6.3.2 解释 218  
6.3.3 示例 218  
6.3.4 条件互信息 219  
6.3.5 互信息作为“广义相关系数” 220  
6.3.6 归一化互信息 221  
6.3.7 最大信息系数 221  
6.3.8 数据处理不等式 223  
6.3.9 充分统计量 224  
6.3.10 费诺不等式 * 225  
6.4 习题 226  
作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

线性代数 229  
7.1 引言 229  
7.1.1 符号表示 229  
7.1.2 向量空间 232  
7.1.3 向量与矩阵的范数 234  
7.1.4 矩阵的性质 236  
7.1.5 特殊类型的矩阵 239  
7.2 矩阵乘法 242  
7.2.1 向量-向量积 242  
7.2.2 矩阵-向量积 243  
7.2.3 矩阵-矩阵积 243  
7.2.4 应用：操作数据矩阵 245  
7.2.5 克罗内克积 * 248  
7.2.6 爱因斯坦求和 * 248  
7.3 矩阵求逆 249  
7.3.1 方阵的逆 249  
7.3.2 舒尔补 * 250  
7.3.3 矩阵求逆引理 * 251  
7.3.4 矩阵行列式引理 * 251  
7.3.5 应用：推导多元正态分布的条件分布 * 252  
7.4 特征值分解（EVD） 253  
7.4.1 基础 253  
7.4.2 对角化 254  
7.4.3 对称矩阵的特征值与特征向量 255  
7.4.4 二次型的几何意义 256  
7.4.5 数据的标准化与白化 256  
7.4.6 幂法 258  
7.4.7 收缩 259  
7.4.8 特征向量优化二次型 259  
7.5 奇异值分解（SVD） 259  
7.5.1 基础 259  
7.5.2 SVD与EVD之间的联系 260  
7.5.3 伪逆 261  
7.5.4 SVD与矩阵的值域和零空间 * 262  
7.5.5 截断SVD 264  
7.6 其他矩阵分解 * 264  
7.6.1 LU分解 264  
7.6.2 QR分解 265  
7.6.3 乔列斯基分解 266  
7.7 求解线性方程组 * 266  
7.7.1 求解方阵系统 267  
7.7.2 求解欠定系统（最小范数估计） 267  
7.7.3 求解超定系统（最小二乘估计） 268  
7.8 矩阵微积分 269  
7.8.1 导数 269  
概率机器学习：导论"。在线版本。2020年11月23日

---

7.8.2 梯度 270  
7.8.3 方向导数 270  
7.8.4 全导数 * 271  
7.8.5 雅可比矩阵 271  
7.8.6 黑塞矩阵 272  
7.8.7 常见函数的梯度 272  
7.9 习题 274  

最优化 275  
8.1 引言 275  
8.1.1 局部优化与全局优化 275  
8.1.2 约束优化与无约束优化 277  
8.1.3 凸优化与非凸优化 277  
8.1.4 光滑优化与非光滑优化 281  
8.2 一阶方法 282  
8.2.1 下降方向 284  
8.2.2 步长（学习率） 284  
8.2.3 收敛速率 286  
8.2.4 动量方法 287  
8.3 二阶方法 289  
8.3.1 牛顿法 289  
8.3.2 BFGS 与其他拟牛顿方法 290  
8.3.3 信赖域方法 291  
8.4 随机梯度下降 292  
8.4.1 在有限和问题中的应用 293  
8.4.2 示例：SGD 拟合线性回归 293  
8.4.3 选择步长（学习率） 294  
8.4.4 迭代均值 297  
8.4.5 方差缩减 * 297  
8.4.6 预条件 SGD 298  
8.5 约束优化 302  
8.5.1 拉格朗日乘数 302  
8.5.2 KKT 条件 304  
8.5.3 线性规划 305  
8.5.4 二次规划 306  
8.5.5 混合整数线性规划 * 307  
8.6 近端梯度方法 * 308  
8.6.1 投影梯度下降 308  
8.6.2 $ \ell_{1} $ 范数正则化子的近端算子 310  
8.6.3 量化的近端算子 311  
8.6.4 增量（在线）近端方法 311  
8.7 界优化 * 312  
8.7.1 一般算法 312  
8.7.2 EM 算法 312  
8.7.3 示例：GMM 的 EM 算法 315  

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证

---

8.8 黑箱与无导数优化 319  
8.9 习题 320  

第二部分 线性模型 321  

9 线性判别分析 323  
9.1 引言 323  
9.2 高斯判别分析 323  
9.2.1 二次决策边界 324  
9.2.2 线性决策边界 325  
9.2.3 LDA 与逻辑回归的联系 325  
9.2.4 模型拟合 326  
9.2.5 最近质心分类器 328  
9.2.6 Fisher 线性判别分析 * 328  
9.3 朴素贝叶斯分类器 332  
9.3.1 示例模型 332  
9.3.2 模型拟合 333  
9.3.3 贝叶斯朴素贝叶斯 334  
9.3.4 朴素贝叶斯与逻辑回归的联系 335  
9.4 生成式与判别式分类器 336  
9.4.1 判别式分类器的优势 336  
9.4.2 生成式分类器的优势 337  
9.4.3 处理缺失特征 337  
9.5 习题 338  

10 逻辑回归 339  
10.1 引言 339  
10.2 二项逻辑回归 339  
10.2.1 线性分类器 339  
10.2.2 非线性分类器 340  
10.2.3 最大似然估计 342  
10.2.4 随机梯度下降 345  
10.2.5 感知机算法 346  
10.2.6 迭代重加权最小二乘 346  
10.2.7 最大后验估计 348  
10.2.8 标准化 350  
10.3 多项逻辑回归 350  
10.3.1 线性与非线性分类器 351  
10.3.2 最大似然估计 351  
10.3.3 基于梯度的优化 354  
10.3.4 边界优化 354  
10.3.5 最大后验估计 355  
10.3.6 最大熵分类器 356  
10.3.7 层次分类 357

---

10.3.8 处理大量类别 358  
10.4 稳健逻辑回归 * 360  
10.4.1 似然的混合模型 360  
10.4.2 双温度损失 361  
10.5 贝叶斯逻辑回归 * 363  
10.5.1 拉普拉斯近似 363  
10.5.2 近似后验预测 366  
10.6 习题 367  

11 线性回归 371  
11.1 引言 371  
11.2 最小二乘线性回归 371  
11.2.1 术语 371  
11.2.2 最小二乘估计 372  
11.2.3 计算最大似然估计的其他方法 376  
11.2.4 拟合优度度量 380  
11.3 岭回归 381  
11.3.1 计算最大后验估计 382  
11.3.2 岭回归与主成分分析的联系 383  
11.3.3 选择正则化强度 384  
11.4 套索回归 385  
11.4.1 拉普拉斯先验的最大后验估计（ $ \ell_1 $ 正则化） 385  
11.4.2 为什么 $ \ell_1 $ 正则化会产生稀疏解？ 386  
11.4.3 硬阈值与软阈值 387  
11.4.4 正则化路径 389  
11.4.5 最小二乘、套索、岭回归与子集选择的比较 390  
11.4.6 变量选择一致性 392  
11.4.7 组套索 393  
11.4.8 弹性网络（岭回归与套索结合） 396  
11.4.9 优化算法 397  
11.5 回归样条 * 399  
11.5.1 B样条基函数 399  
11.5.2 使用样条基拟合线性模型 401  
11.5.3 平滑样条 401  
11.5.4 广义可加模型 401  
11.6 稳健线性回归 * 402  
11.6.1 拉普拉斯似然 402  
11.6.2 学生t似然 404  
11.6.3 胡贝尔损失 404  
11.6.4 RANSAC 404  
11.7 贝叶斯线性回归 * 405  
11.7.1 先验 405  
11.7.2 后验 405  
11.7.3 示例 406  
11.7.4 计算后验预测 406  

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

11.7.5 中心化的优势 408  
11.7.6 处理多重共线性 409  
11.7.7 自动相关性判定（ARD）* 410  
11.8 习题 411  

12 广义线性模型 * 415  
12.1 引言 415  
12.2 示例 415  
12.2.1 线性回归 416  
12.2.2 二项回归 416  
12.2.3 泊松回归 417  
12.3 非规范连接函数的GLMs 417  
12.4 最大似然估计 418  
12.5 实例：预测保险索赔 419  

第三部分 深度神经网络 423  

13 表格数据的神经网络 425  
13.1 引言 425  
13.2 多层感知机（MLPs）426  
13.2.1 XOR问题 427  
13.2.2 可微分MLPs 428  
13.2.3 激活函数 428  
13.2.4 示例模型 430  
13.2.5 深度的重要性 434  
13.2.6 “深度学习革命” 435  
13.2.7 与生物学的联系 436  
13.3 反向传播 438  
13.3.1 正向模式与反向模式微分 438  
13.3.2 多层感知机的反向模式微分 440  
13.3.3 常见层的向量-雅可比乘积 441  
13.3.4 计算图 444  
13.4 训练神经网络 446  
13.4.1 调整学习率 447  
13.4.2 梯度消失与梯度爆炸 447  
13.4.3 非饱和激活函数 448  
13.4.4 残差连接 451  
13.4.5 参数初始化 452  
13.4.6 并行训练 454  
13.5 正则化 455  
13.5.1 早停法 455  
13.5.2 权重衰减 455  
13.5.3 稀疏DNNs 455  
13.5.4 Dropout 455  

“概率机器学习：导论”。在线版本。2024年11月23日

---

13.5.5 贝叶斯神经网络 457  
13.5.6 （随机）梯度下降的正则化效果 * 457  
13.5.7 过参数化模型 459  
13.6 其他类型的前馈网络 * 459  
13.6.1 径向基函数网络 459  
13.6.2 专家混合模型 461  
13.7 习题 463  
14 面向图像的神经网络 467  
14.1 引言 467  
14.2 常用层 468  
14.2.1 卷积层 468  
14.2.2 池化层 475  
14.2.3 整体组合 476  
14.2.4 归一化层 476  
14.3 图像分类的常见架构 479  
14.3.1 LeNet 479  
14.3.2 AlexNet 481  
14.3.3 GoogLeNet（Inception）482  
14.3.4 ResNet 483  
14.3.5 DenseNet 484  
14.3.6 神经架构搜索 485  
14.4 其他形式的卷积 * 486  
14.4.1 空洞卷积 486  
14.4.2 转置卷积 486  
14.4.3 深度可分离卷积 488  
14.5 利用CNN解决其他判别式视觉任务 * 488  
14.5.1 图像标注 488  
14.5.2 目标检测 489  
14.5.3 实例分割 490  
14.5.4 语义分割 491  
14.5.5 人体姿态估计 492  
14.6 通过反转CNN生成图像 * 493  
14.6.1 将训练好的分类器转换为生成模型 493  
14.6.2 图像先验 494  
14.6.3 可视化CNN学习的特征 495  
14.6.4 深度梦境 496  
14.6.5 神经风格迁移 497  
15 面向序列的神经网络 503  
15.1 引言 503  
15.2 循环神经网络（RNN）503  
15.2.1 Vec2Seq（序列生成）503  
15.2.2 Seq2Vec（序列分类）505  
15.2.3 Seq2Seq（序列翻译）507  
作者：Kevin P. Murphy。（C）MIT出版社。CC-BY-NC-ND许可证。

---

15.2.4 教师强制 509  
15.2.5 随时间反向传播 510  
15.2.6 梯度消失与爆炸 511  
15.2.7 门控与长期记忆 512  
15.2.8 束搜索 515  
15.3 一维卷积神经网络 516  
15.3.1 用于序列分类的一维卷积神经网络 516  
15.3.2 用于序列生成的因果一维卷积神经网络 517  
15.4 注意力机制 518  
15.4.1 注意力作为软字典查找 519  
15.4.2 核回归作为非参数注意力 520  
15.4.3 参数化注意力 521  
15.4.4 带注意力的序列到序列 522  
15.4.5 带注意力的序列到向量（文本分类） 523  
15.4.6 带注意力的序列+序列到向量（文本对分类） 523  
15.4.7 软注意力与硬注意力 525  
15.5 Transformer 526  
15.5.1 自注意力 526  
15.5.2 多头注意力 527  
15.5.3 位置编码 528  
15.5.4 整合所有组件 529  
15.5.5 比较Transformer、卷积神经网络与循环神经网络 531  
15.5.6 面向图像的Transformer * 532  
15.5.7 其他Transformer变体 * 533  
15.6 高效Transformer * 533  
15.6.1 固定的不可学习的局部注意力模式 534  
15.6.2 可学习的稀疏注意力模式 535  
15.6.3 记忆与循环方法 535  
15.6.4 低秩与核方法 535  
15.7 语言模型与无监督表示学习 537  
15.7.1 ELMo 538  
15.7.2 BERT 538  
15.7.3 GPT 542  
15.7.4 T5 543  
15.7.5 讨论 543  

V 非参数模型 545  

6 基于样本的方法 547  

16.1 K近邻分类 547  
16.1.1 示例 548  
16.1.2 维度灾难 548  
16.1.3 降低速度与内存需求 550  
16.1.4 开放集识别 550  

概率机器学习：导论》。在线版本。2022年11月23日。

---

16.2 学习距离度量 551  
16.2.1 线性与凸方法 552  
16.2.2 深度度量学习 554  
16.2.3 分类损失 554  
16.2.4 排序损失（Ranking Losses） 555  
16.2.5 加速排序损失优化 556  
16.2.6 DML的其他训练技巧 559  
16.3 核密度估计（KDE） 560  
16.3.1 密度核 560  
16.3.2 Parzen窗密度估计 561  
16.3.3 如何选择带宽参数 562  
16.3.4 从KDE到KNN分类 563  
16.3.5 核回归 563  
17 核方法 * 567  
17.1 Mercer核 567  
17.1.1 Mercer定理 568  
17.1.2 一些常用的Mercer核 569  
17.2 高斯过程 574  
17.2.1 无噪声观测 574  
17.2.2 有噪声观测 575  
17.2.3 与核回归的对比 576  
17.2.4 权重空间与函数空间 577  
17.2.5 数值问题 577  
17.2.6 估计核函数 578  
17.2.7 用于分类的高斯过程 581  
17.2.8 与深度学习的联系 582  
17.2.9 将高斯过程扩展到大规模数据集 582  
17.3 支持向量机（SVM） 585  
17.3.1 大间隔分类器 585  
17.3.2 对偶问题 587  
17.3.3 软间隔分类器 589  
17.3.4 核技巧 590  
17.3.5 将SVM输出转换为概率 591  
17.3.6 与逻辑回归的联系 591  
17.3.7 SVM的多类分类 592  
17.3.8 如何选择正则化参数C 593  
17.3.9 核岭回归 594  
17.3.10 用于回归的SVM 595  
17.4 稀疏向量机 597  
17.4.1 相关向量机（RVM） 598  
17.4.2 稀疏与密集核方法的对比 598  
17.5 习题 601  
18 树、森林、Bagging与Boosting 603  
作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

18.1 分类与回归树 (CART) 603  
18.1.1 模型定义 603  
18.1.2 模型拟合 605  
18.1.3 正则化 606  
18.1.4 处理缺失输入特征 606  
18.1.5 优缺点 606  
18.2 集成学习 608  
18.2.1 堆叠法 608  
18.2.2 集成并非贝叶斯模型平均 609  
18.3 Bagging 609  
18.4 随机森林 610  
18.5 提升方法 611  
18.5.1 前向分阶段加性建模 612  
18.5.2 二次损失与最小二乘提升 612  
18.5.3 指数损失与 AdaBoost 613  
18.5.4 LogitBoost 616  
18.5.5 梯度提升 616  
18.6 解释树集成模型 620  
18.6.1 特征重要性 621  
18.6.2 部分依赖图 623  
V 超越监督学习 625  
19 利用较少标注样本的学习 627  
19.1 数据增强 627  
19.1.1 示例 627  
19.1.2 理论依据 628  
19.2 迁移学习 628  
19.2.1 微调 629  
19.2.2 适配器 630  
19.2.3 有监督预训练 631  
19.2.4 无监督预训练（自监督学习） 632  
19.2.5 域自适应 637  
19.3 半监督学习 638  
19.3.1 自训练与伪标签 638  
19.3.2 熵最小化 639  
19.3.3 协同训练 642  
19.3.4 图上的标签传播 643  
19.3.5 一致性正则化 644  
19.3.6 深度生成模型 * 646  
19.3.7 自监督与半监督学习的结合 649  
19.4 主动学习 650  
19.4.1 决策论方法 650  
19.4.2 信息论方法 650  
“概率机器学习：导论”。在线版本。2024年11月23日

---

19.4.3 批量主动学习 651  
19.5 元学习 651  
19.5.1 模型无关元学习 (MAML) 652  
19.6 小样本学习 653  
19.6.1 匹配网络 653  
19.7 弱监督学习 655  
19.8 习题 655  
0 降维 657  
20.1 主成分分析 (PCA) 657  
20.1.1 示例 657  
20.1.2 算法推导 659  
20.1.3 计算问题 662  
20.1.4 选择潜在维度数量 664  
20.2 因子分析 * 666  
20.2.1 生成模型 667  
20.2.2 概率PCA 668  
20.2.3 FA/PPCA的EM算法 669  
20.2.4 参数不可识别性 671  
20.2.5 非线性因子分析 673  
20.2.6 因子分析混合模型 674  
20.2.7 指数族因子分析 675  
20.2.8 配对数据的因子分析模型 677  
20.3 自编码器 679  
20.3.1 瓶颈自编码器 680  
20.3.2 去噪自编码器 681  
20.3.3 收缩自编码器 682  
20.3.4 稀疏自编码器 683  
20.3.5 变分自编码器 683  
20.4 流形学习 * 689  
20.4.1 什么是流形？ 689  
20.4.2 流形假设 689  
20.4.3 流形学习方法 690  
20.4.4 多维缩放 (MDS) 691  
20.4.5 Isomap 694  
20.4.6 核PCA 695  
20.4.7 最大方差展开 (MVU) 697  
20.4.8 局部线性嵌入 (LLE) 697  
20.4.9 拉普拉斯特征映射 699  
20.4.10 t-SNE 701  
20.5 词嵌入 705  
20.5.1 潜在语义分析/索引 705  
20.5.2 Word2vec 707  
20.5.3 GloVe 710  
20.5.4 词类比 710  
作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND许可证

---

20.5.5 RAND-WALK 词嵌入模型 711  
20.5.6 上下文词嵌入 712  
20.6 习题 712  
  
21 聚类 715  
21.1 引言 715  
21.1.1 评估聚类方法的输出 715  
21.2 层次凝聚聚类 717  
21.2.1 算法 718  
21.2.2 示例 720  
21.2.3 扩展 721  
21.3 K 均值聚类 722  
21.3.1 算法 722  
21.3.2 示例 722  
21.3.3 向量量化 724  
21.3.4 K-means++ 算法 725  
21.3.5 K-medoids 算法 725  
21.3.6 加速技巧 726  
21.3.7 选择聚类数 K 726  
21.4 基于混合模型的聚类 729  
21.4.1 高斯混合模型 730  
21.4.2 伯努利混合模型 733  
21.5 谱聚类 * 734  
21.5.1 归一化割 734  
21.5.2 图拉普拉斯特征向量编码聚类 735  
21.5.3 示例 736  
21.5.4 与其他方法的联系 737  
21.6 双聚类 * 737  
21.6.1 基本双聚类 738  
21.6.2 嵌套分区模型 (Crosscat) 738  
  
22 推荐系统 741  
22.1 显式反馈 741  
22.1.1 数据集 741  
22.1.2 协同过滤 742  
22.1.3 矩阵分解 743  
22.1.4 自编码器 745  
22.2 隐式反馈 747  
22.2.1 贝叶斯个性化排序 747  
22.2.2 因式分解机 748  
22.2.3 神经矩阵分解 749  
22.3 利用辅助信息 749  
22.4 探索-利用权衡 750  
  
23 图嵌入 * 753  
  
“概率机器学习：导论”。在线版本。2024年11月23日

---

23.1 引言 753  
23.2 图嵌入作为编码器/解码器问题 754  
23.3 浅层图嵌入 756  
23.3.1 无监督嵌入 757  
23.3.2 基于距离的：欧几里得方法 757  
23.3.3 基于距离的：非欧几里得方法 758  
23.3.4 基于外积的：矩阵分解方法 758  
23.3.5 基于外积的：Skip-gram 方法 759  
23.3.6 有监督嵌入 761  
23.4 图神经网络 762  
23.4.1 消息传递 GNN 762  
23.4.2 谱图卷积 763  
23.4.3 空间图卷积 763  
23.4.4 非欧几里得图卷积 765  
23.5 深度图嵌入 765  
23.5.1 无监督嵌入 766  
23.5.2 半监督嵌入 768  
23.6 应用 769  
23.6.1 无监督应用 769  
23.6.2 有监督应用 771  
A 符号说明 773  
A.1 引言 773  
A.2 常用数学符号 773  
A.3 函数 774  
A.3.1 一元常见函数 774  
A.3.2 二元常见函数 774  
A.3.3 大于2元常见函数 774  
A.4 线性代数 775  
A.4.1 通用记法 775  
A.4.2 向量 775  
A.4.3 矩阵 775  
A.4.4 矩阵微积分 776  
A.5 优化 776  
A.6 概率论 777  
A.7 信息论 777  
A.8 统计与机器学习 778  
A.8.1 有监督学习 778  
A.8.2 无监督学习与生成模型 778  
A.8.3 贝叶斯推断 778  
A.9 缩写 779  
索引 781  
参考文献 798  
作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可协议

---

请提供需要翻译的英文 Markdown 文本。

---

2012年，我出版了一本1200页的著作《Machine Learning: A Probabilistic Perspective》，该书在当时以概率建模的统一视角，相当全面地涵盖了机器学习（ML）领域。该书广受好评，并于2013年获得De Groot奖。

2012年也被普遍认为是“深度学习革命”的开端。术语“深度学习”指的是机器学习的一个分支，它基于深度神经网络（DNNs）——具有多层处理过程的非线性函数（因此得名“深度”）。尽管这一基本技术已存在多年，但在2012年，[KSH12] 使用深度神经网络以巨大优势赢得了ImageNet图像分类挑战，从而引起了更广泛学术界的关注。在其他难题（如语音识别）上的相关进展也几乎在同一时间出现（参见例如 [Cir+10; Cir+11; Hin+12]）。这些突破得益于硬件技术的进步（特别是将快速图形处理单元（GPUs）从视频游戏重新用于机器学习）、数据收集技术的进步（特别是使用众包工具，如亚马逊的Mechanical Turk平台，来收集大规模标注数据集，例如ImageNet），以及各种新的算法思想——其中部分将在本书中介绍。

自2012年以来，深度学习领域呈爆发式发展，新进展层出不穷。该技术的商业成功及其广泛的应用场景也极大激发了人们对这一领域的兴趣。因此，在2018年，我决定撰写本书的第二版，试图总结其中部分进展。

到2020年3月，我的第二版草稿已膨胀至约1600页，而仍有众多主题未涵盖。因此，麻省理工学院出版社（MIT Press）告知我需要将本书分为两卷。随后，COVID-19疫情爆发。我决定暂搁书稿写作，转而协助开发谷歌曝光通知应用的风险评分算法 [MKS21]，并参与多项预测项目 [Wah+22]。然而，到2020年秋季，我决定回归书稿工作。

为了弥补失去的时间，我邀请了几位同事帮忙撰写各章节（见下文致谢）。最终成果是两本新书：您正在阅读的《Probabilistic Machine Learning: An Introduction》以及作为其续篇的《Probabilistic Machine Learning: Advanced Topics》[Mur23]。这两本书共同尝试以我在2012年著作中使用的同一统一视角——概率建模与贝叶斯决策理论——来呈现约2021年机器学习领域的广泛概览。

2012年著作中的几乎所有内容都得到了保留，但现在被大致均等地分置于两册之中。

---

在两本新书之间。此外，每本新书都包含大量新材料，涵盖深度学习以及该领域其他部分的进展，例如生成模型、变分推断和强化学习。

为了使这本入门书更加自成体系并对学生有用，我添加了一些背景材料，例如优化和线性代数等主题，这些材料在2012年的书中因篇幅限制而被省略。可在入门课程中跳过的高级材料，在章节标题中用 * 标注。部分章节末尾设有习题。标有 † 的习题解答可通过联系 MIT Press 提供给有资质的教师；所有其他习题的解答可在线获取，网址为 https://probml.github.io/pml-book/book1.html，同时还提供了额外的教学材料（例如，图表和幻灯片）。

另一个重大变化是，所有软件现在都使用 Python 而非 Matlab。（将来，我们可能会创建代码的 Julia 版本。）新代码利用了标准 Python 库，例如 NumPy、Scikit-learn、JAX、PyTorch、TensorFlow、PyMC 等。

如果图注显示“Generated by iris_plot.ipynb”，则您可以在 probml.github.io/notebooks#iris_plot.ipynb 找到对应的 Jupyter notebook。点击本书 PDF 版本中的图形链接将跳转到这个 notebook 列表。点击 notebook 链接将在 Google Colab 中打开，它让您可以轻松自行复现图形，并修改底层源代码以更深入地理解这些方法。（Colab 为您提供免费 GPU 访问权限，这对于一些计算量较大的演示非常有用。）

#### 致谢

我要感谢以下人士在本书编写过程中给予的帮助：

• Zico Kolter（CMU），他帮助撰写了第7章（线性代数）的部分内容。

- Frederik Kunstner、Si Yi Meng、Aaron Mishkin、Sharan Vaswani 和 Mark Schmidt，他们帮助撰写了第8章（优化）的部分内容。

• Mathieu Blondel（Google），他帮助撰写了第13.3节（反向传播）。

• Krzysztof Choromanski（Google），他撰写了第15.6节（高效Transformer *）。

• Colin Raffel（UNC），他帮助撰写了第19.2节（迁移学习）和第19.3节（半监督学习）。

• Bryan Perozzi（Google）、Sami Abu-El-Haija（USC）和 Ines Chami，他们帮助撰写了第23章（图嵌入 *）。

• John Fearns 和 Peter Cerno 仔细校对了本书。

• GitHub 社区的许多成员发现了拼写错误等（参见 https://github.com/probml/pml-book/issues?q=is:issue 获取问题列表）。

• MIT Press 征集的4位匿名审稿人。

- Mahmoud Soliman 编写了连接 latex、colab、github 等所有神奇的基础代码，并教会了我关于 GCP 和 TPUs 的知识。

● 2021 届 Google Summer of Code 学生，他们为本书编写了代码：Aleyna Kara、Srikar Jilugu、Drishti Patel、Ming Liang Ang、Gerardo Durán-Martín。（参见 https://probml.github.io/pml-book/gsoc/gsoc2021.html 了解他们的贡献摘要。）

- Zeel B Patel、Karm Patel、Nitish Sharma、Ankita Kumari Jain 和 Nipun Batra 在本书首次出版后帮助改进了图表和代码。

• GitHub 社区的许多成员贡献了代码（参见 https://github.com/probml/pml-book/issues?q=is:issue 获取问题列表）。

---

probml/pyprobml#acknowledgements).

- $ [Zha+20] $、$ [Gér17] $ 和 $ [Mar18] $ 的作者们允许我重用或修改他们优秀书籍中的一些开源代码。

• 我在 Google 的经理 Doug Eck，允许我利用公司时间编写本书。

• 我的妻子 Margaret，允许我利用家庭时间编写本书。

##### 关于封面

封面展示了一个神经网络（第13章）用于将手写数字 $ x $ 分类为 10 个类别标签 $ y \in \{0, 1, \ldots, 9\} $ 之一。右侧的直方图是模型的输出，对应于条件概率分布 $ p(y | \boldsymbol{x}) $。$ ^{1} $

#### 更新日志

所有更改列在 https://github.com/probml/pml-book/issues?q=is%3Aissue+is%3Aclosed。

• 2022年3月。第一次印刷。

• 2023年4月。第二次印刷。

• 2025年1月。第三次印刷。

---

请提供需要翻译的Markdown文本。

---

## 1 引言

### 1.1 什么是机器学习？

机器学习（ML）的一个流行定义来自汤姆·米切尔（Tom Mitchell）[Mit97]：

如果计算机程序在任务 T 上的性能（以性能度量 P 衡量）随着经验 E 而提高，则称该程序从经验 E 中学习。

因此，机器学习有许多不同的类型，具体取决于我们希望系统学习的任务 T 的性质、我们用于评估系统的性能度量 P 的性质，以及我们提供给系统的训练信号或经验 E 的性质。

在本书中，我们将从概率视角介绍最常见的机器学习类型。大致而言，这意味着我们将所有未知量（例如，对未来某个感兴趣量的预测，如明天的温度，或某个模型的参数）视为随机变量，这些变量被赋予概率分布，描述变量可能取值的加权集合。（如有必要，请参阅第 2 章快速回顾概率基础。）

我们采用概率方法主要有两个原因。首先，正如我们在第 5.1 节所述，它是在不确定性下进行决策的最优方法。其次，概率建模是科学和工程中大多数其他领域使用的语言，因此为这些领域提供了一个统一的框架。正如 DeepMind 研究员 Shakir Mohamed 所说：$ ^{1} $

几乎所有机器学习都可以从概率角度来审视，这使得概率思维成为基础。当然，这并非唯一的观点。但正是通过这一视角，我们才能将机器学习中的工作与每一个其他计算科学领域联系起来，无论是随机优化、控制理论、运筹学、计量经济学、信息论、统计物理还是生物统计学。仅此一点，掌握概率思维就至关重要。

### 1.2 监督学习

监督学习是最常见的机器学习形式。在这个问题中，任务 $ T $ 是学习从输入 $\boldsymbol{x} \in \mathcal{X}$ 到输出 $\boldsymbol{y} \in \mathcal{Y}$ 的映射 $ f $。输入 $\boldsymbol{x}$ 也被称为特征。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_195_118_417_337.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_475_118_696_336.jpg" alt="图像" width="19%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_756_118_974_337.jpg" alt="图像" width="18%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 1.1: 三种鸢尾花：Setosa、Versicolor 和 Virginica。经 Dennis Kramb 和 SIGNA 许可使用。</div>



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>索引</td><td style='text-align: center; word-wrap: break-word;'>sl</td><td style='text-align: center; word-wrap: break-word;'>sw</td><td style='text-align: center; word-wrap: break-word;'>pl</td><td style='text-align: center; word-wrap: break-word;'>pw</td><td style='text-align: center; word-wrap: break-word;'>标签</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>5.1</td><td style='text-align: center; word-wrap: break-word;'>3.5</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>Setosa</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>4.9</td><td style='text-align: center; word-wrap: break-word;'>3.0</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>0.2</td><td style='text-align: center; word-wrap: break-word;'>Setosa</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>50</td><td style='text-align: center; word-wrap: break-word;'>7.0</td><td style='text-align: center; word-wrap: break-word;'>3.2</td><td style='text-align: center; word-wrap: break-word;'>4.7</td><td style='text-align: center; word-wrap: break-word;'>1.4</td><td style='text-align: center; word-wrap: break-word;'>Versicolor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>...</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>149</td><td style='text-align: center; word-wrap: break-word;'>5.9</td><td style='text-align: center; word-wrap: break-word;'>3.0</td><td style='text-align: center; word-wrap: break-word;'>5.1</td><td style='text-align: center; word-wrap: break-word;'>1.8</td><td style='text-align: center; word-wrap: break-word;'>Virginica</td></tr></table>

<div style="text-align: center;">表 1.1: 鸢尾花设计矩阵的一个子集。特征包括：花萼长度、花萼宽度、花瓣长度、花瓣宽度。每个类别有 50 个样本。</div>


协变量或预测变量；这通常是一个固定维度的数值向量，例如一个人的身高和体重，或者图像中的像素。在这种情况下，$\mathcal{X} = \mathbb{R}^D$，其中 $D$ 是向量的维度（即输入特征的数量）。输出 $\mathbf{y}$ 也被称为标签、目标或响应。$^2$ 经验 $E$ 以一组 $N$ 个输入-输出对 $\mathcal{D} = \{(\mathbf{x}_n, \mathbf{y}_n)\}_{n=1}^N$ 的形式给出，称为训练集。（$N$ 被称为样本量。）性能度量 $P$ 取决于我们预测的输出类型，如下所述。

#### 1.2.1 分类

在分类问题中，输出空间是一组 $C$ 个无序且互斥的标签，称为类别，$\mathcal{Y} = \{1, 2, \ldots, C\}$。根据输入预测类别标签的问题也称为模式识别。（如果只有两个类别，通常记为 $y \in \{0, 1\}$ 或 $y \in \{-1, +1\}$，称为二分类。）

##### 1.2.1.1 示例：鸢尾花分类

作为一个例子，考虑将鸢尾花分类为三个亚种（Setosa、Versicolor 和 Virginica）的问题。图 1.1 展示了每个类别的一个例子。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_273_123_878_543.jpg" alt="图像" width="52%" /></div>


<div style="text-align: center;">图 1.2: 图像分类问题的示意图。来源：https://cs231n.github.io/。经 Andrej Karpathy 许可使用。</div>


在图像分类中，输入空间 $\mathcal{X}$ 是图像的集合，这是一个非常高维的空间：对于一张具有 $C = 3$ 个通道（如 RGB）和 $D_1 \times D_2$ 个像素的彩色图像，我们有 $\mathcal{X} = \mathbb{R}^D$，其中 $D = C \times D_1 \times D_2$。（实际中，我们通常用整数表示每个像素的强度，范围一般为 $\{0, 1, \ldots, 255\}$，但为了符号简洁，我们假设输入为实数值。）学习从图像到标签的映射 $f: \mathcal{X} \to \mathcal{Y}$ 相当具有挑战性，如图 1.2 所示。然而，通过某些类型的函数可以应对这一问题，例如卷积神经网络（CNN），我们将在第 14.1 节讨论。

幸运的是，一些植物学家已经确定了 4 个简单但信息量丰富的数值特征——花萼长度、花萼宽度、花瓣长度、花瓣宽度——可用于区分三种鸢尾花。在本节中，为简单起见，我们将使用这个更低维的输入空间 $\mathcal{X} = \mathbb{R}^4$。鸢尾花数据集是一个包含 150 个带标签的鸢尾花样本的集合，每种类型各 50 个，由上述 4 个特征描述。它被广泛用作示例，因为它规模小且易于理解。（本书后续将讨论更大、更复杂的数据集。）

当我们拥有小规模的特征数据集时，通常将它们存储在一个 $N \times D$ 的矩阵中，其中每一行代表一个样本，每一列代表一个特征。这被称为设计矩阵；表 1.1 给出了一个示例。$^{3}$

鸢尾花数据集是表格数据的一个例子。当输入是可变大小（例如，单词序列或社交网络）而非固定长度的向量时，数据通常以另一种方式存储。

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_250_134_930_671.jpg" alt="图片" width="59%" /></div>


<div style="text-align: center;">花萼长度（cm） 花萼宽度（cm） 花瓣长度（cm） 花瓣宽度（cm）</div>


<div style="text-align: center;">图 1.3：鸢尾数据集的成对散点图可视化。对角线展示了每个类别下每个特征的边际分布。非对角线部分则包含了所有可能特征对的散点图。由 iris_plot.ipynb 生成。</div>


以不同于设计矩阵的某种格式存在。然而，这类数据通常会被转换为固定大小的特征表示（这一过程称为 $ \underline{\text{特征化}} $），从而隐式地生成一个设计矩阵，便于后续处理。我们在第 1.5.4.1 节中给出了一个示例，讨论了序列数据的“词袋”表示。

##### 1.2.1.2 探索性数据分析

在处理机器学习（ML）问题之前，通常最好进行探索性数据分析，以观察是否存在任何明显的模式（这可能提示选择哪种方法），或者数据是否存在明显问题（例如标签噪声或异常值）。

对于特征数量较少的表格数据，通常绘制成对图（pair plot），其中面板 $(i,j)$ 显示变量 $i$ 和 $j$ 的散点图，对角线 $(i,i)$ 显示变量 $i$ 的边际密度；所有图可按类别标签进行颜色编码——参见图 1.3 的示例。

对于高维数据，通常首先进行降维，然后

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_192_268_572_546.jpg" alt="图像" width="32%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_603_168_986_533.jpg" alt="图像" width="33%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图 1.4: 深度为2的决策树应用于鸢尾花数据集的示例，仅使用花瓣长度和花瓣宽度特征。叶节点根据预测类别进行颜色编码。从根节点传递到某个节点的训练样本数量显示在每个方框内；我们展示了每个类别的样本落入该节点的数量。该计数向量可以归一化，以获得每个节点上类标签的分布。然后我们可以选择多数类。改编自[Gér19]的图6.1和6.2。由iris_dtree.ipynb生成。</div>

以便在二维或三维空间中可视化数据。我们将在第20章讨论降维方法。

##### 1.2.1.3 学习一个分类器

从图1.3中，我们可以看到Setosa类别很容易与其他两个类别区分开来。例如，假设我们创建以下决策规则：

$$  f(\boldsymbol{x};\boldsymbol{\theta})=\begin{cases}Setosa & \text{若花瓣长度}<2.45\\ Versicolor\ 或\ Virginica & \text{否则}\end{cases}   \tag*{(1.1)}$$

这是一个非常简单的分类器示例，我们在此将输入空间划分为两个区域，由一维（1d）决策边界 $ x_{花瓣长度} = 2.45 $ 定义。位于该边界左侧的点被分类为Setosa；右侧的点则为Versicolor或Virginica。

我们看到，该规则完美地分类了Setosa样本，但未能正确分类Virginica和Versicolor样本。为了提高性能，我们可以递归地划分空间，即分割分类器出错的区域。例如，我们可以添加另一个决策规则，应用于未通过第一个测试的输入，以检查花瓣宽度是否小于1.75厘米（若是则预测为Versicolor）或大于该值（若是则预测为Virginica）。我们可以将这些嵌套规则组织成一种树结构。

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND许可证

---

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td rowspan="2"></td><td colspan="4">估计</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Setosa</td><td style='text-align: center; word-wrap: break-word;'>Versicolor</td><td style='text-align: center; word-wrap: break-word;'>Virginica</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td rowspan="3">真实</td><td style='text-align: center; word-wrap: break-word;'>Setosa</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Versicolor</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Virginica</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">表1.2：鸢尾花分类的假设性非对称损失矩阵。</div>

称为决策树，如图1.4a所示。这产生了图1.4b所示的二维决策面。

我们可以通过为每个内部节点存储所使用的特征索引以及对应的阈值来表示该树。我们将所有这些参数记为 $\theta$。我们将在第18.1节讨论如何学习这些参数。

##### 1.2.1.4 经验风险最小化

监督学习的目标是自动得出如图1.4a所示的分类模型，从而可靠地预测任意给定输入的标签。衡量该任务性能的一种常见方法是基于训练集上的误分类率：

$$  \mathcal{L}(\boldsymbol{\theta})\triangleq\frac{1}{N}\sum_{n=1}^{N}\mathbb{I}\left(y_{n}\neq f(\boldsymbol{x}_{n};\boldsymbol{\theta})\right)   \tag*{(1.2)}$$

其中 $\mathbb{I}(e)$ 是二元指示函数，当条件 e 为真时返回1，否则返回0，即：

$$  \mathbb{I}(e)=\left\{\begin{array}{ll}1&\text{如果 } e \text{ 为真}\\ 0&\text{如果 } e \text{ 为假}\end{array}\right.   \tag*{(1.3)}$$

这假设所有错误代价相同。然而，某些错误可能比其他错误代价更高。例如，假设我们在野外觅食，发现了一些鸢尾花。进一步假设Setosa和Versicolor是可食用的，但Virginica有毒。在这种情况下，我们可以使用表1.2所示的非对称损失函数 $\ell(y, \hat{y})$。

然后我们可以将经验风险定义为预测器在训练集上的平均损失：

$$  \mathcal{L}(\boldsymbol{\theta})\triangleq\frac{1}{N}\sum_{n=1}^{N}\ell(y_{n},f(\boldsymbol{x}_{n};\boldsymbol{\theta}))   \tag*{(1.4)}$$

我们看到，当我们使用0-1损失来比较真实标签与预测时，误分类率式(1.2)等于经验风险：

$$  \ell_{01}(y,\hat{y})=\mathbb{I}\left(y\neq\hat{y}\right)   \tag*{(1.5)}$$

更多细节见第5.1节。

---

定义模型拟合或训练问题的一种方式是，找到一组参数，使其在训练集上的经验风险最小化：

$$  \hat{\boldsymbol{\theta}}=\underset{\boldsymbol{\theta}}{\arg\min}\mathcal{L}(\boldsymbol{\theta})=\underset{\boldsymbol{\theta}}{\arg\min}\frac{1}{N}\sum_{n=1}^{N}\ell(y_{n},f(\boldsymbol{x}_{n};\boldsymbol{\theta}))   \tag*{(1.6)}$$

这被称为**经验风险最小化**。

然而，我们的真正目标是使未来未见数据的期望损失最小化。也就是说，我们希望模型具有泛化能力，而不仅仅是在训练集上表现良好。我们将在第 1.2.3 节讨论这一重要观点。

##### 1.2.1.5 不确定性

[我们必须避免] 由于对世界概率本质的无知，以及出于在理应看到灰色地带的地方追求非黑即白的欲望，而产生的虚假自信。——伊曼努尔·康德，玛丽亚·科尼科娃 [Kon20] 的转述。

在许多情况下，由于对输入-输出映射缺乏了解（这称为**认知不确定性**或模型不确定性），和/或映射本身固有的（不可约的）随机性（这称为**偶然不确定性**或数据不确定性），我们无法根据输入完美预测精确的输出。

在我们的预测中表示不确定性对于各种应用可能很重要。例如，让我们回到有毒花朵的例子，其损失矩阵如表 1.2 所示。如果我们以高概率预测该花是维吉尼亚鸢尾，那么就不应该吃它。或者，我们可以采取信息收集行动（例如进行诊断测试）来降低不确定性。关于如何在存在不确定性的情况下做出最优决策，请参见第 5.1 节。

我们可以使用以下条件概率分布来捕捉不确定性：

 $$ p(y=c|\boldsymbol{x};\boldsymbol{\theta})=f_{c}(\boldsymbol{x};\boldsymbol{\theta}) $$ 

其中 $ f : \mathcal{X} \to [0,1]^C $ 将输入映射到 $ C $ 个可能输出标签上的概率分布。由于 $ f_c(\mathbf{x}; \boldsymbol{\theta}) $ 返回类别标签 $ c $ 的概率，我们要求每个 $ c $ 满足 $ 0 \leq f_c \leq 1 $，并且 $ \sum_{c=1}^C f_c = 1 $。为了避免这一限制，一种常见的做法是让模型返回未归一化的对数概率。然后，我们可以使用 softmax 函数将这些对数概率转换为概率，其定义如下：

$$  \mathrm{softmax}(\boldsymbol{a})\triangleq\left[\frac{e^{a_{1}}}{\sum_{c^{\prime}=1}^{C}e^{a_{c^{\prime}}}},\ldots,\frac{e^{a_{C}}}{\sum_{c^{\prime}=1}^{C}e^{a_{c^{\prime}}}}\right]   \tag*{(1.8)}$$

该函数将 $\mathbb{R}^C$ 映射到 $[0,1]^C$，并满足约束条件 $0 \leq \text{softmax}(\boldsymbol{a})_c \leq 1$ 和 $\sum_{c=1}^C \text{softmax}(\boldsymbol{a})_c = 1$。Softmax 的输入 $\boldsymbol{a} = f(\boldsymbol{x}; \boldsymbol{\theta})$ 被称为**logits**（对数几率）。详见第 2.5.2 节。因此，我们将整个模型定义如下：

$$  p(y=c|\boldsymbol{x};\boldsymbol{\theta})=\mathrm{softmax}_{c}(f(\boldsymbol{x};\boldsymbol{\theta}))   \tag*{(1.9)}$$

作者：Kevin P. Murphy。(C) MIT Press。CC-BY-NC-ND 许可证。

---

一个常见的特例是当 $f$ 为如下形式的仿射函数时：

$$  f(\boldsymbol{x};\boldsymbol{\theta})=b+\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}=b+w_{1}x_{1}+w_{2}x_{2}+\cdots+w_{D}x_{D}   \tag*{(1.10)}$$

其中 $\theta = (b, w)$ 是模型的参数。该模型称为**逻辑回归**，将在第10章中详细讨论。

在统计学中，参数 $w$ 通常称为**回归系数**（一般用 $\beta$ 表示），而 $b$ 称为**截距**。在机器学习中，参数 $w$ 称为**权重**，$b$ 称为**偏置**。这一术语源于电气工程，我们将函数 $f$ 视为一个电路，它接收输入 $x$ 并返回 $f(\mathbf{x})$。每个输入通过“导线”馈入电路，导线具有权重 $w$。电路计算输入的加权和，并加上一个恒定的偏置或偏移项 $b$。（此处“偏置”一词的使用不应与第4.7.6.1节讨论的统计概念混淆。）

为简化符号，通常将偏置项 $b$ 吸收到权重 $\boldsymbol{w}$ 中，定义 $\tilde{\boldsymbol{w}} = [b, w_1, \ldots, w_D]$ 和 $\tilde{\boldsymbol{x}} = [1, x_1, \ldots, x_D]$，从而得到：

$$  \tilde{w}^{\top}\tilde{x}=b+w^{\top}x   \tag*{(1.11)}$$

这样就将仿射函数转化为线性函数。我们通常假定已进行此处理，因此可以直接将预测函数写为：

$$  f(x;w)=w^{\top}x   \tag*{(1.12)}$$

##### 1.2.1.6 最大似然估计

在拟合概率模型时，通常使用负对数概率作为损失函数：

$$  \ell(y,f(\boldsymbol{x};\boldsymbol{\theta}))=-\log p(y|f(\boldsymbol{x};\boldsymbol{\theta}))   \tag*{(1.13)}$$

其原因将在第5.1.6.1节中说明，但直觉是：好的模型（损失低）会为每个输入 $x$ 对应的真实输出 $y$ 分配高概率。训练集的平均负对数概率为：

$$  \mathrm{N L L}(\boldsymbol{\theta})=-\frac{1}{N}\sum_{n=1}^{N}\log p(y_{n}|f(\boldsymbol{x}_{n};\boldsymbol{\theta}))   \tag*{(1.14)}$$

这称为**负对数似然**。若将其最小化，即可得到**最大似然估计**（MLE）：

$$  \hat{\theta}_{\mathrm{m l e}}=\underset{\theta}{\mathrm{a r g m i n}}\mathrm{N L L}(\boldsymbol{\theta})   \tag*{(1.15)}$$

正如我们将看到的，这是一种非常常见的模型拟合数据的方法。

#### 1.2.2 回归

现在假设我们希望预测一个实数值 $y \in \mathbb{R}$，而不是类别标签 $y \in \{1, \ldots, C\}$；这称为**回归**。例如，在鸢尾花案例中，$y$ 可能是食用花朵后的毒性程度，或植物的平均高度。

---

回归与分类非常相似。然而，由于输出是实数值，我们需要使用不同的损失函数。对于回归，最常用的选择是二次损失或$\ell_{2}$损失：

$$  \ell_{2}(y,\hat{y})=(y-\hat{y})^{2}   \tag*{(1.16)}$$

该损失对较大残差$y-\hat{y}$的惩罚比较小残差更大。$^{4}$使用二次损失时的经验风险等于均方误差（MSE）：

$$  \mathrm{MSE}(\boldsymbol{\theta})=\frac{1}{N}\sum_{n=1}^{N}(y_{n}-f(\boldsymbol{x}_{n};\boldsymbol{\theta}))^{2}   \tag*{(1.17)}$$

基于第1.2.1.5节的讨论，我们还应该对预测中的不确定性进行建模。在回归问题中，通常假设输出分布是高斯分布或正态分布。如第2.6节所述，该分布定义为

$$  \mathcal{N}(y|\mu,\sigma^{2})\triangleq\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{1}{2\sigma^{2}}(y-\mu)^{2}}   \tag*{(1.18)}$$

其中$\mu$是均值，$\sigma^2$是方差，$\sqrt{2\pi\sigma^2}$是归一化常数，用于确保密度函数积分为1。在回归的语境下，我们可以通过定义$\mu = f(\boldsymbol{x}_n; \boldsymbol{\theta})$使均值依赖于输入。因此得到如下条件概率分布：

$$  p(y_{n}|\boldsymbol{x}_{n};\boldsymbol{\theta})=\mathcal{N}(y_{n}|f(\boldsymbol{x}_{n};\boldsymbol{\theta}),\sigma^{2})   \tag*{(1.19)}$$

如果我们假设方差$\sigma^2$是固定的（为简单起见），相应的平均（每样本）负对数似然变为

$$  \begin{aligned}\mathrm{N L L}(\boldsymbol{\theta})&=-\frac{1}{N}\sum_{n=1}^{N}\log\left[\left(\frac{1}{2\pi\sigma^{2}}\right)^{\frac{1}{2}}\exp\left(-\frac{1}{2\sigma^{2}}(y_{n}-f(\boldsymbol{x}_{n};\boldsymbol{\theta}))^{2}\right)\right]\\&=\frac{1}{2\sigma^{2}}\mathrm{M S E}(\boldsymbol{\theta})+\mathrm{c o n s t}\end{aligned}   \tag*{(1.20)}$$

我们看到NLL与MSE成正比。因此，计算参数的最大似然估计将导致最小化平方误差，这似乎是一种合理的模型拟合方法。

##### 1.2.2.1 线性回归

作为回归模型的一个示例，考虑Figure 1.5a中的一维数据。我们可以使用如下形式的简单线性回归模型来拟合这些数据：

$$  f(x;\boldsymbol{\theta})=b+wx   \tag*{(1.22)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_205_149_579_396.jpg" alt="图像" width="32%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_613_150_988_395.jpg" alt="图像" width="32%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图1.5: (a) 对一维数据进行线性回归。(b) 竖线表示每个输入（蓝色圆点）的观测输出值与其预测值（红色叉号）之间的残差。最小二乘回归的目标是选择一条使残差平方和最小的直线。由 $ \text{linreg\_residuals\_plot.ipynb} $ 生成。</div>


其中 $w$ 是斜率，$b$ 是截距，$\boldsymbol{\theta} = (w, b)$ 是模型的所有参数。通过调整 $\boldsymbol{\theta}$，我们可以最小化平方误差的和，如图1.5b中的竖线所示，直到找到最小二乘解

$$  \hat{\boldsymbol{\theta}}=\underset{\boldsymbol{\theta}}{\operatorname{argmin}}MSE(\boldsymbol{\theta})   \tag*{(1.23)}$$

详见第11.2.2.1节。

如果有多个输入特征，我们可以写成

$$  f(\boldsymbol{x};\boldsymbol{\theta})=b+w_{1}x_{1}+\cdots+w_{D}x_{D}=b+\boldsymbol{w}^{\top}\boldsymbol{x}   \tag*{(1.24)}$$

其中 $ \theta = (w, b) $。这称为多元线性回归。

例如，考虑根据房间内二维位置预测温度的任务。图1.6(a)给出了以下形式的线性模型的结果：

$$  f(\boldsymbol{x};\boldsymbol{\theta})=b+w_{1}x_{1}+w_{2}x_{2}   \tag*{(1.25)}$$

我们可以将该模型扩展为使用 $D > 2$ 个输入特征（如一天中的时间），但此时可视化会变得更困难。

##### 1.2.2.2 多项式回归

图1.5a中的线性模型显然对数据的拟合效果不佳。我们可以通过使用 $D$ 次多项式回归模型来改善拟合效果。其形式为 $f(x; \boldsymbol{w}) = \boldsymbol{w}^{\mathrm{T}} \phi(x)$，其中 $\phi(x)$ 是根据输入导出的特征向量，具体形式如下：

$$  \phi(x)=[1,x,x^{2},\ldots,x^{D}]   \tag*{(1.26)}$$

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_229_151_579_406.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_636_154_990_406.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 1.6：对二维数据应用的线性回归和多项式回归。纵轴为温度，横轴为房间内的位置。数据由加州伯克利 Intel 实验室的一些遥感传感器节点采集（数据由 Romain Thibaux 提供）。(a) 拟合平面形式为 $ \hat{f}(\mathbf{x}) = w_0 + w_1 x_1 + w_2 x_2 $。(b) 温度数据由一个二次函数拟合，形式为 $ \hat{f}(\mathbf{x}) = w_0 + w_1 x_1 + w_2 x_2 + w_3 x_3^2 + w_4 x_4^2 $。由 $ \text{linreg}_2d\_surface\_demo.ipynb $ 生成。</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_190_613_575_856.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">20 次</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_598_616_984_856.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_188_869_577_1103.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;"><img src="imgs/img_in_chart_box_596_875_981_1093.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;"> $ (d) $</div>


<div style="text-align: center;">图 1.7：(a-c) 分别是 2 次、14 次和 20 次多项式对 21 个数据点（与图 1.5 相同数据）的拟合。(d) 均方误差 (MSE) 随次数的变化。由 linreg_poly_vs_degree.ipynb 生成。</div>

---

这是一个特征预处理的简单示例，也被称为特征工程。

在图 1.7a 中，我们看到使用 $D = 2$ 能够获得更好的拟合效果。我们可以不断增加 $D$，从而增加模型中的参数数量，直到 $D = N - 1$；在这种情况下，每个数据点对应一个参数，因此我们可以完美地对数据进行插值。所得模型的均方误差（MSE）将为 0，如图 1.7c 所示。然而，直觉上，所得函数将不是一个良好的未来输入预测器，因为它过于“波动”。我们将在第 1.2.3 节详细讨论这一点。

我们还可以将多项式回归应用于多维输入。例如，图 1.6(b) 绘制了在对输入进行二次展开后温度模型的预测结果：

$$  f(\boldsymbol{x};\boldsymbol{w})=w_{0}+w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{1}^{2}+w_{4}x_{2}^{2}   \tag*{(1.27)}$$

二次形状比图 1.6(a) 中的线性模型更符合数据，因为它捕捉到了房间中部温度更高这一事实。我们还可以添加交叉项，例如 $ x_1x_2 $，以捕捉交互效应。详情见第 1.5.3.2 节。

注意，上述模型仍然使用参数 $\boldsymbol{w}$ 的线性预测函数，尽管它是原始输入 $\boldsymbol{x}$ 的非线性函数。这一点之所以重要，是因为线性模型会导出一个具有唯一全局最优解的 MSE 损失函数 MSE($\theta$)，我们将在第 11.2.2.1 节中解释。

##### 1.2.2.3 深度神经网络

在第 1.2.2.2 节中，我们手动指定了输入特征的变换，即多项式展开：$ \phi(\boldsymbol{x}) = [1, x_1, x_2, x_1^2, x_2^2, \ldots] $。通过自动学习执行这样的非线性特征提取，我们可以创建更强大的模型。如果让 $ \phi(\boldsymbol{x}) $ 拥有自己的参数集，比如 $\mathbf{V}$，那么整体模型的形式为：

$$  f(\boldsymbol{x};\boldsymbol{w},\mathbf{V})=\boldsymbol{w}^{\top}\boldsymbol{\phi}(\boldsymbol{x};\mathbf{V})   \tag*{(1.28)}$$

我们可以递归地将特征提取器 $ \phi(\boldsymbol{x}; \mathbf{V}) $ 分解为更简单函数的组合。由此得到的模型成为 $ L $ 个嵌套函数的堆叠：

$$  f(x;\boldsymbol{\theta})=f_{L}(f_{L-1}(\cdots(f_{1}(x))\cdots))   \tag*{(1.29)}$$

其中 $ f_{\ell}(\boldsymbol{x}) = f(\boldsymbol{x}; \boldsymbol{\theta}_{\ell}) $ 是第 $\ell$ 层的函数。最后一层是线性的，形式为 $ f_{L}(\boldsymbol{x}) = \boldsymbol{w}_{L}^{\top} \boldsymbol{x} $，因此 $ f(\boldsymbol{x}; \boldsymbol{\theta}) = \boldsymbol{w}_{L}^{\top} f_{1:L-1}(\boldsymbol{x}) $，其中 $ f_{1:L-1}(\boldsymbol{x}) = f_{L-1}(\cdots(f_{1}(\boldsymbol{x}))\cdots) $ 是学习到的特征提取器。这是深度神经网络（DNN）的核心思想，其常见变体包括用于图像的卷积神经网络（CNN）和用于序列的循环神经网络（RNN）。详见第三部分。

#### 1.2.3 过拟合与泛化

我们可以将经验风险（式 (1.4)）重写为以下等价形式：

$$  \mathcal{L}(\boldsymbol{\theta};\mathcal{D}_{train})=\frac{1}{\left|\mathcal{D}_{train}\right|}\sum_{(\boldsymbol{x},\boldsymbol{y})\in\mathcal{D}_{train}}\ell(\boldsymbol{y},f(\boldsymbol{x};\boldsymbol{\theta}))   \tag*{(1.30)}$$

其中 $ |\mathcal{D}_{\text{train}}| $ 是训练集 $ \mathcal{D}_{\text{train}} $ 的大小。这种表述很有用，因为它明确指出了损失是在哪个数据集上评估的。

---

使用一个足够灵活的模型，我们可以通过简单地记住每个输入的正确输出，将训练损失降至零（假设没有标签噪声）。例如，Figure 1.7(c) 完美地插值了训练数据（除了最右边的那个点）。但我们关心的是新数据上的预测精度，这些新数据可能不属于训练集。一个完美拟合训练数据但过于复杂的模型，被称为**过拟合**。

为了检测模型是否过拟合，我们暂时假设可以访问用于生成训练集的真实（但未知）分布 $ p^{*}(\boldsymbol{x}, \boldsymbol{y}) $。然后，我们不再计算经验风险，而是计算理论期望损失或总体风险：

$$  \mathcal{L}(\boldsymbol{\theta};p^{*})\triangleq\mathbb{E}_{p^{*}(\boldsymbol{x},\boldsymbol{y})}\left[\ell(\boldsymbol{y},f(\boldsymbol{x};\boldsymbol{\theta}))\right]   \tag*{(1.31)}$$

差值 $ \mathcal{L}(\boldsymbol{\theta};p^{*}) - \mathcal{L}(\boldsymbol{\theta};\mathcal{D}_{\mathrm{train}}) $ 被称为**泛化差距**。如果模型具有较大的泛化差距（即经验风险低但总体风险高），则表明它过拟合了。

在实践中，我们不知道 $ p^{*} $。然而，我们可以将已有的数据划分为两个子集，称为训练集和测试集。然后，我们可以使用测试风险来近似总体风险：

$$  \mathcal{L}(\boldsymbol{\theta};\mathcal{D}_{\mathrm{t e s t}})\triangleq\frac{1}{|\mathcal{D}_{\mathrm{t e s t}}|}\sum_{(\boldsymbol{x},\boldsymbol{y})\in\mathcal{D}_{\mathrm{t e s t}}}\ell(y,f(\boldsymbol{x};\boldsymbol{\theta}))   \tag*{(1.32)}$$

例如，在 Figure 1.7d 中，我们绘制了多项式回归的训练误差和测试误差随阶数 $ D $ 的变化。我们看到，随着模型变得更加复杂，训练误差趋近于0。然而，测试误差呈现出一个典型的 $ \mathbf{U} $ 形曲线：在左侧，$ D = 1 $ 时，模型**欠拟合**；在右侧，$ D \gg 1 $ 时，模型过拟合；而当 $ D = 2 $ 时，模型复杂度“恰到好处”。

如何选择合适复杂度的模型？如果我们使用训练集来评估不同的模型，我们总是会选择最复杂的模型，因为它具有最多的自由度，从而具有最小的损失。因此，我们应当选择测试损失最小的模型。

在实践中，我们需要将数据划分为三个集合：训练集、测试集和验证集；验证集用于模型选择，而测试集仅用于估计未来性能（总体风险），即测试集不用于模型拟合或模型选择。更多细节请参见 Section 4.5.4。

#### 1.2.4 没有免费午餐定理

All models are wrong, but some models are useful. — George Box [BD87, p424]. $ ^{5} $

鉴于文献中模型种类繁多，自然会想知道哪个模型最好。不幸的是，并不存在对所有类型问题都最优的单一最佳模型——这有时被称为**没有免费午餐定理** [Wol96]。原因在于，一组假设（也称为归纳偏置）在一个领域效果良好，但在另一个领域可能效果很差。选择合适的模型的最佳方法是基于领域知识和/或反复试验（即使用模型选择技术，如交叉验证（Section 4.5.4）或贝叶斯方法（Section 5.2.2 和 Section 5.2.6））。因此，在自己的工具箱中拥有多种模型和算法技术以供选择非常重要。

5. George Box is a retired statistics professor at the University of Wisconsin.

---

### 1.3 无监督学习

在监督学习中，我们假设训练集中的每个输入样本 x 都有相应的输出目标 y，目标是学习输入-输出映射。尽管这很有用且可能具有挑战性，但监督学习本质上只是“美化的曲线拟合”[Pea18]。

一个更有趣的任务是尝试“理解”数据，而不仅仅是学习映射。也就是说，我们只得到观测到的“输入” $ \mathcal{D} = \{\pmb{x}_{n} : n = 1 : N\} $，而没有任何对应的“输出” $ \pmb{y}_{n} $。这被称为**无监督学习**。

从概率角度来看，无监督学习可以看作是对形如 $ p(\boldsymbol{x}) $ 的无条件模型进行拟合，该模型能够生成新数据 $ \boldsymbol{x} $；而监督学习则是对条件模型 $ p(\boldsymbol{y}|\boldsymbol{x}) $ 进行拟合，该模型指定了给定输入时输出（的分布）。$ ^{6} $

无监督学习避免了对大量带标签数据集的收集需求——这种收集通常费时且昂贵（想象一下让医生为医学图像标注）。

无监督学习还避免了学习如何将世界划分成往往任意的类别。例如，考虑为视频中的动作（如“喝”或“啜饮”）加标签的任务。动作发生在何时？是当人拿起杯子时，还是杯子第一次接触嘴唇时，或是液体倒出时？如果倒出一些液体，停顿，再倒出——这是两个动作还是一个？人类往往会在这些问题上产生分歧[Idr+17]，这意味着任务定义并不明确。因此，期望机器学习这类映射是不合理的。$ ^{7} $

最后，无监督学习迫使模型“解释”高维输入，而不仅仅是低维输出。这使我们能够学习更丰富的“世界如何运作”的模型。正如多伦多大学著名的机器学习教授Geoff Hinton所说：

> 当我们学习看东西时，没有人告诉我们正确答案是什么——我们只是看。偶尔，你的母亲会说“那是条狗”，但信息量非常少。你如果能在成长过程中以这种方式获得几个比特的信息——甚至每秒一比特——就算幸运了。人脑的视觉系统有 $ O(10^{14}) $ 个神经连接，而你的生命只有 $ O(10^{9}) $ 秒。因此每秒学习一比特毫无用处。你需要大约 $ O(10^{5}) $ 比特每秒。而只有一个地方能获得那么多信息：来自输入本身。——Geoffrey Hinton, 1996（引自[Gor06]）

#### 1.3.1 聚类

无监督学习的一个简单例子是发现数据中的聚类问题。目标是将输入划分为包含“相似”点的区域。以Iris数据集的二维版本为例。在图1.8a中，我们显示了没有类别标签的点。直观上，数据中至少存在两个聚类，一个在左下角，一个在右上角。此外，如果我们认为一组“好的”聚类应该相当紧凑，那么可能需要将右上角分成（至少）两个子聚类。最终划分成三个聚类的结果如图1.8b所示。（注意，聚类的正确数量并不存在；相反，我们需要考虑

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_227_130_533_329.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_634_130_940_329.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图1.8: (a) 鸢尾花数据集中花瓣特征散点图。 (b) 使用 K=3 进行无监督聚类的结果。由 iris_kmeans.ipynb 生成。</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_241_479_569_702.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;"> $ (a) $</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_649_479_978_703.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">图1.9: (a) 鸢尾花数据散点图（前3个特征）。点按类别颜色编码。 (b) 我们使用 PCA 对三维数据拟合了一个二维线性子空间。类别标签被忽略。红点是原始数据，黑点是根据模型  $ \hat{x} = Wz + \mu $ 生成的点，其中 z 是底层推断出的二维线性流形上的潜在点。由 iris_pca.ipynb 生成。</div>

模型复杂度与数据拟合之间的权衡。我们将在第21.3.7节讨论如何做出这种权衡。）

#### 1.3.2 发现潜在的“变化因子”

处理高维数据时，通过将其投影到能够捕捉数据“本质”的低维子空间来降维通常是有用的。解决该问题的一种方法是假设每个观测到的高维输出 $ \boldsymbol{x}_n \in \mathbb{R}^D $ 都是由一组隐藏或未观测到的低维潜在因子 $ \boldsymbol{z}_n \in \mathbb{R}^K $ 生成的。我们可以用如下图形方式表示该模型： $ \boldsymbol{z}_n \to \boldsymbol{x}_n $，其中箭头表示因果关系。由于我们不知道潜在因子 $ \boldsymbol{z}_n $，我们通常为 $ p(\boldsymbol{z}_n) $ 假设一个简单的先验概率模型（如高斯分布），该模型表示每个因子是一个随机的 $ K $ 维向量。如果数据是实值的，我们也可以使用高斯似然。

作者：Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND 许可证.

---

最简单的例子是当我们使用线性模型时，$ p(x_n | z_n; \theta) = \mathcal{N}(x_n | \mathbf{W}z_n + \mu, \Sigma) $。由此产生的模型称为**因子分析**（factor analysis, FA）。它类似于线性回归，只是我们只能观测到输出 $ x_n $，而无法观测到输入 $ z_n $。在特殊情况 $ \Sigma = \sigma^2 \mathbf{I} $ 下，该模型简化为**概率主成分分析**（probabilistic principal components analysis, PCA），我们将在第20.1节中解释。在图1.9中，我们展示了该方法如何应用于一些简单的三维数据，从而找到一个二维线性子空间。

当然，假设从 $ z_n $ 到 $ \mathbf{x}_n $ 是线性映射是高度限制性的。然而，我们可以通过定义 $ p(\mathbf{x}_n | \mathbf{z}_n; \boldsymbol{\theta}) = \mathcal{N}(\mathbf{x}_n | f(\mathbf{z}_n; \boldsymbol{\theta}), \sigma^2 \mathbf{I}) $ 来创建非线性扩展，其中 $ f(\mathbf{z}; \boldsymbol{\theta}) $ 是一个非线性模型，例如深度神经网络。拟合这样的模型（即估计参数 $ \boldsymbol{\theta} $）变得困难得多，因为神经网络的输入以及模型的参数都需要被推断。然而，存在多种近似方法，例如可以应用的**变分自编码器**（见第20.3.5节）。

#### 1.3.3 自监督学习

最近一种流行的无监督学习方法称为**自监督学习**。在这种方法中，我们从无标签数据中创建代理监督任务。例如，我们可能尝试学习从灰度图像预测彩色图像，或者遮盖句子中的单词，然后根据周围的上下文预测它们。我们希望得到的预测器 $ \hat{x}_1 = f(x_2; \theta) $（其中 $ x_2 $ 是观测输入，$ \hat{x}_1 $ 是预测输出）能从数据中学习到有用的特征，进而用于标准的、下游监督任务。这避免了试图推断观测数据背后的“真实潜在因子” $ z $ 这一难题，而是依赖于标准的监督学习方法。我们在第19.2节中更详细地讨论这种方法。

#### 1.3.4 无监督学习的评估

尽管无监督学习很有吸引力，但评估无监督学习方法输出的质量非常困难，因为没有真值可供比较[TOB16]。

评估无监督模型的一种常用方法是测量模型对未见过的测试样本所赋予的概率。我们可以通过计算数据的（无条件）负对数似然来实现：

$$  \mathcal{L}(\boldsymbol{\theta};\mathcal{D})=-\frac{1}{|\mathcal{D}|}\sum_{\boldsymbol{x}\in\mathcal{D}}\log p(\boldsymbol{x}|\boldsymbol{\theta})   \tag*{(1.33)}$$

这实际上将无监督学习问题视为**密度估计**问题。其思想是，一个好的模型不会对实际数据样本感到“惊讶”（即会赋予它们高概率）。此外，由于概率总和必须为1.0，如果模型对数据样本所在的数据空间区域赋予高概率，那么它会隐式地对数据不存在的区域赋予低概率。因此，模型学会了捕捉数据中的典型模式。这可以用于数据压缩算法。

不幸的是，密度估计是困难的，尤其是在高维空间中。此外，一个对数据赋予高概率的模型可能没有学到有用的高层模式（毕竟，模型可能只是记住了所有训练样本）。

另一种评估指标是将学到的无监督表示作为特征或输入，用于下游监督学习方法。如果无监督方法发现了有用的

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_302_118_461_336.jpg" alt="图像" width="13%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_693_119_887_339.jpg" alt="图像" width="16%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 1.10：一些控制问题的示例。(a) 太空侵略者 Atari 游戏。来自 https://gymnasium.farama.org/environments/atari/space_invaders/。(b) 在 MuJuCo 模拟器中控制一个人形机器人，使其尽可能快地行走而不摔倒。来自 https://gymnasium.farama.org/environments/mujoco/humanoid/。</div>


如果存在这些模式，那么就有可能利用这些模式进行监督学习，所需标注数据远少于使用原始特征。例如，在第 1.2.1.1 节中，我们看到了鸢尾花的 4 个人工定义特征如何包含了分类所需的大部分信息。因此，我们仅用 150 个样本就能训练出一个性能近乎完美的分类器。如果输入是原始像素，要达到同样性能，我们需要多得多的样本（见第 14.1 节）。也就是说，通过先学习一个**好的表示**，我们可以提高学习的样本效率（即减少获得良好性能所需的标注样本数量）。

提高样本效率是一个有用的评估指标，但在许多应用中，尤其是在科学领域，无监督学习的目标是获得理解，而不是提升某个预测任务的性能。这需要使用可解释的模型，这些模型同时能够生成或“解释”数据中观察到的大部分模式。套用柏拉图的话来说，目标是发现如何“在自然的关节处切割”。当然，评估我们是否成功发现了某个数据集背后的真正潜在结构，通常需要执行实验并与世界交互。我们将在第 1.4 节进一步讨论这一主题。

### 1.4 强化学习

除了监督学习和无监督学习，还有第三种机器学习——强化学习 (RL)。在这类问题中，系统或代理必须学习如何与其环境交互。这可以通过策略  $ \boldsymbol{a} = \pi(\boldsymbol{x}) $ 来编码，该策略指定了对每个可能的输入  $ \boldsymbol{x} $（从环境状态导出）应采取何种行动。

例如，考虑一个学习玩视频游戏（如 Atari 太空侵略者，见图 1.10a）的代理。在这种情况下，输入 x 是图像（或过去图像的序列），输出 a 是移动方向（左或右）以及是否发射导弹。再举一个更复杂的例子，机器人学习行走的问题（见图 1.10b）。在这种情况下，输入 x 是所有肢体的关节位置和角度集合，输出 a 是一组驱动或电机控制信号。

作者：Kevin P. Murphy。 (C) MIT 出版社。CC-BY-NC-ND 许可证

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_147_104_824_398.jpg" alt="图片" width="58%" /></div>


<div style="text-align: center;">图 1.11：三种机器学习类型可视化为巧克力蛋糕的层次。此图（原始出处：https://bit.ly/2m65Vs1）来自 Yann LeCun 在 NIPS'16 的演讲，经其许可使用。</div>


与监督学习不同的是，系统不会被告知哪个动作是最优的（即对于给定输入应产生哪个输出）。相反，系统仅在执行动作后偶尔收到奖励（或惩罚）信号。这就像向一位批评家学习，他偶尔给出正面或负面的反馈，而非向一位老师学习，后者会在每一步告诉你怎么做。

近年来，强化学习因其广泛的适用性（因为智能体试图优化的奖励信号可以是任意感兴趣的指标）而日益流行。然而，由于多种原因，使强化学习有效工作往往比监督学习或无监督学习更困难。一个关键难点在于，奖励信号可能只是偶尔给出（例如，当智能体最终达到期望状态时），即便如此，智能体也可能不清楚其众多动作中哪些是获得奖励的原因。（想想下棋这类游戏，棋局结束时只有一个输或赢的信号。）

为了弥补奖励信号信息量不足的问题，通常借助其他信息源，例如专家示范（可以以监督方式使用）或无标签数据（可由无监督学习系统用于发现环境的底层结构）。这使得从有限次数的试验（与环境交互）中学习成为可能。正如 Yann LeCun 在 2016 年 NIPS$^{8}$ 会议的特邀演讲中所说：“如果智能是一块蛋糕，那么无监督学习是巧克力海绵蛋糕，监督学习是糖霜，而强化学习则是樱桃。”如图 1.11 所示。

关于强化学习的更多信息可参见本书续篇 [Mur23]。

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_238_119_930_406.jpg" alt="图像" width="60%" /></div>


<div style="text-align: center;"> $ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 1.12: (a) MNIST 数据集的可视化。每张图像大小为 $ 28 \times 28 $。训练集包含 60k 个样本，测试集包含 10k 个样本。我们展示了训练集中的前 25 张图像。由 mnist_viz_tf.ipynb 生成。(b) EMNIST 数据集的可视化。训练集包含 697,932 个样本，测试集包含 116,323 个样本，每张图像大小为 $ 28 \times 28 $。共有 62 个类别（a-z、A-Z、0-9）。我们展示了训练集中的前 25 张图像。由 emnist_viz_jax.ipynb 生成。</div>


### 1.5 数据

机器学习关注的是使用各种算法将模型拟合到数据上。尽管我们主要关注建模和算法方面，但有必要指出，训练数据的性质和质量对于任何学习模型的成功也起着至关重要的作用。

在本节中，我们简要介绍本书将使用的一些常见图像和文本数据集。我们还将简要讨论数据预处理这一主题。

#### 1.5.1 一些常见的图像数据集

在本节中，我们简要讨论本书将使用的一些图像数据集。

##### 1.5.1.1 小型图像数据集

最简单且最广泛使用的数据集之一是 MNIST [LeC+98; YB19]。$ ^{9} $ 该数据集包含 60k 个训练图像和 10k 个测试图像，每张图像大小为 $ 28 \times 28 $（灰度），描绘了来自 10 个类别的手写数字。每个像素是范围 $ \{0,1,\ldots,255\} $ 内的整数；通常将其缩放到 $ [0,1] $ 以表示像素强度。我们也可以选择通过阈值化将其转换为二值图像。如图 1.12a 所示。

MNIST 在机器学习社区中使用非常广泛，著名机器学习研究员 Geoff Hinton 将其称为“机器学习的果蝇”，因为如果我们无法在 MNIST 上使某个方法表现良好，那么它在更困难的数据集上很可能也不会奏效。然而，如今 MNIST 分类被认为

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_241_120_930_411.jpg" alt="图片" width="59%" /></div>


<div style="text-align: center;">$ (a) $</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 1.13: (a) Fashion-MNIST 数据集的可视化 [XRV17]。该数据集与 MNIST 具有相同的大小，但分类难度更高。共包含 10 个类别：T恤/上衣、裤子、套头衫、连衣裙、外套、凉鞋、衬衫、运动鞋、包、踝靴。图中展示了训练集中的前 25 张图像。由 fashion_viz_tf.ipynb 生成。(b) CIFAR-10 数据集中的部分图像 [KH09]。每张图像尺寸为 $ 32 \times 32 \times 3 $，其中最后一个维度 3 表示 RGB 三通道。训练样本 5 万张，测试样本 1 万张。共包含 10 个类别：飞机、汽车、鸟、猫、鹿、狗、青蛙、马、船、卡车。图中展示了训练集中的前 25 张图像。由 cifar_viz_tf.ipynb 生成。</div>


“过于简单”，因为仅通过查看单个像素就能区分大多数数字对。目前已有多种扩展方案被提出。

在文献 [Coh+17] 中，他们提出了 **EMNIST**（扩展 **MNIST**），其中还包含大小写字母。可视化结果见图 1.12b。该数据集比 **MNIST** 难得多，共有 62 个类别，其中一些类别的区分度较低（例如数字 1 与小写字母 l）。

在 [XRV17] 中，他们提出了 Fashion-MNIST，其大小和形状与 MNIST 完全相同，但每张图像是服装图片而非手写数字。可视化结果见图 1.13a。

对于小型彩色图像，最常用的数据集是 CIFAR [KH09]。$ ^{10} $ 该数据集包含 6 万张图像，每张尺寸为 $ 32 \times 32 \times 3 $，代表来自 10 个或 100 个类别的日常物体；图 1.13b 给出了示例。$ ^{11} $

##### 1.5.1.2 ImageNet

小型数据集有助于原型设计，但同样重要的是在更大规模的数据集上测试方法，包括图像尺寸和标记样本数量两方面。最广泛使用的数据集