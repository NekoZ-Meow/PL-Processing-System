#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
ソースコードから木構造表現に変換するプログラムの
pythonと実行ファイルのインターフェースとなるクラス
'''

import subprocess


class SourceToTree:
    '''
    ソースコードから木構造表現に変換するプログラムの
    pythonと実行ファイルのインターフェースとなるクラス
    '''

    def __init__(self, parser_file: str) -> None:
        """
        初期化処理

        Parameters
        ----------
        parser_file : str
            ソースコードから木構造表現に変換するプログラムのパス
        """
        self.parser = parser_file

    def parse(self, source_code: str) -> str:
        """
        ソースコードから木構造表現に変換する

        Parameters
        ----------
        source_code : str
            ソースコード

        Returns
        -------
        str
            木構造表現
        """

        result = subprocess.run([self.parser], input=source_code,
                                encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if result.returncode != 0:
            raise SyntaxError(result.stderr)

        return result.stdout

    def parse_file(self, source_file: str) -> str:
        """
        ソースファイルから木構造表現に変換する

        Parameters
        ----------
        source_file : str
            ソースファイル

        Returns
        -------
        str
            木構造表現
        """
        result = None
        with open(source_file, "r", encoding="utf-8") as file:
            result = subprocess.run([self.parser], stdin=file,
                                    encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if result is None:
            raise ValueError(f"'{source_file}' cant open file.")
        if result.returncode != 0:
            raise SyntaxError(result.stderr)
        return result.stdout
