import os

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')
bd_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/llvm_bindings.py')

with open(cg_path, 'r') as f:
    cg = f.read()

# 1. Reverse the destructive global replace to fix the NameError
bad_str = 'tm=self._tm, pto=__import__("llvmlite.binding", fromlist=["PipelineTuningOptions"]).PipelineTuningOptions(speed_level=opt_level, loop_vectorize=loop_vectorize, slp_vectorize=slp_vectorize), **kwargs)'
cg = cg.replace(bad_str, '**kwargs)')

# 2. Surgically inject the hardware variables ONLY right before the builder call
target = "pmb = create_pass_manager_builder("
if "kwargs['tm'] = self._tm" not in cg:
    injection = """from llvmlite.binding import PipelineTuningOptions
        kwargs['tm'] = self._tm
        kwargs['pto'] = PipelineTuningOptions(speed_level=opt_level, loop_vectorize=loop_vectorize, slp_vectorize=slp_vectorize)
        pmb = create_pass_manager_builder("""
    cg = cg.replace(target, injection)

with open(cg_path, 'w') as f:
    f.write(cg)

with open(bd_path, 'r') as f:
    bd = f.read()

# 3. Ensure the bindings catch the variables and pass them to LLVM 15
bd = bd.replace("def create_pass_builder(tm, pto):", "def create_pass_builder(*args, **kwargs):")
bd = bd.replace("def create_pass_builder():", "def create_pass_builder(*args, **kwargs):")
bd = bd.replace("return ffi.lib.LLVMPY_CreatePassBuilder(tm, pto)", "return llvm.create_pass_builder(kwargs.get('tm'), kwargs.get('pto'))")
bd = bd.replace("pmb = llvm.create_pass_builder(kwargs.get('tm'), kwargs.get('pto'))", "return llvm.create_pass_builder(kwargs.get('tm'), kwargs.get('pto'))")
bd = bd.replace("return llvm.create_pass_builder()", "return llvm.create_pass_builder(kwargs.get('tm'), kwargs.get('pto'))")

with open(bd_path, 'w') as f:
    f.write(bd)

print("Engine synchronization complete. Syntax repaired.")
