---
---
name: qa
description: 交互式 QA 会话：用户以对话方式报告 bug 或问题，代理创建 GitHub issue。会在后台探索代码库以获取上下文和领域术语。当用户想要报告 bug、进行 QA、以对话方式创建 issue，或提到“QA session”时使用。
---

# QA 会话

运行一个交互式 QA 会话。用户描述他们遇到的问题。你进行澄清、探索代码库获取上下文，并创建 GitHub issue，这些 issue 应该是可长期使用的、以用户为中心的，并使用项目的领域语言。

## 针对用户提出的每个问题

### 1. 倾听并轻度澄清

让用户用他们自己的话描述问题。最多提 **2-3 个简短澄清问题**，重点关注：

- 他们预期发生什么 vs 实际发生了什么
- 复现步骤（如果不明显）
- 是稳定复现还是偶发

不要过度追问。如果描述已经足够用于创建 issue，就继续下一步。

### 2. 在后台探索代码库

在与用户交流的同时，在后台启动一个 Agent（`subagent_type=Explore`）来了解相关区域。目标不是找修复方案，而是：

- 学习该区域使用的领域语言（查看 UBIQUITOUS_LANGUAGE.md）
- 理解该功能本应如何工作
- 识别面向用户的行为边界

这些上下文有助于你写出更好的 issue——但 issue 本身不应引用具体文件、行号或内部实现细节。

### 3. 评估范围：单个 issue 还是拆分？

在创建前，判断这是 **单个 issue** 还是需要 **拆分** 为多个 issue。

在以下情况下拆分：

- 修复跨越多个相互独立的区域（例如：“表单校验不对 AND 成功提示缺失 AND 跳转有问题”）
- 存在可明显分离、可由不同人并行处理的关注点
- 用户描述的问题包含多个彼此独立的失败模式或症状

在以下情况下保持单个 issue：

- 是一个位置上的一个行为有误
- 各种症状都由同一个根行为导致

### 4. 创建 GitHub issue（一个或多个）

使用 `gh issue create` 创建 issue。不要先让用户审阅——直接创建并分享 URL。

issue 必须 **可长期使用**——在经历重大重构后仍应有意义。请从用户视角来写。

#### 对于单个 issue

使用此模板：

```
## What happened

[用通俗语言描述用户实际遇到的行为]

## What I expected

[描述期望行为]

## Steps to reproduce

1. [开发者可执行的具体编号步骤]
2. [使用代码库中的领域术语，而不是内部模块名]
3. [包含相关输入、标志或配置]

## Additional context

[来自用户或代码库探索的额外观察，有助于界定问题——例如“仅在使用 Docker layer 时发生，filesystem layer 不会”——使用领域语言，但不要引用文件]
```

#### 对于拆分场景（多个 issue）

按依赖顺序创建 issue（先 blocker），这样你可以引用真实 issue 编号。

每个子 issue 使用此模板：

```
## Parent issue

#<parent-issue-number>（如果你创建了追踪 issue）或 "Reported during QA session"

## What's wrong

[描述这个特定行为问题——只写这一部分，不写整个报告]

## What I expected

[这个特定部分的期望行为]

## Steps to reproduce

1. [仅针对该 issue 的步骤]

## Blocked by

- #<issue-number>（如果此 issue 需等待其他 issue 解决后才能修复）

或如果无阻塞则写 "None — can start immediately"。

## Additional context

[与这一部分相关的额外观察]
```

在创建拆分 issue 时：

- **优先“多而薄”的 issue，而不是“少而厚”**——每个都应可独立修复和验证
- **诚实标注阻塞关系**——如果 issue B 的确无法在 issue A 修复前测试，就明确写出；若独立，则都标为 "None — can start immediately"
- **按依赖顺序创建 issue**，以便在 "Blocked by" 中引用真实 issue 编号
- **最大化并行性**——目标是多个人（或代理）可以同时领取不同 issue

#### 所有 issue 内容规则

- **不要写文件路径或行号**——这些会过时
- **使用项目的领域语言**（如果存在，请查看 UBIQUITOUS_LANGUAGE.md）
- **描述行为，不描述代码**——写“同步服务未能应用补丁”，不要写“applyPatch() 在第 42 行抛错”
- **复现步骤是必填项**——如果无法确定，向用户询问
- **保持简洁**——开发者应在 30 秒内读完 issue

创建完成后，打印所有 issue URL（并总结阻塞关系），然后问："Next issue, or are we done?"

### 5. 继续会话

持续进行，直到用户表示结束。每个 issue 相互独立——不要批量处理。
