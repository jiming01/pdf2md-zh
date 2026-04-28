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

<div style="text-align: center;"><img src="imgs/img_in_image_box_291_221_926_628.jpg" alt="Image" width="51%" /></div>

<div style="text-align: center;">Figure 14.8: Four elevators in a ten-story building.</div>

In practice, modern elevator dispatchers are designed heuristically and evaluated on simulated buildings. The simulators are quite sophisticated and detailed. The physics of each elevator car is modeled in continuous time with continuous state variables. Passenger arrivals are modeled as discrete, stochastic events, with arrival rates varying frequently over the course of a simulated day. Not surprisingly, the times of greatest traffic and greatest challenge to the dispatching algorithm are the morning and evening rush hours. Dispatchers are generally designed primarily for these difficult periods.

The performance of elevator dispatchers is measured in several different ways, all with respect to an average passenger entering the system. The average waiting time is how long the passenger waits before getting on an elevator, and the average system time is how long the passenger waits before being dropped off at the destination floor. Another frequently encountered statistic is the percentage of passengers whose waiting time exceeds 60 seconds. The objective that Crites and Barto focused on is the average squared waiting time. This objective is commonly used because it tends to keep the waiting times low while also encouraging fairness in serving all the passengers.

Crites and Barto applied a version of one-step Q-learning augmented in several ways to take advantage of special features of the problem. The most important of these concerned the formulation of the actions. First, each elevator made its own decisions independently of the others. Second, a number of constraints were placed on the decisions. An elevator carrying passengers could not pass by a floor if any of its passengers wanted to get off there, nor

---

could it reverse direction until all of its passengers wanting to go in its current direction had reached their floors. In addition, a car was not allowed to stop at a floor unless someone wanted to get on or off there, and it could not stop to pick up passengers at a floor if another elevator was already stopped there. Finally, given a choice between moving up or down, the elevator was constrained always to move up (otherwise evening rush hour traffic would tend to push all the elevators down to the lobby). These last three constraints were explicitly included to provide some prior knowledge and make the problem easier. The net result of all these constraints was that each elevator had to make few and simple decisions. The only decision that had to be made was whether or not to stop at a floor that was being approached and that had passengers waiting to be picked up. At all other times, no choices needed to be made.

That each elevator made choices only infrequently permitted a second simplification of the problem. As far as the learning agent was concerned, the system made discrete jumps from one time at which it had to make a decision to the next. When a continuous-time decision problem is treated as a discrete-time system in this way it is known as a semi-Markov decision process. To a large extent, such processes can be treated just like any other Markov decision process by taking the reward on each discrete transition as the integral of the reward over the corresponding continuous-time interval. The notion of return generalizes naturally from a discounted sum of future rewards to a discounted integral of future rewards:

 
$$
G_{t}=\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1}\qquad\\begin{aligned}&\quad becomes\quad G_{t}=\int_{0}^{\infty}e^{-\beta\tau}R_{t+\tau}d\tau,\\ \end{aligned}
$$
 

where  $R_t$ on the left is the usual immediate reward in discrete time and  $R_{t+\tau}$ on the right is the instantaneous reward at continuous time  $t + \tau$. In the elevator problem the continuous-time reward is the negative of the sum of the squared waiting times of all waiting passengers. The parameter  $\beta > 0$ plays a role similar to that of the discount-rate parameter  $\gamma \in [0, 1)$.

The basic idea of the extension of Q-learning to semi-Markov decision problems can now be explained. Suppose the system is in state S and takes action A at time  $t_{1}$, and then the next decision is required at time  $t_{2}$ in state  $S'$. After this discrete-event transition, the semi-Markov Q-learning backup for a tabular action-value function, Q, would be:

 
$$
Q(S,A)\leftarrow Q(S,A)+\alpha\left[\int_{t_{1}}^{t_{2}}e^{-\beta(\tau-t_{1})}R_{\tau}d\tau+e^{-\beta(t_{2}-t_{1})}\min_{a}Q(S^{\prime},a)-Q(S,A)\right].
$$
 

Note how  $e^{-\beta(t_{2}-t_{1})}$ acts as a variable discount factor that depends on the amount of time between events. This method is due to Bradtke and Duff (1995).

---

One complication is that the reward as defined—the negative sum of the squared waiting times—is not something that would normally be known while an actual elevator was running. This is because in a real elevator system one does not know how many people are waiting at a floor, only how long it has been since the button requesting a pickup on that floor was pressed. Of course this information is known in a simulator, and Crites and Barto used it to obtain their best results. They also experimented with another technique that used only information that would be known in an on-line learning situation with a real set of elevators. In this case one can use how long since each button has been pushed together with an estimate of the arrival rate to compute an expected summed squared waiting time for each floor. Using this in the reward measure proved nearly as effective as using the actual summed squared waiting time.

For function approximation, a nonlinear neural network trained by backpropagation was used to represent the action-value function. Crites and Barto experimented with a wide variety of ways of representing states to the network. After much exploration, their best results were obtained using networks with 47 input units, 20 hidden units, and two output units, one for each action. The way the state was encoded by the input units was found to be critical to the effectiveness of the learning. The 47 input units were as follows:

● 18 units: Two units encoded information about each of the nine hall buttons for down pickup requests. A real-valued unit encoded the elapsed time if the button had been pushed, and a binary unit was on if the button had not been pushed.

- 16 units: A unit for each possible location and direction for the car whose decision was required. Exactly one of these units was on at any given time.

- 10 units: The location of the other elevators superimposed over the 10 floors. Each elevator had a “footprint” that depended on its direction and speed. For example, a stopped elevator caused activation only on the unit corresponding to its current floor, but a moving elevator caused activation on several units corresponding to the floors it was approaching, with the highest activations on the closest floors. No information was provided about which one of the other cars was at a particular location.

- 1 unit: This unit was on if the elevator whose decision was required was at the highest floor with a passenger waiting.

● 1 unit: This unit was on if the elevator whose decision was required was at the floor with the passenger who had been waiting for the longest amount of time.

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_225_212_480_437.jpg" alt="Image" width="20%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_496_213_739_438.jpg" alt="Image" width="19%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_chart_box_740_210_999_438.jpg" alt="Image" width="21%" /></div>

<div style="text-align: center;">Figure 14.9: Comparison of elevator dispatchers. The SECTOR dispatcher is similar to what is used in many actual elevator systems. The RL1 and RL2 dispatchers were constructed through reinforcement learning.</div>

• 1 unit: Bias unit was always on.

Two architectures were used. In RL1, each elevator was given its own action-value function and its own neural network. In RL2, there was only one network and one action-value function, with the experiences of all four elevators contributing to learning in the one network. In both cases, each elevator made its decisions independently of the other elevators, but shared a single reward signal with them. This introduced additional stochasticity as far as each elevator was concerned because its reward depended in part on the actions of the other elevators, which it could not control. In the architecture in which each elevator had its own action-value function, it was possible for different elevators to learn different specialized strategies (although in fact they tended to learn the same strategy). On the other hand, the architecture with a common action-value function could learn faster because it learned simultaneously from the experiences of all elevators. Training time was an issue here, even though the system was trained in simulation. The reinforcement learning methods were trained for about four days of computer time on a 100 mips processor (corresponding to about 60,000 hours of simulated time). While this is a considerable amount of computation, it is negligible compared with what would be required by any conventional dynamic programming algorithm.

The networks were trained by simulating a great many evening rush hours while making dispatching decisions using the developing, learned action-value functions. Crites and Barto used the Gibbs softmax procedure to select actions as described in Section 2.3, reducing the “temperature” gradually over training. A temperature of zero was used during test runs on which the performance of the learned dispatchers was assessed.

Figure 14.9 shows the performance of several dispatchers during a simulated evening rush hour, what researchers call down-peak traffic. The dispatchers

---

include methods similar to those commonly used in the industry, a variety of heuristic methods, sophisticated research algorithms that repeatedly run complex optimization algorithms on-line (Bao et al., 1994), and dispatchers learned by using the two reinforcement learning architectures. By all of the performance measures, the reinforcement learning dispatchers compare favorably with the others. Although the optimal policy for this problem is unknown, and the state of the art is difficult to pin down because details of commercial dispatching strategies are proprietary, these learned dispatchers appeared to perform very well.

## 14.5 Dynamic Channel Allocation

An important problem in the operation of a cellular telephone system is how to efficiently use the available bandwidth to provide good service to as many customers as possible. This problem is becoming critical with the rapid growth in the use of cellular telephones. Here we describe a study due to Singh and Bertsekas (1997) in which they applied reinforcement learning to this problem.

Mobile telephone systems take advantage of the fact that a communication channel—a band of frequencies—can be used simultaneously by many callers if these callers are spaced physically far enough apart that their calls do not interfere with each another. The minimum distance at which there is no interference is called the channel reuse constraint. In a cellular telephone system, the service area is divided into a number of regions called cells. In each cell is a base station that handles all the calls made within the cell. The total available bandwidth is divided permanently into a number of channels. Channels must then be allocated to cells and to calls made within cells without violating the channel reuse constraint. There are a great many ways to do this, some of which are better than others in terms of how reliably they make channels available to new calls, or to calls that are “handed off” from one cell to another as the caller crosses a cell boundary. If no channel is available for a new or a handed-off call, the call is lost, or blocked. Singh and Bertsekas considered the problem of allocating channels so that the number of blocked calls is minimized.

A simple example provides some intuition about the nature of the problem. Imagine a situation with three cells sharing two channels. The three cells are arranged in a line where no two adjacent cells can use the same channel without violating the channel reuse constraint. If the left cell is serving a call on channel 1 while the right cell is serving another call on channel 2, as in the left diagram below, then any new call arriving in the middle cell must be blocked.

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_352_204_544_272.jpg" alt="Image" width="15%" /></div>

<div style="text-align: center;"><img src="imgs/img_in_image_box_679_204_869_272.jpg" alt="Image" width="15%" /></div>

Obviously, it would be better for both the left and the right cells to use channel 1 for their calls. Then a new call in the middle cell could be assigned channel 2, as in the right diagram, without violating the channel reuse constraint. Such interactions and possible optimizations are typical of the channel assignment problem. In larger and more realistic cases with many cells, channels, and calls, and uncertainty about when and where new calls will arrive or existing calls will have to be handed off, the problem of allocating channels to minimize blocking can become extremely complex.

The simplest approach is to permanently assign channels to cells in such a way that the channel reuse constraint can never be violated even if all channels of all cells are used simultaneously. This is called a fixed assignment method. In a dynamic assignment method, in contrast, all channels are potentially available to all cells and are assigned to cells dynamically as calls arrive. If this is done right, it can take advantage of temporary changes in the spatial and temporal distribution of calls in order to serve more users. For example, when calls are concentrated in a few cells, these cells can be assigned more channels without increasing the blocking rate in the lightly used cells.

The channel assignment problem can be formulated as a semi-Markov decision process much as the elevator dispatching problem was in the previous section. A state in the semi-MDP formulation has two components. The first is the configuration of the entire cellular system that gives for each cell the usage state (occupied or unoccupied) of each channel for that cell. A typical cellular system with 49 cells and 70 channels has a staggering  $70^{49}$ configurations, ruling out the use of conventional dynamic programming methods. The other state component is an indicator of what kind of event caused a state transition: arrival, departure, or handoff. This state component determines what kinds of actions are possible. When a call arrives, the possible actions are to assign it a free channel or to block it if no channels are available. When a call departs, that is, when a caller hangs up, the system is allowed to reassign the channels in use in that cell in an attempt to create a better configuration. At time t the immediate reward,  $R_{t}$, is the number of calls taking place at that time, and the return is

 
$$
G_{t}=\int_{0}^{\infty}e^{-\beta\tau}R_{t+\tau}d\tau,
$$
 

where  $\beta > 0$ plays a role similar to that of the discount-rate parameter  $\gamma$. Maximizing the expectation of this return is the same as minimizing the expected (discounted) number of calls blocked over an infinite horizon.

---

This is another problem greatly simplified if treated in terms of afterstates (Section 6.6). For each state and action, the immediate result is a new configuration, an afterstate. A value function is learned over just these configurations. To select among the possible actions, the resulting configuration was determined and evaluated. The action was then selected that would lead to the configuration of highest estimated value. For example, when a new call arrived at a cell, it could be assigned to any of the free channels, if there were any; otherwise, it had to be blocked. The new configuration that would result from each assignment was easy to compute because it was always a simple deterministic consequence of the assignment. When a call terminated, the newly released channel became available for reassigning to any of the ongoing calls. In this case, the actions of reassigning each ongoing call in the cell to the newly released channel were considered. An action was then selected leading to the configuration with the highest estimated value.

