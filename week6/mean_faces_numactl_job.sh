#!/bin/bash
#BSUB -J mean_faces_numa
#BSUB -q hpc
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -W 00:20
#BSUB -R "rusage[mem=8GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o output_%J.out
#BSUB -e error_%J.err

module load python3

cd /home/christian/OneDrive/DTU/02613\ Python\ and\ High\ Performance\ Computing/week6

DATA=/dtu/projects/02613_2025/data/celeba/celeba_100K.npy

for n_proc in 1 2 4 8 16; do
    echo "n_proc=$n_proc"
    numactl --interleave=all python3 mean_faces.py $DATA $n_proc
done
