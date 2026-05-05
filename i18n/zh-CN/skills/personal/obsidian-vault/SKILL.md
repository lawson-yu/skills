---
---
name: obsidian-vault
description: 在 Obsidian 知识库中使用 wikilinks 和索引笔记搜索、创建和管理笔记。适用于用户希望在 Obsidian 中查找、创建或整理笔记的场景。
---

# Obsidian 知识库

## 知识库位置

`/mnt/d/Obsidian Vault/AI Research/`

根目录大多为扁平结构。

## 命名规范

- **索引笔记**：聚合同类主题（例如 `Ralph Wiggum Index.md`、`Skills Index.md`、`RAG Index.md`）
- 所有笔记名称使用 **Title case**
- 不使用文件夹进行组织——改用链接和索引笔记

## 链接

- 使用 Obsidian `[[wikilinks]]` 语法：`[[Note Title]]`
- 笔记在底部链接其依赖项/相关笔记
- 索引笔记仅由 `[[wikilinks]]` 列表组成

## 工作流

### 搜索笔记

```bash
# Search by filename
find "/mnt/d/Obsidian Vault/AI Research/" -name "*.md" | grep -i "keyword"

# Search by content
grep -rl "keyword" "/mnt/d/Obsidian Vault/AI Research/" --include="*.md"
```

或直接在知识库路径上使用 Grep/Glob 工具。

### 创建新笔记

1. 文件名使用 **Title Case**
2. 按照一个学习单元编写内容（依据知识库规则）
3. 在底部添加指向相关笔记的 `[[wikilinks]]`
4. 若属于编号序列的一部分，使用分层编号方案

### 查找相关笔记

在整个知识库中搜索 `[[Note Title]]` 以查找反向链接：

```bash
grep -rl "\\[\\[Note Title\\]\\]" "/mnt/d/Obsidian Vault/AI Research/"
```

### 查找索引笔记

```bash
find "/mnt/d/Obsidian Vault/AI Research/" -name "*Index*"
```
