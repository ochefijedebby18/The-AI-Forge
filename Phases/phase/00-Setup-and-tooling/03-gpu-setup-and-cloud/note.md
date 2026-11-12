# Phase 00 — Lesson 03: GPU Setup & Cloud

## 1. Introduction

A GPU (Graphics Processing Unit) is a processor designed to handle many operations simultaneously.

Although GPUs were originally designed for graphics processing, they are now widely used in Artificial Intelligence, Machine Learning, Deep Learning and scientific computing.

AI workloads often involve large amounts of mathematical calculations, particularly matrix multiplication and tensor operations. GPUs can accelerate these calculations through parallel processing.

## 2. CPU vs GPU

### CPU — Central Processing Unit

A CPU is designed to handle general-purpose computing tasks.

It is responsible for executing instructions, managing operating system operations and running applications.

### GPU — Graphics Processing Unit

A GPU is designed to perform many operations in parallel.

This makes it particularly useful for:
- Deep learning.
- Neural network training.
- Matrix multiplication.
- Image processing.
- Large-scale tensor operations.

### Main difference

A CPU typically has fewer, more complex processing cores, while a GPU has many processing units designed for parallel workloads.

Neither is universally better. The right processor depends on the task.

## 3. Understanding CUDA

CUDA stands for Compute Unified Device Architecture.

It is NVIDIA's parallel computing platform and programming model that allows compatible GPUs to perform general-purpose computing tasks.

CUDA enables frameworks such as PyTorch to use supported NVIDIA GPUs for accelerated computations.

Important distinction:

Having a CUDA-enabled PyTorch installation does not automatically mean that a computer has an NVIDIA GPU or that CUDA is available.

## 4. Understanding VRAM

VRAM means Video Random Access Memory.

It is memory associated with a GPU.

In AI workloads, VRAM stores information such as:
- Model parameters.
- Input data.
- Intermediate calculations.
- Activations during neural network training.

Insufficient VRAM can prevent large models or batches from fitting onto a GPU.

## 5. My Computer's Hardware Investigation

I used the following Linux commands to investigate my graphics hardware.

### Identify graphics hardware

```bash
lspci | grep -Ei 'VGA|3D|Display'
```

Result:

```text
Intel Corporation GeminiLake [UHD Graphics 600]
```

This shows that my computer has Intel UHD Graphics 600 integrated graphics.

### Check for NVIDIA hardware

```bash
lspci | grep -i nvidia
```

No output was returned, which means Linux did not detect an NVIDIA device through this check.

### Check NVIDIA management utility

```bash
nvidia-smi
```

The command was not found.

This utility is commonly used to inspect NVIDIA GPU and driver information.

### Check PyTorch CUDA availability

```python
import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.device_count())
```

My results:

```text
PyTorch: 2.15.0+cu132
CUDA available: False
GPU count: 0
```

Interpretation:

My PyTorch installation was built with CUDA 13.2 support, but no CUDA-compatible NVIDIA GPU was detected by PyTorch.

## 6. GPU Diagnostic Program

I created:

`code/gpu_check.py`

The program uses Python's platform module and PyTorch to inspect system information, CUDA availability and CPU tensor operations.

Important operations include:

- `platform.system()`: Returns the operating system name.
- `platform.processor()`: Returns processor information when available.
- `torch.__version__`: Displays the installed PyTorch version.
- `torch.cuda.is_available()`: Checks whether CUDA is available.
- `torch.cuda.device_count()`: Returns the number of available CUDA devices.
- `torch.cuda.get_device_name(0)`: Gets the name of the first CUDA GPU when one is available.
- `torch.tensor()`: Creates a tensor.
- `result.device`: Identifies the device performing the computation.

## 7. CPU-Based Tensor Operations

Even without an NVIDIA GPU, PyTorch can perform tensor calculations using the CPU.

Example:

```python
import torch

numbers = torch.tensor([1, 2, 3, 4, 5])

result = numbers * 2

print(result)
print(result.device)
```

Expected output:

```text
tensor([ 2,  4,  6,  8, 10])
cpu
```

This demonstrates that GPU availability is not a requirement for learning PyTorch or performing every machine learning operation.

## 8. Cloud GPU Computing

Cloud GPU computing allows developers to access remote computers equipped with powerful GPUs through the internet.

It is useful when:
- A local computer does not have a suitable GPU.
- A machine learning model requires more GPU memory.
- Training takes too long on a CPU.
- Developers need access to scalable computing resources.

Cloud GPU computing will be explored in the practical continuation of this lesson.

## 9. Key Lessons

1. CPUs and GPUs are processors designed for different computing workloads.
2. GPUs accelerate many AI workloads through parallel processing.
3. CUDA is NVIDIA's platform for GPU computing.
4. VRAM stores data required by GPU workloads.
5. PyTorch can perform calculations using the CPU.
6. CUDA-enabled PyTorch does not guarantee CUDA availability.
7. Cloud computing provides access to remote GPU resources.

## Conclusion

Understanding hardware is an important part of AI engineering.

Before training or deploying machine learning models, developers need to understand the available computing resources and choose suitable hardware for their workloads.