from src.controllers.IndexController import *
from src.controllers.TeacherController import *
from src.controllers
routes = {
    "index_route": "/", "indexcontroller": IndexController.as_view("Index"),
    "insert_route_teacher": "/insert/teacher", "insert_controller_teacher": TeacherController.as_view("Teacher"),
    "delete_route_teacher": "/delete/teacher/<int:id_teacher>", "delete_controller_teacher": DeleteTeacherController.as_view("Delete_Teacher")   
}

