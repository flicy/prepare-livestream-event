---
name: prepare-livestream-event
description: Use when preparing online livestream event launches for GrowthOS, Coding GrowthTALK, AI builder talks, or similar recurring live sessions, including event content pages, image-generation poster assets, Figma refinement, browser-assisted WeChat Official Account drafts, Xiaohongshu drafts, WeChat Channels or Xiaohongshu live reservation links, and WeChat group announcements.
---

# Prepare Livestream Event

## Overview

Use this skill to turn an online livestream event idea or source page into a reusable launch package: structured event page, five poster directions, platform-specific copy, browser-assisted draft plan, live reservation links, and final group announcement.

Keep the workflow semi-automatic. Create drafts and assets aggressively, but never publish a public post, create a live reservation under the user's account, or send a WeChat group message without explicit approval.

## Workflow

1. **Create the event content page first**
   - Source from the user's brief, pasted content, Notion/page URL, existing Markdown, or `templates/event-template.yml`.
   - If a referenced URL is unavailable, say that and use the pasted content as the source of truth.
   - Normalize the event into the schema in `references/event-schema.md`.
   - Create or update a content page before poster work. Prefer Notion when the user provides access; otherwise create a Markdown page in the working folder.

2. **Prepare the brand and poster brief**
   - Default to the GrowthOS brand in `references/growthos-brand.md`.
   - If the user provides another livestream brand/site/attachment, inspect it and update the brand brief before generating.
   - Run `scripts/plan_image_sizes.py` to choose target exports and generation canvases.
   - Run `scripts/build_poster_prompts.py <event-file>` to create the five-poster prompt pack.

3. **Generate five poster directions**
   - Use Image 2.5 if available, otherwise use the current OpenAI image model available in the environment, such as `gpt-image-2` when supported.
   - Generate five visually distinct directions:
     `growthos-minimal`, `agent-architecture`, `global-livestream`, `fde-enterprise`, and `xiaohongshu-bold`.
   - Do not rely on the image model for dense Chinese text. Keep image-generation text minimal, then use Figma or a layout tool for final typography, QR codes, and safe-area adjustments.
   - Export at least the Xiaohongshu 3:4 cover and WeChat cover first. Derive secondary sizes after a direction is selected.

4. **Refine in Figma when needed**
   - If the user asks for Figma or provides a Figma URL, use the Figma skill/tooling available in the session.
   - Convert the chosen poster direction into editable layers: background, title, subtitle, time/place, organizer line, QR areas, and footer.
   - Respect platform safe areas from `references/poster-sizes.md`, especially the WeChat cover center-square crop.

5. **Stop for user confirmation**
   - Show or summarize all poster options.
   - Ask the user to choose the winning direction and approve the public copy direction.
   - Do not continue to public posting or group sending before this gate.

6. **Draft platform copy**
   - Use `references/copywriting-templates.md` to produce:
     WeChat group warm-up, WeChat Official Account article, Xiaohongshu post, optional Jike short post, and final group announcement.
   - Keep the tone practical, builder-oriented, and community-first.
   - Include placeholders for QR codes, reservation links, article links, and Xiaohongshu links until they exist.

7. **Create drafts and live reservation links**
   - Default to browser-assisted drafts for WeChat Official Account and Xiaohongshu.
   - Fall back to a manual export package if account access or browser automation is unavailable.
   - Prioritize WeChat Channels and Xiaohongshu Live for live reservation links.
   - Create the live reservation link only after confirming the target live platform and account.
   - Write all generated links back to the event content page.

8. **Generate the final group announcement**
   - After links are associated, produce one short group message with the topic, time, location, live reservation link, and article/post links.
   - Ask for final confirmation before sending to any WeChat group.

## Expected Output Folder

For each event, create a folder named with the event date and slug:

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

## Resource Map

- `references/event-schema.md`: required event fields and publishing status structure.
- `references/growthos-brand.md`: default brand palette, tone, visual motifs, and instructions for adapting to another community.
- `references/poster-sizes.md`: WeChat, Xiaohongshu, and Jike poster/export sizes.
- `references/copywriting-templates.md`: copy templates for posts and group messages.
- `references/publishing-adapters.md`: automation boundaries and platform adapter checklist.
- `templates/event-template.yml`: editable human-readable event brief template.
- `templates/event-template.json`: dependency-free event template for scripts and automation.
- `examples/`: public overview images, poster directions, and real GrowthOS poster references.
- `scripts/normalize_event.py`: normalize JSON/YAML event input.
- `scripts/plan_image_sizes.py`: output target dimensions and generation/crop guidance.
- `scripts/build_poster_prompts.py`: generate the five-poster prompt pack.

## Safety Rules

- Never publish, schedule, reserve, or send from a real account without explicit user approval in the current conversation.
- Treat QR codes, private groups, access tokens, cookies, and account sessions as sensitive.
- If an API or connector is unavailable, produce a manual publishing package instead of pretending automation happened.
- If platform rules, API capabilities, or model parameters may have changed, verify current official documentation before implementation.
