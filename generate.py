import json
import argparse

def render(width, height, score, diagonal_score):
    space = {}
    for i in range(0, int(height)):
        for c in range(0, int(width)):
            space[f"{chr(c + ord('a') )}_{i}"] = []
            print(c)
            if i < int(height) - 1:
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c+ord('a'))}_{i+1}", score))
            if i > 0:
                if c < int(width) - 1:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') + 1)}_{i-1}", diagonal_score))
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a'))}_{i-1}", score))
            
            if c < int(width) - 1:
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') + 1)}_{i}", score))
                if i < int(height) - 1:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') + 1)}_{i+1}", diagonal_score))
            
            if c > 0:
                space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') - 1)}_{i}", score))
                if i < int(width) - 1:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') - 1)}_{i+1}", diagonal_score))
                if i > 0:
                    space[f"{chr(c+ord('a'))}_{i}"].append((f"{chr(c + ord('a') - 1)}_{i-1}", diagonal_score))
                
    return space

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('score')
    parser.add_argument('diagonal_score')
    parser.add_argument('width')
    parser.add_argument('height')
    parser.add_argument('dst')
    args = parser.parse_args()
    with open(args.dst, "w") as _file:
        data = render(args.width, args.height, args.score, args.diagonal_score)
        print(data)
        json.dump(data, _file)

