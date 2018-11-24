#  分支算法执行类
class Worker:
    max = 0  # 上界 通过贪心算法找出近似值
    min = 0  # 下界 由每组的最小值组成
    pt_nodes = []  # 存放可扩展的节点
    pt_flag = 0  # 标记队列是否被使用 用于结束算法
    input_file = ''  # 输入文件名
    output_file = ''  # 输出文件名
    matrix = []  # 存放数据矩阵  行为单个任务 每个工人 完成所要的时间
    n = 0  # 数据矩阵的大小 n*n
    min_leaf_node = None  # 消耗最小的节点

    #  初始化参数
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.read_data_from_file()
        self.n = len(self.matrix)
        self.get_low_limit()
        self.get_up_limit()

        # print(self.matrix)
        # print(self.n)
        # print(self.max)
        # print(self.min)

    #  从文件中读取数据 初始化数据矩阵
    def read_data_from_file(self):
        with open(self.input_file) as source:
            for line in source:
                data_cluster = line.split(' ')
                temp = []
                for value in data_cluster:
                    temp.append(int(value))
                self.matrix.append(temp)

    #  获取数据下界  最小值之和
    def get_low_limit(self):
        for i in range(self.n):
            self.min += min(self.matrix[i])

    #  获取数据上界  贪心算法
    def get_up_limit(self):
        #  初始化工人使用标记
        worker_mark = []
        for i in range(self.n):
            worker_mark.append(0)
        # 贪心算法 取得 近似最优解
        for i in range(self.n):
            temp = self.matrix[i]
            min_value = 5000
            index = 0
            for k in range(self.n):
                if worker_mark[k] == 0 and min_value > temp[k]:
                    min_value = temp[k]
                    index = k
            worker_mark[index] = 1  # 标记工人是否被分配
            self.max += min_value  # 累积上限值

    #  分支界限算法
    def branch_limit(self):
        if self.pt_flag == 0:  # 从第一层开始
            for i in range(self.n):
                time = self.matrix[0][i]
                if time <= self.max:  # 没达到上限，创建节点，加入队列
                    node = Node()
                    node.deep = 0
                    node.cost = time
                    node.value = time
                    node.worker = i
                    self.pt_nodes.append(node)
            self.pt_flag = 1

            while self.pt_flag == 1:  # 永久循环 等队列空了在根据条件判断来结束
                if len(self.pt_nodes) == 0:
                    break
                temp = self.pt_nodes.pop(0)  # 先进先出
                present_node = temp
                total_cost = temp.cost
                present_deep = temp.deep
                #  初始化工人分配标记
                worker_mark = []
                for i in range(self.n):
                    worker_mark.append(0)

                #  检查本节点下的作业分配情况

                worker_mark[temp.worker] = 1
                while temp.father is not None:
                    temp = temp.father
                    worker_mark[temp.worker] = 1

                if present_deep + 1 == self.n:  # 最后一排的叶子节点 直接分配结果
                    if self.min_leaf_node is None:
                        self.min_leaf_node = present_node
                    else:
                        if self.min_leaf_node.cost > present_node.cost:
                            self.min_leaf_node = present_node
                else:
                    children = self.matrix[present_deep + 1]
                    #  检查本节点的子节点是否符合进入队列的要求
                    for k in range(self.n):
                        if children[k] + total_cost <= self.max and worker_mark[k] == 0:
                            node = Node()
                            node.deep = present_deep + 1
                            node.cost = children[k] + total_cost
                            node.value = children[k]
                            node.worker = k
                            node.father = present_node
                            self.pt_nodes.append(node)

    #  输出算法执行的结果
    def output_result(self):
        file = open(self.output_file,'a')
        temp = self.min_leaf_node
        file.write('最少的消耗为：' + str(temp.cost) + '\n')
        file.write('第'+str(temp.worker+1) + '位工人完成第'+str(temp.deep+1) + '份工作\n')
        while temp.father is not None:
            temp = temp.father
            file.write('第' + str(temp.worker + 1) + '位工人完成第' + str(temp.deep + 1) + '份工作\n')
        print('算法执行结果以及写入到文件：', self.output_file)


#  分支节点类
class Node:
    def __init__(self):
        self.deep = 0  # 标记该节点的深度
        self.cost = 0  # 标记到达该节点的总消费
        self.father = None  # 标记该节点的父节点
        self.value = 0  # 本节点的消费值
        self.worker = 0  # 本节点的该任务由第几位工人完成

#  主逻辑
# input_file = 'input_assign05_01.dat'
# input_file = 'input_assign05_02.dat'
input_file = 'input.txt'
# output_file = 'output_01.dat'
# output_file = 'output_02.dat'
output_file = 'output.txt'

#  初始化算法执行类
worker = Worker(input_file, output_file)
#  执行分支界限算法
worker.branch_limit()
#  输出结果
worker.output_result()
