import schedule
import time


def task(task_name):
    print("Task running:\t"+str(task_name))


def schedule_task():
    task_name = input("Enter the task name: ")
    scheduled_time = input("Enter the scheduled time (in HH:MM format): ")

    def task_wrapper():
        task(task_name)
    schedule.every().day.at(scheduled_time).do(task_wrapper)
    print("Task scheduled successfully!")


def cancel_task():
    task_name = input("Enter the task name to cancel: ")

    schedule.clear(tag=task_name)
    print("Task canceled successfully!")
    print_scheduled_tasks()


def print_scheduled_tasks():
    print("Scheduled tasks:")
    print(schedule.jobs)


# Run the scheduled tasks indefinitely
while True:
    print("\n1. Schedule a task")
    print("2. Cancel a task")
    print("3. Print scheduled tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        schedule_task()
    elif choice == '2':
        cancel_task()
    elif choice == '3':
        print_scheduled_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

    schedule.run_pending()
    time.sleep(1)
