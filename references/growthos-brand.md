# GrowthOS Brand Reference

Use this as the default event visual system. For another community, replace the palette, motifs, tone, and CTA language while keeping the workflow intact.

## Palette

Extracted from `https://start.growthos.cn/`:

| Token | Color | Use |
| --- | --- | --- |
| `bg` | `#FAFAF9` | warm page background |
| `bg_warm` | `#F5F3EF` | secondary background |
| `surface` | `#F0EEEB` | cards, panels, dividers |
| `ink` | `#1A1A1A` | primary text |
| `ink_secondary` | `#52525B` | body text |
| `accent` | `#E85D3A` | primary highlight, buttons, badges |
| `accent_hover` | `#D14E2E` | deeper accent |
| `blue` | `#3B82F6` | AI/system note |
| `orange` | `#F59E0B` | energy, highlights |
| `pink` | `#EC4899` | social/community note |
| `teal` | `#14B8A6` | collaboration note |
| `green` | `#22C55E` | growth/success note |
| `flower` | `#F43F5E` | small reward/social signal |

## Typography

- Chinese: `Noto Sans SC`, `PingFang SC`, or system sans.
- English/code accents: `Inter` and `JetBrains Mono`.
- Prefer strong hierarchy: short title, clear subtitle, small factual metadata.
- Avoid dense body text on posters. Put long descriptions in the article page.

## Logo status

Current draft asset:

- `assets/brand/growthos-logo-draft.png`

This file is a temporary reference, not a finalized brand standard. Keep a TODO to replace it with an approved GrowthOS logo / wordmark package before a polished public release.

## Visual motifs

- Warm off-white background, thin grid, subtle system lines.
- Orange-red highlight blocks or underline marks.
- Builder/community language: AI Builder, Coding, Growth, Agent, FDE, Demo to Delivery.
- Modular panels, small tags, status indicators, live badge.
- QR areas should be stable rectangular placeholders, not decorative elements.

## Real poster references

The examples in `assets/examples/real-cases/` show the current GrowthOS activity poster language:

- `coding-growthtalk-issue-9.png`: calmer collage layout, large black title, orange brush accents, long-form activity detail, host card, two QR CTAs.
- `coding-growthtalk-agent-fde.png`: bolder hand-drawn social cover, oversized title, robot/marker-style decoration, discussion bullets, target audience card, QR CTA band.

Shared patterns to preserve:

- 3:4 vertical master poster close to `1080 x 1440`.
- Warm paper/collage texture with black and GrowthOS orange-red.
- Strong title first, then time/place, organizer line, discussion bullets, host, and QR CTA.
- Public-builder tone: practical, energetic, "build in public", not corporate brochure.

## Tone

- Practical, builder-oriented, warm, direct.
- Emphasize real business usage, shared practice, and community co-creation.
- Avoid empty hype. Prefer "边聊边建连", "从 Demo 到交付", "真实业务现场", "一起拆解".

## How to adapt for another community

Replace these items first:

1. Palette: change the table above.
2. Typography: define the community's preferred Chinese and English fonts.
3. Motifs: name 3-5 recurring visual symbols or layout habits.
4. Tone: write 5-8 phrases that sound like the community.
5. CTA: replace WeChat/QR language with the community's own channels.

Then rerun `scripts/build_poster_prompts.py` after updating the brand summary in the prompt or reference.
