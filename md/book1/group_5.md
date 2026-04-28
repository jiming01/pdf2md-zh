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

#### 6.3.6 Normalized mutual information

For some applications, it is useful to have a normalized measure of dependence, between 0 and 1. We now discuss one way to construct such a measure.

First, note that

$$
\begin{aligned}\mathbb{I}\left(X;Y\right)&=\mathbb{H}\left(X\right)-\mathbb{H}\left(X|Y\right)\leq\mathbb{H}\left(X\right)\\&=\mathbb{H}\left(Y\right)-\mathbb{H}\left(Y|X\right)\leq\mathbb{H}\left(Y\right)\end{aligned}   \tag*{(6.71)}
$$

SO

$$
0\leq\mathbb{I}\left(X;Y\right)\leq\min\left(\mathbb{H}\left(X\right),\mathbb{H}\left(Y\right)\right)   \tag*{(6.73)}
$$

Therefore we can define the normalized mutual information as follows:

$$
NMI(X,Y)=\frac{\mathbb{I}\left(X;Y\right)}{\min\left(\mathbb{H}\left(X\right),\mathbb{H}\left(Y\right)\right)}\leq1   \tag*{(6.74)}
$$

This normalized mutual information ranges from 0 to 1. When  $NMI(X,Y) = 0$, we have  $\mathbb{I}(X;Y) = 0$, so X and Y are independent. When  $NMI(X,Y) = 1$, and  $\mathbb{H}(X) < \mathbb{H}(Y)$, we have

$$
\mathbb{I}\left(X;Y\right)=\mathbb{H}\left(X\right)-\mathbb{H}\left(X|Y\right)=\mathbb{H}\left(X\right)\Longrightarrow\mathbb{H}\left(X|Y\right)=0   \tag*{(6.75)}
$$

and so X is a deterministic function of Y. For example, suppose X is a discrete random variable with pmf [0.5, 0.25, 0.25]. We have  $MI(X, X) = 1.5$ (using log base 2), and  $H(X) = 1.5$, so the normalized MI is 1, as is to be expected.

For continuous random variables, it is harder to normalize the mutual information, because of the need to estimate the differential entropy, which is sensitive to the level of quantization. See Section 6.3.7 for further discussion.

#### 6.3.7 Maximal information coefficient

As we discussed in Section 6.3.6, it is useful to have a normalized estimate of the mutual information, but this can be tricky to compute for real-valued data. One approach, known as the maximal information coefficient (MIC) [Res+11], is to define the following quantity:

$$
\mathrm{MIC}(X,Y)=\max_{G}\frac{\mathbb{I}((X,Y)|_{G})}{\log\left|\left|G\right|\right|}   \tag*{(6.76)}
$$

where $G$is the set of 2d grids, and$(X,Y)|_G$represents a discretization of the variables onto this grid, and$|G|$is$\min(G_x,G_y)$, where $G_x$is the number of grid cells in the$x$direction, and$G_y$is the number of grid cells in the$y$direction. (The maximum grid resolution depends on the sample size$n$; they suggest restricting grids so that $G_xG_y \leq B(n)$, where $B(n) = n^\alpha$, where $\alpha = 0.6$.) The denominator is the entropy of a uniform joint distribution; dividing by this ensures $0 \leq \text{MIC} \leq 1$.

The intuition behind this statistic is the following: if there is a relationship between X and Y, then there should be some discrete gridding of the 2d input space that captures this. Since we don't know the correct grid to use, MIC searches over different grid resolutions (e.g.,  $2 \times 2$,  $2 \times 3$, etc), as well as over locations of the grid boundaries. Given a grid, it is easy to quantize the data and compute

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_165_139_747_359.jpg" alt="Image" width="50%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_792_167_1014_351.jpg" alt="Image" width="19%" /></div>

<div style="text-align: center;">Figure 6.5: Illustration of how the maximal information coefficient (MIC) is computed. (a) We search over different grid resolutions, and grid cell locations, and compute the MI for each. (b) For each grid resolution  $(k, l)$, we define set  $M(k, l)$ to be the maximum MI for any grid of that size, normalized by  $\log(\min(k, l))$. (c) We visualize the matrix M. The maximum entry (denoted by a star) is defined to be the MIC. From Figure 1 of [Res+11]. Used with kind permission of David Reshef.</div>

MI. We define the characteristic matrix  $M(k,l)$ to be the maximum MI achievable by any grid of size  $(k,l)$, normalized by  $\log(\min(k,l))$. The MIC is then the maximum entry in this matrix,  $\max_{kl \leq B(n)} M(k,l)$. See Figure 6.5 for a visualization of this process.

In [Res+11], they show that this quantity exhibits a property known as \textit{equitability}, which means that it gives similar scores to equally noisy relationships, regardless of the type of relationship (e.g., linear, non-linear, non-functional).

In [Res+16], they present an improved estimator, called MICE, which is more efficient to compute, and only requires optimizing over 1d grids, which can be done in  $O(n)$ time using dynamic programming. They also present another quantity, called TICe (total information content), that has higher power to detect relationships from small sample sizes, but lower equitability. This is defined to be  $\sum_{k \leq B(n)} M(k, l)$. They recommend using TICe to screen a large number of candidate relationships, and then using MICE to quantify the strength of the relationship. For an efficient implementation of both of these metrics, see [Alb+18].

We can interpret MIC of 0 to mean there is no relationship between the variables, and 1 to represent a noise-free relationship of any form. This is illustrated in Figure 6.6. Unlike correlation coefficients, MIC is not restricted to finding linear relationships. For this reason, the MIC has been called “a correlation for the 21st century” [Spe11].

In Figure 6.7, we give a more interesting example, from [Res+11]. The data consists of 357 variables measuring a variety of social, economic, health and political indicators, collected by the World Health Organization (WHO). On the left of the figure, we see the correlation coefficient (CC) plotted against the MIC for all 63,546 variable pairs. On the right of the figure, we see scatter plots for particular pairs of variables, which we now discuss:

- The point marked C (near 0,0 on the plot) has a low CC and a low MIC. The corresponding scatter plot makes it clear that there is no relationship between these two variables (percentage of lives lost to injury and density of dentists in the population).

• The points marked D and H have high CC (in absolute value) and high MIC, because they

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_281_119_882_403.jpg" alt="Image" width="52%" /></div>

<div style="text-align: center;">Figure 6.6: Plots of some 2d distributions and the corresponding estimate of correlation coefficient  $R^{2}$ and the maximal information coefficient (MIC). Compare to Figure 3.1. Generated by MIC_correlation_2d.ipynb.</div>

represent nearly linear relationships.

- The points marked E, F, and G have low CC but high MIC. This is because they correspond to non-linear (and sometimes, as in the case of E and F, non-functional, i.e., one-to-many) relationships between the variables.

#### 6.3.8 Data processing inequality

Suppose we have an unknown variable X, and we observe a noisy function of it, call it Y. If we process the noisy observations in some way to create a new variable Z, it should be intuitively obvious that we cannot increase the amount of information we have about the unknown quantity, X. This is known as the data processing inequality. We now state this more formally, and then prove it.

Theorem 6.3.1. Suppose  $X \to Y \to Z$ forms a Markov chain, so that  $X \perp Z|Y$. Then  $\mathbb{I}(X;Y) \geq \mathbb{I}(X;Z)$.

Proof. By the chain rule for mutual information (Equation (6.62)), we can expand the mutual information in two different ways:

$$
\begin{aligned}\mathbb{I}\left(X;Y,Z\right)&=\mathbb{I}\left(X;Z\right)+\mathbb{I}\left(X;Y|Z\right)\\&=\mathbb{I}\left(X;Y\right)+\mathbb{I}\left(X;Z|Y\right)\end{aligned}   \tag*{(6.77)}
$$

Since  $X \perp Z|Y$, we have  $\mathbb{I}(X; Z|Y) = 0$, so

$$
\mathbb{I}\left(X;Z\right)+\mathbb{I}\left(X;Y|Z\right)=\mathbb{I}\left(X;Y\right)   \tag*{(6.79)}
$$

Since  $\mathbb{I}(X;Y|Z)\geq0$, we have  $\mathbb{I}(X;Y)\geq\mathbb{I}(X;Z)$. Similarly one can prove that  $\mathbb{I}(Y;Z)\geq\mathbb{I}(X;Z)$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_205_127_973_467.jpg" alt="Image" width="66%" /></div>

<div style="text-align: center;">Figure 6.7: Left: Correlation coefficient vs maximal information criterion (MIC) for all pairwise relationships in the WHO data. Right: scatter plots of certain pairs of variables. The red lines are non-parametric smoothing regressions fit separately to each trend. From Figure 4 of [Res+11]. Used with kind permission of David Reshef.</div>

#### 6.3.9 Sufficient Statistics

An important consequence of the DPI is the following. Suppose we have the chain  $\theta \to \mathcal{D} \to s(\mathcal{D})$. Then

$$
\mathbb{I}\left(\theta;s(\mathcal{D})\right)\leq\mathbb{I}\left(\theta;\mathcal{D}\right)   \tag*{(6.80)}
$$

If this holds with equality, then we say that $s(\mathcal{D})$is a sufficient statistic of the data$\mathcal{D}$for the purposes of inferring$\theta$. In this case, we can equivalently write $\theta \to s(\mathcal{D}) \to \mathcal{D}$, since we can reconstruct the data from knowing $s(\mathcal{D})$just as accurately as from knowing$\theta$.

An example of a sufficient statistic is the data itself,  $s(\mathcal{D}) = \mathcal{D}$, but this is not very useful, since it doesn't summarize the data at all. Hence we define a  $\text{minimal}$ sufficient  $\text{statistic}$  $s(\mathcal{D})$ as one which is sufficient, and which contains no extra information about  $\theta$; thus  $s(\mathcal{D})$ maximally compresses the data  $\mathcal{D}$ without losing information which is relevant to predicting  $\theta$. More formally, we say  $s$ is a  $\text{minimal}$ sufficient statistic for  $\mathcal{D}$ if for all sufficient statistics  $s'(\mathcal{D})$ there is some function  $f$ such that  $s(\mathcal{D}) = f(s'(\mathcal{D}))$. We can summarize the situation as follows:

$$
\theta\to s(\mathcal{D})\to s^{\prime}(\mathcal{D})\to\mathcal{D}   \tag*{(6.81)}
$$

Here  $s'(\mathcal{D})$ takes  $s(\mathcal{D})$ and adds redundant information to it, thus creating a one-to-many mapping. For example, a minimal sufficient statistic for a set of  $N$ Bernoulli trials is simply  $N$ and  $N_1 = \sum_n \mathbb{I}(X_n = 1)$, i.e., the number of successes. In other words, we don't need to keep track of the entire sequence of heads and tails and their ordering, we only need to keep track of the total number of heads and tails. Similarly, for inferring the mean of a Gaussian distribution with known variance we only need to know the empirical mean and number of samples.

---

#### 6.3.10 Fano's inequality *

A common method for feature selection is to pick input features  $X_{d}$ which have high mutual information with the response variable Y. Below we justify why this is a reasonable thing to do. In particular, we state a result, known as Fano's inequality, which bounds the probability of misclassification (for any method) in terms of the mutual information between the features X and the class label Y.

Theorem 6.3.2. (Fano’s inequality) Consider an estimator  $\hat{Y} = f(X)$ such that  $Y \to X \to \hat{Y}$ forms a Markov chain. Let E be the event  $\hat{Y} \neq Y$, indicating that an error occurred, and let  $P_e = P(Y \neq \hat{Y})$ be the probability of error. Then we have

$$
\mathbb{H}\left(Y|X\right)\leq\mathbb{H}\left(Y|\hat{Y}\right)\leq\mathbb{H}\left(E\right)+P_{e}\log\left|\mathcal{Y}\right|   \tag*{(6.82)}
$$

Since  $\mathbb{H}(E) \leq 1$, as we saw in Figure 6.1, we can weaken this result to get

$$
1+P_{e}\log\left|\mathcal{Y}\right|\geq\mathbb{H}\left(Y|X\right)   \tag*{(6.83)}
$$

and hence

$$
P_{e}\geq\frac{\mathbb{H}(Y|X)-1}{\log|\mathcal{Y}|}   \tag*{(6.84)}
$$

Thus minimizing  $\mathbb{H}(Y|X)$ (which can be done by maximizing  $\mathbb{I}(X;Y)$) will also minimize the lower bound on  $P_e$.

Proof. (From [CT06, p38].) Using the chain rule for entropy, we have

$$
\begin{aligned}\mathbb{H}\left(E,Y|\hat{Y}\right)&=\mathbb{H}\left(Y|\hat{Y}\right)+\underbrace{\mathbb{H}\left(E|Y,\hat{Y}\right)}_{=0}\\&=\mathbb{H}\left(E|\hat{Y}\right)+\mathbb{H}\left(Y|E,\hat{Y}\right)\end{aligned}   \tag*{(6.85)}
$$

Since conditioning reduces entropy (see Section 6.2.4), we have  $\mathbb{H}\left(E|\hat{Y}\right) \leq \mathbb{H}(E)$. The final term can be bounded as follows:

$$
\begin{aligned}\mathbb{H}\left(Y|E,\hat{Y}\right)&=P(E=0)\mathbb{H}\left(Y|\hat{Y},E=0\right)+P(E=1)\mathbb{H}\left(Y|\hat{Y},E=1\right)\\&\leq(1-P_{e})0+P_{e}\log|\mathcal{Y}|\end{aligned}   \tag*{(6.87)}
$$

Hence

$$
\mathbb{H}\left(Y|\hat{Y}\right)\leq\underbrace{\mathbb{H}\left(E|\hat{Y}\right)}_{\leq\mathbb{H}(E)}+\underbrace{\mathbb{H}\left(Y|E,\hat{Y}\right)}_{P_{e}\log|\mathcal{Y}|}   \tag*{(6.89)}
$$

Finally, by the data processing inequality, we have  $\mathbb{I}(Y;\hat{Y})\leq\mathbb{I}(Y;X)$, so  $\mathbb{H}(Y|X)\leq\mathbb{H}\left(Y|\hat{Y}\right)$, which establishes Equation (6.82).

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

### 6.4 Exercises

Exercise 6.1 [Expressing mutual information in terms of entropies †]

Prove the following identities:

$$
I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)   \tag*{(6.90)}
$$

and

$$
H(X,Y)=H(X|Y)+H(Y|X)+I(X;Y)   \tag*{(6.91)}
$$

Exercise 6.2 [Relationship between  $D(p||q)$ and  $\chi^{2}$ statistic]

(Source: [CT91, Q12.2].)

Show that, if  $p(x) \approx q(x)$, then

$$
D_{\mathbb{K L}}\left(p\parallel q\right)\approx\frac{1}{2}\chi^{2}   \tag*{(6.92)}
$$

where

$$
\chi^{2}=\sum_{x}\frac{\left(p(x)-q(x)\right)^{2}}{q(x)}   \tag*{(6.93)}
$$

Hint: write

$$
p(x)=\Delta(x)+q(x)   \tag*{(6.94)}
$$

$$
\frac{p(x)}{q(x)}=1+\frac{\Delta(x)}{q(x)}   \tag*{(6.95)}
$$

and use the Taylor series expansion for  $\log(1+x)$.

$$
\log(1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}-\frac{x^{4}}{4}\cdots   \tag*{(6.96)}
$$

for  $-1 < x \leq 1$.

Exercise 6.3 [Fun with entropies †]

(Source: Mackay.)

Consider the joint distribution  $p(X, Y)$

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td colspan="4">x</td></tr><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td rowspan="4">y</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/32</td><td style='text-align: center; word-wrap: break-word;'>1/32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/32</td><td style='text-align: center; word-wrap: break-word;'>1/32</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

a. What is the joint entropy  $H(X,Y)$?

b. What are the marginal entropies  $H(X)$ and  $H(Y)$?

c. The entropy of X conditioned on a specific value of y is defined as

$$
H(X|Y=y)=-\sum_{x}p(x|y)\log p(x|y)   \tag*{(6.97)}
$$

Compute  $H(X|y)$ for each value of y. Does the posterior entropy on X ever increase given an observation of Y?

---

d. The conditional entropy is defined as

$$
H(X|Y)=\sum_{y}p(y)H(X|Y=y)   \tag*{(6.98)}
$$

Compute this. Does the posterior entropy on X increase or decrease when averaged over the possible values of Y?

e. What is the mutual information between X and Y?

##### Exercise 6.4 [Forwards vs reverse KL divergence]

(Source: Exercise 33.7 of [Mac03].) Consider a factored approximation  $q(x, y) = q(x)q(y)$ to a joint distribution  $p(x, y)$. Show that to minimize the forwards KL  $D_{\mathbb{K}\mathbb{L}}(p \parallel q)$ we should set  $q(x) = p(x)$ and  $q(y) = p(y)$, i.e., the optimal approximation is a product of marginals.

Now consider the following joint distribution, where the rows represent y and the columns x.

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/4</td></tr></table>

Show that the reverse KL  $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ for this  $p$ has three distinct minima. Identify those minima and evaluate  $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ at each of them. What is the value of  $D_{\mathbb{K}\mathbb{L}}(q \parallel p)$ if we set  $q(x,y) = p(x)p(y)$?

---



---

## 7 Linear Algebra

This chapter is co-authored with Zico Kolter.

### 7.1 Introduction

Linear algebra is the study of matrices and vectors. In this chapter, we summarize the key material that we will need throughout the book. Much more information can be found in other sources, such as [Str09; Ips09; Kle13; Mol04; TB97; Axl15; Th017; Agg20; LLM14].

#### 7.1.1 Notation

In this section, we define some notation.

##### 7.1.1.1 Vectors

A vector  $x \in \mathbb{R}^n$ is a list of  $n$ numbers, usually written as a column vector

$$
\begin{aligned}&\boldsymbol{x}=\begin{bmatrix}x_{1}\\x_{2}\\\vdots\\x_{n}\end{bmatrix}.\end{aligned}   \tag*{(7.1)}
$$

The vector of all ones is denoted 1. The vector of all zeros is denoted 0. The unit vector  $e_i$ is a vector of all 0's, except entry i, which has value 1:

$$
e_{i}=(0,\ldots,0,1,0,\ldots,0)   \tag*{(7.2)}
$$

This is also called a one-hot vector.

##### 7.1.1.2 Matrices

A matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ with  $m$ rows and  $n$ columns is a 2d array of numbers, arranged as follows:

$$
\mathbf{A}=\left[\begin{array}{cccc}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\\\end{array}\right].   \tag*{(7.3)}
$$


---

If m = n, the matrix is said to be square.

We use the notation  $A_{ij}$ or  $A_{i,j}$ to denote the entry of A in the ith row and jth column. We use the notation  $A_{i,:}$ to denote the  $i^{th}$ row and  $A_{:,j}$ to denote the  $j^{th}$ column. We treat all vectors as column vectors by default (so  $A_{i,:}$ is viewed as a column vector with n entries). We use bold upper case letters to denote matrices, bold lower case letters to denote vectors, and non-bold letters to denote scalars.

We can view a matrix as a set of columns stacked along the horizontal axis:

$$
\mathbf{A}=\left[\begin{array}{ccc}\mid&\mid&\\\mathbf{A}_{:,1}&\mathbf{A}_{:,2}&\cdots&\mathbf{A}_{:,n}\\\mid&\mid&&\mid\end{array}\right].   \tag*{(7.4)}
$$

For brevity, we will denote this by

$$
\mathbf{A}=[\mathbf{A}_{:,1},\mathbf{A}_{:,2},\ldots,\mathbf{A}_{:,n}]   \tag*{(7.5)}
$$

We can also view a matrix as a set of rows stacked along the vertical axis:

$$
\mathbf{A}=\left[\begin{array}{ccc}-\mathbf{A}_{1,:}^{\mathsf{T}}&-\\\mathbf{A}_{2,:}^{\mathsf{T}}&-\\\vdots&\\\mathbf{A}_{m,:}^{\mathsf{T}}&-\end{array}\right].   \tag*{(7.6)}
$$

For brevity, we will denote this by

$$
\mathbf{A}=[\mathbf{A}_{1,:};\mathbf{A}_{2,:};\cdots;\mathbf{A}_{m,:}]   \tag*{(7.7)}
$$

(Note the use of a semicolon.)

The transpose of a matrix results from “flipping” the rows and columns. Given a matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$, its transpose, written  $\mathbf{A}^\top \in \mathbb{R}^{n \times m}$, is defined as

$$
(\mathbf{A}^{\mathsf{T}})_{i j}=A_{j i}   \tag*{(7.8)}
$$

The following properties of transposes are easily verified:

$$
(\mathbf{A}^{\mathsf{T}})^{\mathsf{T}}=\mathbf{A}   \tag*{(7.9)}
$$

$$
\left(\mathbf{A}\mathbf{B}\right)^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}   \tag*{(7.10)}
$$

