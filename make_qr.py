"""Generate Ahmed's creative networking QR code -> the scan-card hub page."""
import segno

URL = "https://ahmedabdirahman1-max.github.io/northstar-site/card.html"

# High error-correction (H) = stays scannable even when printed small or styled.
qr = segno.make(URL, error="h")

# 1) Plain high-contrast PNG  (most reliable fallback for any scanner / printer)
qr.save(
    "qr-plain.png",
    scale=14, border=4,
    dark="#0b1120", light="#ffffff",
)

# 2) Creative SVG: deep-navy data modules + cyan finder eyes on white.
#    Brand-matched but keeps strong contrast so phones scan it instantly.
qr.save(
    "qr-creative.svg",
    scale=16, border=4,
    dark="#0b1120",          # data + alignment = brand navy
    data_dark="#0b1120",
    finder_dark="#0c7ea8",   # the 3 corner "eyes" in brand cyan
    light="#ffffff",
)

print("Saved qr-plain.png and qr-creative.svg ->", URL)
print("Matrix size:", qr.symbol_size())
