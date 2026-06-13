#!/usr/bin/env python3
"""Generate five image-generation poster prompts for an event brief."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from normalize_event import load_file, normalize  # noqa: E402


STYLE_DIRECTIONS = [
    {
        "style_id": "growthos-minimal",
        "name": "GrowthOS warm minimal",
        "visual": "warm off-white background, black typography, orange-red accent blocks, thin grid, small live badge, clean modular layout",
    },
    {
        "style_id": "agent-architecture",
        "name": "Agent architecture system map",
        "visual": "diagram-like AI agent workflow, nodes and connectors, subtle code-grid texture, precise product-builder mood",
    },
    {
        "style_id": "global-livestream",
        "name": "AI overseas livestream salon",
        "visual": "global collaboration energy, abstract map lines, livestream interface hints, warm community atmosphere",
    },
    {
        "style_id": "fde-enterprise",
        "name": "FDE enterprise deployment",
        "visual": "business deployment scene, system integration layers, enterprise workflow cards, calm high-trust palette",
    },
    {
        "style_id": "xiaohongshu-bold",
        "name": "Xiaohongshu bold cover",
        "visual": "high-impact 3:4 mobile cover, oversized title zone, strong contrast, clear topic tags, social-media native composition",
    },
]

BRAND = {
    "palette": "#FAFAF9 warm background, #1A1A1A ink, #E85D3A orange-red accent, secondary #3B82F6 blue, #14B8A6 teal, #22C55E green, #EC4899 pink",
    "typography": "Noto Sans SC for Chinese, Inter for English, JetBrains Mono for small code labels",
    "tone": "practical AI builder community, warm, direct, not hype-driven",
}


def compact_list(items: List[str], limit: int = 4) -> str:
    return "；".join(str(item) for item in items[:limit] if str(item).strip())


def build_prompt(event: Dict, style: Dict) -> str:
    title = event.get("title", "")
    subtitle = event.get("subtitle", "")
    series = event.get("series", "")
    time = event.get("time", "")
    location = event.get("location", "")
    organizers = " x ".join(event.get("organizers", []))
    questions = compact_list(event.get("questions", []), 3)

    return f"""Create an event poster concept for Image 2.5 if available, otherwise the current OpenAI image model.

Style direction: {style['name']} - {style['visual']}.
Brand palette: {BRAND['palette']}.
Typography guidance: {BRAND['typography']}.
Tone: {BRAND['tone']}.

Poster content:
- Series: {series}
- Main title: {title}
- Subtitle: {subtitle}
- Time and place: {time} · {location}
- Organizers: {organizers}
- Key discussion cues: {questions}

Composition requirements:
- Generate a polished visual background and layout direction for a Chinese AI builder community event.
- Leave clean editable zones for final Chinese typography, QR codes, and platform-specific safe-area adjustment in Figma.
- Use only short readable text in the generated image; final dense text will be typeset later.
- Avoid generic stock-photo feeling, unreadable fake text, dark blurry atmosphere, and overused purple-blue gradients.
"""


def build_prompt_pack(event_file: Path) -> Dict:
    normalized = normalize(load_file(event_file))
    event = normalized["event"]
    return {
        "event_summary": {
            "series": event.get("series", ""),
            "title": event.get("title", ""),
            "time": event.get("time", ""),
            "location": event.get("location", ""),
            "slug": event.get("slug", ""),
        },
        "model_hint": "Use Image 2.5 if available; otherwise use the current OpenAI image model available in the environment, such as gpt-image-2 when supported.",
        "recommended_first_export": "xhs-cover 1080x1440 and wechat-cover 900x383",
        "poster_variants": [
            {
                "style_id": style["style_id"],
                "name": style["name"],
                "prompt": build_prompt(event, style),
            }
            for style in STYLE_DIRECTIONS
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("event_file", type=Path, help="Normalized or raw event JSON/YAML.")
    parser.add_argument("-o", "--output", type=Path, help="Write prompt pack JSON here.")
    args = parser.parse_args()

    pack = build_prompt_pack(args.event_file)
    output = json.dumps(pack, ensure_ascii=False, indent=2)

    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
