# Event Schema

Normalize every event into this shape before generating posters or copy. Keep the event page as the source of truth after links and publishing status change.

## Required fields

```json
{
  "event": {
    "series": "Coding GrowthTALK",
    "title": "AI+Agent上岗：从 Agent Demo 到真正落地",
    "subtitle": "FDE 到底解决了什么问题？",
    "time": "每周五晚 19:00-21:00",
    "location": "线上直播",
    "organizers": ["GrowthOS", "Datawhale", "launch 100"],
    "host": {
      "name": "Chris（崔莹）",
      "bio": "Data PM｜AI Builder｜GrowthOS 主理人"
    },
    "topic_description": "",
    "goals": [],
    "audience": [],
    "questions": [],
    "agenda": [],
    "guests": [],
    "community_intro": "",
    "cta": {
      "follow_wechat": "扫码关注公众号",
      "join_group": "扫码进群",
      "speaker_signup": "欢迎报名分享"
    },
    "links": {
      "live_reservation": "",
      "wechat_article": "",
      "xiaohongshu_post": "",
      "jike_post": ""
    },
    "assets": {
      "wechat_qr": "",
      "group_qr": "",
      "selected_poster": ""
    },
    "publishing_status": {
      "event_page": "draft",
      "poster": "pending_user_selection",
      "wechat_official": "not_started",
      "xiaohongshu": "not_started",
      "live_reservation": "not_started",
      "wechat_group": "not_started"
    }
  }
}
```

## Status values

Use consistent values so automation can resume safely:

- `not_started`
- `draft`
- `needs_user_confirmation`
- `approved`
- `published`
- `skipped`
- `blocked`

## Event page checklist

The content page must include:

- Topic, date/time, location, organizers.
- One-paragraph public description.
- Host and guest introduction.
- Goals, target audience, core questions, and agenda.
- QR placeholders and final links.
- Publishing status table with owner/tool/last updated notes.

## Link association rule

After creating a live reservation link, write it into:

- WeChat Official Account draft/article.
- Xiaohongshu draft/post.
- Final WeChat group announcement.
- Event content page `links.live_reservation`.

After publishing a platform post, write the post URL back to the event page and regenerate the final group announcement.
