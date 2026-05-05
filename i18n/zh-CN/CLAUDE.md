技能按 `skills/` 下的桶文件夹组织：

- `engineering/` — 日常代码工作
- `productivity/` — 日常非代码工作流工具
- `misc/` — 保留但很少使用
- `personal/` — 绑定到我自己的设置，不对外推广
- `deprecated/` — 不再使用

`engineering/`、`productivity/` 或 `misc/` 中的每个技能都必须在顶层 `README.md` 中有引用，并在 `.claude-plugin/plugin.json` 中有条目。`personal/` 和 `deprecated/` 中的技能不应出现在这两处中的任何一处。

顶层 `README.md` 中的每个技能条目都必须将技能名称链接到其 `SKILL.md`。

每个桶文件夹都有一个 `README.md`，其中列出该桶中的每个技能及其一行描述，并将技能名称链接到其 `SKILL.md`。
