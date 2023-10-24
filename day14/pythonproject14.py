import os
import time
import concurrent.futures
import pandas as pd

# 装饰器，用于记录程序运行时间
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

# 统计单词个数的函数
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# 多进程处理文件
@timing_decorator
def process_files_with_multiprocessing(file_paths, num_processes, num_threads):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(count_words_in_file, file_paths))
    return results

# 多线程处理文件
@timing_decorator
def process_files_with_multithreading(file_paths, num_threads):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(count_words_in_file, file_paths))
    return results

if __name__ == "__main__":
    input_directory = 'your_input_directory'
    output_csv = 'word_counts.csv'
    file_paths = [os.path.join(input_directory, filename) for filename in os.listdir(input_directory)]

    num_processes = 2  # 设置进程数
    num_threads = 4    # 设置线程数

    # 使用多进程处理文件
    process_results = process_files_with_multiprocessing(file_paths, num_processes, num_threads)

    # 使用多线程处理文件
    thread_results = process_files_with_multithreading(file_paths, num_threads)

    # 保存结果到CSV文件
    df = pd.DataFrame({'File': file_paths, 'Word Count (Multiprocessing)': process_results, 'Word Count (Multithreading)': thread_results})
    df.to_csv(output_csv, index=False)
