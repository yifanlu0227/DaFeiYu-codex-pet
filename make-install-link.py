#!/usr/bin/env python3
"""Print the documented desktop install link for this v2 pet."""

import argparse
from urllib.parse import urlencode, urlsplit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image_url", help="Public HTTPS URL of spritesheet.png")
    args = parser.parse_args()
    url = urlsplit(args.image_url)
    if url.scheme != "https" or not url.hostname or url.username or url.password:
        parser.error("image_url must be an absolute HTTPS URL without credentials")
    if any(char.isspace() for char in args.image_url):
        parser.error("image_url must not contain whitespace")
    query = urlencode({
        "name": "蓝色大肥鱼",
        "imageUrl": args.image_url,
        "description": "蓝发蓝眼的Q版小鲸鱼女仆，穿着深蓝白色女仆裙，带着蓬松长发和可爱的鲸鱼尾巴。",
        "spriteVersionNumber": "2",
    })
    print("codex://pets/install?" + query)


if __name__ == "__main__":
    main()
