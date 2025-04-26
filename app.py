# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from tools.manager import AppManager


def main():
    app_manager = AppManager()

    app_manager.show_head()

    url = app_manager.get_url()
    file_name = app_manager.get_name_of_the_final_file()
    app_manager.printer.echo()
    print(f'Text or URL: {url}')
    app_manager.printer.echo()
    print(f'File name: {file_name}')
    app_manager.printer.echo()
    app_manager.qr_code_master.create_qr_code_file(data=url, file_name=file_name)
    app_manager.printer.echo()
    app_manager.show_footer()


if __name__ == '__main__':
    main()
