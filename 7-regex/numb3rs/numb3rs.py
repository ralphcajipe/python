# NUMB3RS

import re


def main():
    """
    Takes a string as input, splits it into a list of strings, checks if the
    list has 4 elements, checks if each element is a number between 0 and
    255, and returns True if all of those conditions are met. Else,
    it returns False.
    """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    If the IP address is in the correct format, then check if each IP octet
    is between 0 and 255.

    :param ip: The IP address to validate
    :return: True or False
    """
    try:
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            ip_list = ip.split(".")
            for octet in ip_list:
                if int(octet) < 0 or int(octet) > 255:
                    return False
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
