#!/bin/bash
python $HOME/scratch/count_pairs.py $HOME/scratch/common_germline_pairs > temp_commonG
mv temp_commonG germline_common_pairs
