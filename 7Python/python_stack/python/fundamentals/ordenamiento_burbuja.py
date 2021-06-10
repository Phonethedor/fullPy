#intercambio de elementos en python
#arr = [1,3,5,7]
#arr[0], arr[1] = arr[1], arr[0]
#\n es el elemento para nueva linea
arr = [8,1,5,3,2,0]
#metodo 1
def ordenBurbuja(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(ordenBurbuja(arr))