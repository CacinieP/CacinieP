"""Small, explicit content diagrams for the folded research index (not UI mockups)."""
from pathlib import Path
from html import escape
root=Path(__file__).resolve().parents[1]
items=[
 ('inference','Inference Index','SERVING / EDGE / RUNTIME','#e9f0ed','#245749','pipeline'),
 ('evolution','Agent Self-Evolution','PAPERS / REPRODUCTIONS','#eef0e5','#6b7048','cycle'),
 ('evalops','AgentEvalOps','REGRESSION / DRIFT / COMPARE','#e9eef5','#426485','compare'),
 ('math-dl','Math → Deep Learning','DERIVE / IMPLEMENT / TRAIN','#ececf6','#625a8b','matrix'),
 ('math-universe','Mathematics Universe','CONNECTED MATHEMATICS','#e8f1ef','#38786c','network'),
 ('mathconnect','MathConnect','EQUIVALENT INFINITESIMALS','#f4eee3','#a26f2c','tiles'),
 ('german','German Linguistics','LEXICON / MORPHOLOGY','#f4eae5','#a06b53','tree'),
 ('typing','Typing Master','MULTILINGUAL PRACTICE','#e9eef7','#586b9e','keys'),
 ('music','Music Research','AUDIO / GENERATION / LOCAL','#efeaf3','#836092','wave'),
 ('beancount','FinancialBeancount','CONVERT / DEDUPLICATE','#e8f0e9','#417652','ledger'),
 ('cpa','CICPA Learning','SUBJECTS / STUDY GUIDE','#f3ece5','#9b7350','books'),
 ('law','LPQE Learning','LEGAL STUDY NOTES','#eee9e5','#7c6453','clauses'),
]
for slug,title,label,bg,ink,kind in items:
    shapes=''
    if kind in ['pipeline','compare']:
        for x,h in [(385,50),(460,85),(535,120)]:shapes+=f'<rect x="{x}" y="{175-h}" width="45" height="{h}" rx="3" fill="{ink}" opacity=".6"/>'
        shapes+=f'<path d="M370 185H595" stroke="{ink}" opacity=".4"/>'
    elif kind=='cycle':
        shapes=f'<circle cx="493" cy="116" r="66" fill="none" stroke="{ink}" stroke-width="2"/><circle cx="493" cy="116" r="43" fill="none" stroke="{ink}" opacity=".35"/>'
        for x,y in [(493,50),(550,149),(436,149)]:shapes+=f'<circle cx="{x}" cy="{y}" r="8" fill="{ink}"/>'
    elif kind in ['matrix','tiles','keys','books']:
        for i in range(6):
            x=390+(i%3)*63;y=58+(i//3)*65
            shapes+=f'<rect x="{x}" y="{y}" width="49" height="49" rx="4" fill="{ink}" opacity="{.12+.11*i}"/>'
        if kind=='matrix':shapes+=f'<path d="M378 49H366V183H378M575 49H587V183H575" fill="none" stroke="{ink}" stroke-width="2"/>'
    elif kind in ['network','tree']:
        for x,y in [(400,151),(472,171),(563,141),(435,72),(543,62)]:shapes+=f'<path d="M490 114L{x} {y}" stroke="{ink}" opacity=".5"/><circle cx="{x}" cy="{y}" r="7" fill="{ink}"/>'
        shapes+=f'<circle cx="490" cy="114" r="18" fill="none" stroke="{ink}" stroke-width="2"/>'
    elif kind=='wave':
        heights=[20,38,73,104,65,126,82,52,102,39,67,22]
        for i,h in enumerate(heights):shapes+=f'<rect x="{380+i*17}" y="{120-h/2}" width="7" height="{h}" rx="3" fill="{ink}" opacity=".65"/>'
    else:
        for i,w in enumerate([185,150,175,115]):shapes+=f'<rect x="390" y="{65+i*30}" width="{w}" height="9" rx="2" fill="{ink}" opacity="{.75-.13*i}"/>'
        shapes+=f'<path d="M378 50V183" stroke="{ink}" opacity=".35"/>'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="240" viewBox="0 0 640 240" role="img"><title>{escape(title)} — content diagram</title><rect width="640" height="240" rx="8" fill="{bg}"/><path d="M24 24H616V216H24Z" fill="none" stroke="{ink}" opacity=".15"/><text x="43" y="58" fill="{ink}" font-family="monospace" font-size="10" letter-spacing="1.6">PROJECT INDEX / CONTENT DIAGRAM</text><text x="43" y="111" fill="{ink}" font-family="Arial,sans-serif" font-size="{23 if len(title)>20 else 27}" font-weight="600">{escape(title)}</text><text x="43" y="150" fill="{ink}" font-family="monospace" font-size="10" letter-spacing=".8">{label}</text><path d="M43 177H110" stroke="{ink}" stroke-width="2"/>{shapes}</svg>'''
    (root/f'assets/projects/{slug}.svg').write_text(svg)
print('Built',len(items),'research content diagrams')
