#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
意味解析で行う処理群を記述したクラス
'''

from lark import Transformer, v_args

from hiyo.vm.hiyo_vm.id import ID


@v_args(inline=True)
class TreeTransformer(Transformer):
    """
    Larkで意味解析を行うためのクラス
    """

    def __init__(self, visit_tokens: bool = True) -> None:
        """
        初期化処理
        """
        super().__init__(visit_tokens)
        self.variable_dict = {}

    def __get_from_variable_dict(self, an_id: ID):
        """
        変数名を受け取り、変数辞書から値を取り出す

        Parameters
        ----------
        an_id : ID
            変数名

        Returns
        -------
        Any
            取得した値

        Raises
        ------
        SyntaxError
            変数名が存在しない時
        """
        if an_id not in self.variable_dict:
            raise SyntaxError(f"id '{an_id}' is not defined.")

        return self.variable_dict[an_id]

    def trees(self, *tokens):
        """
        trees : tree+
        """
        (lambda x: x)(self)  # NOP
        # print(self.variable_dict)
        return tokens

    def tree(self, *tokens):
        '''
        tree : node
        | cons
        | leaf
        '''
        (lambda x: x)(self)  # NOP
        return tokens[0]

    def operation(self, *tokens):
        '''
        node : "node" "(" operator cons ")" -> operation
        '''

        operator = tokens[2]

        left_value, right_value = map(
            lambda v: self.__get_from_variable_dict(v) if isinstance(v, ID) else v, tokens[3])

        if operator == "+":
            return left_value + right_value

        if operator == "-":
            return left_value - right_value

        raise SyntaxError(f"undefined operator '{operator}'")

    def assignment(self, *tokens):
        '''
        node : "node" "(" assign cons ")" -> assignment
        '''
        key, value = tokens[3]
        if isinstance(value, ID):
            value = self.__get_from_variable_dict(value)
        self.variable_dict[key] = value

        return None

    def assign(self, *tokens):
        '''
        assign = "="
        '''
        (lambda x: x)(self)  # NOP
        return str(tokens[0])

    def print(self, *tokens):
        '''
        node : "node" "(" "Print" (node|leaf) ")" -> print
        '''

        (lambda x: x)(self)  # NOP
        value = tokens[3]
        value = self.__get_from_variable_dict(value) if isinstance(value, ID) else value
        print(value)

    def cons(self, *tokens):
        '''
        cons : "cons" "(" (node|leaf) (node|leaf) ")"
        '''
        (lambda x: x)(self)  # NOP
        return (tokens[2], tokens[3])

    def create_id(self, *tokens):
        '''
        leaf : "leaf" "(" variable identifier ")" -> create_id
        '''
        (lambda x: x)(self)  # NOP
        return ID(tokens[3])

    def create_constant(self, *tokens):
        '''
        leaf : "leaf" "(" constant (integer|float) ")" -> create_constant
        '''
        (lambda x: x)(self)  # NOP
        return tokens[3]

    def identifier(self, *tokens):
        '''
        identifier : /[a-zA-Z_][a-zA-Z0-9_]*/
        '''
        (lambda x: x)(self)  # NOP
        return str(tokens[0])

    def integer(self, *tokens):
        '''
        integer : /[0-9]+[0-9]*/
        '''
        (lambda x: x)(self)  # NOP
        return int(tokens[0])

    def float(self, *tokens):
        '''
        float : /[0-9]*.[0-9]+/
        '''
        (lambda x: x)(self)  # NOP
        return float(tokens[0])

    def string(self, *tokens):
        '''
        string: /'.*'/
        '''
        (lambda x: x)(self)  # NOP
        return str(tokens[0][1:-1]).replace("\\'", "'")

    def variable(self, *tokens):
        '''
        variable : "ID"
        '''
        (lambda x: x)(self)  # NOP
        return str(tokens[0])

    def constant(self, *tokens):
        '''
        constant : "INTEGER"|"REAL"|"STRINGS"
        '''
        (lambda x: x)(self)  # NOP
        return str(tokens[0])

    def operator(self, *tokens):
        '''
        operator : "+"|"-"|"*"|"/"
        '''
        (lambda x: x)(self)  # NOP
        return str(tokens[0])
