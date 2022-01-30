#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
hiyo言語のインタラクティヴシェル
'''

import platform
import os
import sys

from lark.exceptions import VisitError
from hiyo.source_to_tree import SourceToTree
from hiyo.vm.hiyo_vm.executer import Executer

# ソースコードから木構造表現に変換するプログラムのパス
PARSER_FILE = os.sep.join([os.path.dirname(__file__), "hiyo", "parser", "tree"])


def make_do_script(executer: Executer, parse_func: 'function') -> 'function':
    """
    スクリプトを実行する関数を生成する関数
    """

    def do_script(argument: str):
        """
        スクリプトを実行する

        Parameters
        ----------
        value : str
            引数
        """
        try:
            executer.execute(parse_func(argument))
        except VisitError as error:
            print(error.__context__, end="")
        except SyntaxError as error:
            print(error, end="")

    return do_script


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
        do_script = make_do_script(a_executer, a_parser.parse_file)
        for file in source_files:
            do_script(file)
    else:
        # インタラクティヴモード
        do_script = make_do_script(a_executer, a_parser.parse)
        print("Welcome to ('8'*) version 1.0.0 ", end="")
        print("(Python " + ".".join(platform.python_version_tuple()) + ")", end=os.linesep * 2)
        try:
            while True:
                script = input(">>> ")
                do_script(script)
        except EOFError as error:
            (lambda e: e)(error)

    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
