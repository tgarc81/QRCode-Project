import qrcode

website_link = "https://www.youtube.com/watch?v=PLOPygVcaVE"

qr_version = input("Enter a version parameter, an integer from 1 to 40 that controls the size of the QR code: ")
qr_box = input("Enter a box size parameter, which controls how many pixels each “box” of the QR code is: ")
qr_border = input("Enter a border parameter, which controls how many boxes thick the border should be: ")
qr = qrcode.QRCode(version=qr_version, box_size=qr_box, border=qr_border)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save("youtube_qr.png")
