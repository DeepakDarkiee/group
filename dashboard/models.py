from django.db import models
from datetime import date 

gender=(
    ('Male','Male'),
    ('Female','Female'),
)
reference=(
    ('facebook','facebook'),
    ('instagram','instagram'),
    ('linkain','linkain'),
    ('twitter','twitter'),
    ('other','other'),
    ('people','people'),
)
state=(
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Asom (Assam)','Asom (Assam)'),
('Bihar','Bihar'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Chhattisgarh','Chhattisgarh'),
('Uttar Pradesh','Uttar Pradesh'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu and Kashmir','Jammu and Kashmir'),
('Jharkhand','Jharkhand'),
('West Bengal','West Bengal'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Orissa','Orissa'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttarakhand (Uttaranchal)','Uttarakhand (Uttaranchal)'),
)
blood_group=(

    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
)
position=(

    ('Beginner','Beginner'),
    ('Intermediate','Intermediate'),
    ('Expert','Expert'),
)


# Create your models here.
class Intern(models.Model):  
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    intern_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.CharField(max_length=10,blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.DateField(blank= True,null=True)
    blood_group =  models.CharField(max_length=100, choices=blood_group,null=True)   
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100, choices=state,null=True)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    document_zip = models.FileField(upload_to='media/',blank=True,null=True) 

    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_year =models.CharField(max_length=4,blank=True,null=True,default=True)
        
    def __str__(self): 
         return self.intern_name

class InternAttendance(models.Model):
    intern_name= models.ForeignKey('Intern',on_delete=models.CASCADE,default=True)
    attendance = models.CharField(max_length=100) 
    date=models.CharField(max_length=100,default=date.today().strftime("%d-%m-%Y"), blank=True) 

    def __str__(self): 
        return str(self.intern_name)




class Trainer(models.Model):  
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    trainer_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 

    aadhar_no = models.IntegerField()   
    pan_card = models.CharField(max_length=10,blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.DateField(blank= True,null=True)
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)

    document_zip = models.FileField(upload_to='media/',blank=True,null=True) 


    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.CharField(max_length=4,blank=True,null=True,default=True)
    
    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.CharField(max_length=4,blank=True,null=True,default=True)
    

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.CharField(max_length=4,blank=True,null=True,default=True)

    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year =models.CharField(max_length=4,blank=True,null=True,default=True)
    
    
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_year =models.CharField(max_length=4,blank=True,null=True,default=True)
    

    skill = models.CharField(max_length=100,blank=True,null=True)
    position = models.CharField(max_length=100, choices=position,null=True)
    experience = models.CharField(max_length=100,blank=True,null=True)

    company_name = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=100,blank=True,null=True)
    contact_no = models.IntegerField(blank=True,null=True) 
    emails = models.EmailField(max_length=100,blank=True,null=True) 
    refference = models.CharField(max_length=100,blank=True,null=True)
    relationships = models.CharField(max_length=100,blank=True,null=True)
    belongs_department= models.CharField(max_length=100,blank=True,null=True)
    joining_date = models.CharField(max_length=100) 
    living_date =  models.CharField(max_length=100) 

    def __str__(self): 
        return str(self.trainer_name)


class TrainerAttendance(models.Model):
    trainer_name= models.ForeignKey('Trainer',on_delete=models.CASCADE,default=True)
    attendance = models.CharField(max_length=100, default='absent') 
    date=models.CharField(max_length=100,default=date.today().strftime("%d-%m-%Y"), blank=True) 

    def __str__(self): 
        return str(self.trainer_name)



class Trainee(models.Model):
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    trainee_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.CharField(max_length=10,blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.DateField(blank= True,null=True)
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True)   
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100)  
    join_date = models.CharField(max_length=100)

    document_zip = models.FileField(upload_to='media/',blank=True,null=True) 


    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    high_school_name = models.CharField(max_length=100,blank=True,null=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True)
    high_school_passing_year =models.CharField(max_length=4,blank=True,null=True,default=True)

    graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    graduation_year =models.CharField(max_length=4,blank=True,null=True,default=True)

    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True)
    post_graduation_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    other_degree = models.CharField(max_length=100,blank=True,null=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True)
    other_year =models.CharField(max_length=4,blank=True,null=True,default=True)
 

    def __str__(self): 
       return str(self.trainee_name)


class TraineeAttendance(models.Model):
    trainee_name= models.ForeignKey('Trainee',on_delete=models.CASCADE,default=True)
    attendance = models.CharField(max_length=100, default='absent') 
    date=models.CharField(max_length=100,default=date.today().strftime("%d-%m-%Y"), blank=True) 

    def __str__(self): 
        return str(self.trainee_name)

 

