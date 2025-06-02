import os


def select_directory(base_path: str, exclude: list[str] = [], depth=0) -> str:
    """
    Recursively let the user select a directory to add a file/subdir to.
    At top level, only allow selecting a directory to enter.
    At 2nd level or deeper, allow creating a subdirectory or selecting the current directory.
    """
    while True:
        dirs = [
            d
            for d in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, d)) and d not in exclude
        ]
        print(f"\nCurrent directory: {base_path}")
        if dirs:
            print("Select a directory:")
            for idx, d in enumerate(dirs):
                print(f"  {idx + 1}. {d}")

        # At depth >= 1 (not top level), allow creating/selecting
        options = len(dirs)
        if depth >= 1:
            print(f"  {options + 1}. Create new subdirectory here")
            options += 1
            # print(f"  {options + 1}. Select this directory")
            # options += 1
        elif not dirs:
            print("No subdirectories. You must create a new subdirectory here.")
            print(f"  1. Create new subdirectory here")
            options = 1

        choice = input("Enter choice number: ").strip()
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if dirs and 1 <= choice <= len(dirs):
            base_path = os.path.join(base_path, dirs[choice - 1])
            depth += 1
        elif (depth >= 1 and choice == len(dirs) + 1) or (not dirs and choice == 1):
            new_dir = input("Enter new subdirectory name: ").strip()
            new_dir_path = os.path.join(base_path, new_dir)
            os.makedirs(new_dir_path, exist_ok=True)
            # Ensure __init__.py
            init_path = os.path.join(new_dir_path, "__init__.py")
            open(init_path, "a").close()
            print(f"Created {new_dir_path} and __init__.py")
            return new_dir_path
        # elif depth >= 1 and choice == len(dirs) + 2:
        #    return base_path
        else:
            print("Invalid choice. Try again.")


def create_python_file(directory: str) -> str:
    file_name = input("Enter new Python file name (without .py): ").strip() + ".py"
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# Your code here\n")
        print(f"Created {file_path}")
    else:
        print(f"{file_path} already exists.")
    return file_path


def mirror_in_tests(src_path: str, file_name: str) -> None:
    # src_path is absolute, file_name is just the filename
    project_root = os.getcwd()
    test_root = os.path.join(project_root, "tests")
    rel_path = os.path.relpath(src_path, project_root)
    test_dir = os.path.join(test_root, rel_path)
    os.makedirs(test_dir, exist_ok=True)
    # Ensure __init__.py in all new dirs under tests/
    test_dir_parts = os.path.relpath(test_dir, test_root).split(os.sep)
    for i in range(len(test_dir_parts) + 1):
        d = os.path.join(test_root, *test_dir_parts[:i])
        if d and not os.path.exists(os.path.join(d, "__init__.py")):
            open(os.path.join(d, "__init__.py"), "a").close()
    # Create test file
    test_file_name = "test_" + file_name
    test_file_path = os.path.join(test_dir, test_file_name)
    if not os.path.exists(test_file_path):
        with open(test_file_path, "w") as f:
            f.write(f"# Test for {file_name}\n")
            f.write("import unittest\n\n")
            f.write("class TestCase(unittest.TestCase):\n")
            f.write("    def test_example(self):\n")
            f.write("        self.assertTrue(True)\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    unittest.main()\n")
        print(f"Created {test_file_path}")
    else:
        print(f"{test_file_path} already exists.")


def main():
    project_root = os.getcwd()
    print(f"Project root: {project_root}")
    # Step 1: Select top-level directory (excluding 'tests', '.git')
    target_dir = select_directory(project_root, exclude=["tests", ".git"], depth=0)
    # Step 2: Create new file (and possibly new subdirectory)
    file_path = create_python_file(target_dir)
    # Step 3: Mirror in tests/
    mirror_in_tests(target_dir, os.path.basename(file_path))


if __name__ == "__main__":
    main()
