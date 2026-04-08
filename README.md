<div align="center">

<h1>毛选拆局.skill</h1>

<p><em>“最近大家都在蒸馏 skill。蒸馏完如果还是不会解决问题，那就等于把热闹做成了周边。”</em></p>

<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://claude.ai/code"><img src="https://img.shields.io/badge/Claude%20Code-Skill-blueviolet" alt="Claude Code Skill"></a>
  <a href="https://openai.com/"><img src="https://img.shields.io/badge/Codex-Compatible-black" alt="Codex Compatible"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/AgentSkills-Standard-green" alt="AgentSkills Standard"></a>
</p>

<br>

<p><strong>把《毛泽东选集》蒸馏成一个真能拆现实问题的 skill。</strong></p>

<p>
  不是语录复读机，不是高压话术生成器，也不是“主要矛盾”四个字到处乱扣帽子。<br>
  它只干一件正事：先把问题看清，再把局面拆开，最后给出能往前推的判断和动作。
</p>

<br>

<p><strong>你可以把它理解成，把“新中国最会解决问题的那种脑子”请来，当一次临时参谋。</strong></p>

<br>

<p>
  <a href="#安装">安装</a> ·
  <a href="#使用">使用</a> ·
  <a href="#适用场景">适用场景</a> ·
  <a href="#输出结果">输出结果</a> ·
  <a href="#边界">边界</a> ·
  <a href="#仓库结构">仓库结构</a>
</p>

</div>

---

## 它适合谁

适合那种一眼看过去像是小问题，拆开才发现背后缠着一堆结构的局面：

- 项目推进不动，人人都在忙，但结果就是不动
- 合伙人、同事、上下级之间互相拉扯，信息不透明，责任不清楚
- 团队表面是执行差，实质是路线、阶段和控制点错位
- 关系问题表面是情绪，背后其实是边界、资源、第三方和旧账
- 你在纠结换工作、止损、继续谈、还是直接掀桌，但脑子里还是一锅粥

一句话：

**它擅长的不是“答题”，而是“拆局”。**

## 它和普通“毛选风格 Prompt”有什么不同

- **不抢答**：先调查，再判断，不装一眼看穿全局
- **不空喊**：不堆大词，重点是主要矛盾、阶段、力量、路线、风险
- **不只分析**：最后会落到下一步动作，而不是停在一段气势很足的话
- **能出成品**：除了文字版分析，还能生成可保存、可分享的单文件 HTML 报告

## 它怎么工作

这不是“你一句，我输出八段”的技能。正常流程是：

1. 先把题目问清楚：目标、关键事件、关键人物、已做尝试、现实约束。
2. 再判断局面结构：主要矛盾在哪，处于什么阶段，控制点和风险点落在哪。
3. 最后再给方案：推荐路线、执行顺序、风险边界、下一步动作。
4. 正式输出前，会确认你要的是文字版深度分析，还是 HTML 报告。

这个 skill 最核心的一句话其实很朴素：

**先别急着下结论，先把题目看对。**

## 适用场景

- 工作推进：项目卡点、资源分配、跨团队协作、执行失灵
- 团队治理：角色混乱、机制失效、权责不清、反馈回路断裂
- 关系边界：伴侣、朋友、合伙人、上下级之间的长期拉扯
- 自我管理：状态波动、节奏失控、长期目标和现实能力脱节
- 生活决策：换工作、分手、合作、止损、继续投入还是撤退

## 安装

### Claude Code

Claude Code 会从项目里的 `.claude/skills/`，或全局的 `~/.claude/skills/` 读取 skill。

```bash
# 安装到当前项目（在你的项目根目录执行）
mkdir -p .claude/skills
git clone https://github.com/SamadhiFire/maozedong-maoxuan-skill.git .claude/skills/maozedong-maoxuan-skill

# 或安装到全局（所有项目都能用）
git clone https://github.com/SamadhiFire/maozedong-maoxuan-skill.git ~/.claude/skills/maozedong-maoxuan-skill
```

### Codex

如果你在用 Codex，一般放进 `$CODEX_HOME/skills/` 或 `~/.codex/skills/` 即可。

```bash
git clone https://github.com/SamadhiFire/maozedong-maoxuan-skill.git ~/.codex/skills/maozedong-maoxuan-skill
```

### 其他平台

不是每个平台都叫 skill，但大多数 agent 平台都支持“自定义系统提示词 / 自定义技能目录 / 项目级规则”。

最省事的用法：

1. 把整个仓库放进平台的自定义 skill 或 prompt 目录。
2. 至少保留 `SKILL.md` 和 `references/`。
3. 在对话里直接说“按这个 skill 的流程先问清楚，再分析”。

如果平台根本没有 skill 机制，也能凑合用：

1. 把 `SKILL.md` 的核心规则作为系统提示词。
2. 把你的问题描述贴进去。
3. 明确要求它先澄清，别抢答。

## 使用

### 最简单的触发方式

把 skill 装好后，直接说这些都行：

- `用毛选帮我分析这个项目为什么推进不动`
- `用教员的方法拆一下我和合伙人的关系`
- `按主要矛盾和阶段判断，分析我现在该不该换工作`
- `别急着给答案，先把问题问清楚`
- `最后给我一份 HTML 报告`

### 想让结果更准，最好顺手给这五样

- `目标`：你最想推进的结果是什么
- `事件`：最近一次最说明问题的关键事件
- `人物`：关键人物、第三方、关系人分别是谁
- `尝试`：你已经做过什么
- `约束`：你现在真正的限制、底线和代价

### 一个好用的提问模板

```text
请用毛选拆局的方法帮我分析这件事。

我的目标：
最近关键事件：
涉及人物：
我已经做过的尝试：
我的现实约束：

先别急着下结论，如果信息不够请先追问我。
```

## 输出结果

### 1. 文字版深度分析

适合先把局面看明白。通常会包括：

- 问题重述
- 核心判断
- 当前阶段
- 推荐路线
- 风险提醒
- 下一步动作

### 2. 单文件 HTML 报告

适合保存、复盘、转发，复杂问题还可以带上：

- 时间线
- 关系图
- 路线比较
- 证据链
- 控制点分布
- 执行计划

可参考示例：[`examples/sample-project-report.html`](./examples/sample-project-report.html)

## 边界

这个 skill 不适合下面几种用法：

- 只想摘毛选原文，不想分析现实问题
- 只想学几句“主要矛盾在于你不听话”这种吓人的台词
- 拿方法论给别人扣帽子、压人、操控关系
- 问题本身很轻，用普通常识建议就够了
- 纯技术实现细节问题，不涉及结构判断和路线设计

一句话：

**别把方法论玩成气势道具。**

## 仓库结构

```text
maozedong-maoxuan-skill/
├── SKILL.md                         # 主入口
├── references/                      # 分类、澄清、方法、风险、输出规则
├── examples/sample-project-report.html
├── distill/                         # 蒸馏材料
└── source-texts/                    # 原始文本
```

如果你想看规则怎么展开：

- 从 [`SKILL.md`](./SKILL.md) 开始
- 具体方法在 [`references/methods`](./references/methods)
- 风险边界在 [`references/risks`](./references/risks)
- HTML 输出规则在 [`references/html-output`](./references/html-output)

## 最后一句

这不是教你背《毛选》。

这是把《毛选》蒸馏成一套今天还能用来拆现实问题、推进现实行动的工具。
