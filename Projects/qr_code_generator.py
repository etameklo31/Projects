# install all the libraries needed 
# create a function that collects a text and converts it to a QR code 
# save the QR code as an image
# run the function

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save("qrimg.png")

url = input("Enter your url: ")
generate_qrcode(url)

# As of right now it is only working with version Python 3.9.9
# Doesn't work from the terminal, you click the qr_code_generator file in the projects folder and type in your url, it will generate a QR code to the website you typed in