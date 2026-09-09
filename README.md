# WebCrawl

Group site for DTU course 02805 *Social Graphs and Interactions*.

Every week we take the shared Marvel Comics superheroes hyperlink network (303
characters from Wikipedia's [Category:Marvel Comics
superheroes](https://en.wikipedia.org/wiki/Category:Marvel_Comics_superheroes),
edges harvested from the wiki-source `[[Page name]]` links) and one week's
tools, and write up whatever we find.

Live site: `https://<github-username>.github.io/social_graphs_class/`
(enable in **Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**)

## Structure

```
index.html               home page, list of posts, EKG lifeline
explore.html              search + interactive graph over all 303 characters
posts/week1.html          week 1: degree distributions + connected components
assets/css/style.css      site styling
assets/img/               figures used in posts + favicon/OG image
assets/data/explore_data.json  per-character stats + layout + edges, powers explore.html
assets/favicon.svg        browser-tab icon
data_1/                   week-1 frozen data snapshot (edges + node roster)
week1.ipynb                the analysis notebook this week's post is drawn from
export_explore_data.py    (not in repo yet — regenerate assets/data/explore_data.json
                           from graph.pkl/extended.pkl if the underlying analysis changes)
```

`explore.html` loads D3 from a CDN (`cdn.jsdelivr.net`) and fetches
`assets/data/explore_data.json` — both need real internet + same-origin serving
to work, so it won't render correctly opened as a bare `file://` path; test it
through `python3 -m http.server` locally, or just check it live on GitHub Pages.

## Adding next week's post

1. Copy `posts/week1.html` as a starting template, swap in the new week's
   write-up and figures under `assets/img/`.
2. In `index.html`, replace that week's `<div class="post-placeholder">…</div>`
   with an `<a class="post-link" href="posts/weekN.html">…</a>` entry (same
   markup shape as the week 1 entry) so it becomes clickable.
3. In `index.html`, update the lifeline (the EKG-style `<svg class="lifeline-svg">`):
   - Replace the `.life-pulse` path's `d` attribute and the `.life-dot`'s `cx`
     with the values for the week you just finished, from the table below.
   - Move `class="done"` up to that week's `<text>` label, and `class="next"`
     to the following week's label (drop it entirely after week 8).
   - Bump the `N / 8 weeks` count.
4. Commit and push — GitHub Pages redeploys automatically.

Pulse path `d` / dot `cx` per completed-weeks count (copy the row for how many
weeks are now done):

| weeks done | `.life-pulse` `d` | `.life-dot` `cx` |
|---|---|---|
| 2 | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60` | `200` |
| 3 | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60 L215,60 L225,15 L235,105 L245,60 L300,60` | `300` |
| 4 | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60 L215,60 L225,15 L235,105 L245,60 L300,60 L315,60 L325,15 L335,105 L345,60 L400,60` | `400` |
| 5 | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60 L215,60 L225,15 L235,105 L245,60 L300,60 L315,60 L325,15 L335,105 L345,60 L400,60 L415,60 L425,15 L435,105 L445,60 L500,60` | `500` |
| 6 | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60 L215,60 L225,15 L235,105 L245,60 L300,60 L315,60 L325,15 L335,105 L345,60 L400,60 L415,60 L425,15 L435,105 L445,60 L500,60 L515,60 L525,15 L535,105 L545,60 L600,60` | `600` |
| 7 | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60 L215,60 L225,15 L235,105 L245,60 L300,60 L315,60 L325,15 L335,105 L345,60 L400,60 L415,60 L425,15 L435,105 L445,60 L500,60 L515,60 L525,15 L535,105 L545,60 L600,60 L615,60 L625,15 L635,105 L645,60 L700,60` | `700` |
| 8 (done!) | `M0,60 L15,60 L25,15 L35,105 L45,60 L100,60 L115,60 L125,15 L135,105 L145,60 L200,60 L215,60 L225,15 L235,105 L245,60 L300,60 L315,60 L325,15 L335,105 L345,60 L400,60 L415,60 L425,15 L435,105 L445,60 L500,60 L515,60 L525,15 L535,105 L545,60 L600,60 L615,60 L625,15 L635,105 L645,60 L700,60 L715,60 L725,15 L735,105 L745,60 L800,60` | `800` |

At 8/8, also remove the `.life-dot` circle entirely (or drop its pulse
animation) so the lifeline reads as finished rather than still "searching."
