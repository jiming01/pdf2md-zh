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

maintain, for each action a, a record of all the rewards that have followed the selection of that action. Then, when the estimate of the value of action a is needed at time t, it can be computed according to (2.1), which we repeat here:

 
$$
Q_{t}(a)=\frac{R_{1}+R_{2}+\cdots+R_{N_{t}(a)}}{N_{t}(a)},
$$
 

where here  $R_{1},\ldots,R_{N_{t}(a)}$ are all the rewards received following all selections of action a prior to play t. A problem with this straightforward implementation is that its memory and computational requirements grow over time without bound. That is, each additional reward following a selection of action a requires more memory to store it and results in more computation being required to determine  $Q_{t}(a)$.

As you might suspect, this is not really necessary. It is easy to devise incremental update formulas for computing averages with small, constant computation required to process each new reward. For some action, let  $Q_k$ denote the estimate for its  $k$th reward, that is, the average of its first  $k - 1$ rewards. Given this average and a  $k$th reward for the action,  $R_k$, then the average of all  $k$ rewards can be computed by

$$
\begin{array}{rcl}Q_{k+1}&=&\displaystyle\frac{1}{k}\sum_{i=1}^{k}R_{i}\\&=&\displaystyle\frac{1}{k}\left(R_{k}+\sum_{i=1}^{k-1}R_{i}\right)\\&=&\displaystyle\frac{1}{k}\Big(R_{k}+(k-1)Q_{k}+Q_{k}-Q_{k}\Big)\\&=&\displaystyle\frac{1}{k}\Big(R_{k}+k Q_{k}-Q_{k}\Big)\\&=&\displaystyle Q_{k}+\displaystyle\frac{1}{k}\Big[R_{k}-Q_{k}\Big],\end{array}   \tag*{(2.3)}
$$

which holds even for $k=1$, obtaining $Q_{2}=R_{1}$for arbitrary$Q_{1}$. This implementation requires memory only for $Q_{k}$and$k$, and only the small computation (2.3) for each new reward.

The update rule  $(2.3)$ is of a form that occurs frequently throughout this book. The general form is

$$
NewEstimate\leftarrow OldEstimate\;+\;StepSize\left[Target-OldEstimate\right].   \tag*{(2.4)}
$$

The expression  $[Target - OldEstimate]$ is an error in the estimate. It is reduced by taking a step toward the “Target.” The target is presumed to

---

indicate a desirable direction in which to move, though it may be noisy. In the case above, for example, the target is the kth reward.

Note that the step-size parameter (StepSize) used in the incremental method described above changes from time step to time step. In processing the kth reward for action a, that method uses a step-size parameter of  $\frac{1}{k}$. In this book we denote the step-size parameter by the symbol  $\alpha$ or, more generally, by  $\alpha_t(a)$. We sometimes use the informal shorthand  $\alpha = \frac{1}{k}$ to refer to this case, leaving the dependence of k on the action implicit.

## 2.4 Tracking a Nonstationary Problem

The averaging methods discussed so far are appropriate in a stationary environment, but not if the bandit is changing over time. As noted earlier, we often encounter reinforcement learning problems that are effectively nonstationary. In such cases it makes sense to weight recent rewards more heavily than long-past ones. One of the most popular ways of doing this is to use a constant step-size parameter. For example, the incremental update rule (2.3) for updating an average  $Q_k$ of the  $k-1$ past rewards is modified to be

$$
Q_{k+1}=Q_{k}+\alpha\Big[R_{k}-Q_{k}\Big],   \tag*{(2.5)}
$$

where the step-size parameter  $\alpha \in (0,1]^{1}$ is constant. This results in  $Q_{k+1}$ being a weighted average of past rewards and the initial estimate  $Q_{1}$:

$$
\begin{array}{rcl}Q_{k+1}&=&Q_{k}+\alpha\Big[R_{k}-Q_{k}\Big]\\&=&{\alpha}R_{k}+(1-\alpha)Q_{k}\\&=&{\alpha}R_{k}+(1-\alpha)\left[{\alpha}R_{k-1}+(1-\alpha)Q_{k-1}\right]\\&=&{\alpha}R_{k}+(1-\alpha)\alpha R_{k-1}+(1-\alpha)^{2}Q_{k-1}\\&=&{\alpha}R_{k}+(1-\alpha)\alpha R_{k-1}+(1-\alpha)^{2}\alpha R_{k-2}+\\&\quad&\cdots+(1-\alpha)^{k-1}\alpha R_{1}+(1-\alpha)^{k}Q_{1}\\&=&(1-\alpha)^{k}Q_{1}+\displaystyle\sum_{i=1}^{k}\alpha(1-\alpha)^{k-i}R_{i}.\end{array}   \tag*{(2.6)}
$$

We call this a weighted average because the sum of the weights is  $(1-\alpha)^{k}+\sum_{i=1}^{k}\alpha(1-\alpha)^{k-i}=1$, as you can check yourself. Note that the weight,  $\alpha(1-\alpha)^{k-i}$, given to the reward  $R_{i}$ depends on how many rewards ago, k-i, it was

---

## 2.5. OPTIMISTIC INITIAL VALUES

observed. The quantity  $1 - \alpha$ is less than 1, and thus the weight given to  $R_i$ decreases as the number of intervening rewards increases. In fact, the weight decays exponentially according to the exponent on  $1 - \alpha$. (If  $1 - \alpha = 0$, then all the weight goes on the very last reward,  $R_k$, because of the convention that  $0^0 = 1$.) Accordingly, this is sometimes called an exponential, recency-weighted average.

Sometimes it is convenient to vary the step-size parameter from step to step. Let  $\alpha_k(a)$ denote the step-size parameter used to process the reward received after the  $k$th selection of action  $a$. As we have noted, the choice  $\alpha_k(a) = \frac{1}{k}$ results in the sample-average method, which is guaranteed to converge to the true action values by the law of large numbers. But of course convergence is not guaranteed for all choices of the sequence  $\{\alpha_k(a)\}$. A well-known result in stochastic approximation theory gives us the conditions required to assure convergence with probability 1:

$$
\sum_{k=1}^{\infty}\alpha_{k}(a)=\infty\qquad and\qquad\sum_{k=1}^{\infty}\alpha_{k}^{2}(a)<\infty.   \tag*{(2.7)}
$$

The first condition is required to guarantee that the steps are large enough to eventually overcome any initial conditions or random fluctuations. The second condition guarantees that eventually the steps become small enough to assure convergence.

Note that both convergence conditions are met for the sample-average case,  $\alpha_k(a) = \frac{1}{k}$, but not for the case of constant step-size parameter,  $\alpha_k(a) = \alpha$. In the latter case, the second condition is not met, indicating that the estimates never completely converge but continue to vary in response to the most recently received rewards. As we mentioned above, this is actually desirable in a nonstationary environment, and problems that are effectively nonstationary are the norm in reinforcement learning. In addition, sequences of step-size parameters that meet the conditions (2.7) often converge very slowly or need considerable tuning in order to obtain a satisfactory convergence rate. Although sequences of step-size parameters that meet these convergence conditions are often used in theoretical work, they are seldom used in applications and empirical research.

## 2.5 Optimistic Initial Values

All the methods we have discussed so far are dependent to some extent on the initial action-value estimates,  $Q_{1}(a)$. In the language of statistics, these methods are biased by their initial estimates. For the sample-average methods,

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_277_212_936_508.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">Figure 2.2: The effect of optimistic initial action-value estimates on the 10-armed testbed. Both methods used a constant step-size parameter,  $\alpha = 0.1$.</div>

the bias disappears once all actions have been selected at least once, but for methods with constant  $\alpha$, the bias is permanent, though decreasing over time as given by (2.6). In practice, this kind of bias is usually not a problem, and can sometimes be very helpful. The downside is that the initial estimates become, in effect, a set of parameters that must be picked by the user, if only to set them all to zero. The upside is that they provide an easy way to supply some prior knowledge about what level of rewards can be expected.

Initial action values can also be used as a simple way of encouraging exploration. Suppose that instead of setting the initial action values to zero, as we did in the 10-armed testbed, we set them all to +5. Recall that the  $q(a)$ in this problem are selected from a normal distribution with mean 0 and variance 1. An initial estimate of +5 is thus wildly optimistic. But this optimism encourages action-value methods to explore. Whichever actions are initially selected, the reward is less than the starting estimates; the learner switches to other actions, being “disappointed” with the rewards it is receiving. The result is that all actions are tried several times before the value estimates converge. The system does a fair amount of exploration even if greedy actions are selected all the time.

Figure 2.2 shows the performance on the 10-armed bandit testbed of a greedy method using  $Q_{1}(a)=+5$, for all a. For comparison, also shown is an  $\varepsilon$-greedy method with  $Q_{1}(a)=0$. Initially, the optimistic method performs worse because it explores more, but eventually it performs better because its exploration decreases with time. We call this technique for encouraging exploration optimistic initial values. We regard it as a simple trick that can be quite effective on stationary problems, but it is far from being a generally useful approach to encouraging exploration. For example, it is not well suited to

---

nonstationary problems because its drive for exploration is inherently temporary. If the task changes, creating a renewed need for exploration, this method cannot help. Indeed, any method that focuses on the initial state in any special way is unlikely to help with the general nonstationary case. The beginning of time occurs only once, and thus we should not focus on it too much. This criticism applies as well to the sample-average methods, which also treat the beginning of time as a special event, averaging all subsequent rewards with equal weights. Nevertheless, all of these methods are very simple, and one of them or some simple combination of them is often adequate in practice. In the rest of this book we make frequent use of several of these simple exploration techniques.

## 2.6 Upper-Confidence-Bound Action Selection

Exploration is needed because the estimates of the action values are uncertain. The greedy actions are those that look best at present, but some of the other actions may actually be better.  $\varepsilon$-greedy action selection forces the non-greedy actions to be tried, but indiscriminately, with no preference for those that are nearly greedy or particularly uncertain. It would be better to select among the non-greedy actions according to their potential for actually being optimal, taking into account both how close their estimates are to being maximal and the uncertainties in those estimates. One effective way of doing this is to select actions as

$$
A_{t}=\underset{a}{\arg\max}\left[Q_{t}(a)+c\sqrt{\frac{\ln t}{N_{t}(a)}}\right],   \tag*{(2.8)}
$$

where  $\ln t$ denotes the natural logarithm of  $t$ (the number that  $e \approx 2.71828$ would have to be raised to in order to equal  $t$), and the number  $c > 0$ controls the degree of exploration. If  $N_t(a) = 0$, then  $a$ is considered to be a maximizing action.

The idea of this upper confidence bound (UCB) action selection is that the square-root term is a measure of the uncertainty or variance in the estimate of a's value. The quantity being max'ed over is thus a sort of upper bound on the possible true value of action a, with the c parameter determining the confidence level. Each time a is selected the uncertainty is presumably reduced;  $N_t(a)$ is incremented and, as it appears in the denominator of the uncertainty term, the term is decreased. On the other hand, each time an action other a is selected t is increased; as it appears in the numerator the uncertainty estimate is increased. The use of the natural logarithm means that the increase gets smaller over time, but is unbounded; all actions will eventually be selected, but

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_216_211_1009_582.jpg" alt="Image" width="64%" /></div>

<div style="text-align: center;">Figure 2.3: Average performance of UCB action selection on the 10-armed testbed. As shown, UCB generally performs better than  $\varepsilon$-greedy action selection, except in the first n plays, when it selects randomly among the as-yet-unplayed actions. UCB with c = 1 would perform even better but would not show the prominent spike in performance on the 11th play. Can you think of an explanation of this spike?</div>

as time goes by it will be a longer wait, and thus a lower selection frequency, for actions with a lower value estimate or that have already been selected more times.

Results with UCB on the 10-armed testbed are shown in Figure 2.3. UCB will often perform well, as shown here, but is more difficult than  $\varepsilon$-greedy to extend beyond bandits to the more general reinforcement learning settings considered in the rest of this book. One difficulty is in dealing with nonstationary problems; something more complex than the methods presented in Section 2.4 would be needed. Another difficulty is dealing with large state spaces, particularly function approximation as developed in Part III of this book. In these more advanced settings there is currently no known practical way of utilizing the idea of UCB action selection.

## 2.7 Gradient Bandits

So far in this chapter we have considered methods that estimate action values and use those estimates to select actions. This is often a good approach, but it is not the only one possible. In this section we consider learning a numerical preference  $H_{t}(a)$ for each action a. The larger the preference, the

---

more often that action is taken, but the preference has no interpretation in terms of reward. Only the relative preference of one action over another is important; if we add 1000 to all the preferences there is no affect on the action probabilities, which are determined according to a soft-max distribution (i.e., Gibbs or Boltzmann distribution) as follows:

$$
\Pr\{A_{t}=a\}=\frac{e^{H_{t}(a))}}{\sum_{b=1}^{n}e^{H_{t}(b)}}=\pi_{t}(a),   \tag*{(2.9)}
$$

where here we have also introduced a useful new notation  $\pi_t(a)$ for the probability of taking action  $a$ at time  $t$. Initially all preferences are the same (e.g.,  $H_1(a) = 0, \forall a$) so that all actions have an equal probability of being selected.

