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

by applying the clustering algorithm (e.g. k-means) to embeddings that are output by an encoder. Further, clustering can be joined with the learning algorithm while learning a shallow [Roz+19] or Graph Convolution [Chi+19a; CEL19] embedding model.

##### 23.6.1.4 Visualization

There are many off-the-shelf tools for mapping graph nodes onto two-dimensional manifolds for the purpose of visualization. Visualizations allow network scientists to qualitatively understand graph properties, understand relationships between nodes or visualize node clusters. Among the popular tools are methods based on Force-Directed Layouts, with various web-app Javascript implementations.

Unsupervised graph embedding methods are also used for visualization purposes: by first training an encoder-decoder model (corresponding to a shallow embedding or graph convolution network), and then mapping every node representation onto a two-dimensional space using t-SNE (Section 20.4.10) or PCA (Section 20.1). Such a process (embedding → dimensionality reduction) is commonly used to qualitatively evaluate the performance of graph learning algorithms. If nodes have attributes, one can use these attributes to color the nodes on 2D visualization plots. Good embedding algorithms embed nodes that have similar attributes nearby in the embedding space, as demonstrated in visualizations of various methods [PARS14; KW16a; AEH+18]. Finally, beyond mapping every node to a 2D coordinate, methods which map every graph to a representation [ARZP19] can similarly be projected into two dimensions to visualize and qualitatively analyze graph-level properties.

#### 23.6.2 Supervised applications

In this section, we discuss common supervised applications.

##### 23.6.2.1 Node classification

Node classification is an important supervised graph application, where the goal is to learn node representations that can accurately predict node labels. (This is sometimes called \textbf{statistical} relational learning [GT07].) For instance, node labels could be scientific topics in citation networks, or gender and other attributes in social networks.

Since labeling large graphs can be time-consuming and expensive, semi-supervised node classification is a particularly common application. In semi-supervised settings, only a fraction of nodes are labeled and the goal is to leverage links between nodes to predict attributes of unlabeled nodes. This setting is transductive since there is only one partially labeled fixed graph. It is also possible to do inductive node classification, which corresponds to the task of classifying nodes in multiple graphs.

Note that node features can significantly boost the performance on node classification tasks if these are descriptive for the target label. Indeed, recent methods such as GCN (Section 23.4.2) GraphSAGE (Section 23.4.3.1) have achieved state-of-the-art performance on multiple node classification benchmarks due to their ability to combine structural information and semantics coming from features. On the other hand, other methods such as random walks on graphs fail to leverage feature information and therefore achieve lower performance on these tasks.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_223_114_948_266.jpg" alt="Image" width="62%" /></div>

<div style="text-align: center;">Figure 23.9: Structurally similar molecules do not necessarily have similar odor descriptors. (A) Lyral, the reference molecule. (B) Molecules with similar structure can share similar odor descriptors. (C) However, a small structural change can render the molecule odorless. (D) Further, large structural changes can leave the odor of the molecule largely unchanged. From Figure 1 of [SL+19], originally from [OPK12]. Used with kind permission of Benjamin Sanchez-Lengeling.</div>

##### 23.6.2.2 Graph classification

Graph classification is a supervised application where the goal is to predict graph labels. Graph classification problems are inductive and a common example is classifying chemical compounds (e.g. predicting toxicity or odor from a molecule, as shown in Figure 23.9).

Graph classification requires some notion of pooling, in order to aggregate node-level information into graph-level information. As discussed earlier, generalizing this notion of pooling to arbitrary graphs is non-trivial because of the lack of regularity in the graph structure making graph pooling an active research area. In addition to the supervised methods discussed above, a number of unsupervised methods for learning graph-level representations have been proposed [Tsi+18; ARZP19; TMP20].

---

# A Notation

### A.1 Introduction

It is very difficult to come up with a single, consistent notation to cover the wide variety of data, models and algorithms that we discuss in this book. Furthermore, conventions differ between different fields (such as machine learning, statistics and optimization), and between different books and papers within the same field. Nevertheless, we have tried to be as consistent as possible. Below we summarize most of the notation used in this book, although individual sections may introduce new notation. Note also that the same symbol may have different meanings depending on the context, although we try to avoid this where possible.

### A.2 Common mathematical symbols

We list some common symbols below.

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\infty$</td><td style='text-align: center; word-wrap: break-word;'>Infinity</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\rightarrow$</td><td style='text-align: center; word-wrap: break-word;'>Tends towards, e.g.,  $n \rightarrow \infty$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\propto$</td><td style='text-align: center; word-wrap: break-word;'>Proportional to, so  $y = ax$ can be written as  $y \propto x$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\triangleq$</td><td style='text-align: center; word-wrap: break-word;'>Defined as</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$O(\cdot)$</td><td style='text-align: center; word-wrap: break-word;'>Big-O: roughly means order of magnitude</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbb{Z}_{+}$</td><td style='text-align: center; word-wrap: break-word;'>The positive integers</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbb{R}$</td><td style='text-align: center; word-wrap: break-word;'>The real numbers</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbb{R}_{+}$</td><td style='text-align: center; word-wrap: break-word;'>The positive reals</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathcal{S}_{K}$</td><td style='text-align: center; word-wrap: break-word;'>The  $K$-dimensional probability simplex</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathcal{S}_{++}^{D}$</td><td style='text-align: center; word-wrap: break-word;'>Cone of positive definite  $D \times D$ matrices</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\approx$</td><td style='text-align: center; word-wrap: break-word;'>Approximately equal to</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\{1,\ldots,N\}$</td><td style='text-align: center; word-wrap: break-word;'>The finite set  $\{1,2,\ldots,N\}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1 :  $N$</td><td style='text-align: center; word-wrap: break-word;'>The finite set  $\{1,2,\ldots,N\}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$[\ell,u]$</td><td style='text-align: center; word-wrap: break-word;'>The continuous interval  $\{\ell \leq x \leq u\}$.</td></tr></table>

---

### A.3 Functions

Generic functions will be denoted by $f$(and sometimes$g$or$h$). We will encounter many named functions, such as $\tanh(x)$or$\sigma(x)$. A scalar function applied to a vector is assumed to be applied elementwise, e.g., $\mathbf{x}^2 = [x_1^2, \ldots, x_D^2]$. Functionals (functions of a function) are written using “blackboard” font, e.g., $\mathbb{H}(p)$for the entropy of a distribution$p$. A function parameterized by fixed parameters $\boldsymbol{\theta}$will be denoted by$f(\mathbf{x};\boldsymbol{\theta})$or sometimes$f_{\boldsymbol{\theta}}(\mathbf{x})$. We list some common functions (with no free parameters) below.

### A.3.1 Common functions of one argument

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$[x]$</td><td style='text-align: center; word-wrap: break-word;'>Floor of  $x$, i.e., round down to nearest integer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$[x]$</td><td style='text-align: center; word-wrap: break-word;'>Ceiling of  $x$, i.e., round up to nearest integer</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\neg a$</td><td style='text-align: center; word-wrap: break-word;'>logical NOT</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbb{I}(x)$</td><td style='text-align: center; word-wrap: break-word;'>Indicator function,  $\mathbb{I}(x) = 1$ if  $x$ is true, else  $\mathbb{I}(x) = 0$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\delta(x)$</td><td style='text-align: center; word-wrap: break-word;'>Dirac delta function,  $\delta(x) = \infty$ if  $x = 0$, else  $\delta(x) = 0$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$|x|$</td><td style='text-align: center; word-wrap: break-word;'>Absolute value</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$|\mathcal{S}|$</td><td style='text-align: center; word-wrap: break-word;'>Size (cardinality) of a set</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$n!$</td><td style='text-align: center; word-wrap: break-word;'>Factorial function</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\log(x)$</td><td style='text-align: center; word-wrap: break-word;'>Natural logarithm of  $x$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\exp(x)$</td><td style='text-align: center; word-wrap: break-word;'>Exponential function  $e^{x}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\Gamma(x)$</td><td style='text-align: center; word-wrap: break-word;'>Gamma function,  $\Gamma(x) = \int_{0}^{\infty} u^{x-1} e^{-u} du$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\Psi(x)$</td><td style='text-align: center; word-wrap: break-word;'>Digamma function,  $\Psi(x) = \frac{d}{dx} \log \Gamma(x)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\sigma(x)$</td><td style='text-align: center; word-wrap: break-word;'>Sigmoid (logistic) function,  $\frac{1}{1 + e^{-x}}$</td></tr></table>

### A.3.2 Common functions of two arguments

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a \wedge b</td><td style='text-align: center; word-wrap: break-word;'>logical AND</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>a \vee b</td><td style='text-align: center; word-wrap: break-word;'>logical OR</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B(a,b)</td><td style='text-align: center; word-wrap: break-word;'>Beta function,  $B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\binom{n}{k}$</td><td style='text-align: center; word-wrap: break-word;'>n choose k, equal to  $n!/(k!(n-k)!)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\delta_{ij}$</td><td style='text-align: center; word-wrap: break-word;'>Kronecker delta, equals  $\mathbb{I}(i=j)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\boldsymbol{u} \odot \boldsymbol{v}$</td><td style='text-align: center; word-wrap: break-word;'>Elementwise product of two vectors</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\boldsymbol{u} \circledast \boldsymbol{v}$</td><td style='text-align: center; word-wrap: break-word;'>Convolution of two vectors</td></tr></table>

### A.3.3 Common functions of > 2 arguments

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>B( $\mathbf{x}$)</td><td style='text-align: center; word-wrap: break-word;'>Multivariate beta function,  $\frac{\prod_{k}\Gamma(x_{k})}{\Gamma(\sum_{k}x_{k})}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\Gamma(\mathbf{x})$</td><td style='text-align: center; word-wrap: break-word;'>Multi. gamma function,  $\pi^{D(D-1)/4}\prod_{d=1}^{D}\Gamma(x+(1-d)/2)$</td></tr></table>

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

 
$$
\begin{array}{r l}{\operatorname{s o f t m a x}(\pmb{x})}&{{}\operatorname{S o f t m a x~f u n c t i o n},[\frac{e^{x_{c}}}{\sum_{c^{\prime}=1}^{C}e^{x_{c^{\prime}}}}]_{c=1}^{C}}\end{array}
$$
 

### A.4 Linear algebra

In this section, we summarize the notation we use for linear algebra (see Chapter 7 for details).

### A.4.1 General notation

Vectors are bold lower case letters such as x, w. Matrices are bold upper case letters, such as X, W. Scalars are non-bold lower case. When creating a vector from a list of N scalars, we write  $\boldsymbol{x} = [x_1, \ldots, x_N]$; this may be a column vector or a row vector, depending on the context. (Vectors are assumed to be column vectors, unless noted otherwise.) When creating an  $M \times N$ matrix from a list of vectors, we write  $\boldsymbol{X} = [x_1, \ldots, x_N]$ if we stack along the columns, or  $\boldsymbol{X} = [x_1; \ldots; x_M]$ if we stack along the rows.

### A.4.2 Vectors

