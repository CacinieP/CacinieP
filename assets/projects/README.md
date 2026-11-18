# Project visuals

The panels combine each product's actual colors with linked screenshots or
explicitly labelled content diagrams. They are presentation assets, not a new
application UI or a claim that a documented run was repeated for this profile.

| Asset | Evidence / image source | Type |
|---|---|---|
| `codetics-play.gif` / `codetics-scene.png` | https://codetics.vercel.app/ | Actual Act I gameplay capture: receiver animation, reception, semantic tagging, perspective and compression; 84 frames, 14 seconds, 2026-11-18 |
| `codetics-scenes.png` | https://codetics.vercel.app/ | Four actual scene captures: reception, semantic tagging, rhetoric room and Babel; no fabricated scene UI |
| `texada.png` | https://github.com/CacinieP/TeXada-the-Math-Agent/blob/main/docs/images/matrix-presets-preview.png | Repository screenshot |
| `studio.png` | https://github.com/CacinieP/TeXada-Studio-with-agentskills/blob/main/assets/studio-workspace.png | Repository screenshot; source README dates it 2026-11-04 |
| `launchgrid.png` | https://github.com/CacinieP/launchgrid/blob/main/doc/screenshots/apps.png | Repository screenshot |
| `slides.png` | https://github.com/CacinieP/slide-recipes/blob/main/docs/img/hero-commercial.jpg | Sample PPTX outputs; figures inside slides are example data |
| `lang.png` | https://caciniep.github.io/lang-master/ | Live app capture, 2026-11-18 |
| `sushi.png` | https://apps.apple.com/app/id6779997923 | App Store conveyor, timer, and home screenshots, obtained through the public iTunes lookup API |
| `doctor.png` | https://github.com/CacinieP/minicpm5-network-doctor/blob/main/docs/evidence/2026-09-18-2b-verbatim-example.md | Clearly labelled excerpt of a historical documented run |
| `video.png` | https://github.com/CacinieP/video2knowledge#readme | Workflow diagram, not an app screenshot |
| `*.svg` | Project descriptions linked in the folded README index | Content diagrams, not product screenshots |

Compositions: `preview/build-project-visuals.py` and
`preview/build-research-visuals.py`. The first builds `project-gallery.html`
from a directory of source captures named in its source. Screenshot each
`.poster` element at 1200 × 680 to reproduce the PNG panels. The second
directly writes the lightweight SVG content diagrams.

The Codetics recording is a presentation excerpt, not a completed-game acceptance run. Later acts were reached through the game’s visible skip controls; no completion is claimed.
