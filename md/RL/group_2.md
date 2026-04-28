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

think of this in terms of a small backup diagram, this one rooted at an action (state-action pair) and branching to the possible next states:

<div style="text-align: center;"><img src="imgs/img_in_image_box_374_281_847_406.jpg" alt="Image" width="38%" /></div>

Give the equation corresponding to this intuition and diagram for the action value,  $q_{\pi}(s,a)$, in terms of the expected next reward,  $R_{t+1}$, and the expected next state value,  $v_{\pi}(S_{t+1})$, given that  $S_t = s$ and  $A_t = a$. Then give a second equation, writing out the expected value explicitly in terms of  $p(s', r|s,a)$ defined by (3.6), such that no expected value notation appears in the equation.

Exercise 3.14 Draw or describe the optimal state-value function for the golf example.

Exercise 3.15 Draw or describe the contours of the optimal action-value function for putting,  $q_{*}(s, \text{putter})$, for the golf example.

Exercise 3.16 Give the Bellman equation for  $q_{*}$ for the recycling robot.

Exercise 3.17 Figure 3.8 gives the optimal value of the best state of the gridworld as 24.4, to one decimal place. Use your knowledge of the optimal policy and (3.2) to express this value symbolically, and then to compute it to three decimal places.

Exercise 3.18 Give a definition of  $v_{*}$ in terms of  $q_{*}$

Exercise 3.19 Give a definition of  $q_{*}$ in terms of  $v_{*}$

Exercise 3.20 Give a definition of  $\pi_{*}$ in terms of  $q_{*}$

Exercise 3.21 Give a definition of  $\pi_{*}$ in terms of  $v_{*}$

---



---

### Chapter 4

### Dynamic Programming

The term dynamic programming (DP) refers to a collection of algorithms that can be used to compute optimal policies given a perfect model of the environment as a Markov decision process (MDP). Classical DP algorithms are of limited utility in reinforcement learning both because of their assumption of a perfect model and because of their great computational expense, but they are still important theoretically. DP provides an essential foundation for the understanding of the methods presented in the rest of this book. In fact, all of these methods can be viewed as attempts to achieve much the same effect as DP, only with less computation and without assuming a perfect model of the environment.

Starting with this chapter, we usually assume that the environment is a finite MDP. That is, we assume that its state, action, and reward sets,  $\mathcal{S}$,  $\mathcal{A}(s)$, and  $\mathcal{R}$, for  $s \in \mathcal{S}$, are finite, and that its dynamics are given by a set of probabilities  $p(s', r | s, a)$, for all  $s \in \mathcal{S}$,  $a \in \mathcal{A}(s)$,  $r \in \mathcal{R}$, and  $s' \in \mathcal{S}^+$ ( $\mathcal{S}^+$ is  $\mathcal{S}$ plus a terminal state if the problem is episodic). Although DP ideas can be applied to problems with continuous state and action spaces, exact solutions are possible only in special cases. A common way of obtaining approximate solutions for tasks with continuous states and actions is to quantize the state and action spaces and then apply finite-state DP methods. The methods we explore in Chapter 9 are applicable to continuous problems and are a significant extension of that approach.

The key idea of DP, and of reinforcement learning generally, is the use of value functions to organize and structure the search for good policies. In this chapter we show how DP can be used to compute the value functions defined in Chapter 3. As discussed there, we can easily obtain optimal policies once we have found the optimal value functions.  $v_{*}$ or  $a_{*}$, which satisfy the Bellman

---

optimality equations:

$$
\begin{align*}\begin{array}{rcl}v_{*}(s)&=&\max_{a}\mathbb{E}[R_{t+1}+\gamma v_{*}(S_{t+1})\mid S_{t}=s,A_{t}=a]\\&=&\max_{a}\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{*}(s^{\prime})\Big]\end{array}\end{align*}   \tag*{(4.1)}
$$

or

$$
\begin{align*}\begin{array}{rcl}q_{*}(s,a)&=&\mathbb{E}\Big[R_{t+1}+\gamma\max_{a^{\prime}}q_{*}(S_{t+1},a^{\prime})\;\Big|\;S_{t}=s,A_{t}=a\Big]\\&=&\displaystyle\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma\max_{a^{\prime}}q_{*}(s^{\prime},a^{\prime})\Big],\end{array}\end{align*}   \tag*{(4.2)}
$$

for all  $s \in \mathcal{S}$,  $a \in \mathcal{A}(s)$, and  $s' \in \mathcal{S}^+$. As we shall see, DP algorithms are obtained by turning Bellman equations such as these into assignments, that is, into update rules for improving approximations of the desired value functions.

## 4.1 Policy Evaluation

First we consider how to compute the state-value function  $v_{\pi}$ for an arbitrary policy  $\pi$. This is called policy evaluation in the DP literature. We also refer to it as the prediction problem. Recall from Chapter 3 that, for all  $s \in \mathcal{S}$,

 
$$
\begin{array}{r l r}{v_{\pi}(s)}&{=}&{\mathbb{E}_{\pi}\big[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\cdots\big|\;S_{t}=s\big]}\end{array}
$$
 

$$
\begin{array}{r l}{=}&{{}\mathbb{E}_{\pi}[R_{t+1}+\gamma v_{\pi}(S_{t+1})|S_{t}=s]}\end{array}   \tag*{(4.3)}
$$

$$
\begin{array}{r l}{=}&{{}\displaystyle\sum_{a}\pi(a|s)\displaystyle\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{\pi}(s^{\prime})\Big],}\end{array}   \tag*{(4.4)}
$$

where  $\pi(a|s)$ is the probability of taking action  $a$ in state  $s$ under policy  $\pi$, and the expectations are subscripted by  $\pi$ to indicate that they are conditional on  $\pi$ being followed. The existence and uniqueness of  $v_{\pi}$ are guaranteed as long as either  $\gamma < 1$ or eventual termination is guaranteed from all states under the policy  $\pi$.

If the environment’s dynamics are completely known, then (4.4) is a system of  $|\mathcal{S}|$ simultaneous linear equations in  $|\mathcal{S}|$ unknowns (the  $v_{\pi}(s), s \in \mathcal{S}$). In principle, its solution is a straightforward, if tedious, computation. For our purposes, iterative solution methods are most suitable. Consider a sequence of approximate value functions  $v_0, v_1, v_2, \ldots$, each mapping  $S^+$ to  $\mathbb{R}$. The initial approximation,  $v_0$, is chosen arbitrarily (except that the terminal state, if any,

---

## 4.1. POLICY EVALUATION

must be given value 0), and each successive approximation is obtained by using the Bellman equation for  $v_{\pi}$ (3.12) as an update rule:

$$
\begin{array}{r c l}{v_{k+1}(s)}&{=}&{\mathbb{E}_{\pi}[R_{t+1}+\gamma v_{k}(S_{t+1})\mid S_{t}=s]}\\ {}&{=}&{\displaystyle\sum_{a}\pi(a|s)\displaystyle\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{k}(s^{\prime})\Big],}\\ \end{array}   \tag*{(4.5)}
$$

for all  $s \in \mathcal{S}$. Clearly,  $v_k = v_\pi$ is a fixed point for this update rule because the Bellman equation for  $v_\pi$ assures us of equality in this case. Indeed, the sequence  $\{v_k\}$ can be shown in general to converge to  $v_\pi$ as  $k \to \infty$ under the same conditions that guarantee the existence of  $v_\pi$. This algorithm is called iterative policy evaluation.

To produce each successive approximation,  $v_{k+1}$ from  $v_k$, iterative policy evaluation applies the same operation to each state s: it replaces the old value of s with a new value obtained from the old values of the successor states of s, and the expected immediate rewards, along all the one-step transitions possible under the policy being evaluated. We call this kind of operation a full backup. Each iteration of iterative policy evaluation backs up the value of every state once to produce the new approximate value function  $v_{k+1}$. There are several different kinds of full backups, depending on whether a state (as here) or a state-action pair is being backed up, and depending on the precise way the estimated values of the successor states are combined. All the backups done in DP algorithms are called full backups because they are based on all possible next states rather than on a sample next state. The nature of a backup can be expressed in an equation, as above, or in a backup diagram like those introduced in Chapter 3. For example, Figure 3.4a is the backup diagram corresponding to the full backup used in iterative policy evaluation.

To write a sequential computer program to implement iterative policy evaluation, as given by (4.5), you would have to use two arrays, one for the old values,  $v_k(s)$, and one for the new values,  $v_{k+1}(s)$. This way, the new values can be computed one by one from the old values without the old values being changed. Of course it is easier to use one array and update the values “in place,” that is, with each new backed-up value immediately overwriting the old one. Then, depending on the order in which the states are backed up, sometimes new values are used instead of old ones on the right-hand side of (4.5). This slightly different algorithm also converges to  $v_\pi$; in fact, it usually converges faster than the two-array version, as you might expect, since it uses new data as soon as they are available. We think of the backups as being done in a sweep through the state space. For the in-place algorithm, the order in which states are backed up during the sweep has a significant influence on the rate of convergence. We usually have the in-place version in mind when we think of DP algorithms.

---

