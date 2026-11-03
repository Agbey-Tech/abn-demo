"""Build the static demo. Standard library only; supports GitHub project subpaths."""
from pathlib import Path
import argparse
import re
import shutil
from html import escape

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--output', default='.', help='Output directory relative to the project root')
args = parser.parse_args()
OUT = (ROOT / args.output).resolve()
SOURCE = (ROOT / 'src' / 'home.html').read_text(encoding='utf-8-sig')

def section(id):
    found = re.search(r'<section\b[^>]*\bid="'+re.escape(id)+r'"[^>]*>[\s\S]*?</section>', SOURCE)
    if not found: raise ValueError('Missing source section '+id)
    return found.group()

NETWORK = [
 ('Explore the Network', [('Network Overview','network/#overview'),('Why the Network Exists','network/#why'),('Member Experience','network/#experience'),('Community Values','network/#values')]),
 ('Membership', [('Founding Membership','network/#founding'),('Who Can Join','network/#who'),('Membership Process','network/#process'),('Membership FAQs','network/#faqs')]),
 ('Signature Experiences', [("The Shepherd’s Roundtable",'roundtable/'),('Leadership Dinners','experiences/#dinners'),('Leadership Retreats','experiences/#retreats'),('Upcoming Gatherings','experiences/#upcoming')])]
STUDIO = [
 ('Creative Services', [('All Services','services/#services'),('Brand Strategy & Identity','services/#brand'),('Digital Marketing & Content','services/#marketing'),('Website & App Development','services/#web'),('Event & Video Production','services/#events'),('Church Media Systems','services/#media')]),
 ('Who We Serve', [('Churches & Ministries','churches-ministries/'),('Real Estate Professionals','real-estate/'),('Faith-Driven Organisations','services/#faith')]),
 ('Work With Us', [('Our Process','services/#process'),('Portfolio & Case Studies','portfolio/#projects'),('Project FAQs','services/#faqs'),('Request a Consultation','work-with-us/#studio')])]
EXPERIENCES = [('Experiences', [('All Experiences','experiences/'),('The Shepherd’s Roundtable','roundtable/'),('Leadership Dinners','experiences/#dinners'),('Leadership Retreats','experiences/#retreats'),('Upcoming Events','experiences/#upcoming'),('Receive Experience Updates','work-with-us/#experience')])]
RESOURCES = [('Resources', [('Resource Center','resources/'),('The Shepherd’s Diary Podcast','resources/#diary'),('Leadership & Ministry Insights','resources/#leadership-insights'),('Church Branding Resources','resources/#church-branding'),('Digital Marketing Insights','resources/#digital-marketing'),('Real Estate Branding Resources','resources/#real-estate-branding'),('Free Downloads','resources/#downloads')])]
ABOUT = [('About ABN', [('About ABN','about/'),('Our Story','about/#story'),('Our Mission','about/#mission'),('Our Values','about/#values'),('The ABN Ecosystem','about/#ecosystem')])]

def href(route, prefix):
    return prefix + ('index.html' if route == '' else route)

def groups(data, prefix):
    return ''.join('<div class="site-menu-group"><h3>'+escape(title)+'</h3>'+''.join('<a href="'+href(url,prefix)+'">'+escape(label)+('<span class="menu-soon">Soon</span>' if title=='Resources' and '#' in url else '')+'</a>' for label,url in links)+'</div>' for title,links in data)