Here is some standard notation for vectors. (We assume u and v are both N-dimensional vectors.)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{u}^{\top}\mathbf{v}$</td><td style='text-align: center; word-wrap: break-word;'>Inner (scalar) product,  $\sum_{i=1}^{N} u_{i} v_{i}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{u}\mathbf{v}^{\top}$</td><td style='text-align: center; word-wrap: break-word;'>Outer product ( $N \times N$ matrix)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{u} \odot \mathbf{v}$</td><td style='text-align: center; word-wrap: break-word;'>Elementwise product,  $[u_{1}v_{1}, \ldots, u_{N}v_{N}]$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{v}^{\top}$</td><td style='text-align: center; word-wrap: break-word;'>Transpose of  $\mathbf{v}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\text{dim}(\mathbf{v})$</td><td style='text-align: center; word-wrap: break-word;'>Dimensionality of  $\mathbf{v}$ (namely  $N$)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\text{diag}(\mathbf{v})$</td><td style='text-align: center; word-wrap: break-word;'>Diagonal  $N \times N$ matrix made from vector  $\mathbf{v}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{1}$ or  $\mathbf{1}_{N}$</td><td style='text-align: center; word-wrap: break-word;'>Vector of ones (of length  $N$)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{0}$ or  $\mathbf{0}_{N}$</td><td style='text-align: center; word-wrap: break-word;'>Vector of zeros (of length  $N$)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$||\mathbf{v}|| = ||\mathbf{v}||_{2}$</td><td style='text-align: center; word-wrap: break-word;'>Euclidean or  $\ell_{2}$ norm  $\sqrt{\sum_{i=1}^{N} v_{i}^{2}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$||\mathbf{v}||_{1}$</td><td style='text-align: center; word-wrap: break-word;'>$\ell_{1}$ norm  $\sum_{i=1}^{N} |v_{i}|$</td></tr></table>

### A.4.3 Matrices

Here is some standard notation for matrices. (We assume  $\mathbf{S}$ is a square  $N \times N$ matrix,  $\mathbf{X}$ and  $\mathbf{Y}$ are of size  $M \times N$, and  $\mathbf{Z}$ is of size  $M' \times N'$.)

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Symbol</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{X}_{:,j}$</td><td style='text-align: center; word-wrap: break-word;'>$j$&#x27;th column of matrix</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{X}_{i,:,}$</td><td style='text-align: center; word-wrap: break-word;'>$i$&#x27;th row of matrix (treated as a column vector)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$X_{ij}$</td><td style='text-align: center; word-wrap: break-word;'>Element  $(i,j)$ of matrix</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\mathbf{S} \succ 0$</td><td style='text-align: center; word-wrap: break-word;'>True iff  $\mathbf{S}$ is a positive definite matrix</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\operatorname{tr}(\mathbf{S})$</td><td style='text-align: center; word-wrap: break-word;'>Trace of a square matrix</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$\det(\mathbf{S})$</td><td style='text-align: center; word-wrap: break-word;'>Determinant of a square matrix</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$|\mathbf{S}|$</td><td style='text-align: center; word-wrap: break-word;'>Determinant of a square matrix</td></tr></table>

---

 $S^{-1}$ Inverse of a square matrix
 $X^{\dagger}$ Pseudo-inverse of a matrix
 $X^{T}$ Transpose of a matrix
diag(S) Diagonal vector extracted from square matrix
I or  $I_{N}$ Identity matrix of size  $N \times N$
 $X \odot Y$ Elementwise product
 $X \otimes Z$ Kronecker product (see Section 7.2.5)

### A.4.4 Matrix calculus

In this section, we summarize the notation we use for matrix calculus (see Section 7.8 for details). Let  $\boldsymbol{\theta} \in \mathbb{R}^N$ be a vector and  $f : \mathbb{R}^N \to \mathbb{R}$ be a scalar valued function. The derivative of  $f$ wrt its argument is denoted by the following:

$$
\nabla_{\boldsymbol{\theta}}f(\boldsymbol{\theta})\triangleq\nabla f(\boldsymbol{\theta})\triangleq\nabla f\triangleq\left(\begin{array}{l l l l}{\frac{\partial f}{\partial\theta_{1}}}&{\cdots}&{\frac{\partial f}{\partial\theta_{N}}}\end{array}\right)   \tag*{(A.1)}
$$

The gradient is a vector that must be evaluated at a point in space. To emphasize this, we will sometimes write

$$
g_{t}\triangleq g(\boldsymbol{\theta}_{t})\triangleq\nabla f(\boldsymbol{\theta})\bigg|_{\boldsymbol{\theta}_{t}}   \tag*{(A.2)}
$$

We can also compute the (symmetric)  $N \times N$ matrix of second partial derivatives, known as the Hessian:

$$
\nabla^{2}f\triangleq\begin{pmatrix}\frac{\partial^{2}f}{\partial\theta_{1}^{2}}&\cdots&\frac{\partial^{2}f}{\partial\theta_{1}\partial\theta_{N}}\\&\vdots&\\ \frac{\partial^{2}f}{\partial\theta_{N}\theta_{1}}&\cdots&\frac{\partial^{2}f}{\partial\theta_{N}^{2}}\end{pmatrix}   \tag*{(A.3)}
$$

The Hessian is a matrix that must be evaluated at a point in space. To emphasize this, we will sometimes write

$$
\mathbf{H}_{t}\triangleq\mathbf{H}(\boldsymbol{\theta}_{t})\triangleq\nabla^{2}f(\boldsymbol{\theta})\bigg|_{\boldsymbol{\theta}_{t}}   \tag*{(A.4)}
$$

### A.5 Optimization

In this section, we summarize the notation we use for optimization (see Chapter 8 for details).

We will often write an objective or cost function that we wish to minimize as  $\mathcal{L}(\boldsymbol{\theta})$, where  $\boldsymbol{\theta}$ are the variables to be optimized (often thought of as parameters of a statistical model). We denote the parameter value that achieves the minimum as  $\boldsymbol{\theta}_* = \arg\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \mathcal{L}(\boldsymbol{\theta})$, where  $\boldsymbol{\Theta}$ is the set we are optimizing over. (Note that there may be more than one such optimal value, so we should really write  $\boldsymbol{\theta}_* \in \arg\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \mathcal{L}(\boldsymbol{\theta})$.)

When performing iterative optimization, we use $t$to index the iteration number. We use$\eta$as a step size (learning rate) parameter. Thus we can write the gradient descent algorithm (explained in Section 8.4) as follows:$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta_t \boldsymbol{g}_t$.

---

We often use a hat symbol to denote an estimate or prediction (e.g.,  $\hat{\theta}$,  $\hat{y}$), a star subscript or superscript to denote a true (but usually unknown) value (e.g.,  $\theta_*$ or  $\theta^*$), an overline to denote a mean value (e.g.,  $\overline{\theta}$).

### A.6 Probability

In this section, we summarize the notation we use for probability theory (see Chapter 2 for details).

We denote a probability density function (pdf) or probability mass function (pmf) by p, a cumulative distribution function (cdf) by P, and the probability of a binary event by Pr. We write  $p(X)$ for the distribution for random variable X, and  $p(Y)$ for the distribution for random variable Y — these refer to different distributions, even though we use the same p symbol in both cases. (In cases where confusion may arise, we write  $p_X(\cdot)$ and  $p_Y(\cdot)$.) Approximations to a distribution p will often be represented by q, or sometimes  $\hat{p}$.

In some cases, we distinguish between a random variable (rv) and the values it can take on. In this case, we denote the variable in upper case (e.g., X), and its value in lower case (e.g., x). However, we often ignore this distinction between variables and values. For example, we sometimes write  $p(x)$ to denote either the scalar value (the distribution evaluated at a point) or the distribution itself, depending on whether X is observed or not.

We write  $X \sim p$ to denote that  $X$ is distributed according to distribution  $p$. We write  $X \perp Y$ |  $Z$ to denote that  $X$ is conditionally independent of  $Y$ given  $Z$. If  $X \sim p$, we denote the expected value of  $f(X)$ using

$$
\mathbb{E}\left[f(X)\right]=\mathbb{E}_{p(X)}\left[f(X)\right]=\mathbb{E}_{X}\left[f(X)\right]=\int_{x}f(x)p(x)d x   \tag*{(A.5)}
$$

If f is the identity function, we write  $\overline{X} \triangleq \mathbb{E}[X]$. Similarly, the variance is denoted by

$$
\mathbb{V}\left[f(X)\right]=\mathbb{V}_{p(X)}\left[f(X)\right]=\mathbb{V}_{X}\left[f(X)\right]=\int_{x}(f(x)-\mathbb{E}\left[f(X)\right])^{2}p(x)d x   \tag*{(A.6)}
$$

If x is a random vector, the covariance matrix is denoted

$$
\mathrm{Cov}\left[\boldsymbol{x}\right]=\mathbb{E}\left[\left(\boldsymbol{x}-\overline{\boldsymbol{x}}\right)\left(\boldsymbol{x}-\overline{\boldsymbol{x}}\right)^{\mathrm{T}}\right]   \tag*{(A.7)}
$$

If  $X \sim p$, the mode of a distribution is denoted by

$$
\hat{x}=mode\left[p\right]=\underset{x}{\operatorname{argmax}}p(x)   \tag*{(A.8)}
$$

We denote parametric distributions using $p(\boldsymbol{x}|\boldsymbol{\theta})$, where $\boldsymbol{x}$are the random variables,$\boldsymbol{\theta}$are the parameters and$p$is a pdf or pmf. For example,$\mathcal{N}(x|\mu,\sigma^{2})$is a Gaussian (normal) distribution with mean$\mu$and standard deviation$\sigma$.

### A.7 Information theory

In this section, we summarize the notation we use for information theory (see Chapter 6 for details).

If  $X \sim p$, we denote the (differential) entropy of the distribution by  $\mathbb{H}(X)$ or  $\mathbb{H}(p)$. If  $Y \sim q$, we denote the KL divergence from distribution p to q by  $D_{\mathbb{K}\mathbb{L}}(p \parallel q)$. If  $(X, Y) \sim p$, we denote the mutual information between X and Y by  $\mathbb{I}(X; Y)$.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

### A.8 Statistics and machine learning

We briefly summarize the notation we use for statistical learning.

### A.8.1 Supervised learning

For supervised learning, we denote the observed features (also called inputs or covariates) by  $\boldsymbol{x} \in \mathcal{X}$. Often  $\mathcal{X} = \mathbb{R}^D$, meaning the features are real-valued. (Note that this includes the case of discrete-valued inputs, which can be represented as one-hot vectors.) Sometimes we compute manually-specified features of the input; we denote these by  $\phi(\boldsymbol{x})$. We also have outputs (also called targets or response variables)  $\boldsymbol{y} \in \mathcal{Y}$ that we wish to predict. Our task is to learn a conditional probability distribution  $p(\boldsymbol{y}|\boldsymbol{x}, \boldsymbol{\theta})$, where  $\boldsymbol{\theta}$ are the parameters of the model. If  $\mathcal{Y} = \{1, \ldots, C\}$, we call this classification. If  $\mathcal{Y} = \mathbb{R}^C$, we call this regression (often  $C = 1$, so we are just predicting a scalar response).

The parameters $\theta$are estimated from training data, denoted by$\mathcal{D} = \{(\mathbf{x}_n, \mathbf{y}_n) : n \in \{1, \ldots, N\}\}$(so$N$is the number of training cases). If$\mathcal{X} = \mathbb{R}^D$, we can store the training inputs in an $N \times D$design matrix denoted by$\mathbf{X}$. If $\mathcal{Y} = \mathbb{R}^C$, we can store the training outputs in an $N \times C$matrix$\mathbf{Y}$. If $\mathcal{Y} = \{1, \ldots, C\}$, we can represent each class label as a $C$-dimensional bit vector, with one element turned on (this is known as a one-hot encoding), so we can store the training outputs in an $N \times C$binary matrix$\mathbf{Y}$.

### A.8.2 Unsupervised learning and generative models

Unsupervised learning is usually formalized as the task of unconditional density estimation, namely modeling  $p(\boldsymbol{x}|\boldsymbol{\theta})$. In some cases, we want to perform conditional density estimation; we denote the values we are conditioning on by  $\boldsymbol{u}$, so the model becomes  $p(\boldsymbol{x}|\boldsymbol{u},\boldsymbol{\theta})$. This is similar to supervised learning, except that  $\boldsymbol{x}$ is usually high dimensional (e.g., an image) and  $\boldsymbol{u}$ is usually low dimensional (e.g., a class label or a text description).

In some models, we have latent variables, also called hidden variables, which are never observed in the training data. We call such models latent variable models (LVM). We denote the latent variables for data case n by  $z_n \in \mathcal{Z}$. Sometimes latent variables are known as hidden variables, and are denoted by  $h_n$. By contrast, the visible variables will be denoted by  $v_n$. Typically the latent variables are continuous or discrete, i.e.,  $\mathcal{Z} = \mathbb{R}^L$ or  $\mathcal{Z} = \{1, \ldots, K\}$.

Most LVMs have the form $p(\boldsymbol{x}_{n}, \boldsymbol{z}_{n}|\boldsymbol{\theta})$; such models can be used for unsupervised learning. However, LVMs can also be used for supervised learning. In particular, we can either create a generative (unconditional) model of the form $p(\boldsymbol{x}_{n}, \boldsymbol{y}_{n}, \boldsymbol{z}_{n}|\boldsymbol{\theta})$, or a discriminative (conditional) model of the form $p(\boldsymbol{y}_{n}, \boldsymbol{z}_{n}|\boldsymbol{x}_{n}, \boldsymbol{\theta})$.

### A.8.3 Bayesian inference

When working with Bayesian inference, we write the prior over the parameters as  $p(\boldsymbol{\theta}|\boldsymbol{\xi})$, where  $\boldsymbol{\xi}$ are the hyperparameters. For conjugate models, the posterior has the same form as the prior (by definition). We can therefore just update the hyperparameters from their prior value,  $\boldsymbol{\xi}$, to their posterior value,  $\widehat{\boldsymbol{\xi}}$.

In variational inference (Section 4.6.8.3), we use ψ to represent the parameters of the variational posterior, i.e.,  $p(\boldsymbol{\theta}|\mathcal{D}) \approx q(\boldsymbol{\theta}|\boldsymbol{\psi})$. We optimize the ELBO wrt ψ to make this a good approximation.

---

When performing Monte Carlo sampling, we use a $s$subscript or superscript to denote a sample (e.g.,$\theta_{s}$or$\theta^{s}$).

### A.9 Abbreviations

Here are some of the abbreviations used in the book.

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Abbreviation</td><td style='text-align: center; word-wrap: break-word;'>Meaning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>cdf</td><td style='text-align: center; word-wrap: break-word;'>Cumulative distribution function</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>CNN</td><td style='text-align: center; word-wrap: break-word;'>Convolutional neural network</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DAG</td><td style='text-align: center; word-wrap: break-word;'>Directed acyclic graph</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DML</td><td style='text-align: center; word-wrap: break-word;'>Deep metric learning</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>DNN</td><td style='text-align: center; word-wrap: break-word;'>Deep neural network</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>dof</td><td style='text-align: center; word-wrap: break-word;'>Degrees of freedom</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EB</td><td style='text-align: center; word-wrap: break-word;'>Empirical Bayes</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>EM</td><td style='text-align: center; word-wrap: break-word;'>Expectation maximization algorithm</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GLM</td><td style='text-align: center; word-wrap: break-word;'>Generalized linear model</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>GMM</td><td style='text-align: center; word-wrap: break-word;'>Gaussian mixture model</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMC</td><td style='text-align: center; word-wrap: break-word;'>Hamiltonian Monte Carlo</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>HMM</td><td style='text-align: center; word-wrap: break-word;'>Hidden Markov model</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iid</td><td style='text-align: center; word-wrap: break-word;'>Independent and identically distributed</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>iff</td><td style='text-align: center; word-wrap: break-word;'>If and only if</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>KDE</td><td style='text-align: center; word-wrap: break-word;'>Kernel density estimation</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>KL</td><td style='text-align: center; word-wrap: break-word;'>Kullback-Leibler divergence</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>KNN</td><td style='text-align: center; word-wrap: break-word;'>K nearest neighbor</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LHS</td><td style='text-align: center; word-wrap: break-word;'>Left hand side (of an equation)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LSTM</td><td style='text-align: center; word-wrap: break-word;'>Long short term memory (a kind of RNN)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>LVM</td><td style='text-align: center; word-wrap: break-word;'>Latent variable model</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MAP</td><td style='text-align: center; word-wrap: break-word;'>Maximum A Posterior estimate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MCMC</td><td style='text-align: center; word-wrap: break-word;'>Markov chain Monte Carlo</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MLE</td><td style='text-align: center; word-wrap: break-word;'>Maximum likelihood estimate</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MLP</td><td style='text-align: center; word-wrap: break-word;'>Multilayer perceptron</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MSE</td><td style='text-align: center; word-wrap: break-word;'>Mean squared error</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>NLL</td><td style='text-align: center; word-wrap: break-word;'>Negative log likelihood</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>OLS</td><td style='text-align: center; word-wrap: break-word;'>Ordinary least squares</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>psd</td><td style='text-align: center; word-wrap: break-word;'>Positive definite (matrix)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pdf</td><td style='text-align: center; word-wrap: break-word;'>Probability density function</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>pmf</td><td style='text-align: center; word-wrap: break-word;'>Probability mass function</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PNLL</td><td style='text-align: center; word-wrap: break-word;'>Penalized NLL</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>PGM</td><td style='text-align: center; word-wrap: break-word;'>Probabilistic graphical model</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RNN</td><td style='text-align: center; word-wrap: break-word;'>Recurrent neural network</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RHS</td><td style='text-align: center; word-wrap: break-word;'>Right hand side (of an equation)</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RSS</td><td style='text-align: center; word-wrap: break-word;'>Residual sum of squares</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>rv</td><td style='text-align: center; word-wrap: break-word;'>Random variable</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>RVM</td><td style='text-align: center; word-wrap: break-word;'>Relevance vector machine</td></tr></table>

<div style="text-align: center;">Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license</div>


---

SGD                      Stochastic gradient descent

SSE                     Sum of squared errors

SVI                      Stochastic variational inference

SVM                     Support vector machine

VB                      Variational Bayes

wrt                      With respect to

---

### Index

ADADELTA, 300

ADAGRAD, 299

ADAM, 300

PADAM, 301

RMSPROP, 299

RPROP, 299

YOGI, 301

1x1 convolution, 474

abstractive summarization, 542

action potential, 436

actions, 167

activation function, 428

activation maximization, 495

active, 305

active learning, 407, 650

active set, 399

activity regularization, 683

Adaboost.M1, 615

AdaBoostClassifier, 615

Adam, 447

Adamic/Adar, 758

adapters, 631

adaptive basis functions, 611

adaptive instance normalization, 501

adaptive learning rate, 299, 301

add-one smoothing, 122, 132, 335

additive attention, 521

additive model, 611

adjoint, 445

adjusted Rand index, 717

admissible, 192

ADOPT, 301

affine function, 8, 8

agent, 17, 167

aggregated gradient, 298

AGI, 28

AI, 28

AI ethics, 28

AI safety, 28

Akaike information criterion, 186

aleatoric uncertainty, 7, 34

AlexNet, 481

alignment, 522

alignment problem, 28

all pairs, 593

all pairs, 593

ALLS, 743

alternating least squares, 743

alternative hypothesis, 179, 198

ambient dimensionality, 690

amortized inference, 685

anchor, 555

anchor boxes, 490

ANN, 436

Anscombe's quartet, 43, 43

approximate posterior inference, 151

approximation error, 194

ARD, 411, 570, 598

ARD kernel, 570

area under the curve, 173

Armijo backtracking method, 286

Armijo-Goldstein, 286

artificial general intelligence, 28

artificial intelligence, 28

artificial neural networks, 436

associative, 242

asymptotic normality, 155

asymptotically optimal, 160

asynchronous training, 454

atomic bomb, 73

attention, 518, 522

attention kernel, 654

attention score, 519

attention weight, 519

AUC, 173

augmented intelligence, 28

auto-covariance matrix, 79

AutoAugment, 627

autocorrelation matrix, 79

autodiff, 438

autoencoder, 679

automatic differentiation, 438

automatic relevancy determination, 411, 570, 598

AutoML, 485

AutoRec, 745

autoregressive model, 101

average link clustering, 720

average pooling, 475

average precision, 175

axis aligned, 82

axis parallel splits, 603

axon, 436

---

B-splines, 399

backbone, 433

backfitting, 402

backpropagation, 428

backpropagation algorithm, 438

backpropagation through time, 510

backslash operator, 267

backsubstitution, 267, 375

bag, 655

bag of word embeddings, 26

bag of words, 24, 432

bagging, 609

BALD, 651

balloon kernel density estimator, 563

band-diagonal matrix, 239

bandwidth, 459, 560, 568

Barnes-Hut algorithm, 705

barycentric coordinates, 698

base measure, 93

basis, 233

basis function expansion, 425

basis vectors, 243

batch learning, 119

batch normalization, 477, 478

batch renormalization, 478

BatchBALD, 651

Bayes decision rule, 168

Bayes error, 127, 547

Bayes estimator, 168, 191

Bayes factor, 180

Bayes model averaging, 129

Bayes risk, 191

Bayes rule, 45

Bayes rule for Gaussians, 87

Bayes' rule, 45, 45

Bayes's rule, 45

Bayesian, 33

Bayesian  $\chi^{2}$-test, 188

Bayesian active learning by disagreement, 651

Bayesian decision theory, 167

Bayesian deep learning, 457

Bayesian factor regression, 677

Bayesian inference, 44, 46

Bayesian information criterion, 185

Bayesian machine learning, 147

Bayesian model selection, 185

Bayesian network, 100

Bayesian neural network, 457

Bayesian Occam's razor, 183

Bayesian optimization, 650

Bayesian personalized ranking, 747

Bayesian statistics, 129, 154

Bayesian t-test, 188

BBO, 319

Beam search, 515

belief state, 46

Berkson's paradox, 102

Bernoulli distribution, 49

Bernoulli mixture model, 98

BERT, 538

Bessel function, 570

beta distribution, 63, 121, 131

beta function, 63

beta-binomial, 135

BFGS, 290

bi-tempered logistic regression, 362

bias, 8, 159, 371

bias-variance tradeoff, 161, 459

BIC, 185

BIC loss, 186

BIC score, 186, 728

biclustering, 737

bidirectional RNN, 506

big data, 3

bigram model, 102, 212

bijector, 67

bilevel optimization, 195

binary classification, 2, 46

binary connect, 311

binary cross entropy, 342

binary entropy function, 208

binary logistic regression, 339

binomial coefficient, 50

binomial distribution, 50, 50

binomial regression, 416

BinomialBoost, 618

BIO, 541

BiT, 532

bits, 207

bivariate Gaussian, 81

black swan paradox, 122

blackbox, 319

blackbox optimization, 319

block diagonal, 239

block structured matrices, 250

Blue Brain Project, 438

BMA, 129

BMM, 98

BN, 477

BNN, 457

Boltzmann distribution, 55

BookCrossing, 742

Boolean logic, 34

Boosting, 611

bootstrap, 156

bottleneck, 679

bound optimization, 312, 354

bounding boxes, 489

bowl shape, 344

box constraints, 308

box plots, 44

boxcar kernel, 560, 562

branching factor, 212

Brier score, 179, 645

Brier Skill Score, 179

Brownian motion, 571

byte-pair encoding, 26

C-way N-shot classification, 653

C4, 543

C4.5, 605

calculus, 269

calculus of variations, 95

calibration plot, 420

canonical correlation analysis, 679

canonical form, 94

canonical link function, 417

canonical parameters, 93

CART, 603, 605

Cartesian, 68

Caser, 750

CatBoost, 619

categorical, 53

categorical PCA, 677

---

CatPCA, 677

Cauchy, 62

causal, 80

causal CNN, 517

causal convolution, 518

CBOW, 707, 708, 708

CCA, 679

cdf, 37, 57

center, 408

centering matrix, 113, 247, 696

central interval, 146

central limit theorem, 60, 72

centroids, 459

chain rule for entropy, 211

chain rule for mutual information, 219

chain rule of calculus, 273

chain rule of probability, 39

change of variables, 67

channels, 467, 473

characteristic equation, 254

characteristic length scale, 570

characteristic matrix, 222

chatbots, 543

ChatGPT, 542, 543

Chi-squared distribution, 65

Cholesky decomposition, 382

Cholesky factorization, 266

Chow's rule, 170

CIFAR, 20

city block distance, 718

class conditional density, 323

class confusion matrix, 172

class imbalance, 173, 359, 593

class-balanced sampling, 359

classes, 2

classical MDS, 692

classical statistics, 154

classification, 2, 778

Classification and regression trees, 603

CLIP, 635

closed world assumption, 550

cloze, 539

cloze task, 632

cluster assumption, 640

Clustering, 715

clustering, 97

clusters, 14

CNN, 3, 426, 467

co-adaptation, 455

Co-training, 642

co-clustering, 737

code generation, 543

codebook, 724

coefficient of determination, 381

CoLA, 543

cold start, 750

collaborative filtering, 737, 742

column rank, 237

column space, 233

column vector, 229

column-major order, 231

committee method, 608

commutative, 242

compactness, 720

comparison of classifiers, 187

complementary log-log, 418

complementary slackness, 305

complete link clustering, 720

completing the square, 88

complexity penalty, 121, 185

composite objective, 282

compositional, 434

compound hypothesis, 199

computation graph, 444

computer graphics, 493

concave, 278

condition number, 123, 238, 286

conditional computation, 463

conditional distribution, 38

conditional entropy, 210

conditional instance normalization, 500

conditional mixture model, 462

conditional mutual information, 219

conditional probability, 35

conditional probability distribution, 7, 50, 100

conditional probability table, 100

conditional variance formula, 42

conditionally independent, 35, 39, 99

confidence interval, 146, 157

confirmation bias, 639

conformer, 533

conjugate function, 279

conjugate gradient, 286, 375

conjugate prior, 87, 130, 130, 131

consensus sequence, 209

conservation of probability mass, 183

Consistency regularization, 644

consistent estimator, 192, 406

constrained optimization, 277

constrained optimization problem, 302

constrained optimization problems, 403

constraints, 277

contextual word embeddings, 26, 537, 712

contingency table, 189

continual learning, 551

continuation method, 398

continuous optimization, 275

continuous random variable, 36

contraction, 683

contractive autoencoder, 682

contradicts, 523

contrastive loss, 555

contrastive tasks, 633

control variate, 297

convex, 344

convex combination, 133

convex function, 278

convex optimization, 277

convex relaxation, 386

convex set, 277

ConvNeXt, 485, 533

convolution, 71, 468

convolution theorem, 71

convolution with holes, 486

convolutional Markov model, 517

convolutional neural network, 3, 21

convolutional neural networks, 12, 426, 467

coordinate descent, 397

coordinate vectors, 233

coordinated based representations, 429

coreference resolution, 527

coreset, 559

corpus, 706

correlation coefficient, 78, 82

---

correlation does not imply causation, 79

correlation matrix, 78, 114

cosine kernel, 571

cosine similarity, 706

cost function, 275

covariance, 77

covariance matrix, 77, 81

covariates, 2, 371, 778

COVID-19, 46

CPD, 100

CPT, 100

Cramer-Rao lower bound, 160

credible interval, 143, 146, 146

critical point, 303

cross correlation, 469

cross entropy, 209, 214, 216

cross validation, 126, 196

cross-covariance, 77

cross-entropy, 178

cross-over rate, 173

cross-validated risk, 126, 196

crosscat, 739

crowding problem, 703

cubic splines, 399

cumulants, 95

cumulative distribution function, 37, 57

curse of dimensionality, 548

curve fitting, 14

curved exponential family, 94

CV, 126, 196

cyclic permutation property, 236

cyclical learning rate, 296

DAG, 100, 444

data augmentation, 216, 627

data compression, 16, 725

data fragmentation, 605

data mining, 27

data parallelism, 454

data processing inequality, 223

Data science, 27

data uncertainty, 7, 34

Datasaurus Dozen, 43, 44

dead ReLU, 450

debiasing, 389

decision boundary, 5, 53, 149, 340

decision making under uncertainty, 1

decision rule, 5

decision surface, 6

decision tree, 6

decision trees, 603

decode, 657

decoder, 679, 687

deconvolution, 487

deduction, 201

deep CCA, 679

deep factorization machines, 748

deep graph infomax, 767

deep metric learning, 552, 554

deep mixture of experts, 463

deep neural networks, 12, 425

DeepDream, 497

DeepWalk, 760

default prior, 145

defender's fallacy, 75

deflated matrix, 713

deflation, 259

degree of normality, 61  

degrees of freedom, 13, 61, 383  

delta rule, 294  

demonstrations, 18  

dendrites, 436  

dendrogram, 718  

denoising autoencoder, 681  

dense prediction, 492  

dense sequence labeling, 507  

DenseNets, 484  

density estimation, 16  

density kernel, 520, 560  

dependent variable, 371  

depth prediction, 492  

depthwise separable convolution, 488  

derivative, 269  

derivative free optimization, 319  

descent direction, 283, 284  

design matrix, 3, 245, 426, 778  

determinant, 237  

development set, 124  

deviance, 185, 420, 606  

DFO, 319  

diagonal covariance matrix, 83  

diagonal matrix, 239  

diagonalizable, 255  

diagonally dominant, 240  

diameter, 720  

differentiable decision tree, 606  

differentiable programming, 444  

differential entropy, 212  

differentiating under the integral sign, 70  

differentiation, 270  

diffuse prior, 145  

dilated convolution, 486, 491  

dilation factor, 486  

dimensionality reduction, 4, 657  

Dirac delta function, 60, 148  

directed acyclic graph, 100, 444  

directional derivative, 270  

Dirichlet distribution, 138, 334  

Dirichlet energy, 701  

discrete AdaBoost, 614  

discrete optimization, 275  

discrete random variable, 35  

discretize, 213, 220  

discriminant function, 324  

discriminative classifier, 323, 336  

dispersion parameter, 415  

distance metric, 213  

distant supervision, 655  

distortion, 657, 722, 724  

distributional hypothesis, 705  

distributive, 242  

divergence measure, 213  

diverse beam search, 516  

DNA sequence motifs, 208  

DNN, 12, 425  

document retrieval, 706  

document summarization, 22  

domain adaptation, 630, 637  

domain adversarial learning, 637  

dominates, 192, 200  

dot product, 242  

double centering trick, 247  

double descent, 459  

double sided exponential, 63

---

dual feasibility, 305  

dual form, 588  

dual problem, 587  

dual variables, 594  

dummy encoding, 23, 53  

Dutch book theorem, 203  

dynamic graph, 446  

dynamic programming, 515

E step, 312, 314  

early stopping, 126, 455  

EB, 145  

echo state network, 511  

ECM, 670  

economy sized QR, 265  

economy sized SVD, 260  

edge devices, 311, 488  

EER, 173  

effect size, 187  

EfficientNetv2, 485  

eigenfaces, 659  

eigenvalue, 253  

eigenvalue decomposition, 253  

eigenvalue spectrum, 123  

eigenvector, 253  

Einstein summation, 248  

einsum, 248  

elastic embedding, 702  

elastic net, 390, 396  

ELBO, 153, 314, 685  

elbow, 728  

electronic health records, 523  

ell-2 loss, 9  

ELM, 584  

ELMo, 538  

ELPD, 187  

ELU, 450  

EM, 85, 312  

EMA, 119  

email spam classification, 22  

embarassingly parallel, 454  

embedding, 657  

EMNIST, 20  

empirical Bayes, 145, 182, 411  

empirical distribution, 65, 72, 109, 193, 215  

empirical risk, 6, 194  

empirical risk minimization, 7, 115, 194, 293  

encode, 657  

encoder, 679, 687  

encoder-decoder, 491  

encoder-decoder architecture, 509  

endogenous variables, 2  

energy based model, 635  

energy function, 152  

ensemble, 296, 457  

ensemble learning, 608  

entails, 523  

entity discovery, 722  

entity linking, 551  

entity resolution, 542, 551  

entropy, 178, 207, 314, 606  

entropy minimization, 639  

entropy SGD, 458  

Epanechnikov kernel, 561  

epigraph, 278  

epistemic uncertainty, 7, 34

epistemology, 34

epoch, 293

epsilon sensitive loss function, 595

equal error rate, 173

equality constraints, 277, 302

equitability, 222

equivalent sample size, 131

equivariance, 475

ERM, 115, 194

error function, 57

estimation error, 194

estimator, 154

EVD, 253

event, 34, 34, 35, 35

events, 33

evidence, 135, 182

evidence lower bound, 153, 314, 685

EWMA, 119, 299

exact line search, 286

exchangeable, 102

exclusive KL, 216

exclusive or, 460

exemplar-based models, 547

exemplars, 459

exogenous variables, 2

expectation maximization, 312

expected complete data log likelihood, 315

expected log pointwise predictive density, 187

expected sufficient statistics, 315

expected value, 40, 58

experiment design, 650

explaining away, 102

explanatory variables, 371

explicit feedback, 741

exploding gradient problem, 447

exploration-exploitation tradeoff, 751

exploratory data analysis, 4

exponential dispersion family, 415

Exponential distribution, 65

exponential family, 93, 96, 144

exponential family factor analysis, 675

exponential family PCA, 675

Exponential linear unit, 448

exponential loss, 614

exponential moving average, 119

exponentially weighted moving average, 119

exponentiated cross entropy, 212

exponentiated quadratic kernel, 568

extractive summarization, 542

extreme learning machine, 584

F score, 175

face detection, 489

face recognition, 489

face verification, 551

FaceNet, 557

factor analysis, 16, 666

factor loading matrix, 667

factorization machine, 748

FAISS, 550

false alarm rate, 172

false negative rate, 46

false positive rate, 46, 172

fan-in, 453

fan-out, 453

Fano's inequality, 225

farthest point clustering, 725

---

Fashion-MNIST, 20  

fast adaptation, 652  

fast Hadamard transform, 584  

fastfood, 584  

feasibility, 304  

feasibility problem, 277  

feasible set, 277  

feature crosses, 24  

feature detection, 471  

feature engineering, 12  

feature extraction, 12  

feature extractor, 372  

feature importance, 621, 621  

feature map, 471  

feature preprocessing, 12  

feature selection, 225, 310, 385  

features, 1  

featurization, 4  

feedforward neural network, 425  

few-shot classification, 551  

few-shot learning, 653  

FFNN, 425  

fill in, 27  

fill-in-the-blank, 539, 632  

filter, 469  

filter response normalization, 479  

filters, 467  

FIM, 155  

fine-grained classification, 21, 653  

fine-grained visual classification, 629  

fine-tune, 537  

fine-tuning phase, 629  

finite difference, 270  

finite sum problem, 293  

first order, 346  

first order Markov condition, 101  

first-order, 282, 289  

Fisher information matrix, 155, 348  

Fisher scoring, 348  

Fisher's linear discriminant analysis, 328  

FISTA, 398  

FLAN-T5, 543  

flat local minimum, 276  

flat minima, 457  

flat prior, 144  

flatten, 431  

FLDA, 328  

folds, 126, 196  

forget gate, 513  

forward mode differentiation, 439  

forward stagewise additive modeling, 612  

forwards KL, 216  

forwards model, 49  

founder variables, 673  

fraction of variance explained, 665  

fraud detection system, 770  

frequentist, 33  

frequentist decision theory, 189  

frequentist statistics, 154  

Frobenius norm, 236  

frozen parameters, 630  

full covariance matrix, 82  

full rank, 237  

full-matrix Adagrad, 301  

function space, 577  

furthest neighbor clustering, 720  

fused batchnorm, 477

gallery, 490, 550

GAM, 401

gamma distribution, 64

GANs, 637

Gated Graph Sequence Neural Networks, 76

gated recurrent units, 512

gating function, 462

Gaussian, 9

Gaussian discriminant analysis, 323

Gaussian distribution, 57

Gaussian kernel, 459, 535, 560, 568

Gaussian mixture model, 97

Gaussian process, 460

Gaussian process regression, 401

Gaussian processes, 574

Gaussian scale mixture, 105

GCN, 763

GDA, 323

GELU, 448, 451

generalization error, 197

generalization gap, 13, 194

generalize, 7, 121

generalized additive model, 401

generalized CCA, 679

generalized eigenvalue, 330

generalized Lagrangian, 304, 587

generalized linear models, 415

generalized low rank models, 675

generalized probit approximation, 367

Generative adversarial networks, 647

generative classifier, 323, 336

generative image model, 493

Geometric Deep Learning, 753

geometric series, 120, 287

Gini index, 605

glmnet, 397

GLMs, 415

global average pooling, 432, 476

global optimization, 275

global optimum, 275, 344

globally convergent, 276

Glorot initialization, 453

GloVe, 710

GMM, 97

GMRES, 376

GNN, 426, 762

goodness of fit, 380

GoogLeNet, 482

GPT, 542

GPT-2, 542

GPT-3, 542

GPT-4, 542

GPUs, 435, 454

GPyTorch, 583

gradient, 270, 283

gradient boosted regression trees, 618

gradient boosting, 616

gradient clipping, 447

gradient sign reversal, 637

gradient tree boosting, 618

Gram matrix, 241, 247, 500, 568

Gram Schmidt, 242

Graph attention network, 764

Graph convolutional networks, 763

graph factorization, 759

graph Laplacian, 700, 735

graph neural network, 762

---

graph neural networks, 426

graph partition, 734

Graph Representation Learning, 753

graphical models, 40

Graphical Mutual Information, 768

graphics processing units, 454

graphite, 767

GraphNet, 763

GraphSAGE, 763

GraRep, 759

greedy decoding, 515

greedy forward selection, 399

grid approximation, 152

grid search, 125, 320

group lasso, 394

group normalization, 479

group sparsity, 393

grouping effect, 396

GRU, 512

Gshard, 533

Gumbel noise, 516

HAC, 717

half Cauchy, 63

half spaces, 340

Hamiltonian Monte Carlo, 154

hard attention, 525

hard clustering, 98, 730

hard negatives, 556

hard thresholding, 388, 391

hardware accelerators, 437

harmonic mean, 175

hat matrix, 375

HDI, 147

He initialization, 453

heads, 433

heat map, 471

Heaviside, 346

Heaviside step function, 443

heaviside step function, 52, 426

heavy ball, 287

heavy tails, 62, 402

Helmholtz machine, 685

Hessian, 344, 776

Hessian matrix, 272

heteroskedastic regression, 59, 376

heuristics, 438

hidden, 45

hidden common cause, 79

hidden units, 427

hidden variables, 102, 312, 778

hierarchical, 434

hierarchical agglomerative clustering, 717

hierarchical Bayesian model, 145

hierarchical mixture of experts, 463

hierarchical softmax, 358

hierarchy, 357

highest density interval, 147

highest posterior density, 147

hinge loss, 116, 320, 591, 747

Hinton diagram, 86

hit rate, 172

HMC, 154

Hoeffding's inequality, 197

hogwild training, 454

holdout set, 196

homogeneous, 101

homoscedastic regression, 59

homotopy, 398

HPD, 147

Huber loss, 177, 404, 617

Huffman encoding, 358

human pose estimation, 493

Hutchinson trace estimator, 236, 237

hyper-parameters, 131, 319

hypercolumn, 474

hypernyms, 358

hyperparameter, 195

hyperparameters, 145

hyperplane, 340

hypothesis, 523

hypothesis space, 194

hypothesis testing, 179

I-projection, 216

IA, 28

ID3, 605

identifiability, 355

identifiable, 192, 355

identity matrix, 239

iid, 71, 108, 130

ill-conditioned, 114, 238

ill-posed, 49

ILP, 307

ILSVRC, 21

image captioning, 505

image classification, 3

image compression, 725

image interpolation, 688

image patches, 467

image tagging, 350, 488

image-to-image, 492

ImageNet, 21, 435, 481

ImageNet-21k, 533

IMDB, 128

IMDB movie review dataset, 22

implicit feedback, 747

implicit regularization, 457

impostors, 552

imputation tasks, 632

inception block, 482

Inceptionism, 497

inclusive KL, 216

incremental learning, 551

indefinite, 240

independent, 35, 39

independent and identically distributed, 71, 130

independent variables, 371

indicator function, 6, 36

induced norm, 235

inducing points, 583

induction, 122, 201

inductive bias, 13, 427, 532

inductive learning, 643

inequality constraints, 277, 302

infeasible, 306

inference, 107, 129

inference network, 684

infinitely wide, 582

InfoNCE, 556

information, 33

information content, 207

information criteria, 185

information diagram, 218

---

information diagrams, 219

information extraction, 541

information gain, 213, 650

information gathering action, 7

information projection, 216

information retrieval, 173

information theory, 178, 207

inner product, 242

input gate, 513

Instagram, 489

instance normalization, 478

instance segmentation, 490

instance-balanced sampling, 359

instance-based learning, 547

InstructGPT, 542

instruction fine-tuning, 543

Integer linear programming, 307

integrated risk, 191

integrating out, 129

intelligence augmentation, 28

inter-quartile range, 44

interaction effects, 23

intercept, 8

interior point method, 306

internal covariate shift, 477

interpolate, 12

interpolated precision, 175

interpolator, 574

interpretable, 17

intrinsic dimensionality, 690

inverse, 249

inverse cdf, 38

inverse document frequency, 25

inverse Gamma distribution, 65

inverse probability, 49

inverse problems, 49

inverse reinforcement learning, 28

inverse Wishart, 122

Iris, 2

Iris dataset, 3

IRLS, 348

isomap, 694

isotropic covariance matrix, 83

ISTA, 398

items, 741

iterate averaging, 297

iterative soft thresholding algorithm, 39

iteratively reweighted least squares, 348

Jacobian, 67, 352

Jacobian, 67, 352

Jacobian formulation, 271

Jacobian matrix, 271

Jacobian vector product, 271

Jensen's inequality, 214, 314

Jeopardy, 170

Jester, 742

JFT, 533

jittered, 461

joint distribution, 38

joint probability, 34

JPEG, 725

just in time, 446

JVP, 271

K nearest neighbor, 547 k-d tree, 550

K-means algorithm, 722

K-means clustering, 98

K-means++, 725

K-medoids, 725

Kalman filter, 91

Karl Popper, 122

Karush-Kuhn-Tucker, 305

Katz centrality index, 758

KDE, 560, 562

kernel, 469, 560

kernel density estimation, 560

kernel density estimator, 562

kernel function, 459, 567, 567

kernel PCA, 695, 737

kernel regression, 520, 564, 576

kernel ridge regression, 576, 595

kernel smoothing, 564

kernel trick, 590

keys, 518

keywords, 261

kink, 728

KKT, 305

KL divergence, 109, 177, 213, 314

KNN, 547

knots, 399

Knowledge distillation, 649

knowledge graph, 770

Kronecker product, 248

Krylov subspace methods, 583

KSG estimator, 220

Kullback Leibler divergence, 109, 177

Kullback-Leibler divergence, 213, 314

L-BFGS, 291

L0-norm, 385, 386

L1 loss, 176

L1 regularization, 385

L1VM, 598

L2 loss, 176

L2 regularization, 123, 349, 381

L2VM, 597

label, 2

label noise, 360, 655

Label propagation, 643, 761

label smearing, 358

label smoothing, 650, 655

Label spreading, 761

label switching problem, 319, 732

Lagrange multiplier, 303

Lagrange multipliers, 95, 111

Lagrange notation, 270

Lagrangian, 95, 259, 277, 303, 386

Lanczos algorithm, 671

language model, 101

language modeling, 22, 505

language models, 211, 537

Laplace, 385

Laplace approximation, 152, 363

Laplace distribution, 63

Laplace smoothing, 335

Laplace vector machine, 598

Laplace's rule of succession, 134

Laplacian eigenmaps, 699, 736, 757

LAR, 399

Large language models, 543

large margin classifier, 585

large margin nearest neighbor, 552

large margin nearest neighbor, 552

---

LASSO, 398

lasso, 307, 385

latent coincidence analysis, 553

latent factors, 15, 659

latent semantic analysis, 707

latent semantic indexing, 706

latent space interpolation, 688

latent variable, 96

latent variable models, 778

latent variables, 778

latent vector, 659

law of iterated expectations, 41

law of total expectation, 41

law of total variance, 42

layer normalization, 478

layer-sequential unit-variance, 453

LCA, 553

LDA, 323, 325

Leaky ReLU, 448

leaky ReLU, 450

learning curve, 127

learning rate, 283

learning rate schedule, 284, 294, 295

learning rate warmup, 296

learning to learn, 652

learning with a critic, 18

learning with a teacher, 18

least angle regression, 399

least favorable prior, 192

least mean squares, 294, 378

least squares boosting, 399, 612

least squares objective, 268

least squares solution, 10

leave-one-out cross-validation, 126, 196

LeCun initialization, 453

left pseudo inverse, 269

Leibniz notation, 270

LeNet, 476, 479

level sets, 82, 83

life-long learning, 551

LightGBM, 619

likelihood, 45

likelihood function, 129

likelihood principle, 202

likelihood ratio, 180, 201

likelihood ratio test, 198

limited memory BFGS, 291, 354

line search, 285

Linear algebra, 229

linear autoencoder, 680

linear combination, 243

linear discriminant analysis, 323, 325

linear function, 8

linear Gaussian system, 86

linear kernel, 581

linear map, 233

linear operator, 376

linear programming, 403

linear rate, 286

linear regression, 59, 371, 415, 425

linear subspace, 243

linear threshold function, 426

linear transformation, 233

linearity of expectation, 40

linearly dependent, 232

linearly independent, 232

linearly separable, 340

Link former, 535

link function, 415, 417

link prediction, 769

Lipschitz constant, 281

liquid state machine, 511

LLMs, 543

LMNN, 552

LMS, 294

local linear embedding, 697

local maximum, 276

local minimum, 275

local optimum, 275, 344

locality sensitive hashing, 550

locally linear regression, 565

locally-weighted scatterplot smoothing, 565

LOESS, 565

log bilinear language model, 711

log likelihood, 108

log loss, 178, 592

log odds, 52

log partition function, 93

log-sum-exp trick, 56

logistic, 51

logistic function, 52, 148

Logistic regression, 339

logistic regression, 8, 53, 148, 415

logit, 51, 339, 342

logit adjustment, 359

logit function, 52

logitBoost, 616

logits, 7, 55, 350

long short term memory, 513

long tail, 151, 358

Lorentz, 62

Lorentz model, 758

loss function, 6, 9, 167, 275

lossy compression, 724

lower triangular matrix, 240

LOWESS, 565

LSA, 707

lse, 56

LSH, 550

LSI, 706

LSTM, 513

M step, 312

M'th order Markov model, 101

M-projection, 216

M1, 646

M2, 646

machine learning, 1

machine translation, 22, 509

Mahalanobis distance, 83, 547

Mahalanobis whitening, 258

main effects, 23

majorize-minimize, 312

MALA, 493

MAML, 652

manifold, 689, 689

manifold assumption, 643

manifold hypothesis, 689

manifold learning, 689

mAP, 175

MAP estimate, 169

MAP estimation, 121, 195

MAR, 27

---

margin errors, 590

marginal distribution, 38

marginal likelihood, 45, 129, 135, 137, 145, 182

marginalizing out, 129, 148

marginalizing over, 129

marginally independent, 39

Markov chain, 101

Markov chain Monte Carlo, 153

Markov kernel, 101

Markov model, 101

MART, 618

masked attention, 520

masked language model, 539

matched filter, 468

matching network, 654

Matern kernel, 570

matrix, 229

matrix completion, 743

matrix determinant lemma, 252

matrix factorization, 743

matrix inversion lemma, 251, 594

matrix square root, 235, 245, 266

matrix vector multiplication, 583

max pooling, 475

maxent classifier, 357

maximal information coefficient, 221

maximum a posteriori estimation, 121

maximum a posteriori, 169

maximum entropy, 60, 207

maximum entropy classifier, 357

maximum entropy model, 95

maximum entropy sampling, 651

maximum expected utility principle, 168

maximum likelihood estimate, 8

maximum likelihood estimation, 107

maximum risk, 191

maximum variance unfolding, 697

MCAR, 27

McCulloch-Pitts model, 436

McKernel, 584

MCMC, 153

MDL, 186

MDN, 463

MDS, 691

mean, 40, 58

mean average precision, 175

mean function, 415

mean squared error, 9, 115

mean value imputation, 27

median, 38, 57

median absolute deviation, 563

medoid, 725

memory cell, 513

memory-based learning, 547

Mercer kernel, 567

Mercer's theorem, 568

message passing neural networks, 762

meta-learning, 652, 654

method of moments, 117

metric MDS, 693

Metropolis-adjusted Langevin algorithm, 493

MICE, 222

min-max scaling, 350

minibatch, 293

minimal, 3

minimal representation, 94

minimal sufficient statistic, 224

minimally informative prior, 145  

minimax estimator, 192  

minimum description length, 186  

minimum mean squared error, 176  

minimum message length, 186  

minimum spanning tree, 719  

minorize-maximize, 312  

MIP, 307  

misclassification rate, 6, 116  

missing at random, 27, 741  

missing completely at random, 27  

missing data, 26, 312  

missing data mechanism, 27, 647  

missing value imputation, 85  

mixed ILP, 307  

mixing weights, 137  

mixmatch, 640  

mixture density network, 463  

mixture model, 96  

mixture of Bernoulli, 98  

mixture of beta distributions, 136  

mixture of experts, 462, 533  

mixture of factor analyzers, 674  

mixture of Gaussians, 97  

ML, 1  

MLE, 8, 107  

MLP, 425, 427  

MLP-mixer, 427  

MM, 312  

MMSE, 176  

MNIST, 19, 479  

MobileNet, 488  

MoCo, 635  

mode, 41, 169  

mode-covering, 216  

mode-seeking, 217  

model compression, 455  

model fitting, 7, 107  

model parallelism, 454  

model selection, 181  

model selection consistent, 392  

model uncertainty, 7, 34  

model-agnostic meta-learning, 652  

modus tollens, 201  

MoE, 462  

MoG, 97  

moment projection, 216  

momentum, 287  

momentum contrastive learning, 635  

MoNet, 765  

Monte Carlo approximation, 73, 153, 3  

Monte Carlo dropout, 457  

Monty Hall problem, 47  

Moore-Penrose pseudo-inverse, 261  

most powerful test, 200  

motes, 11  

MovieLens, 742  

moving average, 119  

MSE, 9, 115  

multi-class classification, 350  

multi-clust, 739  

Multi-dimensional scaling, 757  

multi-headed attention, 527  

multi-instance learning, 655  

multi-label classification, 350  

multi-label classifier, 358

---

multi-object tracking, 551

multiclass logistic regression, 339

multidimensional scaling, 691

multilayer perceptron, 425, 427

multimodal, 41

multinomial coefficient, 54

multinomial distribution, 53, 54

Multinomial logistic regression, 350

multinomial logistic regression, 55, 339

multinomial logit, 54

multiple imputation, 85

multiple linear regression, 10, 371

multiple restarts, 725

multiplicative interaction, 518

multivariate Bernoulli naive Bayes, 332

multivariate Gaussian, 80

multivariate linear regression, 372

multivariate normal, 80

mutual information, 79, 217

mutually independent, 74

MVM, 583

MVN, 80

myopic, 651

N-pairs loss, 556

Nadaraya-Watson, 564

naive Bayes assumption, 327, 332

naive Bayes classifier, 332

named entity recognition, 541

NAS, 485

nats, 207

natural exponential family, 94

natural language inference, 523

natural language processing, 21, 357

natural language understanding, 49

natural parameters, 93

NBC, 332

NCA, 552

NCM, 328

nearest centroid classifier, 328

nearest class mean classifier, 328, 359

nearest class mean metric learning, 328

nearest neighbor clustering, 719

NEF, 94

negative definite, 240

negative log likelihood, 8, 108

negative semidefinite, 240

neighborhood components analysis, 552

neocognitron, 476

nested optimization, 195

nested partitioning, 739

Nesterov accelerated gradient, 288

Netflix Prize, 741

NetMF, 760

neural architecture search, 485

neural implicit representations, 429

neural language model, 102

neural machine translation, 509

neural matrix factorization, 749

neural style transfer, 497

neural tangent kernel, 582

NeurIPS, 18

neural, 523

Newton's method, 289, 347

next sentence prediction, 540

Neyman-Pearson lemma, 200

NHST, 200

NHWC, 474

NIPS, 18

NLL, 108

NLP, 21

NMAR, 27

no free lunch theorem, 13

node2vec, 760

noise floor, 127

non-identifiability, 732

non-identifiable, 410

non-metric MDS, 693

non-parametric bootstrap, 157

non-parametric methods, 689

non-parametric model, 460

non-saturating activation functions, 429, 449

noninformative, 144

nonlinear dimensionality reduction, 689

nonlinear factor analysis, 674

nonparametric methods, 567

nonparametric models, 547

nonsmooth optimization, 281

norm, 234, 238

normal, 9

normal distribution, 57

normal equations, 269, 373

Normal-Inverse-Wishart distribution, 318

normalization layers, 476

normalized, 241

normalized cut, 735

normalized mutual information, 221, 717

normalizer-free networks, 479

Normalizing flows, 648

not missing at random, 27

noun phrase chunking, 541

novelty detection, 551

NT-Xent, 556

nu-SVM classifier, 590

nuclear norm, 235

nucleotide, 208

null hypothesis, 179, 187, 198

null hypothesis significance testing, 200

nullspace, 233

numerator layout, 271

object detection, 489

objective, 144

objective function, 108, 275

observation distribution, 45

Occam factor, 185

Occam's razor, 183

offset, 10, 371

Old Faithful, 316

Olivetti face dataset, 658

OLS, 115, 269, 373

one-cycle learning rate schedule, 296

one-hot, 178

one-hot encoding, 23, 352, 778

one-hot vector, 53, 229

one-shot learning, 328, 653

one-sided p-value, 200

one-sided test, 187

one-standard error rule, 126

one-to-many functions, 461

one-versus-one, 593

one-versus-the-rest, 593

one-vs-all, 593

online learning, 119, 311, 551

---

OOV, 24, 26

open class, 26

open set recognition, 550

open world, 489

open world assumption, 551

OpenPose, 493

opt-einsum, 249

optimal policy, 168

optimism of the training error, 195

optimization problem, 275

order, 231

order statistics, 118

ordered Markov property, 100

ordering constraint, 733

ordinary least squares, 115, 269, 373

Ornstein-Uhlenbeck process, 571

orthodox statistics, 154

orthogonal, 241, 255

orthogonal projection, 375

orthogonal random features, 584

orthonormal, 241, 255

out of vocabulary, 26

out-of-bag instances, 609

out-of-distribution, 551

out-of-sample generalization, 689

out-of-vocabulary, 24

outer product, 243

outliers, 61, 176, 360, 402

output gate, 513

over-complete representation, 94

over-parameterized, 55, 459

overcomplete representation, 679

overdetermined, 266

overdetermined system, 374

overfitting, 13, 120, 133

p-value, 180, 200

PAC learnable, 197

PageRank, 258

pair plot, 4

paired test, 187

pairwise independent, 73

PAM, 726

panoptic segmentation, 491

parameter space, 275

parameter tying, 101

parameters, 6

parametric bootstrap, 157

parametric models, 547

parametric ReLU, 450

part of speech tagging, 541

part-of-speech, 538

partial dependency plot, 623

partial derivative, 270

partial least squares, 678

partial pivoting, 264

partial regression coefficient, 377

partially observed, 167

partition function, 56, 93, 635

partitioned inverse formulae, 250

partitioning around medoids, 726

Parzen window density estimator, 562

pathologies, 203

pattern recognition, 2

PCA, 16, 657, 658

PCA whitening, 257

pdf, 37, 58

peephole connections, 514

penalty term, 309

percent point function, 38

perceptron, 346, 426

perceptron learning algorithm, 346

Performer, 535

periodic kernel, 571

permutation test, 201

perplexity, 211, 505

person re-identification, 551

PersonLab, 493

perturbation theory, 736

PGM, 100

Planetoid, 768

plates, 103

Platt scaling, 591

PLS, 678

plug-in approximation, 133, 148

plugin approximation, 366

PMF, 744

pmf, 36

PMI, 707

Poincaré model, 758

point estimate, 107

point null hypothesis, 187

pointwise convolution, 474

pointwise mutual information, 707

Poisson regression, 417

polar, 68

policy, 17

Polyak-Ruppert averaging, 297

polynomial expansion, 372

polynomial regression, 10, 123, 372

polytope, 305

pool-based active learning, 650

population risk, 13, 125, 193

POS, 538

position weight matrix, 208, 209

positional embedding, 528

positive definite, 240

positive definite kernel, 567

positive PMI, 707

positive semidefinite, 240

post-norm, 530

posterior, 129

posterior distribution, 46, 129

posterior expected loss, 167

posterior inference, 46

posterior mean, 176

posterior median, 177

posterior predictive distribution, 129, 134, 148, 366, 200

power, 200

power method, 258

PPCA, 668

ppf, 38

pre-activation, 339

pre-activations, 428

pre-norm, 530

pre-train, 537

pre-trained word embedding, 26

pre-training phase, 629

preactivation resnet, 484

precision, 57, 141, 174, 174

precision at K, 174

precision matrix, 84, 112

precision-recall curve, 174

---

preconditioned SGD, 298

preconditioner, 298

preconditioning matrix, 298

predictive analytics, 27

predictors, 2

preferences, 167

premise, 523

PreResnet, 484

pretext tasks, 633

prevalence, 46, 175

primal problem, 587

primal variables, 595

principal components analysis, 16, 657

principal components regression, 384

prior, 121, 129

prior distribution, 45

probabilistic forecasting, 177

probabilistic graphical model, 100

probabilistic inference, 46

probabilistic matrix factorization, 744

probabilistic PCA, 657

probabilistic perspective, 1

probabilistic prediction, 177

probabilistic principal components analysis, 668

probability density function, 37, 58

probability distribution, 177

probability distributions, 1

probability mass function, 36

probability simplex, 138

probability theory, 45

probably approximately correct, 197

probit approximation, 367

probit function, 57, 367

probit link function, 418

product rule, 39

product rule of probability, 45

profile likelihood, 665

profile log likelihood, 666

projected gradient descent, 309, 398

projection, 234

projection matrix, 375

prompt, 542

prompt engineering, 543, 637

proper scoring rule, 179

prosecutor's fallacy, 75

proxies, 557

proximal gradient descent, 398

proximal gradient method, 308

proximal operator, 308

ProxQuant, 311

proxy tasks, 633

prune, 606

psd, 240

pseudo counts, 131, 334

pseudo inputs, 583

pseudo inverse, 373

pseudo norm, 235

pseudo-labeling, 639

pseudo-likelihood, 539

pure, 606

purity, 716

Pythagoras's theorem, 268

QALY, 167

QP, 306

quadratic approximation, 152

quadratic form, 240, 256  

quadratic kernel, 568  

quadratic loss, 9, 176  

quadratic program, 306, 386, 596  

quality-adjusted life years, 167  

quantile, 38, 57  

quantile function, 38  

quantization, 212  

quantize, 213, 220  

quantized, 311  

quartiles, 38, 57  

Quasi-Newton, 290  

quasi-Newton, 354  

queries, 518  

query synthesis, 650  

question answering, 22, 542

radial basis function, 560  

radial basis function kernel, 460, 535  

Rand index, 716  

RAND-WALK, 711  

random finite sets, 551  

random forests, 610  

random Fourier features, 584  

random number generator, 72  

random shuffling, 293  

random variable, 35  

random variables, 1  

random walk kernel, 573  

range, 233  

rank, 231, 237  

rank deficient, 237  

rank one update, 251  

rank-nullity theorem, 262  

ranking loss, 555, 747  

RANSAC, 404  

rate, 486, 725  

rate of convergence, 286  

rating, 741  

Rayleigh quotient, 258  

RBF, 560  

RBF kernel, 460, 568  

RBF network, 460  

real AdaBoost, 614  

recall, 172, 174  

receiver operating characteristic, 173  

receptive field, 473, 486  

recognition network, 684  

recommendation systems, 770  

Recommender systems, 741  

reconstruction error, 657, 659, 724  

Rectified linear unit, 448  

rectified linear unit, 429, 449  

recurrent neural network, 503  

recurrent neural networks, 12, 426  

recursive update, 119  

recursively, 377  

reduce-on-plateau, 296  

reduced QR, 265  

Reformer, 535  

region of practical equivalence, 187  

regression, 8, 778  

regression coefficient, 377  

regression coefficients, 8, 371  

regularization, 121  

regularization parameter, 121  

regularization path, 384, 389, 398

---

regularized discriminant analysis, 327

regularized empirical risk, 195

reinforcement learning, 17, 751

reinforcement learning from human feedback, 542

reject option, 170

reject the null hypothesis, 200

relational data, 741

relative entropy, 213

relevance vector machine, 598

ReLU, 429, 449

reparameterization trick, 686

representation learning, 633

reservoir computing, 512

reset gate, 513

reshape, 231

residual block, 451, 483

residual error, 115

residual network, 451

residual plot, 380

residual sum of squares, 115, 373

residuals, 9, 380

ResNet, 451, 483

ResNet-18, 484

response, 2

response variables, 778

responsibility, 98, 315, 463

reverse KL, 216

reverse mode differentiation, 440

reward, 18

reward function, 275

reward hacking, 28

RFF, 584

ridge regression, 123, 162, 381, 455

Riemannian manifold, 689

Riemannian metric, 689

right pseudo inverse, 268

risk, 167, 189

risk averse, 169, 170

risk neutral, 169

risk sensitive, 169

RL, 17

RLHF, 542

RMSE, 115, 381

RNN, 426, 503

Robbins-Monro conditions, 295

robust, 9, 61, 176

robust linear regression, 306

robust logistic regression, 360

robustness, 402

ROC, 173

root mean squared error, 115, 381

ROPE, 187

rotation matrix, 241

row rank, 237

row-major order, 231

RSS, 115

rule of iterated expectation, 104

rule of total probability, 38

running sum, 119

rv, 35

RVM, 598

saddle point, 277, 280

SAGA, 298, 346

same convolution, 471

SAMME, 615

Sammon mapping, 694

sample efficiency, 17  

sample mean, 160  

sample size, 2, 110, 130  

sample space, 35  

sample variance, 143  

sampling distribution, 154  

SARS-CoV-2, 46  

saturated model, 420  

saturates, 429  

scalar field, 270  

scalar product, 242  

scalars, 232  

scale of evidence, 180  

scaled dot-product attention, 521  

scatter matrix, 113, 246  

Schatten p-norm, 235  

scheduled sampling, 510  

Schur complement, 84, 250  

score function, 155, 275, 682  

scree plot, 664  

second order, 346  

Second-order, 289  

self-attention, 526  

self-normalization property, 711  

self-supervised, 632  

self-supervised learning, 16  

self-training, 638, 650  

SELU, 450  

semantic role labeling, 357  

semantic segmentation, 491  

semantic textual similarity, 525  

semi-hard negatives, 557  

semi-supervised embeddings, 768  

Semi-supervised learning, 638  

semi-supervised learning, 337  

semidefinite embedding, 697  

semidefinite programming, 552, 697  

sensible PCA, 668  

sensitivity, 46, 172  

sensor fusion, 92  

sentiment analysis, 22  

seq2seq, 507  

seq2seq model, 22  

seq2vec, 506  

sequence logo, 209  

sequence motif, 209  

sequential minimal optimization, 588  

SGD, 292  

SGNS, 709  

shaded nodes, 102  

shallow parsing, 541  

Shampoo, 301  

Shannon's source coding theorem, 209  

shared, 325  

sharp minima, 457  

sharpness aware minimization, 458  

Sherman-Morrison formula, 251  

Sherman-Morrison-Woodbury formula, 2  

shooting, 397  

short and fat, 3  

shrinkage, 90, 143, 384  

shrinkage estimation, 122  

shrinkage factor, 390, 617  

Siamese network, 555, 633  

side information, 750  

sifting property, 61, 148  

sigmoid, 51, 52, 148, 326

---

signal-to-noise ratio, 90

significance, 199

significance level, 200

silhouette coefficient, 728, 728

silhouette diagram, 728

silhouette score, 728

SiLU, 451

SimCLR, 633

similarity, 547

simple hypothesis, 199

simple linear regression, 9, 371

simple algorithm, 306

Simpson's paradox, 80

simulated annealing, 43

single link clustering, 719

single shot detector, 490

singular, 249

singular statistical model, 186

singular value decomposition, 260

singular values, 238, 260

singular vectors, 260

skip connections, 484

skip-gram with negative sampling, 709

skipgram, 707

skipgram model, 709

slack variables, 589, 596

slate, 750

slope, 10

SMACOF, 693

SMO, 588

smooth optimization, 281

Smoothing splines, 401

SNLI, 523

Sobel edge detector, 494

social networks, 770

soft clustering, 98

soft decision tree, 606

soft margin constraints, 589

soft thresholding, 388, 391

soft thresholding operator, 310

soft triple, 557

softmax, 54

softmax function, 7

Softplus, 448

softplus, 59

solver, 275

source dataset, 629

source domain, 637

span, 232

sparse, 138, 385

sparse Bayesian learning, 411

sparse factor analysis, 673

sparse GP, 583

sparse kernel machine, 460, 550

sparse linear regression, 307

sparse vector machines, 597

sparsity inducing regularizer, 310

specificity, 46

spectral clustering, 734

spectral CNNs, 763

spectral embedding, 699

spectral graph theory, 701

spectral radius, 447

spherical covariance matrix, 83

spherical embedding constraint, 559

split variable trick, 397

spurious correlation, 79

spurious correlations, 80  

spurious features, 337  

square, 230  

square-root sampling, 359  

square-root schedule, 296  

squared error, 176  

squared exponential kernel, 568  

stacking, 609  

standard basis, 233  

standard deviation, 41, 58  

standard error, 133, 156  

standard error of the mean, 126, 143  

standard form, 305  

standard normal, 57  

standardization operation, 246  

standardize, 350, 376  

standardized, 316  

standardizing, 256  

Stanford Natural Language Inference, 523  

state of nature, 167  

state space, 35  

state transition matrix, 101  

static graph, 446  

stationary, 101  

stationary kernels, 569  

stationary point, 276  

statistical learning theory, 196  

statistical machine translation, 509  

statistical relational learning, 771  

statistics, 27  

steepest descent, 284  

Stein's paradox, 193  

step decay, 296  

step function, 65  

step size, 283  

stochastic averaged gradient accelerated, 298  

stochastic beam search, 516  

stochastic gradient boosting, 618  

stochastic gradient descent, 292, 345  

stochastic gradient descent with warm restarts, 296  

stochastic matrix, 101  

stochastic neighbor embedding, 701  

stochastic optimization, 292  

stochastic variance reduced gradient, 297  

stochastic volatility model, 434  

Stochastic Weight Averaging, 297  

stochastic weight averaging, 458, 645  

stop word removal, 24  

storks, 80  

straight-through estimator, 311  

strain, 692  

stream-based active learning, 650  

stress function, 692  

strict, 192  

strict local minimum, 276  

strictly concave, 278  

strictly convex, 278  

strided convolution, 473  

string kernel, 573  

strong learner, 612  

strongly convex, 280  

structural deep network embedding, 766  

structural risk minimization, 195  

structured data, 425  

STS Benchmark, 525  

STSB, 543  

Student distribution, 61

---

Student t distribution, 61

subderivative, 443

subdifferentiable, 282

subdifferential, 282

subgradient, 282

submodular, 651

subword units, 26

sufficient statistic, 224

sufficient statistics, 93, 110, 112, 130

sum of squares matrix, 246

sum rule, 38

supervised learning, 1

supervised PCA, 677

support vector machine, 585

support vector machine regression, 597

support vectors, 585, 588, 597

surface normal prediction, 492

surrogate function, 312

surrogate loss function, 116

surrogate splits, 606

suspicious coincidence, 181

SVD, 260, 383

SVM, 307, 585

SVM regression, 597

SVRG, 297

Swish, 448

swish, 450

Swiss roll, 690

symmetric, 230

symmetric SNE, 702

synaptic connection, 436

synchronous training, 454

syntactic sugar, 103

systems of linear equations, 266

t-SNE, 701

T5, 543

tabular data, 3, 425

tall and skinny, 3

tangent space, 689

target, 2, 371

target dataset, 629

target domain, 637

target neighbors, 552

targets, 778

taxonomy, 357

Taylor series, 152

Taylor series expansion, 226

teacher forcing, 509

temperature, 55

tempered cross entropy, 361

tempered softmax, 361

template matching, 467, 471

tensor, 230, 473

tensor processing units, 437, 454

term frequency matrix, 25

term-document frequency matrix, 706

test risk, 13

test set, 13

test statistic, 200

text to speech, 518

textual entailment, 523

TF-IDF, 25

thin SVD, 260

thresholded linear unit, 479

TICE, 222

tied, 325

Tikhonov damping, 292

Tikhonov regularization, 292

time series forecasting, 505

time-invariant, 101

TinyImages, 20

TL;DR, 542

token, 24

topological instability, 694

topological order, 100

total derivative, 271

total differential, 271

total variation, 494

TPUs, 437, 454

trace, 236

trace norm, 235

trace trick, 236

tracing, 446

training, 7, 107

training data, 778

training set, 2

transductive learning, 643

transfer learning, 537, 559, 629

transformer, 526

transformers, 426

transition function, 101

transition kernel, 101

translation invariance, 467

transpose, 230

transposed convolution, 487, 492

treewidth, 249

Tri-cube kernel, 561

Tri-Training, 642

triangle inequality, 213

tridiagonal, 239

trigram model, 101

triplet loss, 555

true negative rate, 46

true positive rate, 46, 172

truncate, 511

truncated SVD, 264

trust-region optimization, 292

tube, 596

Turing machine, 504

TV, 494

two-part code, 186

two-sided p-value, 200

two-sided test, 187

type I error, 199

type I error rate, 172

type II error, 199

type II maximum likelihood, 145

typical patterns, 16

U-net, 491, 492

U-shaped curve, 13

UMAP, 705

unadjusted Langevin algorithm, 493

unbiased, 160

uncertainty, 33

unconditionally independent, 39

unconstrained optimization, 277

undercomplete representation, 679

underdetermined, 266

underfitting, 13, 124, 127

unidentifiable, 356

uninformative, 132, 144

uninformative prior, 143

---

union bound, 197

uniqueness, 667

unit vector, 229

unit vectors, 53

unitary, 241

universal function approximator, 434

UNK, 26

unrolled, 103

unstable, 608

unstructured data, 426

unsupervised learning, 14

unsupervised pre-training, 632

update gate, 513

upper triangular matrix, 240

users, 741

utility function, 168

VAE, 683

valid convolution, 471

validation risk, 125, 196

validation set, 13, 124, 196

value of information, 650

values, 518

vanishing gradient problem, 429, 447

variable metric, 290

variable selection, 392

variance, 40, 58

variation of information, 717

variational autoencoder, 16, 646, 683

variational autoencoders, 674

variational EM, 315

variational inference, 153

variational RNN, 505

varimax, 673

VC dimension, 198

vec2seq, 503

vector, 229

vector addition, 710

vector field, 270, 682

vector Jacobian product, 272

vector quantization, 724

vector space, 232

vector space model, 24

VI, 153

vicinal risk minimization, 628

violin plot, 44

virtual adversarial training, 644

visible variables, 778

visual n-grams, 637

visual scene understanding, 49

ViT, 532

Viterbi decoding, 515

VJP, 272

Voronoi iteration, 726

Voronoi tessellation, 548, 723

VQ, 724

WAIC, 733

wake sleep, 685

Wald interval, 159

Wald statistic, 200

warm start, 384

warm starting, 398

Watanabe-Akaike information criterion, 187

Watson, 170

wavenet, 518

weak learner, 612

weakly supervised learning, 655

WebText, 542

weight decay, 123, 349, 381, 455

weight space, 577

weighted least squares, 376

weighted least squares problem, 347

weighted linear regression, 376

weights, 8, 371

well-conditioned, 238

whiten, 256

wide and deep, 748

wide data, 3

wide format, 24

wide resnet, 484

widely applicable information criterion, 187

Widrow-Hoff rule, 294

winner takes all, 55

WMT dataset, 22

Wolfe conditions, 291

word analogy problem, 710

word embeddings, 26, 705, 705

word sense disambiguation, 538

word stemming, 24

word2vec, 707

wordpieces, 26

working response, 347

World Health Organization, 222

WSD, 538

Xavier initialization, 453

XGBoost, 619

XOR problem, 427

##### YOLO, 490

ZCA, 258

zero count, 122

zero-avoiding, 216

zero-forcing, 217

zero-one loss, 6, 169

zero-padding, 471

zero-shot classification, 637

zero-shot learning, 653

zero-shot task transfer, 542

zig-zag, 286

---



---

### Bibliography

[AAB21] A. Agrawal, A. Ali, and S. Boyd. “Minimum-distortion embedding”. en. In: Foundations and Trends in Machine Learning 14.3 (2021), pp. 211–378.

[AB08] C. Archambeau and F. Bach. "Sparse probabilistic projections". In: NIPS. 2008.

[AB14] G. Alain and Y. Bengio. "What Regularized Auto-Encoders Learn from the Data-Generating Distribution". In: JMLR (2014).

[AC16] D. K. Agarwal and B.-C. Chen. Statistical Methods for Recommender Systems. en. 1st edition. Cambridge University Press, 2016.

[Ace] “The Turing Test is Bad for Business”. In: (2021).

[AEH+18] S. Abu-El-Haija, B. Perozzi, R. Al-Rfou, and A. A. Alemi. "Watch your step: Learning node embeddings via graph attention". In: Advances in Neural Information Processing Systems. 2018, pp. 9180–9190.

[AEHPAR17] S. Abu-El-Haija, B. Perozzi, and R. Al-Rfou. "Learning Edge Representations via Low-Rank Asymmetric Projections". In: Proceedings of the 2017 ACM on Conference on Information and Knowledge Management. CIKM '17. 2017, 1787–1796.

[AEM18] Ö. D. Akyildiz, V. Elvira, and J. Miguez. "The Incremental Proximal Method: A Probabilistic Perspective". In: ICASSP. 2018.

[AFF19] C. Aicher, N. J. Foti, and E. B. Fox. “Adaptively Truncating Backpropagation Through Time to Control Gradient Bias”. In: (2019). arXiv: 1905.07473 [cs.LG].

[Agg16] C. C. Aggarwal. Recommender Systems: The Textbook. en. 1st ed. 2016 edition. Springer, 2016.

[Agg20] C. C. Aggarwal. Linear Algebra and Optimization for Machine Learning: A Textbook. en. 1st ed. 2020 edition. Springer, 2020.

[AGM19] V. Amrhein, S. Greenland, and B. McShane. "Scientists rise up against statistical significance". In: Nature 567.7748 (2019), p. 305.

[Agr70] A. Agrawala. "Learning with a probabilistic teacher". In: IEEE Transactions on Information Theory 16.4 (1970), pp. 373–379.

[AH19] C. Allen and T. Hospedales. "Analogies Explained: Towards Understanding Word Embeddings". In: ICML. 2019.

[AHK12] A. Anandkumar, D. Hsu, and S. M. Kakade. "A Method of Moments for Mixture Models and Hidden Markov Models". In: COLT. Vol. 23. Proceedings of Machine Learning Research. PMLR, 2012, pp. 33.1–33.34.

[Ahm+13] A. Ahmed, N. Shervashidze, S. Narayanamurthy, V. Josifovski, and A. J. Smola. "Distributed large-scale natural graph factorization". In: Proceedings of the 22nd international conference on World Wide Web. ACM. 2013, pp. 37–48.

[AK15] J. Andreas and D. Klein. "When and why are log-linear models self-normalizing?" In: Proc. ACL. Association for Computational Linguistics, 2015, pp. 244–249.

[Aka74] H. Akaike. "A new look at the statistical model identification". In: IEEE Trans. on Automatic Control 19.6 (1974).

[AKA91] D. W. Aha, D. Kibler, and M. K. Albert. "Instance-based learning algorithms". In: Mach. Learn. 6.1 (1991), pp. 37–66.

[Aky+19] Ö. D. Akyildiz, É. Chouzenoux, V. Elvira, and J. Míguez. "A probabilistic incremental proximal gradient method". In: IEEE Signal Process. Lett. 26.8 (2019).

[AL13] N. Ailon and E. Liberty. "An Almost Optimal Unrestricted Fast Johnson-Lindenstrauss Transform". In: ACM Trans. Algorithms 9.3 (2013), 21:1–21:12.

[Ala18] J. Alammar. Illustrated Transformer. Tech. rep. 2018.

[Alb+17] M. Alber, P.-J. Kindermans, K. Schütt, K.-R. Müller, and F. Sha. "An Empirical Study on The Properties of Random Bases for Kernel Methods". In: NIPS. Curran Associates, Inc., 2017, pp. 2763–2774.

[Alb+18] D. Albanese, S. Riccadonna, C. Donati, and P. Franceschi. "A practical tool for maximal information coefficient analysis". en. In: Giga-science 7.4 (2018), pp. 1–8.

[ALL18] S. Arora, Z. Li, and K. Lyu. "Theoretical Analysis of Auto Rate-Tuning by Batch Normalization". In: (2018). arXiv: 1812.03981 [cs.LG].

[Alm87] L. B. Almeida. "A learning rule for asynchronous perceptrons with feedback in a combinatorial environment." In: Proceedings, 1st First International Conference on Neural Networks. Vol. 2. IEEE. 1987, pp. 609–618.

[Alo+09] D. Aloise, A. Deshpande, P. Hansen, and P. Popat. "NP-hardness of Euclidean sum-of-squares clustering". In: Machine Learning 75 (2009), pp. 245–249.

[Alp04] E. Alpaydin. Introduction to machine learning. MIT Press, 2004.

[Ami+19] E. Amid, M. K. Warmuth, R. Anil, and T. Koren. "Robust Bi-Tempered Logistic Loss Based on Bregman Divergences". In: NIPS. 2019.

[Amo+16] D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané. "Concrete

---

Problems in AI Safety". In: (2016). arXiv:1606.06565 [cs.AI].

[Amo17] Amoeba. What is the difference between ZCA whitening and PCA whitening. Stack-exchange. 2017.

[And01] U. A. Anderson. "Heat and Violence". In: Current Directions in Psychological Science 10.1 (2001), pp. 33–38.

[And+18] R. Anderson, J. Huchette, C. Tjandraatmadja, and J. P. Vielma. "Strong convex relaxations and mixed-integer programming formulations for trained neural networks". In: (2018). arXiv: 1811.01988 [math.OC].

[Ani+20] R. Anil, V. Gupta, T. Koren, K. Regan, and Y. Singer. "Scalable Second Order Optimization for Deep Learning". In: (2020). arXiv:2002.09018 [cs.LG].

[Ans73] F. J. Anscombe. "Graphs in Statistical Analysis". In: Am. Stat. 27.1 (1973), pp. 17–21.

[Arc+19] F. Arcadu, F. Benmansour, A. Maunz, J. Willis, Z. Haskova, and M. Prunotto. "Deep learning algorithm predicts diabetic retinopathy progression in individual patients". en. In: NPJ Digit Med 2 (2019), p. 92.

[AO03] J.-H. Ahn and J.-H. Oh. "A Constrained EM Algorithm for Principal Component Analysis". In: Neural Computation 15 (2003), pp. 57–65.

[Ard+20] R. Ardila, M. Branson, K. Davis, M. Kohler, J. Meyer, M. Henretty, R. Morais, L. Saunders, F. Tyers, and G. Weber. "Common Voice: A Massively-Multilingual Speech Corpus". In: Proceedings of The 12th Language Resources and Evaluation Conference. 2020, pp. 4218–4222.

[Arj21] M. Arjovsky. "Out of Distribution Generalization in Machine Learning". In: (2021). arXiv:2103.02667 [stat.ML].

[Arn+19] S. M. R. Arnold, P.-A. Manzagol, R. Babanezhad, I. Mitliagkas, and N. Le Roux. "Reducing the variance in online optimization by transporting past gradients". In: NIPS. 2019.

[Aro+16] S. Arora, Y. Li, Y. Liang, T. Ma, and A. Risteski. "A Latent Variable Model Approach to PMI-based Word Embeddings". In: TACL 4 (2016), pp. 385–399.

[Aro+19] L. Aroyo, A. Dumitrache, O. Inel, Z. Szlávik, B. Timmermans, and C. Welty. "Crowdsourcing Inclusivity: Dealing with Diversity of Opinions, Perspectives and Ambiguity in Annotated Data". In: WWW. WWW '19. Association for Computing Machinery, 2019, pp. 1294–1295.

[Aro+21] R. Arora et al. Theory of deep learning. 2021.

[ARZP19] R. Al-Rfou, D. Zelle, and B. Perozzi. "DDGK: Learning Graph Representations for Deep Divergence Graph Kernels". In: Proceedings of the 2019 World Wide Web Conference on World Wide Web (2019).

[AS17] A. Achille and S. Soatto. "On the Emergence of Invariance and Disentangling in Deep Representations". In: (2017). arXiv: 1706.01350 [cs.LG].

[AS19] A. Achille and S. Soatto. "Where is the Information in a Deep Neural Network?" In: (2019). arXiv: 1905.12213 [cs.LG].

[Ash18] J. Asher. "A Rise in Murder? Let's Talk About the Weather". In: The New York Times (2018).

[ASR15] A. Ali, S. M. Shamsuddin, and A. L. Ralescu. "Classification with class imbalance problem: A Review". In: Int. J. Advance Soft Comput. Appl 7.3 (2015).

[Ath+19] B. Athiwaratkun, M. Finzi, P. Izmailov, and A. G. Wilson. "There Are Many Consistent Explanations of Unlabeled Data: Why You Should Average". In: ICLR. 2019.

[AV07] D. Arthur and S. Vassilvitskii. "k-means++: the advantages of careful seeding". In: Proc. 18th ACM-SIAM symp. on Discrete algorithms. 2007, 1027–1035.

[AWS19] E. Amid, M. K. Warmuth, and S. Srinivasan. "Two-temperature logistic regression based on the Tsallis divergence". In: AISTATS. 2019.

[Axl15] S. Axler. Linear algebra done right. 2015.

[BA10] R. Bailey and J. Addison. A Smoothed-Distribution Form of Nadaraya-Watson Estimation. Tech. rep. 10-30. Univ. Birmingham, 2010.

[BA97a] A. Bowman and A. Azzalini. Applied Smoothing Techniques for Data Analysis. Oxford, 1997.

[BA97b] L. A. Breslow and D. W. Aha. “Simplifying decision trees: A survey”. In: Knowl. Eng. Rev. 12.1 (1997), pp. 1–40.

[Bab19] S. Babu. A 2019 guide to Human Pose Estimation with Deep Learning. 2019.

[Bac+16] O. Bachem, M. Lucic, H. Hassani, and A. Krause. "Fast and Provably Good Seedings for k-Means". In: NIPS. 2016, pp. 55–63.

[Bah+12] B. Bahmani, B. Moseley, A. Vattani, R. Kumar, and S. Vassilvitskii. "Scalable k-Means++". In: VLDB. 2012.

[Bah+20] Y. Bahri, J. Kadmon, J. Pennington, S. Schoenholz, J. Sohl-Dickstein, and S. Ganguli. "Statistical Mechanics of Deep Learning". In: Annu. Rev. Condens. Matter Phys. (2020).

[BAP14] P. Bachman, O. Alsharif, and D. Precup. "Learning with pseudo-ensembles". In: Advances in neural information processing systems. 2014, pp. 3365–3373.

[Bar09] M. Bar. "The proactive brain: memory for predictions". en. In: Philos. Trans. R. Soc. Lond. B Biol. Sci. 364.1521 (2009), pp. 1235–1243.

[Bar19] J. T. Barron. "A General and Adaptive Robust Loss Function". In: CVPR. 2019.

[Bat+18] P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V. Zambaldi, M. Malinowski, A. Tacchetti, D. Raposo, A. Santoro, R. Faulkner, et al. "Relational inductive biases, deep learning, and graph networks". In: arXiv preprint arXiv:1806.01261 (2018).

[BB08] O. Bousquet and L. Bottou. "The Tradeoffs of Large Scale Learning". In: NIPS. 2008, pp. 161–168.

---

[BB11] L. Bottou and O. Bousquet. "The Tradeoffs of Large Scale Learning". In: Optimization for Machine Learning. Ed. by S. Sra, S. Nowozin, and S. J. Wright. MIT Press, 2011, pp. 351–368.

1. esian

    -ate Carlo".

    -math.OC].