Linear function approximation was used for the value function: the estimated value of a configuration was a weighted sum of features. Configurations were represented by two sets of features: an availability feature for each cell and a packing feature for each cell–channel pair. For any configuration, the availability feature for a cell gave the number of additional calls it could accept without conflict if the rest of the cells were frozen in the current configuration. For any given configuration, the packing feature for a cell–channel pair gave the number of times that channel was being used in that configuration within a four-cell radius of that cell. All of these features were normalized to lie between -1 and 1. A semi-Markov version of linear TD(0) was used to update the weights.

Singh and Bertsekas compared three channel allocation methods using a simulation of a  $7 \times 7$ cellular array with 70 channels. The channel reuse constraint was that calls had to be 3 cells apart to be allowed to use the same channel. Calls arrived at cells randomly according to Poisson distributions possibly having different means for different cells, and call durations were determined randomly by an exponential distribution with a mean of three minutes. The methods compared were a fixed assignment method (FA), a dynamic allocation method called “borrowing with directional channel locking” (BDCL), and the reinforcement learning method (RL). BDCL (Zhang and Yum, 1989) was the best dynamic channel allocation method they found in the literature. It is a heuristic method that assigns channels to cells as in FA, but channels can be borrowed from neighboring cells when needed. It orders the channels in each cell and uses this ordering to determine which channels to borrow and how calls are dynamically reassigned channels within a cell.

Figure 14.10 shows the blocking probabilities of these methods for mean arrival rates of 150, 200, and 350 calls/hour as well as for a case in which

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_322_204_893_535.jpg" alt="Image" width="46%" /></div>

<div style="text-align: center;">Figure 14.10: Performance of FA, BDCL, and RL channel allocation methods for different mean call arrival rates.</div>

different cells had different mean arrival rates. The reinforcement learning method learned on-line. The data shown are for its asymptotic performance, but in fact learning was rapid. The RL method blocked calls less frequently than did the other methods for all arrival rates and soon after starting to learn. Note that the differences between the methods decreased as the call arrival rate increased. This is to be expected because as the system gets saturated with calls there are fewer opportunities for a dynamic allocation method to set up favorable usage patterns. In practice, however, it is the performance of the unsaturated system that is most important. For marketing reasons, cellular telephone systems are built with enough capacity that more than 10% blocking is rare.

Nie and Haykin (1996) also studied the application of reinforcement learning to dynamic channel allocation. They formulated the problem somewhat differently than Singh and Bertsekas did. Instead of trying to minimize the probability of blocking a call directly, their system tried to minimize a more indirect measure of system performance. Cost was assigned to patterns of channel use depending on the distances between calls using the same channels. Patterns in which channels were being used by multiple calls that were close to each other were favored over patterns in which channel-sharing calls were far apart. Nie and Haykin compared their system with a method called MAXAVAIL (Sivarajan, McEliece, and Ketchum, 1990), considered to be one of the best dynamic channel allocation methods. For each new call, it selects the channel that maximizes the total number of channels available in the entire system. Nie and Haykin showed that the blocking probability achieved by their reinforcement learning system was closely comparable to that of MAXAVAIL under a variety of conditions in a 49-cell, 70-channel simulation. A

---

key point, however, is that the allocation policy produced by reinforcement learning can be implemented on-line much more efficiently than MAXAVAIL, which requires so much on-line computation that it is not feasible for large systems.

The studies we described in this section are so recent that the many questions they raise have not yet been answered. We can see, though, that there can be different ways to apply reinforcement learning to the same real-world problem. In the near future, we expect to see many refinements of these applications, as well as many new applications of reinforcement learning to problems arising in communication systems.

## 14.6 Job-Shop Scheduling

Many jobs in industry and elsewhere require completing a collection of tasks while satisfying temporal and resource constraints. Temporal constraints say that some tasks have to be finished before others can be started; resource constraints say that two tasks requiring the same resource cannot be done simultaneously (e.g., the same machine cannot do two tasks at once). The objective is to create a schedule specifying when each task is to begin and what resources it will use that satisfies all the constraints while taking as little overall time as possible. This is the job-shop scheduling problem. In its general form, it is NP-complete, meaning that there is probably no efficient procedure for exactly finding shortest schedules for arbitrary instances of the problem. Job-shop scheduling is usually done using heuristic algorithms that take advantage of special properties of each specific instance.

Zhang and Dietterich (1995, 1996; Zhang, 1996) were motivated to apply reinforcement learning to job-shop scheduling because the design of domain-specific, heuristic algorithms can be expensive and time-consuming. Their goal was to show how reinforcement learning can be used to learn how to quickly find constraint-satisfying schedules of short duration in specific domains, thereby reducing the amount of hand engineering required. They addressed the NASA space shuttle payload processing problem (SSPP), which requires scheduling the tasks required for installation and testing of shuttle cargo bay payloads. An SSPP typically requires scheduling for two to six shuttle missions, each requiring between 34 and 164 tasks. An example of a task is MISSION-SEQUENCE-TEST, which has a duration of 7200 time units and requires the following resources: two quality control officers, two technicians, one ATE, one SPCDS, and one HITS. Some resources are divided into pools, and if a task needs more than one resource of a specific type, the resources must belong to the same pool, and the pool has to be the right one.

---

For example, if a task needs two quality control officers, they both have to be in the pool of quality control officers working on the same shift at the right site. It is not too hard to find a conflict-free schedule for a job, one that meets all the temporal and resource constraints, but the objective is to find a conflict-free schedule with the shortest possible total duration, which is much more difficult.

How can you do this using reinforcement learning? Job-shop scheduling is usually formulated as a search in the space of schedules, what is called a discrete, or combinatorial, optimization problem. A typical solution method would sequentially generate schedules, attempting to improve each over its predecessor in terms of constraint violations and duration (a hill-climbing, or local search, method). You could think of this as a nonassociative reinforcement learning problem of the type we discussed in Chapter 2 with a very large number of possible actions: all the possible schedules! But aside from the problem of having so many actions, any solution obtained this way would just be a single schedule for a single job instance. In contrast, what Zhang and Dietterich wanted their learning system to end up with was a policy that could quickly find good schedules for any SSPP. They wanted it to learn a skill for job-shop scheduling in this specific domain.

For clues about how to do this, they looked to an existing optimization approach to SSPP, in fact, the one actually in use by NASA at the time of their research: the iterative repair method developed by Zweben and Daun (1994). The starting point for the search is a critical path schedule, a schedule that meets the temporal constraints but ignores the resource constraints. This schedule can be constructed efficiently by scheduling each task prior to launch as late as the temporal constraints permit, and each task after landing as early as these constraints permit. Resource pools are assigned randomly. Two types of operators are used to modify schedules. They can be applied to any task that violates a resource constraint. A REASSIGN-POOL operator changes the pool assigned to one of the task's resources. This type of operator applies only if it can reassign a pool so that the resource requirement is satisfied. A MOVE operator moves a task to the first earlier or later time at which its resource needs can be satisfied and uses the critical path method to reschedule all of the task's temporal dependents.

At each step of the iterative repair search, one operator is applied to the current schedule, selected according to the following rules. The earliest task with a resource constraint violation is found, and a REASSIGN-POOL operator is applied to this task if possible. If more than one applies, that is, if several different pool reassignments are possible, one is selected at random. If no REASSIGN-POOL operator applies, then a MOVE operator is selected at random based on a heuristic that prefers short-distance moves of tasks having

---

few temporal dependents and whose resource requirements are close to the task's overallocation. After an operator is applied, the number of constraint violations of the resulting schedule is determined. A simulated annealing procedure is used to decide whether to accept or reject this new schedule. If  $\Delta V$ denotes the number of constraint violations removed by the repair, then the new schedule is accepted with probability  $\exp(-\Delta V/T)$, where T is the current computational temperature that is gradually decreased throughout the search. If accepted, the new schedule becomes the current schedule for the next iteration; otherwise, the algorithm attempts to repair the old schedule again, which will usually produce different results due to the random decisions involved. Search stops when all constraints are satisfied. Short schedules are obtained by running the algorithm several times and selecting the shortest of the resulting conflict-free schedules.

Zhang and Dietterich treated entire schedules as states in the sense of reinforcement learning. The actions were the applicable REASSIGN-POOL and MOVE operators, typically numbering about 20. The problem was treated as episodic, each episode starting with the same critical path schedule that the iterative repair algorithm would start with and ending when a schedule was found that did not violate any constraint. The initial state—a critical path schedule—is denoted  $S_0$. The rewards were designed to promote the quick construction of conflict-free schedules of short duration. The system received a small negative reward  $(-0.001)$ on each step that resulted in a schedule that still violated a constraint. This encouraged the agent to find conflict-free schedules quickly, that is, with a small number of repairs to  $S_0$. Encouraging the system to find short schedules is more difficult because what it means for a schedule to be short depends on the specific SSPP instance. The shortest schedule for a difficult instance, one with a lot of tasks and constraints, will be longer than the shortest schedule for a simpler instance. Zhang and Dietterich devised a formula for a resource dilation factor (RDF), intended to be an instance-independent measure of a schedule's duration. To account for an instance's intrinsic difficulty, the formula makes use of a measure of the resource overallocation of  $S_0$. Since longer schedules tend to produce larger RDFs, the negative of the RDF of the final conflict-free schedule was used as a reward at the end of each episode. With this reward function, if it takes N repairs starting from a schedule s to obtain a final conflict-free schedule,  $S_f$, the return from s is  $-RDF(S_f) - 0.001(N - 1)$.

This reward function was designed to try to make a system learn to satisfy the two goals of finding conflict-free schedules of short duration and finding conflict-free schedules quickly. But the reinforcement learning system really has only one goal—maximizing expected return—so the particular reward values determine how a learning system will tend to trade off these two goals.

---

Setting the immediate reward to the small value of -0.001 means that the learning system will regard one repair, one step in the scheduling process, as being worth 0.001 units of RDF. So, for example, if from some schedule it is possible to produce a conflict-free schedule with one repair or with two, an optimal policy will take extra repair only if it promises a reduction in final RDF of more than 0.001.

Zhang and Dietterich used TD( $\lambda$) to learn the value function. Function approximation was by a multilayer neural network trained by backpropagating TD errors. Actions were selected by an  $\varepsilon$-greedy policy, with  $\varepsilon$ decreasing during learning. One-step lookahead search was used to find the greedy action. Their knowledge of the problem made it easy to predict the schedules that would result from each repair operation. They experimented with a number of modifications to this basic procedure to improve its performance. One was to use the TD( $\lambda$) algorithm backward after each episode, with the eligibility trace extending to future rather than to past states. Their results suggested that this was more accurate and efficient than forward learning. In updating the weights of the network, they also sometimes performed multiple weight updates when the TD error was large. This is apparently equivalent to dynamically varying the step-size parameter in an error-dependent way during learning.

They also tried an experience replay technique due to Lin (1992). At any point in learning, the agent remembered the best episode up to that point. After every four episodes, it replayed this remembered episode, learning from it as if it were a new episode. At the start of training, they similarly allowed the system to learn from episodes generated by a good scheduler, and these could also be replayed later in learning. To make the lookahead search faster for large-scale problems, which typically had a branching factor of about 20, they used a variant they called random sample greedy search that estimated the greedy action by considering only random samples of actions, increasing the sample size until a preset confidence was reached that the greedy action of the sample was the true greedy action. Finally, having discovered that learning could be slowed considerably by excessive looping in the scheduling process, they made their system explicitly check for loops and alter action selections when a loop was detected. Although all of these techniques could improve the efficiency of learning, it is not clear how crucial all of them were for the success of the system.

Zhang and Dietterich experimented with two different network architectures. In the first version of their system, each schedule was represented using a set of 20 handcrafted features. To define these features, they studied small scheduling problems to find features that had some ability to predict RDF. For example, experience with small problems showed that only four of the resource pools tended to cause allocation problems. The mean and standard deviation

---

of each of these pools' unused portions over the entire schedule were computed, resulting in 10 real-valued features. Two other features were the RDF of the current schedule and the percentage of its duration during which it violated resource constraints. The network had 20 input units, one for each feature, a hidden layer of 40 sigmoidal units, and an output layer of 8 sigmoidal units. The output units coded the value of a schedule using a code in which, roughly, the location of the activity peak over the 8 units represented the value. Using the appropriate TD error, the network weights were updated using error backpropagation, with the multiple weight-update technique mentioned above.