def navigation(prefix, page):
    active = 'network' if page in ('network','roundtable') else 'studio' if page in ('services','churches-ministries','real-estate','portfolio') else page
    nav = '<a href="'+href('',prefix)+'"'+(' class="active" aria-current="page"' if page=='home' else '')+'>Home</a>'
    for key,label in [('network','The Network'),('studio','Ascend Studio'),('experiences','Experiences'),('resources','Resources')]:
        nav += '<button class="nav-trigger'+(' active' if active==key else '')+'" id="'+key+'-nav-trigger" data-nav-menu="'+key+'" aria-expanded="false" aria-controls="'+key+'-nav-panel">'+label+'<span class="nav-chevron" aria-hidden="true"></span></button>'
    nav += '<a href="'+href('about/',prefix)+'"'+(' class="active" aria-current="page"' if page=='about' else '')+'>About</a>'
    panels = ''
    for key,data in [('network',NETWORK),('studio',STUDIO),('experiences',EXPERIENCES),('resources',RESOURCES)]:
        compact=key in ('experiences','resources')
        intro = ''
        feature = ''
        if not compact:
            title = 'A room for<br><em>the real you.</em>' if key=='network' else 'Your purpose.<br><em>Our craft.</em>'
            description = 'A private peer community for senior pastors and ministry leaders.' if key=='network' else 'Brand, digital, web, production, and church media.'
            route = 'network/' if key=='network' else 'services/'
            intro = '<div class="nav-panel-intro"><p class="eyebrow">'+('The Network' if key=='network' else 'Ascend Studio')+'</p><h2>'+title+'</h2><p>'+description+'</p><a class="quiet-link" href="'+href(route,prefix)+'">Explore '+('the Network' if key=='network' else 'the Studio')+' <span>↗</span></a></div>'
            photo='conversation.jpg' if key=='network' else 'creative.jpg'
            feature='<a class="site-menu-photo" href="'+href('network/#founding' if key=='network' else 'portfolio/',prefix)+'"><img src="'+prefix+'assets/'+photo+'" alt="'+('Leaders sharing a conversation' if key=='network' else 'Creative team at work')+'"><span>'+('Find your seat at the table.' if key=='network' else 'Explore the work.')+' ↗</span></a>'
        panels += '<div class="nav-panel site-nav-panel '+('nav-compact ' if compact else '')+key+'-panel" role="region" id="'+key+'-nav-panel" aria-labelledby="'+key+'-nav-trigger" hidden>'+intro+'<div class="site-menu-groups">'+groups(data,prefix)+'</div>'+feature+'</div>'
    mobile='<a href="'+href('',prefix)+'">Home <span>00</span></a>'
    for key,label,data in [('network','The Network',NETWORK),('studio','Ascend Studio',STUDIO),('experiences','Experiences',EXPERIENCES),('resources','Resources',RESOURCES),('about','About',ABOUT)]:
        mobile+='<details class="mobile-nav-group"><summary>'+label+'<span aria-hidden="true">+</span></summary><div>'+groups(data,prefix)+'</div></details>'
    return '''<div class="announcement"><span>A new room for the people who lead.</span><a href="'''+href('network/#founding',prefix)+'''">Founding invitations · February 2027 <span>↗</span></a></div>
<header class="site-header"><a class="brand" href="'''+href('',prefix)+'''" aria-label="Ascend Brand Network home"><img src="'''+prefix+'''assets/logo-dark.png" alt="Ascend Brand Network" width="178" height="40"></a><nav class="desktop-nav" aria-label="Main navigation">'''+nav+'''</nav>'''+panels+'''<a class="header-contact text-button" href="'''+href('work-with-us/',prefix)+'''">Let’s Connect <span>↗</span></a><button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span></button><div class="reading-progress" aria-hidden="true"><span></span></div></header><div class="navigation-scrim" hidden></div><nav class="mobile-menu" id="mobile-menu" aria-label="Mobile navigation" hidden><p class="eyebrow mobile-menu-intro">Ascend Brand Network</p>'''+mobile+'''<a class="button button-green" href="'''+href('work-with-us/',prefix)+'''">Let’s Connect <span>↗</span></a></nav>'''