$$
\left(\mathbf{A}+\mathbf{B}\right)^{\mathrm{T}}=\mathbf{A}^{\mathrm{T}}+\mathbf{B}^{\mathrm{T}}   \tag*{(7.11)}
$$

If a square matrix satisfies  $\mathbf{A} = \mathbf{A}^\top$, it is called symmetric. We denote the set of all symmetric matrices of size  $n$ as  $\mathbb{S}^n$.

##### 7.1.1.3 Tensors

A tensor (in machine learning terminology) is just a generalization of a 2d array to more than 2 dimensions, as illustrated in Figure 7.1. For example, the entries of a 3d tensor are denoted by  $A_{ijk}$.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_371_125_798_402.jpg" alt="Image" width="37%" /></div>

<div style="text-align: center;">Figure 7.1: Illustration of a 1d vector, 2d matrix, and 3d tensor. The colors are used to represent individual entries of the vector; this list of numbers can also be stored in a 2d matrix, as shown. (In this example, the matrix is layed out in column-major order, which is the opposite of that used by Python.) We can also reshape the vector into a 3d tensor, as shown.</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_283_541_482_684.jpg" alt="Image" width="17%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_689_548_891_688.jpg" alt="Image" width="17%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 7.2: Illustration of (a) row-major vs (b) column-major order. From https://commons.wikimedia.org/wiki/File:Row_and_column_major_order.svg. Used with kind permission of Wikipedia author Cmqlee.</div>

The number of dimensions is known as the order or rank of the tensor. $^{1}$ In mathematics, tensors can be viewed as a way to define multilinear maps, just as matrices can be used to define linear functions, although we will not need to use this interpretation.

We can reshape a matrix into a vector by stacking its columns on top of each other, as shown in Figure 7.1. This is denoted by

$$
\operatorname{vec}(\mathbf{A})=[\mathbf{A}_{:,1};\cdots;\mathbf{A}_{:,n}]\in\mathbb{R}^{mn\times1}   \tag*{(7.12)}
$$

Conversely, we can reshape a vector into a matrix. There are two choices for how to do this, known as row-major order (used by languages such as Python and C++) and column-major order (used by languages such as Julia, Matlab, R and Fortran). See Figure 7.2 for an illustration of the difference.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_184_113_568_350.jpg" alt="Image" width="33%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_681_118_905_341.jpg" alt="Image" width="19%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 7.3: (a) Top: A vector v (blue) is added to another vector w (red). Bottom: w is stretched by a factor of 2, yielding the sum v + 2w. From https://en.wikipedia.org/wiki/Vector_space. Used with kind permission of Wikipedia author IkamusumeFan (b) A vector v in  $R^2$ (blue) expressed in terms of different bases: using the standard basis of  $R^2$,  $v = xe_1 + ye_2$ (black), and using a different, non-orthogonal basis:  $v = f_1 + f_2$ (red). From https://en.wikipedia.org/wiki/Vector_space. Used with kind permission of Wikipedia author Jakob.scholbach.</div>

#### 7.1.2 Vector spaces

In this section, we discuss some fundamental concepts in linear algebra.

##### 7.1.2.1 Vector addition and scaling

We can view a vector  $\boldsymbol{x} \in \mathbb{R}^n$ as defining a point in  $n$-dimensional Euclidean space. A vector space is a collection of such vectors, which can be added together, and scaled by  $\text{scalars}$ (1-dimensional numbers), in order to create new points. These operations are defined to operate elementwise, in the obvious way, namely  $\boldsymbol{x} + \boldsymbol{y} = (x_1 + y_1, \ldots, x_n + y_n)$ and  $\boldsymbol{c}\boldsymbol{x} = (c x_1, \ldots, c x_n)$, where  $c \in \mathbb{R}$. See Figure 7.3a for an illustration.

##### 7.1.2.2 Linear independence, spans and basis sets

A set of vectors $\{x_1, x_2, \ldots, x_n\}$ is said to be (linearly) independent if no vector can be represented as a linear combination of the remaining vectors. Conversely, a vector which can be represented as a linear combination of the remaining vectors is said to be (linearly) dependent. For example, if

$$
\boldsymbol{x}_{n}=\sum_{i=1}^{n-1}\alpha_{i}\boldsymbol{x}_{i}   \tag*{(7.13)}
$$

for some $\{ \alpha_1, \ldots, \alpha_{n-1} \}$then$x_n$is dependent on$\{x_1, \ldots, x_{n-1}\}$; otherwise, it is independent of $\{x_1, \ldots, x_{n-1}\}$.

The span of a set of vectors $\{x_1, x_2, \ldots, x_n\}$is the set of all vectors that can be expressed as a linear combination of$\{x_1, \ldots, x_n\}$. That is,

$$
\mathrm{s p a n}(\left\{\boldsymbol{x}_{1},\cdots,\boldsymbol{x}_{n}\right\})\triangleq\left\{\boldsymbol{v}:\boldsymbol{v}=\sum_{i=1}^{n}\alpha_{i}\boldsymbol{x}_{i},\alpha_{i}\in\mathbb{R}\right\}.   \tag*{(7.14)}
$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

It can be shown that if $\{x_1, \ldots, x_n\}$is a set of$n$linearly independent vectors, where each$x_i \in \mathbb{R}^n$, then $\operatorname{span}(\{x_1, \ldots, x_n\}) = \mathbb{R}^n$. In other words, any vector $v \in \mathbb{R}^n$can be written as a linear combination of$x_1$through$x_n$.

A basis  $\mathcal{B}$ is a set of linearly independent vectors that spans the whole space, meaning that  $\text{span}(\mathcal{B}) = \mathbb{R}^n$. There are often multiple bases to choose from, as illustrated in Figure 7.3b. The standard basis uses the coordinate vectors  $e_1 = (1, 0, \ldots, 0)$, up to  $e_n = (0, 0, \ldots, 0, 1)$. This lets us translate back and forth between viewing a vector in  $\mathbb{R}^2$ as an either an “arrow in the plane”, rooted at the origin, or as an ordered list of numbers (corresponding to the coefficients for each basis vector).

##### 7.1.2.3 Linear maps and matrices

A linear map or linear transformation is any function $f: \mathcal{V} \to \mathcal{W}$such that$f(\boldsymbol{v} + \boldsymbol{w}) = f(\boldsymbol{v}) + f(\boldsymbol{w})$and$f(a\ \boldsymbol{v}) = a\ f(\boldsymbol{v})$for all$\boldsymbol{v}, \boldsymbol{w} \in \mathcal{V}$. Once the basis of $\mathcal{V}$is chosen, a linear map$f: \mathcal{V} \to \mathcal{W}$is completely determined by specifying the images of the basis vectors, because any element of$\mathcal{V}$can be expressed uniquely as a linear combination of them.

Suppose$\mathcal{V} = \mathbb{R}^n$and$\mathcal{W} = \mathbb{R}^m$. We can compute $f(\boldsymbol{v}_i) \in \mathbb{R}^m$for each basis vector in$\mathcal{V}$, and store these along the columns of an $m \times n$matrix$\mathbf{A}$. We can then compute $\boldsymbol{y} = f(\boldsymbol{x}) \in \mathbb{R}^m$for any$\boldsymbol{x} \in \mathbb{R}^n$ as follows:

$$
\boldsymbol{y}=\left(\sum_{j=1}^{n}a_{1j}x_{j},\ldots,\sum_{j=1}^{n}a_{mj}x_{j}\right)   \tag*{(7.15)}
$$

This corresponds to multiplying the vector x by the matrix A:

$$
y=\mathbf{A}x   \tag*{(7.16)}
$$

See Section 7.2 for more details.

If the function is invertible, we can write

$$
\boldsymbol{x}=\mathbf{A}^{-1}\boldsymbol{y}   \tag*{(7.17)}
$$

See Section 7.3 for details.

##### 7.1.2.4 Range and nullspace of a matrix

Suppose we view a matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ as a set of  $n$ vectors in  $\mathbb{R}^m$. The  $\text{range}$ (sometimes also called the  $\text{column space}$) of this matrix is the span of the columns of  $\mathbf{A}$. In other words,

$$
\mathrm{range}(\mathbf{A})\triangleq\{\boldsymbol{v}\in\mathbb{R}^{m}:\boldsymbol{v}=\mathbf{A}\boldsymbol{x},\boldsymbol{x}\in\mathbb{R}^{n}\}.   \tag*{(7.18)}
$$

This can be thought of as the set of vectors that can be “reached” or “generated” by A; it is a subspace of  $\mathbb{R}^m$ whose dimensionality is given by the rank of  $\mathbf{A}$ (see Section 7.1.4.3). The  $\text{nullspace}$ of a matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ is the set of all vectors that get mapped to the null vector when multiplied by  $\mathbf{A}$, i.e.,

$$
\mathsf{n u l l s p a c e}(\mathbf{A})\triangleq\{\mathbf{x}\in\mathbb{R}^{n}:\mathbf{A}\mathbf{x}=\mathbf{0}\}.   \tag*{(7.19)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_388_134_781_400.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">Figure 7.4: Visualization of the nullspace and range of an  $m \times n$ matrix A. Here  $\mathbf{y}_1 = \mathbf{A}\mathbf{x}_1$ and  $\mathbf{y}_2 = \mathbf{A}\mathbf{x}_4$, so  $\mathbf{y}_1$ and  $\mathbf{y}_2$ are in the range of A (are reachable from some  $\mathbf{x}$). Also  $\mathbf{A}\mathbf{x}_2 = \mathbf{0}$ and  $\mathbf{A}\mathbf{x}_3 = \mathbf{0}$, so  $\mathbf{x}_2$ and  $\mathbf{x}_3$ are in the nullspace of A (get mapped to 0). We see that the range is often a subset of the input domain of the mapping.</div>

The span of the rows of A is the complement to the nullspace of A.

See Figure 7.4 for an illustration of the range and nullspace of a matrix. We shall discuss how to compute the range and nullspace of a matrix numerically in Section 7.5.4 below.

##### 7.1.2.5 Linear projection

The projection of a vector  $\boldsymbol{y} \in \mathbb{R}^m$ onto the span of  $\{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_n\}$ (here we assume  $\boldsymbol{x}_i \in \mathbb{R}^m$) is the vector  $\boldsymbol{v} \in \text{span}(\{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_n\}$) such that  $\boldsymbol{v}$ is as close as possible to  $\boldsymbol{y}$, as measured by the Euclidean norm  $\|\boldsymbol{v} - \boldsymbol{y}\|_2$. We denote the projection as  $\text{Proj}(\boldsymbol{y};\{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_n\})$ and can define it formally as

$$
\operatorname{P r o j}(y;\{x_{1},\dots,x_{n}\})=\operatorname{a r g m i n}_{v\in\operatorname{s p a n}(\{x_{1},\dots,x_{n}\})}\|y-v\|_{2}.   \tag*{(7.20)}
$$

Given a (full rank) matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ with  $m \geq n$, we can define the projection of a vector  $\mathbf{y} \in \mathbb{R}^m$ onto the range of  $\mathbf{A}$ as follows:

$$
\operatorname{P r o j}(\mathbf{y};\mathbf{A})=\operatorname{a r g m i n}_{\mathbf{v}\in\mathcal{R}(\mathbf{A})}\|\mathbf{v}-\mathbf{y}\|_{2}=\mathbf{A}(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}\mathbf{y}\enspace.   \tag*{(7.21)}
$$

These are the same as the normal equations from Section 11.2.2.2.

#### 7.1.3 Norms of a vector and matrix

In this section, we discuss ways of measuring the “size” of a vector and matrix.

##### 7.1.3.1 Vector norms

A norm of a vector  $\|x\|$ is, informally, a measure of the “length” of the vector. More formally, a norm is any function  $f: \mathbb{R}^n \to \mathbb{R}$ that satisfies 4 properties:

• For all  $x \in \mathbb{R}^n$,  $f(x) \geq 0$ (non-negativity).

"Probabilistic Machine Learning: An Introduction". Online version. November 23, 2024

---

### 7.1. Introduction

•  $f(x) = 0$ if and only if  $x = 0$ (definiteness).

• For all  $x \in \mathbb{R}^n$,  $t \in \mathbb{R}$,  $f(tx) = |t|f(x)$ (absolute value homogeneity).

• For all  $x, y \in \mathbb{R}^n$,  $f(x + y) \leq f(x) + f(y)$ (triangle inequality).

Consider the following common examples:

p-norm  $\|x\|_{p} = (\sum_{i=1}^{n}|x_{i}|^{p})^{1/p}$, for  $p \geq 1$.

2-norm  $\|x\|_2 = \sqrt{\sum_{i=1}^{n} x_i^2}$, also called Euclidean norm. Note that  $\|x\|_2^2 = x^\top x$.

1-norm  $\|x\|_1 = \sum_{i=1}^n |x_i|$.

Max-norm  $\|x\|_\infty = \max_i |x_i|$.

0-norm  $\|x\|_0 = \sum_{i=1}^n \mathbb{I}(|x_i| > 0)$. This is a pseudo norm, since it does not satisfy homogeneity. It counts the number of non-zero elements in  $\mathbf{x}$. If we define  $0^0 = 0$, we can write this as  $\|x\|_0 = \sum_{i=1}^n x_i^0$.

##### 7.1.3.2 Matrix norms

Suppose we think of a matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ as defining a linear function  $f(\boldsymbol{x}) = \mathbf{A}\boldsymbol{x}$. We define the induced norm of  $\mathbf{A}$ as the maximum amount by which  $f$ can lengthen any unit-norm input:

$$
\left|\left|\mathbf{A}\right|\right|_{p}=\max_{\mathbf{x}\neq\mathbf{0}}\frac{\left|\left|\mathbf{A}\mathbf{x}\right|\right|_{p}}{\left|\left|\mathbf{x}\right|\right|_{p}}=\max_{\left|\left|\mathbf{x}\right|\right|=1}\left|\left|\mathbf{A}\mathbf{x}\right|\right|_{p}   \tag*{(7.22)}
$$

Typically p = 2, in which case

$$
||\mathbf{A}||_{2}=\sqrt{\lambda_{\max}(\mathbf{A}^{\mathsf{T}}\mathbf{A})}=\max_{i}\sigma_{i}   \tag*{(7.23)}
$$

where  $\lambda_{\max}(\mathbf{M})$ is the largest eigenvalue of  $\mathbf{M}$, and  $\sigma_{i}$ is the  $i^{\prime}$th singular value.

The nuclear norm, also called the trace norm, is defined as

$$
\left|\left|\mathbf{A}\right|\right|_{*}=\mathrm{tr}(\sqrt{\mathbf{A}^{\mathsf{T}}\mathbf{A}})=\sum_{i}\sigma_{i}   \tag*{(7.24)}
$$

where  $\sqrt{A^{\top}A}$ is the matrix square root. Since the singular values are always non-negative, we have

$$
\left|\left|\mathbf{A}\right|\right|_{*}=\sum_{i}\left|\sigma_{i}\right|=\left|\left|\boldsymbol{\sigma}\right|\right|_{1}   \tag*{(7.25)}
$$

Using this as a regularizer encourages many singular values to become zero, resulting in a low rank matrix. More generally, we can define the Schatten p-norm as

$$
\left|\left|\mathbf{A}\right|\right|_{p}=\left(\sum_{i}\sigma_{i}^{p}(\mathbf{A})\right)^{1/p}   \tag*{(7.26)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

If we think of a matrix as a vector, we can define the matrix norm in terms of a vector norm,  $\|A\| = \|vec{v}c(A)\|$. If the vector norm is the 2-norm, the corresponding matrix norm is the  $\text{Frobenius}$ norm:

$$
|\mathbf{A}||_{F}=\sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}^{2}}=\sqrt{\mathrm{tr}(\mathbf{A}^{\mathsf{T}}\mathbf{A})}=||\mathrm{vec}(\mathbf{A})||_{2}   \tag*{(7.27)}
$$

If  $\mathbf{A}$ is expensive to evaluate, but  $\mathbf{A}v$ is cheap (for a random vector  $\mathbf{v}$), we can create a stochastic approximation to the Frobenius norm by using the Hutchinson trace estimator from Equation (7.37) as follows:

$$
||\mathbf{A}||_{F}^{2}=\mathrm{tr}(\mathbf{A}^{\mathsf{T}}\mathbf{A})=\mathbb{E}\left[\mathbf{v}^{\mathsf{T}}\mathbf{A}^{\mathsf{T}}\mathbf{A}\mathbf{v}\right]=\mathbb{E}\left[||\mathbf{A}\mathbf{v}||_{2}^{2}\right]   \tag*{(7.28)}
$$

where v ∼ N(0,1).

#### 7.1.4 Properties of a matrix

In this section, we discuss various scalar properties of matrices.

##### 7.1.4.1 Trace of a square matrix

The trace of a square matrix  $\mathbf{A} \in \mathbb{R}^{n \times n}$, denoted  $\text{tr}(\mathbf{A})$, is the sum of diagonal elements in the matrix:

$$
\mathrm{tr}(\mathbf{A})\triangleq\sum_{i=1}^{n}A_{ii}.   \tag*{(7.29)}
$$

The trace has the following properties, where  $c \in \mathbb{R}$ is a scalar, and  $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{n \times n}$ are square matrices:

 
$$
\mathrm{tr}(\mathbf{A})=\mathrm{tr}(\mathbf{A}^{\mathsf{T}})
$$
 

$$
\mathrm{tr}(\mathbf{A}+\mathbf{B})=\mathrm{tr}(\mathbf{A})+\mathrm{tr}(\mathbf{B})   \tag*{(7.30)}
$$

$$
\mathrm{tr}(\boldsymbol{c}\mathbf{A})=c\mathrm{tr}(\mathbf{A})   \tag*{(7.31)}
$$

$$
\mathrm{tr}(\mathbf{A}\mathbf{B})=\mathrm{tr}(\mathbf{B}\mathbf{A})   \tag*{(7.33)}
$$

$$
\mathrm{tr}(\mathbf{A})=\sum_{i=1}^{n}\lambda_{i}where\lambda_{i}are the eigenvalues of\mathbf{A}   \tag*{(7.34)}
$$

We also have the following important cyclic permutation property: For A, B, C such that ABC is square,

 
$$
\mathrm{tr}(\mathbf{ABC})=\mathrm{tr}(\mathbf{B}\mathbf{CA})=\mathrm{tr}(\mathbf{C}\mathbf{A}\mathbf{B})
$$
 

From this, we can derive the trace trick, which rewrites the scalar inner product  $\boldsymbol{x}^{\top}\boldsymbol{A}\boldsymbol{x}$ as follows

$$
\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}=\mathrm{tr}(\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x})=\mathrm{tr}(\boldsymbol{x}\boldsymbol{x}^{\top}\mathbf{A})   \tag*{(7.36)}
$$


---

In some cases, it may be expensive to evaluate the matrix  $\mathbf{A}$, but we may be able to cheaply evaluate matrix-vector products  $\mathbf{A}\mathbf{v}$. Suppose  $\mathbf{v}$ is a random vector such that  $\mathbf{E}\left[\mathbf{v}\mathbf{v}^{\mathrm{T}}\right]=\mathbf{I}$. In this case, we can create a Monte Carlo approximation to  $\operatorname{tr}(\mathbf{A})$ using the following identity:

$$
\mathrm{tr}(\mathbf{A})=\mathrm{tr}(\mathbf{A}\mathbb{E}\left[\mathbf{v}\mathbf{v}^{\mathrm{T}}\right])=\mathbb{E}\left[\mathrm{tr}(\mathbf{A}\mathbf{v}\mathbf{v}^{\mathrm{T}})\right]=\mathbb{E}\left[\mathrm{tr}(\mathbf{v}^{\mathrm{T}}\mathbf{A}\mathbf{v})\right]=\mathbb{E}\left[\mathbf{v}^{\mathrm{T}}\mathbf{A}\mathbf{v}\right]   \tag*{(7.37)}
$$

This is called the Hutchinson trace estimator [Hut90].

##### 7.1.4.2 Determinant of a square matrix

The determinant of a square matrix, denoted  $\det(\mathbf{A})$ or  $|\mathbf{A}|$, is a measure of how much it changes a unit volume when viewed as a linear transformation. (The formal definition is rather complex and is not needed here.)

The determinant operator satisfies these properties, where  $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{n \times n}$

$$
\left|\mathbf{A}\right|=\left|\mathbf{A}^{\mathrm{T}}\right|   \tag*{(7.38)}
$$

$$
|c\mathbf{A}|=c^{n}|\mathbf{A}|   \tag*{(7.39)}
$$

$$
\left|\mathbf{A}\mathbf{B}\right|=\left|\mathbf{A}\right|\left|\mathbf{B}\right|   \tag*{(7.40)}
$$

$$
\left|\mathbf{A}\right|=0iff\mathbf{A}is singular   \tag*{(7.41)}
$$

