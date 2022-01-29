#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
木構造を表示する
'''

import sys

from hiyo_vm.executer import Executer


def main() -> int:
    """
    メイン関数

    Returns
    -------
    int
        終了コード
    """

    source_files = []
    if len(sys.argv) > 1:
        source_files = sys.argv[1:]
    a_interpretor = Executer()
    for file in source_files:
        a_interpretor.execute_file(file)
    return 0


if __name__ == '__main__':
    sys.exit(main())
