<p align="center">
  <img src="examples/readme-visuals/hero-banner.png" alt="smkt-article-visual 开场 Banner" width="100%">
</p>

<div align="center">

# smkt-article-visual

**把叙事里的关键判断，变成一眼看懂、能继续讲下去的图片。**

把文章、演讲稿、报告、提案或工作坊提纲这类结构化叙事，变成一套统一的封面与内容图系统。它不从一条孤立的视觉 Prompt 开始，而是先把原文原意编译成配图判断，选择合适图法，再以 SimpleMkt 编辑图风格交付可追溯的图片包。`article_package` 把内容图放在读者需要理解的位置；`presentation_frames` 则用同一套图片系统组织连续讲述。

为 Codex 与具备生图能力的 Agent 而设计。

[SimpleMkt](https://simplemkt.cc) · [X](https://x.com/AlchemistZhou) · [小红书](https://www.xiaohongshu.com/user/profile/65a0ecb4000000002201219c) · [抖音](https://www.douyin.com/user/MS4wLjABAAAArV0uXvsSYl6pD-p5nr-5OFlZED5cEUnb7r2K6j9u4tA)

[官方仓库](https://github.com/Lone3m-tech/smkt-article-visual) · [版本发布](https://github.com/Lone3m-tech/smkt-article-visual/releases)

[查看 Demo 源文](examples/demo-article/article.md) · [查看 Skill 运行契约](SKILL.md)

**[English](README.md) | 简体中文**

</div>

## 为什么是这个 Skill

| 产品亮点 | 落到实际使用中 |
| --- | --- |
| **先判断，再出图** | 先找真正的理解卡点，选择一个主图法，并明确哪些原文细节必须在图中保留，再开始生成。 |
| **一套图片系统，两种生成策略** | 共用一套封面模板与内容图模板。`article_package` 服务局部阅读理解；`presentation_frames` 把经过筛选的原文叙事切片组织成连续讲述。 |
| **图片参与解释，不只是装饰** | 用同一套纸张素描语言，把原文中的对象、动作、状态、位置和关系可视化出来。一张内容图只回答一个核心问题，不填充正文旁的空白。 |
| **可用，也可复盘** | 文章图片会落在确认过的段落锚点；Prompt 与调整会记录在同一份 manifest；Logo 稳定落位；需要时可开启基础 QA，但会增加一些耗时与 token。 |

![四个产品亮点：先判断再出图、一套图片系统两种交付、图片参与解释、可用也可复盘](examples/readme-visuals/core-advantages.png)

共同目的很简单：降低读者或听众的认知负担，让内容生产者更清楚地输出叙事中原本就存在的信息。

## 不只是普通生图 Skill

普通生图工作流通常从一条视觉简报开始，以一张图片文件结束。这个 Skill 从读者或听众必须理解的原文关系开始；只有当图片落在需要它的位置、或进入应有的讲述顺序，并留下可追溯记录时，才算完成交付。

| | 普通生图工作流 | smkt-article-visual |
| --- | --- | --- |
| 起点 | 一个画面想法或一条孤立 Prompt | 被原文锁定的理解卡点或叙事节拍 |
| 图片结构 | 围绕单张图片本身选择构图 | 用一个主图法把原文关系画清楚 |
| 交付 | 一张生成的图片文件 | 封面与内容图、准确落位或叙事顺序，以及一份 manifest |
| 可控性 | 品牌处理与复核依赖每次单独写 Prompt | 固定的 Logo 后置覆盖、示例事实提示与可选的只报告 QA |

这个差异让它适合承担完整内容中的解释任务，而不只是让一张图片单独看起来完成了。

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
- **运行边界：**这是由 Agent 执行的包，不是一个仅在浏览器上传图即可运行的工具；完整交付需要能读取源 Markdown，也需要可写入的本地输出目录。

## 共同工作流程

无论选择哪种交付方式，都会经过这三个阶段；它们是工作流程，不是下方两种交付方式。

| 模式 | Skill 会做什么 | 此时不会做什么 |
| --- | --- | --- |
| `plan` | 找出读者或听众的理解卡点，选择一个主图法，明确必须保留的原文细节，以及图片落位或叙事顺序。 | 不生成图片，也不改写源文件。 |
| `generate` | 生成封面与内容图；记录实际 Prompt 与每次调整；按确认锚点插入文章内容图。 | 改写文章正文。 |
| `qa` | 执行可选的基础检查：原文与图法是否一致、版式、Logo 最终处理与交付记录。 | 重新审判内容元素选择或改写生成简报。 |

正常顺序是 `plan → generate`。`enable_logo: true` 默认开启，会在生图后贴上包内 Logo；设为 `false` 时只是不贴 Logo，画面版式保持不变。需要生成后基础检查时，设置 `enable_qa: true`；它可能增加复核耗时与 token，但不会自动重做图片。若用户明确要求直接生成，可以跳过方案确认，但仍会先形成一份配图判断再开始出图。

### 可选的基础 QA

`enable_logo: true` 默认开启，会在生图后用固定脚本精确贴上包内 Logo；`enable_logo: false` 只跳过最后的 Logo 覆盖，仍保留相同的右上角安全区，也不允许模型自行生成字标。`enable_qa: false` 是默认值：生图成功后只完成确定性的最终处理、落位与记录，并在 manifest 记录 `qa.status: skipped`；不会基于画面、内容、文字密度、风格或语义自行拒绝、重试或重做图片。只有希望得到原文与图法、版式、Logo 处理与交付记录的检查报告时，才设置 `enable_qa: true`；它可能额外消耗时间与 token，但不会自动重试或重做图片。生成前的 Prompt 已锁定原文原意、图法、内容密度、示例备注与视觉契约；QA 不在生成后重新审判这些选择。

## 选择交付方式

两种方式共用一套封面模板与内容图模板，目的都是降低理解负担，让原文信息更容易被读懂；生成策略则不同。读者会自行阅读内容时，选择 `article_package`；由你在现场、会议或课堂中带着听众讲述一条完整论述时，选择 `presentation_frames`。

| 判断问题 | `article_package` | `presentation_frames` |
| --- | --- | --- |
| 常见触发说法 | “给这篇文章加封面和正文图”“把图片插回文章”。 | “把文章或演讲稿做成图片式 PPT”“生成连续讲述图”“做一套可以讲的画面”。 |
| 受众如何接收内容 | 边读文章或报告，边在对应段落查看图片。 | 跟随演讲、提案、工作坊或课程的叙事顺序观看。 |
| 图片单位 | 一张统一风格的封面，再加多张落在文章中的正文解释图。 | 一张统一风格的封面，再加同类内容图组成 Frame 01、Frame 02、Frame 03……共同讲完一条叙事。 |
| 生成策略 | 从一个具体段落出发，卸载该段的局部理解卡点，保留原文细节，避免重复读者刚读过的内容。 | 从一个叙事切片出发，承担开场、张力、机制、重构或收束，并在独立投放时也看得懂、能承接下一张。 |
| 何时算交付完成 | 封面与正文图各自在 Markdown 的准确阅读锚点出现且只出现一次。 | 封面先出现一次，每张已确认画面再按 manifest 中的既定叙事顺序出现一次；源文件正文不被修改。 |
| 最适合的输入 | 带 H1 标题的完整 Markdown 文章或报告。 | 演讲稿、提案提纲、工作坊或教学脚本；没有 H1 时提供演示标题。 |

![文章包与演示画面的两种交付方式](examples/readme-visuals/delivery-modes.png)

差异从生成前就开始：文章模式关注内容图是否在恰当的阅读时刻解决局部卡点；演示模式关注内容图能否连续承接讲述。视觉模板保持一致，但两种模式不会默认选择同一组图、同一原文范围、同一判断角度、同一信息密度或同一构图。 同一份源文件若已经有文章包，请为演示模式设置 `presentation_output_root`，让顺序图片与 manifest 独立保存。

## 从文字判断到看得懂的图

当读者或听众需要理解一个流程、比较、层级、边界或关键判断时，一张好看的图还不够。Skill 把叙事中原本存在的关系，而不是一条装饰性的画面方向，变成读者或听众能跟上的图。

## 用在哪些场景

| 场景 | 输入 | 交付方式 | 它会交付什么 |
| --- | --- | --- | --- |
| 文章或报告 | 带 H1 标题的完整 Markdown 文章或研究报告 | `article_package` | 在准确阅读锚点落位的封面与正文解释图。 |
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

不是每个标题或每段口述都强行配图。Skill 先生成 visual plan，明确读者或听众的卡点、图法、交付方式、落位或出场顺序，以及必须保留的原文细节。

### 把叙事关系翻译成合适的图法

叙事结构决定要解释什么；图法决定流程、对比、层级或边界如何被看见；视觉方向负责让一组配图或一组讲述图读起来像同一个系列。

### 图像、落位与记录一起交付

文章模式会把每张内容图落在对应段落后；演讲和提案模式会先交付一张封面，再交付带明确叙事承接关系的同类内容图序列。一份 manifest 记录实际 Prompt、每次调整原因、最终采用版本、确定性的 Logo 处理结果、QA 状态，以及准确的文章锚点或叙事顺序；交付的是图片序列，不是 PPTX 文件。完成生成、最终处理和落位即构成交付；需要基础输出检查时可额外开启 QA。

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

## Demo 交付包

包内 Demo 源文是《开源配图Skill：配图不是装饰，而是解释的一部分》。同一份源文已完成两种交付：文章包包含封面与 5 张准确落位的正文解释图；演示包包含封面与 7 张按叙事顺序组织的讲述图。

[打开 Demo 文章](examples/demo-article/article.md) · [查看文章包 manifest](examples/demo-article/assets/image/manifest.json) · [查看演示包 manifest](examples/demo-presentation/assets/image/manifest.json)

## 默认视觉风格

这一版包内的两种交付方式共用一套封面模板与一套内容图模板：保证一组图读起来像同一个系列，但不把不同关系硬画成同一种版式。图片角色与图法决定共同的视觉语言；交付方式决定每张图生成时使用的原文范围与判断角度。

![字体层级示例](examples/readme-visuals/typography-hierarchy.png)

- **封面与内容图分工不同。** 封面是安静的 PPT 封面：文章 H1 原文保留，用一个简洁的视觉方向承接——可以是形象生动的隐喻，也可以是克制的抽象构图。内容图无论作为文章正文图还是演示讲述图，都遵循同一套解释模板：居中的核心判断、一句短解释、再到一个主关系结构。
- **字体有明确阅读顺序。** 内容图标题小于封面标题，固定在顶部居中区域，不与右上角 Logo 留白竞争。中文使用同一款编辑感衬线字体；英文标识使用克制的搭配字体；语义文字不允许手写体。
- **元素先表达信息，再由标签补充。** 每个核心角色都要用统一的纸张素描语言，直接呈现原文中的对象、动作、状态、位置或关系。只有当文字或文稿本身参与解释时才使用摘录纸页；不能用空纸片加一个标签蒙混过关。
- **图法组织关系，原文原意提供内容。** 一个主图法保证关系清晰，再用与原文相关的铅笔、版画、墨线、纸面、排线和锚点细节把意思画具体。无需强制增加独立素描主体或隐喻。
- **完成感是编辑感，不是 UI 感。** 纯白画布、细而浅的关系线，只在语义纸面上保留轻微纸张质感，默认无阴影，克制使用品牌绿；不出现 Dashboard 卡片、粗箭头、装饰网格、裁切标记或悬浮装饰。
- **Logo 区域固定，覆盖可选。** 每张图都保留右上角固定覆盖区：普通画布在下方自然延续，标题、标签、连线和关键内容不得进入这一区域。`enable_logo: true` 时包内 Logo 会在生图后精确覆盖；设为 `false` 时保留同一版式，只是不贴 Logo。
- **风格同时保护解释与事实边界。** 不是每个标题都自动配图；一张图只回答一个核心问题，并选择一个主图法。文章正文保持不变，每张已确认图片只出现在对应锚点一次。非事实性示例会在左下角加上 `图中示例仅为解释用途，并非事实`；生成图绝不会被当作真实截图、来源或事实。

## License

本包采用 [MIT License](LICENSE) 开源。
