# 1

# import pandas as pd

# df = pd.read_csv('test.csv')
# df = df.drop(columns=['a'])
# print("\n删除a列后的数据:")
# print(df)

# df['c'] = df['e'] + df['b']
# print("\n执行相加操作后的数据:")
# print(df)


# 2
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="CSV操作工具")

parser.add_argument("--path", required=True, help="CSV文件路径")

parser.add_argument("--number", type=int, required=True, help="要删除的列索引")

args = parser.parse_args()

# 读取CSV文件
try:
    df = pd.read_csv(args.path)
except FileNotFoundError:
    print(f"找不到文件：{args.path}")
    exit(1)


if args.number < len(df.columns):
    deleted_column = df.columns[args.number]
    df = df.drop(columns=[deleted_column])
else:
    print("要删除的列索引超出范围")
    exit(1)

print("\n删除列后的数据:")
print(df)