$$
\left|\mathbf{A}^{-1}\right|=1/\left|\mathbf{A}\right|if\mathbf{A}is not singular   \tag*{(7.42)}
$$

$$
\left|\mathbf{A}\right|=\prod_{i=1}^{n}\lambda_{i}\text{where}\lambda_{i}\text{are the eigenvalues of}\mathbf{A}   \tag*{(7.43)}
$$

For a positive definite matrix  $\mathbf{A}$, we can write  $\mathbf{A} = \mathbf{L}\mathbf{L}^{\top}$, where  $\mathbf{L}$ is the lower triangular Cholesky decomposition. In this case, we have

$$
\det(\mathbf{A})=\det(\mathbf{L})\det(\mathbf{L}^{\top})=\det(\mathbf{L})^{2}   \tag*{(7.44)}
$$

so

$$
\log\det(\mathbf{A})=2\log\det(\mathbf{L})=2\log\prod_{i}L_{ii}=2tr(\log(diag(\mathbf{L})))   \tag*{(7.45)}
$$

##### 7.1.4.3 Rank of a matrix

The column rank of a matrix A is the dimension of the space spanned by its columns, and the row rank is the dimension of the space spanned by its rows. It is a basic fact of linear algebra (that can be shown using the SVD, discussed in Section 7.5) that for any matrix A, columnrank(A) = rowrank(A), and so this quantity is simply referred to as the rank of A, denoted as rank(A). The following are some basic properties of the rank:

• For $\mathbf{A} \in \mathbb{R}^{m \times n}$, rank($\mathbf{A}$) $\leq$ min($m, n$). If rank($\mathbf{A}$) = min($m, n)$, then $\mathbf{A}$ is said to be full rank, otherwise it is called rank deficient.

 
$$
\bullet\mathrm{~F o r~}\mathbf{A}\in\mathbb{R}^{m\times n},\mathrm{r a n k}(\mathbf{A})=\mathrm{r a n k}(\mathbf{A}^{\mathsf{T}})=\mathrm{r a n k}(\mathbf{A}^{\mathsf{T}}\mathbf{A})=\mathrm{r a n k}(\mathbf{A}\mathbf{A}^{\mathsf{T}}).
$$
 

• For  $A \in \mathbb{R}^{m \times n}$,  $B \in \mathbb{R}^{n \times p}$, rank( $A B$)  $\leq$ min(rank( $A$), rank( $B$)).

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

• For  $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}$, rank $(\mathbf{A} + \mathbf{B}) \leq \operatorname{rank}(\mathbf{A}) + \operatorname{rank}(\mathbf{B})$.

One can show that a square matrix is invertible if it is full rank.

##### 7.1.4.4 Condition numbers

The condition number of a matrix A is a measure of how numerically stable any computations involving A will be. It is defined as follows:

$$
\kappa(\mathbf{A})\triangleq||\mathbf{A}||\cdot||\mathbf{A}^{-1}||   \tag*{(7.46)}
$$

where  $\|\mathbf{A}\|$ is the norm of the matrix. We can show that  $\kappa(\mathbf{A}) \geq 1$. (The condition number depends on which norm we use; we will assume the  $\ell_2$-norm unless stated otherwise.)

We say A is well-conditioned if  $\kappa(\mathbf{A})$ is small (close to 1), and ill-conditioned if  $\kappa(\mathbf{A})$ is large. A large condition number means A is nearly singular. This is a better measure of nearness to singularity than the size of the determinant. For example, suppose  $\mathbf{A} = 0.1\mathbf{I}_{100 \times 100}$. Then  $\det(\mathbf{A}) = 10^{-100}$, which suggests A is nearly singular, but  $\kappa(\mathbf{A}) = 1$, which means A is well-conditioned, reflecting the fact that  $\mathbf{A}x$ simply scales the entries of  $\mathbf{x}$ by 0.1.

To get a better understanding of condition numbers, consider the linear system of equations  $\mathbf{A}\mathbf{x}=\mathbf{b}$. If  $\mathbf{A}$ is non-singular, the unique solution is  $\mathbf{x}=\mathbf{A}^{-1}\mathbf{b}$. Suppose we change  $\mathbf{b}$ to  $\mathbf{b}+\Delta\mathbf{b}$; what effect will that have on  $\mathbf{x}$? The new solution must satisfy

$$
\mathbf{A}(x+\Delta x)=b+\Delta b   \tag*{(7.47)}
$$

where

$$
\Delta x=\mathbf{A}^{-1}\Delta b   \tag*{(7.48)}
$$

We say that A is well-conditioned if a small  $\Delta b$ results in a small  $\Delta x$; otherwise we say that A is ill-conditioned.

For example, suppose

$$
\mathbf{A}=\frac{1}{2}\begin{pmatrix}{{{1}}}&{{{1}}} \\{{{1+10^{-10}}}}&{{{1-10^{-10}}}}\end{pmatrix},\mathbf{A}^{-1}=\begin{pmatrix}{{{1-10^{10}}}}&{{{10^{10}}}} \\{{{1+10^{10}}}}&{{{-10^{10}}}}\end{pmatrix}   \tag*{(7.49)}
$$

The solution for  $\boldsymbol{b} = (1, 1)$ is  $\boldsymbol{x} = (1, 1)$. If we change  $\boldsymbol{b}$ by  $\Delta\boldsymbol{b}$, the solution changes to

$$
\Delta\boldsymbol{x}=\boldsymbol{A}^{-1}\Delta\boldsymbol{b}=\begin{pmatrix}\Delta b_{1}-10^{10}(\Delta b_{1}-\Delta b_{2})\\\Delta b_{1}+10^{10}(\Delta b_{1}-\Delta b_{2})\end{pmatrix}   \tag*{(7.50)}
$$

So a small change in $b$can lead to an extremely large change in$x$, because $A$is ill-conditioned$(\kappa(\mathbf{A})=2\times10^{10})$.

In the case of the  $\ell_2$-norm, the condition number is equal to the ratio of the largest to smallest singular values (defined in Section 7.5); furthermore, the singular values of  $\mathbf{A}$ are the square roots of the eigenvalues of  $\mathbf{A}^\top \mathbf{A}$, and so

$$
\kappa(\mathbf{A})=\sigma_{max}/\sigma_{min}=\sqrt{\frac{\lambda_{\max}}{\lambda_{\min}}}   \tag*{(7.51)}
$$


---

We can gain further insight into condition numbers by considering a quadratic objective function  $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}$. If we plot the level set of this function, it will be elliptical, as shown in Section 7.4.4. As we increase the condition number of A, the ellipses become more and more elongated along certain directions, corresponding to a very narrow valley in function space. If  $\kappa = 1$ (the minimum possible value), the level set will be circular.

#### 7.1.5 Special types of matrices

In this section, we will list some common kinds of matrices with various forms of structure.

##### 7.1.5.1 Diagonal matrix

A diagonal matrix is a matrix where all non-diagonal elements are 0. This is typically denoted  $\mathbf{D} = \mathrm{diag}(d_1, d_2, \ldots, d_n)$, with

$$
\mathbf{D}=\begin{pmatrix}d_{1}&&&\\&d_{2}&&\\&&\ddots&\\&&&d_{n}\end{pmatrix}   \tag*{(7.52)}
$$

The identity matrix, denoted  $\mathbf{I} \in \mathbb{R}^{n \times n}$, is a square matrix with ones on the diagonal and zeros everywhere else,  $\mathbf{I} = \text{diag}(1, 1, \ldots, 1)$. It has the property that for all  $\mathbf{A} \in \mathbb{R}^{n \times n}$,

$$
\mathbf{A}\mathbf{I}=\mathbf{A}=\mathbf{I}\mathbf{A}   \tag*{(7.53)}
$$

where the size of I is determined by the dimensions of A so that matrix multiplication is possible.

We can extract the diagonal vector from a matrix using  $\boldsymbol{d} = \mathrm{diag}(\boldsymbol{D})$. We can convert a vector into a diagonal matrix by writing  $\boldsymbol{D} = \mathrm{diag}(\boldsymbol{d})$.

A block diagonal matrix is one which contains matrices on its main diagonal, and is 0 everywhere else, e.g.,

$$
\begin{pmatrix}{{{\mathbf{A}}}}&{{{0}}} \\{{{0}}}&{{{\mathbf{B}}}}\end{pmatrix}   \tag*{(7.54)}
$$

A band-diagonal matrix only has non-zero entries along the diagonal, and on $k$sides of the diagonal, where$k$is the bandwidth. For example, a tridiagonal$6 \times 6$ matrix looks like this:

$$
\begin{bmatrix}{{{A_{11}}}}&{{{A_{12}}}}&{{{0}}}&{{{\cdots}}}&{{{\cdots}}}&{{{0}}} \\{{{A_{21}}}}&{{{A_{22}}}}&{{{A_{23}}}}&{{{\ddots}}}&{{{\ddots}}}&{{{\vdots}}} \\{{{0}}}&{{{A_{32}}}}&{{{A_{33}}}}&{{{A_{34}}}}&{{{\ddots}}}&{{{\vdots}}} \\{{{\vdots}}}&{{{\ddots}}}&{{{A_{43}}}}&{{{A_{44}}}}&{{{A_{45}}}}&{{{0}}} \\{{{\vdots}}}&{{{\ddots}}}&{{{\ddots}}}&{{{A_{54}}}}&{{{A_{55}}}}&{{{A_{56}}}} \\{{{0}}}&{{{\cdots}}}&{{{\cdots}}}&{{{0}}}&{{{A_{65}}}}&{{{A_{66}}}}\end{bmatrix}   \tag*{(7.55)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

##### 7.1.5.2 Triangular matrices

An upper triangular matrix only has non-zero entries on and above the diagonal. A lower triangular matrix only has non-zero entries on and below the diagonal.

Triangular matrices have the useful property that the diagonal entries of  $\mathbf{A}$ are the eigenvalues of  $\mathbf{A}$, and hence the determinant is the product of diagonal entries:  $\det(\mathbf{A}) = \prod_i A_{ii}$.

##### 7.1.5.3 Positive definite matrices

Given a square matrix  $\mathbf{A} \in \mathbb{R}^{n \times n}$ and a vector  $\boldsymbol{x} \in \mathbb{R}^n$, the scalar value  $\boldsymbol{x}^\top \mathbf{A} \boldsymbol{x}$ is called a quadratic form. Written explicitly, we see that

$$
\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}=\sum_{i=1}^{n}\sum_{j=1}^{n}A_{i j}x_{i}x_{j}\quad.   \tag*{(7.56)}
$$

Note that,

$$
\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}=(\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x})^{\mathsf{T}}=\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x}=\boldsymbol{x}^{\mathsf{T}}(\frac{1}{2}\boldsymbol{A}+\frac{1}{2}\boldsymbol{A}^{\mathsf{T}})\boldsymbol{x}   \tag*{(7.57)}
$$

For this reason, we often implicitly assume that the matrices appearing in a quadratic form are symmetric.

We give the following definitions:

- A symmetric matrix  $\mathbf{A} \in \mathbb{S}^n$ is positive definite iff for all non-zero vectors  $\boldsymbol{x} \in \mathbb{R}^n$,  $\boldsymbol{x}^\top \mathbf{A} \boldsymbol{x} > 0$. This is usually denoted  $\mathbf{A} \succ 0$ (or just  $\mathbf{A} > 0$). If it is possible that  $\boldsymbol{x}^\top \mathbf{A} \boldsymbol{x} = 0$, we say the matrix is positive semidefinite or PSD. We denote the set of all positive definite matrices by  $\mathbb{S}_{++}^n$.

- A symmetric matrix  $\mathbf{A} \in \mathbb{S}^n$ is negative definite, denoted  $\mathbf{A} \prec 0$ (or just  $\mathbf{A} < 0$) iff for all non-zero  $\mathbf{x} \in \mathbb{R}^n$,  $\mathbf{x}^\top \mathbf{A} \mathbf{x} < 0$. If it is possible that  $\mathbf{x}^\top \mathbf{A} \mathbf{x} = 0$, we say the matrix is negative semidefinite.

- A symmetric matrix  $A \in \mathbb{S}^n$ is indefinite, if it is neither positive semidefinite nor negative semidefinite — i.e., if there exists  $x_1, x_2 \in \mathbb{R}^n$ such that  $x_1^\top A x_1 > 0$ and  $x_2^\top A x_2 < 0$.

It should be obvious that if  $\mathbf{A}$ is positive definite, then  $-\mathbf{A}$ is negative definite and vice versa. Likewise, if  $\mathbf{A}$ is positive semidefinite then  $-\mathbf{A}$ is negative semidefinite and vice versa. If  $\mathbf{A}$ is indefinite, then so is  $-\mathbf{A}$. It can also be shown that positive definite and negative definite matrices are always invertible.

In Section 7.4.3.1, we show that a symmetric matrix is positive definite iff its eigenvalues are positive. Note that if all elements of $\mathbf{A}$are positive, it does not mean$\mathbf{A}$is necessarily positive definite. For example,$\mathbf{A} = \begin{pmatrix} 4 & 3 \\ 3 & 2 \end{pmatrix}$is not positive definite. Conversely, a positive definite matrix can have negative entries e.g.,$\mathbf{A} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$

A sufficient condition for a (real, symmetric) matrix to be positive definite is that it is diagonally dominant, i.e., if in every row of the matrix, the magnitude of the diagonal entry in that row is

---

larger than the sum of the magnitudes of all the other (non-diagonal) entries in that row. More precisely,

$$
|a_{ii}|>\sum_{j\neq i}|a_{ij}|\quad for all i   \tag*{(7.58)}
$$

In 2d, any real, symmetric  $2 \times 2$ matrix  $\begin{pmatrix} a & b \\ b & d \end{pmatrix}$ is positive definite iff a > 0, d > 0 and ad > b^2.

Finally, there is one type of positive definite matrix that comes up frequently, and so deserves some special mention. Given any matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ (not necessarily symmetric or even square), the  $\mathbf{G}\mathbf{a}\mathbf{m}\mathbf{a}\mathbf{t}\mathbf{r}\mathbf{i}\mathbf{x}\mathbf{G} = \mathbf{A}^{\top}\mathbf{A}$ is always positive semidefinite. Further, if  $m \geq n$ (and we assume for convenience that  $\mathbf{A}$ is full rank), then  $\mathbf{G} = \mathbf{A}^{\top}\mathbf{A}$ is positive definite.

##### 7.1.5.4 Orthogonal matrices

Two vectors  $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$ are orthogonal if  $\boldsymbol{x}^\top \boldsymbol{y} = 0$. A vector  $\boldsymbol{x} \in \mathbb{R}^n$ is normalized if  $\|\boldsymbol{x}\|_2 = 1$. A set of vectors that is pairwise orthogonal and normalized is called  $\text{orthonormal}$. A square matrix  $\mathbf{U} \in \mathbb{R}^{n \times n}$ is  $\text{orthogonal}$ if all its columns are  $\text{orthonormal}$. (Note the different meaning of the term  $\text{orthogonal}$ when talking about vectors versus matrices.) If the entries of  $\mathbf{U}$ are complex valued, we use the term  $\text{unitary}$ instead of  $\text{orthogonal}$.

It follows immediately from the definition of orthogonality and normality that U is orthogonal iff

$$
\mathbf{U}^{\mathsf{T}}\mathbf{U}=\mathbf{I}=\mathbf{U}\mathbf{U}^{\mathsf{T}}.   \tag*{(7.59)}
$$

In other words, the inverse of an orthogonal matrix is its transpose. Note that if $\mathbf{U}$is not square — i.e.,$\mathbf{U} \in \mathbb{R}^{m \times n}$, $n < m$— but its columns are still orthonormal, then$\mathbf{U}^\top \mathbf{U} = \mathbf{I}$, but $\mathbf{U} \mathbf{U}^\top \neq \mathbf{I}$. We generally only use the term orthogonal to describe the previous case, where $\mathbf{U}$is square.

An example of an orthogonal matrix is a rotation matrix (see Exercise 7.1). For example, a rotation in 3d by angle$ \alpha $ about the z axis is given by

$$
\mathbf{R}(\alpha)=\begin{pmatrix}{{{\cos(\alpha)}}}&{{{-\sin(\alpha)}}}&{{{0}}} \\{{{\sin(\alpha)}}}&{{{\cos(\alpha)}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{pmatrix}   \tag*{(7.60)}
$$

If  $\alpha = 45^{\circ}$, this becomes

$$
\mathbf{R}(45)=\begin{pmatrix}{{{\frac{1}{\sqrt{2}}}}}&{{{-\frac{1}{\sqrt{2}}}}}&{{{0}}} \\{{{\frac{1}{\sqrt{2}}}}}&{{{\frac{1}{\sqrt{2}}}}}&{{{0}}} \\{{{0}}}&{{{0}}}&{{{1}}}\end{pmatrix}   \tag*{(7.61)}
$$

where  $\frac{1}{\sqrt{2}} = 0.7071$. We see that  $\mathbf{R}(-\alpha) = \mathbf{R}(\alpha)^{-1} = \mathbf{R}(\alpha)^{\top}$, so this is an orthogonal matrix.

One nice property of orthogonal matrices is that operating on a vector with an orthogonal matrix will not change its Euclidean norm, i.e.,

$$
\left\| \mathbf{U} \mathbf{x} \right\|_{2}=\left\| \mathbf{x} \right\|_{2}   \tag*{(7.62)}
$$

for any nonzero  $x \in \mathbb{R}^n$, and orthogonal  $\mathbf{U} \in \mathbb{R}^{n \times n}$.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

Similarly, one can show that the angle between two vectors is preserved after they are transformed by an orthogonal matrix. The cosine of the angle between x and y is given by

$$
\cos(\alpha(\boldsymbol{x},\boldsymbol{y}))=\frac{\boldsymbol{x}^{\top}\boldsymbol{y}}{\left|\left|\boldsymbol{x}\right|\right|\left|\boldsymbol{y}\right|}   \tag*{(7.63)}
$$

so

$$
\cos(\alpha(\mathbf{U}\boldsymbol{x},\mathbf{U}\boldsymbol{y}))=\frac{(\mathbf{U}\boldsymbol{x})^{\top}(\mathbf{U}\boldsymbol{y})}{||\mathbf{U}\boldsymbol{x}||||\mathbf{U}\boldsymbol{y}||}=\frac{\boldsymbol{x}^{\top}\boldsymbol{y}}{||\boldsymbol{x}||||\boldsymbol{y}||}=\cos(\alpha(\boldsymbol{x},\boldsymbol{y}))   \tag*{(7.64)}
$$

In summary, transformations by orthogonal matrices are generalizations of rotations (if  $\det(\mathbf{U})=1$) and reflections (if  $\det(\mathbf{U})=-1$), since they preserve lengths and angles.

Note that there is a technique called Gram Schmidt orthogonalization which is a way to make any square matrix orthogonal, but we will not cover it here.

### 7.2 Matrix multiplication

The product of two matrices  $\mathbf{A} \in \mathbb{R}^{m \times n}$ and  $\mathbf{B} \in \mathbb{R}^{n \times p}$ is the matrix

$$
\mathbf{C}=\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times p},   \tag*{(7.65)}
$$

where

$$
C_{i j}=\sum_{k=1}^{n}A_{i k}B_{k j}.   \tag*{(7.66)}
$$

Note that in order for the matrix product to exist, the number of columns in A must equal the number of rows in B.

Matrix multiplication generally takes  $O(mnp)$ time, although faster methods exist. In addition, specialized hardware, such as GPUs and TPUs, can be leveraged to speed up matrix multiplication significantly, by performing operations across the rows (or columns) in parallel.

It is useful to know a few basic properties of matrix multiplication:

• Matrix multiplication is associative:  $(AB)C = A(BC)$.

• Matrix multiplication is distributive:  $\mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}$.

• Matrix multiplication is, in general, not commutative; that is, it can be the case that AB ≠ BA.

(In each of the above cases, we are assuming that the dimensions match.)

There are many important special cases of matrix multiplication, as we discuss below.

#### 7.2.1 Vector-vector products

Given two vectors  $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^n$, the quantity  $\boldsymbol{x}^\top \boldsymbol{y}$, called the inner product, dot product or scalar product of the vectors, is a real number given by

$$
\langle\boldsymbol{x},\boldsymbol{y}\rangle\triangleq\boldsymbol{x}^{\top}\boldsymbol{y}=\sum_{i=1}^{n}x_{i}y_{i}.   \tag*{(7.67)}
$$


---

Note that it is always the case that  $x^{\top}y = y^{\top}x$.

Given vectors  $\boldsymbol{x} \in \mathbb{R}^m$,  $\boldsymbol{y} \in \mathbb{R}^n$ (they no longer have to be the same size),  $\boldsymbol{x}\boldsymbol{y}^\top$ is called the outer product of the vectors. It is a matrix whose entries are given by  $(\boldsymbol{x}\boldsymbol{y}^\top)_{ij} = x_i y_j$, i.e.,

