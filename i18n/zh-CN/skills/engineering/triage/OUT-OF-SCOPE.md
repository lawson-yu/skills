# 超出范围知识库

仓库中的 `.out-of-scope/` 目录用于存储被拒绝功能请求的持久记录。它有两个目的：

1. **机构记忆** —— 记录某项功能为何被拒绝，以便在 issue 关闭后相关理由不会丢失
2. **去重** —— 当有与先前拒绝项匹配的新 issue 进入时，skill 可以呈现之前的决策，而不是重新争论

## 目录结构

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

每个**概念**对应一个文件，而不是每个 issue 对应一个文件。多个请求同一事项的 issue 应归并到同一个文件下。

## 文件格式

文件应采用轻松、易读的风格来撰写——更像简短的设计文档，而不是数据库条目。使用段落、代码示例和案例，让首次接触的人也能清楚理解并觉得有用。

```markdown
# Dark Mode

This project does not support dark mode or user-facing theming.

## Why this is out of scope

The rendering pipeline assumes a single color palette defined in
`ThemeConfig`. Supporting multiple themes would require:

- A theme context provider wrapping the entire component tree
- Per-component theme-aware style resolution
- A persistence layer for user theme preferences

This is a significant architectural change that doesn't align with the
project's focus on content authoring. Theming is a concern for downstream
consumers who embed or redistribute the output.

```ts
// The current ThemeConfig interface is not designed for runtime switching:
interface ThemeConfig {
  colors: ColorPalette; // single palette, resolved at build time
  fonts: FontStack;
}
```

## Prior requests

- #42 — "Add dark mode support"
- #87 — "Night theme for accessibility"
- #134 — "Dark theme option"
```

### 文件命名

为该概念使用简短、描述性的 kebab-case 名称：`dark-mode.md`、`plugin-system.md`、`graphql-api.md`。名称应足够直观，使浏览目录的人无需打开文件也能理解被拒绝的是什么。

### 撰写拒绝理由

理由应当有实质内容——不是“我们不想做这个”，而是说明为什么。好的理由会引用：

- 项目范围或理念（“本项目聚焦于 X；主题化属于下游关注点”）
- 技术约束（“支持该项需要 Y，这与我们的 Z 架构冲突”）
- 战略决策（“我们选择使用 A 而不是 B，因为……”）

理由应具备长期有效性。避免引用临时性情况（“我们现在太忙了”）——那不是真正的拒绝，而是延期。

## 何时检查 `.out-of-scope/`

在分流期间（步骤 1：收集上下文），读取 `.out-of-scope/` 中的所有文件。评估新 issue 时：

- 检查该请求是否与已有超出范围概念匹配
- 匹配基于概念相似性，而非关键词——“night theme” 匹配 `dark-mode.md`
- 如果匹配，将其反馈给维护者：“这与 `.out-of-scope/dark-mode.md` 类似——我们之前因为 [reason] 拒绝过。你现在仍然这么认为吗？”

维护者可能会：

- **确认** —— 将新 issue 添加到现有文件的 “Prior requests” 列表，然后关闭
- **重新考虑** —— 删除或更新超出范围文件，并让该 issue 继续正常分流流程
- **不同意** —— 这些 issue 相关但不相同，继续正常分流流程

## 何时写入 `.out-of-scope/`

仅当**增强请求**（不是 bug）以 `wontfix` 被拒绝时。流程如下：

1. 维护者决定某个功能请求超出范围
2. 检查是否已存在匹配的 `.out-of-scope/` 文件
3. 如果有：将新 issue 追加到 “Prior requests” 列表
4. 如果没有：使用该概念名称新建文件，写入决策、理由和第一条历史请求
5. 在 issue 下发表评论，解释该决策并提及 `.out-of-scope/` 文件
6. 使用 `wontfix` 标签关闭 issue

## 更新或移除超出范围文件

如果维护者改变了对先前被拒绝概念的看法：

- 删除该 `.out-of-scope/` 文件
- skill 无需重新打开旧 issue —— 它们是历史记录
- 触发重新考虑的新 issue 继续按正常分流流程处理
