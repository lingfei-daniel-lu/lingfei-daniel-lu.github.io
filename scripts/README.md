# 中文简历 PDF 编译

在项目根目录运行：

```sh
bash scripts/build_chinese_cv.sh
```

默认读取 `drafts/Lingfei_LU_CV_Chinese_short.md`，覆盖同目录下的同名 PDF，并显示页数。Markdown 不会被修改。超出一页时会给出提示，不会自动缩小字号。

文件重命名后，可以传入新的路径：

```sh
bash scripts/build_chinese_cv.sh drafts/新的文件名.md
```

当前排版支持：`# 姓名`、姓名后的单位与个人信息、`## 栏目标题`、以空行分隔的正文段落。姓名后的第一段作为单位行；其余个人信息段落均居中排列，分隔线放在第一个栏目标题之前。段落内换行在 PDF 中保留。正文支持用 `**英文内容**` 加粗姓名和期刊名称。此脚本专用于当前简历格式，不解析 Markdown 表格、图片等语法。

脚本优先使用本机 Codex 附带的 Python；也可用 `PYTHON_BIN=/path/to/python3 bash scripts/build_chinese_cv.sh` 指定已安装 `reportlab` 和 `pypdf` 的 Python。PDF 使用 ReportLab 自带的中文字体配置。