$$
\boldsymbol{x}\boldsymbol{y}^{\top}\in\mathbb{R}^{m\times n}=\left[\begin{array}{c c c c}x_{1}y_{1}&x_{1}y_{2}&\cdots&x_{1}y_{n}\\ x_{2}y_{1}&x_{2}y_{2}&\cdots&x_{2}y_{n}\\ \vdots&\vdots&\ddots&\vdots\\ x_{m}y_{1}&x_{m}y_{2}&\cdots&x_{m}y_{n}\end{array}\right].   \tag*{(7.68)}
$$

#### 7.2.2 Matrix-vector products

Given a matrix  $\mathbf{A} \in \mathbb{R}^{m \times n}$ and a vector  $\mathbf{x} \in \mathbb{R}^n$, their product is a vector  $\mathbf{y} = \mathbf{A}\mathbf{x} \in \mathbb{R}^m$. There are a couple of ways of looking at matrix-vector multiplication, and we will look at them both.

If we write A by rows, then we can express y = Ax as follows:

$$
\boldsymbol{y}=\mathbf{A}\boldsymbol{x}=\left[\begin{array}{ccc}-\quad\boldsymbol{a}_{1}^{\top}&-\quad\\-\quad\boldsymbol{a}_{2}^{\top}&-\quad\\\vdots&\quad\\\quad-\quad\boldsymbol{a}_{m}^{\top}&-\quad\end{array}\right]\boldsymbol{x}=\left[\begin{array}{c}\boldsymbol{a}_{1}^{\top}\boldsymbol{x}\\\boldsymbol{a}_{2}^{\top}\boldsymbol{x}\\\vdots\\\boldsymbol{a}_{m}^{\top}\boldsymbol{x}\\\end{array}\right].   \tag*{(7.69)}
$$

In other words, the  $i$th entry of  $\mathbf{y}$ is equal to the inner product of the  $i$th row of  $\mathbf{A}$ and  $\mathbf{x}$,  $y_i = \mathbf{a}_i^\top \mathbf{x}$. Alternatively, let's write  $\mathbf{A}$ in column form. In this case we see that

$$
\begin{aligned}\boldsymbol{y}&=\mathbf{A}\boldsymbol{x}=\left[\begin{array}{ccc}\mid&&\mid\\ \boldsymbol{a}_{1}&\boldsymbol{a}_{2}&\cdots&\boldsymbol{a}_{n}\\\mid&&\mid&\end{array}\right]\left|\begin{array}{c}x_{1}\\x_{2}\\\vdots\\x_{n}\end{array}\right|=\left[\begin{array}{c}\mid\\ \boldsymbol{a}_{1}\\ \mid\end{array}\right]x_{1}+\left[\begin{array}{c}\mid\\ \boldsymbol{a}_{2}\\ \mid\end{array}\right]x_{2}+\cdots+\left[\begin{array}{c}\mid\\ \boldsymbol{a}_{n}\\ \mid\end{array}\right]x_{n}.\end{aligned}   \tag*{(7.70)}
$$

In other words, y is a linear combination of the columns of A, where the coefficients of the linear combination are given by the entries of x. We can view the columns of A as a set of basis vectors defining a linear subspace. We can construct vectors in this subspace by taking linear combinations of the basis vectors. See Section 7.1.2 for details.

#### 7.2.3 Matrix-matrix products

Below we look at four different (but, of course, equivalent) ways of viewing the matrix-matrix multiplication C = AB.

First we can view matrix-matrix multiplication as a set of vector-vector products. The most obvious viewpoint, which follows immediately from the definition, is that the i,j entry of C is equal to the inner product of the ith row of A and the jth column of B. Symbolically, this looks like the following,

$$
\mathbf{C}=\mathbf{A}\mathbf{B}=\left[\begin{array}{ccc}-\quad a_{1}^{\top}&-\quad\\-\quad a_{2}^{\top}&-\quad\\\quad\vdots&\\\quad-a_{m}^{\top}&-\quad\end{array}\right]\left[\begin{array}{ccc}\mid&|\quad&|\\b_{1}&b_{2}&\cdots&b_{p}\\\mid&|\quad&|\end{array}\right]=\left[\begin{array}{cccc}a_{1}^{\top}b_{1}&a_{1}^{\top}b_{2}&\cdots&a_{1}^{\top}b_{p}\\a_{2}^{\top}b_{1}&a_{2}^{\top}b_{2}&\cdots&a_{2}^{\top}b_{p}\\\vdots&\vdots&\ddots&\vdots\\a_{m}^{\top}b_{1}&a_{m}^{\top}b_{2}&\cdots&a_{m}^{\top}b_{p}\end{array}\right].   \tag*{(7.71)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_461_118_676_326.jpg" alt="Image" width="18%" /></div>

<div style="text-align: center;">Figure 7.5: Illustration of matrix multiplication. From https://en.wikipedia.org/wiki/Matrix_multiplication. Used with kind permission of Wikipedia author Bilou.</div>

Remember that since  $\mathbf{A} \in \mathbb{R}^{m \times n}$ and  $\mathbf{B} \in \mathbb{R}^{n \times p}$,  $\mathbf{a}_i \in \mathbb{R}^n$ and  $\mathbf{b}_j \in \mathbb{R}^n$, so these inner products all make sense. This is the most “natural” representation when we represent  $\mathbf{A}$ by rows and  $\mathbf{B}$ by columns. See Figure 7.5 for an illustration.

Alternatively, we can represent A by columns, and B by rows, which leads to the interpretation of AB as a sum of outer products. Symbolically,

$$
\mathbf{C}=\mathbf{A}\mathbf{B}=\left[\begin{array}{ccc}\mid&&\mid\\a_{1}&a_{2}&\cdots&a_{n}\\\mid&&\mid&\end{array}\right]\left[\begin{array}{ccc}-\quad b_{1}^{\top}&-\quad\\-\quad b_{2}^{\top}&-\quad\\\vdots&\quad\\\quad\vdots&\quad\\-\quad b_{n}^{\top}&-\end{array}\right]=\sum_{i=1}^{n}a_{i}b_{i}^{\top}.   \tag*{(7.72)}
$$

Put another way,  $\mathbf{A}\mathbf{B}$ is equal to the sum, over all  $i$, of the outer product of the  $i$th column of  $\mathbf{A}$ and the  $i$th row of  $\mathbf{B}$. Since, in this case,  $\mathbf{a}_i \in \mathbb{R}^m$ and  $\mathbf{b}_i \in \mathbb{R}^p$, the dimension of the outer product  $\mathbf{a}_i \mathbf{b}_i^\top$ is  $m \times p$, which coincides with the dimension of  $\mathbf{C}$.

We can also view matrix-matrix multiplication as a set of matrix-vector products. Specifically, if we represent B by columns, we can view the columns of C as matrix-vector products between A and the columns of B. Symbolically,

$$
\mathbf{C}=\mathbf{A}\mathbf{B}=\mathbf{A}\left[\begin{array}{ccc}\mid&\mid&\\\mathbf{b}_{1}&\mathbf{b}_{2}&\cdots\\\mid&&\mid\end{array}\right.\mathbf{\Lambda}\mathbf{\Lambda}\mathbf{\Lambda}\mathbf{\Lambda}_{p}=\left[\begin{array}{ccc}\mid&\mid&\\\mathbf{A}\mathbf{b}_{1}&\mathbf{A}\mathbf{b}_{2}&\cdots\\\mid&&\mid\end{array}\right.\mathbf{\Lambda}\mathbf{\Lambda}\mathbf{\Lambda}_{p}\mathbf{\Lambda}\mathbf{\Lambda}.   \tag*{(7.73)}
$$

Here the ith column of C is given by the matrix-vector product with the vector on the right,  $c_i = A b_i$. These matrix-vector products can in turn be interpreted using both viewpoints given in the previous subsection.

Finally, we have the analogous viewpoint, where we represent  $\mathbf{A}$ by rows, and view the rows of  $\mathbf{C}$ as the matrix-vector product between the rows of  $\mathbf{A}$ and the matrix  $\mathbf{B}$. Symbolically,

$$
\mathbf{C}=\mathbf{A}\mathbf{B}=\left[\begin{array}{ccc}-\quad a_{1}^{\top}&-\quad\\-\quad a_{2}^{\top}&-\quad\\\quad\vdots&\\\quad\vdots&\\\quad a_{m}^{\top}&-\quad\end{array}\right]\mathbf{B}=\left[\begin{array}{ccc}-\quad a_{1}^{\top}\mathbf{B}&-\quad\\-\quad a_{2}^{\top}\mathbf{B}&-\quad\\\quad\vdots&\\\quad\vdots&\\\quad a_{m}^{\top}\mathbf{B}&-\quad\end{array}\right].   \tag*{(7.74)}
$$


---

Here the ith row of C is given by the matrix-vector product with the vector on the left

It may seem like overkill to dissect matrix multiplication to such a large degree, especially when all these viewpoints follow immediately from the initial definition we gave (in about a line of math) at the beginning of this section. However, virtually all of linear algebra deals with matrix multiplications of some kind, and it is worthwhile to spend some time trying to develop an intuitive understanding of the viewpoints presented here.

Finally, a word on notation. We write  $\mathbf{A}^2$ as shorthand for  $\mathbf{A}\mathbf{A}$, which is the matrix product. To denote elementwise squaring of the elements of a matrix, we write  $\mathbf{A}^{\odot 2} = [A_{ij}^2]$. (If  $\mathbf{A}$ is diagonal, then  $\mathbf{A}^2 = \mathbf{A}^{\odot 2}$.)

We can also define the inverse of  $A^2$ using the matrix square root: we say  $A = \sqrt{M}$ if  $A^2 = M$. To denote elementwise square root of the elements of a matrix, we write  $[\sqrt{M_{ij}}]$.

#### 7.2.4 Application: manipulating data matrices

As an application of the above results, consider the case where  $\mathbf{X}$ is the  $N \times D$ design matrix, whose rows are the data cases. There are various common preprocessing operations that we apply to this matrix, which we summarize below. (Writing these operations in matrix form is useful because it is notationally compact, and it allows us to implement the methods quickly using fast matrix code.)

##### 7.2.4.1 Summing slices of the matrix

Suppose X is an  $N \times D$ matrix. We can sum across the rows by premultiplying by a  $1 \times N$ matrix of ones to create a  $1 \times D$ matrix:

$$
\mathbf{1}_{N}^{\mathsf{T}}\mathbf{X}=\left(\sum_{n}x_{n1}\quad\cdots\quad\sum_{n}x_{nD}\right)   \tag*{(7.75)}
$$

Hence the mean of the data vectors is given by

$$
\overline{{\boldsymbol{x}}}^{\mathsf{T}}=\frac{1}{N}\mathbf{1}_{N}^{\mathsf{T}}\mathbf{X}   \tag*{(7.76)}
$$

We can sum across the columns by postmultiplying by a  $D \times 1$ matrix of ones to create a  $N \times 1$ matrix:

$$
\mathbf{X1}_{D}=\begin{pmatrix}\sum_{d}x_{1d}\\ \vdots\\ \sum_{d}x_{Nd}\end{pmatrix}   \tag*{(7.77)}
$$

We can sum all entries in a matrix by pre and post multiplying by a vector of 1s:

$$
\mathbf{1}_{N}^{\top}\mathbf{X}\mathbf{1}_{D}=\sum_{ij}X_{ij}   \tag*{(7.78)}
$$

Hence the overall mean is given by

$$
\overline{x}=\frac{1}{ND}\mathbf{1}_{N}^{\top}\mathbf{X}\mathbf{1}_{D}   \tag*{(7.79)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

##### 7.2.4.2 Scaling rows and columns of a matrix

We often want to scale rows or columns of a data matrix (e.g., to standardize them). We now show how to write this in matrix notation.

If we pre-multiply  $\mathbf{X}$ by a diagonal matrix  $\mathbf{S} = \mathrm{diag}(\mathbf{s})$, where  $\mathbf{s}$ is an  $N$-vector, then we just scale each row of  $\mathbf{X}$ by the corresponding scale factor in  $\mathbf{s}$:

$$
\mathrm{diag}(\boldsymbol{s})\boldsymbol{X}=\begin{pmatrix}{{{s_{1}}}}&{{{\cdots}}}&{{{0}}} \\{{{\ddots}}} \\{{{0}}}&{{{\cdots}}}&{{{s_{N}}}}\end{pmatrix}\begin{pmatrix}{{{x_{1,1}}}}&{{{\cdots}}}&{{{x_{1,D}}}} \\{{{\ddots}}} \\{{{x_{N,1}}}}&{{{\cdots}}}&{{{x_{N,D}}}}\end{pmatrix}=\begin{pmatrix}{{{s_{1}x_{1,1}}}}&{{{\cdots}}}&{{{s_{1}x_{1,D}}}} \\{{{\ddots}}} \\{{{s_{N}x_{N,1}}}}&{{{\cdots}}}&{{{s_{N}x_{N,D}}}}\end{pmatrix}   \tag*{(7.80)}
$$

If we post-multiply  $\mathbf{X}$ by a diagonal matrix  $\mathbf{S} = \mathrm{diag}(\mathbf{s})$, where  $\mathbf{s}$ is a  $D$-vector, then we just scale each column of  $\mathbf{X}$ by the corresponding element in  $\mathbf{s}$.

$$
\mathbf{X}\mathrm{diag}(\boldsymbol{s})=\begin{pmatrix}{{{x_{1,1}}}}&{{{\cdots}}}&{{{x_{1,D}}}} \\{{{\ddots}}} \\{{{x_{N,1}}}}&{{{\cdots}}}&{{{x_{N,D}}}}\end{pmatrix}\begin{pmatrix}{{{s_{1}}}}&{{{\cdots}}}&{{{0}}} \\{{{\ddots}}} \\{{{0}}}&{{{\cdots}}}&{{{s_{D}}}}\end{pmatrix}=\begin{pmatrix}{{{s_{1}x_{1,1}}}}&{{{\cdots}}}&{{{s_{D}x_{1,D}}}} \\{{{\ddots}}} \\{{{s_{1}x_{N,1}}}}&{{{\cdots}}}&{{{s_{D}x_{N,D}}}}\end{pmatrix}   \tag*{(7.81)}
$$

Thus we can rewrite the standardization operation from Section 10.2.8 in matrix form as follows:

$$
\mathrm{standardize}(\mathbf{X})=(\mathbf{X}-\mathbf{1}_{N}\boldsymbol{\mu}^{T})\mathrm{diag}(\boldsymbol{\sigma})^{-1}   \tag*{(7.82)}
$$

where  $\mu = \overline{x}$ is the empirical mean, and  $\sigma$ is a vector of the empirical standard deviations.

##### 7.2.4.3 Sum of squares and scatter matrix

The sum of squares matrix is  $D \times D$ matrix defined by

$$
\mathbf{S}_{0}\triangleq\mathbf{X}^{\top}\mathbf{X}=\sum_{n=1}^{N}\mathbf{x}_{n}\mathbf{x}_{n}^{\top}=\sum_{n=1}^{N}\begin{pmatrix}x_{n,1}^{2}&\cdots&x_{n,1}x_{n,D}\\ &\ddots&\\ x_{n,D}x_{n,1}&\cdots&x_{n,D}^{2}\end{pmatrix}   \tag*{(7.83)}
$$

The scatter matrix is a  $D \times D$ matrix defined by

$$
\mathbf{S}_{\overline{\mathbf{x}}}\triangleq\sum_{n=1}^{N}(\mathbf{x}_{n}-\overline{\mathbf{x}})(\mathbf{x}_{n}-\overline{\mathbf{x}})^{\top}=\left(\sum_{n}\mathbf{x}_{n}\mathbf{x}_{n}^{\top}\right)-N\overline{\mathbf{x}}\overline{\mathbf{x}}^{\top}   \tag*{(7.84)}
$$

We see that this is the sum of squares matrix applied to the mean-centered data. More precisely, define  $\tilde{\mathbf{X}}$ to be a version of  $\mathbf{X}$ where we subtract the mean  $\overline{\mathbf{x}} = \frac{1}{N} \mathbf{X}^\top \mathbf{1}_N$ off every row. Hence we can compute the centered data matrix using

$$
\tilde{\mathbf{X}}=\mathbf{X}-\mathbf{1}_{N}\overline{\mathbf{x}}^{\mathsf{T}}=\mathbf{X}-\frac{1}{N}\mathbf{1}_{N}\mathbf{1}_{N}^{\mathsf{T}}\mathbf{X}=\mathbf{C}_{N}\mathbf{X}   \tag*{(7.85)}
$$

where

$$
\mathbf{C}_{N}\triangleq\mathbf{I}_{N}-\frac{1}{N}\mathbf{J}_{N}   \tag*{(7.86)}
$$


---

is the centering matrix, and  $\mathbf{J}_N = \mathbf{1}_N \mathbf{1}_N^\top$ is a matrix of all 1s. The scatter matrix can now be computed as follows:

$$
\mathbf{S}_{\overline{{x}}}=\tilde{\mathbf{X}}^{\top}\tilde{\mathbf{X}}=\mathbf{X}^{\top}\mathbf{C}_{N}^{\top}\mathbf{C}_{N}\mathbf{X}=\mathbf{X}^{\top}\mathbf{C}_{N}\mathbf{X}   \tag*{(7.87)}
$$

where we exploited the fact that  $\mathbf{C}_N$ is symmetric and idempotent, i.e.,  $\mathbf{C}_N^k = \mathbf{C}_N$ for  $k = 1, 2, \ldots$ (since once we subtract the mean, subtracting it again has no effect).

##### 7.2.4.4 Gram matrix

The  $N \times N$ matrix  $XX^{\top}$ is a matrix of inner products called the Gram matrix:

$$
\mathbf{K}\triangleq\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}\boldsymbol{x}_{1}^{\top}\boldsymbol{x}_{1}&\cdots&\boldsymbol{x}_{1}^{\top}\boldsymbol{x}_{N}\\ &\ddots&\\ \boldsymbol{x}_{n}^{\top}\boldsymbol{x}_{1}&\cdots&\boldsymbol{x}_{N}^{\top}\boldsymbol{x}_{N}\end{pmatrix}   \tag*{(7.88)}
$$

Sometimes we want to compute the inner products of the mean-centered data vectors,  $\mathbf{\tilde{K}} = \mathbf{\tilde{X}} \mathbf{\tilde{X}}^T$. However, if we are working with a feature similarity matrix instead of raw features, we will only have access to  $\mathbf{K}$, not  $\mathbf{X}$. (We will see examples of this in Section 20.4.4 and Section 20.4.6.) Fortunately, we can compute  $\mathbf{\tilde{K}}$ from  $\mathbf{K}$ using the double centering trick:

$$
\tilde{\mathbf{K}}=\tilde{\mathbf{X}}\tilde{\mathbf{X}}^{\mathsf{T}}=\mathbf{C}_{N}\mathbf{K}\mathbf{C}_{N}=\mathbf{K}-\frac{1}{N}\mathbf{J}\mathbf{K}-\frac{1}{N}\mathbf{K}\mathbf{J}+\frac{1}{N^{2}}\mathbf{1}^{\mathsf{T}}\mathbf{K}\mathbf{1}   \tag*{(7.89)}
$$

This subtracts the row means and column means from  $\mathbf{K}$, and adds back the global mean that gets subtracted twice, so that both row means and column means of  $\tilde{\mathbf{K}}$ are equal to zero.

To see why Equation  $(7.89)$ is true, consider the scalar form:

$$
\begin{aligned}\tilde{K}_{ij}&=\tilde{\boldsymbol{x}}_{i}^{\top}\tilde{\boldsymbol{x}}_{j}=(\boldsymbol{x}_{i}-\frac{1}{N}\sum_{k=1}^{N}\boldsymbol{x}_{k})(\boldsymbol{x}_{j}-\frac{1}{N}\sum_{l=1}^{N}\boldsymbol{x}_{l})\\&=\boldsymbol{x}_{i}^{\top}\boldsymbol{x}_{j}-\frac{1}{N}\sum_{k=1}^{N}\boldsymbol{x}_{i}^{\top}\boldsymbol{x}_{k}-\frac{1}{N}\sum_{k=1}^{N}\boldsymbol{x}_{j}^{\top}\boldsymbol{x}_{k}+\frac{1}{N^{2}}\sum_{k=1}^{N}\sum_{l=1}^{N}\boldsymbol{x}_{k}^{\top}\boldsymbol{x}_{l}\end{aligned}   \tag*{(7.91)}
$$

##### 7.2.4.5 Distance matrix

Let  $\mathbf{X}$ be  $N_x \times D$ datamatrix, and  $\mathbf{Y}$ be another  $N_y \times D$ datamatrix. We can compute the squared pairwise distances between these using

$$
\mathbf{D}_{ij}=(\boldsymbol{x}_{i}-\boldsymbol{y}_{j})^{\mathrm{T}}(\boldsymbol{x}_{i}-\boldsymbol{y}_{j})=||\boldsymbol{x}_{i}||^{2}-2\boldsymbol{x}_{i}^{\mathrm{T}}\boldsymbol{y}_{j}+||\boldsymbol{y}_{j}||^{2}   \tag*{(7.92)}
$$

Let us now write this in matrix form. Let  $\hat{\mathbf{x}} = [||\mathbf{x}_1||^2; \cdots; ||\mathbf{x}_{N_x}||^2] = \text{diag}(\mathbf{X}\mathbf{X}^\top)$ be a vector where each element is the squared norm of the examples in  $\mathbf{X}$, and define  $\hat{\mathbf{y}}$ similarly. Then we have

$$
\mathbf{D}=\hat{\mathbf{x}}\mathbf{1}_{N_{y}}^{\mathsf{T}}-2\mathbf{X}\mathbf{Y}^{\mathsf{T}}+\mathbf{1}_{N_{x}}\hat{\mathbf{y}}^{\mathsf{T}}   \tag*{(7.93)}
$$

In the case that  $\mathbf{X} = \mathbf{Y}$, we have

$$
\mathbf{D}=\hat{\mathbf{x}}\mathbf{1}_{N}^{\top}-2\mathbf{X}\mathbf{X}^{\top}+\mathbf{1}_{N}\hat{\mathbf{x}}^{\top}   \tag*{(7.94)}
$$

This vectorized computation is often much faster than using for loops.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 7.2.5 Kronecker products *

If  $\mathbf{A}$ is an  $m \times n$ matrix and  $\mathbf{B}$ is a  $p \times q$ matrix, then the Kronecker product  $\mathbf{A} \otimes \mathbf{B}$ is the  $mp \times nq$ block matrix

$$
\mathbf{A}\otimes\mathbf{B}=\begin{bmatrix}a_{11}\mathbf{B}&\cdots&a_{1n}\mathbf{B}\\ \vdots&\ddots&\vdots\\ a_{m1}\mathbf{B}&\cdots&a_{mn}\mathbf{B}\end{bmatrix}   \tag*{(7.95)}
$$

For example,

$$
\begin{bmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\\ a_{31}&a_{32}\end{bmatrix}\otimes\begin{bmatrix}b_{11}&b_{12}&b_{13}\\ b_{21}&b_{22}&b_{23}\end{bmatrix}=\begin{bmatrix}a_{11}b_{11}&a_{11}b_{12}&a_{11}b_{13}&a_{12}b_{11}&a_{12}b_{12}&a_{12}b_{13}\\ a_{11}b_{21}&a_{11}b_{22}&a_{11}b_{23}&a_{12}b_{21}&a_{12}b_{22}&a_{12}b_{23}\\ a_{21}b_{11}&a_{21}b_{12}&a_{21}b_{13}&a_{22}b_{11}&a_{22}b_{12}&a_{22}b_{13}\\ a_{21}b_{21}&a_{21}b_{22}&a_{21}b_{23}&a_{22}b_{21}&a_{22}b_{22}&a_{22}b_{23}\\ a_{31}b_{11}&a_{31}b_{12}&a_{31}b_{13}&a_{32}b_{11}&a_{32}b_{12}&a_{32}b_{13}\\ a_{31}b_{21}&a_{31}b_{22}&a_{31}b_{23}&a_{32}b_{21}&a_{32}b_{22}&a_{32}b_{23}\end{bmatrix}   \tag*{(7.96)}
$$

Here are some useful identities:

$$
\left(\mathbf{A}\otimes\mathbf{B}\right)^{-1}=\mathbf{A}^{-1}\otimes\mathbf{B}^{-1}   \tag*{(7.97)}
$$

$$
(\mathbf{A}\otimes\mathbf{B})\mathrm{vec}(\mathbf{C})=\mathrm{vec}(\mathbf{B}\mathbf{C}\mathbf{A}^{\mathrm{T}})   \tag*{(7.98)}
$$

where  $\text{vec}(\mathbf{M})$ stacks the columns of  $\mathbf{M}$. (If we stack along the rows, we get  $(\mathbf{A} \otimes \mathbf{B})\text{vec}(\mathbf{C}) = \text{vec}(\mathbf{ACB}^\top$.) See [Loa00] for a list of other useful properties.

#### 7.2.6 Einstein summation *

Einstein summation, or einsum for short, is a notational shortcut for working with tensors. The convention was introduced by Einstein [Ein16, sec 5], who later joked to a friend, “I have made a great discovery in mathematics; I have suppressed the summation sign every time that the summation must be made over an index which occurs twice…” [Pai05, p.216]. For example, instead of writing matrix multiplication as  $C_{ij} = \sum_k A_{ik} B_{kj}$, we can just write it as  $C_{ij} = A_{ik} B_{kj}$, where we drop the  $\sum_k$.

As a more complex example, suppose we have a 3d tensor  $S_{ntk}$ where n indexes examples in the batch, t indexes locations in the sequence, and k indexes words in a one-hot representation. Let  $W_{kd}$ be an embedding matrix that maps sparse one-hot vectors  $R^k$ to dense vectors in  $R^d$. We can convert the batch of sequences of one-hot to a batch of sequences of embeddings as follows:

$$
E_{n t d}=\sum_{k}S_{n t k}W_{k d}   \tag*{(7.99)}
$$

We can compute the sum of the embedding vectors for each sequence (to get a global representation of each bag of words) as follows:

$$
E_{nd}=\sum_{k}\sum_{t}S_{ntk}W_{kd}   \tag*{(7.100)}
$$


---

Finally we can pass each sequence's vector representation through another linear transform  $V_{dc}$ to map to the logits over a classifier with c labels:

$$
L_{nc}=\sum_{d}E_{nd}V_{dc}=\sum_{d}\sum_{k}\sum_{t}S_{ntk}W_{kd}V_{dc}   \tag*{(7.101)}
$$

In einsum notation, we write  $L_{nc} = S_{ntk} W_{kd} V_{dc}$. We sum over k and d because those indices occur twice on the RHS. We sum over t because that index does not occur on the LHS.

Einsum is implemented in NumPy, Tensorflow, PyTorch, etc. What makes it particularly useful is that it can perform the relevant tensor multiplications in complex expressions in an optimal order, so as to minimize time and intermediate memory allocation. $^{2}$ The library is best illustrated by the examples in einsum_demo.ipynb.

Note that the speed of einsum depends on the order in which the operations are performed, which depends on the shapes of the relevant arguments. The optimal ordering minimizes the treewidth of the resulting computation graph, as explained in [GASG18]. In general, the time to compute the optimal ordering is exponential in the number of arguments, so it is common to use a greedy approximation. However, if we expect to repeat the same calculation many times, using tensors of the same shape but potentially different content, we can compute the optimal ordering once and reuse it multiple times.

### 7.3 Matrix inversion

In this section, we discuss how to invert different kinds of matrices.

#### 7.3.1 The inverse of a square matrix

The inverse of a square matrix  $\mathbf{A} \in \mathbb{R}^{n \times n}$ is denoted  $\mathbf{A}^{-1}$, and is the unique matrix such that

$$
\mathbf{A}^{-1}\mathbf{A}=\mathbf{I}=\mathbf{A}\mathbf{A}^{-1}.   \tag*{(7.102)}
$$

Note that  $A^{-1}$ exists if and only if  $\det(\mathbf{A}) \neq 0$. If  $\det(\mathbf{A}) = 0$, it is called a  $\text{singular matrix}$. The following are properties of the inverse; all assume that  $A, B \in \mathbb{R}^{n \times n}$ are non-singular:

$$
\left(\mathbf{A}^{-1}\right)^{-1}=\mathbf{A}   \tag*{(7.103)}
$$

$$
\left(\mathbf{A}\mathbf{B}\right)^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}   \tag*{(7.104)}
$$

$$
(\mathbf{A}^{-1})^{\mathsf{T}}=(\mathbf{A}^{\mathsf{T}})^{-1}\triangleq\mathbf{A}^{-T}   \tag*{(7.105)}
$$

For the case of a 2 × 2 matrix, the expression for A−1 is simple enough to give explicitly. We have

$$
\mathbf{A}=\begin{pmatrix}{{{a}}}&{{{b}}} \\{{{c}}}&{{{d}}}\end{pmatrix},\mathbf{A}^{-1}=\frac{1}{|\mathbf{A}|}\begin{pmatrix}{{{d}}}&{{{-b}}} \\{{{-c}}}&{{{a}}}\end{pmatrix}   \tag*{(7.106)}
$$

For a block diagonal matrix, the inverse is obtained by simply inverting each block separately, e.g.,

$$
\begin{pmatrix}\mathbf{A}&\mathbf{0}\\\mathbf{0}&\mathbf{B}\end{pmatrix}^{-1}=\begin{pmatrix}\mathbf{A}^{-1}&\mathbf{0}\\\mathbf{0}&\mathbf{B}^{-1}\end{pmatrix}   \tag*{(7.107)}
$$

2. These optimizations are implemented in the opt-einsum library [GASG18]. Its core functionality is included in NumPy and JAX einsum functions, provided you set optimize=True parameter.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 7.3.2 Schur complements  $*$

In this section, we review some useful results concerning block structured matrices.

Theorem 7.3.1 (Inverse of a partitioned matrix). Consider a general partitioned matrix

$$
\mathbf{M}=\begin{pmatrix}\mathbf{E}&\mathbf{F}\\ \mathbf{G}&\mathbf{H}\end{pmatrix}   \tag*{(7.108)}
$$

where we assume E and H are invertible. We have

$$
\begin{aligned}\mathbf{M}^{-1}&=\begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1}&-(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\\-\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}&\mathbf{H}^{-1}+\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\end{pmatrix}\\&=\begin{pmatrix}\mathbf{E}^{-1}+\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&-\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\\-(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&(\mathbf{M}/\mathbf{E})^{-1}\end{pmatrix}\end{aligned}   \tag*{(7.109)}
$$

where

$$
\mathbf{M}/\mathbf{H}\triangleq\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}   \tag*{(7.111)}
$$

$$
\mathbf{M}/\mathbf{E}\triangleq\mathbf{H}-\mathbf{G}\mathbf{E}^{-1}\mathbf{F}   \tag*{(7.112)}
$$

We say that M/H is the Schur complement of M wrt H, and M/E is the Schur complement of M wrt E.

Equation (7.109) and Equation (7.110) are called the partitioned inverse formulae.

Proof. If we could block diagonalize M, it would be easier to invert. To zero out the top right block of M we can pre-multiply as follows

$$
\begin{pmatrix}{{{\mathbf{I}}}}&{{{-\mathbf{F}\mathbf{H}^{-1}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{I}}}}\end{pmatrix}\begin{pmatrix}{{{\mathbf{E}}}}&{{{\mathbf{F}}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}=\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{0}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}   \tag*{(7.113)}
$$

Similarly, to zero out the bottom left we can post-multiply as follows

$$
\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}\begin{pmatrix}{{{\mathbf{I}}}}&{{{\mathbf{0}}}} \\{{{-\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{I}}}}\end{pmatrix}=\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{H}}}}\end{pmatrix}   \tag*{(7.114)}
$$

