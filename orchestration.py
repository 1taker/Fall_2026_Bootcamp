import subprocess

def run_command(command):
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

print("Welcome to the Day 5 Orchestration Program")
print("1) Show current directory")
print("2) Show current user")
print("3) List files")
choice = input("Enter your choice [1-3]: ")
if choice == "1":
    command = "pwd"
elif choice == "2":
    command = "whoami"
elif choice == "3":
    command = "ls"
else:
    command = None
    print("Invalid selection.")
if command:
    run_command(command)