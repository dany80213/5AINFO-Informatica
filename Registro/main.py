from utils import handle_inputs

students = handle_inputs.read_csv_to_dict("data/studenti.csv")
requests = handle_inputs.read_text_to_list("data/richieste.txt")


def find_id(id):
    for student in students:
        if student["ID"] == id:
            print_student(student)
            return
        
    print_student(id,False)

        


def print_student(data,state=True):
    if state == False:
        print(f"ID {data} non trovato")
        return
    print(f"{data["ID"]} {data["cognome"]} {data["nome"]} {data["classe"]} {data["media"]}")

def find_by_surname(surname):
    for student in students:
        if student["cognome"].lower() == surname.lower():
            print_student(student)
    


def print_class_average(considered_students, average):
    print(f"Studenti considerati: {considered_students}")
    print(f"Media: {average}")

def class_average(classe):
    grades = [student["media"] for student in students if student["classe"].lower() == classe.lower()]
    considered_students = len(grades)
    try:
        average = sum(grades)/considered_students
        print_class_average(considered_students,average)
    except ZeroDivisionError:
        print("Classe non trovata")

    


def main():

    for i in range(3):
        if i == 0:
            print("--- Ricerca per ID ---")
            ids = requests[0].split(",")
            for id in ids:
                find_id(int(id))
        
        if i == 1:
            print(f"--- Ricerca per cognome: {requests[1]} ---")
            find_by_surname(requests[1])

        if i == 2:
            print(f"--- Media della classe {requests[2]} ---")
            class_average(requests[2])



        
        
            

if __name__ == "__main__":
    main()



