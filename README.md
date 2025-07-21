# fold in space

<div align="left">
<br>
casting
<br><br>
coding
<br><br>
selling out

# two_spoons

A blog

## Features

## Development

### Prerequisites

- Ruby 3.1+
- Bundler

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/TwoBloodySpoons/two_spoons_online.git
   cd two_spoons_online
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Start the development server:
   ```bash
   bundle exec jekyll serve
   ```

4. Visit https://127.0.0.1:4000

### Adding Content

#### New Posts

Create a new file in `_posts/` with the format:
```
YYYY-MM-DD-title.md
```

Example front matter:
```yaml
---
layout: post
title: "your post title"
date: 2024-01-01 12:00:00 +0000
categories: [writing] # or [casting] or [coding]
author: your_name
---

Your content here...
```

#### Categories

Posts are automatically categorized based on the `categories` field in the front matter:
- `[writing]` 
- `[casting]` 
- `[coding]`
## Deployment

### GitHub Pages

The site automatically deploys to GitHub Pages when you push to the main branch. The Jekyll build process is handled by GitHub Actions.

### Manual Deployment

1. Build the site:
   ```bash
   bundle exec jekyll build
   ```

2. The generated site will be in `_site/`

## Project Structure

```
├── _layouts/              # Jekyll layouts
├── _includes/             # Reusable Jekyll components
├── _posts/               # Blog posts
├── assets/css/           # Stylesheets
├── .github/workflows/    # GitHub Actions
├── _config.yml          # Jekyll configuration
├── Gemfile              # Ruby dependencies
└── index.html          # Homepage
```

## Customization

### Styling

The Dracula theme styles are defined in `assets/css/main.scss`. The site uses:
- CSS custom properties for colors
- Input Mono font for all text
- Lowercase text transformation
- Bootstrap for responsive layout

### Configuration

Site settings can be modified in `_config.yml`:

## Contributing

## License
