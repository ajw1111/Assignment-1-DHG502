import pandas as pd

df = pd.read_csv('/Users/wongtinho/Downloads/明史_傳教士_collocates.csv')
ct = pd.read_csv('/Users/wongtinho/Downloads/明史_傳教士_contingency.csv')
kw = pd.read_csv('/Users/wongtinho/Downloads/明史_傳教士_kwic.csv')

TARGETS = ['利瑪竇', '湯若望', '龐迪峨']
FREQ = {'利瑪竇': 12, '湯若望': 7, '龐迪峨': 10}
KWIC_COUNT = {'利瑪竇': 12, '湯若望': 7, '龐迪峨': 3}
N = 1509138


def fmt_p(p):
    return f"{p:.2e}" if p < 1e-4 else f"{p:.4f}"


def contingency_html(r):
    return f"""<table class="ct">
<tr><td class="hdr"></td><td class="hdr">collocate</td><td class="hdr">other</td><td class="hdr">Σ</td></tr>
<tr><td class="hdr">target</td><td class="o11">{r.O11}</td><td>{r.O21}</td><td class="marg">{r.R1}</td></tr>
<tr><td class="hdr">other</td><td>{r.O12}</td><td>{r.O22:,}</td><td class="marg">{r.N - r.R1:,}</td></tr>
<tr><td class="hdr">Σ</td><td class="marg">{r.C1}</td><td class="marg">{r.N - r.C1:,}</td><td class="marg">{r.N:,}</td></tr>
</table>"""


# ---------- bar chart data (top 8 logDice per target) ----------
chart_data = {}
for t in TARGETS:
    sub = df[df['target'] == t].sort_values('log_dice', ascending=False).head(8)
    chart_data[t] = list(zip(sub['collocate'], sub['log_dice']))

bars_html = []
for t, pairs in chart_data.items():
    max_v = max(v for _, v in pairs) if pairs else 1
    rows = []
    for w, v in pairs:
        pct = v / max_v * 100
        rows.append(f"""<div class="bar-row">
<span class="bar-label">{w}</span>
<div class="bar-track"><div class="bar-fill" style="width:{pct:.1f}%"></div></div>
<span class="bar-val">{v:.2f}</span>
</div>""")
    bars_html.append(f"""
<div class="chart-card">
<h3>{t} <span class="small">(f={FREQ[t]})</span></h3>
{''.join(rows)}
</div>""")

# ---------- tables ----------
sections = []
ct_idx = ct.set_index(['target', 'collocate'])
for t in TARGETS:
    sub = df[df['target'] == t].sort_values('log_dice', ascending=False)
    trs = []
    for _, r in sub.iterrows():
        c = ct_idx.loc[(t, r['collocate'])]
        trs.append(f"""<tr>
<td class="coll">{r['collocate']}</td>
<td class="num">{int(r['obs_local'])}</td>
<td class="num">{r['exp_local']:.4f}</td>
<td class="num">{r['ratio_local']:,.1f}</td>
<td class="num">{int(r['obs_global']):,}</td>
<td>{contingency_html(c)}</td>
<td class="num">{fmt_p(r['p_value'])}</td>
<td class="num strong">{r['log_dice']:.2f}</td>
<td class="num">{r['t_score']:.2f}</td>
<td class="num">{r['mi']:.2f}</td>
<td class="num">{r['log_likelihood']:.2f}</td>
</tr>""")
    sections.append(f"""
<h2>Target: {t} <span class="freq">(corpus freq: {FREQ[t]})</span></h2>
<table class="main">
<thead><tr>
<th>Collocate</th><th>obs<br>local</th><th>exp<br>local</th><th>ratio<br>local</th>
<th>obs<br>global</th><th>Contingency table<br><span class="small">rows: target / other; cols: collocate / other</span></th>
<th>p-value<br>(Fisher, &gt;)</th><th>logDice</th><th>t-score</th><th>MI</th><th>log-lik</th>
</tr></thead>
<tbody>{''.join(trs)}</tbody>
</table>""")

# ---------- KWIC section ----------
kwic_sections = []
for t in TARGETS:
    sub = kw[kw['node'] == t]
    trs = []
    for _, r in sub.iterrows():
        trs.append(f"""<tr>
<td class="kw-juan">{r['section']}·卷{int(r['juan'])}</td>
<td class="kw-left">{r['left']}</td>
<td class="kw-node">{r['node']}</td>
<td class="kw-right">{r['right']}</td>
</tr>""")
    juans = sorted(set((r['section'], int(r['juan'])) for _, r in sub.iterrows()),
                   key=lambda x: x[1])
    juan_str = ', '.join(f'{s}·卷{j}' for s, j in juans)
    kwic_sections.append(f"""
<h3>{t} <span class="small">({len(sub)} lines — appears in {juan_str})</span></h3>
<table class="kwic">
<thead><tr><th class="w-juan">Section</th><th class="w-left">Left context</th><th class="w-node">Node</th><th class="w-right">Right context</th></tr></thead>
<tbody>{''.join(trs)}</tbody>
</table>""")

kwic_html = f"""
<h2>KWIC Concordance <span class="freq">(window ±10 tokens, corpus order)</span></h2>
{''.join(kwic_sections)}"""

