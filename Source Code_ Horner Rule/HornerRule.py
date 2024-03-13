# Mengevaluasi suatu polinomial pada titik tertentu dengan aturan Horner
# Input: Sebuah array P[0..n] dari koefisien polinomial derajat n,
# disimpan dari terendah hingga tertinggi dan sebuah bilangan x
# Output: Nilai polinomial pada x
def evaluasi_polinomial_horner(P, x):
    # Mengambil koefisien polinomial terakhir
    p = P[-1]
    # Iterasi mundur melalui koefisien polinomial
    for i in range(len(P) - 2, -1, -1):
        # Terapkan aturan Horner
        p = x * p + P[i]
    # Kembalikan nilai polinomial pada x
    return p

# Contoh penggunaan
P = [2, -3, 1]  # Koefisien polinomial: 2x^2 - 3x + 1
x = 2  # Titik yang akan dievaluasi
hasil_evaluasi = evaluasi_polinomial_horner(P, x)
print("Hasil evaluasi polinomial pada titik x adalah", hasil_evaluasi)