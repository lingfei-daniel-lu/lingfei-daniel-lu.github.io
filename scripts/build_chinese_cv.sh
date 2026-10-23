#!/bin/bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
bundled_python="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"

if [[ -n "${PYTHON_BIN:-}" ]]; then
    cv_python="$PYTHON_BIN"
elif [[ -x "$bundled_python" ]]; then
    cv_python="$bundled_python"
else
    cv_python="python3"
fi

if ! "$cv_python" -c 'import reportlab, pypdf' >/dev/null 2>&1; then
    echo '缺少编译依赖。请为所用 Python 安装 reportlab 和 pypdf。' >&2
    exit 1
fi

exec "$cv_python" "$script_dir/build_chinese_cv.py" "$@"
