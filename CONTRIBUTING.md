# Contributing

Thanks for helping keep Discord Badge Archive accurate.

## Evidence first

Prefer Discord Help Center, Developer Support, Developer Documentation, and official announcements. Historical/community evidence is acceptable when official material no longer exists, but it must be labeled clearly.

## Adding or correcting a badge

Update `data/badges.json` with a stable ID, display name, category, classification, status, availability, an original summary, current/historical earning method, source URL, source type, and verification date.

Do not copy source-page wording. Summarize facts in your own words.

## Assets

Do not copy an image from another repository merely because it is publicly accessible. For contributed artwork, document the original source, owner/publisher, access date, modification history, and any relevant usage/licensing information.

Use lowercase kebab-case filenames such as `assets/profile/discord-quests.svg`.

## Validate

```bash
python scripts/validate_badges.py
```

GitHub Actions runs the same check for pushes and pull requests.
