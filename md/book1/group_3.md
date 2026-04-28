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

The core of the problem is that the model has enough parameters to perfectly fit the observed training data, so it can perfectly match the empirical distribution. However, in most cases the empirical distribution is not the same as the true distribution, so putting all the probability mass on the observed set of N examples will not leave over any probability for novel data in the future. That is, the model may not generalize.

The main solution to overfitting is to use regularization, which means to add a penalty term to the NLL (or empirical risk). Thus we optimize an objective of the form

$$
\mathcal{L}(\boldsymbol{\theta};\lambda)=\left[\frac{1}{N}\sum_{n=1}^{N}\ell(\boldsymbol{y}_{n},\boldsymbol{\theta};\boldsymbol{x}_{n})\right]+\lambda C(\boldsymbol{\theta})   \tag*{(4.89)}
$$

where λ ≥ 0 is the regularization parameter, and C(θ) is some form of complexity penalty.

A common complexity penalty is to use  $C(\boldsymbol{\theta}) = -\log p(\boldsymbol{\theta})$, where  $p(\boldsymbol{\theta})$ is the prior for  $\boldsymbol{\theta}$. If  $\ell$ is the log loss, the regularized objective becomes

$$
\mathcal{L}(\boldsymbol{\theta};\lambda)=-\frac{1}{N}\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})-\lambda\log p(\boldsymbol{\theta})   \tag*{(4.90)}
$$

By setting  $\lambda = 1$ and rescaling  $p(\boldsymbol{\theta})$ appropriately, we can equivalently minimize the following:

$$
\mathcal{L}(\boldsymbol{\theta};\lambda)=-\left[\sum_{n=1}^{N}\log p(\boldsymbol{y}_{n}|\boldsymbol{x}_{n},\boldsymbol{\theta})+\log p(\boldsymbol{\theta})\right]=-[\log p(\mathcal{D}|\boldsymbol{\theta})+\log p(\boldsymbol{\theta})]   \tag*{(4.91)}
$$

Minimizing this is equivalent to maximizing the log posterior:

$$
\hat{\boldsymbol{\theta}}=\underset{\boldsymbol{\theta}}{\operatorname{argmax}}\log p(\boldsymbol{\theta}|\mathcal{D})=\underset{\boldsymbol{\theta}}{\operatorname{argmax}}\left[\log p(\mathcal{D}|\boldsymbol{\theta})+\log p(\boldsymbol{\theta})-const\right]   \tag*{(4.92)}
$$

This is known as MAP estimation, which stands for maximum a posteriori estimation.

#### 4.5.1 Example: MAP estimation for the Bernoulli distribution

Consider again the coin tossing example. If we observe just one head, the MLE is  $\theta_{\text{mle}} = 1$, which predicts that all future coin tosses will also show up heads. To avoid such overfitting, we can add a penalty to  $\theta$ to discourage “extreme” values, such as  $\theta = 0$ or  $\theta = 1$. We can do this by using a beta distribution as our prior,  $p(\theta) = \text{Beta}(\theta | a, b)$, where  $a, b > 1$ encourages values of  $\theta$ near to  $a/(a + b)$ (see Section 2.7.4 for details). The log likelihood plus log prior becomes

$$
\begin{align*}\ell(\theta)&=\log p(\mathcal{D}|\theta)+\log p(\theta)\\&=[N_{1}\log\theta+N_{0}\log(1-\theta)]+[(a-1)\log(\theta)+(b-1)\log(1-\theta)]\end{align*}   \tag*{(4.93)}
$$

Using the method from Section 4.2.3 we find that the MAP estimate is

$$
\theta_{map}=\frac{N_{1}+a-1}{N_{1}+N_{0}+a+b-2}   \tag*{(4.95)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

If we set a = b = 2 (which weakly favors a value of  $\theta$ near 0.5), the estimate becomes

$$
\theta_{map}=\frac{N_{1}+1}{N_{1}+N_{0}+2}   \tag*{(4.96)}
$$

This is called add-one smoothing, and is a simple but widely used technique to avoid the zero count problem. (See also Section 4.6.2.9.)

The zero-count problem, and overfitting more generally, is analogous to a problem in philosophy called the black swan paradox. This is based on the ancient Western conception that all swans were white. In that context, a black swan was a metaphor for something that could not exist. (Black swans were discovered in Australia by European explorers in the 17th Century.) The term “black swan paradox” was first coined by the famous philosopher of science Karl Popper; the term has also been used as the title of a recent popular book [Tal07]. This paradox was used to illustrate the problem of induction, which is the problem of how to draw general conclusions about the future from specific observations from the past. The solution to the paradox is to admit that induction is in general impossible, and that the best we can do is to make plausible guesses about what the future might hold, by combining the empirical data with prior knowledge.

#### 4.5.2 Example: MAP estimation for the multivariate Gaussian  $*$

In Section 4.2.6, we showed that the MLE for the mean of an MVN is the empirical mean,  $\hat{\mu}_{\text{mle}} = \overline{y}$. We also showed that the MLE for the covariance is the empirical covariance,  $\hat{\Sigma} = \frac{1}{N} S_{\overline{y}}$.

In high dimensions the estimate for  $\Sigma$ can easily become singular. One solution to this is to perform MAP estimation, as we explain below.

##### 4.5.2.1 Shrinkage estimate

A convenient prior to use for  $\Sigma$ is the inverse Wishart prior. This is a distribution over positive definite matrices, where the parameters are defined in terms of a prior scatter matrix,  $\breve{S}$, and a prior sample size or strength  $\breve{N}$. One can show that the resulting MAP estimate is given by

$$
\hat{\mathbf{\Sigma}}_{\mathrm{map}}=\frac{\breve{\mathbf{S}}+\mathbf{S}_{\overline{y}}}{\breve{N}+N}=\frac{\breve{N}}{\breve{N}+N}\frac{\breve{\mathbf{S}}}{\breve{N}}+\frac{N}{\breve{N}+N}\frac{\mathbf{S}_{\overline{y}}}{N}=\lambda\mathbf{\Sigma}_{0}+(1-\lambda)\hat{\mathbf{\Sigma}}_{\mathrm{m l e}}   \tag*{(4.97)}
$$

where  $\lambda = \frac{\breve{N}}{\breve{N} + N}$ controls the amount of regularization.

A common choice (see e.g., [FR07, p6]) for the prior scatter matrix is to use  $\check{\mathbf{S}}=\check{N}$  $\text{diag}(\hat{\mathbf{\Sigma}}_{\text{mle}})$. With this choice, we find that the MAP estimate for  $\Sigma$ is given by

$$
\hat{\mathbf{\Sigma}}_{\mathrm{map}}(i,j)=\left\{\begin{array}{ll}\hat{\mathbf{\Sigma}}_{\mathrm{mle}}(i,j)&if i=j\\ (1-\lambda)\hat{\mathbf{\Sigma}}_{\mathrm{mle}}(i,j)&otherwise\end{array}\right.   \tag*{(4.98)}
$$

Thus we see that the diagonal entries are equal to their ML estimates, and the off-diagonal elements are “shrunk” somewhat towards 0. This technique is therefore called shrinkage estimation.

The other parameter we need to set is  $\lambda$, which controls the amount of regularization (shrinkage towards the MLE). It is common to set  $\lambda$ by cross validation (Section 4.5.5). Alternatively, we can use the closed-form formula provided in [LW04a; LW04b; SS05], which is the optimal

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_196_121_440_369.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_463_122_707_370.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_731_123_970_370.jpg" alt="Image" width="20%" /></div>

<div style="text-align: center;">Figure 4.4: Estimating a covariance matrix in $D = 50$dimensions using$N \in \{100, 50, 25\}$samples. We plot the eigenvalues in descending order for the true covariance matrix (solid black), the MLE (dotted blue) and the MAP estimate (dashed red), using Equation (4.98) with$\lambda = 0.9$. We also list the condition number of each matrix in the legend. We see that the MLE is often poorly conditioned, but the MAP estimate is numerically well behaved. Adapted from Figure 1 of [SS05]. Generated by shrinkcov plots.</div>

frequentist estimate if we use squared loss. This is implemented in the sklearn function https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html.

The benefits of this approach are illustrated in Figure 4.4. We consider fitting a 50-dimensional Gaussian to N = 100, N = 50 and N = 25 data points. We see that the MAP estimate is always well-conditioned, unlike the MLE (see Section 7.1.4.4 for a discussion of condition numbers). In particular, we see that the eigenvalue spectrum of the MAP estimate is much closer to that of the true matrix than the MLE's spectrum. The eigenvectors, however, are unaffected.

#### 4.5.3 Example: weight decay

In Figure 1.7, we saw how using polynomial regression with too high of a degree can result in overfitting. One solution is to reduce the degree of the polynomial. However, a more general solution is to penalize the magnitude of the weights (regression coefficients). We can do this by using a zero-mean Gaussian prior,  $p(\mathbf{w})$. The resulting MAP estimate is given by

$$
\hat{\boldsymbol{w}}_{\mathrm{map}}=\underset{\boldsymbol{w}}{\arg\min}\mathrm{N L L}(\boldsymbol{w})+\lambda||\boldsymbol{w}||_{2}^{2}   \tag*{(4.99)}
$$

where  $\|w\|_{2}^{2}=\sum_{d=1}^{D}w_{d}^{2}$. (We write  $\boldsymbol{w}$ rather than  $\boldsymbol{\theta}$, since it only really makes sense to penalize the magnitude of weight vectors, rather than other parameters, such as bias terms or noise variances.)

Equation (4.99) is called  $\ell_{2}$ regularization or weight decay. The larger the value of  $\lambda$, the more the parameters are penalized for being “large” (deviating from the zero-mean prior), and thus the less flexible the model.

In the case of linear regression, this kind of penalization scheme is called ridge regression. For example, consider the polynomial regression example from Section 1.2.2.2, where the predictor has the form

$$
f(x;\boldsymbol{w})=\sum_{d=0}^{D}w_{d}x^{d}=\boldsymbol{w}^{\mathsf{T}}[1,x,x^{2},\ldots,x^{D}]   \tag*{(4.100)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_202_133_552_378.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_610_132_959_381.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_202_433_552_678.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_601_446_959_684.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">Figure 4.5: (a-c) Ridge regression applied to a degree 14 polynomial fit to 21 datapoints. (d) MSE vs strength of regularizer. The degree of regularization increases from left to right, so model complexity decreases from left to right. Generated by linreg_poly_ridge.ipynb.</div>

Suppose we use a high degree polynomial, say $D = 14$, even though we have a small dataset with just $N = 21$examples. MLE for the parameters will enable the model to fit the data very well, by carefully adjusting the weights, but the resulting function is very “wiggly”, thus resulting in overfitting. Figure 4.5 illustrates how increasing$\lambda$can reduce overfitting. For more details on ridge regression, see Section 11.3.

#### 4.5.4 Picking the regularizer using a validation set

A key question when using regularization is how to choose the strength of the regularizer$ \lambda $: a small value means we will focus on minimizing empirical risk, which may result in overfitting, whereas a large value means we will focus on staying close to the prior, which may result in underfitting.

In this section, we describe a simple but very widely used method for choosing  $\lambda$. The basic idea is to partition the data into two disjoint sets, the training set  $\mathcal{D}_{\text{train}}$ and a validation set  $\mathcal{D}_{\text{valid}}$ (also called a development set). (Often we use about 80% of the data for the training set, and

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_439_139_724_316.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">Figure 4.6: Schematic of 5-fold cross validation.</div>

20% for the validation set.) We fit the model on  $\mathcal{D}_{\text{train}}$ (for each setting of  $\lambda$) and then evaluate its performance on  $\mathcal{D}_{\text{valid}}$. We then pick the value of  $\lambda$ that results in the best validation performance. (This optimization method is a 1d example of grid search, discussed in Section 8.8.)

To explain the method in more detail, we need some notation. Let us define the regularized empirical risk on a dataset as follows:

$$
R_{\lambda}(\boldsymbol{\theta},\mathcal{D})=\frac{1}{|\mathcal{D}|}\sum_{(\mathbf{x},\mathbf{y})\in\mathcal{D}}\ell(\mathbf{y},f(\mathbf{x};\boldsymbol{\theta}))+\lambda C(\boldsymbol{\theta})   \tag*{(4.101)}
$$

For each  $\lambda$, we compute the parameter estimate

$$
\hat{\boldsymbol{\theta}}_{\lambda}(\mathcal{D}_{train})=\underset{\boldsymbol{\theta}}{\arg\min}R_{\lambda}(\boldsymbol{\theta},\mathcal{D}_{train})   \tag*{(4.102)}
$$

We then compute the validation risk:

$$
R_{\lambda}^{\mathrm{v a l}}\triangleq R_{0}(\hat{\pmb{\theta}}_{\lambda}(\mathcal{D}_{\mathrm{t r a i n}}),\mathcal{D}_{\mathrm{v a l i d}})   \tag*{(4.103)}
$$

This is an estimate of the population risk, which is the expected loss under the true distribution  $p^{*}(\boldsymbol{x}, \boldsymbol{y})$. Finally we pick

$$
\lambda^{*}=\underset{\lambda\in\mathcal{S}}{\mathrm{a r g m i n}}R_{\lambda}^{\mathrm{v a l}}   \tag*{(4.104)}
$$

(This requires fitting the model once for each value of  $\lambda$ in S, although in some cases, this can be done more efficiently.)

After picking  $\lambda^*$, we can refit the model to the entire dataset,  $\mathcal{D} = \mathcal{D}_{\text{train}} \cup \mathcal{D}_{\text{valid}}$, to get

$$
\hat{\boldsymbol{\theta}}^{*}=\underset{\boldsymbol{\theta}}{\operatorname{a r g m i n}}R_{\lambda^{*}}(\boldsymbol{\theta},\mathcal{D})   \tag*{(4.105)}
$$

#### 4.5.5 Cross-validation

The above technique in Section 4.5.4 can work very well. However, if the size of the training set is small, leaving aside 20% for a validation set can result in an unreliable estimate of the model parameters.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

A simple but popular solution to this is to use cross validation (CV). The idea is as follows: we split the training data into  $K$ folds; then, for each fold  $k \in \{1, \ldots, K\}$, we train on all the folds but the  $k$'th, and test on the  $k$'th, in a round-robin fashion, as sketched in Figure 4.6. Formally, we have

$$
R_{\lambda}^{\mathrm{c v}}\triangleq\frac{1}{K}\sum_{k=1}^{K}R_{0}(\hat{\boldsymbol{\theta}}_{\lambda}(\mathcal{D}_{-k}),\mathcal{D}_{k})   \tag*{(4.106)}
$$

where  $\mathcal{D}_k$ is the data in the  $k$'th fold, and  $\mathcal{D}_{-k}$ is all the other data. This is called the cross-validated risk. Figure 4.6 illustrates this procedure for  $K = 5$. If we set  $K = N$, we get a method known as leave-one-out cross-validation, since we always train on  $N - 1$ items and test on the remaining one.

We can use the CV estimate as an objective inside of an optimization routine to pick the optimal hyperparameter,  $\hat{\lambda} = \argmin_{\lambda} R_{\lambda}^{\mathrm{cv}}$. Finally we combine all the available data (training and validation), and re-estimate the model parameters using  $\hat{\boldsymbol{\theta}} = \argmin_{\boldsymbol{\theta}} R_{\hat{\lambda}}(\boldsymbol{\theta}, \mathcal{D})$. See Section 5.4.3 for more details.

##### 4.5.5.1 The one standard error rule

CV gives an estimate of  $\hat{R}_\lambda$, but does not give any measure of uncertainty. A standard frequentist measure of uncertainty of an estimate is the  $\text{standard error of the mean}$, which is the mean of the sampling distribution of the estimate (see Section 4.7.1). We can compute this as follows. First let  $L_n = \ell(\mathbf{y}_n, f(\mathbf{x}_n; \hat{\boldsymbol{\theta}}_n(\mathcal{D}_{-n})))$ be the loss on the  $n$'th example, where we use the parameters that were estimated using whichever training fold excludes n. (Note that  $L_n$ depends on  $\lambda$, but we drop this from the notation.) Next let  $\hat{\mu} = \frac{1}{N} \sum_{n=1}^N L_n$ be the empirical mean and  $\hat{\sigma}^2 = \frac{1}{N} \sum_{n=1}^N (L_n - \hat{\mu})^2$ be the empirical variance. Given this, we define our estimate to be  $\hat{\mu}$, and the standard error of this estimate to be  $\text{se}(\hat{\mu}) = \frac{\hat{\sigma}}{\sqrt{N}}$. Note that  $\sigma$ measures the intrinsic variability of  $L_n$ across samples, whereas  $\text{se}(\hat{\mu})$ measures our uncertainty about the mean  $\hat{\mu}$.

Suppose we apply CV to a set of models and compute the mean and se of their estimated risks. A common heuristic for picking a model from these noisy estimates is to pick the value which corresponds to the simplest model whose risk is no more than one standard error above the risk of the best model; this is called the one-standard error rule [HTF01, p216].

##### 4.5.5.2 Example: ridge regression

As an example, consider picking the strength of the  $\ell_2$ regularizer for the ridge regression problem in Section 4.5.3. In Figure 4.7a, we plot the error vs  $\log(\lambda)$ on the train set (blue) and test set (red curve). We see that the test error has a U-shaped curve, where it decreases as we increase the regularizer, and then increases as we start to underfit. In Figure 4.7b, we plot the 5-fold CV estimate of the test MSE vs  $\log(\lambda)$. We see that the minimum CV error is close to the optimal value for the test set (although it does underestimate the spike in the test error for large lambda, due to the small sample size.)

#### 4.5.6 Early stopping

A very simple form of regularization, which is often very effective in practice (especially for complex models), is known as early stopping. This leverages the fact that optimization algorithms are

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_196_150_539_407.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_609_137_947_408.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.7: Ridge regression is applied to a degree 14 polynomial fit to 21 datapoints shown in Figure 4.5 for different values of the regularizer  $\lambda$. The degree of regularization increases from left to right, so model complexity decreases from left to right. (a) MSE on train (blue) and test (red) vs  $\log(\lambda)$. (b) 5-fold cross-validation estimate of test MSE; error bars are standard error of the mean. Vertical line is the point chosen by the one standard error rule. Generated by polyfitRidgeCV.ipynb.</div>

iterative, and so they take many steps to move away from the initial parameter estimates. If we detect signs of overfitting (by monitoring performance on the validation set), we can stop the optimization process, to prevent the model memorizing too much information about the training set. See Figure 4.8 for an illustration.

#### 4.5.7 Using more data

As the amount of data increases, the chance of overfitting (for a model of fixed complexity) decreases (assuming the data contains suitably informative examples, and is not too redundant). This is illustrated in Figure 4.9. We show the MSE on the training and test sets for four different models (polynomials of increasing degree) as a function of the training set size N. (A plot of error vs training set size is known as a learning curve.) The horizontal black line represents the Bayes error, which is the error of the optimal predictor (the true model) due to inherent noise. (In this example, the true model is a degree 2 polynomial, and the noise has a variance of  $\sigma^2 = 4$; this is called the noise floor, since we cannot go below it.)

We notice several interesting things. First, the test error for degree 1 remains high, even as N increases, since the model is too simple to capture the truth; this is called underfitting. The test error for the other models decreases to the optimal level (the noise floor), but it decreases more rapidly for the simpler models, since they have fewer parameters to estimate. The gap between the test error and training error is larger for more complex models, but decreases as N grows.

Another interesting thing we can note is that the training error (blue line) initially increases with N, at least for the models that are sufficiently flexible. The reason for this is as follows: as the data set gets larger, we observe more distinct input-output pattern combinations, so the task of fitting the data becomes harder. However, eventually the training set will come to resemble the test set, and

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_247_137_592_380.jpg" alt="Image" width="29%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_597_137_944_378.jpg" alt="Image" width="30%" /></div>

<div style="text-align: center;">Figure 4.8: Performance of a text classifier (a neural network applied to a bag of word embeddings using average pooling) vs number of training epochs on the IMDB movie sentiment dataset. Blue = train, red = validation. (a) Cross entropy loss. Early stopping is triggered at about epoch 25. (b) Classification accuracy. Generated by imdb_mlp_bow_tf.ipynb.</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_190_524_564_778.jpg" alt="Image" width="32%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_600_524_966_777.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_189_825_563_1076.jpg" alt="Image" width="32%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_600_826_966_1075.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">Figure 4.9: MSE on training and test sets vs size of training set, for data generated from a degree 2 polynomial with Gaussian noise of variance  $\sigma^2 = 4$. We fit polynomial models of varying degree to this data. Generated by linreg_poly_vs_n.ipynb.</div>


---

the error rates will converge, and will reflect the optimal performance of that model.

### 4.6 Bayesian statistics *

So far, we have discussed several ways to estimate parameters from data. However, these approaches ignore any uncertainty in the estimates, which can be important for some applications, such as active learning, or avoiding overfitting, or just knowing how much to trust the estimate of some scientifically meaningful quantity. In statistics, modeling uncertainty about parameters using a probability distribution (as opposed to just computing a point estimate) is known as inference.

In this section, we use the posterior distribution to represent our uncertainty. This is the approach adopted in the field of Bayesian statistics. We give a brief introduction here, but more details can be found in the sequel to this book, [Mur23], as well as other good books, such as [Lam18; Kru15; McE20; Gel+14; MKL21; MFR20].

To compute the posterior, we start with a  $\text{prior}$ distribution  $p(\boldsymbol{\theta})$, which reflects what we know before seeing the data. We then define a likelihood function  $p(\mathcal{D}|\boldsymbol{\theta})$, which reflects the data we expect to see for each setting of the parameters. We then use Bayes rule to condition the prior on the observed data to compute the posterior  $p(\boldsymbol{\theta}|\mathcal{D})$ as follows:

$$
p(\boldsymbol{\theta}|\mathcal{D})=\frac{p(\boldsymbol{\theta})p(\mathcal{D}|\boldsymbol{\theta})}{p(\mathcal{D})}=\frac{p(\boldsymbol{\theta})p(\mathcal{D}|\boldsymbol{\theta})}{\int p(\boldsymbol{\theta}^{\prime})p(\mathcal{D}|\boldsymbol{\theta}^{\prime})d\boldsymbol{\theta}^{\prime}}   \tag*{(4.107)}
$$

The denominator  $p(\mathcal{D})$ is called the marginal likelihood, since it is computed by marginalizing over (or integrating out) the unknown  $\theta$. This can be interpreted as the average probability of the data, where the average is wrt the prior. Note, however, that  $p(\mathcal{D})$ is a constant, independent of  $\theta$, so we will often ignore it when we just want to infer the relative probabilities of  $\theta$ values.

Equation (4.107) is analogous to the use of Bayes rule for COVID-19 testing in Section 2.3.1. The difference is that the unknowns correspond to parameters of a statistical model, rather than the unknown disease state of a patient. In addition, we usually condition on a set of observations D, as opposed to a single observation (such as a single test outcome). In particular, for a supervised or conditional model, the observed data has the form  $\mathcal{D} = \{(\boldsymbol{x}_n, \boldsymbol{y}_n) : n = 1 : N\}$. For an unsupervised or unconditional model, the observed data has the form  $\mathcal{D} = \{(\boldsymbol{y}_n) : n = 1 : N\}$.

Once we have computed the posterior over the parameters, we can compute the posterior predictive distribution over outputs given inputs by marginalizing out the unknown parameters. In the supervised/conditional case, this becomes

$$
p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})=\int p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})p(\boldsymbol{\theta}|\mathcal{D})d\boldsymbol{\theta}   \tag*{(4.108)}
$$

