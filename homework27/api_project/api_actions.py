import logging
import requests
from loguru import logger
from jsonschema import validate, ValidationError
from env import Env


class ApiActions:

    def __init__(self):
        self.url = Env.url
        self.booking_acts_url = f'{self.url}booking'
        self.header = {
            'Content-Type': 'application/json'
        }
        self.login_data = {
            "username": "admin",
            "password": "password123"
        }

        self.new_booking_schema = {
            "type": "object",
            "properties": {
                "bookingid": {"type": "integer"},
                "booking": {
                    "type": "object",
                    "properties": {
                        "firstname": {"type": "string"},
                        "lastname": {"type": "string"},
                        "totalprice": {"type": "integer"},
                        "depositpaid": {"type": "boolean"},
                        "bookingdates": {"type": "object",
                                         "properties": {
                                            "checkin": {"type": "string"},
                                            "checkout": {"type": "string"}
                                         },
                                         "required": ["checkin", "checkout"]},
                        "additionalneeds": {"type": "string"}
                    },
                    "required": ["firstname", "lastname", "totalprice",
                                 "depositpaid", "bookingdates", "additionalneeds"]
                }
            },
            "required": ["bookingid", "booking"]
        }

        self.common_booking_schema = {
            "type": "object",
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "bookingdates": {"type": "object",
                                 "properties": {
                                    "checkin": {"type": "string"},
                                    "checkout": {"type": "string"}
                                 },
                                 "required": ["checkin", "checkout"]},
                "additionalneeds": {"type": "string"}
            },
            "required": ["firstname", "lastname", "totalprice",
                         "depositpaid", "bookingdates", "additionalneeds"]
        }
        self.logger = logging.getLogger()

    def create_token(self):
        answer = requests.post(url=f'{self.url}auth', headers=self.header, json=self.login_data)
        answer.raise_for_status()
        token = answer.json()['token']
        return token

    def auth_and_get_token(self):
        token = self.create_token()
        header = {
            'Accept': 'application/json',
            'Cookie': f'token={token}'
            }
        return header

    def get_booking(self, id):
        booking_data = None
        try:
            booking_data = requests.get(url=f'{self.booking_acts_url}/{id}', headers=self.header)
            booking_data.raise_for_status()
            return booking_data
        except requests.exceptions.HTTPError as h:
            logger.warning(f'HTTP error occured: {h}')
            return booking_data
        except requests.exceptions.RequestException as r:
            logger.warning(f'Request error occured: {r}')
            return None

    def create_booking(self, body):
        new_booking = None
        try:
            new_booking = requests.post(url=self.booking_acts_url, headers=self.header, json=body)
            new_booking.raise_for_status()
            return new_booking
        except requests.exceptions.HTTPError as h:
            logger.warning(f'HTTP error occured: {h}')
            return new_booking
        except requests.exceptions.RequestException as r:
            logger.warning(f'Request error occured: {r}')
            return None

    def update_booking(self, id, body):
        header = self.auth_and_get_token()
        updated = None
        try:
            updated = requests.put(url=f'{self.booking_acts_url}/{id}', headers=header, json=body)
            updated.raise_for_status()
            return updated
        except requests.exceptions.HTTPError as h:
            logger.warning(f'HTTP error occured: {h}')
            return updated
        except requests.exceptions.RequestException as r:
            logger.warning(f'Request error occured: {r}')
            return None

    def part_update_booking(self, id, body):
        header = self.auth_and_get_token()
        part_updated = None
        try:
            part_updated = requests.patch(
                url=f'{self.booking_acts_url}/{id}',
                headers=header,
                json=body)
            part_updated.raise_for_status()
            return part_updated
        except requests.exceptions.HTTPError as h:
            logger.warning(f'HTTP error occured: {h}')
            return part_updated
        except requests.exceptions.RequestException as r:
            logger.warning(f'Request error occured: {r}')
            return None

    def delete_booking(self, id):
        header = self.auth_and_get_token()
        return requests.delete(url=f'{self.booking_acts_url}/{id}', headers=header)

    def is_response_schema_correct(self, response, exp_schema):
        if not response:
            return False
        try:
            current_schema = response.json()
            validate(current_schema, exp_schema)
            return True
        except ValidationError:
            return False
