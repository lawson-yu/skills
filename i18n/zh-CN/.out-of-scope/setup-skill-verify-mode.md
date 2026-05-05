# `setup-matt-pocock-skills` 的 Verify/Check 模式

本项目不会为 `setup-matt-pocock-skills` 添加专用的 verify/check 模式（或单独的 verify skill）。

## 为什么这不在范围内

用于检查 `docs/agents/*.md` 产物是否仍与 seed-template schema 匹配的第二个 skill（或 `--verify` 标志），会重复现有 setup skill 在对话中已经处理的工作。

预期工作流是：**运行 `/setup-matt-pocock-skills` 并告诉它验证你当前的设置。** 该 skill 由提示驱动，因此维护者可以将其限定为一次验证流程（“不要重写任何内容，只需将我现有的文件与当前 seed templates 对照检查并报告漂移”），而无需单独的代码路径。添加一个标志或同级 skill 会拆分一个已经可通过自然语言入口表达的功能的表面区域。

将配置管理保持为单一 skill 也可避免当 seed templates 演进时两个 skills 彼此漂移所带来的维护成本。

## 先前请求

- #106 — 功能请求：为 setup-matt-pocock-skills 提供 verify/check 模式

```python
