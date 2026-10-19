class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number_as_string = ""

        for digit in digits:
            number_as_string += str(digit)

        incremented_number = str(int(number_as_string) + 1)

        result_digits = []

        for digit in incremented_number:
            result_digits.append(int(digit))

        return result_digits