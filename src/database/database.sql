CREATE TABLE IF NOT EXISTS accounts(
    id_accounts int NOT NULL AUTO_INCREMENT,
    username VARCHAR (30) NOT NULL,
    password VARCHAR (100) NOT NULL,
    PRIMARY KEY(id_accounts)
);
CREATE TABLE IF NOT EXISTS course(
    id_course int NOT NULL AUTO_INCREMENT,
    full_n_course VARCHAR (30) NOT NULL,
    short_n_course VARCHAR (20),
    modal_course VARCHAR (20) NOT NULL,
    class_course VARCHAR (20) NOT NULL UNIQUE,
    PRIMARY KEY(id_course)

);

CREATE TABLE IF NOT EXISTS teachers(
    id_teacher int NOT NULL AUTO_INCREMENT,
    full_n_teacher VARCHAR (30) NOT NULL,
    reg_teacher SMALLINT (5) NOT NULL UNIQUE,
    hist_vh_teacher TINYINT (3),
    tittle_teacher VARCHAR (20),
    regime_w_teacher VARCHAR (40),
    d_hiring_teacher date NOT NULL,
    d_close_teacher date,
    status_teacher enum ('ativo','inativo')
    PRIMARY KEY(id_teachers)
);


CREATE TABLE IF NOT EXISTS class(
    id_class int NOT NULL AUTO_INCREMENT,
    institution VARCHAR (50) NOT NULL,
    course VARCHAR (100),
    status_class VARCHAR (20) NOT NULL,
    type_class VARCHAR (20) NOT NULL UNIQUE,
    expected_numb_stud INT (70),
    enrolled_numb_stud INT(70),
    semester FLOAT (6),
    matrix_curriculum VARCHAR(100),
    turn_class VARCHAR(20),
    series_class VARCHAR(20),
    PRIMARY KEY(id_class)
);

CREATE TABLE IF NOT EXISTS building(
    id_name int NOT NULL AUTO_INCREMENT,
    adress VARCHAR(100),
    PRIMARY KEY(id_name)
);

CREATE TABLE IF NOT EXISTS plannings(
    id int NOT NULL AUTO_INCREMENT,
    semester FLOAT(6),
    class VARCHAR(15),
    discipline VARCHAR(20),
    teacher VARCHAR(30),
    workload FLOAT(10),
    modalit_offering VARCHAR(30),
    status VARCHAR(10),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS academic_period(
    academic_period_name FLOAT,
    date_start DATE,
    date_end DATE,
    academic_period_description VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS institution_academy(
    company_name VARCHAR(50),
    institution_name VARCHAR(50),
    headquarters VARCHAR(15),
    branch VARCHAR(15),
    courses VARCHAR(30),
    PRIMARY KEY(company_name)

);

CREATE TABLE IF NOT EXISTS discipline(
    id_discipline int NOT NULL AUTO_INCREMENT,
    name_discipline VARCHAR(30),
    discipline_workload_teory TIME,
    discipline_workload_practice TIME,
    discipline_workload_online TIME,
    discipline_workload_total TIME,
    PRIMARY KEY(id_discipline)
);

CREATE TABLE IF NOT EXISTS matrix_curriculum(
    id_matrix_curriculum int NOT NULL AUTO_INCREMENT,
    date_start DATE,
    course VARCHAR(30),
    PRIMARY KEY(id_matrix_curriculum)
)    id_course int NOT NULL AUTO_INCREMENT,
    full_n_course VARCHAR (30) NOT NULL,
    short_n_course VARCHAR (20),
    modal_course VARCHAR (20) NOT NULL,
    class_course VARCHAR (20) NOT NULL UNIQUE,
    PRIMARY KEY(id_course)

);
