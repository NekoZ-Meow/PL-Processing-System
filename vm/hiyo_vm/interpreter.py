#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
木構造を構文解析する
'''

import os

from lark import Lark

from hiyo_vm.tree_transformer import TreeTransformer


class Interpreter:
    """
    構文解析を行い、Cellの木構造を構築する
    """

    def __init__(self, grammar_file: str) -> None:
        """
        初期設定

        Parameters
        ----------
        grammar_file : str
            構文解析のための構文を記述したファイル
        """
        self.grammar = ""
        if not os.path.isfile(grammar_file):
            raise ValueError(f"'{grammar_file}'は存在しません")

        with open(grammar_file, "r", encoding="utf-8") as a_file:
            self.grammar = "".join(a_file.readlines())

        self.transformer = TreeTransformer()
        self.parser = Lark(self.grammar, keep_all_tokens=True)

    def execute(self, sentence: str) -> str:
        """
        与えられた木構造の表現を読み取り、実行結果を返す

        Parameters
        ----------
        sentence : str
            木構造の表現

        Returns
        -------
        str
            実行結果
        """

        return self.transformer.transform(self.parser.parse(sentence))

    def execute_file(self, source_file: str) -> str:
        """
        ソースファイルを受け取り、実行する

        Parameters
        ----------
        source_file : str
            ソースファイルのパス

        Returns
        -------
        list
            木構造の根のリスト
        """
        if not os.path.isfile(source_file):
            raise ValueError(f"'{source_file}'は存在しません")
        target = ""
        with open(source_file, "r", encoding="utf-8") as a_file:
            target = os.linesep.join(a_file.readlines())
        return self.execute(target)
