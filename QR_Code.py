import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data_to_encode = "Name = DAKAMARI VASU,\nRoll_No = 20951A6655,\nBranch = CSE (Artificial Intelligence and Machine Learning ),\nCollege Name = Institute of Aeronautical Engineering (IARE),\ngithub link = Vasu-Dakamari,\nlinkedin link = dakamari-vasu, \nProgramming = Python*, C, Java, \nDeveloper Tools = HTML, CSS, JavaScript, MS SQL Server,\nFrameworks = Numpy, Pandas, OpenCV"
    output_filename = "My Personal information QrCode.png"     

    generate_qr_code(data_to_encode, output_filename)
    print(f"QR code generated and saved as {output_filename}")
