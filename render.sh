#!/bin/bash

dst=$1
score=$2
d_score=$3
width=$4
height=$5
exclude_list=$6
if [[ -n "$exclude_list" ]]; then
    python3 generate.py $score $d_score $width $height $dst.json --exclude_list $exclude_list
else
    python3 generate.py $score $d_score $width $height $dst.json
fi
python3 render.py $dst.json $dst.dot
dot -Tpng $dst.dot -o $dst.png
display $dst.png
