from lambda_functions import lambda_handler

def test_lambda():
    result = lambda_handler({}, {})

    assert result["statusCode"] == 200