Putting it all together we get

$$
\underbrace{\begin{pmatrix}{{{\mathbf{I}}}}&{{{-\mathbf{F}\mathbf{H}^{-1}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{I}}}}\end{pmatrix}}_{X}\underbrace{\begin{pmatrix}{{{\mathbf{E}}}}&{{{\mathbf{F}}}} \\{{{\mathbf{G}}}}&{{{\mathbf{H}}}}\end{pmatrix}}_{M}\underbrace{\begin{pmatrix}{{{\mathbf{I}}}}&{{{\mathbf{0}}}} \\{{{-\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{I}}}}\end{pmatrix}}_{Z}=\underbrace{\begin{pmatrix}{{{\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{H}}}}\end{pmatrix}}_{W}   \tag*{(7.115)}
$$

Taking the inverse of both sides yields

$$
\mathbf{Z}^{-1}\mathbf{M}^{-1}\mathbf{X}^{-1}=\mathbf{W}^{-1}   \tag*{(7.116)}
$$

$$
\mathbf{M}^{-1}=\mathbf{Z}\mathbf{W}^{-1}\mathbf{X}   \tag*{(7.117)}
$$


---

Substituting in the definitions we get

$$
\begin{pmatrix}\mathbf{E}&\mathbf{F}\\\mathbf{G}&\mathbf{H}\end{pmatrix}^{-1}=\begin{pmatrix}\mathbf{I}&\mathbf{0}\\-\mathbf{H}^{-1}\mathbf{G}&\mathbf{I}\end{pmatrix}\begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1}&\mathbf{0}\\\mathbf{0}&\mathbf{H}^{-1}\end{pmatrix}\begin{pmatrix}\mathbf{I}&-\mathbf{F}\mathbf{H}^{-1}\\\mathbf{0}&\mathbf{I}\end{pmatrix}   \tag*{(7.118)}
$$

$$
\begin{aligned}=\begin{pmatrix}{{{(\mathbf{M}/\mathbf{H})^{-1}}}}&{{{\mathbf{0}}}} \\{{{-\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}}}}&{{{\mathbf{H}^{-1}}}}\end{pmatrix}\begin{pmatrix}{{{\mathbf{I}}}}&{{{-\mathbf{F}\mathbf{H}^{-1}}}} \\{{{\mathbf{0}}}}&{{{\mathbf{I}}}}\end{pmatrix}\end{aligned}   \tag*{(7.119)}
$$

$$
\begin{aligned}=\begin{pmatrix}(\mathbf{M}/\mathbf{H})^{-1}&-(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\\-\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}&\mathbf{H}^{-1}+\mathbf{H}^{-1}\mathbf{G}(\mathbf{M}/\mathbf{H})^{-1}\mathbf{F}\mathbf{H}^{-1}\end{pmatrix}\end{aligned}   \tag*{(7.120)}
$$

Alternatively, we could have decomposed the matrix M in terms of E and M/E = (H - G E^{-1} F), yielding

$$
\begin{pmatrix}\mathbf{E}&\mathbf{F}\\\mathbf{G}&\mathbf{H}\end{pmatrix}^{-1}=\begin{pmatrix}\mathbf{E}^{-1}+\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&-\mathbf{E}^{-1}\mathbf{F}(\mathbf{M}/\mathbf{E})^{-1}\\-(\mathbf{M}/\mathbf{E})^{-1}\mathbf{G}\mathbf{E}^{-1}&(\mathbf{M}/\mathbf{E})^{-1}\end{pmatrix}   \tag*{(7.121)}
$$

☐

#### 7.3.3 The matrix inversion lemma  $*$

 
$$
\left(\mathbf{M}/\mathbf{H}\right)^{-1}=\left(\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}\right)^{-1}=\mathbf{E}^{-1}+\mathbf{E}^{-1}\mathbf{F}(\mathbf{H}-\mathbf{G}\mathbf{E}^{-1}\mathbf{F})^{-1}\mathbf{G}\mathbf{E}^{-1}
$$
 

Equating the top left block of the first matrix in Equation (7.119) with the top left block of the matrix in Equation (7.121)

This is known as the matrix inversion lemma or the Sherman-Morrison-Woodbury formula.

A typical application in machine learning is the following. Let $\mathbf{X}$be an$N \times D$data matrix, and$\mathbf{\Sigma}$be$N \times N$diagonal matrix. Then we have (using the substitutions$\mathbf{E} = \mathbf{\Sigma}$, $\mathbf{F} = \mathbf{G}^{\mathrm{T}} = \mathbf{X}$, and $\mathbf{H}^{-1} = -\mathbf{I}$) the following result:

$$
(\boldsymbol{\Sigma}+\mathbf{X}\mathbf{X}^{\mathrm{T}})^{-1}=\boldsymbol{\Sigma}^{-1}-\boldsymbol{\Sigma}^{-1}\mathbf{X}(\mathbf{I}+\mathbf{X}^{\mathrm{T}}\boldsymbol{\Sigma}^{-1}\mathbf{X})^{-1}\mathbf{X}^{\mathrm{T}}\boldsymbol{\Sigma}^{-1}   \tag*{(7.123)}
$$

The LHS takes  $O(N^{3})$ time to compute, the RHS takes time  $O(D^{3})$ to compute.

Another application concerns computing a rank one update of an inverse matrix. Let  $\mathbf{E} = \mathbf{A}$,  $\mathbf{F} = \mathbf{u}$,  $\mathbf{G} = \mathbf{v}^\top$, and  $H = -1$. Then we have

$$
(\mathbf{A}+\mathbf{u}\mathbf{v}^{\mathsf{T}})^{-1}=\mathbf{A}^{-1}+\mathbf{A}^{-1}\mathbf{u}(-1-\mathbf{v}^{\mathsf{T}}\mathbf{A}^{-1}\mathbf{u})^{-1}\mathbf{v}^{\mathsf{T}}\mathbf{A}^{-1}   \tag*{(7.124)}
$$

$$
=\mathbf{A}^{-1}-\frac{\mathbf{A}^{-1}\mathbf{u}\mathbf{v}^{\top}\mathbf{A}^{-1}}{1+\mathbf{v}^{\top}\mathbf{A}^{-1}\mathbf{u}}   \tag*{(7.125)}
$$

This is known as the Sherman-Morrison formula.

#### 7.3.4 Matrix determinant lemma  $*$

We now use the above results to derive an efficient way to compute the determinant of a block-structured matrix.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

From Equation  $(7.115)$, we have

$$
\left\| \mathbf{X} \right\| \left\| \mathbf{M} \right\| \left\| \mathbf{Z} \right\|= \left\| \mathbf{W} \right\|= \left\| \mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G} \right\| \left\| \mathbf{H} \right\|   \tag*{(7.126)}
$$

$$
\left|\begin{pmatrix}\mathbf{E}&\mathbf{F}\\\mathbf{G}&\mathbf{H}\\\end{pmatrix}\right|=|\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}||\mathbf{H}|   \tag*{(7.127)}
$$

$$
\left|M\right|=\left|M/H\right|\left|H\right|   \tag*{(7.128)}
$$

$$
\left|\mathbf{M}/\mathbf{H}\right|=\frac{\left|\mathbf{M}\right|}{\left|\mathbf{H}\right|}   \tag*{(7.129)}
$$

So we can see that M/H acts somewhat like a division operator (hence the notation).

 
$$
\left\| \mathbf{M} \right\|= \left\| \mathbf{M}/\mathbf{H} \right\| \left\| \mathbf{H} \right\|= \left\| \mathbf{M}/\mathbf{E} \right\| \left\| \mathbf{E} \right\|
$$
 

Furthermore, we have

$$
\left|\mathbf{M}/\mathbf{H}\right|=\frac{\left|\mathbf{M}/\mathbf{E}\right|\left|\mathbf{E}\right|}{\left|\mathbf{H}\right|}   \tag*{(7.131)}
$$

$$
\left|\mathbf{E}-\mathbf{F}\mathbf{H}^{-1}\mathbf{G}\right|=\left|\mathbf{H}-\mathbf{G}\mathbf{E}^{-1}\mathbf{F}\right|\left|\mathbf{H}^{-1}\right|\left|\mathbf{E}\right|   \tag*{(7.132)}
$$

Hence (setting E = A, F = -u, G = v^{T}, H = 1) we have

$$
|\mathbf{A}+u\boldsymbol{v}^{\mathsf{T}}|=(1+v^{\mathsf{T}}\mathbf{A}^{-1}\boldsymbol{u})|\mathbf{A}|   \tag*{(7.133)}
$$

This is known as the matrix determinant lemma.

#### 7.3.5 Application: deriving the conditionals of an MVN *

Consider a joint Gaussian of the form  $p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})=\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu},\boldsymbol{\Sigma})$, where

$$
\boldsymbol{\mu}=\begin{pmatrix}\boldsymbol{\mu}_{1}\\ \boldsymbol{\mu}_{2}\end{pmatrix},\quad\boldsymbol{\Sigma}=\begin{pmatrix}\boldsymbol{\Sigma}_{11}&\boldsymbol{\Sigma}_{12}\\ \boldsymbol{\Sigma}_{21}&\boldsymbol{\Sigma}_{22}\end{pmatrix}   \tag*{(7.134)}
$$

In Section 3.2.3, we claimed that

$$
p(\boldsymbol{x}_{1}|\boldsymbol{x}_{2})=\mathcal{N}(\boldsymbol{x}_{1}|\boldsymbol{\mu}_{1}+\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}),\ \boldsymbol{\Sigma}_{11}-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21})   \tag*{(7.135)}
$$

In this section, we derive this result using Schur complements.

Let us factor the joint  $p(\boldsymbol{x}_{1}, \boldsymbol{x}_{2})$ as  $p(\boldsymbol{x}_{2}) p(\boldsymbol{x}_{1} | \boldsymbol{x}_{2})$ as follows:

