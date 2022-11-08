from src.controllers.MenuController import *
from src.controllers.CourseController import *
from src.controllers.IndexController import *
from src.controllers.TeacherController import *
from src.controllers.ClassController import *
from src.controllers.DisciplineController import *
from src.controllers.PlanningController import *
from src.controllers.Academic_PeriodController import *
from src.controllers.Matrix_Curriculum import *

routes = {
    "index_route": "/", "indexcontroller": IndexController.as_view("Index"),
    "menu_route": "/menu", "menucontroller": MenuController.as_view("Menu"),
    "insert_route_teacher": "/insert/teacher", "insert_controller_teacher": TeacherController.as_view("Teacher"),
    "delete_route_teacher": "/delete/teacher/<int:id_teacher>", "delete_controller_teacher": DeleteTeacherController.as_view("Delete_Teacher"),
    "update_route_teacher": "/update/teacher/<int:id_teacher>", "update_controller_teacher": UpdateTeacherController.as_view("Update_Teacher"),
    "insert_route_course": "/insert/course", "insert_controller_course": CourseController.as_view("Course"),
    "delete_route_course": "/delete/course/<int:id_course>", "delete_controller_course": DeleteCourseController.as_view("Delete_Course"),
    "update_route_course": "/update/course/<int:id_course>", "update_controller_course": UpdateCourseController.as_view("Update_Course"),
    "insert_route_class": "/insert/class", "insert_controller_class": ClassController.as_view("Class"),
    "delete_route_class": "/delete/class/<int:id_class>", "delete_controller_class": DeleteClassController.as_view("Delete_Class"),
    "update_route_class": "/update/class/<int:id_class>", "update_controller_class": UpdateClassController.as_view("Update_Class"),
    "insert_route_discipline": "/insert/discipline", "insert_controller_discipline": DisciplineController.as_view("Discipline"),
    "delete_route_discipline": "/delete/discipline/<int:id_discipline>", "delete_controller_discipline": DeleteDisciplineController.as_view("Delete_Discipline"),
    "update_route_discipline": "/update/discipline/<int:id_discipline>", "update_controller_discipline": UpdateDisciplineController.as_view("Update_Discipline"),
    "insert_route_plan": "/insert/plan", "insert_controller_plan": PlanningController.as_view("Planning"),
    "delete_route_plan": "/delete/plan/<int:id>", "delete_controller_plan": DeletePlanController.as_view("Delete_Planning"),
    "update_route_plan": "/update/plan/<int:id>", "update_controller_plan": UpdatePlanController.as_view("Update_Planning"),
    "insert_route_academic_period": "/insert/academic_period", "insert_controller_academic_period": Academic_PeriodController.as_view("Academic_Period"),
    "delete_route_academic_period": "/delete/academic_period/<int:id_period>", "delete_controller_academic_period": DeleteAcademic_PeriodController.as_view("Delete_Academic_Period"),
    "update_route_academic_period": "/update/academic_period/<int:id_period>", "update_controller_academic_period": UpdateAcademic_PeriodController.as_view("Update_Academic_Period"),
    "insert_route_matrix_curriculum": "/insert/matrix_curriculum", "insert_controller_matrix_curriculum": Matrix_CurriculumController.as_view("Matrix_Curriculum"),
    "delete_route_matrix_curriculum": "/delete/matrix_curriculum/<int:id>", "delete_controller_matrix_curriculum": DeleteMatrix_CurriculumController.as_view("Delete_Matrix_Curriculum"),
    "update_rout_matrix_curriculum": "/update/matrix_curriculum/<int:id>", "update_matrix_curriculum": UpdateMatrix_CurriculumController.as_view("Update_Matrix_Curriculum"),
}
