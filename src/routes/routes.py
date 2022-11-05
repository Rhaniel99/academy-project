from src.controllers.CourseController import *
from src.controllers.IndexController import *
from src.controllers.TeacherController import *
from src.controllers.ClassController import *

routes = {
    "index_route": "/", "indexcontroller": IndexController.as_view("Index"),
    "insert_route_teacher": "/insert/teacher", "insert_controller_teacher": TeacherController.as_view("Teacher"),
    "delete_route_teacher": "/delete/teacher/<int:id_teacher>", "delete_controller_teacher": DeleteTeacherController.as_view("Delete_Teacher"),
    "update_route_teacher": "/update/teacher/<int:id_teacher>", "update_controller_teacher": UpdateTeacherController.as_view("Update_Teacher"),
    "insert_route_course": "/insert/course", "insert_controller_course": CourseController.as_view("Course"),
    "delete_route_course": "/delete/course/<int:id_course>", "delete_controller_course": DeleteCourseController.as_view("Delete_Course"),
    "insert_route_class": "/insert/class", "insert_controller_class": ClassController.as_view("Class"),
    "delete_route_class": "/delete/class/<int:id_class>", "delete_controller_class": DeleteClassController.as_view("Delete_Class"),
    "update_route_class": "/update/class/<int:id_class>", "update_controller_class": UpdateClassController.as_view("Update_Class"),
}