[BC17] D. Beck and T. Cohn. "Learning Kernels over Strings using Gaussian Processes". In: Proceedings of the Eighth International Joint Conference on Natural Language Processing (Volume 2: Short Papers). Vol. 2. 2017, pp. 67–73.

[BCB15] D. Bahdanau, K. Cho, and Y. Bengio. "Neural Machine Translation by Jointly Learning to Align and Translate". In: ICLR. 2015.

[BCD01] L. Brown, T. Cai, and A. DasGupta. "Interval Estimation for a Binomial Proportion". In: Statistical Science 16.2 (2001), pp. 101–133.

[BCN18] L. Bottou, F. E. Curtis, and J. Nocedal. "Optimization Methods for Large-Scale Machine Learning". In: SIAM Rev. 60.2 (2018), pp. 223–311.

[BCV13] Y. Bengio, A. Courville, and P. Vincent. "Representation learning: a review and new perspectives". en. In: IEEE PAMI 35.8 (2013), pp. 1798–1828.

[BD20] B. Barz and J. Denzler. "Do We Train on Test Data? Purging CIFAR of Near-Duplicates". In: J. of Imaging 6.6 (2020).

[BD21] D. G. T. Barrett and B. Dherin. "Implicit Gradient Regularization". In: ICLR. 2021.

