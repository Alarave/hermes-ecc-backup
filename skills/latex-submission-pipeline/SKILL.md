---
name: latex-submission-pipeline
description: "Use when setting up LaTeX, LyX, or paper build pipelines."
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
---

# LaTeX Submission Pipeline（LaTeX 投稿工程链）

## 适用

当用户需要：
- 套用期刊/会议 LaTeX 模板（ACM/IEEE/NeurIPS 等）
- 解决编译错误、引用错误、字体缺失、图片格式不兼容
- 接入 GitHub Actions 自动编译 PDF / 打包 submission zip
- 做格式化（latexindent）与 lint（chktex）
- 搭建本地 LaTeX / LyX / MiKTeX 环境及配置 MCP LaTeX 工具链

---

## 最小流程（从 0 到可提交）

### 1) 选择模板与约束

先记录目标 venue 的官方模板或格式要求：
- 页边距、双栏/单栏、匿名/非匿名、附录策略、页数限制

### 2) 本地可复现构建

推荐统一入口（任选其一）：
- `latexmk -pdf -interaction=nonstopmode -halt-on-error`
- 或在项目中提供 `scripts/build.ps1` / `scripts/build.sh`

### 3) 引用稳定（BibTeX/Biber）

元规则：
- `.bib` 是 source-of-truth
- 同一项目不要混用手工引用与 BibTeX（至少主文统一）

### 4) 图表导出与兼容性

对投稿系统最稳的组合：
- 矢量：`PDF`（matplotlib 导出）
- 栅格：`TIFF 600dpi`（显微/照片/heatmap 视情况）

### 5) Lint + Format（可选但强烈建议）

- Lint：`chktex`（常见 LaTeX 坑）
- Format：`latexindent`（减少 diff 噪声）

### 6) CI 自动编译（GitHub Actions）

模板：`templates/github-actions-latex.yml`（参考 `xu-cheng/latex-action`）

### 7) Windows 本地环境搭建与排障（MiKTeX + LyX）

1. **安装 MiKTeX 并开启无头自动装包**：
   - 安装：`winget install --id MiKTeX.MiKTeX -e --silent --accept-package-agreements --accept-source-agreements`
   - 启用自动安装缺失宏包（避免 GUI 弹窗阻塞编译）：`initexmf --set-config-value [MPM]AutoInstall=1` 并执行 `miktex packages update-package-database`。
2. **静默安装 LyX 避免 UAC 提权阻塞**：
   - LyX 的 NSIS 安装包声明了 `highestAvailable` 权限。在标准非提权终端运行静默安装时会报权限取消错误。
   - 规则：必须先导出 `export __COMPAT_LAYER=RunAsInvoker`，再执行 `"/path/to/LyX-*-Installer-*-x64.exe" /S`。
3. **安装矢量字体支持（避免 Type 3 位图字体导致 PDF 模糊/无法提取文本）**：
   - 基础 MiKTeX 在 `T1` 编码下默认回退到 METAFONT 位图字体，导致生成的 PDF 模糊且文本提取报错（`NeedsOcrError`）。
   - 规则：必须安装 `cm-super` 宏包并重建字体映射表：`miktex packages install cm-super && initexmf --update-fndb && initexmf --mkmaps`。
4. **无头配置与验证 LyX**：
   - 将 MiKTeX 的 `miktex\bin\x64` 加入用户 `PATH` 及 `%APPDATA%\LyX<ver>\preferences` 的 `\path_prefix`。
   - 若安装后 `configure.py` 因超时中断，在 `%APPDATA%\LyX<ver>` 目录下手动补跑：`"$LyXDir/Python/python.exe" "$LyXDir/Resources/configure.py"` 即可快速完成 `textclass.lst` 与 `packages.lst` 生成。
   - 命令行验证导出 PDF：`LyX.exe -e pdf2 test.lyx`。
5. **接入 LaTeX & LyX Model Context Protocol (MCP)**：
   - 部署 `mcp-latex-server`（基于 FastMCP）：FastMCP 在 `mcp 2.x` 重命名/重构，运行 v1 服务脚本必须固定 `uv pip install "mcp<2" "pydantic>=2.0.0"`。
   - 注册至 Hermes 必须通过 CLI 管道自动确认：
     `echo "y" | hermes mcp add latex --command "<venv_python>" --env LATEX_SERVER_ALLOW_ALL=1 --args "<path_to_latex_server.py>"`
   - 启用 `compile_latex`（`.tex` 编译）与 `compile_lyx`（`.lyx` 导出 `pdf2/pdf4/pdf5`），实现 AI 对排版与编译的全自动化闭环。

---

## 常见失败点（速查）

- 图像格式：EPS/PDF/PNG/TIFF 混用导致编译失败（优先统一 PDF）
- 字体：投稿要求嵌入字体（PDF 检查），缺少 `cm-super` 会导致输出位图 Type 3 字体
- Overfull box：大量警告影响排版质量（需要在关键位置修）
- 参考文献缺字段：DOI/年份/期刊名缺失造成审稿人观感差
- NSIS 安装包静默执行挂起：未设 `__COMPAT_LAYER=RunAsInvoker` 触发隐式 UAC 拦截
