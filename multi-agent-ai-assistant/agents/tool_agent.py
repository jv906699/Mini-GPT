class ToolAgent:
    def use_tool(self, agent_type, user_input):

        if agent_type == "coding_agent":
            return f"Generated Python code for: {user_input}"

        elif agent_type == "summarization_agent":
            return f"Summarized text: {user_input[:50]}..."

        elif agent_type == "planning_agent":
            return f"Step-by-step plan created for: {user_input}"

        else:
            return f"Answering general query: {user_input}"`