Code Agent We constructed large-scale, executable environments for software issue resolution by mining millions of issue-Pull Request (PR) pairs from GitHub. This dataset was rigorously filtered using heuristic rules and LLM-based judgments to ensure high quality, requiring that each entry contain a reasonable issue description, a correlated gold patch, and a test patch for validation. An automated environment-setup agent, powered by DeepSeek-V3.2, was employed to build executable environments for these pairs. This agent handles package installation, dependency resolution, and test execution. Test results are output in the standard JUnit format, ensuring consistent parsing across programming languages and test frameworks. An environment is deemed successfully built only when applying the gold patch results in a non-zero count of false-to-positive (F2P) test cases (indicating the issue is fixed) and a zero count of pass-to-fail (P2F) test cases (indicating no regressions). Using this pipeline, we successfully built tens of thousands of reproducible issue resolution environments spanning multiple programming languages, including Python, Java, JavaScript, TypeScript, C, C++, Go, and PHP.

Code Interpreter Agent We utilize Jupyter Notebook as a code interpreter to address complex reasoning tasks. To facilitate this, we curate a diverse set of problems spanning mathematics, logic, and data science, each requiring the model to leverage code execution capabilities to arrive at a solution.

General Agent To scale up agent environments and tasks in RL, we employ an automatic environment-synthesis agent that synthesizes 1,827 task-oriented environments. These tasks are hard to solve but easy to verify. The synthesis workflow primarily consists of environment and toolset construction, task synthesis, and solution generation. Specifically, the workflow proceeds as follows.

1. Given a task category (e.g., planning a travel itinerary) and a sandbox equipped with a bash and a search tool, the agent first uses these tools to generate or retrieve relevant data from the Internet and store them in the sandbox database.

2. The agent then synthesizes a set of task-specific tools, each implemented as a function.

3. To create tasks that are both challenging and automatically verifiable, the agent initially proposes a simple task based on the current database, along with its solution and verification functions implemented in Python. The solution function is restricted to invoking tool functions or performing logical computations, and cannot call other functions or directly access the database, ensuring the task can only be solved through the tool interface. Additionally, the results produced by the solution function must be validated by the verification function. If the solution is not validated, the agent will modify the solution or verification functions until the solution's output passes the verification. The agent then iteratively increases the difficulty of the task and updates the corresponding solution and verification functions. During this iterative process, if the current toolset is not sufficient to solve the task, the agent will augment the toolset.

Following this workflow, we obtain thousands of <environment, tools, task, verifier> tuples. We then perform RL on this dataset using DeepSeek-V3.2 and retain only instances with non-zero pass@100, resulting in 1,827 environments and their corresponding tasks (4,417 in total). A synthetic trip-planning example is illustrated below. This example highlights that, while searching the large combinatorial space for a trip plan that satisfies all constraints is challenging, checking whether a given candidate solution satisfies these constraints is relatively straightforward.
> 代码智能体我们通过从GitHub挖掘数百万个问题-拉取请求（PR）对，构建了大规模、可执行的软件问题解决环境。该数据集经过启发式规则和基于LLM的判断严格筛选，以确保高质量，要求每个条目包含合理的问题描述、相关的黄金补丁以及用于验证的测试补丁。我们利用DeepSeek-V3.2驱动的自动化环境设置代理为这些配对构建可执行环境。该代理处理软件包安装、依赖项解析和测试执行。测试结果以标准JUnit格式输出，确保跨编程语言和测试框架的解析一致性。只有当应用黄金补丁导致假阳性（F2P）测试用例数量非零（表明问题已修复）且通过转失败（P2F）测试用例数量为零（表明无回归）时，环境才被视为成功构建。通过此流程，我们成功构建了数万个可重现的问题解决环境，涵盖Python、Java、JavaScript、TypeScript、C、C++、Go和PHP等多种编程语言。

> 代码解释器智能体我们利用Jupyter Notebook作为代码解释器来处理复杂的推理任务。为此，我们策划了一系列涵盖数学、逻辑和数据科学的多样化问题，每个问题都需要模型利用代码执行能力来得出解决方案。

> 通用智能体为了在强化学习中扩展智能体环境和任务，我们采用了一个自动环境合成智能体，合成了1,827个面向任务的环境。这些任务难以解决但易于验证。合成工作流主要包括环境和工具集构建、任务合成以及解决方案生成。具体流程如下。

> 1. 给定一个任务类别（例如，规划旅行行程）和一个配备bash和搜索工具的沙盒，智能体首先使用这些工具从互联网生成或检索相关数据，并将其存储在沙盒数据库中。

> 2. 然后，智能体合成一组特定于任务的工具，每个工具都实现为一个函数。

> 3. 为了创建既具有挑战性又可自动验证的任务，智能体首先基于当前数据库提出一个简单任务，并附上其解决方案和用Python实现的验证函数。解决方案函数仅限于调用工具函数或执行逻辑计算，不能调用其他函数或直接访问数据库，确保任务只能通过工具接口解决。此外，解决方案函数产生的结果必须由验证函数验证。如果解决方案未通过验证，智能体将修改解决方案或验证函数，直到解决方案的输出通过验证。然后，智能体迭代增加任务难度，并更新相应的解决方案和验证函数。在此迭代过程中，如果当前工具集不足以解决任务，智能体将扩展工具集。

> 遵循此工作流，我们获得了数千个<环境、工具、任务、验证器>元组。然后，我们使用DeepSeek-V3.2对该数据集进行强化学习，并仅保留通过率非零的实例，最终得到1,827个环境及其相应任务（总计4,417个）。下面展示了一个合成的旅行规划示例。该示例强调，虽然在大规模组合空间中搜索满足所有约束的旅行计划具有挑战性，但检查给定候选解决方案是否满足这些约束则相对简单。