Input $\pi$, the policy to be evaluated
Initialize an array $V(s) = 0$, for all $s \in \mathcal{S}^{+}$Repeat$\Delta \leftarrow 0$For each$s \in \mathcal{S}$:
$v \leftarrow V(s)$
$V(s) \leftarrow \sum_{a} \pi(a|s) \sum_{s',r} p(s', r|s, a) \big[ r + \gamma V(s') \big]$
$\Delta \leftarrow \max(\Delta, |v - V(s)|)$until$\Delta < \theta$(a small positive number)
Output$V \approx v_{\pi}$<div style="text-align: center;">Figure 4.1: Iterative policy evaluation.</div>

Another implementation point concerns the termination of the algorithm. Formally, iterative policy evaluation converges only in the limit, but in practice it must be halted short of this. A typical stopping condition for iterative policy evaluation is to test the quantity$ \max_{s \in \mathbb{S}} |v_{k+1}(s) - v_k(s)| $after each sweep and stop when it is sufficiently small. Figure 4.1 gives a complete algorithm for iterative policy evaluation with this stopping criterion.

Example 4.1 Consider the$ 4 \times 4 $gridworld shown below.

<div style="text-align: center;"><img src="imgs/img_in_image_box_354_856_863_1024.jpg" alt="Image" width="41%" /></div>

The nonterminal states are$ \mathcal{S} = \{1, 2, \ldots, 14\} $. There are four actions possible in each state,  $\mathcal{A} = \{up, down, right, left\}$, which deterministically cause the corresponding state transitions, except that actions that would take the agent off the grid in fact leave the state unchanged. Thus, for instance,  $p(6|5, \text{right}) = 1$,  $p(10|5, \text{right}) = 0$, and  $p(7|7, \text{right}) = 1$. This is an undiscounted, episodic task. The reward is -1 on all transitions until the terminal state is reached. The terminal state is shaded in the figure (although it is shown in two places, it is formally one state). The expected reward function is thus  $r(s, a, s') = -1$ for all states  $s, s'$ and actions  $a$. Suppose the agent follows the equiprobable random policy (all actions equally likely). The left side of Figure 4.2 shows the sequence of value functions  $\{v_k\}$ computed by iterative policy evaluation. The final estimate is in fact  $v_\pi$, which in this case gives for each state the negation of the expected number of steps from that state until

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_328_287_883_1134.jpg" alt="Image" width="45%" /></div>

<div style="text-align: center;">Figure 4.2: Convergence of iterative policy evaluation on a small gridworld. The left column is the sequence of approximations of the state-value function for the random policy (all actions equal). The right column is the sequence of greedy policies corresponding to the value function estimates (arrows are shown for all actions achieving the maximum). The last policy is guaranteed only to be an improvement over the random policy, but in this case it, and all policies after the third iteration, are optimal.</div>


---

termination.

## 4.2 Policy Improvement

Our reason for computing the value function for a policy is to help find better policies. Suppose we have determined the value function  $v_{\pi}$ for an arbitrary deterministic policy  $\pi$. For some state s we would like to know whether or not we should change the policy to deterministically choose an action  $a \neq \pi(s)$. We know how good it is to follow the current policy from s—that is  $v_{\pi}(s)$—but would it be better or worse to change to the new policy? One way to answer this question is to consider selecting a in s and thereafter following the existing policy,  $\pi$. The value of this way of behaving is

$$
\begin{array}{r c l}{q_{\pi}(s,a)}&{=}&{\mathbb{E}_{\pi}[R_{t+1}+\gamma v_{\pi}(S_{t+1})\mid S_{t}=s,A_{t}=a]}\\ {}&{=}&{\displaystyle\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{\pi}(s^{\prime})\Big].}\\ \end{array}   \tag*{(4.6)}
$$

The key criterion is whether this is greater than or less than  $v_{\pi}(s)$. If it is greater—that is, if it is better to select a once in s and thereafter follow  $\pi$ than it would be to follow  $\pi$ all the time—then one would expect it to be better still to select a every time s is encountered, and that the new policy would in fact be a better one overall.

That this is true is a special case of a general result called the policy improvement theorem. Let  $\pi$ and  $\pi'$ be any pair of deterministic policies such that, for all  $s \in \mathcal{S}$,

$$
q_{\pi}(s,\pi^{\prime}(s))\geq v_{\pi}(s).   \tag*{(4.7)}
$$

Then the policy  $\pi'$ must be as good as, or better than,  $\pi$. That is, it must obtain greater or equal expected return from all states  $s \in \mathcal{S}$:

$$
v_{\pi^{\prime}}(s)\geq v_{\pi}(s).   \tag*{(4.8)}
$$

Moreover, if there is strict inequality of (4.7) at any state, then there must be strict inequality of (4.8) at at least one state. This result applies in particular to the two policies that we considered in the previous paragraph, an original deterministic policy,  $\pi$, and a changed policy,  $\pi'$, that is identical to  $\pi$ except that  $\pi'(s) = a \neq \pi(s)$. Obviously, (4.7) holds at all states other than s. Thus, if  $q_{\pi}(s, a) > v_{\pi}(s)$, then the changed policy is indeed better than  $\pi$.

The idea behind the proof of the policy improvement theorem is easy to understand. Starting from (4.7), we keep expanding the  $q_{\pi}$ side and reapplying

---

## 4.2. POLICY IMPROVEMENT

(4.7) until we get vπ′(s):

 
$$
\begin{array}{rcl}v_{\pi}(s)&\leq&q_{\pi}(s,\pi^{\prime}(s))\\&=&\mathbb{E}_{\pi^{\prime}}[R_{t+1}+\gamma v_{\pi}(S_{t+1})\mid S_{t}=s]\\&\leq&\mathbb{E}_{\pi^{\prime}}[R_{t+1}+\gamma q_{\pi}(S_{t+1},\pi^{\prime}(S_{t+1}))\mid S_{t}=s]\\&=&\mathbb{E}_{\pi^{\prime}}[R_{t+1}+\gamma\mathbb{E}_{\pi^{\prime}}[R_{t+2}+\gamma v_{\pi}(S_{t+2})]\mid S_{t}=s]\\&=&\mathbb{E}_{\pi^{\prime}}\big[R_{t+1}+\gamma R_{t+2}+\gamma^{2}v_{\pi}(S_{t+2})\big\mid S_{t}=s\big]\\&\leq&\mathbb{E}_{\pi^{\prime}}\big[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\gamma^{3}v_{\pi}(S_{t+3})\big\mid S_{t}=s\big]\\&\vdots\\&\leq&\mathbb{E}_{\pi^{\prime}}\big[R_{t+1}+\gamma R_{t+2}+\gamma^{2}R_{t+3}+\gamma^{3}R_{t+4}+\cdots\big\mid S_{t}=s\big]\\&=&v_{\pi^{\prime}}(s).\end{array}
$$
 

So far we have seen how, given a policy and its value function, we can easily evaluate a change in the policy at a single state to a particular action. It is a natural extension to consider changes at all states and to all possible actions, selecting at each state the action that appears best according to  $q_{\pi}(s,a)$. In other words, to consider the new greedy policy,  $\pi'$, given by

$$
\begin{array}{rcl}\pi^{\prime}(s)&=&\underset{a}{\arg\max}q_{\pi}(s,a)\\&=&\underset{a}{\arg\max}\mathbb{E}[R_{t+1}+\gamma v_{\pi}(S_{t+1})\mid S_{t}=s,A_{t}=a]\\&=&\underset{a}{\arg\max}\displaystyle\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{\pi}(s^{\prime})\Big],\end{array}   \tag*{(4.9)}
$$

where  $\arg\max_{a}$ denotes the value of a at which the expression that follows is maximized (with ties broken arbitrarily). The greedy policy takes the action that looks best in the short term—after one step of lookahead—according to  $v_{\pi}$. By construction, the greedy policy meets the conditions of the policy improvement theorem (4.7), so we know that it is as good as, or better than, the original policy. The process of making a new policy that improves on an original policy, by making it greedy with respect to the value function of the original policy, is called policy improvement.

Suppose the new greedy policy,  $\pi'$, is as good as, but not better than, the old policy  $\pi$. Then  $v_{\pi} = v_{\pi'}$, and from (4.9) it follows that for all  $s \in \mathcal{S}$:

 
$$
\begin{align*}v_{\pi^{\prime}}(s)\quad&=\quad\max_{a}\mathbb{E}[R_{t+1}+\gamma v_{\pi^{\prime}}(S_{t+1})\mid S_{t}=s,A_{t}=a]\\&=\quad\max_{a}\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{\pi^{\prime}}(s^{\prime})\Big].\end{align*}
$$
 

---

But this is the same as the Bellman optimality equation (4.1), and therefore,  $v_{\pi'}$ must be  $v_*$, and both  $\pi$ and  $\pi'$ must be optimal policies. Policy improvement thus must give us a strictly better policy except when the original policy is already optimal.

So far in this section we have considered the special case of deterministic policies. In the general case, a stochastic policy  $\pi$ specifies probabilities,  $\pi(a|s)$, for taking each action, a, in each state, s. We will not go through the details, but in fact all the ideas of this section extend easily to stochastic policies. In particular, the policy improvement theorem carries through as stated for the stochastic case, under the natural definition:

 
$$
q_{\pi}(s,\pi^{\prime}(s))=\sum_{a}\pi^{\prime}(a|s)q_{\pi}(s,a).
$$
 

In addition, if there are ties in policy improvement steps such as  $(4.9)$—that is, if there are several actions at which the maximum is achieved—then in the stochastic case we need not select a single action from among them. Instead, each maximizing action can be given a portion of the probability of being selected in the new greedy policy. Any apportioning scheme is allowed as long as all submaximal actions are given zero probability.

The last row of Figure 4.2 shows an example of policy improvement for stochastic policies. Here the original policy,  $\pi$, is the equiprobable random policy, and the new policy,  $\pi'$, is greedy with respect to  $v_{\pi}$. The value function  $v_{\pi}$ is shown in the bottom-left diagram and the set of possible  $\pi'$ is shown in the bottom-right diagram. The states with multiple arrows in the  $\pi'$ diagram are those in which several actions achieve the maximum in (4.9); any apportionment of probability among these actions is permitted. The value function of any such policy,  $v_{\pi'}(s)$, can be seen by inspection to be either -1, -2, or -3 at all states,  $s \in S$, whereas  $v_{\pi}(s)$ is at most -14. Thus,  $v_{\pi'}(s) \geq v_{\pi}(s)$, for all  $s \in S$, illustrating policy improvement. Although in this case the new policy  $\pi'$ happens to be optimal, in general only an improvement is guaranteed.

## 4.3 Policy Iteration

Once a policy,  $\pi$, has been improved using  $v_{\pi}$ to yield a better policy,  $\pi'$, we can then compute  $v_{\pi'}$ and improve it again to yield an even better  $\pi''$. We can thus obtain a sequence of monotonically improving policies and value functions:

 
$$
\pi_{0}\stackrel{\mathrm{E}}{\longrightarrow}v_{\pi_{0}}\stackrel{\mathrm{I}}{\longrightarrow}\pi_{1}\stackrel{\mathrm{E}}{\longrightarrow}v_{\pi_{1}}\stackrel{\mathrm{I}}{\longrightarrow}\pi_{2}\stackrel{\mathrm{E}}{\longrightarrow}\cdots\stackrel{\mathrm{I}}{\longrightarrow}\pi_{*}\stackrel{\mathrm{E}}{\longrightarrow}v_{*},
$$
 

where  $\xrightarrow{E}$ denotes a policy evaluation and  $\xrightarrow{I}$ denotes a policy improvement. Each policy is guaranteed to be a strict improvement over the previous one

---

## 4.3. POLICY ITERATION

1. Initialization
 $V(s) \in \mathbb{R}$ and  $\pi(s) \in \mathcal{A}(s)$ arbitrarily for all  $s \in \mathcal{S}$

2. Policy Evaluation
Repeat
 $\Delta \leftarrow 0$
