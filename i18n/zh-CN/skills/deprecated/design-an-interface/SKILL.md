---
name: design-an-interface
description: 使用并行子代理为一个模块生成多个截然不同的接口设计。当用户希望设计 API、探索接口选项、比较模块形态，或提到“design it twice”时使用。
---

# 设计一个接口

基于《A Philosophy of Software Design》中的 “Design It Twice”：你的第一个想法很可能不是最好的。生成多个截然不同的设计，然后进行比较。

## 工作流

### 1. 收集需求

在开始设计之前，先理解：

- [ ] 这个模块要解决什么问题？
- [ ] 调用方是谁？（其他模块、外部用户、测试）
- [ ] 关键操作有哪些？
- [ ] 有哪些约束？（性能、兼容性、现有模式）
- [ ] 哪些内容应当隐藏在内部，哪些应当暴露出来？

提问：“这个模块需要做什么？谁会使用它？”

### 2. 生成设计（并行子代理）

使用 Task 工具同时启动 3 个以上子代理。每个子代理都必须产出一个**截然不同**的方法。

```
Prompt template for each sub-agent:

Design an interface for: [module description]

Requirements: [gathered requirements]

Constraints for this design: [assign a different constraint to each agent]
- Agent 1: "Minimize method count - aim for 1-3 methods max"
- Agent 2: "Maximize flexibility - support many use cases"
- Agent 3: "Optimize for the most common case"
- Agent 4: "Take inspiration from [specific paradigm/library]"

Output format:
1. Interface signature (types/methods)
2. Usage example (how caller uses it)
3. What this design hides internally
4. Trade-offs of this approach
```

### 3. 展示设计

对每个设计展示以下内容：

1. **接口签名** - types、methods、params
2. **使用示例** - 调用方在实践中如何实际使用它
3. **它隐藏了什么** - 保持在内部的复杂性

按顺序展示各个设计，让用户在比较之前先吸收每一种方法。

### 4. 比较设计

展示完所有设计后，从以下维度进行比较：

- **接口简洁性**：更少的方法、更简单的参数
- **通用型 vs 专用型**：灵活性与聚焦度
- **实现效率**：这种形态是否允许高效的内部实现？
- **深度**：小接口隐藏大量复杂性（好）vs 大接口配薄实现（坏）
- **正确使用的容易程度** vs **误用的容易程度**

用叙述性文字讨论权衡，不用表格。突出各设计分歧最大的地方。

### 5. 综合

通常最好的设计会结合多个方案的洞见。提问：

- “哪个设计最符合你的主要使用场景？”
- “其他设计中有没有值得吸收的元素？”

## 评估标准

来自《A Philosophy of Software Design》：

**接口简洁性**：方法更少、参数更简单 = 更容易学习并正确使用。

**通用性**：无需修改即可处理未来用例。但要警惕过度泛化。

**实现效率**：接口形态是否支持高效实现？还是会迫使内部实现变得别扭？

**深度**：小接口隐藏大量复杂性 = 深模块（好）。大接口配薄实现 = 浅模块（应避免）。

## 反模式

- 不要让子代理产出相似设计——要强制形成显著差异
- 不要跳过比较——价值在于对比
- 不要实现——这完全是关于接口形态
- 不要基于实现工作量进行评估
