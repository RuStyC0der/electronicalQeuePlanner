from src.databaseConnector import DataBaseConnection
from src.utils.Singleton import Singleton


class QueueAdd(Singleton):

    def __init__(self, databaseConnection):
        self.database = databaseConnection

    def tryToAddForm(self, formJSON):

        try:

            preferable_date = formJSON["Preferable_date"]

            try:
                commission_id = self.database.getCommissionIdByName(formJSON["Comission"])
                faculty_id = self.database.getFacultyIdByName(formJSON["Faculty"])
            except Exception as e:
                return "data error"

            student_name = formJSON["Responder_FIO"]
            email = formJSON["E-mail"]


            commission_faculty_id = self.database.getCommissionFacutyIdByCommissionAndFacultyId(commission_id=commission_id, faculty_id=faculty_id)

            if not self.database.checkIfDayIsWork(date=preferable_date, commission_id=commission_id):
                return "day is not work"

            preferred_time = self.database.getAvailableTime(preferred_date=preferable_date, commission_faculty_id=commission_faculty_id)
            print("Preferred time: ", preferred_time)

            if not preferred_time:
                return "time is not available"
            else:

                preferred_date = preferable_date

                student_id = self.database.getOrCreateStudent(name=student_name, email=email)
                print("Student id: ", student_id)

                self.database.createOrUpdateForm(preferred_time, preferred_date, commission_faculty_id, student_id)

        except Exception as e:
            return e


if __name__ == '__main__':

    dbm = DataBaseConnection()
    qm = QueueAdd(dbm)
    formJSON = {"Responder_FIO":"VAeSA PR",
        "E-mail":"milletrtyr",
        "Comission":"Магистры",
        "Faculty":"ФИПТ",
        "Preferable_date":"2020-08-26"
        }

    print(qm.tryToAddForm(formJSON))
