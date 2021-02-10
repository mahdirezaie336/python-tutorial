class Grade:

    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score

    def __str__(self):
        return str(self.student_id) + ' ' + str(self.course_code) + ' ' + str(self.score)

    def __eq__(self, other):
        return (other.student_id == self.student_id) and (other.course_code == self.course_code)

    @staticmethod
    def parse_grade(string):
        parts = string.split()
        return Grade(int(parts[0]), int(parts[1]), float(parts[2]))


class CourseUtil:

    def __init__(self):
        self.address = None

    def set_file(self, address):
        self.address = address
        with open(address, 'a') as file:
            pass

    def load(self, line_number):
        with open(self.address, 'r') as file:
            for i, row in enumerate(file):
                if line_number == i + 1:
                    return Grade.parse_grade(row)
        return None

    def save(self, grade):
        with open(self.address, 'r') as file:
            for row in file:
                if Grade.parse_grade(row) == grade:
                    return
        with open(self.address, 'a') as file:
            if file.tell() != 0:
                file.write('\n')
            file.write(str(grade))

    def calc_course_average(self, course_code):
        summ = 0.0
        number = 0
        with open(self.address, 'r') as file:
            for row in file:
                parts = row.split()
                if int(parts[1]) == course_code:
                    summ += float(parts[2])
                    number += 1
        if number == 0:
            return 0.0
        return summ / number

    def calc_student_average(self, student_id):
        summ = 0.0
        number = 0
        with open(self.address, 'r') as file:
            for row in file:
                parts = row.split()
                if int(parts[0]) == student_id:
                    summ += float(parts[2])
                    number += 1
        if number == 0:
            return 0.0
        return summ / number

    def count(self):
        num = 0
        with open(self.address, 'r') as file:
            for row in file:
                num += 1
        return num
