# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os
import qrcode


class QrCodeMaster:

    def __init__(self):
        self._qr = qrcode

    def create_qr_code_file(self, data, file_name):
        if not os.path.exists('qr_codes'):
            os.makedirs('qr_codes')

        file_path = os.path.join('qr_codes', file_name)

        if os.path.exists(file_path):
            print(f"The file {file_name} already exists. Skipping creation.")
            return

        img = self._qr.make(data)

        if not file_path.endswith('.png'):
            file_path = f'{file_path}.png'

        img.save(file_path)
        print(f"QR code saved as {file_path}")
