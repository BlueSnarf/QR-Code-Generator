import qrcode

# Prompt user for URL input
url = input("Paste URL here: ")

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Generate and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("foolproofme.png")

print("QR code generated and saved as 'foolproofme.png'")
