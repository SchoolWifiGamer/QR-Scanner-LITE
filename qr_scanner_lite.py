import pyshorteners
import qrcode
import os
from urllib.parse import urlparse

# Install required: pip install pyshorteners qrcode[pil]
# Created by Gao Le


def shorten_url(long_url):
    """Shorten a URL using TinyURL service"""
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        return short_url
    except:
        return "Error: Could not shorten URL"


def generate_qr_code(url, filename="qrcode.png"):
    """Generate QR code for a URL"""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        return f"QR code saved as {filename}"
    except:
        return "Error generating QR code"


def is_valid_url(url):
    """Validate URL format"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


print("=== URL SHORTENER & QR CODE GENERATOR ===")

while True:
    print("\n1. Shorten URL")
    print("2. Generate QR Code")
    print("3. Both")
    print("4. Exit")

    choice = input("\nChoose option (1-4): ")

    if choice == '4':
        break

    url = input("Enter URL: ").strip()

    if not is_valid_url(url):
        print("Invalid URL format! Please include http:// or https://")
        continue

    if choice in ['1', '3']:
        short_url = shorten_url(url)
        print(f"Shortened URL: {short_url}")

    if choice in ['2', '3']:
        filename = input(
            "Enter QR code filename (default: qrcode.png): ").strip()
        if not filename:
            filename = "qrcode.png"
        if not filename.endswith('.png'):
            filename += '.png'

        result = generate_qr_code(url, filename)
        print(result)

        try:
            from PIL import Image
            img = Image.open(filename)
            img.show()
        except:
            pass

print("Thank you for using the URL tools!")
