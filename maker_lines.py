class Node:

    def __init__(self, data, indexloc=None, colorid='#3b3b3b'):
        self.data = data
        self.index = indexloc
        self.color = colorid


nodes = []
list_stations_first = ['Киевская', 'Парк культуры', 'Октябрьская', 'Добрынинская', 'Павелецкая', 'Таганская', 'Курская',
                       'Комсомольская', 'Проспект мира', 'Новослободская', 'Белорусская', 'Краснопресненская']
list_stations_second = ['Коммунарка', 'Ольховая', 'Прокшино', 'Филатов Луг', 'Саларьево', 'Румянцево', 'Тропарёво',
                        'Юго-Западная', 'Проспект Вернадского', 'Университет', 'Воробьёвы горы', 'Спортивная',
                        'Фрунзенская', 'Парк культуры-2', 'Кропоткинская', 'Библиотека имени Ленина', 'Охотный ряд',
                        'Лубянка', 'Чистые пруды', 'Красные ворота', 'Комсомольская-2', 'Красносельская', 'Сокольники',
                        'Преображенская площадь', 'Черкизовская', 'Бульвар Рокоссовского']
list_objects_lines_first = {
    f'a{count}': Node(i, indexloc=count, colorid='#905434') for count, i in enumerate(list_stations_first, start=1)}
list_objects_lines_second = {
    f'a{count}': Node(i, indexloc=count, colorid='#D14A45') for count, i in enumerate(list_stations_second, start=13)}

nodes.extend(list_stations_first)
nodes.extend(list_stations_second)
list_connector = []
init_graph = {}

for node in nodes:
    init_graph[node] = {}
# Первый пак станций
init_graph[list_objects_lines_first['a1'].data][list_objects_lines_first['a2'].data] = 2
list_connector.append((list_objects_lines_first['a1'].index, list_objects_lines_first['a2'].index))
init_graph[list_objects_lines_first['a2'].data][list_objects_lines_first['a3'].data] = 3
list_connector.append((list_objects_lines_first['a2'].index, list_objects_lines_first['a3'].index))
init_graph[list_objects_lines_first['a3'].data][list_objects_lines_first['a4'].data] = 2
list_connector.append((list_objects_lines_first['a3'].index, list_objects_lines_first['a4'].index))
init_graph[list_objects_lines_first['a4'].data][list_objects_lines_first['a5'].data] = 2
list_connector.append((list_objects_lines_first['a4'].index, list_objects_lines_first['a5'].index))
init_graph[list_objects_lines_first['a5'].data][list_objects_lines_first['a6'].data] = 2
list_connector.append((list_objects_lines_first['a5'].index, list_objects_lines_first['a6'].index))
init_graph[list_objects_lines_first['a6'].data][list_objects_lines_first['a7'].data] = 2
list_connector.append((list_objects_lines_first['a6'].index, list_objects_lines_first['a7'].index))
init_graph[list_objects_lines_first['a7'].data][list_objects_lines_first['a8'].data] = 2
list_connector.append((list_objects_lines_first['a7'].index, list_objects_lines_first['a8'].index))
init_graph[list_objects_lines_first['a8'].data][list_objects_lines_first['a9'].data] = 3
list_connector.append((list_objects_lines_first['a8'].index, list_objects_lines_first['a9'].index))
init_graph[list_objects_lines_first['a9'].data][list_objects_lines_first['a10'].data] = 3
list_connector.append((list_objects_lines_first['a9'].index, list_objects_lines_first['a10'].index))
init_graph[list_objects_lines_first['a10'].data][list_objects_lines_first['a11'].data] = 2
list_connector.append((list_objects_lines_first['a10'].index, list_objects_lines_first['a11'].index))
init_graph[list_objects_lines_first['a11'].data][list_objects_lines_first['a12'].data] = 2
list_connector.append((list_objects_lines_first['a11'].index, list_objects_lines_first['a12'].index))
init_graph[list_objects_lines_first['a12'].data][list_objects_lines_first['a1'].data] = 3
list_connector.append((list_objects_lines_first['a12'].index, list_objects_lines_first['a1'].index))
# Второй пак станций
init_graph[list_objects_lines_second['a13'].data][list_objects_lines_second['a14'].data] = 3
list_connector.append((list_objects_lines_second['a13'].index, list_objects_lines_second['a14'].index))
init_graph[list_objects_lines_second['a14'].data][list_objects_lines_second['a15'].data] = 4
list_connector.append((list_objects_lines_second['a14'].index, list_objects_lines_second['a15'].index))
init_graph[list_objects_lines_second['a15'].data][list_objects_lines_second['a16'].data] = 3
list_connector.append((list_objects_lines_second['a15'].index, list_objects_lines_second['a16'].index))
init_graph[list_objects_lines_second['a16'].data][list_objects_lines_second['a17'].data] = 5
list_connector.append((list_objects_lines_second['a16'].index, list_objects_lines_second['a17'].index))
init_graph[list_objects_lines_second['a17'].data][list_objects_lines_second['a18'].data] = 2
list_connector.append((list_objects_lines_second['a17'].index, list_objects_lines_second['a18'].index))
init_graph[list_objects_lines_second['a18'].data][list_objects_lines_second['a19'].data] = 4
list_connector.append((list_objects_lines_second['a18'].index, list_objects_lines_second['a19'].index))
init_graph[list_objects_lines_second['a19'].data][list_objects_lines_second['a20'].data] = 3
list_connector.append((list_objects_lines_second['a19'].index, list_objects_lines_second['a20'].index))
init_graph[list_objects_lines_second['a20'].data][list_objects_lines_second['a21'].data] = 3
list_connector.append((list_objects_lines_second['a20'].index, list_objects_lines_second['a21'].index))
init_graph[list_objects_lines_second['a21'].data][list_objects_lines_second['a22'].data] = 3
list_connector.append((list_objects_lines_second['a21'].index, list_objects_lines_second['a22'].index))
init_graph[list_objects_lines_second['a22'].data][list_objects_lines_second['a23'].data] = 3
list_connector.append((list_objects_lines_second['a22'].index, list_objects_lines_second['a23'].index))
init_graph[list_objects_lines_second['a23'].data][list_objects_lines_second['a24'].data] = 3
list_connector.append((list_objects_lines_second['a23'].index, list_objects_lines_second['a24'].index))
init_graph[list_objects_lines_second['a24'].data][list_objects_lines_second['a25'].data] = 2
list_connector.append((list_objects_lines_second['a24'].index, list_objects_lines_second['a25'].index))
init_graph[list_objects_lines_second['a25'].data][list_objects_lines_second['a26'].data] = 2
list_connector.append((list_objects_lines_second['a25'].index, list_objects_lines_second['a26'].index))

