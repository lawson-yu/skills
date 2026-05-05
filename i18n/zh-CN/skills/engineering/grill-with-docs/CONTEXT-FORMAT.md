# CONTEXT.md 格式

## 结构

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A concise description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account

## Relationships

- An **Order** produces one or more **Invoices**
- An **Invoice** belongs to exactly one **Customer**

## Example dialogue

> **Dev:** "When a **Customer** places an **Order**, do we create the **Invoice** immediately?"
> **Domain expert:** "No — an **Invoice** is only generated once a **Fulfillment** is confirmed."

## Flagged ambiguities

- "account" was used to mean both **Customer** and **User** — resolved: these are distinct concepts.
```

## 规则

- **要有明确立场。** 当同一概念存在多个词时，选择最佳术语，并将其他词列为应避免的别名。
- **明确标注冲突。** 如果术语使用存在歧义，在 “Flagged ambiguities” 中明确指出并给出清晰结论。
- **定义要简洁。** 最多一句话。定义它“是什么”，而不是“做什么”。
- **展示关系。** 使用加粗术语名，并在明显处表达基数关系。
- **仅包含该项目上下文特有的术语。** 通用编程概念（超时、错误类型、工具模式）即使在项目中大量使用也不应包含。添加术语前先问：这是该上下文独有概念，还是通用编程概念？只有前者应被包含。
- **当自然形成聚类时，按子标题分组术语。** 如果所有术语都属于单一且连贯的领域，使用平铺列表即可。
- **编写示例对话。** 通过开发者与领域专家的对话展示术语如何自然交互，并澄清相关概念之间的边界。

## 单上下文与多上下文仓库

**单上下文（大多数仓库）：** 在仓库根目录放置一个 `CONTEXT.md`。

**多上下文：** 在仓库根目录放置一个 `CONTEXT-MAP.md`，列出各个上下文、它们的位置，以及彼此关系：

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) — generates invoices and processes payments
- [Fulfillment](./src/fulfillment/CONTEXT.md) — manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

该技能会推断应使用哪种结构：

- 如果存在 `CONTEXT-MAP.md`，先读取它以定位上下文
- 如果只有根目录的 `CONTEXT.md`，则为单上下文
- 如果两者都不存在，则在首个术语被解析时惰性创建根目录 `CONTEXT.md`

当存在多个上下文时，推断当前主题关联哪一个；若不明确，则提问。
