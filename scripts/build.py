"""Build all Ascend pages. Standard library only; repository-subpath safe."""
from pathlib import Path
from html import escape
import argparse, re, shutil
from urllib.parse import unquote
from pages import PAGES
from content import SERVICES,ROOT
parser=argparse.ArgumentParser();parser.add_argument('--output',default='.');args=parser.parse_args()
OUT=(ROOT/args.output).resolve()
def a(url,label,cls=''):return f'<a href="@{url}"'+(f' class="{cls}"' if cls else '')+'>'+label+'</a>'
def navigation(route):
 services=''.join(a('services/'+s['slug']+'/',s['name']) for s in SERVICES)
 solutions=''.join(a(u,t) for u,t in [('solutions/business/','Businesses & professionals'),('real-estate/','Real estate professionals'),('churches-ministries/','Churches & ministries'),('solutions/faith-driven/','Faith-driven organisations')])
 def drop(title,body,overview):return '<details class="nav-disclosure"><summary>'+title+' <span aria-hidden="true">⌄</span></summary><div class="nav-dropdown">'+a(overview,'Overview <span>↗</span>','dropdown-overview')+body+'</div></details>'
 links=a('work/','Work')+drop('Services',services,'services/')+drop('Solutions',solutions,'solutions/')+a('about/','About')
 brand='<a class="brand" href="@index.html" aria-label="Ascend Brand Network home"><span class="brand-symbol"><img src="@assets/WhatsApp Image 2026-11-05 at 3.55.41 PM (1).jpeg" alt="" width="1600" height="1094"></span><span class="brand-name">ASCEND<small>BRAND NETWORK</small></span></a>'
 return '<header class="site-header"><div class="header-inner wrap">'+brand+'<nav class="desktop-nav" aria-label="Main navigation">'+links+'</nav><div class="header-end">'+a('network/','The Network','network-link')+a('contact/','Start a project <span>↗</span>','button button-small')+'<button class="menu-toggle" aria-label="Open navigation" aria-controls="mobile-menu" aria-expanded="false"><span></span><span></span></button></div></div><nav id="mobile-menu" class="mobile-menu wrap" aria-label="Mobile navigation" hidden>'+links+a('network/','The Network')+a('experiences/','Experiences')+a('resources/','Resources')+a('contact/','Start a project ↗','mobile-contact')+'</nav></header>'
def footer():
 cols=[('Company',[('work/','Our work'),('about/','About Ascend'),('contact/','Let’s connect')]),('What we build',[(f'services/{s["slug"]}/',s['short']) for s in SERVICES]),('Who we serve',[('solutions/business/','Businesses'),('real-estate/','Real estate'),('churches-ministries/','Churches & ministries'),('solutions/faith-driven/','Faith-driven organisations')]),('The Network',[('network/','Network overview'),('network/#founding','Founding membership'),('network/#process','Membership process'),('network/#faqs','Membership FAQs'),('roundtable/','The Shepherd’s Roundtable'),('experiences/','Dinners & retreats'),('resources/','Resource Center'),('resources/#diary','The Shepherd’s Diary')])]
 return '<footer class="site-footer"><div class="wrap"><div class="footer-cta"><div><p class="eyebrow">A conversation is a good place to start.</p><h2>Let’s build<br>what’s next.</h2></div>'+a('contact/','<span aria-hidden="true">↗</span><span class="sr-only">Start a project</span>','footer-arrow')+'</div><div class="footer-grid"><div class="footer-brand"><img src="@assets/WhatsApp Image 2026-11-05 at 3.55.40 PM (1).jpeg" alt="Ascend Brand Network" width="1200" height="386"><p>Thoughtful strategy.<br>Considered design.<br>Practical delivery.</p><span>Nationwide, United States</span></div>'+''.join('<div><h3>'+label+'</h3>'+''.join(a(u,t) for u,t in items)+'</div>' for label,items in cols)+'</div><div class="footer-bottom"><span>© 2026 Ascend Brand Network</span><span>Website redesign preview</span><button class="motion-toggle" type="button" aria-pressed="false">Pause motion</button><a href="#main">Back to top ↑</a></div></div></footer>'
def render(route,title,body,desc):
 prefix='../'*len(Path(route).parts) if route else ''
 legacy=''
 if route in ['contact','work-with-us']:legacy=''.join(f'<span id="{x}" class="anchor-target"></span>' for x in ['studio','network','experience','general'])
 text=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#000E3F"><title>{escape(title)} | Ascend</title><meta name="description" content="{escape(desc,quote=True)}"><meta property="og:title" content="{escape(title,quote=True)}"><meta property="og:description" content="{escape(desc,quote=True)}"><meta property="og:type" content="website"><link rel="icon" href="@assets/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Manrope:wght@400;450;500;550;600;650;700;750;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="@design.css"><script src="@site.js" defer></script></head><body data-page="{route or 'home'}" data-root="{prefix}"><a class="skip-link" href="#main">Skip to content</a>{navigation(route)}<main id="main">{legacy}{body}</main>{footer()}</body></html>'''
 return text.replace('"@','"'+prefix).replace("'@","'"+prefix)
if OUT!=ROOT and OUT.exists():
 if OUT != (ROOT/'_site').resolve(): raise ValueError('Use _site for the deploy artifact')
 shutil.rmtree(OUT)
OUT.mkdir(parents=True,exist_ok=True)
for route,(title,body,desc) in PAGES.items():
 folder=OUT/route;folder.mkdir(parents=True,exist_ok=True)
 (folder/'index.html').write_text(render(route,title,body,desc),encoding='utf-8')
(OUT/'.nojekyll').write_text('',encoding='utf-8')
if OUT!=ROOT:
 for name in ['design.css','site.js']:shutil.copy2(ROOT/name,OUT/name)
 asset_refs=set()
 for page in OUT.rglob('index.html'):
  asset_refs.update(unquote(x) for x in re.findall(r'assets/([^\"]+)',page.read_text(encoding='utf-8')))
 (OUT/'assets').mkdir(exist_ok=True)
 for name in asset_refs:
  src=(ROOT/'assets'/name).resolve()
  if not src.is_relative_to(ROOT/'assets'): raise ValueError('Invalid asset path')
  shutil.copy2(src,OUT/'assets'/name)
print('Built',len(PAGES),'pages in',OUT)
