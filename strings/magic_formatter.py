class MagicFormatter:
    def __init__(self, txt_file_or_string, width):
        """
        Gets a file or a string and formats it
        :param txt_file_or_string: str or file name
        :param width: width of the text you want to extract
        """

        try:
            self.text = open(txt_file_or_string, 'r').read()
        except FileNotFoundError:
            self.text = txt_file_or_string
        self.width = width

    def __justify_phrase(self, phrase, last_line):
        """
        Gets a full phrase (the line formed) and returns a justified phrase with spaces

        IMPORTANT: add_count_auxiliary and reset_loop variables are just for support when adding a new space
        :param phrase: str
        :param last_line: bool (check if last line in sentence)
        :return: phrase: str
        """

        if len(phrase) < self.width:
            list_phrase = list(phrase)
            space_indexes = [index for index, element in enumerate(list_phrase) if element == ' ']
            add_count_auxiliary, space_index, reset_loop = 0, 0, 0

            width = self.width
            if r'\n' in phrase:
                width = self.width + phrase.count(r'\n')+1
            if last_line and width/2 > len(phrase):
                return phrase
            while len(list_phrase) < width and space_indexes:
                list_phrase.insert(space_indexes[space_index] + add_count_auxiliary, ' ')
                add_count_auxiliary += 1 + reset_loop
                if space_index == len(space_indexes)-1:
                    space_index = 0
                    reset_loop += 1
                    add_count_auxiliary = reset_loop
                else:
                    space_index += 1

            phrase = ''.join(list_phrase)
        return phrase

    def __reformat_phrase(self, item, phrase, remove_blank=True, normal_append=False, justify=False, last_line=False):
        """
        Gets an item and the formed phrase until calling function, it means it will be called many times,
        until it forms a complete line
        :param item: str (item do append)
        :param phrase: str (line formed until given point)
        :param remove_blank: bool (removes empty space from last item in phrase)
        :param normal_append: bool
        :param justify: bool (justify text)
        :param last_line: bool (used if justify = True)
        :return:
        """
        if normal_append:
            phrase = phrase + item if len(phrase + item) == self.width else phrase + item + ' '
        if remove_blank:
            phrase = phrase if phrase[-1] is not ' ' else phrase[:-1]
        if justify:
            phrase = self.__justify_phrase(phrase, last_line=last_line)
        return phrase

    def reformat_text(self, file_name, justify=False):
        """
        Gets a string for naming the new file and a justify parameter to justify text
        If justify = True, justifies text
        :param file_name: str
        :param justify: str
        :return:
        """
        file = open(file_name, 'w')
        text = self.text.replace('\n', '\n ')
        phrase = ''

        for index, item in enumerate(text.encode('unicode-escape').decode().split()):
            if r'\n' in phrase:
                phrase = self.__reformat_phrase(item, phrase, justify=justify, last_line=True)
                file.write(phrase.replace(r'\n', '\n'))
                phrase = item + ' '

            elif len(phrase + item) > self.width:
                phrase = self.__reformat_phrase(item, phrase, justify=justify)
                file.write(phrase + '\n')
                phrase = item + ' '

            elif index is len(text.encode('unicode-escape').decode().split())-1:
                phrase = self.__reformat_phrase(item, phrase, remove_blank=True, normal_append=True, justify=justify,
                                                last_line=True)
                file.write(phrase + '\n')
                phrase = item + ' '

            else:
                phrase = self.__reformat_phrase(item, phrase, remove_blank=False, normal_append=True, justify=False)
