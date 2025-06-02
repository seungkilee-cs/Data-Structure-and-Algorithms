import unittest


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # --- Add specific tests here ---

    # To add all tests from a specific test file (module):
    suite.addTests(loader.loadTestsFromName("tests.graph.dfs.test_matrix_dfs"))

    # To add a specific test class:
    # suite.addTests(loader.loadTestsFromName('tests.graph.dfs.test_matrix_dfs.TestMatrixDFS'))

    # To add a specific test method:
    # suite.addTests(loader.loadTestsFromName('tests.graph.dfs.test_matrix_dfs.TestMatrixDFS.test_examples'))

    # To add multiple test files/classes/methods, just repeat the above lines.

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with appropriate code (optional, for CI)
    exit_code = 0 if result.wasSuccessful() else 1
    exit(exit_code)


if __name__ == "__main__":
    main()