html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>明史 Collocates — 利瑪竇 / 湯若望 / 龐迪峨 (h10, logDice)</title>
<style>
body {{ font-family: "PingFang TC", "Hiragino Sans", sans-serif; margin: 2rem; color: #222; background: #fafafa; }}
h1 {{ font-size: 1.5rem; }}
h2 {{ font-size: 1.15rem; margin-top: 2rem; border-left: 4px solid #4a6fa5; padding-left: .5rem; }}
h3 {{ font-size: 1rem; margin: .2rem 0 .6rem; }}
.meta {{ color: #666; font-size: .9rem; }}
.freq {{ color: #888; font-size: .85rem; font-weight: 400; }}
table.main {{ border-collapse: collapse; background: #fff; font-size: .85rem; margin-top: .8rem; box-shadow: 0 1px 3px rgba(0,0,0,.08); }}
table.main th, table.main td {{ border: 1px solid #ddd; padding: .35rem .55rem; }}
table.main th {{ background: #4a6fa5; color: #fff; font-weight: 600; }}
table.main tbody tr:nth-child(even) {{ background: #f4f7fb; }}
td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
td.strong {{ font-weight: 700; color: #1a4d8f; }}
td.coll {{ font-weight: 600; }}
table.ct {{ border-collapse: collapse; font-size: .72rem; }}
table.ct td {{ border: 1px solid #ccc; padding: 1px 6px; text-align: right; font-variant-numeric: tabular-nums; }}
table.ct td.o11 {{ background: #ffe9a8; font-weight: 700; }}
table.ct td.marg {{ background: #eef2f7; color: #555; }}
table.ct td.hdr {{ background: #f7f9fc; color: #4a6fa5; font-weight: 600; font-size: .65rem; text-align: center; }}
.small {{ font-weight: 400; font-size: .7rem; color: #888; }}
.note {{ background: #fff8e1; border-left: 4px solid #f0c040; padding: .6rem 1rem; font-size: .85rem; max-width: 60rem; }}
.charts {{ display: flex; flex-wrap: wrap; gap: 1.2rem; margin-top: 1rem; }}
.chart-card {{ background: #fff; border: 1px solid #e2e6ee; border-radius: 8px; padding: .9rem 1.1rem; box-shadow: 0 1px 3px rgba(0,0,0,.06); min-width: 300px; flex: 1; }}
.bar-row {{ display: flex; align-items: center; gap: .5rem; margin: .28rem 0; }}
.bar-label {{ width: 5.5em; text-align: right; font-size: .82rem; font-weight: 600; flex-shrink: 0; }}
.bar-track {{ flex: 1; background: #eef2f7; border-radius: 4px; height: 1.05rem; overflow: hidden; }}
.bar-fill {{ background: linear-gradient(90deg, #4a6fa5, #6d9bd1); height: 100%; border-radius: 4px; }}
.bar-val {{ width: 3.2em; font-size: .75rem; color: #555; font-variant-numeric: tabular-nums; }}
table.kwic {{ border-collapse: collapse; background: #fff; font-size: .85rem; margin-top: .6rem; box-shadow: 0 1px 3px rgba(0,0,0,.08); width: 100%; }}
table.kwic th, table.kwic td {{ border: 1px solid #ddd; padding: .3rem .55rem; }}
table.kwic th {{ background: #6d9bd1; color: #fff; font-weight: 600; text-align: left; }}
table.kwic tbody tr:nth-child(even) {{ background: #f4f7fb; }}
td.kw-left {{ text-align: right; }}
td.kw-node {{ font-weight: 700; color: #b34700; background: #fff3e6; text-align: center; white-space: nowrap; }}
td.kw-right {{ text-align: left; }}
th.w-left {{ width: 36%; }} th.w-node {{ width: 8%; }} th.w-right {{ width: 50%; }}
th.w-juan {{ width: 6%; }}
td.kw-juan {{ text-align: center; font-weight: 600; color: #4a6fa5; white-space: nowrap; font-size: .78rem; }}
</style>
</head>
<body>
<h1>《明史》Collocate Analysis — Jesuit Missionaries</h1>
<p class="meta">
Targets: 利瑪竇 (Ricci), 湯若望 (Schall), 龐迪峨 (de Pantoja) &nbsp;|&nbsp; Method: <b>window, horizon = 10</b> (±10 words) &nbsp;|&nbsp;
Tokenization: jieba with custom dictionary &nbsp;|&nbsp; Corpus size N = 1,509,139 tokens &nbsp;|&nbsp;
Sorted by <b>logDice</b> &nbsp;|&nbsp; Fisher's exact test, alternative = greater
</p>
<div class="note">
<b>Note:</b> Contingency cells follow Evert (2008): O11 = observed co-occurrence,
R1 = target context size (≈ 2·horizon·f(target)), C1 = collocate corpus frequency,
N = corpus size. R1 is an approximation of the window-position count.
龐迪峨 occurs 10 times counting all variants (龐迪峨 ×1, 龐迪我 ×2, and the
courtesy abbreviations 迪峨 ×4, 迪我 ×3); all were normalized to 龐迪峨
before analysis.
</div>

<h2>Top collocates by logDice</h2>
<div class="charts">{''.join(bars_html)}</div>

{''.join(sections)}

{kwic_html}
</body>
</html>"""

with open('/Users/wongtinho/Downloads/明史_傳教士_collocates.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML saved')