There is a natural learning algorithm for this setting based on the idea of stochastic gradient ascent. On each step, after selecting the action  $A_{t}$ and receiving the reward  $R_{t}$, the preferences are updated by:

$$
\begin{align*}H_{t+1}(A_{t})&=H_{t}(A_{t})+\alpha\big(R_{t}-\bar{R}_{t}\big)\big(1-\pi_{t}(A_{t})\big),\quad&and\\H_{t+1}(a)&=H_{t}(a)-\alpha\big(R_{t}-\bar{R}_{t}\big)\pi_{t}(a),\quad&\forall a\neq A_{t},\end{align*}   \tag*{(2.10)}
$$

where  $\alpha > 0$ is a step-size parameter, and  $R_t \in \mathbb{R}$ is the average of all the rewards up through and including time  $t$, which can be computed incrementally as described in Section 2.3 (or Section 2.4 if the problem is nonstationary). The  $\bar{R}_t$ term serves as a baseline with which the reward is compared. If the reward is higher than the baseline, then the probability of taking  $A_t$ in the future is increased, and if the reward is below baseline, then probability is decreased. The non-selected actions move in the opposite direction.

Figure 2.4 shows results with the gradient-bandit algorithm on a variant of the 10-armed testbed in which the true expected rewards were selected according to a normal distribution with a mean of +4 instead of zero (and with unit variance as before). This shifting up of all the rewards has absolutely no affect on the gradient-bandit algorithm because of the reward baseline term, which instantaneously adapts to the new level. But if the baseline were omitted (that is, if  $\hat{R}_{t}$ was taken to be constant zero in (2.10)), then performance would be significantly degraded, as shown in the figure.

One can gain a deeper insight into this algorithm by understanding it as a stochastic approximation to gradient ascent. In exact gradient ascent, each preference  $H_{t}(a)$ would be incrementing proportional to the increment's effect on performance:

$$
H_{t+1}(a)=H_{t}(a)+\alpha\frac{\partial\mathbb{E}\left[R_{t}\right]}{\partial H_{t}(a)},   \tag*{(2.11)}
$$

where the measure of performance here is the expected reward:

 
$$
\mathbb{E}[R_{t}]=\sum_{b}\pi_{t}(b)q(b).
$$
 

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_214_219_981_649.jpg" alt="Image" width="62%" /></div>

<div style="text-align: center;">Figure 2.4: Average performance of the gradient-bandit algorithm with and without a reward baseline on the 10-armed testbed with  $\mathbb{E}[q(a)] = 4$.</div>

Of course, it is not possible to implement gradient ascent exactly in our case because by assumption we do not know the  $q(b)$, but in fact the updates of our algorithm (2.10) are equal to (2.11) in expected value, making the algorithm an instance of stochastic gradient ascent.

The calculations showing this require only beginning calculus, but take several steps. If you are mathematically inclined, then you will enjoy the rest of this section in which we go through these steps. First we take a closer look at the exact performance gradient:

 
$$
\begin{align*}\frac{\partial\mathbb{E}[R_{t}]}{\partial H_{t}(a)}&=\frac{\partial}{\partial H_{t}(a)}\left[\sum_{b}\pi_{t}(b)q(b)\right]\\&=\sum_{b}q(b)\frac{\partial\pi_{t}(b)}{\partial H_{t}(a)}\\&=\sum_{b}\left(q(b)-X_{t}\right)\frac{\partial\pi_{t}(b)}{\partial H_{t}(a)},\end{align*}
$$
 

where  $X_t$ can be any scalar that does not depend on  $b$. We can include it here because the gradient sums to zero over the all the actions,  $\sum_b \frac{\partial \pi_t(b)}{\partial H_t(a)} = 0$. As  $H_t(a)$ is changed, some actions' probabilities go up and some down, but the sum of the changes must be zero because the sum of the probabilities must

---

## 2.7. GRADIENT BANDITS

remain one.

 
$$
=\sum_{b}\pi_{t}(b)\big(q(b)-X_{t}\big)\frac{\partial\pi_{t}(b)}{\partial H_{t}(a)}/\pi_{t}(b)
$$
 

The equation is now in the form of an expectation, summing over all possible values b of the random variable  $A_{t}$, then multiplying by the probability of taking those values. Thus:

 
$$
\begin{aligned}&=\mathbb{E}\left[\left(q(A_{t})-X_{t}\right)\frac{\partial\pi_{t}(A_{t})}{\partial H_{t}(a)}/\pi_{t}(A_{t})\right]\\&=\mathbb{E}\left[\left(R_{t}-\bar{R}_{t}\right)\frac{\partial\pi_{t}(A_{t})}{\partial H_{t}(a)}/\pi_{t}(A_{t})\right],\end{aligned}
$$
 

where here we have chosen  $X_t = \bar{R}_t$ and substituted  $R_t$ for  $q(A_t)$, which is permitted because  $\mathbb{E}[R_t] = q(A_t)$ and because all the other factors are non-random. Shortly we will establish that  $\frac{\partial \pi_t(b)}{\partial H_t(a)} = \pi_t(b) \left( \mathbb{I}_{a=b} - \pi_t(a) \right)$, where  $\mathbb{I}_{a=b}$ is defined to be 1 if  $a = b$, else 0. Assuming that for now we have

 
$$
\begin{aligned}&=\mathbb{E}\big[\big(R_{t}-\bar{R}_{t}\big)\pi_{t}(A_{t})\big(\mathbb{I}_{a=A_{t}}-\pi_{t}(a)\big)/\pi_{t}(A_{t})\big]\\&=\mathbb{E}\big[\big(R_{t}-\bar{R}_{t}\big)\big(\mathbb{I}_{a=A_{t}}-\pi_{t}(a)\big)\big].\\ \end{aligned}
$$
 

Recall that our plan has been to write the performance gradient as an expectation of something that we can sample on each step, as we have just done, and then update on each step proportional to the sample. Substituting a sample of the expectation above for the performance gradient in  $(2.11)$ yields:

 
$$
H_{t+1}(a)=H_{t}(a)+\alpha\big(R_{t}-\bar{R}_{t}\big)\big(\mathbb{I}_{a=A_{t}}-\pi_{t}(a)\big),\qquad\forall a,
$$
 

which you will recognize as being equivalent to our original algorithm (2.10).

Thus it remains only to show that  $\frac{\partial\pi_{t}(b)}{\partial H_{t}(a)} = \pi_{t}(b)\big(\mathbb{I}_{a=b} - \pi_{t}(a)\big)$, as we assumed earlier. Recall the standard quotient rule for derivatives:

 
$$
\frac{\partial}{\partial x}\left[\frac{f(x)}{g(x)}\right]=\frac{\frac{\partial f(x)}{\partial x}g(x)-f(x)\frac{\partial g(x)}{\partial x}}{g(x)^{2}}.
$$
 

---

Using this, we can write

 
$$
\begin{aligned}\frac{\partial\pi_{t}(b)}{\partial H_{t}(a)}&=\frac{\partial}{\partial H_{t}(a)}\pi_{t}(b)\\&=\frac{\partial}{\partial H_{t}(a)}\left[\frac{e^{H_{t}(b)}}{\sum_{c=1}^{n}e^{H_{t}(c)}}\right]\\&=\frac{\frac{\partial e^{H_{t}(b)}}{\partial H_{t}(a)}\sum_{c=1}^{n}e^{H_{t}(c)}-e^{H_{t}(b)}\frac{\partial\sum_{c=1}^{n}e^{H_{t}(c)}}{\partial H_{t}(a)}}{(\sum_{c=1}^{n}e^{H_{t}(c)})^{2}}\quad(by the quotient rule)\\&=\frac{\mathbb{I}_{a=b}e^{H_{t}(a)}\sum_{c=1}^{n}e^{H_{t}(c)}-e^{H_{t}(b)}e^{H_{t}(a)}}{(\sum_{c=1}^{n}e^{H_{t}(c)})^{2}}\quad(because\frac{\partial e^{x}}{\partial x}=e^{x})\\&=\frac{\mathbb{I}_{a=b}e^{H_{t}(b)}}{\sum_{c=1}^{n}e^{H_{t}(c)}}-\frac{e^{H_{t}(b)}e^{H_{t}(a)}}{(\sum_{c=1}^{n}e^{H_{t}(c)})^{2}}\\&=\mathbb{I}_{a=b}\pi_{t}(b)-\pi_{t}(b)\pi_{t}(a)\\&=\pi_{t}(b)\big(\mathbb{I}_{a=b}-\pi_{t}(a)\big).Q.E.D.\end{aligned}
$$
 

We have just shown that the expected update of the gradient-bandit algorithm is equal to the gradient of expected reward, and thus that the algorithm is an instance of stochastic gradient ascent. This assures us that the algorithm has robust convergence properties.

Note that we did not require anything of the reward baseline other than that it not depend on the selected action. For example, we could have set is to zero, or to 1000, and the algorithm would still have been an instance of stochastic gradient ascent. The choice of the baseline does not affect the expected update of the algorithm, but it does affect the variance of the update and thus the rate of convergence (as shown, e.g., in Figure 2.4). Choosing it as the average of the rewards may not be the very best, but it is simple and works well in practice.

## 2.8 Associative Search (Contextual Bandits)

So far in this chapter we have considered only nonassociative tasks, in which there is no need to associate different actions with different situations. In these tasks the learner either tries to find a single best action when the task is stationary, or tries to track the best action as it changes over time when the task is nonstationary. However, in a general reinforcement learning task there is more than one situation, and the goal is to learn a policy: a mapping from situations to the actions that are best in those situations. To set the stage for

---

the full problem, we briefly discuss the simplest way in which nonassociative tasks extend to the associative setting.

As an example, suppose there are several different n-armed bandit tasks, and that on each play you confront one of these chosen at random. Thus, the bandit task changes randomly from play to play. This would appear to you as a single, nonstationary n-armed bandit task whose true action values change randomly from play to play. You could try using one of the methods described in this chapter that can handle nonstationarity, but unless the true action values change slowly, these methods will not work very well. Now suppose, however, that when a bandit task is selected for you, you are given some distinctive clue about its identity (but not its action values). Maybe you are facing an actual slot machine that changes the color of its display as it changes its action values. Now you can learn a policy associating each task, signaled by the color you see, with the best action to take when facing that task—for instance, if red, play arm 1; if green, play arm 2. With the right policy you can usually do much better than you could in the absence of any information distinguishing one bandit task from another.

This is an example of an associative search task, so called because it involves both trial-and-error learning in the form of search for the best actions and association of these actions with the situations in which they are best. $^{2}$ Associative search tasks are intermediate between the n-armed bandit problem and the full reinforcement learning problem. They are like the full reinforcement learning problem in that they involve learning a policy, but like our version of the n-armed bandit problem in that each action affects only the immediate reward. If actions are allowed to affect the next situation as well as the reward, then we have the full reinforcement learning problem. We present this problem in the next chapter and consider its ramifications throughout the rest of the book.

## 2.9 Summary

We have presented in this chapter several simple ways of balancing exploration and exploitation. The  $\varepsilon$-greedy methods choose randomly a small fraction of the time, whereas UCB methods choose deterministically but achieve exploration by subtly favoring at each step the actions that have so far received fewer samples. Gradient-bandit algorithms estimate not action values, but action preferences, and favor the more preferred actions in a graded, probabilistic manner using a soft-max distribution. The simple expedient of initializing

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_212_219_1005_626.jpg" alt="Image" width="64%" /></div>

<div style="text-align: center;">Figure 2.5: A parameter study of the various bandit algorithms presented in this chapter. Each point is the average reward obtained over 1000 steps with a particular algorithm at a particular setting of its parameter.</div>

estimates optimistically causes even greedy methods to explore significantly.

It is natural to ask which of these methods is best. Although this is a difficult question to answer in general, we can certainly run them all on the 10-armed testbed that we have used throughout this chapter and compare their performances. A complication is that they all have a parameter; to get a meaningful comparison we will have to consider their performance as a function of their parameter. Our graphs so far have shown the course of learning over time for each algorithm and parameter setting, but it would be too visually confusing to show such a learning curve for each algorithm and parameter value. Instead we summarize a complete learning curve by its average value over the 1000 steps; this value is proportional to the area under the learning curves we have shown up to now. Figure 2.5 shows this measure for the various bandit algorithms from this chapter, each as a function of its own parameter shown on a single scale on the x-axis. Note that the parameter values are varied by factors of two and presented on a log scale. Note also the characteristic inverted-U shapes of each algorithm's performance; all the algorithms perform best at an intermediate value of their parameter, neither too large nor too big. In assessing an method, we should attend not just to how well it does at its best parameter setting, but also to how sensitive it is to its parameter value. All of these algorithms are fairly insensitive, performing well over a range of parameter values varying by about an order of magnitude. Overall, on this problem, UCB seems to perform best.

---

Despite their simplicity, in our opinion the methods presented in this chapter can fairly be considered the state of the art. There are more sophisticated methods, but their complexity and assumptions make them impractical for the full reinforcement learning problem that is our real focus. Starting in Chapter 5 we present learning methods for solving the full reinforcement learning problem that use in part the simple methods explored in this chapter.

Although the simple methods explored in this chapter may be the best we can do at present, they are far from a fully satisfactory solution to the problem of balancing exploration and exploitation.

