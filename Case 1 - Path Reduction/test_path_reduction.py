import path_reduction as pr

def test_pathReduc():
    assert pr.pathReduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST"]) == ["WEST"], 'Should be ["WEST"]'
    assert pr.pathReduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"]) == [], 'Should be []'
    assert pr.pathReduc(["NORTH","WEST","SOUTH","EAST"]) == ["NORTH","WEST","SOUTH","EAST"], 'Should be ["NORTH","WEST","SOUTH","EAST"]'

def run_all_tests():
    test_pathReduc()
    print("All tests passed")

run_all_tests()