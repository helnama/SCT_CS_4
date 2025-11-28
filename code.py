# safe_input_logger.py
# Educational input logger (not system-wide keylogger)

def log_input():
    log_file = "input_log.txt"
    print("Type something (type 'exit' to quit):")

    with open(log_file, "a") as f:
        while True:
            user_input = input("> ")
            if user_input.lower() == "exit":
                print("Exiting logger...")
                break
            f.write(user_input + "\n")
            print(f"Logged: {user_input}")

if __name__ == "__main__":
    log_input()
