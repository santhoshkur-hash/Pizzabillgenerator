import sys
from google import genai

# 1. Initialize the client
# Replace 'YOUR_ACTUAL_GEMINI_KEY' with the key you found in your Google AI Studio
client = genai.Client(api_key="YOUR_ACTUAL_GEMINI_KEY")

# 2. Choose the model
# gemini-2.5-flash is a fast, efficient model for these types of tasks
myModel = "gemini-2.5-flash"


def run_app():
    while True:
        print("\n--- Select an option from below ---")
        print("1. Email Generator")
        print("2. Text Summarizer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            topic = input("Enter the topic of the email: ")
            tone = input("Enter the tone (e.g., formal, friendly): ")

            # Generate content using Gemini
            response = client.models.generate_content(
                model=myModel,
                contents=f"Write a {tone} email about {topic}"
            )
            print("\n--- Generated Email ---")
            print(response.text)

        elif choice == "2":
            text = input("Enter the text you want to summarize: ")

            # Generate content using Gemini
            response = client.models.generate_content(
                model=myModel,
                contents=f"Summarize the following text in short bullet points: {text}"
            )
            print("\n--- Summary ---")
            print(response.text)

        elif choice == "3":
            print("Exiting the GenAI Project. Goodbye!")
            # sys.exit() is the professional way to stop a script
            sys.exit(0)

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    run_app()exit