def explain_topic(topic: str) -> str:
    """
    Tool 1: Explains any Data Engineering concept
    Input: topic name (string)
    Output: explanation (string)
    """
    return f"Explaining the topic: {topic}"

def find_resource(topic: str) -> str:
    """
    Tool 2: Finds learning resources for a topic
    Input: topic name (string)
    Output: resource suggestion (string)
    """
    return f"Finding best resources for: {topic}"

def plan_today(current_month: int, weak_areas: list) -> str:
    """
    Tool 3: Creates a study plan for today
    Input: current month number (int), weak areas (list)
    Output: study plan (string)
    """
    return f"Creating study plan for month {current_month}, weak areas: {weak_areas}"