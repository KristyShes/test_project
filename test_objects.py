import requests
import pytest
import allure

from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from endpoints.patch_object import PatchObject
from endpoints.get_all_objects import GetAllObjects


@allure.feature('Create object')
@allure.story('creativity')
def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
        "name": "windy 123",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])

@allure.feature('Get object')
@allure.story('getting')
def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id)

@allure.feature('Get all objects')
@allure.story('getting')
def test_get_objects():
    get_all_objects_endpoint = GetAllObjects()

@allure.feature('Partition update object')
@allure.story('update')
def test_patch_object(obj_id):
    patch_object_endpoint = PatchObject()
    payload = {
        "name": "Apple MacBook Pro 16"
    }
    patch_object_endpoint.patch_object_by_id(obj_id, payload)
    patch_object_endpoint.check_response_is_200()
    patch_object_endpoint.check_response_name(payload['name'])

@allure.feature('Update object')
@allure.story('update')
def test_update_object(obj_id):
    update_object_endpoint = UpdateObject()
    payload = {
        "name": "windy 123",
        "data": {
            "year": 2024,
            "price": 1925.95,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    update_object_endpoint.update_by_id(obj_id, payload)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_response_name(payload['name'])

@allure.feature('Delete object')
@allure.story('delete')
def test_delete_object(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_by_id(obj_id)
    delete_obj_endpoint.check_response_is_200()
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_404()
