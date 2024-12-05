import argparse
import json

def get_data(filename):
    with open(filename, "r") as _file:
        data = json.load(_file)

    return data

def render(data, dst):
    buff = []
    with open(dst, "w") as _file:
        _file.write("graph G {")  
        _file.write("layout=fdp;")
        _file.write("dist=10.0;")
        _file.write("node [shape=circle, width=0.1];")
        for vertice, edges in data.items():
            for edge in edges:
                if f"{edge[0]} -- {vertice} [label=\"{edge[1]}\"]\n" not in buff:
                    buff.append(f"{vertice} -- {edge[0]} [label=\"{edge[1]}\"]\n")
                    _file.write(f"{vertice} -- {edge[0]} [label=\"{edge[1]}\"]\n")
        _file.write("}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('dst')
    args = parser.parse_args()

    render(get_data(args.src), args.dst)
