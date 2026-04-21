import sys
import pandas as pd

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = infile.replace('.csv', '.parquet').replace('.zip', '')
    if not outfile.endswith('.parquet'):
        outfile += '.parquet'

    df = pd.read_csv(infile)
    df.to_parquet(outfile, index=False)
    print(f'Saved to {outfile}')
