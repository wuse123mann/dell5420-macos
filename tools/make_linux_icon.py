#!/usr/bin/env python3
"""Original 'Linux' boot icon for OpenCanopy GoldenGate: graphite tile with a terminal prompt,
plus the theme's own hard-drive icon as a small badge (same layout as the theme's Windows icon)."""
import sys, struct, io
from PIL import Image, ImageDraw, ImageFilter, ImageFont

hd_png, out_icns, preview = sys.argv[1], sys.argv[2], sys.argv[3]
S = 1024  # supersampled canvas


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def tile():
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    m = int(S * 0.055)            # outer margin, like the Windows tile
    r = int(S * 0.20)             # corner radius
    box = (m, m + int(S * 0.01), S - m, S - m + int(S * 0.01))

    # soft drop shadow
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + 18, box[2], box[3] + 18), r, fill=(0, 0, 0, 150))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))

    # silver rim
    rim = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(rim).rounded_rectangle(box, r, fill=(200, 204, 210, 255))
    im.alpha_composite(rim)

    # graphite face with vertical gradient
    inset = int(S * 0.022)
    face_box = (box[0] + inset, box[1] + inset, box[2] - inset, box[3] - inset)
    grad = Image.new("RGBA", (S, S))
    top, bot = (58, 64, 74, 255), (16, 18, 22, 255)
    gd = ImageDraw.Draw(grad)
    for y in range(S):
        gd.line([(0, y), (S, y)], fill=lerp(top, bot, y / S))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle(face_box, r - inset, fill=255)
    im.paste(grad, (0, 0), mask)

    # subtle top gloss
    gloss = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gl = ImageDraw.Draw(gloss)
    for i in range(int(S * 0.30)):
        a = int(38 * (1 - i / (S * 0.30)))
        gl.line([(face_box[0], face_box[1] + i), (face_box[2], face_box[1] + i)], fill=(255, 255, 255, a))
    gm = Image.new("L", (S, S), 0)
    ImageDraw.Draw(gm).rounded_rectangle(face_box, r - inset, fill=255)
    im.paste(gloss, (0, 0), Image.composite(gloss.split()[3], Image.new("L", (S, S), 0), gm))

    # terminal window dots
    dy = face_box[1] + int(S * 0.075)
    for i, col in enumerate([(255, 95, 87), (254, 188, 46), (40, 200, 64)]):
        cx = face_box[0] + int(S * 0.085) + i * int(S * 0.07)
        ImageDraw.Draw(im).ellipse((cx - 20, dy - 20, cx + 20, dy + 20), fill=col + (255,))

    # prompt ">_" with glow
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", int(S * 0.30))
    txt = ">_"
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    tx, ty = face_box[0] + int(S * 0.075), face_box[1] + int(S * 0.13)
    ImageDraw.Draw(glow).text((tx, ty), txt, font=font, fill=(90, 255, 150, 255))
    im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(26)))
    ImageDraw.Draw(im).text((tx, ty), txt, font=font, fill=(150, 255, 190, 255))
    return im


def build():
    im = tile()
    # badge: theme hard drive, bottom right (as in the theme's Windows icon)
    hd = Image.open(hd_png).convert("RGBA")
    bw = int(S * 0.46)
    hd = hd.resize((bw, bw), Image.LANCZOS)
    im.alpha_composite(hd, (S - bw - int(S * 0.02), S - bw - int(S * 0.0)))
    return im


def png(img, size):
    b = io.BytesIO()
    img.resize((size, size), Image.LANCZOS).save(b, "PNG", optimize=True)
    return b.getvalue()


big = build()
chunks = [(b"ic07", png(big, 128)), (b"ic13", png(big, 256))]
body = b"".join(t + struct.pack(">I", len(d) + 8) + d for t, d in chunks)
open(out_icns, "wb").write(b"icns" + struct.pack(">I", len(body) + 8) + body)
big.resize((256, 256), Image.LANCZOS).save(preview)
print("written", out_icns)
