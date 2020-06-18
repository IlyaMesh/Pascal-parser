from nodes import *
from Line import *

op_cmd = {
    '+': 'ADD',
    '-': 'SUB',
    '*': 'MUL',
    '/': 'DIV',
    '%': 'MOD',
    '>=': 'GE',
    '<=': 'LE',
    '=': 'EQ',
    '>': 'GT',
    '<': 'LT',
    'and': 'AND',
    'or': 'OR'
}
class ByteCodeGen():
    # dispatcher = {
    #     'IdentNode_compile':IdentNode_compile
    # }


    def __init__(self, astTree: ProgramNode):
        self.astTree = astTree
        self.lines : List[Line] = []
        self.generateCode(astTree)
        self.lines.append(Line('HALT'))

    def generateCode(self, astTree: AstNode):
        for child in self.astTree.childs:
            self.__codeGen(child)

    def __codeGen(self, node):
        eval("self." + (str(type(node)).replace("<class 'nodes.", '').replace("'>", '') + '_compile'))(node)

    def IdentNode_compile(self, node: IdentNode):
        self.lines.append(Line('LOAD', node.name))

    def VarsDeclNode_compile(self,node):
        pass

    def BodyNode_compile(self,node:BodyNode):
        for child in node.childs:
            self.__codeGen(child)

    def StmtListNode_compile(self,node):
        for child in node.childs:
            self.__codeGen(child)

    def AssignNode_compile(self,node:AssignNode):
        child = node.val
        self.__codeGen(child)
        self.lines.append(Line('STORE',node.var.name))

    def BinOpNode_compile(self,node:BinOpNode):
        if(node.op == ':='):
            self.__codeGen(node.arg2)
            self.lines.append(Line('STORE' , node.arg1.name))
        else:
            self.__codeGen(node.arg1)
            self.__codeGen(node.arg2)
            self.lines.append(Line(op_cmd[node.op.value]))

    def LiteralNode_compile(self,node):
        self.lines.append(Line('PUSH',node.value))


    def CallNode_compile(self,node:CallNode):
        for param in node.params:
            self.__codeGen(param)
        if(node.func.name == "WriteLn"):
            for par in node.params:
                self.lines.append(Line('CPRT',par.name))
        #TODO add other functions and procedures


