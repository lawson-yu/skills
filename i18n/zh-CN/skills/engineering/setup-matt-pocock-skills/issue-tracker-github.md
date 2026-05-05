# 问题跟踪器：GitHub

此仓库的 Issues 和 PRD 以 GitHub issues 的形式管理。所有操作都使用 `gh` CLI。

## 约定

- **创建 issue**：`gh issue create --title "..." --body "..."`。多行 body 使用 heredoc。
- **读取 issue**：`gh issue view <number> --comments`，使用 `jq` 过滤评论，并同时获取 labels。
- **列出 issues**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`，并配合适当的 `--label` 与 `--state` 过滤器。
- **给 issue 评论**：`gh issue comment <number> --body "..."`
- **添加 / 移除 labels**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**：`gh issue close <number> --comment "..."`

从 `git remote -v` 推断仓库——在克隆仓库内运行时，`gh` 会自动完成此操作。

## 当某个 skill 说“publish to the issue tracker”时

创建一个 GitHub issue。

## 当某个 skill 说“fetch the relevant ticket”时

运行 `gh issue view <number> --comments`。