def footer(prefix):
    data=[('The Network', [('Network Overview','network/#overview'),('Founding Membership','network/#founding'),('Membership Process','network/#process'),('Shepherd’s Roundtable','roundtable/'),('Membership FAQs','network/#faqs')]),('Ascend Studio',[('All Services','services/#services'),('Churches & Ministries','churches-ministries/'),('Real Estate Professionals','real-estate/'),('Portfolio','portfolio/#projects'),('Our Process','services/#process'),('Request a Consultation','work-with-us/#studio')]),('Explore ABN',[('About ABN','about/'),('Experiences','experiences/'),('Leadership Dinners','experiences/#dinners'),('Leadership Retreats','experiences/#retreats'),('The Shepherd’s Diary','resources/#diary'),('Resource Center','resources/')]),('Information',[('Contact','work-with-us/#general')])]
    cols=''.join('<div class="footer-column"><span class="eyebrow">'+title+'</span>'+''.join('<a href="'+href(route,prefix)+'">'+escape(label)+'</a>' for label,route in links)+'</div>' for title,links in data)
    return '<footer class="site-footer"><div class="footer-main page-width"><div class="footer-brand"><a href="'+href('',prefix)+'"><img src="'+prefix+'assets/logo-light.png" alt="Ascend Brand Network" width="190" height="42"></a><p>For the Leaders.<br><em>For the Mission.</em></p><span>Nationwide, United States</span></div>'+cols+'</div><div class="footer-bottom page-width"><span>© 2026 Ascend Brand Network</span><span>Where Faith Leads, We Build.</span><span class="concept-label">Independent redesign concept</span></div></footer>'

def hero(eyebrow,title,description,image,cta='studio'):
    return '<section class="interior-hero page-width"><div><p class="breadcrumbs"><a href="../index.html">Home</a><span>/</span>'+escape(eyebrow)+'</p><p class="eyebrow">'+escape(eyebrow)+'</p><h1>'+title+'</h1><p class="interior-lead">'+description+'</p><button class="button button-green" data-contact="'+cta+'">'+('Request consideration' if cta=='network' else 'Let’s connect')+' <span>↗</span></button></div><div class="interior-image"><img src="assets/'+image+'" alt="'+escape(eyebrow)+'" fetchpriority="high"></div></section>'

def block(id,kicker,title,body):
    return '<section class="interior-section page-width" id="'+id+'"><div><p class="eyebrow">'+kicker+'</p><h2>'+title+'</h2></div><div class="interior-content">'+body+'</div></section>'

def cards(items):
    return '<div class="interior-cards">'+''.join('<article><span class="eyebrow">'+str(i+1).zfill(2)+'</span><h3>'+title+'</h3><p>'+text+'</p></article>' for i,(title,text) in enumerate(items))+'</div>'

def faqs(items):
    return ''.join('<details class="interior-faq"><summary>'+q+'<span>+</span></summary><p>'+a+'</p></details>' for q,a in items)

def action(type,label):
    return '<button class="button button-green" data-contact="'+type+'">'+label+' <span>↗</span></button>'

network=hero('The Network','Leadership is<br><em>better together.</em>','A private peer network for senior pastors and ministry leaders, built on trust, shared perspective, and meaningful relationships.','conversation.jpg','network')
network+=block('overview','The community','A place beyond<br><em>the platform.</em>','<p>The Network supports the person carrying the responsibility. It is being developed as a nationwide, independent, non-denominational community.</p>')
network+=block('why','Why the Network exists','Perspective changes<br><em>what comes next.</em>','<p>Senior leadership brings decisions and pressures that are difficult to explain outside the role. A trusted circle creates space to exchange experience and ask honest questions.</p>')
network+=block('experience','Member experience','Small rooms.<br><em>Lasting relationships.</em>',cards([('The Shepherd’s Roundtable','Quarterly peer conversations with 8–12 leaders. The inaugural gathering is planned for June 2027.'),('Dinners & retreats','Private meals and time away, designed around connection.'),('Between gatherings','Relationships that continue after the room empties.'),('Ascend Studio','Creative support for the organisations members lead.')]))
network+=block('values','Community values','Trust is<br><em>the foundation.</em>',cards([('Equal voices','Peer discussion without headliners or a spectator audience.'),('Confidentiality','Conversations are kept private; sharing requires consent.'),('Intentionally small','Gatherings are sized for participation.'),('Long-term connection','Value grows through continuing relationships.')]))
network+=block('founding','Founding membership','The first <em>50.</em>','<p>Founding invitations are planned to begin in February 2027. Expressions of interest are reviewed individually; submitting a request does not guarantee membership.</p>'+action('network','Request membership consideration'))
network+=block('who','Who can join','Already leading.<br><em>Still growing.</em>','<p>Designed for senior and founding pastors, executive pastors, ministry directors, and ministry leaders with significant organisational responsibility.</p>')
network+=block('process','Membership process','A personal<br><em>beginning.</em>',cards([('Consideration request','Introduce yourself and the work you lead.'),('Private call','A 20-minute conversation about fit.'),('A clear response','A personal answer following the conversation.'),('Formal invitation','Founding invitations planned from February 2027.')]))
network+=block('faqs','Membership FAQs','A little<br><em>more clarity.</em>',faqs([('Is membership open to everyone?','Membership is considered individually for experienced senior ministry leaders.'),('Where will gatherings happen?','Locations across the United States are being considered. Confirmed details are shared with invited leaders.'),('Is there a denominational affiliation?','The Network is independent and non-denominational.')]))

