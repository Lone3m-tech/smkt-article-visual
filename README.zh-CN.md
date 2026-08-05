# SMKT Article Visual

> 让文章里的每一张图，都在解释，而不是装饰。

[English](README.md)

把一篇完成或接近完成的 Markdown 文章，变成一组真正服务阅读的封面与正文解释图。

![《开源配图Skill：配图不是装饰，而是解释的一部分》封面](examples/demo-article/assets/image/cover.png)

[查看完整 Demo](examples/demo-article/article.md) · [查看 Skill 运行契约](SKILL.md)

## 配图不是最后五分钟的装饰工作

当文章需要解释流程、比较、层级、边界或一个关键判断时，单靠一张“好看”的图不够。SMKT Article Visual 从文章本身出发，判断哪里值得画、应该用什么图法、图应放在哪一段之后；再生成、落位，并将每张图的 Prompt、调整记录与检查结果收在同一份 manifest 中。

## 适合谁

- 用 Markdown 写长文、希望读者更容易看懂复杂判断的个人创作者。
- 需要稳定输出图文内容的内容团队、顾问与研究者。
- 已有文章逻辑，希望补齐解释图而不是重写文章的人。

## 不适合谁

- 只需要一张独立海报、氛围图或社交媒体封面的任务。
- 需要写文章、发布文章、制作 Logo 或整套 Deck 的任务。
- 需要伪造截图、图表或事实证据的任务。

![SMKT Article Visual 的适用与不适用边界](examples/readme-visuals/audience-fit.png)

## 用在哪些场景

| 文章里的难点 | 它会做什么 |
| --- | --- |
| 一个流程读起来太绕 | 用流程图保留步骤、先后与交接关系。 |
| 两种做法不容易比较 | 用对比图把差异放到同一阅读路径里。 |
| 系统关系太抽象 | 用层级、边界或关系图保留结构。 |
| 一篇文章图文脱节 | 让图片紧跟它解释的段落，并检查最终落位。 |

![SMKT Article Visual 的四类使用场景](examples/readme-visuals/usage-scenarios.png)

## 图法库

一张正文图只选一个主图法：先看读者需要理解哪一种关系，再选结构，不让统一风格把不同问题画成同一种版式。每种图法直接展示对应示例。

| 图法 | 示例 |
| --- | --- |
| Architecture（架构） | <img src="examples/visual-grammar/architecture.png" alt="Architecture 图法示例" width="280"> |
| Flow（流程） | <img src="examples/visual-grammar/flow.png" alt="Flow 图法示例" width="280"> |
| Loop（循环） | <img src="examples/visual-grammar/loop.png" alt="Loop 图法示例" width="280"> |
| Decision tree（决策树） | <img src="examples/visual-grammar/decision-tree.png" alt="Decision tree 图法示例" width="280"> |
| Comparison（对比） | <img src="examples/visual-grammar/comparison.png" alt="Comparison 图法示例" width="280"> |
| Matrix（矩阵） | <img src="examples/visual-grammar/matrix.png" alt="Matrix 图法示例" width="280"> |
| Overlap map（交集） | <img src="examples/visual-grammar/overlap-map.png" alt="Overlap map 图法示例" width="280"> |
| Boundary map（边界） | <img src="examples/visual-grammar/boundary-map.png" alt="Boundary map 图法示例" width="280"> |
| Argument map（论证） | <img src="examples/visual-grammar/argument-map.png" alt="Argument map 图法示例" width="280"> |
| Timeline（时间线） | <img src="examples/visual-grammar/timeline.png" alt="Timeline 图法示例" width="280"> |
| Continuum（连续谱） | <img src="examples/visual-grammar/continuum.png" alt="Continuum 图法示例" width="280"> |
| Layer stack（层级） | <img src="examples/visual-grammar/layer-stack.png" alt="Layer stack 图法示例" width="280"> |
| Annotated source（来源标注） | <img src="examples/visual-grammar/annotated-source.png" alt="Annotated source 图法示例" width="280"> |

## 核心能力

### 先确认“这张图要解释什么”

不是每个标题都强行配图。Skill 先生成 visual plan，明确读者卡点、图法、位置与不该画的内容。

![生成前确认可视化计划](examples/demo-article/assets/image/plan-before-generation.png)

### 把内容关系翻译成合适的图法

文章结构决定要解释什么；图法决定流程、对比、层级或边界如何被看见；视觉方向负责让整组内容读起来像同一个系列。

![内容、图法与编辑图母版](examples/demo-article/assets/image/content-grammar-style.png)

### 图像、位置与记录一起交付

每张图会落到文章的对应段落后；一份 manifest 会记录每次生成、调整原因、Logo 结果与最终采用版本。生成完成不等于交付完成，落位与 QA 通过才算结束。

![可追溯的配图交付](examples/demo-article/assets/image/traceable-delivery.png)

## 安装

本包已发布至 `Lone3m-tech/smkt-article-visual`，提供两种等价的安装方式。

### 方式一：npx 一次性安装（推荐）

```bash
npx skills add Lone3m-tech/smkt-article-visual \
  --skill smkt-article-visual \
  --global \
  --agent codex \
  --copy
```

这条命令不会把本 Skill 当作 Node 运行时依赖安装到 `node_modules`。`npx` 只在本次执行时下载并运行 `skills` 安装器；安装器再从 GitHub 取得完整 Skill 包（`SKILL.md`、`assets/`、`references/`、`scripts/` 与示例），并以副本形式放入 Codex 的全局 Skill 目录。

优点是无需手动找目录、无需全局安装安装器，并能明确选择目标宿主。项目内安装时去掉 `--global`；安装到 Claude Code 时把 `--agent codex` 改为 `--agent claude-code`。

### 方式二：git clone 后手动放置

```bash
git clone --depth 1 https://github.com/Lone3m-tech/smkt-article-visual.git
mkdir -p ~/.codex/skills
cp -R smkt-article-visual ~/.codex/skills/smkt-article-visual
```

这条路径下载的是仓库的完整 Git 工作副本。它适合希望先逐文件审查内容、没有 Node/npx 环境，或需要先切换到指定 release tag 的用户。使用正式版本时，先在克隆目录执行 `git checkout <release-tag>`，再复制；更新也由用户明确拉取和替换，不会隐式升级。

## 开始使用

安装后，在支持本地 Markdown 读写与 `image_gen` 的 Agent 宿主中，提供文章路径：

```yaml
article_path: ./article.md
mode: plan
```

先查看 visual plan；确认后使用 `mode: generate`。如果已经明确要直接生成，也可以在请求中说明。

## 你会得到什么

```text
article.md
assets/image/
├── cover.png
├── <figure-id>.png
└── manifest.json
```

`manifest.json` 为每张图追加生成尝试；`accepted_attempt` 指向当前采用版本。Skill 只新增图片 Markdown 引用，不改写文章正文。

## 完整 Demo

Demo 使用《开源配图Skill：配图不是装饰，而是解释的一部分》这篇文章，包含一张封面与六张正文解释图。

[打开 Demo 文章](examples/demo-article/article.md)

## 默认视觉方向与边界

默认使用 SimpleMkt 编辑图风格：纯白画布、清晰的标题层级、细线关系、克制材质与统一 Logo。它不把生成图当作真实截图或事实证据；非事实示例会使用明确备注。

## License

本包采用 [MIT License](LICENSE) 开源。
