with open("student.txt", "r") as student:
    lines = student.read();
    print(lines)

with open("skills.txt", "w") as file:
    file.write("Python\nGit\nSQL\nMachine Learning\nGenerative AI\n")


skip = False;
while(skip != True): 
    new_skill = input("Enter a new skill:")
    if(new_skill):
        with open("skills.txt", "a") as file:
            file.write(f"{new_skill}\n")
    can_skip = input("Want to enter new skill again (Y/N):")
    if(can_skip and can_skip.lower() == "n"):
        skip = True

name = input("Name:")
topic = input("Topic:")
with open("learning_log.txt", "w") as file:
    file.write(f"{name} - {topic}")