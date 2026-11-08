import sys
import numpy as np
import torch


def check_python():
    print("=== PYTHON ENVIRONMENT ===")
    print("Python version:", sys.version)


def check_numpy():
    print("\n=== NUMPY CHECK ===")

    numbers = np.array([1, 2, 3])

    print("NumPy version:", np.__version__)
    print("Vector:", numbers)
    print("Dot product:", np.dot(numbers, numbers))


def check_pytorch():
    print("\n=== PYTORCH CHECK ===")

    tensor = torch.tensor([1, 2, 3])

    print("PyTorch version:", torch.__version__)
    print("Tensor:", tensor)
    print("Tensor multiplied by 2:", tensor * 2)
    print("CUDA available:", torch.cuda.is_available())


def main():
    check_python()
    check_numpy()
    check_pytorch()


if __name__ == "__main__":
    main()