The classical solution to balancing exploration and exploitation in n-armed bandit problems is to compute special functions called Gittins indices. These provide an optimal solution to a certain kind of bandit problem more general than that considered here but that assumes the prior distribution of possible problems is known. Unfortunately, neither the theory nor the computational tractability of this method appear to generalize to the full reinforcement learning problem that we consider in the rest of the book.

There is also a well-known algorithm for computing the Bayes optimal way to balance exploration and exploitation. This method is computationally intractable when done exactly, but there may be efficient ways to approximate it. In this method we assume that we know the distribution of problem instances, that is, the probability of each possible set of true action values. Given any action selection, we can then compute the probability of each possible immediate reward and the resultant posterior probability distribution over action values. This evolving distribution becomes the information state of the problem. Given a horizon, say 1000 plays, one can consider all possible actions, all possible resulting rewards, all possible next actions, all next rewards, and so on for all 1000 plays. Given the assumptions, the rewards and probabilities of each possible chain of events can be determined, and one need only pick the best. But the tree of possibilities grows extremely rapidly; even if there are only two actions and two rewards, the tree will have  $2^{2000}$ leaves. This approach effectively turns the bandit problem into an instance of the full reinforcement learning problem. In the end, we may be able to use reinforcement learning methods to approximate this optimal solution. But that is a topic for current research and beyond the scope of this book.

#### Bibliographical and Historical Remarks

2.1 Bandit problems have been studied in statistics, engineering, and psychology. In statistics, bandit problems fall under the heading “sequential design of experiments,” introduced by Thompson (1933, 1934) and

---

Robbins (1952), and studied by Bellman (1956). Berry and Fristedt (1985) provide an extensive treatment of bandit problems from the perspective of statistics. Narendra and Thathachar (1989) treat bandit problems from the engineering perspective, providing a good discussion of the various theoretical traditions that have focused on them. In psychology, bandit problems have played roles in statistical learning theory (e.g., Bush and Mosteller, 1955; Estes, 1950).

The term greedy is often used in the heuristic search literature (e.g., Pearl, 1984). The conflict between exploration and exploitation is known in control engineering as the conflict between identification (or estimation) and control (e.g., Witten, 1976). Feldbaum (1965) called it the dual control problem, referring to the need to solve the two problems of identification and control simultaneously when trying to control a system under uncertainty. In discussing aspects of genetic algorithms, Holland (1975) emphasized the importance of this conflict, referring to it as the conflict between the need to exploit and the need for new information.

2.2 Action-value methods for our n-armed bandit problem were first proposed by Thathachar and Sastry (1985). These are often called estimator algorithms in the learning automata literature. The term action value is due to Watkins (1989). The first to use  $\varepsilon$-greedy methods may also have been Watkins (1989, p. 187), but the idea is so simple that some earlier use seems likely.

2.3–4 This material falls under the general heading of stochastic iterative algorithms, which is well covered by Bertsekas and Tsitsiklis (1996).

2.5 Optimistic initialization was used in reinforcement learning by Sutton (1996).

2.6 Early work on using estimates of the upper confidence bound to select actions was done by Lai and Robbins (1985), Kaelbling (1993b), and Agarwal (1995). The UCB algorithm we present here is called UCB1 in the literature and was first developed by Auer, Cesa-Bianchi and Fischer (2002).

2.7 Gradient-bandit algorithms are a special case of the gradient-based reinforcement learning algorithms introduced by Williams (1992), and that later developed into the actor-critic and policy-gradient algorithms that we treat later in this book. Further discussion of the choice of

---

baseline is provided there and by Greensmith, Bartlett, and Baxter (2001, 2004) and Dick (2015).

The term softmax for the action selection rule (2.9) is due to Bridle (1990). This rule appears to have been first proposed by Luce (1959).

2.8 The term associative search and the corresponding problem were introduced by Barto, Sutton, and Brouwer (1981). The term associative reinforcement learning has also been used for associative search (Barto and Anandan, 1985), but we prefer to reserve that term as a synonym for the full reinforcement learning problem (as in Sutton, 1984). (And, as we noted, the modern literature also uses the term “contextual bandits” for this problem.) We note that Thorndike’s Law of Effect (quoted in Chapter 1) describes associative search by referring to the formation of associative links between situations (states) and actions. According to the terminology of operant, or instrumental, conditioning (e.g., Skinner, 1938), a discriminative stimulus is a stimulus that signals the presence of a particular reinforcement contingency. In our terms, different discriminative stimuli correspond to different states.

2.9 The Gittins index approach is due to Gittins and Jones (1974). Duff (1995) showed how it is possible to learn Gittins indices for bandit problems through reinforcement learning. Bellman (1956) was the first to show how dynamic programming could be used to compute the optimal balance between exploration and exploitation within a Bayesian formulation of the problem. The survey by Kumar (1985) provides a good discussion of Bayesian and non-Bayesian approaches to these problems. The term information state comes from the literature on partially observable MDPs; see, e.g., Lovejoy (1991).

#### Exercises

Exercise 2.1 In the comparison shown in Figure 2.1, which method will perform best in the long run in terms of cumulative reward and cumulative probability of selecting the best action? How much better will it be? Express your answer quantitatively.

Exercise 2.2 Give pseudocode for a complete algorithm for the n-armed bandit problem. Use greedy action selection and incremental computation of action values with  $\alpha = \frac{1}{k}$ step-size parameter. Assume a function  $bandit(a)$ that takes an action and returns a reward. Use arrays and variables; do not

---

subscript anything by the time index  $t$ (for examples of this style of pseudocode, see Figures 4.1 and 4.3). Indicate how the action values are initialized and updated after each reward. Indicate how the step-size parameters are set for each action as a function of how many times it has been tried.

Exercise 2.3 If the step-size parameters,  $\alpha_k$, are not constant, then the estimate  $Q_k$ is a weighted average of previously received rewards with a weighting different from that given by (2.6). What is the weighting on each prior reward for the general case, analogous to (2.6), in terms of  $\alpha_k$?

Exercise 2.4 (programming) Design and conduct an experiment to demonstrate the difficulties that sample-average methods have for nonstationary problems. Use a modified version of the 10-armed testbed in which all the  $q(a)$ start out equal and then take independent random walks. Prepare plots like Figure 2.1 for an action-value method using sample averages, incrementally computed by  $\alpha = \frac{1}{k}$, and another action-value method using a constant step-size parameter,  $\alpha = 0.1$. Use  $\varepsilon = 0.1$ and, if necessary, runs longer than 1000 plays.

Exercise 2.5 The results shown in Figure 2.2 should be quite reliable because they are averages over 2000 individual, randomly chosen 10-armed bandit tasks. Why, then, are there oscillations and spikes in the early part of the curve for the optimistic method? What might make this method perform particularly better or worse, on average, on particular early plays?

