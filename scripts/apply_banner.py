from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

hero_pattern = r'<section class="hero">[\s\S]*?</section>\n\n<section class="v3-section" id="about">'
new_hero = '''<section class="hero heroBanner" aria-labelledby="hero-title">
  <div class="container heroBannerInner">
    <div class="heroBannerBrand" aria-label="Circularity Toolkit">
      <span class="heroBannerMark" aria-hidden="true">↻</span>
      <span>Circularity Toolkit</span>
    </div>
    <div class="heroBannerCopy">
      <span class="heroBannerKicker">Decision support for circular material systems</span>
      <h1 id="hero-title">Design, run and scale<br>circular systems that <span>work.</span></h1>
      <p>Practical guidance and diagnostics for the decisions that determine whether material-recovery systems perform — from feedstock and operations to markets and economics.</p>
    </div>
    <nav class="heroBannerLinks" aria-label="Toolkit shortcuts">
      <a href="#tools"><strong>10</strong><span>practitioner modules</span></a>
      <a href="#health-check"><span class="heroShortcutIcon" aria-hidden="true">⌁</span><span>Facility health diagnostic</span></a>
      <a href="#planner"><span class="heroShortcutIcon" aria-hidden="true">↗</span><span>Recovery system planner</span></a>
    </nav>
    <div class="heroBannerFooter">
      <span>Circularity Toolkit · Practitioner decision support</span>
      <span>Feedstock · Operations · Markets · Economics</span>
    </div>
  </div>
</section>

<section class="v3-section systemMapSection" id="system-map">
  <div class="container">
    <div class="systemMapIntro v3-reveal">
      <div>
        <span class="kicker">System map</span>
        <h2>See the whole system before solving one part of it.</h2>
      </div>
      <p>A recovery facility is only one link. Performance depends on what happens before material arrives, what happens inside the facility, and whether recovered material can move into reliable downstream markets.</p>
    </div>
    <div class="systemMapFlow v3-reveal" role="list" aria-label="Four connected stages of a circular material system">
      <a class="systemMapStage" href="#system-pillars" role="listitem">
        <span class="systemMapNum">01</span>
        <span class="systemMapIcon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M10 37V20l14-9 14 9v17M17 37V27h14v10" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round"/><path d="M15 17c3-4 7-6 9-6s6 2 9 6" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg></span>
        <div><strong>Source &amp; segregation</strong><p>What is generated, by whom, and how consistently is it separated?</p></div>
      </a>
      <span class="systemMapArrow" aria-hidden="true">→</span>
      <a class="systemMapStage" href="#tools" role="listitem">
        <span class="systemMapNum">02</span>
        <span class="systemMapIcon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M8 31h23l5-11h-9l-4-7H12l-4 18Z" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linejoin="round"/><circle cx="16" cy="35" r="4" fill="none" stroke="currentColor" stroke-width="2.8"/><circle cx="33" cy="35" r="4" fill="none" stroke="currentColor" stroke-width="2.8"/></svg></span>
        <div><strong>Collection &amp; aggregation</strong><p>Does enough material reach the system, reliably and with manageable contamination?</p></div>
      </a>
      <span class="systemMapArrow" aria-hidden="true">→</span>
      <a class="systemMapStage" href="#health-check" role="listitem">
        <span class="systemMapNum">03</span>
        <span class="systemMapIcon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M10 36h28V17H10v19Z" fill="none" stroke="currentColor" stroke-width="2.8"/><path d="M15 17V11h8v6M29 17V8h7v9M16 27h16M16 32h11" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg></span>
        <div><strong>Recovery &amp; operations</strong><p>Can people, process and infrastructure recover material safely, consistently and at quality?</p></div>
      </a>
      <span class="systemMapArrow" aria-hidden="true">→</span>
      <a class="systemMapStage" href="#planner" role="listitem">
        <span class="systemMapNum">04</span>
        <span class="systemMapIcon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M9 35h30M13 31l8-9 7 5 8-12" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M31 15h5v5" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        <div><strong>Markets &amp; value</strong><p>Does recovered material meet buyer needs and move at a value that supports viability?</p></div>
      </a>
    </div>
    <div class="systemMapPrinciple v3-reveal"><span>Infrastructure is one part of the answer.</span><strong>Design the whole system.</strong></div>
  </div>
</section>

<section class="v3-section" id="about">'''

s, n = re.subn(hero_pattern, new_hero, s, count=1)
if n != 1:
    raise SystemExit(f'Expected one hero section, found {n}')

s = s.replace('<a href="#pathway">Start</a><a href="#tools">Guidance</a>', '<a href="#system-map">System map</a><a href="#pathway">Start</a><a href="#tools">Guidance</a>', 1)
s = s.replace('<li><a href="#pathway">Start</a></li>', '<li><a href="#system-map">System map</a></li><li><a href="#pathway">Start</a></li>', 1)

