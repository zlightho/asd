import matplotlib.pyplot as plt
import networkx as nx

# Данные о клиентах до 14.12.2023
before = {
    "not_ordered_anywhere": 64857,
    "ordered_smkt": 506775,
    "ordered_mm": 672697,
    "ordered_sm": 650468,
    "ordered_smkt_and_mm": 307710,
    "ordered_smkt_and_sm": 330525,
    "ordered_mm_and_sm": 446238,
    "ordered_everywhere": 232002
}

# Данные о клиентах с 14.12.2023 по 24.01.2024
after = {
    "not_ordered_anywhere": 141887,
    "ordered_smkt": 366953,
    "ordered_mm": 496565,
    "ordered_sm": 448645,
    "ordered_smkt_and_mm": 122631,
    "ordered_smkt_and_sm": 118413,
    "ordered_mm_and_sm": 208436,
    "ordered_everywhere": 59641
}

# Создание графа для перетоков
G = nx.DiGraph()

# Добавление узлов для состояний "до" и "после"
for state in before.keys():
    G.add_node(state + "_before")
    G.add_node(state + "_after")

# Добавление ребер с весами, представляющими перетоки
# Это упрощенная версия, реальное распределение перетоков может быть сложнее и требует более детальных данных
for state in before.keys():
    G.add_edge(state + "_before", state + "_after", weight=after[state])

# Настройка позиций узлов для удобства визуализации
pos = {**{state + "_before": (0, i) for i, state in enumerate(before.keys())},
       **{state + "_after": (1, i) for i, state in enumerate(after.keys())}}

# Рисование графа
plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Перетоки клиентов до и после 14.12.2023")

# Добавление меток для значений "после"
for state in after.keys():
    x, y = pos[state + "_after"]
    plt.text(x + 0.1, y, str(after[state]), horizontalalignment='left', verticalalignment='center', fontsize=10, color='black')

plt.savefig('customer_flow_with_values.png')
plt.show()
