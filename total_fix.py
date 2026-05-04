import os

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')

with open(cg_path, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Find the specific builder call and inject the dictionary purge immediately before it
    if "pmb = create_pass_manager_builder(" in line:
        indent = line[:line.find("pmb")]
        new_lines.append(f"{indent}for k in ['opt', 'loop_vectorize', 'slp_vectorize']: kwargs.pop(k, None)\n")
        new_lines.append(f"{indent}pmb = create_pass_manager_builder(self._tm, kwargs.pop('pto', None), opt=opt_level, loop_vectorize=loop_vectorize, slp_vectorize=slp_vectorize, **kwargs)\n")
    elif "loop_vectorize=loop_vectorize," in line or "slp_vectorize=slp_vectorize," in line or "**kwargs)" in line:
        # Skip the multi-line leftovers from previous attempts
        continue
    else:
        new_lines.append(line)

with open(cg_path, 'w') as f:
    f.writelines(new_lines)

print("JIT Stack Purged. Hardware bridge locked and loaded.")
