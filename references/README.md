# References 协同地图

按需读取，不要把整个目录一次性加载进上下文。

## 默认主链

`信息决策门 -> 问题重述 -> 分类/场景 -> 方法卡 -> 风险检查 -> 输出`

其中：

- `clarification/` 判断要不要问、问什么，以及如何防止长问题漂移。
- `clarification/round-response-structure.md` 规定稳定外显三结构：摆情况、抓主导、定行动。
- `categories/` 和 `scenarios/` 负责内部路由，不要求对用户展示分类名。
- `methods/` 负责形成判断；一次通常只读 `1` 到 `2` 张卡。
- `methods/maoxuan-reasoning-style.md` 负责保留毛选式的认识路径、论证节奏和语言气口。
- `risks/` 负责安全旁路、误用边界和高风险术语翻译。
- `routing/` 负责置信度和输出形式。
- `html-output/` 只负责最终呈现，不反向制造分析结论。

## 最短读取路径

### 输入信息足够

1. 读 [ambiguity-gate.md](./clarification/ambiguity-gate.md) 快速放行。
2. 读 [problem-restatement.md](./clarification/problem-restatement.md) 压稳问题。
3. 按需读 [scene-index.md](./scenarios/scene-index.md) 和 [method-index.md](./methods/method-index.md)。
4. 正式输出前读 [maoxuan-reasoning-style.md](./methods/maoxuan-reasoning-style.md)。
5. 命中风险时再读对应风险文件。
6. 直接输出分析或方案。

### 输入基本足够但存在关键缺口

1. 给暂定判断，列出关键假设和替代解释。
2. 只有一个分叉点会改变结论时，补 `1` 个问题。
3. 不因为存在任何未知项就退回完整问卷。

### 输入严重不足

1. 读 [intake-flow.md](./clarification/intake-flow.md)。
2. 首轮最多问 `2` 个高杠杆问题；后续通常一次问 `1` 个。
3. 需要选项题时读 [choice-question-format.md](./clarification/choice-question-format.md)。
4. 复杂长问题再读 [focus-anchor.md](./clarification/focus-anchor.md)。

### 高风险或紧急情况

先读 [safety-escalation.md](./risks/safety-escalation.md)，完成最低限度安全处置后，再决定是否进入常规主链。

### 用户要 HTML

内容判断稳定后再读：

1. [output-mode-routing.md](./routing/output-mode-routing.md)
2. [visual-report-spec.md](./html-output/visual-report-spec.md)
3. [report-build-rules.md](./html-output/report-build-rules.md)
4. [visual-report-template.html](./html-output/visual-report-template.html)

## 层间最小交接

- 澄清层交出：目标、关键事实、关键未知项。
- 分类/场景层交出：最合适的现实入口和候选方法卡。
- 方法层交出：判断、依据、替代解释、下一步验证。
- 风险层交出：可用表达、禁用表达、必要降级或专业转介。
- 输出层交出：文字分析或自包含 HTML 成品。

## 协同约束

- 用户明确要求优先于默认流程。
- 信息足够就放行，不为展示流程而追问。
- 内部可以使用分类和方法名，对外优先写成自然语言。
- 区分原文依据、现代转译和本次推断。
- 新规则只写在负责该规则的文件，其他文件只链接，不重复整段规范。
