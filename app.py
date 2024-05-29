# ------------------------------ set up logging ------------------------------ #

import logging
import warnings
from rich.logging import RichHandler

# suppress UserWarnings from transformers
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("rich").setLevel(logging.DEBUG)

# ------------------------------------------------- regular imports -------------------------------------------------- #

import flet   as ft                                                                                        # type:ignore
from pydantic import HttpUrl

# -------------------------------------------------- local imports --------------------------------------------------- #

from python.tech_enum           import TechStackEnum                                                       # type:ignore
from python.pydantic_structures import TechStack, DataItem, BadgeProps                                     # type:ignore
from python.ai                  import GITImageProcessor                                                   # type:ignore
from python.utils               import UTILS                                                               # type:ignore
from python.utils               import HandleJson                                                          # type:ignore
from python.tests               import RunTests                                                            # type:ignore

# ------------------------------------------------ editable constants ------------------------------------------------ #

DATA_PATH: str = "src/assets/manifest.json"

# ------------------------------------------------- global variables ------------------------------------------------- #

logger: logging.Logger = logging.getLogger("rich")

# -------------------------------------------------------------------------------------------------------------------- #

def make_tech_stack(badge_prop: str) -> TechStack: # ................................................................. #
    logger.info(f"making tech stack for badge_prop: {badge_prop}")

    for tech_stack in TechStackEnum:
        if tech_stack.value.alt == UTILS.to_snake_case(badge_prop):
            logger.info(f"found matching tech stack: {tech_stack.value}")
            return TechStack(
                text=badge_prop,
                alt=tech_stack.value.alt,
                href=tech_stack.value.href
            ) #                                                                                                 return #

    logger.warning(f"no match found for badge_prop: {badge_prop}")
    return TechStack(text="", alt="", href=HttpUrl(""))  #                                                      return #
# end ................................................................................................ make_tech_stack #

# -------------------------------------------------------------------------------------------------------------------- #

def ux_main(page: ft.Page) -> None: # ................................................................................ #
    page.title                = "JSON Data Viewer"
    page.theme_mode           = ft.ThemeMode.LIGHT
    page.vertical_alignment   = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
# end ........................................................................................................ ux_main #

# -------------------------------------------------------------------------------------------------------------------- #

if __name__ == "__main__": # ......................................................................................... #
    logger.info("starting tests")

    tests = RunTests()

    logger.info("loading model and pre-processor into memory")

    GIT_inst = GITImageProcessor()

    tests.next()
    tests.next(DATA_PATH)
    tests.next(GIT_inst)

    data = HandleJson(DATA_PATH).load()
    logger.debug(f"data loaded: {data}")

    while GITImageProcessor.processor is None or GITImageProcessor.model is None or GITImageProcessor.device is None:
        pass

    logger.info("shutting down model and pre-processor")
    GITImageProcessor.shutdown("shutting down app")

    # ft.app(target=ux_main)
# end .................................................................................................... if __main__ #
