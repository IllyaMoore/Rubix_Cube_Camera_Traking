from src import detect, webcam

def main():
    print("Select mode:")
    print("1 - Detect on image")
    print("2 - Detect on webcam")

    choice = input("Enter choice: ")

    if choice == "1":
        detect.run("")
    elif choice == "2":
        webcam.run()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
