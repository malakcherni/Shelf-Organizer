# Shelf Organizer

A Python command-line program that checks whether two books are in the correct order on a shelf, using Library of Congress-style 4-line codes.

## Tools

Python 3 (standard library only, no external libraries)

## How It Works

Shelves are read from left to right. You enter the code for Book 1 and Book 2, each made up of four lines. The program compares them line by line in this order:

1. Alphabetical comparison (e.g., `ABC` vs. `ABD`)
2. Numerical comparison (e.g., `123` vs. `124`)
3. Alphanumeric comparison (e.g., `A45` vs. `A46`)
4. Final string comparison (e.g., `BookA` vs. `BookB`)

Based on the results, the program tells you whether the books are in the correct order.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```
python shelf_organizer.py
```

4. Follow the prompts to enter the codes for both books.

## Example

```
Enter the first line of the book 1 code: ABC
Enter the second line: 123
Enter the third line: A45
Enter the fourth line: BookA

Great, now the second book!

Enter the first line of the book 2 code: ABD
Enter the second line: 124
Enter the third line: A46
Enter the fourth line: BookB

RIGHT ORDER
```

## Limitations

This program only works with books that have exactly four lines of code. It does not support books with more or fewer lines.

## What I Learned

- String and list manipulation
- Writing conditional logic
- Comparing alphabetical and numerical values
- Building a simple interactive command-line application
- Basic library classification systems

## References

- [Library of Congress shelving quiz](https://www.goconqr.com/en/quiz/38743571/library-of-congress-shelving-quiz)
- [UDST Library guide on classification systems](https://library.udst.edu.qa/c.php?g=1462957&p=10881504)
