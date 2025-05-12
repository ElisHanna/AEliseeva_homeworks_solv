import logging
import pytest
import requests
from api_actions import ApiActions
from api_project.test_data import TestData as TD


logger = logging.getLogger()


def test_get_token():
    request = ApiActions()
    response = requests.post(
        url=f'{request.url}auth',
        headers=request.header,
        json=request.login_data
        )
    assert response.status_code == 200
    logger.info('Token is successfully created')


def test_create_new_booking():
    request = ApiActions()
    new_booking = request.create_booking(TD.new_booking_body)
    assert new_booking.status_code == 200
    logger.info('Status code is 200')
    assert request.is_response_schema_correct(new_booking, request.new_booking_schema)
    logger.info('Got schema matches with expected')


def test_get_new_booking():
    request = ApiActions()
    new_booking = request.create_booking(TD.new_booking_body)
    new_id = new_booking.json()["bookingid"]
    booking = request.get_booking(new_id)
    assert booking.status_code == 200
    logger.info('Status code is 200')
    assert request.is_response_schema_correct(booking, request.common_booking_schema)
    logger.info('Got schema matches with expected')


def test_update_booking():
    request = ApiActions()
    booking = request.create_booking(TD.new_booking_body)
    token = request.create_token()
    id = booking.json()["bookingid"]
    upd_booking = request.update_booking(token, id, TD.put_upd_body)
    assert upd_booking.status_code == 200
    logger.info('Status code is 200')
    assert request.is_response_schema_correct(upd_booking, request.common_booking_schema)
    logger.info('Got schema matches with expected')


def test_part_update_booking():
    request = ApiActions()
    booking = request.create_booking(TD.new_booking_body)
    token = request.create_token()
    id = booking.json()["bookingid"]
    upd_booking = request.part_update_booking(token, id, TD.patch_upd_body)
    assert upd_booking.status_code == 200
    logger.info('Status code is 200')
    assert request.is_response_schema_correct(upd_booking, request.common_booking_schema)
    logger.info('Got schema matches with expected')


def test_delete_booking():
    request = ApiActions()
    booking = request.create_booking(TD.new_booking_body)
    token = request.create_token()
    id = booking.json()["bookingid"]
    delete = request.delete_booking(token, id)
    assert delete.status_code == 201
    logger.info('Status code is 200')


def test_get_booking_doesnt_exist():
    request = ApiActions()
    booking = request.get_booking('000')
    assert booking.status_code == 404
    logger.info('Booking with such ID does not exist')


def test_delete_booking_without_auth():
    request = ApiActions()
    token = None
    delete = request.delete_booking(token, '1')
    assert delete.status_code == 403
    logger.info('Status code is 403')


@pytest.mark.xfail
def test_delete_booking_doesnt_exist():
    request = ApiActions()
    token = request.create_token()
    delete = request.delete_booking(token, '000')
    assert delete.status_code == 404
    logger.info('Status code is 404')