[BD87] G. Box and N. Draper. Empirical Model-Building and Response Surfaces. Wiley, 1987.

[BDEL03] S. Ben-David, N. Eiron, and P. M. Long. "On the difficulty of approximately maximizing agreements". In: J. Comput. System Sci. 66.3 (2003), pp. 496–514.

[Bel+19] M. Belkin, D. Hsu, S. Ma, and S. Mandal. "Reconciling modern machine-learning practice and the classical bias-variance trade-off". In: PNAS 116.32 (2019), pp. 15849–15854.

[Ben+04a] Y. Bengio, O. Delalleau, N. Roux, J. Paiement, P. Vincent, and M. Ouimet. "Learning eigenfunctions links spectral embedding and kernel PCA". In: Neural Computation 16 (2004), pp. 2197–2219.

[Ben+04b] Y. Bengio, J.-F. Paiement, P. Vincent, O. Delalleau, N. L. Roux, and M. Ouimet. "Out-of-Sample Extensions for LLE, Isomap, MDS, Eigenmaps, and Spectral Clustering". In: NIPS. MIT Press, 2004, pp. 177–184.

[Ben+15a] S. Bengio, O. Vinyals, N. Jaitly, and N. Shazeer. "Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks". In: NIPS. 2015.

[Ben+15b] Y. Bengio, D.-H. Lee, J. Bornschein, T. Mesnard, and Z. Lin. "Towards Biologically Plausible Deep Learning". In: (2015). arXiv: 1502.04156 [cs.LG].

[Ben+17] A. Benavoli, G. Corani, J. Demsar, and M. Zaffalon. "Time for a change: a tutorial

for comparing multiple classifiers through Bayesian analysis". In: JMLR (2017).

[Ber15] D. Bertsekas. Convex Optimization Algorithms. Athena Scientific, 2015.

[Ber16] D. Bertsekas. Nonlinear Programming. Third. Athena Scientific, 2016.

[Ber+19a] D. Berthelot, N. Carlini, E. D. Cubuk, A. Kurakin, K. Sohn, H. Zhang, and C. Raffel. "Remixmatch: Semi-supervised learning with distribution alignment and augmentation anchoring". In: arXiv preprint arXiv:1911.09785 (2019).

[Ber+19b] D. Berthelot, N. Carlini, I. Goodfellow, N. Papernot, A. Oliver, and C. Raffel. "Mixmatch: A holistic approach to semi-supervised learning". In: Advances in Neural Information Processing Systems. 2019, pp. 5049–5059.

[Ber+21] J. Berner, P. Grohs, G. Kutyniok, and P. Petersen. "The Modern Mathematics of Deep Learning". In: (2021). arXiv: 2105.04026 [cs.LG].

[Ber85] J. Berger. "Bayesian Salesmanship". In: Bayesian Inference and Decision Techniques with Applications: Essays in Honor of Bruno de Finetti. Ed. by P. K. Goel and A. Zellner. North-Holland, 1985.

[Ber99] D. Bertsekas. Nonlinear Programming. Second. Athena Scientific, 1999.

[Bey+19] M. Beyeler, E. L. Rounds, K. D. Carlson, N. Dutt, and J. L. Krichmar. "Neural correlates of sparse coding and dimensionality reduction". en. In: PLoS Comput. Biol. 15.6 (2019), e1006908.

[Bey+20] L. Beyer, O. J. Hénaff, A. Kolesnikov, X. Zhai, and A. van den Oord. "Are we done with ImageNet?" In: (2020). arXiv: 2006.07159 [cs.CV].

[BFO84] L. Breiman, J. Friedman, and R. Olshen. Classification and regression trees. Wadsworth, 1984.

[BG11] P. Buhlmann and S. van de Geer. Statistics for High-Dimensional Data: Methodology, Theory and Applications. Springer, 2011.

[BH07] P. Buhlmann and T. Hothorn. “Boosting Algorithms: Regularization, Prediction and Model Fitting”. In: Statistical Science 22.4 (2007), pp. 477–505.

[BH69] A. Bryson and Y.-C. Ho. Applied optimal control: optimization, estimation, and control. Blaisdell Publishing Company, 1969.

[BH86] J. Barnes and P. Hut. "A hierarchical O(N log N) force-calculation algorithm". In: Nature 324.6096 (1986), pp. 446–449.

[BH89] P. Baldi and K. Hornik. "Neural networks and principal components analysis: Learning from examples without local minima". In: Neural Networks 2 (1989), pp. 53–58.

[Bha+19] A. Bhadra, J. Datta, N. G. Polson, and B. T. Willard. "Lasso Meets Horseshoe: a survey". In: Bayesian Anal. 34.3 (2019), pp. 405–427.

[Bha+20] A. Bhadra, J. Datta, Y. Li, and N. Polson. "Horseshoe regularisation for machine learning

---

in complex and deep models". en. In: Int. Stat. Rev. 88.2 (2020), pp. 302–320.

[BHM92] J. S. Bridle, A. J. Heading, and D. J. MacKay. "Unsupervised Classifiers, Mutual Information and 'Phantom Targets'. In: Advances in neural information processing systems. 1992, pp. 1096–1101.

[BI19] P. Barham and M. Isard. "Machine Learning Systems are Stuck in a Rut". In: Proceedings of the Workshop on Hot Topics in Operating Systems. HotOS '19. Association for Computing Machinery, 2019, pp. 177–183.

[Bis06] C. Bishop. Pattern recognition and machine learning. Springer, 2006.

[Bis94] C. M. Bishop. Mixture Density Networks. Tech. rep. NCRG 4288. Neural Computing Research Group, Department of Computer Science, Aston University, 1994.

[Bis99] C. Bishop. "Bayesian PCA". In: NIPS. 1999.

[BJ05] F. Bach and M. Jordan. A probabilistic interpretation of canonical correlation analysis. Tech. rep. 688. U. C. Berkeley, 2005.

[BJM06] P. Bartlett, M. Jordan, and J. McAuliffe. "Convexity, Classification, and Risk Bounds". In: JASA 101.473 (2006), pp. 138–156.

[BK07] R. M. Bell and Y. Koren. "Lessons from the Netflix Prize Challenge". In: SIGKDD Explor. Newsl. 9.2 (2007), pp. 75–79.

[BK20] E. M. Bender and A. Koller. "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data". In: Proc. ACL. 2020, pp. 5185–5198.

[BKCl7] V. Badrinarayanan, A. Kendall, and R. Cipolla. "SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation". In: IEEE PAMI 39.12 (2017).

[BKH16] J. L. Ba, J. R. Kiros, and G. E. Hinton. "Layer Normalization". In: (2016). arXiv: 1607.06450 [stat.ML].

[BKL10] S. Bird, E. Klein, and E. Loper. Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit. 2010.

[BL04] P. Bickel and E. Levina. "Some theory for Fisher's linear discriminant function, " Naive Bayes", and some alternatives when there are many more variables than observations". In: Bernoulli 10 (2004), pp. 989–1010.

[BL07a] C. M. Bishop and J. Lasserre. "Generative or discriminative? Getting the best of both worlds". In: Bayesian Statistics 8. 2007.

[BL07b] J. A. Bullinaria and J. P. Levy. "Extracting semantic representations from word co-occurrence statistics: a computational study". en. In: Behav. Res. Methods 39.3 (2007), pp. 510–526.

[BL12] J. A. Bullinaria and J. P. Levy. "Extracting semantic representations from word co-occurrence statistics: stop-lists, stemming, and SVD". en. In: Behav. Res. Methods 44.3 (2012), pp. 890–907.

[BL88] D. S. Broomhead and D Lowe. "Multivariable Functional Interpolation and Adaptive Networks". In: Complex Systems (1988).

[BLK17] O. Bachem, M. Lucic, and A. Krause. “Distributed and provably good seedings for k-means in constant rounds”. In: ICML. 2017, pp. 292–300.

[Blo20] M. Blondel. Automatic differentiation. 2020.

[BLV19] X. Bouthillier, C. Laurent, and P. Vincent. "Unreproducible Research is Reproducible". In: ICML. Vol. 97. Proceedings of Machine Learning Research. PMLR, 2019, pp. 725–734.

[BM98] A. Blum and T. Mitchell. "Combining labeled and unlabeled data with co-training". In: Proceedings of the eleventh annual conference on Computational learning theory. 1998, pp. 92–100.

[BN01] M. Belkin and P. Niyogi. "Laplacian Eigenmaps and Spectral Techniques for Embedding and Clustering". In: NIPS. 2001, pp. 585–591.

[BNJ03] D. Blei, A. Ng, and M. Jordan. "Latent Dirichlet allocation". In: JMLR 3 (2003), pp. 993–1022.

[Bo+08] L. Bo, C. Sminchisescu, A. Kanaujia, and D. Metaxas. "Fast Algorithms for Large Scale Conditional 3D Prediction". In: CVPR. 2008.

[Boh92] D. Bohning. “Multinomial logistic regression algorithm”. In: Annals of the Inst. of Statistical Math. 44 (1992), pp. 197–200.

[Bon13] S. Bonnabel. "Stochastic gradient descent on Riemannian manifolds". In: IEEE Transactions on Automatic Control 58.9 (2013), pp. 2217–2229.

[Bos+16] D. Boscaini, J. Masci, E. Rodolà, and M. Bronstein. "Learning shape correspondence with anisotropic convolutional neural networks". In: Advances in Neural Information Processing Systems. 2016, pp. 3189–3197.

[Bot+13] L. Bottou, J. Peters, J. Quiñonero-Candela, D. X. Charles, D. M. Chickering, E. Portugal, D. Ray, P. Simard, and E. Snelson. "Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising". In: JMLR 14 (2013), pp. 3207–3260.

[Bow+15] S. R. Bowman, G. Angeli, C. Potts, and C. D. Manning. "A large annotated corpus for learning natural language inference". In: EMNLP. Association for Computational Linguistics, 2015, pp. 632–642.

[BPC20] I. Beltagy, M. E. Peters, and A. Cohan. "Longformer: The Long-Document Transformer". In: CoRR abs/2004.05150 (2020). arXiv: 2004.05150.

[Bre01] L. Breiman. "Random Forests". In: Machine Learning 45.1 (2001), pp. 5–32.

