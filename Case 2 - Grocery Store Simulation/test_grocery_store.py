import grocery_store as gc

def test_computeCheckoutTime():
    assert gc.computeCheckoutTime([5,3,4], 1) == 12, "Should be 12"
    assert gc.computeCheckoutTime([10,2,3,3], 2) == 10, "Should be 10"
    assert gc.computeCheckoutTime([2,3,10], 2) == 12, "Should be 12"

def run_all_tests():
    test_computeCheckoutTime()
    print("All tests passed")

run_all_tests()