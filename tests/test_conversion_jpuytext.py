import os
# from py2jnb.tools import python_to_notebook
import jupytext


# with open(INPUT_PY) as fin:
#     data = fin.read()
#     res = jupytext.reads(data, ext='.py', format_name='percent')
#
# script2 = jupytext.writes(nb, ext='.py', format_name='percent')
# jupytext.writef(res,OUTPUT_IPYNB)

def test_convert():
    print("\nSTART TEST")
    SAMPLE_DIR = os.path.join(os.getcwd(),'samples')

    INPUT_FNAME = 'hello.py'
    BASENAME, _ = os.path.splitext(INPUT_FNAME)
    INPUT_PY = os.path.join(SAMPLE_DIR,INPUT_FNAME)
    print("Input file:",INPUT_PY)
    assert os.path.exists(INPUT_PY)

    OUTPUT_IPYNB = os.path.join(SAMPLE_DIR,BASENAME+".ipynb")
    print("Output file: ", OUTPUT_IPYNB)
    if os.path.exists(OUTPUT_IPYNB):
        os.remove(OUTPUT_IPYNB)

    with open(INPUT_PY) as fin:
        data = fin.read()
        parsed = jupytext.reads(data, ext='.py', format_name='percent')

    jupytext.writef(res,OUTPUT_IPYNB)

def test_cells_convert():
    SAMPLE_DIR = os.path.join(os.getcwd(), 'samples')

    INPUT_FNAME = 'hello_cells.py'
    BASENAME, _ = os.path.splitext(INPUT_FNAME)
    INPUT_PY = os.path.join(SAMPLE_DIR, INPUT_FNAME)
    print("Input file:", INPUT_PY)
    assert os.path.exists(INPUT_PY)

    OUTPUT_IPYNB = os.path.join(SAMPLE_DIR, BASENAME + ".ipynb")
    print("Output file: ", OUTPUT_IPYNB)
    if os.path.exists(OUTPUT_IPYNB):
        os.remove(OUTPUT_IPYNB)

    with open(INPUT_PY) as fin:
        data = fin.read()
        parsed = jupytext.reads(data, ext='.py', format_name='percent')

    jupytext.writef(res, OUTPUT_IPYNB)