[Bre96] L. Breiman. "Bagging predictors". In: Machine Learning 24 (1996), pp. 123–140.

[Bri50] G. W. Brier. “Verification of forecasts expressed in terms of probability”. In: Monthly Weather Review 78.1 (1950), pp. 1–3.

[Bri90] J. Bridle. “Probabilistic Interpretation of Feedforward Classification Network Outputs, with Relationships to Statistical Pattern Recogni-

---

tion". In: Neurocomputing: Algorithms, Architectures and Applications. Ed. by F. F. Soulie and J. Herault. Springer Verlag, 1990, pp. 227–236.

[Bro+17a] M. M. Bronstein, J Bruna, Y LeCun, A Szlam, and P Vandergheynst. "Geometric Deep Learning: Going beyond Euclidean data". In: IEEE Signal Process. Mag. 34.4 (2017), pp. 18–42.

[Bro+17b] M. M. Bronstein, J. Bruna, Y. LeCun, A. Szlam, and P. Vandergheynst. "Geometric deep learning: going beyond euclidean data". In: IEEE Signal Processing Magazine 34.4 (2017), pp. 18–42.

[Bro19] J. Brownlee. Deep Learning for Computer Vision - Machine Learning Mastery. Accessed: 2020-6-30. Machine Learning Mastery, 2019.

[Bro+20] T. B. Brown et al. "Language Models are few-Shot Learners". In: (2020). arXiv: 2005.14165 [cs.CL].

[Bro+21] A. Brock, S. De, S. L. Smith, and K. Simonyan. "High-Performance Large-Scale Image Recognition Without Normalization". In: (2021). arXiv: 2102.06171 [cs.CV].

[BRR18] T. D. Bui, S. Ravi, and V. Ramavajjala. "Neural Graph Machines: Learning Neural Networks Using Graphs". In: WSDM. 2018.

[Bru+14] J. Bruna, W. Zaremba, A. Szlam, and Y. Lecun. "Spectral networks and locally connected networks on graphs International Conference on Learning Representations (ICLR2014)". In: CBLS, April (2014).

[Bru+19] G. Brunner, Y. Liu, D. Pascual, O. Richter, and R. Wattenhofer. "On the Validity of Self-Attention as Explanation in Transformer Models". In: (2019). arXiv:1908.04211 [cs.CL].

[BS02] M. Balasubramanian and E. L. Schwartz. "The isomap algorithm and topological stability". en. In: Science 295.5552 (2002), p. 7.

[BS16] P. Baldi and P. Sadowski. "A Theory of Local Learning, the Learning Channel, and the Optimality of Backpropagation". In: Neural Netw. 83 (2016), pp. 51–74.

[BS17] D. M. Blei and P. Smyth. "Science and data science". en. In: Proc. Natl. Acad. Sci. U. S. A. (2017).

[BS21] S. Bubeck and M. Sellke. "A Universal Law of Robustness via Isoperimetry". In: NIPS 34 (Dec. 2021), pp. 28811–28822.

[BS94] J. Bernardo and A. Smith. Bayesian Theory. John Wiley, 1994.

[BS97] A. J. Bell and T. J. Sejnowski. "The "independent components" of natural scenes are edge filters". en. In: Vision Res. 37.23 (1997), pp. 3327–3338.

[BT04] G. Bouchard and B. Triggs. "The tradeoff between generative and discriminative classifiers". In: IASC International Symposium on Computational Statistics (COMPSTAT '04). 2004.

[BT08] D. Bertsekas and J. Tsitsiklis. Introduction to Probability. 2nd Edition. Athena Scientific, 2008.

[BT09] A Beck and M Teboulle. "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems". In: SIAM J. Imaging Sci. 2.1 (2009), pp. 183–202.

[BT73] G. Box and G. Tiao. Bayesian inference in statistical analysis. Addison-Wesley, 1973.

[Bul11] A. D. Bull. “Convergence rates of efficient global optimization algorithms”. In: JMLR 12 (2011), 2879–2904.

[Bur10] C. J. C. Burges. "Dimension Reduction: A Guided Tour". en. In: Foundations and Trends in Machine Learning (2010).

[BV04] S. Boyd and L. Vandenberghe. Convex optimization. Cambridge, 2004.

[BW08] P. L. Bartlett and M. H. Wegkamp. "Classification with a Reject Option using a Hinge Loss". In: JMLR 9.Aug (2008), pp. 1823–1840.

[BW88] J. Berger and R. Wolpert. The Likelihood Principle. 2nd edition. The Institute of Mathematical Statistics, 1988.

[BWL19] Y. Bai, Y.-X. Wang, and E. Liberty. "ProxQuant: Quantized Neural Networks via Proximal Operators". In: ICLR. 2019.

[BY03] P. Buhlmann and B. Yu. “Boosting with the L2 loss: Regression and classification”. In: JASA 98.462 (2003), pp. 324–339.

[Byr+16] R Byrd, S Hansen, J Nocedal, and Y Singer. "A Stochastic Quasi-Newton Method for Large-Scale Optimization". In: SIAM J. Optim. 26.2 (2016), pp. 1008–1031.

[BZ20] A. Barbu and S.-C. Zhu. Monte Carlo Methods. en. Springer, 2020.

[Cal20] O. Calin. Deep Learning Architectures: A Mathematical Approach. en. 1st ed. Springer, 2020.

[Cao+18] Z. Cao, G. Hidalgo, T. Simon, S.-E. Wei, and Y. Sheikh. "OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields". In: (2018). arXiv: 1812.08008 [cs.CV].

[CAS16] P. Covington, J. Adams, and E. Sargin. "Deep Neural Networks for YouTube Recommendations". In: Proceedings of the 10th ACM Conference on Recommender Systems. RecSys'16. Association for Computing Machinery, 2016, pp. 191–198.

[CB02] G. Casella and R. Berger. Statistical inference. 2nd edition. Duxbury, 2002.

[CBD15] M. Courbariaux, Y. Bengio, and J.-P. David. "BinaryConnect: Training Deep Neural Networks with binary weights during propagations". In: NIPS. 2015.

[CC07] H. Choi and S. Choi. "Robust kernel Isomap". In: Pattern Recognit. 40.3 (2007), pp. 853–862.

[CCD17] B. P. Chamberlain, J. Clough, and M. P. Deisenroth. "Neural embeddings of graphs in hyperbolic space". In: arXiv preprint arXiv:1705.10359 (2017).

---

[CD14] K. Chaudhuri and S. Dasgupta. "Rates of Convergence for Nearest Neighbor Classification". In: NIPS. 2014.

[CD88] W. Cleveland and S. Devlin. "Locally-Weighted Regression: An Approach to Regression Analysis by Local Fitting". In: JASA 83.403 (1988), pp. 596–610.

[CDL16] J. Cheng, L. Dong, and M. Lapata. "Long Short-Term Memory-Networks for Machine Reading". In: EMNLP. Association for Computational Linguistics, 2016, pp. 551–561.

[CDL19] S. Chen, E. Dobriban, and J. H. Lee. "Invariance reduces Variance: Understanding Data Augmentation in Deep Learning and Beyond". In: (2019). arXiv: 1907.10905 [stat.ML].

[CDS02] M. Collins, S. Dasgupta, and R. E. Schapire. "A Generalization of Principal Components Analysis to the Exponential Family". In: NIPS-14. 2002.

[CEL19] Z. Chen, J. B. Estrach, and L. Li. "Supervised community detection with line graph neural networks". In: 7th International Conference on Learning Representations, ICLR 2019. 2019.

[Cer+17] D. Cer, M. Diab, E. Agirre, I. Lopez-Gazpio, and L. Specia. “SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation”. In: Proc. 11th Intl. Workshop on Semantic Evaluation (SemEval-2017). Association for Computational Linguistics, 2017, pp. 1–14.

[CFD10] Y. Cui, X. Z. Fern, and J. G. Dy. "Learning Multiple Nonredundant Clusterings". In: ACM Transactions on Knowledge Discovery from Data 4.3 (2010).

[CG16] T. Chen and C. Guestrin. "XGBoost: A Scalable Tree Boosting System". In: KDD. ACM, 2016, pp. 785–794.

[CG18] J. Chen and Q. Gu. “Closing the Generalization Gap of Adaptive Gradient Methods in Training Deep Neural Networks”. In: (2018). arXiv: 1806.06763 [cs.LG].

[CGG17] S. E. Chazan, J. Goldberger, and S. Gannot. "Speech Enhancement using a Deep Mixture of Experts". In: (2017). arXiv: 1703.09302 [cs.SD].

[CGW21] W. Chen, X. Gong, and Z. Wang. "Neural Architecture Search on ImageNet in Four GPU Hours: A Theoretically Inspired Perspective". In: ICLR. 2021.

[CH67] T. Cover and P. Hart. “Nearest neighbor pattern classification”. In: IEEE Trans. Inform. Theory 13.1 (1967), pp. 21–27.

[CH90] K. W. Church and P. Hanks. "Word Association Norms, Mutual Information, and Lexicography". In: Computational Linguistics (1990).

[Cha+01] O. Chapelle, J. Weston, L. Bottou, and V. Vapnik. "Vicinal Risk Minimization". In: NIPS. MIT Press, 2001, pp. 416–422.

[Cha+17] P. Chaudhari, A. Choromanska, S. Soatto, Y. LeCun, C. Baldassi, C. Borgs, J. Chayes, L. Sagun, and R. Zecchina. "Entropy-SGD: Biasing Gradient Descent Into Wide Valleys". In: ICLR. 2017.

[Cha+19a] I. Chami, Z. Ying, C. Ré, and J. Leskovec. "Hyperbolic graph convolutional neural networks". In: Advances in Neural Information Processing Systems. 2019, pp. 4869–4880.

[Cha+19b] J. J. Chandler, I. Martinez, M. M. Finucane, J. G. Terziev, and A. M. Resch. "Speaking on Data's Behalf: What Researchers Say and How Audiences Choose". en. In: Eval. Rev. (2019), p. 193841X19834968.

[Cha+21] I. Chami, S. Abu-El-Haija, B. Perozzi, C. Ré, and K. Murphy. "Machine Learning on Graphs: A Model and Comprehensive Taxonomy". In: JMLR (2021).

[Cha21] S. H. Chan. Introduction to Probability for Data Science. Michigan Publishing, 2021.

[Che+16] H.-T. Cheng et al. "Wide & Deep Learning for Recommender Systems". In: (2016). arXiv:1606.07792 [cs.LG].

[Che+20a] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton. "A Simple Framework for Contrastive Learning of Visual Representations". In: ICML. 2020.

[Che+20b] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton. "A simple framework for contrastive learning of visual representations". In: ICML. 2020.

[Che+20c] T. Chen, S. Kornblith, K. Swersky, M. Norouzi, and G. Hinton. "Big Self-Supervised Models are Strong Semi-Supervised Learners". In: NIPS. 2020.

[Chi+19a] W.-L. Chiang, X. Liu, S. Si, Y. Li, S. Bengio, and C.-J. Hsieh. "Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks". In: ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD). 2019.

[Chi+19b] R. Child, S. Gray, A. Radford, and I. Sutskever. "Generating Long Sequences with Sparse Transformers". In: CoRR abs/1904.10509 (2019). arXiv: 1904.10509.

[CHL05] S. Chopra, R. Hadsell, and Y. LeCun. "Learning a Similarity Metric Discriminatively, with Application to Face Verification". en. In: CVPR. 2005.

[Cho+14a] K. Cho, B. van Merrienboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, and Y. Bengio. "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation". In: EMNLP. 2014.

[Cho+14b] K. Cho, B. Van Merriënboer, D. Bahdanau, and Y. Bengio. "On the properties of neural machine translation: Encoder-decoder approaches". In: arXiv preprint arXiv:1409.1259 (2014).

[Cho+15] Y. Chow, A. Tamar, S. Mannor, and M. Pavone. "Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach". In: NIPS. 2015, pp. 1522–1530.

[Cho17] F. Chollet. Deep learning with Python. Manning, 2017.

[Cho+19] K. Choromanski, M. Rowland, W. Chen, and A. Weller. "Unifying Orthogonal Monte Carlo Methods". In: Proceedings of the 36th International Conference on Machine Learning, ICML 2019, 9-15 June 2019, Long Beach,

---

California, USA. Ed. by K. Chaudhuri and R. Salakhutdinov. Vol. 97. Proceedings of Machine Learning Research. PMLR, 2019, pp. 1203–1212.

[Cho+20a] K. Choromanski et al. "Masked Language Modeling for Proteins via Linearly Scalable Long-Context Transformers". In: (2020). arXiv: 2006.03555 [cs.LG].

[Cho+20b] K. Choromanski et al. "Rethinking Attention with Performers". In: CoRR abs/2009.14794 (2020). arXiv:2009.14794.

[Cho21] F. Chollet. Deep learning with Python (second edition). Manning, 2021.

[Cho70] C Chow. "On optimum recognition error and reject tradeoff". en. In: IEEE Trans. Inf. Theory 16.1 (Jan. 1970), pp. 41–46.

[Chr20] B. Christian. The Alignment Problem: Machine Learning and Human Values. en. 1st ed. W. W. Norton & Company, 2020.

[Chu+15] J. Chung, K. Kastner, L. Dinh, K. Goel, A. Courville, and Y. Bengio. "A Recurrent Latent Variable Model for Sequential Data". In: NIPS. 2015.

[Chu+22] H. W. Chung et al. "Scaling Instruction-Finetuned Language Models". In: (Oct. 2022). arXiv: 2210.11416 [cs.LG].

[Chu97] F. Chung. Spectral Graph Theory. AMS, 1997.

[Cir+10] D. C. Ciresan, U. Meier, L. M. Gambardella, and J. Schmidhuber. "Deep Big Simple Neural Nets For Handwritten Digit Recognition". In: Neural Computation 22.12 (2010), pp. 3207–3220.

[Cir+11] D. C. Ciresan, U. Meier, J. Masci, L. M. Gambardella, and J. Schmidhuber. "Flexible, High Performance Convolutional Neural Networks for Image Classification". In: IJCAI. 2011.

[CL96] B. P. Carlin and T. A. Louis. Bayes and Empirical Bayes Methods for Data Analysis. Chapman and Hall, 1996.

[Cla21] A. Clayton. Bernoulli's Fallacy: Statistical Illogic and the Crisis of Modern Science. en. Columbia University Press, 2021.

[CLX15] S. Cao, W. Lu, and Q. Xu. "Grarep: Learning graph representations with global structural information". In: Proceedings of the 24th ACM International on Conference on Information and Knowledge Management. ACM. 2015, pp. 891–900.

[CNB17] C. Chelba, M. Norouzi, and S. Bengio. "N-gram Language Modeling using Recurrent Neural Network Estimation". In: (2017). arXiv:1703.10724 [cs.CL].

[Coh+17] G. Cohen, S. Afshar, J. Tapson, and A. van Schaik. "EMNIST: an extension of MNIST to handwritten letters". In: (2017). arXiv: 1702.05373 [cs.CV].

[Coh94] J. Cohen. "The earth is round (p < .05)". In: American Psychologist 49.12 (1994), pp. 997–1003.

[Con+17] A. Conneau, D. Kiela, H. Schwenk, L. Barrault, and A. Bordes. “Supervised learning of universal sentence representations from

natural language inference data". In: arXiv preprint arXiv:1705.02364 (2017).

[Coo05] J. Cook. Exact Calculation of Beta Inequalities. Tech. rep. M. D. Anderson Cancer Center, Dept. Biostatistics, 2005.

[CP10] M. A. Carreira-Perpinan. "The Elastic Embedding Algorithm for Dimensionality Reduction". In: ICML. 2010.

[CP19] A. Coenen and A. Pearce. Understanding UMAP. 2019.

[CPS06] K. Chellapilla, S. Puri, and P. Simard. "High Performance Convolutional Neural Networks for Document Processing". In: 10th Intl. Workshop on Frontiers in Handwriting Recognition. 2006.

[CRW17] K. Choromanski, M. Rowland, and A. Weller. "The Unreasonable Effectiveness of Structured Random Orthogonal Embeddings". In: NIPS. 2017.

[CS20] F. E. Curtis and K Scheinberg. "Adaptive Stochastic Optimization: A Framework for Analyzing Stochastic Optimization Algorithms". In: IEEE Signal Process. Mag. 37.5 (2020), pp. 32–42.

[Csu17] G. Csurka. "Domain Adaptation for Visual Applications: A Comprehensive Survey". In: Domain Adaptation in Computer Vision Applications. Ed. by G. Csurka. 2017.

[CT06] T. M. Cover and J. A. Thomas. Elements of Information Theory. 2nd edition. John Wiley, 2006.

[CT91] T. M. Cover and J. A. Thomas. Elements of Information Theory. John Wiley, 1991.

[Cub+19] E. D. Cubuk, B. Zoph, D. Mane, V. Vasudevan, and Q. V. Le. "AutoAugment: Learning Augmentation Policies from Data". In: CVPR. 2019.

[CUH16] D.-A. Clevert, T. Unterthiner, and S. Hochreiter. "Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)". In: ICLR. 2016.

[Cui+19] X. Cui, K. Zheng, L. Gao, B. Zhang, D. Yang, and J. Ren. "Multiscale Spatial-Spectral Convolutional Network with Image-Based Framework for Hyperspectral Imagery Classification". en. In: Remote Sensing 11.19 (2019), p. 2220.

[Cur+17] J. D. Curtó, I. C. Zarza, F Yang, A Smola, F Torre, C. W. Ngo, and L Gool. "McKernel: A Library for Approximate Kernel Expansions in Log-linear Time". In: (2017). arXiv:1702.08159v14 [cs.LG].

[Cyb89] G. Cybenko. “Approximation by superpositions of a sigmoidal function”. In: Mathematics of Control, Signals, and Systems 2 (1989), 303–331.

