# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/02_xtend.ipynb.

# %% auto 0
__all__ = ['picocss', 'picolink', 'picocondcss', 'picocondlink', 'set_pico_cls', 'Html', 'A', 'Form', 'AX', 'Checkbox', 'Card',
           'Group', 'Search', 'Grid', 'DialogX', 'Hidden', 'Container', 'Script', 'Style', 'double_braces',
           'undouble_braces', 'loose_format', 'ScriptX', 'replace_css_vars', 'StyleX', 'run_js', 'Titled', 'Socials',
           'Favicon', 'jsd']

# %% ../nbs/api/02_xtend.ipynb
from dataclasses import dataclass, asdict
from typing import Any

from fastcore.utils import *
from fastcore.xtras import partial_format
from fastcore.xml import *
from fastcore.meta import use_kwargs, delegates
from .components import *

try: from IPython import display
except ImportError: display=None

# %% ../nbs/api/02_xtend.ipynb
picocss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"
picolink = (Link(rel="stylesheet", href=picocss),
            Style(":root { --pico-font-size: 100%; }"))
picocondcss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.conditional.min.css"
picocondlink = (Link(rel="stylesheet", href=picocondcss),
                Style(":root { --pico-font-size: 100%; }"))

# %% ../nbs/api/02_xtend.ipynb
def set_pico_cls():
    js = """var sel = '.cell-output, .output_area';
document.querySelectorAll(sel).forEach(e => e.classList.add('pico'));

new MutationObserver(ms => {
  ms.forEach(m => {
    m.addedNodes.forEach(n => {
      if (n.nodeType === 1) {
        var nc = n.classList;
        if (nc && (nc.contains('cell-output') || nc.contains('output_area'))) nc.add('pico');
        n.querySelectorAll(sel).forEach(e => e.classList.add('pico'));
      }
    });
  });
}).observe(document.body, { childList: true, subtree: true });"""
    return display.Javascript(js)

