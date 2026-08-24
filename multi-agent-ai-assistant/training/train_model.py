from agents.planner_agent import PlannerAgent
from agents.tool_agent import ToolAgent
from agents.response_agent import ResponseAgent


planner = PlannerAgent()
tool = ToolAgent()
responder = ResponseAgent()


def run_system(user_input):
    agent_type = planner.decide(user_input)
    tool_output = tool.use_tool(agent_type, user_input)
    final_response = responder.respond(tool_output)

    return final_response


# TEST
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        output = run_system(user_input)
        print(output)