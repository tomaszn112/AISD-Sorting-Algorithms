import sys
import random
import generate
from insertionSort import insertionSort
from selectionSort import selectionSort
from heapsort import heapsort

#Wybór algorytmu
def sort_using_algorithm(data, algorithm):
    if algorithm == 1:
        return insertionSort(data)
    elif algorithm == 2:
        return selectionSort(data)
    elif algorithm == 3:
        return heapsort(data)
    else:
        print("Nieznany algorytm! Używam domyślnego Pythona.")
        return sorted(data)


def main():
    if len(sys.argv) == 1:
        print("ALGORYTMY SORTOWANIA")          
        #Rozmiar tablicy
        n = int(input("Podaj liczbę n (rozmiar tablicy): "))
        
        #Rodzaj ciągu wejściowego
        print("\nWybierz rodzaj ciągu wejściowego:")
        print("1 - Losowy")
        print("2 - Rosnący")
        print("3 - Malejący")
        print("4 - Stały")
        print("5 - A-kształtny")
        inputChoice = int(input("Twój wybór ciągu wejściowego: "))

        if inputChoice == 1:
            data = generate.generate_random_array(n).tolist()
        elif inputChoice == 2:
            data = generate.generate_increasing_array(n).tolist()
        elif inputChoice == 3:
            data = generate.generate_decreasing_array(n).tolist()
        elif inputChoice == 4:
            data = generate.generate_constant_array(n).tolist()
        elif inputChoice == 5:
            data = generate.generate_a_shaped_array(n).tolist()

        print("\nTablica przed sortowaniem:\n", data)
        
        #Wybór algorytmu
        print("\nWybierz algorytm:")
        print("1 - Insertion Sort")
        print("2 - Selection Sort")
        print("3 - Heap Sort")
        algorithmChoice = int(input("Twój wybór algorytmu: "))
        
        sortedData = sort_using_algorithm(data, algorithmChoice)
        
        print(f"\nTablica po sortowaniu:\n", sortedData)
        return

    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    input_data = sys.stdin.read().split()
    try:
        data = [int(x) for x in input_data[1:]]
    except EOFError:
        print("Error reading input.")

    sortedData = sort_using_algorithm(data, algorithm_number)
    print("Sorted data:", sortedData[0:10])

if __name__ == "__main__":
    main()