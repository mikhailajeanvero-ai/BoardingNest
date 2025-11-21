class SimpleMiniInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.call_stack = []

    def eval_expr(self, expr, local_vars=None):
        env = {}
        env.update(self.variables)
        if local_vars:
            env.update(local_vars)
        for v in env:
            expr = expr.replace(v, str(env[v]))
        return eval(expr)

    def execute(self, code):
        lines = [line.strip() for line in code.strip().split("\n") if line.strip() and not line.strip().startswith("#")]
        i = 0
        
        while i < len(lines):
            line = lines[i]

            # function definition
            if line.startswith("fn "):
                header = line.split(" ", 1)[1]
                name, args = header.split("(")
                args = args[:-1]  # remove ")"
                arg_list = [a.strip() for a in args.split(",")] if args else []
                body = []

                i += 1
                while i < len(lines) and lines[i] != "end":
                    body.append(lines[i])
                    i += 1
                
                self.functions[name.strip()] = (arg_list, body)
            
            # variable assignment
            elif line.startswith("let "):
                _, var, _, expr = line.split(" ", 3)
                self.variables[var] = self.eval_expr(expr)

            # print statement
            elif line.startswith("print "):
                _, expr = line.split(" ", 1)
                print(self.eval_expr(expr))

            # function call
            elif line.startswith("call "):
                _, rest = line.split(" ", 1)
                fname, args_raw = rest.split("(")
                fname = fname.strip()
                args_raw = args_raw[:-1]  
                args = [self.eval_expr(a.strip()) for a in args_raw.split(",")] if args_raw else []

                arg_names, body = self.functions[fname]
                local_vars = dict(zip(arg_names, args))

                ret = self.run_function(body, local_vars)
                if ret is not None:
                    self.call_stack.append(ret)

            i += 1

    def run_function(self, body, local_vars):
        for line in body:
            if line.startswith("return "):
                return self.eval_expr(line.split(" ", 1)[1], local_vars)

            if line.startswith("let "):
                _, var, _, expr = line.split(" ", 3)
                local_vars[var] = self.eval_expr(expr, local_vars)

            elif line.startswith("print "):
                _, expr = line.split(" ", 1)
                print(self.eval_expr(expr, local_vars))
                

program = """
# global vars
let x = 5
let y = 10

# function add(a, b)
fn add(a, b)
    let result = a + b
    return result
end

# call function
call add(x, y)

# print function return (should be 15)
print 10 + 5
"""

SimpleMiniInterpreter().execute(program)
