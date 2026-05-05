---
name: git-guardrails-claude-code
description: 设置 Claude Code hooks，在危险的 git 命令（push、reset --hard、clean、branch -D 等）执行前进行拦截阻止。当用户希望防止破坏性 git 操作、添加 git 安全 hooks，或在 Claude Code 中阻止 git push/reset 时使用。
---

# 设置 Git Guardrails

设置一个 PreToolUse hook，在 Claude 执行危险 git 命令之前进行拦截并阻止。

## 会阻止什么

- `git push`（所有变体，包括 `--force`）
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

被阻止时，Claude 会看到一条消息，告知它无权访问这些命令。

## 步骤

### 1. 询问作用范围

询问用户：安装到**仅此项目**（`.claude/settings.json`）还是**所有项目**（`~/.claude/settings.json`）？

### 2. 复制 hook 脚本

打包脚本位于：[scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

根据作用范围复制到目标位置：

- **项目级**：`.claude/hooks/block-dangerous-git.sh`
- **全局级**：`~/.claude/hooks/block-dangerous-git.sh`

使用 `chmod +x` 赋予可执行权限。

### 3. 将 hook 添加到 settings

添加到对应的 settings 文件：

**项目级**（`.claude/settings.json`）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**全局级**（`~/.claude/settings.json`）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

如果 settings 文件已存在，把 hook 合并进已有的 `hooks.PreToolUse` 数组——不要覆盖其他设置。

### 4. 询问是否需要自定义

询问用户是否想在阻止列表中添加或移除任何模式。按需编辑复制后的脚本。

### 5. 验证

运行一个快速测试：

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

应当以退出码 2 退出，并向 stderr 打印一条 BLOCKED 消息。
