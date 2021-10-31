
def convert_to_latex_transposed(text: str):
    ds = dict()
    with open(text) as file:
        rows = file.read().splitlines()
        for row in rows:
            parts = row.split(" ")
            k = parts[1]
            alpha = parts[4]
            entropy = str(round(float(parts[-1]),3))
            if k in ds:
                ds[k].append((alpha, entropy))
            else:
                ds[k] = [(alpha, entropy)]
    points = "\\begin{center}\n\\begin{tabular}{c c c c c c c c c c c c c c c c c c c c} \n"
    keys = sorted(list(ds.keys()), key=lambda v: int(v), reverse=True)
    for key in keys:
        column = ds[key]
        point = " "
        for i, (alpha, value) in enumerate(column):
            if i > 0: point += " & "
            point += value
        point += " \\\\ \\hline \n"
        points += point
    points += "\\end{tabular}\n\\end{center}"
    return points


def convert_to_latex(text: str):
    points = "\\begin{center}\n\\begin{tabular}{c c c c c c c c c c c c c c c c c c c c} \n"
    with open(text) as file:
        rows = file.read().splitlines()
        for row in rows:
            parts = row.split(" ")
            point = " "
            point += str(round(float(parts[-1]),3))
            if parts[1] == str(20):
                point += " \\\\ \\hline \n"
            else:
                point += " & "
            points += point
    points += "\\end{tabular}\n\\end{center}"
    return points


def convert_to_js(text:str):
    points = 'var points = ['
    with open(text) as file:
        rows = file.read().splitlines()
        for row in rows:
            parts = row.split(" ")
            point = "{"
            for i in range(0, len(parts), 3):
                point += f'\"{parts[i].split(":")[0]}\": {parts[i+1]},'
            point += "},\n"
            points += point
    points += "]"
    return points

points = convert_to_latex_transposed("entropy.txt")
print(points)

# with open('points.js', 'w') as file:
#   file.write(points)