from lambda_function import lambda_handler

def test_lambda():
    result = lambda_handler({}, {})

    assert result["statusCode"] == 200