# Matt Pocock Skills

由 Claude Code 加载的 agent skills（斜杠命令和行为）集合。Skills 按 bucket 组织，并由 `/setup-matt-pocock-skills` 生成的按仓库配置进行使用。

## 语言

**Issue tracker**：
承载仓库 issues 的工具——GitHub Issues、Linear、本地 `.scratch/` markdown 约定，或类似工具。像 `to-issues`、`to-prd`、`triage` 和 `qa` 这类 skills 会从中读取并向其中写入。
_避免使用_：backlog manager、backlog backend、issue host

**Issue**：
**Issue tracker** 中单个被跟踪的工作单元——一个 bug、task、PRD，或由 `to-issues` 产出的切片。
_避免使用_：ticket（仅在引用将其称为 tickets 的外部系统时使用）

**Triage role**：
在 triage 期间应用到 **Issue** 的规范状态机标签（例如 `needs-triage`、`ready-for-afk`）。每个 role 都通过 `docs/agents/triage-labels.md` 映射到 **Issue tracker** 中真实的标签字符串。

## 关系

- 一个 **Issue tracker** 包含多个 **Issues**
- 一个 **Issue** 在同一时间只携带一个 **Triage role**

## 已标记的歧义

- “backlog” 之前被用来同时表示承载 issues 的*工具*和其中的*工作集合*——现已解决：该工具称为 **Issue tracker**；“backlog” 不再作为领域术语使用。
- “backlog backend” / “backlog manager”——现已解决：统一并入 **Issue tracker**。
