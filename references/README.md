# References 协同地图

这个目录不是资料堆，而是这个 skill 的公开规则地图。

它只负责三件事：

- 说明默认主链怎么走
- 说明每一层只负责什么、不负责什么
- 说明每一层的最小产出和默认交接方向

如果 `SKILL.md` 是总入口，这里就是总导航。  
以后新增细规则，优先写进对应层，不要再把 `SKILL.md` 继续写成一整本操作手册。

## 默认主链

`clarification -> categories -> scenarios -> methods -> risks -> routing -> html-output`

理解方式：

- `clarification / categories / scenarios / methods` 是主链
- `risks / routing` 是例外层，只在命中条件时进入
- `html-output` 只负责最终呈现，不回头改写前面的判断

## 我先从哪里开始

默认按下面顺序进入：

1. 先看 [ambiguity-gate.md](./clarification/ambiguity-gate.md)，确认当前还缺哪些关键结构
2. 需要澄清时，再看 [intake-flow.md](./clarification/intake-flow.md) 和 [choice-question-format.md](./clarification/choice-question-format.md)
3. 如果某类结构缺口已经很明显，再按需借 [question-packs-by-domain.md](./clarification/question-packs-by-domain.md) 继续补结构；这只是 `临时追问入口`，不等于正式分类
4. 问题偏长、偏复杂或多问并行时，再补 [focus-anchor.md](./clarification/focus-anchor.md)
5. 澄清基本闭合后，看 [problem-restatement.md](./clarification/problem-restatement.md)
6. 然后进 [problem-taxonomy.md](./categories/problem-taxonomy.md) 做分类
7. 再进 [scene-index.md](./scenarios/scene-index.md) 选现实入口
8. 再进 [method-index.md](./methods/method-index.md) 选当前最早缺失的方法卡
9. 命中高风险表达或翻译风险时，再进 [misuse-boundaries.md](./risks/misuse-boundaries.md) 和 [translation-red-lines.md](./risks/translation-red-lines.md)
10. 分类、方法、风险或输出形式拿不准时，再进 [confidence-rules.md](./routing/confidence-rules.md)
11. 正式交付前，再进 [output-mode-routing.md](./routing/output-mode-routing.md)
12. 只有用户明确要 `HTML 报告` 时，才进入 [visual-report-spec.md](./html-output/visual-report-spec.md)

回复格式另外参考：

- [round-response-structure.md](./clarification/round-response-structure.md)

## 每轮回复骨架

不管当前是在澄清、分析还是准备交付，每一轮回复默认都使用同一套三段骨架：

- `背景信息`：沉淀本轮之前已经确认的结构
- `主体结构`：澄清时缩小不确定性，分析时展开当前最需要的结构判断
- `当前进度`：写清当前阶段、当前关注和下一步

补充规则：

- 场景和方法路由默认留在内部，不作为每轮固定外显字段
- 不要让 `当前进度` 压过 `主体结构`
- 提问负载随阶段下降：澄清阶段少量高杠杆提问，分析阶段默认不再追问，方案阶段默认直接给路线

完整规则看 [round-response-structure.md](./clarification/round-response-structure.md)。

## 各层只负责什么

### `clarification/`

负责：

- 判断还缺哪些关键结构
- 分轮澄清
- 必要时临时借追问包补结构
- 把问题重述成稳定版本
- 长问题防漂移

不负责：

- 正式分析
- 正式主领域分类
- 具体方法卡判断
- 正式输出形式

最小产出：

- `目标`
- `关键事件 / 关键事件链`
- `关键人物 / 对象`
- `关键控制点 / 已做尝试 / 约束`
- `问题重述`
- 长问题时补 `主问题锚点 / 原始问题对照 / 案件工作单`

默认交给：

- [problem-taxonomy.md](./categories/problem-taxonomy.md)

### `categories/`

负责：

- 产出稳定分类字段
- 判断主领域
- 判断方法标签
- 判断复杂度

不负责：

- 回头重做澄清
- 替代场景层
- 直接展开方法分析

最小产出：

```text
主领域：
次领域：
方法标签：
复杂度：
优先适用场景：
边界提示：
```

默认交给：

- [scene-index.md](./scenarios/scene-index.md)

### `scenarios/`

负责：

- 选主场景入口
- 给出更顺的现实进入角度
- 提示优先看哪 `1` 到 `3` 张方法卡

不负责：

- 重做澄清
- 替代方法卡正文
- 提前决定输出形式

最小产出：

- `主场景入口`
- `补充场景（如有）`
- `优先方法卡`

默认交给：

- [method-index.md](./methods/method-index.md)

### `methods/`

负责：

- 从当前最早缺失的一张卡起手
- 形成核心判断
- 决定下一张该接哪张卡

不负责：

- 把前门没完成的工作硬跳过去
- 常驻处理风险与输出
- 直接把方法卡正文当最终成品

最小产出：

- `当前最关键判断`
- `为什么从这张卡起手`
- `下一步接哪张卡`

默认交给：

- 命中风险时交给 `risks/`
- 内容判断稳定后交给 `routing/`

### `risks/`

负责：

- 误用边界
- 翻译红线
- 高风险表达检查

不负责：

- 替代方法层主分析
- 回头重做整条主链

最小产出：

- `哪些表达可用`
- `哪些表达不能用`
- `需要怎样降级或改写`

默认交给：

- 回到 `methods/` 或进入 `routing/`

### `routing/`

负责：

- 拿不准时怎么保守处理
- 输出前何时确认交付形式
- `深度分析` 与 `HTML 报告` 的路由

不负责：

- 重做主分析
- 替代 HTML 模板规范

最小产出：

- `继续澄清 / 继续方法分析 / 进入正式交付`
- `深度分析` 或 `HTML 报告`

默认交给：

- 文字交付时结束
- HTML 交付时进入 `html-output/`

### `html-output/`

负责：

- 把同一套内容骨架组织成单文件 HTML
- 复用模板完成最终可视化交付

不负责：

- 回头补澄清
- 改写前面的核心判断
- 另起一套内容逻辑

最小产出：

- 自包含、可直接打开的 `HTML 报告`

## 协同约束

- 每一层只做本层最小结果，做完就交接，不重复上一层
- `risks/` 和 `routing/` 是例外层，不要把它们写成常驻主分析层
- 索引页负责导航和交接，正文卡片负责本卡规则，不要互相重写
- 拿不准时，优先退回更前置、更保守的一层，不往后硬推

## 新规则应该写到哪里

- 触发条件、总边界、全局硬规则：写进 [SKILL.md](../SKILL.md)
- 澄清规则：写进 `clarification/`
- 分类规则：写进 `categories/`
- 场景入口：写进 `scenarios/`
- 方法卡与连卡：写进 `methods/`
- 风险边界：写进 `risks/`
- 输出与 HTML：写进 `routing/` 或 `html-output/`
- 层间交接规则：优先写在本页或对应层的 index

## 一句话总纲

- 先把问题问清，再把题目压稳；然后做分类、选场景、跑方法链；命中风险再做边界检查；最后才确认交付形式并决定是否进入 HTML。
