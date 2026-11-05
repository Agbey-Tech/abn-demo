"""Guard the agreed demo scope and original factual content."""
from pathlib import Path
from html import unescape
import json,re,sys
root=Path(__file__).resolve().parents[1]
out=(root/(sys.argv[1] if len(sys.argv)>1 else '.')).resolve()
sys.path.insert(0,str(root/'scripts'))
from content import SERVICES,TEAM,PROJECTS
errors=[]
def require(condition,message):
 if not condition:errors.append(message)
def text(route):return unescape(re.sub('<[^>]+>',' ',(out/route/'index.html').read_text(encoding='utf-8')))
for s in SERVICES:
 page=text('services/'+s['slug'])
 require(s['name'] in page,'Missing service name: '+s['name'])
 for item in s['items']:require(item in page,'Missing service scope: '+item)
about=text('about')
for _,name,role in TEAM:require(name in about and role in about,'Missing team member or role: '+name)
require(len(PROJECTS)==6,'The pitch must curate six projects')
for project in PROJECTS:
 page=text('work/'+project['slug'])
 require(project['description'] in page,'Original project description changed: '+project['name'])
 require('founding team' in page.lower(),'Missing founding-team attribution: '+project['name'])
require(len(json.loads((root/'content/projects.json').read_text(encoding='utf-8')))==47,'Source portfolio inventory must retain 47 projects')
for route,phrases in {'network':['50','February 2027','June 2027','8–12','20-minute','non-denominational'], 'experiences':['Atlanta','Q3 2027','planned','under consideration'], 'resources':['Coming soon','No episodes are published yet','Neither file is available yet.'], 'contact':['does not send or store','30-minute','20-minute'], '':['Illustrative workflow','Not a client project']}.items():
 page=text(route)
 for phrase in phrases:require(phrase in page,'Missing status or fact: '+route+' / '+phrase)
css=(root/'design.css').read_text(encoding='utf-8')
require(not re.search(r'(linear|radial|conic)-gradient\s*\(',css),'Designed surfaces must not use gradients')
print('Checked service scopes, team attribution, curated projects, original facts, resource status, and solid-colour design.')
if errors:print('\n'.join(errors));sys.exit(1)
print('PASS: demo scope and content preservation checks.')
