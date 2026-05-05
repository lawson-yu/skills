<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="技能" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

# 面向真实工程师的技能

我每天用来做真实工程的 agent 技能——不是 vibe coding。

开发真正的应用很难。像 GSD、BMAD 和 Spec-Kit 这样的方式试图通过接管流程来提供帮助。但在这么做的同时，它们剥夺了你的控制权，并让流程中的 bug 更难解决。

这些技能被设计为小巧、易于适配、可组合。它们适用于任何模型。它们基于数十年的工程经验。尽情折腾它们。把它们改造成你自己的。享受吧。

如果你想跟进这些技能的更新，以及我创建的任何新技能，你可以和约 60,000 名其他开发者一起订阅我的通讯：

[订阅通讯](https://www.aihero.dev/s/skills-newsletter)

## 快速开始（30 秒设置）

1. 运行 skills.sh 安装器：

```bash
npx skills@latest add mattpocock/skills
```

2. 选择你想要的技能，以及你想把它们安装到哪些 coding agent 上。**请确保你选择了 `/setup-matt-pocock-skills`**。

3. 在你的 agent 中运行 `/setup-matt-pocock-skills`。它会：
   - 询问你想使用哪种 issue tracker（GitHub、Linear 或本地文件）
   - 询问你在分诊 ticket 时使用哪些标签（`/triage` 使用标签）
   - 询问你希望将我们创建的文档保存到哪里

4. 搞定——你已经可以开始了。

## 为什么会有这些技能

我构建这些技能，是为了修复我在 Claude Code、Codex 和其他 coding agent 中看到的常见失败模式。

### #1：Agent 没有按我想要的方式做

> “没有人真正知道自己到底想要什么”
>
> David Thomas & Andrew Hunt，[《程序员修炼之道》](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**。软件开发中最常见的失败模式是认知不一致。你以为开发者知道你想要什么。然后你看到他们做出来的东西——才发现它完全没理解你。

在 AI 时代也是一样。你和 agent 之间存在沟通鸿沟。解决方法是进行一次 **grilling session**——让 agent 就你要构建的内容向你提出细致问题。

**解决方案**是使用：

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) —— 用于非代码场景
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) —— 与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 相同，但附带更多好东西（见下文）

这些是我最受欢迎的技能。它们帮助你在开始之前先与 agent 对齐，并更深入地思考你要做的改动。每次你想做改动时都使用它们。

### #2：Agent 太啰嗦了

