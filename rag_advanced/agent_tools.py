from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatZhipuAI
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 读取 API Key
api_key = os.getenv("ZHIPUAI_API_KEY")

def calculate_growth(current, previous):
    growth = ((current - previous) / previous) * 100
    return f"同比增长率为 {growth:.2f}%"

def build_agent():
    llm = ChatZhipuAI(model="glm-4.5", temperature=0, api_key=api_key)

    tools = [
        Tool(
            name="Calculator",
            func=lambda q: eval(q),
            description="用于执行数学计算"
        ),
        Tool(
            name="GrowthCalculator",
            func=lambda q: calculate_growth(*map(float, q.split(","))),
            description="输入格式：current,previous，输出同比增长率"
        )
    ]

    agent = initialize_agent(
        tools, llm, agent="zero-shot-react-description", verbose=True,  handle_parsing_errors=True
    )
    return agent

if __name__ == "__main__":
    agent = build_agent()
    print(agent.run("帮我算净利润同比增长率，假设本期 250 ，上期 200"))
