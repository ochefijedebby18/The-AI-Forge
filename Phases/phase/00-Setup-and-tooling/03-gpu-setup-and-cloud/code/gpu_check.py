import platform
import torch


def check_gpu():
    print("=== SYSTEM INFORMATION ===")
    print("Operating system:", platform.system())
    print("Processor:", platform.processor())

    print("\n=== PYTORCH INFORMATION ===")
    print("PyTorch version:", torch.__version__)

    print("\n=== CUDA INFORMATION ===")
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA version used to build PyTorch:", torch.version.cuda)
    print("Number of CUDA GPUs:", torch.cuda.device_count())

    if torch.cuda.is_available():
        print("GPU name:", torch.cuda.get_device_name(0))
    else:
        print("No CUDA-compatible GPU detected.")

    print("\n=== CPU TEST ===")
    numbers = torch.tensor([1, 2, 3, 4, 5])
    result = numbers * 2

    print("Original tensor:", numbers)
    print("Tensor multiplied by 2:", result)
    print("Tensor device:", result.device)


if __name__ == "__main__":
    check_gpu()
