# 问题追踪器：本地 Markdown

此仓库的 Issues 和 PRD 以 markdown 文件形式存放在 `.scratch/` 中。

## 约定

- 每个功能一个目录：`.scratch/<feature-slug>/`
- PRD 文件为 `.scratch/<feature-slug>/PRD.md`
- 实现 issue 位于 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`，编号从 `01` 开始
- 分诊状态记录在每个 issue 文件顶部附近的 `Status:` 行中（角色字符串见 `triage-labels.md`）
- 评论和会话历史会追加到文件底部的 `## Comments` 标题下

## 当某个技能说“发布到问题追踪器”时

在 `.scratch/<feature-slug>/` 下创建一个新文件（如有需要先创建目录）。

## 当某个技能说“获取相关工单”时

读取引用路径对应的文件。用户通常会直接传入路径或 issue 编号。
