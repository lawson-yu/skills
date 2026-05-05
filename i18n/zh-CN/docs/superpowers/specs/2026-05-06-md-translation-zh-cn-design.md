# 2026-05-06 项目 Markdown 中文镜像翻译设计

## 背景与目标

- 仓库内存在大量 Markdown 文档（含根目录文档、`docs/**`、以及 `skills/**` 下的 `SKILL.md` 与辅助文档）。
- 目标是在**不覆盖原文**的前提下，为仓库内所有 `*.md` 生成**中文译文镜像**，以便中文读者浏览。

## 范围

- 翻译对象：仓库内所有 `*.md` 文件（包含 `skills/personal/`、`skills/deprecated/`、`.out-of-scope/`、`docs/adr/` 等）。
- 产物：为每个原文 `X.md` 生成对应译文 `i18n/zh-CN/X.md`（路径镜像）。

## 产物与目录结构

- 原文文件保持原路径不动。
- 中文译文统一写入：`i18n/zh-CN/`。
- 路径镜像规则：
  - `./README.md` → `./i18n/zh-CN/README.md`
  - `./skills/engineering/tdd/SKILL.md` → `./i18n/zh-CN/skills/engineering/tdd/SKILL.md`
  - `./docs/adr/0001-xxx.md` → `./i18n/zh-CN/docs/adr/0001-xxx.md`

## 翻译内容规则

- 翻译自然语言正文为中文。
- 以下内容保持原样（不翻译）：
  - fenced code block（```）内容
  - 内联代码（`code`）
  - 命令、文件路径、标识符（函数名、变量名、JSON/YAML key 等）
- Markdown 结构尽量保持一致（标题层级、列表、表格、引用块）。

## 链接与锚点处理

目标：中文译文中的仓库内文档链接**优先跳转到对应中文译文**；若目标译文不存在，则保留指向原文。

- 对指向仓库内 `.md` 的**相对链接**：
  - 解析目标真实路径；若 `i18n/zh-CN/<目标原路径>` 存在，则改写链接指向该译文（使用正确的相对路径）；否则保持原链接不变。
- 处理带锚点链接 `some.md#anchor`：
  - 文件路径部分按上述规则改写；
  - `#anchor` 先原样保留（避免依赖不同渲染器的 slug 规则导致误改）。
- 外部链接（http/https）、图片/资源链接保持不变。

## 验收标准

- 对每个原文 `X.md`，存在对应译文 `i18n/zh-CN/X.md`。
- 译文中 code block / 内联代码 / 命令 / 路径 / 标识符保持原样。
- Markdown 结构未被破坏，文件可正常渲染。
- `.md` 相对链接在目标译文存在时优先指向中文译文。
- 不修改原文内容。

## 提交与集成

- 单个提交引入全量 `i18n/zh-CN/**` 译文与必要的最小化改动。
- 用户确认需要直接 push：在 commit 后执行 `git push`。

```python
