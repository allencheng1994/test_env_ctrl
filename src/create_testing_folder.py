from pathlib import Path
import json

DEFAULT_CONFIG = Path(__file__).parent.joinpath("default_config.json")


def create_folders_with_default(project_path: Path, quant: int = 1) -> None:
    """Create the folders by using the default settings

    Create the folders by using the default settings.
    The default folder's layout is stored in src/default_config.json

    Args:
        project_path(Path): The path you want to place your tested folder
        quant(int): Because of unique layout in defult, create the samples by using
        this argument.

    Returns:
        None: It won't retun anything, but it will create a bunch of folders

    """
    with open(DEFAULT_CONFIG, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    config_data["struct_1"]["quant"] = quant
    struct_list = restruct_testcase(config_data)
    for struct in struct_list:
        make_folders(project_path, struct)


def create_folders_with_config(project_path: Path, config_file: Path) -> None:
    """Create the folders with the settings in the configure file

    Create the folder by using custom configure file. You can reference
    src/default_config.json to create your own configure file.

    Args:
        project_path(:obj:`pathlib.Path`): The path you want to place your tested folder
        config_file(:obj:`pathlib.Path`): The configure file

    Returns:
        None: It won't retun anything

    """

    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    struct_list = restruct_testcase(config_data)
    for struct in struct_list:
        make_folders(project_path, struct)


def restruct_testcase(config: dict) -> list[dict]:
    """Convert the 'quant' to the structure

    In this function, we are going to convert 'quant' in config into the
    'struct'

    Args:
        config(dict): The folder's layers config. You can reference 
        src/default_config.json

    Return:
        list: A list of the folder with layers written in dictionary type

    """
    last_case_num = 0
    result = []
    for struct in config:
        go_to_create = (
            config.get(struct).get("quant")
            if config.get(struct).get("quant") != None and config.get(struct) != 0
            else 1
        )
        new_struct = config.get(struct)
        if new_struct.get("quant") != None:
            new_struct.pop("quant")
        for i in range(go_to_create):
            result.append({"testcase_" + str(last_case_num + i + 1): new_struct})
        last_case_num += go_to_create
    return result


def make_folders(project_path: Path, item_struct: dict) -> None:
    """Create the folders by using a specific dictionary
    
    This function can help your create a bunch of folders by using a specific 
    dictionary. The dictionary template is in src/default_config.json

    """
    for item in item_struct:
        created_path = project_path.joinpath(item)
        if not created_path.exists():
            created_path.mkdir()
        if item_struct.get(item) != {} and type(item_struct.get(item) != "dict"):
            make_folders(created_path, item_struct.get(item))


if __name__ == "__main__":
    test_place = Path(r"/Users/chengcl1994/Documents/code/python/test_env_ctrl")
    config = test_place.joinpath("config.json")
    create_folders_with_config(test_place, config)
