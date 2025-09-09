# programa de estructura condicional

age = int(input("ingresa tu edad: "))

'''
if age < 18:
    print("eres menor de edad")
elif age >= 18 and age < 60:
    print("eres un adulto")
elif age == 60:
    print("feliz 60 cumpleaños")
else:
    print("eres adulto mayor")
'''

def team_age(age: int) -> str:
    message = "eres adulto mayor"
    if age < 18:
        message = "eres menor de edad"
    elif age >= 18 and age < 60:
        message = "eres un adulto"
    elif age == 60:
        message = "feliz 60 cumpleaños"
    
    return message

print(team_age(age))