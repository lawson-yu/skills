---
name: tdd
description: 使用 red-green-refactor 循环进行测试驱动开发。当用户希望使用 TDD 构建功能或修复缺陷、提到 "red-green-refactor"、希望进行集成测试，或要求 test-first 开发时使用。
---

# 测试驱动开发

## 理念

**核心原则**：测试应通过公共接口验证行为，而非实现细节。代码可以完全改变；测试不应改变。

**好的测试**是集成风格的：它们通过公共 API 走真实代码路径。它们描述系统做了_什么_，而不是_如何_做。一个好的测试读起来像规范——“user can checkout with valid cart”能准确说明系统具备什么能力。这类测试能在重构后继续有效，因为它们不关心内部结构。

**坏的测试**与实现耦合。它们 mock 内部协作者、测试私有方法，或通过外部手段验证（例如直接查询数据库而不是使用接口）。警示信号是：当你重构时测试失败，但行为并未变化。如果你重命名了一个内部函数而测试失败，这些测试测试的是实现，而不是行为。

参见 [tests.md](tests.md) 获取示例，参见 [mocking.md](mocking.md) 获取 mocking 指南。

## 反模式：水平切片

**不要先把所有测试写完，再写所有实现。**这叫“水平切片”——把 RED 当成“写完所有测试”，把 GREEN 当成“写完所有代码”。

这会产生**糟糕测试**：

- 批量写出的测试测试的是_想象中的_行为，而不是_真实的_行为
- 你最终测试的是事物的_形状_（数据结构、函数签名），而不是面向用户的行为
- 测试会对真实变化不敏感——行为坏了却通过，行为正常却失败
- 你会超前承诺测试结构，在真正理解实现之前就被其束缚

**正确做法**：用 tracer bullet 做垂直切片。一个测试 → 一个实现 → 重复。每个测试都基于你在上个循环中学到的东西。因为你刚写过代码，你会清楚到底什么行为重要，以及如何验证它。

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

## 工作流

### 1. 规划

在探索代码库时，使用项目的领域术语表，使测试名称和接口词汇与项目语言一致，并遵守你所触达区域的 ADR。

在编写任何代码之前：

- [ ] 与用户确认需要哪些接口变更
- [ ] 与用户确认要测试哪些行为（按优先级）
- [ ] 识别 [deep modules](deep-modules.md) 机会（小接口、深实现）
- [ ] 为 [testability](interface-design.md) 设计接口
- [ ] 列出要测试的行为（而非实现步骤）
- [ ] 让用户批准计划

询问：“公共接口应该是什么样？哪些行为最值得优先测试？”

**你不可能测试一切。**与用户明确确认哪些行为最重要。将测试精力集中在关键路径和复杂逻辑，而不是所有可能的边界情况。

### 2. Tracer Bullet

编写**一个**测试，确认系统中的**一件**事：

```
RED:   Write test for first behavior → test fails
GREEN: Write minimal code to pass → test passes
```

这是你的 tracer bullet——证明整条路径端到端可用。

### 3. 增量循环

对每个剩余行为：

```
RED:   Write next test → fails
GREEN: Minimal code to pass → passes
```

规则：

- 一次只写一个测试
- 只写足够通过当前测试的代码
- 不要预判未来测试
- 让测试聚焦于可观察行为

### 4. 重构

当所有测试通过后，寻找 [refactor candidates](refactoring.md)：

- [ ] 提取重复
- [ ] 加深模块（把复杂性移到简洁接口之后）
- [ ] 在自然处应用 SOLID 原则
- [ ] 思考新代码揭示了哪些既有代码问题
- [ ] 每一步重构后都运行测试

**RED 状态下永不重构。**先到 GREEN。

## 每轮检查清单

```
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] Code is minimal for this test
[ ] No speculative features added
```