Exercise 2.6 Suppose you face a binary bandit task whose true action values change randomly from play to play. Specifically, suppose that for any play the true values of actions 1 and 2 are respectively 0.1 and 0.2 with probability 0.5 (case A), and 0.9 and 0.8 with probability 0.5 (case B). If you are not able to tell which case you face at any play, what is the best expectation of success you can achieve and how should you behave to achieve it? Now suppose that on each play you are told if you are facing case A or case B (although you still don't know the true action values). This is an associative search task. What is the best expectation of success you can achieve in this task, and how should you behave to achieve it?

---

# Chapter 3

# Finite Markov Decision Processes

In this chapter we introduce the problem that we try to solve in the rest of the book. For us, this problem defines the field of reinforcement learning: any method that is suited to solving this problem we consider to be a reinforcement learning method.

Our objective in this chapter is to describe the reinforcement learning problem in a broad sense. We try to convey the wide range of possible applications that can be framed as reinforcement learning tasks. We also describe mathematically idealized forms of the reinforcement learning problem for which precise theoretical statements can be made. We introduce key elements of the problem's mathematical structure, such as value functions and Bellman equations. As in all of artificial intelligence, there is a tension between breadth of applicability and mathematical tractability. In this chapter we introduce this tension and discuss some of the trade-offs and challenges that it implies.

## 3.1 The Agent-Environment Interface

The reinforcement learning problem is meant to be a straightforward framing of the problem of learning from interaction to achieve a goal. The learner and decision-maker is called the agent. The thing it interacts with, comprising everything outside the agent, is called the environment. These interact continually, the agent selecting actions and the environment responding to those actions and presenting new situations to the agent. $^{1}$ The environment also

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_320_209_903_413.jpg" alt="Image" width="47%" /></div>

<div style="text-align: center;">Figure 3.1: The agent–environment interaction in reinforcement learning.</div>

gives rise to rewards, special numerical values that the agent tries to maximize over time. A complete specification of an environment defines a task, one instance of the reinforcement learning problem.

More specifically, the agent and environment interact at each of a sequence of discrete time steps,  $t = 0, 1, 2, 3, \ldots^{2}$. At each time step  $t$, the agent receives some representation of the environment's state,  $S_{t} \in \mathcal{S}$, where  $\mathcal{S}$ is the set of possible states, and on that basis selects an action,  $A_{t} \in \mathcal{A}(S_{t})$, where  $\mathcal{A}(S_{t})$ is the set of actions available in state  $S_{t}$. One time step later, in part as a consequence of its action, the agent receives a numerical reward,  $R_{t+1} \in \mathcal{R} \subset \mathbb{R}$, and finds itself in a new state,  $S_{t+1}.^{3}$ Figure 3.1 diagrams the agent-environment interaction.

At each time step, the agent implements a mapping from states to probabilities of selecting each possible action. This mapping is called the agent's policy and is denoted  $\pi_t$, where  $\pi_t(a|s)$ is the probability that  $A_t = a$ if  $S_t = s$. Reinforcement learning methods specify how the agent changes its policy as a result of its experience. The agent's goal, roughly speaking, is to maximize the total amount of reward it receives over the long run.

This framework is abstract and flexible and can be applied to many different problems in many different ways. For example, the time steps need not refer to fixed intervals of real time; they can refer to arbitrary successive stages of decision-making and acting. The actions can be low-level controls, such as the voltages applied to the motors of a robot arm, or high-level decisions, such as whether or not to have lunch or to go to graduate school. Similarly, the states can take a wide variety of forms. They can be completely determined by low-level sensations, such as direct sensor readings, or they can be more

---

high-level and abstract, such as symbolic descriptions of objects in a room. Some of what makes up a state could be based on memory of past sensations or even be entirely mental or subjective. For example, an agent could be in the state of not being sure where an object is, or of having just been surprised in some clearly defined sense. Similarly, some actions might be totally mental or computational. For example, some actions might control what an agent chooses to think about, or where it focuses its attention. In general, actions can be any decisions we want to learn how to make, and the states can be anything we can know that might be useful in making them.

In particular, the boundary between agent and environment is not often the same as the physical boundary of a robot's or animal's body. Usually, the boundary is drawn closer to the agent than that. For example, the motors and mechanical linkages of a robot and its sensing hardware should usually be considered parts of the environment rather than parts of the agent. Similarly, if we apply the framework to a person or animal, the muscles, skeleton, and sensory organs should be considered part of the environment. Rewards, too, presumably are computed inside the physical bodies of natural and artificial learning systems, but are considered external to the agent.

The general rule we follow is that anything that cannot be changed arbitrarily by the agent is considered to be outside of it and thus part of its environment. We do not assume that everything in the environment is unknown to the agent. For example, the agent often knows quite a bit about how its rewards are computed as a function of its actions and the states in which they are taken. But we always consider the reward computation to be external to the agent because it defines the task facing the agent and thus must be beyond its ability to change arbitrarily. In fact, in some cases the agent may know everything about how its environment works and still face a difficult reinforcement learning task, just as we may know exactly how a puzzle like Rubik's cube works, but still be unable to solve it. The agent-environment boundary represents the limit of the agent's absolute control, not of its knowledge.

The agent–environment boundary can be located at different places for different purposes. In a complicated robot, many different agents may be operating at once, each with its own boundary. For example, one agent may make high-level decisions which form part of the states faced by a lower-level agent that implements the high-level decisions. In practice, the agent–environment boundary is determined once one has selected particular states, actions, and rewards, and thus has identified a specific decision-making task of interest.

The reinforcement learning framework is a considerable abstraction of the problem of goal-directed learning from interaction. It proposes that whatever

---

the details of the sensory, memory, and control apparatus, and whatever objective one is trying to achieve, any problem of learning goal-directed behavior can be reduced to three signals passing back and forth between an agent and its environment: one signal to represent the choices made by the agent (the actions), one signal to represent the basis on which the choices are made (the states), and one signal to define the agent's goal (the rewards). This framework may not be sufficient to represent all decision-learning problems usefully, but it has proved to be widely useful and applicable.

Of course, the particular states and actions vary greatly from task to task, and how they are represented can strongly affect performance. In reinforcement learning, as in other kinds of learning, such representational choices are at present more art than science. In this book we offer some advice and examples regarding good ways of representing states and actions, but our primary focus is on general principles for learning how to behave once the representations have been selected.

Example 3.1: Bioreactor Suppose reinforcement learning is being applied to determine moment-by-moment temperatures and stirring rates for a bioreactor (a large vat of nutrients and bacteria used to produce useful chemicals). The actions in such an application might be target temperatures and target stirring rates that are passed to lower-level control systems that, in turn, directly activate heating elements and motors to attain the targets. The states are likely to be thermocouple and other sensory readings, perhaps filtered and delayed, plus symbolic inputs representing the ingredients in the vat and the target chemical. The rewards might be moment-by-moment measures of the rate at which the useful chemical is produced by the bioreactor. Notice that here each state is a list, or vector, of sensor readings and symbolic inputs, and each action is a vector consisting of a target temperature and a stirring rate. It is typical of reinforcement learning tasks to have states and actions with such structured representations. Rewards, on the other hand, are always single numbers.

Example 3.2: Pick-and-Place Robot Consider using reinforcement learning to control the motion of a robot arm in a repetitive pick-and-place task. If we want to learn movements that are fast and smooth, the learning agent will have to control the motors directly and have low-latency information about the current positions and velocities of the mechanical linkages. The actions in this case might be the voltages applied to each motor at each joint, and the states might be the latest readings of joint angles and velocities. The reward might be +1 for each object successfully picked up and placed. To encourage smooth movements, on each time step a small, negative reward can be given as a function of the moment-to-moment “jerkiness” of the motion.

---

Example 3.3: Recycling Robot A mobile robot has the job of collecting empty soda cans in an office environment. It has sensors for detecting cans, and an arm and gripper that can pick them up and place them in an onboard bin; it runs on a rechargeable battery. The robot's control system has components for interpreting sensory information, for navigating, and for controlling the arm and gripper. High-level decisions about how to search for cans are made by a reinforcement learning agent based on the current charge level of the battery. This agent has to decide whether the robot should (1) actively search for a can for a certain period of time, (2) remain stationary and wait for someone to bring it a can, or (3) head back to its home base to recharge its battery. This decision has to be made either periodically or whenever certain events occur, such as finding an empty can. The agent therefore has three actions, and its state is determined by the state of the battery. The rewards might be zero most of the time, but then become positive when the robot secures an empty can, or large and negative if the battery runs all the way down. In this example, the reinforcement learning agent is not the entire robot. The states it monitors describe conditions within the robot itself, not conditions of the robot's external environment. The agent's environment therefore includes the rest of the robot, which might contain other complex decision-making systems, as well as the robot's external environment.

## 3.2 Goals and Rewards

In reinforcement learning, the purpose or goal of the agent is formalized in terms of a special reward signal passing from the environment to the agent. At each time step, the reward is a simple number,  $R_t \in \mathbb{R}$. Informally, the agent's goal is to maximize the total amount of reward it receives. This means maximizing not immediate reward, but cumulative reward in the long run. We can clearly state this informal idea as the reward hypothesis:

That all of what we mean by goals and purposes can be well thought of as the maximization of the expected value of the cumulative sum of a received scalar signal (called reward).

The use of a reward signal to formalize the idea of a goal is one of the most distinctive features of reinforcement learning.

Although formulating goals in terms of reward signals might at first appear limiting, in practice it has proved to be flexible and widely applicable. The best way to see this is to consider examples of how it has been, or could be, used. For example, to make a robot learn to walk, researchers have provided reward

---

on each time step proportional to the robot's forward motion. In making a robot learn how to escape from a maze, the reward is often -1 for every time step that passes prior to escape; this encourages the agent to escape as quickly as possible. To make a robot learn to find and collect empty soda cans for recycling, one might give it a reward of zero most of the time, and then a reward of +1 for each can collected. One might also want to give the robot negative rewards when it bumps into things or when somebody yells at it. For an agent to learn to play checkers or chess, the natural rewards are +1 for winning, -1 for losing, and 0 for drawing and for all nonterminal positions.

You can see what is happening in all of these examples. The agent always learns to maximize its reward. If we want it to do something for us, we must provide rewards to it in such a way that in maximizing them the agent will also achieve our goals. It is thus critical that the rewards we set up truly indicate what we want accomplished. In particular, the reward signal is not the place to impart to the agent prior knowledge about how to achieve what we want it to do. $^{4}$ For example, a chess-playing agent should be rewarded only for actually winning, not for achieving subgoals such taking its opponent's pieces or gaining control of the center of the board. If achieving these sorts of subgoals were rewarded, then the agent might find a way to achieve them without achieving the real goal. For example, it might find a way to take the opponent's pieces even at the cost of losing the game. The reward signal is your way of communicating to the robot what you want it to achieve, not how you want it achieved.

Newcomers to reinforcement learning are sometimes surprised that the rewards—which define of the goal of learning—are computed in the environment rather than in the agent. Certainly most ultimate goals for animals are recognized by computations occurring inside their bodies, for example, by sensors for recognizing food, hunger, pain, and pleasure. Nevertheless, as we discussed in the previous section, one can redraw the agent–environment interface in such a way that these parts of the body are considered to be outside of the agent (and thus part of the agent's environment). For example, if the goal concerns a robot's internal energy reservoirs, then these are considered to be part of the environment; if the goal concerns the positions of the robot's limbs, then these too are considered to be part of the environment—that is, the agent's boundary is drawn at the interface between the limbs and their control systems. These things are considered internal to the robot but external to the learning agent. For our purposes, it is convenient to place the boundary of the learning agent not at the limit of its physical body, but at the limit of

---

its control.

The reason we do this is that the agent’s ultimate goal should be something over which it has imperfect control: it should not be able, for example, to simply decree that the reward has been received in the same way that it might arbitrarily change its actions. Therefore, we place the reward source outside of the agent. This does not preclude the agent from defining for itself a kind of internal reward, or a sequence of internal rewards. Indeed, this is exactly what many reinforcement learning methods do.

## 3.3 Returns

So far we have discussed the objective of learning informally. We have said that the agent's goal is to maximize the cumulative reward it receives in the long run. How might this be defined formally? If the sequence of rewards received after time step t is denoted  $R_{t+1}$,  $R_{t+2}$,  $R_{t+3}$, ..., then what precise aspect of this sequence do we wish to maximize? In general, we seek to maximize the expected return, where the return  $G_t$ is defined as some specific function of the reward sequence. In the simplest case the return is the sum of the rewards:

$$
G_{t}=R_{t+1}+R_{t+2}+R_{t+3}+\cdots+R_{T},   \tag*{(3.1)}
$$

where T is a final time step. This approach makes sense in applications in which there is a natural notion of final time step, that is, when the agent-environment interaction breaks naturally into subsequences, which we call episodes, $^{5}$ such as plays of a game, trips through a maze, or any sort of repeated interactions. Each episode ends in a special state called the terminal state, followed by a reset to a standard starting state or to a sample from a standard distribution of starting states. Tasks with episodes of this kind are called episodic tasks. In episodic tasks we sometimes need to distinguish the set of all nonterminal states, denoted S, from the set of all states plus the terminal state, denoted  $S^{+}$.

On the other hand, in many cases the agent–environment interaction does not break naturally into identifiable episodes, but goes on continually without limit. For example, this would be the natural way to formulate a continual process-control task, or an application to a robot with a long life span. We call these continuing tasks. The return formulation (3.1) is problematic for continuing tasks because the final time step would be  $T = \infty$, and the return, which is what we are trying to maximize, could itself easily be infinite. (For example, suppose the agent receives a reward of +1 at each time step.) Thus,

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_405_204_818_419.jpg" alt="Image" width="33%" /></div>

<div style="text-align: center;">Figure 3.2: The pole-balancing task.</div>

in this book we usually use a definition of return that is slightly more complex conceptually but much simpler mathematically.

The additional concept that we need is that of discounting. According to this approach, the agent tries to select actions so that the sum of the discounted rewards it receives over the future is maximized. In particular, it chooses  $A_{t}$ to maximize the expected discounted return:

$$
G_{t}=R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\cdots=\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1},   \tag*{(3.2)}
$$

where  $\gamma$ is a parameter,  $0 \leq \gamma \leq 1$, called the discount rate.

The discount rate determines the present value of future rewards: a reward received  $k$ time steps in the future is worth only  $\gamma^{k-1}$ times what it would be worth if it were received immediately. If  $\gamma < 1$, the infinite sum has a finite value as long as the reward sequence  $\{R_k\}$ is bounded. If  $\gamma = 0$, the agent is “myopic” in being concerned only with maximizing immediate rewards: its objective in this case is to learn how to choose  $A_t$ so as to maximize only  $R_{t+1}$. If each of the agent’s actions happened to influence only the immediate reward, not future rewards as well, then a myopic agent could maximize (3.2) by separately maximizing each immediate reward. But in general, acting to maximize immediate reward can reduce access to future rewards so that the return may actually be reduced. As  $\gamma$ approaches 1, the objective takes future rewards into account more strongly: the agent becomes more farsighted.

Example 3.4: Pole-Balancing Figure 3.2 shows a task that served as an early illustration of reinforcement learning. The objective here is to apply forces to a cart moving along a track so as to keep a pole hinged to the cart from falling over. A failure is said to occur if the pole falls past a given angle from vertical or if the cart runs off the track. The pole is reset to vertical after each failure. This task could be treated as episodic, where the natural episodes are the repeated attempts to balance the pole. The reward in this

---

## 3.4. UNIFIED NOTATION FOR EPISODIC AND CONTINUING TASKS61

case could be +1 for every time step on which failure did not occur, so that the return at each time would be the number of steps until failure. Alternatively, we could treat pole-balancing as a continuing task, using discounting. In this case the reward would be -1 on each failure and zero at all other times. The return at each time would then be related to  $-\gamma^{K}$, where K is the number of time steps before failure. In either case, the return is maximized by keeping the pole balanced for as long as possible.

## 3.4 Unified Notation for Episodic and Continuing Tasks

In the preceding section we described two kinds of reinforcement learning tasks, one in which the agent–environment interaction naturally breaks down into a sequence of separate episodes (episodic tasks), and one in which it does not (continuing tasks). The former case is mathematically easier because each action affects only the finite number of rewards subsequently received during the episode. In this book we consider sometimes one kind of problem and sometimes the other, but often both. It is therefore useful to establish one notation that enables us to talk precisely about both cases simultaneously.

To be precise about episodic tasks requires some additional notation. Rather than one long sequence of time steps, we need to consider a series of episodes, each of which consists of a finite sequence of time steps. We number the time steps of each episode starting anew from zero. Therefore, we have to refer not just to $S_{t}$, the state representation at time $t$, but to $S_{t,i}$, the state representation at time $t$of episode$i$(and similarly for$A_{t,i}$, $R_{t,i}$, $\pi_{t,i}$, $T_{i}$, etc.). However, it turns out that, when we discuss episodic tasks we will almost never have to distinguish between different episodes. We will almost always be considering a particular single episode, or stating something that is true for all episodes. Accordingly, in practice we will almost always abuse notation slightly by dropping the explicit reference to episode number. That is, we will write $S_{t}$to refer to$S_{t,i}$, and so on.

We need one other convention to obtain a single notation that covers both episodic and continuing tasks. We have defined the return as a sum over a finite number of terms in one case (3.1) and as a sum over an infinite number of terms in the other (3.2). These can be unified by considering episode termination to be the entering of a special absorbing state that transitions only to itself and that generates only rewards of zero. For example, consider the state transition

---

diagram

<div style="text-align: center;"><img src="imgs/img_in_image_box_247_272_959_384.jpg" alt="Image" width="58%" /></div>

Here the solid square represents the special absorbing state corresponding to the end of an episode. Starting from  $S_0$, we get the reward sequence  $+1,+1,+1,0,0,0,\ldots$ Summing these, we get the same return whether we sum over the first T rewards (here T = 3) or over the full infinite sequence. This remains true even if we introduce discounting. Thus, we can define the return, in general, according to (3.2), using the convention of omitting episode numbers when they are not needed, and including the possibility that  $\gamma = 1$ if the sum remains defined (e.g., because all episodes terminate). Alternatively, we can also write the return as

$$
G_{t}=\sum_{k=0}^{T-t-1}\gamma^{k}R_{t+k+1},   \tag*{(3.3)}
$$

including the possibility that  $T = \infty$ or  $\gamma = 1$ (but not both $^{6}$). We use these conventions throughout the rest of the book to simplify notation and to express the close parallels between episodic and continuing tasks.

####  $^{*}$3.5 The Markov Property

In the reinforcement learning framework, the agent makes its decisions as a function of a signal from the environment called the environment's state. In this section we discuss what is required of the state signal, and what kind of information we should and should not expect it to provide. In particular, we formally define a property of environments and their state signals that is of particular interest, called the Markov property.

In this book, by “the state” we mean whatever information is available to the agent. We assume that the state is given by some preprocessing system that is nominally part of the environment. We do not address the issues of constructing, changing, or learning the state signal in this book. We take this approach not because we consider state representation to be unimportant, but

---

in order to focus fully on the decision-making issues. In other words, our main concern is not with designing the state signal, but with deciding what action to take as a function of whatever state signal is available.

Certainly the state signal should include immediate sensations such as sensory measurements, but it can contain much more than that. State representations can be highly processed versions of original sensations, or they can be complex structures built up over time from the sequence of sensations. For example, we can move our eyes over a scene, with only a tiny spot corresponding to the fovea visible in detail at any one time, yet build up a rich and detailed representation of a scene. Or, more obviously, we can look at an object, then look away, and know that it is still there. We can hear the word "yes" and consider ourselves to be in totally different states depending on the question that came before and which is no longer audible. At a more mundane level, a control system can measure position at two different times to produce a state representation including information about velocity. In all of these cases the state is constructed and maintained on the basis of immediate sensations together with the previous state or some other memory of past sensations. In this book, we do not explore how that is done, but certainly it can be and has been done. There is no reason to restrict the state representation to immediate sensations; in typical applications we should expect the state representation to be able to inform the agent of more than that.

On the other hand, the state signal should not be expected to inform the agent of everything about the environment, or even everything that would be useful to it in making decisions. If the agent is playing blackjack, we should not expect it to know what the next card in the deck is. If the agent is answering the phone, we should not expect it to know in advance who the caller is. If the agent is a paramedic called to a road accident, we should not expect it to know immediately the internal injuries of an unconscious victim. In all of these cases there is hidden state information in the environment, and that information would be useful if the agent knew it, but the agent cannot know it because it has never received any relevant sensations. In short, we don't fault an agent for not knowing something that matters, but only for having known something and then forgotten it!

What we would like, ideally, is a state signal that summarizes past sensations compactly, yet in such a way that all relevant information is retained. This normally requires more than the immediate sensations, but never more than the complete history of all past sensations. A state signal that succeeds in retaining all relevant information is said to be Markov, or to have the Markov property (we define this formally below). For example, a checkers position—the current configuration of all the pieces on the board—would serve as a Markov state because it summarizes everything important about the

---

complete sequence of positions that led to it. Much of the information about the sequence is lost, but all that really matters for the future of the game is retained. Similarly, the current position and velocity of a cannonball is all that matters for its future flight. It doesn't matter how that position and velocity came about. This is sometimes also referred to as an “independence of path” property because all that matters is in the current state signal; its meaning is independent of the “path,” or history, of signals that have led up to it.

We now formally define the Markov property for the reinforcement learning problem. To keep the mathematics simple, we assume here that there are a finite number of states and reward values. This enables us to work in terms of sums and probabilities rather than integrals and probability densities, but the argument can easily be extended to include continuous states and rewards. Consider how a general environment might respond at time  $t+1$ to the action taken at time t. In the most general, causal case this response may depend on everything that has happened earlier. In this case the dynamics can be defined only by specifying the complete probability distribution:

$$
\Pr\{R_{t+1}=r,S_{t+1}=s^{\prime}\mid S_{0},A_{0},R_{1},\ldots,S_{t-1},A_{t-1},R_{t},S_{t},A_{t}\},   \tag*{(3.4)}
$$

for all  $r$,  $s'$, and all possible values of the past events:  $S_0$,  $A_0$,  $R_1$, ...,  $S_{t-1}$,  $A_{t-1}$,  $R_t$,  $S_t$,  $A_t$. If the state signal has the Markov property, on the other hand, then the environment's response at  $t+1$ depends only on the state and action representations at  $t$, in which case the environment's dynamics can be defined by specifying only

$$
p(s^{\prime},r|s,a)=\Pr\{R_{t+1}=r,S_{t+1}=s^{\prime}\mid S_{t},A_{t}\},   \tag*{(3.5)}
$$

for all $r$, $s'
$$
, $S_{t}$, and $A_{t}$. In other words, a state signal has the Markov property, and is a Markov state, if and only if (3.5) is equal to (3.4) for all $s'
$$
, $r$, and histories, $S_{0}$, $A_{0}$, $R_{1}$, ..., $S_{t-1}$, $A_{t-1}$, $R_{t}$, $S_{t}$, $A_{t}$. In this case, the environment and task as a whole are also said to have the Markov property.

If an environment has the Markov property, then its one-step dynamics (3.5) enable us to predict the next state and expected next reward given the current state and action. One can show that, by iterating this equation, one can predict all future states and expected rewards from knowledge only of the current state as well as would be possible given the complete history up to the current time. It also follows that Markov states provide the best possible basis for choosing actions. That is, the best policy for choosing actions as a function of a Markov state is just as good as the best policy for choosing actions as a function of complete histories.

Even when the state signal is non-Markov, it is still appropriate to think of the state in reinforcement learning as an approximation to a Markov state.

---

In particular, we always want the state to be a good basis for predicting future rewards and for selecting actions. In cases in which a model of the environment is learned (see Chapter 8), we also want the state to be a good basis for predicting subsequent states. Markov states provide an unsurpassed basis for doing all of these things. To the extent that the state approaches the ability of Markov states in these ways, one will obtain better performance from reinforcement learning systems. For all of these reasons, it is useful to think of the state at each time step as an approximation to a Markov state, although one should remember that it may not fully satisfy the Markov property.

The Markov property is important in reinforcement learning because decisions and values are assumed to be a function only of the current state. In order for these to be effective and informative, the state representation must be informative. All of the theory presented in this book assumes Markov state signals. This means that not all the theory strictly applies to cases in which the Markov property does not strictly apply. However, the theory developed for the Markov case still helps us to understand the behavior of the algorithms, and the algorithms can be successfully applied to many tasks with states that are not strictly Markov. A full understanding of the theory of the Markov case is an essential foundation for extending it to the more complex and realistic non-Markov case. Finally, we note that the assumption of Markov state representations is not unique to reinforcement learning but is also present in most if not all other approaches to artificial intelligence.

Example 3.5: Pole-Balancing State In the pole-balancing task introduced earlier, a state signal would be Markov if it specified exactly, or made it possible to reconstruct exactly, the position and velocity of the cart along the track, the angle between the cart and the pole, and the rate at which this angle is changing (the angular velocity). In an idealized cart-pole system, this information would be sufficient to exactly predict the future behavior of the cart and pole, given the actions taken by the controller. In practice, however, it is never possible to know this information exactly because any real sensor would introduce some distortion and delay in its measurements. Furthermore, in any real cart-pole system there are always other effects, such as the bending of the pole, the temperatures of the wheel and pole bearings, and various forms of backlash, that slightly affect the behavior of the system. These factors would cause violations of the Markov property if the state signal were only the positions and velocities of the cart and the pole.

However, often the positions and velocities serve quite well as states. Some early studies of learning to solve the pole-balancing task used a coarse state signal that divided cart positions into three regions: right, left, and middle (and similar rough quantizations of the other three intrinsic state variables). This distinctly non-Markov state was sufficient to allow the task to be solved.

---

easily by reinforcement learning methods. In fact, this coarse representation may have facilitated rapid learning by forcing the learning agent to ignore fine distinctions that would not have been useful in solving the task.

Example 3.6: Draw Poker In draw poker, each player is dealt a hand of five cards. There is a round of betting, in which each player exchanges some of his cards for new ones, and then there is a final round of betting. At each round, each player must match or exceed the highest bets of the other players, or else drop out (fold). After the second round of betting, the player with the best hand who has not folded is the winner and collects all the bets.

The state signal in draw poker is different for each player. Each player knows the cards in his own hand, but can only guess at those in the other players' hands. A common mistake is to think that a Markov state signal should include the contents of all the players' hands and the cards remaining in the deck. In a fair game, however, we assume that the players are in principle unable to determine these things from their past observations. If a player did know them, then she could predict some future events (such as the cards one could exchange for) better than by remembering all past observations.

In addition to knowledge of one's own cards, the state in draw poker should include the bets and the numbers of cards drawn by the other players. For example, if one of the other players drew three new cards, you may suspect he retained a pair and adjust your guess of the strength of his hand accordingly. The players' bets also influence your assessment of their hands. In fact, much of your past history with these particular players is part of the Markov state. Does Ellen like to bluff, or does she play conservatively? Does her face or demeanor provide clues to the strength of her hand? How does Joe's play change when it is late at night, or when he has already won a lot of money?

Although everything ever observed about the other players may have an effect on the probabilities that they are holding various kinds of hands, in practice this is far too much to remember and analyze, and most of it will have no clear effect on one's predictions and decisions. Very good poker players are adept at remembering just the key clues, and at sizing up new players quickly, but no one remembers everything that is relevant. As a result, the state representations people use to make their poker decisions are undoubtedly non-Markov, and the decisions themselves are presumably imperfect. Nevertheless, people still make very good decisions in such tasks. We conclude that the inability to have access to a perfect Markov state representation is probably not a severe problem for a reinforcement learning agent.

---

## 3.6 Markov Decision Processes

A reinforcement learning task that satisfies the Markov property is called a Markov decision process, or MDP. If the state and action spaces are finite, then it is called a finite Markov decision process (finite MDP). Finite MDPs are particularly important to the theory of reinforcement learning. We treat them extensively throughout this book; they are all you need to understand 90% of modern reinforcement learning.

A particular finite MDP is defined by its state and action sets and by the one-step dynamics of the environment. Given any state and action s and a, the probability of each possible pair of next state and reward,  $s', r$, is denoted

$$
p(s^{\prime},r|s,a)=\Pr\{S_{t+1}=s^{\prime},R_{t+1}=r\mid S_{t}=s,A_{t}=a\}.   \tag*{(3.6)}
$$

These quantities completely specify the dynamics of a finite MDP. Most of the theory we present in the rest of this book implicitly assumes the environment is a finite MDP.

Given the dynamics as specified by  $(3.6)$, one can compute anything else one might want to know about the environment, such as the expected rewards for state-action pairs,

$$
r(s,a)=\mathbb{E}[R_{t+1}\mid S_{t}=s,A_{t}=a]=\sum_{r\in\mathcal{R}}r\sum_{s^{\prime}\in\mathcal{S}}p(s^{\prime},r|s,a),   \tag*{(3.7)}
$$

the state-transition probabilities,

$$
p(s^{\prime}|s,a)=\Pr\{S_{t+1}=s^{\prime}\mid S_{t}=s,A_{t}=a\}=\sum_{r\in\mathcal{R}}p(s^{\prime},r|s,a),   \tag*{(3.8)}
$$

and the expected rewards for state-action-next-state triples,

$$
r(s,a,s^{\prime})=\mathbb{E}[R_{t+1}\mid S_{t}=s,A_{t}=a,S_{t+1}=s^{\prime}]=\frac{\sum_{r\in\mathbb{R}}r p(s^{\prime},r|s,a)}{p(s^{\prime}|s,a)}.   \tag*{(3.9)}
$$

In the first edition of this book, the dynamics were expressed exclusively in terms of the latter two quantities, which were denote  $\mathcal{P}_{ss'}^{a}$ and  $\mathcal{R}_{ss'}^{a}$ respectively. One weakness of that notation is that it still did not fully characterize the dynamics of the rewards, giving only their expectations. Another weakness is the excess of subscripts and superscripts. In this edition we will predominantly use the explicit notation of (3.6), while sometimes referring directly to the transition probabilities (3.8).

Example 3.7: Recycling Robot MDP The recycling robot (Example 3.3) can be turned into a simple example of an MDP by simplifying it and

---

providing some more details. (Our aim is to produce a simple example, not a particularly realistic one.) Recall that the agent makes a decision at times determined by external events (or by other parts of the robot's control system). At each such time the robot decides whether it should (1) actively search for a can, (2) remain stationary and wait for someone to bring it a can, or (3) go back to home base to recharge its battery. Suppose the environment works as follows. The best way to find cans is to actively search for them, but this runs down the robot's battery, whereas waiting does not. Whenever the robot is searching, the possibility exists that its battery will become depleted. In this case the robot must shut down and wait to be rescued (producing a low reward).

The agent makes its decisions solely as a function of the energy level of the battery. It can distinguish two levels, high and low, so that the state set is  $\mathcal{S} = \{high, low\}$. Let us call the possible decisions—the agent's actions—wait, search, and recharge. When the energy level is high, recharging would always be foolish, so we do not include it in the action set for this state. The agent's action sets are

 
$$
\begin{array}{r l r}{\mathcal{A}(\mathrm{h i g h})}&{=}&{\{\mathrm{s e a r c h,w a i t}\}}\end{array}
$$
 

 
$$
\begin{array}{r l r}{\mathcal{A}(\mathrm{l o w})}&{=}&{\{\mathrm{s e a r c h,w a i t,r e c h a r g e}\}.}\end{array}
$$
 

If the energy level is high, then a period of active search can always be completed without risk of depleting the battery. A period of searching that begins with a high energy level leaves the energy level high with probability  $\alpha$ and reduces it to  $10w$ with probability  $1 - \alpha$. On the other hand, a period of searching undertaken when the energy level is  $10w$ leaves it  $10w$ with probability  $\beta$ and depletes the battery with probability  $1 - \beta$. In the latter case, the robot must be rescued, and the battery is then recharged back to high. Each can be collected by the robot counts as a unit reward, whereas a reward of -3 results whenever the robot has to be rescued. Let  $r_{search}$ and  $r_{wait}$, with  $r_{search} > r_{wait}$, respectively denote the expected number of cans the robot will collect (and hence the expected reward) while searching and while waiting. Finally, to keep things simple, suppose that no cans can be collected during a run home for recharging, and that no cans can be collected on a step in which the battery is depleted. This system is then a finite MDP, and we can write down the transition probabilities and the expected rewards, as in Table 3.1.

A transition graph is a useful way to summarize the dynamics of a finite MDP. Figure 3.3 shows the transition graph for the recycling robot example. There are two kinds of nodes: state nodes and action nodes. There is a state node for each possible state (a large open circle labeled by the name of the state), and an action node for each state-action pair (a small solid circle labeled

---


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>s</td><td style='text-align: center; word-wrap: break-word;'>s&#x27;</td><td style='text-align: center; word-wrap: break-word;'>a</td><td style='text-align: center; word-wrap: break-word;'>$p(s&#x27; | s, a)$</td><td style='text-align: center; word-wrap: break-word;'>$r(s, a, s&#x27;)$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>search</td><td style='text-align: center; word-wrap: break-word;'>$\alpha$</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{search}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>search</td><td style='text-align: center; word-wrap: break-word;'>$1 - \alpha$</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{search}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>search</td><td style='text-align: center; word-wrap: break-word;'>$1 - \beta$</td><td style='text-align: center; word-wrap: break-word;'>$-3$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>search</td><td style='text-align: center; word-wrap: break-word;'>$\beta$</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{search}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>wait</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{wait}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>wait</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{wait}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>wait</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{wait}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>wait</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>$r_{\text{wait}}$</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>high</td><td style='text-align: center; word-wrap: break-word;'>recharge</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>low</td><td style='text-align: center; word-wrap: break-word;'>recharge</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0.</td></tr></table>

<div style="text-align: center;">Table 3.1: Transition probabilities and expected rewards for the finite MDP of the recycling robot example. There is a row for each possible combination of current state, s, next state,  $s'$, and action possible in the current state,  $a \in \mathcal{A}(s)$.</div>

by the name of the action and connected by a line to the state node). Starting in state $s$and taking action$a$moves you along the line from state node$s$to action node$(s,a)$. Then the environment responds with a transition to the next state's node via one of the arrows leaving action node $(s,a)$. Each arrow corresponds to a triple $(s,s',a)$, where $s'$is the next state, and we label the arrow with the transition probability,$p(s'|s,a)$, and the expected reward for that transition, $r(s,a,s')$. Note that the transition probabilities labeling the arrows leaving an action node always sum to 1.

<div style="text-align: center;"><img src="imgs/img_in_image_box_290_1048_915_1370.jpg" alt="Image" width="51%" /></div>

<div style="text-align: center;">Figure 3.3: Transition graph for the recycling robot example.</div>


---

## 3.7 Value Functions

Almost all reinforcement learning algorithms involve estimating value functions—functions of states (or of state-action pairs) that estimate how good it is for the agent to be in a given state (or how good it is to perform a given action in a given state). The notion of “how good” here is defined in terms of future rewards that can be expected, or, to be precise, in terms of expected return. Of course the rewards the agent can expect to receive in the future depend on what actions it will take. Accordingly, value functions are defined with respect to particular policies.

Recall that a policy,  $\pi$, is a mapping from each state,  $s \in \mathcal{S}$, and action,  $a \in \mathcal{A}(s)$, to the probability  $\pi(a|s)$ of taking action  $a$ when in state  $s$. Informally, the value of a state  $s$ under a policy  $\pi$, denoted  $v_{\pi}(s)$, is the expected return when starting in  $s$ and following  $\pi$ thereafter. For MDPs, we can define  $v_{\pi}(s)$ formally as

$$
v_{\pi}(s)=\mathbb{E}_{\pi}[G_{t}\mid S_{t}=s]=\mathbb{E}_{\pi}\left[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\middle|S_{t}=s\right],   \tag*{(3.10)}
$$

where  $\mathbb{E}_{\pi}[\cdot]$ denotes the expected value of a random variable given that the agent follows policy  $\pi$, and  $t$ is any time step. Note that the value of the terminal state, if any, is always zero. We call the function  $v_{\pi}$ the state-value function for policy  $\pi$.

Similarly, we define the value of taking action a in state s under a policy  $\pi$, denoted  $q_{\pi}(s,a)$, as the expected return starting from s, taking the action a, and thereafter following policy  $\pi$:

$$
q_{\pi}(s,a)=\mathbb{E}_{\pi}[G_{t}\mid S_{t}=s,A_{t}=a]=\mathbb{E}_{\pi}\Biggl[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\Biggr|\;S_{t}=s,A_{t}=a\Biggr].   \tag*{(3.11)}
$$

We call qπ the action-value function for policy π.

The value functions  $v_{\pi}$ and  $q_{\pi}$ can be estimated from experience. For example, if an agent follows policy  $\pi$ and maintains an average, for each state encountered, of the actual returns that have followed that state, then the average will converge to the state's value,  $v_{\pi}(s)$, as the number of times that state is encountered approaches infinity. If separate averages are kept for each action taken in a state, then these averages will similarly converge to the action values,  $q_{\pi}(s,a)$. We call estimation methods of this kind Monte Carlo methods because they involve averaging over many random samples of actual returns. These kinds of methods are presented in Chapter 5. Of course, if there are very many states, then it may not be practical to keep separate averages for each

---

state individually. Instead, the agent would have to maintain  $v_{\pi}$ and  $q_{\pi}$ as parameterized functions and adjust the parameters to better match the observed returns. This can also produce accurate estimates, although much depends on the nature of the parameterized function approximator (Chapter 9).

A fundamental property of value functions used throughout reinforcement learning and dynamic programming is that they satisfy particular recursive relationships. For any policy  $\pi$ and any state s, the following consistency condition holds between the value of s and the value of its possible successor states:

 
$$
\begin{align*}v_{\pi}(s)\quad&=\quad\mathbb{E}_{\pi}[G_{t}\quad|S_{t}=s]\\&=\quad\mathbb{E}_{\pi}\Biggl[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\quad\Biggl|S_{t}=s\Biggr]\\&=\quad\mathbb{E}_{\pi}\Biggl[R_{t+1}+\gamma\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+2}\quad\Biggl|S_{t}=s\Biggr]\\&=\quad\sum_{a}\pi(a|s)\sum_{s^{\prime}}\sum_{r}p(s^{\prime},r|s,a)\Biggl[r+\gamma\mathbb{E}_{\pi}\Biggl[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+2}\quad\Biggl|S_{t+1}=s^{\prime}\Biggr]\Biggr]\\&=\quad\sum_{a}\pi(a|s)\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Biggl[r+\gamma v_{\pi}(s^{\prime})\Biggr],\quad(3.12)\end{align*}
$$
 

