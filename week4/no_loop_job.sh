#!/bin/bash
#BSUB -J no_loop_haversine
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 00:10
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o output_%J.out
#BSUB -e error_%J.err

module load python3

cd /home/christian/OneDrive/DTU/02613\ Python\ and\ High\ Performance\ Computing/week4
python3 points_no_loop.py input.csv
