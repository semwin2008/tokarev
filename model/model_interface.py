from transformers import AutoModelForCausalLM, AutoTokenizer


def get_model_reply(text):
    """
        returns a LM reply to the input text as a new message
    """
    model = AutoModelForCausalLM.from_pretrained("./merged/qwen_merged", device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained("./merged/qwen_merged")

    # Генерация
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=50, do_sample=True, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)