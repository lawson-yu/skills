# 问题跟踪器：GitLab

此仓库的 Issues 和 PRD 以 GitLab issues 的形式维护。所有操作都使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 约定

- **创建 issue**：`glab issue create --title "..." --description "..."`。多行描述请使用 heredoc。传入 `--description -` 以打开编辑器。
- **读取 issue**：`glab issue view <number> --comments`。机器可读输出请使用 `-F json`。
- **列出 issues**：`glab issue list --state opened -F json`，并配合适当的 `--label` 过滤器。注意 GitLab 的状态值使用 `opened`（不是 `open`）。
- **在 issue 上评论**：`glab issue note <number> --message "..."`。GitLab 将评论称为“notes”。
- **添加 / 移除标签**：`glab issue update <number> --label "..."` / `--unlabel "..."`。多个标签可用逗号分隔，或重复使用该 flag。
- **关闭**：`glab issue close <number>`。`glab issue close` 不接受关闭说明，因此请先用 `glab issue note <number> --message "..."` 发布说明，再执行关闭。
- **合并请求**：GitLab 将 PR 称为“merge requests”。使用 `glab mr create`、`glab mr view`、`glab mr note` 等——其形式与 `gh pr ...` 相同，只是将 `pr` 替换为 `mr`，并将 `comment`/`--body` 替换为 `note`/`--message`。

从 `git remote -v` 推断仓库——在 clone 内运行时，`glab` 会自动完成此操作。

## 当某个技能说“publish to the issue tracker”时

创建一个 GitLab issue。

## 当某个技能说“fetch the relevant ticket”时

运行 `glab issue view <number> --comments`。