where it is implicit that the actions, $a$, are taken from the set $\mathcal{A}(s)$, the next states, $s'$, are taken from the set $\mathcal{S}$(or from$\mathcal{S}^{+}$in the case of an episodic problem), and the rewards,$r$, are taken from the set $\mathcal{R}$. Note also how in the last equation we have merged the two sums, one over all the values of $s'$and the other over all values of$r$, into one sum over all possible values of both. We will use this kind of merged sum often to simplify formulas. Note how the final expression can be read very easily as an expected value. It is really a sum over all values of the three variables, $a$, $s'$, and $r$. For each triple, we compute its probability, $\pi(a|s)p(s',r|s,a)$, weight the quantity in brackets by that probability, then sum over all possibilities to get an expected value.

Equation (3.12) is the Bellman equation for  $v_{\pi}$. It expresses a relationship between the value of a state and the values of its successor states. Think of looking ahead from one state to its possible successor states, as suggested by Figure 3.4a. Each open circle represents a state and each solid circle represents a state-action pair. Starting from state s, the root node at the top, the agent could take any of some set of actions—three are shown in Figure 3.4a. From each of these, the environment could respond with one of several next states,  $s'$, along with a reward, r. The Bellman equation (3.12) averages over all the possibilities, weighting each by its probability of occurring. It states that the

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_291_217_928_418.jpg" alt="Image" width="52%" /></div>

