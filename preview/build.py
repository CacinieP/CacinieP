"""Render both READMEs as a local GitHub-style review page (markdown-it-py)."""
from pathlib import Path
from markdown_it import MarkdownIt

root=Path(__file__).resolve().parents[1]
md=MarkdownIt('commonmark',{'html':True}).enable('table')
css='''
:root{--bg:#fff;--page:#f6f8fa;--fg:#1f2328;--muted:#656d76;--line:#d0d7de;--link:#0969da;--code:#eff1f3}*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--fg);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC",sans-serif}body.dark{--bg:#0d1117;--page:#010409;--fg:#e6edf3;--muted:#919ba6;--line:#30363d;--link:#58a6ff;--code:#21262d}nav{max-width:1050px;margin:24px auto 12px;display:flex;gap:9px;align-items:center;padding:0 24px;font-size:13px;color:var(--muted)}nav strong{margin-right:auto;color:var(--fg)}nav a,button{border:1px solid var(--line);border-radius:6px;padding:5px 12px;text-decoration:none;color:var(--fg);background:var(--bg);font:inherit;cursor:pointer}main{max-width:1012px;margin:0 auto 60px;border:1px solid var(--line);border-radius:6px;background:var(--bg);padding:32px 40px}a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}p{margin:0 0 16px}h2{font-size:24px;border-bottom:1px solid var(--line);padding-bottom:8px;margin:32px 0 16px;font-weight:600}h3{font-size:19px;margin:25px 0 12px;font-weight:600}img{max-width:100%;height:auto}sub{font-size:14px;line-height:1.8}hr{height:1px;background:var(--line);border:0;margin:26px 0}table{border-collapse:collapse;width:100%;font-size:14px;display:block;overflow:auto;margin:16px 0}td,th{border:1px solid var(--line);padding:9px 13px;text-align:left}th{font-weight:600}tr:nth-child(2n){background:var(--page)}td:first-child{white-space:nowrap}td p{margin:0 0 12px}table:has(img){display:table;table-layout:fixed}td:has(img){white-space:normal}td img{display:block;margin-bottom:10px}code{background:var(--code);border-radius:4px;padding:2px 5px;font-size:.9em}summary{cursor:pointer}details{margin:16px 0}iframe{width:100%;aspect-ratio:20/7;border:0;display:block}small.note{display:block;text-align:center;margin:10px auto;color:var(--muted);font-size:12px}.preview-label{font-size:11px;letter-spacing:1px;color:#b95f47}@media(max-width:650px){nav{flex-wrap:wrap;margin:12px auto;padding:0 12px;gap:6px}nav strong{flex-basis:100%}nav a,button{font-size:12px;padding:5px 9px}main{padding:18px 16px;border-radius:0;margin-bottom:0}h2{font-size:22px}h3{font-size:18px}table{font-size:13px}td,th{padding:7px 9px}sub{font-size:13px}main>table:has(img) tr{display:block}main>table:has(img) td{display:block;width:100%!important}main>table:has(img){display:block}}
'''
for filename,out,lang in [('README.md','index.html','zh-CN'),('README.en.md','english.html','en')]:
    rendered=md.render((root/filename).read_text())
    rendered=rendered.replace('./assets/','../assets/').replace('./README.en.md','./english.html').replace('./README.md','./index.html')
    rendered=rendered.replace('<picture>','<picture id="hero">',1)
    document=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CacinieP · README 本地预览</title><style>{css}</style></head><body>
<nav><strong>CacinieP / README <span class="preview-label">LOCAL REVIEW</span></strong><a href="./index.html">中文</a><a href="./english.html">English</a><button id="motion">交互 3D</button><button id="theme">深色预览</button></nav>
<main>{rendered}</main>
<script>
const theme=document.querySelector('#theme');theme.onclick=()=>{{document.body.classList.toggle('dark');theme.textContent=document.body.classList.contains('dark')?'浅色预览':'深色预览'}};
const motion=document.querySelector('#motion');const hero=document.querySelector('#hero');const backup=hero.outerHTML;
motion.onclick=()=>{{const live=document.querySelector('#live-hero');if(live){{live.outerHTML=backup;motion.textContent='交互 3D'}}else{{document.querySelector('#hero').outerHTML='<iframe id="live-hero" src="./hero.html" title="Three.js 交互横幅"></iframe>';motion.textContent='README 动图'}}}};
</script></body></html>'''
    (root/'preview'/out).write_text(document)
print('Built preview/index.html and preview/english.html')
