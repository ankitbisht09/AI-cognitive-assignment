from utils import mock_news_lookup


def pick_topic_from_persona(persona_text: str):
    """
    Very rough heuristic (can be replaced by LLM later).
    Just trying to simulate 'decision making'.
    """

    text = persona_text.lower()

    if "ai" in text or "tech" in text:
        return "impact of AI on jobs"

    if "crypto" in text:
        return "crypto market movement"

    return "macro market trends"


def build_bot_opinion(bot_id: str, persona_text: str):
    """
    Simulates LangGraph flow:
    1. Decide topic
    2. Fetch context
    3. Generate opinionated post
    """

    topic = pick_topic_from_persona(persona_text)

    # pulling external context (mocked)
    context = mock_news_lookup(topic)

    # not over-engineering generation (keeping it simple + realistic)
    post_text = f"{persona_text[:60]} | reacting to: {context[0]}"

    return {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post_text[:280]  # respecting 280 char constraint
    }