services=hero('Ascend Studio','A clear mission.<br><em>A stronger presence.</em>','Strategy, design, digital, and production expertise for churches, ministries, and purpose-led organisations.','creative.jpg')
s=section('studio').replace('id="studio"','id="services"',1)
for i,id in enumerate(['brand','marketing','web','events','media']):
    s=s.replace('<details class="service"'+(' open' if i==0 else '')+'>','<details class="service" id="'+id+'"'+(' open' if i==0 else '')+'>',1)
services+=s
services+=block('faith','Who we serve','Purpose comes<br><em>in many forms.</em>',cards([('Churches & ministries','Branding, communication, websites, production, and systems for congregations.'),('Real estate professionals','Personal identity, digital presence, content, and video for agents and brokers.'),('Faith-driven organisations','Creative services scoped around the needs of nonprofits and mission-led businesses.')]))
services+=block('process','Our process','Thoughtful from<br><em>the start.</em>',cards([('Strategy call','Begin with a free 30-minute conversation.'),('Discovery','Understand the brand, platforms, and goals.'),('Proposal','Agree a practical scope and roadmap.'),('Build & launch','Create, review, test, hand over, and optimise.')]))
services+=block('faqs','Project FAQs','Before we<br><em>begin.</em>',faqs([('How are projects priced?','Each project is scoped individually after the first conversation.'),('How long will it take?','Scope and content readiness determine the timeline, which is agreed in the proposal.'),('Can you work outside our city?','Most work can be delivered remotely; on-site production and installation are scoped separately.')]))

portfolio=hero('Portfolio','Purpose,<br><em>made visible.</em>','A curated selection from the Ascend Studio founding team’s portfolio of 47 websites.','brand.webp')+section('work').replace('id="work"','id="projects"',1)
experiences=hero('Experiences','A different room.<br><em>A deeper connection.</em>','Private gatherings for senior ministry leaders. Small groups, thoughtful settings, and room for honest conversation.','retreat.webp','network')
e=section('experiences').replace('data-experience="dinner"','id="dinners" data-experience="dinner"',1).replace('data-experience="retreat"','id="retreats" data-experience="retreat"',1)
experiences+=e+block('upcoming','Upcoming events','A considered<br><em>2027 calendar.</em>','<div class="calendar-list"><p><strong>February 2027</strong><span>Founding invitations · planned</span></p><p><strong>June 2027</strong><span>Inaugural roundtable · planned</span></p><p><strong>Date to be announced</strong><span>Atlanta leadership dinner · planned</span></p><p><strong>Q3 2027</strong><span>Inaugural retreat · planned</span></p></div>'+action('updates','Receive experience updates'))
roundtable=hero('The Shepherd’s Roundtable','A trusted room.<br><em>An honest conversation.</em>','An invitation-only peer gathering for senior pastors and ministry leaders.','conversation.jpg','network')
roundtable+=block('format','The format','Every voice<br><em>at the table.</em>',cards([('Opening context','A question from the group establishes a starting point.'),('Open conversation','Peers share experience and perspective.'),('Closing commitments','Each participant identifies a decision or next step.'),('Follow-through','Connection continues between gatherings.')]))
roundtable+=block('inaugural','Inaugural gathering','June 2027.<br><em>Planned with intention.</em>','<p>Quarterly sessions of 8–12 leaders are planned. Locations and final details are shared with invited participants.</p>'+action('network','Request consideration'))

