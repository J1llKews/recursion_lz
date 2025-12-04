def pascal_triangle(n):
    if n == 1: 
        return [[1]]
    triangle = pascal_triangle(n - 1)
    last_row = triangle[-1]  
    new_row = [1] + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))] + [1]
    return triangle + [new_row]

def main():
    first = int(input("Введите количество строк треугольника Паскаля: "))
    triangle = pascal_triangle(first)

    print("Треугольник Паскаля:")
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()