[D'A+20] A. D'Amour et al. “Underspecification Presents Challenges for Credibility in Modern Machine Learning”. In: (2020). arXiv: 2011.03395 [cs.LG].

[Dah+11] G. E. Dahl, D. Yu, L. Deng, and A. Acero. "Large vocabulary continuous speech recognition with context-dependent DBN-HMMS". In: ICASSP. IEEE, 2011, pp. 4688–4691.

---

[Dai+19] Z. Dai, Z. Yang, Y. Yang, J. G. Carbonell, Q. V. Le, and R. Salakhutdinov. "TransformerXL: Attentive Language Models beyond a Fixed-Length Context". In: Proc. ACL. 2019, pp. 2978–2988.

[Dao+19] T. Dao, A. Gu, A. J. Ratner, V. Smith, C. De Sa, and C. Re. "A Kernel Theory of Modern Data Augmentation". In: ICML. 2019.

[Daul7] J. Daunizeau. “Semi-analytical approximations to statistical moments of sigmoid and softmax mappings of normal variables”. In: (2017). arXiv: 1703.00091 [stat.ML].

[Day+95] P. Dayan, G. Hinton, R. Neal, and R. Zemel. "The Helmholtz machine". In: Neural Networks 9.8 (1995).

[DB18] A. Defazio and L. Bottou. "On the Ineffectiveness of Variance Reduced Optimization for Deep Learning". In: (2018). arXiv: 1812.04529 [cs.LG].

[DBLJ14] A. Defazio, F. Bach, and S. Lacoste-Julien. "SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives". In: NIPS. Curran Associates, Inc., 2014, pp. 1646–1654.

[DDDM04] I Daubechies, M Defrise, and C De Mol. "An iterative thresholding algorithm for linear inverse problems with a sparsity constraint". In: Commun. Pure Appl. Math. Advances in E 57.11 (2004), pp. 1413–1457.

[Dee+90] S. Deerwester, S. Dumais, G. Furnas, T. Landauer, and R. Harshman. "Indexing by Latent Semantic Analysis". In: J. of the American Society for Information Science 41.6 (1990), pp. 391–407.

[DeG70] M. DeGroot. Optimal Statistical Decisions. McGraw-Hill, 1970.

[Den+12] J. Deng, J Krause, A. C. Berg, and L. Fei-Fei. "Hedging your bets: Optimizing accuracy-specificity trade-offs in large scale visual recognition". In: CVPR. 2012, pp. 3450–3457.

[Den+14] J. Deng, N. Ding, Y. Jia, A. Frome, K. Murphy, S. Bengio, Y. Li, H. Neven, and H. Adam. "Large-Scale Object Classification using Label Relation Graphs". In: ECCV. 2014.

[Dev+19] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". In: NAACL. 2019.

[DG06] J. Davis and M. Goadrich. "The Relationship Between Precision-Recall and ROC Curves". In: ICML. 2006, pp. 233–240.

[DHM07] P. Diaconis, S. Holmes, and R. Montgomery. "Dynamical Bias in the Coin Toss". In: SIAM Review 49.2 (2007), pp. 211–235.

[DHS01] R. O. Duda, P. E. Hart, and D. G. Stork. Pattern Classification. 2nd edition. Wiley Interscience, 2001.

[DHS11] J. Duchi, E. Hazan, and Y. Singer. "Adaptive Subgradient Methods for Online Learning and Stochastic Optimization". In: JMLR 12 (2011), pp. 2121–2159.

[Die98] T. G. Dietterich. "Approximate Statistical Tests for Comparing Supervised Classification

Learning Algorithms". In: Neural Computation. 10.7 (1998), pp. 1895–1923.

[Din+15] N. Ding, J. Deng, K. Murphy, and H. Neven. "Probabilistic Label Relation Graphs with Ising Models". In: ICCV. 2015.

[DJ15] S. Dray and J. Josse. “Principal component analysis with missing values: a comparative survey of methods”. In: Plant Ecol. 216.5 (2015), pp. 657–667.

[DKK12] G Dror, N Koenigstein, and Y Koren. "Web-Scale Media Recommendation Systems". In: Proc. IEEE 100.9 (2012), pp. 2722–2736.

[DKS95] J. Dougherty, R. Kohavi, and M. Sahami. "Supervised and Unsupervised Discretization of Continuous Features". In: ICML. 1995.

[DLLP97] T. Dietterich, R. Lathrop, and T. Lozano-Perez. "Solving the multiple instance problem with axis-parallel rectangles". In: Artificial Intelligence 89 (1997), pp. 31–71.

[DLR77] A. P. Dempster, N. M. Laird, and D. B. Rubin. "Maximum likelihood from incomplete data via the EM algorithm". In: J. of the Royal Statistical Society, Series B 34 (1977), pp. 1–38.

[DM01] D. van Dyk and X.-L. Meng. "The Art of Data Augmentation". In: J. Computational and Graphical Statistics 10.1 (2001), pp. 1–50.

[DM16] P. Drineas and M. W. Mahoney. "RandNLA: Randomized Numerical Linear Algebra". In: CACM (2016).

[DMB21] Y. Dar, V. Muthukumar, and R. G. Baraniuk. "A Farewell to the Bias-Variance Tradeoff? An Overview of the Theory of Overparameterized Machine Learning". In: (Sept. 2021). arXiv:2109.02355 [stat.ML].

[Do+19] T.-T. Do, T. Tran, I. Reid, V. Kumar, T. Hoang, and G. Carneiro. "A Theoretically Sound Upper Bound on the Triplet Loss for Improving the Efficiency of Deep Distance Metric Learning". In: CVPR. 2019, pp. 10404–10413.

[Doe16] C. Doersch. "Tutorial on Variational Autoencoders". In: (2016). arXiv: 1606.05908 [stat.ML].

[Don95] D. L. Donoho. “De-noising by soft-thresholding”. In: IEEE Trans. Inf. Theory 41.3 (1995), pp. 613–627.

[Dos+21] A. Dosovitskiy et al. "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale". In: ICLR. 2021.

[Doy+07] K. Doya, S. Ishii, A. Pouget, and R. P. N. Rao, eds. Bayesian Brain: Probabilistic Approaches to Neural Coding. MIT Press, 2007.

[DP97] P. Domingos and M. Pazzani. "On the Optimality of the Simple Bayesian Classifier under Zero-One Loss". In: Machine Learning 29 (1997), pp. 103–130.

[DR21] H. Duanmu and D. M. Roy. "On extended admissibale procedures and their nonstandard Bayes risk". In: Annals of Statistics (2021).

---

[Dri+04] P. Drineas, A. Frieze, R. Kannan, S. Vempala, and V. Vinay. "Clustering Large Graphs via the Singular Value Decomposition". In: Machine Learning 56 (2004), pp. 9–33.

[DS12] M. Der and L. K. Saul. "Latent Coincidence Analysis: A Hidden Variable Model for Distance Metric Learning". In: NIPS. Curran Associates, Inc., 2012, pp. 3230–3238.

[DSK16] V. Dumoulin, J. Shlens, and M. Kudlur. "A Learned Representation For Artistic Style". In: (2016). arXiv: 1610.07629 [cs.CV].

[Dum+18] A. Dumitrache, O. Inel, B. Timmermans, C. Ortiz, R.-J. Sips, L. Aroyo, and C. Welty. "Empirical Methodology for Crowdsourcing Ground Truth". In: Semantic Web Journal (2018).

[Duv14] D. Duvenaud. "Automatic Model Construction with Gaussian Processes". PhD thesis. Computational and Biological Learning Laboratory, University of Cambridge, 2014.

[DV16] V. Dumoulin and F. Visin. "A guide to convolution arithmetic for deep learning". In: (2016). arXiv: 1603.07285 [stat.ML].

[Dwi+23] R. Dwivedi, C. Singh, B. Yu, and M. J. Wainwright. "Revisiting minimum description length complexity in overparameterized models". In: J. Mach. Learn. Res. (2023).

[Dzi+23] N. Dziri et al. "Faith and Fate: Limits of Transformers on Compositionality". In: (May 2023). arXiv: 2305.18654 [cs.CL].

[EDH19] K. Ethayarajh, D. Duvenaud, and G. Hirst. "Towards Understanding Linear Word Analogies". In: Proc. ACL. Association for Computational Linguistics, 2019, pp. 3253–3262.

[EF15] D. Eigen and R. Fergus. “Predicting Depth, Surface Normals and Semantic Labels with a Common Multi-Scale Convolutional Architecture”. In: ICCV. 2015.

[Efr+04] B. Efron, I. Johnstone, T. Hastie, and R. Tibshirani. "Least angle regression". In: Annals of Statistics 32.2 (2004), pp. 407–499.

[Efr86] B. Efron. "Why Isn't Everyone a Bayesian?" In: The American Statistician 40.1 (1986).

[Efr87] B. Efron. The Jackknife, the Bootstrap, and Other Resampling Plans (CBMS-NSF Regional Conference Series in Applied Mathematics). en. Society for Industrial and Applied Mathematics, 1987.

[EH16] B. Efron and T. Hastie. Computer Age Statistical Inference: Algorithms, Evidence, and Data Science. en. Cambridge University Press, June 2016.

[Ein16] A Einstein. "Die Grundlage der allgemeinen Relativitätstheorie". In: Ann. Phys. 354.7 (1916), pp. 769–822.

[Eis19] J. Eisenstein. Introduction to Natural Language Processing. 2019.

[Elk03] C. Elkan. "Using the triangle inequality to accelerate k-means". In: ICML. 2003.

[EMH19] T. Elsken, J. H. Metzen, and F. Hutter. “Neural Architecture Search: A Survey”. In: JMLR 20 (2019), pp. 1–21.

[Erh+10] D. Erhan, Y. Bengio, A. Courville, P.-A. Manzagol, P. Vincent, and S. Bengio. "Why Does Unsupervised Pre-training Help Deep Learning?" In: JMLR 11 (2010), pp. 625–660.

[FAL17] C. Finn, P. Abbeel, and S. Levine. "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks". In: ICML. 2017.

[FB81] M. A. Fischler and R. Bolles. "Random sample concensus: A paradigm for model fitting with applications to image analysis and automated cartography". In: Comm. ACM 24.6 (1981), pp. 381–395.

[Fen+21] S. Y. Feng, V. Gangal, J. Wei, S. Chandar, S. Vosoughi, T. Mitamura, and E. Hovy. "A Survey of Data Augmentation Approaches for NLP". In: (2021). arXiv: 2105.03075 [cs.CL].

[Fer+10] D. Ferrucci et al. "Building Watson: An Overview of the DeepQA Project". In: AI Magazine (2010), pp. 59–79.

[FH20] E. Fong and C. Holmes. "On the marginal likelihood and cross-validation". In: Biometrika 107.2 (2020).

[FHK12] A. Feuerverger, Y. He, and S. Khatri. "Statistical Significance of the Netflix Challenge". In: Stat. Sci. 27.2 (2012), pp. 202–231.

[FHT00] J. Friedman, T. Hastie, and R. Tibshirani. "Additive logistic regression: a statistical view of boosting". In: Annals of statistics 28.2 (2000), pp. 337–374.

[FHT10] J. Friedman, T. Hastie, and R. Tibshirani. "Regularization Paths for Generalized Linear Models via Coordinate Descent". In: J. of Statistical Software 33.1 (2010).

[Fir57] J. Firth. "A synopsis of linguistic theory 1930-1955". In: Studies in Linguistic Analysis. Ed. by F. Palmer. 1957.

[FJ02] M. A. T. Figueiredo and A. K. Jain. "Unsupervised Learning of Finite Mixture Models". In: IEEE PAMI 24.3 (2002), pp. 381–396.

[FM03] J. H. Friedman and J. J. Meulman. "Multiple additive regression trees with application in epidemiology". en. In: Stat. Med. 22.9 (2003), pp. 1365–1381.

[FMN16] C. Fefferman, S. Mitter, and H. Narayanan. "Testing the manifold hypothesis". In: J. Amer. Math. Soc. 29.4 (2016), pp. 983–1049.

[FNW07] M. Figueiredo, R. Nowak, and S. Wright. "Gradient projection for sparse reconstruction: application to compressed sensing and other inverse problems". In: IEEE. J. on Selected Topics in Signal Processing (2007).

[For+21] P. Foret, A. Kleiner, H. Mobahi, and B. Neyshabur. "Sharpness-aware Minimization for Efficiently Improving Generalization". In: ICLR. 2021.

[Fos19] D. Foster. Generative Deep Learning: Teaching Machines to Paint, Write, Compose, and Play. 1 edition. O'Reilly Media, 2019.

[FR07] C. Fraley and A. Raftery. "Bayesian Regularization for Normal Mixture Estimation and Model-Based Clustering". In: J. of Classification 24 (2007), pp. 155–181.

---

[Fra+17] L. Franceschi, M. Donini, P. Frasconi, and M. Pontil. "Forward and Reverse Gradient-Based Hyperparameter Optimization". In: ICML. 2017.

[Fre98] B. Frey. Graphical Models for Machine Learning and Digital Communication. MIT Press, 1998.

[Fri01] J. Friedman. “Greedy Function Approximation: a Gradient Boosting Machine”. In: Annals of Statistics 29 (2001), pp. 1189–1232.

[Fri97a] J. Friedman. “On bias, variance, 0-1 loss and the curse of dimensionality”. In: J. Data Mining and Knowledge Discovery 1 (1997), pp. 55–77.

[Fri97b] J. H. Friedman. "Data mining and statistics: What's the connection". In: Proceedings of the 29th Symposium on the Interface Between Computer Science and Statistics. 1997.

[Fri99] J. Friedman. Stochastic Gradient Boosting. Tech. rep. 1999.

[FS96] Y. Freund and R. R. Schapire. "Experiments with a new boosting algorithm". In: ICML. 1996.

[FT05] M. Fashing and C. Tomasi. "Mean shift is a bound optimization". en. In: IEEE Trans. Pattern Anal. Mach. Intell. 27.3 (2005), pp. 471–474.

[Fu98] W. Fu. “Penalized regressions: the bridge versus the lasso”. In: J. Computational and graphical statistics 7 (1998), 397–416.

[Fuk75] K. Fukushima. “Cognitron: a self-organizing multilayered neural network”. In: Biological Cybernetics 20.6 (1975), pp. 121–136.

[Fuk80] K Fukushima. “Neocognitron: a self organizing neural network model for a mechanism of pattern recognition unaffected by shift in position”. en. In: Biol. Cybern. 36.4 (1980), pp. 193–202.

[Fuk90] K. Fukunaga. Introduction to Statistical Pattern Recognition. 2nd edition. Academic Press, 1990.

[Gag94] P. Gage. "A New Algorithm for Data Compression". In: Dr Dobbs Journal (1994).

[Gan+16] Y Ganin, E Ustinova, H Ajakan, P Germain, and others. "Domain-adversarial training of neural networks". In: JMLR (2016).

[Gär03] T. Gärtner. "A Survey of Kernels for Structured Data". In: SIGKDD Explor. Newsl. 5.1 (2003), pp. 49–58.

[Gar+18] J. Gardner, G. Pleiss, K. Q. Weinberger, D. Bindel, and A. G. Wilson. "GPyTorch: Blackbox Matrix-Matrix Gaussian Process Inference with GPU Acceleration". In: NIPS. Ed. by S Bengio, H Wallach, H Larochelle, K Grauman, N Cesa-Bianchi, and R Garnett. Curran Associates, Inc., 2018, pp. 7576–7586.

[GASG18] D. G. A. Smith and J. Gray. "opt-einsum - A Python package for optimizing contraction order for einsum-like expressions". In: JOSS 3.26 (2018), p. 753.

[GB05] Y. Grandvalet and Y. Bengio. "Semi-supervised learning by entropy minimization".

In: Advances in neural information processing systems. 2005, pp. 529–536.

[GB10] X. Glorot and Y. Bengio. "Understanding the difficulty of training deep feedforward neural networks". In: AISTATS. 2010, pp. 249–256.

[GB18] V. Garcia and J. Bruna. "Few-shot Learning with Graph Neural Networks". In: International Conference on Learning Representations (ICLR). 2018.

[GBB11] X. Glorot, A. Bordes, and Y. Bengio. "Deep Sparse Rectifier Neural Networks". In: AIS-TATS. 2011.

[GBC16] I. Goodfellow, Y. Bengio, and A. Courville. Deep Learning. http://www.deeplearningbook.org. MIT Press, 2016.

[GBD92] S. Geman, E. Bienenstock, and R. Dour-sat. "Neural networks and the bias-variance dilemma". In: Neural Computing 4 (1992), pp. 1–58.

[GC20] A. Gelman and B. Carpenter. "Bayesian analysis of tests with unknown specificity and sensitivity". In: J. of Royal Stat. Soc. Series C medrxiv;2020.05.22.20108944v2 (2020).

[GEB16] L. A. Gatys, A. S. Ecker, and M. Bethge. "Image style transfer using convolutional neural networks". In: CVPR. 2016, pp. 2414–2423.

[GEH19] T. Gale, E. Elsen, and S. Hooker. "The State of Sparsity in Deep Neural Networks". In: (2019). arXiv: 1902.09574 [cs.LG].

[Gel+04] A. Gelman, J. Carlin, H. Stern, and D. Rubin. Bayesian data analysis. 2nd edition. Chapman and Hall, 2004.

[Gel+14] A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin. Bayesian Data Analysis, Third Edition. Third edition. Chapman and Hall/CRC, 2014.

[Gel16] A. Gelman. "The problems with p-values are not just with p-values". In: American Statistician (2016).

[Gér17] A. Géron. Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools, and Techniques for Building Intelligent Systems. en. O'Reilly Media, Incorporated, 2017.

[Gér19] A. Géron. Hands-On Machine Learning with Scikit-Learn and TensorFlow: Concepts, Tools, and Techniques for Building Intelligent Systems (2nd edition). en. O'Reilly Media, Incorporated, 2019.

[GEY19] Y. Geifman and R. El-Yaniv. "SelectiveNet: A Deep Neural Network with an Integrated Reject Option". In: ICML. 2019.

[GG16] Y. Gal and Z. Ghahramani. "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning". In: ICML. 2016.

[GH96] Z. Ghahramani and G. Hinton. The EM Algorithm for Mixtures of Factor Analyzers. Tech. rep. Dept. of Comp. Sci., Uni. Toronto, 1996.

[GHK17] Y. Gal, J. Hron, and A. Kendall. "Concrete Dropout". In: (2017). arXiv: 1705.07832 [stat.ML].

---

[GHV14] A. Gelman, J. Hwang, and A. Vehtari. "Understanding predictive information criteria for Bayesian models". In: Statistics and Computing 24.6 (2014), pp. 997–1016.

[Gib97] M. Gibbs. "Bayesian Gaussian Processes for Regression and Classification". PhD thesis. U. Cambridge, 1997.

[Gil+17] J. Gilmer, S. S. Schoenholz, P. F. Riley, O. Vinyals, and G. E. Dahl. "Neural message passing for quantum chemistry". In: ICML. 2017, pp. 1263–1272.

[Gil+21] J. Gilmer, B. Ghorbani, A. Garg, S. Kudugunta, B. Neyshabur, D. Cardoze, G. Dahl, Z. Nado, and O. Firat. "A Loss Curvature Perspective on Training Instability in Deep Learning". In: (2021). arXiv: 2110.04369 [cs.LG].

[GIM99] A. Gionis, P. Indyk, and R. Motwani. "Similarity Search in High Dimensions via Hashing". In: Proc. 25th Intl. Conf. on Very Large Data Bases. VLDB '99. 1999, pp. 518–529.

[GKS18] V. Gupta, T. Koren, and Y. Singer. "Shampoo: Preconditioned Stochastic Tensor Optimization". In: ICML. 2018.

[GL15] B. Gu and C. Ling. "A New Generalized Error Path Algorithm for Model Selection". In: ICML. 2015.

[GL16] A. Grover and J. Leskovec. "node2vec: Scalable feature learning for networks". In: Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining. ACM. 2016, pp. 855–864.

[GMS05] M. Gori, G. Monfardini, and F. Scarselli. "A new model for learning in graph domains". In: Proceedings. 2005 IEEE International Joint Conference on Neural Networks, 2005. Vol. 2. IEEE. 2005, pp. 729–734.

[GNK18] R. A. Güler, N. Neverova, and I. Kokkinos. "Densepose: Dense human pose estimation in the wild". In: CVPR. 2018, pp. 7297–7306.

[God18] P. Godec. Graph Embeddings; The Summary. https://towardsdatascience.com/graph-embeddings-the-summary-cc6075aba007. 2018.

[GOF18] O. Gouvert, T. Oberlin, and C. Févotte. "Negative Binomial Matrix Factorization for Recommender Systems". In: (2018). arXiv: 1801.01708 [cs.LG].

[Gol+01] K. Goldberg, T. Roeder, D. Gupta, and C. Perkins. "Eigentaste: A Constant Time Collaborative Filtering Algorithm". In: Information Retrieval 4.2 (2001), pp. 133–151.

[Gol+05] J. Goldberger, S. Roweis, G. Hinton, and R. Salakhutdinov. "Neighbourhood Components Analysis". In: NIPS. 2005.

[Gol+92] D. Goldberg, D. Nichols, B. M. Oki, and D. Terry. "Using collaborative filtering to weave an information tapestry". In: Commun. ACM 35.12 (1992), pp. 61–70.

[Gon85] T. Gonzales. "Clustering to minimize the maximum intercluster distance". In: Theor. Comp. Sci. 38 (1985), pp. 293–306.

[Goo01] N. Goodman. "Classes for fast maximum entropy training". In: ICASSP. 2001.

[Goo+14] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio. "Generative Adversarial Networks". In: NIPS. 2014.

[Gor06] P. F. Gorder. "Neural Networks Show New Promise for Machine Vision". In: Computing in science & engineering 8.6 (2006), pp. 4–8.

[Got+19] A. Gotmare, N. S. Keskar, C. Xiong, and R. Socher. "A Closer Look at Deep Learning Heuristics: Learning rate restarts, Warmup and Distillation". In: ICLR. 2019.

[GOV18] W Gao, S Oh, and P Viswanath. "Demystifying Fixed k-Nearest Neighbor Information Estimators". In: IEEE Trans. Inf. Theory 64.8 (2018), pp. 5629–5661.

[GR07] T. Gneiting and A. E. Raftery. "Strictly Proper Scoring Rules, Prediction, and Estimation". In: JASA 102.477 (2007), pp. 359–378.

[GR18] A. Graves and M.-A. Ranzato. "Tutorial on unsupervised deep learning: part 2". In: NIPS. 2018.

[GR19] P. Grünwald and T. Roos. “Minimum description length revisited”. In: Int. J. Math. Ind. 11.01 (Dec. 2019), p. 1930001.

[Gra04] Y. Grandvalet. "Bagging Equalizes Influence". In: Mach. Learn. 55 (2004), pp. 251–270.

[Grall] A. Graves. "Practical variational inference for neural networks". In: Advances in neural information processing systems. 2011, pp. 2348–2356.

[Gra13] A. Graves. “Generating Sequences With Recurrent Neural Networks”. In: (2013). arXiv:1308.0850 [cs.NE].

[Gra+17] E. Grave, A. Joulin, M. Cissé, D. Grangier, and H. Jégou. "Efficient softmax approximation for GPUs". In: ICML. 2017.

[Gra+18] E. Grant, C. Finn, S. Levine, T. Darrell, and T. Griffiths. "Recasting Gradient-Based Meta-Learning as Hierarchical Bayes". In: ICLR. 2018.

[Gra+20] W. Grathwohl, K.-C. Wang, J.-H. Jacobsen, D. Duvenaud, M. Norouzi, and K. Swersky. "Your classifier is secretly an energy based model and you should treat it like one". In: ICLR. 2020.

[Gre+17] K. Greff, R. K. Srivastava, J. Koutnik, B. R. Steunebrink, and J. Schmidhuber. "LSTM: A Search Space Odyssey". In: IEEE Transactions on Neural Networks and Learning Systems 28.10 (2017).

[Gri20] T. L. Griffiths. "Understanding Human Intelligence through Human Limitations". en. In: Trends Cogn. Sci. 24.11 (2020), pp. 873–883.

[Gru07] P. Grunwald. The Minimum Description Length Principle. MIT Press, 2007.

[GS08] Y Guo and D Schuurmans. "Efficient global optimization for exponential family PCA and low-rank matrix factorization". In: 2008 46th Annual Allerton Conference on Communication, Control, and Computing. 2008, pp. 1100–1107.

---

[GS97] C. M. Grinstead and J. L. Snell. Introduction to probability (2nd edition). American Mathematical Society, 1997.

[GSK18] S. Gidaris, P. Singh, and N. Komodakis. "Unsupervised Representation Learning by Predicting Image Rotations". In: ICLR. 2018.

[GT07] L. Getoor and B. Taskar, eds. Introduction to Relational Statistical Learning. MIT Press, 2007.

[GTA00] G. Gigerenzer, P. M. Todd, and ABC Research Group. Simple Heuristics That Make Us Smart. en. Illustrated edition. Oxford University Press, 2000.

[Gu+18] A. Gu, F. Sala, B. Gunel, and C. Ré. “Learning Mixed-Curvature Representations in Product Spaces”. In: International Conference on Learning Representations (2018).

[Gua+10] Y. Guan, J. Dy, D. Niu, and Z. Ghahramani. "Variational Inference for Nonparametric Multiple Clustering". In: 1st Intl. Workshop on Discovering, Summarizing and Using Multiple Clustering (MultiClust). 2010.

[Gua+17] S. Guadarrama, K. Dahl, D. Bieber, M. Norouzi, J. Shlens, and K. Murphy. "PixColor: Pixel Recursive Colorization". In: BMVC. 2017.

[Gul+20] A. Gulati et al. "Conformer: Convolution-augmented Transformer for Speech Recognition". In: (2020). arXiv: 2005.08100 [eess.AS].

[Guo09] Y. Guo. “Supervised exponential family principal component analysis via convex optimization”. In: NIPS. 2009.

[Guo+17] H. Guo, R. Tang, Y. Ye, Z. Li, and X. He. "DeepFM: a factorization-machine based neural network for CTR prediction". In: IJCAI. IJCAI'17. AAAI Press, 2017, pp. 1725–1731.

[Gus01] M. Gustafsson. "A probabilistic derivation of the partial least-squares algorithm". In: Journal of Chemical Information and Modeling 41 (2001), pp. 288–294.

[GVZ16] A. Gupta, A. Vedaldi, and A. Zisserman. "Synthetic Data for Text Localisation in Natural Images". In: CVPR. 2016.

[GZE19] A. Grover, A. Zweig, and S. Ermon. "Graphite: Iterative Generative Modeling of Graphs". In: International Conference on Machine Learning. 2019, pp. 2434–2444.

[HA85] L. Hubert and P. Arabie. "Comparing Par-

titions". In: J. of Classification 2 (1985),

pp. 193–218.

[HAB19] M. Hein, M. Andriushchenko, and J. Bitterwolf. "Why ReLU networks yield high-confidence predictions far away from the training data and how to mitigate the problem". In: CVPR. 2019.

[Hac75] I. Hacking. The Emergence of Probability: A Philosophical Study of Early Ideas about Probability, Induction and Statistical Inference. Cambridge University Press, 1975.

[Háj08] A. Hájek. "Dutch Book Arguments". In: The Oxford Handbook of Rational and Social Choice. Ed. by P. Anand, P. Pattanaik, and C. Puppe. Oxford University Press, 2008.

[Han+20] B. Han, Q. Yao, T. Liu, G. Niu, I. W. Tsang, J. T. Kwok, and M. Sugiyama. "A Survey of Label-noise Representation Learning: Past, Present and Future". In: (2020). arXiv: 2011.04406 [cs.LG].

[Har54] Z. Harris. “Distributional structure”. In: Word 10.23 (1954), pp. 146–162.

[Has+04] T. Hastie, S. Rosset, R. Tibshirani, and J. Zhu. "The entire regularization path for the support vector machine". In: JMLR 5 (2004), pp. 1391–1415.

[Has+09] T. Hastie, S. Rosset, J. Zhu, and H. Zou. "Multi-class AdaBoost". In: Statistics and its Interface 2.3 (2009), pp. 349–360.

[Has+17] D. Hassabis, D. Kumaran, C. Summerfield, and M. Botvinick. "Neuroscience-Inspired Artificial Intelligence". en. In: Neuron 95.2 (2017), pp. 245–258.

[Has87] J. Hastad. Computational limits of small-depth circuits. MIT Press, 1987.

[HB17] X. Huang and S. Belongie. “Arbitrary style transfer in real-time with adaptive instance normalization”. In: ICCV. 2017.

[HBK23] P. Haluptzok, M. Bowers, and A. T. Kalai. "Language Models Can Teach Themselves to Program Better". In: ICLR. Feb. 2023.

[HCD12] D. Hoiem, Y. Chodpathumwan, and Q. Dai. "Diagnosing Error in Object Detectors". In: ECCV. 2012.

[HCL03] C.-W. Hsu, C.-C. Chang, and C.-J. Lin. A Practical Guide to Support Vector Classification. Tech. rep. Dept. Comp. Sci., National Taiwan University, 2003.

[HDR19] S. Hayou, A. Doucet, and J. Rousseau. "On the Impact of the Activation Function on Deep Neural Networks Training". In: (2019). arXiv:1902.06853 [stat.ML].

[He+15] K. He, X. Zhang, S. Ren, and J. Sun. "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification". In: ICCV. 2015.

[He+16a] K. He, X. Zhang, S. Ren, and J. Sun. "Deep Residual Learning for Image Recognition". In: CVPR. 2016.

[He+16b] K. He, X. Zhang, S. Ren, and J. Sun. "Identity Mappings in Deep Residual Networks". In: ECCV. 2016.

[He+17] X. He, L. Liao, H. Zhang, L. Nie, X. Hu, and T.-S. Chua. "Neural Collaborative Filtering". In: WWW. 2017.

[HE18] D. Ha and D. Eck. "A Neural Representation of Sketch Drawings". In: ICLR. 2018.

[He+20] K. He, H. Fan, Y. Wu, S. Xie, and R. Girshick. "Momentum contrast for unsupervised visual representation learning". In: CVPR. 2020, pp. 9729–9738.

[Hen+15] J. Hensman, A. Matthews, M. Filippone, and Z. Ghahramani. "MCMC for Variationally Sparse Gaussian Processes". In: NIPS. 2015, pp. 1648–1656.

---

[HG16] D. Hendrycks and K. Gimpel. “Gaussian Error Linear Units (GELUs)”. In: arXiv [cs.LG] (2016).

[HG20] J. Howard and S. Gugger. Deep Learning for Coders with Fastai and PyTorch: AI Applications Without a PhD. en. 1st ed. O'Reilly Media, 2020.

[HG21] M. K. Ho and T. L. Griffiths. “Cognitive science as a source of forward and inverse models of human decisions for robotics and control”. In: Annual Review of Control, Robotics, and Autonomous Systems. 2021.

[HGD19] K. He, R. Girshick, and P. Dollár. "Rethinking ImageNet Pre-training". In: CVPR. 2019.

[Hin+12] G. E. Hinton et al. "Deep Neural Networks for Acoustic Modeling in Speech Recognition: The Shared Views of Four Research Groups". In: IEEE Signal Process. Mag. 29.6 (2012), pp. 82–97.

[Hin13] G. Hinton. CSC 2535 Lecture 11: Non-linear dimensionality reduction. 2013.

[Hin14] G. Hinton. Lecture 6e on neural networks (RMSprop: Divide the gradient by a running average of its recent magnitude). 2014.

[HK15] F. M. Harper and J. A. Konstan. "The Movie-Lens Datasets: History and Context". In: ACM Trans. Interact. Intell. Syst. 5.4 (2015), pp. 1–19.

[HK92] A Hertz and J Krogh. "Generalization in a linear perceptron in the presence of noise". In: J. Physics A (1992).

[HKV19] F. Hutter, L. Kotthoff, and J. Vanschoren, eds. Automated Machine Learning - Methods, Systems, Challenges. Springer, 2019.

[HL04] D. R. Hunter and K. Lange. "A Tutorial on MM Algorithms". In: The American Statistician 58 (2004), pp. 30–37.

[HMT11] N. Halko, P.-G. Martinsson, and J. A. Tropp. "Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions". In: SIAM Rev., Survey and Review section 53.2 (2011), pp. 217–288.

[HN19] C. M. Holmes and I. Nemenman. “Estimation of mutual information for real-valued data with error bars and controlled bias”. en. In: Phys Rev E 100.2-1 (2019), p. 022404.

[Hoc+01] S. Hochreiter, Y. Bengio, P. Frasconi, and J. Schmidhuber. "Gradient flow in recurrent nets: the difficulty of learning long-term dependencies". In: A Field Guide to Dynamical Recurrent Neural Networks. Ed. by S. C. Kremer and J. F. Kolen. 2001.

[Hoe+14] R. Hoekstra, R. D. Morey, J. N. Rouder, and E.-J. Wagenmakers. "Robust misinterpretation of confidence intervals". en. In: Psychon. Bull. Rev. 21.5 (2014), pp. 1157–1164.

[Hoe+21] T. Hoefler, D. Alistarh, T. Ben-Nun, N. Dryden, and A. Peste. "Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks". In: (2021). arXiv:2102.00554 [cs.LG].

[Hof09] P. D. Hoff. A First Course in Bayesian Statistical Methods. Springer, 2009.

[Hor61] P Horst. "Generalized canonical correlations and their applications to experimental data". en. In: J. Clin. Psychol. 17 (1961), pp. 331–347.

[Hor91] K. Hornik. “Approximation Capabilities of Multilayer Feedforward Networks”. In: Neural Networks 4.2 (1991), pp. 251–257.

[Hos+19] M. Z. Hossain, F. Sohel, M. F. Shiratuddin, and H. Laga. "A Comprehensive Survey of Deep Learning for Image Captioning". In: ACM Computing Surveys (2019).

[HOT06] G. Hinton, S. Osindero, and Y. Teh. "A fast learning algorithm for deep belief nets". In: Neural Computation 18 (2006), pp. 1527–1554.

[Hot36] H. Hotelling. "Relations Between Two Sets of Variates". In: Biometrika 28.3/4 (1936), pp. 321–377.

[Hou+12] N. Houlsby, F. Huszar, Z. Ghahramani, and J. M. Hernández-lobato. "Collaborative Gaussian Processes for Preference Learning". In: NIPS. 2012, pp. 2096–2104.

[Hou+19] N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. de Laroussilhe, A. Gesmundo, M. Attariyan, and S. Gelly. "Parameter-Efficient Transfer Learning for NLP". In: ICML. 2019.

[How+17] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang, T. Weyand, M. Andreetto, and H. Adam. "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications". In: CVPR. 2017.

[HR03] G. E. Hinton and S. T. Roweis. "Stochastic Neighbor Embedding". In: NIPS. 2003, pp. 857–864.

[HR76] L. Hyafil and R. Rivest. "Constructing Optimal Binary Decision Trees is NP-complete". In: Information Processing Letters 5.1 (1976), pp. 15–17.

[HRP21] M. Huisman, J. N. van Rijn, and A. Plaat. "A Survey of Deep Meta-Learning". In: AI Review (2021).

[HS19] J. Haochen and S. Sra. "Random Shuffling Beats SGD after Finite Epochs". In: ICML. Vol. 97. Proceedings of Machine Learning Research. PMLR, 2019, pp. 2624–2633.

[HS97a] S Hochreiter and J Schmidhuber. "Flat minima". en. In: Neural Comput. 9.1 (1997), pp. 1–42.

[HS97b] S. Hochreiter and J. Schmidhuber. "Long short-term memory". In: Neural Computation 9.8 (1997), 1735–1780.

[HSW89] K. Hornik, M. Stinchcombe, and H. White. "Multilayer feedforward networks are universal approximators". In: Neural Networks 2.5 (1989), pp. 359–366.

[HT90] T. Hastie and R. Tibshirani. Generalized additive models. Chapman and Hall, 1990.

[HTF01] T. Hastie, R. Tibshirani, and J. Friedman. The Elements of Statistical Learning. Springer, 2001.

---

[HTF09] T. Hastie, R. Tibshirani, and J. Friedman. The Elements of Statistical Learning. 2nd edition. Springer, 2009.

[HTW15] T. Hastie, R. Tibshirani, and M. Wainwright. Statistical Learning with Sparsity: The Lasso and Generalizations. CRC Press, 2015.

[Hual4] G.-B. Huang. "An Insight into Extreme Learning Machines: Random Neurons, Random Features and Kernels". In: Cognit. Comput. 6.3 (2014), pp. 376–390.

[Hua+17a] G. Huang, Z. Liu, K. Q. Weinberger, and L. van der Maaten. "Densely Connected Convolutional Networks". In: CVPR. 2017.

[Hua+17b] J. Huang et al. "Speed/accuracy trade-offs for modern convolutional object detectors". In: CVPR. 2017.

[Hua+18] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon, C. Hawthorne, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck. "Music Transformer". In: (2018). arXiv:1809.04281 [cs.LG].

[Hub+08] M. F. Huber, T Bailey, H Durrant-Whyte, and U. D. Hanebeck. "On entropy approximation for Gaussian mixture random vectors". In: 2008 IEEE International Conference on Multisensor Fusion and Integration for Intelligent Systems. 2008, pp. 181–188.

[Hub64] P. Huber. "Robust Estimation of a Location Parameter". In: Annals of Statistics 53 (1964), 73–101.

[Hut90] M. F. Hutchinson. "A stochastic estimator of the trace of the influence matrix for laplacian smoothing splines". In: Communications in Statistics - Simulation and Computation 19.2 (1990), pp. 433–450.

[HVD14] G. Hinton, O. Vinyals, and J. Dean. "Distilling the Knowledge in a Neural Network". In: NIPS Deep Learning Workshop. 2014.

[HW62] D. Hubel and T. Wiesel. “Receptive fields, binocular interaction, and functional architecture in the cat’s visual cortex”. In: J. Physiology 160 (1962), pp. 106–154.

[HY01a] D. J. Hand and K. Yu. “Idiot's Bayes: Not So Stupid after All?” In: Int. Stat. Rev. 69.3 (2001), pp. 385–398.

[HY01b] M. Hansen and B. Yu. "Model selection and the principle of minimum description length". In: JASA (2001).

[HYL17] W. Hamilton, Z. Ying, and J. Leskovec. "Inductive representation learning on large graphs". In: Advances in Neural Information Processing Systems. 2017, pp. 1024–1034.

[Idr+17] H. Idrees, A. R. Zamir, Y.-G. Jiang, A. Gorban, I. Laptev, R. Sukthankar, and M. Shah. "The THUMOS challenge on action recognition for videos "in the wild". In: Comput. Vis. Image Underst. 155 (2017), pp. 1–23.

[Ie+19] E. Ie, V. Jain, J. Wang, S. Narvekar, R. Agarwal, R. Wu, H.-T. Cheng, T. Chandra, and C. Boutilier. "SlateQ: A tractable decomposition for reinforcement learning with recommendation sets". In: IJCAI. International Joint Conferences on Artificial Intelligence Organization, 2019.

[Iof17] S. Ioffe. "Batch Renormalization: Towards Reducing Minibatch Dependence in Batch-Normalized Models". In: (2017). arXiv: 1702.03275 [cs.LG].

[Ips09] I. Ipsen. Numerical matrix analysis: Linear systems and least squares. SIAM, 2009.

[IR10] A. Ilin and T. Raiko. “Practical Approaches to Principal Component Analysis in the Presence of Missing Values”. In: JMLR 11 (2010), pp. 1957–2000.

[IS15] S. Ioffe and C. Szegedy. "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift". In: ICML 2015, pp. 448–456.

[Isc+19] A. Iscen, G. Tolias, Y. Avrithis, and O. Chum. "Label Propagation for Deep Semi-supervised Learning". In: CVPR. 2019.

[Izm+18] P. Izmailov, D. Podoprikhin, T. Garipov, D. Vetrov, and A. G. Wilson. "Averaging Weights Leads to Wider Optima and Better Generalization". In: UAI. 2018.

[Izm+20] P. Izmailov, P. Kirichenko, M. Finzi, and A. G. Wilson. "Semi-supervised learning with normalizing flows". In: ICML. 2020, pp. 4615–4630.

[Jac+91] R. Jacobs, M. Jordan, S. Nowlan, and G. Hinton. "Adaptive mixtures of local experts". In: Neural Computation (1991).

[JAFF16] J. Johnson, A. Alahi, and L. Fei-Fei. "Perceptual Losses for Real-Time Style Transfer and Super-Resolution". In: ECCV. 2016.

[Jan18] E. Jang. Normalizing Flows Tutorial. https://blog.evjang.com/2018/01/nfl.html. 2018.

[Jay03] E. T. Jaynes. Probability theory: the logic of science. Cambridge university press, 2003.

[Jay76] E. T. Jaynes. “Confidence intervals vs Bayesian intervals”. In: Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science, vol II. Ed. by W. L. Harper and C. A. Hooker. Reidel Publishing Co., 1976.

[JD88] A. Jain and R. Dubes. Algorithms for Clustering Data. Prentice Hall, 1988.

[JDJ17] J. Johnson, M. Douze, and H. Jégou. "Billion-scale similarity search with GPUs". In: (2017). arXiv: 1702.08734 [cs.CV].

[Jef61] H. Jeffreys. Theory of Probability. Oxford, 1961.

[Jef73] H. Jeffreys. Scientific Inference. Third edition. Cambridge, 1973.

[JGH18] A. Jacot, F. Gabriel, and C. Hongler. "Neural Tangent Kernel: Convergence and Generalization in Neural Networks". In: NIPS. 2018.

[JH04] H. Jaeger and H. Haas. "Harnessing Nonlinearity: Predicting Chaotic Systems and Saving Energy in Wireless Communication". In: Science 304.5667 (2004).

[JHG00] N. Japkowicz, S. Hanson, and M. Gluck. "Non-linear autoassociation is not equivalent to PCA". In: Neural Computation 12 (2000), pp. 531–545.

---

[Jia+20] Y. Jiang, B. Neyshabur, H. Mobahi, D. Krishnan, and S. Bengio. "Fantastic Generalization Measures and Where to Find Them". In: ICLR. 2020.

[Jin+17] Y. Jing, Y. Yang, Z. Feng, J. Ye, Y. Yu, and M. Song. "Neural Style Transfer: A Review". In: arXiv [cs.CV] (2017).

[JJ94] M. I. Jordan and R. A. Jacobs. "Hierarchical mixtures of experts and the EM algorithm". In: Neural Computation 6 (1994), pp. 181–214.

[JK13] A. Jern and C. Kemp. "A probabilistic account of exemplar and category generation". en. In: Cogn. Psychol. 66.1 (2013), pp. 85–125.

[JM08] D. Jurafsky and J. H. Martin. Speech and language processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition. 2nd edition. Prentice-Hall, 2008.

[JM20] D. Jurafsky and J. H. Martin. Speech and language processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition (Third Edition). Draft of 3rd edition. 2020.

[Jor19] M. Jordan. "Artificial Intelligence — The Revolution Hasn't Happened Yet". In: Harvard Data Science Review 1.1 (2019).

[JT19] L. Jing and Y. Tian. "Self-supervised Visual Feature Learning with Deep Neural Networks: A Survey". In: (2019). arXiv: 1902.06162 [cs.CV].

[Jun+19] W. Jung, D. Jung, B. Kim, S. Lee, W. Rhee, and J. Anh. "Restructuring Batch Normalization to Accelerate CNN Training". In: SysML 2019.

[JW19] S. Jain and B. C. Wallace. "Attention is not Explanation". In: NAACL. 2019.

[JZ13] R. Johnson and T. Zhang. "Accelerating Stochastic Gradient Descent using Predictive Variance Reduction". In: NIPS. Curran Associates, Inc., 2013, pp. 315–323.

[JZS15] R. Jozefowicz, W. Zaremba, and I. Sutskever. "An Empirical Exploration of Recurrent Network Architectures". In: ICML. 2015, pp. 2342–2350.

[KAG19] A. Kirsch, J. van Amersfoort, and Y. Gal. "BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning". In: NIPS. 2019.

[Kai58] H. Kaiser. “The varimax criterion for analytic rotation in factor analysis”. In: Psychometrika 23.3 (1958).

[Kan+12] E. Kandel, J. Schwartz, T. Jessell, S. Siegelbaum, and A. Hudspeth, eds. Principles of Neural Science. Fifth Edition. 2012.

[Kan+20] B. Kang, S. Xie, M. Rohrbach, Z. Yan, A. Gordo, J. Feng, and Y. Kalantidis. "Decoupling Representation and Classifier for Long-Tailed Recognition". In: ICLR. 2020.

[Kap16] J. Kaplan. Artificial Intelligence: What Everyone Needs to Know. en. 1st ed. Oxford University Press, 2016.

[Kat+20] A. Katharopoulos, A. Vyas, N. Pappas, and F. Fleuret. "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention". In: ICML. 2020.

[KB15] D. Kingma and J. Ba. "Adam: A Method for Stochastic Optimization". In: ICLR. 2015.

[KB19] M. Kaya and H. S. Bilge. "Deep Metric Learning: A Survey". en. In: Symmetry 11.9 (2019), p. 1066.

[KBV09] Y. Koren, R. Bell, and C. Volinsky. "Matrix factorization techniques for recommender systems". In: IEEE Computer 42.8 (2009), pp. 30–37.

[KD09] A. D. Kiureghian and O. Ditlevsen. "Aleatory or epistemic? Does it matter?" In: Structural Safety 31.2 (2009), pp. 105–112.

[Kem+06] C. Kemp, J. Tenenbaum, T. Y. T. Griffiths and, and N. Ueda. "Learning systems of concepts with an infinite relational model". In: AAAI. 2006.

[KF05] H. Kuck and N. de Freitas. "Learning about individuals from group statistics". In: UAI. 2005.

[KG05] A. Krause and C. Guestrin. "Near-optimal value of information in graphical models". In: UAI. 2005.

[KG17] A. Kendall and Y. Gal. "What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?" In: NIPS. Curran Associates, Inc., 2017, pp. 5574–5584.

[KGS20] J. von Kügelgen, L. Gresele, and B. Schölkopf. "Simpson's paradox in Covid-19 case fatality rates: a mediation analysis of age-related causal effects". In: (2020). arXiv: 2005.07180 [stat.AP].

[KH09] A Krizhevsky and G Hinton. Learning multiple layers of features from tiny images. Tech. rep. U. Toronto, 2009.

[KH19] D. Krotov and J. J. Hopfield. "Unsupervised learning by competing hidden units". en. In: PNAS 116.16 (2019), pp. 7723–7731.

[Kha+10] M. E. Khan, B. Marlin, G. Bouchard, and K. P. Murphy. "Variational bounds for mixed-data factor analysis". In: NIPS. 2010.

[Kha+20] A. Khan, A. Sohail, U. Zahoora, and A. S. Qureshi. "A Survey of the Recent Architectures of Deep Convolutional Neural Networks". In: AI Review (2020).

[KHB07] A. Kapoor, E. Horvitz, and S. Basu. "Selective Supervision: Guiding Supervised Learning with Decision-Theoretic Active Learning". In: IJCAI. 2007.

[KHW19] W. Kool, H. van Hoof, and M. Welling. "Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement". In: ICML. 2019.

[Kim14] Y. Kim. "Convolutional Neural Networks for Sentence Classification". In: EMNLP. 2014.

[Kim19] D. H. Kim. Survey of Deep Metric Learning. 2019.

[Kin+14] D. P. Kingma, D. J. Rezende, S. Mohamed, and M. Welling. "Semi-Supervised Learning

---

with Deep Generative Models". In: NIPS. 2014.

[Kir+19] A. Kirillov, K. He, R. Girshick, C. Rother, and P. Dollár. "Panoptic Segmentation". In: CVPR. 2019.

[KJ16] L Kang and V Joseph. "Kernel Approximation: From Regression to Interpolation". In: SIAM/ASA J. Uncertainty Quantification 4.1 (2016), pp. 112–129.

[KJ95] J. Karhunen and J. Joutsensalo. "Generalizations of principal component analysis, optimization problems, and neural networks". In: Neural Networks 8.4 (1995), pp. 549–562.

[KJM19] N. M. Kriege, F. D. Johansson, and C. Morris. "A Survey on Graph Kernels". In: (2019). arXiv: 1903.11835 [cs.LG].

[KK06] S. Kotsiantis and D. Kanellopoulos. "Discretization Techniques: A recent survey". In: GESTS Intl. Trans. on Computer Science and Engineering 31.1 (2006), pp. 47–58.

[KKH20] I. Khemakhem, D. P. Kingma, and A. Hyvari-nen. "Variational Autoencoders and Nonlinear ICA: A Unifying Framework". In: AISTATS. 2020.

[KKL20] N. Kitaev, L. Kaiser, and A. Levskaya. "Reformer: The Efficient Transformer". In: 8th International Conference on Learning Representations, ICLR 2020, Addis Ababa, Ethiopia, April 26-30, 2020. OpenReview.net, 2020.

[KKS20] F. Kunstner, R. Kumar, and M. Schmidt. "Homeomorphic-Invariance of EM: Non-Asymptotic Convergence in KL Divergence for Exponential Families via Mirror Descent". In: (2020). arXiv: 2011.01170 [cs.LG].

[KL17] J. K. Kruschke and T. M. Liddell. "The Bayesian New Statistics: Hypothesis testing, estimation, meta-analysis, and power analysis from a Bayesian perspective". In: Psychon. Bull. Rev. (2017).

[KL21] W. M. Kouw and M. Loog. "A review of domain adaptation without target labels". en. In: IEEE PAMI (2021).

[Kla+17] G. Klambauer, T. Unterthiner, A. Mayr, and S. Hochreiter. "Self-Normalizing Neural Networks". In: NIPS. 2017.

[Kle02] J. Kleinberg. "An Impossibility Theorem for Clustering". In: NIPS. 2002.

[Kle+11] A. Kleiner, A. Talwalkar, P. Sarkar, and M. I. Jordan. A scalable bootstrap for massive data. Tech. rep. UC Berkeley, 2011.

[Kle13] P. N. Klein. Coding the Matrix: Linear Algebra through Applications to Computer Science. en. 1 edition. Newtonian Press, 2013.

[KLQ95] C. Ko, J. Lee, and M. Queyranne. "An exact algorithm for maximum entropy sampling". In: Operations Research 43 (1995), 684–691.

[Kok17] I. Kokkinos. "UberNet: Training a Universal Convolutional Neural Network for Low-, Mid-, and High-Level Vision Using Diverse Datasets and Limited Memory". In: CVPR. Vol. 2. 2017, p. 8.

[Kol+19] A. Kolesnikov, L. Beyer, X. Zhai, J. Puigcerver, J. Yung, S. Gelly, and N. Houlsby. "Large Scale Learning of General Visual Representations for Transfer". In: (2019). arXiv:1912.11370 [cs.CV].

[Kol+20] A. Kolesnikov, L. Beyer, X. Zhai, J. Puigcerver, J. Yung, S. Gelly, and N. Houlsby. "Large Scale Learning of General Visual Representations for Transfer". In: ECCV. 2020.

[Kon20] M. Konnikova. The Biggest Bluff: How I Learned to Pay Attention, Master Myself, and Win. en. Penguin Press, 2020.

[Kor09] Y. Koren. The BellKor Solution to the Netflix Grand Prize. Tech. rep. Yahoo! Research, 2009.

[KR19] M. Kearns and A. Roth. The Ethical Algorithm: The Science of Socially Aware Algorithm Design. en. Oxford University Press, 2019.

[KR87] L. Kaufman and P. Rousseeuw. "Clustering by means of Medoids". In: Statistical Data Analysis Based on the L1-norm and Related Methods. Ed. by Y. Dodge. North-Holland, 1987, 405–416.

[KR90] L. Kaufman and P. Rousseeuw. Finding Groups in Data: An Introduction to Cluster Analysis. Wiley, 1990.

[Kri+05] B. Krishnapuram, L. Carin, M. Figueiredo, and A. Hartemink. "Learning sparse Bayesian classifiers: multi-class formulation, fast algorithms, and generalization bounds". In: IEEE Transaction on Pattern Analysis and Machine Intelligence (2005).

[Kru13] J. K. Kruschke. “Bayesian estimation supersedes the t test”. In: J. Experimental Psychology: General 142.2 (2013), pp. 573–603.

[Kru15] J. Kruschke. Doing Bayesian Data Analysis: A Tutorial with R, JAGS and STAN. Second edition. Academic Press, 2015.

[KS15] H. Kaya and A. A. Salah. "Adaptive Mixtures of Factor Analyzers". In: (2015). arXiv: 1507.02801 [stat.ML].

[KSG04] A. Kraskov, H. Stögbauer, and P. Grassberger. "Estimating mutual information". en. In: Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 69.6 Pt 2 (2004), p. 066138.

[KSH12] A. Krizhevsky, I. Sutskever, and G. Hinton. "Imagenet classification with deep convolutional neural networks". In: NIPS. 2012.

[KSJ09] I. Konstas, V. Stathopoulos, and J. M. Jose. "On social networks and collaborative recommendation". In: Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval. 2009, pp. 195–202.

[KST82] D. Kahneman, P. Slovic, and A. Tversky, eds. Judgment under uncertainty: Heuristics and biases. Cambridge, 1982.

[KTB11] D. P. Kroese, T. Taimre, and Z. I. Botev. Handbook of Monte Carlo Methods. en. 1 edition. Wiley, 2011.

[Kua+09] P. Kuan, G. Pan, J. A. Thomson, R. Stewart, and S. Keles. A hierarchical semi-Markov model for detecting enrichment with applica-

---

tion to ChIP-Seq experiments. Tech. rep. U. Wisconsin, 2009.

[Kull13] B. Kulis. "Metric Learning: A Survey". In: Foundations and Trends in Machine Learning 5.4 (2013), pp. 287–364.

[KV94] M. J. Kearns and U. V. Vazirani. An Introduction to Computational Learning Theory. MIT Press, 1994.

[KVK10] A. Klami, S. Virtanen, and S. Kaski. "Bayesian exponential family projections for coupled data sources". In: UAI. 2010.

[KW14] D. P. Kingma and M. Welling. "Auto-encoding variational Bayes". In: ICLR. 2014.

[KW16a] T. N. Kipf and M. Welling. “Semi-supervised classification with graph convolutional networks”. In: arXiv preprint arXiv:1609.02907 (2016).

[KW16b] T. N. Kipf and M. Welling. "Variational graph auto-encoders". In: arXiv preprint arXiv:1611.07308 (2016).

[KW19a] D. P. Kingma and M. Welling. "An Introduction to Variational Autoencoders". In: Foundations and Trends in Machine Learning 12.4 (2019), pp. 307–392.

[KW19b] M. J. Kochenderfer and T. A. Wheeler. Algorithms for Optimization. en. The MIT Press, 2019.

[KWW22] M. J. Kochenderfer, T. A. Wheeler, and K. Wray. Algorithms for Decision Making. The MIT Press, 2022.

[Kyu+10] M. Kyung, J. Gill, M. Ghosh, and G. Casella. "Penalized Regression, Standard Errors and Bayesian Lassos". In: Bayesian Analysis 5.2 (2010), pp. 369–412.

[LA16] S. Laine and T. Aila. "Temporal ensembling for semi-supervised learning". In: arXiv preprint arXiv:1610.02242 (2016).

[Lak+17] B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. Gershman. "Building Machines That Learn and Think Like People". en. In: Behav. Brain Sci. (2017), pp. 1–101.

[Lam18] B. Lambert. A Student's Guide to Bayesian Statistics. en. 1st ed. SAGE Publications Ltd, 2018.

[Law12] N. D. Lawrence. "A Unifying Probabilistic Perspective for Spectral Dimensionality Reduction: Insights and New Models". In: JMLR 13.May (2012), pp. 1609–1638.

[LBM06] J. A. Lasserre, C. M. Bishop, and T. P. Minka. "Principled Hybrids of Generative and Discriminative Models". In: CVPR. Vol. 1. June 2006, pp. 87–94.

[LBS19] Y. Li, J. Bradshaw, and Y. Sharma. "Are Generative Classifiers More Robust to Adversarial Attacks?" In: ICML. Ed. by K. Chaudhuri and R. Salakhutdinov. Vol. 97. Proceedings of Machine Learning Research. PMLR, 2019, pp. 3804–3814.

[LeC18] Y. LeCun. Self-supervised learning: could machines learn like humans? 2018.

[LeC+98] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-Based Learning Applied to Document Recognition". In: Proceedings of the IEEE 86.11 (1998), pp. 2278–2324.

[Lee13] D.-H. Lee. "Pseudo-label: The simple and efficient semi-supervised learning method for deep neural networks". In: ICML Workshop on Challenges in Representation Learning. 2013.

[Lee+13] J. Lee, S. Kim, G. Lebanon, and Y. Singer. "Local Low-Rank Matrix Approximation". In: ICML. Vol. 28. Proceedings of Machine Learning Research. PMLR, 2013, pp. 82–90.

[Lee+19] J. Lee, Y. Lee, J. Kim, A. R. Kosiorek, S. Choi, and Y. W. Teh. "Set Transformer: A Framework for Attention-based Permutation-Invariant Neural Networks". In: ICML. 2019.

[Lee77] J. de Leeuw. "Applications of Convex Analysis to Multidimensional Scaling". In: Recent Developments in Statistics. Ed. by J. R. Barra, F Brodeau, G Romier, and B Van Cutsem. 1977.

[Lep+21] D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer, and Z. Chen. "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding". In: ICLR. 2021.

[LG14] O. Levy and Y. Goldberg. "Neural Word Embedding as Implicit Matrix Factorization". In: NIPS. 2014.

[LH17] I. Loshchilov and F. Hutter. "SGDR: Stochastic Gradient Descent with Warm Restarts". In: ICLR. 2017.

[Li+15] Y. Li, D. Tarlow, M. Brockschmidt, and R. Zemel. "Gated graph sequence neural networks". In: arXiv preprint arXiv:1511.05493 (2015).

[Li+17] A. Li, A. Jabri, A. Joulin, and L. van der Maaten. "Learning Visual N-Grams from Web Data". In: ICCV. 2017.

[Lia20] S. M. Liao, ed. Ethics of Artificial Intelligence. en. 1st ed. Oxford University Press, 2020.

[Lim+19] S. Lim, I. Kim, T. Kim, C. Kim, and S. Kim. "Fast AutoAugment". In: (2019). arXiv: 1905.00397 [cs.LG].

[Lin06] D. Lindley. Understanding Uncertainty. Wiley, 2006.

[Lin+21] T. Lin, Y. Wang, X. Liu, and X. Qiu. "A Survey of Transformers". In: (2021). arXiv:2106.04554 [cs.LG].

[Lin56] D. Lindley. "On a measure of the information provided by an experiment". In: The Annals of Math. Stat. (1956), 986–1005.

[Liu01] J. Liu. Monte Carlo Strategies in Scientific Computation. Springer, 2001.

[Liu+16] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, and S. Reed. "SSD: Single Shot MultiBox Detector". In: ECCV. 2016.

[Liu+18a] H. Liu, Y.-S. Ong, X. Shen, and J. Cai. "When Gaussian Process Meets Big Data: A Review of Scalable GPs". In: (2018). arXiv:1807.01065 [stat.ML].

---

[Liu+18b] L. Liu, X. Liu, C.-J. Hsieh, and D. Tao. "Stochastic Second-order Methods for Non-convex Optimization with Inexact Hessian and Gradient". In: (2018). arXiv: 1809.09853 [math.OC].

[Liu+20] F. Liu, X. Huang, Y. Chen, and J. A. K. Suykens. "Random Features for Kernel Approximation: A Survey on Algorithms, Theory, and Beyond". In: (2020). arXiv: 2004.11154 [stat.ML].

[Liu+22] Z. Liu, H. Mao, C.-Y. Wu, C. Feichtenhofer, T. Darrell, and S. Xie. "A ConvNet for the 2020s". In: (2022). arXiv: 2201.03545 [cs.CV].

[LJ09] H. Lukosevicius and H. Jaeger. "Reservoir computing approaches to recurrent neural network training". In: Computer Science Review 3.3 (2009), 127–149.

[LKB20] Q. Liu, M. J. Kusner, and P. Blunsom. "A Survey on Contextual Embeddings". In: (2020). arXiv: 2003.07278 [cs.CL].

[LLM14] D. Lay, S. Lay, and J. McDonald. Linear algebra and its applications. Pearson, 2014.

[LLT89] K. Lange, R. Little, and J. Taylor. "Robust Statistical Modeling Using the T Distribution". In: JASA 84.408 (1989), pp. 881–896.

[Llo82] S Lloyd. "Least squares quantization in PCM". In: IEEE Trans. Inf. Theory 28.2 (1982), pp. 129–137.

[LM04] E. Learned-Miller. Hyperspacings and the estimation of information theoretic quantities. Tech. rep. 04-104. U. Mass. Amherst Comp. Sci. Dept, 2004.

[LM86] R. Larsen and M. Marx. An introduction to mathematical statistics and its applications. Prentice Hall, 1986.

[LN81] D. V. Lindley and M. R. Novick. "The Role of Exchangeability in Inference". en. In: Annals of Statistics 9.1 (1981), pp. 45–58.

[LNK19] Q. Liu, M. Nickel, and D. Kiela. "Hyperbolic graph neural networks". In: Advances in Neural Information Processing Systems. 2019, pp. 8228–8239.

[Loa00] C. F. V. Loan. "The ubiquitous Kronecker product". In: J. Comput. Appl. Math. 123.1 (2000), pp. 85–100.

[Lod+02] H. Lodhi, C. Saunders, J. Shawe-Taylor, N. Cristianini, and C. Watkins. "Text classification using string kernels". en. In: J. Mach. Learn. Res. (2002).

[LPM15] M.-T. Luong, H. Pham, and C. D. Manning. "Effective Approaches to Attention-based Neural Machine Translation". In: EMNLP. 2015.

[LR87] R. J. Little and D. B. Rubin. Statistical Analysis with Missing Data. Wiley and Son, 1987.

[LRU14] J. Leskovec, A. Rajaraman, and J. Ullman. Mining of massive datasets. Cambridge, 2014.

[LS10] P. Long and R. Servedio. “Random classification noise beats all convex potential boosters”. In: JMLR 78.3 (2010), pp. 287–304.

[LS19a] S. Lattanzi and C. Sohler. "A Better k-means++ Algorithm via Local Search". In: ICML. Vol. 97. Proceedings of Machine Learning Research. PMLR, 2019, pp. 3662–3671.

[LS19b] Z. C. Lipton and J. Steinhardt. "Troubling Trends in Machine Learning Scholarship: Some ML papers suffer from flaws that could mislead the public and stymie future research". In: The Queue 17.1 (2019), pp. 45–77.

[LSS13] Q. Le, T. Sarlos, and A. Smola. "Fastfood - Computing Hilbert Space Expansions in log-linear time". In: ICML. Vol. 28. Proceedings of Machine Learning Research. PMLR, 2013, pp. 244–252.

[LSY19] H. Liu, K. Simonyan, and Y. Yang. "DARTS: Differentiable Architecture Search". In: ICLR. 2019.

[Lu+19] L. Lu, Y. Shin, Y. Su, and G. E. Karniadakis. "Dying ReLU and Initialization: Theory and Numerical Examples". In: (2019). arXiv: 1903.06733 [stat.ML].

[Luo16] M.-T. Luong. "Neural machine translation". PhD thesis. Stanford Dept. Comp. Sci., 2016.

[Luo+19] P. Luo, X. Wang, W. Shao, and Z. Peng. "Towards Understanding Regularization in Batch Normalization". In: ICLR. 2019.

[LUW17] C. Louizos, K. Ullrich, and M. Welling. "Bayesian Compression for Deep Learning". In: NIPS. 2017.

[Lux07] U. von Luxburg. "A tutorial on spectral clustering". In: Statistics and Computing 17.4 (2007), pp. 395–416.

[LW04a] O. Ledoit and M. Wolf. "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices". In: J. of Multivariate Analysis 88.2 (2004), pp. 365–411.

[LW04b] O. Ledoit and M. Wolf. "Honey, I Shrunk the Sample Covariance Matrix". In: J. of Portfolio Management 31.1 (2004).

[LW04c] H. Lopes and M. West. "Bayesian model assessment in factor analysis". In: Statisica Sinica 14 (2004), pp. 41–67.

[LW16] C. Li and M. Wand. "Precomputed Real-Time Texture Synthesis with Markovian Generative Adversarial Networks". In: ECCV. 2016.

[LWG12] U. von Luxburg, R. Williamson, and I. Guyon. "Clustering: science or art?" In: Workshop on Unsupervised and Transfer Learning. 2012.

[LXW19] X. Liu, Q. Xu, and N. Wang. "A survey on deep neural network-based image captioning". In: The Visual Computer 35.3 (2019), pp. 445–470.

[Lyu+20] X.-K. Lyu, Y. Xu, X.-F. Zhao, X.-N. Zuo, and C.-P. Hu. "Beyond psychology: prevalence of p value and confidence interval misinterpretation across different fields". In: Journal of Pacific Rim Psychology 14 (2020).

[MA10] I. Murray and R. P. Adams. "Slice sampling covariance hyperparameters of latent Gaussian models". In: NIPS. 2010, pp. 1732–1740.

[MA+17] Y. Movshovitz-Attias, A. Toshev, T. K. Leung, S. Ioffe, and S. Singh. "No Fuss Distance

---

Metric Learning using Proxies". In: ICCV. 2017.

[Maa+11] A. L. Maas, R. E. Daly, P. T. Pham, D. Huang, A. Y. Ng, and C. Potts. "Learning Word Vectors for Sentiment Analysis". In: Proc. ACL. 2011, pp. 142–150.

[Maa14] L. van der Maaten. "Accelerating t-SNE using Tree-Based Algorithms". In: JMLR (2014).

[Mac03] D. MacKay. Information Theory, Inference, and Learning Algorithms. Cambridge University Press, 2003.

[Mac09] L. W. Mackey. "Deflation Methods for Sparse PCA". In: NIPS. 2009.

[Mac67] J MacQueen. “Some methods for classification and analysis of multivariate observations”. en. In: Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Statistics. The Regents of the University of California, 1967.

[Mac95] D. MacKay. “Probable networks and plausible predictions — a review of practical Bayesian methods for supervised neural networks”. In: Network: Computation in Neural Systems 6.3 (1995), pp. 469–505.

[Mad+20] A. Madani, B. McCann, N. Naik, N. S. Keskar, N. Anand, R. R. Eguchi, P.-S. Huang, and R. Socher. "ProGen: Language Modeling for Protein Generation". en. 2020.

[Mah07] R. P. S. Mahler. Statistical Multisource-Multitarget Information Fusion. Artech House, Inc., 2007.

[Mah13] R Mahler. “Statistics 102 for Multisource-Multitarget Detection and Tracking”. In: IEEE J. Sel. Top. Signal Process. 7.3 (2013), pp. 376–389.

[Mah+18] D. Mahajan, R. Girshick, V. Ramanathan, K. He, M. Paluri, Y. Li, A. Bharambe, and L. van der Maaten. "Exploring the Limits of Weakly Supervised Pretraining". In: (2018). arXiv: 1805.00932 [cs.CV].

[Mah+23] K. Mahowald, A. A. Ivanova, I. A. Blank, N. Kanwisher, J. B. Tenenbaum, and E. Fedorenko. "Dissociating language and thought in large language models: a cognitive perspective". In: (Jan. 2023). arXiv: 2301.06627 [cs.CL].

[Mail5] J Mairal. "Incremental Majorization-Minimization Optimization with Application to Large-Scale Machine Learning". In: SIAM J. Optim. 25.2 (2015), pp. 829–855.

[Mak+19] D. Makowski, M. S. Ben-Shachar, S. H. A. Chen, and D. Lüdecke. "Indices of Effect Existence and Significance in the Bayesian Framework". en. In: Front. Psychol. 10 (2019), p. 2767.

[Mal99] S. Mallat. A Wavelet Tour of Signal Processing. Academic Press, 1999.

[Man+16] V. Mansinghka, P. Shafto, E. Jonas, C. Petschulat, M. Gasner, and J. Tenenbaum. "Crosscat: A Fully Bayesian, Nonparametric Method For Analyzing Heterogeneous, High-dimensional Data." In: JMLR 17 (2016).

[Mar06] H. Markram. "The blue brain project". en. In: Nat. Rev. Neurosci. 7.2 (2006), pp. 153–160.

[Mar08] B. Marlin. "Missing Data Problems in Machine Learning". PhD thesis. U. Toronto, 2008.

[Mar+11] B. M. Marlin, R. S. Zemel, S. T. Roweis, and M. Slaney. "Recommender Systems, Missing Data and Statistical Model Estimation". In: IJCAI. 2011.

[Mar18] O. Martin. Bayesian analysis with Python. Packt, 2018.

[Mar20] G. Marcus. "The Next Decade in AI: Four Steps Towards Robust Artificial Intelligence". In: (2020). arXiv: 2002.06177 [cs.AI].

[Mar72] G. Marsaglia. "Choosing a Point from the Surface of a Sphere". en. In: Ann. Math. Stat. 43.2 (1972), pp. 645–646.

[Mas+00] L. Mason, J. Baxter, P. L. Bartlett, and M. R. Frean. "Boosting Algorithms as Gradient Descent". In: NIPS. 2000, pp. 512–518.

[Mas+15] J. Masci, D. Boscaini, M. Bronstein, and P. Vandergheynst. "Geodesic convolutional neural networks on riemannian manifolds". In: Proceedings of the IEEE international conference on computer vision workshops. 2015, pp. 37–45.

[Mat00] R. Matthews. “Storks Deliver Babies (p = 0.008). In: Teach. Stat. 22.2 (2000), pp. 36–38.

[Mat98] R. Matthews. Bayesian Critique of Statistics in Health: The Great Health Hoax. 1998.

[MAV17] D. Molchanov, A. Ashukha, and D. Vetrov. "Variational Dropout Sparsifies Deep Neural Networks". In: ICML. 2017.

[MB05] F. Morin and Y. Bengio. "Hierarchical Probabilistic Neural Network Language Model". In: AISTATS. 2005.

[MB06] N. Meinshausen and P. Buhlmann. "High dimensional graphs and variable selection with the lasso". In: The Annals of Statistics 34 (2006), pp. 1436–1462.

[MBL20] K. Musgrave, S. Belongie, and S.-N. Lim. "A Metric Learning Reality Check". In: ECCV. 2020.

[McE20] R. McElreath. Statistical Rethinking: A Bayesian Course with Examples in R and Stan (2nd edition). en. Chapman and Hall/CRC, 2020.

[McL75] G. J. McLachlan. “Iterative reclassification procedure for constructing an asymptotically optimal rule of allocation in discriminant analysis”. In: Journal of the American Statistical Association 70.350 (1975), pp. 365–369.

[MD97] X. L. Meng and D. van Dyk. “The EM algorithm — an old folk song sung to a fast new tune (with Discussion)”. In: J. Royal Stat. Soc. B 59 (1997), pp. 511–567.

[ME14] S. Masoudnia and R. Ebrahimpour. "Mixture of experts: a literature survey". In: Artificial Intelligence Review 42.2 (2014), pp. 275–293.

[Mei01] M. Meila. "A random walks view of spectral segmentation". In: AISTATS. 2001.

[Mei05] M. Meila. "Comparing clusterings: an axiomatic view". In: ICML. 2005.

---

[Men+12] T. Mensink, J. Verbeek, F. Perronnin, and G. Csurka. "Metric Learning for Large Scale Image Classification: Generalizing to New Classes at Near-Zero Cost". In: ECCV. Springer Berlin Heidelberg, 2012, pp. 488–501.

[Men+21] A. K. Menon, S. Jayasumana, A. S. Rawat, H. Jain, A. Veit, and S. Kumar. "Long-tail learning via logit adjustment". In: ICLR. 2021.

[Men+22] K. Meng, D. Bau, A. Andonian, and Y. Belinkov. "Locating and Editing Factual Associations in GPT". In: (Feb. 2022). arXiv: 2202.05262 [cs.CL].

[Met21] C. Metz. Genius Makers: The Mavericks Who Brought AI to Google, Facebook, and the World. en. Dutton, 2021.

[MF17] J. Matejka and G. Fitzmaurice. "Same Stats, Different Graphs: Generating Datasets with Varied Appearance and Identical Statistics through Simulated Annealing". In: Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems. Association for Computing Machinery, 2017, pp. 1290–1294.

[MFR20] G. M. Martin, D. T. Frazier, and C. P. Robert. "Computing Bayes: Bayesian Computation from 1763 to the 21st Century". In: (2020). arXiv: 2004.06425 [stat.CO].

[MG05] I. Murray and Z. Ghahramani. A note on the evidence and Bayesian Occam's razor. Tech. rep. Gatsby, 2005.

[MH07] A. Mnih and G. Hinton. "Three new graphical models for statistical language modelling". en. In: ICML. 2007.

[MH08] L. v. d. Maaten and G. Hinton. "Visualizing Data using t-SNE". In: JMLR 9.Nov (2008), pp. 2579–2605.

[MHM18] L. McInnes, J. Healy, and J. Melville. "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction". In: (2018). arXiv: 1802.03426 [stat.ML].

[MHN13] A. L. Maas, A. Y. Hannun, and A. Y. Ng. "Rectifier Nonlinearities Improve Neural Network Acoustic Models". In: ICML. Vol. 28. 2013.

[Mik+13a] T. Mikolov, K. Chen, G. Corrado, and J. Dean. "Efficient Estimation of Word Representations in Vector Space". In: ICLR. 2013.

[Mik+13b] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, and J. Dean. “Distributed Representations of Words and Phrases and their Compositionality”. In: NIPS. 2013.

[Mik+13c] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean. “Distributed representations of words and phrases and their compositionality”. In: NIPS. 2013, pp. 3111–3119.

[Min00] T. Minka. Bayesian model averaging is not model combination. Tech. rep. MIT Media Lab, 2000.

[Min+09] M. Mintz, S. Bills, R. Snow, and D. Jurafsky. "Distant supervision for relation extraction without labeled data". In: Prof. Conf. Recent Advances in NLP. 2009.

[Mit97] T. Mitchell. Machine Learning. McGraw Hill, 1997.

[Miy+18] T. Miyato, S.-I. Maeda, M. Koyama, and S. Ishii. "Virtual Adversarial Training: A Regularization Method for Supervised and Semi-Supervised Learning". In: IEEE PAMI (2018).

[MK97] G. J. McLachlan and T. Krishnan. The EM Algorithm and Extensions. Wiley, 1997.

[MKH19] R. Müller, S. Kornblith, and G. E. Hinton. "When does label smoothing help?" In: NIPS. 2019, pp. 4694–4703.

[MKL11] O. Martin, R. Kumar, and J. Lao. Bayesian Modeling and Computation in Python. CRC Press, 2011.

[MKL21] O. A. Martin, R. Kumar, and J. Lao. Bayesian Modeling and Computation in Python. CRC Press, 2021.

[MKS21] K. Murphy, A. Kumar, and S. Serghiou. "Risk score learning for COVID-19 contact tracing apps". In: Machine Learning for Healthcare. 2021.

[MM16] D. Mishkin and J. Matas. "All you need is a good init". In: ICLR. 2016.

[MN89] P. McCullagh and J. Nelder. Generalized linear models. 2nd edition. Chapman and Hall, 1989.

[MNM02] W. Maass, T. Natschlaeger, and H. Markram. "Real-time computing without stable states: A new framework for neural computation based on perturbations". In: Neural Computation 14.11 (2002), 2531—2560.

[MO04] S. C. Madeira and A. L. Oliveira. “Biclustering Algorithms for Biological Data Analysis: A Survey”. In: IEEE/ACM Transactions on Computational Biology and Bioinformatics 1.1 (2004), pp. 24–45.

[Mol04] C. Moler. Numerical Computing with MATLAB. SIAM, 2004.

[Mon+14] G. F. Montufar, R. Pascanu, K. Cho, and Y. Bengio. "On the Number of Linear Regions of Deep Neural Networks". In: NIPS. 2014.

[Mon+17] F. Monti, D. Boscaini, J. Masci, E. Rodola, J. Svoboda, and M. M. Bronstein. "Geometric deep learning on graphs and manifolds using mixture model cnns". In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2017, pp. 5115–5124.

[Mon+19] N. Monath, A. Kobren, A. Krishnamurthy, M. R. Glass, and A. McCallum. "Scalable Hierarchical Clustering with Tree Grafting". In: KDD. KDD '19. Association for Computing Machinery, 2019, pp. 1438–1448.

[Mon+21] N. Monath et al. "Scalable Bottom-Up Hierarchical Clustering". In: KDD. 2021.

[Mor+16] R. D. Morey, R. Hoekstra, J. N. Rouder, M. D. Lee, and E.-J. Wagenmakers. "The fallacy of placing confidence in confidence intervals". en. In: Psychon. Bull. Rev. 23.1 (2016), pp. 103–123.

[MOT15] A. Mordvintsev, C. Olah, and M. Tyka. Inceptionism: Going Deeper into Neural Networks. https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html. Accessed: NĂ-NĂ-NĂ. 2015.

---

[MP43] W. McCulloch and W. Pitts. "A logical calculus of the ideas immanent in nervous activity". In: Bulletin of Mathematical Biophysics 5 (1943), pp. 115–137.

[MP69] M. Minsky and S. Papert. Perceptrons. MIT Press, 1969.

[MRS08] C. Manning, P. Raghavan, and H. Schuetze. Introduction to Information Retrieval. Cambridge University Press, 2008.

[MS11] D. Mayo and A. Spanos. "Error Statistics". In: Handbook of Philosophy of Science. Ed. by P. S. Bandyopadhyay and M. R. Forster. 2011.

[Muk+19] B. Mukhoty, G. Gopakumar, P. Jain, and P. Kar. "Globally-convergent Iteratively Reweighted Least Squares for Robust Regression Problems". In: AISTATS. 2019, pp. 313–322.

[Mur23] K. P. Murphy. Probabilistic Machine Learning: Advanced Topics. MIT Press, 2023.

[MV15] A Mahendran and A Vedaldi. "Understanding deep image representations by inverting them". In: CVPR. 2015, pp. 5188–5196.

[MV16] A. Mahendran and A. Vedaldi. "Visualizing Deep Convolutional Neural Networks Using Natural Pre-images". In: Intl. J. Computer Vision (2016), pp. 1–23.

[MWK16] A. H. Marblestone, G. Wayne, and K. P. Kording. "Toward an Integration of Deep Learning and Neuroscience". en. In: Front. Comput. Neurosci. 10 (2016), p. 94.

[MWP98] B Moghaddam, W Wahid, and A Pentland. "Beyond eigenfaces: probabilistic matching for face recognition". In: Proceedings Third IEEE International Conference on Automatic Face and Gesture Recognition. 1998, pp. 30–35.

[Nad+19] S. Naderi, K. He, R. Aghajani, S. Sclaroff, and P. Felzenszwalb. "Generalized Majorization-Minimization". In: ICML. 2019.

[Nak+19] P. Nakkiran, G. Kaplun, Y. Bansal, T. Yang, B. Barak, and I. Sutskever. "Deep Double Descent: Where Bigger Models and More Data Hurt". In: (2019). arXiv: 1912.02292 [cs.LG].

[NAM21] C. G. Northcutt, A. Athalye, and J. Mueller. "Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks". In: NeurIPS Track on Datasets and Benchmarks. Mar. 2021.

[Nar+23] H. Narasimhan, A. K. Menon, W. Jitkritum, and S. Kumar. "Plugin estimators for selective classification with out-of-distribution detection". In: arXiv [cs.LG] (Jan. 2023).

[Nea96] R. Neal. Bayesian learning for neural networks. Springer, 1996.

[Nes04] Y. Nesterov. Introductory Lectures on Converx Optimization. A basic course. Kluwer, 2004.

[Neu04] A. Neumaier. "Complete search in continuous global optimization and constraint satisfaction". In: Acta Numer. 13 (2004), pp. 271–369.

[Neu17] G. Neubig. "Neural Machine Translation and Sequence-to-sequence Models: A Tutorial". In: (2017). arXiv: 1703.01619 [cs.CL].

[Ngu+17] A. Nguyen, J. Yosinski, Y. Bengio, A. Dosovitskiy, and J. Clune. "Plug & Play Generative Networks: Conditional Iterative Generation of Images in Latent Space". In: CVPR. 2017.

[NH98] R. M. Neal and G. E. Hinton. "A View of the EM Algorithm that Justifies Incremental, Sparse, and other Variants". In: Learning in Graphical Models. Ed. by M. I. Jordan. Springer Netherlands, 1998, pp. 355–368.

[NHLs19] E. Nalisnick, J. M. Hernández-Lobato, and P. Smyth. "Dropout as a Structured Shrinkage Prior". In: ICML. 2019.

[Nic+15] M. Nickel, K. Murphy, V. Tresp, and E. Gabrilovich. "A Review of Relational Machine Learning for Knowledge Graphs". In: Proc. IEEE (2015).

[Niu+11] F. Niu, B. Recht, C. Re, and S. J. Wright. "HOGWILD!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent". In: NIPS. 2011.

[NJ02] A. Y. Ng and M. I. Jordan. "On Discriminative vs. Generative Classifiers: A comparison of logistic regression and Naive Bayes". In: NIPS-14. 2002.

[NJW01] A. Ng, M. Jordan, and Y. Weiss. "On Spectral Clustering: Analysis and an algorithm". In: NIPS. 2001.

[NK17] M. Nickel and D. Kiela. "Poincaré embeddings for learning hierarchical representations". In: Advances in neural information processing systems. 2017, pp. 6338–6347.

[NK18] M. Nickel and D. Kiela. "Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry". In: International Conference on Machine Learning. 2018, pp. 3779–3788.

[NK19] T. Niven and H.-Y. Kao. "Probing Neural Network Comprehension of Natural Language Arguments". In: Proc. ACL. 2019.

[NMC05] A. Niculescu-Mizil and R. Caruana. "Predicting Good Probabilities with Supervised Learning". In: ICML. 2005.

[Nou+02] M. N. Nounou, B. R. Bakshi, P. K. Goel, and X. Shen. "Process modeling by Bayesian latent variable regression". In: Am. Inst. Chemical Engineers Journal 48.8 (2002), pp. 1775–1793.

[Nov62] A. Novikoff. "On convergence proofs on perceptrons". In: Symp. on the Mathematical Theory of Automata 12 (1962), pp. 615–622.

[NR18] G. Neu and L. Rosasco. "Iterate Averaging as Regularization for Stochastic Gradient Descent". In: COLT. 2018.

[NTL20] J. Nixon, D. Tran, and B. Lakshminarayanan. "Why aren't bootstrapped neural networks better?" In: NIPS Workshop on "I can't believe it's not better". 2020.

[NW06] J. Nocedal and S. Wright. Numerical Optimization. Springer, 2006.

[Ode16] A. Odena. “Semi-supervised learning with generative adversarial networks”. In: arXiv preprint arXiv:1606.01583 (2016).

[OLV18] A. van den Oord, Y. Li, and O. Vinyals. "Representation Learning with Contrastive Predic-

---

tive Coding". In: (2018). arXiv: 1807.03748 [cs.LG].

[OMS17] C. Olah, A. Mordvintsev, and L. Schubert. "Feature Visualization". In: Distill (2017).

[Oor+16] A. Van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu. "WaveNet: A Generative Model for Raw Audio". In: (2016). arXiv: 1609.03499 [cs.SD].

[Oor+18] A. van den Oord et al. "Parallel WaveNet: Fast High-Fidelity Speech Synthesis". In: ICML. Ed. by J. Dy and A. Krause. Vol. 80. Proceedings of Machine Learning Research. PMLR, 2018, pp. 3918–3926.

[Ope] OpenAI. ChatGPT: Optimizing Language Models for Dialogue. Blog.

[Ope23] OpenAI. GPT4. Tech. rep. 2023.

[OPK12] G. Ohloff, W. Pickenhagen, and P. Kraft. Scent and Chemistry. en. Wiley, 2012.

[OPT00a] M. R. Osborne, B. Presnell, and B. A. Turlach. "A new approach to variable selection in least squares problems". In: IMA Journal of Numerical Analysis 20.3 (2000), pp. 389–403.

[OPT00b] M. R. Osborne, B. Presnell, and B. A. Turlach. "On the lasso and its dual". In: J. Computational and graphical statistics 9 (2000), pp. 319–337.

[Ort+19] P. A. Ortega et al. "Meta-learning of Sequential Strategies". In: (2019). arXiv: 1905.03030 [cs.LG].

[Osb16] I. Osband. "Risk versus Uncertainty in Deep Learning: Bayes, Bootstrap and the Dangers of Dropout". In: NIPS workshop on Bayesian deep learning. 2016.

[OTJ07] G. Obozinski, B. Taskar, and M. I. Jordan. Joint covariate selection for grouped classification. Tech. rep. UC Berkeley, 2007.

[Ouy+22] L. Ouyang et al. "Training language models to follow instructions with human feedback". In: (Mar. 2022). arXiv: 2203.02155 [cs.CL].

[Pai05] A. Pais. Subtle Is the Lord: The Science and the Life of Albert Einstein. en. Oxford University Press, 2005.

[Pan+15] V. Panayotov, G. Chen, D. Povey, and S. Khudanpur. "Librispeech: an asr corpus based on public domain audio books". In: ICASSP. IEEE. 2015, pp. 5206–5210.

[Pap+18] G. Papandreou, T. Zhu, L.-C. Chen, S. Gidaris, J. Tompson, and K. Murphy. "Person-Lab: Person Pose Estimation and Instance Segmentation with a Bottom-Up, Part-Based, Geometric Embedding Model". In: ECCV. 2018, pp. 269–286.

[Par+16a] A. Parikh, O. Täckström, D. Das, and J. Uszkoreit. "A Decomposable Attention Model for Natural Language Inference". In: EMNLP. Association for Computational Linguistics, 2016, pp. 2249–2255.

[Par+16b] A. Parikh, O. Täckström, D. Das, and J. Uszkoreit. "A Decomposable Attention Model for Natural Language Inference". In: EMNLP.

Association for Computational Linguistics, 2016, pp. 2249–2255.

[Par+18] N. Parmar, A. Vaswani, J. Uszkoreit, L. Kaiser, N. Shazeer, A. Ku, and D. Tran. "Image Transformer". In: ICLR. 2018.

[Pas14] R. Pascanu. "On Recurrent and Deep Neural Networks". PhD thesis. U. Montreal, 2014.

[PARS14] B. Perozzi, R. Al-Rfou, and S. Skiena. "Deepwalk: Online learning of social representations". In: Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM. 2014, pp. 701–710.

[Pat12] A. Paterek. Predicting movie ratings and recommender systems. 2012.

[Pat+16] D. Pathak, P. Krahenbuhl, J. Donahue, T. Darrell, and A. A. Efros. "Context Encoders: Feature Learning by Inpainting". In: CVPR. 2016.

[Pau+20] A. Paullada, I. D. Raji, E. M. Bender, E. Denton, and A. Hanna. "Data and its (dis)contents: A survey of dataset development and use in machine learning research". In: NeurIPS 2020 Workshop: ML Retrospectives, Surveys & Meta-analyses (ML-RSA). 2020.

[PB+14] N. Parikh, S. Boyd, et al. “Proximal algorithms”. In: Foundations and Trends in Optimization 1.3 (2014), pp. 127–239.

[Pea18] J. Pearl. Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution. Tech. rep. UCLA, 2018.

[Pen+20] Z. Peng, W. Huang, M. Luo, Q. Zheng, Y. Rong, T. Xu, and J. Huang. "Graph Representation Learning via Graphical Mutual Information Maximization". In: Proceedings of The Web Conference. 2020.

[Per+17] B. Perozzi, V. Kulkarni, H. Chen, and S. Skiena. "Don't Walk, Skip! Online Learning of Multi-Scale Network Embeddings". In: Proceedings of the 2017 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining 2017. ASONAM'17. Association for Computing Machinery, 2017, 258–265.

[Pet13] J. Peters. When Ice Cream Sales Rise, So Do Homicides. Coincidence, or Will Your Next Cone Murder You? https://slate.com/news-and-politics/2013/07/warm-weather-homicide-rates-when-ice-cream-sales-rise-homicides-rise-coincidence.html. Accessed: 2020-5-20. 2013.

[Pet+18] M. E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee, and L. Zettlemoyer. "Deep contextualized word representations". In: NAACL. 2018.

[Pey20] G. Peyre. "Course notes on Optimization for Machine Learning". 2020.

[PH18] T. Parr and J. Howard. "The Matrix Calculus You Need For Deep Learning". In: (2018). arXiv: 1802.01528 [cs.LG].

[Pin88] F. J. Pineda. “Generalization of back propagation to recurrent and higher order neural networks”. In: Neural information processing systems. 1988, pp. 602–611.