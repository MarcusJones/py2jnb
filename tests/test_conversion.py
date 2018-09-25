import os
from py2nb.converter import convert

def test_convert():
    print("\nSTART TEST")
    PATH_SIMPLE_PY = "/samples/hello.py"
    print("Input file:",os.path.join(os.getcwd()+PATH_SIMPLE_PY ))
    print("Output file: ")
    assert os.path.exists(os.path.join(os.getcwd()+PATH_SIMPLE_PY ))
    assert True

    # consum = consume(resource=resouce_id,
    #                  consumer_account=ocean.web3.eth.accounts[2],test
    #                  provider_account=ocean.web3.eth.accounts[0],
    #                  ocean_contracts_wrapper=ocean
    #                  )
    # assert consum.status_code == 200
