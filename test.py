import file_parser

file_names = [
    "input/easy.input",
    "input/medium.input"
]
lines_per_file = {}
for file_name in file_names:
    lines_per_file[file_name] = file_parser.read_file(file_name)

for file_name, lines in lines_per_file.items():
    f = file_parser.write_file(file_name.replace("input", "output"))
    f.write('\n'.join(map(str, lines)))
    f.write("\nOUTPUT")

