from privileges import Admin

admin = Admin(first_name='Bello',
              last_name='Ruky',
              age=25,
              privileges=['add', 'delete'])

admin.show_privileges()

