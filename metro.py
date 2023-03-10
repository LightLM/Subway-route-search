import sys
from maker_lines import nodes, list_objects_lines_first, list_objects_lines_second, init_graph, list_connector, nodes_piter, list_objects_lines_first_piter, init_graph_piter, list_connector_piter
from pyvis.network import Network


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика. Другими словами, если существует путь от узла A к B со значением V, должен быть путь от узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        'Возвращает узлы графа'
        return self.nodes

    def get_outgoing_edges(self, node):
        'Возвращает соседей узла'
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        'Возвращает значение ребра между двумя узлами.'
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # Мы будем использовать этот словарь, чтобы сэкономить на посещении каждого узла и обновлять его по мере продвижения по графику
    shortest_path = {}

    # Мы будем использовать этот dict, чтобы сохранить кратчайший известный путь к найденному узлу
    previous_nodes = {}

    # Мы будем использовать max_value для инициализации значения "бесконечности" непосещенных узлов
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # Однако мы инициализируем значение начального узла 0
    shortest_path[start_node] = 0

    # Алгоритм выполняется до тех пор, пока мы не посетим все узлы
    while unvisited_nodes:
        # Приведенный ниже блок кода находит узел с наименьшей оценкой
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # Приведенный ниже блок кода извлекает соседей текущего узла и обновляет их расстояния
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # После посещения его соседей мы отмечаем узел как "посещенный"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Добавить начальный узел вручную
    path.append(start_node)

    print('Найден следующий лучший маршрут с временем {} минуты.'.format(shortest_path[target_node]))
    print(' -> '.join(reversed(path)))


if __name__ == '__main__':
    while True:
        city = input('Выберите город(Москва или Питер): ')
        if city == 'Москва':
            net = Network()  # Объект
            net.add_nodes(
                list(range(1, len(nodes) + 1)),
                label=nodes,
                color=[list_objects_lines_first[i].color for i in list_objects_lines_first] + [list_objects_lines_second[i].color for i in list_objects_lines_second],
                size=[12 for i in range(len(nodes))],
                x=[-600, -500, -350, -250, -100, 0, 0, -100, -250, -350, -500, -600, -500, -550, -600, -650, -650, -650,
                   -650,
                   -650, -650, -650, -600, -550, -515, -455,
                   -400, -350, -275, -225, -175, -125, -70, 30, 80, 150, 110, 60],
                y=[400, 500, 550, 550, 500, 400, 200, 100, 50, 50, 100, 200, 1250, 1200, 1150, 1100, 1050, 1000, 950,
                   900, 800,
                   700, 650, 600, 565, 500, 450, 400, 325,
                   275, 225, 175, 120, 20, -30, -100, -140, -185],
            )
            net.add_edges(list_connector)
            net.barnes_hut(gravity=0, central_gravity=0)
            net.show('graph_moscow.html')
            graph = Graph(nodes, init_graph)
            while True:
                station = input('Введите первую станцию: ')
                station_2 = input('Введите вторую станцию: ')
                if station and station_2 in nodes:
                    break
                print('\nПоробуйте заново. Error: Неправильная станция!\n')
            previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=station)
            print_result(previous_nodes, shortest_path, start_node=station, target_node=station_2)
            break


        elif city == 'Санкт-Петербург' or city == 'Питер':
            net = Network()  # Объект
            net.add_nodes(list(range(1, len(nodes_piter) + 1)),
                          label=nodes_piter,
                          color=[list_objects_lines_first_piter[i].color for i in list_objects_lines_first_piter],
                          size=[12 for i in range(len(nodes_piter))],
                          )
            net.add_edges(list_connector_piter)
            net.barnes_hut(gravity=0, central_gravity=0)
            net.show('graph_piter.html')
            graph_piter = Graph(nodes_piter, init_graph_piter)
            while True:
                station_piter = input('Введите первую станцию: ')
                station_2_piter = input('Введите вторую станцию: ')
                if station_piter and station_2_piter in nodes_piter:
                    break
                print('\nПоробуйте заново. Error: Неправильная станция!\n')
            previous_nodes, shortest_path = dijkstra_algorithm(graph=graph_piter, start_node=station_piter)
            print_result(previous_nodes, shortest_path, start_node=station_piter, target_node=station_2_piter)
            break
        else:
            print('\nError: Неправильно набран город. Поробуйте еще раз.')
