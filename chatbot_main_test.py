def main():
    print("🧠 Mental Health Risk Analysis Chatbot 🤖")
    while True:
        query = input("Ask your question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        answer = ask_question(query)
        print(f"\nAnswer: {answer}\n")

if __name__ == "__main__":
    from chatbot_setup import ask_question
    main()