The second version of the system (Zhang and Dietterich, 1996) used a more complicated time-delay neural network (TDNN) borrowed from the field of speech recognition (Lang, Waibel, and Hinton, 1990). This version divided each schedule into a sequence of blocks (maximal time intervals during which tasks and resource assignments did not change) and represented each block by a set of features similar to those used in the first program. It then scanned a set of “kernel” networks across the blocks to create a set of more abstract features. Since different schedules had different numbers of blocks, another layer averaged these abstract features over each third of the blocks. Then a final layer of 8 sigmoidal output units represented the schedule’s value using the same code as in the first version of the system. In all, this network had 1123 adjustable weights.

A set of 100 artificial scheduling problems was constructed and divided into subsets used for training, determining when to stop training (a validation set), and final testing. During training they tested the system on the validation set after every 100 episodes and stopped training when performance on the validation set stopped changing, which generally took about 10,000 episodes. They trained networks with different values of  $\lambda$ (0.2 and 0.7), with three different training sets, and they saved both the final set of weights and the set of weights producing the best performance on the validation set. Counting each set of weights as a different network, this produced 12 networks, each of which corresponded to a different scheduling algorithm.

Figure 14.11 shows how the mean performance of the 12 TDNN networks (labeled G12TDN) compared with the performances of two versions of Zweben and Daun's iterative repair algorithm, one using the number of constraint violations as the function to be minimized by simulated annealing (IR-V) and the other using the RDF measure (IR-RDF). The figure also shows the performance of the first version of their system that did not use a TDNN (G12N). The mean RDF of the best schedule found by repeatedly running an algorithm is plotted against the total number of schedule repairs (using a log scale). These results show that the learning system produced scheduling algorithms that needed many fewer repairs to find conflict-free schedules of the

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_252_208_970_588.jpg" alt="Image" width="58%" /></div>

<div style="text-align: center;">Figure 14.11: Comparison of accepted schedule repairs. Reprinted with permission from Zhang and Dietterich, 1996.</div>

same quality as those found by the iterative repair algorithms. Figure 14.12 compares the computer time required by each scheduling algorithm to find schedules of various RDFs. According to this measure of performance, the best trade-off between computer time and schedule quality is produced by the non-TDNN algorithm (G12N). The TDNN algorithm (G12TDN) suffered due to the time it took to apply the kernel-scanning process, but Zhang and Dietterich point out that there are many ways to make it run faster.

These results do not unequivocally establish the utility of reinforcement learning for job-shop scheduling or for other difficult search problems. But they do suggest that it is possible to use reinforcement learning methods to learn how to improve the efficiency of search. Zhang and Dietterich's job-shop scheduling system is the first successful instance of which we are aware in which reinforcement learning was applied in plan-space, that is, in which states are complete plans (job-shop schedules in this case), and actions are plan modifications. This is a more abstract application of reinforcement learning than we are used to thinking about. Note that in this application the system learned not just to efficiently create one good schedule, a skill that would not be particularly useful; it learned how to quickly find good schedules for a class of related scheduling problems. It is clear that Zhang and Dietterich went through a lot of trial-and-error learning of their own in developing this example. But remember that this was a groundbreaking exploration of a new aspect of reinforcement learning. We expect that future applications of this kind and complexity will become more routine as experience accumulates.

---

<div style="text-align: center;"><img src="imgs/img_in_chart_box_252_588_964_973.jpg" alt="Image" width="58%" /></div>

<div style="text-align: center;">Figure 14.12: Comparison of CPU time. Reprinted with permission from Zhang and Dietterich, 1996.</div>


---



---

### Chapter 15

### Prospects

In this book we have tried to present reinforcement learning not as a collection of individual methods, but as a coherent set of ideas cutting across methods. Each idea can be viewed as a dimension along which methods vary. The set of such dimensions spans a large space of possible methods. By exploring this space at the level of dimensions we hope to obtain the broadest and most lasting understanding. In this chapter we use the concept of dimensions in method space to recapitulate the view of reinforcement learning we have developed in this book and to identify some of the more important gaps in our coverage of the field.

## 15.1 The Unified View

All of the reinforcement learning methods we have explored in this book have three key ideas in common. First, the objective of all of them is the estimation of value functions. Second, all operate by backing up values along actual or possible state trajectories. Third, all follow the general strategy of generalized policy iteration (GPI), meaning that they maintain an approximate value function and an approximate policy, and they continually try to improve each on the basis of the other. These three ideas that the methods have in common circumscribe the subject covered in this book. We suggest that value functions, backups, and GPI are powerful organizing principles potentially relevant to any model of intelligence.

Two of the most important dimensions along which the methods vary are shown in Figure 15.1. These dimensions have to do with the kind of backup used to improve the value function. The horizontal dimension is whether they are sample backups (based on a sample trajectory) or full backups (based

---

<div style="text-align: center;"><img src="imgs/img_in_image_box_273_258_943_868.jpg" alt="Image" width="54%" /></div>

<div style="text-align: center;">Figure 15.1: A slice of the space of reinforcement learning methods.</div>

on a distribution of possible trajectories). Full backups of course require a model, whereas sample backups can be done either with or without a model (another dimension of variation). The vertical dimension corresponds to the depth of backups, that is, to the degree of bootstrapping. At three of the four corners of the space are the three primary methods for estimating values: DP, TD, and Monte Carlo. Along the left edge of the space are the sample-backup methods, ranging from one-step TD backups to full-return Monte Carlo backups. Between these is a spectrum including methods based on n-step backups and mixtures of n-step backups such as the  $\lambda$-backups implemented by eligibility traces.

DP methods are shown in the extreme upper-right corner of the space because they involve one-step full backups. The lower-right corner is the extreme case of full backups so deep that they run all the way to terminal states (or, in a continuing task, until discounting has reduced the contribution of any further rewards to a negligible level). This is the case of exhaustive search. Intermedi

---

ate methods along this dimension include heuristic search and related methods that search and backup up to a limited depth, perhaps selectively. There are also methods that are intermediate along the horizontal dimension. These include methods that mix full and sample backups, as well as the possibility of methods that mix samples and distributions within a single backup. The interior of the square is filled in to represent the space of all such intermediate methods.

A third important dimension is that of function approximation. Function approximation can be viewed as an orthogonal spectrum of possibilities ranging from tabular methods at one extreme through state aggregation, a variety of linear methods, and then a diverse set of nonlinear methods. This third dimension might be visualized as perpendicular to the plane of the page in Figure 15.1.

Another dimension that we heavily emphasized in this book is the binary distinction between on-policy and off-policy methods. In the former case, the agent learns the value function for the policy it is currently following, whereas in the latter case it learns the value function for the policy that it currently thinks is best. These two policies are often different because of the need to explore. The interaction between this dimension and the bootstrapping and function approximation dimension discussed in Chapter 9 illustrates the advantages of analyzing the space of methods in terms of dimensions. Even though this did involve an interaction between three dimensions, many other dimensions were found to be irrelevant, greatly simplifying the analysis and increasing its significance.

In addition to the four dimensions just discussed, we have identified a number of others throughout the book:

Definition of return Is the task episodic or continuing, discounted or undiscounted?

Action values vs. state values vs. afterstate values What kind of values should be estimated? If only state values are estimated, then either a model or a separate policy (as in actor-critic methods) is required for action selection.

Action selection/exploration How are actions selected to ensure a suitable trade-off between exploration and exploitation? We have considered only the simplest ways to do this:  $\varepsilon$-greedy and softmax action selection, and optimistic initialization of values.

Synchronous vs. asynchronous Are the backups for all states performed simultaneously or one by one in some order?

---

Replacing vs. accumulating traces If eligibility traces are used, which kind is most appropriate?

Real vs. simulated Should one backup real experience or simulated experience? If both, how much of each?

Location of backups What states or state-action pairs should be backed up? Modelfree methods can choose only among the states and state-action pairs actually encountered, but model-based methods can choose arbitrarily. There are many potent possibilities here.

Timing of backups Should backups be done as part of selecting actions, or only afterward?

Memory for backups How long should backed-up values be retained? Should they be retained permanently, or only while computing an action selection, as in heuristic search?

Of course, these dimensions are neither exhaustive nor mutually exclusive. Individual algorithms differ in many other ways as well, and many algorithms lie in several places along several dimensions. For example, Dyna methods use both real and simulated experience to affect the same value function. It is also perfectly sensible to maintain multiple value functions computed in different ways or over different state and action representations. These dimensions do, however, constitute a coherent set of ideas for describing and exploring a wide space of possible methods.

## 15.2 State Estimation

## 15.3 Temporal Abstraction

## 15.4 Predictive Representations

## 15.5 Other Frontier Dimensions

Much research remains to be done within this space of reinforcement learning methods. For example, even for the tabular case no control method using multistep backups has been proved to converge to an optimal policy. Among planning methods, basic ideas such as trajectory sampling and focusing sample backups are almost completely unexplored. On closer inspection, parts of the

---

space will undoubtedly turn out to have far greater complexity and greater internal structure than is now apparent. There are also other dimensions along which reinforcement learning can be extended, we have not yet mentioned, that lead to a much larger space of methods. Here we identify some of these dimensions and note some of the open questions and frontiers that have been left out of the preceding chapters.

One of the most important extensions of reinforcement learning beyond what we have treated in this book is to eliminate the requirement that the state representation have the Markov property. There are a number of interesting approaches to the non-Markov case. Most strive to construct from the given state signal and its past values a new signal that is Markov, or more nearly Markov. For example, one approach is based on the theory of partially observable MDPs (POMDPs). POMDPs are finite MDPs in which the state is not observable, but another “sensation” signal stochastically related to the state is observable. The theory of POMDPs has been extensively studied for the case of complete knowledge of the dynamics of the POMDP. In this case, Bayesian methods can be used to compute at each time step the probability of the environment’s being in each state of the underlying MDP. This probability distribution can then be used as a new state signal for the original problem. The downside for the Bayesian POMDP approach is its computational expense and its strong reliance on complete environment models. Some of the recent work pursuing this approach is by Littman, Cassandra, and Kaelbling (1995), Parr and Russell (1995), and Chrisman (1992). If we are not willing to assume a complete model of a POMDP’s dynamics, then existing theory seems to offer little guidance. Nevertheless, one can still attempt to construct a Markov state signal from the sequence of sensations. Various statistical and ad hoc methods along these lines have been explored (e.g., Chrisman, 1992; McCallum, 1993, 1995; Lin and Mitchell, 1992; Chapman and Kaelbling, 1991; Moore, 1994; Rivest and Schapire, 1987; Colombetti and Dorigo, 1994; Whitehead and Ballard, 1991; Hochreiter and Schmidhuber, 1997).

All of the above methods involve constructing an improved state representation from the non-Markov one provided by the environment. Another approach is to leave the state representation unchanged and use methods that are not too adversely affected by its being non-Markov (e.g., Singh, Jaakkola, and Jordan, 1994, 1995; Jaakkola, Singh and Jordan, 1995). In fact, most function approximation methods can be viewed in this way. For example, state aggregation methods for function approximation are in effect equivalent to a non-Markov representation in which all members of a set of states are mapped into a common sensation. There are other parallels between the issues of function approximation and non-Markov representations. In both cases the overall problem divides into two parts: constructing an improved representation, and

---

making do with the current representation. In both cases the “making do” part is relatively well understood, whereas the constructive part is unclear and wide open. At this point we can only guess as to whether or not these parallels point to any common solution methods for the two problems.

Another important direction for extending reinforcement learning beyond what we have covered in this book is to incorporate ideas of modularity and hierarchy. Introductory reinforcement learning is about learning value functions and one-step models of the dynamics of the environment. But much of what people learn does not seem to fall exactly into either of these categories. For example, consider what we know about tying our shoes, making a phone call, or traveling to London. Having learned how to do such things, we are then able to choose among them and plan as if they were primitive actions. What we have learned in order to do this are not conventional value functions or one-step models. We are able to plan and learn at a variety of levels and flexibly interrelate them. Much of our learning appears not to be about learning values directly, but about preparing us to quickly estimate values later in response to new situations or new information. Considerable reinforcement learning research has been directed at capturing such abilities (e.g., Watkins, 1989; Dayan and Hinton, 1993; Singh, 1992a, 1992b; Ring, 1994, Kaelbling, 1993b; Sutton, 1995).

