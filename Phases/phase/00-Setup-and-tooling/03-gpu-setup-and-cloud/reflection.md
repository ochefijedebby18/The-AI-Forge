# Phase 00 — Lesson 03: GPU Setup & Cloud

## 1. What I Learned

This lesson introduced me to GPU computing and its importance in Artificial Intelligence.

I learned that GPUs are useful in AI because they can execute many mathematical operations in parallel.

I also learned the difference between CPUs and GPUs, how CUDA works, and why VRAM is important when running machine learning models.

## 2. What I Discovered About My Computer

I investigated my computer's graphics hardware using Linux terminal commands.

My computer uses Intel GeminiLake UHD Graphics 600 integrated graphics.

The NVIDIA hardware check returned no results, and PyTorch reported:

- PyTorch version: 2.15.0+cu132
- CUDA availability: False
- CUDA GPU count: 0

This helped me understand why my computer cannot currently use NVIDIA CUDA acceleration.

I also discovered that having a CUDA-enabled PyTorch installation does not mean that compatible GPU hardware is available.

## 3. What I Practised

I used Linux commands to investigate my computer's hardware:

- `lspci`
- `nvidia-smi`

I also used PyTorch to check CUDA availability and the number of available CUDA devices.

Finally, I created a Python GPU diagnostic program called `gpu_check.py`.

The program checks system information, PyTorch configuration, CUDA availability and CPU tensor operations.

## 4. What I Understand Better Now

The most important thing I learned is that AI engineering is not only about writing algorithms or training models.

It also involves understanding the hardware and computing resources required to execute those models.

I now understand that:
- CPUs can perform machine learning computations.
- GPUs can accelerate many computationally intensive AI workloads.
- CUDA is associated with NVIDIA GPU computing.
- VRAM is important when loading and training large models.
- Cloud GPUs can provide computing power beyond what a local computer offers.

## 5. Challenges I Encountered

My biggest discovery was that my computer does not have a detected NVIDIA GPU.

Initially, I needed to understand why PyTorch reported CUDA as unavailable even though my installed PyTorch package included CUDA support.

I now understand that software support and physical hardware availability are different things.

## 6. Connection to My AI Engineering Goals

My long-term goal is to develop and deploy useful AI applications, particularly in healthcare.

Healthcare AI applications may involve image processing, patient data analysis, deep learning and other computationally demanding workloads.

Understanding GPUs and cloud computing will help me make better decisions about where and how to train and deploy these models.

## 7. Areas I Still Need to Explore

I want to gain practical experience with:

- Cloud GPU environments.
- GPU memory management.
- CUDA and GPU acceleration.
- Training machine learning models using GPUs.
- Comparing CPU and GPU performance.
- Selecting suitable computing resources for AI applications.

## 8. Final Reflection

This lesson helped me understand the relationship between AI software and computer hardware.

I discovered the limitations of my local hardware, but I also learned that those limitations do not prevent me from learning AI engineering.

I can continue developing and testing machine learning applications using my CPU and eventually use cloud GPU resources for more demanding workloads.

**Lesson status:** Local GPU investigation and diagnostic program completed. Cloud GPU practical pending.