from controllers.buildingControl import InsertControlBuilding
from controllers.classControl import InsertControlClass
from controllers.courseControl import InsertControlCourse
from controllers.disciplineControl import InsertControlDiscipline
from controllers.planningControl import InsertControlPlanning
from src.controllers.teacherControl import *
from src.app import app


routes = {
    "insert_route_teacher": "/insert/teacher/", "insert_control_teacher": InsertControlTeacher.as_view("insert_teacher"),
   # "delete_route_teacher": "/delete/teacher/<int:id_teacher>","delete_control_teacher": DeleteTeacher.as_view("delete_teacher"),
 #  "update_route_teacher": "/update/teacher/<int:id_teacher>","update_control_teacher": UpdateTeacher.as_view("update_teacher"),
   # "not_found_route": 404, "not_found_control": NotFoundControl.as_view("not_found"),
    "insert_route_course": "/insert/course", "insert_control_course": InsertControlCourse.as_view("insert_course"),
    "insert_route_discipline": "/insert/course", "insert_control_discipline": InsertControlDiscipline.as_view("insert_discipline"),
    "insert_route_class": "/insert/class", "insert_control_class": InsertControlClass.as_view("insert_discipline"),
    "insert_route_planning": "/insert/planning", "insert_control_planning": InsertControlPlanning.as_view("insert_planning"),
    "insert_route_institution_academy": "/insert/institution_academy", "insert_control_institution_academy": InsertControlInstitutionAcademy.as_view("insert_institution_academy"),
    "insert_route_matrix_curriculum": "/insert/matrix_curriculum", "insert_control_matrix_curriculum": InsertControlMatrixCurriculum.as_view("insert_matrix_curriculum"),
    "insert_route_building": "/insert/building", "insert_control_building": InsertControlBuilding.as_view("insert_building"),
    "insert_route_academic_period": "insert/academic_period", "insert_control_academic_period": InsertControlAcademicPeriod.as_view("insert_academic_period")

}

app.add_url_rule(["insert_route_teacher"], view_func=["insert_control_teacher"])

#app.add_url_rule(["delete_route_teacher"], view_func=["delete_control_teacher"])

#app.add_url_rule(["update_route_teacher"], view_func=["update_control_teacher"])

#app.register_error_handler(["not_found_route"], ["not_found_control"])
