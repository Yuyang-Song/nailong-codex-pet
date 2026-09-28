# Nailong imperial skins / 奶龙帝境皮肤

[English README](../README.md) · [中文 README](../README.zh-CN.md)

Two new skins are packaged alongside Classic Nailong. Each has its own complete v2 atlas and validation records under `qa/<skin-id>/`. Use `scripts/install.py --list` to see installable IDs.

| Skin | Identity | Signature sequence |
| --- | --- | --- |
| Shi Hao — 独断万古 | Long black hair, uncovered yellow face, narrowed severe eyes, dark gold emperor armor and sword | Charge → cut a spatial rift → enter it → vanish → 独断万古 |
| Ye Fan — 天帝镇世 | Long black hair, uncovered yellow face, narrowed severe eyes, white/gold robe, feet on bronze cauldron | Cauldron grows step by step → commanding seal → 我为天帝，当镇压世间一切敌 |

The signature sequence occupies the existing five-frame `jumping` row. It is a short keyframe animation, not a new client action or a timed cutscene API. The checked desktop build plays this row as four 140 ms frames and one 280 ms frame (840 ms total). The package cannot change that timing. The desktop client controls triggering, interruptions and looping. Standard action previews use those durations; a separate `signature-slow.gif` is explicitly slowed for reading the captions. The long Ye Fan caption is split into three lines for readability at native pet size.

Quiet idle motion keeps the sword or cauldron stable, with breathing, a measured blink and subtle hair movement. Working uses restrained cultivation gestures; waiting and review retain their own task meanings. Both faces remain completely uncovered, with readable eyes and closed, unsmiling mouths.

The requested signature rows intentionally allow a spatial rift, disappearance, growing cauldron and Chinese lettering. Those are authored scenes rather than extraction defects. Other states maintain stable scale and complete character silhouettes.

## 中文

本次只新增石昊、叶凡两套皮肤，保留原版。两者都有长发和肃杀眼神，脸部完全露出，不戴面具，不再使用大笑表情。

石昊：蓄势、挥剑斩开空间裂隙、进入、消失，最后出现「独断万古」。叶凡：脚下鼎逐帧变大，最后显示「我为天帝，当镇压世间一切敌」。两段使用现有五帧跳跃槽位，核对的桌面端版本采用前四帧各 140 ms、末帧 280 ms，总计 840 ms，皮肤包无法改速。实际触发和循环由桌面端控制，不新增客户端事件。README 的慢放版本会单独标明，不代表客户端实播速度。文字在小尺寸下的可读性需要逐帧检查。

每套都制作独立待机、移动、招呼、受挫、等待、工作、检查和十六方向视线，完成检查后才能安装。服装设计属于非官方同人创作，见 [ASSETS.md](../ASSETS.md)。
