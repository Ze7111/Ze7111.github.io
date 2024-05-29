# ------------------------------------------------- regular imports -------------------------------------------------- #

import os
from   typing import Any, Callable

# -------------------------------------------------- local imports --------------------------------------------------- #

from .tech_enum           import TechStackEnum                                                             # type:ignore
from .ai                  import GITImageProcessor                                                         # type:ignore
from .utils               import UTILS                                                                     # type:ignore
from .utils               import HandleJson                                                                # type:ignore

# -------------------------------------------------- set up logging -------------------------------------------------- #

import  logging
logger: logging.Logger = logging.getLogger("rich")

# --------------------------------------------------- TESTS ---------------------------------------------------------- #

class RunTests: # .................................................................................................... #
    __all_tests: list[Callable[[Any], None]]


    def __init__(self) -> None: # .................................................................................... #
        logger.info("initializing tests")

        self.__current_test: int = 0
        RunTests.__all_tests = [
            getattr(RunTests, func)
            for func in dir(self)
            if (    func    .startswith("_")
                and func[1] .isdigit()
                and callable(getattr(self, func))
            )
        ]

        RunTests.__all_tests.sort(key=lambda x: int(x.__name__[1:])) # sort tests by number 1..n

        logger.debug(f"all tests: {RunTests.__all_tests}")
    # end ............................................. RunTests ......................................... -> __init__ #

    def next(self, *args, **kwargs) -> None: # ....................................................................... #
        if self.__current_test < len(RunTests.__all_tests):
            RunTests.__all_tests[self.__current_test](self, *args, **kwargs)
            self.__current_test += 1
        else:
            logger.error("all tests completed")
    # end ............................................. RunTests ............................................. -> next #


    def _1(self) -> None: # .......................................................................................... #
        logger.debug("running test_1")

        for data in TechStackEnum:
            assert UTILS.to_snake_case(data.value.text) == data.value.alt, f"{data.value.text} != {data.value.alt}"

        logger.debug("test_1 completed successfully")
    # end ............................................. RunTests ........................................... -> test_1 #

    def _2(self, data_path: str) -> None: # .......................................................................... #
        logger.debug("running test_2")
        data = HandleJson(data_path).load()

        assert isinstance(data, list), (f"failed to load data from {data_path} error:\n--------\n{data}\n--------")

        for item in data:
            for tech_stack in item.tech_stack:
                for tech_stack_enum in TechStackEnum:
                    if tech_stack_enum.value.alt == tech_stack.alt:
                        break
                else:
                    assert False, f"{tech_stack.alt} not found in TechStackEnum"

            for badge_props in item.badge_props:
                for tech_stack_enum in TechStackEnum:
                    if tech_stack_enum.value.text == badge_props.text:
                        break
                else:
                    assert False, f"{badge_props.text} not found in TechStackEnum"

        logger.debug("test_2 completed successfully")
    # end ............................................. RunTests ........................................... -> test_2 #

    def _3(self, GIT_inst: GITImageProcessor) -> None: # ............................................................. #
        logger.debug("running test_3")

        imgs_dir = "src/assets/img/"
        logger.debug(
             "testing image caption generation... with "
            f"{len([img for img in os.listdir(imgs_dir) if img.endswith('.png')])} images"
        )

        for img in os.listdir(imgs_dir):
            if not img.endswith(".png"):
                continue

            img = os.path.join(imgs_dir, img)
            alt = GIT_inst.generate_caption(img)

        assert isinstance(alt, str), (f"failed to generate alt for {img} error:\n--------\n{alt}\n--------")
    # end ............................................. RunTests ........................................... -> test_3 #
