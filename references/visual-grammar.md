# 可编译视觉图法契约

`SKILL.md` owns human routing from a source relationship to one grammar. This file is the compiler contract for the selected grammar only: `topology_prompt` and `must_visually_prove` become generation constraints; `forbidden_substitutions` prevents topology drift; `recommended_encodings` lists permissible readability encoding; and `directional_line_allowed: false` forbids directional lines that imply steps, causality, or flow. `visual_solution` may add article-specific objects, but never replace this structure.

<!-- smkt-grammar:architecture -->
```json
{"use_when":["组件、依赖、分支、合并或上下游关系"],"not_for":["纯时间步骤","父子分类"],"topology_prompt":"Make source-derived components, dependencies, branches, and convergence visibly legible as one system; do not imply time order or parent-child classification.","must_visually_prove":["components","relationships","branch or convergence when supported"],"forbidden_substitutions":["timeline","flow","hierarchy"],"recommended_encodings":["label","leader","connector"],"directional_line_allowed":false}
```

<!-- smkt-grammar:hierarchy -->
```json
{"use_when":["父子关系","类别与子类","整体与部分","组织层级"],"not_for":["条件选择","时间顺序","系统依赖"],"topology_prompt":"Make the source-supported parent-child, whole-part, or category-subcategory levels visibly distinct; do not turn the structure into conditions or a time sequence.","must_visually_prove":["levels","containment or parent-child relation"],"forbidden_substitutions":["decision tree","timeline","architecture"],"recommended_encodings":["label","leader"],"directional_line_allowed":false}
```

<!-- smkt-grammar:flow -->
```json
{"use_when":["有先后顺序的步骤","输入到输出"],"not_for":["没有顺序的并列概念"],"topology_prompt":"Make the source-supported ordered steps, state changes, or input-to-output movement legible in one direction; do not imply an ongoing feedback cycle.","must_visually_prove":["ordered states or steps","source-supported transition"],"forbidden_substitutions":["loop","timeline without real time","parallel concept map"],"recommended_encodings":["label","leader","connector","directional_line"],"directional_line_allowed":true}
```

<!-- smkt-grammar:loop -->
```json
{"use_when":["反馈","迭代","优化","约束","重复循环"],"not_for":["一次性路线"],"topology_prompt":"Make the source-supported feedback or repeated iteration visibly return to an earlier state; do not portray it as a one-way route.","must_visually_prove":["recurrence","feedback relationship"],"forbidden_substitutions":["one-way flow","timeline","decorative circular arrows"],"recommended_encodings":["label","leader","connector","directional_line"],"directional_line_allowed":true}
```

<!-- smkt-grammar:decision_tree -->
```json
{"use_when":["条件选择","如果／那么","分叉路径"],"not_for":["没有决策条件的组件依赖"],"topology_prompt":"Make each source-supported condition lead to visibly distinct branches or outcomes; do not invent decision conditions.","must_visually_prove":["condition","branch","outcome"],"forbidden_substitutions":["hierarchy","architecture","unconditional flow"],"recommended_encodings":["label","leader","connector","directional_line"],"directional_line_allowed":true}
```

<!-- smkt-grammar:comparison -->
```json
{"use_when":["两个或多个方案的差异和取舍"],"not_for":["单一过程"],"topology_prompt":"Make two or more source-supported alternatives visibly different even when labels are hidden; at least one difference must be object, position, connection, sequence, or boundary.","must_visually_prove":["two or more alternatives","visible structural difference"],"forbidden_substitutions":["single-process diagram","name-only comparison","generic chart"],"recommended_encodings":["label","leader","connector"],"directional_line_allowed":false}
```

<!-- smkt-grammar:matrix -->
```json
{"use_when":["两个独立维度下的分类","定位","术语区分"],"not_for":["单维分类","细致时间变化"],"topology_prompt":"Place source-derived items by two independent source-supported dimensions; do not use a matrix for a single-category list or detailed time change.","must_visually_prove":["two independent dimensions","meaningful placement"],"forbidden_substitutions":["hierarchy","timeline","single-axis continuum"],"recommended_encodings":["label","leader"],"directional_line_allowed":false}
```

<!-- smkt-grammar:overlap_map -->
```json
{"use_when":["共同部分","差异","交集","共存","冲突"],"not_for":["互斥选项","顺序过程"],"topology_prompt":"Make the source-supported shared area and distinct areas visibly legible; do not imply mutually exclusive options or a sequence.","must_visually_prove":["shared portion","distinct portions"],"forbidden_substitutions":["comparison with no overlap","flow","decision tree"],"recommended_encodings":["label","leader"],"directional_line_allowed":false}
```

<!-- smkt-grammar:boundary_map -->
```json
{"use_when":["什么属于","什么不属于","它不是什么"],"not_for":["操作步骤"],"topology_prompt":"Make what belongs inside, what remains outside, and the source-supported boundary between them visibly distinct; do not depict a temporal process.","must_visually_prove":["inside scope","outside scope","boundary"],"forbidden_substitutions":["flow","timeline","generic comparison"],"recommended_encodings":["label","leader"],"directional_line_allowed":false}
```

<!-- smkt-grammar:argument_map -->
```json
{"use_when":["已有主张","已陈述依据","限制","结论"],"not_for":["编造证据","无依据因果"],"topology_prompt":"Organize only source-supported claims, stated evidence, constraints, and conclusion relationships; do not invent evidence or causal proof.","must_visually_prove":["claim or conclusion","stated support or constraint"],"forbidden_substitutions":["fabricated evidence chart","unsupported causal flow","generic hierarchy"],"recommended_encodings":["label","leader","connector","note"],"directional_line_allowed":false}
```

<!-- smkt-grammar:timeline -->
```json
{"use_when":["历史","阶段","真实时间推进"],"not_for":["同时存在的系统结构"],"topology_prompt":"Make source-supported historical or staged time progression legible in chronological order; do not use it for simultaneously existing system structure.","must_visually_prove":["time order","source-supported stages or events"],"forbidden_substitutions":["flow without real time","continuum","architecture"],"recommended_encodings":["label","leader","connector","directional_line"],"directional_line_allowed":true}
```

<!-- smkt-grammar:continuum -->
```json
{"use_when":["渐进位置","成熟度","强度","非时间光谱"],"not_for":["真实时间进程"],"topology_prompt":"Place source-derived states on a non-temporal gradual spectrum of maturity, intensity, or position; do not imply time passing.","must_visually_prove":["ordered spectrum","non-temporal position"],"forbidden_substitutions":["timeline","flow","binary comparison"],"recommended_encodings":["label","leader"],"directional_line_allowed":false}
```

<!-- smkt-grammar:layer_stack -->
```json
{"use_when":["抽象层","系统层","包含关系"],"not_for":["密集方向依赖","父子分类"],"topology_prompt":"Make source-supported abstract, system, or containment layers visibly stacked while preserving each layer's role; do not turn it into dense directional dependencies or parent-child classification.","must_visually_prove":["layers","layer order or containment"],"forbidden_substitutions":["architecture","hierarchy","flow"],"recommended_encodings":["label","leader","connector"],"directional_line_allowed":false}
```
