import os

cg_path = os.path.expanduser('~/casanovo_env/lib/python3.13/site-packages/numba/core/codegen.py')

with open(cg_path, 'r') as f:
    lines = f.readlines()

with open(cg_path, 'w') as f:
    for line in lines:
        # Strip the unsupported vectorize arguments from the constructor call
        if "PipelineTuningOptions(speed_level=opt_level" in line:
            new_line = line.split("PipelineTuningOptions(")[0] + "PipelineTuningOptions(speed_level=opt_level)\n"
            f.write(new_line)
        else:
            f.write(line)

print("Pipeline Tuning Options aligned. Vectorization flags neutralized.")
