import random
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

def randomise_matrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            matrix[i][j] = random.randint(0, 10)

def multiply_matrices(matrix1, matrix2, n1, m1, n2, m2):
    result = [[0] * m2 for i in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

if __name__ == '__main__':
    random.seed(time.time())
    n1, m1, n2, m2 = 500, 250, 250, 600
    matrix1 = [[0] * m1 for i in range(n1)]
    matrix2 = [[0] * m2 for i in range(n2)]
    randomise_matrix(matrix1, n1, m1)
    randomise_matrix(matrix2, n2, m2)
    threads_num = [1, 2, 3] # список количества потоков для тестирования
    results = [] # список результатов для каждого теста
    times = [] # список времени выполнения каждого теста
    for i in threads_num:
        start_time = time.time()
        pool = mp.Pool(processes=i)
        res = [pool.apply(multiply_matrices, args=(matrix1[j * n1 // i:(j + 1) * n1 // i], matrix2, n1 // i, m1, n2, m2)) for j in range(i)]
        pool.close()
        pool.join()
        end_time = time.time()
        time_taken = end_time - start_time
        results.append([r for res in res for r in res])
        times.append(time_taken)
    # график зависимости времени выполнения от количества потоков
    plt.plot(threads_num, times)
    plt.xlabel('Number of Threads')
    plt.ylabel('Time Taken (s)')
    plt.title('Matrix Multiplication')
    plt.savefig('GravikZav.png')
