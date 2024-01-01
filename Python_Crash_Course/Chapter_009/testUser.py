from Python_Crash_Course.Chapter_009.privilegeAdmin import Admin

admin = Admin(first_name='Sani',
              last_name='Jamil',
              age=15,
              privileges=['add', 'delete', 'post'])

admin.show_privileges()