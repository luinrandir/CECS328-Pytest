# Tests for PA3 - Crates
# Alex Gonzalez

import pytest
from cecs328pa3 import *


@pytest.mark.parametrize(
    "test_crates, test_toasters, test_washers, test_dryers, expected_result",
    [
        (["tdwwddt", "t", "dwww", "ddww", "wwww"], 3, 5, 4, 3),
        (["dwtd", "td", "td", "ddd", "www"], 2, 1, 1, 1),
        (["d", "t", "w", "wdw", "tdt"], 2, 1, 2, 3),
        (["ddwwtt"], 1, 1, 1, 0),
        (["d"], 21, 22, 23, 1),
        (["d"], 1, 1, 1, 1),
        (
            [
                "twwddwwdtdtdddddwwwtwtttdddwwtdwt",
                "td",
                "wddddwwwwwttwwdwdtddwttdww",
                "ddtttwwwwwwwtttwwdwdwwttdwtwdwwtdwt",
                "wtt",
                "ttdtdtdddwtdtwtwwtwtwwwdwwwtdddtwtd",
                "dwwtwtdwddddt",
                "twtttw",
                "ddttdwwttdtwwdwtddddddwttdddwdtwwwddwddtdw",
                "ddtdddttt",
                "wttdttdddwdttwtww",
                "t",
                "ttwttdtwdtwwd",
                "wdtwdwdttdwwdwdwtwtt",
                "twwwdtttttdwttdttdtdwdwdwwtwdttwwddt",
                "dwtwtwwttdtdwwdwddttwtwwtwtwttdwdtwtwtddwdttt",
                "twtwdddttwtwtdwwwddwdttwwwtddwdtwtdddwd",
                "wtttwwtwwwdwddwtddwwwwdwttwwdttdtdwttw",
                "twtwdddtwddttttddwtddwwtddtwdwtt",
                "wtdwwwddtttwtddtdwwdwwwdtddd",
                "wwwt",
                "ddtttwwdw",
                "ttdwwwwwwwdddttttddwwd",
                "d",
                "dwwwwddwwdddtwtwdttwtdw",
                "tddddtwtttwttttt",
                "dtwwtdwtddddwdddwwwdwwwwwdtdddtdwwdtdddwtd",
                "wdttwwwtwtwt",
                "tdtwwwwwwtwttdtwdddd",
                "dwwwddwddddtttwdwtdwttdtdtdtd",
                "wwdtddtdwdtdwwtdttddwttdwwtwwtwdtwttwwwddtddt",
                "wtdddtttwdtdddwwtddtdwdtdwwdtwttdddwtwtwtttdtdwtd",
                "wdwdddtdddtddtdwtdtdtwwttwtwwwwwtdddwwdddwdtwwt",
                "wdwtdwttdddwwwwtwdddtdtdwdtwwddttt",
                "dtddtttwdtw",
                "dwwddwwdwtdwd",
                "twwtdwdwtwtttwddwttdwtddwtdwwttwddwwtdtttdttddt",
                "ttwtwddtwdwdt",
                "wdwwdddddtwdwwddwdtttwwttdwdwttdwttddttwtdww",
                "tddddwwtdwddd",
                "dtwwdttdttdwwwtdtdwtwwwdwdddtdd",
                "twwwddwtdtdttddtwdtwtdtd",
                "ttttwtdwwwtddwdwddwdwdwdwtwtdtwddttw",
                "dwddtdwwwtdwwwtddtwdtdddtwtdww",
                "dwdwwtwwdddttdwdwtw",
                "wwwtwdddwdtddwddddddwddttdwwt",
                "wtttttttddwwtdwdtd",
                "dwwwddwttwdwtwddtdwddtdddddwddddwwddwdt",
                "dwwwwwdttdtwtwwtttdddwwtwtwwwdt",
                "wdtwtwdwtttwddtwdwwwwwddddddtwdwttw",
            ],
            20,
            20,
            20,
            9,
        ),
    ],
)
def test_cargo(test_crates, test_toasters, test_washers, test_dryers, expected_result):
    assert (
        cargo(test_crates, test_toasters, test_washers, test_dryers) == expected_result
    )