<div style="text-align: center;">Figure 3.4: Backup diagrams for (a)  $v_{\pi}$ and (b)  $q_{\pi}$.</div>

value of the start state must equal the (discounted) value of the expected next state, plus the reward expected along the way.

The value function  $v_{\pi}$ is the unique solution to its Bellman equation. We show in subsequent chapters how this Bellman equation forms the basis of a number of ways to compute, approximate, and learn  $v_{\pi}$. We call diagrams like those shown in Figure 3.4 backup diagrams because they diagram relationships that form the basis of the update or backup operations that are at the heart of reinforcement learning methods. These operations transfer value information back to a state (or a state-action pair) from its successor states (or state-action pairs). We use backup diagrams throughout the book to provide graphical summaries of the algorithms we discuss. (Note that unlike transition graphs, the state nodes of backup diagrams do not necessarily represent distinct states; for example, a state might be its own successor. We also omit explicit arrowheads because time always flows downward in a backup diagram.)

Example 3.8: Gridworld Figure 3.5a uses a rectangular grid to illustrate value functions for a simple finite MDP. The cells of the grid correspond to the states of the environment. At each cell, four actions are possible: north, south, east, and west, which deterministically cause the agent to move one cell in the respective direction on the grid. Actions that would take the agent off the grid leave its location unchanged, but also result in a reward of -1. Other actions result in a reward of 0, except those that move the agent out of the special states A and B. From state A, all four actions yield a reward of +10 and take the agent to A'. From state B, all actions yield a reward of +5 and take the agent to B'.

Suppose the agent selects all four actions with equal probability in all states. Figure 3.5b shows the value function,  $v_{\pi}$, for this policy, for the discounted reward case with  $\gamma = 0.9$. This value function was computed by solving the system of equations (3.12). Notice the negative values near the lower edge; these are the result of the high probability of hitting the edge of the grid there under the random policy. State A is the best state to be in under this policy.

---

## 3.7. VALUE FUNCTIONS

<div style="text-align: center;"><img src="imgs/img_in_image_box_385_232_881_395.jpg" alt="Image" width="40%" /></div>

<div style="text-align: center;">Figure 3.5: Grid example: (a) exceptional reward dynamics; (b) state-value function for the equiprobable random policy.</div>

icy, but its expected return is less than 10, its immediate reward, because from A the agent is taken to A', from which it is likely to run into the edge of the grid. State B, on the other hand, is valued more than 5, its immediate reward, because from B the agent is taken to B', which has a positive value. From B' the expected penalty (negative reward) for possibly running into an edge is more than compensated for by the expected gain for possibly stumbling onto A or B.

Example 3.9: Golf To formulate playing a hole of golf as a reinforcement learning task, we count a penalty (negative reward) of -1 for each stroke until we hit the ball into the hole. The state is the location of the ball. The value of a state is the negative of the number of strokes to the hole from that location. Our actions are how we aim and swing at the ball, of course, and which club we select. Let us take the former as given and consider just the choice of club, which we assume is either a putter or a driver. The upper part of Figure 3.6 shows a possible state-value function,  $v_{\text{putt}}(s)$, for the policy that always uses the putter. The terminal state in-the-hole has a value of 0. From anywhere on the green we assume we can make a putt; these states have value -1. Off the green we cannot reach the hole by putting, and the value is greater. If we can reach the green from a state by putting, then that state must have value one less than the green's value, that is, -2. For simplicity, let us assume we can putt very precisely and deterministically, but with a limited range. This gives us the sharp contour line labeled -2 in the figure; all locations between that line and the green require exactly two strokes to complete the hole. Similarly, any location within putting range of the -2 contour line must have a value of -3, and so on to get all the contour lines shown in the figure. Putting doesn't get us out of sand traps, so they have a value of -∞. Overall, it takes us six strokes to get from the tee to the hole by putting.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_272_399_982_1158.jpg" alt="Image" width="58%" /></div>

<div style="text-align: center;">Figure 3.6: A golf example: the state-value function for putting (above) and the optimal action-value function for using the driver (below).</div>


---

## 3.8 Optimal Value Functions

Solving a reinforcement learning task means, roughly, finding a policy that achieves a lot of reward over the long run. For finite MDPs, we can precisely define an optimal policy in the following way. Value functions define a partial ordering over policies. A policy  $\pi$ is defined to be better than or equal to a policy  $\pi'$ if its expected return is greater than or equal to that of  $\pi'$ for all states. In other words,  $\pi \geq \pi'$ if and only if  $v_{\pi}(s) \geq v_{\pi'}(s)$ for all  $s \in S$. There is always at least one policy that is better than or equal to all other policies. This is an optimal policy. Although there may be more than one, we denote all the optimal policies by  $\pi_*$. They share the same state-value function, called the optimal state-value function, denoted  $v_*$, and defined as

$$
v_{*}(s)=\max_{\pi}v_{\pi}(s),   \tag*{(3.13)}
$$

for all  $s \in \mathcal{S}$.

Optimal policies also share the same optimal action-value function, denoted  $q_{*}$, and defined as

$$
q_{*}(s,a)=\max_{\pi}q_{\pi}(s,a),   \tag*{(3.14)}
$$

for all  $s \in \mathcal{S}$ and  $a \in \mathcal{A}(s)$. For the state-action pair  $(s, a)$, this function gives the expected return for taking action  $a$ in state  $s$ and thereafter following an optimal policy. Thus, we can write  $q_*$ in terms of  $v_*$ as follows:

