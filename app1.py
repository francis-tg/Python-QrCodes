import qrcode
import qrcode.image.svg


class MakeQr:
    def __init__(self, data, version=2, box_size=20, border=3, extension='PNG', filename='defaut'):
        self.data = data
        qr = qrcode.QRCode(
            version=version,
            box_size=box_size,
            border=border,
            error_correction=qrcode.constants.ERROR_CORRECT_L
        )
        if extension == 'PNG':
            qr.add_data(self.data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='red', back_color='black')
            img.save(f'{filename}.png')
        elif extension == 'SVG':
            factory = qrcode.image.svg.SvgPathImage
            svg_img = qrcode.make(self.data, image_factory=factory)
            svg_img.save(f'{filename}.svg')


MakeQr(data="Bonjour c'est mon premier qrcode", filename='tuto', extension='SVG')
