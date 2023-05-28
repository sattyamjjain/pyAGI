import argparse

from pyAGI.pyagi import PyAGI
from pyAGI.utils import setup_logger

logger = setup_logger("pyAGI")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="PyAGI agent for your python app objective"
    )

    parser.add_argument("obj", type=str, help="Objective of the app")
    parser.add_argument(
        "model", type=str, help="open ai model", default="text-davinci-003", nargs="?"
    )
    args = parser.parse_args()
    logger.info(
        f"Running autonomous agent pyAGI for the python app of objective {args.obj}"
    )
    py_agi = PyAGI.create_llm_chain(selected_model=args.model)
    py_agi({"objective": args.obj, "selected_model": args.model})
