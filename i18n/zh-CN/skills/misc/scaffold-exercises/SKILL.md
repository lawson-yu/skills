---
---
name: scaffold-exercises
description: 创建练习目录结构，包含章节、题目、解答和讲解，并通过 lint 检查。当用户希望搭建练习结构、创建练习桩，或设置新课程章节时使用。
---

# 搭建练习结构

创建能够通过 `pnpm ai-hero-cli internal lint` 的练习目录结构，然后使用 `git commit` 提交。

## 目录命名

- **章节**：在 `exercises/` 内使用 `XX-section-name/`（例如：`01-retrieval-skill-building`）
- **练习**：在章节内使用 `XX.YY-exercise-name/`（例如：`01.03-retrieval-with-bm25`）
- 章节编号 = `XX`，练习编号 = `XX.YY`
- 名称使用 dash-case（小写，使用连字符）

## 练习变体

每个练习至少需要以下子文件夹之一：

- `problem/` - 带 TODO 的学员工作区
- `solution/` - 参考实现
- `explainer/` - 概念性材料，不含 TODO

在创建桩时，默认使用 `explainer/`，除非计划另有说明。

## 必需文件

每个子文件夹（`problem/`、`solution/`、`explainer/`）都需要一个 `readme.md`，并且：

- **不能为空**（必须有真实内容，即使只有一行标题也可以）
- 不能有失效链接

在创建桩时，创建一个包含标题和描述的最小 readme：

```md
# Exercise Title

Description here
```

如果子文件夹中有代码，还需要一个 `main.ts`（>1 行）。但对于桩，仅有 readme 的练习也可以。

## 工作流程

1. **解析计划** - 提取章节名称、练习名称和变体类型
2. **创建目录** - 为每个路径执行 `mkdir -p`
3. **创建桩 readme** - 每个变体文件夹创建一个带标题的 `readme.md`
4. **运行 lint** - 执行 `pnpm ai-hero-cli internal lint` 进行校验
5. **修复所有错误** - 迭代直到 lint 通过

## Lint 规则摘要

lint 工具（`pnpm ai-hero-cli internal lint`）会检查：

- 每个练习都有子文件夹（`problem/`、`solution/`、`explainer/`）
- 至少存在 `problem/`、`explainer/` 或 `explainer.1/` 之一
- 主子文件夹中的 `readme.md` 存在且非空
- 不允许有 `.gitkeep` 文件
- 不允许有 `speaker-notes.md` 文件
- readme 中不能有失效链接
- readme 中不能有 `pnpm run exercise` 命令
- 除非是仅 readme，否则每个子文件夹都要求 `main.ts`

## 移动/重命名练习

在重新编号或移动练习时：

1. 使用 `git mv`（不要用 `mv`）重命名目录 - 可保留 git 历史
2. 更新数字前缀以保持顺序
3. 移动后重新运行 lint

示例：

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## 示例：根据计划创建桩

给定如下计划：

```
Section 05: Memory Skill Building
- 05.01 Introduction to Memory
- 05.02 Short-term Memory (explainer + problem + solution)
- 05.03 Long-term Memory
```

创建：

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

然后创建 readme 桩：

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# Introduction to Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md -> "# Long-term Memory"
```
