![蓝色大肥鱼动画预览](preview.gif)

# 蓝色大肥鱼 🐳

蓝发蓝眼的 Q 版小鲸鱼女仆宠物，包含 **9 组动作和 16 个视线方向**，可用于支持 Pets 的 ChatGPT / Codex 客户端。

## 安装到桌面端

使用支持 Pets 安装功能的桌面客户端，在浏览器地址栏粘贴下面的完整链接，按客户端提示完成安装，然后在 Pets 设置中选择「蓝色大肥鱼」。

```text
codex://pets/install?name=%E8%93%9D%E8%89%B2%E5%A4%A7%E8%82%A5%E9%B1%BC&imageUrl=https%3A%2F%2Fraw.githubusercontent.com%2Fyifanlu0227%2FDaFeiYu-codex-pet%2Fmain%2Fspritesheet.png&description=%E8%93%9D%E5%8F%91%E8%93%9D%E7%9C%BC%E7%9A%84Q%E7%89%88%E5%B0%8F%E9%B2%B8%E9%B1%BC%E5%A5%B3%E4%BB%86%EF%BC%8C%E7%A9%BF%E7%9D%80%E6%B7%B1%E8%93%9D%E7%99%BD%E8%89%B2%E5%A5%B3%E4%BB%86%E8%A3%99%EF%BC%8C%E5%B8%A6%E7%9D%80%E8%93%AC%E6%9D%BE%E9%95%BF%E5%8F%91%E5%92%8C%E5%8F%AF%E7%88%B1%E7%9A%84%E9%B2%B8%E9%B1%BC%E5%B0%BE%E5%B7%B4%E3%80%82&spriteVersionNumber=2
```

[查看并复制安装链接](install-link.txt) · [下载透明动画图集](https://raw.githubusercontent.com/yifanlu0227/DaFeiYu-codex-pet/main/spritesheet.png)

安装链接遵循[官方桌面安装链接格式](https://learn.chatgpt.com/docs/reference/commands#pets)，指定了 `spriteVersionNumber=2`。请复制完整地址到浏览器地址栏。功能可用性取决于客户端版本和工作区设置。

## 使用 Pets 插件导入

1. 下载上面的 `spritesheet.png`。
2. 将图集附到支持 Pets 插件的聊天中。
3. 发送：

> 使用 Pets 插件，把附件中的 v2 宠物动画图集导入为我的自定义宠物，命名为「蓝色大肥鱼」，验证后创建并启用。请直接使用附件中的现有动画，不重新生成形象。

插件会在你的账号中创建宠物副本。

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

普通网页端 Upload pet 文档列出的 1536 × 1872 上传入口与本图集规格不同。请使用上述 v2 安装链接或 Pets 插件导入。[Pets 官方文档](https://learn.chatgpt.com/docs/pets)

## 文件说明

- `spritesheet.png`：安装所需的完整透明动画图集。
- `preview.gif`：九组动作的循环预览。
- `look.gif`：十六个视线方向的循环预览。
- `install-link.txt`：桌面安装链接。
- `pet.json`：名称、说明、规格和 SHA-256；用于说明素材，不是客户端安装清单。
- `make-install-link.py`：根据图集 HTTPS 地址生成安装链接，只依赖 Python 标准库。

如需使用其他图集托管地址，可以运行：

```sh
python3 make-install-link.py 'https://你的图集下载地址/spritesheet.png'
```

图集基于用户提供的角色参考图制作。本仓库未指定素材许可。