init_graph[list_objects_lines_second['a26'].data][list_objects_lines_first['a2'].data] = 5
list_connector.append((list_objects_lines_second['a26'].index, list_objects_lines_first['a2'].index))

init_graph[list_objects_lines_second['a26'].data][list_objects_lines_second['a27'].data] = 2
list_connector.append((list_objects_lines_second['a26'].index, list_objects_lines_second['a27'].index))
init_graph[list_objects_lines_second['a27'].data][list_objects_lines_second['a28'].data] = 2
list_connector.append((list_objects_lines_second['a27'].index, list_objects_lines_second['a28'].index))
init_graph[list_objects_lines_second['a28'].data][list_objects_lines_second['a29'].data] = 2
list_connector.append((list_objects_lines_second['a28'].index, list_objects_lines_second['a29'].index))
init_graph[list_objects_lines_second['a29'].data][list_objects_lines_second['a30'].data] = 1
list_connector.append((list_objects_lines_second['a29'].index, list_objects_lines_second['a30'].index))
init_graph[list_objects_lines_second['a30'].data][list_objects_lines_second['a31'].data] = 2
list_connector.append((list_objects_lines_second['a30'].index, list_objects_lines_second['a31'].index))
init_graph[list_objects_lines_second['a31'].data][list_objects_lines_second['a32'].data] = 2
list_connector.append((list_objects_lines_second['a31'].index, list_objects_lines_second['a32'].index))
init_graph[list_objects_lines_second['a32'].data][list_objects_lines_second['a33'].data] = 2
list_connector.append((list_objects_lines_second['a32'].index, list_objects_lines_second['a33'].index))

init_graph[list_objects_lines_second['a33'].data][list_objects_lines_first['a8'].data] = 5
list_connector.append((list_objects_lines_second['a33'].index, list_objects_lines_first['a8'].index))

init_graph[list_objects_lines_second['a33'].data][list_objects_lines_second['a34'].data] = 2
list_connector.append((list_objects_lines_second['a33'].index, list_objects_lines_second['a34'].index))
init_graph[list_objects_lines_second['a34'].data][list_objects_lines_second['a35'].data] = 2
list_connector.append((list_objects_lines_second['a34'].index, list_objects_lines_second['a35'].index))
init_graph[list_objects_lines_second['a35'].data][list_objects_lines_second['a36'].data] = 4
list_connector.append((list_objects_lines_second['a35'].index, list_objects_lines_second['a36'].index))
init_graph[list_objects_lines_second['a36'].data][list_objects_lines_second['a37'].data] = 3
list_connector.append((list_objects_lines_second['a36'].index, list_objects_lines_second['a37'].index))
init_graph[list_objects_lines_second['a37'].data][list_objects_lines_second['a38'].data] = 4
list_connector.append((list_objects_lines_second['a37'].index, list_objects_lines_second['a38'].index))

if __name__ == '__main__':
    print(len(list_stations_first))
    print(len(list_objects_lines_second))
    print(list_objects_lines_first)
    print(list_objects_lines_second)
    print(init_graph)
    print(list_connector)
    print([(list_objects_lines_first[i].index, list_objects_lines_first[i].data) for i in list_objects_lines_first])
    print([(list_objects_lines_second[i].index, list_objects_lines_second[i].data) for i in list_objects_lines_second])
    print([list_objects_lines_first[i].color for i in list_objects_lines_first] + [list_objects_lines_second[i_2].color
                                                                                   for i_2 in
                                                                                   list_objects_lines_second])