$$
q_{*}(s,a)=\mathbb{E}[R_{t+1}+\gamma v_{*}(S_{t+1})\mid S_{t}=s,A_{t}=a].   \tag*{(3.15)}
$$

Example 3.10: Optimal Value Functions for Golf The lower part of Figure 3.6 shows the contours of a possible optimal action-value function  $q_{*}(s,\text{driver})$. These are the values of each state if we first play a stroke with the driver and afterward select either the driver or the putter, whichever is better. The driver enables us to hit the ball farther, but with less accuracy. We can reach the hole in one shot using the driver only if we are already very close; thus the -1 contour for  $q_{*}(s,\text{driver})$ covers only a small portion of the green. If we have two strokes, however, then we can reach the hole from much farther away, as shown by the -2 contour. In this case we don't have to drive all the way to within the small -1 contour, but only to anywhere on the green; from there we can use the putter. The optimal action-value function gives the values after committing to a particular first action, in this case, to the driver, but afterward using whichever actions are best. The -3 contour is still farther out and includes the starting tee. From the tee, the best sequence of actions is two drives and one putt, sinking the ball in three strokes.

---

Because  $v_{*}$ is the value function for a policy, it must satisfy the self-consistency condition given by the Bellman equation for state values (3.12). Because it is the optimal value function, however,  $v_{*}$'s consistency condition can be written in a special form without reference to any specific policy. This is the Bellman equation for  $v_{*}$, or the Bellman optimality equation. Intuitively, the Bellman optimality equation expresses the fact that the value of a state under an optimal policy must equal the expected return for the best action from that state:

$$
\begin{array}{r c l}{v_{*}(s)}&{=}&{\displaystyle\operatorname*{m a x}_{a\in\mathcal{A}(s)}q_{\pi_{*}}(s,a)}\\ {}&{=}&{\displaystyle\operatorname*{m a x}_{a}\mathbb{E}_{\pi^{*}}[G_{t}\mid S_{t}=s,A_{t}=a]}\\ {}&{=}&{\displaystyle\operatorname*{m a x}_{a}\mathbb{E}_{\pi^{*}}\left[\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\Bigg\vert S_{t}=s,A_{t}=a\right]}\\ {}&{=}&{\displaystyle\operatorname*{m a x}_{a}\mathbb{E}_{\pi^{*}}\left[R_{t+1}+\gamma\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+2}\Bigg\vert S_{t}=s,A_{t}=a\right]}\\ {}&{=}&{\displaystyle\operatorname*{m a x}_{a}\mathbb{E}[R_{t+1}+\gamma v_{*}(S_{t+1})\mid S_{t}=s,A_{t}=a]}\\ {}&{=}&{\displaystyle\operatorname*{m a x}_{a\in\mathcal{A}(s)}\sum_{s^{\prime},r}p(s^{\prime},r\vert s,a)\big[r+\gamma v_{*}(s^{\prime})\big].}\\ \end{array}   \tag*{(3.16)}
$$

The last two equations are two forms of the Bellman optimality equation for  $v_{*}$. The Bellman optimality equation for  $q_{*}$ is

 
$$
\begin{align*}q_{*}(s,a)\ &=\mathbb{E}\Big[R_{t+1}+\gamma\max_{a^{\prime}}q_{*}(S_{t+1},a^{\prime})\ \Big|\ S_{t}=s,A_{t}=a\Big]\\&=\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma\max_{a^{\prime}}q_{*}(s^{\prime},a^{\prime})\Big].\end{align*}
$$
 

The backup diagrams in Figure 3.7 show graphically the spans of future states and actions considered in the Bellman optimality equations for  $v_{*}$ and  $q_{*}$. These are the same as the backup diagrams for  $v_{\pi}$ and  $q_{\pi}$ except that arcs have been added at the agent's choice points to represent that the maximum over that choice is taken rather than the expected value given some policy. Figure 3.7a graphically represents the Bellman optimality equation (3.17).

For finite MDPs, the Bellman optimality equation (3.17) has a unique solution independent of the policy. The Bellman optimality equation is actually a system of equations, one for each state, so if there are $N$states, then there are$N$equations in$N$unknowns. If the dynamics of the environment are known$(p(s', r|s, a))$, then in principle one can solve this system of equations

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_291_218_929_418.jpg" alt="Image" width="52%" /></div>

<div style="text-align: center;">Figure 3.7: Backup diagrams for (a)  $v_{*}$ and (b)  $q_{*}$</div>

for  $v_{*}$ using any one of a variety of methods for solving systems of nonlinear equations. One can solve a related set of equations for  $q_{*}$.

Once one has  $v_{*}$, it is relatively easy to determine an optimal policy. For each state s, there will be one or more actions at which the maximum is obtained in the Bellman optimality equation. Any policy that assigns nonzero probability only to these actions is an optimal policy. You can think of this as a one-step search. If you have the optimal value function,  $v_{*}$, then the actions that appear best after a one-step search will be optimal actions. Another way of saying this is that any policy that is greedy with respect to the optimal evaluation function  $v_{*}$ is an optimal policy. The term greedy is used in computer science to describe any search or decision procedure that selects alternatives based only on local or immediate considerations, without considering the possibility that such a selection may prevent future access to even better alternatives. Consequently, it describes policies that select actions based only on their short-term consequences. The beauty of  $v_{*}$ is that if one uses it to evaluate the short-term consequences of actions—specifically, the one-step consequences—then a greedy policy is actually optimal in the long-term sense in which we are interested because  $v_{*}$ already takes into account the reward consequences of all possible future behavior. By means of  $v_{*}$, the optimal expected long-term return is turned into a quantity that is locally and immediately available for each state. Hence, a one-step-ahead search yields the long-term optimal actions.

Having $q_{*}$makes choosing optimal actions still easier. With$q_{*}$, the agent does not even have to do a one-step-ahead search: for any state $s$, it can simply find any action that maximizes $q_{*}(s,a)$. The action-value function effectively caches the results of all one-step-ahead searches. It provides the optimal expected long-term return as a value that is locally and immediately available for each state-action pair. Hence, at the cost of representing a function of state-action pairs, instead of just of states, the optimal action-value function allows optimal actions to be selected without having to know anything about possible successor states and their values, that is, without having to know

---

anything about the environment’s dynamics.

Example 3.11: Bellman Optimality Equations for the Recycling Robot Using (3.17), we can explicitly give the Bellman optimality equation for the recycling robot example. To make things more compact, we abbreviate the states high and low, and the actions search, wait, and recharge respectively by h, 1, s, w, and re. Since there are only two states, the Bellman optimality equation consists of two equations. The equation for  $v_{*}(h)$ can be written as follows:

 
$$
\begin{array}{r c l}{v_{*}(\mathbf{h})}&{=}&{\operatorname*{m a x}\left\{\begin{array}{l}{p(\mathbf{h}|\mathbf{h},\mathbf{s})[r(\mathbf{h},\mathbf{s},\mathbf{h})+\gamma v_{*}(\mathbf{h})]+p(\mathbf{l}|\mathbf{h},\mathbf{s})[r(\mathbf{h},\mathbf{s},\mathbf{l})+\gamma v_{*}(\mathbf{l})],}\\ {p(\mathbf{h}|\mathbf{h},\mathbf{w})[r(\mathbf{h},\mathbf{w},\mathbf{h})+\gamma v_{*}(\mathbf{h})]+p(\mathbf{l}|\mathbf{h},\mathbf{w})[r(\mathbf{h},\mathbf{w},\mathbf{l})+\gamma v_{*}(\mathbf{l})]}\end{array}\right\}}\\ {}&{=}&{\operatorname*{m a x}\left\{\begin{array}{l}{\alpha[r_{\mathbf{s}}+\gamma v_{*}(\mathbf{h})]+(1-\alpha)[r_{\mathbf{s}}+\gamma v_{*}(\mathbf{l})],}\\ {1[r_{\mathbf{w}}+\gamma v_{*}(\mathbf{h})]+0[r_{\mathbf{w}}+\gamma v_{*}(\mathbf{l})]}\end{array}\right\}}\\ {}&{=}&{\operatorname*{m a x}\left\{\begin{array}{l}{r_{\mathbf{s}}+\gamma[\alpha v_{*}(\mathbf{h})+(1-\alpha)v_{*}(\mathbf{l})],}\\ {r_{\mathbf{w}}+\gamma v_{*}(\mathbf{h})}\end{array}\right\}.}\\ \end{array}
$$
 

Following the same procedure for  $v_{*}(1)$ yields the equation

 
$$
v_{*}(\mathbf{1})=\max\left\{\begin{array}{l}\beta r_{\mathbf{s}}-3(1-\beta)+\gamma[(1-\beta)v_{*}(\mathbf{h})+\beta v_{*}(\mathbf{l})]\\ r_{\mathbf{w}}+\gamma v_{*}(\mathbf{l}),\\ \gamma v_{*}(\mathbf{h})\end{array}\right\}.
$$
 

For any choice of  $r_{\mathbf{s}}, r_{\mathbf{w}}, \alpha, \beta$, and  $\gamma$, with  $0 \leq \gamma < 1$,  $0 \leq \alpha, \beta \leq 1$, there is exactly one pair of numbers,  $v_{*}(\mathbf{h})$ and  $v_{*}(1)$, that simultaneously satisfy these two nonlinear equations.

Example 3.12: Solving the Gridworld Suppose we solve the Bellman equation for  $v_{*}$ for the simple grid task introduced in Example 3.8 and shown again in Figure 3.8a. Recall that state A is followed by a reward of +10 and transition to state  $A'$, while state B is followed by a reward of +5 and transition to state  $B'$. Figure 3.8b shows the optimal value function, and Figure 3.8c shows the corresponding optimal policies. Where there are multiple arrows in a cell, any of the corresponding actions is optimal.

Explicitly solving the Bellman optimality equation provides one route to finding an optimal policy, and thus to solving the reinforcement learning problem. However, this solution is rarely directly useful. It is akin to an exhaustive search, looking ahead at all possibilities, computing their probabilities of occurrence and their desirabilities in terms of expected rewards. This solution relies on at least three assumptions that are rarely true in practice: (1) we accurately know the dynamics of the environment; (2) we have enough computational resources to complete the computation of the solution; and (3) the Markov property. For the kinds of tasks in which we are interested, one is

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_360_233_518_390.jpg" alt="Image" width="12%" /></div>

<div style="text-align: center;">a) gridworld</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_556_234_713_392.jpg" alt="Image" width="12%" /></div>

<div style="text-align: center;">b) V*</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_748_233_906_391.jpg" alt="Image" width="12%" /></div>

<div style="text-align: center;">c)  $\pi_{*}$</div>

<div style="text-align: center;">Figure 3.8: Optimal solutions to the gridworld example.</div>

generally not able to implement this solution exactly because various combinations of these assumptions are violated. For example, although the first and third assumptions present no problems for the game of backgammon, the second is a major impediment. Since the game has about  $10^{20}$ states, it would take thousands of years on today's fastest computers to solve the Bellman equation for  $v_{*}$, and the same is true for finding  $q_{*}$. In reinforcement learning one typically has to settle for approximate solutions.

Many different decision-making methods can be viewed as ways of approximately solving the Bellman optimality equation. For example, heuristic search methods can be viewed as expanding the right-hand side of (3.17) several times, up to some depth, forming a “tree” of possibilities, and then using a heuristic evaluation function to approximate  $v_{*}$ at the “leaf” nodes. (Heuristic search methods such as  $A^{*}$ are almost always based on the episodic case.) The methods of dynamic programming can be related even more closely to the Bellman optimality equation. Many reinforcement learning methods can be clearly understood as approximately solving the Bellman optimality equation, using actual experienced transitions in place of knowledge of the expected transitions. We consider a variety of such methods in the following chapters.

## 3.9 Optimality and Approximation

We have defined optimal value functions and optimal policies. Clearly, an agent that learns an optimal policy has done very well, but in practice this rarely happens. For the kinds of tasks in which we are interested, optimal policies can be generated only with extreme computational cost. A well-defined notion of optimality organizes the approach to learning we describe in this book and provides a way to understand the theoretical properties of various learning algorithms, but it is an ideal that agents can only approximate to varying degrees. As we discussed above, even if we have a complete and accurate model of the environment's dynamics, it is usually not possible to simply

---

compute an optimal policy by solving the Bellman optimality equation. For example, board games such as chess are a tiny fraction of human experience, yet large, custom-designed computers still cannot compute the optimal moves. A critical aspect of the problem facing the agent is always the computational power available to it, in particular, the amount of computation it can perform in a single time step.

The memory available is also an important constraint. A large amount of memory is often required to build up approximations of value functions, policies, and models. In tasks with small, finite state sets, it is possible to form these approximations using arrays or tables with one entry for each state (or state-action pair). This we call the tabular case, and the corresponding methods we call tabular methods. In many cases of practical interest, however, there are far more states than could possibly be entries in a table. In these cases the functions must be approximated, using some sort of more compact parameterized function representation.

