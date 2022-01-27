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
    a_interpretor = Interpreter(grammar_file)
    a_interpretor.execute_file("./tmp.txt")
    return 0


if __name__ == '__main__':
    sys.exit(main())
