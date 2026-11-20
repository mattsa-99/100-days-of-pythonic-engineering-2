"""Build the Day 04 LinkedIn carousel (7 slides, 1080x1350) as one HTML file.

Usage:
    python3 build.py <theme> <output.html>
    theme: "pino" | "bosque" | "medianoche" (see CLAUDE.md section 3)
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).parent
REPO = ROOT.parents[1]
FONTS = REPO / "design" / "fonts"
TOTAL = 7

FONT_FILES: list[tuple[str, int, str]] = [
    ("Montserrat", 700, "montserrat-latin-700-normal.woff2"),
    ("Montserrat", 800, "montserrat-latin-800-normal.woff2"),
    ("Montserrat", 900, "montserrat-latin-900-normal.woff2"),
    ("Roboto", 400, "roboto-latin-400-normal.woff2"),
    ("Roboto", 500, "roboto-latin-500-normal.woff2"),
    ("Roboto", 700, "roboto-latin-700-normal.woff2"),
    ("Roboto Mono", 400, "roboto-mono-latin-400-normal.woff2"),
    ("Roboto Mono", 500, "roboto-mono-latin-500-normal.woff2"),
]


def font_css() -> str:
    """Return @font-face rules with the font files embedded as base64."""
    rules = []
    for family, weight, rel in FONT_FILES:
        data = base64.b64encode((FONTS / rel).read_bytes()).decode()
        rules.append(
            f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:normal;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}"
        )
    return "\n".join(rules)


def chrome(idx: int, tone: str, swipe: bool = True) -> str:
    """Shared header, footer and progress bar for a slide."""
    segs = "".join(f'<i class="{"on" if i < idx else ""}"></i>' for i in range(TOTAL))
    cue = '<div class="swipe">Desliza &rarr;</div>' if swipe else ""
    return (
        f'<div class="top"><span class="day">D&iacute;a 04 / 100</span>'
        f'<span class="lvl">Avanzado</span></div><div class="rule"></div>'
        f'{cue}'
        f'<div class="foot"><b>Mateo Soto</b><span class="num">{idx:02d} / {TOTAL:02d}</span></div>'
        f'<div class="prog">{segs}</div>'
    )


def slide(idx: int, tone: str, body: str, swipe: bool = True) -> str:
    return f'<section class="slide {tone}">{chrome(idx, tone, swipe)}<div class="body">{body}</div></section>'


# ---------- 01 · portada ----------
def s1() -> str:
    durations = [9, 7, 11, 8, 100, 10, 7, 9]
    rows = []
    for i, w in enumerate(durations, start=1):
        hot = w == 100
        color = "var(--hl)" if hot else "var(--a1)"
        label = '<span style="font-family:Roboto Mono;font-weight:500;font-size:26px;color:#071A22;padding-left:16px">58 min</span>' if hot else ""
        rows.append(
            f'<div style="display:flex;align-items:center;gap:22px;height:46px">'
            f'<span style="font-family:Roboto Mono;font-size:24px;color:var(--mut);width:48px">T{i}</span>'
            f'<div style="flex:1;height:100%;position:relative"><div style="width:{w}%;height:100%;background:{color};'
            f'display:flex;align-items:center">{label}</div></div></div>'
        )
    chart = (
        '<div style="margin-top:44px;display:flex;flex-direction:column;gap:14px">' + "".join(rows) + "</div>"
        '<div style="display:flex;justify-content:space-between;margin-top:22px;font-size:26px;color:var(--mut)">'
        '<span>Resto de tareas: ~2 min c/u</span><span style="font-style:italic">Ilustrativo</span></div>'
    )
    return slide(
        1, "dark",
        '<div style="margin-top:52px"><div class="kicker">Spark &middot; Rendimiento</div>'
        '<h1>Tu job espera una hora por <span class="hl">UNA</span> sola tarea.</h1></div>' + chart,
    )


# ---------- 02 · qué es ----------
def s2() -> str:
    cols = [("P1", 12, "120 mil"), ("P2", 9, "90 mil"), ("P3", 14, "140 mil"), ("P4", 100, "9.8 M")]
    bars = []
    for name, h, rows in cols:
        hot = h == 100
        bg = "var(--a1d)" if hot else "color-mix(in srgb, var(--a1) 45%, var(--icebg))"
        bars.append(
            f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:12px">'
            f'<span style="font-family:Roboto Mono;font-size:24px;font-weight:500;color:{"var(--a1d)" if hot else "var(--mut)"}">{rows}</span>'
            f'<div style="width:100%;height:{h*3.4}px;background:{bg}"></div>'
            f'<span style="font-family:Montserrat;font-weight:800;font-size:26px">{name}</span></div>'
        )
    body = (
        '<div style="margin-top:56px"><div class="kicker">El problema</div>'
        '<h2>Se llama <span class="hl">data skew</span>.</h2>'
        '<p class="lead" style="margin-top:28px">Los datos se reparten mal: una partici&oacute;n recibe casi todo.</p></div>'
        '<div style="display:flex;gap:30px;align-items:flex-end;margin-top:36px;height:480px;border-bottom:3px solid #071A22;padding:0 8px">'
        + "".join(bars) + "</div>"
        '<p class="cap" style="font-size:34px"><b>El stage termina cuando termina la m&aacute;s lenta.</b> '
        'Las dem&aacute;s ya acabaron y el cl&uacute;ster paga por esperar.</p>'
    )
    return slide(2, "light", body)


# ---------- 03 · señales ----------
def s3() -> str:
    items = [
        ("01", "Una tarea dura <b>10x</b> m&aacute;s que la mediana."),
        ("02", "Su <b>Shuffle Read</b> es enorme frente al resto."),
        ("03", "<b>Spill a disco</b> solo en unas pocas tareas."),
    ]
    lines = "".join(
        f'<div style="display:flex;gap:34px;align-items:baseline;padding:26px 0;border-top:2px solid var(--rule)">'
        f'<span style="font-family:Montserrat;font-weight:900;font-size:92px;color:var(--a1l);line-height:1;width:150px">{n}</span>'
        f'<span style="font-size:40px;line-height:1.3">{t}</span></div>'
        for n, t in items
    )
    table = (
        '<div style="margin-top:36px;background:#05141A;border-radius:6px;padding:26px 30px;font-family:Roboto Mono;font-size:25px">'
        '<div style="color:var(--mut);margin-bottom:14px">Stage &rarr; Summary Metrics &rarr; Duration</div>'
        '<div style="display:flex;justify-content:space-between"><span style="color:var(--mut)">Min</span><span style="color:var(--mut)">Median</span><span style="color:var(--mut)">75th</span><span style="color:var(--hl)">Max</span></div>'
        '<div style="display:flex;justify-content:space-between;margin-top:8px;font-size:30px"><span>1 s</span><span>3 s</span><span>3 s</span><span style="color:var(--hl);font-weight:500">58 min</span></div></div>'
    )
    body = (
        '<div style="margin-top:56px"><div class="kicker">C&oacute;mo detectarlo</div>'
        '<h2>3 se&ntilde;ales en la Spark UI.</h2></div>'
        f'<div style="margin-top:34px">{lines}</div>' + table
    )
    return slide(3, "dark", body)


# ---------- 04 · fixes 1 y 2 ----------
def s4() -> str:
    c1 = (
        '<div class="code" style="font-size:30px;padding:36px 38px"><span class="c"># 1. Fuera las llaves nulas</span>\n'
        'clean = events.<span class="f">filter</span>(\n'
        '    F.<span class="f">col</span>(<span class="s">"customer_id"</span>).<span class="f">isNotNull</span>()\n'
        ')</div>'
        '<p class="cap" style="font-size:34px">Todos los <b>NULL</b> caen en la misma partici&oacute;n.</p>'
    )
    c2 = (
        '<div class="code" style="font-size:27px;padding:36px 38px"><span class="c"># 2. AQE divide particiones sesgadas</span>\n'
        'conf = spark.conf\n'
        'conf.<span class="f">set</span>(<span class="s">"spark.sql.adaptive.enabled"</span>, <span class="s">"true"</span>)\n'
        'conf.<span class="f">set</span>(\n'
        '    <span class="s">"spark.sql.adaptive.skewJoin.enabled"</span>, <span class="s">"true"</span>\n'
        ')</div>'
        '<p class="cap" style="font-size:34px">Revisa que est&eacute; activo en tu runtime.</p>'
    )
    body = (
        '<div style="margin-top:56px"><div class="kicker">Arreglo 1 y 2</div>'
        '<h2>Lo barato, <span class="hl">primero</span>.</h2></div>'
        f'<div style="margin-top:52px">{c1}</div><div style="margin-top:46px">{c2}</div>'
    )
    return slide(4, "light", body)


# ---------- 05 · broadcast ----------
def s5() -> str:
    node = (
        '<div style="flex:1;border:3px solid var(--a1l);padding:26px 20px;display:flex;flex-direction:column;gap:20px">'
        '<div style="height:64px;background:var(--a1)"></div>'
        '<div style="display:flex;align-items:center;gap:12px"><div style="width:30px;height:30px;background:var(--hl)"></div>'
        '<span style="font-family:Roboto Mono;font-size:24px;color:var(--mut)">dim</span></div></div>'
    )
    diagram = (
        '<div style="display:flex;gap:24px;margin-top:48px">' + node * 3 + "</div>"
        '<p style="font-size:29px;color:var(--mut);margin-top:20px">La tabla grande no se mueve. La peque&ntilde;a se copia a cada nodo.</p>'
    )
    code = (
        '<div class="code" style="margin-top:48px;font-size:31px;padding:38px 40px"><span class="k">from</span> pyspark.sql.functions <span class="k">import</span> broadcast\n\n'
        'joined = big.<span class="f">join</span>(<span class="f">broadcast</span>(small), <span class="s">"key"</span>)</div>'
    )
    body = (
        '<div style="margin-top:56px"><div class="kicker">Arreglo 3</div>'
        '<h2>Si la otra tabla es peque&ntilde;a: <span class="hl">broadcast</span>.</h2></div>'
        + diagram + code +
        '<p class="cap" style="font-size:34px">Sin shuffle no hay skew en ese join. Lo vimos en el <b>D&iacute;a 03</b>.</p>'
        '<p class="cap" style="font-size:30px;color:var(--mut);margin-top:14px"><b style="color:#E7F3F1">Ojo:</b> solo si la tabla peque&ntilde;a cabe de sobra en la memoria del executor.</p>'
    )
    return slide(5, "dark", body)


# ---------- 06 · salting ----------
def s6() -> str:
    hot = (
        '<div style="display:flex;align-items:center;gap:20px">'
        '<span style="font-family:Montserrat;font-weight:900;font-size:34px;width:70px">A</span>'
        '<div style="flex:1;height:64px;background:var(--a1d)"></div></div>'
    )
    parts = "".join(
        f'<div style="flex:1;height:64px;background:color-mix(in srgb, var(--a1) 55%, var(--icebg));display:flex;align-items:center;justify-content:center;'
        f'font-family:Roboto Mono;font-weight:500;font-size:26px;color:#071A22">A_{i}</div>'
        for i in range(4)
    )
    diagram = (
        '<div style="margin-top:48px;display:flex;flex-direction:column;gap:20px">' + hot +
        '<div style="padding-left:90px;font-family:Montserrat;font-weight:800;font-size:28px;color:var(--a1d)">&darr; salt</div>'
        '<div style="display:flex;align-items:center;gap:20px"><span style="width:70px"></span>'
        '<div style="flex:1;display:flex;gap:6px">' + parts + "</div></div></div>"
    )
    code = (
        '<div class="code" style="margin-top:34px;font-size:26px;padding:34px 36px">'
        'N = <span class="n">8</span>\n'
        'big = big.<span class="f">withColumn</span>(\n'
        '    <span class="s">"salt"</span>, (F.<span class="f">rand</span>() * N).<span class="f">cast</span>(<span class="s">"int"</span>)\n'
        ')\n'
        'salts = F.<span class="f">array</span>(*[F.<span class="f">lit</span>(i) <span class="k">for</span> i <span class="k">in</span> <span class="f">range</span>(N)])\n'
        'small = small.<span class="f">withColumn</span>(<span class="s">"salt"</span>, F.<span class="f">explode</span>(salts))\n'
        'joined = big.<span class="f">join</span>(small, [<span class="s">"key"</span>, <span class="s">"salt"</span>])</div>'
    )
    body = (
        '<div style="margin-top:56px"><div class="kicker">Arreglo 4</div>'
        '<h2>Salting: parte la llave <span class="hl">caliente</span>.</h2></div>'
        + diagram + code +
        '<p class="cap" style="font-size:31px"><b>El costo:</b> la tabla peque&ntilde;a se replica N veces. Elige N seg&uacute;n qu&eacute; tan caliente es la llave.</p>'
    )
    return slide(6, "light", body)


# ---------- 07 · cierre ----------
def s7() -> str:
    body = (
        '<div style="margin-top:64px"><div class="kicker">Tu turno</div>'
        '<h1 style="font-size:96px">&iquest;Cu&aacute;l ha sido tu peor caso de <span class="hl">skew</span>?</h1>'
        '<p class="lead" style="margin-top:34px;color:var(--mut)">Cu&eacute;ntalo en los comentarios.</p></div>'
        '<div style="margin-top:56px;display:flex;flex-direction:column;gap:0">'
        '<div style="display:flex;gap:26px;align-items:center;padding:36px 0;border-top:2px solid var(--rule)">'
        '<span class="tag">Guarda</span><span style="font-size:36px">Para tu pr&oacute;ximo job lento.</span></div>'
        '<div style="display:flex;gap:26px;align-items:center;padding:36px 0;border-top:2px solid var(--rule)">'
        '<span class="tag">D&iacute;a 05</span><span style="font-size:36px">repartition() vs coalesce()</span></div>'
        '<div style="display:flex;gap:26px;align-items:center;padding:36px 0;border-top:2px solid var(--rule);border-bottom:2px solid var(--rule)">'
        '<span class="tag">Repo</span><span style="font-family:Roboto Mono;font-size:28px">github.com/mateosotoa/<br>100-days-of-pythonic-engineering</span></div></div>'
    )
    return slide(7, "dark", body, swipe=False)


def main() -> None:
    theme, out = sys.argv[1], Path(sys.argv[2])
    css = (REPO / "design" / "theme.css").read_text(encoding="utf-8")
    slides = "".join(f() for f in (s1, s2, s3, s4, s5, s6, s7))
    html = (
        f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Dia 04 - Data Skew</title>'
        f"<style>{font_css()}\n{css}</style></head><body data-theme=\"{theme}\">{slides}</body></html>"
    )
    out.write_text(html, encoding="utf-8")
    print("wrote", out, len(html) // 1024, "KB")


if __name__ == "__main__":
    main()
