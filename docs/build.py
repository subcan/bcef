#!/usr/bin/env python3
"""Regenerate index.html from the source Markdown. Requires Python 3 and Pandoc."""
from pathlib import Path
import re, subprocess, html
from datetime import date
ROOT = Path(__file__).resolve().parent
SITE = ROOT
source = SITE / 'biblical-creation-epistemic-framework.md'
body = subprocess.check_output(['pandoc', str(source), '--from=markdown-smart+tex_math_single_backslash', '--to=html5', '--mathml', '--wrap=none'], text=True)
body = re.sub(r'<h1[^>]*>.*?</h1>\s*', '', body, count=1, flags=re.S)
headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
def plain(s): return html.unescape(re.sub('<[^>]+>', '', s))
items=[]
for anchor, label in headings:
    label = plain(label)
    match = re.match(r'^(\d+)\. (.*)',label)
    number, title = (match.group(1).zfill(2),match.group(2)) if match else ('—',label)
    items.append(f'<li><a href="#{anchor}"><span class="toc-num">{number}</span><span>{html.escape(title)}</span></a></li>')
toc = '<ol class="toc">'+''.join(items)+'</ol>'
body=re.sub(r'<(h[23]) id="([^"]+)">(.*?)</\1>',lambda m:f'<{m[1]} id="{m[2]}">{m[3]}<a class="permalink" href="#{m[2]}" aria-label="Link to {html.escape(plain(m[3]),quote=True)}">#</a></{m[1]}>',body)
body=re.sub(r'<span class="math display">.*?</span>',lambda m:'<div class="equation" tabindex="0" role="region" aria-label="Equation; scroll horizontally if needed">'+m[0]+'</div>',body,flags=re.S)
# Pandoc places display math in paragraph wrappers; remove those wrappers.
body=re.sub(r'<p>(<div class="equation".*?</div>)</p>',r'\1',body,flags=re.S)
body=re.sub(r'<table>.*?</table>',lambda m:'<div class="table-wrap">'+m[0]+'</div>',body,flags=re.S)
meta=source.read_text().split('---',2)[1]
version=re.search(r'^version: "(.*?)"',meta,re.M)[1]
updated=re.search(r'^last_updated: (.*)',meta,re.M)[1]
page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biblical Creation Epistemic Framework · BCEF</title>
<meta name="description" content="The complete Biblical Creation Epistemic Framework: premises, evidence distinctions, historical boundaries, and procedures for evaluating scientific and historical claims within BCEF.">
<meta name="theme-color" content="#112c44"><link rel="stylesheet" href="assets/style.css"><script defer src="assets/navigation.js"></script></head>
<body id="top"><a class="skip" href="#main">Skip to content</a>
<header class="masthead"><a class="brand" href="#top"><span class="monogram">BCEF</span><span class="brand-text">Biblical Creation Epistemic Framework</span></a><span class="edition">Foundational framework</span></header>
<div class="mobile-nav"><details><summary>Contents · 22 sections</summary><nav aria-label="Mobile contents">{toc}</nav></details></div>
<div class="layout"><aside class="sidebar"><p class="toc-title">In this framework</p><nav aria-label="Document contents">{toc}</nav><a class="source-link" href="biblical-creation-epistemic-framework.md" download>Download Markdown source</a></aside>
<main id="main" tabindex="-1"><header class="document-header"><p class="eyebrow">Scripture · Observation · Inference</p><h1>Biblical Creation<br>Epistemic Framework</h1><div class="metadata"><span>Updated <time datetime="{updated}">{date.fromisoformat(updated).strftime('%d %B %Y').lstrip('0')}</time></span><span>Version {version} · UTC−08:00</span></div></header>
<article class="document" aria-label="Complete framework">{body}</article>
<footer class="footer"><span>Biblical Creation Epistemic Framework</span><a href="biblical-creation-epistemic-framework.md" download>Markdown source</a><a href="#top">Back to top ↑</a></footer></main></div></body></html>'''
(SITE/'index.html').write_text(page)
print(f'Generated {len(headings)} top-level sections, {body.count(chr(60)+"math")} equations and inline expressions.')
