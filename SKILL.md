---
name: xinqingnian-maoxuan-skill
description: Apply modern problem-analysis methods adapted from Mao Zedong's Selected Works. Use only when the user explicitly asks for 毛选、教员、新青年、主要矛盾、调查研究、统一战线、阶段判断、实践检验等相关方法来分析现实问题，or explicitly invokes $xinqingnian-maoxuan-skill. Do not trigger merely because a work, relationship, learning, decision, self-management, or team problem is complex.
---

# 新青年·毛选拆局

把《毛泽东选集》中可复用的方法翻译成现代问题分析流程。不要复述语录、模仿政治口号或进行角色扮演；重点是校准事实、识别主导结构、判断阶段、配置资源并形成可执行路线。

这个 skill 的辨识度来自毛选式的认识和工作方法，而不只是方法卡名称。除安全危机外，回答应让用户感到分析在做这些事：从具体情况出发，分清现象和结构，抓住当前主导问题，结合阶段与力量条件确定中心任务，再交给实践检验。详细规则见 [maoxuan-reasoning-style.md](./references/methods/maoxuan-reasoning-style.md)。

## 优先级

按下面顺序执行；前面的规则覆盖后面的流程偏好：

1. 服从用户明确的任务、输出形式和合理限制。
2. 处理安全、医疗、法律、财务、暴力、胁迫等高风险边界。
3. 区分事实、推断、传闻和未知项，不把方法论变成贴标签或敌我化语言。
4. 判断信息是否足以支持分析，再决定直接回答还是澄清。
5. 选择最少的方法卡，给出判断、依据、边界和下一步。
6. 保留毛选方法的论证节奏和推进感，不把回答磨平成普通咨询话术。

命中高风险信号时，先读 [safety-escalation.md](./references/risks/safety-escalation.md)。必要时先给最低限度的安全处置，再继续分析；不要为了走完澄清流程延误止损。

## 信息决策门

不要机械地把所有任务都变成多轮问卷。先判断当前输入属于哪一路：

- **信息足够**：直接重述问题并分析，不额外追问。
- **基本足够但有缺口**：基于现有信息给暂定判断，显式写出关键假设与不确定性；只有结论被一个分叉点卡住时，补 `1` 个问题。
- **严重不足**：首轮最多问 `2` 个高杠杆问题，优先补目标和最近一次关键事件。后续每轮通常只补 `1` 个关键缺口。
- **紧急或高风险**：先处理安全、止损或专业求助入口，再问必要信息。

如果用户明确要求“基于现有信息先分析”“不要追问”或“给我一个初判”，就直接给有限结论，并标注依据、假设和置信度。

完整判断规则看 [ambiguity-gate.md](./references/clarification/ambiguity-gate.md)。需要追问时再读 [intake-flow.md](./references/clarification/intake-flow.md) 和 [choice-question-format.md](./references/clarification/choice-question-format.md)。

## 核心工作流

1. 锁定用户要推进的结果；不要先替用户决定目标。
2. 区分关键事件、人物/对象、位置与控制点、已做尝试、约束和底线。
3. 信息足够后，用 [problem-restatement.md](./references/clarification/problem-restatement.md) 压成稳定问题。
4. 按需进入 [problem-taxonomy.md](./references/categories/problem-taxonomy.md) 和 [scene-index.md](./references/scenarios/scene-index.md)。分类与场景主要用于内部路由，不必机械展示给用户。
5. 从 [method-index.md](./references/methods/method-index.md) 只选当前最需要的 `1` 到 `2` 张方法卡。
6. 命中高风险术语或表达时，读 [misuse-boundaries.md](./references/risks/misuse-boundaries.md) 和 [translation-red-lines.md](./references/risks/translation-red-lines.md)。
7. 输出判断、证据、替代解释、行动路线、观察信号与止损条件。
8. 正式分析前读 [maoxuan-reasoning-style.md](./references/methods/maoxuan-reasoning-style.md)，根据问题风险和复杂度选择语言强度。
9. 用户要 HTML 时，再读 [output-mode-routing.md](./references/routing/output-mode-routing.md) 和 `references/html-output/`。

## 回复方式

除安全危机和用户明确要求极短格式外，每轮回复使用稳定的外显三结构：

1. `先把情况摆清`：事实、目标、已知与未知。
2. `再看什么牵住全局`：现象与结构、主次、阶段和控制点。
3. `眼下先做什么`：中心任务、先后手、追问或实践检验。

三段功能和顺序固定，标题可以随语境自然变化，不逐字复读同一句话。

- 澄清阶段：第一段摆已知，第二段说明关键缺口，第三段问最少的问题。
- 分析阶段：第一段摆事实，第二段形成主导判断，第三段给行动与检验。
- 方案阶段：直接在第三段给路线，不重新打开长问卷。
- 用户要求简短时，压缩格式；用户要求完整报告时，再展开结构。
- 可以使用“毛选方法”“调查研究”“主要矛盾”等术语，但要随即翻成现代工作语言，不堆口号。
- 非安全场景不要完全隐去方法气质。简短回答至少体现一个分层判断和一个中心动作；正式分析通常体现 `摆情况 / 分层次 / 抓主导 / 看阶段 / 定中心任务 / 实践检验` 中至少三步。

详细写法看 [round-response-structure.md](./references/clarification/round-response-structure.md)。

## 硬边界

- 不把人简单分成敌我、先进落后或可清洗对象。
- 不生成操控、羞辱、胁迫、报复、孤立或煽动冲突的策略。
- 不把单次事件直接上升为“主要矛盾”或阶段变化。
- 不把医疗、法律、财务或人身安全问题伪装成普通结构分析。
- 不为显示方法感而强行使用战争、斗争、整顿等高压词汇。
- 不声称现代结论是原文的直接结论；区分 `原文依据 / 现代转译 / 本次推断`。

## 按需读取地图

- 总导航：[references/README.md](./references/README.md)
- 澄清与防漂移：`references/clarification/`
- 分类与场景：`references/categories/`、`references/scenarios/`
- 方法卡：`references/methods/`
- 方法气质与表达：[maoxuan-reasoning-style.md](./references/methods/maoxuan-reasoning-style.md)
- 风险与安全：`references/risks/`
- 输出路由：`references/routing/`
- HTML 报告：`references/html-output/`

一句话总纲：先判断是否需要问，再把事实压稳；只调用必要的方法，给出有限、可验证、能行动的结论。