class Employee(models.Model):  
    profile = models.FileField(upload_to='media/',blank=True,null=True)  
    emp_name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField()   
    pan_card = models.CharField(max_length=10,blank=True,null=True)   
    gender = models.CharField(max_length=100, choices=gender,null=True)  
    date_of_birth = models.DateField(blank= True,null=True)
    blood_group = models.CharField(max_length=100,blank=True,null=True)  
    father_name = models.CharField(max_length=100,default=True)  
    father_occupation = models.CharField(max_length=100,blank=True,null=True)  
    father_no = models.IntegerField(blank=True,null=True,default=True)   
    city = models.CharField(max_length=100,default=True)  
    state = models.CharField(max_length=100,default=True)  
    pin_code = models.IntegerField(blank=True,null=True)   
    address = models.CharField(max_length=100,default=True)  
    join_date = models.CharField(max_length=100,default=True)

    document_zip = models.FileField(upload_to='media/',blank=True,null=True) 

    
    school_name = models.CharField(max_length=100,blank=True,null=True)
    board = models.CharField(max_length=100,blank=True,null=True)
    passing_year =models.CharField(max_length=4,blank=True,null=True,default=True)

    high_school_name = models.CharField(max_length=100,blank=True,null=True,default=True)
    high_school_board = models.CharField(max_length=100,blank=True,null=True,default=True)
    high_school_passing_year =models.CharField(max_length=4,blank=True,null=True,default=True)
    
 
    graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    graduation_year =models.CharField(max_length=4,blank=True,null=True,default=True)
    
    post_graduation_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    post_graduation_year =models.CharField(max_length=4,blank=True,null=True,default=True)

     
    other_degree = models.CharField(max_length=100,blank=True,null=True,default=True)
    other_univercity = models.CharField(max_length=100,blank=True,null=True,default=True)
    other_year = models.CharField(max_length=4,blank=True,null=True,default=True)

    skill = models.CharField(max_length=100,blank=True,null=True,default=True)
    position = models.CharField(max_length=100, choices=position,null=True)  
    # position = models.CharField(max_length=100,blank=True,null=True,default=True)
    experience = models.CharField(max_length=100,blank=True,null=True,default=True)

    company_name = models.CharField(max_length=100,blank=True,null=True,default=True)
    designation = models.CharField(max_length=100,blank=True,null=True,default=True)
    contact_no = models.IntegerField(blank=True,null=True,default=True) 
    emails = models.EmailField(max_length=100,blank=True,null=True,default=True) 
    refference = models.CharField(max_length=100,blank=True,null=True,default=True)
    relationships = models.CharField(max_length=100,blank=True,null=True ,default=True)
    belongs_department= models.CharField(max_length=100,blank=True,null=True ,default=True)
    joining_date = models.CharField(max_length=100,default=True) 
    living_date =  models.CharField(max_length=100,default=True) 

    def __str__(self): 
        return str(self.emp_name)


class EmployeeAttendance(models.Model):
    emp_name= models.ForeignKey('Employee',on_delete=models.CASCADE,default=True)
    attendance = models.CharField(max_length=100) 
    date=models.CharField(max_length=100,default=date.today().strftime("%d-%m-%Y"), blank=True) 

    def __str__(self): 
        return str(self.emp_name)


 
class Payroll(models.Model):
    emp_name= models.ForeignKey('Employee',on_delete=models.CASCADE)
    salary = models.IntegerField() 
    tds =  models.CharField(max_length=100) 
    basic = models.IntegerField() 
    pf = models.IntegerField()   
    da =  models.IntegerField()   
    prof_tax =  models.IntegerField() 
    hra =  models.IntegerField() 
    ta = models.IntegerField() 
    deductions =  models.CharField(max_length=100)  
    medical_allowance =  models.IntegerField() 
    other = models.IntegerField() 
    net_salary =  models.IntegerField()  
    sub_total =  models.IntegerField() 
   

 

    def __str__(self): 
        return str(self.emp_name)
       

 


class Staff(models.Model):  
    staff_id= models.CharField(max_length=20,unique=True,null=True)
    staff_name = models.CharField(max_length=100)  
    phone_no = models.IntegerField() 
    aadhar_no = models.IntegerField(blank=True,null=True)   
    role = models.CharField(max_length=100)    
    join_date = models.CharField(max_length=100)
    
    def __str__(self): 
        return str(self.staff_name)


class StaffAttendance(models.Model):
    staff_name= models.ForeignKey('Staff',on_delete=models.CASCADE,default=True)
    attendance = models.CharField(max_length=100) 
    date=models.CharField(max_length=100,default=date.today().strftime("%d-%m-%Y"), blank=True) 

    def __str__(self): 
        return str(self.staff_name)


# ######################################lead#####################################################################

class Lead(models.Model):    
    name = models.CharField(max_length=100)  
    email = models.EmailField(max_length=100) 
    regarding = models.CharField(max_length=100,blank=True,null=True,default=True)
    reference = models.CharField(max_length=100, choices=reference,null=True) 
    message = models.CharField(max_length=100,blank=True,null=True,default=True)    

    def __str__(self): 
        return str(self.name)