css = r'''
/* ============ horizontal hero + system map ============ */
.heroBanner{padding:0;min-height:600px;display:flex;align-items:stretch;color:#fff;background:radial-gradient(circle at 88% 20%,rgba(82,137,255,.28),transparent 34%),linear-gradient(112deg,#0b2344 0%,#123f78 54%,#2457b0 100%);position:relative;overflow:hidden}
.heroBanner:after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(rgba(255,255,255,.02) 1px,transparent 1px);background-size:72px 72px;mask-image:linear-gradient(to right,transparent,rgba(0,0,0,.4),transparent);opacity:.3}
.heroBannerInner{position:relative;z-index:1;display:flex;flex-direction:column;padding-top:54px;padding-bottom:52px}
.heroBannerBrand{display:flex;align-items:center;gap:14px;font-size:24px;font-weight:850;letter-spacing:-.025em}.heroBannerMark{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;background:#2f6eff;color:#fff;font-size:27px;box-shadow:0 12px 28px rgba(0,0,0,.14)}
.heroBannerCopy{max-width:960px;margin-top:50px}.heroBannerKicker{display:block;color:#a9c8ff;font-size:11px;font-weight:850;text-transform:uppercase;letter-spacing:.15em;margin-bottom:14px}.heroBanner h1{font-size:clamp(52px,7.1vw,88px);line-height:.91;letter-spacing:-.062em;margin:0;color:#fff;max-width:980px}.heroBanner h1 span{color:#8fb5ff}.heroBannerCopy p{max-width:830px;margin:24px 0 0;color:#c9d9ef;font-size:18px;line-height:1.55}
.heroBannerLinks{display:flex;gap:12px;flex-wrap:wrap;margin-top:34px}.heroBannerLinks a{display:inline-flex;align-items:center;gap:9px;min-height:48px;padding:0 20px;border:1px solid rgba(211,226,250,.32);border-radius:999px;background:rgba(255,255,255,.055);color:#e5eeff;font-weight:760;font-size:15px;transition:background .2s,border-color .2s,transform .2s}.heroBannerLinks a:hover{background:rgba(255,255,255,.11);border-color:rgba(220,233,255,.58);transform:translateY(-2px)}.heroBannerLinks strong{color:#fff;font-size:17px}.heroShortcutIcon{color:#91b8ff;font-size:19px;line-height:1}
.heroBannerFooter{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-top:auto;padding-top:38px;color:#a7c0df;font-size:13px;font-weight:650;letter-spacing:.01em}
.systemMapSection{background:var(--bg);padding-top:78px;padding-bottom:88px}.systemMapIntro{display:grid;grid-template-columns:.95fr 1.05fr;gap:70px;align-items:end;margin-bottom:38px}.systemMapIntro h2{font-size:clamp(34px,4.4vw,54px);line-height:1.04;letter-spacing:-.045em;margin:7px 0 0}.systemMapIntro>p{font-size:17px;color:var(--muted);margin:0;max-width:650px}
.systemMapFlow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;gap:10px;align-items:stretch}.systemMapStage{border:1px solid var(--line);border-radius:22px;padding:20px;background:var(--surface);box-shadow:var(--shadow);display:flex;flex-direction:column;min-height:245px;transition:transform .22s,border-color .22s,box-shadow .22s}.systemMapStage:hover{transform:translateY(-4px);border-color:var(--line-strong);box-shadow:var(--shadow-lift)}.systemMapNum{font-size:11px;font-weight:900;color:var(--brand);letter-spacing:.08em}.systemMapIcon{width:54px;height:54px;border-radius:16px;display:grid;place-items:center;background:var(--brand-soft);color:var(--brand);margin:22px 0 18px}.systemMapIcon svg{width:30px;height:30px}.systemMapStage strong{display:block;font-size:18px;letter-spacing:-.02em;line-height:1.18}.systemMapStage p{font-size:13px;color:var(--muted);margin:8px 0 0;line-height:1.5}.systemMapArrow{display:grid;place-items:center;color:#7fa5e8;font-size:24px}
.systemMapPrinciple{display:flex;justify-content:space-between;gap:24px;align-items:center;margin-top:18px;padding:20px 24px;border-radius:18px;background:linear-gradient(115deg,#0b2344,#17467f);color:#c8d9ef}.systemMapPrinciple strong{color:#fff;font-size:18px}
@media(max-width:1000px){.systemMapFlow{grid-template-columns:1fr 1fr}.systemMapArrow{display:none}.systemMapIntro{grid-template-columns:1fr;gap:16px}.heroBanner{min-height:560px}}
@media(max-width:620px){.heroBannerInner{padding-top:38px;padding-bottom:36px}.heroBannerBrand{font-size:20px}.heroBannerMark{width:42px;height:42px}.heroBannerCopy{margin-top:38px}.heroBanner h1{font-size:49px}.heroBannerCopy p{font-size:16px}.heroBannerLinks{display:grid}.heroBannerLinks a{width:100%;justify-content:flex-start}.heroBannerFooter{font-size:12px}.systemMapFlow{grid-template-columns:1fr}.systemMapStage{min-height:0}.systemMapPrinciple{align-items:flex-start;flex-direction:column;gap:6px}}
'''

if 'horizontal hero + system map' not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')
print('Patched index.html')
