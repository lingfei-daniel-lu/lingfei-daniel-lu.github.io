from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
import argparse
import re

parser = argparse.ArgumentParser(description='将中文简历 Markdown 转为同名 PDF。')
parser.add_argument('source', nargs='?', type=Path,
                    default=Path(__file__).resolve().parents[1] / 'drafts/Lingfei_LU_CV_Chinese_short.md')
args = parser.parse_args()
src = args.source.resolve()
if not src.is_file():
    parser.error(f'找不到 Markdown 文件：{src}')
blocks = re.split(r'\n\s*\n', src.read_text(encoding='utf-8').strip())
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
bold_font_path = Path('/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf')
bold_font = 'Times-Bold'
if bold_font_path.is_file():
    pdfmetrics.registerFont(TTFont('CVLatinBold', str(bold_font_path)))
    bold_font = 'CVLatinBold'

def inline_markup(text):
    """Render Markdown bold spans after escaping PDF paragraph markup."""
    return re.sub(r'\*\*(.+?)\*\*',
                  lambda match: f'<font name="{bold_font}">{match.group(1)}</font>',
                  escape(text))

styles={
'name':ParagraphStyle('name',fontName='STSong-Light',fontSize=24,leading=31,alignment=TA_CENTER,textColor=HexColor('#17334a'),spaceAfter=7),
'head':ParagraphStyle('head',fontName='STSong-Light',fontSize=11.5,leading=16.5,alignment=TA_CENTER,spaceAfter=3),
'contact':ParagraphStyle('contact',fontName='STSong-Light',fontSize=9.5,leading=16.5,alignment=TA_CENTER,spaceAfter=3),
'section':ParagraphStyle('section',fontName='STSong-Light',fontSize=12.5,leading=17.5,textColor=HexColor('#17334a'),spaceBefore=9,spaceAfter=5,keepWithNext=True),
'body':ParagraphStyle('body',fontName='STSong-Light',fontSize=10.8,leading=16.5,spaceAfter=4.5,wordWrap='CJK')}
contact_left = ParagraphStyle('contact_left', parent=styles['contact'], alignment=TA_RIGHT)
contact_right = ParagraphStyle('contact_right', parent=styles['contact'], alignment=TA_LEFT)
content_width = A4[0] - 86
story=[]
in_header = True
for i,block in enumerate(blocks):
    if block.startswith('# '):
        story.append(Paragraph(escape(block[2:]),styles['name']))
    elif block.startswith('## '):
        if in_header:
            story.append(Spacer(1, 5))
            story.append(HRFlowable(width='100%',thickness=.7,color=HexColor('#9aabb7')))
            in_header = False
        story.append(Paragraph(escape(block[3:]),styles['section']))
    else:
        style=styles['head'] if in_header and i==1 else styles['contact'] if in_header else styles['body']
        if in_header and i > 1 and '｜' in block:
            left, right = (part.strip() for part in block.split('｜', 1))
            row = Table([[
                Paragraph(escape(left), contact_left),
                Paragraph('｜', styles['contact']),
                Paragraph(escape(right), contact_right),
            ]], colWidths=[(content_width - 18) / 2, 18, (content_width - 18) / 2],
                hAlign='CENTER', spaceAfter=3)
            row.setStyle(TableStyle([
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            story.append(row)
        else:
            story.append(Paragraph('<br/>'.join(inline_markup(line) for line in block.splitlines()),style))
out=src.with_suffix('.pdf')
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=32,bottomMargin=32,title='卢凌飞｜中文简历',author='Lingfei Lu').build(story)
pages = len(PdfReader(out).pages)
print(f'已生成：{out}')
print(f'页数：{pages}')
if pages > 1:
    print('提示：内容已超出一页，请精简 Markdown 后重新编译。')
