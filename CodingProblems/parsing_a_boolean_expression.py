class Solution:
    def __init__(self):
        self.expression: str = ""
        self.idx: int = 0

    def _parse_bool_expr_handler(self) -> bool:
        operation = self.expression[self.idx]

        self.idx += 2

        ch = self.expression[self.idx]

        if ch == 't':
            result = True
            self.idx += 1
        elif ch == 'f':
            result = False
            self.idx += 1
        else:
            result = self._parse_bool_expr_handler()

        ch = self.expression[self.idx]

        while ch != ')':
            if ch == ',':
                self.idx += 1
            else:
                if ch == 't':
                    current = True
                    self.idx += 1
                elif ch == 'f':
                    current = False
                    self.idx += 1
                else:
                    current = self._parse_bool_expr_handler()
                if operation == '&':
                    result = result and current
                elif operation == '|':
                    result = result or current
            ch = self.expression[self.idx]

        self.idx += 1

        if operation == '!':
            result = not result

        return result

    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return expression[0] == 't'

        self.idx = 0
        self.expression = expression

        return self._parse_bool_expr_handler()
