# NLPGenie

```
  _   _ _     ____   ____            _      
 | \ | | |   |  _ \ / ___| ___ _ __ (_) ___ 
 |  \| | |   | |_) | |  _ / _ \ '_ \| |/ _ \
 | |\  | |___|  __/| |_| |  __/ | | | |  __/
 |_| \_|_____|_|    \____|\___|_| |_|_|\___|

                DSPY based
```
![1707471817175](https://github.com/Kirouane-Ayoub/NLPGenie/assets/99510125/393577f4-18bd-4d85-994c-befc31a6826a)

## Overview

**NLPGenie** is a Python project designed to simplify the execution of various Natural Language Processing (NLP) tasks using the DSPy framework. DSPy provides a powerful and flexible way to interact with large language models (LLMs) for text generation, summarization, translation, and more. NLPGenie leverages DSPy to perform these tasks with minimal configuration, making it accessible for developers and researchers.

## Installation

To install NLPGenie, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Kirouane-Ayoub/NLPGenie.git
   cd NLPGenie
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

You can use NLPGenie to perform various NLP tasks by running the `main.py` script with the appropriate arguments.

### Command-Line Interface

The `main.py` script uses `argparse` to parse command-line arguments. Here is the basic usage:

```sh
python src/main.py <task> <prompt>
```

### Available Tasks

- **generate**: Generate text based on a prompt.
- **text_summarizer**: Summarize a given text.
- **text_summarizer_with_key_theme_extract**: Summarize a text and extract key themes.
- **emotion_classification**: Classify the emotion of a given text.
- **categorizer**: Categorize text and analyze its sentiment.
- **translator**: Translate text to another language.
- **translate_into_english**: Translate text into English.
- **text_corrector**: Correct grammatical errors in a text.
- **ner_zero_shot**: Perform zero-shot entity name recognition.

### Examples

1. **Generate Text**:
   ```sh
   python src/main.py generate "Once upon a time"
   ```

2. **Summarize Text**:
   ```sh
   python src/main.py text_summarizer "This is a long text that needs summarizing..."
   ```

3. **Classify Emotion**:
   ```sh
   python src/main.py emotion_classification "I am so happy today!"
   ```

## Development

### Adding New Tasks

To add new tasks or modify existing ones, you can edit the corresponding functions in `common_task.py` and their signatures in `dspy_utils.py`. Ensure to update the `main.py` to include any new task functions you create.

---
