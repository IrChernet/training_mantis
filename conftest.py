
import pytest
import json
import os.path
from fixture.application import Application


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_path) as open_file1:
            target = json.load(open_file1)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    br_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=br_config['baseUrl'])
#    fixture.session.ensure_login(username=br_config["username"], passw=br_config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
#    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")