Researchers have also explored ways of using the structure of particular tasks to advantage. For example, many problems have state representations that are naturally lists of variables, like the readings of multiple sensors or actions that are lists of component actions. The independence or near independence of some variables from others can sometimes be exploited to obtain more efficient special forms of reinforcement learning algorithms. It is sometimes even possible to decompose a problem into several independent subproblems that can be solved by separate learning agents. A reinforcement learning problem can usually be structured in many different ways, some reflecting natural aspects of the problem, such as the existence of physical sensors, and others being the result of explicit attempts to decompose the problem into simpler subproblems. Possibilities for exploiting structure in reinforcement learning and related planning problems have been studied by many researchers (e.g., Boutilier, Dearden, and Goldszmidt, 1995; Dean and Lin, 1995). There are also related studies of multiagent or distributed reinforcement learning (e.g., Littman, 1994; Markey, 1994; Crites and Barto, 1996; Tan, 1993).

Finally, we want to emphasize that reinforcement learning is meant to be a general approach to learning from interaction. It is general enough not to require special-purpose teachers and domain knowledge, but also general enough to utilize such things if they are available. For example, it is often possible to accelerate reinforcement learning by giving advice or hints to the agent.

---

## 15.5. OTHER FRONTIER DIMENSIONS

(Clouse and Utgoff, 1992; Maclin and Shavlik, 1994) or by demonstrating instructive behavioral trajectories (Lin, 1992). Another way to make learning easier, related to “shaping” in psychology, is to give the learning agent a series of relatively easy problems building up to the harder problem of ultimate interest (e.g., Selfridge, Sutton, and Barto, 1985). These methods, and others not yet developed, have the potential to give the machine-learning terms training and teaching new meanings that are closer to their meanings for animal and human learning.

---



---

## References

Agrawal, R. (1995). Sample mean based index policies with  $O(\log n)$ regret for the multi-armed bandit problem. Advances in Applied Probability, 27:1054–1078.

Agre, P. E. (1988). The Dynamic Structure of Everyday Life. Ph.D. thesis, Massachusetts Institute of Technology. AI-TR 1085, MIT Artificial Intelligence Laboratory.

Agre, P. E., Chapman, D. (1990). What are plans for? Robotics and Autonomous Systems, 6:17–34.

Albus, J. S. (1971). A theory of cerebellar function. Mathematical Biosciences, 10:25–61.

Albus, J. S. (1981). Brain, Behavior, and Robotics. Byte Books, Peterborough, NH.

Anderson, C. W. (1986). Learning and Problem Solving with Multilayer Connectionist Systems. Ph.D. thesis, University of Massachusetts, Amherst.

Anderson, C. W. (1987). Strategy learning with multilayer connectionist representations. Proceedings of the Fourth International Workshop on Machine Learning, pp. 103–114. Morgan Kaufmann, San Mateo, CA.

Anderson, J. A., Silverstein, J. W., Ritz, S. A., Jones, R. S. (1977). Distinctive features, categorical perception, and probability learning: Some applications of a neural model. Psychological Review, 84:413–451.

Andreae, J. H. (1963). STELLA: A scheme for a learning machine. In Proceedings of the 2nd IFAC Congress, Basle, pp. 497–502. Butterworths, London.

Andreae, J. H. (1969a). A learning machine with monologue. International Journal of Man-Machine Studies, 1:1–20.

Andreae, J. H. (1969b). Learning machines—a unified view. In A. R. Meetham and R. A. Hudson (eds.), Encyclopedia of Information, Linguistics, and Control, pp. 261–270. Pergamon, Oxford.

---

Andreae, J. H. (1977). Thinking with the Teachable Machine. Academic Press, London.

Arthur, W. B. (1991). Designing economic agents that act like human agents: A behavioral approach to bounded rationality. The American Economic Review 81(2):353-359.

Auer, P., Cesa-Bianchi, N., Fischer, P. (2002). Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2-3):235–256.

Baird, L. C. (1995). Residual algorithms: Reinforcement learning with function approximation. In Proceedings of the Twelfth International Conference on Machine Learning, pp. 30–37. Morgan Kaufmann, San Francisco.

Bao, G., Cassandras, C. G., Djaferis, T. E., Gandhi, A. D., Looze, D. P. (1994). Elevator dispatchers for down peak traffic. Technical report. ECE Department, University of Massachusetts, Amherst.

Barnard, E. (1993). Temporal-difference methods and Markov models. IEEE Transactions on Systems, Man, and Cybernetics, 23:357–365.

Barto, A. G. (1985). Learning by statistical cooperation of self-interested neuron-like computing elements. Human Neurobiology, 4:229–256.

Barto, A. G. (1986). Game-theoretic cooperativity in networks of self-interested units. In J. S. Denker (ed.), Neural Networks for Computing, pp. 41–46. American Institute of Physics, New York.

Barto, A. G. (1990). Connectionist learning for control: An overview. In T. Miller, R. S. Sutton, and P. J. Werbos (eds.), Neural Networks for Control, pp. 5–58. MIT Press, Cambridge, MA.

Barto, A. G. (1991). Some learning tasks from a control perspective. In L. Nadel and D. L. Stein (eds.), 1990 Lectures in Complex Systems, pp. 195–223. Addison-Wesley, Redwood City, CA.

Barto, A. G. (1992). Reinforcement learning and adaptive critic methods. In D. A. White and D. A. Sofge (eds.), Handbook of Intelligent Control: Neural, Fuzzy, and Adaptive Approaches, pp. 469–491. Van Nostrand Reinhold, New York.

Barto, A. G. (1995a). Adaptive critics and the basal ganglia. In J. C. Houk, J. L. Davis, and D. G. Beiser (eds.), Models of Information Processing in the Basal Ganglia, pp. 215–232. MIT Press, Cambridge, MA.

Barto, A. G. (1995b). Reinforcement learning. In M. A. Arbib (ed.), Handbook of Brain Theory and Neural Networks, pp. 804–809. MIT Press, Cambridge, MA.

Barto, A. G., Anandan, P. (1985). Pattern recognizing stochastic learning

---

automata. IEEE Transactions on Systems, Man, and Cybernetics, 15:360–375.

Barto, A. G., Anderson, C. W. (1985). Structural learning in connectionist systems. In Program of the Seventh Annual Conference of the Cognitive Science Society, pp. 43–54.

Barto, A. G., Anderson, C. W., Sutton, R. S. (1982). Synthesis of nonlinear control surfaces by a layered associative search network. Biological Cybernetics, 43:175–185.

Barto, A. G., Bradtke, S. J., Singh, S. P. (1991). Real-time learning and control using asynchronous dynamic programming. Technical Report 91-57. Department of Computer and Information Science, University of Massachusetts, Amherst.

Barto, A. G., Bradtke, S. J., Singh, S. P. (1995). Learning to act using real-time dynamic programming. Artificial Intelligence, 72:81–138.

