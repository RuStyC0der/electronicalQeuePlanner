import configparser
from datetime import timedelta

import pymysql

from src.utils.Exceptions import MyltipleDefinitionInDatabaseException
from src.utils.Singleton import Singleton


class DataBaseConnection(Singleton):

    DUPLICATE_ERROR_CODE = 1062
    CONFIG_PATH = "./Config.ini"

    def __init__(self):

        config = configparser.ConfigParser()
        config.read(self.CONFIG_PATH)

        host = config["Database"]["host"]
        user = config["Database"]["user"]
        password = config["Database"]["password"]
        database = config["Database"]["database"]

        self.connection = pymysql.connect(host, user, password, database,)
        self.cursor = self.connection.cursor()


    def getResultOfQuery(self, query, only_one=True):
        # print(query)
        conutOfQery = self.cursor.execute(query)

        if (conutOfQery == 1):
            return self.cursor.fetchone()[0]
        elif (conutOfQery == 0):
            # print("False on: " + query)
            return False
        else:
            if (only_one):
                raise MyltipleDefinitionInDatabaseException(query)
            return self.cursor.fetchall()


    def __del__(self):
        try:
            self.cursor.close()
            self.connection.close()
        except:
            pass

    def checkIfDayIsWork(self, date, commission_id):
        return self.getResultOfQuery(
            f"select id from custom_schedule where date = '{date}' and commission_id = {commission_id};")

    def checkIfHasTime(self, day, time):
        raise NotImplemented

    def getCommissionIdByName(self, name):
        result = self.getResultOfQuery(f"select id from commission where name = '{name}'")
        return result

    def getFacultyIdByName(self, name):
        result = self.getResultOfQuery(f"select id from faculty where name = '{name}'")
        return result

    def getCommissionFacutyIdByCommissionAndFacultyId(self, commission_id, faculty_id):
        sql = f"select id from commission_faculty where commission_id = {commission_id} and faculty_id = {faculty_id}"
        result = self.getResultOfQuery(sql)
        return result

    def getCommissionIdByCommissionFacutyId(self, commission_faculty_id):
        sql = f"select commission_id from commission_faculty where id = {commission_faculty_id}"
        result = self.getResultOfQuery(sql)
        return result

    def getFacultyIdByCommissionFacultyId(self, commission_faculty_id):
        sql = f"select faculty_id from commission_faculty where id = {commission_faculty_id}"
        result = self.getResultOfQuery(sql)
        return result

    def getUsedTimes(self, preferred_date, commission_faculty_id):

        sql = f"SELECT preferred_time from form where commission_faculty_id = {commission_faculty_id} and preferred_date = '{preferred_date}'"
        result = self.getResultOfQuery(sql, only_one=False)
        return result

    def getAvailableTime(self, preferred_date, commission_faculty_id):
        # TODO may be this not working!!!
        usedTimesTupleInTuple = self.getUsedTimes(preferred_date, commission_faculty_id)

        commission_id = self.getCommissionIdByCommissionFacutyId(commission_faculty_id)
        faculty_id = self.getFacultyIdByCommissionFacultyId(commission_faculty_id)

        if usedTimesTupleInTuple == False:
            print("return first time")
            return self.getStartTimeOfReception(commission_id=commission_id, date=preferred_date)

        usedTimesSet = {i[0] for i in usedTimesTupleInTuple}

        startTime = self.getStartTimeOfReception(commission_id, date=preferred_date)
        endTime = self.getEndTimeOfReception(commission_id, date=preferred_date)
        reception_interval_in_minutes_int = int(self.getReceptionIntervalByFaculytId(faculty_id))
        reception_interval = timedelta(minutes=reception_interval_in_minutes_int)

        while startTime < endTime:
            if startTime not in usedTimesSet:
                return startTime
            else:
                startTime += reception_interval

        print("time overflow")
        return None




    def getStartTimeOfReception(self, commission_id, date):
        sql = f"select start_time from custom_schedule join schedule s on custom_schedule.schedule_id = s.id where date = '{date}' and commission_id = {commission_id};"
        result = self.getResultOfQuery(sql)
        return result

    def getEndTimeOfReception(self, commission_id, date):
        sql = f"select end_time from custom_schedule join schedule s on custom_schedule.schedule_id = s.id where date = '{date}' and commission_id = {commission_id};"
        result = self.getResultOfQuery(sql)
        return result

    def getReceptionIntervalByFaculytId(self,faculty_id):
        sql = f"SELECT reception_interval_in_minutes from faculty where id = {faculty_id}"
        result = self.getResultOfQuery(sql)
        return result

    def createStudent(self, name, email):
        sql = f"insert into student (name, email) values ('{name}', '{email}')"
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor.lastrowid


    def getAvailableStudent(self, email):
        sql = f"SELECT id from student where email = '{email}'"
        result = self.getResultOfQuery(sql)
        return result

    def getOrCreateStudent(self, name, email):
        id = self.getAvailableStudent(email=email)
        if not id:
            id = self.createStudent(name=name, email=email)
        return id


    def createForm(self, preferred_time, preferred_date, commission_faculty_id, student_id):
        sql = (f"insert into form (preferred_time, preferred_date, commission_faculty_id, student_id) \n"
               f"values\n"
               f"('{preferred_time}', '{preferred_date}', {commission_faculty_id}, {student_id});")
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor.lastrowid

    def updateAvailableForm(self, preferred_time, preferred_date, commission_faculty_id, student_id):

        sql = (f"update form\n"
               f"set\n"
               f" preferred_date = '{preferred_date}',\n"
               f" preferred_time = '{preferred_time}'\n"
               f"where student_id = '{student_id}' and commission_faculty_id = {commission_faculty_id};")
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor.lastrowid

    def createOrUpdateForm(self, preferred_time, preferred_date, commission_faculty_id, student_id):
        try:
            self.createForm(preferred_time, preferred_date, commission_faculty_id, student_id)
        except pymysql.err.IntegrityError as e:
            errorCode = e.args[0]
            if errorCode == self.DUPLICATE_ERROR_CODE:
                self.updateAvailableForm(preferred_time, preferred_date, commission_faculty_id, student_id)


if __name__ == '__main__':


    dbm = DataBaseConnection()

    print(dbm.checkIfDayIsWork('2020-08-26', 1))
    print(dbm.checkIfDayIsWork('2020-08-30', 1))

    print(dbm.getCommissionIdByName("Магистры"))
    print(dbm.getFacultyIdByName("ФИПТ"))



    print(dbm.getReceptionIntervalByFaculytId(1))
    print(type(dbm.getReceptionIntervalByFaculytId(1)))
    print(dbm.getOrCreateStudent("vasa", "por"))
    print(dbm.getAvailableTime("2020-08-26", 1))
    # print(type(dbm.getAvailableTime("2020-08-26", 1)))
    # print(dbm.getLastRegisteredTime("2020-08-26", 10))
    # # print(type(dbm.getAvailableTime("2020-08-26", 10)))
    print("////////////////////////////////")
