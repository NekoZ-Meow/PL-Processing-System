#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
変数名を保持するクラス

'''


class ID:
    '''
    変数名を保持するクラス
    '''

    def __init__(self, name: str) -> None:
        """
        初期化処理

        Parameters
        ----------
        name : str
            変数名
        """
        self.__name = name

    def __eq__(self, __o: object) -> bool:
        """
        オブジェクトが同値か

        Parameters
        ----------
        __o : object
            比較するオブジェクト

        Returns
        -------
        bool
            同値ならTrueそれ以外はFalse
        """
        if not isinstance(__o, ID):
            return False

        return self.get_name() == __o.get_name()

    def __repr__(self) -> str:
        """
        このオブジェクトを文字列にして返す

        Returns
        -------
        str
            このオブジェクトを表す文字列
        """

        return self.get_name()

    def __hash__(self) -> int:
        """
        このオブジェクトのハッシュ値を返す

        Returns
        -------
        int
            ハッシュ値
        """

        return self.get_name().__hash__()

    def get_name(self) -> str:
        """
        変数名を取得する

        Returns
        -------
        str
            変数名
        """

        return self.__name
