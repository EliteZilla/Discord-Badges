<div align="center">

# ✦ Discord Badge Archive

### A modern, source-first catalog of Discord badges, experiments, app indicators, and historical profile icons.

**Accurate · Searchable · Structured · Community-maintained**

![Last Verified](https://img.shields.io/badge/last%20verified-2026--08--28-5865F2?style=flat-square)
![Badge Data](https://img.shields.io/badge/data-JSON-23A55A?style=flat-square)
![Contributions](https://img.shields.io/badge/contributions-welcome-F0B232?style=flat-square)
![License](https://img.shields.io/badge/code%20license-MIT-57F287?style=flat-square)

</div>

> [!IMPORTANT]
> **Last verified: August 28, 2026.** Discord changes badge availability and experiments over time. Every factual entry in the starter dataset includes a primary source and verification date.

## Explore

[Profile badges](#profile-badges) ·
[Experimental](#experimental-badges) ·
[Apps & developers](#app--developer-badges) ·
[Legacy](#legacy--historical-badges) ·
[Evolving badges](#evolving-badge-series) ·
[Data](#use-the-data) ·
[Contributing](#contributing)

## Why this archive exists

Most badge lists mix current badges, experiments, old screenshots, and outdated earning instructions together. This project separates the **visual archive** from the **verified data layer**, so facts can stay current even when artwork changes.

### Status language

| Label | Meaning |
|---|---|
| 🟢 **Active** | Current feature or badge |
| 🟣 **Experimental** | Discord says access is limited to an experiment |
| 🔴 **Legacy** | Historical badge that is no longer obtainable |
| ⚫ **Retired** | Feature was decommissioned or removed |

Availability is tracked separately because an active badge can still be restricted, automatic, program-based, or limited to eligible accounts.

---

## Profile Badges

| Badge | Classification | Status | Availability | How to get |
|---|---|---|---|---|
| **Discord Nitro** | `COMMON` | 🟢 Active | `OBTAINABLE` | Subscribe to an eligible Discord Nitro plan. |
| **Server Booster** | `COMMON` | 🟢 Active | `OBTAINABLE` | Actively boost a Discord server. |
| **Discord Quests** | `COMMON` | 🟢 Active | `OBTAINABLE` | Complete an eligible Quest. |
| **Orbs** | `COMMON` | 🟢 Active | `OBTAINABLE` | Purchase the badge with Orbs in the Orbs shop. |
| **Legacy Username** | `COMMON` | 🟢 Active | `LIMITED` | Available only to eligible accounts from the legacy username system. |
| **Bug Hunter** | `RARE` | 🟢 Active | `PROGRAM` | Participate actively in the Discord Testers community and meet its recognition criteria. |
| **Golden Bug Hunter** | `RARE` | 🟢 Active | `PROGRAM` | Reach the highest Bug Hunter level through exceptional participation in Discord Testers. |
| **Discord Staff** | `MYTHIC` | 🟢 Active | `RESTRICTED` | Reserved for Discord employees. |

> [!NOTE]
> Discord currently groups documented profile badges into **Common**, **Rare**, **Mythic**, and **Legacy** sections. This archive preserves those classifications where the official documentation provides one.

## Experimental Badges

| Badge | Classification | Status | Availability | How to get |
|---|---|---|---|---|
| **Gifting** | `EXPERIMENTAL` | 🟣 Experimental | `SELECTED-USERS` | Currently available only to selected users in Discord's experiment. |
| **Account Age** | `EXPERIMENTAL` | 🟣 Experimental | `SELECTED-USERS` | Currently available only to a small subset of desktop users. |
| **Streaming** | `EXPERIMENTAL` | 🟣 Experimental | `SELECTED-USERS` | Currently available only to a small subset of desktop users. |
| **Game Time** | `EXPERIMENTAL` | 🟣 Experimental | `SELECTED-USERS` | Currently available only to a small subset of desktop users. |
| **Game Variety** | `EXPERIMENTAL` | 🟣 Experimental | `SELECTED-USERS` | Currently available only to a small subset of desktop users. |

> [!WARNING]
> Experimental badges may change, expand, disappear, or never receive a general release.

## App & Developer Badges

| Badge | Classification | Status | Availability | How to get |
|---|---|---|---|---|
| **Active Developer** | `RETIRED` | ⚫ Retired | `UNOBTAINABLE` | No longer obtainable. |
| **Supports Commands** | `APP` | 🟢 Active | `AUTOMATIC` | Register at least one global application command for the app. |
| **Uses AutoMod** | `APP` | 🟢 Active | `AUTOMATIC` | Have at least 100 AutoMod rules across all servers for the app. |

> [!IMPORTANT]
> **Active Developer** is intentionally listed as retired. Discord Developer Support says the badge was decommissioned and previously displayed badges were removed.

## Legacy & Historical Badges

| Badge | Classification | Status | Availability | How to get |
|---|---|---|---|---|
| **HypeSquad Events** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **HypeSquad Bravery** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **HypeSquad Brilliance** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **HypeSquad Balance** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **Moderator Program Alumni** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **Early Supporter** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **Partnered Server Owner** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |
| **Last Meadow Online** | `LEGACY` | 🔴 Legacy | `UNOBTAINABLE` | No longer obtainable. |

## Evolving Badge Series

### Nitro

Discord documents an evolving Nitro profile badge for eligible Nitro subscriptions.

- Nitro Basic and Classic do **not** receive the evolving progression.
- The current milestone is selected automatically.
- Ending the eligible subscription resets progression when subscribing again.
- Users cannot manually select an older milestone.

Source: [Discord — Evolving Nitro Badges](https://support.discord.com/hc/en-us/articles/29136565881623-Evolving-Nitro-Badges)

### Server Booster

The Server Booster badge evolves with an uninterrupted boosting streak.

- It is tied to active Server Boosting.
- If a user is no longer boosting any server, Discord says the streak resets.
- With multiple boosted servers, the badge reflects the longest current streak/milestone.

Source: [Discord — Server Boosting FAQ](https://support.discord.com/hc/en-us/articles/360028038352-Server-Boosting-FAQ)

## Server Identity

Server Tags are tracked separately from achievement/profile badges. Discord describes them as a custom four-character tag paired with an icon that members can display on their profiles.

Source: [Discord — Server Tags](https://support.discord.com/hc/en-us/articles/31444248479639-Server-Tags)

## Use the Data

The source of truth lives in [`data/badges.json`](data/badges.json).

```python
import json

with open("data/badges.json", encoding="utf-8") as f:
    archive = json.load(f)

active = [b for b in archive["badges"] if b["status"] == "active"]

for badge in active:
    print(badge["name"], badge["primary_source"])
```

See [`docs/DATA_FORMAT.md`](docs/DATA_FORMAT.md) for the complete format.

## Artwork

Artwork is deliberately separated from badge facts.

```text
assets/
├── profile/
├── nitro/
├── boosts/
├── developers/
├── apps/
├── experimental/
├── legacy/
└── server/
```

> [!TIP]
> Add an asset only when its source and redistribution status are understood. Do not copy another badge repository's asset folder merely because it is publicly visible.

See [`assets/README.md`](assets/README.md).

## Repository Layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── assets/
├── data/
│   ├── badges.json
│   └── series.json
├── docs/
│   ├── CHANGELOG.md
│   ├── DATA_FORMAT.md
│   └── SOURCES.md
├── schema/
│   └── badges.schema.json
├── scripts/
│   └── validate_badges.py
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE.md
└── README.md
```

## Contributing

Corrections and discoveries are welcome. Contributions should include a trustworthy source, verification date, and asset provenance when artwork is included.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md), or use one of the repository's issue templates.

## Source Policy

Preferred evidence order:

1. Discord Help Center
2. Discord Developer Support
3. Discord Developer Documentation
4. Official Discord announcements/blog posts
5. Well-documented historical/community evidence when official material is unavailable

## Disclaimer

This is an independent community archive and is **not affiliated with, endorsed by, or sponsored by Discord Inc.** Discord and related marks belong to their respective owners.

## License

Repository **code and original written material** are released under the [MIT License](LICENSE). Third-party artwork, trademarks, screenshots, and externally sourced assets are not automatically relicensed by this repository. See [NOTICE.md](NOTICE.md).

---

<div align="center">

**Found something new? Open an issue or send a pull request.**

</div>
