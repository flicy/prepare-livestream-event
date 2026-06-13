# Publishing Adapters

Use the best available adapter in the current environment. This skill defaults to browser-assisted draft creation for WeChat Official Account and Xiaohongshu, then asks the user to approve before publishing.

## Adapter order

1. Browser-assisted draft creation with the user's logged-in account.
2. Manual publishing package with Markdown, images, and checklist.
3. Official API or connected app tool, only when account access and API capability are confirmed.

## WeChat Official Account

Outputs to prepare:

- Title.
- Author/source line.
- Summary.
- Cover image.
- Article body with inline poster, agenda, CTA, QR placeholders, and live reservation link.

Automation notes:

- Use browser-assisted editor by default when the user has authorized access.
- Create a draft first.
- Ask for approval before publish or schedule.
- After publish, record the article URL in `event.links.wechat_article`.

## Xiaohongshu

Outputs to prepare:

- 3-5 title options.
- Cover image.
- Body copy.
- Topic tags.
- Live reservation link or platform-safe CTA.

Automation notes:

- Default to browser-assisted draft creation or manual package.
- Ask before posting.
- After publish, record the post URL in `event.links.xiaohongshu_post`.

## Live reservation

Prioritize WeChat Channels and Xiaohongshu Live. Ask which platform to use unless the event page already specifies it.

Priority destinations:

- WeChat Channels.
- Xiaohongshu Live.

Other possible destinations:

- Bilibili.
- Zoom/Tencent Meeting.
- Custom landing page.

Create the reservation link only after confirming platform, account, date/time, title, and cover. Record it in `event.links.live_reservation`.

## WeChat group announcement

Never send directly without explicit user approval.

Prepare:

- Warm-up message before links exist.
- Final announcement after live/article/post links exist.
- Optional short reminder message on event day.

If no WeChat automation tool is available, provide copy-ready text.

## Publishing status file

Keep a `publishing-status.json` with:

```json
{
  "wechat_official": {
    "status": "draft",
    "draft_url": "",
    "public_url": "",
    "notes": ""
  },
  "xiaohongshu": {
    "status": "not_started",
    "draft_url": "",
    "public_url": "",
    "notes": ""
  },
  "live_reservation": {
    "status": "not_started",
    "platform": "",
    "url": "",
    "notes": ""
  },
  "wechat_group": {
    "status": "needs_user_confirmation",
    "target_group": "",
    "message": "",
    "notes": ""
  }
}
```
