class TestData:
    new_booking_body = {
        "firstname": "Annie",
        "lastname": "Profit",
        "totalprice": 245,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-05-22",
            "checkout": "2025-06-17"
        },
        "additionalneeds": "Breakfast"
    }

    put_upd_body = {
        "firstname": "Galina",
        "lastname": "Kindermoerder",
        "totalprice": 339,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-07-20",
            "checkout": "2025-07-06"
        },
        "additionalneeds": "Breakfast"
    }

    patch_upd_body = {
        "firstname": "Eddy",
        "lastname": "Murphy",
    }
