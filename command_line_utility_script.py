import argparse


def main():
    parser = argparse.ArgumentParser(description="Creating a new command line tool")
    parser.add_argument('operation', nargs='?', help="input the type of operation that needs to be performed on the file.", default='')
    parser.add_argument('input_file', help="Path to the input file.")

    args = parser.parse_args()
    print(args)

    # print(f'Operation : {args.operation}')
    # print(f'Input file : {args.input_file}')
    input_file_name = args.input_file
    total_bytes = 0
    total_lines = 0
    total_words = 0

    with open(input_file_name) as f:
        data = f.readlines()
        print(type(data))
        print(data)
        total_lines = len(data)
        # line = data.split()
        # print(line)
        # total_words += len(line)
        # lines = f.readlines()
        # print(lines)
        # for i in range(len(data)):
        #     total_bytes = total_bytes  + bytes(data[i], "UTF-8")
        # print(total_bytes)
    
    return total_lines

if __name__ == "__main__":
    main()