This can be viewed as a form of Bayes model averaging (BMA), since we are making predictions using an infinite set of models (parameter values), each one weighted by how likely it is. The use of BMA reduces the chance of overfitting (Section 1.2.3), since we are not just using the single best model.

#### 4.6.1 Conjugate priors

In this section, we consider a set of (prior, likelihood) pairs for which we can compute the posterior in closed form. In particular, we will use priors that are “conjugate” to the likelihood. We say that

---

a prior $p(\boldsymbol{\theta}) \in \mathcal{F}$is a conjugate prior for a likelihood function$p(\mathcal{D}|\boldsymbol{\theta})$if the posterior is in the same parameterized family as the prior, i.e.,$p(\boldsymbol{\theta}|\mathcal{D}) \in \mathcal{F}$. In other words, $\mathcal{F}$is closed under Bayesian updating. If the family$\mathcal{F}$corresponds to the exponential family (defined in Section 3.4), then the computations can be performed in closed form.

In the sections below, we give some common examples of this framework, which we will use later in the book. For simplicity, we focus on unconditional models (i.e., there are only outcomes or targets y, and no inputs or features x); we relax this assumption in Section 4.6.7.

#### 4.6.2 The beta-binomial model

Suppose we toss a coin$N$times, and want to infer the probability of heads. Let$y_n = 1$denote the event that the$n$'th trial was heads, $y_n = 0$represent the event that the$n$'th trial was tails, and let $\mathcal{D} = \{y_n : n = 1 : N\}$be all the data. We assume$y_n \sim \mathrm{Ber}(\theta)$, where $\theta \in [0, 1]$is the rate parameter (probability of heads). In this section, we discuss how to compute$p(\theta|\mathcal{D})$.

##### 4.6.2.1 Bernoulli likelihood

We assume the data are  $\underline{\text{iid}}$ or independent and identically distributed. Thus the likelihood has the form

$$
p(\mathcal{D}|\theta)=\prod_{n=1}^{N}\theta^{y_{n}}(1-\theta)^{1-y_{n}}=\theta^{N_{1}}(1-\theta)^{N_{0}}   \tag*{(4.109)}
$$

where we have defined  $N_1 = \sum_{n=1}^{\infty} \mathbb{1}(y_n = 1)$ and  $N_0 = \sum_{n=1}^{\infty} \mathbb{1}(y_n = 0)$, representing the number of heads and tails. These counts are called the sufficient statistics of the data, since this is all we need to know about  $\mathcal{D}$ to infer  $\theta$. The total count,  $N = N_0 + N_1$, is called the sample size.

##### 4.6.2.2 Binomial likelihood

Note that we can also consider a Binomial likelihood model, in which we perform N trials and observe the number of heads, y, rather than observing a sequence of coin tosses. Now the likelihood has the following form:

$$
p(\mathcal{D}|\theta)=\mathrm{B i n}(y|N,\theta)=\binom{N}{y}\theta^{y}(1-\theta)^{N-y}   \tag*{(4.110)}
$$

The scaling factor  $\binom{N}{y}$ is independent of  $\theta$, so we can ignore it. Thus this likelihood is proportional to the Bernoulli likelihood in Equation (4.109), so our inferences about  $\theta$ will be the same for both models.

##### 4.6.2.3 Prior

To simplify the computations, we will assume that the prior  $p(\boldsymbol{\theta}) \in \mathcal{F}$ is a conjugate prior for the likelihood function  $p(\boldsymbol{y}|\boldsymbol{\theta})$. This means that the posterior is in the same parameterized family as the prior, i.e.,  $p(\boldsymbol{\theta}|\mathcal{D}) \in \mathcal{F}$.

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_242_131_529_330.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_653_131_935_328.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.10: Updating a Beta prior with a Bernoulli likelihood with sufficient statistics  $N_{1}=4, N_{0}=1$. (a) Beta(2,2) prior. (b) Uniform Beta(1,1) prior. Generated by beta_binom_post_plot.ipynb.</div>

To ensure this property when using the Bernoulli (or Binomial) likelihood, we should use a prior of the following form:

$$
p(\theta)\propto\theta^{\breve{\alpha}-1}(1-\theta)^{\breve{\beta}-1}\propto\mathrm{Beta}(\theta|\breve{\alpha},\breve{\beta})   \tag*{(4.111)}
$$

We recognize this as the pdf of a beta distribution (see Section 2.7.4).

##### 4.6.2.4 Posterior

If we multiply the Bernoulli likelihood in Equation (4.109) with the beta prior in Equation (2.136) we get a beta posterior:

$$
p(\theta|\mathcal{D})\propto\theta^{N_{1}}(1-\theta)^{N_{0}}\theta^{\alpha-1}(1-\theta)^{\widetilde{\beta}-1}   \tag*{(4.112)}
$$

$$
\propto Beta(\theta|\ \breve{\alpha}+N_{1},\breve{\beta}+N_{0})   \tag*{(4.113)}
$$

$$
=\mathrm{Beta}(\theta|\hat{\alpha},\hat{\beta})   \tag*{(4.114)}
$$

where  $\widehat{\alpha}^{\triangle}\check{\alpha} + N_{1}$ and  $\widehat{\beta}^{\triangle}\check{\beta} + N_{0}$ are the parameters of the posterior. Since the posterior has the same functional form as the prior, we say that the beta distribution is a conjugate prior for the Bernoulli likelihood.

The parameters of the prior are called hyper-parameters. It is clear that (in this example) the hyper-parameters play a role analogous to the sufficient statistics; they are therefore often called pseudo counts. We see that we can compute the posterior by simply adding the observed counts (from the likelihood) to the pseudo counts (from the prior).

The strength of the prior is controlled by  $N = \bar{\alpha} + \beta$; this is called the equivalent sample size, since it plays a role analogous to the observed sample size,  $N = N_0 + N_1$.

##### 4.6.2.5 Example

For example, suppose we set  $\check{\alpha}=\check{\beta}=2$. This is like saying we believe we have already seen two heads and two tails before we see the actual data; this is a very weak preference for the value of  $\theta=0.5$.

---

The effect of using this prior is illustrated in Figure 4.10a. We see the posterior (blue line) is a “compromise” between the prior (red line) and the likelihood (black line).

If we set  $\tilde{\alpha} = \tilde{\beta} = 1$, the corresponding prior becomes the uniform distribution:

$$
p(\theta)=\operatorname{Beta}(\theta|1,1)\propto\theta^{0}(1-\theta)^{0}=\operatorname{Unif}(\theta|0,1)   \tag*{(4.115)}
$$

The effect of using this prior is illustrated in Figure 4.10b. We see that the posterior has exactly the same shape as the likelihood, since the prior was “uninformative”.

##### 4.6.2.6 Posterior mode (MAP estimate)

The most probable value of the parameter is given by the MAP estimate

$$
\hat{\theta}_{\mathrm{m a p}}=\arg\max_{\theta}p(\theta|\mathcal{D})   \tag*{(4.116)}
$$

$$
=\arg\max_{\theta}\log p(\theta|\mathcal{D})   \tag*{(4.117)}
$$

$$
=\arg\max_{\theta}\log p(\theta)+\log p(\mathcal{D}|\theta)   \tag*{(4.118)}
$$

Using calculus, one can show that this is given by

$$
\hat{\theta}_{map}=\frac{\breve{\alpha}+N_{1}-1}{\breve{\alpha}+N_{1}-1+\breve{\beta}+N_{0}-1}   \tag*{(4.119)}
$$

If we use a Beta(θ|2,2) prior, this amounts to add-one smoothing:

$$
\hat{\theta}_{map}=\frac{N_{1}+1}{N_{1}+1+N_{0}+1}=\frac{N_{1}+1}{N+2}   \tag*{(4.120)}
$$

If we use a uniform prior, p(θ) ∝ 1, the MAP estimate becomes the MLE, since log p(θ) = 0:

$$
\hat{\theta}_{\mathrm{m l e}}=\arg\max_{\theta}\log p(\mathcal{D}|\theta)   \tag*{(4.121)}
$$

When we use a Beta prior, the uniform distribution is  $\bar{\alpha}=\bar{\beta}=1$. In this case, the MAP estimate reduces to the MLE:

$$
\hat{\theta}_{mle}=\frac{N_{1}}{N_{1}+N_{0}}=\frac{N_{1}}{N}   \tag*{(4.122)}
$$

If  $N_1 = 0$, we will estimate that  $p(Y = 1) = 0.0$, which says that we do not predict any future observations to be 1. This is a very extreme estimate, that is likely due to insufficient data. We can solve this problem using a MAP estimate with a stronger prior, or using a fully Bayesian approach, in which we marginalize out  $\theta$ instead of estimating it, as explained in Section 4.6.2.9.

##### 4.6.2.7 Posterior mean

The posterior mode can be a poor summary of the posterior, since it corresponds to a single point. The posterior mean is a more robust estimate, since it integrates over the whole space.

---

If  $p(\theta|\mathcal{D}) = \mathrm{Beta}(\theta|\hat{\alpha},\hat{\beta})$, then the posterior mean is given by

$$
\overline{{\theta}}\triangleq\mathbb{E}\left[\theta|\mathcal{D}\right]=\frac{\widehat{\alpha}}{\widehat{\beta}+\widehat{\alpha}}=\frac{\widehat{\alpha}}{\widehat{N}}   \tag*{(4.123)}
$$

where  $\widehat{N}=\widehat{\beta}+\widehat{\alpha}$ is the strength (equivalent sample size) of the posterior.

We will now show that the posterior mean is a convex combination of the prior mean,  $m = \tilde{\alpha} / \tilde{N}$ (where  $\tilde{N} \triangleq \tilde{\alpha} + \tilde{\beta}$ is the prior strength), and the MLE:  $\hat{\theta}_{\text{mle}} = \frac{N_1}{N}$:

$$
\mathbb{E}\left[\theta|\mathcal{D}\right]=\frac{\breve{\alpha}+N_{1}}{\breve{\alpha}+N_{1}+\breve{\beta}+N_{0}}=\frac{\breve{N}m+N_{1}}{N+\breve{N}}=\frac{\breve{N}}{N+\breve{N}}m+\frac{N}{N+\breve{N}}\frac{N_{1}}{N}=\lambda m+(1-\lambda)\hat{\theta}_{\mathrm{m l e}}   \tag*{(4.124)}
$$

where  $\lambda = \frac{\overline{N}}{\overline{N}}$ is the ratio of the prior to posterior equivalent sample size. So the weaker the prior, the smaller is  $\lambda$, and hence the closer the posterior mean is to the MLE.

##### 4.6.2.8 Posterior variance

To capture some notion of uncertainty in our estimate, a common approach is to compute the standard error of our estimate, which is just the posterior standard deviation:

$$
\mathrm{s e}(\theta)=\sqrt{\mathbb{V}\left[\theta|\mathcal{D}\right]}   \tag*{(4.125)}
$$

In the case of the Bernoulli model, we showed that the posterior is a beta distribution. The variance of the beta posterior is given by

$$
\mathbb{V}\left[\theta|\mathcal{D}\right]=\frac{\widehat{\alpha}\widehat{\beta}}{(\widehat{\alpha}+\widehat{\beta})^{2}(\widehat{\alpha}+\widehat{\beta}+1)}=\mathbb{E}\left[\theta|\mathcal{D}\right]^{2}\frac{\widehat{\beta}}{\widehat{\alpha}\left(1+\widehat{\alpha}+\widehat{\beta}\right)}   \tag*{(4.126)}
$$

where  $\widehat{\alpha}=\widetilde{\alpha}+N_{1}$ and  $\widehat{\beta}=\widetilde{\beta}+N_{0}$. If  $N\gg\widetilde{\alpha}+\widetilde{\beta}$, this simplifies to

$$
\mathbb{V}\left[\theta|\mathcal{D}\right]\approx\frac{N_{1}N_{0}}{N^{3}}=\frac{\hat{\theta}(1-\hat{\theta})}{N}   \tag*{(4.127)}
$$

where  $\hat{\theta}$ is the MLE. Hence the standard error is given by

$$
\sigma=\sqrt{\mathbb{V}\left[\theta|\mathcal{D}\right]}\approx\sqrt{\frac{\hat{\theta}(1-\hat{\theta})}{N}}   \tag*{(4.128)}
$$

We see that the uncertainty goes down at a rate of  $1/\sqrt{N}$. We also see that the uncertainty (variance) is maximized when  $\hat{\theta} = 0.5$, and is minimized when  $\hat{\theta}$ is close to 0 or 1. This makes sense, since it is easier to be sure that a coin is biased than to be sure that it is fair.

##### 4.6.2.9 Posterior predictive

Suppose we want to predict future observations. A very common approach is to first compute an estimate of the parameters based on training data,  $\hat{\theta}(\mathcal{D})$, and then to plug that parameter back into the model and use  $p(y|\hat{\theta})$ to predict the future; this is called a plug-in approximation. However, this can result in overfitting. As an extreme example, suppose we have seen N = 3 heads in a row. The MLE is  $\hat{\theta} = 3/3 = 1$. However, if we use this estimate, we would predict that tails are impossible.

One solution to this is to compute a MAP estimate, and plug that in, as we discussed in Section 4.5.1. Here we discuss a fully Bayesian solution, in which we marginalize out  $\theta$.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_452_128_733_326.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">Figure 4.11: Illustration of sequential Bayesian updating for the beta-Bernoulli model. Each colored box represents the predicted distribution  $p(x_t|\mathbf{h}_t)$, where  $\mathbf{h}_t = (N_{1,t}, N_{0,t})$ is the sufficient statistic derived from history of observations up until time  $t$, namely the total number of heads and tails. The probability of heads (blue bar) is given by  $p(x_t = 1|\mathbf{h}_t) = (N_{t,1} + 1)/(t + 2)$, assuming we start with a uniform Beta( $\theta | 1,1$) prior. From Figure 3 of [Ort+19]. Used with kind permission of Pedro Ortega.</div>

