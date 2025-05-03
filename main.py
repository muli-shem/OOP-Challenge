from pet import Pet

def main():
    buddy = Pet("Buddy")
    buddy.get_status()

    print("\n🦴 Feeding...")
    buddy.eat()
    buddy.get_status()

    print("\n😴 Sleeping...")
    buddy.sleep()
    buddy.get_status()

    print("\n🎾 Playing...")
    buddy.play()
    buddy.get_status()

    print("\n🎓 Training...")
    buddy.train("sit")
    buddy.train("roll over")
    buddy.train("sit")  # Trying duplicate

    print("\n📚 Tricks Known:")
    buddy.show_tricks()

if __name__ == "__main__":
    main()
