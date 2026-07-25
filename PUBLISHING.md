# Publishing to the blog

Everything you need to know to put words on twospoons.online.

---

## The short version

Put a `.md` or `.txt` file in `inbox/`. Commit it. Push. You're published.

```
inbox/some thoughts on dune.txt
   │
   │   Publish inbox workflow
   ▼
_posts/2026-07-25-some-thoughts-on-dune.md
   │
   │   Build and Deploy Jekyll workflow
   ▼
https://twospoons.online/blog/2026/some-thoughts-on-dune/
```

No front matter. No naming convention. No date to type. Roughly ninety
seconds from push to live.

---

## Why it works this way

### The problem it solves

Jekyll only recognises a post if its filename matches `YYYY-MM-DD-slug.md`
exactly. A file named `2026-03-18 you're probably a little bit obligated to try
and do something lad.md` — spaces instead of hyphens — is **silently ignored**.
No error. No warning. The build succeeds, the site deploys, and the post simply
does not exist. That happened to a real post in this repo, and it sat invisible
until someone diffed the build output against `_posts/`.

That's the worst kind of failure: writing disappears and nothing tells you.
Every design decision below follows from wanting that to be impossible.

### Why an inbox instead of writing to `_posts/` directly

The friction in Jekyll blogging isn't writing — it's the ceremony around it.
The filename has to be exactly right, the front matter has to be valid YAML,
the date has to be typed twice (filename and front matter) and kept in sync.
Get any of it wrong and the failure is silent.

`inbox/` has no requirements at all. Any name, any of three extensions, front
matter or not. The ceremony is done by a script that can't forget it, and the
script is the only thing that ever writes to `_posts/`.

This matters most on a phone. You can hit **Add file → Create new file** in
GitHub's web UI, type a name, paste your text, and commit — without knowing or
caring what Jekyll wants.

### Why the date comes from your commit

The date is read from git: the timestamp of the commit that first added the
file. Not from your system clock at build time, not from a date you type.

Committing *is* the act of publishing, so the commit time is the publication
time by definition. It's recorded in history, it's identical no matter who
builds the site or when, and rebuilding the site next year won't restamp
anything. There's nothing to keep in sync because there's only one source.

### Why the bot commits a real file back

The workflow doesn't convert your text on the fly during the build. It writes
an actual post file into `_posts/` and commits it to the repo.

A build-time-only transformation would mean the canonical version of your
writing exists nowhere but a temporary CI artifact. Instead the repo stays the
source of truth: you can read exactly what was published, edit it later, revert
it, or see it in `git log`. The inbox is a doorway, not a storage location.

### Why it validates in CI

`bin/publish-inbox --check` runs before every single build, and it fails the
build if any file in `_posts/` has a name Jekyll would skip. The original bug
can't recur silently — it becomes a red X on the commit instead of a post that
quietly never appeared.

---

## Publishing, step by step

### From your phone or any browser

1. Go to the repo on github.com.
2. Open the `inbox` folder → **Add file** → **Create new file**.
3. Name it whatever you like, ending in `.md` or `.txt`.
   (`the trouble with tuesdays.md`)
4. Paste or type your post.
5. **Commit changes** at the bottom. Commit straight to `master`.

Done. Check the **Actions** tab if you want to watch it land.

### From your machine

```bash
echo "..." > "inbox/the trouble with tuesdays.md"
git add inbox && git commit -m "new post" && git push
```

### Skipping the inbox entirely

If you're at a terminal and want the post file directly:

```bash
bin/new-post "the trouble with tuesdays"          # creates it in _posts/
bin/new-post "a bug i found" coding               # ...under a category
pbpaste | bin/new-post                            # ...from the clipboard
bin/new-post < notes.txt                          # ...from a file
```

It prints the path it created; open that and write. Then commit and push as
normal — this path bypasses the inbox workflow and deploys directly.

### Running the inbox conversion locally

```bash
bin/publish-inbox          # convert inbox/ → _posts/ on your machine
bin/publish-inbox --check  # say what would happen, change nothing
```

Useful for previewing with `bundle exec jekyll serve` before you push.

---

## What gets filled in for you

| Field | Where it comes from |
|---|---|
| **Title** | Your `title:` if you wrote one → else the first `#` heading → else the first line, if it reads like a title → else the filename |
| **Date** | Your `date:` if you wrote one → else a `2026-07-25-` prefix on the filename → else the time you committed the file |
| **Category** | Your `categories:` if you wrote one → else the subfolder (`inbox/coding/` → `coding`) → else `writing` |
| **Author** | `two_spoons` |
| **Slug** | Built from the title: lowercased, punctuation dropped, spaces hyphenated, a leading "a"/"an"/"the" removed, capped at 80 characters |
| **Layout** | `post` |

