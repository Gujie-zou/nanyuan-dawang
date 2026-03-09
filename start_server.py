#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
南院大王知识库 - 本地服务器启动脚本
双击运行后，在浏览器中打开 http://localhost:8080 查看
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# 配置
PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # 添加CORS支持
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# 简单的Markdown渲染HTML模板
MARKDOWN_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 南院大王</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', sans-serif;
            background: #f5f5f5;
            color: #333;
            line-height: 1.8;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        h1 {{ color: #1a1a2e; border-bottom: 2px solid #ffd700; padding-bottom: 10px; margin-bottom: 20px; }}
        h2 {{ color: #2d2d44; margin-top: 30px; margin-bottom: 15px; }}
        h3 {{ color: #444; margin-top: 20px; margin-bottom: 10px; }}
        p {{ margin-bottom: 15px; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e9ecef;
        }}
        th {{
            background: #f8f9fa;
            font-weight: 600;
            color: #1a1a2e;
        }}
        tr:hover {{ background: #f8f9fa; }}
        blockquote {{
            border-left: 4px solid #ffd700;
            padding-left: 20px;
            margin: 20px 0;
            color: #666;
            font-style: italic;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background: #1a1a2e;
            color: #fff;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 20px 0;
        }}
        ul, ol {{ margin: 15px 0; padding-left: 30px; }}
        li {{ margin-bottom: 8px; }}
        .tag {{
            display: inline-block;
            padding: 2px 8px;
            background: #e9ecef;
            border-radius: 4px;
            font-size: 0.75em;
            margin-right: 5px;
            color: #666;
        }}
        a {{ color: #1a1a2e; text-decoration: none; border-bottom: 1px solid #ffd700; }}
        a:hover {{ background: #ffd700; }}
        .back-btn {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 8px 16px;
            background: #1a1a2e;
            color: white;
            text-decoration: none;
            border-radius: 6px;
        }}
        .back-btn:hover {{ background: #2d2d44; }}
        @media (max-width: 768px) {{
            .container {{ padding: 20px; }}
            body {{ padding: 10px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back-btn">← 返回首页</a>
        {content}
    </div>
</body>
</html>'''

def render_markdown(md_content, title):
    """简单的Markdown转HTML"""
    import re
    
    html = md_content
    
    # 转义HTML特殊字符
    html = html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # 标题
    html = re.sub(r'^###### (.*?)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.*?)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # 粗体和斜体
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # 代码块
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    # 引用
    html = re.sub(r'^\> (.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # 表格（简化处理）
    lines = html.split('\n')
    in_table = False
    table_html = []
    new_lines = []
    
    for line in lines:
        if '|' in line and not in_table:
            in_table = True
            table_html = ['<table>']
        elif '|' not in line and in_table:
            in_table = False
            table_html.append('</table>')
            new_lines.append('\n'.join(table_html))
            table_html = []
        
        if in_table:
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if cells and not all(c.replace('-', '').replace(' ', '') == '' for c in cells):
                if '---' in line:
                    continue
                row = '<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>'
                table_html.append(row)
        else:
            new_lines.append(line)
    
    if in_table:
        table_html.append('</table>')
        new_lines.append('\n'.join(table_html))
    
    html = '\n'.join(new_lines)
    
    # 列表
    html = re.sub(r'^\- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>\n)+', r'<ul>\g<0></ul>', html, flags=re.DOTALL)
    
    # 段落
    paragraphs = html.split('\n\n')
    new_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<') and not p.startswith('---'):
            p = f'<p>{p}</p>'
        new_paragraphs.append(p)
    html = '\n\n'.join(new_paragraphs)
    
    # 标签
    html = re.sub(r'#(\w+)', r'<span class="tag">#\1</span>', html)
    
    return MARKDOWN_TEMPLATE.format(title=title, content=html)

class MarkdownHandler(MyHTTPRequestHandler):
    def do_GET(self):
        # 如果请求的是.md文件，渲染为HTML
        if self.path.endswith('.md'):
            file_path = os.path.join(DIRECTORY, self.path.lstrip('/'))
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                title = os.path.basename(file_path).replace('.md', '')
                html = render_markdown(content, title)
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(html.encode('utf-8'))
                return
        
        # 否则使用默认的文件服务
        super().do_GET()

def main():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n{'='*50}")
        print(f"🎯 南院大王知识库已启动！")
        print(f"{'='*50}")
        print(f"\n📍 本地访问地址: {url}")
        print(f"📱 手机/平板在同一WiFi下也可访问")
        print(f"\n⚠️  按 Ctrl+C 停止服务器")
        print(f"{'='*50}\n")
        
        # 自动打开浏览器
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 服务器已停止")

if __name__ == '__main__':
    main()
