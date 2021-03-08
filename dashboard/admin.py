from django.contrib import admin

# Register your models here.
from .models import Intern
admin.site.register(Intern)

from .models import Trainee
admin.site.register(Trainee)


from .models import Trainer
admin.site.register(Trainer)

from .models import Employee
admin.site.register(Employee)

from .models import Staff
admin.site.register(Staff)

from .models import InternAttendance
admin.site.register(InternAttendance)

from .models import TraineeAttendance
admin.site.register(TraineeAttendance)

from .models import EmployeeAttendance
admin.site.register(EmployeeAttendance)

from .models import TrainerAttendance
admin.site.register(TrainerAttendance)

from .models import StaffAttendance
admin.site.register(StaffAttendance)

from .models import Payroll
admin.site.register(Payroll)

from .models import Lead
admin.site.register(Lead)


