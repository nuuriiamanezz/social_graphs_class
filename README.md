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
index.html          home page, list of posts
posts/week1.html     week 1: degree distributions + connected components
assets/css/style.css site styling
assets/img/          figures used in posts
data_1/              week-1 frozen data snapshot (edges + node roster)
week1.ipynb           the analysis notebook this week's post is drawn from
```

## Adding next week's post

1. Copy `posts/week1.html` as a starting template, swap in the new week's
   write-up and figures under `assets/img/`.
2. Add a new `<a class="post-link">` entry to the posts list in `index.html`.
3. Commit and push — GitHub Pages redeploys automatically.
