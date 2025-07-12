def ai_writer(text):
    print("[AI Writer] Spinning the content...")
    # Placeholder logic; replace with Gemini/OpenAI API
    rewritten = text.replace("he", "the man").replace("she", "the woman")
    rewritten = "[Rewritten] " + rewritten[:3000]  # Truncate if too long
    return rewritten
