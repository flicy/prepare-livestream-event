# Productization Roadmap

This skill is named `prepare-livestream-event`. It prepares reusable online livestream event launch packages: event page, poster generation prompts, platform copy, browser-assisted drafts, live reservation links, and group promotion.

## Final name

`prepare-livestream-event`

The name is precise, verb-led, and safe. It communicates that the skill prepares assets and drafts before human approval.

## Positioning

One-line positioning:

> A Codex Skill for preparing online livestream event launches: event page, poster directions, Figma-ready assets, WeChat/Xiaohongshu drafts, live reservation links, and group announcements.

Chinese positioning:

> 一个用于准备线上直播活动发布包的 Codex Skill：活动内容页、海报方向、Figma 可编辑素材、公众号/小红书草稿、直播预约链接和群预告。

## GitHub placement

Recommended standalone repo:

```text
https://github.com/flicy/prepare-livestream-event
```

A "GrowthOS toolkit repo" would mean a future collection repo for multiple GrowthOS skills/tools. This first release is clearer as a standalone repo.

## Productization checklist

1. Final skill name, folder, frontmatter, README, and install command use `prepare-livestream-event`.
2. MIT license is included.
3. Real poster references are included under `assets/examples/real-cases/`.
4. Screenshots and real poster references are included in README.
5. Publishing adapter docs cover:
   - WeChat Official Account.
   - Xiaohongshu.
   - WeChat group.
   - WeChat Channels live reservation.
   - Xiaohongshu Live reservation.
6. Release checklist:
   - Validate `SKILL.md`.
   - Run script tests.
   - Verify README image links.
   - Rebuild zip.
7. Publish as a standalone GitHub repo first. Consider a plugin later only if account adapters become real tools.

## Inputs still needed

- Standard GrowthOS logo / wordmark file. Current asset is a draft logo reference.
- Optional public sample event folder with generated outputs.
- Browser-assisted workflow notes from the actual WeChat Official Account and Xiaohongshu accounts after the first real run.
