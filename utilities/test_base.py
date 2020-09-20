from utilities.read_files import ReadFiles
from dotenv import load_dotenv
import os


class TestBase:
    TEST_DATA_JSON_FILE_PATH = './resources/test_data.json'
    files_reader = ReadFiles()
    test_data = files_reader.read_json_file(TEST_DATA_JSON_FILE_PATH)

    # Load env variables
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
