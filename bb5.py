class Course():
    def __init__(self,course):
        self.course = course
    def get_course(self):
        return self.course
bb=Course(["math","science","english"])
print(bb.get_course())
    