from agent import run_agent

print("=" * 50)
print("DE Learning Agent")
print("Type 'exit' to quit")
print("=" * 50)

if __name__ == "__main__":
    while True:
        question = input("\nAsk me anything: ")
        
        if question.lower() == "exit":
            print("Goodbye! Keep learning. 🚀")
            break
            
        if question.strip() == "":
            print("Please type a question.")
            continue
            
        run_agent(question)