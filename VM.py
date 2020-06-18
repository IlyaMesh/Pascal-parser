from collections import deque
from context import *
from Line import *

HALT = 'HALT'
PUSH = 'PUSH'
POP = 'POP'
DUP = 'DUP'
ADD = 'ADD'
SUB = 'SUB'
MUL = 'MUL'
DIV = 'DIV'
MOD = 'MOD'
AND = 'AND'
OR = 'OR'
EQ = 'EQ'
GT = 'GT'
LT = 'LT'
GE = 'GE'
LE = 'LE'
LOAD = 'LOAD'
STORE = 'STORE'
CPRT = 'CPRT'


class VM:
    def __init__(self, byteCode):
        self._code = byteCode
        self._cur_line_id = 0
        self._stack = deque()
        self._contexts = [Context(0)]
        self._halted = False
        self.run()

    def run(self):
        while self._cur_line_id < len(self._code) and not self._halted:
            listcode = self.get_code()
            self.execute_operation(listcode)

    def execute_operation(self, instruction):
        opcode = {
            HALT: self.halt,
            POP: self.pop,
            DUP: self.dup,
            ADD: self.add,
            SUB: self.sub,
            MUL: self.mul,
            DIV: self.div,
            MOD: self.mod,
            AND: self._and,
            OR: self._or,
            EQ: self.eq,
            GT: self.gt,
            LT: self.lt,
            GE: self.ge,
            LE: self.le,
        }
        opcode_with_val = {
            PUSH: self.push,
            LOAD: self.load,
            STORE: self.store,
            CPRT: self.callPrint
        }

        if instruction.cmd in opcode:
            opcode[instruction.cmd]()
        elif instruction.cmd in opcode_with_val:
            opcode_with_val[instruction.cmd](instruction.value)

    def halt(self):
        self._halted = True

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        self.is_stack_empty()
        return self._stack.pop()

    #duplicate
    def dup(self):
        self.is_stack_empty()
        last = self._stack[len(self._stack) - 1]
        self._stack.append(last)

    def add(self):
        self.check_stack("ADD")
        right = self.pop()
        left = self.pop()
        self._stack.append(left + right)

    def sub(self):
        self.check_stack("SUB")
        right = self.pop()
        left = self.pop()
        self._stack.append(left - right)

    def mul(self):
        self.check_stack("MUL")
        right = self.pop()
        left = self.pop()
        self._stack.append(left * right)

    def div(self):
        self.check_stack("DIV")
        right = self.pop()
        left = self.pop()
        self._stack.append(left / right)

    def mod(self):
        self.check_stack("MOD")
        right = self.pop()
        left = self.pop()
        self._stack.append(right % left)

    def _and(self):
        self.check_stack("AND")
        right = self.pop()
        left = self.pop()
        self._stack.append(left and right)

    def _or(self):
        self.check_stack("OR")
        right = self.pop()
        left = self.pop()
        self._stack.append(left or right)

    def eq(self):
        self.check_stack("EQ")
        right = self.pop()
        left = self.pop()
        self._stack.append(left == right)

    def gt(self):
        self.check_stack("GT")
        right = self.pop()
        left = self.pop()
        self._stack.append(left > right)

    def lt(self):
        self.check_stack("LT")
        right = self.pop()
        left = self.pop()
        self._stack.append(left < right)

    def ge(self):
        self.check_stack("GE")
        right = self.pop()
        left = self.pop()
        self._stack.append(left >= right)

    def le(self):
        self.check_stack("LE")
        right = self.pop()
        left = self.pop()
        self._stack.append(left <= right)

    def load(self, var_name):
        self._stack.append(self.get_current_context().get_variable(var_name))

    def store(self, var_name):
        self.is_stack_empty()
        self.get_current_context().set_variable(var_name, self.pop())

    def callPrint(self, n):
        args = []
        args.append(self._stack.pop())
        print(*args)


    def get_code(self):
        if self._cur_line_id < len(self._code):
            code = self._code[self._cur_line_id]
            self._cur_line_id += 1
            return code

    def check_stack(self, instruction):
        if len(self._stack) < 2:
            raise RuntimeError("Недостаточно элементов в стеке" + instruction)

    def is_stack_empty(self):
        if len(self._stack) == 0:
            raise RuntimeError("Стек пуст")

    def get_current_context(self):
        return self._contexts[len(self._contexts) - 1]

