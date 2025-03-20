from latex_generator.generator import generate_table, generate_image


table_data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"]
]
latex_table = generate_table(table_data)


latex_image = generate_image("image.png", "Sample Image", "0.6\\textwidth")

latex_document = (
    "\\documentclass{article}\n"
    "\\usepackage{graphicx}\n"
    "\\begin{document}\n"
    f"{latex_table}\n\n"
    f"{latex_image}\n"
    "\\end{document}"
)

with open("output.tex", "w") as f:
    f.write(latex_document)