resources=hero('Resource Center','A little more<br><em>perspective.</em>','A podcast, practical guides, and tools are being prepared. The collections below are not yet published.','podcast.jpg','updates')
resources+=section('journal').replace('id="journal"','id="diary"',1)
resources+=block('library','The library','Ideas for the<br><em>work ahead.</em>','<div class="resource-list">'+''.join('<article id="'+id+'"><span class="eyebrow">Coming soon</span><h3>'+title+'</h3><p>'+desc+'</p></article>' for id,title,desc in [('leadership-insights','Leadership & Ministry Insights','Perspective on the decisions leaders carry.'),('church-branding','Church Branding Resources','Identity and messaging for congregations.'),('digital-marketing','Digital Marketing Insights','Purposeful communication across digital channels.'),('real-estate-branding','Real Estate Branding Resources','Positioning and presence for agents and brokers.')])+'</div>')
resources+=block('downloads','Free downloads','Tools in<br><em>preparation.</em>',cards([('The Church Brand Audit Checklist','A forthcoming church digital-presence assessment.'),('The Faith-Based Agent Brand Toolkit','Forthcoming positioning guidance for values-driven agents.')])+action('updates','Notify me when resources are ready'))

about=hero('About ABN','Supporting the leader.<br><em>Strengthening the work.</em>','Two complementary divisions, connected by a commitment to people and purpose.','church.webp')
about+=block('story','Our story','Two needs.<br><em>One organisation.</em>','<p>The Network supports the people leading. Ascend Studio supports the organisations and work they are building.</p>')
about+=block('mission','Our mission','People first.<br><em>Purpose always.</em>','<p>Supporting leaders through trusted relationships, while strengthening the way their organisations communicate and operate.</p>')
about+=block('values','Our values','How we build<br><em>matters.</em>',cards([('Relationships','Understand people before recommending solutions.'),('Clarity','Define the need before adding complexity.'),('Purpose','Connect creative decisions to meaningful objectives.'),('Integrity','Communicate expectations and commitments clearly.')]))
about+=block('ecosystem','The ABN ecosystem','Distinct ways<br><em>to serve.</em>','<div class="interior-link-list">'+''.join('<a href="../'+url+'">'+label+' <span>↗</span></a>' for label,url in [('The Network','network/'),('The Shepherd’s Roundtable','roundtable/'),('Experiences','experiences/'),('Ascend Studio','services/'),('The Shepherd’s Diary','resources/#diary')])+'</div>')

