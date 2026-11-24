from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    arr = np.array(x)
    mean = np.mean(arr)
    median = np.median(arr)
    freq = Counter(x)
    max_freq = max(freq.values())
    # mode = []
    # for num,count in freq.items():
    #     if count == max_freq:
    #         mode.append(num)
    # mode = min(mode)
    mode = min(num for num,count in freq.items() if count == max_freq)
    return {"mean":float(mean),"median":float(median),"mode":float(mode)}