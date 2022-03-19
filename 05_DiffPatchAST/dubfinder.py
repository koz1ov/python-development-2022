import inspect
import importlib
import sys
import ast
import textwrap
import difflib

def _get_simplified_source(obj):
    source = inspect.getsource(obj)
    source = textwrap.dedent(source)
    parsed_fun = ast.parse(source)
    for node in ast.walk(parsed_fun):
        for attr in ['name', 'id', 'arg', 'attr']:
            if hasattr(node, attr):
                setattr(node, attr, '_')
       
    return ast.unparse(parsed_fun)


def _fill_functions_dict(obj, res_dict, prefix):
    
    for name, value in inspect.getmembers(obj):
        if inspect.isfunction(value):
            
            fun_name = f"{prefix}.{name}"
            res_dict[fun_name] = _get_simplified_source(value)

        elif inspect.isclass(value) and not name.startswith('__'):

            _fill_functions_dict(value, res_dict, f"{prefix}.{name}")
            
def _fill_fun_dict_from_module(module_name):
    module = importlib.import_module(module_name)
    _fill_functions_dict(module, functions_dict, module_name)

if __name__ == '__main__':
    functions_dict = {}
    _fill_fun_dict_from_module(sys.argv[1])
    if len(sys.argv) > 2:
        _fill_fun_dict_from_module(sys.argv[2])

    fun_names = sorted(functions_dict.keys())
    seq_matcher = difflib.SequenceMatcher(None)
    for idx, fun_name_1 in enumerate(fun_names):
        for fun_name_2 in fun_names[idx + 1:]:
            seq_matcher.set_seqs(functions_dict[fun_name_1], functions_dict[fun_name_2])
            if seq_matcher.ratio() > 0.95:
                print(f"{fun_name_1} : {fun_name_2}")
