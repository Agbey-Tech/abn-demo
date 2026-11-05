"""Content and component helpers for the Ascend redesign."""
import json
from pathlib import Path
from html import escape as e
ROOT=Path(__file__).resolve().parents[1]
INVENTORY=json.loads((ROOT/'content/projects.json').read_text(encoding='utf-8'))
SELECTED=['rengovtech-dubai','cire-homes','the-base-marketing','springs-gate-chapel','faircross','recharge-global']
PROJECTS=[next(p for p in INVENTORY if p['slug']==slug) for slug in SELECTED]
ORIGINAL=json.loads((ROOT/'content/original-site.json').read_text(encoding='utf-8'))
SERVICES=[
 dict(slug='websites',id='web',name='Website & App Development',short='Websites',line='A better first impression. A clearer next step.',text='Custom websites and companion apps that help visitors find information and take action, with a CMS your team can manage.',items=['Custom websites for businesses and organisations','Custom church websites, not templates','Companion apps: giving, sermons, events, groups','Real estate websites and lead-capture pages','Maintenance and optimisation'],image='base-marketing.webp'),
 dict(slug='platforms',id='platforms',name='Platforms & Web Applications',short='Platforms',line='Give your ideas a place to work.',text='Purpose-built platforms and web applications, shaped around the people using them and the work they need to do.',items=['Understand users, roles and core journeys','Define the platform scope and priorities','Design and build the agreed experience','Test, launch and hand over'],image='rengovtech.webp'),
 dict(slug='systems',id='systems',name='Business Systems',short='Systems',line='Build around the way your business works.',text='Digital systems that bring structure to business workflows. We begin with your process, then define what needs to connect and what your team needs to manage.',items=['Map the existing workflow','Identify practical requirements','Design the agreed system and connections','Prepare your team for handover'],image='creative.jpg'),
 dict(slug='brand',id='brand',name='Brand Strategy & Identity',short='Brand & identity',line='Make who you are unmistakable.',text='Complete brand systems: identity, visual language, messaging and governance that give an organisation authority in its community.',items=['Visual identity system: logo suite, colour, typography','Messaging framework and brand voice','Brand governance for internal and vendor use','Rebrands for growing or multi-site congregations'],image='brand.webp'),
 dict(slug='marketing',id='marketing',name='Digital Marketing & Content',short='Marketing & content',line='Keep the conversation going.',text="Social strategy, content production, email, SEO and end-to-end podcast production for businesses and organisations. For ministries, digital systems help Sunday’s message travel through the week.",items=['Social media strategy and content calendars','Paid media on Meta, Google and other platforms','SEO and local search','Podcast production, recording to distribution'],image='creative.jpg'),
 dict(slug='production',id='events',name='Event & Video Production',short='Events & production',line='Every detail handled. Every moment captured.',text='Planning, on-site coordination and professional video for conferences, outreach events, launches, client events and open houses.',items=['End-to-end event planning and coordination','Multi-day conference and retreat logistics','Video production and post-production','Event photography'],image='creative.jpg'),
 dict(slug='church-media',id='media',name='Church Media Systems',short='Church media',line='Let the message come through.',text='Design, sourcing and installation of cameras, lighting, sound, LED and streaming, with training so your team can run it.',items=['Full media system design','Equipment sourcing and procurement','Installation and cable management','Streaming, live and on demand','Team training and technical support'],image='church-media.jpg')]
PROCESS=[('Free Strategy Call','30 minutes on where you are and where you need to go.'),('Discovery & Assessment','A structured review of your brand, platforms and goals.'),('Strategy & Proposal','A prioritised roadmap scoped to your capacity and budget.'),('Build & Execute','Delivery with regular check-ins on progress and timelines.'),('Launch & Optimise','Deployment, testing and an active post-launch period.')]
VALUES=[('Relationships Before Transactions','Understanding people and their needs before recommending solutions.'),('Clarity Before Complexity','Define the problem first, not add unnecessary services or technology.'),('Purpose Behind Creativity','Design, communication and technology serve meaningful objectives.'),('Integrity in Every Commitment','Expectations, responsibilities and limitations, communicated clearly.')]
TEAM=[('KJ','Kobin Johnson','Executive Director'),('SI','Saad Iftikhar','CEO'),('AH','Ahmed Haseeb','Full Stack Developer'),('AA','Ali Abbas','Developer'),('BA','Bashir Ahmed','SEO Expert'),('AM','Adil Mumtaz','Marketing Head')]
def link(url,label,cls='text-link'):
 return f'<a class="{cls}" href="@{url}">{label}<span aria-hidden="true">↗</span></a>'
def image(file,alt,cls='',eager=False):
 return f'<img class="{cls}" src="@{file if file.startswith("assets/") else "assets/"+file}" alt="{e(alt)}" {"fetchpriority=high" if eager else "loading=lazy"} decoding="async">'
def section(kicker,title,body,id='',cls=''):
 return f'<section class="section wrap {cls}"'+(f' id="{id}"' if id else '')+f'><div class="section-heading"><p class="eyebrow">{kicker}</p><h2>{title}</h2></div>{body}</section>'
def rows(items):
 return '<div class="editorial-rows">'+''.join(f'<article class="editorial-row"><span class="index">{i:02}</span><h3>{title}</h3><p>{text}</p></article>' for i,(title,text) in enumerate(items,1))+'</div>'
def faq(key):
 data=ORIGINAL[key]
 return '<div class="faqs">'+''.join(f'<details><summary>{e(x["question"])}<span aria-hidden="true">+</span></summary><p>{e(x["answer"].removeprefix(x["question"]))}</p></details>' for x in data)+'</div>'
def intro(kicker,title,text,photo=None,cls=''):
 return f'<section class="page-intro wrap {cls}"><div><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="lead">{text}</p></div>'+('<div class="intro-media">'+image(photo,kicker,eager=True)+'</div>' if photo else '')+'</section>'
def project(slug):return next(p for p in PROJECTS if p['slug']==slug)
def project_card(p,small=False):
 art=image(p['image'],p['name']+' original website preview') if p['image'] else f'<span class="type-art">{e(p["name"])}</span>'
 return f'<a class="project-card {"compact" if small else ""}" href="@work/{p["slug"]}/"><div class="project-art">{art}<span class="project-arrow" aria-hidden="true">↗</span></div><div class="project-caption"><h3>{e(p["name"])}</h3><span>{e(p["sector"])}</span></div></a>'
def project_grid(slugs):return '<div class="project-grid">'+''.join(project_card(project(s)) for s in slugs)+'</div>'
def service_rows():
 return '<div class="service-rows">'+''.join(f'<article class="service-row" id="{s["id"]}"><span class="index">{i:02}</span><div><h3>{link("services/"+s["slug"]+"/",s["name"])}</h3><p>{s["text"]}</p></div><span class="service-type">{ "Digital" if i<4 else "Creative"}</span></article>' for i,s in enumerate(SERVICES,1))+'</div>'
def network_nav():
 return '<nav class="network-subnav wrap" aria-label="Network pages">'+''.join(link(u,t) for u,t in [('network/','The Network'),('roundtable/','The Roundtable'),('experiences/','Experiences'),('resources/','Resources')])+'</nav>'
def contact_link(mode='studio',label='Start a conversation'):return link('contact/#'+mode,label,'button')
def tag(text):return f'<span class="tag">{text}</span>'
def callout(title,text,url,label):return f'<div class="callout"><div><h2>{title}</h2><p>{text}</p></div>{link(url,label,"button")}</div>'
