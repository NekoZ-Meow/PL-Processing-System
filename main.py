#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
hiyo言語のインタラクティヴシェル
'''

import os
import sys

from lark.exceptions import VisitError
from hiyo.source_to_tree import SourceToTree
from hiyo.vm.hiyo_vm.executer import Executer

PARSER_FILE = os.sep.join([os.path.dirname(__file__), "hiyo", "parser", "tree"])


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

    a_parser = SourceToTree(PARSER_FILE)
    a_executer = Executer()
    if source_files:
        for file in source_files:
            try:
                a_executer.execute(a_parser.parse_file(file))
            except VisitError as error:
                print(error.__context__)
            except SyntaxError as error:
                print(error)
    else:
        # インタラクティヴモード
        try:
            while True:
                sentence = input(">>> ")
                try:
                    a_executer.execute(a_parser.parse(sentence))
                except VisitError as error:
                    print(error.__context__)
                except SyntaxError as error:
                    print(error)
        except EOFError as error:
            (lambda e: e)(error)

    return 0


if __name__ == '__main__':
    sys.exit(main())
