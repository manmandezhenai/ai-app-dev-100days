# Day12：JSON 数据读写与结构化处理

## 【核心知识点】

### 1. JSON 模块基础与数据类型对应

- JSON 是通用结构化数据格式，Python 通过标准库 `json` 实现读写，无需额外安装
- Python 与 JSON 数据类型映射关系：

| Python 数据类型      | JSON 对应类型        |
|------------------|------------------|
| `dict`           | `object`（对象）     |
| `list` / `tuple` | `array`（数组）      |
| `str`            | `string`（字符串）    |
| `int` / `float`  | `number`（数字）     |
| `True` / `False` | `true` / `false` |
| `None`           | `null`           |

### 2. 序列化：Python 数据转 JSON

字符串序列化语法：

```python
import json

json字符串 = json.dumps(Python数据, ensure_ascii=False, indent=缩进空格数)
```

文件写入序列化语法：

```python
import json

with open(文件路径, "w", encoding="utf-8") as f:
    json.dump(Python数据, f, ensure_ascii=False, indent=缩进空格数)
```

- `ensure_ascii=False`：保留中文正常显示，避免转为 Unicode 编码
- `indent`：设置缩进空格数，格式化输出提升可读性

### 3. 反序列化：JSON 转 Python 数据

字符串反序列化语法：

```python
import json

Python数据 = json.loads(JSON字符串)
```

文件读取反序列化语法：

```python
import json

with open(文件路径, "r", encoding="utf-8") as f:
    Python数据 = json.load(f)
```

- 解析失败会触发 `JSONDecodeError` 异常，可通过异常捕获处理非法 JSON
- 从文件读取时必须指定 `encoding="utf-8"`，避免中文乱码

### 4. 结构化 JSON 数据处理

- 访问嵌套数据：按层级逐层通过键或索引取值，`数据["键名"][索引]["子键名"]`
- 遍历数组：使用 for 循环遍历 JSON 数组中的每个对象
- 字段提取：批量提取对象列表中的指定字段，组成新列表
- 数据过滤：按条件筛选符合要求的 JSON 对象

## 【今日易错点】

1. 序列化中文不加 `ensure_ascii=False`，中文会显示为 Unicode 编码字符
2. JSON 字符串的键必须使用双引号，单引号内容解析会触发 `JSONDecodeError`
3. 混淆 `dumps` / `dump`、`loads` / `load`，传入字符串 / 文件对象类型不匹配会报错
4. 访问嵌套 JSON 时层级或键名写错，会触发 `KeyError` 或索引越界错误
5. 直接序列化 Python 特有类型（如集合、自定义对象）会触发类型错误