# Local profile preview

The README banner is rendered with Three.js, then exported to a six-second GIF.
GitHub displays the GIF; browsers that request reduced motion use the PNG.
The local preview includes a live WebGL scene with subtle pointer movement.

```bash
cd preview
npm install
npm run vendor
npm run render  # needs ffmpeg and Chrome; CHROME_PATH overrides the browser path
python3 -m pip install -r requirements.txt
python3 build.py
cd ..
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/preview/index.html`.
The preview approximates GitHub Markdown typography; GitHub controls the final rendering.
`hero.html` and `hero.js` are the original deterministic animation source.
Call `window.renderAt(seconds)` to render an exact frame in a 1200 × 420 viewport.
The cycle is six seconds, exported at 12 fps. Frame zero is the static poster.

Three.js 0.170.0 is MIT-licensed; it is installed as a dependency, not embedded in the GIF source.
The visual uses original procedural geometry, local system fonts, and no external textures.
