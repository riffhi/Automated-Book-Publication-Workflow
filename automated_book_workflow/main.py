# main.py
import os
from scraper.main import scrape_chapter
from ai_agents.writer import ai_writer
from ai_agents.reviewer import ai_reviewer
from rl_reward.reward import calculate_reward
from versioning.chroma_versioning import save_version
from voice_support.voice import voice_prompt, voice_output
from utils.helpers import read_text_file

def run_pipeline(url):
    print("\n[1] Scraping content...")
    raw_text_path = scrape_chapter(url)

    print("\n[2] AI Writing...")
    original_text = read_text_file(raw_text_path)
    print(f"Original text length: {len(original_text.strip().split())} words")
    rewritten_text = ai_writer(original_text)

    print("\n[3] AI Reviewing...")
    reviewed_text = ai_reviewer(rewritten_text)

    print("\n[4] Asking for human feedback...")
    voice_output("Do you accept the rewritten chapter? Say Yes or No.")
    user_response = voice_prompt()
    feedback_score = 1 if "yes" in user_response.lower() else 0

    print("\n[5] RL-based reward calculation...")
    if len(original_text.strip().split()) < 20:
        print("⚠️ Skipping reward calc due to insufficient original text.")
        reward = 0.0
    else:
        reward = calculate_reward(original_text, reviewed_text, feedback_score)
    print(f"Reward Score: {reward:.2f}")

    print("\n[6] Saving version to ChromaDB...")
    save_version(reviewed_text, {"url": url, "reward": reward})
    print("✅ Workflow completed successfully!")

if __name__ == "__main__":
    chapter_url = input("🔗 Enter the URL of the chapter to process: ")
    run_pipeline(chapter_url)
