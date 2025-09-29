from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    """Translate English text to Hindi using Helsinki-NLP model."""
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

    def translate(self, text: str) -> str:
        if not text.strip():
            return text

        # Split text into smaller chunks to avoid token limit
        chunk_size = 300
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        translated_chunks = []

        for chunk in chunks:
            inputs = self.tokenizer(chunk, return_tensors="pt", truncation=True, padding=True)
            outputs = self.model.generate(**inputs, max_length=chunk_size*2)
            translated_chunks.append(self.tokenizer.decode(outputs[0], skip_special_tokens=True))

        return " ".join(translated_chunks)


# translator = Translator()
# print(translator.translate("Your innate leadership and warmth will shine today. Embrace spontaneity and avoid overthinking."))
