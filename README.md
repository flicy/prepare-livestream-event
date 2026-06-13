# Prepare Livestream Event

> English | [中文](#中文说明)

![Prepare Livestream Event overview](assets/examples/readme-intro-screenshot.png)

`prepare-livestream-event` is a GitHub-ready Codex Skill for preparing online livestream event launches. It turns an event brief into an event content page, poster prompts, Figma-editable visual assets, WeChat Official Account copy, Xiaohongshu copy, live reservation links, and WeChat group announcement drafts.

The recommended repository location is:

```text
https://github.com/flicy/prepare-livestream-event
```

A "GrowthOS toolkit repo" would simply mean a future collection repo that contains many GrowthOS skills/tools together. For this release, a standalone repo is clearer.

The workflow is intentionally semi-automatic: create drafts and assets quickly, use browser-assisted draft creation for WeChat Official Account and Xiaohongshu, and keep publishing, live reservation creation, and group sending behind human confirmation.

## What It Does

- Create a structured livestream event content page from a brief, Notion page, Markdown draft, or pasted text.
- Generate five distinct poster directions with Image 2.5-ready prompts, or the current OpenAI image model available in your environment.
- Prepare WeChat Official Account, Xiaohongshu, and Jike image export sizes.
- Provide Figma-editable SVG sources for visual explanation and layout refinement.
- Draft WeChat Official Account and Xiaohongshu announcement copy.
- Prioritize live reservation workflows for WeChat Channels and Xiaohongshu Live.
- Generate warm-up and final WeChat group announcement copy.

## Core Workflow

1. Event Page: normalize the livestream event brief into a reusable event schema.
2. Poster Prompts: create five visual directions for image generation.
3. Figma Polish: refine title, QR codes, safe areas, and layout in Figma.
4. WeChat/XHS Drafts: create browser-assisted platform drafts.
5. Live Links: create or record WeChat Channels / Xiaohongshu live reservation links.
6. Group Launch: generate a concise final group announcement.

## Visual Assets

The overview image above has an editable source:

- PNG screenshot: `assets/examples/readme-intro-screenshot.png`
- Figma-importable SVG: `assets/examples/readme-intro-editable.svg`
- AI-generated overview concept: `assets/examples/readme-visual-overview.png`

You can drag the SVG into Figma and edit text, shapes, colors, and layout.

## Brand Assets

This repo includes a draft GrowthOS logo reference:

![GrowthOS draft logo](assets/brand/growthos-logo-draft.png)

The logo is included as a temporary brand reference. A standardized GrowthOS logo / wordmark file is still a TODO before a polished public release.

## Poster Examples

These five sample posters were generated as visual references for the five built-in directions.

![Poster examples contact sheet](assets/examples/contact-sheet.png)

Individual files:

- `assets/examples/poster-growthos-minimal.png`
- `assets/examples/poster-agent-architecture.png`
- `assets/examples/poster-global-livestream.png`
- `assets/examples/poster-fde-enterprise.png`
- `assets/examples/poster-xiaohongshu-bold.png`

For production, use generated posters as concept art, then finalize text, QR codes, and safe-area crops in Figma.

## Real GrowthOS References

These real GrowthOS activity posters are included as public reference cases. Both are `1086 x 1448`, close to the Xiaohongshu 3:4 cover format, and useful as a master vertical poster source for livestream promotions.

![Real GrowthOS poster references](assets/examples/real-cases/real-cases-sheet.png)

Case files:

- `assets/examples/real-cases/coding-growthtalk-issue-9.png`
- `assets/examples/real-cases/coding-growthtalk-agent-fde.png`

The shared visual language is: warm paper collage, orange-black contrast, oversized title, live time row, organizer line, practical discussion bullets, host card, and QR-driven CTA.

## Install

Copy this folder into your Codex skills directory:

```bash
cp -R prepare-livestream-event ~/.codex/skills/
```

Then invoke it in Codex:

```text
Use $prepare-livestream-event to prepare a livestream event launch package for this activity brief.
```

## Quick Start

Use the dependency-free JSON template:

```bash
python3 scripts/normalize_event.py assets/event-template.json -o /tmp/event.json
python3 scripts/plan_image_sizes.py > /tmp/poster-sizes.json
python3 scripts/build_poster_prompts.py /tmp/event.json -o /tmp/poster-prompts.json
```

Then use `/tmp/poster-prompts.json` with your image generation workflow. After choosing a poster direction, refine final text, QR codes, and platform safe areas in Figma or your preferred design tool.

`assets/event-template.yml` is also included as a more human-readable version. YAML input requires PyYAML; JSON works with the Python standard library.

## Customize For Your Livestream Brand

Most teams should change these files first:

- `assets/event-template.yml`: recurring livestream event structure and default fields.
- `assets/event-template.json`: dependency-free template for scripts and automation.
- `references/growthos-brand.md`: colors, fonts, tone, visual motifs, logo TODO, and CTA language.
- `references/copywriting-templates.md`: WeChat, Xiaohongshu, group, and short-post templates.
- `references/poster-sizes.md`: platform sizes if your channels use different dimensions.
- `references/publishing-adapters.md`: browser-assisted draft workflow, account tools, and manual fallback.
- `references/productization-roadmap.md`: GitHub release positioning and checklist.

To adapt this from GrowthOS to another livestream brand:

1. Replace the palette and typography in `references/growthos-brand.md`.
2. Replace `assets/brand/growthos-logo-draft.png` with your own approved logo or remove it.
3. Rewrite the community tone phrases and CTA language.
4. Update `assets/event-template.yml` and `assets/event-template.json` with your default host, organizer, QR placeholders, and link fields.
5. Rewrite copy templates so the voice sounds like your brand.
6. Keep the confirmation gates unless your team has a separate approval system.

## Publishing Notes

WeChat Official Account, Xiaohongshu, live reservation platforms, and WeChat groups all have different access models. This skill defaults to browser-assisted draft creation for WeChat Official Account and Xiaohongshu.

Recommended adapter order:

1. Browser-assisted draft creation with the user's logged-in account.
2. Manual publishing package with Markdown, images, and checklist.
3. Official API or connected app tool, only when the account and API access are clearly available.

Priority live reservation platforms:

- WeChat Channels.
- Xiaohongshu Live.

Do not publish, schedule, reserve, or send from a real account unless the operator explicitly approves the final draft.

## Suggested Output Structure

```text
YYYY-MM-DD-event-slug/
  event.json
  event-page.md
  poster-prompts.json
  posters/
  copy/
    wechat-official.md
    xiaohongshu.md
    group-warmup.md
    group-final.md
  publishing-status.json
```

## License

MIT License. See `LICENSE`.

---

## 中文说明

![Prepare Livestream Event overview](assets/examples/readme-intro-screenshot.png)

`prepare-livestream-event` 是一个可以发布到 GitHub 的 Codex Skill，用来准备线上直播活动发布包：活动内容页、海报 prompt、Figma 可编辑视觉资产、公众号图文、小红书图文、直播预约链接和微信群预告文案。

建议发布位置：

```text
https://github.com/flicy/prepare-livestream-event
```

我之前说的 “GrowthOS 工具箱 repo” 只是未来的一种组织方式：如果你以后有很多 GrowthOS skills/tools，可以建一个合集仓库。这个 Skill 的第一版更适合做成独立 repo。

这个 Skill 默认采用“半自动发布”方式：可以快速生成草稿和素材；公众号和小红书优先做浏览器辅助草稿；公众号发布、小红书发布、视频号/小红书直播预约创建、微信群发送都必须经过人工确认。

## 这个 Skill 能做什么

- 从活动 brief、Notion 页面、Markdown 草稿或粘贴文本生成结构化线上直播活动内容页。
- 生成五种不同风格的海报方向，prompt 兼容 Image 2.5 或当前环境可用的 OpenAI 图片模型。
- 准备公众号、小红书、即刻常用图片尺寸。
- 提供可导入 Figma 修改的 SVG 视觉源文件。
- 生成公众号和小红书活动预告文案。
- 优先支持视频号和小红书直播预约链接流程。
- 生成微信群预热和最终活动预告。

## 核心流程

1. 活动内容页：把直播活动信息整理成可复用 schema。
2. 五版海报：生成五种视觉方向和图片生成 prompt。
3. Figma 修图：调整标题、二维码、安全区和版式。
4. 图文草稿：浏览器辅助创建公众号和小红书草稿。
5. 直播预约：创建或记录视频号/小红书直播预约链接。
6. 群预告：生成最终微信群发布文案。

## 视觉介绍图

上方介绍图包含可编辑源文件：

- PNG 截图：`assets/examples/readme-intro-screenshot.png`
- 可导入 Figma 的 SVG：`assets/examples/readme-intro-editable.svg`
- AI 生成的视觉概念图：`assets/examples/readme-visual-overview.png`

把 SVG 拖进 Figma 后，可以继续修改文字、颜色、形状和版式。

## 品牌素材

仓库内包含一个 GrowthOS draft logo 参考：

![GrowthOS draft logo](assets/brand/growthos-logo-draft.png)

这个文件目前只作为临时品牌参考。正式公开发布前，标准 GrowthOS logo / wordmark 仍然是 TODO。

## 五种海报样例

下面是 Skill 内置五种海报方向的样例图：

![Poster examples contact sheet](assets/examples/contact-sheet.png)

单图文件：

- `assets/examples/poster-growthos-minimal.png`
- `assets/examples/poster-agent-architecture.png`
- `assets/examples/poster-global-livestream.png`
- `assets/examples/poster-fde-enterprise.png`
- `assets/examples/poster-xiaohongshu-bold.png`

正式发布时，建议把 AI 生成图当成视觉方向，再进入 Figma 里修正文案、二维码和平台安全区。

## 真实 GrowthOS 案例

下面两张真实活动海报已经作为公开案例加入目录。它们都是 `1086 x 1448`，接近小红书 3:4 主推封面比例，也适合作为线上直播活动的竖版主视觉母版。

![Real GrowthOS poster references](assets/examples/real-cases/real-cases-sheet.png)

案例文件：

- `assets/examples/real-cases/coding-growthtalk-issue-9.png`
- `assets/examples/real-cases/coding-growthtalk-agent-fde.png`

这两张图体现了 GrowthOS 当前的活动视觉语言：纸张拼贴、橙黑对比、超大标题、直播时间条、联合主办方、真实讨论问题、发起人信息和二维码 CTA。

## 安装方式

把这个文件夹复制到 Codex skills 目录：

```bash
cp -R prepare-livestream-event ~/.codex/skills/
```

然后在 Codex 里调用：

```text
Use $prepare-livestream-event to prepare a livestream event launch package for this activity brief.
```

## 快速开始

使用不依赖额外库的 JSON 模板：

```bash
python3 scripts/normalize_event.py assets/event-template.json -o /tmp/event.json
python3 scripts/plan_image_sizes.py > /tmp/poster-sizes.json
python3 scripts/build_poster_prompts.py /tmp/event.json -o /tmp/poster-prompts.json
```

然后把 `/tmp/poster-prompts.json` 接到你的图片生成流程。选定海报方向后，再用 Figma 或其他设计工具处理最终文字、二维码和平台安全区。

`assets/event-template.yml` 是更适合人阅读和编辑的版本。YAML 输入需要 PyYAML；JSON 可以直接用 Python 标准库运行。

## 改成自己的直播活动品牌

建议优先修改这些文件：

- `assets/event-template.yml`：常规直播活动结构和默认字段。
- `assets/event-template.json`：脚本和自动化使用的无依赖模板。
- `references/growthos-brand.md`：品牌色、字体、语气、视觉元素、logo TODO 和 CTA。
- `references/copywriting-templates.md`：公众号、小红书、群消息和短帖模板。
- `references/poster-sizes.md`：如果你的平台尺寸不同，在这里改。
- `references/publishing-adapters.md`：浏览器辅助草稿、账号工具和手动发布兜底方案。
- `references/productization-roadmap.md`：GitHub 发布定位和检查清单。

从 GrowthOS 改成其他直播活动品牌时：

1. 替换 `references/growthos-brand.md` 里的品牌色和字体。
2. 替换或删除 `assets/brand/growthos-logo-draft.png`。
3. 改写社群语气、常用表达和 CTA。
4. 更新 `assets/event-template.yml` 和 `assets/event-template.json` 里的默认主理人、组织方、二维码占位和链接字段。
5. 改写文案模板，让它听起来像你的品牌。
6. 除非你有独立审核系统，否则保留人工确认节点。

## 发布说明

公众号、小红书、直播预约平台和微信群的权限模型都不同。这个 Skill 默认使用浏览器辅助创建公众号和小红书草稿。

推荐 adapter 顺序：

1. 浏览器辅助创建草稿，使用用户已登录账号。
2. 手动发布包，包含 Markdown、图片和检查清单。
3. 官方 API 或已连接工具，仅在账号和 API 权限明确可用时使用。

优先直播预约平台：

- 视频号。
- 小红书直播。

不要在没有明确确认的情况下，用真实账号发布、定时、创建预约或发送群消息。

## License

MIT License. See `LICENSE`.