For each  $s \in \mathcal{S}$:
 $v \leftarrow V(s)$
 $V(s) \leftarrow \sum_{s', r} p(s', r | s, \pi(s)) [r + \gamma V(s')]$
 $\Delta \leftarrow \max(\Delta, |v - V(s)|)$
until  $\Delta < \theta$ (a small positive number)

3. Policy Improvement
policy-stable  $\leftarrow$ true
For each  $s \in \mathcal{S}$:
 $a \leftarrow \pi(s)$
 $\pi(s) \leftarrow \arg\max_a \sum_{s', r} p(s', r | s, a) [r + \gamma V(s')]$
If  $a \neq \pi(s)$, then policy-stable  $\leftarrow$ false
If policy-stable, then stop and return V and  $\pi$; else go to 2

<div style="text-align: center;">Figure 4.3: Policy iteration (using iterative policy evaluation) for  $v_{*}$. This algorithm has a subtle bug, in that it may never terminate if the policy continually switches between two or more policies that are equally good. The bug can be fixed by adding additional flags, but it makes the pseudocode so ugly that it is not worth it. :-)</div>

(unless it is already optimal). Because a finite MDP has only a finite number of policies, this process must converge to an optimal policy and optimal value function in a finite number of iterations.

This way of finding an optimal policy is called policy iteration. A complete algorithm is given in Figure 4.3. Note that each policy evaluation, itself an iterative computation, is started with the value function for the previous policy. This typically results in a great increase in the speed of convergence of policy evaluation (presumably because the value function changes little from one policy to the next).

Policy iteration often converges in surprisingly few iterations. This is illustrated by the example in Figure 4.2. The bottom-left diagram shows the value function for the equiprobable random policy, and the bottom-right diagram shows a greedy policy for this value function. The policy improvement theorem assures us that these policies are better than the original random policy. In this case, however, these policies are not just better, but optimal, proceed

---

ing to the terminal states in the minimum number of steps. In this example, policy iteration would find the optimal policy after just one iteration.

Example 4.2: Jack’s Car Rental Jack manages two locations for a nationwide car rental company. Each day, some number of customers arrive at each location to rent cars. If Jack has a car available, he rents it out and is credited $10 by the national company. If he is out of cars at that location, then the business is lost. Cars become available for renting the day after they are returned. To help ensure that cars are available where they are needed, Jack can move them between the two locations overnight, at a cost of $2 per car moved. We assume that the number of cars requested and returned at each location are Poisson random variables, meaning that the probability that the number is $n$is$\frac{\lambda^n}{n!}e^{-\lambda}$, where $\lambda$is the expected number. Suppose$\lambda$is 3 and 4 for rental requests at the first and second locations and 3 and 2 for returns. To simplify the problem slightly, we assume that there can be no more than 20 cars at each location (any additional cars are returned to the nationwide company, and thus disappear from the problem) and a maximum of five cars can be moved from one location to the other in one night. We take the discount rate to be$\gamma = 0.9$and formulate this as a continuing finite MDP, where the time steps are days, the state is the number of cars at each location at the end of the day, and the actions are the net numbers of cars moved between the two locations overnight. Figure 4.4 shows the sequence of policies found by policy iteration starting from the policy that never moves any cars.

## 4.4 Value Iteration

One drawback to policy iteration is that each of its iterations involves policy evaluation, which may itself be a protracted iterative computation requiring multiple sweeps through the state set. If policy evaluation is done iteratively, then convergence exactly to$ v_{\pi} $ occurs only in the limit. Must we wait for exact convergence, or can we stop short of that? The example in Figure 4.2 certainly suggests that it may be possible to truncate policy evaluation. In that example, policy evaluation iterations beyond the first three have no effect on the corresponding greedy policy.

In fact, the policy evaluation step of policy iteration can be truncated in several ways without losing the convergence guarantees of policy iteration. One important special case is when policy evaluation is stopped after just one sweep (one backup of each state). This algorithm is called value iteration. It can be written as a particularly simple backup operation that combines the

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_246_473_961_969.jpg" alt="Image" width="58%" /></div>

<div style="text-align: center;">Figure 4.4: The sequence of policies found by policy iteration on Jack’s car rental problem, and the final state-value function. The first five diagrams show, for each number of cars at each location at the end of the day, the number of cars to be moved from the first location to the second (negative numbers indicate transfers from the second location to the first). Each successive policy is a strict improvement over the previous policy, and the last policy is optimal.</div>


---

policy improvement and truncated policy evaluation steps:

$$
\begin{align*}\begin{array}{rcl}v_{k+1}(s)&=&\max\limits_{a}\mathbb{E}[R_{t+1}+\gamma v_{k}(S_{t+1})\mid S_{t}=s,A_{t}=a]\\&=&\max\limits_{a}\sum\limits_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{k}(s^{\prime})\Big],\end{array}\end{align*}   \tag*{(4.10)}
$$

for all $s \in \mathcal{S}$. For arbitrary $v_0$, the sequence $\{v_k\}$can be shown to converge to$v_*$under the same conditions that guarantee the existence of$v_*.$Another way of understanding value iteration is by reference to the Bellman optimality equation (4.1). Note that value iteration is obtained simply by turning the Bellman optimality equation into an update rule. Also note how the value iteration backup is identical to the policy evaluation backup (4.5) except that it requires the maximum to be taken over all actions. Another way of seeing this close relationship is to compare the backup diagrams for these algorithms: Figure 3.4a shows the backup diagram for policy evaluation and Figure 3.7a shows the backup diagram for value iteration. These two are the natural backup operations for computing$ v_{\pi} $and$ v_{*} $.

Finally, let us consider how value iteration terminates. Like policy evaluation, value iteration formally requires an infinite number of iterations to converge exactly to  $v_{*}$. In practice, we stop once the value function changes by only a small amount in a sweep. Figure 4.5 gives a complete value iteration algorithm with this kind of termination condition.

Value iteration effectively combines, in each of its sweeps, one sweep of policy evaluation and one sweep of policy improvement. Faster convergence is often achieved by interposing multiple policy evaluation sweeps between each policy improvement sweep. In general, the entire class of truncated policy iteration algorithms can be thought of as sequences of sweeps, some of which use policy evaluation backups and some of which use value iteration backups. Since the max operation in (4.10) is the only difference between these backups, this just means that the max operation is added to some sweeps of policy evaluation. All of these algorithms converge to an optimal policy for discounted finite MDPs.

Example 4.3: Gambler’s Problem A gambler has the opportunity to make bets on the outcomes of a sequence of coin flips. If the coin comes up heads, he wins as many dollars as he has staked on that flip; if it is tails, he loses his stake. The game ends when the gambler wins by reaching his goal of 100, or loses by running out of money. On each flip, the gambler must decide what portion of his capital to stake, in integer numbers of dollars. This problem can be formulated as an undiscounted, episodic, finite MDP. The state is the gambler’s capital,  $s \in \{1, 2, \ldots, 99\}$ and the actions are stakes,

---

Initialize array V arbitrarily (e.g.,  $V(s) = 0$ for all  $s \in \mathcal{S}^{+}$)

Repeat
 $\Delta \leftarrow 0$

For each  $s \in \mathcal{S}$:
     $v \leftarrow V(s)$
     $V(s) \leftarrow \max_a \sum_{s', r} p(s', r | s, a) [r + \gamma V(s')]$
     $\Delta \leftarrow \max(\Delta, |v - V(s)|)$
until  $\Delta < \theta$ (a small positive number)

Output a deterministic policy,  $\pi$, such that
 $\pi(s) = \arg\max_a \sum_{s', r} p(s', r | s, a) [r + \gamma V(s')]$

<div style="text-align: center;">Figure 4.5: Value iteration.</div>

$a \in \{0, 1, \ldots, \min(s, 100 - s)\}$. The reward is zero on all transitions except those on which the gambler reaches his goal, when it is +1. The state-value function then gives the probability of winning from each state. A policy is a mapping from levels of capital to stakes. The optimal policy maximizes the probability of reaching the goal. Let $p_h$denote the probability of the coin coming up heads. If$p_h$is known, then the entire problem is known and it can be solved, for instance, by value iteration. Figure 4.6 shows the change in the value function over successive sweeps of value iteration, and the final policy found, for the case of$p_h = 0.4$. This policy is optimal, but not unique. In fact, there is a whole family of optimal policies, all corresponding to ties for the argmax action selection with respect to the optimal value function. Can you guess what the entire family looks like?

## 4.5 Asynchronous Dynamic Programming

A major drawback to the DP methods that we have discussed so far is that they involve operations over the entire state set of the MDP, that is, they require sweeps of the state set. If the state set is very large, then even a single sweep can be prohibitively expensive. For example, the game of backgammon has over  $10^{20}$ states. Even if we could perform the value iteration backup on a million states per second, it would take over a thousand years to complete a single sweep.

Asynchronous DP algorithms are in-place iterative DP algorithms that are not organized in terms of systematic sweeps of the state set. These algorithms back up the values of states in any order whatsoever, using whatever values of

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_269_415_939_797.jpg" alt="Image" width="54%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_294_873_949_1110.jpg" alt="Image" width="53%" /></div>

<div style="text-align: center;">Figure 4.6: The solution to the gambler's problem for  $p_{h} = 0.4$. The upper graph shows the value function found by successive sweeps of value iteration. The lower graph shows the final policy.</div>


---

other states happen to be available. The values of some states may be backed up several times before the values of others are backed up once. To converge correctly, however, an asynchronous algorithm must continue to backup the values of all the states: it can't ignore any state after some point in the computation. Asynchronous DP algorithms allow great flexibility in selecting states to which backup operations are applied.

For example, one version of asynchronous value iteration backs up the value, in place, of only one state,  $s_k$, on each step,  $k$, using the value iteration backup (4.10). If  $0 \leq \gamma < 1$, asymptotic convergence to  $v_*$ is guaranteed given only that all states occur in the sequence  $\{s_k\}$ an infinite number of times (the sequence could even be stochastic). (In the undiscounted episodic case, it is possible that there are some orderings of backups that do not result in convergence, but it is relatively easy to avoid these.) Similarly, it is possible to intermix policy evaluation and value iteration backups to produce a kind of asynchronous truncated policy iteration. Although the details of this and other more unusual DP algorithms are beyond the scope of this book, it is clear that a few different backups form building blocks that can be used flexibly in a wide variety of sweepless DP algorithms.

Of course, avoiding sweeps does not necessarily mean that we can get away with less computation. It just means that an algorithm does not need to get locked into any hopelessly long sweep before it can make progress improving a policy. We can try to take advantage of this flexibility by selecting the states to which we apply backups so as to improve the algorithm's rate of progress. We can try to order the backups to let value information propagate from state to state in an efficient way. Some states may not need their values backed up as often as others. We might even try to skip backing up some states entirely if they are not relevant to optimal behavior. Some ideas for doing this are discussed in Chapter 8.

Asynchronous algorithms also make it easier to intermix computation with real-time interaction. To solve a given MDP, we can run an iterative DP algorithm at the same time that an agent is actually experiencing the MDP. The agent's experience can be used to determine the states to which the DP algorithm applies its backups. At the same time, the latest value and policy information from the DP algorithm can guide the agent's decision-making. For example, we can apply backups to states as the agent visits them. This makes it possible to focus the DP algorithm's backups onto parts of the state set that are most relevant to the agent. This kind of focusing is a repeated theme in reinforcement learning.

---

## 4.6 Generalized Policy Iteration

Policy iteration consists of two simultaneous, interacting processes, one making the value function consistent with the current policy (policy evaluation), and the other making the policy greedy with respect to the current value function (policy improvement). In policy iteration, these two processes alternate, each completing before the other begins, but this is not really necessary. In value iteration, for example, only a single iteration of policy evaluation is performed in between each policy improvement. In asynchronous DP methods, the evaluation and improvement processes are interleaved at an even finer grain. In some cases a single state is updated in one process before returning to the other. As long as both processes continue to update all states, the ultimate result is typically the same—convergence to the optimal value function and an optimal policy.

We use the term generalized policy iteration (GPI) to refer to the general idea of letting policy evaluation and policy improvement processes interact, independent of the granularity and other details of the two processes. Almost all reinforcement learning methods are well described as GPI. That is, all have identifiable policies and value functions, with the policy always being improved with respect to the value function and the value function always being driven toward the value function for the policy. This overall schema for GPI is illustrated in Figure 4.7.

It is easy to see that if both the evaluation process and the improvement process stabilize, that is, no longer produce changes, then the value function and policy must be optimal. The value function stabilizes only when it is consistent with the current policy, and the policy stabilizes only when it is greedy with respect to the current value function. Thus, both processes stabilize only when a policy has been found that is greedy with respect to its own evaluation function. This implies that the Bellman optimality equation (4.1) holds, and thus that the policy and the value function are optimal.

The evaluation and improvement processes in GPI can be viewed as both competing and cooperating. They compete in the sense that they pull in opposing directions. Making the policy greedy with respect to the value function typically makes the value function incorrect for the changed policy, and making the value function consistent with the policy typically causes that policy no longer to be greedy. In the long run, however, these two processes interact to find a single joint solution: the optimal value function and an optimal policy.

One might also think of the interaction between the evaluation and improvement processes in GPI in terms of two constraints or goals—for example, as two lines in two-dimensional space:

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_469_219_751_671.jpg" alt="Image" width="23%" /></div>

<div style="text-align: center;">Figure 4.7: Generalized policy iteration: Value and policy functions interact until they are optimal and thus consistent with each other.</div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_371_842_852_1114.jpg" alt="Image" width="39%" /></div>

Although the real geometry is much more complicated than this, the diagram suggests what happens in the real case. Each process drives the value function or policy toward one of the lines representing a solution to one of the two goals. The goals interact because the two lines are not orthogonal. Driving directly toward one goal causes some movement away from the other goal. Inevitably, however, the joint process is brought closer to the overall goal of optimality. The arrows in this diagram correspond to the behavior of policy iteration in that each takes the system all the way to achieving one of the two goals completely. In GPI one could also take smaller, incomplete steps toward each goal. In either case, the two processes together achieve the overall goal.

---

of optimality even though neither is attempting to achieve it directly.

## 4.7 Efficiency of Dynamic Programming

DP may not be practical for very large problems, but compared with other methods for solving MDPs, DP methods are actually quite efficient. If we ignore a few technical details, then the (worst case) time DP methods take to find an optimal policy is polynomial in the number of states and actions. If n and m denote the number of states and actions, this means that a DP method takes a number of computational operations that is less than some polynomial function of n and m. A DP method is guaranteed to find an optimal policy in polynomial time even though the total number of (deterministic) policies is  $m^{n}$. In this sense, DP is exponentially faster than any direct search in policy space could be, because direct search would have to exhaustively examine each policy to provide the same guarantee. Linear programming methods can also be used to solve MDPs, and in some cases their worst-case convergence guarantees are better than those of DP methods. But linear programming methods become impractical at a much smaller number of states than do DP methods (by a factor of about 100). For the largest problems, only DP methods are feasible.

DP is sometimes thought to be of limited applicability because of the curse of dimensionality (Bellman, 1957a), the fact that the number of states often grows exponentially with the number of state variables. Large state sets do create difficulties, but these are inherent difficulties of the problem, not of DP as a solution method. In fact, DP is comparatively better suited to handling large state spaces than competing methods such as direct search and linear programming.

In practice, DP methods can be used with today's computers to solve MDPs with millions of states. Both policy iteration and value iteration are widely used, and it is not clear which, if either, is better in general. In practice, these methods usually converge much faster than their theoretical worst-case run times, particularly if they are started with good initial value functions or policies.

On problems with large state spaces, asynchronous DP methods are often preferred. To complete even one sweep of a synchronous method requires computation and memory for every state. For some problems, even this much memory and computation is impractical, yet the problem is still potentially solvable because only a relatively few states occur along optimal solution trajectories. Asynchronous methods and other variations of GPI can be applied in such cases and may find good or optimal policies much faster than synchronous.

---

methods can.

## 4.8 Summary

In this chapter we have become familiar with the basic ideas and algorithms of dynamic programming as they relate to solving finite MDPs. Policy evaluation refers to the (typically) iterative computation of the value functions for a given policy. Policy improvement refers to the computation of an improved policy given the value function for that policy. Putting these two computations together, we obtain policy iteration and value iteration, the two most popular DP methods. Either of these can be used to reliably compute optimal policies and value functions for finite MDPs given complete knowledge of the MDP.

Classical DP methods operate in sweeps through the state set, performing a full backup operation on each state. Each backup updates the value of one state based on the values of all possible successor states and their probabilities of occurring. Full backups are closely related to Bellman equations: they are little more than these equations turned into assignment statements. When the backups no longer result in any changes in value, convergence has occurred to values that satisfy the corresponding Bellman equation. Just as there are four primary value functions  $(v_{\pi}, v_{*}, q_{\pi}, \text{ and } q_{*})$, there are four corresponding Bellman equations and four corresponding full backups. An intuitive view of the operation of backups is given by backup diagrams.

Insight into DP methods and, in fact, into almost all reinforcement learning methods, can be gained by viewing them as generalized policy iteration (GPI). GPI is the general idea of two interacting processes revolving around an approximate policy and an approximate value function. One process takes the policy as given and performs some form of policy evaluation, changing the value function to be more like the true value function for the policy. The other process takes the value function as given and performs some form of policy improvement, changing the policy to make it better, assuming that the value function is its value function. Although each process changes the basis for the other, overall they work together to find a joint solution: a policy and value function that are unchanged by either process and, consequently, are optimal. In some cases, GPI can be proved to converge, most notably for the classical DP methods that we have presented in this chapter. In other cases convergence has not been proved, but still the idea of GPI improves our understanding of the methods.

It is not necessary to perform DP methods in complete sweeps through the state set. Asynchronous DP methods are in-place iterative methods that back

---

up states in an arbitrary order, perhaps stochastically determined and using out-of-date information. Many of these methods can be viewed as fine-grained forms of GPI.

Finally, we note one last special property of DP methods. All of them update estimates of the values of states based on estimates of the values of successor states. That is, they update estimates on the basis of other estimates. We call this general idea bootstrapping. Many reinforcement learning methods perform bootstrapping, even those that do not require, as DP requires, a complete and accurate model of the environment. In the next chapter we explore reinforcement learning methods that do not require a model and do not bootstrap. In the chapter after that we explore methods that do not require a model but do bootstrap. These key features and properties are separable, yet can be mixed in interesting combinations.

#### Bibliographical and Historical Remarks

The term “dynamic programming” is due to Bellman (1957a), who showed how these methods could be applied to a wide range of problems. Extensive treatments of DP can be found in many texts, including Bertsekas (1995), Bertsekas and Tsitsiklis (1996), Dreyfus and Law (1977), Ross (1983), White (1969), and Whittle (1982, 1983). Our interest in DP is restricted to its use in solving MDPs, but DP also applies to other types of problems. Kumar and Kanal (1988) provide a more general look at DP.

To the best of our knowledge, the first connection between DP and reinforcement learning was made by Minsky (1961) in commenting on Samuel's checkers player. In a footnote, Minsky mentioned that it is possible to apply DP to problems in which Samuel's backing-up process can be handled in closed analytic form. This remark may have misled artificial intelligence researchers into believing that DP was restricted to analytically tractable problems and therefore largely irrelevant to artificial intelligence. Andreae (1969b) mentioned DP in the context of reinforcement learning, specifically policy iteration, although he did not make specific connections between DP and learning algorithms. Werbos (1977) suggested an approach to approximating DP called "heuristic dynamic programming" that emphasizes gradient-descent methods for continuous-state problems (Werbos, 1982, 1987, 1988, 1989, 1992). These methods are closely related to the reinforcement learning algorithms that we discuss in this book. Watkins (1989) was explicit in connecting reinforcement learning to DP, characterizing a class of reinforcement learning methods as "incremental dynamic programming."

---

4.1–4 These sections describe well-established DP algorithms that are covered in any of the general DP references cited above. The policy improvement theorem and the policy iteration algorithm are due to Bellman (1957a) and Howard (1960). Our presentation was influenced by the local view of policy improvement taken by Watkins (1989). Our discussion of value iteration as a form of truncated policy iteration is based on the approach of Puterman and Shin (1978), who presented a class of algorithms called modified policy iteration, which includes policy iteration and value iteration as special cases. An analysis showing how value iteration can be made to find an optimal policy in finite time is given by Bertsekas (1987).

Iterative policy evaluation is an example of a classical successive approximation algorithm for solving a system of linear equations. The version of the algorithm that uses two arrays, one holding the old values while the other is updated, is often called a Jacobi-style algorithm, after Jacobi's classical use of this method. It is also sometimes called a synchronous algorithm because it can be performed in parallel, with separate processors simultaneously updating the values of individual states using input from other processors. The second array is needed to simulate this parallel computation sequentially. The in-place version of the algorithm is often called a Gauss–Seidel-style algorithm after the classical Gauss–Seidel algorithm for solving systems of linear equations. In addition to iterative policy evaluation, other DP algorithms can be implemented in these different versions. Bertsekas and Tsitsiklis (1989) provide excellent coverage of these variations and their performance differences.

4.5 Asynchronous DP algorithms are due to Bertsekas (1982, 1983), who also called them distributed DP algorithms. The original motivation for asynchronous DP was its implementation on a multiprocessor system with communication delays between processors and no global synchronizing clock. These algorithms are extensively discussed by Bertsekas and Tsitsiklis (1989). Jacobi-style and Gauss-Seidel-style DP algorithms are special cases of the asynchronous version. Williams and Baird (1990) presented DP algorithms that are asynchronous at a finer grain than the ones we have discussed: the backup operations themselves are broken into steps that can be performed asynchronously.

4.7 This section, written with the help of Michael Littman, is based on Littman, Dean, and Kaelbling (1995).

---

#### Exercises

Exercise 4.1 If  $\pi$ is the equiprobable random policy, what is  $q_{\pi}(11, down)$? What is  $q_{\pi}(7, down)$?

Exercise 4.2 Suppose a new state 15 is added to the gridworld just below state 13, and its actions, left, up, right, and down, take the agent to states 12, 13, 14, and 15, respectively. Assume that the transitions from the original states are unchanged. What, then, is  $v_{\pi}(15)$ for the equiprobable random policy? Now suppose the dynamics of state 13 are also changed, such that action down from state 13 takes the agent to the new state 15. What is  $v_{\pi}(15)$ for the equiprobable random policy in this case?

Exercise 4.3 What are the equations analogous to (4.3), (4.4), and (4.5) for the action-value function  $q_{\pi}$ and its successive approximation by a sequence of functions  $q_{0}, q_{1}, q_{2}, \ldots$?

Exercise 4.4 In some undiscounted episodic tasks there may be policies for which eventual termination is not guaranteed. For example, in the grid problem above it is possible to go back and forth between two states forever. In a task that is otherwise perfectly sensible,  $v_{\pi}(s)$ may be negative infinity for some policies and states, in which case the algorithm for iterative policy evaluation given in Figure 4.1 will not terminate. As a purely practical matter, how might we amend this algorithm to assure termination even in this case? Assume that eventual termination is guaranteed under the optimal policy.

Exercise 4.5 (programming) Write a program for policy iteration and re-solve Jack's car rental problem with the following changes. One of Jack's employees at the first location rides a bus home each night and lives near the second location. She is happy to shuttle one car to the second location for free. Each additional car still costs $2, as do all cars moved in the other direction. In addition, Jack has limited parking space at each location. If more than 10 cars are kept overnight at a location (after any moving of cars), then an additional cost of $4 must be incurred to use a second parking lot (independent of how many cars are kept there). These sorts of nonlinearities and arbitrary dynamics often occur in real problems and cannot easily be handled by optimization methods other than dynamic programming. To check your program, first replicate the results given for the original problem. If your computer is too slow for the full problem, cut all the numbers of cars in half.

Exercise 4.6 How would policy iteration be defined for action values? Give a complete algorithm for computing  $q_{*}$, analogous to Figure 4.3 for computing  $v_{*}$. Please pay special attention to this exercise, because the ideas involved will be used throughout the rest of the book.

---

Exercise 4.7 Suppose you are restricted to considering only policies that are  $\epsilon$-soft, meaning that the probability of selecting each action in each state, s, is at least  $\epsilon/|\mathcal{A}(s)|$. Describe qualitatively the changes that would be required in each of the steps 3, 2, and 1, in that order, of the policy iteration algorithm for  $v_*(Figure\ 4.3)$.

Exercise 4.8 Why does the optimal policy for the gambler’s problem have such a curious form? In particular, for capital of 50 it bets it all on one flip, but for capital of 51 it does not. Why is this a good policy?

Exercise 4.9 (programming) Implement value iteration for the gambler's problem and solve it for  $p_h = 0.25$ and  $p_h = 0.55$. In programming, you may find it convenient to introduce two dummy states corresponding to termination with capital of 0 and 100, giving them values of 0 and 1 respectively. Show your results graphically, as in Figure 4.6. Are your results stable as  $\theta \to 0$?

Exercise 4.10 What is the analog of the value iteration backup (4.10) for action values,  $q_{k+1}(s, a)$?

---



---

### Chapter 5

### Monte Carlo Methods

In this chapter we consider our first learning methods for estimating value functions and discovering optimal policies. Unlike the previous chapter, here we do not assume complete knowledge of the environment. Monte Carlo methods require only experience—sample sequences of states, actions, and rewards from actual or simulated interaction with an environment. Learning from actual experience is striking because it requires no prior knowledge of the environment's dynamics, yet can still attain optimal behavior. Learning from simulated experience is also powerful. Although a model is required, the model need only generate sample transitions, not the complete probability distributions of all possible transitions that is required for dynamic programming (DP). In surprisingly many cases it is easy to generate experience sampled according to the desired probability distributions, but infeasible to obtain the distributions in explicit form.

Monte Carlo methods are ways of solving the reinforcement learning problem based on averaging sample returns. To ensure that well-defined returns are available, here we define Monte Carlo methods only for episodic tasks. That is, we assume experience is divided into episodes, and that all episodes eventually terminate no matter what actions are selected. Only on the completion of an episode are value estimates and policies changed. Monte Carlo methods can thus be incremental in an episode-by-episode sense, but not in a step-by-step (online) sense. The term “Monte Carlo” is often used more broadly for any estimation method whose operation involves a significant random component. Here we use it specifically for methods based on averaging complete returns (as opposed to methods that learn from partial returns, considered in the next chapter).

Monte Carlo methods sample and average returns for each state–action pair much like the bandit methods we explored in Chapter 2 sample and average

---

rewards for each action. The main difference is that now there are multiple states, each acting like a different bandit problem (like an associative-search or contextual bandit) and that the different bandit problems are interrelated. That is, the return after taking an action in one state depends on the actions taken in later states in the same episode. Because all the action selections are undergoing learning, the problem becomes nonstationary from the point of view of the earlier state.

To handle the nonstationarity, we adapt the idea of general policy iteration (GPI) developed in Chapter 4 for DP. Whereas there we computed value functions from knowledge of the MDP, here we learn value functions from sample returns with the MDP. The value functions and corresponding policies still interact to attain optimality in essentially the same way (GPI). As in the DP chapter, first we consider the prediction problem (the computation of  $v_{\pi}$ and  $q_{\pi}$ for a fixed arbitrary policy  $\pi$) then policy improvement, and, finally, the control problem and its solution by GPI. Each of these ideas taken from DP is extended to the Monte Carlo case in which only sample experience is available.

## 5.1 Monte Carlo Prediction

We begin by considering Monte Carlo methods for learning the state-value function for a given policy. Recall that the value of a state is the expected return—expected cumulative future discounted reward—starting from that state. An obvious way to estimate it from experience, then, is simply to average the returns observed after visits to that state. As more returns are observed, the average should converge to the expected value. This idea underlies all Monte Carlo methods.

In particular, suppose we wish to estimate  $v_{\pi}(s)$, the value of a state s under policy  $\pi$, given a set of episodes obtained by following  $\pi$ and passing through s. Each occurrence of state s in an episode is called a visit to s. Of course, s may be visited multiple times in the same episode; let us call the first time it is visited in an episode the first visit to s. The first-visit MC method estimates  $v_{\pi}(s)$ as the average of the returns following first visits to s, whereas the every-visit MC method averages the returns following all visits to s. These two Monte Carlo (MC) methods are very similar but have slightly different theoretical properties. First-visit MC has been most widely studied, dating back to the 1940s, and is the one we focus on in this chapter. Every-visit MC extends more naturally to function approximation and eligibility traces, as discussed in Chapters 9 and 7. First-visit MC is shown in procedural form in Figure 5.1.

---

Initialize:
 $\pi \leftarrow$ policy to be evaluated
 $V \leftarrow$ an arbitrary state-value function
 $Returns(s) \leftarrow$ an empty list, for all  $s \in S$

Repeat forever:
Generate an episode using  $\pi$
For each state s appearing in the episode:
 $G \leftarrow$ return following the first occurrence of s
Append  $G$ to  $Returns(s)$
 $V(s) \leftarrow$ average( $Returns(s)$)

<div style="text-align: center;">Figure 5.1: The first-visit MC method for estimating  $v_{\pi}$. Note that we use a capital letter V for the approximate value function because, after initialization, it soon becomes a random variable.</div>

Both first-visit MC and every-visit MC converge to  $v_{\pi}(s)$ as the number of visits (or first visits) to s goes to infinity. This is easy to see for the case of first-visit MC. In this case each return is an independent, identically distributed estimate of  $v_{\pi}(s)$ with finite variance. By the law of large numbers the sequence of averages of these estimates converges to their expected value. Each average is itself an unbiased estimate, and the standard deviation of its error falls as  $1/\sqrt{n}$, where n is the number of returns averaged. Every-visit MC is less straightforward, but its estimates also converge asymptotically to  $v_{\pi}(s)$ (Singh and Sutton, 1996).

The use of Monte Carlo methods is best illustrated through an example.

Example 5.1: Blackjack The object of the popular casino card game of blackjack is to obtain cards the sum of whose numerical values is as great as possible without exceeding 21. All face cards count as 10, and an ace can count either as 1 or as 11. We consider the version in which each player competes independently against the dealer. The game begins with two cards dealt to both dealer and player. One of the dealer's cards is face up and the other is face down. If the player has 21 immediately (an ace and a 10-card), it is called a natural. He then wins unless the dealer also has a natural, in which case the game is a draw. If the player does not have a natural, then he can request additional cards, one by one (hits), until he either stops (sticks) or exceeds 21 (goes bust). If he goes bust, he loses; if he sticks, then it becomes the dealer's turn. The dealer hits or sticks according to a fixed strategy without choice: he sticks on any sum of 17 or greater, and hits otherwise. If the dealer goes bust, then the player wins; otherwise, the outcome—win, lose, or draw—is determined by whose final sum is closer to 21.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_312_205_899_600.jpg" alt="Image" width="47%" /></div>

<div style="text-align: center;">Figure 5.2: Approximate state-value functions for the blackjack policy that sticks only on 20 or 21, computed by Monte Carlo policy evaluation.</div>

Playing blackjack is naturally formulated as an episodic finite MDP. Each game of blackjack is an episode. Rewards of +1, -1, and 0 are given for winning, losing, and drawing, respectively. All rewards within a game are zero, and we do not discount ( $\gamma = 1$); therefore these terminal rewards are also the returns. The player's actions are to hit or to stick. The states depend on the player's cards and the dealer's showing card. We assume that cards are dealt from an infinite deck (i.e., with replacement) so that there is no advantage to keeping track of the cards already dealt. If the player holds an ace that he could count as 11 without going bust, then the ace is said to be usable. In this case it is always counted as 11 because counting it as 1 would make the sum 11 or less, in which case there is no decision to be made because, obviously, the player should always hit. Thus, the player makes decisions on the basis of three variables: his current sum (12–21), the dealer's one showing card (ace–10), and whether or not he holds a usable ace. This makes for a total of 200 states.

Consider the policy that sticks if the player’s sum is 20 or 21, and otherwise hits. To find the state-value function for this policy by a Monte Carlo approach, one simulates many blackjack games using the policy and averages the returns following each state. Note that in this task the same state never recurs within one episode, so there is no difference between first-visit and every-visit MC methods. In this way, we obtained the estimates of the state-value function shown in Figure 5.2. The estimates for states with a usable ace are less certain and less regular because these states are less common. In any event, after 500,000 games the value function is very well approximated.

---

## 5.1. MONTE CARLO PREDICTION

Although we have complete knowledge of the environment in this task, it would not be easy to apply DP methods to compute the value function. DP methods require the distribution of next events—in particular, they require the quantities  $p(s', r|s, a)$—and it is not easy to determine these for blackjack. For example, suppose the player's sum is 14 and he chooses to stick. What is his expected reward as a function of the dealer's showing card? All of these expected rewards and transition probabilities must be computed before DP can be applied, and such computations are often complex and error-prone. In contrast, generating the sample games required by Monte Carlo methods is easy. This is the case surprisingly often; the ability of Monte Carlo methods to work with sample episodes alone can be a significant advantage even when one has complete knowledge of the environment's dynamics.

Can we generalize the idea of backup diagrams to Monte Carlo algorithms? The general idea of a backup diagram is to show at the top the root node to be updated and to show below all the transitions and leaf nodes whose rewards and estimated values contribute to the update. For Monte Carlo estimation of  $v_{\pi}$, the root is a state node, and below it is the entire trajectory of transitions along a particular single episode, ending at the terminal state, as in Figure 5.3. Whereas the DP diagram (Figure 3.4a) shows all possible transitions, the Monte Carlo diagram shows only those sampled on the one episode. Whereas the DP diagram includes only one-step transitions, the Monte Carlo diagram goes all the way to the end of the episode. These differences in the diagrams accurately reflect the fundamental differences between the algorithms.

An important fact about Monte Carlo methods is that the estimates for each state are independent. The estimate for one state does not build upon the estimate of any other state, as is the case in DP. In other words, Monte Carlo methods do not bootstrap as we defined it in the previous chapter.

In particular, note that the computational expense of estimating the value of a single state is independent of the number of states. This can make Monte Carlo methods particularly attractive when one requires the value of only one or a subset of states. One can generate many sample episodes starting from the states of interest, averaging returns from only these states ignoring all others. This is a third advantage Monte Carlo methods can have over DP methods (after the ability to learn from actual experience and from simulated experience).

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_213_199_973_610.jpg" alt="Image" width="62%" /></div>

<div style="text-align: center;">Figure 5.3: The backup diagram for Monte Carlo estimation of  $v_{\pi}$.</div>

##### Example 5.2: Soap Bubble

Suppose a wire frame forming a closed loop is dunked in soapy water to form a soap surface or bubble conforming at its edges to the wire frame. If the geometry of the wire frame is irregular but known, how can you compute the shape of the surface? The shape has the property that the total force on each point exerted by neighboring points is zero (or else the shape would change). This means that the surface's

<div style="text-align: center;"><img src="imgs/img_in_image_box_658_740_1008_994.jpg" alt="Image" width="28%" /></div>

<div style="text-align: center;">A bubble on a wire loop</div>

height at any point is the average of its heights at points in a small circle around that point. In addition, the surface must meet at its boundaries with the wire frame. The usual approach to problems of this kind is to put a grid over the area covered by the surface and solve for its height at the grid points by an iterative computation. Grid points at the boundary are forced to the wire frame, and all others are adjusted toward the average of the heights of their four nearest neighbors. This process then iterates, much like DP's iterative policy evaluation, and ultimately converges to a close approximation to the desired surface.

This is similar to the kind of problem for which Monte Carlo methods were originally designed. Instead of the iterative computation described above, imagine standing on the surface and taking a random walk, stepping randomly from grid point to neighboring grid point, with equal probability, until you

---

reach the boundary. It turns out that the expected value of the height at the boundary is a close approximation to the height of the desired surface at the starting point (in fact, it is exactly the value computed by the iterative method described above). Thus, one can closely approximate the height of the surface at a point by simply averaging the boundary heights of many walks started at the point. If one is interested in only the value at one point, or any fixed small set of points, then this Monte Carlo method can be far more efficient than the iterative method based on local consistency.

## 5.2 Monte Carlo Estimation of Action Values

If a model is not available, then it is particularly useful to estimate action values (the values of state-action pairs) rather than state values. With a model, state values alone are sufficient to determine a policy; one simply looks ahead one step and chooses whichever action leads to the best combination of reward and next state, as we did in the chapter on DP. Without a model, however, state values alone are not sufficient. One must explicitly estimate the value of each action in order for the values to be useful in suggesting a policy. Thus, one of our primary goals for Monte Carlo methods is to estimate  $q_{*}$. To achieve this, we first consider the policy evaluation problem for action values.

The policy evaluation problem for action values is to estimate  $q_{\pi}(s,a)$, the expected return when starting in state s, taking action a, and thereafter following policy  $\pi$. The Monte Carlo methods for this are essentially the same as just presented for state values, except now we talk about visits to a state-action pair rather than to a state. A state-action pair s, a is said to be visited in an episode if ever the state s is visited and action a is taken in it. The every-visit MC method estimates the value of a state-action pair as the average of the returns that have followed visits all the visits to it. The first-visit MC method averages the returns following the first time in each episode that the state was visited and the action was selected. These methods converge quadratically, as before, to the true expected values as the number of visits to each state-action pair approaches infinity.

The only complication is that many state–action pairs may never be visited. If  $\pi$ is a deterministic policy, then in following  $\pi$ one will observe returns only for one of the actions from each state. With no returns to average, the Monte Carlo estimates of the other actions will not improve with experience. This is a serious problem because the purpose of learning action values is to help in choosing among the actions available in each state. To compare alternatives we need to estimate the value of all the actions from each state, not just the one we currently favor.

---

This is the general problem of maintaining exploration, as discussed in the context of the n-armed bandit problem in Chapter 2. For policy evaluation to work for action values, we must assure continual exploration. One way to do this is by specifying that the episodes start in a state-action pair, and that every pair has a nonzero probability of being selected as the start. This guarantees that all state-action pairs will be visited an infinite number of times in the limit of an infinite number of episodes. We call this the assumption of exploring starts.

The assumption of exploring starts is sometimes useful, but of course it cannot be relied upon in general, particularly when learning directly from actual interaction with an environment. In that case the starting conditions are unlikely to be so helpful. The most common alternative approach to assuring that all state-action pairs are encountered is to consider only policies that are stochastic with a nonzero probability of selecting all actions in each state. We discuss two important variants of this approach in later sections. For now, we retain the assumption of exploring starts and complete the presentation of a full Monte Carlo control method.

## 5.3 Monte Carlo Control

We are now ready to consider how Monte Carlo estimation can be used in control, that is, to approximate optimal policies. The overall idea is to proceed according to the same pattern as in the DP chapter, that is, according to the idea of generalized policy iteration (GPI). In GPI one maintains both an approximate policy and an approximate value function. The value function is repeatedly altered to more closely approximate the value function for the current policy, and the policy is repeatedly improved with respect to the current value function:

<div style="text-align: center;"><img src="imgs/img_in_image_box_479_1105_743_1354.jpg" alt="Image" width="21%" /></div>

These two kinds of changes work against each other to some extent, as each creates a moving target for the other, but together they cause both policy and

---

value function to approach optimality.

To begin, let us consider a Monte Carlo version of classical policy iteration. In this method, we perform alternating complete steps of policy evaluation and policy improvement, beginning with an arbitrary policy  $\pi_{0}$ and ending with the optimal policy and optimal action-value function:

 
$$
\pi_{0}\stackrel{\mathrm{E}}{\longrightarrow}q_{\pi_{0}}\stackrel{\mathrm{I}}{\longrightarrow}\pi_{1}\stackrel{\mathrm{E}}{\longrightarrow}q_{\pi_{1}}\stackrel{\mathrm{I}}{\longrightarrow}\pi_{2}\stackrel{\mathrm{E}}{\longrightarrow}\cdots\stackrel{\mathrm{I}}{\longrightarrow}\pi_{*}\stackrel{\mathrm{E}}{\longrightarrow}q_{*},
$$
 

where  $\xrightarrow{\mathrm{E}}$ denotes a complete policy evaluation and  $\xrightarrow{T}$ denotes a complete policy improvement. Policy evaluation is done exactly as described in the preceding section. Many episodes are experienced, with the approximate action-value function approaching the true function asymptotically. For the moment, let us assume that we do indeed observe an infinite number of episodes and that, in addition, the episodes are generated with exploring starts. Under these assumptions, the Monte Carlo methods will compute each  $q_{\pi_k}$ exactly, for arbitrary  $\pi_k$.

Policy improvement is done by making the policy greedy with respect to the current value function. In this case we have an action-value function, and therefore no model is needed to construct the greedy policy. For any action-value function  $q$, the corresponding greedy policy is the one that, for each  $s \in \mathcal{S}$, deterministically chooses an action with maximal action-value:

$$
\pi(s)=\arg\max_{a}q(s,a).   \tag*{(5.1)}
$$

Policy improvement then can be done by constructing each  $\pi_{k+1}$ as the greedy policy with respect to  $q_{\pi_k}$. The policy improvement theorem (Section 4.2) then applies to  $\pi_k$ and  $\pi_{k+1}$ because, for all  $s \in \mathcal{S}$,

 
$$
\begin{array}{r c l}{q_{\pi_{k}}(s,\pi_{k+1}(s))}&{=}&{q_{\pi_{k}}(s,\underset{a}{\operatorname{a r g}\operatorname*{m a x}}q_{\pi_{k}}(s,a))}\\ {}&{}&{}\\ {}&{=}&{\underset{a}{\operatorname*{m a x}}q_{\pi_{k}}(s,a)}\\ {}&{\geq}&{q_{\pi_{k}}(s,\pi_{k}(s))}\\ {}&{=}&{v_{\pi_{k}}(s).}\\ \end{array}
$$
 

As we discussed in the previous chapter, the theorem assures us that each  $\pi_{k+1}$ is uniformly better than  $\pi_k$, or just as good as  $\pi_k$, in which case they are both optimal policies. This in turn assures us that the overall process converges to the optimal policy and optimal value function. In this way Monte Carlo methods can be used to find optimal policies given only sample episodes and no other knowledge of the environment's dynamics.

We made two unlikely assumptions above in order to easily obtain this guarantee of convergence for the Monte Carlo method. One was that the

---

episodes have exploring starts, and the other was that policy evaluation could be done with an infinite number of episodes. To obtain a practical algorithm we will have to remove both assumptions. We postpone consideration of the first assumption until later in this chapter.

For now we focus on the assumption that policy evaluation operates on an infinite number of episodes. This assumption is relatively easy to remove. In fact, the same issue arises even in classical DP methods such as iterative policy evaluation, which also converge only asymptotically to the true value function. In both DP and Monte Carlo cases there are two ways to solve the problem. One is to hold firm to the idea of approximating  $q_{\pi_k}$ in each policy evaluation. Measurements and assumptions are made to obtain bounds on the magnitude and probability of error in the estimates, and then sufficient steps are taken during each policy evaluation to assure that these bounds are sufficiently small. This approach can probably be made completely satisfactory in the sense of guaranteeing correct convergence up to some level of approximation. However, it is also likely to require far too many episodes to be useful in practice on any but the smallest problems.

The second approach to avoiding the infinite number of episodes nominally required for policy evaluation is to forgo trying to complete policy evaluation before returning to policy improvement. On each evaluation step we move the value function toward  $q_{\pi_k}$, but we do not expect to actually get close except over many steps. We used this idea when we first introduced the idea of GPI in Section 4.6. One extreme form of the idea is value iteration, in which only one iteration of iterative policy evaluation is performed between each step of policy improvement. The in-place version of value iteration is even more extreme; there we alternate between improvement and evaluation steps for single states.

For Monte Carlo policy evaluation it is natural to alternate between evaluation and improvement on an episode-by-episode basis. After each episode, the observed returns are used for policy evaluation, and then the policy is improved at all the states visited in the episode. A complete simple algorithm along these lines is given in Figure 5.4. We call this algorithm Monte Carlo ES, for Monte Carlo with Exploring Starts.

In Monte Carlo ES, all the returns for each state–action pair are accumulated and averaged, irrespective of what policy was in force when they were observed. It is easy to see that Monte Carlo ES cannot converge to any suboptimal policy. If it did, then the value function would eventually converge to the value function for that policy, and that in turn would cause the policy to change. Stability is achieved only when both the policy and the value function are optimal. Convergence to this optimal fixed point seems inevitable as the changes to the action-value function decrease over time, but has not yet

---

Initialize, for all  $s \in S$,  $a \in \mathcal{A}(s)$:
 $Q(s, a) \leftarrow \text{arbitrary}$
 $\pi(s) \leftarrow \text{arbitrary}$
 $Returns(s, a) \leftarrow \text{empty list}$

Repeat forever:
Choose  $S_0 \in S$ and  $A_0 \in \mathcal{A}(S_0)$ s.t. all pairs have probability > 0
Generate an episode starting from  $S_0$,  $A_0$, following  $\pi$
For each pair s, a appearing in the episode:
 $G \leftarrow \text{return following the first occurrence of } s, a$
 $\text{Append } G \text{ to } \text{Returns}(s, a)$
 $Q(s, a) \leftarrow \text{average}(\text{Returns}(s, a))$
For each s in the episode:
 $\pi(s) \leftarrow \arg\max_a Q(s, a)$

<div style="text-align: center;">Figure 5.4: Monte Carlo ES: A Monte Carlo control algorithm assuming exploring starts and that episodes always terminate for all policies.</div>

been formally proved. In our opinion, this is one of the most fundamental open theoretical questions in reinforcement learning (for a partial solution, see Tsitsiklis, 2002).

Example 5.3: Solving Blackjack It is straightforward to apply Monte Carlo ES to blackjack. Since the episodes are all simulated games, it is easy to arrange for exploring starts that include all possibilities. In this case one simply picks the dealer's cards, the player's sum, and whether or not the player has a usable ace, all at random with equal probability. As the initial policy we use the policy evaluated in the previous blackjack example, that which sticks only on 20 or 21. The initial action-value function can be zero for all state-action pairs. Figure 5.5 shows the optimal policy for blackjack found by Monte Carlo ES. This policy is the same as the "basic" strategy of Thorp (1966) with the sole exception of the leftmost notch in the policy for a usable ace, which is not present in Thorp's strategy. We are uncertain of the reason for this discrepancy, but confident that what is shown here is indeed the optimal policy for the version of blackjack we have described.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_306_234_897_651.jpg" alt="Image" width="48%" /></div>

<div style="text-align: center;">Figure 5.5: The optimal policy and state-value function for blackjack, found by Monte Carlo ES (Figure 5.4). The state-value function shown was computed from the action-value function found by Monte Carlo ES.</div>

## 5.4 Monte Carlo Control without Exploring Starts

How can we avoid the unlikely assumption of exploring starts? The only general way to ensure that all actions are selected infinitely often is for the agent to continue to select them. There are two approaches to ensuring this, resulting in what we call on-policy methods and off-policy methods. On-policy methods attempt to evaluate or improve the policy that is used to make decisions, whereas off-policy methods evaluate or improve a policy different from that used to generate the data. The Monte Carlo ES method developed above is an example of an on-policy method. In this section we show how an on-policy Monte Carlo control method can be designed that does not use the unrealistic assumption of exploring starts. Off-policy methods are considered in the next section.

In on-policy control methods the policy is generally soft, meaning that  $\pi(a|s) > 0$ for all  $s \in \mathcal{S}$ and all  $a \in \mathcal{A}(s)$, but gradually shifted closer and closer to a deterministic optimal policy. Many of the methods discussed in Chapter 2 provide mechanisms for this. The on-policy method we present in this section uses  $\varepsilon$-greedy policies, meaning that most of the time they choose an action that has maximal estimated action value, but with probability  $\varepsilon$.

---

## 5.4. MONTE CARLO CONTROL WITHOUT EXPLORING STARTS 125

they instead select an action at random. That is, all nongreedy actions are given the minimal probability of selection,  $\frac{\epsilon}{|\mathcal{A}(s)|}$, and the remaining bulk of the probability,  $1 - \varepsilon + \frac{\epsilon}{|\mathcal{A}(s)|}$, is given to the greedy action. The  $\varepsilon$-greedy policies are examples of  $\varepsilon$-soft policies, defined as policies for which  $\pi(a|s) \geq \frac{\epsilon}{|A(s)|}$ for all states and actions, for some  $\varepsilon > 0$. Among  $\varepsilon$-soft policies,  $\varepsilon$-greedy policies are in some sense those that are closest to greedy.

The overall idea of on-policy Monte Carlo control is still that of GPI. As in Monte Carlo ES, we use first-visit MC methods to estimate the action-value function for the current policy. Without the assumption of exploring starts, however, we cannot simply improve the policy by making it greedy with respect to the current value function, because that would prevent further exploration of nongreedy actions. Fortunately, GPI does not require that the policy be taken all the way to a greedy policy, only that it be moved toward a greedy policy. In our on-policy method we will move it only to an  $\varepsilon$-greedy policy. For any  $\varepsilon$-soft policy,  $\pi$, any  $\varepsilon$-greedy policy with respect to  $q_{\pi}$ is guaranteed to be better than or equal to  $\pi$.

That any  $\varepsilon$-greedy policy with respect to  $q_\pi$ is an improvement over any  $\varepsilon$-soft policy  $\pi$ is assured by the policy improvement theorem. Let  $\pi'$ be the  $\varepsilon$-greedy policy. The conditions of the policy improvement theorem apply because for any  $s \in \mathcal{S}$:

$$
\begin{array}{r c l}{q_{\pi}(s,\pi^{\prime}(s))}&{=}&{\displaystyle\sum_{a}\pi^{\prime}(a|s)q_{\pi}(s,a)}\\ {}&{=}&{\displaystyle\frac{\epsilon}{|\mathcal{A}(s)|}\displaystyle\sum_{a}q_{\pi}(s,a)\;+\;(1-\varepsilon)\operatorname*{m a x}_{a}q_{\pi}(s,a)}\\ {}&{\geq}&{\displaystyle\frac{\epsilon}{|\mathcal{A}(s)|}\displaystyle\sum_{a}q_{\pi}(s,a)\;+\;(1-\varepsilon)\displaystyle\sum_{a}\frac{\pi(a|s)-\frac{\epsilon}{|\mathcal{A}(s)|}}{1-\varepsilon}q_{\pi}(s,a)}\\ \end{array}   \tag*{(5.2)}
$$

(the sum is a weighted average with nonnegative weights summing to 1, and as such it must be less than or equal to the largest number averaged)

 
$$
\begin{array}{r l}{=}&{{}\frac{\epsilon}{|\mathcal{A}(s)|}\displaystyle\sum_{a}q_{\pi}(s,a)~-~\frac{\epsilon}{|\mathcal{A}(s)|}\displaystyle\sum_{a}q_{\pi}(s,a)~+~\displaystyle\sum_{a}\pi(a|s)q_{\pi}(s,a)}\\ {=}&{{}v_{\pi}(s).}\end{array}
$$
 

Thus, by the policy improvement theorem,  $\pi' \geq \pi$ (i.e.,  $v_{\pi'}(s) \geq v_{\pi}(s)$, for all  $s \in \mathcal{S}$). We now prove that equality can hold only when both  $\pi'$ and  $\pi$ are optimal among the  $\varepsilon$-soft policies, that is, when they are better than or equal to all other  $\varepsilon$-soft policies.

Consider a new environment that is just like the original environment, except with the requirement that policies be  $\varepsilon$-soft “moved inside” the environment. The new environment has the same action and state set as the original

---

and behaves as follows. If in state $s$and taking action$a$, then with probability $1 - \varepsilon$the new environment behaves exactly like the old environment. With probability$\varepsilon$it repicks the action at random, with equal probabilities, and then behaves like the old environment with the new, random action. The best one can do in this new environment with general policies is the same as the best one could do in the original environment with$\varepsilon$-soft policies. Let $\tilde{v}_*$and$\tilde{q}_*$denote the optimal value functions for the new environment. Then a policy$\pi$is optimal among$\varepsilon$-soft policies if and only if $v_{\pi} = \tilde{v}_*.$From the definition of$\tilde{v}_*$, we know that it is the unique solution to

 
$$
\begin{align*}\widetilde{v}_{*}(s)\quad=&\quad(1-\varepsilon)\max_{a}\widetilde{q}_{*}(s,a)+\frac{\epsilon}{|\mathcal{A}(s)|}\sum_{a}\widetilde{q}_{*}(s,a)\\=&\quad(1-\varepsilon)\max_{a}\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma\widetilde{v}_{*}(s^{\prime})\Big]\\&+\quad\frac{\epsilon}{|\mathcal{A}(s)|}\sum_{a}\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma\widetilde{v}_{*}(s^{\prime})\Big].\end{align*}
$$
 

When equality holds and the  $\varepsilon$-soft policy  $\pi$ is no longer improved, then we also know, from (5.2), that

 
$$
\begin{align*}\begin{array}{rcl}v_{\pi}(s)&=&(1-\varepsilon)\max_{a}q_{\pi}(s,a)+\frac{\epsilon}{|\mathcal{A}(s)|}\sum_{a}q_{\pi}(s,a)\\&=&\left.(1-\varepsilon)\max_{a}\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{\pi}(s^{\prime})\Big]\right.\\&&\left.+\quad\frac{\epsilon}{|\mathcal{A}(s)|}\sum_{a}\sum_{s^{\prime},r}p(s^{\prime},r|s,a)\Big[r+\gamma v_{\pi}(s^{\prime})\Big].\end{array}\end{align*}
$$
 

However, this equation is the same as the previous one, except for the substitution of  $v_{\pi}$ for  $\widetilde{v}_{\star}$. Since  $\widetilde{v}_{\star}$ is the unique solution, it must be that  $v_{\pi} = \widetilde{v}_{\star}$.

In essence, we have shown in the last few pages that policy iteration works for  $\varepsilon$-soft policies. Using the natural notion of greedy policy for  $\varepsilon$-soft policies, one is assured of improvement on every step, except when the best policy has been found among the  $\varepsilon$-soft policies. This analysis is independent of how the action-value functions are determined at each stage, but it does assume that they are computed exactly. This brings us to roughly the same point as in the previous section. Now we only achieve the best policy among the  $\varepsilon$-soft policies, but on the other hand, we have eliminated the assumption of exploring starts. The complete algorithm is given in Figure 5.6.

---

Initialize, for all $s \in \mathcal{S}$, $a \in \mathcal{A}(s)$:
$Q(s, a) \leftarrow$arbitrary$Returns(s, a) \leftarrow$empty list$\pi(a|s) \leftarrow$an arbitrary$\varepsilon$-soft policy

Repeat forever:
(a) Generate an episode using $\pi$(b) For each pair$s$, $a$appearing in the episode:$G \leftarrow$return following the first occurrence of$s$, $a$Append$G$to$Returns(s, a)$
$Q(s, a) \leftarrow$ average($Returns(s, a)$)
(c) For each $s$in the episode:$a^* \leftarrow$ $\arg\max_{a} Q(s, a)$For all$a \in \mathcal{A}(s)$:
$\pi(a|s) \leftarrow$ $\left\{\begin{array}{ll}1 - \varepsilon + \varepsilon / |\mathcal{A}(s)| & \text{if } a = a^* \\ \varepsilon / |\mathcal{A}(s)| & \text{if } a \neq a^* \end{array}\right.$<div style="text-align: center;">Figure 5.6: An on-policy first-visit MC control algorithm for$ \varepsilon $-soft policies.</div>

## 5.5 Off-policy Prediction via Importance Sampling

So far we have considered methods for estimating the value functions for a policy given an infinite supply of episodes generated using that policy. Suppose now that all we have are episodes generated from a different policy. That is, suppose we wish to estimate  $v_{\pi}$ or  $q_{\pi}$, but all we have are episodes following another policy  $\mu$, where  $\mu \neq \pi$. We call  $\pi$ the target policy because learning its value function is the target of the learning process, and we call  $\mu$ the behavior policy because it is the policy controlling the agent and generating behavior. The overall problem is called off-policy learning because it is learning about a policy given only experience “off” (not following) that policy.

In order to use episodes from  $\mu$ to estimate values for  $\pi$, we must require that every action taken under  $\pi$ is also taken, at least occasionally, under  $\mu$. That is, we require that  $\pi(a|s) > 0$ implies  $\mu(a|s) > 0$. This is called the assumption of coverage. It follows from coverage that  $\mu$ must be stochastic in states where it is not identical to  $\pi$. The target policy  $\pi$, on the other hand, may be deterministic, and, in fact, this is a case of particular interest. Typically the target policy is the deterministic greedy policy with respect to the current action-value function estimate. This policy we hope becomes a deterministic optimal policy while the behavior policy remains stochastic and more exploratory, for example, an  $\varepsilon$-greedy policy.

---

Importance sampling is a general technique for estimating expected values under one distribution given samples from another. We apply this technique to off-policy learning by weighting returns according to the relative probability of their trajectories occurring under the target and behavior policies, called the importance-sampling ratio. Given a starting state  $S_t$, the probability of the subsequent state–action trajectory,  $A_t$,  $S_{t+1}$,  $A_{t+1}$, ...,  $S_T$, occurring under any policy  $\pi$ is

 
$$
\prod_{k=t}^{T-1}\pi(A_{k}|S_{k})p(S_{k+1}|S_{k},A_{k}),
$$
 

where p is the state-transition probability function defined by (3.8). Thus, the relative probability of the trajectory under the target and behavior policies (the importance-sampling ratio) is

$$
\rho_{t}^{T}=\frac{\prod_{k=t}^{T-1}\pi(A_{k}|S_{k})p(S_{k+1}|S_{k},A_{k})}{\prod_{k=t}^{T-1}\mu(A_{k}|S_{k})p(S_{k+1}|S_{k},A_{k})}=\prod_{k=t}^{T-1}\frac{\pi(A_{k}|S_{k})}{\mu(A_{k}|S_{k})}.   \tag*{(5.3)}
$$

Note that although the trajectory probabilities depend on the MDP’s transition probabilities, which are generally unknown, all the transition probabilities cancel and drop out. The importance sampling ratio ends up depending only on the two policies and not at all on the MDP.

Now we are ready to give a Monte Carto algorithm that uses a batch of observed episodes following policy  $\mu$ to estimate  $v_{\pi}(s)$. It is convenient here to number time steps in a way that increases across episode boundaries. That is, if the first episode of the batch ends in a terminal state at time 100, then the next episode begins at time  $t = 101$. This enables us to use time-step numbers to refer to particular steps in particular episodes. In particular, we can define the set of all time steps in which state  $s$ is visited, denoted  $\mathcal{T}(s)$. This is for an every-visit method; for a first-visit method,  $\mathcal{T}(s)$ would only include time steps that were first visits to  $s$ within their episode. Also, let  $T(t)$ denote the first time of termination following time  $t$, and  $G_t$ denote the return after  $t$ up through  $T(t)$. Then  $\{G_t\}_{t \in \mathcal{T}(s)}$ are the returns that pertain to state  $s$, and  $\{\rho_t^{T(t)}\}_{t \in \mathcal{T}(s)}$ are the corresponding importance-sampling ratios. To estimate  $v_{\pi}(s)$, we simply scale the returns by the ratios and average the results:

$$
V(s)=\frac{\sum_{t\in\mathcal{T}(s)}\rho_{t}^{T(t)}G_{t}}{|\mathcal{T}(s)|}.   \tag*{(5.4)}
$$

When importance sampling is done as a simple average in this way it is called ordinary importance sampling.

---

An important alternative is weighted importance sampling, which uses a weighted average, defined as

$$
V(s)=\frac{\sum_{t\in\mathcal{T}(s)}\rho_{t}^{T(t)}G_{t}}{\sum_{t\in\mathcal{T}(s)}\rho_{t}^{T(t)}},   \tag*{(5.5)}
$$

or zero if the denominator is zero. To understand these two varieties of importance sampling, consider their estimates after observing a single return. In the weighted-average estimate, the ratio  $\rho_t^{T(t)}$ for the single return cancels in the numerator and denominator, so that the estimate is equal to the observed return independent of the ratio (assuming the ratio is nonzero). Given that this return was the only one observed, this is a reasonable estimate, but of course its expectation is  $v_\mu(s)$ rather than  $v_\pi(s)$, and in this statistical sense it is biased. In contrast, the simple average (5.4) is always  $v_\pi(s)$ in expectation (it is unbiased), but it can be extreme. Suppose the ratio were ten, indicating that the trajectory observed is ten times as likely under the target policy as under the behavior policy. In this case the ordinary importance-sampling estimate would be ten times the observed return. That is, it would be quite far from the observed return even though the episode's trajectory is considered very representative of the target policy.

Formally, the difference between the two kinds of importance sampling is expressed in their variances. The variance of the ordinary importance-sampling estimator is in general unbounded because the variance of the ratios is unbounded, whereas in the weighted estimator the largest weight on any single return is one. In fact, assuming bounded returns, the variance of the weighted importance-sampling estimator converges to zero even if the variance of the ratios themselves is infinite (Precup, Sutton, and Dasgupta 2001). In practice, the weighted estimator usually has dramatically lower variance and is strongly preferred. A complete every-visit MC algorithm for off-policy policy evaluation using weighted importance sampling is given at the end of the next section in Figure 5.9.

---

##### Sample 5.4: Off-policy Estimation of a Blackjack State Value

We applied both ordinary and weighted importance-sampling methods to estimate the value of a single blackjack state from off-policy data. Recall that one of the advantages of Monte Carlo methods is that they can be used to evaluate a single state without forming estimates for any other states. In this example, we evaluated the state in which the dealer is showing a deuce, the sum of the player's cards is 13, and the player has a usable ace (that is, the player holds an ace and a deuce, or equivalently three aces). The data was generated by starting in this state then choosing to hit or stick at random with equal probability (the behavior policy). The target policy was to stick only on a sum of 20 or 21, as in Example 5.1. The value of this state under the target policy is approximately -0.27726 (this was determined by separately generating one-hundred million episodes using the target policy and averaging their returns). Both off-policy methods closely approximated this value after 1000 off-policy episodes using the random policy. Figure 5.7 shows the mean squared error (estimated from 100 independent runs) for each method as a function of number of episodes. The weighted importance-sampling method has much lower overall error in this example, as is typical in practice.

<div style="text-align: center;"><img src="imgs/img_in_chart_box_222_764_929_1101.jpg" alt="Image" width="57%" /></div>

<div style="text-align: center;">Figure 5.7: Weighted importance sampling produces lower error estimates of the value of a single blackjack state from off-policy episodes (see Example 5.4).</div>


---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_213_209_1005_633.jpg" alt="Image" width="64%" /></div>

<div style="text-align: center;">Figure 5.8: Ordinary importance sampling produces surprisingly unstable estimates on the one-state MDP shown inset (Example 5.5). The correct estimate here is 1, and, even though this is the expected value of a sample return (after importance sampling), the variance of the samples is infinite, and the estimates do not convergence to this value. These results are for off-policy first-visit MC.</div>

##### Example 5.5: Infinite Variance

The estimates of ordinary importance sampling will typically have infinite variance, and thus unsatisfactory convergence properties, whenever the scaled returns have infinite variance—and this can easily happen in off-policy learning when trajectories contain loops. A simple example is shown inset in Figure 5.8. There is only one nonterminal state s and two actions, end and back. The end action causes a deterministic transition to termination, whereas the back action transitions, with probability 0.9, back to s or, with probability 0.1, on to termination. The rewards are +1 on the latter transition and otherwise zero. Consider the target policy that always selects back. All episodes under this policy consist of some number (possibly zero) of transitions back to s followed by termination with a reward and return of +1. Thus the value of s under the target policy is thus 1. Suppose we are estimating this value from off-policy data using the behavior policy that selects end and back with equal probability. The lower part of Figure 5.8 shows ten independent runs of the first-visit MC algorithm using ordinary importance sampling. Even after millions of episodes, the estimates fail to converge to the correct value of 1. In contrast, the weighted importance-sampling algorithm would give an estimate of exactly 1 everafter the first episode that was consistent with the target policy (i.e., that ended with the back action). This is clear because

---

that algorithm produces a weighted average of the returns consistent with the target policy, all of which would be exactly 1.

We can verify that the variance of the importance-sampling-scaled returns is infinite in this example by a simple calculation. The variance of any random variable X is the expected value of the deviation from its mean  $\bar{X}$, which can be written

 
$$
\mathrm{Var}[X]=\mathbb{E}\Big[\big(X-\bar{X}\big)^{2}\Big]=\mathbb{E}\big[X^{2}-2X\bar{X}+\bar{X}^{2}\big]=\mathbb{E}\big[X^{2}\big]-\bar{X}^{2}.
$$
 

Thus, if the mean is finite, as it is in our case, the variance is infinite if and only if the expectation of the square of the random variable is infinite. Thus, we need only show that the expected square of the importance-sampling-scaled return is infinite:

 
$$
\mathbb{E}\left[\left(\prod_{t=0}^{T-1}\frac{\pi(A_{t}|S_{t})}{\mu(A_{t}|S_{t})}G_{0}\right)^{2}\right].
$$
 

To compute this expectation, we break it down into cases based on episode length and termination. First note that, for any episode ending with the end action, the importance sampling ratio is zero, because the target policy would never take this action; these episodes thus contribute nothing to the expectation (the quantity in parenthesis will be zero) and can be ignored. We need only consider episodes that involve some number (possibly zero) of back actions that transition back to the nonterminal state, followed by a back action transitioning to termination. All of these episodes have a return of 1, so the  $G_{0}$ factor can be ignored. To get the expected square we need only consider each length of episode, multiplying the probability of the episode's occurrence by the square of its importance-sampling ratio, and add these up:

(the length 1 episode)

 
$$
\begin{aligned}&=\frac{1}{2}\cdot0.1\left(\frac{1}{0.5}\right)^{2}\\&\quad+\frac{1}{2}\cdot0.9\cdot\frac{1}{2}\cdot0.1\left(\frac{1}{0.5}\frac{1}{0.5}\right)^{2}\\&\quad+\frac{1}{2}\cdot0.9\cdot\frac{1}{2}\cdot0.9\cdot\frac{1}{2}\cdot0.1\left(\frac{1}{0.5}\frac{1}{0.5}\frac{1}{0.5}\right)^{2}\\&\quad+\cdots\\&=0.1\sum_{k=0}^{\infty}0.9^{k}\cdot2^{k}\cdot2\\&=0.2\sum_{k=0}^{\infty}1.8^{k}\\&=\infty.\end{aligned}
$$
 

(the length 2 episode)

(the length 3 episode)

---

## 5.6 Incremental Implementation

Monte Carlo prediction methods can be implemented incrementally, on an episode-by-episode basis, using extensions of the techniques described in Chapter 2. Whereas in Chapter 2 we averaged rewards, in Monte Carlo methods we average returns. In all other respects exactly the same methods as used in Chapter 2 can be used for on-policy Monte Carlo methods. For off-policy Monte Carlo methods, we need to separately consider those that use ordinary importance sampling and those that use weighted importance sampling.

In ordinary importance sampling, the returns are scaled by the importance sampling ratio  $\rho_t^{T(t)}$ (5.3), then simply averaged. For these methods we can again use the incremental methods of Chapter 2, but using the scaled returns in place of the rewards of that chapter. This leaves the case of off-policy methods using weighted importance sampling. Here we have to form a weighted average of the returns, and a slightly different incremental algorithm is required.

Suppose we have a sequence of returns  $G_1, G_2, \ldots, G_{n-1}$, all starting in the same state and each with a corresponding random weight  $W_i$ (e.g.,  $W_i = \rho_t^{T(t)}$). We wish to form the estimate

$$
V_{n}=\frac{\sum_{k=1}^{n-1}W_{k}G_{k}}{\sum_{k=1}^{n-1}W_{k}},\qquad n\geq2,   \tag*{(5.6)}
$$

and keep it up-to-date as we obtain a single additional return  $G_{n}$. In addition to keeping track of  $V_{n}$, we must maintain for each state the cumulative sum  $C_{n}$ of the weights given to the first n returns. The update rule for  $V_{n}$ is

$$
V_{n+1}=V_{n}+\frac{W_{n}}{C_{n}}\Big[G_{n}-V_{n}\Big],\qquad n\geq1,   \tag*{(5.7)}
$$

and

 
$$
C_{n+1}=C_{n}+W_{n+1},
$$
 

where  $C_0 = 0$ (and  $V_1$ is arbitrary and thus need not be specified). Figure 5.9 gives a complete episode-by-episode incremental algorithm for Monte Carlo policy evaluation. The algorithm is nominally for the off-policy case, using weighted importance sampling, but applies as well to the on-policy case just by choosing the target and behavior policies as the same.

---

Initialize, for all $s \in \mathcal{S}$, $a \in \mathcal{A}(s)$:
$Q(s, a) \leftarrow$arbitrary$C(s, a) \leftarrow 0$
$\mu(a|s) \leftarrow$an arbitrary soft behavior policy$\pi(a|s) \leftarrow$an arbitrary target policy

Repeat forever:
Generate an episode using$\mu$:
$S_0, A_0, R_1, \ldots, S_{T-1}, A_{T-1}, R_T, S_T$
$G \leftarrow 0$
$W \leftarrow 1$For$t = T - 1, T - 2, \ldots$downto 0:$G \leftarrow \gamma G + R_{t+1}$
$C(S_t, A_t) \leftarrow C(S_t, A_t) + W$
$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \frac{W}{C(S_t, A_t)} [G - Q(S_t, A_t)]$
$W \leftarrow W \frac{\pi(A_t|S_t)}{\mu(A_t|S_t)}$If$W = 0$then ExitForLoop

<div style="text-align: center;">Figure 5.9: An incremental every-visit MC policy-evaluation algorithm, using weighted importance sampling. The approximation$ Q $converges to$ q_{\pi} $(for all encountered state-action pairs) even though all actions are selected according to a potentially different policy,$ \mu $. In the on-policy case  $(\pi = \mu)$,  $W$ is always 1.</div>


---

## 5.7 Off-Policy Monte Carlo Control

We are now ready to present an example of the second class of learning control methods we consider in this book: off-policy methods. Recall that the distinguishing feature of on-policy methods is that they estimate the value of a policy while using it for control. In off-policy methods these two functions are separated. The policy used to generate behavior, called the behavior policy, may in fact be unrelated to the policy that is evaluated and improved, called the target policy. An advantage of this separation is that the target policy may be deterministic (e.g., greedy), while the behavior policy can continue to sample all possible actions.

Off-policy Monte Carlo control methods use one of the techniques presented in the preceding two sections. They follow the behavior policy while learning about and improving the target policy. These techniques requires that the behavior policy has a nonzero probability of selecting all actions that might be selected by the target policy (coverage). To explore all possibilities, we require that the behavior policy be soft (i.e., that it select all actions in all states with nonzero probability).

Figure 5.10 shows an off-policy Monte Carlo method, based on GPI and weighted importance sampling, for estimating  $q_{*}$. The target policy  $\pi$ is the greedy policy with respect to  $Q$, which is an estimate of  $q_{\pi}$. The behavior policy  $\mu$ can be anything, but in order to assure convergence of  $\pi$ to the optimal policy, an infinite number of returns must be obtained for each pair of state and action. This can be assured by choosing  $\mu$ to be  $\varepsilon$-soft.

A potential problem is that this method learns only from the tails of episodes, after the last nongreedy action. If nongreedy actions are frequent, then learning will be slow, particularly for states appearing in the early portions of long episodes. Potentially, this could greatly slow learning. There has been insufficient experience with off-policy Monte Carlo methods to assess how serious this problem is. If it is serious, the most important way to address it is probably by incorporating temporal-difference learning, the algorithmic idea developed in the next chapter. Alternatively, if  $\gamma$ is less than 1, then the idea developed in the next section may also help significantly.

---

Initialize, for all $s \in \mathcal{S}$, $a \in \mathcal{A}(s)$:
$Q(s, a) \leftarrow$arbitrary$C(s, a) \leftarrow 0$
$\pi(s) \leftarrow$a deterministic policy that is greedy with respect to$Q$Repeat forever:
Generate an episode using any soft policy$\mu$:
$S_0, A_0, R_1, \ldots, S_{T-1}, A_{T-1}, R_T, S_T$
$G \leftarrow 0$
$W \leftarrow 1$For$t = T - 1, T - 2, \ldots$downto 0:$G \leftarrow \gamma G + R_{t+1}$
$C(S_t, A_t) \leftarrow C(S_t, A_t) + W$
$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \frac{W}{C(S_t, A_t)} [G - Q(S_t, A_t)]$
$\pi(S_t) \leftarrow \arg\max_a Q(S_t, a)$(with ties broken arbitrarily)$W \leftarrow W \frac{1}{\mu(A_t | S_t)}$If$W = 0$then ExitForLoop

<div style="text-align: center;">Figure 5.10: An off-policy every-visit MC control algorithm, using weighted importance sampling. The policy$ \pi $converges to optimal at all encountered states even though actions are selected according to a different soft policy$ \mu $, which may change between or even within episodes.</div>

## *5.8 Importance Sampling on Truncated Returns

So far our off-policy methods have formed importance-sampling ratios for returns considered as unitary wholes. This is clearly the right thing for a Monte Carlo method to do in the absence of discounting (i.e., if  $\gamma = 1$), but if  $\gamma < 1$ then there may be something better. Consider the case where episodes are long and  $\gamma$ is significantly less than 1. For concreteness, say that episodes last 100 steps and that  $\gamma = 0$. The return from time 0 will then be  $G_0 = R_1$, and its importance sampling ratio will be a product of 100 factors,  $\frac{\pi(A_0|S_0)}{\mu(A_0|S_0)} \frac{\pi(A_1|S_1)}{\mu(A_1|S_1)} \cdots \frac{\pi(A_{99}|S_{99})}{\mu(A_{99}|S_{99})}$. In ordinary importance sampling, the return will be scaled by the entire product, but it is really only necessary to scale by the first factor, by  $\frac{\pi(A_0|S_0)}{\mu(A_0|S_0)}$. The other 99 factors  $\frac{\pi(A_1|S_1)}{\mu(A_1|S_1)} \cdots \frac{\pi(A_{99}|S_{99})}{\mu(A_{99}|S_{99})}$ are irrelevant because after the first reward the return has already been determined. These later factors are all independent of the return and of expected value 1; they do not change the expected update, but they add enormously to its variance. In some cases they could even make the variance infinite. Let us now consider an idea for avoiding this large extraneous variance.