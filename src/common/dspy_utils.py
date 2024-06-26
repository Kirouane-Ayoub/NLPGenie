import dspy


class QuestionAnswer(dspy.Signature):
    """Answer questions based on the input question."""

    question = dspy.InputField()
    answer = dspy.OutputField()


class ClassifyEmotion(dspy.Signature):
    """Classify emotion based on the input sentence
    and provide the sentiment as the output."""

    sentence = dspy.InputField()
    sentiment = dspy.OutputField(
        desc="generate reponse as positive, negative or neutral"
    )


class SummarizeText(dspy.Signature):
    """Summarize a given text into a succinct summary, in no more
    than a combination of 10 or 15 simple, compound, complex, and
    compound-complex complete sentences. Don't truncate the text.
    """

    text = dspy.InputField()
    summary = dspy.OutputField()


class SummarizeTextAndExtractKeyTheme(dspy.Signature):
    """Summarize a given text succinctly, in no more
    than a combination of six simple, compound, complex, and
    compound-complex sentences. Extract the key themes
    from the text, label it as 'Key Subjects:', and
    enumerate 'Takeaways:'.
    """

    text = dspy.InputField()
    summary = dspy.OutputField()
    key_themes = dspy.OutputField()
    takeaways = dspy.OutputField()


class TranslateText(dspy.Signature):
    """Given text indentify the language, translate into
    Spanish, French, German, Portugese, Japense, Korean,
    and Mandarin."""

    text = dspy.InputField()
    language = dspy.OutputField()
    translated_text = dspy.OutputField()


class TranslateTextToLanguage(dspy.Signature):
    """Given text, indentify the language and translate into
    English language."""

    text = dspy.InputField()
    language = dspy.OutputField()
    translated_text = dspy.OutputField()


class TextCompletion(dspy.Signature):
    """Complete a given text with more words to the best
    of your acquired knowledge. Don't truncate the generated
    response.
    """

    in_text = dspy.InputField()
    out_text = dspy.OutputField()


class TextTransformationAndCorrection(dspy.Signature):
    """Transform the given text on Pirate speak to a standard english text.
    Correct any grammatical errors. Provide the corrected
    text as the output.
    """

    text = dspy.InputField()
    corrected_text = dspy.OutputField()


class ZeroShotEntityNameRecognition(dspy.Signature):
    """Given a text, identify the named entities in the text.
    Output the named entities as persons,organizations,
    and locations.
    """

    text = dspy.InputField()
    entities = dspy.OutputField()


class TextCategorizationAndSentimentAnalsysis(dspy.Signature):
    """Categorize the given text into one of the following categories:
    Technical support, Billing, Account Management, New Customer or General inquiry.
    If you can't classify the text, default to 'General inquiry.'
    If customer text contatins a foul language, then respond with
    'No need for foul language. Please be respectful."
    Also provide the sentiment of the text as the output as positive, negative or neutral.
    """

    text = dspy.InputField()
    category = dspy.OutputField()
    sentiment = dspy.OutputField()
