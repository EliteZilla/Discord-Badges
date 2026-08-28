# Badge Artwork

The README now uses **real Discord badge artwork**, not generated placeholder graphics.

## How the visuals are handled

The current artwork is remote-linked from the public
[`dev-hoehle/discord-badges`](https://github.com/dev-hoehle/discord-badges) collection.

That lets the GitHub README show the actual badges while keeping third-party visual files
separate from this repository's MIT-licensed code and original writing.

Discord's official Help Center and Developer documentation remain the authority for badge
status, availability, and requirements.

## Local assets later

The data format supports both remote and local assets. If cleared local copies are added later,
set `asset` to the repository path and `asset_mode` to `local`.
