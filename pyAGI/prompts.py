from typing import Tuple

from pyAGI.utils import setup_logger, log_header

logger = setup_logger(__name__)

CHAIN_GENERATOR_PROMPT = """
            You are code generation AI proficient in Python.\n
            Your task is to build a '{objective}' console-based Python app.\n 
            {maincontent}.\n
            {outcome}:"""


def get_description_generator_prompt() -> Tuple[str, str, int]:
    log_header(logger, "DESCRIPTION AREA")
    return (
        "Description",
        """
            Your task is to create a concise description for the console-based Python app.\n
            Users will interact with the app in a console terminal.\n
            Use your expertise to envision the app's purpose and functionality.
            """,
        200,
    )


def get_architecture_generator_prompt(description: str) -> Tuple[str, str, int]:
    log_header(logger, "ARCHITECTURE AREA")
    return (
        "Architecture",
        f"""
            Based on the provided app description, create a detailed app architecture.\n
            Outline the components and structure of the code.\n
            Present the app architecture in an ordered list.\n
            Description: {description}
            """,
        350,
    )


def get_ux_flow_generator_prompt(
    description: str, architecture: str
) -> Tuple[str, str, int]:
    log_header(logger, "UX FLOW AREA")
    return (
        "UX Flow",
        f"""
            Based on the app description and architecture outline the app UX flow.\n
            Present the UX flow an ordered list.\n
            Description: {description}\n
            Architecture: {architecture}""",
        400,
    )


def get_code_flow_generator_prompt(
    description: str, architecture: str, ux_flow: str
) -> Tuple[str, str, int]:
    log_header(logger, "CODE FLOW AREA")
    return (
        "Code Flow",
        f"""
            Based on the app description, architecture and UX flow, create a detailed code flow.\n
            Outline the code components and structure.\n
            Present the code flow in an ordered list.\n
            Description: {description}\n
            Architecture: {architecture}\n
            UX Flow: {ux_flow}""",
        400,
    )


def get_coding_steps_generator_prompt(
    description: str, architecture: str, ux_flow: str, code_flow: str
) -> Tuple[str, str, int]:
    log_header(logger, "CODING STEPS AREA")
    return (
        "Coding Steps",
        f"""
            You are provided with the app description, architecture, UX flow, and code flow.\n
            Create an ordered list of coding steps required to build the app.\n
            Exclude environment setup, testing, debugging, and deployment steps.\n
            Description: {description}\n
            Architecture: {architecture}\n
            UX Flow: {ux_flow}\n
            Code Flow: {code_flow}""",
        400,
    )


def get_app_code_generator_prompt(
    description: str, architecture: str, ux_flow: str, code_flow: str, coding_steps: str
) -> Tuple[str, str, int]:
    log_header(logger, "APP CODE AREA")
    return (
        "App Code",
        f"""
            With access to the Python terminal, your task is to write the Python code for the app.\n
            You are given the app description, architecture, code flow, and tasks.\n
            Write the Python code with a main function to execute the app in a console terminal.\n
            Avoid using database for backend storage, instead use in-memory options.
            Exclude environment setup, testing, debugging, and deployment tasks.\n
            Description: {description}\n
            Architecture: {architecture}\n
            UX Flow: {ux_flow}\n
            Code Flow: {code_flow}\n
            Coding Steps: {coding_steps}'""",
        3000,
    )
