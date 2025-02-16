from agent.agent_setup import create_agent_executor

def main():
    agent = create_agent_executor()
    
    # # Example input
    # user_input = "Sector of tech and AI. Nvidia, Meta, Amazon"
    
    # print(f"User Input: {user_input}")
    # result = agent.invoke({"input": user_input})
    
    # print("\n" + "="*50 + "\nAnalysis Report:")
    # print(result['output'])
    print("\n" + "="*50)
    user_input = input("Enter sector/companies to analyze (e.g., 'Tech sector: Apple, Google'):\n> ")
    # Validate input
    while not user_input.strip():
        print("\n[ERROR] Input cannot be empty!")
        user_input = input("Please enter your analysis request:\n> ")
    
    # Process request
    print("\n" + "="*50 + "\nProcessing request...")
    try:
        result = agent.invoke({"input": user_input})
        print("\n" + "="*50 + "\nANALYSIS REPORT:")
        print(result['output'])
        print("\n" + "="*50)
    except Exception as e:
        print(f"\n[ERROR] Analysis failed: {str(e)}")
if __name__ == "__main__":
    main()