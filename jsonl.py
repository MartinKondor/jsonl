from typing import Any, List
import json


class jsonl:
    
    @staticmethod
    def load(file_name: str) -> List[Any]:
        """
        Loads data from a JSONL file into a list.
        
        Args:
            file_name (str): The name of the JSONL file.
        
        Returns:
            List[Any]: List containing the loaded data.
        """
        with open(file_name, "r") as file:
            jsonl_data = [json.loads(line) for line in file.read().splitlines()]
        return jsonl_data

    @staticmethod
    def dump(data: List[Any], file_name: str) -> None:
        """
        Writes data to a JSONL file.
        
        Args:
            data (List[Any]): The data to be written to the file.
            file_name (str): The name of the JSONL file.
        """
        with open(file_name, "w+") as file:
            for row in data:
                file.write(json.dumps(row))
                file.write("\n")

    @staticmethod
    def append(obj: Any, file_name: str) -> None:
        """
        Appends data to an existing JSONL file.
        
        Args:
            obj (Any): The data to be appended to the file.
            file_name (str): The name of the JSONL file.
        """
        with open(file_name, "a") as file:
            file.write(json.dumps(obj))
            file.write("\n")

    @staticmethod
    def dumps(data: List[Any], indent: int=0) -> None:
        """
        Serializes data to a JSON formatted str.
        
        Args:
            data (List[Any]): The data to be serialized.
            indent (int): The indentation level in the JSON output (default: 2).
        
        Returns:
            str: The JSON serialized string.
        """
        return json.dumps(data, indent=indent)

    @staticmethod
    def print(data: List[Any]) -> None:
        """
        Prints JSON formatted data to the console.
        
        Args:
            data (List[Any]): The data to be printed.
        """
        print(jsonl.dumps(data, 2))


if __name__ == "__main__":
    a = [
        {"first_name": "Joe1", "last_name": "Doe1"},
        {"first_name": "Joe2", "last_name": "Doe2"},
        {"first_name": "Joe3", "last_name": "Doe3"},
    ]
    jsonl.dump(a, "temp.jsonl")
    
    obj = {"first_name": "Joe_Appended", "last_name": "Doe_Appended"}
    jsonl.append(obj, "temp.jsonl")

    data = jsonl.load("temp.jsonl")
    jsonl.print(data)
