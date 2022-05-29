from pathlib import Path
import json

DEFAULT_CONFIG = Path(__file__).parent.joinpath("default_config.json")


def create_folders_with_default(project_path: Path, quant: int = 1):
    with open(DEFAULT_CONFIG, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    config_data["struct_1"]["quant"] = quant
    struct_list = restruct_testcase(config_data)
    for struct in struct_list:
        make_folders(project_path, struct)


def create_folders_with_config(project_path: Path, config_file: Path) -> None:
    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    struct_list = restruct_testcase(config_data)
    for struct in struct_list:
        make_folders(project_path, struct)


def restruct_testcase(config: dict) -> list[dict]:
    last_case_num = 0
    result = []
    for struct in config:
        go_to_create = (
            config.get(struct).get("quant")
            if config.get(struct).get("quant") != None
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
