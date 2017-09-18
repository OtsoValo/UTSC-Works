"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-decrypted.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    The function will open files and close files.
    The function will return nothing.
    """
    # open and read the messages file
    file_messages = open(MSG_FILENAME, 'r')
    messages = cipher_functions.read_messages(file_messages)
    # close the file
    file_messages.close()
    # open and read the cards file
    file_cards = open(DECK_FILENAME, 'r')
    deck_of_cards = cipher_functions.read_deck(file_cards)
    # close the file
    file_cards.close()
    # encrypt or decrypt based on cards, messages and MODE
    result = cipher_functions.process_messages(deck_of_cards, messages, MODE)
    # print the result
    print(result)
    return None


main()
