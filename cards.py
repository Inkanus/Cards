from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, first_name, last_name, email_address,tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_priv = tel_priv
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.occupation}, {self.company}"

    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address})"

    def contact(self):
        return f"Wybieram numer domowy: {self.tel_priv} i dzwonię do {self.first_name} {self.last_name} "
    
    def workcontact(self):
        return f"Wybieram numer służbowy: {self.tel_work} i dzownię do {self.first_name} {self.last_name}"
    
    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name),+1])

    
    

class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation
human_1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_1)
print(human_1.contact())
print(human_1.workcontact())
print(human_1.label_lenght)
print()
human_2 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_2)
print(human_2.contact())
print(human_2.workcontact())
print(human_2.label_lenght)
print()
human_3 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_3)
print(human_3.contact())
print(human_3.workcontact())
print(human_3.label_lenght)
print()
human_4 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_4)
print(human_4.contact())
print(human_4.workcontact())
print(human_4.label_lenght)
print()
human_5 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(human_5)
print(human_5.contact())
print(human_5.workcontact())
print(human_5.label_lenght)
print()

def create_contacts(kind, how_many):


    contacts= []
    for i in range(how_many):
        if kind == 'b':
            how_many.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job()))
        elif kind == 'd':
            how_many.append(BaseContact(first_name=fake.first_name(),
            last_name=fake.last_name(),
            tel_priv=fake.phone_number()))
    return contacts


if __name__ == "__main__":
    kind = input("Jaki rodzaj wizytówki? b - biznesowa, d - domowa: ")
    how_many = int(input('Proszę podaj liczbę wizytówek do stworzenia '))
    contacts = create_contacts(kind, how_many)
    print(contacts)
