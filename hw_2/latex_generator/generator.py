def generate_table(data):
    if not data:
        return ""
    num_cols = len(data[0])
    alignment = "|".join(["l"] * num_cols)
    header = f"\\begin{{tabular}}{{|{alignment}|}}\n\\hline\n"
    rows = []
    for row in data:
        rows.append(" & ".join(map(str, row)) + " \\\\ \\hline")
    return header + "\n".join(rows) + "\n\\end{tabular}"

def generate_image(image_path, caption="", width="0.5\\textwidth"):
    return (
        "\\begin{figure}[h]\n"
        "\\centering\n"
        f"\\includegraphics[width={width}]{{{image_path}}}\n"
        f"\\caption{{{caption}}}\n"
        "\\end{figure}"
    )