$$
p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})\propto\exp\left\{-\frac{1}{2}\begin{pmatrix}\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}\\ \boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}\end{pmatrix}^{\top}\begin{pmatrix}\boldsymbol{\Sigma}_{11}&\boldsymbol{\Sigma}_{12}\\ \boldsymbol{\Sigma}_{21}&\boldsymbol{\Sigma}_{22}\end{pmatrix}^{-1}\begin{pmatrix}\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}\\ \boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}\end{pmatrix}\right\}   \tag*{(7.136)}
$$


---

Using Equation  $(7.118)$ the above exponent becomes

$$
p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})\propto\exp\left\{-\frac{1}{2}\begin{pmatrix}{{{\boldsymbol{x}_{1}-\mu_{1}}}} \\{{{\boldsymbol{x}_{2}-\mu_{2}}}}\end{pmatrix}^{\top}\begin{pmatrix}{{{\mathbf{I}}}}&{{{\mathbf{0}}}} \\{{{-\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}}}}&{{{\mathbf{I}}}}\end{pmatrix}\begin{pmatrix}{{{(\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22})^{-1}}}}&{{{\mathbf{0}}}} \\{{{\mathbf{0}}}}&{{{\boldsymbol{\Sigma}_{22}^{-1}}}}\end{pmatrix}\right.   \tag*{(7.137)}
$$

$$
\times\begin{pmatrix}\mathbf{I}&-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\\\mathbf{0}&\mathbf{I}\end{pmatrix}\begin{pmatrix}\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}\\\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}\end{pmatrix}   \tag*{(7.138)}
$$

$$
=\exp\left\{-\frac{1}{2}(\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2}))^{\top}(\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22})^{-1}\right.   \tag*{(7.139)}
$$

$$
\left(\boldsymbol{x}_{1}-\boldsymbol{\mu}_{1}-\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})\right)\times\exp\left\{-\frac{1}{2}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})^{\top}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})\right\}   \tag*{(7.140)}
$$

This is of the form

$$
\exp(quadratic form in\boldsymbol{x}_{1},\boldsymbol{x}_{2})\times\exp(quadratic form in\boldsymbol{x}_{2})   \tag*{(7.141)}
$$

Hence we have successfully factorized the joint as

$$
p(\boldsymbol{x}_{1},\boldsymbol{x}_{2})=p(\boldsymbol{x}_{1}|\boldsymbol{x}_{2})p(\boldsymbol{x}_{2})   \tag*{(7.142)}
$$

$$
=\mathcal{N}(\boldsymbol{x}_{1}|\boldsymbol{\mu}_{1|2},\boldsymbol{\Sigma}_{1|2})\mathcal{N}(\boldsymbol{x}_{2}|\boldsymbol{\mu}_{2},\boldsymbol{\Sigma}_{22})   \tag*{(7.143)}
$$

where the parameters of the conditional distribution can be read off from the above equations using

$$
\boldsymbol{\mu}_{1|2}=\boldsymbol{\mu}_{1}+\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\boldsymbol{x}_{2}-\boldsymbol{\mu}_{2})   \tag*{(7.144)}
$$

$$
\mathbf{\Sigma}_{1|2}=\mathbf{\Sigma}/\mathbf{\Sigma}_{22}=\mathbf{\Sigma}_{11}-\mathbf{\Sigma}_{12}\mathbf{\Sigma}_{22}^{-1}\mathbf{\Sigma}_{21}   \tag*{(7.145)}
$$

We can also use the fact that  $|\mathbf{M}| = |\mathbf{M}/\mathbf{H}||\mathbf{H}|$ to check the normalization constants are correct:

$$
\begin{align*}(2\pi)^{(d_{1}+d_{2})/2}|\boldsymbol{\Sigma}|^{\frac{1}{2}}&=(2\pi)^{(d_{1}+d_{2})/2}(|\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22}|\;|\boldsymbol{\Sigma}_{22}|)^{\frac{1}{2}}\\ &=(2\pi)^{d_{1}/2}|\boldsymbol{\Sigma}/\boldsymbol{\Sigma}_{22}|^{\frac{1}{2}}\;(2\pi)^{d_{2}/2}|\boldsymbol{\Sigma}_{22}|^{\frac{1}{2}}\end{align*}   \tag*{(7.146)}
$$

where  $d_{1}=\dim(\boldsymbol{x}_{1})$ and  $d_{2}=\dim(\boldsymbol{x}_{2})$.

### 7.4 Eigenvalue decomposition (EVD)

In this section, we review some standard material on the eigenvalue decomposition or EVD of square (real-valued) matrices.

#### 7.4.1 Basics

Given a square matrix  $\mathbf{A} \in \mathbb{R}^{n \times n}$, we say that  $\lambda \in \mathbb{R}$ is an eigenvalue of  $\mathbf{A}$ and  $\boldsymbol{u} \in \mathbb{R}^n$ is the corresponding eigenvector if

$$
\mathbf{A}\boldsymbol{u}=\lambda\boldsymbol{u},\quad\boldsymbol{u}\neq\boldsymbol{0}.   \tag*{(7.148)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

Intuitively, this definition means that multiplying  $\mathbf{A}$ by the vector  $\mathbf{u}$ results in a new vector that points in the same direction as  $\mathbf{u}$, but is scaled by a factor  $\lambda$. For example, if  $\mathbf{A}$ is a rotation matrix, then  $\mathbf{u}$ is the axis of rotation and  $\lambda = 1$.

Note that for any eigenvector  $\boldsymbol{u} \in \mathbb{R}^n$, and scalar  $c \in \mathbb{R}$,

$$
\mathbf{A}(c\mathbf{u})=c\mathbf{A}\mathbf{u}=c\lambda\mathbf{u}=\lambda(c\mathbf{u})   \tag*{(7.149)}
$$

Hence  $\mathbf{c}\mathbf{u}$ is also an eigenvector. For this reason when we talk about “the” eigenvector associated with  $\lambda$, we usually assume that the eigenvector is normalized to have length 1 (this still creates some ambiguity, since  $\mathbf{u}$ and  $-\mathbf{u}$ will both be eigenvectors, but we will have to live with this).

We can rewrite the equation above to state that (λ, x) is an eigenvalue-eigenvector pair of A if

$$
(\lambda\mathbf{I}-\mathbf{A})\boldsymbol{u}=\mathbf{0},\quad\boldsymbol{u}\neq\boldsymbol{0}.   \tag*{(7.150)}
$$

Now $(\lambda\mathbf{I}-\mathbf{A})\boldsymbol{u}=\mathbf{0}$has a non-zero solution to$\boldsymbol{u}$if and only if$(\lambda\mathbf{I}-\mathbf{A})$has a non-empty nullspace, which is only the case if$(\lambda\mathbf{I}-\mathbf{A})$ is singular, i.e.,

$$
\det(\lambda\mathbf{I}-\mathbf{A})=0\quad.   \tag*{(7.151)}
$$

This is called the characteristic equation of A. (See Exercise 7.2.) The $n$solutions of this equation are the$n$(possibly complex-valued) eigenvalues$\lambda_{i}$, and $u_{i}$ are the corresponding eigenvectors. It is standard to sort the eigenvectors in order of their eigenvalues, with the largest magnitude ones first.

The following are properties of eigenvalues and eigenvectors.

• The trace of a matrix is equal to the sum of its eigenvalues,

$$
\mathrm{tr}(\mathbf{A})=\sum_{i=1}^{n}\lambda_{i}\quad.   \tag*{(7.152)}
$$

• The determinant of A is equal to the product of its eigenvalues,

$$
\det(\mathbf{A})=\prod_{i=1}^{n}\lambda_{i}\quad.   \tag*{(7.153)}
$$

• The rank of A is equal to the number of non-zero eigenvalues of A.

• If A is non-singular then  $1/\lambda_i$ is an eigenvalue of  $A^{-1}$ with associated eigenvector  $u_i$, i.e.,  $A^{-1}u_i = (1/\lambda_i)u_i$.

• The eigenvalues of a diagonal or triangular matrix are just the diagonal entries.

#### 7.4.2 Diagonalization

We can write all the eigenvector equations simultaneously as

$$
\mathbf{A}\mathbf{U}=\mathbf{U}\mathbf{\Lambda}   \tag*{(7.154)}
$$


---

where the columns of  $\mathbf{U} \in \mathbb{R}^{n \times n}$ are the eigenvectors of  $\mathbf{A}$ and  $\mathbf{\Lambda}$ is a diagonal matrix whose entries are the eigenvalues of  $\mathbf{A}$, i.e.,

$$
\mathbf{U}\in\mathbb{R}^{n\times n}=\left[\begin{array}{ccc}\mid&|\ &\\\mathbf{u}_{1}&\mathbf{u}_{2}&\cdots&\mathbf{u}_{n}\\\mid&|\ &|\end{array}\right],\mathbf{\Lambda}=diag(\lambda_{1},\ldots,\lambda_{n})\ .   \tag*{(7.155)}
$$

If the eigenvectors of A are linearly independent, then the matrix U will be invertible, so

$$
\mathbf{A}=\mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{-1}   \tag*{(7.156)}
$$

A matrix that can be written in this form is called diagonalizable.

#### 7.4.3 Eigenvalues and eigenvectors of symmetric matrices

When $\mathbf{A}$is real and symmetric, it can be shown that all the eigenvalues are real, and the eigenvectors are orthonormal, i.e.,$\mathbf{u}_i^\top \mathbf{u}_j = 0$if$i \neq j$, and $\mathbf{u}_i^\top \mathbf{u}_i = 1$, where $\mathbf{u}_i$are the eigenvectors. In matrix form, this becomes$\mathbf{U}^\top \mathbf{U} = \mathbf{U} \mathbf{U}^\top = \mathbf{I}$; hence we see that $\mathbf{U}$ is an orthogonal matrix.

We can therefore represent A as

$$
\begin{aligned}\mathbf{A}&=\mathbf{U}\mathbf{\Lambda}\mathbf{U}^{\mathsf{T}}=\begin{pmatrix}|\quad|&\quad|\\\mathbf{u}_{1}&\mathbf{u}_{2}&\cdots&\mathbf{u}_{n}\\\end{pmatrix}\begin{pmatrix}\lambda_{1}&&\\&\lambda_{2}&\\&&\ddots&\\&&&\lambda_{n}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{u}_{1}^{\mathsf{T}}&-&\\-\quad\mathbf{u}_{2}^{\mathsf{T}}&-&\\&\vdots&\\-\quad\mathbf{u}_{n}^{\mathsf{T}}&-&\\&\end{pmatrix}\\&=\lambda_{1}\begin{pmatrix}|\quad|\\\mathbf{u}_{1}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{u}_{1}^{\mathsf{T}}&-\end{pmatrix}+\cdots+\lambda_{n}\begin{pmatrix}|\quad|\\\mathbf{u}_{n}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{u}_{n}^{\mathsf{T}}&-\end{pmatrix}=\sum_{i=1}^{n}\lambda_{i}\mathbf{u}_{i}\mathbf{u}_{i}^{\mathsf{T}}\\\end{aligned}   \tag*{(7.157)}
$$

Thus multiplying by any symmetric matrix A can be interpreted as multiplying by a rotation matrix  $\mathbf{U}^{\top}$, a scaling matrix  $\Lambda$, followed by an inverse rotation  $\mathbf{U}$.

Once we have diagonalized a matrix, it is easy to invert. Since  $\mathbf{A} = \mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{\mathrm{T}}$, where  $\mathbf{U}^{\mathrm{T}} = \mathbf{U}^{-1}$, we have

$$
\mathbf{A}^{-1}=\mathbf{U}\boldsymbol{\Lambda}^{-1}\mathbf{U}^{\mathrm{T}}=\sum_{i=1}^{d}\frac{1}{\lambda_{i}}\boldsymbol{u}_{i}\boldsymbol{u}_{i}^{\mathrm{T}}   \tag*{(7.159)}
$$

This corresponds to rotating, unscaling, and then rotating back.

##### 7.4.3.1 Checking for positive definiteness

We can also use the diagonalization property to show that a symmetric matrix is positive definite if all its eigenvalues are positive. To see this, note that

$$
\boldsymbol{x}^{\mathrm{T}}\mathbf{A}\boldsymbol{x}=\boldsymbol{x}^{\mathrm{T}}\mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{\mathrm{T}}\boldsymbol{x}=\boldsymbol{y}^{\mathrm{T}}\boldsymbol{\Lambda}\boldsymbol{y}=\sum_{i=1}^{n}\lambda_{i}y_{i}^{2}   \tag*{(7.160)}
$$

where  $\mathbf{y} = \mathbf{U}^\top \mathbf{x}$. Because  $y_i^2$ is always nonnegative, the sign of this expression depends entirely on the  $\lambda_i$’s. If all  $\lambda_i > 0$, then the matrix is positive definite; if all  $\lambda_i \geq 0$, it is positive semidefinite. Likewise, if all  $\lambda_i < 0$ or  $\lambda_i \leq 0$, then  $\mathbf{A}$ is negative definite or negative semidefinite respectively. Finally, if  $\mathbf{A}$ has both positive and negative eigenvalues, it is indefinite.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_378_127_793_394.jpg" alt="Image" width="36%" /></div>

<div style="text-align: center;">Figure 7.6: Visualization of a level set of the quadratic form  $(\mathbf{x} - \boldsymbol{\mu})^{\top} \mathbf{A}(\mathbf{x} - \boldsymbol{\mu})$ in 2d. The major and minor axes of the ellipse are defined by the first two eigenvectors of  $\mathbf{A}$, namely  $\mathbf{u}_1$ and  $\mathbf{u}_2$. Adapted from Figure 2.7 of [Bis06]. Generated by gaussEvec.ipynb.</div>

#### 7.4.4 Geometry of quadratic forms

A quadratic form is a function that can be written as

$$
f(\boldsymbol{x})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}   \tag*{(7.161)}
$$

where  $x \in \mathbb{R}^n$ and  $A$ is a positive definite, symmetric  $n$-by- $n$ matrix. Let  $A = U \Lambda U^\top$ be a diagonalization of  $A$ (see Section 7.4.3). Hence we can write

$$
f(\boldsymbol{x})=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}=\boldsymbol{x}^{\top}\mathbf{U}\boldsymbol{\Lambda}\mathbf{U}^{\top}\boldsymbol{x}=\boldsymbol{y}^{\top}\boldsymbol{\Lambda}\boldsymbol{y}=\sum_{i=1}^{n}\lambda_{i}y_{i}^{2}   \tag*{(7.162)}
$$

where  $y_i = \boldsymbol{x}^t \boldsymbol{u}_i$ and  $\lambda_i > 0$ (since  $\mathbf{A}$ is positive definite). The level sets of  $f(\boldsymbol{x})$ define hyper-ellipsoids. For example, in 2d, we have

$$
\lambda_{1}y_{1}^{2}+\lambda_{2}y_{2}^{2}=r   \tag*{(7.163)}
$$

which is the equation of a 2d ellipse. This is illustrated in Figure 7.6. The eigenvectors determine the orientation of the ellipse, and the eigenvalues determine how elongated it is. In particular, the major and minor semi-axes of the ellipse satisfy  $a^{-2} = \lambda_1$ and  $b^{-2} = \lambda_2$. In the case of a Gaussian distribution, we have  $\mathbf{A} = \Sigma^{-1}$, so small values of  $\lambda_i$ correspond to directions where the posterior has low precision and hence high variance.

#### 7.4.5 Standardizing and whitening data

Suppose we have a dataset  $\mathbf{X} \in \mathbb{R}^{N \times D}$. It is common to preprocess the data so that each column has zero mean and unit variance. This is called standardizing the data, as we discuss in Section 10.2.8. Although standardizing forces the variance to be 1, it does not remove correlation between the columns. To do that, we must  $\text{whiten}$ the data. To define this, let the empirical covariance matrix

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_209_139_540_395.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_606_138_947_399.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_213_460_541_721.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_617_460_949_724.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">Figure 7.7: (a) Height/weight data. (b) Standardized. (c) PCA Whitening. (d) ZCA whitening. Numbers refer to the first 4 datapoints, but there are 73 datapoints in total. Generated by height_weight_whiten_plot.ipynb.</div>

be  $\mathbf{S} = \frac{1}{N} \mathbf{X}^{\mathrm{T}} \mathbf{X}$, and let  $\mathbf{S} = \mathbf{E} \mathbf{D} \mathbf{E}^{\mathrm{T}}$ be its diagonalization. Equivalently, let  $[\mathbf{U}, \mathbf{S}, \mathbf{V}]$ be the SVD of  $\frac{1}{\sqrt{N}} \mathbf{X}$ (so  $\mathbf{E} = \mathbf{V}$ and  $\mathbf{D} = \mathbf{S}^2$, as we discuss in Section 20.1.3.3.) Now define

$$
\mathbf{W}_{p c a}=\mathbf{D}^{-\frac{1}{2}}\mathbf{E}^{\mathsf{T}}   \tag*{(7.164)}
$$

This is called the PCA whitening matrix. (We discuss PCA in Section 20.1.) Let  $\boldsymbol{y} = \boldsymbol{W}_{pca} \boldsymbol{x}$ be a transformed vector. We can check that its covariance is white as follows:

$$
\mathrm{Cov}\left[\boldsymbol{y}\right]=\mathbf{W}\mathbb{E}\left[\boldsymbol{x}\boldsymbol{x}^{\mathrm{T}}\right]\mathbf{W}^{\mathrm{T}}=\mathbf{W}\boldsymbol{\Sigma}\mathbf{W}^{\mathrm{T}}=(\mathbf{D}^{-\frac{1}{2}}\mathbf{E}^{\mathrm{T}})(\mathbf{E}\mathbf{D}\mathbf{E}^{\mathrm{T}})(\mathbf{E}\mathbf{D}^{-\frac{1}{2}})=\mathbf{I}   \tag*{(7.165)}
$$

The whitening matrix is not unique, since any rotation of it,  $\mathbf{W} = \mathbf{R} \mathbf{W}_{pca}$, will still maintain the whitening property, i.e.,  $\mathbf{W}^\top \mathbf{W} = \boldsymbol{\Sigma}^{-1}$. For example, if we take  $\mathbf{R} = \mathbf{E}$, we get

