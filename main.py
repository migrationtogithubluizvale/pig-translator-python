class PigLatinTranslator:
    """
        Class used to represent a simple translate phrase/world bases on specific rules.
    """

    __LOWER_CASE = [chr(lo) for lo in range(97, 123)]
    __UPPER_CASE = [chr(up) for up in range(65, 91)]
    __PUNCTUATION = [chr(pu) for pu in range(32, 64)]
    __VOWEL = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
    __ALPHABETIC = __LOWER_CASE + __UPPER_CASE
    __WITH_CONSONANT = "ay"
    __WITHOUT_CONSONANT = "yay"

    def __init__(self, string):
        if string == "":
            raise ValueError("Sentence can not be empty")
        self._phrase = string.split()
        self._string = string
        self._first_letter = string[0]

    def __repr__(self):
        return f'Simple text translator for {self._string}'

    def __str__(self):
        return f'Simple text translator to convert {self._string} to:'

    @staticmethod
    def has_consonant(string):
        consonants = [c for c in PigLatinTranslator.__ALPHABETIC if c not in PigLatinTranslator.__VOWEL]
        if any((c in consonants) for c in string):
            return True
        else:
            return False

    @staticmethod
    def has_punctuation(string):
        if any((c in PigLatinTranslator.__PUNCTUATION) for c in string):
            return True
        else:
            return False

    @staticmethod
    def has_letters(string):
        if any((c in PigLatinTranslator.__ALPHABETIC) for c in string):
            return True
        else:
            return False

    @staticmethod
    def readjust_punctuation(string):
        string_to_return = string
        for index, s in enumerate(string):
            if s in PigLatinTranslator.__PUNCTUATION:
                string_to_return = string_to_return.replace(s, "")
                string_to_return += s

        return string_to_return

    def __find_ending_and_prefix(self):
        """
        This method returns the last part of the translated world, defining the index where the first part
        should start

        :returns: ending: string, prefix: ending, index: int
        """
        prefix = ""
        index = 0
        for i, c in enumerate(self._string):
            if c not in PigLatinTranslator.__VOWEL:
                prefix += c
            else:
                index = i
                break

        if PigLatinTranslator.has_consonant(self._string):
            return PigLatinTranslator.__WITH_CONSONANT, prefix.lower(), index
        else:
            prefix = ""
            return PigLatinTranslator.__WITHOUT_CONSONANT, prefix.lower(), index

    def __find_stem(self, index):
        """
        This method returns the first part of the translated world
        :param index: int
        :return: stem: string
        """
        stem = self._string[index:]
        if self._first_letter.isupper():
            return stem.capitalize()

        return stem

    def __resolve(self):
        """
            This method apply the translation rules
        """
        string_to_return = ""
        ending, prefix, index = self.__find_ending_and_prefix()
        stem = self.__find_stem(index)
        string_to_return += stem + prefix + ending
        if PigLatinTranslator.has_punctuation(string_to_return):
            string_to_return = PigLatinTranslator.readjust_punctuation(string_to_return)
        return string_to_return

    def translate(self):
        """
        This method translate a single world

        >>> sandwich = PigLatinTranslator("sandwich")
        >>> sandwich.translate()
        'andwichsay'
        """
        if PigLatinTranslator.has_letters(self._string):
            return self.__resolve()
        else:
            return self._string

    def translate_phrase(self):
        """
        This method translate a complete sentence
        :return: sentence: string
        """
        sentence = ""
        for string in self._phrase:
            latin_translate = PigLatinTranslator(string)
            sentence_translated = latin_translate.translate()
            sentence += sentence_translated + " "
        return sentence


if __name__ == '__main__':
    sample_session = ["Stop", "No littering", "No shirts, no shoes, no service", "No persons under 14 admitted",
                      "Hey buddy, get away from my car!"]

    for phrase in sample_session:
        translator = PigLatinTranslator(phrase)
        print(translator, translator.translate_phrase())
