# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os

from tools.config import AppConfig
from tools.printer import SmartPrinter
import readline

from tools.qr_code_master import QrCodeMaster


def input_with_completion(prompt):
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")

    user_input = input(prompt)

    return user_input


class AppManager:

    def __init__(self):
        self.config = AppConfig()
        self.printer = SmartPrinter()
        self.qr_code_master = QrCodeMaster()

    def show_head(self):
        self.printer.echo(char='*')
        self.printer.echo(text=self.config.app_name)

    def show_footer(self):
        self.printer.echo(text=self.config.copyright_, char='|')
        self.printer.echo(text=self.config.url, char='=')

    @staticmethod
    def get_url():
        while 1:
            url = input(f'Enter text or URL: ')
            if len(url) <= 0:
                print(f'ERROR! Please enter correct text or URL!')
                continue
            return url

    @staticmethod
    def get_name_of_the_final_file():
        while 1:
            name = input(f'Enter the name of the final file: ')
            if len(name) <= 0:
                print(f'ERROR! Please enter correct name!')
                continue
            return name
