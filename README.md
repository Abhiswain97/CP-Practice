# CP-Practice
Data Structures and Algo prep for CP

## VS-Code Python Snippets

1. Ctrl + Shift + P to open Command Pallete. 
2. Go to Configure Snippets, select Python Snippet.
3. Paste this:
    ```
    {
        "Fast I/O": {
            "body": [
                "",
                "# Author: Abhishek Swain",
                "# Mail: abhi08as.as@gmail.com",
                "# Date: ${CURRENT_DATE}-${CURRENT_MONTH}-${CURRENT_YEAR}",
                "",
                "from io import BytesIO",
                "from os import read, fstat",
                "from sys import stdout",
                "",
                "fast_input = BytesIO(read(0, fstat(0).st_size)).readline",

            ],
            "description": "Python template to take fast input"
        },
        "Fast I/O with List": {
            "body": [
                "",
                "# Author: Abhishek Swain",
                "# Mail: abhi08as.as@gmail.com",
                "# Date: ${CURRENT_DATE}-${CURRENT_MONTH}-${CURRENT_YEAR}",
                "",
                "from io import BytesIO",
                "from os import read, fstat",
                "from sys import stdout",
                "",
                "fast_input = BytesIO(read(0, fstat(0).st_size)).readline",
                "",
                "n = int(fast_input().decode())",
                "",
                "# Take input for newline separated integers",
                "arr = [int(fast_input().decode()) for _ in range(n)]",
                "",
                "# Take input for space separated integers",
                "arr = list(map(int, fast_input().split()))"
            ],
            "description": "Python template to take fast input with lists"
        }
    }
    ```
