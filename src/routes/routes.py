from src.controllers.CourseController import *
from src.controllers.IndexController import *
from src.controllers.TeacherController import *
<<<<<<< HEAD


=======
>>>>>>> 2f77beae1591b5444b0b7d5b5f6e76257bd4ca84
routes = {

    "index_route": "/", "indexcontroller": IndexController.as_view("Index"),
    "insert_route_teacher": "/insert/teacher", "insert_controller_teacher": TeacherController.as_view("Teacher"),
    "delete_route_teacher": "/delete/teacher/<int:id_teacher>", "delete_controller_teacher": DeleteTeacherController.as_view("Delete_Teacher"),
<<<<<<< HEAD
    "insert_route_course": "/insert/course", "insert_controller_course": CourseController.as_view("Course"),
    "delete_route_course": "/delete/course/<int:id_course>", "delete_controller_course": DeleteCourseController.as_view("Delete_Course"),

=======
    "update_route_teacher": "/update/teacher/<int:id_teacher>", "update_controller_teacher": UpdateTeacherController.as_view("Update_Teacher"),
>>>>>>> 2f77beae1591b5444b0b7d5b5f6e76257bd4ca84
}

