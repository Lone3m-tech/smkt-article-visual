<p align="center">
  <img src="examples/readme-visuals/hero-banner.png" alt="smkt-article-visual 开场 Banner" width="100%">
</p>

<div align="center">

# smkt-article-visual

**把每个关键判断，讲成一张看得懂的图。**

把文章、演讲稿、报告、提案或工作坊提纲这类结构化叙事，变成**文章包**或一组连续的**演示画面**。它判断什么值得画，选择合适图法，并以 SimpleMkt 编辑图风格交付可追溯的图片包。

为 Codex 与具备生图能力的 Agent 而设计。

[SimpleMkt](https://simplemkt.cc) · [X](https://x.com/AlchemistZhou) · [小红书](https://www.xiaohongshu.com/user/profile/65a0ecb4000000002201219c) · [抖音](https://www.douyin.com/user/MS4wLjABAAAArV0uXvsSYl6pD-p5nr-5OFlZED5cEUnb7r2K6j9u4tA)

[查看完整 Demo](examples/demo-article/article.md) · [查看 Skill 运行契约](SKILL.md)

**[English](README.md) | 简体中文**

</div>

## 安装

把任一命令直接发给 Agent，或在终端运行。优先使用 `npx`；没有 `npx` 时使用 `git clone`。

### npx（推荐）

```bash
npx skills add Lone3m-tech/smkt-article-visual \
  --skill smkt-article-visual \
  --global \
  --agent codex \
  --copy
```

### git clone

```bash
mkdir -p ~/.codex/skills
git clone --depth 1 https://github.com/Lone3m-tech/smkt-article-visual.git \
  ~/.codex/skills/smkt-article-visual
```

项目内安装时去掉 `--global`；安装到 Claude Code 时把 `--agent codex` 改为 `--agent claude-code`，并将克隆目录改为 `~/.claude/skills/smkt-article-visual`。

## 运行环境与兼容性

- **主要验证宿主：**具备 `image_gen` 能力的 Codex。
- **必要能力：**Agent 能调用图像生成，并能读写本地文件。
- **图像模型：**由宿主运行环境选择；本 Skill 不固定某个图像模型。
- **其他 Agent：**安装可以成功，但完整生图仍需要等效的图像生成能力。

## 共同工作流程

无论选择哪种交付方式，都会经过这三个阶段；它们是工作流程，不是下方两种交付方式。

| 模式 | Skill 会做什么 | 此时不会做什么 |
| --- | --- | --- |
| `plan` | 找出读者或听众的理解卡点，选择一个主图法，明确必须保留的原文细节、落位与不该画的内容。 | 不生成图片，也不改写源文件。 |
| `generate` | 生成已确认的封面、正文图或讲述图；记录实际 Prompt 与每次调整；按确认锚点插入文章图片。 | 改写文章正文。 |
| `qa` | 检查解释是否成立、图法拓扑、字体层级、Logo 留白、事实备注、文件落位与 manifest 记录。 | 因为“图片已经生成”就视为完成。 |

正常顺序是 `plan → generate → qa`。如果用户明确要求直接生成，可以跳过方案确认，但仍会先形成一份配图判断再开始出图。

## 选择交付方式

读者会自行阅读内容时，选择 `article_package`；由你在现场、会议或课堂中带着听众讲述时，选择 `presentation_frames`。

| 判断问题 | `article_package` | `presentation_frames` |
| --- | --- | --- |
| 受众如何接收内容 | 边读文章或报告，边在对应段落查看图片。 | 跟随演讲、提案、工作坊或课程的叙事顺序观看。 |
| 图片单位 | 一张封面，再加多张正文解释图。 | 一张演示封面，再加 Frame 01、Frame 02、Frame 03……共同讲完一条叙事。 |
| 何时算交付完成 | 封面与正文图各自在 Markdown 的准确阅读锚点出现且只出现一次。 | 封面先出现一次，每张已确认画面再按 manifest 中的既定叙事顺序出现一次；源文件正文不被修改。 |
| 最适合的输入 | 完成的 Markdown 文章或报告。 | 演讲稿、提案提纲、工作坊或教学脚本。 |

![文章包与演示画面的两种交付方式](examples/readme-visuals/delivery-modes.png)

## 从文字判断到看得懂的图

当读者或听众需要理解一个流程、比较、层级、边界或关键判断时，一张好看的图还不够。Skill 从叙事本身出发：找出需要被解释的点，选择图法，生成图片，并把 Prompt、调整记录与 QA 收在同一份 manifest 中。

## 用在哪些场景

| 场景 | 输入 | 交付方式 | 它会交付什么 |
| --- | --- | --- | --- |
| 文章或报告 | 完成的 Markdown 文章或研究报告 | `article_package` | 在准确阅读锚点落位的封面与正文解释图。 |
| 演讲或分享 | 演讲稿或分享提纲 | `presentation_frames` | 一张演示封面，加上一组按顺序讲清关键判断的讲述图。 |
| 咨询提案 | 策略叙事或提案 | `presentation_frames` | 由封面带领的叙事画面序列，让机制、选项或建议更容易被讲清楚。 |
| 内部对齐 | 战略 memo 或项目复盘 | 取决于大家自行阅读，还是由人带着讲述 | 共同理解决策、边界、系统与交接关系的图。 |
| 工作坊或课程 | 教学提纲或课程脚本 | `presentation_frames` | 一张封面加一组可讲、可记的教学图，把抽象概念讲成完整关系。 |

![SMKT Article Visual 的五类使用场景](examples/readme-visuals/usage-scenarios.png)

## 它解释什么

| 阅读或讲述中的难点 | 它会做什么 |
| --- | --- |
| 一个流程读起来太绕 | 用流程图保留步骤、先后与交接关系。 |
| 两种做法不容易比较 | 用对比图把差异放到同一阅读路径里。 |
| 系统关系太抽象 | 用层级、边界或关系图保留结构。 |
| 图文或讲述脱节 | 让图片落在准确文章锚点，或把叙事交付成由封面带领、自洽完整的演示序列。 |

## 适合谁

- 希望让复杂判断更快被读者或听众理解的创作者与分享者。
- 需要稳定产出解释图的内容团队、咨询师、研究者与教育者。
- 已经有叙事观点，需要图片帮它解释，而不是重写内容的作者或演讲者。

## 不适合谁

- 没有解释任务、只追求氛围的海报、情绪图或社媒封面。
- 文章写作、发布、Logo 设计，或完整 PPTX / Deck 制作流程。
- 伪造截图、图表或事实证据。

![适用边界](examples/readme-visuals/audience-fit.png)

## 核心能力

### 先确认“这张图要解释什么”

不是每个标题或每段口述都强行配图。Skill 先生成 visual plan，明确读者或听众的卡点、图法、交付模式、落位或出场顺序，以及不该画的内容。

![生成前确认可视化计划](examples/demo-article/assets/image/plan-before-generation.png)

### 把叙事关系翻译成合适的图法

叙事结构决定要解释什么；图法决定流程、对比、层级或边界如何被看见；视觉方向负责让一组配图或一组讲述图读起来像同一个系列。

![内容、图法与编辑图母版](examples/demo-article/assets/image/content-grammar-style.png)

### 图像、落位与记录一起交付

文章模式会把每张图落在对应段落后；演讲和提案模式会先交付一张封面，再交付带明确叙事承接关系的独立画面序列。一份 manifest 记录每次生成、调整原因、Logo 结果、最终采用版本与稳定的封面/画面顺序；交付的是图片序列，不是 PPTX 文件。生成完成不等于交付完成，所选交付模式与 QA 通过才算结束。

![可追溯的配图交付](examples/demo-article/assets/image/traceable-delivery.png)

## 图法库

一张图只选一个主图法：先看读者或听众需要理解哪一种关系，再选结构，不让统一风格把不同问题画成同一种版式。

| 图法 | 示例 |
| --- | --- |
| Architecture（架构） | <img src="examples/visual-grammar/architecture.png" alt="Architecture 图法示例" width="520"> |
| Flow（流程） | <img src="examples/visual-grammar/flow.png" alt="Flow 图法示例" width="520"> |
| Loop（循环） | <img src="examples/visual-grammar/loop.png" alt="Loop 图法示例" width="520"> |
| Decision tree（决策树） | <img src="examples/visual-grammar/decision-tree.png" alt="Decision tree 图法示例" width="520"> |
| Comparison（对比） | <img src="examples/visual-grammar/comparison.png" alt="Comparison 图法示例" width="520"> |
| Matrix（矩阵） | <img src="examples/visual-grammar/matrix.png" alt="Matrix 图法示例" width="520"> |
| Overlap map（交集） | <img src="examples/visual-grammar/overlap-map.png" alt="Overlap map 图法示例" width="520"> |
| Boundary map（边界） | <img src="examples/visual-grammar/boundary-map.png" alt="Boundary map 图法示例" width="520"> |
| Argument map（论证） | <img src="examples/visual-grammar/argument-map.png" alt="Argument map 图法示例" width="520"> |
| Timeline（时间线） | <img src="examples/visual-grammar/timeline.png" alt="Timeline 图法示例" width="520"> |
| Continuum（连续谱） | <img src="examples/visual-grammar/continuum.png" alt="Continuum 图法示例" width="520"> |
| Layer stack（层级） | <img src="examples/visual-grammar/layer-stack.png" alt="Layer stack 图法示例" width="520"> |
| Annotated source（来源标注） | <img src="examples/visual-grammar/annotated-source.png" alt="Annotated source 图法示例" width="520"> |

## 完整 Demo

包内 Demo 展示的是 `article_package`：使用《开源配图Skill：配图不是装饰，而是解释的一部分》这篇文章，包含一张封面与六张正文解释图。

[打开 Demo 文章](examples/demo-article/article.md)

## 默认视觉风格

这一版包内的封面、正文图与讲述图共用一套编辑图视觉系统：保证一组图读起来像同一个系列，但不把不同关系硬画成同一种版式。

![字体层级示例](examples/readme-visuals/typography-hierarchy.png)

- **封面与正文图分工不同。** 封面是安静的 PPT 封面：文章 H1 原文保留，用一个主视觉隐喻承接。正文图负责解释：居中的核心判断、一句短解释、再到一个主关系结构。
- **字体有明确阅读顺序。** 正文标题小于封面标题，固定在顶部居中区域，不与右上角 Logo 留白竞争。中文使用同一款编辑感衬线字体；英文标识使用克制的搭配字体；语义文字不允许手写体。
- **元素先表达信息，再由标签补充。** 原文与主张使用摘录纸页，步骤与输出使用窄纸条，决策与边界使用裁切纸面，位置或变化使用墨线、排线或锚点。不能用空纸片加一个标签蒙混过关。
- **素描必须参与解释。** 版画感或铅笔素描只能从原文关系或具体细节生长出来，并由细引线与直接标注解释；不会默认画植物、泛化物体、图标或纯装饰隐喻。
- **完成感是编辑感，不是 UI 感。** 纯白画布、细而浅的关系线、统一且极轻的纸张悬浮、克制的品牌绿强调；不出现 Dashboard 卡片、粗箭头、装饰网格、裁切标记或悬浮装饰。
- **Logo 由程序确定落位。** 包内 Logo 在生图后放入固定白色保护区，模型不能自行生成 Logo，标题、标签和连线也不能进入这一区域。
- **风格同时保护解释与事实边界。** 不是每个标题都自动配图；一张图只回答一个核心问题，并选择一个主图法。文章正文保持不变，每张已确认图片只出现在对应锚点一次。非事实性示例会在左下角加上 `图中示例仅为解释用途，并非事实`；生成图绝不会被当作真实截图、来源或事实。

## License

本包采用 [MIT License](LICENSE) 开源。
