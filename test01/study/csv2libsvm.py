
import pandas as pd

def csv2libsvm(file_name, output_name):
    readin = open(file_name, 'r')
    # write data file
    output = open(output_name, 'w')
    try:
        the_line = readin.readline()
        while the_line:
            # delete the \n
            the_line = the_line.strip('\n')
            index = 0;
            output_line = ''
            for sub_line in the_line.split(','):
                # the label col
                if index == 0:
                    output_line = sub_line
                # the features cols
                if sub_line != 'NULL' and index != 0:
                    the_text = ' ' + str(index) + ':' + sub_line
                    output_line = output_line + the_text
                index = index + 1
            output_line = output_line + '\n'
            output.write(output_line)
            the_line = readin.readline()
    finally:
        readin.close()


if __name__ == '__main__':
    file_name = "wis.csv"
    output_name = "sample_wis_libsvm.txt"

    csv2libsvm(file_name, output_name)

