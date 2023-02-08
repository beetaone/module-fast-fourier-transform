from os import getenv

PARAMS = {
    "INPUT_LABEL": getenv("INPUT_LABEL", "vibrations"),
    "SAMPLE_SIZE": int(getenv("SAMPLE_SIZE", 1024)),
}
