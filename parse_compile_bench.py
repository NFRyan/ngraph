import re

input_file = "build/compile_bench_out.txt"
output_file = "build/compile_bench_out.csv"

with open(output_file, 'w') as fo:
    with open(input_file, 'r') as fi:
        lines = fi.readlines()
        lines = [line.strip() for line in lines]
        lines = "\n".join(lines)

        frontend_opt_levels = re.findall(r'FRONTEND_OPT_LEVEL=(.) ', lines)
        print(frontend_opt_levels)
        backend_opt_levels = re.findall(r'BACKEND_OPT_LEVEL=(.) ', lines)
        print(backend_opt_levels)
        compile_times = re.findall(r'compile time: (.+?)ms', lines)
        print(compile_times)
        per_iteration_times = re.findall(r'\n(.+?)ms per iteration', lines)
        print(per_iteration_times)

        for f, b, c, i in zip(frontend_opt_levels, backend_opt_levels,
                              compile_times, per_iteration_times):
            print(", ".join([f, b, c, i]), file=fo)