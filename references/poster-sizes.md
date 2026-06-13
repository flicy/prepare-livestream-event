# Poster Sizes

Use these exact export sizes for platform deliverables. If the image model cannot generate the exact target size, generate a nearby high-resolution canvas and crop/export precisely in Figma or another layout tool.

## Confirmation note

These are production recommendations for common WeChat Official Account and Xiaohongshu publishing workflows, last reviewed on 2026-06-11. Platform editors may change crop behavior, compression, or preview surfaces. Always do a final upload preview in the platform backend before publishing.

The included real GrowthOS examples are `1086 x 1448`, which is effectively a 3:4 vertical poster and works as a Xiaohongshu-style cover source. Use the same visual master to derive WeChat article inline posters and separate WeChat cover crops.

## WeChat Official Account

| Asset | Target px | Notes |
| --- | ---: | --- |
| Headline cover | `900 x 383` | Main info must fit the center `383 x 383` safe square for sharing crops. |
| Secondary cover | `200 x 200` | Square thumbnail. Keep title short. |
| Inline horizontal poster | `900 x 500` | Good for article body. |
| Inline vertical poster | `750 x 1334` | Use when the article needs a full event poster. |
| Inline square poster | `800 x 800` | Good for QR-heavy CTA. |

Prefer JPG under 5 MB for WeChat images.

Recommended production set:

- Required: `900 x 383` headline cover with center-square safe area.
- Required when publishing a secondary article: `200 x 200`.
- Recommended for article body: one vertical poster (`750 x 1334` or 3:4-derived crop) plus one square QR/CTA image if needed.

## Xiaohongshu

| Asset | Target px | Notes |
| --- | ---: | --- |
| Main cover | `1080 x 1440` | Preferred 3:4 activity cover. |
| High-res cover | `1242 x 1660` | Optional, same ratio family. |
| Square poster | `1080 x 1080` | Use for product/venue/QR-centered posts. |
| Horizontal image | `1200 x 900` | Use sparingly. |

Keep all images in the same post at the same ratio unless there is a specific reason to mix formats.

Recommended production set:

- Main: `1080 x 1440` 3:4 cover.
- Optional high-res: `1242 x 1660` when the workflow benefits from larger uploads.
- Keep the first image as the strongest title cover; use the rest for agenda, audience, host, and QR/CTA details.

## Jike

Jike accepts flexible image ratios. Reuse the Xiaohongshu 3:4 cover and WeChat square image unless the user requests a separate layout.

## Generation and export guidance

- Keep generated artwork slightly larger than the target export when possible, then crop down.
- Use final layout tooling for all dense text, QR codes, platform-safe margins, and article-specific cover crops.
- `scripts/plan_image_sizes.py` outputs preferred generation canvases and fallback generation sizes for this workflow.
- Always check readability on a phone-sized preview before publishing.