##### Bernoulli model

For the Bernoulli model, the resulting posterior predictive distribution has the form

$$
p(y=1|\mathcal{D})=\int_{0}^{1}p(y=1|\theta)p(\theta|\mathcal{D})d\theta   \tag*{(4.129)}
$$

$$
=\int_{0}^{1}\theta\operatorname{Beta}(\theta|\widehat{\alpha},\widehat{\beta})d\theta=\mathbb{E}\left[\theta|\mathcal{D}\right]=\frac{\widehat{\alpha}}{\widehat{\alpha}+\widehat{\beta}}   \tag*{(4.130)}
$$

In Section 4.5.1, we had to use the Beta(2,2) prior to recover add-one smoothing, which is a rather unnatural prior. In the Bayesian approach, we can get the same effect using a uniform prior,  $p(\theta) = \operatorname{Beta}(\theta|1,1)$, since the predictive distribution becomes

$$
p(y=1|\mathcal{D})=\frac{N_{1}+1}{N_{1}+N_{0}+2}   \tag*{(4.131)}
$$

This is known as Laplace’s rule of succession. See Figure 4.11 for an illustration of this in the sequential setting.

##### Binomial model

Now suppose we were interested in predicting the number of heads in M > 1 future coin tossing trials, i.e., we are using the binomial model instead of the Bernoulli model. The posterior over  $\theta$ is the same as before, but the posterior predictive distribution is different:

$$
\begin{align*}p(y|\mathcal{D},M)&=\int_{0}^{1}\mathrm{Bin}(y|M,\theta)\mathrm{Beta}(\theta|\widehat{\alpha},\widehat{\beta})d\theta\\&=\binom{M}{y}\frac{1}{B(\widehat{\alpha},\widehat{\beta})}\int_{0}^{1}\theta^{y}(1-\theta)^{M-y}\theta^{\widehat{\alpha}-1}(1-\theta)^{\widehat{\beta}-1}d\theta\end{align*}   \tag*{(4.132)}
$$


---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_253_122_504_329.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_660_121_912_328.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.12: (a) Posterior predictive distributions for 10 future trials after seeing  $N_{1}=4$ heads and  $N_{0}=1$ tails. (b) Plug-in approximation based on the same data. In both cases, we use a uniform prior. Generated by beta_binom_post_pred_plot.ipynb.</div>

We recognize the integral as the normalization constant for a  $\mathrm{Beta}(\widehat{\alpha} + y, M - y + \widehat{\beta})$ distribution. Hence

$$
\int_{0}^{1}\theta^{y+\widehat{\alpha}-1}(1-\theta)^{M-y+\widehat{\beta}-1}d\theta=B(y+\widehat{\alpha},M-y+\widehat{\beta})   \tag*{(4.134)}
$$

Thus we find that the posterior predictive is given by the following, known as the (compound) beta-binomial distribution:

$$
B b(x|M,\widehat{\alpha},\widehat{\beta})\triangleq\binom{M}{x}\frac{B(x+\widehat{\alpha},M-x+\widehat{\beta})}{B(\widehat{\alpha},\widehat{\beta})}   \tag*{(4.135)}
$$

In Figure 4.12(a), we plot the posterior predictive density for M = 10 after seeing  $N_1 = 4$ heads and  $N_0 = 1$ tails, when using a uniform Beta(1,1) prior. In Figure 4.12(b), we plot the plug-in approximation, given by

$$
p(\theta|\mathcal{D})\approx\delta(\theta-\hat{\theta})   \tag*{(4.136)}
$$

$$
p(y|\mathcal{D},M)=\int_{0}^{1}\mathrm{B i n}(y|M,\theta)p(\theta|\mathcal{D})d\theta=\mathrm{B i n}(y|M,\hat{\theta})   \tag*{(4.137)}
$$

where  $\theta$ is the MAP estimate. Looking at Figure 4.12, we see that the Bayesian prediction has longer tails, spreading its probability mass more widely, and is therefore less prone to overfitting and black-swan type paradoxes. (Note that we use a uniform prior in both cases, so the difference is not arising due to the use of a prior; rather, it is due to the fact that the Bayesian approach integrates out the unknown parameters when making its predictions.)

##### 4.6.2.10 Marginal likelihood

The marginal likelihood or evidence for a model M is defined as

$$
p(\mathcal{D}|\mathcal{M})=\int p(\boldsymbol{\theta}|\mathcal{M})p(\mathcal{D}|\boldsymbol{\theta},\mathcal{M})d\boldsymbol{\theta}   \tag*{(4.138)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

When performing inference for the parameters of a specific model, we can ignore this term, since it is constant wrt  $\theta$. However, this quantity plays a vital role when choosing between different models, as we discuss in Section 5.2.2. It is also useful for estimating the hyperparameters from data (an approach known as empirical Bayes), as we discuss in Section 4.6.5.3.

In general, computing the marginal likelihood can be hard. However, in the case of the beta-Bernoulli model, the marginal likelihood is proportional to the ratio of the posterior normalizer to the prior normalizer. To see this, recall that the posterior for the beta-binomial models is given by  $p(\theta|\mathcal{D}) = \text{Beta}(\theta|a', b')$, where  $a' = a + N_1$ and  $b' = b + N_0$. We know the normalization constant of the posterior is  $B(a', b')$. Hence

$$
p(\theta|\mathcal{D})=\frac{p(\mathcal{D}|\theta)p(\theta)}{p(\mathcal{D})}   \tag*{(4.139)}
$$

$$
=\frac{1}{p(\mathcal{D})}\left[\frac{1}{B(a,b)}\theta^{a-1}(1-\theta)^{b-1}\right]\left[\binom{N}{N_{1}}\theta^{N_{1}}(1-\theta)^{N_{0}}\right]   \tag*{(4.140)}
$$

$$
=\binom{N}{N_{1}}\frac{1}{p(\mathcal{D})}\frac{1}{B(a,b)}\left[\theta^{a+N_{1}-1}(1-\theta)^{b+N_{0}-1}\right]   \tag*{(4.141)}
$$

So

$$
\frac{1}{B(a+N_{1},b+N_{0})}=\binom{N}{N_{1}}\frac{1}{p(\mathcal{D})}\frac{1}{B(a,b)}   \tag*{(4.142)}
$$

$$
p(\mathcal{D})=\binom{N}{N_{1}}\frac{B(a+N_{1},b+N_{0})}{B(a,b)}   \tag*{(4.143)}
$$

The marginal likelihood for the beta-Bernoulli model is the same as above, except it is missing the  $\binom{N}{N_{1}}$ term.

##### 4.6.2.11 Mixtures of conjugate priors

The beta distribution is a conjugate prior for the binomial likelihood, which enables us to easily compute the posterior in closed form, as we have seen. However, this prior is rather restrictive. For example, suppose we want to predict the outcome of a coin toss at a casino, and we believe that the coin may be fair, but may equally likely be biased towards heads. This prior cannot be represented by a beta distribution. Fortunately, it can be represented as a mixture of beta distributions. For example, we might use

$$
p(\theta)=0.5Beta(\theta|20,20)+0.5Beta(\theta|30,10)   \tag*{(4.144)}
$$

If  $\theta$ comes from the first distribution, the coin is fair, but if it comes from the second, it is biased towards heads.

We can represent a mixture by introducing a latent indicator variable h, where h = k means that  $\theta$ comes from mixture component k. The prior has the form

$$
p(\theta)=\sum_{k}p(h=k)p(\theta|h=k)   \tag*{(4.145)}
$$


---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_450_121_716_339.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">Figure 4.13: A mixture of two Beta distributions. Generated by mixbetademo.ipynb.</div>

where each $p(\theta|h=k)$is conjugate, and$p(h=k)$ are called the (prior) mixing weights. One can show (Exercise 4.6) that the posterior can also be written as a mixture of conjugate distributions as follows:

$$
p(\theta|\mathcal{D})=\sum_{k}p(h=k|\mathcal{D})p(\theta|\mathcal{D},h=k)   \tag*{(4.146)}
$$

where  $p(h = k|\mathcal{D})$ are the posterior mixing weights given by

$$
p(h=k|\mathcal{D})=\frac{p(h=k)p(\mathcal{D}|h=k)}{\sum_{k^{\prime}}p(h=k^{\prime})p(\mathcal{D}|h=k^{\prime})}   \tag*{(4.147)}
$$

Here the quantity p(D|h = k) is the marginal likelihood for mixture component k (see Section 4.6.2.10).

Returning to our example above, if we have the prior in Equation (4.144), and we observe  $N_{1}=20$ heads and  $N_{0}=10$ tails, then, using Equation (4.143), the posterior becomes

$$
p(\theta|\mathcal{D})=0.346Beta(\theta|40,30)+0.654Beta(\theta|50,20)   \tag*{(4.148)}
$$

See Figure 4.13 for an illustration.

We can compute the posterior probability that the coin is biased towards heads as follows:

$$
\Pr(\theta>0.5|\mathcal{D})=\sum_{k}\Pr(\theta>0.5|\mathcal{D},h=k)p(h=k|\mathcal{D})=0.9604   \tag*{(4.149)}
$$

If we just used a single Beta(20,20) prior, we would get a slightly smaller value of  $\Pr(\theta > 0.5|\mathcal{D}) = 0.8858$. So if we were “suspicious” initially that the casino might be using a biased coin, our fears would be confirmed more quickly than if we had to be convinced starting with an open mind.

#### 4.6.3 The Dirichlet-multinomial model

In this section, we generalize the results from Section 4.6.2 from binary variables (e.g., coins) to K-ary variables (e.g., dice).

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

##### 4.6.3.1 Likelihood

Let  $Y \sim \text{Cat}(\theta)$ be a discrete random variable drawn from a categorical distribution. The likelihood has the form

$$
p(\mathcal{D}|\boldsymbol{\theta})=\prod_{n=1}^{N}\mathrm{Cat}(y_{n}|\boldsymbol{\theta})=\prod_{n=1}^{N}\prod_{c=1}^{C}\theta_{c}^{\mathbb{I}(y_{n}=c)}=\prod_{c=1}^{C}\theta_{c}^{N_{c}}   \tag*{(4.150)}
$$

where  $N_c = \sum_n \mathbb{I}(y_n = c)$.

##### 4.6.3.2 Prior

The conjugate prior for a categorical distribution is the Dirichlet distribution, which is a multivariate generalization of the beta distribution. This has support over the probability simplex, defined by

$$
S_{K}=\left\{\boldsymbol{\theta}:0\leq\theta_{k}\leq1,\sum_{k=1}^{K}\theta_{k}=1\right\}   \tag*{(4.151)}
$$

The pdf of the Dirichlet is defined as follows:

$$
\mathrm{Dir}(\boldsymbol{\theta}|\breve{\boldsymbol{\alpha}})\triangleq\frac{1}{B(\breve{\boldsymbol{\alpha}})}\prod_{k=1}^{K}\theta_{k}^{\breve{\alpha}_{k}-1}\mathbb{I}\left(\boldsymbol{\theta}\in S_{K}\right)   \tag*{(4.152)}
$$

where  $B(\breve{\alpha})$ is the multivariate beta function,

$$
B(\breve{\alpha})\triangleq\frac{\prod_{k=1}^{K}\Gamma(\breve{\alpha}_{k})}{\Gamma(\sum_{k=1}^{K}\breve{\alpha}_{k})}   \tag*{(4.153)}
$$

Figure 4.14 shows some plots of the Dirichlet when $K = 3$. We see that $\widetilde{\alpha}_0 = \sum_k \widetilde{\alpha}_k$controls the strength of the distribution (how peaked it is), and the$\widetilde{\alpha}_k$control where the peak occurs. For example, Dir(1, 1, 1) is a uniform distribution, Dir(2, 2, 2) is a broad distribution centered at (1/3, 1/3, 1/3), and Dir(20, 20, 20) is a narrow distribution centered at (1/3, 1/3, 1/3). Dir(3, 3, 20) is an asymmetric distribution that puts more density in one of the corners. If$\widetilde{\alpha}_k < 1$for all$k$, we get “spikes” at the corners of the simplex. Samples from the distribution when $\widetilde{\alpha}_k < 1$ will be sparse, as shown in Figure 4.15.

##### 4.6.3.3 Posterior

We can combine the multinomial likelihood and Dirichlet prior to compute the posterior, as follows:

$$
p(\boldsymbol{\theta}|\mathcal{D})\propto p(\mathcal{D}|\boldsymbol{\theta})\mathrm{Dir}(\boldsymbol{\theta}|\boldsymbol{\check{\alpha}})   \tag*{(4.154)}
$$

$$
=\left[\prod_{k}\theta_{k}^{N_{k}}\right]\left[\prod_{k}\theta_{k}^{\breve{\alpha}_{k}-1}\right]   \tag*{(4.155)}
$$

$$
=\mathrm{Dir}(\boldsymbol{\theta}|\boldsymbol{\alpha}_{1}+N_{1},\ldots,\boldsymbol{\alpha}_{K}+N_{K})   \tag*{(4.156)}
$$

$$
=\mathrm{Dir}(\boldsymbol{\theta}|\hat{\boldsymbol{\alpha}})   \tag*{(4.157)}
$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_300_157_546_341.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_640_169_914_398.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">0.10,0.10,0.10</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_234_490_506_718.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_642_493_914_717.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">Figure 4.14: (a) The Dirichlet distribution when $K = 3$defines a distribution over the simplex, which can be represented by the triangular surface. Points on this surface satisfy$0 \leq \theta_k \leq 1$and$\sum_{k=1}^3 \theta_k = 1$. Generated by dirichlet_3d_triangle_plot.ipymb. (b) Plot of the Dirichlet density for $\mathbf{\tilde{\alpha}} = (20, 20, 20)$. (c) Plot of the Dirichlet density for $\mathbf{\tilde{\alpha}} = (3, 3, 20)$. (d) Plot of the Dirichlet density for $\mathbf{\tilde{\alpha}} = (0.1, 0.1, 0.1)$. Generated by dirichlet_3d_spiky_plot.ipymb.</div>

where  $\widehat{\alpha}_k = \widetilde{\alpha}_k + N_k$ are the parameters of the posterior. So we see that the posterior can be computed by adding the empirical counts to the prior counts.

The posterior mean is given by

$$
\overline{{\theta}}_{k}=\frac{\widehat{\alpha}_{k}}{\sum_{k^{\prime}=1}^{K}\widehat{\alpha}_{k^{\prime}}}   \tag*{(4.158)}
$$

The posterior mode, which corresponds to the MAP estimate, is given by

$$
\hat{\theta}_{k}=\frac{\hat{\alpha}_{k}-1}{\sum_{k^{\prime}=1}^{K}(\hat{\alpha}_{k^{\prime}}-1)}   \tag*{(4.159)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_182_116_580_344.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_592_117_988_345.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.15: Samples from a 5-dimensional symmetric Dirichlet distribution for different parameter values. (a)  $\mathbf{\check{a}}=(0.1,\ldots,0.1)$. This results in very sparse distributions, with many 0s. (b)  $\mathbf{\check{a}}=(1,\ldots,1)$. This results in more uniform (and dense) distributions. Generated by dirichlet samples plot. ipynb.</div>

If we use  $\breve{\alpha}_{k}=1$, corresponding to a uniform prior, the MAP becomes the MLE:

$$
\hat{\theta}_{k}=N_{k}/N   \tag*{(4.160)}
$$

(See Section 4.2.4 for a more direct derivation of this result.)

##### 4.6.3.4 Posterior predictive

The posterior predictive distribution is given by

$$
\begin{align*}p(y=k|\mathcal{D})&=\int p(y=k|\boldsymbol{\theta})p(\boldsymbol{\theta}|\mathcal{D})d\boldsymbol{\theta}\\&=\int\theta_{k} p(\theta_{k}|\mathcal{D})d\theta_{k}=\mathbb{E}\left[\theta_{k}|\mathcal{D}\right]=\frac{\widehat{\alpha}_{k}}{\sum_{k^{\prime}}\widehat{\alpha}_{k^{\prime}}}\end{align*}   \tag*{(4.162)}
$$

In other words, the posterior predictive distribution is given by

$$
p(y|\mathcal{D})=\mathrm{Cat}(y|\overline{\boldsymbol{\theta}})   \tag*{(4.163)}
$$

where  $\overline{\theta} \triangleq \mathbb{E}[\theta|\mathcal{D}]$ are the posterior mean parameters. If instead we plug-in the MAP estimate, we will suffer from the zero-count problem. The only way to get the same effect as add-one smoothing is to use a MAP estimate with  $\check{\alpha}_c = 2$.

Equation (4.162) gives the probability of a single future event, conditioned on past observations  $\boldsymbol{y} = (y_1, \ldots, y_N)$. In some cases, we want to know the probability of observing a batch of future data, say  $\tilde{\boldsymbol{y}} = (\tilde{y}_1, \ldots, \tilde{y}_M)$. We can compute this as follows:

$$
p(\tilde{\boldsymbol{y}}|\boldsymbol{y})=\frac{p(\tilde{\boldsymbol{y}},\boldsymbol{y})}{p(\boldsymbol{y})}   \tag*{(4.164)}
$$

The denominator is the marginal likelihood of the training data, and the numerator is the marginal likelihood of the training and future test data. We discuss how to compute such marginal likelihoods in Section 4.6.3.5.

---

##### 4.6.3.5 Marginal likelihood

By the same reasoning as in Section 4.6.2.10, one can show that the marginal likelihood for the Dirichlet-categorical model is given by

$$
p(\mathcal{D})=\frac{B(\mathbf{N}+\boldsymbol{\alpha})}{B(\boldsymbol{\alpha})}   \tag*{(4.165)}
$$

where

$$
B(\boldsymbol{\alpha})=\frac{\prod_{k=1}^{K}\Gamma(\alpha_{k})}{\Gamma(\sum_{k}\alpha_{k})}   \tag*{(4.166)}
$$

Hence we can rewrite the above result in the following form, which is what is usually presented in the literature:

$$
p(\mathcal{D})=\frac{\Gamma(\sum_{k}\alpha_{k})}{\Gamma(N+\sum_{k}\alpha_{k})}\prod_{k}\frac{\Gamma(N_{k}+\alpha_{k})}{\Gamma(\alpha_{k})}   \tag*{(4.167)}
$$

#### 4.6.4 The Gaussian-Gaussian model

In this section, we derive the posterior for the parameters of a Gaussian distribution. For simplicity, we assume the variance is known. (The general case is discussed in the sequel to this book, [Mur23], as well as other standard references on Bayesian statistics.)

##### 4.6.4.1 Univariate case

If σ² is a known constant, the likelihood for μ has the form

$$
p(\mathcal{D}|\mu)\propto\exp\left(-\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}(y_{n}-\mu)^{2}\right)   \tag*{(4.168)}
$$

One can show that the conjugate prior is another Gaussian,  $\mathcal{N}(\mu|\tilde{m},\tilde{\tau}^2)$. Applying Bayes' rule for Gaussians, as in Section 4.6.4.1, we find that the corresponding posterior is given by

$$
p(\mu|\mathcal{D},\sigma^{2})=\mathcal{N}(\mu|\hat{m},\hat{\tau}^{2})   \tag*{(4.169)}
$$

$$
\widehat{\tau}^{2}=\frac{1}{\frac{N}{\sigma^{2}}+\frac{1}{\breve{\tau}^{2}}}=\frac{\sigma^{2}\breve{\tau}^{2}}{N\breve{\tau}^{2}+\sigma^{2}}   \tag*{(4.170)}
$$

$$
\widehat{m}=\widehat{\tau}^{2}\left(\frac{\breve{m}}{\breve{\tau}^{2}}+\frac{N\overline{y}}{\sigma^{2}}\right)=\frac{\sigma^{2}}{N\breve{\tau}^{2}+\sigma^{2}}\breve{m}+\frac{N\breve{\tau}^{2}}{N\breve{\tau}^{2}+\sigma^{2}}\overline{y}   \tag*{(4.171)}
$$

where  $\overline{y} \triangleq \frac{1}{N} \sum_{n=1}^{N} y_{n}$ is the empirical mean.

This result is easier to understand if we work in terms of the precision parameters, which are just inverse variances. Specifically, let  $\kappa = 1/\sigma^2$ be the observation precision, and  $\check{\lambda} = 1/\check{\tau}^2$ be the

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_182_114_580_380.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_591_114_987_382.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.16: Inferring the mean of a univariate Gaussian with known  $\sigma^2$ given observation  $y = 3$. (a) Using strong prior,  $p(\mu) = \mathcal{N}(\mu|0,1)$. (b) Using weak prior,  $p(\mu) = \mathcal{N}(\mu|0,5)$. Generated by gauss_infer_1d.ipynb.</div>

precision of the prior. We can then rewrite the posterior as follows:

$$
p(\mu|\mathcal{D},\kappa)=\mathcal{N}(\mu|\widehat{m},\widehat{\lambda}^{-1})   \tag*{(4.172)}
$$

$$
\widehat{\lambda}=\check{\lambda}+N\kappa   \tag*{(4.173)}
$$

$$
\hat{m}=\frac{N\kappa\overline{y}+\breve{\lambda}\breve{m}}{\hat{\lambda}}=\frac{N\kappa}{N\kappa+\breve{\lambda}}\overline{y}+\frac{\breve{\lambda}}{N\kappa+\breve{\lambda}}\breve{m}   \tag*{(4.174)}
$$

These equations are quite intuitive: the posterior precision  $\hat{\lambda}$ is the prior precision  $\hat{\lambda}$ plus  $N$ units of measurement precision  $\kappa$. Also, the posterior mean  $\hat{m}$ is a convex combination of the empirical mean  $\bar{y}$ and the prior mean  $\hat{m}$. This makes it clear that the posterior mean is a compromise between the empirical mean and the prior. If the prior is weak relative to the signal strength ( $\bar{\lambda}$ is small relative to  $\kappa$), we put more weight on the empirical mean. If the prior is strong relative to the signal strength ( $\bar{\lambda}$ is large relative to  $\kappa$), we put more weight on the prior. This is illustrated in Figure 4.16. Note also that the posterior mean is written in terms of  $N\kappa\bar{y}$, so having  $N$ measurements each of precision  $\kappa$ is like having one measurement with value  $\bar{y}$ and precision  $N\kappa$.

##### Posterior after seeing N = 1 examples

To gain further insight into these equations, consider the posterior after seeing a single data point  $y$ (so  $N = 1$). Then the posterior mean can be written in the following equivalent ways:

$$
\hat{m}=\frac{\breve{\lambda}}{\hat{\breve{\lambda}}}\breve{m}+\frac{\kappa}{\hat{\breve{\lambda}}}y   \tag*{(4.175)}
$$

$$
=m+\frac{\kappa}{\widehat{\lambda}}(y-\breve{m})   \tag*{(4.176)}
$$

$$
=y-\frac{\breve{\lambda}}{\breve{\lambda}}(y-\breve{m})   \tag*{(4.177)}
$$

The first equation is a convex combination of the prior mean and the data. The second equation is the prior mean adjusted towards the data y. The third equation is the data adjusted towards

---

the prior mean; this is called a shrinkage estimate. This is easier to see if we define the weight  $w = \tilde{\lambda}/\hat{\lambda}$, which is the ratio of the prior to posterior precision. Then we have

$$
\hat{m}=y-w(y-\breve{m})=(1-w)y+w\breve{m}   \tag*{(4.178)}
$$

Note that, for a Gaussian, the posterior mean and posterior mode are the same. Thus we can use the above equations to perform MAP estimation. See Exercise 4.2 for a simple example.

##### Posterior variance

In addition to the posterior mean or mode of  $\mu$, we might be interested in the posterior variance, which gives us a measure of confidence in our estimate. The square root of this is called the standard error of the mean:

$$
\mathrm{s e}(\mu)\triangleq\sqrt{\mathbb{V}\left[\mu|\mathcal{D}\right]}   \tag*{(4.179)}
$$

Suppose we use an uninformative prior for  $\mu$ by setting  $\bar{\lambda}=0$ (see Section 4.6.5.1). In this case, the posterior mean is equal to the MLE,  $\hat{m}=\bar{y}$. Suppose, in addition, that we approximate  $\sigma^2$ by the sample variance

$$
s^{2}\triangleq\frac{1}{N}\sum_{n=1}^{N}(y_{n}-\overline{y})^{2}   \tag*{(4.180)}
$$

Hence  $\widehat{\lambda}=N\widehat{\kappa}=N/s^{2}$, so the SEM becomes

$$
\mathrm{se}(\mu)=\sqrt{\mathbb{V}\left[\mu|\mathcal{D}\right]}=\frac{1}{\sqrt{\lambda}}=\frac{s}{\sqrt{N}}   \tag*{(4.181)}
$$

Thus we see that the uncertainty in  $\mu$ is reduced at a rate of  $1/\sqrt{N}$.

In addition, we can use the fact that 95% of a Gaussian distribution is contained within 2 standard deviations of the mean to approximate the 95% credible interval for  $\mu$ using

$$
I_{.95}(\mu|\mathcal{D})=\overline{y}\pm2\frac{s}{\sqrt{N}}   \tag*{(4.182)}
$$

##### 4.6.4.2 Multivariate case

For $D$-dimensional data, the likelihood has the following form (where we drop terms that are independent of $\mu$):

$$
p(\mathcal{D}|\boldsymbol{\mu})=\prod_{n=1}^{N}\mathcal{N}(y_{n}|\boldsymbol{\mu},\boldsymbol{\Sigma})   \tag*{(4.183)}
$$

$$
=\left(\frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{\frac{1}{2}}}\right)^{N}\exp\left[-\frac{1}{2}\sum_{n=1}^{N}(\boldsymbol{y}_{n}-\boldsymbol{\mu})^{\mathsf{T}}\boldsymbol{\Sigma}^{-1}(\boldsymbol{y}_{n}-\boldsymbol{\mu})\right]   \tag*{(4.184)}
$$

