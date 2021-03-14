import json
from pprint import pprint
from typing import Union
from hammock import Hammock as hammock

versions: list[dict[str, Union[str, list[dict[str, str]]]]] = json.loads(hammock(
    "https://github.com/actions/python-versions/raw/main/versions-manifest.json").GET().text)

platforms: dict[str, list[str]] = {}

for version in versions:
    for file in version["files"]:
        platform_version = file["platform"] + (("-" + file["platform_version"])
                                               if file.get("platform_version") else "")
        platforms.setdefault(platform_version, []).append(version["version"])

for platform in platforms:
    print(platform)
    print(platforms[platform])
    print()
