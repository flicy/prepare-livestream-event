#!/usr/bin/env python3
"""Print platform poster export targets and generation canvas guidance."""

from __future__ import annotations

import json
import sys


ASSETS = [
    {
        "id": "wechat-cover",
        "platform": "wechat_official",
        "label": "公众号头条封面",
        "target_px": [900, 383],
        "ratio": "2.35:1",
        "preferred_generation_px": [912, 384],
        "fallback_generation_px": [1536, 1024],
        "safe_area": "center 383x383 square",
        "notes": "Keep title and core information inside the center square crop.",
    },
    {
        "id": "wechat-secondary-cover",
        "platform": "wechat_official",
        "label": "公众号次条小封面",
        "target_px": [200, 200],
        "ratio": "1:1",
        "preferred_generation_px": [1024, 1024],
        "fallback_generation_px": [1024, 1024],
        "safe_area": "full square",
        "notes": "Use a short title or symbol; avoid dense text.",
    },
    {
        "id": "wechat-inline-horizontal",
        "platform": "wechat_official",
        "label": "公众号正文横版海报",
        "target_px": [900, 500],
        "ratio": "9:5",
        "preferred_generation_px": [1440, 800],
        "fallback_generation_px": [1536, 1024],
        "safe_area": "center 80%",
        "notes": "Good for article body and agenda section.",
    },
    {
        "id": "wechat-inline-vertical",
        "platform": "wechat_official",
        "label": "公众号正文竖版海报",
        "target_px": [750, 1334],
        "ratio": "9:16",
        "preferred_generation_px": [752, 1344],
        "fallback_generation_px": [1024, 1536],
        "safe_area": "center 85%",
        "notes": "Use Figma for final text and QR placement.",
    },
    {
        "id": "wechat-inline-square",
        "platform": "wechat_official",
        "label": "公众号正文方海报",
        "target_px": [800, 800],
        "ratio": "1:1",
        "preferred_generation_px": [1024, 1024],
        "fallback_generation_px": [1024, 1024],
        "safe_area": "center 80%",
        "notes": "Good for QR and CTA.",
    },
    {
        "id": "xhs-cover",
        "platform": "xiaohongshu",
        "label": "小红书主推封面海报",
        "target_px": [1080, 1440],
        "ratio": "3:4",
        "preferred_generation_px": [1088, 1440],
        "fallback_generation_px": [1024, 1536],
        "safe_area": "center 88%",
        "notes": "Crop from preferred canvas to exact 1080x1440.",
    },
    {
        "id": "xhs-cover-hd",
        "platform": "xiaohongshu",
        "label": "小红书高清备选封面",
        "target_px": [1242, 1660],
        "ratio": "3:4",
        "preferred_generation_px": [1248, 1664],
        "fallback_generation_px": [1024, 1536],
        "safe_area": "center 88%",
        "notes": "Use when the platform benefits from a larger upload.",
    },
    {
        "id": "xhs-square",
        "platform": "xiaohongshu",
        "label": "小红书方形活动海报",
        "target_px": [1080, 1080],
        "ratio": "1:1",
        "preferred_generation_px": [1088, 1088],
        "fallback_generation_px": [1024, 1024],
        "safe_area": "center 85%",
        "notes": "Useful for QR, venue, or product-focused posts.",
    },
    {
        "id": "xhs-horizontal",
        "platform": "xiaohongshu",
        "label": "小红书横版备选",
        "target_px": [1200, 900],
        "ratio": "4:3",
        "preferred_generation_px": [1200, 912],
        "fallback_generation_px": [1536, 1024],
        "safe_area": "center 85%",
        "notes": "Use sparingly; 3:4 is preferred.",
    },
]


def main() -> int:
    print(
        json.dumps(
            {
                "policy": "Export exact target sizes after generation. Use fallback_generation_px when the image API cannot produce preferred_generation_px.",
                "assets": ASSETS,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
