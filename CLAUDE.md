# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Setup

This is a Jekyll-based static site using the al-folio theme for TwoBloodySpoons.github.io.

### Local Development (Docker - Recommended)

```bash
docker compose pull
docker compose up
```

Site will be available at http://localhost:8080

### Local Development (Native)

```bash
bundle install
bundle exec jekyll serve
```

Site will be available at http://localhost:4000

### Build for Production

```bash
bundle exec jekyll build
```

Output goes to `_site/` directory.

### CSS Purging (Optional)

```bash
purgecss -c purgecss.config.js
```

Run after build to remove unused CSS classes.

### Code Formatting

```bash
npx prettier --write "**/*.{liquid,html,md,yml,yaml,js,css,scss}"
```

## Site Architecture

### Content Structure

- **Homepage**: `_pages/about.md` - main landing page with profile
- **Blog**: `_pages/1blog_writing.md` - displays posts from `_posts/` with pagination
- **Casting**: `_pages/1projects_casting.md` - gaming/streaming content
- **Coding**: `_pages/1repositories_coding.md` - GitHub repositories and coding projects
- **News**: `_pages/news.md` - displays announcements from `_news/`

### Data Files

- `_config.yml` - main site configuration
- `_data/cv.yml` - CV/resume data (fallback)
- `_data/repositories.yml` - GitHub user/repo configuration
- `assets/json/resume.json` - primary resume data (JSON Resume format)

### Content Collections

- `_posts/` - blog articles (markdown with front matter)
- `_news/` - short announcements
- `_projects/` - project showcase items (currently disabled)
- `_bibliography/papers.bib` - academic publications

### Styling

- `_sass/` - SCSS partials and variables
- `assets/css/main.scss` - main stylesheet entry point
- Theme customization via `_sass/_variables.scss`

## Key Features

### Jekyll Plugins

- jekyll-scholar (bibliography management)
- jekyll-feed (RSS generation)
- jekyll-paginate-v2 (blog pagination)
- jekyll-imagemagick (responsive images)
- jekyll-tabs, jekyll-toc (enhanced content)

### Content Features

- **Math rendering** via MathJax (enable with `enable_math: true`)
- **Code syntax highlighting** with Rouge
- **Responsive images** with lazy loading
- **Dark mode** support
- **Search functionality** (ninja-keys)
- **Social media integration**

### Blog Configuration

- Blog name: "digestion"
- Tagline: "often an idea fascinates"
- Display tags: games, math, code, philosophy
- Pagination: 5 posts per page
- Related posts: up to 5 based on shared tags

## Development Guidelines

### Adding Content

- **New blog posts**: Create in `_posts/` with format `YYYY-MM-DD-title.md`
- **New pages**: Create in `_pages/` and update navigation if needed
- **News items**: Create in `_news/` (displays on homepage)
- **Projects**: Create in `_projects/` (currently disabled in config)

### Front Matter Requirements

All content should include proper front matter. Blog posts need:

```yaml
---
layout: post
title: "Post Title"
date: 2024-01-01
tags: [games, code]
---
```

### Image Handling

- Place images in `assets/img/`
- Use responsive image syntax: `{% include figure.liquid path="assets/img/image.jpg" %}`
- WebP conversion is automatic if imagemagick is enabled

### Social Media Configuration

Update social links in `_config.yml` under social integration section. Currently configured:

- GitHub: TwoBloodySpoons
- Bluesky: twospoons.online
- Discord: MDNXQzfmp2

### Theme Customization

- Modify `_sass/_variables.scss` for colors and fonts
- Override layouts by creating files in `_layouts/`
- Add custom includes in `_includes/`

## Deployment

Site deploys automatically to GitHub Pages via GitHub Actions when pushing to master branch. The workflow builds the site and pushes to gh-pages branch.

### Manual Deployment Trigger

Go to Actions → Deploy → Run workflow

### Alternative Hosting

For non-GitHub Pages hosting, build locally and copy `_site/` contents to your server.
