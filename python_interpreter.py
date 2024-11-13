import sys
import os

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.isfile(file_path):
            try:
                # If a script is provided as an argument, execute it
                exec(open(file_path).read())
            except Exception as e:
                print(f"Error executing the script: {e}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Error: The file '{file_path}' does not exist.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: No file path provided.", file=sys.stderr)
        sys.exit(1)