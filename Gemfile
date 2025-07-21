source 'https://rubygems.org'

gem 'jekyll', '~> 4.0'
gem 'webrick'
gem 'kramdown-parser-gfm'
gem 'base64'
gem 'logger'
gem 'bigdecimal'
gem 'classifier-reborn'
gem 'mini_racer'
gem 'unicode_utils'
gem 'ostruct'
gem "faraday-retry"

group :jekyll_plugins do
    gem 'jekyll-archives'
    gem 'jekyll-email-protect'
    gem 'jekyll-feed'
    gem 'jekyll-get-json'
    gem 'jekyll-imagemagick'
    gem 'jekyll-jupyter-notebook'
    gem 'jekyll-link-attributes'
    gem 'jekyll-minifier'
    gem 'jekyll-paginate-v2'
    gem 'jekyll-regex-replace'
    gem 'jekyll-scholar', '~> 7.0'
    gem 'jekyll-sitemap'
    gem 'jekyll-tabs'
    gem 'jekyll-toc'
    gem 'jekyll-twitter-plugin'
    gem 'jemoji'
    gem "jekyll-seo-tag"
    gem "jekyll-github-metadata"
end

group :other_plugins do
    gem 'css_parser'
    gem 'feedjira'
    gem 'httparty'
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
