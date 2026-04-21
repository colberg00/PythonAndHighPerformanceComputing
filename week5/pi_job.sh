#!/bin/bash
#BSUB -J pi_timing
#BSUB -q hpc
#BSUB -n 10
#BSUB -R "span[hosts=1]"
#BSUB -W 00:10
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -o output_%J.out
#BSUB -e error_%J.err

module load python3

cd /home/christian/OneDrive/DTU/02613\ Python\ and\ High\ Performance\ Computing/week5

echo "--- Serial ---"
time python3 pi_serial.py

echo "--- Fully parallel ---"
time python3 pi_parallel.py

echo "--- Chunked parallel ---"
time python3 pi_chunked.py
