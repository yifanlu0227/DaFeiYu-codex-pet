![蓝色大肥鱼动画预览](preview.gif)

# 蓝色大肥鱼 🐳

蓝发蓝眼的 Q 版小鲸鱼女仆宠物，包含 **9 组动作和 16 个视线方向**，可用于支持 Pets 的 ChatGPT / Codex 客户端。

## 让 Codex 安装

把下面这句话发给 Codex，让 agent 访问仓库并完成安装：

> 请访问 https://github.com/yifanlu0227/DaFeiYu-codex-pet ，读取 README 和 pet.json，使用当前环境可用的宠物 skill，将仓库中已完成的 spritesheet.png 安装为我的宠物「蓝色大肥鱼」并启用。请直接使用现有图集，自动下载、验证、安装并检查结果。

## 给安装 agent 的说明

这是一个已经制作完成的 **v2 宠物动画图集**。安装素材在仓库根目录，名称、描述和校验值以 `pet.json` 为准。请下载素材到你的工作目录，由 agent 完成导入和启用；用户不需要手动下载、上传图片或到设置中选择宠物。

### 素材位置

| 文件 | 用途 | 原始文件地址 |
| --- | --- | --- |
| `spritesheet.png` | **安装用图集**，透明 PNG，包含全部动作和视线帧 | [下载原始 PNG](https://raw.githubusercontent.com/yifanlu0227/DaFeiYu-codex-pet/main/spritesheet.png) |
| `pet.json` | 宠物名称、描述、v2 规格、各行帧数和图集 SHA-256 | [读取元数据](https://raw.githubusercontent.com/yifanlu0227/DaFeiYu-codex-pet/main/pet.json) |
| `preview.gif` | 九组动作预览 | [查看动作 GIF](https://raw.githubusercontent.com/yifanlu0227/DaFeiYu-codex-pet/main/preview.gif) |
| `look.gif` | 十六个视线方向预览 | [查看视线 GIF](https://raw.githubusercontent.com/yifanlu0227/DaFeiYu-codex-pet/main/look.gif) |

`spritesheet.png` 是最终成品，可以直接用于安装。两个 GIF 只用于预览。保留 PNG 的透明度、尺寸和帧排列，直接验证原始文件即可，无需重新生成角色或动作。

### 使用哪些 skill

先发现并读取当前环境可用的宠物技能，使用它所支持的安装方式：

- **Pets 插件的 `work-pets:create-pet`**：将现有图集导入为用户自己的自定义宠物。沿用 skill 的验证、上传、创建和检查流程，输入使用本仓库的成品图集。
- **Pets 插件的 `work-pets:pets`**：查询宠物列表、启用安装后的宠物，并确认当前选中状态。
- **桌面客户端的内置 `hatch-pet`**：若当前环境提供该技能，读取它的说明并使用其支持的本机安装方式，输入仍使用现有图集。

技能名称可能因客户端或插件版本不同而变化，以当前环境实际提供的技能为准。安装后确认名称为「蓝色大肥鱼」，宠物已启用，再向用户报告完成。若环境缺少宠物能力或工作区禁止安装，应明确报告具体阻碍。

## 视线动画

![十六个视线方向的循环预览](look.gif)

## 图集规格

| 项目 | 规格 |
| --- | --- |
| 格式 | 透明 PNG，v2 |
| 尺寸 | 1536 × 2288 像素 |
| 网格 | 8 列 × 11 行 |
| 单帧 | 192 × 208 像素 |
| 总帧数 | 73 |

`pet.json` 是本仓库的素材元数据；具体安装方式由当前环境的宠物 skill 决定。

图集基于用户提供的角色参考图制作。本仓库未指定素材许可。
