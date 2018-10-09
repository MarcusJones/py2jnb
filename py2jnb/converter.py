# from IPython.nbformat.v3 import nbpy
# from nbformat.v3 import nbpy
import nbformat
# from IPython import nbformat as nbf

from io import StringIO


def convert(input_string, output_filename):
    """
    Convert a preprocessed string object into notebook file
    """
    # Read using v3
    with StringIO(input_string) as fin:
        nb = nbformat.read(fin, as_version=None)
    # Write using the most recent version
    with open(output_filename, 'w') as fout:
        nbformat.write(nb, fout, version=max(nbformat.versions))
