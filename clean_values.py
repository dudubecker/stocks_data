def clean_values(string):
    
    import numpy as np
    
    try:

        string = string.replace('\n', '')  # filtering '\n'

    except:

        return 0

    else:

        if '%' in string:

            try:
                string = string.replace('%', '').replace(',', '.')  # filtering "%", replacing commas for dots
                value = float(string)

                return round(value / 100, 3)

            except:  # possible error if percentage >= 1000%

                string = string.replace('%', '')

                if '-' in string:  # the comma position will be different if the number is negative

                    comma_pos = string.find(',')  # the value will be given based on the comma position
                    string = string.replace(',', '').replace('.', '')
                    value = float(string) / (10 ** comma_pos - 5)

                else:

                    comma_pos = string.find(',')
                    string = string.replace(',', '').replace('.', '')
                    value = float(string) / (10 ** comma_pos - 4)

                return round(value / 100, 3)

        elif string.count('.') >= 2:

            try:

                string = string.replace('.', '')  # filtering dots for big values
                value = float(string)
                return value

            except:

                string = string.replace('.', '')
                string = string[0:string.find(',')]
                value = float(string)

                return value

        elif string == '-':  # this means that the value is missing

            return np.nan  # returning NaN if the information is missing

        else:

            try:
                string = string.replace(',', '.')  # replacing commas for dots
                value = float(string)

                return value

            except:  # possible error if the value is >= 1000

                if '-' in string:

                    comma_pos = string.find(',')
                    string = string.replace(',', '').replace('.', '')

                    return float(string) / (10 ** (comma_pos - 4))


                else:

                    comma_pos = string.find(',')
                    string = string.replace(',', '').replace('.', '')

                    return float(string) / (10 ** (comma_pos - 3))
