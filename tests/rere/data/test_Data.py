from rere.data.Data import Data


def test_inheritance():

    class A:
        pass

    class B(A, Data):
        pass

    assert isinstance(B(), Data)
