# Data Format

`data/badges.json` is the canonical dataset.

| Field | Purpose |
|---|---|
| `id` | Stable lowercase identifier |
| `name` | Display name |
| `category` | Archive grouping |
| `classification` | Discord or archive classification |
| `status` | `active`, `experimental`, `legacy`, or `retired` |
| `obtainability` | More precise availability |
| `description` | Original archive summary |
| `how_to_obtain` | Current/historical earning method |
| `asset` | Optional local artwork path |
| `primary_source` | Best evidence URL |
| `source_type` | `official`, `community`, or `historical` |
| `last_verified` | ISO date |
| `notes` | Optional context |

Status and obtainability are separate because a badge can be active while restricted to staff, selected experiment users, or an official program.
