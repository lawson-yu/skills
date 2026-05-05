---
name: ubiquitous-language
description: 从当前对话中提取 DDD 风格的通用语言术语表，标记歧义并提出规范术语。保存到 UBIQUITOUS_LANGUAGE.md。当用户希望定义领域术语、构建术语表、强化术语一致性、创建通用语言，或提到“domain model”或“DDD”时使用。
disable-model-invocation: true
---

# 通用语言

从当前对话中提取并规范化领域术语，形成一致的术语表，并保存到本地文件。

## 流程

1. **扫描对话**，查找与领域相关的名词、动词和概念
2. **识别问题**：
   - 同一个词用于不同概念（歧义）
   - 不同词用于同一个概念（同义词）
   - 含糊或语义过载的术语
3. **提出规范术语表**，并给出明确的术语选择
4. **写入 `UBIQUITOUS_LANGUAGE.md`** 到当前工作目录，使用如下格式
5. **在对话中输出摘要**

## 输出格式

使用以下结构写入 `UBIQUITOUS_LANGUAGE.md` 文件：

```md
# Ubiquitous Language

## Order lifecycle

| Term        | Definition                                              | Aliases to avoid      |
| ----------- | ------------------------------------------------------- | --------------------- |
| **Order**   | A customer's request to purchase one or more items      | Purchase, transaction |
| **Invoice** | A request for payment sent to a customer after delivery | Bill, payment request |

## People

| Term         | Definition                                  | Aliases to avoid       |
| ------------ | ------------------------------------------- | ---------------------- |
| **Customer** | A person or organization that places orders | Client, buyer, account |
| **User**     | An authentication identity in the system    | Login, account         |

## Relationships

- An **Invoice** belongs to exactly one **Customer**
- An **Order** produces one or more **Invoices**

## Example dialogue

> **Dev:** "When a **Customer** places an **Order**, do we create the **Invoice** immediately?"
> **Domain expert:** "No — an **Invoice** is only generated once a **Fulfillment** is confirmed. A single **Order** can produce multiple **Invoices** if items ship in separate **Shipments**."
> **Dev:** "So if a **Shipment** is cancelled before dispatch, no **Invoice** exists for it?"
> **Domain expert:** "Exactly. The **Invoice** lifecycle is tied to the **Fulfillment**, not the **Order**."

## Flagged ambiguities

- "account" was used to mean both **Customer** and **User** — these are distinct concepts: a **Customer** places orders, while a **User** is an authentication identity that may or may not represent a **Customer**.
```

## 规则

- **要有明确倾向。** 当同一概念存在多个词时，选择最佳术语，并将其他词列为应避免的别名。
- **明确标记冲突。** 如果某个术语在对话中被歧义使用，请在“Flagged ambiguities”部分明确指出并给出清晰建议。
- **只包含对领域专家有意义的术语。** 除非模块名或类名在领域语言中有明确意义，否则跳过它们。
- **定义要简洁。** 最多一句话。定义它“是什么”，而不是“做什么”。
- **展示关系。** 使用加粗术语名，并在明显时表达基数关系。
- **只包含领域术语。** 跳过通用编程概念（array、function、endpoint），除非它们在该领域里有特定含义。
- **在自然聚类出现时分多张表展示术语。**（例如按子域、生命周期或参与者分组）。每组使用独立标题和表格。若所有术语属于单一一致领域，可只用一张表——不要强行分组。
- **编写示例对话。** 由开发者与领域专家进行 3-5 轮简短对话，展示术语如何自然互动。该对话应澄清相关概念边界，并展示术语的精确使用。

<example>

## 示例对话

> **Dev:** “如何在不使用 Docker 的情况下测试 **sync service**？”

> **Domain expert:** “提供 **filesystem layer** 而不是 **Docker layer**。它实现了同一个 **Sandbox service** 接口，但使用本地目录作为 **sandbox**。”

> **Dev:** “所以 **sync-in** 仍然会创建 **bundle** 并解包吗？”

> **Domain expert:** “完全正确。**sync service** 不知道它在与哪一层通信。它调用 `exec` 和 `copyIn`——而 **filesystem layer** 只是将它们作为本地 shell 命令执行。”

</example>

## 重新运行

在同一对话中再次调用时：

1. 读取现有的 `UBIQUITOUS_LANGUAGE.md`
2. 合并后续讨论中的新术语
3. 如果理解发生演进，更新定义
4. 重新标记任何新的歧义
5. 重写示例对话以纳入新术语
