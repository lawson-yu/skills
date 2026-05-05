---
name: migrate-to-shoehorn
description: 将测试文件从 `as` 类型断言迁移到 @total-typescript/shoehorn。当用户提到 shoehorn、想在测试中替换 `as`，或需要部分测试数据时使用。
---

# 迁移到 Shoehorn

## 为什么使用 shoehorn？

`shoehorn` 让你在测试中传入部分数据，同时保持 TypeScript 满意。它用类型安全的替代方案取代 `as` 断言。

**仅用于测试代码。** 永远不要在生产代码中使用 shoehorn。

测试中使用 `as` 的问题：

- 训练中会避免使用它
- 必须手动指定目标类型
- 对于故意错误的数据需要双重断言（`as unknown as Type`）

## 安装

```bash
npm i @total-typescript/shoehorn
```

## 迁移模式

### 只需要少量属性的大对象

Before:

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
  // ...20 more properties
};

it("gets user by id", () => {
  // Only care about body.id but must fake entire Request
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
    // ...fake all 20 properties
  });
});
```

After:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("gets user by id", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`

Before:

```ts
getUser({ body: { id: "123" } } as Request);
```

After:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`

Before:

```ts
getUser({ body: { id: 123 } } as unknown as Request); // wrong type on purpose
```

After:

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## 各自的使用场景

| Function        | Use case                                           |
| --------------- | -------------------------------------------------- |
| `fromPartial()` | 传入仍可通过类型检查的部分数据                     |
| `fromAny()`     | 传入故意错误的数据（保留自动补全）                 |
| `fromExact()`   | 强制完整对象（后续可与 fromPartial 互换）          |

## 工作流程

1. **收集需求** - 询问用户：
   - 哪些测试文件中的 `as` 断言导致了问题？
   - 他们是否在处理只关心部分属性的大对象？
   - 他们是否需要在错误测试中传入故意错误的数据？

2. **安装并迁移**：
   - [ ] 安装：`npm i @total-typescript/shoehorn`
   - [ ] 查找包含 `as` 断言的测试文件：`grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`
   - [ ] 将 `as Type` 替换为 `fromPartial()`
   - [ ] 将 `as unknown as Type` 替换为 `fromAny()`
   - [ ] 添加来自 `@total-typescript/shoehorn` 的导入
   - [ ] 运行类型检查以验证

```python
