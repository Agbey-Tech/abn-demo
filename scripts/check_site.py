"""Check local links, assets, fragments and IDs at root and repository subpaths."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys

root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
class Page(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        for name in ('href','src'):
            if name in attrs:self.links.append(attrs[name])

files=[root/'index.html']+[p for p in root.glob('*/index.html') if p.parent.name not in ('src','_site')]
pages={}
for file in files:
    p=Page();p.feed(file.read_text(encoding='utf-8-sig'));pages[file.resolve()]=p
errors=[]
for file,p in pages.items():
    dup={id for id in p.ids if p.ids.count(id)>1}
    if dup:errors.append(str(file.relative_to(root))+': duplicate IDs '+str(dup))
    for ref in p.links:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        if url.path.startswith('/'):errors.append(str(file.relative_to(root))+': root-relative link '+ref);continue
        target=(file.parent/unquote(url.path)).resolve() if url.path else file
        if target.is_dir():target=target/'index.html'
        if not target.is_file():errors.append(str(file.relative_to(root))+': missing '+ref);continue
        if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(str(file.relative_to(root))+': missing fragment '+ref)
print('Checked',len(pages),'HTML pages;',sum(len(p.links) for p in pages.values()),'references')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('PASS: all local assets, page destinations, and fragment targets resolve; no root-relative URLs or duplicate IDs.')