$$
\mathbf{W}_{zca}=\mathbf{E}\mathbf{D}^{-\frac{1}{2}}\mathbf{E}^{\mathsf{T}}=\boldsymbol{\Sigma}^{-\frac{1}{2}}=\mathbf{V}\mathbf{S}^{-1}\mathbf{V}^{\mathsf{T}}   \tag*{(7.166)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

This is called Mahalanobis whitening or ZCA. (ZCA stands for “zero-phase component analysis”, and was introduced in [BS97].) The advantage of ZCA whitening over PCA whitening is that the resulting transformed data is as close as possible to the original data (in the least squares sense) [Amo17]. This is illustrated in Figure 7.7. When applied to images, the ZCA transformed data vectors still look like images. This is useful when the method is used inside a deep learning system [KH09].

#### 7.4.6 Power method

We now describe a simple iterative method for computing the eigenvector corresponding to the largest eigenvalue of a real, symmetric matrix; this is called the power method. This can be useful when the matrix is very large but sparse. For example, it is used by Google's PageRank to compute the stationary distribution of the transition matrix of the world wide web (a matrix of size about 3 billion by 3 billion!). In Section 7.4.7, we will see how to use this method to compute subsequent eigenvectors and values.

Let $\mathbf{A}$be a matrix with orthonormal eigenvectors$\mathbf{u}_i$and eigenvalues$|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_m| \geq 0$, so $\mathbf{A} = \mathbf{U}\mathbf{\Lambda}\mathbf{U}^\top$. Let $\mathbf{v}_{(0)}$be an arbitrary vector in the range of$\mathbf{A}$, so $\mathbf{A}\mathbf{x} = \mathbf{v}_{(0)}$for some$\mathbf{x}$. Hence we can write $\mathbf{v}_{(0)}$ as

$$
\boldsymbol{v}_{0}=\mathbf{U}(\boldsymbol{\Lambda}\mathbf{U}^{\top}\boldsymbol{x})=a_{1}\boldsymbol{u}_{1}+\cdots+a_{m}\boldsymbol{u}_{m}   \tag*{(7.167)}
$$

for some constants  $a_{i}$. We can now repeatedly multiply v by A and renormalize:

$$
\boldsymbol{v}_{t}\propto\mathbf{A}\boldsymbol{v}_{t-1}   \tag*{(7.168)}
$$

(We normalize at each iteration for numerical stability.)

Since  $v_{t}$ is a multiple of  $A^{t}v_{0}$, we have

$$
\begin{aligned}\boldsymbol{v}_{t}&\propto a_{1}\lambda_{1}^{t}\boldsymbol{u}_{1}+a_{2}\lambda_{2}^{t}\boldsymbol{u}_{2}+\cdots+a_{m}\lambda_{m}^{t}\boldsymbol{u}_{m}\\&=\lambda_{1}^{t}\left(a_{1}\boldsymbol{u}_{1}+a_{1}(\lambda_{2}/\lambda_{1})^{t}\boldsymbol{u}_{2}+\cdots+a_{m}(\lambda_{m}/\lambda_{1})^{t}\boldsymbol{u}_{m}\right)\\&\rightarrow\lambda_{1}^{t}a_{1}\boldsymbol{u}_{1}\end{aligned}   \tag*{(7.170)}
$$

since  $\left|\frac{\lambda_k}{\lambda_1}\right| < 1$ for  $k > 1$ (assuming the eigenvalues are sorted in descending order). So we see that this converges to  $\boldsymbol{u}_1$, although not very quickly (the error is reduced by approximately  $|\lambda_2/\lambda_1|$ at each iteration). The only requirement is that the initial guess satisfy  $\boldsymbol{v}_0^\top \boldsymbol{u}_1 \neq 0$, which will be true for a random  $\boldsymbol{v}_0$ with high probability.

We now discuss how to compute the corresponding eigenvalue,  $\lambda_{1}$. Define the Rayleigh quotient to be

$$
R(\mathbf{A},x)\triangleq\frac{x^{\top}\mathbf{A}x}{x^{\top}x}   \tag*{(7.172)}
$$

Hence

$$
R(\mathbf{A},\boldsymbol{u}_{i})=\frac{\boldsymbol{u}_{i}^{\top}\mathbf{A}\boldsymbol{u}_{i}}{\boldsymbol{u}_{i}^{\top}\boldsymbol{u}_{i}}=\frac{\lambda_{i}\boldsymbol{u}_{i}^{\top}\boldsymbol{u}_{i}}{\boldsymbol{u}_{i}^{\top}\boldsymbol{u}_{i}}=\lambda_{i}   \tag*{(7.173)}
$$

Thus we can easily compute  $\lambda_{1}$ from  $u_{1}$ and A. See power_method_demo.ipynb for a demo.

---

#### 7.4.7 Deflation

Suppose we have computed the first eigenvector and value  $\boldsymbol{u}_{1}, \lambda_{1}$ by the power method. We now describe how to compute subsequent eigenvectors and values. Since the eigenvectors are orthonormal, and the eigenvalues are real, we can project out the  $\boldsymbol{u}_{1}$ component from the matrix as follows:

$$
\mathbf{A}^{(2)}=(\mathbf{I}-\boldsymbol{u}_{1}\boldsymbol{u}_{1}^{\top})\mathbf{A}^{(1)}=\mathbf{A}^{(1)}-\boldsymbol{u}_{1}\boldsymbol{u}_{1}^{\top}\mathbf{A}^{(1)}=\mathbf{A}^{(1)}-\lambda_{1}\boldsymbol{u}_{1}\boldsymbol{u}_{1}^{\top}   \tag*{(7.174)}
$$

This is called matrix deflation. We can then apply the power method to  $\mathbf{A}^{(2)}$, which will find the largest eigenvector/value in the subspace orthogonal to  $\mathbf{u}_{1}$.

In Section 20.1.2, we show that the optimal estimate  $\mathbf{W}$ for the PCA model (described in Section 20.1) is given by the first  $K$ eigenvectors of the empirical covariance matrix. Hence deflation can be used to implement PCA. It can also be modified to implement sparse PCA [Mac09].

#### 7.4.8 Eigenvectors optimize quadratic forms

We can use matrix calculus to solve an optimization problem in a way that leads directly to eigenvalue/eigenvector analysis. Consider the following, equality constrained optimization problem:

$$
\max_{\boldsymbol{x}\in\mathbb{R}^{n}}\ \boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}\quad subject to\|\boldsymbol{x}\|_{2}^{2}=1   \tag*{(7.175)}
$$

for a symmetric matrix  $\mathbf{A} \in \mathbb{S}^n$. A standard way of solving optimization problems with equality constraints is by forming the Lagrangian, an objective function that includes the equality constraints (see Section 8.5.1). The Lagrangian in this case can be given by

$$
\mathcal{L}(\boldsymbol{x},\lambda)=\boldsymbol{x}^{\top}\mathbf{A}\boldsymbol{x}+\lambda(1-\boldsymbol{x}^{\top}\boldsymbol{x})   \tag*{(7.176)}
$$

where  $\lambda$ is called the Lagrange multiplier associated with the equality constraint. It can be established that for  $x^{*}$ to be a optimal point to the problem, the gradient of the Lagrangian has to be zero at  $x^{*}$ (this is not the only condition, but it is required). That is,

$$
\nabla_{x}\mathcal{L}(x,\lambda)=2\mathbf{A}^{\top}x-2\lambda x=\mathbf{0}.   \tag*{(7.177)}
$$

Notice that this is just the linear equation  $\mathbf{A}\mathbf{x} = \lambda\mathbf{x}$. This shows that the only points which can possibly maximize (or minimize)  $\mathbf{x}^\top \mathbf{A}\mathbf{x}$ assuming  $\mathbf{x}^\top \mathbf{x} = 1$ are the eigenvectors of  $\mathbf{A}$.

### 7.5 Singular value decomposition (SVD)

We now discuss the SVD, which generalizes EVD to rectangular matrices.

#### 7.5.1 Basics

Any (real)  $m \times n$ matrix A can be decomposed as

$$
\mathbf{A}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}}=\sigma_{1}\begin{pmatrix}|\\\mathbf{u}_{1}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{v}_{1}^{\mathsf{T}}&-\end{pmatrix}+\cdots+\sigma_{r}\begin{pmatrix}|\\\mathbf{u}_{r}\\\end{pmatrix}\begin{pmatrix}-\quad\mathbf{v}_{r}^{\mathsf{T}}&-\end{pmatrix}   \tag*{(7.178)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_121_1016_275.jpg" alt="Image" width="68%" /></div>

<div style="text-align: center;">Figure 7.8: SVD decomposition of a matrix,  $\mathbf{A} = \mathbf{USV}^\top$. The shaded parts of each matrix are not computed in the economy-sized version. (a) Tall skinny matrix. (b) Short wide matrix.</div>

where  $\mathbf{U}$ is an  $m \times m$ whose columns are orthonormal (so  $\mathbf{U}^\top \mathbf{U} = \mathbf{I}_m$),  $\mathbf{V}$ is  $n \times n$ matrix whose rows and columns are orthonormal (so  $\mathbf{V}^\top \mathbf{V} = \mathbf{V} \mathbf{V}^\top = \mathbf{I}_n$), and  $\mathbf{S}$ is a  $m \times n$ matrix containing the  $r = \min(m, n)$ singular values  $\sigma_i \geq 0$ on the main diagonal, with 0s filling the rest of the matrix. The columns of  $\mathbf{U}$ are the left singular vectors, and the columns of  $\mathbf{V}$ are the right singular vectors. This is called the singular value decomposition or SVD of the matrix. See Figure 7.8 for an example.

As is apparent from Figure 7.8a, if  $m > n$, there are at most  $n$ singular values, so the last  $m - n$ columns of  $\mathbf{U}$ are irrelevant (since they will be multiplied by 0). The  $\mathbf{e}$conomy  $\mathbf{sized}$  $\mathbf{SVD}$, also called a  $\mathbf{thin}$  $\mathbf{SVD}$, avoids computing these unnecessary elements. In other words, if we write the  $\mathbf{U}$ matrix as  $\mathbf{U} = [\mathbf{U}_1, \mathbf{U}_2]$, we only compute  $\mathbf{U}_1$. Figure 7.8b shows the opposite case, where  $m < n$, where we represent  $\mathbf{V} = [\mathbf{V}_1; \mathbf{V}_2]$, and only compute  $\mathbf{V}_1$.

The cost of computing the SVD is  $O(\min(mn^2, m^2n))$. Details on how it works can be found in standard linear algebra textbooks.

#### 7.5.2 Connection between SVD and EVD

If  $\mathbf{A}$ is real, symmetric and positive definite, then the singular values are equal to the eigenvalues, and the left and right singular vectors are equal to the eigenvectors (up to a sign change):

$$
\mathbf{A}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathrm{T}}=\mathbf{U}\mathbf{S}\mathbf{U}^{\mathrm{T}}=\mathbf{U}\mathbf{S}\mathbf{U}^{-1}   \tag*{(7.179)}
$$

Note, however, that NumPy always returns the singular values in decreasing order, whereas the eigenvalues need not necessarily be sorted.

In general, for an arbitrary real matrix  $\mathbf{A}$, if  $\mathbf{A} = \mathbf{U} \mathbf{S} \mathbf{V}^{\mathrm{T}}$, we have

$$
\mathbf{A}^{\mathsf{T}}\mathbf{A}=\mathbf{V}\mathbf{S}^{\mathsf{T}}\mathbf{U}^{\mathsf{T}}\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}}=\mathbf{V}(\mathbf{S}^{\mathsf{T}}\mathbf{S})\mathbf{V}^{\mathsf{T}}   \tag*{(7.180)}
$$

Hence

$$
(\mathbf{A}^{\top}\mathbf{A})\mathbf{V}=\mathbf{V}\mathbf{D}_{n}   \tag*{(7.181)}
$$

so the eigenvectors of  $\mathbf{A}^\top \mathbf{A}$ are equal to  $\mathbf{V}$, the right singular vectors of  $\mathbf{A}$, and the eigenvalues of  $\mathbf{A}^\top \mathbf{A}$ are equal to  $\mathbf{D}_n = \mathbf{S}^\top \mathbf{S}$, which is an  $n \times n$ diagonal matrix containing the squared singular values. Similarly

$$
\mathbf{A}\mathbf{A}^{\mathrm{T}}=\mathbf{U}\mathbf{S}\mathbf{V}^{\mathrm{T}}\mathbf{V}\mathbf{S}^{\mathrm{T}}\mathbf{U}^{\mathrm{T}}=\mathbf{U}(\mathbf{S}\mathbf{S}^{\mathrm{T}})\mathbf{U}^{\mathrm{T}}   \tag*{(7.182)}
$$

$$
(\mathbf{A}\mathbf{A}^{\mathrm{T}})\mathbf{U}=\mathbf{U}\mathbf{D}_{m}   \tag*{(7.183)}
$$


---

so the eigenvectors of  $\mathbf{A}\mathbf{A}^{\top}$ are equal to  $\mathbf{U}$, the left singular vectors of  $\mathbf{A}$, and the eigenvalues of  $\mathbf{A}\mathbf{A}^{\top}$ are equal to  $\mathbf{D}_{m}=\mathbf{S}\mathbf{S}^{\top}$, which is an  $m\times m$ diagonal matrix containing the squared singular values. In summary,

$$
\mathbf{U}=\mathrm{e v e c}(\mathbf{A}\mathbf{A}^{\mathsf{T}}),\mathbf{V}=\mathrm{e v e c}(\mathbf{A}^{\mathsf{T}}\mathbf{A}),\mathbf{D}_{m}=\mathrm{e v a l}(\mathbf{A}\mathbf{A}^{\mathsf{T}}),\mathbf{D}_{n}=\mathrm{e v a l}(\mathbf{A}^{\mathsf{T}}\mathbf{A})   \tag*{(7.184)}
$$

If we just use the computed (non-zero) parts in the economy-sized SVD, then we can define

$$
\mathbf{D}=\mathbf{S}^{2}=\mathbf{S}^{\mathsf{T}}\mathbf{S}=\mathbf{S}\mathbf{S}^{\mathsf{T}}   \tag*{(7.185)}
$$

Note also that an EVD does not always exist, even for square A, whereas an SVD always exists.

#### 7.5.3 Pseudo inverse

The Moore-Penrose pseudo-inverse of A, pseudo inverse denoted  $A^{\dagger}$, is defined as the unique matrix that satisfies the following 4 properties:

$$
\mathbf{A}\mathbf{A}^{\dagger}\mathbf{A}=\mathbf{A},\mathbf{A}^{\dagger}\mathbf{A}\mathbf{A}^{\dagger}=\mathbf{A}^{\dagger},(\mathbf{A}\mathbf{A}^{\dagger})^{\mathsf{T}}=\mathbf{A}\mathbf{A}^{\dagger},(\mathbf{A}^{\dagger}\mathbf{A})^{\mathsf{T}}=\mathbf{A}^{\dagger}\mathbf{A}   \tag*{(7.186)}
$$

If A is square and non-singular, then  $A^\dagger = A^{-1}$.

If m > n (tall, skinny) and the columns of A are linearly independent (so A is full rank), then

$$
\mathbf{A}^{\dagger}=(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}   \tag*{(7.187)}
$$

which is the same expression as arises in the normal equations (see Section 11.2.2.1). In this case,  $\mathbf{A}^{\dagger}$ is a left inverse of  $\mathbf{A}$ because

$$
\mathbf{A}^{\dagger}\mathbf{A}=(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}\mathbf{A}=\mathbf{I}   \tag*{(7.188)}
$$

but is not a right inverse because

$$
\mathbf{A}\mathbf{A}^{\dagger}=\mathbf{A}(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}\mathbf{A}^{\mathsf{T}}   \tag*{(7.189)}
$$

only has rank n, and so cannot be the  $m \times m$ identity matrix.

If $m < n$(short, fat) and the rows of$\mathbf{A}$are linearly independent (so$\mathbf{A}^{\mathrm{T}}$ is full rank), then the pseudo inverse is

$$
\mathbf{A}^{\dagger}=\mathbf{A}^{\mathsf{T}}(\mathbf{A}\mathbf{A}^{\mathsf{T}})^{-1}   \tag*{(7.190)}
$$

In this case, A† is a right inverse of A.

We can compute the pseudo inverse using the SVD decomposition  $\mathbf{A} = \mathbf{USV}^\top$. In particular, one can show that

$$
\mathbf{A}^{\dagger}=\mathbf{V}[\mathrm{diag}(1/\sigma_{1},\cdots,1/\sigma_{r},0,\cdots,0)]\mathbf{U}^{\top}=\mathbf{V}\mathbf{S}^{-1}\mathbf{U}^{\top}   \tag*{(7.191)}
$$

where $r$is the rank of the matrix, and where we define$\mathbf{S}^{-1} = \mathrm{diag}(\sigma_1^{-1}, \ldots, \sigma_r^{-1}, 0, \ldots, 0)$. Indeed if the matrices were square and full rank we would have

