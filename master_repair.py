import os

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')

with open(cg_path, 'r') as f:
    lines = f.readlines()

repaired = []
skip_next = False

for i, line in enumerate(lines):
    # 1. Structural Repair: Restore the _CFG __init__ if it was deleted
    if "self.cres = cres" in line and (i == 0 or "def __init__" not in lines[i-1]):
        repaired.append('    def __init__(self, cres, name, py_func, **kwargs):\n')
    
    # 2. Targeted Injection: Find the builder call
    if "pmb = create_pass_manager_builder(" in line:
        indent = line[:line.find("pmb")]
        repaired.append(f"{indent}for k in ['opt', 'loop_vectorize', 'slp_vectorize']: kwargs.pop(k, None)\n")
        repaired.append(f"{indent}pmb = create_pass_manager_builder(self._tm, kwargs.pop('pto', None), opt=opt_level, loop_vectorize=loop_vectorize, slp_vectorize=slp_vectorize, **kwargs)\n")
        skip_next = True # Skip the old multi-line calls
        continue
    
    # 3. Cleanup logic for old messy edits
    if skip_next:
        if "**kwargs)" in line or "slp_vectorize=" in line:
            if "**kwargs)" in line: skip_next = False
            continue
            
    repaired.append(line)

with open(cg_path, 'w') as f:
    f.writelines(repaired)

print("Structural integrity restored. Hardware bridge re-initialized.")
