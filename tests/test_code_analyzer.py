import ast

from docuhook.code_analyzer import DocstringFinder


def test_finder_identifies_undocumented_functions():
    """
    Sprawdza, czy DocstringFinder poprawnie znajduje funkcje bez docstringów.
    """
    # KROK 1: ARRANGE (Przygotuj dane)
    # Przygotowujemy kod z mieszanką funkcji - z docstringami i bez
    sample_code = """
def function_with_docstring():
    \"\"\"This is a docstring.\"\"\"
    pass

def function_without_docstring():
    # No docstring here
    pass

class MyClass:
    def method_with_docstring(self):
        \"\"\"Another docstring.\"\"\"
        pass
    
    def method_without_docstring(self):
        pass
"""

    finder = DocstringFinder()
    tree = ast.parse(sample_code)
    finder.visit(tree)

    found_function_names = {node.name for node in finder.undocumented_functions}

    expected_names = {"function_without_docstring", "method_without_docstring"}

    assert found_function_names == expected_names
