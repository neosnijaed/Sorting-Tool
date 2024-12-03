import argparse

from enums import DataType, SortingType
from sorting_tool import DataNumbers, DataWords, DataLines, SortingCount, SortingNatural


def get_command_line_arguments() -> tuple[str, str, str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument('-dataType', nargs='?', const='no_data_type')
    parser.add_argument('-sortingType', nargs='?', const='no_sorting_type')
    parser.add_argument('-inputFile', nargs='?', const='no_input_file_name')
    parser.add_argument('-outputFile', nargs='?', const='no_output_file_name')
    args, unknown_args = parser.parse_known_args()
    for unknown_arg in unknown_args:
        print(f'"{unknown_arg}" is not a valid parameter. It will be skipped. ')
    if args.sortingType == 'no_sorting_type':
        print('No sorting type defined!')
        exit(0)
    if args.dataType == 'no_data_type':
        print('No data type defined!')
        exit(0)
    if args.inputFile == 'no_input_file_name':
        print('No input file name defined!')
        exit(0)
    if args.outputFile == 'no_output_file_name':
        print('No output file name defined!')
        exit(0)
    return (args.sortingType or SortingType.NATURAL.value,
            args.dataType or DataType.LONG.value,
            args.inputFile or 'no_input_file',
            args.outputFile or 'no_output_file')


def read_input(inputs: list) -> None:
    while True:
        try:
            data = input()
        except EOFError:
            break
        else:
            inputs.append(data)


def read_input_from_file(filename: str, inputs: list) -> None:
    with open(filename, 'r') as file:
        for line in file:
            inputs.append(line.strip())


def select_data_tool(data_type: DataType, data: list) -> DataNumbers or DataWords or DataLines:
    data_tool = {
        DataType.LONG: DataNumbers,
        DataType.WORD: DataWords,
        DataType.LINE: DataLines
    }
    return data_tool[data_type](data)


def select_sorting_tool(sorting_type: SortingType, elements: list) -> SortingNatural or SortingCount:
    sorting_tool = {
        SortingType.COUNT: SortingCount,
        SortingType.NATURAL: SortingNatural
    }
    return sorting_tool[sorting_type](elements)


def main() -> None:
    data = []
    sorting_type, data_type, input_file_name, output_file_name = get_command_line_arguments()
    if input_file_name == 'no_input_file':
        read_input(data)
    else:
        read_input_from_file(input_file_name, data)
    data_tool = select_data_tool(DataType(data_type), data)
    data_tool.set_elements()
    sorting_tool = select_sorting_tool(SortingType(sorting_type), data_tool.elements)
    sorting_tool.sort_elements()
    if output_file_name == 'no_output_file':
        sorting_tool.display(DataType(data_type))
    else:
        sorting_tool.write_to_file(output_file_name, DataType(data_type))


if __name__ == '__main__':
    main()
