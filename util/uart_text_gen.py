import argparse

def coe2raw(file_name: str) -> list:
    with open(file_name, "r") as f:
        lines = f.readlines()
    
    lines = lines[2:]
    lines = list(map(lambda line: line.strip().strip(",").strip(";"), lines))
    return lines


def write_to_file(f, lines, size):
    cnt = 0
    for line in lines:
        f.write(line)
        cnt += 1
        if cnt >= size:
            break
    if cnt < size:
        for _ in range(size - cnt):
            f.write("00000000")


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        "-t", "--text", help="path to text coe to be parsed. The file must be generated by rawhex2coe.py", type=str)
    argParser.add_argument(
        "-d", "--data", help="path to data coe to be parsed. The file must be generated by rawhex2coe.py", type=str)
    argParser.add_argument(
        "-o", "--output", help="path to target file. A new file will be created if non-exist.", type=str, default="output.txt")
    argParser.add_argument(
        "-s", "--size", help="size of each segment in words (32 bit). Default to 16384.", type=int, default=16384)
    cmd_args = argParser.parse_args()

    text_lines = coe2raw(cmd_args.text)
    data_lines = coe2raw(cmd_args.data)
    size = cmd_args.size

    new_file = cmd_args.output
    with open(new_file, "w") as f:
        f.write("03020000")
        write_to_file(f, text_lines, size)
        write_to_file(f, data_lines, size)

    print(f'Text:\t"{cmd_args.text}"')
    print(f'Data:\t"{cmd_args.data}"')
    print(f'Dst:\t"{new_file}"')
    print(f'Transformed {size * 2} lines.')