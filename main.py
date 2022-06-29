
class Company:

    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):

    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        super().__init__(company_bank, company_name)

    def get_salary(self):
        if self.company_bank < self.salary:
            print("У компании не достаточно средств!")
        else:
            self.company_bank -= self.salary
            print(f'''
            Бюджет банка {self.company_bank}
            Зарплата {self.salary}
            ''')

    def person_info(self):
        print(
            f'''
            {self.last_name} {self.first_name}:
            Выданная зарплата {self.salary}.
            '''
        )


Grand_Master = Company(100000, 'Grand_Master')
Emir = Person(Grand_Master.company_bank, Grand_Master.company_name, 'Emir', 'Orozobekov', 20000)
Emir.get_salary()
Emir.get_salary()
Emir.person_info()