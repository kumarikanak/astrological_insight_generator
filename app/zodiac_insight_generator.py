import re
import os
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
from app.translator import Translator

class LLMClient:
    def __init__(self, model_name=None, prompt_path="data/prompts/daily_prompt.txt"):
        # Load text-generation model
        self.model_name = model_name or os.getenv("LLM_MODEL", "stevhliu/astroGPT")
        self.pipe = pipeline("text-generation", model=self.model_name)

        # Load prompt template
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.prompt_template = f.read()

        # Hindi translation model
        self.translator = Translator()

    def generate(
        self, sign: str, base_rule: str, context: str = "", language: str = "en", max_tokens: int = 100
    ) -> str:
        """
        Generate horoscope text using LLM with vector-context.
        :param sign: Zodiac sign
        :param base_rule: Personality / daily rule
        :param context: Retrieved vector context from templates
        :param language: "en" or "hi"
        :param max_tokens: Max tokens to generate
        :return: Horoscope text
        """
        # Fill prompt dynamically
        prompt = self.prompt_template.format(sign=sign, base_rule=base_rule, context=context)

        response = self.pipe(
            prompt,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )

        text = response[0]["generated_text"]

        # Remove prompt from output
        if prompt in text:
            text = text.replace(prompt, "").strip()

        # Remove date-like patterns
        text = re.sub(
            r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{1,2},\s\d{4}\b",
            "",
            text,
        )

        # Keep 2–3 sentences
        sentences = [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]
        truncated = ". ".join(sentences[:3])
        if truncated and not truncated.endswith("."):
            truncated += "."

        # Remove repeated phrases
        truncated = re.sub(r"(\b\w+\b)(\s+\1)+", r"\1", truncated)

        # Translate to Hindi if requested
        if language.lower() == "hi":
            truncated = self.translator.translate(truncated)

        return truncated
