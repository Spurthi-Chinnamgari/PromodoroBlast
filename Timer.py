import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up! \n")

def main():
    print(" Study Timer (Pomodoro)")
    work_minutes = int(input("Enter work duration in minutes: "))
    break_minutes = int(input("Enter break duration in minutes: "))
    cycles = int(input("Enter number of cycles: "))

    for i in range(cycles):
        print(f"\nCycle {i+1} - Work Time!")
        countdown(work_minutes)
        print(f"Cycle {i+1} - Break Time!")
        countdown(break_minutes)

    print("All cycles completed! Great job! ")

if __name__ == "__main__":
    main()
