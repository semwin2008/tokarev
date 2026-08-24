from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path

MAX_NEW_TOKENS = 30
TEMPERATURE = 0.7


def get_model_reply(text):
    """
        returns a LM reply to the input text as a new message
    """
    if len(text) > 30 * 4:
        return "Ты чо охренел ???"

    model_name = "qwen_merged"
    model_path = Path(__file__).parent / "merged" / model_name

    model = AutoModelForCausalLM.from_pretrained(str(model_path.resolve()), device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(str(model_path.resolve()))

    # Генерация
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(
                **inputs,
                max_new_tokens=MAX_NEW_TOKENS,
                do_sample=True,
                temperature=TEMPERATURE,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