$$
\propto\mathcal{N}(\overline{{y}}|\mu,\frac{1}{N}\Sigma)   \tag*{(4.185)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_208_125_956_375.jpg" alt="Image" width="64%" /></div>

<div style="text-align: center;">Figure 4.17: Illustration of Bayesian inference for the mean of a 2d Gaussian. (a) The data is generated from  $\mathbf{y}_n \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$, where  $\boldsymbol{\mu} = [0.5, 0.5]^\top$ and  $\boldsymbol{\Sigma} = 0.1[2, 1; 1, 1]$. (b) The prior is  $p(\boldsymbol{\mu}) = \mathcal{N}(\boldsymbol{\mu}|\mathbf{0}, 0.1\mathbf{I}_2)$. (c) We show the posterior after 10 data points have been observed. Generated by gauss_infer_2d.ipynb.</div>

where  $\overline{y} = \frac{1}{N} \sum_{n=1}^{N} y_n$. (The proof of the last equation is given right after Equation (3.65).) Thus we replace the set of observations with their mean, and scale down the covariance by a factor of  $N$.

For simplicity, we will use a conjugate prior, which in this case is a Gaussian, namely

$$
p(\boldsymbol{\mu})=\mathcal{N}(\boldsymbol{\mu}|\breve{m},\breve{\mathbf{V}})   \tag*{(4.186)}
$$

We can derive a Gaussian posterior for  $\mu$ based on the results in Section 3.3.1. We get

$$
p(\boldsymbol{\mu}|\mathcal{D},\boldsymbol{\Sigma})=\mathcal{N}(\boldsymbol{\mu}|\boldsymbol{\hat{m}},\hat{\mathbf{V}})   \tag*{(4.187)}
$$

$$
\hat{\mathbf{V}}^{-1}=\check{\mathbf{V}}^{-1}+N\mathbf{\Sigma}^{-1}   \tag*{(4.188)}
$$

$$
\hat{m}=\hat{\mathbf{V}}\left(\mathbf{\Sigma}^{-1}(N\overline{y})+\check{\mathbf{V}}^{-1}\check{m}\right)   \tag*{(4.189)}
$$

Figure 4.17 gives a 2d example of these results.

#### 4.6.5 Beyond conjugate priors

We have seen various examples of conjugate priors, all of which have come from the exponential family (see Section 3.4). These priors have the advantage of being easy to interpret (in terms of sufficient statistics from a virtual prior dataset), and easy to compute with. However, for most models, there is no prior in the exponential family that is conjugate to the likelihood. Furthermore, even where there is a conjugate prior, the assumption of conjugacy may be too limiting. Therefore in the sections below, we briefly discuss various other kinds of priors.

##### 4.6.5.1 Noninformative priors

When we have little or no domain specific knowledge, it is desirable to use an uninformative, noninformative or objective priors, to “let the data speak for itself”. For example, if we want to infer a real valued quantity, such as a location parameter  $\mu \in \mathbb{R}$, we can use a flat prior  $p(\mu) \propto 1$. This can be viewed as an “infinitely wide” Gaussian.

---

Unfortunately, there is no unique way to define uninformative priors, and they all encode some kind of knowledge. It is therefore better to use the term diffuse prior, minimally informative prior or default prior. See the sequel to this book, [Mur23], for more details.

##### 4.6.5.2 Hierarchical priors

Bayesian models require specifying a prior  $p(\boldsymbol{\theta})$ for the parameters. The parameters of the prior are called hyperparameters, and will be denoted by  $\boldsymbol{\xi}$. If these are unknown, we can put a prior on them; this defines a hierarchical Bayesian model, or multi-level model, which can visualize like this:  $\boldsymbol{\xi} \to \boldsymbol{\theta} \to \mathcal{D}$. We assume the prior on the hyper-parameters is fixed (e.g., we may use some kind of minimally informative prior), so the joint distribution has the form

$$
p(\boldsymbol{\xi},\boldsymbol{\theta},\mathcal{D})=p(\boldsymbol{\xi})p(\boldsymbol{\theta}|\boldsymbol{\xi})p(\mathcal{D}|\boldsymbol{\theta})   \tag*{(4.190)}
$$

The hope is that we can learn the hyperparameters by treating the parameters themselves as datapoints. This is useful when we have multiple related parameters that need to be estimated (e.g., from different subpopulations, or multiple tasks); this provides a learning signal to the top level of the model. See the sequel to this book, [Mur23], for details.

##### 4.6.5.3 Empirical priors

In Section 4.6.5.2, we discussed hierarchical Bayes as a way to infer parameters from data. Unfortunately, posterior inference in such models can be computationally challenging. In this section, we discuss a computationally convenient approximation, in which we first compute a point estimate of the hyperparameters,  $\xi$, and then compute the conditional posterior,  $p(\boldsymbol{\theta}|\boldsymbol{\xi},\mathcal{D})$, rather than the joint posterior,  $p(\boldsymbol{\theta},\boldsymbol{\xi}|\mathcal{D})$.

To estimate the hyper-parameters, we can maximize the marginal likelihood:

$$
\hat{\xi}_{\mathrm{m m l}}(\mathcal{D})=\underset{\boldsymbol{\xi}}{\operatorname{a r g m a x}}p(\mathcal{D}|\boldsymbol{\xi})=\underset{\boldsymbol{\xi}}{\operatorname{a r g m a x}}\int p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta}|\boldsymbol{\xi})d\boldsymbol{\theta}   \tag*{(4.191)}
$$

This technique is known as type II maximum likelihood, since we are optimizing the hyperparameters, rather than the parameters. Once we have estimated  $\hat{\xi}$, we compute the posterior  $p(\boldsymbol{\theta}|\boldsymbol{\hat{\xi}},\mathcal{D})$ in the usual way.

Since we are estimating the prior parameters from data, this approach is empirical Bayes (EB) [CL96]. This violates the principle that the prior should be chosen independently of the data. However, we can view it as a computationally cheap approximation to inference in the full hierarchical Bayesian model, just as we viewed MAP estimation as an approximation to inference in the one level model  $\theta \to \mathcal{D}$. In fact, we can construct a hierarchy in which the more integrals one performs, the “more Bayesian” one becomes, as shown below.

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Method</td><td style='text-align: center; word-wrap: break-word;'>Definition</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Maximum likelihood</td><td style='text-align: center; word-wrap: break-word;'>$\hat{\theta} = \arg\max_{\theta} p(\mathcal{D}|\boldsymbol{\theta})$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MAP estimation</td><td style='text-align: center; word-wrap: break-word;'>$\hat{\boldsymbol{\theta}}(\boldsymbol{\xi}) = \arg\max_{\boldsymbol{\theta}} p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta}|\boldsymbol{\xi})$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>ML-II (Empirical Bayes)</td><td style='text-align: center; word-wrap: break-word;'>$\hat{\boldsymbol{\xi}} = \arg\max_{\boldsymbol{\xi}} \int p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta}|\boldsymbol{\xi})d\boldsymbol{\theta}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>MAP-II</td><td style='text-align: center; word-wrap: break-word;'>$\hat{\boldsymbol{\xi}} = \arg\max_{\boldsymbol{\xi}} \int p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta}|\boldsymbol{\xi})p(\boldsymbol{\xi})d\boldsymbol{\theta}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Full Bayes</td><td style='text-align: center; word-wrap: break-word;'>$p(\boldsymbol{\theta}, \boldsymbol{\xi}|\mathcal{D}) \propto p(\mathcal{D}|\boldsymbol{\theta})p(\boldsymbol{\theta}|\boldsymbol{\xi})p(\boldsymbol{\xi})$</td></tr></table>

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_242_120_516_343.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_648_120_925_346.jpg" alt="Image" width="24%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.18: (a) Central interval and (b) HPD region for a Beta(3,9) posterior. The CI is (0.06, 0.52) and the HPD is (0.04, 0.48). Adapted from Figure 3.6 of [Hof09]. Generated by betaHPD.ipynb.</div>

Note that ML-II is less likely to overfit than “regular” maximum likelihood, because there are typically fewer hyper-parameters  $\xi$ than there are parameters  $\theta$. See the sequel to this book, [Mur23], for details.

#### 4.6.6 Credible intervals

A posterior distribution is (usually) a high dimensional object that is hard to visualize and work with. A common way to summarize such a distribution is to compute a point estimate, such as the posterior mean or mode, and then to compute a credible interval, which quantifies the uncertainty associated with that estimate. (A credible interval is not the same as a confidence interval, which is a concept from frequentist statistics which we discuss in Section 4.7.4.)

More precisely, we define a  $100(1-\alpha)\%$ credible interval to be a (contiguous) region  $C=(\ell,u)$ (standing for lower and upper) which contains  $1-\alpha$ of the posterior probability mass, i.e.,

$$
C_{\alpha}(\mathcal{D})=(\ell,u):P(\ell\leq\theta\leq u|\mathcal{D})=1-\alpha   \tag*{(4.192)}
$$

There may be many intervals that satisfy Equation (4.192), so we usually choose one such that there is  $(1-\alpha)/2$ mass in each tail; this is called a \textit{central interval}. If the posterior has a known functional form, we can compute the posterior central interval using  $\ell = F^{-1}(\alpha/2)$ and  $u = F^{-1}(1-\alpha/2)$, where  $F$ is the cdf of the posterior, and  $F^{-1}$ is the inverse cdf. For example, if the posterior is Gaussian,  $p(\theta|\mathcal{D}) = \mathcal{N}(0,1)$, and  $\alpha = 0.05$, then we have  $\ell = \Phi^{-1}(\alpha/2) = -1.96$, and  $u = \Phi^{-1}(1-\alpha/2) = 1.96$, where  $\Phi$ denotes the cdf of the Gaussian. This is illustrated in Figure 2.2b. This justifies the common practice of quoting a credible interval in the form of  $\mu \pm 2\sigma$, where  $\mu$ represents the posterior mean,  $\sigma$ represents the posterior standard deviation, and  $2$ is a good approximation to 1.96.

In general, it is often hard to compute the inverse cdf of the posterior. In this case, a simple alternative is to draw samples from the posterior, and then to use a Monte Carlo approximation to the posterior quantiles: we simply sort the $S$samples, and find the one that occurs at location$\alpha/S$along the sorted list. As$S \to \infty$, this converges to the true quantile. See beta_credible_int_demo.ipynb for a demo of this.

A problem with central intervals is that there might be points outside the central interval which have higher probability than points that are inside, as illustrated in Figure 4.18(a). This motivates

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_253_139_502_328.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_652_140_909_330.jpg" alt="Image" width="22%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.19: (a) Central interval and (b) HPD region for a hypothetical multimodal posterior. Adapted from Figure 2.2 of [Gel+04]. Generated by postDensityIntervals.ipynb.</div>

an alternative quantity known as the highest posterior density or HPD region, which is the set of points which have a probability above some threshold. More precisely we find the threshold  $p^{*}$ on the pdf such that

$$
1-\alpha=\int_{\theta:p(\theta|\mathcal{D})>p^{*}}p(\theta|\mathcal{D})d\theta   \tag*{(4.193)}
$$

