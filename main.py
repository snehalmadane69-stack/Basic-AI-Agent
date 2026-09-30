from agent import run_agent

print("===== Basic AI Agent =====")

question = input("Ask your question or describe your situation: ")

answer = run_agent(question)

print("\nAI Agent Response:")
print(answer)