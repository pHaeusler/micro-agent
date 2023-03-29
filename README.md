# Micro Agent

A tiny implementation of an autonomous agent powered by LLMs (OpenAI GPT-4)

What is this?

- A bare-bones AI software engineer (for Python for now...)
- A step towards AGI
- A research tool to experiment with agent development

What can it do?

- It writes software for you
- Give it a "purpose" and let it go!

Inspired by [langchain](https://github.com/hwchase17/langchain) and [micrograd](https://github.com/karpathy/micrograd)

## How to use?

Set your `OPENAI_API_KEY` environment variable

Edit `run.py` to set your `purpose` and the `directory` of the target application

The `directory` should have a `requirements.txt` file and an `__init__.py`

Let it run free! `python run.py`

![purpose](./assets/purpose.jpg "Purpose")