and then define the HPD as

$$
C_{\alpha}(\mathcal{D})=\{\theta:p(\theta|\mathcal{D})\geq p^{*}\}   \tag*{(4.194)}
$$

In 1d, the HPD region is sometimes called a highest density interval or HDI. For example, Figure 4.18(b) shows the 95% HDI of a Beta(3,9) distribution, which is (0.04, 0.48). We see that this is narrower than the central interval, even though it still contains 95% of the mass; furthermore, every point inside of it has higher density than every point outside of it.

For a unimodal distribution, the HDI will be the narrowest interval around the mode containing 95% of the mass. To see this, imagine “water filling” in reverse, where we lower the level until 95% of the mass is revealed, and only 5% is submerged. This gives a simple algorithm for computing HDIs in the 1d case: simply search over points such that the interval contains 95% of the mass and has minimal width. This can be done by 1d numerical optimization if we know the inverse CDF of the distribution, or by search over the sorted data points if we have a bag of samples (see betaHPD.ipynb for some code).

If the posterior is multimodal, the HDI may not even be a connected region: see Figure 4.19(b) for an example. However, summarizing multimodal posteriors is always difficult.

#### 4.6.7 Bayesian machine learning

So far, we have focused on unconditional models of the form  $p(\boldsymbol{y}|\boldsymbol{\theta})$. In supervised machine learning, we use conditional models of the form  $p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})$. The posterior over the parameters is now  $p(\boldsymbol{\theta}|\mathcal{D})$, where  $\mathcal{D}=\{(\boldsymbol{x}_{n},\boldsymbol{y}_{n}):n=1:N\}$. Computing this posterior can be done using the principles we have already discussed. This approach is called Bayesian machine learning, since we are “being Bayesian” about the model parameters.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

##### 4.6.7.1 Plugin approximation

Once we have computed the posterior over the parameters, we can compute the posterior predictive distribution over outputs given inputs by marginalizing out the unknown parameters:

$$
p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})=\int p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})p(\boldsymbol{\theta}|\mathcal{D})d\boldsymbol{\theta}   \tag*{(4.195)}
$$

Of course, computing this integral is often intractable. A very simple approximation is to assume there is just a single best model,  $\pmb{\theta}$, such as the MLE. This is equivalent to approximating the posterior as an infinitely narrow, but infinitely tall, “spike” at the chosen value. We can write this as follows:

$$
p(\boldsymbol{\theta}|\mathcal{D})=\delta(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})   \tag*{(4.196)}
$$

where  $\delta$ is the Dirac delta function (see Section 2.6.5). If we use this approximation, then the predictive distribution can be obtained by simply “plugging in” the point estimate into the likelihood:

$$
p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})=\int p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})p(\boldsymbol{\theta}|\mathcal{D})d\boldsymbol{\theta}\approx\int p(\boldsymbol{y}|\boldsymbol{x},\boldsymbol{\theta})\delta(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})d\boldsymbol{\theta}=p(\boldsymbol{y}|\boldsymbol{x},\hat{\boldsymbol{\theta}})   \tag*{(4.197)}
$$

This follows from the sifting property of delta functions (Equation (2.129)).

The approach in Equation (4.197) is called a plug-in approximation. This approach is equivalent to the standard approach used in most of machine learning, in which we first fit the model (i.e. compute a point estimate  $\hat{\theta}$) and then use it to make predictions. However, the standard (plug-in) approach can suffer from overfitting and overconfidence, as we discussed in Section 1.2.3. The fully Bayesian approach avoids this by marginalizing out the parameters, but can be expensive. Fortunately, even simple approximations, in which we average over a few plausible parameter values, can improve performance. We give some examples of this below.

##### 4.6.7.2 Example: scalar input, binary output

Suppose we want to perform binary classification, so  $y \in \{0,1\}$. We will use a model of the form

$$
p(y|\boldsymbol{x};\boldsymbol{\theta})=\mathrm{Ber}(y|\sigma(\boldsymbol{w}^{\top}\boldsymbol{x}+b))   \tag*{(4.198)}
$$

where

$$
\sigma(a)\triangleq\frac{e^{a}}{1+e^{a}}   \tag*{(4.199)}
$$

is the sigmoid or logistic function which maps  $\mathbb{R} \to [0,1]$, and  $\mathrm{Ber}(y|\mu)$ is the Bernoulli distribution with mean  $\mu$ (see Section 2.4 for details). In other words,

$$
p(y=1|\boldsymbol{x};\boldsymbol{\theta})=\sigma(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}+b)=\frac{1}{1+e^{-(\boldsymbol{w}^{\mathsf{T}}\boldsymbol{x}+b)}}   \tag*{(4.200)}
$$

This model is called logistic regression. (We discuss this in more detail in Chapter 10.)

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_193_149_578_401.jpg" alt="Image" width="33%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_599_151_995_409.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.20: (a) Logistic regression for classifying if an Iris flower is Versicolor (y = 1) or setosa (y = 0) using a single input feature x corresponding to sepal length. Labeled points have been (vertically) jittered to avoid overlapping too much. Vertical line is the decision boundary. Generated by  $\text{logreg\_iris\_1d.ipynb}$. (b) Same as (a) but showing posterior distribution. Adapted from Figure 4.4 of [Mar18]. Generated by  $\text{logreg\_iris\_bayes\_1d\_pymc3.ipynb}$.</div>

Let us apply this model to the task of determining if an iris flower is of type Setosa or Versicolor,  $y_n \in \{0,1\}$, given information about the sepal length,  $x_n$. (See Section 1.2.1.1 for a description of the iris dataset.)

We first fit a 1d logistic regression model of the following form

$$
p(y=1|x;\boldsymbol{\theta})=\sigma(b+wx)   \tag*{(4.201)}
$$

to the dataset  $\mathcal{D} = \{(x_n, y_n)\}$ using maximum likelihood estimation. (See Section 10.2.3 for details on how to compute the MLE for this model.) Figure 4.20a shows the plugin approximation to the posterior predictive,  $p(y = 1 | x, \hat{\theta})$, where  $\hat{\theta}$ is the MLE of the parameters. We see that we become more confident that the flower is of type Versicolor as the sepal length gets larger, as represented by the sigmoidal (S-shaped) logistic function.

The decision boundary is defined to be the input value  $x^*$ where  $p(y = 1|x^*; \hat{\theta}) = 0.5$. We can solve for this value as follows:

$$
\sigma(b+wx^{*})=\frac{1}{1+e^{-(b+wx^{*})}}=\frac{1}{2}   \tag*{(4.202)}
$$

$$
b+wx^{*}=0   \tag*{(4.203)}
$$

$$
x^{*}=-\frac{b}{w}   \tag*{(4.204)}
$$

From Figure 4.20a, we see that  $x^* \approx 5.5 \, cm$.

However, the above approach does not model the uncertainty in our estimate of the parameters, and therefore ignores the induced uncertainty in the output probabilities, and the location of the decision boundary. To capture this additional uncertainty, we can use a Bayesian approach to approximate

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_315_117_858_328.jpg" alt="Image" width="47%" /></div>

<div style="text-align: center;">Figure 4.21: Distribution of arrival times for two different shipping companies. ETA is the expected time of arrival. A's distribution has greater uncertainty, and may be too risky. From https://bit.ly/39bc4XL. Used with kind permission of Brendan Hasz.</div>

the posterior $p(\boldsymbol{\theta}|\mathcal{D})$. (See Section 10.5 for details.) Given this, we can approximate the posterior predictive distribution using a Monte Carlo approximation:

$$
p(y=1|x,\mathcal{D})\approx\frac{1}{S}\sum_{s=1}^{S}p(y=1|x,\boldsymbol{\theta}^{s})   \tag*{(4.205)}
$$

where  $\boldsymbol{\theta}^{s} \sim p(\boldsymbol{\theta}|\mathcal{D})$ is a posterior sample. Figure 4.20b plots the mean and 95% credible interval of this function. We see that there is now a range of predicted probabilities for each input. We can also compute a distribution over the location of the decision boundary by using the Monte Carlo approximation

$$
p(x^{*}|\mathcal{D})\approx\frac{1}{S}\sum_{s=1}^{S}\delta\left(x^{*}-(-\frac{b^{s}}{w^{s}})\right)   \tag*{(4.206)}
$$

where  $(b^{s}, w^{s}) = \theta^{s}$. The 95% credible interval for this distribution is shown by the “fat” vertical line in Figure 4.20b.

Although carefully modeling our uncertainty may not matter for this application, it can be important in risk-sensitive applications, such as health care and finance, as we discuss in Chapter 5.

##### 4.6.7.3 Example: binary input, scalar output

Now suppose we want to predict the delivery time for a package,  $y \in \mathbb{R}$, if shipped by company A vs B. We can encode the company id using a binary feature  $x \in \{0,1\}$, where  $x = 0$ means company A and  $x = 1$ means company B. We will use the following discriminative model for this problem:

$$
p(y|x,\boldsymbol{\theta})=\mathcal{N}(y|\mu_{x},\sigma_{x}^{2})   \tag*{(4.207)}
$$

where  $\mathcal{N}(y|\mu,\sigma^{2})$ is the Gaussian distribution

$$
\mathcal{N}(y|\mu,\sigma^{2})\triangleq\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{1}{2\sigma^{2}}(y-\mu)^{2}}   \tag*{(4.208)}
$$

“Probabilistic Machine Learning: An Introduction”. Online version. November 23, 2024

---

and  $\boldsymbol{\theta} = (\mu_0, \mu_1, \sigma_0, \sigma_1)$ are the parameters of the model. We can fit this model using maximum likelihood estimation as we discuss in Section 4.2.5; alternatively, we can adopt a Bayesian approach, as we discuss in Section 4.6.4.

The advantage of the Bayesian approach is that by capturing uncertainty in the parameters  $\theta$, we also capture uncertainty in our forecasts  $p(y|x,\mathcal{D})$, whereas using a plug-in approximation  $p(y|x,\hat{\theta})$ would underestimate this uncertainty. For example, suppose we have only used each company once, so our training set has the form  $\mathcal{D}=\{(x_1=0,y_1=15),(x_2=1,y_2=20)\}$. As we show in Section 4.2.5, the MLE for the means will be the empirical means,  $\hat{\mu}_0=15$ and  $\hat{\mu}_1=20$, but the MLE for the standard deviations will be zero,  $\hat{\sigma}_0=\hat{\sigma}_1=0$, since we only have a single sample from each “class”. The resulting plug-in prediction will therefore not capture any uncertainty.

To see why modeling the uncertainty is important, consider Figure 4.21. We see that the expected time of arrival (ETA) for company A is less than for company B; however, the variance of A's distribution is larger, which makes it a risky choice if you want to be confident the package will arrive by the specified deadline. (For more details on how to choose optimal actions in the presence of uncertainty, see Chapter 5.)

Of course, the above example is extreme, because we assumed we only had one example from each delivery company. However, this kind of problem occurs whenever we have few examples of a given kind of input, as can happen whenever the data has a long tail of novel patterns, such as a new combination of words or categorical features.

##### 4.6.7.4 Scaling up

The above examples were both extremely simple, involving 1d input and 1d output, and just 2-4 parameters. Most practical problems involve high dimensional inputs, and sometimes high dimensional outputs, and therefore use models with lots of parameters. Unfortunately, computing the posterior,  $p(\boldsymbol{\theta}|\mathcal{D})$, and the posterior predictive,  $p(\boldsymbol{y}|\boldsymbol{x},\mathcal{D})$, can be computationally challenging in such cases. We discuss this issue in Section 4.6.8.

#### 4.6.8 Computational issues

Given a likelihood  $p(\mathcal{D}|\boldsymbol{\theta})$ and a prior  $p(\boldsymbol{\theta})$, we can compute the posterior  $p(\boldsymbol{\theta}|\mathcal{D})$ using Bayes' rule. However, actually performing this computation is usually intractable, except for simple special cases, such as conjugate models (Section 4.6.1), or models where all the latent variables come from a small finite set of possible values. We therefore need to approximate the posterior. There are a large variety of methods for performing approximate posterior inference, which trade off accuracy, simplicity, and speed. We briefly discuss some of these algorithms below, but go into more detail in the sequel to this book, [Mur23]. (See also [MFR20] for a review of various approximate inference methods, starting with Bayes' original method in 1763.)

As a running example, we will use the problem of approximating the posterior of a beta-Bernoulli model. Specifically, the goal is to approximate

$$
p(\theta|\mathcal{D})\propto\left[\prod_{n=1}^{N}\mathrm{Bin}(y_{n}|\theta)\right]\mathrm{Beta}(\theta|1,1)   \tag*{(4.209)}
$$

where D consists of 10 heads and 1 tail (so the total number of observations is N = 11), and we use a uniform prior. Although we can compute this posterior exactly (see Figure 4.22), using the

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_183_117_575_337.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_591_117_984_339.jpg" alt="Image" width="34%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.22: Approximating the posterior of a beta-Bernoulli model. (a) Grid approximation using 20 grid points. (b) Laplace approximation. Generated by laplace_approx_beta_binom_jax.ipynb.</div>

method discussed in Section 4.b.2, this serves as a useful pedagogical example since we can compare the approximation to the exact answer. Also, since the target distribution is just 1d, it is easy to visualize the results. (Note, however, that the problem is not completely trivial, since the posterior is highly skewed, due to the use of an imbalanced sample of 10 heads and 1 tail.)

##### 4.6.8.1 Grid approximation

The simplest approach to approximate posterior inference is to partition the space of possible values for the unknowns into a finite set of possibilities, call them  $\theta_1, \ldots, \theta_K$, and then to approximate the posterior by brute-force enumeration, as follows:

$$
p(\boldsymbol{\theta}=\boldsymbol{\theta}_{k}|\mathcal{D})\approx\frac{p(\mathcal{D}|\boldsymbol{\theta}_{k})p(\boldsymbol{\theta}_{k})}{p(\mathcal{D})}=\frac{p(\mathcal{D}|\boldsymbol{\theta}_{k})p(\boldsymbol{\theta}_{k})}{\sum_{k^{\prime}=1}^{K}p(\mathcal{D},\boldsymbol{\theta}_{k^{\prime}})}   \tag*{(4.210)}
$$

This is called a grid approximation. In Figure 4.22a, we illustrate this method applied to our 1d problem. We see that it is easily able to capture the skewed posterior. Unfortunately, this approach does not scale to problems in more than 2 or 3 dimensions, because the number of grid points grows exponentially with the number of dimensions.

##### 4.6.8.2 Quadratic (Laplace) approximation

In this section, we discuss a simple way to approximate the posterior using a multivariate Gaussian; this is known as a Laplace approximation or a quadratic approximation (see e.g., [TK86; RMC09]).

To

$$
p(\boldsymbol{\theta}|\mathcal{D})=\frac{1}{Z}e^{-\mathcal{E}(\boldsymbol{\theta})}   \tag*{(4.211)}
$$

where  $\mathcal{E}(\boldsymbol{\theta}) = -\log p(\boldsymbol{\theta}, \mathcal{D})$ is called an energy function, and  $Z = p(\mathcal{D})$ is the normalization constant. Performing a Taylor series expansion around the mode  $\hat{\boldsymbol{\theta}}$ (i.e., the lowest energy state) we get

$$
\mathcal{E}(\boldsymbol{\theta})\approx\mathcal{E}(\hat{\boldsymbol{\theta}})+(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})^{\top}\boldsymbol{g}+\frac{1}{2}(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})^{\top}\mathbf{H}(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})   \tag*{(4.212)}
$$


---

where g is the gradient at the mode, and H is the Hessian. Since  $\theta$ is the mode, the gradient term is zero. Hence

$$
\hat{p}(\boldsymbol{\theta},\mathcal{D})=e^{-\mathcal{E}(\hat{\boldsymbol{\theta}})}\exp\left[-\frac{1}{2}(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})^{\top}\mathbf{H}(\boldsymbol{\theta}-\hat{\boldsymbol{\theta}})\right]   \tag*{(4.213)}
$$

$$
\hat{p}(\boldsymbol{\theta}|\mathcal{D})=\frac{1}{Z}\hat{p}(\boldsymbol{\theta},\mathcal{D})=\mathcal{N}(\boldsymbol{\theta}|\hat{\boldsymbol{\theta}},\mathbf{H}^{-1})   \tag*{(4.214)}
$$

$$
Z=e^{-\mathcal{E}(\hat{\boldsymbol{\theta}})}\big(2\pi\big)^{D/2}|\mathbf{H}|^{-\frac{1}{2}}   \tag*{(4.215)}
$$

The last line follows from normalization constant of the multivariate Gaussian.

The Laplace approximation is easy to apply, since we can leverage existing optimization algorithms to compute the MAP estimate, and then we just have to compute the Hessian at the mode. (In high dimensional spaces, we can use a diagonal approximation.)

In Figure 4.22b, we illustrate this method applied to our 1d problem. Unfortunately we see that it is not a particularly good approximation. This is because the posterior is skewed, whereas a Gaussian is symmetric. In addition, the parameter of interest lies in the constrained interval  $\theta \in [0, 1]$, whereas the Gaussian assumes an unconstrained space,  $\boldsymbol{\theta} \in \mathbb{R}$. Fortunately, we can solve this latter problem by using a change of variable. For example, in this case we can apply the Laplace approximation to  $\alpha = \log(\theta)$. This is a common trick to simplify the job of inference.

##### 4.6.8.3 Variational approximation

In Section 4.6.8.2, we discussed the Laplace approximation, which uses an optimization procedure to find the MAP estimate, and then approximates the curvature of the posterior at that point based on the Hessian. In this section, we discuss variational inference (VI), which is another optimization-based approach to posterior inference, but which has much more modeling flexibility (and thus can give a much more accurate approximation).

VI attempts to approximate an intractable probability distribution, such as  $p(\boldsymbol{\theta}|\mathcal{D})$, with one that is tractable,  $q(\boldsymbol{\theta})$, so as to minimize some discrepancy  $D$ between the distributions:

$$
q^{*}=\underset{q\in\mathcal{Q}}{\operatorname{argmin}}D(q,p)   \tag*{(4.216)}
$$

where Q is some tractable family of distributions (e.g., multivariate Gaussian). If we define D to be the KL divergence (see Section 6.2), then we can derive a lower bound to the log marginal likelihood; this quantity is known as the evidence lower bound or ELBO. By maximizing the ELBO, we can improve the quality of the posterior approximation. See the sequel to this book, [Mur23], for details.

##### 4.6.8.4 Markov Chain Monte Carlo (MCMC) approximation

