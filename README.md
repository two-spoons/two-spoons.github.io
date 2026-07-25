# two_spoons

The blog at [twospoons.online](https://twospoons.online). Jekyll, built and
deployed by GitHub Actions on every push to `master`.

## Writing a post

Drop a `.md` or `.txt` file into `inbox/` and push. That's it.

```
inbox/some thoughts on dune.txt
      │
      ▼  Publish inbox workflow
_posts/2026-07-25-some-thoughts-on-dune.md   →   /blog/2026/some-thoughts-on-dune/
```

The workflow timestamps it, gives it a slug, adds the front matter, moves it to
`_posts/`, deletes it from `inbox/`, and redeploys the site. Posts sort
themselves by date. You can do this from GitHub's web UI on your phone —
**Add file → Create new file**, name it, paste, commit.

What gets inferred:

| | |
|---|---|
| **Title** | the first `# heading`; else the first line if it reads like a title; else the filename |
| **Date** | the time you committed the file. Prefix the filename with `2026-07-25-` to set it yourself |
| **Category** | `writing`. Drop the file in `inbox/coding/` to file it under `coding` instead |
| **Author** | `two_spoons` |

Write your own front matter if you want control — it's preserved, and only the
missing keys are filled in.

### From the terminal

```bash
bin/new-post "on the difficulty of naming things"   # creates the file in _posts/
bin/new-post "a bug i found" coding                 # ...under a category
pbpaste | bin/new-post                              # ...from the clipboard
bin/publish-inbox                                   # process inbox/ locally
bin/publish-inbox --check                           # validate, change nothing
```

`--check` also runs in CI before every build, so a post Jekyll would silently
skip (a filename with spaces, say) fails the build instead of quietly
disappearing.

## Running it locally

Needs Ruby 3.1+ and ImageMagick.

```bash
bundle install
bundle exec jekyll serve
```

Then http://127.0.0.1:4000.

## Layout of the repo

```
_posts/          published posts, YYYY-MM-DD-slug.md
inbox/           drop zone — anything here becomes a post
_pages/          about (/), writing, casting, coding, 404
_layouts/        about, page, post, default, archive-{year,tag,category}
_includes/       head, header, footer, social, metadata, figure, pagination,
                 related_posts, giscus, scripts/
_sass/           Dracula theme lives in _base.scss / _themes.scss
assets/css/      main.scss (site styles), highlight-{light,dark}.css
bin/             new-post, publish-inbox
.github/workflows/
  jekyll.yml         build + deploy to Pages
  publish-inbox.yml  inbox → _posts, then calls jekyll.yml
```

## URLs

Posts live at `/blog/:year/:slug/`. jekyll-archives generates `/blog/:year/`,
`/blog/tag/:name/` and `/blog/category/:name/` to match — if you change
`permalink` in `_config.yml`, change those together, or the tag and category
links on each post stop resolving.

## Styling

Dracula palette, Anonymous Pro, lowercase everything. Colours are CSS custom
properties at the top of `assets/css/main.scss`; layout and components are in
`_sass/_base.scss`.
