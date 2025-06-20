def main():
    questions = [
        "Do you regularly track your monthly income and expenses?",
        "Do you have a written budget?",
        "Do you have an emergency fund?",
        "Do you understand how interest rates affect loans?",
        "Do you save a portion of your income every month?",
        "Do you know your credit score or how it’s calculated?",
        "Have you ever created a financial goal (e.g. saving for a car)?",
        "Do you know the difference between needs and wants?",
        "Are you aware of how taxes affect your income?",
        "Do you know the basics of investing (e.g. stocks, bonds)?"
    ]

    score = 0
    for question in questions:
        score += ask_yes_no(question)
        
    give_suggestion(score)

def ask_yes_no(question):
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer == "yes":
            return 1
        elif answer == "no":
            return 0
        else:
            print("Please answer with yes or no!")

def give_suggestion(score):
    print(f"\nYour financial awareness score is: {score}/10\n")
    if score <= 3:
        print("🟥 You're just starting out, and that's perfectly okay! 💡")
        print("* Track where your money goes each month 🧾!")
        print("* Learn what a budget is and try creating one!")
        print("* Watch beginner videos on money habits!")
        print("👉 Start small and stay consistent. You're on the right path :)")
    
    elif score <= 6:
        print("🟧 You’ve got some knowledge, let’s build on that! 🌱")
        print("* Set a small financial goal this month (e.g. save 50 $, don't forget it doesn't have to a big amount :)")
        print("* Learn how interest and credit cards work!")
        print("* Try budgeting apps for visual insights!")
        print("👉 Keep exploring. One step at a time.")

    elif score <= 8:
        print("🟨 You're doing well and it actually shows! 🔍")
        print("* Start learning about investments (stocks, bonds)!")
        print("* Explore emergency funds and passive income ideas!")
        print("* Consider how taxes affect your income!")
        print("👉 Smart habits now = more freedom later! (Take it from someone who's been through it :)")

    else:
        print("🟩 Excellent! Your financial literacy is pretty impressive 💎")
        print("* Look into retirement plans, side hustles, index funds!")
        print("* Maybe start mentoring others or writing about finance!")
        print("👉 You're not just managing money, you're building wealth :)")

if __name__ == "__main__":
    main()