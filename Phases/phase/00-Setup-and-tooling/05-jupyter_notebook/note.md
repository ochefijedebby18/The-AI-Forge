# Phase 00: Setup & Tooling
## Lesson 05: Jupyter Notebooks

### 1. What is a Jupyter Notebook?

A Jupyter Notebook is an interactive programming environment that allows developers to execute code in individual cells, display results inline, visualize data, and combine executable code with documentation.

The notebook file format is `.ipynb`.

Notebooks are commonly used in data science, machine learning, AI research, experimentation, and education.

### 2. Notebook Cells

There are two primary types of cells:

**Code cells**
- Contain executable Python code.
- Can create variables, import libraries, perform calculations, train models, and generate outputs.

**Markdown cells**
- Contain documentation and explanations.
- Support headings, formatting, tables, and mathematical expressions.
- Help document experiments and explain code.

### 3. The Kernel

The kernel is a separate Python process that executes notebook cells and maintains variables and objects in memory.

All cells in a notebook normally share the same active kernel.

The kernel maintains state, which means variables created in one cell can be accessed in other cells.

### 4. Execution Order

Jupyter cells can be executed in an order different from their physical position in the notebook.

This can cause inconsistent results because variables may contain old values from previous executions.

Execution counters indicate the order in which cells were executed, not their physical position.

**Reliable practice:**
Kernel → Restart and Run All.

This clears the previous state and executes the notebook sequentially.

### 5. Notebook Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| Shift + Enter | Run cell and move to next |
| A | Insert cell above |
| B | Insert cell below |
| DD | Delete cell |
| M | Convert to Markdown |
| Y | Convert to Code |
| Z | Undo cell operation |
| Enter | Enter edit mode |
| Esc | Enter command mode |
| Tab | Autocomplete |
| Shift + Tab | Show function information |
| Ctrl + / | Toggle comment |

### 6. Magic Commands

Magic commands are special IPython/Jupyter commands. They are not standard Python syntax.

**`%timeit`**
Runs an operation repeatedly and estimates its execution time. Useful for comparing small operations and benchmarking code.

**`%%time`**
Measures the execution time of an entire cell, executing it once.

**`%matplotlib inline`**
Enables inline plotting in supported notebook environments.

**`!`**
Executes shell commands from a notebook cell.

**`%env`**
Displays or sets environment variables.

### 7. Rich Output

Jupyter can display:

- DataFrames as formatted tables.
- Matplotlib graphs.
- Images.
- HTML output.
- Mathematical expressions.
- Other rich representations supported by libraries.

This makes notebooks effective for exploring data and communicating experiment results.

### 8. Google Colab

Google Colab is a cloud-based notebook environment.

Advantages:
- Minimal local setup.
- Access to cloud computing resources.
- GPU availability on eligible sessions.
- Common ML libraries may already be installed.
- Google Drive integration.
- Easy sharing.

Limitations:
- Runtime sessions can terminate.
- Temporary runtime files may not persist.
- GPU availability and resources can be limited.
- Files should be saved to persistent storage when needed.

### 9. Notebooks vs. Scripts

Use notebooks for:
- Exploring datasets.
- Prototyping models.
- Visualization.
- Experimentation.
- Learning.
- Testing ideas.

Use Python scripts for:
- Reusable functions.
- Training pipelines.
- Production code.
- Applications.
- Backend services.
- Automation.
- Scheduled processes.

### 10. The AI Engineering Workflow

1. Explore data in a notebook.
2. Investigate and visualize patterns.
3. Prototype a model.
4. Test ideas and compare results.
5. Move reliable code into Python files.
6. Organize reusable functionality.
7. Integrate the code into an application or production system.

**Principle: Explore in notebooks, ship in scripts.**

### 11. Common Notebook Traps

**Out-of-order execution**
Cells executed in the wrong order may depend on stale variables or previous executions.

Solution: Restart and Run All.

**Hidden state**
Variables may still exist in kernel memory after the cells that created them have been deleted.

Solution: Restart the kernel and verify the notebook from top to bottom.

**Memory accumulation**
Large datasets, trained models, and intermediate objects can consume significant RAM.

Solutions:
- Delete unused objects using `del`.
- Use `gc.collect()` when appropriate.
- Restart the kernel when necessary.

### 12. Important Terms

**Kernel:** A separate Python process that executes notebook code and maintains variables in memory.

**Cell:** An independently executable notebook unit containing code or Markdown.

**Magic command:** A special Jupyter/IPython command prefixed with `%` or `%%`.

**State:** The current information held by a running program, including variables and objects.

**`.ipynb`:** The notebook file format, storing notebook cells, outputs, and metadata.

**Benchmarking:** Measuring the performance of code, often in terms of execution time or resource usage.

### 13. Core Lessons

- A notebook is an interactive environment, not simply a Python file.
- Cells can be executed independently.
- The kernel maintains state between executions.
- Execution order can create hidden bugs.
- Notebooks combine code, explanations, data, and visualizations.
- Restarting and running all cells is an important reliability check.
- Large objects can consume memory.
- Notebooks are excellent for experimentation.
- Scripts are better for reusable and production code.

### Final Principle

**Explore in notebooks. Build reliable code in scripts. Deploy your systems as applications.**

