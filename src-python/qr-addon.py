import qrcode

# https://pypi.python.org/pypi/qrcode
# TODO
# - use short URL, smaller image
# - read Chinese char, use Unicode to generate the zdic URL
# - put all QR code on an A4 paper
# - put Chinese char at the center of the QR code image?

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

qr.add_data('http://www.zdic.net/z/17/js/5929.htm')
qr.make(fit=True)

img = qr.make_image()
# should encode the sequence number and unicode in the image file name
# for the further image processing
img.save("tian_qrcode.png")

