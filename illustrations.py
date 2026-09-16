# -*- coding: utf-8 -*-
"""
Custom SVG illustration system for Orbit.
No stock photography is fetched here (no network access to image CDNs from
this build environment, and licensing would be a mess anyway) — instead
this gives the site a consistent, bold, illustrated art-direction that
reads as a deliberate choice rather than a placeholder. Swap any
`photo_panel(...)` call for a real <img> once you have licensed photography
— the CSS class `.photo-panel` already expects either.
"""

BLOB_PATHS = [
    "M60,-56C77,-42,86,-19,84,3C82,25,69,44,49,58C29,72,3,80,-22,74C-47,68,-70,48,-79,22C-88,-4,-83,-35,-64,-53C-45,-71,-13,-76,13,-73C39,-70,43,-70,60,-56Z",
    "M54,-63C68,-51,74,-25,73,-1C72,23,64,45,47,59C30,73,5,79,-19,74C-43,69,-65,53,-75,30C-85,7,-83,-23,-67,-44C-51,-65,-21,-77,4,-76C29,-75,40,-75,54,-63Z",
    "M45,-52C58,-42,66,-21,66,-1C66,19,58,37,44,49C30,61,10,67,-11,65C-32,63,-54,53,-64,36C-74,19,-72,-5,-62,-25C-52,-45,-34,-61,-14,-64C6,-67,32,-62,45,-52Z",
]


def blob(cx, cy, size, color, path_idx=0, opacity=0.55, extra_class=""):
    d = BLOB_PATHS[path_idx % len(BLOB_PATHS)]
    return f"""<svg class="blob {extra_class}" style="left:{cx};top:{cy};width:{size};height:{size};opacity:{opacity};" viewBox="-100 -100 200 200">
      <path d="{d}" fill="{color}" transform="translate(0,0)"/>
    </svg>"""


def blob_field(blobs):
    """blobs: list of dicts with cx, cy, size, color, path_idx, opacity"""
    inner = "".join(blob(**b) for b in blobs)
    return f'<div class="blob-field" aria-hidden="true">{inner}</div>'


# -- gradient "photo" panels -------------------------------------------------
ICONS = {
    "chat": '<path d="M8 30c0-12 10-20 22-20s22 8 22 20-10 20-22 20c-3 0-6-.4-8.6-1.2L10 32l2-8.4" stroke="white" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "chart": '<path d="M8 46V18M22 46V26M36 46V10M50 46V32" stroke="white" stroke-width="4" stroke-linecap="round"/>',
    "cross": '<path d="M27 8v38M8 27h38" stroke="white" stroke-width="6" stroke-linecap="round"/>',
    "anchor": '<circle cx="27" cy="10" r="5" stroke="white" stroke-width="3" fill="none"/><path d="M27 15v33M12 32c0 8 7 15 15 16M42 32c0 8-7 15-15 16M10 24h10M34 24h10" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/>',
    "cup": '<path d="M12 14h26l-3 26a6 6 0 0 1-6 5H21a6 6 0 0 1-6-5L12 14Z" stroke="white" stroke-width="3" fill="none"/><path d="M38 18h5a6 6 0 0 1 0 12h-4M16 6c1 2 3 2 4 0M24 6c1 2 3 2 4 0" stroke="white" stroke-width="3" fill="none" stroke-linecap="round"/>',
    "bolt": '<path d="M30 6 12 32h14l-4 22 22-30H30l4-18Z" stroke="white" stroke-width="3" fill="none" stroke-linejoin="round"/>',
    "orbit": '<circle cx="27" cy="27" r="6" fill="white"/><ellipse cx="27" cy="27" rx="20" ry="9" stroke="white" stroke-width="3" fill="none" transform="rotate(-24 27 27)"/>',
    "route": '<circle cx="10" cy="44" r="4" fill="white"/><circle cx="44" cy="10" r="4" fill="white"/><path d="M10 44C10 24 24 24 24 24S44 24 44 10" stroke="white" stroke-width="3" fill="none" stroke-dasharray="2 5" stroke-linecap="round"/>',
}

GRADIENTS = {
    "sunset":  ("#FF4FA3", "#8B5CF6"),
    "sky":     ("#4C7DFF", "#17C98D"),
    "citrus":  ("#FFC93C", "#FF4FA3"),
    "meadow":  ("#17C98D", "#4C7DFF"),
    "grape":   ("#8B5CF6", "#4C7DFF"),
    "peach":   ("#FF8FAB", "#FFC93C"),
}


def photo_panel(gradient="sunset", icon="orbit", circle=False, caption=None, extra_style=""):
    c1, c2 = GRADIENTS.get(gradient, GRADIENTS["sunset"])
    gid = f"g-{gradient}-{icon}"
    icon_svg = ICONS.get(icon, ICONS["orbit"])
    cls = "photo-panel circle" if circle else "photo-panel"
    cap_html = f'<span class="cap">{caption}</span>' if caption else ""
    return f"""<div class="{cls}" style="{extra_style}">
  <svg viewBox="0 0 200 150" preserveAspectRatio="xMidYMid slice" style="width:100%;height:100%;">
    <defs>
      <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="{c1}"/>
        <stop offset="1" stop-color="{c2}"/>
      </linearGradient>
    </defs>
    <rect width="200" height="150" fill="url(#{gid})"/>
    <circle cx="170" cy="20" r="46" fill="white" opacity="0.08"/>
    <circle cx="20" cy="135" r="60" fill="black" opacity="0.06"/>
    <g transform="translate(73,48) scale(0.9)" opacity="0.9">{icon_svg}</g>
  </svg>
  {cap_html}
</div>"""


# -- friendly rounded avatar illustrations (no stock photography) -----------
AVATARS = {
    "a": dict(skin="#F2B387", hair="#2B1A10", top="#FF4FA3"),
    "b": dict(skin="#8B5A2B", hair="#1A1310", top="#4C7DFF"),
    "c": dict(skin="#FFE0BD", hair="#B5651D", top="#17C98D"),
    "d": dict(skin="#C68642", hair="#0E0E0E", top="#FFC93C"),
    "e": dict(skin="#F6D2B2", hair="#5B3A29", top="#8B5CF6"),
}


def avatar(key="a", size="100%"):
    a = AVATARS.get(key, AVATARS["a"])
    return f"""<div class="photo-panel circle" style="width:{size};background:#fff;">
  <svg viewBox="0 0 100 100" style="width:100%;height:100%;">
    <circle cx="50" cy="50" r="50" fill="{a['top']}"/>
    <circle cx="50" cy="46" r="20" fill="{a['skin']}"/>
    <path d="M30 40 Q30 18 50 18 Q70 18 70 40 L70 34 Q50 22 30 34 Z" fill="{a['hair']}"/>
    <path d="M22 92 Q22 66 50 66 Q78 66 78 92 Z" fill="{a['top']}"/>
    <circle cx="42" cy="48" r="2.6" fill="#17121F"/>
    <circle cx="58" cy="48" r="2.6" fill="#17121F"/>
    <path d="M42 58 Q50 64 58 58" stroke="#17121F" stroke-width="2.4" fill="none" stroke-linecap="round"/>
  </svg>
</div>"""
