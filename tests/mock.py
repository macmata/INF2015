from builder.quote import (Driver, Car, Contract, Moto)

def mock_driver(
    birthday, city, province, gender, date_end_of_driving_lessons,
    driving_lessons_caa, first_contract, oiq_member
):
    driver = Driver()
    driver.birthday = birthday
    driver.city = city
    driver.province = province
    driver.gender = gender
    driver.date_end_of_driving_lessons = date_end_of_driving_lessons
    driver.driving_lessons_caa = driving_lessons_caa
    driver.first_contract = first_contract
    driver.oiq_member = oiq_member

    return driver

def mock_contract(length, starting_date):
    contract = Contract()
    contract.length = length
    contract.starting_date = starting_date

    return contract

def mock_car(
    year, make, model, option_value, chiseling, interior_garage,
    alarm
):
    car = Car()
    car.year = year
    car.make = make
    car.model = model
    car.option_value = option_value
    car.chiseling = chiseling
    car.interior_garage = interior_garage
    car.alarm = alarm

    return car

def mock_moto(
    year, make, model, option_value, chiseling, interior_garage,
    alarm
):
    moto = Moto()
    moto.year = year
    moto.make = make
    moto.model = model
    moto.option_value = option_value
    moto.chiseling = chiseling
    moto.interior_garage = interior_garage
    moto.alarm = alarm

    return moto
