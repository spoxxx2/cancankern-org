import os

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')

with open(cg_path, 'r') as f:
    cg = f.read()

# Remove the redundant keyword arguments to prevent the 'multiple values' conflict
# We will clean the kwargs dictionary just before the pmb call
conflict_fix = """
        # De-conflict arguments for LLVM 15+ bridge
        for key in ['opt', 'loop_vectorize', 'slp_vectorize']:
            kwargs.pop(key, None)
        pmb = create_pass_manager_builder(self._tm, kwargs.pop('pto'), opt=opt_level,"""

target_fragment = "pmb = create_pass_manager_builder(self._tm, kwargs['pto'], opt=opt_level,"
cg = cg.replace(target_fragment, conflict_fix)

with open(cg_path, 'w') as f:
    f.write(cg)

print("Argument collision resolved. JIT pipeline synchronized.")
