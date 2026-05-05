---
name: setup-matt-pocock-skills
description: 在 AGENTS.md/CLAUDE.md 和 `docs/agents/` 中设置一个 `## Agent skills` 区块，使工程技能了解此仓库的问题跟踪器（GitHub 或本地 markdown）、分诊标签词汇以及领域文档布局。在首次使用 `to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture` 或 `zoom-out` 之前运行；或者当这些技能看起来缺少关于问题跟踪器、分诊标签或领域文档的上下文时运行。
disable-model-invocation: true
---

# 设置 Matt Pocock 的技能

搭建工程技能默认使用的每仓库配置：

- **问题跟踪器** —— 问题存放的位置（默认是 GitHub；开箱即支持本地 markdown）
- **分诊标签** —— 五个规范分诊角色使用的字符串
- **领域文档** —— `CONTEXT.md` 和 ADR 的位置，以及读取它们的使用规则

这是一个由提示驱动的技能，不是确定性脚本。先探索、展示你发现的内容、与用户确认，然后再写入。

## 流程

### 1. 探索

查看当前仓库以了解其初始状态。读取已有内容；不要假设：

- `git remote -v` 和 `.git/config` —— 这是一个 GitHub 仓库吗？具体是哪一个？
- 仓库根目录下的 `AGENTS.md` 和 `CLAUDE.md` —— 任一是否存在？任一中是否已有 `## Agent skills` 区段？
- 仓库根目录下的 `CONTEXT.md` 和 `CONTEXT-MAP.md`
- `docs/adr/` 以及任何 `src/*/docs/adr/` 目录
- `docs/agents/` —— 该技能先前的输出是否已存在？
- `.scratch/` —— 这表明本地 markdown 问题跟踪器约定可能已经在使用中

### 2. 展示发现并提问

总结哪些已存在、哪些缺失。然后引导用户逐个完成这三项决策——一次展示一个部分，获取用户回答后再进入下一个。不要一次性抛出全部三项。

假设用户不了解这些术语。每个部分都以简短说明开头（它是什么、为什么这些技能需要它、如果做不同选择会改变什么）。然后展示选项和默认值。

**部分 A —— 问题跟踪器。**

> 说明：“问题跟踪器”是该仓库问题所在的位置。像 `to-issues`、`triage`、`to-prd` 和 `qa` 这样的技能会从这里读取并写入——它们需要知道是调用 `gh issue create`、在 `.scratch/` 下写 markdown 文件，还是按你描述的其他工作流执行。请选择你在该仓库里实际跟踪工作的地方。

默认立场：这些技能最初是为 GitHub 设计的。如果 `git remote` 指向 GitHub，建议用它。如果 `git remote` 指向 GitLab（`gitlab.com` 或自托管主机），建议用 GitLab。否则（或如果用户更偏好），提供：

- **GitHub** —— 问题存放在仓库的 GitHub Issues 中（使用 `gh` CLI）
- **GitLab** —— 问题存放在仓库的 GitLab Issues 中（使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI）
- **本地 markdown** —— 问题作为文件存放在该仓库的 `.scratch/<feature>/` 下（适合个人项目或无远程仓库的仓库）
- **其他**（Jira、Linear 等）—— 请用户用一段话描述工作流；技能会将其记录为自由格式文本

**部分 B —— 分诊标签词汇。**

> 说明：当 `triage` 技能处理新进问题时，它会按状态机推进——需要评估、等待报告者、准备好给 AFK agent 接手、准备好给人工处理，或不予修复。要做到这一点，它需要应用与你实际配置一致的标签（或你的问题跟踪器中的等价物）字符串。如果你的仓库已使用不同标签名（例如 `bug:triage` 而不是 `needs-triage`），请在这里进行映射，这样技能会应用正确标签而不是创建重复标签。

五个规范角色：

- `needs-triage` —— 维护者需要评估
- `needs-info` —— 等待报告者补充信息
- `ready-for-agent` —— 规格完整，可 AFK 处理（agent 无需人工上下文即可接手）
- `ready-for-human` —— 需要人工实现
- `wontfix` —— 不会处理

默认值：每个角色的字符串等于其名称。询问用户是否要覆盖任意项。如果其问题跟踪器中还没有现有标签，默认值即可。

**部分 C —— 领域文档。**

> 说明：某些技能（`improve-codebase-architecture`、`diagnose`、`tdd`）会读取 `CONTEXT.md` 文件以学习项目领域术语，并读取 `docs/adr/` 了解历史架构决策。它们需要知道仓库是单一全局上下文还是多个上下文（例如前后端分离的 monorepo），这样才能在正确位置查找。

确认布局：

- **单上下文** —— 仓库根目录下一个 `CONTEXT.md` + `docs/adr/`。大多数仓库是这种。
- **多上下文** —— 根目录下 `CONTEXT-MAP.md` 指向各上下文 `CONTEXT.md` 文件（通常是 monorepo）。

### 3. 确认并编辑

向用户展示草稿：

- 将添加到 `CLAUDE.md` / `AGENTS.md` 之一中的 `## Agent skills` 区块（选择规则见步骤 4）
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` 的内容

允许他们在写入前编辑。

### 4. 写入

**选择要编辑的文件：**

- 如果 `CLAUDE.md` 存在，编辑它。
- 否则如果 `AGENTS.md` 存在，编辑它。
- 若两者都不存在，询问用户要创建哪一个——不要替他们决定。

当 `CLAUDE.md` 已存在时绝不要创建 `AGENTS.md`（反之亦然）——始终编辑已存在的那个。

如果所选文件中已存在 `## Agent skills` 区块，请就地更新其内容，而不是追加重复区块。不要覆盖用户对周边区段的编辑。

该区块：

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Domain docs

[one-line summary of layout — "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

然后使用此技能文件夹中的种子模板作为起点写入这三个文档文件：

- [issue-tracker-github.md](./issue-tracker-github.md) —— GitHub 问题跟踪器
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) —— GitLab 问题跟踪器
- [issue-tracker-local.md](./issue-tracker-local.md) —— 本地 markdown 问题跟踪器
- [triage-labels.md](./triage-labels.md) —— 标签映射
- [domain.md](./domain.md) —— 领域文档读取规则 + 布局

对于“其他”问题跟踪器，请根据用户描述从零开始编写 `docs/agents/issue-tracker.md`。

### 5. 完成

告诉用户设置已完成，以及哪些工程技能现在会从这些文件读取。提到他们之后可以直接编辑 `docs/agents/*.md` —— 只有在他们想切换问题跟踪器或从头重新开始时，才需要重新运行此技能。
