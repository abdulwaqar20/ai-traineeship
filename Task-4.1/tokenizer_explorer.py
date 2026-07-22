"""
Task 4.1 — Part B: Tokenization Hands-On
Explore how LLMs see text through tiktoken.
"""
import tiktoken
import os


def analyze_text(text, model="gpt-4"):
    """
    Tokenize text and show tokens, count, and character breakdown.
    """
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode(text)
    token_strings = [encoder.decode([t]) for t in tokens]
    
    print(f"\n{'='*60}")
    print(f"Text: \"{text}\"")
    print(f"{'='*60}")
    print(f"Word count: {len(text.split())}")
    print(f"Character count: {len(text)}")
    print(f"Token count: {len(tokens)}")
    print(f"Tokens per word: {len(tokens)/len(text.split()):.2f}")
    print(f"\nTokens: {token_strings}")
    
    # Show each token with its ID
    print(f"\nToken breakdown:")
    for i, (token_id, token_str) in enumerate(zip(tokens, token_strings)):
        print(f"  [{i}] ID {token_id}: '{token_str}'")
    
    return len(tokens)


def compare_languages():
    """
    Compare tokenization between English and a non-Latin script.
    """
    # Same meaning, different scripts
    english = "The weather is very nice today."
    urdu = "آج موسم بہت اچھا ہے۔"  # "The weather is very nice today."
    
    print("\n" + "="*60)
    print("LANGUAGE COMPARISON")
    print("="*60)
    
    en_tokens = analyze_text(english)
    ur_tokens = analyze_text(urdu)
    
    print(f"\n{'='*60}")
    print("COMPARISON SUMMARY")
    print(f"{'='*60}")
    print(f"English: {en_tokens} tokens for {len(english)} chars")
    print(f"Urdu:    {ur_tokens} tokens for {len(urdu)} chars")
    print(f"Ratio:   Urdu uses {ur_tokens/en_tokens:.1f}x more tokens")
    print(f"\n💡 Cost implication: Non-Latin scripts often cost more")
    print(f"   because each character maps to multiple tokens.")


def rare_word_demo():
    """
    Show how long/rare words split into many tokens.
    """
    words = [
        "hello",
        "antidisestablishmentarianism",
        "pneumonoultramicroscopicsilicovolcanoconiosis",
        "AI",
        "artificial intelligence"
    ]
    
    print("\n" + "="*60)
    print("RARE / LONG WORDS")
    print("="*60)
    
    for word in words:
        analyze_text(word)


def cost_calculation():
    """
    Calculate real API cost for a given text.
    """
    # Example pricing (OpenAI GPT-4o as of 2026 — update with current rates)
    INPUT_PRICE_PER_1K = 0.005   # $0.005 per 1K input tokens
    OUTPUT_PRICE_PER_1K = 0.015  # $0.015 per 1K output tokens
    
    # A 2,000-word article (approximate)
    sample_article = """
    Artificial intelligence has transformed nearly every industry in the past decade.
    From healthcare to finance, from education to entertainment, AI systems now
    assist humans in making decisions, creating content, and solving complex
    problems. Large language models like GPT-4, Claude, and Llama have demonstrated
    remarkable capabilities in understanding and generating human-like text. However,
    these systems also raise important questions about bias, privacy, and the future
    of work. As we continue to integrate AI into our daily lives, it becomes crucial
    to develop frameworks for responsible deployment. This includes transparency in
    how models are trained, accountability for their outputs, and ensuring that
    the benefits of AI are distributed equitably across society. The next decade
    will likely see even more profound changes as multimodal models and agentic
    systems become mainstream. Organizations that invest in AI literacy and ethical
    governance today will be better positioned to harness these technologies
    responsibly tomorrow.
    """.strip()
    
    encoder = tiktoken.encoding_for_model("gpt-4")
    tokens = encoder.encode(sample_article)
    token_count = len(tokens)
    word_count = len(sample_article.split())
    
    # Assume output is roughly same length as input (conservative estimate)
    input_cost = (token_count / 1000) * INPUT_PRICE_PER_1K
    output_cost = (token_count / 1000) * OUTPUT_PRICE_PER_1K
    total_cost = input_cost + output_cost
    
    print("\n" + "="*60)
    print("COST CALCULATION")
    print("="*60)
    print(f"Sample text: ~{word_count} words")
    print(f"Token count: {token_count}")
    print(f"Tokens per word: {token_count/word_count:.2f}")
    print(f"\nPricing (GPT-4o):")
    print(f"  Input:  ${INPUT_PRICE_PER_1K}/1K tokens")
    print(f"  Output: ${OUTPUT_PRICE_PER_1K}/1K tokens")
    print(f"\nCost for this request:")
    print(f"  Input:  ${input_cost:.4f}")
    print(f"  Output: ${output_cost:.4f}")
    print(f"  Total:  ${total_cost:.4f}")
    print(f"\n💡 At scale: 1,000 such requests/day = ${total_cost*1000:.2f}/day")
    print(f"   = ${total_cost*1000*30:.2f}/month")


def main():
    print("="*60)
    print("TOKENIZATION EXPLORER — Task 4.1 Part B")
    print("="*60)
    
    # 1. Simple English sentence
    print("\n" + "="*60)
    print("1. SIMPLE ENGLISH SENTENCE")
    print("="*60)
    analyze_text("AI is transforming software.")
    
    # 2. Rare/long words
    rare_word_demo()
    
    # 3. English vs. Urdu comparison
    compare_languages()
    
    # 4. Cost calculation
    cost_calculation()
    
    # 5. Interactive mode
    print("\n" + "="*60)
    print("INTERACTIVE MODE")
    print("="*60)
    print("Enter your own text to analyze (or 'quit' to exit):")
    
    while True:
        user_input = input("\n> ").strip()
        if user_input.lower() in ('quit', 'exit', 'q'):
            break
        if user_input:
            analyze_text(user_input)


if __name__ == "__main__":
    main()