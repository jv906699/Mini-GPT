class PlannerAgent:
    def decide(self, user_input):
        user_input = user_input.lower()

        if "code" in user_input or "python" in user_input:
            return "coding_agent"

        elif "summarize" in user_input:
            return "summarization_agent"

        elif "plan" in user_input or "trip" in user_input:
            return "planning_agent"

        else:
            return "general_agent"