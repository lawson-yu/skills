---
name: setup-pre-commit
description: 在当前仓库中使用 lint-staged（Prettier）、类型检查和测试设置 Husky pre-commit hooks。用于用户希望添加 pre-commit hooks、设置 Husky、配置 lint-staged，或添加提交时格式化/类型检查/测试时。
---

# 设置 Pre-Commit Hooks

## 这会设置什么

- **Husky** pre-commit hook
- **lint-staged** 在所有已暂存文件上运行 Prettier
- **Prettier** 配置（若缺失）
- 在 pre-commit hook 中添加 **typecheck** 和 **test** 脚本

## 步骤

### 1. 检测包管理器

检查 `package-lock.json`（npm）、`pnpm-lock.yaml`（pnpm）、`yarn.lock`（yarn）、`bun.lockb`（bun）。使用存在的那个。若不明确，默认使用 npm。

### 2. 安装依赖

作为 devDependencies 安装：

```
husky lint-staged prettier
```

### 3. 初始化 Husky

```bash
npx husky init
```

这会创建 `.husky/` 目录，并在 package.json 中添加 `prepare: "husky"`。

### 4. 创建 `.husky/pre-commit`

写入此文件（Husky v9+ 不需要 shebang）：

```
npx lint-staged
npm run typecheck
npm run test
```

**适配**：将 `npm` 替换为检测到的包管理器。如果仓库的 package.json 中没有 `typecheck` 或 `test` 脚本，省略这些行并告知用户。

### 5. 创建 `.lintstagedrc`

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. 创建 `.prettierrc`（若缺失）

仅在不存在 Prettier 配置时创建。使用以下默认值：

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. 验证

- [ ] `.husky/pre-commit` 存在且可执行
- [ ] `.lintstagedrc` 存在
- [ ] package.json 中 `prepare` 脚本为 `"husky"`
- [ ] `prettier` 配置存在
- [ ] 运行 `npx lint-staged` 以验证其可正常工作

### 8. 提交

暂存所有已变更/新建文件，并使用以下信息提交：`Add pre-commit hooks (husky + lint-staged + prettier)`

这将跑一遍新的 pre-commit hooks——是一个很好的冒烟测试，用于确认一切正常工作。

## 说明

- Husky v9+ 在 hook 文件中不需要 shebang
- `prettier --ignore-unknown` 会跳过 Prettier 无法解析的文件（图片等）
- pre-commit 会先运行 lint-staged（快速、仅针对已暂存文件），然后再运行完整类型检查和测试
