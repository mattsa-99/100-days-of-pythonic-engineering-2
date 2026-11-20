"""Build the Day 04 LinkedIn carousel (8 slides, 1080x1350) as one HTML file.

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
TOTAL = 8

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
        '<span>Cada barra es una tarea en paralelo. El resto: ~2 min</span><span style="font-style:italic">Ilustrativo</span></div>'
    )
    return slide(
        1, "dark",
        '<div style="margin-top:52px"><div class="kicker">Spark &middot; Rendimiento</div>'
        '<h1>Tu job espera una hora por <span class="hl">UNA</span> sola tarea.</h1></div>' + chart,
    )


# ---------- 02 · qué es ----------
def defs(pairs: list[tuple[str, str]]) -> str:
    """Inline glossary rows: plain-language definition of each technical term."""
    rows = "".join(f'<div class="def"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in pairs)
    return f'<dl class="defs">{rows}</dl>'


def s2() -> str:
    cols = [("key B", 12, "120 mil"), ("key C", 9, "90 mil"), ("key D", 14, "140 mil"), ("key A", 100, "9.8 M")]
    bars = []
    for name, h, rows in cols:
        hot = h == 100
        bg = "var(--a1d)" if hot else "color-mix(in srgb, var(--a1) 45%, var(--icebg))"
        bars.append(
            f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:10px">'
            f'<span style="font-family:Roboto Mono;font-size:24px;font-weight:500;color:{"var(--a1d)" if hot else "var(--mut)"}">{rows}</span>'
            f'<div style="width:100%;height:{h*2.5}px;background:{bg}"></div></div>'
        )
    labels = "".join(
        f'<span style="flex:1;text-align:center;font-family:Montserrat;font-weight:800;font-size:24px">{name}</span>'
        for name, _, _ in cols
    )
    body = (
        '<div style="margin-top:48px"><div class="kicker">El problema</div>'
        '<h2>Se llama <span class="hl">data skew</span>.</h2>'
        '<p class="lead" style="margin-top:24px;font-size:34px">En un join, Spark junta las filas con la misma <b>key</b> (la columna del join, ej. customer_id). '
        'Si una key tiene casi todas las filas, una sola partición recibe casi todo.</p></div>'
        '<div style="display:flex;gap:30px;align-items:flex-end;margin-top:30px;height:300px;border-bottom:3px solid #071A22;padding:0 8px">'
        + "".join(bars) + "</div>"
        f'<div style="display:flex;gap:30px;padding:12px 8px 0">{labels}</div>'
        + defs([
            ("Partición", "Un pedazo de tus datos. Cada una la procesa una tarea, en paralelo."),
            ("Shuffle", "Mover filas por la red para juntar las de la misma key."),
        ])
    )
    return slide(2, "light", body)


# ---------- 03 · señales ----------
def s3() -> str:
    items = [
        ("01", "Una tarea dura <b>10x</b> más que la mediana.", "La mediana es lo que dura una tarea típica."),
        ("02", "Su <b>Shuffle Read</b> es enorme.", "Shuffle Read: datos que le llegaron por la red en el shuffle."),
        ("03", "<b>Spill a disco</b> en pocas tareas.", "Spill: no le cabe en memoria y usa el disco (lento)."),
    ]
    lines = "".join(
        f'<div style="display:flex;gap:30px;align-items:baseline;padding:16px 0;border-top:2px solid var(--rule)">'
        f'<span style="font-family:Montserrat;font-weight:900;font-size:68px;color:var(--a1l);line-height:1;width:120px;flex:none">{n}</span>'
        f'<div><div style="font-size:35px;line-height:1.25">{t}</div>'
        f'<div style="font-size:28px;line-height:1.35;color:var(--mut);margin-top:8px">{d}</div></div></div>'
        for n, t, d in items
    )
    table = (
        '<div style="margin-top:18px;background:#05141A;border-radius:6px;padding:20px 30px;font-family:Roboto Mono;font-size:25px">'
        '<div style="color:var(--mut);margin-bottom:12px">Stage &rarr; Summary Metrics &rarr; Duration</div>'
        '<div style="display:flex;justify-content:space-between"><span style="color:var(--mut)">Min</span><span style="color:var(--mut)">Median</span><span style="color:var(--mut)">75th</span><span style="color:var(--hl)">Max</span></div>'
        '<div style="display:flex;justify-content:space-between;margin-top:8px;font-size:30px"><span>1 s</span><span>3 s</span><span>3 s</span><span style="color:var(--hl);font-weight:500">58 min</span></div></div>'
    )
    body = (
        '<div style="margin-top:48px"><div class="kicker">Cómo detectarlo</div>'
        '<h2>3 señales en la <span class="hl">Spark UI</span>.</h2>'
        '<p style="font-size:28px;color:var(--mut);margin-top:14px">La Spark UI es la página que muestra cómo corrió cada tarea de tu job.</p></div>'
        f'<div style="margin-top:16px">{lines}</div>' + table
    )
    return slide(3, "dark", body)


# ---------- 04 · arreglos 1 y 2 ----------
def s4() -> str:
    fix1 = (
        '<div class="step"><span class="n">1</span>Quita las filas con key NULL</div>'
        '<p class="why">Una key NULL nunca encuentra pareja en el join, pero todas esas filas '
        'igual viajan juntas a la misma partición.</p>'
        '<div class="code" style="font-size:27px;padding:28px 32px">'
        'events = events.<span class="f">filter</span>(\n'
        '    F.<span class="f">col</span>(<span class="s">"customer_id"</span>).<span class="f">isNotNull</span>()\n'
        ')</div>'
    )
    fix2 = (
        '<div class="step"><span class="n">2</span>Deja que Spark lo parta solo</div>'
        '<p class="why"><b style="color:#071A22">AQE</b> (Adaptive Query Execution) mide las particiones '
        'mientras el job corre y divide las que quedaron gigantes.</p>'
        '<div class="code" style="font-size:26px;padding:28px 30px">'
        'spark.conf.<span class="f">set</span>(<span class="s">"spark.sql.adaptive.enabled"</span>, <span class="s">"true"</span>)\n'
        'spark.conf.<span class="f">set</span>(\n'
        '    <span class="s">"spark.sql.adaptive.skewJoin.enabled"</span>, <span class="s">"true"</span>)</div>'
    )
    body = (
        '<div style="margin-top:48px"><div class="kicker">Arreglo 1 y 2</div>'
        '<h2>Lo barato, <span class="hl">primero</span>.</h2></div>'
        f'<div style="margin-top:44px">{fix1}</div><div style="margin-top:44px">{fix2}</div>'
    )
    return slide(4, "light", body)


# ---------- 05 · broadcast ----------
def s5() -> str:
    node = (
        '<div style="flex:1;border:3px solid var(--a1l);padding:20px 18px;display:flex;flex-direction:column;gap:14px">'
        '<span style="font-family:Montserrat;font-weight:800;font-size:22px;letter-spacing:.12em;color:var(--mut)">EXECUTOR {i}</span>'
        '<div style="height:52px;background:var(--a1);display:flex;align-items:center;padding-left:14px;'
        'font-family:Roboto Mono;font-size:24px;color:#071A22">big</div>'
        '<div style="display:flex;align-items:center;gap:12px"><div style="width:30px;height:30px;background:var(--hl)"></div>'
        '<span style="font-family:Roboto Mono;font-size:24px;color:var(--mut)">copia de small</span></div></div>'
    )
    diagram = (
        '<div style="display:flex;gap:20px;margin-top:28px">' + "".join(node.format(i=i) for i in (1, 2, 3)) + "</div>"
    )
    code = (
        '<div class="code" style="margin-top:26px;font-size:29px;padding:24px 34px"><span class="k">from</span> pyspark.sql.functions <span class="k">import</span> broadcast\n\n'
        'joined = big.<span class="f">join</span>(<span class="f">broadcast</span>(small), <span class="s">"key"</span>)</div>'
    )
    body = (
        '<div style="margin-top:48px"><div class="kicker">Arreglo 3</div>'
        '<h2>Si la otra tabla es pequeña: <span class="hl">broadcast</span>.</h2>'
        '<p class="lead" style="margin-top:22px;font-size:32px">Spark copia la tabla pequeña completa a cada executor. '
        'La grande no se mueve: sin shuffle, no hay partición gigante.</p></div>'
        + diagram + code +
        defs([("Executor", "El proceso de Spark que ejecuta las tareas. Un clúster tiene varios.")]) +
        '<p class="cap" style="font-size:29px;color:var(--mut);margin-top:18px"><b style="color:#E7F3F1">Ojo:</b> la tabla pequeña debe caber en memoria. Más en el Día 03.</p>'
    )
    return slide(5, "dark", body)


# ---------- 06 · salting: la idea ----------
def mini_table(title: str, header: list[str], rows: list[list[str]], dup: bool = False) -> str:
    """Small data table drawn with divs, used to show real rows in a slide."""
    cell = "flex:1;padding:8px 14px;font-family:Roboto Mono;font-size:25px"
    head = "".join(
        f'<span style="{cell};font-family:Montserrat;font-weight:800;font-size:22px;letter-spacing:.1em;color:var(--mut)">{h.upper()}</span>'
        for h in header
    )
    bg = "color-mix(in srgb, var(--a1) 35%, var(--icebg))" if dup else "transparent"
    body = "".join(
        f'<div style="display:flex;border-top:2px solid var(--rule);background:{bg}">'
        + "".join(
            f'<span style="{cell};{"color:var(--a1d);font-weight:500" if j == 1 else ""}">{v}</span>'
            for j, v in enumerate(r)
        )
        + "</div>"
        for r in rows
    )
    return (
        f'<div style="flex:1"><div style="font-size:27px;line-height:1.3;margin-bottom:12px;min-height:72px">{title}</div>'
        f'<div style="display:flex">{head}</div>{body}</div>'
    )


def s6() -> str:
    big = mini_table(
        "<b>1.</b> Tabla grande: cada fila recibe un <b>salt</b> al azar.",
        ["key", "salt"], [["A", "2"], ["A", "0"], ["A", "3"], ["A", "1"]],
    )
    small = mini_table(
        "<b>2.</b> Tabla pequeña: la fila de A se copia una vez por salt.",
        ["key", "salt", "city"], [["A", "0", "Lima"], ["A", "1", "Lima"], ["A", "2", "Lima"], ["A", "3", "Lima"]],
        dup=True,
    )
    tasks = "".join(
        f'<div style="flex:1;border:2px solid var(--a1d);padding:12px 0;text-align:center;font-family:Roboto Mono;font-size:25px">'
        f'A&middot;{i}<div style="font-family:Roboto;font-size:24px;color:var(--mut)">tarea {i + 1}</div></div>'
        for i in range(4)
    )
    body = (
        '<div style="margin-top:48px"><div class="kicker">Arreglo 4 &middot; Salting</div>'
        '<h2>Parte la key <span class="hl">caliente</span>.</h2>'
        '<p class="lead" style="margin-top:20px;font-size:31px">La key A tiene millones de filas y cae en una sola tarea. '
        'La idea: agregar una columna extra, <b>salt</b>, para dividirla.</p></div>'
        f'<div style="display:flex;gap:40px;margin-top:30px">{big}{small}</div>'
        '<div style="font-size:27px;line-height:1.3;margin-top:30px"><b>3.</b> Join por <b>key + salt</b>: '
        'cada pareja va a su propia tarea, en paralelo.</div>'
        f'<div style="display:flex;gap:12px;margin-top:14px">{tasks}</div>'
        '<p class="cap" style="font-size:29px"><b>Antes:</b> 1 tarea con todas las filas de A. '
        '<b>Ahora:</b> 4 tareas con una cuarta parte cada una.</p>'
    )
    return slide(6, "light", body)


# ---------- 07 · salting: el código ----------
def s7() -> str:
    def step(n: int, title: str, why: str, code: str) -> str:
        why_html = f'<p class="why" style="margin:8px 0 14px">{why}</p>' if why else '<div style="height:14px"></div>'
        return (
            f'<div style="margin-top:30px"><div class="step"><span class="n">{n}</span>{title}</div>{why_html}'
            f'<div class="code" style="font-size:26px;padding:22px 30px">{code}</div></div>'
        )

    body = (
        '<div style="margin-top:48px"><div class="kicker">Arreglo 4 &middot; El código</div>'
        '<h2>Ahora, en <span class="hl">código</span>.</h2></div>'
        + step(
            1, "Salt al azar en la tabla grande",
            "rand() da un número entre 0 y 1. Por N y a entero: 0, 1, 2 o 3.",
            'N = <span class="n">4</span>  <span class="c"># en cuántas partes dividir la key</span>\n'
            'big = big.<span class="f">withColumn</span>(\n'
            '    <span class="s">"salt"</span>, (F.<span class="f">rand</span>() * N).<span class="f">cast</span>(<span class="s">"int"</span>))',
        )
        + step(
            2, "Una copia por salt en la pequeña",
            "explode convierte la lista [0, 1, 2, 3] en 4 filas.",
            'salts = F.<span class="f">array</span>(*[F.<span class="f">lit</span>(i) <span class="k">for</span> i <span class="k">in</span> <span class="f">range</span>(N)])\n'
            'small = small.<span class="f">withColumn</span>(<span class="s">"salt"</span>, F.<span class="f">explode</span>(salts))',
        )
        + step(
            3, "Join por key + salt", "",
            'joined = big.<span class="f">join</span>(small, [<span class="s">"key"</span>, <span class="s">"salt"</span>])',
        )
        + '<p class="cap" style="font-size:29px;color:var(--mut);margin-top:22px"><b style="color:#E7F3F1">El costo:</b> '
        'la tabla pequeña crece N veces.</p>'
    )
    return slide(7, "dark", body)


# ---------- 08 · cierre ----------
def s8() -> str:
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
    return slide(8, "dark", body, swipe=False)


def main() -> None:
    theme, out = sys.argv[1], Path(sys.argv[2])
    css = (REPO / "design" / "theme.css").read_text(encoding="utf-8")
    slides = "".join(f() for f in (s1, s2, s3, s4, s5, s6, s7, s8))
    html = (
        f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Dia 04 - Data Skew</title>'
        f"<style>{font_css()}\n{css}</style></head><body data-theme=\"{theme}\">{slides}</body></html>"
    )
    out.write_text(html, encoding="utf-8")
    print("wrote", out, len(html) // 1024, "KB")


if __name__ == "__main__":
    main()
