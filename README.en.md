# Prepare Livestream Event · Livestream Launch Skill

[中文](README.md) | **English**

> One brief, one launch package, publish only after approval.
> 一个主题，一套素材，一次确认后再发布。

A Codex Skill for preparing online livestream event launches. It turns an event brief, Notion page, or draft copy into an event page, five poster directions, WeChat Official Account and Xiaohongshu drafts, live reservation link tracking, and WeChat group announcements.

It is not an autoposting bot. Think of it as an event-ops partner: prepare the content, visuals, copy, and publishing checklist first; ask the human to confirm; publish only after approval.

Born from the real GrowthOS / Coding GrowthTALK event preparation workflow.

![overview](examples/overview.png)

Local showcase page: open `examples/showcase.html` directly in your browser.  
Launch copy examples: see `examples/promo-copy.md`.

## What's Inside

- **Event page** — Normalizes topic, time, guests, agenda, audience, CTA, and links into one structure.
- **Five poster directions** — Prompt packs for Image 2.5 or the current image model available in your environment.
- **Platform size guide** — WeChat cover, article posters, Xiaohongshu 3:4 cover, square, and horizontal fallback.
- **Copy templates** — Drafts for WeChat Official Account, Xiaohongshu, warm-up messages, and final group announcements.
- **Approval gates** — Draft creation can be assisted, but public publishing, live reservation creation, and group sending require explicit human approval.

## Examples

| Poster directions | Real GrowthOS cases |
|---|---|
| ![](examples/poster-directions.png) | ![](examples/real-growthos-cases.png) |

The default visual language follows current GrowthOS event posters: paper collage, orange-black contrast, oversized titles, live-time rows, co-organizer lines, practical discussion bullets, host cards, and QR-driven CTAs.

To adapt it to your community, edit `references/growthos-brand.md` and `references/copywriting-templates.md`.

## Install

Works with AI agents that support the `SKILL.md` convention. For Codex:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/flicy/prepare-livestream-event.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/prepare-livestream-event"
```

Restart Codex, then ask:

```text
Use $prepare-livestream-event to prepare a livestream event launch package from this activity brief.
```

## Quick Start

```bash
python3 scripts/normalize_event.py templates/event-template.json -o /tmp/event.json
python3 scripts/plan_image_sizes.py > /tmp/poster-sizes.json
python3 scripts/build_poster_prompts.py /tmp/event.json -o /tmp/poster-prompts.json
```

Use `/tmp/poster-prompts.json` with your image generation workflow. After choosing a direction, refine final Chinese typography, QR codes, and safe areas in Figma or your preferred design tool.

## Structure

```text
.
├── README.md
├── README.en.md
├── SKILL.md
├── LICENSE.md
├── agents/
│   └── openai.yaml
├── examples/
│   ├── overview.png
│   ├── overview-editable.svg
│   ├── showcase.html
│   ├── promo-copy.md
│   ├── poster-directions.png
│   └── real-growthos-cases.png
├── templates/
│   ├── event-template.json
│   └── event-template.yml
├── references/
│   ├── event-schema.md
│   ├── growthos-brand.md
│   ├── poster-sizes.md
│   ├── copywriting-templates.md
│   └── publishing-adapters.md
└── scripts/
    ├── normalize_event.py
    ├── plan_image_sizes.py
    └── build_poster_prompts.py
```

`examples/` is public visual context for humans. `templates/`, `references/`, and `scripts/` are the working materials used by the skill.

## Customize

Most teams start here:

- `templates/event-template.yml`: your recurring event fields.
- `references/growthos-brand.md`: palette, visual tone, poster style.
- `references/copywriting-templates.md`: WeChat, Xiaohongshu, and group-message voice.
- `references/poster-sizes.md`: adjust if your channels use different dimensions.
- `examples/`: replace with real cases from your own community.

## Report Bad Outputs

Useful bad cases:

- Posters do not match the target community style.
- Chinese titles are too crowded or unreadable.
- WeChat covers ignore the center-square safe area.
- Xiaohongshu titles are not strong enough.
- Copy feels generic, hollow, or too AI-like.
- QR codes, live reservation links, and article links are not associated clearly.

Do not include private QR codes, group links, account screenshots, or unpublished event details in public issues unless you explicitly intend to share them.

## License

MIT License. See [LICENSE.md](LICENSE.md).
