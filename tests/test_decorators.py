from src.decorators import my_function


def test_my_function(capsys):
    print(my_function(2, 1))
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n3\n"


def test_function(capsys):
    print(my_function(2, 2))
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n4\n"


def test_error_function(capsys):
    print(my_function(2, ""))
    captured = capsys.readouterr()
    assert (
        captured.out == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (2, ''), {}\n"
    )


def test_error_my_function(capsys):
    print(my_function(2, {}))
    captured = capsys.readouterr()
    assert (
        captured.out == "my_function error: unsupported operand type(s) for +: 'int' and 'dict'. Inputs: (2, {}), {}\n"
    )
