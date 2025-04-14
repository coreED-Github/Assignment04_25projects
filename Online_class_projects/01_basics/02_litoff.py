import time

def main():
    print("=== Welcome to the Space Launch Simulator ===\n")
    print("Countdown begins...\n")
    
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("\nLiftoff! *** The rocket has launched! ***")

if __name__ == '__main__':
    main()