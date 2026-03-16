import sys
import random
import generate

# 1. Sortowanie przez wstawianie (Insertion Sort)
def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# 2. Sortowanie przez wybieranie (Selection Sort)
def selection_sort(arr):
    data = arr.copy()
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# GŁÓWNY ROUTER ALGORYTMÓW
def sort_using_algorithm(data, algorithm):
    if algorithm == 1:
        return insertion_sort(data)
    elif algorithm == 2:
        return selection_sort(data)
    else:
        print("Nieznany algorytm! Używam domyślnego Pythona.")
        return sorted(data)

def main():
    # --- NOWY TRYB: INTERAKTYWNY (NA ZAJĘCIA) ---
    if len(sys.argv) == 1:
        print("\n--- TEST ALGORYTMÓW SORTOWANIA ---")
        n = int(input("Podaj liczbę n (rozmiar tablicy): "))
        
        print("\nWybierz układ danych wejściowych:")
        print("1 - Losowy")
        print("2 - Rosnący")
        print("3 - Malejący")
        print("4 - Stały")
        print("5 - A-kształtny")
        data_choice = int(input("Twój wybór ciągu: "))

        # Generowanie wybranego ciągu za pomocą pliku prowadzącego
        if data_choice == 1:
            data = generate.generate_random_array(n).tolist()
        elif data_choice == 2:
            data = generate.generate_increasing_array(n).tolist()
        elif data_choice == 3:
            data = generate.generate_decreasing_array(n).tolist()
        elif data_choice == 4:
            data = generate.generate_constant_array(n).tolist()
        elif data_choice == 5:
            data = generate.generate_a_shaped_array(n).tolist()
        else:
            print("Zły wybór, generuję losowy.")
            data = generate.generate_random_array(n).tolist()

        print(f"\nTablica PRZED sortowaniem:\n{data}")
        
        print("\nWybierz algorytm:")
        print("1 - Insertion Sort")
        print("2 - Selection Sort")
        algo_choice = int(input("Twój wybór algorytmu: "))
        
        sorted_data = sort_using_algorithm(data, algo_choice)
        
        print(f"\nTablica PO sortowaniu:\n{sorted_data}\n")
        return # Zakończ tutaj, żeby nie wchodzić w kod dla stopera

    # --- STARY TRYB: BENCHMARK PROWADZĄCEGO (Zostawiamy bez zmian!) ---
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    input_data = sys.stdin.read().split()
    try:
        data = [int(x) for x in input_data[1:]]
    except EOFError:
        print("Error reading input.")

    sorted_data = sort_using_algorithm(data, algorithm_number)
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()