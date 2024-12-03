from collections import OrderedDict

from enums import DataType


class DataTool:
    def __init__(self, data):
        self.data = data
        self.elements = []

    def set_elements(self):
        pass


class DataNumbers(DataTool):
    def __init__(self, data):
        super().__init__(data)

    def set_elements(self):
        for data in self.data:
            for char in data.split():
                if (char.startswith('-') and char[1:].isdigit()) or char.isdigit():
                    self.elements.append(int(char))
                else:
                    print(f'"{char}" is not a long. It will be skipped.')


class DataWords(DataTool):
    def __init__(self, data):
        super().__init__(data)

    def set_elements(self):
        for data in self.data:
            self.elements.extend(data.split())


class DataLines(DataTool):
    def __init__(self, data):
        super().__init__(data)

    def set_elements(self):
        self.elements = self.data


class SortingTool:
    def __init__(self, elements):
        self.elements = elements

    def sort_elements(self):
        pass

    def display(self, data_type: DataType):
        pass

    def write_to_file(self, filename: str, data_type: DataType):
        pass


class SortingNatural(SortingTool):
    def __init__(self, elements):
        super().__init__(elements)

    def sort_elements(self):
        self.elements.sort(reverse=False)

    def display(self, data_type: DataType):
        print(f'Total '
              f'{"numbers" if data_type is DataType.LONG else "words" if data_type is DataType.WORD else "lines"}: '
              f'{len(self.elements)}.')
        if data_type is not DataType.LINE:
            print(f'Sorted data: {" ".join(map(str, self.elements))}')
        else:
            print('Sorted data:')
            print('\n'.join(self.elements))

    def write_to_file(self, filename: str, data_type: DataType):
        with open(filename, 'w') as file:
            file.write(
                f'Total '
                f'{"numbers" if data_type is DataType.LONG else "words" if data_type is DataType.WORD else "lines"}: '
                f'{len(self.elements)}.\n'
            )
            if data_type is not DataType.LINE:
                file.write(f'Sorted data: {" ".join(map(str, self.elements))}')
            else:
                file.write('Sorted data:\n')
                file.write('\n'.join(self.elements))


class SortingCount(SortingTool):
    def __init__(self, elements):
        super().__init__(elements)
        self.ordered_elements = None

    def sort_elements(self):
        counts = {
            element: self.elements.count(element) for element in self.elements
        }
        self.ordered_elements = OrderedDict(sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=False))

    def display(self, data_type: DataType):
        print(f'Total '
              f'{"numbers" if data_type is DataType.LONG else "words" if data_type is DataType.WORD else "lines"}: '
              f'{len(self.elements)}.')
        for element, count in self.ordered_elements.items():
            print(f'{element}: {count} time(s), {int(count / len(self.elements) * 100)}%')

    def write_to_file(self, filename: str, data_type: DataType):
        with open(filename, 'w') as file:
            file.write(
                f'Total '
                f'{"numbers" if data_type is DataType.LONG else "words" if data_type is DataType.WORD else "lines"}: '
                f'{len(self.elements)}.\n'
            )
            for element, count in self.ordered_elements.items():
                file.write(f'{element}: {count} time(s), {int(count / len(self.elements) * 100)}%\n')
