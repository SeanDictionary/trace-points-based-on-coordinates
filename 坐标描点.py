# made by SeanDictionary
import matplotlib.pyplot as plt

# 读取txt文件并解析坐标数据
def read_coordinates(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            # 去除行首行尾空白符，并去掉括号，用逗号分隔获取坐标
            line = line.strip().replace("(", "").replace(")", "")
            x, y = map(int, line.split(','))
            coordinates.append((x, y))
    return coordinates

# 绘制坐标点
def plot_coordinates(coordinates):
    x_vals = [x for x, y in coordinates]
    y_vals = [y for x, y in coordinates]

    plt.scatter(x_vals, y_vals, color='black')  # 使用scatter函数绘制散点图
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter plot')
    plt.grid(False)
    plt.show()

# 文件路径
file_path = input("输入文件路径：")
coordinates = read_coordinates(file_path)
plot_coordinates(coordinates)