Although VI is a fast, optimization-based method, it can give a biased approximation to the posterior, since it is restricted to a specific function form  $q \in \mathcal{Q}$. A more flexible approach is to use a non-parametric approximation in terms of a set of samples,  $q(\boldsymbol{\theta}) \approx \frac{1}{S} \sum_{s=1}^{S} \delta(\boldsymbol{\theta} - \boldsymbol{\theta}^s)$. This is called a Monte Carlo approximation to the posterior. The key issue is how to create the posterior samples  $\boldsymbol{\theta}^s \sim p(\boldsymbol{\theta} | \mathcal{D})$ efficiently, without having to evaluate the normalization constant  $p(\mathcal{D}) = \int p(\boldsymbol{\theta}, \mathcal{D}) \, d\boldsymbol{\theta}$. A common approach to this problem is known as Markov chain Monte Carlo or MCMC. If we augment this algorithm with gradient-based information, derived from  $\nabla \log p(\boldsymbol{\theta}, \mathcal{D})$, we can

---

significantly speed up the method; this is called Hamiltonian Monte Carlo or HMC. See the sequel to this book, [Mur23], for details.

### 4.7 Frequentist statistics *

The approach to statistical inference that we described in Section 4.6 is called Bayesian statistics. It treats parameters of models just like any other unknown random variable, and applies the rules of probability theory to infer them from data. Attempts have been made to devise approaches to statistical inference that avoid treating parameters like random variables, and which thus avoid the use of priors and Bayes rule. This alternative approach is known as frequentist statistics, classical statistics or orthodox statistics.

The basic idea (formalized in Section 4.7.1) is to represent uncertainty by calculating how a quantity estimated from data (such as a parameter or a predicted label) would change if the data were changed. It is this notion of variation across repeated trials that forms the basis for modeling uncertainty used by the frequentist approach. By contrast, the Bayesian approach views probability in terms of information rather than repeated trials. This allows the Bayesian to compute the probability of one-off events, as we discussed in Section 2.1.1. Perhaps more importantly, the Bayesian approach avoids certain paradoxes that plague the frequentist approach (see Section 4.7.5 and Section 5.5.4). These pathologies led the famous statistician George Box to say:

I believe that it would be very difficult to persuade an intelligent person that current [frequentist] statistical practice was sensible, but that there would be much less difficulty with an approach via likelihood and Bayes' theorem. — George Box, 1962 (quoted in [Jay76]).

Nevertheless, it is useful to be familiar with frequentist statistics, since it is widely used, and has some key concepts that are useful even for Bayesians [Rub84].

#### 4.7.1 Sampling distributions

In frequentist statistics, uncertainty is not represented by the posterior distribution of a random variable, but instead by the sampling distribution of an estimator.

The term “estimator” is defined in the section on decision theory in Section 5.1, but in brief, an estimator  $\delta: \mathcal{D} \to \mathcal{A}$ is a decision procedure that specifies what action to take given some observed data. The action could be to predict a class label, or the next observation, or to predict the unknown parameters. In the latter case, the estimator is often denoted by  $\hat{\theta}$, but this notation is ambiguous, since it looks like it represents a parameter vector rather than a function. So instead we will use the notation  $\hat{\Theta}$. This function could compute the MLE, or the method of moments estimate, etc. The output of this function, when applied to a specific dataset of size  $N$, is denote  $\hat{\boldsymbol{\theta}} = \hat{\boldsymbol{\Theta}}(\mathcal{D})$, where  $\mathcal{D} = \{\boldsymbol{x}_1, \ldots, \boldsymbol{x}_N\}$.

The key idea in frequentist statistics is to view the data  $\mathcal{D}$ as a random variable, and the parameters from which the data are drawn,  $\boldsymbol{\theta}^*$, as a fixed but unknown constant. Thus  $\hat{\boldsymbol{\theta}} = \hat{\boldsymbol{\Theta}}(\mathcal{D})$ is a random variable, and its distribution is known as the sampling distribution of the estimator. To understand what thus means, suppose we create  $S$ different datasets, each of the form

$$
\mathcal{D}^{(s)}=\{\boldsymbol{x}_{n}\sim p(\boldsymbol{x}_{n}|\boldsymbol{\theta}^{*}):n=1:N\}   \tag*{(4.217)}
$$


---

We denote this by  $\mathcal{D}^{(s)} \sim \theta^*$ for brevity. Now we apply the estimator to each  $\mathcal{D}^{(s)}$ to get a set of estimates,  $\{\hat{\theta}(\mathcal{D}^{(s)})\}$. As we let  $S \to \infty$, the distribution induced by this set is the sampling distribution of the estimator. More precisely, we have

$$
\mathrm{S a m p l i n g D i s t}(\hat{\Theta},\boldsymbol{\theta}^{*})=\mathrm{P u s h T h r o u g h}(p(\tilde{\mathcal{D}}|\boldsymbol{\theta}^{*}),\hat{\Theta})   \tag*{(4.218)}
$$

where we push the data distribution through the estimator function to induce a distribution of estimates. In some cases, we can compute the sampling distribution analytically, as we discuss in Section 4.7.2, although typically we need to approximate it by Monte Carlo, as we discuss in Section 4.7.3.

#### 4.7.2 Gaussian approximation of the sampling distribution of the MLE

The most common estimator is the MLE. When the sample size becomes large, the sampling distribution of the MLE for certain models becomes Gaussian. This is known as the asymptotic normality of the sampling distribution. More formally, we have the following result:

Theorem 4.7.1. If the parameters are identifiable, then

$$
\mathrm{SamplingDist}(\hat{\boldsymbol{\Theta}}^{\mathrm{m l e}},\boldsymbol{\theta}^{*})\rightarrow\mathcal{N}(\cdot|\boldsymbol{\theta}^{*},(\boldsymbol{N}\mathbf{F}(\boldsymbol{\theta}^{*}))^{-1})   \tag*{(4.219)}
$$

where  $\mathbf{F}(\boldsymbol{\theta}^{*})$ is the Fisher information matrix, defined in Equation (4.220).

Equivalently, the above result says that the distribution of  $\sqrt{NF(\boldsymbol{\theta}^{*})(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}^{*})}$ approaches  $\mathcal{N}(\mathbf{0},\mathbf{I})$ where  $\hat{\boldsymbol{\theta}}=\hat{\boldsymbol{\Theta}}^{\mathrm{mle}}(\tilde{\mathcal{D}})$.

The Fisher information matrix measures the amount of curvature of the log-likelihood surface at its peak, as we show below. More formally, the Fisher information matrix (FIM) is defined to be the covariance of the gradient of the log likelihood (also called the score function):

$$
\mathbf{F}(\boldsymbol{\theta})\triangleq\mathbb{E}_{\boldsymbol{x}\sim p(\boldsymbol{x}|\boldsymbol{\theta})}\left[\nabla\log p(\boldsymbol{x}|\boldsymbol{\theta})\nabla\log p(\boldsymbol{x}|\boldsymbol{\theta})^{\top}\right]   \tag*{(4.220)}
$$

Hence the  $(i,j)$th entry has the form

$$
F_{ij}=\mathbb{E}_{\boldsymbol{x}\sim\boldsymbol{\theta}}\left[\left(\frac{\partial}{\partial\theta_{i}}\log p(\boldsymbol{x}|\boldsymbol{\theta})\right)\left(\frac{\partial}{\partial\theta_{j}}\log p(\boldsymbol{x}|\boldsymbol{\theta})\right)\right]   \tag*{(4.221)}
$$

One can show the following result.

Theorem 4.7.2. If  $\log p(\boldsymbol{x}|\boldsymbol{\theta})$ is twice differentiable, and under certain regularity conditions, the FIM is equal to the expected Hessian of the NLL, i.e.,

$$
\mathbf{F}_{ij}=-\mathbb{E}_{\mathbf{x}\sim\theta}\left[\frac{\partial^{2}}{\partial\theta_{i}\theta_{j}}\log p(\mathbf{x}|\boldsymbol{\theta})\right]   \tag*{(4.222)}
$$

If we replace the expectation over x with the observed value, to get the empirical FIM, we see this is equal to the Hessian of the NLL. This helps us understand the result in Equation (4.219): a log-likelihood function with high curvature (large Hessian) will result in a low variance estimate, since the parameters are “well determined” by the data, and hence robust to repeated sampling.

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_208_116_568_338.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(a)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_603_118_961_339.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_209_382_569_586.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(c)</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_602_377_961_587.jpg" alt="Image" width="31%" /></div>

<div style="text-align: center;">(d)</div>

<div style="text-align: center;">Figure 4.23: Bootstrap (top row) vs Bayes (bottom row). The N data cases were generated from  $\text{Ber}(\theta=0.7)$. Left column: N = 10. Right column: N = 100. (a-b) A bootstrap approximation to the sampling distribution of the MLE for a Bernoulli distribution. We show the histogram derived from B = 10,000 bootstrap samples. (c-d) Histogram of 10,000 samples from the posterior distribution using a uniform prior. Generated by bootstrap_demo_bernoulli.ipynb.</div>

In the scalar case, we have that  $\mathbb{V}\left[\hat{\theta} - \theta^*\right] \to \frac{1}{NF(\theta^*)}$. The square root of the variance of the sampling distribution of an estimator is known as its  $\text{standard error}$ or se. Hence we can say that the distribution of  $\frac{\hat{\theta} - \theta^*}{\text{se}}$ approaches  $\mathcal{N}(0,1)$. In practice the se is not known, but it can be estimated from data. For example, suppose  $X_n \sim \text{Ber}(\theta^*)$ and let  $\hat{\theta} = \frac{1}{N} \sum_{n=1}^N X_n$ be the MLE. The standard error is  $\text{se} = \sqrt{\mathbb{V}\left[\hat{\theta}\right]} = \sqrt{\theta^*(1 - \theta^*)/N}$, so the estimated standard error is  $\hat{\text{se}} = \sqrt{\hat{\theta}(1 - \hat{\theta})/N}$.

#### 4.7.3 Bootstrap approximation of the sampling distribution of any estimator

In cases where the estimator is a complex function of the data (e.g., not just an MLE), or when the sample size is small, we can approximate its sampling distribution using a Monte Carlo technique known as the bootstrap.

The idea is simple. If we knew the true parameters  $\boldsymbol{\theta}^*$, we could generate many (say  $S$) fake datasets, each of size  $N$, from the true distribution, using  $\hat{\mathcal{D}}^{(s)} = \{\boldsymbol{x}_n \sim p(\boldsymbol{x}_n | \boldsymbol{\theta}^*) : n = 1 : N\}$. We could then compute our estimate from each sample,  $\hat{\boldsymbol{\theta}}^s = \hat{\boldsymbol{\Theta}}(\tilde{\mathcal{D}}^{(s)})$ and use the empirical distribution of the resulting  $\hat{\boldsymbol{\theta}}^s$ as our estimate of the sampling distribution, as in Equation (4.218). Since  $\boldsymbol{\theta}^*$ is

---

unknown, we can use the dataset itself as an empirical approximation to  $p(\boldsymbol{x}_n|\boldsymbol{\theta}^*)$. More precisely, the idea is to generate each  $\tilde{D}^{(s)}$ by sampling  $N$ data points with replacement from the original dataset. (If we sampled  $N$ times without replacement, we would just recover the original dataset.) This is like “lifting yourself up from your own bootstraps”, since we use the observed data sample to make new hypothetical data samples. $^6$

Figure 4.23(a-b) shows an example where we compute the sampling distribution of the MLE for a Bernoulli using the bootstrap. When N = 10, we see that the sampling distribution is asymmetric, and therefore quite far from Gaussian, but when N = 100, the distribution looks more Gaussian, as theory suggests (see Section 4.7.2).

The number of unique data points in a bootstrap sample is just  $0.632 \times N$, on average. (To see this, note that the probability an item is picked at least once is  $(1 - (1 - 1/N)^N)$, which approaches  $1 - e^{-1} \approx 0.632$ for large  $N$.) However, there are more sophisticated versions of bootstrap that improve on this (see e.g., [Efr87; EH16]).

##### 4.7.3.1 Bootstrap is a “poor man’s” posterior

A natural question is: what is the connection between the parameter estimates  $\hat{\boldsymbol{\theta}}^{s} = \hat{\Theta}(\mathcal{D}^{(s)})$ computed by the bootstrap and parameter values sampled from the posterior,  $\boldsymbol{\theta}^{s} \sim p(\cdot|\mathcal{D})$? Conceptually they are quite different. But in the common case that the estimator is MLE and the prior is not very strong, they can be quite similar. For example, Figure 4.23(c-d) shows an example where we compute the posterior using a uniform Beta(1,1) prior, and then sample from it. We see that the posterior and the sampling distribution are quite similar. So one can think of the bootstrap distribution as a “poor man’s” posterior [HTF01, p235].

However, perhaps surprisingly, bootstrap can be slower than posterior sampling. The reason is that the bootstrap has to generate S sampled datasets, and then fit a model to each one. By contrast, in posterior sampling, we only have to “fit” a model once given a single dataset. (Some methods for speeding up the bootstrap when applied to massive data sets are discussed in [Kle+11].)

#### 4.7.4 Confidence intervals

In frequentist statistics, we use the variability induced by the sampling distribution as a way to estimate uncertainty of a parameter estimate.

In particular, we define a  $100(1 - \alpha)\%$ confidence interval for parameter  $\theta$ as an estimator that returns an interval that captures the true parameter with probability at least  $1 - \alpha$. Denote the estimator by  $I(\mathcal{D}) = (\ell(\mathcal{D}), u(\mathcal{D}))$. The sampling distribution of this estimator is the distribution that is induced by sampling  $\tilde{D} \sim \theta^*$ and then computing  $I(\tilde{D})$. We require that

$$
\operatorname{Pr}(\theta^{*}\in I(\tilde{\mathcal{D}})|\tilde{\mathcal{D}}\sim\theta^{*})\geq1-\alpha   \tag*{(4.223)}
$$

It is common to set  $\alpha = 0.05$, which yields a 95% CI. This means that, if we repeatedly sampled data, and compute  $I(\tilde{\mathcal{D}})$ for each such dataset, then about 95% of such intervals will contain the true parameter  $\theta$.

---

Let us give an example. Suppose that  $\hat{\theta} = \hat{\Theta}(\mathcal{D})$ is an estimator for some parameter with true but unknown value  $\theta^*$. Also, suppose that the sampling distribution of  $\Delta = \theta^* - \hat{\theta}$ is known. Let  $\underline{\delta}$ and  $\overline{\delta}$ denote its  $\alpha/2$ and  $1 - \alpha/2$ quantiles, so

$$
\Pr(\underline{\delta}\leq\Delta\leq\overline{\delta})=\Pr(\underline{\delta}\leq\theta^{*}-\hat{\theta}\leq\overline{\delta})=1-\alpha   \tag*{(4.224)}
$$

Rearranging we get

$$
\Pr(\hat{\theta}+\underline{\delta}\leq\theta^{*}\leq\hat{\theta}+\overline{\delta})=1-\alpha   \tag*{(4.225)}
$$

Hence we can construct a 100(1 -  $\alpha$)\% confidence interval as follows:

$$
I(\mathcal{D})=(L,U)=(\hat{\theta}(\mathcal{D})+\underline{\delta}(\mathcal{D}),\hat{\theta}(\mathcal{D})+\overline{\delta}(\mathcal{D}))   \tag*{(4.226)}
$$

In some cases, we can analytically compute the sampling distribution of the above interval. However, it is more common to assume a Gaussian approximation to the sampling distribution, as in Section 4.7.2. In this case, we have  $\hat{\theta} \approx \mathcal{N}(\theta^*, \hat{\mathbf{s}}^2)$. Hence we can compute an approximate CI using

$$
I=(\hat{\theta}-z_{\alpha/2}\hat{\mathrm{s e}},\hat{\theta}+z_{\alpha/2}\hat{\mathrm{s e}})   \tag*{(4.227)}
$$

where  $z_{\alpha/2}$ is the  $\alpha/2$ quantile of the Gaussian cdf. If we set  $\alpha = 0.05$, we have  $z_{\alpha/2} = 1.96$, which justifies the common approximation  $\hat{\theta} \pm 2\hat{s}e$.

If the Gaussian approximation is not a good one, we can use a bootstrap approximation (see Section 4.7.3). In particular, we sample $S$datasets from$\hat{\theta}(\mathcal{D})$, and apply the estimator to each one to get $\hat{\theta}(\mathcal{D}^{(s)})$; we then use the empirical distribution of $\hat{\theta}(\mathcal{D}) - \hat{\theta}(\mathcal{D}^{(s)})$as an approximation to the sampling distribution of$\Delta$. We can then use the $\alpha/2$and$1 - \alpha/2$quantiles of this distribution to derive the CI (see [Was04, p110] for details).

#### 4.7.5 Caution: Confidence intervals are not credible

It is commonly believed that a 95% confidence interval$ I $for a parameter estimate$ \theta $given data$ \mathcal{D} $means that the true parameter lies in this interval with probability 0.95, i.e.,$ p(\theta^* \in I | \mathcal{D}) = 0.95 $. However, this quantity is what a Bayesian credible interval computes (Section 4.6.6), but is not what a frequentist confidence interval computes. Instead the frequentist approach just means that the procedure for generating CIs will contain the true value 95% of the time. That is, if we repeatedly sample datasets  $\mathcal{D}$ from  $\theta^*$, and compute their CIs to get  $I(\mathcal{D})$, then we have  $\Pr(\theta^* \in I(\mathcal{D})) = 0.95$, as we explain in Section 4.7.4. Thus we see that these concepts are quite different: In the frequentist approach,  $\theta$ is treated as an unknown fixed constant, and the data is treated as random. In the Bayesian approach, we treat the data as fixed (since it is known) and the parameter as random (since it is unknown).

This counter-intuitive definition of confidence intervals can lead to bizarre results. Consider the following example from [Ber85, p11]. Suppose we draw two integers  $\mathcal{D} = (y_1, y_2)$ from

