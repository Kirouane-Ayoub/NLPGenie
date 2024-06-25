import argparse

from common.common_task import (
    categorizer,
    emotion_classification,
    generate,
    ner_zero_shot,
    text_corrector,
    text_summarizer,
    text_summarizer_with_key_theme_extract,
    translate_into_english,
    translator,
)


def main():
    parser = argparse.ArgumentParser(
        description="Run various NLP tasks using dspy.Predict."
    )
    parser.add_argument(
        "task",
        type=str,
        choices=[
            "generate",
            "text_summarizer",
            "text_summarizer_with_key_theme_extract",
            "emotion_classification",
            "categorizer",
            "translator",
            "translate_into_english",
            "text_corrector",
            "ner_zero_shot",
        ],
        help="The NLP task to perform.",
    )
    parser.add_argument("prompt", type=str, help="The prompt or text to process.")

    args = parser.parse_args()

    task_function_mapping = {
        "generate": generate,
        "text_summarizer": text_summarizer,
        "text_summarizer_with_key_theme_extract": text_summarizer_with_key_theme_extract,
        "emotion_classification": emotion_classification,
        "categorizer": categorizer,
        "translator": translator,
        "translate_into_english": translate_into_english,
        "text_corrector": text_corrector,
        "ner_zero_shot": ner_zero_shot,
    }

    task_function = task_function_mapping[args.task]
    result = task_function(args.prompt)
    print(result)


if __name__ == "__main__":
    main()