# %% ../nbs/api/02_xtend.ipynb
def Html(*c, doctype=True, **kwargs)->FT:
    "An HTML tag, optionally preceeded by `!DOCTYPE HTML`"
    res = ft('html', *c, **kwargs)
    if not doctype: return res
    return (ft('!DOCTYPE', html=True), res)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def A(*c, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs)->FT:
    "An A tag; `href` defaults to '#' for more concise use with HTMX"
    return ft_hx('a', *c, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Form(*c, enctype="multipart/form-data", **kwargs)->FT:
    "A Form tag; identical to plain `ft_hx` version except default `enctype='multipart/form-data'`"
    return ft_hx('form', *c, enctype=enctype, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def AX(txt, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs)->FT:
    "An A tag with just one text child, allowing hx_get, target_id, and hx_swap to be positional params"
    return ft_hx('a', txt, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Checkbox(checked:bool=False, label=None, value="1", **kwargs)->FT:
    "A Checkbox optionally inside a Label"
    if not checked: checked=None
    res = Input(type="checkbox", checked=checked, value=value, **kwargs)
    if label: res = Label(res, label)
    return res

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Card(*c, header=None, footer=None, **kwargs)->FT:
    "A PicoCSS Card, implemented as an Article with optional Header and Footer"
    if header: c = (Header(header),) + c
    if footer: c += (Footer(footer),)
    return Article(*c, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Group(*c, **kwargs)->FT:
    "A PicoCSS Group, implemented as a Fieldset with role 'group'"
    return Fieldset(*c, role="group", **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Search(*c, **kwargs)->FT:
    "A PicoCSS Search, implemented as a Form with role 'search'"
    return Form(*c, role="search", **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Grid(*c, cls='grid', **kwargs)->FT:
    "A PicoCSS Grid, implemented as child Divs in a Div with class 'grid'"
    c = tuple(o if isinstance(o,list) else Div(o) for o in c)
    return ft_hx('div', *c, cls=cls, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def DialogX(*c, open=None, header=None, footer=None, id=None, **kwargs)->FT:
    "A PicoCSS Dialog, with children inside a Card"
    card = Card(*c, header=header, footer=footer, **kwargs)
    return Dialog(card, open=open, id=id)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Hidden(value:Any="", **kwargs)->FT:
    "An Input of type 'hidden'"
    return Input(type="hidden", value=value, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Container(*args, **kwargs)->FT:
    "A PicoCSS Container, implemented as a Main with class 'container'"
    return Main(*args, cls="container", **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_html, keep=True)
def Script(code:str="", **kwargs)->FT:
    "A Script tag that doesn't escape its code"
    return ft_html('script', NotStr(code), **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_html, keep=True)
def Style(*c, **kwargs)->FT:
    "A Style tag that doesn't escape its code"
    return ft_html('style', map(NotStr,c), **kwargs)

# %% ../nbs/api/02_xtend.ipynb
def double_braces(s):
    "Convert single braces to double braces if next to special chars or newline"
    s = re.sub(r'{(?=[\s:;\'"]|$)', '{{', s)
    return re.sub(r'(^|[\s:;\'"])}', r'\1}}', s)

# %% ../nbs/api/02_xtend.ipynb
def undouble_braces(s):
    "Convert double braces to single braces if next to special chars or newline"
    s = re.sub(r'\{\{(?=[\s:;\'"]|$)', '{', s)
    return re.sub(r'(^|[\s:;\'"])\}\}', r'\1}', s)

# %% ../nbs/api/02_xtend.ipynb
def loose_format(s, **kw):
    "String format `s` using `kw`, without being strict about braces outside of template params"
    if not kw: return s
    return undouble_braces(partial_format(double_braces(s), **kw)[0])

# %% ../nbs/api/02_xtend.ipynb
def ScriptX(fname, type=None, _async=None, defer=None, charset=None, crossorigin=None, integrity=None, **kw):
    "A `script` element with contents read from `fname`"
    attrs = ['src', 'type', 'async', 'defer', 'charset', 'crossorigin', 'integrity', 'nomodule']
    scr_kw = {k:kw.pop(k) for k in attrs if k in kw}
    s = loose_format(Path(fname).read_text(), **kw)
    return Script(s, **scr_kw)

# %% ../nbs/api/02_xtend.ipynb
def replace_css_vars(css, pre='tpl', **kwargs):
    "Replace `var(--)` CSS variables with `kwargs` if name prefix matches `pre`"
    if not kwargs: return css
    def replace_var(m):
        var_name = m.group(1).replace('-', '_')
        return kwargs.get(var_name, m.group(0))
    return re.sub(fr'var\(--{pre}-([\w-]+)\)', replace_var, css)

# %% ../nbs/api/02_xtend.ipynb
def StyleX(fname, **kw):
    "A `style` element with contents read from `fname` and variables replaced from `kw`"
    s = Path(fname).read_text()
    attrs = ['type', 'media', 'scoped', 'title', 'nonce', 'integrity', 'crossorigin']
    sty_kw = {k:kw.pop(k) for k in attrs if k in kw}
    return Style(replace_css_vars(s, **kw), **sty_kw)

# %% ../nbs/api/02_xtend.ipynb
def run_js(js, id=None, **kw):
    "Run `js` script, auto-generating `id` based on name of caller if needed, and js-escaping any `kw` params"
    if not id: id = sys._getframe(1).f_code.co_name
    kw = {k:dumps(v) for k,v in kw.items()}
    return Script(js.format(**kw), id=id, hx_swap_oob='true')

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Titled(title:str="FastHTML app", *args, **kwargs)->FT:
    "An HTML partial containing a `Title`, and `H1`, and any provided children"
    return Title(title), Main(H1(title), *args, cls="container", **kwargs)

# %% ../nbs/api/02_xtend.ipynb
def Socials(title, site_name, description, image, url=None, w=1200, h=630, twitter_site=None, creator=None, card='summary'):
    "OG and Twitter social card headers"
    if not url: url=site_name
    if not url.startswith('http'): url = f'https://{url}'
    if not image.startswith('http'): image = f'{url}{image}'
    res = [Meta(property='og:image', content=image),
        Meta(property='og:site_name', content=site_name),
        Meta(property='og:image:type', content='image/png'),
        Meta(property='og:image:width', content=w),
        Meta(property='og:image:height', content=h),
        Meta(property='og:type', content='website'),
        Meta(property='og:url', content=url),
        Meta(property='og:title', content=title),
        Meta(property='og:description', content=description),
        Meta(name='twitter:image', content=image),
        Meta(name='twitter:card', content=card),
        Meta(name='twitter:title', content=title),
        Meta(name='twitter:description', content=description)]
    if twitter_site is not None: res.append(Meta(name='twitter:site',    content=twitter_site))
    if creator      is not None: res.append(Meta(name='twitter:creator', content=creator))
    return tuple(res)

# %% ../nbs/api/02_xtend.ipynb
def Favicon(light_icon, dark_icon):
    "Light and dark favicon headers"
    return (Link(rel='icon', type='image/x-ico', href=light_icon, media='(prefers-color-scheme: light)'),
            Link(rel='icon', type='image/x-ico', href=dark_icon, media='(prefers-color-scheme: dark)'))

# %% ../nbs/api/02_xtend.ipynb
def jsd(org, repo, root, path, prov='gh', typ='script', ver=None, esm=False, **kwargs)->FT:
    "jsdelivr `Script` or CSS `Link` tag, or URL"
    ver = '@'+ver if ver else ''
    s = f'https://cdn.jsdelivr.net/{prov}/{org}/{repo}{ver}/{root}/{path}'
    if esm: s += '/+esm'
    return Script(src=s, **kwargs) if typ=='script' else Link(rel='stylesheet', href=s, **kwargs) if typ=='css' else s
