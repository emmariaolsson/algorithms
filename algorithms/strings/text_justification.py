"""
Given an array of words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
"""

"""
The requirements of the function is as follows
1. The function must output a list of strings with length equal to max_width
2. The function must throw a ValueError exception if a word is longer
    than max_width
3. The function must return lines that separate each word with at least 
    one blank space
4. The function must pad words that are alone in a line with spaces trailing
    the word


The cyclomatic complexity (as calculated by lizard) before refactoring
was 13 which means I should be able to refactor this code to obtain a 
cyclomatic complexity of 9 n order to decrease the complexity by at least 
35%

The algorithm does the following:
1. while there are more words, do:
    1.1. while there is more space in the line, do:
        1.1.1. check that the word fits in a single line, throw ValueError otherwise
        1.1.2. add the word to the line
        1.1.3. add a blank space for every word that isn't the first word
        1.1.4. if the word and blank space does not fit to the line: remove it and exit loop
        1.1.5. go to next word
    1.2. if we are at the last word in input, do:
        1.2.1. for all words in the line:
            1.2.1.1. add word to the line
            1.2.1.2. add a blank space to the line
        1.2.2. remove the last blank space
        1.2.3. add blank spaces so that the row has a length of max_width
    1.3. if we have more words in input and there are more than one word in row, do:
        1.3.1. determine how many spaces should be between every word in order
            to have the rowo be of length max_width
        1.3.2. for every word in the row, do:
            1.3.2.1. add word to the line
            1.3.2.2. add space after each word
            1.3.2.3. add more space if the space isn't evenly divisible
    1.4. if there are more words in input but there is only one word in row, do:
        1.4.1. add the word to the row
        1.4.2. add space so that the row length is max_width
    1.5. add the row to the output list


The function can be refacored into the following functions:
1. main function
2. function for fitting a list of words to a string of fix length
3. function for giving what words fit in a row
4. function for left aligning text

The new algorithm would then be

text_justification: 
1. while there are more words in the input, do:
    1.1. calculate what words fit in the row
    1.2. if there are no more words in the input, do:
        1.2.1. left align row
    1.3. if there are more words in the input, do:
        1.3.1. fit words to row
    1.4. add row to output

fit_words_to_row:
1. if there is only one word in row, do:
    1.1. add word to output
    1.2. add spaces in order to fit to width
2. if there is more than one word in input, do:
    2.1. calculate how much space should be between words
    2.2. while there are still words, do:
        2.2.1. add word to row
        2.2.2. add space between words to row
        2.2.3. add more space if it isn't evenly divisble in row

left_align:
1. while there are more words in input, do:
    1.1. add word to row
    1.2. add blank space to row
2. remove last blank space of row
3. add blank space in order to fit row to width

words_in_next_row:
1. while there is still space in the row, do:
    1.2. add word to row
    1.3. add blank space to row


The results are as follows:
100% test coverage
cyclomatic complexity (as calculated by lizard):
    text_justification: 3
    left_align: 2
    words_in_next_row: 4
    fit_words_to_row: 6
"""

def left_align(words, width):
    """
    :type words: list(string)
    :type width: int
    :rtype: string
    returns a string of length width
    words must fit within width characters with a space between them
    """
    row = ""
    for word in words:
        row += word
        row += " "
    row = row[:-1] # remove last space
    row += (" " * (width - len(row))) # Add trailing space
    return row

def words_in_next_row(words, index, width):
    """
    :type words: list(string)
    :type index: int
    :type width: int
    :Throws ValueError if words[i] > width for words in row:
    words is the words to be aligned
    the index denotes which word will be the first in the row
    width tells how much space is in each row
    """
    space_left = width
    words_in_row = []
    i = index
    while i < len(words) and space_left >= len(words[i]):
        words_in_row.append(words[i])
        space_left = space_left - (len(words[i]) + 1)
        i += 1
    if not words_in_row:
        raise ValueError("there exists a word whose length is larger than max_width")
    return words_in_row

def fit_words_to_row(words, width):
    """
    :type words: list(string)
    :type width: int
    fits words to a string of length width with evenly divided space between words
    words must fit within a string of length width with at least one blank space 
    between them
    """
    row = ""
    if len(words) == 1:
        row = left_align(words, width)
    else:
        space_num = width - sum(len(word) for word in words)
        interval_space = space_num // (len(words) - 1)
        rest_space = space_num - interval_space * (len(words) - 1)
        for i in range(len(words)):
            row += words[i]
            if i < len(words) -1:
                row += (" " * (interval_space))
            if rest_space > 0:
                row += " "
                rest_space -= 1
    return row
            
    


def text_justification(words, max_width):
    '''
    :type words: list
    :type max_width: int
    :rtype: list
    '''
    ret = []  # return value
    index = 0  # the index of current word in words
    while index < len(words):
        row_words = words_in_next_row(words, index, max_width)
        index += len(row_words)
        # if the row is the last
        if index == len(words):
            ret.append(left_align(row_words, max_width))
        # not the last row
        else:
            ret.append(fit_words_to_row(row_words, max_width))
    return ret
