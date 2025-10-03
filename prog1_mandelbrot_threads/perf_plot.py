import pandas as pd
import matplotlib.pyplot as plt

figurefilename = '/home/ruihan/courses/stf-cs149/asst1/prog1_mandelbrot_threads/thread_perf_view2.png'
csvfilename = '/home/ruihan/courses/stf-cs149/asst1/prog1_mandelbrot_threads/thread_perf_view2.csv'

df = pd.read_csv(csvfilename)
df = df.sort_values(by='numThread').reset_index(drop=True)


plt.figure(figsize=(10, 6))

baseline_time = df[df['numThread'] == 1]['timeInMs'].iloc[0]
df['Speedup'] = baseline_time / df['timeInMs']

# 一次性绘制所有数据点，X轴是线程数，Y轴是加速比
plt.plot(
    df['numThread'],         # X轴: Number of Threads
    df['Speedup'],           # Y轴: Calculated Speedup Ratio
    marker='o',              # 在每个数据点上显示圆点
    linestyle='-',           # 绘制连接点之间的线条
    color='blue'
)

# 4. 绘制理想加速比（Optional，但推荐）：理想情况下，Speedup = numThread
plt.plot(
    df['numThread'], 
    df['numThread'], 
    linestyle='--', 
    color='red', 
    label='Ideal Speedup'
)

plt.title('Speedup with different number of threads')
plt.xlabel('Number of Threads')
plt.ylabel('Speedup Ratio')

plt.tight_layout()
plt.savefig(figurefilename)