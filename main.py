import networkx as nx
import matplotlib.pyplot as plt


def main():
    # 1. Definiujemy zbiór S: liczby całkowite od -3 do 3
    S = list(range(-3, 4))

    # 2. Tworzymy pusty graf skierowany
    G = nx.DiGraph()
    G.add_nodes_from(S)

    default_relation = "(x - y) % 2 == 0"

    print(f"Set S = {S}")
    print("Enter a relation condition using variables 'x' and 'y'.")
    print(f"Press ENTER to use the default relation: {default_relation}")
    print("-" * 50)

    user_input = input("Your condition (or press ENTER): ").strip()

    if not user_input:
        relation_str = default_relation
        print(f"-> Default relation selected: {relation_str}")
    else:
        relation_str = user_input
        print(f"-> Custom relation selected: {relation_str}")

    # 3. Definiujemy warunek relacji i dodajemy krawędzie
    edges = []
    print("\nPairs that satisfy the relation:")

    try:
        for x in S:
            for y in S:
                if eval(relation_str):
                    edges.append((x, y))

    except Exception as e:
        print(f"\n[ERROR] Failed to evaluate the relation: {e}")
        print("Make sure you use correct syntax (e.g. '==' instead of '=').")
        return

    G.add_edges_from(edges)

    # 4. Rysowanie grafu
    plt.figure(figsize=(9, 7))
    pos = nx.circular_layout(G)

    # Rysowanie węzłów
    nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightgreen', edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Rysowanie krawędzi z zakrzywieniem (aby widzieć relacje zwrotne)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20,
                           connectionstyle='arc3, rad=0.1', edge_color='gray')

    plt.title(f"Relation visualization:\n{relation_str}", fontsize=14)
    plt.axis('off')

    # Dodanie informacji o zbiorze na dole wykresu
    plt.figtext(0.5, 0.02, f"Set S: {S}", ha="center", fontsize=10, style='italic')

    plt.show()


if __name__ == "__main__":
    main()