churches=hero('Churches & Ministries','Your church,<br><em>beyond Sunday.</em>','A clearer identity, a welcoming digital presence, and dependable production for the congregation you serve.','church.webp')
churches+=block('solutions','Church solutions','A message worth<br><em>being heard.</em>',cards([('Identity & messaging','Reflect who your church is and where it is going.'),('Websites & content','Make service times, next steps, sermons, and events easier to find.'),('Media & production','Support worship, live events, and streaming with workable systems.')]))
churches+=block('work','Selected church work','A welcoming<br><em>first encounter.</em>','<a class="interior-project" href="../portfolio/#projects"><img src="assets/springs-gate.webp" alt="Springs Gate Chapel website"><span>Springs Gate Chapel · Explore selected work ↗</span></a>')
realestate=hero('Real Estate Professionals','Your reputation.<br><em>Clearly expressed.</em>','Branding, listings-ready websites, content, and video for agents, brokers, and property businesses.','creative.jpg')
realestate+=block('solutions','For agents & brokers','Stand for<br><em>something.</em>',cards([('Personal brand','An identity and voice distinct from a brokerage template.'),('Your digital home','Present listings, local expertise, and clear enquiry paths.'),('Content & video','Stay visible between transactions.')]))
realestate+=block('work','Selected property work','A stronger<br><em>presence.</em>','<a class="interior-project" href="../portfolio/#projects"><img src="assets/cire-homes.webp" alt="Cire Homes website"><span>Cire Homes · Explore selected work ↗</span></a>')
contact=hero('Let’s Connect','Start with<br><em>a conversation.</em>','Choose the right starting point. These presentation forms validate locally without sending or storing information.','dinner.jpg')
contact+=block('paths','Choose your path','What brings<br><em>you here?</em>','<div class="contact-paths">'+''.join('<button id="'+id+'" data-contact="'+mode+'"><span class="eyebrow">'+label+'</span><h3>'+title+'</h3><p>'+text+'</p><span class="quiet-link">Begin <span>↗</span></span></button>' for id,mode,label,title,text in [('network','network','The Network','Membership consideration','Introduce yourself and the ministry you lead.'),('studio','studio','Ascend Studio','Request a consultation','Begin with a free 30-minute strategy conversation.'),('experience','updates','Experiences','Gathering updates','Hear about planned dinners, retreats, and roundtables.'),('general','general','General','Something else?','Questions, collaborations, and general enquiries.')])+'</div>')

PAGES={'network':('The Network',network),'services':('Ascend Studio',services),'portfolio':('Portfolio',portfolio),'experiences':('Experiences',experiences),'roundtable':('The Shepherd’s Roundtable',roundtable),'resources':('Resource Center',resources),'about':('About ABN',about),'churches-ministries':('Churches & Ministries',churches),'real-estate':('Real Estate Professionals',realestate),'work-with-us':('Let’s Connect',contact)}

head=SOURCE[SOURCE.index('<head>'):SOURCE.index('</head>')+7]
head=head.replace('</head>','  <link rel="stylesheet" href="site.css">\n</head>')
dialogs=SOURCE[SOURCE.index('  <dialog id="contact-dialog"'):SOURCE.index('</body>')]
home_main=SOURCE[SOURCE.index('  <main id="main">'):SOURCE.index('  <footer')]
home_main=home_main.replace('href="#network"','href="network/"').replace('href="#studio"','href="services/"')
# Keep the immersive homepage, while its larger chapter calls now lead to pages.
home_main=home_main.replace('href="#about"','href="about/"')

def render(page,title,content):
    prefix='' if page=='home' else '../'
    h=head if page=='home' else re.sub(r'<title>.*?</title>','<title>'+escape(title)+' | Ascend Brand Network</title>',head)
    if page!='home':
        content='<main id="main">'+content+'</main>'
        content=re.sub(r'(src=")assets/',r'\1../assets/',content)
        content=content.replace('href="#network"','href="../network/"').replace('href="#studio"','href="../services/"')
        # All shared assets resolve against this page, not the domain root.
        h=re.sub(r'(href=")(assets/|styles.css|refinements.css|site.css)',r'\1../\2',h)
        h=h.replace('src="app.js"','src="../app.js"')
    d=dialogs.replace('src="assets/','src="'+prefix+'assets/')
    return '<!doctype html>\n<html lang="en">\n'+h+'\n<body data-page="'+page+'"><a class="skip-link" href="#main">Skip to content</a>'+navigation(prefix,page)+content+footer(prefix)+'<button class="back-to-top" aria-label="Back to top" hidden>↑</button>'+d+'</body></html>\n'

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'index.html').write_text(render('home','Home',home_main),encoding='utf-8')
for page,(title,content) in PAGES.items():
    directory=OUT/page;directory.mkdir(parents=True,exist_ok=True)
    (directory/'index.html').write_text(render(page,title,content),encoding='utf-8')
(OUT/'.nojekyll').write_text('',encoding='utf-8')
if OUT!=ROOT:
    for name in ('styles.css','refinements.css','site.css','app.js'):
        shutil.copy2(ROOT/name,OUT/name)
    shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
print('Built homepage +',len(PAGES),'static demo destinations in',OUT)
