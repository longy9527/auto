import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def load_file():
    # 使用文件对话框获取文件路径
    file_path = filedialog.askopenfilename(title="选择文件", filetypes=[("文本文件", "*.txt")])
    return file_path

def save_file():
    # 使用文件对话框获取保存文件路径
    return filedialog.asksaveasfilename(title="保存文件为", defaultextension=".txt", filetypes=[("文本文件", "*.txt")])

def remove_duplicates(file1_path, file2_path, output_path):
    try:
        # 从文件加载数据
        df1 = pd.read_csv(file1_path, header=None, names=['Data'], dtype=str)
        df2 = pd.read_csv(file2_path, header=None, names=['Data'], dtype=str)

        # 格式化电话号码，删除非数字字符
        df1['Data'] = df1['Data'].str.replace(r'\D', '', regex=True)
        df2['Data'] = df2['Data'].str.replace(r'\D', '', regex=True)

        # 查找两个数据集中的独特元素（对称差集）
        unique_data = pd.concat([df1, df2]).drop_duplicates(keep=False)

        # 将独特结果保存到新文件
        unique_data.to_csv(output_path, index=False, header=False)
        messagebox.showinfo("成功", "独特条目已保存到新文件。")
    except Exception as e:
        messagebox.showerror("错误", str(e))

def main_app():
    root = tk.Tk()
    root.title("文本文件比对器（含电话号码格式化）")

    # 配置网格布局
    root.grid_columnconfigure(1, weight=1)

    # 第一个文件的输入框
    entry1 = tk.Entry(root, width=50)
    entry1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="浏览...", command=lambda: entry1.insert(0, load_file())).grid(row=0, column=2, padx=10)

    # 第二个文件的输入框
    entry2 = tk.Entry(root, width=50)
    entry2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(root, text="浏览...", command=lambda: entry2.insert(0, load_file())).grid(row=1, column=2, padx=10)

    # 处理文件的按钮
    tk.Button(root, text="比较并删除重复", command=lambda: remove_duplicates(entry1.get(), entry2.get(), save_file())).grid(row=2, column=1, padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_app()
