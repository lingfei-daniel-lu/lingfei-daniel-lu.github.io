# lingfei-daniel-lu.github.io

Personal academic website of [Lingfei Lu](https://lingfei-daniel-lu.github.io), Assistant Professor of Finance at the School of Finance, Renmin University of China.

Built with [Jekyll](https://jekyllrb.com) on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template (a fork of Minimal Mistakes) and hosted on GitHub Pages.

## Running locally

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

Then open http://localhost:4000. A Dockerfile and `localhost.sh` are also available from the upstream template.

## Site structure

| Path | Content |
|---|---|
| `_config.yml` | Site-wide settings, author profile, collections |
| `_pages/` | Homepage (`about.md`), Research, Teaching, CV, 404, archive pages |
| `_publications/` | Published papers (one Markdown file each) |
| `_working_papers/` | Working papers and works in progress, distinguished by the `status2` front-matter field (`jmp`, `revise_resubmit`, `in_progress`, ...) |
| `_teaching/` | Teaching entries |
| `files/` | PDFs (papers, slides, CV) served from `/files/` |
| `images/` | Avatar and favicon/PWA assets |
| `_sass/`, `_includes/`, `_layouts/` | Vendored Academic Pages theme + a small `_sass/custom.scss` for personal styles |
| `assets/js/` | Site scripts (`research-summaries.js` powers the expand/collapse buttons on the Research page) |

## Adding a paper

1. Create a Markdown file in `_publications/` (published) or `_working_papers/` (working/in progress). Copy the front matter from an existing entry: `title`, `date` (ISO format), `status2`, `permalink`, `coauthors`, `excerpt`/`abstract`, `citation`, and optionally `presentation`, `highlights`, `wppaperurl`.
2. Drop the paper PDF (and slides) into `files/` using the same slug as the Markdown filename — the `[PDF]` / `[Slides]` links are generated automatically from `/files/<slug>.pdf` and `/files/<slug>_slides.pdf`.
3. The Research page groups entries by `status2`; published papers appear under Publications.

The Research page list is maintained by hand; `markdown_generator/pubsFromBib.py` can bootstrap Markdown entries from a BibTeX file.
