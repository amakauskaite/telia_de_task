import path_reduction as pr


def test_pathReduc():
    assert pr.pathReduc(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    ) == ["WEST"], 'Should be ["WEST"]'
    assert (
        pr.pathReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) == []
    ), "Should be []"
    assert pr.pathReduc(["NORTH", "WEST", "SOUTH", "EAST"]) == [
        "NORTH",
        "WEST",
        "SOUTH",
        "EAST",
    ], 'Should be ["NORTH","WEST","SOUTH","EAST"]'
    assert pr.pathReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]) == [
        "WEST",
        "WEST",
    ], 'Should be ["WEST", "WEST"]'


def test_pathReduc_corner_cases():
    assert pr.pathReduc([]) == [], "Should be []"
    assert pr.pathReduc(["NORTH", "SOUTH", "SOUTH", "NORTH"]) == [], "Should be []"
    assert pr.pathReduc(["NORTH", "SOUTH", "WEST", "NORTH", "SOUTH"]) == [
        "WEST"
    ], 'Should be ["WEST"]'
    assert pr.pathReduc(["EAST"]) == ["EAST"], 'Should be ["EAST"]'
    assert pr.pathReduc(["EAST", "EAST", "EAST", "EAST"]) == [
        "EAST",
        "EAST",
        "EAST",
        "EAST",
    ], 'Should be ["EAST", "EAST","EAST","EAST"]'


def run_all_tests():
    test_pathReduc()
    test_pathReduc_corner_cases()
    print("All tests passed")


run_all_tests()