$$
p(y|\theta)=\left\{\begin{array}{ll}0.5&if y=\theta\\0.5&if y=\theta+1\\0&otherwise\end{array}\right.   \tag*{(4.228)}
$$


---

If  $\theta = 39$, we would expect the following outcomes each with probability 0.25:

$$
\left(39,39\right),\left(39,40\right),\left(40,39\right),\left(40,40\right)   \tag*{(4.229)}
$$

Let  $m = \min(y_1, y_2)$ and define the following interval:

$$
[\ell(\mathcal{D}),u(\mathcal{D})]=[m,m]   \tag*{(4.230)}
$$

For the above samples this yields

$$
\left[39,39\right],\quad\left[39,39\right],\quad\left[39,39\right],\quad\left[40,40\right]   \tag*{(4.231)}
$$

Hence Equation (4.230) is clearly a 75% CI, since 39 is contained in 3/4 of these intervals. However, if we observe  $\mathcal{D} = (39, 40)$ then  $p(\theta = 39|\mathcal{D}) = 1.0$, so we know that  $\theta$ must be 39, yet we only have 75% “confidence” in this fact. We see that the CI will “cover” the true parameter 75% of the time, if we compute multiple CIs from different randomly sampled datasets, but if we just have a single observed dataset, and hence a single CI, then the frequentist “coverage” probability can be very misleading.

Another, less contrived, example is as follows. Suppose we want to estimate the parameter  $\theta$ of a Bernoulli distribution. Let  $\overline{y} = \frac{1}{N} \sum_{n=1}^{N} y_n$ be the sample mean. The MLE is  $\hat{\theta} = \overline{y}$. An approximate 95% confidence interval for a Bernoulli parameter is  $\overline{y} \pm 1.96 \sqrt{\frac{\overline{y}(1 - \overline{y})}{N}}$ (this is called a Wald interval and is based on a Gaussian approximation to the Binomial distribution; compare to Equation (4.128)). Now consider a single trial, where  $N = 1$ and  $y_1 = 0$. The MLE is 0, which overfits, as we saw in Section 4.5.1. But our 95% confidence interval is also  $(0, 0)$, which seems even worse. It can be argued that the above flaw is because we approximated the true sampling distribution with a Gaussian, or because the sample size was too small, or the parameter “too extreme”. However, the Wald interval can behave badly even for large N, and non-extreme parameters [BCD01]. By contrast, a Bayesian credible interval with a non-informative Jeffreys prior behaves in the way we would expect.

Several more interesting examples, along with Python code, can be found at [Van14]. See also [Hoe+14; Mor+16; Lyu+20; Cha+19b], who show that many people, including professional statisticians, misunderstand and misuse frequentist confidence intervals in practice, whereas Bayesian credible intervals do not suffer from these problems.

#### 4.7.6 The bias-variance tradeoff

An estimator is a procedure applied to data which returns an estimand. Let  $\hat{\theta}(\cdot)$ be the estimator, and  $\hat{\theta}(\mathcal{D})$ be the estimand. In frequentist statistics, we treat the data as a random variable, drawn from some true but unknown distribution,  $p^{*}(\mathcal{D})$; this induces a distribution over the estimand,  $p^{*}(\hat{\theta}(\mathcal{D}))$, known as the sampling distribution (see Section 4.7.1). In this section, we discuss two key properties of this distribution, its bias and its variance, which we define below.

##### 4.7.6.1 Bias of an estimator

The bias of an estimator is defined as

$$
\mathrm{b i a s}(\hat{\theta}(\cdot))\triangleq\mathbb{E}\left[\hat{\theta}(\mathcal{D})\right]-\theta^{*}   \tag*{(4.232)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

where  $\theta^*$ is the true parameter value, and the expectation is wrt “nature’s distribution”  $p(\mathcal{D}|\theta^*)$. If the bias is zero, the estimator is called unbiased. For example, the MLE for a Gaussian mean is unbiased:

$$
\mathrm{bias}(\hat{\mu})=\mathbb{E}\left[\overline{x}\right]-\mu=\mathbb{E}\left[\frac{1}{N}\sum_{n=1}^{N}x_{n}\right]-\mu=\frac{N\mu}{N}-\mu=0   \tag*{(4.233)}
$$

where  $\overline{x}$ is the sample mean.

However, the MLE for a Gaussian variance,  $\sigma_{\mathrm{mle}}^{2} = \frac{1}{N} \sum_{n=1}^{N} (x_{n} - \overline{x})^{2}$, is not an unbiased estimator of  $\sigma^{2}$. In fact, one can show (Exercise 4.7) that

$$
\mathbb{E}\left[\sigma_{mle}^{2}\right]=\frac{N-1}{N}\sigma^{2}   \tag*{(4.234)}
$$

so the ML estimator slightly underestimates the variance. Intuitively, this is because we “use up” one of the data points to estimate the mean, so if we have a sample size of 1, we will estimate the variance to be 0. If, however,  $\mu$ is known, the ML estimator is unbiased (see Exercise 4.8).

Now consider the following estimator

$$
\sigma_{\mathrm{unb}}^{2}\triangleq\frac{1}{N-1}\sum_{n=1}^{N}(x_{n}-\overline{x})^{2}=\frac{N}{N-1}\sigma_{\mathrm{m l e}}^{2}   \tag*{(4.235)}
$$

This is an unbiased estimator, which we can easily prove as follows:

$$
\mathbb{E}\left[\sigma_{\mathrm{unb}}^{2}\right]=\frac{N}{N-1}\mathbb{E}\left[\sigma_{\mathrm{mle}}^{2}\right]=\frac{N}{N-1}\frac{N-1}{N}\sigma^{2}=\sigma^{2}   \tag*{(4.236)}
$$

##### 4.7.6.2 Variance of an estimator

It seems intuitively reasonable that we want our estimator to be unbiased. However, being unbiased is not enough. For example, suppose we want to estimate the mean of a Gaussian from $\mathcal{D} = \{x_1, \ldots, x_N\}$. The estimator that just looks at the first data point, $\hat{\theta}(\mathcal{D}) = x_1$, is an unbiased estimator, but will generally be further from $\theta^*$than the empirical mean$\overline{x}$ (which is also unbiased). So the variance of an estimator is also important.

We define the variance of an estimator as follows:

$$
\mathbb{V}\left[\hat{\theta}\right]\triangleq\mathbb{E}\left[\hat{\theta}^{2}\right]-\left(\mathbb{E}\left[\hat{\theta}\right]\right)^{2}   \tag*{(4.237)}
$$

where the expectation is taken wrt  $p(\mathcal{D}|\theta^*)$. This measures how much our estimate will change as the data changes. We can extend this to a covariance matrix for vector valued estimators.

Intuitively we would like the variance of our estimator to be as small as possible. Therefore, a natural question is: how low can the variance go? A famous result, called the Cramer-Rao lower bound, provides a lower bound on the variance of any unbiased estimator. More precisely, let  $X_1, \ldots, X_N \sim p(X|\theta^*)$ and  $\hat{\theta} = \hat{\theta}(x_1, \ldots, x_N)$ be an unbiased estimator of  $\theta^*$. Then, under various smoothness assumptions on  $p(X|\theta^*)$, we have  $\mathbb{V}\left[\hat{\theta}\right] \geq \frac{1}{NF(\theta^*)}$, where  $F(\theta^*)$ is the Fisher information matrix (Section 4.7.2). A proof can be found e.g., in [Ric95, p275].

It can be shown that the MLE achieves the Cramer Rao lower bound, and hence has the smallest asymptotic variance of any unbiased estimator. Thus MLE is said to be asymptotically optimal.

---

##### 4.7.6.3 The bias-variance tradeoff

In this section, we discuss a fundamental tradeoff that needs to be made when picking a method for parameter estimation, assuming our goal is to minimize the mean squared error (MSE) of our estimate. Let  $\hat{\theta} = \hat{\theta}(\mathcal{D})$ denote the estimate, and  $\overline{\theta} = \mathbb{E}\left[\hat{\theta}\right]$ denote the expected value of the estimate (as we vary  $\mathcal{D}$). (All expectations and variances are wrt  $p(\mathcal{D}|\theta^*)$, but we drop the explicit conditioning for notational brevity.) Then we have

$$
\mathbb{E}\left[(\hat{\theta}-\theta^{*})^{2}\right]=\mathbb{E}\left[\left[(\hat{\theta}-\overline{\theta})+(\overline{\theta}-\theta^{*})\right]^{2}\right]   \tag*{(4.238)}
$$

$$
=\mathbb{E}\left[\left(\hat{\theta}-\overline{\theta}\right)^{2}\right]+2(\overline{\theta}-\theta^{*})\mathbb{E}\left[\hat{\theta}-\overline{\theta}\right]+(\overline{\theta}-\theta^{*})^{2}   \tag*{(4.239)}
$$

$$
=\mathbb{E}\left[\left(\hat{\theta}-\overline{\theta}\right)^{2}\right]+(\overline{\theta}-\theta^{*})^{2}   \tag*{(4.240)}
$$

$$
=\mathbb{V}\left[\hat{\theta}\right]+\mathrm{b i a s}^{2}(\hat{\theta})   \tag*{(4.241)}
$$

In words,

 
$$
\mathrm{M S E}=\mathrm{v a r i a n c e}+\mathrm{b i a s}^{2}
$$
 

This is called the bias-variance tradeoff (see e.g., [GBD92]). What it means is that it might be wise to use a biased estimator, so long as it reduces our variance by more than the square of the bias, assuming our goal is to minimize squared error.

##### 4.7.6.4 Example: MAP estimator for a Gaussian mean

Let us give an example, based on [Hof09, p79]. Suppose we want to estimate the mean of a Gaussian from  $\boldsymbol{x} = (x_1, \ldots, x_N)$. We assume the data is sampled from  $x_n \sim \mathcal{N}(\theta^* = 1, \sigma^2)$. An obvious estimate is the MLE. This has a bias of 0 and a variance of

$$
\mathbb{V}\left[\overline{x}|\theta^{*}\right]=\frac{\sigma^{2}}{N}   \tag*{(4.243)}
$$

But we could also use a MAP estimate. In Section 4.6.4.2, we show that the MAP estimate under a Gaussian prior of the form  $\mathcal{N}(\theta_0, \sigma^2/\kappa_0)$ is given by

$$
\tilde{x}\triangleq\frac{N}{N+\kappa_{0}}\overline{x}+\frac{\kappa_{0}}{N+\kappa_{0}}\theta_{0}=w\overline{x}+(1-w)\theta_{0}   \tag*{(4.244)}
$$

where  $0 \leq w \leq 1$ controls how much we trust the MLE compared to our prior. The bias and variance are given by

$$
\mathbb{E}\left[\tilde{x}\right]-\theta^{*}=w\theta^{*}+(1-w)\theta_{0}-\theta^{*}=\left(1-w\right)\left(\theta_{0}-\theta^{*}\right)   \tag*{(4.245)}
$$

$$
\mathbb{V}\left[\tilde{x}\right]=w^{2}\frac{\sigma^{2}}{N}   \tag*{(4.246)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_229_123_535_375.jpg" alt="Image" width="26%" /></div>

<div style="text-align: center;"> $(a)$</div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_625_123_938_384.jpg" alt="Image" width="27%" /></div>

<div style="text-align: center;">(b)</div>

<div style="text-align: center;">Figure 4.24: Left: Sampling distribution of the MAP estimate (equivalent to the posterior mean) under a  $\mathcal{N}(\theta_0 = 0, \sigma^2 / \kappa_0)$ prior with different prior strengths  $\kappa_0$. (If we set  $\kappa = 0$, the MAP estimate reduces to the MLE.) The data is  $n = 5$ samples drawn from  $\mathcal{N}(\theta^* = 1, \sigma^2 = 1)$. Right: MSE relative to that of the MLE versus sample size. Adapted from Figure 5.6 of [Hof09]. Generated by samplingDistributionGaussianShrinkage.ipynb.</div>

So although the MAP estimate is biased (assuming w < 1), it has lower variance.

Let us assume that our prior is slightly misspecified, so we use  $\theta_0 = 0$, whereas the truth is  $\theta^* = 1$. In Figure 4.24(a), we see that the sampling distribution of the MAP estimate for  $\kappa_0 > 0$ is biased away from the truth, but has lower variance (is narrower) than that of the MLE.

In Figure 4.24(b), we plot  $\text{mse}(\tilde{x})/\text{mse}(\overline{x})$ vs  $N$. We see that the MAP estimate has lower MSE than the MLE for  $\kappa_0 \in \{1, 2\}$. The case  $\kappa_0 = 0$ corresponds to the MLE, and the case  $\kappa_0 = 3$ corresponds to a strong prior, which hurts performance because the prior mean is wrong. Thus we see that, provided the prior strength is properly “tuned”, a MAP estimate can outperform an ML estimate in terms of minimizing MSE.

##### 4.7.6.5 Example: MAP estimator for linear regression

Another important example of the bias-variance tradeoff arises in ridge regression, which we discuss in Section 11.3. In brief, this corresponds to MAP estimation for linear regression under a Gaussian prior,  $p(\boldsymbol{w}) = \mathcal{N}(\boldsymbol{w} | \boldsymbol{0}, \lambda^{-1} \mathbf{I})$. The zero-mean prior encourages the weights to be small, which reduces overfitting; the precision term,  $\lambda$, controls the strength of this prior. Setting  $\lambda = 0$ results in the MLE; using  $\lambda > 0$ results in a biased estimate. To illustrate the effect on the variance, consider a simple example where we fit a 1d ridge regression model using 2 different values of  $\lambda$. Figure 4.25 on the left plots each individual fitted curve, and on the right plots the average fitted curve. We see that as we increase the strength of the regularizer, the variance decreases, but the bias increases.

See also Figure 4.26 where we give a cartoon sketch of the bias variance tradeoff in terms of model complexity.

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_319_164_567_375.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_597_163_849_374.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_319_400_566_595.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_597_393_848_594.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;">Figure 4.25: Illustration of bias-variance tradeoff for ridge regression. We generate 100 data sets from the true function, shown in solid green. Left: we plot the regularized fit for 20 different data sets. We use linear regression with a Gaussian RBF expansion, with 25 centers evenly spread over the [0,1] interval. Right: we plot the average of the fits, averaged over all 100 datasets. Top row: strongly regularized: we see that the individual fits are similar to each other (low variance), but the average is far from the truth (high bias). Bottom row: lightly regularized: we see that the individual fits are quite different from each other (high variance), but the average is close to the truth (low bias). Adapted from [Bis06] Figure 3.5. Generated by biasVarModelComplexity3.ipynb.</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_319_897_608_1092.jpg" alt="Image" width="25%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_651_902_841_1089.jpg" alt="Image" width="16%" /></div>

<div style="text-align: center;">Figure 4.26: Cartoon illustration of the bias variance tradeoff. From http://scott.fortmann-roe.com/docs/BiasVariance.html. Used with kind permission of Scott Fortmann-Roe.</div>


---

##### 4.7.6.6 Bias-variance tradeoff for classification

If we use 0-1 loss instead of squared error, the frequentist risk is no longer expressible as squared bias plus variance. In fact, one can show (Exercise 7.2 of [HTF09]) that the bias and variance combine multiplicatively. If the estimate is on the correct side of the decision boundary, then the bias is negative, and decreasing the variance will decrease the misclassification rate. But if the estimate is on the wrong side of the decision boundary, then the bias is positive, so it pays to increase the variance [Fri97a]. This little known fact illustrates that the bias-variance tradeoff is not very useful for classification. It is better to focus on expected loss, not directly on bias and variance. We can approximate the expected loss using cross validation, as we discuss in Section 4.5.5.

### 4.8 Exercises

Exercise 4.1 [MLE for the univariate Gaussian †]

Show that the MLE for a univariate Gaussian is given by

$$
\hat{\mu}=\frac{1}{N}\sum_{n=1}^{N}y_{n}   \tag*{(4.247)}
$$

$$
\hat{\sigma}^{2}=\frac{1}{N}\sum_{n=1}^{N}(y_{n}-\hat{\mu})^{2}   \tag*{(4.248)}
$$

##### Exercise 4.2 [MAP estimation for 1D Gaussians  $\dagger$]

(Source: Jaakkola.)

Consider samples  $x_1, \ldots, x_n$ from a Gaussian random variable with known variance  $\sigma^2$ and unknown mean  $\mu$. We further assume a prior distribution (also Gaussian) over the mean,  $\mu \sim \mathcal{N}(m, s^2)$, with fixed mean  $m$ and fixed variance  $s^2$. Thus the only unknown is  $\mu$.

a. Calculate the MAP estimate  $\hat{\mu}_{MAP}$. You can state the result without proof. Alternatively, with a lot more work, you can compute derivatives of the log posterior, set to zero and solve.

b. Show that as the number of samples n increase, the MAP estimate converges to the maximum likelihood estimate.

c. Suppose $n$is small and fixed. What does the MAP estimator converge to if we increase the prior variance$s^{2}$?

d. Suppose n is small and fixed. What does the MAP estimator converge to if we decrease the prior variance  $s^{2}$?

##### Exercise 4.3 [Gaussian posterior credible interval]

(Source: DeGroot.) Let  $X \sim \mathcal{N}(\mu, \sigma^2 = 4)$ where  $\mu$ is unknown but has prior  $\mu \sim \mathcal{N}(\mu_0, \sigma_0^2 = 9)$. The posterior after seeing  $n$ samples is  $\mu \sim \mathcal{N}(\mu_n, \sigma_n^2)$. (This is called a credible interval, and is the Bayesian analog of a confidence interval.) How big does  $n$ have to be to ensure

$$
p(\ell\leq\mu_{n}\leq u|D)\geq0.95   \tag*{(4.249)}
$$

where $(\ell, u)$is an interval (centered on$\mu_n$) of width 1 and $D$is the data? Hint: recall that 95% of the probability mass of a Gaussian is within$\pm 1.96\sigma$ of the mean.

---

##### Exercise 4.4 [BIC for Gaussians  $\dagger$]

(Source: Jaakkola.)

The Bayesian information criterion (BIC) is a penalized log-likelihood function that can be used for model selection. It is defined as

$$
B I C=\log p(\mathcal{D}|\hat{\pmb{\theta}}_{M L})-\frac{d}{2}\log(N)   \tag*{(4.250)}
$$

where d is the number of free parameters in the model and N is the number of samples. In this question, we will see how to use this to choose between a full covariance Gaussian and a Gaussian with a diagonal covariance. Obviously a full covariance Gaussian has higher likelihood, but it may not be “worth” the extra parameters if the improvement over a diagonal covariance matrix is too small. So we use the BIC score to choose the model.

We can write

$$
\log p(\mathcal{D}|\hat{\mathbf{\Sigma}},\hat{\boldsymbol{\mu}})=-\frac{N}{2}\mathrm{t r}\left(\hat{\mathbf{\Sigma}}^{-1}\hat{\mathbf{S}}\right)-\frac{N}{2}\log(|\hat{\mathbf{\Sigma}}|)   \tag*{(4.251)}
$$

$$
\hat{\mathbf{S}}=\frac{1}{N}\sum_{i=1}^{N}(\mathbf{x}_{i}-\overline{\mathbf{x}})(\mathbf{x}_{i}-\overline{\mathbf{x}})^{T}   \tag*{(4.252)}
$$

where  $\hat{S}$ is the scatter matrix (empirical covariance), the trace of a matrix is the sum of its diagonals, and we have used the trace trick.

a. Derive the BIC score for a Gaussian in D dimensions with full covariance matrix. Simplify your answer as much as possible, exploiting the form of the MLE. Be sure to specify the number of free parameters d.

b. Derive the BIC score for a Gaussian in $D$dimensions with a diagonal covariance matrix. Be sure to specify the number of free parameters$d$. Hint: for the digaonal case, the ML estimate of $\Sigma$is the same as$\hat{\Sigma}_{ML}$ except the off-diagonal terms are zero:

$$
\hat{\mathbf{\Sigma}}_{d i a g}=\mathrm{d i a g}(\hat{\mathbf{\Sigma}}_{M L}(1,1),\ldots,\hat{\mathbf{\Sigma}}_{M L}(D,D))   \tag*{(4.253)}
$$

##### Exercise 4.5 [BIC for a 2d discrete distribution]

(Source: Jaakkola.)

Let  $x \in \{0,1\}$ denote the result of a coin toss ( $x = 0$ for tails,  $x = 1$ for heads). The coin is potentially biased, so that heads occurs with probability  $\theta_1$. Suppose that someone else observes the coin flip and reports to you the outcome,  $y$. But this person is unreliable and only reports the result correctly with probability  $\theta_2$; i.e.,  $p(y | x, \theta_2)$ is given by

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>y=0</td><td style='text-align: center; word-wrap: break-word;'>y=1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>x=0</td><td style='text-align: center; word-wrap: break-word;'>$\theta_{2}$</td><td style='text-align: center; word-wrap: break-word;'>$1-\theta_{2}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>x=1</td><td style='text-align: center; word-wrap: break-word;'>$1-\theta_{2}$</td><td style='text-align: center; word-wrap: break-word;'>$\theta_{2}$</td></tr></table>

Assume that  $\theta_{2}$ is independent of x and  $\theta_{1}$

a. Write down the joint probability distribution  $p(x, y|\boldsymbol{\theta})$ as a  $2 \times 2$ table, in terms of  $\boldsymbol{\theta} = (\theta_1, \theta_2)$.

b. Suppose have the following dataset:  $\boldsymbol{x} = (1, 1, 0, 1, 1, 0, 0)$,  $\boldsymbol{y} = (1, 0, 0, 0, 1, 0, 1)$. What are the MLEs for  $\theta_1$ and  $\theta_2$? Justify your answer. Hint: note that the likelihood function factorizes,

$$
p(x,y|\boldsymbol{\theta})=p(y|x,\theta_{2})p(x|\theta_{1})   \tag*{(4.254)}
$$

What is  $p(\mathcal{D}|\hat{\boldsymbol{\theta}}, M_{2})$ where  $M_{2}$ denotes this 2-parameter model? (You may leave your answer in fractional form if you wish.)

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

c. Now consider a model with 4 parameters,  $\boldsymbol{\theta} = (\theta_{0,0}, \theta_{0,1}, \theta_{1,0}, \theta_{1,1})$, representing  $p(x, y|\boldsymbol{\theta}) = \theta_{x,y}$. (Only 3 of these parameters are free to vary, since they must sum to one.) What is the MLE of  $\boldsymbol{\theta}$? What is  $p(\mathcal{D}|\hat{\boldsymbol{\theta}}, M_4)$ where  $M_4$ denotes this 4-parameter model?

d. Suppose we are not sure which model is correct. We compute the leave-one-out cross validated log likelihood of the 2-parameter model and the 4-parameter model as follows:

$$
L(m)=\sum_{i=1}^{n}\log p(x_{i},y_{i}|m,\hat{\theta}(\mathcal{D}_{-i}))   \tag*{(4.255)}
$$

and  $\hat{\theta}(\mathcal{D}_{-i})$ denotes the MLE computed on  $\mathcal{D}$ excluding row i. Which model will CV pick and why? Hint: notice how the table of counts changes when you omit each training case one at a time.

e. Recall that an alternative to CV is to use the BIC score, defined as

$$
\mathrm{B I C}(M,\mathcal{D})\triangleq\log p(\mathcal{D}|\hat{\boldsymbol{\theta}}_{M L E})-\frac{\mathrm{d o f}(M)}{2}\log N   \tag*{(4.256)}
$$

where  $\text{dof}(M)$ is the number of free parameters in the model, Compute the BIC scores for both models (use log base e). Which model does BIC prefer?

Exercise 4.6 [A mixture of conjugate priors is conjugate  $\dagger$]

Consider a mixture prior

$$
p(\theta)=\sum_{k}p(z=k)p(\theta|z=k)   \tag*{(4.257)}
$$

where each  $p(\theta|z=k)$ is conjugate to the likelihood. Prove that this is a conjugate prior.

Exercise 4.7 [ML estimator  $\sigma_{mle}^{2}$ is biased]

Show that  $\hat{\sigma}_{MLE}^2 = \frac{1}{N} \sum_{n=1}^N (x_n - \hat{\mu})^2$ is a biased estimator of  $\sigma^2$, i.e., show

 
$$
\mathbf{E}_{\mathrm{X}_{1},\ldots,\mathrm{X}_{\mathrm{n}}\sim\mathcal{N}(\mu,\sigma)}\big[\hat{\sigma}^{2}(\mathrm{X}_{1},\ldots,\mathrm{X}_{\mathrm{n}})\big]\neq\sigma^{2}
$$
 

Hint: note that  $X_{1},\ldots,X_{N}$ are independent, and use the fact that the expectation of a product of independent random variables is the product of the expectations.

##### Exercise 4.8 [Estimation of  $\sigma^{2}$ when  $\mu$ is known  $\dagger$]

Suppose we sample  $x_1, \ldots, x_N \sim \mathcal{N}(\mu, \sigma^2)$ where  $\mu$ is a known constant. Derive an expression for the MLE for  $\sigma^2$ in this case. Is it unbiased?

Exercise 4.9 [Variance and MSE of estimators for Gaussian variance  $\dagger$ ] Prove that the standard error for the MLE for a Gaussian variance is

$$
\sqrt{\mathbb{V}\left[\sigma_{mle}^{2}\right]}=\sqrt{\frac{2(N-1)}{N^{2}}}\sigma^{2}   \tag*{(4.258)}
$$

Hint: use the fact that

$$
\frac{N-1}{\sigma^{2}}\sigma_{\mathrm{unb}}^{2}\sim\chi_{N-1}^{2},   \tag*{(4.259)}
$$

and that  $\mathbb{V}\left[\chi_{N-1}^{2}\right]=2(N-1)$. Finally, show that  $\mathrm{MSE}(\sigma_{\mathrm{unb}}^{2})=\frac{2N-1}{N^{2}}\sigma^{4}$ and  $\mathrm{MSE}(\sigma_{\mathrm{mle}}^{2})=\frac{2}{N-1}\sigma^{4}$.

---

## 5 Decision Theory

### 5.1 Bayesian decision theory

Bayesian inference provides the optimal way to update our beliefs about hidden quantities H given observed data  $\mathbf{X} = \mathbf{x}$ by computing the posterior  $p(H|\mathbf{x})$. However, at the end of the day, we need to turn our beliefs into actions that we can perform in the world. How can we decide which action is best? This is where Bayesian decision theory comes in. In this chapter, we give a brief introduction. For more details, see e.g., [DeG70; KWW22].

#### 5.1.1 Basics

In decision theory, we assume the decision maker, or  $\underline{\text{agent}}$, has a set of possible actions, A, to choose from. For example, consider the case of a hypothetical doctor treating someone who may have COVID-19. Suppose the actions are to do nothing, or to give the patient an expensive drug with bad side effects, but which can save their life.

Each of these actions has costs and benefits, which will depend on the underlying state of nature  $H \in \mathcal{H}$. We can encode this information into a loss function  $\ell(h, a)$, that specifies the loss we incur if we take action  $a \in \mathcal{A}$ when the state of nature is  $h \in \mathcal{H}$.

For example, suppose the state is defined by the age of the patient (young vs old), and whether they have COVID-19 or not. Note that the age can be observed directly, but the disease state must be inferred from noisy observations, as we discussed in Section 2.3. Thus the state is partially observed.

Let us assume that the cost of administering a drug is the same, no matter what the state of the patient is. However, the benefits will differ. If the patient is young, we expect them to live a long time, so the cost of not giving the drug if they have COVID-19 is high; but if the patient is old, they have fewer years to live, so the cost of not giving the drug if they have COVID-19 is arguably less (especially in view of the side effects). In medical circles, a common unit of cost is quality-adjusted life years or QALY. Suppose that the expected QALY for a young person is 60, and for an old person is 10. Let us assume the drug costs the equivalent of 8 QALY, due to induced pain and suffering from side effects. Then we get the loss matrix shown in Table 5.1.

These numbers reflect relative costs and benefits, and will depend on many factors. The numbers can be derived by asking the decision maker about their preferences about different possible outcomes. It is a theorem of decision theory that any consistent set of preferences can be converted into an ordinal cost scale (see e.g., https://en.wikipedia.org/wiki/Preference_(economics)).

Once we have specified the loss function, we can compute the posterior expected loss or risk

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>State</td><td style='text-align: center; word-wrap: break-word;'>Nothing</td><td style='text-align: center; word-wrap: break-word;'>Drugs</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No COVID-19, young</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COVID-19, young</td><td style='text-align: center; word-wrap: break-word;'>60</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>No COVID-19, old</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>COVID-19, old</td><td style='text-align: center; word-wrap: break-word;'>10</td><td style='text-align: center; word-wrap: break-word;'>8</td></tr></table>

<div style="text-align: center;">Table 5.1: Hypothetical loss matrix for a decision maker, where there are 4 states of nature, and 2 possible actions.</div>

<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>test</td><td style='text-align: center; word-wrap: break-word;'>age</td><td style='text-align: center; word-wrap: break-word;'>pr(covid)</td><td style='text-align: center; word-wrap: break-word;'>cost-noop</td><td style='text-align: center; word-wrap: break-word;'>cost-drugs</td><td style='text-align: center; word-wrap: break-word;'>action</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>0.84</td><td style='text-align: center; word-wrap: break-word;'>8.00</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.01</td><td style='text-align: center; word-wrap: break-word;'>0.14</td><td style='text-align: center; word-wrap: break-word;'>8.00</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.80</td><td style='text-align: center; word-wrap: break-word;'>47.73</td><td style='text-align: center; word-wrap: break-word;'>8.00</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0.80</td><td style='text-align: center; word-wrap: break-word;'>7.95</td><td style='text-align: center; word-wrap: break-word;'>8.00</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;">Table 5.2: Optimal policy for treating COVID-19 patients for each possible observation.</div>

for each possible action a given all the relevant evidence, which may be a single datum x or an entire data set D, depending on the problem:

$$
\rho(a|\boldsymbol{x})\triangleq\mathbb{E}_{p(h|\boldsymbol{x})}\left[\ell(h,a)\right]=\sum_{h\in\mathcal{H}}\ell(h,a)p(h|\boldsymbol{x})   \tag*{(5.1)}
$$

The optimal policy  $\pi^{*}(x)$, also called the Bayes estimator or Bayes decision rule  $\delta^{*}(x)$, specifies what action to take when presented with evidence x so as to minimize the risk:

$$
\pi^{*}(\boldsymbol{x})=\underset{a\in\mathcal{A}}{\operatorname{argmin}}\mathbb{E}_{p(h|\boldsymbol{x})}\left[\ell(h,a)\right]   \tag*{(5.2)}
$$

An alternative, but equivalent, way of stating this result is as follows. Let us define a utility function  $U(h,a)$ to be the desirability of each possible action in each possible state. If we set  $U(h,a) = -\ell(h,a)$, then the optimal policy is as follows:

$$
\pi^{*}(\boldsymbol{x})=\underset{a\in\mathcal{A}}{\operatorname{argmax}}\mathbb{E}_{h}\left[U(h,a)\right]   \tag*{(5.3)}
$$

This is called the maximum expected utility principle.

Let us return to our COVID-19 example. The observation x consists of the age (young or old) and the test result (positive or negative). Using the results from Section 2.3.1 on Bayes rule for COVID-19 diagnosis, we can convert the test result into a distribution over disease states (i.e., compute the probability the patient has COVID-19 or not). Given this belief state, and the loss matrix in Table 5.1, we can compute the optimal policy for each possible observation, as shown in Table 5.2.

We see from Table 5.2 that the drug should only be given to young people who test positive. If, however, we reduce the cost of the drug from 8 units to 5, then the optimal policy changes: in this case, we should give the drug to everyone who tests positive. The policy can also change depending

---

on the reliability of the test. For example, if we increase the sensitivity from 0.875 to 0.975, then the probability that someone has COVID-19 if they test positive increases from 0.80 to 0.81, which changes the optimal policy to be one in which we should administer the drug to everyone who tests positive, even if the drug costs 8 QALY. (See dtheory.ipynb for the code to reproduce this example.)

So far, we have implicitly assumed that the agent is \textbf{risk} \textbf{neutral}. This means that their decision is not affected by the degree of certainty in a set of outcomes. For example, such an agent would be indifferent between getting $50 for sure, or a 50% chance of $100 or $0. By contrast, a \textbf{risk} \textbf{averse} agent would choose the first. We can generalize the framework of Bayesian decision theory to \textbf{risk} \textbf{sensitive} applications, but we do not pursue the matter here. (See e.g., \textbf{Cho+15} for details.)

#### 5.1.2 Classification problems

In this section, we use Bayesian decision theory to decide the optimal class label to predict given an observed input  $\boldsymbol{x} \in \mathcal{X}$.

##### 5.1.2.1 Zero-one loss

Suppose the states of nature correspond to class labels, so  $\mathcal{H} = \mathcal{Y} = \{1, \ldots, C\}$. Furthermore, suppose the actions also correspond to class labels, so  $\mathcal{A} = \mathcal{Y}$. In this setting, a very commonly used loss function is the zero-one loss  $\ell_{01}(y^{*}, \hat{y})$, defined as follows:

$$
\begin{array}{c|ccc}{{{}}&{{{\hat{y}=0}}}&{{{\hat{y}=1}}} \\{{{\hline y^{*}=0}}}&{{{0}}}&{{{1}}} \\{{{y^{*}=1}}}&{{{1}}}&{{{0}}} \\\end{array}   \tag*{(5.4)}
$$

We can write this more concisely as follows:

$$
\ell_{01}(y^{*},\hat{y})=\mathbb{I}(y^{*}\neq\hat{y})   \tag*{(5.5)}
$$

In this case, the posterior expected loss is

 
$$
\rho(\hat{y}|\boldsymbol{x})=p(\hat{y}\neq y^{*}|\boldsymbol{x})=1-p(y^{*}=\hat{y}|\boldsymbol{x})
$$
 

Hence the action that minimizes the expected loss is to choose the most probable label:

$$
\pi(\boldsymbol{x})=\underset{y\in\mathcal{Y}}{\operatorname{argmax}}p(y|\boldsymbol{x})   \tag*{(5.7)}
$$

This corresponds to the mode of the posterior distribution, also known as the maximum a posteriori or MAP estimate.

##### 5.1.2.2 Cost-sensitive classification

Consider a binary classification problem where the loss function is  $\ell(y^{*},\hat{y})$ is as follows:

$$
\left(\begin{array}{l l}\ell_{00}&\ell_{01}\\ \ell_{10}&\ell_{11}\end{array}\right)   \tag*{(5.8)}
$$

Author: Kevin P. Murphy. (C) MIT Press. CC-BY-NC-ND license

---

Let  $p_0 = p(y^* = 0 | x)$ and  $p_1 = 1 - p_0$. Thus we should choose label  $\hat{y} = 0$ iff

$$
\ell_{00}p_{0}+\ell_{10}p_{1}<\ell_{01}p_{0}+\ell_{11}p_{1}   \tag*{(5.9)}
$$

If  $\ell_{00} = \ell_{11} = 0$, this simplifies to

$$
p_{1}<\frac{\ell_{01}}{\ell_{01}+\ell_{10}}   \tag*{(5.10)}
$$

Now suppose $\ell_{10} = c\ell_{01}$, so a false negative costs $c$times more than a false positive. The decision rule further simplifies to the following: pick$a = 0$iff$p_1 < 1/(1 + c)$. For example, if a false negative costs twice as much as false positive, so $c = 2$, then we use a decision threshold of $1/3$before declaring a positive.

##### 5.1.2.3 Classification with the “reject” option

In some cases, we may able to say “I don’t know” instead of returning an answer that we don’t really trust; this is called picking the reject option (see e.g., [BW08]). This is particularly important in domains such as medicine and finance where we may be risk averse.

We can formalize the reject option as follows. Suppose the states of nature are$ \mathcal{H} = \mathcal{Y} = \{1, \ldots, C\} $, and the actions are  $\mathcal{A} = \mathcal{Y} \cup \{0\}$, where action 0 represents the reject action. Now define the following loss function:

$$
\ell(y^{*},a)=\left\{\begin{array}{ll}0&\text{if}y^{*}=a\text{and}a\in\{1,\ldots,C\}\\ \lambda_{r}&\text{if}a=0\\ \lambda_{e}&\text{otherwise}\end{array}\right.   \tag*{(5.11)}
$$

where  $\lambda_r$ is the cost of the reject action, and  $\lambda_e$ is the cost of a classification error. Exercise 5.1 asks you to show that the optimal action is to pick the reject action if the most probable class has a probability below  $\lambda^* = 1 - \frac{\lambda_r}{\lambda_e}$; otherwise you should just pick the most probable class. In other words, the optimal policy is as follows (known as  $\text{Chow's}$ rule [Cho70]):

$$
a^{*}=\begin{cases}y^{*}&if p^{*}>\lambda^{*}\\ reject&otherwise\end{cases}   \tag*{(5.12)}
$$

where

$$
y^{*}=\underset{y\in\{1,\ldots,C\}}{\operatorname{argmax}}p(y|x)   \tag*{(5.13)}
$$

$$
p^{*}=p(y^{*}|x)=\max_{y\in\{1,\ldots,C\}}p(y|x)   \tag*{(5.14)}
$$

$$
\lambda^{*}=1-\frac{\lambda_{r}}{\lambda_{e}}   \tag*{(5.15)}
$$

See Figure 5.1 for an illustration.

One interesting application of the reject option arises when playing the TV game show Jeopardy. In this game, contestants have to solve various word puzzles and answer a variety of trivia questions, but if they answer incorrectly, they lose money. In 2011, IBM unveiled a computer system called Watson