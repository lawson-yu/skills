# 语言

此技能所给每条建议的共享词汇。请严格使用这些术语——不要替换为 “component”、“service”、“API” 或 “boundary”。语言一致性正是核心目标。

## 术语

**Module**
任何具有 interface 和 implementation 的事物。刻意与规模无关——同样适用于函数、类、包，或跨层级切片。
_避免使用_：unit、component、service。

**Interface**
调用方为正确使用 module 必须了解的一切。包含类型签名，但也包括不变式、顺序约束、错误模式、必需配置与性能特征。
_避免使用_：API、signature（过于狭窄——它们只指类型层面的表面）。

**Implementation**
module 的内部——其代码主体。与 **Adapter** 不同：一个事物可以是小型 adapter 配大型 implementation（如 Postgres repo），也可以是大型 adapter 配小型 implementation（如内存 fake）。当讨论重点是接缝（seam）时用 “adapter”；否则用 “implementation”。

**Depth**
interface 层面的杠杆——调用方（或测试）每学会一个单位的 interface 所能驱动的行为量。若大量行为隐藏在小 interface 后，module 就是 **deep**。若 interface 几乎与 implementation 一样复杂，module 就是 **shallow**。

**Seam** _(来自 Michael Feathers)_
你可以在不编辑该处代码的情况下改变行为的位置。它是 module 的 interface 所在的 *位置*。将 seam 放在哪里本身就是设计决策，与其后放什么是不同问题。
_避免使用_：boundary（与 DDD 的 bounded context 语义重叠）。

**Adapter**
在 seam 处满足某个 interface 的具体事物。描述的是 *角色*（它填充了哪个槽位），而不是内容（它内部是什么）。

**Leverage**
调用方从 depth 获得的收益。每学会一个单位的 interface，获得更多能力。一次 implementation 的投入，可在 N 个调用点与 M 个测试中回收。

**Locality**
维护者从 depth 获得的收益。变更、缺陷、知识与验证集中在一个地方，而不是分散到调用方。

## 原则

- **Depth 是 interface 的属性，不是 implementation 的属性。** 一个 deep module 内部可以由小型、可 mock、可替换的部件组成——只是它们不属于 interface。module 可以有 **internal seams**（implementation 私有、供自身测试使用）以及位于 interface 的 **external seam**。
- **删除测试（deletion test）。** 设想删除这个 module。若复杂度随之消失，说明 module 没有隐藏任何复杂度（它只是透传层）。若复杂度在 N 个调用方中重新出现，说明 module 发挥了价值。
- **interface 就是测试表面。** 调用方与测试跨越的是同一 seam。若你想测试 *越过* interface，module 的形状很可能不对。
- **一个 adapter 代表假设性的 seam；两个 adapter 代表真实 seam。** 除非某些东西确实会在 seam 两侧变化，否则不要引入 seam。

## 关系

- 一个 **Module** 恰有一个 **Interface**（它呈现给调用方与测试的表面）。
- **Depth** 是 **Module** 的属性，相对于其 **Interface** 来度量。
- **Seam** 是 **Module** 的 **Interface** 所在之处。
- **Adapter** 位于 **Seam** 并满足该 **Interface**。
- **Depth** 为调用方带来 **Leverage**，为维护者带来 **Locality**。

## 被否定的表述方式

- **将 Depth 视为 implementation 行数与 interface 行数之比**（Ousterhout）：会激励在 implementation 中填充无效内容。我们改用“depth-as-leverage”。
- **将 “Interface” 视为 TypeScript 的 `interface` 关键字或某个类的 public methods**：过于狭窄——此处的 interface 包含调用方必须知道的每一个事实。
- **“Boundary”**：与 DDD 的 bounded context 语义重叠。请使用 **seam** 或 **interface**。
