import textstat

def calculate_reward(original, rewritten, feedback_score):
    print("[RL Reward] Calculating reward...")

    if not original.strip():
        print("⚠️ Original text is empty. Returning reward 0.0")
        return 0.0

    try:
        novelty = len(set(rewritten.split()) - set(original.split())) / len(original.split())
    except ZeroDivisionError:
        novelty = 0.0

    try:
        readability = textstat.flesch_reading_ease(rewritten)
    except:
        readability = 0.0

    reward = 0.3 * novelty + 0.5 * (readability / 100) + 0.2 * feedback_score
    return reward
