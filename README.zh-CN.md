# Learning Skills · 通用教学与笔记技能

[English](README.md)

这是从个人课程工作流中提炼的两项通用 Agent Skills，适合学生、自学者，以及希望让 AI 按目标持续辅导的人。

- **learning-tutor**：测起点、生成学习路径、逐步讲授、验证实际能力、补讲、间隔复习、保存会话断点。
- **study-notes**：整理概念、速查、错题和课程信息，保留来源与关联，兼容普通 Markdown 和 Obsidian。

两个技能可以独立安装。学校、课程码、双语、选择题、笔记软件和持久化目录都不是必选前提。它们适配的是可配置的学习流程，不声称一个流程适用于所有人或所有教学场景。

## 安装与开始

把 `skills/` 下需要的完整技能文件夹复制到宿主的技能目录，保留 `references/`、`assets/`、`LICENSE` 等文件。

| 宿主 | 项目内目录 | 用户级目录 |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |

安装位置依据 [OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills) 和 [Claude Code 官方说明](https://code.claude.com/docs/en/skills)。Codex 可用 `$learning-tutor`、`$study-notes`，Claude Code 可用 `/learning-tutor`、`/study-notes`；其他支持 Agent Skills 的工具按各自规则加载。已有同名技能时先检查，勿直接覆盖。

```text
用 learning-tutor 教我统计推断，中文讲解，练习可以用英文。
先确认我能做什么，按我这周的目标安排，每次半小时。

用 study-notes 整理这些材料，放进我指定的笔记目录。
保留现有的长篇推导；补充资料要注明来源。
```

可选初始化工具只需要 Python 3.10+ 标准库。在本项目根目录执行：

```shell
python skills/learning-tutor/scripts/init_workspace.py --workspace ./workspaces/statistics --topic "统计推断" --language zh-CN --assessment-language en --notes-format obsidian
```

`--workspace` 必填。`--dry-run` 预览；`--notes-format none` 禁用笔记；`--style reference` 选择长篇参考风格；`--date YYYY-MM-DD` 指定本地日期。工具创建的管理页默认英文，导师可按语言设置翻译正文。技能本身不用 Python 也能工作，只是无法运行这个辅助工具。

初始化会创建 `.learning/` 中的设置、状态、学习路径、偏好和作答记录，以及可选的 `notes/Overview.md`。不创建空概念页，不捏造教学进度。再次运行遇到已有 `.learning/` 时不修改任何文件，新增参数也不会覆盖旧配置。使用旧笔记库时先以 `none` 初始化，再明确设置笔记路径。

## 通用版保留了什么

学习路径、验证方法和练习来源分别选择：可以按教材、作业、实验、项目、考试或自主目标来排；可以选择解释、推导、代码、写作等证据。不会用一道选择题证明一个人能独立编程，也不会把讲过、记过当成学会。

状态保存“现在到哪、下一步做什么”，路径保存阶段与通过条件，偏好保存“如何配合这个人”，作答记录保存事实证据，笔记保存可复用知识。拆分这些职责是为了避免多处进度互相矛盾。

保留真实错因、答案与选项重排后的核对、资料修订后回改笔记、速查链接到完整解释等机制。双语、题型、通过比例、复习间隔和笔记长度都可以调整。用户可以跳过流程，但未验证的能力会如实标记。

## 开源定位与验证

类似项目已经存在，不能宣传“GitHub 首个教学 skill”。本项目希望提供的是轻量、可拆装的教学与笔记协作流程。详细比较在 [开源价值评估](docs/open-source-assessment.zh-CN.md)，配置在 [customization](docs/customization.md)，个人版迁移在 [迁移说明](docs/migration.zh-CN.md)。

```shell
python scripts/validate_package.py
python -m unittest discover -s tests -v
```

这是 0.1 候选版本。自动验证覆盖目录结构和初始化行为，不代表学习效果得到实验证明，也不代表所有宿主集成都已实测。[验证说明](docs/validation.md) 列出了范围和后续行为评估场景。

采用 [MIT](LICENSE) 许可。发布的是技能和工具，不包含个人学习档案、学校课件或真实作答历史。学习数据宜存放在另一个目录；写入复习日期不会自动创建通知。
