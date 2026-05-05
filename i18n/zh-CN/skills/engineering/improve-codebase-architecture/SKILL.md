---
name: improve-codebase-architecture
description: 在代码库中发现加深机会，参考 `CONTEXT.md` 中的领域语言以及 `docs/adr/` 中的决策。当用户希望改进架构、寻找重构机会、整合紧密耦合的模块，或让代码库更易测试、更便于 AI 导航时使用。
---

# 改进代码库架构

识别架构摩擦并提出**加深机会**——将浅模块重构为深模块。目标是可测试性和 AI 可导航性。

## 术语表

在每一条建议中都精确使用这些术语。一致的语言才是重点——不要漂移到 “component”、“service”、“API” 或 “boundary”。完整定义见 [LANGUAGE.md](LANGUAGE.md)。

- **Module** — 任何具有接口和实现的事物（function、class、package、slice）。
- **Interface** — 调用方为使用该模块必须了解的一切：types、invariants、error modes、ordering、config。不只是 type signature。
- **Implementation** — 内部代码。
- **Depth** — 接口层面的杠杆：用小接口承载大量行为。**Deep** = 高杠杆。**Shallow** = 接口几乎和实现一样复杂。
- **Seam** — 接口所在之处；无需就地修改即可改变行为的位置。（使用这个词，不用 “boundary”。）
- **Adapter** — 在某个 seam 上满足接口的具体实现。
- **Leverage** — 调用方从 depth 中获得的收益。
- **Locality** — 维护者从 depth 中获得的收益：变更、缺陷、知识集中在同一个地方。

关键原则（完整列表见 [LANGUAGE.md](LANGUAGE.md)）：

- **Deletion test**：设想删除该模块。如果复杂度随之消失，它就是透传层。如果复杂度在 N 个调用方中重新出现，它就在发挥价值。
- **The interface is the test surface.**
- **One adapter = hypothetical seam. Two adapters = real seam.**

此技能会由项目的领域模型_提供信息_。领域语言为优质 seam 命名；ADR 记录了该技能不应重复争论的决策。

## 流程

### 1. 探索

先阅读项目的领域术语表，以及你要涉及区域中的所有 ADR。

然后使用 Agent 工具并设置 `subagent_type=Explore` 来遍历代码库。不要遵循僵化启发式——自然探索，并记录你感受到摩擦的位置：

- 理解一个概念时，是否必须在许多小模块之间来回跳转？
- 哪些模块是**shallow**——接口几乎和实现一样复杂？
- 哪些纯函数只是为了可测试性而被提取，但真实缺陷隐藏在调用方式中（缺乏 **locality**）？
- 哪些紧密耦合的模块跨 seam 泄漏？
- 代码库中哪些部分未测试，或难以通过当前 interface 进行测试？

对任何你怀疑是 shallow 的对象应用 **deletion test**：删除它会集中复杂度，还是仅仅转移复杂度？你要的信号是“会集中”。

### 2. 展示候选项

用编号列表给出加深机会。每个候选项包含：

- **Files** — 涉及哪些文件/模块
- **Problem** — 当前架构为何造成摩擦
- **Solution** — 用简单英文描述将发生什么变化
- **Benefits** — 从 locality 和 leverage 的角度解释收益，同时说明测试将如何改进

**领域请使用 `CONTEXT.md` 词汇，架构请使用 [LANGUAGE.md](LANGUAGE.md) 词汇。** 如果 `CONTEXT.md` 定义了 “Order”，就说 “the Order intake module”——不要说 “the FooBarHandler”，也不要说 “the Order service”。

**ADR 冲突**：如果某个候选项与现有 ADR 冲突，只有在摩擦真实到足以重新审视 ADR 时才提出。务必清晰标注（例如 _“contradicts ADR-0007 — but worth reopening because…”_）。不要罗列所有被 ADR 禁止的理论性重构。

暂时不要提出接口。请询问用户：“Which of these would you like to explore?”

### 3. 深挖循环（Grilling loop）

用户选定候选项后，进入深挖对话。与用户一起走完整个设计树——约束、依赖、加深后模块的形态、seam 后面放什么、哪些测试仍然成立。

随着决策逐步清晰，副作用将同步发生：

- **把加深后的模块命名为 `CONTEXT.md` 中不存在的概念？** 把该术语加入 `CONTEXT.md`——与 `/grill-with-docs` 相同的纪律（见 [CONTEXT-FORMAT.md](../grill-with-docs/CONTEXT-FORMAT.md)）。如文件不存在则按需创建。
- **在对话中把一个模糊术语变得更清晰？** 当场更新 `CONTEXT.md`。
- **用户以关键理由否决候选项？** 提供 ADR 建议，措辞为：_“Want me to record this as an ADR so future architecture reviews don't re-suggest it?”_ 仅当该理由确实会帮助未来探索者避免重复建议时才提出——跳过短期理由（“现在不值得做”）和不言自明的理由。见 [ADR-FORMAT.md](../grill-with-docs/ADR-FORMAT.md)。
- **想为加深后的模块探索替代接口？** 见 [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md)。
