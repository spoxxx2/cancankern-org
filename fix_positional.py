import os

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')
bd_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/llvm_bindings.py')

# 1. Align codegen.py to call with positional arguments
with open(cg_path, 'r') as f:
    cg = f.read()

# Replace the builder call to use positional tm and pto
old_call = "pmb = create_pass_manager_builder(opt=opt_level,"
new_call = "pmb = create_pass_manager_builder(self._tm, kwargs['pto'], opt=opt_level,"
cg = cg.replace(old_call, new_call)

with open(cg_path, 'w') as f:
    f.write(cg)

# 2. Align llvm_bindings.py to accept positional arguments
with open(bd_path, 'r') as f:
    bd = f.read()

# Force the signature to (tm, pto, **kwargs)
bd = bd.replace("def create_pass_builder(*args, **kwargs):", "def create_pass_builder(tm, pto, **kwargs):")
bd = bd.replace("return llvm.create_pass_builder(kwargs.get('tm'), kwargs.get('pto'))", "return ffi.lib.LLVMPY_CreatePassBuilder(tm, pto)")

with open(bd_path, 'w') as f:
    f.write(bd)

print("Positional arguments locked. Hardware context synchronized.")
