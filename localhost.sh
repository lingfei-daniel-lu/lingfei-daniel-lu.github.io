cd "$(dirname "${BASH_SOURCE[0]:-$0}")"
conda activate jekyll
bundle exec jekyll serve -l -H localhost