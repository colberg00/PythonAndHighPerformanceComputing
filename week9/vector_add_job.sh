#!/bin/bash
# Week 9 - Exercise 2.2 (CUDA Vector Addition): GPU job script
#BSUB -J vector_add
#BSUB -q c02613
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -W 00:10
#BSUB -R "rusage[mem=2GB]"
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -o output_%J.out
#BSUB -e error_%J.err

module load python3
module load cuda

cd /home/christian/OneDrive/DTU/02613\ Python\ and\ High\ Performance\ Computing/week9
python3 vector_add.py
