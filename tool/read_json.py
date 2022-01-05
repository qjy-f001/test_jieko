import json


def read_json(filename):
    # 打开 获取文件流
    with open("../data/" + filename, "r", encoding="utf-8")as f:
        # 调用json.load()
        return json.load(f)


if __name__ == '__main__':
    print(read_json("login.json"))
    print("--" * 50)
    """
        问题：读取出来的格式{...}
        预期:[()]
        解决：
            1. 字典.values() # 获取字典所有的值
            2. tuple(str) # 将str强转为元祖
            3. arr.append() # 向列表中追加数据
    """
    arr = []
    arr.append(tuple(read_json("login.json").values()))
    print(arr)
