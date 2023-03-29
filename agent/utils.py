import ast
import glob
import os


def parse_file_content(string: str):
    first_break = string.find("---")
    last_break = string.rfind("---")
    if first_break == -1 and last_break == -1 or first_break == last_break:
        return None, None
    nl_after = string.find("\n", last_break)
    description = string[nl_after:]
    return string[first_break + 4 : last_break], description.strip("\n")


def parse_action(string: str):
    assert string.startswith("action:")
    idx = string.find("action_input=")
    if idx == -1:
        return string[8:], None
    return string[8 : idx - 1], string[idx + 13 :].strip("'").strip('"')


def extract_imports(file_contents):
    module_ast = ast.parse(file_contents)
    imports = []
    functions = [n for n in module_ast.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in module_ast.body if isinstance(n, ast.ClassDef)]
    for node in ast.walk(module_ast):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module_name = node.module
            for alias in node.names:
                name = alias.name
                if module_name:
                    imports.append(f"{module_name}.{name}")
                else:
                    imports.append(name)
    return imports, functions, classes


def read_python_module_structure(path):
    file_types = ["*.py"]
    code = []
    for file_type in file_types:
        code += glob.glob(os.path.join(path, "**", file_type), recursive=True)

    structure_prompt = "Files:\n"
    structure_prompt += "(listing all files and their functions and classes)\n\n"

    def get_file_name(i):
        return "./{}.py".format(i.replace(".", "/"))

    content = {}
    internal_imports_map = {}
    for fn in code:
        if os.path.basename(fn) == "gpt.py":
            continue
        with open(fn, "r") as f:
            content[fn] = f.read()
            imports, functions, classes = extract_imports(content[fn])
            internal_imports = list(
                {".".join(i.split(".")[:-1]) for i in imports if i.startswith("app.")}
            )
            internal_imports_map[fn] = [get_file_name(i) for i in internal_imports]
            structure_prompt += f"{fn}\n"
            for function in functions:
                structure_prompt += "  {}()\n".format(function.name, function.args.args)

            for class_ in classes:
                structure_prompt += "  {}\n".format(class_.name)
                methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
                for method in methods:
                    structure_prompt += "  {}.{}()\n".format(class_.name, method.name)
            structure_prompt += "\n"

    return structure_prompt, content, internal_imports_map