$$
(\mathbf{U}\mathbf{S}\mathbf{V}^{\mathsf{T}})^{-1}=\mathbf{V}\mathbf{S}^{-1}\mathbf{U}^{\mathsf{T}}   \tag*{(7.192)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 7.5.4 SVD and the range and null space of a matrix *

In this section, we show that the left and right singular vectors form an orthonormal basis for the range and null space.

From Equation  $(7.178)$ we have

$$
\mathbf{A}\boldsymbol{x}=\sum_{j:\sigma_{j}>0}\sigma_{j}(\boldsymbol{v}_{j}^{\mathsf{T}}\boldsymbol{x})\boldsymbol{u}_{j}=\sum_{j=1}^{r}\sigma_{j}(\boldsymbol{v}_{j}^{\mathsf{T}}\boldsymbol{x})\boldsymbol{u}_{j}   \tag*{(7.193)}
$$

where $r$is the rank of$\mathbf{A}$. Thus any $\mathbf{A}\mathbf{x}$can be written as a linear combination of the left singular vectors$\mathbf{u}_{1},\ldots,\mathbf{u}_{r}$, so the range of $\mathbf{A}$ is given by

$$
\mathrm{range}(\mathbf{A})=\mathrm{span}\left(\left\{\boldsymbol{u}_{j}:\sigma_{j}>0\right\}\right)   \tag*{(7.194)}
$$

with dimension r.

To find a basis for the null space, let us now define a second vector  $\mathbf{y} \in \mathbb{R}^n$ that is a linear combination solely of the right singular vectors for the zero singular values,

$$
\boldsymbol{y}=\sum_{j:\sigma_{j}=0}c_{j}\boldsymbol{v}_{j}=\sum_{j=r+1}^{n}c_{j}\boldsymbol{v}_{j}   \tag*{(7.195)}
$$

Since the  $v_{j}'$s are orthonormal, we have

$$
\mathbf{A}\boldsymbol{y}=\mathbf{U}\left(\begin{array}{c}\sigma_{1}\boldsymbol{v}_{1}^{\top}\boldsymbol{y}\\ \vdots\\ \sigma_{r}\boldsymbol{v}_{r}^{\top}\boldsymbol{y}\\ \sigma_{r+1}\boldsymbol{v}_{r+1}^{\top}\boldsymbol{y}\\ \vdots\\ \sigma_{n}\boldsymbol{v}_{n}^{\top}\boldsymbol{y}\end{array}\right)=\mathbf{U}\left(\begin{array}{c}\sigma_{1}0\\ \vdots\\ \sigma_{r}0\\ 0\boldsymbol{v}_{r+1}^{\top}\boldsymbol{y}\\ \vdots\\ 0\boldsymbol{v}_{n}^{\top}\boldsymbol{y}\end{array}\right)=\mathbf{U}\mathbf{0}=\mathbf{0}   \tag*{(7.196)}
$$

Hence the right singular vectors form an orthonormal basis for the null space:

$$
\mathrm{n u l l s p a c e}(\mathbf{A})=\mathrm{s p a n}\left(\{\boldsymbol{v}_{j}:\sigma_{j}=0\}\right)   \tag*{(7.197)}
$$

with dimension n - r. We see that

$$
\mathrm{dim}(\mathrm{range}(\mathbf{A}))+\mathrm{dim}(\mathrm{nullspace}(\mathbf{A}))=r+(n-r)=n   \tag*{(7.198)}
$$

In words, this is often written as

$$
rank+nullity=n   \tag*{(7.199)}
$$

This is called the rank-nullity theorem. It follows from this that the rank of a matrix is the number of nonzero singular values.

---

<div style="text-align: center;">rank 200</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_236_183_536_373.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;">rank 2</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_644_176_944_373.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">rank 5</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_236_506_536_695.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;">rank 20</div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_645_505_944_694.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;"> $(d)$</div>

<div style="text-align: center;">Figure 7.9: Low rank approximations to an image. Top left: The original image is of size  $200 \times 320$, so has rank 200. Subsequent images have ranks 2, 5, and 20. Generated by svd_image_demo.ipynb.</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_451_902_705_1091.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">Figure 7.10: First 100 log singular values for the clown image (red line), and for a data matrix obtained by randomly shuffling the pixels (blue line). Generated by svd_image_demo.ipynb. Adapted from Figure 14.24 of [HTF09].</div>


---

#### 7.5.5 Truncated SVD

Let  $\mathbf{A} = \mathbf{U} \mathbf{S} \mathbf{V}^T$ be the SVD of  $\mathbf{A}$, and let  $\hat{\mathbf{A}}_K = \mathbf{U}_K \mathbf{S}_K \mathbf{V}_K^T$, where we use the first  $K$ columns of  $\mathbf{U}$ and  $\mathbf{V}$. This can be shown to be the optimal rank  $K$ approximation, in the sense that it minimizes  $\|\mathbf{A} - \hat{\mathbf{A}}_K\|_F^2$.

If $K = r = \text{rank}(\mathbf{A})$, there is no error introduced by this decomposition. But if $K < r$, we incur some error. This is called a $\text{truncated SVD}$. If the singular values die off quickly, as is typical in natural data (see e.g., Figure 7.10), the error will be small. The total number of parameters needed to represent an $N \times D$matrix using a rank$K$ approximation is

$$
NK+KD+K=K(N+D+1)   \tag*{(7.200)}
$$

As an example, consider the  $200 \times 320$ pixel image in Figure 7.9(top left). This has 64,000 numbers in it. We see that a rank 20 approximation, with only  $(200 + 320 + 1) \times 20 = 10,420$ numbers is a very good approximation.

One can show that the error in this rank-K approximation is given by

$$
\left|\left|\mathbf{A}-\hat{\mathbf{A}}\right|\right|_{F}=\sum_{k=K+1}^{r}\sigma_{k}   \tag*{(7.201)}
$$

where  $\sigma_{k}$ is the  $k'$th singular value of A.

### 7.6 Other matrix decompositions *

In this section, we briefly review some other useful matrix decompositions.

#### 7.6.1 LU factorization

We can factorize any square matrix A into a product of a lower triangular matrix L and an upper triangular matrix U. For example,

$$
\begin{bmatrix}{{{a_{11}}}}&{{{a_{12}}}}&{{{a_{13}}}} \\{{{a_{21}}}}&{{{a_{22}}}}&{{{a_{23}}}} \\{{{a_{31}}}}&{{{a_{32}}}}&{{{a_{33}}}}\end{bmatrix}=\begin{bmatrix}{{{l_{11}}}}&{{{0}}}&{{{0}}} \\{{{l_{21}}}}&{{{l_{22}}}}&{{{0}}} \\{{{l_{31}}}}&{{{l_{32}}}}&{{{l_{33}}}}\end{bmatrix}\begin{bmatrix}{{{u_{11}}}}&{{{u_{12}}}}&{{{u_{13}}}} \\{{{0}}}&{{{u_{22}}}}&{{{u_{23}}}} \\{{{0}}}&{{{0}}}&{{{u_{33}}}}\end{bmatrix}.   \tag*{(7.202)}
$$

In general we may need to permute the entries in the matrix before creating this decomposition. To see this, suppose  $a_{11} = 0$. Since  $a_{11} = l_{11}u_{11}$, this means either  $l_{11}$ or  $u_{11}$ or both must be zero, but that would imply  $\mathbf{L}$ or  $\mathbf{U}$ are singular. To avoid this, the first step of the algorithm can simply reorder the rows so that the first element is nonzero. This is repeated for subsequent steps. We can denote this process by

$$
PA=LU   \tag*{(7.203)}
$$

where P is a permutation matrix, i.e., a square binary matrix where  $P_{ij} = 1$ if row j gets permuted to row i. This is called partial pivoting.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_198_118_552_279.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_607_215_964_287.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 7.11: Illustration of QR decomposition,  $\mathbf{A} = \mathbf{Q}\mathbf{R}$, where  $\mathbf{Q}^{\top}\mathbf{Q} = \mathbf{I}$ and  $\mathbf{R}$ is upper triangular. (a) Tall, skinny matrix. The shaded parts are not computed in the economy-sized version, since they are not needed. (b) Short, wide matrix.</div>

#### 7.6.2 QR decomposition

Suppose we have  $\mathbf{A} \in \mathbb{R}^{m \times n}$ representing a set of linearly independent basis vectors (so  $m \geq n$), and we want to find a series of orthonormal vectors  $\mathbf{q}_1, \mathbf{q}_2, \ldots$ that span the successive subspaces of  $\text{span}(\mathbf{a}_1)$,  $\text{span}(\mathbf{a}_1, \mathbf{a}_2)$, etc. In other words, we want to find vectors  $\mathbf{q}_j$ and coefficients  $r_{ij}$ such that

$$
\begin{pmatrix}|\quad|&&&\\a_{1}&a_{2}&\cdots&a_{n}\\\end{pmatrix}=\begin{pmatrix}|\quad|&&&|\\q_{1}&q_{2}&\cdots&q_{n}\\\end{pmatrix}\begin{pmatrix}r_{11}&r_{12}&\cdots&r_{1n}\\&r_{22}&\cdots&r_{2n}\\\end{pmatrix}   \tag*{(7.204)}
$$

We can write this

$$
a_{1}=r_{11}q_{1}   \tag*{(7.205)}
$$

$$
\boldsymbol{a}_{2}=r_{12}\boldsymbol{q}_{1}+r_{22}\boldsymbol{q}_{2}   \tag*{(7.206)}
$$

 
$$
\therefore
$$
 

$$
\boldsymbol{a}_{n}=r_{1n}\boldsymbol{q}_{1}+\cdots+r_{n n}\boldsymbol{q}_{n}   \tag*{(7.207)}
$$

so we see q1 spans the space of a1, and q1 and q2 span the space of {a1, a2}, etc.

In matrix notation, we have

$$
\mathbf{A}=\hat{\mathbf{Q}}\hat{\mathbf{R}}   \tag*{(7.208)}
$$

where  $\hat{Q}$ is  $m \times n$ with orthonormal columns and  $\hat{R}$ is  $n \times n$ and upper triangular. This is called a reduced QR or economy sized QR factorization of A; see Figure 7.11.

A full QR factorization appends an additional $m-n$orthonormal columns to$\mathbf{Q}$so it becomes a square, orthogonal matrix$\mathbf{Q}$, which satisfies $\mathbf{QQ}^{\mathrm{T}}=\mathbf{Q}^{\mathrm{T}}\mathbf{Q}=\mathbf{I}$. Also, we append rows made of zero to $\mathbf{R}$so it becomes an$m\times n$matrix that is still upper triangular, called$\mathbf{R}$: see Figure 7.11. The zero entries in $\mathbf{R}$“kill off” the new columns in$\mathbf{Q}$, so the result is the same as $\mathbf{\hat{Q}}\mathbf{\hat{R}}$.

QR decomposition is commonly used to solve systems of linear equations, as we discuss in Section 11.2.2.3.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

#### 7.6.3 Cholesky decomposition

Any symmetric positive definite matrix can be factorized as  $\mathbf{A} = \mathbf{R}^\top \mathbf{R}$, where  $\mathbf{R}$ is upper triangular with real, positive diagonal elements. (This can also be written as  $\mathbf{A} = \mathbf{L} \mathbf{L}^\top$, where  $\mathbf{L} = \mathbf{R}^\top$ is lower triangular.) This is called a Cholesky factorization or matrix square root. In NumPy, this is implemented by np.linalg.cholesky. The computational complexity of this operation is  $O(V^3)$, where  $V$ is the number of variables, but can be less for sparse matrices. Below we give some applications of this factorization.

##### 7.6.3.1 Application: Sampling from an MVN

The Cholesky decomposition of a covariance matrix can be used to sample from a multivariate Gaussian. Let  $\mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and  $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^\top$. We first sample  $\boldsymbol{x} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, which is easy because it just requires sampling from  $d$ separate  $1d$ Gaussians. We then set  $\mathbf{y} = \mathbf{L}\mathbf{x} + \boldsymbol{\mu}$. This is valid since

$$
\mathrm{Cov}\left[\boldsymbol{y}\right]=\mathrm{L}\mathrm{Cov}\left[\boldsymbol{x}\right]\boldsymbol{L}^{\top}=\mathrm{L}\mathrm{~I~L}^{\top}=\boldsymbol{\Sigma}   \tag*{(7.209)}
$$

See cholesky  $\underline{\text{}}$ demo.ipynb for some code.

### 7.7 Solving systems of linear equations *

An important application of linear algebra is the study of systems of linear equations. For example, consider the following set of 3 equations:

$$
3x_{1}+2x_{2}-x_{3}=1   \tag*{(7.210)}
$$

$$
2x_{1}-2x_{2}+4x_{3}=-2   \tag*{(7.211)}
$$

$$
-x_{1}+\frac{1}{2}x_{2}-x_{3}=0   \tag*{(7.212)}
$$

We can represent this in matrix-vector form as follows:

$$
\mathbf{A}\boldsymbol{x}=\boldsymbol{b}   \tag*{(7.213)}
$$

where

$$
\mathbf{A}=\begin{pmatrix}{{{3}}}&{{{2}}}&{{{-1}}} \\{{{2}}}&{{{-2}}}&{{{4}}} \\{{{-1}}}&{{{\frac{1}{2}}}}&{{{-1}}}\end{pmatrix},\mathbf{b}=\begin{pmatrix}{{{1}}} \\{{{-2}}} \\{{{0}}}\end{pmatrix}   \tag*{(7.214)}
$$

The solution is  $x = [1, -2, -2]$.

In general, if we have $m$equations and$n$unknowns, then$\mathbf{A}$will be a$m \times n$matrix, and$\mathbf{b}$will be a$m \times 1$vector. If$m = n$(and$\mathbf{A}$is full rank), there is a single unique solution. If$m < n$, the system is underdetermined, so there is not a unique solution. If $m > n$, the system is overdetermined, since there are more constraints than unknowns, and not all the lines intersect at the same point. See Figure 7.12 for an illustration. We discuss how to compute solutions in each of these cases below.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_304_125_861_251.jpg" alt="Image" width="48%" /></div>

<div style="text-align: center;">Figure 7.12: Solution of a set of m linear equations in n = 2 variables. (a) m = 1 < n so the system is underdetermined. We show the minimal norm solution as a blue circle. (The dotted red line is orthogonal to the line, and its length is the distance to the origin.) (b) m = n = 2, so there is a unique solution. (c) m = 3 > n, so there is no unique solution. We show the least squares solution.</div>

#### 7.7.1 Solving square systems

In the case where m = n, we can solve for x by computing an LU decomposition,  $\mathbf{A} = \mathbf{L} \mathbf{U}$, and then proceeding as follows:

$$
\mathbf{A}\boldsymbol{x}=\boldsymbol{b}   \tag*{(7.215)}
$$

$$
\mathbf{L}\mathbf{U}\mathbf{x}=\mathbf{b}   \tag*{(7.216)}
$$

$$
\mathbf{U}\mathbf{x}=\mathbf{L}^{-1}\mathbf{b}\triangleq\mathbf{y}   \tag*{(7.217)}
$$

$$
x=\mathrm{U}^{-1}y   \tag*{(7.218)}
$$

The crucial point is that L and U are both triangular matrices, so we can avoid taking matrix inverses, and use a method known as backsubstitution instead.

In particular, we can solve  $y = L^{-1}b$ without taking inverses as follows. First we write

$$
\begin{pmatrix}L_{11}&&&\\L_{21}&L_{22}&&\\&&\ddots&\\&&&L_{n1}&L_{n2}\quad\cdots\quad L_{nn}\end{pmatrix}\begin{pmatrix}y_{1}\\ \vdots\\ y_{n}\end{pmatrix}=\begin{pmatrix}b_{1}\\ \vdots\\ b_{n}\end{pmatrix}   \tag*{(7.219)}
$$

We start by solving  $L_{11}y_{1}=b_{1}$ to find  $y_{1}$ and then substitute this in to solve

$$
L_{21}y_{1}+L_{22}y_{2}=b_{2}   \tag*{(7.220)}
$$

for $y_2$. We repeat this recursively. This process is often denoted by the backslash operator, $y = \mathbf{L} \setminus b$. Once we have $y$, we can solve $x = \mathbf{U}^{-1} y$using backsubstitution in a similar manner.

#### 7.7.2 Solving underconstrained systems (least norm estimation)

In this section, we consider the underconstrained setting, where$ m < n $. We assume the rows are linearly independent, so A is full rank.

---

When m < n, there are multiple possible solutions, which have the form

$$
\{x:\mathbf{A}x=b\}=\{x_{p}+z:z\in\mathrm{n u l l s p a c e}(\mathbf{A})\}   \tag*{(7.221)}
$$

where  $\pmb{x}_{p}$ is any particular solution. It is standard to pick the particular solution with minimal  $\ell_{2}$ norm, i.e.,

$$
\hat{x}=\underset{\mathbf{x}}{\operatorname{argmin}}\left|\left|\mathbf{x}\right|\right|_{2}^{2}\text{s.t.}\mathbf{A}\mathbf{x}=\mathbf{b}   \tag*{(7.222)}
$$

We can compute the minimal norm solution using the right pseudo inverse:

$$
\boldsymbol{x}_{\mathrm{p i n v}}=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\boldsymbol{b}   \tag*{(7.223)}
$$

(See Section 7.5.3 for more details.)

To see this, suppose x is some other solution, so  $Ax = b$, and  $\mathbf{A}(x - x_{\mathrm{pinv}}) = 0$. Thus

$$
(\boldsymbol{x}-\boldsymbol{x}_{\mathrm{p i n v}})^{\top}\boldsymbol{x}_{\mathrm{p i n v}}=(\boldsymbol{x}-\boldsymbol{x}_{\mathrm{p i n v}})^{\top}\boldsymbol{A}^{\top}(\boldsymbol{A}\boldsymbol{A}^{\top})^{-1}\boldsymbol{b}=(\boldsymbol{A}(\boldsymbol{x}-\boldsymbol{x}_{\mathrm{p i n v}}))^{\top}(\boldsymbol{A}\boldsymbol{A}^{\top})^{-1}\boldsymbol{b}=0   \tag*{(7.224)}
$$

and hence  $(x - x_{\mathrm{pinv}}) \perp x_{\mathrm{pinv}}$. By Pythagoras's theorem, the norm of x is

$$
||\boldsymbol{x}||^{2}=||\boldsymbol{x}_{\mathrm{p i n v}}+\boldsymbol{x}-\boldsymbol{x}_{\mathrm{p i n v}}||^{2}=||\boldsymbol{x}_{\mathrm{p i n v}}||^{2}+||\boldsymbol{x}-\boldsymbol{x}_{\mathrm{p i n v}}||^{2}\geq||\boldsymbol{x}_{\mathrm{p i n v}}||^{2}   \tag*{(7.225)}
$$

Thus any solution apart from x_{pinv} has larger norm.

We can also solve the constrained optimization problem in Equation (7.222) by minimizing the following unconstrained objective

$$
\mathcal{L}(\boldsymbol{x},\boldsymbol{\lambda})=\boldsymbol{x}^{\top}\boldsymbol{x}+\boldsymbol{\lambda}^{\top}(\mathbf{A}\boldsymbol{x}-\boldsymbol{b})   \tag*{(7.226)}
$$

From Section 8.5.1, the optimality conditions are

$$
\nabla_{x}\mathcal{L}=2\boldsymbol{x}+\mathbf{A}^{\top}\boldsymbol{\lambda}=\mathbf{0},\nabla_{\boldsymbol{\lambda}}\mathcal{L}=\mathbf{A}\boldsymbol{x}-\boldsymbol{b}=\mathbf{0}   \tag*{(7.227)}
$$

From the first condition we have  $\boldsymbol{x} = -\boldsymbol{A}^{\mathrm{T}}\boldsymbol{\lambda}/2$. Subsituing into the second we get

$$
\mathbf{A}\boldsymbol{x}=-\frac{1}{2}\mathbf{A}\mathbf{A}^{\top}\boldsymbol{\lambda}=\boldsymbol{b}   \tag*{(7.228)}
$$

which implies  $\lambda = -2(\mathbf{A}\mathbf{A}^\top)^{-1}\mathbf{b}$. Hence  $\boldsymbol{x} = \mathbf{A}^\top(\mathbf{A}\mathbf{A}^\top)^{-1}\boldsymbol{b}$, which is the right pseudo inverse solution.

#### 7.7.3 Solving overconstrained systems (least squares estimation)

If $m > n$, we have an overdetermined solution, which typically does not have an exact solution, but we will try to find the solution that gets as close as possible to satisfying all of the constraints specified by $\mathbf{A}\mathbf{x} = \mathbf{b}$. We can do this by minimizing the following cost function, known as the least squares objective.⁴

$$
f(\boldsymbol{x})=\frac{1}{2}||\boldsymbol{A}\boldsymbol{x}-\boldsymbol{b}||_{2}^{2}   \tag*{(7.233)}
$$


---

Using matrix calculus results from Section 7.8 we have that the gradient is given by

$$
\boldsymbol{g}(\boldsymbol{x})=\frac{\partial}{\partial\boldsymbol{x}}\boldsymbol{f}(\boldsymbol{x})=\boldsymbol{A}^{\top}\boldsymbol{A}\boldsymbol{x}-\boldsymbol{A}^{\top}\boldsymbol{b}   \tag*{(7.234)}
$$

The optimum can be found by solving  $\boldsymbol{g}(\boldsymbol{x})=\boldsymbol{0}$. This gives

$$
\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\mathbf{A}^{\top}\mathbf{b}   \tag*{(7.235)}
$$

These are known as the normal equations, since, at the optimal solution,  $\mathbf{b} - \mathbf{A}\mathbf{x}$ is normal (orthogonal) to the range of  $\mathbf{A}$, as we explain in Section 11.2.2.2. The corresponding solution  $\hat{\mathbf{x}}$ is the ordinary least squares (OLS) solution, which is given by

$$
\hat{\boldsymbol{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\boldsymbol{b}   \tag*{(7.236)}
$$

The quantity  $\mathbf{A}^\dagger = (\mathbf{A}^\top \mathbf{A})^{-1} \mathbf{A}^\top$ is the left pseudo inverse of the (non-square) matrix  $\mathbf{A}$ (see Section 7.5.3 for more details).

We can check that the solution is unique by showing that the Hessian is positive definite. In this case, the Hessian is given by

$$
\mathbf{H}(\boldsymbol{x})=\frac{\partial^{2}}{\partial\boldsymbol{x}^{2}}f(\boldsymbol{x})=\mathbf{A}^{\top}\mathbf{A}   \tag*{(7.237)}
$$

If  $\mathbf{A}$ is full rank (so the columns of  $\mathbf{A}$ are linearly independent), then  $\mathbf{H}$ is positive definite, since for any  $\mathbf{v} > \mathbf{0}$, we have

$$
\boldsymbol{v}^{\mathrm{T}}(\mathbf{A}^{\mathrm{T}}\mathbf{A})\boldsymbol{v}=(\mathbf{A}\boldsymbol{v})^{\mathrm{T}}(\mathbf{A}\boldsymbol{v})=||\mathbf{A}\boldsymbol{v}||^{2}>0   \tag*{(7.238)}
$$

Hence in the full rank case, the least squares objective has a unique global minimum.

### 7.8 Matrix calculus

The topic of calculus concerns computing “rates of change” of functions as we vary their inputs. It is of vital importance to machine learning, as well as almost every other numerical discipline. In this section, we review some standard results. In some cases, we use some concepts and notation from matrix algebra, which we cover in Chapter 7. For more details on these results from a deep learning perspective, see [PH18].

#### 7.8.1 Derivatives

Consider a scalar-argument function  $f : \mathbb{R} \to \mathbb{R}$. We define its derivative at a point  $x$ to be the quantity

$$
f^{\prime}(x)\triangleq\lim_{h\to0}\frac{f(x+h)-f(x)}{h}   \tag*{(7.239)}
$$

assuming the limit exists. This measures how quickly the output changes when we move a small distance in input space away from x (i.e., the “rate of change” of the function). We can interpret  $f'(x)$ as the slope of the tangent line at  $f(x)$, and hence

$$
f(x+h)\approx f(x)+f^{\prime}(x)h   \tag*{(7.240)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

for small h.

We can compute a finite difference approximation to the derivative by using a finite step size h, as follows:

$$
f^{\prime}(x)\equiv\underbrace{\lim_{h\to0}\frac{f(x+h)-f(x)}{h}}_{forward difference}=\underbrace{\lim_{h\to0}\frac{f(x+h/2)-f(x-h/2)}{h}}_{central difference}=\underbrace{\lim_{h\to0}\frac{f(x)-f(x-h)}{h}}_{backward difference}   \tag*{(7.241)}
$$

The smaller the step size h, the better the estimate, although if h is too small, there can be errors due to numerical cancellation.

We can think of differentiation as an operator that maps functions to functions,  $D(f) = f'$, where  $f'(x)$ computes the derivative at  $x$ (assuming the derivative exists at that point). The use of the prime symbol  $f'$ to denote the derivative is called Lagrange notation. The second derivative function, which measures how quickly the gradient is changing, is denoted by  $f''$. The  $n'$th derivative function is denoted  $f^{(n)}$.

Alternatively, we can use  $\mathbf{Leibniz}$ notation, in which we denote the function by  $y = f(x)$, and its derivative by  $\frac{dy}{dx}$ or  $\frac{d}{dx}f(x)$. To denote the evaluation of the derivative at a point  $a$, we write  $\left.\frac{df}{dx}\right|_{x=a}$.

#### 7.8.2 Gradients

We can extend the notion of derivatives to handle vector-argument functions,  $f : \mathbb{R}^n \to \mathbb{R}$, by defining the partial derivative of  $f$ with respect to  $x_i$ to be

$$
\frac{\partial f}{\partial x_{i}}=\lim_{h\to0}\frac{f(\boldsymbol{x}+h\boldsymbol{e}_{i})-f(\boldsymbol{x})}{h}   \tag*{(7.242)}
$$

where  $e_i$ is the  $i'$th unit vector.

The gradient of a function at a point x is the vector of its partial derivatives:

$$
\boldsymbol{g}=\frac{\partial f}{\partial\boldsymbol{x}}=\nabla f=\begin{pmatrix}\frac{\partial f}{\partial x_{1}}\\ \vdots\\ \frac{\partial f}{\partial x_{n}}\end{pmatrix}   \tag*{(7.243)}
$$

To emphasize the point at which the gradient is evaluated, we can write

$$
g(x^{*})\triangleq\left.\frac{\partial f}{\partial x}\right|_{x^{*}}   \tag*{(7.244)}
$$

We see that the operator  $\nabla$ (pronounced “nabla”) maps a function  $f : \mathbb{R}^n \to \mathbb{R}$ to another function  $g : \mathbb{R}^n \to \mathbb{R}^n$. Since  $g()$ is a vector-valued function, it is known as a vector field. By contrast, the derivative function  $f'$ is a scalar field.

#### 7.8.3 Directional derivative

The directional derivative measures how much the function  $f : \mathbb{R}^n \to \mathbb{R}$ changes along a direction  $v$ in space. It is defined as follows

$$
D_{v}f(\boldsymbol{x})=\lim_{h\to0}\frac{f(\boldsymbol{x}+h\boldsymbol{v})-f(\boldsymbol{x})}{h}   \tag*{(7.245)}
$$
