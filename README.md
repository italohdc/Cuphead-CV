# Cuphead CV

> This project was originally created and developed in May 2022.

Currently, this project features a **computer vision** program that captures the Cuphead game window in real-time
and detects objects in the game.

![GIF of the model detecting objects in Cuphead](/assets/demo.gif)

For that purpose, I **fine-tuned the YOLOv5 model** to detect objects from the game. I created a dataset with images of the game
and annotated them using [labelImg](https://github.com/HumanSignal/labelImg).

The program uses `win32gui` to
record the game window. The code to record the game window was based on the following YouTube playlist: [OpenCV Object Detection in Games](https://youtube.com/playlist?list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&si=b61Np6aIG-HEVaFh).


## Model in Action

Here are some videos showing the computer vision model in action.

- Model detecting objects in a pre-recorded video: [YouTube](https://www.youtube.com/watch?v=3Q1Q1Q1Q1Q1)
- Model detecting objects in real-time: [YouTube](https://youtu.be/cdgi73MJAAU)


## Jupyter Notebooks

These Jupyter Notebooks contain details of how the project was
developed and explain how the Python code inside `/src` works.

- [**notebook.ipynb**](notebook.ipynb): info about how the project was developed and how to use some tools.

- [**yolo_training.ipynb**](yolo_training.ipynb): quick tutorial on how to train your own dataset for YOLOv5.


## Dataset and Model

Link to the dataset and the model used in this project:
[Dropbox](https://www.dropbox.com/scl/fo/wlfsiugr4xq0o515u3erg/AOrz403txT0kwlf0yHCguXc?rlkey=j63nkh8skhthr9rfnl7kmj78t&st=pu30wb6u&dl=0)


## Next Steps

- [x] Create an adapter to send keystrokes to the game.

An adapter was created to automate sending keystrokes to the game. It was developed using the PyAutoGUI library.
That adapter can be used to control the game using an automated algorithm.

- [ ] Train a Machine Learning algorithm to play the game.

A next step is to train a Machine Learning algorithm to play the game. Maybe a good path would be to use a Reinforcement Learning
algorithm (Deep Q-Learning) to train an agent to play the game.
