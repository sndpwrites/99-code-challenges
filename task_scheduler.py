import schedule
import time


def task(task_name):
    print("Running task:", task_name)


def schedule_task():
    task_name = input("Enter the task name: ")
    scheduled_time = input("Enter the scheduled time (in HH:MM format): ")

    # Split the scheduled time into hours and minutes
    scheduled_hour, scheduled_minute = scheduled_time.split(':')

    # Schedule the task at the specified time
    schedule.every().day.at(scheduled_time).do(task, task_name=task_name)

    print("Task scheduled successfully!")


def cancel_task():
    task_name = input("Enter the task name to cancel: ")

    # Remove the task from the schedule
    schedule.clear(tag=task_name)

    print("Task canceled successfully!")


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
