import dspy
from common.dspy_utils import (
    ClassifyEmotion,
    SummarizeText,
    SummarizeTextAndExtractKeyTheme,
    TextCategorizationAndSentimentAnalsysis,
    TextCompletion,
    TextTransformationAndCorrection,
    TranslateText,
    TranslateTextToLanguage,
    ZeroShotEntityNameRecognition,
)
from utils.models import llm

dspy.settings.configure(lm=llm)


def generate(prompt):
    complete = dspy.Predict(TextCompletion)
    result = complete(in_text=prompt)
    return result.out_text


def text_summarizer(prompt):
    summarize = dspy.Predict(SummarizeText)
    response = summarize(text=prompt)
    return response.summary


def text_summarizer_with_key_theme_extract(prompt):
    summarize_theme = dspy.Predict(SummarizeTextAndExtractKeyTheme)
    response = summarize_theme(text=prompt)
    response.key_themes = response.key_themes.split("\n")
    final_res = f"{response.summary} \n\n{response.key_themes}\n\n{response.takeaways}"
    return final_res


def emotion_classification(propmt):
    classify = dspy.Predict(ClassifyEmotion)
    response = classify(sentence=propmt)
    return response.sentiment


def categorizer(prompt):
    categorize = dspy.Predict(TextCategorizationAndSentimentAnalsysis)
    response = categorize(text=prompt)
    final_res = f"{response.category} \n\n {response.sentiment}"
    return final_res


def translator(prompt):
    translate = dspy.Predict(TranslateText)
    response = translate(text=prompt)
    final_res = f"{response.language} \n\n {response.translated_text}"
    return final_res


def translate_into_english(prompt):
    translate = dspy.Predict(TranslateTextToLanguage)
    response = translate(text=prompt)
    final_res = f"{response.language} \n\n {response.translated_text}"
    return final_res


def text_corrector(prompt):
    correct = dspy.Predict(TextTransformationAndCorrection)
    response = correct(text=prompt)
    return response.corrected_text


def ner_zero_shot(prompt):
    zero = dspy.Predict(ZeroShotEntityNameRecognition, max_iters=5)
    result = zero(text=prompt)
    return result.entities
