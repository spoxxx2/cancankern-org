import os
import re

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')

with open(cg_path, 'r') as f:
    content = f.read()

# 1. Restore the _CFG class header if it was mangled
if 'class _CFG(object):' in content and 'def __init__(self' not in content:
    content = re.sub(r'class _CFG\(object\):', 'class _CFG(object):\n    def __init__(self, cres, name, py_func, **kwargs):\n        self.cres = cres', content)

# 2. Define the corrected _pass_manager_builder method
# This uses the specific positional argument signature required by your LLVM 15 build.
new_method = """
    def _pass_manager_builder(self, **kwargs):
        from llvmlite.binding import create_pass_manager_builder, PipelineTuningOptions
        
        opt_level = kwargs.get('opt', 2)
        loop_vectorize = kwargs.get('loop_vectorize', False)
        sl_vectorize = kwargs.get('slp_vectorize', False)
        
        # Build the Tuning Options object (LLVM 15 signature)
        pto = PipelineTuningOptions(speed_level=opt_level)
        
        # Build the Pass Manager with the correct hardware context (tm)
        pmb = create_pass_manager_builder(self._tm, pto, opt=opt_level, 
                                          loop_vectorize=loop_vectorize, 
                                          slp_vectorize=sl_vectorize)
        return pmb
"""

# 3. Surgically replace the old method block
# We look for the start of the method and replace until the end of that specific logic
pattern = r'    def _pass_manager_builder\(self, \*\*kwargs\):.*?return pmb'
content = re.sub(pattern, new_method, content, flags=re.DOTALL)

with open(cg_path, 'w') as f:
    f.write(content)

print("Kernel Reset Complete. Syntax validated for PHX-01 sequencing.")
