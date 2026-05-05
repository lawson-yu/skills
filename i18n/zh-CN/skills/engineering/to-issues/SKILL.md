---
---
name: to-issues
description: 将计划、规范或 PRD 拆分为项目 issue 跟踪器上可独立领取的问题，使用 tracer-bullet 垂直切片。当用户希望把计划转换为 issues、创建实现工单，或将工作拆分为 issues 时使用。
---

# To Issues

使用垂直切片（tracer bullets）将计划拆分为可独立领取的问题。

问题跟踪器和分诊标签词汇应已提供给你——如果没有，请运行 `/setup-matt-pocock-skills`。

## 流程

### 1. 收集上下文

基于对话上下文中已有的内容开展工作。如果用户通过参数传入 issue 引用（issue 编号、URL 或路径），从问题跟踪器获取它并阅读其完整正文和评论。

### 2. 探索代码库（可选）

如果你尚未探索代码库，请先进行探索以了解代码当前状态。Issue 标题和描述应使用项目的领域术语词汇，并遵循你所触及区域中的 ADR。

### 3. 起草垂直切片

将计划拆分为 **tracer bullet** issues。每个 issue 都是一个贯穿所有集成层端到端的细垂直切片，而不是单层的水平切片。

切片可以是 “HITL” 或 “AFK”。HITL 切片需要人工交互，例如架构决策或设计评审。AFK 切片可以在无需人工交互的情况下实现并合并。尽可能优先选择 AFK 而不是 HITL。

<vertical-slice-rules>
- 每个切片交付一条狭窄但完整的、穿过每一层（schema、API、UI、tests）的路径
- 已完成的切片应可单独演示或验证
- 优先选择多个薄切片，而不是少量厚切片
</vertical-slice-rules>

### 4. 向用户提问

以编号列表形式展示建议的拆分。对于每个切片，展示：

- **Title**：简短的描述性名称
- **Type**：HITL / AFK
- **Blocked by**：必须先完成的其他切片（如有）
- **User stories covered**：该切片覆盖了哪些用户故事（如果源材料包含用户故事）

向用户询问：

- 粒度是否合适？（太粗 / 太细）
- 依赖关系是否正确？
- 是否有切片应进一步合并或拆分？
- HITL 与 AFK 的标记是否正确？

迭代直到用户批准该拆分。

### 5. 将 issues 发布到问题跟踪器

对于每个已批准的切片，在问题跟踪器中发布一个新 issue。使用下面的 issue 正文模板。应用 `needs-triage` 分诊标签，使每个 issue 进入常规分诊流程。

按依赖顺序发布 issues（先阻塞项），这样你可以在 “Blocked by” 字段中引用真实的 issue 标识符。

<issue-template>
## Parent

父 issue 在问题跟踪器上的引用（如果来源是现有 issue，否则省略本节）。

## What to build

对此垂直切片的简要描述。描述端到端行为，而不是逐层实现。

## Acceptance criteria

- [ ] 标准 1
- [ ] 标准 2
- [ ] 标准 3

## Blocked by

- 阻塞工单的引用（如有）

若无阻塞项，则写 “None - can start immediately”。

</issue-template>

不要关闭或修改任何父 issue。