> 有了统一语言，开发者之间的对话和代码表达都源自同一个领域模型。
>
> Eric Evans，[《领域驱动设计》](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**问题**：在项目开始时，开发者和他们所服务的软件需求方（领域专家）通常说着不同的语言。

我和我的 agent 也感受到了同样的张力。Agent 往往被直接扔进项目里，要求边做边理解术语。于是本来 1 个词能说清的事，它会用 20 个词。

**解决方案**是建立共享语言。这是一份文档，用于帮助 agent 解码项目中使用的术语。

<details>
<summary>
示例
</summary>

这是我 `course-video-manager` 仓库中的一个 [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) 示例。哪一种更容易读？

- **之前**："There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **之后**："There's a problem with the materialization cascade"

这种简洁会在一次又一次会话中持续带来收益。

</details>

这已经内置在 [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) 中。它是一场 grilling session，同时还帮助你与 AI 建立共享语言，并将难以解释的决策记录到 ADR 中。

这有多强大很难用语言说明。它可能是这个仓库里最酷的单一技巧。试试看你就知道了。

> [!TIP]
> 共享语言除了减少冗长，还有许多其他好处：
>
> - **变量、函数和文件命名更一致**，都基于共享语言
> - 因此，agent **更容易在代码库中导航**
> - agent 还会**在思考时消耗更少 token**，因为它可以使用更简洁的语言

### #3：代码跑不起来

> “始终采取小而审慎的步骤。反馈速度就是你的限速器。永远不要承担过大的任务。”
>
> David Thomas & Andrew Hunt，[《程序员修炼之道》](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**：假设你和 agent 已经就“要构建什么”达成一致。那如果 agent _仍然_ 产出垃圾怎么办？

这时该看看你的反馈回路了。如果没有关于它产出的代码实际运行情况的反馈，agent 就是在盲飞。

**解决方案**：你需要常规的一整套反馈回路：静态类型、浏览器访问和自动化测试。

对于自动化测试，red-green-refactor 循环至关重要。也就是 agent 先写一个失败测试，再去修复测试。这能给 agent 提供稳定一致的反馈层级，从而产出更好的代码。

我构建了一个可插入任意项目的 **[`/tdd`](./skills/engineering/tdd/SKILL.md) 技能**。它鼓励 red-green-refactor，并为 agent 提供大量关于什么是好测试、什么是坏测试的指导。

对于调试，我还构建了一个 **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** 技能，把最佳调试实践封装成一个简单循环。

### #4：我们造出了一团泥球

> “每天都要投入到系统设计中。”
>
> Kent Beck，[《解析极限编程》](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> “最好的模块是深模块。它们通过简单接口提供大量功能。”
>
> John Ousterhout，[《软件设计的哲学》](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**问题**：大多数由 agent 构建的应用都复杂且难以变更。因为 agent 能极大加速编码，也同样会加速软件熵增。代码库复杂度以前所未有的速度上升。

**解决方案**是采用一种由 AI 驱动开发的全新激进方法：重视代码设计。

这被内置到这些技能的每一层：

- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) 会在创建 PRD 之前，就你将触及哪些模块对你提问
- [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) 会让 agent 在整个系统上下文中解释代码

更关键的是，[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) 能帮助你拯救已经变成泥球的代码库。我建议你每隔几天就在代码库上跑一次它。

### 总结

软件工程基本功比以往任何时候都更重要。这些技能是我对将这些基本功浓缩为可重复实践的最佳尝试，帮助你交付职业生涯中最好的应用。享受吧。

## 参考

### Engineering

我每天用于代码工作的技能。

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** —— 针对疑难 bug 和性能回归的纪律化诊断循环：复现 → 最小化 → 假设 → 埋点 → 修复 → 回归测试。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** —— 一场 grilling session，用现有领域模型来挑战你的计划，打磨术语，并内联更新 `CONTEXT.md` 与 ADR。
- **[triage](./skills/engineering/triage/SKILL.md)** —— 通过一个分诊角色状态机来分诊问题。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** —— 在 `CONTEXT.md` 的领域语言和 `docs/adr/` 中决策的指导下，发现代码库中的深化机会。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** —— 搭建每个仓库的配置脚手架（issue tracker、分诊标签词汇、领域文档布局），供其他工程技能使用。每个仓库只需运行一次，然后再使用 `to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture` 或 `zoom-out`。
- **[tdd](./skills/engineering/tdd/SKILL.md)** —— 采用 red-green-refactor 循环的测试驱动开发。一次一个垂直切片地构建功能或修复 bug。
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** —— 将任意计划、规范或 PRD 拆分为可独立领取的 GitHub issue，采用垂直切片方式。
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** —— 将当前对话上下文转为 PRD，并提交为 GitHub issue。无需访谈——只综合你已经讨论过的内容。
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** —— 让 agent 抽离到更高层次，对不熟悉的代码区域给出更广泛上下文或更高层视角。

### Productivity

通用工作流工具，不限于代码。

- **[caveman](./skills/productivity/caveman/SKILL.md)** —— 超压缩沟通模式。通过去除填充内容，在保持完整技术准确性的同时将 token 使用量削减约 75%。
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** —— 就一个计划或设计对你进行持续追问，直到决策树的每个分支都被解决。
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** —— 按正确结构、渐进式披露和捆绑资源来创建新技能。

### Misc

我保留但很少使用的工具。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** —— 设置 Claude Code hooks，在危险 git 命令（push、reset --hard、clean 等）执行前进行拦截。
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** —— 将测试文件从 `as` 类型断言迁移到 @total-typescript/shoehorn。
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** —— 创建包含章节、题目、解答和讲解的练习目录结构。
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** —— 使用 lint-staged、Prettier、类型检查和测试来设置 Husky pre-commit hooks。

```python
