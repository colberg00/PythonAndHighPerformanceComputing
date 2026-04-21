import sys
import pandas as pd

if __name__ == '__main__':
    fname = sys.argv[1]
    df = pd.read_csv(fname)
    total = df[df['parameterId'] == 'precip_past10min']['value'].sum()
    print(total)