Barto, A. G., Duff, M. (1994). Monte Carlo matrix inversion and reinforcement learning. In J. D. Cohen, G. Tesauro, and J. Alspector (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1993 Conference, pp. 687–694. Morgan Kaufmann, San Francisco.

Barto, A. G., Jordan, M. I. (1987). Gradient following without back-propagation in layered networks. In M. Caudill and C. Butler (eds.), Proceedings of the IEEE First Annual Conference on Neural Networks, pp. II629–II636. SOS Printing, San Diego, CA.

Barto, A. G., Sutton, R. S. (1981a). Goal seeking components for adaptive intelligence: An initial assessment. Technical Report AFWAL-TR-81-1070. Air Force Wright Aeronautical Laboratories/Avionics Laboratory, Wright-Patterson AFB, OH.

Barto, A. G., Sutton, R. S. (1981b). Landmark learning: An illustration of associative search. Biological Cybernetics, 42:1–8.

Barto, A. G., Sutton, R. S. (1982). Simulation of anticipatory responses in classical conditioning by a neuron-like adaptive element. Behavioural Brain Research, 4:221–235.

Barto, A. G., Sutton, R. S., Anderson, C. W. (1983). Neuronlike elements that can solve difficult learning control problems. IEEE Transactions on Systems, Man, and Cybernetics, 13:835–846. Reprinted in J. A. Anderson and E. Rosenfeld (eds.), Neurocomputing: Foundations of Research, pp. 535–549. MIT Press, Cambridge, MA, 1988.

Barto, A. G., Sutton, R. S., Brouwer, P. S. (1981). Associative search net-

---

work: A reinforcement learning associative memory. Biological Cybernetics, 40:201–211.

Bellman, R. E. (1956). A problem in the sequential design of experiments. Sankhya, 16:221–229.

Bellman, R. E. (1957a). Dynamic Programming. Princeton University Press, Princeton.

Bellman, R. E. (1957b). A Markov decision process. Journal of Mathematical Mechanics, 6:679–684.

Bellman, R. E., Dreyfus, S. E. (1959). Functional approximations and dynamic programming. Mathematical Tables and Other Aids to Computation, 13:247–251.

Bellman, R. E., Kalaba, R., Kotkin, B. (1973). Polynomial approximation—A new computational technique in dynamic programming: Allocation processes. Mathematical Computation, 17:155–161.

Berry, D. A., Fristedt, B. (1985). Bandit Problems. Chapman and Hall, London.

Bertsekas, D. P. (1982). Distributed dynamic programming. IEEE Transactions on Automatic Control, 27:610–616.

Bertsekas, D. P. (1983). Distributed asynchronous computation of fixed points. Mathematical Programming, 27:107–120.

Bertsekas, D. P. (1987). Dynamic Programming: Deterministic and Stochastic Models. Prentice-Hall, Englewood Cliffs, NJ.

Bertsekas, D. P. (1995). Dynamic Programming and Optimal Control. Athena Scientific, Belmont, MA.

Bertsekas, D. P., Tsitsiklis, J. N. (1989). Parallel and Distributed Computation: Numerical Methods. Prentice-Hall, Englewood Cliffs, NJ.

Bertsekas, D. P., Tsitsiklis, J. N. (1996). Neuro-Dynamic Programming. Athena Scientific, Belmont, MA.

Biermann, A. W., Fairfield, J. R. C., Beres, T. R. (1982). Signature table systems and learning. IEEE Transactions on Systems, Man, and Cybernetics, 12:635–648.

Booker, L. B. (1982). Intelligent Behavior as an Adaptation to the Task Environment. Ph.D. thesis, University of Michigan, Ann Arbor.

Bishop, C. M. (1995). Neural Networks for Pattern Recognition. Clarendon, Oxford.

---

Boone, G. (1997). Minimum-time control of the acrobot. In 1997 International Conference on Robotics and Automation, pp. 3281–3287. IEEE Robotics and Automation Society.

Boutilier, C., Dearden, R., Goldszmidt, M. (1995). Exploiting structure in policy construction. In Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence, pp. 1104–1111. Morgan Kaufmann.

Boyan, J. A., Moore, A. W. (1995). Generalization in reinforcement learning: Safely approximating the value function. In G. Tesauro, D. S. Touretzky, and T. Leen (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1994 Conference, pp. 369–376. MIT Press, Cambridge, MA.

Boyan, J. A., Moore, A. W., Sutton, R. S. (eds.). (1995). Proceedings of the Workshop on Value Function Approximation. Machine Learning Conference 1995. Technical Report CMU-CS-95-206. School of Computer Science, Carnegie Mellon University, Pittsburgh, PA.

Bradtke, S. J. (1993). Reinforcement learning applied to linear quadratic regulation. In S. J. Hanson, J. D. Cowan, and C. L. Giles (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1992 Conference, pp. 295–302. Morgan Kaufmann, San Mateo, CA.

Bradtke, S. J. (1994). Incremental Dynamic Programming for On-Line Adaptive Optimal Control. Ph.D. thesis, University of Massachusetts, Amherst. Appeared as CMPSCI Technical Report 94-62.

Bradtke, S. J., Barto, A. G. (1996). Linear least-squares algorithms for temporal difference learning. Machine Learning, 22:33–57.

Bradtke, S. J., Ydstie, B. E., Barto, A. G. (1994). Adaptive linear quadratic control using policy iteration. In Proceedings of the American Control Conference, pp. 3475–3479. American Automatic Control Council, Evanston, IL.

Bradtke, S. J., Duff, M. O. (1995). Reinforcement learning methods for continuous-time Markov decision problems. In G. Tesauro, D. Touretzky, and T. Leen (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1994 Conference, pp. 393–400. MIT Press, Cambridge, MA.

Bridle, J. S. (1990). Training stochastic model recognition algorithms as networks can lead to maximum mutual information estimates of parameters. In D. S. Touretzky (ed.), Advances in Neural Information Processing Systems: Proceedings of the 1989 Conference, pp. 211–217. Morgan Kaufmann, San Mateo, CA.

---

Broomhead, D. S., Lowe, D. (1988). Multivariable functional interpolation and adaptive networks. Complex Systems, 2:321–355.

Bryson, A. E., Jr. (1996). Optimal control—1950 to 1985. IEEE Control Systems, 13(3):26–33.

Bush, R. R., Mosteller, F. (1955). Stochastic Models for Learning. Wiley, New York.

Byrne, J. H., Gingrich, K. J., Baxter, D. A. (1990). Computational capabilities of single neurons: Relationship to simple forms of associative and nonassociative learning in aplysia. In R. D. Hawkins and G. H. Bower (eds.), Computational Models of Learning, pp. 31–63. Academic Press, New York.

Camerer, C. (2003). Behavioral game theory: Experiments in strategic interaction. Princeton University Press.

Campbell, D. T. (1960). Blind variation and selective survival as a general strategy in knowledge-processes. In M. C. Yovits and S. Cameron (eds.), Self-Organizing Systems, pp. 205–231. Pergamon, New York.

Carlström, J., Nordström, E. (1997). Control of self-similar ATM call traffic by reinforcement learning. In Proceedings of the International Workshop on Applications of Neural Networks to Telecommunications 3, pp. 54–62. Erlbaum, Hillsdale, NJ.

Chapman, D., Kaelbling, L. P. (1991). Input generalization in delayed reinforcement learning: An algorithm and performance comparisons. In Proceedings of the Twelfth International Conference on Artificial Intelligence, pp. 726–731. Morgan Kaufmann, San Mateo, CA.

Chow, C.-S., Tsitsiklis, J. N. (1991). An optimal one-way multigrid algorithm for discrete-time stochastic control. IEEE Transactions on Automatic Control, 36:898–914.

Chrisman, L. (1992). Reinforcement learning with perceptual aliasing: The perceptual distinctions approach. In Proceedings of the Tenth National Conference on Artificial Intelligence, pp. 183–188. AAAI/MIT Press, Menlo Park, CA.

Christensen, J., Korf, R. E. (1986). A unified theory of heuristic evaluation functions and its application to learning. In Proceedings of the Fifth National Conference on Artificial Intelligence, pp. 148–152. Morgan Kaufmann, San Mateo, CA.

Cichosz, P. (1995). Truncating temporal differences: On the efficient implementation of TD( $\lambda$) for reinforcement learning. Journal of Artificial

---

Intelligence Research, 2:287–318.

Clark, W. A., Farley, B. G. (1955). Generalization of pattern recognition in a self-organizing system. In Proceedings of the 1955 Western Joint Computer Conference, pp. 86–91.

Clouse, J. (1996). On Integrating Apprentice Learning and Reinforcement Learning TITLE2. Ph.D. thesis, University of Massachusetts, Amherst. Appeared as CMPSCI Technical Report 96-026.

Clouse, J., Utgoff, P. (1992). A teaching method for reinforcement learning systems. In Proceedings of the Ninth International Machine Learning Conference, pp. 92–101. Morgan Kaufmann, San Mateo, CA.

Colombetti, M., Dorigo, M. (1994). Training agent to perform sequential behavior. Adaptive Behavior, 2(3):247–275.

Connell, J. (1989). A colony architecture for an artificial creature. Technical Report AI-TR-1151. MIT Artificial Intelligence Laboratory, Cambridge, MA.

Connell, J., Mahadevan, S. (1993). Robot Learning. Kluwer Academic, Boston.

Craik, K. J. W. (1943). The Nature of Explanation. Cambridge University Press, Cambridge.

Crites, R. H. (1996). Large-Scale Dynamic Optimization Using Teams of Reinforcement Learning Agents. Ph.D. thesis, University of Massachusetts, Amherst.

Crites, R. H., Barto, A. G. (1996). Improving elevator performance using reinforcement learning. In D. S. Touretzky, M. C. Mozer, and M. E. Hasselmo (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1995 Conference, pp. 1017–1023. MIT Press, Cambridge, MA.

Cross, J. G. (1973). A stochastic learning model of economic behavior. The Quarterly Journal of Economics 87(2):239-266.

Curtiss, J. H. (1954). A theoretical comparison of the efficiencies of two classical methods and a Monte Carlo method for computing one component of the solution of a set of linear algebraic equations. In H. A. Meyer (ed.), Symposium on Monte Carlo Methods, pp. 191–233. Wiley, New York.

Cziko, G. (1995). Without Miracles: Universal Selection Theory and the Second Darwinian Revolution. MIT Press, Cambridge, MA.

Daniel, J. W. (1976). Splines and efficiency in dynamic programming. Journal of Mathematical Analysis and Applications, 54:402–407.

---

Dayan, P. (1991). Reinforcement comparison. In D. S. Touretzky, J. L. Elman, T. J. Sejnowski, and G. E. Hinton (eds.), Connectionist Models: Proceedings of the 1990 Summer School, pp. 45–51. Morgan Kaufmann, San Mateo, CA.

Dayan, P. (1992). The convergence of TD( $\lambda$) for general  $\lambda$. Machine Learning, 8:341–362.

Dayan, P., Hinton, G. E. (1993). Feudal reinforcement learning. In S. J. Hanson, J. D. Cohen, and C. L. Giles (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1992 Conference, pp. 271–278. Morgan Kaufmann, San Mateo, CA.

Dayan, P., Sejnowski, T. (1994). TD( $\lambda$) converges with probability 1. Machine Learning, 14:295–301.

Dean, T., Lin, S.-H. (1995). Decomposition techniques for planning in stochastic domains. In Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence, pp. 1121–1127. Morgan Kaufmann. See also Technical Report CS-95-10, Brown University, Department of Computer Science, 1995.

DeJong, G., Spong, M. W. (1994). Swinging up the acrobot: An example of intelligent control. In Proceedings of the American Control Conference, pp. 2158–2162. American Automatic Control Council, Evanston, IL.

Denardo, E. V. (1967). Contraction mappings in the theory underlying dynamic programming. SIAM Review, 9:165–177.

Dennett, D. C. (1978). Brainstorms, pp. 71–89. Bradford/MIT Press, Cambridge, MA.

Dick, T. (2015). A Regret-full Perspective on Policy Gradient Methods for Reinforcement Learning. MSc Thesis, University of Alberta.

Dietterich, T. G., Flann, N. S. (1995). Explanation-based learning and reinforcement learning: A unified view. In A. Prieditis and S. Russell (eds.), Proceedings of the Twelfth International Conference on Machine Learning, pp. 176–184. Morgan Kaufmann, San Francisco.

Doya, K. (1996). Temporal difference learning in continuous time and space. In D. S. Touretzky, M. C. Mozer, and M. E. Hasselmo (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1995 Conference, pp. 1073–1079. MIT Press, Cambridge, MA.

Doyle, P. G., Snell, J. L. (1984). Random Walks and Electric Networks. The Mathematical Association of America. Carus Mathematical Monograph 22.

---

Dreyfus, S. E., Law, A. M. (1977). The Art and Theory of Dynamic Programming. Academic Press, New York.

Duda, R. O., Hart, P. E. (1973). Pattern Classification and Scene Analysis. Wiley, New York.

Duff, M. O. (1995). Q-learning for bandit problems. In A. Prieditis and S. Russell (eds.), Proceedings of the Twelfth International Conference on Machine Learning, pp. 209–217. Morgan Kaufmann, San Francisco.

Estes, W. K. (1950). Toward a statistical theory of learning. Psychological Review, 57:94–107.

Farley, B. G., Clark, W. A. (1954). Simulation of self-organizing systems by digital computer. IRE Transactions on Information Theory, 4:76–84.

Feldbaum, A. A. (1965). Optimal Control Systems. Academic Press, New York.

Fogel, L. J., Owens, A. J., Walsh, M. J. (1966). Artificial intelligence through simulated evolution. John Wiley and Sons.

Friston, K. J., Tononi, G., Reeke, G. N., Sporns, O., Edelman, G. M. (1994). Value-dependent selection in the brain: Simulation in a synthetic neural model. Neuroscience, 59:229–243.

Fu, K. S. (1970). Learning control systems—Review and outlook. IEEE Transactions on Automatic Control, 15:210–221.

Galanter, E., Gerstenhaber, M. (1956). On thought: The extrinsic theory. Psychological Review, 63:218–227.

Gallant, S. I. (1993). Neural Network Learning and Expert Systems. MIT Press, Cambridge, MA.

Gallistel, C. R. (2005). Deconstructing the law of effect. Games and Economic Behavior 52(2), 410-423.

Gällmo, O., Asplund, L. (1995). Reinforcement learning by construction of hypothetical targets. In J. Alspector, R. Goodman, and T. X. Brown (eds.), Proceedings of the International Workshop on Applications of Neural Networks to Telecommunications 2, pp. 300–307. Erlbaum, Hillsdale, NJ.

Gardner, M. (1973). Mathematical games. Scientific American, 228(1):108–115.

Gelperin, A., Hopfield, J. J., Tank, D. W. (1985). The logic of limax learning. In A. Selverston (ed.), Model Neural Networks and Behavior, pp. 247–261. Plenum Press, New York.

Gittins, J. C., Jones, D. M. (1974). A dynamic allocation index for the

---

sequential design of experiments. In J. Gani, K. Sarkadi, and I. Vincze (eds.), Progress in Statistics, pp. 241–266. North-Holland, Amsterdam–London.

Goldberg, D. E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning. Addison-Wesley, Reading, MA.

Goldstein, H. (1957). Classical Mechanics. Addison-Wesley, Reading, MA.

Goodwin, G. C., Sin, K. S. (1984). Adaptive Filtering Prediction and Control. Prentice-Hall, Englewood Cliffs, NJ.

Gordon, G. J. (1995). Stable function approximation in dynamic programming. In A. Prieditis and S. Russell (eds.), Proceedings of the Twelfth International Conference on Machine Learning, pp. 261–268. Morgan Kaufmann, San Francisco. An expanded version was published as Technical Report CMU-CS-95-103. Carnegie Mellon University, Pittsburgh, PA, 1995.

Gordon, G. J. (1996). Chattering in SARSA( $\lambda$). CMU learning lab internal report.

Gordon, G. J. (1996). Stable fitted reinforcement learning. In D. S. Touretzky, M. C. Mozer, M. E. Hasselmo (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1995 Conference, pp. 1052–1058. MIT Press, Cambridge, MA.

Gordon, G. J. (2001). Reinforcement learning with function approximation converges to a region. Advances in neural information processing systems.

Greensmith, E., Bartlett, P. L., Baxter, J. (2001). Variance reduction techniques for gradient estimates in reinforcement learning. In Advances in Neural Information Processing Systems: Proceedings of the 2000 Conference, pp. 1507–1514.

Greensmith, E., Bartlett, P. L., Baxter, J. (2004). Variance reduction techniques for gradient estimates in reinforcement learning. Journal of Machine Learning Research 5, 1471-1530.

Griffith, A. K. (1966). A new machine learning technique applied to the game of checkers. Technical Report Project MAC, Artificial Intelligence Memo 94. Massachusetts Institute of Technology, Cambridge, MA.

Griffith, A. K. (1974). A comparison and evaluation of three machine learning procedures as applied to the game of checkers. Artificial Intelligence, 5:137–148.

Gullapalli, V. (1990). A stochastic reinforcement algorithm for learning real-valued functions. Neural Networks, 3:671–692.

Gurvits, L., Lin, L.-J., Hanson, S. J. (1994). Incremental learning of evalua-

---

tion functions for absorbing Markov chains: New methods and theorems. Preprint.

Hampson, S. E. (1983). A Neural Model of Adaptive Behavior. Ph.D. thesis, University of California, Irvine.

Hampson, S. E. (1989). Connectionist Problem Solving: Computational Aspects of Biological Learning. Birkhauser, Boston.

Hawkins, R. D., Kandel, E. R. (1984). Is there a cell-biological alphabet for simple forms of learning? Psychological Review, 91:375–391.

Herrnstein, R. J. (1970). On the Law of Effect. Journal of the Experimental Analysis of Behavior 13(2), 243-266.

Hersh, R., Griego, R. J. (1969). Brownian motion and potential theory. Scientific American, 220:66–74.

Hesterberg, T. C. (1988), Advances in importance sampling, Ph.D. Dissertation, Statistics Department, Stanford University.

Hilgard, E. R., Bower, G. H. (1975). Theories of Learning. Prentice-Hall, Englewood Cliffs, NJ.

Hinton, G. E. (1984). Distributed representations. Technical Report CMU-CS-84-157. Department of Computer Science, Carnegie-Mellon University, Pittsburgh, PA.

Hochreiter, S., Schmidhuber, J. (1997). LTSM can solve hard time lag problems. In Advances in Neural Information Processing Systems: Proceedings of the 1996 Conference, pp. 473–479. MIT Press, Cambridge, MA.

Holland, J. H. (1975). Adaptation in Natural and Artificial Systems. University of Michigan Press, Ann Arbor.

Holland, J. H. (1976). Adaptation. In R. Rosen and F. M. Snell (eds.), Progress in Theoretical Biology, vol. 4, pp. 263–293. Academic Press, New York.

Holland, J. H. (1986). Escaping brittleness: The possibility of general-purpose learning algorithms applied to rule-based systems. In R. S. Michalski, J. G. Carbonell, and T. M. Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach, vol. 2, pp. 593–623. Morgan Kaufmann, San Mateo, CA.

Houk, J. C., Adams, J. L., Barto, A. G. (1995). A model of how the basal ganglia generates and uses neural signals that predict reinforcement. In J. C. Houk, J. L. Davis, and D. G. Beiser (eds.), Models of Information Processing in the Basal Ganglia, pp. 249–270. MIT Press, Cambridge, MA.

---

Howard, R. (1960). Dynamic Programming and Markov Processes. MIT Press, Cambridge, MA.

Hull, C. L. (1943). Principles of Behavior. Appleton-Century, New York.

Hull, C. L. (1952). A Behavior System. Wiley, New York.

Jaakkola, T., Jordan, M. I., Singh, S. P. (1994). On the convergence of stochastic iterative dynamic programming algorithms. Neural Computation, 6:1185–1201.

Jaakkola, T., Singh, S. P., Jordan, M. I. (1995). Reinforcement learning algorithm for partially observable Markov decision problems. In G. Tesauro, D. S. Touretzky, T. Leen (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1994 Conference, pp. 345–352. MIT Press, Cambridge, MA.

Kaelbling, L. P. (1993a). Hierarchical learning in stochastic domains: Preliminary results. In Proceedings of the Tenth International Conference on Machine Learning, pp. 167–173. Morgan Kaufmann, San Mateo, CA.

Kaelbling, L. P. (1993b). Learning in Embedded Systems. MIT Press, Cambridge, MA.

Kaelbling, L. P. (ed.). (1996). Special issue of Machine Learning on reinforcement learning, 22.

Kaelbling, L. P., Littman, M. L., Moore, A. W. (1996). Reinforcement learning: A survey. Journal of Artificial Intelligence Research, 4:237–285.

Kakutani, S. (1945). Markov processes and the Dirichlet problem. Proceedings of the Japan Academy, 21:227–233.

Kalos, M. H., Whitlock, P. A. (1986). Monte Carlo Methods. Wiley, New York.

Kanerva, P. (1988). Sparse Distributed Memory. MIT Press, Cambridge, MA.

Kanerva, P. (1993). Sparse distributed memory and related models. In M. H. Hassoun (ed.), Associative Neural Memories: Theory and Implementation, pp. 50–76. Oxford University Press, New York.

Kashyap, R. L., Blaydon, C. C., Fu, K. S. (1970). Stochastic approximation. In J. M. Mendel and K. S. Fu (eds.), Adaptive, Learning, and Pattern Recognition Systems: Theory and Applications, pp. 329–355. Academic Press, New York.

Keerthi, S. S., Ravindran, B. (1997). Reinforcement learning. In E. Fiesler and R. Beale (eds.), Handbook of Neural Computation, C3. Oxford University Press, New York.

---

Kimble, G. A. (1961). Hilgard and Marquis' Conditioning and Learning. Appleton-Century-Crofts, New York.

Kimble, G. A. (1967). Foundations of Conditioning and Learning. Appleton-Century-Crofts, New York.

Klopf, A. H. (1972). Brain function and adaptive systems—A heterostatic theory. Technical Report AFCRL-72-0164, Air Force Cambridge Research Laboratories, Bedford, MA. A summary appears in Proceedings of the International Conference on Systems, Man, and Cybernetics. IEEE Systems, Man, and Cybernetics Society, Dallas, TX, 1974.

Klopf, A. H. (1975). A comparison of natural and artificial intelligence. SIGART Newsletter, 53:11–13.

Klopf, A. H. (1982). The Hedonistic Neuron: A Theory of Memory, Learning, and Intelligence. Hemisphere, Washington, DC.

Klopf, A. H. (1988). A neuronal model of classical conditioning. Psychobiology, 16:85–125.

Kohonen, T. (1977). Associative Memory: A System Theoretic Approach. Springer-Verlag, Berlin.

Koller, D., Friedman, N. (2009). Probabilistic Graphical Models: Principles and Techniques. MIT Press, 2009.

Korf, R. E. (1988). Optimal path finding algorithms. In L. N. Kanal and V. Kumar (eds.), Search in Artificial Intelligence, pp. 223–267. Springer Verlag, Berlin.

Koza, J. R. (1992). Genetic programming: On the programming of computers by means of natural selection (Vol. 1). MIT press.

Kraft, L. G., Campagna, D. P. (1990). A summary comparison of CMAC neural network and traditional adaptive control systems. In T. Miller, R. S. Sutton, and P. J. Werbos (eds.), Neural Networks for Control, pp. 143–169. MIT Press, Cambridge, MA.

Kraft, L. G., Miller, W. T., Dietz, D. (1992). Development and application of CMAC neural network-based control. In D. A. White and D. A. Sofge (eds.), Handbook of Intelligent Control: Neural, Fuzzy, and Adaptive Approaches, pp. 215–232. Van Nostrand Reinhold, New York.

Kumar, P. R., Varaiya, P. (1986). Stochastic Systems: Estimation, Identification, and Adaptive Control. Prentice-Hall, Englewood Cliffs, NJ.

Kumar, P. R. (1985). A survey of some results in stochastic adaptive control. SIAM Journal of Control and Optimization, 23:329–380.

---

Kumar, V., Kanal, L. N. (1988). The CDP: A unifying formulation for heuristic search, dynamic programming, and branch-and-bound. In L. N. Kanal and V. Kumar (eds.), Search in Artificial Intelligence, pp. 1–37. Springer-Verlag, Berlin.

Kushner, H. J., Dupuis, P. (1992). Numerical Methods for Stochastic Control Problems in Continuous Time. Springer-Verlag, New York.

Lai, T. L., Robbins, H. (1985). Asymptotically efficient adaptive allocation rules. Advances in applied mathematics, 6(1):4–22.

Lang, K. J., Waibel, A. H., Hinton, G. E. (1990). A time-delay neural network architecture for isolated word recognition. Neural Networks, 3:33–43.

Lin, C.-S., Kim, H. (1991). CMAC-based adaptive critic self-learning control. IEEE Transactions on Neural Networks, 2:530–533.

Lin, L.-J. (1992). Self-improving reactive agents based on reinforcement learning, planning and teaching. Machine Learning, 8:293–321.

Lin, L.-J., Mitchell, T. (1992). Reinforcement learning with hidden states. In Proceedings of the Second International Conference on Simulation of Adaptive Behavior: From Animals to Animals, pp. 271–280. MIT Press, Cambridge, MA.

Littman, M. L. (1994). Markov games as a framework for multi-agent reinforcement learning. In Proceedings of the Eleventh International Conference on Machine Learning, pp. 157–163. Morgan Kaufmann, San Francisco.

Littman, M. L., Cassandra, A. R., Kaelbling, L. P. (1995). Learning policies for partially observable environments: Scaling up. In A. Prieditis and S. Russell (eds.), Proceedings of the Twelfth International Conference on Machine Learning, pp. 362–370. Morgan Kaufmann, San Francisco.

Littman, M. L., Dean, T. L., Kaelbling, L. P. (1995). On the complexity of solving Markov decision problems. In Proceedings of the Eleventh Annual Conference on Uncertainty in Artificial Intelligence, pp. 394–402.

Liu, J. S. (2001). Monte Carlo strategies in scientific computing. Berlin, Springer-Verlag.

Ljung, L., Söderstrom, T. (1983). Theory and Practice of Recursive Identification. MIT Press, Cambridge, MA.

Lovejoy, W. S. (1991). A survey of algorithmic methods for partially observed Markov decision processes. Annals of Operations Research, 28:47–66.

Luce, D. (1959). Individual Choice Behavior. Wiley, New York.

---

Maclin, R., Shavlik, J. W. (1994). Incorporating advice into agents that learn from reinforcements. In Proceedings of the Twelfth National Conference on Artificial Intelligence, pp. 694–699. AAAI Press, Menlo Park, CA.

Mahadevan, S. (1996). Average reward reinforcement learning: Foundations, algorithms, and empirical results. Machine Learning, 22:159–196.

Markey, K. L. (1994). Efficient learning of multiple degree-of-freedom control problems with quasi-independent Q-agents. In M. C. Mozer, P. Smolensky, D. S. Touretzky, J. L. Elman, and A. S. Weigend (eds.), Proceedings of the 1990 Connectionist Models Summer School. Erlbaum, Hillsdale, NJ.

Mazur, J. E. (1994). Learning and Behavior, 3rd ed. Prentice-Hall, Englewood Cliffs, NJ.

McCallum, A. K. (1993). Overcoming incomplete perception with utile distinction memory. In Proceedings of the Tenth International Conference on Machine Learning, pp. 190–196. Morgan Kaufmann, San Mateo, CA.

McCallum, A. K. (1995). Reinforcement Learning with Selective Perception and Hidden State. Ph.D. thesis, University of Rochester, Rochester, NY.

Mendel, J. M. (1966). A survey of learning control systems. ISA Transactions, 5:297–303.

Mendel, J. M., McLaren, R. W. (1970). Reinforcement learning control and pattern recognition systems. In J. M. Mendel and K. S. Fu (eds.), Adaptive, Learning and Pattern Recognition Systems: Theory and Applications, pp. 287–318. Academic Press, New York.

Michie, D. (1961). Trial and error. In S. A. Barnett and A. McLaren (eds.), Science Survey, Part 2, pp. 129–145. Penguin, Harmondsworth.

Michie, D. (1963). Experiments on the mechanisation of game learning. 1. characterization of the model and its parameters. Computer Journal, 1:232–263.

Michie, D. (1974). On Machine Intelligence. Edinburgh University Press, Edinburgh.

Michie, D., Chambers, R. A. (1968). BOXES: An experiment in adaptive control. In E. Dale and D. Michie (eds.), Machine Intelligence 2, pp. 137–152. Oliver and Boyd, Edinburgh.

Miller, S., Williams, R. J. (1992). Learning to control a bioreactor using a neural net Dyna-Q system. In Proceedings of the Seventh Yale Workshop on Adaptive and Learning Systems, pp. 167–172. Center for Systems Science, Dunham Laboratory, Yale University, New Haven.

Miller, W. T., Scalera, S. M., Kim, A. (1994). Neural network control of

---

dynamic balance for a biped walking robot. In Proceedings of the Eighth Yale Workshop on Adaptive and Learning Systems, pp. 156–161. Center for Systems Science, Dunham Laboratory, Yale University, New Haven.

Minsky, M. L. (1954). Theory of Neural-Analog Reinforcement Systems and Its Application to the Brain-Model Problem. Ph.D. thesis, Princeton University.

Minsky, M. L. (1961). Steps toward artificial intelligence. Proceedings of the Institute of Radio Engineers, 49:8–30. Reprinted in E. A. Feigenbaum and J. Feldman (eds.), Computers and Thought, pp. 406–450. McGraw-Hill, New York, 1963.

Minsky, M. L. (1967). Computation: Finite and Infinite Machines. Prentice-Hall, Englewood Cliffs, NJ.

Montague, P. R., Dayan, P., Sejnowski, T. J. (1996). A framework for mesencephalic dopamine systems based on predictive Hebbian learning. Journal of Neuroscience, 16:1936–1947.

Moore, A. W. (1990). Efficient Memory-Based Learning for Robot Control. Ph.D. thesis, University of Cambridge.

Moore, A. W. (1994). The parti-game algorithm for variable resolution reinforcement learning in multidimensional spaces. In J. D. Cohen, G. Tesauro and J. Alspector (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1993 Conference, pp. 711–718. Morgan Kaufmann, San Francisco.

Moore, A. W., Atkeson, C. G. (1993). Prioritized sweeping: Reinforcement learning with less data and less real time. Machine Learning, 13:103–130.

Moore, J. W., Desmond, J. E., Berthier, N. E., Blazis, E. J., Sutton, R. S., and Barto, A. G. (1986). Simulation of the classically conditioned nictitating membrane response by a neuron-like adaptive element: I. Response topography, neuronal firing, and interstimulus intervals. Behavioural Brain Research, 21:143–154.

Narendra, K. S., Thathachar, M. A. L. (1974). Learning automata—A survey. IEEE Transactions on Systems, Man, and Cybernetics, 4:323–334.

Narendra, K. S., Thathachar, M. A. L. (1989). Learning Automata: An Introduction. Prentice-Hall, Englewood Cliffs, NJ.

Narendra, K. S., Wheeler, R. M. (1986). Decentralized learning in finite Markov chains. IEEE Transactions on Automatic Control, AC31(6):519–526.

Nie, J., Haykin, S. (1996). A dynamic channel assignment policy through

---

Q-learning. CRL Report 334. Communications Research Laboratory, McMaster University, Hamilton, Ontario.

Nowé, A., Vrancx, P., De Hauwere, Y. M. (2012). Game theory and multi-agent reinforcement learning. In Reinforcement Learning (pp. 441-470). Springer Berlin Heidelberg.

Page, C. V. (1977). Heuristics for signature table analysis as a pattern recognition technique. IEEE Transactions on Systems, Man, and Cybernetics, 7:77–86.

Parr, R., Russell, S. (1995). Approximating optimal policies for partially observable stochastic domains. In Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence, pp. 1088–1094. Morgan Kaufmann.

Pavlov, P. I. (1927). Conditioned Reflexes. Oxford University Press, London.

Pearl, J. (1984). Heuristics: Intelligent Search Strategies for Computer Problem Solving. Addison-Wesley, Reading, MA.

Pearl, J. (1995). Causal diagrams for empirical research. Biometrika, 82(4), 669-688.

Balke, A., Pearl, J. (1994). Counterfactual probabilities: Computational methods, bounds and applications. In Proceedings of the Tenth International Conference on Uncertainty in Artificial Intelligence (pp. 46-54). Morgan Kaufmann.

Peng, J. (1993). Efficient Dynamic Programming-Based Learning for Control. Ph.D. thesis, Northeastern University, Boston.

Peng, J., Williams, R. J. (1993). Efficient learning and planning within the Dyna framework. Adaptive Behavior, 1(4):437–454.

Peng, J., Williams, R. J. (1994). Incremental multi-step Q-learning. In W. W. Cohen and H. Hirsh (eds.), Proceedings of the Eleventh International Conference on Machine Learning, pp. 226–232. Morgan Kaufmann, San Francisco.

Peng, J., Williams, R. J. (1996). Incremental multi-step Q-learning. Machine Learning, 22:283–290.

Phansalkar, V. V., Thathachar, M. A. L. (1995). Local and global optimization algorithms for generalized learning automata. Neural Computation, 7:950–973.

Poggio, T., Girosi, F. (1989). A theory of networks for approximation and learning. A.I. Memo 1140. Artificial Intelligence Laboratory, Massachusetts Institute of Technology, Cambridge, MA.

---

Poggio, T., Girosi, F. (1990). Regularization algorithms for learning that are equivalent to multilayer networks. Science, 247:978–982.

Powell, M. J. D. (1987). Radial basis functions for multivariate interpolation: A review. In J. C. Mason and M. G. Cox (eds.), Algorithms for Approximation, pp. 143–167. Clarendon Press, Oxford.

Powell, W. B. (2011). Approximate Dynamic Programming: Solving the Curses of Dimensionality, Second edition. John Wiley and Sons.

Precup, D., Sutton, R. S., Dasgupta, S. (2001). Off-policy temporal-difference learning with function approximation. In Proceedings of the 18th International Conference on Machine Learning.

Precup, D., Sutton, R. S., Singh, S. (2000). Eligibility traces for off-policy policy evaluation. In Proceedings of the 17th International Conference on Machine Learning, pp. 759–766. Morgan Kaufmann.

Puterman, M. L. (1994). Markov Decision Problems. Wiley, New York.

Puterman, M. L., Shin, M. C. (1978). Modified policy iteration algorithms for discounted Markov decision problems. Management Science, 24:1127–1137.

Reetz, D. (1977). Approximate solutions of a discounted Markovian decision process. Bonner Mathematische Schriften, 98:77–92.

Ring, M. B. (1994). Continual Learning in Reinforcement Environments. Ph.D. thesis, University of Texas, Austin.

Rivest, R. L., Schapire, R. E. (1987). Diversity-based inference of finite automata. In Proceedings of the Twenty-Eighth Annual Symposium on Foundations of Computer Science, pp. 78–87. Computer Society Press of the IEEE, Washington, DC.

Robbins, H. (1952). Some aspects of the sequential design of experiments. Bulletin of the American Mathematical Society, 58:527–535.

Robertie, B. (1992). Carbon versus silicon: Matching wits with TD-Gammon. Inside Backgammon, 2:14–22.

Rosenblatt, F. (1962). Principles of Neurodynamics: Perceptrons and the Theory of Brain Mechanisms. Spartan Books, Washington, DC.

Ross, S. (1983). Introduction to Stochastic Dynamic Programming. Academic Press, New York.

Rubinstein, R. Y. (1981). Simulation and the Monte Carlo Method. Wiley, New York.

Rumelhart, D. E., Hinton, G. E., Williams, R. J. (1986). Learning internal

---

representations by error propagation. In D. E. Rumelhart and J. L. McClelland (eds.), Parallel Distributed Processing: Explorations in the Microstructure of Cognition, vol. I, Foundations. Bradford/MIT Press, Cambridge, MA.

Rummery, G. A. (1995). Problem Solving with Reinforcement Learning. Ph.D. thesis, Cambridge University.

Rummery, G. A., Niranjan, M. (1994). On-line Q-learning using connectionist systems. Technical Report CUED/F-INFENG/TR 166. Engineering Department, Cambridge University.

Russell, S., Norvig, P. (2009). Artificial Intelligence: A Modern Approach. Prentice-Hall, Englewood Cliffs, NJ.

Rust, J. (1996). Numerical dynamic programming in economics. In H. Amman, D. Kendrick, and J. Rust (eds.), Handbook of Computational Economics, pp. 614–722. Elsevier, Amsterdam.

Samuel, A. L. (1959). Some studies in machine learning using the game of checkers. IBM Journal on Research and Development, 3:211–229. Reprinted in E. A. Feigenbaum and J. Feldman (eds.), Computers and Thought, pp. 71–105. McGraw-Hill, New York, 1963.

Samuel, A. L. (1967). Some studies in machine learning using the game of checkers. II—Recent progress. IBM Journal on Research and Development, 11:601–617.

Schultz, D. G., Melsa, J. L. (1967). State Functions and Linear Control Systems. McGraw-Hill, New York.

Schultz, W., Dayan, P., Montague, P. R. (1997). A neural substrate of prediction and reward. Science, 275:1593–1598.

Schwartz, A. (1993). A reinforcement learning method for maximizing undiscounted rewards. In Proceedings of the Tenth International Conference on Machine Learning, pp. 298–305. Morgan Kaufmann, San Mateo, CA.

Schweitzer, P. J., Seidmann, A. (1985). Generalized polynomial approximations in Markovian decision processes. Journal of Mathematical Analysis and Applications, 110:568–582.

Selfridge, O. J., Sutton, R. S., Barto, A. G. (1985). Training and tracking in robotics. In A. Joshi (ed.), Proceedings of the Ninth International Joint Conference on Artificial Intelligence, pp. 670–672. Morgan Kaufmann, San Mateo, CA.

Shannon, C. E. (1950). Programming a computer for playing chess. Philosophical Magazine, 41:256–275.

---

Shelton, C. R. (2001). Importance Sampling for Reinforcement Learning with Multiple Objectives. PhD thesis, Massachusetts Institute of Technology.

Shewchuk, J., Dean, T. (1990). Towards learning time-varying functions with high input dimensionality. In Proceedings of the Fifth IEEE International Symposium on Intelligent Control, pp. 383–388. IEEE Computer Society Press, Los Alamitos, CA.

Si, J., Barto, A., Powell, W., Wunsch, D. (Eds.). (2004). Handbook of learning and approximate dynamic programming. John Wiley and Sons.

Singh, S. P. (1992a). Reinforcement learning with a hierarchy of abstract models. In Proceedings of the Tenth National Conference on Artificial Intelligence, pp. 202–207. AAAI/MIT Press, Menlo Park, CA.

Singh, S. P. (1992b). Scaling reinforcement learning algorithms by learning variable temporal resolution models. In Proceedings of the Ninth International Machine Learning Conference, pp. 406–415. Morgan Kaufmann, San Mateo, CA.

Singh, S. P. (1993). Learning to Solve Markovian Decision Processes. Ph.D. thesis, University of Massachusetts, Amherst. Appeared as CMPSCI Technical Report 93-77.

Singh, S. P., Bertsekas, D. (1997). Reinforcement learning for dynamic channel allocation in cellular telephone systems. In Advances in Neural Information Processing Systems: Proceedings of the 1996 Conference, pp. 974–980. MIT Press, Cambridge, MA.

Singh, S. P., Jaakkola, T., Jordan, M. I. (1994). Learning without state-estimation in partially observable Markovian decision problems. In W. W. Cohen and H. Hirsch (eds.), Proceedings of the Eleventh International Conference on Machine Learning, pp. 284–292. Morgan Kaufmann, San Francisco.

Singh, S. P., Jaakkola, T., Jordan, M. I. (1995). Reinforcement learing with soft state aggregation. In G. Tesauro, D. S. Touretzky, T. Leen (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1994 Conference, pp. 359–368. MIT Press, Cambridge, MA.

Singh, S. P., Sutton, R. S. (1996). Reinforcement learning with replacing eligibility traces. Machine Learning, 22:123–158.

Sivarajan, K. N., McEliece, R. J., Ketchum, J. W. (1990). Dynamic channel assignment in cellular radio. In Proceedings of the 40th Vehicular Technology Conference, pp. 631–637.

Skinner, B. F. (1938). The Behavior of Organisms: An Experimental Analysis.

---

Appleton-Century, New York.

Sofge, D. A., White, D. A. (1992). Applied learning: Optimal control for manufacturing. In D. A. White and D. A. Sofge (eds.), Handbook of Intelligent Control: Neural, Fuzzy, and Adaptive Approaches, pp. 259–281. Van Nostrand Reinhold, New York.

Spong, M. W. (1994). Swing up control of the acrobot. In Proceedings of the 1994 IEEE Conference on Robotics and Automation, pp. 2356-2361. IEEE Computer Society Press, Los Alamitos, CA.

Staddon, J. E. R. (1983). Adaptive Behavior and Learning. Cambridge University Press, Cambridge.

Sutton, R. S. (1978a). Learning theory support for a single channel theory of the brain. Unpublished report.

Sutton, R. S. (1978b). Single channel theory: A neuronal theory of learning. Brain Theory Newsletter, 4:72–75. Center for Systems Neuroscience, University of Massachusetts, Amherst, MA.

Sutton, R. S. (1978c). A unified theory of expectation in classical and instrumental conditioning. Bachelors thesis, Stanford University.

Sutton, R. S. (1984). Temporal Credit Assignment in Reinforcement Learning. Ph.D. thesis, University of Massachusetts, Amherst.

Sutton, R. S. (1988). Learning to predict by the method of temporal differences. Machine Learning, 3:9–44.

Sutton, R. S. (1990). Integrated architectures for learning, planning, and reacting based on approximating dynamic programming. In Proceedings of the Seventh International Conference on Machine Learning, pp. 216–224. Morgan Kaufmann, San Mateo, CA.

Sutton, R. S. (1991a). Dyna, an integrated architecture for learning, planning, and reacting. SIGART Bulletin, 2:160–163. ACM Press.

Sutton, R. S. (1991b). Planning by incremental dynamic programming. In L. A. Birnbaum and G. C. Collins (eds.), Proceedings of the Eighth International Workshop on Machine Learning, pp. 353–357. Morgan Kaufmann, San Mateo, CA.

Sutton, R. S. (1995). TD models: Modeling the world at a mixture of time scales. In A. Prieditis and S. Russell (eds.), Proceedings of the Twelfth International Conference on Machine Learning, pp. 531–539. Morgan Kaufmann, San Francisco.

Sutton, R. S. (1996). Generalization in reinforcement learning: Successful examples using sparse coarse coding. In D. S. Touretzky, M. C. Mozer

---

and M. E. Hasselmo (eds.), Advances in Neural Information Processing Systems: Proceedings of the 1995 Conference, pp. 1038–1044. MIT Press, Cambridge, MA.

Sutton, R. S. (ed.). (1992). Special issue of Machine Learning on reinforcement learning, 8. Also published as Reinforcement Learning. Kluwer Academic, Boston, 1992.

Sutton, R. S., Barto, A. G. (1981a). Toward a modern theory of adaptive networks: Expectation and prediction. Psychological Review, 88:135–170.

Sutton, R. S., Barto, A. G. (1981b). An adaptive network that constructs and uses an internal model of its world. Cognition and Brain Theory, 3:217–246.

Sutton, R. S., Barto, A. G. (1987). A temporal-difference model of classical conditioning. In Proceedings of the Ninth Annual Conference of the Cognitive Science Society, pp. 355-378. Erlbaum, Hillsdale, NJ.

Sutton, R. S., Barto, A. G. (1990). Time-derivative models of Pavlovian reinforcement. In M. Gabriel and J. Moore (eds.), Learning and Computational Neuroscience: Foundations of Adaptive Networks, pp. 497–537. MIT Press, Cambridge, MA.

Sutton, R. S., Mahmood, A. R., Precup, D., van Hasselt, H. (2014). A new Q( $\lambda$) with interim forward view and Monte Carlo equivalence. In Proceedings of the 31st International Conference on Machine Learning, Beijing, China.

Sutton, R. S., Pinette, B. (1985). The learning of world models by connectionist networks. In Proceedings of the Seventh Annual Conference of the Cognitive Science Society, pp. 54–64.

Sutton, R. S., Singh, S. (1994). On bias and step size in temporal-difference learning. In Proceedings of the Eighth Yale Workshop on Adaptive and Learning Systems, pp. 91–96. Center for Systems Science, Dunham Laboratory, Yale University, New Haven.

Sutton, R. S., Whitehead, D. S. (1993). Online learning with random representations. In Proceedings of the Tenth International Machine Learning Conference, pp. 314–321. Morgan Kaufmann, San Mateo, CA.

Szepesvri, C. (2010). Algorithms for reinforcement learning. Synthesis Lectures on Artificial Intelligence and Machine Learning 4(1), 1–103.

Szita, I. (2012). Reinforcement learning in games. In Reinforcement Learning (pp. 539-577). Springer Berlin Heidelberg.

Tadepalli, P., Ok, D. (1994). H-learning: A reinforcement learning method to

---

optimize undiscounted average reward. Technical Report 94-30-01. Oregon State University, Computer Science Department, Corvallis.

Tan, M. (1991). Learning a cost-sensitive internal representation for reinforcement learning. In L. A. Birnbaum and G. C. Collins (eds.), Proceedings of the Eighth International Workshop on Machine Learning, pp. 358–362. Morgan Kaufmann, San Mateo, CA.

Tan, M. (1993). Multi-agent reinforcement learning: Independent vs. cooperative agents. In Proceedings of the Tenth International Conference on Machine Learning, pp. 330–337. Morgan Kaufmann, San Mateo, CA.

Tesauro, G. J. (1986). Simple neural models of classical conditioning. Biological Cybernetics, 55:187–200.

Tesauro, G. J. (1992). Practical issues in temporal difference learning. Machine Learning, 8:257–277.

Tesauro, G. J. (1994). TD-Gammon, a self-teaching backgammon program, achieves master-level play. Neural Computation, 6(2):215–219.

Tesauro, G. J. (1995). Temporal difference learning and TD-Gammon. Communications of the ACM, 38:58–68.

Tesauro, G. J., Galperin, G. R. (1997). On-line policy improvement using Monte-Carlo search. In Advances in Neural Information Processing Systems: Proceedings of the 1996 Conference, pp. 1068–1074. MIT Press, Cambridge, MA.

Tham, C. K. (1994). Modular On-Line Function Approximation for Scaling up Reinforcement Learning. PhD thesis, Cambridge University.

Thathachar, M. A. L. and Sastry, P. S. (1985). A new approach to the design of reinforcement schemes for learning automata. IEEE Transactions on Systems, Man, and Cybernetics, 15:168–175.

Thompson, W. R. (1933). On the likelihood that one unknown probability exceeds another in view of the evidence of two samples. Biometrika, 25:285–294.

Thompson, W. R. (1934). On the theory of apportionment. American Journal of Mathematics, 57:450–457.

Thorndike, E. L. (1911). Animal Intelligence. Hafner, Darien, CT.

Thorp, E. O. (1966). Beat the Dealer: A Winning Strategy for the Game of Twenty-One. Random House, New York.

Tolman, E. C. (1932). Purposive Behavior in Animals and Men. Century, New York.

---

Tsetlin, M. L. (1973). Automaton Theory and Modeling of Biological Systems. Academic Press, New York.

Tsitsiklis, J. N. (1994). Asynchronous stochastic approximation and Q-learning. Machine Learning, 16:185–202.

Tsitsiklis, J. N. (2002). On the convergence of optimistic policy iteration. Journal of Machine Learning Research, 3:59–72.

Tsitsiklis, J. N. and Van Roy, B. (1996). Feature-based methods for large scale dynamic programming. Machine Learning, 22:59–94.

Tsitsiklis, J. N., Van Roy, B. (1997). An analysis of temporal-difference learning with function approximation. IEEE Transactions on Automatic Control, 42:674–690.

Tsitsiklis, J. N., Van Roy, B. (1999). Average cost temporal-difference learning. Automatica, 35:1799–1808. Also: Technical Report LIDS-P-2390. Laboratory for Information and Decision Systems, Massachusetts Institute of Technology, Cambridge, MA, 1997.

Turing, A. M. (1950). Computing machinery and intelligence. Mind 433–460.

Turing, A. M. (1948). Intelligent Machinery, A Heretical Theory. The Turing Test: Verbal Behavior as the Hallmark of Intelligence, 105.

Ungar, L. H. (1990). A bioreactor benchmark for adaptive network-based process control. In W. T. Miller, R. S. Sutton, and P. J. Werbos (eds.), Neural Networks for Control, pp. 387–402. MIT Press, Cambridge, MA.

Urbanowicz, R. J., Moore, J. H. (2009). Learning classifier systems: A complete introduction, review, and roadmap. Journal of Artificial Evolution and Applications.

Waltz, M. D., Fu, K. S. (1965). A heuristic approach to reinforcement learning control systems. IEEE Transactions on Automatic Control, 10:390–398.

Watkins, C. J. C. H. (1989). Learning from Delayed Rewards. Ph.D. thesis, Cambridge University.

Watkins, C. J. C. H., Dayan, P. (1992). Q-learning. Machine Learning, 8:279–292.

Wiering, M., Van Otterlo, M. (2012). Reinforcement Learning. Springer Berlin Heidelberg.

Werbos, P. J. (1977). Advanced forecasting methods for global crisis warning and models of intelligence. General Systems Yearbook, 22:25–38.

Werbos, P. J. (1982). Applications of advances in nonlinear sensitivity analysis. In R. F. Drenick and F. Kozin (eds.), System Modeling and Optimiza-

---

tion, pp. 762–770. Springer-Verlag, Berlin.

Werbos, P. J. (1987). Building and understanding adaptive systems: A statistical/numerical approach to factory automation and brain research. IEEE Transactions on Systems, Man, and Cybernetics, 17:7–20.

Werbos, P. J. (1988). Generalization of back propagation with applications to a recurrent gas market model. Neural Networks, 1:339–356.

Werbos, P. J. (1989). Neural networks for control and system identification. In Proceedings of the 28th Conference on Decision and Control, pp. 260–265. IEEE Control Systems Society.

Werbos, P. J. (1990). Consistency of HDP applied to a simple reinforcement learning problem. Neural Networks, 3:179–189.

Werbos, P. J. (1992). Approximate dynamic programming for real-time control and neural modeling. In D. A. White and D. A. Sofge (eds.), Handbook of Intelligent Control: Neural, Fuzzy, and Adaptive Approaches, pp. 493–525. Van Nostrand Reinhold, New York.

White, D. J. (1969). Dynamic Programming. Holden-Day, San Francisco.

White, D. J. (1985). Real applications of Markov decision processes. Interfaces, 15:73–83.

White, D. J. (1988). Further real applications of Markov decision processes. Interfaces, 18:55–61.

White, D. J. (1993). A survey of applications of Markov decision processes. Journal of the Operational Research Society, 44:1073–1096.

Whitehead, S. D., Ballard, D. H. (1991). Learning to perceive and act by trial and error. Machine Learning, 7:45–83.

Whitt, W. (1978). Approximations of dynamic programs I. Mathematics of Operations Research, 3:231–243.

Whittle, P. (1982). Optimization over Time, vol. 1. Wiley, New York.

Whittle, P. (1983). Optimization over Time, vol. 2. Wiley, New York.

Widrow, B., Gupta, N. K., Maitra, S. (1973). Punish/reward: Learning with a critic in adaptive threshold systems. IEEE Transactions on Systems, Man, and Cybernetics, 3:455–465.

Widrow, B., Hoff, M. E. (1960). Adaptive switching circuits. In 1960 WESCON Convention Record Part IV, pp. 96–104. Institute of Radio Engineers, New York. Reprinted in J. A. Anderson and E. Rosenfeld, Neurocomputing: Foundations of Research, pp. 126–134. MIT Press, Cambridge, MA, 1988.

---

Widrow, B., Smith, F. W. (1964). Pattern-recognizing control systems. In J. T. Tou and R. H. Wilcox (eds.), Computer and Information Sciences, pp. 288–317. Spartan, Washington, DC.

Widrow, B., Stearns, S. D. (1985). Adaptive Signal Processing. Prentice-Hall, Englewood Cliffs, NJ.

Williams, R. J. (1986). Reinforcement learning in connectionist networks: A mathematical analysis. Technical Report ICS 8605. Institute for Cognitive Science, University of California at San Diego, La Jolla.

Williams, R. J. (1987). Reinforcement-learning connectionist systems. Technical Report NU-CCS-87-3. College of Computer Science, Northeastern University, Boston.

Williams, R. J. (1988). On the use of backpropagation in associative reinforcement learning. In Proceedings of the IEEE International Conference on Neural Networks, pp. I263–I270. IEEE San Diego section and IEEE TAB Neural Network Committee.

Williams, R. J. (1992). Simple statistical gradient-following algorithms for connectionist reinforcement learning. Machine Learning, 8:229–256.

Williams, R. J., Baird, L. C. (1990). A mathematical analysis of actor-critic architectures for learning optimal controls through incremental dynamic programming. In Proceedings of the Sixth Yale Workshop on Adaptive and Learning Systems, pp. 96–101. Center for Systems Science, Dunham Laboratory, Yale University, New Haven.

Wilson, S. W. (1994). ZCS: A zeroth order classifier system. Evolutionary Computation, 2:1–18.

Witten, I. H. (1976). The apparent conflict between estimation and control—A survey of the two-armed problem. Journal of the Franklin Institute, 301:161–189.

Witten, I. H. (1977). An adaptive optimal controller for discrete-time Markov environments. Information and Control, 34:286–295.

Witten, I. H., Corbin, M. J. (1973). Human operators and automatic adaptive controllers: A comparative study on a particular control task. International Journal of Man-Machine Studies, 5:75–104.

Woodworth, R. S., Schlosberg, H. (1938). Experimental psychology. New York: Henry Holt and Company.

Yee, R. C., Saxena, S., Utgoff, P. E., Barto, A. G. (1990). Explaining temporal differences to create useful concepts for evaluating states. In Proceedings of the Eighth National Conference on Artificial Intelligence, pp. 882–888.