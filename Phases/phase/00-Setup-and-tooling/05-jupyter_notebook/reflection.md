# Lesson Reflection — Jupyter Notebooks

In this lesson, I learned about Jupyter Notebooks and why they are important in AI engineering, machine learning, and data science.

I understood that a Jupyter Notebook is an interactive environment where I can execute code in separate cells, observe outputs immediately, and combine Python code with explanations, mathematical expressions, tables, and visualizations. Unlike a traditional Python script, I do not always need to execute the entire program to test an individual part of my experiment.

One of the most important concepts was the kernel. The kernel is responsible for executing my code and maintaining variables and objects in memory. This helped me understand why variables created in one cell can be accessed from another cell, even when I am not executing the cells in order.

Another important lesson was knowing when to use notebooks and when to use Python scripts. Notebooks are useful for experimentation, visualization, prototyping, and exploring data, while scripts are better for reusable functions, training pipelines, applications, automation, and production systems.

I also learned that this flexibility can create problems. Executing cells out of order can produce incorrect results because variables may contain outdated values. A notebook can appear to work while depending on execution history that is not visible from its current code. I now understand why restarting the kernel and running all cells from beginning to end is an important way to verify a notebook.

I learned about Jupyter magic commands, including `%timeit` for repeatedly measuring code performance and `%%time` for measuring the execution time of a cell. I also learned how notebooks can display graphs, tables, and images inline, which makes them particularly useful for exploring datasets and understanding machine-learning experiments.

I also learned about hidden state, out-of-order execution, and memory accumulation. These problems can make notebooks unreliable or consume excessive computer memory, especially when working with large datasets or machine-learning models.

Overall, this lesson helped me understand that Jupyter Notebooks are more than a place to write Python code. They are an experimental environment where I can investigate problems, test hypotheses, analyze results, and develop ideas before turning them into reliable software.

As I continue learning AI engineering, I want to use notebooks to understand the mathematics, experiment with data, test models, visualize results, and document what I learn, while developing the discipline to move reliable code into properly organized Python files.

My key takeaway is: **Explore in notebooks, ship in scripts.**