### On titles

"Reads like a title" means: 90 characters or under, and not ending in `.`, `!`
or `?`. A sentence gets treated as prose, not a heading.

Whichever line becomes the title is removed from the body, so it isn't
displayed twice — once as the post title and again as the first line.

```markdown
# on the difficulty of naming things

there are only two hard problems.
```

→ titled *on the difficulty of naming things*, body starts at "there are only".

```
just some raw text with no heading, dropped in from my phone.
```

→ ends in a period, so it stays in the body. The title comes from the filename.

---

## Taking control

Anything you write by hand wins. The script only fills in what's missing, and
never overwrites, reorders or reformats what you wrote.

```markdown
---
title: "a title with: a colon in it"
date: 2019-04-01 09:00:00 +0000
categories: [coding, philosophy]
tags: [meta, longform]
---

the body.
```

Useful overrides:

- **Backdating** — set `date:`, or name the file `2019-04-01-whatever.md`.
- **Multiple categories** — `categories: [coding, philosophy]`.
- **Tags** — `tags: [meta]`. Tags and categories both get archive pages, at
  `/blog/tag/:name/` and `/blog/category/:name/`, and the lists on `/writing/`
  build themselves from whatever your posts actually use.
- **A different author** — `author: someone else`.
- **A description** — `description:` shows under the title in the post list.
- **Pinning to the top of /writing/** — `featured: "true"`.
- **A table of contents** — `toc: {beginning: true}`.

---

## What happens after you push

1. **Publish inbox** fires on any push touching `inbox/**`.
2. It checks out the repo with full history (needed to date your file by its
   first commit).
3. `bin/publish-inbox` converts each file, writes it to `_posts/`, and deletes
   it from `inbox/`.
4. `github-actions[bot]` commits and pushes the result.
5. It then calls the **Build and Deploy Jekyll** workflow directly.

   *Step 5 is explicit for a reason:* GitHub refuses to trigger workflows from
   a push made with the automatic `GITHUB_TOKEN`, to stop workflows looping
   forever. So the bot's commit can't set off the deploy on its own. `jekyll.yml`
   declares `workflow_call:` and the inbox job invokes it — same run, no extra
   token, no loop.
6. The build validates every post filename, builds the site, and deploys to
   GitHub Pages.

Ordinary pushes that don't touch `inbox/` skip straight to step 6.

---

## When something goes wrong

The workflow fails loudly rather than publishing something wrong. Check the
**Actions** tab; the error names the file and the problem.

| Message | What happened |
|---|---|
| `not a text file` | Extension isn't `.md`, `.markdown` or `.txt`. Rename it. |
| `file is empty` | Nothing but whitespace. |
| `<name>.md already exists` | A post with that date and slug is already published. Change the title, or edit the existing post instead. |
| `bad filename — Jekyll will skip this file silently` | Something in `_posts/` isn't named `YYYY-MM-DD-slug.md`. This is the guard against the original bug. Rename it to match. |

**A failure stops the whole batch.** If you push five files and one of them is
empty, the job fails before the commit step, so none of the five are published
that run — not even the four that converted cleanly. Nothing is lost: your files
are all still sitting in `inbox/` exactly as you left them. Fix the one problem,
push again, and all five go together.

**The post didn't appear.** Check Actions for a red run first. If both workflows
are green, GitHub Pages caches aggressively — try a hard refresh. If it's still
missing, `git log` will show whether the bot's `publish:` commit happened.

**I want to unpublish something.** Delete the file from `_posts/` and push. The
post and its archive entries disappear on the next build.

---

## Where things live

```
inbox/                     drop zone. anything here becomes a post
_posts/                    published posts, YYYY-MM-DD-slug.md
bin/publish-inbox          the converter, and the --check validator
bin/new-post               local shortcut, straight to _posts/
.github/workflows/
  publish-inbox.yml        inbox → _posts → calls jekyll.yml
  jekyll.yml               validate, build, deploy to Pages
```

Posts are served from `/blog/:year/:slug/`. That's set by `permalink` in
`_config.yml`, and the `jekyll-archives` permalinks below it are written to
match — if you ever change one, change both, or the tag and category links on
every post stop resolving.
