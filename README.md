SHELF ORGANIZER:

This is a beginner-friendly Python program that checks whether two books are arranged in the correct order on a shelf, based on their unique 4-line codes.

TOOLS:
This project was created using Python 3 and standard libraries only. No external libraries were required.

HOW IT WORKS:
Shelves are read from left to right. The user enters the code for Book 1 and Book 2, each made up of four lines. The program then compares each line in the following order:

Alphabetical comparison (e.g., ABC vs. ABD)

Numerical comparison (e.g., 123 vs. 124)

Alphanumeric logic (e.g., A45 vs. A46)

Final string comparison (e.g., BookA vs. BookB)
Based on the results, the program tells the user if the books are in the correct order or not.

SAMPLE INPUT:
Enter the first line of the book 1 code: ABC
Enter the second line: 123
Enter the third line: A45
Enter the fourth line: BookA

Great, now the second book!

Enter the first line of the book 2 code: ABD
Enter the second line: 124
Enter the third line: A46
Enter the fourth line: BookB

SAMPLE OUTPUT:
AMAZING! RIGHT ORDER
or
OH NO! WRONG ORDER

RESOURSES:

Python programming language

Standard Python libraries (no extra installations)

REFERENCES:
Library of Congress shelving quiz: https://www.goconqr.com/en/quiz/38743571/library-of-congress-shelving-quiz

UDST Library guide on classification systems: https://library.udst.edu.qa/c.php?g=1462957&p=10881504

LIMITATIONS:
This program only works with books that have exactly four lines of code. It does not support books with more or fewer lines.

WHAT I LEARNED:
Through this project, I practiced and strengthened my skills in the following areas:

String and list manipulation

Writing conditional logic

Comparing alphabetical and numerical values

Creating a simple and interactive command-line application

Understanding basic classification systems

HOW TO RUN:

Download or clone the repository to your computer.

Open the file named “Shelfe organizer code.py” in any code editor or terminal.

Run the script using Python 3.

Follow the prompts to input the codes for both books.
