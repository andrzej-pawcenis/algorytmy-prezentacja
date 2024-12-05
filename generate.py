import json
import argparse

def render(width, height, score, diagonal_score, exlude_list):
    space = {}
    for i in range(0, int(height)):
        for c in range(0, int(width)):
            if f"{chr(c + ord('a') )}_{i}" in exlude_list:
                continue
            space[f"{chr(c + ord('a') )}_{i}"] = []
            if i < int(height) - 1 and f"{chr(c + ord('a') )}_{i+1}" not in exlude_list:
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c+ord('a'))}_{i+1}", score))
            if i > 0 and f"{chr(c + ord('a')  )}_{i-1}" not in exlude_list:
                if c < int(width) - 1 and f"{chr(c + ord('a') + 1 )}_{i-1}" not in exlude_list:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') + 1)}_{i-1}", diagonal_score))
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a'))}_{i-1}", score))
            
            if c < int(width) - 1 and f"{chr(c + ord('a') +1 )}_{i}" not in exlude_list:
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') + 1)}_{i}", score))
                
                if i < int(height) - 1 and f"{chr(c + ord('a') + 1)}_{i+1}" not in exlude_list:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') + 1)}_{i+1}", diagonal_score))
            
            if c > 0 and f"{chr(c + ord('a') -1 )}_{i}" not in exlude_list:
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') - 1)}_{i}", score))
                if i < int(width) - 1 and f"{chr(c + ord('a') -1 )}_{i+1}" not in exlude_list:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') - 1)}_{i+1}", diagonal_score))
                if i > 0 and f"{chr(c + ord('a') -1 )}_{i-1}" not in exlude_list:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') - 1)}_{i-1}", diagonal_score))
                
    return space

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('score')
    parser.add_argument('diagonal_score')
    parser.add_argument('width')
    parser.add_argument('height')
    parser.add_argument('dst')
    parser.add_argument('--exclude_list', default="")
    args = parser.parse_args()
    exclude_list = args.exclude_list.split(",")
    with open(args.dst, "w") as _file:
        data = render(args.width, args.height, args.score, args.diagonal_score, exclude_list)
        json.dump(data, _file)

