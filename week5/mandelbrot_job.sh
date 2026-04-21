#!/bin/bash
#BSUB -J mandelbrot
#BSUB -q hpc
#BSUB -n 10
#BSUB -R "span[hosts=1]"
#BSUB -W 00:15
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o output_%J.out
#BSUB -e error_%J.err

module load python3

cd /home/christian/OneDrive/DTU/02613\ Python\ and\ High\ Performance\ Computing/week5

for n_proc in 1 2 4 6 8 10; do
    echo "n_proc=$n_proc"
    time python3 mandelbrot.py $n_proc
done
