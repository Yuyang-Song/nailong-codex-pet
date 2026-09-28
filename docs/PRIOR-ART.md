# Earlier Nailong projects: a research note

**Research date: 2026-09-28.** Dates below are UTC. This note investigates a first-of-its-kind claim; it is not a ranking of artwork quality or an assertion of ownership.

## Conclusion

**This repository should not claim to be the first open-source Nailong project, the first Nailong desktop pet, or the first Nailong pet for Codex.** Earlier public projects exist in each relevant category. In particular, an earlier Codex v2 package explicitly carries an MIT license, so the conclusion does not depend only on counting unlicensed public repositories.

The strongest positioning for this release is concrete: this interpretation of the character, nine semantic animations, sixteen gaze directions, independent direction review, English/Chinese documentation, and an installer that preserves the previous version. None of those features alone is claimed to be globally unique.

## Scope and method

The search combined general web searches in Chinese and English with GitHub repository search, direct README and license inspection, repository metadata, and commit history. Terms included:

- `奶龙 Codex 宠物 GitHub`, `Nailong Codex pet github`
- `奶龙 桌面宠物 github 开源`, `Nailong desktop pet open source github`
- `奶龙 codex`, `nailong codex`, `nailong pet`, `nailoong pet`
- `奶龙` and `奶龙 桌宠 site:gitee.com` as broader checks

Ten candidate repositories received direct GitHub API checks. Selected metadata is preserved in [prior-art-evidence.json](prior-art-evidence.json). Search results were not treated as enough by themselves for the central conclusion: the key Codex package's README, license, and first commit were checked directly. The Gitee search did not produce an additional verified source used here.

The sample is bounded. Search can miss renamed, unindexed, deleted, private, or differently described projects. Finding predecessors is enough to reject our own first claim; it is not enough to crown any one project the global first.

## Direct Codex precedents

| Repository | Created on GitHub | What was verified | License observation |
| --- | --- | --- | --- |
| [LC606mob/codex-yellow-reviewer-pet](https://github.com/LC606mob/codex-yellow-reviewer-pet) | 2026-05-03 | Description mentions 奶龙; README calls it Yellow Reviewer, with an 8×9 Codex atlas | LICENSE specifies CC-BY-NC-4.0; adjacent example, not a clean permissive-open-source or v2 claim |
| [ZUNGJYU-dotcom/codex-nailong-pet](https://github.com/ZUNGJYU-dotcom/codex-nailong-pet) | 2026-07-10 | Named Nailoong/Nailong packages, v2 atlas, previews and install files | LICENSE-CODE and character-rights notice separate code/config from artwork |
| [erich207/nailong-codex-pet](https://github.com/erich207/nailong-codex-pet) | 2026-07-13 | Named Nailong, 1536×2288 v2 atlas, pet manifest and install instructions | MIT text directly inspected; separate NOTICE also exists |
| [li2631026381-alt/nailong-codex-pet](https://github.com/li2631026381-alt/nailong-codex-pet) | 2026-08-03 | README, pet.json and spritesheet.webp present; described as Codex-compatible v2 | No license detected in checked root/API metadata |
| [Tomorins/nailong-codex-pet](https://github.com/Tomorins/nailong-codex-pet) | 2026-08-08 | Native v2 package, nine actions, build tools and optional Windows sound support | Asset-use and notice files; no root LICENSE detected |
| [FBBer/codex-milk-dragon-pet](https://github.com/FBBer/codex-milk-dragon-pet) | 2026-08-09 | Unofficial Nailong v2 package with scripts, release files and QA | Separate code license and asset notice |

The [erich207 initial commit](https://github.com/erich207/nailong-codex-pet/commit/7244a83aaabc6e0b55f473097ee10f0e7d69d6d8) is recorded at **2026-07-13 13:22:52 UTC**. Its current repository README describes the same broad installation format as ours. The repository's [MIT license](https://github.com/erich207/nailong-codex-pet/blob/main/LICENSE) was read directly. This is a particularly strong counterexample to a broad “first open-source Codex Nailong pet” claim; it does not establish third-party character rights.

The May 3 example needs qualification: its Chinese description mentions Nailong, while the README uses a generic name, disclaims brand affiliation, and specifies an earlier atlas layout. Its noncommercial license is also distinct from a permissive software license. It is useful historical context, but the conclusion above does not rely on treating it as an exact match.

## Wider ecosystem

| Repository | Created on GitHub | Relevance |
| --- | --- | --- |
| [ZreXoc/nailong-classification](https://github.com/ZreXoc/nailong-classification) | 2024-10-06 | Public image-classification code; shows the wider Nailong software ecosystem predates this pet. No license detected in checked metadata. |
| [nkxingxh/NailongDetection](https://github.com/nkxingxh/NailongDetection) | 2024-10-28 | Detection project with an AGPL-3.0 license reported by GitHub; unrelated to desktop-pet installation. |
| [mmexile/nailong-pet](https://github.com/mmexile/nailong-pet) | 2026-05-12 | Standalone desktop-pet source/assets and a release ZIP. The previously used NKU-mexile URL redirects here. No root license was detected. |
| [2002yxy/dsh-nailong-desktop-pet](https://github.com/2002yxy/dsh-nailong-desktop-pet) | 2026-08-14 | Nailong pet plugin for DeepSeek Harness; its README separates code licensing and preset-artwork rights. MIT is reported by GitHub. |

These are related projects, not dependencies or sources for our artwork. Additional search hits included pixel variants, Naiwa/Naifrog variants, and hybrid characters; they are not needed to establish the conclusion and are not treated as the same character implementation.

## What the dates can and cannot prove

- `created_at` is GitHub's repository creation time, **not necessarily its first public-release time**. A repository may have started private or may contain imported history.
- Commit dates describe the checked Git history and can precede repository creation. They are not a trusted universal publication clock.
- Current license detection can be incomplete (`null` or `NOASSERTION`). A public repository is not automatically permissively licensed. The key MIT license was checked as actual text rather than inferred from visibility.
- A project license cannot by itself establish rights to a third-party character. We did not obtain authorizations from any character rights holder.
- No attempt was made to inspect private projects or to prove the identity of the earliest project worldwide.

Confidence is **high that a first-of-its-kind marketing claim is unsupported and should not be used**. Confidence about the global earliest creator, first public timestamp, or comprehensive licensing of all character imagery is insufficient.

## Suggested public description

> An unofficial Nailong desktop companion for Codex, with nine animated states, sixteen gaze directions, bilingual setup instructions, and inspectable validation records.

Avoid “world's first,” “the original open-source Nailong,” and similarly unverified exclusivity claims.

## 中文结论

**不是第一批，更不能写“全球首个”或“第一个开源 Codex 奶龙”。** 检索已找到多个早于本仓库的直接同类项目，其中 erich207 的仓库创建于 2026-07-13，提供 v2 图集，并有直接核对过的 MIT 许可证。

更早的 2026-05-03 项目也提到奶龙，但 README 将其称作 Yellow Reviewer，采用 8×9 布局和非商业许可，因此不能不加区分地算作完全相同的开源 v2 项目。公开仓库、明确开源许可、角色素材授权是三件不同的事。

本次研究记录了十个候选仓库的公开元数据，不能证明全网最早是谁。对外建议强调本版本的具体设计、九种动作、十六方向、安装体验和中英文文档，而不是争夺没有证据的“第一”。
