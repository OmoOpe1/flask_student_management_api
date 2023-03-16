## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY | ACCESS |
| ------ | ----- | ------------- | ------ |
| *POST* | ```/auth/signup/``` | _Register new user_ | _All users_ |
| *POST* | ```/auth/login/``` | _Login user_ | _All users_ |
| *GET* | ```/students/students/``` | _Fetch students_ | _All users_ |
| *POST* | ```/students/students/``` | _Create a new student_ | _superuser_ |
| *GET* | ```/students/student/{student_id}/``` | _Get specific student_ | _All users_ |
| *PUT* | ```/students/student/{student_id}``` | _Edit student information_ | _All users_ |
| *DELETE* | ```/students/student/{student_id}/``` | _Delete student_ | _superuser_ |
| *GET* | ```/courses/courses``` | _Get courses_ | _All users_ |
| *POST* | ```/courses/courses/``` | _Add a new course_ | _superuser_ |
| *GET* | ```/courses/course/{course_id}/{course_id}/``` | _Get a course_ | _All users_ |
| *GET* | ```/courses/course/{course_id}/students``` | _Get all the students in a course_ | _superuser_ |
