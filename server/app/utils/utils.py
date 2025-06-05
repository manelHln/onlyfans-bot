import random
import datetime


def get_birthdate() -> dict:
    today = datetime.date.today()

    latest_birthdate = today.replace(year=today.year - 18)

    random_year = random.randint(1900, latest_birthdate.year)

    if random_year == latest_birthdate.year:
        random_month = random.randint(1, latest_birthdate.month)
        if random_month == latest_birthdate.month:
            random_day = random.randint(1, latest_birthdate.day)
        else:
            # Default to 28 to handle February
            random_day = random.randint(1, 28)
    else:
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  # Default to 28 for simplicity

    return {"year": str(random_year), "month": str(random_month), "day": str(random_day)}
