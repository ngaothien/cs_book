import markdown
import sys

text = open('translation/18_translation.md', encoding='utf-8').read()
html = markdown.markdown(text, extensions=['extra'])
full = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Chương 1: Giới thiệu - Foundations of Machine Learning</title>
<style>
body { font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px 40px; line-height: 1.8; color: #222; }
h1 { font-size: 28px; border-bottom: 2px solid #333; padding-bottom: 10px; }
h2 { font-size: 22px; margin-top: 30px; color: #1a1a2e; }
ul, ol { margin-left: 20px; }
li { margin-bottom: 8px; }
blockquote { background: #f9f9f9; border-left: 4px solid #ccc; padding: 10px 20px; margin: 20px 0; font-style: italic; }
strong { color: #1a1a2e; }
code { background: #f0f0f0; padding: 2px 6px; border-radius: 3px; font-size: 14px; }
@media print { body { margin: 0; padding: 20px; } }
</style>
</head>
<body>
''' + html + '''
</body>
</html>'''
with open('translation/18_translation.html', 'w', encoding='utf-8') as f:
    f.write(full)
print('HTML generated successfully')
