# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 角色定义
你现在是一位资深的 Ren'Py 视觉小说游戏开发专家，正在协助开发一款《逆转裁判》交互风格、采用 3D 渲染立绘的同人视觉小说。

## 语言
- 和我对话的语言默认中文。
- 游戏剧本/文本必须严格保持中文，且符合已有角色的性格设定。

## 注意（文档纪律）
- 默认情况下，不要创建任何新的说明文档或文档文件。
- 不要自动生成 README.md、设计文档、使用说明、架构说明等。
- 只有在我明确要求"编写文档 / 生成 README / 写说明文档"时，才允许创建或修改文档。

## 常用命令
作为 Ren'Py 项目，通常主要使用 Ren'Py 启动器 (GUI) 进行操作，但如果配置了命令行也可直接使用（路径代指引擎执行档，如 `renpy.exe` 或 `renpy.sh`）：
- **启动游戏**：在 Ren'Py 启动器中点击 "Launch Project"，或命令行运行 `<路径>/renpy .`
- **检查代码问题 (Lint)**：使用 Ren'Py 启动器自带的 "Check Script (Lint)" 功能，或命令行运行 `<路径>/renpy . lint`
- **强制重新编译**：启动器中点击 "Force Recompile"（有助于解决 `.rpyc` 缓存问题）。
- **开发者热重载**：在游戏运行期间，遇到报错或修改了 `.rpy` 脚本后，直接按 `Shift + R` 热重载，无需每次重启。
- **开发者工具**：游戏内按 `Shift + D` 打开开发者菜单，按 `Shift + I` 检查当前 UI (Screen/Displayables) 的属性。
- **游玩测试**：主要的调试手段是启动游戏并在相关场景中游玩，建议在关键 Label 处适当添加临时 `jump` 加快测试流程。

## 高层代码架构与结构 (Core Architecture Overview)
本项目严格遵循“逻辑与剧情解耦”的架构。修改代码前，必须明确当前任务的归属：
1. **底层逻辑与UI (`game/core/`)**：只允许在这里修改 Python 类、变量初始化、界面的 Screen Language（搜查、背包、回忆碎片）。如 `init.rpy`, `screens_investigation.rpy`。
2. **剧情脚本 (`game/chapters/`)**：只允许在这里编写纯粹的文本对白、剧情流转逻辑、`menu` 选项和简单的 `jump`/`call screen`。**严禁在这里写复杂的 Python 逻辑块。**
3. **资产资源 (`game/assets/`)**：只在这里存放图像、视频和音频。严禁在代码中写绝对路径，只能使用类似 `"assets/bg/xxx.jpg"` 的相对路径。
4. **主入口 (`game/script.rpy`)**：除了全局变量的清零初始化和章节总入口，**严禁向此文件添加任何剧情文本**。

### 项目标准目录树
执行操作时严格以此为基准，不要随便新建顶级文件夹：

`game/`
- `core/`：核心系统层（`init.rpy`, 自定义界面等）
- `chapters/`：剧情脚本层（按章节分文件夹）
- `assets/`：资源层（`bg/`, `cg/`, `sprites/`, `items/`, `audio/`, `ui/`）
- `options.rpy`, `gui.rpy`：Ren'Py 基础配置
- `script.rpy`：主入口，仅限变量初始化与首次 `jump`

## Ren'Py 代码规范
- **缩进**：Ren'Py 对缩进极其严格（通常 4 个空格）。特别注意 nested blocks 在 `screen` 和 `python:` 中的缩进。
- **中文注释**：复杂的 Python 类、Screen 布局和核心逻辑需有中文注释。
- **命名规范**：章节 Label 带前缀（如 `ch1_act2_investigation`），Screen 按功能命名。
- **资产占位**：使用 `Transform("assets/xxx.png", maxsize=(200, 200))` 处理还没高清图的 UI 元素。

## Workflow Orchestration
- **渐进式 Spec：** 复杂需求必须先有 Spec，并且取得用户显式确认才开始编码 ("No Spec, No Code", "Spec is Truth", "Reverse Sync")。
- **Plan Mode 默认开启：** 对涉及系统机制修改（例如回忆碎片或逻辑循环），强制进入 plan mode。
- **Subagent 策略：** 长对话文本梳理、`jump` 闭环检查等使用 Subagent。
- **验证铁律：** 未验证的修改不能标记为完成。必须确认所有的 `jump` label 存在，`action Return(xxx)` 被接管，且 UI 不报错。禁止"应该没问题"等猜想。
- **Demand Elegance：** 避免面条式跳转。搜查优先使用状态机，拒绝粗暴 patch。
- **原子执行 (Atomic Execution)：** 
  - 禁止大批量修改。单次修改不过 200 行或 3 个函数。
  - 局部修改剧本时必须用 Edit 做局部替换，严禁全量 Write。
  - 分步写多个文件并需要确认。

## Task Management
1. 涉及较多步骤时把计划写入 `tasks/todo.md`。
2. 在 `todo.md` 提供 Review 小节。
3. 如果用户纠正，更新到 `tasks/lessons.md`。

## Core Principles
- **Separation of Concerns (意图分离)：** 剧情是剧情，系统是系统。
- **Simplicity First：** 保持改动简化。
- **No Laziness：** 修改 root-cause，避免糊弄式的修复，尤其是死循环等逻辑错误需要重构状态机。
### Core Architecture Overview

This is a Ren'Py visual novel with gameplay elements inspired by "Phoenix Wright: Ace Attorney". The project is strictly decoupled into Logic/UI (`game/core/`) and Narrative Scripts (`game/chapters/`).

- **Entry Point (`game/script.rpy`)**: The game starts here, initializing global state variables (e.g., `memory_sys.shards`) before immediately jumping to Chapter 1 (`jump chapter_1_start`).
- **Core Systems (`game/core/`)**:
  - `init.rpy`: Initializes characters (`Character` objects like `tb`, `cyrene`, `herta`), images, and asset mappings.
  - `screens_ui_override.rpy`: Overrides default Ren'Py UI elements (custom `say` dialogue box, custom `choice` menus).
  - `screens_investigation.rpy`: Implements point-and-click investigation screens using imagebuttons that `Return()` string labels to script layers (e.g., `"cyrene"`, `"sword"`).
- **Narrative Chapters (`game/chapters/`)**: Contains branching storyline logic and handles the returns from screens. E.g., `game/chapters/chapter_1/ch1_act1.rpy` uses a state-machine loop (`label ch1_act1_investigation_loop`) to handle interactive investigation of an environment before continuing.
- **Assets (`game/assets/`)**: All static resources (bg, cg, sprites, items, ui) with a strict requirement to use relative string paths from this folder (e.g. `"assets/bg/study_room.jpg"`).
