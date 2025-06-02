# import crewai
# import crewai_tools

# print("Contents of crewai:")
# print(dir(crewai))
# print("\nContents of crewai_tools:")
# print(dir(crewai_tools))


import os

def print_directory_tree(start_path='.', indent=''):
    for item in sorted(os.listdir(start_path)):
        path = os.path.join(start_path, item)
        if os.path.isdir(path):
            print(f"{indent}📁 {item}/")
            print_directory_tree(path, indent + '    ')
        else:
            print(f"{indent}📄 {item}")

print("📦 Project Structure:\n")
print_directory_tree('.')
