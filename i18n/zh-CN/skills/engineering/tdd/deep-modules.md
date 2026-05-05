# 深层模块

来自《A Philosophy of Software Design》：

**深层模块** = 小接口 + 大量实现

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│                     │
│  Deep Implementation│  ← Complex logic hidden
│                     │
│                     │
└─────────────────────┘
```

**浅层模块** = 大接口 + 少量实现（避免）

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

在设计接口时，问自己：

- 我能减少方法数量吗？
- 我能简化参数吗？
- 我能在内部隐藏更多复杂性吗？
