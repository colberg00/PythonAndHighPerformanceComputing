#!/bin/bash
#BSUB -J notify_job
#BSUB -q hpc
#BSUB -n 1
#BSUB -W 02:00
#BSUB -R "rusage[mem=2GB]"
#BSUB -o output_%J.out
#BSUB -e error_%J.err

# -B : Send email when job starts (BEGIN)
# -N : Send email when job ends (END)
#BSUB -B
#BSUB -N

# #BSUB -u your_email@example.com

# ===== ENVIRONMENT =====
module load python

# ===== EXECUTION =====
echo "Job started at $(date)"
echo "Job ID: $LSB_JOBID"
echo "Hostname: $(hostname)"

# Your actual work here
python -c "
import time
import sys
print('Running computation...')
for i in range(5):
    print(f'Step {i+1}/5')
    time.sleep(1)
print('Computation complete!')
"

echo "Job ended at $(date)"
