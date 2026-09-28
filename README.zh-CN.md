[English](README.md) · **简体中文**

<div align="center">

# 奶龙 · Codex 桌面宠物

**把一只会眨眼、挥手、蹦跶的小黄龙，放到你的桌面上。**

适用于支持自定义 v2 宠物的 Codex 桌面端 · 九种动作 · 十六个视线方向 · 透明背景

<img src="docs/previews/idle.gif" width="192" alt="奶龙眨眼待机动画"> <img src="docs/previews/waving.gif" width="192" alt="奶龙挥手动画"> <img src="docs/previews/jumping.gif" width="192" alt="奶龙跳跃动画">

[下载安装包](https://github.com/Yuyang-Song/nailong-codex-pet/releases/latest) · [安装方法](#安装) · [全部动作](#它会做什么) · [制作与修改](docs/DEVELOPMENT.md)

</div>

这是一份奶龙主题的非官方桌面宠物作品。你写代码时，它会安静眨眼；任务运行时，它会认真思考；等你确认时，它会露出期待的小表情。支持宠物视线交互的桌面端，还能让它朝鼠标所在方向看。

**下载即用，不需要重新生成图片，也不需要 API Key。** 仓库公开提供完整精灵图、配置、安装脚本和制作说明。角色相关权利不因本仓库公开而转让，详见[素材与许可说明](ASSETS.md)。

## 安装

### 方法一：下载 ZIP，复制两个文件

1. 打开 [Releases](https://github.com/Yuyang-Song/nailong-codex-pet/releases/latest)，下载 **`nailong.zip`**。
2. 解压后，把整个 **`nailong` 文件夹**放入你的 Codex 宠物目录。macOS 默认位置如下：

   ```text
   ~/.codex/pets/nailong/
   ├── pet.json
   └── spritesheet.webp
   ```

   ZIP 还附带许可、素材说明与中英文 README；桌面端实际只读取 `nailong/` 内的两个文件。

   在 Finder 中按 **⌘⇧G**，输入 `~/.codex/pets/` 即可前往该目录。如果目录不存在，先创建它。如果设置过 `CODEX_HOME`，请使用 `$CODEX_HOME/pets/`。

3. 打开桌面端 **Settings → Mini & Pets（部分版本显示为 Pets）**，在自定义宠物区域刷新列表，选择 **「奶龙」**。没有出现时，完全退出再重新打开应用。

> 安装的是 `pet.json` 和 `spritesheet.webp`。README 中的 GIF 只是预览，不能代替精灵图。请避免多套一层目录，例如 `pets/nailong/nailong/pet.json`。

### 方法二：克隆后安装

需要 Git 和 Python 3.9+，安装脚本不依赖第三方 Python 包。

```bash
git clone https://github.com/Yuyang-Song/nailong-codex-pet.git
cd nailong-codex-pet
python3 scripts/install.py
```

安装脚本默认使用 `CODEX_HOME`，未设置时使用 `~/.codex`。它只安装这只宠物，不修改桌面端设置，也不会自动切换当前宠物。

```bash
# 指定另一处 Codex 数据目录
python3 scripts/install.py --codex-home /path/to/codex

# 更新已安装版本：先备份旧目录，再安装
python3 scripts/install.py --replace
```

已有同名宠物时，默认拒绝覆盖。使用 `--replace` 会把旧版本移到 `CODEX_HOME/pet-backups/` 下，并打印备份路径。

**兼容性：** 已核对本项目制作时 macOS 桌面端的本地宠物加载格式；需要客户端支持 `spriteVersionNumber: 2`。其他平台和后续版本尚未实际验证，设置入口也可能随版本变化。安装已在磁盘上验证，尚未通过应用界面自动化验证播放。

## 它会做什么

| 动作 | 画面表现 | 帧数 |
| --- | --- | ---: |
| 待机 `idle` | 轻轻呼吸、眨眼 | 6 |
| 向右跑 `running-right` | 向右迈步、交替摆动手脚 | 8 |
| 向左跑 `running-left` | 与右跑对应的左向动作 | 8 |
| 挥手 `waving` | 抬手打招呼 | 4 |
| 跳跃 `jumping` | 蹲下、起跳、腾空、落地 | 5 |
| 受挫 `failed` | 低头、委屈、摊手 | 8 |
| 等待 `waiting` | 合手等待、期待回应 | 6 |
| 工作 `running` | 托腮、思考、专注处理任务 | 6 |
| 检查 `review` | 歪头、观察、眨眼 | 6 |
| 视线方向 | 从正上方开始，顺时针一圈 | 16 |

`running` 是任务工作状态；桌面上向左、向右移动使用另外两组跑动动画。实际何时播放由客户端决定。

<details>
<summary>展开查看完整精灵图预览</summary>

![九种动作和十六个视线方向](docs/animation-sheet.png)

</details>

## 仓库里有什么

```text
pet/nailong/          可直接安装的两个文件
docs/previews/       从最终精灵图导出的动画预览
docs/DEVELOPMENT.md  帧布局、生成过程和修改方法
scripts/install.py  无第三方依赖的本地安装器
scripts/assets.py   校验图片、导出预览、构建发布 ZIP
qa/                 去除本机路径后的校验和视觉检查记录
ASSETS.md           素材来源、AI 生成说明和权利范围
LICENSE             原创脚本与文档的 MIT 许可
```

最终精灵图为 **1536 × 2288** 的透明 WebP，按 **8 列 × 11 行**排列，每格 **192 × 208**。提供的是最终栅格素材，不包含 3D 模型、骨骼或可以确定性重现 AI 原图的工程文件。

## 常见问题

**复制后看不到奶龙？**

- 检查两个文件是否直接位于 `pets/nailong/` 下。
- 使用自定义 `CODEX_HOME` 时，确认复制到了该目录。
- 检查 `pet.json` 中 `spriteVersionNumber` 为 `2`，`spritesheetPath` 为 `spritesheet.webp`。
- 刷新宠物列表或重启应用；旧客户端可能不支持此格式。

**需要运行服务器、安装插件或提供 API Key 吗？**

不需要。运行宠物只需要桌面端和两个本地文件。Python 只用于可选的安装脚本；手动复制不需要 Python。

**能换名字吗？**

可以修改 `pet.json` 的 `displayName`。若要与另一只奶龙并存，请同时换一个文件夹名和 `id`。

**怎么卸载或恢复旧版？**

先在客户端切换到其他宠物，再把 `pets/nailong/` 移出宠物目录。使用安装器更新过的用户，可将 `pet-backups/` 中对应的备份目录移回并命名为 `nailong`。

**有哪些已知小问题？**

接近正上方的 22.5° 姿势，向右看的幅度较轻；跳跃为了留出腾空空间，整体略小。视觉检查接受了这些差异，详见 [QA 记录](qa/visual-review.json)。它们不影响文件格式校验。

## 是第一个开源奶龙吗？

不是。我们找到多个更早的公开奶龙项目，包括 Codex v2 宠物；其中存在明确的 MIT 许可项目。本仓库不作“首个”声明。创建时间、许可范围与检索局限详见[先例研究](docs/PRIOR-ART.md)。

## 相关项目

更早的社区作品包括 [erich207/nailong-codex-pet](https://github.com/erich207/nailong-codex-pet) 和 [ZUNGJYU-dotcom/codex-nailong-pet](https://github.com/ZUNGJYU-dotcom/codex-nailong-pet)，可以了解不同的角色表现。本项目独立制作，没有合入这些项目的素材或代码。更多项目与时间证据见[先例研究](docs/PRIOR-ART.md)。

## 参与改进

欢迎提交动画衔接、安装兼容性、文档或脚本改进。反馈问题时，请附上操作系统、桌面端版本、安装方式和复现步骤；截图中请遮住个人信息。修改动作前可先阅读[开发说明](docs/DEVELOPMENT.md)。

## 许可与声明

原创脚本和文档使用 [MIT License](LICENSE)。奶龙角色名称、形象及相关第三方权利**不包含在 MIT 授权内**；精灵图和预览的来源与适用范围见 [ASSETS.md](ASSETS.md)。本项目非奶龙权利方或 OpenAI 官方项目，也不表示获得其背书。

---

<div align="center">愿你的下一次编译顺利，奶龙也少委屈一次。</div>