Our framing of the reinforcement learning problem forces us to settle for approximations. However, it also presents us with some unique opportunities for achieving useful approximations. For example, in approximating optimal behavior, there may be many states that the agent faces with such a low probability that selecting suboptimal actions for them has little impact on the amount of reward the agent receives. Tesauro's backgammon player, for example, plays with exceptional skill even though it might make very bad decisions on board configurations that never occur in games against experts. In fact, it is possible that TD-Gammon makes bad decisions for a large fraction of the game's state set. The on-line nature of reinforcement learning makes it possible to approximate optimal policies in ways that put more effort into learning to make good decisions for frequently encountered states, at the expense of less effort for infrequently encountered states. This is one key property that distinguishes reinforcement learning from other approaches to approximately solving MDPs.

## 3.10 Summary

Let us summarize the elements of the reinforcement learning problem that we have presented in this chapter. Reinforcement learning is about learning from interaction how to behave in order to achieve a goal. The reinforcement learning agent and its environment interact over a sequence of discrete time steps. The specification of their interface defines a particular task: the actions are the choices made by the agent; the states are the basis for making the choices; and the rewards are the basis for evaluating the choices. Everything

---

inside the agent is completely known and controllable by the agent; everything outside is incompletely controllable but may or may not be completely known. A policy is a stochastic rule by which the agent selects actions as a function of states. The agent's objective is to maximize the amount of reward it receives over time.

The return is the function of future rewards that the agent seeks to maximize. It has several different definitions depending upon the nature of the task and whether one wishes to discount delayed reward. The undiscounted formulation is appropriate for episodic tasks, in which the agent-environment interaction breaks naturally into episodes; the discounted formulation is appropriate for continuing tasks, in which the interaction does not naturally break into episodes but continues without limit.

An environment satisfies the Markov property if its state signal compactly summarizes the past without degrading the ability to predict the future. This is rarely exactly true, but often nearly so; the state signal should be chosen or constructed so that the Markov property holds as nearly as possible. In this book we assume that this has already been done and focus on the decision-making problem: how to decide what to do as a function of whatever state signal is available. If the Markov property does hold, then the environment is called a Markov decision process (MDP). A finite MDP is an MDP with finite state and action sets. Most of the current theory of reinforcement learning is restricted to finite MDPs, but the methods and ideas apply more generally.

A policy’s value functions assign to each state, or state-action pair, the expected return from that state, or state-action pair, given that the agent uses the policy. The optimal value functions assign to each state, or state-action pair, the largest expected return achievable by any policy. A policy whose value functions are optimal is an optimal policy. Whereas the optimal value functions for states and state-action pairs are unique for a given MDP, there can be many optimal policies. Any policy that is greedy with respect to the optimal value functions must be an optimal policy. The Bellman optimality equations are special consistency condition that the optimal value functions must satisfy and that can, in principle, be solved for the optimal value functions, from which an optimal policy can be determined with relative ease.

A reinforcement learning problem can be posed in a variety of different ways depending on assumptions about the level of knowledge initially available to the agent. In problems of complete knowledge, the agent has a complete and accurate model of the environment's dynamics. If the environment is an MDP, then such a model consists of the one-step transition probabilities and expected rewards for all states and their allowable actions. In problems of incomplete knowledge, a complete and perfect model of the environment is not available.

---

Even if the agent has a complete and accurate environment model, the agent is typically unable to perform enough computation per time step to fully use it. The memory available is also an important constraint. Memory may be required to build up accurate approximations of value functions, policies, and models. In most cases of practical interest there are far more states than could possibly be entries in a table, and approximations must be made.

A well-defined notion of optimality organizes the approach to learning we describe in this book and provides a way to understand the theoretical properties of various learning algorithms, but it is an ideal that reinforcement learning agents can only approximate to varying degrees. In reinforcement learning we are very much concerned with cases in which optimal solutions cannot be found but must be approximated in some way.

#### Bibliographical and Historical Remarks

The reinforcement learning problem is deeply indebted to the idea of Markov decision processes (MDPs) from the field of optimal control. These historical influences and other major influences from psychology are described in the brief history given in Chapter 1. Reinforcement learning adds to MDPs a focus on approximation and incomplete information for realistically large problems. MDPs and the reinforcement learning problem are only weakly linked to traditional learning and decision-making problems in artificial intelligence. However, artificial intelligence is now vigorously exploring MDP formulations for planning and decision-making from a variety of perspectives. MDPs are more general than previous formulations used in artificial intelligence in that they permit more general kinds of goals and uncertainty.

Our presentation of the reinforcement learning problem was influenced by Watkins (1989).

3.1 The bioreactor example is based on the work of Ungar (1990) and Miller and Williams (1992). The recycling robot example was inspired by the can-collecting robot built by Jonathan Connell (1989).

3.3–4 The terminology of episodic and continuing tasks is different from that usually used in the MDP literature. In that literature it is common to distinguish three types of tasks: (1) finite-horizon tasks, in which interaction terminates after a particular fixed number of time steps; (2) indefinite-horizon tasks, in which interaction can last arbitrarily long but must eventually terminate; and (3) infinite-horizon tasks, in which interaction does not terminate. Our episodic and continuing tasks are

---

similar to indefinite-horizon and infinite-horizon tasks, respectively, but we prefer to emphasize the difference in the nature of the interaction. This difference seems more fundamental than the difference in the objective functions emphasized by the usual terms. Often episodic tasks use an indefinite-horizon objective function and continuing tasks an infinite-horizon objective function, but we see this as a common coincidence rather than a fundamental difference.

The pole-balancing example is from Michie and Chambers (1968) and Barto, Sutton, and Anderson (1983).

3.5 For further discussion of the concept of state, see Minsky (1967).

3.6 The theory of MDPs is treated by, e.g., Bertsekas (1995), Ross (1983), White (1969), and Whittle (1982, 1983). This theory is also studied under the heading of stochastic optimal control, where adaptive optimal control methods are most closely related to reinforcement learning (e.g., Kumar, 1985; Kumar and Varaiya, 1986).

The theory of MDPs evolved from efforts to understand the problem of making sequences of decisions under uncertainty, where each decision can depend on the previous decisions and their outcomes. It is sometimes called the theory of multistage decision processes, or sequential decision processes, and has roots in the statistical literature on sequential sampling beginning with the papers by Thompson (1933, 1934) and Robbins (1952) that we cited in Chapter 2 in connection with bandit problems (which are prototypical MDPs if formulated as multiple-situation problems).

The earliest instance of which we are aware in which reinforcement learning was discussed using the MDP formalism is Andreae's (1969b) description of a unified view of learning machines. Witten and Corbin (1973) experimented with a reinforcement learning system later analyzed by Witten (1977) using the MDP formalism. Although he did not explicitly mention MDPs, Werbos (1977) suggested approximate solution methods for stochastic optimal control problems that are related to modern reinforcement learning methods (see also Werbos, 1982, 1987, 1988, 1989, 1992). Although Werbos's ideas were not widely recognized at the time, they were prescient in emphasizing the importance of approximately solving optimal control problems in a variety of domains, including artificial intelligence. The most influential integration of reinforcement learning and MDPs is due to Watkins (1989). His treatment of reinforcement learning using the MDP formalism has been widely adopted.

---

Our characterization of the dynamics of an MDP in terms of  $p(s', r|s, a)$ is slightly unusual. It is more common in the MDP literature to describe the dynamics in terms of the state transition probabilities  $p(s' | s, a)$ and expected next rewards  $r(s, a)$. In reinforcement learning, however, we more often have to refer to individual actual or sample rewards (rather than just their expected values). Our notation also makes it plainer that  $S_t$ and  $R_t$ are in general jointly determined, and thus must have the same time index. In teaching reinforcement learning, we have found our notation to be more straightforward conceptually and easier to understand.

3.7–8 Assigning value on the basis of what is good or bad in the long run has ancient roots. In control theory, mapping states to numerical values representing the long-term consequences of control decisions is a key part of optimal control theory, which was developed in the 1950s by extending nineteenth century state-function theories of classical mechanics (see, e.g., Schultz and Melsa, 1967). In describing how a computer could be programmed to play chess, Shannon (1950) suggested using an evaluation function that took into account the long-term advantages and disadvantages of chess positions.

Watkins’s (1989) Q-learning algorithm for estimating  $q_{*}$ (Chapter 6) made action-value functions an important part of reinforcement learning, and consequently these functions are often called Q-functions. But the idea of an action-value function is much older than this. Shannon (1950) suggested that a function  $h(P, M)$ could be used by a chess-playing program to decide whether a move M in position P is worth exploring. Michie’s (1961, 1963) MENACE system and Michie and Chambers’s (1968) BOXES system can be understood as estimating action-value functions. In classical physics, Hamilton’s principal function is an action-value function; Newtonian dynamics are greedy with respect to this function (e.g., Goldstein, 1957). Action-value functions also played a central role in Denardo’s (1967) theoretical treatment of DP in terms of contraction mappings.

What we call the Bellman equation for  $v_{*}$ was first introduced by Richard Bellman (1957a), who called it the “basic functional equation.” The counterpart of the Bellman optimality equation for continuous time and state problems is known as the Hamilton–Jacobi–Bellman equation (or often just the Hamilton–Jacobi equation), indicating its roots in classical physics (e.g., Schultz and Melsa, 1967).

The golf example was suggested by Chris Watkins.

---

#### Exercises

Exercise 3.1 Devise three example tasks of your own that fit into the reinforcement learning framework, identifying for each its states, actions, and rewards. Make the three examples as different from each other as possible. The framework is abstract and flexible and can be applied in many different ways. Stretch its limits in some way in at least one of your examples.

Exercise 3.2 Is the reinforcement learning framework adequate to usefully represent all goal-directed learning tasks? Can you think of any clear exceptions?

Exercise 3.3 Consider the problem of driving. You could define the actions in terms of the accelerator, steering wheel, and brake, that is, where your body meets the machine. Or you could define them farther out—say, where the rubber meets the road, considering your actions to be tire torques. Or you could define them farther in—say, where your brain meets your body, the actions being muscle twitches to control your limbs. Or you could go to a really high level and say that your actions are your choices of where to drive. What is the right level, the right place to draw the line between agent and environment? On what basis is one location of the line to be preferred over another? Is there any fundamental reason for preferring one location over another, or is it a free choice?

Exercise 3.4 Suppose you treated pole-balancing as an episodic task but also used discounting, with all rewards zero except for -1 upon failure. What then would the return be at each time? How does this return differ from that in the discounted, continuing formulation of this task?

Exercise 3.5 Imagine that you are designing a robot to run a maze. You decide to give it a reward of +1 for escaping from the maze and a reward of zero at all other times. The task seems to break down naturally into episodes—the successive runs through the maze—so you decide to treat it as an episodic task, where the goal is to maximize expected total reward (3.1). After running the learning agent for a while, you find that it is showing no improvement in escaping from the maze. What is going wrong? Have you effectively communicated to the agent what you want it to achieve?

Exercise 3.6: Broken Vision System Imagine that you are a vision system. When you are first turned on for the day, an image floods into your camera. You can see lots of things, but not all things. You can't see objects that are occluded, and of course you can't see objects that are behind you. After seeing that first scene, do you have access to the Markov state of the environment? Suppose your camera was broken that day and you received no

---

images at all, all day. Would you have access to the Markov state then?

Exercise 3.7 There is no exercise 3.7.

Exercise 3.8 What is the Bellman equation for action values, that is, for  $q_{\pi}$? It must give the action value  $q_{\pi}(s,a)$ in terms of the action values,  $q_{\pi}(s',a')$, of possible successors to the state-action pair  $(s,a)$. As a hint, the backup diagram corresponding to this equation is given in Figure 3.4b. Show the sequence of equations analogous to (3.12), but for action values.

Exercise 3.9 The Bellman equation (3.12) must hold for each state for the value function  $v_{\pi}$ shown in Figure 3.5b. As an example, show numerically that this equation holds for the center state, valued at +0.7, with respect to its four neighboring states, valued at +2.3, +0.4, -0.4, and +0.7. (These numbers are accurate only to one decimal place.)

Exercise 3.10 In the gridworld example, rewards are positive for goals, negative for running into the edge of the world, and zero the rest of the time. Are the signs of these rewards important, or only the intervals between them? Prove, using (3.2), that adding a constant c to all the rewards adds a constant,  $v_{c}$, to the values of all states, and thus does not affect the relative values of any states under any policies. What is  $v_{c}$ in terms of c and  $\gamma$?

Exercise 3.11 Now consider adding a constant c to all the rewards in an episodic task, such as maze running. Would this have any effect, or would it leave the task unchanged as in the continuing task above? Why or why not? Give an example.

Exercise 3.12 The value of a state depends on the values of the actions possible in that state and on how likely each action is to be taken under the current policy. We can think of this in terms of a small backup diagram rooted at the state and considering each possible action:

<div style="text-align: center;"><img src="imgs/img_in_image_box_324_1077_883_1193.jpg" alt="Image" width="45%" /></div>

Give the equation corresponding to this intuition and diagram for the value at the root node,  $v_{\pi}(s)$, in terms of the value at the expected leaf node,  $q_{\pi}(s,a)$, given  $S_{t}=s$. This expectation depends on the policy,  $\pi$. Then give a second equation in which the expected value is written out explicitly in terms of  $\pi(a|s)$ such that no expected value notation appears in the equation.

Exercise 3.13 The value of an action,  $q_{\pi}(s,a)$, depends on the expected next reward and the expected sum of the remaining rewards. Again we can