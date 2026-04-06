import cupy as cp

# 乱数＆FFT（GPU）
x = cp.random.rand(1_048_576).astype(cp.float32)   # 1Mポイント
y = cp.fft.fft(x)
cp.cuda.Stream.null.synchronize()
print("OK: FFT size =", y.size, "dtype =", y.dtype)