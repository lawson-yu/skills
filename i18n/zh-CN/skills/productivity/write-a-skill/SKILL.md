---
name: write-a-skill
description: 使用正确结构、渐进披露和捆绑资源创建新的代理技能。用于用户想要创建、编写或构建新技能时。
---

# 编写技能

## 流程

1. **收集需求** - 询问用户：
   - 该技能覆盖什么任务/领域？
   - 它应处理哪些具体用例？
   - 需要可执行脚本还是仅需说明？
   - 是否有需要包含的参考资料？

2. **起草技能** - 创建：
   - 包含简洁说明的 SKILL.md
   - 若内容超过 500 行则添加额外参考文件
   - 若需要确定性操作则添加实用脚本

3. **与用户评审** - 展示草稿并询问：
   - 这是否覆盖了你的用例？
   - 是否有缺失或不清楚的地方？
   - 某些部分是否应更详细/更简略？

## 技能结构

```
skill-name/
├── SKILL.md           # Main instructions (required)
├── REFERENCE.md       # Detailed docs (if needed)
├── EXAMPLES.md        # Usage examples (if needed)
└── scripts/           # Utility scripts (if needed)
    └── helper.js
```

## SKILL.md 模板

```md
---
name: skill-name
description: Brief description of capability. Use when [specific triggers].
---

# Skill Name

## Quick start

[Minimal working example]

## Workflows

[Step-by-step processes with checklists for complex tasks]

## Advanced features

[Link to separate files: See [REFERENCE.md](REFERENCE.md)]
```

## Description 要求

description 是**你的代理在决定加载哪个技能时唯一能看到的内容**。它会与其他所有已安装技能一起显示在系统提示中。你的代理会读取这些 description，并根据用户请求选择相关技能。

**目标**：给代理恰好足够的信息，让它知道：

1. 该技能提供什么能力
2. 何时/为何触发它（具体关键词、上下文、文件类型）

**格式**：

- 最多 1024 个字符
- 使用第三人称
- 第一句：它做什么
- 第二句："Use when [specific triggers]"

**好的示例**：

```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**不好的示例**：

```
Helps with documents.
```

这个不好的示例没有给代理任何方式将其与其他文档类技能区分开来。

## 何时添加脚本

在以下情况添加实用脚本：

- 操作是确定性的（校验、格式化）
- 同样的代码会被重复生成
- 错误需要显式处理

与生成代码相比，脚本可以节省 token 并提升可靠性。

## 何时拆分文件

在以下情况拆分到独立文件：

- SKILL.md 超过 100 行
- 内容包含不同领域（如 finance 与 sales schema）
- 高级功能很少会被用到

## 评审清单

起草后，确认：

- [ ] Description 包含触发条件（"Use when..."）
- [ ] SKILL.md 少于 100 行
- [ ] 不包含时效性信息
- [ ] 术语一致
- [ ] 包含具体示例
- [ ] 引用深度仅一层
