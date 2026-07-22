class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_choices = {
            0: 0,
            1: 0
        }
        number_of_sandwiches = len(sandwiches)

        for student in students:
            student_choices[student] += 1
        
        for sandwich in sandwiches:
            if student_choices[sandwich] > 0:
                student_choices[sandwich] -= 1
                number_of_sandwiches -= 1
            else:
                return number_of_sandwiches
        
        return number_of_sandwiches