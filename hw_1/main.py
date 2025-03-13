import os.path
import sys

def nl(_data):
    if len(_data) == 0:
        print("nl need args")
        return
    if len(_data) == 1 and not os.path.exists(_data[0]):
        lines = str(_data[0][1:-1]).split('\\n')
        ind = 1
        for line in lines:
            print(f"{ind:6}  {line.rstrip()}")
            ind += 1
        return

    for i, _path in enumerate(_data):
        ind = 1
        input_stream = open(_path, "r")
        if len(_data) > 1:
            print(f"==> {_path} <==")
        with input_stream:
            for line in input_stream:
                print(f"{ind:6}  {line.rstrip()}")
                ind += 1
            if i < len(_data) - 1:
                print()
    return

def tail_(file, n):
    try:
        if isinstance(file, str):
            with open(file, 'r') as f:
                lines = f.readlines()
        else:
            lines = file.readlines()

        return lines[-n:]
    except FileNotFoundError:
        print(f"tail: cannot open '{file}' for reading: No such file or directory")
        return []

def tail(_data):
    if len(_data) == 0:
        lines = tail_(sys.stdin, 17)
        sys.stdout.writelines(lines)
    else:
        for i, path in enumerate(_data):
            try:
                if len(_data) > 1:
                    print(f"==> {path} <==")

                lines = tail_(path, n=10)
                sys.stdout.writelines(lines)

                if i < len(_data) - 1:
                    print()
            except Exception as e:
                print(f"tail: error processing '{path}': {e}", file=sys.stderr)

def count_statistics(data):
    lines = data.count('\\n')
    words = len(data.split())
    bytes_ = len(data.encode('utf-8'))
    return lines + 1, words, bytes_

def wc(_data):
    total_lines = total_words = total_bytes = 0
    results = []
    for file in _data:
        if not os.path.exists(file):
                data = file[1:-1]
        else:
            with open(file, 'r') as f:
                data = f.read()
        stats = count_statistics(data)
        if stats is not None:
            lines, words, bytes_ = stats
            results.append((lines, words, bytes_, file))
            total_lines += lines
            total_words += words
            total_bytes += bytes_
    for lines, words, bytes_, file in results:
        if not os.path.exists(file):
            print(f"{lines:>8} {words:>8} {bytes_:>8}")
        else:
            print(f"{lines:>8} {words:>8} {bytes_:>8} {file}")

    if len(results) > 1:
        print(f"{total_lines:>8} {total_words:>8} {total_bytes:>8} total")


cmds = {'nl': nl, 'tail': tail, 'wc': wc}
while True:
    data = input(">>> ").split(" ", 1)
    if data[0] not in cmds:
        print("Unknown command")
        continue
    parts = []
    if len(data) < 2 or data[0]== '':
        parts = []
    elif data[1][0] == '\"' and data[1][-1] == '\"':
        parts.append(data[1])
    else:
        parts = data[1].split()
    cmds[data[0]](parts)


