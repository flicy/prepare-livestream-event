#!/usr/bin/env python3
"""Normalize an event brief into the prepare-livestream-event schema."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict


DEFAULT_EVENT: Dict[str, Any] = {
    "series": "",
    "title": "",
    "subtitle": "",
    "time": "",
    "location": "",
    "organizers": [],
    "host": {"name": "", "bio": ""},
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
        "speaker_signup": "欢迎报名分享",
    },
    "links": {
        "live_reservation": "",
        "wechat_article": "",
        "xiaohongshu_post": "",
        "jike_post": "",
    },
    "assets": {
        "wechat_qr": "",
        "group_qr": "",
        "selected_poster": "",
    },
    "publishing_status": {
        "event_page": "draft",
        "poster": "pending_user_selection",
        "wechat_official": "not_started",
        "xiaohongshu": "not_started",
        "live_reservation": "not_started",
        "wechat_group": "not_started",
    },
}


def deep_merge(default: Any, value: Any) -> Any:
    if isinstance(default, dict) and isinstance(value, dict):
        merged = dict(default)
        for key, item in value.items():
            merged[key] = deep_merge(default.get(key), item)
        return merged
    if value is None:
        return default
    return value


def load_file(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)

    if path.suffix.lower() in {".yml", ".yaml"}:
        try:
            import yaml  # type: ignore
        except ImportError as exc:
            raise SystemExit(
                "YAML input requires PyYAML. Install it or provide JSON input."
            ) from exc
        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            raise SystemExit("YAML input must contain an object at the top level.")
        return data

    raise SystemExit("Input must be .json, .yml, or .yaml")


def slugify(title: str) -> str:
    ascii_words = re.findall(r"[A-Za-z0-9]+", title.lower())
    if ascii_words:
        return "-".join(ascii_words[:8])
    digest = hashlib.sha1(title.encode("utf-8")).hexdigest()[:8]
    return f"event-{digest}"


def normalize(payload: Dict[str, Any]) -> Dict[str, Any]:
    event = payload.get("event", payload)
    if not isinstance(event, dict):
        raise SystemExit("Event payload must be an object.")

    normalized = deep_merge(DEFAULT_EVENT, event)
    normalized["organizers"] = ensure_list(normalized.get("organizers"))
    for key in ["goals", "audience", "questions", "agenda", "guests"]:
        normalized[key] = ensure_list(normalized.get(key))
    normalized["slug"] = normalized.get("slug") or slugify(normalized.get("title", "event"))

    return {"event": normalized}


def ensure_list(value: Any) -> list:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    return [value]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Event JSON/YAML file.")
    parser.add_argument("-o", "--output", type=Path, help="Write JSON to this path.")
    args = parser.parse_args()

    data = normalize(load_file(args.input))
    output = json.dumps(data, ensure_ascii=False, indent=2)

    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
