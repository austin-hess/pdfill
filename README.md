### pdfill

This is really just a working POC for filling static PDF forms. Needs to be refactored into a meaningful API.

The bulk of the work is in parse_request to turn a JSON request (example is request.json) into a dictionary that can be transformed into meaningful input for the library "pdfformfields"
methods "fill_form_fields" and "generate_dictionary". Docs for these methods can be found here: https://pypi.org/project/pdfformfields/
