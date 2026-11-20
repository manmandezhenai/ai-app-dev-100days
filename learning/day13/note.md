# Day13：CSV 文件读写与表格型数据操作

## 【核心知识点】

### 1. CSV 格式与 csv 模块基础

- CSV 是逗号分隔的表格型文本格式，每行对应一条数据，字段间用逗号分隔
- Python 内置 `csv` 标准库，无需额外安装，专门处理 CSV 格式文本
- 两种常用读写模式：列表模式（按索引取字段）、字典模式（按列名取字段）
- 处理中文 CSV 文件必须指定 `encoding="utf-8"`，避免乱码

### 2. 列表模式读写 CSV

写入语法：

```python
import csv

with open(文件路径, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(表头列表)
    writer.writerows(数据行列表)
```

读取语法：

```python
import csv

with open(文件路径, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for 行列表 in reader:
        逐行处理逻辑
```

- 写入时必须加 `newline=""` 参数，避免生成的文件每行多出空行
- `writerow` 写入单行数据，`writerows` 批量写入多行二维列表
- `reader` 为可迭代对象，遍历一次后无法重复读取，需持久化可转为列表

### 3. 字典模式读写 CSV

写入语法：

```python
import csv

with open(文件路径, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=字段名列表)
    writer.writeheader()
    writer.writerows(字典列表)
```

读取语法：

```python
import csv

with open(文件路径, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for 行字典 in reader:
        通过列名访问字段
```

- `DictReader` 自动将首行作为字段名，每行返回字典，通过列名取值更直观
- `DictWriter` 写入前必须调用 `writeheader()` 写入表头，否则文件缺失列名

### 4. 表格数据基础处理

- 字段提取：遍历每行，提取指定列的数据组成新列表
- 条件筛选：按字段值过滤符合条件的数据行
- 数值统计：对数值型字段执行求和、计数、平均值计算
- 数据追加：以追加模式打开文件，在末尾新增数据行

## 【今日易错点】

1. 写入 CSV 时文件模式漏写 `newline=""`，会导致生成的文件每行多出空行
2. 读取中文 CSV 不指定 `utf-8` 编码，Windows 环境下易出现中文乱码
3. `DictWriter` 写入前忘记调用 `writeheader()`，会导致 CSV 文件缺失表头
4. 直接重复遍历 `reader` 对象会返回空，需转列表保存才能多次使用
5. 手动字符串拼接生成 CSV，遇到含逗号的字段会导致列错位，必须用 `csv` 模块处理