# inbox

Drop a `.md` or `.txt` file in here and push. That's the whole workflow.

On push, GitHub Actions turns it into a dated, sorted post in `_posts/` and
deletes it from here — then the site rebuilds and deploys.

- **Title** — the first `# heading` in the file, or the first line if it reads
  like a title, or the filename.
- **Date** — when you committed the file. Put `2026-07-25-` at the front of the
  filename to override it.
- **Category** — `writing` by default. Drop the file in `inbox/coding/` to file
  it under `coding` instead.

You never need to write front matter. If you do, it's kept as-is and only the
missing pieces get filled in.

To do it locally instead: `bin/new-post "a title"` creates the file in `_posts/`
directly, or `bin/publish-inbox` processes this folder on your machine.

Full details, including how to override any of the above and what to do when a
push fails: [PUBLISHING.md](../PUBLISHING.md).

(This README is ignored by the publisher.)
