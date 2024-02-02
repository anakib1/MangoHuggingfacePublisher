import pathlib
from git import Repo

if not pathlib.Path('./MangoDemo').exists():
    Repo.clone_from('https://github.com/anakib1/MangoDemo', './MangoDemo')

from MangoDemo.mango.gradio import gradio_interface

if __name__ == '__main__':
    gradio_interface.launch()
