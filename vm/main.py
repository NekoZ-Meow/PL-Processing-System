#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
木構造を表示する
'''

import sys

from hiyo_vm.interpreter import Interpreter


def main() -> int:
    """
    メイン関数

    Returns
    -------
    int
        終了コード
    """

    grammar_file = "./grammar.lark"
    source_files = []
    if len(sys.argv) > 1:
        source_files = sys.argv[1:]
    a_interpretor = Interpreter(grammar_file)
    if source_files:
        for file in source_files:
            a_interpretor.execute_file(file)
    else:
        # インタラクティヴモード
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
