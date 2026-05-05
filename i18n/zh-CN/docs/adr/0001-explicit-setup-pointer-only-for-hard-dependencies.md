---
# 仅对硬依赖保留显式 `/setup-matt-pocock-skills` 指引

工程技能依赖由 `/setup-matt-pocock-skills` 预置的每仓库配置（issue tracker、分诊标签词汇、领域文档布局）。有些技能如果没有这套配置就无法有意义地工作——它们必须发布到特定的 issue tracker，或应用特定的标签字符串。另一些技能只用它来提升输出质量（词汇、ADR 感知），即使没有它也能优雅降级。

我们将这些拆分为**硬依赖**和**软依赖**技能：

- **硬依赖**（`to-issues`、`to-prd`、`triage`）——包含一条显式单行提示：_"… should have been provided to you — run `/setup-matt-pocock-skills` if not."_ 没有映射时，输出不是模糊，而是错误。
- **软依赖**（`diagnose`、`tdd`、`improve-codebase-architecture`、`zoom-out`）——仅以模糊措辞提及“项目的领域术语表”和“你正在触及区域内的 ADR”。如果这些文档不存在，技能仍可工作；只是输出不够精准。

这种拆分让软依赖技能保持轻量（token-light），并避免在并非关键承载的位置生搬硬套 setup 指引。
