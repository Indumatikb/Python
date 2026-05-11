
#1st que
class person:
    registry=[]
    def __init__(self,name):
        self.name=name
        person.registry.append(self)
    @classmethod
    def find(cls,name):
        for obj in cls.registry:
            if obj.name==name:
                return obj
            return None
a=person("indu")
b=person("rahul")
r=person.find("indu")
p=person.find("akash")
if p:
    print("found",r.name)
else:
    print("not found")

#2nd que
class datarange:
    def __init__(self,start_date,end_date):
        self.start_date=start_date
        self.end_date=end_date

    @classmethod
    def from_string(cls,string):
        start, end= string.split( "to" )
        return cls(start,end)
    
    @staticmethod
    def leap_year(year):
        return (year%400==0 or year%4==0 and year%100!=0)
    
dr=datarange.from_string("2024-01-01 to 2024-12-31")
print(dr.start_date)
print(dr.end_date)
print(datarange.leap_year(2021))

#3rd que
class UnitConverter:

    @staticmethod
    def cm_to_inch(cm):
        return cm / 2.54

    @staticmethod
    def kg_to_lb(kg):
        return kg * 2.20462

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        if from_unit == "cm" and to_unit == "inch":
            return cls.cm_to_inch(value)

        elif from_unit == "kg" and to_unit == "lb":
            return cls.kg_to_lb(value)

        else:
            return "Conversion not supported"


print(UnitConverter.convert(10, "cm", "inch"))
print(UnitConverter.convert(5, "kg", "lb"))