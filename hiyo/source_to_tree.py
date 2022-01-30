#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
ソースコードから木構造表現に変換するプログラムの
pythonと実行ファイルのインターフェースとなるクラス
'''

__author__ = 'Okayama Kodai'
__version__ = '1.0.0'

import subprocess
from subprocess import CalledProcessError


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

        try:
            result = subprocess.run([self.parser], input=source_code,
                                    encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        except CalledProcessError as error:
            raise SyntaxError(error.stderr) from error

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
        try:
            with open(source_file, "r", encoding="utf-8") as file:
                result = subprocess.run([self.parser], stdin=file, encoding="utf-8",
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        except CalledProcessError as error:
            raise SyntaxError(error.stderr) from error

        return result.stdout
