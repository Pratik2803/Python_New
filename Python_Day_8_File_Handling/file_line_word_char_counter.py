def count_lines_words_chars(filename: str) -> tuple:
    """
    Counts the number of lines, words, charcaters in a file

    Args:
        filename: Name of the file with location which need to be analyzed

    Returns:
        A tuple containing the number of lines, words, and characters.
    """

    lines_count = 0
    words_count = 0
    chars_count = 0

    try:
        with open(file=filename, mode='r') as file:
            for line in file:
                lines_count += 1
                words_count += len(line.strip().split())
                chars_count += len(line.strip())

    except FileNotFoundError:
        print(f"File :{filename} not found")
        return 0, 0, 0

    return lines_count, words_count, chars_count


if __name__ == "__main__":
    filename = "Python_Day_8_File_Handling\\log.txt"

    lines, words, chars = count_lines_words_chars(filename)
    print(f"Number of lines {lines}")
    print(f"Number of words {words}")
    print(f"Number of characters {chars}")
